---
schema: human-scale-entry/v1
id: kidney
name: Kidney
atlas: 01-human
scale: 06-organ
status: draft
last_reviewed: 2026-06-04
summary: "Paired retroperitoneal organs (~150 g each) housing ~1 million nephrons. Core functions: plasma filtration (GFR ~125 mL/min), tubular reabsorption, acid-base balance, and endocrine roles (EPO, renin, calcitriol). Central to blood pressure regulation via RAAS."
aliases: ["ren", "renal organ"]
sources:
  - id: hall-guyton-14
    type: textbook
    cite: "Hall JE. Guyton and Hall Textbook of Medical Physiology. 14th ed. Elsevier; 2021. Ch. 26-32."
    url: "https://www.elsevier.com/books/guyton-and-hall-textbook-of-medical-physiology/hall/978-0-323-59712-8"
    accessed: "2026-06-04"
  - id: levey-2003-ckd-definition
    type: peer-reviewed
    cite: "Levey AS, Coresh J, Balk E, et al. National Kidney Foundation practice guidelines for chronic kidney disease: evaluation, classification, and stratification. Ann Intern Med. 2003;139(2):137-47."
    doi: "10.7326/0003-4819-139-2-200307150-00013"
    pmid: "12859163"
    url: "https://doi.org/10.7326/0003-4819-139-2-200307150-00013"
  - id: kdigo-2012-ckd
    type: regulatory
    cite: "Kidney Disease: Improving Global Outcomes (KDIGO) CKD Work Group. KDIGO 2012 Clinical Practice Guideline for the Evaluation and Management of Chronic Kidney Disease. Kidney Int Suppl. 2013;3(1):1-150."
    url: "https://kdigo.org/guidelines/ckd-evaluation-and-management/"
    accessed: "2026-06-04"
  - id: kdigo-2012-aki
    type: regulatory
    cite: "Kidney Disease: Improving Global Outcomes (KDIGO) AKI Work Group. KDIGO Clinical Practice Guideline for Acute Kidney Injury. Kidney Int Suppl. 2012;2(1):1-138."
    url: "https://kdigo.org/guidelines/acute-kidney-injury/"
    accessed: "2026-06-04"
  - id: vanholder-2021-ckd-epidemiology
    type: peer-reviewed
    cite: "Vanholder R, Annemans L, Brown E, et al. Reducing the costs of chronic kidney disease while delivering quality health care: a call to action. Nat Rev Nephrol. 2017;13(7):393-409."
    doi: "10.1038/nrneph.2017.63"
    pmid: "28479604"
    url: "https://doi.org/10.1038/nrneph.2017.63"
