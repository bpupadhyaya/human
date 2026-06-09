---
schema: human-scale-entry/v1
id: bdnf
name: BDNF
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-08
summary: "BDNF activates TrkB → MAPK/PI3K → neuronal survival, dendritic complexity, and LTP; reduced in MDD, Alzheimer's, and with aging; exercise robustly raises BDNF; Val66Met SNP impairs activity-dependent secretion and elevates risk for depression and cognitive decline."
aliases: ["brain-derived neurotrophic factor", "BDNF", "NGF-2", "BDNF Val66Met", "TrkB ligand", "neurotrophin", "NTRK2 ligand", "BDNF neuroplasticity", "hippocampal BDNF"]
sources:
  - id: barde-1982-bdnf-discovery
    type: peer-reviewed
    cite: "Barde YA, Edgar D, Thoenen H. Purification of a new neurotrophic factor from mammalian brain. EMBO J. 1982;1(5):549-553."
    doi: "10.1002/j.1460-2075.1982.tb01207.x"
    pmid: "7188352"
    url: "https://doi.org/10.1002/j.1460-2075.1982.tb01207.x"
    accessed: "2026-06-08"
  - id: duman-2012-bdnf-depression
    type: peer-reviewed
    cite: "Duman RS, Aghajanian GK. Synaptic dysfunction in depression: potential therapeutic targets. Science. 2012;338(6103):68-72."
    doi: "10.1126/science.1222939"
    pmid: "23042884"
    url: "https://doi.org/10.1126/science.1222939"
    accessed: "2026-06-08"
  - id: erickson-2011-exercise-bdnf-hippocampus
    type: peer-reviewed
    cite: "Erickson KI, Voss MW, Prakash RS, et al. Exercise training increases size of hippocampus and improves memory. Proc Natl Acad Sci USA. 2011;108(7):3017-3022."
    doi: "10.1073/pnas.1015950108"
    pmid: "21251194"
    url: "https://doi.org/10.1073/pnas.1015950108"
    accessed: "2026-06-08"
cross_links:
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "BDNF deficiency is central to the neuroplasticity hypothesis of MDD: stress reduces hippocampal BDNF; antidepressants (SSRIs, MAOIs, ketamine) normalize BDNF; BDNF Val66Met SNP impairs activity-dependent secretion and increases MDD vulnerability."
  - target: 01-human/07-system/alzheimers-disease
    relation: connects-to
    note: "BDNF and TrkB expression are reduced in hippocampus and basal forebrain of Alzheimer's disease; BDNF deficiency impairs cholinergic neuron survival; AAV-BDNF gene therapy is in early clinical trials for AD as a neuroprotective strategy."
  - target: 01-human/07-system/parkinsons-disease
    relation: connects-to
    note: "BDNF supports dopaminergic neuron survival in substantia nigra via TrkB/MAPK; BDNF is reduced in SNc in Parkinson's disease; GDNF and BDNF trophic factor delivery (AAV-GDNF) are in Phase 1-2 clinical trials for PD neuroprotection."
  - target: 01-human/06-organ/brain
    relation: modulates
    note: "BDNF is the most abundant neurotrophin in adult brain; hippocampal BDNF is essential for adult neurogenesis in the subgranular zone and LTP in CA1/CA3; aerobic exercise increases hippocampal BDNF and expands hippocampal volume in humans."
  - target: 01-human/07-system/ptsd
    relation: connects-to
    note: "Chronic stress-induced BDNF suppression causes hippocampal volume loss (~8%) in PTSD; reduced BDNF impairs contextual fear discrimination and extinction consolidation; SSRIs normalize BDNF and partially restore hippocampal volume; Val66Met SNP increases PTSD risk."
  - target: 01-human/07-system/bipolar-disorder
    relation: connects-to
    note: "BDNF Val66Met SNP associates with 2× increased bipolar risk; BDNF is reduced during depressive episodes; lithium and valproate both upregulate BDNF and BCL-2, promoting hippocampal neurogenesis and neuroprotection as a convergent mood stabilizer mechanism."
  - target: 01-human/07-system/huntingtons-disease
    relation: connects-to
    note: "mHTT disrupts REST/NRSF cytoplasmic sequestration → nuclear REST represses BDNF transcription; mHTT impairs HAP1-mediated BDNF vesicle transport from cortex to striatum → MSN trophic deprivation; BDNF/TrkB restoration is a key Huntington disease therapeutic goal."
  - target: 01-human/07-system/attention-deficit-hyperactivity-disorder
    relation: connects-to
    note: "BDNF Val66Met SNP is over-represented in ADHD; BDNF supports PFC dopaminergic circuit maturation; stimulant treatment increases BDNF in PFC; aerobic exercise, which robustly raises BDNF, reduces ADHD symptom severity and improves executive function outcomes in children."
  - target: 01-human/07-system/alcohol-use-disorder
    relation: connects-to
    note: "Chronic alcohol reduces BDNF in NAcc and dorsomedial striatum → impairs BDNF-mediated braking on compulsive drinking; BDNF infusion into NAcc reduces ethanol preference in rodent models; abstinence partially restores BDNF; Val66Met BDNF SNP associated with AUD vulnerability."
