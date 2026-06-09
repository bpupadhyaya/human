---
schema: human-scale-entry/v1
id: orexin
name: Orexin
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-08
summary: "Orexin (hypocretin-A/B) neuropeptides from lateral hypothalamic neurons maintain wakefulness by activating LC, raphe, TMN, and basal forebrain; orexin neuron loss causes narcolepsy type 1; OX1R/OX2R antagonists (suvorexant, lemborexant, daridorexant) treat insomnia."
aliases: ["orexin", "hypocretin", "OX-A", "OX-B", "orexin A", "orexin B", "HCRT", "OX1R", "OX2R", "HCRTR1", "HCRTR2", "dual orexin receptor antagonist", "DORA"]
sources:
  - id: de-lecea-1998-hypocretin-discovery
    type: peer-reviewed
    cite: "de Lecea L, Kilduff TS, Peyron C, et al. The hypocretins: hypothalamus-specific peptides with neuroexcitatory activity. Proc Natl Acad Sci USA. 1998;95(1):322-327."
    doi: "10.1073/pnas.95.1.322"
    pmid: "9419374"
    url: "https://doi.org/10.1073/pnas.95.1.322"
    accessed: "2026-06-08"
  - id: sakurai-1998-orexin-discovery
    type: peer-reviewed
    cite: "Sakurai T, Amemiya A, Ishii M, et al. Orexins and orexin receptors: a family of hypothalamic neuropeptides and G protein-coupled receptors that regulate feeding behavior. Cell. 1998;92(4):573-585."
    doi: "10.1016/S0092-8674(00)80949-6"
    pmid: "9491897"
    url: "https://doi.org/10.1016/S0092-8674(00)80949-6"
    accessed: "2026-06-08"
  - id: scammell-2015-narcolepsy-review
    type: peer-reviewed
    cite: "Scammell TE. Narcolepsy. N Engl J Med. 2015;373(27):2654-2662."
    doi: "10.1056/NEJMra1500587"
    pmid: "26716917"
    url: "https://doi.org/10.1056/NEJMra1500587"
    accessed: "2026-06-08"
cross_links:
  - target: 01-human/06-organ/brain
    relation: modulates
    note: "Orexin neurons confined to lateral hypothalamus project broadly to LC, TMN, raphe, basal forebrain, and VTA; loss of ~70,000 orexin neurons in narcolepsy type 1 is the most precisely characterized cause of a primary sleep disorder; circuit dysfunction explains EDS and cataplexy."
  - target: 01-human/03-molecular/histamine
    relation: modulates
    note: "Orexin neurons excite tuberomammillary nucleus (TMN) histamine neurons via OX2R → histamine H1 → cortical wakefulness; this OX-histamine axis sustains continuous wakefulness; reduced orexin in narcolepsy → impaired TMN drive → fragmented wakefulness and sleep attacks."
  - target: 01-human/03-molecular/norepinephrine
    relation: modulates
    note: "Orexin strongly excites LC neurons via OX2R → sustained NE release → cortical arousal and attention; LC is a primary orexin target; LC NE neurons are silenced during sleep; reduced orexin input in narcolepsy contributes to excessive daytime sleepiness and impaired alerting."
  - target: 01-human/03-molecular/serotonin
    relation: modulates
    note: "Orexin excites dorsal raphe serotonin neurons via OX2R → 5-HT → wakefulness and emotional arousal; serotonin reciprocally inhibits orexin neurons via 5-HT1A autoreceptors; sodium oxybate (GHB) in narcolepsy consolidates sleep partly via serotonergic and GABAergic mechanisms."
  - target: 01-human/03-molecular/dopamine
    relation: modulates
    note: "OX1R in VTA activates mesolimbic dopamine → NAcc DA release → reinforces wakefulness and reward-seeking; orexin drives cue-induced drug reinstatement via the OX1R-VTA-DA axis; OX1R antagonists reduce alcohol, cocaine, and opioid seeking in preclinical models."
  - target: 01-human/03-molecular/gaba
    relation: connects-to
    note: "VLPO GABAergic neurons release GABA and galanin to inhibit orexin neurons and arousal centers during NREM sleep; orexin neurons reciprocally inhibit VLPO; mutual inhibition creates a bistable flip-flop switch; DORAs block orexin input without direct GABA-A modulation."
  - target: 01-human/07-system/insomnia-disorder
    relation: connects-to
    note: "Dual OX1R/OX2R antagonists (DORAs: suvorexant 2014, lemborexant 2019, daridorexant 2022) are FDA-approved for insomnia; blocking orexin's wake-promoting drive reduces sleep onset latency and WASO without GABA-A dependency risk or rebound insomnia."
  - target: 01-human/03-molecular/adenosine
    relation: connects-to
    note: "Adenosine (process S) and orexin (arousal drive) are complementary sleep-wake regulators; basal forebrain adenosine inhibits orexin-activating circuits; caffeine blocks adenosine sleep pressure without affecting orexin tone; alignment of both is required for sleep initiation."
