---
schema: human-scale-entry/v1
id: hiv-aids
name: HIV/AIDS
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-08
summary: "HIV/AIDS (HIV-1; retrovirus; CCR5/CXCR4 co-receptor) systematically depletes CD4+ T cells → immunodeficiency → AIDS-defining illnesses; ART (antiretrovirals, 6+ classes) suppresses viral load to undetectable; U=U (Undetectable = Untransmittable) prevents sexual transmission."
aliases: ["HIV", "human immunodeficiency virus", "AIDS", "acquired immunodeficiency syndrome", "HIV-1", "HIV-2", "PLHIV", "ART", "antiretroviral therapy", "HAART"]
sources:
  - id: barre-sinoussi-1983-hiv
    type: peer-reviewed
    cite: "Barré-Sinoussi F, Chermann JC, Rey F, et al. Isolation of a T-lymphotropic retrovirus from a patient at risk for acquired immune deficiency syndrome (AIDS). Science. 1983;220(4599):868-871."
    doi: "10.1126/science.6189183"
    pmid: "6189183"
    url: "https://doi.org/10.1126/science.6189183"
    accessed: "2026-06-08"
  - id: dhhs-2024-hiv-guidelines
    type: clinical-guideline
    cite: "Panel on Antiretroviral Guidelines for Adults and Adolescents. Guidelines for the Use of Antiretroviral Agents in Adults and Adolescents with HIV. US Department of Health and Human Services. 2024."
    url: "https://clinicalinfo.hiv.gov/en/guidelines"
    accessed: "2026-06-08"
