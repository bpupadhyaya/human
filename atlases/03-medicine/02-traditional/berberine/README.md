---
schema: medicine-entry/v1
id: berberine
name: Berberine
atlas: 03-medicine
scale: 02-traditional
status: draft
last_reviewed: 2026-06-05
summary: "Isoquinoline alkaloid from Berberis spp. Used in TCM (huáng bò), Ayurveda, and Unani. Activates AMPK → mimics metformin; lowers HbA1c ~1.0% (RCT). Anti-inflammatory via NF-κB suppression. Improves NAFLD, dyslipidaemia. Poor oral bioavailability (~1%) limits dosing."
aliases: ["berberine", "berberine hydrochloride", "huáng bò", "huánglián", "daruharidra", "tree turmeric", "BBR", "berberine sulfate"]
sources:
  - id: yin-2008-berberine-t2dm
    type: peer-reviewed
    cite: "Yin J, Xing H, Ye J. Efficacy of berberine in patients with type 2 diabetes mellitus. Metabolism. 2008;57(5):712-17."
    doi: "10.1016/j.metabol.2008.01.013"
    pmid: "18442638"
    url: "https://doi.org/10.1016/j.metabol.2008.01.013"
  - id: zhang-2010-berberine-insulin-receptor
    type: peer-reviewed
    cite: "Zhang H, Wei J, Xue R, et al. Berberine lowers blood glucose in type 2 diabetes mellitus patients through increasing insulin receptor expression. Metabolism. 2010;59(2):285-92."
    doi: "10.1016/j.metabol.2009.07.029"
    pmid: "19800084"
    url: "https://doi.org/10.1016/j.metabol.2009.07.029"
  - id: lan-2015-berberine-meta
    type: peer-reviewed
    cite: "Lan J, Zhao Y, Dong F, et al. Meta-analysis of the effect and safety of berberine in the treatment of type 2 diabetes mellitus, hyperlipemia and hypertension. J Ethnopharmacol. 2015;161:69-81."
    doi: "10.1016/j.jep.2014.09.049"
    pmid: "25498346"
    url: "https://doi.org/10.1016/j.jep.2014.09.049"
cross_links:
  - target: 01-human/03-molecular/insulin
    relation: modulates
    evidence: yin-2008-berberine-t2dm
    note: "Berberine activates AMPK in hepatocytes and skeletal muscle, mimicking the insulin-sensitising effect of metformin. Separately, berberine upregulates insulin receptor expression at the mRNA and protein level in peripheral tissues, enhancing insulin signal transduction independent of AMPK. RCTs show HbA1c reductions of ~1.0% comparable to metformin 1500 mg/day over 13 weeks."
  - target: 01-human/03-molecular/il-6
    relation: modulates
    evidence: lan-2015-berberine-meta
    note: "Berberine suppresses NF-κB activation by blocking IKKβ phosphorylation, reducing transcription of pro-inflammatory cytokines including IL-6 and TNF-α. In metabolic syndrome patients, berberine reduces CRP and IL-6; the anti-inflammatory effect is considered synergistic with metabolic benefits in NAFLD and atherosclerosis contexts."
  - target: 01-human/06-organ/liver
    relation: treats
    evidence: yin-2008-berberine-t2dm
    note: "Berberine activates AMPK in hepatocytes via Complex I inhibition (similar to metformin), reducing malonyl-CoA and lipogenesis. It inhibits SREBP-1c → reduced fatty acid synthesis; activates autophagy via AMPK → improved lipid clearance. Clinical RCTs show improved liver enzyme profiles (ALT, AST), reduced hepatic fat on imaging, and improved histological NAFLD activity scores."
---

# Berberine

## Overview

**Berberine** is an isoquinoline alkaloid (MW 336.4 Da) found in the roots, rhizomes, and stem bark of plants in the genera *Berberis*, *Coptis*, *Hydrastis* (goldenseal), *Phellodendron*, and related species. It produces the characteristic bright yellow colour of these plant tissues and has been used as a natural dye as well as a medicine across multiple traditional systems.

