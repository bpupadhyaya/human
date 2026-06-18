---
schema: human-scale-entry/v1
id: obsessive-compulsive-disorder
name: Obsessive-Compulsive Disorder
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-08
summary: "OCD (2-3% lifetime prevalence) is driven by cortico-striato-thalamo-cortical circuit hyperactivity; SSRIs at high doses are first-line; CBT with ERP achieves remission in ~60%; glutamatergic and dopaminergic dysregulation underlie treatment-resistant OCD."
aliases: ["OCD", "obsessive compulsive disorder", "obsessive-compulsive", "OCD spectrum", "CSTC circuit", "contamination OCD", "checking OCD", "hoarding disorder"]
sources:
  - id: abramowitz-2009-ocd-review
    type: peer-reviewed
    cite: "Abramowitz JS, Taylor S, McKay D. Obsessive-compulsive disorder. Lancet. 2009;374(9688):491-499."
    doi: "10.1016/S0140-6736(09)60240-3"
    pmid: "19665647"
    url: "https://doi.org/10.1016/S0140-6736(09)60240-3"
    accessed: "2026-06-08"
  - id: chamberlain-2008-ocd-neuroscience
    type: peer-reviewed
    cite: "Chamberlain SR, Menzies L, Hampshire A, et al. Orbitofrontal dysfunction in patients with obsessive-compulsive disorder and their unaffected relatives. Science. 2008;321(5887):421-422."
    doi: "10.1126/science.1154433"
    pmid: "18635808"
    url: "https://doi.org/10.1126/science.1154433"
    accessed: "2026-06-08"
  - id: pittenger-2017-ocd-glutamate
    type: peer-reviewed
    cite: "Pittenger C. Glutamate and anxiety disorders. Curr Top Behav Neurosci. 2015;23:145-168."
    doi: "10.1007/7854_2014_295"
    pmid: "25091538"
    url: "https://doi.org/10.1007/7854_2014_295"
    accessed: "2026-06-08"
  - id: soomro-2008-ssri-ocd
    type: peer-reviewed
    cite: "Soomro GM, Altman D, Rajagopal S, Oakley-Browne M. Selective serotonin re-uptake inhibitors (SSRIs) versus placebo for obsessive compulsive disorder (OCD). Cochrane Database Syst Rev. 2008;(1):CD001765."
    doi: "10.1002/14651858.CD001765.pub3"
    pmid: "18253995"
    url: "https://doi.org/10.1002/14651858.CD001765.pub3"
    accessed: "2026-06-08"
