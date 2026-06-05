---
schema: pathogen-entry/v1
id: candida-albicans
name: Candida albicans
atlas: 02-pathogen
scale: 03-fungi
status: draft
last_reviewed: 2026-06-05
summary: "Diploid dimorphic fungus; most common human fungal pathogen. Commensal of oral mucosa, GI tract, vagina (25% carriage). Yeast-to-hypha transition is virulence switch. Causes thrush, vulvovaginal candidiasis, and invasive candidiasis (mortality 40–60%) in immunocompromised hosts."
aliases: ["C. albicans", "monilia", "thrush", "candida"]
sources:
  - id: kullberg-2015-invasive-fungal
    type: peer-reviewed
    cite: "Kullberg BJ, Arendrup MC. Invasive fungal disease in the patient with hematologic malignancy. Hematology Am Soc Hematol Educ Program. 2015;2015:385-92."
    doi: "10.1182/asheducation-2015.1.385"
    pmid: "26637749"
    url: "https://doi.org/10.1182/asheducation-2015.1.385"
  - id: gow-2017-candida-profile
    type: peer-reviewed
    cite: "Gow NAR, Yadav B. Microbe profile: Candida albicans: a shape-changing, opportunistic pathogenic fungus of humans. Microbiology. 2017;163(8):1145-7."
    doi: "10.1099/mic.0.000499"
    pmid: "28792889"
    url: "https://doi.org/10.1099/mic.0.000499"
  - id: pappas-2016-candidiasis-guideline
    type: peer-reviewed
    cite: "Pappas PG, Kauffman CA, Andes DR, et al. Clinical practice guideline for the management of candidiasis: 2016 update. Clin Infect Dis. 2016;62(4):e1-50."
    doi: "10.1093/cid/civ933"
    pmid: "26679628"
    url: "https://doi.org/10.1093/cid/civ933"
cross_links:
  - target: 01-human/04-cellular/dendritic-cell
    relation: infects
    note: "Skin and mucosal dendritic cells are primary innate sensors of Candida. C-type lectin receptors Dectin-1 and Dectin-2 on DCs recognise β-glucan and α-mannans respectively on the fungal surface, triggering NF-κB and CARD9/BCL10/MALT1 signalling to drive Th17 differentiation — the dominant protective response against mucosal candidiasis."
  - target: 01-human/07-system/immune-system
    relation: damages
    note: "Systemic candidiasis exploits immunocompromised states. C. albicans evades phagocytosis via hyphal escape, biofilm formation, and secretion of candidalysin (hyphal toxin). It induces IL-10 production and suppresses the Th17 response — the primary adaptive defence — allowing mucosal and systemic invasion."
  - target: 01-human/06-organ/liver
    relation: damages
    note: "Hepatosplenic candidiasis (chronic disseminated candidiasis) occurs in neutropenic patients recovering from haematological malignancy treatment. Candida seeds the liver and spleen during neutropenia; granulomas form as neutrophils recover. Presents as persistent fever with hepatosplenomegaly and rising alkaline phosphatase."
---

# Candida albicans

## Overview

*Candida albicans* is a **diploid, dimorphic fungus** of the phylum Ascomycota and the most prevalent human fungal pathogen. It occupies a dual ecological role: a **commensal** coloniser of the oral mucosa, gastrointestinal tract, and vaginal epithelium in approximately 25% of healthy adults, and an **opportunistic pathogen** capable of causing life-threatening invasive disease when host defences fail [^gow-2017-candida-profile].

Globally, *C. albicans* causes an estimated **750,000 cases of invasive candidiasis** annually — primarily candidaemia (bloodstream infection), intra-abdominal candidiasis, and disseminated candidiasis. Case-fatality rates for invasive candidiasis range from **40–60%** even with appropriate antifungal therapy, placing it among the most lethal hospital-acquired infections [^kullberg-2015-invasive-fungal]. Superficial forms (oral thrush, vulvovaginal candidiasis) affect hundreds of millions: vulvovaginal candidiasis alone affects ~75% of women at least once during their lifetime.

