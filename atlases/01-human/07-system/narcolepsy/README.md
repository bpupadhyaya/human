---
schema: human-scale-entry/v1
id: narcolepsy
name: Narcolepsy
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-08
summary: "Narcolepsy is a chronic hypersomnia disorder caused by selective loss of orexin (hypocretin) neurons in type 1; HLA-DQB1*06:02 and autoimmune destruction; characterized by EDS, cataplexy, sleep paralysis, and hallucinations. Sodium oxybate, pitolisant, modafinil treat symptoms."
aliases: ["narcolepsy", "narcolepsy type 1", "narcolepsy with cataplexy", "narcolepsy type 2", "hypocretin deficiency", "orexin deficiency", "excessive daytime sleepiness", "cataplexy"]
cross_links:
  - target: 01-human/03-molecular/orexin
    relation: connects-to
    note: "Type 1 narcolepsy results from autoimmune destruction of ~70,000 lateral hypothalamic orexin neurons; CSF hypocretin-1 <110 pg/mL is diagnostic; OX2R agonists (TAK-994) showed anti-narcoleptic efficacy but were halted; OX2R signaling is the fundamental missing signal."
  - target: 01-human/03-molecular/histamine
    relation: connects-to
    note: "Orexin normally drives TMN histamine neurons via OX2R → H1R cortical wakefulness; narcolepsy impairs this axis; pitolisant (H3R inverse agonist, FDA-approved 2019) blocks presynaptic H3R autoreceptors → ↑histamine release → wakefulness; only non-scheduled narcolepsy drug."
  - target: 01-human/03-molecular/dopamine
    relation: connects-to
    note: "Modafinil/armodafinil inhibit DAT → ↑synaptic dopamine → wakefulness (FDA-approved); stimulants (methylphenidate, amphetamines) block/reverse DAT for EDS; REM-off dopaminergic neurons in VTA are dysregulated in narcolepsy contributing to inappropriate REM intrusions."
  - target: 01-human/03-molecular/serotonin
    relation: connects-to
    note: "Antidepressants (SSRIs, SNRIs, clomipramine) suppress cataplexy via serotonin + NE reuptake inhibition that reduces REM muscle atonia; sodium oxybate may also act via serotonergic pathways; 5-HT regulates REM-off neuron activity in the dorsal raphe in narcolepsy."
  - target: 01-human/06-organ/brain
    relation: targets
    note: "Narcolepsy specifically destroys lateral hypothalamic orexin neurons → destabilizes the VLPO-arousal center flip-flop switch; TMN histamine, LC norepinephrine, and raphe serotonin projections are all impaired; pontine REM-on/off circuit dysregulation underlies cataplexy."
  - target: 01-human/03-molecular/bdnf
    relation: connects-to
    note: "BDNF supports survival and function of hypothalamic orexin neurons via TrkB; BDNF Val66Met SNP may influence orexin neuron vulnerability; aerobic exercise increases BDNF and modestly reduces EDS in narcolepsy patients; BDNF-TrkB pathway is a potential neuroprotective target."
  - target: 01-human/03-molecular/melatonin
    relation: connects-to
    note: "Melatonin timing is disrupted in narcolepsy type 1 due to orexin neuron loss and sleep-wake switch instability; circadian-timed melatonin modestly improves sleep consolidation; MT1/MT2 agonists (ramelteon) are used adjunctively for circadian realignment."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Type 1 narcolepsy is autoimmune: in HLA-DQB1*06:02 carriers, autoreactive CD8+ and CD4+ T cells destroy the ~70,000 hypothalamic orexin neurons, abolishing the orexin signal that stabilizes wakefulness — strong evidence that a T-cell attack, not neurodegeneration, causes it."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "Narcolepsy type 1 comes down to loss of one tiny neuron population: the ~70,000 orexin (hypocretin) neurons of the lateral hypothalamus, whose destruction collapses the switch holding wakefulness stable — causing sleep attacks, cataplexy, and REM intrusion into wakefulness."
  - target: 01-human/07-system/influenza
    relation: connects-to
    note: "Narcolepsy is famously linked to influenza: the 2009 H1N1 pandemic and Pandemrix vaccine both raised type 1 narcolepsy incidence in HLA-DQB1*06:02 carriers, apparently via molecular mimicry between an H1N1 hemagglutinin epitope and orexin — infection-triggered autoimmunity."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: connects-to
    note: "Type 1 narcolepsy is an autoimmune disease where tolerance fails: on an HLA-DQB1*06:02 background, autoreactive T cells escape regulatory-T-cell control and destroy hypothalamic orexin neurons, abolishing the orexin that stabilizes wakefulness and REM gating."
  - target: 01-human/07-system/obesity
    relation: connects-to
    note: "Narcolepsy and obesity are metabolically linked: loss of orexin, which normally promotes energy expenditure and activity, leaves many narcolepsy patients prone to weight gain and a higher BMI despite reduced appetite—an early clue, especially in children near onset."
  - target: 01-human/04-cellular/microglia
    relation: connects-to
    note: "Microglia may participate in the orexin-neuron loss of narcolepsy: as the brain's resident immune cells, activated microglia present antigen and clear neurons, and neuroinflammation in the lateral hypothalamus is implicated in the autoimmune destruction of orexin signaling."
  - target: 01-human/07-system/type-1-diabetes
    relation: connects-to
    note: "Narcolepsy type 1 and type 1 diabetes are both autoimmune diseases that destroy a specific cell population: narcolepsy loses the hypothalamic orexin neurons, T1DM the pancreatic β-cells—each tied to HLA risk alleles and likely T-cell-mediated."
  - target: 01-human/07-system/multiple-sclerosis
    relation: connects-to
    note: "Narcolepsy and multiple sclerosis are both immune-mediated CNS disorders: MS demyelinates white matter, and lesions in the hypothalamus can even cause secondary narcolepsy by destroying orexin pathways—linking an autoimmune brain disease to a sleep disorder."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "Narcolepsy and depression overlap clinically and are easily confused: the daytime sleepiness and low energy of narcolepsy mimic depression, the two frequently coexist, and some antidepressants suppress cataplexy—so screening for mood disorder is part of narcolepsy care."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "Narcolepsy type 1 is an autoimmune disease: T cells, in genetically susceptible (HLA-DQB1*06:02) people often after H1N1 infection or vaccination, destroy the brain's orexin neurons—so a sleep disorder traces to immune attack on a tiny hypothalamic cell population."
  - target: 01-human/03-molecular/acetylcholine
    relation: connects-to
    note: "Acetylcholine drives the REM intrusions of narcolepsy: losing orexin unleashes cholinergic REM-on circuits, so REM phenomena—dream sleep, atonia—break into wakefulness as cataplexy and sleep paralysis, the hallmark symptoms beyond sleepiness."
  - target: 01-human/07-system/insomnia-disorder
    relation: connects-to
    note: "Narcolepsy and insomnia are opposite faces of dysregulated sleep: narcolepsy floods wake with sleep (and fragments night sleep too), while insomnia fails to initiate it—yet both disrupt the orexin/circadian machinery that stabilizes the sleep-wake switch."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "Narcolepsy is a focal nervous-system disorder of sleep-wake control: selective loss of ~70,000 orexin (hypocretin) neurons in the hypothalamus destabilizes the boundaries between wake, REM and sleep, so REM intrudes into wakefulness as cataplexy and sleep attacks."
  - target: 02-pathogen/02-bacteria/streptococcus-pyogenes
    relation: connects-to
    note: "Streptococcal infection is a recognized trigger of type 1 narcolepsy: along with H1N1 influenza and its vaccine, strep can precipitate the autoimmune attack on orexin neurons in genetically susceptible (HLA-DQB1*06:02) people—molecular mimicry turned against sleep."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "Narcolepsy carries cardiovascular risk: disrupted sleep and loss of normal nocturnal blood-pressure dipping raise the risk of hypertension and heart disease, and stimulant treatments add cardiac considerations—so the sleep disorder has whole-body consequences."
  - target: 01-human/03-molecular/mhc-class-ii
    relation: connects-to
    note: "Narcolepsy type 1 is almost always HLA-DQB1*06:02 positive: this MHC class II variant presents orexin-related peptides to T cells, the strongest genetic clue that the disease is an autoimmune attack destroying the brain's orexin neurons."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "Autoreactive T-helper cells appear central to narcolepsy: CD4 T cells recognizing orexin (with cytotoxic T cells) are thought to drive destruction of the hypothalamic orexin neurons, explaining why the disease follows certain infections and vaccinations."
  - target: 01-human/03-molecular/norepinephrine
    relation: connects-to
    note: "Orexin normally props up norepinephrine-driven wakefulness: losing orexin neurons leaves the noradrenergic system unstable, so wake states collapse into sleep and—during cataplexy—the locus coeruleus falls silent, releasing muscle tone."
  - target: 01-human/03-molecular/gaba
    relation: connects-to
    note: "Narcolepsy's cataplexy is tamed through GABA: sodium oxybate, a GABA-B agonist taken at night, consolidates fragmented sleep and sharply reduces cataplexy—the most effective drug for the disorder, working on the brain's main inhibitory system."
  - target: 01-human/03-molecular/adenosine
    relation: connects-to
    note: "Narcolepsy collides with the brain's sleep-pressure signal, adenosine: this molecule accumulates to drive sleepiness, and caffeine—an adenosine blocker—is the everyday self-treatment patients reach for against overwhelming daytime sleep."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "Narcolepsy may begin when dendritic cells present a flu look-alike: after H1N1 infection or vaccination, these antigen-presenters can display peptides mimicking orexin, priming T cells that then destroy the orexin neurons—a molecular-mimicry origin."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "Sodium oxybate is a mainstay narcolepsy drug: the sodium salt of GHB, taken at night, consolidates deep sleep and sharply reduces cataplexy and daytime sleepiness, though its sodium load is a reason newer low-sodium versions were developed."
  - target: 01-human/05-tissue/synapse
    relation: connects-to
    note: "Narcolepsy is a disease of lost wake-promoting synapses: destruction of the orexin neurons strips the brain of their stabilizing input to arousal circuits, so the synaptic switch between sleep and wake becomes unstable, intruding REM into waking life."
  - target: 01-human/04-cellular/astrocyte
    relation: connects-to
    note: "Astrocytes shape the sleep pressure narcolepsy disrupts: they release adenosine and regulate the orexin circuit's environment, so glial support of the wake-sleep system is part of the biology surrounding the orexin-neuron loss."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "Narcolepsy is hard on the heart: fragmented sleep and blunted nighttime blood-pressure dipping, with the autonomic swings of REM intrusion, raise long-term cardiovascular risk in these patients."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Light still helps steady narcolepsy's broken sleep-wake switch: photons reaching the retina reinforce the circadian arousal signal, so bright light and good light hygiene support wakefulness alongside medication."
  - target: 01-human/04-cellular/adipocyte
    relation: connects-to
    note: "Narcolepsy tends to add fat: orexin normally curbs appetite and lifts metabolism, so its loss shifts adipocytes toward storage, and weight gain and obesity are common in the disorder."
  - target: 01-human/06-organ/eye
    relation: connects-to
    note: "Narcolepsy lets REM sleep invade the eye while waking: dream imagery as hypnagogic hallucinations, paralysis on waking, and the rapid REM-onset eye movements timed in the multiple sleep latency test that confirms the diagnosis."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Losing orexin scrambles leptin's satiety signal: narcolepsy patients show blunted leptin signaling and gain weight despite eating less, a metabolic paradox tying the wake-promoting peptide to the body's fat-sensing hormone."
  - target: 01-human/03-molecular/glutamate
    relation: connects-to
    note: "Orexin neurons speak in glutamate: they co-release this excitatory transmitter to drive the arousal circuits, so when the orexin cells die the loss of their glutamatergic push helps collapse the boundary between waking and sleep."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Narcolepsy is the loss of a tiny cell population: electron and immuno-microscopy reveal the near-total disappearance of the hypothalamus's few thousand orexin neurons, destroyed in what looks like a targeted autoimmune attack."
  - target: 01-human/05-tissue/peripheral-nerve
    relation: connects-to
    note: "Cataplexy hijacks the body's muscle-tone circuit: the REM atonia that should only paralyze us in dreams intrudes into waking, switching off the motor pathways to peripheral nerves so the knees buckle at a burst of emotion."
  - target: 01-human/06-organ/large-intestine
    relation: connects-to
    note: "Orexin loss ripples into the gut: narcolepsy patients report more constipation and irritable-bowel symptoms, the wake-and-feeding peptide's absence disturbing the autonomic and gut-brain signaling that paces digestion."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "Narcolepsy type 1 looks autoimmune: tied to HLA-DQB1*06:02 and a T-cell attack, it follows H1N1 flu and the Pandemrix vaccine, and antibodies cross-reacting between influenza or streptococcal antigens and orexin neurons are a leading suspect in the molecular mimicry."
  - target: 01-human/06-organ/thyroid
    relation: connects-to
    note: "The thyroid sits in the differential and the company it keeps: hypothyroidism causes its own daytime sleepiness and is checked before narcolepsy is diagnosed, while autoimmune thyroid disease appears more often in these patients, fitting the autoimmune picture."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "In children, orexin loss can hurry puberty: pediatric narcolepsy is associated with precocious puberty and weight gain, the hypothalamic damage that abolishes wakefulness also disturbing the nearby circuits that time sexual maturation."
  - target: 01-human/06-organ/thymus
    relation: connects-to
    note: "Narcolepsy type 1 is an autoimmune disease at heart: orexin neurons are destroyed by a T-cell attack, and the thymus that should delete such self-reactive T cells fails to, a breakdown of central tolerance acting on an HLA-DQB1*06:02 background."
  - target: 01-human/07-system/attention-deficit-hyperactivity-disorder
    relation: connects-to
    note: "Sleepiness can masquerade as inattention: narcolepsy and ADHD overlap heavily, with daytime drowsiness mimicking and worsening attention problems, and both responding to the same wakefulness-promoting stimulants — a link that complicates telling them apart."
  - target: 01-human/04-cellular/b-cell
    relation: connects-to
    note: "Antibodies join the attack on orexin: B cells in narcolepsy produce autoantibodies such as anti-TRIB2, and the post-H1N1-vaccine surge in cases points to a humoral, molecular-mimicry arm alongside the cytotoxic T cells."
  - target: 01-human/07-system/type-2-diabetes
    relation: connects-to
    note: "Losing orexin disturbs metabolism: beyond weight gain, narcolepsy carries a higher rate of insulin resistance and type 2 diabetes, since the orexin system helps regulate glucose and energy balance, not just wakefulness."
  - target: 01-human/07-system/hypertension
    relation: connects-to
    note: "The night-time blood pressure stays high: narcoleptics often lose the normal nocturnal dip in blood pressure, a non-dipping pattern linked to orexin loss and fragmented sleep that adds to their long-term cardiovascular risk."
  - target: 01-human/03-molecular/ghrelin
    relation: connects-to
    note: "Appetite signals run awry: orexin normally integrates the hunger hormone ghrelin with arousal, so its loss in narcolepsy unbalances the appetite-energy axis, contributing to the increased eating and weight gain that accompany the disorder."
  - target: 01-human/03-molecular/tnf-alpha
    relation: connects-to
    note: "Post-infectious inflammation may help trigger it: TNF-α and other cytokines rise after the infections (H1N1, streptococcus) that precede type 1 narcolepsy, part of the immune storm thought to unmask the autoimmune attack on orexin neurons."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "The mind carries the burden of broken sleep: anxiety and depression are markedly more common in narcolepsy, both from the disorder's neurobiology and the strain of unpredictable sleepiness and cataplexy on daily life."
  - target: 01-human/07-system/migraine
    relation: connects-to
    note: "Headache shadows the sleep disorder: migraine occurs more often in people with narcolepsy, the two sharing dysregulation of the hypothalamic and monoaminergic circuits that govern arousal and pain."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "An autoimmune T-cell attack runs on STAT3: type 1 narcolepsy is driven by HLA-restricted, likely Th17-skewed T cells destroying orexin neurons, and STAT3 sits at the heart of that autoreactive T-cell program."
  - target: 01-human/07-system/bipolar-disorder
    relation: connects-to
    note: "Mood disorder rides with the sleepiness: bipolar disorder and depression are over-represented in narcolepsy, the shared dysregulation of sleep, reward and monoamine systems blurring the boundary and complicating treatment."
  - target: 01-human/07-system/panic-disorder
    relation: connects-to
    note: "Sudden sleep phenomena breed fear: the frightening sleep paralysis and hypnagogic hallucinations of narcolepsy, and its disrupted arousal, feed high rates of panic and anxiety disorders."
  - target: 01-human/07-system/schizophrenia
    relation: connects-to
    note: "Its hallucinations can masquerade as psychosis: the vivid hypnagogic hallucinations and dream intrusions of narcolepsy mimic schizophrenia, a diagnostic overlap complicated further by stimulant treatment that can itself provoke psychosis."
  - target: 01-human/07-system/heart-failure
    relation: connects-to
    note: "Disrupted sleep strains the heart: the autonomic dysregulation, obesity and nocturnal sympathetic surges of narcolepsy raise cardiovascular risk, contributing over time to hypertension and heart failure."
  - target: 01-human/07-system/stroke
    relation: connects-to
    note: "Its cardiovascular toll reaches the brain: the metabolic syndrome and autonomic disturbance of narcolepsy are linked to a higher long-term risk of cardiovascular events including stroke."
  - target: 01-human/07-system/binge-eating-disorder
    relation: connects-to
    note: "Orexin loss reshapes appetite: hypocretin-deficient narcolepsy type 1 carries higher BMI and a recognised tendency to binge-eating and disordered eating beyond the weight gain alone."
  - target: 01-human/07-system/epilepsy
    relation: connects-to
    note: "Sudden attacks blur the diagnosis: cataplexy and sleep-onset events of narcolepsy are frequently mistaken for seizures, and the two coexist, so EEG and sleep studies are needed to separate them."
  - target: 01-human/07-system/parkinsons-disease
    relation: connects-to
    note: "Both disorders unsettle REM sleep: narcolepsy's REM intrusion and the REM sleep behavior disorder and hypocretin-neuron loss seen in Parkinson's reflect overlapping dysregulation of sleep-state control."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "Orexin loss unsettles metabolism and hormones: hypocretin/orexin normally governs energy balance and arousal, so its loss in narcolepsy type 1 brings weight gain, metabolic change and, in children, precocious puberty."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "It travels with sleep-disordered breathing: narcolepsy is frequently complicated by comorbid obstructive sleep apnoea, on a background of its associated obesity, fragmenting sleep further."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "Cataplexy drops the body without warning: the sudden emotion-triggered loss of muscle tone in narcolepsy type 1 causes collapses and falls that risk fractures and soft-tissue injury."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "Loss of orexin reshapes appetite and the gut: hypocretin deficiency dysregulates appetite and contributes to weight gain, and sodium oxybate, a mainstay treatment, commonly causes nausea."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "Its drug carries a heavy salt load: sodium oxybate delivers a large daily dose of sodium that affects blood pressure and fluid balance, prompting development of lower-sodium formulations."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "A stimulant can trigger severe rashes: modafinil, used for narcolepsy's daytime sleepiness, carries a warning for serious skin reactions including Stevens-Johnson syndrome."
  - target: 03-medicine/01-modern/10-mental-health/fluoxetine
    relation: connects-to
    note: "SSRIs and SNRIs treat cataplexy: by suppressing REM sleep, antidepressants like fluoxetine reduce the cataplexy, sleep paralysis and hallucinations of narcolepsy."
  - target: 01-human/07-system/stimulant-use-disorder
    relation: connects-to
    note: "Its sleepiness is treated with stimulants: modafinil, methylphenidate and amphetamines promote daytime wakefulness in narcolepsy, linking it to stimulant pharmacology and controlled prescribing."
  - target: 03-medicine/02-traditional/panax-ginseng
    relation: connects-to
    note: "Traditional stimulants are tried for fatigue: ginseng and other adaptogens are used by some for daytime tiredness, though they are no substitute for the established wake-promoting drugs of narcolepsy."
  - target: 02-pathogen/01-viruses/influenza-a
    relation: connects-to
    note: "A pandemic flu that triggered it: the 2009 H1N1 influenza and the Pandemrix vaccine against it sharply raised narcolepsy incidence, the virus's antigens cross-reacting with orexin neurons in genetically susceptible people."
  - target: 01-human/07-system/huntingtons-disease
    relation: connects-to
    note: "Neurodegeneration steals orexin too: Huntington's disease damages hypothalamic orexin neurons, producing the fragmented sleep and daytime sleepiness that overlap with narcolepsy's hallmark orexin loss."
  - target: 01-human/07-system/fibromyalgia
    relation: connects-to
    note: "Unrefreshing sleep links them: narcolepsy and fibromyalgia both disrupt sleep architecture and cause profound daytime fatigue, and the two are more likely to coexist."
  - target: 01-human/07-system/myasthenia-gravis
    relation: connects-to
    note: "Two HLA-linked neuro-autoimmune diseases: type 1 narcolepsy is a T-cell attack on orexin neurons tied to HLA-DQB1*06:02, as myasthenia gravis is an antibody attack on the neuromuscular junction—self-directed immunity striking different neural targets."
  - target: 01-human/07-system/ptsd
    relation: connects-to
    note: "Disordered REM connects them: narcolepsy intrudes REM sleep into wakefulness, while PTSD fragments REM with nightmares; the two are comorbid and share noradrenergic and orexin dysregulation of the sleep-wake switch."
  - target: 01-human/05-tissue/guillain-barre
    relation: connects-to
    note: "Both can follow an infection: narcolepsy surged after H1N1 influenza and Pandemrix vaccination, and Guillain-Barré syndrome classically follows infection too—post-infectious autoimmunity by molecular mimicry striking the nervous system."
  - target: 01-human/07-system/gambling-disorder
    relation: connects-to
    note: "Stimulant-linked impulse control: the dopaminergic stimulants treating narcolepsy can unmask impulse-control behaviours such as pathological gambling, a reward-circuit overlap between the two conditions."
  - target: 01-human/05-tissue/cardiac-conduction-system
    relation: connects-to
    note: "Cardiovascular load of treatment: narcolepsy carries raised cardiovascular risk, and its stimulant treatments (modafinil, amphetamines) raise heart rate and blood pressure and can affect cardiac conduction."
  - target: 01-human/07-system/lewy-body-dementia
    relation: connects-to
    note: "Orexin and sleep across disorders: orexin loss causes narcolepsy's cataplexy and sleep instability, while synucleinopathies like Lewy body dementia disrupt orexin signalling and REM sleep in their own way."
