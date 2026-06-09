---
schema: human-scale-entry/v1
id: glp-1
name: GLP-1
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-07
summary: "GLP-1 is an incretin produced by intestinal L-cells; binds GLP-1R → cAMP → glucose-dependent insulin secretion and β-cell proliferation; GLP-1R agonists (semaglutide, liraglutide) are first-line therapy for type 2 diabetes and obesity with proven cardiovascular benefit."
aliases: ["GLP-1", "glucagon-like peptide 1", "GLP1", "incretin", "GLP-1 receptor agonist", "semaglutide target", "liraglutide target", "GLP-1R agonist", "tirzepatide GLP1", "Ozempic mechanism"]
cross_links:
  - target: 01-human/07-system/type-2-diabetes
    relation: connects-to
    note: "GLP-1R agonists (semaglutide, liraglutide, dulaglutide) reduce HbA1c 1-1.5% and weight 5-15%; glucose-dependent insulin secretion avoids hypoglycemia; SUSTAIN-6 (semaglutide) and LEADER (liraglutide) showed CV risk reduction in T2D with established cardiovascular disease."
  - target: 01-human/07-system/nash
    relation: connects-to
    note: "Semaglutide resolved NASH histology in 59% vs 17% placebo (Phase 2); GLP-1R activation reduces hepatic lipogenesis, liver inflammation, and oxidative stress; semaglutide ESSENCE Phase 3 NASH trial is ongoing; GLP-1R agonists are promising disease-modifying agents for NASH."
  - target: 01-human/03-molecular/glucagon
    relation: connects-to
    note: "GLP-1 and glucagon are both encoded by GCG (proglucagon) and produced via tissue-specific PC2/PC1 cleavage: α-cells make glucagon; L-cells make GLP-1 and GLP-2; GLP-1 suppresses glucagon secretion, opposing glucagon-driven hepatic glucose output."
  - target: 01-human/03-molecular/insulin
    relation: connects-to
    note: "GLP-1 amplifies glucose-stimulated insulin secretion in pancreatic β-cells via GLP-1R/cAMP/PKA pathway; glucose-dependence prevents hypoglycemia at low glucose; GLP-1 promotes β-cell proliferation via PI3K/Akt and inhibits apoptosis, preserving β-cell mass in type 2 diabetes."
  - target: 01-human/07-system/obesity
    relation: connects-to
    note: "GLP-1, secreted by intestinal L-cells post-meal, potentiates insulin release, suppresses glucagon and appetite; GLP-1/GIP receptor agonists (semaglutide ~15%, tirzepatide ~22% weight loss) are the most effective pharmacological obesity treatments available."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "SELECT trial (semaglutide 2.4 mg, obesity without T2DM): 20% MACE reduction vs placebo; SUSTAIN-6 and LEADER established GLP-1R agonists as antidiabetic drugs with proven CV benefit; GLP-1R on cardiomyocytes → anti-inflammatory and vasodilatory cardioprotective effects."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "GLP-1R in hypothalamic ARC/PVN neurons → reduced appetite and food cue reactivity; brainstem area postrema GLP-1R → nausea and gastric emptying delay; GLP-1R in VTA/NAcc reward circuits reduces motivation for high-fat food; semaglutide reduces food reward in human fMRI studies."
  - target: 01-human/07-system/alzheimers-disease
    relation: connects-to
    note: "GLP-1R activation reduces amyloid-β, tau phosphorylation, and neuroinflammation in preclinical AD models; semaglutide EVOKE Phase 3 trial targets early AD; GLP-1R agonists may address brain insulin resistance via Akt → reduced GSK-3β → less tau hyperphosphorylation."
sources:
  - id: drucker-2006-glp1-biology
    type: peer-reviewed
    cite: "Drucker DJ. The biology of incretin hormones. Cell Metab. 2006;3(3):153-165."
    doi: "10.1016/j.cmet.2006.01.004"
    pmid: "16517403"
    url: "https://doi.org/10.1016/j.cmet.2006.01.004"
  - id: marso-2016-semaglutide-cvd
    type: peer-reviewed
    cite: "Marso SP, Bain SC, Consoli A, et al. Semaglutide and cardiovascular outcomes in patients with type 2 diabetes. N Engl J Med. 2016;375(19):1834-1844."
    doi: "10.1056/NEJMoa1607141"
    pmid: "27633186"
    url: "https://doi.org/10.1056/NEJMoa1607141"
---

# GLP-1

## Overview

**GLP-1** (glucagon-like peptide 1) is a 30 amino acid **incretin hormone** produced by intestinal L-cells and a subset of brainstem neurons. It is encoded by the *GCG* (proglucagon) gene on chromosome 2q24.2, processed from the 160 amino acid proglucagon precursor via differential tissue-specific action of **prohormone convertase 1/3 (PC1/3)** in intestinal L-cells and hypothalamic neurons — yielding GLP-1(7–36)amide and GLP-1(7–37), the two principal active forms. Pancreatic α-cells express **PC2** instead, generating glucagon from the same proglucagon gene.

