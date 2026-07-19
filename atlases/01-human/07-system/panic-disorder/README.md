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
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "Hormones modulate its attacks: panic symptoms can fluctuate with the menstrual cycle and emerge or worsen in pregnancy and the postpartum period, reflecting hormonal influences on anxiety."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "Overbreathing and its drugs shift chemistry: hyperventilation during attacks causes respiratory alkalosis that the kidney buffers, and the SSRIs used to treat panic can cause hyponatraemia."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "Chronic anxiety inflames the body: persistent panic and stress raise inflammatory markers and dysregulate cortisol, linking the disorder to systemic inflammation over time."
  - target: 03-medicine/01-modern/04-cardio/beta-blockers
    relation: connects-to
    note: "A heart drug for the body's alarm: beta-blockers like propranolol blunt the palpitations, tremor and sweating of a panic attack by blocking the adrenergic surge, though SSRIs treat the disorder itself."
  - target: 03-medicine/03-food/magnesium-dietary
    relation: connects-to
    note: "A mineral linked to anxiety: low magnesium is associated with anxiety and panic, and supplementation is trialled as an adjunct, though the evidence is modest."
  - target: 03-medicine/02-traditional/ashwagandha
    relation: connects-to
    note: "Traditional calm is sought for it: ashwagandha and other adaptogens are used for anxiety with some evidence of benefit, complementing rather than replacing established panic-disorder treatment."
  - target: 01-human/07-system/fibromyalgia
    relation: connects-to
    note: "Anxiety and bodily symptoms overlap: panic disorder is markedly more common in fibromyalgia, the two sharing central sensitisation, autonomic dysregulation and a heavy symptom burden."
  - target: 03-medicine/03-food/omega-3-fatty-acids
    relation: connects-to
    note: "Diet offers a modest adjunct: omega-3 supplementation shows small anxiolytic effects in trials, used alongside but not instead of established treatment for panic disorder."
  - target: 01-human/07-system/borderline-personality-disorder
    relation: connects-to
    note: "Panic rides with emotional dysregulation: panic attacks are frequent in borderline personality disorder, where affective instability and hyperarousal lower the threshold for acute anxiety surges."
  - target: 01-human/07-system/epilepsy
    relation: connects-to
    note: "Panic mimics and overlaps seizures: temporal-lobe epilepsy can produce fear and autonomic surges indistinguishable from a panic attack, and the two share limbic (amygdala-hippocampal) hyperexcitability and GABAergic dysfunction—an important diagnostic crossover."
  - target: 01-human/05-tissue/cardiac-conduction-system
    relation: connects-to
    note: "Its symptoms feel cardiac: a panic attack floods the heart with adrenaline, causing palpitations, tachycardia and chest pain that mimic a supraventricular arrhythmia and send patients to the emergency room fearing a heart attack."
  - target: 01-human/07-system/binge-eating-disorder
    relation: connects-to
    note: "Anxiety can drive the binge: panic disorder and other anxiety disorders frequently co-occur with binge-eating disorder, where acute distress and emotional dysregulation trigger loss-of-control eating as a maladaptive coping response."
  - target: 01-human/05-tissue/myocardium
    relation: connects-to
    note: "When panic mimics—and harms—the heart: panic attacks cause chest pain that mimics myocardial infarction, and extreme emotional stress can precipitate takotsubo stress cardiomyopathy of the myocardium."
  - target: 01-human/05-tissue/alveolus
    relation: connects-to
    note: "Hyperventilation and the suffocation alarm: panic drives hyperventilation that blows off CO2 into respiratory alkalosis, and brain CO2-sensing underlies the 'false suffocation alarm' theory of panic."
  - target: 01-human/05-tissue/peripheral-nerve
    relation: connects-to
    note: "Paraesthesiae and tetany: the respiratory alkalosis of a panic attack drops ionised calcium, hyperexciting peripheral nerves to cause the tingling, numbness and carpopedal spasm that frighten patients further."
  - target: 01-human/07-system/atherosclerosis
    relation: connects-to
    note: "The acute-coronary mimic: a panic attack's chest pain, palpitations and sweating imitate a heart attack, a leading reason for emergency cardiac workups, while chronic anxiety itself modestly raises atherosclerotic cardiovascular risk."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "The can't-miss differential: pulmonary embolism causes sudden dyspnoea, tachycardia, chest pain and a sense of doom indistinguishable from a panic attack, the dangerous diagnosis to exclude before attributing symptoms to anxiety."
  - target: 01-human/07-system/covid-19-disease
    relation: connects-to
    note: "A pandemic of anxiety: COVID-19 and its social upheaval drove a global surge in panic and anxiety disorders, and post-COVID breathlessness and palpitations can themselves trigger or mimic panic attacks."
  - target: 01-human/03-molecular/npy
    relation: connects-to
    note: "Resilience neuropeptide: neuropeptide Y dampens the stress and fear response, and reduced NPY signalling is associated with vulnerability to panic and anxiety."
  - target: 01-human/03-molecular/substance-p
    relation: connects-to
    note: "Fear circuit signalling: substance P acting on NK1 receptors in the amygdala modulates fear and panic responses, an explored anxiolytic target."
  - target: 01-human/05-tissue/intestinal-epithelium
    relation: connects-to
    note: "Gut-brain axis: panic disorder overlaps with irritable bowel syndrome, and signalling across the intestinal epithelium and microbiome feeds the fear and arousal circuits behind it."
  - target: 01-human/03-molecular/acetylcholine
    relation: connects-to
    note: "Cholinergic provocation: cholinergic agents can provoke panic-like attacks, and the cholinergic system modulates the respiratory and arousal circuits implicated in panic disorder."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "Inflammatory anxiety: elevated IL-6 is found in panic disorder, part of the bidirectional link between chronic anxiety and low-grade systemic inflammation."
  - target: 01-human/03-molecular/tnf-alpha
    relation: connects-to
    note: "Stress cytokine: raised TNF-α accompanies panic disorder, reflecting the neuroimmune activation increasingly implicated in anxiety disorders."
  - target: 01-human/03-molecular/serotonin-transporter
    relation: connects-to
    note: "First-line drug target: SSRIs that block the serotonin transporter are the pharmacological mainstay of panic disorder, and the 5-HTTLPR transporter polymorphism modulates susceptibility and treatment response."
  - target: 01-human/03-molecular/mu-opioid-receptor
    relation: connects-to
    note: "Suffocation alarm: the opioidergic-deficit hypothesis holds that blunted endogenous opioid tone leaves the brainstem suffocation alarm hypersensitive to CO2, helping explain the spontaneous panic attacks of panic disorder."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "Neuroinflammation: IL-1β is among the inflammatory cytokines elevated in panic disorder, contributing to the HPA-axis activation and neuroimmune signalling that accompany recurrent panic."
  - target: 01-human/03-molecular/endocannabinoid
    relation: connects-to
    note: "Fear extinction: endocannabinoid signalling at amygdala CB1 receptors is essential for extinguishing conditioned fear, and a deficient endocannabinoid tone impairs the extinction learning whose failure perpetuates panic and anticipatory anxiety."
  - target: 01-human/03-molecular/cgrp
    relation: connects-to
    note: "Panicogenic peptide: CGRP released from the parabrachial nucleus into the amygdala signals threat and arousal, and CGRP infusion provokes panic-like anxiety — a neuropeptide pathway linking panic disorder to the migraine with which it is comorbid."
  - target: 01-human/03-molecular/vasopressin
    relation: connects-to
    note: "HPA amplification: arginine vasopressin co-secreted with CRH synergistically drives ACTH release at the V1b receptor, and this AVP arm of the stress axis is implicated in the heightened neuroendocrine reactivity of panic disorder."
  - target: 01-human/03-molecular/beta1-adrenergic-receptor
    relation: connects-to
    note: "Somatic symptoms: the palpitations, tachycardia and chest discomfort of a panic attack arise from catecholamine activation of cardiac β1-adrenergic receptors, the target of the β-blockers used to blunt the peripheral symptoms that fuel catastrophic misinterpretation."
  - target: 01-human/03-molecular/glucocorticoid-receptor
    relation: connects-to
    note: "HPA feedback: impaired glucocorticoid-receptor sensitivity weakens cortisol's negative feedback on the CRH-ACTH axis, sustaining the stress-hormone tone that lowers the threshold for panic in vulnerable individuals."
  - target: 01-human/03-molecular/nlrp3-inflammasome
    relation: connects-to
    note: "Neuroinflammation: psychological stress activates the NLRP3 inflammasome to generate IL-1β, the upstream source of the inflammatory cytokines linked here to panic, connecting stress signalling to the low-grade neuroinflammation seen in anxiety disorders."
  - target: 01-human/03-molecular/acth
    relation: connects-to
    note: "HPA-axis activation: a panic attack drives CRH (mapped) to release pituitary ACTH, which raises cortisol (mapped), completing the stress-hormone axis engaged in panic disorder."
  - target: 01-human/03-molecular/histamine
    relation: connects-to
    note: "Arousal signalling: histaminergic neurons promote wakefulness and vigilance alongside orexin (mapped), and this arousal circuitry contributes to the hypervigilance and nocturnal panic attacks of panic disorder."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "Anti-inflammatory balance: a relative deficit of regulatory IL-10 against the IL-6, IL-1β and TNF (all mapped) elevated in anxiety is part of the neuroinflammatory contribution to panic disorder."
  - target: 01-human/03-molecular/tlr4
    relation: connects-to
    note: "Neuroinflammatory hyperexcitability: TLR4-driven neuroinflammation links peripheral and central inflammation to the amygdala hyperexcitability implicated in the panic response."
  - target: 01-human/03-molecular/ntrk
    relation: connects-to
    note: "Fear-circuit plasticity: BDNF signalling through its TrkB receptor (NTRK) mediates the amygdala-prefrontal fear-circuit plasticity whose dysregulation underlies panic disorder."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "Fear-memory consolidation: amygdala ERK-MAPK signalling consolidates the fear-conditioned memories that drive the recurrent, interoception-triggered attacks of panic disorder."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "BDNF/serotonergic PI3K-AKT-mTOR signalling supports the fear-circuit neuroplasticity that anxiolytic treatment restores in panic disorder."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Microglial galectin-3 reflects the low-grade neuroinflammation increasingly associated with panic disorder."
  - target: 01-human/03-molecular/myd88
    relation: connects-to
    note: "TLR4-MyD88 innate signalling (TLR4 mapped) contributes to the neuroinflammation implicated in panic-disorder pathophysiology."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "GSK-3β signalling in fear and arousal circuits shapes the synaptic plasticity relevant to the heightened threat reactivity of panic disorder."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "IL-6-STAT3 signalling transduces the inflammatory tone associated with the heightened stress reactivity of panic disorder."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "Cytosolic mitochondrial DNA released during chronic stress can engage cGAS-STING, contributing to the neuroinflammation implicated in panic disorder."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "FOXO downstream of PI3K-AKT signaling (AKT already mapped) regulates neuronal oxidative-stress handling relevant to the fear-circuit dysregulation of panic disorder."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "IFN-STAT1 neuroinflammatory signaling contributes to the inflammatory tone associated with panic disorder."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "JAK1/2 signaling upstream of STAT3 (IL-6 already mapped) relays the inflammatory tone linked to the anxiety circuitry of panic disorder."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "PI3K (PIK3CA)-AKT signaling (AKT already mapped), downstream of BDNF-TrkB (BDNF and NTRK already mapped), participates in the fear-circuit neuroplasticity of panic disorder."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "mTOR signaling participates in the synaptic plasticity of the fear and anxiety circuits implicated in panic disorder."
  - target: 01-human/03-molecular/melatonin
    relation: connects-to
    note: "Melatonin and circadian signaling modulate the sleep-related and nocturnal-panic features of panic disorder."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK-linked metabolic signaling participates in the neurometabolic and stress-adaptation responses relevant to panic disorder."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Autophagy modulates the neuronal stress resilience and fear-circuit homeostasis implicated in panic disorder."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "DNMT3A-mediated DNA methylation contributes to the epigenetic (early-life-stress) programming implicated in panic disorder."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-driven chemokine signaling participates in the neuroimmune and microglial responses implicated in panic disorder."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "CXCL12-CXCR4 signaling participates in the neuroimmune interactions implicated in panic disorder."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "IL-33 alarmin signaling participates in the neuroinflammatory responses implicated in panic disorder."
  - target: 01-human/03-molecular/thyroid-hormones
    relation: connects-to
    note: "Endocrine mimic: thyrotoxicosis produces palpitations, tremor and anxiety that mimic and precipitate panic attacks, which is why thyroid-hormone screening is a standard part of the panic-disorder workup to exclude a treatable endocrine driver."
  - target: 01-human/03-molecular/angiotensin-ii
    relation: connects-to
    note: "Brain renin-angiotensin: central angiotensin II modulates sympathetic outflow and HPA-axis reactivity, and angiotensin blockade attenuates stress and anxiety responses, linking panic vulnerability to a neuroendocrine pressor axis beyond classical neurotransmitters."
  - target: 01-human/03-molecular/nitric-oxide
    relation: connects-to
    note: "Gaseous neurotransmission: nitric oxide signalling in the amygdala and periaqueductal grey shapes the fear and defensive responses underlying panic, and nNOS activity modulates the exaggerated CO2/chemosensory alarm that provokes attacks."
  - target: 01-human/01-subatomic/proton
    relation: connects-to
    note: "CO2 suffocation alarm: panic disorder features a hypersensitive suffocation alarm, and inhaled carbon dioxide or infused lactate, which shift acid-base balance by raising protons, reliably provoke attacks, implicating acid-base chemosensing in panic."
  - target: 01-human/03-molecular/insulin
    relation: connects-to
    note: "Hypoglycaemia trigger: falling glucose from insulin action provokes an adrenergic counter-regulatory surge (epinephrine already mapped) whose palpitations, sweating and tremor mimic and can trigger panic attacks, one of the metabolic precipitants of panic."
  - target: 01-human/03-molecular/troponin-complex
    relation: connects-to
    note: "Cardiac mimic: the chest pain, palpitations and tachycardia of a panic attack closely mimic myocardial infarction, so troponin is often measured to exclude it, and panic disorder is a frequent presentation to emergency cardiology."
  - target: 01-human/03-molecular/xanthine-oxidase
    relation: connects-to
    note: "Oxidative stress: anxiety disorders including panic are associated with heightened oxidative stress, to which xanthine oxidase contributes, and the resulting reactive oxygen species may affect the fear-circuit neurons and stress physiology."
  - target: 01-human/03-molecular/prostaglandins
    relation: connects-to
    note: "Neuroinflammation: prostaglandins from the low-grade neuroinflammation (IL-6 and IL-1 already mapped) linked to panic disorder modulate the fear circuitry and the autonomic and stress responses that generate panic attacks."
  - target: 01-human/03-molecular/glp-1
    relation: connects-to
    note: "Gut-brain interoception: GLP-1 signalling in the brainstem and hypothalamus links visceral and metabolic state to the interoceptive processing (insulin already mapped) whose misreading contributes to the bodily alarm of a panic attack."
  - target: 01-human/03-molecular/cholesterol
    relation: connects-to
    note: "Metabolic association: panic disorder is associated with metabolic and cardiovascular findings, and the dyslipidaemia (insulin already mapped) that clusters with anxiety links lipid metabolism to the disorder and its cardiac risk."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Adipokine-stress link: the adipokine leptin, part of the appetite and stress-axis signalling (insulin already mapped), is altered in anxiety disorders, a metabolic dimension of the dysregulated fear and autonomic responses of panic disorder."
  - target: 01-human/03-molecular/ghrelin
    relation: connects-to
    note: "Stress and appetite: ghrelin rises with stress and modulates the HPA (cortisol already mapped) and fear responses, and its dysregulation, with leptin (already mapped), links the appetite-stress axis to the anxiety of panic disorder."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "Neuroimmune balance: the anti-inflammatory IL-4, with IL-10 (already mapped), counters the pro-inflammatory cytokines (IL-6, TNF and IL-1 already mapped) of the low-grade neuroinflammation reported in panic and anxiety disorders."
  - target: 01-human/02-atomic/copper
    relation: connects-to
    note: "Copper and noradrenaline: copper is the cofactor of dopamine-β-hydroxylase, which makes noradrenaline from dopamine (both already mapped), linking copper handling to the noradrenergic (locus coeruleus) arousal that drives panic attacks."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "Zinc and NMDA: zinc modulates the glutamatergic (already mapped) NMDA receptors and has an anxiolytic role, and low zinc status is reported in anxiety disorders including panic disorder."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "Type-2 neuroimmune arm: IL-13, with IL-4 (already mapped), is part of the type-2 immune arm balancing the neuroinflammation (TNF, IL-1 and IL-6 already mapped) increasingly implicated in panic disorder."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Metabolic-inflammatory adipokine: adiponectin, with leptin (already mapped), links the metabolic-inflammatory state to the anxiety and neuroinflammation of panic disorder."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), is the pro-inflammatory adipokine of the metabolic-inflammatory milieu of panic disorder."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Interferon-induced anxiety: the type-I interferon (therapy) induces the anxiety and mood symptoms, linking the innate-immune (cGAS-STING already mapped) signalling to the neuroinflammation of panic disorder."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Th1 neuroinflammation: the IFN-γ of the T cells is the type-II interferon arm of the low-grade neuroinflammation (TNF and IL-1 already mapped) associated with panic disorder."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the immune-inflammatory dimension implicated in panic disorder."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune dysregulation associated with panic disorder."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the immune-inflammatory dimension of panic disorder."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the low-grade inflammation associated with panic disorder."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Psychoneuroimmune arm: the peripheral cytotoxic T cells (perforin pathway) reflect the stress-associated adaptive immune activation of the psychoneuroimmunology of panic disorder."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "Stress-modulated NK: the NK-cell number and cytotoxicity are altered by the acute and chronic stress reactivity (cortisol and catecholamines already mapped) of panic disorder."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "CD4 cytokine source: the CD4 T-helper cells are the source of the Th1/Th2/Th17 (IFN-γ, IL-4 and IL-17 already mapped) cytokines of the low-grade inflammation associated with panic disorder."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Neuroimmune complement: the complement C3 activation is part of the low-grade innate inflammation and the neuroinflammatory dimension implicated in panic disorder."
  - target: 01-human/03-molecular/c5ar1
    relation: connects-to
    note: "C5a receptor: the C5aR1 signalling (with the complement C3 already mapped) contributes to the innate inflammatory dimension of the neuroimmune interaction in panic disorder."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "CNS-border antigen presentation: the dendritic cells of the CNS-border compartments are part of the neuroimmune interface implicated in the low-grade inflammation of panic disorder."
  - target: 01-human/03-molecular/tslp
    relation: connects-to
    note: "Airway-CNS axis: TSLP-driven airway inflammation underpins the asthma-panic disorder comorbidity; the shared sensitisation of the brainstem's CO2-sensitive locus coeruleus by airway alarmins links asthma and panic attacks."
  - target: 01-human/03-molecular/bradykinin
    relation: connects-to
    note: "Dyspnoea–panic trigger: bradykinin, released during respiratory inflammation, activates bronchial C-fibres that signal brainstem suffocation-detection circuits, directly precipitating panic attacks in sensitised individuals."
  - target: 01-human/03-molecular/complement-c5
    relation: connects-to
    note: "Terminal neuroinflammation: C5 cleavage generates C5a, which via C5aR1 (already mapped) amplifies the low-grade neuroinflammation of the locus coeruleus and limbic circuits that regulate the fear-suffocation alarm implicated in panic disorder."
  - target: 01-human/03-molecular/c1-esterase-inhibitor
    relation: connects-to
    note: "Kallikrein-kinin control: C1-esterase inhibitor modulates the kallikrein-kinin system (bradykinin already mapped) and the classical complement (C3/C5 already mapped), constraining the neuroimmune contact cascade implicated in panic attacks."
  - target: 01-human/03-molecular/erythropoietin
    relation: connects-to
    note: "Neuroprotective EPO axis: erythropoietin, acting through EPOR in the brain, exerts neuroprotective and anxiolytic effects on the amygdala and hippocampus (already mapped), attenuating fear-memory consolidation in panic-disorder circuits."
  - target: 01-human/03-molecular/prolactin
    relation: connects-to
    note: "Post-attack anxiolytic: prolactin surges after panic attacks, exerting acute anxiolytic effects via the GABAergic (GABA already mapped) and serotonin (already mapped) systems, modulating the neuroendocrine recovery phase after panic episodes."
  - target: 01-human/03-molecular/testosterone
    relation: connects-to
    note: "Panic testosterone axis: testosterone exerts anxiolytic effects via androgen receptor in the amygdala (already mapped) and hippocampus (already mapped), modulating the HPA-axis CRH (already mapped) response and GABAergic interneuron activity in panic-disorder circuits."
  - target: 01-human/02-atomic/selenium
    relation: connects-to
    note: "Panic selenium: selenium via GPX4 and selenoproteins reduces oxidative stress in amygdala (already mapped) and locus coeruleus neurons, attenuating the noradrenergic and serotonin (already mapped) circuit vulnerability of panic disorder."
  - target: 01-human/03-molecular/transferrin
    relation: connects-to
    note: "Panic iron axis: transferrin-mediated iron delivery is required for tryptophan hydroxylase (for serotonin already mapped) and tyrosine hydroxylase (for dopamine already mapped) activity in the raphe nuclei and locus coeruleus; iron deficiency amplifies panic-disorder risk."
  - target: 01-human/02-atomic/iodine
    relation: connects-to
    note: "Panic iodine: iodine via thyroid hormones (already mapped) modulates the HPA-axis CRH (already mapped) and amygdala (already mapped) noradrenergic responsiveness; sub-clinical hypothyroidism amplifies panic-disorder vulnerability through HPA-axis dysregulation."
  - target: 01-human/02-atomic/potassium
    relation: connects-to
    note: "Panic potassium: potassium via Kv4.3/Kir3 neuronal channels regulates amygdala (already mapped) and hippocampus (already mapped) action-potential firing thresholds; hypokalaemia amplifies the GABAergic (already mapped) interneuron dysregulation of panic disorder."
  - target: 01-human/02-atomic/phosphorus
    relation: connects-to
    note: "Panic phosphorus: phosphorus as ATP and cAMP-PKA in amygdala (already mapped) and locus coeruleus neurons powers the norepinephrine (already mapped) and GABA (already mapped) neurotransmitter cascades that govern the panic-attack threshold in panic disorder."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Panic disorder iron: iron, as cofactor of monoamine oxidase in neurons (already mapped) and microglia (already mapped), supports monoamine catabolism; iron deficiency amplifies the NF-κB (already mapped) and TNF-α (already mapped) neuroinflammatory cascade of panic disorder."
  - target: 01-human/02-atomic/chloride
    relation: connects-to
    note: "Panic disorder chloride: chloride via GABA-A Cl⁻ channels on neurons (already mapped) and astrocytes (already mapped) sets inhibitory tone; chloride dysregulation impairs GABAergic control, amplifying the NF-κB (already mapped) hyperexcitability cascade of panic disorder."
  - target: 01-human/02-atomic/sulfur
    relation: connects-to
    note: "Panic disorder sulfur: sulfur, as component of glutathione in neurons (already mapped) and astrocytes (already mapped), buffers oxidative stress; sulfur deficiency amplifies the NF-κB (already mapped) and TNF-α (already mapped) neuroinflammatory cascade of panic disorder."
  - target: 01-human/02-atomic/nitrogen
    relation: connects-to
    note: "Panic disorder nitrogen: nitrogen is the backbone of GABA (already mapped) and glutamate (already mapped) in neurons (already mapped); nitrogen deficiency amplifies the NF-κB (already mapped) and TNF-α (already mapped) neuroinflammatory cascade of panic disorder."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "Panic disorder oxygen: oxygen powers neuron (already mapped) and astrocyte (already mapped) mitochondria in the corticolimbic circuit; hypoxic stress amplifies the NF-κB (already mapped) and TNF-α (already mapped) neuroinflammatory cascade of panic disorder."
  - target: 01-human/03-molecular/dopamine
    relation: connects-to
    note: "Panic disorder dopamine: dopamine modulates norepinephrine (already mapped) release and fear-salience signalling in the locus coeruleus; dopamine dysregulation amplifies the NF-κB (already mapped) and TNF-α (already mapped) neuroinflammatory tone of panic disorder."
  - target: 01-human/03-molecular/pd-1
    relation: connects-to
    note: "Panic disorder PD-1: PD-1 checkpoint expression on microglia (already mapped) and T-cells modulates corticolimbic neuroinflammatory tone; PD-1 dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) neuroinflammatory cascade of panic disorder."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "Panic disorder VEGF: VEGF promotes neurovascular remodelling in the amygdala and cortex; VEGF dysregulation amplifies NF-κB (already mapped) and TNF-α (already mapped) neuroinflammatory signalling and impairs neurotrophic repair in panic disorder."
  - target: 01-human/03-molecular/wnt-beta-catenin
    relation: connects-to
    note: "Panic disorder Wnt/β-catenin: Wnt/β-catenin signalling supports neuronal (already mapped) survival and synaptic plasticity in the corticolimbic circuit; Wnt dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) neuroinflammatory cascade of panic disorder."
  - target: 01-human/03-molecular/rankl
    relation: connects-to
    note: "Panic disorder RANKL: RANKL from T-cells (already mapped) in corticolimbic microglia (already mapped) modulates bone-immune crosstalk; RANKL excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) cascade of panic disorder."
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "Panic disorder SMAD4: SMAD4-mediated TGF-β (already mapped) signalling in neurons (already mapped) and microglia (already mapped) regulates corticolimbic neuroinflammation; SMAD4 dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) cascade of panic disorder."
  - target: 01-human/03-molecular/il-2
    relation: connects-to
    note: "Panic disorder IL-2: IL-2 from T-cells (already mapped) in corticolimbic microglia (already mapped) modulates neuroinflammatory tone; IL-2 excess amplifies NF-κB (already mapped) and TNF-α (already mapped) and CRH (already mapped) neuroinflammatory cascade of panic disorder."
  - target: 01-human/03-molecular/fibronectin
    relation: connects-to
    note: "Panic disorder fibronectin: fibronectin in fibroblasts (already mapped) and astrocytes (already mapped) anchors stress-circuit ECM; fibronectin excess amplifies nf-kb (already mapped) and il-6 (already mapped) and tnf-alpha (already mapped) cascade of panic disorder."
  - target: 01-human/03-molecular/notch
    relation: connects-to
    note: "Panic disorder notch: NOTCH on neurons (already mapped) and astrocytes (already mapped) regulates fear extinction plasticity; notch dysregulation amplifies nf-kb (already mapped) and il-6 (already mapped) and tnf-alpha (already mapped) cascade of panic disorder."
  - target: 01-human/03-molecular/igf-1
    relation: connects-to
    note: "Panic disorder igf-1: IGF-1 from fibroblasts (already mapped) and astrocytes (already mapped) modulates neuronal stress resilience; igf-1 dysregulation amplifies nf-kb (already mapped) and il-6 (already mapped) and tnf-alpha (already mapped) cascade of panic disorder."
  - target: 01-human/03-molecular/activin-a
    relation: connects-to
    note: "Panic activin-a: activin-A from neurons (already mapped) and astrocytes (already mapped) drives neuroinflammatory signalling in panic circuits; activin-a excess amplifies nf-kb (already mapped) and il-6 (already mapped) and tnf-alpha (already mapped) cascade of panic disorder."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "Panic tgf-beta: TGF-β from neurons (already mapped) and astrocytes (already mapped) regulates neuroinflammatory fibrosis in panic circuits; tgf-beta excess amplifies nf-kb (already mapped) and il-6 (already mapped) and tnf-alpha (already mapped) cascade of panic disorder."
  - target: 01-human/03-molecular/calcitonin
    relation: connects-to
    note: "Panic calcitonin: calcitonin from neurons (already mapped) and astrocytes (already mapped) modulates calcium tone in panic circuits; calcitonin dysregulation amplifies nf-kb (already mapped) and il-6 (already mapped) and tnf-alpha (already mapped) cascade of panic disorder."
  - target: 01-human/03-molecular/insulin-receptor
    relation: connects-to
    note: "Panic insulin-receptor: insulin receptor on neurons (already mapped) and astrocytes (already mapped) drives stress-circuit metabolic repair; insulin-receptor loss amplifies nf-kb (already mapped) and il-6 (already mapped) and tnf-alpha (already mapped) cascade of panic disorder."
  - target: 01-human/03-molecular/aldosterone
    relation: connects-to
    note: "Panic aldosterone: aldosterone from neurons (already mapped) and astrocytes (already mapped) modulates stress-circuit ion balance; aldosterone excess amplifies nf-kb (already mapped) and il-6 (already mapped) and tnf-alpha (already mapped) cascade of panic disorder."
  - target: 01-human/03-molecular/androgen-receptor
    relation: connects-to
    note: "Panic androgen-receptor: androgen receptor on neurons (already mapped) and astrocytes (already mapped) modulates steroid signalling; androgen-receptor loss amplifies nf-kb (already mapped) and il-6 (already mapped) and tnf-alpha (already mapped) cascade of panic disorder."
  - target: 01-human/03-molecular/adrenomedullin
    relation: connects-to
    note: "Panic adrenomedullin: Adrenomedullin from neurons (already mapped) and astrocytes (already mapped) modulates panic vascular tone; adrenomedullin excess amplifies nf-kb (already mapped) and il-6 (already mapped) and tnf-alpha (already mapped) cascade of panic disorder."
  - target: 01-human/03-molecular/osteopontin
    relation: connects-to
    note: "Panic osteopontin: Osteopontin from neurons (already mapped) and astrocytes (already mapped) modulates panic matrix remodelling; osteopontin excess amplifies nf-kb (already mapped) and il-6 (already mapped) and tnf-alpha (already mapped) cascade of panic disorder."
  - target: 01-human/03-molecular/fgfr
    relation: connects-to
    note: "Panic fgfr: FGFR on neurons (already mapped) and astrocytes (already mapped) modulates panic neural growth; fgfr dysregulation amplifies nf-kb (already mapped) and il-6 (already mapped) and tnf-alpha (already mapped) cascade of panic disorder."
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
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — Hormones modulate its attacks: panic symptoms can fluctuate with the menstrual cycle and emerge or worsen in pregnancy and the postpartum period, reflecting hormonal influences on anxiety.
- `connects-to` → **[Renal System](../renal-system/README.md)** — Overbreathing and its drugs shift chemistry: hyperventilation during attacks causes respiratory alkalosis that the kidney buffers, and the SSRIs used to treat panic can cause hyponatraemia.
- `connects-to` → **[Immune System](../immune-system/README.md)** — Chronic anxiety inflames the body: persistent panic and stress raise inflammatory markers and dysregulate cortisol, linking the disorder to systemic inflammation over time.
- `connects-to` → **[Beta-blockers](../../../03-medicine/01-modern/04-cardio/beta-blockers/README.md)** — A heart drug for the body's alarm: beta-blockers like propranolol blunt the palpitations, tremor and sweating of a panic attack by blocking the adrenergic surge, though SSRIs treat the disorder itself.
- `connects-to` → **[Dietary Magnesium](../../../03-medicine/03-food/magnesium-dietary/README.md)** — A mineral linked to anxiety: low magnesium is associated with anxiety and panic, and supplementation is trialled as an adjunct, though the evidence is modest.
- `connects-to` → **[Ashwagandha](../../../03-medicine/02-traditional/ashwagandha/README.md)** — Traditional calm is sought for it: ashwagandha and other adaptogens are used for anxiety with some evidence of benefit, complementing rather than replacing established panic-disorder treatment.
- `connects-to` → **[Fibromyalgia](../fibromyalgia/README.md)** — Anxiety and bodily symptoms overlap: panic disorder is markedly more common in fibromyalgia, the two sharing central sensitisation, autonomic dysregulation and a heavy symptom burden.
- `connects-to` → **[Omega-3 Fatty Acids](../../../03-medicine/03-food/omega-3-fatty-acids/README.md)** — Diet offers a modest adjunct: omega-3 supplementation shows small anxiolytic effects in trials, used alongside but not instead of established treatment for panic disorder.
- `connects-to` → **[Borderline Personality Disorder](../borderline-personality-disorder/README.md)** — Panic rides with emotional dysregulation: panic attacks are frequent in borderline personality disorder, where affective instability and hyperarousal lower the threshold for acute anxiety surges.
- `connects-to` → **[Epilepsy](../epilepsy/README.md)** — Panic mimics and overlaps seizures: temporal-lobe epilepsy can produce fear and autonomic surges indistinguishable from a panic attack, and the two share limbic (amygdala-hippocampal) hyperexcitability and GABAergic dysfunction—an important diagnostic crossover.
- `connects-to` → **[Cardiac Conduction System](../../05-tissue/cardiac-conduction-system/README.md)** — Its symptoms feel cardiac: a panic attack floods the heart with adrenaline, causing palpitations, tachycardia and chest pain that mimic a supraventricular arrhythmia and send patients to the emergency room fearing a heart attack.
- `connects-to` → **[Binge-Eating Disorder](../binge-eating-disorder/README.md)** — Anxiety can drive the binge: panic disorder and other anxiety disorders frequently co-occur with binge-eating disorder, where acute distress and emotional dysregulation trigger loss-of-control eating as a maladaptive coping response.
- `connects-to` → **[Myocardium](../../05-tissue/myocardium/README.md)** — When panic mimics—and harms—the heart: panic attacks cause chest pain that mimics myocardial infarction, and extreme emotional stress can precipitate takotsubo stress cardiomyopathy of the myocardium.
- `connects-to` → **[Alveolus](../../05-tissue/alveolus/README.md)** — Hyperventilation and the suffocation alarm: panic drives hyperventilation that blows off CO2 into respiratory alkalosis, and brain CO2-sensing underlies the 'false suffocation alarm' theory of panic.
- `connects-to` → **[Peripheral Nerve](../../05-tissue/peripheral-nerve/README.md)** — Paraesthesiae and tetany: the respiratory alkalosis of a panic attack drops ionised calcium, hyperexciting peripheral nerves to cause the tingling, numbness and carpopedal spasm that frighten patients further.
- `connects-to` → **[Atherosclerosis](../atherosclerosis/README.md)** — The acute-coronary mimic: a panic attack's chest pain, palpitations and sweating imitate a heart attack, a leading reason for emergency cardiac workups, while chronic anxiety itself modestly raises atherosclerotic cardiovascular risk.
- `connects-to` → **[Venous Thromboembolism](../venous-thromboembolism/README.md)** — The can't-miss differential: pulmonary embolism causes sudden dyspnoea, tachycardia, chest pain and a sense of doom indistinguishable from a panic attack, the dangerous diagnosis to exclude before attributing symptoms to anxiety.
- `connects-to` → **[COVID-19 Disease](../covid-19-disease/README.md)** — A pandemic of anxiety: COVID-19 and its social upheaval drove a global surge in panic and anxiety disorders, and post-COVID breathlessness and palpitations can themselves trigger or mimic panic attacks.
- `connects-to` → **[NPY](../../03-molecular/npy/README.md)** — Resilience neuropeptide: neuropeptide Y dampens the stress and fear response, and reduced NPY signalling is associated with vulnerability to panic and anxiety.
- `connects-to` → **[Substance P](../../03-molecular/substance-p/README.md)** — Fear circuit signalling: substance P acting on NK1 receptors in the amygdala modulates fear and panic responses, an explored anxiolytic target.
- `connects-to` → **[Intestinal Epithelium](../../05-tissue/intestinal-epithelium/README.md)** — Gut-brain axis: panic disorder overlaps with irritable bowel syndrome, and signalling across the intestinal epithelium and microbiome feeds the fear and arousal circuits behind it.
- `connects-to` → **[Acetylcholine](../../03-molecular/acetylcholine/README.md)** — Cholinergic provocation: cholinergic agents can provoke panic-like attacks, and the cholinergic system modulates the respiratory and arousal circuits implicated in panic disorder.
- `connects-to` → **[IL-6](../../03-molecular/il-6/README.md)** — Inflammatory anxiety: elevated IL-6 is found in panic disorder, part of the bidirectional link between chronic anxiety and low-grade systemic inflammation.
- `connects-to` → **[TNF-α](../../03-molecular/tnf-alpha/README.md)** — Stress cytokine: raised TNF-α accompanies panic disorder, reflecting the neuroimmune activation increasingly implicated in anxiety disorders.
- `connects-to` → **[Serotonin transporter](../../03-molecular/serotonin-transporter/README.md)** — SSRIs that block the serotonin transporter are the pharmacological mainstay of panic disorder, and the 5-HTTLPR transporter polymorphism modulates both susceptibility to panic and the response to treatment.
- `connects-to` → **[μ-opioid receptor](../../03-molecular/mu-opioid-receptor/README.md)** — The opioidergic-deficit hypothesis holds that blunted endogenous opioid tone leaves the brainstem suffocation alarm hypersensitive to CO2, helping explain the spontaneous, unprovoked panic attacks that distinguish panic disorder from situational anxiety.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — IL-1β is among the inflammatory cytokines elevated in panic disorder, contributing to the HPA-axis activation and neuroimmune signaling that accompany recurrent panic and tie anxiety to systemic inflammation.
- `connects-to` → **[Endocannabinoid](../../03-molecular/endocannabinoid/README.md)** — Endocannabinoid signaling at amygdala CB1 receptors is essential for extinguishing conditioned fear, and a deficient endocannabinoid tone impairs the extinction learning whose failure perpetuates panic and anticipatory anxiety.
- `connects-to` → **[CGRP](../../03-molecular/cgrp/README.md)** — CGRP released from the parabrachial nucleus into the amygdala signals threat and arousal, and CGRP infusion provokes panic-like anxiety—a neuropeptide pathway linking panic disorder to the migraine with which it is comorbid.
- `connects-to` → **[Vasopressin](../../03-molecular/vasopressin/README.md)** — Arginine vasopressin co-secreted with CRH synergistically drives ACTH release at the V1b receptor, and this AVP arm of the stress axis is implicated in the heightened neuroendocrine reactivity of panic disorder.
- `connects-to` → **[β1-adrenergic receptor](../../03-molecular/beta1-adrenergic-receptor/README.md)** — The palpitations, tachycardia and chest discomfort of a panic attack arise from catecholamine activation of cardiac β1-adrenergic receptors, the target of the β-blockers used to blunt the peripheral symptoms that fuel catastrophic misinterpretation.
- `connects-to` → **[Glucocorticoid Receptor](../../03-molecular/glucocorticoid-receptor/README.md)** — Impaired glucocorticoid-receptor sensitivity weakens cortisol's negative feedback on the CRH-ACTH axis, sustaining the stress-hormone tone that lowers the threshold for panic in vulnerable individuals.
- `connects-to` → **[NLRP3 Inflammasome](../../03-molecular/nlrp3-inflammasome/README.md)** — Psychological stress activates the NLRP3 inflammasome to generate IL-1β, the upstream source of the inflammatory cytokines linked here to panic, connecting stress signaling to the low-grade neuroinflammation seen in anxiety disorders.
- `connects-to` → **[ACTH](../../03-molecular/acth/README.md)** — A panic attack drives CRH (mapped) to release pituitary ACTH, which raises cortisol (mapped), completing the stress-hormone axis engaged in panic disorder.
- `connects-to` → **[Histamine](../../03-molecular/histamine/README.md)** — Histaminergic neurons promote wakefulness and vigilance alongside orexin (mapped), and this arousal circuitry contributes to the hypervigilance and nocturnal panic attacks of panic disorder.
- `connects-to` → **[Interleukin-10](../../03-molecular/il-10/README.md)** — A relative deficit of regulatory IL-10 against the IL-6, IL-1β and TNF (all mapped) elevated in anxiety is part of the neuroinflammatory contribution to panic disorder.
- `connects-to` → **[TLR4](../../03-molecular/tlr4/README.md)** — TLR4-driven neuroinflammation links peripheral and central inflammation to the amygdala hyperexcitability implicated in the panic response.
- `connects-to` → **[NTRK](../../03-molecular/ntrk/README.md)** — BDNF signaling through its TrkB receptor (NTRK) mediates the amygdala-prefrontal fear-circuit plasticity whose dysregulation underlies panic disorder.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — Amygdala ERK-MAPK signaling consolidates the fear-conditioned memories that drive the recurrent, interoception-triggered attacks of panic disorder.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — BDNF/serotonergic PI3K-AKT-mTOR signaling supports the fear-circuit neuroplasticity that anxiolytic treatment restores in panic disorder.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Microglial galectin-3 reflects the low-grade neuroinflammation increasingly associated with panic disorder.
- `connects-to` → **[MYD88](../../03-molecular/myd88/README.md)** — TLR4-MyD88 innate signaling (TLR4 mapped) contributes to the neuroinflammation implicated in panic-disorder pathophysiology.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β signaling in fear and arousal circuits shapes the synaptic plasticity relevant to the heightened threat reactivity of panic disorder.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — IL-6-STAT3 signaling transduces the inflammatory tone associated with the heightened stress reactivity of panic disorder.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — Cytosolic mitochondrial DNA released during chronic stress can engage cGAS-STING, contributing to the neuroinflammation implicated in panic disorder.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — FOXO downstream of PI3K-AKT signaling (AKT already mapped) regulates neuronal oxidative-stress handling relevant to the fear-circuit dysregulation of panic disorder.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — IFN-STAT1 neuroinflammatory signaling contributes to the inflammatory tone associated with panic disorder.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — JAK1/2 signaling upstream of STAT3 (IL-6 already mapped) relays the inflammatory tone linked to the anxiety circuitry of panic disorder.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — PI3K (PIK3CA)-AKT signaling (AKT already mapped), downstream of BDNF-TrkB (BDNF and NTRK already mapped), participates in the fear-circuit neuroplasticity of panic disorder.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — mTOR signaling participates in the synaptic plasticity of the fear and anxiety circuits implicated in panic disorder.
- `connects-to` → **[Melatonin](../../03-molecular/melatonin/README.md)** — Melatonin and circadian signaling modulate the sleep-related and nocturnal-panic features of panic disorder.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK-linked metabolic signaling participates in the neurometabolic and stress-adaptation responses relevant to panic disorder.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — Autophagy modulates the neuronal stress resilience and fear-circuit homeostasis implicated in panic disorder.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — DNMT3A-mediated DNA methylation contributes to the epigenetic (early-life-stress) programming implicated in panic disorder.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-driven chemokine signaling participates in the neuroimmune and microglial responses implicated in panic disorder.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — CXCL12-CXCR4 signaling participates in the neuroimmune interactions implicated in panic disorder.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — IL-33 alarmin signaling participates in the neuroinflammatory responses implicated in panic disorder.
- `connects-to` → **[Thyroid hormones](../../03-molecular/thyroid-hormones/README.md)** — Endocrine mimic: thyrotoxicosis produces palpitations, tremor and anxiety that mimic and precipitate panic attacks, which is why thyroid-hormone screening is a standard part of the panic-disorder workup to exclude a treatable endocrine driver.
- `connects-to` → **[Angiotensin II](../../03-molecular/angiotensin-ii/README.md)** — Brain renin-angiotensin: central angiotensin II modulates sympathetic outflow and HPA-axis reactivity, and angiotensin blockade attenuates stress and anxiety responses, linking panic vulnerability to a neuroendocrine pressor axis beyond classical neurotransmitters.
- `connects-to` → **[Nitric oxide](../../03-molecular/nitric-oxide/README.md)** — Gaseous neurotransmission: nitric oxide signalling in the amygdala and periaqueductal grey shapes the fear and defensive responses underlying panic, and nNOS activity modulates the exaggerated CO2/chemosensory alarm that provokes attacks.
- `connects-to` → **[Proton](../../01-subatomic/proton/README.md)** — CO2 suffocation alarm: panic disorder features a hypersensitive suffocation alarm, and inhaled carbon dioxide or infused lactate, which shift acid-base balance by raising protons, reliably provoke attacks, implicating acid-base chemosensing in panic.
- `connects-to` → **[Insulin](../../03-molecular/insulin/README.md)** — Hypoglycaemia trigger: falling glucose from insulin action provokes an adrenergic counter-regulatory surge (epinephrine already mapped) whose palpitations, sweating and tremor mimic and can trigger panic attacks, one of the metabolic precipitants of panic.
- `connects-to` → **[Troponin complex](../../03-molecular/troponin-complex/README.md)** — Cardiac mimic: the chest pain, palpitations and tachycardia of a panic attack closely mimic myocardial infarction, so troponin is often measured to exclude it, and panic disorder is a frequent presentation to emergency cardiology.
- `connects-to` → **[Xanthine oxidase](../../03-molecular/xanthine-oxidase/README.md)** — Oxidative stress: anxiety disorders including panic are associated with heightened oxidative stress, to which xanthine oxidase contributes, and the resulting reactive oxygen species may affect the fear-circuit neurons and stress physiology.
- `connects-to` → **[Prostaglandins](../../03-molecular/prostaglandins/README.md)** — Neuroinflammation: prostaglandins from the low-grade neuroinflammation (IL-6 and IL-1 already mapped) linked to panic disorder modulate the fear circuitry and the autonomic and stress responses that generate panic attacks.
- `connects-to` → **[GLP-1](../../03-molecular/glp-1/README.md)** — Gut-brain interoception: GLP-1 signalling in the brainstem and hypothalamus links visceral and metabolic state to the interoceptive processing (insulin already mapped) whose misreading contributes to the bodily alarm of a panic attack.
- `connects-to` → **[Cholesterol](../../03-molecular/cholesterol/README.md)** — Metabolic association: panic disorder is associated with metabolic and cardiovascular findings, and the dyslipidaemia (insulin already mapped) that clusters with anxiety links lipid metabolism to the disorder and its cardiac risk.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Adipokine-stress link: the adipokine leptin, part of the appetite and stress-axis signalling (insulin already mapped), is altered in anxiety disorders, a metabolic dimension of the dysregulated fear and autonomic responses of panic disorder.
- `connects-to` → **[Ghrelin](../../03-molecular/ghrelin/README.md)** — Stress and appetite: ghrelin rises with stress and modulates the HPA (cortisol already mapped) and fear responses, and its dysregulation, with leptin (already mapped), links the appetite-stress axis to the anxiety of panic disorder.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — Neuroimmune balance: the anti-inflammatory IL-4, with IL-10 (already mapped), counters the pro-inflammatory cytokines (IL-6, TNF and IL-1 already mapped) of the low-grade neuroinflammation reported in panic and anxiety disorders.
- `connects-to` → **[Copper](../../02-atomic/copper/README.md)** — Copper and noradrenaline: copper is the cofactor of dopamine-β-hydroxylase, which makes noradrenaline from dopamine (both already mapped), linking copper handling to the noradrenergic (locus coeruleus) arousal that drives panic attacks.
- `connects-to` → **[Zinc](../../02-atomic/zinc/README.md)** — Zinc and NMDA: zinc modulates the glutamatergic (already mapped) NMDA receptors and has an anxiolytic role, and low zinc status is reported in anxiety disorders including panic disorder.
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — Type-2 neuroimmune arm: IL-13, with IL-4 (already mapped), is part of the type-2 immune arm balancing the neuroinflammation (TNF, IL-1 and IL-6 already mapped) increasingly implicated in panic disorder.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — Metabolic-inflammatory adipokine: adiponectin, with leptin (already mapped), links the metabolic-inflammatory state to the anxiety and neuroinflammation of panic disorder.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), is the pro-inflammatory adipokine of the metabolic-inflammatory milieu of panic disorder.
- `connects-to` → **[Type I interferon](../../03-molecular/type-i-interferon/README.md)** — Interferon-induced anxiety: the type-I interferon (therapy) induces the anxiety and mood symptoms, linking the innate-immune (cGAS-STING already mapped) signalling to the neuroinflammation of panic disorder.
- `connects-to` → **[IFN-gamma](../../03-molecular/ifn-gamma/README.md)** — Th1 neuroinflammation: the IFN-γ of the T cells is the type-II interferon arm of the low-grade neuroinflammation (TNF and IL-1 already mapped) associated with panic disorder.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the immune-inflammatory dimension implicated in panic disorder.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune dysregulation associated with panic disorder.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the immune-inflammatory dimension of panic disorder.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the low-grade inflammation associated with panic disorder.
- `connects-to` → **[Cytotoxic T cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Psychoneuroimmune arm: the peripheral cytotoxic T cells (perforin pathway) reflect the stress-associated adaptive immune activation of the psychoneuroimmunology of panic disorder.
- `connects-to` → **[Natural killer cell](../../04-cellular/natural-killer-cell/README.md)** — Stress-modulated NK: the NK-cell number and cytotoxicity are altered by the acute and chronic stress reactivity (cortisol and catecholamines already mapped) of panic disorder.
- `connects-to` → **[T-helper cell](../../04-cellular/t-helper-cell/README.md)** — CD4 cytokine source: the CD4 T-helper cells are the source of the Th1/Th2/Th17 (IFN-γ, IL-4 and IL-17 already mapped) cytokines of the low-grade inflammation associated with panic disorder.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Neuroimmune complement: the complement C3 activation is part of the low-grade innate inflammation and the neuroinflammatory dimension implicated in panic disorder.
- `connects-to` → **[C5aR1](../../03-molecular/c5ar1/README.md)** — C5a receptor: the C5aR1 signalling (with the complement C3 already mapped) contributes to the innate inflammatory dimension of the neuroimmune interaction in panic disorder.
- `connects-to` → **[Dendritic cell](../../04-cellular/dendritic-cell/README.md)** — CNS-border antigen presentation: the dendritic cells of the CNS-border compartments are part of the neuroimmune interface implicated in the low-grade inflammation of panic disorder.
- `connects-to` → **[TSLP](../../03-molecular/tslp/README.md)** — Airway-CNS axis: TSLP-driven airway inflammation underpins the asthma-panic disorder comorbidity; the shared sensitisation of the brainstem's CO2-sensitive locus coeruleus by airway alarmins links asthma and panic attacks.
- `connects-to` → **[Bradykinin](../../03-molecular/bradykinin/README.md)** — Dyspnoea–panic trigger: bradykinin, released during respiratory inflammation, activates bronchial C-fibres that signal brainstem suffocation-detection circuits, directly precipitating panic attacks in sensitised individuals.
- `connects-to` → **[Complement C5](../../03-molecular/complement-c5/README.md)** — Terminal neuroinflammation: C5 cleavage generates C5a, which via C5aR1 (already mapped) amplifies the low-grade neuroinflammation of the locus coeruleus and limbic circuits that regulate the fear-suffocation alarm implicated in panic disorder.
- `connects-to` → **[C1-Esterase Inhibitor](../../03-molecular/c1-esterase-inhibitor/README.md)** — Kallikrein-kinin control: C1-esterase inhibitor modulates the kallikrein-kinin system (bradykinin already mapped) and the classical complement (C3/C5 already mapped), constraining the neuroimmune contact cascade implicated in panic attacks.
- `connects-to` → **[Erythropoietin](../../03-molecular/erythropoietin/README.md)** — Neuroprotective EPO axis: erythropoietin, acting through EPOR in the brain, exerts neuroprotective and anxiolytic effects on the amygdala and hippocampus (already mapped), attenuating fear-memory consolidation in panic-disorder circuits.
- `connects-to` → **[Prolactin](../../03-molecular/prolactin/README.md)** — Post-attack anxiolytic: prolactin surges after panic attacks, exerting acute anxiolytic effects via the GABAergic (GABA already mapped) and serotonin (already mapped) systems, modulating the neuroendocrine recovery phase after panic episodes.
- `connects-to` → **[Testosterone](../../03-molecular/testosterone/README.md)** — Panic testosterone axis: testosterone exerts anxiolytic effects via androgen receptor in the amygdala (already mapped) and hippocampus (already mapped), modulating the HPA-axis CRH (already mapped) response and GABAergic interneuron activity in panic-disorder circuits.
- `connects-to` → **[Selenium](../../02-atomic/selenium/README.md)** — Panic selenium: selenium via GPX4 and selenoproteins reduces oxidative stress in amygdala (already mapped) and locus coeruleus neurons, attenuating the noradrenergic and serotonin (already mapped) circuit vulnerability of panic disorder.
- `connects-to` → **[Transferrin](../../03-molecular/transferrin/README.md)** — Panic iron axis: transferrin-mediated iron delivery is required for tryptophan hydroxylase (for serotonin already mapped) and tyrosine hydroxylase (for dopamine already mapped) activity in the raphe nuclei and locus coeruleus; iron deficiency amplifies panic-disorder risk.
- `connects-to` → **[Iodine](../../02-atomic/iodine/README.md)** — Panic iodine: iodine via thyroid hormones (already mapped) modulates the HPA-axis CRH (already mapped) and amygdala (already mapped) noradrenergic responsiveness; sub-clinical hypothyroidism amplifies panic-disorder vulnerability through HPA-axis dysregulation.
- `connects-to` → **[Potassium](../../02-atomic/potassium/README.md)** — Panic potassium: potassium via Kv4.3/Kir3 neuronal channels regulates amygdala (already mapped) and hippocampus (already mapped) action-potential firing thresholds; hypokalaemia amplifies the GABAergic (already mapped) interneuron dysregulation of panic disorder.
- `connects-to` → **[Phosphorus](../../02-atomic/phosphorus/README.md)** — Panic phosphorus: phosphorus as ATP and cAMP-PKA in amygdala (already mapped) and locus coeruleus neurons powers the norepinephrine (already mapped) and GABA (already mapped) neurotransmitter cascades that govern the panic-attack threshold in panic disorder.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Panic disorder iron: iron, as cofactor of monoamine oxidase in neurons (already mapped) and microglia (already mapped), supports monoamine catabolism; iron deficiency amplifies the NF-κB (already mapped) and TNF-α (already mapped) neuroinflammatory cascade of panic disorder.
- `connects-to` → **[Chloride](../../02-atomic/chloride/README.md)** — Panic disorder chloride: chloride via GABA-A Cl⁻ channels on neurons (already mapped) and astrocytes (already mapped) sets inhibitory tone; chloride dysregulation impairs GABAergic control, amplifying the NF-κB (already mapped) hyperexcitability cascade of panic disorder.
- `connects-to` → **[Sulfur](../../02-atomic/sulfur/README.md)** — Panic disorder sulfur: sulfur, as component of glutathione in neurons (already mapped) and astrocytes (already mapped), buffers oxidative stress; sulfur deficiency amplifies the NF-κB (already mapped) and TNF-α (already mapped) neuroinflammatory cascade of panic disorder.
- `connects-to` → **[Nitrogen](../../02-atomic/nitrogen/README.md)** — Panic disorder nitrogen: nitrogen is the backbone of GABA (already mapped) and glutamate (already mapped) in neurons (already mapped); nitrogen deficiency amplifies the NF-κB (already mapped) and TNF-α (already mapped) neuroinflammatory cascade of panic disorder.
- `connects-to` → **[Oxygen](../../02-atomic/oxygen/README.md)** — Panic disorder oxygen: oxygen powers neuron (already mapped) and astrocyte (already mapped) mitochondria in the corticolimbic circuit; hypoxic stress amplifies the NF-κB (already mapped) and TNF-α (already mapped) neuroinflammatory cascade of panic disorder.
- `connects-to` → **[Dopamine](../../03-molecular/dopamine/README.md)** — Panic disorder dopamine: dopamine modulates norepinephrine (already mapped) release and fear-salience signalling in the locus coeruleus; dopamine dysregulation amplifies the NF-κB (already mapped) and TNF-α (already mapped) neuroinflammatory tone of panic disorder.
- `connects-to` → **[PD-1](../../03-molecular/pd-1/README.md)** — Panic disorder PD-1: PD-1 checkpoint expression on microglia (already mapped) and T-cells modulates corticolimbic neuroinflammatory tone; PD-1 dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) neuroinflammatory cascade of panic disorder.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — Panic disorder VEGF: VEGF promotes neurovascular remodelling in the amygdala and cortex; VEGF dysregulation amplifies NF-κB (already mapped) and TNF-α (already mapped) neuroinflammatory signalling and impairs neurotrophic repair in panic disorder.
- `connects-to` → **[Wnt/β-catenin](../../03-molecular/wnt-beta-catenin/README.md)** — Panic disorder Wnt/β-catenin: Wnt/β-catenin signalling supports neuronal (already mapped) survival and synaptic plasticity in the corticolimbic circuit; Wnt dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) neuroinflammatory cascade of panic disorder.
- `connects-to` → **[RANKL](../../03-molecular/rankl/README.md)** — Panic disorder RANKL: RANKL from T-cells (already mapped) in corticolimbic microglia (already mapped) modulates bone-immune crosstalk; RANKL excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) cascade of panic disorder.
- `connects-to` → **[SMAD4](../../03-molecular/smad4/README.md)** — Panic disorder SMAD4: SMAD4-mediated TGF-β (already mapped) signalling in neurons (already mapped) and microglia (already mapped) regulates corticolimbic neuroinflammation; SMAD4 dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) cascade of panic disorder.
- `connects-to` → **[IL-2](../../03-molecular/il-2/README.md)** — Panic disorder IL-2: IL-2 from T-cells (already mapped) in corticolimbic microglia (already mapped) modulates neuroinflammatory tone; IL-2 excess amplifies NF-κB (already mapped) and TNF-α (already mapped) and CRH (already mapped) neuroinflammatory cascade of panic disorder.
- `connects-to` → **[Fibronectin](../../03-molecular/fibronectin/README.md)** — Panic disorder fibronectin: fibronectin in fibroblasts (already mapped) and astrocytes (already mapped) anchors stress-circuit ECM; fibronectin excess amplifies nf-kb (already mapped) and il-6 (already mapped) and tnf-alpha (already mapped) cascade of panic disorder.
- `connects-to` → **[NOTCH](../../03-molecular/notch/README.md)** — Panic disorder notch: NOTCH on neurons (already mapped) and astrocytes (already mapped) regulates fear extinction plasticity; notch dysregulation amplifies nf-kb (already mapped) and il-6 (already mapped) and tnf-alpha (already mapped) cascade of panic disorder.
- `connects-to` → **[IGF-1](../../03-molecular/igf-1/README.md)** — Panic disorder igf-1: IGF-1 from fibroblasts (already mapped) and astrocytes (already mapped) modulates neuronal stress resilience; igf-1 dysregulation amplifies nf-kb (already mapped) and il-6 (already mapped) and tnf-alpha (already mapped) cascade of panic disorder.
- `connects-to` → **[Activin-A](../../03-molecular/activin-a/README.md)** — Panic activin-a: activin-A from neurons (already mapped) and astrocytes (already mapped) drives neuroinflammatory signalling in panic circuits; activin-a excess amplifies nf-kb (already mapped) and il-6 (already mapped) and tnf-alpha (already mapped) cascade of panic disorder.
- `connects-to` → **[TGF-β](../../03-molecular/tgf-beta/README.md)** — Panic tgf-beta: TGF-β from neurons (already mapped) and astrocytes (already mapped) regulates neuroinflammatory fibrosis in panic circuits; tgf-beta excess amplifies nf-kb (already mapped) and il-6 (already mapped) and tnf-alpha (already mapped) cascade of panic disorder.
- `connects-to` → **[Calcitonin](../../03-molecular/calcitonin/README.md)** — Panic calcitonin: calcitonin from neurons (already mapped) and astrocytes (already mapped) modulates calcium tone in panic circuits; calcitonin dysregulation amplifies nf-kb (already mapped) and il-6 (already mapped) and tnf-alpha (already mapped) cascade of panic disorder.
- `connects-to` → **[Insulin Receptor](../../03-molecular/insulin-receptor/README.md)** — Panic insulin-receptor: insulin receptor on neurons (already mapped) and astrocytes (already mapped) drives stress-circuit metabolic repair; insulin-receptor loss amplifies nf-kb (already mapped) and il-6 (already mapped) and tnf-alpha (already mapped) cascade of panic disorder.
- `connects-to` → **[Aldosterone](../../03-molecular/aldosterone/README.md)** — Panic aldosterone: aldosterone from neurons (already mapped) and astrocytes (already mapped) modulates stress-circuit ion balance; aldosterone excess amplifies nf-kb (already mapped) and il-6 (already mapped) and tnf-alpha (already mapped) cascade of panic disorder.
- `connects-to` → **[Androgen Receptor](../../03-molecular/androgen-receptor/README.md)** — Panic androgen-receptor: androgen receptor on neurons (already mapped) and astrocytes (already mapped) modulates steroid signalling; androgen-receptor loss amplifies nf-kb (already mapped) and il-6 (already mapped) and tnf-alpha (already mapped) cascade of panic disorder.
- `connects-to` → **[Adrenomedullin](../../03-molecular/adrenomedullin/README.md)** — Panic adrenomedullin: Adrenomedullin from neurons (already mapped) and astrocytes (already mapped) modulates panic vascular tone; adrenomedullin excess amplifies nf-kb (already mapped) and il-6 (already mapped) and tnf-alpha (already mapped) cascade of panic disorder.
- `connects-to` → **[Osteopontin](../../03-molecular/osteopontin/README.md)** — Panic osteopontin: Osteopontin from neurons (already mapped) and astrocytes (already mapped) modulates panic matrix remodelling; osteopontin excess amplifies nf-kb (already mapped) and il-6 (already mapped) and tnf-alpha (already mapped) cascade of panic disorder.
- `connects-to` → **[FGFR](../../03-molecular/fgfr/README.md)** — Panic fgfr: FGFR on neurons (already mapped) and astrocytes (already mapped) modulates panic neural growth; fgfr dysregulation amplifies nf-kb (already mapped) and il-6 (already mapped) and tnf-alpha (already mapped) cascade of panic disorder.

[^gorman-2000-panic-neurobiology]: Gorman JM, Kent JM, Sullivan GM, Coplan JD. Neuroanatomical hypothesis of panic disorder, revised. *Am J Psychiatry.* 2000;157(4):493-505. [doi:10.1176/appi.ajp.157.4.493](https://doi.org/10.1176/appi.ajp.157.4.493) · [PubMed 10739407](https://pubmed.ncbi.nlm.nih.gov/10739407/)
[^nardi-2009-clonazepam-panic]: Nardi AE, Freire RC, Zin WA. Panic disorder and control of breathing. *Respir Physiol Neurobiol.* 2009;167(1):133-143. [doi:10.1016/j.resp.2008.07.011](https://doi.org/10.1016/j.resp.2008.07.011) · [PubMed 18708168](https://pubmed.ncbi.nlm.nih.gov/18708168/)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
