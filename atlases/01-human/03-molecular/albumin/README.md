---
schema: human-scale-entry/v1
id: albumin
name: Albumin
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-05
summary: "Most abundant plasma protein (~35–50 g/L); 66.5 kDa, 585 aa, 3 α-helical domains; synthesised by hepatocytes (~12–14 g/day, t½ ~20 days). Provides ~80% of oncotic pressure; transports FAs, bilirubin, drugs, hormones. Hypoalbuminaemia → oedema, ascites."
aliases: ["serum albumin", "HSA", "human serum albumin", "ALB"]
sources:
  - id: stryer-biochemistry
    type: textbook
    cite: "Berg JM, Tymoczko JL, Stryer L. Biochemistry. 9th ed. W.H. Freeman; 2019."
    url: "https://www.macmillanlearning.com/college/us/product/Biochemistry/p/131911467X"
    accessed: "2026-06-05"
  - id: alberts-mol-cell-biology
    type: textbook
    cite: "Alberts B, Johnson A, Lewis J, et al. Molecular Biology of the Cell. 7th ed. W.W. Norton; 2022."
    url: "https://www.ncbi.nlm.nih.gov/books/NBK26880/"
    accessed: "2026-06-05"
cross_links:
  - target: 01-human/04-cellular/hepatocyte
    relation: expresses
    note: "Albumin is synthesised exclusively by hepatocytes at ~12–14 g/day; albumin mRNA is among the most highly expressed in liver; serum albumin is a key surrogate marker of hepatic synthetic function."
  - target: 01-human/05-tissue/glomerulus
    relation: modulates
    note: "Albumin is excluded from filtrate by the glomerular charge barrier; microalbuminuria (≥30 mg/day) indicates glomerular injury in diabetic or hypertensive nephropathy and is the earliest marker of CKD."
  - target: 01-human/07-system/cardiovascular-system
    relation: modulates
    note: "Albumin generates ~80% of plasma oncotic pressure (~21 mmHg), opposing hydrostatic pressure in Starling equilibrium; hypoalbuminaemia → ↓oncotic pressure → interstitial oedema and ascites."
  - target: 01-human/06-organ/kidney
    relation: modulates
    note: "Only free (albumin-unbound) drugs and hormones are filtered by glomeruli; albumin binding prolongs drug t½; urinary albumin excretion (ACR) is the earliest marker of diabetic nephropathy and CKD progression."
---

# Albumin

## Overview

**Albumin** (human serum albumin, HSA) is the **most abundant plasma protein** in human blood, present at concentrations of **35–50 g/L** in healthy adults [^stryer-biochemistry]. It is produced exclusively by **hepatocytes** at a rate of approximately 12–14 g/day, accounting for roughly 25% of total hepatic protein synthesis. With a plasma half-life of ~20 days — maintained by neonatal Fc receptor (FcRn)-mediated recycling from endosomes — albumin is a long-lived protein that acts simultaneously as the principal **oncotic agent**, a **molecular taxi** for lipophilic molecules, and a **redox buffer** in the circulation.

Clinically, serum albumin is one of the most commonly measured laboratory values: it reflects hepatic synthetic capacity, nutritional status, and the severity of inflammatory states. **Hypoalbuminaemia** (< 35 g/L) is a robust predictor of morbidity and mortality across virtually every disease category.

## Structure

**Molecular weight:** ~66.5 kDa  
**Amino acids:** 585 (mature form, after signal peptide cleavage)  
**Disulfide bonds:** 17 disulfide bridges; **1 free cysteine** at position 34 (Cys34) — the principal free thiol in plasma  
**Glycosylation:** none — albumin is not glycosylated, distinguishing it from most secreted plasma proteins

### Domain architecture

Albumin consists of three homologous α-helical domains (I, II, III), each subdivided into two subdomains (A and B), giving a total of six subdomains in a heart- or kidney-shaped three-dimensional structure [^alberts-mol-cell-biology]:

| Domain | Subdomains | Principal ligand-binding function |
|:---|:---|:---|
| **Domain I (IA/IB)** | IA, IB | Metal binding (Cu²⁺, Ni²⁺ via ATCUN motif at N-terminus) |
| **Domain II (IIA/IIB)** | IIA, IIB | **Sudlow site I** — warfarin, NSAIDs (bulky heterocyclic compounds) |
| **Domain III (IIIA/IIIB)** | IIIA, IIIB | **Sudlow site II** — benzodiazepines, ibuprofen (aromatic carboxylates) |

**Fatty acid binding:** 6–8 high-affinity FA binding sites distributed across all three domains; FA binding induces conformational rearrangement (N→B transition) that allosterically modulates drug-binding affinity.

