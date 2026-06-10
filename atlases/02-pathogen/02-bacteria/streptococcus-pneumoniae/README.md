---
schema: pathogen-entry/v1
id: streptococcus-pneumoniae
name: Streptococcus pneumoniae
atlas: 02-pathogen
scale: 02-bacteria
status: draft
last_reviewed: 2026-06-04
summary: "Gram-positive, encapsulated, alpha-hemolytic diplococci. Leading cause of community-acquired pneumonia and bacterial meningitis in adults globally. >100 serotypes defined by polysaccharide capsule; preventable with PCV13 and PPSV23 vaccines."
aliases: ["pneumococcus", "S. pneumoniae", "Diplococcus pneumoniae"]
taxonomy:
  family: Streptococcaceae
  genus: Streptococcus
genome: "DNA, ~2.1 Mb circular chromosome; Gram-positive (thick peptidoglycan, no outer membrane)"
replication_site: "upper respiratory tract (nasopharynx), lungs, blood, meninges"
transmission: "respiratory droplets, direct contact with respiratory secretions"
tags:
  - streptococcus
  - pneumonia
  - bacterial
  - meningitis
  - polysaccharide-capsule
  - penicillin
  - vaccine-preventable
sources:
  - id: tillett-francis-1930
    type: peer-reviewed
    cite: "Tillett WS, Francis T Jr. Serological reactions in pneumonia with a non-protein somatic fraction of pneumococcus. J Exp Med. 1930;52(4):561-71."
    pmid: "19869631"
    url: "https://pubmed.ncbi.nlm.nih.gov/19869631/"
  - id: klugman-2002-resistance
    type: peer-reviewed
    cite: "Klugman KP. Pneumococcal resistance to antibiotics. Clin Microbiol Rev. 2002;15(4):716-22. (See also: Klugman KP. Pneumococcal resistance to antibiotics. N Engl J Med. 2002.)"
    doi: "10.1056/NEJMra013578"
    url: "https://doi.org/10.1056/NEJMra013578"
  - id: bonten-2015-capita
    type: peer-reviewed
    cite: "Bonten MJ, Huijts SM, Bolkenbaas M, et al. Polysaccharide conjugate vaccine against pneumococcal pneumonia in adults. N Engl J Med. 2015;372(12):1114-25. (CAPiTA trial)"
    doi: "10.1056/NEJMoa1408544"
    url: "https://doi.org/10.1056/NEJMoa1408544"
cross_links:
  - target: 01-human/06-organ/lung
    relation: infects
    note: "S. pneumoniae is the most common cause of community-acquired lobar pneumonia; aspiration of colonised nasopharyngeal secretions seeds the alveolar space, causing alveolar consolidation with fibrinous exudate — classic lobar pneumonia."
  - target: 01-human/07-system/respiratory-system
    relation: infects
    note: "Colonises the nasopharynx (carrier state 5–70% by age); spreads contiguously to sinuses, middle ear, and lower respiratory tract; invasive disease follows bloodstream dissemination."
  - target: 01-human/07-system/respiratory-system
    relation: damages
    note: "Pneumococcal pneumonia causes acute lobar consolidation, alveolar flooding with inflammatory exudate, impaired gas exchange, and — in severe disease — respiratory failure requiring mechanical ventilation."
  - target: 01-human/07-system/immune-system
    relation: infects
    note: "Pneumolysin disrupts complement activation and inhibits oxidative burst in phagocytes; PspA and CbpA impair complement deposition and antibody-mediated opsonophagocytosis — key evasion of innate and adaptive immunity."
  - target: 01-human/03-molecular/immunoglobulin-g
    relation: target-of
    note: "Serotype-specific IgG antibodies against the polysaccharide capsule are the primary correlate of vaccine-mediated protection; PCV-elicited T-dependent IgG persists longer than PPSV23-elicited T-independent responses."
  - target: 03-medicine/01-modern/06-antimicrobial/amoxicillin
    relation: treated-by
    note: "S. pneumoniae is the primary target for amoxicillin in community-acquired pneumonia; high-dose amoxicillin (3g/day) overcomes intermediate-level penicillin resistance via PBP2b affinity changes (MIC ≤2 mg/L)."
