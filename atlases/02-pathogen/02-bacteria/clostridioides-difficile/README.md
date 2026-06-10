---
schema: pathogen-entry/v1
id: clostridioides-difficile
name: Clostridioides difficile
atlas: 02-pathogen
scale: 02-bacteria
status: draft
last_reviewed: 2026-06-05
summary: "Gram-positive anaerobic spore-forming rod; reclassified from Clostridium in 2016. Causes antibiotic-associated colitis via TcdA/TcdB glucosyltransferase toxins and binary toxin (CDT). NAP1/027 hypervirulent ribotype; FMT ~90% effective for recurrent CDI."
aliases: ["C. difficile", "C. diff", "Clostridium difficile", "CDI", "CDAD", "NAP1/027 strain"]
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
  - target: 01-human/05-tissue/intestinal-epithelium
    relation: infects
    note: "TcdA and TcdB bind colonocyte receptors (FZD/PVRL3 for TcdB) → Rho GTPase glucosylation → tight junction disruption, cytoskeletal collapse, colonocyte apoptosis → epithelial barrier failure → diarrhoea and pseudomembranous colitis."
  - target: 01-human/07-system/digestive-system
    relation: damages
    note: "C. difficile overgrows after antibiotic-induced microbiome disruption; TcdA/B destroy colonic epithelium → pseudomembranous colitis (yellow-white plaques), toxic megacolon, perforation; NAP1/027 (↑toxin output) → ↑mortality and recurrence."
  - target: 01-human/07-system/immune-system
    relation: damages
    note: "Colonisation resistance (commensal microbiome competition) is the primary defence; antibiotic exposure depletes this defence. Spores survive alcohol hand gel. Anti-TcdA/TcdB serum IgG correlates with protection against recurrent CDI."
  - target: 01-human/04-cellular/neutrophil
    relation: damages
    note: "TcdA stimulates IL-8/CXCL8 from colonocytes and macrophages → intense neutrophilic mucosal infiltration (acute-phase response); CDT binary toxin promotes neutrophil evasion by inducing microtubule-dependent actin protrusions on bacterial surface."
  - target: 03-medicine/01-modern/08-gi/omeprazole
    relation: connects-to
    note: "PPIs (omeprazole) are a C. diff risk factor (OR ~1.7×): suppressed gastric acid → C. diff spores survive stomach transit and germinate in small bowel; meta-analyses confirm PPI-C. diff association in hospitals; dose-dependent; consider PPI deprescription in low-risk patients."
  - target: 03-medicine/01-modern/06-antimicrobial/vancomycin
    relation: treated-by
    note: "Oral vancomycin 125 mg QDS × 10 days is first-line for severe/severe-complicated C. diff (IDSA 2021); fidaxomicin preferred for recurrence; IV vancomycin does NOT reach colon — oral route only; oral vancomycin disrupts gut anaerobes and increases VRE colonization risk."
  - target: 03-medicine/01-modern/06-antimicrobial/amoxicillin
    relation: connects-to
    note: "Amoxicillin is a common precipitant of C. diff colitis via disruption of colonization resistance; risk lower than fluoroquinolones or clindamycin; patients on amoxicillin >7 days have ~3-fold increased C. diff risk."
  - target: 02-pathogen/06-microbiome/lactobacillus-rhamnosus
    relation: modulated-by
    note: "L. rhamnosus GG (LGG) competes with C. difficile for intestinal mucin-binding sites via SpaCBA pili, acidifies the lumen via lactic acid, and prevents antibiotic-associated C. difficile colonisation and diarrhoea (NNT ~7 for AAD prevention)."
---

# Clostridioides difficile

## Overview

*Clostridioides difficile* (C. diff; formerly *Clostridium difficile*, reclassified 2016 based on 16S rRNA phylogeny) is a **Gram-positive, obligate anaerobic, spore-forming rod** and the **most common cause of healthcare-associated infectious diarrhoea** in high-income countries [^mandell-principles]. It causes approximately **500,000 infections and 30,000 deaths per year in the United States alone**, with a global burden estimated at several million cases annually.

The defining epidemiological characteristic is the organism's **spore biology**: endospores are:
- Resistant to alcohol-based hand gels (the dominant hand hygiene agent in healthcare) — necessitating soap-and-water handwashing for physical spore removal
- Resistant to heat and many common disinfectants
- Capable of surviving on environmental surfaces (bedrails, commodes, medical equipment) for **months**
- Not killed by gastric acid → readily establish colonisation after oral ingestion

The disease — **Clostridioides difficile infection (CDI)** — arises almost exclusively in the context of **antibiotic-disrupted colonic microbiota**, which collapses the colonisation resistance provided by the normal gut flora.

