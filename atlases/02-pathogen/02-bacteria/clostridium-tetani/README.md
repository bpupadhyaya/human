---
schema: pathogen-entry/v1
id: clostridium-tetani
name: Clostridium tetani
atlas: 02-pathogen
scale: 02-bacteria
status: active
last_reviewed: 2026-06-05
summary: "Anaerobic, spore-forming, Gram-positive rod. Produces tetanospasmin (TeNT), a zinc-metalloprotease that cleaves VAMP-2 in inhibitory interneurons, blocking GABA/glycine release causing spastic paralysis. 100% preventable by tetanus toxoid vaccination."
taxonomy:
  family: Clostridiaceae
  genus: Clostridium
  species: Clostridium tetani
genome:
  type: DNA
  description: "2.8 Mb chromosome + 74 kb plasmid (pE88) encoding tetanospasmin (tetX gene) and tetanolysin (tetZ gene)"
replication_site: "Anaerobic wound environment (deep puncture wounds, necrotic tissue, umbilical stumps); organism does not disseminate — toxin alone causes systemic disease"
transmission:
  - wound contamination by soil/dust/feces containing spores
  - puncture wounds (nails, splinters, needles)
  - crush injuries, burns, surgical wounds (rare)
  - neonatal tetanus (umbilical stump contamination)
  - injection drug use
aliases: ["C. tetani", "tetanus bacillus", "Clostridium tetani Flugge 1881"]
tags: [clostridium, anaerobe, spore-forming, tetanospasmin, tent, vamp2, tetanus, zinc-metalloprotease, toxoid-vaccine, gram-positive]
sources:
  - id: bruggemann-2003-genome
    type: peer-reviewed
    cite: "Brüggemann H, Bäumer S, Fricke WF, et al. The genome sequence of Clostridium tetani, the causative agent of tetanus disease. Proc Natl Acad Sci USA. 2003;100(3):1316-21."
    doi: "10.1073/pnas.0335853100"
    pmid: "12552129"
    url: "https://doi.org/10.1073/pnas.0335853100"
  - id: montecucco-2004-clostridial-toxins
    type: peer-reviewed
    cite: "Montecucco C, Schiavo G. Structure and function of tetanus and botulinum neurotoxins. Q Rev Biophys. 1995;28(4):423-72."
    doi: "10.1017/S0033583500003292"
    pmid: "8771234"
    url: "https://doi.org/10.1017/S0033583500003292"
  - id: popoff-2020-clostridium-review
    type: peer-reviewed
    cite: "Popoff MR. Tetanus in animals. J Vet Diagn Invest. 2020;32(2):184-191."
    doi: "10.1177/1040638720906645"
    pmid: "32089082"
    url: "https://doi.org/10.1177/1040638720906645"
  - id: who-tetanus-2018
    type: regulatory
    cite: "World Health Organization. Tetanus vaccines: WHO position paper, February 2017. Wkly Epidemiol Rec. 2017;92(6):53-76."
    url: "https://www.who.int/publications/i/item/who-wer9206"
    accessed: "2026-06-05"
  - id: chalk-2011-tetanus-treatment
    type: peer-reviewed
    cite: "Chalk CH, Mills KR, Newsom-Davis J. Tetanus. Lancet. 2011. [see also: Rodrigo C, Fernando D, Rajapakse S. Pharmacological management of tetanus: an evidence-based review. Crit Care. 2014;18(2):217.]"
    doi: "10.1186/cc13797"
    pmid: "24661523"
    url: "https://doi.org/10.1186/cc13797"
  - id: lalli-2003-retrograde-transport
    type: peer-reviewed
    cite: "Lalli G, Bohnert S, Deinhardt K, Verastegui C, Schiavo G. The journey of tetanus and botulinum neurotoxins in neurons. Trends Microbiol. 2003;11(9):431-7."
    doi: "10.1016/S0966-842X(03)00210-5"
    pmid: "12948668"
    url: "https://doi.org/10.1016/S0966-842X(03)00210-5"
