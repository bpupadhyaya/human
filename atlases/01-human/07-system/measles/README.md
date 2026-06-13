---
schema: human-scale-entry/v1
id: measles
name: Measles
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-08
summary: "Measles virus (MV; Morbillivirus; negative-sense ssRNA) caused ~128,000 deaths in 2021; SLAM/CD150 tropism enables immune amnesia (memory B/T cell depletion lasting 2-3 years); Koplik's spots and Warthin-Finkeldey giant cells are pathognomonic; MMR vaccine provides >97% efficacy."
aliases: ["measles", "rubeola", "measles virus", "MV", "Morbillivirus", "measles immune amnesia", "SSPE", "Warthin-Finkeldey", "Koplik's spots", "MMR vaccine", "measles encephalitis", "measles pneumonia", "measles bronchopneumonia", "immune amnesia virus"]
sources:
  - id: panum-1847-faroe-measles
    type: peer-reviewed
    cite: "Panum PL. Observations made during the epidemic of measles on the Faroe Islands in the year 1846. Med Classics. 1939;3:829-886."
    url: "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2536613/"
    accessed: "2026-06-08"
  - id: mina-2019-immune-amnesia
    type: peer-reviewed
    cite: "Mina MJ, Kula T, Leng Y, et al. Measles virus infection diminishes preexisting antibodies that offer protection from other pathogens. Science. 2019;366(6465):599-606."
    doi: "10.1126/science.aay6485"
    pmid: "31672891"
    url: "https://doi.org/10.1126/science.aay6485"
    accessed: "2026-06-08"
  - id: strebel-2019-measles-lancet
    type: peer-reviewed
    cite: "Strebel PM, Orenstein WA. Measles. N Engl J Med. 2019;381(4):349-357."
    doi: "10.1056/NEJMcp1905181"
    pmid: "31340710"
    url: "https://doi.org/10.1056/NEJMcp1905181"
    accessed: "2026-06-08"
