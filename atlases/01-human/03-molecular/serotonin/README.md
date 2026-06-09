---
schema: human-scale-entry/v1
id: serotonin
name: Serotonin
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-04
summary: "5-Hydroxytryptamine (5-HT); monoamine neurotransmitter synthesized from tryptophan by TPH1/TPH2 + AADC. ~95% in GI enterochromaffin cells; ~5% CNS (raphe nuclei). Regulates mood, sleep, GI motility, and platelet aggregation. Key SSRI target."
aliases: ["5-HT", "5-hydroxytryptamine", "enteramine", "serotonergic"]
taxonomy:
  gene_symbol: "TPH2"
  uniprot: "P17752"
  note: "TPH1 (peripheral) and TPH2 (CNS) are the two tryptophan hydroxylase isoforms synthesizing 5-HT"
sources:
  - id: rapport-1948-isolation
    type: peer-reviewed
    cite: "Rapport MM, Green AA, Page IH. Serum vasoconstrictor (serotonin) IV. Isolation and characterization. J Biol Chem. 1948;176(3):1243-51."
    pmid: "18887360"
  - id: berger-2009-ssri
    type: peer-reviewed
    cite: "Berger M, Gray JA, Roth BL. The expanded biology of serotonin. Annu Rev Med. 2009;60:355-66."
    doi: "10.1146/annurev.med.60.042307.110802"
  - id: gershon-1999-gut-serotonin
    type: peer-reviewed
    cite: "Gershon MD. The enteric nervous system: a second brain. Hosp Pract (1995). 1999;34(7):31-42."
    pmid: "10090070"
