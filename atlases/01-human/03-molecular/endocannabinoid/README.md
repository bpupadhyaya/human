---
schema: human-scale-entry/v1
id: endocannabinoid
name: Endocannabinoid System
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-08
summary: "Retrograde lipid signaling system: 2-AG and AEA activate CB1R (Gi, presynaptic) to suppress neurotransmitter release on demand. Regulates synaptic plasticity, appetite, pain, anxiety, and stress. THC mimics AEA; rimonabant (CB1R antagonist) caused psychiatric adverse events."
aliases: ["endocannabinoid", "endocannabinoid system", "ECS", "CB1R", "CB2R", "2-AG", "anandamide", "AEA", "FAAH", "MAGL", "cannabinoid receptor", "THC", "retrograde signaling"]
cross_links:
  - target: 01-human/03-molecular/dopamine
    relation: modulates
    note: "CB1R on VTA inputs and GABAergic interneurons modulates mesolimbic DA; 2-AG retrograde signaling → DSI/DSE → VTA DA disinhibition → NAcc surge; THC hijacks this circuit → reward; rimonabant (CB1R antagonist) reduces DA-driven cue reinstatement in preclinical models."
  - target: 01-human/03-molecular/gaba
    relation: modulates
    note: "CB1R densely expressed on GABAergic interneurons (CCK+ basket cells); 2-AG release → CB1R on GABA terminals → DSI → reduced GABA release → local disinhibition; endocannabinoid-LTD modulates inhibitory plasticity throughout hippocampus, cortex, and striatum."
  - target: 01-human/03-molecular/glutamate
    relation: modulates
    note: "CB1R on glutamatergic terminals mediates DSE (depolarization-induced suppression of excitation); 2-AG retrograde release → CB1R → Gi → reduced glutamate release; endocannabinoid-LTD in NAcc and hippocampus requires mGluR5 activation to trigger 2-AG synthesis via PLCβ/DAGLα."
  - target: 01-human/03-molecular/bdnf
    relation: connects-to
    note: "CB1R activation → ERK1/2 → BDNF expression; cannabinoids modulate hippocampal neurogenesis via CB1R-BDNF-TrkB; chronic THC reduces hippocampal BDNF in adolescent models; CBD (non-psychoactive) may increase BDNF via 5-HT1A and TrkB mechanisms."
  - target: 01-human/06-organ/brain
    relation: modulates
    note: "CB1R is among the most abundant GPCRs in the brain, densely expressed in basal ganglia, hippocampus, cerebellum, and cortex; retrograde endocannabinoid signaling modulates synaptic plasticity; THC disrupts hippocampal memory encoding and cerebellar coordination via CB1R."
  - target: 01-human/07-system/cannabis-use-disorder
    relation: connects-to
    note: "Repeated THC activates CB1R → desensitization (GRK/β-arrestin), downregulation, and reduced endocannabinoid tone; withdrawal: anxiety, irritability, insomnia, appetite loss; cannabis use disorder prevalence ~9% of users; CB1R downregulation is the primary neuroadaptation of CUD."
  - target: 01-human/07-system/ptsd
    relation: connects-to
    note: "CB1R at BLA-prefrontal synapses facilitates fear extinction via eCB-LTD; low AEA found in PTSD; THC reduces nightmares; nabilone approved in Canada for PTSD nightmares; FAAH inhibition (↑AEA) enhances extinction — supporting adjunct use in exposure therapy."
sources:
  - id: devane-1992-anandamide
    type: peer-reviewed
    cite: "Devane WA, Hanus L, Breuer A, et al. Isolation and structure of a brain constituent that binds to the cannabinoid receptor. Science. 1992;258(5090):1946-1949."
    doi: "10.1126/science.1470919"
    pmid: "1470919"
    url: "https://doi.org/10.1126/science.1470919"
  - id: lu-2016-ecs-review
    type: peer-reviewed
    cite: "Lu HC, Mackie K. An introduction to the endogenous cannabinoid system. Biol Psychiatry. 2016;79(7):516-525."
    doi: "10.1016/j.biopsych.2015.07.028"
    pmid: "26698193"
    url: "https://doi.org/10.1016/j.biopsych.2015.07.028"
