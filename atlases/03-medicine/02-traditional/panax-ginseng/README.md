---
schema: medicine-entry/v1
id: panax-ginseng
name: Panax ginseng (Korean Red Ginseng)
atlas: 03-medicine
scale: 02-traditional
status: draft
last_reviewed: 2026-06-05
summary: "Korean Red Ginseng root; ginsenosides (Rb1, Rg1, Re) modulate HPA stress axis, stimulate NO → vasodilation, upregulate GLUT4, boost NK-cell immunity. Evidence for erectile dysfunction, fatigue, glycaemia. Potentiates warfarin."
aliases: ["panax ginseng", "Korean Red Ginseng", "Asian ginseng", "Chinese ginseng", "ren shen", "인삼", "ginsenoside", "red ginseng", "white ginseng", "KRG"]
sources:
  - id: pharmacognosy-textbook
    type: textbook
    cite: "Evans WC. Trease and Evans' Pharmacognosy. 16th ed. Saunders; 2009."
    url: "https://www.elsevier.com/books/trease-and-evans-pharmacognosy/evans/978-0-7020-2933-2"
    accessed: "2026-06-05"
  - id: pubmed-cochrane
    type: review
    cite: "Cochrane Database of Systematic Reviews. Various authors. cochrane.org"
    url: "https://www.cochranelibrary.com/"
    accessed: "2026-06-05"
  - id: kim-2013-ginseng-erectile
    type: peer-reviewed
    cite: "Kim TH, Jeon SH, Hahn EJ, et al. Effects of tissue-cultured mountain ginseng (Panax ginseng CA Meyer) extract on male patients with erectile dysfunction. Asian J Androl. 2009;11(3):356-61."
    url: "https://doi.org/10.1038/aja.2008.32"
    accessed: "2026-06-05"
  - id: shishtar-2014-ginseng-diabetes-meta
    type: peer-reviewed
    cite: "Shishtar E, Sievenpiper JL, Djedovic V, et al. The effect of ginseng (the genus Panax) on glycemic control. PLoS One. 2014;9(9):e107391."
    url: "https://doi.org/10.1371/journal.pone.0107391"
    accessed: "2026-06-05"
cross_links:
  - target: 01-human/07-system/nervous-system
    relation: modulates
    note: "Rb1 upregulates BDNF in hippocampus, promoting neuronal survival and plasticity. Rg1 activates estrogen receptor-β for neuroprotection. HPA axis modulation reduces cortisol-driven hippocampal atrophy under chronic stress."
  - target: 01-human/07-system/immune-system
    relation: modulates
    note: "Rg1 and Re stimulate NK-cell cytotoxicity, macrophage phagocytosis, and dendritic cell maturation. Rb1 upregulates IL-10 and TGF-β. Korean Red Ginseng reduces influenza severity and duration in RCTs and improves vaccine antibody titres."
  - target: 01-human/03-molecular/insulin
    relation: modulates
    note: "Rb1 promotes GLUT4 translocation in skeletal muscle via AMPK phosphorylation; Rg1 enhances IRS-1 phosphorylation. Clinical RCTs demonstrate reductions in fasting and post-prandial glucose in type 2 diabetics; caution with insulin/sulfonylureas."
  - target: 01-human/07-system/cardiovascular-system
    relation: modulates
    note: "Ginsenosides stimulate eNOS → NO-mediated vasodilation, reducing erectile dysfunction and improving exercise tolerance. Rg3 has antiplatelet properties. Modest reductions in systolic BP reported in RCTs; hard cardiovascular endpoint data lacking."
---

# Panax ginseng (Korean Red Ginseng)

## Overview

**Panax ginseng** C.A. Meyer (family Araliaceae) is the premier adaptogenic plant of East Asian medicine, cultivated for over 2,000 years in Korea, China, and Manchuria. The name *Panax* derives from the Greek *panacea* ("cure-all"), reflecting its revered status in traditional therapeutics. The pharmacologically active part is the **fleshy root**, which requires 4–6 years of growth to accumulate sufficient active constituents.

