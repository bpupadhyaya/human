---
schema: pathogen-entry/v1
id: rotavirus
name: Rotavirus
atlas: 02-pathogen
scale: 01-viruses
status: draft
last_reviewed: 2026-06-05
summary: "Reoviridae; triple-layered icosahedral dsRNA virus (11 segments). Infects villus tip enterocytes causing secretory diarrhea. Leading cause of severe diarrhea in children <5; ~128,000 deaths/year. Vaccine-preventable (Rotarix, RotaTeq)."
aliases: ["RV", "rotavirus A", "infantile gastroenteritis virus"]
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
  - id: tate-2016-who-mortality
    type: peer-reviewed
    cite: "Tate JE, Burton AH, Boschi-Pinto C, Parashar UD. Global, regional, and national estimates of rotavirus mortality in children <5 years of age, 2000-2013. Clin Infect Dis. 2016;62(Suppl 2):S96-S105."
    doi: "10.1093/cid/civ1013"
    pmid: "26966244"
    url: "https://doi.org/10.1093/cid/civ1013"
    accessed: "2026-06-05"
  - id: estes-2006-rotavirus-biology
    type: peer-reviewed
    cite: "Estes MK, Kapikian AZ. Rotaviruses. In: Knipe DM, Howley PM, eds. Fields Virology. 5th ed. Lippincott Williams & Wilkins; 2007:1917-1974."
    accessed: "2026-06-05"
  - id: parashar-2016-vaccine-impact
    type: peer-reviewed
    cite: "Parashar UD, Johnson H, Estes MK, Gentsch JR. Global illness and deaths caused by rotavirus disease in children. Emerg Infect Dis. 2003;9(5):565-572."
    doi: "10.3201/eid0905.020562"
    pmid: "12737740"
    url: "https://doi.org/10.3201/eid0905.020562"
    accessed: "2026-06-05"
cross_links:
  - target: 01-human/06-organ/small-intestine
    relation: infects
    note: "Rotavirus infects mature villus tip enterocytes via VP4/VP7-integrin-Hsc70 interactions, causing cytoskeletal disruption, CFTR activation, and NSP4 enterotoxin-driven secretory diarrhea without mucosal destruction."
  - target: 01-human/07-system/digestive-system
    relation: damages
    note: "Rotavirus causes villous atrophy, impaired brush-border enzyme activity, and NSP4 enterotoxin-mediated fluid hypersecretion in the digestive system, producing watery diarrhea that rapidly causes fatal dehydration in infants."
  - target: 04-vaccine/05-live-attenuated/rotarix
    relation: prevented-by
    note: "Rotarix (G1P[8] monovalent oral) and RotaTeq (G1-G4/P[8] pentavalent oral) live-attenuated vaccines prevent severe rotavirus gastroenteritis; WHO recommends inclusion in all national immunization programmes."
  - target: 01-human/04-cellular/macrophage
    relation: damages
    note: "Rotavirus antigens and particles detected in mesenteric-node macrophages; macrophage activation drives the systemic viremia and biliary excretion seen in immunocompromised hosts with chronic rotavirus infection."
---

# Rotavirus

## Overview

Rotavirus is a **non-enveloped, double-stranded RNA (dsRNA) virus** (family *Reoviridae*, genus *Rotavirus*) and the leading cause of severe dehydrating diarrheal disease in children under 5 years worldwide. Before widespread vaccine introduction, rotavirus was responsible for an estimated **500,000–600,000 child deaths per year**. Following WHO recommendation of rotavirus vaccine inclusion in national immunization programmes (2009), global mortality has fallen dramatically to approximately **128,000 deaths per year**, with most remaining deaths concentrated in sub-Saharan Africa and South Asia where vaccine coverage and cold-chain infrastructure remain challenging [^tate-2016-who-mortality].