---

# Endocannabinoid System

## Overview

The **endocannabinoid system (ECS)** is a retrograde lipid-based neuromodulatory system consisting of endogenous cannabinoid ligands (endocannabinoids), their G protein-coupled receptors (primarily CB1R and CB2R), and the enzymatic machinery for their synthesis and degradation. Discovered through the characterization of Δ9-tetrahydrocannabinol's (THC) mechanism of action, the ECS was later found to be a fundamental regulator of synaptic plasticity, energy balance, pain processing, and emotional homeostasis.

**Key discovery timeline:**
- 1988: First cannabinoid receptor (CB1R) identified in rat brain (Allyn Howlett)
- 1990: CB1R gene cloned (Matsuda et al.)
- 1992: Anandamide (AEA, arachidonoylethanolamide) isolated as the first endocannabinoid [^devane-1992-anandamide]
- 1993: CB2R cloned (Munro et al.)
- 1995: 2-Arachidonoylglycerol (2-AG) identified as endocannabinoid

**Defining feature — retrograde signaling:** Unlike classical neurotransmitters that signal anterograde (presynaptic → postsynaptic), endocannabinoids are synthesized on demand in the **postsynaptic neuron** in response to strong depolarization or mGluR/muscarinic receptor activation, then released to act on **presynaptic CB1R** to suppress further neurotransmitter release. This retrograde mechanism makes the ECS the primary "on-demand" synaptic modulator.

**Clinical significance:**
1. **Cannabis use disorder** — THC mimics AEA at CB1R; repeated exposure → CB1R desensitization/downregulation → withdrawal syndrome
2. **Pain and inflammation** — CB1R/CB2R both reduce pain signaling; medical cannabis for chronic pain, neuropathy, MS spasticity
3. **Appetite regulation** — CB1R in hypothalamus and brainstem drives appetite (munchies); rimonabant (CB1R antagonist) was approved for obesity then withdrawn for psychiatric adverse events
4. **Anxiety and PTSD** — endocannabinoid tone at BLA regulates fear extinction; nabilone for PTSD nightmares
5. **Epilepsy** — CBD (non-psychoactive) approved as Epidiolex for Dravet/LGS; mechanism includes TRPV1, GPR55, 5-HT1A

## Structure

### Endocannabinoid Ligands

**2-Arachidonoylglycerol (2-AG):**
- Most abundant endocannabinoid in the brain (~170× more concentrated than AEA)
- Full agonist at CB1R and CB2R
- Synthesis: Diacylglycerol (DAG) → **diacylglycerol lipase α (DAGLα)** → 2-AG; triggered by mGluR5 → PLCβ → DAG or postsynaptic depolarization → PLC
- Degradation: **Monoacylglycerol lipase (MAGL)** at presynaptic terminals (rapid); also ABHD6/12 (minor pathways)
- MAGL inhibitors (JZL184, MJN110) raise 2-AG; in development for pain and neurodegeneration

**Anandamide (AEA, N-arachidonoylethanolamide):**
- Named from Sanskrit "ananda" (bliss); partial/full agonist at CB1R; also TRPV1 agonist (vanilloid receptor)
- Much lower brain concentrations than 2-AG; acts more tonically
- Synthesis: N-arachidonoyl-phosphatidylethanolamine (NAPE) → **NAPE-PLD** (major) or multiple alternative pathways
- Degradation: **Fatty acid amide hydrolase (FAAH)** in postsynaptic neurons; FAAH inhibitors (URB597, PF-04457845) raise AEA → anxiolytic and analgesic effects in animal models; human trials for anxiety and AUD ongoing

