---
schema: human-scale-entry/v1
id: obesity
name: Obesity
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-08
summary: "Obesity (BMI ≥30; 650M affected) is driven by genetic (FTO, MC4R), neuroendocrine (leptin resistance), gut-microbiome, and environmental factors; adipose inflammation causes metabolic syndrome; GLP-1 receptor agonists (semaglutide) achieve 15-20% weight loss."
aliases: ["obesity", "adiposity", "BMI", "metabolic syndrome", "leptin resistance", "GLP-1 agonist", "semaglutide", "tirzepatide", "adipose tissue", "central obesity"]
sources:
  - id: bluher-2019-obesity-review
    type: peer-reviewed
    cite: "Blüher M. Obesity: global epidemiology and pathogenesis. Nat Rev Endocrinol. 2019;15(5):288-298."
    doi: "10.1038/s41574-019-0176-8"
    pmid: "30814686"
    url: "https://doi.org/10.1038/s41574-019-0176-8"
    accessed: "2026-06-08"
  - id: wilding-2021-semaglutide-step1
    type: peer-reviewed
    cite: "Wilding JPH, Batterham RL, Calanna S, et al. Once-weekly semaglutide in adults with overweight or obesity. N Engl J Med. 2021;384(11):989-1002."
    doi: "10.1056/NEJMoa2032183"
    pmid: "33567185"
    url: "https://doi.org/10.1056/NEJMoa2032183"
    accessed: "2026-06-08"
  - id: backhed-2004-gut-microbiome-obesity
    type: peer-reviewed
    cite: "Bäckhed F, Ding H, Wang T, et al. The gut microbiota as an environmental factor that regulates fat storage. Proc Natl Acad Sci USA. 2004;101(44):15718-15723."
    doi: "10.1073/pnas.0407076101"
    pmid: "15505215"
    url: "https://doi.org/10.1073/pnas.0407076101"
    accessed: "2026-06-08"
