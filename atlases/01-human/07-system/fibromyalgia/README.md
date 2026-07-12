---
schema: human-scale-entry/v1
id: fibromyalgia
name: Fibromyalgia
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-08
summary: "Fibromyalgia (2-3% prevalence, F:M 3:1) is a central sensitization disorder: SP-NMDA wind-up, descending serotonin/NE inhibition failure, reduced NAcc dopamine. Duloxetine, milnacipran (SNRIs), and pregabalin are FDA-approved; exercise and CBT are first-line."
aliases: ["fibromyalgia", "FM", "fibromyalgia syndrome", "FMS", "central sensitization", "chronic widespread pain", "fibro fog", "wind-up pain"]
cross_links:
  - target: 01-human/03-molecular/glutamate
    relation: connects-to
    note: "Spinal NMDA receptor hyperactivation by repetitive C-fiber input + SP → wind-up and central sensitization; elevated glutamate in posterior insula on MRS correlates with FM severity; ketamine (NMDA antagonist) reduces FM pain in small controlled trials."
  - target: 01-human/03-molecular/serotonin
    relation: connects-to
    note: "Descending serotonergic inhibition from raphe to dorsal horn is impaired in FM (low CSF 5-HIAA); duloxetine and amitriptyline restore descending inhibition; 5-HT3 antagonist tropisetron reduces FM pain in small RCTs; 5-HT2A polymorphisms associate with FM risk."
  - target: 01-human/03-molecular/norepinephrine
    relation: connects-to
    note: "Descending NE inhibition from LC to dorsal horn is deficient in FM; duloxetine and milnacipran (FDA-approved SNRIs) increase NE in descending pain pathways — the core analgesic mechanism; NE deficiency amplifies SP and glutamate-driven central sensitization."
  - target: 01-human/03-molecular/dopamine
    relation: connects-to
    note: "FM shows reduced NAcc dopamine release (↓ [¹¹C]raclopride binding PET — Harris 2007); blunted NAcc DA → reduced endogenous analgesia (dopamine activates descending antinociception); low-dose naltrexone may act partly via dopaminergic disinhibition of opioid circuits."
  - target: 01-human/03-molecular/substance-p
    relation: connects-to
    note: "CSF substance P is elevated ~3-fold in FM — one of the most reproducible biomarkers; elevated SP → NK1R sensitization → dorsal horn wind-up → diffuse hyperalgesia and allodynia; FM patients have consistently lower pain thresholds consistent with SP-driven central sensitization."
  - target: 01-human/06-organ/brain
    relation: targets
    note: "FM involves thalamic hypersensitivity, ACC and insula hyperactivation to pain stimuli (fMRI), and altered DMN connectivity; MRS shows elevated glutamate in posterior insula; gray matter density reductions correlate with pain chronicity; changes partially reverse with treatment."
  - target: 01-human/03-molecular/cgrp
    relation: connects-to
    note: "CGRP is elevated in plasma and CSF in fibromyalgia; CGRP-mediated peripheral C-fiber sensitization contributes to FM's diffuse hyperalgesia and allodynia; anti-CGRP mAbs are under investigation for FM; CGRP and substance P are co-released from FM peripheral nociceptors."
  - target: 01-human/07-system/neuropathic-pain
    relation: connects-to
    note: "FM and neuropathic pain share central sensitization (NMDA wind-up, descending inhibition failure) but differ: neuropathic pain requires nerve injury while FM is nociplastic; both respond to SNRIs and α2δ ligands; small fiber neuropathy co-occurs in ~40% of FM patients."
  - target: 01-human/07-system/migraine
    relation: connects-to
    note: "Fibromyalgia and migraine frequently co-occur and share central sensitization and CGRP biology: both feature amplified pain processing and descending-inhibition failure, anti-CGRP antibodies developed for migraine are under study in FM, and SNRIs and exercise help both."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "Depression coexists with fibromyalgia in ~40-60%: they share serotonin-norepinephrine dysregulation and HPA-axis changes, the SNRIs duloxetine and milnacipran treat both, and depression worsens FM pain and disability—though FM pain is not merely somatized depression."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "Anxiety disorders are highly comorbid with fibromyalgia: shared monoaminergic dysregulation and stress-axis dysfunction link them, anxiety amplifies pain perception and sleep disruption in a vicious cycle, and combined CBT plus SNRI treatment targets both pain and affective load."
  - target: 01-human/07-system/ptsd
    relation: connects-to
    note: "Fibromyalgia and PTSD overlap through central sensitization and stress: trauma and HPA-axis dysregulation prime the nervous system to amplify pain, PTSD is a common antecedent and comorbidity of fibromyalgia, and both respond to approaches targeting the stress-pain loop."
  - target: 01-human/07-system/rheumatoid-arthritis
    relation: connects-to
    note: "Fibromyalgia frequently coexists with rheumatoid arthritis as secondary fibromyalgia: central pain sensitization adds widespread non-inflammatory pain atop joint disease, so inflated disease-activity scores mislead—distinguishing them avoids overtreating RA."
  - target: 01-human/07-system/sjogrens-syndrome
    relation: connects-to
    note: "Fibromyalgia is common in Sjögren's and other autoimmune diseases: chronic illness and dysautonomia drive central sensitization, so widespread pain and fatigue in Sjögren's often reflect comorbid fibromyalgia rather than active glandular inflammation."
  - target: 01-human/07-system/gut-microbiome
    relation: connects-to
    note: "Fibromyalgia is increasingly tied to the gut-brain axis: patients show an altered gut microbiome, and microbial metabolites may influence pain signaling and central sensitization—part of why it overlaps with IBS and why diet and microbiome are studied as modifiers."
  - target: 01-human/07-system/systemic-lupus-erythematosus
    relation: connects-to
    note: "Fibromyalgia is a major confounder in lupus: up to a third of SLE patients develop comorbid fibromyalgia, inflating disease-activity scores—so separating central-sensitization pain from true lupus inflammation guides whether to escalate immunotherapy or treat pain."
  - target: 01-human/05-tissue/hippocampus
    relation: connects-to
    note: "Fibromyalgia involves the hippocampus and central pain processing: imaging shows hippocampal changes alongside augmented pain perception (central sensitization) and 'fibro-fog'—evidence that fibromyalgia is a disorder of brain pain processing, not peripheral tissue."
  - target: 01-human/07-system/insomnia-disorder
    relation: connects-to
    note: "Nonrestorative sleep is core to fibromyalgia, not incidental: disrupted deep sleep lowers pain thresholds and worsens fatigue and cognition, and the disorder and insomnia reinforce each other—so sleep-targeted treatment is central to managing fibromyalgia."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "Fibromyalgia is a disorder of pain-processing neurons (central sensitization): amplified spinal and brain pain signaling makes normal stimuli hurt, so it is a problem of how the nervous system processes pain, not tissue damage—explaining why analgesics often fail."
  - target: 01-human/03-molecular/cortisol
    relation: connects-to
    note: "HPA-axis and cortisol dysregulation feature in fibromyalgia: blunted stress-hormone responses accompany the disorder, linking chronic stress and poor sleep to amplified pain—so fibromyalgia sits at the interface of the stress system and pain processing."
  - target: 01-human/04-cellular/microglia
    relation: connects-to
    note: "Fibromyalgia may be sustained by activated microglia: these immune cells of the cord and brain release pain-amplifying cytokines, supporting the idea that central sensitization—a volume knob turned up on pain—has a neuroinflammatory basis."
  - target: 01-human/03-molecular/gaba
    relation: connects-to
    note: "Fibromyalgia shows weakened pain braking: reduced GABA, the main inhibitory transmitter, leaves descending pain control too weak to dampen signals—part of why gabapentinoids like pregabalin, which boost inhibitory tone, are among its few effective drugs."
  - target: 01-human/05-tissue/peripheral-nerve
    relation: connects-to
    note: "Fibromyalgia is not purely central: about half of patients have small-fiber neuropathy, with reduced nerve-fiber density in skin biopsies—so damaged peripheral nerves may feed the amplified pain, blurring the line between central and peripheral pain disorders."
  - target: 01-human/06-organ/thyroid
    relation: connects-to
    note: "Hypothyroidism mimics and worsens fibromyalgia: low thyroid hormone causes the same fatigue, aches and cognitive fog, so checking the thyroid is essential before settling on a fibromyalgia diagnosis—and treating it can relieve overlapping symptoms."
  - target: 03-medicine/03-food/vitamin-d
    relation: connects-to
    note: "Vitamin D deficiency is common in fibromyalgia and may amplify pain: low levels are linked to more widespread musculoskeletal pain, and repletion is a simple, often-checked step that can modestly ease symptoms in deficient patients."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Fibromyalgia's lead drugs act on calcium channels: pregabalin and gabapentin bind the alpha-2-delta subunit of voltage-gated calcium channels in overactive pain neurons, dampening neurotransmitter release—calming the central sensitization that drives the pain."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "Fibromyalgia is linked to low magnesium: the mineral gates the NMDA receptor and fuels muscle energy, so deficiency may heighten the central pain sensitization and fatigue, and supplementation is studied as an adjunct."
  - target: 01-human/04-cellular/astrocyte
    relation: connects-to
    note: "Fibromyalgia's central sensitization runs through astrocytes: together with microglia, these glial cells amplify pain signaling in the spinal cord and brain, turning up the volume on normal sensations into the widespread pain that defines it."
  - target: 01-human/03-molecular/growth-hormone
    relation: connects-to
    note: "Fibromyalgia disrupts growth hormone via broken sleep: the lack of deep slow-wave sleep blunts nighttime GH secretion and lowers IGF-1, contributing to the poor tissue repair, fatigue, and muscle pain of the syndrome."
  - target: 01-human/05-tissue/synapse
    relation: connects-to
    note: "Fibromyalgia is a disease of amplified pain synapses: central sensitization strengthens transmission in the spinal cord and brain so ordinary signals are felt as pain, shifting the disorder from the muscles to the synapses that process pain."
  - target: 01-human/06-organ/large-intestine
    relation: connects-to
    note: "Fibromyalgia travels with the gut: irritable bowel syndrome overlaps heavily, and a disturbed microbiome and gut-brain signaling may feed the pain and fatigue, linking the large intestine to this whole-body pain disorder."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "Mast cells are an emerging suspect in fibromyalgia: increased in the skin of patients, they release mediators that sensitize nerve endings, offering one explanation for the widespread tenderness and the overlap with sensitivity syndromes."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Brain imaging shows fibromyalgia is real: fMRI photons reveal amplified activity in pain-processing networks to stimuli that wouldn't hurt others, objective evidence of the central sensitization behind the disorder."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "A skin biopsy can reveal fibromyalgia's nerves: many patients show small-fiber neuropathy, a reduced density of fine nerve endings in the skin that helps explain the burning, tingling quality of the pain."
  - target: 01-human/03-molecular/bdnf
    relation: connects-to
    note: "BDNF helps wire fibromyalgia's amplified pain: this growth factor, raised in patients, promotes the synaptic plasticity that strengthens pain transmission, a molecular contributor to central sensitization."
  - target: 01-human/03-molecular/mu-opioid-receptor
    relation: connects-to
    note: "Fibromyalgia's own painkillers are turned down: imaging shows reduced mu-opioid receptor availability and a blunted endogenous opioid system, which helps explain why opioid drugs work poorly and can even worsen the pain."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "Fibromyalgia comes with a jittery autonomic system: many patients have dysautonomia with palpitations, a racing resting heart, and orthostatic intolerance overlapping POTS, reflecting the same nervous-system dysregulation that amplifies pain."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "Overactive sodium channels keep the pain nerves firing: gain in voltage-gated sodium currents makes the sensory neurons of fibromyalgia hyperexcitable, part of the peripheral drive feeding the central sensitization."
  - target: 01-human/03-molecular/melatonin
    relation: connects-to
    note: "Fibromyalgia's unrefreshing sleep has a chemical signature: disrupted circadian rhythm and altered melatonin leave patients waking tired, and the resulting sleep deprivation itself lowers the pain threshold, locking in a vicious cycle."
  - target: 01-human/06-organ/stomach
    relation: connects-to
    note: "The gut keeps fibromyalgia company: irritable bowel and functional dyspepsia overlap heavily with it through a shared gut-brain hypersensitivity, so bloating, pain, and altered bowel habit travel with the widespread body pain."
  - target: 01-human/03-molecular/adenosine
    relation: connects-to
    note: "Adenosine sits at the crossroads of its fatigue and pain: the molecule builds sleep pressure and dampens pain signaling, and disturbed adenosine handling may help explain the exhaustion and the poor pain control in fibromyalgia."
  - target: 01-human/03-molecular/endocannabinoid
    relation: connects-to
    note: "A 'clinical endocannabinoid deficiency' is one leading idea: low endocannabinoid tone may underlie fibromyalgia, migraine, and IBS together, the rationale behind trying cannabinoids to lift pain thresholds and ease the sleep disturbance."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "Fibromyalgia is overwhelmingly a women's diagnosis: symptoms often worsen premenstrually and around menopause as sex hormones shift, and it overlaps with painful menstrual and pelvic conditions, hinting hormones modulate central pain."
  - target: 01-human/06-organ/small-intestine
    relation: connects-to
    note: "The small bowel may feed the pain: small intestinal bacterial overgrowth (SIBO) is found more often in fibromyalgia, and the bloating and altered gut signaling it brings feed back through the gut-brain axis onto central sensitization."
  - target: 01-human/03-molecular/estrogen
    relation: connects-to
    note: "A hormonal tilt may explain the female predominance: fibromyalgia overwhelmingly affects women and often flares perimenstrually and around menopause, hinting that falling estrogen — which modulates pain and serotonin pathways — lowers the pain threshold."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "A faint immune signal underlies the pain: fibromyalgia shows low-grade neuroinflammation with raised cytokines from activated T cells and glia, evidence the disorder is more than purely psychological even without overt tissue damage."
  - target: 01-human/07-system/obesity
    relation: connects-to
    note: "Weight and pain worsen each other: obesity is common in fibromyalgia and amplifies pain and fatigue through inflammation, poor sleep and deconditioning, so weight management and exercise are core to treatment."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "It is increasingly seen as a nervous-system disorder: fibromyalgia is a disease of how the brain and cord process pain, amplifying ordinary signals through central sensitization rather than arising from damaged tissue at the painful sites."
  - target: 01-human/03-molecular/nlrp3-inflammasome
    relation: connects-to
    note: "Glial inflammation may stoke the pain: activation of the NLRP3 inflammasome in microglia and the periphery releases IL-1β and other mediators implicated in the neuroinflammation thought to underlie fibromyalgia's amplified pain."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "Its immune profile is subtly off: reduced natural killer cell number and function are reported in fibromyalgia, part of the immune dysregulation it shares with chronic fatigue syndrome that hints at a low-grade immune component."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "A low-grade cytokine hum accompanies the pain: IL-6 and other pro-inflammatory cytokines run modestly elevated in fibromyalgia, feeding the neuroinflammation and central sensitization thought to amplify pain signals."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "The pain is felt in muscle and joint though the tissue is intact: fibromyalgia presents as widespread musculoskeletal pain and tenderness without true inflammation or damage, the hallmark of a centrally driven pain disorder."
  - target: 01-human/07-system/panic-disorder
    relation: connects-to
    note: "Anxiety travels with the pain: panic disorder and other anxiety conditions are markedly over-represented in fibromyalgia, sharing the stress-axis and autonomic dysregulation that link the two."
  - target: 01-human/07-system/opioid-use-disorder
    relation: connects-to
    note: "Treating the pain courts dependence: opioids are largely ineffective for fibromyalgia's central pain yet are still prescribed, and the chronic exposure carries real risk of tolerance, hyperalgesia and opioid use disorder."
  - target: 01-human/07-system/attention-deficit-hyperactivity-disorder
    relation: connects-to
    note: "Shared dopamine wiring and the cognitive overlap link them: ADHD is over-represented in fibromyalgia, and the inattention of 'fibro-fog' blurs with ADHD's, both tied to dopaminergic dysregulation."
  - target: 01-human/07-system/borderline-personality-disorder
    relation: connects-to
    note: "Early trauma is a shared root: childhood adversity that predisposes to borderline personality disorder also sensitizes the central pain system, and the two co-occur, each amplifying the other's distress."
  - target: 01-human/07-system/bipolar-disorder
    relation: connects-to
    note: "Mood instability runs alongside the pain: fibromyalgia shows markedly elevated rates of bipolar disorder, and the two share disturbances in sleep, stress reactivity and monoamine signaling."
  - target: 01-human/07-system/psoriatic-arthritis
    relation: connects-to
    note: "Central pain confounds an inflammatory arthritis: fibromyalgia frequently coexists with psoriatic arthritis, where its widespread tenderness can mimic active joint disease and complicate measuring true inflammatory control."
  - target: 01-human/07-system/type-2-diabetes
    relation: connects-to
    note: "Metabolic disease and chronic pain overlap: fibromyalgia is more common in type 2 diabetes, sharing obesity, inflammation and the painful sensory changes that blur with diabetic neuropathy."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "It travels with a hypersensitive gut: irritable bowel syndrome and other functional GI disorders are strikingly common in fibromyalgia, both reflecting central sensitisation and visceral hyperalgesia."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "A bladder version of the same syndrome: interstitial cystitis/painful bladder syndrome overlaps heavily with fibromyalgia, part of a cluster of central sensitivity syndromes sharing amplified pain processing."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "Its stress axis runs awry: fibromyalgia is associated with dysregulation of the hypothalamic-pituitary-adrenal axis and growth-hormone secretion, and it often coexists with and is screened against thyroid disease."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "The skin reveals nerve loss: biopsy shows reduced intraepidermal nerve-fibre density in a large subset of fibromyalgia, evidence of a small-fibre neuropathy underlying some of its pain."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "Hints of immune involvement: neuroinflammation and, in some patients, an IgG autoantibody component shown by passive-transfer studies, alongside its frequent overlap with autoimmune rheumatic diseases."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "Its autonomic control falters: fibromyalgia often features dysautonomia with orthostatic intolerance, POTS-like tachycardia and palpitations, reflecting altered cardiovascular reflex regulation."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "It alters the pattern of breathing: a dysfunctional breathing pattern with air hunger and breathlessness despite normal lungs is common in fibromyalgia, part of its central-sensitivity symptom cluster."
  - target: 01-human/07-system/covid-19-disease
    relation: connects-to
    note: "It can follow a viral illness: a fibromyalgia-like syndrome of widespread pain and fatigue commonly emerges after COVID-19, overlapping with long COVID."
  - target: 03-medicine/03-food/magnesium-dietary
    relation: connects-to
    note: "Magnesium is studied for its symptoms: low magnesium can worsen muscle cramps and pain, and magnesium supplementation is investigated as an adjunct for fibromyalgia."
  - target: 03-medicine/01-modern/10-mental-health/fluoxetine
    relation: connects-to
    note: "Antidepressants modulate the pain: SSRIs like fluoxetine, and especially the SNRI duloxetine, raise serotonin and noradrenaline to dampen the central pain amplification of fibromyalgia."
  - target: 02-pathogen/01-viruses/epstein-barr-virus
    relation: connects-to
    note: "It can follow an infection: fibromyalgia often begins after a viral illness such as Epstein-Barr glandular fever, part of the post-infectious central-sensitisation picture also seen after COVID."
  - target: 03-medicine/02-traditional/ashwagandha
    relation: connects-to
    note: "Traditional remedies are sought for it: adaptogens like ashwagandha are used by some for the fatigue, pain and poor sleep of fibromyalgia, complementing exercise and the established drugs."
  - target: 01-human/07-system/cannabis-use-disorder
    relation: connects-to
    note: "Cannabinoids are widely tried for it: fibromyalgia is a leading reason for medical-cannabis use, and the clinical endocannabinoid deficiency hypothesis frames its pain and sleep disturbance — though efficacy is uncertain and dependence is a real risk."
  - target: 03-medicine/02-traditional/panax-ginseng
    relation: connects-to
    note: "A studied botanical adjunct: like ashwagandha, Panax ginseng has been trialled for the fatigue, pain and poor sleep of fibromyalgia, part of the complementary approaches patients often turn to when drugs disappoint."
  - target: 03-medicine/01-modern/13-cancer/cancer-chemotherapy
    relation: connects-to
    note: "Treatment-related central sensitisation: chemotherapy and aromatase-inhibitor therapy in cancer survivors commonly cause chronic widespread musculoskeletal pain and fatigue resembling fibromyalgia, reflecting shared central pain-sensitisation mechanisms."
  - target: 01-human/07-system/ankylosing-spondylitis
    relation: connects-to
    note: "A confounding overlay on inflammatory arthritis: comorbid fibromyalgia is common in ankylosing spondylitis and inflates its disease-activity scores with widespread pain, so separating central sensitisation from active inflammation guides treatment."
  - target: 01-human/07-system/narcolepsy
    relation: connects-to
    note: "Unrefreshing sleep links them: fibromyalgia and narcolepsy both fragment sleep and cause profound daytime fatigue, with alpha-wave intrusion into deep sleep a hallmark of the non-restorative sleep of fibromyalgia."
  - target: 01-human/07-system/epilepsy
    relation: connects-to
    note: "Shared central hyperexcitability: fibromyalgia and epilepsy both reflect neuronal hyperexcitability with disturbed glutamate/GABA balance, and the gabapentinoids pregabalin and gabapentin treat both."
  - target: 01-human/07-system/systemic-sclerosis
    relation: connects-to
    note: "A confounder in connective-tissue disease: fibromyalgia frequently coexists with systemic sclerosis, its central pain amplification inflating disease-activity scores and complicating assessment of true inflammatory burden."
  - target: 01-human/07-system/social-anxiety-disorder
    relation: connects-to
    note: "The anxiety overlap: fibromyalgia is highly comorbid with anxiety disorders including social anxiety, sharing serotonergic-noradrenergic dysregulation that SNRIs like duloxetine target in both."
  - target: 01-human/03-molecular/tnf-alpha
    relation: connects-to
    note: "A low-grade neuroimmune signal: though fibromyalgia lacks classic inflammation, modestly raised TNF-α and other cytokines in blood and CSF support a neuroimmune contribution to its central sensitisation."
  - target: 01-human/05-tissue/intestinal-epithelium
    relation: connects-to
    note: "The IBS overlap: fibromyalgia coexists strongly with irritable bowel syndrome, sharing central sensitisation and gut-brain dysregulation at the intestinal epithelium and barrier, so the two are best treated together."
  - target: 01-human/05-tissue/cardiac-conduction-system
    relation: connects-to
    note: "Dysautonomia: fibromyalgia frequently features autonomic dysfunction with orthostatic intolerance, POTS and reduced heart-rate variability, reflecting dysregulated autonomic control of the cardiac conduction system."
  - target: 01-human/07-system/obsessive-compulsive-disorder
    relation: connects-to
    note: "Anxiety-spectrum comorbidity: fibromyalgia is over-represented alongside obsessive-compulsive and other anxiety disorders, sharing the serotonergic and stress-axis dysregulation that links central pain to anxiety."
  - target: 01-human/03-molecular/npy
    relation: connects-to
    note: "Pain and autonomic dysregulation: altered neuropeptide Y signalling is implicated in the pain processing and autonomic dysfunction of fibromyalgia."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Adiposity and pain: leptin, elevated in obesity, correlates with fibromyalgia pain severity, linking adipose-driven inflammation to central sensitisation."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "Neuroinflammation: IL-1β and inflammasome activation contribute to the central neuroinflammation increasingly implicated in fibromyalgia."
  - target: 01-human/03-molecular/serotonin-transporter
    relation: connects-to
    note: "Descending pain control: serotonin-transporter polymorphisms and reduced serotonergic reuptake modulation underlie blunted descending inhibition in fibromyalgia, the rationale for SNRI and tricyclic therapy."
  - target: 01-human/03-molecular/oxytocin
    relation: connects-to
    note: "Endogenous analgesia: oxytocin dampens nociception and stress reactivity, and lower oxytocinergic tone is linked to greater pain and distress in fibromyalgia, an emerging therapeutic target."
  - target: 01-human/03-molecular/nitric-oxide
    relation: connects-to
    note: "Oxidative stress: dysregulated nitric oxide and peroxynitrite formation drive the mitochondrial oxidative stress and central sensitisation reported in fibromyalgia muscle and CNS."
  - target: 01-human/03-molecular/igf-1
    relation: connects-to
    note: "Growth-axis disruption: many fibromyalgia patients have low IGF-1, reflecting the blunted growth-hormone secretion of disrupted deep sleep, which may impair muscle microtrauma repair and contribute to chronic myalgia."
  - target: 01-human/03-molecular/tlr4
    relation: connects-to
    note: "Glial priming: TLR4 signalling on microglia and astrocytes promotes the central sensitisation of fibromyalgia, part of the neuroinflammatory amplification of pain processing in the spinal cord and brain."
  - target: 01-human/03-molecular/ntrk
    relation: connects-to
    note: "Nociceptor sensitisation: elevated nerve growth factor signalling through TrkA sensitises peripheral nociceptors and is linked to the small-fibre neuropathy found in a substantial subset of fibromyalgia patients."
  - target: 01-human/03-molecular/orexin
    relation: connects-to
    note: "Non-restorative sleep: orexin signalling that stabilises sleep-wake states and modulates descending pain control is dysregulated in fibromyalgia, contributing to the unrefreshing sleep and arousal disturbance that worsen the pain and fatigue."
  - target: 01-human/03-molecular/histamine
    relation: connects-to
    note: "Mast-cell involvement: increased dermal mast cells releasing histamine are found in fibromyalgia skin, a peripheral neuroinflammatory contributor to the sensory symptoms and one proposed link to its frequent overlap with mast-cell-activation conditions."
  - target: 01-human/03-molecular/acetylcholine
    relation: connects-to
    note: "Autonomic dysfunction: fibromyalgia features reduced vagal tone and a blunted cholinergic anti-inflammatory reflex, an autonomic imbalance that leaves inflammation unchecked and contributes to the dysautonomia accompanying the chronic pain."
  - target: 01-human/03-molecular/crh
    relation: connects-to
    note: "HPA stress axis: corticotropin-releasing hormone sits at the apex of the dysregulated HPA stress axis of fibromyalgia, and its altered signalling links chronic stress to the central pain amplification of the disorder."
  - target: 01-human/03-molecular/glucocorticoid-receptor
    relation: connects-to
    note: "Blunted cortisol feedback: a hypofunctional cortisol response and impaired glucocorticoid-receptor feedback characterise the HPA dysregulation of fibromyalgia, contributing to its fatigue, poor stress resilience and widespread pain."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "Neuroinflammation balance: the low-grade neuroinflammation of fibromyalgia (IL-1β, IL-6 and TNF-α already mapped) is normally restrained by regulatory IL-10, whose relative deficiency may sustain glial pain signalling."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "Central sensitization: BDNF-TrkB signalling (BDNF and NTRK mapped) through MAPK-ERK in dorsal-horn neurons drives the spinal central sensitization that amplifies pain in fibromyalgia."
  - target: 01-human/03-molecular/acth
    relation: connects-to
    note: "HPA dysfunction: blunted and dysregulated CRH-ACTH-cortisol stress-axis reactivity (CRH, cortisol and the glucocorticoid receptor mapped) is a characteristic neuroendocrine feature of fibromyalgia."
  - target: 01-human/03-molecular/myd88
    relation: connects-to
    note: "Glial activation: TLR4 (mapped) signalling through MyD88 activates microglia and the neuroinflammatory cytokine response that contributes to the central pain amplification of fibromyalgia."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "Neuroinflammatory transcription: NF-κB-driven neuroinflammation (downstream of the TLR4-MyD88 signalling already mapped) contributes to the glial activation and central sensitisation of fibromyalgia."
  - target: 01-human/03-molecular/nfe2l2
    relation: connects-to
    note: "Oxidative stress: NRF2-regulated antioxidant defence counters the oxidative stress implicated in the muscle and central-nervous-system dysfunction of fibromyalgia."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "Cytokine signalling: IL-6 and inflammatory-cytokine signalling through JAK-STAT (IL-6 already mapped) contributes to the neuroinflammatory component of fibromyalgia."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "GSK-3β signalling in the central nervous system shapes the synaptic plasticity and pain-modulation balance relevant to the central sensitisation of fibromyalgia."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "IL-6-STAT3 signalling transduces the inflammatory tone implicated in the neuroinflammatory component and fatigue of fibromyalgia."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Galectin-3 released by activated microglia amplifies the neuroinflammation thought to contribute to the central pain amplification of fibromyalgia."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "IFN-STAT1 neuroinflammatory signaling in activated microglia is implicated in the central sensitization of fibromyalgia."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "Cytosolic DNA sensing through cGAS-STING contributes to the low-grade neuroinflammatory tone proposed in fibromyalgia."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "FOXO downstream of stress and insulin-PI3K signaling governs neuronal oxidative-stress handling relevant to the stress vulnerability of fibromyalgia."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "PI3K-AKT signaling in dorsal-horn neurons participates in the central sensitization underlying the amplified pain of fibromyalgia."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "HIF-1α-linked metabolic and mitochondrial dysfunction contributes to the muscle and neural energetics implicated in fibromyalgia."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "S100A8/A9 alarmins reflect the low-grade neuroinflammatory activation associated with fibromyalgia."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "PI3K (PIK3CA)-AKT signaling (AKT already mapped), downstream of BDNF-TrkB (BDNF and NTRK already mapped), participates in the central-sensitization neuroplasticity of fibromyalgia."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "mTOR signaling participates in the synaptic plasticity underlying the central sensitization of fibromyalgia."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK-linked metabolic signaling participates in the mitochondrial and metabolic disturbances associated with fibromyalgia."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Autophagy modulates the neuronal and glial homeostasis implicated in the central sensitization of fibromyalgia."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC-family kinase signaling participates in the NMDA-receptor and synaptic-plasticity mechanisms of the central sensitization of fibromyalgia."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "DNMT3A-mediated DNA methylation participates in the epigenetic regulation of the pain-processing and stress pathways of fibromyalgia."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-driven chemokine signaling participates in the neuroimmune and glial responses implicated in fibromyalgia."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "CXCL12-CXCR4 signaling participates in the neuroimmune and pain-sensitization interactions implicated in fibromyalgia."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "IL-33 alarmin signaling participates in the neuroinflammatory and glial responses implicated in fibromyalgia."
  - target: 01-human/03-molecular/thyroid-hormones
    relation: connects-to
    note: "Thyroid overlap: hypothyroidism produces widespread pain, fatigue and cognitive slowing that mimic and worsen fibromyalgia, so thyroid-hormone status is a standard part of the assessment to exclude a treatable contributor."
  - target: 01-human/03-molecular/progesterone
    relation: connects-to
    note: "Neurosteroid modulation: progesterone-derived allopregnanolone potentiates GABA-A signalling, and its cyclical fall is linked to premenstrual worsening of fibromyalgia pain, part of the sex-hormone influence on central pain processing behind the female predominance."
  - target: 01-human/03-molecular/xanthine-oxidase
    relation: connects-to
    note: "Oxidative stress: increased oxidative stress, to which xanthine-oxidase-derived reactive oxygen species contribute, is reported in fibromyalgia and may aggravate the mitochondrial dysfunction and muscle pain of the syndrome."
  - target: 01-human/03-molecular/angiotensin-ii
    relation: connects-to
    note: "Brain renin-angiotensin: central angiotensin II modulates stress reactivity and pain processing, and the RAS interacts with the HPA axis (cortisol already mapped), a neuroendocrine dimension of the stress-linked pathophysiology of fibromyalgia."
  - target: 01-human/03-molecular/insulin
    relation: connects-to
    note: "Metabolic overlap: fibromyalgia is associated with insulin resistance and metabolic dysregulation beyond what obesity explains (leptin already mapped), a metabolic dimension increasingly recognised alongside the pain and fatigue."
  - target: 01-human/03-molecular/aldosterone
    relation: connects-to
    note: "Mineralocorticoid stress axis: aldosterone acts on brain mineralocorticoid receptors that, balanced against glucocorticoid receptors (already mapped), tune the stress response implicated in the HPA-axis dysregulation of fibromyalgia."
  - target: 01-human/03-molecular/prostaglandins
    relation: connects-to
    note: "Pain eicosanoids: prostaglandins sensitise peripheral and central pain pathways in fibromyalgia (substance P already mapped), yet the limited response to NSAIDs reflects that the dominant mechanism is central rather than inflammatory."
  - target: 01-human/03-molecular/vasopressin
    relation: connects-to
    note: "Neuroendocrine stress arm: vasopressin, with CRH and ACTH (already mapped), drives the hypothalamic-pituitary-adrenal axis whose dysregulation is implicated in the fatigue and stress-sensitivity of fibromyalgia."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "Neuroinflammatory signature: a mild elevation of IL-17 and other cytokines (IL-6, TNF and IL-1 already mapped) is reported in fibromyalgia, consistent with the low-grade neuroinflammation thought to contribute to central sensitisation."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "Neuroimmune balance: the anti-inflammatory IL-4, with IL-10 (already mapped), counters the mildly elevated pro-inflammatory cytokines (IL-6, TNF and IL-1 already mapped) of the low-grade neuroinflammation implicated in fibromyalgia."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "Zinc and glutamate: zinc modulates the glutamatergic (already mapped) NMDA signalling central to the pain sensitisation of fibromyalgia, and low zinc status has been reported in the condition."
  - target: 01-human/02-atomic/copper
    relation: connects-to
    note: "Copper and monoamines: copper is the cofactor of dopamine-β-hydroxylase, which makes noradrenaline from dopamine (both already mapped), linking copper to the monoamine signalling that the SNRIs used in fibromyalgia target."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "Type-2 neuroimmunity: IL-13, with IL-4 (already mapped), supports the M2 microglia (already mapped) and the anti-inflammatory arm balancing the central neuroinflammation (IL-1, IL-6 and TNF already mapped) implicated in fibromyalgia."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Adipokine dimension: adiponectin, with leptin (already mapped), is part of the adipokine milieu of the metabolic and inflammatory comorbidity that accompanies the pain and fatigue of fibromyalgia."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), links the adipose-inflammatory state to the low-grade inflammation associated with the symptom burden of fibromyalgia."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "Mood comorbidity: major depression is highly comorbid with fibromyalgia, the two sharing the serotonin-norepinephrine (already mapped) and stress (HPA and cortisol already mapped) dysregulation and the SNRI treatment."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "Neurogenic mast cells: the increased dermal mast cells (histamine already mapped) and the neurogenic (substance-P and CGRP already mapped) inflammation are implicated in the pain and the small-fibre involvement of fibromyalgia."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "Zinc status: the low zinc status reported in fibromyalgia; zinc modulates the NMDA and glutamate (already mapped) signalling and the antioxidant (xanthine oxidase already mapped) defence."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Innate neuroinflammation: the type-I interferon, downstream of the cGAS-STING (already mapped) pathway, is part of the low-grade neuroinflammation (IL-6 and TNF already mapped) implicated in the central sensitisation of fibromyalgia."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Th1 arm: the IFN-γ of the T cells is the type-II interferon arm of the subtle immune-inflammatory dimension associated with fibromyalgia."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the immune-inflammatory dimension reported in fibromyalgia."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the subtle immune dysregulation reported in fibromyalgia."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the immune-inflammatory dimension reported in fibromyalgia."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension reported in a subset of fibromyalgia."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Psychoneuroimmune arm: the peripheral cytotoxic T cells (perforin pathway) reflect the adaptive-immune activation reported in the small-fibre and psychoneuroimmune dimension of fibromyalgia."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "CNS-border antigen presentation: the dendritic cells of the meningeal and CNS-border compartments present antigen to the T cells (already mapped) of the neuroinflammation implicated in the central sensitisation of fibromyalgia."
  - target: 01-human/02-atomic/selenium
    relation: connects-to
    note: "Antioxidant micronutrient: selenium, a selenoprotein antioxidant cofactor whose low status is reported in fibromyalgia, is part of the oxidative-stress and micronutrient dimension of the disorder."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Neuroimmune complement: the complement C3 activation is part of the low-grade neuroinflammation implicated in the central sensitisation of fibromyalgia."
  - target: 01-human/03-molecular/c5ar1
    relation: connects-to
    note: "C5a receptor: the C5aR1 signalling (with the complement C3 already mapped) links the complement to the microglial (already mapped) neuroinflammation implicated in fibromyalgia."
  - target: 01-human/03-molecular/factor-h
    relation: connects-to
    note: "Complement regulation: factor H regulates the alternative complement pathway (complement C3 and C5aR1 already mapped) of the neuroinflammation implicated in fibromyalgia."
  - target: 01-human/03-molecular/tslp
    relation: connects-to
    note: "Mast-cell sensitiser: TSLP, released from keratinocytes and connective-tissue cells, activates mast cells (already mapped) in fibromyalgia, promoting the central-sensitisation cascade driven by IL-4 and IL-13 (already mapped)."
  - target: 01-human/03-molecular/bradykinin
    relation: connects-to
    note: "Kinin pain amplifier: bradykinin, acting through B1 and B2 receptors, lowers the nociceptive threshold and amplifies the CGRP (already mapped) and substance P (already mapped) pain signals of fibromyalgia."
  - target: 01-human/03-molecular/erythropoietin
    relation: connects-to
    note: "Neurotrophic EPO: erythropoietin, signalling through EPOR on neurons (already mapped), exerts neuroprotective and analgesic effects, modulating the central sensitisation and nociceptive threshold of fibromyalgia."
  - target: 01-human/03-molecular/c1-esterase-inhibitor
    relation: connects-to
    note: "Contact-pathway pain modulation: the C1-esterase inhibitor controls the contact-pathway activation (bradykinin already mapped) and classical complement in the central sensitisation of fibromyalgia, regulating the kinin-driven amplification of the nociceptive signal."
  - target: 01-human/03-molecular/periostin
    relation: connects-to
    note: "Connective-tissue ECM: periostin, expressed in peritendinous and fascial connective tissue, may contribute to the tender-point ECM remodelling and the altered mechanical nociception (CGRP and substance P already mapped) of fibromyalgia."
  - target: 01-human/03-molecular/complement-c5
    relation: connects-to
    note: "Neuroinflammatory complement: complement C5, upstream of MAC and C5aR1 (already mapped), amplifies the neuroimmune and glial (microglia already mapped) inflammation that sustains the central sensitisation and widespread pain of fibromyalgia."
  - target: 01-human/03-molecular/testosterone
    relation: connects-to
    note: "FM testosterone: testosterone deficiency amplifies substance-p (already mapped) driven central sensitisation in fibromyalgia; androgen receptor signalling also modulates the cortisol (already mapped) HPA axis dysregulation and the norepinephrine (already mapped) imbalance."
  - target: 01-human/03-molecular/prolactin
    relation: connects-to
    note: "FM prolactin: prolactin modulates the HPA axis (cortisol already mapped) and amplifies IL-6 (already mapped) neuroinflammation in fibromyalgia; elevated prolactin worsens substance-p (already mapped) driven central sensitisation and impairs BDNF (already mapped) signalling."
  - target: 01-human/03-molecular/transferrin
    relation: connects-to
    note: "FM transferrin: transferrin delivers iron for dopamine (already mapped) and norepinephrine (already mapped) synthesis; iron deficiency amplifies glutamate (already mapped) excitotoxicity and worsens BDNF (already mapped) signalling in the fibromyalgia brain (already mapped)."
  - target: 01-human/02-atomic/iodine
    relation: connects-to
    note: "FM iodine: thyroid hormones (iodine-dependent) modulate serotonin (already mapped) and dopamine (already mapped) sensitivity; iodine deficiency amplifies NF-κB (already mapped) neuroinflammation and worsens glutamate (already mapped) excitotoxicity in central sensitisation."
  - target: 01-human/02-atomic/potassium
    relation: connects-to
    note: "FM potassium: potassium channels regulate the threshold for substance P (already mapped) and glutamate (already mapped) central sensitisation; potassium dysregulation amplifies NF-κB (already mapped) neuroinflammation and impairs dopamine (already mapped) neurotransmission."
  - target: 01-human/02-atomic/phosphorus
    relation: connects-to
    note: "FM phosphorus: ATP-phosphate metabolism drives NF-κB (already mapped) neuroinflammatory signalling; phosphorus-dependent PI3K/AKT sustains BDNF (already mapped) neurotrophic support and modulates glutamate (already mapped) excitotoxicity in fibromyalgia central sensitisation."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "FM iron: iron, via ferroptosis-signalling and monoamine synthesis, regulates dopamine (already mapped) and serotonin (already mapped) neurotransmission; iron deficiency amplifies NF-κB (already mapped) central sensitisation and BDNF (already mapped) deficit in fibromyalgia."
  - target: 01-human/02-atomic/chloride
    relation: connects-to
    note: "FM chloride: chloride homeostasis via GABA(A) receptors (GABA already mapped) sets the inhibitory tone; chloride dysregulation amplifies glutamate (already mapped) excitotoxicity and NF-κB (already mapped) and substance P (already mapped) central sensitisation in fibromyalgia."
  - target: 01-human/02-atomic/sulfur
    relation: connects-to
    note: "FM sulfur: H2S from sulfur-amino acids in neurons (already mapped) and astrocytes (already mapped) modulates GABA (already mapped) inhibitory tone; sulfur deficiency amplifies NF-κB (already mapped) and substance P (already mapped) and glutamate (already mapped) excitotoxicity."
  - target: 01-human/02-atomic/nitrogen
    relation: connects-to
    note: "FM nitrogen: nitric oxide from iNOS in microglia (already mapped) modulates glutamate (already mapped) central sensitisation; nitrogen excess amplifies NF-κB (already mapped) and substance P (already mapped) and NLRP3 (already mapped) neuroinflammation in fibromyalgia."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "FM oxygen: mitochondrial oxygen sustains ATP in neurons (already mapped) for GABA (already mapped) inhibitory tone; hypoxia amplifies NF-κB (already mapped) and NLRP3 (already mapped) neuroinflammation and substance P (already mapped) sensitisation in fibromyalgia."
  - target: 01-human/02-atomic/carbon
    relation: connects-to
    note: "FM carbon: carbon, as metabolic backbone of neurotransmitters in neurons (already mapped) and astrocytes (already mapped), drives GABA (already mapped) synthesis; carbon dysregulation amplifies NF-κB (already mapped) and substance P (already mapped) sensitisation in fibromyalgia."
  - target: 01-human/02-atomic/chloride
    relation: connects-to
    note: "FM chloride: chloride channels in neurons (already mapped) and astrocytes (already mapped) modulate GABA (already mapped) inhibitory tone; chloride dysregulation amplifies NF-κB (already mapped) and substance P (already mapped) sensitisation in fibromyalgia."
  - target: 01-human/02-atomic/hydrogen
    relation: connects-to
    note: "FM hydrogen: hydrogen, via redox homeostasis in microglia (already mapped) and astrocytes (already mapped), quenches neuroinflammatory ROS; hydrogen dysregulation amplifies NF-κB (already mapped) and substance P (already mapped) sensitisation in fibromyalgia."
  - target: 01-human/03-molecular/pd-1
    relation: connects-to
    note: "FM pd-1: PD-1 on T-cytotoxic cells (already mapped) and microglia (already mapped) suppresses neuroimmune surveillance; pd-1 dysfunction amplifies NF-κB (already mapped) and substance P (already mapped) and IL-6 (already mapped) central sensitisation cascade of fibromyalgia."
  - target: 01-human/03-molecular/glp-1
    relation: connects-to
    note: "FM glp-1: GLP-1 from neurons (already mapped) and astrocytes (already mapped) modulates metabolic-neuroinflammatory tone; glp-1 dysfunction amplifies NF-κB (already mapped) and substance P (already mapped) and IL-6 (already mapped) sensitisation cascade of fibromyalgia."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "FM vegf: VEGF from microglia (already mapped) and astrocytes (already mapped) drives neuroinflammatory angiogenesis; vegf dysregulation amplifies NF-κB (already mapped) and substance P (already mapped) and IL-6 (already mapped) central sensitisation cascade of fibromyalgia."
