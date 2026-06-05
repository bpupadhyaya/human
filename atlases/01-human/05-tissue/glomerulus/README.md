---
schema: human-scale-entry/v1
id: glomerulus
name: Glomerulus
atlas: 01-human
scale: 05-tissue
status: draft
last_reviewed: 2026-06-04
summary: "Tuft of fenestrated capillaries (~8–10 loops) in Bowman's capsule — the nephron's primary filtration unit. Three-layer barrier filters ~180 L/day of plasma at GFR ~125 mL/min. ~1 million glomeruli per adult kidney."
aliases: ["renal glomerulus", "glomerular tuft", "Malpighian corpuscle"]
sources:
  - id: haraldsson-2008-filtration-barrier
    type: peer-reviewed
    cite: "Haraldsson B, Nystrom J, Deen WM. Properties of the glomerular barrier and mechanisms of proteinuria. Physiol Rev. 2008;88(2):451-87."
    doi: "10.1152/physrev.00055.2006"
    pmid: "18391170"
    url: "https://doi.org/10.1152/physrev.00055.2006"
  - id: hall-guyton-14
    type: textbook
    cite: "Hall JE. Guyton and Hall Textbook of Medical Physiology. 14th ed. Elsevier; 2021. Ch. 26-27."
    url: "https://www.elsevier.com/books/guyton-and-hall-textbook-of-medical-physiology/hall/978-0-323-59712-8"
    accessed: "2026-06-04"
  - id: quaggin-kreidberg-2008
    type: peer-reviewed
    cite: "Quaggin SE, Kreidberg JA. Development of the renal glomerulus: good neighbors and good fences. Development. 2008;135(4):609-20."
    doi: "10.1242/dev.001081"
    pmid: "18223199"
    url: "https://doi.org/10.1242/dev.001081"
  - id: kriz-2013-mesangial
    type: peer-reviewed
    cite: "Kriz W, Hackenthal E, Nobiling R, Sakai T, Elger M, Hähnel B. A role for podocytes to counteract capillary wall distension. Kidney Int. 1994;45(2):369-76."
    doi: "10.1038/ki.1994.48"
    pmid: "8164423"
    url: "https://doi.org/10.1038/ki.1994.48"
  - id: tryggvason-2006-nephrin
    type: peer-reviewed
    cite: "Tryggvason K, Patrakka J, Wartiovaara J. Hereditary proteinuria syndromes and mechanisms of proteinuria. N Engl J Med. 2006;354(13):1387-401."
    doi: "10.1056/NEJMra052131"
    pmid: "16571882"
    url: "https://doi.org/10.1056/NEJMra052131"
cross_links:
  - target: 01-human/04-cellular/podocyte
    relation: contains
    note: "Podocytes form the visceral (outer) epithelial layer of the glomerulus, providing the protein-selective slit diaphragm of the filtration barrier."
  - target: 01-human/06-organ/kidney
    relation: part-of
    note: "Each glomerulus is part of a nephron within the kidney cortex; ~1 million glomeruli per adult kidney."
  - target: 01-human/07-system/renal-system
    relation: part-of
    note: "Glomeruli are the tissue-level filtration structures that collectively define the renal system's plasma-filtering capacity (GFR ~125 mL/min in adults)."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "Glomerular filtration is driven by hydrostatic pressure from the renal artery (afferent arteriole ~60 mmHg); the cardiovascular system directly determines GFR."
  - target: 02-pathogen/01-viruses/sars-cov-2
    relation: damaged-by
    note: "SARS-CoV-2 causes glomerulonephritis, collapsing glomerulopathy, and AKI via direct endothelial injury, podocyte damage, and immune complex deposition."
  - target: 01-human/07-system/cardiovascular-system
    relation: modulated-by
    note: "Systemic blood pressure directly modulates glomerular hydrostatic pressure and GFR; hypertension causes glomerular hyperfiltration and eventual glomerulosclerosis."
  - target: 01-human/03-molecular/collagen
    relation: composed-of
    note: "Composed Of by Collagen."
  - target: 01-human/03-molecular/complement-c3
    relation: modulated-by
    note: "Modulated by Complement C3."
  - target: 01-human/03-molecular/albumin
    relation: modulated-by
    note: "Modulated by Albumin."
---

# Glomerulus

## Overview

The glomerulus is the microscopic primary filtration unit of the nephron — a tight tuft of ~8–10 fenestrated capillary loops suspended within the cup-shaped Bowman's capsule at the proximal end of each renal tubule [^hall-guyton-14]. Each human kidney contains approximately one million glomeruli, distributed throughout the renal cortex. Together they filter an astonishing 180 liters of plasma per day — nearly 125 mL per minute — generating the primary urine that is subsequently concentrated, modified, and reabsorbed as it traverses the nephron tubule.

