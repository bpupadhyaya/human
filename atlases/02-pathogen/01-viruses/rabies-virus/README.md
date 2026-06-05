---
schema: pathogen-entry/v1
id: rabies-virus
name: Rabies Virus (RABV)
atlas: 02-pathogen
scale: 01-viruses
status: draft
last_reviewed: 2026-06-05
summary: "Rhabdoviridae; bullet-shaped enveloped negative-sense ssRNA. G protein binds nAChR at NMJ; retrograde axonal transport to CNS. Near-100% fatal once symptomatic; ~59,000 deaths/year. PEP (RIG + vaccine) essentially 100% effective if timely."
aliases: ["RABV", "classical rabies virus", "rabies lyssavirus", "Lyssavirus rabies"]
sources:
  - id: mandell-principles
    type: textbook
    cite: "Bennett JE, Dolin R, Blaser MJ. Mandell, Douglas, and Bennett's Principles and Practice of Infectious Diseases. 9th ed. Elsevier; 2020."
    url: "https://www.elsevier.com/books/mandell-douglas-and-bennetts-principles-and-practice-of-infectious-diseases/bennett/978-0-323-48255-4"
    accessed: "2026-06-05"
  - id: murray-microbiology
    type: textbook
    cite: "Murray PR, Rosenthal KS, Pfaller MA. Medical Microbiology. 9th ed. Elsevier; 2021."
    url: "https://www.elsevier.com/books/medical-microbiology/murray/978-0-323-67378-4"
    accessed: "2026-06-05"
  - id: hampson-2015-global-burden
    type: peer-reviewed
    cite: "Hampson K, Coudeville L, Lembo T, et al. Estimating the global burden of endemic canine rabies. PLoS Negl Trop Dis. 2015;9(4):e0003709."
    doi: "10.1371/journal.pntd.0003709"
    pmid: "25881058"
    url: "https://doi.org/10.1371/journal.pntd.0003709"
    accessed: "2026-06-05"
  - id: lafon-2005-rabies-evasion
    type: peer-reviewed
    cite: "Lafon M. Rabies virus receptors. J Neurovirol. 2005;11(1):82-87."
    doi: "10.1080/13550280590900427"
    pmid: "15804965"
    url: "https://doi.org/10.1080/13550280590900427"
    accessed: "2026-06-05"
  - id: rupprecht-2017-pep
    type: peer-reviewed
    cite: "Rupprecht CE, Briggs D, Brown CM, et al. Use of a reduced (4-dose) vaccine schedule for postexposure prophylaxis to prevent human rabies. MMWR Recomm Rep. 2010;59(RR-2):1-9."
    pmid: "20300058"
    url: "https://www.cdc.gov/mmwr/preview/mmwrhtml/rr5902a1.htm"
    accessed: "2026-06-05"
cross_links:
  - target: 01-human/07-system/nervous-system
    relation: damages
    note: "Rabies travels by retrograde axonal transport through peripheral nervous system to the CNS at ~2-3 mm/day, causing encephalomyelitis with Negri bodies in hippocampal neurons and near-universal fatality once symptoms appear."
  - target: 01-human/06-organ/brain
    relation: damages
    note: "Rabies spreads trans-synaptically from limbic regions to neocortex and brainstem, causing behavioural changes, hydrophobia, and autonomic failure; Negri bodies (eosinophilic inclusions) are pathognomonic in hippocampal neurons."
  - target: 01-human/04-cellular/neuron
    relation: infects
    note: "Rabies G protein binds nAChR, NCAM, and p75NTR on neurons at the NMJ; endocytic internalization enables retrograde axonal transport to cell bodies and subsequent trans-synaptic spread through neuronal networks."
  - target: 04-vaccine/04-inactivated/rabies-vaccine
    relation: prevented-by
    note: "PrEP and PEP using inactivated rabies vaccines (HDCV, PCECV) with rabies immunoglobulin essentially eliminate fatal outcome; timeliness of administration after exposure is the critical determinant of efficacy."
---

# Rabies Virus (RABV)

## Overview