cross_links:
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Adipocyte-secreted leptin signals satiety via hypothalamic LepR/JAK2/STAT3; common obesity involves leptin resistance (elevated leptin, impaired STAT3 signaling via SOCS3 upregulation); monogenic LEP deficiency causes morbid childhood obesity treatable with metreleptin."
  - target: 01-human/03-molecular/ghrelin
    relation: connects-to
    note: "Ghrelin, released by gastric A-like cells during fasting, stimulates appetite via hypothalamic GHSR; ghrelin is paradoxically low in obesity but meal-suppression is blunted; GLP-1 receptor agonists (semaglutide) suppress ghrelin, contributing to appetite and weight reduction."
  - target: 01-human/03-molecular/glp-1
    relation: connects-to
    note: "GLP-1, secreted by intestinal L-cells in response to nutrients, potentiates insulin release and suppresses glucagon and appetite; GLP-1/GIP receptor agonists (semaglutide 15%, tirzepatide 22% body weight loss) are the most effective pharmacological obesity treatments available."
  - target: 01-human/03-molecular/insulin
    relation: connects-to
    note: "Chronic hyperinsulinemia in obesity drives mTORC1-mediated S6K1 → IRS-1 serine phosphorylation → insulin resistance; adipose inflammation (IL-6, TNF-α via IKKβ/NF-κB) impairs insulin signaling; type 2 diabetes develops when pancreatic β-cell compensation fails."
  - target: 01-human/07-system/gut-microbiome
    relation: connects-to
    note: "Dysbiosis in obesity — increased Firmicutes/Bacteroidetes ratio, reduced Akkermansia muciniphila — increases energy harvest and drives metabolic endotoxemia (LPS → TLR4 → systemic inflammation); gut microbiome transfer from obese to germ-free mice transfers adiposity phenotype."
  - target: 01-human/03-molecular/npy
    relation: connects-to
    note: "ARC NPY/AgRP neurons are master orexigenic drivers: NPY → Y1R/Y5R on PVN → increased food intake and reduced energy expenditure; ghrelin activates and leptin/insulin suppress ARC NPY/AgRP; NPY Leu7Pro polymorphism associates with higher BMI and metabolic syndrome risk."
  - target: 01-human/03-molecular/growth-hormone
    relation: connects-to
    note: "GH deficiency increases visceral adiposity and dyslipidemia, phenocopying metabolic syndrome; GH therapy reduces visceral fat ~15-20% in deficient adults; obesity-driven leptin resistance suppresses GHRH pulsatility → blunted GH amplitude; weight loss restores GH dynamics."
  - target: 01-human/03-molecular/testosterone
    relation: connects-to
    note: "Visceral adiposity suppresses testosterone via aromatase upregulation and SHBG reduction; hypogonadal-obesity cycle: T deficiency worsens adiposity, which further suppresses T; 5-10% weight loss raises testosterone 2-3 nmol/L without TRT; TRT reduces fat mass ~3 kg."
  - target: 01-human/03-molecular/thyroid-hormones
    relation: connects-to
    note: "Thyroid hormones set basal metabolic rate — hypothyroidism reduces BMR → weight gain; T3 drives UCP1 in BAT (thermogenesis) and mitochondrial biogenesis; TRβ agonist resmetirom reduces hepatic fat in MASH; levothyroxine normalizes TSH but does not reliably reverse obesity."
  - target: 01-human/03-molecular/melatonin
    relation: connects-to
    note: "Circadian disruption (night-shift work, social jet lag) → disrupted melatonin → leptin resistance → 40% higher obesity risk; light at night suppresses melatonin → metabolic dysregulation; MTNR1B variants modulate BMI; melatonin reduces adiposity in rodent models."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Adipose tissue secretes adiponectin, but obese adipocytes paradoxically produce less: visceral fat expansion → TNF-α/IL-6 → ADIPOQ suppression → adiponectin deficiency → insulin resistance and cardiovascular risk; TZDs and caloric restriction restore adiponectin."
  - target: 01-human/07-system/type-2-diabetes
    relation: connects-to
    note: "Obesity is the dominant cause of type 2 diabetes: excess adipose tissue drives insulin resistance via free fatty acids and inflammatory adipokines, so the obesity epidemic powers the diabetes epidemic—and weight loss can put type 2 diabetes into remission."
  - target: 01-human/07-system/nash
    relation: connects-to
    note: "Obesity is the leading driver of NASH: visceral fat floods the liver with free fatty acids, causing steatosis that inflames into steatohepatitis, fibrosis, and cirrhosis—the hepatic arm of the same metabolic syndrome that links obesity to diabetes and heart disease."
  - target: 01-human/04-cellular/adipocyte
    relation: connects-to
    note: "Adipocytes are the cellular engine of obesity: as they enlarge with triglyceride they turn dysfunctional, secreting leptin and inflammatory cytokines, less adiponectin, and recruiting macrophages—so adipose acts as an endocrine organ driving obesity's complications."
  - target: 01-human/07-system/atherosclerosis
    relation: connects-to
    note: "Obesity accelerates atherosclerosis and cardiovascular disease: visceral fat drives dyslipidemia, hypertension, insulin resistance and chronic inflammation that injure arteries—a central, modifiable driver of heart attack and stroke."
  - target: 01-human/07-system/endometrial-cancer
    relation: connects-to
    note: "Obesity is the strongest modifiable risk factor for endometrial cancer: adipose tissue aromatizes androgens into estrogen, and unopposed estrogen drives endometrial proliferation, so most endometrial cancers are obesity-related—a hormone-mediated obesity cancer."
  - target: 01-human/07-system/colorectal-cancer
    relation: connects-to
    note: "Obesity raises colorectal cancer risk: insulin/IGF-1 signaling, chronic inflammation and altered gut flora from excess adiposity promote colonic tumorigenesis, contributing to rising early-onset colorectal cancer."
  - target: 01-human/03-molecular/dopamine
    relation: connects-to
    note: "Obesity engages the brain's dopamine reward system: highly palatable food drives dopamine release like other rewards, and blunted reward signaling can promote overeating to compensate—so food intake is partly an addiction-like behavior, not simple appetite."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "Obesity directly damages the heart: excess volume load and fat-driven inflammation cause obesity cardiomyopathy and heart failure with preserved ejection fraction, so the heart strains under both the metabolic and mechanical burden of excess weight."
  - target: 01-human/07-system/breast-cancer
    relation: connects-to
    note: "Obesity raises postmenopausal breast cancer risk: after menopause, adipose tissue becomes the main estrogen source via aromatase, so excess fat sustains estrogen signaling that drives hormone-receptor-positive breast cancer—an endocrine link between fat and cancer."
---

# Obesity

## Overview

**Obesity** is a chronic, relapsing metabolic disorder defined by **excess adipose tissue accumulation** sufficient to impair health, conventionally classified by body mass index (BMI):

