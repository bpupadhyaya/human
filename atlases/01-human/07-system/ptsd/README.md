---
schema: human-scale-entry/v1
id: ptsd
name: PTSD
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-08
summary: "PTSD (7-10% lifetime risk after trauma) involves amygdala hyperreactivity, hippocampal atrophy, noradrenergic hyperarousal, and hypocortisolemia; first-line: trauma-focused CBT and SSRIs (sertraline, paroxetine); prazosin (α1 antagonist) reduces nightmares."
aliases: ["PTSD", "post-traumatic stress disorder", "trauma", "combat PTSD", "complex PTSD", "fear extinction", "prazosin PTSD", "EMDR", "prolonged exposure", "TRD PTSD"]
sources:
  - id: yehuda-2015-ptsd-review
    type: peer-reviewed
    cite: "Yehuda R, Hoge CW, McFarlane AC, et al. Post-traumatic stress disorder. Nat Rev Dis Primers. 2015;1:15057."
    doi: "10.1038/nrdp.2015.57"
    pmid: "27189040"
    url: "https://doi.org/10.1038/nrdp.2015.57"
    accessed: "2026-06-08"
  - id: foa-2019-ptsd-treatments
    type: peer-reviewed
    cite: "Foa EB, McLean CP. The efficacy of exposure therapy for anxiety and related disorders and its underlying mechanisms: the emotional processing theory. Annu Rev Clin Psychol. 2016;12:1-28."
    doi: "10.1146/annurev-clinpsy-021815-093533"
    pmid: "26928206"
    url: "https://doi.org/10.1146/annurev-clinpsy-021815-093533"
    accessed: "2026-06-08"
  - id: mitchell-2021-mdma-ptsd
    type: peer-reviewed
    cite: "Mitchell JM, Bogenschutz M, Lilienstein A, et al. MDMA-assisted therapy for severe PTSD: a randomized, double-blind, placebo-controlled phase 3 trial. Nat Med. 2021;27(6):1025-1033."
    doi: "10.1038/s41591-021-01336-3"
    url: "https://doi.org/10.1038/s41591-021-01336-3"
    accessed: "2026-06-08"
