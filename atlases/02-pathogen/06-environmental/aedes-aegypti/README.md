---
schema: pathogen-entry/v1
id: aedes-aegypti
name: Aedes aegypti
atlas: 02-pathogen
scale: 06-environmental
status: draft
last_reviewed: 2026-06-06
summary: "Tropical/subtropical day-biting mosquito; primary vector for dengue, Zika, chikungunya, and yellow fever. Breeds in man-made water containers; endophilic/endophagic behavior maximizes human contact. ~390 million dengue infections/year attributable."
aliases: ["yellow fever mosquito", "dengue mosquito", "Aedes", "A. aegypti", "arboviral vector"]
sources:
  - id: bhatt-2013-dengue-global
    type: peer-reviewed
    cite: "Bhatt S, Gething PW, Brady OJ, et al. The global distribution and burden of dengue. Nature. 2013;496(7446):504-507."
    doi: "10.1038/nature12060"
    pmid: "23563266"
    url: "https://doi.org/10.1038/nature12060"
  - id: kraemer-2015-aedes-distribution
    type: peer-reviewed
    cite: "Kraemer MUG, Sinka ME, Duda KA, et al. The global distribution of the arbovirus vectors Aedes aegypti and Ae. albopictus. eLife. 2015;4:e08347."
    doi: "10.7554/eLife.08347"
    pmid: "26126267"
    url: "https://doi.org/10.7554/eLife.08347"
  - id: moreira-2009-wolbachia
    type: peer-reviewed
    cite: "Moreira LA, Iturbe-Ormaetxe I, Jeffery JA, et al. A Wolbachia symbiont in Aedes aegypti limits infection with dengue, Chikungunya, and Plasmodium. Cell. 2009;139(7):1268-1278."
    doi: "10.1016/j.cell.2009.11.042"
    pmid: "20064373"
    url: "https://doi.org/10.1016/j.cell.2009.11.042"
cross_links:
  - target: 02-pathogen/01-viruses/dengue-virus
    relation: targets
    note: "Aedes aegypti is the principal vector of all four dengue serotypes (DENV1-4); virus replicates in salivary glands after 8-12 day extrinsic incubation period; transmitted during bloodmeal."
  - target: 02-pathogen/01-viruses/zika-virus
    relation: targets
    note: "Aedes aegypti is the primary vector of Zika virus (ZIKV); drove the 2015-2016 Americas epidemic; sexual transmission also documented but vector transmission accounts for most spread."
---

# Aedes aegypti

## Overview

*Aedes aegypti* (the yellow fever mosquito) is a small (~3–4 mm), dark-colored mosquito with distinctive white lyre-shaped markings on the thorax and banded white tarsal segments. It is the **primary arthropod vector** responsible for transmitting four medically critical arboviruses: **dengue virus** (all four serotypes), **Zika virus**, **chikungunya virus**, and **yellow fever virus** [^bhatt-2013-dengue-global].

Unlike many mosquito species, *Ae. aegypti* is **highly anthropophilic** — preferring to feed on humans — and **endophilic/endophagic** — living and feeding indoors. These traits make it an extraordinarily efficient bridge between human hosts, amplifying arboviral transmission in dense urban settings. The species originated in sub-Saharan Africa and has spread globally through the slave trade and global commerce, now inhabiting tropical and subtropical regions between approximately 35°N and 35°S latitude [^kraemer-2015-aedes-distribution].

Dengue alone accounts for **~390 million infections per year** (96 million apparent cases; 294 million subclinical) across 128 endemic countries — all attributable primarily to *Ae. aegypti* transmission.

## Structure

### Biological Classification and Morphology

| Feature | Detail |
|:---|:---|
| **Order / Family** | Diptera / Culicidae |
| **Genus / Species** | *Aedes aegypti* (Linnaeus, 1762); formerly *Culex aegypti* |
| **Size** | Female: 3–5 mm; Male: 2–3 mm |
| **Distinguishing marks** | Lyre-shaped white scales on scutum (dorsal thorax); white tarsal banding; silvery-white lateral thoracic markings |
| **Wings** | Narrow; darkly scaled; venation without pale spots (distinguishes from *Ae. albopictus* which has plain scutum) |
| **Mouthparts** | Female: piercing-sucking proboscis; male: non-piercing (nectar-feeding only) |

