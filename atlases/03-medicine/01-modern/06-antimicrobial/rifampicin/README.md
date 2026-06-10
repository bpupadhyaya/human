---
schema: medicine-entry/v1
id: rifampicin
name: Rifampicin
atlas: 03-medicine
scale: 01-modern
status: draft
last_reviewed: 2026-06-04
summary: "Semisynthetic rifamycin antibiotic and potent CYP3A4/P-gp inducer. Bactericidal against dividing and dormant mycobacteria via rpoB RNA polymerase inhibition. Backbone of first-line TB (HRZE); also used in leprosy, meningococcal prophylaxis, and MRSA biofilm."
aliases: ["rifampin", "rifampicine", "rifaldazine", "Rimactane", "Rifadin", "RIF", "R (in TB regimen notation)"]
drug_class: rifamycin antibiotic
modality: small molecule
key_agents:
  - rifampicin
  - rifampin
who_essential_medicine: true
atc: J04AB02
tags:
  - antibiotic
  - tuberculosis
  - rifamycin
  - rna-polymerase
  - bactericidal
  - hepatotoxic
  - inducer
sources:
  - id: sensi-1959-original
    type: peer-reviewed
    cite: "Sensi P, Margalith P, Timbal MT. Rifomycin, a new antibiotic — preliminary report. Farmaco Ed Sci. 1959;14:146-7. (Original rifomycin discovery)"
    url: "https://pubmed.ncbi.nlm.nih.gov/13629243/"
  - id: who-tb-guidelines-2022
    type: clinical-guideline
    cite: "World Health Organization. Consolidated Guidelines on Tuberculosis, Module 4: Treatment — Drug-Susceptible Tuberculosis Treatment. WHO; 2022."
    url: "https://www.who.int/publications/i/item/9789240048126"
    accessed: "2026-06-04"
  - id: mitchison-1985-sterilizing
    type: peer-reviewed
    cite: "Mitchison DA. The action of antituberculosis drugs in short-course chemotherapy. Tubercle. 1985;66(3):219-25."
    pmid: "3884428"
    url: "https://pubmed.ncbi.nlm.nih.gov/3884428/"
cross_links:
  - target: 02-pathogen/02-bacteria/mycobacterium-tuberculosis
    relation: treats
    note: "Rifampicin is the most potent bactericidal and sterilizing component of first-line TB therapy (HRZE regimen); acts on both rapidly dividing bacilli in cavities and metabolically dormant bacilli in granulomas — the combination responsible for the 6-month cure rate achievable in drug-sensitive TB."
  - target: 02-pathogen/02-bacteria/mycobacterium-tuberculosis
    relation: modulates
    note: "Binds the rpoB subunit of M. tuberculosis RNA polymerase; rpoB mutations (especially codons 516, 526, 531) confer high-level resistance — and RIF resistance is used as a proxy for MDR-TB in rapid molecular diagnostics (GeneXpert MTB/RIF)."
  - target: 01-human/06-organ/liver
    relation: damages
    note: "Rifampicin causes transient transaminase elevation in 10–20% and frank hepatitis in ~1–2% of patients; CYP induction accelerates isoniazid → hydrazine metabolite conversion → additive hepatotoxicity; baseline LFTs + monthly monitoring required."
  - target: 03-medicine/01-modern/09-hematology/warfarin
    relation: modulates
    note: "Rifampicin is the most potent known CYP2C9/CYP3A4 inducer via PXR activation; S-warfarin plasma levels fall 70–90% within 7 days; warfarin dose may need doubling; INR monitoring weekly at start and monthly during TB therapy."
  - target: 01-human/04-cellular/hepatocyte
    relation: targets
    note: "Rifampicin activates PXR (pregnane X receptor) in hepatocytes → CYP3A4/CYP2C9/CYP2B6/P-gp transcriptional upregulation; maximal induction in 5–7 days; reversal 2–4 weeks post-discontinuation; basis of all rifampicin drug-drug interactions."
---

# Rifampicin

## Overview

Rifampicin (US spelling: **rifampin**) is a **semisynthetic antibiotic** of the rifamycin class, derived from rifamycin B produced by the soil actinomycete *Amycolatopsis rifamycinica* (formerly *Streptomyces mediterranei*, discovered in 1957 in a soil sample from Castiglione della Pescaia, Italy). The semisynthetic derivative rifampicin, developed by Piero Sensi and colleagues at Gruppo Lepetit (Milan) [^sensi-1959-original], was introduced clinically in 1968 and transformed tuberculosis treatment by enabling the shortening of therapy from 18–24 months to 6 months.

