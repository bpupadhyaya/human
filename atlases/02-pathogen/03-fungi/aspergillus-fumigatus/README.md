---
schema: pathogen-entry/v1
id: aspergillus-fumigatus
name: Aspergillus fumigatus
atlas: 02-pathogen
scale: 03-fungi
status: draft
last_reviewed: 2026-06-05
summary: "Ubiquitous saprophytic mould; conidia (2–3 µm) inhaled by all humans daily. Primary human pathogen via airways. Causes allergic bronchopulmonary aspergillosis, aspergilloma, and invasive pulmonary aspergillosis (mortality 40–90%) in neutropenic or corticosteroid-treated hosts."
aliases: ["A. fumigatus", "aspergillus", "IPA causative agent"]
sources:
  - id: latge-2020-aspergillus-review
    type: peer-reviewed
    cite: "Latge JP, Chamilos G. Aspergillus fumigatus and aspergillosis in 2019. Clin Microbiol Rev. 2020;33(1):e00140-18."
    doi: "10.1128/CMR.00140-18"
    pmid: "31722890"
    url: "https://doi.org/10.1128/CMR.00140-18"
  - id: patterson-2016-aspergillosis-guideline
    type: peer-reviewed
    cite: "Patterson TF, Thompson GR, Denning DW, et al. Practice guidelines for the diagnosis and management of aspergillosis. Clin Infect Dis. 2016;63(4):e1-60."
    doi: "10.1093/cid/ciw326"
    pmid: "27365388"
    url: "https://doi.org/10.1093/cid/ciw326"
cross_links:
  - target: 01-human/07-system/immune-system
    relation: infects
    note: "Immunocompromised patients — with deficient neutrophil or macrophage function — are at high risk for invasive aspergillosis. Conidia evade phagocyte killing via RodA hydrophobin surface masking of β-glucan, gliotoxin-mediated neutrophil/macrophage apoptosis, and catalase/superoxide dismutase-mediated ROS neutralisation."
  - target: 01-human/07-system/respiratory-system
    relation: damages
    note: "Inhaled conidia lodge in alveoli and, in immunocompromised hosts, germinate to form hyphae that invade the pulmonary parenchyma. Invasive pulmonary aspergillosis causes angioinvasion, thrombosis, and haemorrhagic infarction. Radiographic hallmarks include the halo sign, air-crescent sign, and cavitation."
  - target: 01-human/04-cellular/dendritic-cell
    relation: damages
    note: "A. fumigatus impairs dendritic cell maturation and IL-12 production, skewing toward a tolerogenic response. Gliotoxin directly suppresses DC function by inhibiting NF-κB, blocking costimulatory molecule upregulation (CD80, CD86) and impairing T-cell priming — a key immune evasion mechanism in invasive aspergillosis."
  - target: 01-human/06-organ/lung
    relation: damages
    note: "A. fumigatus is the dominant mould pathogen of the lung; conidia germinate to hyphae in neutropenic hosts within 6-12h; angioinvasion → thrombosis and haemorrhagic infarction; CT halo sign (early) and air-crescent sign (recovery); IPA mortality 40-90%."
  - target: 01-human/05-tissue/alveolus
    relation: damages
    note: "Conidia (2-3 µm) deposit in terminal alveoli due to aerodynamic size; alveolar macrophages phagocytose via Dectin-1 within 4-8h in immunocompetent hosts; in neutropenic hosts, RodA hydrophobin shields conidia from Dectin-1 → germination → hyphal invasion of alveolar walls."
---

# Aspergillus fumigatus

## Overview

*Aspergillus fumigatus* is a **ubiquitous, thermotolerant saprophytic mould** found in decaying organic matter worldwide. It is the most important mould pathogen of humans and is responsible for the vast majority of cases of **invasive aspergillosis** — the leading mould infection in immunocompromised patients. Remarkably, *A. fumigatus* is encountered by virtually all humans daily: an average person inhales several hundred to thousands of airborne conidia every day. In immunocompetent individuals, this constant exposure is cleared efficiently by the innate immune system; in immunocompromised hosts, it causes rapidly progressive, frequently fatal disease [^latge-2020-aspergillus-review].

