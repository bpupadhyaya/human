---
schema: human-scale-entry/v1
id: bipolar-disorder
name: Bipolar Disorder
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-08
summary: "Bipolar disorder (60M affected) causes episodic mania and depression; dopaminergic dysregulation and CLOCK gene variants drive mood cycles; lithium (GSK-3β inhibitor, suicide prevention) is gold-standard mood stabilizer; valproate and quetiapine are alternatives."
aliases: ["bipolar disorder", "bipolar I", "bipolar II", "manic-depressive disorder", "mania", "hypomania", "mood stabilizer", "lithium", "valproate bipolar"]
sources:
  - id: grande-2016-bipolar-review
    type: peer-reviewed
    cite: "Grande I, Berk M, Birmaher B, Vieta E. Bipolar disorder. Lancet. 2016;387(10027):1561-1572."
    doi: "10.1016/S0140-6736(15)00241-X"
    pmid: "26388529"
    url: "https://doi.org/10.1016/S0140-6736(15)00241-X"
    accessed: "2026-06-08"
  - id: geddes-2013-bipolar-treatment
    type: peer-reviewed
    cite: "Geddes JR, Miklowitz DJ. Treatment of bipolar disorder. Lancet. 2013;381(9878):1672-1682."
    doi: "10.1016/S0140-6736(13)60857-0"
    pmid: "23663953"
    url: "https://doi.org/10.1016/S0140-6736(13)60857-0"
    accessed: "2026-06-08"
  - id: cipriani-2013-lithium-suicide
    type: peer-reviewed
    cite: "Cipriani A, Hawton K, Stockton S, Geddes JR. Lithium in the prevention of suicide in mood disorders: updated systematic review and meta-analysis. BMJ. 2013;346:f3646."
    doi: "10.1136/bmj.f3646"
    pmid: "23814104"
    url: "https://doi.org/10.1136/bmj.f3646"
    accessed: "2026-06-08"
cross_links:
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "Lithium, the gold-standard mood stabilizer, directly inhibits GSK-3β (uncompetitive Mg²⁺ site); GSK-3β hyperactivity in bipolar drives circadian dysregulation and BDNF suppression; lithium-induced β-catenin stabilization promotes neuroprotection."
  - target: 01-human/03-molecular/dopamine
    relation: connects-to
    note: "Mesolimbic dopamine hyperactivity drives manic symptoms (euphoria, impulsivity, grandiosity, decreased sleep need); antipsychotics (haloperidol, quetiapine, olanzapine) block D2 receptors and reduce acute mania; mesocortical D1 hypofunction may contribute to bipolar depression."
  - target: 01-human/03-molecular/serotonin
    relation: connects-to
    note: "SSRIs can trigger manic switching in bipolar disorder — serotonergic antidepressants are generally used only with mood stabilizer cover; 5-HT2A-blocking atypical antipsychotics (quetiapine) are effective for bipolar depression without switch risk."
  - target: 01-human/03-molecular/bdnf
    relation: connects-to
    note: "BDNF Val66Met SNP is associated with 2× increased bipolar disorder risk; BDNF is reduced during depressive phases; lithium and valproate both upregulate BDNF and BCL-2, promoting hippocampal neurogenesis and neuroprotection — a common mechanism of mood stabilizers."
  - target: 01-human/03-molecular/gaba
    relation: connects-to
    note: "Valproate (VPA) potentiates GABA-A function and blocks voltage-gated Na⁺/Ca²⁺ channels in bipolar disorder; GABA deficiency in prefrontal cortex is associated with bipolar depression; benzodiazepines provide acute antimanic sedation via GABA-A agonism."
  - target: 01-human/06-organ/brain
    relation: targets
    note: "Bipolar disorder features amygdala hyperreactivity and reduced vmPFC regulation; hippocampal volume is reduced ~6% (BD-I); DLPFC shows reduced activation during working memory tasks; lithium partially reverses hippocampal atrophy with long-term use."
---

# Bipolar Disorder

## Overview

**Bipolar disorder (BD)** is a chronic, episodic mood disorder characterized by alternating periods of **mania** (or hypomania in BD-II) and **depression**, with periods of euthymia between episodes. It affects approximately **60 million people** worldwide (~1–2% lifetime prevalence) across all cultures and socioeconomic strata [^grande-2016-bipolar-review]. It ranks among the top 10 causes of global disability, with the highest years-lived-with-disability burden occurring in young adults during their most productive decades.

Bipolar disorder is often underdiagnosed — the average time from first symptom to correct diagnosis is **7–10 years**, frequently because depressive episodes present first and are mistakenly treated as unipolar depression (risking SSRI-induced manic switching). When correctly diagnosed and treated, most patients can achieve sustained mood stability, though the condition remains lifelong.