cross_links:
  - target: 01-human/03-molecular/mv-h-protein
    relation: connects-to
    note: "MV-H (hemagglutinin) binds SLAM/CD150 on immune cells and nectin-4 on airway epithelium; H-F fusion complex drives syncytia (Warthin-Finkeldey cells); SLAM tropism enables immune amnesia by depleting memory B and T cells."
  - target: 01-human/03-molecular/mavs
    relation: connects-to
    note: "MV negative-sense ssRNA replication generates 5′ppp RNA → RIG-I → MAVS → IFN-β; MV V protein sequesters MDA5 and LGP2 → blocks MAVS activation; P protein blocks IRF3 phosphorylation; attenuated vaccine strains (Edmonston) with impaired V/P activate MAVS → faster clearance."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "MV V protein binds STAT1/STAT2 → blocks JAK-STAT signaling → ISG suppression; MV C protein blocks IFN-β induction; MV P/V proteins sequester MDA5/LGP2 → prevent MAVS-IRF3-IFN-β; wild-type MV IFN evasion is more complete than attenuated strains — key pathogenicity distinction."
  - target: 02-pathogen/01-viruses/measles-virus
    relation: connects-to
    note: "MV (Morbillivirus; negative-sense ssRNA; R₀ 12-18) is the causative agent; SLAM/CD150 attachment glycoprotein H mediates systemic lymphoid spread; F protein drives syncytia (Warthin-Finkeldey cells); persistent MV in neurons with hypermutated genome causes SSPE."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "MV-H binds SLAM/CD150 on dendritic cells → productive DC infection → impaired IL-12/IFN-α production and reduced T cell priming; MV-infected DCs poorly present antigens; DC dysfunction contributes to measles immune amnesia lasting 2-3 years post-infection."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "Measles immune amnesia (Mina 2019): MV SLAM/CD150 tropism infects SLAM-high memory B cells → erases 20-70% of pre-existing antibody diversity; naive B cells cannot reconstitute pathogen-specific memory → 2-3 years re-susceptibility to other infections after measles."
  - target: 01-human/04-cellular/b-cell
    relation: connects-to
    note: "Measles erases immune memory by destroying memory B cells: these cells carry the most SLAM/CD150 (3-10× naive B cells), exactly the receptor measles H protein binds, so the virus preferentially infects and deletes them — wiping out 20-70% of a child's antibody repertoire."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "Measles attacks the brain in several ways: acute post-infectious encephalitis and ADEM, and — years to decades later — SSPE, a fatal degeneration driven by hypermutated measles virus persisting in neurons; the MMR vaccine essentially eliminates all of these."
  - target: 01-human/07-system/tuberculosis
    relation: connects-to
    note: "Measles induces a profound, lasting immunosuppression that can reactivate latent tuberculosis: measles-infected dendritic cells make less IL-12, crippling the Th1 response that contains TB — one way post-measles immune amnesia raises susceptibility to other infections for years."
  - target: 01-human/07-system/influenza
    relation: connects-to
    note: "Both are vaccine-preventable respiratory viruses but differ sharply: measles (paramyxovirus) is among the most contagious pathogens (R0 12-18) and causes immune amnesia, while influenza (orthomyxovirus) drifts and shifts antigenically, needing annual reformulated vaccines."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "Pneumonia is the leading cause of measles death: the virus directly infects respiratory epithelium and, by erasing immune memory (immune amnesia), opens the door to secondary bacterial pneumonia for months afterward; giant-cell pneumonia can be fatal in the immunocompromised."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Measles both needs and subverts cytotoxic T cells: CD8+ T cells clear measles-infected cells and drive recovery, but the virus infects memory lymphocytes via CD150/SLAM and depletes them, causing 'immune amnesia' that erases pre-existing immunity to other pathogens for 2-3 years."
  - target: 01-human/07-system/rsv
    relation: connects-to
    note: "Measles and RSV are paramyxoviruses but cause very different disease: RSV is a bronchiolitis-causing pneumovirus of infants, while measles is a contagious morbillivirus with rash, fever, and Koplik spots—both can cause severe pneumonia, the leading killer in measles."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "Measles can attack neurons years after infection: persistent defective virus in the brain causes subacute sclerosing panencephalitis (SSPE), a fatal degenerative disease appearing years later—one reason measles is far more than a transient childhood rash."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Measles spreads through the body via myeloid cells: alveolar macrophages and dendritic cells in the airway are the first infected, carrying the virus to lymphoid tissue where it amplifies—so these innate sentinels become the vehicle for systemic measles dissemination."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "Natural killer cells help control measles early: NK and interferon responses limit initial viral spread, but measles still infects immune cells and causes profound, lasting immunosuppression—so the innate response is overwhelmed by a virus that targets immunity itself."
  - target: 01-human/07-system/hiv-aids
    relation: connects-to
    note: "Measles is especially dangerous in HIV and immunosuppression: without competent T-cell immunity, measles can cause giant-cell pneumonia and fatal disease without the typical rash, so live measles vaccine is contraindicated in severe immunosuppression."
  - target: 01-human/07-system/covid-19-disease
    relation: connects-to
    note: "Measles and COVID-19 illustrate herd-immunity thresholds at opposite extremes: measles is so contagious (R0 12-18) that ~95% vaccination is needed to stop spread, far above COVID's threshold—so falling measles vaccination quickly reignites outbreaks."
---

# Measles

## Overview

**Measles** (caused by measles virus, MV; family *Paramyxoviridae*, genus *Morbillivirus*) is a **highly contagious acute viral infection** — with a basic reproduction number (R₀) of 12-18, measles is the most transmissible human pathogen. Despite the existence of a safe, inexpensive, and >97%-efficacious vaccine (MMR), measles remains a significant cause of global child mortality: WHO estimates ~128,000 measles deaths in 2021, down from ~2.6 million annually in the pre-vaccine era but reflecting dangerous resurgences linked to vaccine hesitancy and supply disruptions.

