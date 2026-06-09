---
schema: human-scale-entry/v1
id: norepinephrine
name: Norepinephrine
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-05
summary: "Catecholamine (MW 169.18), immediate Epi precursor and primary sympathetic postganglionic neurotransmitter. Activates α₁, α₂, β₁ adrenergic receptors. Locus coeruleus projects modulate CNS arousal. NET reuptake targeted by TCAs, SNRIs, cocaine, atomoxetine."
aliases: ["noradrenaline", "NE", "NA", "levarterenol", "norepinephrinum"]
sources:
  - id: stryer-biochemistry
    type: textbook
    cite: "Berg JM, Tymoczko JL, Stryer L. Biochemistry. 9th ed. W.H. Freeman; 2019."
    url: "https://www.macmillanlearning.com/college/us/product/Biochemistry/p/131911467X"
    accessed: "2026-06-05"
  - id: alberts-mol-cell-biology
    type: textbook
    cite: "Alberts B, Johnson A, Lewis J, et al. Molecular Biology of the Cell. 7th ed. W.W. Norton; 2022."
    url: "https://www.ncbi.nlm.nih.gov/books/NBK26880/"
    accessed: "2026-06-05"
cross_links:
  - target: 01-human/03-molecular/beta1-adrenergic-receptor
    relation: modulates
    note: "Norepinephrine is the primary endogenous agonist of β₁AR on cardiomyocytes (Gs→cAMP→PKA); activates SA node, ↑HR, ↑AV conduction, ↑ventricular contractility; maintains sympathetic tone."
  - target: 01-human/07-system/nervous-system
    relation: modulates
    note: "Locus coeruleus NE neurons project to entire CNS modulating arousal, attention, fear, and autonomic tone; LC hyperactivation in PTSD/anxiety; α₂ agonists (clonidine) suppress LC for opioid withdrawal."
  - target: 01-human/07-system/cardiovascular-system
    relation: modulates
    note: "NE is the principal sympathetic vasoconstrictor — activates vascular smooth muscle α₁AR → ↑peripheral resistance; maintains basal vascular tone; IV NE (vasopressor) used in septic shock."
  - target: 01-human/03-molecular/dopamine
    relation: modulated-by
    note: "Norepinephrine is synthesised from dopamine by DβH in synaptic vesicles; the DA:NE ratio in sympathetic terminals is governed by DβH activity and vesicular transport capacity."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "NE deficit via locus coeruleus-PFC projection underlies psychomotor retardation in MDD; SNRIs (venlafaxine, duloxetine) and TCAs block NET; mirtazapine raises NE via α2 autoreceptor blockade; melancholic depression preferentially responds to NE-targeting antidepressants."
  - target: 01-human/07-system/ptsd
    relation: connects-to
    note: "Locus coeruleus hyperactivation in PTSD → excess NE → amygdala hyperreactivity, hyperarousal, and intrusive re-experiencing; prazosin (α1 antagonist) reduces NE-driven nightmares; propranolol may reduce fear memory reconsolidation when given acutely after trauma."
  - target: 01-human/07-system/attention-deficit-hyperactivity-disorder
    relation: connects-to
    note: "NE α2A-receptor signaling in PFC strengthens layer III pyramidal neuron connectivity underlying working memory; atomoxetine (selective NE reuptake inhibitor) and guanfacine/clonidine (α2A agonists) treat ADHD by restoring NE-PFC function without dopamine-reward circuit effects."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "Locus coeruleus NE hyperactivity drives sympathetic arousal, hypervigilance, and somatic anxiety symptoms in GAD; SNRIs (duloxetine, venlafaxine) treat GAD via dual NE + 5-HT reuptake inhibition; propranolol reduces peripheral β-adrenergic anxiety manifestations."
  - target: 01-human/07-system/panic-disorder
    relation: connects-to
    note: "LC hyperactivation in panic disorder drives tachycardia, chest tightness, and hyperarousal via α1-NE stimulation in amygdala; yohimbine (α2 antagonist) reliably provokes panic in PD patients; propranolol reduces somatic symptoms; clonidine reduces LC firing and hyperarousal."
  - target: 01-human/07-system/social-anxiety-disorder
    relation: connects-to
    note: "Adrenergic surge in social situations causes blushing, tremor, and sweating; propranolol (β1 antagonist) reduces somatic performance anxiety; NE amplifies amygdala reactivity to social threat; venlafaxine XR (SNRI) addresses both NE hyperarousal and serotonin dysregulation."
