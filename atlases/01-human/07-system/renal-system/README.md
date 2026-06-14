---
schema: human-scale-entry/v1
id: renal-system
name: Renal System
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-04
summary: "Two kidneys, two ureters, bladder, and urethra. Filters 180 L plasma/day, maintains fluid/electrolyte/acid-base homeostasis, excretes nitrogenous waste, and produces EPO, renin, and calcitriol. Tightly coupled to cardiovascular system via RAAS."
aliases: ["urinary system", "renal-urinary system", "excretory system"]
sources:
  - id: hall-guyton-14
    type: textbook
    cite: "Hall JE. Guyton and Hall Textbook of Medical Physiology. 14th ed. Elsevier; 2021. Ch. 26-32."
    url: "https://www.elsevier.com/books/guyton-and-hall-textbook-of-medical-physiology/hall/978-0-323-59712-8"
    accessed: "2026-06-04"
  - id: vanholder-2017-ckd-costs
    type: peer-reviewed
    cite: "Vanholder R, Annemans L, Brown E, et al. Reducing the costs of chronic kidney disease while delivering quality health care: a call to action. Nat Rev Nephrol. 2017;13(7):393-409."
    doi: "10.1038/nrneph.2017.63"
    pmid: "28479604"
    url: "https://doi.org/10.1038/nrneph.2017.63"
  - id: kdigo-2012-ckd
    type: regulatory
    cite: "Kidney Disease: Improving Global Outcomes (KDIGO) CKD Work Group. KDIGO 2012 Clinical Practice Guideline for the Evaluation and Management of Chronic Kidney Disease. Kidney Int Suppl. 2013;3(1):1-150."
    url: "https://kdigo.org/guidelines/ckd-evaluation-and-management/"
    accessed: "2026-06-04"
  - id: openstax-anatomy-ch25
    type: textbook
    cite: "OpenStax. Anatomy & Physiology 2e, Ch. 25: The Urinary System."
    url: "https://openstax.org/books/anatomy-and-physiology-2e/pages/25-introduction"
    accessed: "2026-06-04"
