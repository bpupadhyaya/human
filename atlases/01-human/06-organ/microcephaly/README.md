---
schema: human-scale-entry/v1
id: microcephaly
name: Microcephaly
atlas: 01-human
scale: 06-organ
status: draft
last_reviewed: 2026-06-06
summary: "Head circumference >2–3 SD below mean for age/sex; reflects reduced brain volume from impaired neuroprogenitor proliferation. Causes: congenital infections (Zika, CMV, rubella), genetic mutations (ASPM, CDK5RAP2), metabolic disorders. Prognosis varies by etiology and severity."
aliases: ["primary microcephaly", "secondary microcephaly", "microcephalic primordial dwarfism"]
sources:
  - id: gilmore-2010-microcephaly-genetics
    type: peer-reviewed
    cite: "Gilmore EC, Walsh CA. Genetic causes of microcephaly and lessons for neuronal development. Genes Dev. 2013;27(24):2659-2672."
    doi: "10.1101/gad.215327.113"
    pmid: "24352420"
    url: "https://doi.org/10.1101/gad.215327.113"
  - id: brasil-2016-zika-microcephaly
    type: peer-reviewed
    cite: "Brasil P, Pereira JP Jr, Moreira ME, et al. Zika Virus Infection in Pregnant Women in Rio de Janeiro. N Engl J Med. 2016;375(24):2321-2334."
    doi: "10.1056/NEJMoa1602412"
    pmid: "26943629"
    url: "https://doi.org/10.1056/NEJMoa1602412"
  - id: passemard-2013-microcephaly-review
    type: peer-reviewed
    cite: "Passemard S, Kaindl AM, Verloes A. Microcephaly. Handb Clin Neurol. 2013;111:129-141."
    doi: "10.1016/B978-0-444-52891-9.00013-0"
    pmid: "23622159"
    url: "https://doi.org/10.1016/B978-0-444-52891-9.00013-4"
cross_links:
  - target: 01-human/06-organ/brain
    relation: targets
    note: "Microcephaly reflects failure of normal brain growth; the cortex is the primary affected structure — reduced cortical surface area and simplified gyral pattern arise from premature depletion of radial glial progenitors during fetal neuroproliferation."
  - target: 01-human/07-system/nervous-system
    relation: part-of
    note: "Microcephaly is primarily a neurodevelopmental disorder with downstream effects on the entire nervous system: cognitive impairment, epilepsy, motor dysfunction, and behavioral disorders arise from the reduced and disorganized cortical circuitry."
  - target: 01-human/06-organ/placenta
    relation: connects-to
    note: "Zika virus uses AXL receptor on extravillous trophoblast and syncytiotrophoblast for placental entry; Zika-infected placenta → neuroprogenitor apoptosis → congenital microcephaly; placental intervillositis and villitis are histological hallmarks of vertical Zika transmission."
  - target: 01-human/07-system/aicardi-goutieres-syndrome
    relation: connects-to
    note: "AGS causes post-natal progressive microcephaly via chronic IFN-α → microglial activation → cortical neuronal death; distinguishes from primary MCPH (genetic proliferation defects); basal ganglia calcification + acquired microcephaly = pseudo-TORCH presentation on neuroimaging."
  - target: 02-pathogen/06-environmental/aedes-aegypti
    relation: connects-to
    note: "Ae. aegypti-transmitted ZIKV is the primary infectious cause of congenital microcephaly; the 2015-2016 Americas epidemic established the epidemiological link; first-trimester ZIKV infects cortical neural progenitors via AXL/Tyro3 → apoptosis and cortical hypoplasia."
---

# Microcephaly

## Overview

**Microcephaly** is a neurodevelopmental condition defined by a **head circumference (HC) more than 2 standard deviations (SD) below the mean** for gestational age, sex, and ethnicity at birth or during childhood; **severe microcephaly** is defined as HC >3 SD below mean [^passemard-2013-microcephaly-review]. Head circumference serves as a proxy for brain volume: a microcephalic head reflects an abnormally small brain (microbrain), typically with a disproportionately reduced cerebral cortex.

Microcephaly affects **1–10 per 10,000 live births** depending on diagnostic threshold and population studied. It is etiologically heterogeneous — a phenotypic endpoint of diverse processes that impair the proliferative expansion of the cerebral cortex during fetal brain development.

Two broad categories are distinguished:
- **Primary (congenital) microcephaly:** Present at birth; genetic or early congenital infection; reflects impaired neuroprogenitor cell (NPC) proliferation during the second trimester
- **Secondary (postnatal) microcephaly:** Normal HC at birth followed by deceleration of head growth; results from postnatal brain injury, metabolic disorders, or progressive genetic conditions