---

# BDNF

## Overview

**BDNF (Brain-Derived Neurotrophic Factor)** is the most abundantly expressed and studied member of the **neurotrophin family** — a group of secreted dimeric proteins that regulate neuronal survival, differentiation, synaptic plasticity, and cognitive function. BDNF was first purified from pig brain by Barde, Edgar, and Thoenen in 1982 [^barde-1982-bdnf-discovery] and later identified as a key regulator of hippocampal long-term potentiation (LTP), adult neurogenesis, and the molecular basis of activity-dependent synaptic strengthening.

BDNF is encoded by the **BDNF gene** (chromosome 11p14.1, 11 exons) and produced as **proBDNF** (32 kDa) → cleaved to **mature BDNF** (14 kDa) by furin or tPA/plasminogen extracellularly. This processing is functionally important: proBDNF preferentially activates **p75NTR** (triggering apoptosis and long-term depression), while mature BDNF activates **TrkB** (NTRK2, tropomyosin receptor kinase B) to promote survival and LTP.

BDNF is critical at the intersection of three major disease categories:
1. **Neuropsychiatric disorders**: Depression, PTSD, anxiety (reduced hippocampal BDNF)
2. **Neurodegenerative diseases**: Alzheimer's, Parkinson's, Huntington's (BDNF-TrkB signaling fails)
3. **Cognitive aging**: Declining BDNF with age; exercise is the most potent lifestyle intervention to restore BDNF

## Structure

### Protein structure

**Mature BDNF** is a **non-covalent homodimer** (27.8 kDa total):
- Each monomer: 119 amino acids with three disulfide bonds forming a **cystine knot** (conserved structural motif shared by all neurotrophins: NGF, BDNF, NT-3, NT-4/5)
- The cystine knot core is surrounded by three pairs of β-hairpin loops (loop 1, 2, 4) that define receptor-binding specificity
- BDNF binds TrkB with Kd ~1 nM; NGF binds TrkA; NT-3 binds TrkC (with some cross-reactivity)

**Val66Met polymorphism (rs6265):**
- The most studied single nucleotide polymorphism in neuroscience: valine (Val) → methionine (Met) at position 66 of the prodomain
- Val66Met reduces activity-dependent BDNF secretion ~30-40% without affecting constitutive (basal) secretion; the prodomain with Met impairs BDNF trafficking into regulated secretory vesicles
- Met allele (carried by ~30% of Europeans, ~50% of Asians): associated with smaller hippocampal volume, reduced episodic memory performance, increased risk of MDD, anxiety, PTSD, and earlier cognitive decline in aging
- Paradoxically, Val66Met carriers show reduced anxiety in some populations (controversial; moderating role of serotonin transporter 5-HTTLPR)

### Regulation of BDNF expression

BDNF expression is remarkably **activity-dependent** — regulated by neuronal firing, synaptic glutamate activity, calcium influx, and numerous transcription factors:

| Stimulus | Mechanism | Timescale |
|:---|:---|:---|
| **Neuronal activity (action potentials)** | Ca²⁺ influx → CaMKIV → CREB phosphorylation (Ser133) → CRE binding on BDNF promoter IV → rapid transcription | Minutes to hours |
| **NMDA receptor activation** | Ca²⁺/CaM → CaMKII → MAPK → CREB; also MEF2 transcription factor | Minutes |
| **Aerobic exercise** | Muscular contraction → IGF-1, irisin → hippocampal BDNF | Hours to days (sustained) |
| **Serotonin (5-HT)** | SSRIs → increased 5-HT → 5-HT receptor → downstream CREB activation → BDNF induction | Weeks (explains SSRI delay) |
| **BDNF itself** | Auto-amplification via TrkB → ERK → CREB → BDNF gene transcription | Self-reinforcing |
| **Chronic stress / glucocorticoids** | CORT → GR → repression of BDNF promoters (p-CREB dephosphorylation, epigenetic silencing) | Chronic (days to weeks) |
| **Ketamine** | Rapid AMPA receptor stimulation → BDNF release → TrkB → mTOR → AMPA receptor synthesis | Hours (rapid antidepressant effect) |

**Epigenetic regulation:** BDNF promoter methylation silences BDNF expression in chronic stress and early-life adversity; histone deacetylase inhibitors (valproate, vorinostat) increase BDNF by chromatin remodeling.