The legendary epidemiological observation by **Peter Ludwig Panum in 1846** — who investigated a measles outbreak on the Faroe Islands and documented that elderly islanders who had been infected 65 years earlier were completely protected from reinfection — established that measles confers **lifelong immunity** after natural infection. This immunity requires adequate MV-specific memory B cells and neutralizing antibodies against MV-H and MV-F. The paradox of measles immunology is that while it induces strong long-lived immunity against MV itself, it simultaneously **destroys pre-existing immunological memory** to other pathogens — the phenomenon of **immune amnesia** [^mina-2019-immune-amnesia], now understood as a consequence of SLAM/CD150-expressing memory B and T cell infection and depletion.

**Public health crisis:** Multiple high-income countries lost measles-eliminated status in 2017-2019 due to vaccine hesitancy outbreaks (United States, Europe). The 2019 DRC outbreak exceeded 300,000 cases. COVID-19 pandemic disruptions caused global routine immunization to fall to 2008 levels by 2021, setting the stage for large resurgences.

## Structure

### MV genome and proteins

Measles virus has a ~16 kb negative-sense ssRNA genome (one of the largest among Paramyxoviridae) encoding **8 proteins** from 6 genes:

| Gene | Proteins | Function |
|------|----------|----------|
| **N (nucleoprotein)** | N | Encapsidates RNA → nucleocapsid (helical symmetry); serology target (anti-N IgM, anti-N IgG) |
| **P** | P, V, C | P: L-polymerase cofactor; **V**: IFN antagonist (cysteine-rich C-terminus; binds MDA5, LGP2, STAT1/2, IRF9); **C**: Short ORF; IFN-β antagonist; required for pathogenicity |
| **M (matrix protein)** | M | Virion assembly; bridges nucleocapsid and glycoproteins |
| **F (fusion protein)** | F | Class I viral fusogen; F0 cleaved by cathepsin/furin → F1+F2; drives cell-cell fusion → syncytia |
| **H (hemagglutinin)** | H | Receptor binding; binds SLAM/CD150 (immune cells), nectin-4 (epithelium); drives H-F fusion complex; target of neutralizing antibodies |
| **L (large protein)** | L | RNA-dependent RNA polymerase (RdRp); 5′-mRNA capping, N7-methylation |

Two proteins encoded by RNA editing (P gene): **V** (V-domain from P-gene RNA edited with one G insertion; V is the primary IFN antagonist) and **C** (alternative ORF from P gene).

### MV surface glycoproteins and receptor tropism

**Receptor switching — three phases of infection:**
1. **Lymph nodes / lymphoid organs** → H binds **SLAM/CD150** (signaling lymphocytic activation molecule; CD150) on **T cells, B cells, dendritic cells, macrophages** → systemic dissemination + immune suppression
2. **Lung** → H binds **SLAM/CD150** on alveolar macrophages and DC → RSV-like bronchiolitis
3. **Airway epithelium (shedding)** → H binds **nectin-4** (PVRL4; an adherens junction protein) on polarized bronchial epithelium → amplification and respiratory transmission
4. *(Historical)* **Neurons (SSPE)** → H-independent entry via unknown receptor + MV genome accumulation

**Atypical measles:** Historical vaccine VED (killed measles vaccine, 1960s) → non-neutralizing H antibodies + Th2 skew → on wild-type MV exposure → eosinophilic pneumonitis; abandoned in 1967.

## Function

### Immune amnesia — the most important measles biology

