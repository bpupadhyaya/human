---
schema: human-scale-entry/v1
id: endothelial-cell
name: Endothelial Cell
atlas: 01-human
scale: 04-cellular
status: draft
last_reviewed: 2026-06-05
summary: "Squamous cells lining all blood and lymphatic vessels (~350 m² total surface). Regulate vascular tone via eNOS/NO, prevent thrombosis via thrombomodulin/TFPI, control leukocyte trafficking via selectins/ICAM-1, and enable angiogenesis via VEGF/VEGFR2."
aliases: ["EC", "vascular endothelium", "microvascular endothelial cell", "HUVEC"]
sources:
  - id: alberts-mol-cell-biology
    type: textbook
    cite: "Alberts B, Johnson A, Lewis J, et al. Molecular Biology of the Cell. 7th ed. W.W. Norton; 2022."
    url: "https://www.ncbi.nlm.nih.gov/books/NBK26880/"
    accessed: "2026-06-05"
  - id: guyton-hall
    type: textbook
    cite: "Hall JE, Hall ME. Guyton and Hall Textbook of Medical Physiology. 14th ed. Elsevier; 2021."
    url: "https://www.elsevier.com/books/guyton-and-hall-textbook-of-medical-physiology/hall/978-0-323-59712-8"
    accessed: "2026-06-05"
cross_links:
  - target: 01-human/07-system/cardiovascular-system
    relation: part-of
    note: "Endothelial cells line the entire cardiovascular tree (~350 m² surface); regulate vascular tone (eNOS→NO), prevent thrombosis (thrombomodulin, TFPI, PGI₂), recruit leukocytes (E-selectin, ICAM-1, VCAM-1)."
  - target: 01-human/04-cellular/macrophage
    relation: modulates
    note: "Activated EC express E-selectin, P-selectin (from WPBs), ICAM-1, VCAM-1 → capture and guide monocyte/macrophage transmigration into tissues; sinusoidal EC in liver perform endocytosis of colloidal materials."
  - target: 01-human/07-system/immune-system
    relation: modulates
    note: "Endothelial cells are gatekeepers of leukocyte trafficking; ICAM-1/VCAM-1 (NF-κB target) bind LFA-1/VLA-4 on leukocytes; CXCL8 presented on endothelial glycocalyx guides neutrophil/monocyte emigration."
  - target: 01-human/05-tissue/hepatic-lobule
    relation: modulates
    note: "Liver sinusoidal endothelial cells (LSECs) have large fenestrae (100–200 nm), no basement membrane; enable direct plasma-hepatocyte exchange via Space of Disse; LSEC scavenge colloidal waste and modulate hepatic fibrosis."
  - target: 01-human/03-molecular/protein-c
    relation: connects-to
    note: "EPCR (endothelial protein C receptor) on ECs presents PC to thrombin-thrombomodulin → APC generation; EPCR-bound APC signals via PAR-1 → endothelial barrier protection (VE-cadherin), anti-inflammatory (NF-κB↓), anti-apoptotic (PI3K/Akt); EPCR expression falls in septic ECs."
---

# Endothelial Cell

## Overview

The endothelial cell is the **squamous epithelium of the vasculature** — a single continuous monolayer of cells lining the luminal surface of every blood vessel and lymphatic channel in the body. The total endothelial surface area is approximately **350 m²** with a mass of around **1 kg**, making the endothelium one of the largest and most functionally diverse organs in the body [^guyton-hall].

Endothelial cells are not inert bystanders — they are **dynamic signal-processing nodes** that continuously sense haemodynamic forces (shear stress, cyclic stretch), blood-borne signals (hormones, cytokines, growth factors, metabolites), and direct cell-cell contacts, translating these inputs into real-time adjustments of vascular tone, permeability, haemostasis, and leukocyte trafficking [^alberts-mol-cell-biology]. Endothelial dysfunction — the loss of normal anti-inflammatory, anti-thrombotic, and vasodilatory phenotype — is the earliest and most fundamental lesion in atherosclerosis, and a key mediator of tissue injury in sepsis, COVID-19, and diabetes.