sources:
  - id: scammell-2015-narcolepsy-review
    type: peer-reviewed
    cite: "Scammell TE. Narcolepsy. N Engl J Med. 2015;373(27):2654-2662."
    doi: "10.1056/NEJMra1500587"
    pmid: "26716917"
    url: "https://doi.org/10.1056/NEJMra1500587"
    accessed: "2026-06-08"
  - id: dauvilliers-2007-narcolepsy-clinical
    type: peer-reviewed
    cite: "Dauvilliers Y, Arnulf I, Mignot E. Narcolepsy with cataplexy. Lancet. 2007;369(9560):499-511."
    doi: "10.1016/S0140-6736(07)60237-2"
    pmid: "17292770"
    url: "https://doi.org/10.1016/S0140-6736(07)60237-2"
    accessed: "2026-06-08"
  - id: szakacs-2023-pitolisant-narcolepsy
    type: peer-reviewed
    cite: "Szakacs Z, Dauvilliers Y, Mikhaylov V, et al. Safety and efficacy of pitolisant on cataplexy in patients with narcolepsy: a randomised, double-blind, placebo-controlled trial. Lancet Neurol. 2017;16(3):200-207."
    doi: "10.1016/S1474-4422(16)30333-7"
    pmid: "28129985"
    url: "https://doi.org/10.1016/S1474-4422(16)30333-7"
    accessed: "2026-06-08"
