---
schema: human-scale-entry/v1
id: attention-deficit-hyperactivity-disorder
name: Attention-Deficit/Hyperactivity Disorder
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-08
summary: "ADHD (5-10% prevalence; 4:1 male:female) is driven by prefrontal cortex dopamine/norepinephrine deficiency impairing executive function; stimulants (methylphenidate, amphetamines) are first-line; 60-70% of childhood ADHD persists into adulthood."
aliases: ["ADHD", "attention deficit hyperactivity disorder", "ADD", "attention deficit disorder", "hyperactivity disorder", "ADHD inattentive type", "ADHD combined type"]
sources:
  - id: faraone-2021-adhd-primer
    type: peer-reviewed
    cite: "Faraone SV, Banaschewski T, Coghill D, et al. The World Federation of ADHD International Consensus Statement: 208 Evidence-based conclusions about the disorder. Neurosci Biobehav Rev. 2021;128:789-818."
    doi: "10.1016/j.neubiorev.2021.01.022"
    pmid: "33549739"
    url: "https://doi.org/10.1016/j.neubiorev.2021.01.022"
    accessed: "2026-06-08"
  - id: arnsten-2009-adhd-neuroscience
    type: peer-reviewed
    cite: "Arnsten AF. Toward a new understanding of attention-deficit hyperactivity disorder pathophysiology: an important role for prefrontal cortex dysfunction. CNS Drugs. 2009;23(Suppl 1):33-41."
    doi: "10.2165/00023210-200923000-00005"
    pmid: "19621976"
    url: "https://doi.org/10.2165/00023210-200923000-00005"
    accessed: "2026-06-08"
  - id: biederman-2005-adhd-adults
    type: peer-reviewed
    cite: "Biederman J, Faraone SV. Attention-deficit hyperactivity disorder. Lancet. 2005;366(9481):237-248."
    doi: "10.1016/S0140-6736(05)66915-2"
    pmid: "16023516"
    url: "https://doi.org/10.1016/S0140-6736(05)66915-2"
    accessed: "2026-06-08"
cross_links:
  - target: 01-human/03-molecular/dopamine
    relation: connects-to
    note: "ADHD involves hypofunctional PFC dopamine D1 receptor signaling impairing working memory and executive control; methylphenidate and amphetamines increase synaptic dopamine/NE; COMT Val158Met SNP (rapid dopamine catabolism) increases ADHD risk and alters stimulant response."
  - target: 01-human/03-molecular/norepinephrine
    relation: connects-to
    note: "NE α2A-receptor signaling in PFC strengthens layer III pyramidal neuron connectivity underlying working memory; atomoxetine (selective NE reuptake inhibitor) and guanfacine/clonidine (α2A agonists) treat ADHD by restoring NE-PFC function without dopamine-reward effects."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "ADHD involves PFC, anterior cingulate cortex, striatum, and cerebellum circuit dysfunction; MRI shows ~3% smaller total brain volume; PFC gray matter thinning delays 2-5 years relative to controls; default mode network fails to deactivate during tasks → attention lapses."
  - target: 01-human/03-molecular/bdnf
    relation: connects-to
    note: "BDNF Val66Met SNP is over-represented in ADHD; BDNF supports PFC dopaminergic circuit maturation; stimulant treatment increases BDNF expression in PFC; exercise (which raises BDNF) reduces ADHD symptom severity in children and improves executive function outcomes."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "PFC layer III pyramidal neurons are the core ADHD substrate; they express DA D1 and NE α2A receptors maintaining persistent firing for working memory; D1 → cAMP → HCN/K⁺ channel closure → strengthened circuit; catecholamine deficiency → HCN open → signal noise → inattention."
  - target: 01-human/07-system/autism-spectrum-disorder
    relation: connects-to
    note: "ADHD and ASD co-occur in 20-50% of cases; DSM-5 (2013) allows dual diagnosis; both share genetic architecture (CNVs at 16p13.11, 1q21.1; FOXP2, SHANK3) and PFC-striatal circuit dysfunction; methylphenidate has lower efficacy and more side effects in ASD+ADHD vs ADHD alone."
  - target: 01-human/05-tissue/hippocampus
    relation: connects-to
    note: "Hippocampus is ~3-4% smaller in ADHD (meta-analysis); working memory deficits partly reflect hippocampal-PFC circuit dysfunction; stimulants normalize hippocampal-PFC connectivity on fMRI; episodic memory impairment is an underrecognized domain affecting academic performance."
  - target: 01-human/07-system/bulimia-nervosa
    relation: connects-to
    note: "ADHD and bulimia nervosa are linked by impulsivity and reward dysregulation: childhood ADHD roughly doubles later bulimia risk, with shared deficits in prefrontal inhibitory control and dopaminergic reward driving both loss-of-control eating and impulsive behavior."
  - target: 01-human/07-system/stimulant-use-disorder
    relation: connects-to
    note: "ADHD and stimulant use disorder share a dopaminergic core: untreated ADHD raises later substance-use risk, yet properly prescribed stimulants lower it; still, the same drugs carry misuse and diversion potential, so prescribing balances benefit against addiction risk."
  - target: 01-human/07-system/bipolar-disorder
    relation: connects-to
    note: "ADHD and bipolar disorder overlap and are easily confused: both feature distractibility, impulsivity, and high energy, but ADHD is chronic and trait-like while bipolar elevation is episodic; they co-occur, and stimulants are used cautiously in bipolar ADHD to avoid mania."
