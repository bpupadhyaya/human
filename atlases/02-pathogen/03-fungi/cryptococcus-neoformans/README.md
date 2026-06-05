---
schema: pathogen-entry/v1
id: cryptococcus-neoformans
name: Cryptococcus neoformans
atlas: 02-pathogen
scale: 03-fungi
status: draft
last_reviewed: 2026-06-05
summary: "Basidiomycete yeast pathogen with a unique polysaccharide capsule (glucuronoxylomannan) enabling immune evasion. Causes life-threatening cryptococcal meningitis, particularly in HIV/AIDS patients with CD4 <100. ~180,000 deaths annually worldwide."
aliases: ["C. neoformans", "cryptococcus", "cryptococcal meningitis", "Torula histolytica"]
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
  - id: perfect-2010-cryptococcosis
    type: peer-reviewed
    cite: "Perfect JR, Dismukes WE, Dromer F, et al. Clinical practice guidelines for the management of cryptococcal disease: 2010 update. Clin Infect Dis. 2010;50(3):291-322."
    doi: "10.1086/649858"
    pmid: "20047480"
    url: "https://doi.org/10.1086/649858"
  - id: rajasingham-2017-global-burden
    type: peer-reviewed
    cite: "Rajasingham R, Smith RM, Park BJ, et al. Global burden of disease of HIV-associated cryptococcal meningitis: an updated analysis. Lancet Infect Dis. 2017;17(8):873-881."
    doi: "10.1016/S1473-3099(17)30243-8"
    pmid: "28483415"
    url: "https://doi.org/10.1016/S1473-3099(17)30243-8"
cross_links:
  - target: 01-human/06-organ/brain
    relation: damages
    note: "Cryptococcal meningitis establishes in the CNS via hematogenous spread. ICP elevation from polysaccharide accumulation in CSF is the primary driver of mortality; serial lumbar punctures or VP shunting are life-saving in refractory raised ICP."
  - target: 01-human/07-system/nervous-system
    relation: damages
    note: "Cryptococcal meningoencephalitis is the dominant CNS manifestation. Neurological sequelae (hydrocephalus, cranial nerve palsies, cognitive decline) result from direct fungal invasion and polysaccharide-driven elevation of intracranial pressure."
  - target: 01-human/07-system/immune-system
    relation: damages
    note: "GXM capsule suppresses T-cell activation, inhibits complement, and paralyses macrophages, enabling CNS colonisation in CD4 <100 HIV patients. Post-ART immune reconstitution inflammatory syndrome (IRIS) can paradoxically worsen neurological outcomes."
  - target: 01-human/04-cellular/macrophage
    relation: damages
    note: "Intracellular yeast survive phagolysosomal killing via melanin, urease-driven alkalinisation, and anti-apoptotic signalling, then cross the blood-brain barrier inside macrophages — the classical Trojan horse mechanism of CNS dissemination."
---

# Cryptococcus neoformans

## Overview

*Cryptococcus neoformans* is an **encapsulated Basidiomycete yeast** and the leading cause of fungal meningitis worldwide. Unlike most human fungal pathogens that exploit immune deficiency opportunistically, *C. neoformans* carries a uniquely sophisticated virulence arsenal — centred on its **massive polysaccharide capsule** — that allows it to survive and propagate within host phagocytes and cross the blood-brain barrier [^perfect-2010-cryptococcosis].

The organism is **environmental**, ubiquitously distributed in soil enriched with **pigeon and bird droppings** (which supply nitrogen and creatinine as growth substrates). Exposure occurs globally by inhalation of desiccated yeast cells or spores (basidiospores). After primary pulmonary infection, the organism may enter latency and reactivate decades later when host immunity wanes — a key feature that distinguishes cryptococcosis from purely opportunistic disease. The closely related species *C. gattii* infects immunocompetent hosts, but *C. neoformans* predominantly targets the severely immunocompromised.

Globally, *C. neoformans* causes approximately **1 million cases of cryptococcal meningitis per year**, with an estimated **180,000 deaths annually** — the vast majority in sub-Saharan Africa among HIV-positive individuals with CD4 counts below 100 cells/µL [^rajasingham-2017-global-burden]. It accounts for ~15% of all AIDS-related deaths worldwide, making it one of the most lethal AIDS-defining illnesses. Immunocompromised transplant recipients, patients on prolonged corticosteroids, and those with haematological malignancies represent the other major at-risk groups.

