---
schema: pathogen-entry/v1
id: trypanosoma-brucei
name: Trypanosoma brucei
atlas: 02-pathogen
scale: 04-parasites
status: draft
last_reviewed: 2026-06-05
summary: "Kinetoplastid flagellate; tsetse fly vector. T. b. gambiense (West Africa, chronic); T. b. rhodesiense (East Africa, acute). VSG antigenic variation evades antibodies. Bloodstream → CNS → sleeping sickness. ~992 cases/year near-elimination target."
aliases: ["T. brucei", "African sleeping sickness", "human African trypanosomiasis", "HAT", "Trypanosoma brucei gambiense", "Trypanosoma brucei rhodesiense"]
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
  - id: matthews-2005-tbrucei
    type: peer-reviewed
    cite: "Matthews KR. The developmental cell biology of Trypanosoma brucei. J Cell Sci. 2005;118(Pt 2):283-90."
    doi: "10.1242/jcs.01649"
    pmid: "15647371"
    url: "https://doi.org/10.1242/jcs.01649"
  - id: who-hat-2021
    type: clinical-guideline
    cite: "World Health Organization. Control and surveillance of human African trypanosomiasis. WHO Technical Report Series No. 984. WHO; 2013 (updated data 2022)."
    url: "https://www.who.int/trypanosomiasis_african/en/"
    accessed: "2026-06-05"
cross_links:
  - target: 01-human/07-system/nervous-system
    relation: damages
    note: "Stage 2 sleeping sickness: trypanosomes cross blood-brain barrier via choroid plexus and post-capillary venules; neuroinflammation (astrocyte activation, demyelination) disrupts sleep-wake cycle (circadian reversal)."
  - target: 01-human/06-organ/brain
    relation: damages
    note: "CNS penetration causes progressive encephalitis; neuropsychiatric symptoms (personality change, seizures, coma) and circadian rhythm disruption; without treatment, 100% fatal in Stage 2 disease."
  - target: 01-human/07-system/immune-system
    relation: damages
    note: "VSG coat (10 million copies/cell) shields invariant surface antigens from antibody recognition; monoallelic VSG expression switching every ~100 generations exhausts antibody responses; >1000 VSG genes per genome."
  - target: 01-human/04-cellular/macrophage
    relation: damages
    note: "Trypanosome-derived factors (trypanosome-released triggers, TLRs ligands) activate macrophages to produce TNF-alpha, IL-6, and IFN-gamma; systemic inflammation, anaemia, and cachexia hallmarks of disease."
---

# Trypanosoma brucei

## Overview

***Trypanosoma brucei*** causes **human African trypanosomiasis (HAT)**, popularly known as sleeping sickness — one of Africa's most historically devastating parasitic diseases, responsible for massive epidemics in the 20th century (notably 1896–1906 in Uganda and the Congo; 300,000–500,000 deaths). Two subspecies infect humans: ***T. b. gambiense*** (West and Central Africa; chronic disease course, 97% of all HAT cases) and ***T. b. rhodesiense*** (East Africa; acute disease, wildlife animal reservoir) [^who-hat-2021].

The global burden of HAT has been dramatically reduced through intensive vector control, systematic active screening, and improved treatment — from ~300,000 cases/year in the 1990s to **992 reported cases in 2019**, approaching the WHO 2030 elimination target. However, the disease remains 100% fatal without treatment, the tsetse fly vector persists across sub-Saharan Africa, and the potential for resurgence from the animal reservoir (*T. b. rhodesiense*) remains [^who-hat-2021].

*T. brucei* is a **kinetoplastid** (named for the kinetoplast — a large mitochondrial DNA-containing structure unique to this order) and exists exclusively as an extracellular pathogen in the mammalian host, living freely in blood, lymphatics, and ultimately cerebrospinal fluid. Its defining virulence mechanism — **VSG (variant surface glycoprotein) antigenic variation** — is one of the most sophisticated immune evasion strategies in biology: a densely packed coat of 10 million identical VSG copies shields the parasite surface, and periodic switching of VSG expression ensures the parasite always stays ahead of the antibody response [^matthews-2005-tbrucei].

## Structure

**Life cycle stages and morphology:**

| Stage | Location | Size | Biology |
|:---|:---|:---|:---|
| **Procyclic trypomastigote** | Tsetse fly midgut | 20–40 µm | Proliferating; procyclin surface coat (not VSG); kinetoplast posterior |
| **Epimastigote** | Tsetse salivary gland | Variable | Transition form; kinetoplast anterior of nucleus |
| **Metacyclic trypomastigote** | Tsetse salivary gland | ~15 µm | Non-dividing; VSG coat established; injected into host |
| **Slender bloodstream form** | Mammalian blood/lymph/CSF | 20–30 µm | Proliferating; VSG coat; dependent on glycolysis (glycosomes) |
| **Stumpy bloodstream form** | Mammalian blood | 15–25 µm, rounded | Non-dividing; pre-adapted for uptake by tsetse; ESAG9 upregulation |