**Key clinical dimensions:**
- **BD-I**: Full manic episodes (≥7 days or requiring hospitalization), with or without depression — most severe form; associated with psychosis during mania in ~60%
- **BD-II**: Hypomanic episodes (≥4 days, no hospitalization) + major depressive episodes — often initially misdiagnosed as MDD; depression predominates; high suicide risk
- **Cyclothymia**: Subthreshold hypomanic and depressive symptoms for ≥2 years
- **BD-NOS/Other specified**: Rapid cycling (≥4 episodes/year); mixed features (simultaneous manic + depressive symptoms — highest suicide risk)

**Suicide:** BD carries the **highest suicide rate** of any psychiatric disorder — 15-fold higher than the general population; 25–50% of patients attempt suicide. Lithium is the only medication with Level 1 evidence for **suicide prevention** (Cipriani 2013) [^cipriani-2013-lithium-suicide], through mechanisms beyond mood stabilization (possibly NF-κB → neuroinflammation suppression, GSK-3β → apoptosis inhibition).

## Structure

### DSM-5 diagnostic criteria

**Manic episode** (DSM-5, required for BD-I diagnosis):
- ≥7 days (or any duration if hospitalization required or psychosis present) of persistently elevated, expansive, or irritable mood AND increased goal-directed activity/energy
- ≥3 of (DIGFAST): **D**istractibility, **I**mpulsivity/reckless behavior, **G**randiosity, **F**light of ideas, **A**ctivity increase, **S**leep decreased, **T**alkativeness/pressured speech

**Hypomanic episode** (BD-II): same symptom criteria but ≥4 days, not severe enough for hospitalization, no psychosis, and a marked functional change observable by others (not just self-reported)

**Major depressive episode**: same criteria as MDD (5/9 SIG E CAPS for ≥2 weeks)

**Specifiers relevant to treatment:**
- **Mixed features**: ≥3 symptoms of opposite polarity during current episode → highest suicide risk; lithium + quetiapine recommended; antidepressants contraindicated
- **Rapid cycling**: ≥4 distinct mood episodes/year → valproate + atypical antipsychotics; lithium less effective; rule out thyroid dysfunction and substance use
- **With psychotic features**: Typically mood-congruent (grandiosity in mania; guilt/nihilism in depression); olanzapine or aripiprazole often added
- **With anxious distress**: Very common; higher suicidality; benzodiazepines adjunctive

### Neurobiology of bipolar mood cycling

**Circadian system dysregulation:**
- **CLOCK gene** (CLOCK, ARNTL/BMAL1, PER3, CRY1/2) variants are the most consistently associated with BD across GWAS; ~50% of circadian genes are GSK-3β substrates
- GSK-3β phosphorylates CLOCK → period lengthening; PER2 → degradation; REV-ERBα → destabilization
- BD patients show reduced sleep need in mania, hypersomnia in depression, irregular sleep-wake cycles, and phase shifts — all consistent with circadian clock pathology
- Lithium lengthens circadian period (via GSK-3β inhibition) and stabilizes amplitude — likely contributing to mood stabilization

**Monoamine dysregulation:**
- **Mania:** Mesolimbic dopamine hyperactivity (D2/D3 hypersensitivity) → reward overdrive, euphoria, impulsivity, reduced sleep need; dopamine release from VTA to NAc is pathologically increased
- **Depression:** Relative hyperdopaminergic tone withdrawn; norepinephrine and serotonin deficit similar to MDD; mesocortical hypodopaminergia impairs PFC executive function
- Catecholamine hypothesis: mania = catecholamine excess; depression = catecholamine deficit (bidirectional oscillation driven by homeostatic counter-regulation and receptor downregulation/upregulation cycles)

**Intracellular signaling:**
- **GSK-3β hyperactivity**: Directly supported by postmortem studies (reduced Ser9-phosphorylated/inactivated GSK-3β in frontal cortex); lithium's clinical efficacy proportional to GSK-3β inhibition
- **IP3/DAG/PKC pathway**: Myo-inositol depletion by lithium reduces PKC-mediated signal amplification in neurons; carbamazepine similarly depletes DAG
- **Mitochondrial dysfunction**: BD shows reduced Complex I activity in postmortem brain; mitochondrial haplogroups associated with BD; N-acetylcysteine (antioxidant) shows efficacy in bipolar depression trials
- **Neuroinflammation**: TNF-α, IL-6, and CRP are elevated during mood episodes; normalized with lithium and quetiapine; shared with MDD biology but more episodic