The genus *Rotavirus* comprises species A through J; **Rotavirus A (RVA)** causes the overwhelming majority of human disease. RVA is further classified by the serotype of its two outer capsid proteins: **VP7 (G-type, glycoprotein)** and **VP4 (P-type, protease-sensitive)**. The dominant global strains are G1P[8], G2P[4], G3P[8], G4P[8], and G9P[8] — collectively causing >80% of cases in most settings [^estes-2006-rotavirus-biology].

The name "rotavirus" derives from the Latin *rota* (wheel): by electron microscopy, the triple-layered capsid gives the particle a distinctive wheel-like appearance with spoke-like radiating structures. Nearly every child in the world is infected by rotavirus at least once before age 5, and primary infection with a virulent strain produces the most severe disease; subsequent reinfections are progressively milder owing to serotype-specific and cross-reactive immunity [^mandell-principles].

## Structure

| Layer | Proteins | Function |
|:---|:---|:---|
| **Outer capsid** | VP7 (glycoprotein, G-type), VP4 (spike protein, P-type; cleaved to VP5* + VP8* by trypsin) | Cell attachment (VP8* binds HBGAs/sialylated glycans), membrane penetration (VP5*), serotype determinant |
| **Inner capsid (middle layer)** | VP6 | Most abundant structural protein; group antigen (A–J classification); not directly exposed in intact virion |
| **Core** | VP2 (structural), VP1 (RdRp), VP3 (capping enzyme) | RNA replication and genome packaging |
| **Non-structural proteins** | NSP1–NSP6 | NSP4 (enterotoxin, Ca2+ channel modulator), NSP3 (translation enhancer), NSP1 (IFN antagonist) |
| **Genome** | 11 dsRNA segments; 18.5 kb total | Encodes 6 structural (VP1-4, VP6, VP7) and 6 non-structural proteins (NSP1-6) |
| **Particle size** | 70–75 nm | Triple-layered icosahedral particle |

### NSP4 — The Viral Enterotoxin

NSP4 is a **non-structural glycoprotein** that functions as a viral enterotoxin: it is secreted by infected enterocytes and acts on adjacent non-infected cells to mobilize intracellular calcium via phospholipase C-independent pathways, activating CFTR and calcium-dependent chloride channels. This secretory signal precedes cell death and accounts for early-onset watery diarrhea before significant villous destruction occurs — a defining mechanistic feature distinguishing rotavirus from other enteric pathogens [^estes-2006-rotavirus-biology].

## Infection Mechanism

### 1. Cell Attachment

Rotavirus attachment to the enterocyte surface is a sequential, multi-step process:

1. **VP8* (tip of VP4 spike)** binds **histo-blood group antigens (HBGAs)** or sialylated glycolipids on the villus tip enterocyte surface — the specific ligand varies by strain (P[8] binds Lewis b/H type 1; P[4] binds Lewis x/Lewis b; P[6] binds A antigen)
2. **Hsc70 and integrins** (α2β1, αvβ3, αxβ2) serve as post-attachment receptors mediating tight virus-cell contact
3. **VP5*** (stalk of VP4) undergoes conformational change analogous to class II fusion proteins, driving viral penetration

### 2. Entry and Replication

Rotavirus enters via **receptor-mediated endocytosis** (primarily direct membrane penetration during endosomal acidification). Within the endosome, the outer capsid is lost, generating a transcriptionally active double-layered particle (DLP). The VP1 RdRp transcribes each genome segment into capped positive-sense mRNAs that serve as both templates for translation and — packaged into new core particles — as templates for dsRNA synthesis. Viral assembly occurs in cytoplasmic **viroplasms** (inclusions containing NSP2, NSP5, VP1, VP2, VP3, and VP6), and new triple-layered particles bud through the endoplasmic reticulum, acquiring VP7 and VP4 from ER membranes before release [^mandell-principles].

### 3. Infectious Dose and Spread