cross_links:
  - target: 01-human/04-cellular/neuron
    relation: damages
    note: "TeNT undergoes retrograde axonal transport to inhibitory interneurons; VAMP-2 cleavage blocks GABA and glycine vesicle release, removing inhibitory control of α-motor neurons and causing spastic rigidity and trismus."
  - target: 01-human/07-system/nervous-system
    relation: damages
    note: "Tetanospasmin blocks inhibitory interneurons throughout the CNS, causing generalised tetanus (risus sardonicus, opisthotonos, autonomic instability); untreated case fatality exceeds 50% in low-resource settings."
  - target: 01-human/07-system/nervous-system
    relation: prevents
    note: "Tetanus toxoid vaccine (DTP/Td/TT) prevents nervous system damage by inducing neutralising IgG against TeNT; a childhood primary series plus boosters maintains protective antibody titres for at least 10 years."
  - target: 01-human/07-system/nervous-system
    relation: treats
    note: "Treatment includes TIG (tetanus immunoglobulin) to neutralise unbound toxin, wound debridement, metronidazole, and ICU supportive care with benzodiazepines to control muscle spasms and prevent respiratory failure."
  - target: 01-human/03-molecular/gaba
    relation: damages
    note: "TeNT LC cleaves VAMP-2 in GABAergic inhibitory interneurons → blocks GABA vesicle fusion → eliminates inhibitory neurotransmission; α-motor neurons fire continuously → spastic paralysis; benzodiazepines (GABA-A potentiators) are first-line symptomatic treatment for tetanus."
  - target: 04-vaccine/06-toxoid/tetanus-toxoid
    relation: prevents
    note: "Tetanus toxoid (formalin-inactivated TeNT) induces neutralising IgG that inactivates TeNT before CNS entry; DTP/DTaP primary series + adult Tdap booster maintain protective antibody titres for ≥10 years; tetanus toxoid is among the most effective vaccines ever developed."
  - target: 01-human/05-tissue/neuromuscular-junction
    relation: damages
    note: "TeNT binds gangliosides at the NMJ → endocytosis → retrograde axonal transport → transcytosis into spinal inhibitory interneurons; NMJ entry is the obligate first step; botulinum toxin remains at the NMJ → flaccid paralysis; TeNT travels centrally → spastic paralysis."
---

# Clostridium tetani

## Overview

*Clostridium tetani* is a **spore-forming, obligate anaerobic, Gram-positive rod** and the causative agent of **tetanus** — a potentially fatal neuromuscular disorder characterised by spastic paralysis. The bacterium itself does not invade tissues or disseminate; disease is caused entirely by a single exotoxin, **tetanospasmin (TeNT)**, which acts on the central nervous system to block inhibitory neurotransmission [^montecucco-2004-clostridial-toxins].

*C. tetani* spores are ubiquitous in soil worldwide — particularly in agriculturally enriched and horse-manured soils — and can survive extreme environmental conditions (heat, desiccation, chemical disinfection) for years. Approximately **50,000 people** die from tetanus annually, with the burden concentrated in low- and middle-income countries (LMICs) where vaccination coverage remains incomplete. Neonatal tetanus — infection of the umbilical stump in newborns of unvaccinated mothers — accounts for a substantial fraction of deaths.

Tetanus is unique among vaccine-preventable diseases in that immunity is entirely **toxin-mediated** (not based on immunity to the bacteria itself). The disease is **100% preventable** through tetanus toxoid immunisation — one of the most effective vaccines in history [^who-tetanus-2018].

The organism was first described by Carle and Rattone (1884) and the toxin was characterised by Knud Faber (1890). The tetanus toxoid vaccine was developed by Gaston Ramon in the 1920s using formaldehyde-inactivated tetanospasmin.

## Structure

### Cell Biology

