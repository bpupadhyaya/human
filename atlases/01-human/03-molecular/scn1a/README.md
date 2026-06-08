---
schema: human-scale-entry/v1
id: scn1a
name: SCN1A
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-08
summary: "SCN1A encodes Nav1.1 (voltage-gated sodium channel, GABAergic interneurons); loss-of-function causes Dravet syndrome with fever-sensitive tonic-clonic and myoclonic seizures; sodium channel blockers worsen Dravet; fenfluramine and cannabidiol are FDA-approved for Dravet."
aliases: ["SCN1A", "Nav1.1", "PARK1", "Dravet syndrome gene", "SMEI gene", "GEFS+ gene", "sodium channel Nav1.1", "voltage-gated sodium channel type I alpha", "SCN1A Dravet", "SUDEP risk gene"]
sources:
  - id: claes-2001-scn1a-dravet
    type: peer-reviewed
    cite: "Claes L, Del-Favero J, Ceulemans B, Lagae L, Van Broeckhoven C, De Jonghe P. De novo mutations in the sodium-channel gene SCN1A cause severe myoclonic epilepsy of infancy. Am J Hum Genet. 2001;68(6):1327-1332."
    doi: "10.1086/320609"
    pmid: "11359211"
    url: "https://doi.org/10.1086/320609"
    accessed: "2026-06-08"
  - id: ogiwara-2007-nav1-interneuron
    type: peer-reviewed
    cite: "Ogiwara I, Miyamoto H, Morita N, et al. Nav1.1 localizes to axons of parvalbumin-positive inhibitory interneurons: a circuit basis for epileptic seizures in mice carrying an Scn1a gene mutation. J Neurosci. 2007;27(22):5903-5914."
    doi: "10.1523/JNEUROSCI.5270-06.2007"
    pmid: "17537961"
    url: "https://doi.org/10.1523/JNEUROSCI.5270-06.2007"
    accessed: "2026-06-08"
  - id: wirrell-2022-dravet-treatment
    type: peer-reviewed
    cite: "Wirrell EC, Hood V, Knupp KG, et al. International consensus on diagnosis and management of Dravet syndrome. Epilepsia. 2022;63(7):1761-1777."
    doi: "10.1111/epi.17274"
    pmid: "35522095"
    url: "https://doi.org/10.1111/epi.17274"
    accessed: "2026-06-08"
cross_links:
  - target: 01-human/07-system/epilepsy
    relation: connects-to
    note: "SCN1A loss-of-function mutations cause Dravet syndrome (~80% of cases; Nav1.1 haploinsufficiency in GABAergic interneurons → impaired inhibition → fever-sensitive tonic-clonic and myoclonic seizures); SCN1A gain-of-function → GEFS+; sodium channel blockers worsen Dravet."
  - target: 01-human/03-molecular/gaba
    relation: connects-to
    note: "Nav1.1 (SCN1A) primarily sustains GABAergic interneuron firing; SCN1A haploinsufficiency → interneuron silencing → reduced GABA release → cortical disinhibition → seizures; clobazam (GABA-A enhancer) and valproate (GABA transaminase inhibitor) are mainstay Dravet treatments."
  - target: 01-human/07-system/parkinsons-disease
    relation: connects-to
    note: "Nav1.1 is expressed in dopaminergic neurons of the substantia nigra in addition to GABAergic interneurons; SCN1A gain-of-function mutations impair nigrostriatal dopaminergic signaling in animal models; SCN1A variants have been identified in PD GWAS with borderline significance."
---

# SCN1A

## Overview

**SCN1A** encodes **Nav1.1** (sodium voltage-gated channel alpha subunit 1) — the predominant voltage-gated sodium channel (VGSC) in the axon initial segments of **GABAergic inhibitory interneurons** throughout the cortex, hippocampus, brainstem, and cerebellum. Nav1.1 is responsible for the rapid inward sodium current that initiates and propagates action potentials in these interneurons, making it essential for sustaining the high-frequency firing required to maintain cortical inhibitory tone.

SCN1A was identified as a major epilepsy gene in 2001 when Claes et al. demonstrated that de novo heterozygous loss-of-function (LOF) mutations cause **Dravet syndrome** (SMEI, severe myoclonic epilepsy of infancy) [^claes-2001-scn1a-dravet] — one of the most severe and pharmacologically challenging genetic epilepsies. The critical mechanistic insight came from Ogiwara et al. in 2007 [^ogiwara-2007-nav1-interneuron], showing that Nav1.1 is specifically concentrated on the axon initial segments of **parvalbumin-positive (PV+) fast-spiking inhibitory interneurons** — explaining why SCN1A LOF leads to network disinhibition and seizures rather than reduced excitability.

SCN1A is now the most clinically significant single-gene epilepsy locus, accounting for:
- **~80% of Dravet syndrome** (de novo heterozygous LOF/truncation mutations)
- **Generalized epilepsy with febrile seizures plus (GEFS+)** — autosomal dominant, gain-of-function or partial LOF missense mutations; milder phenotype
- **Borderline SMEI (SMEB)** — intermediate severity
- Rare cases of **familial hemiplegic migraine type 3 (FHM3)** — gain-of-function SCN1A mutations