cross_links:
  - target: 01-human/08-whole-body/human-body
    relation: part-of
    note: "The renal system is one of the major organ systems of the integrated human body."
  - target: 01-human/06-organ/kidney
    relation: contains
    note: "The kidneys are the primary functional organs of the renal system — housing nephrons, performing filtration, reabsorption, secretion, and endocrine functions."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "RAAS (renin-angiotensin-aldosterone system) bidirectionally couples renal function to cardiac output and systemic BP; ANP/BNP natriuretic peptides from the heart modulate renal Na⁺ handling."
  - target: 03-medicine/01-modern/04-cardio/ace-inhibitors
    relation: treated-by
    note: "ACE inhibitors are first-line renoprotective therapy in diabetic and non-diabetic CKD; they reduce intraglomerular pressure and proteinuria by blocking Ang II."
  - target: 03-medicine/01-modern/04-cardio/loop-diuretics
    relation: treated-by
    note: "Loop diuretics block NKCC2 in the thick ascending limb; cornerstone of fluid management in AKI, CKD-associated edema, and nephrotic syndrome."
  - target: 01-human/05-tissue/glomerulus
    relation: contains
    note: "The glomerulus is the tissue-level filtration structure within each nephron of the kidney."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "Renal and intestinal Na⁺/H₂O handling are complementary; aldosterone and ANP coordinate gut and kidney fluid reabsorption; hepatorenal interactions include shared RAAS regulation."
  - target: 03-medicine/01-modern/04-cardio/arbs
    relation: treated-by
    note: "ARBs are first-line renoprotective therapy in diabetic and non-diabetic CKD; AT1 blockade dilates the efferent arteriole, reducing intraglomerular pressure, proteinuria, and CKD progression (RENAAL, IDNT trials)."
  - target: 03-medicine/01-modern/04-cardio/arbs
    relation: modulated-by
    note: "RAAS blockade by ARBs reduces angiotensin II–driven efferent vasoconstriction, decreasing glomerular hypertension and filtration of albumin; also reduces aldosterone-driven Na⁺ retention and tubular fibrosis."
  - target: 01-human/03-molecular/vasopressin
    relation: modulated-by
    note: "Modulated by Vasopressin."
  - target: 02-pathogen/02-bacteria/streptococcus-pyogenes
    relation: damaged-by
    note: "Damaged by Streptococcus pyogenes."
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "Chronic kidney disease is the renal system's common end state: progressive nephron loss from diabetes, hypertension, or glomerular disease reduces GFR, so the kidney fails its fluid, electrolyte, acid-base, waste, and endocrine roles—ending in dialysis or transplant."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "The renal system is also an endocrine organ within the endocrine system: the kidney secretes erythropoietin and renin and activates vitamin D, while responding to aldosterone, ADH, and PTH—so kidney disease causes anemia, bone disease, and blood-pressure dysregulation."
  - target: 01-human/07-system/iga-nephropathy
    relation: connects-to
    note: "IgA nephropathy is the world's commonest primary glomerulonephritis, a core renal-system disease: galactose-deficient IgA1 immune complexes deposit in the mesangium, causing hematuria (often after mucosal infection) and, in many, progression to chronic kidney disease."
  - target: 01-human/03-molecular/erythropoietin
    relation: connects-to
    note: "The renal system is an endocrine organ via erythropoietin: peritubular cells sense low oxygen and secrete EPO to drive red-cell production, so kidney disease causes anemia while EPO excess causes polycythemia—linking renal function to oxygen-carrying capacity."
  - target: 01-human/02-atomic/potassium
    relation: connects-to
    note: "Potassium balance is a core renal-system job: the kidney tunes potassium excretion under aldosterone, so renal failure causes life-threatening hyperkalemia while diuretics cause hypokalemia—small shifts in this ion can stop the heart, making renal K+ handling vital."
  - target: 01-human/07-system/renal-cell-carcinoma
    relation: connects-to
    note: "Renal cell carcinoma is the principal cancer of the renal system: arising from tubular epithelium, it can secrete erythropoietin or renin (paraneoplastic syndromes) and presents late with hematuria or a mass—turning the kidney's own physiology into its tumor's behavior."
  - target: 01-human/04-cellular/podocyte
    relation: connects-to
    note: "Podocytes are the renal system's filtration gatekeepers: their interlocking foot processes form the slit diaphragm that holds protein back, so podocyte injury causes proteinuria and nephrotic syndrome—a frequent first step toward chronic kidney disease."
  - target: 01-human/03-molecular/renin
    relation: connects-to
    note: "Renin launches the renal system's blood-pressure axis: juxtaglomerular cells release it when renal perfusion or sodium falls, triggering angiotensin and aldosterone to retain salt and water—so the kidney is the body's master regulator of volume and pressure."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "Sodium handling is the renal system's central task: the nephron filters and precisely reabsorbs sodium to set extracellular volume and blood pressure, so disordered renal sodium balance drives both hypertension and edema, and is the target of most diuretics."
  - target: 01-human/03-molecular/aldosterone
    relation: connects-to
    note: "Aldosterone is the kidney's salt-retaining hormone: released via the renin axis, it makes the distal nephron reabsorb sodium and excrete potassium, so it sets blood volume and pressure—and blocking it (spironolactone) treats resistant hypertension and heart failure."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "The kidney is central to calcium balance: it activates vitamin D to absorb calcium, fine-tunes calcium excretion under PTH, and when it fails, disturbed calcium-phosphate handling drives the bone disease and stones of kidney disease."
  - target: 01-human/07-system/hypertension
    relation: connects-to
    note: "Kidney and blood pressure are locked in a two-way grip: the kidney sets long-term pressure through salt and the renin system, yet high pressure also damages its vessels—so hypertension is both a leading cause and a consequence of kidney disease."
  - target: 03-medicine/03-food/vitamin-d
    relation: connects-to
    note: "The kidney is where vitamin D becomes active: it performs the final 1-alpha-hydroxylation to calcitriol, so kidney failure causes vitamin D deficiency and the bone disease of CKD—one of the organ's vital endocrine, non-excretory jobs."
  - target: 01-human/02-atomic/phosphorus
    relation: connects-to
    note: "The renal system is the body's phosphate gatekeeper: kidneys excrete phosphate under FGF23 and PTH control, so failing kidneys retain it, driving the calcium-phosphate imbalance and vascular calcification of CKD-mineral bone disorder."
  - target: 01-human/03-molecular/pth
    relation: connects-to
    note: "The kidney and PTH run the calcium-phosphate axis together: failing kidneys retain phosphate and underproduce active vitamin D, driving secondary hyperparathyroidism in which PTH soars to defend calcium—at the cost of the bones."
  - target: 01-human/02-atomic/hydrogen
    relation: connects-to
    note: "The kidney is the body's slow acid-base regulator through hydrogen: it excretes hydrogen ions and regenerates bicarbonate to hold blood pH steady, so kidney failure or tubular defects cause the metabolic acidosis (renal tubular acidosis) of renal disease."
  - target: 01-human/03-molecular/albumin
    relation: connects-to
    note: "The kidney's filter is judged by albumin: a healthy glomerulus keeps this protein in the blood, so albumin leaking into urine (albuminuria) is the earliest, most sensitive sign of kidney damage and a marker that guides treatment."
  - target: 01-human/03-molecular/angiotensin-ii
    relation: connects-to
    note: "The renal system controls blood pressure through angiotensin II: the kidney's renin launches the cascade that makes angiotensin II to constrict vessels and tune filtration, the loop that ACE inhibitors and ARBs block to protect the kidney."
