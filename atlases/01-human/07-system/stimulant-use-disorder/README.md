---
schema: human-scale-entry/v1
id: stimulant-use-disorder
name: Stimulant Use Disorder
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-08
summary: "Cocaine and amphetamine misuse causing pathological dopamine surges (DAT block/reversal). VTA-NAcc remodeling via ΔFosB accumulation; D2R downregulation; hypodopaminergic withdrawal state. No FDA-approved pharmacotherapy; contingency management has strongest evidence."
aliases: ["cocaine use disorder", "cocaine addiction", "methamphetamine use disorder", "stimulant addiction", "amphetamine use disorder"]
sources:
  - id: volkow-2007-cocaine-dopamine
    type: peer-reviewed
    cite: "Volkow ND, Wang GJ, Fowler JS, Telang F. Overlapping neuronal circuits in addiction and obesity: evidence of systems pathology. Philos Trans R Soc Lond B Biol Sci. 2008;363(1507):3191-200."
    doi: "10.1098/rstb.2008.0107"
    pmid: "18640918"
  - id: robinson-berridge-2003-incentive-salience
    type: peer-reviewed
    cite: "Robinson TE, Berridge KC. Addiction. Annu Rev Psychol. 2003;54:25-53."
    doi: "10.1146/annurev.psych.54.101601.145237"
    pmid: "12185211"
  - id: pettinati-2011-contingency-management
    type: peer-reviewed
    cite: "Prendergast M, Podus D, Finney J, Greenwell L, Roll J. Contingency management for treatment of substance use disorders: a meta-analysis. Addiction. 2006;101(11):1546-60."
    doi: "10.1111/j.1360-0443.2006.01581.x"
    pmid: "17034434"