cross_links:
  - target: 01-human/03-molecular/serotonin
    relation: connects-to
    note: "SSRIs at high doses (fluoxetine 40-80 mg, fluvoxamine, sertraline) are first-line OCD treatment; serotonin modulates cortico-striatal signaling; SSRI response in OCD requires 8-12 weeks at maximal doses; serotonergic augmentation of CBT improves outcomes."
  - target: 01-human/03-molecular/dopamine
    relation: connects-to
    note: "Dopamine in ventral striatum and OFC drives reward learning and habit formation; CSTC circuit dopamine dysregulation contributes to compulsive behaviors; atypical antipsychotic augmentation (risperidone, aripiprazole) of SSRIs benefits treatment-resistant OCD via D2 blockade."
  - target: 01-human/03-molecular/glutamate
    relation: connects-to
    note: "Glutamatergic hyperactivity in OFC-striatum projections drives compulsive symptom circuits; riluzole (glutamate release inhibitor) and memantine reduce OCD symptoms in randomized trials; ketamine produces rapid anti-OCD effects in treatment-resistant cases."
  - target: 01-human/03-molecular/gaba
    relation: connects-to
    note: "Reduced GABAergic inhibitory tone in OFC and striatum contributes to CSTC hyperactivity in OCD; benzodiazepines provide short-term symptom relief; inositol (indirect GABA modulator) and D-cycloserine (NMDA partial agonist) augment ERP therapy outcomes."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "OCD is a CSTC circuit disorder: OFC and ACC hyperactivity → excessive error detection; caudate nucleus fail to suppress OFC-thalamus loop → repetitive behaviors; SSRI treatment and ERP both normalize caudate hypermetabolism on PET imaging."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "Major depression is the most common comorbidity of OCD (~65% lifetime), usually arising secondary to the burden of obsessions and compulsions; the two share serotonergic dysfunction and both respond to SSRIs, though OCD needs higher doses and 8-12 weeks to respond."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "OCD is distinguished from generalized anxiety disorder by the form of the thoughts: OCD obsessions are intrusive, ego-dystonic, and trigger stereotyped compulsions, whereas GAD worry is about realistic everyday concerns, ego-syntonic, and not ritualized."
  - target: 02-pathogen/02-bacteria/streptococcus-pyogenes
    relation: connects-to
    note: "PANDAS links Group A Streptococcus to abrupt-onset pediatric OCD: anti-streptococcal antibodies cross-react with basal-ganglia neurons to inflame the CSTC circuit, producing sudden obsessions and tics that may respond to antibiotics and immunotherapy."
  - target: 01-human/07-system/borderline-personality-disorder
    relation: connects-to
    note: "OCD and BPD both involve distressing, hard-to-control inner experience but differ in form: OCD is ego-dystonic intrusive thoughts and compulsions, BPD is emotional instability, impulsivity and unstable relationships; they can co-occur, with ERP/CBT central to OCD and DBT to BPD."
  - target: 01-human/07-system/autism-spectrum-disorder
    relation: connects-to
    note: "OCD and autism overlap substantially: both feature repetitive behaviors and need for sameness, OCD is markedly more prevalent in autistic people, and distinguishing ego-dystonic compulsions from autistic routines (often not distressing in themselves) is a key clinical challenge."
  - target: 01-human/07-system/anorexia-nervosa
    relation: connects-to
    note: "OCD and anorexia nervosa are closely linked: they share perfectionism, intrusive thoughts and ritualized behavior, frequently co-occur, and high premorbid OCD traits predict anorexia; orbitofrontal-striatal circuitry features in both, though anorexia's rituals center on food."
  - target: 01-human/07-system/panic-disorder
    relation: connects-to
    note: "OCD and panic disorder are anxiety-spectrum disorders that often co-occur but differ: OCD's anxiety is driven by intrusive obsessions relieved by compulsions, while panic is sudden autonomic surges of fear—both share SSRI responsiveness and exposure-based therapy."
  - target: 01-human/07-system/schizophrenia
    relation: connects-to
    note: "OCD and schizophrenia intersect in schizo-obsessive presentations: OC symptoms are common in schizophrenia and can worsen on antipsychotics like clozapine, and both involve glutamate and dopamine dysregulation—so telling obsessions from delusions guides care."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "OCD arises from dysfunction in cortico-striato-thalamo-cortical neurons: overactive loops through the orbitofrontal cortex, caudate, and thalamus generate the repetitive obsessions and compulsions, which is why SSRIs and, in refractory cases, deep brain stimulation can help."
  - target: 01-human/07-system/ptsd
    relation: connects-to
    note: "OCD and PTSD both feature intrusive, distressing thoughts but differ in origin: OCD's obsessions are recognized as one's own and neutralized by compulsions, while PTSD's intrusions are trauma memories—overlapping phenomenology with different roots."
  - target: 01-human/07-system/bipolar-disorder
    relation: connects-to
    note: "OCD and bipolar disorder frequently co-occur and complicate each other: comorbid OCD worsens bipolar outcomes, and SSRIs used for OCD can trigger mania in bipolar patients—so screening for bipolarity is essential before treating OCD pharmacologically."
  - target: 01-human/07-system/internet-gaming-disorder
    relation: connects-to
    note: "OCD and internet gaming disorder both involve compulsive, hard-to-resist behaviors engaging fronto-striatal circuits: OCD's compulsions relieve anxiety while gaming is reward-driven, but both show the loss of behavioral control that blurs compulsion and addiction."
  - target: 01-human/03-molecular/cortisol
    relation: connects-to
    note: "OCD involves a dysregulated stress axis: HPA-axis and cortisol abnormalities accompany the disorder, and stress worsens obsessions and compulsions—so the stress system interacts with the cortico-striatal circuits that drive the repetitive, intrusive symptoms."
  - target: 01-human/07-system/social-anxiety-disorder
    relation: connects-to
    note: "OCD sits within the anxiety-related spectrum alongside social anxiety: both involve excessive fear-driven avoidance and respond to SSRIs and exposure therapy, though OCD's hallmark is intrusive obsessions and ritualized compulsions rather than social fear."
  - target: 01-human/05-tissue/hippocampus
    relation: connects-to
    note: "OCD shows altered cortico-striatal-limbic circuitry including the hippocampus: imaging reveals overactive orbitofrontal-striatal loops with hippocampal and memory-circuit changes, so OCD maps to specific brain-circuit dysfunction that medication and CBT recalibrate."
  - target: 01-human/03-molecular/bdnf
    relation: connects-to
    note: "BDNF links OCD to faulty brain wiring: this neuroplasticity factor shapes the cortico-striatal circuits that misfire in OCD, and BDNF gene variants are among its genetic risk factors—helping explain why SSRIs, which raise BDNF, slowly remodel the disorder."
  - target: 01-human/07-system/attention-deficit-hyperactivity-disorder
    relation: connects-to
    note: "OCD and ADHD frequently co-occur yet pull in opposite directions: both involve frontostriatal dysfunction, but OCD is over-controlled and ADHD impulsive, so stimulants for ADHD can sometimes worsen obsessions—complicating treatment when the two coexist."
  - target: 01-human/07-system/huntingtons-disease
    relation: connects-to
    note: "Huntington's disease shows OCD's basal-ganglia roots: striatal degeneration produces perseverative, obsessive, and compulsive behaviors, echoing the cortico-striatal-thalamic loop that misfires in OCD—evidence this circuit can generate repetitive thought and action."
  - target: 01-human/04-cellular/microglia
    relation: connects-to
    note: "OCD can flare from brain inflammation in PANDAS: after strep infection, activated microglia and autoantibodies inflame the basal ganglia, triggering sudden-onset obsessions and tics in children—evidence the immune system can drive the disorder."
  - target: 01-human/03-molecular/mhc-class-ii
    relation: connects-to
    note: "PANDAS ties OCD to immune genetics: streptococcal antigens presented by MHC class II can prime antibodies that cross-react with basal-ganglia neurons (molecular mimicry), an autoimmune route to abrupt childhood obsessive-compulsive symptoms."
  - target: 01-human/07-system/insomnia-disorder
    relation: connects-to
    note: "OCD and insomnia feed each other: intrusive obsessions and compulsive rituals delay and fragment sleep, and the resulting sleep loss worsens the anxiety and cognitive control that keep OCD going—so sleep is part of treatment."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Some childhood OCD is autoimmune, flagged by complement: in PANDAS, strep infection triggers antibodies and complement that attack basal-ganglia neurons, and complement-driven synaptic pruning is implicated in the circuit changes of OCD."
  - target: 01-human/04-cellular/astrocyte
    relation: connects-to
    note: "OCD's faulty brain circuit involves astrocytes: these glial cells clear glutamate in the cortico-striatal loop that misfires in OCD, so astrocyte dysfunction may sustain the runaway excitation behind intrusive thoughts and compulsions."
  - target: 01-human/03-molecular/oxytocin
    relation: connects-to
    note: "Oxytocin shapes the repetitive behaviors of OCD: the bonding hormone also drives grooming and checking-type behaviors and is dysregulated in OCD, linking the social hormone to compulsive ritual."
  - target: 01-human/05-tissue/synapse
    relation: connects-to
    note: "OCD is increasingly seen as a synapse disorder: genes for the glutamatergic synapse (like SAPAP3) disturb signaling in the cortico-striatal loop, so faulty synaptic wiring underlies the circuit that locks into obsessions and compulsions."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "OCD's signaling leans on calcium: voltage-gated calcium-channel genes implicated across psychiatric disorders shape the synaptic plasticity of the OCD circuit, tying ion flux to how compulsive habits are learned and held."
  - target: 01-human/04-cellular/b-cell
    relation: connects-to
    note: "In PANDAS, B cells turn OCD on suddenly: a strep infection makes the immune system produce cross-reactive antibodies that attack the basal ganglia, triggering abrupt-onset OCD and tics in susceptible children."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Brain imaging reveals OCD's overactive circuit: PET and fMRI photons show a hyperactive loop linking the orbitofrontal cortex, striatum and thalamus, the target even of radiosurgical capsulotomy in refractory cases."
  - target: 01-human/04-cellular/oligodendrocyte
    relation: connects-to
    note: "OCD shows altered white matter: the oligodendrocytes that myelinate the cortico-striatal tracts shape how fast the circuit signals, and changes in these connections appear in diffusion imaging studies."
  - target: 01-human/06-organ/large-intestine
    relation: connects-to
    note: "The gut may sway OCD: emerging work ties the intestinal microbiome to anxiety and compulsive behavior through the gut-brain axis, hinting the bowel's microbes influence the disorder's severity."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "OCD's cousins attack the skin: body-focused repetitive behaviors — compulsive skin-picking and hair-pulling — sit in the OCD spectrum, driving sufferers to wound their own skin in irresistible, shame-laden rituals."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "Zinc may matter to the obsessive brain: low zinc is reported in OCD and the mineral modulates the glutamate signaling implicated in the disorder, so zinc supplementation has been trialed as an adjunct to standard treatment."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "OCD weighs on the heart over time: the chronic anxiety and stress raise cardiovascular risk, and the SSRIs that treat it can prolong the QT interval, so the heart is watched in long-term, high-dose therapy."
  - target: 01-human/03-molecular/norepinephrine
    relation: connects-to
    note: "OCD's most potent drug works partly on noradrenaline: clomipramine, the tricyclic that set the benchmark for treating it, blocks both serotonin and norepinephrine reuptake, a dual action that helps in cases SSRIs alone do not."
  - target: 01-human/03-molecular/melatonin
    relation: connects-to
    note: "OCD disturbs the night: insomnia and a delayed circadian rhythm with blunted melatonin are common, and the lost sleep worsens the intrusive thoughts and compulsions that already crowd the evening hours."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "OCD is increasingly seen as a glutamatergic disorder, and magnesium sits in that pathway: as a natural NMDA-receptor blocker it dampens the over-excitation of the cortico-striatal circuits, making it a studied adjunct alongside glutamate-modulating drugs."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "Some childhood OCD is an autoimmune storm: in PANDAS/PANS, antibodies raised against streptococcus cross-react with basal-ganglia neurons, triggering abrupt-onset obsessions and tics that may respond to immune therapy rather than SSRIs alone."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "Hormonal transitions can unmask OCD: it often first appears or sharply worsens in pregnancy and the postpartum period, the perinatal form fixating on the baby's safety, while symptoms can also flare premenstrually."
  - target: 01-human/07-system/gut-microbiome
    relation: connects-to
    note: "The gut may whisper into the obsessive brain: altered microbiome composition is reported in OCD, and through the microbiome-gut-brain axis it can shape the serotonin and stress signaling implicated in the disorder."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "PANDAS makes OCD an autoimmune disease: after strep infection, molecular mimicry drives T helper cells and antibodies against basal-ganglia neurons, sparking the abrupt onset of obsessions and tics in susceptible children."
  - target: 01-human/07-system/bulimia-nervosa
    relation: connects-to
    note: "OCD and eating disorders share a compulsive core: bulimia nervosa frequently co-occurs with OCD, the binge-purge rituals echoing obsessive thoughts and compulsive acts, and the two run together in families."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "Inflammation may stoke the obsessive brain: studies find raised IL-6 and other inflammatory cytokines in OCD, hinting that immune activation contributes to the disorder alongside its serotonin and glutamate disturbances."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "It is a disorder of a specific brain loop: OCD arises from overactivity in the cortico-striatal-thalamic circuit linking the orbitofrontal cortex and basal ganglia, the wiring whose miscommunication generates intrusive thoughts and the urge to ritualize."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: connects-to
    note: "An immune arm shows up in some cases: in the PANDAS subtype where strep infection triggers OCD, dysregulated T-cell immunity — including regulatory T cells — lets autoantibodies cross-react with the basal ganglia."
  - target: 01-human/03-molecular/endocannabinoid
    relation: connects-to
    note: "The body's cannabis system modulates compulsivity: endocannabinoid signaling tunes the fear and habit circuits implicated in OCD, and cannabinoid agents are being explored for the obsessions and compulsions that resist standard drugs."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "Neuroinflammation may stoke the circuits: NF-κB-driven microglial inflammation is implicated in OCD, fitting the autoimmune PANDAS subtype where strep-triggered inflammation inflames the basal ganglia behind sudden-onset symptoms."
  - target: 01-human/07-system/parkinsons-disease
    relation: connects-to
    note: "Shared basal-ganglia wiring links them: OCD and Parkinson's both involve cortico-striatal circuits, and the dopamine-replacement therapy of Parkinson's can itself unleash obsessive-compulsive and impulse-control behaviors."
  - target: 01-human/07-system/alcohol-use-disorder
    relation: connects-to
    note: "Compulsion can spill into the bottle: alcohol and other substance use disorders are over-represented in OCD, with some patients drinking to quiet relentless anxiety and intrusive thoughts."
  - target: 01-human/07-system/binge-eating-disorder
    relation: connects-to
    note: "Compulsion can fix on food: the repetitive, hard-to-resist urges of OCD overlap with binge eating, and the two co-occur, sharing the impaired inhibitory control of cortico-striatal circuits."
  - target: 01-human/07-system/cannabis-use-disorder
    relation: connects-to
    note: "Some self-medicate intrusive thoughts: cannabis is used by some with OCD to dampen anxiety and obsessions, a self-medication that can foster dependence while heavy use may worsen the underlying symptoms."
  - target: 01-human/07-system/epilepsy
    relation: connects-to
    note: "Temporal-lobe circuits can generate both: obsessive-compulsive symptoms are over-represented in epilepsy, especially temporal-lobe epilepsy, reflecting shared limbic and cortico-striatal dysfunction."
  - target: 01-human/07-system/migraine
    relation: connects-to
    note: "Headache keeps company with the disorder: OCD shows elevated comorbidity with migraine, the two sharing serotonergic dysregulation and a tendency toward chronic, recurrent symptom patterns."
  - target: 01-human/07-system/atopic-dermatitis
    relation: connects-to
    note: "Compulsive scratching meets chronic itch: OCD-spectrum skin-picking and the relentless itch of atopic dermatitis reinforce each other, and the two conditions co-occur more than chance."
  - target: 01-human/07-system/obesity
    relation: connects-to
    note: "Its long-term medications add weight: the high-dose SSRIs and antipsychotic augmentation used in OCD promote weight gain, contributing to obesity over years of treatment."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "Compulsive washing wrecks the skin: repetitive handwashing in OCD causes chronic irritant contact dermatitis with cracking and bleeding, the visible toll of the contamination-and-cleaning cycle."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "Its strongest old drug strains the heart: clomipramine, the tricyclic uniquely effective in OCD, prolongs the QT interval and carries arrhythmia and orthostatic risk, demanding cardiac caution."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "Anticholinergic therapy slows the gut: clomipramine and high-dose SSRIs used for OCD cause constipation and other anticholinergic and serotonergic gut effects that complicate long-term treatment."
