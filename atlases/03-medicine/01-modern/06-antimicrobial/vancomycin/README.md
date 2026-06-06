---
schema: medicine-entry/v1
id: vancomycin
name: Vancomycin
atlas: 03-medicine
scale: 01-modern
status: draft
last_reviewed: 2026-06-06
summary: "Glycopeptide antibiotic; binds D-Ala-D-Ala terminus of peptidoglycan precursors → steric inhibition of cell wall synthesis. Essential for MRSA, VRE (with D-Ala-D-Lac resistance), and severe gram-positive infections. First-line IV MRSA bacteremia. 1952 discovery."
aliases: ["vancomycin", "Vancocin", "vancomycin hydrochloride", "vancomycin HCl"]
sources:
  - id: mccormick-1956-vancomycin
    type: peer-reviewed
    cite: "McCormick MH, Stark WM, Pittenger GE, Pittenger RC, McGuire JM. Vancomycin, a new antibiotic. I. Chemical and biologic properties. Antibiot Annu. 1956;3:606-11."
    pmid: "13425756"
    url: "https://pubmed.ncbi.nlm.nih.gov/13425756/"
  - id: liu-2011-mrsa-guidelines
    type: clinical-guideline
    cite: "Liu C, Bayer A, Cosgrove SE, et al. Clinical practice guidelines by the Infectious Diseases Society of America for the treatment of methicillin-resistant Staphylococcus aureus infections in adults and children. Clin Infect Dis. 2011;52(3):e18-55."
    doi: "10.1093/cid/ciq146"
    pmid: "21208910"
    url: "https://doi.org/10.1093/cid/ciq146"
  - id: arthur-1996-vancomycin-resistance
    type: peer-reviewed
    cite: "Arthur M, Courvalin P. Genetics and mechanisms of glycopeptide resistance in enterococci. Antimicrob Agents Chemother. 1993;37(8):1563-71."
    doi: "10.1128/AAC.37.8.1563"
    pmid: "8215264"
    url: "https://doi.org/10.1128/AAC.37.8.1563"
  - id: rybak-2020-vancomycin-trough
    type: clinical-guideline
    cite: "Rybak MJ, Le J, Lodise TP, et al. Therapeutic monitoring of vancomycin for serious methicillin-resistant Staphylococcus aureus infections: A revised consensus guideline and review by the American Society of Health-System Pharmacists, the Infectious Diseases Society of America, and the Society of Infectious Diseases Pharmacists. Am J Health Syst Pharm. 2020;77(11):835-864."
    doi: "10.1093/ajhp/zxaa036"
    pmid: "32191793"
    url: "https://doi.org/10.1093/ajhp/zxaa036"
cross_links:
  - target: 02-pathogen/02-bacteria/staphylococcus-aureus
    relation: treats
    evidence: liu-2011-mrsa-guidelines
    note: "MRSA (methicillin-resistant Staphylococcus aureus) expresses PBP2a (mecA gene) that is resistant to all beta-lactams; vancomycin remains first-line IV therapy for MRSA bacteremia, endocarditis, and pneumonia per IDSA guidelines."
---

# Vancomycin

## Overview

**Vancomycin** (Vancocin) is a **glycopeptide antibiotic** isolated in 1952 from *Amycolatopsis orientalis* (then called *Streptomyces orientalis*) by scientists at Eli Lilly, found in soil samples from Borneo. Named for its ability to "vanquish" difficult organisms, it was introduced clinically in 1958. Though initially supplanted by penicillinase-resistant penicillins, it became critically important with the emergence of **MRSA** (methicillin-resistant *S. aureus*) and **enterococcal** infections in the 1980s, and remains a WHO Essential Medicine and backbone of treatment for serious gram-positive infections [^mccormick-1956-vancomycin].

Its mechanism — binding the **D-Ala-D-Ala terminus of peptidoglycan precursors** — is structurally distinct from beta-lactams, explaining why it retains activity against beta-lactam-resistant organisms. The emergence of **vancomycin-resistant enterococci (VRE)** via D-Ala-D-Lac substitution (VanA/VanB operons) represents one of the major antibiotic resistance challenges of the late 20th–21st century.