## Structure

### Morphology and Growth

| Feature | Detail |
|:---|:---|
| **Shape** | Straight to slightly curved rod, 3–5 µm × 0.5 µm |
| **Gram stain** | Gram-positive (variable in older cultures; may appear Gram-variable) |
| **Oxygen requirement** | Obligate anaerobe (cannot survive aerobic conditions beyond spore form) |
| **Spores** | Oval, subterminal; extraordinarily environmentally resistant; not killed by alcohol gel |
| **Colony morphology** | White/off-white, irregular ("ground glass"); characteristic **horse-manure odour** (p-cresol production) on CCFA agar |
| **Motility** | Peritrichous flagella → motile in reduced media |

### Genome and Pathogenicity Locus

The **PaLoc (pathogenicity locus)** — a 19.6-kb genomic island — is the primary determinant of virulence:

| Gene | Product | Function |
|:---|:---|:---|
| **tcdA** | Toxin A (TcdA; 309 kDa) | Glucosyltransferase; enterotoxin; ↑inflammation |
| **tcdB** | Toxin B (TcdB; 270 kDa) | Glucosyltransferase; cytotoxin; primary driver of CDI |
| **tcdE** | TcdE holin-like protein | Facilitates toxin release from bacterial cell |
| **tcdR** | Sigma factor σ^TcdR | Positive regulator of tcdA and tcdB transcription |
| **tcdC** | TcdC (anti-sigma) | **Negative regulator** of toxin production; mutated/deleted in hypervirulent NAP1/027 strains → loss of negative regulation → ↑toxin output |

Strains lacking PaLoc are **non-toxigenic** and non-pathogenic (some used in biotherapy: VP20621).

**Binary toxin (CDT/CdtAB):** Present only in hypervirulent strains (NAP1/B1/027, ribotype 078):
- CdtA: ADP-ribosyltransferase → ADP-ribosylates actin → G-actin sequestration → F-actin depolymerisation
- CdtB: Binding component (binds LSR receptor on colonocytes)
- Effect: Actin disruption induces **microtubule-dependent protrusions** from the bacterial surface → ↑bacterial adhesion to colonocyte surface → ↑colonisation → ↑virulence

## Infection Mechanism

### The Antibiotic–CDI Cascade

CDI follows a predictable sequence [^mandell-principles]:

```
Antibiotic exposure
    ↓ (days to weeks)
Disruption of colonic microbiome ("dysbiosis")
    ↓
↓ Colonisation resistance (↓Bacteroidetes, ↓Lachnospiraceae, ↓bile acid secondary metabolism)
    ↓
C. difficile spore ingestion (environmental — hands, surfaces, or commensal overgrowth)
    ↓
Spore germination in colon (triggered by bile acids — taurocholate; disrupted in dysbiosis)
    ↓
Vegetative cell colonisation and toxin production
    ↓
TcdA/TcdB-mediated epithelial damage → CDI
```

**Antibiotics with highest CDI risk** (in descending order): clindamycin > fluoroquinolones (especially ciprofloxacin, moxifloxacin) > 3rd-generation cephalosporins > broad-spectrum penicillins (amoxicillin-clavulanate) > carbapenems. Even single perioperative doses of antibiotics can precipitate CDI in susceptible hosts.

**Other risk factors:** Age >65 years, hospitalisation/LTCF residence, PPI use (↓gastric acid barrier), immunosuppression (↓anti-toxin IgG), prior CDI (↑risk of recurrence), IBD, renal failure.

### Toxin Mechanism — Rho GTPase Glucosylation

**TcdA and TcdB** share the same molecular mechanism [^murray-microbiology]:

1. **Receptor binding:** TcdA binds carbohydrate receptors on colonocytes; TcdB binds Frizzled (FZD1,2,7), PVRL3 (nectin-3), and CSPG4 — explaining higher potency (10–1,000× TcdA) in human colonic epithelium
2. **Endocytosis:** Receptor-mediated → late endosome
3. **Pore formation:** Acidic endosome pH → hydrophobic loop insertion → pore → translocation of N-terminal glucosyltransferase domain into cytosol
4. **Rho GTPase glucosylation:** Transfers **UDP-glucose** onto **Thr37 of RhoA** (and Thr35 of Rac1, Cdc42) — mono-O-glucosylation → steric blockade of GEF (guanine exchange factor) binding → Rho GTPase locked in GDP-bound (inactive) state
5. **Cytoskeletal consequence:** ↓Active Rho → F-actin depolymerisation → cell rounding, stress fibre loss, tight junction breakdown, apoptosis → epithelial barrier failure

