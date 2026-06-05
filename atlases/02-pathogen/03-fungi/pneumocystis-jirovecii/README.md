---
schema: pathogen-entry/v1
id: pneumocystis-jirovecii
name: Pneumocystis jirovecii (formerly carinii)
atlas: 02-pathogen
scale: 03-fungi
status: draft
last_reviewed: 2026-06-05
summary: "Atypical Ascomycete fungus; obligate human lung pathogen lacking ergosterol. Causes Pneumocystis pneumonia (PCP) in immunocompromised hosts (HIV CD4 <200, transplant, steroid users). Treated with TMP-SMX; steroids added for moderate-severe disease."
aliases: ["P. jirovecii", "PCP", "Pneumocystis carinii", "pneumocystis pneumonia", "P. jirovecii pneumonia", "PJP"]
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
  - id: thomas-2004-pneumocystis-review
    type: peer-reviewed
    cite: "Thomas CF Jr, Limper AH. Pneumocystis pneumonia. N Engl J Med. 2004;350(24):2487-98."
    doi: "10.1056/NEJMra032588"
    pmid: "15190141"
    url: "https://doi.org/10.1056/NEJMra032588"
  - id: kovacs-2009-pcp-guideline
    type: peer-reviewed
    cite: "Kovacs JA, Masur H. Evolving health effects of Pneumocystis: one hundred years of progress in diagnosis and treatment. JAMA. 2009;301(24):2578-85."
    doi: "10.1001/jama.2009.880"
    pmid: "19549975"
    url: "https://doi.org/10.1001/jama.2009.880"
cross_links:
  - target: 01-human/06-organ/lung
    relation: damages
    note: "PCP causes bilateral diffuse alveolar damage with foamy intra-alveolar exudate and impaired gas exchange. Untreated PCP progresses to respiratory failure; mortality in ICU-admitted PCP patients exceeds 40% despite treatment."
  - target: 01-human/05-tissue/alveolus
    relation: infects
    note: "Trophic forms attach to type I pneumocytes via major surface glycoprotein and fibronectin, spreading across alveolar surfaces. Cysts rupture releasing ascospores that propagate infection throughout alveolar epithelium."
  - target: 01-human/07-system/immune-system
    relation: damages
    note: "Antigenic variation of the Msg surface glycoprotein family (>80 gene copies) evades antibody-mediated clearance. Loss of CD4+ T-cell help removes the critical signal for alveolar macrophage activation and fungal clearance."
  - target: 01-human/07-system/respiratory-system
    relation: damages
    note: "Bilateral interstitial pneumonitis causes progressive hypoxemia (PaO2 <70 mmHg or A-a gradient >35 mmHg in moderate-severe PCP), necessitating adjunctive corticosteroids to reduce inflammatory lung injury and lower the risk of respiratory failure."
---

# Pneumocystis jirovecii (formerly carinii)

## Overview

*Pneumocystis jirovecii* is a **taxonomically unusual fungus** — classified within the phylum Ascomycota but possessing biological characteristics that set it apart from virtually all other clinically significant fungi. It is an **obligate human pathogen** that cannot be cultured on standard fungal media, lacks the ergosterol that is the target of most antifungal drugs, and exists exclusively within the alveolar spaces of human lungs. These features make it both diagnostically challenging and therapeutically unique among the human fungal pathogens [^thomas-2004-pneumocystis-review].

Originally classified as a protozoan (1909; Chagas, then Delanöe), *Pneumocystis* was reclassified as a fungus in the 1980s following ribosomal RNA phylogenetic analysis. The species name *jirovecii* (replacing *carinii*, which refers to the rat-specific organism) was formalised in 2002 to honour Otto Jirovec, the Czech parasitologist who characterised the human-infecting form. The abbreviation PCP remains in use, now standing for **Pneumocystis pneumonia** or *Pneumocystis jirovecii* pneumonia (PJP) [^kovacs-2009-pcp-guideline].

