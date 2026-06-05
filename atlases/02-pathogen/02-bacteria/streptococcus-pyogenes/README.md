---
schema: pathogen-entry/v1
id: streptococcus-pyogenes
name: Streptococcus pyogenes
atlas: 02-pathogen
scale: 02-bacteria
status: draft
last_reviewed: 2026-06-05
summary: "Gram-positive, beta-haemolytic Group A Streptococcus (GAS). Causes pharyngitis, scarlet fever, and necrotising fasciitis. Superantigen exotoxins drive toxic shock; M-protein mimicry triggers rheumatic fever and post-streptococcal GN."
aliases: ["Group A Streptococcus", "GAS", "S. pyogenes", "GAS pharyngitis", "strep throat organism"]
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
    note: "GAS evades neutrophils via M protein (factor H → ↓C3b opsonisation), C5a peptidase (↓recruitment), SLO pore-forming cytolysis, and hyaluronic acid capsule (anti-phagocytic); streptodornase Sda1 dissolves neutrophil extracellular traps."
  - target: 01-human/07-system/immune-system
    relation: damages
    note: "Pyrogenic exotoxins SpeA/SpeC are superantigens crosslinking MHCII with TCR Vβ → polyclonal T cell expansion → massive TNF-α/IL-1β/IL-6 cytokine storm → Streptococcal TSS; M-protein molecular mimicry drives acute rheumatic fever carditis."
  - target: 01-human/07-system/cardiovascular-system
    relation: damages
    note: "ARF: anti-M protein Ab cross-react with cardiac myosin/tropomyosin → carditis (acute mitral regurgitation; chronic stenosis from scarring); up to 60% of ARF cases progress to chronic rheumatic heart disease — leading preventable heart disease globally."
  - target: 01-human/07-system/renal-system
    relation: damages
    note: "Post-streptococcal GN follows throat [M12] or skin [M49] GAS infection; immune complexes deposit in glomeruli → complement activation → acute nephritic syndrome; ↓C3, ↑ASO titre; self-limiting in most patients but may progress to CKD."
---

# Streptococcus pyogenes

## Overview

*Streptococcus pyogenes* — also termed **Group A Streptococcus (GAS)** — is a **Gram-positive, beta-haemolytic coccus** that forms chains and carries the **Lancefield Group A** carbohydrate antigen (N-acetylglucosamine polymer) on its cell wall [^mandell-principles]. It is an **obligate human pathogen** — humans are the only significant reservoir — and is spread predominantly via respiratory droplets (pharyngitis) and direct contact (skin infections).

GAS causes an exceptionally broad spectrum of disease, ranging from trivial (strep throat) to immediately life-threatening (necrotising fasciitis type 2, Streptococcal toxic shock syndrome), and uniquely causes **non-suppurative post-infectious autoimmune complications** — acute rheumatic fever (ARF) and post-streptococcal glomerulonephritis (PSGN) — that affect organs never directly infected by the bacterium [^mandell-principles].

**Rapid identification characteristics:**
- Beta-haemolysis (complete haemolysis — clear zone) on blood agar
- PYR (pyrrolidonyl arylamidase) **positive** — differentiates from other beta-haemolytic streptococci
- Bacitracin **sensitive** (zone of inhibition — Group A, not Group B/C/G)
- Catalase **negative** (all streptococci)

## Structure

### Cell Architecture

| Feature | Detail |
|:---|:---|
| **Shape** | Spherical cocci in chains (2 to >20 cells per chain) |
| **Gram stain** | Gram-positive (thick peptidoglycan cell wall) |
| **Haemolysis** | Beta (complete) on sheep blood agar — streptolysin S (O₂-stable) responsible for surface colonies; streptolysin O (O₂-labile) in deep subsurface |
| **Lancefield antigen** | Group A (Lancefield C carbohydrate: rhamnose-N-acetylglucosamine polymer) |
| **Capsule** | Hyaluronic acid (non-immunogenic molecular mimicry of host HA → ↓antibody recognition; antiphagocytic) |
| **Flagella** | None; non-motile |