cross_links:
  - target: 01-human/04-cellular/neuron
    relation: expressed-by
    note: "CNS serotonin (~5% of body total) is synthesized in raphe nucleus neurons and projected broadly to limbic, cortical, and cerebellar targets."
  - target: 01-human/07-system/nervous-system
    relation: modulates
    note: "CNS 5-HT regulates mood, sleep-wake cycles, appetite, cognition, and thermoregulation via 14+ receptor subtypes spanning raphe projections."
  - target: 01-human/07-system/digestive-system
    relation: modulates
    note: "GI 5-HT coordinates peristalsis (5-HT4), mediates nausea signaling (5-HT3), and regulates secretion across the enteric nervous system."
  - target: 01-human/03-molecular/serotonin-transporter
    relation: modulated-by
    evidence: berger-2009-ssri
    note: "SERT (SLC6A4) terminates serotonergic neurotransmission by actively transporting 5-HT from the synapse into the presynaptic terminal; SSRI blockade of SERT increases synaptic 5-HT and mediates antidepressant effects."
  - target: 03-medicine/02-traditional/st-johns-wort
    relation: modulated-by
    note: "Modulated by St. John's Wort (Hypericum perforatum)."
  - target: 01-human/07-system/schizophrenia
    relation: connects-to
    note: "5-HT2A blockade in PFC by atypical antipsychotics (clozapine, olanzapine, risperidone) enhances dopaminergic output; 5-HT2A agonism by hallucinogens (LSD, psilocybin) models positive symptoms; serotonin-dopamine interaction shapes atypical antipsychotic efficacy."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "Reduced serotonergic tone is central to MDD; SSRIs (fluoxetine, sertraline, escitalopram) are first-line antidepressants; tryptophan depletion triggers relapse in remitted patients; 5-HT1A autoreceptor desensitization explains the 2-4 week delayed onset of antidepressant effect."
  - target: 01-human/03-molecular/cgrp
    relation: connects-to
    note: "Triptans (5-HT1B/D agonists) reduce trigeminal CGRP release and abort migraine; serotonin regulates CGRP release from TNC neurons; combining triptans with SSRIs carries a theoretical serotonin syndrome risk but is generally well-tolerated clinically."
  - target: 01-human/07-system/migraine
    relation: connects-to
    note: "Low interictal serotonin primes trigeminovascular sensitization in migraine; triptans (5-HT1B/D agonists) are first-line acute therapy; lasmiditan (5-HT1F ditan) provides relief without vasoconstriction; SSRIs may modestly reduce migraine frequency."
  - target: 01-human/07-system/bipolar-disorder
    relation: connects-to
    note: "SSRIs risk manic switching in bipolar disorder and are contraindicated as monotherapy; atypical antipsychotics with 5-HT2A blockade (quetiapine) effectively treat bipolar depression without switch risk; serotonergic antidepressants require mood stabilizer cover."
  - target: 01-human/07-system/obsessive-compulsive-disorder
    relation: connects-to
    note: "SSRIs at high doses are uniquely effective for OCD (vs. imipramine/desipramine which are ineffective); clomipramine (SRI-dominant TCA) has equivalent efficacy; 5-HT modulates OFC-striatal CSTC signaling; serotonergic augmentation of ERP therapy improves treatment outcomes."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "SSRIs (escitalopram, sertraline) and SNRIs (venlafaxine, duloxetine) are first-line GAD pharmacotherapy; buspirone (5-HT1A partial agonist) is a non-addictive alternative; serotonergic deficiency in amygdala-PFC circuits contributes to hypervigilance and pathological worry."
  - target: 01-human/07-system/panic-disorder
    relation: connects-to
    note: "SSRIs are first-line for panic disorder via raphe-amygdala serotonin modulation of the fear circuit; paradoxical jitteriness requires starting low; paroxetine and sertraline have strong evidence; clomipramine (5-HT/NE TCA) is highly effective but limited by side effects."
  - target: 01-human/07-system/social-anxiety-disorder
    relation: connects-to
    note: "Reduced SERT binding in amygdala and striatum in SAD; SSRIs (paroxetine, sertraline FDA-approved; escitalopram, venlafaxine XR evidence-based) are first-line pharmacotherapy; serotonergic modulation of amygdala reduces social threat hyperreactivity and improves social function."
  - target: 01-human/07-system/alcohol-use-disorder
    relation: connects-to
    note: "Reduced serotonin in AUD → disinhibition and impulsivity; 5-HT3 receptors in NAcc amplify dopamine reward; ondansetron (5-HT3 antagonist) has modest efficacy in early-onset AUD (≤25 years); SSRIs are ineffective in AUD without comorbid depression."
  - target: 01-human/07-system/insomnia-disorder
    relation: connects-to
    note: "Trazodone (5-HT2A antagonist + α1/H1 blocker) is the most prescribed off-label insomnia medication; 5-HT2A blockade shifts sleep architecture toward slow-wave sleep; raphe serotonin promotes wakefulness during day and transitions to sleep-onset at night."
  - target: 01-human/03-molecular/orexin
    relation: modulated-by
    note: "Orexin excites dorsal raphe serotonin neurons via OX2R → 5-HT → wakefulness and emotional arousal; serotonin reciprocally inhibits orexin neurons; sodium oxybate consolidates sleep in narcolepsy partly via complex serotonergic mechanisms."
  - target: 01-human/07-system/anorexia-nervosa
    relation: connects-to
    note: "5-HT2A receptor hyperactivation in PFC contributes to heightened harm avoidance and rigidity in AN; serotonin dysregulation persists after recovery; SSRIs are ineffective at low weight (insufficient tryptophan substrate); olanzapine (5-HT2A antagonist) modestly aids weight gain."
  - target: 01-human/07-system/borderline-personality-disorder
    relation: connects-to
    note: "5-HT2A and 5-HT1A dysregulation drive impulsivity and affective instability in BPD; reduced serotonin in amygdala and PFC reduces top-down inhibitory control; SSRIs reduce impulsive aggression in BPD; no FDA-approved medication for BPD but SSRIs used for comorbid depression."
  - target: 01-human/07-system/bulimia-nervosa
    relation: connects-to
    note: "Serotonin hypofunction in prefrontal-limbic circuits drives impulse control failure and binge episodes in BN; reduced 5-HT2C satiety signaling; fluoxetine 60 mg (FDA-approved for BN) reduces binge/purge frequency ~50% and is first-line pharmacotherapy."
  - target: 01-human/07-system/stimulant-use-disorder
    relation: connects-to
    note: "Cocaine blocks SERT → ↑ synaptic 5-HT in limbic circuits; MDMA reverses SERT → massive 5-HT/DA release → empathogenic effects; chronic MDMA causes SERT downregulation and serotonergic neurotoxicity; serotonergic modulation influences relapse in stimulant use disorder."
  - target: 01-human/07-system/ptsd
    relation: connects-to
    note: "SSRIs (sertraline, paroxetine) are FDA-approved for PTSD; 5-HT modulates vmPFC fear extinction; serotonin dysregulation contributes to PTSD hyperarousal, emotional numbing, and sleep disturbance; SNRIs (venlafaxine) also have good evidence for PTSD symptom reduction."
  - target: 01-human/07-system/gambling-disorder
    relation: connects-to
    note: "Serotonin hypofunction contributes to impulsivity and loss of behavioral inhibition in gambling disorder; 5-HT1B knockout mice show increased risk-taking; fluvoxamine and paroxetine showed modest efficacy in small trials; comorbid depression or OCD may respond to SSRIs."
  - target: 01-human/07-system/fibromyalgia
    relation: connects-to
    note: "Descending serotonergic inhibition from raphe nuclei to spinal dorsal horn is impaired in FM (low CSF 5-HIAA); duloxetine and amitriptyline restore descending inhibitory tone; 5-HT3 antagonist tropisetron reduces FM pain; 5-HT2A polymorphisms associate with FM susceptibility."
  - target: 01-human/03-molecular/substance-p
    relation: connects-to
    note: "Serotonin and substance P are co-expressed in raphe nuclei; descending 5-HT pathways gate spinal SP release (5-HT3 → SP excitation; 5-HT1A → SP inhibition); duloxetine's serotonergic component suppresses SP-driven central sensitization in chronic pain."
  - target: 01-human/07-system/internet-gaming-disorder
    relation: connects-to
    note: "Serotonin hypofunction contributes to impulsivity and compulsivity in IGD; 5-HT modulates OFC impulse control circuits; SSRIs show modest evidence for IGD with comorbid OCD or depression; impulsivity is a shared serotonin-related trait across behavioral addictions."
  - target: 01-human/07-system/binge-eating-disorder
    relation: connects-to
    note: "5-HT2C hypofunction reduces hypothalamic melanocortin satiety signaling in BED; SSRIs (fluoxetine 60mg) reduce binge frequency ~50%; lorcaserin (5-HT2C agonist, withdrawn) reduced binge eating; impaired 5-HT prefrontal inhibition drives loss-of-control eating."
  - target: 01-human/07-system/neuropathic-pain
    relation: connects-to
    note: "Descending serotonergic inhibition is impaired in neuropathic pain; duloxetine (SNRI) restores 5-HT/NE descending inhibition and is FDA-approved for diabetic neuropathy; 5-HT3 receptors facilitate dorsal horn pain; 5-HT3 antagonists do not improve neuropathic pain."
  - target: 01-human/07-system/narcolepsy
    relation: connects-to
    note: "SSRIs and SNRIs suppress cataplexy via monoamine reuptake inhibition reducing pontine REM-on circuit activity; clomipramine (potent SERT inhibitor) is highly effective for cataplexy; abrupt antidepressant discontinuation can precipitate status cataplecticus in narcolepsy."
  - target: 01-human/03-molecular/melatonin
    relation: modulates
    note: "Pineal gland serotonin (from TPH1) is directly converted to melatonin via AANAT (dark-activated by NE/β1/cAMP) then ASMT; serotonin daytime availability constrains nocturnal melatonin production; TPH inhibition or tryptophan depletion reduces melatonin synthesis capacity."
  - target: 01-human/03-molecular/prolactin
    relation: modulates
    note: "5-HT2A and 5-HT2B receptors on pituitary lactotrophs stimulate prolactin release; SSRI-induced serotonin excess causes galactorrhea in 2-5% of users; 5-HT-mediated prolactin elevation is a pharmacodynamic marker of brain serotonin activity."