---

# Orexin

## Overview

**Orexin** (also named **hypocretin**) refers to two neuropeptides — **orexin A** (OX-A; hypocretin-1; 33 amino acids) and **orexin B** (OX-B; hypocretin-2; 28 amino acids) — that were simultaneously discovered in 1998 by two independent groups [^de-lecea-1998-hypocretin-discovery] [^sakurai-1998-orexin-discovery]. They are produced exclusively by ~70,000 neurons in the **lateral hypothalamic area (LHA)** and **perifornical area (PFA)** in humans, yet these neurons project extensively throughout the neuraxis to virtually every major wakefulness and reward circuit.

**Key functions:**
- Maintain **wakefulness** and prevent inappropriate sleep state transitions
- Stabilize the sleep-wake "flip-flop switch" between sleeping and waking
- Regulate **appetite and energy balance** (lateral hypothalamus = "hunger center"; orexin neurons co-express galanin, dynorphin, MCH in adjacent neurons)
- Modulate **reward, motivation, and drug-seeking** via OX1R → VTA → NAcc
- Regulate **autonomic function** (sympathetic tone, heart rate, blood pressure)
- Contribute to **stress responses** and neuroendocrine regulation

## Structure

### Peptide structure

**Orexin A (OX-A):**
- 33 amino acids; N-terminal pyroglutamate modification and C-terminal amidation for receptor binding stability
- Binds OX1R and OX2R with approximately equal affinity
- Crosses blood-brain barrier poorly from periphery; measured in CSF (narcolepsy diagnostic)

**Orexin B (OX-B):**
- 28 amino acids; C-terminally amidated
- Selective for OX2R (~10× higher affinity vs OX1R)

### Receptors

| Receptor | Gene | Coupling | Key brain regions | Role |
|:---|:---|:---|:---|:---|
| **OX1R** (Hcrt-R1) | HCRTR1 | Gq → PLC → IP3/DAG → Ca²⁺ (primarily) | LC, VTA, BLA, cortex | Arousal, reward, addiction |
| **OX2R** (Hcrt-R2) | HCRTR2 | Gq + Gi/Gs (mixed coupling) | TMN, LDT/PPT, raphe, VTA | Sleep-wake stability, histamine |

Both receptors also couple to voltage-gated Ca²⁺ channels and suppress GIRK K⁺ channels → membrane depolarization → increased neuronal firing.

### Biosynthesis and regulation

- Encoded by the **HCRT gene** (chromosome 17q21) → prepro-orexin → cleaved to OX-A and OX-B
- Orexin neuron activity: maximal during active wakefulness, reduced during quiet wake, minimal during NREM, nearly absent during REM
- Regulated by: glucose (low glucose → activates orexin neurons → feeding/wake); leptin (inhibits orexin); ghrelin (activates orexin); input from SCN (circadian gate)
- **Circadian profile:** Orexin peaks in the morning/active phase (humans: ~9-11am) and declines toward sleep onset; this daily orexin surge is the "circadian alerting signal" that opposes homeostatic sleep pressure (adenosine)

## Function

### Sleep-wake flip-flop switch

**Saper's flip-flop model** describes a mutually inhibitory circuit:

**Wake state:**
- Arousal centers (LC-NE, TMN-histamine, raphe-5HT, cholinergic basal forebrain) → active → release monoamines → inhibit VLPO
- Orexin neurons → active → reinforce ALL arousal centers → stable wakefulness

**Sleep state:**
- VLPO (GABAergic/galaninergic) → active → inhibit all arousal centers AND orexin neurons → stable sleep
- Adenosine (sleepiness signal) → activates VLPO, inhibits arousal centers

**Critical role of orexin:** Without orexin, the mutual inhibition between VLPO and arousal centers is unstable → rapid state transitions → the flip-flop switch "flickers" → narcolepsy (abrupt wake-to-REM transitions, cataplexy)

### Cataplexy and REM dissociation

In narcolepsy type 1, loss of orexin → during emotional arousal:
- REM sleep atonia circuit (GABA/glycine from sublaterodorsal nucleus → spinal motor neurons) inappropriately activates during wakefulness
- **Cataplexy:** Sudden bilateral muscle weakness or paralysis triggered by strong emotion (laughter, surprise, anger) while conscious; pathognomonic for orexin deficiency
- **Sleep paralysis and hypnagogic hallucinations:** REM sleep intrusions at wake-sleep transitions

