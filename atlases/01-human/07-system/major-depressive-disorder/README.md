---
schema: human-scale-entry/v1
id: major-depressive-disorder
name: Major Depressive Disorder
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-08
summary: "Major depressive disorder (280M affected) involves serotonergic/noradrenergic deficit, HPA dysregulation, neuroinflammation, and reduced BDNF neuroplasticity; SSRIs/SNRIs are first-line; ketamine (IV racemic or nasal esketamine) is the fastest-acting approved antidepressant."
aliases: ["major depressive disorder", "MDD", "depression", "unipolar depression", "TRD", "treatment-resistant depression", "antidepressant", "SSRI", "SNRI", "ketamine depression", "esketamine"]
sources:
  - id: cipriani-2018-antidepressants-meta
    type: peer-reviewed
    cite: "Cipriani A, Furukawa TA, Salanti G, et al. Comparative efficacy and acceptability of 21 antidepressant drugs for the acute treatment of adults with major depressive disorder: a systematic review and network meta-analysis. Lancet. 2018;391(10128):1357-1366."
    doi: "10.1016/S0140-6736(17)32802-7"
    pmid: "29477251"
    url: "https://doi.org/10.1016/S0140-6736(17)32802-7"
    accessed: "2026-06-08"
  - id: zarate-2006-ketamine-rapid
    type: peer-reviewed
    cite: "Zarate CA Jr, Singh JB, Carlson PJ, et al. A randomized trial of an N-methyl-D-aspartate antagonist in treatment-resistant major depression. Arch Gen Psychiatry. 2006;63(8):856-864."
    doi: "10.1001/archpsyc.63.8.856"
    pmid: "16894061"
    url: "https://doi.org/10.1001/archpsyc.63.8.856"
    accessed: "2026-06-08"
  - id: duman-2012-bdnf-depression
    type: peer-reviewed
    cite: "Duman RS, Aghajanian GK. Synaptic dysfunction in depression: potential therapeutic targets. Science. 2012;338(6103):68-72."
    doi: "10.1126/science.1222939"
    pmid: "23042884"
    url: "https://doi.org/10.1126/science.1222939"
    accessed: "2026-06-08"
