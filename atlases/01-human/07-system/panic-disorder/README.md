---
schema: human-scale-entry/v1
id: panic-disorder
name: Panic Disorder
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-08
summary: "Panic disorder (2-3% lifetime) involves recurrent unexpected panic attacks driven by LC-NE hyperactivation and amygdala CO2 hypersensitivity; first-line: SSRIs/SNRIs + CBT with interoceptive exposure; benzodiazepines for acute attacks; avoid long-term BZ use."
aliases: ["panic disorder", "panic attack", "agoraphobia", "CO2 hypersensitivity", "Klein suffocation alarm", "interoceptive exposure", "unexpected panic", "anticipatory anxiety"]
sources:
  - id: craske-2007-panic-review
    type: peer-reviewed
    cite: "Craske MG, Barlow DH. Panic disorder and agoraphobia. In: Barlow DH, ed. Clinical Handbook of Psychological Disorders. 4th ed. Guilford; 2007."
    pmid: "17542550"
  - id: gorman-2000-panic-neurobiology
    type: peer-reviewed
    cite: "Gorman JM, Kent JM, Sullivan GM, Coplan JD. Neuroanatomical hypothesis of panic disorder, revised. Am J Psychiatry. 2000;157(4):493-505."
    doi: "10.1176/appi.ajp.157.4.493"
    pmid: "10739407"
    url: "https://doi.org/10.1176/appi.ajp.157.4.493"
    accessed: "2026-06-08"
  - id: nardi-2009-clonazepam-panic
    type: peer-reviewed
    cite: "Nardi AE, Freire RC, Zin WA. Panic disorder and control of breathing. Respir Physiol Neurobiol. 2009;167(1):133-143."
    doi: "10.1016/j.resp.2008.07.011"
    pmid: "18708168"
    url: "https://doi.org/10.1016/j.resp.2008.07.011"
    accessed: "2026-06-08"
