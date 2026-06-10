---
schema: pathogen-entry/v1
id: escherichia-coli
name: Escherichia coli
atlas: 02-pathogen
scale: 02-bacteria
status: draft
last_reviewed: 2026-06-05
summary: "Gram-negative rod; dominant facultative anaerobe of the human colon. Commensal in health; pathotypes (EPEC, ETEC, EHEC O157:H7, ExPEC) cause gastroenteritis, UTI, neonatal meningitis, and Shiga-toxin HUS. Leading cause of healthcare-associated UTI and Gram-negative bacteraemia."
aliases: ["E. coli", "coliform", "ETEC", "EPEC", "EHEC", "STEC", "ExPEC", "UPEC"]
sources:
  - id: kaper-2004-pathogenic-ecoli
    type: peer-reviewed
    cite: "Kaper JB, Nataro JP, Mobley HL. Pathogenic Escherichia coli. Nat Rev Microbiol. 2004;2(2):123-40."
    doi: "10.1038/nrmicro818"
    pmid: "15040260"
    url: "https://doi.org/10.1038/nrmicro818"
  - id: croxen-2010-ecoli-pathogenicity
    type: peer-reviewed
    cite: "Croxen MA, Finlay BB. Molecular mechanisms of Escherichia coli pathogenicity. Nat Rev Microbiol. 2010;8(1):26-38."
    doi: "10.1038/nrmicro2265"
    pmid: "19966814"
    url: "https://doi.org/10.1038/nrmicro2265"
cross_links:
  - target: 01-human/07-system/digestive-system
    relation: infects
    note: "E. coli colonises the large intestine as the dominant facultative anaerobe in health. Pathogenic strains (EPEC, ETEC, EHEC, EIEC) cause gastroenteritis via distinct virulence mechanisms: ETEC secretes heat-labile (LT) and heat-stable (ST) enterotoxins; EPEC and EHEC use type III secretion to inject effectors into enterocytes; EIEC invades colonic epithelial cells like Shigella."
  - target: 01-human/06-organ/liver
    relation: damages
    note: "E. coli bacteraemia via portal or systemic routes seeds hepatic abscesses. In cirrhosis patients, E. coli is the most common cause of spontaneous bacterial peritonitis (SBP) — bacterial translocation from gut to peritoneal cavity — and subsequent hepatorenal syndrome. LPS (endotoxin) activates hepatic Kupffer cells and drives hepatic inflammation."
  - target: 01-human/04-cellular/hepatocyte
    relation: damages
    note: "LPS (lipopolysaccharide/endotoxin) from E. coli outer membrane binds TLR4 on hepatic Kupffer cells, triggering TNF-α and IL-1β release. These cytokines induce hepatocyte apoptosis via TRAIL-R/caspase-8 and TNFR1/caspase pathways. In septic shock, this cascade contributes to acute liver injury and elevated transaminases seen in Gram-negative sepsis."
  - target: 01-human/05-tissue/intestinal-epithelium
    relation: infects
    note: "EPEC/EHEC T3SS injects Tir, Map, EspF into enterocytes → attaching-effacing lesions; EspF disrupts tight junctions → barrier loss; EIEC invades colonic epithelium like Shigella; UPEC invades urothelial umbrella cells forming IBCs → recurrent UTI."
  - target: 01-human/06-organ/kidney
    relation: damages
    note: "UPEC ascends ureters via P fimbriae → pyelonephritis; EHEC Shiga toxin (Stx2) attacks Gb3-rich glomerular endothelium → endothelial lysis → platelet microthrombi → HUS triad (MAHA+thrombocytopenia+AKI); HUS causes AKI in 5-15% EHEC infections; 25% long-term CKD."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "E. coli LPS (TLR4) and flagellin (TLR5/NLRC4) trigger IL-8 → neutrophil recruitment; UPEC reduces flagellin expression to evade neutrophil detection; UPEC IBCs resist neutrophil killing; EHEC Stx causes neutropenia in HUS via bone marrow suppression."
