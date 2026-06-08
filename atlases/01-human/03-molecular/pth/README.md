---
schema: human-scale-entry/v1
id: pth
name: PTH
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-07
summary: "PTH raises serum calcium via bone resorption (RANKL), renal calcium retention, and calcitriol synthesis; primary hyperparathyroidism causes hypercalcemia; CKD drives secondary hyperparathyroidism; intermittent PTH 1-34 (teriparatide) is anabolic for osteoporosis."
aliases: ["PTH", "parathyroid hormone", "PTH1R", "teriparatide", "PTH 1-34", "PTH 1-84", "parathyroid", "cinacalcet", "CaSR", "hyperparathyroidism", "hypoparathyroidism", "PTHrP"]
cross_links:
  - target: 01-human/07-system/osteoporosis
    relation: connects-to
    note: "Continuous PTH → RANKL → osteoclast activation and bone resorption; intermittent PTH 1-34 (teriparatide, SC daily) preferentially activates Wnt signaling in osteoblasts → net anabolic effect; FPT trial: 65% RRR for vertebral fractures; PTH 1-84 treats hypoparathyroidism."
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "In CKD, reduced calcitriol and hyperphosphatemia → secondary hyperparathyroidism (SHPT); chronic PTH excess → renal osteodystrophy and vascular calcification; cinacalcet (CaSR agonist) and calcitriol/paricalcitol suppress SHPT and improve CKD-MBD."
  - target: 01-human/03-molecular/fgf23
    relation: connects-to
    note: "FGF23 suppresses PTH secretion via FGFR1/αKlotho in the parathyroid gland; PTH reciprocally stimulates FGF23 from osteocytes; in CKD, Klotho depletion blunts FGF23-mediated PTH suppression → both rise simultaneously driving CKD-MBD."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "Chronic PTH excess in primary and secondary hyperparathyroidism → vascular calcification, LVH, and endothelial dysfunction; cinacalcet (EVOLVE trial) reduced cardiovascular events in dialysis patients with SHPT."
sources:
  - id: bilezikian-2018-phpt-review
    type: peer-reviewed
    cite: "Bilezikian JP, Bandeira L, Khan A, Cusano NE. Hyperparathyroidism. Lancet. 2018;391(10116):168-178."
    doi: "10.1016/S0140-6736(17)31430-7"
    pmid: "29331474"
    url: "https://doi.org/10.1016/S0140-6736(17)31430-7"
  - id: neer-2001-teriparatide-fpt
    type: peer-reviewed
    cite: "Neer RM, Arnaud CD, Zanchetta JR, et al. Effect of parathyroid hormone (1-34) on fractures and bone mineral density in postmenopausal women with osteoporosis. N Engl J Med. 2001;344(19):1434-1441."
    doi: "10.1056/NEJM200105103441904"
    pmid: "11346808"
    url: "https://doi.org/10.1056/NEJM200105103441904"
---

# PTH

## Overview

**PTH** (parathyroid hormone; gene *PTH*, chromosome 11p15.3) is an **84-amino acid peptide hormone** secreted by **parathyroid chief cells** — the master regulator of serum calcium and phosphate homeostasis. PTH is the primary acute responder to hypocalcemia, acting within minutes to raise calcium by mobilizing bone stores (RANKL-mediated osteoclastic resorption), increasing renal calcium reabsorption, and stimulating calcitriol (1,25-dihydroxyvitamin D₃) synthesis — which in turn increases intestinal calcium absorption.

PTH biology is uniquely dose-rate–dependent: **continuous elevated PTH (endogenous or infusion)** drives net bone resorption; **intermittent low-dose PTH (subcutaneous daily injection)** paradoxically stimulates anabolic bone formation by activating Wnt/β-catenin signaling in osteoblasts faster than it upregulates RANKL. This duality is the pharmacologic basis of **teriparatide (PTH 1-34)** and **abaloparatide (PTHrP 1-34 analogue)** — the only approved anabolic osteoporosis therapies with proven vertebral and non-vertebral fracture reduction [^neer-2001-teriparatide-fpt].

The calcium-sensing receptor (**CaSR**, chromosome 3q21.1) on parathyroid chief cells responds to extracellular calcium: hypocalcemia → CaSR is less activated → PTH released; hypercalcemia → CaSR activated → PTH suppressed. **Cinacalcet (Sensipar)** is an allosteric CaSR agonist (calcimimetic) — it increases CaSR sensitivity → suppresses PTH → used to treat primary hyperparathyroidism and secondary hyperparathyroidism in CKD [^bilezikian-2018-phpt-review].

**Clinical syndromes:**

