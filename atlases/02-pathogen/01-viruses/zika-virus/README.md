---
schema: pathogen-entry/v1
id: zika-virus
name: Zika Virus (ZIKV)
atlas: 02-pathogen
scale: 01-viruses
status: draft
last_reviewed: 2026-06-05
summary: "Flaviviridae; positive-sense ssRNA; Aedes-vectored plus sexual transmission. Targets neural progenitor cells via AXL/TYRO3 → microcephaly. Congenital Zika syndrome; Guillain-Barre in adults. 2015-2016 Americas epidemic. No approved vaccine."
aliases: ["ZIKV", "Zika fever virus", "Zika arbovirus"]
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
  - id: mlakar-2016-microcephaly
    type: peer-reviewed
    cite: "Mlakar J, Korva M, Tul N, et al. Zika virus associated with microcephaly. N Engl J Med. 2016;374(10):951-958."
    doi: "10.1056/NEJMoa1600651"
    pmid: "26862926"
    url: "https://doi.org/10.1056/NEJMoa1600651"
    accessed: "2026-06-05"
  - id: tang-2016-axl-npc
    type: peer-reviewed
    cite: "Tang H, Hammack C, Ogden SC, et al. Zika virus infects human cortical neural progenitors and attenuates their growth. Cell Stem Cell. 2016;18(5):587-590."
    doi: "10.1016/j.stem.2016.02.016"
    pmid: "26952783"
    url: "https://doi.org/10.1016/j.stem.2016.02.016"
    accessed: "2026-06-05"
  - id: cao-lormeau-2016-gbs
    type: peer-reviewed
    cite: "Cao-Lormeau VM, Blake A, Mons S, et al. Guillain-Barré syndrome outbreak associated with Zika virus infection in French Polynesia: a case-control study. Lancet. 2016;387(10027):1531-1539."
    doi: "10.1016/S0140-6736(16)00562-6"
    pmid: "26948433"
    url: "https://doi.org/10.1016/S0140-6736(16)00562-6"
    accessed: "2026-06-05"
cross_links:
  - target: 01-human/07-system/nervous-system
    relation: damages
    note: "Zika infects neural progenitor cells via AXL/TYRO3, causing NPC apoptosis, impaired cortical neurogenesis, microcephaly, and Guillain-Barre syndrome through molecular mimicry of gangliosides on peripheral nervous system myelin."
  - target: 01-human/06-organ/brain
    relation: damages
    note: "Congenital Zika destroys proliferating neural progenitor cells in the ventricular zone, producing lissencephaly, cortical thinning, and periventricular calcifications characteristic of congenital Zika syndrome in the developing brain."
  - target: 01-human/07-system/immune-system
    relation: damages
    note: "Zika NS5 inhibits STAT2 phosphorylation, blocking IFN-beta signalling and suppressing innate immune antiviral responses; NS1 and NS3 further antagonise complement, restricting immune-mediated viral clearance."
  - target: 01-human/03-molecular/nf-kb
    relation: modulates
    note: "Zika activates NF-kB in infected neural progenitor cells and placental trophoblasts, upregulating pro-inflammatory cytokines and apoptotic mediators that amplify tissue damage beyond directly virus-infected cells."
---

# Zika Virus (ZIKV)

## Overview

Zika virus (ZIKV) is a **positive-sense single-stranded RNA virus** (family *Flaviviridae*, genus *Flavivirus*) first isolated from a sentinel rhesus macaque in the Zika Forest of Uganda in 1947. For over six decades, ZIKV was considered a minor arbovirus causing sporadic mild febrile illness in equatorial Africa and Asia. The virus transformed into a global public health emergency following explosive epidemics in Yap Island (2007), French Polynesia (2013–2014), and most dramatically, the Americas (2015–2016), when ZIKV's causal role in **congenital microcephaly** and **Guillain-Barré syndrome** (GBS) was established [^mlakar-2016-microcephaly].