*P. jirovecii* is the cause of **Pneumocystis pneumonia (PCP)**, one of the most important opportunistic infections defining the AIDS epidemic. Before the widespread use of antiretroviral therapy and prophylaxis, PCP was the **leading AIDS-defining illness** and the most common cause of death in HIV/AIDS patients in North America. In the modern era, it predominantly affects HIV-positive individuals with CD4 counts below 200 cells/µL who are not on prophylaxis, solid organ and bone marrow transplant recipients, patients on prolonged high-dose corticosteroids, those receiving biologic immunosuppressants, and individuals with primary immunodeficiencies.

The clinical presentation is characteristically **subacute**: progressive dyspnoea over days to weeks, non-productive cough, low-grade fever, and progressive hypoxemia — distinguishing PCP from the acute presentation of typical bacterial pneumonia. Untreated, PCP carries a mortality approaching **100%** in severely immunocompromised patients; with treatment, mortality ranges from **10–50%** depending on disease severity.

## Structure

### Morphological Forms

*P. jirovecii* has a complex life cycle within the alveolar space and exists in two principal morphological forms that are both diagnostically and biologically important:

| Form | Size | Description | Function |
|:---|:---|:---|:---|
| **Trophic form (trophozoite)** | 1–4 µm | Pleomorphic; single-membrane; thin cell wall; highly irregular surface with filopodia-like extensions; haploid | Adherent to type I pneumocyte surface; predominant form in infection; feeds and replicates |
| **Ascus (cyst form)** | 5–8 µm | Thick-walled, ovoid to spherical; contains 8 intracystic bodies (ascospores); mature cyst wall stains with methenamine silver (Gomori-GMS) and calcofluor white | Reproductive/transmission form; ruptures to release ascospores |
| **Intracystic bodies (ascospores)** | 1–2 µm | 8 per ascus; develop into trophic forms after cyst rupture | Propagate infection within alveolar spaces |
| **Precystic forms** | 3–5 µm | Intermediate developmental stages between trophic and cystic forms | Life cycle intermediates |

Trophic forms vastly outnumber cyst forms in infected lung tissue (ratio ~10:1 to 100:1 in favour of trophic forms). However, cysts are more reliably detected by histochemical stains and are the primary diagnostic target.

### Cell Wall — the Ergosterol-Absent Wall

The cell wall of *P. jirovecii* is fundamentally different from those of most pathogenic fungi:

**What it has:**
- **β-1,3-glucan:** Major cyst wall component; synthesised by Fks1 glucan synthase; recognised by Dectin-1 on alveolar macrophages → triggers innate immune activation (NF-κB, IL-8, TNF-α)
- **β-1,6-glucan and chitin:** Minor structural components in cyst wall
- **Major surface glycoprotein (Msg/gpA):** An abundant, extensively O- and N-glycosylated GPI-anchored protein family; encoded by ~80 gene copies in the genome; present on both trophic forms and cysts; the dominant surface antigen

**What it lacks — the critical pharmacological gap:**
- **Ergosterol is absent** from the *P. jirovecii* cell membrane — replaced by **cholesterol** acquired from the host alveolar epithelium
- This ergosterol absence confers **intrinsic resistance to azoles** (triazoles target CYP51/Erg11 in ergosterol biosynthesis), **amphotericin B** (targets ergosterol directly), and most other antifungal agents
- *FKS1* mutations conferring echinocandin resistance have been identified in *P. jirovecii*, though echinocandins are not the primary therapeutic class

### Genome and Obligate Parasitism

*P. jirovecii* has a **markedly reduced genome** (~7 Mb, encoding ~3,800 genes) — among the smallest of any pathogenic fungus:

