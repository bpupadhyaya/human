---
schema: human-scale-entry/v1
id: dengue-fever
name: Dengue Fever
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-08
summary: "Dengue fever (DENV 1-4; Aedes aegypti vector; flavivirus) causes 400M infections annually; NS1/TLR4 → vascular leak; ADE drives dengue hemorrhagic fever in secondary infections; Dengvaxia restricted to seropositive individuals; TAK-003 (Qdenga) approved 2022."
aliases: ["DENV", "dengue", "dengue hemorrhagic fever", "DHF", "dengue shock syndrome", "DSS", "breakbone fever", "Aedes aegypti", "flavivirus dengue", "ADE dengue", "Dengvaxia", "TAK-003"]
sources:
  - id: bhatt-2013-dengue-burden
    type: peer-reviewed
    cite: "Bhatt S, Gething PW, Brady OJ, et al. The global distribution and burden of dengue. Nature. 2013;496(7446):504-507."
    doi: "10.1038/nature12060"
    pmid: "23563266"
    url: "https://doi.org/10.1038/nature12060"
    accessed: "2026-06-08"
  - id: who-2009-dengue-guidelines
    type: clinical-guideline
    cite: "World Health Organization. Dengue: Guidelines for Diagnosis, Treatment, Prevention and Control. Geneva: WHO; 2009."
    url: "https://www.who.int/publications/i/item/9789241547871"
    accessed: "2026-06-08"
cross_links:
  - target: 01-human/03-molecular/mavs
    relation: connects-to
    note: "DENV positive-sense ssRNA activates RIG-I and MDA5 → MAVS → IFN-β; DENV evades MAVS by: NS4B blocking RIG-I signaling, NS2B/NS3 protease disrupting MAVS, NS5 targeting STAT2 for degradation; early robust IFN-β correlates with mild dengue; IFN evasion drives severe disease."
  - target: 01-human/03-molecular/tlr4
    relation: connects-to
    note: "Dengue NS1 protein activates TLR4 on endothelial cells: NS1 hexamer → TLR4/MD-2 → NF-κB → CXCL1, IL-8 → endothelial permeability and plasma leakage; TLR4-mediated NS1 endothelial activation is a key mechanism of dengue hemorrhagic fever; anti-TLR4 may reduce plasma leakage."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Dengue actively evades type I IFN: NS5 targets STAT2 for proteasomal degradation → blocks IFNAR/STAT1/STAT2 signaling; NS2B/NS3 inhibit IRF3; early IFN-β (first 24 h) limits viral replication; delayed IFN induction after immune evasion correlates with severe dengue."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "Dengue evades both RNA (MAVS) and DNA (cGAS-STING) sensing: mitochondrial DNA released during dengue-induced apoptosis → cGAS → cGAMP → STING; however, DENV NS2B/NS3 disrupts STING signaling; dengue-mtDNA-cGAS-STING axis activates inflammatory cytokines during severe dengue."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "DENV NS5 degrades STAT2 via UBR4 → ISGF3 (STAT1/STAT2/IRF9) cannot form → ISG transcription blocked; NS5 selectively targets human STAT2 (not mouse) → human-specific IFN evasion; STAT2 degradation is a major determinant of dengue viremia and is absent in murine dengue models."
---

# Dengue Fever

## Overview

**Dengue fever** is the most prevalent arboviral disease globally, caused by **dengue virus (DENV)** — a positive-sense single-stranded RNA virus of the *Flaviviridae* family (genus *Flavivirus*), with four antigenically distinct serotypes (DENV-1 through DENV-4). Transmitted by the bite of infected *Aedes aegypti* (primary vector) and *Aedes albopictus* mosquitoes, dengue causes an estimated **400 million infections annually** across 128 countries, with ~100 million symptomatic cases and 22,000 deaths, primarily in tropical and subtropical regions [^bhatt-2013-dengue-burden].

The **central immunological challenge** of dengue is the phenomenon of **antibody-dependent enhancement (ADE)**: prior immunity to one DENV serotype does not protect against and can actually exacerbate infection by a different serotype — through subneutralizing antibodies that enhance viral uptake by Fc-receptor-bearing cells (monocytes/macrophages) → higher viral load → more severe disease. This ADE biology has frustrated vaccine development for decades and remains the dominant constraint on dengue vaccine deployment.