cross_links:
  - target: 01-human/03-molecular/dopamine
    relation: connects-to
    note: "Cocaine blocks DAT/NET/SERT → acute DA surge in NAcc (euphoria); amphetamines reverse DAT via TAAR1/PKC → massive cytoplasmic DA release; chronic use → D2R downregulation and ΔFosB accumulation → hypodopaminergic withdrawal state and anhedonia."
  - target: 01-human/03-molecular/norepinephrine
    relation: connects-to
    note: "Cocaine/amphetamines block or reverse NET → acute NE surge → tachycardia, hypertension, mydriasis; PFC NE elevation → arousal and attention; chronic stimulant NE dysregulation contributes to anxiety, agitation, and withdrawal dysphoria."
  - target: 01-human/03-molecular/serotonin
    relation: connects-to
    note: "Cocaine blocks SERT → ↑ synaptic 5-HT in limbic circuits; MDMA reverses SERT → massive 5-HT/DA release → empathogenic effects; chronic MDMA causes SERT downregulation and serotonergic neurotoxicity; 5-HT dysregulation modulates relapse vulnerability."
  - target: 01-human/03-molecular/bdnf
    relation: connects-to
    note: "Repeated stimulant use → ΔFosB accumulation in NAcc → altered BDNF expression; BDNF in VTA sensitizes stimulant reward; withdrawal-phase BDNF changes contribute to depression and craving; BDNF/TrkB signaling is a target in relapse prevention research."
  - target: 01-human/03-molecular/glutamate
    relation: connects-to
    note: "Chronic stimulant use disrupts glutamate homeostasis in NAcc via reduced system Xc activity; drug cues trigger PFC→NAcc glutamate surges → craving; N-acetylcysteine restores system Xc and reduces cue-induced craving; mGluR2/3 agonists are in clinical trials."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "Stimulant use disorders remodel VTA-NAcc circuits (ΔFosB, D2R loss), PFC (gray matter thinning, ↓ inhibitory control), and amygdala (cue craving); PET shows reduced DAT and D2R in striatum; meth causes DAT terminal destruction detectable on transporter imaging."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "Cocaine is directly cardiotoxic: by blocking norepinephrine reuptake and triggering α1-adrenergic coronary vasospasm it can cause myocardial infarction even in young people, plus arrhythmia and aortic dissection — cocaine chest pain is a leading drug-related ED visit."
  - target: 01-human/07-system/opioid-use-disorder
    relation: connects-to
    note: "Stimulant and opioid use disorders engage the same VTA-NAcc dopamine reward system from opposite ends, and the two increasingly overlap: 'speedball' co-use and fentanyl-adulterated cocaine/meth now drive tens of thousands of stimulant-involved overdose deaths a year."
  - target: 01-human/07-system/schizophrenia
    relation: connects-to
    note: "Heavy methamphetamine or cocaine use can produce a psychosis clinically indistinguishable from schizophrenia, reflecting shared excess striatal dopamine; the paranoid delusions and hallucinations may persist for weeks after the drug stops and are treated with antipsychotics."
  - target: 01-human/07-system/stroke
    relation: connects-to
    note: "Stimulants are a major cause of stroke in the young: cocaine and methamphetamine drive surges in blood pressure, vasospasm and vasculitis-like arteriopathy → ischemic and hemorrhagic stroke (and MI), often within hours of use; chronic meth also accelerates small-vessel disease."
  - target: 01-human/07-system/hiv-aids
    relation: connects-to
    note: "Stimulant use disorder fuels HIV transmission: methamphetamine drives high-risk sexual behavior and, when injected, needle sharing; it also worsens antiretroviral adherence and accelerates neurocognitive decline, making integrated addiction and HIV care essential."
  - target: 01-human/07-system/alcohol-use-disorder
    relation: connects-to
    note: "Stimulant and alcohol use disorders commonly co-occur, and the combination is uniquely toxic: co-use of cocaine and alcohol forms cocaethylene, a longer-acting metabolite that heightens cardiac and hepatic toxicity and sudden-death risk; alcohol is often used to 'come down'."
  - target: 01-human/07-system/cannabis-use-disorder
    relation: connects-to
    note: "Stimulant and cannabis use disorders often co-occur but differ pharmacologically: stimulants flood the synapse with dopamine for an intense high and crash, while cannabis acts on CB1 receptors with milder reward—using both compounds psychiatric and cardiovascular risk."
  - target: 01-human/07-system/bipolar-disorder
    relation: connects-to
    note: "Stimulant use disorder and bipolar disorder are tightly linked and hard to disentangle: stimulant intoxication mimics mania and withdrawal mimics depression, while bipolar patients are prone to stimulant misuse—so each can trigger or mask the other."
  - target: 01-human/04-cellular/cardiomyocyte
    relation: connects-to
    note: "Stimulants are directly cardiotoxic to cardiomyocytes: cocaine and methamphetamine drive catecholamine excess, vasospasm, and tachycardia that cause infarction, arrhythmia, and dilated cardiomyopathy—making cardiac disease a leading cause of death in stimulant users."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "Stimulant use disorder and depression are bound by the crash: dopamine depletion after a binge produces profound dysphoria, anhedonia and fatigue that mimics and can trigger major depression, so withdrawal-driven low mood fuels relapse to restore the lost reward signal."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "Stimulants are vascular poisons beyond the heart: cocaine and amphetamines cause surges in blood pressure and vasospasm that drive aortic dissection, hypertensive emergency and ischemic stroke, so the cardiovascular system bears acute catastrophic risk with every binge."
  - target: 01-human/07-system/insomnia-disorder
    relation: connects-to
    note: "Stimulants wreck sleep: by flooding dopamine and norepinephrine they suppress sleep during binges, and the rebound crash brings hypersomnia then chronic insomnia—and the sleep deprivation worsens cravings, mood and psychosis risk in stimulant use disorder."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "Stimulants directly remodel neurons: cocaine and amphetamines flood synapses with dopamine, and chronic use prunes and reshapes dendritic spines in reward circuits—structural neuroadaptations underlying the entrenched craving of stimulant use disorder."
  - target: 01-human/07-system/attention-deficit-hyperactivity-disorder
    relation: connects-to
    note: "Stimulant use disorder has a complicated tie to ADHD: prescription stimulants effectively treat ADHD and properly used rarely cause addiction, yet diversion and misuse of these same drugs is a route into stimulant use disorder—so prescribing balances benefit and risk."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "Stimulant use disorder is a chronic disorder of the nervous system's reward and control circuits: repeated dopamine surges blunt the reward system and weaken prefrontal control, so craving and relapse persist long after the drug clears—addiction as brain disease."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "Stimulant use shows on the skin: methamphetamine causes formication—the sensation of 'bugs' crawling—driving compulsive picking and sores, while injection leaves track marks and abscesses, so skin findings are visible clues to stimulant use disorder."
  - target: 01-human/06-organ/placenta
    relation: connects-to
    note: "Stimulants in pregnancy damage the placenta: cocaine and methamphetamine constrict placental vessels, raising the risk of abruption, growth restriction, and preterm birth—so stimulant use disorder in pregnancy threatens the fetus through impaired placental blood flow."
  - target: 01-human/07-system/panic-disorder
    relation: connects-to
    note: "Stimulants can manufacture panic: the surge of dopamine and noradrenaline races the heart and floods the body with fight-or-flight signals, triggering panic attacks during intoxication and withdrawal—so stimulant use both mimics and worsens panic disorder."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "Stimulants can wreck the kidneys: cocaine and methamphetamine cause vasoconstriction, severe hypertension and rhabdomyolysis, so acute kidney injury and, over time, chronic kidney disease are recognized harms of heavy stimulant use."
  - target: 01-human/04-cellular/microglia
    relation: connects-to
    note: "Methamphetamine inflames the brain via microglia: it activates microglia whose toxic mediators damage dopamine neurons, contributing to the lasting cognitive and movement problems seen after heavy use—neurotoxicity beyond addiction."
  - target: 01-human/07-system/hypertension
    relation: connects-to
    note: "Stimulants drive dangerous spikes in blood pressure: cocaine and amphetamines surge catecholamines to cause acute hypertension that triggers heart attacks, strokes and aortic dissection—the cardiovascular emergencies that make stimulant toxicity lethal."
  - target: 01-human/05-tissue/synapse
    relation: connects-to
    note: "Stimulant addiction is etched into synapses: cocaine and amphetamines flood the reward pathway with dopamine, and repeated surges strengthen and remodel synaptic connections, the lasting plasticity that drives craving and relapse."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "Stimulants attack the blood vessel lining: cocaine and amphetamines constrict and injure the endothelium and accelerate clotting and plaque, causing the vasospasm behind stimulant heart attacks and strokes even in young users."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "Smoked stimulants injure the lungs: inhaling crack cocaine or methamphetamine causes 'crack lung'—bleeding, inflammation and fluid in the air sacs—plus pulmonary hypertension, so the route of use brings its own respiratory harm."