Clinical management combines aggressive antifungal therapy with careful management of **intracranial pressure (ICP)** — a frequently lethal but treatable complication driven by the capsule's ability to obstruct CSF reabsorption.

## Structure

### Morphology

*C. neoformans* exists as an **encapsulated budding yeast** (blastoconidia) under standard laboratory and host conditions. Unlike *Candida*, it does not exhibit classical dimorphism in vivo under routine circumstances, though sexual reproduction on appropriate substrates produces **basidiospores** (2–3 µm) that may be the infectious particle initiating pulmonary disease.

| Feature | Specification |
|:---|:---|
| **Cell body size** | 5–7 µm diameter (yeast form) |
| **Capsule thickness** | 1–30+ µm (can exceed cell body diameter in vivo) |
| **Titan cells** | 5–100 µm; polyploid (up to 4n); formed in alveolar and CNS environments under CO₂ and physiological stress |
| **Colony appearance** | Mucoid, cream-coloured; capsule visible on India ink preparation as clear halo surrounding yeast |
| **Temperature** | Thermotolerant; grows at 37°C (essential virulence determinant) |

**Titan cells** — massive polyploid yeast formed in vivo — are too large for phagocytosis (>10 µm), contribute to immune evasion, and can shed daughter micro-cells that are highly infective.

### Cell Wall Composition

The cell wall is a bilayered structure with an outer polysaccharide capsule overlying the conventional fungal wall:

**Capsule (outer layer — primary virulence determinant):**
- **Glucuronoxylomannan (GXM):** ~90% of capsule mass; a high-molecular-weight (MW up to 10⁷ Da) branched polysaccharide composed of mannose backbone with glucuronic acid and xylose side chains. Serogroups A (most common) and D are defined by GXM structure.
- **Glucuronoxylomannogalactan (GXMGal):** ~10% of capsule; contributes to capsule structural integrity and immunomodulation
- **Mannoproteins:** Embedded in capsule; include MP98, Cda1, Cda2 (chitin deacetylases)

**Inner cell wall:**
- **Chitin** (~3–11% dry weight): structural scaffold; inner layer
- **β-1,3-glucan:** Structural polysaccharide; less prominent than in other fungi
- **α-1,3-glucan:** Outer cell wall component; masks chitin from immune detection
- **Melanin:** Deposited in the cell wall by laccase enzymes (see Virulence Factors below)

### Key Virulence Factors

| Factor | Gene(s) | Mechanism |
|:---|:---|:---|
| **Polysaccharide capsule (GXM)** | *CAP59, CAP60, CAP64, UGD1* | Inhibits phagocytosis; depletes complement (C3 consumption); suppresses T-cell activation; induces IL-10 (immunosuppressive); impairs dendritic cell maturation |
| **Laccase** | *LAC1, LAC2* | Converts host catecholamines (dopamine, epinephrine) → melanin; melanin deposits in cell wall; antioxidant shield (scavenges ROS/RNS); iron acquisition; brain tropism (dopamine-rich regions) |
| **Urease** | *URE1* | Hydrolyses urea → ammonia; alkalinises phagolysosome; promotes CNS penetration via BBB disruption by ammonia |
| **Phospholipase B** | *PLB1* | Degrades phospholipids in lung surfactant; promotes evasion of alveolar defences; assists intracellular survival |
| **Thermotolerance** | *CDC50, HSP90* | Growth at 37°C; essential for human pathogenicity; attenuated strains fail to grow at 37°C |
| **Titan cell formation** | Multiple (CO₂ sensing, mating pathway) | Oversized polyploid cells resist phagocytosis; generate small infective daughter cells via budding |

## Infection Mechanism

### Route of Infection and Initial Pulmonary Colonisation

Infection begins with **inhalation** of desiccated yeast cells (5–7 µm) or basidiospores (2–3 µm, smaller than vegetative cells) from environmental sources. The small particle size allows deep alveolar deposition.

In the alveolus:
1. **Alveolar macrophage engulfment:** Complement (C3b) opsonisation facilitates phagocytosis via CR3/CR4; antibody-mediated uptake via Fcγ receptors is less efficient due to capsule shielding. Non-opsonised yeast are also phagocytosed at lower rates.
2. **Phagolysosomal survival:** Intracellular yeast employ multiple strategies to survive within macrophages (see Host Interactions). In immunocompetent hosts, T-cell-mediated immunity (particularly Th1/CD4+ responses) confines infection to a latent pulmonary granuloma.
3. **Latency establishment:** Latent cryptococcal infection within lung granulomata — analogous to tuberculosis latency — is widely believed to be the source of reactivation disease decades later when CD4 counts fall.