sources:
  - id: wolfe-2016-fibromyalgia-criteria
    type: peer-reviewed
    cite: "Wolfe F, Clauw DJ, Fitzcharles MA, et al. 2016 Revisions to the 2010/2011 fibromyalgia diagnostic criteria. Semin Arthritis Rheum. 2016;46(3):319-329."
    doi: "10.1016/j.semarthrit.2016.08.012"
    pmid: "27916278"
    url: "https://doi.org/10.1016/j.semarthrit.2016.08.012"
  - id: clauw-2014-fibromyalgia-review
    type: peer-reviewed
    cite: "Clauw DJ. Fibromyalgia: a clinical review. JAMA. 2014;311(15):1547-1555."
    doi: "10.1001/jama.2014.3266"
    pmid: "24737367"
    url: "https://doi.org/10.1001/jama.2014.3266"
  - id: harris-2007-fibromyalgia-dopamine
    type: peer-reviewed
    cite: "Harris RE, Clauw DJ, Scott DJ, et al. Decreased central mu-opioid receptor availability in fibromyalgia. J Neurosci. 2007;27(37):10000-10006."
    doi: "10.1523/JNEUROSCI.2849-07.2007"
    pmid: "17855614"
    url: "https://doi.org/10.1523/JNEUROSCI.2849-07.2007"