- Genomic reduction reflects **obligate parasitic adaptation**: genes for amino acid, lipid, and cofactor biosynthesis are lost; the organism depends entirely on host cell-derived nutrients
- **No thymidylate synthase (TS) separate domain:** In most organisms, TS and dihydrofolate reductase (DHFR) are separate enzymes. In *P. jirovecii*, a bifunctional DHFR-TS fusion protein is the target of **TMP-SMX** (trimethoprim inhibits DHFR; sulfamethoxazole inhibits dihydropteroate synthase — the preceding enzyme in the folate pathway)
- **No in vitro cultivation:** Loss of key biosynthetic pathways renders the organism incapable of sustained growth outside a mammalian lung host; this makes susceptibility testing impossible with standard methods

## Infection Mechanism

### Transmission and Initial Pulmonary Entry

*P. jirovecii* is transmitted **person-to-person** via the airborne route (respiratory droplets or aerosols from colonised/infected individuals). Unlike most fungi, there is no well-characterised environmental reservoir for the human-specific species.

Key epidemiological features of transmission:
- **Ubiquitous human exposure:** Seroprevalence studies show that >80% of healthy children acquire anti-*Pneumocystis* antibodies by age 4, suggesting universal early exposure
- **Asymptomatic carriage:** Immunocompetent adults frequently carry low-level pulmonary *P. jirovecii* without disease; this colonisation state acts as a potential transmission reservoir
- **Hospital transmission:** Nosocomial clusters among immunosuppressed patients (transplant wards, haematology units) support significant healthcare-associated transmission
- **Molecular epidemiology:** Genotyping of Msg and Dihydropteroate synthase (DHPS) loci shows strain diversity, ruling out simple reactivation as the sole mechanism — acquisition of new strains from community/hospital contacts is common

### Alveolar Attachment — Trophic Form Adhesion

Following alveolar deposition, trophic forms establish intimate contact with **type I pneumocytes** (thin alveolar lining cells that cover >95% of alveolar surface area):

1. **Fibronectin-mediated adhesion:** *P. jirovecii* binds fibronectin deposited on the type I pneumocyte surface via surface mannoproteins and Msg; fibronectin-integrin (α5β1) interactions anchor trophic forms
2. **Msg/gpA direct binding:** Major surface glycoprotein binds directly to surface proteins on type I pneumocytes including A disintegrin and metalloprotease (ADAM) proteins
3. **Vitronectin and fibronectin matrix:** Alveolar ECM proteins are concentrated on the basal surface of type I pneumocytes; trophic forms flatten and spread along this surface, maximising host-contact area
4. **Cytoskeletal reorganisation:** Host actin reorganisation is induced at attachment sites; filopodia-like trophic form extensions interdigitate with microvilli of type I pneumocytes

### Cyst Development and Ascospore Release

The cyst form develops from trophic forms through a sexual life cycle:
1. Two trophic forms conjugate (cell fusion) → diploid zygote
2. Meiosis → tetrad → 8 haploid intracystic bodies (ascospores) within the developing ascus
3. Mature ascus (cyst) ruptures → 8 ascospores released into alveolar lumen → develop into new trophic forms
4. The empty ghost cyst remains in alveolar exudate — a diagnostically important remnant

### Alveolar Damage Mechanism

PCP lung damage is driven by **two compounding processes**:

**1. Direct fungal effects:**
- Dense coating of alveolar surfaces by trophic forms physically displaces surfactant, disrupts type I pneumocyte function, and impairs gas exchange
- β-1,3-glucan activates Dectin-1 → alveolar macrophage-derived ROS → oxidative injury to pneumocytes
- Protease activity contributes to alveolar protein accumulation and foamy exudate formation

**2. Host inflammatory response (dominant contributor to injury):**
- Alveolar macrophage activation → IL-8, TNF-α, IL-1β → neutrophil recruitment → neutrophil-mediated oxidant injury to alveolar epithelium
- Robust macrophage Dectin-1 signalling drives **NF-κB → cytokine storm** that exceeds the requirement for fungal clearance
- The characteristic **foamy intra-alveolar exudate** on histology reflects a mixture of destroyed type I pneumocytes, desquamated organisms (ghost cysts), surfactant, and proteinaceous inflammatory fluid
- **Surfactant dysfunction:** *P. jirovecii* produces beta-glucan that disrupts surfactant protein B and D function, compounding gas exchange failure; adjunctive corticosteroids work partly by preserving surfactant function and reducing inflammatory exudate

