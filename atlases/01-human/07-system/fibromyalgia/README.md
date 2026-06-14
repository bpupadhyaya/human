---
schema: human-scale-entry/v1
id: fibromyalgia
name: Fibromyalgia
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-08
summary: "Fibromyalgia (2-3% prevalence, F:M 3:1) is a central sensitization disorder: SP-NMDA wind-up, descending serotonin/NE inhibition failure, reduced NAcc dopamine. Duloxetine, milnacipran (SNRIs), and pregabalin are FDA-approved; exercise and CBT are first-line."
aliases: ["fibromyalgia", "FM", "fibromyalgia syndrome", "FMS", "central sensitization", "chronic widespread pain", "fibro fog", "wind-up pain"]
cross_links:
  - target: 01-human/03-molecular/glutamate
    relation: connects-to
    note: "Spinal NMDA receptor hyperactivation by repetitive C-fiber input + SP → wind-up and central sensitization; elevated glutamate in posterior insula on MRS correlates with FM severity; ketamine (NMDA antagonist) reduces FM pain in small controlled trials."
  - target: 01-human/03-molecular/serotonin
    relation: connects-to
    note: "Descending serotonergic inhibition from raphe to dorsal horn is impaired in FM (low CSF 5-HIAA); duloxetine and amitriptyline restore descending inhibition; 5-HT3 antagonist tropisetron reduces FM pain in small RCTs; 5-HT2A polymorphisms associate with FM risk."
  - target: 01-human/03-molecular/norepinephrine
    relation: connects-to
    note: "Descending NE inhibition from LC to dorsal horn is deficient in FM; duloxetine and milnacipran (FDA-approved SNRIs) increase NE in descending pain pathways — the core analgesic mechanism; NE deficiency amplifies SP and glutamate-driven central sensitization."
  - target: 01-human/03-molecular/dopamine
    relation: connects-to
    note: "FM shows reduced NAcc dopamine release (↓ [¹¹C]raclopride binding PET — Harris 2007); blunted NAcc DA → reduced endogenous analgesia (dopamine activates descending antinociception); low-dose naltrexone may act partly via dopaminergic disinhibition of opioid circuits."
  - target: 01-human/03-molecular/substance-p
    relation: connects-to
    note: "CSF substance P is elevated ~3-fold in FM — one of the most reproducible biomarkers; elevated SP → NK1R sensitization → dorsal horn wind-up → diffuse hyperalgesia and allodynia; FM patients have consistently lower pain thresholds consistent with SP-driven central sensitization."
  - target: 01-human/06-organ/brain
    relation: targets
    note: "FM involves thalamic hypersensitivity, ACC and insula hyperactivation to pain stimuli (fMRI), and altered DMN connectivity; MRS shows elevated glutamate in posterior insula; gray matter density reductions correlate with pain chronicity; changes partially reverse with treatment."
  - target: 01-human/03-molecular/cgrp
    relation: connects-to
    note: "CGRP is elevated in plasma and CSF in fibromyalgia; CGRP-mediated peripheral C-fiber sensitization contributes to FM's diffuse hyperalgesia and allodynia; anti-CGRP mAbs are under investigation for FM; CGRP and substance P are co-released from FM peripheral nociceptors."
  - target: 01-human/07-system/neuropathic-pain
    relation: connects-to
    note: "FM and neuropathic pain share central sensitization (NMDA wind-up, descending inhibition failure) but differ: neuropathic pain requires nerve injury while FM is nociplastic; both respond to SNRIs and α2δ ligands; small fiber neuropathy co-occurs in ~40% of FM patients."
  - target: 01-human/07-system/migraine
    relation: connects-to
    note: "Fibromyalgia and migraine frequently co-occur and share central sensitization and CGRP biology: both feature amplified pain processing and descending-inhibition failure, anti-CGRP antibodies developed for migraine are under study in FM, and SNRIs and exercise help both."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "Depression coexists with fibromyalgia in ~40-60%: they share serotonin-norepinephrine dysregulation and HPA-axis changes, the SNRIs duloxetine and milnacipran treat both, and depression worsens FM pain and disability—though FM pain is not merely somatized depression."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "Anxiety disorders are highly comorbid with fibromyalgia: shared monoaminergic dysregulation and stress-axis dysfunction link them, anxiety amplifies pain perception and sleep disruption in a vicious cycle, and combined CBT plus SNRI treatment targets both pain and affective load."
  - target: 01-human/07-system/ptsd
    relation: connects-to
    note: "Fibromyalgia and PTSD overlap through central sensitization and stress: trauma and HPA-axis dysregulation prime the nervous system to amplify pain, PTSD is a common antecedent and comorbidity of fibromyalgia, and both respond to approaches targeting the stress-pain loop."
  - target: 01-human/07-system/rheumatoid-arthritis
    relation: connects-to
    note: "Fibromyalgia frequently coexists with rheumatoid arthritis as secondary fibromyalgia: central pain sensitization adds widespread non-inflammatory pain atop joint disease, so inflated disease-activity scores mislead—distinguishing them avoids overtreating RA."
  - target: 01-human/07-system/sjogrens-syndrome
    relation: connects-to
    note: "Fibromyalgia is common in Sjögren's and other autoimmune diseases: chronic illness and dysautonomia drive central sensitization, so widespread pain and fatigue in Sjögren's often reflect comorbid fibromyalgia rather than active glandular inflammation."
  - target: 01-human/07-system/gut-microbiome
    relation: connects-to
    note: "Fibromyalgia is increasingly tied to the gut-brain axis: patients show an altered gut microbiome, and microbial metabolites may influence pain signaling and central sensitization—part of why it overlaps with IBS and why diet and microbiome are studied as modifiers."
  - target: 01-human/07-system/systemic-lupus-erythematosus
    relation: connects-to
    note: "Fibromyalgia is a major confounder in lupus: up to a third of SLE patients develop comorbid fibromyalgia, inflating disease-activity scores—so separating central-sensitization pain from true lupus inflammation guides whether to escalate immunotherapy or treat pain."
  - target: 01-human/05-tissue/hippocampus
    relation: connects-to
    note: "Fibromyalgia involves the hippocampus and central pain processing: imaging shows hippocampal changes alongside augmented pain perception (central sensitization) and 'fibro-fog'—evidence that fibromyalgia is a disorder of brain pain processing, not peripheral tissue."
  - target: 01-human/07-system/insomnia-disorder
    relation: connects-to
    note: "Nonrestorative sleep is core to fibromyalgia, not incidental: disrupted deep sleep lowers pain thresholds and worsens fatigue and cognition, and the disorder and insomnia reinforce each other—so sleep-targeted treatment is central to managing fibromyalgia."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "Fibromyalgia is a disorder of pain-processing neurons (central sensitization): amplified spinal and brain pain signaling makes normal stimuli hurt, so it is a problem of how the nervous system processes pain, not tissue damage—explaining why analgesics often fail."
  - target: 01-human/03-molecular/cortisol
    relation: connects-to
    note: "HPA-axis and cortisol dysregulation feature in fibromyalgia: blunted stress-hormone responses accompany the disorder, linking chronic stress and poor sleep to amplified pain—so fibromyalgia sits at the interface of the stress system and pain processing."
  - target: 01-human/04-cellular/microglia
    relation: connects-to
    note: "Fibromyalgia may be sustained by activated microglia: these immune cells of the cord and brain release pain-amplifying cytokines, supporting the idea that central sensitization—a volume knob turned up on pain—has a neuroinflammatory basis."
  - target: 01-human/03-molecular/gaba
    relation: connects-to
    note: "Fibromyalgia shows weakened pain braking: reduced GABA, the main inhibitory transmitter, leaves descending pain control too weak to dampen signals—part of why gabapentinoids like pregabalin, which boost inhibitory tone, are among its few effective drugs."
  - target: 01-human/05-tissue/peripheral-nerve
    relation: connects-to
    note: "Fibromyalgia is not purely central: about half of patients have small-fiber neuropathy, with reduced nerve-fiber density in skin biopsies—so damaged peripheral nerves may feed the amplified pain, blurring the line between central and peripheral pain disorders."