---

# Norepinephrine

## Overview

Norepinephrine (noradrenaline, NE) is a catecholamine neurotransmitter and hormone (MW 169.18 Da) that serves as the **primary neurotransmitter of sympathetic postganglionic neurons** throughout the body, and as a major neuromodulator in the CNS via projections from the **locus coeruleus (LC)** — the largest noradrenergic nucleus in the brain (A6 group, pontine brainstem).[^stryer-biochemistry] NE is also the immediate biosynthetic precursor of epinephrine. It acts predominantly at α₁ (vasoconstriction), α₂ (autoreceptor/presynaptic inhibition), and β₁ (cardiac stimulation) adrenergic receptors, with much weaker β₂ activity than epinephrine. Peripherally, NE maintains basal vascular tone and blood pressure; centrally, it modulates arousal, attention, fear circuits, and autonomic state.[^alberts-mol-cell-biology]

## Structure

Norepinephrine is structurally identical to epinephrine except it bears a **primary amine** (NH₂) rather than a secondary N-methyl amine. This single difference reduces β₂ receptor affinity substantially and is exploited pharmacologically (terbutaline, salbutamol: selective β₂ agonists with bulky N-substituents).

- **Catechol nucleus** (3,4-dihydroxybenzene): essential for receptor binding; catechol-O-methyltransferase (COMT) methylates the 3-OH in catabolism → normetanephrine.
- **Benzylic chiral centre** (R-configuration in natural L-NE): stereoselective receptor binding; synthetic racemic mixtures are less potent.
- **Primary amine** at the β-carbon: higher α₁ and lower β₂ selectivity compared to Epi.

NE is stored in **dense-core synaptic vesicles** (in sympathetic terminals) or **large dense-core granules** (in adrenal medulla) co-packaged with chromogranin A, ATP, and neuropeptide Y.[^stryer-biochemistry]

## Function

### Adrenergic Receptor Profile of NE

| Receptor | Signalling | Key tissue | Effect |
|----------|-----------|-----------|--------|
| α₁ | Gq → IP3/DAG → ↑Ca²⁺ | Arteriolar smooth muscle | Vasoconstriction → ↑TPR → ↑BP |
| α₂A/B | Gi → ↓cAMP | Presynaptic NE terminals (autoreceptor); CNS | ↓NE release; sedation/analgesia |
| α₂C | Gi | Adrenal medulla, brain | ↓Epi release, modulates stress |
| β₁ | Gs → ↑cAMP → PKA | SA node, AV node, ventricle, kidney | ↑HR, ↑inotropy, ↑renin |
| β₂ | Gs | Bronchi, skeletal muscle vessels | Minimal (NE weak β₂ agonist) |

The **net cardiovascular effect of IV NE** is ↑ peripheral resistance (α₁) + ↑ contractility (β₁), but ↑BP triggers the **baroreflex** → ↑ vagal tone → reflex bradycardia, partially counteracting the direct β₁ effect on heart rate.

### CNS Locus Coeruleus Projections

The LC's ~15,000–50,000 noradrenergic neurons (bilateral) project to virtually every brain region:[^alberts-mol-cell-biology]
- **Prefrontal cortex**: attention, working memory, executive control (inverted-U: optimal NE tone; excess or deficit impairs PFC)
- **Hippocampus**: memory consolidation, LTP (β₁/β₂ → cAMP → CREB)
- **Amygdala**: fear encoding and extinction; LC burst-firing during threat → ↑ amygdala NE → fear memory formation
- **Cerebellum**: motor coordination
- **Spinal cord**: descending pain modulation (α₂ → analgesic effect; exploited by clonidine intrathecally)
- **Arousal/wakefulness**: LC is tonically active during wakefulness, silent during REM sleep