## Host Interactions

### Innate Immunity — Alveolar Macrophage and Dectin-1

Alveolar macrophages are the **primary innate effectors** against *P. jirovecii*:

| Receptor | Ligand | Response |
|:---|:---|:---|
| **Dectin-1** | β-1,3-glucan (cyst wall) | NF-κB activation → TNF-α, IL-6, IL-8, IL-12; NADPH oxidase assembly → ROS; key innate recognition signal |
| **Mannose receptor (CD206)** | Mannoproteins, Msg glycans | Phagocytosis; alternative pathway complement activation |
| **TLR2** | Msg glycoproteins | MyD88 → NF-κB → pro-inflammatory cytokines; cooperates with Dectin-1 |
| **SP-A and SP-D** | Msg binding | Opsonisation; agglutination of organisms; SP-D deficiency increases PCP susceptibility in animal models |

Alveolar macrophage fungicidal mechanisms include:
- **Oxidative burst:** ROS (superoxide, hydrogen peroxide, hydroxyl radical) generated by NADPH oxidase
- **Nitric oxide:** iNOS-derived NO and reactive nitrogen species (RNS) are critical; macrophages deficient in iNOS have impaired *Pneumocystis* killing
- **β-glucanase activity:** Limited direct enzymatic degradation of cyst walls

### Immune Evasion — Antigenic Variation of Msg

The most elegant *P. jirovecii* immune evasion strategy is **Msg antigenic variation**:

- The genome contains **~80 Msg gene copies** organised in subtelomeric loci; only **1 Msg gene is expressed at a time** from a unique transcriptional active locus (UCS — upstream conserved sequence)
- **Gene switching** at the UCS changes which Msg variant is expressed on the organism surface
- Since Msg is the dominant antibody target, surface switching allows the organism to escape B-cell memory responses
- **Consequence:** Even previously infected and recovered individuals can develop repeat PCP episodes, as antibodies to prior Msg variants do not protect against new-variant organisms

**Additional evasion mechanisms:**

| Mechanism | Detail |
|:---|:---|
| **Trophic form predominance** | Trophic forms have thinner walls and less exposed β-glucan than cysts; lower Dectin-1 stimulation per organism at high trophic form:cyst ratios |
| **Surfactant protein evasion** | Msg can bind SP-A and SP-D in a non-productive manner, competitively inhibiting functional opsonisation |
| **Complement evasion** | Limited complement activation on trophic form surface; GPI-anchored proteins interfere with C3b deposition |

### T-Cell Dependence — Why CD4 Count Matters

PCP is quintessentially a **CD4+ T-lymphocyte-dependent** infection:

- CD4+ T cells provide the **cognate T-cell help signal** (CD40L → CD40 on alveolar macrophages) required for full macrophage activation against *P. jirovecii*
- In CD4-depleted states, alveolar macrophages receive incomplete activation signals → residual Dectin-1 signalling drives **inflammatory injury** (IL-8, neutrophil recruitment) without effective fungal clearance → compounding lung damage without microbial control
- **CD8+ T cells** contribute to clearance but cannot fully compensate for CD4 loss; in CD8-depleted models, disease is less severe than CD4 depletion — confirming CD4 primacy
- **B cells and antibody:** Anti-Msg IgG antibodies contribute to opsonisation; CD40-deficient patients (Hyper-IgM syndrome) are PCP-susceptible even with normal CD4 counts, confirming importance of T-cell/B-cell collaboration
- **IFN-γ is the critical macrophage activation cytokine:** CD4+ Th1 cells produce IFN-γ → macrophage M1 polarisation → upregulation of iNOS, NADPH oxidase, and lysosomal killing capacity

## Connections