**Clinical spectrum:**
- **Dengue fever (DF)**: Fever, severe headache, retro-orbital pain, myalgia/arthralgia ("breakbone fever"), rash; self-limiting ~7 days
- **Dengue hemorrhagic fever (DHF)**: Plasma leakage (hematocrit rise ≥20%, pleural effusion/ascites), thrombocytopenia, hemorrhagic manifestations
- **Dengue shock syndrome (DSS)**: DHF + circulatory failure (narrow pulse pressure or hypotension); mortality ~1-5% with proper management

## Structure

### Dengue virus biology

DENV is a spherical enveloped virus (~50 nm):

- **Genome**: 10.7 kb positive-sense ssRNA; single open reading frame → polyprotein → cleaved into 3 structural + 7 non-structural proteins
- **Structural proteins**:
  - **C (capsid)**: Nucleocapsid core protein
  - **prM/M (precursor membrane/membrane)**: Furin-cleaved during maturation; immature virions (prM) are less infectious
  - **E (envelope)**: Major surface glycoprotein; receptor binding (AXL, DC-SIGN, heparan sulfate); fusion at endosomal pH 5-6; target of neutralizing antibodies
- **Non-structural (NS) proteins**:
  - **NS1**: Secreted hexamer; diagnostic antigen; activates TLR4 on endothelium → plasma leakage; disrupts endothelial junction proteins
  - **NS3/NS2B**: Serine protease (cleaves polyprotein) + RNA helicase; immune evasion (MAVS, STING disruption)
  - **NS5**: RNA-dependent RNA polymerase + cap methyltransferase; degrades STAT2 → IFN evasion

### DENV entry

1. E protein binds DC-SIGN (CD209), AXL, heparan sulfate proteoglycans on dendritic cells and macrophages
2. Clathrin-mediated endocytosis → endosomal acidification → E protein conformational change → membrane fusion → RNA release into cytoplasm
3. DENV replication on ER-derived replication compartments → assembly → budding into ER lumen → Golgi maturation → secretion

## Function

### Immune response timeline

| Phase | Time | Host response | Viral countermeasures |
|-------|------|---------------|----------------------|
| Early innate | 0–24 h | RIG-I/MDA5 → MAVS → IFN-β | NS4B blocks RIG-I; NS2B/NS3 cleaves MAVS |
| Amplification | 24–48 h | pDC IFN-α; NK cell activation; CXCL10 recruitment | NS5 degrades STAT2; JAK-STAT blocked |
| Adaptive | Day 4–7 | Virus-specific CD8+ T cells; neutralizing IgM | Cytokine storm from T cell cross-reactivity |
| Febrile phase | Day 2–7 | Fever, myalgia; viremia peaks Day 4–5 | — |
| Critical phase | Day 4–6 | Plasma leakage (secondary infection); thrombocytopenia | ADE enhances monocyte infection → NS1-TLR4 vascular leak |
| Recovery | Day 6–7+ | Reabsorption of leaked fluid; platelet recovery | — |

### Antibody-dependent enhancement (ADE)

In secondary heterotypic infection (different serotype):

1. Pre-existing non-neutralizing anti-DENV IgG (from previous serotype) binds virions
2. Immune complexes bind Fcγ receptors (FcγRIIA/FcγRI) on monocytes/macrophages → enhanced viral entry
3. Higher viral load in macrophages → increased cytokine production (TNF-α, IL-6, IL-10)
4. IL-10 suppresses antiviral T cell responses → more permissive infection
5. T cell cross-reactivity (original antigenic sin): memory T cells from prior serotype activated → cytokine storm without efficient viral clearance

ADE is most dangerous with DENV-2 secondary to DENV-1 primary infection; explains why DHF and DSS occur predominantly in secondary infections.

## Pathology

### Vascular leak mechanism

Central to DHF/DSS pathogenesis:

- **NS1-TLR4 axis**: Secreted NS1 hexamer → TLR4 on vascular endothelium → NF-κB → CXCL1, IL-8 → endothelial activation; NS1 also disrupts glycocalyx (by activating endothelial sialidase) → junction protein degradation → plasma leakage
- **Complement activation**: NS1 activates complement via C4b-binding protein → C5a → mast cell degranulation → histamine → vascular permeability
- **T cell cytokine storm**: DENV-specific T cells produce IFN-γ, TNF-α, LTA → endothelial activation

