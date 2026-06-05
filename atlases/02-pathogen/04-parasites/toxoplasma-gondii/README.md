---
schema: pathogen-entry/v1
id: toxoplasma-gondii
name: Toxoplasma gondii
atlas: 02-pathogen
scale: 04-parasites
status: draft
last_reviewed: 2026-06-05
summary: "Apicomplexan; obligate intracellular; cats are definitive hosts (oocysts). Tachyzoite (acute), bradyzoite/tissue cyst (chronic). Parasitophorous vacuole resists killing. Congenital toxoplasmosis; reactivation encephalitis in AIDS. >33% of humans seropositive globally."
aliases: ["T. gondii", "Toxoplasma", "toxoplasmosis", "congenital toxoplasmosis", "cerebral toxoplasmosis"]
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
  - id: blader-2015-toxoplasma
    type: peer-reviewed
    cite: "Blader IJ, Coleman BI, Chen CT, Bhatt D. Lytic Cycle of Toxoplasma gondii: 15 Years Later. Annu Rev Microbiol. 2015;69:463-85."
    doi: "10.1146/annurev-micro-091014-104100"
    pmid: "26332089"
    url: "https://doi.org/10.1146/annurev-micro-091014-104100"
  - id: montoya-2004-toxo-review
    type: peer-reviewed
    cite: "Montoya JG, Liesenfeld O. Toxoplasmosis. Lancet. 2004;363(9425):1965-76."
    doi: "10.1016/S0140-6736(04)16412-X"
    pmid: "15194258"
    url: "https://doi.org/10.1016/S0140-6736(04)16412-X"
cross_links:
  - target: 01-human/06-organ/brain
    relation: damages
    note: "Bradyzoites persist as tissue cysts in neurons and glial cells; reactivation in AIDS (CD4<100) causes necrotising encephalitis with ring-enhancing MRI lesions, mass effect, and risk of herniation."
  - target: 01-human/07-system/nervous-system
    relation: damages
    note: "Chronic neurological infection disrupts dopamine metabolism and GABAergic signalling; congenital toxoplasmosis causes hydrocephalus and intracranial calcifications in neonates."
  - target: 01-human/04-cellular/macrophage
    relation: damages
    note: "Toxoplasma resides in PV within macrophages; ROP18/ROP5 kinases phosphorylate and neutralise GBP/IRGB immunity-related GTPases, preventing vacuole destruction and enabling intracellular survival."
  - target: 01-human/07-system/immune-system
    relation: damages
    note: "Toxoplasma actively modulates Th1/Th2 balance; IL-12/IFN-gamma axis is critical for control; chronic infection induces IL-10-mediated immunosuppression; CD8+ T cell exhaustion promotes cyst persistence."
---

# Toxoplasma gondii

## Overview

***Toxoplasma gondii*** is an obligate intracellular apicomplexan protozoan with arguably the widest host range of any eukaryotic pathogen — it can infect virtually all warm-blooded vertebrates. Despite causing generally asymptomatic infection in immunocompetent adults, it represents a major pathogen in three critical contexts: **congenital toxoplasmosis** (devastating fetal neurological damage), **reactivation encephalitis in AIDS** (leading cause of focal CNS lesions in advanced HIV), and severe primary infection in other immunocompromised hosts (transplant recipients, haematological malignancies) [^montoya-2004-toxo-review].

More than **one-third of the global human population** is estimated to carry latent *T. gondii* infection based on seropositivity surveys — making it one of the most prevalent parasitic infections worldwide. Seroprevalence varies dramatically by region, from ~10–15% in the USA to >80% in parts of France, Brazil, and Ethiopia, reflecting differences in raw meat consumption habits, cat density, and environmental oocyst burden.

The parasite's clinical significance is shaped almost entirely by **immune status**: in healthy individuals, a robust Th1 response (IL-12, IFN-γ, CD8+ T cells) contains infection in latent tissue cysts indefinitely. When cellular immunity collapses — particularly in AIDS with CD4 counts below 100 cells/µL — cyst reactivation produces rapidly expanding necrotic brain lesions that are fatal without treatment [^blader-2015-toxoplasma]. Pyrimethamine combined with sulfadiazine (plus leucovorin) is the standard treatment; TMP-SMX is used for prophylaxis when CD4 <100.

## Structure

**Life cycle stages and morphology:**

