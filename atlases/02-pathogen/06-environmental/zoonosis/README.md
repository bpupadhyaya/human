---
schema: pathogen-entry/v1
id: zoonosis
name: Zoonosis
atlas: 02-pathogen
scale: 06-environmental
status: draft
last_reviewed: 2026-06-06
summary: "Infectious disease transmitted from non-human vertebrates to humans. Comprises ~60% of known human pathogens and ~75% of emerging infectious diseases. Spillover occurs at human-animal interfaces. WHO One Health framework addresses zoonotic risk."
aliases: ["zoonotic disease", "zoonoses", "zoonotic infection", "animal-to-human transmission", "spillover infection"]
sources:
  - id: jones-2008-emerging-infectious
    type: peer-reviewed
    cite: "Jones KE, Patel NG, Levy MA, et al. Global trends in emerging infectious diseases. Nature. 2008;451(7181):990-993."
    doi: "10.1038/nature06536"
    pmid: "18288193"
    url: "https://doi.org/10.1038/nature06536"
  - id: woolhouse-2005-zoonoses
    type: peer-reviewed
    cite: "Woolhouse MEJ, Gowtage-Sequeria S. Host range and emerging and reemerging pathogens. Emerg Infect Dis. 2005;11(12):1842-1847."
    doi: "10.3201/eid1112.050997"
    pmid: "16485468"
    url: "https://doi.org/10.3201/eid1112.050997"
  - id: who-one-health
    type: regulatory
    cite: "World Health Organization. One Health. WHO; 2023."
    url: "https://www.who.int/news-room/questions-and-answers/item/one-health"
cross_links:
  - target: 02-pathogen/01-viruses/ebola-virus
    relation: targets
    note: "Ebola virus (EBOV) is a zoonosis with fruit bat reservoir (Pteropodidae); spillover to humans and non-human primates via contact with infected animals or their bodily fluids; causes hemorrhagic fever with CFR 25-90%."
  - target: 02-pathogen/01-viruses/influenza-a
    relation: targets
    note: "Influenza A is a classic zoonosis with avian and swine reservoirs; antigenic shift via reassortment of gene segments between animal strains generates novel pandemic viruses (e.g. 1918 H1N1, 2009 pH1N1) to which humans lack immunity."
  - target: 02-pathogen/01-viruses/sars-cov-2
    relation: targets
    note: "SARS-CoV-2 is a bat-origin betacoronavirus that spilled over to humans, likely via an intermediate host, initiating the COVID-19 pandemic. Zoonotic origin established by phylogenetic relatedness to bat coronaviruses (RaTG13, ~96% identity)."
---

# Zoonosis

## Overview

A **zoonosis** (plural: zoonoses; from Greek *zōon* = animal + *nosos* = disease) is an infectious disease that is naturally transmitted between non-human vertebrate animals and humans. This includes direct transmission (animal bite, contact with blood/tissues/urine), indirect transmission (environmental contamination, fomites), and vector-borne transmission (arthropod intermediaries such as ticks, mosquitoes, or fleas).

The epidemiological significance of zoonoses is enormous:
- **~60%** of all known human infectious disease pathogens are zoonotic in origin [^woolhouse-2005-zoonoses]
- **~75%** of emerging infectious diseases (EIDs) since 1940 have zoonotic origins [^jones-2008-emerging-infectious]
- Every major pandemic of the 20th–21st centuries (1918 influenza, HIV/AIDS, SARS, MERS, Ebola epidemics, COVID-19) originated as a zoonotic spillover event

The WHO **One Health** framework recognizes that human, animal, and environmental health are inextricably linked — and that preventing zoonotic spillover requires integrated surveillance and intervention across all three domains [^who-one-health].

## Structure

### Classification by Reservoir

| Reservoir type | Example pathogens | Transmission route |
|:---|:---|:---|
| **Wildlife** | Ebola (fruit bats), rabies (bats/foxes/dogs), Nipah (bats), COVID-19 (bats) | Direct contact, aerosol, vector |
| **Domestic animals (livestock)** | Brucellosis (cattle/goats), Q fever (cattle), anthrax (cattle/sheep), Salmonella | Contact, foodborne, aerosol |
| **Companion animals** | Rabies (dogs), ringworm, MRSA, Campylobacter | Direct contact, bite |
| **Rodents** | Plague (rodents/fleas), leptospirosis, hantavirus, Lassa fever | Urine/feces, bite, flea vector |
| **Birds (avian)** | Influenza A (H5N1, H7N9), Campylobacter, Salmonella, Chlamydophila psittaci | Respiratory, foodborne |
| **Non-human primates** | HIV (chimpanzee SIVcpz origin), Ebola, monkeypox | Direct contact, bushmeat |