cross_links:
  - target: 01-human/03-molecular/norepinephrine
    relation: connects-to
    note: "Locus coeruleus hyperactivation in PTSD → excess NE → amygdala hyperreactivity, hyperarousal, and intrusive re-experiencing; prazosin (α1 antagonist) reduces NE-driven nightmares; propranolol may reduce fear memory reconsolidation when given within hours of trauma."
  - target: 01-human/03-molecular/cortisol
    relation: connects-to
    note: "PTSD exhibits paradoxical hypocortisolemia — elevated CRH but enhanced GR sensitivity → excess negative feedback; low cortisol impairs fear extinction; hydrocortisone given within hours of trauma shows prophylactic benefit in some randomized trials."
  - target: 01-human/03-molecular/bdnf
    relation: connects-to
    note: "Reduced hippocampal BDNF in PTSD mirrors findings in MDD; chronic stress → glucocorticoid-mediated BDNF suppression → hippocampal volume loss (~8% in chronic PTSD); SSRIs normalize BDNF and partially restore hippocampal volume with sustained treatment."
  - target: 01-human/03-molecular/glutamate
    relation: connects-to
    note: "NMDA receptor-mediated processes underlie fear memory consolidation and extinction in amygdala and vmPFC; D-cycloserine (partial NMDA agonist) enhances extinction in CBT; ketamine reduces PTSD symptoms via rapid BDNF/mTOR signaling and disrupted fear memory reconsolidation."
  - target: 01-human/06-organ/brain
    relation: targets
    note: "PTSD features amygdala hyperreactivity and reduced vmPFC control over fear responses; hippocampal volume is reduced ~8%; anterior cingulate shows reduced activation; normalization of amygdala-vmPFC connectivity predicts treatment response on fMRI."
  - target: 01-human/03-molecular/oxytocin
    relation: connects-to
    note: "Oxytocin facilitates fear extinction in the amygdala via OTR on CeA neurons; chronic stress reduces OT signaling; intranasal oxytocin is under investigation as an adjunct to exposure therapy to enhance extinction memory consolidation in PTSD."
  - target: 01-human/03-molecular/serotonin
    relation: connects-to
    note: "SSRIs (sertraline, paroxetine) are FDA-approved for PTSD; serotonin modulates fear extinction in vmPFC; serotonin dysregulation contributes to PTSD hyperarousal, emotional numbing, and sleep disturbance; SNRIs (venlafaxine) also used for PTSD with good evidence."
  - target: 01-human/03-molecular/crh
    relation: connects-to
    note: "PTSD shows CSF CRH excess, elevated ACTH, and paradoxically low cortisol (enhanced glucocorticoid feedback); CRH hyperdrive in amygdala/BNST drives hyperarousal and re-experiencing; CRHR1 antagonists are a proposed pharmacotherapy pending adequate clinical trials."
  - target: 01-human/03-molecular/acth
    relation: connects-to
    note: "PTSD shows dissociated HPA: normal or elevated ACTH responses to CRH but low basal cortisol — due to GR hypersensitivity (enhanced negative feedback); contrasts with MDD (high ACTH + high cortisol + GR resistance); enhanced DST suppression (<0.5 µg/dL) is the PTSD biomarker."
  - target: 01-human/03-molecular/npy
    relation: connects-to
    note: "Amygdala and CSF NPY are reduced in PTSD; Y1R-mediated anxiolysis is impaired; plasma NPY correlates with stress resilience in veterans; glucocorticoid excess in chronic stress depletes amygdala NPY; NPY Y1R agonists are under investigation as PTSD pharmacotherapy."
  - target: 01-human/03-molecular/vasopressin
    relation: connects-to
    note: "CSF vasopressin is elevated in PTSD; AVP-CRH synergy at corticotroph V1bR potentiates ACTH when CRH receptors desensitise; elevated AVP sustains HPA hyperactivation; V1bR antagonists show anxiolytic effects and are a proposed PTSD pharmacotherapy."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "PTSD and major depression are highly comorbid and share neurobiology: HPA-axis and monoaminergic dysregulation, hippocampal changes, and overlapping symptoms link them, about half of PTSD patients also meet criteria for depression, and SSRIs treat both."
  - target: 01-human/05-tissue/hippocampus
    relation: connects-to
    note: "The hippocampus is central to PTSD: reduced hippocampal volume impairs contextualizing fear memories, so trauma cues are not recognized as past, and the hippocampus fails to restrain an overactive amygdala—a core circuit abnormality targeted by trauma-focused therapy."
  - target: 01-human/07-system/alcohol-use-disorder
    relation: connects-to
    note: "PTSD and alcohol use disorder form a vicious cycle: many drink to blunt hyperarousal and intrusive memories, but alcohol fragments sleep and worsens PTSD, and the two strongly co-occur—so integrated treatment of both outperforms addressing either alone."
  - target: 01-human/07-system/panic-disorder
    relation: connects-to
    note: "PTSD and panic disorder share a hyperactive fear response but differ in trigger: both feature surges of autonomic arousal, but panic attacks come 'out of the blue' while PTSD's are cued by trauma reminders—and panic commonly complicates PTSD."
  - target: 01-human/07-system/bipolar-disorder
    relation: connects-to
    note: "PTSD and bipolar disorder frequently co-occur and worsen each other: trauma raises bipolar risk, comorbid PTSD predicts more mood episodes and suicidality, and overlapping irritability and arousal can blur diagnosis—so screening for trauma is part of bipolar assessment."
  - target: 01-human/07-system/fibromyalgia
    relation: connects-to
    note: "PTSD and fibromyalgia are tightly linked through chronic stress: trauma and HPA-axis dysregulation promote central sensitization, so fibromyalgia is far more common in PTSD—evidence that psychological trauma can manifest as bodily pain."
  - target: 01-human/03-molecular/gaba
    relation: connects-to
    note: "PTSD reflects a tipped excitatory-inhibitory balance: deficient GABAergic inhibition leaves fear circuits hyperexcitable, underlying hyperarousal and intrusive memories, which is why benzodiazepines that boost GABA paradoxically tend to worsen long-term PTSD."
  - target: 01-human/07-system/insomnia-disorder
    relation: connects-to
    note: "Sleep disturbance is a core feature of PTSD, not just a symptom: nightmares and insomnia are diagnostic criteria and can precede and perpetuate the disorder, and treating the insomnia (e.g., with prazosin or CBT-I) improves overall PTSD outcomes."
  - target: 01-human/07-system/cannabis-use-disorder
    relation: connects-to
    note: "PTSD and cannabis use disorder feed each other: many with PTSD use cannabis to dampen hyperarousal and insomnia, but tolerance and withdrawal worsen the symptoms it masks, so this common self-treatment readily slides into dependence."
  - target: 01-human/03-molecular/endocannabinoid
    relation: connects-to
    note: "The endocannabinoid system governs fear extinction central to PTSD: cannabinoid signaling helps the brain unlearn trauma cues, and deficits may lock in fear—so this pathway underlies why cannabis is sought for PTSD nightmares and why it is a drug-development target."
  - target: 01-human/03-molecular/epinephrine
    relation: connects-to
    note: "Adrenaline burns trauma into memory: the epinephrine surge during a terrifying event strengthens memory consolidation, helping explain PTSD's intrusive recollections—and why beta-blockers like propranolol have been tested to blunt or weaken fear memories."
  - target: 01-human/07-system/borderline-personality-disorder
    relation: connects-to
    note: "PTSD and borderline personality disorder share a traumatic root: childhood trauma drives both, and complex PTSD overlaps BPD's emotional dysregulation and unstable relationships—so the two frequently co-occur and can be hard to disentangle clinically."
  - target: 01-human/06-organ/adrenal-gland
    relation: connects-to
    note: "PTSD dysregulates the adrenal stress axis: chronic trauma alters HPA-axis output so the adrenal gland's cortisol response is blunted and abnormal, leaving the noradrenergic alarm system unrestrained—part of the biology behind hypervigilance and flashbacks."
  - target: 01-human/04-cellular/microglia
    relation: connects-to
    note: "Trauma leaves an inflammatory mark via microglia: PTSD is linked to activated brain microglia and neuroinflammation that may damage the hippocampus and prefrontal cortex, connecting psychological trauma to measurable brain changes."
  - target: 01-human/03-molecular/dopamine
    relation: connects-to
    note: "Dopamine ties PTSD to reward and to its therapies: trauma blunts reward-related dopamine signaling (contributing to numbing and anhedonia), and dopamine is part of why MDMA-assisted therapy is being studied to help process traumatic memories."
