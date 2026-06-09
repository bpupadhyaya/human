---
schema: human-scale-entry/v1
id: leptin
name: Leptin
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-05
summary: "16 kDa adipokine encoded by LEP/ob gene. Signals fat mass to hypothalamus via JAK2/STAT3 → suppresses NPY/AgRP, induces POMC → ↓food intake, ↑energy expenditure. Leptin resistance underlies obesity despite high circulating levels."
aliases: ["OB protein", "adipokine", "satiety hormone", "obesity hormone", "LEP"]
sources:
  - id: stryer-biochemistry
    type: textbook
    cite: "Berg JM, Tymoczko JL, Stryer L. Biochemistry. 9th ed. W.H. Freeman; 2019."
    url: "https://www.macmillanlearning.com/college/us/product/Biochemistry/p/131911467X"
    accessed: "2026-06-05"
  - id: guyton-hall
    type: textbook
    cite: "Hall JE, Hall ME. Guyton and Hall Textbook of Medical Physiology. 14th ed. Elsevier; 2021."
    url: "https://www.elsevier.com/books/guyton-and-hall-textbook-of-medical-physiology/hall/978-0-323-59712-8"
    accessed: "2026-06-05"
cross_links:
  - target: 01-human/07-system/nervous-system
    relation: modulates
    note: "Leptin acts on ARC neurons (suppresses NPY/AgRP, stimulates POMC) via JAK2/STAT3; hypothalamic leptin resistance in obesity impairs satiety; leptin also regulates GnRH, TRH, CRH axes and sympathetic outflow to BAT."
  - target: 01-human/07-system/immune-system
    relation: modulates
    note: "LEPR-Rb on T cells, macrophages, NK cells; leptin promotes Th1 polarisation (↑IFN-γ) and macrophage activation; leptin deficiency impairs immunity; obesity-driven hyperleptinemia promotes chronic low-grade inflammation."
  - target: 01-human/04-cellular/t-helper-cell
    relation: modulates
    note: "Leptin promotes Th1 and Th17 differentiation (STAT3-mediated), inhibits Treg expansion; ob/ob mice have impaired T cell responses; high leptin in obesity skews toward inflammatory phenotypes and adipose macrophage infiltration."
  - target: 01-human/04-cellular/hepatocyte
    relation: modulates
    note: "Leptin signals in hepatocytes via LEPR-Rb → STAT3 → suppresses SREBP-1c (lipogenesis) and promotes fatty acid oxidation (AMPK/CPT1); leptin resistance in NAFLD removes this brake, promoting steatohepatitis progression."
  - target: 01-human/07-system/obesity
    relation: connects-to
    note: "Adipocyte-secreted leptin signals satiety via hypothalamic LepR/JAK2/STAT3; common obesity involves leptin resistance (elevated leptin, impaired STAT3 signaling via SOCS3 upregulation); monogenic LEP deficiency causes morbid childhood obesity treatable with metreleptin."
  - target: 01-human/07-system/anorexia-nervosa
    relation: connects-to
    note: "Leptin falls sharply with fat mass loss in AN → amenorrhea, bone loss, immune suppression, and cognitive impairment; some AN patients have paradoxically elevated leptin relative to weight → false satiety signal; leptin normalizes with sustained weight restoration."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "LEPR-Rb in hypothalamic ARC, DMH, VMH → STAT3 → ↑POMC/CART and ↓NPY/AgRP → ↓appetite and ↑energy expenditure; leptin resistance blunts this; exogenous leptin reverses starvation anovulation and immune suppression; BBB leptin transport saturates at obesity-range concentrations."
  - target: 01-human/07-system/type-2-diabetes
    relation: connects-to
    note: "Leptin resistance in obesity links to T2DM: SOCS3 impairs IRS-1 → convergent blunting of leptin and insulin signalling; hyperleptinemia independently predicts T2DM onset; metformin reduces leptin; bariatric surgery lowers leptin and improves insulin sensitivity."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "Leptin falls during caloric restriction → ↓POMC → ↓α-MSH → ↓melanocortin tone; hyperleptinemia (obesity) associates with depressive symptoms; LEPR polymorphisms associate with MDD risk; leptin restores BDNF and reverses anhedonia in diet-induced obesity rodent models."
---

# Leptin

## Overview