sources:
  - id: wolfe-2016-fibromyalgia-criteria
    type: peer-reviewed
    cite: "Wolfe F, Clauw DJ, Fitzcharles MA, et al. 2016 Revisions to the 2010/2011 fibromyalgia diagnostic criteria. Semin Arthritis Rheum. 2016;46(3):319-329."
    doi: "10.1016/j.semarthrit.2016.08.012"
    pmid: "27916278"
    url: "https://doi.org/10.1016/j.semarthrit.2016.08.012"
  - id: clauw-2014-fibromyalgia-review
    type: peer-reviewed
    cite: "Clauw DJ. Fibromyalgia: a clinical review. JAMA. 2014;311(15):1547-1555."
    doi: "10.1001/jama.2014.3266"
    pmid: "24737367"
    url: "https://doi.org/10.1001/jama.2014.3266"
  - id: harris-2007-fibromyalgia-dopamine
    type: peer-reviewed
    cite: "Harris RE, Clauw DJ, Scott DJ, et al. Decreased central mu-opioid receptor availability in fibromyalgia. J Neurosci. 2007;27(37):10000-10006."
    doi: "10.1523/JNEUROSCI.2849-07.2007"
    pmid: "17855614"
    url: "https://doi.org/10.1523/JNEUROSCI.2849-07.2007"
