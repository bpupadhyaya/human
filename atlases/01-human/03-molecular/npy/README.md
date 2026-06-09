---
schema: human-scale-entry/v1
id: npy
name: Neuropeptide Y
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-08
summary: "Neuropeptide Y (NPY); 36-aa pancreatic polypeptide family member; most abundant neuropeptide in the CNS. Orexigenic via Y1R/Y5R on PVN; anxiolytic via Y1R on amygdala; vasoconstrictor co-released with NE from sympathetic terminals; stress-resilience peptide."
aliases: ["NPY", "neuropeptide Y", "Y1R", "Y2R", "Y5R", "AgRP", "ARC NPY neurons", "pancreatic polypeptide family"]
sources:
  - id: tatemoto-1982-npy-discovery
    type: peer-reviewed
    cite: "Tatemoto K, Carlquist M, Mutt V. Neuropeptide Y — a novel brain peptide with structural similarities to peptide YY and pancreatic polypeptide. Nature. 1982;296(5858):659-660."
    doi: "10.1038/296659a0"
    pmid: "6978320"
    url: "https://doi.org/10.1038/296659a0"
    accessed: "2026-06-08"
  - id: heilig-2004-npy-alcohol
    type: peer-reviewed
    cite: "Heilig M. The NPY system in stress, anxiety and depression. Neuropeptides. 2004;38(4):213-224."
    doi: "10.1016/j.npep.2004.05.002"
    pmid: "15337373"
    url: "https://doi.org/10.1016/j.npep.2004.05.002"
    accessed: "2026-06-08"
  - id: parker-2014-npy-review
    type: peer-reviewed
    cite: "Parker RM, Herzog H. Regional distribution of Y-receptor subtype mRNAs in rat brain. Eur J Neurosci. 1999;11(4):1431-1448."
    doi: "10.1046/j.1460-9568.1999.00553.x"
    pmid: "10103134"
cross_links:
  - target: 01-human/03-molecular/dopamine
    relation: connects-to
    note: "NPY Y1R on VTA neurons modulates dopamine firing; NPY in ARC inhibits POMC neurons competing with melanocortin signaling; NPY-AgRP coexpression shifts mesolimbic dopamine toward caloric reward; Y1R activation attenuates cocaine-conditioned place preference in rodents."
  - target: 01-human/03-molecular/gaba
    relation: connects-to
    note: "NPY interneurons in hippocampus and cortex are GABAergic; Y1R/Y2R on GABAergic terminals presynaptically modulate GABA release; NPY-SST+ co-expressing interneurons regulate network oscillations; NPY inhibits mossy fiber LTP and gates hippocampal theta-gamma coupling."
  - target: 01-human/06-organ/brain
    relation: modulates
    note: "NPY is the most abundant neuropeptide in the brain; ARC AgRP/NPY neurons are master orexigenic effectors; Y1R on amygdala CeA/BLA neurons is anxiolytic; brainstem NTS/LC NPY modulates autonomic tone; hippocampal NPY interneurons regulate excitability and seizure threshold."
  - target: 01-human/07-system/ptsd
    relation: connects-to
    note: "Amygdala NPY is reduced in PTSD; Y1R activation is anxiolytic; stress resilience in combat veterans correlates with higher plasma NPY; NPY attenuates the HPA axis response to acute stress; NPY agonists are proposed as pharmacotherapy for PTSD and trauma-related disorders."
  - target: 01-human/07-system/alcohol-use-disorder
    relation: connects-to
    note: "NPY reduces voluntary alcohol intake; Y2R knockout mice show increased alcohol preference; alcohol withdrawal reduces NPY in limbic regions; stress-induced alcohol relapse is attenuated by NPY; Y1R agonism reduces anxiety-driven alcohol-seeking in preclinical models."
  - target: 01-human/07-system/obesity
    relation: connects-to
    note: "ARC NPY/AgRP neurons are master orexigenic effectors: NPY → Y1R/Y5R on PVN → increased food intake; ghrelin (from stomach) activates ARC NPY/AgRP; leptin (from adipocytes) suppresses NPY/AgRP; NPY knockout alone does not cause obesity but amplifies hyperphagia in ob/ob mice."
---

# Neuropeptide Y

## Overview

**Neuropeptide Y (NPY)** is a 36-amino acid neuropeptide and the **most abundant neuropeptide in the mammalian central nervous system**. It was isolated and sequenced by Kazuhiko Tatemoto in 1982 from porcine brain as part of the pancreatic polypeptide (PP) family — a trio that includes PP itself, peptide YY (PYY), and NPY [^tatemoto-1982-npy-discovery]. The name reflects its high tyrosine (Y) content: the molecule contains 5 tyrosine residues, including the critical C-terminal amidated tyrosine required for receptor binding.