Leptin is a 16 kDa cytokine secreted primarily by white adipocytes in proportion to fat mass. Its discovery by Zhang et al. (1994) — identifying the *ob* gene product mutated in the obese *ob/ob* mouse — was the decisive proof that body fat is an endocrine organ that communicates its size to the hypothalamus [^stryer-biochemistry]. Leptin is the **adiposity signal**: chronically elevated leptin tells the brain that long-term energy stores are sufficient, suppressing appetite and permitting energy-expensive biological functions (reproduction, immunity, growth). When fat stores fall — during starvation, excessive exercise, or lipodystrophy — leptin falls precipitously, triggering a coordinated starvation response: ↑hunger, ↓energy expenditure, ↓fertility, ↓thyroid function, ↓immunity [^guyton-hall].

The tragedy of obesity is that despite dramatically elevated leptin levels (100-fold above lean), the hypothalamus becomes **leptin-resistant** — failing to read the satiety signal. This resistance, mediated by SOCS3 induction, PTP1B upregulation, ↓BBB transport, and LEPR downregulation, perpetuates hyperphagia even in the presence of abundant adipose tissue.

Recombinant leptin (metreleptin) is approved for the rare condition of congenital leptin deficiency and lipodystrophy — where the therapeutic logic is straightforward. In common obesity, leptin therapy has largely failed because resistance blocks its action at the receptor level.

## Structure

Leptin is a member of the **class I cytokine superfamily**, sharing the canonical 4-helix bundle (helices A–D, left-handed antiparallel) with IL-6, CNTF, oncostatin M, and G-CSF, despite minimal sequence similarity:

| Feature | Detail |
|:---|:---|
| **Gene** | *LEP* (also called *ob*), chromosome 7q31.3; 3 exons |
| **Precursor** | 167 aa after 21 aa signal peptide cleavage = 146 aa mature form; UniProt P41159 |
| **Molecular weight** | 16 kDa |
| **Structure** | 4-α-helix bundle; one disulfide bond (Cys96–Cys146) — required for folding and receptor binding |
| **Glycosylation** | Non-glycosylated (unlike EPO or FSH) |
| **Circulating form** | Free (10–50 ng/mL in lean; 20–300+ ng/mL in obese); ~50% bound to soluble LEPR ectodomain at low concentrations; bound fraction ↓ in obesity |

**LEPR (leptin receptor, Ob-R):** Class I cytokine receptor; single-pass transmembrane; six splice isoforms:
- **LEPR-Rb (long form):** intracellular domain with full signalling capacity (Box1/Box2 for JAK2, Tyr985/Tyr1077/Tyr1138 for SOCS3/SHP-2/STAT3 docking); expressed in hypothalamic ARC, DMN, VMH, LHA, brainstem, and immune cells
- **LEPR-a/c/d/e/f (short forms):** truncated intracellular domains; abundant in choroid plexus and brain capillaries — may mediate transcytosis of leptin across the BBB; signalling limited to JAK2 activation only

## Function

Leptin exerts functions across four domains:

**1. Energy homeostasis (primary function):**
- ↑Leptin → hypothalamic LEPR-Rb → ↓food intake, ↑energy expenditure (↑sympathetic tone → BAT UCP1 thermogenesis, ↑heart rate, ↑brown adipose activity)
- Starvation → ↓leptin → 100-fold ↑NPY/AgRP → hyperphagia + ↓metabolic rate (defence of body weight)

**2. Neuroendocrine axis regulation:**
- ↓Leptin → ↓GnRH pulse frequency → ↓LH/FSH → ↓reproductive function (amenorrhoea in female athletes, ↓testosterone in starvation, delayed puberty in leptin-deficient children)
- ↓Leptin → ↓TRH → ↓TSH → ↓T3/T4 → metabolic rate suppression (adaptive hypothyroidism of starvation)
- ↑Leptin → ↑CRH → ↑HPA activation in obesity → chronic cortisol elevation → insulin resistance

**3. Immune function:**
- LEPR-Rb on T lymphocytes, macrophages, DCs, NK cells
- ↑Leptin → Th1 polarisation (↑IL-2, ↑IFN-γ, ↑TNF-α), ↑macrophage phagocytosis, ↑NK cytotoxicity
- ↓Leptin → ↓T cell proliferation, ↑apoptosis → impaired innate and adaptive immunity (ob/ob mice are immunosuppressed)