---

# Stimulant Use Disorder

## Overview

Stimulant use disorder encompasses the pathological use of psychostimulants — primarily **cocaine** (plant-derived alkaloid from Erythroxylum coca) and **amphetamines** (synthetic amines: d-amphetamine, methamphetamine, MDMA) — characterized by compulsive drug-seeking, loss of control, and continuation despite adverse consequences. Despite shared clinical features, cocaine and amphetamine have distinct molecular mechanisms: cocaine is a **monoamine transporter reuptake inhibitor** (blocking DAT, NET, and SERT), while amphetamines are **monoamine releasers** (reversing DAT/NET via intracellular mechanisms) [^robinson-berridge-2003-incentive-salience].

Both produce pathological surges of dopamine in the nucleus accumbens that are far in excess of any natural reward — estimated at 3–5× the DA release from sex, food, or social reward in preclinical models. This supraphysiological DA flooding drives the reward learning and neural remodeling that constitutes addiction.

The public health burden is substantial: approximately **5 million Americans** had cocaine use disorder and **2.5 million** had methamphetamine use disorder in recent National Survey on Drug Use and Health estimates. The methamphetamine epidemic has intensified dramatically with illicitly manufactured supply. Despite decades of research, **no FDA-approved pharmacotherapy** exists for stimulant use disorders; **contingency management** (voucher-based behavioral reinforcement) has the strongest evidence base [^pettinati-2011-contingency-management].

## Structure

### Pharmacology: Cocaine vs. Amphetamine Mechanisms

