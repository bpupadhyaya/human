---
schema: human-scale-entry/v1
id: melatonin
name: Melatonin
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-08
summary: "N-acetyl-5-methoxytryptamine synthesized from serotonin in the pineal gland; the primary circadian timing hormone. Darkness → NE → AANAT activation → melatonin peak (2-4 AM); suppressed by blue light. MT1 facilitates sleep onset; MT2 phase-shifts the SCN clock."
aliases: ["melatonin", "N-acetyl-5-methoxytryptamine", "pineal hormone", "ramelteon", "tasimelteon", "agomelatine", "MT1", "MT2", "AANAT", "ASMT"]
sources:
  - id: lerner-1958-melatonin-isolation
    type: peer-reviewed
    cite: "Lerner AB, Case JD, Takahashi Y, Lee TH, Mori W. Isolation of melatonin, the pineal gland factor that lightens melanocytes. J Am Chem Soc. 1958;80(10):2587."
    doi: "10.1021/ja01543a060"
  - id: lewy-1980-light-suppresses-melatonin
    type: peer-reviewed
    cite: "Lewy AJ, Wehr TA, Goodwin FK, Newsome DA, Markey SP. Light suppresses melatonin secretion in humans. Science. 1980;210(4475):1267-1269."
    doi: "10.1126/science.7434030"
    pmid: "7434030"
    url: "https://doi.org/10.1126/science.7434030"
    accessed: "2026-06-08"
  - id: zisapel-2018-melatonin-review
    type: peer-reviewed
    cite: "Zisapel N. New perspectives on the role of melatonin in human sleep, circadian rhythms and their regulation. Br J Pharmacol. 2018;175(16):3190-3199."
    doi: "10.1111/bph.14116"
    pmid: "29318587"
    url: "https://doi.org/10.1111/bph.14116"
    accessed: "2026-06-08"
cross_links:
  - target: 01-human/03-molecular/serotonin
    relation: modulated-by
    note: "Serotonin → N-acetylserotonin (via AANAT, dark-activated by NE/β1/cAMP) → melatonin (via ASMT); pineal TPH1 synthesizes the serotonin pool; AANAT is rate-limiting; the serotonin–melatonin axis links daytime neurotransmission to circadian hormonal output."
  - target: 01-human/07-system/insomnia-disorder
    relation: connects-to
    note: "MT1 activation lowers SCN firing → sleep onset; MT2 mediates phase shifts; ramelteon (MT1/MT2 agonist, FDA 2005) treats sleep-onset insomnia with no abuse liability; melatonin (0.5–3 mg) is effective for jet lag and circadian phase shifting."
  - target: 01-human/06-organ/brain
    relation: modulates
    note: "SCN drives pineal melatonin via RHT → SCG → NE → β1 → AANAT; MT2 on SCN neurons mediates circadian phase shifts; melanopsin ipRGC blue-light input suppresses SCN-driven melatonin — the basis of light-hygiene recommendations."
  - target: 01-human/03-molecular/adenosine
    relation: connects-to
    note: "Melatonin (process C, circadian) and adenosine (process S, homeostatic) are complementary sleep signals; melatonin encodes time-of-day, adenosine encodes wakefulness duration; both reduce arousal threshold at sleep onset; caffeine blocks adenosine, not melatonin."
  - target: 01-human/03-molecular/norepinephrine
    relation: modulated-by
    note: "SCG NE activates pineal β1 → cAMP → PKA → AANAT → melatonin synthesis in darkness; light suppresses SCN→SCG NE drive → AANAT inhibition → melatonin suppression; NE is the essential dark-phase permissive signal for melatonin synthesis."
  - target: 01-human/07-system/narcolepsy
    relation: connects-to
    note: "Melatonin timing is disrupted in narcolepsy type 1 due to orexin neuron loss and sleep-wake switch instability; circadian-timed melatonin modestly improves sleep consolidation; MT1/MT2 agonists (ramelteon) are used adjunctively for circadian realignment."
---

# Melatonin

## Overview

Melatonin (*N*-acetyl-5-methoxytryptamine; MW 232.3 Da) is the primary **circadian timing hormone** in vertebrates, synthesized predominantly by the **pineal gland** in a light-suppressed, dark-activated manner [^lerner-1958-melatonin-isolation]. It was isolated in 1958 by Aaron Lerner from bovine pineal extracts. The key experimental milestone establishing its role in human circadian biology was Alfred Lewy's 1980 demonstration that **bright light suppresses nocturnal melatonin secretion** in humans — the first proof that the human circadian system is entrained by light [^lewy-1980-light-suppresses-melatonin].