### Thrombocytopenia

- Direct BM suppression: DENV infects megakaryocyte precursors → reduced platelet production
- Platelet destruction: Autoantibodies (anti-platelet NS1 antibodies — molecular mimicry); complement-mediated platelet lysis
- Platelet consumption: Endothelial activation → platelet aggregation and consumption

### Diagnosis

- **NS1 antigen RDT**: Positive Day 1–5 (viremic phase); ~80% sensitivity; preferred for febrile phase
- **IgM/IgG serology**: Positive from Day 4; IgG-dominant in secondary infection; dengue NS1 IgG correlates with ADE risk
- **RT-PCR**: Gold standard Day 1–5; not routinely available in endemic regions
- **CBC**: Leukopenia + thrombocytopenia + rising hematocrit = dengue hemorrhagic fever

### Treatment

No approved antiviral therapy for dengue. Management is entirely supportive:

- **Oral hydration** for uncomplicated dengue fever
- **IV crystalloid** (NOT colloid) for plasma leakage; careful fluid balance (risk of fluid overload in recovery phase)
- **Paracetamol** for fever/pain (avoid NSAIDs — antiplatelet effect; avoid corticosteroids — no benefit, potential harm)
- **Platelet transfusion**: Only for active significant bleeding + platelets <20,000/μL; prophylactic transfusion not recommended
- **Critical monitoring**: Hematocrit, urine output, hemodynamic status during critical phase (Day 4–6)

### Vaccines

**Dengvaxia (CYD-TDV; Sanofi Pasteur)**: Live-attenuated chimeric tetravalent (yellow fever backbone + DENV1-4 prM/E). FDA-approved 2019 but **restricted to individuals 9–45 years with documented prior dengue infection** — seronegative recipients had increased severe dengue risk (through ADE mechanism with waning vaccine-induced immunity). Mass vaccination program in Philippines caused public health controversy.

**TAK-003 (Qdenga; Takeda)**: Live-attenuated tetravalent (DENV-2 backbone). EU-approved 2022; WHO prequalified 2023; efficacy 80% against symptomatic dengue (3 years post-vaccination); can be given regardless of prior serostatus (though seropositive recipients have higher protection). Active rollout in endemic countries.

## Connections

**→ [MAVS](../../../03-molecular/mavs/)**: DENV positive-sense ssRNA activates RIG-I and MDA5 → MAVS → IFN-β; DENV evades MAVS by: NS4B blocking RIG-I signaling, NS2B/NS3 protease disrupting MAVS, NS5 targeting STAT2 for degradation; early robust IFN-β correlates with mild dengue; IFN evasion drives severe disease.

**→ [TLR4](../../../03-molecular/tlr4/)**: Dengue NS1 protein activates TLR4 on endothelial cells: NS1 hexamer → TLR4/MD-2 → NF-κB → CXCL1, IL-8 → endothelial permeability and plasma leakage; TLR4-mediated NS1 endothelial activation is a key mechanism of dengue hemorrhagic fever; anti-TLR4 may reduce plasma leakage.

**→ [Type I Interferon](../../../03-molecular/type-i-interferon/)**: Dengue actively evades type I IFN: NS5 targets STAT2 for ubiquitin-mediated degradation → blocks IFNAR-JAK1/TYK2/STAT1/STAT2 signaling; NS2B/NS3 inhibit IRF3; early IFN-β (first 24 h) limits viral replication; delayed IFN induction after immune evasion correlates with severe dengue.

**→ [cGAS-STING](../../../03-molecular/cgas-sting/)**: Dengue evades both RNA (MAVS) and DNA (cGAS-STING) sensing: mitochondrial DNA released during dengue-induced apoptosis → cGAS → cGAMP → STING; however, DENV NS2B/NS3 disrupts STING signaling; dengue-mtDNA-cGAS-STING axis activates inflammatory cytokines during severe dengue.

**→ [STAT1](../../../03-molecular/stat1/)**: DENV NS5 degrades STAT2 via UBR4 → ISGF3 (STAT1/STAT2/IRF9) cannot form → ISG transcription blocked; NS5 selectively targets human STAT2 (not mouse) → human-specific IFN evasion; STAT2 degradation is a major determinant of dengue viremia and is absent in murine dengue models.