---

# Obsessive-Compulsive Disorder

## Overview

**Obsessive-compulsive disorder (OCD)** is a chronic, disabling neuropsychiatric condition characterized by recurrent **obsessions** (intrusive, unwanted thoughts, images, or urges causing marked anxiety) and **compulsions** (repetitive behaviors or mental acts performed to neutralize anxiety) that consume ≥1 hour per day and cause significant functional impairment [^abramowitz-2009-ocd-review].

OCD affects approximately **2–3% of the global population** (lifetime prevalence) — roughly 75–100 million people — and carries the fourth-highest burden of neuropsychiatric illness worldwide by disability-adjusted life years (DALYs). Mean age of onset is bimodal: **early-onset** (~10 years, male-predominant) and **adult-onset** (~20 years, female-predominant). Onset is usually gradual, worsens under stress, and is chronic in ~40–50% of untreated cases.

**DSM-5 diagnosis** requires:
1. Presence of obsessions, compulsions, or both
2. Time-consuming (>1 hour/day) or causing significant distress/impairment
3. Not attributable to substances or medical conditions
4. Not better explained by another psychiatric disorder

**OCD spectrum disorders** (DSM-5 "Obsessive-Compulsive and Related Disorders" chapter) include body dysmorphic disorder (BDD), hoarding disorder, trichotillomania (hair-pulling), excoriation (skin-picking), and olfactory reference disorder — all sharing CSTC circuit dysfunction.