cross_links:
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "HIV-1 entry requires CD4 + CCR5 (R5-tropic, early infection) or CXCR4 (X4-tropic, late/AIDS stage); CCR5-Δ32 homozygosity → complete HIV-1 resistance; maraviroc (CCR5 antagonist) requires prior tropism testing (Trofile assay) to exclude X4-tropic virus."
  - target: 01-human/07-system/tuberculosis
    relation: connects-to
    note: "HIV-TB co-infection is the most lethal pathogen combination: HIV depletes CD4+ Th1 cells → granuloma dissolution → TB reactivation; TB is the leading cause of AIDS death; concurrent ART + HRZE reduces mortality; IRIS complicates early ART in TB-HIV co-infection."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "HIV-1 depletes CD4+ T cells (gp120 → CD4/CCR5 → fusion → reverse transcription → integration → viral DNA); AIDS defined as CD4 <200/μL or AIDS-defining illness; chronic immune activation drives T cell exhaustion and monocyte dysregulation even with ART."
  - target: 01-human/07-system/anemia-of-chronic-disease
    relation: connects-to
    note: "HIV drives ACD via sustained immune activation → IL-6 + IFN-γ → hepcidin elevation → functional iron deficiency; AZT-induced bone marrow suppression adds an aplastic component; severity correlates with viral load and CD4 count; ART reduces ACD severity."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "IL-12/IFN-γ axis is severely impaired in HIV-AIDS: HIV depletes CD4+ Th1 cells → ↓IFN-γ → ↓macrophage activation; DCs in AIDS produce less IL-12; IL-12 deficiency → susceptibility to TB, NTM, Leishmania, and dimorphic fungi; ART partially restores IL-12 responsiveness."
  - target: 01-human/07-system/leishmaniasis
    relation: connects-to
    note: "HIV-VL co-infection: CD4+ Th1 cell depletion → loss of IFN-γ → Leishmania escapes macrophage control → disseminated VL; Mediterranean Europe, East Africa, and Indian subcontinent are co-endemic zones; ART partially restores anti-Leishmania Th1 immunity; L-AmB prophylaxis needed."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "AIDS is defined by the loss of CD4+ T helper cells: as HIV drives their count below 200/μL, cell-mediated immunity collapses, opening the door to the opportunistic infections and cancers that define the syndrome; ART restores ~100-150 cells/μL per year."
  - target: 02-pathogen/03-fungi/pneumocystis-jirovecii
    relation: connects-to
    note: "Pneumocystis jirovecii pneumonia (PCP) is the classic AIDS-defining infection, striking once CD4 falls below 200/μL: this fungus causes a diffuse interstitial pneumonia, treated and prevented with trimethoprim-sulfamethoxazole — prophylaxis started at that CD4 threshold."
  - target: 01-human/07-system/pcnsl
    relation: connects-to
    note: "Primary CNS lymphoma is an AIDS-defining malignancy of profound immunosuppression (CD4 <50/μL): unchecked Epstein-Barr virus drives a brain B-cell lymphoma, and restoring immunity with ART is central to treatment alongside methotrexate or radiation."
  - target: 02-pathogen/01-viruses/hiv-1
    relation: connects-to
    note: "AIDS is the late stage of HIV-1 infection: years of unchecked viral replication deplete CD4 T cells below ~200/µL, collapsing cell-mediated immunity and opening the door to opportunistic infections and cancers; antiretroviral therapy suppressing HIV-1 prevents and can reverse it."
  - target: 01-human/07-system/cervical-cancer
    relation: connects-to
    note: "Cervical cancer is an AIDS-defining illness: HIV-driven immunosuppression lets oncogenic HPV persist and progress faster to invasive cancer, so women with HIV face markedly higher risk; antiretroviral therapy and HPV vaccination plus screening are key preventive measures."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "AIDS reflects the collapse of T-cell immunity: as CD4 helper cells fall, CD8+ cytotoxic T cells lose the help they need and become exhausted, so cell-mediated control of viruses, intracellular bacteria and tumors fails—explaining the opportunistic infections that define AIDS."
  - target: 01-human/07-system/hiv
    relation: connects-to
    note: "HIV/AIDS is the disease end of HIV infection: as the retrovirus depletes CD4 T cells, defenses collapse and AIDS-defining opportunistic infections and cancers appear—so the pathogen and the syndrome name one continuum, now arrested early by antiretroviral therapy."
  - target: 01-human/07-system/burkitt-lymphoma
    relation: connects-to
    note: "Burkitt lymphoma is an AIDS-defining cancer: HIV-driven immune dysregulation and chronic B-cell activation, often with EBV co-infection, raise Burkitt risk even at preserved CD4 counts—so a fast-growing lymphoma in an HIV patient is Burkitt until proven otherwise."
  - target: 01-human/07-system/hepatitis-b
    relation: connects-to
    note: "HIV and hepatitis B frequently coinfect via shared blood and sexual routes: HIV accelerates HBV liver fibrosis, and several antiretrovirals (tenofovir, lamivudine) suppress both viruses—so HIV regimens are chosen to cover HBV and avoid flares if stopped."
---

# HIV/AIDS

## Overview

Human Immunodeficiency Virus (HIV-1) is a **lentivirus** (genus *Lentivirus*, family *Retroviridae*) first isolated by Barré-Sinoussi and colleagues in 1983 [^barre-sinoussi-1983-hiv]. HIV-1 and the related HIV-2 (less virulent, West Africa) cause **acquired immunodeficiency syndrome (AIDS)** by progressively depleting CD4⁺ T helper cells until cell-mediated immunity collapses, leaving the host vulnerable to AIDS-defining opportunistic infections and malignancies.

**Global burden (2023):**
- ~39 million people living with HIV (PLHIV) globally
- ~1.3 million new infections per year
- ~630,000 AIDS-related deaths per year (down from 2M/year peak in 2004)
- Sub-Saharan Africa carries ~65% of global HIV burden
- ~29.8 million PLHIV on antiretroviral therapy (ART)

**Transformative paradigm: U=U (Undetectable = Untransmittable)**

HIV-positive individuals with sustained undetectable viral load on ART pose **zero risk** of sexual HIV transmission to HIV-negative partners (PARTNER, Opposites Attract, HPTN 052 studies). This scientific finding has transformed HIV prevention and destigmatisation.