The **immune amnesia** phenomenon was mechanistically demonstrated by Mina et al. (2019) [^mina-2019-immune-amnesia] using the VirScan platform:
1. MV-H binds SLAM/CD150 on **memory B cells** (the cells with highest CD150 expression) → infects and depletes them preferentially
2. Loss of memory B cells → loss of 11-73% of pre-existing antibody diversity (depends on MV exposure duration)
3. Surviving naive B cells cannot compensate because they lack the antigen-specific memory necessary to reconstitute protection against previously cleared pathogens
4. **Clinical consequence**: Children recovering from measles are susceptible to previously controlled infections for **2-3 years** — this re-susceptibility to other pathogens explains why measles indirectly accounts for far more child deaths than direct measles mortality

**VirScan serology:** Comparing pre- and post-measles antibody repertoires showed measles erases 20-70% of antibody diversity (median ~40% loss) — the antigen-specific antibodies lost were those the child had accumulated through years of infection and vaccination.

**SLAM/CD150 expression on memory B cells** is the key determinant: Memory B cells express ~3-10× more SLAM than naive B cells → measles specifically targets the cells encoding immunological history.

### IFN evasion — the MV V/P/C system

MV has evolved one of the most sophisticated IFN evasion systems among RNA viruses:

**V protein:**
- N-terminal CARD-like domain (shared with P): Required for polymerase activity
- C-terminal cysteine-rich V-domain (unique to V): Multifunctional IFN antagonist
  - Binds **MDA5** and **LGP2** → sequesters RNA sensors → prevents MAVS activation
  - Binds **STAT1 and STAT2** → prevents JAK-STAT phosphorylation → ISG suppression
  - Binds **IRF9** → blocks ISGF3 assembly
  - Binds **IKKα** → blocks NF-κB-driven IFN-β induction in some contexts

**P protein:**
- Larger protein sharing N-terminus with V
- Sequesters **IRF3** → blocks TBK1-mediated IRF3 phosphorylation → prevents IFN-β transcription
- Coordinates with V for full IFN suppression

**C protein:**
- Short protein from alternative ORF of P gene
- Inhibits IFN-β induction independently; acts at MAVS level
- Required for efficient viral replication in vivo; C-deleted MV is attenuated

**Attenuated vaccine strains (Edmonston, Schwarz):** Multiple passages in non-immune cells selected for mutations in V and P that reduce IFN evasion efficiency → attenuated strains activate stronger innate IFN responses → faster clearance by immune cells → vaccine attenuation.

### Immunosuppression mechanisms

Beyond immune amnesia (memory B cell depletion), MV causes acute immune suppression through:
1. **IL-12 suppression**: MV-infected DCs produce less IL-12 → impaired Th1 responses → susceptibility to TB reactivation post-measles
2. **IL-10 upregulation**: MV-infected DCs → high IL-10 → anti-inflammatory; secondary immunosuppression
3. **FasL upregulation**: MV-infected cells express FasL → Fas-FasL killing of CD4+ T cells → lymphopenia
4. **mTOR-mediated anergy**: MV → mTOR inhibition in T cells → transcriptional anergy
5. **Lymphopenia**: Absolute lymphocyte count falls 40-60% during acute measles (B and T cells both lost)

## Pathology

### Clinical course and manifestations

**Incubation:** 8-12 days (range 7-21 days) from exposure to prodrome
**Prodrome (3-4 days):** Classic **3 C's**: Cough, Coryza (runny nose), Conjunctivitis (photophobia); high fever (>40°C); **Koplik's spots** (pathognomonic): transient white salt-grain-sized spots on buccal mucosa opposite molars; appear 1-2 days before rash
**Exanthem:** **Morbilliform (maculopapular) rash** begins behind ears → spreads centrifugally to trunk/extremities (3 days); rash is caused by MV-specific CD4+ T cell attack on MV-infected dermal capillary endothelium (not direct viral cytopathology)
**Infectivity:** Begins 4 days before rash; highest during prodrome; resolves 4 days after rash onset

**Warthin-Finkeldey giant cells:** Pathognomonic multinucleated syncytia formed by H-F fusion of infected lymphoid cells; visible in lymph nodes, tonsils, appendix, and lung on histology; created by MV F protein on infected cell surfaces fusing with SLAM+ neighbor cells.