### Life Cycle

The life cycle is holometabolous (complete metamorphosis):

1. **Egg**: Laid singly just above water surface; resistant to desiccation for months to years; laid in batches of 100–200 per bloodmeal; dark brown/black, ribbed surface; ~0.5 mm.
2. **Larva (4 instars)**: Aquatic; 5–7 days at 25°C; filter-feeder on microorganisms and organic detritus; breathes via siphon at water surface; highly sensitive to larvicides (Bti, temephos).
3. **Pupa**: Aquatic, comma-shaped; non-feeding; 2–3 days; buoyant; metamorphosis occurs.
4. **Adult**: Emerges from pupal case; feeds on plant nectar (energy); females require a **blood meal** for egg development (gonotrophic cycle).

**Key trait: Preferred breeding habitat** — small, stagnant, typically clean water containers:
- Flower vases, water storage containers, roof gutters, discarded tires, plant saucers, bottle caps, construction debris
- Unlike Anopheles (natural water bodies) or *Ae. albopictus* (peri-domestic/forest), *Ae. aegypti* exploits entirely man-made microhabitats

## Infection Mechanism

### Arboviral Transmission Cycle

*Ae. aegypti* transmits arboviruses via a **biological transmission** mechanism (not mechanical):

1. **Bloodmeal acquisition (infection)**: Female mosquito feeds on viremic human; ingests blood containing virus particles.
2. **Midgut infection**: Virus must cross the midgut epithelium, replicate, and escape into the hemocoel — the **midgut escape barrier** is a key determinant of vector competence.
3. **Dissemination**: Virus spreads through hemolymph to secondary tissues (fat body, muscle, trachea).
4. **Salivary gland infection**: Virus must infect and replicate in salivary glands; the **salivary gland escape barrier** is the final determinant.
5. **Extrinsic incubation period (EIP)**: Time from bloodmeal to transmission competence. Dengue: **8–12 days at 28°C** (temperature-dependent; shorter at higher temperature); Zika: 7–10 days; Chikungunya: 7–10 days.
6. **Transmission**: During subsequent bloodmeal, infective saliva is injected into human host; virus-laden saliva also contains vasodilators and anticoagulants that facilitate feeding.

### Vector Competence and Specificity

*Ae. aegypti* is **not universally susceptible** to all arboviruses. It shows high vector competence for dengue, Zika, chikungunya, and yellow fever due to evolved receptor-ligand compatibility and permissive midgut cells. Competence is modulated by:
- **Endogenous microbiome**: Commensal bacteria affect midgut susceptibility
- **Temperature**: EIP and replication rate both inversely proportional to temperature
- **Wolbachia symbiont** (experimental): *wMel* strain of *Wolbachia* introduced into *Ae. aegypti* blocks dengue, Zika, and chikungunya replication by ~40–70%; basis of the **World Mosquito Program** biocontrol intervention [^moreira-2009-wolbachia]

### Biting Behavior

| Characteristic | Detail |
|:---|:---|
| **Biting time** | **Diurnal** (day-biting): peaks 2–3 h after sunrise and 2–3 h before sunset; unlike malaria vector *Anopheles* (nocturnal) |
| **Host preference** | Strongly anthropophilic (humans over animals); genetic differences between African and cosmopolitan populations in host preference |
| **Feeding pattern** | Often feeds multiple times per gonotrophic cycle (interrupted feeding) — significantly increasing transmission risk |
| **Flight range** | Typically < 200 m from breeding site; dispersal via transport of eggs/adults in goods |

## Host Interactions

### Human Host

Humans are the **amplifying host** for dengue, Zika, and chikungunya — the mosquito acquires virus from viremic humans and transmits to susceptible humans (human-mosquito-human cycle). Yellow fever also has a sylvatic cycle (non-human primates).

The mosquito's **saliva** modulates the human immune response at the inoculation site:
- Salivary proteins suppress dendritic cell activation and NK cell function
- Vasoactive amines (apyrase, AAPP) facilitate bloodmeal acquisition
- This immunosuppression may enhance initial viral replication at the inoculation site

### Control Strategies