| Classification | BMI (kg/m²) | Global prevalence |
|:---|:---|:---|
| Overweight | 25.0–29.9 | ~38% adults |
| Obesity Class I | 30.0–34.9 | ~13% adults |
| Obesity Class II | 35.0–39.9 | ~5% adults |
| Obesity Class III (severe) | ≥40 | ~2% adults |

**Epidemiology:** As of 2024, over **650 million adults** globally are obese (BMI ≥30) and over 1 billion overweight — representing a 3× increase since 1975. Obesity is projected to exceed 50% of US adults by 2030. The disorder reduces life expectancy by 3–10 years depending on severity, is the leading preventable cause of type 2 diabetes, cardiovascular disease, obstructive sleep apnea, osteoarthritis, non-alcoholic steatohepatitis (NASH), and multiple cancers [^bluher-2019-obesity-review].

Obesity is not a simple behavioral failure but a **complex neuroendocrine disorder** with strong genetic determinants (heritability ~40–70%), driven by dysregulated appetite regulation, adipokine signaling, gut-brain axis communication, and the obesogenic food environment. The revolution in understanding its biology — particularly the leptin axis (1994) and GLP-1 receptor agonist pharmacology — has transformed treatment from ineffective counseling to highly effective, mechanism-targeted pharmacotherapy.

## Structure

### Adipose tissue biology

Adipose tissue is not merely an energy depot but an active **endocrine organ** with two functionally distinct compartments:

**White adipose tissue (WAT):**
- Stores triglycerides in large unilocular lipid droplets
- Secretes **adipokines**: leptin (satiety signal), adiponectin (insulin sensitizer), resistin, visfatin, TNF-α, IL-6
- **Visceral WAT** (omental, mesenteric): metabolically harmful; directly drains into portal circulation → hepatic lipotoxicity; inflammatory adipokine secretion correlates with metabolic syndrome risk
- **Subcutaneous WAT**: metabolically more benign; leptin-rich depot that reflects overall energy status

**Brown adipose tissue (BAT):**
- Multilocular lipid droplets; rich in mitochondria expressing **UCP1** (uncoupling protein 1 / thermogenin)
- UCP1 uncouples oxidative phosphorylation → heat generation (non-shivering thermogenesis) at the expense of ATP synthesis
- Active BAT correlates with leanness; cold exposure, β3-adrenergic agonists, and FGF21 activate BAT
- BAT is a target for obesity pharmacology (thyromimetics, β3-AR agonists)

**Beige/brite adipocytes:**
- White adipocytes that acquire brown-fat-like characteristics (UCP1 expression) upon sympathetic stimulation or cold — **WAT browning**
- PRDM16 transcription factor is the master regulator of beige adipocyte differentiation
- Irisin (FNDC5 cleavage product, released by muscle during exercise) promotes WAT browning

### Hypothalamic appetite circuits

The **arcuate nucleus (ARC)** of the hypothalamus integrates peripheral satiety and hunger signals via two antagonistic neuron populations:

**ARC POMC/CART neurons (anorexigenic):**
- Respond to leptin, insulin, GLP-1, PYY → release α-MSH → melanocortin 4 receptor (MC4R) activation in paraventricular nucleus → satiety and reduced feeding
- α-MSH is the agonist of MC4R (the most common monogenic obesity gene in humans — 2–5% of severe obesity)

**ARC AgRP/NPY neurons (orexigenic):**
- Inhibited by leptin and insulin; activated by ghrelin → release NPY and AgRP (endogenous MC4R antagonist) → stimulate feeding
- These neurons drive hunger during caloric restriction; hyperactive in obesity via leptin resistance

**Melanocortin pathway mutations causing monogenic obesity:**
- **MC4R LOF** (~2–5% of severe obesity): hyperphagia, normal height, obesity
- **LEP (leptin) LOF** (<0.01%): severe hyperphagia, morbid obesity from infancy; treatable with recombinant metreleptin
- **LEPR (leptin receptor) LOF**: similar to LEP deficiency; hypogonadotropic hypogonadism in addition
- **POMC LOF**: adrenal insufficiency (loss of ACTH) + red hair (loss of MSH pigment) + early obesity

## Function

### Energy balance: the set point problem

The body defends a **body weight set point** determined by hypothalamic arcuate circuits. Caloric restriction activates multiple counter-regulatory mechanisms to restore weight:
- Leptin levels fall → AgRP neurons activate → hunger increases dramatically
- Metabolic rate decreases (reduced thyroid hormone, sympathetic tone)
- Ghrelin rises → additional hunger drive