### Complications

| Complication | Incidence | Mechanism | Risk factors |
|---|---|---|---|
| **Otitis media** | 7-9% | Secondary bacterial (Streptococcus, H. influenzae) | Age <5 years |
| **Pneumonia (primary)** | ~1-6% | MV-induced interstitial pneumonitis (giant cell pneumonia); Warthin-Finkeldey cells in alveoli | Immunocompromised, malnourished |
| **Secondary pneumonia** | ~5% | Bacterial superinfection (pneumococcus, Staph) | Any age |
| **Diarrhea** | ~8% | MV intestinal epithelial infection → mucosal damage | Developing countries; contributes to measles mortality |
| **Croup** | ~1-2% | MV-induced laryngotracheitis | Young children |
| **Acute measles encephalitis (AME)** | 1/1000 | MV-specific T cell-mediated autoimmune attack on CNS (not direct MV invasion) | Any age; high mortality/morbidity |
| **ADEM (acute disseminated encephalomyelitis)** | ~1/1000 | Autoimmune demyelination post-measles; similar to AME | Any age |
| **SSPE (subacute sclerosing panencephalitis)** | ~1-2/10,000; higher in <2 year infection | Persistent MV CNS infection with hypermutated genome; decades-later fatal encephalitis | First infection <2 years old |
| **Measles inclusion body encephalitis (MIBE)** | Rare; immunocompromised | Acute MV CNS replication without immune control | Immunosuppressed |
| **Vitamin A deficiency → blindness** | ~20,000/year globally | MV → conjunctivitis + vitamin A deficiency → corneal ulceration → blindness | Developing countries |

**SSPE (Subacute Sclerosing Panencephalitis):**
- Fatal progressive neurodegenerative disease occurring 5-15 years after acute measles (range 1-27 years)
- Caused by **persistent MV infection in neurons** with defective, hypermutated viral genome (accumulation of biased hypermutation in M, F, and H genes → non-cytopathic variant cannot complete replication cycle but persists in neurons)
- **MV M gene mutations** → loss of matrix protein assembly → virus cannot bud → neuronal spread only
- **MV H gene mutations** (especially in cytoplasmic tail) → altered antigenicity; allows escape from immune clearance in CNS
- **MV F gene biased hypermutation** (A-to-I/G RNA editing) → hyperfusogenic F → enhanced cell-cell spread → syncytium-mediated neuronal loss
- Clinical stages: Stage I (behavioral change, memory loss; EEG normal) → Stage II (myoclonic seizures, deteriorating cognition; EEG: Rademecker complexes) → Stage III (decorticate rigidity, coma) → Stage IV (death); total duration 1-3 years
- **Prevention**: MMR vaccine essentially eliminates SSPE risk; avoiding measles infection in infancy is the only prevention; no effective treatment

### Diagnosis

- **Clinical**: Rash + 3 C's + Koplik's spots during endemic period; straightforward
- **Serology**: MV IgM (positive 1-2 days after rash onset; peaks day 5-14; wanes by 30-60 days); MV IgG seroconversion
- **RT-PCR**: Throat/nasopharyngeal swab, urine, blood; gold standard for confirmation and genotyping; 10 WHO genotypes (A-D, F-H, N-D)
- **Virus culture**: BSL-2; not routine clinical use
- **Notifiable disease**: Mandated reporting in all WHO member states

### Treatment and prevention

**No approved antiviral therapy for measles.** Management is supportive:
- **Vitamin A supplementation**: WHO recommends for all children with measles in developing countries (reduces mortality 50%); mechanism: vitamin A → retinoic acid → epithelial integrity + IFN-γ production + ILC3 function; reduces pneumonia severity and measles-induced vitamin A deficiency
- Fever management; hydration; antibiotics for bacterial superinfections
- Ribavirin has in vitro activity but no established clinical benefit