ZIKV is transmitted primarily by the bite of infected **Aedes aegypti** and *Aedes albopictus* mosquitoes — the same vectors responsible for dengue and chikungunya. Uniquely among arboviruses of public health significance, ZIKV is also transmitted **sexually** (male-to-female, female-to-male, and male-to-male), perinatally (transplacental), and by blood transfusion. Sexual transmission can occur weeks after symptomatic or asymptomatic male infection owing to persistence of ZIKV RNA in semen.

The 2015–2016 Americas epidemic resulted in over 800,000 confirmed and suspected cases in Brazil alone, thousands of infants born with congenital Zika syndrome (CZS), and triggered the WHO declaration of a Public Health Emergency of International Concern (PHEIC) in February 2016. As of 2026, **no vaccine or specific antiviral** is approved for ZIKV, though mRNA vaccine candidates have entered clinical trials [^mandell-principles].

## Structure

| Component | Detail |
|:---|:---|
| **Genome** | ~10.8 kb positive-sense ssRNA; single open reading frame |
| **Structural proteins** | C (capsid), prM/M (pre-membrane/membrane), E (envelope) |
| **Non-structural proteins** | NS1, NS2A, NS2B, NS3 (helicase/protease), NS4A, NS4B, NS5 (RdRp + methyltransferase) |
| **Envelope (E) protein** | Homotrimeric on virion surface; domain III mediates receptor binding; target of neutralizing antibodies; cross-reactive with dengue E |
| **NS5 protein** | Bifunctional: N-terminal methyltransferase (5' cap formation) and C-terminal RdRp; critical IFN antagonist (blocks STAT2 phosphorylation) |
| **Particle size** | ~40 nm icosahedral, enveloped |
| **Genome organization** | 5'-UTR — C — prM — E — NS1 — NS2A — NS2B — NS3 — NS4A — NS4B — NS5 — 3'-UTR |

### Phylogenetic Lineages

ZIKV is classified into two major lineages:
- **African lineage** (East African + West African clades): original Ugandan isolates and related strains; generally associated with mild sylvatic transmission cycle
- **Asian lineage**: descended from an Asian ancestor; responsible for all epidemic disease in the Pacific and Americas; harbors specific genetic signatures in the prM protein (S139N substitution) associated with enhanced neurovirulence in mouse and human organoid models

## Infection Mechanism

### 1. Mosquito-Mediated Inoculation

*Aedes aegypti* deposits saliva containing ZIKV into the skin during blood feeding. Salivary proteins in the inoculum modulate local immune responses, enhancing viral infection. In the skin, **keratinocytes, fibroblasts, and dermal dendritic cells** (particularly Langerhans cells) are the primary initial targets, expressing the entry receptors **AXL, TYRO3, TIM-1**, and **DC-SIGN**. AXL and TYRO3 are receptor tyrosine kinases that bind phosphatidylserine (PS)-coated viral envelopes via their ligands Gas6 and Protein S (PS-mediated viral entry, or "apoptotic mimicry") [^tang-2016-axl-npc].

### 2. Viremia and Systemic Spread

After local replication, ZIKV enters lymphatics and bloodstream, establishing viremia (typically peaking at 3–7 days post-infection). ZIKV RNA is detectable in blood for 5–7 days, in urine for 2–3 weeks, and in semen for up to 6 months. The virus crosses the **placenta** via infection of Hofbauer cells (placental macrophages) and trophoblasts (which express high AXL levels), gaining access to the fetal circulation.

### 3. Neural Progenitor Cell (NPC) Tropism

The most consequential tropism of ZIKV is for **cortical neural progenitor cells (NPCs)** in the developing brain. NPCs of the ventricular zone express **AXL** at high levels, making them highly susceptible to infection. ZIKV infection of NPCs causes [^tang-2016-axl-npc]:

- **G2/M cell cycle arrest** via degradation of the centrosomal regulator ANKLE2 (a substrate identified via ZIKV NS4A/NS4B interaction)
- **Activation of caspase-3-mediated apoptosis** and p53-dependent cell death
- **Disruption of asymmetric division**: infected NPCs are more likely to undergo symmetric terminal differentiation rather than self-renewal, depleting the progenitor pool
- **Mitotic spindle disruption**: NS5 and ZIKV envelope protein interactions with centrosomal components disrupt mitotic spindle formation

The result is **reduced cortical surface area** and **microcephaly** — the hallmark of congenital Zika syndrome.

## Host Interactions

### Immune Evasion

ZIKV has evolved multiple mechanisms to suppress innate antiviral defenses:

- **NS5 methyltransferase domain** directly binds and promotes proteasomal degradation of **STAT2**, blocking type I and type III IFN signaling cascades downstream of IFNAR1/2 and IFNLR1. This is the primary mechanism of IFN antagonism and explains why ZIKV replicates efficiently even in IFN-competent cells [^mandell-principles]
- **NS1** activates the NLRP3 inflammasome in macrophages and promotes IL-1β secretion, potentially contributing to both local tissue damage and placental inflammation
- **NS3/NS4A** interaction with ANKLE2 disrupts Lamin B1 — a nuclear laminar protein — causing mitotic defects in NPCs even in absence of productive infection
- **Complement evasion**: NS1 (secreted form) binds complement component C1q and inhibits classical pathway activation, limiting antibody-mediated viral clearance
- **NF-κB activation** in infected NPCs and trophoblasts upregulates pro-inflammatory cytokines (IL-6, IL-8, TNF-α) and anti-apoptotic signals initially, but sustained NF-κB activity eventually tips toward apoptotic gene expression, amplifying cell death beyond directly infected cells

### Guillain-Barré Syndrome Mechanism

ZIKV infection is associated with a markedly elevated incidence of GBS (~24-fold increase), particularly the **acute motor axonal neuropathy (AMAN)** subtype. The proposed mechanism involves **molecular mimicry**: ZIKV glycoproteins share epitopes with gangliosides (GM1, GD1a) on peripheral nerve myelin. Antibodies generated against viral antigens cross-react with ganglioside epitopes, activating complement at the nodes of Ranvier and axon initial segments, causing immune-mediated axonal injury [^cao-lormeau-2016-gbs].

## Pathology

### Disease Spectrum

| Presentation | Frequency | Key Features |
|:---|:---|:---|
| Asymptomatic infection | ~80% of ZIKV-infected adults | No symptoms; viremia and shedding still occur; seropositivity documented retrospectively |
| Acute Zika fever | ~20% | Mild fever, maculopapular rash (often pruritic), arthralgia, conjunctivitis, retro-orbital headache; 3–7 day self-limited illness |
| Guillain-Barré syndrome | ~1–2/10,000 infections | Usually AMAN or AMSAN subtype; onset 1–4 weeks after acute illness; ascending paralysis; cranial nerve involvement; intensive care in severe cases |
| Congenital Zika syndrome (CZS) | ~5–14% of pregnancies during viremic phase (first trimester highest risk) | Microcephaly, lissencephaly, cortical thinning, periventricular and subcortical calcifications, ventriculomegaly, cerebellar hypoplasia, optic nerve abnormalities |
| Other congenital abnormalities | Variable | Clubfoot, arthrogryposis, sensorineural hearing loss, intellectual disability without microcephaly |

### Congenital Zika Syndrome — Neuroimaging Hallmarks

CZS neuroimaging shows a characteristic pattern on fetal or neonatal MRI/CT:
1. **Microcephaly** (head circumference >2 SD below mean) — may be progressive
2. **Periventricular and subcortical calcifications** — distinguish CZS from other TORCH infections
3. **Simplified gyral pattern** (pachygyria/lissencephaly) — reflects cortical neurogenesis failure
4. **Ventriculomegaly** (ex vacuo) — secondary to cortical volume loss
5. **Cerebellar and corpus callosum hypoplasia** — white matter abnormalities prominent

### Treatment

No approved antiviral therapy exists. Management:

| Condition | Management |
|:---|:---|
| **Acute Zika fever** | Supportive (antipyretics — avoid NSAIDs/aspirin in endemic areas due to dengue co-circulation and hemorrhage risk) |
| **GBS** | IVIG (2 g/kg over 5 days) or plasmapheresis; ICU respiratory support if bulbar/respiratory involvement |
| **Congenital Zika syndrome** | Multidisciplinary developmental support; neurology, ophthalmology, audiology follow-up; seizure management; no disease-modifying therapy |
| **Prevention in pregnancy** | Avoidance of travel to endemic areas; insect repellent; sexual abstinence or condom use by male partners returning from endemic areas (6 months if symptomatic; ongoing discussions about duration for asymptomatic exposures) |

### Vaccine Development (as of 2026)

| Platform | Developer | Status |
|:---|:---|:---|
| mRNA (lipid nanoparticle) | Moderna, NIH | Phase II |
| DNA (pVAX1-ZIKV-prME) | NIAID/Inovio | Phase II |
| Purified inactivated virus (ZPIV) | WRAIR/GSK | Phase II |
| Live-attenuated chimeric | Multiple | Preclinical-Phase I |

No candidate has reached Phase III efficacy trials as of the last_reviewed date, partly due to waning incidence making efficacy endpoint achievement difficult [^mandell-principles].

## Connections

- **Damages** → [Nervous System](../../../01-human/07-system/nervous-system/README.md): Zika infects neural progenitor cells via AXL/TYRO3, causing NPC apoptosis, impaired cortical neurogenesis, microcephaly, and Guillain-Barre syndrome through molecular mimicry of gangliosides on peripheral nervous system myelin.
- **Damages** → [Brain](../../../01-human/06-organ/brain/README.md): Congenital Zika destroys proliferating neural progenitor cells in the ventricular zone, producing lissencephaly, cortical thinning, and periventricular calcifications characteristic of congenital Zika syndrome in the developing brain.
- **Damages** → [Immune System](../../../01-human/07-system/immune-system/README.md): Zika NS5 inhibits STAT2 phosphorylation, blocking IFN-beta signalling and suppressing innate immune antiviral responses; NS1 and NS3 further antagonise complement, restricting immune-mediated viral clearance.
- **Modulates** → [NF-kB](../../../01-human/03-molecular/nf-kb/README.md): Zika activates NF-kB in infected neural progenitor cells and placental trophoblasts, upregulating pro-inflammatory cytokines and apoptotic mediators that amplify tissue damage beyond directly virus-infected cells.

---

> **AI co-maintenance notice:** This entry was drafted with AI assistance and is subject to expert review. Content reflects published literature as of the last_reviewed date. Errors may be present; verify critical facts against primary sources before clinical or research use.

[^mandell-principles]: Bennett JE, Dolin R, Blaser MJ. *Mandell, Douglas, and Bennett's Principles and Practice of Infectious Diseases.* 9th ed. Elsevier; 2020.
[^murray-microbiology]: Murray PR, Rosenthal KS, Pfaller MA. *Medical Microbiology.* 9th ed. Elsevier; 2021.
[^mlakar-2016-microcephaly]: Mlakar J, Korva M, Tul N, et al. Zika virus associated with microcephaly. *N Engl J Med.* 2016;374(10):951-958. [doi:10.1056/NEJMoa1600651](https://doi.org/10.1056/NEJMoa1600651) · [PubMed 26862926](https://pubmed.ncbi.nlm.nih.gov/26862926/)
[^tang-2016-axl-npc]: Tang H, Hammack C, Ogden SC, et al. Zika virus infects human cortical neural progenitors and attenuates their growth. *Cell Stem Cell.* 2016;18(5):587-590. [doi:10.1016/j.stem.2016.02.016](https://doi.org/10.1016/j.stem.2016.02.016) · [PubMed 26952783](https://pubmed.ncbi.nlm.nih.gov/26952783/)
[^cao-lormeau-2016-gbs]: Cao-Lormeau VM, Blake A, Mons S, et al. Guillain-Barré syndrome outbreak associated with Zika virus infection in French Polynesia. *Lancet.* 2016;387(10027):1531-1539. [doi:10.1016/S0140-6736(16)00562-6](https://doi.org/10.1016/S0140-6736(16)00562-6) · [PubMed 26948433](https://pubmed.ncbi.nlm.nih.gov/26948433/)