## Mechanism

**Cell wall synthesis — glycopeptide target:**
1. **Peptidoglycan synthesis pathway:** Bacterial cell wall synthesis proceeds through several steps:
   - Cytoplasmic: synthesis of UDP-MurNAc-pentapeptide (with D-Ala-D-Ala terminus)
   - Membrane: attachment to undecaprenyl phosphate lipid carrier (lipid I → lipid II via MurG)
   - **Extracellular (periplasmic):** Lipid II flips to outer leaflet; the **D-Ala-D-Ala terminus is exposed** for transglycosylation (polymerization of glycan chains) and transpeptidation (cross-linking of peptide stems)

2. **Vancomycin binding:** Vancomycin is a rigid, tricyclic glycopeptide (MW 1449 Da) that forms a **5-hydrogen bond clamp** around the D-Ala-D-Ala dipeptide C-terminus of lipid II and nascent peptidoglycan — a highly specific, high-affinity interaction (Ka ~10⁶ M⁻¹)

3. **Steric blockade:** The vancomycin-D-Ala-D-Ala complex physically blocks:
   - **Transglycosylases:** Cannot elongate glycan chains (polymerization of lipid II into peptidoglycan)
   - **Transpeptidases (PBPs):** Cannot access D-Ala-D-Ala for cross-linking; unlike beta-lactams, vancomycin doesn't bind PBPs directly — it sequesters their substrate

4. **Bactericidal:** Inhibition of both transglycosylation and transpeptidation → cell wall defects → osmotic lysis; bactericidal against most gram-positives at therapeutic concentrations