Key risk factors for invasive disease include haematological malignancy, bone marrow/solid organ transplantation, prolonged neutropenia, broad-spectrum antibiotics (loss of bacterial competition), central venous catheters, abdominal surgery, parenteral nutrition, corticosteroid use, and HIV/AIDS. The emergence of **azole-resistant** and **echinocandin-resistant** strains poses a growing therapeutic challenge [^pappas-2016-candidiasis-guideline].

## Structure

### Morphology and Dimorphism

*C. albicans* exists in three principal morphological forms, and the ability to switch between them — **dimorphism** — is its central virulence strategy:

| Form | Description | Context |
|:---|:---|:---|
| **Budding yeast (blastoconidia)** | Oval cells, 3–6 µm; reproduce by budding | Commensal growth; bloodstream dissemination |
| **Pseudohyphae** | Chains of elongated yeast cells that remain attached; incomplete septation | Intermediate invasive state |
| **True hyphae** | Parallel-walled filamentous cells; germ tube initiates within 2–4 h at 37°C and neutral pH; septa with no constriction | Tissue invasion, biofilm formation; the virulent phase |

The yeast-to-hypha transition is controlled by a network of transcription factors (Efg1, Cph1) responding to temperature (37°C), neutral pH, serum, CO₂, and the Ras1-cAMP-Pka1 and MAP-kinase pathways. In hyphae, **candidalysin** (a 31-amino-acid amphipathic peptide toxin encoded by *ECE1*) is expressed and secreted — it perforates epithelial cell membranes to initiate invasion.

### Cell Wall

The *C. albicans* cell wall is a dynamic, layered structure (~100–200 nm thick) essential for viability, morphogenesis, and immune interaction:

- **Inner skeletal layer:** β-1,3-glucan and β-1,6-glucan polymers cross-linked to chitin (N-acetylglucosamine chains); provide mechanical strength; β-glucan is the dominant PAMP (pathogen-associated molecular pattern) recognised by Dectin-1 on host immune cells
- **Outer mannoprotein layer:** Heavily glycosylated GPI (glycosylphosphatidylinositol)-anchored proteins; α-mannans project outward and are recognised by Dectin-2, mannose receptor, and DC-SIGN; mask inner β-glucan from Dectin-1 in yeast form
- Hyphae expose β-glucan at the hyphal tip — accounting for the greater immunogenicity of invasive hyphal forms

### Genome

- **Genome size:** ~28 Mb; **8 chromosome pairs** (diploid); high heterozygosity
- Lacks a complete meiotic cycle under normal conditions (parasexual cycle via loss of heterozygosity under stress)
- ~6,200 open reading frames; notable gene families: ALS (agglutinin-like sequence) adhesins (8 members), SAP (secreted aspartyl protease) family (10 members), LIP (lipase) family
- **White-opaque switching:** Epigenetic phenotypic switching between white (round) and opaque (elongated) cell types affects mating competence and tissue tropism

## Infection Mechanism

### Colonisation to Invasion

*C. albicans* transitions from commensal to pathogen via a **sequential invasion cascade** driven by host immune compromise:

1. **Colonisation:** Yeast adhere to epithelial surfaces via Als (agglutinin-like sequence) adhesins (especially Als3) binding to E-cadherin and N-cadherin on host epithelial cells, and via Hwp1 (hyphal wall protein 1) — a substrate for host transglutaminase — providing covalent attachment in hyphal form
2. **Epithelial penetration:** Hyphal transition triggered by epithelial contact. Candidalysin (Ece1-derived peptide) disrupts epithelial membrane integrity. Invasion occurs by two mechanisms: **induced endocytosis** (Als3/Ssa1 bind E-cadherin/EGFR → clathrin-mediated uptake) and **active penetration** (physical force of hyphal extension)
3. **Subepithelial dissemination:** Hyphae traverse the basement membrane and lamina propria, reaching dermal blood vessels or draining lymphatics
4. **Haematogenous spread:** Yeast form (smaller, more resistant to physical shear) circulates in blood; adheres to vascular endothelium via Als3 binding VE-cadherin; re-invades as hyphae in target organs

### Biofilm Formation

