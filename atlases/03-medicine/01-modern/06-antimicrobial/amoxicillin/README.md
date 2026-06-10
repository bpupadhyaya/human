---
schema: medicine-entry/v1
id: amoxicillin
name: Amoxicillin
atlas: 03-medicine
scale: 01-modern
status: draft
last_reviewed: 2026-06-06
summary: "Aminopenicillin beta-lactam antibiotic; binds PBPs (penicillin-binding proteins) → inhibits peptidoglycan cross-linking → cell lysis. Broad gram-positive + selected gram-negative coverage. Most widely prescribed antibiotic globally. WHO Access group antibiotic."
aliases: ["amoxicillin", "amoxycillin", "Amoxil", "Trimox", "Moxatag", "Augmentin (with clavulanate)", "(2S,5R,6R)-6-[(R)-2-amino-2-(4-hydroxyphenyl)acetamido]-3,3-dimethyl-7-oxo-4-thia-1-azabicyclo[3.2.0]heptane-2-carboxylic acid"]
sources:
  - id: rolinson-1998-penicillins-history
    type: peer-reviewed
    cite: "Rolinson GN. Forty years of beta-lactam research. J Antimicrob Chemother. 1998;41(6):589-603."
    doi: "10.1093/jac/41.6.589"
    pmid: "9687086"
    url: "https://doi.org/10.1093/jac/41.6.589"
  - id: finch-2007-amoxicillin-clinical
    type: peer-reviewed
    cite: "Finch RG, Greenwood D, Whitley RJ, Norrby SR, eds. Antibiotic and Chemotherapy, 8th ed. Churchill Livingstone, 2010. Chapter: Aminopenicillins."
    url: "https://www.ncbi.nlm.nih.gov/books/NBK526128/"
  - id: who-awre-2019
    type: clinical-guideline
    cite: "WHO. Critically important antimicrobials for human medicine, 6th revision. 2019. World Health Organization, Geneva."
    url: "https://www.who.int/publications/i/item/critically-important-antimicrobials-for-human-medicine"
    accessed: "2026-06-06"
  - id: lode-2009-amoxicillin-cap
    type: peer-reviewed
    cite: "Lode H. Safety and tolerability of commonly prescribed oral antibiotics for the treatment of respiratory tract infections. Am J Med. 2010;123(4 Suppl):S26-38."
    doi: "10.1016/j.amjmed.2010.02.004"
    pmid: "20350720"
    url: "https://doi.org/10.1016/j.amjmed.2010.02.004"
cross_links:
  - target: 02-pathogen/02-bacteria/streptococcus-pneumoniae
    relation: treats
    note: "S. pneumoniae is the primary target for amoxicillin in community-acquired pneumonia; high-dose amoxicillin (3g/day) overcomes intermediate-level penicillin resistance via PBP2b affinity changes (MIC ≤2 mg/L)."
  - target: 02-pathogen/02-bacteria/helicobacter-pylori
    relation: treats
    note: "Core component of H. pylori triple therapy (PPI + clarithromycin + amoxicillin 1g BD × 14 days); targets H. pylori PBPs; clarithromycin resistance ~20–30% in Europe drives bismuth quadruple therapy preference."
  - target: 02-pathogen/02-bacteria/clostridioides-difficile
    relation: connects-to
    note: "Amoxicillin is a common precipitant of C. diff colitis via disruption of colonization resistance; risk lower than fluoroquinolones or clindamycin; patients on amoxicillin >7 days have ~3-fold increased C. diff risk."
  - target: 01-human/07-system/gut-microbiome
    relation: modulates
    note: "Amoxicillin reduces gram-positive and gram-negative gut microbiota diversity; Enterobacteriaceae bloom during treatment; microbiome recovery takes 1–2 months post-course; repeated courses associate with persistent dysbiosis."
---

# Amoxicillin

## Overview