NPY is expressed by neurons throughout the hypothalamus, amygdala, hippocampus, brainstem, and spinal cord, as well as by sympathetic postganglionic neurons where it is co-released with norepinephrine. Its physiological roles span:
- **Energy homeostasis**: the most potent orexigenic neuropeptide known
- **Stress and anxiety**: anxiolytic via amygdala Y1R circuits; promotes stress resilience
- **Cardiovascular regulation**: vasoconstriction and chronotropic effects via Y1R on vascular smooth muscle
- **Alcohol and addiction**: reduces stress-driven alcohol seeking via limbic Y1R/Y2R
- **Seizure threshold**: hippocampal NPY interneurons act as endogenous anticonvulsants

[^parker-2014-npy-review]

## Structure

NPY belongs to the **pancreatic polypeptide (PP) family** along with PYY (released postprandially from intestinal L-cells) and PP (released from pancreatic islet F-cells). All share a characteristic "PP-fold" tertiary structure stabilized by hydrophobic interactions between the N-terminal polyproline helix and the C-terminal α-helix — a feature essential for receptor selectivity.

| Property | Value |
|:---|:---|
| Length | 36 amino acids |
| Molecular weight | 4272 Da |
| C-terminus | Amidated tyrosine (Tyr36-NH₂) — required for receptor binding |
| Precursor | Pre-pro-NPY (97 aa) → pro-NPY → NPY by PC1/3 and carboxypeptidase E |
| Gene | *NPY* (chromosome 7p15.3); regulated by cAMP, glucocorticoids, fasting |
| Half-life | ~10-30 min (plasma); faster in brain ECF |

### NPY Receptors

Five GPCRs mediate NPY signaling (Gi-coupled, all):

| Receptor | Gene | Distribution | Primary Actions |
|:---|:---|:---|:---|
| **Y1R** | *NPY1R* | Hypothalamus (PVN), amygdala, hippocampus, vascular smooth muscle | Food intake ↑, anxiolysis, vasomotor tone |
| **Y2R** | *NPY2R* | Hippocampus, cortex (presynaptic autoreceptor), gut | Presynaptic inhibition of NPY release (autoreceptor); reduces gut motility |
| **Y3R** | *NPYR* (atypical) | Brainstem, heart | Cardiovascular modulation; NE co-release regulation |
| **Y4R** | *NPY4R* | Hypothalamus, gut | Pancreatic polypeptide-preferring; satiety |
| **Y5R** | *NPY5R* | Hypothalamus (ARC, PVN), hippocampus | Feeding stimulation; sleep promotion |

All Y receptors couple to **Gαi** → ↓adenylyl cyclase → ↓cAMP, and also activate GIRK channels (↑K+ conductance → hyperpolarization) and inhibit voltage-gated Ca²+ channels (↓neurotransmitter exocytosis).

## Function

### 1. Energy Homeostasis — Master Orexigen

The hypothalamic arcuate nucleus (ARC) contains **NPY/AgRP co-expressing neurons** — one of the two main energy-sensing neuronal populations (the other being the anorexigenic POMC/CART neurons):

```
Fasting/Ghrelin → ARC NPY/AgRP neurons activated
    ↓
Axons project to PVN, LHA, dorsomedial hypothalamus
    ↓
Y1R/Y5R on PVN neurons → Gi → ↓cAMP → ↓CRH transcription
    → Increased food intake, reduced energy expenditure
    → Inhibits POMC/α-MSH signaling (AgRP is a competitive MC4R antagonist)

Leptin/Insulin (fed state) → ARC NPY/AgRP neurons suppressed
    → Decreased food intake
```

NPY injection into the PVN produces the most robust acute hyperphagia of any known agent — increasing food intake by >3-fold within 30 minutes. Chronic NPY overexpression in rodents produces obesity.

### 2. Stress Resilience and Anxiolysis

NPY acts as an endogenous **anxiolytic and anti-stress** peptide in the brain [^heilig-2004-npy-alcohol]:

- **Amygdala** (CeA and BLA): Y1R activation → Gi → ↓CRH release → reduced fear expression; NPY in CeA reduces conditioned fear and anxiety-like behavior
- **HPA axis attenuation**: NPY reduces CRH gene expression in PVN → blunts ACTH/cortisol surge; NPY is released during acute stress and acts as a negative feedback brake on the HPA axis
- **Locus coeruleus**: Y2R inhibits LC NE release → reduces stress-driven NE hyperactivation
- **Stress resilience biomarker**: Plasma NPY is higher in combat veterans who remain resilient vs. those who develop PTSD; controlled stress experiments in healthy humans show that high NPY responders have lower anxiety after stressor exposure