**Other endocannabinoids:** Noladin ether, virodhamine, N-arachidonoyl-dopamine (NADA; CB1R + TRPV1)

### Cannabinoid Receptors

| Feature | CB1R | CB2R |
|:---|:---|:---|
| Gene | CNR1 (chr6q15) | CNR2 (chr1p36) |
| Class | Class A GPCR | Class A GPCR |
| Coupling | Gi/Go → ↓cAMP, ↑GIRK, ↓VGCC | Gi/Go → ↓cAMP |
| Expression (CNS) | Highest in basal ganglia, hippocampus, cerebellum, cortex | Low/absent in healthy neurons; upregulated in neuroinflammation |
| Expression (peripheral) | Adipocytes, liver, GI, spinal cord | Immune cells (microglia, macrophages, B/T cells), liver, gut |
| Psychoactivity | YES (THC effects) | No |
| Key functions | Synaptic plasticity, analgesia, appetite, reward, memory | Immune modulation, neuroinflammation, bone metabolism |

**CB1R signal transduction:**
1. Gi → **↓adenylyl cyclase** → ↓cAMP → ↓PKA activity
2. Gβγ → **activate GIRK K⁺ channels** → hyperpolarization → ↓neuronal firing
3. Gβγ → **inhibit N/P/Q-type VGCC** → ↓Ca²⁺ influx → ↓neurotransmitter release
4. ERK1/2 activation (via Gi βγ or β-arrestin) → gene regulation
5. β-arrestin recruitment → desensitization and internalization (GRK3 phosphorylation → β-arrestin 2 → clathrin-mediated endocytosis)

### FAAH and MAGL as Drug Targets

| Enzyme | Substrate | Location | Inhibitors in development |
|:---|:---|:---|:---|
| FAAH | AEA (primary), OEA, PEA | Postsynaptic neuron (intracellular) | URB597, PF-04457845 (clinical: anxiety, AUD) |
| MAGL | 2-AG (primary) | Presynaptic terminal | JZL184, MJN110, ABX-1431 (clinical: pain, MS) |
| ABHD6 | 2-AG (postsynaptic pool) | Postsynaptic neuron | — |

## Function

### Retrograde Synaptic Modulation

**Depolarization-Induced Suppression of Inhibition (DSI) / Excitation (DSE):**
1. Strong postsynaptic depolarization → Ca²⁺ influx → DAGLα activation → 2-AG synthesis
2. 2-AG released from postsynaptic membrane → diffuses backward → binds presynaptic CB1R
3. CB1R → Gi → ↓VGCC → ↓vesicular neurotransmitter release
4. DSI: suppresses GABA release (short-term) → local circuit disinhibition
5. DSE: suppresses glutamate release → reduced excitatory drive

**Endocannabinoid Long-Term Depression (eCB-LTD):**
- Sustained low-frequency stimulation + mGluR5 coactivation → 2-AG synthesis → CB1R → prolonged downregulation of neurotransmitter release → LTD
- Requires CB1R signaling to presynaptic RIM1α → impairs vesicle release probability
- Forms the cellular basis of motor learning (cerebellum), extinction memory (amygdala), and habit formation (striatum)

### Appetite and Energy Balance

CB1R in hypothalamus and brainstem regulates feeding:
- Fasting → elevated 2-AG in hypothalamus → CB1R on anorexigenic POMC neurons → reduced POMC firing → increased appetite
- Orexigenic NPY/AgRP neurons: CB1R activation → enhanced firing → increased feeding
- "Munchies" (THC): exogenous CB1R activation mimics fasting state → stimulates appetite even in fed individuals
- **Rimonabant (Acomplia):** CB1R inverse agonist; approved EU 2006 for obesity/metabolic syndrome; reduced weight, waist circumference, triglycerides; withdrawn 2008 due to depression and suicidality (EMEA)

### Pain Modulation