| Feature | Cocaine | Amphetamine / Methamphetamine |
|:---|:---|:---|
| **Primary mechanism** | DAT/NET/SERT competitive reuptake inhibitor | DAT/NET reversal (efflux via TAAR1 + PKC-DAT phosphorylation) |
| **DA source** | Prevents reuptake → synaptic accumulation | Reverses DAT → cytoplasmic DA effluxed regardless of vesicle release |
| **Onset** | Rapid (IV/smoked: seconds; intranasal: minutes) | Rapid (IV/smoked: seconds; oral: 30–60 min) |
| **Duration** | Short (45–90 min; intense "high") | Long (8–12+ h for methamphetamine) |
| **NE effects** | NET block → NE surge → ↑BP, ↑HR | NET reversal → NE efflux → ↑BP, ↑HR, ↑arousal |
| **SERT effects** | SERT block → ↑ synaptic 5-HT | Moderate 5-HT reversal (less than DA/NE) |
| **Local anesthetic** | Yes (Na⁺ channel block; used in ENT surgery) | No |
| **Neurotoxicity** | Primarily vascular (stroke, vasospasm) | Direct dopaminergic/serotonergic neurotoxicity (oxidative stress) |
| **MDMA distinction** | — | MDMA: primarily SERT reversal → massive 5-HT release; also DAT reversal |

### Key Molecular Targets

**Dopamine transporter (DAT/SLC6A3):**
- Cocaine binds to the outward-facing conformation of DAT → competitive blockade → DA accumulates in synapse
- Amphetamine enters neurons via DAT → activates TAAR1 (intracellular receptor) → Gβγ → PKC → phosphorylates DAT Ser7 → DAT internalization and reversal → DA efflux independent of vesicle release
- With repeated cocaine: DAT expression initially upregulates (tolerance attempt); with meth: DAT is internalized and neurotoxic oxidative damage reduces DAT permanently

**ΔFosB accumulation:**
- Repeated stimulant administration → acute FosB (bZIP transcription factor) → truncated isoform ΔFosB accumulates (highly stable; half-life weeks)
- ΔFosB in NAcc → altered transcription: ↑CyclinD3, ↑GluR2 → sensitized reward circuit
- ΔFosB is the molecular "switch" converting recreational use into compulsive addiction; ΔFosB levels predict the degree of behavioral sensitization

## Function

### Acute Effects: Dopamine Storm

**Mesolimbic circuit:**
- Normal eating/sex: NAcc dopamine increases ~100–150% above baseline
- Cocaine (0.5 mg/kg IV): NAcc DA increases ~300–400% above baseline
- Peak plasma DA in NAcc during stimulant high is far outside the range of any natural reward — producing an artificial "superstimulus" that drives powerful associative learning

**Incentive salience hijacking (Robinson-Berridge model) [^robinson-berridge-2003-incentive-salience]:**
- Liking (hedonic pleasure): mediated by opioid/endocannabinoid systems in NAcc hot zones
- Wanting (incentive salience): mediated by mesolimbic DA
- With repeated stimulant use: sensitized DA system → ↑"wanting" (craving) even as "liking" (hedonic pleasure) decreases (hedonic tolerance)
- This dissociation explains compulsive drug-seeking despite diminishing pleasure

**Peripheral sympathomimetic effects (acute):**
- NE surge → ↑ heart rate, ↑ blood pressure, mydriasis, hyperthermia
- Cocaine additional effects: local anesthetic (membrane-stabilizing), coronary vasospasm (risk of MI even in young patients without coronary artery disease)
- Hypertensive crisis risk with MAOIs (contraindicated combination)

### Chronic Effects: Neuroplasticity and Hypodopaminergic State

With repeated use, compensatory downregulation shifts the brain toward a **hypodopaminergic state** during abstinence:

| Change | Mechanism | Consequence |
|:---|:---|:---|
| **↓ D2R in striatum** | Receptor downregulation in response to chronic DA excess | Anhedonia, inability to feel reward from natural stimuli; drives continued drug seeking |
| **↓ DAT availability** | Meth: oxidative damage to dopaminergic terminals; cocaine: compensation then depletion | Reduced capacity for normal DA cycling; persists months-years |
| **ΔFosB accumulation** | Stable truncated FosB isoform in NAcc | Sensitized response to drug and drug cues; drives craving |
| **Glutamate dysregulation** | ↓ System Xc activity in NAcc → ↓ extrasynaptic glutamate → loss of mGluR2/3 autoreceptor tone | Cue-triggered PFC→NAcc glutamate surge → craving/relapse |
| **PFC gray matter loss** | Chronic stimulant-induced inflammation, oxidative stress | ↓ Inhibitory control over drug seeking; impaired decision-making |
| **Amygdala sensitization** | Drug-cue conditioning → fear/craving overlap | Intense cue-triggered craving; high relapse risk in cue-rich environments |

### Methamphetamine Neurotoxicity

Unlike cocaine, methamphetamine causes **direct neurotoxic damage** to dopaminergic and serotonergic terminals:
- METH entry into neurons → reverses VMAT2 → DA released from vesicles into cytoplasm → oxidation → hydroxyl radical formation → protein carbonylation, lipid peroxidation
- Terminal damage: striatal DAT density reduced 50–80% in long-term users (PET imaging)
- Serotonergic terminals damaged by oxidative 5-HT metabolism (less severe than DA)
- Microglial activation in striatum and PFC → neuroinflammation → further neuronal loss
- Partial recovery of DAT with prolonged abstinence (12+ months) possible but often incomplete

## Pathology

### Clinical Presentation

**Intoxication:**
- Euphoria, increased energy, decreased appetite, hyperthermia, tachycardia, hypertension, mydriasis, insomnia
- Cocaine: intense but brief high (45–90 min); "binge" pattern driven by short duration
- Meth: prolonged (8–12 h) high; binge-crash cycles lasting days ("tweaking")
- Severe: paranoid psychosis (especially with meth — can be clinically indistinguishable from schizophrenia), hallucinations, violent behavior, hyperthermia, cardiac arrhythmia

**Cocaine cardiac complications:**
- Coronary vasospasm → MI in young adults (mechanism: α1-adrenergic + reduced endothelial NO)
- Aortic dissection (hypertensive crisis)
- QTc prolongation → ventricular arrhythmias
- Cocaine-associated chest pain is the leading cause of drug-related ED visits in adults

**Withdrawal:**
- Dysphoric "crash": profound anhedonia, fatigue, hypersomnia, depression (hours to days)
- No physical withdrawal syndrome (unlike opioids or alcohol) — psychological withdrawal
- Craving peaks at 1–3 days, subsides but persists for months; cue-triggered craving can persist years

**Stimulant-induced psychosis:**
- High-dose meth (or cocaine) → transient psychosis with auditory/visual/tactile hallucinations, paranoid delusions
- Can persist weeks after cessation in some patients
- Clinically difficult to distinguish from primary schizophrenia without history; treated with antipsychotics

### Epidemiology and Comorbidities

| Feature | Value |
|:---|:---|
| **US cocaine use disorder** | ~5 million (2022 NSDUH) |
| **US meth use disorder** | ~2.5 million |
| **HIV risk** | ↑ 3–5× (IV use + risky sexual behavior on meth) |
| **HCV risk** | ↑ (IV use) |
| **Comorbid MDD** | ~50–60% |
| **Comorbid anxiety** | ~40–50% |
| **Comorbid AUD** | ~30–40% |
| **Comorbid ASPD** | ~30% |
| **Overdose deaths** | Stimulants cause ~30,000 deaths/year in US (often combined with fentanyl) |

## Connections