---

# Attention-Deficit/Hyperactivity Disorder

## Overview

**Attention-deficit/hyperactivity disorder (ADHD)** is one of the most common neurodevelopmental disorders, affecting approximately **5-10% of children** and **2.5-5% of adults** worldwide — roughly 366 million adults globally [^faraone-2021-adhd-primer]. It is characterized by persistent, developmentally inappropriate inattention, hyperactivity, and impulsivity that impairs functioning across multiple settings (home, school, work). ADHD is the most heritable common psychiatric disorder (~75–80% heritability in twin studies) and is defined by a complex polygenetic architecture.

**ADHD is not a deficit of attention per se** — it is more accurately understood as a **deficit in executive regulation of attention**: the ability to direct, sustain, and shift attention according to goals rather than immediate stimuli. Crucially, ADHD individuals can hyperfocus intensely on high-interest activities while being unable to sustain attention on low-interest tasks — reflecting motivational rather than attentional capacity differences [^arnsten-2009-adhd-neuroscience].

ADHD persists into adulthood in approximately **60-70%** of childhood cases (though symptoms may shift from overt hyperactivity to inner restlessness and disorganization). Adult ADHD is associated with markedly elevated rates of underemployment, relationship instability, accidental injury, substance use disorders (~25% comorbidity), and a 13-year reduction in life expectancy in the most severely affected.

**DSM-5 ADHD subtypes:**
- **Combined presentation (ADHD-C):** ≥6 inattentive + ≥6 hyperactive-impulsive symptoms; ~50-70% of cases
- **Predominantly Inattentive (ADHD-PI, "ADD"):** ≥6 inattentive symptoms; ~20-30%; under-diagnosed, especially in females
- **Predominantly Hyperactive-Impulsive (ADHD-PH):** ≥6 hyperactive-impulsive symptoms; ~5-15%; most common presentation in preschool children

## Structure

### Neurobiological basis: PFC catecholamine deficit [^arnsten-2009-adhd-neuroscience]

The dominant neurobiological model of ADHD centers on **prefrontal cortex (PFC) dysfunction driven by dopamine (DA) and norepinephrine (NE) deficiency**:

**PFC and executive function:**
The PFC (dorsolateral PFC, anterior cingulate cortex, orbital PFC) is the neural substrate of executive function: working memory, response inhibition, attentional control, and decision-making. PFC layer III pyramidal neurons maintain persistent firing representing task-relevant information ("working memory"). This persistent activity requires optimal DA D1 and NE α2A receptor stimulation:

| Signal | Receptor | Effect at optimal level | Effect at deficit |
|:---|:---|:---|:---|
| **Dopamine** | D1 (Gs/cAMP) → closes HCN/K⁺ channels | Strengthens task-relevant PFC column connectivity | Weakens signal; distraction prevails |
| **Norepinephrine** | α2A (Gi/cAMP↓) → HCN channel closure | Strengthens working memory networks | NE deficiency → HCN channels open → signal noise |

**"Inverted-U" tuning:** Both DA and NE PFC effects follow an inverted-U concentration curve — too little OR too much impairs PFC function. Stimulants optimize catecholamines by increasing synaptic levels from sub-optimal to optimal (rather than simply "adding more").

**Striatal dopamine and reward:** Mesolimbic (VTA→striatum) dopamine is also affected — reduced dopamine release to non-immediate rewards reduces motivation for deferred outcomes, contributing to impulsivity and procrastination. This is distinct from the PFC catecholamine deficit driving inattention.