The infectious dose for rotavirus is estimated at 10–100 particles (HID50 ~10 PFU in volunteers). Shedding in feces during acute infection can reach 10^10–10^12 particles/mL, and the virus survives on hands for up to 4 hours and on surfaces for days. Transmission is primarily **fecal-oral** via contaminated hands, fomites, water, and food. Respiratory transmission has been proposed but not confirmed [^tate-2016-who-mortality].

## Host Interactions

### Immune Evasion

- **NSP1** is the principal IFN antagonist: it targets IRF3, IRF5, IRF7, and β-TrCP (an E3 ubiquitin ligase required for NF-κB and IFN induction) for proteasomal degradation, broadly suppressing innate immune gene expression [^estes-2006-rotavirus-biology]
- **VP3** has 2'-5'-phosphodiesterase (PDE) activity that degrades 2-5A oligoadenylates, blocking RNase L activation downstream of the OAS pathway
- Rotavirus replicates in viroplasms that sequester dsRNA from cytosolic pattern recognition receptors (RIG-I, MDA5)

### Cell Tropism

Rotavirus infects **mature villus tip enterocytes** of the small intestine, particularly in the proximal jejunum. Crypt cells and immature enterocytes are relatively resistant, which contributes to the self-limiting nature of infection: villous regeneration from crypt stem cells occurs over 3–5 days. In immunocompromised hosts (severe combined immunodeficiency, HIV, post-transplant), rotavirus can establish **chronic infection** and spread beyond the gut to bile ducts, liver, and potentially other organs via systemic viremia [^parashar-2016-vaccine-impact].

### Secretory IgA and Protection

Protective immunity to rotavirus involves **virus-specific fecal IgA** (correlates with protection against reinfection), serum IgA, and VP6-specific antibodies (which protect from within the transcytosis pathway). VP4 (P-type) and VP7 (G-type) are the primary neutralizing antibody targets. Homotypic immunity after natural infection is robust; heterotypic cross-protection is partial, explaining how children can be reinfected with a different strain. Vaccine-induced immunity is more modest than natural immunity in low-income country settings — a finding attributed to differences in gut microbiota, co-infections, and maternal antibody interference [^tate-2016-who-mortality].

## Pathology

### Disease Spectrum

| Presentation | Typical Host | Features |
|:---|:---|:---|
| Asymptomatic infection | Neonates, re-exposed adults | Common; neonatal strains (P[6]) often non-pathogenic |
| Mild-to-moderate gastroenteritis | Children 6 months – 2 years | Watery diarrhea 3–8 days, vomiting, low fever; ORT sufficient |
| Severe dehydrating gastroenteritis | Children 3 months – 2 years, elderly | High-volume watery diarrhea, profound dehydration; IV rehydration required; major cause of mortality |
| Chronic infection | Immunocompromised (SCID, HIV, transplant) | Persistent diarrhea weeks-months; evolving viral quasi-species; biliary involvement |
| Extraintestinal manifestations | Rarely in healthy hosts | Hepatitis, encephalopathy, benign convulsions with mild gastroenteritis (CwG) |

### Pathophysiology

The classic rotavirus diarrheal mechanism involves two overlapping phases:
1. **Early NSP4-mediated secretory diarrhea**: NSP4 acts as a secretagogue, elevating intracellular Ca2+ in non-infected enterocytes and activating chloride secretion before significant structural damage
2. **Late malabsorptive diarrhea**: villous tip cell lysis and sloughing reduces absorptive surface area, impairs sodium-glucose cotransporter (SGLT1) activity, and reduces brush-border disaccharidase levels — producing osmotic diarrhea from carbohydrate malabsorption

### Treatment

