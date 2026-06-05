---
schema: medicine-entry/v1
id: quercetin
name: Quercetin
atlas: 03-medicine
scale: 03-food
status: draft
last_reviewed: 2026-06-05
summary: "Flavonol abundant in onions and apples; mast cell stabilizer, NF-κB inhibitor, Zn ionophore, and antiviral; bioavailability varies significantly across aglycone vs. glycoside vs. phytosome formulations."
aliases: ["quercetin", "3,3',4',5,7-pentahydroxyflavone", "quercetin aglycone", "rutin (quercetin-3-rutinoside)", "quercitrin", "isoquercetin", "quercetin dihydrate", "quercetin phytosome"]
sources:
  - id: boots-2008-quercetin-review
    type: peer-reviewed
    cite: "Boots AW, Haenen GR, Bast A. Health effects of quercetin: from antioxidant to nutraceutical. Eur J Pharmacol. 2008;585(2-3):325-37."
    doi: "10.1016/j.ejphar.2008.03.008"
    pmid: "18417116"
    url: "https://doi.org/10.1016/j.ejphar.2008.03.008"
  - id: formica-1995-quercetin-review
    type: peer-reviewed
    cite: "Formica JV, Regelson W. Review of the biology of quercetin and related bioflavonoids. Food Chem Toxicol. 1995;33(12):1061-80."
    doi: "10.1016/0278-6915(95)00077-1"
    pmid: "8847003"
    url: "https://doi.org/10.1016/0278-6915(95)00077-1"
  - id: cochrane-quercetin
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
  - target: 01-human/07-system/immune-system
    relation: modulates
    note: "Quercetin stabilizes mast cell membranes via PKC inhibition, reducing histamine and LTC4 release; also suppresses T-helper polarization toward Th2 and inhibits IgE-mediated degranulation pathways."
  - target: 01-human/03-molecular/histamine
    relation: modulates
    note: "Quercetin inhibits histamine release by blocking Ca²⁺ influx and PKC activation in mast cells and basophils; COMT inhibition by quercetin additionally prolongs catecholamine half-life in adrenergic signaling."
  - target: 01-human/03-molecular/nf-kb
    relation: modulates
    note: "Quercetin blocks IKK phosphorylation and prevents IκBα degradation, inhibiting NF-κB nuclear translocation and downstream expression of TNF-α, IL-6, IL-8, and COX-2 in macrophages and epithelial cells."
  - target: 01-human/04-cellular/macrophage
    relation: modulates
    note: "Quercetin suppresses NLRP3 inflammasome assembly and caspase-1 activation in macrophages, reducing IL-1β and IL-18 maturation; also inhibits PI3K/Akt survival signaling in activated macrophages."
---

# Quercetin

## Overview

**Quercetin** (3,3',4',5,7-pentahydroxyflavone, C₁₅H₁₀O₇, MW 302.2 Da) is a **flavonol** — a subclass of flavonoids characterised by a 3-hydroxyflavone backbone with a 2,3-double bond and a ketone at position 4 in the C-ring. Quercetin is one of the most abundant dietary flavonoids consumed by humans globally, estimated at 5–40 mg/day in typical Western diets.

**Primary dietary sources:**
- **Onions (yellow, red):** Highest among common foods — 200–1200 mg/kg fresh weight, predominantly as quercetin-4'-glucoside and quercetin-3,4'-diglucoside; outer skins have the highest concentration
- **Capers:** Exceptionally high — up to 1800 mg/kg fresh (quercetin aglycone and rutin); the richest common food source by weight
- **Apples:** Quercetin-3-galactoside (hyperoside) and quercetin-3-glucoside; concentrated in peel (~40 mg/100 g peel vs. ~10 mg/100 g flesh)
- **Kale and broccoli:** Quercetin-3-glucoside and rutin (quercetin-3-rutinoside); ~50–100 mg/kg fresh weight
- **Berries (blueberries, cranberries, elderberries):** 10–150 mg/kg fresh; also contain myricetin and cyanidin glycosides
- **Black and green tea:** Quercetin glycosides (primarily kaempferol and quercetin conjugates) plus catechins; ~2–5 mg per cup of quercetin equivalents
- **Red wine:** ~2–12 mg/L quercetin aglycone and glycosides