*C. albicans* forms structured, antifungal-resistant **biofilms** on indwelling medical devices (central venous catheters, urinary catheters, prosthetic valves):

- Biofilm architecture: yeast basal layer → pseudohyphal/hyphal network → extracellular matrix (β-1,3-glucan, mannoproteins, eDNA)
- Biofilm β-glucan sequesters fluconazole and echinocandins, reducing effective drug concentrations 1,000-fold
- Cells dispersed from biofilms seed new infection foci — the primary mechanism of catheter-related candidaemia

## Host Interactions

### Innate Immune Response

| Immune cell | Receptor | Response |
|:---|:---|:---|
| **Dendritic cells** | Dectin-1 (β-glucan), Dectin-2 (α-mannan), DC-SIGN | NF-κB activation → IL-6, IL-23 → Th17 polarisation; IL-12 → Th1 polarisation |
| **Macrophages** | Dectin-1, TLR2, mannose receptor | Phagocytosis of yeast; hyphae escape by extending beyond phagosome capacity; candidalysin lyses macrophages |
| **Neutrophils** | Fcγ receptors, complement receptors, Dectin-1 | Oxidative burst (ROS/RNS); NETs (neutrophil extracellular traps) immobilise hyphae; primary defence against invasive candidiasis |

Neutropenia (ANC <500 cells/µL) is the single strongest risk factor for invasive candidiasis — reflecting the absolute dependence on neutrophil killing of *C. albicans* hyphae.

### Adaptive Immune Response and Evasion

The key protective adaptive response is **Th17-driven mucosal immunity**:
- IL-17A and IL-17F from Th17 cells stimulate epithelial cells to produce defensins, calprotectin, and lactoferrin, limiting mucosal colonisation
- Patients with **IL-17 signalling defects** (STAT3 LOF, IL-17RA/IL-17F mutations, anti-IL-17 biologics) develop chronic mucocutaneous candidiasis (CMC) — persistent mucosal candidiasis with normal systemic immunity

**Immune evasion mechanisms:**

| Mechanism | Detail |
|:---|:---|
| **Hyphal escape from phagosomes** | Hyphae physically rupture phagosomal and macrophage membranes, releasing viable fungi |
| **Candidalysin** | Lyses neutrophils and macrophages; activates NLRP3 inflammasome (IL-1β), which paradoxically contributes to immunopathology |
| **IL-10 induction** | *C. albicans* mannoproteins engage DC-SIGN → IL-10 production → Treg expansion → suppressed Th1/Th17 responses |
| **Phenotypic switching** | White-opaque and GUT (gastrointestinally induced transition) phenotypes down-regulate immunogenic surface molecules |
| **Proteolytic cleavage** | SAP (secreted aspartyl proteases) degrade immunoglobulins, complement proteins (C3b), and cell-surface immune receptors |

### Cytokine Profile

*C. albicans* infection triggers a complex cytokine environment that determines mucosal protection vs. systemic immunopathology:
- **Protective (mucosal):** IL-17A, IL-17F, IL-22 (Th17/ILC3) — epithelial barrier reinforcement; IL-12, IFN-γ (Th1) — macrophage activation
- **Pathological (systemic):** IL-1β, IL-6, TNF-α (excessive NF-κB activation) — sepsis-like syndrome; IL-10 (immunosuppression in chronically ill patients)

## Connections

**Infects** → [Dendritic cell](../../../01-human/04-cellular/dendritic-cell/README.md): Mucosal and skin dendritic cells are the primary innate sentinels of *C. albicans*, recognising fungal PAMPs via Dectin-1 and Dectin-2. This interaction is essential for downstream Th17 polarisation that mediates mucosal protection. In invasive candidiasis, *C. albicans* subverts DC function through mannose receptor-mediated IL-10 induction.

**Damages** → [Immune system](../../../01-human/07-system/immune-system/README.md): *C. albicans* exploits immune deficiency — particularly neutropenia and Th17 defects — to cause systemic disease. Conversely, the immune response to disseminated candidiasis can produce a hyperinflammatory state (IRIS in HIV, immune reconstitution in neutropenic patients) that contributes to organ damage.