## Structure

### OCD subtypes and common themes

| Obsession theme | Core fear | Compulsion type |
|:---|:---|:---|
| **Contamination** | Illness, dirt, spreading germs | Washing, cleaning, avoidance |
| **Checking** | Harm to self/others, incompleteness | Repeated checking (locks, stoves, light switches) |
| **Symmetry/ordering** | "Not just right" feeling, incompleteness | Arranging, counting, touching |
| **Unacceptable thoughts** | Blasphemous, sexual, violent intrusive thoughts | Mental rituals, seeking reassurance, avoidance |
| **Hoarding** | Fear of losing important items | Excessive acquisition, inability to discard |

**Y-BOCS (Yale-Brown Obsessive Compulsive Scale)** is the gold-standard severity measure: 10 items (5 obsession + 5 compulsion, each rated 0–4); total 0–40; mild 8–15, moderate 16–23, severe 24–31, extreme 32–40. Treatment response is defined as ≥35% Y-BOCS reduction.

### Cortico-striato-thalamo-cortical (CSTC) circuit model [^chamberlain-2008-ocd-neuroscience]

OCD is understood as a circuit disorder with two competing pathways:

**"Worry loop" (hyperactive in OCD):**
Orbitofrontal cortex (OFC) → caudate nucleus → globus pallidus interna (GPi) → thalamus → back to OFC (direct pathway via striatum → inhibits GPi → disinhibits thalamus → enhances OFC activity)

**Normal suppression mechanism (underactive in OCD):**
OFC → putamen → globus pallidus externa (GPe) → subthalamic nucleus → GPi → thalamus → OFC suppression (indirect pathway)

**OCD pathology:** Caudate nucleus hyperactivity disinhibits the thalamus → excess thalamocortical drive back to OFC → OFC → excessive error monitoring signals ("something is wrong" even after checking) → compulsive corrective behaviors that fail to terminate because the "error" signal persists.

**PET/fMRI evidence:**
- Pre-treatment: increased glucose metabolism in OFC (Brodmann area 11/12/13), caudate nucleus, and thalamus in untreated OCD
- Post-treatment (SSRI or CBT/ERP): normalized caudate and OFC activity, with both treatments converging on the same circuit
- Unaffected relatives of OCD patients show intermediate OFC hyperactivity [^chamberlain-2008-ocd-neuroscience], suggesting a heritable endophenotype

## Function

### Clinical presentation

**Obsessions:** Ego-dystonic (experienced as unwanted, contrary to self-concept), intrusive, and cause marked anxiety. Unlike generalized worry, obsessions are focused on specific feared outcomes and trigger compulsive responses. Common obsessions are sexual, blasphemous, or violent intrusions in ~60%, contamination fears in ~50%, and symmetry/ordering concerns in ~40% (many patients have multiple themes).

**Compulsions:** Repetitive behaviors (washing, checking, ordering) or mental acts (praying, counting, undoing) that temporarily reduce obsessional anxiety but are not pleasurable in themselves and not proportionate to any realistic threat. The temporary relief powerfully reinforces compulsive behavior via negative reinforcement — explaining the self-perpetuating nature of OCD.

**Insight:** Approximately 95% of OCD patients have good-to-fair insight (recognize obsessions as unreasonable); ~5% have poor or absent insight (may appear delusional). Poor insight predicts worse treatment response and greater functional impairment.

**OCD with tic disorder:** ~20-30% of OCD patients have comorbid Tourette syndrome or chronic tic disorder; this subgroup has earlier onset, male predominance, and modestly different treatment response (alpha-2 agonists or antipsychotic augmentation more beneficial).

### Comorbidities

| Comorbidity | Frequency | Implication |
|:---|:---|:---|
| Major depressive disorder | ~65% | Leads to earlier treatment seeking; depression secondary to OCD in most cases |
| Anxiety disorders (GAD, SAD, panic) | ~50% | Shared CSTC/serotonergic dysfunction; SSRIs treat both |
| ADHD | ~20-30% | May require stimulant treatment even in OCD; stimulants rarely worsen OCD |
| Tic disorder/Tourette | ~20-30% | Antipsychotic augmentation more effective |
| Body dysmorphic disorder | ~15% | Same neurobiology, same treatment; may require higher SSRI doses |
| Hoarding disorder | ~25% | Lower SSRI response; may benefit more from CBT/cognitive approaches |

## Pathology

### Neurobiology

**Serotonergic system:** SSRIs are uniquely effective for OCD (compared to imipramine and desipramine, which are ineffective) — establishing a privileged role for serotonin in OCD pathophysiology. High SSRI doses are typically required (fluoxetine 40-80 mg/day vs. 20-40 mg for depression), and full response takes 8-12 weeks. Clomipramine (tricyclic SNRI with dominant serotonin reuptake inhibition) is equally effective to SSRIs but has worse tolerability [^soomro-2008-ssri-ocd].