*Aspergillus fumigatus* causes a **clinical spectrum** spanning from non-invasive to profoundly invasive disease:
- **Allergic bronchopulmonary aspergillosis (ABPA):** Hypersensitivity to *A. fumigatus* antigens in asthma and cystic fibrosis patients
- **Aspergilloma (fungal ball):** Non-invasive colonisation of pre-existing pulmonary cavities
- **Subacute/chronic pulmonary aspergillosis (CCPA/CNPA):** Slowly progressive destruction in mildly immunosuppressed patients
- **Invasive pulmonary aspergillosis (IPA):** Rapidly progressive angioinvasive infection in profoundly immunosuppressed hosts; mortality 40–90% depending on host

Global burden estimates suggest **250,000 cases of invasive aspergillosis** annually, with ~180,000 attributable deaths [^patterson-2016-aspergillosis-guideline]. The majority of cases occur in patients with haematological malignancies, recipients of haematopoietic stem cell transplants (HSCT), solid organ transplant recipients, and those on prolonged corticosteroid therapy. Critically ill COVID-19 patients developed a distinct entity — **COVID-19-associated pulmonary aspergillosis (CAPA)** — recognised since 2020.

## Structure

### Conidial and Hyphal Morphology

*A. fumigatus* is a filamentous fungus that grows as **multicellular hyphae** (4–6 µm diameter) with regular septation and dichotomous 45° branching — the classic radiological and pathological hallmark distinguishing *Aspergillus* from mucormycoses (non-septate, wide-angle branching). In culture, it produces characteristic **conidiophores**: a stalk with a flask-shaped vesicle bearing a single row of phialides that bud off chains of **conidia (2–3 µm diameter)** — small enough to penetrate to the alveolar level on inhalation.

| Structure | Size | Significance |
|:---|:---|:---|
| **Conidia** | 2–3 µm | Airborne infectious units; thermostable; inhaled daily by all humans |
| **Hyphae** | 4–6 µm width | Tissue-invasive form; angioinvasive; antifungal-treated tissue shows hyphal clearance |
| **Conidiophore** | ~300 µm stalk | Sporulating structure in environment; single row of phialides (uniseriate) |
| **Asexual conidia chain** | Chains of 20–100+ conidia | Released upon physical disturbance; dominant transmission route |

### Cell Wall

The conidial cell wall has unique properties that facilitate immune evasion:
- **RodA hydrophobin layer:** The outermost layer of resting conidia is coated by RodA — a self-assembling hydrophobic protein that shields immunogenic β-glucan and chitin from pattern recognition receptors (PRRs), especially Dectin-1. This masking allows conidia to reside briefly in airways without triggering full immune activation
- **β-1,3-glucan:** Exposed during germination; activates Dectin-1 on macrophages and neutrophils → strong pro-inflammatory response against germinating conidia
- **Galactomannan (GM) and galactofuranose:** Cell wall polysaccharides shed during active growth → circulate in blood/urine as biomarkers for invasive aspergillosis (Platelia GM ELISA test)
- **Dihydroxynaphthalene (DHN)-melanin:** Present in conidia; quenches superoxide radicals from phagocyte NADPH oxidase, conferring phagocyte resistance

### Virulence Factors

| Factor | Gene/Product | Mechanism |
|:---|:---|:---|
| **Gliotoxin** | *gli* cluster | Mycotoxin; induces apoptosis in macrophages/neutrophils via caspase activation; inhibits NF-κB in DCs; suppresses T-cell activation |
| **Fumagillin** | *fma* cluster | Inhibits MetAP2 (methionine aminopeptidase 2); anti-angiogenic; contributes to vascular invasion |
| **Proteases (Alp1, Alp2, Pep1, Mep)** | Multiple secreted protease genes | Degrade elastin, laminin, fibronectin; facilitate tissue invasion; cleave complement proteins |
| **Siderophores (TAFC, FSME)** | *sid* gene cluster | Iron acquisition from host transferrin/lactoferrin; essential for virulence |
| **RodA hydrophobin** | *rodA* | Conidial surface masking; immune evasion at initial contact |