## Structure

### Protein architecture

Nav1.1 is a large (1998 aa; ~220 kDa) transmembrane protein with one alpha subunit (Nav1.1/SCN1A) and two auxiliary beta subunits (SCN1B, SCN2B):

**Four homologous domains (I–IV)** each containing:
- **6 transmembrane segments (S1–S6)**
- **S1–S4**: Voltage sensor module; S4 contains positively charged arginine residues that move outward upon membrane depolarization → channel gating
- **S5–S6 pore loop**: Forms the ion-conducting pore; selectivity filter (DEKA motif in Nav channels) provides Na+ selectivity ~12× over K+
- **Inactivation particle**: Hydrophobic IFM (Ile-Phe-Met) motif in the III-IV linker → fast inactivation within milliseconds of opening

**Functional states:**
1. **Resting (closed)**: Voltage sensors in inward position; pore closed; available for activation
2. **Open**: S4 segments activated by depolarization → pore opens → Na+ influx → action potential upstroke
3. **Fast-inactivated**: IFM particle blocks pore within 1–2 ms; Na+ current ceases; must recover during repolarization
4. **Slow-inactivated**: Second inactivation state from prolonged depolarization; important for Nav channel-modulating AED mechanisms

**Beta subunits:** SCN1B (β1) — non-covalently associated; modulates Nav1.1 inactivation kinetics and membrane trafficking; SCN1B LOF mutations themselves cause GEFS+ and Dravet-like phenotypes.

### Cellular distribution

Nav1.1 is the predominant sodium channel in:
- **Parvalbumin-positive (PV+) fast-spiking interneurons** (basket cells, chandelier cells in cortex and hippocampus) — axon initial segment expression; required for high-frequency (200-500 Hz) burst firing that provides perisomatic inhibition of pyramidal neurons
- **Somatostatin-positive (SST+) interneurons** — dendritic-targeting inhibitory neurons
- **Purkinje cells** (cerebellum) — explains cerebellar dysfunction and ataxia in Dravet syndrome
- **Dorsal root ganglia neurons** — explains the pain sensitivity and temperature sensitivity in Dravet
- **Brainstem neurons** — locus coeruleus, raphe; explains autonomic dysfunction in Dravet

In contrast, **Nav1.2 (SCN2A)** and **Nav1.6 (SCN8A)** predominate in excitatory (glutamatergic) pyramidal neurons.

## Function

### Physiological role in inhibitory interneurons

PV+ interneurons are the principal source of **perisomatic feed-forward inhibition** in the cortex, generating the inhibitory post-synaptic potentials (IPSPs) that:
- Limit pyramidal neuron excitation and spike timing
- Generate cortical gamma oscillations (30–80 Hz) that underlie cognitive function
- Participate in theta-gamma coupling in hippocampus (spatial navigation and memory encoding)

Nav1.1 enables PV+ interneurons to fire at frequencies >200 Hz without failure — the defining property of fast-spiking interneurons. When Nav1.1 is haploinsufficient, PV+ interneurons cannot sustain high-frequency firing → **interneuron adaptation/silencing** under repetitive stimulation → cortical disinhibition → epileptiform discharges.

### Dravet syndrome seizure mechanism [^ogiwara-2007-nav1-interneuron]

**Temperature sensitivity (fever-triggered seizures):**
- Nav1.1 LOF increases temperature sensitivity of interneuron firing: at 37°C PV+ interneurons fire normally, but at 38–40°C (febrile range) Nav1.1 LOF interneurons fail catastrophically → acute cortical disinhibition → febrile seizure
- This explains the cardinal Dravet feature of fever-triggered status epilepticus (average onset 6 months, often prolonged, requiring emergency treatment)

**SUDEP risk (sudden unexpected death in epilepsy):**
- Nav1.1 in brainstem respiratory neurons (Kölliker-Fuse nucleus, pre-Bötzinger complex) — SCN1A LOF → impaired respiratory control → postictal apnea → SUDEP
- SCN1A Dravet has the highest SUDEP risk of any epilepsy syndrome (~15% lifetime risk)

## Mechanism

### SCN1A mutation spectrum

| Mutation type | Effect on Nav1.1 | Syndrome | Severity |
|:---|:---|:---|:---|
| Truncation (stop, frameshift, splice) | Complete LOF one allele; haploinsufficiency | Dravet syndrome | Severe |
| Missense — critical residue | Severe LOF (trafficking failure or channel non-function) | Dravet syndrome | Severe |
| Missense — moderate | Partial LOF; altered gating kinetics | SMEB (borderline SMEI) | Moderate |
| Missense — gain-of-function | Prolonged opening or impaired inactivation | GEFS+; FHM3 | Mild-moderate |
| Whole gene deletion | LOF | Dravet; developmental encephalopathy | Severe |
| De novo duplication | Overexpression? | Rare; context-dependent | Variable |