**Cys34:** The only free thiol in albumin; forms a mixed disulfide with cysteine in circulation (oxidized form); serves as major plasma antioxidant (~0.5 mM concentration); coordinates Cu²⁺ via the N-terminal ATCUN (Asp-Thr-His-) motif; site of S-nitrosylation (albumin-SNO — circulating NO reservoir).

## Function

### 1. Oncotic pressure maintenance

Albumin is responsible for approximately **80% of plasma colloid osmotic (oncotic) pressure** (~21 mmHg out of a total ~25 mmHg), primarily because of its high concentration and relatively small molecular weight [^stryer-biochemistry]. The Starling equation governs transcapillary fluid exchange:

> **Net filtration = Kf × [(Pc − Pi) − σ(πc − πi)]**

Where πc = plasma oncotic pressure (dominated by albumin) and πi = interstitial oncotic pressure. A fall in serum albumin of 10 g/L reduces πc by ~2–4 mmHg, sufficient to shift the Starling equilibrium toward filtration → **interstitial oedema** and, in the peritoneal cavity, **ascites**.

### 2. Lipid transport

Albumin maintains plasma free fatty acid (FFA) concentrations in the nanomolar range by binding 6–8 FA molecules with affinities spanning the nanomolar-to-micromolar range. This is essential because unbound long-chain FAs are detergent-like and disrupt membranes. Albumin ferries FAs from **adipose tissue to liver and muscle** during fasting, exercise, and physiological lipolysis.

### 3. Drug transport

The two Sudlow sites on albumin determine the pharmacokinetics of a vast array of clinical drugs:
- **Site I (domain IIA):** warfarin, phenytoin, sulfonamides, NSAIDs (salicylate), furosemide, bilirubin
- **Site II (domain IIIA):** benzodiazepines (diazepam), ibuprofen, digitoxin, fatty acids

**Critical pharmacokinetic principle:** only the **free (unbound) fraction** of a drug is pharmacologically active, able to cross membranes, and subject to renal/hepatic clearance. In hypoalbuminaemia, drugs with normally high protein binding (e.g., warfarin ~99% bound) have dramatically increased free fractions → toxicity at standard doses.

### 4. Bilirubin transport

Unconjugated bilirubin (UCB) is water-insoluble and neurotoxic at high concentrations. Albumin's Sudlow site I binds UCB with very high affinity (KD ~50 nM), maintaining essentially all circulating UCB in bound form. This prevents UCB from crossing the blood-brain barrier (**kernicterus** — bilirubin encephalopathy in neonates — occurs when free UCB overwhelms albumin binding capacity, as in haemolysis or hypoalbuminaemia).

### 5. Hormone transport

| Hormone | Albumin-bound fraction | Higher-affinity binding protein |
|:---|:---|:---|
| Cortisol | ~10% | CBG (corticosteroid-binding globulin, 80%) |
| Thyroxine (T4) | ~15% | TBG (thyroid-binding globulin, 70%) |
| Testosterone | ~38% | SHBG (60%) |
| Oestradiol | ~40% | SHBG (58%) |

Albumin's large circulating mass makes it a significant reservoir for these hormones even at low individual affinities; albumin-bound hormone is in rapid equilibrium with the free form, unlike the tighter, slower-dissociating CBG/SHBG complexes.

### 6. Antioxidant function

Cys34 scavenges reactive oxygen and nitrogen species:
- React with HOCl (hypochlorous acid from neutrophil myeloperoxidase)
- React with ONOO⁻ (peroxynitrite)
- Form **S-nitroso-albumin** (SNO-albumin) — a circulating NO reservoir that can transfer NO to thiols on red blood cells (Hb-SNO) for delivery to hypoxic tissues

## Mechanism

### Biosynthesis and secretion

Hepatocytes synthesise albumin constitutively as pre-proalbumin → signal peptide cleaved in ER → proalbumin (propeptide at N-terminus) → signal peptide-independent processing in Golgi → **mature albumin** secreted directly into sinusoidal blood.

**Regulation:** Albumin synthesis is downregulated during acute-phase response (IL-6, IL-1β, TNF-α redirect hepatocyte translation toward acute-phase proteins — CRP, fibrinogen, SAA) — making albumin a **negative acute-phase reactant**. Hypo-oncotic states stimulate albumin synthesis (colloid osmoreceptor mechanism in liver).

### FcRn-mediated recycling

Albumin shares the **neonatal Fc receptor (FcRn)** recycling pathway with IgG:
1. Albumin is endocytosed by vascular endothelial cells and macrophages via fluid-phase and receptor-mediated routes
2. In acidic endosomes (pH ~6.0), albumin binds FcRn with high affinity (FcRn does not bind at pH 7.4, preventing competition with circulating albumin)
3. FcRn-albumin complex is transcytosed back to the cell surface
4. At pH 7.4, albumin is released → returns to circulation
5. Albumin not rescued by FcRn is degraded in lysosomes