**Damages** → [Liver](../../../01-human/06-organ/liver/README.md): Hepatosplenic (chronic disseminated) candidiasis is a distinct syndrome of neutropenic recovery — Candida seeded the liver and spleen during neutropenia forms granulomas as immune function recovers, manifesting as persistent febrile illness with hepatosplenomegaly and elevated alkaline phosphatase.

## Pathology

### Disease Spectrum

| Disease | Population | Clinical Features | Mortality |
|:---|:---|:---|:---|
| **Oral candidiasis (thrush)** | HIV/AIDS (CD4 <200), denture wearers, inhaled corticosteroids, dry mouth | White removable plaques on erythematous oral mucosa; dysphagia if oesophageal | <1% (superficial) |
| **Oesophageal candidiasis** | HIV/AIDS; transplant recipients | Dysphagia, odynophagia; linear white plaques on endoscopy; AIDS-defining illness | <5% |
| **Vulvovaginal candidiasis (VVC)** | Healthy women (75% lifetime risk); precipitated by antibiotics, pregnancy, diabetes | Thick white discharge; pruritus; erythema; dyspareunia | <1% |
| **Candidaemia** | ICU, haematology, transplant patients | Fever unresponsive to antibacterials; often no obvious focus; high-grade bacteraemia equivalent | 40–60% |
| **Invasive candidiasis** | Neutropenic, post-surgical, parenteral nutrition | Multi-organ seeding: endophthalmitis, endocarditis, osteomyelitis, meningitis, hepatosplenic | 40–75% |
| **Hepatosplenic candidiasis** | AML, ALL patients recovering from neutropenia | Persistent fever despite neutrophil recovery; hepatosplenomegaly; elevated ALP; MRI: "bull's-eye" lesions | 30–50% |
| **Chronic mucocutaneous candidiasis** | IL-17 pathway defects (STAT3 LOF, CARD9 deficiency) | Refractory oral/skin/nail candidiasis; normal susceptibility to systemic infection | Low (condition specific) |

### Treatment

- **Fluconazole** (azole: blocks ergosterol synthesis via CYP51/Erg11) — first-line for non-critical candidiasis; resistance via *ERG11* mutation (Y132F, K143R) or CDR1/MDR1 efflux pump upregulation
- **Echinocandins** (caspofungin, micafungin, anidulafungin: inhibit β-1,3-glucan synthase/Fks1) — first-line for invasive candidiasis, candidaemia, and azole-resistant strains; *FKS1* mutations confer resistance
- **Amphotericin B** (polyene: binds ergosterol → membrane pores → ion leakage) — reserved for refractory cases; significant nephrotoxicity
- **Catheter removal** essential in candidaemia: reduces mortality and shortens candidaemia duration significantly [^pappas-2016-candidiasis-guideline]

[^kullberg-2015-invasive-fungal]: Kullberg BJ, Arendrup MC. Invasive fungal disease in the patient with hematologic malignancy. *Hematology Am Soc Hematol Educ Program.* 2015;2015:385-92. [doi:10.1182/asheducation-2015.1.385](https://doi.org/10.1182/asheducation-2015.1.385) · [PubMed 26637749](https://pubmed.ncbi.nlm.nih.gov/26637749/)
[^gow-2017-candida-profile]: Gow NAR, Yadav B. Microbe profile: *Candida albicans*: a shape-changing, opportunistic pathogenic fungus of humans. *Microbiology.* 2017;163(8):1145-7. [doi:10.1099/mic.0.000499](https://doi.org/10.1099/mic.0.000499) · [PubMed 28792889](https://pubmed.ncbi.nlm.nih.gov/28792889/)
[^pappas-2016-candidiasis-guideline]: Pappas PG, Kauffman CA, Andes DR, et al. Clinical practice guideline for the management of candidiasis: 2016 update. *Clin Infect Dis.* 2016;62(4):e1-50. [doi:10.1093/cid/civ933](https://doi.org/10.1093/cid/civ933) · [PubMed 26679628](https://pubmed.ncbi.nlm.nih.gov/26679628/)