Drucker (2006) provided the definitive characterization of GLP-1 biology [^drucker-2006-glp1-biology]. GLP-1 is the most therapeutically important gut hormone: GLP-1R agonists have become first-line agents for type 2 diabetes (T2D) and obesity, with semaglutide and tirzepatide (GLP-1R + GIPR dual agonist) achieving unprecedented weight loss (~15–22% of body weight). The SUSTAIN-6 trial of subcutaneous semaglutide [^marso-2016-semaglutide-cvd] and LEADER trial of liraglutide demonstrated significant cardiovascular risk reduction, establishing GLP-1R agonists as the only antidiabetic drugs with proven CV benefit in T2D patients with established cardiovascular disease.

**GLP-1 receptor agonists approved or in late development:**

| Drug | GLP-1R selectivity | Route | Key indication | Weight loss |
|---|---|---|---|---|
| Liraglutide (Victoza/Saxenda) | GLP-1R only | SC daily | T2D, obesity | 6-8% |
| Semaglutide (Ozempic/Wegovy) | GLP-1R only | SC weekly / oral | T2D, obesity, CV | 10-15% |
| Dulaglutide (Trulicity) | GLP-1R only | SC weekly | T2D | 5-8% |
| Tirzepatide (Mounjaro/Zepbound) | GLP-1R + GIPR | SC weekly | T2D, obesity | 15-22% |
| Retatrutide (phase 3) | GLP-1R + GIPR + GCGR | SC weekly | Obesity | ~24% |

## Structure

GLP-1(7–36)amide is the predominant circulating form (C-terminal amidation prolongs half-life slightly). The peptide adopts an **amphipathic α-helix** from residues 11–29 upon GLP-1R binding, with hydrophobic residues packing against a hydrophobic groove in the receptor extracellular domain.

**Key structure-activity relationships:**
- His7 is essential for receptor binding and activation (removal destroys activity)
- Ala8 makes the peptide a DPP-4 substrate (penultimate N-terminal residue; DPP-4 cleaves after Ala8 → GLP-1(9–36) with 1000-fold lower activity)
- Phe12, Ala13, Glu15, Glu17, Lys18 form the helix contact face with GLP-1R
- GLP-1(9–36) acts as a GLP-1R antagonist and may have cardioprotective effects via GLP-1R-independent pathways

**Resistance to degradation (drug design rationale):**
- Native GLP-1 t₁/₂ ~2 min in plasma (DPP-4 + neutral endopeptidase)
- Liraglutide: Ala8→Lys26 fatty acid conjugation → albumin binding → reduced renal clearance (t₁/₂ ~13 h)
- Semaglutide: Ala8→Aib (α-aminoisobutyric acid) substitution + C18 diacid → albumin binding (t₁/₂ ~165 h)
- Oral semaglutide: SNAC absorption enhancer enables 1% intestinal uptake

**GLP-1R structure:** Class B1 GPCR; ECD (extracellular domain) binds the GLP-1 C-terminal helix; TM bundle binds the N-terminal region; signal propagation through G-protein coupling. Cryo-EM structures (2020) reveal the active-state GLP-1R/Gs complex at 3.3 Å — enabling structure-based design of oral non-peptide GLP-1R agonists (Pfizer danuglipron, Eli Lilly orforglipron; Phase 2/3).

## Function

**Pancreatic actions (β-cells):**
- Glucose-dependent insulin secretion: GLP-1R → Gs → adenylyl cyclase → cAMP → PKA and EPAC → KATP channel closure, L-type Ca²⁺ channel opening → insulin exocytosis. The critical feature: this pathway is inactive at fasting glucose levels, explaining the absence of hypoglycemia risk.
- β-cell mass preservation: GLP-1R/PI3K/Akt/PDX-1 → β-cell proliferation and inhibition of apoptosis; GLP-1R agonists increase β-cell mass in rodent models; human evidence is emerging.
- α-cell suppression: GLP-1 directly suppresses glucagon secretion from α-cells, reducing post-meal glucose excursions.

**Extrapancreatic actions:**
- **Satiety and weight loss:** GLP-1R in hypothalamic ARC/PVN neurons → reduced appetite, food intake, and food preference for high-fat food; brainstem area postrema GLP-1R → nausea and gastric emptying delay
- **Cardiovascular protection:** GLP-1R on cardiomyocytes → cAMP → improved cardiac contractility; endothelial GLP-1R → NO production → vasodilation; anti-atherosclerotic effects via monocyte/macrophage suppression
- **Liver:** Hepatocyte GLP-1R expression is low but GLP-1R agonists reduce hepatic de novo lipogenesis (via insulin sensitization and direct AMPK activation), suppress Kupffer cell activation, and reduce liver fat in NASH
- **Kidney:** GLP-1R on proximal tubule → reduced Na⁺/H⁺ exchanger activity → natriuresis → blood pressure reduction; GLP-1R agonists reduce albuminuria and slow eGFR decline in T2D nephropathy

## Mechanism