Melatonin is the molecular messenger of **darkness**: its nocturnal rise (beginning ~2 hours before habitual sleep onset; peak 2–4 AM; suppressed by morning light) signals the biological night to all tissues expressing melatonin receptors — including the SCN master clock itself, the pituitary, gonads, gut, and immune system. This "darkness signal" integrates the light-dark cycle into peripheral circadian timing, making melatonin the hormonal link between the photic environment and the body's internal clock [^zisapel-2018-melatonin-review].

Beyond circadian timing, melatonin functions as a direct sleep-onset facilitator (via MT1), an immunomodulator, and a potent lipid-soluble antioxidant — scavenging hydroxyl radicals and stimulating antioxidant enzymes at concentrations achievable pharmacologically.

## Structure

### Chemical structure

| Property | Value |
|:---|:---|
| Molecular formula | C₁₃H₁₆N₂O₂ |
| Molecular weight | 232.28 Da |
| Precursor | Serotonin (5-hydroxytryptamine) |
| Biosynthetic enzymes | AANAT (rate-limiting) → ASMT/HIOMT |
| Half-life (plasma) | 30–45 minutes |
| Lipophilicity | High (log P ~1.6); crosses BBB freely |
| Peak plasma | 2–4 AM (~80–150 pg/mL); trough ~5 pg/mL |

The molecule contains an indole ring (shared with serotonin), an acetyl group (added by AANAT), and a methoxy group (added by ASMT) at position 5.

### Receptors

Melatonin acts on two high-affinity GPCRs plus a third low-affinity site:

| Receptor | Coupling | Key locations | Primary functions |
|:---|:---|:---|:---|
| **MT1** | Gi → ↓ cAMP → ↓ PKA | SCN neurons, pituitary, retina | Sleep onset (acute inhibition of SCN neural activity); reproductive suppression |
| **MT2** | Gi/Gq → ↓ cAMP, ↑ cGMP | SCN, hippocampus, retina | Circadian phase shifting; modulates retinal light adaptation |
| **MT3 / NQO2** | Enzymatic quinone reductase | Ubiquitous | Antioxidant/detoxification; melatonin binds as substrate |

## Function

### 1. Circadian phase signaling

Melatonin communicates the phase of the circadian clock to the entire organism. MT2 receptors on SCN neurons are critical for **phase-shifting the clock** [^zisapel-2018-melatonin-review]:
- **Phase advances (morning melatonin):** Exogenous melatonin in the afternoon–early evening advances the clock (shifts sleep earlier) — the basis for jet lag treatment and delayed sleep phase disorder management
- **Phase delays:** Evening bright light or melatonin taken in the morning delays the clock
- The human **dim-light melatonin onset (DLMO)** — the rise of melatonin in dim light — is the gold-standard circadian phase marker, occurring ~2 hours before habitual sleep onset

### 2. Sleep-onset facilitation

MT1 receptor activation on SCN neurons **inhibits the wake-promoting neuronal firing** of the SCN — effectively dampening the circadian arousal signal and lowering the threshold for sleep initiation. This is distinct from adenosine-mediated sleep pressure (process S) and from GABA-A sedation — melatonin does not cause sedation or impair psychomotor function at physiological doses.

**Exogenous melatonin:**
- Effective for **circadian sleep-wake phase disorders** (DSPD, jet lag, shift work) at 0.5–3 mg taken at the target bedtime
- Less effective for primary sleep-maintenance insomnia (which is not a circadian disorder)
- **Ramelteon (Rozerem, FDA 2005):** High-affinity MT1/MT2 agonist (Ki ~14 pM for MT1) with no affinity for GABA-A, histamine H1, or opioid receptors; no abuse potential; scheduled as non-controlled; approved for sleep-onset insomnia; no next-day impairment at 8 mg
- **Tasimelteon (Hetlioz, FDA 2014/2023):** MT1/MT2 agonist; approved for non-24-hour sleep-wake disorder (blind individuals without light perception) and Smith-Magenis syndrome; the only drug approved for blind patients' circadian disorder
- **Agomelatine:** MT1/MT2 agonist + 5-HT2C antagonist; European-approved antidepressant; normalizes disrupted sleep architecture in MDD; not approved in the US

