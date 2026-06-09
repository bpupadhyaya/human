---
schema: human-scale-entry/v1
id: ghrelin
name: Ghrelin
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-07
summary: "Ghrelin (GHRL, chr3p25.3) is the only circulating orexigenic hormone; n-octanoyl Ser3 acylation by GOAT is required for GHSR1a binding; ghrelin → GH release and appetite stimulation; Prader-Willi syndrome has pathologically high ghrelin; anamorelin treats cancer cachexia."
aliases: ["ghrelin", "GHRL", "growth hormone secretagogue", "motilin-related peptide", "des-acyl ghrelin", "appetite hormone"]
cross_links:
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "Ghrelin from gastric fundus X/A cells rises preprandially → vagal GHSR1a → gastric motility (prokinetic); relamorelin (GHSR1a agonist) showed Phase 2b efficacy for diabetic gastroparesis; ghrelin falls after eating, coordinating hunger and gastric emptying."
  - target: 01-human/07-system/type-2-diabetes
    relation: connects-to
    note: "Ghrelin opposes insulin: GHSR1a in pancreatic β cells → reduced insulin secretion; obese T2DM patients have blunted ghrelin suppression after meals; GLP-1 receptor agonists suppress ghrelin surges — contributing to satiety; anamorelin (GHSR1a agonist) treats cancer cachexia."
  - target: 01-human/03-molecular/igf-1
    relation: connects-to
    note: "Ghrelin → hypothalamic arcuate GHSR1a → GHRH release + somatostatin suppression → pituitary GH pulse → hepatic IGF-1 production; ghrelin is the endogenous GH secretagogue; growth hormone secretagogues (MK-677/ibutamoren) act as orally bioavailable GHSR1a agonists to raise IGF-1."
  - target: 01-human/07-system/obesity
    relation: connects-to
    note: "Ghrelin, released by gastric A-like cells during fasting, stimulates appetite via hypothalamic GHSR; ghrelin is paradoxically low in obesity but meal-suppression is blunted; GLP-1 receptor agonists (semaglutide) suppress ghrelin, contributing to appetite and weight reduction."
  - target: 01-human/07-system/bulimia-nervosa
    relation: connects-to
    note: "Ghrelin is elevated in BN during restriction phases → amplifies binge trigger via GHSR1a/NPY axis; post-meal ghrelin suppression is impaired in BN, failing to terminate binge episodes; ghrelin-NPY drive is central to restriction-binge cycling in BN."
  - target: 01-human/07-system/binge-eating-disorder
    relation: connects-to
    note: "Fasting ghrelin is elevated in BED; post-meal ghrelin suppression is blunted, failing to terminate binge episodes; ghrelin drives NPY/AgRP cravings for high-calorie food; GOAT inhibitors are under investigation for BED."
sources:
  - id: kojima-1999-ghrelin
    type: peer-reviewed
    cite: "Kojima M, Hosoda H, Date Y, Nakazato M, Matsuo H, Kangawa K. Ghrelin is a growth-hormone-releasing acylated peptide from stomach. Nature. 1999;402(6762):656-660."
    doi: "10.1038/45230"
    pmid: "10604470"
    url: "https://doi.org/10.1038/45230"
  - id: camilleri-2013-relamorelin
    type: peer-reviewed
    cite: "Camilleri M, Acosta A, Busciglio I, et al. Effect of relamorelin on gastrointestinal transit and symptoms in diabetic gastroparesis. Neurogastroenterol Motil. 2014;26(10):1452-1462."
    doi: "10.1111/nmo.12408"
    pmid: "25167781"
    url: "https://doi.org/10.1111/nmo.12408"
---

# Ghrelin

## Overview