---

# Fibromyalgia

## Overview

**Fibromyalgia (FM)** is a chronic syndrome of widespread musculoskeletal pain, fatigue, cognitive impairment ("fibro fog"), and sleep disturbance, resulting from **central pain amplification** rather than peripheral tissue damage. FM was reconceptualized in the 2000s–2010s from a rheumatic/musculoskeletal diagnosis to a **central sensitization syndrome** — a disorder of pain processing in the brain and spinal cord, not a primary inflammatory or structural condition [^clauw-2014-fibromyalgia-review].

**Epidemiology:**
- Prevalence: 2–3% globally; ~10 million Americans
- Female:male ratio ~3:1; peak onset ages 30–50
- Strong comorbidity with other central sensitization syndromes: IBS (30–70%), migraine (32%), interstitial cystitis, temporomandibular disorder
- High psychiatric comorbidity: depression (40%), anxiety (30%), PTSD (45% in FM patients from trauma backgrounds)
- High economic burden: annual direct costs ~$4,000–$8,000/patient; major cause of disability claims

**Why it matters:** FM is the **prototypical central sensitization disorder** — it established that chronic pain can be maintained entirely by central neuroplastic changes (amplified spinal and cortical pain processing) in the absence of ongoing tissue pathology. This paradigm has reshaped pain medicine and validated nociplastic pain as a distinct mechanistic category alongside nociceptive and neuropathic pain.