### 3. Antioxidant functions

Melatonin and its metabolites (AFMK, AMK) are potent free-radical scavengers — particularly of the highly reactive hydroxyl radical (OH•) and peroxynitrite (ONOO⁻) [^zisapel-2018-melatonin-review]. Unlike enzymatic antioxidants, melatonin crosses all cellular compartments (mitochondria, nucleus) due to its lipophilicity. It also upregulates superoxide dismutase (SOD), catalase, and glutathione peroxidase. Melatonin's antioxidant role may contribute to its oncostatic, neuroprotective, and immunomodulatory properties.

### 4. Immunomodulation and oncostasis

Melatonin has complex immunomodulatory effects: it generally promotes Th1 immunity during the dark phase, acts as an anti-inflammatory at physiological concentrations, and opposes glucocorticoid-mediated immunosuppression. Epidemiological data show that night-shift workers (with chronically suppressed nocturnal melatonin) have elevated rates of breast, prostate, and colorectal cancers — the basis of WHO classification of "shift work" as a probable carcinogen.

## Mechanism

### Biosynthesis

```
L-Tryptophan
  ↓ (TPH2 + AADC)
Serotonin (5-HT)
  ↓ (AANAT — dark-activated via NE → β1 → cAMP → PKA)
N-Acetylserotonin (NAS)
  ↓ (ASMT/HIOMT)
Melatonin
```

**AANAT (arylalkylamine N-acetyltransferase)** is the rate-limiting enzyme. Its activity is 10–100× higher at night than during the day in the pineal gland. In the dark, SCN activity decreases → superior cervical ganglion (SCG) norepinephrine release increases → pineal β₁-adrenergic receptor → ↑ cAMP → PKA activates AANAT and prevents its proteasomal degradation → melatonin synthesis.

### Light suppression pathway

The **retinohypothalamic tract (RHT)** carries light information from retinal intrinsically photosensitive ganglion cells (ipRGCs, expressing melanopsin) to the SCN:
1. Light (especially blue, 450–480 nm) → ipRGC melanopsin → glutamate/PACAP → SCN activation
2. Active SCN → paraventricular nucleus → intermediolateral nucleus (IML) of spinal cord → superior cervical ganglion → **inhibits** NE release to pineal
3. Without NE, AANAT activity collapses → melatonin synthesis stops within 30–90 minutes of light exposure

This explains why **blue light from screens in the evening** suppresses melatonin and delays circadian phase — and why blue-light-blocking glasses and screen filters improve sleep onset latency in some individuals.

### Receptor signaling (MT1 vs MT2)

**MT1/Gi pathway:**
- Gαi → ↓ adenylyl cyclase → ↓ cAMP → ↓ PKA → inhibition of SCN firing → sleep facilitation
- Gβγ → GIRK channel activation → neuronal hyperpolarization
- Gβγ → PLC-β → IP3 → Ca²⁺ signaling (in some tissues)

**MT2/Gi + cGMP pathway:**
- ↓ cAMP (as MT1) + inhibition of guanylyl cyclase isoforms in some tissues
- MT2 is specifically required for circadian phase shifting — MT1-selective agonists do not phase-shift the clock
- Ramelteon and tasimelteon activate both MT1 and MT2, providing both sleep onset and phase-shifting effects

## Connections

- `modulated-by` → **[Serotonin](../serotonin/README.md)** — melatonin is synthesized from serotonin via AANAT (rate-limiting, dark-activated by NE/β1/cAMP/PKA) and ASMT; the serotonin → melatonin pathway links the indolamine neurotransmitter system to circadian hormonal output; pineal 5-HT is the substrate pool for nocturnal melatonin synthesis.

- `connects-to` → **[Insomnia Disorder](../../07-system/insomnia-disorder/README.md)** — MT1 agonism reduces SCN neuronal firing → sleep onset facilitation; ramelteon (MT1/MT2 agonist, FDA 2005) is approved for sleep-onset insomnia with no abuse potential; OTC melatonin (0.5–3 mg) is effective for circadian phase disorders (jet lag, DSPD) but modest for pure sleep-maintenance insomnia.