**Damages** → [Lung](../../../01-human/06-organ/lung/README.md): PCP produces bilateral diffuse alveolar damage — the foamy intra-alveolar exudate, type I pneumocyte destruction, and inflammatory cytokine storm collectively impair alveolar gas exchange. Without treatment, progressive hypoxemic respiratory failure is universal; ICU-admitted PCP carries >40% mortality. Lung damage is partly direct (organism-mediated) and substantially host-driven (macrophage-neutrophil inflammation).

**Infects** → [Alveolus](../../../01-human/05-tissue/alveolus/README.md): Trophic forms establish intimate attachment to type I pneumocytes via major surface glycoprotein and fibronectin-integrin interactions, flattening across the alveolar surface. Cyst wall β-1,3-glucan triggers Dectin-1 on alveolar macrophages, initiating the inflammatory cascade. Ascospore release propagates infection across alveolar surfaces.

**Damages** → [Immune system](../../../01-human/07-system/immune-system/README.md): Msg antigenic variation (>80 gene copies, single UCS expression site) allows the organism to evade B-cell memory and antibody-mediated clearance. Loss of CD4+ T-cell help — in HIV (CD4 <200), transplant, or iatrogenic immunosuppression — removes the critical macrophage activation signal, converting asymptomatic carriage into progressive pneumonia.

**Damages** → [Respiratory system](../../../01-human/07-system/respiratory-system/README.md): Bilateral interstitial pneumonitis causes progressive hypoxemia (PaO₂ <70 mmHg or A-a gradient >35 mmHg in moderate-severe PCP), necessitating adjunctive corticosteroids to reduce inflammatory lung injury and lower the risk of respiratory failure. Surfactant dysfunction and inflammatory exudate accumulation compound gas exchange impairment throughout the respiratory tree.

## Pathology

### Clinical Presentation

PCP has a **characteristic subacute presentation** that distinguishes it from typical bacterial pneumonia:

| Feature | Description |
|:---|:---|
| **Onset** | Subacute, over 1–4 weeks (HIV patients often more insidious; transplant/steroid patients more acute) |
| **Dyspnoea** | Progressive exertional dyspnoea; the dominant symptom; eventually present at rest |
| **Cough** | Non-productive or minimally productive; dry, persistent |
| **Fever** | Low-grade to moderate (38–39°C); less prominent than bacterial pneumonia |
| **Chest auscultation** | Often clear or with fine crackles; lack of consolidation signs distinguishes from lobar bacterial pneumonia |
| **Oxygen saturation** | May be preserved at rest initially; **exertional desaturation** is an early sensitive finding; room air walk test is clinically useful |

**Laboratory findings:**

| Test | Typical Finding | Significance |
|:---|:---|:---|
| **LDH** | Elevated (often >500 U/L; can exceed 1000 U/L) | Reflects alveolar epithelial cell destruction; correlates with disease severity; not specific |
| **Arterial blood gas** | Respiratory alkalosis; reduced PaO₂; widened A-a gradient | Severity staging: mild (A-a gradient <35), moderate-severe (≥35 or PaO₂ <70 mmHg) |
| **1,3-β-D-glucan (serum)** | Markedly elevated (>80 pg/mL) | Highly sensitive (>90%) for PCP; not specific (positive in other fungal infections); useful adjunct |
| **CBC** | May show lymphopenia; mild anaemia | Reflects underlying immunosuppression |
| **CD4 count (HIV)** | Almost invariably <200 cells/µL; often <100 | Defines risk threshold |

### Imaging

**Chest X-ray (CXR):**
- Classic: **bilateral perihilar, interstitial ("ground-glass")** pattern radiating from hila; "bat-wing" appearance
- Normal CXR does not exclude PCP (10–20% of cases early)
- Lobar consolidation or pleural effusion is atypical and suggests concurrent or alternative diagnosis

**High-resolution CT (HRCT):**
- More sensitive than CXR; reveals **bilateral ground-glass opacities (GGO)** even when CXR appears near-normal
- "Crazy paving" pattern (GGO + interlobular septal thickening)
- Cystic/pneumatocele formation (up to 35% of cases) — associated with spontaneous pneumothorax risk
- **Pneumothorax** (bilateral in severe PCP) is a recognised complication and may be the presenting event