**Epidemiology:**
- Transmission: sexual (most common globally: vaginal and anal intercourse); mother-to-child (pregnancy, delivery, breastfeeding); blood (injecting drug use, transfusion, needlestick)
- Anal sex carries ~18× higher per-act transmission risk than vaginal sex
- Primary risk co-factors: other STIs (especially HSV-2, ulcerative STIs disrupt mucosal barrier), high viral load in the source partner, acute/early HIV infection (peak viremia), lack of male circumcision

## Structure

### HIV-1 Virion and Genome

The **HIV-1 virion** (~120 nm spherical particle) is enveloped and architecturally complex:

| Component | Structure | Function |
|:----------|:----------|:---------|
| **Envelope (Env)** | gp120/gp41 trimeric spikes (~72 per virion); gp120 = surface; gp41 = transmembrane | CD4 binding (gp120); membrane fusion (gp41 heptad repeats) |
| **Matrix (MA/p17)** | Beneath lipid bilayer | Structural integrity; mediates nuclear import of PIC |
| **Capsid (CA/p24)** | Fullerene cone; ~1,200 CA monomers | Protects viral RNA; interacts with host restriction factors (TRIM5α, cyclophilin A) |
| **Nucleocapsid (NC/p7)** | Zinc-finger protein, coats viral RNA | RNA packaging, reverse transcription chaperone |
| **Genome** | Two copies of (+)ssRNA; 9.8 kb; 9 genes | Genetic blueprint; dimerises via dimerisation initiation site (DIS) |
| **Enzymes** | Reverse transcriptase (RT), integrase (IN), protease (PR) | Replication, integration, polyprotein processing |

**HIV-1 genome organisation:**
- **Structural genes:** *gag* (MA/CA/NC/p6), *pol* (PR/RT/IN), *env* (gp120/gp41)
- **Regulatory:** *tat* (transcriptional transactivator, HIV-LTR → 100× transcription boost), *rev* (nuclear export of unspliced mRNAs via RRE)
- **Accessory:** *vif* (degrades APOBEC3G restriction), *vpr* (G2 arrest, nuclear import), *vpu* (CD4 degradation, BST-2/tetherin antagonism), *nef* (CD4/MHC-I downregulation, virion infectivity)

### HIV-1 Clades

HIV-1 is divided into four groups (M, N, O, P), with Group M comprising >90% of global infections. Group M subtype B (Europe, Americas, Australia) is the most studied in clinical research; subtype C (sub-Saharan Africa, India) accounts for ~50% of global infections.

## Function

### HIV-1 Replication Cycle

1. **Attachment and entry:** gp120 binds CD4 (Kd ~4 nM) → conformational change exposes V3 loop → V3 + bridging sheet contact CCR5 (or CXCR4) → gp41 hairpin refolding → six-helix bundle → membrane fusion → capsid released into cytoplasm
2. **Reverse transcription:** RT converts (+)ssRNA → dsDNA (via RNA:DNA hybrid intermediate); RNA strand degraded by RT RNase H domain → ss(-) DNA → complementary (+) strand synthesis → blunt-ended linear dsDNA (10.0 kb)
3. **Nuclear import:** Pre-integration complex (PIC: dsDNA + MA + IN + LEDGF/p75) enters nucleus via nuclear pore; LEDGF/p75 tethers PIC to chromatin
4. **Integration:** IN catalyses strand transfer → HIV-1 proviral DNA inserted into host genome (preferentially in active transcription units); INSTI drugs (raltegravir, elvitegravir, dolutegravir, bictegravir) block integration
5. **Transcription:** HIV-LTR → Pol II → early spliced mRNAs (*tat*, *rev*, *nef*); Tat → P-TEFb (CDK9/cyclinT1) → phosphorylates RNA Pol II → full-length genomic RNA; Rev → nuclear export of unspliced gRNA and partially spliced mRNAs
6. **Assembly:** Gag and GagPol polyproteins bud at plasma membrane; MA targets Env (gp41) into budding sites
7. **Budding:** ESCRT pathway (TSG101, ALIX) mediates membrane scission → immature virion released
8. **Maturation:** PR cleaves Gag/GagPol polyproteins → capsid condensation → infectious virion; PI drugs block PR

