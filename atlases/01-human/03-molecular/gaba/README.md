---
schema: human-scale-entry/v1
id: gaba
name: GABA
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-04
summary: "γ-Aminobutyric acid — the principal inhibitory neurotransmitter of the brain. Acts via GABA-A (ionotropic Cl⁻ channel) and GABA-B (metabotropic GPCR) receptors. E/I balance governs circuit stability; GABA-A is target of benzodiazepines, barbiturates, and anesthetics."
aliases: ["γ-aminobutyric acid", "GABA-A", "GABA-B", "GABAergic", "gamma-aminobutyric acid"]
sources:
  - id: olsen-sieghart-2008
    type: peer-reviewed
    cite: "Olsen RW, Sieghart W. International Union of Pharmacology. LXX. Subtypes of gamma-aminobutyric acid(A) receptors: classification on the basis of subunit composition, pharmacology, and function. Pharmacol Rev. 2008;60(3):243-260."
    doi: "10.1124/pr.108.00505"
    pmid: "18790874"
  - id: purves-neuroscience
    type: textbook
    cite: "Purves D, Augustine GJ, Fitzpatrick D, et al. Neuroscience. 6th ed. Sinauer Associates; 2018."
    url: "https://www.ncbi.nlm.nih.gov/books/NBK10792/"
    accessed: "2026-06-04"
  - id: bowery-smart-2006
    type: peer-reviewed
    cite: "Bowery NG, Smart TG. GABA and glycine as neurotransmitters: a brief history. Br J Pharmacol. 2006;147(Suppl 1):S109-S119."
    doi: "10.1038/sj.bjp.0706443"
    pmid: "16402094"
  - id: sieghart-2015-gaba-subunits
    type: peer-reviewed
    cite: "Sieghart W. Allosteric modulation of GABAA receptors via multiple drug-binding sites. Adv Pharmacol. 2015;72:53-96."
    doi: "10.1016/bs.apha.2014.10.002"
    pmid: "25600566"
    accessed: "2026-06-04"