## Structure

### Morphology

Endothelial cells are elongated (~50–70 µm long, 10–15 µm wide), **aligned parallel to the direction of blood flow** through mechanosensing mechanisms involving:
- **Primary cilia** — flow sensors expressing polycystin-1/2
- **Glycocalyx** — 0.5–3 µm thick luminal layer of proteoglycans (heparan sulfate, hyaluronan) and glycoproteins that attenuates shear stress to the actin cytoskeleton
- **PECAM-1 (CD31)** — junctional mechanosensor; phosphorylated by shear stress → eNOS activation
- **Integrins** (αvβ3, α5β1) — matrix mechanosensors

Cell thickness varies: **0.2–0.5 µm** in large arteries, **1–2 µm** at capillaries [^guyton-hall].

### Weibel-Palade Bodies (WPBs)

The defining secretory organelle of endothelial cells — rod-shaped (~0.2 × 3 µm) storage granules containing:
- **von Willebrand factor (vWF)** — large multimers organised in characteristic tubular arrays
- **P-selectin** — rapidly mobilised to the cell surface upon WPB exocytosis
- **IL-8 (CXCL8)**, angiopoietin-2 (Ang2), and other pro-inflammatory mediators

WPBs are exocytosed within seconds of stimulation by thrombin, histamine, or reactive oxygen species [^alberts-mol-cell-biology].

### Heterogeneity — Three Structural Types

| Type | Location | Permeability | Key Features |
|:---|:---|:---|:---|
| **Continuous non-fenestrated** | Brain (BBB), heart, muscle, lung | Most restrictive | Claudin-5, occludin, ZO-1 tight junctions; minimal transcytosis |
| **Continuous fenestrated** | Kidney glomerulus, intestinal villi, endocrine glands | Intermediate | 60–80 nm fenestrae with (gut, glands) or without (glomerulus) diaphragm |
| **Discontinuous / Sinusoidal** | Liver, spleen, bone marrow | Most permeable | Large 100–200 nm fenestrae, absent basement membrane; direct plasma access to hepatocytes |

## Function

### 1. Vascular Tone Regulation

Endothelial cells are the **primary source of vasoactive mediators**:

| Mediator | Pathway | Effect |
|:---|:---|:---|
| **NO** (nitric oxide) | eNOS (Ser1177-P by Akt/shear stress/VEGF) → L-Arg + O₂ → NO + citrulline → sGC → cGMP | Vasodilation; anti-platelet; anti-inflammatory |
| **PGI₂** (prostacyclin) | COX-1 → AA → PGH₂ → PGIS → PGI₂ → IP receptor → cAMP | Vasodilation; ↓platelet aggregation |
| **ET-1** (endothelin-1) | Pre-pro-ET-1 → ECE-1 → ET-1 → ET_A/ET_B (Gq) → IP₃ → Ca²⁺ | Potent vasoconstriction |
| **EDHF** | KCa3.1 / KCa2.3 → K⁺ efflux → smooth muscle hyperpolarisation | Vasodilation (especially in small vessels) |

### 2. Haemostasis — Dual-State Control

**Quiescent/antithrombotic state:**
- **Thrombomodulin (TM)**: binds thrombin → activates protein C (APC) → degrades factors Va and VIIIa
- **TFPI**: inhibits FXa and TF:FVIIa complex
- **tPA**: converts plasminogen → plasmin → fibrinolysis
- **Ecto-ADPase (CD39/NTPDase1)**: converts ADP → AMP → adenosine (↓platelet activation)
- **PGI₂**, **NO**: both inhibit platelet aggregation and smooth muscle proliferation

**Activated/prothrombotic state (injury/inflammation):**
- WPB exocytosis → **vWF multimers** (platelet tethering) + **P-selectin** (leukocyte rolling)
- **Tissue factor (TF/CD142)** expression → initiates extrinsic coagulation cascade

### 3. Permeability Barrier