---

# Serotonin

## Overview

Serotonin (5-hydroxytryptamine, 5-HT) is a **monoamine neurotransmitter, paracrine mediator, and vasoactive amine** that operates across radically different biological compartments simultaneously. It was first isolated from serum in 1948 by Rapport, Green, and Page [^rapport-1948-isolation], who named it for its vasoconstrictive activity — a name that belies the remarkable breadth of its roles in human physiology.

Contrary to its popular association with the brain, approximately **95% of the body's serotonin resides in the gastrointestinal tract**, synthesized and stored in **enterochromaffin (EC) cells** of the intestinal mucosa and in enteric neurons [^gershon-1999-gut-serotonin]. Only ~5% is found in the CNS, concentrated in **raphe nucleus neurons** that project widely to the limbic system, cortex, cerebellum, and brainstem. A third pool exists in **platelets**, which cannot synthesize 5-HT but take it up from portal blood via the serotonin transporter SERT and release it during aggregation.

This anatomical distribution — gut, brain, blood — means serotonin simultaneously orchestrates intestinal motility, emotional regulation, sleep architecture, and hemostasis. Its pharmacological manipulation, via **selective serotonin reuptake inhibitors (SSRIs)**, represents one of the most widely prescribed therapeutic interventions in modern medicine [^berger-2009-ssri].