**4. Metabolic signalling in peripheral tissues:**
- Liver: ↓lipogenesis (↓SREBP-1c), ↑FAO (↑CPT1 via AMPK)
- Muscle: ↑fatty acid oxidation, ↑AMPK activity, insulin sensitisation
- Pancreatic β-cells: LEPR-Rb expressed; leptin → ↓insulin secretion (direct inhibition, counters insulin's adipogenic role in a negative feedback loop)

## Mechanism

### Hypothalamic Arcuate Nucleus Circuit

The arcuate nucleus (ARC) sits adjacent to the median eminence — outside the blood-brain barrier — allowing leptin to access neurons directly. Two opposing first-order neuron populations:

**NPY/AgRP neurons (orexigenic):**
- Constitutively active (fire tonically); release NPY → Y1R/Y5R on PVN → ↑food intake; release AgRP → MC3R/MC4R antagonist → blocks αMSH → ↑food intake; also release GABA → inhibit adjacent POMC neurons
- Leptin → LEPR-Rb → JAK2 → STAT3 (Tyr705) → nucleus → ↓NPY promoter, ↓AgRP transcription; also PI3K/Akt → FoxO1 nuclear exclusion → ↓AgRP
- Also: leptin hyperpolarises NPY/AgRP neurons (via KATP channels) → ↓firing → ↓NPY/AgRP release (rapid, within minutes)

**POMC/CART neurons (anorexigenic):**
- Leptin → STAT3 → ↑POMC transcription → POMC protein cleaved by PC1/3 → αMSH (among other peptides)
- αMSH → MC4R (primary anorectic receptor) on PVN neurons → Gs → ↑cAMP → ↑energy expenditure, ↓food intake
- MC4R mutations (most common monogenic obesity in humans, ~0.5% of severe obese cases) prevent αMSH signalling

**Downstream hypothalamic targets:**
- **PVN:** receives POMC/AgRP input → controls TRH, CRH, oxytocin secretion
- **LHA (lateral hypothalamic area):** orexin/hypocretin and MCH neurons; leptin inhibits MCH (↓food intake) and modulates orexin (↑wakefulness/activity)
- **VMH:** SF-1 neurons; leptin here primarily controls energy expenditure rather than food intake

### JAK2/STAT3 Signalling

1. Leptin binding → LEPR-Rb homodimerisation → JAK2 transphosphorylation (Tyr1007/Tyr1008)
2. Activated JAK2 → LEPR-Rb Tyr1138 → STAT3 docking → STAT3 Tyr705 phosphorylation → STAT3 homodimer → nucleus
3. STAT3 → ↑SOCS3 transcription (negative feedback — SOCS3 binds JAK2 kinase domain → blocks further STAT3 phosphorylation) and ↑POMC, ↓NPY/AgRP
4. Also: LEPR-Rb Tyr985 → SHP-2 → Ras/ERK (proliferative); Tyr985 → IRS-1/2 → PI3K/Akt (metabolic, overlaps insulin signalling)

### Leptin Resistance — Mechanisms

In obesity, leptin levels are elevated but hypothalamic signalling fails:

| Mechanism | Detail |
|:---|:---|
| **SOCS3 induction** | STAT3 → ↑SOCS3 → inhibits JAK2; also impairs IRS-1 → blocks both leptin and insulin signalling (convergent resistance) |
| **PTP1B upregulation** | Tyrosine phosphatase; dephosphorylates JAK2 Tyr1007/1008 → terminates signalling; PTP1B knockout mice are leptin-hypersensitive and resistant to diet-induced obesity |
| **ER stress** | High-fat diet → ER stress in ARC → IKKβ/JNK activation → Ser phosphorylation of IRS-1 → impairs downstream PI3K/Akt |
| **↓BBB transport** | Short LEPR isoforms mediate leptin transport across BBB; transport saturates at high leptin concentrations; CSF leptin/serum leptin ratio ↓ in obesity |
| **↓LEPR-Rb expression** | ARC LEPR-Rb mRNA ↓ in diet-induced obesity → ↓receptor density → ↓signal per unit leptin |

## Connections

- `modulates` → **[nervous-system](../../07-system/nervous-system/README.md)** — leptin acts on ARC NPY/AgRP and POMC neurons via JAK2/STAT3; regulates GnRH, TRH, CRH neuroendocrine axes; sympathetic outflow to BAT; leptin resistance in obesity impairs all these signals
- `modulates` → **[immune-system](../../07-system/immune-system/README.md)** — LEPR-Rb on T cells, macrophages, NK cells; promotes Th1 polarisation and macrophage activation; leptin deficiency causes immunosuppression; obesity hyperleptinemia drives chronic inflammation
- `modulates` → **[t-helper-cell](../../04-cellular/t-helper-cell/README.md)** — leptin promotes Th1/Th17 differentiation via STAT3 and inhibits Treg expansion; ob/ob mice have impaired T cell responses; high leptin in obesity skews toward inflammatory phenotypes
- `modulates` → **[hepatocyte](../../04-cellular/hepatocyte/README.md)** — leptin → LEPR-Rb → STAT3 → ↓SREBP-1c (lipogenesis) and ↑FA oxidation (AMPK/CPT1); leptin resistance in NAFLD removes this anti-steatotic brake, promoting steatohepatitis
- `connects-to` → **[Obesity](../../07-system/obesity/README.md)** — leptin signals satiety via hypothalamic LepR/JAK2/STAT3 proportional to fat mass; common obesity involves leptin resistance (elevated leptin, impaired STAT3 signaling via SOCS3 upregulation); monogenic LEP deficiency causes morbid childhood obesity curable with metreleptin.
- `connects-to` → **[Anorexia Nervosa](../../07-system/anorexia-nervosa/README.md)** — leptin falls sharply with fat mass loss in AN → amenorrhea, bone loss, immune suppression, and cognitive impairment; paradoxically, some AN patients have elevated leptin relative to weight → false satiety; normalizes with weight restoration.
- `connects-to` → **[Brain](../../06-organ/brain/README.md)** — LEPR-Rb in hypothalamic ARC, DMH, VMH → STAT3 → ↑POMC/CART and ↓NPY/AgRP → ↓appetite and ↑energy expenditure; leptin resistance blunts this; exogenous leptin reverses starvation anovulation and immune suppression; BBB leptin transport saturates at obesity-range concentrations.
- `connects-to` → **[Type 2 Diabetes](../../07-system/type-2-diabetes/README.md)** — leptin resistance in obesity links to T2DM: SOCS3 impairs IRS-1 → convergent blunting of leptin and insulin signalling; hyperleptinemia independently predicts T2DM onset; metformin reduces leptin; bariatric surgery lowers leptin and improves insulin sensitivity.
- `connects-to` → **[Major Depressive Disorder](../../07-system/major-depressive-disorder/README.md)** — leptin falls during caloric restriction → ↓POMC → ↓α-MSH → ↓melanocortin tone; hyperleptinemia (obesity) associates with depressive symptoms; LEPR polymorphisms associate with MDD risk; leptin restores BDNF and reverses anhedonia in diet-induced obesity rodent models.

## Pathology

| Condition | Mechanism | Key Features |
|:---|:---|:---|
| **Congenital leptin deficiency** | Homozygous LEP loss-of-function mutations (missense/nonsense; described in Pakistani, Turkish, Egyptian families) → undetectable serum leptin | Severe hyperphagia and early-onset morbid obesity (begins infancy), hypogonadotropic hypogonadism, ↓T cell number/function; remarkable response to metreleptin (recombinant leptin) — normalises weight and reproductive function |
| **Congenital leptin receptor deficiency** | LEPR loss-of-function mutations → same clinical phenotype as LEP deficiency; additionally: GH deficiency, TSH deficiency (central hypothyroidism) | Serum leptin is elevated (not deficient); no response to metreleptin (receptor absent); leptin levels paradoxically high |
| **Lipodystrophy** | Generalised or partial absence of adipose tissue → very low leptin (despite normal or ↑caloric intake) → unrestrained appetite, severe metabolic syndrome, fatty liver, hypertriglyceridemia | Metreleptin approved for generalised lipodystrophy; significant improvement in triglycerides, liver fat, and HbA1c |
| **Common obesity (polygenic)** | Polygenic risk (FTO, MC4R, others) + environment → ↑fat mass → ↑leptin → central leptin resistance → hyperphagia despite high leptin | Serum leptin high; hypothalamic LEPR-Rb signalling impaired; metreleptin ineffective in common obesity; focus on SOCS3/PTP1B as drug targets |
| **Anorexia nervosa / starvation** | ↓Fat mass → ↓leptin → ↑NPY/AgRP (but behavioural override) → ↓GnRH → amenorrhoea, ↓bone density, ↓immunity | Exogenous leptin may restore reproductive function without requiring full weight restoration (research only) |
| **Female athlete triad** | Low energy availability → ↓leptin → ↓GnRH pulses → oligomenorrhoea/amenorrhoea + ↓bone mineral density | Leptin threshold for normal menstrual cycling ~3–4 ng/mL; athletes with body fat <15–17% at risk |

## See Also

- [^stryer-biochemistry] Berg JM, Tymoczko JL, Stryer L. *Biochemistry.* 9th ed. W.H. Freeman; 2019.
- [^guyton-hall] Hall JE, Hall ME. *Guyton and Hall Textbook of Medical Physiology.* 14th ed. Elsevier; 2021.
- Related entries: [insulin](../insulin/README.md), [cortisol](../cortisol/README.md), [il-6](../il-6/README.md), [stat3](../stat3/README.md), [t-helper-cell](../../04-cellular/t-helper-cell/README.md)
