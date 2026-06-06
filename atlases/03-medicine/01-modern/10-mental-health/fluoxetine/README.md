---
schema: medicine-entry/v1
id: fluoxetine
name: Fluoxetine
atlas: 03-medicine
scale: 01-modern
status: draft
last_reviewed: 2026-06-06
summary: "Selective serotonin reuptake inhibitor (SSRI); blocks SERT → ↑ synaptic 5-HT → downstream neuroplasticity via BDNF/TrkB. First-line for MDD, OCD, panic disorder, bulimia, PMDD. Long half-life (1–6 days + active metabolite). Prozac; ~40 million users."
aliases: ["fluoxetine", "Prozac", "Sarafem", "Selfemra", "fluoxetine hydrochloride", "N-methyl-3-phenyl-3-[4-(trifluoromethyl)phenoxy]propan-1-amine"]
sources:
  - id: cipriani-2018-antidepressants
    type: peer-reviewed
    cite: "Cipriani A, Furukawa TA, Salanti G, et al. Comparative efficacy and acceptability of 21 antidepressant drugs for the acute treatment of adults with major depressive disorder. Lancet. 2018;391(10128):1357-1366."
    doi: "10.1016/S0140-6736(17)32802-7"
    pmid: "29477251"
    url: "https://doi.org/10.1016/S0140-6736(17)32802-7"
  - id: preskorn-2003-fluoxetine
    type: peer-reviewed
    cite: "Preskorn SH. Clinically relevant pharmacology of selective serotonin reuptake inhibitors. An overview with emphasis on pharmacokinetics and effects on oxidative drug metabolism. Clin Pharmacokinet. 1997;32 Suppl 1:1-21."
    doi: "10.2165/00003088-199700321-00003"
    pmid: "9068931"
    url: "https://doi.org/10.2165/00003088-199700321-00003"
  - id: krishnan-2008-ssri-neuroplasticity
    type: peer-reviewed
    cite: "Castrén E, Rantamäki T. The role of BDNF and its receptors in depression and antidepressant drug action: reactivation of developmental plasticity. Dev Neurobiol. 2010;70(5):289-97."
    doi: "10.1002/dneu.20758"
    pmid: "20186710"
    url: "https://doi.org/10.1002/dneu.20758"
  - id: walker-2019-fluoxetine-paediatric
    type: peer-reviewed
    cite: "Hammad TA, Laughren T, Racoosin J. Suicidality in pediatric patients treated with antidepressant drugs. Arch Gen Psychiatry. 2006;63(3):332-9."
    doi: "10.1001/archpsyc.63.3.332"
    pmid: "16520440"
    url: "https://doi.org/10.1001/archpsyc.63.3.332"
cross_links:
  - target: 01-human/03-molecular/serotonin
    relation: modulates
    evidence: preskorn-2003-fluoxetine
    note: "Fluoxetine selectively blocks SERT (serotonin transporter, SLC6A4) → prolongs synaptic 5-HT dwell time → desensitization of presynaptic 5-HT1A autoreceptors over 2–4 weeks → sustained ↑ serotonergic neurotransmission in limbic and prefrontal circuits."
  - target: 01-human/03-molecular/bdnf
    relation: modulates
    evidence: krishnan-2008-ssri-neuroplasticity
    note: "Chronic SSRI treatment upregulates BDNF expression and TrkB signaling in hippocampus — reversing stress-induced hippocampal atrophy; this neuroplastic mechanism likely underlies the delayed 2–6 week therapeutic onset."
---

# Fluoxetine

## Overview

**Fluoxetine** (Prozac), introduced in 1987, was the first **selective serotonin reuptake inhibitor (SSRI)** to achieve widespread clinical use and became the world's most prescribed antidepressant in the 1990s. It is a racemic phenylpropylamine derivative that selectively blocks the **serotonin transporter (SERT, SLC6A4)** with high selectivity over norepinephrine and dopamine transporters — a pharmacological profile that gave it a substantially improved tolerability and safety profile compared with earlier tricyclic antidepressants.

Fluoxetine is approved for **major depressive disorder (MDD)**, **obsessive-compulsive disorder (OCD)**, **panic disorder**, **bulimia nervosa**, **premenstrual dysphoric disorder (PMDD)**, and bipolar depression (in combination with olanzapine). It is the only antidepressant FDA-approved for depression in children (8+ years) and adolescents. An estimated 40 million people have taken fluoxetine — its cultural impact is reflected in the 1994 book "Listening to Prozac."

A distinctive pharmacokinetic feature is its **exceptionally long half-life**: ~1–4 days for fluoxetine itself, and ~4–16 days for its active metabolite **norfluoxetine** — the longest of any SSRI. This provides protection against discontinuation syndrome but means drug interactions persist for weeks after stopping.

## Mechanism