This **adaptive thermogenesis** explains why most dietary interventions fail long-term: the body fights weight loss at the hormonal/neural level. Up to 80% of lost weight is regained within 5 years without pharmacological maintenance.

### Adipose tissue inflammation (metainflammation)

In obesity, adipocytes expand to pathological sizes → **hypoxia within the adipose depot** → macrophage infiltration (M1-polarized, pro-inflammatory):

1. **Dead adipocyte "crown-like structures":** Lipid-laden macrophage accumulations around dying adipocytes
2. **Adipokine dysregulation:** Elevated TNF-α, IL-6, MCP-1 (CCL2); reduced anti-inflammatory adiponectin
3. **Free fatty acid (FFA) spill-over:** Lipolysis in dysfunctional adipocytes → elevated circulating FFAs → ectopic lipid deposition in liver, skeletal muscle, heart, pancreas → lipotoxicity
4. **TLR4 activation by saturated FFAs and LPS (from gut dysbiosis):** NF-κB activation → chronic low-grade systemic inflammation → insulin resistance

This **metainflammation** mechanistically links obesity to type 2 diabetes, atherosclerosis, NASH, and certain cancers (via adipokine-driven inflammation and IGF-1/insulin signaling).

### Genetic architecture of common obesity

**Monogenic obesity** (<5% of severe cases): MC4R, LEP, LEPR, POMC, PCSK1, SIM1, KSR2.

**Polygenic common obesity (>95% of cases):**
- Most strongly associated common variant: **FTO (rs9939609)** — intronic SNP; actual causal mechanism involves altered transcriptional regulation of nearby **IRX3 and IRX5** genes → reduced brown adipose tissue activity and thermogenesis
- **>900 loci** identified by GWAS (2023); most enriched in CNS pathways (appetite regulation, reward) rather than adipocyte-specific pathways — confirming obesity as primarily a brain-regulated set point disorder
- Polygenic risk score (PRS) for obesity predicts risk 2–4× better than any single gene

## Pathology

### Metabolic consequences

**Metabolic syndrome** (central obesity + 2 of: elevated TG, low HDL, hypertension, elevated fasting glucose):
- Present in ~40% of obese adults
- Driven by visceral adipose inflammation, hepatic lipotoxicity, and insulin resistance

**Type 2 diabetes:**
- 80–90% of T2D patients have overweight or obesity
- Mechanism: insulin resistance → compensatory hyperinsulinemia → β-cell exhaustion → T2D; each 1 kg/m² BMI increase → ~6% higher T2D risk

**Cardiovascular disease:**
- Obesity-associated hypertension (visceral adipose → increased renin-angiotensin; insulin → sodium retention)
- Dyslipidemia (small dense LDL, elevated TG, low HDL)
- Cardiomyopathy (lipotoxicity, adipokine effects on myocardium)

**Cancer:**
- Obesity-associated cancers: endometrial (2-4×), postmenopausal breast (1.5×), colon (1.5-2×), kidney (1.5-2×), esophageal adenocarcinoma (7×), pancreatic (1.5×)
- Mechanisms: hyperinsulinemia/IGF-1 (pro-proliferative), adipose inflammation, estrogen production by adipose aromatase (endometrial/breast), altered bile acid metabolism (colorectal)

### Treatment

**Lifestyle modification:**
- Diet + physical activity: 5–10% weight loss achievable; significant metabolic benefit even without normalization of BMI; typically regained within 5 years

**Pharmacotherapy:**
| Drug | Mechanism | Weight loss | FDA approval |
|:---|:---|:---|:---|
| **Semaglutide (Wegovy)** | GLP-1 receptor agonist | ~15% (STEP 1) [^wilding-2021-semaglutide-step1] | 2021 (obesity) |
| **Tirzepatide (Zepbound)** | GLP-1 + GIP dual agonist | ~22% (SURMOUNT-1) | 2023 (obesity) |
| **Naltrexone-bupropion (Contrave)** | Opioid antagonist + dopamine/NE reuptake inhibitor | ~5-6% | 2014 |
| **Phentermine-topiramate (Qsymia)** | Amphetamine + anticonvulsant | ~8-10% | 2012 |
| **Orlistat (Xenical)** | Pancreatic lipase inhibitor | ~3-4% | 1999 |

**Bariatric surgery:**
- Roux-en-Y gastric bypass (RYGB): ~30% EWL at 5 years; T2D remission in 60–80% (precedes weight loss → involves GLP-1, bile acid, microbiome effects)
- Sleeve gastrectomy: ~25% EWL; simpler; no intestinal rerouting; standard first-line bariatric procedure
- RYGB vs. best medical therapy: surgery superior for T2D remission, CV events, and mortality (STAMPEDE, Swedish Obese Subjects study)