**Key molecular architecture:**

- **VSG (Variant Surface Glycoprotein):** ~55–60 kDa; GPI-anchored glycoprotein forming a dense homodimeric coat (~10 million copies); N-terminal domain forms a structurally conserved fold shielding the invariant GPI anchor from antibody recognition; only one of >1,000 VSG genes expressed at a time from a subtelomeric **Expression Site (ESQ)**; periodic switching (every ~100 cell divisions on average) via recombination or in situ activation of an alternative ESQ
- **VSG Expression Sites (ES):** ~15 polycistronic telomeric loci; one active at a time (active ES Body, eESB); switching occurs by: (a) transcriptional silencing of active ES + activation of new ES; (b) gene conversion (copying new VSG into active ES); (c) reciprocal recombination; each mechanism monitored by the RNA polymerase I-containing ESB
- **Kinetoplast:** Unusual mitochondrial DNA structure — concatenated network of thousands of minicircles (~1 kb) and ~25 maxicircles (~22 kb); minicircles encode guide RNAs for editing of maxicircle transcripts (U-insertion/deletion RNA editing adds up to 55% of the uridines in some mRNAs) — entirely absent in most eukaryotes; essential for mitochondrial function
- **Glycosomes:** Peroxisome-related organelles uniquely containing glycolytic enzymes (hexokinase, phosphoglucose isomerase, phosphofructokinase, etc.); sequestration of glycolysis from the cytoplasm has pharmacological implications (glycosomal enzymes are potential drug targets)
- **Flagellum:** Single flagellum emerging from the flagellar pocket (site of all endo/exocytosis); para-flagellar rod (PFR) structure unique to kinetoplastids; VSG is shed and re-expressed at the flagellar pocket to remove antibody-coated VSG via hydrodynamic force

## Infection Mechanism

**Step-by-step molecular pathogenesis:**

**1. Tsetse fly bite (inoculation):**
- *Glossina* (tsetse fly) females and males require blood meals; when feeding, metacyclic trypomastigotes from salivary glands are injected into the dermal extracellular space with tsetse saliva (~300–3,000 metacyclic forms per bite)
- **Tsetse saliva** contains immunosuppressive molecules (sialylated glycoproteins, prostaglandins, anti-complement factors) that facilitate parasite survival at the inoculation site

**2. Chancre formation (skin, first week):**
- Metacyclic trypomastigotes multiply locally in dermis, provoking an intense inflammatory response (macrophage, neutrophil, T cell infiltration) → **trypanosomal chancre** — a painful, indurated skin nodule at the bite site (more prominent in *T. b. rhodesiense*)
- Metacyclic VSGs (a subset of ~27 distinct metacyclic VSG genes expressed stochastically) serve as the initial coat; these are replaced by bloodstream VSGs as parasites disseminate