The clinical significance of microcephaly lies not just in the head size, but in its association with **cognitive impairment** (70–90% of cases with severe microcephaly), **epilepsy** (~30–50%), **cerebral palsy**, and behavioral disorders — reflecting the underlying cortical dysgenesis.

## Structure

### Neuropathology of microcephaly

The dominant structural correlate of microcephaly is **reduced cerebral cortical surface area and volume** [^gilmore-2010-microcephaly-genetics]:

**Normal cortical development:** Radial glial progenitors (RGPs) in the ventricular zone undergo symmetric divisions (expanding the progenitor pool) and then asymmetric divisions (generating neurons that migrate outward along radial glial fibers to form the cortical layers in an inside-out order: layer VI first, layer II last). Outer radial glial (oRG) cells in the outer subventricular zone (OSVZ) amplify neuronal output in gyrencephalic species.

**Microcephaly pathogenesis:**
- **Premature switch from proliferative to neurogenic divisions:** NPC exit from cell cycle too early → exhausted progenitor pool → reduced total neuron number
- **Centrosomal/spindle defects:** Most MCPH (primary microcephaly) genes encode centrosomal proteins (ASPM, CDK5RAP2, CENPJ/CPAP, CEP135, STIL) → impaired spindle orientation → inappropriate horizontal (neurogenic) divisions → pool depletion
- **p53-mediated apoptosis:** DNA damage response activation in NPCs (e.g., Zika-induced) → p53 → apoptosis → NPC loss
- **Impaired cortical folding:** In some cases, not just reduced volume but simplification of gyral pattern (pachygyria) or complete absence of gyri (lissencephaly)

**Neuroimaging findings (MRI):**
- Simplified gyral pattern (pachygyria, agyria)
- Simplified cortical ribbon with normal or reduced thickness
- Corpus callosum abnormalities (partial or complete agenesis)
- Cerebellar hypoplasia (in some genetic forms)
- Calcifications: characteristic of congenital infections (periventricular for CMV; cortical/subcortical for Zika)

### Primary microcephaly genetics (MCPH loci)

Autosomal recessive primary microcephaly (MCPH) is caused by mutations in >25 genes; most encode **centrosomal or spindle-associated proteins**:

| Gene | Protein | Function |
|:---|:---|:---|
| ASPM (MCPH5) | Abnormal spindle-like microcephaly-associated | Apical cell division; regulates spindle pole |
| CDK5RAP2 (MCPH3) | CDK5 regulatory subunit-associated protein 2 | Centrosome maturation; γ-tubulin recruitment |
| CENPJ/CPAP (MCPH6) | Centromere protein J | Centriole length control |
| WDR62 (MCPH2) | WD40 repeat protein 62 | Spindle pole localization |
| CEP135 (MCPH8) | Centrosomal protein 135 kDa | Centriole assembly |

ASPM and CDK5RAP2 are the two most common MCPH genes in humans; ASPM underwent strong positive selection along the human lineage — correlating with the evolutionary expansion of brain size.

## Function

### Clinical correlates

**Cognitive impairment:** Severity ranges from borderline IQ (HC 2–3 SD below mean) to profound intellectual disability (>3 SD below mean or severe MCPH); reflects reduced cortical connectivity and synapse number rather than simply reduced neuron count.

**Epilepsy:** Present in ~30–50% of severe microcephaly; reflects cortical dysorganization (heterotopia, malformed layering) creating epileptogenic foci.

**Motor function:** Variable; may be relatively preserved in isolated primary microcephaly (allowing walking with physiotherapy); severely impaired in cases with associated lissencephaly or periventricular leukomalacia.

**Behavioral disorders:** Autism spectrum features, ADHD, hyperkinetic movement disorders are enriched in microcephaly syndromes.

### Zika virus-induced microcephaly [^brasil-2016-zika-microcephaly]

The 2015–2016 Zika virus (ZIKV) outbreak in Brazil dramatically elevated global awareness of microcephaly. ZIKV:
- Infects neural progenitor cells via AXL receptor (highly expressed on radial glial cells) and Tyro3
- Induces p53-mediated apoptosis and autophagy in NPCs → massive progenitor depletion
- Also produces immune evasion (IRF3 degradation) and mitotic arrest
- First trimester infection: most severe; HC deficit proportional to gestational age at infection
- Congenital Zika syndrome: microcephaly + cortical calcifications + eye abnormalities (chorioretinopathy) + contractures

ZIKV-related microcephaly highlighted the vulnerability of the expanding NPC pool to viral cytopathology during the critical second-trimester period of neuroproliferation.

### Diagnosis and management