Rabies virus (RABV) is an **enveloped, negative-sense single-stranded RNA virus** (family *Rhabdoviridae*, genus *Lyssavirus*, species *Rabies lyssavirus*) and the causative agent of rabies encephalitis — one of the oldest and most feared infectious diseases known to humanity. RABV is virtually unique among human pathogens in that **established infection is nearly 100% fatal**, yet it is also almost entirely **preventable** through post-exposure prophylaxis (PEP) administered prior to the onset of symptoms.

Globally, rabies kills approximately **59,000 people per year**, with >95% of deaths occurring in Asia and Africa where domestic dog bites are the overwhelmingly dominant exposure route (~99% of human cases) [^hampson-2015-global-burden]. Children under 15 account for ~40% of deaths. In addition to RABV, the genus *Lyssavirus* includes 17 other species (e.g., Australian bat lyssavirus, Duvenhage virus), some of which have caused fatal human infections unresponsive to standard rabies PEP.

The infection follows a clinically dramatic course: a prolonged and variable incubation period (typically 1–3 months, but ranging from days to years depending on inoculum site and density of peripheral nervous system innervation), followed by a prodrome of non-specific symptoms and paraesthesias at the bite site, then rapid neurological deterioration and death within days to weeks of encephalitis onset. A handful of survivorship cases (most linked to the Milwaukee Protocol of induced therapeutic coma) have been documented, but survival remains exceedingly rare [^mandell-principles].

## Structure

| Component | Detail |
|:---|:---|
| **Genome** | ~12 kb negative-sense ssRNA; 5 genes in linear order: N-P-M-G-L |
| **Nucleoprotein (N)** | Encapsidates RNA; forms helical nucleocapsid; primary target for diagnostic RT-PCR and DFA |
| **Phosphoprotein (P)** | Polymerase cofactor; also an IFN antagonist (blocks STAT1/STAT2 nuclear import) |
| **Matrix protein (M)** | Links nucleocapsid to envelope; drives bullet-shape morphology and budding |
| **Glycoprotein (G)** | Homotrimeric surface spike; receptor binding and membrane fusion; sole target of virus-neutralizing antibodies; key pathogenicity and neurotropism determinant |
| **Large protein (L)** | RNA-dependent RNA polymerase; also mRNA capping enzyme |
| **Particle morphology** | Bullet-shaped, 75 × 180 nm; distinctive asymmetric shape unique among human-pathogenic viruses |
| **Envelope** | Host-derived lipid bilayer with G protein trimers; acquired during budding from plasma membrane |

### The G Protein — Neurotropism Determinant

Amino acid position **333 of the G protein** is the primary determinant of RABV pathogenicity: virulent strains bear arginine (R333), while attenuated laboratory and vaccine strains often carry glutamine or glycine at this position. R333 is critical for efficient binding to the low-affinity nerve growth factor receptor **p75NTR**, and mutations here reduce neuroinvasiveness by orders of magnitude without affecting viral replication [^lafon-2005-rabies-evasion].

## Infection Mechanism

### 1. Entry at the Neuromuscular Junction

Following inoculation (typically by bite with deposition of infected saliva into muscle or subcutaneous tissue), RABV preferentially infects **motor nerve terminals at the neuromuscular junction (NMJ)**. Three identified neuronal receptors mediate G protein binding:

- **Nicotinic acetylcholine receptor (nAChR)** — concentrated at NMJ postsynaptic folds; binds G protein via a region homologous to neurotoxin binding sites
- **Neural cell adhesion molecule (NCAM/CD56)** — present on neurons and myocytes
- **p75 neurotrophin receptor (p75NTR)** — low-affinity NGF receptor; expressed on peripheral neurons

The virus is internalized by clathrin-mediated endocytosis. Acidification of the endosome triggers G protein conformational change and membrane fusion, releasing the nucleocapsid into the cytoplasm [^lafon-2005-rabies-evasion].

### 2. Retrograde Axonal Transport to the CNS