**Serotonin transporter (SERT) inhibition:**
1. **SERT function:** SERT is a Na⁺/Cl⁻-dependent cotransporter located on presynaptic serotonergic neurons (dorsal raphe nuclei → limbic system, prefrontal cortex, striatum). It reuptakes synaptic serotonin (5-HT) back into the presynaptic terminal following release — the primary mechanism terminating serotonergic neurotransmission
2. **Acute SERT block:** Fluoxetine binds the outward-facing conformation of SERT (at the central binding site), blocking serotonin re-entry; synaptic 5-HT concentration rises immediately. Ki ~0.8 nM for SERT; >1000× selectivity over NET and DAT
3. **Presynaptic autoreceptor desensitization (the delayed mechanism):** Acutely, elevated synaptic 5-HT activates presynaptic 5-HT1A somatodendritic autoreceptors → **reduces neuronal firing** (negative feedback) — this counteracts the SERT blockade initially. Over 2–4 weeks, these autoreceptors **desensitize/downregulate** → loss of feedback inhibition → sustained increase in 5-HT release + SERT blockade = net increase in serotonergic tone. This explains the 2–6 week delay to antidepressant effect
4. **Downstream neuroplasticity:** Chronic elevated 5-HT → activation of postsynaptic 5-HT2A and 5-HT4 receptors → cAMP/PKA signaling → **CREB phosphorylation** → upregulation of **BDNF (brain-derived neurotrophic factor)** → TrkB receptor activation → MAPK/ERK and PI3K/Akt pathways → dendritic spine density restoration and hippocampal neurogenesis [^krishnan-2008-ssri-neuroplasticity]. This neuroplastic effect is increasingly understood as the core mechanism of antidepressant action — not merely serotonin levels per se

**Key pharmacokinetic features:**
- Oral bioavailability: ~72%
- Plasma protein binding: ~94%
- Extensively metabolized by **CYP2D6** to **norfluoxetine** (active, similar potency, even longer t½ 4–16 days)
- Fluoxetine is also a **potent CYP2D6 inhibitor** — important drug interactions (codeine → morphine conversion blocked; tamoxifen → endoxifen conversion reduced; TCAs, antipsychotics elevated)
- Half-life: 1–6 days (fluoxetine) + 4–16 days (norfluoxetine) — washout takes 5–7 weeks

## Clinical Use

**Major Depressive Disorder (MDD):**
- Standard dose: 20 mg OD (morning, with or without food); may increase to 40–60 mg after 4–8 weeks if inadequate response
- Cipriani 2018 network meta-analysis (21 antidepressants, 116,477 patients): Fluoxetine was used as the reference drug; all SSRIs significantly more effective than placebo (OR ~1.8–2.2 for response) [^cipriani-2018-antidepressants]
- FDA-approved for depression in children ≥8 years and adolescents (only SSRI with this pediatric approval)

**OCD:**
- Dose: 20–80 mg/day; higher doses often required (60 mg OD effective)
- Response: 40–60% patients show ≥25% reduction in Y-BOCS score

**Bulimia Nervosa:**
- Only FDA-approved pharmacotherapy for bulimia
- Dose: 60 mg OD (higher than for depression); reduces binge-purge frequency ~50–67%

**Panic Disorder:**
- Start 10 mg (to avoid initial anxiogenic effect from acute 5-HT surge); titrate to 20–60 mg

**Discontinuation:**
- Due to the very long half-life, fluoxetine withdrawal syndrome is **rare** (gradual self-tapering via slow drug elimination)
- No dose tapering required in most patients — simply stop; this makes it useful for patients who frequently miss doses

**Adverse effects:**
- **GI:** Nausea (20–30%, most common; give with food; transient), diarrhea
- **Sexual dysfunction:** Delayed ejaculation, anorgasmia (20–40%); most common reason for non-adherence
- **Insomnia/activation:** Give in morning; some patients report agitation initially
- **Weight:** Neutral short-term; modest weight gain with long-term use
- **Serotonin syndrome:** Risk with MAOIs (contraindicated), triptans, tramadol, linezolid — hyperthermia, clonus, altered consciousness
- **Black box warning:** Increased suicidal ideation in children/adolescents <25 years (class effect) [^walker-2019-fluoxetine-paediatric] — monitor closely

## Evidence

| Trial / Analysis | Key Finding |
|:---|:---|
| Cipriani et al. Lancet (2018) [^cipriani-2018-antidepressants] | Comprehensive NMA of 21 antidepressants: all more effective than placebo; fluoxetine better tolerated than many older agents; sertraline ranked highest for efficacy-acceptability balance |
| TADS (Treatment for Adolescents with Depression Study) | Fluoxetine + CBT superior to either alone in adolescent MDD; fluoxetine alone also significantly better than CBT alone |
| Bulimia RCTs | Fluoxetine 60 mg OD: significant reduction in binge/purge frequency vs placebo; effect maintained 1 year |
| OCD meta-analyses | Higher doses (60–80 mg) more effective for OCD than antidepressant doses; 4–12 weeks to OCD response |
| STAR*D trial | ~30% remission with initial antidepressant (citalopram); 10–20% additional remission with switch to second agent (including SSRIs); established sequential treatment approach |

## Connections

- **Modulates** → [Serotonin](../../../../../01-human/03-molecular/serotonin/README.md): Blocks SERT to prolong synaptic 5-HT; downstream desensitization of presynaptic 5-HT1A autoreceptors over 2–4 weeks is required for full antidepressant effect.
- **Modulates** → [BDNF](../../../../../01-human/03-molecular/bdnf/README.md): Chronic SERT blockade drives BDNF upregulation in hippocampus via CREB → TrkB → neuroplasticity; this is now understood as the primary mechanism of antidepressant action rather than serotonin levels per se.