In **Traditional Chinese Medicine (TCM)**, berberine-containing plants are employed as *huáng bò* (*Phellodendron amurense*, Amur cork tree) and *huánglián* (*Coptis chinensis*, Chinese goldthread), primarily for damp-heat conditions, dysentery, and fevers — uses that align with berberine's well-documented antibacterial activity. In **Ayurveda**, *Berberis aristata* (daruharidra, tree turmeric) is used for skin disorders, diabetes (*prameha*), and liver disease. **Unani medicine** employs *zereshk* (*Berberis vulgaris*, barberry) similarly.

Contemporary clinical interest centres on metabolic disease: berberine's AMPK-activating, insulin-sensitising, lipid-lowering, and gut-microbiome-modulating properties have made it the subject of numerous RCTs in type 2 diabetes, dyslipidaemia, NAFLD, and polycystic ovary syndrome (PCOS).

A critical **pharmacokinetic limitation** constrains clinical use: oral bioavailability is approximately **1–5%** due to poor intestinal absorption, P-glycoprotein (P-gp) efflux, and extensive first-pass metabolism. Despite this, luminal concentrations in the gut are high, which explains both the direct gut effects (antimicrobial, microbiome modulation) and raises questions about whether systemic or luminal mechanisms account for metabolic efficacy.

## Mechanism

### AMPK Activation — The Metformin Parallel

The most characterised mechanism of berberine's metabolic effects is **AMPK activation**, following a pathway parallel to metformin:

1. **Mitochondrial Complex I inhibition:** Berberine (as a positively charged molecule) accumulates in mitochondria and inhibits Complex I (NADH:ubiquinone oxidoreductase) at micromolar concentrations, raising the intracellular AMP/ATP ratio
2. **AMPK activation:** Elevated AMP/ATP activates AMPK (via LKB1-mediated Thr172 phosphorylation), the master cellular energy sensor
3. **Downstream metabolic effects:**
   - **Hepatic gluconeogenesis:** AMPK phosphorylates CRTC2 → disrupts CREB-TORC2 → ↓ PEPCK and G6Pase transcription → reduced hepatic glucose output
   - **Lipogenesis:** AMPK phosphorylates ACC → ↓ malonyl-CoA → ↓ fatty acid synthesis; berberine also directly inhibits **SREBP-1c** transcription, reducing de novo lipogenesis
   - **Fatty acid oxidation:** ↓ Malonyl-CoA relieves CPT1 inhibition → increased mitochondrial fatty acid import and β-oxidation
   - **Cholesterol:** PCSK9 inhibition (berberine reduces PCSK9 mRNA) → increased LDL receptor recycling → reduced circulating LDL-C

### Insulin Receptor Upregulation

Independent of AMPK, berberine increases insulin receptor expression. Zhang et al. (2010) [^zhang-2010-berberine-insulin-receptor] demonstrated:
- Berberine stabilises **insulin receptor mRNA** by inhibiting a mRNA destabilisation mechanism (involved AU-rich element binding proteins)
- Protein-level increases in insulin receptor expression were confirmed in primary hepatocytes and skeletal muscle cell lines
- In T2DM patients, berberine treatment increased insulin receptor expression with functional insulin sensitisation

This dual mechanism (AMPK activation + insulin receptor upregulation) may account for effect sizes comparable to metformin despite berberine's poor bioavailability.

### Anti-inflammatory Mechanisms

- **NF-κB suppression:** Berberine inhibits IKKβ phosphorylation, preventing IκBα degradation and NF-κB nuclear translocation; reduces transcription of IL-6, TNF-α, IL-1β, COX-2
- **NLRP3 inflammasome:** Berberine inhibits NLRP3 assembly, reducing IL-1β and IL-18 maturation — relevant in metabolic inflammation and gout models
- **MAPK pathway:** Inhibits ERK1/2 and p38 MAPK phosphorylation in macrophages → reduced inflammatory cytokine release