### Reward and addiction circuits

OX1R in VTA integrates orexin input with dopamine signaling:
- Orexin from lateral hypothalamus → OX1R on VTA DA neurons → direct depolarization → increased DA firing → NAcc DA release
- Orexin also acts on OX1R on glutamatergic inputs to VTA → increased glutamate → further DA activation
- **Cue-induced reinstatement:** Orexin drives reinstatement of drug-seeking in response to drug-associated cues; OX1R antagonists reduce reinstatement of alcohol, cocaine, heroin, and methamphetamine seeking in rodent models without affecting baseline locomotion or food intake
- This suggests OX1R as a potential target for addiction treatment beyond insomnia

## Mechanism

### OX1R/OX2R signal transduction

Upon OX-A or OX-B binding, orexin receptors initiate multiple intracellular cascades:

**Primary Gq pathway (dominant in OX1R, shared in OX2R):**
1. Gq → phospholipase C (PLC) → IP₃ + DAG
2. IP₃ → ER Ca²⁺ release → elevated [Ca²⁺]ᵢ → CaMKII activation
3. DAG → PKC activation → phosphorylation of downstream effectors
4. Net effect: membrane depolarization + enhanced neurotransmitter release

**Ion channel modulation:**
- Inhibit GIRK K⁺ channels → less hyperpolarization → increased firing rate
- Activate non-selective cation channels (NSCCs) → depolarization
- Inhibit voltage-gated K⁺ channels (Kv) → prolonged action potentials
- Modulate voltage-gated Ca²⁺ channels (VGCC) in complex cell-type-dependent ways

**OX2R Gi coupling:**
OX2R has significant Gi coupling in some cell types (particularly TMN) → ↓cAMP → PKA inhibition — providing finer regulation of histaminergic tone

**Arrestin pathway and desensitization:**
- Sustained OX-R activation → GRK phosphorylation → β-arrestin recruitment → receptor internalization → reduced surface expression → tachyphylaxis with prolonged orexin exposure
- This may limit acute pharmacological effects of exogenous orexin peptides

### Pharmacological modulation

**DORA (Dual Orexin Receptor Antagonist) mechanism:**
- Competitive antagonism at both OX1R and OX2R — blocks orexin-driven excitation of all arousal centers simultaneously
- Dose-dependent: higher doses increase NREM and REM sleep; lower doses primarily reduce NREM wakefulness
- No effect on GABA-A, benzodiazepine sites, histamine receptors, or other sleep-related targets → avoids polypharmacology of older sedatives
- Unlike GABA-A PAMs: DORAs do not suppress delta (slow-wave) sleep — may actually increase N3 and REM relative to benzodiazepines

## Pathology

### Narcolepsy

**Narcolepsy Type 1 (with cataplexy):**
- Caused by autoimmune destruction of orexin neurons (HLA-DQB1*06:02 — 98% of patients; T-cell-mediated attack on orexin neurons) [^scammell-2015-narcolepsy-review]
- CSF orexin-A < 110 pg/mL (or < 1/3 of normal mean) is diagnostic (ICSD-3 criterion)
- Prevalence: ~1/2,000; onset typically adolescence
- Post-influenza vaccination narcolepsy (Pandemrix H1N1 2009-10): molecular mimicry between influenza nucleoprotein and orexin neurons; HLA-DQB1*06:02 required for susceptibility

**Narcolepsy Type 2 (without cataplexy):**
- Normal or borderline CSF orexin; mechanism less clear; may be partial orexin neuron loss or downstream circuit dysfunction

**Narcolepsy treatment:**

| Drug | Class | Mechanism | Target |
|:---|:---|:---|:---|
| Sodium oxybate (GHB) | CNS depressant | Enhances delta sleep; consolidates nighttime sleep | EDS + cataplexy |
| Pitolisant | H3 inverse agonist | Blocks presynaptic H3 autoreceptor → ↑histamine release → wakefulness | EDS + cataplexy |
| Modafinil/armodafinil | Wake-promoting | Possible weak DAT blockade, possible OX-R; unclear mechanism | EDS |
| Methylphenidate/amphetamines | Stimulants | DAT/NET block/reversal | EDS |
| Sodium oxybate + oxybate | Dual formulation | Lower Na+ load variant | EDS + cataplexy |
| Fluoxetine/venlafaxine | SSRI/SNRI | Suppress REM → reduce cataplexy (serotonergic) | Cataplexy |
| Solriamfetol | DAT/NET inhibitor | Wakefulness-promoting | EDS |