## Mechanism

### Biosynthesis

NE is synthesised in sympathetic nerve terminals and LC neurons via the **Blaschko pathway** up to the DβH step:[^stryer-biochemistry]

```
L-Tyrosine
     ↓  TH (tyrosine hydroxylase) — RATE-LIMITING; BH4/Fe²⁺/O₂; inhibited by end-product NE
L-DOPA
     ↓  AADC (aromatic L-amino acid decarboxylase / DOPA decarboxylase; PLP cofactor)
Dopamine (transported into vesicle by VMAT2/SLC18A2)
     ↓  DβH (dopamine β-hydroxylase) — INTRA-VESICULAR; Cu²⁺/ascorbate/O₂
Norepinephrine
```

In adrenal medulla chromaffin cells, NE is further methylated to epinephrine by cytosolic PNMT. In sympathetic neurons and LC, the pathway stops at NE (no PNMT expression).[^stryer-biochemistry]

**TH regulation**: TH is the rate-limiting enzyme; it is allosterically inhibited by catecholamines (product inhibition); phosphorylated (activated) by PKA (Ser40), CaMKII (Ser19), and MAPKAPK (Ser31) during neural activity — coupling biosynthesis to demand.

### Vesicular Storage and Release

NE (synthesised in vesicle lumen by DβH) is stored in vesicles by **VMAT2 (SLC18A2)**, driven by the vesicular H⁺-ATPase proton gradient. Synaptic vesicles at sympathetic terminals release NE at **varicose en-passant boutons** onto smooth muscle, cardiac cells, and glands — a form of **volume transmission** (paracrine, not point-to-point).[^alberts-mol-cell-biology]

Action potential → Cav2.2 (N-type VGCC) Ca²⁺ influx → SNARE-mediated exocytosis → NE into synaptic cleft or perivascular space.

### Termination: NET Reuptake

**NET (norepinephrine transporter, SLC6A2)** is the primary signal termination mechanism — responsible for ~80–90% of released NE reuptake into the presynaptic terminal:
- Na⁺/Cl⁻-dependent secondary active transporter (1 Na⁺ + 1 Cl⁻ co-transported per NE molecule)
- High affinity (Km ~0.5 µM), selective for NE > Epi > DA
- Pharmacological targets:[^stryer-biochemistry]

| Drug | NET action | Clinical use |
|------|-----------|-------------|
| Tricyclic antidepressants (imipramine, amitriptyline, nortriptyline) | Non-selective NET + SERT block | Depression, neuropathic pain |
| SNRIs (duloxetine, venlafaxine, desvenlafaxine) | NET + SERT block | Depression, anxiety, fibromyalgia, diabetic neuropathy |
| Atomoxetine | Selective NET block | ADHD (↑ prefrontal NE/DA) |
| Cocaine | NET + SERT + DAT block | Drug of abuse (↑ extracellular DA, NE) |
| Amphetamines | NET reverse transport (efflux) | ADHD, narcolepsy |
| Reboxetine | Selective NET block | Depression (Europe) |

Reuptaken NE is either recycled into vesicles (VMAT2) or metabolised by **MAO-A** (mitochondrial) → DHPG → VMA (peripheral) or MHPG (CNS).[^alberts-mol-cell-biology]

### Autoreceptor Feedback (α₂A)

α₂A autoreceptors on presynaptic NE terminals detect extracellular NE → Gi → ↓cAMP → ↓vesicle fusion probability → feedback inhibition of NE release. This circuit prevents NE overflow and limits sympathetic activation. **Clonidine** and **dexmedetomidine** are α₂ agonists that exploit this mechanism for sedation/analgesia and sympatholysis.

### Catabolism