---

# Narcolepsy

## Overview

**Narcolepsy** is a chronic neurological sleep disorder characterized by **excessive daytime sleepiness (EDS)** — the defining and most impairing symptom — alongside distinctive REM-sleep intrusion phenomena: cataplexy, hypnagogic/hypnopompic hallucinations, and sleep paralysis. Together these are called the **narcolepsy tetrad**.

**Classification:**
- **Type 1 (Narcolepsy with Cataplexy; NT1):** Caused by selective autoimmune destruction of ~70,000 lateral hypothalamic orexin (hypocretin) neurons. Diagnostic: CSF hypocretin-1 <110 pg/mL OR typical cataplexy + sleep-onset REM periods (SOREMPs). Nearly all NT1 patients carry HLA-DQB1*06:02 (98% prevalence vs. ~22% in general population).
- **Type 2 (Narcolepsy without Cataplexy; NT2):** EDS with SOREMPs but normal or intermediate CSF hypocretin-1 (>110 pg/mL); HLA-DQB1*06:02 association weaker; pathophysiology less well characterized; some patients evolve to NT1 over time.

**Epidemiology:**
- Prevalence: ~1 in 2,000 (0.05%) in the US and Europe; approximately 200,000 Americans affected
- Onset: typically peaks in adolescence (15–25 years) and has a secondary peak at 35–45 years
- Significant diagnostic delay: median 10 years between symptom onset and diagnosis [^scammell-2015-narcolepsy-review]
- Equal sex distribution in NT1; slight female predominance in NT2
- Associated comorbidities: obesity (BMI often elevated despite normal food intake — leptin resistance may contribute), type 2 diabetes, REM sleep behavior disorder, depression, ADHD