**Prevention — MMR vaccine:**
- Live attenuated **Edmonston lineage** strains (USA: Moraten; Europe: Schwarz, Enders) for measles; combined with attenuated rubella (Wistar RA 27/3) and mumps (Jeryl Lynn or Urabe)
- **Primary schedule**: Dose 1 at 12-15 months; Dose 2 at 4-6 years; seroconversion rate >97% after two doses
- **Coverage threshold for elimination**: >95% two-dose coverage required in all age cohorts (R₀ ~12-18 requires >91-94% herd immunity)
- **MMRV** (measles-mumps-rubella-varicella): quadrivalent; approved; slightly higher febrile seizure risk in 12-23 month age group vs. MMR + separate varicella (∼1 extra febrile seizure per 2,300-2,600 doses MMRV vs. separate vaccines)
- **Maternal measles antibody waning**: Passively transferred maternal MV-IgG wanes by 4-6 months in exclusively formula-fed infants, 9-12 months in breastfed infants → window of susceptibility before MMR at 12 months

## Connections

**→ [MV-H Protein](../../../03-molecular/mv-h-protein/)**: MV-H (hemagglutinin) binds SLAM/CD150 on immune cells for systemic spread and nectin-4 on airway epithelium for respiratory shedding; H-F fusion complex drives syncytia formation (Warthin-Finkeldey giant cells); SLAM tropism is the mechanistic basis of measles-induced immune amnesia by targeting memory B and T cells.

**→ [MAVS](../../../03-molecular/mavs/)**: MV negative-sense RNA replication generates 5′ppp RNA intermediates → RIG-I → MAVS → TBK1/IRF3 → IFN-β; MV V protein sequesters MDA5 and LGP2 → prevents MAVS activation; MV P protein blocks IRF3 phosphorylation; attenuated vaccine strains with impaired V/P activate MAVS more robustly → faster innate response.

**→ [Type I Interferon](../../../03-molecular/type-i-interferon/)**: MV V protein binds STAT1/STAT2 → blocks JAK-STAT signaling → ISG suppression; MV C protein blocks IFN-β induction; V-domain mutations in attenuated Edmonston/Schwarz strains reduce STAT1 binding affinity → stronger type I IFN response in vaccinated individuals vs. WT MV infection → basis of vaccine attenuation.