---

# Fibromyalgia

## Overview

**Fibromyalgia (FM)** is a chronic syndrome of widespread musculoskeletal pain, fatigue, cognitive impairment ("fibro fog"), and sleep disturbance, resulting from **central pain amplification** rather than peripheral tissue damage. FM was reconceptualized in the 2000s–2010s from a rheumatic/musculoskeletal diagnosis to a **central sensitization syndrome** — a disorder of pain processing in the brain and spinal cord, not a primary inflammatory or structural condition [^clauw-2014-fibromyalgia-review].

**Epidemiology:**
- Prevalence: 2–3% globally; ~10 million Americans
- Female:male ratio ~3:1; peak onset ages 30–50
- Strong comorbidity with other central sensitization syndromes: IBS (30–70%), migraine (32%), interstitial cystitis, temporomandibular disorder
- High psychiatric comorbidity: depression (40%), anxiety (30%), PTSD (45% in FM patients from trauma backgrounds)
- High economic burden: annual direct costs ~$4,000–$8,000/patient; major cause of disability claims

**Why it matters:** FM is the **prototypical central sensitization disorder** — it established that chronic pain can be maintained entirely by central neuroplastic changes (amplified spinal and cortical pain processing) in the absence of ongoing tissue pathology. This paradigm has reshaped pain medicine and validated nociplastic pain as a distinct mechanistic category alongside nociceptive and neuropathic pain.

**2021 classification:** The International Association for the Study of Pain (IASP) coined the term **nociplastic pain** — pain arising from altered nociception without clear evidence of tissue damage or nerve injury — specifically to capture FM, IBS, and related syndromes.

## Structure

### Diagnostic criteria (ACR 2016 / Wolfe et al.)

FM diagnosis requires ALL three: [^wolfe-2016-fibromyalgia-criteria]

1. **Widespread Pain Index (WPI) ≥ 7** AND **Symptom Severity Scale (SSS) ≥ 5**
   OR **WPI 4–6** AND **SSS ≥ 9**

2. Symptoms present at **similar level for ≥ 3 months**

3. FM diagnosis is appropriate **regardless of other diagnoses** (fibromyalgia does not exclude other painful conditions)

**WPI regions (0–19):** Jaw, chest, abdomen, upper/lower back, neck + bilateral: shoulder girdle, upper arm, lower arm, hip/buttock, upper leg, lower leg (count each region where pain was present in past week)

**SSS (0–12):** Scores for sleep problems, fatigue, cognitive problems (0-3 each) + somatic symptoms presence (0-3 global)

