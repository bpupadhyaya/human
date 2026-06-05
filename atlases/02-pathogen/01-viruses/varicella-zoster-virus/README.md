---
schema: pathogen-entry/v1
id: varicella-zoster-virus
name: Varicella-Zoster Virus
atlas: 02-pathogen
scale: 01-viruses
status: draft
last_reviewed: 2026-06-05
summary: "Alphaherpesvirinae; dsDNA ~125 kb; enveloped. Primary infection: varicella (chickenpox). Establishes lifelong latency in sensory ganglia. Reactivation: herpes zoster (shingles) with dermatomal neuritis and postherpetic neuralgia."
aliases: ["VZV", "HHV-3", "human herpesvirus 3", "varicella virus", "zoster virus", "chickenpox virus"]
sources:
  - id: mandell-principles
    type: textbook
    cite: "Bennett JE, Dolin R, Blaser MJ. Mandell, Douglas, and Bennett's Principles and Practice of Infectious Diseases. 9th ed. Elsevier; 2020."
    url: "https://www.elsevier.com/books/mandell-douglas-and-bennetts-principles-and-practice-of-infectious-diseases/bennett/978-0-323-48255-4"
    accessed: "2026-06-05"
  - id: fields-virology
    type: textbook
    cite: "Knipe DM, Howley PM, eds. Fields Virology. 7th ed. Wolters Kluwer; 2021."
    url: "https://www.lww.com/product/9781975112547"
    accessed: "2026-06-05"
cross_links:
  - target: 01-human/04-cellular/neuron
    relation: infects
    note: "VZV establishes lifelong latency in sensory ganglia neurons (DRG, trigeminal); VLT/ORF63 transcript maintains latency; reactivation causes anterograde transport to dermatome — herpes zoster (shingles); DRG neuronal damage underlies postherpetic neuralgia."
  - target: 01-human/07-system/nervous-system
    relation: damages
    note: "VZV reactivation (herpes zoster) causes dermatomal neuritis and postherpetic neuralgia (PHN, neuropathic pain, 10–15% of cases); Ramsay Hunt syndrome (CN VII palsy); encephalitis (rare); VITT-like vasculopathy (rare cerebral artery involvement)."
  - target: 01-human/07-system/immune-system
    relation: damages
    note: "VZV IE62/IE63 block IRF3, STAT1, and IFN-β; gE/gI heterodimer acts as IgG Fc receptor (immune evasion); VZV-specific T cell decline with ageing → zoster reactivation risk; immunosuppressed patients at risk for disseminated VZV."
  - target: 01-human/06-organ/lung
    relation: damages
    note: "VZV pneumonitis in adults (~1 in 400 varicella cases) and immunocompromised — diffuse bilateral nodular infiltrates, risk of respiratory failure; haemorrhagic pneumonia in severe immunosuppression; IV aciclovir reduces mortality."
---

# Varicella-Zoster Virus

## Overview

Varicella-zoster virus (VZV) is a human-restricted herpesvirus causing two distinct clinical diseases in the same host over a lifetime: **varicella (chickenpox)** on primary infection and **herpes zoster (shingles)** upon reactivation from latency. VZV belongs to the family **Herpesviridae**, subfamily **Alphaherpesvirinae** — a classification it shares with herpes simplex viruses 1 and 2 (HSV-1/2) — but unlike HSV, VZV has an extremely restricted host range, naturally infecting only humans [^fields-virology].

After primary infection, VZV establishes **lifelong latency** in the nuclei of sensory neurons in dorsal root ganglia (DRG), trigeminal ganglia, and autonomic ganglia. More than **90% of adults worldwide** are seropositive, reflecting near-universal childhood exposure in the pre-vaccine era. Reactivation probability over a lifetime approaches **30%**, rising sharply with age and immunosuppression as VZV-specific T cell immunity declines [^mandell-principles].

## Structure

### Virion Architecture

| Component | Description |
|:---|:---|
| **Envelope** | Host-derived lipid bilayer; ~180–200 nm diameter |
| **Tegument** | Protein layer between capsid and envelope; contains IE62, IE63 and other virulence/transactivation proteins |
| **Capsid** | Icosahedral; encloses the dsDNA genome |
| **gB** | Major fusion glycoprotein; required for cell entry |
| **gE/gI heterodimer** | Most abundant envelope glycoprotein; essential for cell-to-cell spread, immune evasion; acts as IgG Fc receptor |
| **gH/gL** | Fusion helper complex; required for membrane fusion and cell-to-cell spread |
| **gC** | Binds complement C3b; immune evasion |

### Genome Organisation

VZV genome is **~125 kb dsDNA** encoding ~70 open reading frames (ORFs). Unlike HSV, VZV has a smaller unique region and lacks the internal repeat sequences that allow HSV to invert its genome segments. Key genes include:

| Gene | Protein | Function |
|:---:|:---|:---|
| ORF62 | **IE62** (major transactivator) | ICP4 homologue; transactivates all kinetic gene classes (IE, E, L); packaged in tegument |
| ORF63 | **IE63** | Inhibits IRF3 and PKR; blocks STAT1 phosphorylation; required for latency maintenance |
| ORF36 | **Thymidine kinase (TK)** | Phosphorylates aciclovir/valaciclovir (first phosphorylation step); VZV TK less efficient than HSV TK → higher aciclovir doses required |
| ORF28 | **DNA polymerase** | Target of aciclovir triphosphate (chain termination) and foscarnet (pyrophosphate analogue) |
| ORF14 | **gC** | Complement C3b binding; immune evasion |

## Infection Mechanism

### Primary Infection (Varicella)

1. **Respiratory exposure:** VZV in respiratory droplets from an infectious individual (or vesicular contact) reaches the nasopharyngeal mucosa.
2. **Tonsillar T cell infection:** VZV infects CD4+ CD29+ T cells in tonsillar tissue via unknown receptor (not CD150/SLAM); gB and gH mediate membrane fusion.
3. **Primary viraemia:** Infected T cells carry VZV in the bloodstream to skin and viscera — explaining the diffuse, centripetal rash distribution.
4. **Skin entry:** VZV infects keratinocytes via gB/gH-mediated fusion → vesicular lesions (hallmark "dew drops on rose petal" appearance: clear vesicles on erythematous base); all lesion stages present simultaneously (unlike smallpox) [^mandell-principles].
5. **Ganglionic seeding:** VZV reaches DRG during viraemia via retrograde axonal transport from skin nerve endings or haematogenous seeding of CD4+ T cells → establishes latency.

### Latency Establishment

In latently infected sensory neurons, VZV persists as a circular episome in the nucleus. The **VZV Latency Transcript (VLT)**, a recently characterised spliced RNA that reads through ORF63, is expressed in latency along with ORF63 protein (IE63). IE63 in latent neurons is thought to inhibit stress-induced viral reactivation by blocking PKR and restricting IE62-driven lytic transcription [^fields-virology].

### Reactivation (Herpes Zoster)

1. **Trigger:** Decline in VZV-specific CD4+ and CD8+ T cell immunity (ageing, immunosuppression, stress, intercurrent illness).
2. **Lytic reactivation** in DRG neuron: IE62 drives full lytic cascade → virus replicates in the ganglion → intense inflammatory neuritis → **severe pain (neuralgia)** in the corresponding dermatome even before rash appears.
3. **Anterograde transport:** Progeny virus travels down sensory axons to the skin of the corresponding dermatome → unilateral, single-dermatome vesicular rash + erythema.
4. **Contagion:** Zoster vesicular fluid contains infectious VZV; contact with vesicles can cause primary varicella in seronegative individuals.

### Immune Evasion

| Protein/Mechanism | Action |
|:---|:---|
| **IE63** | Blocks IRF3 activation → ↓IFN-β; inhibits PKR → prevents eIF2α phosphorylation → resists antiviral translational shutdown |
| **IE62** | Modulates host gene expression; reduces stress-induced apoptosis |
| **gE/gI Fc receptor** | Binds IgG Fc domain → sequesters antibody; prevents ADCC and complement fixation |
| **gC** | Binds complement C3b → prevents opsonisation and complement lysis |
| **MHC-I downregulation** | VZV reduces surface MHC-I on infected keratinocytes → impairs CD8+ CTL recognition |

## Host Interactions

### Neuronal Latency

VZV demonstrates exquisite **neurotropism**: latency is established exclusively in neurons of sensory and autonomic ganglia, never in non-neuronal satellite glial cells (unlike HSV which can also infect satellite cells). Within latently infected neurons, VZV episomes are maintained in an epigenetically silenced state, with limited viral gene expression restricted to VLT and ORF63 protein [^fields-virology].

The ageing immune system shows progressive decline in VZV-specific T cell numbers and function (both CD4+ T helper and CD8+ CTL), while humoral immunity (IgG anti-VZV) remains largely intact. This mismatch explains why zoster is predominantly an **age-associated disease** — antibodies cannot eliminate intraneuronal virus, so T cell surveillance is the key brake on reactivation.

### Immunosuppressed Patients

In patients with severely impaired T cell immunity (HIV/AIDS with CD4 <200, haematological malignancies, stem cell transplant, high-dose corticosteroids), VZV can disseminate beyond the dermatome to involve visceral organs — **disseminated zoster** or **haemorrhagic varicella** — with involvement of lungs (pneumonitis), liver (hepatitis), brain (encephalitis), and coagulation pathways (DIC). Mortality in this setting without prompt antiviral treatment is high.

## Connections