**Genetics:**
- Heritability: ~70–80% (among highest in psychiatry)
- Twin concordance: monozygotic ~45%, dizygotic ~10%
- BD-I and schizophrenia share significant genetic overlap (GWAS; ~70% overlapping loci); BD is not merely a mood disorder — it represents a neurodevelopmental spectrum overlapping schizophrenia
- Key GWAS loci: CACNA1C (L-type Ca²⁺ channel — voltage-gated Ca²⁺ entry; convergence with migraine and schizophrenia), SHANK2 (synaptic scaffold; also autism), ANK3 (ankyrin G — Nav channel anchoring), TRANK1, and CLOCK pathway genes
- BDNF Val66Met: associated with earlier illness onset and increased depressive episodes in BD

## Function

### Manic episode biology

During acute mania, the following neurobiological cascade unfolds:

1. **Mesolimbic DA hyperactivation:** VTA → NAc dopamine surge → reward hypersensitivity → goal-directed behavior amplified → impulsivity (temporal discounting shifts toward immediate reward)
2. **NE/CORT surge:** Sympatho-adrenal activation → decreased sleep need (patients often sleep 0–2h without fatigue) → NE → LC hyperactivation → arousal
3. **Reduced vmPFC-amygdala control:** Elevated dopamine in PFC paradoxically impairs executive control (inverted U-curve of D1 receptor stimulation) → impulsivity, poor insight
4. **Circadian disruption:** CLOCK gene phase advance → sleep-wake cycle compression → positive feedback with mood elevation

### Bipolar depression biology

During bipolar depression (often longer and more disabling than mania):
- Reduced mesolimbic and mesocortical dopamine → anhedonia, psychomotor retardation, cognitive slowing
- Reduced serotonin → depressed mood, suicidality (similar to MDD)
- HPA dysregulation: unlike PTSD (hypocortisolemia) and MDD (hypercortisolemia) — BD shows mixed: elevated cortisol in acute depression but blunted diurnal rhythm; cortisol normalization correlates with mood recovery
- BDNF reduced in depressive episodes; restored with successful treatment

## Pathology

### Treatment

**Acute mania:**
- **Lithium** (serum target 0.8–1.2 mEq/L): effective for acute mania (~70% response); IV not available; takes 5–7 days for full effect; always combine with antipsychotic acutely
- **Atypical antipsychotics**: haloperidol (fastest), olanzapine, aripiprazole, risperidone, quetiapine — primary acute antimanic agents; D2 blockade rapidly reduces dopamine-driven mania within days
- **Valproate** (VPA): IV loading possible for rapid control; good for mixed features, rapid cycling, dysphoric mania; antimanic onset ~5 days; teratogenic
- **Benzodiazepines**: Lorazepam or clonazepam for behavioral control, sleep, anxiety — adjunctive; short-term only

**Bipolar depression (most challenging aspect):**
- **Quetiapine (Seroquel)**: FDA-approved for bipolar depression; 5-HT2A/D2 blockade + serotonergic modulation; 300–600 mg QD; most evidence
- **Lurasidone**: FDA-approved; good for bipolar depression with anxiety; weight-neutral
- **OFC (olanzapine-fluoxetine combination)**: FDA-approved; significant weight gain
- **Lamotrigine**: Excellent for bipolar depression prevention; slow titration required (Stevens-Johnson risk); not effective for acute mania
- **Lithium**: Effective for bipolar depression (add-on); also suicide prevention
- **Ketamine**: Emerging rapid-acting treatment for bipolar depression (IV racemic, intranasal esketamine); NMDA antagonism → rapid BDNF/mTOR-mediated synaptogenesis; mania switch risk with repeated use is low in current trials but monitoring required
- **SSRIs**: Generally avoided as monotherapy in BD — risk of manic switching; if used, always with mood stabilizer; evidence base weaker than in MDD

**Long-term maintenance (prevention of recurrence):**

| Drug | Best for | Key advantages | Key risks |
|:---|:---|:---|:---|
| **Lithium** | BD-I, suicide prevention, long-term stability | Only drug with Level 1 suicide prevention evidence; reduces BD mortality | Narrow TI (0.6–1.2 mEq/L); renal toxicity; thyroid dysfunction; teratogen; requires monitoring |
| **Valproate** | Mixed features, rapid cycling, mania prevention | Broader spectrum than lithium for cycling | Teratogenic (neural tube defects); PCOS; hepatotoxicity |
| **Lamotrigine** | Bipolar depression prevention, BD-II | No weight gain; depression focus; well-tolerated | Slow titration; Stevens-Johnson; poor acute mania efficacy |
| **Quetiapine** | Both poles; agitation | FDA-approved for all phases; sedating (useful for sleep) | Metabolic syndrome; tardive dyskinesia risk |
| **Aripiprazole** | BD-I maintenance; weight-neutral | Partial D2 agonist; low metabolic risk | Akathisia; activation can worsen agitation |
| **Long-acting injectable antipsychotics** | Non-adherence (major cause of relapse) | Bypasses daily pill adherence | Injection site reactions; metabolic effects |