**Orexin receptor agonist (emerging):** TAK-994 (OX2R agonist) — Phase 2 narcolepsy trials (Takeda); demonstrates that restoring OX2R signaling alone can suppress narcoleptic symptoms; stopped Phase 2 due to hepatotoxicity signals; next-generation OX2R agonists in development.

### Insomnia pharmacology

Dual OX1R/OX2R antagonists (DORAs) approved for insomnia:
- **Suvorexant (Belsomra, 2014):** 10-20mg; reduces sleep onset latency (by ~10-15 min) and WASO; distinct from BZDs — does not cause rebound insomnia or dependence at approved doses
- **Lemborexant (Dayvigo, 2019):** 5-10mg; superior to zolpidem for fall prevention in elderly; faster offset than suvorexant
- **Daridorexant (Quviviq, 2022):** 25-50mg; improved daytime functioning endpoint in Phase 3; favorable for next-day alertness

## Connections

- `modulates` → **[Brain](../../06-organ/brain/README.md)** — orexin neurons in lateral hypothalamus project to LC, TMN, raphe, basal forebrain, and VTA; loss of ~70,000 orexin neurons in narcolepsy type 1 is the most precisely characterized cause of a primary sleep disorder.

- `modulates` → **[Histamine](../histamine/README.md)** — orexin neurons excite TMN histamine neurons via OX2R → histamine H1 → cortical wakefulness; the OX-histamine axis sustains continuous wakefulness; reduced orexin in narcolepsy impairs TMN drive → sleep attacks.

- `modulates` → **[Norepinephrine](../norepinephrine/README.md)** — orexin strongly excites LC neurons via OX2R → sustained NE release → cortical arousal and attention; LC is a primary orexin target; reduced orexin input in narcolepsy contributes to impaired alerting and excessive daytime sleepiness.

- `modulates` → **[Serotonin](../serotonin/README.md)** — orexin excites dorsal raphe serotonin neurons via OX2R → 5-HT → wakefulness and emotional arousal; serotonin reciprocally inhibits orexin neurons; sodium oxybate consolidates sleep in narcolepsy via complex serotonergic mechanisms.

- `modulates` → **[Dopamine](../dopamine/README.md)** — OX1R in VTA activates mesolimbic dopamine → NAcc DA release → reinforces wakefulness and reward-seeking; orexin drives cue-induced drug reinstatement via the OX1R-VTA-DA axis; OX1R antagonists reduce drug-seeking in preclinical models.

- `connects-to` → **[GABA](../gaba/README.md)** — VLPO GABAergic neurons inhibit orexin neurons during sleep; mutual inhibition between VLPO and arousal centers (including orexin) creates a bistable sleep-wake flip-flop switch; DORAs block orexin without direct GABA-A modulation — avoiding tolerance/dependence.

- `connects-to` → **[Insomnia Disorder](../../07-system/insomnia-disorder/README.md)** — DORAs (suvorexant 2014, lemborexant 2019, daridorexant 2022) block OX1R/OX2R → reduce wake-promoting drive → facilitate sleep onset and maintenance without GABA-A modulation, avoiding tolerance, rebound insomnia, and dependence seen with benzodiazepines.

- `connects-to` → **[Adenosine](../adenosine/README.md)** — adenosine (process S sleep pressure) and orexin (arousal drive) are the two complementary sleep-wake regulators; basal forebrain adenosine inhibits orexin-activating circuits; caffeine removes adenosine-mediated sleep pressure without affecting orexin tone; both systems must align for normal sleep initiation.

[^de-lecea-1998-hypocretin-discovery]: de Lecea L, Kilduff TS, Peyron C, et al. The hypocretins: hypothalamus-specific peptides with neuroexcitatory activity. *Proc Natl Acad Sci USA.* 1998;95(1):322-327. [doi:10.1073/pnas.95.1.322](https://doi.org/10.1073/pnas.95.1.322) · [PubMed 9419374](https://pubmed.ncbi.nlm.nih.gov/9419374/)
[^sakurai-1998-orexin-discovery]: Sakurai T, Amemiya A, Ishii M, et al. Orexins and orexin receptors: a family of hypothalamic neuropeptides and G protein-coupled receptors that regulate feeding behavior. *Cell.* 1998;92(4):573-585. [doi:10.1016/S0092-8674(00)80949-6](https://doi.org/10.1016/S0092-8674(00)80949-6) · [PubMed 9491897](https://pubmed.ncbi.nlm.nih.gov/9491897/)
[^scammell-2015-narcolepsy-review]: Scammell TE. Narcolepsy. *N Engl J Med.* 2015;373(27):2654-2662. [doi:10.1056/NEJMra1500587](https://doi.org/10.1056/NEJMra1500587) · [PubMed 26716917](https://pubmed.ncbi.nlm.nih.gov/26716917/)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
