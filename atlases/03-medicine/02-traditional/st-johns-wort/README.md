---
schema: medicine-entry/v1
id: st-johns-wort
name: St. John's Wort (Hypericum perforatum)
atlas: 03-medicine
scale: 02-traditional
status: draft
last_reviewed: 2026-06-05
summary: "Hypericum perforatum. Hyperforin inhibits monoamine reuptake via TRPC6 channel; hypericin weakly inhibits MAO. Cochrane evidence supports efficacy in mild-moderate depression. CYP3A4/P-gp inducer — reduces cyclosporine, OCP, and antiretroviral levels."
aliases: ["St. John's Wort", "Hypericum perforatum", "SJW", "Johanniskraut", "hyperforin", "hypericin", "klamath weed", "goatweed", "tipton weed"]
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
  - id: linde-2008-cochrane-sjw
    type: review
    cite: "Linde K, Berner MM, Kriston L. St John's wort for major depression. Cochrane Database Syst Rev. 2008;(4):CD000448."
    url: "https://doi.org/10.1002/14651858.CD000448.pub3"
    accessed: "2026-06-05"
  - id: madabushi-2006-hyperforin-pxr
    type: peer-reviewed
    cite: "Madabushi R, Frank B, Drewelow B, et al. Hyperforin in St. John's wort drug interactions. Eur J Clin Pharmacol. 2006;62(3):225-33."
    url: "https://doi.org/10.1007/s00228-006-0096-z"
    accessed: "2026-06-05"
cross_links:
  - target: 01-human/07-system/nervous-system
    relation: modulates
    note: "Hyperforin activates TRPC6 → Na+ influx → inhibits vesicular reuptake of serotonin, dopamine, norepinephrine, GABA, and glutamate. This broad multi-transmitter reuptake inhibition is mechanistically distinct from selective SSRI or SNRI pharmacology."
  - target: 01-human/03-molecular/dopamine
    relation: modulates
    note: "Hyperforin TRPC6 activation inhibits DAT by raising presynaptic Na+, increasing dopaminergic tone. Hypericin weakly inhibits MAO-A/B, reducing dopamine catabolism. Their relative contribution to antidepressant effect remains unresolved."
  - target: 01-human/03-molecular/serotonin
    relation: modulates
    note: "Hyperforin inhibits SERT via TRPC6-mediated depolarization; hypericin MAO-A inhibition further amplifies serotonergic tone. Clinically significant serotonin syndrome risk with SSRIs, SNRIs, tramadol, or linezolid. FDA warns against combination use."
  - target: 01-human/06-organ/brain
    relation: modulates
    note: "Cochrane meta-analysis (29 RCTs, n>5000) confirms efficacy comparable to TCAs/SSRIs for mild-moderate depression with superior tolerability. Hyperforin-driven PXR activation induces CYP3A4, reducing plasma levels of hepatic substrates."
---

# St. John's Wort (Hypericum perforatum)

## Overview

**Hypericum perforatum** (family Hypericaceae) is a perennial herb native to Europe and western Asia, now widely naturalised across temperate regions worldwide. Its common name derives from the traditional harvest around St. John's Day (June 24), when the plant blooms. The "perforatum" epithet refers to the translucent secretory gland-like oil dots visible in leaves when held to light — these are lysigenous secretory ducts containing phloroglucinol derivatives.

**Traditional use** spans over 2,000 years: Hippocrates, Paracelsus, and Culpeper all described uses for wound healing, anxiety, nerve pain, and melancholy. In European folk medicine, it was used topically as an anti-inflammatory and internally for nervous disorders. This aligns well with modern pharmacological understanding of its antidepressant and anti-inflammatory mechanisms.