---

# PTSD

## Overview

**Post-traumatic stress disorder (PTSD)** is a trauma- and stressor-related psychiatric condition that develops in a subset of individuals following exposure to actual or threatened death, serious injury, or sexual violence. It affects approximately **7–10% of individuals** who experience qualifying traumatic events over their lifetimes — with higher rates in certain exposed groups (veterans: 15–30%; sexual assault survivors: 30–50%; disaster workers: 10–20%). Globally, an estimated 3.9–5.6% of adults have lifetime PTSD, with women affected at 2× the rate of men.

**DSM-5 PTSD** (requires exposure to trauma + symptoms from all 4 clusters ≥1 month):

**Criterion A (Trauma):** Exposure to death, serious injury, or sexual violence (direct, witnessed, learned about, or repeated first-responder exposure)

**4 Symptom clusters:**

| Cluster | Examples | Neural correlate |
|:---|:---|:---|
| **B — Intrusion** | Flashbacks, nightmares, psychological/physiological distress to cues | Amygdala hyperreactivity; context-independent fear retrieval |
| **C — Avoidance** | Avoiding trauma-related thoughts, feelings, places, people | vmPFC failure to suppress amygdala; anhedonia |
| **D — Negative cognitions/mood** | Persistent negative beliefs, distorted blame, emotional numbing, dissociation | Hippocampal memory encoding failure; PFC hypofunction |
| **E — Hyperarousal** | Hypervigilance, exaggerated startle, irritability, sleep disturbance, reckless behavior | Locus coeruleus-NE hyperactivation; amygdala sensitization |

**Complex PTSD (ICD-11):** Includes three additional domains — emotional dysregulation, negative self-concept, and relationship disturbances — typical of prolonged childhood trauma (complex developmental trauma).

## Structure

### Neurobiology of fear circuits

PTSD represents a pathological state of the **amygdala-hippocampus-prefrontal fear circuit**:

**Basolateral amygdala (BLA):**
- Core site of **fear memory acquisition and storage** — Pavlovian fear conditioning occurs here: CS (conditioned stimulus, e.g., sound) + US (unconditioned stimulus, shock) → CS-US association encoded via CaMKII/CREB-dependent plasticity
- In PTSD: heightened BLA activity, reduced threshold for fear acquisition, overgeneralization of conditioned fear to non-threatening cues (conceptually similar to gun exposure → freeze in a patient with combat PTSD)
- BLA → downstream nuclei: central amygdala (CeA) → fear expression (freezing, HR increase, cortisol); basal amygdala → vHPC → avoidance behavior