cross_links:
  - target: 01-human/03-molecular/norepinephrine
    relation: connects-to
    note: "LC hyperactivation in panic disorder drives tachycardia, chest tightness, and hyperarousal via α1-NE stimulation in amygdala; yohimbine (α2 antagonist) reliably provokes panic in PD patients; propranolol reduces somatic symptoms; clonidine reduces LC firing and hyperarousal."
  - target: 01-human/03-molecular/serotonin
    relation: connects-to
    note: "SSRIs are first-line for panic disorder via raphe-amygdala serotonin modulation of the fear circuit; paradoxical jitteriness requires starting low; paroxetine and sertraline have strong evidence; clomipramine (5-HT/NE TCA) is highly effective but limited by side effects."
  - target: 01-human/03-molecular/gaba
    relation: connects-to
    note: "GABA-A activation by benzodiazepines (clonazepam, alprazolam) rapidly terminates panic attacks; reduced BZ binding in temporal lobe in PD suggests GABAergic deficit; BZDs bridge therapy while SSRIs take effect but avoided long-term due to dependence and impaired extinction."
  - target: 01-human/03-molecular/glutamate
    relation: connects-to
    note: "NMDA receptor activation in BLA mediates fear memory consolidation in panic disorder; excessive glutamate signaling may amplify amygdala hyperreactivity; D-cycloserine (partial NMDA agonist) enhances extinction learning in CBT augmentation trials for panic disorder."
  - target: 01-human/06-organ/brain
    relation: targets
    note: "Panic disorder features BLA hyperreactivity to interoceptive and CO2 stimuli, insula hyperactivation (heightened body awareness), reduced vmPFC control over amygdala, and LC-NE dysregulation; CBT with interoceptive exposure normalizes amygdala-insula reactivity over weeks."
  - target: 01-human/03-molecular/oxytocin
    relation: connects-to
    note: "Oxytocin modulates the BLA fear circuit via OTR on amygdala neurons reducing CRH-driven arousal; LC-NE hyperactivation is partially OT-regulated; intranasal OT reduces fear generalization and behavioral anxiety; may augment interoceptive exposure therapy in panic disorder."
  - target: 03-medicine/01-modern/10-mental-health/fluoxetine
    relation: treated-by
    note: "Fluoxetine is FDA-approved for panic disorder with/without agoraphobia; SSRIs first-line over benzodiazepines; initial paradoxical anxiety (5-HT1A stimulation) requires start-low-go-slow dosing; onset 4–8 weeks; 70–80% response rate; CBT additive with fluoxetine."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "Panic disorder and generalized anxiety disorder are neighboring anxiety disorders that often co-occur and share serotonergic/GABAergic biology and first-line SSRIs, but differ in tempo: panic is paroxysmal terror with autonomic symptoms, GAD sustained free-floating worry."
  - target: 01-human/07-system/social-anxiety-disorder
    relation: connects-to
    note: "Panic disorder and social anxiety disorder are both fear-circuit anxiety disorders treated first-line with SSRIs, but differ in trigger: panic attacks are unexpected and somatic (interoceptive), social anxiety cued by scrutiny; they often coexist, exposure CBT tailored to each."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "Panic attacks originate in fear-circuit neurons: hyperexcitable locus coeruleus and basolateral amygdala neurons fire to interoceptive or CO2 cues, triggering the autonomic surge, while weak prefrontal inhibition fails to restrain them — the target of SSRIs and benzodiazepines."
  - target: 01-human/07-system/ptsd
    relation: connects-to
    note: "Panic disorder and PTSD overlap in fear circuitry: both involve a hyperreactive amygdala and noradrenergic surges, panic attacks are common in PTSD, and they share SSRIs and exposure CBT—but PTSD is anchored to a trauma memory while panic strikes unpredictably."
  - target: 01-human/06-organ/adrenal-gland
    relation: connects-to
    note: "A panic attack is a false alarm of the fight-or-flight axis the adrenal gland serves: surging adrenaline drives palpitations, sweating, and tremor, and because pheochromocytoma produces identical paroxysms, panic with severe hypertension warrants catecholamine testing."
  - target: 01-human/07-system/asthma
    relation: connects-to
    note: "Panic disorder and asthma are tightly comorbid and can mimic each other: breathlessness triggers panic and hyperventilation worsens bronchospasm, while CO2 hypersensitivity links both—so telling an asthma attack from a panic attack matters clinically."
  - target: 01-human/07-system/pheochromocytoma-paraganglioma
    relation: connects-to
    note: "Pheochromocytoma is the classic organic mimic of panic disorder: its catecholamine surges produce sudden palpitations and a sense of doom indistinguishable from a panic attack—so refractory 'panic' with hypertension warrants metanephrine testing to exclude it."
  - target: 01-human/03-molecular/cortisol
    relation: connects-to
    note: "Panic disorder engages the HPA stress axis through cortisol: although the acute attack is driven by adrenaline, chronic anxiety dysregulates cortisol secretion, and the hormone's feedback shapes fear circuits—linking the body's main stress hormone to recurrent panic."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "Panic disorder and depression are highly comorbid and share treatment: most patients with one develop the other, both respond to SSRIs, and co-occurring panic worsens depression's prognosis and suicide risk—so screening for depression is routine in panic disorder."
  - target: 01-human/03-molecular/adenosine
    relation: connects-to
    note: "Adenosine links caffeine to panic attacks: blocking adenosine receptors (as caffeine does) can provoke panic in susceptible people, evidence that the adenosine system modulates anxiety—so caffeine avoidance is part of managing panic disorder."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "Panic disorder masquerades as heart disease: surging adrenaline causes palpitations, chest pain and tachycardia that mimic a heart attack, so panic is a leading reason for emergency cardiac workups—and real cardiac disease must be excluded before diagnosing it."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "Panic disorder may stem from a faulty suffocation alarm: patients are hypersensitive to rising CO2, so air hunger and hyperventilation trigger attacks (and CO2 inhalation can provoke them in the lab)—linking the respiratory system's chemosensing to panic."
  - target: 01-human/03-molecular/orexin
    relation: connects-to
    note: "Orexin links arousal to panic: the orexin (hypocretin) system drives wakefulness and the stress response, and heightened orexin signaling is implicated in panic attacks—suggesting the same neurons that stabilize wakefulness also tune the brain's alarm circuitry."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "Panic disorder is a misfiring of the nervous system's fear circuitry: a hypersensitive amygdala-brainstem alarm triggers a full fight-or-flight surge without real danger, so the body's threat response—racing heart, breathlessness, terror—erupts as a panic attack."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "Panic attacks masquerade as cardiac emergencies: the surge of palpitations, chest pain and breathlessness mimics a heart attack and floods emergency rooms, so panic disorder is a major reason chest pain is evaluated—after truly excluding cardiovascular causes."
  - target: 01-human/03-molecular/epinephrine
    relation: connects-to
    note: "A panic attack is in part an adrenaline storm: surging epinephrine drives the pounding heart, sweating, tremor and chest tightness, which is why panic can mimic a heart attack—and why a catecholamine-secreting pheochromocytoma is on the differential."
  - target: 01-human/02-atomic/carbon
    relation: connects-to
    note: "Panic disorder is tied to carbon dioxide sensing: inhaling CO2 reliably provokes attacks in patients, supporting a 'suffocation false-alarm' theory in which an oversensitive brainstem misreads rising CO2 as suffocation and fires panic."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "Panic's respiratory subtype centers on the lungs: hyperventilation blows off CO2 causing the tingling, lightheadedness and air hunger of an attack, and breathing retraining is a core treatment—linking a psychiatric disorder to respiratory physiology."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Panic attacks tingle because of calcium: hyperventilation blows off CO2 and raises blood pH, which lowers ionized calcium—producing the perioral numbness, hand tingling, and carpopedal spasm that frighten patients mid-attack."
  - target: 01-human/05-tissue/hippocampus
    relation: connects-to
    note: "Panic disorder engages the hippocampus's fear memory: by encoding the context of past attacks, the hippocampus drives anticipatory anxiety and agoraphobic avoidance of places where panic struck, extending the disorder beyond the attacks themselves."
  - target: 01-human/04-cellular/astrocyte
    relation: connects-to
    note: "Astrocytes help tune the panic circuit: by clearing and recycling glutamate and GABA around the amygdala and brainstem, these glial cells shape the excitatory-inhibitory balance whose disturbance can tip neurons into a panic response."
  - target: 01-human/02-atomic/hydrogen
    relation: connects-to
    note: "Panic may be a misfiring suffocation alarm read in acid: rising CO2 turns to carbonic acid, and acid-sensing channels in the amygdala detect the falling pH, triggering the sudden terror and air hunger of an attack—why breathing CO2 can provoke one."
  - target: 01-human/05-tissue/synapse
    relation: connects-to
    note: "Panic disorder is wired into fear-circuit synapses: repeated attacks strengthen connections in the amygdala and its pathways, so neutral cues come to trigger alarm—plasticity that exposure therapy and SSRIs work to reshape."
  - target: 01-human/04-cellular/microglia
    relation: connects-to
    note: "Microglia may stoke the panic-prone brain: chronic stress activates these immune cells to release cytokines that shift the excitatory-inhibitory balance in fear circuits, linking neuroinflammation to vulnerability to panic."
  - target: 01-human/06-organ/thyroid
    relation: connects-to
    note: "An overactive thyroid mimics panic: excess thyroid hormone causes palpitations, sweating, and dread that look just like panic attacks, so thyroid function is checked before settling on the diagnosis."
  - target: 01-human/06-organ/large-intestine
    relation: connects-to
    note: "Panic grips the gut: through the gut-brain axis attacks bring nausea, cramping, and urgent bowel movements, and panic disorder overlaps heavily with irritable bowel syndrome."
  - target: 01-human/04-cellular/cardiomyocyte
    relation: connects-to
    note: "Panic floods heart-muscle cells with adrenaline: the surge drives cardiomyocytes into pounding palpitations and chest pain, and rarely into a transient stress cardiomyopathy, the 'heart attack' feeling of an attack."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Photons expose the panicking brain: functional MRI and PET reveal an overactive amygdala and fear circuit with weak prefrontal restraint, the imaging signature researchers use to map why an attack erupts without real danger."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "Sodium lactate is the classic panic trigger: infusing it into the vein reliably provokes a full attack in patients but not in healthy people, a reproducible challenge test that helped prove panic disorder has a distinct biology."
  - target: 01-human/03-molecular/dopamine
    relation: connects-to
    note: "Dopamine wires panic into avoidance: the reward-and-threat transmitter helps stamp in the fear conditioning that turns a single attack into agoraphobia, as the brain learns to dread and flee the places where panic struck."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "Panic floods to the skin: the sympathetic surge of an attack drives drenching sweat, flushing, and chills, the visible autonomic storm that accompanies the racing heart and breathlessness."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "Magnesium tempers excitability, and its lack feeds anxiety: low magnesium heightens neuronal firing and the stress response, and deficiency is associated with anxiety and panic, making repletion a simple thing to check."
  - target: 01-human/06-organ/stomach
    relation: connects-to
    note: "Panic turns the stomach: the brain-gut axis routes the attack into nausea, churning, and the 'butterflies' of acute fear, and recurrent panic often overlaps with functional gut complaints."
  - target: 01-human/03-molecular/progesterone
    relation: connects-to
    note: "Panic tracks the hormonal tide: its metabolite allopregnanolone tunes the calming GABA receptor, so the premenstrual and postpartum drops in progesterone, like a withdrawal, can unmask or worsen panic attacks in vulnerable women."
  - target: 01-human/07-system/gut-microbiome
    relation: connects-to
    note: "The gut's microbes whisper to the anxious brain: through the microbiome-gut-brain axis they shape GABA, serotonin, and vagal signaling, and the dysbiosis common in panic and its frequent IBS overlap is studied as both consequence and contributor."
  - target: 01-human/04-cellular/platelet
    relation: connects-to
    note: "Platelets offer a peripheral window on the disorder: they take up and store serotonin much as neurons do, so altered platelet serotonin transport and receptor binding have served as accessible research markers of the serotonergic disturbance in panic."
  - target: 01-human/03-molecular/estrogen
    relation: connects-to
    note: "Hormone shifts sway the panic threshold: attacks often cluster premenstrually, postpartum, and around menopause, as falling estrogen modulates the serotonin and fear circuits — part of why panic disorder is roughly twice as common in women."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "Mast cells can mimic a panic attack: in mast cell activation syndrome, surges of histamine and mediators cause flushing, palpitations and a sense of doom indistinguishable from panic, a medical mimic worth excluding in atypical cases."
  - target: 01-human/07-system/insomnia-disorder
    relation: connects-to
    note: "Panic invades sleep: nocturnal panic attacks jolt patients awake in terror, and the resulting fear of sleep feeds an insomnia that worsens daytime anxiety in a self-reinforcing loop."
  - target: 01-human/07-system/alcohol-use-disorder
    relation: connects-to
    note: "Many self-medicate their way into a second illness: people with panic disorder often drink or take sedatives to quell attacks, and the withdrawal rebound itself provokes panic — a vicious loop that makes alcohol use disorder a frequent companion."
  - target: 01-human/07-system/migraine
    relation: connects-to
    note: "The two travel together: panic disorder and migraine are strongly comorbid, sharing serotonergic and autonomic dysregulation, so each roughly doubles the odds of the other and both can flare under the same stressors."
  - target: 01-human/03-molecular/bdnf
    relation: connects-to
    note: "Stress reshapes the fear circuitry: altered BDNF signaling, which governs the synaptic plasticity of the amygdala and hippocampus, is implicated in how chronic stress lowers the threshold for the runaway fear response of a panic attack."
  - target: 01-human/03-molecular/crh
    relation: connects-to
    note: "CRH sets the alarm's sensitivity: the corticotropin-releasing hormone that launches the HPA stress response also acts in the amygdala to heighten fear, and its dysregulation lowers the threshold for the spontaneous surge of a panic attack."
  - target: 01-human/07-system/copd
    relation: connects-to
    note: "Breathlessness and panic feed each other: panic disorder is markedly more common in COPD, where air hunger triggers attacks and CO2-sensitive suffocation alarms misfire, each worsening the other's symptoms and disability."
  - target: 01-human/07-system/stimulant-use-disorder
    relation: connects-to
    note: "Stimulants ignite the panic circuit: caffeine and stimulant drugs provoke the racing heart and hyperarousal that set off attacks, so stimulant use can unmask or worsen panic disorder."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "Chronic alarm leaves an inflammatory mark: the repeated stress responses of panic disorder activate NF-κB-driven cytokine signaling, a low-grade inflammation tied to its physical-health comorbidities."
  - target: 01-human/07-system/bipolar-disorder
    relation: connects-to
    note: "Panic rides with mood instability: panic disorder is over-represented in bipolar disorder, the comorbidity worsening its course and raising suicide risk, a pairing that shapes treatment choices."
  - target: 01-human/07-system/cannabis-use-disorder
    relation: connects-to
    note: "Cannabis cuts both ways with panic: it can acutely trigger panic attacks and, with heavy use and withdrawal, worsen the disorder, even as some users turn to it to self-medicate anxiety."
  - target: 01-human/07-system/hypertension
    relation: connects-to
    note: "Repeated catecholamine surges press on the arteries: each panic attack floods the body with adrenaline and noradrenaline, and the chronic autonomic arousal of panic disorder is linked to higher rates of sustained hypertension."
  - target: 01-human/07-system/heart-failure
    relation: connects-to
    note: "Acute panic can stun the heart: an intense surge of stress hormones during a severe attack can precipitate takotsubo (stress) cardiomyopathy, a transient but real cause of acute heart failure that mimics a heart attack."
  - target: 01-human/07-system/stroke
    relation: connects-to
    note: "Chronic panic tracks with cerebrovascular risk: the autonomic arousal, hypertension and platelet activation tied to panic disorder, plus its overlap with smoking and inactivity, are associated with an elevated long-term risk of stroke."
  - target: 01-human/07-system/obsessive-compulsive-disorder
    relation: connects-to
    note: "Two anxiety-spectrum disorders that travel together: panic disorder frequently coexists with OCD, sharing heightened threat sensitivity and serotonergic dysregulation and responding to overlapping SSRI and CBT treatment."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "Stress hormones drive the attacks: panic is mediated by surges of adrenaline and HPA-axis cortisol, and endocrine disease such as thyrotoxicosis or a phaeochromocytoma can precipitate panic-identical episodes."
  - target: 01-human/07-system/attention-deficit-hyperactivity-disorder
    relation: connects-to
    note: "Frequently comorbid, and treatment can collide: anxiety and panic are common alongside ADHD, and the stimulants used to treat ADHD can provoke or worsen panic attacks, complicating management."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "Panic speaks through the gut: attacks bring nausea and abdominal distress, and panic disorder is strongly comorbid with irritable bowel syndrome through the gut-brain axis."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "Hyperventilation cramps the muscles: the overbreathing of a panic attack causes respiratory alkalosis with carpopedal spasm and tetany, on top of the chronic muscle tension anxiety brings."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "The body sweats and flushes in fear: profuse diaphoresis, flushing and chills are autonomic skin manifestations of a panic attack, mediated by the adrenaline surge."