### Major Surface and Secreted Virulence Factors

**M protein** — the defining GAS virulence factor:
- Surface-anchored fibrillar coiled-coil dimer; >250 M-types described (basis of serotyping)
- **Antiphagocytic:** M protein binds **factor H** (complement regulatory protein) → ↓C3b deposition on the bacterial surface → ↓opsonophagocytosis by neutrophils
- **Molecular mimicry:** M protein shares epitopes with cardiac myosin, tropomyosin, laminin, and collagen — the basis of **ARF pathogenesis**
- **M-type-disease associations:** M1T1 — most common GAS lineage globally, associated with pharyngitis, scarlet fever, NF, TSS; M12 — pharyngeal PSGN; M49 — skin/impetigo-associated PSGN

## Infection Mechanism

### Pharyngeal Colonisation and Invasion

Pharyngeal GAS infection (strep throat) involves:
1. **Attachment** to pharyngeal epithelium via M protein (fibronectin-binding; FBPs bind fibronectin on epithelial cells), Protein F1/SfbI (fibronectin), pili
2. **Spreading factors** degrade extracellular matrix components: hyaluronidase (degrades HA in connective tissue), streptodornase/DNases (B, C, D — degrade NETs and extracellular DNA), streptokinase (activates plasminogen → plasmin → fibrinolysis → ↑tissue invasion)
3. **C5a peptidase (ScpA):** Cleaves and inactivates the neutrophil chemoattractant C5a → ↓neutrophil influx to the infection site → immune evasion

### Toxin Production

| Toxin | Class | Mechanism | Disease relevance |
|:---|:---|:---|:---|
| **Streptolysin O (SLO)** | Cholesterol-dependent cytolysin (CDC) | Binds cholesterol in cell membranes → oligomerises → large pores (~30 nm) → cell lysis | Immunogenic → anti-SLO (ASO) titre rises; diagnostic marker for recent GAS infection (ARF workup); neutrophil lysis |
| **Streptolysin S (SLS)** | Non-protein (linked to peptide backbone); O₂-stable | Membrane-disrupting | Responsible for beta-haemolysis on surface blood agar plates; not immunogenic |
| **Pyrogenic exotoxins (Spe) A, B, C, G, H, I, J, K** | Superantigens (SpeA, SpeC, SpeG, SpeJ, SpeH, SpeK) | Crosslink **MHC class II** (on APCs) with **TCR Vβ** (on T cells) without antigen processing → polyclonal T cell activation (up to 20% of all T cells vs. <0.01% in conventional Ag response) → massive TNF-α, IL-1β, IL-6, IL-2 → cytokine storm | Streptococcal toxic shock syndrome (STSS); scarlet fever (SpeA) |
| **SpeB** | Cysteine protease | Cleaves host and bacterial surface proteins; degrades cytokines, immunoglobulins, extracellular matrix; activates IL-18 | Tissue invasion; NADase (nicotinamide adenine dinucleotidase) — co-secreted with SpeB |
| **NADase (Spn/NdaS)** | NAD⁺ glycohydrolase | Depletes intracellular NAD⁺ in invaded cells → cytotoxicity | Intracellular killing by macrophages/neutrophils ↓ |
| **Streptokinase (SK)** | Plasminogen activator | Binds plasminogen → conformational change → plasmin activity without cleavage → fibrin dissolution | Systemic spread; NF/TSS dissemination |

## Host Interactions

### Neutrophil Evasion — Multi-layered Strategy

GAS has co-evolved sophisticated mechanisms to evade the primary innate barrier [^murray-microbiology]:

1. **Complement evasion:** M protein + factor H → ↓C3b on surface; M protein also blocks C3b binding; SIC (streptococcal inhibitor of complement, M1T1 strains) inhibits MAC
2. **C5a destruction:** C5a peptidase degrades the most potent neutrophil chemoattractant → ↓neutrophil influx
3. **Capsule:** Hyaluronic acid capsule is non-immunogenic (molecular mimicry); anti-phagocytic physical barrier
4. **Pore-forming toxins:** SLO lyses neutrophils that have engulfed bacteria; also triggers NLRP3 inflammasome in surviving cells
5. **NET dissolution:** Streptodornases (DNase Sda1 in M1T1) — among the most important invasion determinants; dissolve neutrophil extracellular traps → escape entrapment

### Post-infectious Autoimmune Sequelae — Molecular Mimicry

The most distinctive feature of GAS pathogenesis is its ability to trigger **autoimmune disease in organs never infected** by the bacterium [^mandell-principles]:

**Acute Rheumatic Fever (ARF) — the M-protein mimicry paradigm:**
- GAS pharyngitis (not skin infection) triggers the immune response
- Anti-M-protein antibodies (particularly against the N-terminal hypervariable region) cross-react with:
  - **Cardiac myosin** (cross-reactive epitopes in M5, M6, M19 types especially) → myocarditis, valvulitis
  - **Tropomyosin, vimentin, laminin** → valvular endothelium targeting
  - **N-acetyl-β-D-glucosamine (valve carbohydrate)** → molecular mimicry
- **Jones criteria (2015 revision):** Major criteria = carditis, polyarthritis (migratory, large joints), Sydenham's chorea, erythema marginatum, subcutaneous nodules; Minor = fever, elevated ESR/CRP, prolonged PR interval; ≥2 major or 1 major + 2 minor + evidence of preceding GAS infection → ARF diagnosis
- **Chronic rheumatic heart disease (RHD):** Scarring from recurrent ARF episodes → mitral stenosis (most common), aortic insufficiency; globally affects ~40 million people — a major cause of preventable heart disease in LMICs

**Post-streptococcal glomerulonephritis (PSGN):**
- Follows pharyngeal GAS infection (M type 12 most common) or skin infection (M type 49 most common)
- **Mechanism:** Streptococcal antigens (SPEB/zymogen, GAPDH/SDH, plasmin receptor NaPl-1, enolase) deposited in glomeruli → in situ immune complex formation → complement activation (↓C3, normal C4 = alternative pathway) → neutrophilic glomerulonephritis
- **Clinical:** Acute nephritic syndrome (haematuria — "cola/smoky urine", proteinuria, hypertension, oliguria, oedema); ↓C3 (90%), ↑ASO titre (if pharyngeal) or ↑anti-DNase B (if skin)
- **Prognosis:** Most children recover fully; adults at ↑risk of CKD progression

## Connections

- **Infects** → [Neutrophil](../../../01-human/04-cellular/neutrophil/README.md): GAS uses M protein (factor H binding → ↓C3b opsonisation), C5a peptidase (↓neutrophil recruitment), hyaluronic acid capsule (anti-phagocytic), SLO (pore-forming cytolysis of neutrophils), and streptodornase Sda1 (dissolves neutrophil extracellular traps) to evade the primary innate cellular defence [^mandell-principles].
- **Damages** → [Immune system](../../../01-human/07-system/immune-system/README.md): Pyrogenic exotoxins SpeA and SpeC function as superantigens, crosslinking MHCII with TCR Vβ to activate up to 20% of T cells → massive cytokine storm (TNF-α, IL-1β, IL-6) → Streptococcal TSS. M-protein molecular mimicry subsequently drives ARF-associated autoimmune carditis [^mandell-principles].
- **Damages** → [Cardiovascular system](../../../01-human/07-system/cardiovascular-system/README.md): Acute rheumatic fever arises from anti-M-protein antibodies cross-reacting with cardiac myosin and tropomyosin → carditis (acute mitral regurgitation; chronic scarring → mitral stenosis and aortic insufficiency). Up to 60% of ARF episodes lead to chronic RHD — a leading preventable cause of heart disease globally [^murray-microbiology].
- **Damages** → [Renal system](../../../01-human/07-system/renal-system/README.md): PSGN follows throat (M12) or skin (M49) GAS infection. Streptococcal antigens (SPEB, enolase, NaPl-1) deposit in glomeruli → immune complex formation → alternative complement activation (↓C3, normal C4) → acute nephritic syndrome. Typically self-resolving in children; adults risk CKD [^murray-microbiology].