cross_links:
  - target: 01-human/04-cellular/neuron
    relation: modulates
    note: "GABA hyperpolarizes postsynaptic neurons via GABA-A (Cl⁻ influx) and GABA-B (K⁺ efflux/↓cAMP) receptors, reducing excitability and action potential firing."
  - target: 01-human/04-cellular/neuron
    relation: expressed-by
    note: "Synthesized and released by GABAergic interneurons, the predominant inhibitory cell class of the CNS."
  - target: 01-human/05-tissue/synapse
    relation: modulates
    note: "Mediates fast and slow inhibitory synaptic transmission, opposing glutamatergic excitation to maintain E/I balance."
  - target: 01-human/06-organ/brain
    relation: modulates
    note: "GABA governs neural circuit stability, oscillations, and synchrony across all brain regions."
  - target: 01-human/07-system/nervous-system
    relation: part-of
    note: "GABA is the primary inhibitory chemical signal throughout the CNS."
  - target: 01-human/02-atomic/chloride
    relation: modulated-by
    note: "Modulated by Chloride."
  - target: 01-human/07-system/epilepsy
    relation: connects-to
    note: "Loss of GABAergic inhibitory tone — via SCN1A LOF, GABA-A subunit mutations, or interneuron loss — causes epilepsy; GABA-A potentiators (benzodiazepines, clobazam) and GABA-T inhibitors (valproate, vigabatrin) are the most widely used antiepileptic drug classes."
  - target: 01-human/03-molecular/scn1a
    relation: connects-to
    note: "Nav1.1 (SCN1A) is the dominant sodium channel in PV+ GABAergic interneurons; SCN1A haploinsufficiency silences these interneurons → reduced GABA release → cortical disinhibition; clobazam (GABA-A modulator) and valproate (GABA-T inhibitor) are mainstay Dravet treatments."
  - target: 01-human/07-system/schizophrenia
    relation: connects-to
    note: "Parvalbumin interneuron hypofunction in PFC — reduced GAD67, impaired GABA synthesis — causes deficient gamma oscillations that underlie working memory deficits in schizophrenia; GABAergic interneuron loss may be primary, upstream of dopamine and glutamate dysregulation."
  - target: 01-human/07-system/bipolar-disorder
    relation: connects-to
    note: "Valproate potentiates GABA-A function and blocks voltage-gated Na⁺/Ca²⁺ channels in bipolar disorder; GABA deficiency in PFC is associated with bipolar depression; benzodiazepines provide acute antimanic sedation via GABA-A agonism."
  - target: 01-human/07-system/autism-spectrum-disorder
    relation: connects-to
    note: "Reduced GABAergic inhibition contributes to cortical E/I imbalance in ASD; GABA-A subunit mutations (GABRA1, GABRB3) are associated with ASD; PV interneuron deficits in ASD cortex reduce inhibitory tone and contribute to sensory hypersensitivity."
  - target: 01-human/07-system/obsessive-compulsive-disorder
    relation: connects-to
    note: "Reduced GABAergic inhibitory tone in OFC and striatum (MRS studies) contributes to CSTC hyperactivity in OCD; benzodiazepines provide acute relief but don't modify OCD; D-cycloserine (NMDA partial agonist) augments ERP via enhanced NMDA-dependent fear extinction learning."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "Reduced GABA in amygdala, hippocampus, and PFC (MRS studies) allows excitatory anxiety circuits to dominate in GAD; benzodiazepines provide rapid relief via GABA-A allosteric potentiation but risk dependence; pregabalin reduces glutamate/GABA imbalance via α2δ VGCC blockade."
  - target: 01-human/07-system/panic-disorder
    relation: connects-to
    note: "GABA-A activation by benzodiazepines (clonazepam, alprazolam) rapidly terminates panic attacks; reduced BZ binding in temporal lobe in PD suggests GABAergic deficit; BZDs bridge therapy while SSRIs take effect but avoided long-term due to dependence and impaired extinction."
  - target: 01-human/07-system/social-anxiety-disorder
    relation: connects-to
    note: "Benzodiazepines (clonazepam) are effective for SAD but dependency concerns limit use; GABAergic deficits in limbic circuits may impair amygdala threat dampening in social situations; pregabalin and gabapentin show evidence for SAD as alternative GABAergic treatments."
  - target: 01-human/07-system/alcohol-use-disorder
    relation: connects-to
    note: "Alcohol potentiates GABA-A → sedation and tolerance; chronic use → GABA-A downregulation; abrupt cessation → GABA-A insufficiency → withdrawal seizures (6-48h) and delirium tremens (24-72h); GABRA2 (α2 subunit) polymorphisms are the strongest GWAS hit for AUD."
  - target: 01-human/07-system/opioid-use-disorder
    relation: connects-to
    note: "μ-opioid receptors on VTA GABAergic interneurons mediate euphoric disinhibition; chronic opioid → tolerance at MOR on GABA interneurons; buprenorphine (partial MOR agonist) provides stable DA tone without the high-reinforcement surge of full agonist opioids."
  - target: 01-human/07-system/insomnia-disorder
    relation: connects-to
    note: "Z-drugs (zolpidem, zaleplon, eszopiclone) and benzodiazepines are GABA-A positive allosteric modulators highly effective for insomnia but carry tolerance, rebound insomnia, and dependency risks; CBT-I is preferred because it normalizes sleep without GABA-A pharmacology."
  - target: 01-human/03-molecular/orexin
    relation: connects-to
    note: "VLPO GABAergic neurons inhibit orexin neurons during sleep; mutual inhibition between VLPO and arousal centers (including orexin) creates a bistable sleep-wake flip-flop switch; DORAs block orexin without GABA-A modulation — avoiding tolerance and dependence."
  - target: 01-human/03-molecular/mu-opioid-receptor
    relation: connects-to
    note: "MOR expressed on VTA and PAG GABAergic interneurons; Gi activation → hyperpolarizes GABA interneurons → disinhibition of DA neurons (VTA reward) and PAG output neurons (analgesia); buprenorphine (partial MOR agonist) maintains stable GABA-mediated inhibitory tone."
---

# GABA

## Overview

γ-Aminobutyric acid (GABA) is the **principal inhibitory neurotransmitter of the mammalian brain**, acting as the primary brake on neuronal excitability. If glutamate is the accelerator of neural circuits, GABA is the brake — and the proper ratio between them, the **excitation–inhibition (E/I) balance**, is the fundamental homeostatic parameter that keeps neural networks in a functional operating range. Disruption of E/I balance toward excess excitation underlies epilepsy; disruption toward excess inhibition can impair cognition and wakefulness.