*C. tetani* is a **slender Gram-positive rod** (0.5–1.7 µm × 2.1–18.1 µm). Its most distinctive morphological feature is the formation of **spherical terminal endospores** that give the cell a characteristic **"drumstick" or "tennis racket" appearance** when stained.

| Feature | Description |
|:---|:---|
| **Cell wall** | Classic Gram-positive thick peptidoglycan layer; no outer membrane; teichoic acids on surface |
| **Spores** | Terminal, spherical endospores; resistant to heat (survive boiling >1 h), desiccation, UV, and most disinfectants; killed by autoclaving (121°C, 15 min) or 2% glutaraldehyde |
| **Flagella** | Peritrichous; motile in early log phase; non-motile in stationary/sporulation phase |
| **Oxygen sensitivity** | Obligate anaerobe; does not grow aerobically; requires redox potential < −50 mV for germination and vegetative growth |

### Genome

The *C. tetani* genome (strain E88) was sequenced in 2003 [^bruggemann-2003-genome]:

- **Chromosome:** 2,799,251 bp; GC content 28.6%
- **Plasmid pE88:** 74,082 bp; harbours the **tetX gene** (tetanospasmin) and **tetZ gene** (tetanolysin)
- 2,617 predicted coding sequences
- The toxin gene is plasmid-encoded — analogous to Shiga toxin (*E. coli* phage) and anthrax toxin (*B. anthracis* pXO1) — and absent in non-toxigenic *C. tetani* strains

### Toxins

*C. tetani* produces two toxins:

1. **Tetanospasmin (TeNT):** The primary neurotoxin; responsible for all clinical manifestations of tetanus; discussed in detail below.
2. **Tetanolysin (TetZ):** A haemolysin; cytolytic to red blood cells and other cells; disrupts tissue locally and may contribute to necrosis at the wound site but is not essential for tetanus disease.

## Infection Mechanism

### Spore Germination and Toxin Production

*C. tetani* infection follows a predictable sequence:

1. **Wound contamination:** Spores enter a wound (puncture, laceration, crush injury, burn, surgical site, umbilical stump). The critical factor is **local anaerobiosis** — created by tissue necrosis, devitalized tissue, coexisting aerobic bacteria consuming oxygen, or foreign bodies (e.g., a nail).
2. **Germination:** Spores germinate in the anaerobic microenvironment → vegetative bacilli begin multiplying.
3. **Toxin synthesis:** Vegetative *C. tetani* synthesises and secretes tetanospasmin as a single-chain precursor (150 kDa); proteolytic nicking (by bacterial protease or trypsin-like enzymes) yields the di-chain active form — a **100 kDa heavy chain (HC)** and **50 kDa light chain (LC)** linked by a disulphide bond.

### Tetanospasmin Structure and Retrograde Transport

Tetanospasmin is a **zinc-dependent metalloprotease** of the clostridial neurotoxin family (same superfamily as botulinum toxins A–G). Its domain architecture [^montecucco-2004-clostridial-toxins]:

| Domain | Chain | Function |
|:---:|:---:|:---|
| **HC-C (C-terminal)** | Heavy chain | Binds gangliosides (GT1b, GD1b) at the presynaptic motor nerve terminal; dictates neurospecific tropism |
| **HC-N (N-terminal)** | Heavy chain | Mediates endosomal translocation of LC into the cytosol |
| **LC (light chain)** | Light chain | Zinc metalloprotease active site; cleaves **VAMP-2 (synaptobrevin-2)** |

After release at the wound, TeNT undergoes:

1. **Binding** at the neuromuscular junction (HC-C binds gangliosides on α-motor nerve terminals)
2. **Endocytosis** into vesicular compartments within motor axon terminals
3. **Retrograde axonal transport** — travelling at ~10 mm/h toward the spinal cord and brainstem via acidic endosomes inside motor axons [^lalli-2003-retrograde-transport]
4. **Transcytosis** into the **inhibitory interneurons** of the spinal cord (Renshaw cells and other GABAergic/glycinergic interneurons) where it exerts its pathological action