**Ventromedial prefrontal cortex (vmPFC, includes infralimbic cortex):**
- Source of **fear extinction** — vmPFC neurons send GABAergic projections to amygdala intercalated cells (ITC) → inhibit CeA → safety signal; extinction learning is vmPFC-dependent
- In PTSD: reduced vmPFC volume and activation → inadequate suppression of BLA → persistence of conditioned fear → failure of extinction → PTSD maintenance
- Target of MDMA-assisted therapy: MDMA restores vmPFC control over amygdala

**Hippocampus:**
- Essential for **contextual fear discrimination** — allows fear response to be appropriately limited to the original danger context (not generalized)
- In PTSD: hippocampal volume reduced ~8% (bilateral; predominantly CA3 and dentate gyrus); impaired contextual encoding → fear triggered in "safe" contexts
- Mechanism: chronic stress → glucocorticoid excess → reduced BDNF → CA3 dendritic retraction; SSRI treatment partially restores hippocampal volume over 6–12 months

**Locus coeruleus (LC):**
- Source of CNS norepinephrine; projects widely to cortex, amygdala, hippocampus, spinal cord
- In PTSD: hyperactivated LC → elevated tonic and phasic NE → chronic hyperarousal, exaggerated startle, sleep disruption
- Target of prazosin (α1 antagonist, reduces nightmares) and clonidine (α2 agonist, reduces LC firing)

## Function

### HPA axis in PTSD: the cortisol paradox

Unlike MDD (which features **hypercortisolemia**), PTSD — particularly chronic PTSD — paradoxically shows **hypocortisolemia** [^yehuda-2015-ptsd-review]:

- **Acute trauma response:** Cortisol surge (normal) → should suppress traumatic memory consolidation and aid resolution
- **Chronic PTSD:** Cortisol levels are often **below normal**, combined with:
  - Enhanced negative feedback sensitivity (lower dexamethasone dose required for cortisol suppression)
  - Upregulated glucocorticoid receptors on lymphocytes
  - Elevated CRH in CSF despite low cortisol

**Mechanistic interpretation:**
- Enhanced GR sensitivity → more powerful negative feedback → greater cortisol suppression
- Low cortisol in PTSD impairs extinction: cortisol normally facilitates extinction memory consolidation; without it, fear memories cannot be adequately resolved
- Yehuda's model: PTSD is not an excess of cortisol but a dysregulation — the normal post-trauma cortisol surge fails to suppress trauma memory → persistent fear encoding

**Implications:** Hydrocortisone given acutely (within hours of trauma) in ICU patients or combat settings reduces PTSD incidence in some RCTs — by rescuing the normal cortisol surge needed for memory resolution.

### Noradrenergic system

The **norepinephrine hyperactivation model of PTSD** explains hyperarousal symptoms:
- LC hyperactivation → elevated NE → increased amygdala reactivity (BLA has dense α1-NE receptors → NE enhances fear memory acquisition and intrusive retrieval)
- Sleep disruption: NE during REM sleep normally decreases → in PTSD, high NE during REM → nightmares
- Startle: NE lowers the sensory threshold for CeA-mediated startle
- Exaggerated cardiovascular response to trauma reminders: sympathetic surge

**Pharmacological targets:**
- **Prazosin (α1 antagonist):** Reduces nightmares and overall PTSD severity in multiple RCTs; blocks NE signaling in amygdala and brainstem circuits during sleep
- **Propranolol (β-blocker):** May reduce fear memory reconsolidation when given within 1–6 hours of reactivating a trauma memory (controversial; reconsolidation blockade hypothesis)
- **Clonidine (α2 agonist):** Reduces LC firing → decreases NE release → reduces hyperarousal; used in children with PTSD/complex PTSD

## Pathology

### Trauma characteristics and risk factors

Not all trauma leads to PTSD. Risk and resilience factors include:

**Risk factors:**
- Trauma type: interpersonal violence (sexual assault, combat) > accidents > natural disasters
- Peritraumatic dissociation (strongest predictor of PTSD development)
- Prior trauma (especially childhood adversity — sensitizes amygdala and HPA axis)
- Genetic factors: heritability ~40%; Val66Met BDNF, FKBP5 (GR co-chaperone variants alter cortisol sensitivity), RELN (reelin)
- Female sex; poverty; lack of social support