**Glutamatergic system:** OFC-striatal projections use glutamate as the primary neurotransmitter [^pittenger-2017-ocd-glutamate]. CSF glutamate levels are elevated in OCD. Riluzole (glutamate release inhibitor) reduces OCD symptoms in randomized controlled trials; memantine (NMDA antagonist) shows benefit in treatment-resistant OCD; single-dose ketamine (NMDA antagonist) produces rapid (~48 hour) anti-compulsive effects.

**Dopaminergic system:** Striatal dopamine dysregulation in OCD contributes to habitual behavior formation. PET studies show D2 receptor abnormalities in caudate. Atypical antipsychotic augmentation (risperidone 0.5-2 mg, aripiprazole 10-15 mg) of SSRI is the best-supported strategy for partial SSRI responders (NNT ~3-4 in pooled trials).

**GABAergic system:** Reduced GABA in OFC and basal ganglia (MRS studies) contributes to CSTC hyperactivity. Benzodiazepines reduce OCD anxiety acutely but do not treat core OCD; long-term use risks dependence.

**Genetics:** OCD is moderately heritable (~40-65% twin studies). First-degree relatives have 5-10× elevated risk. GWAS: no single large-effect loci; implicated pathways include glutamatergic signaling (GRIN2B, DLGAP1, SLC1A1) and serotonin metabolism (SERT/SLC6A4, HTR2A). Copy number variants: 16p13.11 microduplications; 22q11.2 deletions. OCD is genetically correlated with Tourette syndrome (common neuronal circuits) and anxiety disorders.

### Diagnosis

OCD is often underdiagnosed due to shame and secrecy. Mean time from symptom onset to diagnosis is **7-10 years**. Key diagnostic pitfalls:

- **OCD vs. GAD:** OCD obsessions are intrusive, ego-dystonic, and trigger specific compulsions; GAD worry is about realistic everyday concerns, is ego-syntonic, and is not followed by stereotyped compulsions
- **OCD vs. psychosis:** OCD patients retain insight that obsessions are products of their own mind; psychotic patients have true delusions/hallucinations with absent insight
- **Pediatric OCD:** PANS/PANDAS (Pediatric Acute-onset Neuropsychiatric Syndrome) — sudden-onset OCD following Group A streptococcal infection; autoimmune anti-basal ganglia antibodies; treated with antibiotics and immunotherapy plus standard OCD therapy

### Treatment

**First-line — Cognitive-Behavioral Therapy (CBT) with Exposure and Response Prevention (ERP):**
- Gold-standard psychotherapy: patient deliberately confronts feared stimuli (exposure) and refrains from compulsive responses (response prevention) → habituation and violation of feared predictions → CSTC circuit normalization
- Achieves ≥35% Y-BOCS improvement (treatment response) in ~60-70%; remission in ~30-40%
- Optimal delivery: individual therapist-guided sessions (typically 14-20 sessions), 90-minute exposure sessions; limited by access and patient dropout (confronting feared situations is distressing)
- D-cycloserine (partial NMDA agonist, 50 mg before exposure sessions): augments ERP by enhancing NMDA-dependent fear extinction learning; modest effect size in meta-analyses

**First-line — SSRIs (at OCD-level doses):**

| Drug | Starting dose | OCD target dose | Notes |
|:---|:---|:---|:---|
| **Fluoxetine** | 20 mg/day | 40-80 mg/day | Long half-life (active metabolite); once-daily; minimal withdrawal |
| **Fluvoxamine** | 50 mg/day | 150-300 mg/day | FDA-approved for OCD in adults and children; twice-daily; notable CYP1A2/2C19 interactions |
| **Sertraline** | 25-50 mg/day | 100-200 mg/day | FDA-approved for OCD; well-tolerated; once-daily; most-prescribed |
| **Paroxetine** | 10-20 mg/day | 40-60 mg/day | FDA-approved; anticholinergic effects; withdrawal syndrome with abrupt discontinuation |
| **Clomipramine** | 25 mg/day | 100-250 mg/day | Non-selective TCA; equivalent efficacy to SSRIs; anticholinergic + cardiac AEs limit use; reserved for SSRI failures |

**Allow 8-12 weeks** at maximal tolerated dose before declaring failure. Approximately 40-60% of patients respond partially; combination SSRI + ERP is superior to either alone.

**Second-line — Augmentation strategies for SSRI-partial response:**

| Strategy | Evidence | Notes |
|:---|:---|:---|
| **Aripiprazole** (5-15 mg) | Strong (RCT-level) | Partial D2 agonist; reduces EPS vs. risperidone; weight gain |
| **Risperidone** (0.5-2 mg) | Strong (RCT-level) | D2/5-HT2A antagonist; NNT ~3.4; weight gain, EPS possible |
| **Quetiapine** (50-150 mg) | Moderate | More sedating; used when insomnia is comorbid |
| **Riluzole** (50-100 mg) | Moderate (RCT) | Reduces OFC glutamate release; especially in pediatric OCD |
| **Memantine** (5-20 mg) | Moderate (open-label) | NMDA antagonism; reduces Y-BOCS in several small RCTs |

**Neuromodulation (treatment-resistant OCD — SSRI + ERP failures):**
- **Deep brain stimulation (DBS):** FDA Humanitarian Device Exemption (HDE) approval 2009 for treatment-resistant OCD; targets include anterior limb of internal capsule/ventral capsule–ventral striatum (VC/VS), nucleus accumbens, and subthalamic nucleus (STN); 50-60% response rate (≥35% Y-BOCS reduction) in carefully selected patients
- **Transcranial magnetic stimulation (TMS):** FDA-cleared 2018 for OCD; targets supplementary motor area (SMA) or dorsal medial PFC (dmPFC); inhibitory theta-burst or low-frequency rTMS; response ~40% in treatment-resistant patients; well-tolerated
- **Gamma Knife radiosurgery (anterior capsulotomy):** Used in extreme treatment-resistant cases; creates anterior capsule lesion to disrupt CSTC circuit; effective but irreversible

## Connections