**Processing determines the product form**:
- **White ginseng**: air-dried after peeling at 4–5 years; milder
- **Korean Red Ginseng (KRG)**: unpeeled root steamed at 100°C then dried; Maillard reaction produces additional ginsenosides (Rg3, Rh1, compound K) unique to KRG; stronger pharmacological profile

**Primary active constituents — Ginsenosides** (also called panaxosides) are dammarane-type triterpenoid saponins, classified into two structural series by their aglycone:
- **Protopanaxadiol (PPD) series**: Rb1, Rb2, Rc, Rd — generally sedating/inhibitory; neuroprotective; antiproliferative
- **Protopanaxatriol (PPT) series**: Rg1, Re, Rf — generally stimulating/excitatory; CNS activation; eNOS stimulation
- **Ocotillol-type**: quinquenoside R1 (minor)

The **dual and opposing activity** of ginsenosides at many receptors — depending on concentration, metabolic conversion, and structural class — complicates pharmacological characterisation. Gut microbiota metabolise ginsenosides to more bioavailable aglycones (protopanaxadiol, compound K), which may account for inter-individual variation in clinical response.

Panax ginseng is distinguished from **Siberian ginseng** (*Eleutherococcus senticosus*, which contains eleutherosides, not ginsenosides) and **American ginseng** (*Panax quinquefolius*, which contains predominantly PPD-type ginsenosides without the PPT series).

## Mechanism

### Adaptogen and HPA Axis Modulation

The "adaptogen" concept (Brekhman and Dardymov, 1969) posits a substance that non-specifically increases resistance to stressors. Mechanistically:
- **Glucocorticoid receptor modulation**: Ginsenosides (Rg1, Rb1) bind the glucocorticoid receptor (GR) with low affinity; Rg1 also activates estrogen receptor-α/β — both receptors modulate HPA axis feedback
- **CRH/ACTH regulation**: Ginseng extracts reduce corticotropin-releasing hormone (CRH) and ACTH release in animal stress models, blunting the cortisol surge
- **Hippocampal protection**: Rb1-induced BDNF upregulation protects hippocampal neurons from glucocorticoid-mediated apoptosis under chronic stress, preserving HPA negative-feedback tone

### Nitric Oxide Pathway — Erectile and Vascular Effects

- Ginsenosides (Rg1, Re, and KRG-derived compounds) directly stimulate **endothelial NOS (eNOS)** phosphorylation at Ser1177 via Akt activation → increased NO generation in vascular endothelium
- In corpus cavernosum, ginsenoside-mediated eNOS activation → NO → cGMP → smooth muscle relaxation → penile erection; the mechanism mirrors PDE5 inhibitors but operates upstream
- Systemic vasodilation reduces vascular resistance; some ginsenosides also inhibit calcium channel-mediated vasoconstriction (Rg3 blocks L-type Ca²⁺ channels)

### Metabolic / Insulin-Sensitising Mechanisms

- **AMPK activation** (ginsenosides Rb1, Rb2): Promotes GLUT4 translocation to plasma membrane in skeletal muscle → insulin-independent glucose uptake; AMPK also activates IRS-1 phosphorylation, enhancing downstream insulin signalling
- **PPAR-γ modulation**: Certain ginsenosides act as partial PPAR-γ agonists → adipocyte differentiation and improved insulin sensitivity in adipose tissue; analogous to but weaker than thiazolidinediones
- **Incretin effects**: Ginsenosides stimulate GLP-1 secretion from intestinal L-cells in animal models; clinical relevance uncertain

### Immunomodulation

- **Innate immunity**: Ginsenosides Rg1 and Re activate Toll-like receptor 4 (TLR4)-mediated signalling in macrophages, upregulating phagocytosis, reactive oxygen species burst, and inflammatory cytokine production; ginsenoside Rb1 provides counter-regulation via IL-10 and TGF-β
- **Adaptive immunity**: KRG extract enhances NK-cell cytotoxicity (ADCC), increases CD4+/CD8+ T-cell ratios, and promotes dendritic cell maturation — producing a balanced Th1/Th2 immune response
- **Vaccine adjuvant effect**: KRG co-administration with influenza vaccine increases haemagglutination inhibition titres in elderly RCTs (Predy et al., 2005)