---

# Streptococcus pneumoniae

## Overview

*Streptococcus pneumoniae* (the **pneumococcus**) is a **Gram-positive, alpha-hemolytic, encapsulated diplococcus** of the family Streptococcaceae. It is the leading cause of **community-acquired pneumonia (CAP)**, **bacterial meningitis in adults**, bacteremia, otitis media, and sinusitis globally. It colonises the human nasopharynx asymptomatically in a substantial fraction of healthy individuals — particularly children (up to 70% carriage in toddlers) — from which it spreads by respiratory droplets and secretion contact.

The pneumococcus is one of the most clinically significant human pathogens and simultaneously one of the great vaccine-prevention success stories. Introduction of pneumococcal conjugate vaccines (PCV7 in 2000, PCV13 in 2010) has dramatically reduced invasive pneumococcal disease (IPD) in immunised populations and generated broad herd protection in non-immunised adults via reduced carriage transmission [^bonten-2015-capita].

Antibiotic resistance — particularly penicillin non-susceptibility mediated by altered penicillin-binding protein (PBP) mutations — is a growing global challenge, but penicillin/amoxicillin remains first-line for drug-susceptible strains and for most non-meningeal disease with appropriate dose escalation.

## Structure

### Morphology

*S. pneumoniae* presents as **lancet-shaped diplococci** (pairs of elongated cocci with pointed ends pointing away from each other) measuring approximately 1.2 µm in diameter. On blood agar, colonies display characteristic **alpha-hemolysis** — a greenish zone of partial haemolysis due to production of pneumolysin-related haem oxidation — distinguishing them from beta-haemolytic streptococci. Organisms are non-motile and non-spore-forming.

### Polysaccharide Capsule — Primary Virulence Factor

The defining structural and virulence feature of *S. pneumoniae* is its **polysaccharide capsule**, which:

- Surrounds the cell wall and varies in chemical composition across serotypes
- Defines over **100 distinct serotypes** (serogroups 1–48 plus subtypes); serotyping is performed by the Quellung reaction (capsule swelling with type-specific antisera)
- Acts as the primary **antiphagocytic** virulence factor: negatively charged polysaccharide repels phagocyte receptors, inhibits opsonisation, and resists complement deposition
- Is the immunodominant antigen for both natural immunity and vaccine responses

Non-encapsulated (unencapsulated) strains are essentially avirulent — demonstrating that the capsule is essential for invasive disease.

### Cell Wall and Other Structural Components

| Component | Description | Role |
|:---|:---|:---|
| **Peptidoglycan** | Thick layer; Gram-positive staining | Structural rigidity; target of penicillin via PBP binding |
| **Teichoic acid / Lipoteichoic acid** | Phosphocholine-decorated polymers | Receptor for platelet-activating factor receptor (PAFr) on epithelial cells → bacterial adhesion and translocation |
| **PspA (Pneumococcal Surface Protein A)** | Surface-exposed choline-binding protein | Inhibits complement deposition (binds and inhibits factor H activation) |
| **CbpA (PspC/SpsA)** | Complement-binding protein | Binds secretory IgA and complement factor H; promotes nasopharyngeal colonisation |
| **Autolysin (LytA)** | Murein hydrolase | Regulated cell lysis releasing pneumolysin and cell wall fragments into host tissue; mediates penicillin's lytic killing |

### Key Toxins and Secreted Virulence Factors

**Pneumolysin** is the most important secreted virulence factor:
- A **pore-forming toxin** (CDC — cholesterol-dependent cytolysin family) that binds membrane cholesterol and oligomerises into ~30 nm transmembrane pores
- Kills ciliated respiratory epithelial cells, disrupting mucociliary clearance
- Inhibits the oxidative burst and phagocyte migration
- Activates complement, contributing to inflammatory tissue damage
- At sub-lytic concentrations, triggers apoptosis and modulates cytokine production
- Released primarily by LytA-mediated autolysis during antibiotic-induced cell death — explaining the paradox of transient clinical worsening with antibiotic initiation in meningitis (dexamethasone co-administration reduces this)