### 3. Cardiovascular Regulation

NPY is co-stored with NE in dense-core vesicles of sympathetic postganglionic neurons and co-released during high-frequency sympathetic stimulation:
- **Y1R on vascular smooth muscle** → Gi → MAPK → vasoconstriction (long-lasting, synergistic with NE)
- **Y2R on presynaptic sympathetic terminals** → autoreceptor → inhibits further NE + NPY release
- **Y1R on cardiac SA node** → reduces heart rate (negative chronotropy)
- NPY is elevated in heart failure and pheochromocytoma; contributes to coronary vasospasm

### 4. Hippocampal Excitability and Seizure Suppression

Hippocampal NPY interneurons (co-expressing somatostatin and GABA) act as **endogenous anticonvulsants**:
- Released during high-frequency bursting → Y2R on mossy fiber terminals → Gi → ↓glutamate release → terminate excitatory bursts
- Y5R on dentate granule cells → ↓excitability → higher seizure threshold
- NPY is depleted in hippocampal sclerosis (temporal lobe epilepsy); NPY gene delivery (AAV vectors) reduces seizure frequency in rodent epilepsy models — a potential gene therapy approach

### 5. Alcohol and Substance Use Modulation

NPY tonically reduces alcohol preference via limbic anxiolytic effects [^heilig-2004-npy-alcohol]:
- **Genetic evidence**: Y2R knockout mice spontaneously consume 2× more alcohol than wildtype; these mice also show higher anxiety
- **Y1R agonism** in CeA reduces stress-induced relapse drinking in rodent models
- **Withdrawal**: alcohol withdrawal reduces NPY mRNA in limbic regions, increasing anxiety that drives relapse drinking (negative reinforcement model)
- **Translation**: NPY Y1R agonists are a proposed pharmacotherapy target for AUD, particularly for stress-related relapse

## Mechanism

### Hypothalamic Energy Circuit

The ARC NPY/AgRP and POMC/CART neurons form a **push-pull system**:

| Signal | NPY/AgRP neurons | POMC neurons |
|:---|:---|:---|
| Leptin (↑) | Suppressed (LepRb → STAT3 → ↓Npy transcription) | Activated (↑POMC, α-MSH) |
| Ghrelin (↑) | Activated (GHS-R1a → Gq/Gs → ↑Npy) | Suppressed |
| Insulin (↑) | Suppressed | Activated |
| Glucose (↑) | Suppressed | Activated |
| Glucocorticoids (↑) | Activated (GRE in NPY promoter) | Suppressed |

NPY and AgRP (Agouti-related peptide) are co-expressed and functionally synergistic: NPY drives short-term feeding via Y1R/Y5R (Gi → ↓cAMP), while AgRP provides longer-term orexigenic tone by competitively blocking MC4R (the target of anorexigenic α-MSH).

### Stress Resilience Circuit

During acute stress:
1. CRH (PVN) → HPA activation → cortisol surge
2. Stress also activates NPY release in amygdala (from CeA NPY interneurons)
3. NPY → Y1R on CeA neurons → Gi → ↓CRH release from CeA → negative feedback
4. NPY → Y2R on LC → ↓NE hyperactivation
5. Net: NPY buffers the emotional and somatic amplification of acute stress

In chronic stress or PTSD, this NPY buffering is diminished — potentially via glucocorticoid-driven NPY depletion and Y1R downregulation in amygdala.

## Connections

- `connects-to` → **[Dopamine](../dopamine/README.md)** — NPY/AgRP ARC neurons inhibit POMC neurons and modulate mesolimbic dopamine tone; Y1R activation on VTA neurons reduces dopamine firing; NPY shifts reward circuitry toward caloric reward and attenuates non-food reward; Y1R activation reduces cocaine-conditioned place preference and relapse in preclinical models.

- `connects-to` → **[GABA](../gaba/README.md)** — hippocampal and cortical NPY interneurons are GABAergic (co-expressing SST); Y2R presynaptic autoreceptors modulate GABA release; NPY-SST+ interneurons regulate network oscillations (theta-gamma) and gate mossy fiber LTP; NPY inhibition of hippocampal excitation depends partly on GABA-mediated feed-forward inhibition.

