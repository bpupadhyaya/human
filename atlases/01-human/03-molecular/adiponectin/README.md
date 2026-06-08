---
schema: human-scale-entry/v1
id: adiponectin
name: Adiponectin
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-07
summary: "Adiponectin is an adipokine paradoxically reduced in obesity; AdipoR1/AdipoR2 → AMPK and PPARα → insulin sensitization and fatty acid oxidation; low adiponectin drives NASH, T2D, and CVD; pioglitazone restores adiponectin and reduces NASH fibrosis."
aliases: ["adiponectin", "ADIPOQ", "Acrp30", "AdipoQ", "GBP-28", "adipokine", "adiponectin receptor", "AdipoR1", "AdipoR2"]
cross_links:
  - target: 01-human/07-system/nash
    relation: connects-to
    note: "Adiponectin deficiency impairs hepatic AMPK → reduced fatty acid oxidation → steatosis; adiponectin suppresses TNF-α and NF-κB in Kupffer cells → reduced hepatic inflammation; pioglitazone (PPARγ agonist) raises adiponectin, reduces NASH steatohepatitis, and slows fibrosis."
  - target: 01-human/07-system/type-2-diabetes
    relation: connects-to
    note: "Low adiponectin predicts T2D onset and correlates with insulin resistance; AdipoR1/AdipoR2 → AMPK → GLUT4 translocation in muscle; adiponectin suppresses hepatic gluconeogenesis via AMPK; pioglitazone raises adiponectin and improves insulin sensitivity."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "Adiponectin binds AdipoR1 and AdipoR2 → APPL1 scaffold protein → AMPK activation; AMPK → ACC phosphorylation → reduced fatty acid synthesis → increased fatty acid oxidation; this pathway mediates adiponectin's insulin-sensitizing and anti-steatotic effects."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "Low adiponectin predicts incident CAD, stroke, and heart failure; high adiponectin suppresses macrophage foam cell formation and eNOS uncoupling; obesity-induced adiponectin deficiency contributes to cardiovascular risk via impaired endothelial function and vascular inflammation."
sources:
  - id: kadowaki-2005-adiponectin-review
    type: peer-reviewed
    cite: "Kadowaki T, Yamauchi T. Adiponectin and adiponectin receptors. Endocr Rev. 2005;26(3):439-451."
    doi: "10.1210/er.2005-0005"
    pmid: "15897297"
    url: "https://doi.org/10.1210/er.2005-0005"
  - id: scherer-1995-adiponectin-discovery
    type: peer-reviewed
    cite: "Scherer PE, Williams S, Fogliano M, Baldini G, Lodish HF. A novel serum protein similar to C1q, produced exclusively in adipocytes. J Biol Chem. 1995;270(45):26746-26749."
    doi: "10.1074/jbc.270.45.26746"
    pmid: "7592907"
    url: "https://doi.org/10.1074/jbc.270.45.26746"
---

# Adiponectin

## Overview

**Adiponectin** (gene *ADIPOQ*, chromosome 3q27.3; also ACRP30, AdipoQ, GBP-28) is the most abundantly expressed adipokine, constituting ~0.01% of total plasma protein (~3–30 µg/mL in healthy humans). Despite being produced exclusively by **white adipose tissue** (primarily mature adipocytes), circulating adiponectin is paradoxically **inversely correlated with adiposity** — levels fall dramatically in obesity, T2DM, metabolic syndrome, and cardiovascular disease. This paradox reflects adipocyte dysfunction in pathological adipose expansion: hypoxia, inflammatory cytokines (TNF-α, IL-6), and ER stress suppress adiponectin gene expression and protein multimerization in obese adipocytes.

Scherer et al. (1995) first described adiponectin as a complement C1q-like protein secreted exclusively by adipocytes [^scherer-1995-adiponectin-discovery]. Kadowaki and Yamauchi (2005) identified AdipoR1 and AdipoR2 as the functional receptors and established adiponectin as a key mediator of AMPK and PPARα activation, linking adipose tissue to systemic insulin sensitivity and fatty acid metabolism [^kadowaki-2005-adiponectin-review].

**Adiponectin levels in disease:**