cross_links:
  - target: 01-human/03-molecular/serotonin
    relation: connects-to
    note: "Reduced serotonergic neurotransmission is central to MDD; SSRIs (fluoxetine, sertraline, escitalopram) are first-line antidepressants; tryptophan depletion triggers depressive relapse in remitted MDD; 5-HT1A autoreceptor desensitization is required for delayed SSRI onset."
  - target: 01-human/03-molecular/norepinephrine
    relation: connects-to
    note: "SNRIs (venlafaxine, duloxetine) and TCAs raise synaptic NE via NET blockade; NE deficit underlies psychomotor retardation; mirtazapine (α2 antagonist) raises NE and 5-HT by blocking autoreceptors; melancholic MDD preferentially responds to NE-targeting antidepressants."
  - target: 01-human/03-molecular/cortisol
    relation: connects-to
    note: "HPA hyperactivation in MDD — elevated CRH, cortisol, blunted dexamethasone suppression — causes hippocampal atrophy via GR-mediated BDNF suppression; normalizing cortisol (mifepristone, CRH antagonists) correlates with antidepressant response; cortisol predicts remission."
  - target: 01-human/03-molecular/crh
    relation: connects-to
    note: "CRH hyperdrive from PVN and CeA drives HPA hyperactivation in MDD; elevated CSF CRH and blunted DST are the most replicated biomarkers; CRHR1 antagonists reduce depressive symptoms in trials; CRH excess causes hippocampal BDNF suppression and dendritic atrophy."
  - target: 01-human/03-molecular/bdnf
    relation: connects-to
    note: "BDNF deficiency is central to the neuroplasticity hypothesis of MDD: stress reduces hippocampal BDNF; antidepressants (SSRIs, MAOIs, ketamine) normalize BDNF; BDNF Val66Met SNP impairs activity-dependent secretion and increases MDD vulnerability to stress."
  - target: 01-human/06-organ/brain
    relation: targets
    note: "MDD involves reduced hippocampal volume (~2% per episode), reduced DLPFC gray matter, and hyperactive amygdala; functional dysconnectivity between DLPFC and limbic regions; subgenual cingulate (Area 25) hyperactivity is normalized by DBS and antidepressants."
  - target: 01-human/03-molecular/acth
    relation: connects-to
    note: "MDD features ACTH hypersecretion from CRH-driven corticotroph excess → hypercortisolemia; DST nonsuppression reflects HPA hyperdrive; blunted ACTH response to exogenous CRH indicates corticotroph downregulation; ACTH/cortisol normalisation with antidepressants predicts remission."
  - target: 01-human/03-molecular/prolactin
    relation: connects-to
    note: "Antipsychotic-induced hyperprolactinemia causes sexual dysfunction and anhedonia driving non-adherence; postpartum prolactin dynamics may modulate MDD vulnerability; cabergoline (D2 agonist) has shown adjunctive antidepressant effects in small trials."
  - target: 01-human/03-molecular/testosterone
    relation: connects-to
    note: "Male hypogonadism (T <300 ng/dL) predicts MDD risk; testosterone deficiency causes fatigue, anhedonia, and low libido indistinguishable from MDD; TRT has adjunctive antidepressant efficacy in hypogonadal men; SSRI-treated men with residual anhedonia benefit from TRT augmentation."
  - target: 01-human/03-molecular/estrogen
    relation: connects-to
    note: "Perimenopausal estrogen fluctuations trigger or worsen MDD; transdermal estradiol (100 mcg/day patch) has antidepressant efficacy in perimenopausal women; PMDD involves abnormal CNS sensitivity to allopregnanolone (progesterone metabolite) fluctuations, not estrogen deficiency."
  - target: 01-human/03-molecular/thyroid-hormones
    relation: connects-to
    note: "Hypothyroidism causes reversible depressive syndrome indistinguishable from MDD; TSH >10 mIU/L is a diagnostic exclusion for MDD; subclinical hypothyroidism accounts for ~10% of refractory MDD; T3 (25-50 mcg/day) augments antidepressant response in treatment-resistant depression."
  - target: 01-human/03-molecular/progesterone
    relation: connects-to
    note: "Luteal allopregnanolone fluctuations drive PMDD and PPD; declining P4 post-delivery triggers PPD; brexanolone (IV allopregnanolone) and zuranolone (oral) treat PPD; PMDD responds to SSRIs, combined OCP, or GnRH agonist; progesterone withdrawal worsens anxiety."
  - target: 01-human/03-molecular/melatonin
    relation: connects-to
    note: "Seasonal affective disorder (winter depression) involves delayed circadian phase and abnormal melatonin timing; agomelatine (MT1/MT2 agonist + 5-HT2C antagonist) is an approved antidepressant with circadian phase-advancing effects; light therapy resets SCN/melatonin phase in SAD."
---

# Major Depressive Disorder

## Overview

**Major depressive disorder (MDD)** is a common, recurrent, and potentially life-threatening psychiatric condition characterized by sustained depressed mood and/or anhedonia, representing the leading cause of disability worldwide. It affects approximately **280 million people globally** (~5% of the population), with a lifetime prevalence of 15–20% in high-income countries. Women are affected approximately twice as often as men. MDD is a top 5 cause of global disease burden by disability-adjusted life years (DALYs), ahead of ischemic heart disease and stroke in many countries.

**DSM-5 diagnostic criteria** require ≥5 of the following symptoms present ≥2 weeks (with at least one being depressed mood or anhedonia):
1. Depressed mood (nearly every day)
2. **Anhedonia** (loss of interest or pleasure — the most reliable diagnostic marker)
3. Significant weight change or appetite disturbance
4. Insomnia or hypersomnia
5. Psychomotor agitation or retardation (observable by others)
6. Fatigue or loss of energy
7. Feelings of worthlessness or excessive guilt
8. Difficulty concentrating or indecisiveness
9. Recurrent thoughts of death or suicidal ideation