- `modulates` → **[Brain](../../06-organ/brain/README.md)** — NPY is the most abundant neuropeptide in the brain; ARC NPY/AgRP neurons drive orexigenic behavior (Y1R/Y5R on PVN); CeA/BLA NPY-Y1R circuits are anxiolytic; hippocampal NPY interneurons suppress mossy fiber bursting and set seizure threshold; LC NPY attenuates NE hyperactivation during stress.

- `connects-to` → **[PTSD](../../07-system/ptsd/README.md)** — amygdala and CSF NPY are reduced in PTSD; Y1R-mediated anxiolysis in the amygdala is impaired; higher plasma NPY predicts stress resilience in combat veterans; cortisol/glucocorticoid excess in chronic stress depletes ARC and amygdala NPY; NPY Y1R agonists are under investigation as PTSD pharmacotherapy.

- `connects-to` → **[Alcohol Use Disorder](../../07-system/alcohol-use-disorder/README.md)** — NPY reduces voluntary alcohol intake via limbic anxiolysis; Y2R knockout mice show 2× baseline alcohol preference and higher anxiety; alcohol withdrawal reduces limbic NPY → anxiety → negative reinforcement relapse; Y1R agonism in CeA reduces stress-induced reinstatement of alcohol-seeking behavior in rodent models.

- `connects-to` → **[Obesity](../../07-system/obesity/README.md)** — ARC NPY/AgRP neurons are the primary drivers of hunger: NPY → Y1R/Y5R on PVN → increased food intake + reduced metabolic rate; ghrelin activates ARC NPY/AgRP neurons; leptin and insulin suppress them; chronic NPY overexpression causes obesity; NPY polymorphisms (Leu7Pro) associate with higher BMI and metabolic syndrome.

## Pathology

| Condition | NPY involvement | Clinical significance |
|:---|:---|:---|
| **Obesity** | ARC NPY/AgRP overactivity → chronic orexigenic drive; leptin resistance fails to suppress NPY neurons | NPY system failure underlies treatment-resistant hyperphagia; Y2R agonists/Y5R antagonists were investigated as anti-obesity agents |
| **PTSD** | Reduced amygdala NPY, impaired Y1R anxiolytic circuit | Plasma NPY predicts resilience vs. susceptibility; NPY Y1R agonists are in preclinical development for PTSD |
| **Alcohol Use Disorder** | Limbic NPY depletion during withdrawal → anxiety-driven relapse | Y1R agonism reduces stress-induced relapse; Y2R KO mouse model of increased alcohol preference |
| **Epilepsy** | Hippocampal NPY interneurons depleted in temporal lobe epilepsy (sclerosis) | AAV-NPY gene delivery reduces seizure frequency in rodent TLE models; translational gene therapy target |
| **Cardiovascular disease** | Co-released with NE during sympathetic activation → vasoconstriction; elevated in heart failure and pheochromocytoma | NPY drives coronary vasospasm in Prinzmetal angina; Y1R antagonism studied for hypertension |
| **Anorexia Nervosa** | Paradoxically elevated CSF NPY during restriction (compensatory hunger drive); fails to adequately drive food intake due to cognitive override | Restoration of normal NPY tone requires weight normalization |
| **Anxiety disorders** | Reduced plasma NPY associated with trait anxiety; Y1R agonism anxiolytic in animal models | Therapeutic target under investigation |

[^tatemoto-1982-npy-discovery]: Tatemoto K, Carlquist M, Mutt V. Neuropeptide Y — a novel brain peptide with structural similarities to peptide YY and pancreatic polypeptide. *Nature.* 1982;296(5858):659-660. [doi:10.1038/296659a0](https://doi.org/10.1038/296659a0) · [PubMed 6978320](https://pubmed.ncbi.nlm.nih.gov/6978320/)
[^heilig-2004-npy-alcohol]: Heilig M. The NPY system in stress, anxiety and depression. *Neuropeptides.* 2004;38(4):213-224. [doi:10.1016/j.npep.2004.05.002](https://doi.org/10.1016/j.npep.2004.05.002) · [PubMed 15337373](https://pubmed.ncbi.nlm.nih.gov/15337373/)
[^parker-2014-npy-review]: Parker RM, Herzog H. Regional distribution of Y-receptor subtype mRNAs in rat brain. *Eur J Neurosci.* 1999;11(4):1431-1448. [doi:10.1046/j.1460-9568.1999.00553.x](https://doi.org/10.1046/j.1460-9568.1999.00553.x) · [PubMed 10103134](https://pubmed.ncbi.nlm.nih.gov/10103134/)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