---

# Panic Disorder

## Overview

**Panic disorder (PD)** is an anxiety disorder characterized by recurrent, unexpected **panic attacks** — abrupt surges of intense fear or discomfort that peak within minutes and include at least four of 13 physical or cognitive symptoms — accompanied by at least one month of either persistent concern about future attacks or maladaptive behavioral change related to attacks.

**Epidemiology:**
- Lifetime prevalence: 2–3% (US and globally); 12-month prevalence ~1.8%
- Female-to-male ratio: 2:1 to 3:1; onset typically late adolescence to early 30s
- High comorbidity: 50–65% comorbid MDD; 30–40% comorbid GAD; 50–65% develop agoraphobia if untreated
- Economic burden: PD is among the most frequent reasons for emergency department visits (chest pain, dyspnea) that ultimately have no cardiac etiology

**DSM-5 Panic Attack — 13 symptoms (requires ≥4):**

| Domain | Symptoms |
|:---|:---|
| **Cardiovascular** | Palpitations, racing heart, chest pain or pressure |
| **Respiratory** | Shortness of breath, choking sensation |
| **Neurological** | Dizziness, unsteadiness, tingling/numbness |
| **Autonomic** | Sweating, trembling, chills or hot flushes |
| **Cognitive** | Derealization/depersonalization, fear of losing control, fear of dying |

