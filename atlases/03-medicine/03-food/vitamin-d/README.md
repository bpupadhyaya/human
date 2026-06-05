---
schema: medicine-entry/v1
id: vitamin-d
name: Vitamin D (Calciferol)
atlas: 03-medicine
scale: 03-food
status: draft
last_reviewed: 2026-06-05
summary: "Fat-soluble secosteroid hormone; UV-B-synthesized or dietary; activated in liver then kidney to calcitriol; VDR nuclear receptor regulates >1,000 genes governing calcium homeostasis, bone integrity, and immune modulation."
aliases: ["vitamin D", "calciferol", "cholecalciferol (D3)", "ergocalciferol (D2)", "calcitriol (active form)", "1,25-dihydroxyvitamin D3", "calcidiol (25(OH)D)", "25-hydroxyvitamin D", "vitamin D deficiency", "VDR ligand"]
sources:
  - id: holick-2007-vitamin-d-nejm
    type: peer-reviewed
    cite: "Holick MF. Vitamin D deficiency. N Engl J Med. 2007;357(3):266-81."
    doi: "10.1056/NEJMra070553"
    pmid: "17634462"
    url: "https://doi.org/10.1056/NEJMra070553"
  - id: autier-2014-vitamin-d-bmj
    type: peer-reviewed
    cite: "Autier P, Mullie P, Macacu A, et al. Effect of vitamin D supplementation on non-skeletal disorders: a systematic review of meta-analyses and randomised trials. Lancet Diabetes Endocrinol. 2017;5(12):986-1004."
    doi: "10.1016/S2213-8587(17)30357-1"
    pmid: "29102597"
    url: "https://doi.org/10.1016/S2213-8587(17)30357-1"
  - id: vital-trial-2019
    type: peer-reviewed
    cite: "Manson JE, Cook NR, Lee IM, et al. Vitamin D Supplements and Prevention of Cancer and Cardiovascular Disease. N Engl J Med. 2019;380(1):33-44."
    doi: "10.1056/NEJMoa1809944"
    pmid: "30415629"
    url: "https://doi.org/10.1056/NEJMoa1809944"
  - id: stryer-biochemistry
    type: textbook
    cite: "Berg JM, Tymoczko JL, Stryer L. Biochemistry. 9th ed. W.H. Freeman; 2019."
    url: "https://www.macmillanlearning.com/college/us/product/Biochemistry/p/131911467X"
    accessed: "2026-06-05"
cross_links:
  - target: 01-human/07-system/musculoskeletal-system
    relation: modulates
    note: "Calcitriol upregulates intestinal TRPV6 and calbindin-D9k for calcium absorption and renal TRPV5 for reabsorption; also stimulates RANKL on osteoblasts promoting osteoclastogenesis essential for bone remodeling."
  - target: 01-human/07-system/immune-system
    relation: modulates
    note: "VDR activation in macrophages and dendritic cells induces cathelicidin and β-defensin 2 for innate immunity; in lymphocytes promotes regulatory T-cell differentiation, suppressing Th1/Th17 autoimmune responses."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: modulates
    note: "Calcitriol drives naïve CD4+ T-cell differentiation toward Foxp3+ regulatory T cells by upregulating IL-2 and CTLA-4; this Treg induction reduces autoreactive T-cell activity in MS, T1D, and IBD models."
  - target: 01-human/06-organ/kidney
    relation: modulates
    note: "Renal CYP27B1 converts 25(OH)D to active calcitriol under PTH stimulation; CYP24A1 catalyzes inactivation forming 24,25(OH)₂D; FGF-23 from bone suppresses CYP27B1 and stimulates CYP24A1 to limit calcitriol."
---

# Vitamin D (Calciferol)

## Overview

**Vitamin D** is a fat-soluble **secosteroid** — structurally related to steroid hormones, differing by a broken B-ring in the four-ring steroid backbone (hence *seco*-). Unlike true vitamins (which cannot be synthesised endogenously), vitamin D is more accurately described as a **prohormone**: it is synthesised in the skin from a cholesterol derivative under UV-B irradiation and converted through two successive hydroxylation steps into a potent nuclear receptor ligand with broad hormonal actions.