**Emerging treatments:**
- **CagriSema (cagrilintide + semaglutide):** ~25% weight loss in Phase 3 (REDEFINE-1)
- **Retatrutide (GLP-1/GIP/glucagon triple agonist):** ~24% at 48 weeks (Phase 2)
- **Leptin sensitizers and MC4R agonists** (setmelanotide: FDA-approved for POMC/PCSK1/LEPR deficiency)
- **Adipose tissue engineering:** Targeting UCP1 activation in WAT via β3-AR agonism, thyromimetics, or PRDM16 induction

## Connections

- `connects-to` → **[Leptin](../../../03-molecular/leptin/README.md)** — Leptin, secreted by adipocytes proportional to fat mass, signals satiety via hypothalamic LepR/JAK2/STAT3; common obesity involves leptin resistance (high leptin levels, impaired signaling) driven by SOCS3; monogenic leptin deficiency causes severe childhood obesity treatable with recombinant metreleptin.

- `connects-to` → **[Ghrelin](../../../03-molecular/ghrelin/README.md)** — Ghrelin rises during fasting and stimulates appetite via hypothalamic GHSR; ghrelin levels are paradoxically reduced in common obesity but the meal-suppression response is blunted; GLP-1 receptor agonists suppress ghrelin release, contributing to profound appetite reduction.

- `connects-to` → **[GLP-1](../../../03-molecular/glp-1/README.md)** — GLP-1, secreted by intestinal L-cells post-meal, potentiates insulin release, suppresses glucagon, and reduces appetite via hypothalamic GLP-1R; GLP-1/GIP receptor agonists (semaglutide ~15%, tirzepatide ~22% weight loss) are the most effective pharmacological obesity treatments available.

- `connects-to` → **[Insulin](../../../03-molecular/insulin/README.md)** — Chronic hyperinsulinemia in obesity drives mTORC1/S6K1 → IRS-1 serine phosphorylation → insulin resistance; adipose inflammation via IKKβ/NF-κB further impairs insulin signaling; type 2 diabetes develops when pancreatic β-cell compensation fails under sustained metabolic demand.

- `connects-to` → **[Gut Microbiome](../../gut-microbiome/README.md)** — Dysbiosis in obesity — increased Firmicutes/Bacteroidetes ratio, reduced Akkermansia muciniphila — increases energy harvest and drives metabolic endotoxemia (LPS → TLR4 → systemic inflammation); gut microbiome transfer from obese to germ-free mice transfers the adiposity phenotype.