cross_links:
  - target: 01-human/05-tissue/glomerulus
    relation: contains
    note: "Each kidney contains ~1 million glomeruli, the primary filtration units of the nephron."
  - target: 01-human/04-cellular/podocyte
    relation: contains
    note: "Podocytes are resident glomerular cells essential for maintaining filtration barrier integrity."
  - target: 01-human/07-system/renal-system
    relation: part-of
    note: "The kidney is the primary functional organ of the renal/urinary system."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "RAAS links renal function to systemic blood pressure; heart failure reduces renal perfusion → cardiorenal syndrome; kidneys regulate vascular volume."
  - target: 02-pathogen/01-viruses/sars-cov-2
    relation: damaged-by
    note: "COVID-19 AKI occurs in up to 30% of ICU patients via direct tubular ACE2-mediated infection, cytokine storm, thrombotic microangiopathy, and collapsing glomerulopathy."
  - target: 03-medicine/01-modern/04-cardio/ace-inhibitors
    relation: treated-by
    note: "ACE inhibitors reduce intraglomerular pressure by dilating the efferent arteriole; slow CKD progression in diabetic and non-diabetic nephropathy."
  - target: 03-medicine/01-modern/04-cardio/loop-diuretics
    relation: treated-by
    note: "Loop diuretics (e.g., furosemide) block NKCC2 in the thick ascending limb of Henle; used for fluid overload in AKI and CKD."
  - target: 01-human/03-molecular/vasopressin
    relation: modulated-by
    note: "Modulated by Vasopressin."
  - target: 01-human/03-molecular/angiotensin-ii
    relation: modulated-by
    note: "Modulated by Angiotensin II."
  - target: 01-human/03-molecular/albumin
    relation: modulated-by
    note: "Modulated by Albumin."
  - target: 01-human/03-molecular/erythropoietin
    relation: expressed-by
    note: "Expressed by Erythropoietin."
  - target: 01-human/02-atomic/chloride
    relation: modulated-by
    note: "Modulated by Chloride."
  - target: 03-medicine/03-food/vitamin-d
    relation: modulated-by
    note: "Modulated by Vitamin D (Calciferol)."
  - target: 03-medicine/02-traditional/licorice-root
    relation: modulated-by
    note: "Modulated by Licorice Root (Glycyrrhiza glabra / G. uralensis)."
  - target: 03-medicine/01-modern/06-antimicrobial/vancomycin
    relation: damaged-by
    note: "Vancomycin causes nephrotoxicity via oxidative tubular injury; AUC/MIC-guided dosing (target AUC 400–600 mg·h/L) replaces trough monitoring (2020 ASHP/IDSA consensus); risk factors: CKD, prolonged courses, NSAIDs or aminoglycoside co-administration."
  - target: 01-human/02-atomic/hydrogen
    relation: connects-to
    note: "Renal α-intercalated cells secrete H⁺ via luminal H⁺-ATPase; NHE3 in proximal tubule secretes H⁺ and reabsorbs Na⁺; kidney recovers ~4500 mmol HCO₃⁻/day; H⁺ excretion as NH₄⁺ from glutamine deamidation is essential for systemic acid-base homeostasis."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "NHE3 (proximal tubule) reabsorbs ~65% of filtered Na⁺; NKCC2 (TAL, furosemide target) ~25%; ENaC (collecting duct, aldosterone-regulated) ~2%; overall 99.5% of filtered Na⁺ is reclaimed; renal Na⁺ handling is the primary long-term determinant of blood pressure."
  - target: 03-medicine/01-modern/04-cardio/beta-blockers
    relation: modulated-by
    note: "β1-AR blockade on renal juxtaglomerular cells reduces renin secretion → reduced angiotensin II and aldosterone → lower blood pressure; renal renin suppression contributes to antihypertensive efficacy independently of cardiac rate and contractility effects."
taxonomy:
  uberon: "UBERON:0002113"
  fma: "FMA:7203"
---

# Kidney

## Overview

The kidneys are paired, bean-shaped retroperitoneal organs that are the primary regulators of body fluid composition, volume, and acid-base balance. Each weighs approximately 150 g (range 120–170 g), measuring ~11 × 6 × 3 cm, and sits at the level of vertebrae T12–L3 in the posterior abdominal wall, with the right kidney typically 1–2 cm lower than the left (displaced by the liver) [^hall-guyton-14].

The kidney's essential task is to continuously filter the circulating plasma, retain what the body needs, and excrete what it does not — a discriminating process achieved at extraordinary scale. At a normal GFR of 125 mL/min, the two kidneys filter 180 liters of plasma per day — more than 30 times the total blood volume. Yet only about 1.5 liters of urine is produced, meaning 99% of the filtrate is reabsorbed with exquisite selectivity. Beyond filtration, the kidneys act as an endocrine organ, secreting erythropoietin (EPO), renin, and the active form of vitamin D (calcitriol), making them central to erythropoiesis, blood pressure, and calcium homeostasis.

## Structure

### Gross Anatomy

| Region | Contents | Function |
|:---|:---|:---|
| **Cortex** | Glomeruli, proximal/distal convoluted tubules, cortical collecting ducts | Filtration, most reabsorption |
| **Medulla** | Loops of Henle, medullary collecting ducts, vasa recta | Countercurrent multiplication/exchange, urine concentration |
| **Pelvis** | Calyces → renal pelvis → ureter | Urine collection and drainage |

The medulla is organized into 8–18 **renal pyramids** (cone-shaped structures whose apices — the renal papillae — drain into minor calyces). Each pyramid + associated cortex = one **renal lobe**.

A **renal column** (of Bertin) is cortical tissue extending between pyramids, carrying arcuate and interlobar vessels.

### The Nephron

The nephron is the structural and functional unit of the kidney. Each kidney contains ~0.7–1.4 million nephrons (average ~1 million). Each nephron consists of:

1. **Renal corpuscle** — glomerulus + Bowman's capsule
2. **Proximal convoluted tubule (PCT)** — in cortex; ~60–70% of reabsorption; isosmotic
3. **Loop of Henle** — descends into medulla (descending limb: water-permeable, salt-impermeable; ascending limb: salt-permeable, water-impermeable); creates the medullary osmotic gradient
4. **Distal convoluted tubule (DCT)** — aldosterone target; Na⁺/K⁺ exchange via ENaC
5. **Collecting duct** — ADH target; water permeability tunable; final urine concentration