### Diagnosis

**Gold standard: microscopic identification of organisms in respiratory specimens**

| Method | Specimen | Stain/Technique | Performance |
|:---|:---|:---|:---|
| **BAL (bronchoalveolar lavage)** | BAL fluid | GMS (Gomori methenamine silver), calcofluor white, Giemsa, DIF (direct immunofluorescence with anti-Msg antibodies) | Sensitivity 90–99%; gold standard specimen |
| **Induced sputum** | Induced sputum (3% hypertonic saline nebulisation) | DIF or GMS | Sensitivity 50–92%; non-invasive; preferred first-line if available |
| **Transbronchial biopsy** | Lung tissue | GMS; histology shows foamy intra-alveolar exudate | For BAL-negative cases; adds sensitivity |
| **PCR (BAL or induced sputum)** | BAL or sputum | Real-time PCR targeting *mtLSU rRNA* or *DHFR* | Highly sensitive (>95%); distinguishes colonisation from disease requires quantitative thresholds |

**Key staining principles:**
- **GMS (silver stain):** Stains cyst walls black on green background — the classic *Pneumocystis* appearance (collapsed "crushed ping-pong ball" cysts; 8 intracystic dots may be visible in well-stained sections)
- **DIF (direct immunofluorescence):** Monoclonal antibodies against Msg; detects both trophic forms and cysts; most sensitive single stain; requires fluorescence microscopy
- **Giemsa:** Stains intracystic bodies and trophic forms but not cyst walls; lower sensitivity for cysts

### Treatment

**First-line: TMP-SMX (Trimethoprim-Sulfamethoxazole)**

TMP-SMX is the definitive treatment and the cornerstone of PCP management. Its mechanism is **sequential folate pathway inhibition**:

1. **Sulfamethoxazole** inhibits **dihydropteroate synthase (DHPS)**: blocks conversion of para-aminobenzoic acid (PABA) → dihydropteroate (first step of folate synthesis)
2. **Trimethoprim** inhibits **dihydrofolate reductase (DHFR)**: blocks conversion of dihydrofolate → tetrahydrofolate (active form)
3. Combined blockade of sequential steps creates synergistic depletion of tetrahydrofolate → thymidylate synthesis failure → DNA synthesis arrest

| Setting | Dose | Duration |
|:---|:---|:---|
| **Mild PCP** | TMP 15-20 mg/kg/day + SMX 75-100 mg/kg/day PO in 3-4 divided doses | 21 days |
| **Moderate-severe PCP** | Same dose IV initially; switch to PO when clinically improving | 21 days |

**DHPS mutations (codons 55 and 57):** Point mutations in the DHPS gene — selected by sulfonamide prophylaxis — reduce sulfamethoxazole binding; associated with prior sulfonamide exposure and potentially with TMP-SMX treatment failure, though clinical significance debated.

**Alternative regimens (TMP-SMX intolerance/failure):**

| Regimen | Indication | Notes |
|:---|:---|:---|
| **Pentamidine IV** (4 mg/kg/day) | Severe PCP; TMP-SMX intolerance | Parenteral; significant toxicities: nephrotoxicity, hypoglycaemia, dysrhythmias |
| **Atovaquone** (1500 mg BID PO with fatty food) | Mild-moderate PCP | Inhibits mitochondrial electron transport (Cytochrome bc1); well tolerated; lower efficacy vs. TMP-SMX |
| **Primaquine + Clindamycin** | Moderate PCP; TMP-SMX failure | Primaquine: oxidant fungicidal; G6PD deficiency contraindication; clindamycin: uncertain mechanism against *Pneumocystis* |
| **Dapsone + TMP** | Mild-moderate PCP | Alternative to TMP-SMX in mild disease; dapsone inhibits DHPS similarly to SMX |

**Adjunctive Corticosteroids — evidence-based life-saving intervention:**