### Genome

- **Genome size:** ~29.4 Mb; haploid; 8 chromosomes; ~9,900 predicted genes (Af293 reference)
- Sexual cycle: **heterothallic** (MAT1-1 and MAT1-2 mating types identified); cryptic sexual reproduction produces ascospores
- Rich secondary metabolite gene clusters (>40): gliotoxin, fumagillin, pseurotin A, helvolic acid
- Resistance mutations: *cyp51A* mutations (L98H with tandem repeat TR34/L98H the dominant azole resistance mechanism; also G54R, G138C, M220)

## Infection Mechanism

### Conidial Inhalation and Alveolar Deposition

1. **Inhalation:** Conidia are released from decaying organic matter (compost, soil, building debris, hospital HEPA filter failures). Their aerodynamic diameter (2–3 µm) allows passage through the upper airways and bronchial tree to **terminal bronchioles and alveoli**
2. **Alveolar clearance (immunocompetent):** Alveolar macrophages rapidly phagocytose conidia via pattern recognition receptors (Dectin-1, TLR2, TLR4, complement receptors CR3/CR4). Non-opsonised conidial clearance occurs within 4–8 hours. If the macrophage burden is exceeded, recruited neutrophils provide additional killing via oxidative burst and NETs
3. **Failed clearance (immunocompromised):** With neutropenia or macrophage impairment (corticosteroids suppress oxidative burst), conidia **germinate** — transitioning from dormant 2–3 µm spheres to actively growing 4–6 µm hyphae within 6–12 hours at 37°C

### Hyphal Invasion and Angioinvasion

The transition to invasive disease follows a stereotyped progression:

1. **Germination:** Swelling (isotropic growth) → polarised growth → germ tube emergence → hypha elongation. β-glucan is exposed on the germinating surface, now triggering Dectin-1 recognition — but neutrophil and macrophage effector function is impaired by the underlying immunosuppression
2. **Tissue penetration:** Hyphae secrete proteases (alkaline proteases, metalloprotease Mep) that degrade the alveolar basement membrane and extracellular matrix (elastin, laminin, fibronectin)
3. **Angioinvasion:** Hyphae penetrate vessel walls (this is distinctive of *Aspergillus* and distinguishes it from mucormycetes which are also angioinvasive). Intravascular growth → **thrombosis and infarction** of pulmonary parenchyma
4. **Haematogenous dissemination:** Less common than in candidiasis but occurs in profoundly immunosuppressed patients — brain, kidneys, liver, and heart are secondary sites

### Conidial-Specific Virulence

Resting conidia are thermotolerant (grow at up to 55°C vs. other *Aspergillus* spp. limited to 37–42°C) — contributing to *A. fumigatus* being the dominant human-pathogenic *Aspergillus* species. Conidia can withstand UV radiation, desiccation, and mild chemical disinfectants.

## Host Interactions

### Innate Immune Defence

In immunocompetent hosts, multilayered innate defence is highly effective:

| Defence layer | Mechanism | Efficiency |
|:---|:---|:---|
| **Mucociliary escalator** | Traps conidia >5 µm in upper airways; ciliary beating removes them | Handles most large particles |
| **Alveolar macrophages** | Dectin-1/TLR phagocytosis → phagolysosomal killing | Handles routine conidial load |
| **Recruited neutrophils** | NADPH oxidase (ROS), MPO-halide, NETs | Essential for hyphal killing — absent in neutropenia |
| **Dendritic cells** | β-glucan/mannan sensing → IL-12 → Th1; furanomycin → IL-23 → Th17 | Links innate to adaptive |
| **Complement** | Classical and alternative pathway opsonisation → enhanced phagocytosis | Amplifies macrophage/neutrophil killing |

### Immune Evasion