### Gut Microbiome Effects

At luminal concentrations achievable with oral dosing, berberine:
- Inhibits growth of gram-positive bacteria (including *Enterococcus*, *Staphylococcus*) and some gram-negative pathogens; mechanism: DNA intercalation, inhibition of topoisomerase II
- Promotes growth of *Akkermansia muciniphila* and short-chain fatty acid-producing *Lactobacillus* and *Bifidobacterium* species
- This gut microbiome remodelling may independently contribute to improved insulin sensitivity and reduced intestinal permeability ("leaky gut"), though the contribution relative to systemic AMPK effects is unresolved

### Antibacterial Mechanisms (Traditional Use Basis)

The original TCM/Ayurvedic use for dysentery and infectious diarrhoea has mechanistic support:
- Berberine inhibits bacterial topoisomerase II (DNA gyrase) via intercalation — mechanism distinct from fluoroquinolones, so some cross-resistance is not expected
- Active against *Vibrio cholerae*, enterotoxigenic *E. coli*, *Giardia lamblia* at concentrations achievable luminally after oral dosing
- WHO does not endorse berberine as a standalone antibiotic, but traditional use for infectious diarrhoea is mechanistically coherent

## Clinical Use

### Indications and Dosing

| Indication | Dose | Duration studied | Evidence quality |
|:---|:---|:---|:---|
| Type 2 diabetes / hyperglycemia | 500 mg three times daily (1500 mg/day) | 13–24 weeks | Moderate (several RCTs vs. metformin) |
| Dyslipidaemia | 500 mg three times daily | 8–24 weeks | Moderate |
| NAFLD / NASH | 500 mg three times daily | 16 weeks | Low-moderate |
| PCOS | 500 mg three times daily | 3–6 months | Low (limited RCTs) |
| Infectious diarrhoea | 400 mg three times daily | 3–7 days | Low-moderate |

The standard clinical dose used in RCTs is **1500 mg/day** (500 mg × 3, taken 30 minutes before meals). The timing before meals matters: berberine taken pre-meal reduces post-prandial glucose excursions more effectively than taken post-meal.

### Formulations and Bioavailability Enhancement

- **Standard berberine hydrochloride**: ~1–5% oral bioavailability; this is the form used in most clinical trials
- **Berberine with piperine (Bioperine):** Piperine (from black pepper) inhibits P-gp efflux and CYP3A4, potentially increasing berberine AUC by 50–100%; no large RCTs using this combination
- **Dihydroberberine (DHB):** Reduced form with ~5× higher intestinal absorption; converts back to berberine in intestinal cells; marketed as "glucose disposal agent"; limited clinical trial data
- **Berberine phytosome** (complexed with phosphatidylcholine): improved absorption reported in pilot studies

### Drug Interactions (Important)

- **Metformin:** Additive glucose-lowering; combination studied in small trials — monitor for hypoglycemia if insulin secretagogues are co-prescribed
- **Cyclosporine (CYP3A4 substrate):** Berberine inhibits CYP3A4 and P-gp → increased cyclosporine levels; documented interaction — **clinically significant, avoid combination or monitor closely**
- **Anticoagulants:** Berberine may prolong prothrombin time; use with caution with warfarin
- **CYP2D6 substrates** (metoprolol, codeine): Berberine inhibits CYP2D6; potential for increased exposure of 2D6 substrates
- **Glucose-lowering agents:** Additive hypoglycemic risk when combined with sulfonylureas or insulin

### Safety

Generally well-tolerated at 1500 mg/day. Common adverse effects: constipation (most frequent), nausea, abdominal cramping, diarrhoea. These often resolve after dose titration. Serious adverse effects are rare in reported trials but long-term safety data (>1 year) in large populations are lacking. Contraindicated in pregnancy (potential teratogenicity; uterotonic effects reported in animal studies) and in neonates/infants.

## Evidence

### Type 2 Diabetes