**Prenatal detection:** Fetal HC by ultrasound at 18–20 weeks and 28–32 weeks gestation; microcephaly confirmed if HC <2 SD below mean for gestational age. MRI provides more detailed cortical anatomy.

**Postnatal:** Serial HC measurements plotted on growth charts; neuroimaging (MRI > CT to avoid radiation); genetic workup (chromosomal microarray, gene panel for MCPH genes); TORCH serology (toxoplasmosis, rubella, CMV, HSV, Zika) for congenital infections.

**Management:** No curative treatment; multidisciplinary supportive care — seizure management (antiepileptics), physiotherapy, occupational therapy, early childhood intervention, and family counseling. Prognosis depends heavily on etiology and severity.

## Connections

- `targets` → **[Brain](../../06-organ/brain/README.md)** — microcephaly directly reflects failure of normal brain growth, particularly cortical expansion; the cerebral cortex is the primary affected structure, with reduced surface area, simplified gyral pattern, and disordered lamination.
- `part-of` → **[Nervous System](../../07-system/nervous-system/README.md)** — microcephaly is a neurodevelopmental disorder of the central nervous system; the downstream clinical manifestations — cognitive impairment, epilepsy, motor dysfunction — reflect dysfunction of CNS circuits built from a reduced and disorganized cortex.
- `connects-to` → **[Placenta](../placenta/README.md)** — Zika virus uses AXL receptor on extravillous trophoblast and syncytiotrophoblast for placental entry; Zika-infected placenta → neuroprogenitor apoptosis → congenital microcephaly; placental intervillositis and villitis are histological hallmarks of vertical Zika transmission.
- `connects-to` → **[Aicardi-Goutières Syndrome](../../07-system/aicardi-goutieres-syndrome/README.md)** — AGS causes post-natal progressive microcephaly via chronic IFN-α → microglial activation → cortical neuronal death; distinguishes from primary MCPH (genetic proliferation defects); basal ganglia calcification + acquired microcephaly = pseudo-TORCH presentation on neuroimaging.
- `connects-to` → **[Aedes aegypti](../../../02-pathogen/06-environmental/aedes-aegypti/README.md)** — Ae. aegypti-transmitted ZIKV is the primary infectious cause of congenital microcephaly; the 2015-2016 Americas epidemic established the epidemiological link; first-trimester ZIKV infects cortical neural progenitors via AXL/Tyro3 → apoptosis and cortical hypoplasia.

## Pathology

**Congenital cytomegalovirus (CMV):** The most common infectious cause of congenital microcephaly in high-income countries; CMV infects NPCs via PDGFR-α and other receptors; calcifications are periventricular (characteristic); sensorineural hearing loss is the most common CMV-associated disability even without microcephaly.

**Metabolic microcephaly:** PKU (phenylketonuria), organic acidemias, mitochondrial disease → brain injury from toxic metabolite accumulation or energy failure → postnatal microcephaly. PKU microcephaly is almost entirely preventable with newborn screening and dietary restriction.

**Microcephalic primordial dwarfism:** Severe reduction of brain AND body size — Seckel syndrome (ATR mutation), MOPD (microcephalic osteodysplastic primordial dwarfism); these are separate from isolated MCPH.

**Radiation-induced microcephaly:** Historical observation — second-trimester fetal exposure to ionizing radiation (e.g., atomic bomb survivors) → dose-dependent microcephaly; maximum sensitivity at 8–15 weeks gestation (peak of neuroproliferation); provided early evidence for the critical-period concept.

[^gilmore-2010-microcephaly-genetics]: Gilmore EC, Walsh CA. Genetic causes of microcephaly and lessons for neuronal development. *Genes Dev.* 2013;27(24):2659-2672. [doi:10.1101/gad.215327.113](https://doi.org/10.1101/gad.215327.113) · [PubMed 24352420](https://pubmed.ncbi.nlm.nih.gov/24352420/)
[^brasil-2016-zika-microcephaly]: Brasil P, Pereira JP Jr, Moreira ME, et al. Zika Virus Infection in Pregnant Women in Rio de Janeiro. *N Engl J Med.* 2016;375(24):2321-2334. [doi:10.1056/NEJMoa1602412](https://doi.org/10.1056/NEJMoa1602412) · [PubMed 26943629](https://pubmed.ncbi.nlm.nih.gov/26943629/)
[^passemard-2013-microcephaly-review]: Passemard S, Kaindl AM, Verloes A. Microcephaly. *Handb Clin Neurol.* 2013;111:129-141. [doi:10.1016/B978-0-444-52891-9.00013-0](https://doi.org/10.1016/B978-0-444-52891-9.00013-0) · [PubMed 23622159](https://pubmed.ncbi.nlm.nih.gov/23622159/)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