**2021 classification:** The International Association for the Study of Pain (IASP) coined the term **nociplastic pain** — pain arising from altered nociception without clear evidence of tissue damage or nerve injury — specifically to capture FM, IBS, and related syndromes.

## Structure

### Diagnostic criteria (ACR 2016 / Wolfe et al.)

FM diagnosis requires ALL three: [^wolfe-2016-fibromyalgia-criteria]

1. **Widespread Pain Index (WPI) ≥ 7** AND **Symptom Severity Scale (SSS) ≥ 5**
   OR **WPI 4–6** AND **SSS ≥ 9**

2. Symptoms present at **similar level for ≥ 3 months**

3. FM diagnosis is appropriate **regardless of other diagnoses** (fibromyalgia does not exclude other painful conditions)

**WPI regions (0–19):** Jaw, chest, abdomen, upper/lower back, neck + bilateral: shoulder girdle, upper arm, lower arm, hip/buttock, upper leg, lower leg (count each region where pain was present in past week)

**SSS (0–12):** Scores for sleep problems, fatigue, cognitive problems (0-3 each) + somatic symptoms presence (0-3 global)

**Subgroups:**
| Subgroup | Profile | Treatment implications |
|:---|:---|:---|
| **Central sensitization primary** | No peripheral trigger; bilateral; high SSS | SNRI + pregabalin + CBT; avoid opioids |
| **Post-trauma/post-infectious** | Onset after injury, surgery, viral illness | Address underlying trigger; trauma-informed care |
| **Comorbid rheumatic** | Concurrent RA, lupus, OA | Treat both; address central component separately |
| **Psychiatric comorbid** | High depression/anxiety/PTSD | Integrated psychiatric + pain management |

### Assessment tools

| Tool | Purpose |
|:---|:---|
| **FIQ-R (Fibromyalgia Impact Questionnaire — Revised)** | 21-item; functional impairment, symptom severity |
| **FKBQ (FM Keele STarT tool)** | Risk stratification for outcome |
| **BPI (Brief Pain Inventory)** | Pain severity and interference |
| **PCS (Pain Catastrophizing Scale)** | Predicts treatment response; catastrophizing = poor outcome |
| **PSQI / ESS** | Sleep quality and daytime sleepiness |

## Function

### Central sensitization mechanisms

**Spinal wind-up (SP-NMDA synergy):**
- Repetitive C-fiber input → sustained SP release at dorsal horn → NK1R activation → membrane depolarization → removes Mg²⁺ block from NMDA receptors
- SP (NK1R) + glutamate (NMDA) → synergistic Ca²⁺ influx → PKC-ε activation → phosphorylation of NR2B → reduced NMDA activation threshold
- Result: spinal cord amplifies innocuous stimuli as painful (allodynia) and amplifies painful stimuli excessively (hyperalgesia)

**Descending pain inhibition failure:**
- Normally, brainstem RVM and PAG project serotonergic and noradrenergic fibers to spinal dorsal horn → suppress pain signals
- In FM: reduced descending 5-HT and NE inhibitory tone → unopposed SP/glutamate-driven amplification
- CSF 5-HIAA (5-HT metabolite) is reduced in FM; CSF MHPG (NE metabolite) reduced in some studies
- Duloxetine and milnacipran restore descending inhibition by increasing 5-HT and NE availability

**Dopamine and endogenous analgesia:**
- Nucleus accumbens (NAcc) dopamine normally activates the mesolimbic descending antinociception system — DA D2R agonism reduces pain
- PET studies (Harris 2007) [^harris-2007-fibromyalgia-dopamine] show reduced NAcc mu-opioid receptor availability AND reduced dopamine function in FM
- Blunted NAcc DA → impaired endogenous opioid/dopamine analgesia → pain persists without pharmacological support

### Brain imaging findings in FM

| Finding | Method | Significance |
|:---|:---|:---|
| ↑ Posterior insula glutamate | MRS | Correlates with pain severity |
| ↑ ACC, insula activation to pain | fMRI | Disproportionate cortical response to low stimuli |
| ↑ Thalamic excitability | PET/fMRI | Reduced thalamic gating of pain |
| ↓ Endogenous opioid receptor availability | PET ([¹¹C]carfentanil) | Tonically occupied by endogenous opioids in pain state |
| Gray matter ↓ in dlPFC, ACC | VBM MRI | Correlates with pain chronicity; partially reversible |
| Altered default mode network | Resting-state fMRI | Predicts treatment response to CBT |