**Amoxicillin** (Amoxil) is an **aminopenicillin** — a semi-synthetic penicillin developed in 1972 by Beecham Pharmaceuticals — and is the **most widely prescribed antibiotic in the world**. It is a bactericidal beta-lactam antibiotic with broader spectrum than benzylpenicillin (penicillin G) due to its 4'-hydroxyphenyl side chain, which improves penetration through gram-negative outer membranes. It retains excellent activity against gram-positive organisms and extends coverage to key gram-negative pathogens including *H. influenzae* and *H. pylori*.

The WHO lists amoxicillin as an **Access group antibiotic** — first-line for common infections with low resistance risk — on the Essential Medicines List. Combined with the beta-lactamase inhibitor **clavulanate** (co-amoxiclav, Augmentin), it extends coverage to beta-lactamase-producing organisms.

## Mechanism

**Beta-lactam mechanism — PBP inhibition:**
1. **Beta-lactam ring:** The four-membered lactam ring (β-lactam) is the pharmacophore; it is a structural analogue of the D-Ala-D-Ala terminus of the peptidoglycan pentapeptide stem
2. **PBP binding:** Amoxicillin enters the bacterial periplasm (outer membrane pores in gram-negatives; direct access in gram-positives) and binds the **penicillin-binding proteins (PBPs)** — serine transpeptidases that catalyze the final cross-linking step of peptidoglycan synthesis (DD-transpeptidase reaction)
3. **Acylation:** The beta-lactam ring opens nucleophilically, acylating the catalytic serine residue of PBP → stable acyl-enzyme complex → PBP permanently inactivated (covalent, irreversible under physiological conditions)
4. **Loss of peptidoglycan integrity:** Cross-linking of peptidoglycan strands ceases; the cell wall becomes thin and structurally defective; the bacteria cannot maintain osmotic integrity → **osmotic lysis** (bactericidal)
5. **Autolysis activation:** Release of murein hydrolases (autolysins) from cell membrane contributes to lysis in many species [^rolinson-1998-penicillins-history]

**Spectrum of activity:**
- **Gram-positive:** *Streptococcus pyogenes* (Group A Strep), *S. pneumoniae* (most strains), *Streptococcus agalactiae*, *Enterococcus faecalis*, *Listeria monocytogenes*
- **Gram-negative (selected):** *Haemophilus influenzae* (non-beta-lactamase-producing), *Escherichia coli* (community strains, increasingly resistant), *Helicobacter pylori*, *Neisseria gonorrhoeae* (resistance common)
- **Not covered:** *Staphylococcus aureus* (MSSA or MRSA — penicillinase or PBP2a), *Pseudomonas aeruginosa*, *Klebsiella*, *Enterobacteriaceae* producing ESBL, anaerobes (variable)

**Resistance mechanisms:**
1. **Beta-lactamase production:** Most common; beta-lactamase cleaves the C-N bond of the beta-lactam ring → inactive amoxicilloic acid; clavulanate is a suicide inhibitor of beta-lactamases → co-amoxiclav restores activity
2. **PBP modification:** *S. pneumoniae* with altered PBP2b/PBP2x (mosaic genes from viridans streptococci) → reduced affinity for amoxicillin; high-dose amoxicillin overcomes intermediate-level resistance (MIC ≤2 mg/L)
3. **MRSA — PBP2a:** mecA-encoded PBP2a has minimal affinity for all beta-lactams → intrinsic resistance; amoxicillin inactive against MRSA

**Pharmacokinetics:**
- Oral bioavailability: ~80–90% (superior to ampicillin ~40%)
- Food: absorption not significantly affected
- Half-life: ~1 h; renal elimination (60–70% unchanged)
- Distributes widely into most tissues; poor CNS penetration unless meninges inflamed
- Dose-adjustment required for eGFR <30 mL/min

## Clinical Use

**Community-acquired pneumonia (CAP):**
- First-line for mild-moderate CAP (presumed S. pneumoniae): amoxicillin 500 mg–1 g TDS × 5–7 days
- High-dose amoxicillin (3 g/day in divided doses) for intermediate-resistance pneumococci; covers MIC up to 2 mg/L [^lode-2009-amoxicillin-cap]