**Resilience factors:**
- Strong social support (most protective modifiable factor)
- Prior mastery experiences; sense of agency
- High BDNF (exercise, social engagement)
- Rapid cortisol normalization after trauma (adequate glucocorticoid response)

### Treatment

**First-line evidence-based treatments:**

**Trauma-focused psychotherapy (superior to pharmacotherapy in most trials):**
- **Prolonged Exposure (PE):** Imaginal and in vivo exposure to trauma memories and avoided situations; disrupts conditioned fear through extinction learning; 50-60% remission [^foa-2019-ptsd-treatments]
- **Cognitive Processing Therapy (CPT):** Modifies maladaptive cognitions about trauma (stuck points); equivalent to PE; used widely in VA system
- **EMDR (Eye Movement Desensitization and Reprocessing):** Bilateral sensory stimulation during trauma memory processing; equivalent efficacy to PE/CPT; mechanism debated (eye movements may be inert — exposure component may drive benefit)

**Pharmacotherapy:**
- **SSRIs (sertraline, paroxetine):** FDA-approved for PTSD; moderate efficacy (~30-40% response); normalize serotonin and BDNF; useful for comorbid depression/anxiety
- **Venlafaxine (SNRI):** Off-label but evidence-based; addresses NE hyperarousal component
- **Prazosin (α1 antagonist):** For nightmares and sleep disruption; addresses NE-driven dream pathology
- **Benzodiazepines:** NOT recommended in PTSD — impair fear extinction learning (GABA-A-mediated amnesia blocks extinction consolidation); worsen long-term course despite short-term symptom reduction

**Novel/Emerging:**

**MDMA-assisted therapy:**
- Phase 3 trial (Mitchell et al., Nat Med 2021) [^mitchell-2021-mdma-ptsd]: MDMA-assisted therapy → 67% no longer met PTSD criteria vs. 32% placebo at 18-week endpoint; large effect size (d=0.9)
- Mechanism: MDMA releases serotonin, oxytocin, and NE → dampens amygdala reactivity while enabling emotional processing within therapy session; facilitates "therapeutic window" — processing trauma without overwhelming anxiety; may restore vmPFC-amygdala connectivity
- FDA Advisory Committee rejected approval (2024) on manufacturing and data integrity grounds; Phase 3b trial ongoing; widely available in clinical settings outside the US (Australia approved 2023)

**Stellate ganglion block:**
- Single injection of local anesthetic into cervical sympathetic ganglion; appears to reduce LC-sympathetic outflow; ~50-60% responder rate in RCTs for combat PTSD; mechanism may involve NGF-driven sympathetic hyperinnervation of LC

**Cannabis and cannabinoids:**
- Endocannabinoid system (CB1 receptors in amygdala and hippocampus) regulates fear extinction; THC reduces nightmare severity; synthetic nabilone approved in Canada for PTSD nightmares; clinical use outpacing evidence base

## Connections

- `connects-to` → **[Norepinephrine](../../../03-molecular/norepinephrine/README.md)** — locus coeruleus hyperactivation in PTSD drives excess NE → amygdala hyperreactivity, hyperarousal, and intrusive re-experiencing; prazosin (α1 antagonist) reduces NE-driven nightmares; propranolol given acutely after trauma may reduce fear memory reconsolidation.

- `connects-to` → **[Cortisol](../../../03-molecular/cortisol/README.md)** — PTSD exhibits paradoxical hypocortisolemia with enhanced GR sensitivity → excess negative feedback; low cortisol impairs fear extinction; hydrocortisone given within hours of trauma shows prophylactic benefit; opposite HPA profile from MDD despite clinical overlap.

- `connects-to` → **[BDNF](../../../03-molecular/bdnf/README.md)** — chronic stress-induced glucocorticoid BDNF suppression causes hippocampal volume loss (~8%) in PTSD; reduced BDNF impairs contextual fear discrimination; SSRIs normalize hippocampal BDNF and partially restore volume; Val66Met SNP increases PTSD risk.

- `connects-to` → **[Glutamate](../../../03-molecular/glutamate/README.md)** — NMDA receptors mediate fear memory consolidation and extinction in amygdala and vmPFC; D-cycloserine (partial NMDA agonist) enhances extinction learning in prolonged exposure therapy; ketamine reduces PTSD symptoms via BDNF/mTOR-mediated synaptic remodeling.