**Ghrelin** (gene *GHRL*, chromosome 3p25.3) is the **only known circulating orexigenic (appetite-stimulating) hormone** — a 28-amino acid acylated peptide secreted predominantly by **X/A-like enteroendocrine cells** in the fundus of the stomach, with smaller contributions from the duodenum, jejunum, and hypothalamus. Discovered in 1999 by Kojima et al. [^kojima-1999-ghrelin] while searching for the endogenous ligand of the "growth hormone secretagogue receptor" (GHSR1a), ghrelin is now recognized as a **master coordinator of energy homeostasis** — rising preprandially to signal hunger, orchestrating GH pulses for anabolic metabolism, enhancing gastric motility to prepare for feeding, and functioning as a counterpart to leptin's satiety signal.

The defining biochemical feature of active ghrelin is the **n-octanoyl modification on Serine 3** — added by **ghrelin O-acyltransferase (GOAT; MBOAT4 gene)** in the ER of X/A cells before secretion. This octanoylation is essential for GHSR1a binding and all classical ghrelin actions (GH release, appetite stimulation, gastric motility). Des-acyl ghrelin (the unmodified form; ~90% of circulating ghrelin) does not bind GHSR1a and has distinct, less-characterized metabolic effects.

**Three major clinical contexts:**
1. **Pathological hyperghrelin** — Prader-Willi syndrome: extremely high circulating ghrelin (1.5–4× normal) despite obesity → insatiable hyperphagia → severe obesity; GLP-1 agonists modestly suppress ghrelin in PWS
2. **Cancer cachexia / anorexia** — GHSR1a agonists (anamorelin) approved in Japan 2021, under EMA review for cancer anorexia-cachexia syndrome; improved appetite and lean mass
3. **Gastroparesis** — ghrelin's prokinetic effect on GHSR1a in enteric neurons → treatment target; relamorelin (ulimorelin) in clinical trials for diabetic and post-surgical gastroparesis

## Structure

**Ghrelin peptide processing:**
Pre-pro-ghrelin (117 aa, signal peptide + pro-ghrelin + obestatin C-terminus):
1. Signal peptide (23 aa) cleavage → **Pro-ghrelin (94 aa)**
2. GOAT (ghrelin O-acyltransferase, membrane-bound ER enzyme) catalyzes **transfer of n-octanoic acid (C8:0) → Ser3** hydroxyl group → n-octanoyl-pro-ghrelin
3. Prohormone convertase 1/3 (PC1/3) cleaves after position 28 → mature **Acyl-ghrelin (28 aa)** + C-terminal fragment (obestatin)
4. **Obestatin** (23 aa): initially proposed as appetite-suppressing (GPR39 ligand); later evidence weakened; physiological role uncertain

**Mature ghrelin structure (28 aa):**
- Sequence: GSSFLSPEHQRVQQRKESKKPPAKLQPR (human)
- **Gly1-Ser2-Ser3(n-octanoyl)-Phe4-Leu5-Ser6-...:** N-terminal region (aa 1-5) is critical for GHSR1a binding; Phe4 and Leu5 are the primary hydrophobic receptor contacts; the octanoyl chain on Ser3 penetrates the GHSR1a transmembrane bundle
- **Phe4Ala substitution:** completely abolishes GHSR1a binding
- Circulating forms: ~10% active acyl-ghrelin; ~90% des-acyl ghrelin (inactive for GHSR1a); enzymatic deacylation by butyrylcholinesterase (BuChE) and paraoxonase-1 in blood

**GHSR1a (Growth Hormone Secretagogue Receptor type 1a; GHSR gene, chr3q26.31):**
- Class A (rhodopsin-like) GPCR; 7 TM helices; 366-aa
- **GHSR1a** = full-length, functional receptor; **GHSR1b** = truncated 5-TM splice variant, does not traffic to membrane, dominant-negative regulator
- Coupling: Gq/G11 → PLC → IP3 → Ca²⁺ + DAG → PKC (primary; rapid); also Gi → ↓cAMP; β-arrestin 1/2 → internalization and biased signaling
- **Constitutive activity:** GHSR1a has ~50% basal activity without ligand — one of the highest constitutive activity GPCRs; pharmacological implications for inverse agonist development
- Expression: pituitary somatotrophs (GH cells), hypothalamic arcuate nucleus (NPY/AgRP neurons), nucleus tractus solitarius, vagal afferent neurons, dorsal vagal complex, pancreatic islets, cardiac tissue