---

# Escherichia coli

## Overview

*Escherichia coli* is simultaneously the most important **model organism in molecular biology** and one of the most important **human pathogens**. Named after Theodor Escherich who first described it in 1885 as "Bacterium coli commune," *E. coli* is a **Gram-negative, facultative anaerobic rod** (Enterobacteriaceae / Enterobacterales) that colonises the human large intestine within hours of birth and persists throughout life. In health, *E. coli* constitutes ~0.1% of total gut bacteria by count but represents the numerically dominant **facultative anaerobe** (~10⁸ CFU/g of colon contents) — an important niche given the largely obligate anaerobe-dominated microbiome [^kaper-2004-pathogenic-ecoli].

The duality of *E. coli* — commensal and pathogen — is explained by the enormous **pan-genome diversity** of the species. The *E. coli* pan-genome contains >90,000 genes; a typical *E. coli* strain encodes only ~4,000–5,500. Pathogenic strains acquired virulence gene clusters on mobile genetic elements (pathogenicity islands, plasmids, phages) that distinguish them from benign commensals. Six major **pathotypes** (variants with distinct virulence strategies) cause intestinal disease; a separate group (**ExPEC** — extraintestinal pathogenic *E. coli*) causes UTIs, bacteraemia, and neonatal meningitis [^croxen-2010-ecoli-pathogenicity].

Clinical importance:
- **UTI:** ~80–85% of community-acquired UTIs and >40% of healthcare-associated UTIs caused by UPEC (uropathogenic *E. coli*); 150 million UTIs/year globally
- **Neonatal meningitis:** *E. coli* K1 is the second most common cause of neonatal meningitis (after Group B Streptococcus); case-fatality rate 15–40%; neurological sequelae in >30% of survivors
- **Traveller's diarrhoea:** ETEC causes ~80% of cases among travellers to developing countries; 10–20 million cases/year
- **EHEC O157:H7:** Produces Shiga toxin (Stx1/Stx2); causes haemorrhagic colitis and haemolytic uraemic syndrome (HUS) — the leading cause of acute kidney injury in children; notable outbreaks from contaminated beef, spinach, and sprouts
- **Bacteraemia:** Leading cause of Gram-negative bacteraemia in hospitalised patients; case-fatality rate ~20–30%; third most common cause of bacteraemia overall (after *S. aureus* and coagulase-negative staphylococci)

## Structure

### Morphology

*E. coli* cells are **straight rods** (1.0–2.0 µm × 0.4–0.7 µm), occurring singly or in pairs. Most strains are **peritrichously flagellated** (multiple flagella distributed over cell surface; H antigens), enabling motility through liquid environments. Many strains express **fimbriae/pili** (thin filamentous surface appendages): **type 1 fimbriae** (mannose-sensitive; encoded by *fim* genes) and **P fimbriae** (mannose-resistant; encoded by *pap* genes) for adhesion; and **sex pili** for conjugation.

### Cell Envelope

The Gram-negative cell envelope is critical to *E. coli* pathogenicity and antibiotic resistance:

| Layer | Composition | Function / Clinical Relevance |
|:---|:---|:---|
| **Cytoplasmic membrane** | Phospholipid bilayer | Selective permeability; electron transport chain |
| **Periplasm** | Gel-like compartment (~13–25 nm); contains peptidoglycan (thin, 2–3 nm) | β-lactamases reside here (CTX-M ESBL, KPC carbapenemase); osmosensors |
| **Outer membrane (OM)** | Asymmetric lipid bilayer: inner leaflet (phospholipids), outer leaflet (LPS); β-barrel proteins (OmpA, OmpC, OmpF porins) | Permeability barrier; LPS is the endotoxin; porins are route of entry for hydrophilic antibiotics |
| **Lipopolysaccharide (LPS)** | Lipid A (toxic moiety, TLR4 agonist) + core polysaccharide + O-antigen side chains (serotype determinant) | Lipid A is the major endotoxin; O-antigen serology (O1, O6, O157, etc.) defines serotype; O-antigen impairs complement deposition |
| **Capsule (K antigen)** | Polysialic acid in K1 strains (neonatal meningitis); K2, K5, K100 in UPEC | Resists complement-mediated killing; K1 polysialic acid mimics human neural cell adhesion molecules (NCAMs) — molecular mimicry for CNS invasion |