- **Infects** → [Neuron](../../../01-human/04-cellular/neuron/README.md): VZV establishes lifelong latency in sensory ganglia neurons (DRG, trigeminal); VLT/ORF63 transcripts maintain latency; reactivation causes anterograde transport to the corresponding dermatome — herpes zoster (shingles); DRG neuronal damage during reactivation underlies postherpetic neuralgia.
- **Damages** → [Nervous system](../../../01-human/07-system/nervous-system/README.md): VZV reactivation (herpes zoster) causes dermatomal neuritis and postherpetic neuralgia (PHN; neuropathic pain persisting >3 months post-rash; ~10–15% of all zoster cases); Ramsay Hunt syndrome (CN VII palsy + auricular vesicles); encephalitis and cerebral vasculopathy in rare severe cases.
- **Damages** → [Immune system](../../../01-human/07-system/immune-system/README.md): VZV IE62/IE63 block IRF3, STAT1 phosphorylation, and IFN-β; gE/gI heterodimer binds IgG Fc to sequester antibody; VZV-specific T cell decline with ageing drives zoster reactivation risk; immunosuppressed patients risk life-threatening disseminated VZV.
- **Damages** → [Lung](../../../01-human/06-organ/lung/README.md): VZV pneumonitis complicates approximately 1 in 400 adult varicella cases — diffuse bilateral nodular infiltrates, risk of respiratory failure; haemorrhagic pneumonia in severe immunosuppression; IV aciclovir reduces mortality.

## Pathology

### Primary Varicella: Clinical Features

| Feature | Detail |
|:---|:---|
| **Incubation** | 14–21 days (average ~14 days) |
| **Rash morphology** | Begins on trunk; spreads centrifugally; pruritic "dew drops on rose petal" — clear vesicles on erythematous base; multiple lesion stages simultaneously (macule → papule → vesicle → pustule → crust); 200–500 lesions in primary infection |
| **Fever** | 38–39 °C, concurrent with rash |
| **Infectivity** | 2 days before rash until all lesions have crusted (~5–7 days after rash onset) |
| **Histology** | Intranuclear inclusions (Cowdry type A) in keratinocytes; acantholysis, ballooning degeneration |

### Herpes Zoster: Clinical Features and Complications

| Complication | Frequency | Notes |
|:---|:---|:---|
| **Postherpetic neuralgia (PHN)** | 10–15% overall; 30–50% in >60 years | Neuropathic pain >3 months; treat with gabapentin/pregabalin, TCA, lidocaine patch, capsaicin 8% |
| **Ramsay Hunt syndrome** | ~1 in 1,000 zoster cases | Reactivation in geniculate ganglion → CN VII palsy + ear pain + auricular/oral vesicles |
| **Zoster ophthalmicus** | ~10–25% of zoster | CN V1 (ophthalmic branch) → corneal ulceration, uveitis, keratitis; treat with IV aciclovir + topical steroids; can cause blindness |
| **Disseminated zoster** | Immunocompromised | Visceral involvement: pneumonitis, hepatitis, encephalitis, DIC; high mortality |
| **Congenital VZV syndrome** | <20 weeks gestation | Skin scarring (cicatricial), limb hypoplasia, eye defects, CNS abnormalities |

### Epidemiology and Prevention

- **Varicella vaccine (Varivax/Varilrix):** Live-attenuated Oka strain; 2-dose schedule (12–15 months, 4–6 years); >95% efficacy against severe varicella.
- **Recombinant zoster vaccine (Shingrix/RZV):** **gE subunit + AS01B adjuvant** (MPL + QS-21); 2-dose schedule 2–6 months apart; >90% efficacy against zoster in adults ≥50 years; >85% against PHN; recommended over older live-attenuated Zostavax (which had declining efficacy with age).

### Treatment

| Drug | Mechanism | Indication |
|:---|:---|:---|
| **Aciclovir/valaciclovir** | VZV TK phosphorylates aciclovir → triphosphate → chain-terminating DNA polymerase substrate | Uncomplicated zoster (oral); severe varicella/zoster in adults (IV) |
| **Famciclovir** | Prodrug → penciclovir triphosphate → DNA polymerase inhibitor | Uncomplicated zoster; bioavailability advantage over aciclovir |
| **Foscarnet** | Pyrophosphate analogue → directly inhibits DNA polymerase (no TK-dependent activation) | Aciclovir-resistant VZV (thymidine kinase-deficient mutants in HIV/AIDS); IV only |
| **VZV IVIG** | Passive immunisation | Post-exposure prophylaxis in high-risk seronegative individuals (pregnant women, immunocompromised) |

[^mandell-principles]: Bennett JE, Dolin R, Blaser MJ. *Mandell, Douglas, and Bennett's Principles and Practice of Infectious Diseases.* 9th ed. Elsevier; 2020.
[^fields-virology]: Knipe DM, Howley PM, eds. *Fields Virology.* 7th ed. Wolters Kluwer; 2021.