**Subgroups:**
| Subgroup | Profile | Treatment implications |
|:---|:---|:---|
| **Central sensitization primary** | No peripheral trigger; bilateral; high SSS | SNRI + pregabalin + CBT; avoid opioids |
| **Post-trauma/post-infectious** | Onset after injury, surgery, viral illness | Address underlying trigger; trauma-informed care |
| **Comorbid rheumatic** | Concurrent RA, lupus, OA | Treat both; address central component separately |
| **Psychiatric comorbid** | High depression/anxiety/PTSD | Integrated psychiatric + pain management |

### Assessment tools

| Tool | Purpose |
|:---|:---|
| **FIQ-R (Fibromyalgia Impact Questionnaire — Revised)** | 21-item; functional impairment, symptom severity |
| **FKBQ (FM Keele STarT tool)** | Risk stratification for outcome |
| **BPI (Brief Pain Inventory)** | Pain severity and interference |
| **PCS (Pain Catastrophizing Scale)** | Predicts treatment response; catastrophizing = poor outcome |
| **PSQI / ESS** | Sleep quality and daytime sleepiness |

## Function

### Central sensitization mechanisms

**Spinal wind-up (SP-NMDA synergy):**
- Repetitive C-fiber input → sustained SP release at dorsal horn → NK1R activation → membrane depolarization → removes Mg²⁺ block from NMDA receptors
- SP (NK1R) + glutamate (NMDA) → synergistic Ca²⁺ influx → PKC-ε activation → phosphorylation of NR2B → reduced NMDA activation threshold
- Result: spinal cord amplifies innocuous stimuli as painful (allodynia) and amplifies painful stimuli excessively (hyperalgesia)

**Descending pain inhibition failure:**
- Normally, brainstem RVM and PAG project serotonergic and noradrenergic fibers to spinal dorsal horn → suppress pain signals
- In FM: reduced descending 5-HT and NE inhibitory tone → unopposed SP/glutamate-driven amplification
- CSF 5-HIAA (5-HT metabolite) is reduced in FM; CSF MHPG (NE metabolite) reduced in some studies
- Duloxetine and milnacipran restore descending inhibition by increasing 5-HT and NE availability

**Dopamine and endogenous analgesia:**
- Nucleus accumbens (NAcc) dopamine normally activates the mesolimbic descending antinociception system — DA D2R agonism reduces pain
- PET studies (Harris 2007) [^harris-2007-fibromyalgia-dopamine] show reduced NAcc mu-opioid receptor availability AND reduced dopamine function in FM
- Blunted NAcc DA → impaired endogenous opioid/dopamine analgesia → pain persists without pharmacological support

### Brain imaging findings in FM

| Finding | Method | Significance |
|:---|:---|:---|
| ↑ Posterior insula glutamate | MRS | Correlates with pain severity |
| ↑ ACC, insula activation to pain | fMRI | Disproportionate cortical response to low stimuli |
| ↑ Thalamic excitability | PET/fMRI | Reduced thalamic gating of pain |
| ↓ Endogenous opioid receptor availability | PET ([¹¹C]carfentanil) | Tonically occupied by endogenous opioids in pain state |
| Gray matter ↓ in dlPFC, ACC | VBM MRI | Correlates with pain chronicity; partially reversible |
| Altered default mode network | Resting-state fMRI | Predicts treatment response to CBT |

## Pathology

### Pathophysiology summary

FM is not a single-etiology disorder but a convergent syndrome resulting from the intersection of:
1. **Genetic predisposition:** 5-HT2A promoter variants, COMT Val158Met (catecholamine metabolism), TRPV3 variants
2. **Triggering events:** Physical trauma, surgery, viral illness, psychosocial stress (PTSD, adverse childhood experiences)
3. **Neuroplastic amplification:** SP-NMDA wind-up → dorsal horn sensitization → cortical reorganization
4. **Sleep disruption:** Non-restorative sleep → reduced central pain inhibition (α-EEG anomaly — intrusion of alpha waves into delta sleep) → bidirectional worsening

### Medical and psychiatric comorbidities