### CD4⁺ T Cell Depletion

HIV-1 pathogenesis is primarily driven by CD4⁺ T cell loss:
- **Direct killing:** Viral cytopathic effect (accumulation of unintegrated viral DNA; apoptosis via Env/CD4 signalling)
- **Bystander killing:** HIV-infected macrophages and DCs kill uninfected CD4⁺ T cells via pyroptosis (cGAS-STING sensing of abortive viral DNA → IL-1β → CD4 T cell death — the dominant mechanism in lymph nodes)
- **Immune activation:** Translocated gut microbial products (LPS) drive chronic immune activation → T cell exhaustion → functional CD4 depletion exceeding absolute depletion

**CD4 count and clinical correlates:**
| CD4 Count | Immune Status | Risks |
|:----------|:-------------|:------|
| >500/μL | Normal range | HIV replication; mild immune impairment |
| 200–500/μL | Mild-moderate | Recurrent bacterial infections; oral thrush; herpes zoster |
| <200/μL | AIDS | *Pneumocystis jirovecii* pneumonia (PCP), CMV retinitis, toxoplasmosis |
| <100/μL | Severe AIDS | Cryptococcal meningitis, MAC (Mycobacterium avium complex) |
| <50/μL | Profound AIDS | CMV colitis, progressive multifocal leukoencephalopathy (PML) |

## Pathology

### Antiretroviral Therapy (ART)

**Six classes of approved antiretroviral drugs** [^dhhs-2024-hiv-guidelines]:

| Class | Mechanism | Key Drugs | Resistance Pathway |
|:------|:----------|:---------|:-------------------|
| **NRTI** (nucleoside RT inhibitors) | Compete with natural dNTPs → chain termination | Tenofovir (TDF/TAF), emtricitabine (FTC), abacavir (ABC), lamivudine (3TC), zidovudine (AZT) | M184V (3TC/FTC resistance); K65R (TDF); TAMs (thymidine analogue mutations) |
| **NNRTI** (non-nucleoside RT inhibitors) | Allosteric RT inhibition (palm subdomain) | Efavirenz, rilpivirine, doravirine, etravirine | K103N (efavirenz); E138K (rilpivirine) |
| **PI** (protease inhibitors) | Block GagPol polyprotein cleavage | Darunavir/r (boosted), atazanavir/r | Complex patterns; boosting with RTV/COBI prevents resistance |
| **INSTI** (integrase strand transfer inhibitors) | Block HIV-1 integrase strand transfer step | Dolutegravir (DTG), bictegravir (BIC), raltegravir, elvitegravir/c | N155H, Q148H (RAL/EVG); DTG/BIC has higher barrier to resistance |
| **Fusion inhibitor** | Block gp41-mediated membrane fusion | Enfuvirtide (T-20) | gp41 HR1 mutations; injectable only; rarely used |
| **CCR5 antagonist** | Block gp120/CCR5 co-receptor binding | Maraviroc | Tropism switch to X4; requires pre-treatment tropism assay |
| **CD4-attachment inhibitor** | Block gp120/CD4 primary receptor | Fostemsavir (prodrug of temsavir) | gp120 BMS pocket mutations |
| **Capsid inhibitor** | Block capsid-mediated nuclear import + assembly | Lenacapavir | Capsid mutations; injectable every 6 months |

**Preferred initial regimens (DHHS 2024):**
- **BIC/TAF/FTC** (Biktarvy): Single-pill once-daily; high barrier to resistance; most prescribed globally
- **DTG/ABC/3TC** (Triumeq): HLA-B*5701 test required before ABC (hypersensitivity)
- **DTG + TAF/FTC** (separate): Alternative

**Goal:** Viral load <20–50 copies/mL within 24 weeks; CD4 count recovery (~100–150 cells/μL per year).

### HIV Prevention