This recycling mechanism explains the ~20-day half-life of both albumin and IgG — both use FcRn as a "molecular salvation" pathway. FcRn-based engineering is exploited to extend the half-life of therapeutic proteins.

## Connections

- **Expressed-by** → [Hepatocyte](../../04-cellular/hepatocyte/README.md): Albumin is synthesised exclusively by hepatocytes at ~12–14 g/day; albumin mRNA is among the most highly expressed in the liver; serum albumin is a key surrogate marker of hepatic synthetic function [^stryer-biochemistry].
- **Modulates** → [Glomerulus](../../05-tissue/glomerulus/README.md): Albumin is excluded from filtrate by the glomerular charge barrier (net negative charge at pH 7.4 repels the GBM polyanion layer); microalbuminuria indicates glomerular injury (diabetic/hypertensive nephropathy) [^alberts-mol-cell-biology].
- **Modulates** → [Cardiovascular System](../../07-system/cardiovascular-system/README.md): Albumin generates ~80% of plasma oncotic pressure (~21 mmHg), opposing hydrostatic pressure in Starling equilibrium; hypoalbuminaemia reduces oncotic pressure, driving interstitial oedema and ascites [^stryer-biochemistry].
- **Modulates** → [Kidney](../../06-organ/kidney/README.md): Only free (albumin-unbound) drugs and hormones are filtered by glomeruli; albumin binding prolongs drug t½; urinary albumin excretion (ACR) is the earliest marker of diabetic nephropathy and CKD progression [^alberts-mol-cell-biology].

## Pathology

| Condition | Mechanism | Consequences |
|:---|:---|:---|
| **Hypoalbuminaemia (< 35 g/L)** | ↓synthesis (liver failure), ↑urinary loss (nephrotic), protein-losing enteropathy, burns, critical illness | Peripheral oedema, ascites, pulmonary oedema, altered drug pharmacokinetics |
| **Nephrotic syndrome** | Glomerular damage → albumin loss > 3.5 g/day in urine | Severe hypoalbuminaemia, generalised oedema, hyperlipidaemia (↑VLDL synthesis), DVT risk (↓antithrombin III) |
| **Liver cirrhosis** | Hepatocyte loss + stellate cell fibrosis → ↓albumin synthesis | Portal hypertension + hypoalbuminaemia → ascites; monitor with Child-Pugh/MELD |
| **Malnutrition / kwashiorkor** | Protein deficiency → ↓albumin synthesis | Peripheral oedema with adequate caloric intake; classic presentation in kwashiorkor vs marasmus |
| **Acute-phase response** | IL-6 redirects hepatic synthesis → ↓albumin; volume expansion also dilutes | Transient hypoalbuminaemia in sepsis/surgery; serum albumin not a reliable nutrition marker acutely |
| **Familial dysalbuminaemia** | R218H mutation in albumin domain II → abnormally high T4 binding → misleading ↑total T4 (euthyroid) | Spurious hyperthyroxinaemia; FT4 normal |
| **Warfarin sensitivity (hypoalbuminaemia)** | ↓albumin → ↑free warfarin → over-anticoagulation at standard dose | Haemorrhage; dose reduction required |
| **Kernicterus** | ↑unconjugated bilirubin overwhelms albumin-binding capacity in neonates → free bilirubin crosses BBB | Bilirubin encephalopathy → cerebral palsy, sensorineural deafness |

## See Also

- [Hepatocyte](../../04-cellular/hepatocyte/README.md) — site of albumin synthesis; serum albumin reflects hepatocellular function
- [Hepatic lobule](../../05-tissue/hepatic-lobule/README.md) — structural unit of albumin production; pericentral hepatocytes contribute most synthesis
- [Glomerulus](../../05-tissue/glomerulus/README.md) — glomerular filtration barrier determines urinary albumin loss
- [Podocyte](../../04-cellular/podocyte/README.md) — podocyte foot-process fusion impairs glomerular selectivity → proteinuria → albumin loss
- [IL-6](../il-6/README.md) — negative regulator of albumin synthesis during acute-phase response; IL-6 suppresses ALB mRNA
- [Cortisol](../cortisol/README.md) — partially albumin-bound (~10%); glucocorticoid excess or deficiency alters free cortisol availability

[^stryer-biochemistry]: Berg JM, Tymoczko JL, Stryer L. *Biochemistry.* 9th ed. W.H. Freeman; 2019.
[^alberts-mol-cell-biology]: Alberts B, Johnson A, Lewis J, et al. *Molecular Biology of the Cell.* 7th ed. W.W. Norton; 2022.