**Streptococcal pharyngitis (Group A Strep):**
- 500 mg BD × 10 days; prevents rheumatic fever; equivalent efficacy to penicillin V with better palatability (and once-daily dosing feasible)

**Acute otitis media:**
- First-line in children: 40–45 mg/kg/day in divided doses × 5–10 days
- High-dose (80–90 mg/kg/day) for suspected penicillin-resistant pneumococci or treatment failure

**H. pylori eradication:**
- Component of triple therapy (PPI + clarithromycin + amoxicillin × 14 days) [WHO Maastricht VI]
- Also used in quadruple therapy

**Urinary tract infections:**
- Community E. coli: decreasing susceptibility (resistance 20–50% in many regions); trimethoprim or nitrofurantoin preferred empirically; amoxicillin for confirmed susceptible isolates

**Allergy and cross-reactivity:**
- Penicillin allergy reported in ~10% of patients; true IgE-mediated allergy ~1%; cross-reactivity with cephalosporins ~1–2% (mostly R1 side-chain dependent)
- Anaphylaxis: 1–4 per 10,000 courses; most life-threatening reactions occur in first 30 minutes (IV) or 1–2 h (oral)
- **Ampicillin/amoxicillin rash:** Non-allergic, maculopapular rash in ~5% of patients (80–100% in EBV infectious mononucleosis — do not indicate allergy)

**Adverse effects:**
- GI (most common): nausea, diarrhea, abdominal discomfort (less with amoxicillin vs ampicillin)
- *Clostridioides difficile* infection (risk with any antibiotic; amoxicillin lower risk than fluoroquinolones or clindamycin)
- Rash (5%), urticaria (1%)

## Evidence

| Study / Guideline | Key Finding |
|:---|:---|
| WHO AWaRe classification (2019) [^who-awre-2019] | Amoxicillin classified as Access antibiotic — first-line for common infections; guidance to limit broader-spectrum agents |
| CAP guidelines (BTS, IDSA/ATS) | Amoxicillin first-line oral agent for mild-moderate CAP in non-severe patients without atypical features or risk factors for resistant organisms |
| Meta-analysis pharyngitis | Amoxicillin equivalent to penicillin V for streptococcal pharyngitis; superior compliance |
| Amoxicillin vs placebo (otitis media) | NNT ~7–14 for resolution at 24h; NNT ~20 for prevention of tympanic membrane perforation; watchful waiting appropriate in mild disease (age >2 years) |

## Connections

- **Targets** → [Peptidoglycan / PBPs](../../../../../01-human/03-molecular/peptidoglycan/README.md): Covalent acylation of PBP catalytic serine → DD-transpeptidase inactivation → peptidoglycan cross-linking failure → osmotic lysis.
- **Treats** → [S. pneumoniae](../../../../../02-pathogen/02-bacteria/streptococcus-pneumoniae/README.md): Primary clinical target in CAP, AOM, and sinusitis; high-dose amoxicillin overcomes intermediate resistance via PBP affinity changes.
- **Treats** → [Helicobacter pylori](../../../../../02-pathogen/02-bacteria/helicobacter-pylori/README.md): Core component of triple therapy (PPI + clarithromycin + amoxicillin × 14 days); targets H. pylori PBPs; clarithromycin resistance drives bismuth quadruple therapy preference.
- **Connects-to** → [Clostridioides difficile](../../../../../02-pathogen/02-bacteria/clostridioides-difficile/README.md): Common precipitant of C. diff colitis via disruption of colonization resistance; risk lower than fluoroquinolones or clindamycin; >7-day courses carry ~3-fold increased C. diff risk.
- **Modulates** → [Gut Microbiome](../../../../../01-human/07-system/gut-microbiome/README.md): Reduces gram-positive and gram-negative gut microbiota diversity; Enterobacteriaceae bloom during treatment; microbiome recovery takes 1–2 months; repeated courses associate with persistent dysbiosis.

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