Two nephron classes:
- **Cortical nephrons** (85%) — short loops of Henle, extending only into outer medulla
- **Juxtamedullary nephrons** (15%) — long loops reaching deep medulla, essential for maximal urine concentration

### Blood Supply

The kidney receives ~20–25% of cardiac output (~1.1 L/min from both kidneys together):
- **Renal artery** → **segmental arteries** → **interlobar arteries** → **arcuate arteries** → **interlobular (cortical radiate) arteries** → **afferent arterioles** → **glomerular capillaries** → **efferent arterioles** → **peritubular capillaries** (cortex) / **vasa recta** (medulla) → venous drainage

The **vasa recta** are hairpin-shaped capillaries descending into the medulla alongside the loops of Henle; they are essential for countercurrent exchange that preserves the medullary osmotic gradient without washing it out.

### Juxtaglomerular Apparatus (JGA)

The JGA sits at the vascular pole of each glomerulus and consists of:
- **Juxtaglomerular (JG) cells** — granular cells in the afferent arteriole wall; synthesize and store renin
- **Macula densa** — specialized NaCl-sensing cells in the distal nephron wall adjacent to the JGA
- **Extraglomerular mesangial cells** (lacis cells)

## Function

### Glomerular Filtration

At the [glomerulus](../../05-tissue/glomerulus/README.md), hydrostatic pressure (~60 mmHg) drives plasma ultrafiltration across the three-layer barrier (fenestrated endothelium → GBM → podocyte slit diaphragm). The resulting filtrate is protein-free plasma [^hall-guyton-14].

**GFR determinants:**
- Filtration coefficient (Kf): permeability × surface area
- Afferent arteriole tone (↑ constriction → ↓ GFR)
- Efferent arteriole tone (↑ constriction → ↑ GFR temporarily, then ↓ with severe constriction)
- Oncotic pressure of plasma (↑ protein → ↓ GFR)

### Tubular Reabsorption

| Segment | Key reabsorption | Mechanism |
|:---|:---|:---|
| PCT | 65-70% Na⁺/H₂O, 100% glucose, 100% amino acids | Na⁺-linked cotransporters (SGLT1/2), Na⁺/H⁺ exchanger (NHE3), aquaporin-1 |
| Descending limb Henle | Water (~15%) | Aquaporin-1; passive water follows medullary gradient |
| Thick ascending limb | 25% NaCl (no water) | NKCC2 (target of loop diuretics), K⁺ recycle via ROMK |
| DCT | ~5% NaCl | NCC (thiazide target), Ca²⁺ via TRPV5 |
| Collecting duct | 2-3% Na⁺; variable H₂O (ADH-regulated) | ENaC (aldosterone target), aquaporin-2 (ADH target) |

### Tubular Secretion

The nephron actively secretes into the tubular lumen:
- **H⁺** (distal tubule, collecting duct) — acid excretion, titratable acid formation
- **K⁺** (collecting duct) — regulated by aldosterone
- **NH₄⁺** (from glutamine catabolism in PCT) — ammonium excretion buffering
- **Drugs/xenobiotics** — organic anion/cation transporters (OAT, OCT) in PCT secrete many drugs (penicillin, metformin, cisplatin)

### Urine Concentration Mechanism

The **countercurrent multiplier** in the loop of Henle creates a medullary interstitial osmotic gradient (from ~300 mOsm/kg at cortex → ~1200 mOsm/kg at papilla in antidiuresis). The mechanism:
1. NKCC2 pumps NaCl out of the thick ascending limb without water → builds interstitial gradient
2. Descending limb equilibrates water into hyperosmotic interstitium → tubular fluid becomes concentrated
3. Urea recycling from collecting duct adds to deep medullary gradient
4. **ADH (vasopressin)** from posterior pituitary inserts aquaporin-2 into collecting duct apical membrane → water reabsorbed along gradient → concentrated urine (up to 1200 mOsm/kg)

### Acid-Base Homeostasis

The kidney is the only organ that can regenerate HCO₃⁻ and vary net acid excretion:
- **Proximal tubule:** reabsorbs 85% of filtered HCO₃⁻ (via NHE3 + carbonic anhydrase)
- **Collecting duct α-intercalated cells:** secrete H⁺ via H⁺-ATPase → new HCO₃⁻ returned to blood; titratable acid (mainly phosphate) and ammonium excretion
- **β-intercalated cells:** secrete HCO₃⁻ (alkalosis correction)