GABAergic interneurons — typically local-circuit neurons that do not project to distant brain regions — make up approximately **20–30% of cortical neurons** but control the timing, synchrony, and gain of the much larger population of glutamatergic principal neurons. By shaping the temporal windows in which neurons can fire, GABA-expressing parvalbumin and somatostatin interneurons generate the **gamma oscillations** (30–80 Hz) that are thought to coordinate information processing across cortical networks.

Pharmacologically, GABA receptors are among the **most important drug targets in medicine**, underpinning the actions of benzodiazepines (anxiolytics, anticonvulsants), barbiturates, general anesthetics (propofol, etomidate), alcohol, Z-drugs (zolpidem), and the antiepileptic drug class [^olsen-sieghart-2008].

## Structure

### Chemical identity

GABA is a **four-carbon amino acid** that is **not incorporated into proteins** — it is found only as a free molecule in neurons and other tissues. Molecular formula: C₄H₉NO₂; MW 103.12 g/mol. Unlike glutamate, GABA is a non-standard amino acid (not α-amino): its amino group is on the γ-carbon. It is neutral at physiological pH.

### Biosynthesis

GABA is synthesized in the cytosol of GABAergic neurons in a single step from glutamate:

| Step | Enzyme | Cofactor | Substrate → Product |
|:---|:---|:---|:---|
| 1 | **Glutamic acid decarboxylase (GAD)** isoforms GAD65 and GAD67 | Pyridoxal phosphate (B6, vitamin B6) | L-Glutamate → **GABA** + CO₂ |

Two isoforms serve distinct roles:
- **GAD67** — cytoplasmic, constitutively active, generates the bulk GABA pool for tonic inhibition
- **GAD65** — associates with vesicle membranes, inducible, generates GABA for phasic (activity-driven) release

**Vitamin B6 deficiency** (pyridoxine deficiency) impairs both isoforms and is a recognized cause of neonatal seizures — a direct demonstration that GABA synthesis is essential for seizure suppression.

After release, GABA is cleared from the synapse by high-affinity **GABA transporters GAT-1, GAT-2, GAT-3** (SLC6A1, 13, 11) on neurons and astrocytes. In astrocytes, GABA is catabolized by **GABA transaminase (GABA-T)** → succinic semialdehyde → succinate (enters TCA cycle). Vigabatrin (antiepileptic) irreversibly inhibits GABA-T, raising extracellular GABA.

### Receptors

GABA acts on two fundamentally distinct receptor types [^olsen-sieghart-2008][^bowery-smart-2006]:

#### GABA-A receptors (ionotropic)

**Chloride-permeable ligand-gated ion channels** — the primary mediators of fast (<1 ms) inhibitory postsynaptic potentials (IPSPs).

- **Structure:** Heteropentamers from a family of 19 subunits (α1–6, β1–3, γ1–3, δ, ε, θ, π, ρ1–3). The dominant synaptic configuration is **2α + 2β + 1γ** (e.g., α1β2γ2).
- **Function:** GABA binding opens a central Cl⁻ channel. In adult neurons, intracellular Cl⁻ is low (maintained by KCC2 transporter), so Cl⁻ flows inward → **hyperpolarization** and inhibition. (Note: in neonatal neurons, intracellular Cl⁻ is high due to immature KCC2 → GABA is paradoxically depolarizing.)
- **Allosteric modulation sites** [^sieghart-2015-gaba-subunits]:

| Site | Modulator class | Effect |
|:---|:---|:---|
| **Benzodiazepine site** (α-γ interface) | Benzodiazepines (diazepam, lorazepam) | Positive allosteric modulator: ↑ frequency of channel opening |
| **Barbiturate site** (β subunit TM2/3) | Barbiturates (phenobarbital), propofol | Positive allosteric modulator: ↑ duration of channel opening; at high doses, direct channel activation |
| **Neurosteroid site** (δ/γ2-containing) | Allopregnanolone, brexanolone | Positive allosteric modulation of extrasynaptic receptors → tonic inhibition |
| **Alcohol / general anesthetic site** | Ethanol, isoflurane, ketamine | Various modulation |
| **Picrotoxin site** (channel pore) | Picrotoxin | Channel blocker; used as experimental GABA-A antagonist and convulsant |