Rifampicin is:
- **Bactericidal** against *Mycobacterium tuberculosis* and other susceptible bacteria
- The only antibiotic with demonstrated **sterilizing activity** — it kills metabolically dormant (non-replicating) mycobacteria within granulomas and macrophages, a property unique among anti-TB drugs and critical for preventing relapse [^mitchison-1985-sterilizing]
- A **potent inducer** of cytochrome P450 3A4 (CYP3A4) and P-glycoprotein (P-gp) — creating clinically critical drug interactions
- A **WHO Group A drug** in drug-resistant TB regimens and a cornerstone of the standard first-line HRZE regimen

Rifampicin is included on every version of the **WHO Model List of Essential Medicines** and is considered irreplaceable in TB chemotherapy. Resistance to rifampicin is both a clinical catastrophe (proxy marker for MDR-TB) and a diagnostic marker — the Xpert MTB/RIF assay detects *rpoB* mutations for this reason.

## Mechanism

### RNA Polymerase Inhibition

The molecular target of rifampicin is the **β-subunit (rpoB) of bacterial DNA-dependent RNA polymerase** (RNAP):

1. **Structure of bacterial RNAP:** Five-subunit complex (α₂ββ'ω), with the β-subunit forming part of the active site RNA/DNA channel. The σ-factor confers promoter selectivity; core enzyme performs elongation.
2. **Rifampicin binding:** Binds a specific pocket in the β-subunit within the RNA exit channel, approximately 12 Å from the active site, with high affinity (Kd ~1 nM in *M. tuberculosis*). The binding is non-covalent but very stable.
3. **Mechanism of inhibition:** Does NOT prevent initial RNAP binding to DNA promoters or formation of the first phosphodiester bond. Instead, it **sterically blocks RNA elongation after initiation of the first 2–3 nucleotides** — the growing RNA chain physically cannot pass through the rifampicin-obstructed exit channel. This is sometimes described as "blocking the RNA exit tunnel after the dinucleotide step."
4. **Net effect:** Bacteria fail to synthesise mRNA; protein synthesis halts; bactericidal killing occurs within hours for rapidly dividing cells.

### Sterilizing Activity Against Dormant Bacilli

The exceptional clinical importance of rifampicin derives from its activity against **metabolically dormant** (non-replicating persistent, NRP) mycobacteria:

- Standard bactericidal antibiotics (isoniazid, aminoglycosides) are only effective against actively dividing bacteria where cell wall synthesis or protein synthesis is occurring at high rates
- Dormant Mtb bacilli in granulomas, lipid-rich macrophage environments, and acidic caseous necrosis are metabolically quiescent — and largely resistant to most agents
- Rifampicin retains bactericidal activity against NRP bacilli because RNAP is constitutively required for maintaining even minimal metabolic activity; RNA polymerase inhibition kills even near-dormant cells over time
- This is why standard TB therapy without rifampicin required 18–24 months; rifampicin-containing regimens achieve cure in 6 months [^mitchison-1985-sterilizing]

### Resistance — rpoB Mutations

Resistance to rifampicin in *M. tuberculosis* arises exclusively via spontaneous mutations in the **rifampicin resistance-determining region (RRDR) of rpoB** (codons 507–534, H37Rv numbering):

| Codon | Common mutation | Frequency in RIF-resistant Mtb |
|:---|:---|:---|
| **531** | S531L (Ser→Leu) | ~40–50% of resistant strains globally |
| **526** | H526Y, H526D | ~20–30% |
| **516** | D516V | ~5–10% |
| **Other positions** | Multiple rare mutations | ~15–25% |

- Rifampicin resistance in Mtb is used as a **proxy for MDR-TB** because co-resistance with isoniazid is so common (~90% of RIF-resistant Mtb strains are also isoniazid-resistant); the Xpert MTB/RIF and Xpert Ultra assays exploit this by detecting *rpoB* mutations molecularly
- Resistance to rifampicin does NOT confer resistance to other antibiotic classes — the rpoB mutations are highly specific to rifampicin's binding pocket

### Induction of Drug Metabolism — CYP3A4 and P-gp

Rifampicin is the **most potent known inducer of CYP3A4** and also strongly induces:
- CYP2B6, CYP2C8, CYP2C9, CYP2C19 (multiple CYP450 isoforms)
- P-glycoprotein (P-gp, ABCB1) — increases drug efflux from gut epithelium and CNS endothelium
- UDP-glucuronosyltransferases (UGTs)

Induction mechanism: Rifampicin activates the **pregnane X receptor (PXR)**, a nuclear receptor that transcriptionally upregulates CYP3A4, CYP2B6, and MDR1 (P-gp). Maximal induction takes 5–7 days; reversal after rifampicin discontinuation takes 2–4 weeks.

**Critical drug interactions:**

| Drug class affected | Clinical consequence |
|:---|:---|
| **Combined oral contraceptives** | Failure of contraception — plasma ethinylestradiol reduced ~50%; barrier methods required |
| **Antiretrovirals** (protease inhibitors, NNRTIs) | Dramatic reduction in plasma levels; rifabutin preferred for HIV/TB coinfection (weaker inducer) |
| **Warfarin** | Anticoagulant effect reduced; INR must be monitored closely; warfarin dose may need doubling |
| **Corticosteroids** | Steroid dose often needs doubling; transplant rejection risk |
| **Calcineurin inhibitors** (tacrolimus, ciclosporin) | Transplant rejection — tacrolimus levels can fall >90%; requires 5–50-fold dose increases |
| **Azole antifungals** (itraconazole, voriconazole) | Near-complete elimination of plasma drug levels; combination generally contraindicated |
| **Methadone** | Opioid withdrawal precipitated; dose adjustment required |
| **Sulfonylureas** | Reduced glycaemic control |

## Clinical Use

### Tuberculosis — First-Line HRZE Regimen

Rifampicin is the backbone of **standard first-line TB chemotherapy** [^who-tb-guidelines-2022]:

**Standard regimen (drug-susceptible TB):**
- **Intensive phase (2 months):** HRZE — Isoniazid (H) + Rifampicin (R) + Pyrazinamide (Z) + Ethambutol (E) daily
- **Continuation phase (4 months):** HR — Isoniazid + Rifampicin daily

Rationale of combination:
| Drug | Primary role |
|:---|:---|
| **Rifampicin (R)** | Sterilizing activity; kills dormant bacilli; prevents relapse |
| **Isoniazid (H)** | Early bactericidal activity; kills rapidly dividing bacilli |
| **Pyrazinamide (Z)** | Active at acidic pH in macrophages/caseous foci; reduces duration from 9 to 6 months |
| **Ethambutol (E)** | Bacteriostatic; prevents emergence of resistance to H and R |

The inclusion of rifampicin (with its unique sterilizing activity) is the primary reason the regimen achieves >95% cure in drug-susceptible TB with 6 months of therapy, compared to 18–24 months required by pre-rifampicin regimens.

**Dosing:**
- Adults: 10 mg/kg/day (range 8–12 mg/kg); maximum 600 mg/day
- Children: 15 mg/kg/day; maximum 600 mg/day
- Fixed-dose combination tablets (Rifater: RHZ; Rifinah: RH) simplify adherence and prevent monotherapy

### Drug-Resistant TB

- **MDR-TB** (resistant to H and R): rifampicin is **not** used; regimens use Group B-D drugs (fluoroquinolones, bedaquiline, linezolid, etc.)
- **Rifampicin-resistant TB (RR-TB)** without proven isoniazid resistance: treated as MDR-TB
- **WHO Group A drugs** (highest priority in DR-TB regimens): levofloxacin/moxifloxacin, bedaquiline, linezolid — rifampicin categorised separately as the standard sensitivity control

### Other Clinical Indications

| Indication | Regimen | Notes |
|:---|:---|:---|
| **Leprosy (Hansen disease)** | Rifampicin monthly + dapsone (PB) or + dapsone + clofazimine (MB), WHO MDT regimen | Standard WHO multi-drug therapy; monthly rifampicin kills 99.9% of *M. leprae* within 3–7 days |
| **Meningococcal prophylaxis** | 600 mg orally q12h × 2 days (adults) | Eradicates nasopharyngeal carriage; increasingly replaced by ciprofloxacin single dose |
| **MRSA biofilm/device infections** | Adjunct to vancomycin/daptomycin in device-related osteomyelitis, joint prosthesis infections | Unique penetration of biofilm and intracellular reservoirs; never used as monotherapy (rapid resistance) |
| **Brucellosis** | Rifampicin + doxycycline × 6 weeks | Alternative to streptomycin-doxycycline in resource-limited settings; WHO recommended |
| **Non-tuberculous mycobacteria (NTM)** | *M. avium* complex (MAC), *M. kansasii*: rifampicin-containing regimens | *M. kansasii* highly susceptible; MAC requires azithromycin + rifabutin + ethambutol |
| **Staphylococcal endocarditis** | Adjunct in prosthetic valve endocarditis per guidelines | Anti-biofilm and intracellular activity; must be combined (monotherapy selects resistance within days) |

## Evidence

### Sterilizing Activity and Therapy Duration

Mitchison (1985) [^mitchison-1985-sterilizing] provided the conceptual framework explaining rifampicin's unique role: bactericidal drugs with sterilizing activity (killing the dormant, slowly metabolising "persisters") are the key determinant of therapy duration. By quantifying the sterilizing activity of rifampicin versus other drugs in culture and animal models, Mitchison established why rifampicin-containing regimens could achieve 6-month cure — a finding that transformed global TB policy.

### WHO Consolidated TB Guidelines (2022)

The WHO 2022 guidelines [^who-tb-guidelines-2022] reaffirm rifampicin as the cornerstone of:
- Standard 6-month HRZE/HR regimen for drug-sensitive TB
- Preventive therapy for LTBI: 3-month regimen of isoniazid + rifampicin (3HR) as an alternative to 6H isoniazid monotherapy, with comparable efficacy and potentially better completion rates
- Shorter 4-month regimen for selected drug-sensitive TB patients (2 months HRZE + 2 months rifapentine-moxifloxacin: HRZE/PaM) — rifampicin's role can potentially be fulfilled by long-acting rifapentine in once-weekly regimens (1HP)

### Hepatotoxicity

Rifampicin causes hepatotoxicity via multiple mechanisms:
- **Transient, adaptive transaminase elevation:** Occurs in 10–20% of patients within first 2 months; usually self-limiting; therapy may be continued with monitoring if ALT <5× ULN without symptoms
- **Drug-induced liver injury (DILI):** Frank hepatitis requiring cessation: ~1–2% of patients; fulminant hepatic failure rare (<0.1%) but potentially fatal
- **Risk factors:** Pre-existing liver disease, alcohol use, HIV co-infection, malnutrition
- **Drug interaction:** Rifampicin induces its own metabolism (CYP induction); also accelerates hepatic metabolism of isoniazid → increased isoniazid hepatotoxicity paradoxically (by converting more INH to hydrazine metabolites)

### Characteristic Orange-Red Discolouration

Rifampicin produces **harmless orange-red colouration** of all body fluids: urine, tears, sweat, saliva, sputum, breast milk. This serves as an indirect **adherence marker** (coloured urine confirms recent ingestion). Patients must be counselled: permanent staining of soft contact lenses (must switch to glasses during therapy).

## Connections

- **Treats** → [Mycobacterium tuberculosis](../../../../02-pathogen/02-bacteria/mycobacterium-tuberculosis/README.md): first-line TB chemotherapy backbone; sterilizing activity enables 6-month cure.
- **Modulates** → [Mycobacterium tuberculosis](../../../../02-pathogen/02-bacteria/mycobacterium-tuberculosis/README.md): rpoB mutations confer high-level resistance; RIF resistance = proxy for MDR-TB.
- **Damages** → [Liver](../../../../01-human/06-organ/liver/README.md): transient transaminase elevation in 10–20%; frank hepatitis in ~1–2%; CYP induction accelerates isoniazid → hydrazine metabolite conversion → additive hepatotoxicity; baseline LFTs + monthly monitoring required.
- **Modulates** → [Warfarin](../../../../03-medicine/01-modern/09-hematology/warfarin/README.md): most potent CYP2C9/CYP3A4 inducer via PXR; S-warfarin levels fall 70–90% within 7 days; warfarin dose may need doubling; INR monitoring weekly at initiation.
- **Targets** → [Hepatocyte](../../../../01-human/04-cellular/hepatocyte/README.md): PXR activation → CYP3A4/CYP2C9/CYP2B6/P-gp upregulation; maximal induction in 5–7 days; reversal 2–4 weeks post-discontinuation; basis of all rifampicin drug-drug interactions.

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^sensi-1959-original]: Sensi P, Margalith P, Timbal MT. Rifomycin, a new antibiotic — preliminary report. *Farmaco Ed Sci.* 1959;14:146-7. [PubMed 13629243](https://pubmed.ncbi.nlm.nih.gov/13629243/)
[^who-tb-guidelines-2022]: World Health Organization. *Consolidated Guidelines on Tuberculosis, Module 4: Treatment — Drug-Susceptible Tuberculosis Treatment.* WHO; 2022. [who.int/publications/i/item/9789240048126](https://www.who.int/publications/i/item/9789240048126)
[^mitchison-1985-sterilizing]: Mitchison DA. The action of antituberculosis drugs in short-course chemotherapy. *Tubercle.* 1985;66(3):219-25. [PubMed 3884428](https://pubmed.ncbi.nlm.nih.gov/3884428/)
