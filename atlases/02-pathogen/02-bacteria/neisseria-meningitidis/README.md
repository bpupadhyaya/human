---
schema: pathogen-entry/v1
id: neisseria-meningitidis
name: Neisseria meningitidis
atlas: 02-pathogen
scale: 02-bacteria
status: draft
last_reviewed: 2026-06-05
summary: "Gram-negative encapsulated diplococcus; obligate human pathogen. Causes bacterial meningitis and fulminant septicaemia. Serogroups A/B/C/W/Y/X; LOS endotoxin drives DIC and Waterhouse-Friderichsen syndrome. Complement deficiency markedly increases risk."
aliases: ["N. meningitidis", "meningococcus", "meningococcal disease", "IMD", "serogroup A B C W Y X meningococcus"]
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
cross_links:
  - target: 01-human/04-cellular/neutrophil
    relation: infects
    note: "N. meningitidis evades neutrophils via polysaccharide capsule (anti-phagocytic), fHbp (complement evasion), and IgA1 protease (↓mucosal IgA); LOS activates TLR4 → massive cytokine storm paradoxically drives endovascular damage rather than clearance."
  - target: 01-human/06-organ/brain
    relation: damages
    note: "Meningococci seed the subarachnoid space → LOS triggers neutrophilic meningitis → ↑ICP, cerebral oedema, vasculitis, neuronal loss; herniation is the primary cause of death; hearing loss (VIII nerve) and brain infarcts are common sequelae in survivors."
  - target: 01-human/07-system/immune-system
    relation: damages
    note: "Complement deficiency (C5–C9/MAC) dramatically increases meningococcal risk; eculizumab (anti-C5) raises risk 1000–2000×→ mandatory MenACWY+MenB vaccination before anti-complement therapy; properdin deficiency → fulminant meningococcaemia."
  - target: 01-human/07-system/cardiovascular-system
    relation: damages
    note: "Meningococcal septicaemia: LOS→TLR4→TNF-α storm → endothelial apoptosis + DIC → purpuric haemorrhage (petechiae→ecchymoses→gangrene); Waterhouse-Friderichsen syndrome (bilateral adrenal haemorrhage → cortisol deficiency → refractory shock)."
---

# Neisseria meningitidis

## Overview

*Neisseria meningitidis* (the **meningococcus**) is a **Gram-negative, encapsulated diplococcus** and an **obligate human pathogen** — humans are the only natural reservoir [^mandell-principles]. It is carried asymptomatically in the nasopharynx of approximately **10% of adults** (carriage rates highest in 15–24 year olds, up to 24% on college campuses) and causes **invasive meningococcal disease (IMD)** in a small fraction of carriers or contacts.

IMD presents as two overlapping but distinct syndromes: **bacterial meningitis** (infection of the meninges) and **meningococcal septicaemia** (primary bacteraemia with DIC and multi-organ failure), or a combination of both. The organism is notorious for the speed of its lethality — a child can be well at breakfast and dead by evening. Even with optimal care, IMD carries **5–10% mortality** and significant morbidity (hearing loss, limb amputation from DIC-driven gangrene, brain injury) in survivors.

**Global serogroup distribution:**
| Serogroup | Geography/Population | Notes |
|:---|:---|:---|
| **A** | Sub-Saharan Africa (meningitis belt: Senegal to Ethiopia); epidemic waves | Polysaccharide vaccine (MenA conjugate) dramatically reduced burden |
| **B** | Europe, North America, Australia | Most common in UK, Netherlands; ~35% of US IMD; requires protein-based vaccines (MenB) |
| **C** | Young adults, college campuses; Europe | Conjugate vaccine highly effective; near elimination in vaccinated populations |
| **W** | Global spread post-2000 (hajj pilgrimage amplification); high severity; pneumonia, septic arthritis | Rising in sub-Saharan Africa and South America |
| **Y** | North America, elderly; pneumonia phenotype | Conjugate vaccine covers Y |
| **X** | Africa (meningitis belt); **no licensed vaccine** | Emerging burden; conjugate vaccine in development |

## Structure

### Morphology and Key Features