**Two primary forms:**
- **Vitamin D₃ (cholecalciferol):** The mammalian form, synthesised endogenously; also found in animal dietary sources; more potent than D₂ at raising serum 25(OH)D levels
- **Vitamin D₂ (ergocalciferol):** Produced by UV-irradiation of ergosterol in fungi and plants; bioavailable but approximately half as effective as D₃ at raising 25(OH)D in most studies; used in some fortified foods and supplements

**UV-B skin synthesis pathway:**
1. **7-Dehydrocholesterol** (provitamin D₃) in keratinocytes and fibroblasts of the epidermis/dermis absorbs UV-B photons (290–315 nm)
2. **Photolysis** → pre-vitamin D₃ (via electrocyclic ring opening of the B-ring)
3. Thermal isomerisation → **cholecalciferol (vitamin D₃)**; excess UV-B converts pre-vitamin D₃ to tachysterol and lumisterol (inactive photoproducts) — a built-in photoregulatory mechanism preventing vitamin D toxicity from sun exposure
4. Cholecalciferol released into circulation bound to **vitamin D-binding protein (DBP, GC globulin)**

**Dietary sources:**
| Source | Vitamin D content |
|:---|:---|
| Salmon (wild-caught, 3 oz) | 600–1000 IU D₃ |
| Canned tuna | 150–200 IU D₃ |
| Cod liver oil (1 tsp) | ~400 IU D₃ |
| Egg yolk | 40–60 IU D₃ |
| UV-irradiated mushrooms (3 oz) | 400–1000 IU D₂ (variable) |
| Fortified milk (8 oz) | 100–120 IU D₃ |
| Fortified orange juice | 100 IU D₃ |
| Fortified cereals | 40–120 IU D₃ per serving |

**Serum 25(OH)D — the clinical measure:**
- 25(OH)D (calcidiol) is the accepted serum biomarker of vitamin D status due to its long half-life (2–3 weeks) and reflecting both endogenous synthesis and dietary/supplemental intake
- **Deficiency:** <20 ng/mL (50 nmol/L) — Endocrine Society, NIH Office of Dietary Supplements
- **Insufficiency:** 20–29 ng/mL (50–75 nmol/L)
- **Sufficiency:** 30–60 ng/mL (75–150 nmol/L)
- **Toxicity threshold:** Generally >150 ng/mL (375 nmol/L) — hypercalcaemia risk [^holick-2007-vitamin-d-nejm]