**TcdB** additionally activates the Pyrin inflammasome (via RHOA glucosylation → Pyrin de-repression → IL-1β/IL-18 maturation) — contributing to the intense mucosal inflammatory response.

## Host Interactions

### Colonisation Resistance — the Microbiome as Immune Effector

The healthy colonic microbiome provides multi-layered protection against C. difficile colonisation [^mandell-principles]:

| Mechanism | Detail |
|:---|:---|
| **Nutrient competition** | Commensal bacteria consume available carbohydrates and amino acids, limiting C. difficile growth |
| **Secondary bile acids** | *Clostridium scindens* and related Lachnospiraceae convert primary (taurocholate — stimulates spore germination) → secondary bile acids (deoxycholate, lithocholate — inhibit vegetative growth) |
| **Short-chain fatty acids (SCFAs)** | Butyrate, propionate, acetate → ↓colonic pH → ↓C. difficile colonisation; butyrate maintains colonocyte tight junctions |
| **Bacteriocins** | Commensal species produce antimicrobial peptides directly toxic to C. difficile |
| **IgA** | Secretory IgA against C. difficile colonisation factors from prior exposure |

Systemic **anti-TcdA/TcdB IgG** correlates strongly with protection against symptomatic CDI and recurrence — the rationale for bezlotoxumab (anti-TcdB monoclonal antibody) and vaccine development.

### Inflammation and Pseudomembrane Formation

TcdA is the primary driver of mucosal inflammation:
- Activates colonocyte NF-κB → IL-8 (CXCL8), IL-6, IL-1β production
- IL-8 recruits massive neutrophilic infiltration into the mucosa
- Neutrophil-derived MPO/ROS, combined with toxin-mediated apoptosis → mucosal necrosis
- Fibrin, mucus, dead neutrophils, and necrotic cells accumulate on the mucosal surface → **pseudomembranes** (2–10 mm yellow-white plaques seen on colonoscopy)

## Connections

- **Infects** → [Intestinal epithelium](../../../01-human/05-tissue/intestinal-epithelium/README.md): TcdA and TcdB bind colonocyte surface receptors (FZD1/2/7 and PVRL3 for TcdB) → glucosylate Rho GTPases (Thr37) → actin depolymerisation, tight junction breakdown, and colonocyte apoptosis → epithelial barrier failure driving diarrhoea and pseudomembranous colitis [^mandell-principles].
- **Damages** → [Digestive system](../../../01-human/07-system/digestive-system/README.md): C. difficile overgrows in antibiotic-disrupted microbiome with collapsed colonisation resistance. TcdA/B produce pseudomembranous colitis (yellow-white mucosal plaques on colonoscopy); severe disease → toxic megacolon, perforation, death. NAP1/027 hypervirulent ribotype (↑toxin, binary toxin CDT) → ↑mortality and recurrence [^mandell-principles].
- **Damages** → [Immune system](../../../01-human/07-system/immune-system/README.md): Colonisation resistance (commensal microbiome competition) is the primary host defence; antibiotic exposure destroys this defence. Spores survive alcohol-based hand gels (unique among common nosocomial pathogens). Serum anti-TcdA/TcdB IgG titres correlate with protection against CDI; low IgG predicts recurrence risk [^murray-microbiology].
- **Damages** → [Neutrophil](../../../01-human/04-cellular/neutrophil/README.md): TcdA stimulates colonocyte and macrophage IL-8/CXCL8 production → intense neutrophilic mucosal infiltration (the dominant acute-phase histological finding). Binary toxin CDT promotes neutrophil evasion via microtubule-dependent actin protrusions that enhance bacterial adhesion despite neutrophil presence [^murray-microbiology].
- **Connects-to** → [Omeprazole](../../../03-medicine/01-modern/08-gi/omeprazole/README.md): PPIs are a C. diff risk factor (OR ~1.7×): suppressed gastric acid → C. diff spores survive stomach transit and germinate in small bowel; meta-analyses confirm PPI-C. diff association in hospitals; dose-dependent; consider PPI deprescription in low-risk patients.
- **Treated-by** → [Vancomycin](../../../03-medicine/01-modern/06-antimicrobial/vancomycin/README.md): Oral vancomycin 125 mg QDS × 10 days is first-line for severe/severe-complicated C. diff (IDSA 2021); fidaxomicin preferred for recurrence; IV vancomycin does NOT reach colon — oral route only; oral vancomycin disrupts gut anaerobes and increases VRE colonization risk.
- **Connects-to** → [Amoxicillin](../../../03-medicine/01-modern/06-antimicrobial/amoxicillin/README.md): Amoxicillin is a common precipitant of C. diff colitis via disruption of colonization resistance; risk lower than fluoroquinolones or clindamycin; patients on amoxicillin >7 days have ~3-fold increased C. diff risk.
- `modulated-by` → **[Lactobacillus rhamnosus](../../../../02-pathogen/06-microbiome/lactobacillus-rhamnosus/README.md)** — *L. rhamnosus* GG (LGG) competes with *C. difficile* for intestinal mucin-binding sites via SpaCBA pili, acidifies the lumen via lactic acid, and prevents antibiotic-associated *C. difficile* colonisation and diarrhoea (NNT ~7 for AAD prevention).

