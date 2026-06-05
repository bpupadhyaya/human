---
schema: medicine-entry/v1
id: sulforaphane
name: Sulforaphane
atlas: 03-medicine
scale: 03-food
status: draft
last_reviewed: 2026-06-05
summary: "Isothiocyanate from broccoli glucoraphanin hydrolysis; potent Nrf2 activator inducing phase II detoxification enzymes and glutathione synthesis; HDAC inhibitor with liver-protective and anti-inflammatory activity."
aliases: ["sulforaphane", "SFN", "1-isothiocyanato-4-(methylsulfinyl)butane", "4-methylsulfinylbutyl isothiocyanate", "glucoraphanin (precursor)", "broccoli isothiocyanate", "sulforaphane nitrile"]
sources:
  - id: fahey-2001-sulforaphane-review
    type: peer-reviewed
    cite: "Fahey JW, Talalay P. Antioxidant functions of sulforaphane: a potent inducer of Phase II detoxication enzymes. Food Chem Toxicol. 1999;37(9-10):973-9."
    doi: "10.1016/s0278-6915(99)00082-4"
    pmid: "10541453"
    url: "https://doi.org/10.1016/s0278-6915(99)00082-4"
  - id: kensler-2013-nrf2-sulforaphane
    type: peer-reviewed
    cite: "Kensler TW, Egner PA, Agyeman AS, et al. Keap1-Nrf2 signaling: a target for cancer prevention by sulforaphane. Top Curr Chem. 2013;329:163-77."
    doi: "10.1007/128_2012_339"
    pmid: "22752583"
    url: "https://doi.org/10.1007/128_2012_339"
  - id: cochrane-sulforaphane
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
  - target: 01-human/06-organ/liver
    relation: modulates
    note: "Sulforaphane activates Nrf2 in hepatocytes, inducing NQO1, HO-1, and glutathione-S-transferases; reduces oxidative hepatocellular damage in APAP toxicity models and attenuates NASH-related fibrosis."
  - target: 01-human/07-system/immune-system
    relation: modulates
    note: "Nrf2-mediated HO-1 induction by sulforaphane suppresses NF-κB-driven cytokine release; sulforaphane also reduces NLRP3 inflammasome activation in dendritic cells and macrophages via KEAP1/Nrf2 axis."
  - target: 01-human/03-molecular/nf-kb
    relation: modulates
    note: "Sulforaphane alkylates KEAP1 cysteines (C151, C273, C288), releasing Nrf2 to suppress IKK and NF-κB; also directly inhibits HDAC activity, altering chromatin accessibility at inflammatory gene promoters."
  - target: 01-human/04-cellular/hepatocyte
    relation: modulates
    note: "Sulforaphane induces phase II detoxification enzymes (GSTM1, GSTP1, UGT1A) in hepatocytes via Nrf2/ARE, increasing xenobiotic conjugation capacity and protecting against aflatoxin B1 and APAP hepatotoxicity."
---

# Sulforaphane

## Overview

**Sulforaphane** (SFN; 1-isothiocyanato-4-(methylsulfinyl)butane, C₆H₁₁NOS₂, MW 177.3 Da) is an **isothiocyanate** — a class of organosulfur compounds bearing the −N=C=S functional group — generated enzymatically in cruciferous vegetables. Unlike most bioactive phytochemicals that exist preformed in plant tissue, sulforaphane is a **prodrug** that does not exist in intact plant cells. It is produced by a **two-component reaction** triggered only when plant tissue is damaged:

**Glucoraphanin + Myrosinase → Sulforaphane + Glucose + SO₄²⁻**

1. **Glucoraphanin** (4-methylsulfinylbutyl glucosinolate) is the stable, water-soluble precursor stored in vacuoles of broccoli (*Brassica oleracea* var. *italica*) and related Brassica species
2. **Myrosinase** (β-thioglucosidase; EC 3.2.1.147) is a plant enzyme stored separately in myrosin cells; upon tissue disruption (chewing, cutting, crushing), glucoraphanin and myrosinase mix → hydrolytic cleavage of the glucose-sulfur bond → unstable aglycone → sulforaphane (or sulforaphane nitrile via the ESP — epithiospecifier protein — diverting pathway to less bioactive nitrile product)