### Endocrine Functions

| Hormone | Cell | Stimulus | Effect |
|:---|:---|:---|:---|
| **Erythropoietin (EPO)** | Peritubular fibroblasts (cortex) | Hypoxia → HIF-2α | Stimulates RBC production in bone marrow |
| **Renin** | JG cells of afferent arteriole | Low perfusion pressure, low NaCl (macula densa), β1-adrenergic | Cleaves angiotensinogen → Ang I → Ang II (via ACE) → vasoconstriction + aldosterone → Na⁺/H₂O retention → BP ↑ |
| **Calcitriol (1,25(OH)₂D₃)** | Proximal tubule 1α-hydroxylase | PTH, low Ca²⁺, low phosphate | Active vitamin D; increases intestinal Ca²⁺/PO₄ absorption; bone mineral mobilization; PTH suppression |

### RAAS — Renin-Angiotensin-Aldosterone System

The RAAS is the primary hormonal loop linking renal perfusion to systemic blood pressure:
```
Low renal perfusion → JG cells release renin
Renin + angiotensinogen (liver) → Angiotensin I (inactive)
ACE (lung endothelium) converts Ang I → Angiotensin II
Ang II → (1) vasoconstriction (AT1R on VSMCs), (2) aldosterone release from adrenal cortex
Aldosterone → ENaC upregulation in collecting duct → Na⁺/H₂O retention → volume ↑ → BP ↑
```
ACE inhibitors interrupt this cascade by blocking ACE; this reduces Ang II, dilates efferent arterioles, lowers intraglomerular pressure, and slows CKD progression [^levey-2003-ckd-definition].

## Connections

- **Contains:** [Glomerulus](../../05-tissue/glomerulus/README.md) — the tissue-scale filtration unit.
- **Contains:** [Podocyte](../../04-cellular/podocyte/README.md) — the glomerular epithelial cell.
- **Part of:** [Renal System](../../07-system/renal-system/README.md) — kidney is the primary functional organ.
- **Connects to:** [Cardiovascular System](../../07-system/cardiovascular-system/README.md) — RAAS couples renal function to systemic BP; cardiorenal syndrome links heart failure to AKI.
- **Damaged by:** SARS-CoV-2 — AKI via multiple mechanisms.
- **Treated by:** ACE inhibitors — renoprotection in CKD.
- **Treated by:** Loop diuretics — fluid management in kidney disease.
- **Damaged-by** → [Vancomycin](../../03-medicine/01-modern/06-antimicrobial/vancomycin/README.md): Nephrotoxicity via oxidative tubular injury; AUC/MIC-guided dosing (target AUC 400–600 mg·h/L) replaces trough monitoring (2020 ASHP/IDSA consensus); risk factors: CKD, prolonged courses, NSAIDs or aminoglycoside co-administration.
- `connects-to` → **[Hydrogen](../../02-atomic/hydrogen/README.md)** — Renal α-intercalated cells secrete H⁺ via luminal H⁺-ATPase; NHE3 reabsorbs Na⁺ while secreting H⁺; kidney recovers ~4500 mmol HCO₃⁻/day; H⁺ excretion as NH₄⁺ from glutamine maintains systemic acid-base homeostasis.
- `connects-to` → **[Sodium](../../02-atomic/sodium/README.md)** — NHE3 reabsorbs ~65% of filtered Na⁺ in the proximal tubule; NKCC2 (TAL, furosemide target) ~25%; aldosterone-regulated ENaC (collecting duct) ~2%; 99.5% of filtered Na⁺ is reclaimed; renal Na⁺ handling is the primary long-term blood pressure determinant.
- `modulated-by` → **[Beta-blockers](../../../../03-medicine/01-modern/04-cardio/beta-blockers/README.md)** — β1-AR blockade on renal juxtaglomerular cells reduces renin secretion → reduced angiotensin II and aldosterone → lower blood pressure; renal renin suppression contributes to antihypertensive efficacy independently of cardiac rate and contractility effects.

## Pathology

### Acute Kidney Injury (AKI)

AKI is defined by the **KDIGO criteria**: rise in serum creatinine ≥0.3 mg/dL within 48 h, ≥1.5× baseline within 7 days, or urine output <0.5 mL/kg/h for ≥6 h [^kdigo-2012-aki].