## Pathology

### Pathophysiology summary

FM is not a single-etiology disorder but a convergent syndrome resulting from the intersection of:
1. **Genetic predisposition:** 5-HT2A promoter variants, COMT Val158Met (catecholamine metabolism), TRPV3 variants
2. **Triggering events:** Physical trauma, surgery, viral illness, psychosocial stress (PTSD, adverse childhood experiences)
3. **Neuroplastic amplification:** SP-NMDA wind-up → dorsal horn sensitization → cortical reorganization
4. **Sleep disruption:** Non-restorative sleep → reduced central pain inhibition (α-EEG anomaly — intrusion of alpha waves into delta sleep) → bidirectional worsening

### Medical and psychiatric comorbidities

| Comorbidity | Prevalence in FM | Shared mechanism |
|:---|:---|:---|
| IBS / functional dyspepsia | 30–70% | Central sensitization (shared spinal pathways) |
| Migraine | 32% | Trigeminal sensitization, shared SP/CGRP |
| PTSD | 45% (trauma-onset FM) | CRH-driven HPA dysregulation, central sensitization |
| Major depressive disorder | 30–40% | Shared serotonin/NE/dopamine hypofunction |
| Generalized anxiety disorder | 25–35% | Shared HPA axis dysregulation |
| Non-restorative sleep / sleep apnea | >70% | Sleep disruption amplifies central sensitization |

### Treatment

**FDA-approved pharmacotherapy:**

| Drug | Mechanism | Evidence |
|:---|:---|:---|
| **Duloxetine (Cymbalta)** | SNRI; ↑ NE/5-HT in descending pain pathways | FDA 2008; 30–60% pain reduction vs 20% placebo; NNT ~8-10 |
| **Milnacipran (Savella)** | SNRI (NE > 5-HT); unique for FM-first FDA approval | FDA 2009; comparable efficacy to duloxetine |
| **Pregabalin (Lyrica)** | α2δ VGCC subunit ligand; reduces SP/glutamate release | FDA 2007; reduces pain and improves sleep; NNT ~10-12 |

**Other evidence-based options (off-label):**
- **Amitriptyline (10–50 mg):** Low-dose TCA; 5-HT/NE + H1 + anticholinergic → pain + sleep; NNT ~4-5 (strong evidence)
- **Cyclobenzaprine:** Tricyclic muscle relaxant; reduces alpha-EEG sleep anomaly; small but consistent effect
- **Gabapentin:** α2δ ligand (like pregabalin); often used off-label; comparable to pregabalin
- **Low-dose naltrexone (LDN, 1.5–4.5 mg):** Blocks microglial Toll-like receptor 4; anti-neuroinflammatory; 3 small RCTs positive for pain reduction — promising but not yet replicated in large trials
- **Tramadol:** Weak opioid + NE/5-HT reuptake; some FM evidence but opioid concerns
- **Opioids (standard):** NOT recommended — no RCT evidence in FM; may worsen central sensitization via opioid-induced hyperalgesia

**Non-pharmacological (first-line alongside or instead of drugs):**
- **Aerobic exercise:** Best long-term intervention; reduces central sensitization; improves sleep, mood, and pain; dose-dependent effect; water aerobics well-tolerated for severe cases
- **CBT:** Reduces pain catastrophizing; addresses fear-avoidance; improves function; NNT comparable to pharmacotherapy
- **Multidisciplinary pain rehabilitation:** Integrates CBT, physiotherapy, occupational therapy — most effective for severe FM
- **Sleep hygiene / CBT-I:** Treating non-restorative sleep directly reduces FM pain

## Connections

- `connects-to` → **[Glutamate](../../../03-molecular/glutamate/README.md)** — spinal NMDA receptor hyperactivation by repetitive C-fiber nociceptive input + substance P → wind-up and central sensitization; elevated glutamate in posterior insula measurable by MRS correlates with FM symptom severity; NMDA antagonists (ketamine) reduce FM pain in controlled trials.

- `connects-to` → **[Serotonin](../../../03-molecular/serotonin/README.md)** — descending serotonergic inhibition from raphe nuclei to spinal dorsal horn is impaired in FM (reduced CSF 5-HIAA); duloxetine (SNRI) and amitriptyline (TCA) restore descending inhibition; 5-HT3 antagonist tropisetron reduces FM pain in small RCTs; 5-HT2A receptor polymorphisms are associated with FM susceptibility.

- `connects-to` → **[Norepinephrine](../../../03-molecular/norepinephrine/README.md)** — descending NE inhibitory pathways from LC to spinal dorsal horn are deficient in FM; duloxetine and milnacipran (both FDA-approved for FM) increase NE in descending pain pathways — the primary analgesic mechanism; NE deficiency in descending pathways amplifies SP-NMDA-driven central sensitization.

- `connects-to` → **[Dopamine](../../../03-molecular/dopamine/README.md)** — FM shows reduced NAcc dopamine release detected by PET; blunted NAcc DA → impaired endogenous mesolimbic analgesia (dopamine activates descending antinociceptive circuits); dopaminergic dysfunction may explain why reward and motivation are impaired in FM and why cognitive deficits (fibro fog) are prominent.

- `connects-to` → **[Substance P](../../../03-molecular/substance-p/README.md)** — CSF substance P is elevated ~3-fold in FM patients vs healthy controls — the most consistently replicated biological finding in FM; elevated SP drives NK1R sensitization at the dorsal horn → wind-up → diffuse hyperalgesia and allodynia; SP-NMDA synergy is the mechanistic core of FM's central pain amplification.

- `targets` → **[Brain](../../../06-organ/brain/README.md)** — FM involves thalamic hypersensitivity, ACC and posterior insula hyperactivation to pain stimuli (fMRI), and altered default mode network connectivity; MRS shows elevated glutamate in posterior insula correlating with pain severity; gray matter density reductions in dlPFC and ACC correlate with chronicity and partially reverse with effective treatment.