**Cruciferous vegetable sources (glucoraphanin content):**
- **Broccoli sprouts (3-day-old):** Highest concentration — 20–50× more glucoraphanin than mature broccoli; 1 oz (28 g) sprouts ≈ 100–400 mg sulforaphane potential; Fahey et al. (1997, PNAS) first established this
- **Mature broccoli:** 10–100 mg glucoraphanin / 100 g fresh weight; cooking critically degrades myrosinase (inactivated at 60°C), reducing conversion significantly
- **Brussels sprouts:** High glucoraphanin; also contains sinigrin (generating allyl isothiocyanate)
- **Kale, cabbage, cauliflower:** Lower but significant glucoraphanin and related glucosinolates
- **Wasabi and horseradish:** Different glucosinolates (glucosinigrin → allyl isothiocyanate); not sulforaphane sources

**Key dietary preparation principles:**
- **Raw or briefly steamed (al dente):** Preserves myrosinase → full sulforaphane conversion
- **Boiling or microwaving:** Destroys myrosinase → glucoraphanin reaches colon intact → gut microbiome provides partial conversion via bacterial myrosinase-like enzymes (bacteroides, enterococcus) but efficiency is 3–10× lower than plant myrosinase; systemic exposure to sulforaphane is substantially reduced
- **Chew thoroughly:** More tissue disruption → more myrosinase-glucoraphanin mixing → more sulforaphane
- **Add raw mustard seed powder** to cooked broccoli: provides exogenous myrosinase → restores sulforaphane production from glucoraphanin

**Pharmacokinetics:** Sulforaphane is absorbed efficiently (~80% of intact sulforaphane dose) from the small intestine; plasma Cmax is ~1–3 µM after a broccoli sprout-based dose; t₁/₂ ~2–3 h; metabolised via the mercapturic acid pathway (conjugation with glutathione by glutathione-S-transferase → GS-SFN → Cys-SFN → N-acetyl-Cys-SFN excreted in urine). Importantly, urinary N-acetylcysteine-sulforaphane serves as a validated biomarker of exposure in epidemiological studies.

## Mechanism

### KEAP1/Nrf2 Pathway — The Central Mechanism

Sulforaphane is the best-characterised **Nrf2 activator** in the dietary small molecule literature:

**Under basal conditions:**
- Nrf2 (nuclear factor erythroid 2-related factor 2; NF-E2L2) is an oxidative-stress-responsive transcription factor held in the cytoplasm by KEAP1 (Kelch-like ECH-associated protein 1)
- KEAP1 acts as an E3 ubiquitin ligase adaptor (Cullin3-based complex) → polyubiquitinates Nrf2 at Lys residues → targets Nrf2 for proteasomal degradation (t₁/₂ <20 min basal)
- KEAP1 functions as an electrophile/oxidant sensor via reactive cysteines: **Cys151, Cys273, Cys288** are the primary sensor cysteines

**Upon sulforaphane treatment:**
1. **KEAP1 cysteine alkylation:** Sulforaphane (as an electrophile via its isothiocyanate group −N=C=S) forms **covalent adducts** with KEAP1 Cys151, Cys273, and Cys288 (carbamate/dithiocarbamate bond formation); the reaction is chemically analogous to Michael addition [^fahey-2001-sulforaphane-review]
2. **KEAP1 conformational change:** Cysteine alkylation alters KEAP1 conformation → loss of ability to ubiquitinate Nrf2 → Nrf2 escapes proteasomal degradation and accumulates
3. **Nrf2 nuclear translocation:** Stabilised Nrf2 translocates to the nucleus, heterodimerises with small Maf proteins (MafF, MafG, MafK)
4. **ARE-driven gene expression:** Nrf2/Maf heterodimer binds **antioxidant response elements (AREs)** — a specific DNA motif (5'-TGACnnnGCA-3') in promoters of Nrf2 target genes:

| Nrf2 target gene | Protein | Function |
|:---|:---|:---|
| NQO1 | NAD(P)H quinone oxidoreductase 1 | 2-electron reduction of quinones → prevents semiquinone radical formation |
| HMOX1 | Heme oxygenase-1 (HO-1) | Heme catabolism → CO (vasodilatory), biliverdin/bilirubin (antioxidant), Fe²⁺; anti-inflammatory |
| GSTM1, GSTP1 | Glutathione S-transferases (Mu, Pi) | Phase II conjugation: electrophile + GSH → GS-conjugates (water-soluble, excretable) |
| GCL (GCLC, GCLM) | Glutamate-cysteine ligase (catalytic + modifier) | Rate-limiting enzyme of glutathione biosynthesis |
| SLC7A11 (xCT) | Cystine/glutamate antiporter | Imports cystine for intracellular cysteine → GSH synthesis |
| TXNRD1 | Thioredoxin reductase 1 | Reduces thioredoxin → electron relay for peroxiredoxins → H₂O₂ clearance |
| PRDX1, PRDX6 | Peroxiredoxins | H₂O₂ and lipid hydroperoxide reduction |
| FTH1, FTL | Ferritin H/L chains | Iron sequestration → ↓free Fe²⁺ → ↓Fenton-type OH• generation |
| SRXN1 | Sulfiredoxin-1 | Reduces hyperoxidised peroxiredoxins; retrograde antioxidant defence |

5. **Glutathione induction:** The combined upregulation of GCL (rate-limiting GSH synthesis step) and SLC7A11 (cystine import) substantially increases cellular GSH content — sulforaphane is among the most potent physiological inducers of intracellular glutathione [^kensler-2013-nrf2-sulforaphane]

### HDAC Inhibition

A second major mechanism independent of Nrf2:
- Sulforaphane inhibits **class I and II histone deacetylases (HDAC1, HDAC2, HDAC3, HDAC6, HDAC8)** in vitro (IC₅₀ values in the µM range)
- HDAC inhibition → maintained histone acetylation → relaxed chromatin → increased transcriptional accessibility at promoters of tumour suppressor genes and anti-inflammatory genes
- HDAC inhibition is proposed to underlie sulforaphane's anti-cancer effects in prostate, breast, and colorectal cancer cell models (↑p21/CDKN1A, ↑p27, ↓HDAC-driven gene silencing of tumour suppressors)
- **Concentration caveat:** HDAC inhibition in cells requires 5–30 µM sulforaphane; achievable plasma concentrations after broccoli sprout consumption are ~1–3 µM peak, declining rapidly; HDAC inhibition may be more relevant at local tissue/gut concentrations

### NF-κB Suppression via Nrf2 Cross-talk

- HO-1 (induced by Nrf2) produces carbon monoxide (CO), which inhibits IKK → ↓IκBα phosphorylation → ↓NF-κB nuclear translocation
- Nrf2 activation competes with and limits NF-κB for shared coactivators (CBP/p300) and for nuclear Nrf2 binding that may occupy RelA binding sites
- GSH elevation (Nrf2-mediated) reduces oxidative activation of NF-κB (ROS-dependent IKK activation is attenuated)
- Net effect: sulforaphane → ↓TNF-α, ↓IL-6, ↓IL-1β, ↓COX-2, ↓MCP-1 in macrophages, epithelial cells, and hepatocytes

### Helicobacter pylori Inhibition

- Sulforaphane (and other isothiocyanates) directly inhibit *H. pylori* growth in vitro (MIC ~4–12 µg/mL); proposed mechanism involves isothiocyanate reactivity with bacterial proteins
- Fahey et al. (2002, PNAS) demonstrated that sulforaphane eradicated *H. pylori* in gastric mucosa of infected mice; also clinical pilot data showing reduction of *H. pylori* density after broccoli sprout consumption
- Sulforaphane also suppresses *H. pylori*-induced NF-κB activation in gastric epithelial cells, reducing IL-8 secretion (IL-8 is the critical chemokine for neutrophil recruitment in gastric mucosa)

### Apoptosis and Anti-cancer Mechanisms

- **Intrinsic apoptosis:** Sulforaphane ↑Bax, ↓Bcl-2 → mitochondrial membrane depolarisation → cytochrome c release → caspase-9/3 activation
- **Cell cycle arrest:** ↑p21 (Nrf2/HDAC-dependent), ↓cyclin D1/E → G2/M arrest in cancer cells
- **Autophagy induction:** mTOR suppression (via AMPK activation) + Beclin-1 upregulation → autophagy
- **Anti-androgen receptor:** In prostate cancer cells, sulforaphane reduces androgen receptor (AR) protein levels via HDAC inhibition-dependent mechanisms — relevant for castration-resistant prostate cancer

## Clinical Use