- `targets` → **[Brain](../../../06-organ/brain/README.md)** — PTSD features BLA hyperreactivity, reduced vmPFC-amygdala suppression, ~8% hippocampal volume reduction, and reduced anterior cingulate activation; normalization of amygdala-vmPFC functional connectivity is a biomarker of treatment response on task-based fMRI.

- `connects-to` → **[Oxytocin](../../../03-molecular/oxytocin/README.md)** — oxytocin facilitates fear extinction in the amygdala via OTR on CeA neurons; chronic stress reduces OT signaling; intranasal oxytocin is under investigation as an adjunct to exposure therapy to enhance extinction memory consolidation.

- `connects-to` → **[Serotonin](../../../03-molecular/serotonin/README.md)** — SSRIs (sertraline, paroxetine) are FDA-approved for PTSD; serotonin modulates fear extinction in vmPFC; serotonin dysregulation contributes to hyperarousal, emotional numbing, and sleep disturbance; SNRIs (venlafaxine) are also evidence-based for PTSD symptom reduction.

- `connects-to` → **[CRH](../../../03-molecular/crh/README.md)** — PTSD shows CSF CRH excess, elevated ACTH, and paradoxically low cortisol (enhanced glucocorticoid feedback); CRH hyperdrive in amygdala/BNST drives hyperarousal and re-experiencing; CRHR1 antagonists are a proposed pharmacotherapy pending adequate clinical trials.

- `connects-to` → **[ACTH](../../../03-molecular/acth/README.md)** — PTSD exhibits a dissociated HPA pattern: normal or elevated ACTH responses to CRH challenge but chronically low basal cortisol, explained by GR hypersensitivity (enhanced negative feedback) rather than pituitary hypofunction; enhanced DST suppression (<0.5 µg/dL) is a biological signature of PTSD that distinguishes it from MDD.