#### GABA-B receptors (metabotropic)

**Gαi/o-coupled GPCRs** mediating slow (100s of ms) inhibition [^bowery-smart-2006].

- **Structure:** Obligate heterodimer of **GABA-B1 + GABA-B2** subunits; GABA binds to GABA-B1, GABA-B2 couples to G protein.
- **Presynaptic function:** Inhibit voltage-gated Ca²⁺ channels → reduced neurotransmitter release (autoreceptors on GABAergic terminals; heteroreceptors on glutamatergic terminals).
- **Postsynaptic function:** Activate **GIRK (G-protein-regulated inwardly rectifying K⁺) channels** → membrane hyperpolarization. Also inhibit adenylyl cyclase → ↓cAMP.
- **Baclofen** — GABA-B agonist; used for spasticity, alcohol withdrawal, treatment-resistant depression.

## Function

### Fast synaptic inhibition (GABA-A)

At inhibitory synapses (predominantly axosomatic and axo-axonic locations), an arriving action potential releases GABA from presynaptic vesicles. GABA binds postsynaptic GABA-A receptors, opening Cl⁻ channels within milliseconds. The resulting **inhibitory postsynaptic potential (IPSP)** reduces the probability that the postsynaptic neuron will fire in response to concurrent excitatory input.

**Axo-axonic synapses** (from chandelier cells onto the axon initial segment of pyramidal neurons) are particularly powerful — they control the final output site of principal neurons.

### Tonic inhibition (extrasynaptic GABA-A)

In addition to phasic, synapse-specific inhibition, **extrasynaptic GABA-A receptors** (often δ-containing) sense ambient extracellular GABA levels and generate a **tonic conductance** — a persistent Cl⁻ leak that sets the overall excitability of the neuron. Tonic inhibition is particularly important in the dentate gyrus, thalamus, and cerebellum. It is the target of neurosteroids, alcohol, and low-dose anesthetics.

### E/I balance and network function

The ratio of excitatory to inhibitory drive determines the **dynamic range** of cortical circuits. Optimally balanced networks can:
- Process information across a wide range of input intensities
- Generate oscillatory rhythms (alpha, beta, gamma) used for communication within and between brain regions
- Suppress noise while amplifying signal

When E/I balance shifts toward excess excitation (loss of GABAergic interneurons, GABA-A dysfunction, or excess glutamate), the result is **epilepsy** — synchronized, self-reinforcing electrical activity spreading across neural circuits.

## Mechanism

### GABA-A gating cycle

1. Two GABA molecules must bind simultaneously (to the two α/β interfaces per pentamer) to efficiently open the channel.
2. Binding causes a concerted conformational change: the five TM2 helices lining the channel pore rotate, opening the gate.
3. With continued GABA present, the channel **desensitizes** (pore closes despite ligand still bound) — a self-limiting mechanism.
4. Benzodiazepines shift the GABA concentration–response curve leftward (increase apparent affinity), increasing the frequency of channel opening without affecting peak conductance or desensitization rate.

### GABA-B slow inhibitory cycle

1. GABA binds the Venus flytrap domain of GABA-B1.
2. Conformational change in the heterodimer activates Gαi/o.
3. Gαi/o-GTP: inhibits adenylyl cyclase (↓PKA pathway) and directly activates GIRK channels (via Gβγ).
4. GIRK K⁺ efflux hyperpolarizes the membrane (postsynaptic effect, onset ~50–200 ms, duration ~300–1000 ms).
5. Presynaptically, Gβγ binds P/Q-type and N-type Ca²⁺ channels → reduced Ca²⁺ entry → reduced vesicle release.

## Connections

