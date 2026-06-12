---
schema: human-scale-entry/v1
id: huntingtons-disease
name: Huntington Disease
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-07
summary: "Huntington disease is caused by HTT CAG repeat expansion (≥36 copies); autosomal dominant; choreoathetosis, cognitive decline, and psychiatric disturbance onset in the 4th-5th decade; disease-modifying HTT-lowering therapies (ASOs, siRNA) are in Phase 3 clinical trials."
aliases: ["Huntington disease", "HD", "Huntington's disease", "HTT CAG expansion", "huntingtin disease", "chorea HD", "polyQ neurodegeneration", "HD neurodegeneration", "CAG repeat disease", "HTT repeat expansion"]
cross_links:
  - target: 01-human/03-molecular/htt
    relation: connects-to
    note: "HTT CAG repeat ≥36 → polyglutamine mHTT aggregation → impaired proteostasis, mitochondrial dysfunction, and transcriptional dysregulation in striatal MSNs; caudate/putamen atrophy is the hallmark; juvenile HD (>60 CAG) presents with rigidity and seizures rather than chorea."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Mutant huntingtin (mHTT) sequesters p62/SQSTM1 and impairs autophagosome formation → defective selective autophagy → mHTT aggregate accumulation → neuronal proteotoxicity; mTOR inhibitors (rapamycin) and autophagy enhancers reduce mHTT burden in HD mouse models."
  - target: 01-human/03-molecular/dopamine
    relation: connects-to
    note: "mHTT causes preferential degeneration of striatal MSNs expressing D1 and D2 dopamine receptors; early loss of indirect pathway MSNs (D2) → dopamine pathway imbalance → chorea; tetrabenazine (VMAT2 inhibitor) depletes presynaptic dopamine → suppresses choreiform movements."
  - target: 01-human/03-molecular/caspase-3
    relation: connects-to
    note: "mHTT aggregates activate caspase-3 and caspase-9 in striatal MSNs via mitochondrial pathway; mHTT N-terminal fragments (calpain-cleaved) amplify caspase activation; caspase-3 inhibition with z-DEVD-fmk is neuroprotective in HD mouse models, supporting apoptosis as a driver."
  - target: 01-human/03-molecular/bdnf
    relation: connects-to
    note: "mHTT disrupts HTT's cytoplasmic REST/NRSF sequestration → nuclear REST represses BDNF transcription; mHTT also impairs HAP1-mediated BDNF vesicle transport from cortex to striatum → MSN trophic deprivation; BDNF/TrkB restoration is a key HD therapeutic goal."
  - target: 01-human/03-molecular/glutamate
    relation: connects-to
    note: "Striatal MSNs receive massive glutamatergic input from cortex; mHTT sensitizes MSNs to NMDA receptor excitotoxicity via NR2B (GluN2B) dysregulation; riluzole and memantine reduce excitotoxic MSN death in HD models; E/I imbalance contributes to early HD cognitive symptoms."
  - target: 01-human/06-organ/brain
    relation: targets
    note: "HD selectively atrophies striatum (caudate + putamen) detectable by MRI 15+ years pre-onset; cortical layer V and thalamic neurons also degenerate; lateral ventricle enlargement mirrors striatal volume loss and tracks disease progression by UHDRS total functional capacity."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "Huntington's disease kills a specific neuron: the GABAergic medium spiny neurons of the striatum, especially indirect-pathway (D2) MSNs whose loss disinhibits movement and causes chorea; mutant huntingtin starves them of BDNF and sensitizes them to glutamate excitotoxicity."
  - target: 01-human/04-cellular/microglia
    relation: connects-to
    note: "Neuroinflammation is an early feature of Huntington's disease: microglia activate in the striatum and cortex years before symptoms (on PET), and mutant huntingtin acts cell-autonomously inside microglia to make them hyper-reactive — adding inflammation to the neurodegeneration."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "Huntington's disease is an autosomal-dominant neurodegenerative disease of the CNS: a CAG-repeat expansion in HTT makes a toxic polyglutamine protein that destroys the striatum and cortex, causing chorea, cognitive decline, and psychiatric disturbance over 15-20 years."