Paracellular permeability is controlled by two junction types:
- **Tight junctions (TJ)**: claudin-5 (most critical in brain), occludin, ZO-1/2 — regulated by PKC, PKA, Rho/ROCK
- **Adherens junctions (AJ)**: VE-cadherin (CD144)/catenin complex — VEGF-A → VEGFR2 → Src → VE-cadherin Tyr658/Y731 phosphorylation → junction opening → vascular leak

Ang1 (Tie2 agonist) → PI3K/Akt → cortactin → VE-cadherin stabilisation → barrier function ↑. Ang2 antagonises Tie2 → junction loosening → angiogenic/inflammatory permissiveness [^alberts-mol-cell-biology].

### 4. Leukocyte Recruitment Cascade

Activated endothelium (TNF-α, IL-1β → NF-κB) sequentially upregulates adhesion molecules:

1. **P-selectin** (minutes; WPB exocytosis) + **E-selectin** (2–6 h; transcription) → **leukocyte rolling** (PSGL-1, CD44)
2. **ICAM-1** + **VCAM-1** (hours; NF-κB) → **firm adhesion** (LFA-1/Mac-1 binding ICAM-1; VLA-4 binding VCAM-1)
3. **Chemokines** (CXCL8 bound to glycocalyx) → integrin activation (inside-out signalling) → **arrest**
4. **PECAM-1**, **JAM** molecules → **transendothelial migration (TEM)** through junctions or transcellularly

### 5. Angiogenesis

New vessel formation follows a tip/stalk cell model driven by VEGF gradient:
- **Tip cells** (highest VEGF signal, DLL4-hi): extend filopodia, migrate toward VEGF source; express VEGFR2 (Flk-1/KDR), Notch ligand DLL4
- **Stalk cells** (Notch-activated by tip DLL4): proliferate to elongate the sprout; express fewer VEGFR2, more VEGFR1 (decoy)
- VEGF-A/VEGFR2 → Erk1/2 (proliferation), PI3K/Akt (survival), PLC→DAG→PKC (permeability, migration)

**Arteriovenous specification**: Notch/EphrinB2 → arterial; COUP-TFII/EphB4 → venous identity.

### 6. Lymphatic Endothelium

Lymphatic endothelial cells (LECs) are phenotypically distinct:
- **Markers**: LYVE-1, PROX1, VEGFR-3, podoplanin, CCRL2
- **Function**: drain interstitial fluid and macromolecules; transport dietary lipids (lacteals); house dendritic cell trafficking to lymph nodes
- **Development**: specified from cardinal vein venous ECs by PROX1, GATA2, FOXC2

## Lifecycle

### Vasculogenesis

During embryonic development, **angioblasts** (EC precursors from lateral plate mesoderm) coalesce in situ to form a primitive vascular plexus (de novo tube formation). In the yolk sac, **hemangioblasts** give rise to both EC and haematopoietic lineages. Key signals: VEGF-A/VEGFR2, FGF2, SCF, CXCL12 [^guyton-hall].

### Angiogenesis and Remodelling

The primitive plexus undergoes:
1. **Sprouting angiogenesis** — tip/stalk selection, filopodia extension, lumen formation
2. **Intussusception** — insertion of tissue pillars to split vessels
3. **Vascular pruning** — elimination of poorly perfused segments by haemodynamic shunting and Ang2/Notch signals

### Quiescence vs. Activation

Adult EC turnover is extremely slow (~years in large vessels). Quiescent EC maintain anti-thrombotic, anti-inflammatory phenotype through:
- Constitutive eNOS, TM, TFPI, CD39 expression
- Laminar shear stress → KLF2/KLF4 transcription factors → eNOS, TM, PGI₂ synthase upregulation
- Low NF-κB activity

Activation (by disturbed flow, inflammation, hypoxia, metabolic dysregulation) shifts EC to pro-inflammatory, pro-thrombotic, angiogenic phenotype.

## Connections