- `expressed-by` → **[neuron](../../04-cellular/neuron/README.md)** — synthesized by GABAergic interneurons throughout the CNS
- `modulates` → **[synapse](../../05-tissue/synapse/README.md)** — mediates fast (GABA-A) and slow (GABA-B) inhibitory synaptic transmission
- `modulates` → **[brain](../../06-organ/brain/README.md)** — governs E/I balance, oscillatory rhythms, and circuit stability across all brain regions
- `part-of` → **[nervous-system](../../07-system/nervous-system/README.md)** — the dominant inhibitory neurotransmitter system
- `connects-to` → **[Epilepsy](../../07-system/epilepsy/README.md)** — Loss of GABAergic inhibitory tone — via SCN1A LOF, GABA-A subunit mutations, or interneuron loss — causes epilepsy; GABA-A potentiators (benzodiazepines, clobazam) and GABA-T inhibitors (valproate, vigabatrin) are the most widely used antiepileptic drug classes.
- `connects-to` → **[SCN1A](../scn1a/README.md)** — Nav1.1 (SCN1A) is the dominant sodium channel in PV+ GABAergic interneurons; SCN1A haploinsufficiency silences these interneurons → reduced GABA release → cortical disinhibition; clobazam (GABA-A modulator) and valproate (GABA-T inhibitor) are mainstay Dravet treatments.
- `connects-to` → **[Schizophrenia](../../07-system/schizophrenia/README.md)** — parvalbumin interneuron hypofunction in PFC — reduced GAD67, impaired GABA synthesis — causes deficient gamma oscillations underlying working memory deficits; GABAergic interneuron loss may be primary, upstream of dopamine and glutamate dysregulation in schizophrenia.
- `connects-to` → **[Bipolar Disorder](../../07-system/bipolar-disorder/README.md)** — valproate potentiates GABA-A function and blocks voltage-gated Na⁺/Ca²⁺ channels in bipolar disorder; GABA deficiency in PFC is associated with bipolar depression; benzodiazepines provide acute antimanic sedation via GABA-A agonism.
- `connects-to` → **[Autism Spectrum Disorder](../../07-system/autism-spectrum-disorder/README.md)** — reduced GABAergic inhibition contributes to cortical E/I imbalance in ASD; GABA-A subunit mutations (GABRA1, GABRB3) are associated with ASD; PV interneuron deficits in ASD cortex reduce inhibitory tone and contribute to sensory hypersensitivity.
- `connects-to` → **[Obsessive-Compulsive Disorder](../../07-system/obsessive-compulsive-disorder/README.md)** — reduced GABAergic inhibitory tone in OFC and striatum (MRS studies) contributes to CSTC circuit hyperactivity in OCD; benzodiazepines provide acute relief but don't modify disease course; D-cycloserine augments ERP via enhanced NMDA-dependent fear extinction learning.
- `connects-to` → **[Generalized Anxiety Disorder](../../07-system/generalized-anxiety-disorder/README.md)** — reduced GABA in amygdala, hippocampus, and PFC (MRS studies) allows excitatory anxiety circuits to dominate in GAD; benzodiazepines provide rapid symptom relief via GABA-A allosteric potentiation; pregabalin reduces glutamate/substance P release via α2δ VGCC blockade.
- `connects-to` → **[Panic Disorder](../../07-system/panic-disorder/README.md)** — GABA-A activation by benzodiazepines (clonazepam, alprazolam) rapidly terminates panic attacks; reduced BZ binding in temporal lobe in PD suggests a GABAergic deficit; BZDs bridge therapy while SSRIs take effect but avoided long-term due to dependence and impaired fear extinction.
- `connects-to` → **[Social Anxiety Disorder](../../07-system/social-anxiety-disorder/README.md)** — benzodiazepines (clonazepam) are effective for SAD but dependency concerns limit use; GABAergic deficits in limbic circuits may impair amygdala threat dampening in social situations; pregabalin and gabapentin show evidence for SAD as GABAergic alternatives.
- `connects-to` → **[Alcohol Use Disorder](../../07-system/alcohol-use-disorder/README.md)** — alcohol potentiates GABA-A → sedation and tolerance; chronic use → GABA-A downregulation → tolerance; abrupt cessation → GABA-A insufficiency → withdrawal seizures (6–48h) and delirium tremens; GABRA2 polymorphisms are the strongest GWAS association with AUD.
- `connects-to` → **[Opioid Use Disorder](../../07-system/opioid-use-disorder/README.md)** — μ-opioid receptors on VTA GABAergic interneurons mediate euphoric disinhibition; chronic opioid → tolerance at MOR on GABA interneurons; buprenorphine (partial MOR agonist) provides stable DA tone without high-reinforcement surge of full agonist opioids.
- `connects-to` → **[Insomnia Disorder](../../07-system/insomnia-disorder/README.md)** — Z-drugs (zolpidem, zaleplon, eszopiclone) and benzodiazepines enhance GABA-A function and are highly effective for insomnia but carry tolerance, rebound insomnia, and dependency risks; CBT-I normalizes sleep without pharmacological GABA-A modulation.
- `connects-to` → **[Orexin](../orexin/README.md)** — VLPO GABAergic neurons inhibit orexin neurons during sleep; mutual inhibition between VLPO and arousal centers (including orexin) creates a bistable sleep-wake flip-flop switch; DORAs block orexin without GABA-A modulation — avoiding tolerance and dependence.
- `connects-to` → **[Mu-Opioid Receptor](../mu-opioid-receptor/README.md)** — MOR expressed on VTA and PAG GABAergic interneurons; Gi activation → hyperpolarizes GABA interneurons → disinhibition of DA neurons (VTA reward) and PAG output neurons (descending analgesia); buprenorphine (partial MOR agonist) maintains stable GABA-mediated inhibitory tone.