Additional virulence factors include:
- **Hyaluronidase and neuraminidase (NanA, NanB):** Degrade mucus and host glycoproteins to expose underlying epithelial receptors; facilitate biofilm formation
- **IgA protease:** Cleaves secretory IgA at the hinge region, disabling the primary mucosal antibody
- **Hydrogen peroxide:** Produced in quantity; causes DNA damage and ciliary paralysis in epithelial cells

## Infection Mechanism

### Nasopharyngeal Colonisation

*S. pneumoniae* is an **obligate human commensal** at its ecological niche in the nasopharynx. Colonisation:
- Occurs via respiratory droplet acquisition; typically asymptomatic
- Carriage rates: 5–10% in adults, 20–60% in school-age children; up to 70% in toddlers in high-density settings
- Each colonisation episode with a new serotype lasts 1–6 months in children, shorter in adults
- A single person carries one or occasionally two serotypes simultaneously; serotype competition influences carriage ecology
- Colonisation is a prerequisite for invasive disease — vaccine-mediated reduction in carriage is the mechanism of herd protection

Adhesion molecules mediating colonisation:
- **Phosphocholine on teichoic acid** binds PAFr (platelet-activating factor receptor) on nasopharyngeal epithelium
- **PspC (CbpA)** binds polymeric immunoglobulin receptor (pIgR) for transcytosis across epithelium
- **Neuraminidase** exposes underlying receptors by cleaving mucus glycoprotein sialic acids

### Progression to Invasive Disease

The transition from asymptomatic colonisation to invasive disease is facilitated by:
1. **Viral co-infection** (especially influenza): damages the mucosal barrier, impairs mucociliary clearance, and transiently suppresses innate immunity → allows pneumococcal descent to the lower respiratory tract
2. **Aspiration** of colonised secretions (anesthesia, alcohol, seizures, stroke)
3. **Impaired local/systemic immunity**: functional asplenia, hypogammaglobulinemia, HIV, complement deficiencies
4. **Viral respiratory infection in children**: respiratory syncytial virus (RSV) increases receptor expression for pneumococcal adhesins

Once in the lower respiratory tract:
- Alveolar macrophages phagocytose pneumococci; overwhelmed macrophages undergo cytolysis → massive inflammatory cascade
- Polymorphonuclear neutrophil (PMN) influx → alveolar filling with inflammatory exudate (consolidation)
- **Red hepatisation:** alveoli flooded with erythrocytes and fibrin → rust-coloured sputum (classic pneumococcal sign)
- **Grey hepatisation:** PMN-dominant consolidation; liver-like consistency
- **Resolution:** fibrinolysis and macrophage clearance → lobular restoration (most cases)

Bacteremia occurs in ~25–30% of pneumococcal pneumonia; once in blood, the organism can seed:
- **Meninges:** causing bacterial meningitis (most common bacterial cause in adults globally)
- **Pericardium** (purulent pericarditis)
- **Joints** (septic arthritis)
- **Pleural space** (empyema)

## Host Interactions

### Immune Response and Evasion

| Immune component | Pneumococcal interaction |
|:---|:---|
| **Complement** | Capsule prevents C3b deposition; PspA inhibits factor H-independent complement activation; pneumolysin activates complement and C-reactive protein (CRP) binds phosphocholine to activate classical pathway |
| **Innate phagocytes** | Capsule is antiphagocytic — without opsonising IgG/C3b, macrophages cannot efficiently engulf pneumococci |
| **Neutrophils** | Recruited in massive numbers during pneumonia; oxidative burst neutralised by pneumolysin at sub-lytic concentrations |
| **Adaptive immunity (IgG)** | Serotype-specific IgG against capsular polysaccharide is the definitive opsonin; titers ≥0.35 µg/mL correlate with protection (WHO/FDA threshold) |