| Comorbidity | Prevalence in FM | Shared mechanism |
|:---|:---|:---|
| IBS / functional dyspepsia | 30–70% | Central sensitization (shared spinal pathways) |
| Migraine | 32% | Trigeminal sensitization, shared SP/CGRP |
| PTSD | 45% (trauma-onset FM) | CRH-driven HPA dysregulation, central sensitization |
| Major depressive disorder | 30–40% | Shared serotonin/NE/dopamine hypofunction |
| Generalized anxiety disorder | 25–35% | Shared HPA axis dysregulation |
| Non-restorative sleep / sleep apnea | >70% | Sleep disruption amplifies central sensitization |

### Treatment

**FDA-approved pharmacotherapy:**

| Drug | Mechanism | Evidence |
|:---|:---|:---|
| **Duloxetine (Cymbalta)** | SNRI; ↑ NE/5-HT in descending pain pathways | FDA 2008; 30–60% pain reduction vs 20% placebo; NNT ~8-10 |
| **Milnacipran (Savella)** | SNRI (NE > 5-HT); unique for FM-first FDA approval | FDA 2009; comparable efficacy to duloxetine |
| **Pregabalin (Lyrica)** | α2δ VGCC subunit ligand; reduces SP/glutamate release | FDA 2007; reduces pain and improves sleep; NNT ~10-12 |

**Other evidence-based options (off-label):**
- **Amitriptyline (10–50 mg):** Low-dose TCA; 5-HT/NE + H1 + anticholinergic → pain + sleep; NNT ~4-5 (strong evidence)
- **Cyclobenzaprine:** Tricyclic muscle relaxant; reduces alpha-EEG sleep anomaly; small but consistent effect
- **Gabapentin:** α2δ ligand (like pregabalin); often used off-label; comparable to pregabalin
- **Low-dose naltrexone (LDN, 1.5–4.5 mg):** Blocks microglial Toll-like receptor 4; anti-neuroinflammatory; 3 small RCTs positive for pain reduction — promising but not yet replicated in large trials
- **Tramadol:** Weak opioid + NE/5-HT reuptake; some FM evidence but opioid concerns
- **Opioids (standard):** NOT recommended — no RCT evidence in FM; may worsen central sensitization via opioid-induced hyperalgesia

**Non-pharmacological (first-line alongside or instead of drugs):**
- **Aerobic exercise:** Best long-term intervention; reduces central sensitization; improves sleep, mood, and pain; dose-dependent effect; water aerobics well-tolerated for severe cases
- **CBT:** Reduces pain catastrophizing; addresses fear-avoidance; improves function; NNT comparable to pharmacotherapy
- **Multidisciplinary pain rehabilitation:** Integrates CBT, physiotherapy, occupational therapy — most effective for severe FM
- **Sleep hygiene / CBT-I:** Treating non-restorative sleep directly reduces FM pain

## Connections

- `connects-to` → **[Glutamate](../../../03-molecular/glutamate/README.md)** — spinal NMDA receptor hyperactivation by repetitive C-fiber nociceptive input + substance P → wind-up and central sensitization; elevated glutamate in posterior insula measurable by MRS correlates with FM symptom severity; NMDA antagonists (ketamine) reduce FM pain in controlled trials.

- `connects-to` → **[Serotonin](../../../03-molecular/serotonin/README.md)** — descending serotonergic inhibition from raphe nuclei to spinal dorsal horn is impaired in FM (reduced CSF 5-HIAA); duloxetine (SNRI) and amitriptyline (TCA) restore descending inhibition; 5-HT3 antagonist tropisetron reduces FM pain in small RCTs; 5-HT2A receptor polymorphisms are associated with FM susceptibility.

- `connects-to` → **[Norepinephrine](../../../03-molecular/norepinephrine/README.md)** — descending NE inhibitory pathways from LC to spinal dorsal horn are deficient in FM; duloxetine and milnacipran (both FDA-approved for FM) increase NE in descending pain pathways — the primary analgesic mechanism; NE deficiency in descending pathways amplifies SP-NMDA-driven central sensitization.