| Condition | PTH | Calcium | Phosphate | Key mechanism |
|---|---|---|---|---|
| Primary hyperparathyroidism (PHPT) | ↑↑ | ↑ | ↓ | Autonomous PTH secretion (adenoma 80%, hyperplasia 15%, carcinoma <1%) |
| Secondary hyperparathyroidism | ↑↑ | N/↓ | ↑ | CKD → reduced calcitriol + hyperphosphatemia → sustained PTH drive |
| Tertiary hyperparathyroidism | ↑↑ | ↑ | ↑ | Autonomous function after prolonged SHPT (post-transplant) |
| Hypoparathyroidism | ↓ | ↓ | ↑ | Post-thyroidectomy most common; autoimmune; DiGeorge syndrome |
| PTHrP excess | suppressed | ↑ | ↓ | Humoral hypercalcemia of malignancy (SCC, RCC, breast cancer) |

## Structure

PTH is synthesized as a **115-amino acid prepro-PTH** → signal sequence cleavage (−25 aa) → **pro-PTH (90 aa)** → propeptide cleavage (−6 aa) → **mature PTH (84 aa)** stored in secretory granules:

**Functional domains:**
- **N-terminal 1-34 (PTH 1-34):** Required for PTH1R binding and activation; all known calcium-raising and anabolic effects map to this region
- **Mid-region (35-65):** Binds a subpopulation of CPTH2 receptors; modulates osteoclast activity; circulates as C-terminal fragments (renally cleared — accumulate in CKD)
- **C-terminal (66-84):** No PTH1R activity; large C-terminal PTH fragments accumulate in CKD (long half-life) → complicate immunoassay interpretation

**Receptor:**
- **PTH1R (GPCR):** Expressed in kidney proximal tubule, distal tubule, bone (osteoblasts and osteocytes); couples to Gαs → cAMP → PKA and to Gαq → IP₃/DAG → PKC; also activates MAPK and Wnt pathways via β-arrestin
- **PTH2R:** Expressed in brain, testis, pancreas; activated by TIP39 (tuberoinfundibular peptide); limited clinical relevance
- **CPTH2 receptor:** C-terminal PTH receptor on osteoclasts; mediates PTH-independent bone effects of C-terminal fragments

## Function

**Calcium homeostasis — three target organs:**

*Bone (acute: 0–24h):*
- PTH binds PTH1R on osteoblasts/osteocytes → RANKL upregulation → RANK on osteoclast precursors → osteoclastogenesis → lacunar bone resorption → Ca²⁺ and phosphate released
- Simultaneously reduces OPG (osteoprotegerin, a RANKL decoy receptor) → disinhibits osteoclast activation
- Under continuous high PTH: net resorption dominates → progressive BMD loss (hyperparathyroidism pattern)
- Under intermittent low PTH: Wnt/LRP5/β-catenin activated in osteoblasts → preosteoblast proliferation and differentiation > RANKL effect → net bone formation (teriparatide mechanism)

*Kidney:*
- **Proximal tubule:** Reduces NaPi-IIa/NaPi-IIc cotransporter expression → phosphaturia (↑ urinary phosphate); inhibits bicarbonate reabsorption → mild hyperchloremic metabolic acidosis in PHPT
- **Distal tubule:** Stimulates TRPV5 Ca²⁺ channels and calbindin → increased calcium reabsorption → hypocalciuria (net calcium retention despite increased filtered load)
- **1α-hydroxylase (CYP27B1):** PTH stimulates 25-OH-D → 1,25-(OH)₂-D (calcitriol) conversion → increased intestinal calcium and phosphate absorption

*Intestine (indirect via calcitriol):*
- Calcitriol → VDR → TRPV6, calbindin-D9k expression → transcellular Ca²⁺ absorption in duodenum and jejunum
- Also increases phosphate absorption via NaPi-IIb → counteracts renal phosphaturia

**Phosphate regulation:**
- PTH lowers serum phosphate by two mechanisms: increased renal phosphate excretion (direct) and stimulated FGF23 release from osteocytes (indirect) — FGF23 also reduces renal phosphate reabsorption and calcitriol synthesis
- In primary hyperparathyroidism: hypercalcemia + hypophosphatemia + mild hypercalciuria (despite increased TRPV5) → the biochemical signature

## Mechanism

**PTH1R signaling cascade:**

1. PTH(1-34) binds PTH1R extracellular loops → receptor conformational change → Gαs activation
2. Gαs → adenylyl cyclase → cAMP ↑ → PKA → CREB phosphorylation → gene transcription (RANKL, CYP27B1, TRPV5)
3. Gαq (at high [PTH]) → PLC → IP₃ → ER Ca²⁺ release + DAG → PKC → MAPK activation
4. β-arrestin recruitment → internalization + MAPK/ERK signaling (independent of Gα) → contributes to anabolic Wnt signaling