CB1R in PAG, spinal dorsal horn, and DRG reduces pain signaling:
- CB1R → Gi → ↓VGCC → ↓substance P/CGRP release from primary afferents
- Supraspinal CB1R in PAG → ↓excitatory transmission to rostral ventromedial medulla → reduced descending pain facilitation
- CB2R on spinal microglia/DRG macrophages → reduced neuroinflammatory cytokines → neuropathic pain reduction
- Clinical: nabiximols (Sativex; THC:CBD 1:1) approved for MS spasticity and cancer pain in multiple countries

### Fear Extinction

CB1R at BLA-prefrontal synapses regulates fear extinction:
- Fear extinction requires endocannabinoid-LTD at BLA → reduced CS-US association; FAAH inhibition (↑AEA) → enhanced extinction in rodent models
- Endocannabinoid signaling provides the "forgetting" signal that erases conditioned fear responses
- Low AEA in PTSD patients; CBD may enhance extinction by FAAH inhibition + 5-HT1A agonism

## Mechanism

### THC vs. Endocannabinoids: Pharmacological Distinctions

**Δ9-Tetrahydrocannabinol (THC):**
- Partial agonist at CB1R and CB2R; binds the same orthosteric site as 2-AG and AEA
- Unlike 2-AG (degraded within seconds by MAGL), THC is **not rapidly metabolized** by FAAH or MAGL → sustained CB1R activation (hours vs. seconds for 2-AG) — this prolonged activation explains tolerance, desensitization, and the breadth of psychoactive effects
- THC → active metabolite **11-hydroxy-THC** (psychoactive, especially oral) → 11-nor-9-carboxy-THC (inactive, urinary marker; detectable up to 30 days in chronic users)
- **CBD (cannabidiol):** Does not bind CB1R at pharmacological doses; acts at TRPV1 (desensitization), GPR55 (antagonism), 5-HT1A (partial agonist), adenosine A1/A2A (uptake inhibition); anticonvulsant via multiple mechanisms; does not produce intoxication or tolerance

### CB1R Desensitization and Tolerance

Repeated THC or high 2-AG exposure → CB1R tolerance:
1. **Short-term desensitization:** GRK3 (G protein receptor kinase 3) phosphorylates agonist-bound CB1R at C-terminus → β-arrestin 2 recruitment → uncoupling of Gi from receptor → loss of acute signaling within minutes to hours
2. **Internalization:** β-arrestin 2 → clathrin-mediated endocytosis → intracellular CB1R pool → reduced surface receptor density
3. **Downregulation:** Prolonged internalization → lysosomal degradation → net reduction in CB1R protein; requires days to weeks for reversal (measured by PET radioligand imaging in cannabis users)

### FAAH and MAGL as Druggable Targets

| Target | Mechanism | Effect | Clinical stage |
|:---|:---|:---|:---|
| **FAAH inhibition** | ↑ AEA → CB1R + TRPV1 | Anxiolytic, analgesic; enhanced extinction | Phase 2 (anxiety, AUD) |
| **MAGL inhibition** | ↑ 2-AG → CB1R | Analgesic, anti-inflammatory, neuroprotective | Phase 1-2 (pain, MS) |
| **CB1R antagonism/inverse agonism** | ↓ endocannabinoid signaling | Reduces appetite; anti-addictive | Withdrawn (rimonabant) due to psychiatric AEs |
| **CB2R agonism** | ↑ immune/glial signaling | Anti-inflammatory, neuroprotective | Phase 2 (neuroinflammation) |

## Pathology

### Cannabis Use Disorder

Repeated THC exposure → CB1R desensitization (GRK3 phosphorylation → β-arrestin) → receptor internalization → tolerance; withdrawal syndrome upon cessation: anxiety, irritability, insomnia, decreased appetite, craving. See: [Cannabis Use Disorder](../../07-system/cannabis-use-disorder/README.md)

### Neurological Applications of Cannabinoids