**Autoimmune mechanism in NT1:**
- Strong HLA association (DQB1*06:02/DQA1*01:02) implicates CD4⁺/CD8⁺ T-cell-mediated attack on orexin neurons
- Environmental triggers identified: H1N1 influenza infection and H1N1 Pandemrix vaccination (Europe, 2009-10) produced a sharp narcolepsy incidence spike — 6–13-fold increased risk in vaccinated European children carrying HLA-DQB1*06:02
- Molecular mimicry: viral or vaccine antigens share epitopes with orexin neurons — triggering autoreactive T cells that destroy orexin-containing neurons specifically while sparing neighboring cell types

## Structure

### The orexin system and narcolepsy

Lateral hypothalamic orexin neurons project broadly to all major arousal centers [^scammell-2015-narcolepsy-review]:
- **LC (norepinephrine):** OX2R → NE → cortical arousal
- **TMN (histamine):** OX2R → histamine H1 → wakefulness (the most important single pathway for sustained wakefulness)
- **Raphe (serotonin):** OX1/2R → 5-HT → wakefulness and REM suppression
- **Basal forebrain (acetylcholine):** OX1/2R → ACh → cortical desynchronization
- **VTA (dopamine):** OX1R → DA → reward and arousal
- **Spinal cord motor neurons:** OX1/2R → maintain motor tone during wakefulness

Loss of orexin signaling destabilizes the **VLPO-arousal center bistable flip-flop switch** — which normally exists in two stable states (wake or sleep) with sharp transitions. Without orexin reinforcing the wake state, the switch flickers: patients experience involuntary sleep attacks (wake→NREM) and REM intrusions (wake→REM) — the neurobiological basis of EDS, sleep attacks, and cataplexy.

### Sleep architecture in narcolepsy

| Feature | Normal | Narcolepsy type 1 |
|:---|:---|:---|
| Sleep onset latency | >10 min | <8 min (often <5 min) |
| REM latency | 90–110 min | <15 min (SOREMP) — pathognomonic |
| SOREMPs (sleep studies) | 0–1 | ≥2 (MSLT criterion) |
| Nocturnal sleep architecture | Normal | Fragmented; intrusions of wakefulness |
| REM density | Normal | Elevated; vivid dreams |

**Multiple Sleep Latency Test (MSLT):** Gold-standard objective test — measures time to sleep onset in 5 nap opportunities (every 2 hours) after overnight polysomnography. Criteria for narcolepsy: mean sleep latency ≤8 minutes AND ≥2 sleep-onset REM periods (SOREMPs).

### Cataplexy

Cataplexy is the **pathognomonic** feature of NT1 — sudden, bilateral loss of voluntary muscle tone triggered by strong positive emotions (laughter, surprise, excitement, elation). It is caused by intrusion of REM sleep atonia circuits into wakefulness:
- Emotion → limbic → amygdala/cingulate activation → directly activates pontine REM-on circuits (REM-promoting neurons in sublateral dorsal nucleus) in the absence of orexin's restraint
- Amygdala → activates spinal glycinergic/GABAergic interneurons → hyperpolarizes ventral horn motor neurons → flaccid paralysis
- Consciousness is preserved during cataplexy (differentiating it from seizures and syncope)
- Duration: seconds to 2 minutes; partial cataplexy (facial muscles, jaw, knees) is more common than complete collapse
- Trigger specificity: highly specific to positive emotion in NT1; anger/fear can also trigger in some patients