| Condition | Adiponectin level | Clinical significance |
|---|---|---|
| Healthy lean | 5–30 µg/mL | Baseline cardiometabolic protection |
| Obesity | 1–5 µg/mL | Insulin resistance, metabolic syndrome |
| Type 2 diabetes | ↓↓ (<5 µg/mL) | Predicts T2DM onset; TZD treatment restores |
| NASH | ↓↓ | Impaired hepatic AMPK → steatohepatitis |
| ESRD/dialysis | ↑↑ (paradoxical) | Cachexia-driven; high levels inversely predict survival in CKD |
| Centenarians | ↑ (>15 µg/mL) | Genetic variants (ADIPOQ SNPs) linked to longevity |

## Structure

Adiponectin is a 244 amino acid (mature protein) glycoprotein with a collagen-like domain (aa 18–107) and a globular C1q-like domain (aa 108–244):

**Collagen domain:**
- Contains 15 Gly-X-Y repeats (X = proline, Y = hydroxyproline); these form a collagen triple-helix structure
- Enables trimerization → hexamerization → high-molecular-weight (HMW) 12-18-mer assembly via interchain disulfide bonds (Cys39) and hydrophobic interactions
- Post-translational modifications: hydroxylation of Pro (by P4H) and Lys residues (by LH); O-linked glycosylation at Lys68, Lys71, Lys80, Lys97 — critical for HMW multimerization and receptor binding

**Globular domain:**
- β-sandwich TNF/C1q homology fold; 10 antiparallel β-strands
- Receptor interaction surface: electrostatic and hydrophobic contacts with AdipoR1/AdipoR2 extracellular loops
- **Globular adiponectin (gAd):** Proteolytic cleavage product retaining the globular domain; highly potent AMPK activator at lower concentrations than full-length; circulates at low levels (~0.1% of total)

**Multimeric forms and bioactivity:**
- **LMW trimer:** Lowest activity; predominant form in some assays
- **MMW hexamer:** Intermediate activity
- **HMW (≥12-mer):** Most bioactive form; strongest predictor of insulin sensitivity and cardiovascular risk; measured by ratio HMW/total adiponectin (HMW/total > 0.4 is protective)
- HMW assembly requires Cys39 disulfide bonds and ER-resident DsbA-L (disulfide bond A-like) — deficient in obesity → impaired HMW formation

## Function

**Metabolic actions:**

*Liver (AdipoR2 → PPARα):*
- AdipoR2 activation → PPARα → β-oxidation gene transcription (CPT1α, ACOX1, HADHA) → increased fatty acid oxidation → reduced hepatic triglyceride accumulation
- Adiponectin suppresses hepatic SREBP-1c → reduced de novo lipogenesis → decreased VLDL secretion
- Adiponectin activates hepatic AMPK → phosphorylates ACC2 → malonyl-CoA ↓ → CPT1 disinhibition → fatty acid import into mitochondria
- Net: adiponectin is the major adipokine suppressing hepatic steatosis and gluconeogenesis

*Skeletal muscle (AdipoR1 → AMPK):*
- AdipoR1 has highest affinity for globular adiponectin; widespread muscle expression
- APPL1 (adaptor protein-containing PH domain) bridges AdipoR1 → CaMKKβ → AMPK activation
- AMPK → GLUT4 translocation to plasma membrane (via Akt/AS160 pathway) → increased glucose uptake
- AMPK → PGC-1α → mitochondrial biogenesis → improved oxidative capacity

*Adipose tissue (autocrine):*
- Adiponectin promotes its own secretion and multimerization — a positive autocrine loop disrupted in obese adipocytes

**Anti-inflammatory actions:**
- Suppresses NF-κB activation in macrophages and endothelial cells via AMPK → IKK inhibition
- Inhibits TNF-α secretion from macrophages (switching M1 → M2 polarization)
- Reduces VCAM-1 and ICAM-1 expression on endothelium → less monocyte adhesion
- Inhibits macrophage foam cell formation by reducing SR-A expression and increasing ABCA1-mediated cholesterol efflux

