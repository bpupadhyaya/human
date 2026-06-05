---
schema: human-scale-entry/v1
id: dopamine
name: Dopamine
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-04
summary: "Catecholamine neurotransmitter and hormone synthesized from L-DOPA in dopaminergic neurons. Mediates reward, motor control, cognition, and prolactin inhibition via four major CNS pathways and D1–D5 GPCRs."
aliases: ["DA", "3,4-dihydroxyphenethylamine", "dopaminergic"]
sources:
  - id: schultz-1998-reward
    type: peer-reviewed
    cite: "Schultz W. Predictive reward signal of dopamine neurons. J Neurophysiol. 1998;80(1):1-27."
    doi: "10.1152/jn.1998.80.1.1"
    pmid: "9658025"
  - id: carlsson-2000-nobel
    type: peer-reviewed
    cite: "Carlsson A. A half-century of neurotransmitter research: impact on neurology and psychiatry. Nobel Lecture, 2000. Biosci Rep. 2001;21(4):333-344."
    doi: "10.1023/a:1017979709343"
    pmid: "12092847"
    accessed: "2026-06-04"
  - id: stahl-psychopharm
    type: textbook
    cite: "Stahl SM. Stahl's Essential Psychopharmacology: Neuroscientific Basis and Practical Applications. 5th ed. Cambridge University Press; 2021."
    url: "https://stahlonline.cambridge.org"
    accessed: "2026-06-04"
  - id: beaulieu-2011-da-signaling
    type: peer-reviewed
    cite: "Beaulieu JM, Gainetdinov RR. The physiology, signaling, and pharmacology of dopamine receptors. Pharmacol Rev. 2011;63(1):182-217."
    doi: "10.1124/pr.110.002642"
    pmid: "21303898"
cross_links:
  - target: 01-human/04-cellular/neuron
    relation: modulates
    note: "Dopamine modulates neuronal excitability and plasticity via D1-like (Gs/cAMP) and D2-like (Gi/GIRK) receptor signaling in dopaminoceptive neurons throughout the brain."
  - target: 01-human/05-tissue/synapse
    relation: modulates
    note: "Dopamine modulates synaptic plasticity (LTP/LTD threshold) and neurotransmitter release at excitatory and inhibitory synapses via presynaptic and postsynaptic D1–D5 receptors."
  - target: 01-human/04-cellular/neuron
    relation: expressed-by
    note: "Synthesized and released by dopaminergic neurons in the VTA, SNc, and arcuate nucleus."
  - target: 01-human/06-organ/brain
    relation: modulates
    note: "Dopamine regulates reward processing, motor control, executive cognition, and hormonal output across multiple brain circuits."
  - target: 01-human/07-system/nervous-system
    relation: part-of
    note: "Dopamine is a core chemical signal within the nervous system."
  - target: 01-human/03-molecular/norepinephrine
    relation: modulates
    note: "Modulates by Norepinephrine."
  - target: 01-human/02-atomic/copper
    relation: modulated-by
    note: "Modulated by Copper."
  - target: 03-medicine/02-traditional/st-johns-wort
    relation: modulated-by
    note: "Modulated by St. John's Wort (Hypericum perforatum)."
---

# Dopamine

## Overview

Dopamine (DA) is a **catecholamine neurotransmitter and neuromodulator** — one of the most functionally versatile small molecules in the human brain. It serves as both a fast-acting synaptically released signal and a diffuse volumetric modulator, shaping the activity of vast cortical and subcortical networks. Dopamine is also a circulating hormone from the adrenal medulla, and is the direct metabolic precursor to norepinephrine and epinephrine.

In the brain, dopaminergic neurons are numerically rare — perhaps 400,000–600,000 in the adult human brain — yet their projection fields span enormous territories, from nucleus accumbens to prefrontal cortex to dorsal striatum [^stahl-psychopharm]. The consequences of their dysfunction are correspondingly vast: depletion of substantia nigra pars compacta (SNc) neurons causes **Parkinson's disease**; dysregulated dopaminergic signaling is central to the pathophysiology of **schizophrenia**, **addiction**, **ADHD**, and **bipolar disorder**.

Dopamine's fundamental role in **reward prediction error signaling** — discovered through the landmark single-unit recordings of Wolfram Schultz [^schultz-1998-reward] — has reshaped our understanding of how the brain learns from experience and why motivational dysfunction underlies so many psychiatric conditions.

