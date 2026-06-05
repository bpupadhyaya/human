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
