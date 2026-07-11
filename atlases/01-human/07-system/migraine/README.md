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
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "Migraine with aura is linked to the heart's PFO: a patent foramen ovale (a small atrial shunt) is more common in aura migraineurs, and migraine with aura independently raises stroke risk—tying the headache to cardiovascular and structural heart findings."
  - target: 01-human/02-atomic/potassium
    relation: connects-to
    note: "Migraine aura is a wave of potassium and glutamate: cortical spreading depression—a slow tide of neuronal depolarization with surging extracellular potassium—sweeps across the cortex, producing the visual aura before the headache."
  - target: 01-human/03-molecular/histamine
    relation: connects-to
    note: "Histamine can trigger migraine: it dilates cerebral vessels and activates trigeminal pain pathways, so histamine-rich foods and mast-cell release provoke attacks in susceptible people—one of many vasoactive triggers."
  - target: 01-human/03-molecular/adenosine
    relation: connects-to
    note: "Adenosine helps explain caffeine's grip on migraine: adenosine levels rise during attacks and dilate cerebral vessels, and because caffeine blocks adenosine receptors it can both abort a headache and, on withdrawal, trigger one."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "Mast cells inflame the migraine brain's lining: in the meninges they degranulate, releasing histamine and other mediators that sensitize trigeminal pain fibers, a cellular source of the neurogenic inflammation behind throbbing pain."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "Migraine, especially with aura, marks the blood vessel lining: endothelial dysfunction accompanies attacks and helps explain the raised stroke risk in aura migraineurs, tying the headache to the health of cerebral vessels."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Light is both trigger and torment in migraine: photons reaching the retina feed a pathway to the thalamus that intensifies headache, so photophobia is a core symptom and bright or flickering light can set an attack off."
  - target: 01-human/06-organ/stomach
    relation: connects-to
    note: "Migraine paralyzes the stomach: attacks bring nausea and vomiting and slow gastric emptying (gastroparesis), which delays oral painkiller absorption—why early or non-oral treatment works better in a severe attack."
  - target: 01-human/05-tissue/synapse
    relation: connects-to
    note: "Migraine aura is a wave across synapses: cortical spreading depression, a slow tide of neuronal and synaptic depolarization sweeping the cortex, produces the shimmering visual aura and primes the pain that follows."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "Migraine rides on sodium channels: the SCN1A sodium channel mutated in hemiplegic migraine, and the action of sodium valproate, tie the ion's flux to the cortical hyperexcitability that triggers attacks."
  - target: 01-human/05-tissue/peripheral-nerve
    relation: connects-to
    note: "Migraine pain travels the trigeminal nerve: this peripheral sensory nerve carries the throb from inflamed meningeal vessels, and nerve blocks and CGRP drugs that target it relieve attacks."
  - target: 01-human/06-organ/large-intestine
    relation: connects-to
    note: "Migraine travels with the gut: it overlaps heavily with irritable bowel syndrome, and shared serotonin signaling along the gut-brain axis links bowel symptoms to the headache disorder."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Migraine may be an energy disorder at the cell's core: evidence of mitochondrial dysfunction in migraine neurons underlies the use of riboflavin and coenzyme Q10 — boosters of the electron transport chain — as preventives."
  - target: 03-medicine/03-food/vitamin-d
    relation: connects-to
    note: "Vitamin D shadows the migraine brain: deficiency is associated with more frequent attacks, and supplementation has shown modest benefit, fitting the vitamin's role in calming neuronal excitability and inflammation."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "Migraine can make the skin hurt: cutaneous allodynia, where a light touch to the scalp or face becomes painful during an attack, signals central sensitization and predicts a poorer response to late treatment."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "Migraine prevention turned to antibodies: monoclonal antibodies against CGRP or its receptor (erenumab, fremanezumab, galcanezumab) are the first drugs designed specifically to prevent migraine, blocking the peptide that drives the attack."
  - target: 01-human/03-molecular/melatonin
    relation: connects-to
    note: "Migraine keeps time with sleep: too little or too much sleep is a classic trigger, the hypothalamus links it to the circadian clock, and melatonin has shown promise as a simple preventive."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "Hormones rule many migraines: estrogen withdrawal before menstruation triggers attacks, migraine often eases in pregnancy and after menopause, and migraine with aura plus estrogen contraception raises stroke risk enough to change prescribing."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "Migraine, especially with aura, is a vascular risk: it modestly raises the odds of stroke and heart attack, and the vasoconstricting triptans are avoided in established coronary or cerebrovascular disease."
  - target: 01-human/04-cellular/platelet
    relation: connects-to
    note: "Platelets carry a migraine clue: they store and release serotonin, and platelet activation and aggregation are heightened in migraine, one strand of the serotonin theory that links the disorder to its vascular changes."
  - target: 01-human/03-molecular/epinephrine
    relation: connects-to
    note: "Stress and its let-down trigger attacks: surges and withdrawals of adrenergic tone help precipitate migraines, and the autonomic features — pallor, nausea, and a racing or sluggish pulse — color the attack."
  - target: 01-human/03-molecular/substance-p
    relation: connects-to
    note: "Substance P inflames the meninges: released with CGRP from trigeminal nerve endings, it drives the neurogenic inflammation — vasodilation, plasma leak, and mast-cell activation — that sensitizes the pain fibers in a migraine."
  - target: 01-human/04-cellular/smooth-muscle-cell
    relation: connects-to
    note: "The cranial vessels' muscle joins the attack: vascular smooth muscle in the meningeal and cerebral arteries dilates under CGRP and nitric oxide, the throbbing component of migraine and a target of the older vasoconstrictor triptans."
  - target: 01-human/07-system/bipolar-disorder
    relation: connects-to
    note: "Migraine and bipolar disorder run together: they share a strong comorbidity and overlapping ion-channel and serotonin biology, and several mood stabilizers (valproate, topiramate) treat both conditions."
  - target: 01-human/03-molecular/calcitonin
    relation: connects-to
    note: "Migraine's key peptide is the calcitonin gene's other product: CGRP arises from alternative splicing of the CALCA gene that also encodes calcitonin, linking the headache's central mediator to calcium-regulating peptide biology."
  - target: 01-human/07-system/obesity
    relation: connects-to
    note: "Obesity worsens migraine: it roughly triples the risk of episodic migraine progressing to chronic daily headache, via adipose-driven inflammation and shared CGRP/leptin signalling — making weight a modifiable factor in headache frequency."
  - target: 01-human/07-system/ptsd
    relation: connects-to
    note: "Trauma and migraine reinforce each other: PTSD is markedly over-represented among people with migraine, especially chronic and medication-overuse forms, with shared stress-axis and serotonergic dysregulation worsening both."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "Neurogenic inflammation runs on NF-κB: activation of the trigeminovascular system releases CGRP and triggers NF-κB-driven cytokine production in the meninges, the sterile neuroinflammation that sustains a migraine attack."
  - target: 01-human/07-system/panic-disorder
    relation: connects-to
    note: "Headache and panic keep close company: panic disorder is far more common in people with migraine, the two sharing serotonergic and autonomic dysregulation that makes each more frequent and harder to treat."
  - target: 01-human/07-system/asthma
    relation: connects-to
    note: "Two episodic inflammatory disorders travel together: migraine and asthma co-occur more than chance, sharing mast-cell and inflammatory biology, and asthma predicts the progression of episodic migraine to chronic."
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "Overusing painkillers scars the kidney: the chronic NSAID and combination-analgesic use of frequent migraine can cause analgesic nephropathy, a slow interstitial injury that progresses to chronic kidney disease."
  - target: 01-human/07-system/social-anxiety-disorder
    relation: connects-to
    note: "Unpredictable attacks breed social fear: migraine carries elevated rates of social anxiety, as the fear of being struck by disabling head pain in public fosters avoidance, sharing serotonergic dysregulation."
  - target: 01-human/07-system/obsessive-compulsive-disorder
    relation: connects-to
    note: "Shared serotonergic wiring links them: OCD is over-represented among people with migraine, the two sharing serotonin-system dysregulation that underlies both the headache and the intrusive-thought disorder."
  - target: 01-human/07-system/atherosclerosis
    relation: connects-to
    note: "Aura signals vascular dysfunction: migraine with aura is associated with endothelial dysfunction and accelerated atherosclerosis, part of why it carries elevated cardiovascular and cerebrovascular risk."
  - target: 01-human/07-system/hypertension
    relation: connects-to
    note: "Headache and blood pressure travel together: migraine and hypertension are bidirectionally comorbid, and uncontrolled hypertension can worsen headache while some antihypertensives double as migraine prophylaxis."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "Aura plus estrogen raises the clot risk: migraine with aura carries a prothrombotic tendency, and combined with estrogen-containing contraception it elevates the risk of venous thromboembolism, prompting caution in prescribing."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "Hormones drive a major migraine subtype: oestrogen withdrawal around menstruation triggers menstrual migraine, and the swings of puberty, pregnancy and menopause reshape its pattern across a woman's life."
  - target: 01-human/07-system/gut-microbiome
    relation: connects-to
    note: "The gut-brain axis modulates attacks: migraine is strongly tied to the gut through nausea, abdominal migraine and cyclic vomiting, and the microbiome and gut-brain signalling influence its frequency."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "Neck and jaw feed the headache: migraine is highly comorbid with neck pain and temporomandibular disorder, with cervical muscle and joint dysfunction both triggering and amplifying attacks."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "The skin turns painful to touch: cutaneous allodynia — scalp and skin hypersensitivity so that brushing hair or wearing glasses hurts — is a hallmark of central sensitisation during migraine attacks."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "Its painkillers can harm the kidney: frequent NSAID use for migraine risks analgesic nephropathy and acute kidney injury, and renal impairment limits which abortive drugs are safe."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "It runs on neurogenic inflammation: the trigeminovascular system releases CGRP and inflammatory mediators that dilate vessels and sensitise nerves, a process now blocked by anti-CGRP therapies."
  - target: 03-medicine/01-modern/04-cardio/beta-blockers
    relation: connects-to
    note: "First-line prevention borrows a heart drug: beta-blockers like propranolol are a mainstay of migraine prophylaxis, reducing attack frequency though their mechanism in migraine is incompletely understood."
  - target: 03-medicine/03-food/magnesium-dietary
    relation: connects-to
    note: "A supplement with real evidence: magnesium is one of the better-supported nutritional prophylactics for migraine, and low magnesium status is linked to attack susceptibility."
  - target: 01-human/07-system/lymphatic-system
    relation: connects-to
    note: "Waste clearance may matter: dysfunction of the brain's glymphatic drainage system is increasingly implicated in migraine, linking sleep, fluid balance and headache."
  - target: 03-medicine/01-modern/04-cardio/aspirin
    relation: connects-to
    note: "A first-line acute treatment: high-dose aspirin and other NSAIDs abort migraine attacks, and aspirin combined with caffeine and paracetamol is a common over-the-counter option."
  - target: 03-medicine/01-modern/04-cardio/arbs
    relation: connects-to
    note: "Blood-pressure drugs prevent attacks: the ARB candesartan, like beta-blockers, reduces migraine frequency, a useful preventive especially when hypertension coexists."
  - target: 01-human/07-system/multiple-sclerosis
    relation: connects-to
    note: "Headache shadows demyelination: migraine is more common in multiple sclerosis than in the general population, the two sharing neuroinflammatory and vascular mechanisms."
  - target: 03-medicine/01-modern/13-cancer/targeted-therapy
    relation: connects-to
    note: "Anti-CGRP biology transformed it: monoclonal antibodies against CGRP or its receptor (erenumab, fremanezumab) and oral gepants prevent and abort migraine by blocking the neuropeptide central to the trigeminovascular attack."
  - target: 01-human/05-tissue/arterial-wall
    relation: connects-to
    note: "It is a neurovascular disorder: migraine engages the trigeminovascular system and meningeal arteries, and migraine with aura raises the risk of ischaemic stroke and arterial-wall disease, especially with oestrogen and smoking."
  - target: 01-human/05-tissue/myocardium
    relation: connects-to
    note: "Its acute drugs squeeze the coronaries: triptans and ergots cause vasoconstriction and are contraindicated in coronary disease, and migraine with aura independently raises the risk of myocardial infarction."
  - target: 01-human/03-molecular/orexin
    relation: connects-to
    note: "The hypothalamic trigger: orexin signalling from the hypothalamus is implicated in migraine's premonitory phase—yawning, food craving and fatigue—and in the tight link between migraine and disrupted sleep."
  - target: 01-human/05-tissue/hippocampus
    relation: connects-to
    note: "Why chronic migraine clouds memory: repeated attacks and the stress of recurrent pain remodel the hippocampus, tying migraine to memory complaints and its comorbidity with anxiety and depression."
  - target: 01-human/06-organ/thyroid
    relation: connects-to
    note: "A two-way thyroid link: hypothyroidism is commoner in people with migraine and migraine commoner in thyroid disease, likely through shared autonomic and inflammatory pathways."
  - target: 01-human/07-system/antiphospholipid-syndrome
    relation: connects-to
    note: "Headache as an autoimmune clue: migraine—especially with aura—is common in antiphospholipid syndrome, where a hypercoagulable state and patent foramen ovale also raise the risk of aura-associated stroke."
  - target: 01-human/07-system/narcolepsy
    relation: connects-to
    note: "Headache and the sleep switch: migraine is markedly more common in narcolepsy and other sleep disorders, sharing hypothalamic and orexinergic dysregulation that links sleep-wake control to headache."
  - target: 01-human/07-system/covid-19-disease
    relation: connects-to
    note: "Headache of infection: headache is among the commonest COVID-19 symptoms, and the infection can trigger new daily persistent headache or worsen pre-existing migraine."
  - target: 01-human/07-system/opioid-use-disorder
    relation: connects-to
    note: "Medication-overuse headache: opioids worsen migraine and transform it into chronic daily headache while risking dependence, the main reason they are avoided in headache management."
  - target: 01-human/07-system/anorexia-nervosa
    relation: connects-to
    note: "A serotonergic, female-predominant overlap: migraine co-occurs with eating disorders such as anorexia nervosa, sharing serotonergic dysregulation, while meal-skipping and dehydration are potent migraine triggers."
  - target: 01-human/05-tissue/endocardium
    relation: connects-to
    note: "Patent foramen ovale: migraine with aura is associated with a patent foramen ovale in the atrial septum, whose right-to-left shunt lets vasoactive substances and paradoxical emboli bypass the lungs."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "Neurogenic inflammation: IL-6 released during the sterile neurogenic inflammation around meningeal vessels contributes to the sensitisation and pain of a migraine attack."
  - target: 01-human/03-molecular/tnf-alpha
    relation: connects-to
    note: "Inflammatory sensitisation: TNF-α is elevated during migraine and helps sensitise trigeminal nociceptors, part of the inflammatory cascade that sustains the headache."
  - target: 01-human/03-molecular/norepinephrine
    relation: connects-to
    note: "Brainstem modulation: noradrenergic signalling from the locus coeruleus modulates cerebral blood flow and pain processing in migraine, and its dysregulation features in the autonomic symptoms of attacks."
  - target: 01-human/03-molecular/prostaglandins
    relation: connects-to
    note: "Neurogenic inflammation: prostaglandins sensitise and excite trigeminal nociceptors and dilate meningeal vessels during migraine, which is why NSAIDs that block their synthesis abort attacks."
  - target: 01-human/03-molecular/endothelin-1
    relation: connects-to
    note: "Vascular dysregulation: endothelin-1 contributes to the meningeal and cerebral vascular tone changes of migraine, part of the neurovascular dysfunction underlying the headache and aura."
  - target: 01-human/03-molecular/serotonin-transporter
    relation: connects-to
    note: "Serotonergic comorbidity: serotonin-transporter function links migraine to its frequent depression and anxiety comorbidity and shapes the serotonergic descending pain modulation triptans engage."
  - target: 01-human/03-molecular/progesterone
    relation: connects-to
    note: "Hormonal triggering: the estrogen-progesterone fluctuations of the menstrual cycle drive menstrual migraine, with the perimenstrual estrogen withdrawal (and shifting progesterone) precipitating attacks in many women."
  - target: 01-human/03-molecular/bradykinin
    relation: connects-to
    note: "Trigeminovascular sensitisation: bradykinin generated in the meninges sensitises and excites trigeminal nociceptors, part of the neurogenic inflammation that produces the throbbing pain of migraine."
  - target: 01-human/03-molecular/atp
    relation: connects-to
    note: "Bioenergetic deficit: the mitochondrial-energy-deficit hypothesis links migraine susceptibility to impaired ATP production in neurons, the rationale behind riboflavin and coenzyme Q10 as preventives."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Calcium-channel migraine: mutations in the P/Q-type calcium channel gene CACNA1A cause familial hemiplegic migraine type 1, directly linking dysregulated neuronal calcium currents and glutamate release to the cortical spreading depression of migraine aura."
  - target: 01-human/03-molecular/kit
    relation: connects-to
    note: "Meningeal mast cells: KIT-dependent mast cells in the dura degranulate to release histamine, tryptase and cytokines that sensitise trigeminal nociceptors, an arm of the neurogenic meningeal inflammation that generates migraine pain."
  - target: 01-human/03-molecular/oxytocin
    relation: connects-to
    note: "Trigeminal modulation: oxytocin acting on trigeminal-ganglion receptors inhibits nociceptive signalling and CGRP release, the basis for intranasal oxytocin being explored as a migraine treatment and a possible mediator of hormonal migraine patterns."
  - target: 01-human/03-molecular/connexin43
    relation: connects-to
    note: "Cortical spreading depression: astrocytic connexin-43 gap junctions propagate the slow wave of depolarisation — cortical spreading depression — that underlies the migraine aura."
  - target: 01-human/03-molecular/nlrp3-inflammasome
    relation: connects-to
    note: "Sterile neuroinflammation: cortical spreading depression activates the NLRP3 inflammasome and IL-1β in microglia (already mapped), driving the sterile neuroinflammation that sensitises the trigeminovascular pain pathway in migraine."
  - target: 01-human/03-molecular/crh
    relation: connects-to
    note: "Stress trigger: stress is a major migraine trigger, and CRH-driven HPA-axis activation lowers the threshold for attacks, linking the stress system to migraine susceptibility."
  - target: 01-human/03-molecular/tlr4
    relation: connects-to
    note: "Neurogenic inflammation: TLR4-driven neuroinflammation in the trigeminovascular system sensitises meningeal nociceptors, contributing to the neurogenic inflammation that sustains the migraine attack."
  - target: 01-human/03-molecular/ntrk
    relation: connects-to
    note: "Central sensitisation: BDNF signalling through its TrkB receptor (NTRK) mediates the central sensitisation of trigeminal pain pathways that underlies the allodynia and chronification of migraine."
  - target: 01-human/03-molecular/nfe2l2
    relation: connects-to
    note: "Oxidative susceptibility: NRF2-regulated antioxidant defences counter the oxidative stress implicated in migraine pathophysiology and in the metabolic vulnerability to cortical spreading depression."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "ERK-MAPK activation in trigeminal neurons mediates the central sensitisation and CGRP-related signalling (CGRP mapped) that sustain migraine pain."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "PI3K-AKT signalling participates in trigeminovascular neuronal excitability and the neurogenic inflammation underlying migraine attacks."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Microglial galectin-3 reflects the neuroinflammatory activation increasingly implicated in migraine chronification."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "IL-6-STAT3 signalling transduces the neuroinflammatory tone implicated in trigeminovascular sensitisation and migraine chronification."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "GSK-3β signalling modulates neuronal excitability relevant to the cortical spreading depression that underlies migraine aura."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "Cytosolic DNA released by neuronal and glial stress can engage cGAS-STING, contributing to the neuroinflammation associated with chronic migraine."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "FOXO downstream of PI3K-AKT signaling (AKT already mapped) regulates neuronal oxidative-stress handling relevant to the cortical excitability of migraine."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "IFN-STAT1 neuroinflammatory signaling contributes to the trigeminovascular inflammation implicated in migraine."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "JAK1/2 signaling upstream of STAT3 (IL-6 already mapped) relays the neuroinflammatory tone associated with chronic migraine."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "HIF-1α responses to the metabolic and hypoxic stress of cortical spreading depression contribute to migraine pathophysiology."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "S100A8/A9 alarmins reflect the neurogenic and meningeal inflammatory activation implicated in migraine."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "PI3K (PIK3CA)-AKT signaling (AKT already mapped) participates in the neuronal excitability and trigeminal sensitization of migraine."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK-linked neuronal energy sensing participates in the metabolic-stress and cortical-excitability mechanisms of migraine."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Autophagy modulates the neuronal and glial homeostasis relevant to the cortical spreading depression of migraine."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "DNMT3A-mediated DNA methylation contributes to the epigenetic regulation implicated in migraine susceptibility."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC-family kinase signaling participates in the neuronal-glial signaling and trigeminovascular sensitization of migraine."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-driven neuroimmune signaling participates in the neuroinflammation of migraine."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "CXCL12-CXCR4 signaling participates in the neuroimmune and trigeminovascular processes of migraine."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "IL-1β-driven neuroinflammation participates in the trigeminovascular sensitization of migraine."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "IL-33 alarmin signaling participates in the neuroinflammatory and mast-cell responses of migraine."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "IL-17A signaling participates in the neuroinflammation associated with migraine."
  - target: 01-human/03-molecular/beta1-adrenergic-receptor
    relation: connects-to
    note: "Beta-blocker prophylaxis: propranolol and metoprolol are first-line migraine preventives acting through beta-adrenergic blockade (norepinephrine already mapped), among the oldest effective prophylactic classes despite an incompletely understood mechanism."
  - target: 01-human/03-molecular/angiotensin-ii
    relation: connects-to
    note: "RAAS prophylaxis: the angiotensin-receptor blocker candesartan and ACE inhibitors reduce migraine frequency, implicating the renin-angiotensin system in migraine and providing a preventive option for patients with comorbid hypertension."
  - target: 01-human/03-molecular/testosterone
    relation: connects-to
    note: "Sex differences: migraine is far more common in women, and testosterone appears protective by dampening trigeminal nociception and cortical excitability (estrogen and progesterone already mapped), part of the hormonal basis of the sex disparity."
  - target: 01-human/03-molecular/mu-opioid-receptor
    relation: connects-to
    note: "Medication-overuse headache: opioids acting on the mu-opioid receptor relieve acute headache but, overused, cause medication-overuse headache and dependence, a major reason opioids are discouraged in migraine management."
  - target: 01-human/03-molecular/aldosterone
    relation: connects-to
    note: "Mineralocorticoid arm of the RAAS: alongside the angiotensin II already mapped, aldosterone and mineralocorticoid signalling are implicated in migraine, consistent with the preventive benefit of the renin-angiotensin blockade used in prophylaxis."
  - target: 01-human/03-molecular/insulin
    relation: connects-to
    note: "Metabolic association: migraine is associated with insulin resistance and the metabolic syndrome, and impaired brain energy metabolism is one proposed contributor to the neuronal hyperexcitability underlying attacks."
  - target: 01-human/03-molecular/xanthine-oxidase
    relation: connects-to
    note: "Oxidative and energy stress: mitochondrial dysfunction and oxidative stress, to which xanthine oxidase contributes, are implicated in the neuronal energy deficit and hyperexcitability of migraine (NRF2 already mapped), and antioxidant supplements are used in prophylaxis."
  - target: 01-human/03-molecular/cholesterol
    relation: connects-to
    note: "Vascular risk: migraine, especially with aura, is associated with dyslipidaemia and a raised risk of stroke and cardiovascular events (insulin already mapped), part of its vascular comorbidity."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Obesity link: obesity raises migraine frequency, and the adipokine leptin, with the low-grade inflammation (IL-6 and TNF already mapped) of excess adiposity, is one proposed mediator of the obesity-migraine association."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "Neuroimmune balance: the anti-inflammatory IL-4 counters the pro-inflammatory cytokines (IL-6, TNF and IL-1 already mapped) of the neurogenic inflammation implicated in migraine, part of its immune dimension."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "Zinc and neuronal excitability: zinc modulates the glutamatergic (already mapped) signalling and, with magnesium (already mapped), the neuronal excitability implicated in the cortical spreading depression of migraine."
  - target: 03-medicine/03-food/omega-3-fatty-acids
    relation: connects-to
    note: "Omega-3 prophylaxis: the omega-3 fatty acids give rise to pro-resolving mediators that counter the neurogenic inflammation (prostaglandins already mapped) of migraine, and dietary omega-3 has been studied for migraine prevention."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "Type-2 neuroimmunity: IL-13, with IL-4 (already mapped), supports the M2 microglial arm balancing the neurogenic inflammation (substance-P and CGRP already mapped) implicated in migraine."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Adipokine and chronic migraine: adiponectin, with leptin (already mapped), is part of the adipokine dimension of the obesity that is a risk factor for the transformation to chronic migraine."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), links the adipose-inflammatory milieu (IL-6 already mapped) to the chronic migraine associated with obesity."
  - target: 01-human/04-cellular/astrocyte
    relation: connects-to
    note: "Cortical spreading depression: the astrocytes propagate the cortical spreading depression (the aura; glutamate and connexin43 already mapped, the K+ waves) of migraine."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "Depression comorbidity: migraine and major depression are bidirectionally comorbid, sharing the serotonergic (already mapped) dysregulation."
  - target: 01-human/07-system/epilepsy
    relation: connects-to
    note: "Epilepsy comorbidity: migraine and epilepsy are comorbid, sharing the cortical hyperexcitability, the SCN1A (already mapped) channelopathies and the cortical spreading depression."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Innate neuroinflammation: the type-I interferon, downstream of the cGAS-STING (already mapped) pathway, is part of the sterile neuroinflammation (IL-1 and TNF already mapped) of the trigeminovascular activation of migraine."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Th1 neuroinflammation: the IFN-γ of the T cells is the type-II interferon arm of the immune-inflammatory dimension associated with migraine."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the immune-inflammatory dimension of migraine."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the neuroimmune interaction in migraine."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the neuroinflammatory dimension of migraine."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Type-2/mast-cell arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), arms the dural mast cells (already mapped) whose degranulation contributes to the neurogenic inflammation of migraine."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Meningeal complement: the complement C3 activation contributes to the dural neurogenic inflammation and the immune component of migraine."
  - target: 01-human/03-molecular/c5ar1
    relation: connects-to
    note: "C5a receptor: the C5aR1 signalling (with the complement C3 already mapped) links the complement to the mast-cell (already mapped) and myeloid activation of the neurogenic inflammation of migraine."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Psychoneuroimmune arm: the peripheral cytotoxic T cells (perforin pathway) reflect the adaptive-immune dimension of the neuroinflammatory interaction in migraine."
  - target: 01-human/03-molecular/complement-c5
    relation: connects-to
    note: "Terminal complement: the complement C5 and its C5a (with C3 and C5aR1 already mapped) are part of the complement activation of the neurogenic inflammation of migraine."
  - target: 01-human/03-molecular/factor-h
    relation: connects-to
    note: "Complement regulation: factor H regulates the alternative complement pathway (complement C3, C5 and C5aR1 already mapped) of the neuroinflammatory dimension of migraine."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "Meningeal antigen presentation: the dendritic cells of the meningeal and CNS-border compartments are part of the neuroimmune interface implicated in the neurogenic inflammation of migraine."
  - target: 01-human/03-molecular/tslp
    relation: connects-to
    note: "Alarmin-meningeal axis: TSLP, from meningeal mast cells (already mapped) and the trigeminal epithelium, primes dendritic cells (already mapped) and amplifies the neurogenic and meningeal inflammation underlying the migraine attack."
  - target: 01-human/03-molecular/c1-esterase-inhibitor
    relation: connects-to
    note: "Complement brake: C1-esterase inhibitor regulates the classical-complement and contact-pathway activation (complement C3, C5 and bradykinin already mapped) contributing to the neurogenic oedema and vasodilation of the migraine attack."
  - target: 01-human/03-molecular/erythropoietin
    relation: connects-to
    note: "Neuroprotective EPO: erythropoietin, via EpoR on neurons (already mapped) and microglia (already mapped), exerts anti-inflammatory and neuroprotective effects relevant to the central sensitisation and the chronic neuroinflammation of migraine."
  - target: 01-human/03-molecular/periostin
    relation: connects-to
    note: "Meningeal ECM: periostin, from meningeal fibroblasts and trigeminal-ganglion stroma, contributes to the extracellular-matrix remodelling at the meningeal neuroimmune interface of the neurogenic inflammation and sensitisation of migraine."
  - target: 01-human/03-molecular/prolactin
    relation: connects-to
    note: "Hormonal migraine trigger: prolactin modulates nociception via PRLR on trigeminal neurons (already mapped) and correlates with menstrual migraine, complementing the oestrogen/progesterone (already mapped) hormonal dimension of migraine susceptibility."
  - target: 01-human/03-molecular/transferrin
    relation: connects-to
    note: "Iron-migraine metabolism: transferrin, the iron carrier, reflects the iron deficiency that is a recognised migraine risk; dysregulated brain iron handling is linked to cortical spreading depression and the structural brain changes of chronic migraine."
  - target: 01-human/03-molecular/vasopressin
    relation: connects-to
    note: "Migraine vasopressin: vasopressin, via V1aR on neurons (already mapped) and endothelial cells (already mapped), modulates cerebral vasomotor tone; vasopressin dysregulation amplifies the CGRP (already mapped) and nitric-oxide (already mapped) vasoactive cascade of migraine."
  - target: 01-human/02-atomic/selenium
    relation: connects-to
    note: "Migraine selenium: selenium, as neuroprotective GPx in neurons (already mapped) and astrocytes (already mapped), scavenges neuroinflammatory ROS; selenium deficiency impairs GABA (already mapped) inhibitory tone and amplifies the cortical spreading depression of migraine."
  - target: 01-human/02-atomic/iodine
    relation: connects-to
    note: "Migraine iodine: iodine-dependent thyroid hormones modulate the serotonergic (serotonin already mapped) and dopaminergic (dopamine already mapped) pathways; iodine deficiency impairs the nitric-oxide (already mapped) and CGRP (already mapped) neurovascular axis of migraine."
  - target: 01-human/02-atomic/copper
    relation: connects-to
    note: "Migraine copper: copper, via dopamine-β-hydroxylase, supports dopamine (already mapped) and norepinephrine (already mapped) neurotransmission; copper deficiency impairs NF-κB (already mapped) antioxidant signalling and CGRP (already mapped) neurovascular axis of migraine."
  - target: 01-human/02-atomic/phosphorus
    relation: connects-to
    note: "Migraine phosphorus: phosphorus drives ATP (already mapped)-dependent synaptic (synapse already mapped) transmission in neurons (already mapped); phosphate dysregulation amplifies NLRP3 (already mapped) microglial (microglia already mapped) neuroinflammation and migraine attacks."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Migraine iron: iron is required for dopamine (already mapped) and serotonin (already mapped) synthesis; iron deficiency amplifies NF-κB (already mapped) and CGRP (already mapped) neuroinflammatory cascade and worsens cortical spreading depression and migraine attack burden."
  - target: 01-human/02-atomic/nitrogen
    relation: connects-to
    note: "Migraine nitrogen: nitric oxide (NO, nitrogen-derived) is a potent vasodilator and CGRP (already mapped) releaser in trigeminal neurons (already mapped); nitric-oxide excess amplifies NF-κB (already mapped) neuroinflammation and cortical-spreading-depression in migraine."
  - target: 01-human/02-atomic/chloride
    relation: connects-to
    note: "Migraine chloride: chloride via GABA(A) receptors (GABA already mapped) on neurons (already mapped) sets cortical inhibitory tone; chloride dysregulation amplifies glutamate (already mapped) and NF-κB (already mapped) and CGRP (already mapped) neuroinflammation in migraine."
  - target: 01-human/02-atomic/sulfur
    relation: connects-to
    note: "Migraine sulfur: H2S from sulfur-amino acids in trigeminal neurons (already mapped) and astrocytes (already mapped) modulates CGRP (already mapped) release; sulfur deficiency amplifies NF-κB (already mapped) and NLRP3 (already mapped) neuroinflammation in migraine."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "Migraine oxygen: mitochondrial oxygen sustains ATP in neurons (already mapped) and astrocytes (already mapped) for trigeminal signalling; hypoxia amplifies NLRP3 (already mapped) and NF-κB (already mapped) and CGRP (already mapped) neuroinflammatory cascade of migraine."
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
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — Migraine with aura is linked to the heart's PFO: a patent foramen ovale (a small atrial shunt) is more common in aura migraineurs, and migraine with aura independently raises stroke risk—tying the headache to cardiovascular and structural heart findings.
- `connects-to` → **[Potassium](../../02-atomic/potassium/README.md)** — Migraine aura is a wave of potassium and glutamate: cortical spreading depression—a slow tide of neuronal depolarization with surging extracellular potassium—sweeps across the cortex, producing the visual aura before the headache.
- `connects-to` → **[Histamine](../../03-molecular/histamine/README.md)** — Histamine can trigger migraine: it dilates cerebral vessels and activates trigeminal pain pathways, so histamine-rich foods and mast-cell release provoke attacks in susceptible people—one of many vasoactive triggers.
- `connects-to` → **[Adenosine](../../03-molecular/adenosine/README.md)** — Adenosine helps explain caffeine's grip on migraine: adenosine levels rise during attacks and dilate cerebral vessels, and because caffeine blocks adenosine receptors it can both abort a headache and, on withdrawal, trigger one.
- `connects-to` → **[Mast Cell](../../04-cellular/mast-cell/README.md)** — Mast cells inflame the migraine brain's lining: in the meninges they degranulate, releasing histamine and other mediators that sensitize trigeminal pain fibers, a cellular source of the neurogenic inflammation behind throbbing pain.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — Migraine, especially with aura, marks the blood vessel lining: endothelial dysfunction accompanies attacks and helps explain the raised stroke risk in aura migraineurs, tying the headache to the health of cerebral vessels.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Light is both trigger and torment in migraine: photons reaching the retina feed a pathway to the thalamus that intensifies headache, so photophobia is a core symptom and bright or flickering light can set an attack off.
- `connects-to` → **[Stomach](../../06-organ/stomach/README.md)** — Migraine paralyzes the stomach: attacks bring nausea and vomiting and slow gastric emptying (gastroparesis), which delays oral painkiller absorption—why early or non-oral treatment works better in a severe attack.
- `connects-to` → **[Synapse](../../05-tissue/synapse/README.md)** — Migraine aura is a wave across synapses: cortical spreading depression, a slow tide of neuronal and synaptic depolarization sweeping the cortex, produces the shimmering visual aura and primes the pain that follows.
- `connects-to` → **[Sodium](../../02-atomic/sodium/README.md)** — Migraine rides on sodium channels: the SCN1A sodium channel mutated in hemiplegic migraine, and the action of sodium valproate, tie the ion's flux to the cortical hyperexcitability that triggers attacks.
- `connects-to` → **[Peripheral Nerve](../../05-tissue/peripheral-nerve/README.md)** — Migraine pain travels the trigeminal nerve: this peripheral sensory nerve carries the throb from inflamed meningeal vessels, and nerve blocks and CGRP drugs that target it relieve attacks.
- `connects-to` → **[Large Intestine](../../06-organ/large-intestine/README.md)** — Migraine travels with the gut: it overlaps heavily with irritable bowel syndrome, and shared serotonin signaling along the gut-brain axis links bowel symptoms to the headache disorder.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Migraine may be an energy disorder at the cell's core: evidence of mitochondrial dysfunction in migraine neurons underlies the use of riboflavin and coenzyme Q10 — boosters of the electron transport chain — as preventives.
- `connects-to` → **[Vitamin D (Calciferol)](../../../03-medicine/03-food/vitamin-d/README.md)** — Vitamin D shadows the migraine brain: deficiency is associated with more frequent attacks, and supplementation has shown modest benefit, fitting the vitamin's role in calming neuronal excitability and inflammation.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — Migraine can make the skin hurt: cutaneous allodynia, where a light touch to the scalp or face becomes painful during an attack, signals central sensitization and predicts a poorer response to late treatment.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — Migraine prevention turned to antibodies: monoclonal antibodies against CGRP or its receptor (erenumab, fremanezumab, galcanezumab) are the first drugs designed specifically to prevent migraine, blocking the peptide that drives the attack.
- `connects-to` → **[Melatonin](../../03-molecular/melatonin/README.md)** — Migraine keeps time with sleep: too little or too much sleep is a classic trigger, the hypothalamus links it to the circadian clock, and melatonin has shown promise as a simple preventive.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — Hormones rule many migraines: estrogen withdrawal before menstruation triggers attacks, migraine often eases in pregnancy and after menopause, and migraine with aura plus estrogen contraception raises stroke risk enough to change prescribing.
- `connects-to` → **[Cardiovascular system](../cardiovascular-system/README.md)** — Migraine, especially with aura, is a vascular risk: it modestly raises the odds of stroke and heart attack, and the vasoconstricting triptans are avoided in established coronary or cerebrovascular disease.
- `connects-to` → **[Platelet](../../04-cellular/platelet/README.md)** — Platelets carry a migraine clue: they store and release serotonin, and platelet activation and aggregation are heightened in migraine, one strand of the serotonin theory that links the disorder to its vascular changes.
- `connects-to` → **[Epinephrine](../../03-molecular/epinephrine/README.md)** — Stress and its let-down trigger attacks: surges and withdrawals of adrenergic tone help precipitate migraines, and the autonomic features — pallor, nausea, and a racing or sluggish pulse — color the attack.
- `connects-to` → **[Substance P](../../03-molecular/substance-p/README.md)** — Substance P inflames the meninges: released with CGRP from trigeminal nerve endings, it drives the neurogenic inflammation — vasodilation, plasma leak, and mast-cell activation — that sensitizes the pain fibers in a migraine.
- `connects-to` → **[Smooth Muscle Cell](../../04-cellular/smooth-muscle-cell/README.md)** — The cranial vessels' muscle joins the attack: vascular smooth muscle in the meningeal and cerebral arteries dilates under CGRP and nitric oxide, the throbbing component of migraine and a target of the older vasoconstrictor triptans.
- `connects-to` → **[Bipolar Disorder](../bipolar-disorder/README.md)** — Migraine and bipolar disorder run together: they share a strong comorbidity and overlapping ion-channel and serotonin biology, and several mood stabilizers (valproate, topiramate) treat both conditions.
- `connects-to` → **[Calcitonin](../../03-molecular/calcitonin/README.md)** — Migraine's key peptide is the calcitonin gene's other product: CGRP arises from alternative splicing of the CALCA gene that also encodes calcitonin, linking the headache's central mediator to calcium-regulating peptide biology.
- `connects-to` → **[Obesity](../obesity/README.md)** — Obesity worsens migraine: it roughly triples the risk of episodic migraine progressing to chronic daily headache, via adipose-driven inflammation and shared CGRP/leptin signalling — making weight a modifiable factor in headache frequency.
- `connects-to` → **[PTSD](../ptsd/README.md)** — Trauma and migraine reinforce each other: PTSD is markedly over-represented among people with migraine, especially chronic and medication-overuse forms, with shared stress-axis and serotonergic dysregulation worsening both.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — Neurogenic inflammation runs on NF-κB: activation of the trigeminovascular system releases CGRP and triggers NF-κB-driven cytokine production in the meninges, the sterile neuroinflammation that sustains a migraine attack.
- `connects-to` → **[Panic Disorder](../panic-disorder/README.md)** — Headache and panic keep close company: panic disorder is far more common in people with migraine, the two sharing serotonergic and autonomic dysregulation that makes each more frequent and harder to treat.
- `connects-to` → **[Asthma](../asthma/README.md)** — Two episodic inflammatory disorders travel together: migraine and asthma co-occur more than chance, sharing mast-cell and inflammatory biology, and asthma predicts the progression of episodic migraine to chronic.
- `connects-to` → **[Chronic Kidney Disease](../ckd/README.md)** — Overusing painkillers scars the kidney: the chronic NSAID and combination-analgesic use of frequent migraine can cause analgesic nephropathy, a slow interstitial injury that progresses to chronic kidney disease.
- `connects-to` → **[Social Anxiety Disorder](../social-anxiety-disorder/README.md)** — Unpredictable attacks breed social fear: migraine carries elevated rates of social anxiety, as the fear of being struck by disabling head pain in public fosters avoidance, sharing serotonergic dysregulation.
- `connects-to` → **[Obsessive-Compulsive Disorder](../obsessive-compulsive-disorder/README.md)** — Shared serotonergic wiring links them: OCD is over-represented among people with migraine, the two sharing serotonin-system dysregulation that underlies both the headache and the intrusive-thought disorder.
- `connects-to` → **[Atherosclerosis](../atherosclerosis/README.md)** — Aura signals vascular dysfunction: migraine with aura is associated with endothelial dysfunction and accelerated atherosclerosis, part of why it carries elevated cardiovascular and cerebrovascular risk.
- `connects-to` → **[Hypertension](../hypertension/README.md)** — Headache and blood pressure travel together: migraine and hypertension are bidirectionally comorbid, and uncontrolled hypertension can worsen headache while some antihypertensives double as migraine prophylaxis.
- `connects-to` → **[Venous Thromboembolism](../venous-thromboembolism/README.md)** — Aura plus estrogen raises the clot risk: migraine with aura carries a prothrombotic tendency, and combined with estrogen-containing contraception it elevates the risk of venous thromboembolism, prompting caution in prescribing.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — Hormones drive a major migraine subtype: oestrogen withdrawal around menstruation triggers menstrual migraine, and the swings of puberty, pregnancy and menopause reshape its pattern across a woman's life.
- `connects-to` → **[Gut Microbiome](../gut-microbiome/README.md)** — The gut-brain axis modulates attacks: migraine is strongly tied to the gut through nausea, abdominal migraine and cyclic vomiting, and the microbiome and gut-brain signalling influence its frequency.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — Neck and jaw feed the headache: migraine is highly comorbid with neck pain and temporomandibular disorder, with cervical muscle and joint dysfunction both triggering and amplifying attacks.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — The skin turns painful to touch: cutaneous allodynia — scalp and skin hypersensitivity so that brushing hair or wearing glasses hurts — is a hallmark of central sensitisation during migraine attacks.
- `connects-to` → **[Renal System](../renal-system/README.md)** — Its painkillers can harm the kidney: frequent NSAID use for migraine risks analgesic nephropathy and acute kidney injury, and renal impairment limits which abortive drugs are safe.
- `connects-to` → **[Immune System](../immune-system/README.md)** — It runs on neurogenic inflammation: the trigeminovascular system releases CGRP and inflammatory mediators that dilate vessels and sensitise nerves, a process now blocked by anti-CGRP therapies.
- `connects-to` → **[Beta-blockers](../../../03-medicine/01-modern/04-cardio/beta-blockers/README.md)** — First-line prevention borrows a heart drug: beta-blockers like propranolol are a mainstay of migraine prophylaxis, reducing attack frequency though their mechanism in migraine is incompletely understood.
- `connects-to` → **[Dietary Magnesium](../../../03-medicine/03-food/magnesium-dietary/README.md)** — A supplement with real evidence: magnesium is one of the better-supported nutritional prophylactics for migraine, and low magnesium status is linked to attack susceptibility.
- `connects-to` → **[Lymphatic System](../lymphatic-system/README.md)** — Waste clearance may matter: dysfunction of the brain's glymphatic drainage system is increasingly implicated in migraine, linking sleep, fluid balance and headache.
- `connects-to` → **[Aspirin](../../../03-medicine/01-modern/04-cardio/aspirin/README.md)** — A first-line acute treatment: high-dose aspirin and other NSAIDs abort migraine attacks, and aspirin combined with caffeine and paracetamol is a common over-the-counter option.
- `connects-to` → **[ARBs](../../../03-medicine/01-modern/04-cardio/arbs/README.md)** — Blood-pressure drugs prevent attacks: the ARB candesartan, like beta-blockers, reduces migraine frequency, a useful preventive especially when hypertension coexists.
- `connects-to` → **[Multiple Sclerosis](../multiple-sclerosis/README.md)** — Headache shadows demyelination: migraine is more common in multiple sclerosis than in the general population, the two sharing neuroinflammatory and vascular mechanisms.
- `connects-to` → **[Targeted Therapy](../../../03-medicine/01-modern/13-cancer/targeted-therapy/README.md)** — Anti-CGRP biology transformed it: monoclonal antibodies against CGRP or its receptor (erenumab, fremanezumab) and oral gepants prevent and abort migraine by blocking the neuropeptide central to the trigeminovascular attack.
- `connects-to` → **[Arterial Wall](../../05-tissue/arterial-wall/README.md)** — It is a neurovascular disorder: migraine engages the trigeminovascular system and meningeal arteries, and migraine with aura raises the risk of ischaemic stroke and arterial-wall disease, especially with oestrogen and smoking.
- `connects-to` → **[Myocardium](../../05-tissue/myocardium/README.md)** — Its acute drugs squeeze the coronaries: triptans and ergots cause vasoconstriction and are contraindicated in coronary disease, and migraine with aura independently raises the risk of myocardial infarction.
- `connects-to` → **[Orexin](../../03-molecular/orexin/README.md)** — The hypothalamic trigger: orexin signalling from the hypothalamus is implicated in migraine's premonitory phase—yawning, food craving and fatigue—and in the tight link between migraine and disrupted sleep.
- `connects-to` → **[Hippocampus](../../05-tissue/hippocampus/README.md)** — Why chronic migraine clouds memory: repeated attacks and the stress of recurrent pain remodel the hippocampus, tying migraine to memory complaints and its comorbidity with anxiety and depression.
- `connects-to` → **[Thyroid](../../06-organ/thyroid/README.md)** — A two-way thyroid link: hypothyroidism is commoner in people with migraine and migraine commoner in thyroid disease, likely through shared autonomic and inflammatory pathways.
- `connects-to` → **[Antiphospholipid Syndrome](../antiphospholipid-syndrome/README.md)** — Headache as an autoimmune clue: migraine—especially with aura—is common in antiphospholipid syndrome, where a hypercoagulable state and patent foramen ovale also raise the risk of aura-associated stroke.
- `connects-to` → **[Narcolepsy](../narcolepsy/README.md)** — Headache and the sleep switch: migraine is markedly more common in narcolepsy and other sleep disorders, sharing hypothalamic and orexinergic dysregulation that links sleep-wake control to headache.
- `connects-to` → **[COVID-19 Disease](../covid-19-disease/README.md)** — Headache of infection: headache is among the commonest COVID-19 symptoms, and the infection can trigger new daily persistent headache or worsen pre-existing migraine.
- `connects-to` → **[Opioid Use Disorder](../opioid-use-disorder/README.md)** — Medication-overuse headache: opioids worsen migraine and transform it into chronic daily headache while risking dependence, the main reason they are avoided in headache management.
- `connects-to` → **[Anorexia Nervosa](../anorexia-nervosa/README.md)** — A serotonergic, female-predominant overlap: migraine co-occurs with eating disorders such as anorexia nervosa, sharing serotonergic dysregulation, while meal-skipping and dehydration are potent migraine triggers.
- `connects-to` → **[Endocardium](../../05-tissue/endocardium/README.md)** — Patent foramen ovale: migraine with aura is associated with a patent foramen ovale in the atrial septum, whose right-to-left shunt lets vasoactive substances and paradoxical emboli bypass the lungs.
- `connects-to` → **[IL-6](../../03-molecular/il-6/README.md)** — Neurogenic inflammation: IL-6 released during the sterile neurogenic inflammation around meningeal vessels contributes to the sensitisation and pain of a migraine attack.
- `connects-to` → **[TNF-α](../../03-molecular/tnf-alpha/README.md)** — Inflammatory sensitisation: TNF-α is elevated during migraine and helps sensitise trigeminal nociceptors, part of the inflammatory cascade that sustains the headache.
- `connects-to` → **[Norepinephrine](../../03-molecular/norepinephrine/README.md)** — Brainstem modulation: noradrenergic signalling from the locus coeruleus modulates cerebral blood flow and pain processing in migraine, and its dysregulation features in the autonomic symptoms of attacks.
- `connects-to` → **[Prostaglandins](../../03-molecular/prostaglandins/README.md)** — Neurogenic inflammation: prostaglandins sensitise and excite trigeminal nociceptors and dilate meningeal vessels during migraine, which is why NSAIDs that block their synthesis abort attacks.
- `connects-to` → **[Endothelin-1](../../03-molecular/endothelin-1/README.md)** — Vascular dysregulation: endothelin-1 contributes to the meningeal and cerebral vascular tone changes of migraine, part of the neurovascular dysfunction underlying the headache and aura.
- `connects-to` → **[Serotonin Transporter](../../03-molecular/serotonin-transporter/README.md)** — Serotonergic comorbidity: serotonin-transporter function links migraine to its frequent depression and anxiety comorbidity and shapes the serotonergic descending pain modulation triptans engage.
- `connects-to` → **[Progesterone](../../03-molecular/progesterone/README.md)** — The estrogen-progesterone fluctuations of the menstrual cycle drive menstrual migraine, with the perimenstrual estrogen withdrawal and shifting progesterone precipitating the attacks that cluster around menses in many women.
- `connects-to` → **[Bradykinin](../../03-molecular/bradykinin/README.md)** — Bradykinin generated in the meninges sensitizes and excites trigeminal nociceptors, part of the neurogenic inflammation that produces the throbbing pain of migraine alongside CGRP and substance P.
- `connects-to` → **[ATP](../../03-molecular/atp/README.md)** — The mitochondrial-energy-deficit hypothesis links migraine susceptibility to impaired neuronal ATP production, the rationale behind riboflavin and coenzyme Q10—mitochondrial cofactors—as evidence-based migraine preventives.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Mutations in the P/Q-type calcium channel gene CACNA1A cause familial hemiplegic migraine type 1, directly linking dysregulated neuronal calcium currents and glutamate release to the cortical spreading depression of migraine aura.
- `connects-to` → **[KIT](../../03-molecular/kit/README.md)** — KIT-dependent mast cells in the dura degranulate to release histamine, tryptase and cytokines that sensitize trigeminal nociceptors, an arm of the neurogenic meningeal inflammation that generates migraine pain.
- `connects-to` → **[Oxytocin](../../03-molecular/oxytocin/README.md)** — Oxytocin acting on trigeminal-ganglion receptors inhibits nociceptive signaling and CGRP release, the basis for intranasal oxytocin being explored as a migraine treatment and a possible mediator of hormonal migraine patterns.
- `connects-to` → **[Connexin-43](../../03-molecular/connexin43/README.md)** — Astrocytic connexin-43 gap junctions propagate the slow wave of depolarization—cortical spreading depression—that underlies the migraine aura.
- `connects-to` → **[NLRP3 Inflammasome](../../03-molecular/nlrp3-inflammasome/README.md)** — Cortical spreading depression activates the NLRP3 inflammasome and IL-1β in microglia (already mapped), driving the sterile neuroinflammation that sensitizes the trigeminovascular pain pathway in migraine.
- `connects-to` → **[CRH](../../03-molecular/crh/README.md)** — Stress is a major migraine trigger, and CRH-driven HPA-axis activation lowers the threshold for attacks, linking the stress system to migraine susceptibility.
- `connects-to` → **[TLR4](../../03-molecular/tlr4/README.md)** — TLR4-driven neuroinflammation in the trigeminovascular system sensitizes meningeal nociceptors, contributing to the neurogenic inflammation that sustains the migraine attack.
- `connects-to` → **[NTRK](../../03-molecular/ntrk/README.md)** — BDNF signaling through its TrkB receptor (NTRK) mediates the central sensitization of trigeminal pain pathways that underlies the allodynia and chronification of migraine.
- `connects-to` → **[NRF2](../../03-molecular/nfe2l2/README.md)** — NRF2-regulated antioxidant defenses counter the oxidative stress implicated in migraine pathophysiology and in the metabolic vulnerability to cortical spreading depression.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — ERK-MAPK activation in trigeminal neurons mediates the central sensitization and CGRP-related signaling (CGRP mapped) that sustain migraine pain.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — PI3K-AKT signaling participates in trigeminovascular neuronal excitability and the neurogenic inflammation underlying migraine attacks.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Microglial galectin-3 reflects the neuroinflammatory activation increasingly implicated in migraine chronification.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — IL-6-STAT3 signaling transduces the neuroinflammatory tone implicated in trigeminovascular sensitization and migraine chronification.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β signaling modulates neuronal excitability relevant to the cortical spreading depression that underlies migraine aura.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — Cytosolic DNA released by neuronal and glial stress can engage cGAS-STING, contributing to the neuroinflammation associated with chronic migraine.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — FOXO downstream of PI3K-AKT signaling (AKT already mapped) regulates neuronal oxidative-stress handling relevant to the cortical excitability of migraine.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — IFN-STAT1 neuroinflammatory signaling contributes to the trigeminovascular inflammation implicated in migraine.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — JAK1/2 signaling upstream of STAT3 (IL-6 already mapped) relays the neuroinflammatory tone associated with chronic migraine.
- `connects-to` → **[HIF-1alpha](../../03-molecular/hif-1alpha/README.md)** — HIF-1α responses to the metabolic and hypoxic stress of cortical spreading depression contribute to migraine pathophysiology.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — S100A8/A9 alarmins reflect the neurogenic and meningeal inflammatory activation implicated in migraine.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — PI3K (PIK3CA)-AKT signaling (AKT already mapped) participates in the neuronal excitability and trigeminal sensitization of migraine.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK-linked neuronal energy sensing participates in the metabolic-stress and cortical-excitability mechanisms of migraine.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — Autophagy modulates the neuronal and glial homeostasis relevant to the cortical spreading depression of migraine.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — DNMT3A-mediated DNA methylation contributes to the epigenetic regulation implicated in migraine susceptibility.
- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — SRC-family kinase signaling participates in the neuronal-glial signaling and trigeminovascular sensitization of migraine.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-driven neuroimmune signaling participates in the neuroinflammation of migraine.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — CXCL12-CXCR4 signaling participates in the neuroimmune and trigeminovascular processes of migraine.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — IL-1β-driven neuroinflammation participates in the trigeminovascular sensitization of migraine.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — IL-33 alarmin signaling participates in the neuroinflammatory and mast-cell responses of migraine.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — IL-17A signaling participates in the neuroinflammation associated with migraine.
- `connects-to` → **[Beta-1 adrenergic receptor](../../03-molecular/beta1-adrenergic-receptor/README.md)** — Beta-blocker prophylaxis: propranolol and metoprolol are first-line migraine preventives acting through beta-adrenergic blockade (norepinephrine already mapped), among the oldest effective prophylactic classes despite an incompletely understood mechanism.
- `connects-to` → **[Angiotensin II](../../03-molecular/angiotensin-ii/README.md)** — RAAS prophylaxis: the angiotensin-receptor blocker candesartan and ACE inhibitors reduce migraine frequency, implicating the renin-angiotensin system in migraine and providing a preventive option for patients with comorbid hypertension.
- `connects-to` → **[Testosterone](../../03-molecular/testosterone/README.md)** — Sex differences: migraine is far more common in women, and testosterone appears protective by dampening trigeminal nociception and cortical excitability (estrogen and progesterone already mapped), part of the hormonal basis of the sex disparity.
- `connects-to` → **[Mu-opioid receptor](../../03-molecular/mu-opioid-receptor/README.md)** — Medication-overuse headache: opioids acting on the mu-opioid receptor relieve acute headache but, overused, cause medication-overuse headache and dependence, a major reason opioids are discouraged in migraine management.
- `connects-to` → **[Aldosterone](../../03-molecular/aldosterone/README.md)** — Mineralocorticoid arm of the RAAS: alongside the angiotensin II already mapped, aldosterone and mineralocorticoid signalling are implicated in migraine, consistent with the preventive benefit of the renin-angiotensin blockade used in prophylaxis.
- `connects-to` → **[Insulin](../../03-molecular/insulin/README.md)** — Metabolic association: migraine is associated with insulin resistance and the metabolic syndrome, and impaired brain energy metabolism is one proposed contributor to the neuronal hyperexcitability underlying attacks.
- `connects-to` → **[Xanthine oxidase](../../03-molecular/xanthine-oxidase/README.md)** — Oxidative and energy stress: mitochondrial dysfunction and oxidative stress, to which xanthine oxidase contributes, are implicated in the neuronal energy deficit and hyperexcitability of migraine (NRF2 already mapped), and antioxidant supplements are used in prophylaxis.
- `connects-to` → **[Cholesterol](../../03-molecular/cholesterol/README.md)** — Vascular risk: migraine, especially with aura, is associated with dyslipidaemia and a raised risk of stroke and cardiovascular events (insulin already mapped), part of its vascular comorbidity.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Obesity link: obesity raises migraine frequency, and the adipokine leptin, with the low-grade inflammation (IL-6 and TNF already mapped) of excess adiposity, is one proposed mediator of the obesity-migraine association.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — Neuroimmune balance: the anti-inflammatory IL-4 counters the pro-inflammatory cytokines (IL-6, TNF and IL-1 already mapped) of the neurogenic inflammation implicated in migraine, part of its immune dimension.
- `connects-to` → **[Zinc](../../02-atomic/zinc/README.md)** — Zinc and neuronal excitability: zinc modulates the glutamatergic (already mapped) signalling and, with magnesium (already mapped), the neuronal excitability implicated in the cortical spreading depression of migraine.
- `connects-to` → **[Omega-3 fatty acids](../../../03-medicine/03-food/omega-3-fatty-acids/README.md)** — Omega-3 prophylaxis: the omega-3 fatty acids give rise to pro-resolving mediators that counter the neurogenic inflammation (prostaglandins already mapped) of migraine, and dietary omega-3 has been studied for migraine prevention.
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — Type-2 neuroimmunity: IL-13, with IL-4 (already mapped), supports the M2 microglial arm balancing the neurogenic inflammation (substance-P and CGRP already mapped) implicated in migraine.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — Adipokine and chronic migraine: adiponectin, with leptin (already mapped), is part of the adipokine dimension of the obesity that is a risk factor for the transformation to chronic migraine.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), links the adipose-inflammatory milieu (IL-6 already mapped) to the chronic migraine associated with obesity.
- `connects-to` → **[Astrocyte](../../04-cellular/astrocyte/README.md)** — Cortical spreading depression: the astrocytes propagate the cortical spreading depression (the aura; glutamate and connexin43 already mapped, the K+ waves) of migraine.
- `connects-to` → **[Major depressive disorder](../major-depressive-disorder/README.md)** — Depression comorbidity: migraine and major depression are bidirectionally comorbid, sharing the serotonergic (already mapped) dysregulation.
- `connects-to` → **[Epilepsy](../epilepsy/README.md)** — Epilepsy comorbidity: migraine and epilepsy are comorbid, sharing the cortical hyperexcitability, the SCN1A (already mapped) channelopathies and the cortical spreading depression.
- `connects-to` → **[Type I interferon](../../03-molecular/type-i-interferon/README.md)** — Innate neuroinflammation: the type-I interferon, downstream of the cGAS-STING (already mapped) pathway, is part of the sterile neuroinflammation (IL-1 and TNF already mapped) of the trigeminovascular activation of migraine.
- `connects-to` → **[IFN-gamma](../../03-molecular/ifn-gamma/README.md)** — Th1 neuroinflammation: the IFN-γ of the T cells is the type-II interferon arm of the immune-inflammatory dimension associated with migraine.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the immune-inflammatory dimension of migraine.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the neuroimmune interaction in migraine.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the neuroinflammatory dimension of migraine.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — Type-2/mast-cell arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), arms the dural mast cells (already mapped) whose degranulation contributes to the neurogenic inflammation of migraine.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Meningeal complement: the complement C3 activation contributes to the dural neurogenic inflammation and the immune component of migraine.
- `connects-to` → **[C5aR1](../../03-molecular/c5ar1/README.md)** — C5a receptor: the C5aR1 signalling (with the complement C3 already mapped) links the complement to the mast-cell (already mapped) and myeloid activation of the neurogenic inflammation of migraine.
- `connects-to` → **[Cytotoxic T cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Psychoneuroimmune arm: the peripheral cytotoxic T cells (perforin pathway) reflect the adaptive-immune dimension of the neuroinflammatory interaction in migraine.
- `connects-to` → **[Complement C5](../../03-molecular/complement-c5/README.md)** — Terminal complement: the complement C5 and its C5a (with C3 and C5aR1 already mapped) are part of the complement activation of the neurogenic inflammation of migraine.
- `connects-to` → **[Factor H](../../03-molecular/factor-h/README.md)** — Complement regulation: factor H regulates the alternative complement pathway (complement C3, C5 and C5aR1 already mapped) of the neuroinflammatory dimension of migraine.
- `connects-to` → **[Dendritic cell](../../04-cellular/dendritic-cell/README.md)** — Meningeal antigen presentation: the dendritic cells of the meningeal and CNS-border compartments are part of the neuroimmune interface implicated in the neurogenic inflammation of migraine.
- `connects-to` → **[TSLP](../../03-molecular/tslp/README.md)** — Alarmin-meningeal axis: TSLP, from meningeal mast cells (already mapped) and the trigeminal epithelium, primes dendritic cells (already mapped) and amplifies the neurogenic and meningeal inflammation underlying the migraine attack.
- `connects-to` → **[C1-Esterase Inhibitor](../../03-molecular/c1-esterase-inhibitor/README.md)** — Complement brake: C1-esterase inhibitor regulates the classical-complement and contact-pathway activation (complement C3, C5 and bradykinin already mapped) contributing to the neurogenic oedema and vasodilation of the migraine attack.
- `connects-to` → **[Erythropoietin](../../03-molecular/erythropoietin/README.md)** — Neuroprotective EPO: erythropoietin, via EpoR on neurons (already mapped) and microglia (already mapped), exerts anti-inflammatory and neuroprotective effects relevant to the central sensitisation and the chronic neuroinflammation of migraine.
- `connects-to` → **[Periostin](../../03-molecular/periostin/README.md)** — Meningeal ECM: periostin, from meningeal fibroblasts and trigeminal-ganglion stroma, contributes to the extracellular-matrix remodelling at the meningeal neuroimmune interface of the neurogenic inflammation and sensitisation of migraine.
- `connects-to` → **[Prolactin](../../03-molecular/prolactin/README.md)** — Hormonal migraine trigger: prolactin modulates nociception via PRLR on trigeminal neurons (already mapped) and correlates with menstrual migraine, complementing the oestrogen/progesterone (already mapped) hormonal dimension of migraine susceptibility.
- `connects-to` → **[Transferrin](../../03-molecular/transferrin/README.md)** — Iron-migraine metabolism: transferrin, the iron carrier, reflects the iron deficiency that is a recognised migraine risk; dysregulated brain iron handling is linked to cortical spreading depression and the structural brain changes of chronic migraine.
- `connects-to` → **[Vasopressin](../../03-molecular/vasopressin/README.md)** — Cerebral vasomotor tone: vasopressin, via V1aR on neurons (already mapped) and endothelial cells (already mapped), modulates cerebral vasomotor tone; vasopressin dysregulation amplifies the CGRP (already mapped) and nitric-oxide (already mapped) vasoactive cascade of migraine.
- `connects-to` → **[Selenium](../../02-atomic/selenium/README.md)** — Neuroprotective antioxidant: selenium, as neuroprotective GPx in neurons (already mapped) and astrocytes (already mapped), scavenges neuroinflammatory ROS; selenium deficiency impairs GABA (already mapped) inhibitory tone and amplifies the cortical spreading depression of migraine.
- `connects-to` → **[Iodine](../../02-atomic/iodine/README.md)** — Thyroid-neurovascular axis: iodine-dependent thyroid hormones modulate the serotonergic (serotonin already mapped) and dopaminergic (dopamine already mapped) pathways; iodine deficiency impairs the nitric-oxide (already mapped) and CGRP (already mapped) neurovascular axis of migraine.
- `connects-to` → **[Copper](../../02-atomic/copper/README.md)** — Migraine copper: copper, via dopamine-β-hydroxylase, supports dopamine (already mapped) and norepinephrine (already mapped) neurotransmission; copper deficiency impairs NF-κB (already mapped) antioxidant signalling and CGRP (already mapped) neurovascular axis of migraine.
- `connects-to` → **[Phosphorus](../../02-atomic/phosphorus/README.md)** — Migraine phosphorus: phosphorus drives ATP (already mapped)-dependent synaptic (synapse already mapped) transmission in neurons (already mapped); phosphate dysregulation amplifies NLRP3 (already mapped) microglial (microglia already mapped) neuroinflammation and migraine attacks.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Migraine iron: iron is required for dopamine (already mapped) and serotonin (already mapped) synthesis; iron deficiency amplifies NF-κB (already mapped) and CGRP (already mapped) neuroinflammatory cascade and worsens cortical spreading depression and migraine attack burden.
- `connects-to` → **[Nitrogen](../../02-atomic/nitrogen/README.md)** — Migraine nitrogen: nitric oxide (NO, nitrogen-derived) is a potent vasodilator and CGRP (already mapped) releaser in trigeminal neurons (already mapped); nitric-oxide excess amplifies NF-κB (already mapped) neuroinflammation and cortical-spreading-depression in migraine.
- `connects-to` → **[Chloride](../../02-atomic/chloride/README.md)** — Migraine chloride: chloride via GABA(A) receptors (GABA already mapped) on neurons (already mapped) sets cortical inhibitory tone; chloride dysregulation amplifies glutamate (already mapped) and NF-κB (already mapped) and CGRP (already mapped) neuroinflammation in migraine.
- `connects-to` → **[Sulfur](../../02-atomic/sulfur/README.md)** — Migraine sulfur: H2S from sulfur-amino acids in trigeminal neurons (already mapped) and astrocytes (already mapped) modulates CGRP (already mapped) release; sulfur deficiency amplifies NF-κB (already mapped) and NLRP3 (already mapped) neuroinflammation in migraine.
- `connects-to` → **[Oxygen](../../02-atomic/oxygen/README.md)** — Migraine oxygen: mitochondrial oxygen sustains ATP in neurons (already mapped) and astrocytes (already mapped) for trigeminal signalling; hypoxia amplifies NLRP3 (already mapped) and NF-κB (already mapped) and CGRP (already mapped) neuroinflammatory cascade of migraine.

[^gbd-2016-migraine-burden]: GBD 2016 Headache Collaborators. Global, regional, and national burden of migraine and tension-type headache, 1990-2016. *Lancet Neurol.* 2018;17(11):954-976. [doi:10.1016/S1474-4422(18)30322-3](https://doi.org/10.1016/S1474-4422(18)30322-3) · [PubMed 30353868](https://pubmed.ncbi.nlm.nih.gov/30353868/)
[^goadsby-2002-migraine-review]: Goadsby PJ, Lipton RB, Ferrari MD. Migraine — current understanding and treatment. *N Engl J Med.* 2002;346(4):257-270. [doi:10.1056/NEJMra010917](https://doi.org/10.1056/NEJMra010917) · [PubMed 11807151](https://pubmed.ncbi.nlm.nih.gov/11807151/)
[^dodick-2018-erenumab-arise]: Dodick DW, Ashina M, Brandes JL, et al. ARISE: A Phase 3 randomized trial of erenumab for episodic migraine. *Cephalalgia.* 2018;38(6):1026-1037. [doi:10.1177/0333102418759786](https://doi.org/10.1177/0333102418759786) · [PubMed 29471679](https://pubmed.ncbi.nlm.nih.gov/29471679/)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