| Strategy | Mechanism | Efficacy/Status |
|:---|:---|:---|
| **Larviciding** | Bacillus thuringiensis israelensis (Bti), temephos → kill larvae in water | High efficacy if access to containers; community compliance required |
| **Indoor residual spraying** | Pyrethroids, organophosphates on indoor surfaces | Moderate; limited by insecticide resistance (kdr mutations in *vgsc* gene) |
| **Source reduction** | Eliminate/cover water containers | Community-level; reduces breeding sites; cornerstone of urban control |
| **Wolbachia release** | *wMel*-carrying mosquitoes self-sustain in wild population; block arboviral replication | Field trials (Indonesia, Brazil, Australia): ~77% dengue reduction (NEJM 2021) |
| **Sterile Insect Technique (SIT)** | Male-only irradiated/genetically sterile mosquitoes released; wild females mate unproductively → population suppression | Oxitec OX513A: male-only releases; population reduction 90–95% in field trials |
| **Dengvaxia (CYD-TDV)** | Tetravalent dengue vaccine; approved for seropositive individuals ≥9 y; reduces severe disease | Reduces vector-transmissible dengue burden in endemic regions |

## Connections

- `targets` → **[Dengue virus](../../01-viruses/dengue-virus/README.md)** — primary biological vector; virus replicates in midgut and salivary glands after 8–12 day extrinsic incubation; ~390 million dengue infections/year attributable to *Ae. aegypti*
- `targets` → **[Zika Virus (ZIKV)](../../01-viruses/zika-virus/README.md)** — primary vector of the 2015–2016 Americas Zika epidemic; salivary transmission following 7–10 day extrinsic incubation

## Pathology

### Impact as a Disease Vector

*Ae. aegypti* itself does not cause direct disease in humans; its pathological significance is entirely as a **biological vector** amplifying and transmitting arboviruses at pandemic scale:

| Disease | Annual burden | Geographic range |
|:---|:---|:---|
| **Dengue** | ~390 million infections; ~20,000 deaths | >128 countries; 3.9 billion at risk |
| **Zika** | 1.5 million cases in 2015–2016 epidemic; congenital microcephaly | Americas, Southeast Asia, Pacific |
| **Chikungunya** | ~3–4 million cases/year; incapacitating arthralgia | Africa, Asia, Americas, Europe (imported) |
| **Yellow fever** | ~200,000 cases, ~30,000 deaths/year | Sub-Saharan Africa (90% of cases), South America |

### Climate and Urbanization

Climate change is expanding the geographic range of *Ae. aegypti* northward and to higher altitudes. Urban population growth increases breeding habitat availability (water storage containers). Models project >2 billion additional people entering *Ae. aegypti* range by 2080 under RCP 8.5 climate scenarios, substantially increasing global dengue/Zika/chikungunya risk [^kraemer-2015-aedes-distribution].

### Insecticide Resistance

Widespread pyrethroid resistance (knockdown resistance, *kdr*, via Vssc/voltage-gated sodium channel mutations; also metabolic resistance via CYP450 upregulation) has substantially reduced the efficacy of indoor spraying in many endemic regions, necessitating Wolbachia/SIT-based biological control.

[^bhatt-2013-dengue-global]: Bhatt S et al. The global distribution and burden of dengue. *Nature.* 2013;496(7446):504-507. [doi:10.1038/nature12060](https://doi.org/10.1038/nature12060) · [PubMed 23563266](https://pubmed.ncbi.nlm.nih.gov/23563266/)
[^kraemer-2015-aedes-distribution]: Kraemer MUG et al. The global distribution of the arbovirus vectors Aedes aegypti and Ae. albopictus. *eLife.* 2015;4:e08347. [doi:10.7554/eLife.08347](https://doi.org/10.7554/eLife.08347) · [PubMed 26126267](https://pubmed.ncbi.nlm.nih.gov/26126267/)
[^moreira-2009-wolbachia]: Moreira LA et al. A Wolbachia symbiont in Aedes aegypti limits infection with dengue, Chikungunya, and Plasmodium. *Cell.* 2009;139(7):1268-1278. [doi:10.1016/j.cell.2009.11.042](https://doi.org/10.1016/j.cell.2009.11.042) · [PubMed 20064373](https://pubmed.ncbi.nlm.nih.gov/20064373/)