**Teriparatide pharmacology (PTH 1-34):**
- SC injection → peak plasma ~30 min → cleared in ~60–90 min
- Pulse kinetics activate osteoblast anabolic signaling before osteoclast RANKL effects plateau
- **FPT trial (Neer 2001):** PTH 1-34 21 µg daily × 21 months in postmenopausal osteoporosis: **65% RRR** for vertebral fractures (NNT ~11); **35% RRR** non-vertebral fractures; BMD spine +9%, hip +3%
- Maximum 2-year cumulative therapy (lifetime limit); must transition to antiresorptive (bisphosphonate, denosumab) after completion to preserve gains (bone resorbs rapidly without maintenance)
- Black box warning: osteosarcoma in Sprague-Dawley rats at suprapharmacological doses × lifetime; not confirmed in human pharmacovigilance (>2 million patient-years)

**Cinacalcet (calcimimetic) mechanism:**
- Allosteric positive modulator of CaSR (increases CaSR sensitivity to extracellular Ca²⁺)
- In PHPT: cinacalcet reduces PTH and serum calcium; does not improve BMD; preferred when parathyroidectomy is contraindicated
- In SHPT (CKD): reduces PTH, calcium, phosphate; **EVOLVE trial** (SHPT on hemodialysis): cinacalcet vs. placebo — trend toward reduced CV events and mortality (not significant in ITT analysis; post-hoc analyses suggest ~12% reduction in composite CV endpoint after statistical adjustment)

**PTH in CKD-Mineral Bone Disorder (CKD-MBD):**
1. Reduced nephron mass → ↓CYP27B1 → ↓calcitriol → ↓intestinal Ca²⁺ absorption → hypocalcemia
2. GFR ↓ → phosphate retention → FGF23 rise (early compensatory) → further suppresses calcitriol
3. Hypocalcemia + reduced calcitriol → direct PTH gene transcription relief → SHPT
4. Prolonged SHPT → osteitis fibrosa cystica (high-turnover bone disease) → fractures
5. Phosphate overload + high PTH → vascular smooth muscle calcification (calcium × phosphate product)
6. Treatment: dietary phosphate restriction, phosphate binders (calcium-based or non-calcium-based sevelamer/lanthanum), calcitriol/paricalcitol (VDR agonists) → directly suppress PTH gene; cinacalcet → CaSR activation in parathyroid

## Connections

Continuous PTH → RANKL → osteoclast activation and bone resorption; intermittent PTH 1-34 (teriparatide, SC daily) preferentially activates Wnt signaling in osteoblasts → net anabolic effect; FPT trial: 65% RRR for vertebral fractures; PTH 1-84 treats hypoparathyroidism.

In CKD, reduced calcitriol and hyperphosphatemia → secondary hyperparathyroidism (SHPT); chronic PTH excess → renal osteodystrophy and vascular calcification; cinacalcet (CaSR agonist) and calcitriol/paricalcitol suppress SHPT and improve CKD-MBD.

FGF23 suppresses PTH secretion via FGFR1/αKlotho in the parathyroid gland; PTH reciprocally stimulates FGF23 from osteocytes; in CKD, Klotho depletion blunts FGF23-mediated PTH suppression → both rise simultaneously driving CKD-MBD.

Chronic PTH excess in primary and secondary hyperparathyroidism → vascular calcification, LVH, and endothelial dysfunction; cinacalcet (EVOLVE trial) reduced cardiovascular events in dialysis patients with SHPT.

[^bilezikian-2018-phpt-review]: Bilezikian JP, Bandeira L, Khan A, Cusano NE. Hyperparathyroidism. *Lancet.* 2018;391(10116):168-178. [doi:10.1016/S0140-6736(17)31430-7](https://doi.org/10.1016/S0140-6736(17)31430-7) · [PubMed 29331474](https://pubmed.ncbi.nlm.nih.gov/29331474/)
[^neer-2001-teriparatide-fpt]: Neer RM, Arnaud CD, Zanchetta JR, et al. Effect of parathyroid hormone (1-34) on fractures and bone mineral density in postmenopausal women with osteoporosis. *N Engl J Med.* 2001;344(19):1434-1441. [doi:10.1056/NEJM200105103441904](https://doi.org/10.1056/NEJM200105103441904) · [PubMed 11346808](https://pubmed.ncbi.nlm.nih.gov/11346808/)