### Neural circuit abnormalities (neuroimaging)

MRI studies in ADHD (pooled N > 10,000) reveal:
- **Total brain volume:** ~3-5% smaller than non-ADHD controls; delay of ~2-5 years in cortical maturation; volume difference normalizes partially with age
- **PFC gray matter:** Dorsolateral and anterior cingulate PFC thinning correlates with ADHD severity; right-predominant
- **Caudate nucleus:** Smaller; normalizes with stimulant treatment (suggesting medication normalizes volume)
- **Cerebellum:** 3-5% smaller; contributes to timing and motor control deficits
- **Default mode network (DMN):** Fails to deactivate during tasks → competes with task-positive networks → internal thoughts interrupt goal-directed behavior ("mind wandering")
- **White matter:** Reduced fractional anisotropy (FA) in frontostriatal and frontoparietal tracts

## Function

### DSM-5 symptom criteria

**Inattention (≥6 of 9 for ≥6 months, not explained by developmental level):**
- Often fails to give close attention to details; careless mistakes
- Difficulty sustaining attention in tasks or play
- Does not seem to listen when spoken to directly
- Does not follow through on instructions; fails to finish tasks
- Difficulty organizing tasks; poor time management
- Avoids, dislikes, or reluctantly engages tasks requiring sustained mental effort
- Often loses things necessary for tasks
- Easily distracted by extraneous stimuli
- Often forgetful in daily activities

**Hyperactivity-Impulsivity (≥6 of 9 symptoms for ≥6 months):**
- Often fidgets or squirms; leaves seat when expected to remain seated
- Runs/climbs when inappropriate (in adults: feelings of restlessness)
- Unable to engage in leisure activities quietly
- "On the go," "driven by a motor"
- Often talks excessively; blurts out answers; difficulty waiting turn
- Often interrupts or intrudes on others

**Diagnostic requirements:** Symptoms present before age 12; present in ≥2 settings; impair social, academic, or occupational function; not exclusively during psychosis or another disorder.

### ADHD in females

ADHD is diagnosed ~4:1 male:female in children, narrowing to ~2:1 in adults. Female under-diagnosis is a recognized systemic bias:
- Females more often present with inattentive (not hyperactive) subtype — less disruptive, less likely to trigger referral
- Females develop more effective compensatory strategies masking impairment
- Comorbid anxiety and depression (more common in females with ADHD) are often treated without the underlying ADHD being identified
- Female ADHD symptoms often worsen with hormonal fluctuations (premenstrual, peripartum, menopause) due to estrogen-dopamine interaction

### Comorbidities

| Comorbidity | Frequency | Notes |
|:---|:---|:---|
| Anxiety disorders | ~50% | Can co-exist with ADHD; distinguish from ADHD-driven "worry about consequences of inattention" |
| Major depressive disorder | ~35% | Often secondary to ADHD-related failures; treat ADHD first |
| Oppositional defiant disorder (ODD) | ~60% in children | Treat with ADHD medications + behavioral therapy |
| Learning disabilities | ~45% | Distinct from ADHD; reading disorder (dyslexia) most common |
| Substance use disorders | ~25% | ADHD is a major risk factor; treatment with stimulants reduces SUD risk |
| Autism spectrum disorder | ~20-50% | Significant overlap; both can co-exist per DSM-5 (allowed since 2013) |
| Tic disorder/Tourette | ~10-20% | Stimulants rarely worsen tics contrary to previous concern |
| Sleep disorders | ~75% | Delayed sleep phase (DSPS) very common; poor sleep worsens ADHD |

## Pathology

### Genetics

ADHD heritability: **75-80%** (twin studies), making it the most heritable common psychiatric disorder.

**Candidate gene associations (before GWAS):**
- **DAT1/SLC6A3:** Dopamine transporter; 10-repeat VNTR in 3'UTR associated with ADHD; methylphenidate is a DAT inhibitor
- **DRD4 7-repeat:** D4 receptor exon III 7-repeat allele; associated with ADHD, novelty-seeking; encodes reduced-sensitivity receptor
- **DRD5:** D5 receptor microsatellite polymorphism; meta-analytic association
- **COMT Val158Met:** Met allele → slower dopamine catabolism → higher PFC DA; Val allele → faster catabolism → lower PFC DA → ADHD risk; affects stimulant response
- **SNAP25:** Synaptosomal-associated protein 25; presynaptic DA release

