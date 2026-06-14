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
  - target: 01-human/07-system/zika-virus
    relation: connects-to
    note: "ZIKV and DENV share Aedes aegypti vector and flavivirus biology; cross-reactive anti-DENV antibodies may enhance ZIKV infection via ADE in Fcγ receptor-bearing cells; prior dengue immunity has complex effects on Zika severity; both NS5 proteins degrade STAT2 for IFN evasion."
  - target: 01-human/07-system/west-nile-virus
    relation: connects-to
    note: "WNV and DENV share flavivirus biology and NS5-mediated STAT1/STAT2 evasion; anti-DENV IgG cross-reacts with WNV E protein but provides limited protection; WNV causes neuroinvasive disease (encephalitis, AFP) not seen in DENV; both lack approved antivirals."
  - target: 02-pathogen/06-environmental/aedes-aegypti
    relation: connects-to
    note: "Dengue is spread by the day-biting Aedes aegypti mosquito, which also carries Zika, chikungunya, and yellow fever; its spread into the warming, urbanizing tropics is why dengue now causes ~400 million infections a year, and vector control remains a mainstay of prevention."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Macrophages are dengue's main host cell and engine of severe disease: in reinfection with another serotype, non-neutralizing antibodies ferry virus into Fcγ-bearing macrophages — antibody-dependent enhancement — raising viral load and the cytokines that drive hemorrhagic dengue."
  - target: 01-human/07-system/cytokine-storm
    relation: connects-to
    note: "Severe dengue is partly a cytokine storm: antibody-enhanced macrophage infection plus cross-reactive memory T cells pour out TNF-α, IL-6, and IFN-γ that — with NS1 acting on the endothelium — break vascular integrity, causing the plasma leak of dengue hemorrhagic fever and shock."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "Severe dengue is a disease of the endothelium: viral NS1 protein and cytokines transiently disrupt the endothelial glycocalyx and tight junctions, causing the plasma leakage (hemoconcentration, effusions, shock) that defines dengue hemorrhagic fever and dengue shock syndrome."
  - target: 01-human/07-system/disseminated-intravascular-coagulation
    relation: connects-to
    note: "Severe dengue can trigger disseminated intravascular coagulation: endothelial injury, thrombocytopenia and cytokine-driven tissue-factor activation consume clotting factors, producing the bleeding of dengue hemorrhagic fever; DIC marks the severe end and worsens shock."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "The liver is a key dengue target: the virus replicates in hepatocytes and Kupffer cells, raising transaminases in most cases and occasionally causing fulminant hepatitis; marked AST/ALT elevation is a warning sign of progression to severe dengue and correlates with bleeding."
  - target: 01-human/04-cellular/platelet
    relation: connects-to
    note: "Thrombocytopenia defines severe dengue: the virus suppresses marrow megakaryopoiesis and antibodies destroy platelets, while plasma leak concentrates the blood—so a falling platelet count with rising hematocrit warns of progression to dengue hemorrhagic fever."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "Dengue virus first infects dendritic cells via DC-SIGN: skin dendritic cells captured at the mosquito bite are the earliest replication site and carry the virus onward, and antibody-dependent enhancement on a second infection worsens this uptake—driving severe dengue."
  - target: 01-human/07-system/malaria
    relation: connects-to
    note: "Dengue and malaria are the two great mosquito-borne tropical fevers and key differentials: both cause fever, thrombocytopenia, and can be severe, but dengue (Aedes flavivirus) brings plasma leak and hemorrhage while malaria (Plasmodium) brings hemolysis and cerebral disease."
  - target: 02-pathogen/01-viruses/dengue-virus
    relation: connects-to
    note: "Dengue virus drives the disease through four serotypes: infection gives lasting immunity to one serotype but only brief cross-protection, so later infection by a different serotype risks severe dengue—the serotype diversity central to the virus's danger."
  - target: 01-human/03-molecular/immunoglobulin-g
    relation: connects-to
    note: "Pre-existing IgG can worsen dengue via antibody-dependent enhancement: non-neutralizing antibodies from a prior serotype bind the new virus and ferry it into macrophages, boosting viral load—why second heterotypic infections cause severe, hemorrhagic dengue."
  - target: 01-human/05-tissue/bone-marrow
    relation: connects-to
    note: "Dengue suppresses the bone marrow: the virus infects marrow progenitors and dampens production, causing the falling platelet and white-cell counts that define and grade the illness—so cytopenias track severity and signal the risk of hemorrhage."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Cytotoxic T cells help drive severe dengue: cross-reactive memory T cells from a prior dengue serotype respond suboptimally on reinfection, releasing cytokines that worsen vascular leak—part of why a second, different-serotype infection is the dangerous one."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "Dengue's danger is immunological: antibodies from a first infection can enhance uptake of a second serotype (antibody-dependent enhancement), amplifying viral load and the immune overreaction that causes plasma leak—so prior immunity paradoxically raises severe-dengue risk."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "Dengue can invade the nervous system: beyond classic fever and bleeding, the virus and its immune response cause encephalitis, Guillain-Barré-like syndromes and stroke, so neurological dengue is an increasingly recognized severe manifestation."
  - target: 01-human/04-cellular/b-cell
    relation: connects-to
    note: "Dengue's danger lies in B-cell antibodies: non-neutralizing antibodies from a prior infection can enhance a second one (antibody-dependent enhancement), so partial immunity worsens disease—the paradox that makes dengue vaccines hard to design."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "Severe dengue is a cardiovascular emergency: cytokines make capillaries leak plasma, dropping blood volume into dengue shock syndrome, so careful fluid management—not antivirals—is what saves lives in the critical phase."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "Severe dengue can injure the kidney: shock, hemolysis, and direct viral effects cause acute kidney injury in the critical phase, so renal function is watched closely as a marker of severity and a target for supportive care."
  - target: 01-human/03-molecular/albumin
    relation: connects-to
    note: "Severe dengue is defined by leaking albumin: the virus makes capillaries leak, so plasma and albumin escape into the chest and belly, concentrating the blood and dropping pressure into the shock that makes dengue hemorrhagic fever deadly."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "Mast cells help make dengue severe: infection activates them to release chymase and vasoactive mediators that pull apart vascular junctions, driving the plasma leak of severe dengue—and blood chymase levels track with disease severity."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "Dengue can inflame the heart: the virus causes myocarditis with weakened contraction and arrhythmias, an underrecognized contributor to the shock and fluid-balance problems that complicate severe infection."
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