## Function

### Pathophysiology of symptoms

| Symptom | Mechanism |
|:---|:---|
| **EDS** | Loss of orexin → impaired arousal center drive → failure to sustain wakefulness; TMN histamine deficiency plays primary role |
| **Cataplexy** | Emotional activation of amygdala → direct pontine REM-on circuit activation without orexin restraint → REM atonia during wakefulness |
| **Sleep paralysis** | Brief continuation of REM atonia after awakening — dissociated REM state; normal population also experiences this occasionally |
| **Hypnagogic hallucinations** | Vivid, often frightening dream imagery during sleep-onset/offset transitions when consciousness and REM dreaming overlap |
| **Fragmented nocturnal sleep** | Unstable VLPO-arousal switch → awakening during the night; insufficient restorative sleep contributes to daytime EDS |

## Pathology

### Diagnosis

**Polysomnography + MSLT (gold standard):**
- Overnight PSG rules out other causes of EDS (obstructive sleep apnea — the most common EDS mimic) and establishes sleep architecture
- MSLT the next day: ≥2 SOREMPs + mean sleep latency ≤8 minutes
- Note: SSRIs/SNRIs suppress REM and must be withdrawn ≥2 weeks before MSLT to avoid false-negative SOREMPs

**CSF hypocretin-1 measurement:**
- <110 pg/mL (or <1/3 of mean normal values) = highly specific for NT1 (sensitivity ~90%, specificity ~99%)
- Requires lumbar puncture; used when MSLT is inconclusive or to confirm NT1 definitively
- Undetectable in ~90% of NT1; normal in NT2

**HLA typing:** DQB1*06:02 has high sensitivity (98%) but poor specificity (~22% of general population carry it); used as supporting evidence, not diagnostic

### Treatment

**Excessive daytime sleepiness:**
- **Sodium oxybate (GHB; Xyrem):** FDA-approved for both EDS and cataplexy (2002); consolidates nocturnal sleep → reduces EDS; mechanism: GABA-B agonist → consolidates slow-wave sleep → reduces fragmentation; second dose given 2.5-4 hours after sleep onset; schedule III; abuse potential but rare in narcolepsy context; contraindicated with CNS depressants or respiratory insufficiency; low sodium formulation (Lumryz, QD dosing) FDA-approved 2023
- **Modafinil/Armodafinil (Provigil/Nuvigil):** First-line wakefulness promoters; exact mechanism debated — primarily DAT inhibition → ↑synaptic dopamine; schedule IV; no significant peripheral sympathomimetic effects; well-tolerated [^scammell-2015-narcolepsy-review]
- **Traditional stimulants (methylphenidate, amphetamine salts):** Used for refractory EDS; schedule II; effective but higher abuse potential and cardiovascular effects; still widely prescribed due to cost advantage
- **Pitolisant (Wakix):** H3R inverse agonist — blocks presynaptic histamine autoreceptors → ↑histamine release → wakefulness; FDA-approved 2019 for EDS and 2020 for cataplexy; non-scheduled (not a controlled substance) — unique among narcolepsy treatments; allows patients to work or hold certain occupations denied to scheduled-drug users [^szakacs-2023-pitolisant-narcolepsy]

**Cataplexy:**
- **Sodium oxybate:** Most effective treatment; dramatically reduces cataplexy frequency in most patients
- **Antidepressants (SSRIs, SNRIs, clomipramine, venlafaxine):** Suppress cataplexy via serotonin/NE reuptake inhibition → suppress pontine REM-on circuits; used at sub-antidepressant doses; must be tapered not stopped abruptly (sudden discontinuation can cause severe status cataplecticus — continuous cataplexy)
- **Pitolisant:** FDA-approved for cataplexy (2020) — only non-scheduled medication for both EDS and cataplexy

**Emerging treatments:**
- **OX2R agonists:** TAK-994 (oral OX2R agonist) dramatically reduced narcolepsy symptoms in Phase 2 but halted due to liver toxicity; next-generation OX2R agonists (TAK-861) in trials without hepatotoxicity signal
- **Immunotherapy at onset:** Case reports of IV Ig, rituximab, or corticosteroids given acutely during orexin neuron destruction phase; animal data supports the concept but no controlled trials

## Connections

- `connects-to` → **[Orexin](../../../03-molecular/orexin/README.md)** — type 1 narcolepsy results from selective autoimmune destruction of ~70,000 lateral hypothalamic orexin neurons; CSF hypocretin-1 <110 pg/mL is diagnostic; loss of orexin destabilizes the VLPO-arousal center flip-flop switch → EDS, cataplexy, and REM intrusions; OX2R agonists (TAK-861) are in clinical trials.

- `connects-to` → **[Histamine](../../../03-molecular/histamine/README.md)** — orexin normally drives TMN histamine neurons via OX2R, and histamine H1R activation sustains cortical wakefulness; narcolepsy disrupts this orexin-histamine axis; pitolisant (H3R inverse agonist, FDA-approved 2019 for EDS; 2020 for cataplexy) blocks histamine autoreceptors → ↑histamine release → wakefulness; it is the only non-controlled narcolepsy medication.

- `connects-to` → **[Dopamine](../../../03-molecular/dopamine/README.md)** — modafinil and armodafinil inhibit DAT → ↑synaptic dopamine → sustained wakefulness (first-line EDS treatment); methylphenidate and amphetamines also target DAT for refractory EDS; REM-off dopaminergic neurons in VTA are dysregulated in narcolepsy contributing to inappropriate REM sleep intrusions during wakefulness.

- `connects-to` → **[Serotonin](../../../03-molecular/serotonin/README.md)** — SSRIs and SNRIs (venlafaxine, fluoxetine) suppress cataplexy via monoamine reuptake inhibition reducing pontine REM-on circuit activity; clomipramine (TCA, potent SERT inhibitor) is highly effective for cataplexy; sodium oxybate may act partly via serotonergic consolidation of slow-wave sleep.

- `targets` → **[Brain](../../../06-organ/brain/README.md)** — NT1 selectively destroys lateral hypothalamic orexin neurons, destabilizing the VLPO-arousal flip-flop switch; downstream TMN histamine, LC norepinephrine, raphe serotonin, and VTA dopamine arousal centers are all under-driven; pontine REM-on/off circuit dysregulation underlies cataplexy.

- `connects-to` → **[BDNF](../../../03-molecular/bdnf/README.md)** — BDNF supports survival and function of hypothalamic orexin neurons via TrkB; BDNF Val66Met SNP may influence orexin neuron vulnerability; aerobic exercise increases BDNF and modestly reduces daytime sleepiness in narcolepsy; BDNF-TrkB is a potential neuroprotective target in early narcolepsy.

- `connects-to` → **[Melatonin](../../../03-molecular/melatonin/README.md)** — melatonin secretion timing is disrupted in narcolepsy type 1 due to orexin neuron loss destabilizing the sleep-wake switch and fragmenting nocturnal sleep architecture; circadian-timed melatonin (0.5–3 mg, 1 h before target sleep time) modestly improves sleep consolidation; MT1/MT2 agonists such as ramelteon are used adjunctively for circadian realignment in narcolepsy.