Once inside the motor or sensory nerve terminal, the nucleocapsid is **transported retrogradely toward the neuronal cell body** using the dynein/dynactin motor complex on microtubule tracks, at a rate of **~2–3 mm/day** (slower in sensory nerves, faster in motor nerves). This rate directly determines the incubation period: bites to the face or neck (short peripheral nerve length to brainstem) cause rapid disease; bites to extremities allow weeks to months before CNS penetration.

Upon reaching the dorsal root ganglion and spinal cord, the virus replicates and spreads **centripetally** through the neuraxis, reaching the brainstem, cerebellum, hippocampus, and cortex via **trans-synaptic spread** — releasing new virions across synapses to infect successive neurons [^mandell-principles].

### 3. Centrifugal Spread

After establishing CNS infection, RABV spreads **centrifugally** along efferent autonomic and motor nerves to peripheral organs: salivary glands (enabling transmission), cornea, skin, heart, adrenal glands, and retina. Viral antigen detection in skin biopsies (nape of neck) and corneal impression smears exploits this centrifugal spread for antemortem diagnosis.

## Host Interactions

### Immune Evasion — Exploiting Immunological Privilege of the CNS

RABV has evolved multiple strategies that allow it to replicate in neurons while avoiding immune detection:

- **Phosphoprotein (P)** blocks nuclear import of STAT1 (phosphorylated) and STAT2, preventing IFN-stimulated gene transcription — a critical early evasion mechanism in peripheral nerve terminals before CNS entry [^lafon-2005-rabies-evasion]
- RABV replicates without triggering significant neuronal apoptosis early in infection — maintaining neuronal viability is essential for trans-synaptic spread
- **Minimal inflammation** in early CNS infection: the virus exploits neuronal immune privilege (low MHC-I expression, blood-brain barrier) to avoid T cell-mediated clearance
- Perivascular lymphocytic infiltration (Babes nodules) and microglial activation occur only after viral replication is firmly established
- **G protein mimicry of snake neurotoxin**: RABV G protein binds nAChR at the acetylcholine binding site, potentially inhibiting synaptic transmission, which may contribute to the neurological dysfunction disproportionate to the modest degree of neuronal death observed at autopsy

### Absence of Substantial Neuronal Death

A paradox of rabies encephalitis is that **neuronal loss is relatively modest** despite overwhelming clinical severity. The mechanism of neurological dysfunction may be largely **functional** (disruption of ion channels, synaptic signaling, neurotransmitter release) rather than structural (cell death). This has implications for the rare survival cases: rapid immune clearance before irreversible structural damage could theoretically permit neurological recovery.

## Pathology

### Disease Stages

| Stage | Duration | Clinical Features |
|:---|:---|:---|
| **Incubation** | Days to years (median 1–3 months) | Asymptomatic; virus confined to peripheral nervous system |
| **Prodrome** | 2–10 days | Fever, malaise, headache; paraesthesias/pain at bite site (pathognomonic when present) |
| **Acute neurological phase — furious (encephalitic) form** | 2–7 days | Hydrophobia, aerophobia, autonomic dysfunction, agitation, hypersalivation, fluctuating consciousness; ~80% of clinical cases |
| **Acute neurological phase — paralytic (dumb) form** | 2–14 days | Ascending flaccid paralysis mimicking Guillain-Barré; less hydrophobia; ~20% of clinical cases |
| **Coma and death** | Days | Progressive brainstem failure, cardiac arrhythmias, respiratory arrest |

### Neuropathology

- **Negri bodies**: eosinophilic intracytoplasmic inclusion bodies in hippocampal pyramidal neurons (Sommer sector, CA3) and cerebellar Purkinje cells — pathognomonic of rabies; represent aggregates of viral nucleocapsid protein and viral RNA within membrane-less organelles termed **Negri body-like structures** (NBLs)
- **Babes nodules**: small perivascular glial/lymphocytic aggregates throughout the brainstem and spinal cord
- **Diffuse neuronal involvement** without commensurate cell death — supporting the functional over structural mechanism hypothesis

### Treatment

**Once clinical rabies begins, no therapy has reliably prevented death.** Management is palliative or experimental:

| Approach | Status |
|:---|:---|
| **Supportive ICU care** (sedation, mechanical ventilation) | Standard palliative |
| **Milwaukee Protocol** (induced therapeutic coma with ketamine, midazolam, ribavirin, amantadine) | Anecdotal survivors; controlled trial negative; not recommended outside experimental context |
| **PEP (wound care + RIG + vaccine)** | ~100% effective if initiated before symptom onset |
| **Pre-exposure prophylaxis (PrEP)** | 3-dose series IM (days 0, 7, 21 or 28); recommended for high-risk occupations and travelers |

### Post-Exposure Prophylaxis Protocol (WHO/CDC)

1. **Immediate wound washing**: soap and water for ≥15 minutes; povidone-iodine application
2. **Rabies immunoglobulin (RIG)**: human RIG (HRIG) 20 IU/kg or equine RIG (ERIG) 40 IU/kg — infiltrated into and around wound; remainder IM (not same site as vaccine); administered on day 0 only
3. **Rabies vaccine** (HDCV, PCECV, or PVRV): 4 doses IM (days 0, 3, 7, 14); previously vaccinated individuals require only 2 doses (days 0, 3); no RIG if previously vaccinated [^rupprecht-2017-pep]

## Connections

- **Damages** → [Nervous System](../../../01-human/07-system/nervous-system/README.md): Rabies travels by retrograde axonal transport through peripheral nervous system to the CNS at ~2-3 mm/day, causing encephalomyelitis with Negri bodies in hippocampal neurons and near-universal fatality once symptoms appear.
- **Damages** → [Brain](../../../01-human/06-organ/brain/README.md): Rabies spreads trans-synaptically from limbic regions to neocortex and brainstem, causing behavioural changes, hydrophobia, and autonomic failure; Negri bodies (eosinophilic inclusions) are pathognomonic in hippocampal neurons.
- **Infects** → [Neuron](../../../01-human/04-cellular/neuron/README.md): Rabies G protein binds nAChR, NCAM, and p75NTR on neurons at the NMJ; endocytic internalization enables retrograde axonal transport to cell bodies and subsequent trans-synaptic spread through neuronal networks.
- **Prevented-by** → [Rabies Vaccine](../../../04-vaccine/04-inactivated/rabies-vaccine/README.md): PrEP and PEP using inactivated rabies vaccines (HDCV, PCECV) with rabies immunoglobulin essentially eliminate fatal outcome; timeliness of administration after exposure is the critical determinant of efficacy.

---

> **AI co-maintenance notice:** This entry was drafted with AI assistance and is subject to expert review. Content reflects published literature as of the last_reviewed date. Errors may be present; verify critical facts against primary sources before clinical or research use.

[^mandell-principles]: Bennett JE, Dolin R, Blaser MJ. *Mandell, Douglas, and Bennett's Principles and Practice of Infectious Diseases.* 9th ed. Elsevier; 2020.
[^murray-microbiology]: Murray PR, Rosenthal KS, Pfaller MA. *Medical Microbiology.* 9th ed. Elsevier; 2021.
[^hampson-2015-global-burden]: Hampson K, Coudeville L, Lembo T, et al. Estimating the global burden of endemic canine rabies. *PLoS Negl Trop Dis.* 2015;9(4):e0003709. [doi:10.1371/journal.pntd.0003709](https://doi.org/10.1371/journal.pntd.0003709) · [PubMed 25881058](https://pubmed.ncbi.nlm.nih.gov/25881058/)
[^lafon-2005-rabies-evasion]: Lafon M. Rabies virus receptors. *J Neurovirol.* 2005;11(1):82-87. [doi:10.1080/13550280590900427](https://doi.org/10.1080/13550280590900427) · [PubMed 15804965](https://pubmed.ncbi.nlm.nih.gov/15804965/)
[^rupprecht-2017-pep]: Rupprecht CE, Briggs D, Brown CM, et al. Use of a reduced (4-dose) vaccine schedule for postexposure prophylaxis to prevent human rabies. *MMWR Recomm Rep.* 2010;59(RR-2):1-9. [PubMed 20300058](https://pubmed.ncbi.nlm.nih.gov/20300058/)