- **Part of** cardiovascular system [→ cardiovascular-system](../../07-system/cardiovascular-system/README.md): Endothelial cells line the entire cardiovascular tree (~350 m² surface); regulate vascular tone (eNOS→NO), prevent thrombosis (thrombomodulin, TFPI, PGI₂), recruit leukocytes (E-selectin, ICAM-1, VCAM-1).
- **Modulates** macrophage [→ macrophage](../../04-cellular/macrophage/README.md): Activated EC express E-selectin, P-selectin (from WPBs), ICAM-1, VCAM-1 → capture and guide monocyte/macrophage transmigration into tissues; sinusoidal EC in liver perform endocytosis of colloidal materials.
- **Modulates** immune system [→ immune-system](../../07-system/immune-system/README.md): Endothelial cells are gatekeepers of leukocyte trafficking into tissues; ICAM-1/VCAM-1 (NF-κB target) bind LFA-1/VLA-4 on leukocytes; CXCL8 presented on endothelial glycocalyx guides neutrophil/monocyte emigration.
- **Modulates** hepatic lobule [→ hepatic-lobule](../../05-tissue/hepatic-lobule/README.md): Liver sinusoidal endothelial cells (LSECs) have large fenestrae (100–200 nm), no basement membrane; enable direct plasma-hepatocyte exchange via Space of Disse; LSEC scavenge colloidal waste and modulate hepatic fibrosis.
- `connects-to` → **[Protein C](../../03-molecular/protein-c/README.md)** — EPCR (endothelial protein C receptor) on ECs presents PC to thrombin-thrombomodulin → APC generation; EPCR-bound APC signals via PAR-1 → endothelial barrier protection (VE-cadherin), anti-inflammatory (NF-κB↓), anti-apoptotic (PI3K/Akt); EPCR expression falls in septic ECs.

## Pathology

| Condition | Mechanism | Key Features |
|:---|:---|:---|
| **Atherosclerosis** | Endothelial dysfunction (↓NO, ↑ROS, ↑ICAM-1) at arterial bends/bifurcations → LDL oxidation → foam cell accumulation → plaque | KLF2 ↓ in disturbed flow; NF-κB ↑; initial lesion is endothelial |
| **COVID-19 endotheliitis** | SARS-CoV-2 infects EC via ACE2/TMPRSS2 → NF-κB activation → cytokine storm, microthrombi | Multiorgan failure; vascular micro-thrombosis; elevated D-dimer, vWF |
| **Hereditary haemorrhagic telangiectasia (HHT)** | Loss-of-function mutations in ENG (endoglin, HHT1) or ACVRL1 (ALK1, HHT2) → impaired BMP9/10 → EC TGF-β signalling | Abnormal AV malformations; mucocutaneous telangiectasias; epistaxis |
| **Von Willebrand disease (VWD)** | vWF quantity/quality defects (WPB content) | Mucocutaneous bleeding; impaired platelet adhesion at high shear |
| **Tumour angiogenesis** | VEGF-A overexpression → pathological sprouting; immature, leaky, tortuous vessels | Impairs drug delivery; anti-VEGF (bevacizumab) normalises vasculature transiently |
| **Septic shock** | LPS/PAMPs → endothelial TLR4 → NF-κB → ↑TF, ↓TM, ↑permeability → DIC + oedema | Glycocalyx shedding (heparanase); vascular leak; multi-organ failure |

## See Also

- [Cardiovascular System](../../07-system/cardiovascular-system/README.md) — the larger vascular circuit the endothelium lines and regulates
- [Macrophage](../../04-cellular/macrophage/README.md) — monocyte/macrophage transmigration is gated by endothelial adhesion molecule expression
- [Hepatic Lobule](../../05-tissue/hepatic-lobule/README.md) — liver sinusoidal endothelial cells (LSECs) have unique fenestrated, basement-membrane-free structure
- [Heart](../../06-organ/heart/README.md) — endocardial endothelium and coronary artery endothelium; coronary EC dysfunction → ischaemic heart disease
- [Hepatocyte](../../04-cellular/hepatocyte/README.md) — hepatocytes exchange metabolites with blood across the LSEC fenestrae via the Space of Disse

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