For **moderate-severe PCP** (PaO₂ <70 mmHg on room air or A-a gradient >35 mmHg):
- **Prednisolone** 40 mg BID (days 1–5) → 40 mg daily (days 6–10) → 20 mg daily (days 11–21)
- Or methylprednisolone IV if unable to take orally
- **Mechanism:** Reduces macrophage-neutrophil-driven inflammatory lung injury that compounds fungal damage; preserves surfactant function
- **Benefit:** Randomised trial evidence (NIH RCT, 1990) shows 50% reduction in mortality and respiratory failure with steroids in moderate-severe PCP
- **Timing:** Must be started **within 72 hours of antimicrobial therapy** to be effective

**Prophylaxis:**

| Indication | Regimen | Notes |
|:---|:---|:---|
| **HIV, CD4 <200 cells/µL** | TMP-SMX DS 1 tab daily (or 3×/week) | Discontinue when CD4 >200 cells/µL sustained on ART for 3 months |
| **Transplant recipients** | TMP-SMX DS 1 tab daily | Duration: 6-12 months post-transplant; lifelong if ongoing immunosuppression |
| **Prolonged high-dose steroids** | TMP-SMX DS 1 tab daily | Prednisone ≥20 mg/day for >4 weeks (common threshold) |
| **TMP-SMX intolerant** | Dapsone 100 mg daily, or atovaquone 1500 mg daily, or aerosolised pentamidine 300 mg monthly | Aerosolised pentamidine less effective; increased atypical PCP presentations |

### Epidemiology and Changing Landscape

- **Pre-ART era (1980s-1990s):** PCP occurred in ~70–80% of untreated HIV patients at some point; leading AIDS-defining illness and cause of death
- **Post-ART era:** Incidence fell dramatically after 1996 (introduction of HAART); in high-income countries, PCP now predominantly affects HIV-undiagnosed or ART-non-adherent patients
- **Non-HIV immunosuppressed patients:** The proportion of PCP in non-HIV hosts is rising as more patients receive biologics (rituximab, alemtuzumab, JAK inhibitors), prolonged corticosteroids, and immunosuppression after organ transplantation
- **Mortality:** 10–15% in HIV patients treated appropriately; 30–60% in non-HIV immunosuppressed patients (higher inflammatory response in non-HIV hosts contributes to worse outcomes even with treatment)
- **Prophylaxis thresholds in non-HIV patients** remain debated; CD4 count thresholds are less reliable; lymphocyte counts <200/µL and CD4+ T-cell counts <200/µL correlate with risk in non-HIV settings

---

*This page is co-maintained by human expert review and AI-assisted synthesis. Content reflects published medical literature as of 2026-06-05 and should not be used as clinical guidance. See [equalinformation.com/human](https://equalinformation.com/human) for project details; contact bpupadhyaya@gmail.com.*

[^thomas-2004-pneumocystis-review]: Thomas CF Jr, Limper AH. Pneumocystis pneumonia. *N Engl J Med.* 2004;350(24):2487-98. [doi:10.1056/NEJMra032588](https://doi.org/10.1056/NEJMra032588) · [PubMed 15190141](https://pubmed.ncbi.nlm.nih.gov/15190141/)
[^kovacs-2009-pcp-guideline]: Kovacs JA, Masur H. Evolving health effects of Pneumocystis: one hundred years of progress in diagnosis and treatment. *JAMA.* 2009;301(24):2578-85. [doi:10.1001/jama.2009.880](https://doi.org/10.1001/jama.2009.880) · [PubMed 19549975](https://pubmed.ncbi.nlm.nih.gov/19549975/)
[^mandell-principles]: Bennett JE, Dolin R, Blaser MJ. *Mandell, Douglas, and Bennett's Principles and Practice of Infectious Diseases.* 9th ed. Elsevier; 2020.
[^murray-microbiology]: Murray PR, Rosenthal KS, Pfaller MA. *Medical Microbiology.* 9th ed. Elsevier; 2021.