## Function

### TrkB signaling pathway

Mature BDNF binds TrkB dimers → receptor tyrosine kinase autophosphorylation at Y705, Y706 (kinase domain), Y515 (Shc), Y816 (PLCγ binding) → three major downstream cascades:

**1. MAPK/ERK pathway:**
- pY515 → Shc → Grb2/SOS → Ras → Raf → MEK → ERK1/2
- ERK1/2 → phosphorylate CREB (Ser133) → BDNF, c-Fos, Arc gene transcription
- MAPK → RSK2 → CREB; also p70S6K → ribosomal protein synthesis
- **Biological effect:** Neuronal survival, dendritic growth, synaptic protein synthesis

**2. PI3K/Akt pathway:**
- pY515 → IRS-1 → PI3K → PIP3 → PDK1 → Akt (Ser473)
- Akt → phosphorylates and inactivates: GSK-3β (↓pro-apoptotic tau phosphorylation), FOXO transcription factors (↓Bim/FasL), Bad (↓apoptosis)
- Akt → mTORC1 → protein synthesis, spine growth, LTP maintenance
- **Biological effect:** Anti-apoptosis, cell survival, synaptic growth

**3. PLCγ pathway:**
- pY816 → PLCγ → PIP2 → DAG + IP3 → PKC activation + intracellular Ca²⁺ release
- PKC → MAPK synergy; Ca²⁺ → CaMKII → LTP induction mechanisms
- **Biological effect:** Short-term synaptic plasticity, neurotransmitter release modulation

### Long-term potentiation and memory

BDNF is essential for **late-phase LTP (L-LTP)** — the form of synaptic strengthening that persists beyond 3 hours and requires new protein synthesis:
- BDNF released from postsynaptic dendrites (upon NMDA receptor-mediated Ca²⁺ influx) acts on presynaptic TrkB → increased glutamate release probability
- BDNF acts on postsynaptic TrkB → mTORC1 → increased AMPA receptor synthesis and surface trafficking → sustained synaptic strength
- Blocking BDNF-TrkB signaling (with TrkB-Fc scavenger) during LTP induction prevents memory consolidation

**Adult hippocampal neurogenesis:**
- BDNF is essential for survival and dendritic maturation of newly born neurons in the subgranular zone (SGZ) of the dentate gyrus
- Antidepressants (SSRIs, ketamine) increase BDNF → increased hippocampal neurogenesis → improved pattern separation and stress resilience
- Neurogenesis suppression (irradiation, glucocorticoids) blocks behavioral antidepressant effects in rodents — suggesting neurogenesis is a downstream target of BDNF required for antidepressant response

### Exercise and BDNF

Aerobic exercise is the most potent and accessible method to increase brain BDNF [^erickson-2011-exercise-bdnf-hippocampus]:
- 1-year aerobic exercise program in older adults (120 min/week): increased hippocampal volume 2% vs. 1.4% decrease in stretching controls; improved spatial memory; correlated with blood BDNF increase
- Mechanisms: muscular PGC-1α → FNDC5/irisin → crosses BBB → BDNF expression; IGF-1 from liver/muscle → brain; lactate → MCT2 → hippocampus → increased BDNF via VEGF
- Resistance training also increases BDNF (via IGF-1 pathway)

## Mechanism

### Antidepressant convergence on BDNF

The **neurotrophic hypothesis of depression** (Duman and Aghajanian, 2012) [^duman-2012-bdnf-depression] posits that reduced BDNF in hippocampus and prefrontal cortex is a common mechanism underlying depression, and that all effective antidepressants ultimately restore BDNF signaling:

**Conventional antidepressants (SSRIs, SNRIs):**
- Increased serotonin/norepinephrine → monoamine receptor activation → CREB phosphorylation → BDNF gene transcription
- Delayed 2–4 week onset of antidepressant effect corresponds to the timeline for BDNF-driven neurogenesis and synaptic remodeling

**Ketamine (fast-acting antidepressant):**
- At subanesthetic doses: blocks tonic NMDA receptor activation on GABAergic interneurons → disinhibition of pyramidal neurons → burst glutamate release → postsynaptic AMPA receptor stimulation → BDNF release from dendrites → TrkB → mTOR → rapid AMPA receptor synthesis
- Antidepressant effect within 2–4 hours; persists 1–2 weeks; BDNF is mechanistically required (BDNF Val66Met mice are ketamine-insensitive in preclinical models)
- Esketamine (Spravato, FDA-approved 2019): intranasal S-ketamine for treatment-resistant MDD

**ECT (electroconvulsive therapy):**
- Most effective treatment for severe/refractory MDD; mechanism: generalized seizure → massive BDNF induction → hippocampal neurogenesis → antidepressant effect