- `connects-to` → **[NPY](../../../03-molecular/npy/README.md)** — ARC NPY/AgRP neurons are master orexigenic drivers: NPY → Y1R/Y5R on PVN → increased food intake and reduced energy expenditure; ghrelin activates and leptin/insulin suppress ARC NPY/AgRP; NPY Leu7Pro polymorphism associates with higher BMI and metabolic syndrome risk.
- `connects-to` → **[Growth Hormone](../../../03-molecular/growth-hormone/README.md)** — GH deficiency increases visceral adiposity and dyslipidemia, phenocopying metabolic syndrome; GH therapy reduces visceral fat ~15-20% in deficient adults; leptin resistance in obesity suppresses GHRH pulsatility → blunted GH amplitude; weight loss restores GH secretory dynamics.
- `connects-to` → **[Testosterone](../../../03-molecular/testosterone/README.md)** — Visceral adiposity suppresses testosterone via aromatase upregulation and SHBG reduction; hypogonadal-obesity cycle: T deficiency worsens adiposity, which further suppresses T; 5-10% weight loss raises testosterone 2-3 nmol/L without TRT; TRT reduces fat mass ~3 kg.
- `connects-to` → **[Thyroid Hormones](../../../03-molecular/thyroid-hormones/README.md)** — Thyroid hormones set basal metabolic rate — hypothyroidism reduces BMR → weight gain; T3 drives UCP1 in BAT (thermogenesis) and mitochondrial biogenesis; TRβ agonist resmetirom reduces hepatic fat in MASH; levothyroxine normalizes TSH but does not reliably reverse obesity.
- `connects-to` → **[Melatonin](../../../03-molecular/melatonin/README.md)** — Circadian disruption (night-shift work, social jet lag) → disrupted melatonin → leptin resistance → 40% higher obesity risk; light at night suppresses melatonin → metabolic dysregulation; MTNR1B variants modulate BMI; melatonin reduces adiposity in rodent models.
- `connects-to` → **[Adiponectin](../../../03-molecular/adiponectin/README.md)** — Adipose tissue secretes adiponectin, but obese adipocytes paradoxically produce less: visceral fat expansion → TNF-α/IL-6 → ADIPOQ suppression → adiponectin deficiency → insulin resistance and cardiovascular risk; TZDs and caloric restriction restore adiponectin.
- `connects-to` → **[Type 2 Diabetes](../type-2-diabetes/README.md)** — Obesity is the dominant cause of type 2 diabetes: excess adipose tissue drives insulin resistance via free fatty acids and inflammatory adipokines, so the obesity epidemic powers the diabetes epidemic—and weight loss can put type 2 diabetes into remission.
- `connects-to` → **[NASH](../nash/README.md)** — Obesity is the leading driver of NASH: visceral fat floods the liver with free fatty acids, causing steatosis that inflames into steatohepatitis, fibrosis, and cirrhosis—the hepatic arm of the same metabolic syndrome that links obesity to diabetes and heart disease.
- `connects-to` → **[Adipocyte](../../04-cellular/adipocyte/README.md)** — Adipocytes are the cellular engine of obesity: as they enlarge with triglyceride they turn dysfunctional, secreting leptin and inflammatory cytokines, less adiponectin, and recruiting macrophages—so adipose acts as an endocrine organ driving obesity's complications.
- `connects-to` → **[Atherosclerosis](../atherosclerosis/README.md)** — Obesity accelerates atherosclerosis and cardiovascular disease: visceral fat drives dyslipidemia, hypertension, insulin resistance and chronic inflammation that injure arteries—a central, modifiable driver of heart attack and stroke.
- `connects-to` → **[Endometrial Cancer](../endometrial-cancer/README.md)** — Obesity is the strongest modifiable risk factor for endometrial cancer: adipose tissue aromatizes androgens into estrogen, and unopposed estrogen drives endometrial proliferation, so most endometrial cancers are obesity-related—a hormone-mediated obesity cancer.
- `connects-to` → **[Colorectal Cancer](../colorectal-cancer/README.md)** — Obesity raises colorectal cancer risk: insulin/IGF-1 signaling, chronic inflammation and altered gut flora from excess adiposity promote colonic tumorigenesis, contributing to rising early-onset colorectal cancer.
- `connects-to` → **[Dopamine](../../03-molecular/dopamine/README.md)** — Obesity engages the brain's dopamine reward system: highly palatable food drives dopamine release like other rewards, and blunted reward signaling can promote overeating to compensate—so food intake is partly an addiction-like behavior, not simple appetite.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — Obesity directly damages the heart: excess volume load and fat-driven inflammation cause obesity cardiomyopathy and heart failure with preserved ejection fraction, so the heart strains under both the metabolic and mechanical burden of excess weight.
- `connects-to` → **[Breast Cancer](../breast-cancer/README.md)** — Obesity raises postmenopausal breast cancer risk: after menopause, adipose tissue becomes the main estrogen source via aromatase, so excess fat sustains estrogen signaling that drives hormone-receptor-positive breast cancer—an endocrine link between fat and cancer.

[^bluher-2019-obesity-review]: Blüher M. Obesity: global epidemiology and pathogenesis. *Nat Rev Endocrinol.* 2019;15(5):288-298. [doi:10.1038/s41574-019-0176-8](https://doi.org/10.1038/s41574-019-0176-8) · [PubMed 30814686](https://pubmed.ncbi.nlm.nih.gov/30814686/)
[^wilding-2021-semaglutide-step1]: Wilding JPH, Batterham RL, Calanna S, et al. Once-weekly semaglutide in adults with overweight or obesity. *N Engl J Med.* 2021;384(11):989-1002. [doi:10.1056/NEJMoa2032183](https://doi.org/10.1056/NEJMoa2032183) · [PubMed 33567185](https://pubmed.ncbi.nlm.nih.gov/33567185/)
[^backhed-2004-gut-microbiome-obesity]: Bäckhed F, Ding H, Wang T, et al. The gut microbiota as an environmental factor that regulates fat storage. *Proc Natl Acad Sci USA.* 2004;101(44):15718-15723. [doi:10.1073/pnas.0407076101](https://doi.org/10.1073/pnas.0407076101) · [PubMed 15505215](https://pubmed.ncbi.nlm.nih.gov/15505215/)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