**Quercetin forms in food and supplements:**
- **Aglycone (free quercetin):** No attached sugar; low water solubility (0.0006 mg/mL); used in many supplements; paradoxically, better absorbed than rutin in some studies because colonic deglycosylation is a rate-limiting step
- **Quercetin-3-glucoside (isoquercetin):** Better absorbed than aglycone in the small intestine via sodium-dependent glucose transporter (SGLT1) or lactase-phlorizin hydrolase; naturally found in onions
- **Rutin (quercetin-3-rutinoside):** Disaccharide (rutinose = rhamnose-glucose) attached at position 3; must be deglycosylated by gut microbiome enzymes (α-rhamnosidases, β-glucosidases) in the colon; absorption is slower and more variable; used clinically in some countries for chronic venous insufficiency
- **Quercetin phytosome:** Quercetin-phosphatidylcholine complex (QUERCEFIT, Sophora brand); improved absorption ~20-fold vs. aglycone in comparative pharmacokinetic studies

Historically, quercetin (as part of rutin-containing extracts) has been used in European phytomedicine for capillary fragility, chronic venous insufficiency, and hemorrhoidal disease (bioflavonoid therapy). It gained contemporary research interest for its pleiotropic anti-inflammatory, antiviral, and anti-cancer mechanisms.

## Mechanism

### Mast Cell Stabilisation (Primary Anti-allergic Mechanism)

Quercetin is a potent **mast cell stabiliser** — one of its most clinically relevant mechanisms:

1. **PKC inhibition:** Quercetin inhibits protein kinase C (PKC), which is required for signal transduction downstream of the high-affinity IgE receptor (FcεRI) on mast cells and basophils. PKC activation normally leads to exocytosis of secretory granules (histamine, tryptase, heparin) and de novo synthesis of lipid mediators (prostaglandins, leukotrienes)
2. **Ca²⁺ influx inhibition:** Quercetin inhibits Ca²⁺-dependent signalling cascades; reduces IP₃-mediated calcium release from the ER and store-operated calcium entry (SOCE) — both required for mast cell degranulation. Without adequate cytoplasmic Ca²⁺ rise, degranulation is incomplete
3. **Consequences:**
   - ↓Histamine release from mast cells and basophils (immediate-phase allergic response)
   - ↓Leukotriene C4 (LTC4) and LTD4 release (bronchoconstriction/chemotaxis mediators)
   - ↓Prostaglandin D2 (PGD2) release
   - ↓Tryptase secretion
4. Quercetin's mast cell stabilisation is mechanistically distinct from antihistamines (which block H1/H2 receptors post-release) — quercetin prevents mediator release entirely [^boots-2008-quercetin-review]

### NF-κB Inhibition

- **IKK inhibition:** Quercetin inhibits IκB kinase (IKK) complex activity → IκBα is not phosphorylated → not ubiquitinated and degraded → NF-κB (p65/p50) remains sequestered in cytoplasm in inactive complex
- **PI3K/Akt pathway suppression:** PI3K activates IKK via Akt; quercetin is a PI3K inhibitor (targeting the ATP-binding pocket of PI3K catalytic subunits — particularly PI3Kδ, relevant in immune cells) → upstream NF-κB suppression
- **Net transcriptional effects:** ↓TNF-α, ↓IL-6, ↓IL-8, ↓MCP-1, ↓COX-2, ↓iNOS, ↓VCAM-1
- This NF-κB suppression operates across macrophages, epithelial cells, and endothelial cells — broadly anti-inflammatory [^boots-2008-quercetin-review]

### NLRP3 Inflammasome Inhibition

- Quercetin inhibits **NLRP3 inflammasome** assembly — the multiprotein complex responsible for caspase-1 activation and IL-1β/IL-18 maturation
- Mechanistic steps: quercetin inhibits NLRP3 ATPase activity (required for oligomerisation), ASC speck formation, and caspase-1 auto-processing
- ↓IL-1β and ↓IL-18 secretion from macrophages and inflammasome-activated tissues
- Relevant in gout (NLRP3 activated by monosodium urate crystals), metabolic syndrome, and atherosclerosis contexts