**3. Stage 1 — Haemolymphatic dissemination:**
- Trypomastigotes enter lymphatics and bloodstream; replicate by binary fission as slender bloodstream forms (dividing, VSG-coated)
- Waves of parasitaemia: each VSG-specific antibody response eliminates the dominant variant → selects for rare VSG-switching parasites → new wave; this cycle produces the hallmark **relapsing fever waves** of HAT
- Parasites disseminate to lymph nodes (lymphadenopathy; **Winterbottom's sign** = posterior cervical lymphadenopathy, pathognomonic for *T. b. gambiense*), spleen, liver
- Slender → stumpy differentiation: triggered by **stumpy induction factor (SIF)**, a density-dependent signal (adenosine/AMP); stumpy forms are arrested in G1/G0 and pre-adapted for tsetse uptake

**4. VSG antigenic variation (molecular detail):**
- Only one of ~15 Expression Sites (ES) is transcribed at a time by RNA polymerase I from the **ES body** (a distinct nuclear compartment)
- Switching frequency: ~10⁻⁷ per cell per generation (overall population switches ~once per 100 generations)
- Three switching mechanisms:
  - *In situ* activation: transcriptional switching to a different pre-existing ES (no DNA rearrangement)
  - Gene conversion: upstream VSG gene copied into the active ES by homologous recombination (most common); mediated by RAD51 and the *T. brucei* BRCA2 homologue
  - Reciprocal recombination: exchange between two ES (rare)
- Net result: host antibody response is perpetually behind the parasite's VSG repertoire; full VSG cycling would take years, exceeding the lifespan of the host

**5. Stage 2 — CNS invasion:**
- The transition to Stage 2 is the critical virulence step: trypanosomes penetrate the blood-brain barrier (BBB) and blood-cerebrospinal fluid barrier (BCSFB)
- Routes of CNS entry:
  - **Choroid plexus:** Parasites cross the epithelium of the choroid plexus directly (lower tight junction expression vs. brain capillary endothelium)
  - **Post-capillary venules:** Parasite-induced neuroinflammation → increased BBB permeability; CCL2/CXCL10 chemokine gradients recruit trypanosomes and inflammatory cells together
  - **Circumventricular organs:** Sites of incomplete BBB (subfornical organ, area postrema) may provide initial CNS entry points
- Within the CNS: trypanosomes reside in CSF, choroid plexus stroma, and perivascular spaces (Virchow-Robin spaces); profound **meningoencephalitis** with CD8+ T cell, B cell, and plasma cell infiltration; astroglial activation; myelin degradation

**6. Circadian rhythm disruption:**
- *T. brucei* secretes **trypanothione-related factors** and **aromatic metabolites** (indole compounds, tryptamine derivatives); accumulation of prostaglandin D₂ in CSF → somnolence via DP-1 receptors on hypothalamic neurons
- The sleep-wake cycle is progressively inverted: daytime somnolence, nocturnal insomnia (the eponymous "sleeping sickness")
- Hypothalamic-pituitary-adrenal and growth hormone axes disrupted → metabolic wasting, impotence, amenorrhoea

## Host Interactions

**Cells and tissues targeted:**

| Cell/Tissue | Interaction | Consequence |
|:---|:---|:---|
| Erythrocytes | Not invaded (extracellular pathogen) | Haemolytic anaemia via complement-mediated RBC destruction; autoantibodies (anti-RBC, anti-DNA, RF) |
| Macrophages (spleen, liver, lymph nodes) | Phagocytosis of antibody-opsonised stumpy forms | Contribute to systemic inflammation; VSA-coated trypanosomes resist complement before antibody coating |
| B cells | Polyclonal B cell activation | Hypergammaglobulinaemia (IgM elevation); autoantibody production; bystander B cell activation by parasite-released mitogens |
| Microglia/astrocytes | Neuroinflammatory activation in Stage 2 | Demyelination, neuronal apoptosis, synaptic dysfunction; glial scarring |
| Choroid plexus epithelium | Transcytosis and breaching | Primary gateway for CNS invasion |

**Immune evasion:**

- **VSG coat density:** 10 million VSG molecules per cell; coat is 12–15 nm thick; this steric shield prevents antibodies from accessing the invariant GPI anchor or invariant membrane proteins — only the variant N-terminal domain is exposed to immune surveillance
- **Rapid VSG shedding:** VSG is continuously shed by a GPI-specific phospholipase C (GPI-PLC) on the trypanosome surface; antibody-coated VSG complexes are endocytosed at the flagellar pocket at >2000/min (faster than new antibody can bind) — a form of kinetic immune evasion
- **Immunosuppression:** Trypanosome-derived factors suppress lymphocyte proliferative responses; IL-10 production from regulatory T cells and macrophages suppresses effector immunity; polyclonal B cell activation exhausts antigen-specific B cell responses
- **Complement evasion:** VSG binds complement factor H (via its conserved C-terminus) → prevents C3b deposition and MAC formation on the trypanosome surface; stumpy forms express trypanosome complement regulatory protein (TCRP)

## Connections

- **Damages** → [Nervous System](../../../01-human/07-system/nervous-system/README.md): Stage 2 sleeping sickness: trypanosomes cross blood-brain barrier via choroid plexus and post-capillary venules; neuroinflammation (astrocyte activation, demyelination) disrupts sleep-wake cycle (circadian reversal).

- **Damages** → [Brain](../../../01-human/06-organ/brain/README.md): CNS penetration causes progressive encephalitis; neuropsychiatric symptoms (personality change, seizures, coma) and circadian rhythm disruption; without treatment, 100% fatal in Stage 2 disease.

- **Damages** → [Immune System](../../../01-human/07-system/immune-system/README.md): VSG coat (10 million copies/cell) shields invariant surface antigens from antibody recognition; monoallelic VSG expression switching every ~100 generations exhausts antibody responses; >1000 VSG genes per genome.

- **Damages** → [Macrophage](../../../01-human/04-cellular/macrophage/README.md): Trypanosome-derived factors (trypanosome-released triggers, TLRs ligands) activate macrophages to produce TNF-alpha, IL-6, and IFN-gamma; systemic inflammation, anaemia, and cachexia hallmarks of disease.

## Pathology

**Clinical stages:**

**Stage 1 (haemolymphatic stage):**
- Fever (remittent, in waves correlating with VSG switching–driven parasitaemia peaks), headache, malaise, myalgia, arthralgia
- Lymphadenopathy — posterior cervical (Winterbottom's sign, seen in ~80% of *T. b. gambiense*); hepatosplenomegaly
- Trypanosomal chancre at bite site (more common in *T. b. rhodesiense*; rare in gambiense)
- Haematological: normocytic anaemia, thrombocytopenia, elevated IgM; DIC in severe rhodesiense infection
- Duration: weeks-months (*T. b. rhodesiense*) to months-years (*T. b. gambiense*)

**Stage 2 (meningoencephalitic stage):**
- Neuropsychiatric symptoms: personality change, irritability, confusion, hallucinations, depression
- Motor dysfunction: cerebellar ataxia, hyperreflexia, extrapyramidal signs (Kerandel's sign = delayed hyperaesthesia to pressure)
- **Circadian reversal**: pathognomonic sleep disorder — somnolence during day, insomnia at night; progressive → somnolence → stupor → coma → death
- Endocrine disruption: amenorrhoea, impotence, growth hormone dysregulation
- Without treatment: 100% fatal; with Stage 2 treatment: significant neurological sequelae common

**Staging criteria:**
Stage 2 is defined by CNS involvement: CSF lymphocyte count >5 cells/µL OR presence of trypanosomes in CSF (after lumbar puncture).

**Epidemiology:**

| Parameter | Value |
|:---|:---|
| Annual cases (2022) | ~992 (WHO; 97% *T. b. gambiense*) |
| Endemic countries | 36 sub-Saharan African countries |
| Animal reservoir | *T. b. rhodesiense*: cattle, game animals; *T. b. gambiense*: humans primary reservoir, pigs secondary |
| Vector | *Glossina* (tsetse fly); G. palpalis group (riverine, gambiense); G. morsitans group (savannah, rhodesiense) |
| WHO 2030 target | Elimination as public health problem (zero transmission) |

**Diagnosis:**

| Test | Stage | Notes |
|:---|:---|:---|
| CATT (Card Agglutination Test for Trypanosomiasis) | Stage 1 — gambiense screening | Rapid serological field test; high sensitivity but lower specificity |
| mAECT (Mini Anion Exchange Centrifugation Technique) | Stage 1 — parasitological confirmation | Concentrates trypanosomes from blood; gold standard confirmation |
| Microscopy (blood/lymph node aspirate/CSF) | Parasitological | Direct visualisation; lower sensitivity in early/low parasitaemia |
| Lumbar puncture + CSF analysis | Stage determination | Mandatory for all confirmed cases; >5 WBC/µL or trypanosomes in CSF = Stage 2 |
| rHAT Sero-K-SeT | Stage 1 — rapid diagnostic | Lateral flow RDT; approved WHO Essential Diagnostics List |

**Treatment:**

| Drug | Stage | Subspecies | Route | Notes |
|:---|:---|:---|:---|:---|
| Pentamidine | Stage 1 | *T. b. gambiense* | IM | Standard Stage 1 for gambiense; >95% cure rate |
| Suramin | Stage 1 | *T. b. rhodesiense* | IV | Stage 1 rhodesiense; complex dosing; nephrotoxicity |
| Fexinidazole | Stage 1 and 2 | Both (gambiense primarily) | Oral, 10 days | WHO approved 2019; first oral treatment for both stages; cure rate ~90%; neuropsychiatric AEs |
| NECT (Nifurtimox-Eflornithine combination therapy) | Stage 2 | *T. b. gambiense* | IV + oral | Previous Stage 2 standard; supplanted by fexinidazole where available |
| Eflornithine | Stage 2 | *T. b. gambiense* only | IV | Irreversible inhibitor of ornithine decarboxylase (ODC); *T. b. rhodesiense* has higher ODC turnover (resistance); 14-day IV regimen |
| Acoziborole | Stage 1 and 2 | *T. b. gambiense* | Single oral dose | Phase 3 trial; single dose treatment; highly promising for elimination campaigns |

[^matthews-2005-tbrucei]: Matthews KR. The developmental cell biology of Trypanosoma brucei. J Cell Sci. 2005;118(Pt 2):283–90.
[^who-hat-2021]: World Health Organization. Control and surveillance of human African trypanosomiasis. WHO Technical Report Series No. 984. WHO; 2013 (updated data 2022).
[^mandell-principles]: Bennett JE, Dolin R, Blaser MJ. Mandell, Douglas, and Bennett's Principles and Practice of Infectious Diseases. 9th ed. Elsevier; 2020.
[^murray-microbiology]: Murray PR, Rosenthal KS, Pfaller MA. Medical Microbiology. 9th ed. Elsevier; 2021.