### Types of Zoonotic Pathogens

| Category | Examples |
|:---|:---|
| **Viruses** | Rabies, Ebola, SARS-CoV-2, influenza A, Hendra, Nipah, yellow fever, West Nile, monkeypox |
| **Bacteria** | Brucella, Yersinia pestis (plague), Borrelia burgdorferi (Lyme), Salmonella, Leptospira, Coxiella burnetii |
| **Fungi** | Cryptococcus gattii (birds), histoplasmosis (bats/birds), ringworm (many animals) |
| **Parasites** | Toxoplasma gondii (cats), Echinococcus (dogs/sheep), Trichinella (pigs), Toxocara (dogs/cats) |
| **Prions** | Bovine spongiform encephalopathy (BSE → vCJD in humans) |

## Infection Mechanism

### The Spillover Process

Zoonotic spillover follows a stepwise process that is not guaranteed to result in epidemic spread:

1. **Reservoir maintenance**: The pathogen circulates sustainably in its animal reservoir population, causing minimal pathology in reservoir hosts (often due to co-evolution).
2. **Exposure event**: A human comes into contact with an infected animal, its tissues, fluids, or vector. Key exposures: wildlife hunting/butchering ("bushmeat"), agricultural settings, wet markets, deforestation-driven habitat encroachment, veterinary work.
3. **Initial infection (spillover)**: The pathogen crosses the species barrier; requires receptor compatibility at the molecular level (e.g., SARS-CoV-2 spike affinity for human ACE2) and capacity to evade innate immune responses in the new host.
4. **Human-to-human transmission (epidemic potential)**: Most spillovers result in dead-end infections (Ebola spillovers without human-to-human propagation) or limited chains. Pandemic potential requires sustained human-to-human transmission (R₀ > 1 in humans).

### Molecular Basis of Host Range

The ability of an animal pathogen to infect humans depends on:
- **Receptor compatibility**: Viral surface proteins must bind human cell surface receptors (e.g., influenza HA must cleave sialic acids accessible in the human respiratory tract; SARS-CoV-2 spike binds human ACE2 with high affinity)
- **Intracellular replication machinery**: Compatibility with human transcription/translation factors
- **Innate immune evasion**: Ability to suppress human IFN-α/β, complement, or pattern recognition receptor signaling
- **Protease activation**: Viral surface proteins often require host proteases for activation (influenza HA requires TMPRSS2 or furin; SARS-CoV-2 spike has both TMPRSS2 and furin sites)

### Risk Factors for Spillover

Epidemiological drivers that increase zoonotic spillover frequency [^jones-2008-emerging-infectious]:

| Driver | Mechanism |
|:---|:---|
| **Deforestation and land-use change** | Human encroachment into wildlife habitat → increased human-wildlife contact at forest edges |
| **Intensive animal agriculture** | Dense livestock populations → amplifying host for avian influenza, swine-origin pathogens; antibiotic pressure driving resistance |
| **Wildlife trade and wet markets** | Multiple species in close proximity → increased interspecies transmission; ideal mixing vessel for influenza reassortment |
| **Urbanization** | Dense human populations amplify any successful spillover into epidemic/pandemic |
| **International travel** | Rapid global dissemination of spillover events (e.g., SARS 2003 spread from Guangdong to 29 countries in weeks) |
| **Climate change** | Expanding geographic ranges of vector species (Aedes, Anopheles, Ixodes); changing reservoir animal distributions |

## Host Interactions

### One Health Framework

The WHO One Health approach recognizes that zoonotic risks emerge at the intersection of human, animal, and environmental health and requires coordinated surveillance [^who-one-health]:

- **Human health sector**: Clinical surveillance, outbreak detection, vaccine development
- **Animal health sector (veterinary)**: Animal disease surveillance (WAHIS/OIE), vaccination of domestic animals, wildlife monitoring
- **Environmental sector**: Ecosystem surveillance, biodiversity monitoring, land-use policy

**Key surveillance networks**:
- PREDICT (USAID-funded): Wildlife sampling for novel pathogens in high-risk interfaces across Africa, Asia
- Global Virome Project: Systematic discovery of unknown animal viruses with zoonotic potential
- WHO Event Information Site: Real-time zoonotic event reporting