Yin et al. (2008) [^yin-2008-berberine-t2dm] — RCT, n=116, T2DM patients, berberine 500 mg three times daily vs. metformin 500 mg three times daily vs. rosiglitazone, 13 weeks:
- Berberine: HbA1c **−2.0%** (from 9.5% to 7.5%); FBG −6.9 mmol/L; post-prandial glucose −11.1 mmol/L
- Metformin: HbA1c **−1.8%**; statistically non-inferior to metformin
- **Limitation:** Chinese population only; single-centre; no placebo arm

Zhang et al. (2010) [^zhang-2010-berberine-insulin-receptor] — mechanistic RCT demonstrating insulin receptor upregulation alongside glucose-lowering; HOMA-IR reduced.

Lan et al. (2015) meta-analysis [^lan-2015-berberine-meta] — 27 RCTs included:
- HbA1c: pooled reduction **−0.92%** (95% CI: −1.14 to −0.70) vs. comparators
- FBG: −1.28 mmol/L; post-prandial glucose: −2.44 mmol/L
- Total cholesterol: −0.53 mmol/L; LDL-C: −0.59 mmol/L; triglycerides: −0.50 mmol/L
- Blood pressure: modest reductions in SBP and DBP
- **Limitations of the meta-analysis:** High proportion of Chinese trials (different population, diet, background therapy); high heterogeneity; many trials small and short; industry involvement in several

### NAFLD

Multiple small RCTs (n=50–170) show berberine 500 mg three times daily for 16 weeks:
- Reduces hepatic fat fraction on MRI/ultrasound
- Improves ALT/AST normalisation rates
- Reduces liver fibrosis markers (though histological data are limited to one biopsy-confirmed trial)
- GRADE evidence: **Low** — methodological limitations and inconsistent outcome reporting

### Evidence Gaps

- No large RCT (n>500) in Western populations with pre-defined hard cardiovascular or liver endpoints
- Long-term safety trials (>1 year) absent
- Optimal formulation for systemic vs. luminal effects unclear
- PCOS and fertility effects require larger adequately powered trials

## Connections

- **Modulates** → [Insulin](../../../../../01-human/03-molecular/insulin/README.md): Berberine activates AMPK (Complex I inhibition) and independently upregulates insulin receptor expression, sensitising peripheral tissues to insulin signalling without stimulating insulin secretion. The combined mechanism explains glucose-lowering comparable to metformin 1500 mg/day in head-to-head RCTs.

- **Modulates** → [IL-6](../../../../../01-human/03-molecular/il-6/README.md): IKKβ inhibition → NF-κB suppression → reduced IL-6 and TNF-α transcription; NLRP3 inflammasome inhibition further reduces IL-1β/IL-18; MAPK pathway suppression adds to the anti-inflammatory profile. In metabolic syndrome patients, berberine reduces systemic CRP and IL-6 alongside metabolic improvements, suggesting the metabolic and anti-inflammatory effects are intertwined rather than independent.

- **Treats** → [Liver](../../../../../01-human/06-organ/liver/README.md): The liver is the primary metabolic target. AMPK activation in hepatocytes reduces gluconeogenesis (via CRTC2/PEPCK/G6Pase suppression) and lipogenesis (via ACC phosphorylation and SREBP-1c inhibition). Autophagy activation promotes lipid clearance. Clinical RCTs demonstrate improved liver enzymes, reduced hepatic fat, and improved NAFLD histology — making berberine one of the more evidence-supported botanicals for non-alcoholic fatty liver disease.

[^yin-2008-berberine-t2dm]: Yin J et al. Metabolism. 2008;57(5):712-17. doi:10.1016/j.metabol.2008.01.013
[^zhang-2010-berberine-insulin-receptor]: Zhang H et al. Metabolism. 2010;59(2):285-92. doi:10.1016/j.metabol.2009.07.029
[^lan-2015-berberine-meta]: Lan J et al. J Ethnopharmacol. 2015;161:69-81. doi:10.1016/j.jep.2014.09.049