**Global deficiency burden:** Vitamin D deficiency affects an estimated 1 billion people worldwide; risk factors include high latitude, limited sun exposure (indoor lifestyle, cultural dress), dark skin (melanin reduces UV-B penetration — requires 3–5× more sun exposure vs. pale skin to synthesise equivalent D₃), ageing (reduced 7-DHC in skin, reduced renal 1α-hydroxylase activity), obesity (fat-soluble D₃ sequestered in adipose tissue), malabsorption (Crohn's disease, coeliac), and chronic kidney disease.

## Mechanism

### Metabolic Activation — Two-Step Hydroxylation

**Step 1: Hepatic 25-hydroxylation**
- **Enzyme:** CYP2R1 (primarily; also CYP27A1 as minor contributor) — mitochondrial/microsomal cytochrome P450 in hepatocytes
- **Reaction:** Vitamin D₃ → **25(OH)D₃ (calcidiol)**; 25-position hydroxylation
- **Regulation:** Largely constitutive; not tightly regulated; 25(OH)D level primarily reflects substrate availability (sun exposure + dietary intake)
- **DBP transport:** 25(OH)D circulates tightly bound to DBP (>99% bound); only free fraction is biologically active and filtered at the glomerulus

**Step 2: Renal 1α-hydroxylation**
- **Enzyme:** CYP27B1 (1α-hydroxylase) — expressed primarily in renal proximal tubular cells; also in immune cells (macrophages, dendritic cells), skin, placenta, parathyroid, and other extrarenal tissues
- **Reaction:** 25(OH)D₃ → **1,25(OH)₂D₃ (calcitriol)** — the biologically active hormone
- **Tight regulation (renal CYP27B1):**
  - ↑ Stimulated by: PTH (primary upregulator — ↑ via cAMP-PKA; Gs-coupled PTH1R → ↑CYP27B1 transcription), low serum phosphate, low serum calcium, prolactin, IGF-1
  - ↓ Inhibited by: FGF-23 (from osteocytes → activates FGFR1-Klotho → ↑CYP24A1 + ↓CYP27B1 → ↓calcitriol), high calcitriol itself (negative feedback), high serum calcium, high phosphate

**Inactivation — CYP24A1:**
- CYP24A1 (24-hydroxylase) is the primary catabolic enzyme for calcitriol and calcidiol
- Converts 1,25(OH)₂D₃ → 1,24,25(OH)₃D₃ → calcitroic acid (water-soluble; excreted in bile)
- CYP24A1 is a direct Nrf-2-independent but VDR-direct target gene — calcitriol upregulates its own degradation (autoregulatory feedback)
- FGF-23 also strongly induces CYP24A1 — the key phosphate homeostasis hormonal axis

### VDR Nuclear Receptor — Genomic Actions

**Calcitriol (1,25(OH)₂D₃) acts via VDR (Vitamin D Receptor; NR1I1):**
- **VDR** is a member of the nuclear receptor superfamily — ligand-activated transcription factor
- Expressed in virtually all nucleated cell types; particularly high expression in intestine, kidney, bone, parathyroid, immune cells, skin, pancreatic β-cells, neurons
- **Mechanism:**
  1. Calcitriol diffuses into cells, binds VDR with high affinity (Kd ~0.1 nM)
  2. VDR heterodimerises with **RXR** (retinoid X receptor; activated by 9-cis retinoic acid)
  3. VDR/RXR heterodimer binds **vitamin D response elements (VDREs)** — DR3-type (direct repeat with 3-nucleotide spacer: AGGTCAnnnAGGTCA) in promoters/enhancers
  4. Recruits co-activators (SRC-1/NCoA-1, DRIP/Mediator complex) → chromatin remodelling → transcriptional activation or (with co-repressors NCOR, SMRT) repression
  5. Regulates expression of **>1,000 genes** across diverse tissue types — VDR ChIP-seq (genome-wide) studies have identified extensive calcitriol-responsive enhancer regions

**Non-genomic VDR actions:**
- Membrane-associated VDR (or PDIA3 — protein disulfide isomerase A3, an alternative rapid-response receptor) mediates rapid (seconds–minutes) signalling: ↑intracellular Ca²⁺ (via PLC → IP₃), ↑PKC activation, ↑MAPK → rapid regulation of ion channels and hormone secretion (e.g., rapid insulin secretion from pancreatic β-cells)

### Calcium and Phosphate Homeostasis (Musculoskeletal)

Calcitriol's classical physiological role — the hormonal axis maintaining serum Ca²⁺ and phosphate homeostasis:

**Intestinal calcium absorption:**
- VDR → ↑**TRPV6** (transient receptor potential vanilloid 6) — apical Ca²⁺ entry channel in duodenal enterocytes
- VDR → ↑**Calbindin-D9k** (CALB3) — intracellular Ca²⁺ buffer facilitating transcellular Ca²⁺ diffusion
- VDR → ↑**PMCA1b** (plasma membrane Ca²⁺-ATPase) — basolateral Ca²⁺ extrusion
- Net: active transcellular Ca²⁺ absorption in duodenum/jejunum; calcitriol increases fractional Ca²⁺ absorption from ~10–15% to ~30–40%

**Renal calcium reabsorption:**
- VDR → ↑**TRPV5** (apical Ca²⁺ channel) in distal convoluted tubule → ↑Ca²⁺ reabsorption
- ↑Calbindin-D28k (CALB1) → intracellular Ca²⁺ buffering in renal tubular cells

**Bone:**
- VDR → ↑**RANKL** on osteoblasts → binds RANK on osteoclast precursors → osteoclastogenesis → bone resorption → Ca²⁺/phosphate release
- At adequate vitamin D status, this osteoclast-mediated bone remodelling is balanced; deficiency leads to rickets/osteomalacia (undermineralised osteoid)
- VDR also required for osteoblast differentiation and mineralisation capacity (↑osteocalcin, ↑osteopontin — bone matrix proteins)

**PTH regulation:**
- VDR → ↓PTH gene transcription (parathyroid gland VDR — calcitriol suppresses PTH synthesis and parathyroid cell proliferation)
- Secondary hyperparathyroidism in vitamin D deficiency drives elevated PTH → ↑bone resorption → ↑fracture risk

### Immune Modulation

VDR is expressed in virtually all immune cells:

**Innate immunity:**
- Macrophages and DCs express CYP27B1 — they can locally produce calcitriol from 25(OH)D, creating autocrine/paracrine immune regulation
- VDR → ↑**Cathelicidin** (CAMP/LL-37) — broad-spectrum antimicrobial peptide disrupting bacterial/viral membranes; critical in tuberculosis defence (VDR-cathelicidin pathway explains why vitamin D deficiency is a TB risk factor)
- VDR → ↑**β-Defensin 2** (DEFB4A) — epithelial antimicrobial peptide [^holick-2007-vitamin-d-nejm]

**Adaptive immunity — immunosuppressive axis:**
- ↓Th1 differentiation: ↓IL-12 production by DCs → ↓IFN-γ by T-cells → ↓Th1 autoimmune response
- ↓Th17 differentiation: ↓IL-17A, ↓IL-23 → ↓Th17-mediated autoimmunity (MS, psoriasis, IBD)
- ↑Treg induction: VDR in CD4+ T-cells promotes Foxp3+ Treg differentiation → ↑IL-10, ↑TGF-β → immune tolerance
- ↓B-cell proliferation and ↓immunoglobulin secretion (relevant in autoantibody-mediated diseases)
- Net: calcitriol is immunoregulatory — enhancing innate antimicrobial immunity while suppressing excessive adaptive autoimmune responses

## Clinical Use

### Established Indications (Skeletal)

**Prevention and treatment of deficiency:** The primary, unambiguous indication.

| Clinical setting | Recommendation |
|:---|:---|
| Deficiency treatment (25(OH)D <20 ng/mL) | 50,000 IU vitamin D₂/D₃ weekly × 8–12 weeks, then maintenance |
| Insufficiency (20–30 ng/mL) | 1,000–2,000 IU D₃ daily |
| Maintenance in general population | 600 IU/day (adults <70); 800 IU/day (≥70) — RDA (US) |
| Osteoporosis prevention/treatment | 800–1,000 IU D₃ daily + calcium (evidence: fracture reduction) |
| Chronic kidney disease (CKD) | Calcitriol (active form) or analogue (paricalcitol, alfacalcidol) — bypasses impaired renal hydroxylation |
| Nutritional rickets prevention | 400 IU D₃ from birth; WHO recommendation |
| Hypoparathyroidism | Calcitriol (bypasses PTH-regulated activation) |

**Rickets and osteomalacia:** Historically the defining deficiency diseases; near-eliminated in developed countries by food fortification but resurging in nutritionally at-risk populations.

### At-Risk Populations for Deficiency

- **Exclusively breastfed infants:** Breast milk is low in vitamin D (<25 IU/L) — supplementation 400 IU/day recommended from birth (AAP)
- **Elderly:** Reduced skin synthesis capacity (~4× less D₃ synthesised from same UV-B exposure at age 70 vs. age 20); reduced renal 1α-hydroxylase activity; reduced outdoor activity; institutionalised elderly especially at risk
- **Dark-skinned individuals at high latitude:** Melanin absorbs UV-B → 3–5× more sun exposure required; risk increased in winter at latitudes >35°
- **Obese individuals:** Vitamin D₃ (fat-soluble) sequestered in adipose tissue → lower serum 25(OH)D per unit synthesised; obesity is an independent risk factor for deficiency
- **Malabsorption syndromes:** Crohn's disease, coeliac disease, gastric bypass surgery — reduced fat-soluble vitamin absorption
- **CKD:** Impaired renal CYP27B1 → reduced calcitriol synthesis despite normal or elevated 25(OH)D

### Non-Skeletal Uses Under Investigation

- **Cancer:** Large meta-analyses suggest inverse association between 25(OH)D levels and colorectal, breast, prostate cancer risk; mechanism via VDR anti-proliferative, pro-differentiation, and pro-apoptotic effects
- **Multiple sclerosis:** Strong epidemiological association (latitude gradient, deficiency as MS risk factor); VDR immunosuppression → ↓Th1/Th17 activity; supplementation trials show immunological effects but modest/unclear clinical impact
- **Type 1 diabetes prevention:** VDR-mediated Treg induction → ↓pancreatic β-cell autoimmunity; observational evidence; no definitive prevention RCT
- **Cardiovascular disease:** VDR expressed in cardiomyocytes and vascular smooth muscle; deficiency associated with ↑hypertension, ↑LVH, ↑heart failure risk; large RCTs negative for cardiovascular endpoints
- **Respiratory infections (including COVID-19):** Cathelicidin/defensin induction; some meta-analyses show modest reduction in acute respiratory tract infections with vitamin D supplementation

### Drug Interactions

- **Glucocorticoids:** ↓CYP27B1 activity → ↓calcitriol; ↓intestinal VDR expression → ↓Ca²⁺ absorption; accelerates bone loss; vitamin D supplementation essential in long-term steroid users
- **Antiepileptics (phenytoin, carbamazepine, phenobarbital):** CYP3A4/CYP2R1 induction → accelerated vitamin D catabolism → ↓25(OH)D; supplementation needed
- **Rifampicin:** CYP induction → accelerated D₃ and 25(OH)D metabolism → deficiency risk in TB treatment
- **Thiazide diuretics:** Reduce renal Ca²⁺ excretion; combined with high-dose vitamin D → hypercalcaemia risk; monitor Ca²⁺
- **Cholestyramine, orlistat:** Reduce fat-soluble vitamin absorption including vitamin D
- **Magnesium:** Magnesium is a cofactor for CYP2R1 and CYP27B1 — severe magnesium deficiency can impair vitamin D activation; magnesium deficiency may blunt response to vitamin D supplementation

### Toxicity

- **Vitamin D toxicity** is almost exclusively from excessive supplementation (not sun exposure, due to photoregulatory conversion of pre-vitamin D₃ to inactive photoproducts)
- **Hypervitaminosis D:** 25(OH)D >150 ng/mL; features: hypercalcaemia (nausea, vomiting, polyuria, polydipsia, confusion, weakness), hypercalciuria → nephrolithiasis; metastatic calcification (vascular, renal) in severe/prolonged cases
- Risk begins with prolonged intake >10,000 IU/day in most adults; Tolerable Upper Intake Level (UL): 4,000 IU/day (US), 100 µg/day (EU) — conservative
- **CYP24A1 inactivating mutations (Williams syndrome):** Rare genetic cause of vitamin D hypersensitivity

## Evidence

### Skeletal Outcomes

**Fracture prevention:** Multiple meta-analyses:
- Vitamin D + calcium (vs. calcium alone or placebo): consistent reduction in hip fracture risk, particularly in institutionalised elderly
- DIPART meta-analysis (2010): pooled individual participant data, n=68,500 — vitamin D₃ + calcium reduced hip fractures by 16% (HR 0.84; 95% CI 0.74–0.96)
- Vitamin D alone (without calcium): less consistent benefit in fracture prevention
- GRADE: **Moderate** for D₃ + calcium in hip fracture prevention in the elderly

**Rickets prevention:** Unequivocal evidence from uncontrolled historical studies and surveillance data after fortification programmes; no modern RCT ethically feasible or necessary.

### VITAL Trial (2019) — Non-Skeletal Outcomes

The landmark VITAL (VITamin D and OmegA-3 TriaL) RCT: [^vital-trial-2019]
- n=25,871 adults; vitamin D₃ 2,000 IU/day + omega-3 (1 g/day) vs. placebo; median follow-up 5.3 years
- **Primary outcomes:**
  - **Cancer incidence:** No significant reduction overall (HR 0.96; 95% CI 0.88–1.06)
  - **Cardiovascular events (MACE):** No significant reduction (HR 0.97; 95% CI 0.85–1.12)
- **Notable secondary findings:**
  - Cancer-related mortality reduced (HR 0.83; 95% CI 0.67–1.02; p=0.06 — marginal)
  - Metastatic cancer risk reduced in the vitamin D group (HR 0.83 for cancer death after diagnosis, p=0.04 in supplementary analysis)
  - Participants with BMI <25: greater cancer risk reduction vs. overweight/obese
  - No benefit demonstrated for autoimmune diseases or diabetes as primary endpoints in VITAL
- **Interpretation:** VITAL definitively showed no benefit for cardiovascular disease or overall cancer incidence from 2,000 IU/day D₃ supplementation in a well-nourished US population with median baseline 25(OH)D ~30 ng/mL (already sufficient). This does not rule out benefit in truly deficient populations.

### Respiratory Infections — Martineau Meta-analysis (2017)

BMJ meta-analysis of 25 RCTs (n=11,321):
- Vitamin D supplementation reduced the proportion experiencing at least one acute respiratory tract infection (OR 0.88; 95% CI 0.81–0.96; p=0.002)
- Daily or weekly dosing: significant protection (OR 0.81; 95% CI 0.72–0.91)
- Bolus dosing (single large doses): no significant benefit
- Effect strongest in severely deficient participants (25(OH)D <25 nmol/L): OR 0.30 (70% risk reduction)
- GRADE: **Moderate** (high-quality systematic review; pre-specified analysis plan)

### Non-skeletal Evidence Summary (Autier et al., 2017)

Landmark re-analysis of non-skeletal vitamin D RCT data: [^autier-2014-vitamin-d-bmj]
- **Key conclusion:** While observational studies show strong inverse associations between 25(OH)D and numerous disease outcomes, **RCTs consistently fail to replicate these benefits** — suggesting low 25(OH)D is largely a *consequence* of poor health (reverse causation: sick, inactive people go outdoors less → lower D₃ synthesis) rather than a cause
- This does not negate the established role of vitamin D in skeletal health and severe deficiency treatment
- GRADE for non-skeletal indications (cancer, CVD, T2D, MS, autoimmunity): **Low to Insufficient**

## Connections

- **Modulates** → [Musculoskeletal System](../../../../../01-human/07-system/musculoskeletal-system/README.md): Calcitriol is the primary hormonal driver of intestinal calcium absorption (via TRPV6/calbindin-D9k) and renal calcium reabsorption (TRPV5); VDR-driven RANKL expression couples mineral homeostasis to bone remodelling; deficiency produces rickets in children and osteomalacia/osteoporosis in adults.

- **Modulates** → [Immune System](../../../../../01-human/07-system/immune-system/README.md): VDR activation in macrophages and dendritic cells induces cathelicidin (LL-37) and β-defensin 2 for frontline antimicrobial innate defence; simultaneously dampens adaptive immune overactivation by suppressing Th1/Th17 polarisation and DC-derived IL-12, creating an immunomodulatory rather than broadly immunosuppressive effect.

- **Modulates** → [Regulatory T Cell](../../../../../01-human/04-cellular/regulatory-t-cell/README.md): Calcitriol, acting through VDR expressed in naïve CD4+ T cells, promotes Foxp3+ Treg differentiation by upregulating IL-2 signalling and CTLA-4 expression; the resultant Treg expansion suppresses autoreactive effector T-cell populations implicated in MS, T1D, and inflammatory bowel disease pathogenesis.

- **Modulates** → [Kidney](../../../../../01-human/06-organ/kidney/README.md): The kidney is the dominant site of calcitriol production via proximal tubular CYP27B1, under PTH stimulation; CYP24A1-mediated calcitriol inactivation also occurs here under FGF-23/VDR feedback; renal tubular TRPV5 and calbindin-D28k expression (VDR targets) determine final urinary calcium reabsorption, completing the calcium homeostasis circuit.

[^holick-2007-vitamin-d-nejm]: Holick MF. N Engl J Med. 2007;357(3):266-81. doi:10.1056/NEJMra070553
[^autier-2014-vitamin-d-bmj]: Autier P et al. Lancet Diabetes Endocrinol. 2017;5(12):986-1004. doi:10.1016/S2213-8587(17)30357-1
[^vital-trial-2019]: Manson JE et al. N Engl J Med. 2019;380(1):33-44. doi:10.1056/NEJMoa1809944

---
*This page is co-maintained with AI assistance. Content reflects current scientific literature as of the last review date; it is not medical advice. See [footer disclaimer](../../../README.md) for full terms.*