- `connects-to` → **[Dopamine](../../03-molecular/dopamine/README.md)** — cocaine blocks DAT/NET/SERT → DA accumulates in NAcc synapse; amphetamines reverse DAT → massive cytoplasmic DA efflux; chronic use → D2R downregulation, ΔFosB accumulation, and hypodopaminergic withdrawal state; PET shows ↓ striatal D2R availability predicts poor treatment outcomes.
- `connects-to` → **[Norepinephrine](../../03-molecular/norepinephrine/README.md)** — stimulants block or reverse NET → acute NE surge → tachycardia, hypertension, ↑ arousal; cocaine coronary vasospasm mediated partly by α1-NE stimulation; chronic NE dysregulation contributes to anxiety, agitation, and withdrawal dysphoria in stimulant use disorder.
- `connects-to` → **[Serotonin](../../03-molecular/serotonin/README.md)** — cocaine blocks SERT → ↑ synaptic 5-HT in limbic circuits; MDMA reverses SERT → massive 5-HT release → empathogenic effects; chronic MDMA causes serotonergic neurotoxicity (SERT downregulation); serotonergic modulation influences relapse vulnerability in stimulant use disorder.
- `connects-to` → **[BDNF](../../03-molecular/bdnf/README.md)** — repeated cocaine/amphetamine drives ΔFosB accumulation in NAcc → altered BDNF/TrkB expression; BDNF in VTA sensitizes stimulant reward; withdrawal-phase BDNF changes contribute to depression and craving; BDNF dysregulation is a therapeutic target for relapse prevention.
- `connects-to` → **[Glutamate](../../03-molecular/glutamate/README.md)** — chronic stimulant use disrupts glutamate homeostasis in NAcc via reduced system Xc activity; drug cues trigger PFC→NAcc glutamate surges that drive craving; N-acetylcysteine (restores system Xc) and mGluR2/3 agonists (reduce prefrontal glutamate release) are in clinical trials for stimulant relapse prevention.
- `connects-to` → **[Brain](../../06-organ/brain/README.md)** — stimulant use disorders remodel VTA-NAcc circuits (ΔFosB, D2R loss), PFC (gray matter thinning, impaired inhibitory control), amygdala (cue-conditioned craving), and LC-NE arousal circuits; PET shows reduced DAT and D2R in striatum of chronic users; meth causes DAT terminal destruction detectable by TRODAT/FP-CIT imaging.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — Cocaine is directly cardiotoxic: by blocking norepinephrine reuptake and triggering α1-adrenergic coronary vasospasm it can cause myocardial infarction even in young people, plus arrhythmia and aortic dissection — cocaine chest pain is a leading drug-related ED visit.
- `connects-to` → **[Opioid Use Disorder](../opioid-use-disorder/README.md)** — Stimulant and opioid use disorders engage the same VTA-NAcc dopamine reward system from opposite ends, and the two increasingly overlap: 'speedball' co-use and fentanyl-adulterated cocaine/meth now drive tens of thousands of stimulant-involved overdose deaths a year.
- `connects-to` → **[Schizophrenia](../schizophrenia/README.md)** — Heavy methamphetamine or cocaine use can produce a psychosis clinically indistinguishable from schizophrenia, reflecting shared excess striatal dopamine; the paranoid delusions and hallucinations may persist for weeks after the drug stops and are treated with antipsychotics.
- `connects-to` → **[Stroke](../stroke/README.md)** — Stimulants are a major cause of stroke in the young: cocaine and methamphetamine drive surges in blood pressure, vasospasm and vasculitis-like arteriopathy → ischemic and hemorrhagic stroke (and MI), often within hours of use; chronic meth also accelerates small-vessel disease.
- `connects-to` → **[HIV/AIDS](../hiv-aids/README.md)** — Stimulant use disorder fuels HIV transmission: methamphetamine drives high-risk sexual behavior and, when injected, needle sharing; it also worsens antiretroviral adherence and accelerates neurocognitive decline, making integrated addiction and HIV care essential.
- `connects-to` → **[Alcohol Use Disorder](../alcohol-use-disorder/README.md)** — Stimulant and alcohol use disorders commonly co-occur, and the combination is uniquely toxic: co-use of cocaine and alcohol forms cocaethylene, a longer-acting metabolite that heightens cardiac and hepatic toxicity and sudden-death risk; alcohol is often used to 'come down'.
- `connects-to` → **[Cannabis Use Disorder](../cannabis-use-disorder/README.md)** — Stimulant and cannabis use disorders often co-occur but differ pharmacologically: stimulants flood the synapse with dopamine for an intense high and crash, while cannabis acts on CB1 receptors with milder reward—using both compounds psychiatric and cardiovascular risk.
- `connects-to` → **[Bipolar Disorder](../bipolar-disorder/README.md)** — Stimulant use disorder and bipolar disorder are tightly linked and hard to disentangle: stimulant intoxication mimics mania and withdrawal mimics depression, while bipolar patients are prone to stimulant misuse—so each can trigger or mask the other.
- `connects-to` → **[Cardiomyocyte](../../04-cellular/cardiomyocyte/README.md)** — Stimulants are directly cardiotoxic to cardiomyocytes: cocaine and methamphetamine drive catecholamine excess, vasospasm, and tachycardia that cause infarction, arrhythmia, and dilated cardiomyopathy—making cardiac disease a leading cause of death in stimulant users.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — Stimulant use disorder and depression are bound by the crash: dopamine depletion after a binge produces profound dysphoria, anhedonia and fatigue that mimics and can trigger major depression, so withdrawal-driven low mood fuels relapse to restore the lost reward signal.
- `connects-to` → **[Cardiovascular system](../cardiovascular-system/README.md)** — Stimulants are vascular poisons beyond the heart: cocaine and amphetamines cause surges in blood pressure and vasospasm that drive aortic dissection, hypertensive emergency and ischemic stroke, so the cardiovascular system bears acute catastrophic risk with every binge.
- `connects-to` → **[Insomnia Disorder](../insomnia-disorder/README.md)** — Stimulants wreck sleep: by flooding dopamine and norepinephrine they suppress sleep during binges, and the rebound crash brings hypersomnia then chronic insomnia—and the sleep deprivation worsens cravings, mood and psychosis risk in stimulant use disorder.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — Stimulants directly remodel neurons: cocaine and amphetamines flood synapses with dopamine, and chronic use prunes and reshapes dendritic spines in reward circuits—structural neuroadaptations underlying the entrenched craving of stimulant use disorder.
- `connects-to` → **[Attention-Deficit/Hyperactivity Disorder](../attention-deficit-hyperactivity-disorder/README.md)** — Stimulant use disorder has a complicated tie to ADHD: prescription stimulants effectively treat ADHD and properly used rarely cause addiction, yet diversion and misuse of these same drugs is a route into stimulant use disorder—so prescribing balances benefit and risk.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — Stimulant use disorder is a chronic disorder of the nervous system's reward and control circuits: repeated dopamine surges blunt the reward system and weaken prefrontal control, so craving and relapse persist long after the drug clears—addiction as brain disease.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — Stimulant use shows on the skin: methamphetamine causes formication—the sensation of 'bugs' crawling—driving compulsive picking and sores, while injection leaves track marks and abscesses, so skin findings are visible clues to stimulant use disorder.
- `connects-to` → **[Placenta](../../06-organ/placenta/README.md)** — Stimulants in pregnancy damage the placenta: cocaine and methamphetamine constrict placental vessels, raising the risk of abruption, growth restriction, and preterm birth—so stimulant use disorder in pregnancy threatens the fetus through impaired placental blood flow.
- `connects-to` → **[Panic Disorder](../panic-disorder/README.md)** — Stimulants can manufacture panic: the surge of dopamine and noradrenaline races the heart and floods the body with fight-or-flight signals, triggering panic attacks during intoxication and withdrawal—so stimulant use both mimics and worsens panic disorder.
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — Stimulants can wreck the kidneys: cocaine and methamphetamine cause vasoconstriction, severe hypertension and rhabdomyolysis, so acute kidney injury and, over time, chronic kidney disease are recognized harms of heavy stimulant use.
- `connects-to` → **[Microglia](../../04-cellular/microglia/README.md)** — Methamphetamine inflames the brain via microglia: it activates microglia whose toxic mediators damage dopamine neurons, contributing to the lasting cognitive and movement problems seen after heavy use—neurotoxicity beyond addiction.
- `connects-to` → **[Hypertension](../hypertension/README.md)** — Stimulants drive dangerous spikes in blood pressure: cocaine and amphetamines surge catecholamines to cause acute hypertension that triggers heart attacks, strokes and aortic dissection—the cardiovascular emergencies that make stimulant toxicity lethal.
- `connects-to` → **[Synapse](../../05-tissue/synapse/README.md)** — Stimulant addiction is etched into synapses: cocaine and amphetamines flood the reward pathway with dopamine, and repeated surges strengthen and remodel synaptic connections, the lasting plasticity that drives craving and relapse.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — Stimulants attack the blood vessel lining: cocaine and amphetamines constrict and injure the endothelium and accelerate clotting and plaque, causing the vasospasm behind stimulant heart attacks and strokes even in young users.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — Smoked stimulants injure the lungs: inhaling crack cocaine or methamphetamine causes 'crack lung'—bleeding, inflammation and fluid in the air sacs—plus pulmonary hypertension, so the route of use brings its own respiratory harm.