- `connects-to` → **[Cytotoxic T Cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Type 1 narcolepsy is autoimmune: in HLA-DQB1*06:02 carriers, autoreactive CD8+ and CD4+ T cells destroy the ~70,000 hypothalamic orexin neurons, abolishing the orexin signal that stabilizes wakefulness — strong evidence that a T-cell attack, not neurodegeneration, causes it.

- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — Narcolepsy type 1 comes down to loss of one tiny neuron population: the ~70,000 orexin (hypocretin) neurons of the lateral hypothalamus, whose destruction collapses the switch holding wakefulness stable — causing sleep attacks, cataplexy, and REM intrusion into wakefulness.

- `connects-to` → **[Influenza](../influenza/README.md)** — Narcolepsy is famously linked to influenza: the 2009 H1N1 pandemic and Pandemrix vaccine both raised type 1 narcolepsy incidence in HLA-DQB1*06:02 carriers, apparently via molecular mimicry between an H1N1 hemagglutinin epitope and orexin — infection-triggered autoimmunity.
- `connects-to` → **[Regulatory T Cell](../../04-cellular/regulatory-t-cell/README.md)** — Type 1 narcolepsy is an autoimmune disease where tolerance fails: on an HLA-DQB1*06:02 background, autoreactive T cells escape regulatory-T-cell control and destroy hypothalamic orexin neurons, abolishing the orexin that stabilizes wakefulness and REM gating.
- `connects-to` → **[Obesity](../obesity/README.md)** — Narcolepsy and obesity are metabolically linked: loss of orexin, which normally promotes energy expenditure and activity, leaves many narcolepsy patients prone to weight gain and a higher BMI despite reduced appetite—an early clue, especially in children near onset.
- `connects-to` → **[Microglia](../../04-cellular/microglia/README.md)** — Microglia may participate in the orexin-neuron loss of narcolepsy: as the brain's resident immune cells, activated microglia present antigen and clear neurons, and neuroinflammation in the lateral hypothalamus is implicated in the autoimmune destruction of orexin signaling.
- `connects-to` → **[Type 1 Diabetes](../type-1-diabetes/README.md)** — Narcolepsy type 1 and type 1 diabetes are both autoimmune diseases that destroy a specific cell population: narcolepsy loses the hypothalamic orexin neurons, T1DM the pancreatic β-cells—each tied to HLA risk alleles and likely T-cell-mediated.
- `connects-to` → **[Multiple Sclerosis](../multiple-sclerosis/README.md)** — Narcolepsy and multiple sclerosis are both immune-mediated CNS disorders: MS demyelinates white matter, and lesions in the hypothalamus can even cause secondary narcolepsy by destroying orexin pathways—linking an autoimmune brain disease to a sleep disorder.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — Narcolepsy and depression overlap clinically and are easily confused: the daytime sleepiness and low energy of narcolepsy mimic depression, the two frequently coexist, and some antidepressants suppress cataplexy—so screening for mood disorder is part of narcolepsy care.
- `connects-to` → **[Immune System](../immune-system/README.md)** — Narcolepsy type 1 is an autoimmune disease: T cells, in genetically susceptible (HLA-DQB1*06:02) people often after H1N1 infection or vaccination, destroy the brain's orexin neurons—so a sleep disorder traces to immune attack on a tiny hypothalamic cell population.
- `connects-to` → **[Acetylcholine](../../03-molecular/acetylcholine/README.md)** — Acetylcholine drives the REM intrusions of narcolepsy: losing orexin unleashes cholinergic REM-on circuits, so REM phenomena—dream sleep, atonia—break into wakefulness as cataplexy and sleep paralysis, the hallmark symptoms beyond sleepiness.
- `connects-to` → **[Insomnia Disorder](../insomnia-disorder/README.md)** — Narcolepsy and insomnia are opposite faces of dysregulated sleep: narcolepsy floods wake with sleep (and fragments night sleep too), while insomnia fails to initiate it—yet both disrupt the orexin/circadian machinery that stabilizes the sleep-wake switch.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — Narcolepsy is a focal nervous-system disorder of sleep-wake control: selective loss of ~70,000 orexin (hypocretin) neurons in the hypothalamus destabilizes the boundaries between wake, REM and sleep, so REM intrudes into wakefulness as cataplexy and sleep attacks.
- `connects-to` → **[Streptococcus pyogenes](../../../02-pathogen/02-bacteria/streptococcus-pyogenes/README.md)** — Streptococcal infection is a recognized trigger of type 1 narcolepsy: along with H1N1 influenza and its vaccine, strep can precipitate the autoimmune attack on orexin neurons in genetically susceptible (HLA-DQB1*06:02) people—molecular mimicry turned against sleep.
- `connects-to` → **[Cardiovascular system](../cardiovascular-system/README.md)** — Narcolepsy carries cardiovascular risk: disrupted sleep and loss of normal nocturnal blood-pressure dipping raise the risk of hypertension and heart disease, and stimulant treatments add cardiac considerations—so the sleep disorder has whole-body consequences.
- `connects-to` → **[MHC Class II](../../03-molecular/mhc-class-ii/README.md)** — Narcolepsy type 1 is almost always HLA-DQB1*06:02 positive: this MHC class II variant presents orexin-related peptides to T cells, the strongest genetic clue that the disease is an autoimmune attack destroying the brain's orexin neurons.
- `connects-to` → **[T Helper Cell](../../04-cellular/t-helper-cell/README.md)** — Autoreactive T-helper cells appear central to narcolepsy: CD4 T cells recognizing orexin (with cytotoxic T cells) are thought to drive destruction of the hypothalamic orexin neurons, explaining why the disease follows certain infections and vaccinations.
- `connects-to` → **[Norepinephrine](../../03-molecular/norepinephrine/README.md)** — Orexin normally props up norepinephrine-driven wakefulness: losing orexin neurons leaves the noradrenergic system unstable, so wake states collapse into sleep and—during cataplexy—the locus coeruleus falls silent, releasing muscle tone.
- `connects-to` → **[GABA](../../03-molecular/gaba/README.md)** — Narcolepsy's cataplexy is tamed through GABA: sodium oxybate, a GABA-B agonist taken at night, consolidates fragmented sleep and sharply reduces cataplexy—the most effective drug for the disorder, working on the brain's main inhibitory system.
- `connects-to` → **[Adenosine](../../03-molecular/adenosine/README.md)** — Narcolepsy collides with the brain's sleep-pressure signal, adenosine: this molecule accumulates to drive sleepiness, and caffeine—an adenosine blocker—is the everyday self-treatment patients reach for against overwhelming daytime sleep.
- `connects-to` → **[Dendritic Cell](../../04-cellular/dendritic-cell/README.md)** — Narcolepsy may begin when dendritic cells present a flu look-alike: after H1N1 infection or vaccination, these antigen-presenters can display peptides mimicking orexin, priming T cells that then destroy the orexin neurons—a molecular-mimicry origin.
- `connects-to` → **[Sodium](../../02-atomic/sodium/README.md)** — Sodium oxybate is a mainstay narcolepsy drug: the sodium salt of GHB, taken at night, consolidates deep sleep and sharply reduces cataplexy and daytime sleepiness, though its sodium load is a reason newer low-sodium versions were developed.
- `connects-to` → **[Synapse](../../05-tissue/synapse/README.md)** — Narcolepsy is a disease of lost wake-promoting synapses: destruction of the orexin neurons strips the brain of their stabilizing input to arousal circuits, so the synaptic switch between sleep and wake becomes unstable, intruding REM into waking life.
- `connects-to` → **[Astrocyte](../../04-cellular/astrocyte/README.md)** — Astrocytes shape the sleep pressure narcolepsy disrupts: they release adenosine and regulate the orexin circuit's environment, so glial support of the wake-sleep system is part of the biology surrounding the orexin-neuron loss.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — Narcolepsy is hard on the heart: fragmented sleep and blunted nighttime blood-pressure dipping, with the autonomic swings of REM intrusion, raise long-term cardiovascular risk in these patients.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Light still helps steady narcolepsy's broken sleep-wake switch: photons reaching the retina reinforce the circadian arousal signal, so bright light and good light hygiene support wakefulness alongside medication.
- `connects-to` → **[Adipocyte](../../04-cellular/adipocyte/README.md)** — Narcolepsy tends to add fat: orexin normally curbs appetite and lifts metabolism, so its loss shifts adipocytes toward storage, and weight gain and obesity are common in the disorder.
- `connects-to` → **[Eye](../../06-organ/eye/README.md)** — Narcolepsy lets REM sleep invade the eye while waking: dream imagery as hypnagogic hallucinations, paralysis on waking, and the rapid REM-onset eye movements timed in the multiple sleep latency test that confirms the diagnosis.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Losing orexin scrambles leptin's satiety signal: narcolepsy patients show blunted leptin signaling and gain weight despite eating less, a metabolic paradox tying the wake-promoting peptide to the body's fat-sensing hormone.
- `connects-to` → **[Glutamate](../../03-molecular/glutamate/README.md)** — Orexin neurons speak in glutamate: they co-release this excitatory transmitter to drive the arousal circuits, so when the orexin cells die the loss of their glutamatergic push helps collapse the boundary between waking and sleep.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Narcolepsy is the loss of a tiny cell population: electron and immuno-microscopy reveal the near-total disappearance of the hypothalamus's few thousand orexin neurons, destroyed in what looks like a targeted autoimmune attack.
- `connects-to` → **[Peripheral Nerve](../../05-tissue/peripheral-nerve/README.md)** — Cataplexy hijacks the body's muscle-tone circuit: the REM atonia that should only paralyze us in dreams intrudes into waking, switching off the motor pathways to peripheral nerves so the knees buckle at a burst of emotion.
- `connects-to` → **[Large Intestine](../../06-organ/large-intestine/README.md)** — Orexin loss ripples into the gut: narcolepsy patients report more constipation and irritable-bowel symptoms, the wake-and-feeding peptide's absence disturbing the autonomic and gut-brain signaling that paces digestion.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — Narcolepsy type 1 looks autoimmune: tied to HLA-DQB1*06:02 and a T-cell attack, it follows H1N1 flu and the Pandemrix vaccine, and antibodies cross-reacting between influenza or streptococcal antigens and orexin neurons are a leading suspect in the molecular mimicry.
- `connects-to` → **[Thyroid Gland](../../06-organ/thyroid/README.md)** — The thyroid sits in the differential and the company it keeps: hypothyroidism causes its own daytime sleepiness and is checked before narcolepsy is diagnosed, while autoimmune thyroid disease appears more often in these patients, fitting the autoimmune picture.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — In children, orexin loss can hurry puberty: pediatric narcolepsy is associated with precocious puberty and weight gain, the hypothalamic damage that abolishes wakefulness also disturbing the nearby circuits that time sexual maturation.
- `connects-to` → **[Thymus](../../06-organ/thymus/README.md)** — Narcolepsy type 1 is an autoimmune disease at heart: orexin neurons are destroyed by a T-cell attack, and the thymus that should delete such self-reactive T cells fails to, a breakdown of central tolerance acting on an HLA-DQB1*06:02 background.
- `connects-to` → **[Attention-Deficit/Hyperactivity Disorder](../attention-deficit-hyperactivity-disorder/README.md)** — Sleepiness can masquerade as inattention: narcolepsy and ADHD overlap heavily, with daytime drowsiness mimicking and worsening attention problems, and both responding to the same wakefulness-promoting stimulants — a link that complicates telling them apart.
- `connects-to` → **[B Cell](../../04-cellular/b-cell/README.md)** — Antibodies join the attack on orexin: B cells in narcolepsy produce autoantibodies such as anti-TRIB2, and the post-H1N1-vaccine surge in cases points to a humoral, molecular-mimicry arm alongside the cytotoxic T cells.
- `connects-to` → **[Type 2 Diabetes](../type-2-diabetes/README.md)** — Losing orexin disturbs metabolism: beyond weight gain, narcolepsy carries a higher rate of insulin resistance and type 2 diabetes, since the orexin system helps regulate glucose and energy balance, not just wakefulness.
- `connects-to` → **[Hypertension](../hypertension/README.md)** — The night-time blood pressure stays high: narcoleptics often lose the normal nocturnal dip in blood pressure, a non-dipping pattern linked to orexin loss and fragmented sleep that adds to their long-term cardiovascular risk.
- `connects-to` → **[Ghrelin](../../03-molecular/ghrelin/README.md)** — Appetite signals run awry: orexin normally integrates the hunger hormone ghrelin with arousal, so its loss in narcolepsy unbalances the appetite-energy axis, contributing to the increased eating and weight gain that accompany the disorder.
- `connects-to` → **[TNF-α (Tumor Necrosis Factor-alpha)](../../03-molecular/tnf-alpha/README.md)** — Post-infectious inflammation may help trigger it: TNF-α and other cytokines rise after the infections (H1N1, streptococcus) that precede type 1 narcolepsy, part of the immune storm thought to unmask the autoimmune attack on orexin neurons.
- `connects-to` → **[Generalized Anxiety Disorder](../generalized-anxiety-disorder/README.md)** — The mind carries the burden of broken sleep: anxiety and depression are markedly more common in narcolepsy, both from the disorder's neurobiology and the strain of unpredictable sleepiness and cataplexy on daily life.
- `connects-to` → **[Migraine](../migraine/README.md)** — Headache shadows the sleep disorder: migraine occurs more often in people with narcolepsy, the two sharing dysregulation of the hypothalamic and monoaminergic circuits that govern arousal and pain.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — An autoimmune T-cell attack runs on STAT3: type 1 narcolepsy is driven by HLA-restricted, likely Th17-skewed T cells destroying orexin neurons, and STAT3 sits at the heart of that autoreactive T-cell program.
- `connects-to` → **[Bipolar Disorder](../bipolar-disorder/README.md)** — Mood disorder rides with the sleepiness: bipolar disorder and depression are over-represented in narcolepsy, the shared dysregulation of sleep, reward and monoamine systems blurring the boundary and complicating treatment.
- `connects-to` → **[Panic Disorder](../panic-disorder/README.md)** — Sudden sleep phenomena breed fear: the frightening sleep paralysis and hypnagogic hallucinations of narcolepsy, and its disrupted arousal, feed high rates of panic and anxiety disorders.
- `connects-to` → **[Schizophrenia](../schizophrenia/README.md)** — Its hallucinations can masquerade as psychosis: the vivid hypnagogic hallucinations and dream intrusions of narcolepsy mimic schizophrenia, a diagnostic overlap complicated further by stimulant treatment that can itself provoke psychosis.
- `connects-to` → **[Heart Failure](../heart-failure/README.md)** — Disrupted sleep strains the heart: the autonomic dysregulation, obesity and nocturnal sympathetic surges of narcolepsy raise cardiovascular risk, contributing over time to hypertension and heart failure.
- `connects-to` → **[Stroke](../stroke/README.md)** — Its cardiovascular toll reaches the brain: the metabolic syndrome and autonomic disturbance of narcolepsy are linked to a higher long-term risk of cardiovascular events including stroke.
- `connects-to` → **[Binge-Eating Disorder](../binge-eating-disorder/README.md)** — Orexin loss reshapes appetite: hypocretin-deficient narcolepsy type 1 carries higher BMI and a recognised tendency to binge-eating and disordered eating beyond the weight gain alone.
- `connects-to` → **[Epilepsy](../epilepsy/README.md)** — Sudden attacks blur the diagnosis: cataplexy and sleep-onset events of narcolepsy are frequently mistaken for seizures, and the two coexist, so EEG and sleep studies are needed to separate them.
- `connects-to` → **[Parkinson's Disease](../parkinsons-disease/README.md)** — Both disorders unsettle REM sleep: narcolepsy's REM intrusion and the REM sleep behavior disorder and hypocretin-neuron loss seen in Parkinson's reflect overlapping dysregulation of sleep-state control.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — Orexin loss unsettles metabolism and hormones: hypocretin/orexin normally governs energy balance and arousal, so its loss in narcolepsy type 1 brings weight gain, metabolic change and, in children, precocious puberty.
- `connects-to` → **[Respiratory System](../respiratory-system/README.md)** — It travels with sleep-disordered breathing: narcolepsy is frequently complicated by comorbid obstructive sleep apnoea, on a background of its associated obesity, fragmenting sleep further.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — Cataplexy drops the body without warning: the sudden emotion-triggered loss of muscle tone in narcolepsy type 1 causes collapses and falls that risk fractures and soft-tissue injury.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — Loss of orexin reshapes appetite and the gut: hypocretin deficiency dysregulates appetite and contributes to weight gain, and sodium oxybate, a mainstay treatment, commonly causes nausea.
- `connects-to` → **[Renal System](../renal-system/README.md)** — Its drug carries a heavy salt load: sodium oxybate delivers a large daily dose of sodium that affects blood pressure and fluid balance, prompting development of lower-sodium formulations.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — A stimulant can trigger severe rashes: modafinil, used for narcolepsy's daytime sleepiness, carries a warning for serious skin reactions including Stevens-Johnson syndrome.
- `connects-to` → **[Fluoxetine](../../../03-medicine/01-modern/10-mental-health/fluoxetine/README.md)** — SSRIs and SNRIs treat cataplexy: by suppressing REM sleep, antidepressants like fluoxetine reduce the cataplexy, sleep paralysis and hallucinations of narcolepsy.
- `connects-to` → **[Stimulant Use Disorder](../stimulant-use-disorder/README.md)** — Its sleepiness is treated with stimulants: modafinil, methylphenidate and amphetamines promote daytime wakefulness in narcolepsy, linking it to stimulant pharmacology and controlled prescribing.
- `connects-to` → **[Panax Ginseng](../../../03-medicine/02-traditional/panax-ginseng/README.md)** — Traditional stimulants are tried for fatigue: ginseng and other adaptogens are used by some for daytime tiredness, though they are no substitute for the established wake-promoting drugs of narcolepsy.
- `connects-to` → **[Influenza A](../../../02-pathogen/01-viruses/influenza-a/README.md)** — A pandemic flu that triggered it: the 2009 H1N1 influenza and the Pandemrix vaccine against it sharply raised narcolepsy incidence, the virus's antigens cross-reacting with orexin neurons in genetically susceptible people.
- `connects-to` → **[Huntington's Disease](../huntingtons-disease/README.md)** — Neurodegeneration steals orexin too: Huntington's disease damages hypothalamic orexin neurons, producing the fragmented sleep and daytime sleepiness that overlap with narcolepsy's hallmark orexin loss.
- `connects-to` → **[Fibromyalgia](../fibromyalgia/README.md)** — Unrefreshing sleep links them: narcolepsy and fibromyalgia both disrupt sleep architecture and cause profound daytime fatigue, and the two are more likely to coexist.
- `connects-to` → **[Myasthenia Gravis](../myasthenia-gravis/README.md)** — Two HLA-linked neuro-autoimmune diseases: type 1 narcolepsy is a T-cell attack on orexin neurons tied to HLA-DQB1*06:02, as myasthenia gravis is an antibody attack on the neuromuscular junction—self-directed immunity striking different neural targets.
- `connects-to` → **[PTSD](../ptsd/README.md)** — Disordered REM connects them: narcolepsy intrudes REM sleep into wakefulness, while PTSD fragments REM with nightmares; the two are comorbid and share noradrenergic and orexin dysregulation of the sleep-wake switch.
- `connects-to` → **[Guillain-Barré](../../05-tissue/guillain-barre/README.md)** — Both can follow an infection: narcolepsy surged after H1N1 influenza and Pandemrix vaccination, and Guillain-Barré syndrome classically follows infection too—post-infectious autoimmunity by molecular mimicry striking the nervous system.
- `connects-to` → **[Gambling Disorder](../gambling-disorder/README.md)** — Stimulant-linked impulse control: the dopaminergic stimulants treating narcolepsy can unmask impulse-control behaviours such as pathological gambling, a reward-circuit overlap between the two conditions.
- `connects-to` → **[Cardiac Conduction System](../../05-tissue/cardiac-conduction-system/README.md)** — Cardiovascular load of treatment: narcolepsy carries raised cardiovascular risk, and its stimulant treatments (modafinil, amphetamines) raise heart rate and blood pressure and can affect cardiac conduction.
- `connects-to` → **[Lewy Body Dementia](../lewy-body-dementia/README.md)** — Orexin and sleep across disorders: orexin loss causes narcolepsy's cataplexy and sleep instability, while synucleinopathies like Lewy body dementia disrupt orexin signalling and REM sleep in their own way.

[^scammell-2015-narcolepsy-review]: Scammell TE. Narcolepsy. *N Engl J Med.* 2015;373(27):2654-2662. [doi:10.1056/NEJMra1500587](https://doi.org/10.1056/NEJMra1500587) · [PubMed 26716917](https://pubmed.ncbi.nlm.nih.gov/26716917/)
[^dauvilliers-2007-narcolepsy-clinical]: Dauvilliers Y, Arnulf I, Mignot E. Narcolepsy with cataplexy. *Lancet.* 2007;369(9560):499-511. [doi:10.1016/S0140-6736(07)60237-2](https://doi.org/10.1016/S0140-6736(07)60237-2) · [PubMed 17292770](https://pubmed.ncbi.nlm.nih.gov/17292770/)
[^szakacs-2023-pitolisant-narcolepsy]: Szakacs Z, Dauvilliers Y, Mikhaylov V, et al. Safety and efficacy of pitolisant on cataplexy in patients with narcolepsy: a randomised, double-blind, placebo-controlled trial. *Lancet Neurol.* 2017;16(3):200-207. [doi:10.1016/S1474-4422(16)30333-7](https://doi.org/10.1016/S1474-4422(16)30333-7) · [PubMed 28129985](https://pubmed.ncbi.nlm.nih.gov/28129985/)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