## Structure

### Chemical identity

Serotonin is a **monoamine indoleamine**: it is derived from tryptophan and contains an indole ring system with a 5-hydroxy group and an ethylamine sidechain. Molecular formula: C₁₀H₁₂N₂O; molecular weight: 176.21 g/mol. It belongs to the monoamine family alongside dopamine, norepinephrine, epinephrine, and histamine, but is structurally distinguished by its indole (bicyclic) ring rather than a catechol core.

### Biosynthesis

Serotonin is synthesized in a two-step pathway from the essential amino acid **L-tryptophan**:

| Step | Enzyme | Cofactor | Product |
|:---|:---|:---|:---|
| 1 | **Tryptophan hydroxylase (TPH)** — rate-limiting | Tetrahydrobiopterin (BH₄), O₂ | 5-Hydroxytryptophan (5-HTP) |
| 2 | **Aromatic L-amino acid decarboxylase (AADC)** | Pyridoxal phosphate (B6) | **Serotonin (5-HT)** |

Two isoforms of TPH exist with distinct tissue distributions:
- **TPH1** (gene: *TPH1*, UniProt P17752) — expressed in enterochromaffin cells, pineal gland, and mast cells; synthesizes peripheral 5-HT
- **TPH2** (gene: *TPH2*) — expressed exclusively in CNS raphe neurons; responsible for all brain serotonin synthesis; *TPH2* variants are associated with depression and bipolar disorder

The blood-brain barrier is essentially impermeable to peripheral serotonin, making the central and peripheral pools functionally independent despite using the same biosynthetic machinery.

### Storage, release, and reuptake

Serotonin is packaged into vesicles by **VMAT1** (SLC18A1) in enterochromaffin cells and platelets, and by **VMAT2** (SLC18A2) in neurons. Reuptake from the synapse/extracellular space is mediated by the **serotonin transporter SERT** (SLC6A4), a Na⁺/Cl⁻-dependent transporter that is the definitive pharmacological target of SSRIs and SNRIs. Platelets express high levels of SERT and accumulate circulating 5-HT from portal blood; they do not synthesize it.

### Degradation

Primary catabolic pathway: **MAO-A** oxidatively deaminates 5-HT to **5-hydroxyindoleacetaldehyde**, which is further oxidized by aldehyde dehydrogenase to **5-hydroxyindoleacetic acid (5-HIAA)**. Urinary 5-HIAA is the standard biochemical marker of serotonin turnover; elevated 5-HIAA diagnoses carcinoid tumors secreting ectopic 5-HT. Low CSF 5-HIAA has been linked to suicidality and impulsive aggression.

In the **pineal gland**, 5-HT takes an alternative path: serotonin → N-acetylserotonin (by AANAT) → **melatonin** (by ASMT/HIOMT), linking serotonin to circadian rhythm regulation.

### Receptor subtypes

Serotonin signals through **14+ receptor subtypes** spanning six families (5-HT1–7). All are GPCRs except 5-HT3, which is a ligand-gated ion channel:

| Receptor | Coupling | Effect | Key locations | Pharmacological relevance |
|:---|:---|:---|:---|:---|
| **5-HT1A** | Gαi/o | ↓ cAMP; K⁺ channel opening | Raphe (autoreceptor), hippocampus, prefrontal cortex | Buspirone (partial agonist); antidepressant augmentation |
| **5-HT1B** | Gαi/o | ↓ cAMP | Basal ganglia, cerebral arteries (autoreceptor) | Triptans (migraines) |
| **5-HT2A** | Gαq | ↑ IP₃/DAG; excitatory | Prefrontal cortex, platelets, vascular smooth muscle | Hallucinogens (agonists); atypical antipsychotics (antagonists) |
| **5-HT2B** | Gαq | ↑ IP₃/DAG | Heart valves, GI | Cabergoline valve disease; ergot alkaloid toxicity |
| **5-HT3** | Ion channel (Na⁺/K⁺) | Rapid depolarization | Area postrema, GI enteric neurons, vagal afferents | Ondansetron (anti-emetic antagonist) |
| **5-HT4** | Gαs | ↑ cAMP | GI smooth muscle (intestinal peristalsis) | Prucalopride, cisapride (prokinetics) |
| **5-HT7** | Gαs | ↑ cAMP | Hypothalamus, thalamus, smooth muscle | Thermoregulation; circadian phase-shifting |