**GWAS (2019, iPSYCH/deCODE, N > 55,000):** 12 genome-wide significant loci identified; genes implicated in neuronal development (FOXP2, STK39) and DA/NE signaling; SNP heritability ~22%; most loci are shared with educational attainment, executive function, and other psychiatric disorders.

**Copy number variants (CNVs):** 16p13.11 duplications, 1q21.1 deletions, and chromosomal regions overlapping with ASD and schizophrenia — ADHD shares genetic architecture with multiple neurodevelopmental conditions.

### Diagnosis and assessment

ADHD is a clinical diagnosis requiring [^biederman-2005-adhd-adults]:
1. Comprehensive history (parent/teacher/self-report rating scales)
2. **Rating scales:** Conners 3, ADHD Rating Scale-5 (ADHD-RS-5), Adult ADHD Self-Report Scale (ASRS)
3. Cognitive testing (not required but informative): TOVA, CPT (sustained attention); BRIEF-2 (executive function)
4. Neuroimaging and EEG: NOT diagnostic (no biomarker distinguishes ADHD from controls at individual level)
5. Rule out: thyroid dysfunction, sleep apnea, vision/hearing deficits, mood disorders, substance use

**EEG:** Elevated theta/alpha power and reduced beta power at frontal electrodes are group-level findings but not diagnostic. Theta/beta ratio: FDA cleared as adjunctive tool but insufficient alone for diagnosis.

### Treatment

**Stimulant medications — first-line:**

| Drug class | Mechanism | Examples | Onset/Duration |
|:---|:---|:---|:---|
| **Methylphenidate (MPH)** | Blocks DAT and NET reuptake | Ritalin (IR), Concerta (OROS), Jornay PM (delayed-release), Daytrana (patch) | IR: 4h; ER: 8-12h |
| **Amphetamine** | Blocks DAT/NET + reverses transporter (active DA/NE release) | Adderall XR, Vyvanse (lisdexamfetamine, prodrug), Dexedrine | IR: 4-6h; XR: 10-14h |

- Response rate: ~70-80% for any stimulant; if one stimulant class fails, try the other
- Effect sizes: Cohen's d ~0.8-1.0 for core ADHD symptoms (one of the highest in psychiatry)
- Safety: Modest appetite suppression (most children stay within normal growth curves), heart rate/BP increase (~3-5 bpm/1-2 mmHg average); cardiovascular screening required
- Lisdexamfetamine (Vyvanse): prodrug converted to d-amphetamine by red blood cell enzymes → lower abuse potential; FDA-approved for ADHD and binge eating disorder

**Non-stimulant medications — second-line:**

| Drug | Mechanism | Use case |
|:---|:---|:---|
| **Atomoxetine (Strattera)** | Selective NE reuptake inhibitor | Stimulant intolerance, active substance use disorder, tic disorder |
| **Guanfacine ER (Intuniv)** | α2A agonist | Combined with stimulants for incomplete response; especially for hyperactivity/impulsivity |
| **Clonidine ER (Kapvay)** | α2A/α2B/α2C agonist | Similar to guanfacine; also treats sleep-onset insomnia in ADHD |
| **Viloxazine ER (Qelbree)** | NE reuptake inhibitor + 5-HT2B antagonist | Newer FDA-approved non-stimulant; faster onset than atomoxetine |
| **Bupropion** | DA/NE reuptake inhibitor | Off-label; useful if comorbid depression; lower effect size than stimulants |

**Behavioral interventions:**
- **Children:** Behavioral parent training (BPT) is evidence-based; organizational skills training; school accommodations (extended time, preferential seating, reduced-distraction environment)
- **Adults:** CBT for ADHD (CBT-ADHD) addresses maladaptive beliefs, time management deficits, emotional dysregulation; combined with medication superior to either alone
- **Exercise:** Acute aerobic exercise (20-30 min) produces ~24-hour reduction in ADHD symptoms; chronic exercise raises BDNF, increases catecholamine release, and improves executive function — recommended as adjunct

## Connections