**GLP-1R signaling cascade:**
1. GLP-1 binds ECD of GLP-1R → conformational change in TM bundle
2. Gs coupling → Gαs dissociation → adenylyl cyclase III/VII activation → cAMP accumulation (~10-fold increase in β-cells)
3. cAMP activates PKA (phosphorylates KATP channel Kir6.2 subunit → reduced open probability) AND EPAC2 (Rap1 → PLC→ IP3 → ER Ca²⁺ release)
4. Voltage-gated Ca²⁺ channels open → [Ca²⁺]ᵢ rise → insulin granule exocytosis
5. β-arrestin recruitment → GLP-1R internalization → receptor recycling (endosomes) or degradation (lysosomes); internalized GLP-1R continues cAMP signaling from endosomes

**Tirzepatide dual agonism:** Tirzepatide (GLP-1R + GIPR) achieves superior weight loss (~22% vs ~15% for semaglutide) by activating GIPR on adipocytes (promoting lipid storage and thermogenesis, paradoxically reducing visceral fat via complex adipokine signaling) while also activating GLP-1R. GIPR activation alone has modest anti-obesity effects; the synergy with GLP-1R is mechanistically distinct from simple additive effects.

## Connections

- `connects-to` → **[Type 2 Diabetes](../../07-system/type-2-diabetes/README.md)** — GLP-1R agonists (semaglutide, liraglutide, dulaglutide) reduce HbA1c 1-1.5% and weight 5-15%; glucose-dependent insulin secretion avoids hypoglycemia; SUSTAIN-6 (semaglutide) and LEADER (liraglutide) showed CV risk reduction in T2D with established cardiovascular disease.
- `connects-to` → **[NASH](../../07-system/nash/README.md)** — semaglutide resolved NASH histology in 59% vs 17% placebo (Phase 2); GLP-1R activation reduces hepatic lipogenesis, liver inflammation, and oxidative stress; semaglutide ESSENCE Phase 3 NASH trial is ongoing; GLP-1R agonists are promising disease-modifying agents for NASH.
- `connects-to` → **[Glucagon](../../03-molecular/glucagon/README.md)** — GLP-1 and glucagon are both encoded by GCG (proglucagon) and produced via tissue-specific PC2/PC1 cleavage: α-cells make glucagon; L-cells make GLP-1 and GLP-2; GLP-1 suppresses glucagon secretion, opposing glucagon-driven hepatic glucose output.
- `connects-to` → **[Insulin](../../03-molecular/insulin/README.md)** — GLP-1 amplifies glucose-stimulated insulin secretion in pancreatic β-cells via GLP-1R/cAMP/PKA pathway; glucose-dependence prevents hypoglycemia at low glucose; GLP-1 promotes β-cell proliferation via PI3K/Akt and inhibits apoptosis, preserving β-cell mass in type 2 diabetes.
- `connects-to` → **[Obesity](../../07-system/obesity/README.md)** — GLP-1, secreted by intestinal L-cells post-meal, potentiates insulin release, suppresses glucagon and appetite via hypothalamic GLP-1R; GLP-1/GIP receptor agonists (semaglutide ~15%, tirzepatide ~22% weight loss) are the most effective pharmacological obesity treatments currently available.
- `connects-to` → **[Cardiovascular System](../../07-system/cardiovascular-system/README.md)** — SELECT trial (semaglutide 2.4 mg, obesity without T2DM): 20% MACE reduction vs placebo; SUSTAIN-6 and LEADER established GLP-1R agonists as antidiabetic drugs with proven CV benefit; GLP-1R on cardiomyocytes → anti-inflammatory and vasodilatory cardioprotective effects.
- `connects-to` → **[Brain](../../06-organ/brain/README.md)** — GLP-1R in hypothalamic ARC/PVN neurons → reduced appetite and food cue reactivity; brainstem area postrema GLP-1R → nausea and gastric emptying delay; GLP-1R in VTA/NAcc reward circuits reduces motivation for high-fat food; semaglutide reduces food reward in human fMRI studies.
- `connects-to` → **[Alzheimer's Disease](../../07-system/alzheimers-disease/README.md)** — GLP-1R activation reduces amyloid-β, tau phosphorylation, and neuroinflammation in preclinical AD models; semaglutide EVOKE Phase 3 trial targets early AD; GLP-1R agonists may address brain insulin resistance via Akt → reduced GSK-3β → less tau hyperphosphorylation.

[^drucker-2006-glp1-biology]: Drucker DJ. The biology of incretin hormones. *Cell Metab.* 2006;3(3):153-165. [doi:10.1016/j.cmet.2006.01.004](https://doi.org/10.1016/j.cmet.2006.01.004) · [PubMed 16517403](https://pubmed.ncbi.nlm.nih.gov/16517403/)
[^marso-2016-semaglutide-cvd]: Marso SP, Bain SC, Consoli A, et al. Semaglutide and cardiovascular outcomes in patients with type 2 diabetes. *N Engl J Med.* 2016;375(19):1834-1844. [doi:10.1056/NEJMoa1607141](https://doi.org/10.1056/NEJMoa1607141) · [PubMed 27633186](https://pubmed.ncbi.nlm.nih.gov/27633186/)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