| Stage | Location | Size | Biology |
|:---|:---|:---|:---|
| **Oocyst** | Cat feces → soil/water | 10–12 µm | Unsporulated (non-infectious); sporulates in 1–5 days; extremely hardy (survives months in soil) |
| **Sporozoite** | Inside sporulated oocyst | ~8 µm elongated | 2 per sporocyst (4 sporocysts/oocyst); infectious after sporulation |
| **Tachyzoite** | Acute infection, all tissues | 4–8 µm, banana-shaped | Rapidly dividing (endodyogeny every 6–8 h); responsible for acute illness and tissue dissemination |
| **Bradyzoite** | Chronic/latent, tissue cysts | 5–9 µm, slower metabolism | Inside cysts in brain and muscle; metabolically quiescent; cysts 5–200 µm diameter |
| **Tissue cyst** | Brain, skeletal muscle, heart | 5–200 µm | Wall of cyst matrix proteins (CST1/MAG1); bradyzoites within; extremely stable; lifelong persistence |

**Key molecular virulence factors:**

- **MIC proteins (Microneme proteins):** MIC2, MIC3, MIC8 — secreted from apical micronemes upon host cell contact; mediate initial adhesion (MIC2 binds heparan sulfate/ICAM-1) and act as bridging molecules between parasite and host
- **RON proteins (Rhoptry neck proteins):** RON2/RON4/RON5/RON8 complex — injected into host cell membrane to form the **moving junction** (tight ring through which the parasite threads itself during invasion)
- **ROP kinases (Rhoptry body proteins):** ROP18 (active kinase) phosphorylates immunity-related GTPases (IRGAs) to prevent vacuole disruption; ROP5 (pseudokinase) stabilises ROP18 and acts as a co-factor; ROP16 directly phosphorylates and activates STAT3/STAT6 (anti-inflammatory)
- **GRA proteins (Dense granule proteins):** GRA7, GRA15, GRA24 — secreted into PV lumen and through PV membrane into host cytosol; GRA15 activates NF-κB; GRA24 self-associates with host p38 MAPK to upregulate IL-12
- **Parasitophorous vacuole (PV):** Non-fusogenic vacuole derived during invasion; does not fuse with endosomes or lysosomes (lacks Rab5, Rab7 markers); host mitochondria and ER contact PV membrane for nutrient acquisition

## Infection Mechanism

**Step-by-step molecular pathogenesis:**

**1. Acquisition (three routes):**
- **Oral ingestion of oocysts** from soil/water/unwashed produce contaminated by cat feces (sporulated oocysts survive for months)
- **Ingestion of tissue cysts** in undercooked or raw meat (most common in seropositive adults in France/Latin America)
- **Congenital transmission:** Primary infection during pregnancy → tachyzoitaemia → transplacental crossing to fetus; risk increases with gestational age (1st trimester: lower risk but more severe disease; 3rd trimester: higher risk, milder disease)

**2. Gut invasion:**
- Sporozoites/bradyzoites released by gastric acid and intestinal enzymes differentiate into tachyzoites
- Tachyzoites invade intestinal epithelial cells actively using **gliding motility** (glideosome motor complex: MyoA/MLC1/GAP45/GAPM proteins) — parasite moves in a corkscrew pattern at ~1–2 µm/s, powered by actin-myosin interaction beneath the inner membrane complex

**3. Formation of the parasitophorous vacuole (PV):**
- During invasion, the parasite actively invaginates the host cell membrane, forming a vacuole
- **Cholesterol** is selectively excluded from the nascent PV membrane (unlike phagosomes), preventing phagosomal fusion markers from accumulating
- RON2 is injected into the host membrane prior to complete entry; it serves as the receptor for AMA1 (apical membrane antigen 1) on the parasite surface, forming the constricting tight junction ring
- Upon completion of invasion, the nascent PV is sealed; parasite secretes GRA proteins to remodel the PV membrane, establishing nutrient-scavenging contacts with host organelles

**4. Intracellular replication (endodyogeny):**
- Two daughter cells form simultaneously within the mother cell; each inherits one nucleus (post-replication), half the apicoplast, half the mitochondrion, and newly assembled inner membrane complex
- Division cycle: ~6–8 hours per division; a rosette of 8–32 tachyzoites fills the PV before host cell lysis