- `connects-to` → **[Dopamine](../../03-molecular/dopamine/README.md)** — ADHD involves hypofunctional PFC D1 receptor signaling impairing working memory; methylphenidate and amphetamines increase synaptic dopamine; COMT Val158Met SNP (rapid catabolism) increases ADHD risk; striatal dopamine deficiency reduces reward motivation and drives impulsivity.
- `connects-to` → **[Norepinephrine](../../03-molecular/norepinephrine/README.md)** — NE α2A-receptor signaling in PFC strengthens layer III pyramidal neuron connectivity underlying working memory; atomoxetine (selective NE reuptake inhibitor) and guanfacine/clonidine (α2A agonists) treat ADHD by restoring NE-PFC function without dopamine-reward circuit effects.
- `connects-to` → **[Brain](../../06-organ/brain/README.md)** — ADHD involves PFC, anterior cingulate, and striatal circuit dysfunction; MRI shows ~3-5% smaller total brain volume with 2-5 year cortical maturation delay; default mode network fails to deactivate during tasks → attention lapses; PFC gray matter thinning correlates with ADHD severity.
- `connects-to` → **[BDNF](../../03-molecular/bdnf/README.md)** — BDNF Val66Met SNP is over-represented in ADHD; BDNF supports PFC dopaminergic circuit maturation; stimulant treatment increases BDNF in PFC; aerobic exercise, which robustly raises BDNF, reduces ADHD symptom severity and improves executive function outcomes.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — PFC layer III pyramidal neurons are the core ADHD substrate; they express DA D1 and NE α2A receptors maintaining persistent firing for working memory; D1 → cAMP → HCN/K⁺ channel closure → strengthened circuit; catecholamine deficiency → HCN open → signal noise → inattention.
- `connects-to` → **[Autism Spectrum Disorder](../autism-spectrum-disorder/README.md)** — ADHD and ASD co-occur in 20-50% of cases; DSM-5 (2013) allows dual diagnosis; both share genetic architecture (CNVs at 16p13.11, 1q21.1; FOXP2, SHANK3) and PFC-striatal circuit dysfunction; methylphenidate has lower efficacy and more side effects in ASD+ADHD vs ADHD alone.
- `connects-to` → **[Hippocampus](../../05-tissue/hippocampus/README.md)** — hippocampus is ~3-4% smaller in ADHD (meta-analysis); working memory deficits partly reflect hippocampal-PFC circuit dysfunction; stimulants normalize hippocampal-PFC connectivity on fMRI; episodic memory impairment is an underrecognized domain affecting academic performance.
- `connects-to` → **[Bulimia Nervosa](../bulimia-nervosa/README.md)** — ADHD and bulimia nervosa are linked by impulsivity and reward dysregulation: childhood ADHD roughly doubles later bulimia risk, with shared deficits in prefrontal inhibitory control and dopaminergic reward driving both loss-of-control eating and impulsive behavior.
- `connects-to` → **[Stimulant Use Disorder](../stimulant-use-disorder/README.md)** — ADHD and stimulant use disorder share a dopaminergic core: untreated ADHD raises later substance-use risk, yet properly prescribed stimulants lower it; still, the same drugs carry misuse and diversion potential, so prescribing balances benefit against addiction risk.
- `connects-to` → **[Bipolar Disorder](../bipolar-disorder/README.md)** — ADHD and bipolar disorder overlap and are easily confused: both feature distractibility, impulsivity, and high energy, but ADHD is chronic and trait-like while bipolar elevation is episodic; they co-occur, and stimulants are used cautiously in bipolar ADHD to avoid mania.

[^faraone-2021-adhd-primer]: Faraone SV, Banaschewski T, Coghill D, et al. The World Federation of ADHD International Consensus Statement: 208 Evidence-based conclusions about the disorder. *Neurosci Biobehav Rev.* 2021;128:789-818. [doi:10.1016/j.neubiorev.2021.01.022](https://doi.org/10.1016/j.neubiorev.2021.01.022) · [PubMed 33549739](https://pubmed.ncbi.nlm.nih.gov/33549739/)
[^arnsten-2009-adhd-neuroscience]: Arnsten AF. Toward a new understanding of ADHD pathophysiology: an important role for prefrontal cortex dysfunction. *CNS Drugs.* 2009;23(Suppl 1):33-41. [doi:10.2165/00023210-200923000-00005](https://doi.org/10.2165/00023210-200923000-00005) · [PubMed 19621976](https://pubmed.ncbi.nlm.nih.gov/19621976/)
[^biederman-2005-adhd-adults]: Biederman J, Faraone SV. Attention-deficit hyperactivity disorder. *Lancet.* 2005;366(9481):237-248. [doi:10.1016/S0140-6736(05)66915-2](https://doi.org/10.1016/S0140-6736(05)66915-2) · [PubMed 16023516](https://pubmed.ncbi.nlm.nih.gov/16023516/)

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