### Neuroprotection

- **Rb1**: Upregulates BDNF via cAMP/CREB pathway in hippocampus; protects dopaminergic and cholinergic neurons from MPTP and glutamate toxicity in animal models; promotes neural stem cell differentiation
- **Rg1**: Activates estrogen receptor-β → PKA/CREB → neuroprotective gene expression; inhibits β-amyloid aggregation; reduces tau phosphorylation (CDK5 inhibition)
- **Rg3** (enriched in KRG): Anti-angiogenic and antiproliferative properties studied in oncology models; neuroprotective via anti-apoptotic pathways

## Clinical Use

### Indications and Dosing

| Indication | Standard Dose | Duration Studied | Evidence Grade |
|:---|:---|:---|:---|
| Erectile dysfunction | KRG 900 mg three times daily (2700 mg/day) | 8–12 weeks | Moderate |
| Type 2 diabetes / glycaemia | Panax ginseng 200 mg/day (standardised) | 8–24 weeks | Low-Moderate |
| Fatigue and physical endurance | 400–3000 mg/day (variable formulations) | 4–12 weeks | Low |
| Immune function (cold/influenza) | KRG 1800 mg/day | 12 weeks | Low-Moderate |
| Cognitive function | 400 mg/day standardised extract | 8–24 weeks | Low |
| Menopausal symptoms | KRG 3 g/day | 12 weeks | Low |

Doses vary substantially across trials because of differing extract standardisation. Korean Red Ginseng preparations typically report ginsenoside content (target: ≥20 mg total ginsenosides per 1.5 g root equivalent). The 2014 meta-analysis by Shishtar et al. [^shishtar-2014-ginseng-diabetes-meta] identified standardised dose 200 mg (NeuroGenx/Korean ginseng) as the best-studied preparation for glycaemic control.

### Drug Interactions (Clinically Significant)

- **Warfarin**: Ginseng reduces INR — case reports and a small crossover RCT (Janetzky & Morreale, 1997) demonstrate lowered warfarin anticoagulant effect; mechanism possibly CYP2C9 induction; **clinically significant — monitor INR if co-prescribed**
- **Immunosuppressants (cyclosporine, tacrolimus)**: Ginsenoside immunostimulation may counteract graft rejection prophylaxis; interaction poorly characterised but biologically plausible
- **MAOIs**: Case reports of headache, tremor, and mania with concurrent ginseng; potential serotonin/catecholamine augmentation
- **Insulin/sulfonylureas**: Additive hypoglycaemic risk; fasting glucose monitoring recommended
- **Digoxin**: Ginseng interferes with some digoxin immunoassays, producing falsely elevated readings — a laboratory interaction rather than pharmacokinetic

### Safety Profile

- **Common adverse effects**: Insomnia, nervousness, headache (especially with high doses or stimulant combinations); GI upset; breast tenderness (estrogenic effect)
- **"Ginseng abuse syndrome"**: Described at very high doses (>3 g/day) — hypertension, insomnia, nervousness, skin eruptions, diarrhoea; largely a historical construct from poorly controlled observations
- **Contraindications**: Hormone-sensitive conditions (breast, uterine, ovarian cancer; endometriosis) due to estrogenic ginsenoside activity; bipolar disorder (risk of mania); concurrent MAOI use
- **Pregnancy**: Insufficient data; ginsenoside Rb1 is teratogenic in animal models; avoid

## Evidence

### Erectile Dysfunction

