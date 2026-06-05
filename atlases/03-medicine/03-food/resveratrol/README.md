---
schema: medicine-entry/v1
id: resveratrol
name: Resveratrol
atlas: 03-medicine
scale: 03-food
status: draft
last_reviewed: 2026-06-05
summary: "Stilbenoid polyphenol from grape skin and red wine; SIRT1 activator driving anti-inflammatory and mitochondrial biogenesis effects; phytoestrogen; poor oral bioavailability limits clinical translation despite promising preclinical data."
aliases: ["resveratrol", "trans-resveratrol", "trans-3,5,4'-trihydroxystilbene", "3,5,4'-stilbenetriol", "Veri-te", "pterostilbene precursor analogue", "grape polyphenol"]
sources:
  - id: baur-2006-resveratrol-nature
    type: peer-reviewed
    cite: "Baur JA, Pearson KJ, Price NL, et al. Resveratrol improves health and survival of mice on a high-calorie diet. Nature. 2006;444(7117):337-342."
    doi: "10.1038/nature05354"
    pmid: "17086191"
    url: "https://doi.org/10.1038/nature05354"
  - id: walle-2004-bioavailability
    type: peer-reviewed
    cite: "Walle T, Hsieh F, DeLegge MH, Oatis JE Jr, Walle UK. High absorption but very low bioavailability of oral resveratrol in humans. Drug Metab Dispos. 2004;32(12):1377-82."
    doi: "10.1124/dmd.104.000885"
    pmid: "15333514"
    url: "https://doi.org/10.1124/dmd.104.000885"
  - id: cochrane-resveratrol-meta
    type: review
    cite: "Cochrane Database of Systematic Reviews. Various systematic reviews available at cochranelibrary.com"
    url: "https://www.cochranelibrary.com/"
    accessed: "2026-06-05"
  - id: stryer-biochemistry
    type: textbook
    cite: "Berg JM, Tymoczko JL, Stryer L. Biochemistry. 9th ed. W.H. Freeman; 2019."
    url: "https://www.macmillanlearning.com/college/us/product/Biochemistry/p/131911467X"
    accessed: "2026-06-05"
cross_links:
  - target: 01-human/07-system/cardiovascular-system
    relation: modulates
    note: "Resveratrol activates SIRT1 and AMPK in vascular endothelium, reducing oxidative stress, improving endothelial NO bioavailability, and attenuating atherosclerotic plaque progression in animal models."
  - target: 01-human/03-molecular/nf-kb
    relation: modulates
    note: "SIRT1-mediated deacetylation of RelA/p65 suppresses NF-κB transcriptional activity; resveratrol also stabilizes IκBα, reducing downstream cytokine gene expression in immune and epithelial cells."
  - target: 01-human/04-cellular/macrophage
    relation: modulates
    note: "Resveratrol polarizes macrophages toward an M2 anti-inflammatory phenotype via SIRT1/PGC-1α axis, reducing TNF-α and IL-6 secretion while increasing IL-10 output in LPS-stimulated models."
  - target: 01-human/06-organ/liver
    relation: modulates
    note: "Resveratrol activates hepatic SIRT1, promoting fatty acid oxidation via PGC-1α/PPARα, reducing steatosis in NAFLD models; also inhibits hepatic stellate cell activation, limiting fibrosis progression."
---

# Resveratrol

## Overview