**→ [Zika Virus](../zika-virus/)**: ZIKV and DENV share Aedes aegypti vector and flavivirus biology; cross-reactive anti-DENV antibodies may enhance ZIKV infection via ADE in Fcγ receptor-bearing cells; prior dengue immunity has complex effects on Zika severity; both NS5 proteins degrade STAT2 for IFN evasion.

**→ [West Nile Virus](../west-nile-virus/)**: WNV and DENV share flavivirus biology and NS5-mediated STAT1/STAT2 evasion; anti-DENV IgG cross-reacts with WNV E protein but provides limited protection; WNV causes neuroinvasive disease (encephalitis, AFP) not seen in DENV; both lack approved antivirals.

**→ [Aedes aegypti](../../../../02-pathogen/06-environmental/aedes-aegypti/)**: Dengue is spread by the day-biting Aedes aegypti mosquito, which also carries Zika, chikungunya, and yellow fever; its spread into the warming, urbanizing tropics is why dengue now causes ~400 million infections a year, and vector control remains a mainstay of prevention.

**→ [Macrophage](../../04-cellular/macrophage/)**: Macrophages are dengue's main host cell and engine of severe disease: in reinfection with another serotype, non-neutralizing antibodies ferry virus into Fcγ-bearing macrophages — antibody-dependent enhancement — raising viral load and the cytokines that drive hemorrhagic dengue.

**→ [Cytokine Storm](../cytokine-storm/)**: Severe dengue is partly a cytokine storm: antibody-enhanced macrophage infection plus cross-reactive memory T cells pour out TNF-α, IL-6, and IFN-γ that — with NS1 acting on the endothelium — break vascular integrity, causing the plasma leak of dengue hemorrhagic fever and shock.

- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — Severe dengue is a disease of the endothelium: viral NS1 protein and cytokines transiently disrupt the endothelial glycocalyx and tight junctions, causing the plasma leakage (hemoconcentration, effusions, shock) that defines dengue hemorrhagic fever and dengue shock syndrome.
- `connects-to` → **[Disseminated Intravascular Coagulation](../disseminated-intravascular-coagulation/README.md)** — Severe dengue can trigger disseminated intravascular coagulation: endothelial injury, thrombocytopenia and cytokine-driven tissue-factor activation consume clotting factors, producing the bleeding of dengue hemorrhagic fever; DIC marks the severe end and worsens shock.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — The liver is a key dengue target: the virus replicates in hepatocytes and Kupffer cells, raising transaminases in most cases and occasionally causing fulminant hepatitis; marked AST/ALT elevation is a warning sign of progression to severe dengue and correlates with bleeding.
- `connects-to` → **[Platelet](../../04-cellular/platelet/README.md)** — Thrombocytopenia defines severe dengue: the virus suppresses marrow megakaryopoiesis and antibodies destroy platelets, while plasma leak concentrates the blood—so a falling platelet count with rising hematocrit warns of progression to dengue hemorrhagic fever.
- `connects-to` → **[Dendritic Cell](../../04-cellular/dendritic-cell/README.md)** — Dengue virus first infects dendritic cells via DC-SIGN: skin dendritic cells captured at the mosquito bite are the earliest replication site and carry the virus onward, and antibody-dependent enhancement on a second infection worsens this uptake—driving severe dengue.
- `connects-to` → **[Malaria](../malaria/README.md)** — Dengue and malaria are the two great mosquito-borne tropical fevers and key differentials: both cause fever, thrombocytopenia, and can be severe, but dengue (Aedes flavivirus) brings plasma leak and hemorrhage while malaria (Plasmodium) brings hemolysis and cerebral disease.
- `connects-to` → **[Dengue virus](../../../02-pathogen/01-viruses/dengue-virus/README.md)** — Dengue virus drives the disease through four serotypes: infection gives lasting immunity to one serotype but only brief cross-protection, so later infection by a different serotype risks severe dengue—the serotype diversity central to the virus's danger.
- `connects-to` → **[Immunoglobulin G](../../03-molecular/immunoglobulin-g/README.md)** — Pre-existing IgG can worsen dengue via antibody-dependent enhancement: non-neutralizing antibodies from a prior serotype bind the new virus and ferry it into macrophages, boosting viral load—why second heterotypic infections cause severe, hemorrhagic dengue.
- `connects-to` → **[Bone Marrow](../../05-tissue/bone-marrow/README.md)** — Dengue suppresses the bone marrow: the virus infects marrow progenitors and dampens production, causing the falling platelet and white-cell counts that define and grade the illness—so cytopenias track severity and signal the risk of hemorrhage.
- `connects-to` → **[Cytotoxic T Cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Cytotoxic T cells help drive severe dengue: cross-reactive memory T cells from a prior dengue serotype respond suboptimally on reinfection, releasing cytokines that worsen vascular leak—part of why a second, different-serotype infection is the dangerous one.
- `connects-to` → **[Immune System](../immune-system/README.md)** — Dengue's danger is immunological: antibodies from a first infection can enhance uptake of a second serotype (antibody-dependent enhancement), amplifying viral load and the immune overreaction that causes plasma leak—so prior immunity paradoxically raises severe-dengue risk.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — Dengue can invade the nervous system: beyond classic fever and bleeding, the virus and its immune response cause encephalitis, Guillain-Barré-like syndromes and stroke, so neurological dengue is an increasingly recognized severe manifestation.
- `connects-to` → **[B Cell](../../04-cellular/b-cell/README.md)** — Dengue's danger lies in B-cell antibodies: non-neutralizing antibodies from a prior infection can enhance a second one (antibody-dependent enhancement), so partial immunity worsens disease—the paradox that makes dengue vaccines hard to design.
- `connects-to` → **[Cardiovascular system](../cardiovascular-system/README.md)** — Severe dengue is a cardiovascular emergency: cytokines make capillaries leak plasma, dropping blood volume into dengue shock syndrome, so careful fluid management—not antivirals—is what saves lives in the critical phase.
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — Severe dengue can injure the kidney: shock, hemolysis, and direct viral effects cause acute kidney injury in the critical phase, so renal function is watched closely as a marker of severity and a target for supportive care.
- `connects-to` → **[Albumin](../../03-molecular/albumin/README.md)** — Severe dengue is defined by leaking albumin: the virus makes capillaries leak, so plasma and albumin escape into the chest and belly, concentrating the blood and dropping pressure into the shock that makes dengue hemorrhagic fever deadly.
- `connects-to` → **[Mast Cell](../../04-cellular/mast-cell/README.md)** — Mast cells help make dengue severe: infection activates them to release chymase and vasoactive mediators that pull apart vascular junctions, driving the plasma leak of severe dengue—and blood chymase levels track with disease severity.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — Dengue can inflame the heart: the virus causes myocarditis with weakened contraction and arrhythmias, an underrecognized contributor to the shock and fluid-balance problems that complicate severe infection.