The polysaccharide capsule by itself is a **T-independent antigen** in adults — it can elicit IgM and class-switched IgG without T-cell help via B-cell crosslinking, but responses are weak and non-boostable in children <2 years (no immunologic memory established). **Protein conjugation** in PCV overcomes this by converting the polysaccharide into a T-dependent antigen recognised by CD4⁺ T helper cells, generating affinity maturation, class switching, and memory B cells.

### C-Reactive Protein (CRP)

The **discovery of CRP** by Tillett and Francis in 1930 [^tillett-francis-1930] used pneumococcal somatic fraction (C-polysaccharide of the cell wall) precipitating with serum of acutely ill patients — the founding experiment in acute-phase protein biology. CRP binds phosphocholine on the pneumococcal cell wall and activates the classical complement pathway — a physiological opsonisation mechanism.

## Connections

- **Infects** → [Lung](../../../01-human/06-organ/lung/README.md): primary site of pneumococcal pneumonia; lobar consolidation, rust-coloured sputum, alveolar flooding.
- **Infects** → [Respiratory System](../../../01-human/07-system/respiratory-system/README.md): colonises nasopharynx; spreads to sinuses, middle ear, lower respiratory tract.
- **Damages** → [Respiratory System](../../../01-human/07-system/respiratory-system/README.md): pneumolysin destroys ciliated epithelium, lobar pneumonia impairs gas exchange.
- **Damages** → [Lung](../../../01-human/06-organ/lung/README.md): consolidation, cavitation (rare), parapneumonic effusion, empyema.
- **Infects** → [Immune System](../../../01-human/07-system/immune-system/README.md): evasion of complement and phagocytic killing by capsule and PspA; pneumolysin impairs phagocyte function.
- **Target-of** → Immunoglobulin G: serotype-specific IgG is the primary protective antibody; vaccine responses correlate with IgG titer ≥0.35 µg/mL.
- **Treated by** → PCV13 and PPSV23: pneumococcal conjugate and polysaccharide vaccines.
- **Treated-by** → [Amoxicillin](../../../03-medicine/01-modern/06-antimicrobial/amoxicillin/README.md): Primary clinical target in CAP, AOM, and sinusitis; high-dose amoxicillin (3g/day) overcomes intermediate resistance via PBP2b affinity changes; ceftriaxone preferred for meningitis.

## Pathology

### Clinical Syndromes

| Syndrome | Features |
|:---|:---|
| **Lobar pneumonia (CAP)** | Acute onset fever, pleuritic chest pain, productive cough with rust-coloured (blood-tinged, fibrinous) sputum; lobular or lobar consolidation on chest X-ray; Gram stain of sputum shows lancet-shaped diplococci; most common in elderly, alcoholics, asplenic patients |
| **Bacteremia** | ~25–30% of pneumococcal pneumonia; primary bacteremia (no obvious focus) common in children and asplenic adults; fulminant sepsis with DIC in asplenic patients (overwhelming post-splenectomy infection, OPSI) |
| **Bacterial meningitis** | Leading bacterial cause in adults globally; presents with fever, headache, neck stiffness (meningismus), photophobia, altered consciousness; Kernig's sign (inability to extend knee with flexed hip) and Brudzinski's sign (reflex hip flexion on neck flexion); CSF: polymorphonuclear pleocytosis, low glucose, high protein, Gram-positive diplococci; mortality 20–30%; neurological sequelae in survivors |
| **Otitis media** | Most common complication in children; *S. pneumoniae* is the #1 bacterial cause; middle ear effusion, otalgia, tympanic membrane bulging; may progress to mastoiditis |
| **Sinusitis** | Maxillary sinusitis most common; facial pain, nasal discharge; typically following viral URI |
| **Empyema** | Infected pleural fluid complicating pneumonia; requires drainage in addition to antibiotics; fibropurulent or organised stages may require surgical decortication |
| **Pericarditis** | Rare; purulent pericarditis with tamponade risk; requires pericardiocentesis |