| Feature | Detail |
|:---|:---|
| **Shape** | Gram-negative diplococci (kidney/coffee-bean shaped pairs), ~0.6–1.0 µm diameter |
| **Capsule** | Polysaccharide; defines serogroup (A: N-acetyl-mannosamine-1-phosphate; B: poly-α-2,8-N-acetylneuraminic acid [polysialic acid]; C: poly-α-2,9-N-acetylneuraminic acid) |
| **Atmosphere** | Aerobic; grows best in 5% CO₂; fastidious (requires enriched media) |
| **Culture** | Chocolate agar or blood agar with CO₂; Thayer-Martin medium (selective: vancomycin, colistin, nystatin) for clinical specimens |
| **Oxidase** | Positive (all Neisseria) |
| **Carbohydrate utilisation** | Glucose and maltose (distinguishes from *N. gonorrhoeae* which ferments glucose only) |

### Capsule — the Central Virulence Factor

The polysaccharide capsule is the dominant antiphagocytic determinant and the **basis of vaccine development** for most serogroups:

- **Antiphagocytic:** Capsule prevents C3b deposition on the bacterial surface and physically blocks phagocytosis
- **Serogrouping:** Capsule polysaccharide structure defines the serogroup; used as the antigen in polysaccharide and conjugate vaccines (MenACWY)
- **Serogroup B capsule exception:** Serogroup B capsule is **polysialic acid (PSA)** — identical to human NCAM (neural cell adhesion molecule) → molecular mimicry → **T-independent, poorly immunogenic in humans** → cannot be used as a vaccine antigen → MenB vaccines use protein antigens instead

### Outer Membrane and Surface Proteins

| Component | Detail |
|:---|:---|
| **Porins (PorA, PorB)** | Major OMPs; PorA is polymorphic → basis of fine-typing (PorA typing); **component of MenB OMV vaccines** (Bexsero contains PorA OMV) |
| **Factor H binding protein (fHbp)** | Binds human complement regulatory factor H → ↓alternative complement activation → ↓C3b deposition; **key MenB vaccine antigen** (both Bexsero and Trumenba); high antigenic variability |
| **NHBA (Neisseria Heparin Binding Antigen)** | Binds heparan sulfate → ↑serum resistance; Bexsero component |
| **NadA (Neisseria adhesin A)** | Outer membrane trimeric autotransporter; binds β1-integrins on endothelium; Bexsero component |
| **LOS (lipooligosaccharide)** | Lacks the O-antigen repeat of classical LPS; short oligosaccharide core; **potent TLR4 agonist** → massive TNF-α/IL-1β release; primary mediator of endotoxic shock in IMD |
| **IgA1 protease** | Cleaves mucosal IgA1 (Pro-Ser/Pro-Thr bond in hinge region) → inactivates secretory IgA in nasopharynx → ↓mucosal immune defence → facilitates colonisation |
| **Type IV pili (tfpA/pilC)** | Initial adhesion to nasopharyngeal epithelium via CD46 and CEACAMs (CEACAM1, CEACAM3); retractile pili (PilT ATPase) generate strong attachment force; required for DNA uptake (natural transformation) |

## Infection Mechanism

### Nasopharyngeal Colonisation

1. **Attachment:** Type IV pili contact CEACAM1 on nasopharyngeal columnar epithelial cells → initial loose attachment → retraction → tight apposition → microcolony formation
2. **Epithelial transcytosis:** After pilus-mediated signalling, meningococci are endocytosed by non-immune columnar epithelial cells → transcytosis through the mucosa → subepithelial space → enter the bloodstream
3. **Key immune evasion at mucosa:**
   - IgA1 protease cleaves secretory IgA1 → ↓mucosal antibody defence
   - Capsule provides serum resistance
   - LOS sialylation (sialyltransferase adds sialic acid from host CMP-NAN) → ↑factor H binding → ↑complement evasion

### Bacteraemia and Complement Evasion

Once in the bloodstream, meningococci must evade complement-mediated killing — the primary bactericidal mechanism in serum:

| Mechanism | Detail |
|:---|:---|
| **fHbp (factor H binding protein)** | Recruits factor H → ↑complement factor I-mediated C3b cleavage → ↓opsonisation and MAC formation |
| **Polysaccharide capsule** | Prevents C3b deposition; physical barrier to MAC insertion |
| **LOS sialylation** | Mimics self (host cells sialylated) → factor H recruitment |
| **PorB channel** | Suppresses apoptosis of infected cells |