```
NE
 ├─ MAO-A (mitochondria) → DHPG → DOMA → VMA (peripheral tissues, urine)
 ├─ COMT (cytosol, SAM) → Normetanephrine → MHPG (CNS, CSF) / VMA (urine)
 └─ Combined → VMA (vanillylmandelic acid, major urinary metabolite)
```

24h urinary normetanephrine and VMA are diagnostic markers for phaeochromocytoma/paraganglioma.[^stryer-biochemistry]

## Connections

- **Modulates beta1-adrenergic-receptor** — Norepinephrine is the primary endogenous agonist of β₁AR on cardiomyocytes (Gs→cAMP→PKA); activates SA node, ↑HR, ↑AV conduction, ↑ventricular contractility; maintains sympathetic tone. See [beta1-adrenergic-receptor](../beta1-adrenergic-receptor/README.md).
- **Modulates nervous system** — Locus coeruleus NE neurons project to entire CNS modulating arousal, attention, fear, and autonomic tone; LC hyperactivation in PTSD/anxiety; α₂ agonists (clonidine) suppress LC for opioid withdrawal. See [nervous-system](../../07-system/nervous-system/README.md).
- `connects-to` → **[ADHD](../../07-system/attention-deficit-hyperactivity-disorder/README.md)** — NE α2A-receptor signaling in PFC strengthens layer III pyramidal neuron connectivity underlying working memory and attention; atomoxetine (selective NE reuptake inhibitor) and guanfacine/clonidine (α2A agonists) treat ADHD by restoring NE-PFC function without engaging dopamine-reward circuits.
- `connects-to` → **[Generalized Anxiety Disorder](../../07-system/generalized-anxiety-disorder/README.md)** — locus coeruleus NE hyperactivity drives sympathetic arousal, hypervigilance, and somatic anxiety in GAD; SNRIs (duloxetine, venlafaxine) treat GAD via dual NE + 5-HT reuptake inhibition; propranolol reduces peripheral β-adrenergic anxiety manifestations.
- `connects-to` → **[Panic Disorder](../../07-system/panic-disorder/README.md)** — LC hyperactivation drives tachycardia, chest tightness, and hyperarousal via α1-NE stimulation in amygdala; yohimbine (α2 antagonist) reliably provokes panic attacks in PD patients; propranolol reduces somatic symptoms; clonidine reduces LC firing.
- `connects-to` → **[Social Anxiety Disorder](../../07-system/social-anxiety-disorder/README.md)** — adrenergic surge in social situations causes blushing, tremor, and sweating; propranolol (β1 antagonist) reduces somatic performance anxiety; NE amplifies amygdala reactivity to social threat; venlafaxine XR (SNRI) addresses both NE hyperarousal and serotonin dysregulation.
- **Modulates cardiovascular system** — NE is the principal sympathetic vasoconstrictor — activates vascular smooth muscle α₁AR → ↑peripheral resistance; maintains basal vascular tone; IV NE (vasopressor) used in septic shock. See [cardiovascular-system](../../07-system/cardiovascular-system/README.md).
- **Modulated by dopamine** — Norepinephrine is synthesised from dopamine by DβH in synaptic vesicles; the DA:NE ratio in sympathetic terminals is governed by DβH activity and vesicular transport capacity. See [dopamine](../dopamine/README.md).

## Pathology

### Major Depressive Disorder — Norepinephrine Hypothesis
Reduced NE signalling in the **prefrontal cortex and anterior cingulate** underlies anhedonia, loss of motivation, impaired concentration, and fatigue (separate from the serotonin hypothesis). Evidence: tricyclic antidepressants (which block NET) are effective; reserpine (depletes catecholamines) can precipitate depression. SNRIs and TCAs restore NE by blocking NET reuptake.[^alberts-mol-cell-biology]