### Resistance Mechanisms

Pneumococcal resistance to beta-lactams is **not mediated by beta-lactamase** — unlike most Gram-positive resistance. Instead:
- **Altered penicillin-binding proteins (PBPs):** Mutations in *pbp1a*, *pbp2b*, and *pbp2x* genes (often acquired via horizontal gene transfer from viridans streptococci) reduce penicillin binding affinity
- Resistance is therefore not reversed by beta-lactamase inhibitors (e.g., clavulanic acid has no benefit)
- Penicillin MIC breakpoints: susceptible ≤0.06 µg/mL (oral); intermediate/resistant defined differently for CNS vs. non-CNS infections
- **Macrolide resistance** (erythromycin A ribosomal methylase, *erm(B)*; efflux pump *mef(A)*): >40% of strains in some regions
- **Fluoroquinolone resistance** (rare but increasing): *parC* and *gyrA* mutations

### Treatment

- **Drug-susceptible pneumococcal pneumonia:** Amoxicillin (oral, outpatient); benzylpenicillin or amoxicillin IV (inpatient); beta-lactams remain fully active in most non-CNS infections even with intermediate MICs when dosed appropriately
- **Bacterial meningitis:** Ceftriaxone 2g IV q12h ± vancomycin (for resistant strains) + dexamethasone 0.15 mg/kg q6h × 4 days (reduces neurological sequelae via blunting pneumolysin-driven inflammation)
- **Penicillin-resistant strains:** Ceftriaxone (for most); levofloxacin or moxifloxacin (CAP with resistance concerns); linezolid or vancomycin (high-level resistance or meningitis)

### Prevention

| Vaccine | Type | Mechanism | Use |
|:---|:---|:---|:---|
| **PCV13 (Prevnar 13)** | 13-valent conjugate; polysaccharide coupled to CRM197 carrier protein | T-dependent IgG; memory B cells; reduces carriage → herd protection | Children (primary series 2, 4, 6, 12–15 mo); adults ≥65; immunocompromised |
| **PPSV23 (Pneumovax 23)** | 23-valent unconjugated polysaccharide | T-independent IgG; no memory; no herd protection; poor response in <2 years | Adults ≥65; asplenic; immunocompromised ≥2 years old |
| **PCV15/PCV20** | Newer conjugates with expanded coverage | T-dependent; higher valence than PCV13 | Replacing PCV13 in many national programs |

The **CAPiTA trial** (Bonten 2015) [^bonten-2015-capita] demonstrated for the first time that PCV13 reduces vaccine-type community-acquired pneumonia in adults ≥65 (45% efficacy for vaccine-type CAP, 75% for vaccine-type non-bacteraemic CAP) — establishing a role for conjugate vaccines in adult immunization programs.

## See Also

- [Lung](../../../01-human/06-organ/lung/README.md) — primary site of pneumococcal disease.
- [Respiratory System](../../../01-human/07-system/respiratory-system/README.md) — system affected.
- [Mycobacterium tuberculosis](../mycobacterium-tuberculosis/README.md) — another major bacterial respiratory pathogen.

[^tillett-francis-1930]: Tillett WS, Francis T Jr. Serological reactions in pneumonia with a non-protein somatic fraction of pneumococcus. *J Exp Med.* 1930;52(4):561-71. [PubMed 19869631](https://pubmed.ncbi.nlm.nih.gov/19869631/)
[^klugman-2002-resistance]: Klugman KP. Pneumococcal resistance to antibiotics. *N Engl J Med.* 2002. [doi:10.1056/NEJMra013578](https://doi.org/10.1056/NEJMra013578)
[^bonten-2015-capita]: Bonten MJ, Huijts SM, Bolkenbaas M, et al. Polysaccharide conjugate vaccine against pneumococcal pneumonia in adults. *N Engl J Med.* 2015;372(12):1114-25. [doi:10.1056/NEJMoa1408544](https://doi.org/10.1056/NEJMoa1408544)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