**Complement deficiency and meningococcal susceptibility:** The terminal complement pathway (MAC, C5b-C9) is the critical bactericidal effector against *N. meningitidis* [^mandell-principles]:
- **C5–C9 deficiency (MAC deficiency):** 500–1000× increased risk of IMD; often recurrent episodes
- **Properdin deficiency (X-linked):** ↓Alternative complement pathway amplification → severe, often fulminant IMD
- **Eculizumab (anti-C5 monoclonal antibody):** Blocks MAC formation → **1000–2000× increased IMD risk** in treated patients → mandatory MenACWY + MenB vaccination before initiation

### Meningeal Seeding

Meningococcal bacteraemia → choroid plexus traversal and meningeal infection:
1. Meningococci adhere to blood-brain barrier (BBB) endothelium via **CEACAM1, NadA, pili**
2. Transcytosis through BBB → subarachnoid space
3. CSF is poor in complement, antibody, and immune cells → unrestricted meningococcal replication
4. LOS/inflammatory mediators → **neutrophilic pleocytosis** → ↑ICP → cerebral oedema → herniation risk

## Host Interactions

### Endotoxin-driven Septicaemia

**LOS** (lipooligosaccharide) is the proximate mediator of meningococcal septicaemia [^murray-microbiology]:

```
LOS  →  TLR4/MD-2 complex on monocytes/macrophages/endothelium
    ↓
MyD88/TRIF signalling → NF-κB + IRF3
    ↓
Massive release: TNF-α, IL-1β, IL-6, IL-8, IL-12, IFN-γ
    ↓
Endothelial activation/injury → ↑vascular permeability, ↑tissue factor expression
    ↓
DIC (disseminated intravascular coagulation): fibrin thrombi + simultaneous haemorrhage
    ↓
Purpuric rash (petechiae → ecchymoses → confluence → gangrene)
+ Waterhouse-Friderichsen syndrome (bilateral adrenal haemorrhage)
+ Multi-organ failure
```

**LOS serum concentration** correlates directly with disease severity, mortality, and complication rate in IMD — making meningococcal septicaemia one of the most potent endotoxinaemias known.

### Meningitis Pathophysiology

| Phase | Events |
|:---|:---|
| **Early** | Meningococcal replication in CSF; LOS/peptidoglycan release → cytokine/chemokine production by meningeal and ependymal cells |
| **Neutrophilic response** | IL-8/CXCL8 → massive neutrophil influx into CSF → ↑CSF protein (>100 mg/dL), ↑WBC (>1000 cells/µL), ↓glucose (<40 mg/dL, CSF:serum ratio <0.4) |
| **↑ICP** | Cerebral oedema (vasogenic + cytotoxic), hydrocephalus, ↓CSF outflow → ↑ICP → ↓CPP → ischemia |
| **Vasculitis** | Meningococcal invasion of subarachnoid blood vessels → vessel wall inflammation → thrombosis → brain infarcts |
| **Cranial nerve injury** | VIII nerve (cochlear blood vessel thrombosis/inflammation → **sensorineural hearing loss** in 5–10% of survivors) |

## Connections

- **Infects** → [Neutrophil](../../../01-human/04-cellular/neutrophil/README.md): N. meningitidis evades neutrophil killing via polysaccharide capsule (anti-phagocytic), fHbp-mediated complement evasion (↓C3b opsonisation), and IgA1 protease (degrades mucosal IgA). Once in the bloodstream, LOS activates TLR4 → massive neutrophil/cytokine response that paradoxically drives microvascular damage rather than pathogen clearance [^mandell-principles].
- **Damages** → [Brain](../../../01-human/06-organ/brain/README.md): Meningococci seed the subarachnoid space, where LOS drives neutrophilic meningitis → ↑ICP, cerebral oedema, subarachnoid vessel vasculitis, and neuronal injury. Brain herniation is the primary cause of acute mortality. Sensorineural hearing loss and brain infarcts are the most frequent sequelae in survivors [^mandell-principles].
- **Damages** → [Immune system](../../../01-human/07-system/immune-system/README.md): Terminal complement (C5–C9/MAC) is the critical bactericidal defence against meningococcus. C5–C9 deficiency → 500–1000× increased IMD risk; properdin deficiency → fulminant meningococcaemia. Eculizumab (anti-C5) raises risk 1000–2000× → MenACWY + MenB vaccination mandatory before anti-complement therapy [^murray-microbiology].
- **Damages** → [Cardiovascular system](../../../01-human/07-system/cardiovascular-system/README.md): Meningococcal septicaemia: LOS → TLR4 → TNF-α endotoxic storm → endothelial injury + DIC → purpuric haemorrhage progressing from petechiae to ecchymoses to skin gangrene. Waterhouse-Friderichsen syndrome (bilateral adrenal haemorrhage → acute cortisol deficiency → refractory shock) occurs in ~10% of fulminant septicaemia [^murray-microbiology].