- `connects-to` → **[Dopamine](../../../03-molecular/dopamine/README.md)** — FM shows reduced NAcc dopamine release detected by PET; blunted NAcc DA → impaired endogenous mesolimbic analgesia (dopamine activates descending antinociceptive circuits); dopaminergic dysfunction may explain why reward and motivation are impaired in FM and why cognitive deficits (fibro fog) are prominent.

- `connects-to` → **[Substance P](../../../03-molecular/substance-p/README.md)** — CSF substance P is elevated ~3-fold in FM patients vs healthy controls — the most consistently replicated biological finding in FM; elevated SP drives NK1R sensitization at the dorsal horn → wind-up → diffuse hyperalgesia and allodynia; SP-NMDA synergy is the mechanistic core of FM's central pain amplification.

- `targets` → **[Brain](../../../06-organ/brain/README.md)** — FM involves thalamic hypersensitivity, ACC and posterior insula hyperactivation to pain stimuli (fMRI), and altered default mode network connectivity; MRS shows elevated glutamate in posterior insula correlating with pain severity; gray matter density reductions in dlPFC and ACC correlate with chronicity and partially reverse with effective treatment.

- `connects-to` → **[CGRP](../../../03-molecular/cgrp/README.md)** — CGRP is elevated in plasma and CSF in FM patients; CGRP-mediated peripheral C-fiber sensitization contributes to FM's widespread hyperalgesia and allodynia; anti-CGRP monoclonal antibodies (developed for migraine) are under investigation as potential FM treatments; CGRP and substance P are co-released from peripheral nociceptors and synergistically drive neurogenic inflammation.
- `connects-to` → **[Neuropathic Pain](../neuropathic-pain/README.md)** — FM and neuropathic pain share central sensitization mechanisms (NMDA wind-up, loss of descending inhibitory control) but differ mechanistically: neuropathic pain requires a demonstrable nerve lesion while FM is nociplastic (amplified without peripheral pathology); both respond to SNRIs (duloxetine, milnacipran) and α2δ ligands (pregabalin, gabapentin); small fiber neuropathy (SFN) co-occurs in approximately 40% of FM patients on skin biopsy.
- `connects-to` → **[Migraine](../migraine/README.md)** — Fibromyalgia and migraine frequently co-occur and share central sensitization and CGRP biology: both feature amplified pain processing and descending-inhibition failure, anti-CGRP antibodies developed for migraine are under study in FM, and SNRIs and exercise help both.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — Depression coexists with fibromyalgia in ~40-60%: they share serotonin-norepinephrine dysregulation and HPA-axis changes, the SNRIs duloxetine and milnacipran treat both, and depression worsens FM pain and disability—though FM pain is not merely somatized depression.
- `connects-to` → **[Generalized Anxiety Disorder](../generalized-anxiety-disorder/README.md)** — Anxiety disorders are highly comorbid with fibromyalgia: shared monoaminergic dysregulation and stress-axis dysfunction link them, anxiety amplifies pain perception and sleep disruption in a vicious cycle, and combined CBT plus SNRI treatment targets both pain and affective load.
- `connects-to` → **[PTSD](../ptsd/README.md)** — Fibromyalgia and PTSD overlap through central sensitization and stress: trauma and HPA-axis dysregulation prime the nervous system to amplify pain, PTSD is a common antecedent and comorbidity of fibromyalgia, and both respond to approaches targeting the stress-pain loop.
- `connects-to` → **[Rheumatoid Arthritis](../rheumatoid-arthritis/README.md)** — Fibromyalgia frequently coexists with rheumatoid arthritis as secondary fibromyalgia: central pain sensitization adds widespread non-inflammatory pain atop joint disease, so inflated disease-activity scores mislead—distinguishing them avoids overtreating RA.
- `connects-to` → **[Sjögren's Syndrome](../sjogrens-syndrome/README.md)** — Fibromyalgia is common in Sjögren's and other autoimmune diseases: chronic illness and dysautonomia drive central sensitization, so widespread pain and fatigue in Sjögren's often reflect comorbid fibromyalgia rather than active glandular inflammation.
- `connects-to` → **[Gut Microbiome](../gut-microbiome/README.md)** — Fibromyalgia is increasingly tied to the gut-brain axis: patients show an altered gut microbiome, and microbial metabolites may influence pain signaling and central sensitization—part of why it overlaps with IBS and why diet and microbiome are studied as modifiers.
- `connects-to` → **[Systemic Lupus Erythematosus](../systemic-lupus-erythematosus/README.md)** — Fibromyalgia is a major confounder in lupus: up to a third of SLE patients develop comorbid fibromyalgia, inflating disease-activity scores—so separating central-sensitization pain from true lupus inflammation guides whether to escalate immunotherapy or treat pain.
- `connects-to` → **[Hippocampus](../../05-tissue/hippocampus/README.md)** — Fibromyalgia involves the hippocampus and central pain processing: imaging shows hippocampal changes alongside augmented pain perception (central sensitization) and 'fibro-fog'—evidence that fibromyalgia is a disorder of brain pain processing, not peripheral tissue.
- `connects-to` → **[Insomnia Disorder](../insomnia-disorder/README.md)** — Nonrestorative sleep is core to fibromyalgia, not incidental: disrupted deep sleep lowers pain thresholds and worsens fatigue and cognition, and the disorder and insomnia reinforce each other—so sleep-targeted treatment is central to managing fibromyalgia.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — Fibromyalgia is a disorder of pain-processing neurons (central sensitization): amplified spinal and brain pain signaling makes normal stimuli hurt, so it is a problem of how the nervous system processes pain, not tissue damage—explaining why analgesics often fail.
- `connects-to` → **[Cortisol](../../03-molecular/cortisol/README.md)** — HPA-axis and cortisol dysregulation feature in fibromyalgia: blunted stress-hormone responses accompany the disorder, linking chronic stress and poor sleep to amplified pain—so fibromyalgia sits at the interface of the stress system and pain processing.
- `connects-to` → **[Microglia](../../04-cellular/microglia/README.md)** — Fibromyalgia may be sustained by activated microglia: these immune cells of the cord and brain release pain-amplifying cytokines, supporting the idea that central sensitization—a volume knob turned up on pain—has a neuroinflammatory basis.
- `connects-to` → **[GABA](../../03-molecular/gaba/README.md)** — Fibromyalgia shows weakened pain braking: reduced GABA, the main inhibitory transmitter, leaves descending pain control too weak to dampen signals—part of why gabapentinoids like pregabalin, which boost inhibitory tone, are among its few effective drugs.
- `connects-to` → **[Peripheral Nerve](../../05-tissue/peripheral-nerve/README.md)** — Fibromyalgia is not purely central: about half of patients have small-fiber neuropathy, with reduced nerve-fiber density in skin biopsies—so damaged peripheral nerves may feed the amplified pain, blurring the line between central and peripheral pain disorders.

[^wolfe-2016-fibromyalgia-criteria]: Wolfe F, Clauw DJ, Fitzcharles MA, et al. 2016 Revisions to the 2010/2011 fibromyalgia diagnostic criteria. *Semin Arthritis Rheum.* 2016;46(3):319-329. [doi:10.1016/j.semarthrit.2016.08.012](https://doi.org/10.1016/j.semarthrit.2016.08.012) · [PubMed 27916278](https://pubmed.ncbi.nlm.nih.gov/27916278/)
[^clauw-2014-fibromyalgia-review]: Clauw DJ. Fibromyalgia: a clinical review. *JAMA.* 2014;311(15):1547-1555. [doi:10.1001/jama.2014.3266](https://doi.org/10.1001/jama.2014.3266) · [PubMed 24737367](https://pubmed.ncbi.nlm.nih.gov/24737367/)
[^harris-2007-fibromyalgia-dopamine]: Harris RE, Clauw DJ, Scott DJ, et al. Decreased central mu-opioid receptor availability in fibromyalgia. *J Neurosci.* 2007;27(37):10000-10006. [doi:10.1523/JNEUROSCI.2849-07.2007](https://doi.org/10.1523/JNEUROSCI.2849-07.2007) · [PubMed 17855614](https://pubmed.ncbi.nlm.nih.gov/17855614/)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