### Therapeutic Applications

| Indication | Dose studied | Form | Evidence quality |
|:---|:---|:---|:---|
| Cancer chemoprevention (general) | Broccoli sprout extract 200–400 µmol/day | Sprout extract / stabilised SFN | Low–moderate |
| NAFLD / liver protection | 150–400 mg/day SFN equivalent | Broccoli sprout extract | Low |
| H. pylori infection (adjunct) | Broccoli sprout 70 g/day | Fresh sprouts | Low |
| Autism spectrum disorder (ASD) | 150 µmol/day | Broccoli sprout extract (sulforaphane-enriched) | Low (Phase II data) |
| Air pollution / oxidative stress | 600 µmol/day | Sprout beverage | Low |
| Type 2 diabetes (insulin sensitivity) | 150 mg/day SFN | Stabilised SFN | Low |

**Dosing notes:**
- Commercial supplements vary widely in sulforaphane content and stability; **stabilised sulforaphane** (e.g., SFN-glucosinolate + myrosinase co-formulated) or certified broccoli sprout extracts with verified glucoraphanin + active myrosinase are preferred
- Dried broccoli sprout powder without active myrosinase yields far less sulforaphane — glucoraphanin requires myrosinase for conversion; many commercial products test only glucoraphanin content, not actual SFN yield

### Populations at Potential Benefit

- **Individuals with high air pollution / chemical exposure:** Nrf2 induction upregulates Phase II carcinogen-detoxifying enzymes (aflatoxin B1 detoxification; benzene metabolism)
- **NAFLD patients:** Hepatoprotective and anti-inflammatory mechanisms; emerging RCT data
- **Autism spectrum disorder:** Phase II trial rationale based on Nrf2 upregulation improving redox balance in ASD; subsequent replication has been mixed
- **H. pylori-positive individuals** (as adjunct, not monotherapy)

### Drug Interactions and Safety

- **Thyroid function:** Cruciferous isothiocyanates can interfere with iodine uptake in the thyroid at very high doses or in iodine-deficient individuals (thiocyanate competition); at normal dietary/supplemental doses, this is not clinically significant
- **CYP1A2 induction:** Sulforaphane activates Nrf2, which can induce CYP1A2 → potential for reduced efficacy of CYP1A2-metabolised drugs (clozapine, theophylline, caffeine, duloxetine) with prolonged high-dose supplementation
- **GSTM1 null genotype:** ~50% of Caucasians lack functional GSTM1; paradoxically, GSTM1-null individuals may show different sulforaphane kinetics (GSTM1 conjugates SFN as part of its mercapturic acid metabolism pathway; null individuals have higher and more prolonged plasma SFN exposure — potentially greater Nrf2 activation)
- **Well-tolerated** in clinical trials up to 400 µmol/day; GI discomfort at very high doses; no major safety signals in Phase I/II trials

## Evidence

### Foundational Biochemical Studies

Fahey and Talalay (1999) [^fahey-2001-sulforaphane-review] established sulforaphane as among the most potent inducers of Phase II detoxification enzymes in mammalian cells, with potency defined by the **CD value** (concentration doubling NQO1 activity in Hepa1c1c7 murine hepatoma cells). Sulforaphane CD = 0.2 µM — roughly 10× more potent than the next most potent broccoli extract component at NQO1 induction.

Kensler et al. (2013) [^kensler-2013-nrf2-sulforaphane] provided detailed review of KEAP1/Nrf2 as a cancer prevention target, with sulforaphane as the prototypical inducer.

### Aflatoxin / Liver Cancer Prevention (Phase II/III)

The **Qidong, China trial** (Kensler group, Johns Hopkins):
- Population at high risk of hepatocellular carcinoma (HCC) due to aflatoxin B1 (AFB1) dietary exposure
- Broccoli sprout beverage (containing glucoraphanin + myrosinase → SFN in vivo) for 12 weeks
- **Outcome:** Urinary biomarkers of AFB1-DNA adducts and mercapturic acid metabolites of benzene/acrolein (air pollutants) were significantly reduced vs. placebo, indicating enhanced detoxification of environmental carcinogens via Phase II enzyme induction
- GRADE: **Moderate** (well-designed; large n=291; objective biomarker endpoint; real-world exposure context)
- This is the strongest clinical evidence for sulforaphane's Nrf2-mediated carcinogen detoxification mechanism