- `connects-to` → **[Measles Virus](../../../02-pathogen/01-viruses/measles-virus/README.md)** — MV (Morbillivirus; negative-sense ssRNA; R₀ 12-18) is the causative agent; SLAM/CD150-binding H glycoprotein mediates systemic lymphoid spread; F protein drives syncytia (Warthin-Finkeldey cells); persistent MV with hypermutated genome causes SSPE.
- `connects-to` → **[Dendritic Cell](../../04-cellular/dendritic-cell/README.md)** — MV-H binds SLAM/CD150 on DCs → productive DC infection → impaired IL-12/IFN-α production and reduced T cell priming; MV-infected DCs poorly present antigens; DC dysfunction is a core driver of measles immune amnesia lasting 2-3 years.
- `connects-to` → **[Immune System](../../immune-system/README.md)** — Measles immune amnesia (Mina 2019): MV SLAM/CD150 tropism infects SLAM-high memory B cells → erases 20-70% of pre-existing antibody diversity; naive B cells cannot reconstitute pathogen-specific memory → 2-3 years re-susceptibility to other infections.
- `connects-to` → **[B Cell](../../04-cellular/b-cell/README.md)** — Measles erases immune memory by destroying memory B cells: these cells carry the most SLAM/CD150 (3-10× naive B cells), exactly the receptor measles H protein binds, so the virus preferentially infects and deletes them — wiping out 20-70% of a child's antibody repertoire.
- `connects-to` → **[Brain](../../06-organ/brain/README.md)** — Measles attacks the brain in several ways: acute post-infectious encephalitis and ADEM, and — years to decades later — SSPE, a fatal degeneration driven by hypermutated measles virus persisting in neurons; the MMR vaccine essentially eliminates all of these.
- `connects-to` → **[Tuberculosis](../tuberculosis/README.md)** — Measles induces a profound, lasting immunosuppression that can reactivate latent tuberculosis: measles-infected dendritic cells make less IL-12, crippling the Th1 response that contains TB — one way post-measles immune amnesia raises susceptibility to other infections for years.
- `connects-to` → **[Influenza](../influenza/README.md)** — Both are vaccine-preventable respiratory viruses but differ sharply: measles (paramyxovirus) is among the most contagious pathogens (R0 12-18) and causes immune amnesia, while influenza (orthomyxovirus) drifts and shifts antigenically, needing annual reformulated vaccines.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — Pneumonia is the leading cause of measles death: the virus directly infects respiratory epithelium and, by erasing immune memory (immune amnesia), opens the door to secondary bacterial pneumonia for months afterward; giant-cell pneumonia can be fatal in the immunocompromised.
- `connects-to` → **[Cytotoxic T Cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Measles both needs and subverts cytotoxic T cells: CD8+ T cells clear measles-infected cells and drive recovery, but the virus infects memory lymphocytes via CD150/SLAM and depletes them, causing 'immune amnesia' that erases pre-existing immunity to other pathogens for 2-3 years.
- `connects-to` → **[RSV](../rsv/README.md)** — Measles and RSV are paramyxoviruses but cause very different disease: RSV is a bronchiolitis-causing pneumovirus of infants, while measles is a contagious morbillivirus with rash, fever, and Koplik spots—both can cause severe pneumonia, the leading killer in measles.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — Measles can attack neurons years after infection: persistent defective virus in the brain causes subacute sclerosing panencephalitis (SSPE), a fatal degenerative disease appearing years later—one reason measles is far more than a transient childhood rash.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Measles spreads through the body via myeloid cells: alveolar macrophages and dendritic cells in the airway are the first infected, carrying the virus to lymphoid tissue where it amplifies—so these innate sentinels become the vehicle for systemic measles dissemination.
- `connects-to` → **[Natural Killer Cell](../../04-cellular/natural-killer-cell/README.md)** — Natural killer cells help control measles early: NK and interferon responses limit initial viral spread, but measles still infects immune cells and causes profound, lasting immunosuppression—so the innate response is overwhelmed by a virus that targets immunity itself.
- `connects-to` → **[HIV/AIDS](../hiv-aids/README.md)** — Measles is especially dangerous in HIV and immunosuppression: without competent T-cell immunity, measles can cause giant-cell pneumonia and fatal disease without the typical rash, so live measles vaccine is contraindicated in severe immunosuppression.
- `connects-to` → **[COVID-19 Disease](../covid-19-disease/README.md)** — Measles and COVID-19 illustrate herd-immunity thresholds at opposite extremes: measles is so contagious (R0 12-18) that ~95% vaccination is needed to stop spread, far above COVID's threshold—so falling measles vaccination quickly reignites outbreaks.

[^panum-1847-faroe-measles]: Panum PL. Observations made during the epidemic of measles on the Faroe Islands in the year 1846. *Med Classics.* 1939;3:829-886.
[^mina-2019-immune-amnesia]: Mina MJ, Kula T, Leng Y, et al. Measles virus infection diminishes preexisting antibodies that offer protection from other pathogens. *Science.* 2019;366(6465):599-606. [doi:10.1126/science.aay6485](https://doi.org/10.1126/science.aay6485) · [PubMed 31672891](https://pubmed.ncbi.nlm.nih.gov/31672891/)
[^strebel-2019-measles-lancet]: Strebel PM, Orenstein WA. Measles. *N Engl J Med.* 2019;381(4):349-357. [doi:10.1056/NEJMcp1905181](https://doi.org/10.1056/NEJMcp1905181) · [PubMed 31340710](https://pubmed.ncbi.nlm.nih.gov/31340710/)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