### CNS Dissemination — the Trojan Horse Mechanism

The blood-brain barrier (BBB) crossing is the critical pathogenic step that defines cryptococcal meningoencephalitis:

**Three proposed mechanisms (evidence for all exists):**

| Mechanism | Description |
|:---|:---|
| **Transcellular (direct)** | Free yeast bind and transcytose through brain microvascular endothelial cells (BMVECs) via CD44, HSPG, and other surface receptors |
| **Paracellular** | Urease-generated ammonia disrupts tight junction proteins (claudin-5, occludin) at the BBB, allowing paracellular traversal |
| **Trojan horse** | Intracellular yeast within circulating macrophages or monocytes traverse the BBB during normal immune surveillance; macrophages naturally cross BBB — yeast hitch a ride |

Once in the CNS, *C. neoformans* replicates in the **Virchow-Robin perivascular spaces** and subarachnoid space. Capsular polysaccharide (GXM) is shed in massive amounts into CSF, causing **obstruction of arachnoid villi** and impaired CSF reabsorption → **intracranial hypertension**.

### Brain Tropism — Dopamine and Laccase

*C. neoformans* exhibits a striking affinity for dopamine-rich brain regions (basal ganglia, substantia nigra). Laccase enzymes use dopamine and other catecholamines as substrates to synthesise melanin:

- Dopamine concentrations in basal ganglia (~3 µM) are sufficient to sustain laccase-mediated melanogenesis
- Melanin provides structural protection against oxidative and nitrosative killing and chelates iron from host transferrin
- The high dopamine-to-norepinephrine ratio in the brain (compared to peripheral tissues) likely explains preferential CNS localisation of cryptococcal infection

## Host Interactions

### Innate Immune Evasion

The GXM capsule is the master immune evasion molecule:

| Mechanism | Molecular Detail |
|:---|:---|
| **Anti-phagocytic** | GXM steric hindrance reduces phagocytic receptor access; GXM binds FcγRIIB (inhibitory Fc receptor) on macrophages → suppressed phagocytosis |
| **Complement evasion** | GXM binds and consumes complement proteins without generating opsonic C3b fragments efficiently; shed GXM acts as a "decoy" consuming serum complement away from the cell surface |
| **Dendritic cell paralysis** | GXM binding to TLR4 and FcγRIII on DCs drives IL-10 production and suppresses IL-12; impaired DC maturation prevents effective T-cell priming |
| **NK cell inhibition** | Shed GXM inhibits NK cell cytotoxicity; impairs NK-DC crosstalk needed for early IFN-γ production |

### Macrophage Interaction — Intracellular Pathogenesis

*C. neoformans* is an **intracellular pathogen** that subverts the very cell meant to destroy it:

1. **Phagolysosome alkalinisation:** Urease hydrolyses urea → NH₃ + CO₂; ammonia raises phagolysosomal pH from ~5 to ~6.5, impairing lysosomal hydrolase activity; cryptococcal growth optimum is pH 5.5–6.5 (coincidentally matching partially alkalinised phagolysosomes)
2. **Laccase-melanin shield:** Melanin deposited in cell wall scavenges ROS and RNS from the oxidative burst; melanised cells survive macrophage killing at dramatically higher rates than unmelanised mutants
3. **Anti-apoptotic signalling:** *C. neoformans* upregulates macrophage Bcl-2 family anti-apoptotic proteins, preventing caspase-3 activation and macrophage death that would release the yeast into a hostile environment
4. **Vomocytosis (non-lytic exocytosis):** Viable intracellular yeast are expelled from live macrophages without cell lysis — a unique escape mechanism that preserves macrophage integrity for further Trojan horse dissemination
5. **Intracellular replication:** Doubling time in macrophage phagosomes (~6 hours) is comparable to in vitro doubling time — infection amplifies intracellularly

### Adaptive Immune Response

**Th1-polarised CD4+ T-cell immunity** is the dominant protective adaptive response:

- Alveolar macrophages and DCs present cryptococcal antigens via MHC-II → CD4+ Th1 cells produce **IFN-γ** → macrophage classical activation (M1) → enhanced fungicidal activity
- Cryptococcal-specific CD4+ T cells are detected in seropositive immunocompetent individuals (evidence of controlled exposure)
- **CD4 depletion below 100 cells/µL** (HIV/AIDS) removes the Th1 effector arm, converting latent infection to disseminated lethal disease
- Humoral immunity plays a secondary role: capsule-specific IgG antibodies can opsonise via Fcγ receptors and activate complement; the monoclonal antibody 18B7 (discontinued) demonstrated proof-of-concept benefit