- `connects-to` → **[CGRP](../../../03-molecular/cgrp/README.md)** — CGRP is elevated in plasma and CSF in FM patients; CGRP-mediated peripheral C-fiber sensitization contributes to FM's widespread hyperalgesia and allodynia; anti-CGRP monoclonal antibodies (developed for migraine) are under investigation as potential FM treatments; CGRP and substance P are co-released from peripheral nociceptors and synergistically drive neurogenic inflammation.
- `connects-to` → **[Neuropathic Pain](../neuropathic-pain/README.md)** — FM and neuropathic pain share central sensitization mechanisms (NMDA wind-up, loss of descending inhibitory control) but differ mechanistically: neuropathic pain requires a demonstrable nerve lesion while FM is nociplastic (amplified without peripheral pathology); both respond to SNRIs (duloxetine, milnacipran) and α2δ ligands (pregabalin, gabapentin); small fiber neuropathy (SFN) co-occurs in approximately 40% of FM patients on skin biopsy.
- `connects-to` → **[Migraine](../migraine/README.md)** — Fibromyalgia and migraine frequently co-occur and share central sensitization and CGRP biology: both feature amplified pain processing and descending-inhibition failure, anti-CGRP antibodies developed for migraine are under study in FM, and SNRIs and exercise help both.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — Depression coexists with fibromyalgia in ~40-60%: they share serotonin-norepinephrine dysregulation and HPA-axis changes, the SNRIs duloxetine and milnacipran treat both, and depression worsens FM pain and disability—though FM pain is not merely somatized depression.
- `connects-to` → **[Generalized Anxiety Disorder](../generalized-anxiety-disorder/README.md)** — Anxiety disorders are highly comorbid with fibromyalgia: shared monoaminergic dysregulation and stress-axis dysfunction link them, anxiety amplifies pain perception and sleep disruption in a vicious cycle, and combined CBT plus SNRI treatment targets both pain and affective load.
- `connects-to` → **[PTSD](../ptsd/README.md)** — Fibromyalgia and PTSD overlap through central sensitization and stress: trauma and HPA-axis dysregulation prime the nervous system to amplify pain, PTSD is a common antecedent and comorbidity of fibromyalgia, and both respond to approaches targeting the stress-pain loop.
- `connects-to` → **[Rheumatoid Arthritis](../rheumatoid-arthritis/README.md)** — Fibromyalgia frequently coexists with rheumatoid arthritis as secondary fibromyalgia: central pain sensitization adds widespread non-inflammatory pain atop joint disease, so inflated disease-activity scores mislead—distinguishing them avoids overtreating RA.
- `connects-to` → **[Sjögren's Syndrome](../sjogrens-syndrome/README.md)** — Fibromyalgia is common in Sjögren's and other autoimmune diseases: chronic illness and dysautonomia drive central sensitization, so widespread pain and fatigue in Sjögren's often reflect comorbid fibromyalgia rather than active glandular inflammation.
- `connects-to` → **[Gut Microbiome](../gut-microbiome/README.md)** — Fibromyalgia is increasingly tied to the gut-brain axis: patients show an altered gut microbiome, and microbial metabolites may influence pain signaling and central sensitization—part of why it overlaps with IBS and why diet and microbiome are studied as modifiers.
- `connects-to` → **[Systemic Lupus Erythematosus](../systemic-lupus-erythematosus/README.md)** — Fibromyalgia is a major confounder in lupus: up to a third of SLE patients develop comorbid fibromyalgia, inflating disease-activity scores—so separating central-sensitization pain from true lupus inflammation guides whether to escalate immunotherapy or treat pain.
- `connects-to` → **[Hippocampus](../../05-tissue/hippocampus/README.md)** — Fibromyalgia involves the hippocampus and central pain processing: imaging shows hippocampal changes alongside augmented pain perception (central sensitization) and 'fibro-fog'—evidence that fibromyalgia is a disorder of brain pain processing, not peripheral tissue.
- `connects-to` → **[Insomnia Disorder](../insomnia-disorder/README.md)** — Nonrestorative sleep is core to fibromyalgia, not incidental: disrupted deep sleep lowers pain thresholds and worsens fatigue and cognition, and the disorder and insomnia reinforce each other—so sleep-targeted treatment is central to managing fibromyalgia.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — Fibromyalgia is a disorder of pain-processing neurons (central sensitization): amplified spinal and brain pain signaling makes normal stimuli hurt, so it is a problem of how the nervous system processes pain, not tissue damage—explaining why analgesics often fail.
- `connects-to` → **[Cortisol](../../03-molecular/cortisol/README.md)** — HPA-axis and cortisol dysregulation feature in fibromyalgia: blunted stress-hormone responses accompany the disorder, linking chronic stress and poor sleep to amplified pain—so fibromyalgia sits at the interface of the stress system and pain processing.
- `connects-to` → **[Microglia](../../04-cellular/microglia/README.md)** — Fibromyalgia may be sustained by activated microglia: these immune cells of the cord and brain release pain-amplifying cytokines, supporting the idea that central sensitization—a volume knob turned up on pain—has a neuroinflammatory basis.
- `connects-to` → **[GABA](../../03-molecular/gaba/README.md)** — Fibromyalgia shows weakened pain braking: reduced GABA, the main inhibitory transmitter, leaves descending pain control too weak to dampen signals—part of why gabapentinoids like pregabalin, which boost inhibitory tone, are among its few effective drugs.
- `connects-to` → **[Peripheral Nerve](../../05-tissue/peripheral-nerve/README.md)** — Fibromyalgia is not purely central: about half of patients have small-fiber neuropathy, with reduced nerve-fiber density in skin biopsies—so damaged peripheral nerves may feed the amplified pain, blurring the line between central and peripheral pain disorders.
- `connects-to` → **[Thyroid Gland](../../06-organ/thyroid/README.md)** — Hypothyroidism mimics and worsens fibromyalgia: low thyroid hormone causes the same fatigue, aches and cognitive fog, so checking the thyroid is essential before settling on a fibromyalgia diagnosis—and treating it can relieve overlapping symptoms.
- `connects-to` → **[Vitamin D (Calciferol)](../../../03-medicine/03-food/vitamin-d/README.md)** — Vitamin D deficiency is common in fibromyalgia and may amplify pain: low levels are linked to more widespread musculoskeletal pain, and repletion is a simple, often-checked step that can modestly ease symptoms in deficient patients.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Fibromyalgia's lead drugs act on calcium channels: pregabalin and gabapentin bind the alpha-2-delta subunit of voltage-gated calcium channels in overactive pain neurons, dampening neurotransmitter release—calming the central sensitization that drives the pain.
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — Fibromyalgia is linked to low magnesium: the mineral gates the NMDA receptor and fuels muscle energy, so deficiency may heighten the central pain sensitization and fatigue, and supplementation is studied as an adjunct.
- `connects-to` → **[Astrocyte](../../04-cellular/astrocyte/README.md)** — Fibromyalgia's central sensitization runs through astrocytes: together with microglia, these glial cells amplify pain signaling in the spinal cord and brain, turning up the volume on normal sensations into the widespread pain that defines it.
- `connects-to` → **[Growth Hormone](../../03-molecular/growth-hormone/README.md)** — Fibromyalgia disrupts growth hormone via broken sleep: the lack of deep slow-wave sleep blunts nighttime GH secretion and lowers IGF-1, contributing to the poor tissue repair, fatigue, and muscle pain of the syndrome.
- `connects-to` → **[Synapse](../../05-tissue/synapse/README.md)** — Fibromyalgia is a disease of amplified pain synapses: central sensitization strengthens transmission in the spinal cord and brain so ordinary signals are felt as pain, shifting the disorder from the muscles to the synapses that process pain.
- `connects-to` → **[Large Intestine](../../06-organ/large-intestine/README.md)** — Fibromyalgia travels with the gut: irritable bowel syndrome overlaps heavily, and a disturbed microbiome and gut-brain signaling may feed the pain and fatigue, linking the large intestine to this whole-body pain disorder.
- `connects-to` → **[Mast Cell](../../04-cellular/mast-cell/README.md)** — Mast cells are an emerging suspect in fibromyalgia: increased in the skin of patients, they release mediators that sensitize nerve endings, offering one explanation for the widespread tenderness and the overlap with sensitivity syndromes.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Brain imaging shows fibromyalgia is real: fMRI photons reveal amplified activity in pain-processing networks to stimuli that wouldn't hurt others, objective evidence of the central sensitization behind the disorder.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — A skin biopsy can reveal fibromyalgia's nerves: many patients show small-fiber neuropathy, a reduced density of fine nerve endings in the skin that helps explain the burning, tingling quality of the pain.
- `connects-to` → **[BDNF](../../03-molecular/bdnf/README.md)** — BDNF helps wire fibromyalgia's amplified pain: this growth factor, raised in patients, promotes the synaptic plasticity that strengthens pain transmission, a molecular contributor to central sensitization.
- `connects-to` → **[Mu-Opioid Receptor](../../03-molecular/mu-opioid-receptor/README.md)** — Fibromyalgia's own painkillers are turned down: imaging shows reduced mu-opioid receptor availability and a blunted endogenous opioid system, which helps explain why opioid drugs work poorly and can even worsen the pain.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — Fibromyalgia comes with a jittery autonomic system: many patients have dysautonomia with palpitations, a racing resting heart, and orthostatic intolerance overlapping POTS, reflecting the same nervous-system dysregulation that amplifies pain.
- `connects-to` → **[Sodium](../../02-atomic/sodium/README.md)** — Overactive sodium channels keep the pain nerves firing: gain in voltage-gated sodium currents makes the sensory neurons of fibromyalgia hyperexcitable, part of the peripheral drive feeding the central sensitization.
- `connects-to` → **[Melatonin](../../03-molecular/melatonin/README.md)** — Fibromyalgia's unrefreshing sleep has a chemical signature: disrupted circadian rhythm and altered melatonin leave patients waking tired, and the resulting sleep deprivation itself lowers the pain threshold, locking in a vicious cycle.
- `connects-to` → **[Stomach](../../06-organ/stomach/README.md)** — The gut keeps fibromyalgia company: irritable bowel and functional dyspepsia overlap heavily with it through a shared gut-brain hypersensitivity, so bloating, pain, and altered bowel habit travel with the widespread body pain.
- `connects-to` → **[Adenosine](../../03-molecular/adenosine/README.md)** — Adenosine sits at the crossroads of its fatigue and pain: the molecule builds sleep pressure and dampens pain signaling, and disturbed adenosine handling may help explain the exhaustion and the poor pain control in fibromyalgia.
- `connects-to` → **[Endocannabinoid System](../../03-molecular/endocannabinoid/README.md)** — A 'clinical endocannabinoid deficiency' is one leading idea: low endocannabinoid tone may underlie fibromyalgia, migraine, and IBS together, the rationale behind trying cannabinoids to lift pain thresholds and ease the sleep disturbance.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — Fibromyalgia is overwhelmingly a women's diagnosis: symptoms often worsen premenstrually and around menopause as sex hormones shift, and it overlaps with painful menstrual and pelvic conditions, hinting hormones modulate central pain.
- `connects-to` → **[Small Intestine](../../06-organ/small-intestine/README.md)** — The small bowel may feed the pain: small intestinal bacterial overgrowth (SIBO) is found more often in fibromyalgia, and the bloating and altered gut signaling it brings feed back through the gut-brain axis onto central sensitization.
- `connects-to` → **[Estrogen](../../03-molecular/estrogen/README.md)** — A hormonal tilt may explain the female predominance: fibromyalgia overwhelmingly affects women and often flares perimenstrually and around menopause, hinting that falling estrogen — which modulates pain and serotonin pathways — lowers the pain threshold.
- `connects-to` → **[T Helper Cell](../../04-cellular/t-helper-cell/README.md)** — A faint immune signal underlies the pain: fibromyalgia shows low-grade neuroinflammation with raised cytokines from activated T cells and glia, evidence the disorder is more than purely psychological even without overt tissue damage.
- `connects-to` → **[Obesity](../obesity/README.md)** — Weight and pain worsen each other: obesity is common in fibromyalgia and amplifies pain and fatigue through inflammation, poor sleep and deconditioning, so weight management and exercise are core to treatment.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — It is increasingly seen as a nervous-system disorder: fibromyalgia is a disease of how the brain and cord process pain, amplifying ordinary signals through central sensitization rather than arising from damaged tissue at the painful sites.
- `connects-to` → **[NLRP3 Inflammasome](../../03-molecular/nlrp3-inflammasome/README.md)** — Glial inflammation may stoke the pain: activation of the NLRP3 inflammasome in microglia and the periphery releases IL-1β and other mediators implicated in the neuroinflammation thought to underlie fibromyalgia's amplified pain.
- `connects-to` → **[Natural Killer Cell](../../04-cellular/natural-killer-cell/README.md)** — Its immune profile is subtly off: reduced natural killer cell number and function are reported in fibromyalgia, part of the immune dysregulation it shares with chronic fatigue syndrome that hints at a low-grade immune component.
- `connects-to` → **[Interleukin-6](../../03-molecular/il-6/README.md)** — A low-grade cytokine hum accompanies the pain: IL-6 and other pro-inflammatory cytokines run modestly elevated in fibromyalgia, feeding the neuroinflammation and central sensitization thought to amplify pain signals.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — The pain is felt in muscle and joint though the tissue is intact: fibromyalgia presents as widespread musculoskeletal pain and tenderness without true inflammation or damage, the hallmark of a centrally driven pain disorder.
- `connects-to` → **[Panic Disorder](../panic-disorder/README.md)** — Anxiety travels with the pain: panic disorder and other anxiety conditions are markedly over-represented in fibromyalgia, sharing the stress-axis and autonomic dysregulation that link the two.
- `connects-to` → **[Opioid Use Disorder](../opioid-use-disorder/README.md)** — Treating the pain courts dependence: opioids are largely ineffective for fibromyalgia's central pain yet are still prescribed, and the chronic exposure carries real risk of tolerance, hyperalgesia and opioid use disorder.
- `connects-to` → **[Attention-Deficit/Hyperactivity Disorder](../attention-deficit-hyperactivity-disorder/README.md)** — Shared dopamine wiring and the cognitive overlap link them: ADHD is over-represented in fibromyalgia, and the inattention of 'fibro-fog' blurs with ADHD's, both tied to dopaminergic dysregulation.
- `connects-to` → **[Borderline Personality Disorder](../borderline-personality-disorder/README.md)** — Early trauma is a shared root: childhood adversity that predisposes to borderline personality disorder also sensitizes the central pain system, and the two co-occur, each amplifying the other's distress.
- `connects-to` → **[Bipolar Disorder](../bipolar-disorder/README.md)** — Mood instability runs alongside the pain: fibromyalgia shows markedly elevated rates of bipolar disorder, and the two share disturbances in sleep, stress reactivity and monoamine signaling.
- `connects-to` → **[Psoriatic Arthritis](../psoriatic-arthritis/README.md)** — Central pain confounds an inflammatory arthritis: fibromyalgia frequently coexists with psoriatic arthritis, where its widespread tenderness can mimic active joint disease and complicate measuring true inflammatory control.
- `connects-to` → **[Type 2 Diabetes](../type-2-diabetes/README.md)** — Metabolic disease and chronic pain overlap: fibromyalgia is more common in type 2 diabetes, sharing obesity, inflammation and the painful sensory changes that blur with diabetic neuropathy.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — It travels with a hypersensitive gut: irritable bowel syndrome and other functional GI disorders are strikingly common in fibromyalgia, both reflecting central sensitisation and visceral hyperalgesia.
- `connects-to` → **[Renal System](../renal-system/README.md)** — A bladder version of the same syndrome: interstitial cystitis/painful bladder syndrome overlaps heavily with fibromyalgia, part of a cluster of central sensitivity syndromes sharing amplified pain processing.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — Its stress axis runs awry: fibromyalgia is associated with dysregulation of the hypothalamic-pituitary-adrenal axis and growth-hormone secretion, and it often coexists with and is screened against thyroid disease.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — The skin reveals nerve loss: biopsy shows reduced intraepidermal nerve-fibre density in a large subset of fibromyalgia, evidence of a small-fibre neuropathy underlying some of its pain.
- `connects-to` → **[Immune System](../immune-system/README.md)** — Hints of immune involvement: neuroinflammation and, in some patients, an IgG autoantibody component shown by passive-transfer studies, alongside its frequent overlap with autoimmune rheumatic diseases.
- `connects-to` → **[Cardiovascular System](../cardiovascular-system/README.md)** — Its autonomic control falters: fibromyalgia often features dysautonomia with orthostatic intolerance, POTS-like tachycardia and palpitations, reflecting altered cardiovascular reflex regulation.
- `connects-to` → **[Respiratory System](../respiratory-system/README.md)** — It alters the pattern of breathing: a dysfunctional breathing pattern with air hunger and breathlessness despite normal lungs is common in fibromyalgia, part of its central-sensitivity symptom cluster.
- `connects-to` → **[COVID-19](../covid-19-disease/README.md)** — It can follow a viral illness: a fibromyalgia-like syndrome of widespread pain and fatigue commonly emerges after COVID-19, overlapping with long COVID.
- `connects-to` → **[Magnesium (Dietary)](../../../03-medicine/03-food/magnesium-dietary/README.md)** — Magnesium is studied for its symptoms: low magnesium can worsen muscle cramps and pain, and magnesium supplementation is investigated as an adjunct for fibromyalgia.
- `connects-to` → **[Fluoxetine](../../../03-medicine/01-modern/10-mental-health/fluoxetine/README.md)** — Antidepressants modulate the pain: SSRIs like fluoxetine, and especially the SNRI duloxetine, raise serotonin and noradrenaline to dampen the central pain amplification of fibromyalgia.
- `connects-to` → **[Epstein-Barr Virus](../../../02-pathogen/01-viruses/epstein-barr-virus/README.md)** — It can follow an infection: fibromyalgia often begins after a viral illness such as Epstein-Barr glandular fever, part of the post-infectious central-sensitisation picture also seen after COVID.
- `connects-to` → **[Ashwagandha](../../../03-medicine/02-traditional/ashwagandha/README.md)** — Traditional remedies are sought for it: adaptogens like ashwagandha are used by some for the fatigue, pain and poor sleep of fibromyalgia, complementing exercise and the established drugs.
- `connects-to` → **[Cannabis Use Disorder](../cannabis-use-disorder/README.md)** — Cannabinoids are widely tried for it: fibromyalgia is a leading reason for medical-cannabis use, and the clinical endocannabinoid deficiency hypothesis frames its pain and sleep disturbance — though efficacy is uncertain and dependence is a real risk.
- `connects-to` → **[Panax Ginseng](../../../03-medicine/02-traditional/panax-ginseng/README.md)** — A studied botanical adjunct: like ashwagandha, Panax ginseng has been trialled for the fatigue, pain and poor sleep of fibromyalgia, part of the complementary approaches patients often turn to when drugs disappoint.
- `connects-to` → **[Cancer Chemotherapy](../../../03-medicine/01-modern/13-cancer/cancer-chemotherapy/README.md)** — Treatment-related central sensitisation: chemotherapy and aromatase-inhibitor therapy in cancer survivors commonly cause chronic widespread musculoskeletal pain and fatigue resembling fibromyalgia, reflecting shared central pain-sensitisation mechanisms.
- `connects-to` → **[Ankylosing Spondylitis](../ankylosing-spondylitis/README.md)** — A confounding overlay on inflammatory arthritis: comorbid fibromyalgia is common in ankylosing spondylitis and inflates its disease-activity scores with widespread pain, so separating central sensitisation from active inflammation guides treatment.
- `connects-to` → **[Narcolepsy](../narcolepsy/README.md)** — Unrefreshing sleep links them: fibromyalgia and narcolepsy both fragment sleep and cause profound daytime fatigue, with alpha-wave intrusion into deep sleep a hallmark of the non-restorative sleep of fibromyalgia.
- `connects-to` → **[Epilepsy](../epilepsy/README.md)** — Shared central hyperexcitability: fibromyalgia and epilepsy both reflect neuronal hyperexcitability with disturbed glutamate/GABA balance, and the gabapentinoids pregabalin and gabapentin treat both.
- `connects-to` → **[Systemic Sclerosis](../systemic-sclerosis/README.md)** — A confounder in connective-tissue disease: fibromyalgia frequently coexists with systemic sclerosis, its central pain amplification inflating disease-activity scores and complicating assessment of true inflammatory burden.
- `connects-to` → **[Social Anxiety Disorder](../social-anxiety-disorder/README.md)** — The anxiety overlap: fibromyalgia is highly comorbid with anxiety disorders including social anxiety, sharing serotonergic-noradrenergic dysregulation that SNRIs like duloxetine target in both.
- `connects-to` → **[TNF-alpha](../../03-molecular/tnf-alpha/README.md)** — A low-grade neuroimmune signal: though fibromyalgia lacks classic inflammation, modestly raised TNF-α and other cytokines in blood and CSF support a neuroimmune contribution to its central sensitisation.
- `connects-to` → **[Intestinal Epithelium](../../05-tissue/intestinal-epithelium/README.md)** — The IBS overlap: fibromyalgia coexists strongly with irritable bowel syndrome, sharing central sensitisation and gut-brain dysregulation at the intestinal epithelium and barrier, so the two are best treated together.
- `connects-to` → **[Cardiac Conduction System](../../05-tissue/cardiac-conduction-system/README.md)** — Dysautonomia: fibromyalgia frequently features autonomic dysfunction with orthostatic intolerance, POTS and reduced heart-rate variability, reflecting dysregulated autonomic control of the cardiac conduction system.
- `connects-to` → **[Obsessive-Compulsive Disorder](../obsessive-compulsive-disorder/README.md)** — Anxiety-spectrum comorbidity: fibromyalgia is over-represented alongside obsessive-compulsive and other anxiety disorders, sharing the serotonergic and stress-axis dysregulation that links central pain to anxiety.
- `connects-to` → **[NPY](../../03-molecular/npy/README.md)** — Pain and autonomic dysregulation: altered neuropeptide Y signalling is implicated in the pain processing and autonomic dysfunction of fibromyalgia.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Adiposity and pain: leptin, elevated in obesity, correlates with fibromyalgia pain severity, linking adipose-driven inflammation to central sensitisation.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — Neuroinflammation: IL-1β and inflammasome activation contribute to the central neuroinflammation increasingly implicated in fibromyalgia.
- `connects-to` → **[Serotonin Transporter](../../03-molecular/serotonin-transporter/README.md)** — Descending pain control: serotonin-transporter polymorphisms and reduced serotonergic reuptake modulation underlie blunted descending inhibition in fibromyalgia, the rationale for SNRI and tricyclic therapy.
- `connects-to` → **[Oxytocin](../../03-molecular/oxytocin/README.md)** — Endogenous analgesia: oxytocin dampens nociception and stress reactivity, and lower oxytocinergic tone is linked to greater pain and distress in fibromyalgia, an emerging therapeutic target.
- `connects-to` → **[Nitric Oxide](../../03-molecular/nitric-oxide/README.md)** — Oxidative stress: dysregulated nitric oxide and peroxynitrite formation drive the mitochondrial oxidative stress and central sensitisation reported in fibromyalgia muscle and CNS.
- `connects-to` → **[IGF-1](../../03-molecular/igf-1/README.md)** — Many fibromyalgia patients have low IGF-1, reflecting the blunted growth-hormone secretion of disrupted deep sleep, which may impair muscle microtrauma repair and contribute to the chronic myalgia and the rationale once explored for GH supplementation.
- `connects-to` → **[NTRK / TrkA](../../03-molecular/ntrk/README.md)** — Elevated nerve growth factor signaling through TrkA sensitizes peripheral nociceptors and is linked to the small-fiber neuropathy found in a substantial subset of fibromyalgia patients—evidence of a peripheral contribution to a centrally amplified syndrome.
- `connects-to` → **[TLR4](../../03-molecular/tlr4/README.md)** — TLR4 signaling on microglia and astrocytes promotes the central sensitization of fibromyalgia, part of the neuroinflammatory amplification of pain processing in the spinal cord and brain that underlies the diffuse, persistent pain.
- `connects-to` → **[Orexin](../../03-molecular/orexin/README.md)** — Orexin signaling that stabilizes sleep-wake states and modulates descending pain control is dysregulated in fibromyalgia, contributing to the unrefreshing sleep and arousal disturbance that worsen the pain and fatigue.
- `connects-to` → **[Histamine](../../03-molecular/histamine/README.md)** — Increased dermal mast cells releasing histamine are found in fibromyalgia skin, a peripheral neuroinflammatory contributor to the sensory symptoms and one proposed link to its frequent overlap with mast-cell-activation conditions.
- `connects-to` → **[Acetylcholine](../../03-molecular/acetylcholine/README.md)** — Fibromyalgia features reduced vagal tone and a blunted cholinergic anti-inflammatory reflex, an autonomic imbalance that leaves inflammation unchecked and contributes to the dysautonomia accompanying the chronic pain.
- `connects-to` → **[CRH](../../03-molecular/crh/README.md)** — Corticotropin-releasing hormone sits at the apex of the dysregulated HPA stress axis of fibromyalgia, and its altered signaling links chronic stress to the central pain amplification of the disorder.
- `connects-to` → **[Glucocorticoid Receptor](../../03-molecular/glucocorticoid-receptor/README.md)** — A hypofunctional cortisol response and impaired glucocorticoid-receptor feedback characterize the HPA dysregulation of fibromyalgia, contributing to its fatigue, poor stress resilience and widespread pain.
- `connects-to` → **[Interleukin-10](../../03-molecular/il-10/README.md)** — The low-grade neuroinflammation of fibromyalgia (IL-1β, IL-6 and TNF-α already mapped) is normally restrained by regulatory IL-10, whose relative deficiency may sustain glial pain signaling.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — BDNF-TrkB signaling (BDNF and NTRK mapped) through MAPK-ERK in dorsal-horn neurons drives the spinal central sensitization that amplifies pain in fibromyalgia.
- `connects-to` → **[ACTH](../../03-molecular/acth/README.md)** — Blunted and dysregulated CRH-ACTH-cortisol stress-axis reactivity (CRH, cortisol and the glucocorticoid receptor mapped) is a characteristic neuroendocrine feature of fibromyalgia.
- `connects-to` → **[MYD88](../../03-molecular/myd88/README.md)** — TLR4 (mapped) signaling through MyD88 activates microglia and the neuroinflammatory cytokine response that contributes to the central pain amplification of fibromyalgia.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — NF-κB-driven neuroinflammation (downstream of the TLR4-MyD88 signaling already mapped) contributes to the glial activation and central sensitization of fibromyalgia.
- `connects-to` → **[NRF2](../../03-molecular/nfe2l2/README.md)** — NRF2-regulated antioxidant defense counters the oxidative stress implicated in the muscle and central-nervous-system dysfunction of fibromyalgia.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — IL-6 and inflammatory-cytokine signaling through JAK-STAT (IL-6 already mapped) contributes to the neuroinflammatory component of fibromyalgia.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β signaling in the central nervous system shapes the synaptic plasticity and pain-modulation balance relevant to the central sensitization of fibromyalgia.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — IL-6-STAT3 signaling transduces the inflammatory tone implicated in the neuroinflammatory component and fatigue of fibromyalgia.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Galectin-3 released by activated microglia amplifies the neuroinflammation thought to contribute to the central pain amplification of fibromyalgia.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — IFN-STAT1 neuroinflammatory signaling in activated microglia is implicated in the central sensitization of fibromyalgia.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — Cytosolic DNA sensing through cGAS-STING contributes to the low-grade neuroinflammatory tone proposed in fibromyalgia.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — FOXO downstream of stress and insulin-PI3K signaling governs neuronal oxidative-stress handling relevant to the stress vulnerability of fibromyalgia.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — PI3K-AKT signaling in dorsal-horn neurons participates in the central sensitization underlying the amplified pain of fibromyalgia.
- `connects-to` → **[HIF-1alpha](../../03-molecular/hif-1alpha/README.md)** — HIF-1α-linked metabolic and mitochondrial dysfunction contributes to the muscle and neural energetics implicated in fibromyalgia.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — S100A8/A9 alarmins reflect the low-grade neuroinflammatory activation associated with fibromyalgia.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — PI3K (PIK3CA)-AKT signaling (AKT already mapped), downstream of BDNF-TrkB (BDNF and NTRK already mapped), participates in the central-sensitization neuroplasticity of fibromyalgia.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — mTOR signaling participates in the synaptic plasticity underlying the central sensitization of fibromyalgia.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK-linked metabolic signaling participates in the mitochondrial and metabolic disturbances associated with fibromyalgia.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — Autophagy modulates the neuronal and glial homeostasis implicated in the central sensitization of fibromyalgia.
- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — SRC-family kinase signaling participates in the NMDA-receptor and synaptic-plasticity mechanisms of the central sensitization of fibromyalgia.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — DNMT3A-mediated DNA methylation participates in the epigenetic regulation of the pain-processing and stress pathways of fibromyalgia.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-driven chemokine signaling participates in the neuroimmune and glial responses implicated in fibromyalgia.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — CXCL12-CXCR4 signaling participates in the neuroimmune and pain-sensitization interactions implicated in fibromyalgia.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — IL-33 alarmin signaling participates in the neuroinflammatory and glial responses implicated in fibromyalgia.
- `connects-to` → **[Thyroid hormones](../../03-molecular/thyroid-hormones/README.md)** — Thyroid overlap: hypothyroidism produces widespread pain, fatigue and cognitive slowing that mimic and worsen fibromyalgia, so thyroid-hormone status is a standard part of the assessment to exclude a treatable contributor.
- `connects-to` → **[Progesterone](../../03-molecular/progesterone/README.md)** — Neurosteroid modulation: progesterone-derived allopregnanolone potentiates GABA-A signalling, and its cyclical fall is linked to premenstrual worsening of fibromyalgia pain, part of the sex-hormone influence on central pain processing behind the female predominance.
- `connects-to` → **[Xanthine oxidase](../../03-molecular/xanthine-oxidase/README.md)** — Oxidative stress: increased oxidative stress, to which xanthine-oxidase-derived reactive oxygen species contribute, is reported in fibromyalgia and may aggravate the mitochondrial dysfunction and muscle pain of the syndrome.
- `connects-to` → **[Angiotensin II](../../03-molecular/angiotensin-ii/README.md)** — Brain renin-angiotensin: central angiotensin II modulates stress reactivity and pain processing, and the RAS interacts with the HPA axis (cortisol already mapped), a neuroendocrine dimension of the stress-linked pathophysiology of fibromyalgia.
- `connects-to` → **[Insulin](../../03-molecular/insulin/README.md)** — Metabolic overlap: fibromyalgia is associated with insulin resistance and metabolic dysregulation beyond what obesity explains (leptin already mapped), a metabolic dimension increasingly recognised alongside the pain and fatigue.
- `connects-to` → **[Aldosterone](../../03-molecular/aldosterone/README.md)** — Mineralocorticoid stress axis: aldosterone acts on brain mineralocorticoid receptors that, balanced against glucocorticoid receptors (already mapped), tune the stress response implicated in the HPA-axis dysregulation of fibromyalgia.
- `connects-to` → **[Prostaglandins](../../03-molecular/prostaglandins/README.md)** — Pain eicosanoids: prostaglandins sensitise peripheral and central pain pathways in fibromyalgia (substance P already mapped), yet the limited response to NSAIDs reflects that the dominant mechanism is central rather than inflammatory.
- `connects-to` → **[Vasopressin](../../03-molecular/vasopressin/README.md)** — Neuroendocrine stress arm: vasopressin, with CRH and ACTH (already mapped), drives the hypothalamic-pituitary-adrenal axis whose dysregulation is implicated in the fatigue and stress-sensitivity of fibromyalgia.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — Neuroinflammatory signature: a mild elevation of IL-17 and other cytokines (IL-6, TNF and IL-1 already mapped) is reported in fibromyalgia, consistent with the low-grade neuroinflammation thought to contribute to central sensitisation.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — Neuroimmune balance: the anti-inflammatory IL-4, with IL-10 (already mapped), counters the mildly elevated pro-inflammatory cytokines (IL-6, TNF and IL-1 already mapped) of the low-grade neuroinflammation implicated in fibromyalgia.
- `connects-to` → **[Zinc](../../02-atomic/zinc/README.md)** — Zinc and glutamate: zinc modulates the glutamatergic (already mapped) NMDA signalling central to the pain sensitisation of fibromyalgia, and low zinc status has been reported in the condition.
- `connects-to` → **[Copper](../../02-atomic/copper/README.md)** — Copper and monoamines: copper is the cofactor of dopamine-β-hydroxylase, which makes noradrenaline from dopamine (both already mapped), linking copper to the monoamine signalling that the SNRIs used in fibromyalgia target.
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — Type-2 neuroimmunity: IL-13, with IL-4 (already mapped), supports the M2 microglia (already mapped) and the anti-inflammatory arm balancing the central neuroinflammation (IL-1, IL-6 and TNF already mapped) implicated in fibromyalgia.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — Adipokine dimension: adiponectin, with leptin (already mapped), is part of the adipokine milieu of the metabolic and inflammatory comorbidity that accompanies the pain and fatigue of fibromyalgia.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), links the adipose-inflammatory state to the low-grade inflammation associated with the symptom burden of fibromyalgia.
- `connects-to` → **[Major depressive disorder](../major-depressive-disorder/README.md)** — Mood comorbidity: major depression is highly comorbid with fibromyalgia, the two sharing the serotonin-norepinephrine (already mapped) and stress (HPA and cortisol already mapped) dysregulation and the SNRI treatment.
- `connects-to` → **[Mast cell](../../04-cellular/mast-cell/README.md)** — Neurogenic mast cells: the increased dermal mast cells (histamine already mapped) and the neurogenic (substance-P and CGRP already mapped) inflammation are implicated in the pain and the small-fibre involvement of fibromyalgia.
- `connects-to` → **[Zinc](../../02-atomic/zinc/README.md)** — Zinc status: the low zinc status reported in fibromyalgia; zinc modulates the NMDA and glutamate (already mapped) signalling and the antioxidant (xanthine oxidase already mapped) defence.
- `connects-to` → **[Type I interferon](../../03-molecular/type-i-interferon/README.md)** — Innate neuroinflammation: the type-I interferon, downstream of the cGAS-STING (already mapped) pathway, is part of the low-grade neuroinflammation (IL-6 and TNF already mapped) implicated in the central sensitisation of fibromyalgia.
- `connects-to` → **[IFN-gamma](../../03-molecular/ifn-gamma/README.md)** — Th1 arm: the IFN-γ of the T cells is the type-II interferon arm of the subtle immune-inflammatory dimension associated with fibromyalgia.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the immune-inflammatory dimension reported in fibromyalgia.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the subtle immune dysregulation reported in fibromyalgia.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the immune-inflammatory dimension reported in fibromyalgia.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension reported in a subset of fibromyalgia.
- `connects-to` → **[Cytotoxic T cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Psychoneuroimmune arm: the peripheral cytotoxic T cells (perforin pathway) reflect the adaptive-immune activation reported in the small-fibre and psychoneuroimmune dimension of fibromyalgia.
- `connects-to` → **[Dendritic cell](../../04-cellular/dendritic-cell/README.md)** — CNS-border antigen presentation: the dendritic cells of the meningeal and CNS-border compartments present antigen to the T cells (already mapped) of the neuroinflammation implicated in the central sensitisation of fibromyalgia.
- `connects-to` → **[Selenium](../../02-atomic/selenium/README.md)** — Antioxidant micronutrient: selenium, a selenoprotein antioxidant cofactor whose low status is reported in fibromyalgia, is part of the oxidative-stress and micronutrient dimension of the disorder.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Neuroimmune complement: the complement C3 activation is part of the low-grade neuroinflammation implicated in the central sensitisation of fibromyalgia.
- `connects-to` → **[C5aR1](../../03-molecular/c5ar1/README.md)** — C5a receptor: the C5aR1 signalling (with the complement C3 already mapped) links the complement to the microglial (already mapped) neuroinflammation implicated in fibromyalgia.
- `connects-to` → **[Factor H](../../03-molecular/factor-h/README.md)** — Complement regulation: factor H regulates the alternative complement pathway (complement C3 and C5aR1 already mapped) of the neuroinflammation implicated in fibromyalgia.
- `connects-to` → **[TSLP](../../03-molecular/tslp/README.md)** — Mast-cell sensitiser: TSLP, released from keratinocytes and connective-tissue cells, activates mast cells (already mapped) in fibromyalgia, promoting the central-sensitisation cascade driven by IL-4 and IL-13 (already mapped).
- `connects-to` → **[Bradykinin](../../03-molecular/bradykinin/README.md)** — Kinin pain amplifier: bradykinin, acting through B1 and B2 receptors, lowers the nociceptive threshold and amplifies the CGRP (already mapped) and substance P (already mapped) pain signals of fibromyalgia.
- `connects-to` → **[Erythropoietin](../../03-molecular/erythropoietin/README.md)** — Neurotrophic EPO: erythropoietin, signalling through EPOR on neurons (already mapped), exerts neuroprotective and analgesic effects, modulating the central sensitisation and nociceptive threshold of fibromyalgia.
- `connects-to` → **[C1-esterase inhibitor](../../03-molecular/c1-esterase-inhibitor/README.md)** — Contact-pathway pain modulation: the C1-esterase inhibitor controls the contact-pathway activation (bradykinin already mapped) and classical complement in the central sensitisation of fibromyalgia, regulating the kinin-driven amplification of the nociceptive signal.
- `connects-to` → **[Periostin](../../03-molecular/periostin/README.md)** — Connective-tissue ECM: periostin, expressed in peritendinous and fascial connective tissue, may contribute to the tender-point ECM remodelling and the altered mechanical nociception (CGRP and substance P already mapped) of fibromyalgia.
- `connects-to` → **[Complement C5](../../03-molecular/complement-c5/README.md)** — Neuroinflammatory complement: complement C5, upstream of MAC and C5aR1 (already mapped), amplifies the neuroimmune and glial (microglia already mapped) inflammation that sustains the central sensitisation and widespread pain of fibromyalgia.
- `connects-to` → **[Testosterone](../../03-molecular/testosterone/README.md)** — FM testosterone: testosterone deficiency amplifies substance-p (already mapped) driven central sensitisation in fibromyalgia; androgen receptor signalling also modulates the cortisol (already mapped) HPA axis dysregulation and the norepinephrine (already mapped) imbalance.
- `connects-to` → **[Prolactin](../../03-molecular/prolactin/README.md)** — FM prolactin: prolactin modulates the HPA axis (cortisol already mapped) and amplifies IL-6 (already mapped) neuroinflammation in fibromyalgia; elevated prolactin worsens substance-p (already mapped) driven central sensitisation and impairs BDNF (already mapped) signalling.
- `connects-to` → **[Transferrin](../../03-molecular/transferrin/README.md)** — FM transferrin: transferrin delivers iron for dopamine (already mapped) and norepinephrine (already mapped) synthesis; iron deficiency amplifies glutamate (already mapped) excitotoxicity and worsens BDNF (already mapped) signalling in the fibromyalgia brain (already mapped).
- `connects-to` → **[Iodine](../../02-atomic/iodine/README.md)** — FM iodine: thyroid hormones (iodine-dependent) modulate serotonin (already mapped) and dopamine (already mapped) sensitivity; iodine deficiency amplifies NF-κB (already mapped) neuroinflammation and worsens glutamate (already mapped) excitotoxicity in central sensitisation.
- `connects-to` → **[Potassium](../../02-atomic/potassium/README.md)** — FM potassium: potassium channels regulate the threshold for substance P (already mapped) and glutamate (already mapped) central sensitisation; potassium dysregulation amplifies NF-κB (already mapped) neuroinflammation and impairs dopamine (already mapped) neurotransmission.
- `connects-to` → **[Phosphorus](../../02-atomic/phosphorus/README.md)** — FM phosphorus: ATP-phosphate metabolism drives NF-κB (already mapped) neuroinflammatory signalling; phosphorus-dependent PI3K/AKT sustains BDNF (already mapped) neurotrophic support and modulates glutamate (already mapped) excitotoxicity in fibromyalgia central sensitisation.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — FM iron: iron, via ferroptosis-signalling and monoamine synthesis, regulates dopamine (already mapped) and serotonin (already mapped) neurotransmission; iron deficiency amplifies NF-κB (already mapped) central sensitisation and BDNF (already mapped) deficit in fibromyalgia.
- `connects-to` → **[Chloride](../../02-atomic/chloride/README.md)** — FM chloride: chloride homeostasis via GABA(A) receptors (GABA already mapped) sets the inhibitory tone; chloride dysregulation amplifies glutamate (already mapped) excitotoxicity and NF-κB (already mapped) and substance P (already mapped) central sensitisation in fibromyalgia.
- `connects-to` → **[Sulfur](../../02-atomic/sulfur/README.md)** — FM sulfur: H2S from sulfur-amino acids in neurons (already mapped) and astrocytes (already mapped) modulates GABA (already mapped) inhibitory tone; sulfur deficiency amplifies NF-κB (already mapped) and substance P (already mapped) and glutamate (already mapped) excitotoxicity.
- `connects-to` → **[Nitrogen](../../02-atomic/nitrogen/README.md)** — FM nitrogen: nitric oxide from iNOS in microglia (already mapped) modulates glutamate (already mapped) central sensitisation; nitrogen excess amplifies NF-κB (already mapped) and substance P (already mapped) and NLRP3 (already mapped) neuroinflammation in fibromyalgia.
- `connects-to` → **[Oxygen](../../02-atomic/oxygen/README.md)** — FM oxygen: mitochondrial oxygen sustains ATP in neurons (already mapped) for GABA (already mapped) inhibitory tone; hypoxia amplifies NF-κB (already mapped) and NLRP3 (already mapped) neuroinflammation and substance P (already mapped) sensitisation in fibromyalgia.
- `connects-to` → **[Carbon](../../02-atomic/carbon/README.md)** — FM carbon: carbon, as metabolic backbone of neurotransmitters in neurons (already mapped) and astrocytes (already mapped), drives GABA (already mapped) synthesis; carbon dysregulation amplifies NF-κB (already mapped) and substance P (already mapped) sensitisation in fibromyalgia.
- `connects-to` → **[Chloride](../../02-atomic/chloride/README.md)** — FM chloride: chloride channels in neurons (already mapped) and astrocytes (already mapped) modulate GABA (already mapped) inhibitory tone; chloride dysregulation amplifies NF-κB (already mapped) and substance P (already mapped) sensitisation in fibromyalgia.
- `connects-to` → **[Hydrogen](../../02-atomic/hydrogen/README.md)** — FM hydrogen: hydrogen, via redox homeostasis in microglia (already mapped) and astrocytes (already mapped), quenches neuroinflammatory ROS; hydrogen dysregulation amplifies NF-κB (already mapped) and substance P (already mapped) sensitisation in fibromyalgia.
- `connects-to` → **[PD-1](../../03-molecular/pd-1/README.md)** — FM pd-1: PD-1 on T-cytotoxic cells (already mapped) and microglia (already mapped) suppresses neuroimmune surveillance; pd-1 dysfunction amplifies NF-κB (already mapped) and substance P (already mapped) and IL-6 (already mapped) central sensitisation cascade of fibromyalgia.
- `connects-to` → **[GLP-1](../../03-molecular/glp-1/README.md)** — FM glp-1: GLP-1 from neurons (already mapped) and astrocytes (already mapped) modulates metabolic-neuroinflammatory tone; glp-1 dysfunction amplifies NF-κB (already mapped) and substance P (already mapped) and IL-6 (already mapped) sensitisation cascade of fibromyalgia.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — FM vegf: VEGF from microglia (already mapped) and astrocytes (already mapped) drives neuroinflammatory angiogenesis; vegf dysregulation amplifies NF-κB (already mapped) and substance P (already mapped) and IL-6 (already mapped) central sensitisation cascade of fibromyalgia.

[^wolfe-2016-fibromyalgia-criteria]: Wolfe F, Clauw DJ, Fitzcharles MA, et al. 2016 Revisions to the 2010/2011 fibromyalgia diagnostic criteria. *Semin Arthritis Rheum.* 2016;46(3):319-329. [doi:10.1016/j.semarthrit.2016.08.012](https://doi.org/10.1016/j.semarthrit.2016.08.012) · [PubMed 27916278](https://pubmed.ncbi.nlm.nih.gov/27916278/)
[^clauw-2014-fibromyalgia-review]: Clauw DJ. Fibromyalgia: a clinical review. *JAMA.* 2014;311(15):1547-1555. [doi:10.1001/jama.2014.3266](https://doi.org/10.1001/jama.2014.3266) · [PubMed 24737367](https://pubmed.ncbi.nlm.nih.gov/24737367/)
[^harris-2007-fibromyalgia-dopamine]: Harris RE, Clauw DJ, Scott DJ, et al. Decreased central mu-opioid receptor availability in fibromyalgia. *J Neurosci.* 2007;27(37):10000-10006. [doi:10.1523/JNEUROSCI.2849-07.2007](https://doi.org/10.1523/JNEUROSCI.2849-07.2007) · [PubMed 17855614](https://pubmed.ncbi.nlm.nih.gov/17855614/)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