**5. Evasion of immune killing:**
- **ROP18** phosphorylates IRGAs (immunity-related GTPases IRGA6, IRGB6) at inhibitory Thr/Ser residues → prevents their oligomerisation on PV membrane → vacuole is not disrupted
- **ROP5** co-localises with IRGB/GBP proteins and blocks GBP-mediated vacuole coating
- Host cell **autophagy** of PV is blocked by ROP18-mediated phosphorylation of ATG13 (prevents autophagosome nucleation around PV)

**6. Stage conversion to bradyzoites:**
- Stress signals (alkaline pH, nutrient deprivation, immune pressure, NO, heat shock) trigger AP2IV transcription factor cascades → tachyzoite → bradyzoite differentiation
- Bradyzoites upregulate CST1 (cyst wall glycoprotein), BAG1 (small heat shock protein), and amylopectin granules (energy storage); downregulate tachyzoite-specific TgSAG1 (p30)
- Tissue cysts are immunologically invisible: cyst wall is poorly immunogenic; bradyzoites express surface antigens distinct from tachyzoites

**7. Reactivation in immunosuppression:**
- CD8+ T cell depletion (AIDS, immunosuppressive therapy) removes the principal effector controlling cyst persistence
- Bradyzoites convert back to tachyzoites, lyse cyst walls, and establish a fulminating necrotic encephalitis

## Host Interactions

**Cells and organs targeted:**

| Cell/Organ | Interaction | Consequence |
|:---|:---|:---|
| Intestinal epithelium | Active invasion by tachyzoites | Portal of entry; local inflammation |
| Macrophages, dendritic cells | Hijacked as dissemination vehicles ("Trojan horse") | Systemic spread; evasion of innate killing |
| Neurons (brain, retina) | Bradyzoite cyst formation | Lifelong latent infection; reactivation encephalitis |
| Skeletal and cardiac muscle | Bradyzoite cyst formation | Source of foodborne transmission |
| Placental trophoblasts | Transplacental crossing | Congenital infection of fetus |

**Immune evasion mechanisms:**

- **PV non-fusogenicity:** The parasitophorous vacuole avoids lysosomal fusion, escaping degradation that would occur in a conventional phagosome
- **ROP kinase-mediated IFN-γ resistance:** ROP18/ROP5 neutralise the IFN-γ-induced IRG (immunity-related GTPase) pathway — the key innate effector mechanism against *T. gondii* in mice; in humans, GBP (guanylate-binding proteins) play an analogous role and are similarly targeted
- **STAT modulation:** ROP16 (type I/III strains) directly phosphorylates STAT3 and STAT6 → IL-4/IL-13 signalling → Th2-skewed/anti-inflammatory environment reduces IFN-γ production
- **IL-10 induction:** Chronic infection drives IL-10 from regulatory T cells (Tregs) and exhausted CD8+ T cells; IL-10 suppresses macrophage activation and IL-12 production
- **MHC modulation:** *T. gondii* transiently upregulates MHC class I on infected cells (facilitating CD8+ T cell recognition of infected vs. uninfected cells) while simultaneously reducing antigen presentation efficiency via interference with TAP transporters in some strain backgrounds

**Tropism for the CNS:**

The predilection of *T. gondii* for brain tissue (neurons, astrocytes) in chronic infection is not fully explained but involves:
- Decreased IFN-γ responsiveness of neurons compared with peripheral tissues (lower STAT1 levels, less MHC class I)
- Bradyzoite cysts protected by CST1 matrix protein, resistant to proteolysis and immune recognition
- Dopaminergic neurons may be preferentially infected (bradyzoites synthesise tyrosine hydroxylase, potentially altering host dopamine signalling)

## Connections

- **Damages** → [Brain](../../../01-human/06-organ/brain/README.md): Bradyzoites persist as tissue cysts in neurons and glial cells; reactivation in AIDS (CD4<100) causes necrotising encephalitis with ring-enhancing MRI lesions, mass effect, and risk of herniation.

- **Damages** → [Nervous System](../../../01-human/07-system/nervous-system/README.md): Chronic neurological infection disrupts dopamine metabolism and GABAergic signalling; congenital toxoplasmosis causes hydrocephalus and intracranial calcifications in neonates.

- **Damages** → [Macrophage](../../../01-human/04-cellular/macrophage/README.md): Toxoplasma resides in PV within macrophages; ROP18/ROP5 kinases phosphorylate and neutralise GBP/IRGB immunity-related GTPases, preventing vacuole destruction and enabling intracellular survival.