- `connects-to` → **[Serotonin](../../03-molecular/serotonin/README.md)** — SSRIs at high doses are uniquely effective for OCD; serotonin modulates OFC-striatal CSTC signaling; clomipramine (TCA with dominant serotonin reuptake inhibition) has equivalent efficacy to SSRIs and 8-12 weeks response latency.
- `connects-to` → **[Dopamine](../../03-molecular/dopamine/README.md)** — striatal dopamine dysregulation contributes to compulsive habit formation in OCD; D2 receptor abnormalities in caudate on PET; atypical antipsychotic augmentation (aripiprazole, risperidone) of SSRIs is the best-supported strategy for partial SSRI responders (NNT ~3).
- `connects-to` → **[Glutamate](../../03-molecular/glutamate/README.md)** — glutamatergic hyperactivity in OFC-striatum projections drives compulsive symptom circuits; CSF glutamate elevated in OCD; riluzole and memantine reduce OCD symptoms in RCTs; ketamine produces rapid anti-compulsive effects in treatment-resistant OCD.
- `connects-to` → **[GABA](../../03-molecular/gaba/README.md)** — reduced GABAergic inhibitory tone in OFC and striatum (MRS studies) contributes to CSTC hyperactivity; benzodiazepines provide short-term relief but not disease modification; D-cycloserine (NMDA partial agonist) augments ERP via fear extinction learning.
- `connects-to` → **[Brain](../../06-organ/brain/README.md)** — OCD is a CSTC circuit disorder: OFC/ACC hyperactivity drives excessive error detection; caudate nucleus hyperactivity disinhibits thalamocortical drive back to OFC; SSRIs and ERP both normalize caudate hypermetabolism on PET — converging on the same circuit.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — Major depression is the most common comorbidity of OCD (~65% lifetime), usually arising secondary to the burden of obsessions and compulsions; the two share serotonergic dysfunction and both respond to SSRIs, though OCD needs higher doses and 8-12 weeks to respond.
- `connects-to` → **[Generalized Anxiety Disorder](../generalized-anxiety-disorder/README.md)** — OCD is distinguished from generalized anxiety disorder by the form of the thoughts: OCD obsessions are intrusive, ego-dystonic, and trigger stereotyped compulsions, whereas GAD worry is about realistic everyday concerns, ego-syntonic, and not ritualized.
- `connects-to` → **[Streptococcus pyogenes](../../../02-pathogen/02-bacteria/streptococcus-pyogenes/README.md)** — PANDAS links Group A Streptococcus to abrupt-onset pediatric OCD: anti-streptococcal antibodies cross-react with basal-ganglia neurons to inflame the CSTC circuit, producing sudden obsessions and tics that may respond to antibiotics and immunotherapy.
- `connects-to` → **[Borderline Personality Disorder](../borderline-personality-disorder/README.md)** — OCD and BPD both involve distressing, hard-to-control inner experience but differ in form: OCD is ego-dystonic intrusive thoughts and compulsions, BPD is emotional instability, impulsivity and unstable relationships; they can co-occur, with ERP/CBT central to OCD and DBT to BPD.
- `connects-to` → **[Autism Spectrum Disorder](../autism-spectrum-disorder/README.md)** — OCD and autism overlap substantially: both feature repetitive behaviors and need for sameness, OCD is markedly more prevalent in autistic people, and distinguishing ego-dystonic compulsions from autistic routines (often not distressing in themselves) is a key clinical challenge.
- `connects-to` → **[Anorexia Nervosa](../anorexia-nervosa/README.md)** — OCD and anorexia nervosa are closely linked: they share perfectionism, intrusive thoughts and ritualized behavior, frequently co-occur, and high premorbid OCD traits predict anorexia; orbitofrontal-striatal circuitry features in both, though anorexia's rituals center on food.
- `connects-to` → **[Panic Disorder](../panic-disorder/README.md)** — OCD and panic disorder are anxiety-spectrum disorders that often co-occur but differ: OCD's anxiety is driven by intrusive obsessions relieved by compulsions, while panic is sudden autonomic surges of fear—both share SSRI responsiveness and exposure-based therapy.
- `connects-to` → **[Schizophrenia](../schizophrenia/README.md)** — OCD and schizophrenia intersect in schizo-obsessive presentations: OC symptoms are common in schizophrenia and can worsen on antipsychotics like clozapine, and both involve glutamate and dopamine dysregulation—so telling obsessions from delusions guides care.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — OCD arises from dysfunction in cortico-striato-thalamo-cortical neurons: overactive loops through the orbitofrontal cortex, caudate, and thalamus generate the repetitive obsessions and compulsions, which is why SSRIs and, in refractory cases, deep brain stimulation can help.
- `connects-to` → **[PTSD](../ptsd/README.md)** — OCD and PTSD both feature intrusive, distressing thoughts but differ in origin: OCD's obsessions are recognized as one's own and neutralized by compulsions, while PTSD's intrusions are trauma memories—overlapping phenomenology with different roots.
- `connects-to` → **[Bipolar Disorder](../bipolar-disorder/README.md)** — OCD and bipolar disorder frequently co-occur and complicate each other: comorbid OCD worsens bipolar outcomes, and SSRIs used for OCD can trigger mania in bipolar patients—so screening for bipolarity is essential before treating OCD pharmacologically.
- `connects-to` → **[Internet Gaming Disorder](../internet-gaming-disorder/README.md)** — OCD and internet gaming disorder both involve compulsive, hard-to-resist behaviors engaging fronto-striatal circuits: OCD's compulsions relieve anxiety while gaming is reward-driven, but both show the loss of behavioral control that blurs compulsion and addiction.
- `connects-to` → **[Cortisol](../../03-molecular/cortisol/README.md)** — OCD involves a dysregulated stress axis: HPA-axis and cortisol abnormalities accompany the disorder, and stress worsens obsessions and compulsions—so the stress system interacts with the cortico-striatal circuits that drive the repetitive, intrusive symptoms.
- `connects-to` → **[Social Anxiety Disorder](../social-anxiety-disorder/README.md)** — OCD sits within the anxiety-related spectrum alongside social anxiety: both involve excessive fear-driven avoidance and respond to SSRIs and exposure therapy, though OCD's hallmark is intrusive obsessions and ritualized compulsions rather than social fear.
- `connects-to` → **[Hippocampus](../../05-tissue/hippocampus/README.md)** — OCD shows altered cortico-striatal-limbic circuitry including the hippocampus: imaging reveals overactive orbitofrontal-striatal loops with hippocampal and memory-circuit changes, so OCD maps to specific brain-circuit dysfunction that medication and CBT recalibrate.
- `connects-to` → **[BDNF](../../03-molecular/bdnf/README.md)** — BDNF links OCD to faulty brain wiring: this neuroplasticity factor shapes the cortico-striatal circuits that misfire in OCD, and BDNF gene variants are among its genetic risk factors—helping explain why SSRIs, which raise BDNF, slowly remodel the disorder.
- `connects-to` → **[Attention-Deficit/Hyperactivity Disorder](../attention-deficit-hyperactivity-disorder/README.md)** — OCD and ADHD frequently co-occur yet pull in opposite directions: both involve frontostriatal dysfunction, but OCD is over-controlled and ADHD impulsive, so stimulants for ADHD can sometimes worsen obsessions—complicating treatment when the two coexist.
- `connects-to` → **[Huntington Disease](../huntingtons-disease/README.md)** — Huntington's disease shows OCD's basal-ganglia roots: striatal degeneration produces perseverative, obsessive, and compulsive behaviors, echoing the cortico-striatal-thalamic loop that misfires in OCD—evidence this circuit can generate repetitive thought and action.
- `connects-to` → **[Microglia](../../04-cellular/microglia/README.md)** — OCD can flare from brain inflammation in PANDAS: after strep infection, activated microglia and autoantibodies inflame the basal ganglia, triggering sudden-onset obsessions and tics in children—evidence the immune system can drive the disorder.
- `connects-to` → **[MHC Class II](../../03-molecular/mhc-class-ii/README.md)** — PANDAS ties OCD to immune genetics: streptococcal antigens presented by MHC class II can prime antibodies that cross-react with basal-ganglia neurons (molecular mimicry), an autoimmune route to abrupt childhood obsessive-compulsive symptoms.
- `connects-to` → **[Insomnia Disorder](../insomnia-disorder/README.md)** — OCD and insomnia feed each other: intrusive obsessions and compulsive rituals delay and fragment sleep, and the resulting sleep loss worsens the anxiety and cognitive control that keep OCD going—so sleep is part of treatment.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Some childhood OCD is autoimmune, flagged by complement: in PANDAS, strep infection triggers antibodies and complement that attack basal-ganglia neurons, and complement-driven synaptic pruning is implicated in the circuit changes of OCD.
- `connects-to` → **[Astrocyte](../../04-cellular/astrocyte/README.md)** — OCD's faulty brain circuit involves astrocytes: these glial cells clear glutamate in the cortico-striatal loop that misfires in OCD, so astrocyte dysfunction may sustain the runaway excitation behind intrusive thoughts and compulsions.
- `connects-to` → **[Oxytocin](../../03-molecular/oxytocin/README.md)** — Oxytocin shapes the repetitive behaviors of OCD: the bonding hormone also drives grooming and checking-type behaviors and is dysregulated in OCD, linking the social hormone to compulsive ritual.
- `connects-to` → **[Synapse](../../05-tissue/synapse/README.md)** — OCD is increasingly seen as a synapse disorder: genes for the glutamatergic synapse (like SAPAP3) disturb signaling in the cortico-striatal loop, so faulty synaptic wiring underlies the circuit that locks into obsessions and compulsions.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — OCD's signaling leans on calcium: voltage-gated calcium-channel genes implicated across psychiatric disorders shape the synaptic plasticity of the OCD circuit, tying ion flux to how compulsive habits are learned and held.
- `connects-to` → **[B Cell](../../04-cellular/b-cell/README.md)** — In PANDAS, B cells turn OCD on suddenly: a strep infection makes the immune system produce cross-reactive antibodies that attack the basal ganglia, triggering abrupt-onset OCD and tics in susceptible children.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Brain imaging reveals OCD's overactive circuit: PET and fMRI photons show a hyperactive loop linking the orbitofrontal cortex, striatum and thalamus, the target even of radiosurgical capsulotomy in refractory cases.
- `connects-to` → **[Oligodendrocyte](../../04-cellular/oligodendrocyte/README.md)** — OCD shows altered white matter: the oligodendrocytes that myelinate the cortico-striatal tracts shape how fast the circuit signals, and changes in these connections appear in diffusion imaging studies.
- `connects-to` → **[Large Intestine](../../06-organ/large-intestine/README.md)** — The gut may sway OCD: emerging work ties the intestinal microbiome to anxiety and compulsive behavior through the gut-brain axis, hinting the bowel's microbes influence the disorder's severity.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — OCD's cousins attack the skin: body-focused repetitive behaviors — compulsive skin-picking and hair-pulling — sit in the OCD spectrum, driving sufferers to wound their own skin in irresistible, shame-laden rituals.
- `connects-to` → **[Zinc](../../02-atomic/zinc/README.md)** — Zinc may matter to the obsessive brain: low zinc is reported in OCD and the mineral modulates the glutamate signaling implicated in the disorder, so zinc supplementation has been trialed as an adjunct to standard treatment.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — OCD weighs on the heart over time: the chronic anxiety and stress raise cardiovascular risk, and the SSRIs that treat it can prolong the QT interval, so the heart is watched in long-term, high-dose therapy.
- `connects-to` → **[Norepinephrine](../../03-molecular/norepinephrine/README.md)** — OCD's most potent drug works partly on noradrenaline: clomipramine, the tricyclic that set the benchmark for treating it, blocks both serotonin and norepinephrine reuptake, a dual action that helps in cases SSRIs alone do not.
- `connects-to` → **[Melatonin](../../03-molecular/melatonin/README.md)** — OCD disturbs the night: insomnia and a delayed circadian rhythm with blunted melatonin are common, and the lost sleep worsens the intrusive thoughts and compulsions that already crowd the evening hours.
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — OCD is increasingly seen as a glutamatergic disorder, and magnesium sits in that pathway: as a natural NMDA-receptor blocker it dampens the over-excitation of the cortico-striatal circuits, making it a studied adjunct alongside glutamate-modulating drugs.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — Some childhood OCD is an autoimmune storm: in PANDAS/PANS, antibodies raised against streptococcus cross-react with basal-ganglia neurons, triggering abrupt-onset obsessions and tics that may respond to immune therapy rather than SSRIs alone.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — Hormonal transitions can unmask OCD: it often first appears or sharply worsens in pregnancy and the postpartum period, the perinatal form fixating on the baby's safety, while symptoms can also flare premenstrually.
- `connects-to` → **[Gut Microbiome](../gut-microbiome/README.md)** — The gut may whisper into the obsessive brain: altered microbiome composition is reported in OCD, and through the microbiome-gut-brain axis it can shape the serotonin and stress signaling implicated in the disorder.
- `connects-to` → **[T Helper Cell](../../04-cellular/t-helper-cell/README.md)** — PANDAS makes OCD an autoimmune disease: after strep infection, molecular mimicry drives T helper cells and antibodies against basal-ganglia neurons, sparking the abrupt onset of obsessions and tics in susceptible children.
- `connects-to` → **[Bulimia Nervosa](../bulimia-nervosa/README.md)** — OCD and eating disorders share a compulsive core: bulimia nervosa frequently co-occurs with OCD, the binge-purge rituals echoing obsessive thoughts and compulsive acts, and the two run together in families.
- `connects-to` → **[Interleukin-6](../../03-molecular/il-6/README.md)** — Inflammation may stoke the obsessive brain: studies find raised IL-6 and other inflammatory cytokines in OCD, hinting that immune activation contributes to the disorder alongside its serotonin and glutamate disturbances.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — It is a disorder of a specific brain loop: OCD arises from overactivity in the cortico-striatal-thalamic circuit linking the orbitofrontal cortex and basal ganglia, the wiring whose miscommunication generates intrusive thoughts and the urge to ritualize.
- `connects-to` → **[Regulatory T Cell](../../04-cellular/regulatory-t-cell/README.md)** — An immune arm shows up in some cases: in the PANDAS subtype where strep infection triggers OCD, dysregulated T-cell immunity — including regulatory T cells — lets autoantibodies cross-react with the basal ganglia.
- `connects-to` → **[Endocannabinoid System](../../03-molecular/endocannabinoid/README.md)** — The body's cannabis system modulates compulsivity: endocannabinoid signaling tunes the fear and habit circuits implicated in OCD, and cannabinoid agents are being explored for the obsessions and compulsions that resist standard drugs.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — Neuroinflammation may stoke the circuits: NF-κB-driven microglial inflammation is implicated in OCD, fitting the autoimmune PANDAS subtype where strep-triggered inflammation inflames the basal ganglia behind sudden-onset symptoms.
- `connects-to` → **[Parkinson's Disease](../parkinsons-disease/README.md)** — Shared basal-ganglia wiring links them: OCD and Parkinson's both involve cortico-striatal circuits, and the dopamine-replacement therapy of Parkinson's can itself unleash obsessive-compulsive and impulse-control behaviors.
- `connects-to` → **[Alcohol Use Disorder](../alcohol-use-disorder/README.md)** — Compulsion can spill into the bottle: alcohol and other substance use disorders are over-represented in OCD, with some patients drinking to quiet relentless anxiety and intrusive thoughts.
- `connects-to` → **[Binge Eating Disorder](../binge-eating-disorder/README.md)** — Compulsion can fix on food: the repetitive, hard-to-resist urges of OCD overlap with binge eating, and the two co-occur, sharing the impaired inhibitory control of cortico-striatal circuits.
- `connects-to` → **[Cannabis Use Disorder](../cannabis-use-disorder/README.md)** — Some self-medicate intrusive thoughts: cannabis is used by some with OCD to dampen anxiety and obsessions, a self-medication that can foster dependence while heavy use may worsen the underlying symptoms.
- `connects-to` → **[Epilepsy](../epilepsy/README.md)** — Temporal-lobe circuits can generate both: obsessive-compulsive symptoms are over-represented in epilepsy, especially temporal-lobe epilepsy, reflecting shared limbic and cortico-striatal dysfunction.
- `connects-to` → **[Migraine](../migraine/README.md)** — Headache keeps company with the disorder: OCD shows elevated comorbidity with migraine, the two sharing serotonergic dysregulation and a tendency toward chronic, recurrent symptom patterns.
- `connects-to` → **[Atopic Dermatitis](../atopic-dermatitis/README.md)** — Compulsive scratching meets chronic itch: OCD-spectrum skin-picking and the relentless itch of atopic dermatitis reinforce each other, and the two conditions co-occur more than chance.
- `connects-to` → **[Obesity](../obesity/README.md)** — Its long-term medications add weight: the high-dose SSRIs and antipsychotic augmentation used in OCD promote weight gain, contributing to obesity over years of treatment.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — Compulsive washing wrecks the skin: repetitive handwashing in OCD causes chronic irritant contact dermatitis with cracking and bleeding, the visible toll of the contamination-and-cleaning cycle.
- `connects-to` → **[Cardiovascular System](../cardiovascular-system/README.md)** — Its strongest old drug strains the heart: clomipramine, the tricyclic uniquely effective in OCD, prolongs the QT interval and carries arrhythmia and orthostatic risk, demanding cardiac caution.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — Anticholinergic therapy slows the gut: clomipramine and high-dose SSRIs used for OCD cause constipation and other anticholinergic and serotonergic gut effects that complicate long-term treatment.

[^abramowitz-2009-ocd-review]: Abramowitz JS, Taylor S, McKay D. Obsessive-compulsive disorder. *Lancet.* 2009;374(9688):491-499. [doi:10.1016/S0140-6736(09)60240-3](https://doi.org/10.1016/S0140-6736(09)60240-3) · [PubMed 19665647](https://pubmed.ncbi.nlm.nih.gov/19665647/)
[^chamberlain-2008-ocd-neuroscience]: Chamberlain SR, Menzies L, Hampshire A, et al. Orbitofrontal dysfunction in patients with OCD and their unaffected relatives. *Science.* 2008;321(5887):421-422. [doi:10.1126/science.1154433](https://doi.org/10.1126/science.1154433) · [PubMed 18635808](https://pubmed.ncbi.nlm.nih.gov/18635808/)
[^pittenger-2017-ocd-glutamate]: Pittenger C. Glutamate and anxiety disorders. *Curr Top Behav Neurosci.* 2015;23:145-168. [doi:10.1007/7854_2014_295](https://doi.org/10.1007/7854_2014_295) · [PubMed 25091538](https://pubmed.ncbi.nlm.nih.gov/25091538/)
[^soomro-2008-ssri-ocd]: Soomro GM, Altman D, Rajagopal S, Oakley-Browne M. SSRIs versus placebo for OCD. *Cochrane Database Syst Rev.* 2008;(1):CD001765. [doi:10.1002/14651858.CD001765.pub3](https://doi.org/10.1002/14651858.CD001765.pub3) · [PubMed 18253995](https://pubmed.ncbi.nlm.nih.gov/18253995/)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