## Structure

### Chemical identity

Dopamine is a **catecholamine**: it contains a catechol ring (benzene-1,2-diol) and a two-carbon amine sidechain. Molecular formula: C₈H₁₁NO₂; molecular weight: 153.18 g/mol. It belongs to the same chemical family as norepinephrine (noradrenaline) and epinephrine (adrenaline), differing only in the presence or absence of hydroxyl substitutions on the β-carbon of the sidechain.

### Biosynthesis

Dopamine synthesis proceeds through the catecholamine biosynthetic cascade, originating from the dietary amino acid **L-tyrosine**:

| Step | Enzyme | Cofactor | Product |
|:---|:---|:---|:---|
| 1 | **Tyrosine hydroxylase (TH)** — rate-limiting | Tetrahydrobiopterin (BH₄), Fe²⁺, O₂ | L-DOPA (levodopa) |
| 2 | **DOPA decarboxylase (aromatic L-amino acid decarboxylase, AADC)** | Pyridoxal phosphate (B6) | **Dopamine** |

In noradrenergic and adrenergic neurons, dopamine is further converted:
- Dopamine → **norepinephrine** by dopamine β-hydroxylase (DBH, in the vesicle lumen)
- Norepinephrine → **epinephrine** by phenylethanolamine N-methyltransferase (PNMT)

Thus dopamine is both a functional transmitter in its own right and the obligate precursor to all catecholamines.

### Vesicular packaging and release

Dopamine is packaged into **large dense-core vesicles** and **small synaptic vesicles** by the vesicular monoamine transporter **VMAT2** (SLC18A2), which uses a proton gradient to concentrate dopamine ~100-fold within vesicles. Exocytosis is calcium-triggered via the SNARE machinery (see synapse entry). Reuptake is mediated by the **dopamine transporter DAT** (SLC6A3), a Na⁺/Cl⁻-cotransporter that clears dopamine from the synapse and is the pharmacological target of cocaine and amphetamine.

### Degradation

Dopamine is inactivated by two enzymatic pathways:
- **MAO** (monoamine oxidase, isoforms MAO-A and MAO-B) — oxidative deamination, producing DOPAC
- **COMT** (catechol-O-methyltransferase) — O-methylation, producing 3-methoxytyramine

Final metabolite: **homovanillic acid (HVA)**, measured in CSF as a marker of central dopaminergic turnover.

### Receptors

Dopamine signals through five GPCRs — **D1 through D5** — divided into two families [^beaulieu-2011-da-signaling]:

| Family | Receptors | G-protein | cAMP effect | Key locations |
|:---|:---|:---|:---|:---|
| **D1-like** | D1, D5 | Gαs | ↑ cAMP / PKA | Striatum, prefrontal cortex, nucleus accumbens |
| **D2-like** | D2, D3, D4 | Gαi/o | ↓ cAMP; ↑ GIRK | Striatum, limbic cortex, VTA (autoreceptors), pituitary |

D2-like receptors also serve as **presynaptic autoreceptors** on dopaminergic terminals and somatodendrites, creating a feedback brake on dopamine synthesis and release. This autoreceptor function is the target of antipsychotic drugs, which at therapeutic doses preferentially occupy D2 receptors.

## Function

### The four dopaminergic pathways

| Pathway | Origin → Target | Function | Disease relevance |
|:---|:---|:---|:---|
| **Mesolimbic** | VTA → nucleus accumbens, amygdala, hippocampus | Reward, motivation, aversion prediction error, emotional salience | Addiction, schizophrenia (positive symptoms), depression |
| **Mesocortical** | VTA → prefrontal cortex, anterior cingulate | Working memory, executive function, cognitive flexibility | Schizophrenia (negative/cognitive symptoms), ADHD |
| **Nigrostriatal** | SNc → putamen, caudate (dorsal striatum) | Voluntary motor control, habit formation, procedural learning | Parkinson's disease (pathway degeneration) |
| **Tuberoinfundibular** | Hypothalamic arcuate nucleus → median eminence | Tonic inhibition of prolactin secretion from the anterior pituitary | Hyperprolactinemia (D2 blockade by antipsychotics) |

### Reward prediction error