sources:
  - id: gusella-1983-htt-locus
    type: peer-reviewed
    cite: "Gusella JF, Wexler NS, Conneally PM, et al. A polymorphic DNA marker genetically linked to Huntington's disease. Nature. 1983;306(5940):234-238."
    doi: "10.1038/306234a0"
    pmid: "6316146"
    url: "https://doi.org/10.1038/306234a0"
  - id: macdonald-1993-htt-gene
    type: peer-reviewed
    cite: "The Huntington's Disease Collaborative Research Group. A novel gene containing a trinucleotide repeat that is expanded and unstable on Huntington's disease chromosomes. Cell. 1993;72(6):971-983."
    doi: "10.1016/0092-8674(93)90585-E"
    pmid: "8458085"
    url: "https://doi.org/10.1016/0092-8674(93)90585-E"
---

# Huntington Disease

## Overview

Huntington disease (HD) is an autosomal dominant neurodegenerative disorder caused by CAG trinucleotide repeat expansion (≥36 repeats) in exon 1 of the HTT gene on chromosome 4p16.3. Prevalence is ~5–10 per 100,000 in populations of European ancestry; lower in Asian and African populations. Repeat length is the primary determinant of age of onset: 36–39 repeats → reduced penetrance (onset often >60 years); 40–55 repeats → classic adult HD (mean onset ~40 years); >60 repeats → juvenile HD (onset <20 years). HD is uniformly progressive and fatal, with death typically 15–20 years after motor onset. No disease-modifying therapy is currently approved, but several HTT-lowering strategies are in late-phase trials.

## Structure

HD pathology centers on preferential degeneration of striatal medium spiny neurons (MSNs), which constitute ~95% of striatal neurons. The indirect pathway MSNs (D2 receptor-expressing, enkephalinergic, projecting to globus pallidus externa) are lost early, disinhibiting the subthalamic nucleus and producing hyperkinesia (chorea). Direct pathway MSNs (D1, substance P, projecting to GPi/SNr) are lost later, causing rigidity and bradykinesia in advanced disease. Cortical neurons (layer V pyramidal cells) also degenerate, contributing to cognitive and psychiatric features. Caudate and putamen atrophy is the neuroimaging hallmark; ventricular enlargement (especially lateral horns) is proportional to striatal volume loss and correlates with disease stage.

## Function

HD disrupts multiple neural circuit functions:
- **Motor control**: Cortico-striato-thalamo-cortical loops are disrupted; early indirect pathway loss → chorea; late direct pathway loss → rigidity/dystonia.
- **Cognition**: Executive dysfunction (frontal-striatal), working memory loss, and slowed processing precede motor onset by years; dementia is universal in late HD.
- **Psychiatry**: Depression (prevalence ~40%), irritability, apathy, OCD-like behaviors, and psychosis occur throughout the disease course; psychiatric symptoms often predate motor diagnosis.
- **Autonomic/systemic**: Weight loss is common (despite adequate intake) due to hypothalamic involvement and elevated metabolic rate; sleep disturbances (REM sleep behavior disorder, circadian disruption) are prominent.

## Pathology

**Genetics**: Juvenile HD (>60 CAG) presents with akinetic-rigid syndrome, seizures, and rapid progression rather than chorea. New mutations (>36 CAG de novo) arise primarily from paternal transmission of intermediate alleles (27–35 repeats); somatic instability in striatum amplifies repeat length beyond the germline count, explaining tissue-specific vulnerability.

**Neuropathology**: Intranuclear inclusions (NIIs) containing mHTT exon-1 fragments are present in neurons; paradoxically, neurons with inclusions may survive longer than inclusion-free neurons — soluble oligomeric mHTT is the primary toxic species. MSN loss follows a dorsomedial → ventrolateral gradient in caudate; putamen loss parallels caudate. Vonsattel grade 0–4 grading system (grade 0 = no visible atrophy but microscopically abnormal; grade 4 = severe global striatal loss).

**Diagnosis**: Clinical diagnosis requires motor signs + positive genetic test (≥36 CAG repeats). Predictive genetic testing is available for at-risk individuals (with mandatory pre- and post-test counseling per HDSA/EHN guidelines). Plasma neurofilament light (NfL) is an emerging biomarker: NfL rises 15+ years before expected motor onset in CAG expansion carriers and tracks disease progression.