## Function

### Gastrointestinal: the enteric serotonin system

The GI tract is the body's primary serotonin organ [^gershon-1999-gut-serotonin]. Enterochromaffin cells — specialized epithelial sensory cells distributed throughout the intestinal mucosa — release 5-HT in response to mechanical distension, mucosal irritants, and luminal chemistry. Released 5-HT acts on:

- **5-HT4 receptors** on enteric neurons → ascending excitation and descending inhibition → **peristaltic reflex** (coordinated propulsive contractions)
- **5-HT3 receptors** on vagal afferents and area postrema → **nausea and vomiting signals**; ondansetron blocks 5-HT3 to suppress chemotherapy-induced emesis
- **5-HT1P receptors** on enteric neurons → modulate secretomotor reflexes

Disruption of enteric serotonin signaling underlies symptoms in **irritable bowel syndrome (IBS)**: altered SERT expression and EC cell density are documented in IBS-D (diarrhea-predominant) and IBS-C (constipation-predominant) subtypes.

### CNS: mood, sleep, and cognition

Raphe nucleus neurons provide **diffuse modulatory innervation** to virtually the entire CNS. Serotonin does not simply convey point-to-point signals — it sets a global "tone" that scales the responsiveness of cortical and limbic circuits:

- **Mood and emotional regulation**: 5-HT1A/2A balance in prefrontal cortex and amygdala shapes fear, anxiety, and affective valence. Reduced raphe 5-HT firing correlates with depressed mood states.
- **Sleep architecture**: 5-HT promotes wakefulness (raphe neurons are active during waking, quiescent in sleep); the 5-HT → melatonin conversion in the pineal gland links serotonin to circadian timing.
- **Appetite**: 5-HT2C activation in the hypothalamic arcuate nucleus suppresses food intake; fenfluramine and lorcaserin exploited this (the latter withdrawn for cardiac concerns).
- **Cognition and memory**: 5-HT modulates hippocampal neurogenesis and synaptic plasticity; 5-HT4 agonism enhances learning.
- **Thermoregulation**: 5-HT7 in the hypothalamus and spinal cord participates in core temperature control; serotonin syndrome produces hyperthermia partly through 5-HT1A/2A overactivation.

### Platelets: amplification of hemostasis

Platelets express SERT and accumulate serotonin from portal blood. Upon platelet activation (ADP, collagen, thrombin), granule-stored 5-HT is released and acts on **5-HT2A receptors on adjacent platelets**, amplifying ADP-induced aggregation via Gαq → IP₃ → Ca²⁺ signaling. 5-HT also causes vasoconstriction (5-HT2A on vascular smooth muscle), contributing to hemostatic vasoconstriction at wound sites.

## Mechanism

### SERT-mediated reuptake and SSRI pharmacology

SERT (SLC6A4) terminates serotonergic signaling by co-transporting one 5-HT, one Na⁺, and one Cl⁻ into the presynaptic terminal, using the Na⁺ gradient as the driving force. **SSRIs** — fluoxetine, sertraline, escitalopram, paroxetine — competitively block the extracellular 5-HT binding site on SERT, prolonging 5-HT dwell time in the synapse. Therapeutic effect requires sustained upregulation (weeks), partly because initial SSRI treatment also activates presynaptic 5-HT1A autoreceptors, blunting firing; desensitization of these autoreceptors with chronic use is required for full antidepressant effect.

**SNRIs** (venlafaxine, duloxetine) additionally block the norepinephrine transporter (NET). **MAOIs** inhibit 5-HT degradation upstream. Combining SSRI + MAOI risks fatal **serotonin syndrome** (see Pathology).

### 5-HT2A signaling and hallucinogens

5-HT2A (Gαq-coupled) in the prefrontal cortex mediates the psychedelic effects of psilocybin, LSD, and DMT — all of which are 5-HT2A partial agonists. Activation → ↑IP₃ → IP₃R-mediated ER Ca²⁺ release and downstream ERK/β-arrestin signaling. The biased agonism profile (G-protein vs. β-arrestin signaling) is increasingly linked to therapeutic vs. hallucinogenic effects, driving next-generation psychedelic drug design.

### Gut-brain axis serotonin signaling