### Prevention Strategies

| Strategy | Target | Example |
|:---|:---|:---|
| **Vaccination of reservoir/amplifying hosts** | Domestic animals | Rabies vaccination of dogs (eliminates 99% of human rabies globally); brucellosis vaccine for livestock |
| **Vector control** | Arthropod vectors | Tick control reduces Lyme disease; mosquito control reduces arboviral zoonoses |
| **Behavioral change** | Human-animal interface | Avoid bushmeat consumption; PPE in livestock/veterinary settings |
| **Wet market reform** | Mixing vessel elimination | Separation of live animal species; slaughter-free markets |
| **Surveillance and rapid response** | Early detection | GOARN activation; ring vaccination for Ebola (Ervebo); antiviral stockpiling for H5N1 |
| **Pandemic preparedness** | Pre-pandemic | CEPI vaccine platform pre-development for priority zoonotic pathogens (Coalition for Epidemic Preparedness Innovations) |

## Connections

- `targets` → **[Ebola Virus (EBOV)](../../01-viruses/ebola-virus/README.md)** — fruit bat reservoir; spillover to humans and NHPs via direct contact with infected animals; causes hemorrhagic fever with DIC and vascular leak
- `targets` → **[Influenza A virus](../../01-viruses/influenza-a/README.md)** — avian and swine reservoirs; antigenic shift via segment reassortment generates pandemic strains; H5N1 and H7N9 are active spillover threats
- `targets` → **[SARS-CoV-2 (cardiac effects)](../../01-viruses/sars-cov-2/README.md)** — bat-origin betacoronavirus; pandemic spillover event of 2019; exemplifies zoonotic spillover amplified by global travel and dense urban settings

## Pathology

### Historical Zoonotic Pandemics

| Event | Pathogen | Reservoir | Deaths |
|:---|:---|:---|:---|
| **Plague** (Justinian, Black Death, 3rd pandemic) | *Yersinia pestis* | Rodents / fleas | ~50 million (Black Death, 14th c.) |
| **1918 Influenza** | Influenza A H1N1 | Avian/swine | ~50–100 million |
| **HIV/AIDS** | HIV-1 (group M) | Chimpanzee SIVcpz → human | ~40 million deaths (ongoing) |
| **SARS** (2003) | SARS-CoV-1 | Bats → civet cat → human | ~800 deaths |
| **Ebola** (2013–2016 West Africa) | EBOV | Fruit bats | ~11,000 deaths |
| **MERS** (ongoing) | MERS-CoV | Dromedary camels | >800 deaths |
| **COVID-19** | SARS-CoV-2 | Bat → human | >7 million confirmed; ~15–20 million excess |

### Economic Impact

Zoonotic diseases impose enormous economic burden beyond mortality:
- The 2001 UK foot-and-mouth epidemic (FMD, not human-pathogenic) cost ~£8 billion
- SARS 2003: ~$40 billion GDP loss in affected regions
- COVID-19: >$12 trillion in global GDP contraction (2020–2021)
- **Lost agricultural productivity** from endemic zoonoses (brucellosis, tuberculosis, Newcastle disease) exceeds $20 billion annually in developing countries

### Emerging Threats

Actively monitored high-risk zoonotic pathogens with pandemic potential (WHO R&D Blueprint 2023):
- **H5N1 influenza** (recent cattle/poultry outbreaks, 2024–2025 U.S. dairy herds)
- **Nipah virus** (bat reservoir; recurring Kerala outbreaks; CFR 40–75%; no approved vaccine)
- **Disease X** (unknown future zoonotic pathogen; CEPI preparedness platform)

[^jones-2008-emerging-infectious]: Jones KE et al. Global trends in emerging infectious diseases. *Nature.* 2008;451(7181):990-993. [doi:10.1038/nature06536](https://doi.org/10.1038/nature06536) · [PubMed 18288193](https://pubmed.ncbi.nlm.nih.gov/18288193/)
[^woolhouse-2005-zoonoses]: Woolhouse MEJ, Gowtage-Sequeria S. Host range and emerging and reemerging pathogens. *Emerg Infect Dis.* 2005;11(12):1842-1847. [doi:10.3201/eid1112.050997](https://doi.org/10.3201/eid1112.050997) · [PubMed 16485468](https://pubmed.ncbi.nlm.nih.gov/16485468/)
[^who-one-health]: World Health Organization. One Health. WHO; 2023. [who.int/news-room](https://www.who.int/news-room/questions-and-answers/item/one-health)