~85% of Dravet-causing mutations are de novo (not inherited); ~15% are inherited from an affected parent with GEFS+.

### Drug sensitivity and contraindication

**Contraindicated drugs in SCN1A LOF (Dravet syndrome):**
- **Sodium channel blockers** (carbamazepine, oxcarbazepine, phenytoin, lamotrigine): Further reduce Nav1.1 activity in GABAergic interneurons → paradoxically worsen seizure frequency (clinical observation: lamotrigine worsens Dravet in 80% of patients)
- **Vigabatrin**: Contraindicated (mechanism unclear; possibly via altering GABAergic balance)

**Effective treatments (Wirrell 2022 consensus):**
- **Valproate**: First-line; broad-spectrum sodium channel modulator (less specific than carbamazepine) + GABA-transaminase inhibitor → increases GABA levels; reduces Dravet seizures in ~60%
- **Clobazam**: 1,5-benzodiazepine; positive allosteric modulator of GABA-A receptor; FDA-approved adjunct for Dravet (CONTAIN trial: 49% responder rate)
- **Stiripentol**: Inhibits CYP enzymes (increases clobazam levels) + direct GABA-A modulation; approved in EU and US as adjunct to valproate/clobazam in Dravet
- **Fenfluramine**: Serotonin (5-HT) releaser; FDA/EMA approved for Dravet (2020) via activation of serotonergic modulatory circuits; 54% responder rate in Phase 3; reduces SUDEP risk (serotonin stimulates respiration)
- **Cannabidiol (Epidiolex)**: Plant-derived CBD; mechanism in Dravet unclear (GPR55 antagonism? Na channel modulation?); FDA-approved for Dravet ≥2 years (GWPCARE trials: 39% responder rate)
- **Quinidine**: Experimental; open sodium channels (gain-of-function in SCN1A → GEFS+ overlap variant); not for LOF Dravet
- **Gene therapy approaches**: ASO (antisense oligonucleotide) to increase Nav1.1 expression from the intact allele; AAV-SCN1A delivery; in preclinical/early Phase 1

### Precision medicine: genotype-guided treatment

SCN1A genotype directly guides epilepsy management:
1. **Truncating/LOF mutations**: Avoid all sodium channel blockers; start valproate + clobazam; add fenfluramine or CBD when breakthrough seizures occur; discuss SUDEP counseling and seizure response plan
2. **Gain-of-function mutations (GEFS+)**: Sodium channel blockers may be beneficial; trial of carbamazepine or lamotrigine is appropriate
3. **Missense of unclear pathogenicity**: Functional studies or Nav1.1 gating analysis required; empirical treatment avoidance of SCN blockers until functional data available

## Connections

**→ [Epilepsy](../../07-system/epilepsy/)**: SCN1A loss-of-function mutations cause Dravet syndrome (~80% of cases) via Nav1.1 haploinsufficiency in GABAergic interneurons → impaired high-frequency inhibitory interneuron firing → cortical disinhibition → fever-sensitive tonic-clonic and myoclonic seizures; SCN1A gain-of-function causes milder GEFS+; sodium channel blockers worsen Dravet.

**→ [GABA](../gaba/)**: Nav1.1 (SCN1A) primarily sustains GABAergic interneuron action potential firing; SCN1A haploinsufficiency → interneuron silencing → reduced GABA release → cortical disinhibition → seizures; clobazam (GABA-A modulator) and valproate (GABA-T inhibitor) are mainstay Dravet treatments because they compensate for lost GABAergic inhibitory tone.

[^claes-2001-scn1a-dravet]: Claes L, Del-Favero J, Ceulemans B, Lagae L, Van Broeckhoven C, De Jonghe P. De novo mutations in the sodium-channel gene SCN1A cause severe myoclonic epilepsy of infancy. *Am J Hum Genet.* 2001;68(6):1327-1332. [doi:10.1086/320609](https://doi.org/10.1086/320609) · [PubMed 11359211](https://pubmed.ncbi.nlm.nih.gov/11359211/)
[^ogiwara-2007-nav1-interneuron]: Ogiwara I, Miyamoto H, Morita N, et al. Nav1.1 localizes to axons of parvalbumin-positive inhibitory interneurons: a circuit basis for epileptic seizures in mice carrying an Scn1a gene mutation. *J Neurosci.* 2007;27(22):5903-5914. [doi:10.1523/JNEUROSCI.5270-06.2007](https://doi.org/10.1523/JNEUROSCI.5270-06.2007) · [PubMed 17537961](https://pubmed.ncbi.nlm.nih.gov/17537961/)
[^wirrell-2022-dravet-treatment]: Wirrell EC, Hood V, Knupp KG, et al. International consensus on diagnosis and management of Dravet syndrome. *Epilepsia.* 2022;63(7):1761-1777. [doi:10.1111/epi.17274](https://doi.org/10.1111/epi.17274) · [PubMed 35522095](https://pubmed.ncbi.nlm.nih.gov/35522095/)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