**Immune reconstitution inflammatory syndrome (IRIS) post-ART:**
- Paradoxical IRIS: existing cryptococcal disease worsens after ART initiation due to rapid recovery of Th1 cells attacking a large fungal burden
- Manifests as worsening CNS inflammation, new pulmonary infiltrates, lymphadenitis
- Management: corticosteroids (prednisolone) reduce IRIS severity without impairing antifungal efficacy

## Connections

**Damages** → [Brain](../../../01-human/06-organ/brain/README.md): Cryptococcal meningitis is established via hematogenous dissemination to the CNS. Polysaccharide accumulation in CSF obstructs arachnoid villi, driving intracranial hypertension — the dominant proximate cause of death. Serial therapeutic lumbar punctures or ventriculoperitoneal (VP) shunting are critical ICP management strategies in severe or refractory disease.

**Damages** → [Nervous system](../../../01-human/07-system/nervous-system/README.md): Cryptococcal meningoencephalitis can produce lasting neurological injury including hydrocephalus, cranial nerve palsies (II, III, VI, VII, VIII), cognitive decline, and cryptococcomas (mass lesions). Direct neuronal toxicity from GXM and ammonia, combined with ICP-driven ischemia, contributes to sequelae even after microbiological cure.

**Damages** → [Immune system](../../../01-human/07-system/immune-system/README.md): GXM capsule actively disables innate and adaptive arms of immunity by inhibiting phagocytosis, consuming complement, driving IL-10 production, and suppressing DC maturation. In CD4 <100 HIV patients, these evasion strategies go unopposed, enabling uncontrolled CNS colonisation. Post-ART IRIS reflects paradoxical immune re-engagement against a large fungal burden.

**Damages** → [Macrophage](../../../01-human/04-cellular/macrophage/README.md): Intracellular yeast survive phagolysosomal killing via melanin, urease-driven alkalinisation, and anti-apoptotic signalling, then traverse the blood-brain barrier inside macrophages via vomocytosis and re-entry — the canonical Trojan horse mechanism of cryptococcal CNS dissemination.

## Pathology

### Clinical Presentation

*C. neoformans* infection spans a spectrum from **asymptomatic pulmonary colonisation** to **fatal meningoencephalitis**:

| Syndrome | Clinical Features | Population |
|:---|:---|:---|
| **Asymptomatic pulmonary** | Incidental finding; solitary nodule or focal infiltrate on imaging | Immunocompetent; detected on CT |
| **Pulmonary cryptococcosis** | Fever, cough, pleuritic chest pain; lobar consolidation or miliary pattern; may progress to ARDS in immunocompromised | Solid organ transplant; hematologic malignancy |
| **Cryptococcal meningitis** | Insidious onset over 1–2 weeks: headache (>90%), fever (>70%), meningismus (variable — may be absent), altered consciousness, papilloedema, visual changes, cranial nerve palsies | HIV CD4 <100 (majority); transplant recipients |
| **Cryptococcaemia** | Fever, often without focal signs; seed all organs; may present as ARDS, peritonitis, skin lesions (umbilicated, molluscum-like papules) | Any severely immunocompromised host |
| **Cryptococcoma** | CNS mass lesion; headache, focal neurological deficit, seizures; may mimic cerebral toxoplasmosis or primary CNS lymphoma | HIV/AIDS; steroid-treated patients |
| **Disseminated (skin)** | Umbilicated papules resembling molluscum contagiosum; often marker of disseminated disease; biopsy reveals encapsulated yeast | HIV CD4 <50 |

### Epidemiology

- **~1 million cases** of cryptococcal meningitis annually; **~180,000 deaths/year** (predominantly sub-Saharan Africa) [^rajasingham-2017-global-burden]
- HIV accounts for **>80%** of all cryptococcal meningitis cases worldwide
- *C. neoformans* var. grubii (serotype A): cosmopolitan; the predominant cause in HIV patients
- *C. neoformans* var. neoformans (serotype D): Europe; slightly less virulent; more often affects other immunocompromised hosts
- *C. gattii* (serotype B/C): tropical/subtropical; infects immunocompetent hosts; Vancouver Island/Pacific Northwest outbreak (2000s)

### Diagnosis