MDD is distinct from **bereavement**, **bipolar depression** (which requires prior manic/hypomanic episode), **persistent depressive disorder** (dysthymia, ≥2 years of milder depression), and **secondary depression** (hypothyroidism, Cushing's, interferon therapy, corticosteroids).

## Structure

### Neuroanatomy of depression

Neuroimaging and postmortem studies consistently identify structural and functional abnormalities across a depression-specific circuit:

**Subgenual anterior cingulate cortex (sgACC, Brodmann Area 25):**
- Most consistently hyperactivated region in acute depression; increased metabolism on PET correlates with depression severity
- Deep brain stimulation (DBS) of white matter tracts adjacent to Area 25 (subcallosal cingulate tract) produces rapid remission in treatment-resistant MDD (~60% response at 1 year — Kennedy et al., NEJM Evidence 2022)
- Projects to brainstem monoamine nuclei (raphe, locus coeruleus) and hypothalamus; hyperactivation suppresses monoaminergic output and dysregulates HPA axis

**Hippocampus:**
- Volume reduced 2–5% in first-episode MDD; further atrophy (~0.5-1% per episode) with recurrent episodes — reversible with sustained antidepressant treatment
- Loss of CA1 and dentate gyrus pyramidal neurons; reduced subgranular zone neurogenesis
- Mechanism: glucocorticoid excess → GR-mediated BDNF suppression → loss of trophic support → dendritic atrophy and neuronal apoptosis

**Dorsolateral prefrontal cortex (DLPFC):**
- Reduced volume and metabolic activity (hypofrontality) correlates with cognitive symptoms (concentration, decision-making)
- Target of repetitive transcranial magnetic stimulation (rTMS; FDA-cleared for MDD)
- Reduced DLPFC activity → impaired top-down regulation of limbic hyperreactivity

**Amygdala:**
- Hyperactivated (increased metabolism; exaggerated to emotional stimuli); enlarged in first-episode MDD vs. controls
- Hyperactive amygdala → exaggerated negative emotional processing, increased stress reactivity, fear generalization → rumination

**Default Mode Network (DMN):**
- Increased DMN activity and connectivity during MDD → maladaptive self-referential processing (rumination, negative self-focus)
- Psilocybin and ketamine rapidly disrupt DMN hyperconnectivity → correlated with antidepressant response

## Function

### Monoamine hypothesis

The classical **monoamine deficiency hypothesis** (Schildkraut 1965) proposed that MDD arises from insufficient monoamine (serotonin, norepinephrine, dopamine) neurotransmission. Evidence:
- All effective conventional antidepressants increase monoamine availability (SSRI → 5-HT; SNRI → 5-HT + NE; TCAs → 5-HT + NE + DA; MAOIs → all monoamines)
- Tryptophan depletion (reduces brain 5-HT) causes relapse in SSRI-remitted patients
- Catecholamine depletion (alpha-methyl-para-tyrosine → reduces NE/DA) triggers depression in remitted patients treated with NE-preferring antidepressants

**Limitations:** The monoamine hypothesis alone is insufficient:
- Monoamine increase occurs within hours of antidepressant administration, but clinical benefit requires 2–4 weeks → downstream synaptic remodeling (BDNF-neuroplasticity) is required
- ~30% of patients do not respond to monoamine-targeting antidepressants (treatment-resistant depression)
- Tianeptine (a serotonin reuptake enhancer, not blocker) is an effective antidepressant → simple monoamine increase is not sufficient

### Neuroplasticity hypothesis (BDNF hypothesis)

Duman and Aghajanian (2012) [^duman-2012-bdnf-depression] proposed that MDD results from impaired synaptic plasticity — specifically from reduced BDNF-TrkB signaling in hippocampus and prefrontal cortex:

- **Chronic stress** → elevated cortisol → GR-mediated suppression of BDNF promoters → reduced BDNF in hippocampus → dendritic retraction, reduced LTP, impaired neurogenesis → depression-like phenotype (in rodent models)
- **Antidepressants** → ultimately increase BDNF regardless of primary mechanism (SSRI → 5-HT → CREB → BDNF; ketamine → AMPA stimulation → BDNF release; ECT → seizure → massive BDNF induction)
- Intra-hippocampal BDNF infusion produces antidepressant-like effects; dominant-negative TrkB blocks antidepressant response in rodents

### HPA axis dysregulation

In ~50% of MDD patients (especially severe/melancholic depression):
- **Elevated CRH** in CSF (excess hypothalamic drive)
- **Elevated basal cortisol** and flattened diurnal variation
- **Blunted dexamethasone suppression test (DST):** Failure to suppress cortisol after 1 mg dexamethasone (a GR agonist) indicates hypercortisolemia and HPA axis escape
- **Mechanism:** Reduced hippocampal GR expression (due to early-life stress and BDNF loss) → impaired negative feedback → HPA hyperactivity → more cortisol → more BDNF suppression → further hippocampal atrophy (vicious cycle)

Normalization of HPA axis (return of DST suppression) predicts remission better than symptom rating scales.

### Neuroinflammation

Approximately 30–40% of MDD patients have elevated inflammatory markers:
- **Elevated IL-6, TNF-α, CRP** in blood correlate with depression severity
- **IDO pathway activation:** Inflammatory cytokines induce indoleamine 2,3-dioxygenase (IDO) → converts tryptophan to kynurenine instead of serotonin → depletes serotonin and produces glutamate (quinolinic acid) → excitotoxic → NMDA receptor-mediated hippocampal injury
- **Microglia activation:** Translocator protein (TSPO) PET shows increased microglial activation in MDD vs. controls
- Anti-inflammatory antidepressants (celecoxib adjunct, infliximab for high-CRP patients) show efficacy in inflammatory subtype MDD

## Pathology

### Subtypes

| Subtype | Characteristics | Treatment implication |
|:---|:---|:---|
| **Melancholic depression** | Diurnal variation (worse AM), loss of reactivity, psychomotor retardation, marked anhedonia | TCAs or high-dose SSRIs; ECT for severe; ketamine; NE-targeted drugs (SNRIs, desipramine) |
| **Atypical depression** | Mood reactivity preserved; hypersomnia, hyperphagia, leaden paralysis, rejection sensitivity | MAOIs historically most effective; SSRIs effective; avoid TCAs |
| **Psychotic depression** | Delusions or hallucinations co-occurring with depression | Antidepressant + antipsychotic; ECT is first-line for psychotic depression |
| **Postpartum depression (PPD)** | Within 4 weeks post-delivery; associated with allopregnanolone withdrawal | Brexanolone (GABA-A neurosteroid) — FDA 2019; SSRIs safe in breastfeeding |
| **Seasonal affective disorder (SAD)** | Winter depression; hypersomnia, hyperphagia, carbohydrate craving | Light therapy (10,000 lux, 30 min AM); bupropion XL preventive |
| **Treatment-resistant depression (TRD)** | Failure of ≥2 adequate antidepressant trials | Augmentation (lithium, atypical antipsychotic, thyroid), ketamine/esketamine, ECT, DBS, psilocybin |

### Antidepressant pharmacology [^cipriani-2018-antidepressants-meta]

**First-line treatments — SSRIs and SNRIs:**

| Drug | Class | Mechanism | Notes |
|:---|:---|:---|:---|
| Escitalopram | SSRI | Most selective SERT inhibitor | Best efficacy/tolerability ratio in Cipriani 2018 meta-analysis |
| Sertraline | SSRI | SERT + weak DAT inhibition | Preferred in cardiac patients; most studied |
| Fluoxetine | SSRI | SERT; long half-life (2–6 days) | Low discontinuation syndrome risk; Prozac |
| Venlafaxine | SNRI | SERT >> NET at low doses; SERT + NET at higher doses | Better efficacy than SSRIs in severe depression |
| Duloxetine | SNRI | SERT + NET (more balanced than venlafaxine) | Also FDA-approved for chronic pain, diabetic neuropathy |
| Mirtazapine | Tetracyclic | α2 antagonist + 5-HT2A/C antagonist | No sexual side effects; sedating; weight gain; effective |

**Fast-acting antidepressants:**

**Ketamine/esketamine:**
- IV ketamine (0.5 mg/kg over 40 min): antidepressant effect within 2–4 hours; 70% response in treatment-resistant MDD (vs. ~30% for conventional antidepressants) [^zarate-2006-ketamine-rapid]
- Mechanism: NMDA receptor block → disinhibition of pyramidal neurons → AMPA stimulation → BDNF release → TrkB → mTOR → rapid synaptogenesis
- Esketamine (Spravato, nasal spray): FDA-approved 2019 for TRD and MDD with acute suicidal ideation; 56 mg or 84 mg twice weekly → weekly → biweekly
- Limitations: dissociation, transient BP increase, abuse potential; administered in supervised medical setting

**Brexanolone (Zulresso):**
- IV GABA-A neurosteroid agonist (synthetic allopregnanolone); FDA-approved 2019 for postpartum depression
- 60-hour IV infusion; ~70% remission vs. ~30% placebo; rapid effect (24–48h)
- Mechanistic implication: allopregnanolone withdrawal postpartum is a key trigger for PPD

**Psilocybin:**
- Two-dose psilocybin therapy (25 mg) produced sustained antidepressant effect at 12 weeks (Compass Pathways COMP360 Phase 2, 2022): 29% remission vs. 8% placebo at 3 weeks
- Mechanism: 5-HT2A agonism in PFC → disruption of DMN → enhanced cognitive flexibility; BDNF increase; neuroplasticity
- FDA Breakthrough Therapy designation for TRD; Phase 3 trials ongoing

**ECT and Neuromodulation:**
- **ECT (electroconvulsive therapy):** Most effective treatment for severe/refractory MDD (80% response); mechanism: generalized tonic-clonic seizure → massive monoamine and BDNF release → hippocampal neurogenesis; retrograde amnesia is primary side effect
- **rTMS (repetitive TMS):** 10 Hz stimulation of left DLPFC; FDA-cleared; ~40-50% response in TRD; Deep TMS (H-coil) reaches sgACC
- **DBS:** Subcallosal cingulate tract stimulation; 60% response in severe TRD at 1 year; investigational

### Risk and protective factors

**Genetic:** Heritability ~37% (lower than schizophrenia or bipolar); polygenic; GWAS identified >100 loci; 5-HTTLPR (SLC6A4 promoter) × stress interaction; BDNF Val66Met

**Environmental risk factors:** Early-life adversity (childhood abuse/neglect — 3× increased risk), chronic stress, socioeconomic factors, social isolation, chronic medical illness (cardiovascular, chronic pain)

**Protective factors:** Social support, aerobic exercise (reduces MDD risk by 25–35%), adequate sleep, omega-3 fatty acids, mindfulness, purpose/meaning

## Connections

- `connects-to` → **[Serotonin](../../../03-molecular/serotonin/README.md)** — reduced serotonergic neurotransmission is central to MDD; SSRIs are first-line antidepressants; tryptophan depletion triggers depressive relapse in remitted patients; 5-HT1A autoreceptor desensitization determines the delayed therapeutic onset of SSRIs.

- `connects-to` → **[Norepinephrine](../../../03-molecular/norepinephrine/README.md)** — NE deficit underlies psychomotor retardation and concentration difficulty in MDD; SNRIs (venlafaxine, duloxetine) block NET to raise synaptic NE; mirtazapine (α2 antagonist) increases NE and 5-HT by blocking autoreceptors; melancholic depression preferentially responds to NE-targeting drugs.

- `connects-to` → **[Cortisol](../../../03-molecular/cortisol/README.md)** — HPA axis hyperactivation in MDD — elevated CRH, cortisol, and blunted dexamethasone suppression — causes hippocampal atrophy via GR-mediated BDNF suppression; cortisol normalization predicts antidepressant response; mifepristone and CRH receptor antagonists are experimental antidepressants.

- `connects-to` → **[CRH](../../../03-molecular/crh/README.md)** — CRH hyperdrive from PVN and CeA drives the HPA hyperactivation of MDD; elevated CSF CRH and blunted dexamethasone suppression are the most replicated biological findings in MDD; CRHR1 antagonists and mifepristone (GR antagonist) show antidepressant activity; CRH excess drives hippocampal BDNF suppression and dendritic retraction.

- `connects-to` → **[BDNF](../../../03-molecular/bdnf/README.md)** — BDNF deficiency is central to the neuroplasticity hypothesis of MDD; stress reduces hippocampal BDNF via glucocorticoid-mediated CREB repression; all effective antidepressants (SSRIs, MAOIs, ketamine, ECT) ultimately normalize BDNF; Val66Met SNP increases MDD vulnerability.

- `targets` → **[Brain](../../../06-organ/brain/README.md)** — MDD involves reduced hippocampal volume (~2% per episode), DLPFC hypofrontality, hyperactive amygdala, and sgACC (Area 25) hyperactivation; functional DLPFC–limbic dysconnectivity; sgACC DBS produces rapid remission in severe TRD by normalizing Area 25 hypermetabolism.

- `connects-to` → **[ACTH](../../../03-molecular/acth/README.md)** — MDD shows HPA hyperdrive: CRH excess → ACTH hypersecretion → hypercortisolemia; paradoxically, the CRH stimulation test reveals blunted ACTH response (indicating corticotroph downregulation from chronic CRH excess); normalization of the ACTH/cortisol rhythm with antidepressant treatment reliably predicts and follows clinical remission.

- `connects-to` → **[Prolactin](../../../03-molecular/prolactin/README.md)** — antipsychotic-induced hyperprolactinemia causes sexual dysfunction and anhedonia driving non-adherence; postpartum prolactin dynamics (peaking at delivery then falling) may modulate MDD vulnerability via dopaminergic systems; cabergoline has shown adjunctive antidepressant effects in small trials.

- `connects-to` → **[Testosterone](../../../03-molecular/testosterone/README.md)** — Male hypogonadism (T <300 ng/dL) predicts MDD risk; testosterone deficiency causes fatigue, anhedonia, and low libido indistinguishable from MDD; TRT has adjunctive antidepressant efficacy in hypogonadal men; SSRI-treated men with residual anhedonia benefit from TRT augmentation.

- `connects-to` → **[Estrogen](../../../03-molecular/estrogen/README.md)** — Perimenopausal estrogen fluctuations trigger or worsen MDD; transdermal estradiol (100 mcg/day patch) has antidepressant efficacy in perimenopausal women; PMDD involves abnormal CNS sensitivity to allopregnanolone (progesterone metabolite) fluctuations, not estrogen deficiency.

- `connects-to` → **[Thyroid Hormones](../../../03-molecular/thyroid-hormones/README.md)** — Hypothyroidism causes reversible depressive syndrome indistinguishable from MDD; TSH >10 mIU/L is a diagnostic exclusion for MDD; subclinical hypothyroidism accounts for ~10% of refractory MDD; T3 (25-50 mcg/day) augments antidepressant response in treatment-resistant depression.

- `connects-to` → **[Progesterone](../../../03-molecular/progesterone/README.md)** — Luteal allopregnanolone fluctuations drive PMDD and PPD; declining P4 post-delivery triggers PPD; brexanolone (IV allopregnanolone) and zuranolone (oral) treat PPD; PMDD responds to SSRIs, combined OCP, or GnRH agonist; progesterone withdrawal worsens anxiety.

- `connects-to` → **[Melatonin](../../../03-molecular/melatonin/README.md)** — Seasonal affective disorder (winter depression) involves delayed circadian phase and abnormal melatonin timing; agomelatine (MT1/MT2 agonist + 5-HT2C antagonist) is an approved antidepressant with circadian phase-advancing effects; light therapy resets SCN/melatonin phase in SAD.

[^cipriani-2018-antidepressants-meta]: Cipriani A, Furukawa TA, Salanti G, et al. Comparative efficacy and acceptability of 21 antidepressant drugs for acute treatment of adults with major depressive disorder. *Lancet.* 2018;391(10128):1357-1366. [doi:10.1016/S0140-6736(17)32802-7](https://doi.org/10.1016/S0140-6736(17)32802-7) · [PubMed 29477251](https://pubmed.ncbi.nlm.nih.gov/29477251/)
[^zarate-2006-ketamine-rapid]: Zarate CA Jr, Singh JB, Carlson PJ, et al. A randomized trial of an N-methyl-D-aspartate antagonist in treatment-resistant major depression. *Arch Gen Psychiatry.* 2006;63(8):856-864. [doi:10.1001/archpsyc.63.8.856](https://doi.org/10.1001/archpsyc.63.8.856) · [PubMed 16894061](https://pubmed.ncbi.nlm.nih.gov/16894061/)
[^duman-2012-bdnf-depression]: Duman RS, Aghajanian GK. Synaptic dysfunction in depression: potential therapeutic targets. *Science.* 2012;338(6103):68-72. [doi:10.1126/science.1222939](https://doi.org/10.1126/science.1222939) · [PubMed 23042884](https://pubmed.ncbi.nlm.nih.gov/23042884/)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