- **Damages** → [Immune System](../../../01-human/07-system/immune-system/README.md): Toxoplasma actively modulates Th1/Th2 balance; IL-12/IFN-gamma axis is critical for control; chronic infection induces IL-10-mediated immunosuppression; CD8+ T cell exhaustion promotes cyst persistence.

## Pathology

**Congenital toxoplasmosis:**

Primary *T. gondii* infection during pregnancy causes transplacental transmission in ~20–50% of cases (depending on gestational timing and immune status). Fetal manifestations (the classic "Sabin tetrad") include:
- **Chorioretinitis:** Retinal inflammation → macular scarring → progressive visual impairment; most common sequela
- **Hydrocephalus:** Aqueductal stenosis from periventricular inflammation
- **Intracranial calcifications:** Periventricular calcium deposits on skull X-ray/CT (contrast with CMV which is more periventricular)
- **Psychomotor retardation:** From diffuse CNS damage; intellectual disability, seizures
Many congenitally infected infants appear normal at birth but develop chorioretinitis and neurological symptoms months to years later. Prenatal diagnosis via amniotic fluid PCR; maternal serological screening protocols vary by country (universal in France).

**Cerebral toxoplasmosis (AIDS):**

The most common cause of focal brain lesions in HIV-infected individuals with CD4 < 100 cells/µL (before widespread ART). Imaging: multiple ring-enhancing lesions at grey-white junction and basal ganglia on contrast CT/MRI (must be distinguished from primary CNS lymphoma — single lesion, positive EBV in CSF, no therapeutic response to anti-toxo therapy). Empirical anti-toxoplasma treatment (pyrimethamine + sulfadiazine) initiated with positive serology and characteristic imaging — clinical/radiological response at 2 weeks confirms diagnosis.

**Epidemiology:**

| Parameter | Value |
|:---|:---|
| Global seroprevalence | >33% (varies: USA 11%, France 45–70%, Brazil 50–80%) |
| Congenital infections/year | ~190,000 (globally; WHO estimate) |
| Mortality (congenital) | ~1,200/year; long-term morbidity is far higher |
| AIDS reactivation incidence | ~10–15% of seropositive AIDS patients without prophylaxis |

**Diagnosis:**

| Test | Context | Notes |
|:---|:---|:---|
| Serology (IgG/IgM) | Screening, acute infection | IgM may persist years; IgG avidity test determines timing of infection |
| IgG avidity | Pregnancy — determining timing | Low avidity = recent (<4 months); high avidity = past infection |
| PCR (amniotic fluid, CSF, blood) | Congenital, CNS disease | High specificity; sensitivity varies by stage |
| Brain biopsy | Atypical/non-responsive CNS lesions | Rarely needed if classic presentation |

**Treatment:**

| Indication | Regimen | Notes |
|:---|:---|:---|
| Acute toxoplasmosis (immunocompromised) | Pyrimethamine + sulfadiazine + leucovorin × 6 weeks | Leucovorin prevents pyrimethamine bone marrow toxicity |
| Alternative | Pyrimethamine + clindamycin | For sulfadiazine allergy |
| Cerebral toxoplasmosis maintenance | Pyrimethamine + sulfadiazine + leucovorin (lifelong until CD4 >200 on ART) | Secondary prophylaxis required in AIDS |
| Congenital (neonatal) | Pyrimethamine + sulfadiazine × 12 months | Initiated at birth even if asymptomatic |
| Primary prophylaxis (AIDS, CD4 <100) | TMP-SMX 1DS daily | Also covers *Pneumocystis jirovecii* |
| Pregnancy | Spiramycin (to prevent transmission) or pyrimethamine/sulfadiazine if confirmed fetal infection (after 18 weeks) | Pyrimethamine is teratogenic in 1st trimester |

[^blader-2015-toxoplasma]: Blader IJ, et al. Lytic Cycle of Toxoplasma gondii: 15 Years Later. Annu Rev Microbiol. 2015;69:463–85.
[^montoya-2004-toxo-review]: Montoya JG, Liesenfeld O. Toxoplasmosis. Lancet. 2004;363(9425):1965–76.
[^mandell-principles]: Bennett JE, Dolin R, Blaser MJ. Mandell, Douglas, and Bennett's Principles and Practice of Infectious Diseases. 9th ed. Elsevier; 2020.
[^murray-microbiology]: Murray PR, Rosenthal KS, Pfaller MA. Medical Microbiology. 9th ed. Elsevier; 2021.