Treatment is **supportive**:
- **Oral rehydration therapy (ORT)** using WHO low-osmolarity solution: first-line for mild-moderate dehydration
- **Intravenous fluids** (Ringer's lactate or normal saline) for severe dehydration or inability to tolerate oral intake
- **Zinc supplementation** (10–20 mg/day for 10–14 days): reduces duration and severity in low-income country settings (WHO/UNICEF recommendation)
- **Nitazoxanide**: modest evidence for shortening duration in immunocompetent children; not universally recommended

### Vaccines

| Vaccine | Type | Coverage | Efficacy (high-income/low-income) |
|:---|:---|:---|:---|
| **Rotarix** (GSK) | Monovalent G1P[8] oral live-attenuated | 2 doses at 6, 10 weeks | ~85–90% / ~50–65% against severe disease |
| **RotaTeq** (Merck) | Pentavalent G1-4/P[8] oral live-attenuated | 3 doses at 2, 4, 6 months | ~85–98% / ~39–63% against severe disease |
| **ROTAVAC** (Bharat) | Monovalent 116E human-bovine reassortant | 3 doses | ~55% against severe disease in India |
| **RotaSIIL** (SII) | Pentavalent, bovine-human reassortant | 3 doses | ~67% against severe disease in India |

## Connections

- **Infects** → [Small Intestine](../../../01-human/06-organ/small-intestine/README.md): Rotavirus infects mature villus tip enterocytes via VP4/VP7-integrin-Hsc70 interactions, causing cytoskeletal disruption, CFTR activation, and NSP4 enterotoxin-driven secretory diarrhea without mucosal destruction.
- **Damages** → [Digestive System](../../../01-human/07-system/digestive-system/README.md): Rotavirus causes villous atrophy, impaired brush-border enzyme activity, and NSP4 enterotoxin-mediated fluid hypersecretion in the digestive system, producing watery diarrhea that rapidly causes fatal dehydration in infants.
- **Prevented-by** → [Rotavirus Vaccine](../../../04-vaccine/02-inactivated/rotavirus-vaccine/README.md): Rotarix (G1P[8] monovalent oral) and RotaTeq (G1-G4/P[8] pentavalent oral) live-attenuated vaccines prevent severe rotavirus gastroenteritis; WHO recommends inclusion in all national immunization programmes.
- **Damages** → [Macrophage](../../../01-human/04-cellular/macrophage/README.md): Rotavirus antigens and particles detected in mesenteric-node macrophages; macrophage activation drives the systemic viremia and biliary excretion seen in immunocompromised hosts with chronic rotavirus infection.

---

> **AI co-maintenance notice:** This entry was drafted with AI assistance and is subject to expert review. Content reflects published literature as of the last_reviewed date. Errors may be present; verify critical facts against primary sources before clinical or research use.

[^mandell-principles]: Bennett JE, Dolin R, Blaser MJ. *Mandell, Douglas, and Bennett's Principles and Practice of Infectious Diseases.* 9th ed. Elsevier; 2020.
[^murray-microbiology]: Murray PR, Rosenthal KS, Pfaller MA. *Medical Microbiology.* 9th ed. Elsevier; 2021.
[^tate-2016-who-mortality]: Tate JE, Burton AH, Boschi-Pinto C, Parashar UD. Global, regional, and national estimates of rotavirus mortality in children <5 years of age, 2000-2013. *Clin Infect Dis.* 2016;62(Suppl 2):S96-S105. [doi:10.1093/cid/civ1013](https://doi.org/10.1093/cid/civ1013) · [PubMed 26966244](https://pubmed.ncbi.nlm.nih.gov/26966244/)
[^estes-2006-rotavirus-biology]: Estes MK, Kapikian AZ. Rotaviruses. In: Knipe DM, Howley PM, eds. *Fields Virology.* 5th ed. Lippincott Williams & Wilkins; 2007:1917-1974.
[^parashar-2016-vaccine-impact]: Parashar UD, Johnson H, Estes MK, Gentsch JR. Global illness and deaths caused by rotavirus disease in children. *Emerg Infect Dis.* 2003;9(5):565-572. [doi:10.3201/eid0905.020562](https://doi.org/10.3201/eid0905.020562) · [PubMed 12737740](https://pubmed.ncbi.nlm.nih.gov/12737740/)