## Pathology

### Clinical Presentations

| Syndrome | Frequency | Key Features | Emergency signs |
|:---|:---|:---|:---|
| **Meningococcal meningitis** | ~50% of IMD | Headache, photophobia, neck stiffness, fever; Kernig's/Brudzinski's signs; CSF: turbid, WBC>1000 neutrophils, ↑protein, ↓glucose | Papilloedema → herniation risk; do NOT delay treatment for LP |
| **Meningococcal septicaemia (±meningitis)** | ~30–40% | Purpuric/petechial **non-blanching rash** (pathognomonic); high fever; haemodynamic instability; MODS | Rapidly expanding purpura; shock; limb ischaemia |
| **Combined meningitis + septicaemia** | ~20% | Features of both syndromes | Worst prognosis |
| **Occult bacteraemia** | Rare | Fever without focus; transient | Self-limited in most; may seed meninges |
| **Pneumonia** | Serogroup Y association | Lobar/multilobar pneumonia; elderly | Consider meningococcal in culture-negative pneumonia |
| **Arthritis, pericarditis, endophthalmitis** | Rare | Secondary immune-complex manifestations | Post-infectious inflammatory |

### Treatment

**Immediately life-threatening — treat before diagnostic workup if IMD clinically suspected:**

| Intervention | Detail |
|:---|:---|
| **IV Ceftriaxone 2g (adult)** | First-line antibiotic; give IMMEDIATELY — before LP if LP not immediately available; bactericidal, excellent CSF penetration |
| **Dexamethasone** | 0.15 mg/kg IV before/with first antibiotic dose; ↓hearing loss in bacterial meningitis (best data for pneumococcal); benefit in meningococcal less clear but recommended |
| **ICU support** | Aggressive fluid resuscitation, vasopressors (meningococcal septicaemia → distributive shock + adrenal insufficiency); consider hydrocortisone in refractory shock |
| **Penicillin G** | Alternative to ceftriaxone if confirmed susceptible; acquired penicillin resistance rare but documented |
| **Close contact prophylaxis** | Rifampicin (2 days) or ciprofloxacin (single dose) or ceftriaxone IM (single dose) for household contacts within 24h; eradicates nasopharyngeal carriage |

### Vaccines and Prevention

| Vaccine | Serogroups | Product examples | Schedule (US) |
|:---|:---|:---|:---|
| **MenACWY conjugate** | A, C, W, Y | Menactra (MCV4-D), Menveo (MCV4-CRM), MenQuadfi | Routine: 11–12 years + booster at 16; high-risk groups: ≥2 months |
| **MenB (4-component)** | B | Bexsero (4CMenB: fHbp, NHBA, NadA, PorA OMV) | 2-dose series; 16–23 years; outbreak response; complement-deficient patients |
| **MenB (bivalent fHbp)** | B | Trumenba | 2 or 3-dose series depending on risk |
| **MenA conjugate (Africa)** | A | MenAfriVac | Single dose meningitis belt mass vaccination → near-elimination of serogroup A epidemics |
| **Serogroup X** | X | None licensed | Active development; increasing African burden |

**High-priority vaccination targets:** Complement-deficient patients (C5–C9, properdin), eculizumab/ravulizumab recipients (anti-C5 therapy), asplenic patients, HIV-positive individuals, college freshmen in dormitories, travellers to sub-Saharan Africa/hajj, microbiologists handling meningococcal cultures.

[^mandell-principles]: Bennett JE, Dolin R, Blaser MJ. *Mandell, Douglas, and Bennett's Principles and Practice of Infectious Diseases.* 9th ed. Elsevier; 2020.
[^murray-microbiology]: Murray PR, Rosenthal KS, Pfaller MA. *Medical Microbiology.* 9th ed. Elsevier; 2021.