**GOAT (ghrelin O-acyltransferase; MBOAT4 gene, chr8p12):**
- Membrane-bound polytopic enzyme in ER; member of membrane-bound O-acyltransferase (MBOAT) family (also includes HHAT for Hedgehog palmitoylation)
- Transfers octanoyl-CoA (C8:0) OR decanoyl-CoA (C10:0) → Ser3 of pro-ghrelin; octanoylation is the dominant modification
- GOAT inhibitors (GO-CoA-Tat, GLWL-01) reduce active ghrelin → reduce food intake in diet-induced obese mice; in clinical development for obesity

## Function

**Appetite and energy homeostasis:**
1. **Preprandial rise:** Ghrelin peaks 30-60 min before anticipated meal time (circadian entrained) → acyl-ghrelin → arcuate nucleus NPY/AgRP neurons (GHSR1a highly expressed) → rapid NPY/AgRP mRNA upregulation + immediate neuropeptide release
2. **NPY/AgRP → downstream circuits:** Lateral hypothalamus (orexin neurons) → feeding behavior; paraventricular nucleus → sympathetic activity reduction → energy conservation
3. **Postprandial suppression:** Nutrient-induced → ghrelin rapidly falls within 20-30 min of meal onset (glucose, fat, protein all suppress; glucose most potent) → hunger signal terminated
4. **Ghrelin in obesity:** Paradoxically LOW in obese individuals (not high as intuition suggests); fails to show normal preprandial rise → may reflect downregulated gastric X/A cell response to chronic nutrient excess; ghrelin suppression after gastric bypass is dramatically enhanced → contributing to weight loss benefit beyond restriction

**GH secretagogue action:**
1. Ghrelin → GHSR1a in pituitary somatotrophs → Gq → Ca²⁺ → GH granule exocytosis; AND arcuate → GHRH neurons → enhanced GHRH release; somatostatin suppression
2. Acts **synergistically** with GHRH — ghrelin alone or GHRH alone gives modest GH; together → supra-additive GH pulse amplitude
3. **Pharmacological application:** MK-677 (ibutamoren) — oral non-peptide GHSR1a agonist; raises GH and IGF-1 chronically; used investigationally for sarcopenia, GH deficiency, Alzheimer's disease (IGF-1 neuroprotection hypothesis)

**Gastric motility (prokinetic):**
- GHSR1a on enteric neurons (Auerbach/Meissner plexus) and vagal afferents → enhanced antral motility → accelerated gastric emptying
- Ghrelin is the endogenous **motilin-like prokinetic** for the stomach; motilin (a related peptide) acts similarly in the intestine (erythromycin is a motilin agonist)
- Diabetic gastroparesis: hyperglycemia → oxidative stress → loss of enteric NO-producing neurons → delayed emptying; GHSR1a agonists (relamorelin) compensate by enhancing antral contractions [^camilleri-2013-relamorelin]

**Anti-inflammatory effects:**
- GHSR1a in macrophages and immune cells → ghrelin → reduced NF-κB activity → decreased TNF-α, IL-6, IL-1β production; ghrelin is protective in rodent sepsis and IBD models; mechanism: Gq → PLC → PKC → β-arrestin 2 → suppression of NF-κB nuclear translocation
- **Vagal anti-inflammatory reflex:** Ghrelin → dorsal motor nucleus of vagus → cholinergic efferents → α7 nAChR on macrophages → acetylcholine-mediated immune suppression (overlapping with the cholinergic anti-inflammatory reflex)

## Mechanism

**Anamorelin in cancer cachexia:**
- GHSR1a agonist; approved Japan 2021 (Adlumiz) for cancer anorexia-cachexia in NSCLC, gastric, pancreatic, colorectal cancer; EMA review ongoing
- ROMANA 1 and 2 Phase 3 trials: anamorelin 100 mg orally QD vs. placebo in NSCLC with cachexia
- Lean body mass: +0.99 kg vs. -0.47 kg (p<0.001); handgrip strength: +0.83 vs. -0.37 kg (not statistically significant); improved appetite and quality-of-life scores
- FDA has not approved anamorelin for cancer cachexia; FDA endpoints include muscle function, not just lean mass