### VAMP-2 Cleavage: Molecular Mechanism

In inhibitory interneurons, the light chain (LC) escapes from the endosome (driven by HC-N at low pH) into the cytoplasm. There it acts as a zinc endopeptidase:

- **Substrate:** **VAMP-2 (synaptobrevin-2)** — the v-SNARE protein on synaptic vesicles carrying GABA and glycine
- **Cleavage:** TeNT LC cleaves the Gln⁷⁶–Phe⁷⁷ peptide bond in VAMP-2
- **Effect:** Cleavage prevents SNARE complex formation → synaptic vesicles cannot fuse with the presynaptic membrane → **no neurotransmitter (GABA, glycine) release**

Unlike botulinum toxin (which acts at the neuromuscular junction to block ACh release → flaccid paralysis), tetanospasmin acts centrally to remove inhibitory control → **spastic paralysis**.

## Host Interactions

### Neurophysiology of Tetanus

Normal motor control depends on a balance of excitatory (glutamate) and inhibitory (GABA, glycine) interneurons:

- **Ia inhibitory interneurons** prevent co-contraction of antagonist muscles
- **Renshaw cells** provide recurrent inhibition of motor neurons
- **Glycinergic interneurons** in the brainstem coordinate jaw, facial, and respiratory muscles

TeNT silences these inhibitory circuits → **sustained α-motor neuron firing** → persistent muscle contraction. The clinical consequences:

- **Trismus** ("lockjaw"): Masseter spasm (first manifestation in ~90% of cases)
- **Risus sardonicus:** Facial spasm produces a fixed grin
- **Opisthotonos:** Extensor muscle dominance arches the back
- **Laryngospasm and respiratory failure:** Leading cause of death in untreated tetanus

### Autonomic Instability

Tetanospasmin also impairs inhibitory interneurons in the **sympathetic chain** and **medulla**, causing severe **autonomic dysfunction** (most prominent in the second week):

- Sympathetic hyperactivity: Hypertension, tachycardia, diaphoresis, hyperpyrexia, peripheral vasoconstriction
- Parasympathetic surges: Bradycardia, hypotension, hypersalivation
- Cardiac arrhythmias — a major cause of death in ICU patients
- Autonomic instability is the hardest aspect of tetanus to manage clinically

### Wound Microenvironment

*C. tetani* itself remains localised to the wound and does not cause invasive bacteraemia. The wound may appear relatively clean (incubation period can be 3–21 days). Necrotic tissue, poor blood supply, and coinfecting aerobic bacteria (consuming O₂) maintain the anaerobic niche required for vegetative growth and toxin production.

## Connections