- `modulates` → **[Brain](../../06-organ/brain/README.md)** — the SCN (anterior hypothalamus, master circadian pacemaker) controls pineal melatonin via the retinohypothalamic tract → SCG NE → AANAT; SCN MT2 receptors mediate circadian phase shifts by melatonin; melanopsin ipRGC blue-light pathway suppresses SCG NE → AANAT inhibition, explaining light-induced melatonin suppression.

- `connects-to` → **[Adenosine](../adenosine/README.md)** — melatonin (circadian process C signal, timing) and adenosine (homeostatic process S, accumulated wakefulness) are complementary sleep-onset drivers; melatonin signals "it is biologically night" while adenosine signals "you have been awake long enough"; caffeine blocks adenosine without affecting melatonin; both converge at sleep onset.

- `modulated-by` → **[Norepinephrine](../norepinephrine/README.md)** — NE from superior cervical ganglion (SCN-driven) activates pineal β1-adrenergic receptors → cAMP → PKA → AANAT → nocturnal melatonin synthesis; light suppresses SCN→SCG NE drive → AANAT collapse → melatonin suppression; NE is the essential permissive dark-phase signal for melatonin production.

- `connects-to` → **[Narcolepsy](../../07-system/narcolepsy/README.md)** — melatonin secretion timing and amplitude are disrupted in narcolepsy type 1 due to orexin neuron loss and sleep-wake switch instability; melatonin supplements at the appropriate circadian phase modestly improve sleep consolidation; MT1/MT2 agonists (ramelteon) are occasionally used adjunctively for circadian realignment in narcolepsy.

## Pathology

| Condition | Melatonin role | Clinical implication |
|:---|:---|:---|
| **Delayed sleep phase disorder (DSPD)** | Intrinsically late DLMO; melatonin peaks 3–6 h after normal | Low-dose melatonin (0.5 mg) taken 5–7 h before current sleep onset; combined with morning bright light therapy |
| **Jet lag** | Rapid trans-meridian travel → misaligned melatonin phase | Exogenous melatonin (0.5–5 mg) at destination bedtime for 3–5 days; eastward jet lag requires phase advance |
| **Shift work disorder** | Nocturnal light exposure → melatonin suppression → disrupted sleep | Blackout curtains, blue-light glasses on commute home; melatonin before daytime sleep |
| **Non-24-hour sleep-wake disorder** | Blind individuals lack light entrainment → free-running period 24.1–24.5 h | Tasimelteon (FDA 2014) entrains free-running rhythm in totally blind; most effective treatment available |
| **Smith-Magenis syndrome** | RAI1 haploinsufficiency → inverted melatonin rhythm (high day, low night) | Tasimelteon (FDA 2023) — the first non-orphan drug for SMS; corrects the paradoxical daytime melatonin elevation |
| **Aging** | Progressive decline in pineal AANAT activity → ↓ nocturnal melatonin amplitude → sleep fragmentation | Melatonin replacement (Circadin 2mg prolonged-release) licensed in EU for ≥55 years insomnia |
| **Cancer / shift work** | WHO Group 2A carcinogen (shift work involving circadian disruption); melatonin suppression → ↓ oncostatic signaling | Melatonin's anti-tumor role is under clinical investigation (adjunct to chemotherapy); avoid night-shift work when possible |

[^lerner-1958-melatonin-isolation]: Lerner AB, Case JD, Takahashi Y, Lee TH, Mori W. Isolation of melatonin, the pineal gland factor that lightens melanocytes. *J Am Chem Soc.* 1958;80(10):2587. [doi:10.1021/ja01543a060](https://doi.org/10.1021/ja01543a060)
[^lewy-1980-light-suppresses-melatonin]: Lewy AJ, Wehr TA, Goodwin FK, Newsome DA, Markey SP. Light suppresses melatonin secretion in humans. *Science.* 1980;210(4475):1267-1269. [doi:10.1126/science.7434030](https://doi.org/10.1126/science.7434030) · [PubMed 7434030](https://pubmed.ncbi.nlm.nih.gov/7434030/)
[^zisapel-2018-melatonin-review]: Zisapel N. New perspectives on the role of melatonin in human sleep, circadian rhythms and their regulation. *Br J Pharmacol.* 2018;175(16):3190-3199. [doi:10.1111/bph.14116](https://doi.org/10.1111/bph.14116) · [PubMed 29318587](https://pubmed.ncbi.nlm.nih.gov/29318587/)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