**Lithium's unique properties:**
- Only mood stabilizer proven to reduce suicide attempts and completions (Cipriani 2013, meta-analysis)
- Neuroprotective: increases gray matter volume, preserves hippocampal volume, promotes neurogenesis
- Anti-inflammatory: reduces TNF-α, IL-6, NF-κB
- Telomere preservation: BD associated with accelerated telomere shortening; lithium attenuates this
- Long-term lithium users have lower rates of dementia — likely via GSK-3β → reduced tau pathology

**Psychosocial interventions (essential, evidence-based):**
- Psychoeducation: understanding prodromal symptoms, sleep as leading indicator of mood episode onset, medication adherence
- Interpersonal and Social Rhythm Therapy (IPSRT): stabilizes daily rhythms/sleep-wake cycles → reduces circadian dysregulation → fewer episodes
- Family-focused therapy: reduces high-expressed-emotion environments; reduces relapse
- Cognitive-behavioral therapy: relapse prevention, adherence, comorbid anxiety

## Connections

- `connects-to` → **[GSK-3β](../../../03-molecular/gsk-3b/README.md)** — lithium directly inhibits GSK-3β (uncompetitive Mg²⁺ site); GSK-3β hyperactivity in bipolar drives circadian dysregulation and BDNF suppression; lithium → β-catenin stabilization → neuroprotective gene expression and hippocampal neurogenesis.

- `connects-to` → **[Dopamine](../../../03-molecular/dopamine/README.md)** — mesolimbic dopamine hyperactivity drives manic symptoms; antipsychotics (D2 blockers) are first-line acute antimanic agents; mesocortical D1 hypofunction contributes to bipolar depression; dopamine catecholamine oscillation hypothesis explains mood cycling.

- `connects-to` → **[Serotonin](../../../03-molecular/serotonin/README.md)** — SSRIs risk manic switching in BD and are generally avoided as monotherapy; atypical antipsychotics with 5-HT2A blockade (quetiapine) effectively treat bipolar depression without switch risk; serotonin deficit contributes to depressive phases.

- `connects-to` → **[BDNF](../../../03-molecular/bdnf/README.md)** — BDNF Val66Met SNP increases bipolar risk; BDNF is reduced during depressive episodes; lithium and valproate both upregulate BDNF and BCL-2, promoting neurogenesis and neuroprotection as a common mood stabilizer mechanism.

- `connects-to` → **[GABA](../../../03-molecular/gaba/README.md)** — valproate potentiates GABA-A function and blocks voltage-gated Na⁺/Ca²⁺ channels; GABA deficiency in PFC is associated with bipolar depression; benzodiazepines provide acute antimanic sedation via GABA-A agonism.

- `targets` → **[Brain](../../../06-organ/brain/README.md)** — bipolar disorder features amygdala hyperreactivity and reduced vmPFC regulation; hippocampal volume is reduced ~6% (BD-I); DLPFC shows reduced working memory activation; long-term lithium partially reverses hippocampal volume loss.

[^grande-2016-bipolar-review]: Grande I, Berk M, Birmaher B, Vieta E. Bipolar disorder. *Lancet.* 2016;387(10027):1561-1572. [doi:10.1016/S0140-6736(15)00241-X](https://doi.org/10.1016/S0140-6736(15)00241-X) · [PubMed 26388529](https://pubmed.ncbi.nlm.nih.gov/26388529/)
[^geddes-2013-bipolar-treatment]: Geddes JR, Miklowitz DJ. Treatment of bipolar disorder. *Lancet.* 2013;381(9878):1672-1682. [doi:10.1016/S0140-6736(13)60857-0](https://doi.org/10.1016/S0140-6736(13)60857-0) · [PubMed 23663953](https://pubmed.ncbi.nlm.nih.gov/23663953/)
[^cipriani-2013-lithium-suicide]: Cipriani A, Hawton K, Stockton S, Geddes JR. Lithium in the prevention of suicide in mood disorders: updated systematic review and meta-analysis. *BMJ.* 2013;346:f3646. [doi:10.1136/bmj.f3646](https://doi.org/10.1136/bmj.f3646) · [PubMed 23814104](https://pubmed.ncbi.nlm.nih.gov/23814104/)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