**Treatment**:
- Chorea: Tetrabenazine (VMAT2 inhibitor, FDA 2008), deutetrabenazine (FDA 2017), valbenazine (FDA 2023) reduce chorea without altering disease course.
- Psychiatric: Standard antidepressants, antipsychotics (olanzapine, quetiapine for irritability/psychosis); avoid typical antipsychotics (worsen rigidity).
- HTT-lowering (investigational): Tominersen (intrathecal ASO targeting HTT mRNA) showed dose-dependent CSF HTT reduction but unexpected clinical worsening in the 2021 Phase 3 GENERATION HD1 trial (120 mg every 8 weeks cohort); lower-dose regimens under re-evaluation. WVE-003 (allele-selective ASO targeting SNP rs362307 on mHTT allele) and siRNA approaches (RG6042, ARB-1001) in Phase 1/2. AAV5-miHTT gene therapy (uniQure) in Phase 1/2.

## Connections

- `connects-to` → **[HTT](../../03-molecular/htt/README.md)** — HTT CAG repeat ≥36 → polyglutamine mHTT aggregation → impaired proteostasis, mitochondrial dysfunction, and transcriptional dysregulation in striatal MSNs; caudate/putamen atrophy is the hallmark; juvenile HD (>60 CAG) presents with rigidity and seizures rather than chorea.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — mutant huntingtin sequesters p62/SQSTM1 and impairs autophagosome formation → defective selective autophagy → mHTT accumulation → neuronal proteotoxicity; mTOR inhibitors and autophagy enhancers reduce mHTT burden in HD mouse models.
- `connects-to` → **[Dopamine](../../03-molecular/dopamine/README.md)** — mHTT causes preferential degeneration of striatal MSNs expressing D1 and D2 dopamine receptors; indirect pathway MSN (D2) loss → chorea; tetrabenazine (VMAT2 inhibitor) depletes presynaptic dopamine to suppress choreiform movements; approved FDA 2008.
- `connects-to` → **[Caspase-3](../../03-molecular/caspase-3/README.md)** — mHTT aggregates activate caspase-3 and caspase-9 in striatal MSNs via mitochondrial pathway; calpain-cleaved mHTT N-terminal fragments amplify caspase activation; caspase-3 inhibition is neuroprotective in HD mouse models.
- `connects-to` → **[BDNF](../../03-molecular/bdnf/README.md)** — mHTT disrupts REST/NRSF cytoplasmic sequestration → nuclear REST represses BDNF transcription; mHTT also impairs HAP1-mediated BDNF vesicle transport from cortex to striatum → MSN trophic deprivation; BDNF/TrkB signaling restoration is a key therapeutic goal.
- `connects-to` → **[Glutamate](../../03-molecular/glutamate/README.md)** — striatal MSNs receive massive glutamatergic input from cortex; mHTT sensitizes MSNs to NMDA excitotoxicity via NR2B dysregulation; riluzole and memantine reduce excitotoxic MSN death in HD models; E/I imbalance contributes to early cognitive symptoms.
- `targets` → **[Brain](../../06-organ/brain/README.md)** — HD selectively atrophies striatum (caudate + putamen) detectable by MRI 15+ years pre-onset; cortical layer V and thalamic neurons also degenerate; lateral ventricle enlargement mirrors striatal atrophy and tracks disease progression by UHDRS-TFC.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — Huntington's disease kills a specific neuron: the GABAergic medium spiny neurons of the striatum, especially indirect-pathway (D2) MSNs whose loss disinhibits movement and causes chorea; mutant huntingtin starves them of BDNF and sensitizes them to glutamate excitotoxicity.
- `connects-to` → **[Microglia](../../04-cellular/microglia/README.md)** — Neuroinflammation is an early feature of Huntington's disease: microglia activate in the striatum and cortex years before symptoms (on PET), and mutant huntingtin acts cell-autonomously inside microglia to make them hyper-reactive — adding inflammation to the neurodegeneration.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — Huntington's disease is an autosomal-dominant neurodegenerative disease of the CNS: a CAG-repeat expansion in HTT makes a toxic polyglutamine protein that destroys the striatum and cortex, causing chorea, cognitive decline, and psychiatric disturbance over 15-20 years.