### O:H Serotyping

*E. coli* strains are designated by **O (LPS O-antigen), H (flagellar), and K (capsular)** antigen serotypes:
- **O157:H7** — the archetypal EHEC serotype responsible for the 1982 US outbreak and most subsequent HUS outbreaks
- **O1:K1:H7** — dominant neonatal meningitis strain
- **O6:H1** and **O18:K1:H7** — common UPEC serotypes
- More than 700 O-antigen serogroups and 56 H antigens are recognised

### Genome

- **Genome size:** ~4.6 Mb (K-12 reference E. coli MG1655); GC content ~50.8%; ~4,200–5,500 coding sequences
- **Extensive pan-genome:** Core genome ~3,000 genes; accessory genome includes pathogenicity islands (LEE, PAI I–V), plasmids, and integrated phages
- **Pathogenicity islands (PAIs):** Large genomic inserts (10–200 kb) acquired by horizontal gene transfer; encode type III/IV/V secretion systems, fimbriae, toxins, iron acquisition systems
- **Key resistance elements:** CTX-M-type ESBLs (plasmid-encoded; hydrolyse 3rd-gen cephalosporins); KPC and NDM carbapenemases (plasmid-encoded; hydrolyse carbapenems); *mcr-1* plasmid (colistin resistance); fluoroquinolone resistance via *gyrA*/*parC* mutations and *qnr* plasmid genes

## Infection Mechanism

### Intestinal Pathotypes

*E. coli* intestinal pathotypes use fundamentally distinct virulence strategies classified by molecular mechanism:

| Pathotype | Acronym | Virulence Mechanism | Disease |
|:---|:---|:---|:---|
| **Enterotoxigenic** | ETEC | LT (heat-labile toxin, ADP-ribosylates Gsα → ↑cAMP → Cl⁻ secretion) and/or ST (heat-stable toxin, activates guanylate cyclase → ↑cGMP → Cl⁻ secretion); CFA/CS colonisation factor adhesins | Watery traveller's diarrhoea; cholera-like severe secretory diarrhoea in children in developing world |
| **Enteropathogenic** | EPEC | Locus of Enterocyte Effacement (LEE) — type III secretion system (T3SS) injects effectors (Tir, Map, EspF) into enterocytes; Tir is receptor for intimin (bacterial adhesin) → attaching and effacing (A/E) lesion; actin pedestal formation | Infant diarrhoea in developing world; non-bloody |
| **Enterohaemorrhagic** | EHEC (STEC) | Same LEE-encoded T3SS as EPEC + Shiga toxin 1/2 (Stx1/Stx2): ribosome-inactivating toxin — binds Gb3 on host cells, cleaves 28S rRNA → protein synthesis arrest → cell death; phage-encoded (Stx2 on lambdoid phage) | Bloody (haemorrhagic) colitis → HUS (haemolytic uraemic syndrome): Stx in circulation attacks glomerular endothelium; microangiopathic haemolytic anaemia + thrombocytopenia + ARF |
| **Enteroinvasive** | EIEC | Virulence plasmid pWR encoding T3SS similar to *Shigella*; invades and replicates in colonic epithelial cells; actin-based intracellular motility (IcsA/VirG) | Dysentery-like: bloody mucoid diarrhoea, fever, tenesmus |
| **Enteroaggregative** | EAEC | Aggregative adherence fimbriae (AAF/I–IV); forms stacked-brick aggregates on mucosa; ST-like enterotoxin (EAST1); dispersin (disperses bacteria for spread) | Persistent diarrhoea (>14 days) in children; traveller's diarrhoea; immunocompromised |
| **Diffusely adherent** | DAEC | Afa/Dr adhesins binding DAF (CD55) on epithelial cells; F1845 fimbriae | Diarrhoea in young children; clinical significance debated |

### ExPEC — Extraintestinal Pathotypes

**Uropathogenic *E. coli*** (UPEC) is the dominant ExPEC pathotype. UTI pathogenesis:

1. **Faecal-perineal-urethral colonisation:** UPEC strains colonising the colon migrate to the perineum (more common in women due to anatomy) and ascend the urethra
2. **Bladder colonisation:** Type 1 fimbriae (FimH tip adhesin) bind mannosylated uroplakin receptors (UPIa/Ib) on bladder urothelium; P fimbriae bind Galα1-4Gal on upper urinary tract glycolipids (implicated in pyelonephritis)
3. **Intracellular bacterial communities (IBCs):** UPEC invades umbrella cells, forms pod-like biofilm-like IBCs (10²–10⁴ bacteria/IBC), protected from antibiotics and immune clearance; source of recurrent UTI
4. **Iron acquisition:** Siderophores (aerobactin, enterobactin, salmochelin, yersiniabactin) scavenge iron from urine (iron-limited environment) — essential virulence determinant in UTI and bacteraemia
5. **Pyelonephritis:** UPEC ascends the ureter (P fimbriae mediated); invades renal tubular cells; triggers TLR4/TLR11 responses; local IL-6, IL-8 surge → pyuria, fever, loin pain

**Neonatal meningitis *E. coli*** (NMEC) — K1 capsule strains:
- Colonise neonatal GI tract at delivery; bacteraemia via gut translocation
- K1 polysialic acid capsule resists complement; IbeA/IbeB invasins breach blood-brain barrier endothelium
- CNS invasion triggers catastrophic neuroinflammation

## Host Interactions

### Innate Immune Engagement

*E. coli* LPS (lipid A) is the archetypal **endotoxin** — the prototypic TLR4 agonist:

1. **LPS recognition:** LBP (LPS-binding protein) transfers LPS monomer to CD14 (soluble or membrane-bound) → presented to TLR4/MD-2 heterodimer → MyD88 and TRIF signalling
2. **Downstream signalling:** NF-κB (TNF-α, IL-1β, IL-6, IL-8) + IRF3 (IFN-β via TRIF)
3. **Physiological concentration:** Triggers local inflammation, neutrophil recruitment, bacterial killing
4. **Pathological concentration (sepsis):** Overwhelming LPS release (during bacteraemia or antibiotic lysis) → systemic TLR4 activation → cytokine storm (TNF-α ↑↑, IL-1β ↑↑) → distributive shock, DIC, multi-organ failure

### Flagellin Sensing

*E. coli* flagellin (H antigen) is detected by **TLR5** (surface sensing) and **IPAF/NAIP** (cytoplasmic sensing via NLRC4 inflammasome):
- TLR5/flagellin → NF-κB → IL-8 (neutrophil recruitment) — important in UTI pathogenesis
- UPEC reduces flagellin expression during bladder colonisation (phase variation) — active immune evasion

### EHEC Shiga Toxin — Target Cell Biology

Shiga toxin (Stx1/Stx2) mechanism in HUS:
1. Stx2 (more potent than Stx1 for HUS) is released from EHEC in the gut → absorbed into bloodstream (possibly via macrophage ferrying)
2. Stx B-subunit pentamer binds **Gb3 (globotriaosylceramide)** on target cells: glomerular endothelium (high Gb3), brain neurons (intermediate Gb3), renal tubular cells
3. Receptor-mediated endocytosis → retrograde transport to ER → A subunit (N-glycosidase) cleaves adenine from 28S rRNA of 60S ribosomal subunit → **irreversible ribosome inactivation → cell death**
4. Glomerular endothelial cell death → platelet microthrombi → MAHA + thrombocytopenia + ARF = HUS triad

### Cytokine Profile

| Context | Profile |
|:---|:---|
| **Commensalism** | Tolerogenic; limited NF-κB activation; tonic IgA; Treg maintenance |
| **Symptomatic UTI** | IL-6, IL-8 (urothelial CXCL8), TNF-α; TLR4/TLR5 activation; neutrophil pyuria |
| **Gram-negative bacteraemia (early)** | IL-6, IL-8, TNF-α, IL-1β; CRP; procalcitonin ↑↑ |
| **Septic shock** | TNF-α ↑↑↑, IL-1β ↑↑, IL-6 ↑↑, IL-10 ↑ (compensatory); endothelial injury → DIC |
| **EHEC/HUS** | Stx-induced endothelial injury → TF (tissue factor) expression → coagulation cascade; relative absence of systemic infection (neutropenia in HUS is paradoxical) |

## Connections

**Infects** → [Digestive system](../../../01-human/07-system/digestive-system/README.md): In health, *E. coli* is a stable low-abundance member of the colonic microbiome. In disease, distinct pathotypes hijack specific intestinal mechanisms — ETEC exploits secretory diarrhoea pathways via cAMP/cGMP upregulation; EHEC uses type III effectors to subvert enterocyte signalling and then Shiga toxin to destroy the vascular endothelium of the colon and beyond.

**Damages** → [Liver](../../../01-human/06-organ/liver/README.md): In cirrhosis, *E. coli* is the most common cause of spontaneous bacterial peritonitis (SBP) — bacterial translocation through the damaged gut barrier seeds the peritoneal cavity and triggers hepatorenal syndrome. In septic shock, endotoxin-driven Kupffer cell activation causes hepatocyte apoptosis and acute liver injury.

**Damages** → [Hepatocyte](../../../01-human/04-cellular/hepatocyte/README.md): LPS from *E. coli* triggers TLR4-mediated TNF-α and IL-1β production by hepatic Kupffer cells. These cytokines induce hepatocyte apoptosis via TNFR1/caspase-8 and TRAIL-R pathways. This hepatocellular injury is a major contributor to the elevated liver enzymes observed in Gram-negative sepsis and to the progressive liver failure in severe septic shock.

**Infects** → [Intestinal Epithelium](../../../01-human/05-tissue/intestinal-epithelium/README.md): EPEC/EHEC use a T3SS to inject effectors (Tir, Map, EspF) into enterocytes, creating attaching-effacing lesions and disrupting tight junctions. EIEC invades the colonic epithelium like Shigella. UPEC invades urothelial umbrella cells to form intracellular bacterial communities (IBCs) protected from antibiotics.

**Damages** → [Kidney](../../../01-human/06-organ/kidney/README.md): UPEC ascends the urinary tract via P fimbriae to cause pyelonephritis, triggering TLR4/TLR11-mediated renal inflammation. EHEC Shiga toxin (Stx2) targets Gb3-rich glomerular endothelial cells → endothelial lysis → microthrombi → haemolytic uraemic syndrome (HUS triad: MAHA + thrombocytopenia + AKI) in 5–15% of EHEC infections.

**Connects to** → [Neutrophil](../../../01-human/04-cellular/neutrophil/README.md): *E. coli* LPS (TLR4) and flagellin (TLR5/NLRC4) drive IL-8-mediated neutrophil recruitment. UPEC downregulates flagellin expression during bladder colonisation to evade detection, and IBCs resist neutrophil killing. EHEC Shiga toxin causes paradoxical neutropenia in HUS by suppressing bone marrow progenitors.

## Pathology

### Disease Spectrum

| Disease / Pathotype | Key Clinical Features | Mortality / Outcome |
|:---|:---|:---|
| **Uncomplicated UTI (UPEC)** | Dysuria, frequency, suprapubic pain; pyuria; nitrite-positive dipstick; E. coli in culture | Excellent; 3–7 days TMP-SMX or nitrofurantoin |
| **Pyelonephritis (UPEC)** | Fever, rigors, loin pain, CVA tenderness; bacteraemia in 20–30% | 1–5%; oral fluoroquinolone or IV cephalosporin |
| **Traveller's diarrhoea (ETEC)** | Watery diarrhoea 12–72h post-exposure; self-limited 3–5 days; dehydration risk in infants | <1% |
| **Infant diarrhoea (EPEC)** | Protracted watery diarrhoea in infants; develops world predominant | 3–25% in developing world (dehydration) |
| **Haemorrhagic colitis (EHEC O157:H7)** | Bloody diarrhoea after 3–4 day incubation; severe abdominal cramps; low-grade fever or afebrile | <1% |
| **HUS (Shiga-toxin)** | Develops in 5–15% EHEC infections; microangiopathic haemolytic anaemia + thrombocytopenia + AKI triad; 7–10 days post-diarrhoea onset | 3–5% acute; 25% long-term CKD |
| **Neonatal meningitis (NMEC K1)** | Fever, bulging fontanelle, seizures; CSF: >1,000 cells; E. coli K1 PCR/culture | 15–40% acute; >30% neurological sequelae |
| **Gram-negative bacteraemia** | Fever/rigors or hypothermia; tachycardia; hypotension; positive blood cultures; biliary/urinary/GI source | 20–30% |
| **Septic shock (ESBL/CRE)** | As above + refractory hypotension; ESBL or carbapenemase-producing E. coli limits treatment options | 40–60% in carbapenem-resistant strains |
| **Spontaneous bacterial peritonitis** | Cirrhotic patients; fever, worsening encephalopathy, abdominal pain; ascitic fluid PMN >250 cells/mm³ | 20–30% in-hospital |

### Antibiotic Resistance — A Critical Global Threat

*E. coli* has emerged as the dominant vehicle for dissemination of **extended-spectrum β-lactamases (ESBLs)** and **carbapenemases** globally:

- **CTX-M ESBLs** (especially CTX-M-15): Plasmid-encoded; hydrolyse 3rd-gen cephalosporins (ceftriaxone, ceftazidime) and penicillins; inhibited by clavulanate/tazobactam (partially); ESBL-E prevalence now 15–30% of community *E. coli* UTI isolates in many countries
- **KPC and NDM carbapenemases:** Hydrolyse carbapenems (meropenem, ertapenem); leave only colistin, fosfomycin, tigecycline, newer β-lactam/β-lactamase inhibitor combinations (ceftazidime-avibactam, meropenem-vaborbactam, imipenem-relebactam) active
- **MCR-1 plasmid (colistin resistance):** First described in China (2015); now globally disseminated; adds colistin resistance to NDM-producing strains → pandrug-resistance
- Treatment for ESBL infections: **ertapenem or meropenem** (carbapenems); **fosfomycin** (for uncomplicated UTI only); **pivmecillinam** (for lower UTI only, not systemic)
- Treatment for CRE: **ceftazidime-avibactam** (KPC, OXA-48); **meropenem-vaborbactam** (KPC); **aztreonam-avibactam** (MBL/NDM); combination strategies for extensively resistant strains

[^kaper-2004-pathogenic-ecoli]: Kaper JB, Nataro JP, Mobley HL. Pathogenic *Escherichia coli*. *Nat Rev Microbiol.* 2004;2(2):123-40. [doi:10.1038/nrmicro818](https://doi.org/10.1038/nrmicro818) · [PubMed 15040260](https://pubmed.ncbi.nlm.nih.gov/15040260/)
[^croxen-2010-ecoli-pathogenicity]: Croxen MA, Finlay BB. Molecular mechanisms of *Escherichia coli* pathogenicity. *Nat Rev Microbiol.* 2010;8(1):26-38. [doi:10.1038/nrmicro2265](https://doi.org/10.1038/nrmicro2265) · [PubMed 19966814](https://pubmed.ncbi.nlm.nih.gov/19966814/)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