### proBDNF/BDNF balance

The ratio of proBDNF to mature BDNF in synapses has opposing functional consequences:
- **proBDNF → p75NTR:** Long-term depression (LTD), dendritic pruning, apoptosis — "forget" signal
- **Mature BDNF → TrkB:** Long-term potentiation (LTP), dendritic growth, survival — "strengthen" signal
- In depression and stress, increased furin activity is reduced → more proBDNF; increased MMP-9/tPA activity → more mature BDNF after ketamine

## Connections

**→ [Major Depressive Disorder](../../07-system/major-depressive-disorder/)**: BDNF deficiency is central to the neuroplasticity hypothesis of MDD; stress reduces hippocampal BDNF via glucocorticoid-mediated CREB repression; SSRIs, MAOIs, and ketamine all normalize BDNF; Val66Met SNP impairs activity-dependent secretion and increases MDD vulnerability.

**→ [Alzheimer's Disease](../../07-system/alzheimers-disease/)**: BDNF and TrkB expression are reduced in hippocampus and basal forebrain of Alzheimer's disease; BDNF deficiency impairs cholinergic neuron survival and LTP; AAV-BDNF gene therapy and TrkB agonists are in early clinical trials for AD neuroprotection.

**→ [Parkinson's Disease](../../07-system/parkinsons-disease/)**: BDNF supports dopaminergic neuron survival in substantia nigra via TrkB/MAPK signaling; BDNF is reduced in SNc in Parkinson's disease; GDNF and BDNF delivery via convection-enhanced AAV infusion are in Phase 1-2 trials as disease-modifying PD therapy.

**→ [Brain](../../06-organ/brain/)**: BDNF is the most abundant neurotrophin in the adult brain; hippocampal BDNF is essential for subgranular zone adult neurogenesis and CA1/CA3 LTP; aerobic exercise increases hippocampal BDNF and expands hippocampal volume by ~2% in controlled trials.

**→ [Bipolar Disorder](../../07-system/bipolar-disorder/)**: BDNF Val66Met SNP associates with 2× increased bipolar disorder risk; BDNF is reduced during depressive episodes; lithium and valproate both upregulate BDNF and BCL-2, promoting hippocampal neurogenesis and neuroprotection as a convergent mood stabilizer mechanism.

**→ [Huntington Disease](../../07-system/huntingtons-disease/)**: mHTT disrupts REST/NRSF cytoplasmic sequestration → nuclear REST represses BDNF transcription; mHTT impairs HAP1-mediated BDNF vesicle transport from cortex to striatum, depriving striatal MSNs of trophic support; BDNF/TrkB signaling restoration is a key therapeutic goal in HD.

**→ [ADHD](../../07-system/attention-deficit-hyperactivity-disorder/)**: BDNF Val66Met SNP is over-represented in ADHD; BDNF supports PFC dopaminergic circuit maturation; stimulant treatment increases BDNF expression in PFC; aerobic exercise, which robustly raises BDNF, reduces ADHD symptom severity and improves executive function outcomes in children.

**→ [Alcohol Use Disorder](../../07-system/alcohol-use-disorder/)**: chronic alcohol reduces BDNF in NAcc and dorsomedial striatum → impairs BDNF-mediated braking on compulsive drinking; BDNF infusion into NAcc reduces ethanol preference in rodent models; abstinence partially restores BDNF; Val66Met BDNF SNP is associated with increased AUD vulnerability.

[^barde-1982-bdnf-discovery]: Barde YA, Edgar D, Thoenen H. Purification of a new neurotrophic factor from mammalian brain. *EMBO J.* 1982;1(5):549-553. [doi:10.1002/j.1460-2075.1982.tb01207.x](https://doi.org/10.1002/j.1460-2075.1982.tb01207.x) · [PubMed 7188352](https://pubmed.ncbi.nlm.nih.gov/7188352/)
[^duman-2012-bdnf-depression]: Duman RS, Aghajanian GK. Synaptic dysfunction in depression: potential therapeutic targets. *Science.* 2012;338(6103):68-72. [doi:10.1126/science.1222939](https://doi.org/10.1126/science.1222939) · [PubMed 23042884](https://pubmed.ncbi.nlm.nih.gov/23042884/)
[^erickson-2011-exercise-bdnf-hippocampus]: Erickson KI, Voss MW, Prakash RS, et al. Exercise training increases size of hippocampus and improves memory. *Proc Natl Acad Sci USA.* 2011;108(7):3017-3022. [doi:10.1073/pnas.1015950108](https://doi.org/10.1073/pnas.1015950108) · [PubMed 21251194](https://pubmed.ncbi.nlm.nih.gov/21251194/)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