## Pathology

### Clinical Disease Spectrum

| Disease | Key Features | Treatment | Complication prevention |
|:---|:---|:---|:---|
| **Pharyngitis/tonsillitis** | Sore throat, fever, tonsillar exudate, anterior cervical LAD, no cough; Centor/McIsaac score; RADT | Penicillin V 10 days (or amoxicillin); azithromycin if PCN-allergic | ARF prevented if antibiotics given within 9 days of symptom onset |
| **Scarlet fever** | Pharyngitis + sandpaper erythematous rash (SpeA-driven); strawberry tongue; circumoral pallor; Pastia lines in flexures | Same as pharyngitis | — |
| **Impetigo** | Superficial skin — honey-crusted vesicular/pustular lesions; painless; GAS or S. aureus | Topical mupirocin (mild); oral amoxicillin-clavulanate (extensive) | PSGN not prevented by antibiotics (unlike ARF); watch for post-streptococcal GN 1–3 weeks later |
| **Erysipelas** | Sharply demarcated, raised, fiery-red, butterfly/facial or lower limb; fever; lymphadenopathy; GAS (not S. aureus) | IV penicillin G (or cefazolin) | — |
| **Cellulitis (GAS)** | Less sharply demarcated; deeper dermis/subcutis; systemic fever | IV penicillin G + clindamycin (to block toxin synthesis) if systemic | Distinguish from DVT, necrotising fasciitis |
| **Necrotising fasciitis type 2 (NF2)** | Rapidly progressing deep fascial plane infection; severe pain out of proportion to skin findings; "dusky" skin → bullae → necrosis; STSS in ~50% | Immediate surgical debridement + IV penicillin G + clindamycin (protein synthesis blockade stops exotoxin) | Mortality 20–30% even with surgery |
| **Streptococcal TSS (STSS)** | SpeA/SpeC superantigen → fever, hypotension, multi-organ failure, DIC; may arise from any GAS focus (often skin/soft tissue) | ICU support; IV penicillin G + clindamycin; IVIG (neutralises toxins) in severe cases | Mortality up to 30–70% in fulminant TSS |
| **Puerperal fever** | Post-partum GAS endometritis/sepsis; Semmelweis-era nosocomial epidemic; still occurs | IV penicillin G + clindamycin | Mandatory hand hygiene; household contacts may be GAS carriers |

### ARF Prevention — the Critical Window

**Penicillin treats GAS pharyngitis and, critically, prevents ARF if started within 9 days of symptom onset** — even though clinical improvement occurs earlier. This is the primary public health rationale for testing and treating strep throat in children. Penicillin/amoxicillin remain universally active against GAS (no acquired penicillin resistance documented to date).

**Long-term benzathine penicillin prophylaxis** (IM every 3–4 weeks, or oral penicillin V daily) prevents recurrent GAS pharyngitis → prevents additional ARF episodes → limits progressive valvular damage. Duration: 10+ years (or age 21) without carditis; lifelong if severe RHD.

[^mandell-principles]: Bennett JE, Dolin R, Blaser MJ. *Mandell, Douglas, and Bennett's Principles and Practice of Infectious Diseases.* 9th ed. Elsevier; 2020.
[^murray-microbiology]: Murray PR, Rosenthal KS, Pfaller MA. *Medical Microbiology.* 9th ed. Elsevier; 2021.