- `connects-to` → **[NPY](../../../03-molecular/npy/README.md)** — amygdala and CSF NPY are reduced in PTSD; Y1R-mediated anxiolysis is impaired; plasma NPY correlates with stress resilience in veterans; glucocorticoid excess in chronic stress depletes amygdala NPY; NPY Y1R agonists are under investigation as PTSD pharmacotherapy.
- `connects-to` → **[Vasopressin](../../../03-molecular/vasopressin/README.md)** — CSF vasopressin is elevated in PTSD; AVP-CRH synergy at corticotroph V1bR potentiates ACTH when CRH receptors desensitise; elevated AVP sustains HPA hyperactivation; V1bR antagonists show anxiolytic effects and are a proposed PTSD pharmacotherapy.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — PTSD and major depression are highly comorbid and share neurobiology: HPA-axis and monoaminergic dysregulation, hippocampal changes, and overlapping symptoms link them, about half of PTSD patients also meet criteria for depression, and SSRIs treat both.
- `connects-to` → **[Hippocampus](../../05-tissue/hippocampus/README.md)** — The hippocampus is central to PTSD: reduced hippocampal volume impairs contextualizing fear memories, so trauma cues are not recognized as past, and the hippocampus fails to restrain an overactive amygdala—a core circuit abnormality targeted by trauma-focused therapy.
- `connects-to` → **[Alcohol Use Disorder](../alcohol-use-disorder/README.md)** — PTSD and alcohol use disorder form a vicious cycle: many drink to blunt hyperarousal and intrusive memories, but alcohol fragments sleep and worsens PTSD, and the two strongly co-occur—so integrated treatment of both outperforms addressing either alone.
- `connects-to` → **[Panic Disorder](../panic-disorder/README.md)** — PTSD and panic disorder share a hyperactive fear response but differ in trigger: both feature surges of autonomic arousal, but panic attacks come 'out of the blue' while PTSD's are cued by trauma reminders—and panic commonly complicates PTSD.
- `connects-to` → **[Bipolar Disorder](../bipolar-disorder/README.md)** — PTSD and bipolar disorder frequently co-occur and worsen each other: trauma raises bipolar risk, comorbid PTSD predicts more mood episodes and suicidality, and overlapping irritability and arousal can blur diagnosis—so screening for trauma is part of bipolar assessment.
- `connects-to` → **[Fibromyalgia](../fibromyalgia/README.md)** — PTSD and fibromyalgia are tightly linked through chronic stress: trauma and HPA-axis dysregulation promote central sensitization, so fibromyalgia is far more common in PTSD—evidence that psychological trauma can manifest as bodily pain.
- `connects-to` → **[GABA](../../03-molecular/gaba/README.md)** — PTSD reflects a tipped excitatory-inhibitory balance: deficient GABAergic inhibition leaves fear circuits hyperexcitable, underlying hyperarousal and intrusive memories, which is why benzodiazepines that boost GABA paradoxically tend to worsen long-term PTSD.
- `connects-to` → **[Insomnia Disorder](../insomnia-disorder/README.md)** — Sleep disturbance is a core feature of PTSD, not just a symptom: nightmares and insomnia are diagnostic criteria and can precede and perpetuate the disorder, and treating the insomnia (e.g., with prazosin or CBT-I) improves overall PTSD outcomes.
- `connects-to` → **[Cannabis Use Disorder](../cannabis-use-disorder/README.md)** — PTSD and cannabis use disorder feed each other: many with PTSD use cannabis to dampen hyperarousal and insomnia, but tolerance and withdrawal worsen the symptoms it masks, so this common self-treatment readily slides into dependence.
- `connects-to` → **[Endocannabinoid System](../../03-molecular/endocannabinoid/README.md)** — The endocannabinoid system governs fear extinction central to PTSD: cannabinoid signaling helps the brain unlearn trauma cues, and deficits may lock in fear—so this pathway underlies why cannabis is sought for PTSD nightmares and why it is a drug-development target.
- `connects-to` → **[Epinephrine](../../03-molecular/epinephrine/README.md)** — Adrenaline burns trauma into memory: the epinephrine surge during a terrifying event strengthens memory consolidation, helping explain PTSD's intrusive recollections—and why beta-blockers like propranolol have been tested to blunt or weaken fear memories.
- `connects-to` → **[Borderline Personality Disorder](../borderline-personality-disorder/README.md)** — PTSD and borderline personality disorder share a traumatic root: childhood trauma drives both, and complex PTSD overlaps BPD's emotional dysregulation and unstable relationships—so the two frequently co-occur and can be hard to disentangle clinically.
- `connects-to` → **[Adrenal Gland](../../06-organ/adrenal-gland/README.md)** — PTSD dysregulates the adrenal stress axis: chronic trauma alters HPA-axis output so the adrenal gland's cortisol response is blunted and abnormal, leaving the noradrenergic alarm system unrestrained—part of the biology behind hypervigilance and flashbacks.
- `connects-to` → **[Microglia](../../04-cellular/microglia/README.md)** — Trauma leaves an inflammatory mark via microglia: PTSD is linked to activated brain microglia and neuroinflammation that may damage the hippocampus and prefrontal cortex, connecting psychological trauma to measurable brain changes.
- `connects-to` → **[Dopamine](../../03-molecular/dopamine/README.md)** — Dopamine ties PTSD to reward and to its therapies: trauma blunts reward-related dopamine signaling (contributing to numbing and anhedonia), and dopamine is part of why MDMA-assisted therapy is being studied to help process traumatic memories.

[^yehuda-2015-ptsd-review]: Yehuda R, Hoge CW, McFarlane AC, et al. Post-traumatic stress disorder. *Nat Rev Dis Primers.* 2015;1:15057. [doi:10.1038/nrdp.2015.57](https://doi.org/10.1038/nrdp.2015.57) · [PubMed 27189040](https://pubmed.ncbi.nlm.nih.gov/27189040/)
[^foa-2019-ptsd-treatments]: Foa EB, McLean CP. The efficacy of exposure therapy for anxiety and related disorders. *Annu Rev Clin Psychol.* 2016;12:1-28. [doi:10.1146/annurev-clinpsy-021815-093533](https://doi.org/10.1146/annurev-clinpsy-021815-093533) · [PubMed 26928206](https://pubmed.ncbi.nlm.nih.gov/26928206/)
[^mitchell-2021-mdma-ptsd]: Mitchell JM, Bogenschutz M, Lilienstein A, et al. MDMA-assisted therapy for severe PTSD: a randomized, double-blind, placebo-controlled phase 3 trial. *Nat Med.* 2021;27(6):1025-1033. [doi:10.1038/s41591-021-01336-3](https://doi.org/10.1038/s41591-021-01336-3)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