- `damages` → **[Neuron](../../../01-human/04-cellular/neuron/README.md)** — TeNT undergoes retrograde axonal transport to inhibitory interneurons; VAMP-2 cleavage blocks GABA and glycine release, removing inhibitory control of α-motor neurons and causing rigidity and trismus.
- `damages` → **[Nervous System](../../../01-human/07-system/nervous-system/README.md)** — Tetanospasmin blocks inhibitory interneurons throughout the CNS, causing generalised tetanus (risus sardonicus, opisthotonos, autonomic instability); untreated case fatality exceeds 50% in low-resource settings.
- `prevents` → **[Nervous System](../../../01-human/07-system/nervous-system/README.md)** — Tetanus toxoid vaccine induces neutralising IgG against TeNT; childhood primary series (DTP) and boosters maintain protective antibody titres, preventing nervous system damage.
- `treats` → **[Nervous System](../../../01-human/07-system/nervous-system/README.md)** — TIG (tetanus immunoglobulin), wound debridement, metronidazole, and ICU supportive care (benzodiazepines for spasm control) are the treatment pillars once disease occurs.
- `damages` → **[GABA](../../../01-human/03-molecular/gaba/README.md)** — TeNT LC cleaves VAMP-2 in GABAergic inhibitory interneurons → blocks GABA vesicle fusion → eliminates inhibitory neurotransmission; α-motor neurons fire continuously → spastic paralysis; benzodiazepines (GABA-A potentiators) are first-line symptomatic treatment for tetanus.
- `prevents` → **[Tetanus Toxoid](../../../04-vaccine/06-toxoid/tetanus-toxoid/README.md)** — Tetanus toxoid (formalin-inactivated TeNT) induces neutralising IgG that inactivates TeNT before CNS entry; DTP/DTaP primary series + adult Tdap booster maintain protective antibody titres for ≥10 years; tetanus toxoid is among the most effective vaccines ever developed.
- `damages` → **[Neuromuscular Junction](../../../01-human/05-tissue/neuromuscular-junction/README.md)** — TeNT binds gangliosides at the NMJ → endocytosis → retrograde axonal transport → transcytosis into spinal inhibitory interneurons; NMJ entry is the obligate first step; botulinum toxin remains at the NMJ → flaccid paralysis; TeNT travels centrally → spastic paralysis.

## Pathology

### Clinical Classification

| Form | Definition | Key Features |
|:---|:---:|:---|
| **Generalised tetanus** | Most common (~80%) | Descending: trismus → facial spasm (risus sardonicus) → neck stiffness → dysphagia → opisthotonos → intercostal/abdominal rigidity; autonomic instability in severe cases |
| **Localised tetanus** | Muscle rigidity near wound | Usually mild; may progress to generalised; excellent prognosis |
| **Cephalic tetanus** | Head/face wounds | Cranial nerve palsies (especially facial nerve); can progress to generalised |
| **Neonatal tetanus** | Neonate of unvaccinated mother | Typically 3–14 days after birth; inability to suck → generalised spasms; CFR >70% without intensive care |

### Severity Grading — Ablett Classification

| Grade | Features |
|:---:|:---|
| I (mild) | Mild trismus; mild spasticity; no respiratory compromise |
| II (moderate) | Moderate trismus; moderate rigidity; reflex spasms; mild dysphagia/tachycardia |
| III (severe) | Severe trismus; generalised rigidity; prolonged spasms; tachycardia >120; respiratory compromise |
| IV (very severe) | Grade III + severe autonomic instability (hypertension/hypotension cycles, arrhythmias) |

### Incubation and Onset

- **Incubation period:** 3–21 days (range 1 day to several months); shorter incubation correlates with wound proximity to CNS and worse prognosis
- **Period of onset:** Time from first symptom to first generalised spasm; <48 h = severe disease

### Treatment

Management requires **intensive care** and multiple simultaneous interventions [^chalk-2011-tetanus-treatment]:

| Intervention | Rationale |
|:---|:---|
| **Tetanus immunoglobulin (TIG):** 3,000–6,000 U IM | Neutralises unbound toxin in blood; does not reverse already-fixed toxin |
| **Wound debridement** | Eliminates the toxin source |
| **Metronidazole** 500 mg IV/PO q6–8 h × 7–10 days | Kills vegetative *C. tetani*; penicillin historically used but metronidazole is superior |
| **Benzodiazepines** (diazepam, midazolam) | GABA-A agonist; controls muscle spasms; first-line sedation in ICU |
| **Magnesium sulphate** | Reduces sympathetic hyperactivity and spasm frequency; used widely in LMICs |
| **Labetalol / morphine** | Cardiovascular autonomic instability management |
| **Mechanical ventilation** | Respiratory failure from laryngospasm/thoracic rigidity — common indication for intubation |
| **Tracheostomy** | For prolonged ventilatory support |
| **Nutrition** | Nasogastric or parenteral nutrition — high metabolic demands from spasms |

### Vaccine and Prevention