| Mechanism | Detail |
|:---|:---|
| **RodA masking** | Shields β-glucan, delays Dectin-1 activation on resting conidia |
| **DHN-melanin** | Quenches phagocyte-generated reactive oxygen species (ROS); inhibits phagosome acidification |
| **Gliotoxin secretion** | Induces macrophage and neutrophil apoptosis; inhibits NF-κB in DCs; prevents T cell activation |
| **Catalase (Cat1, Cat2)** and **SOD (SodA, SodB/SodC)** | Neutralise H₂O₂ and superoxide from NADPH oxidase; *cat*/*sod* double mutants are highly attenuated in neutropenic models |
| **Complement evasion** | Proteases cleave C3b/C5a; conidial surface modulates complement activation |
| **DC functional suppression** | Gliotoxin and fumagillin impair DC maturation, reduce IL-12 output, and prevent CD80/CD86 upregulation → impaired Th1 and Th17 priming |

### Adaptive Immune Interaction

In immunocompetent hosts, adaptive immunity is important for long-term control:
- **Th1 (IFN-γ):** Activates alveolar macrophages to enhanced killing; driven by DC-derived IL-12 in response to β-glucan and mannan
- **Th17 (IL-17A/F):** Recruits neutrophils and promotes epithelial antimicrobial peptide production; important in ABPA regulation
- **Treg:** Excessive Treg responses (IL-10, TGF-β) correlate with worse outcomes in IPA; gliotoxin promotes Treg-like states by suppressing effector T cells
- In ABPA, sensitisation to *A. fumigatus* allergens (Asp f1–6) drives IgE-mediated and eosinophilic inflammation — the immune response causes the disease

### Cytokine Profile

- **Protective:** IL-12, IFN-γ (Th1 macrophage activation); IL-17A, IL-22 (Th17 neutrophil recruitment); GM-CSF (neutrophil/macrophage enhancement)
- **Pathological in ABPA:** IL-4, IL-5, IL-13 (Th2 IgE class switching, eosinophilia, mucus production); IL-33, TSLP (epithelial alarmins)
- **Pathological in IPA:** TNF-α, IL-1β, IL-6 (excessive inflammation in recovering patients); paradoxically, IFN-γ deficiency is common in IPA patients

## Connections

- `infects` → **[Immune System](../../../01-human/07-system/immune-system/README.md)** — archetypical opportunistic pathogen; conidia suppress DC maturation via gliotoxin → impaired Th1/Th17 priming; virtually harmless in immunocompetent hosts; rapidly lethal when neutrophil or macrophage function is compromised.
- `damages` → **[Respiratory System](../../../01-human/07-system/respiratory-system/README.md)** — exclusive airway portal; IPA destroys alveolar parenchyma via hyphal angioinvasion and ischaemic infarction; ABPA causes bronchiectasis and mucoid impaction via IgE/eosinophil-driven hypersensitivity; dominant mould of the respiratory tract.
- `damages` → **[Dendritic Cell](../../../01-human/04-cellular/dendritic-cell/README.md)** — gliotoxin induces DC apoptosis, inhibits NF-κB, blocks CD80/CD86 upregulation and IL-12 secretion → tolerogenic skewing; prevents effective Th1/Th17 priming — key persistence mechanism in immunosuppressed hosts.
- `damages` → **[Lung](../../../01-human/06-organ/lung/README.md)** — dominant mould pathogen of the lung; conidia germinate to hyphae in neutropenic hosts within 6-12h; angioinvasion → thrombosis and haemorrhagic infarction; CT halo sign (early) and air-crescent sign (recovery); IPA mortality 40-90%.
- `damages` → **[Alveolus](../../../01-human/05-tissue/alveolus/README.md)** — conidia (2-3 µm) deposit in terminal alveoli; alveolar macrophages phagocytose via Dectin-1 within 4-8h; in neutropenic hosts, RodA hydrophobin shields conidia from Dectin-1 → germination → hyphal invasion of alveolar walls.

## Pathology

### Clinical Disease Spectrum

| Disease | Population | Key Features | Mortality |
|:---|:---|:---|:---|
| **Allergic bronchopulmonary aspergillosis (ABPA)** | Asthma (1–2%), cystic fibrosis (2–15%) | IgE >1000 kU/L; peripheral eosinophilia; fleeting pulmonary infiltrates; central bronchiectasis; mucoid impaction | Low (quality of life impact) |
| **Aspergilloma (fungus ball)** | Patients with TB cavities, sarcoidosis, bronchiectasis | Moveable intracavitary mass on CT; haemoptysis (can be massive); positive serum precipitins | Haemoptysis-related: 5–15% |
| **Subacute/chronic pulmonary aspergillosis** | Mildly immunosuppressed (low-dose steroids, COPD, prior TB) | Slowly progressive over months to years; weight loss, cough, haemoptysis; cavitation, nodules | ~40% at 1 year if untreated |
| **Invasive pulmonary aspergillosis (IPA)** | Neutropenia, HSCT, SOT, high-dose steroids, COVID-19-associated | Fever unresponsive to antibacterials; pleuritic chest pain; haemoptysis; CT halo sign → air-crescent sign | 40–90% |
| **Tracheobronchitis** | Lung transplant recipients, AIDS | Ulcerative or pseudomembranous tracheobronchitis; airway obstruction; bronchial anastomosis involvement post-transplant | High without early treatment |
| **Disseminated aspergillosis** | Profound prolonged neutropenia, HSCT | CNS (cerebral aspergillosis: infarction, abscess, meningitis); endocarditis; osteomyelitis | >90% |
| **Azole-resistant IPA** | Any IPA patient; especially in TR34/L98H-endemic regions (Europe, South/East Asia) | TR34/L98H *cyp51A* mutation; environmental azole exposure | Worse prognosis than azole-sensitive |

### Diagnosis

- **CT chest:** Halo sign (ground-glass halo around dense nodule = haemorrhagic infarction) is early and sensitive in neutropenic patients; air-crescent sign (late, as neutrophils recover) is highly specific
- **Galactomannan (GM) index:** Serum GM ELISA (Platelia) — sensitivity ~60–80% in neutropenic IPA; specificity ~80–90%; useful for monitoring treatment response
- **Beta-D-glucan:** Pan-fungal marker; elevated in IPA and candidiasis; less specific
- **Bronchoscopy with BAL:** BAL GM (cut-off index ≥1.0) is more sensitive than serum; culture positive in ~50% of IPA (low sensitivity)
- **Molecular (PCR):** Blood and BAL *A. fumigatus* PCR increasingly used; excellent sensitivity, can detect azole-resistance mutations directly

### Treatment

- **Voriconazole** (triazole, CYP51 inhibitor): First-line for IPA; superior to amphotericin B in landmark 2002 trial; monitor plasma levels
- **Isavuconazole:** Alternative triazole; better tolerability than voriconazole; active against azole-resistant strains with some *cyp51A* mutations
- **Liposomal amphotericin B (L-AMB):** Alternative first-line; preferred when drug interactions contraindicate azoles; significant nephrotoxicity with conventional formulation
- **Echinocandins:** Caspofungin/micafungin as salvage monotherapy or in combination with voriconazole; *A. fumigatus* β-glucan synthase (*fks1*) mutations conferring echinocandin resistance are rare
- **Surgery:** Resection of localised aspergilloma causing haemoptysis; debridement of CNS aspergillosis when accessible; bronchial stent/laser for obstructive tracheobronchitis
- **ABPA:** Systemic corticosteroids (reduce inflammation) + itraconazole/voriconazole (reduce fungal burden and steroid requirement)

[^latge-2020-aspergillus-review]: Latge JP, Chamilos G. *Aspergillus fumigatus* and aspergillosis in 2019. *Clin Microbiol Rev.* 2020;33(1):e00140-18. [doi:10.1128/CMR.00140-18](https://doi.org/10.1128/CMR.00140-18) · [PubMed 31722890](https://pubmed.ncbi.nlm.nih.gov/31722890/)
[^patterson-2016-aspergillosis-guideline]: Patterson TF, Thompson GR, Denning DW, et al. Practice guidelines for the diagnosis and management of aspergillosis. *Clin Infect Dis.* 2016;63(4):e1-60. [doi:10.1093/cid/ciw326](https://doi.org/10.1093/cid/ciw326) · [PubMed 27365388](https://pubmed.ncbi.nlm.nih.gov/27365388/)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