**Why vancomycin is inactive against gram-negative bacteria:**
- Vancomycin cannot penetrate the gram-negative outer membrane (too large, hydrophilic at MW 1449 Da); only effective where D-Ala-D-Ala is accessible from the external environment → gram-positive organisms and *Clostridium* (oral vancomycin for C. diff, as it doesn't need to penetrate)

**Vancomycin resistance mechanisms:**
1. **VanA resistance (VRE):** VanH (reductase) + VanA (ligase) convert D-Ala-D-Ala → **D-Ala-D-Lac** (D-lactate replaces D-alanine); loss of one H-bond reduces vancomycin binding affinity 1000×; VanX dipeptidase eliminates remaining D-Ala-D-Ala; VanY carboxypeptidase removes terminal D-Ala from any remaining precursors → MIC >256 μg/mL [^arthur-1996-vancomycin-resistance]
2. **VanB resistance:** Similar mechanism but inducible; resistant to vancomycin but susceptible to teicoplanin (different inducibility)
3. **VISA (vancomycin-intermediate S. aureus, MIC 4–8 μg/mL):** Thickened cell wall (increased peptidoglycan synthesis) traps vancomycin in outer layers; requires AUC/MIC-guided dosing
4. **VRSA (vancomycin-resistant S. aureus, MIC ≥16):** VanA operon transfer from VRE → S. aureus; rare but clinically devastating

**Pharmacokinetics:**
- Route: IV (for systemic infections); PO (only for *C. difficile* — not absorbed, acts intraluminally)
- Distribution: Vd ~0.4–1.0 L/kg; good tissue penetration (bone, endocardium, lung with inflamed barriers)
- Half-life: ~4–8 h in normal renal function; substantially prolonged in renal impairment
- **Renal elimination: >90% unchanged** — major dose adjustments required for CKD; requires TDM

**Therapeutic drug monitoring (TDM):**
- 2020 ASHP/IDSA guidelines: **AUC/MIC-guided monitoring** replaces trough-only monitoring [^rybak-2020-vancomycin-trough]
- Target: AUC₀₋₂₄/MIC 400–600 mg·h/L (for MIC ≤1 μg/mL) for serious infections
- Trough alone (target 15–20 mg/L) associated with nephrotoxicity without superior efficacy
- Continuous infusion protocols increasingly used (target steady-state 20–25 mg/L)

## Clinical Use

**MRSA infections — IV vancomycin:**
- **Bacteremia/endocarditis:** First-line per IDSA MRSA guidelines [^liu-2011-mrsa-guidelines]; 15–20 mg/kg q8–12h (AUC-guided); consider adjunctive rifampicin for prosthetic valve endocarditis
- **Pneumonia:** Less effective than daptomycin for lung (surfactant inactivates daptomycin though, so vancomycin remains preferred despite suboptimal lung penetration); linezolid superior for MRSA VAP (higher lung tissue levels)
- **Meningitis:** Vancomycin + ceftriaxone empirically for suspected bacterial meningitis (covers penicillin-resistant pneumococcus + gram-negatives); penetrates inflamed meninges

**C. difficile infection (CDI):**
- **Oral vancomycin** 125 mg QDS × 10 days: equivalent to fidaxomicin for non-hypervirulent strains; preferred over metronidazole for moderate-severe CDI
- Not absorbed — acts entirely within gut lumen; no systemic effects

**Surgical prophylaxis (MRSA colonized patients):**
- Single IV dose before cardiac surgery, joint replacement; replaces cefazolin in MRSA carriers

**Dose calculation and renal adjustment:**
- Loading dose 25–30 mg/kg IV (for severe infections) to rapidly achieve therapeutic levels
- Maintenance: 15–20 mg/kg q8–12h, adjusted for renal function (AUC-guided)
- Hemodialysis: supplemental dosing post-dialysis; significant clearance

**Adverse effects:**
- **Nephrotoxicity (most important):** ~10–15% incidence; risk increases with: prolonged treatment, high trough levels, concurrent nephrotoxins (aminoglycosides, NSAIDs, contrast); AUC-guided dosing reduces nephrotoxicity vs trough-guided
- **Red man syndrome:** Infusion-related reaction (not allergy) — histamine release from mast cells → flushing, erythema, pruritus, hypotension of face/neck/chest; caused by rapid infusion rate; prevent with slow infusion (>60 min for 1g) and pre-medication with antihistamines; not a contraindication to continued vancomycin use
- **Ototoxicity:** Cochlear/vestibular; rare at therapeutic concentrations; risk with high levels and concurrent loop diuretics; cochlear toxicity manifests as sensorineural hearing loss
- **Thrombophlebitis:** Peripheral IV administration causes inflammation; use central line for prolonged courses

## Evidence

| Study / Guideline | Key Finding |
|:---|:---|
| IDSA MRSA Guidelines (Liu 2011) [^liu-2011-mrsa-guidelines] | Vancomycin first-line for MRSA bacteremia, endocarditis, skin/soft tissue infections, pneumonia, and meningitis; daptomycin an alternative for bacteremia/right-sided endocarditis |
| 2020 ASHP/IDSA TDM Consensus (Rybak 2020) [^rybak-2020-vancomycin-trough] | AUC/MIC 400–600 mg·h/L target superior to trough-only monitoring; reduces nephrotoxicity without compromising efficacy |
| Resistance mechanism (Arthur 1993) [^arthur-1996-vancomycin-resistance] | VanA operon (vanH/vanA/vanX/vanY/vanZ) characterized — D-Ala-D-Lac substitution reducing vancomycin affinity 1000-fold; provided framework for understanding all glycopeptide resistance |
| CDI meta-analyses | Oral vancomycin 125 mg QDS: superior to metronidazole for severe CDI; similar outcomes to fidaxomicin; fidaxomicin superior for recurrence prevention (non-hypervirulent strains) |

## Connections

- **Targets** → [Peptidoglycan](../../../../../01-human/03-molecular/peptidoglycan/README.md): 5-H-bond clamp on D-Ala-D-Ala terminus of lipid II → physical blockade of transglycosylation and transpeptidation; too large for PBP mutations to overcome — hence active against MRSA.
- **Treats** → [MRSA / S. aureus](../../../../../01-human/02-microbial/staphylococcus-aureus/README.md): First-line IV treatment for MRSA bacteremia, endocarditis, and CNS infections; the mecA-encoded PBP2a that renders S. aureus resistant to all beta-lactams does not affect vancomycin's mechanism.