### Zinc Ionophore Activity

An important and relatively underappreciated mechanism:
- Quercetin forms membrane-permeable complexes with Zn²⁺ ions, acting as a **zinc ionophore** — facilitating intracellular zinc accumulation
- Intracellular Zn²⁺ inhibits RNA-dependent RNA polymerase (RdRp) of RNA viruses — this is the proposed mechanism for quercetin's antiviral activity
- The ionophore function requires quercetin to form stable lipophilic Zn-chelate complexes that cross cell membranes; this was proposed as a rationale for combining quercetin with zinc supplementation for antiviral purposes (analogous to zinc + chloroquine)

### Antiviral Mechanisms

- **SARS-CoV-2 3CL protease (Mpro) inhibition:** Computational docking studies and in vitro enzyme assays show quercetin inhibits 3CL protease (IC₅₀ ~7–50 µM depending on assay conditions), a key viral protease for polyprotein processing; however, concentrations are well above achievable plasma levels
- **Helicase inhibition:** Quercetin inhibits SARS-CoV-2 helicase (nsp13) in biochemical assays — helicase unwinds dsRNA during viral replication
- **Zinc ionophore + Zn²⁺ → RdRp inhibition:** As above
- **Host cell entry:** Some evidence for inhibition of viral spike protein binding to ACE2 and TMPRSS2
- **Caveat:** All antiviral mechanisms demonstrated in vitro at concentrations (5–100 µM) far exceeding typical plasma quercetin levels (<1 µM after standard doses); clinical antiviral efficacy in humans is not established by RCTs

### COMT Inhibition