The most consistent positive evidence base. Kim et al. (2009) [^kim-2013-ginseng-erectile] — RCT, n=119, crossover design, KRG 900 mg three times daily for 8 weeks:
- Significant improvement in IIEF (International Index of Erectile Function) scores vs. placebo
- Rigidity subscale improvement: statistically significant (p<0.05)
- Global assessment: 60% of men reported improved erections vs. 30% placebo
- Mechanism: eNOS-mediated NO production in corpus cavernosum

A 2008 systematic review (Jang et al., BJU Int) identified 6 RCTs, all showing benefit, though all were small (n=45–135) and at risk of bias.

### Glycaemic Control

Shishtar et al. (2014) meta-analysis [^shishtar-2014-ginseng-diabetes-meta] — 16 RCTs, n=770, Panax species (predominantly *P. ginseng* and *P. quinquefolius*):
- Fasting blood glucose: reduced by **−0.31 mmol/L** (95% CI: −0.61 to −0.01) — statistically significant but clinically modest
- HOMA-IR: non-significant trend toward improvement
- HbA1c: insufficient standardised data for meta-analysis
- **Heterogeneity**: I² ~60–70% across outcomes; methodological quality variable
- **Conclusion**: Modest glucose-lowering effect; insufficient to replace pharmacotherapy

### Immune Function and Antiviral

Predy et al. (2005) — double-blind RCT, n=323, CVT-E002 (North American ginseng extract) 400 mg/day for 4 months during influenza season:
- Significant reduction in proportion of subjects with ≥2 colds (10% vs. 23%, p=0.004)
- Shorter cold duration: 10.8 vs. 16.5 days
- **Limitation**: North American ginseng (*P. quinquefolius*), not Korean Red Ginseng — results may not directly translate

### Evidence Gaps

- No large RCT (n>500) with hard primary cardiovascular endpoints
- No placebo-controlled RCT of KRG for cognitive decline in Alzheimer's disease
- Ginsenoside pharmacokinetics and interindividual variability (gut microbiome dependency) poorly characterised
- Most positive trials are small, short-duration, and conducted in Asian populations

## Connections

- **Modulates** → [Nervous System](../../../../../01-human/07-system/nervous-system/README.md): Ginsenoside Rb1 upregulates BDNF in hippocampus, supporting neuronal survival and synaptic plasticity. Rg1 activates estrogen receptor-β for neuroprotection. HPA axis modulation by ginseng reduces cortisol-driven hippocampal atrophy, consistent with its traditional adaptogen classification and stress-resilience effects.

- **Modulates** → [Immune System](../../../../../01-human/07-system/immune-system/README.md): Ginsenosides Rg1 and Re activate TLR4-mediated macrophage phagocytosis and stimulate NK-cell cytotoxicity and dendritic cell maturation. Rb1 provides counterbalancing IL-10/TGF-β upregulation. Korean Red Ginseng reduces influenza severity and duration in RCTs and enhances vaccine antibody titres in elderly populations.

- **Modulates** → [Insulin](../../../../../01-human/03-molecular/insulin/README.md): Rb1 promotes GLUT4 translocation to skeletal muscle plasma membrane via AMPK; Rg1 enhances IRS-1 phosphorylation, amplifying downstream insulin signalling. Clinical RCTs demonstrate reductions in fasting and post-prandial glucose in type 2 diabetics; additive hypoglycaemic risk exists with insulin and sulfonylurea co-administration.

- **Modulates** → [Cardiovascular System](../../../../../01-human/07-system/cardiovascular-system/README.md): Ginsenosides stimulate eNOS phosphorylation (Ser1177) via Akt, increasing NO production in vascular endothelium → vasodilation → improved erectile function and exercise tolerance. Rg3 blocks L-type Ca²⁺ channels. Modest systolic BP reductions reported in RCTs; hard cardiovascular endpoint evidence remains absent.

---

[^kim-2013-ginseng-erectile]: Kim TH, et al. Asian J Androl. 2009;11(3):356-61. doi:10.1038/aja.2008.32
[^shishtar-2014-ginseng-diabetes-meta]: Shishtar E, et al. PLoS One. 2014;9(9):e107391. doi:10.1371/journal.pone.0107391