Schultz's 1998 recordings [^schultz-1998-reward] established that dopamine neurons encode a **temporal difference reward prediction error**: they fire phasically when an unexpected reward occurs, are suppressed when an expected reward is omitted, and are unchanged when a cued reward arrives as predicted. This is the neural substrate of Pavlovian and instrumental conditioning and has become a cornerstone of computational neuroscience and psychiatry.

## Mechanism

### D1-like receptor cascade

D1/D5 activation couples to Gαs → adenylyl cyclase → ↑cAMP → PKA activation → phosphorylation of **DARPP-32** (dopamine and cAMP-regulated phosphoprotein 32) and AMPA receptor GluA1 subunits → enhanced synaptic potentiation. This pathway drives the "direct" basal ganglia pathway (striatonigral), which facilitates motor programs and reward-driven behavior.

### D2-like receptor cascade

D2/D3/D4 couple to Gαi/o → inhibition of adenylyl cyclase → ↓cAMP; additionally activate GIRK (K⁺) channels → membrane hyperpolarization → reduced firing. The "indirect" basal ganglia pathway (striatopallidal) expresses predominantly D2 and when activated suppresses movement and behavior.

### Dopamine and long-term synaptic plasticity

Dopamine gates **corticostriatal LTP and LTD** by modulating NMDA receptor function and AMPA receptor trafficking via PKA. DA acts as a "gating signal" — it does not initiate plasticity but determines whether glutamatergic activity will be reinforced or suppressed. This explains why rewarding events (high DA) lead to behavioral learning and why DA depletion impairs motor learning.

## Connections

- `expressed-by` → **[neuron](../../04-cellular/neuron/README.md)** — synthesized and released by dopaminergic neurons in VTA, SNc, and arcuate nucleus
- `modulates` → **[brain](../../06-organ/brain/README.md)** — shapes reward, motor control, cognition, and pituitary function
- `part-of` → **[nervous-system](../../07-system/nervous-system/README.md)** — foundational neurotransmitter of the CNS

## Pathology

| Disease | Mechanism | Therapeutic implication |
|:---|:---|:---|
| **Parkinson's disease** | Selective degeneration of SNc dopaminergic neurons (>50–70% loss before clinical onset) | Levodopa (L-DOPA), dopamine agonists, MAO-B inhibitors |
| **Schizophrenia** | Excess mesolimbic DA (positive symptoms); insufficient mesocortical DA (negative/cognitive) | D2 antagonists (typical/atypical antipsychotics) |
| **Addiction** | Drug-induced supraphysiological DA release hijacks reward circuitry; blunts natural rewards | DAT inhibitors, DA agonists for withdrawal |
| **ADHD** | Reduced DA signaling in PFC and striatum impairs executive function | Methylphenidate (DAT block), amphetamine (DA release) |
| **Depression** | Reduced mesocortical DA contributes to anhedonia | Bupropion (DAT/NET inhibitor), dopamine agonist adjuncts |
| **Hyperprolactinemia** | D2 blockade in tuberoinfundibular pathway removes tonic prolactin suppression | Dopamine agonists (bromocriptine, cabergoline) |

[^schultz-1998-reward]: Schultz W. Predictive reward signal of dopamine neurons. *J Neurophysiol.* 1998;80(1):1-27. [doi:10.1152/jn.1998.80.1.1](https://doi.org/10.1152/jn.1998.80.1.1) · [PubMed 9658025](https://pubmed.ncbi.nlm.nih.gov/9658025/)
[^carlsson-2000-nobel]: Carlsson A. A half-century of neurotransmitter research: impact on neurology and psychiatry. *Biosci Rep.* 2001;21(4):333-344. [doi:10.1023/a:1017979709343](https://doi.org/10.1023/a:1017979709343) · [PubMed 12092847](https://pubmed.ncbi.nlm.nih.gov/12092847/)
[^stahl-psychopharm]: Stahl SM. *Stahl's Essential Psychopharmacology: Neuroscientific Basis and Practical Applications.* 5th ed. Cambridge University Press; 2021. [stahlonline.cambridge.org](https://stahlonline.cambridge.org)
[^beaulieu-2011-da-signaling]: Beaulieu JM, Gainetdinov RR. The physiology, signaling, and pharmacology of dopamine receptors. *Pharmacol Rev.* 2011;63(1):182-217. [doi:10.1124/pr.110.002642](https://doi.org/10.1124/pr.110.002642) · [PubMed 21303898](https://pubmed.ncbi.nlm.nih.gov/21303898/)