**Active constituents**:
- **Hyperforin** (phloroglucinol derivative, 2–5% in dried aerial parts; up to 5% in commercial extracts): the primary antidepressant compound; monoamine reuptake inhibitor via TRPC6 channel activation
- **Hypericin** (naphthodianthrone, 0.1–0.3%): historic "active constituent"; weak MAO-A/B inhibitor; photosensitiser (associated with phototoxicity adverse effect); was originally thought to be the primary active compound
- **Pseudohypericin** (naphthodianthrone, ~0.5%): co-occurring with hypericin; similar photosensitising properties
- **Flavonoids** (hyperoside, rutin, quercetin, amentoflavone): antioxidant and possibly anti-inflammatory contributions
- **Hyperforin is unstable**: oxidises rapidly in air and light; explains why stabilised extracts (WS 5570, with 5% hyperforin) and enteric formulations are pharmacologically different from unstabilised products

**Clinical importance**: St. John's Wort is the best-selling botanical antidepressant in Europe, particularly Germany, where it outsells synthetic antidepressants. It is a clinically significant source of pharmacokinetic drug interactions via CYP3A4 and P-glycoprotein induction.

## Mechanism

### Hyperforin — TRPC6 Channel-Mediated Monoamine Reuptake Inhibition

Hyperforin's mechanism of action is mechanistically unique among antidepressants, discovered by Müller and Rö (2001) and confirmed by Leuner et al. (2007):

1. **TRPC6 activation**: Hyperforin is a potent activator of **Transient Receptor Potential Canonical 6 (TRPC6)** channels, a sodium-permeable non-selective cation channel
2. **Na+ influx**: TRPC6 opening → Na+ influx into the presynaptic terminal → membrane depolarisation
3. **Electrochemical gradient collapse**: The vesicular monoamine transporters (VMAT2) and plasma membrane monoamine transporters (SERT, DAT, NET) all depend on the Na+ electrochemical gradient across the membrane; raised presynaptic [Na+] reduces the driving force for reuptake
4. **Consequence**: Simultaneous inhibition of reuptake of **serotonin (5-HT), dopamine (DA), norepinephrine (NE), GABA, and glutamate** — a non-selective, non-competitive multi-transmitter reuptake inhibitor
5. **pH-dependent mechanism**: Hyperforin also acts as a proton transporter (ionophore) in mitochondrial inner membranes, affecting vesicular pH and quantal size of neurotransmitter release

This mechanism contrasts sharply with SSRIs (selective SERT inhibition), SNRIs (SERT + NET), and TCAs (SERT + NET + multiple receptor blockade). The multi-transmitter reuptake inhibition via TRPC6 is unique to hyperforin.

### Hypericin — MAO Inhibition and Photosensitisation

- **MAO inhibition**: Hypericin inhibits MAO-A and MAO-B with IC50 values in the micromolar range — significantly weaker than pharmaceutical MAO inhibitors (phenelzine, tranylcypromine); not clinically relevant at standard doses
- **Photosensitiser**: Hypericin absorbs UV-A and UV-B light and generates singlet oxygen and free radicals in the excited triplet state → oxidative damage to lipid membranes in sun-exposed skin; explains photosensitivity adverse effect
- Pseudohypericin has similar photosensitising properties

### CYP3A4 and P-gp Induction — The Drug Interaction Mechanism

This is clinically the most important pharmacological property of St. John's Wort:
- **Hyperforin is a potent ligand of PXR** (Pregnane X Receptor, NR1I2), the nuclear receptor master regulator of drug metabolism genes
- Hyperforin-activated PXR heterodimerises with RXR and binds to PXREs (PXR response elements) in the promoter regions of CYP3A4 (the major drug-metabolising P450) and MDR1/ABCB1 (P-glycoprotein, the drug efflux pump)
- Result: **CYP3A4 mRNA and protein expression increases 3–8 fold**; P-gp expression increases 2–4 fold
- **Clinical consequence**: plasma levels of drugs metabolised by CYP3A4 or transported by P-gp are reduced substantially:

| Drug affected | Clinical consequence |
|:---|:---|
| Cyclosporine | Transplant rejection (multiple case series) |
| Tacrolimus | Transplant rejection |
| HIV antiretrovirals (indinavir, nevirapine) | Virological failure |
| Oral contraceptive pill (ethinylestradiol) | Contraceptive failure; breakthrough bleeding |
| Warfarin | Reduced INR; thrombosis risk |
| Digoxin (P-gp substrate) | Reduced plasma levels |
| Irinotecan, imatinib | Reduced antineoplastic efficacy |
| Midazolam, alprazolam | Reduced sedative effect |

### Anti-inflammatory and Other Mechanisms

- Hyperforin inhibits NF-κB activation and cyclooxygenase-1/2 at higher concentrations — may contribute to traditional wound-healing use
- Amentoflavone (biflavonoid): CNS benzodiazepine-binding site modulation; inhibits PDE; anxiolytic contribution uncertain

## Clinical Use

### Indications and Dosing

| Indication | Standard Dose | Preparation | Duration Studied | Evidence Grade |
|:---|:---|:---|:---|:---|
| Mild-moderate depression | 300 mg three times daily (900 mg/day) | LI 160 or WS 5570 (standardised) | 6–12 weeks | High (Cochrane) |
| Seasonal affective disorder | 300–900 mg/day | Standardised extract | 8 weeks | Moderate |
| Menopausal symptoms | 300–600 mg/day | Standardised extract | 12 weeks | Low |
| Anxiety | 300–600 mg/day | Standardised extract | 6–12 weeks | Low |
| Severe/major depression | Not recommended | — | — | Insufficient evidence |

**Standard extracts**:
- **LI 160** (Lichtwer Pharma): standardised to 0.3% hypericin; most-studied preparation in older trials
- **WS 5570** (Dr. Willmar Schwabe): standardised to 0.3% hypericin + **3% hyperforin** (higher and more stable); used in more recent mechanistically-informed trials
- Doses and preparations are not interchangeable — LI 160 and WS 5570 show comparable efficacy but WS 5573 (low-hyperforin variant) was less effective in one RCT, supporting hyperforin's importance

### Drug Interactions — Critical Warnings

**Must be avoided or closely monitored with**:
- Cyclosporine / tacrolimus (transplant recipients) — **absolute contraindication**
- HIV protease inhibitors and NNRTIs — **avoid** (virological failure documented)
- Combined oral contraceptive pill — **switch to alternative contraception**
- Warfarin — **monitor INR closely; likely need dose increase**
- SSRIs, SNRIs, MAOIs, tramadol — **serotonin syndrome risk** (additive serotonergic effects)
- Digoxin — **monitor drug levels**

### Safety

- **Photosensitivity**: Fair-skinned individuals; avoid excessive sun exposure; especially with high-dose hypericin preparations
- **Drug interactions**: By far the dominant safety concern; patient self-medication without physician awareness is common
- **Serotonin syndrome**: Can occur when combined with SSRIs (case reports of agitation, myoclonus, diaphoresis, hyperthermia); risk is real though severity varies
- **Induction washout period**: CYP3A4 induction persists for 1–2 weeks after discontinuation; bridging period needed before starting sensitive CYP3A4-substrate drugs
- **Discontinuation**: Tapering recommended for patients on maintenance therapy to avoid rebound depressive symptoms

## Evidence

### Cochrane Systematic Review — The Definitive Evidence Base

Linde, Berner, and Kriston (2008) [^linde-2008-cochrane-sjw] — the most comprehensive systematic review:
- **29 RCTs included**; **n > 5,000 patients** with depressive disorders
- Comparisons: vs. placebo (17 trials) and vs. synthetic antidepressants (13 trials: TCAs and SSRIs)

**vs. Placebo**:
- Remission rates: RR 2.77 (95% CI: 1.87–4.11) for mild-moderate depression
- Superior to placebo across multiple depression scales (HAM-D, BDI, CGI)

**vs. Standard antidepressants** (TCAs and SSRIs pooled):
- Similar efficacy: RR for response 1.02 (95% CI: 0.92–1.13) — non-inferior
- **Superior tolerability**: Dropout rate due to adverse effects: SJW 0–3%, TCAs 10–15%, SSRIs 3–6%