The **tetanus toxoid vaccine** (formalin-inactivated tetanospasmin) is the cornerstone of prevention [^who-tetanus-2018]:

- **Formulations:** DTP (diphtheria, tetanus, pertussis), DTaP (acellular pertussis), Td (adult tetanus-diphtheria), TT (tetanus toxoid alone)
- **Primary series:** 3 doses in infancy → 2 boosters in childhood (DTP at 4–6 years, Tdap at 11–12 years)
- **Duration of protection:** ≥10 years per dose; complete primary series (5 doses) confers lifelong protection in most individuals; boosters recommended every 10 years or after significant wounds
- **Maternal immunisation:** Tdap during each pregnancy boosts maternal IgG → placental transfer to neonate → prevents neonatal tetanus
- **Wound prophylaxis algorithm:** Wound severity and immunisation history determine whether TIG ± booster is needed

**Neonatal tetanus elimination** is achieved when ≥80% of women of reproductive age have ≥2 doses of tetanus toxoid.

### Epidemiology

- **Global incidence:** WHO reported ~49,000 neonatal tetanus deaths in 2013; total tetanus deaths (all ages) estimated ~50,000/year
- **Distribution:** Concentrated in sub-Saharan Africa and South/South-East Asia; rare in countries with high vaccination coverage
- **Herd immunity:** Does NOT apply — tetanus is a toxin-mediated disease, not transmitted person-to-person; every individual must maintain personal immunity
- **Mortality:** With ICU care: ~10–15%; without ICU: >50%; neonatal tetanus without intensive care: ~70–80%

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^bruggemann-2003-genome]: Brüggemann H, Bäumer S, Fricke WF, et al. The genome sequence of Clostridium tetani, the causative agent of tetanus disease. *Proc Natl Acad Sci USA.* 2003;100(3):1316-21. [doi:10.1073/pnas.0335853100](https://doi.org/10.1073/pnas.0335853100) · [PubMed 12552129](https://pubmed.ncbi.nlm.nih.gov/12552129/)
[^montecucco-2004-clostridial-toxins]: Montecucco C, Schiavo G. Structure and function of tetanus and botulinum neurotoxins. *Q Rev Biophys.* 1995;28(4):423-72. [doi:10.1017/S0033583500003292](https://doi.org/10.1017/S0033583500003292) · [PubMed 8771234](https://pubmed.ncbi.nlm.nih.gov/8771234/)
[^popoff-2020-clostridium-review]: Popoff MR. Tetanus in animals. *J Vet Diagn Invest.* 2020;32(2):184-191. [doi:10.1177/1040638720906645](https://doi.org/10.1177/1040638720906645) · [PubMed 32089082](https://pubmed.ncbi.nlm.nih.gov/32089082/)
[^who-tetanus-2018]: World Health Organization. Tetanus vaccines: WHO position paper, February 2017. *Wkly Epidemiol Rec.* 2017;92(6):53-76. [who.int/publications/i/item/who-wer9206](https://www.who.int/publications/i/item/who-wer9206)
[^chalk-2011-tetanus-treatment]: Rodrigo C, Fernando D, Rajapakse S. Pharmacological management of tetanus: an evidence-based review. *Crit Care.* 2014;18(2):217. [doi:10.1186/cc13797](https://doi.org/10.1186/cc13797) · [PubMed 24661523](https://pubmed.ncbi.nlm.nih.gov/24661523/)
[^lalli-2003-retrograde-transport]: Lalli G, Bohnert S, Deinhardt K, Verastegui C, Schiavo G. The journey of tetanus and botulinum neurotoxins in neurons. *Trends Microbiol.* 2003;11(9):431-7. [doi:10.1016/S0966-842X(03)00210-5](https://doi.org/10.1016/S0966-842X(03)00210-5) · [PubMed 12948668](https://pubmed.ncbi.nlm.nih.gov/12948668/)