## Treatment

### Evidence-Based Interventions

**No FDA-approved pharmacotherapy exists** for cocaine or methamphetamine use disorder (2024). This is in contrast to opioid (buprenorphine, methadone, naltrexone) and alcohol (naltrexone, acamprosate, disulfiram) use disorders.

| Intervention | Evidence | Mechanism |
|:---|:---|:---|
| **Contingency management (CM)** | Strongest evidence (meta-analysis: large ES) | Voucher/prize for drug-negative urine → positive reinforcement competes with drug reward |
| **CBT for SUD** | Moderate evidence; best for relapse prevention | Identifies triggers; coping skills; craving management |
| **Motivational interviewing** | Moderate evidence; best for engagement | Ambivalence resolution; builds intrinsic motivation |
| **Bupropion** | Modest evidence for meth (not cocaine) | DAT/NET inhibitor; may partially replace meth reward and reduce craving |
| **Modafinil** | Modest evidence for cocaine (inconsistent) | Non-stimulant DA/NE modulator; reduces cocaine subjective effects |
| **N-acetylcysteine** | Emerging evidence | Restores system Xc glutamate homeostasis → reduces cue-induced craving |
| **Naltrexone** | Weak evidence for cocaine | Opioid component of cocaine reinforcement |
| **Topiramate** | Modest evidence for cocaine | GABA-A agonist/AMPA antagonist; reduces craving |
| **Disulfiram** | Some evidence for cocaine | May inhibit DA-β-hydroxylase → ↑ DA → aversive cocaine reactions |