Peripheral 5-HT cannot cross the blood-brain barrier, yet peripheral serotonin signaling influences CNS function indirectly via the **vagus nerve**: EC-cell-released 5-HT activates 5-HT3 on mucosal vagal afferents → sensory signals ascend to the nucleus tractus solitarius → influence on brainstem and limbic circuits. This gut-to-brain pathway is one mechanism through which the intestinal microbiome modulates mood (tryptophan availability and EC cell activity are microbially regulated).

## Connections

- `expressed-by` → **enterochromaffin-cell** — ~95% of body 5-HT synthesized in GI mucosa (forward ref; entry pending)
- `expressed-by` → **neuron** — CNS serotonin from raphe nucleus dopaminergic neurons; TPH2 isoform
- `modulated-by` → **ssri** — SSRIs block SERT to increase synaptic 5-HT; first-line antidepressants (forward ref; entry pending)
- `modulates` → **[nervous-system](../../07-system/nervous-system/README.md)** — mood, sleep, appetite, cognition, thermoregulation
- `modulates` → **[digestive-system](../../07-system/digestive-system/README.md)** — peristalsis, nausea, secretion via enteric nervous system
- `connects-to` → **[Schizophrenia](../../07-system/schizophrenia/README.md)** — 5-HT2A blockade in PFC by atypical antipsychotics (clozapine, olanzapine, risperidone) enhances dopaminergic output; 5-HT2A agonism by hallucinogens (LSD, psilocybin) models positive symptoms; serotonin-dopamine interaction shapes atypical antipsychotic efficacy.
- `connects-to` → **[CGRP](../cgrp/README.md)** — triptans (5-HT1B/D agonists) reduce trigeminal CGRP release and abort migraine; serotonin regulates CGRP release from TNC neurons; combining triptans with SSRIs carries a theoretical serotonin syndrome risk but is generally well-tolerated clinically.
- `connects-to` → **[Migraine](../../07-system/migraine/README.md)** — low interictal serotonin primes trigeminovascular sensitization in migraine; triptans (5-HT1B/D agonists) are first-line acute therapy; lasmiditan (5-HT1F ditan) provides relief without vasoconstriction; SSRIs may modestly reduce migraine frequency.
- `connects-to` → **[Bipolar Disorder](../../07-system/bipolar-disorder/README.md)** — SSRIs risk manic switching in bipolar disorder and are contraindicated as monotherapy; atypical antipsychotics with 5-HT2A blockade (quetiapine) treat bipolar depression without switch risk; serotonergic antidepressants require mood stabilizer cover.
- `connects-to` → **[Obsessive-Compulsive Disorder](../../07-system/obsessive-compulsive-disorder/README.md)** — SSRIs at high doses are uniquely effective for OCD (vs. imipramine/desipramine which are ineffective), establishing a privileged role for 5-HT; clomipramine (SRI-dominant TCA) has equivalent efficacy; 5-HT modulates OFC-striatal CSTC circuit; 8-12 weeks at maximum dose required.
- `connects-to` → **[Generalized Anxiety Disorder](../../07-system/generalized-anxiety-disorder/README.md)** — SSRIs (escitalopram, sertraline) and SNRIs (duloxetine, venlafaxine) are first-line GAD pharmacotherapy; buspirone (5-HT1A partial agonist) is a non-addictive alternative; serotonergic deficiency in amygdala-PFC circuits contributes to hypervigilance and pathological worry.
- `connects-to` → **[Panic Disorder](../../07-system/panic-disorder/README.md)** — SSRIs are first-line for panic disorder via raphe-amygdala serotonin modulation of the fear circuit; paradoxical jitteriness in initial weeks requires starting low and titrating slowly; paroxetine and sertraline have strong evidence; clomipramine (5-HT/NE TCA) is highly effective.
- `connects-to` → **[Social Anxiety Disorder](../../07-system/social-anxiety-disorder/README.md)** — reduced SERT binding in amygdala and striatum in SAD; SSRIs (paroxetine, sertraline FDA-approved; escitalopram, venlafaxine XR evidence-based) are first-line; serotonergic modulation of amygdala reduces social threat hyperreactivity and improves social approach.
- `connects-to` → **[Alcohol Use Disorder](../../07-system/alcohol-use-disorder/README.md)** — reduced serotonin in AUD → disinhibition and impulsivity; 5-HT3 receptors in NAcc amplify dopamine reward; ondansetron (5-HT3 antagonist) has modest efficacy in early-onset AUD; SSRIs are ineffective in AUD without comorbid depression.
- `connects-to` → **[Insomnia Disorder](../../07-system/insomnia-disorder/README.md)** — trazodone (5-HT2A antagonist + α1/H1 blocker) is the most commonly prescribed off-label insomnia medication; 5-HT2A blockade shifts sleep architecture toward slow-wave sleep; raphe serotonin promotes wakefulness during day and transitions at sleep onset.
- `modulated-by` → **[Orexin](../orexin/README.md)** — orexin excites dorsal raphe serotonin neurons via OX2R → 5-HT → wakefulness and emotional arousal; serotonin reciprocally inhibits orexin neurons; sodium oxybate (narcolepsy) consolidates sleep partly via serotonergic mechanisms.
- `connects-to` → **[Anorexia Nervosa](../../07-system/anorexia-nervosa/README.md)** — 5-HT2A receptor hyperactivation in PFC contributes to heightened harm avoidance and rigidity in AN; serotonin dysregulation persists after recovery; SSRIs are ineffective at low weight (insufficient tryptophan substrate); olanzapine (5-HT2A antagonist) modestly aids weight gain.
- `connects-to` → **[Borderline Personality Disorder](../../07-system/borderline-personality-disorder/README.md)** — 5-HT2A and 5-HT1A dysregulation drive impulsivity and affective instability in BPD; reduced serotonin in amygdala and PFC reduces top-down inhibitory control; SSRIs reduce impulsive aggression in BPD; no FDA-approved medication for BPD but SSRIs used for comorbid depression.
- `connects-to` → **[Bulimia Nervosa](../../07-system/bulimia-nervosa/README.md)** — serotonin hypofunction in prefrontal-limbic circuits drives impulse control failure and binge episodes in BN; reduced 5-HT2C satiety signaling; fluoxetine 60 mg (FDA-approved, highest SSRI dose for any indication) reduces binge/purge frequency ~50% and is first-line BN pharmacotherapy.
- `connects-to` → **[Stimulant Use Disorder](../../07-system/stimulant-use-disorder/README.md)** — cocaine blocks SERT → ↑ synaptic 5-HT in limbic circuits; MDMA reverses SERT → massive 5-HT/DA release → empathogenic effects; chronic MDMA causes SERT downregulation and serotonergic neurotoxicity; serotonergic modulation influences relapse vulnerability in stimulant use disorder.