- Quercetin inhibits **catechol-O-methyltransferase (COMT)** — the enzyme responsible for methylation and inactivation of catecholamines (dopamine, epinephrine, norepinephrine) and estrogens (catechol estrogens)
- **Consequences:** ↑Catecholamine half-life → ↑adrenergic signalling; ↑catechol estrogen levels → potential modulation of estrogen metabolism (relevant in breast cancer risk contexts)
- COMT inhibition by quercetin is a structural consequence of its catechol-like 3',4'-dihydroxy arrangement in the B-ring (similar to entacapone and tolcapone, clinical COMT inhibitors used in Parkinson's disease)

### Antioxidant Activity

- Quercetin is a potent radical scavenger (H-atom transfer and single-electron transfer mechanisms) due to the catechol B-ring and 3-OH + 4-keto arrangement
- Superoxide anion (O₂•⁻) scavenging: quercetin chelates Fe²⁺/Cu²⁺ to reduce Fenton-type OH• generation (metal chelation at 3-OH/4-keto and 5-OH/4-keto sites)
- Direct ORAC (oxygen radical absorbance capacity): quercetin has one of the highest ORAC values among common dietary flavonoids
- Note: like curcumin, quercetin has PAINS-like properties (autofluorescence, metal chelation) that may confound assay readouts in high-throughput biochemical studies

### PI3K/Akt Pathway Inhibition

- Quercetin inhibits PI3Kδ (IC₅₀ ~3 µM in enzyme assays) and PI3Kγ → ↓Akt phosphorylation → ↓mTOR → anti-proliferative and pro-autophagic effects in cancer cell lines
- Relevant in cancer biology and immune cell activation (PI3Kδ is predominantly expressed in immune cells — the same target as idelalisib in B-cell cancers)

## Clinical Use

### Therapeutic Applications

| Indication | Dose studied | Form | Evidence quality |
|:---|:---|:---|:---|
| Allergic rhinitis / allergic conditions | 400–600 mg/day | Aglycone or phytosome | Low |
| Chronic venous insufficiency | 400–600 mg/day rutin | Rutin (quercetin-rutinoside) | Moderate |
| Hypertension | 150–730 mg/day | Aglycone | Low–moderate |
| Metabolic syndrome / inflammation | 500–1000 mg/day | Aglycone | Low |
| Exercise performance / muscle recovery | 500–1000 mg/day | Aglycone | Low |
| COVID-19 supportive | 500–1000 mg/day + zinc | Phytosome | Very low |

**Chronic venous insufficiency:** Rutin-containing preparations (as part of flavonoid mixtures, e.g., Daflon — combination of diosmin + hesperidin with rutin) have moderate-quality RCT evidence for symptom relief (leg pain, heaviness, oedema) and are approved/registered as medicines in several EU countries for this indication.

**Hypertension:** A systematic review (Serban et al., 2016, JAHA) of 7 RCTs found quercetin supplementation significantly reduced systolic BP (−3.04 mmHg, 95% CI −5.26 to −0.83) and diastolic BP (−2.63 mmHg, 95% CI −3.72 to −1.53). Effects were more pronounced at doses ≥500 mg/day and in trials >8 weeks.

### Populations of Interest

- Allergic individuals (mast cell-mediated conditions: allergic rhinitis, urticaria, food allergy — theoretical benefit, limited clinical data)
- Individuals with chronic venous insufficiency
- Metabolic syndrome patients (anti-inflammatory adjunct)
- Exercise athletes (claimed ergogenic aid — reduced post-exercise muscle damage via antioxidant and anti-inflammatory mechanisms; modest RCT support)

### Drug Interactions

- **Quinolone antibiotics (e.g., ciprofloxacin):** Quercetin inhibits organic anion transporter-mediated renal ciprofloxacin excretion → ↑ciprofloxacin exposure; also may be competitive substrate for CYP1A2
- **Cyclosporine:** Quercetin inhibits CYP3A4 and P-gp → ↑cyclosporine AUC; clinically significant interaction with narrow therapeutic index drug
- **Warfarin:** CYP2C9 inhibition (quercetin IC₅₀ ~1–5 µM in microsomes) → ↑warfarin exposure; additive anticoagulant concern; monitor INR
- **Estrogen-containing medications:** COMT inhibition may alter estrogen catechol metabolism; theoretical interaction with HRT or OCP, not clinically characterised
- **Digoxin:** P-glycoprotein inhibition → ↑digoxin absorption; cardiac toxicity risk
- **Fluoroquinolones/iron:** Quercetin chelates metal ions (Fe³⁺, Zn²⁺, Cu²⁺) → potential reduction in absorption of iron supplements and metal-dependent drugs when taken concomitantly

### Bioavailability Optimisation

- **Take with food** (especially fatty meals) — improves lymphatic absorption of quercetin
- **Isoquercetin (quercetin glucoside):** Absorbed ~3× more efficiently than aglycone via intestinal SGLT1 and brush-border β-glucosidase
- **Quercetin phytosome (QUERCEFIT):** Published pharmacokinetic comparison shows ~20-fold higher Cmax vs. quercetin aglycone
- **Avoid high-fiber meals simultaneously** — dietary fiber may bind quercetin and reduce absorption

## Evidence

### Blood Pressure Meta-analysis

Serban et al. (2016, J Am Heart Assoc): systematic review of 7 RCTs (n=587 total):
- Quercetin significantly reduced SBP (−3.04 mmHg; 95% CI: −5.26 to −0.83; p=0.006) and DBP (−2.63 mmHg; 95% CI: −3.72 to −1.53; p<0.0001)
- Subgroup: doses ≥500 mg/day showed stronger effects; trials in metabolic syndrome populations showed larger reductions
- GRADE: **Low–Moderate** — small sample sizes per trial (n=30–100), short duration (4–12 weeks), heterogeneous quercetin forms, potential publication bias

### Inflammatory Markers

Li et al. (2014) and subsequent meta-analyses confirm that quercetin supplementation reduces CRP, TNF-α, and IL-6 in populations with elevated baseline inflammatory markers:
- CRP: mean reduction −0.33 mg/L (modest; not consistently significant across all meta-analyses)
- IL-6: variable; more consistent in high-dose trials (≥500 mg/day)
- GRADE: **Low** — heterogeneous populations and formulations; risk of bias in individual trials

### Rutin / Chronic Venous Insufficiency

Multiple European RCTs (n=50–500, 2–6 months) of rutin-containing flavonoid preparations (diosmin/hesperidin/rutin mixtures):
- Consistent improvements in leg pain, heaviness, oedema, and quality-of-life scores vs. placebo
- Venous clinical severity scores improved in several RCTs
- **Cochrane Review (Martinez-Zapata et al., 2016):** 53 RCTs of flavonoids for chronic venous disease — significant reduction in oedema and trophic skin changes; evidence quality **Moderate** (older Cochrane review ratings; newer GRADE would likely rate as **Low to Moderate**)

### Antiviral / COVID-19

Several small RCTs examined quercetin phytosome (500–1000 mg/day) + zinc + vitamin C during early COVID-19 (2020–2022):
- Di Pierro et al. (2021, Int J Gen Med): quercetin phytosome (1 g/day) in COVID-19 outpatients — reduced rate of hospitalisation vs. standard care in non-randomised observational study (n=152); **very high risk of bias**; not a controlled RCT
- No large, adequately powered, blinded RCT demonstrating clinical benefit for quercetin in COVID-19 as of 2026
- GRADE: **Insufficient/Very Low** for antiviral indication

### Limitations Across Studies

1. **Formulation heterogeneity:** Aglycone, rutin, isoquercetin, and phytosome preparations have profoundly different pharmacokinetics; pooling across formulations in meta-analyses is methodologically problematic
2. **Small sample sizes:** Most individual quercetin RCTs: n<100; underpowered for clinical endpoints
3. **Short duration:** Few trials exceed 12 weeks
4. **Bioavailability gap:** Mechanistic in vitro studies at 5–100 µM; achievable plasma levels <1 µM with standard aglycone; phytosome formulations improve this but remain below in vitro effective concentrations for antiviral mechanisms

## Connections

- **Modulates** → [Immune System](../../../../../01-human/07-system/immune-system/README.md): Quercetin's mast cell-stabilising (PKC inhibition, ↓Ca²⁺ influx, ↓histamine/LTC4 release), NLRP3 inflammasome-suppressing, and T-helper-2 polarisation-attenuating activities collectively dampen the effector arm of allergic and innate immune responses; PI3Kδ inhibition reduces B-cell and mast cell signalling amplitudes.

- **Modulates** → [Histamine](../../../../../01-human/03-molecular/histamine/README.md): Quercetin reduces histamine synthesis and secretion from mast cells and basophils by blocking Ca²⁺-dependent degranulation via PKC and SOCE pathway inhibition; COMT inhibition additionally modulates catecholamine metabolism with downstream effects on adrenergic regulation of histamine-releasing cells.

- **Modulates** → [NF-κB](../../../../../01-human/03-molecular/nf-kb/README.md): IKK inhibition prevents IκBα phosphorylation and degradation, trapping NF-κB in the cytoplasm; PI3K/Akt inhibition provides upstream blockade of the NF-κB activation cascade; net transcriptional suppression of TNF-α, IL-6, COX-2, and VCAM-1 in macrophages and endothelial cells.

- **Modulates** → [Macrophage](../../../../../01-human/04-cellular/macrophage/README.md): Quercetin suppresses NLRP3 inflammasome assembly and caspase-1-mediated IL-1β/IL-18 maturation in LPS-primed macrophages; PI3K inhibition attenuates Akt-mediated macrophage survival and M1 activation; overall phenotypic shift toward reduced pro-inflammatory cytokine output observed across multiple in vitro models.

[^boots-2008-quercetin-review]: Boots AW, Haenen GR, Bast A. Eur J Pharmacol. 2008;585(2-3):325-37. doi:10.1016/j.ejphar.2008.03.008
[^formica-1995-quercetin-review]: Formica JV, Regelson W. Food Chem Toxicol. 1995;33(12):1061-80. doi:10.1016/0278-6915(95)00077-1

---
*This page is co-maintained with AI assistance. Content reflects current scientific literature as of the last review date; it is not medical advice. See [footer disclaimer](../../../README.md) for full terms.*
