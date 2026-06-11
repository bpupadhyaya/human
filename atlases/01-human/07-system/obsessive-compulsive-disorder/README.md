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

[^abramowitz-2009-ocd-review]: Abramowitz JS, Taylor S, McKay D. Obsessive-compulsive disorder. *Lancet.* 2009;374(9688):491-499. [doi:10.1016/S0140-6736(09)60240-3](https://doi.org/10.1016/S0140-6736(09)60240-3) · [PubMed 19665647](https://pubmed.ncbi.nlm.nih.gov/19665647/)
[^chamberlain-2008-ocd-neuroscience]: Chamberlain SR, Menzies L, Hampshire A, et al. Orbitofrontal dysfunction in patients with OCD and their unaffected relatives. *Science.* 2008;321(5887):421-422. [doi:10.1126/science.1154433](https://doi.org/10.1126/science.1154433) · [PubMed 18635808](https://pubmed.ncbi.nlm.nih.gov/18635808/)
[^pittenger-2017-ocd-glutamate]: Pittenger C. Glutamate and anxiety disorders. *Curr Top Behav Neurosci.* 2015;23:145-168. [doi:10.1007/7854_2014_295](https://doi.org/10.1007/7854_2014_295) · [PubMed 25091538](https://pubmed.ncbi.nlm.nih.gov/25091538/)
[^soomro-2008-ssri-ocd]: Soomro GM, Altman D, Rajagopal S, Oakley-Browne M. SSRIs versus placebo for OCD. *Cochrane Database Syst Rev.* 2008;(1):CD001765. [doi:10.1002/14651858.CD001765.pub3](https://doi.org/10.1002/14651858.CD001765.pub3) · [PubMed 18253995](https://pubmed.ncbi.nlm.nih.gov/18253995/)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