- `connects-to` → **[PTSD](../../07-system/ptsd/README.md)** — SSRIs (sertraline, paroxetine) are FDA-approved for PTSD; 5-HT modulates vmPFC fear extinction; serotonin dysregulation contributes to PTSD hyperarousal, emotional numbing, and sleep disturbance; SNRIs (venlafaxine) also have good evidence for PTSD symptom reduction.
- `connects-to` → **[Gambling Disorder](../../07-system/gambling-disorder/README.md)** — serotonin hypofunction contributes to impulsivity and loss of behavioral inhibition in gambling disorder; 5-HT1B knockout mice show increased risk-taking; fluvoxamine and paroxetine showed modest efficacy in small RCTs; SSRIs are more effective in gambling disorder comorbid with depression or OCD.
- `connects-to` → **[Fibromyalgia](../../07-system/fibromyalgia/README.md)** — descending serotonergic inhibition from raphe nuclei to spinal dorsal horn is impaired in FM (reduced CSF 5-HIAA); duloxetine (SNRI) and amitriptyline (TCA) restore descending inhibitory tone and reduce pain; 5-HT3 antagonist tropisetron reduces FM pain in small RCTs; 5-HT2A receptor polymorphisms associate with FM susceptibility.
- `connects-to` → **[Substance P](../substance-p/README.md)** — serotonin and substance P are co-expressed in raphe nuclei and co-released at pain-modulating synapses; 5-HT3 receptors on dorsal horn neurons facilitate SP release (pronociceptive); 5-HT1A/1B receptors inhibit SP release (antinociceptive); duloxetine exploits serotonergic suppression of SP-driven central sensitization.
- `connects-to` → **[Internet Gaming Disorder](../../07-system/internet-gaming-disorder/README.md)** — serotonin hypofunction contributes to impulsivity and compulsive behavior in IGD; 5-HT modulates OFC-PFC impulse control circuits that are hypoactive in IGD; SSRIs have modest evidence for IGD when driven by comorbid depression or OCD; impulsivity is a core serotonin-linked risk trait across behavioral addictions.
- `connects-to` → **[Binge Eating Disorder](../../07-system/binge-eating-disorder/README.md)** — 5-HT2C receptor hypofunction reduces hypothalamic melanocortin satiety signaling in BED, allowing binge episodes to continue beyond caloric need; fluoxetine 60 mg reduces binge frequency ~50% (off-label); SSRIs are more effective in BED with comorbid depression; impaired serotonergic PFC inhibition drives loss-of-control eating.
- `connects-to` → **[Neuropathic Pain](../../07-system/neuropathic-pain/README.md)** — descending serotonergic inhibition from raphe to spinal dorsal horn is impaired in neuropathic pain states; duloxetine (SNRI) restores 5-HT/NE descending inhibitory tone and is FDA-approved for diabetic peripheral neuropathy; 5-HT3 receptors on dorsal horn neurons facilitate pain transmission and are not a useful analgesic target.
- `connects-to` → **[Narcolepsy](../../07-system/narcolepsy/README.md)** — SSRIs and SNRIs suppress cataplexy via monoamine reuptake inhibition reducing pontine REM-on circuit activity; clomipramine (potent SERT inhibitor) is the most effective anticataplectic antidepressant; abrupt discontinuation can precipitate status cataplecticus; sodium oxybate consolidates sleep partly via complex serotonergic mechanisms.
- `modulates` → **[Melatonin](../melatonin/README.md)** — pineal serotonin (synthesized by TPH1) is the direct substrate for melatonin synthesis: AANAT (dark-activated via NE/β1/cAMP from the superior cervical ganglion) converts serotonin → N-acetylserotonin; ASMT methylates it to melatonin; daytime serotonin availability constrains nocturnal melatonin production — tryptophan depletion and TPH inhibition reduce melatonin output.
- `modulates` → **[Prolactin](../prolactin/README.md)** — 5-HT2A and 5-HT2B receptors on pituitary lactotrophs stimulate prolactin release; SSRI-induced serotonin excess causes galactorrhea in 2-5% of users; 5-HT-mediated prolactin elevation is a pharmacodynamic marker of CNS serotonin activity, used in neuroendocrine challenge tests.