- **PrEP (Pre-Exposure Prophylaxis):** Daily TDF/FTC (Truvada) or TAF/FTC (Descovy) reduces HIV acquisition by >99% in adherent MSM (iPrEX trial); daily oral PrEP widely recommended; **cabotegravir LA** (Apretude; long-acting injectable cabotegravir every 8 weeks) demonstrated superiority to daily oral TDF/FTC (HPTN 083/084)
- **PEP (Post-Exposure Prophylaxis):** Within 72 hours of exposure; 28-day course TDF/FTC + DTG; ~80% effective
- **Male circumcision:** 60% reduction in female-to-male HIV transmission (VMMC — voluntary medical male circumcision)
- **PMTCT (Prevention of Mother-to-Child Transmission):** ART during pregnancy + intrapartum + infant NVP → <1% MTCT rate (from ~45% without intervention)

### HIV Cure Strategies

- **Functional cure:** Durable viral suppression without ART (achieved in >10 individuals after HSCT from CCR5-Δ32 donors — "Berlin/London/Düsseldorf/City of Hope/Geneva/New York patients")
- **Shock-and-kill (latency reversal):** LRAs (latency-reversing agents: IL-15, HDAC inhibitors, TLR7 agonists) to reactivate latent reservoir → ART + immune clearance → clinical trials ongoing; limited efficacy to date
- **Gene editing:** CCR5 knockout of CD4⁺ T cells and HSCs (ZFN, CRISPR-Cas9) — Phase I/II trials (SB-728, Excision BioTherapeutics); not yet approved

## Connections

- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — HIV-1 gp120 binds CD4 then CCR5 (R5-tropic) or CXCR4 (X4-tropic) as co-receptor for membrane fusion; CCR5-Δ32 homozygosity confers near-complete HIV-1 resistance; maraviroc blocks CCR5; HSCT from Δ32 donors has achieved functional HIV cure.
- `connects-to` → **[Tuberculosis](../tuberculosis/README.md)** — TB is the leading AIDS-defining cause of death; HIV depletes CD4⁺ Th1 cells → granuloma destabilisation → TB reactivation; HIV-TB co-infection requires simultaneous ART + HRZE; IRIS (immune reconstitution inflammatory syndrome) complicates early ART in TB-HIV; WHO recommends ART regardless of CD4 count in TB-HIV co-infection.
- `connects-to` → **[Immune System](../immune-system/README.md)** — HIV-1 systematically destroys CD4⁺ T helper cells (primary reservoir) and impairs DC antigen presentation, NK cytotoxicity, and B cell memory; AIDS is defined by CD4 <200 cells/μL or AIDS-defining illness; chronic immune activation persists despite ART (residual inflammation, T cell exhaustion, monocyte dysregulation).
- `connects-to` → **[Anemia of Chronic Disease](../anemia-of-chronic-disease/README.md)** — HIV drives ACD through sustained immune activation → IL-6 + IFN-γ → hepcidin elevation; AZT-related bone marrow suppression adds a direct aplastic component; anemia severity tracks viral load and CD4 count; ART suppression improves ACD within months.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — IL-12/IFN-γ axis is profoundly impaired in HIV-AIDS: CD4⁺ Th1 depletion → ↓IFN-γ; HIV-infected DCs produce less IL-12; the resulting Th1 deficiency explains susceptibility to TB, NTM, Leishmania, and dimorphic fungi; ART partially restores IL-12 pathway function.
- `connects-to` → **[Leishmaniasis](../leishmaniasis/README.md)** — HIV-VL co-infection: CD4+ Th1 cell depletion → loss of IFN-γ → Leishmania escapes macrophage control → disseminated VL; Mediterranean Europe, East Africa, and Indian subcontinent are co-endemic zones; ART partially restores anti-Leishmania Th1 immunity; L-AmB prophylaxis needed.
- `connects-to` → **[T Helper Cell](../../04-cellular/t-helper-cell/README.md)** — AIDS is defined by the loss of CD4+ T helper cells: as HIV drives their count below 200/μL, cell-mediated immunity collapses, opening the door to the opportunistic infections and cancers that define the syndrome; ART restores ~100-150 cells/μL per year.
- `connects-to` → **[Pneumocystis jirovecii](../../../02-pathogen/03-fungi/pneumocystis-jirovecii/README.md)** — Pneumocystis jirovecii pneumonia (PCP) is the classic AIDS-defining infection, striking once CD4 falls below 200/μL: this fungus causes a diffuse interstitial pneumonia, treated and prevented with trimethoprim-sulfamethoxazole — prophylaxis started at that CD4 threshold.
- `connects-to` → **[Primary CNS Lymphoma](../pcnsl/README.md)** — Primary CNS lymphoma is an AIDS-defining malignancy of profound immunosuppression (CD4 <50/μL): unchecked Epstein-Barr virus drives a brain B-cell lymphoma, and restoring immunity with ART is central to treatment alongside methotrexate or radiation.
- `connects-to` → **[Human Immunodeficiency Virus type 1](../../../02-pathogen/01-viruses/hiv-1/README.md)** — AIDS is the late stage of HIV-1 infection: years of unchecked viral replication deplete CD4 T cells below ~200/µL, collapsing cell-mediated immunity and opening the door to opportunistic infections and cancers; antiretroviral therapy suppressing HIV-1 prevents and can reverse it.
- `connects-to` → **[Cervical Cancer](../cervical-cancer/README.md)** — Cervical cancer is an AIDS-defining illness: HIV-driven immunosuppression lets oncogenic HPV persist and progress faster to invasive cancer, so women with HIV face markedly higher risk; antiretroviral therapy and HPV vaccination plus screening are key preventive measures.
- `connects-to` → **[Cytotoxic T Cell](../../04-cellular/t-cytotoxic-cell/README.md)** — AIDS reflects the collapse of T-cell immunity: as CD4 helper cells fall, CD8+ cytotoxic T cells lose the help they need and become exhausted, so cell-mediated control of viruses, intracellular bacteria and tumors fails—explaining the opportunistic infections that define AIDS.
- `connects-to` → **[HIV](../hiv/README.md)** — HIV/AIDS is the disease end of HIV infection: as the retrovirus depletes CD4 T cells, defenses collapse and AIDS-defining opportunistic infections and cancers appear—so the pathogen and the syndrome name one continuum, now arrested early by antiretroviral therapy.
- `connects-to` → **[Burkitt Lymphoma](../burkitt-lymphoma/README.md)** — Burkitt lymphoma is an AIDS-defining cancer: HIV-driven immune dysregulation and chronic B-cell activation, often with EBV co-infection, raise Burkitt risk even at preserved CD4 counts—so a fast-growing lymphoma in an HIV patient is Burkitt until proven otherwise.
- `connects-to` → **[Hepatitis B](../hepatitis-b/README.md)** — HIV and hepatitis B frequently coinfect via shared blood and sexual routes: HIV accelerates HBV liver fibrosis, and several antiretrovirals (tenofovir, lamivudine) suppress both viruses—so HIV regimens are chosen to cover HBV and avoid flares if stopped.

## See Also

- [^barre-sinoussi-1983-hiv] Barré-Sinoussi F et al. Isolation of a T-lymphotropic retrovirus from a patient at risk for AIDS. *Science.* 1983;220(4599):868-871. [doi:10.1126/science.6189183](https://doi.org/10.1126/science.6189183) · [PubMed 6189183](https://pubmed.ncbi.nlm.nih.gov/6189183/)
- [^dhhs-2024-hiv-guidelines] Panel on Antiretroviral Guidelines for Adults and Adolescents. *Guidelines for the Use of Antiretroviral Agents in Adults and Adolescents with HIV.* US DHHS. 2024. [clinicalinfo.hiv.gov](https://clinicalinfo.hiv.gov/en/guidelines)
- Related entries: [ccr5](../../03-molecular/ccr5/README.md), [tuberculosis](../tuberculosis/README.md), [immune-system](../immune-system/README.md), [il-12](../../03-molecular/il-12/README.md)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