**Prader-Willi syndrome and ghrelin:**
- PWS (maternal imprinting disorder; chr15q11-q13 paternal deletion or maternal UPD): hypotonia, hyperphagia, obesity, hypogonadism, cognitive impairment
- Ghrelin is 4–5× higher in PWS than weight-matched obese controls → does not fall normally after meals → persistent hunger drive
- Mechanism: hypothalamic dysfunction + increased X/A cell secretion; GLP-1 agonists (exenatide, semaglutide) modestly reduce ghrelin and hyperphagia in PWS (Phase 2 data)
- GOAT inhibition is a theoretical PWS target (reduce active ghrelin at source)

**Bariatric surgery and ghrelin:**
- Sleeve gastrectomy removes 70-80% of gastric fundus → removes major ghrelin-producing tissue → dramatic reduction in ghrelin postoperatively → contributes to weight loss (distinct from RYGB)
- Roux-en-Y gastric bypass (RYGB): ghrelin suppression is less pronounced than sleeve, but ghrelin response to meals is altered; enhanced GLP-1/GIP/PYY responses may dominate over ghrelin normalization

## Connections

Ghrelin from gastric fundus X/A cells rises preprandially → vagal GHSR1a → gastric motility (prokinetic); ghrelin levels fall sharply after eating; relamorelin (GHSR1a agonist) showed Phase 2b efficacy for diabetic gastroparesis; ghrelin links satiety signaling and gastric emptying.

Ghrelin opposes insulin: GHSR1a in pancreatic β cells → reduced insulin secretion; obese T2DM patients have blunted ghrelin suppression after meals; GLP-1 receptor agonists suppress ghrelin surges — contributing to satiety; anamorelin (GHSR1a agonist) treats cancer cachexia.

Ghrelin → hypothalamic arcuate GHSR1a → GHRH release + somatostatin suppression → pituitary GH pulse → hepatic IGF-1 production; ghrelin is the endogenous GH secretagogue; growth hormone secretagogues (MK-677/ibutamoren) act as orally bioavailable GHSR1a agonists to raise IGF-1.

Ghrelin, released by gastric A-like cells during fasting, stimulates appetite via hypothalamic GHSR; ghrelin is paradoxically low in common obesity but meal-suppression response is blunted; GLP-1 receptor agonists (semaglutide) suppress ghrelin release, contributing to weight reduction in obesity treatment.

Ghrelin is elevated in BN during restriction phases → amplifies binge trigger via GHSR1a/NPY axis; post-meal ghrelin suppression is impaired in BN, failing to terminate binge episodes; ghrelin-NPY drive is central to restriction-binge cycling in BN.

Fasting ghrelin is elevated in BED patients vs. non-binge-eating controls matched for weight; post-meal ghrelin suppression is blunted in BED — the normal "stop eating" signal fails to terminate binge episodes; ghrelin drives NPY/AgRP-mediated cravings for high-calorie foods; GOAT inhibitors are under investigation as a pharmacological approach to BED.

[^kojima-1999-ghrelin]: Kojima M, Hosoda H, Date Y, Nakazato M, Matsuo H, Kangawa K. Ghrelin is a growth-hormone-releasing acylated peptide from stomach. *Nature.* 1999;402(6762):656-660. [doi:10.1038/45230](https://doi.org/10.1038/45230) · [PubMed 10604470](https://pubmed.ncbi.nlm.nih.gov/10604470/)
[^camilleri-2013-relamorelin]: Camilleri M, Acosta A, Busciglio I, et al. Effect of relamorelin on gastrointestinal transit and symptoms in diabetic gastroparesis. *Neurogastroenterol Motil.* 2014;26(10):1452-1462. [doi:10.1111/nmo.12408](https://doi.org/10.1111/nmo.12408) · [PubMed 25167781](https://pubmed.ncbi.nlm.nih.gov/25167781/)