**DSM-5 PD Criteria:**
1. Recurrent **unexpected** panic attacks (not all attacks are unexpected; situational attacks common once PD established)
2. ≥1 month of at least ONE of: (a) persistent worry about future attacks or their consequences; (b) significant maladaptive behavioral change (avoidance, reassurance-seeking, dietary restriction)
3. Not better explained by substances, medical conditions, or another mental disorder

**Agoraphobia (separate DSM-5 diagnosis):** Fear and avoidance of situations where escape would be difficult or help unavailable (crowds, public transit, open spaces, being outside home alone); frequently comorbid with PD but can occur independently.

## Structure

### Neuroanatomy of panic

**Gorman's revised fear network model** [^gorman-2000-panic-neurobiology] proposes two interacting circuits:

**Central fear circuit (conditioned fear):**
- **Basolateral amygdala (BLA):** Integrates sensory input and body-state signals; in PD, chronically sensitized → lowers threshold for panic initiation; receives input from thalamus (rapid threat detection), cortex (conceptual appraisal), and hippocampus (contextual memory)
- **Central amygdala (CeA):** Panic output — projects to LC (NE hyperactivation), PAG (autonomic/defensive response), PBN (respiratory alarm), hypothalamus (HPA axis)
- **vmPFC:** Inhibits CeA via intercalated cell GABAergic projections → safety signaling; reduced in PD → failure to suppress BLA-CeA alarm

**Suffocation/CO2 alarm circuit:**
- **Parabrachial nucleus (PBN):** Detects CO2 increases via ASIC1a channels; projects to amygdala and locus coeruleus; the "respiratory panic trigger"
- **Periaqueductal gray (PAG):** Mediates unconditioned defensive responses; dorsal PAG activation → fight-or-flight; patients with PD show heightened PAG-amygdala coupling during CO2 challenge
- **Insula:** Interoceptive awareness — monitors heart rate, respiratory sensations; hyperactivated in PD → catastrophic misinterpretation of bodily sensations

**Norepinephrine circuit:**
- **Locus coeruleus (LC):** CNS NE source; LC → BLA (amplifies fear acquisition and retrieval via α1 receptors); LC → cortex (hyperarousal, vigilance); LC → cardiovascular centers (sympathetic outflow → palpitations)
- Yohimbine (α2-adrenergic antagonist) increases LC firing → provokes panic attacks in >50% of PD patients but rarely in controls

### Klein's suffocation alarm hypothesis

Donald Klein proposed that PD represents a biological **false alarm of suffocation** — the brain misreads CO2 accumulation as asphyxiation risk:
- Inhaled 7.5% CO2 reliably provokes panic in ~70% of PD patients vs. ~10% of controls
- CO2 sensitivity mediated by ASIC1a channels and TASK-1/TASK-3 channels on amygdala neurons
- Individuals with variants in ASIC1a (acid-sensing ion channels) have higher CO2 sensitivity and panic vulnerability
- This explains why hyperventilation (reduces CO2) acutely aborts some panic attacks, and why rebreathing into a paper bag can worsen panic (CO2 retention)
- Respiratory rate as a trait marker: PD patients have mildly elevated basal respiratory rate even between attacks

## Function

### Interoceptive fear conditioning

The **interoceptive fear conditioning model** (Bouton, Mineka, Barlow) explains panic disorder maintenance:

1. **First attack:** Often occurs in the context of stress, caffeine, or physiological perturbation → catastrophic misinterpretation ("I'm dying")
2. **Conditioning:** Interoceptive cues (heart rate elevation, slight breathlessness) become conditioned stimuli for fear responses → body sensations trigger anticipatory fear
3. **Amplification loop:** Anxiety about having a panic attack → sympathetic arousal → increased heart rate → perceived as sign of impending panic → catastrophic appraisal → full panic attack (self-fulfilling prophecy)
4. **Avoidance:** Behavioral change to prevent feared sensations (avoidance of exercise, caffeine, sexual arousal, movies) → negative reinforcement → maintenance

**Clark's cognitive model:**
- Core belief: "Bodily sensations are dangerous and indicate catastrophe"
- Selective attention to interoceptive cues → detection of normal bodily fluctuations → misinterpretation → anxiety → amplified sensations → full panic attack
- Safety behaviors (sitting down, taking pulse, seeking reassurance) prevent disconfirmation of feared catastrophe → perpetuate disorder

### HPA axis and stress sensitization

- Acute cortisol response during panic attacks is modest but present
- Prior stress history (early adversity, life events) sensitizes the HPA axis → lower threshold for panic initiation
- Corticotropin-releasing factor (CRF) receptors in amygdala amplify fear responses; CRF1 antagonists reduce anxiety in preclinical models
- Unlike PTSD (hypocortisolemia), PD typically shows near-normal basal cortisol with exaggerated phasic stress responses

## Pathology

### Panic disorder variants

| Type | Characteristics |
|:---|:---|
| **With agoraphobia** | Avoidance of ≥2 situations; severe functional impairment; may become housebound |
| **Without agoraphobia** | Attacks present; behavioral impact limited; better prognosis |
| **Performance-limited** | Context-dependent panic (overlaps with social anxiety disorder) |
| **Nocturnal panic** | Awaken from sleep in panic; non-REM attacks; not nightmares; strong NE component |
| **Pharmacologically provoked** | Caffeine, cannabis, sympathomimetics, β-agonists lower threshold |

### Differential diagnosis

- **Cardiac arrhythmia:** Holter monitoring; PD diagnosis after cardiac workup often delayed 10+ years
- **Hyperthyroidism:** TSH essential in workup; thyroid storm may resemble severe panic
- **Pheochromocytoma:** Episodic HTN + palpitations; 24h urine catecholamines
- **Hypoglycemia:** Food-related panic attacks; check glucose during attack
- **Epilepsy:** Temporal lobe seizures may produce panic-like experience + automatisms
- **Substance use:** Cocaine, cannabis (particularly high-THC), stimulant withdrawal

### Treatment

**Cognitive-Behavioral Therapy (CBT):**
- Most effective long-term intervention; 55–70% panic-free at 1 year; relapse rate lower than pharmacotherapy alone
- **Components:**
  - **Psychoeducation:** Panic physiology; fight-or-flight; CO2 model; normalization
  - **Cognitive restructuring:** Challenge catastrophic misinterpretations of bodily sensations; decatastrophizing ("heart racing ≠ heart attack")
  - **Breathing retraining:** Diaphragmatic breathing; correct hyperventilation pattern; reduces CO2-mediated provocation
  - **Interoceptive exposure:** Deliberately induce feared sensations in session (spin in chair → dizziness; run in place → palpitations; breathe through narrow straw → breathlessness) → habituation; disrupts interoceptive conditioning
  - **Situational exposure:** Graded exposure to avoided situations (elevators, crowds, public transit) with agoraphobia
- **Combination > monotherapy:** CBT + pharmacotherapy superior in short-term; CBT alone superior at 2-year follow-up (durability)

**First-line pharmacotherapy:**

| Medication | Class | Notes |
|:---|:---|:---|
| Sertraline | SSRI | Flexible dosing; well-tolerated |
| Paroxetine | SSRI | Also reduces anticipatory anxiety; discontinuation syndrome risk |
| Escitalopram | SSRI | Fewest drug interactions |
| Fluoxetine | SSRI | Long half-life; "start low" — jitteriness risk |
| Venlafaxine XR | SNRI | NE component may address physical symptoms |
| Clomipramine | TCA | Among most effective; limited by side effects (anticholinergic, QTc) |
| Imipramine | TCA | Historical gold standard; now third-line |

**Benzodiazepines:**
- **Clonazepam, alprazolam:** Rapid onset; highly effective for acute attacks; useful as bridging therapy during SSRI initiation (reduces early jitteriness)
- **Limitations:** Dependence; impair fear extinction learning (GABA-A-mediated amnesia); long-term use may worsen course; taper required for discontinuation
- **Appropriate use:** PRN for situational anticipatory anxiety; short-term bridge (4–6 weeks); avoid in patients with substance use history

**Novel approaches:**
- **D-cycloserine augmentation:** Partial NMDA agonist; enhances extinction memory consolidation when given before CBT interoceptive exposure sessions; promising in RCTs
- **Stellate ganglion block:** Reduces sympathetic hyperactivation; limited evidence for PD specifically
- **Transcranial magnetic stimulation (TMS):** Low-frequency rTMS over right PFC; modestly reduces PD severity in preliminary trials

## Connections

- `connects-to` → **[Norepinephrine](../../../03-molecular/norepinephrine/README.md)** — locus coeruleus hyperactivation drives tachycardia, chest tightness, and hyperarousal via α1-NE receptor stimulation in amygdala; yohimbine (α2 antagonist) reliably provokes panic in PD patients; propranolol reduces somatic symptoms; clonidine reduces LC firing.

- `connects-to` → **[Serotonin](../../../03-molecular/serotonin/README.md)** — SSRIs are first-line for panic disorder via raphe-amygdala serotonin modulation of the fear circuit; paradoxical jitteriness during initial weeks requires starting low; paroxetine and sertraline have strong evidence; clomipramine (5-HT/NE TCA) is highly effective.

- `connects-to` → **[GABA](../../../03-molecular/gaba/README.md)** — GABA-A activation by benzodiazepines (clonazepam, alprazolam) rapidly terminates panic attacks; reduced BZ binding in temporal lobe in PD suggests GABAergic deficit; BZDs bridge therapy while SSRIs take effect but avoided long-term due to dependence and impaired extinction.