The glomerulus is not merely a passive filter. It is a precisely engineered tissue whose three-layer barrier discriminates between molecules by both size and charge with remarkable selectivity: water, ions, glucose, amino acids, and urea pass freely; albumin (67 kDa, anionic) is retained to 99.97%; larger proteins are virtually completely excluded. This filtration selectivity is the foundation of plasma composition maintenance — failure of glomerular barrier integrity is among the most clinically significant events in nephrology, leading to proteinuria, nephrotic syndrome, and progressive kidney failure [^haraldsson-2008-filtration-barrier].

## Structure

### The Renal Corpuscle

The glomerulus (the capillary tuft itself) sits within **Bowman's capsule**, together forming the **renal corpuscle**. Bowman's capsule has two layers:
- **Parietal epithelium** — simple squamous cells forming the outer wall
- **Visceral epithelium (podocytes)** — specialized cells wrapping the capillaries

The space between the capillaries and Bowman's parietal wall is **Bowman's space** (also called the urinary space), into which the filtrate drains before entering the proximal tubule.

### The Three-Layer Filtration Barrier

Blood entering through the afferent arteriole passes through the filtration barrier (blood → filtrate direction):

**Layer 1 — Fenestrated Endothelium**
The glomerular capillary endothelium is unique: it is perforated by circular fenestrae (pores) 60–100 nm in diameter, which are absent their diaphragm (unlike fenestrated capillaries elsewhere). These pores permit free passage of water and solutes but exclude blood cells and platelets. The endothelial surface is coated with a glycocalyx rich in heparan sulfate proteoglycans (perlecan, glypican), providing a charge-selective electronegativity that repels anionic albumin.

**Layer 2 — Glomerular Basement Membrane (GBM)**
The GBM is a 250–400 nm thick fused basement membrane formed by contributions from both endothelial cells and podocytes. It is the primary structural scaffold of the filtration barrier. Composition:
- **Collagen IV** (predominantly α3α4α5 isoforms — the ones absent in Alport syndrome)
- **Laminin-521** (α5β2γ1) — critical for podocyte and endothelial adhesion
- **Agrin and perlecan** — heparan sulfate proteoglycans providing charge selectivity
- **Nidogen** — crosslinks laminin and collagen IV networks

The GBM acts as both a size barrier (~8 nm Stokes radius maximum passage) and a charge barrier (anionic proteoglycans retard albumin).

**Layer 3 — Podocyte Foot Processes with Slit Diaphragm**
[Podocytes](../../04-cellular/podocyte/README.md) extend interdigitating foot processes that cover the outer GBM surface. The 35–40 nm gaps between adjacent foot processes (filtration slits) are bridged by the **slit diaphragm**, a molecular zipper of nephrin, NEPH1, and podocin that provides final size-selective protein retention [^tryggvason-2006-nephrin].

### Mesangial Cells

The glomerular mesangium — located centrally between capillary loops — contains **mesangial cells**: specialized pericyte-like cells with smooth muscle characteristics. They:
- Provide structural support for capillary loops (maintain the architecture of the tuft)
- Regulate GFR by contracting in response to angiotensin II, endothelin, and vasopressin (reducing filtration surface area)
- Produce mesangial matrix (collagen IV, fibronectin, laminin)
- Phagocytose immune complexes and cellular debris
- Are mesenchymal in origin (unlike the epithelial and endothelial layers)

**IgA nephropathy** — the most common primary glomerulonephritis worldwide — is defined by mesangial IgA immune complex deposition, triggering mesangial inflammation and GFR decline.

### Vascular Architecture

| Vessel | Role |
|:---|:---|
| Afferent arteriole | Delivers blood; tone controls inflow pressure (~60 mmHg hydrostatic in capillary) |
| Glomerular capillaries (8–10 loops) | Filtration surface; fenestrated, high-pressure |
| Efferent arteriole | Drains filtered blood; tone controls outflow pressure and oncotic gradient |
| Peritubular capillaries (from efferent) | Reabsorb reabsorbed filtrate downstream |
| Juxtaglomerular cells (JG cells) | In afferent arteriole wall; secrete renin in response to low perfusion |

The net filtration pressure is governed by the **Starling equation** applied to the glomerulus:
```
Net filtration pressure = (Pcap - Pspace) - (πcap - πspace)
= (60 - 18) - (32 - 0) = +10 mmHg
```
Where Pcap ≈ 60 mmHg, Pspace ≈ 18 mmHg, πcap ≈ 32 mmHg (oncotic pressure of plasma), and πspace ≈ 0 mmHg (protein-free filtrate).