### Post-Traumatic Stress Disorder (PTSD)
LC hyperactivation after trauma → chronically elevated NE in amygdala → enhanced fear memory consolidation, hypervigilance, and intrusive memories. **Prazosin** (α₁ antagonist) reduces NE-mediated nightmares. **Clonidine/lofexidine** (α₂ agonist) suppress LC firing → reduce hyperarousal symptoms.[^stryer-biochemistry]

### ADHD — Prefrontal NE Deficiency
Optimal NE (and dopamine) signalling through α₂A receptors in the prefrontal cortex supports sustained attention and working memory. Insufficient noradrenergic tone → distractibility, impulsivity. **Atomoxetine** (selective NET inhibitor) and **guanfacine/clonidine** (α₂A agonists, stimulate postsynaptic receptors) are non-stimulant ADHD treatments.[^alberts-mol-cell-biology]

### Opioid Withdrawal
Chronic opioid receptor activation suppresses LC activity (μ-opioid → Gi → ↓cAMP). Abrupt opioid cessation → LC rebound hyperactivation → excessive NE → anxiety, piloerection, diaphoresis, tachycardia, hypertension, diarrhoea, abdominal cramping. **Clonidine/lofexidine** (α₂ agonists) reduce LC firing rate → suppress withdrawal symptoms.

### Phaeochromocytoma / Paraganglioma
Catecholamine-secreting tumours of chromaffin cell origin. NE-dominant phaeochromocytomas (vs Epi-dominant): classically **sustained** rather than paroxysmal hypertension; normetanephrine elevated in plasma/urine. Management identical to Epi-dominant (alpha-block then surgery).

### Septic Shock
IV norepinephrine is the **first-line vasopressor** in septic shock (surviving sepsis campaign guidelines): restores vascular α₁AR-mediated tone → ↑mean arterial pressure → organ perfusion. Targets: MAP ≥65 mmHg. Adjuncts: vasopressin (V1R), epinephrine if refractory.

### Parkinson's Disease — Non-Motor Features
Locus coeruleus degeneration (often precedes substantia nigra loss, Braak stage 2) → noradrenergic deficiency → depression, autonomic dysfunction, REM sleep behaviour disorder, cognitive impairment. Loss of LC NE → reduced resilience to neuroinflammation (NE has anti-inflammatory effects on microglia via β-adrenergic receptors).

### Multiple System Atrophy (MSA)
α-Synuclein oligodendrocytic inclusions affect sympathetic ganglia and LC → severe autonomic failure + cerebellar/parkinsonian features; orthostatic hypotension from loss of postganglionic NE terminals.

## See Also

- [Epinephrine](../epinephrine/README.md) — downstream product of NE via PNMT in adrenal medulla
- [Dopamine](../dopamine/README.md) — biosynthetic precursor of NE; distinct CNS reward circuits
- [Beta1-Adrenergic Receptor](../beta1-adrenergic-receptor/README.md) — primary cardiac and renal receptor
- [Glucocorticoid Receptor](../glucocorticoid-receptor/README.md) — TH (NE biosynthesis rate-limiting step) is stress-regulated
- [Cortisol](../cortisol/README.md) — stress co-response with NE/Epi; also regulates TH expression
- [Serotonin](../serotonin/README.md) — parallel monoamine modulator; SNRIs affect both SERT + NET
- [Serotonin Transporter](../serotonin-transporter/README.md) — structural and functional homolog of NET (SLC6 family)
- [Cardiovascular System](../../07-system/cardiovascular-system/README.md) — primary peripheral target
- [Nervous System](../../07-system/nervous-system/README.md) — LC-NE modulation of CNS state
- [Beta-blockers](../../../03-medicine/01-modern/04-cardio/beta-blockers/README.md) — pharmacologically antagonise NE at β₁AR in heart

[^stryer-biochemistry]: Berg JM, Tymoczko JL, Stryer L. *Biochemistry*. 9th ed. W.H. Freeman; 2019.
[^alberts-mol-cell-biology]: Alberts B, Johnson A, Lewis J, et al. *Molecular Biology of the Cell*. 7th ed. W.W. Norton; 2022.