**CSF analysis — the cornerstone of diagnosis:**

| Test | Finding | Sensitivity |
|:---|:---|:---|
| **India ink preparation** | Clear halo (capsule) around yeast; direct visualisation | 50–90% (HIV); lower in non-HIV |
| **Cryptococcal antigen (CrAg) — latex agglutination or LFA** | Detects GXM in CSF and serum | >95% sensitivity in HIV-associated cryptococcal meningitis; gold standard |
| **Fungal culture (CSF, blood)** | Mucoid colonies on Sabouraud agar; growth within 72 hours | Gold standard for confirmation and susceptibility |
| **Opening pressure** | Elevated (>25 cm H₂O) in >75% of HIV patients; may exceed 40 cm H₂O | — |
| **CSF profile** | Typically: mild lymphocytic pleocytosis (or pauci-cellular in advanced HIV); elevated protein; low glucose | Variable |

**Serum CrAg screening** is recommended for HIV patients with CD4 <100 entering care — pre-emptive fluconazole if positive prevents progression to meningitis.

### Treatment

Treatment is divided into three phases per IDSA 2010 guidelines [^perfect-2010-cryptococcosis]:

**1. Induction (2 weeks):**
- **Amphotericin B deoxycholate** 0.7–1.0 mg/kg/day IV **+** **5-flucytosine (5-FC)** 100 mg/kg/day PO (in 4 divided doses)
- Liposomal amphotericin B (3–4 mg/kg/day) preferred when available (less nephrotoxicity)
- Synergy between amphotericin B (membrane disruption → increased 5-FC uptake) and 5-FC (inhibits DNA/RNA synthesis via flucytosine → fluorouracil → thymidylate synthase inhibition) is essential — combination significantly superior to monotherapy

**2. Consolidation (8 weeks):**
- **Fluconazole** 400 mg/day PO
- Bridges gap until immune reconstitution (HIV) or immunosuppression reduction (transplant)

**3. Maintenance (12+ months):**
- **Fluconazole** 200 mg/day PO
- Continue until CD4 >100 cells/µL sustained on ART for ≥3 months (HIV patients)

**Intracranial Pressure Management — critical, life-saving:**
- Therapeutic lumbar punctures (LP): remove CSF to opening pressure target <20 cm H₂O; repeat daily or every other day until pressure controlled
- Lumbar drain or VP shunt for refractory elevated ICP
- **Corticosteroids are NOT recommended** for ICP management (worsened outcomes in COAT trial)
- ICP management reduces 2-week mortality in cryptococcal meningitis by ~40%

**ART timing in HIV:** Defer ART initiation by **4–6 weeks** after antifungal induction — early ART (<2 weeks) increases IRIS-related mortality (ACTG 5164 / COAT trial evidence).

**Azole resistance:** Emerging *ERG11* mutations (Y145F, G484S) and efflux pump overexpression (AFR1 upregulation) compromise fluconazole maintenance therapy; susceptibility testing recommended for treatment failures.

---

*This page is co-maintained by human expert review and AI-assisted synthesis. Content reflects published medical literature as of 2026-06-05 and should not be used as clinical guidance. See [equalinformation.com/human](https://equalinformation.com/human) for project details; contact bpupadhyaya@gmail.com.*

[^perfect-2010-cryptococcosis]: Perfect JR, Dismukes WE, Dromer F, et al. Clinical practice guidelines for the management of cryptococcal disease: 2010 update. *Clin Infect Dis.* 2010;50(3):291-322. [doi:10.1086/649858](https://doi.org/10.1086/649858) · [PubMed 20047480](https://pubmed.ncbi.nlm.nih.gov/20047480/)
[^rajasingham-2017-global-burden]: Rajasingham R, Smith RM, Park BJ, et al. Global burden of disease of HIV-associated cryptococcal meningitis: an updated analysis. *Lancet Infect Dis.* 2017;17(8):873-881. [doi:10.1016/S1473-3099(17)30243-8](https://doi.org/10.1016/S1473-3099(17)30243-8) · [PubMed 28483415](https://pubmed.ncbi.nlm.nih.gov/28483415/)
[^mandell-principles]: Bennett JE, Dolin R, Blaser MJ. *Mandell, Douglas, and Bennett's Principles and Practice of Infectious Diseases.* 9th ed. Elsevier; 2020.
[^murray-microbiology]: Murray PR, Rosenthal KS, Pfaller MA. *Medical Microbiology.* 9th ed. Elsevier; 2021.