**Subgroup finding** (crucial for interpretation):
- Trials in **Germany and other European countries** (where SJW is licensed, standardised, and prescribed by physicians): consistent positive results
- Trials in **USA and UK** (where SJW is unregulated, purchased OTC, product quality variable): more inconsistent results, more negative outcomes
- This geographic discrepancy suggests **product standardisation and quality are critical determinants of efficacy**

### Key Individual Trials

- **Harrer et al. (1994)**: RCT, n=102, LI 160 vs. maprotiline — comparable efficacy, better tolerability for SJW
- **Shelton et al. (2001)** [JAMA]: n=200, LI 160 vs. placebo for major depression (more severe than mild-moderate) — no significant difference; subsequently used to argue SJW does not work for major depression
- **Hypericum Depression Trial Study Group (2002)** [JAMA]: n=340, hypericum extract vs. sertraline vs. placebo for major depression — hypericum non-superior to placebo; sertraline also non-significant vs. placebo in this trial (suggesting inadequate sensitivity)

The JAMA trials targeted **major depression** (more severe) — the Cochrane review explicitly identifies the strongest evidence base as **mild-moderate** depression, where SJW's efficacy is well-established.

### Mechanism-Pharmacology Translation

Madabushi et al. (2006) [^madabushi-2006-hyperforin-pxr] — clinical pharmacokinetic study demonstrating:
- SJW intake for 14 days reduces midazolam (CYP3A4 probe) AUC by 52%
- Hyperforin content of preparation correlates with magnitude of CYP3A4 induction
- Washout of induction effect: 14–21 days after discontinuation

## Connections

- **Modulates** → [Nervous System](../../../../../01-human/07-system/nervous-system/README.md): Hyperforin's activation of TRPC6 cation channels raises presynaptic Na+ concentration, simultaneously inhibiting reuptake of serotonin, dopamine, norepinephrine, GABA, and glutamate. This broad multi-transmitter inhibition is mechanistically unique, distinct from the selective transporter blockade characteristic of SSRIs or SNRIs, and explains the drug's efficacy across multiple depression subtypes.

- **Modulates** → [Dopamine](../../../../../01-human/03-molecular/dopamine/README.md): Hyperforin-mediated TRPC6 activation inhibits the dopamine transporter (DAT) by raising presynaptic Na+ concentration, increasing dopaminergic tone in mesolimbic and mesocortical circuits. Hypericin weakly inhibits MAO-A and MAO-B, reducing dopamine catabolism. Their relative contribution to the antidepressant effect remains unresolved.

- **Modulates** → [Serotonin](../../../../../01-human/03-molecular/serotonin/README.md): Hyperforin inhibits the serotonin transporter (SERT) via TRPC6-mediated presynaptic depolarisation; hypericin MAO-A inhibition further amplifies serotonergic tone. Clinically significant serotonin syndrome risk exists when combined with SSRIs, SNRIs, tramadol, or linezolid — FDA warns against combination use without supervision.

- **Modulates** → [Brain](../../../../../01-human/06-organ/brain/README.md): Cochrane meta-analysis (29 RCTs, n>5,000) confirms SJW is comparably efficacious to TCAs and SSRIs for mild-moderate depression with superior tolerability. Hyperforin-driven PXR activation induces CYP3A4, substantially reducing plasma levels of co-administered drugs metabolised hepatically — a clinically dominant interaction with transplant, HIV, and contraceptive medications.

---

[^linde-2008-cochrane-sjw]: Linde K, Berner MM, Kriston L. St John's wort for major depression. Cochrane Database Syst Rev. 2008;(4):CD000448. doi:10.1002/14651858.CD000448.pub3
[^madabushi-2006-hyperforin-pxr]: Madabushi R, et al. Eur J Clin Pharmacol. 2006;62(3):225-33. doi:10.1007/s00228-006-0096-z