- `connects-to` → **[Glutamate](../../../03-molecular/glutamate/README.md)** — NMDA receptor activation in BLA mediates fear memory consolidation in panic disorder; excessive glutamate signaling amplifies amygdala hyperreactivity; D-cycloserine (partial NMDA agonist) enhances extinction learning in CBT augmentation trials.

- `targets` → **[Brain](../../../06-organ/brain/README.md)** — panic disorder features BLA hyperreactivity to interoceptive and CO2 stimuli, insula hyperactivation, reduced vmPFC control over amygdala, and LC-NE dysregulation; CBT with interoceptive exposure normalizes amygdala-insula reactivity on fMRI over 12+ weeks of treatment.

- `connects-to` → **[Oxytocin](../../../03-molecular/oxytocin/README.md)** — OTR on BLA and CeA neurons dampens fear circuit hyperreactivity and CRH-driven arousal that underlies panic; oxytocin modulates LC-NE excitability, attenuating the spontaneous high-frequency LC firing associated with panic attacks; intranasal OT reduces fear generalization and anticipatory anxiety; OT augmentation of interoceptive exposure therapy is an active research avenue.
- `treated-by` → **[Fluoxetine](../../../03-medicine/01-modern/10-mental-health/fluoxetine/README.md)** — FDA-approved for panic disorder with/without agoraphobia; SSRIs first-line over benzodiazepines; initial paradoxical anxiety (5-HT1A stimulation) requires start-low-go-slow dosing; onset 4–8 weeks; 70–80% response rate; CBT additive.

- `connects-to` → **[Generalized Anxiety Disorder](../generalized-anxiety-disorder/README.md)** — Panic disorder and generalized anxiety disorder are neighboring anxiety disorders that often co-occur and share serotonergic/GABAergic biology and first-line SSRIs, but differ in tempo: panic is paroxysmal terror with autonomic symptoms, GAD sustained free-floating worry.

- `connects-to` → **[Social Anxiety Disorder](../social-anxiety-disorder/README.md)** — Panic disorder and social anxiety disorder are both fear-circuit anxiety disorders treated first-line with SSRIs, but differ in trigger: panic attacks are unexpected and somatic (interoceptive), social anxiety cued by scrutiny; they often coexist, exposure CBT tailored to each.

- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — Panic attacks originate in fear-circuit neurons: hyperexcitable locus coeruleus and basolateral amygdala neurons fire to interoceptive or CO2 cues, triggering the autonomic surge, while weak prefrontal inhibition fails to restrain them — the target of SSRIs and benzodiazepines.
- `connects-to` → **[PTSD](../ptsd/README.md)** — Panic disorder and PTSD overlap in fear circuitry: both involve a hyperreactive amygdala and noradrenergic surges, panic attacks are common in PTSD, and they share SSRIs and exposure CBT—but PTSD is anchored to a trauma memory while panic strikes unpredictably.
- `connects-to` → **[Adrenal Gland](../../06-organ/adrenal-gland/README.md)** — A panic attack is a false alarm of the fight-or-flight axis the adrenal gland serves: surging adrenaline drives palpitations, sweating, and tremor, and because pheochromocytoma produces identical paroxysms, panic with severe hypertension warrants catecholamine testing.
- `connects-to` → **[Asthma](../asthma/README.md)** — Panic disorder and asthma are tightly comorbid and can mimic each other: breathlessness triggers panic and hyperventilation worsens bronchospasm, while CO2 hypersensitivity links both—so telling an asthma attack from a panic attack matters clinically.
- `connects-to` → **[Pheochromocytoma/Paraganglioma](../pheochromocytoma-paraganglioma/README.md)** — Pheochromocytoma is the classic organic mimic of panic disorder: its catecholamine surges produce sudden palpitations and a sense of doom indistinguishable from a panic attack—so refractory 'panic' with hypertension warrants metanephrine testing to exclude it.
- `connects-to` → **[Cortisol](../../03-molecular/cortisol/README.md)** — Panic disorder engages the HPA stress axis through cortisol: although the acute attack is driven by adrenaline, chronic anxiety dysregulates cortisol secretion, and the hormone's feedback shapes fear circuits—linking the body's main stress hormone to recurrent panic.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — Panic disorder and depression are highly comorbid and share treatment: most patients with one develop the other, both respond to SSRIs, and co-occurring panic worsens depression's prognosis and suicide risk—so screening for depression is routine in panic disorder.
- `connects-to` → **[Adenosine](../../03-molecular/adenosine/README.md)** — Adenosine links caffeine to panic attacks: blocking adenosine receptors (as caffeine does) can provoke panic in susceptible people, evidence that the adenosine system modulates anxiety—so caffeine avoidance is part of managing panic disorder.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — Panic disorder masquerades as heart disease: surging adrenaline causes palpitations, chest pain and tachycardia that mimic a heart attack, so panic is a leading reason for emergency cardiac workups—and real cardiac disease must be excluded before diagnosing it.
- `connects-to` → **[Respiratory system](../respiratory-system/README.md)** — Panic disorder may stem from a faulty suffocation alarm: patients are hypersensitive to rising CO2, so air hunger and hyperventilation trigger attacks (and CO2 inhalation can provoke them in the lab)—linking the respiratory system's chemosensing to panic.
- `connects-to` → **[Orexin](../../03-molecular/orexin/README.md)** — Orexin links arousal to panic: the orexin (hypocretin) system drives wakefulness and the stress response, and heightened orexin signaling is implicated in panic attacks—suggesting the same neurons that stabilize wakefulness also tune the brain's alarm circuitry.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — Panic disorder is a misfiring of the nervous system's fear circuitry: a hypersensitive amygdala-brainstem alarm triggers a full fight-or-flight surge without real danger, so the body's threat response—racing heart, breathlessness, terror—erupts as a panic attack.
- `connects-to` → **[Cardiovascular system](../cardiovascular-system/README.md)** — Panic attacks masquerade as cardiac emergencies: the surge of palpitations, chest pain and breathlessness mimics a heart attack and floods emergency rooms, so panic disorder is a major reason chest pain is evaluated—after truly excluding cardiovascular causes.
- `connects-to` → **[Epinephrine](../../03-molecular/epinephrine/README.md)** — A panic attack is in part an adrenaline storm: surging epinephrine drives the pounding heart, sweating, tremor and chest tightness, which is why panic can mimic a heart attack—and why a catecholamine-secreting pheochromocytoma is on the differential.
- `connects-to` → **[Carbon](../../02-atomic/carbon/README.md)** — Panic disorder is tied to carbon dioxide sensing: inhaling CO2 reliably provokes attacks in patients, supporting a 'suffocation false-alarm' theory in which an oversensitive brainstem misreads rising CO2 as suffocation and fires panic.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — Panic's respiratory subtype centers on the lungs: hyperventilation blows off CO2 causing the tingling, lightheadedness and air hunger of an attack, and breathing retraining is a core treatment—linking a psychiatric disorder to respiratory physiology.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Panic attacks tingle because of calcium: hyperventilation blows off CO2 and raises blood pH, which lowers ionized calcium—producing the perioral numbness, hand tingling, and carpopedal spasm that frighten patients mid-attack.
- `connects-to` → **[Hippocampus](../../05-tissue/hippocampus/README.md)** — Panic disorder engages the hippocampus's fear memory: by encoding the context of past attacks, the hippocampus drives anticipatory anxiety and agoraphobic avoidance of places where panic struck, extending the disorder beyond the attacks themselves.
- `connects-to` → **[Astrocyte](../../04-cellular/astrocyte/README.md)** — Astrocytes help tune the panic circuit: by clearing and recycling glutamate and GABA around the amygdala and brainstem, these glial cells shape the excitatory-inhibitory balance whose disturbance can tip neurons into a panic response.
- `connects-to` → **[Hydrogen](../../02-atomic/hydrogen/README.md)** — Panic may be a misfiring suffocation alarm read in acid: rising CO2 turns to carbonic acid, and acid-sensing channels in the amygdala detect the falling pH, triggering the sudden terror and air hunger of an attack—why breathing CO2 can provoke one.
- `connects-to` → **[Synapse](../../05-tissue/synapse/README.md)** — Panic disorder is wired into fear-circuit synapses: repeated attacks strengthen connections in the amygdala and its pathways, so neutral cues come to trigger alarm—plasticity that exposure therapy and SSRIs work to reshape.
- `connects-to` → **[Microglia](../../04-cellular/microglia/README.md)** — Microglia may stoke the panic-prone brain: chronic stress activates these immune cells to release cytokines that shift the excitatory-inhibitory balance in fear circuits, linking neuroinflammation to vulnerability to panic.
- `connects-to` → **[Thyroid Gland](../../06-organ/thyroid/README.md)** — An overactive thyroid mimics panic: excess thyroid hormone causes palpitations, sweating, and dread that look just like panic attacks, so thyroid function is checked before settling on the diagnosis.
- `connects-to` → **[Large Intestine](../../06-organ/large-intestine/README.md)** — Panic grips the gut: through the gut-brain axis attacks bring nausea, cramping, and urgent bowel movements, and panic disorder overlaps heavily with irritable bowel syndrome.
- `connects-to` → **[Cardiomyocyte](../../04-cellular/cardiomyocyte/README.md)** — Panic floods heart-muscle cells with adrenaline: the surge drives cardiomyocytes into pounding palpitations and chest pain, and rarely into a transient stress cardiomyopathy, the 'heart attack' feeling of an attack.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Photons expose the panicking brain: functional MRI and PET reveal an overactive amygdala and fear circuit with weak prefrontal restraint, the imaging signature researchers use to map why an attack erupts without real danger.
- `connects-to` → **[Sodium](../../02-atomic/sodium/README.md)** — Sodium lactate is the classic panic trigger: infusing it into the vein reliably provokes a full attack in patients but not in healthy people, a reproducible challenge test that helped prove panic disorder has a distinct biology.
- `connects-to` → **[Dopamine](../../03-molecular/dopamine/README.md)** — Dopamine wires panic into avoidance: the reward-and-threat transmitter helps stamp in the fear conditioning that turns a single attack into agoraphobia, as the brain learns to dread and flee the places where panic struck.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — Panic floods to the skin: the sympathetic surge of an attack drives drenching sweat, flushing, and chills, the visible autonomic storm that accompanies the racing heart and breathlessness.
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — Magnesium tempers excitability, and its lack feeds anxiety: low magnesium heightens neuronal firing and the stress response, and deficiency is associated with anxiety and panic, making repletion a simple thing to check.
- `connects-to` → **[Stomach](../../06-organ/stomach/README.md)** — Panic turns the stomach: the brain-gut axis routes the attack into nausea, churning, and the 'butterflies' of acute fear, and recurrent panic often overlaps with functional gut complaints.
- `connects-to` → **[Progesterone](../../03-molecular/progesterone/README.md)** — Panic tracks the hormonal tide: its metabolite allopregnanolone tunes the calming GABA receptor, so the premenstrual and postpartum drops in progesterone, like a withdrawal, can unmask or worsen panic attacks in vulnerable women.
- `connects-to` → **[Gut Microbiome](../gut-microbiome/README.md)** — The gut's microbes whisper to the anxious brain: through the microbiome-gut-brain axis they shape GABA, serotonin, and vagal signaling, and the dysbiosis common in panic and its frequent IBS overlap is studied as both consequence and contributor.
- `connects-to` → **[Platelet](../../04-cellular/platelet/README.md)** — Platelets offer a peripheral window on the disorder: they take up and store serotonin much as neurons do, so altered platelet serotonin transport and receptor binding have served as accessible research markers of the serotonergic disturbance in panic.
- `connects-to` → **[Estrogen](../../03-molecular/estrogen/README.md)** — Hormone shifts sway the panic threshold: attacks often cluster premenstrually, postpartum, and around menopause, as falling estrogen modulates the serotonin and fear circuits — part of why panic disorder is roughly twice as common in women.
- `connects-to` → **[Mast Cell](../../04-cellular/mast-cell/README.md)** — Mast cells can mimic a panic attack: in mast cell activation syndrome, surges of histamine and mediators cause flushing, palpitations and a sense of doom indistinguishable from panic, a medical mimic worth excluding in atypical cases.
- `connects-to` → **[Insomnia Disorder](../insomnia-disorder/README.md)** — Panic invades sleep: nocturnal panic attacks jolt patients awake in terror, and the resulting fear of sleep feeds an insomnia that worsens daytime anxiety in a self-reinforcing loop.
- `connects-to` → **[Alcohol Use Disorder](../alcohol-use-disorder/README.md)** — Many self-medicate their way into a second illness: people with panic disorder often drink or take sedatives to quell attacks, and the withdrawal rebound itself provokes panic — a vicious loop that makes alcohol use disorder a frequent companion.
- `connects-to` → **[Migraine](../migraine/README.md)** — The two travel together: panic disorder and migraine are strongly comorbid, sharing serotonergic and autonomic dysregulation, so each roughly doubles the odds of the other and both can flare under the same stressors.
- `connects-to` → **[BDNF](../../03-molecular/bdnf/README.md)** — Stress reshapes the fear circuitry: altered BDNF signaling, which governs the synaptic plasticity of the amygdala and hippocampus, is implicated in how chronic stress lowers the threshold for the runaway fear response of a panic attack.
- `connects-to` → **[CRH](../../03-molecular/crh/README.md)** — CRH sets the alarm's sensitivity: the corticotropin-releasing hormone that launches the HPA stress response also acts in the amygdala to heighten fear, and its dysregulation lowers the threshold for the spontaneous surge of a panic attack.
- `connects-to` → **[COPD](../copd/README.md)** — Breathlessness and panic feed each other: panic disorder is markedly more common in COPD, where air hunger triggers attacks and CO2-sensitive suffocation alarms misfire, each worsening the other's symptoms and disability.
- `connects-to` → **[Stimulant Use Disorder](../stimulant-use-disorder/README.md)** — Stimulants ignite the panic circuit: caffeine and stimulant drugs provoke the racing heart and hyperarousal that set off attacks, so stimulant use can unmask or worsen panic disorder.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — Chronic alarm leaves an inflammatory mark: the repeated stress responses of panic disorder activate NF-κB-driven cytokine signaling, a low-grade inflammation tied to its physical-health comorbidities.
- `connects-to` → **[Bipolar Disorder](../bipolar-disorder/README.md)** — Panic rides with mood instability: panic disorder is over-represented in bipolar disorder, the comorbidity worsening its course and raising suicide risk, a pairing that shapes treatment choices.
- `connects-to` → **[Cannabis Use Disorder](../cannabis-use-disorder/README.md)** — Cannabis cuts both ways with panic: it can acutely trigger panic attacks and, with heavy use and withdrawal, worsen the disorder, even as some users turn to it to self-medicate anxiety.
- `connects-to` → **[Hypertension](../hypertension/README.md)** — Repeated catecholamine surges press on the arteries: each panic attack floods the body with adrenaline and noradrenaline, and the chronic autonomic arousal of panic disorder is linked to higher rates of sustained hypertension.
- `connects-to` → **[Heart Failure](../heart-failure/README.md)** — Acute panic can stun the heart: an intense surge of stress hormones during a severe attack can precipitate takotsubo (stress) cardiomyopathy, a transient but real cause of acute heart failure that mimics a heart attack.
- `connects-to` → **[Stroke](../stroke/README.md)** — Chronic panic tracks with cerebrovascular risk: the autonomic arousal, hypertension and platelet activation tied to panic disorder, plus its overlap with smoking and inactivity, are associated with an elevated long-term risk of stroke.
- `connects-to` → **[Obsessive-Compulsive Disorder](../obsessive-compulsive-disorder/README.md)** — Two anxiety-spectrum disorders that travel together: panic disorder frequently coexists with OCD, sharing heightened threat sensitivity and serotonergic dysregulation and responding to overlapping SSRI and CBT treatment.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — Stress hormones drive the attacks: panic is mediated by surges of adrenaline and HPA-axis cortisol, and endocrine disease such as thyrotoxicosis or a phaeochromocytoma can precipitate panic-identical episodes.
- `connects-to` → **[Attention-Deficit/Hyperactivity Disorder](../attention-deficit-hyperactivity-disorder/README.md)** — Frequently comorbid, and treatment can collide: anxiety and panic are common alongside ADHD, and the stimulants used to treat ADHD can provoke or worsen panic attacks, complicating management.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — Panic speaks through the gut: attacks bring nausea and abdominal distress, and panic disorder is strongly comorbid with irritable bowel syndrome through the gut-brain axis.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — Hyperventilation cramps the muscles: the overbreathing of a panic attack causes respiratory alkalosis with carpopedal spasm and tetany, on top of the chronic muscle tension anxiety brings.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — The body sweats and flushes in fear: profuse diaphoresis, flushing and chills are autonomic skin manifestations of a panic attack, mediated by the adrenaline surge.

[^gorman-2000-panic-neurobiology]: Gorman JM, Kent JM, Sullivan GM, Coplan JD. Neuroanatomical hypothesis of panic disorder, revised. *Am J Psychiatry.* 2000;157(4):493-505. [doi:10.1176/appi.ajp.157.4.493](https://doi.org/10.1176/appi.ajp.157.4.493) · [PubMed 10739407](https://pubmed.ncbi.nlm.nih.gov/10739407/)
[^nardi-2009-clonazepam-panic]: Nardi AE, Freire RC, Zin WA. Panic disorder and control of breathing. *Respir Physiol Neurobiol.* 2009;167(1):133-143. [doi:10.1016/j.resp.2008.07.011](https://doi.org/10.1016/j.resp.2008.07.011) · [PubMed 18708168](https://pubmed.ncbi.nlm.nih.gov/18708168/)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