| KDIGO Stage | Creatinine criterion | UO criterion |
|:---|:---|:---|
| 1 | ×1.5–1.9 baseline or +0.3 mg/dL | <0.5 mL/kg/h for 6–12 h |
| 2 | ×2.0–2.9 baseline | <0.5 mL/kg/h for ≥12 h |
| 3 | ×3.0 baseline or ≥4.0 mg/dL | <0.3 mL/kg/h for ≥24 h or anuria ≥12 h |

Major causes: prerenal (hypoperfusion), intrinsic (ATN, glomerulonephritis, AIN, rhabdomyolysis), postrenal (obstruction). COVID-19 AKI occurs in ~25–30% of ICU patients.

### Chronic Kidney Disease (CKD)

CKD: GFR <60 mL/min/1.73 m² or markers of kidney damage for ≥3 months [^levey-2003-ckd-definition] [^kdigo-2012-ckd].

| GFR category | GFR (mL/min/1.73m²) | Description |
|:---|:---|:---|
| G1 | ≥90 | Normal/high |
| G2 | 60–89 | Mildly decreased |
| G3a | 45–59 | Mild-moderately decreased |
| G3b | 30–44 | Moderate-severely decreased |
| G4 | 15–29 | Severely decreased |
| G5 | <15 | Kidney failure / ESRD |

Leading causes worldwide: **diabetic nephropathy** (40%), hypertensive nephrosclerosis (25%), glomerulonephritis (15%).

### Glomerular Diseases

- **Minimal change disease** — podocyte effacement without light-microscopy change; primary cause of nephrotic syndrome in children; steroid-responsive
- **Focal segmental glomerulosclerosis (FSGS)** — podocyte loss → scarring; primary (genetic: NPHS1/2, ACTN4, TRPC6) or secondary (obesity, HIV, sickle cell)
- **IgA nephropathy** — mesangial IgA immune complex deposition; most common primary glomerulonephritis worldwide
- **Membranous nephropathy** — subepithelial immune complex deposition (anti-PLA2R antibodies in 70% of primary cases)
- **Anti-GBM disease (Goodpasture's)** — autoantibodies to collagen IV α3 chain; rapidly progressive glomerulonephritis ± pulmonary hemorrhage

### Other Kidney Diseases

- **Polycystic kidney disease (PKD)** — ADPKD (PKD1/PKD2 mutations, ~1:400–1000) or ARPKD (PKHD1); cyst growth replaces parenchyma, progressive renal failure
- **Renal cell carcinoma (RCC)** — clear cell (75%, VHL mutation), papillary, chromophobe subtypes; often found incidentally on imaging
- **Nephrolithiasis** — calcium oxalate (80%), uric acid, struvite, cystine stones; recurrent without metabolic workup and treatment
- **Renal hypertension** — renovascular (renal artery stenosis) or parenchymal; renin-mediated hypertension

[^hall-guyton-14]: Hall JE. *Guyton and Hall Textbook of Medical Physiology.* 14th ed. Elsevier; 2021. Ch. 26-32.
[^levey-2003-ckd-definition]: Levey AS, Coresh J, Balk E, et al. National Kidney Foundation practice guidelines for chronic kidney disease. *Ann Intern Med.* 2003;139(2):137-47. [doi:10.7326/0003-4819-139-2-200307150-00013](https://doi.org/10.7326/0003-4819-139-2-200307150-00013) · [PubMed 12859163](https://pubmed.ncbi.nlm.nih.gov/12859163/)
[^kdigo-2012-ckd]: KDIGO CKD Work Group. KDIGO 2012 Clinical Practice Guideline for CKD. *Kidney Int Suppl.* 2013;3(1):1-150. [kdigo.org](https://kdigo.org/guidelines/ckd-evaluation-and-management/)
[^kdigo-2012-aki]: KDIGO AKI Work Group. KDIGO Clinical Practice Guideline for Acute Kidney Injury. *Kidney Int Suppl.* 2012;2(1):1-138. [kdigo.org](https://kdigo.org/guidelines/acute-kidney-injury/)
[^vanholder-2021-ckd-epidemiology]: Vanholder R, Annemans L, Brown E, et al. Reducing the costs of chronic kidney disease while delivering quality health care. *Nat Rev Nephrol.* 2017;13(7):393-409. [doi:10.1038/nrneph.2017.63](https://doi.org/10.1038/nrneph.2017.63) · [PubMed 28479604](https://pubmed.ncbi.nlm.nih.gov/28479604/)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