**Resveratrol** (*trans*-3,5,4'-trihydroxystilbene, C₁₄H₁₂O₃, MW 228.2 Da) is a stilbenoid polyphenol produced by plants as a phytoalexin — a stress-response compound synthesised in response to pathogen attack, UV irradiation, drought, and mechanical injury. It belongs to the stilbene chemical class, characterised by two aromatic rings connected by a trans-ethylene bridge. The *trans* isomer is the biologically predominant form; the *cis* isomer is less stable and less studied.

**Primary dietary sources:**
- **Grape skin and seeds:** 50–100 µg/g fresh weight; predominantly in the skin of red and purple varieties (Muscadine, Pinot Noir, Merlot)
- **Red wine:** 0.1–14.3 mg/L (*trans*-resveratrol); significant variation by wine style, region, and vintage; white wines contain far less due to minimal skin contact during fermentation
- **Blueberries and bilberries:** 16–100 µg/g fresh weight; lower than grapes but significant in diet
- **Peanuts and peanut butter:** 0.02–1.79 µg/g; boiled peanuts contain more than dry-roasted
- **Japanese knotweed (*Fallopia japonica*):** Extremely high concentrations (up to 0.5% dry weight) — the primary botanical source for commercial resveratrol supplements
- **Dark chocolate / cocoa:** Trace amounts; consumed in sufficient quantity, minor contributor

The **French Paradox** — the observation of relatively low cardiovascular mortality in France despite high dietary saturated fat intake — was proposed in the early 1990s (Renaud and de Lorgeril, 1992) to partly reflect resveratrol-containing red wine consumption, driving enormous research interest. This hypothesis remains controversial; alcohol itself, overall dietary patterns (Mediterranean diet elements), and reporting biases are likely major confounders.

**Xenohormesis hypothesis:** Resveratrol exemplifies xenohormesis — the concept that compounds produced by plants under stress activate conserved survival/stress-response pathways in animals consuming them. A stressed plant producing resveratrol signals environmental adversity; herbivores consuming stressed plants gain advance warning and activate their own longevity-promoting stress responses (Howitz and Sinclair, 2004). This elegant hypothesis provides evolutionary rationale but is difficult to test directly in humans.

Commercially, resveratrol is standardised from Japanese knotweed root extract and sold as supplements typically at 100–500 mg per serving — concentrations orders of magnitude above those achievable by food consumption.

## Mechanism

### SIRT1 Activation — Primary Pathway

The most cited mechanism of resveratrol is activation of **SIRT1** (Sirtuin-1), a NAD⁺-dependent protein deacetylase and class III histone deacetylase (HDAC):

1. **Allosteric activation:** Resveratrol binds the SIRT1 enzyme at an allosteric site (N-terminal STAC-binding domain), enhancing substrate binding affinity and increasing deacetylase catalytic rate. This mechanism requires a hydrophobic motif in the substrate; early concerns about an assay artefact (fluorophore-dependent activation) have been partially resolved — resveratrol does activate SIRT1 in cell-free and cellular systems with native substrates
2. **Key SIRT1 substrates deacetylated by resveratrol-activated SIRT1:**
   - **PGC-1α** (PPARG coactivator 1-alpha): deacetylation activates PGC-1α → ↑mitochondrial biogenesis (via NRF1, TFAM), ↑fatty acid oxidation (via PPARα), ↑OXPHOS gene expression; phenocopies aspects of caloric restriction
   - **RelA/p65 (NF-κB):** deacetylation at Lys-310 reduces transcriptional activity → ↓TNF-α, ↓IL-6, ↓IL-1β, ↓COX-2
   - **p53:** deacetylation regulates p53 activity (complex: pro-apoptotic in some contexts, survival-promoting in others)
   - **FOXO3a:** deacetylation activates FOXO3a → ↑antioxidant gene expression (catalase, SOD2, GADD45), ↑autophagy
3. **NAD⁺ dependence:** SIRT1 activity is critically NAD⁺-dependent; resveratrol's effect may be amplified or diminished depending on cellular NAD⁺/NADH ratio; this links resveratrol's mechanism to AMPK activation (AMPK ↑NAD⁺ via ↑NAMPT) [^baur-2006-resveratrol-nature]

### AMPK Activation (Indirect/Downstream)

- Resveratrol activates **AMPK** (AMP-activated protein kinase) by inhibiting mitochondrial Complex I (at high concentrations), raising AMP/ATP ratio → AMPK activation by LKB1 phosphorylation
- Activated AMPK → ↑SIRT1 activity (via ↑NAD⁺ from ↑NAMPT), ↑fatty acid oxidation (via ACC phosphorylation), ↓mTOR → ↑autophagy, ↑mitochondrial biogenesis
- This SIRT1-AMPK positive feedback loop may underlie resveratrol's caloric restriction-mimicking phenotype in animal studies

### NF-κB Inhibition

- SIRT1-mediated deacetylation of RelA/p65 at Lys-310 directly suppresses NF-κB transcriptional activity
- Resveratrol independently stabilises IκBα by inhibiting its phosphorylation (IKKβ inhibition, though weaker than curcumin)
- Net effect: ↓TNF-α, ↓IL-6, ↓IL-8, ↓MCP-1, ↓VCAM-1, ↓ICAM-1 (endothelium) — anti-inflammatory and anti-atherosclerotic transcriptional profile

### Anti-cancer Mechanisms (SIRT1/p300 Axis)

- SIRT1 deacetylates p53 at Lys-382; resveratrol-mediated SIRT1 activation lowers p53 acetylation, affecting p53's transcriptional activity in a context-dependent manner
- Resveratrol ↑Bax and ↓Bcl-2 expression → shifted apoptotic balance toward cell death in cancer cell lines
- ↑p21 (CDKN1A) expression → G1/S cell cycle arrest
- **These mechanisms are established in cell culture; clinical anti-cancer evidence in humans is lacking**

### Phytoestrogenic Activity (ER-α/β)

- Resveratrol binds estrogen receptors (ERα and ERβ) with weak affinity (IC₅₀ ~10,000-fold weaker than 17β-estradiol) → selective estrogen receptor modulator (SERM)-like activity
- ERβ selectivity: resveratrol preferentially activates ERβ over ERα — potentially anti-proliferative in breast cancer (opposite of ERα-driven effects)
- Clinical relevance in hormone-sensitive conditions (breast cancer, menopause) is debated; very low affinity suggests minimal in vivo hormonal effect at standard doses

### Antiplatelet and Cardiovascular Mechanisms

- **COX-1 inhibition:** Resveratrol inhibits COX-1 at high concentrations → reduced thromboxane A₂ (TXA₂) synthesis → antiplatelet effect (analogous to aspirin mechanism but far weaker)
- **eNOS upregulation:** SIRT1-mediated deacetylation of eNOS (endothelial nitric oxide synthase) at Lys-496/Lys-506 increases eNOS activity → ↑NO → vasodilation and ↓platelet aggregation
- **SIRT1-AMPK-eNOS axis:** A key proposed cardiovascular mechanism linking resveratrol's SIRT1 activation to endothelial NO bioavailability and vascular tone

### Bioavailability — The Major Limitation

Resveratrol has extremely poor oral bioavailability despite high intestinal absorption: [^walle-2004-bioavailability]
- Intestinal absorption: ~70% of a dose is absorbed (high)
- **Rapid first-pass glucuronidation and sulfation** in intestinal enterocytes (UGT1A1, UGT1A6, SULT1A1): >99% of absorbed resveratrol is converted to conjugates (resveratrol-3-O-glucuronide, resveratrol-3-sulfate, resveratrol-4'-sulfate) before reaching systemic circulation
- **Systemic free resveratrol bioavailability: <1%** — plasma free resveratrol after 25 mg oral dose is ≈5–10 ng/mL, declining rapidly (t₁/₂ ~1–3 h)
- **Pharmacokinetic mismatch:** Most in vitro mechanistic studies used 1–100 µM resveratrol; peak plasma free concentrations after standard doses are ~30–100 nM — 100–1000-fold below effective in vitro concentrations
- **Conjugates may have partial activity** and undergo enterohepatic recycling; microbiome resveratrol metabolism generates additional metabolites (dihydroresveratrol, lunularin) of uncertain bioactivity
- **Micronised, liposomal, and nano-encapsulated formulations** improve Cmax modestly; the Longevinex formulation claims enhanced bioavailability but independent clinical pharmacokinetic validation is limited

**CYP3A4/2C9 inhibition:** Resveratrol inhibits CYP3A4 and CYP2C9 in vitro; potential drug interactions with warfarin, statins, ciclosporin — clinically relevant at high supplement doses (500 mg/day+).

## Clinical Use

### Therapeutic Areas Under Investigation

| Indication | Typical dose studied | Key findings | Evidence quality |
|:---|:---|:---|:---|
| Cardiovascular risk / endothelial function | 150–1000 mg/day | Small improvements in flow-mediated dilation; inconsistent effects on lipids or BP | Low–moderate |
| Type 2 diabetes / insulin sensitivity | 150–500 mg/day | Modest HbA1c and fasting glucose reductions in some RCTs | Low |
| NAFLD / NASH | 300–500 mg/day | Some improvement in ALT, steatosis on ultrasound | Low |
| Metabolic syndrome | 150–500 mg/day | Improvements in inflammatory biomarkers (CRP, IL-6); inconsistent metabolic effects | Low |
| Cognitive ageing | 200 mg/day | One RCT: improved memory performance; not replicated consistently | Low |
| Cancer prevention | Not established | No clinical endpoint data | Insufficient |

### Populations Studied

- Healthy overweight/obese adults (metabolic studies)
- Type 2 diabetes patients
- Post-menopausal women
- Elderly with mild cognitive decline
- NAFLD/metabolic syndrome cohorts

### Safety Profile

- **Generally well-tolerated** at doses up to 1 g/day in most short-term trials
- **GI adverse effects** (nausea, diarrhoea) at doses >2.5 g/day
- Theoretical concerns: antiplatelet effect (avoid pre-operatively or with anticoagulants); CYP inhibition (drug interactions at high doses); phytoestrogen activity (caution in hormone-sensitive conditions — though evidence for clinical hormonal effect is weak)
- **No established therapeutic dose** for any indication; regulatory status: dietary supplement (GRAS in food, widely sold as supplement)

### Drug Interactions

- **Warfarin:** CYP2C9 inhibition may increase warfarin exposure → elevated INR; monitor
- **Statins:** CYP3A4 inhibition may increase simvastatin, atorvastatin, lovastatin AUC → myopathy risk at high resveratrol doses (>500 mg/day)
- **Antiplatelet drugs:** Additive antiplatelet effect; caution with aspirin, clopidogrel, NSAIDs, heparin
- **Ciclosporin:** CYP3A4 inhibition → increased ciclosporin toxicity

## Evidence

### Landmark Preclinical Study

Baur et al. (2006, Nature) — the foundational paper driving resveratrol's scientific prominence: [^baur-2006-resveratrol-nature]
- High-calorie-diet mice treated with resveratrol (22 mg/kg/day) showed improved survival (vs. untreated high-calorie), better insulin sensitivity, increased mitochondrial biogenesis, reduced hepatic steatosis, and phenotypic resemblance to caloric-restriction mice
- Mechanism attributed to SIRT1 activation → PGC-1α deacetylation
- **Limitation:** Murine doses far exceed human equivalent doses; mice metabolise resveratrol differently; landmark but not directly translatable

### Human RCTs

**Cardiovascular/endothelial:**
- Timmers et al. (2011, Cell Metab): 150 mg/day resveratrol for 30 days in healthy obese men — ↓metabolic rate, ↑AMPK, ↑SIRT1 activity in muscle biopsies, ↑mitochondrial density. Promising but small (n=11 crossover)
- Crandall et al. (2012): 100–2500 mg/day in elderly type 2 diabetes — modest improvements in insulin sensitivity but dose-dependent GI tolerability issues
- Multiple small RCTs of flow-mediated dilation (FMD): inconsistent, with some showing improvement at 75–300 mg/day and others null

**Diabetes/metabolic:**
- Meta-analysis (Liu et al., 2014, Am J Clin Nutr): pooled analysis of 9 RCTs — resveratrol significantly reduced fasting glucose (−5.9 mg/dL, 95% CI −11.2 to −0.5) and insulin resistance (HOMA-IR −0.38) vs. placebo
- However, many individual trials were small (n<30), short (<3 months), and heterogeneous in formulation

**Overall clinical evidence quality:**
- GRADE assessment: **Low for most indications** — small samples, short durations, formulation heterogeneity, inconsistent primary endpoints, limited mechanistic biomarker validation in humans
- No large-scale, adequately powered Phase III RCT demonstrating clinical outcome benefit (mortality, cardiovascular events, diabetes incidence)
- The CALERIE-2 trial (caloric restriction) provided context that caloric restriction's benefits in humans may not be replicated by SIRT1-activating compounds alone

### Bioavailability-Enhancement Formulations

Emerging trials with micronised resveratrol (particle size reduction → ↑dissolution), liposomal, or nanoparticle formulations report improved Cmax and AUC. The RESV-BIOHANCE formulation (SRT-501) achieved higher plasma levels but a clinical trial in multiple myeloma was halted due to renal adverse events at high doses. The field continues to investigate formulation strategies to close the pharmacokinetic gap.

## Connections

- **Modulates** → [Cardiovascular System](../../../../../01-human/07-system/cardiovascular-system/README.md): Resveratrol's SIRT1/AMPK/eNOS axis improves endothelial NO bioavailability and reduces vascular oxidative stress; COX-1 inhibition limits TXA₂-mediated platelet aggregation; animal models show consistent anti-atherosclerotic effects, but human clinical trials demonstrating improved cardiovascular outcomes remain elusive due to bioavailability limitations.

- **Modulates** → [NF-κB](../../../../../01-human/03-molecular/nf-kb/README.md): SIRT1-mediated deacetylation of RelA/p65 at Lys-310 is the dominant mechanism by which resveratrol attenuates NF-κB transcriptional activity; independent IκBα stabilisation via IKKβ inhibition provides additional suppression of downstream cytokine gene expression in immune and epithelial cell contexts.

- **Modulates** → [Macrophage](../../../../../01-human/04-cellular/macrophage/README.md): Resveratrol polarises macrophages toward an M2 anti-inflammatory phenotype via SIRT1/PGC-1α-mediated metabolic reprogramming, reducing TNF-α and IL-6 while increasing IL-10 secretion; this shift reduces foam cell formation in atherosclerosis and attenuates adipose tissue inflammation in obesity models.

- **Modulates** → [Liver](../../../../../01-human/06-organ/liver/README.md): Hepatic SIRT1 activation promotes fatty acid oxidation through PGC-1α/PPARα transcriptional co-activation, reducing hepatic lipid accumulation in NAFLD; resveratrol additionally inhibits TGF-β-mediated hepatic stellate cell activation, limiting collagen deposition and fibrosis progression in experimental liver injury models.

[^baur-2006-resveratrol-nature]: Baur JA et al. Nature. 2006;444(7117):337-342. doi:10.1038/nature05354
[^walle-2004-bioavailability]: Walle T et al. Drug Metab Dispos. 2004;32(12):1377-82. doi:10.1124/dmd.104.000885

---
*This page is co-maintained with AI assistance. Content reflects current scientific literature as of the last review date; it is not medical advice. See [footer disclaimer](../../../README.md) for full terms.*