| Condition | Cannabinoid | Evidence |
|:---|:---|:---|
| **Dravet / LGS epilepsy** | CBD (Epidiolex) | FDA-approved 2018; NNT ~7 |
| **MS spasticity** | Nabiximols (Sativex) | Approved UK, Canada, Europe |
| **Neuropathic pain** | Medical cannabis | Moderate evidence; Canadian guideline recommended |
| **PTSD nightmares** | Nabilone | Approved Canada; RCT evidence |
| **Cancer pain** | Nabiximols | Approved Canada, UK, Europe |
| **Chemotherapy nausea** | Dronabinol, nabilone | FDA-approved |

## Connections

- `modulates` → **[Dopamine](../dopamine/README.md)** — CB1R on VTA inputs modulates mesolimbic dopamine; 2-AG retrograde signaling mediates DSI/DSE at VTA → DA disinhibition → NAcc surge; THC hijacks this mechanism → reward and reinforcement; rimonabant reduces DA-driven cue reinstatement of drug seeking.

- `modulates` → **[GABA](../gaba/README.md)** — CB1R is densely expressed on CCK+ GABAergic interneurons; postsynaptic 2-AG → CB1R on GABA terminals → DSI → reduced GABA release → local circuit disinhibition; endocannabinoid-LTD modulates inhibitory plasticity throughout hippocampus, cortex, and striatum.

- `modulates` → **[Glutamate](../glutamate/README.md)** — CB1R on glutamatergic terminals mediates DSE; 2-AG retrograde release → CB1R → Gi → reduced glutamate release; eCB-LTD in NAcc and hippocampus requires mGluR5 to trigger 2-AG synthesis via PLCβ/DAGLα — linking mGluR5 to retrograde plasticity.

- `connects-to` → **[BDNF](../bdnf/README.md)** — CB1R activation → ERK1/2 → BDNF expression; cannabinoids modulate hippocampal neurogenesis via CB1R-BDNF-TrkB; chronic THC reduces hippocampal BDNF in adolescent models; CBD may increase BDNF through 5-HT1A and TRPV1 mechanisms.

- `modulates` → **[Brain](../../06-organ/brain/README.md)** — CB1R is among the most abundant GPCRs in the brain; densely expressed in basal ganglia, hippocampus, cerebellum, and cortex; endocannabinoid retrograde signaling tunes synaptic plasticity throughout brain circuits; THC disrupts hippocampal memory encoding and cerebellar motor coordination via CB1R.

- `connects-to` → **[Cannabis Use Disorder](../../07-system/cannabis-use-disorder/README.md)** — repeated THC → CB1R desensitization and downregulation → reduced endocannabinoid tone; withdrawal: anxiety, irritability, insomnia, appetite loss (~9% of users develop CUD); CB1R downregulation is the primary neuroadaptation; no FDA-approved pharmacotherapy.

- `connects-to` → **[PTSD](../../07-system/ptsd/README.md)** — CB1R at BLA-prefrontal synapses facilitates fear extinction via eCB-LTD; low AEA in PTSD; THC reduces nightmares; nabilone approved in Canada for PTSD nightmares; FAAH inhibition (↑AEA) enhances extinction learning in rodent models — supporting adjunct use in exposure therapy.

[^devane-1992-anandamide]: Devane WA, Hanus L, Breuer A, et al. Isolation and structure of a brain constituent that binds to the cannabinoid receptor. *Science.* 1992;258(5090):1946-1949. [doi:10.1126/science.1470919](https://doi.org/10.1126/science.1470919) · [PubMed 1470919](https://pubmed.ncbi.nlm.nih.gov/1470919/)
[^lu-2016-ecs-review]: Lu HC, Mackie K. An introduction to the endogenous cannabinoid system. *Biol Psychiatry.* 2016;79(7):516-525. [doi:10.1016/j.biopsych.2015.07.028](https://doi.org/10.1016/j.biopsych.2015.07.028) · [PubMed 26698193](https://pubmed.ncbi.nlm.nih.gov/26698193/)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