taxonomy:
  uberon: "UBERON:0001008"
---

# Renal System

## Overview

The renal system — also called the urinary system — is the body's master regulator of plasma composition, fluid volume, and chemical waste elimination. It comprises two **kidneys**, two **ureters**, the **urinary bladder**, and the **urethra** [^openstax-anatomy-ch25].

While its anatomical simplicity belies its functional complexity, the renal system executes one of the most demanding tasks in human physiology: continuously sampling and adjusting the chemical composition of every milliliter of plasma, 24 hours a day, filtering 180 liters of plasma per day while returning 99% of the filtrate to the circulation with exquisite selectivity. The kidneys maintain plasma Na⁺ within ±5 mEq/L, pH within ±0.05 units, and plasma osmolality within ±5 mOsm/kg — tolerances that no other organ system can achieve.

Beyond excretion, the renal system is an endocrine hub: the kidneys secrete **erythropoietin** (EPO, regulating red blood cell production), **renin** (initiating the RAAS cascade to control blood pressure), and produce **calcitriol** (1,25-dihydroxyvitamin D₃, regulating calcium-phosphate metabolism). This makes CKD a multisystem disease — its complications span anemia (low EPO), hypertension (high renin), and bone disease (low calcitriol) [^hall-guyton-14].

The renal and cardiovascular systems are deeply interdependent: renal perfusion depends on cardiac output; renal RAAS controls vascular resistance and cardiac preload; impaired kidney function is the dominant non-cardiac predictor of cardiovascular mortality.

## Structure

### Organs and Anatomical Relationships