## Pathology

| Condition | Mechanism | Clinical implication |
|:---|:---|:---|
| **Major depressive disorder** | Reduced 5-HT neurotransmission (complex; RAT/5-HT1A desensitization) | SSRIs, SNRIs, MAOIs; ketamine/ECT for treatment-resistant cases |
| **Anxiety disorders** | Altered 5-HT1A/2A balance; amygdala hyperactivity | SSRIs first-line; 5-HT1A partial agonists (buspirone) |
| **Serotonin syndrome** | Excess 5-HT activity (SSRI + MAOI; SSRI + tramadol; overdose) → triad: altered mental status, autonomic instability, neuromuscular abnormalities (clonus, hyperreflexia) | Cyproheptadine (5-HT2A antagonist); benzodiazepines; supportive; SSRI+MAOI combination is potentially lethal |
| **Carcinoid tumor** | EC cell neoplasm secretes excess 5-HT → flushing, diarrhea, bronchospasm, right-sided valvular disease (5-HT2B) | Octreotide; urinary 5-HIAA diagnosis |
| **IBS** | Altered EC cell density and SERT expression → abnormal GI motility | 5-HT4 agonists (prucalopride, IBS-C); 5-HT3 antagonists (alosetron, IBS-D) |
| **Migraine** | Trigeminovascular 5-HT1B/1D/1F signaling | Triptans (5-HT1B/1D agonists); CGRP antagonists |
| **Depression genetics** | TPH2 variants; SLC6A4 promoter polymorphism (5-HTTLPR) | Pharmacogenetic SSRI response prediction |

[^rapport-1948-isolation]: Rapport MM, Green AA, Page IH. Serum vasoconstrictor (serotonin) IV. Isolation and characterization. *J Biol Chem.* 1948;176(3):1243-51. [PubMed 18887360](https://pubmed.ncbi.nlm.nih.gov/18887360/)
[^berger-2009-ssri]: Berger M, Gray JA, Roth BL. The expanded biology of serotonin. *Annu Rev Med.* 2009;60:355-66. [doi:10.1146/annurev.med.60.042307.110802](https://doi.org/10.1146/annurev.med.60.042307.110802)
[^gershon-1999-gut-serotonin]: Gershon MD. The enteric nervous system: a second brain. *Hosp Pract (1995).* 1999;34(7):31-42. [PubMed 10090070](https://pubmed.ncbi.nlm.nih.gov/10090070/)