**Contingency management (CM)** is the most evidence-based non-pharmacological intervention: drug-negative urine screens earn escalating vouchers redeemable for goods/services. Meta-analyses show the largest effect sizes of any SUD treatment for cocaine (~d = 0.58). The PACT Act (2023) removed regulatory barriers to implementing CM in federally-funded clinics in the US.

### Harm Reduction

- Fentanyl test strips: critical due to stimulant supplies contaminated with fentanyl (many meth and cocaine overdose deaths involve polysubstance involvement with fentanyl)
- Naloxone distribution for stimulant users at risk of opioid co-exposure
- HIV prevention: PrEP for meth users engaging in high-risk sexual behavior; needle programs for IV users
- Wound care (skin-popping in meth users): serious wound infections, necrotizing fasciitis
- Cardiovascular monitoring: ECG, cardiac biomarkers if chest pain

[^volkow-2007-cocaine-dopamine]: Volkow ND, Wang GJ, Fowler JS, Telang F. Overlapping neuronal circuits in addiction and obesity: evidence of systems pathology. *Philos Trans R Soc Lond B Biol Sci.* 2008;363(1507):3191-200. [doi:10.1098/rstb.2008.0107](https://doi.org/10.1098/rstb.2008.0107) · [PubMed 18640918](https://pubmed.ncbi.nlm.nih.gov/18640918/)
[^robinson-berridge-2003-incentive-salience]: Robinson TE, Berridge KC. Addiction. *Annu Rev Psychol.* 2003;54:25-53. [doi:10.1146/annurev.psych.54.101601.145237](https://doi.org/10.1146/annurev.psych.54.101601.145237) · [PubMed 12185211](https://pubmed.ncbi.nlm.nih.gov/12185211/)
[^pettinati-2011-contingency-management]: Prendergast M, Podus D, Finney J, Greenwell L, Roll J. Contingency management for treatment of substance use disorders: a meta-analysis. *Addiction.* 2006;101(11):1546-60. [doi:10.1111/j.1360-0443.2006.01581.x](https://doi.org/10.1111/j.1360-0443.2006.01581.x) · [PubMed 17034434](https://pubmed.ncbi.nlm.nih.gov/17034434/)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