**Kidneys** — paired, retroperitoneal, at T12–L3. Right kidney displaced inferior by liver. Each ~150 g, ~11 × 6 × 3 cm. Surrounded by renal capsule, perirenal fat, renal fascia (Gerota's). Composed of cortex (glomeruli, proximal/distal tubules), medulla (loops of Henle, collecting ducts, pyramids), and pelvis (drainage).

**Ureters** — fibromuscular tubes (~25–30 cm) connecting renal pelvis to bladder. Peristaltic waves propel urine. Three anatomical narrowings (sites of stone impaction): ureteropelvic junction, pelvic brim crossing, ureterovesical junction.

**Urinary Bladder** — muscular reservoir (capacity 400–600 mL comfortable, ~1000 mL maximum). Wall: urothelium (transitional epithelium) → lamina propria → detrusor muscle (smooth muscle). Trigone (base): orifices of two ureters + internal urethral orifice.

**Urethra** — female (~4 cm) or male (~20 cm, incorporating prostatic, membranous, and spongy/penile segments). External urethral sphincter (voluntary, skeletal muscle) allows conscious voiding control.

### Innervation and Voiding Reflex

Micturition is controlled by overlapping autonomic and somatic systems:
- **Parasympathetic (S2–S4, pelvic nerves)** — detrusor contraction (M3 receptors); internal sphincter relaxation
- **Sympathetic (T10–L2, hypogastric nerves)** — detrusor relaxation (β3 receptors); internal sphincter contraction (α1 receptors) — stores urine
- **Somatic (S2–S4, pudendal nerve)** — external sphincter voluntary control
- **Pontine micturition center** — coordinates parasympathetic activation + sphincter relaxation; overridden by cortical inhibition during continent storage

### Nephron Structure

~1–2 million nephrons per kidney (combined total ~2 million). Each nephron = renal corpuscle + proximal tubule + loop of Henle + distal tubule + collecting duct. See [Kidney](../../06-organ/kidney/README.md) for detailed nephron anatomy.

### Vascular Supply

Renal arteries arise directly from the aorta at L1–L2 and deliver 20–25% of cardiac output to the kidneys (~1.1 L/min combined). The high flow relative to kidney mass (5× body average) reflects the filtration function, not metabolic demand. Renal veins drain to the inferior vena cava.

### Lymphatics

Renal lymphatics drain to para-aortic lymph nodes. Obstruction (lymphoma, retroperitoneal fibrosis) can cause chyluria.

## Function

### Plasma Ultrafiltration and Selective Reabsorption

At the [glomerulus](../../05-tissue/glomerulus/README.md), hydrostatic pressure forces a protein-free filtrate into Bowman's space. Tubular epithelial cells then selectively reabsorb 99%+ of the filtrate through a coordinated array of transporters and channels:

- **PCT:** 65–70% NaCl and water; 100% glucose, amino acids, phosphate; 85% HCO₃⁻
- **Loop of Henle:** ~25% NaCl (ascending limb); ~15% water (descending limb); creates medullary gradient
- **DCT:** ~5% NaCl; regulated Ca²⁺ and Mg²⁺
- **Collecting duct:** aldosterone-regulated Na⁺; ADH-regulated water

### Electrolyte and Volume Homeostasis

The kidney is the dominant regulator of:

| Parameter | Mechanism |
|:---|:---|
| **Na⁺** | PCT (NHE3, Na⁺-K⁺-ATPase), TAL (NKCC2), DCT (NCC), CCD (ENaC/aldosterone) |
| **K⁺** | CCD principal cells: aldosterone ↑ K⁺ secretion via ROMK; intercalated cells reabsorb K⁺ |
| **Ca²⁺** | PCT (passive, 60%), TAL (passive, CLDN16/19), DCT (active, TRPV5/calbidin/NCX1) — PTH and calcitriol regulate |
| **Phosphate** | PCT (NaPi-IIa/IIc) — PTH inhibits; FGF-23 inhibits |
| **Magnesium** | TAL (CLDN16 paracellular), DCT (TRPM6 active) |
| **H⁺/HCO₃⁻** | PCT (HCO₃⁻ reclamation), α-IC cells (H⁺ secretion/net acid excretion) |

### Nitrogen Waste Excretion

The kidneys are the primary route for excreting nitrogenous waste:
- **Urea** — product of hepatic urea cycle (from ammonia of amino acid catabolism); filtered + partially reabsorbed + recycled in medullary concentration mechanism; serum BUN reflects balance between generation and excretion
- **Creatinine** — nonenzymatic breakdown product of creatine phosphate in muscle; near-freely filtered, minimally secreted; serum creatinine inversely reflects GFR (the basis of CKD staging)
- **Uric acid** — purine catabolism end-product; filtered, largely reabsorbed, secreted by PCT OAT4/URAT1 transporters; hyperuricemia causes gout, and high urate predicts CKD progression

### Acid-Base Homeostasis

Normal plasma pH = 7.35–7.45. The kidney handles long-term acid-base balance:
1. **HCO₃⁻ reclamation** in PCT — 85% of filtered bicarbonate recovered
2. **New HCO₃⁻ generation** in collecting duct α-intercalated cells via H⁺-ATPase — each H⁺ secreted = one new HCO₃⁻ returned to blood
3. **Ammonium (NH₄⁺) excretion** — PCT glutamine catabolism generates NH₃ → combines with H⁺ → NH₄⁺ in tubular lumen → excreted in urine; most important buffer for chronic acid loads
4. **Titratable acid excretion** — H⁺ buffered by HPO₄²⁻ → H₂PO₄⁻; excreted

### RAAS and Blood Pressure

RAAS is the dominant hormonal control loop for long-term blood pressure (see [Kidney](../../06-organ/kidney/README.md)):
- Renin from JG cells → Ang I → Ang II → vasoconstriction + aldosterone → Na⁺/water retention → blood pressure restoration
- ACE inhibitors block this cascade — antihypertensive + renoprotective

Natriuretic counterpoint:
- **ANP/BNP** (from atria/ventricles when stretched) → increase GFR, inhibit ENaC, suppress aldosterone and renin → natriuresis + diuresis → volume reduction

### Endocrine Functions

- **Erythropoietin (EPO):** Cortical peritubular fibroblasts; secreted in response to HIF-2α activation under hypoxia; drives RBC production in bone marrow. CKD → EPO deficiency → normocytic normochromic anemia of CKD; treated with recombinant EPO (epoetin) or HIF-prolyl hydroxylase inhibitors.
- **Renin:** JG cells; cleaves angiotensinogen; RAAS initiator.
- **Calcitriol (1,25(OH)₂D₃):** CYP27B1 (1α-hydroxylase) in PCT converts 25(OH)D → calcitriol; regulated by PTH, FGF-23, Ca²⁺, phosphate; stimulates intestinal Ca²⁺/PO₄ absorption; suppresses PTH; CKD → loss of 1α-hydroxylase → low calcitriol → secondary hyperparathyroidism → renal osteodystrophy.

## Connections

- **Part of:** [Human Body](../../08-whole-body/human-body/README.md) — one of the major organ systems.
- **Contains:** [Kidney](../../06-organ/kidney/README.md) — the primary functional organ.
- **Contains:** [Glomerulus](../../05-tissue/glomerulus/README.md) — the tissue-level filtration unit.
- **Contains:** [Podocyte](../../04-cellular/podocyte/README.md) — the key glomerular cell.
- **Connects to:** [Cardiovascular System](../../07-system/cardiovascular-system/README.md) — RAAS, natriuretic peptides, and volume/pressure interdependence.
- **Connects to:** [Digestive System](../digestive-system/README.md) — water and electrolyte reabsorption in the gut is complementary and overlapping with renal control.
- **Connects to:** [Chronic Kidney Disease](../ckd/README.md) — the renal system's common end state: progressive nephron loss reduces GFR until fluid, electrolyte, acid-base, waste, and endocrine roles all fail, ending in dialysis or transplant.
- **Connects to:** [Endocrine System](../endocrine-system/README.md) — the kidney is itself endocrine, secreting erythropoietin and renin and activating vitamin D while responding to aldosterone, ADH, and PTH.
- **Connects to:** [IgA Nephropathy](../iga-nephropathy/README.md) — the world's commonest primary glomerulonephritis: mesangial galactose-deficient IgA1 deposits cause hematuria and can progress to chronic kidney disease.
- **Connects to:** [Erythropoietin](../../03-molecular/erythropoietin/README.md) — the renal system is an endocrine organ: peritubular cells sense low oxygen and secrete EPO to drive red-cell production, so kidney disease causes anemia while EPO excess causes polycythemia.
- **Connects to:** [Potassium](../../02-atomic/potassium/README.md) — potassium balance is a core renal job: the kidney tunes K+ excretion under aldosterone, so renal failure causes hyperkalemia while diuretics cause hypokalemia—shifts that can stop the heart.
- **Connects to:** [Renal Cell Carcinoma](../renal-cell-carcinoma/README.md) — the principal cancer of the renal system: arising from tubular epithelium, it can secrete erythropoietin or renin (paraneoplastic) and presents late with hematuria or a mass.
- **Connects to:** [Podocyte](../../04-cellular/podocyte/README.md) — podocytes are the renal system's filtration gatekeepers: their foot processes form the slit diaphragm that holds protein back, so podocyte injury causes proteinuria and nephrotic syndrome, a frequent first step toward CKD.
- **Connects to:** [Renin](../../03-molecular/renin/README.md) — renin launches the renal system's blood-pressure axis: juxtaglomerular cells release it when perfusion or sodium falls, triggering angiotensin and aldosterone to retain salt and water—making the kidney the master regulator of volume and pressure.
- **Connects to:** [Sodium](../../02-atomic/sodium/README.md) — sodium handling is the renal system's central task: the nephron filters and reabsorbs sodium to set extracellular volume and blood pressure, so disordered renal sodium balance drives hypertension and edema and is the target of most diuretics.
- **Connects to:** [Aldosterone](../../03-molecular/aldosterone/README.md) — Aldosterone is the kidney's salt-retaining hormone: released via the renin axis, it makes the distal nephron reabsorb sodium and excrete potassium, so it sets blood volume and pressure—and blocking it (spironolactone) treats resistant hypertension and heart failure.
- **Connects to:** [Calcium](../../02-atomic/calcium/README.md) — The kidney is central to calcium balance: it activates vitamin D to absorb calcium, fine-tunes calcium excretion under PTH, and when it fails, disturbed calcium-phosphate handling drives the bone disease and stones of kidney disease.
- **Connects to:** [Hypertension](../hypertension/README.md) — Kidney and blood pressure are locked in a two-way grip: the kidney sets long-term pressure through salt and the renin system, yet high pressure also damages its vessels—so hypertension is both a leading cause and a consequence of kidney disease.
- **Connects to:** [Vitamin D (Calciferol)](../../../03-medicine/03-food/vitamin-d/README.md) — The kidney is where vitamin D becomes active: it performs the final 1-alpha-hydroxylation to calcitriol, so kidney failure causes vitamin D deficiency and the bone disease of CKD—one of the organ's vital endocrine, non-excretory jobs.
- **Connects to:** [Phosphorus](../../02-atomic/phosphorus/README.md) — The renal system is the body's phosphate gatekeeper: kidneys excrete phosphate under FGF23 and PTH control, so failing kidneys retain it, driving the calcium-phosphate imbalance and vascular calcification of CKD-mineral bone disorder.
- **Connects to:** [PTH](../../03-molecular/pth/README.md) — The kidney and PTH run the calcium-phosphate axis together: failing kidneys retain phosphate and underproduce active vitamin D, driving secondary hyperparathyroidism in which PTH soars to defend calcium—at the cost of the bones.
- **Connects to:** [Hydrogen](../../02-atomic/hydrogen/README.md) — the kidney is the body's slow acid-base regulator through hydrogen: it excretes hydrogen ions and regenerates bicarbonate to hold blood pH steady, so kidney failure or tubular defects cause the metabolic acidosis (renal tubular acidosis) of renal disease.
- **Connects to:** [Albumin](../../03-molecular/albumin/README.md) — the kidney's filter is judged by albumin: a healthy glomerulus keeps this protein in the blood, so albumin leaking into urine (albuminuria) is the earliest, most sensitive sign of kidney damage and a marker that guides treatment.
- **Connects to:** [Angiotensin II](../../03-molecular/angiotensin-ii/README.md) — the renal system controls blood pressure through angiotensin II: the kidney's renin launches the cascade that makes angiotensin II to constrict vessels and tune filtration, the loop that ACE inhibitors and ARBs block to protect the kidney.
- **Treated by:** ACE inhibitors — renoprotection in CKD.
- **Treated by:** Loop diuretics — fluid management.

## Pathology

### Chronic Kidney Disease (CKD)

CKD affects ~850 million people worldwide — about 10% of the global adult population [^vanholder-2017-ckd-costs]. It is defined by GFR <60 mL/min/1.73 m² or markers of kidney damage for ≥3 months [^kdigo-2012-ckd].

**Systemic complications of advanced CKD (GFR <30 mL/min):**
- **Anemia** (EPO deficiency) → fatigue, dyspnea on exertion
- **Hypertension** (renin excess, volume overload) → cardiovascular risk
- **Metabolic acidosis** (reduced acid excretion capacity) → muscle wasting, bone disease
- **Hyperkalemia** (impaired K⁺ excretion) → arrhythmia risk
- **Renal osteodystrophy** (low calcitriol → secondary HPT → high PTH → bone turnover)
- **Uremia** (retention of urea, uremic toxins) → pericarditis, encephalopathy, platelet dysfunction
- **ESRD (GFR <15 mL/min)** → renal replacement therapy: hemodialysis, peritoneal dialysis, or transplant

### Acute Kidney Injury (AKI)

Sudden-onset rise in creatinine (≥0.3 mg/dL in 48h or ≥1.5× baseline in 7 days) or oliguria. Major causes: prerenal (60-70%), intrinsic (25-40%), postrenal (5-10%). COVID-19 AKI up to 30% of ICU patients.

### Urinary Tract Infections (UTI) and Pyelonephritis

Ascending bacterial infection (>80% *E. coli*): cystitis (bladder), pyelonephritis (kidney parenchyma). Predisposing factors: female anatomy, urinary obstruction, vesicoureteral reflux, immunosuppression, diabetes, catheterization.

### Nephrolithiasis

Most common urological condition in adults (~10% lifetime prevalence). Calcium oxalate (75%), uric acid (10%), struvite (5-10%), cystine (1%). Predisposing: dehydration, hypercalciuria, hyperoxaluria, low urine volume, anatomical abnormalities.

### Bladder Cancer

Predominantly urothelial (transitional cell) carcinoma. Most common risk factor: cigarette smoking. Other: occupational aromatic amine exposure, cyclophosphamide, chronic UTI (squamous cell), schistosomiasis.

### Polycystic Kidney Disease

ADPKD (PKD1/PKD2): autosomal dominant, progressive cyst growth in both kidneys → progressive renal failure by median age 55-70 depending on gene. Complication: hypertension (RAAS activation), intracranial aneurysms, liver cysts.

[^hall-guyton-14]: Hall JE. *Guyton and Hall Textbook of Medical Physiology.* 14th ed. Elsevier; 2021. Ch. 26-32.
[^vanholder-2017-ckd-costs]: Vanholder R, Annemans L, Brown E, et al. Reducing the costs of chronic kidney disease while delivering quality health care. *Nat Rev Nephrol.* 2017;13(7):393-409. [doi:10.1038/nrneph.2017.63](https://doi.org/10.1038/nrneph.2017.63) · [PubMed 28479604](https://pubmed.ncbi.nlm.nih.gov/28479604/)
[^kdigo-2012-ckd]: KDIGO CKD Work Group. KDIGO 2012 Clinical Practice Guideline for CKD. *Kidney Int Suppl.* 2013;3(1):1-150. [kdigo.org](https://kdigo.org/guidelines/ckd-evaluation-and-management/)
[^openstax-anatomy-ch25]: OpenStax. *Anatomy & Physiology 2e*, Ch. 25: The Urinary System. [Read online →](https://openstax.org/books/anatomy-and-physiology-2e/pages/25-introduction)