## Pathology

### Clinical Severity Classification (IDSA/SHEA 2021)

| Category | Definition | Management |
|:---|:---|:---|
| **Asymptomatic colonisation** | PCR+ or stool GDH+, no symptoms | No treatment (risk of CDI); infection control |
| **Non-severe CDI** | Diarrhoea (≥3 loose stools/24h); WBC ≤15,000/µL; serum Cr <1.5× baseline | Fidaxomicin (preferred) or vancomycin oral × 10 days |
| **Severe CDI** | WBC >15,000/µL OR serum Cr ≥1.5× baseline | Fidaxomicin or vancomycin oral × 10 days; hospitalise |
| **Fulminant CDI** | Hypotension/shock, ileus, or megacolon | Vancomycin 500 mg PO QID + metronidazole 500 mg IV TID; surgical consult; colectomy if progressive |
| **Recurrent CDI (rCDI)** | CDI within 8 weeks of prior episode (same or different strain); 15–35% after 1st episode, ~60% after 2nd | Fidaxomicin pulse-taper or vancomycin taper; FMT for ≥2nd recurrence; bezlotoxumab adjunct; SER-109 |

### Diagnosis

| Test | Principle | Performance | Use |
|:---|:---|:---|:---|
| **PCR/NAAT (toxin gene)** | Amplifies tcdA/tcdB gene | Sensitivity >95%, Specificity >97% | Best rule-out test; may detect colonisation (not disease) — must correlate with clinical diarrhoea |
| **GDH ELISA** | Detects C. difficile glutamate dehydrogenase (all strains) | Sensitivity >90%, Specificity ~50% | Screening only; must confirm with toxin test |
| **Toxin A/B EIA** | Detects toxin protein | Sensitivity 60–75%, Specificity >95% | High specificity; misses ~25–40% of true CDI |
| **Two-step algorithm** | GDH + toxin EIA ± NAAT as tiebreaker | Best overall accuracy | Recommended by IDSA/SHEA |
| **Cell cytotoxicity assay** | Toxin-mediated cell rounding; neutralised by antitoxin | Sensitivity ~80%, Specificity >99% | Historical gold standard; impractical (24–48h, specialist lab) |
| **Colonoscopy** | Direct visualisation of pseudomembranes | Diagnostic if positive | Reserved for severe/unclear cases; biopsy for histopathology |

### Treatment Detail

**Fidaxomicin** (narrow-spectrum macrocyclic lactone):
- Inhibits bacterial RNA polymerase (different binding site to rifamycins)
- Narrow spectrum → minimal impact on Bacteroidetes (spares colonisation resistance recovery)
- ↓Spore shedding vs. vancomycin
- ~40% relative reduction in recurrence vs. vancomycin (pivotal trials); FDA-approved first and second line
- High cost limits use in many settings

**Faecal Microbiota Transplant (FMT):**
- Restores colonisation resistance via engraftment of donor microbiome
- ~85–90% cure rate for recurrent CDI
- Delivery: colonoscopy (most effective), upper GI tube, oral capsule (equivalent efficacy in trials)
- FDA-approved live biotherapeutic products (LBP): SER-109 (spore-based oral product; FDA 2023), RBX2660 (enema-based; FDA 2023)

**Bezlotoxumab:** Anti-TcdB human monoclonal antibody; given as single IV infusion concurrent with antibiotics; reduces recurrence by ~40% in high-risk patients (≥65 years, hypervirulent strain, severe CDI, prior CDI, immunosuppressed); FDA-approved 2016.

[^mandell-principles]: Bennett JE, Dolin R, Blaser MJ. *Mandell, Douglas, and Bennett's Principles and Practice of Infectious Diseases.* 9th ed. Elsevier; 2020.
[^murray-microbiology]: Murray PR, Rosenthal KS, Pfaller MA. *Medical Microbiology.* 9th ed. Elsevier; 2021.

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