## Function

### Ultrafiltration of Plasma

The glomerulus functions as an ultrafiltration device, producing a protein-free (or nearly so) plasma filtrate from whole blood. At the normal GFR of ~125 mL/min (180 L/day):

- **Freely filtered:** water, Na⁺, K⁺, Cl⁻, HCO₃⁻, glucose, amino acids, urea, creatinine, inulin
- **Partially filtered:** small peptides, β₂-microglobulin
- **Minimally filtered:** albumin (~0.03% passes), IgG
- **Not filtered:** red/white blood cells, platelets, large proteins, protein-bound drugs

The **filtration coefficient (Kf)** = GFR / net filtration pressure. In normal adults, Kf ≈ 12.5 mL/min/mmHg, determined by both hydraulic permeability and filtration surface area (~0.8 m² per kidney).

### GFR Autoregulation

Kidneys maintain remarkably constant GFR (±10%) over a mean arterial pressure range of 80–180 mmHg through two intrinsic mechanisms:
1. **Myogenic response** — afferent arteriole smooth muscle constricts reflexively when stretched by rising blood pressure
2. **Tubuloglomerular feedback (TGF)** — macula densa cells in the distal tubule sense NaCl delivery; high NaCl → adenosine and ATP release → afferent arteriole vasoconstriction → reduced GFR

Beyond this autoregulatory range, GFR tracks blood pressure: hypertension causes hyperfiltration → glomerular injury; hypotension causes prerenal azotemia.

### Endocrine Integration

The juxtaglomerular apparatus (JGA) — comprising juxtaglomerular cells + macula densa + extraglomerular mesangium — is the command center of RAAS activation:
- **Renin release** is triggered by: low renal perfusion pressure, low tubular NaCl (macula densa signal), and sympathetic activation (β1 adrenergic)
- Renin cleaves angiotensinogen → angiotensin I → (ACE) → angiotensin II → vasoconstriction + aldosterone → Na⁺/H₂O retention → blood pressure correction

## Connections

- **Contains:** [Podocyte](../../04-cellular/podocyte/README.md) — the visceral epithelial cell forming the slit diaphragm.
- **Part of:** [Kidney](../../06-organ/kidney/README.md) — one nephron component within the renal parenchyma.
- **Connects to:** [Cardiovascular System](../../07-system/cardiovascular-system/README.md) — systemic BP drives filtration; RAAS from the glomerulus feeds back to the heart and vasculature.
- **Modulated by:** [Cardiovascular System](../../07-system/cardiovascular-system/README.md) — hypertension accelerates glomerular injury; heart failure reduces perfusion → decreased GFR.
- **Damaged by:** SARS-CoV-2 — collapsing glomerulopathy, thrombotic microangiopathy, AKI.

[^haraldsson-2008-filtration-barrier]: Haraldsson B, Nystrom J, Deen WM. Properties of the glomerular barrier and mechanisms of proteinuria. *Physiol Rev.* 2008;88(2):451-87. [doi:10.1152/physrev.00055.2006](https://doi.org/10.1152/physrev.00055.2006) · [PubMed 18391170](https://pubmed.ncbi.nlm.nih.gov/18391170/)
[^hall-guyton-14]: Hall JE. *Guyton and Hall Textbook of Medical Physiology.* 14th ed. Elsevier; 2021. Ch. 26-27.
[^quaggin-kreidberg-2008]: Quaggin SE, Kreidberg JA. Development of the renal glomerulus: good neighbors and good fences. *Development.* 2008;135(4):609-20. [doi:10.1242/dev.001081](https://doi.org/10.1242/dev.001081) · [PubMed 18223199](https://pubmed.ncbi.nlm.nih.gov/18223199/)
[^kriz-2013-mesangial]: Kriz W, Hackenthal E, Nobiling R, Sakai T, Elger M, Hähnel B. A role for podocytes to counteract capillary wall distension. *Kidney Int.* 1994;45(2):369-76. [doi:10.1038/ki.1994.48](https://doi.org/10.1038/ki.1994.48) · [PubMed 8164423](https://pubmed.ncbi.nlm.nih.gov/8164423/)
[^tryggvason-2006-nephrin]: Tryggvason K, Patrakka J, Wartiovaara J. Hereditary proteinuria syndromes and mechanisms of proteinuria. *N Engl J Med.* 2006;354(13):1387-401. [doi:10.1056/NEJMra052131](https://doi.org/10.1056/NEJMra052131) · [PubMed 16571882](https://pubmed.ncbi.nlm.nih.gov/16571882/)