**Regulation of adiponectin secretion:**
- Inducers: caloric restriction, exercise, TZDs (PPARγ agonists), omega-3 fatty acids, AMPK activators (metformin)
- Suppressors: TNF-α, IL-6, glucocorticoids, insulin (paradoxically), hypoxia, endoplasmic reticulum stress

## Mechanism

**AdipoR signaling in detail:**

1. Adiponectin (LMW, HMW, or gAd) → extracellular AdipoR1/AdipoR2 N-terminal domain binding
2. AdipoR1 (7-transmembrane, unique topology — N-terminus intracellular) → APPL1 recruitment → CaMKKβ activation → AMPK-α1/α2 phosphorylation (Thr172)
3. AdipoR2 → similar pathway but also directly couples to PPARα activation via unknown intermediaries; AdipoR2 may have intrinsic ceramidase activity → reduces ceramide → activates AMPK
4. **Ceramide reduction:** A novel mechanism — AdipoR1/R2 have intrinsic ceramidase activity → converts ceramide (pro-apoptotic, lipotoxic) → sphingosine → S1P (pro-survival); in NASH, high ceramide promotes hepatocyte lipoapoptosis, and adiponectin counteracts this
5. AMPK → multiple downstream effects: phospho-ACC2 → ↓malonyl-CoA → CPT1 active → fatty acid oxidation; phospho-HMGCR → ↓cholesterol synthesis; phospho-TSC2 → mTORC1 inhibition → autophagy; phospho-FOXO1 → ↓gluconeogenesis

**Pioglitazone and adiponectin:**
- TZDs (thiazolidinediones) are PPARγ agonists that directly transactivate the ADIPOQ promoter → 50–100% increase in total adiponectin, particularly HMW fraction
- Pioglitazone is the only drug proven to histologically improve NASH (NAS score, fibrosis) in randomized trials; the adiponectin-raising effect contributes significantly to its hepatoprotection
- TZDs also reduce ceramide and increase AdipoR expression — further amplifying adiponectin signaling

**AdipoRon (AdipoR agonist):**
- Small molecule AdipoR1/R2 agonist; improves insulin sensitivity, reduces hepatic steatosis, and extends lifespan in ob/ob mice; in early clinical development as an adiponectin mimetic

## Connections

Adiponectin deficiency impairs hepatic AMPK → reduced fatty acid oxidation → steatosis; adiponectin suppresses TNF-α and NF-κB in Kupffer cells → reduced hepatic inflammation; pioglitazone (PPARγ agonist) raises adiponectin, reduces NASH steatohepatitis, and slows fibrosis.

Low adiponectin predicts T2D onset and correlates with insulin resistance; AdipoR1/AdipoR2 → AMPK → GLUT4 translocation in muscle; adiponectin suppresses hepatic gluconeogenesis via AMPK; pioglitazone raises adiponectin and improves insulin sensitivity.

Adiponectin binds AdipoR1 and AdipoR2 → APPL1 scaffold protein → AMPK activation; AMPK → ACC phosphorylation → reduced fatty acid synthesis → increased fatty acid oxidation; this pathway mediates adiponectin's insulin-sensitizing and anti-steatotic effects.

Low adiponectin predicts incident CAD, stroke, and heart failure; high adiponectin suppresses macrophage foam cell formation and eNOS uncoupling; obesity-induced adiponectin deficiency contributes to cardiovascular risk via impaired endothelial function and vascular inflammation.

[^kadowaki-2005-adiponectin-review]: Kadowaki T, Yamauchi T. Adiponectin and adiponectin receptors. *Endocr Rev.* 2005;26(3):439-451. [doi:10.1210/er.2005-0005](https://doi.org/10.1210/er.2005-0005) · [PubMed 15897297](https://pubmed.ncbi.nlm.nih.gov/15897297/)
[^scherer-1995-adiponectin-discovery]: Scherer PE, Williams S, Fogliano M, Baldini G, Lodish HF. A novel serum protein similar to C1q, produced exclusively in adipocytes. *J Biol Chem.* 1995;270(45):26746-26749. [doi:10.1074/jbc.270.45.26746](https://doi.org/10.1074/jbc.270.45.26746) · [PubMed 7592907](https://pubmed.ncbi.nlm.nih.gov/7592907/)