## Pathology

| Disease | Mechanism | Therapeutic implication |
|:---|:---|:---|
| **Epilepsy** | Loss of GABAergic interneurons or GABA-A mutations → E/I shift toward hyperexcitability | Benzodiazepines, barbiturates, valproate, vigabatrin, GABA-A agonists |
| **Anxiety disorders** | Reduced GABA-A tone in amygdala, PFC; stress-driven interneuron hypofunction | Benzodiazepines (acute); SSRIs, GABAergic modulators (chronic) |
| **Insomnia** | Reduced GABAergic sleep-promoting tone | Z-drugs (zolpidem — α1-GABA-A selective), benzodiazepines |
| **Schizophrenia** | Parvalbumin interneuron hypofunction → loss of gamma synchrony; reduced GAD67 in PFC | GABAergic targets under investigation |
| **Post-partum depression** | Withdrawal of allopregnanolone (endogenous GABA-A neurosteroid) postpartum | Brexanolone (synthetic allopregnanolone) — FDA-approved |
| **Neonatal seizures** | Immature KCC2 → GABA is depolarizing → GABA-A activation is pro-convulsant | Phenobarbital (first line); bumetanide (KCC2-forcing) experimental |
| **Alcohol use disorder** | Chronic alcohol potentiates GABA-A → homeostatic downregulation → withdrawal seizures when alcohol removed | Benzodiazepines for detox; GABA-B agonists (baclofen) for craving |

[^olsen-sieghart-2008]: Olsen RW, Sieghart W. International Union of Pharmacology. LXX. Subtypes of gamma-aminobutyric acid(A) receptors. *Pharmacol Rev.* 2008;60(3):243-260. [doi:10.1124/pr.108.00505](https://doi.org/10.1124/pr.108.00505) · [PubMed 18790874](https://pubmed.ncbi.nlm.nih.gov/18790874/)
[^purves-neuroscience]: Purves D, Augustine GJ, Fitzpatrick D, et al. *Neuroscience.* 6th ed. Sinauer Associates; 2018. [ncbi.nlm.nih.gov/books/NBK10792/](https://www.ncbi.nlm.nih.gov/books/NBK10792/)
[^bowery-smart-2006]: Bowery NG, Smart TG. GABA and glycine as neurotransmitters: a brief history. *Br J Pharmacol.* 2006;147(Suppl 1):S109-S119. [doi:10.1038/sj.bjp.0706443](https://doi.org/10.1038/sj.bjp.0706443) · [PubMed 16402094](https://pubmed.ncbi.nlm.nih.gov/16402094/)
[^sieghart-2015-gaba-subunits]: Sieghart W. Allosteric modulation of GABAA receptors via multiple drug-binding sites. *Adv Pharmacol.* 2015;72:53-96. [doi:10.1016/bs.apha.2014.10.002](https://doi.org/10.1016/bs.apha.2014.10.002) · [PubMed 25600566](https://pubmed.ncbi.nlm.nih.gov/25600566/)