### Autism Spectrum Disorder (Phase I/II)

Singh et al. (2014, PNAS):
- 44-week randomised, double-blind, placebo-controlled trial of sulforaphane (50–150 µmol/day from broccoli sprout extract) in adolescent males with moderate-to-severe ASD (n=40)
- Significant improvements vs. placebo in ABC (Aberrant Behavior Checklist) social withdrawal subscale and SRS (Social Responsiveness Scale) at 18 weeks (p<0.001 for ABC, p=0.017 for SRS)
- Changes largely reversed after discontinuation
- **Mechanism hypothesis:** Nrf2-mediated improvement in redox balance and reduction of neuroinflammation in ASD; heat shock protein induction
- **Limitations:** Small n=40; single centre; not replicated in a subsequent larger trial (Curtin et al., 2022, JAMA Netw Open, n=54 — did not meet primary endpoint)
- GRADE: **Low** — promising signal but replication failure in larger trial

### NAFLD

Multiple small RCTs (n=30–80, 12–24 weeks) using broccoli sprout extracts:
- Reductions in ALT, AST, and gamma-GT; improvements in liver stiffness (Fibroscan) and ultrasound steatosis grading
- Consistent direction of effect but small samples and short follow-up
- GRADE: **Low**

### Air Pollution Detoxification

Egner et al. (2014, Cancer Prev Res): randomised trial in Jiangsu Province, China (high air pollution exposure) — broccoli sprout beverage for 12 weeks:
- Urinary excretion of benzene mercapturic acid (BMA) increased 61% and acrolein mercapturic acid 23% in the intervention group vs. placebo — direct evidence of enhanced carcinogen detoxification via SFN-induced mercapturic acid pathway enzymes (GST, GCL)
- GRADE: **Moderate** — objective biomarker; good sample size (n=291); well-controlled

## Connections

- **Modulates** → [Liver](../../../../../01-human/06-organ/liver/README.md): Sulforaphane is a potent Nrf2 activator in hepatocytes, inducing NQO1, HO-1, GCL, and glutathione-S-transferases that protect against oxidative, electrophilic, and carcinogen-mediated hepatocellular damage; in experimental NAFLD, sulforaphane also reduces TGF-β-driven hepatic stellate cell activation, attenuating fibrosis progression.

- **Modulates** → [Immune System](../../../../../01-human/07-system/immune-system/README.md): Nrf2-driven HO-1 induction by sulforaphane generates CO and bilirubin, both of which suppress NF-κB signalling in dendritic cells and macrophages; sulforaphane's HDAC inhibition reduces cytokine gene accessibility in innate immune cells; net effects include reduced IL-1β, IL-6, and TNF-α output without global immunosuppression.

- **Modulates** → [NF-κB](../../../../../01-human/03-molecular/nf-kb/README.md): Sulforaphane suppresses NF-κB through multiple Nrf2-dependent mechanisms (HO-1-derived CO → IKK inhibition; GSH ↑ → ↓ROS-dependent IKK activation) and HDAC inhibition (altered chromatin accessibility at NF-κB-driven gene promoters); covalent KEAP1 alkylation by sulforaphane's isothiocyanate group is the upstream initiating event.

- **Modulates** → [Hepatocyte](../../../../../01-human/04-cellular/hepatocyte/README.md): Nrf2/ARE activation in hepatocytes by sulforaphane substantially increases Phase II conjugating enzyme capacity (GSTM1, GSTP1, UGT1A1), intracellular GSH levels, and H₂O₂ clearance via peroxiredoxins; this multifaceted detoxification upregulation protects against aflatoxin B1-DNA adduct formation, acetaminophen hepatotoxicity, and oxidative lipid damage in steatohepatitis.

[^fahey-2001-sulforaphane-review]: Fahey JW, Talalay P. Food Chem Toxicol. 1999;37(9-10):973-9. doi:10.1016/s0278-6915(99)00082-4
[^kensler-2013-nrf2-sulforaphane]: Kensler TW et al. Top Curr Chem. 2013;329:163-77. doi:10.1007/128_2012_339

---
*This page is co-maintained with AI assistance. Content reflects current scientific literature as of the last review date; it is not medical advice. See [footer disclaimer](../../../README.md) for full terms.*
