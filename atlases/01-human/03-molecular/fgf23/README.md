---
schema: human-scale-entry/v1
id: fgf23
name: FGF23
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-07
summary: "FGF23 is an osteocyte-secreted hormone that reduces renal phosphate reabsorption and inhibits vitamin D activation via FGFR1/αKlotho; elevated 100-1000× in CKD → drives secondary hyperparathyroidism, LVH, and mortality; burosumab (anti-FGF23) treats XLH-related rickets."
aliases: ["FGF23", "fibroblast growth factor 23", "FGF-23", "phosphatonin", "XLH phosphate regulator", "CKD-MBD mediator", "hypophosphatemia FGF23"]
cross_links:
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "FGF23 rises 100-1000× in CKD → suppresses 1α-hydroxylase → reduced calcitriol → secondary hyperparathyroidism and CKD-MBD; very high FGF23 predicts LVH, heart failure, and mortality in dialysis patients independent of traditional risk factors."
  - target: 01-human/07-system/heart-failure
    relation: connects-to
    note: "Elevated FGF23 in CKD activates cardiac FGFR4 independent of αKlotho → HDAC4 nuclear translocation → cardiac hypertrophic gene program → LVH and HF; FGF23 is an independent predictor of incident heart failure and cardiovascular death in CKD and the general population."
  - target: 01-human/07-system/osteoporosis
    relation: connects-to
    note: "FGF23 inhibits 1α-hydroxylase → reduces calcitriol → decreases intestinal calcium absorption → bone demineralization; genetic FGF23 excess (XLH, ARHR) causes hypophosphatemic rickets; burosumab (anti-FGF23 mAb) corrects hypophosphatemia and heals rickets in XLH."
  - target: 01-human/03-molecular/aldosterone
    relation: connects-to
    note: "FGF23 stimulates aldosterone secretion from the adrenal gland via FGFR1 independently of the RAAS; elevated FGF23 in CKD → hyperaldosteronism → volume expansion and hypertension; FGF23-aldosterone axis may amplify cardiovascular risk in CKD beyond RAAS blockade."
sources:
  - id: shimada-2004-fgf23-vitamin-d
    type: peer-reviewed
    cite: "Shimada T, Hasegawa H, Yamazaki Y, et al. FGF-23 is a potent regulator of vitamin D metabolism and phosphate homeostasis. J Bone Miner Res. 2004;19(3):429-435."
    doi: "10.1359/JBMR.0301264"
    pmid: "15040830"
    url: "https://doi.org/10.1359/JBMR.0301264"
  - id: gutierrez-2008-fgf23-mortality
    type: peer-reviewed
    cite: "Gutierrez OM, Mannstadt M, Isakova T, et al. Fibroblast growth factor 23 and mortality among patients undergoing hemodialysis. N Engl J Med. 2008;359(6):584-592."
    doi: "10.1056/NEJMoa0706130"
    pmid: "18687639"
    url: "https://doi.org/10.1056/NEJMoa0706130"
---

# FGF23

## Overview

**FGF23** (fibroblast growth factor 23; gene *FGF23*, chromosome 12p13.3) is a **32 kDa N-glycosylated endocrine hormone** secreted primarily by **osteocytes** and osteoblasts in bone. Unlike the majority of FGF family members (which act locally as paracrine/autocrine growth factors), FGF23 circulates in blood and acts on distant target organs — particularly the **kidney** and **parathyroid gland** — to regulate **phosphate homeostasis** and **vitamin D metabolism**. FGF23 is the central humoral mediator of the **bone-kidney-parathyroid endocrine axis**.

Shimada et al. (2004) established FGF23 as a potent phosphatonin — demonstrating that FGF23 injection suppresses renal sodium-phosphate cotransporters and 1α-hydroxylase activity, reducing serum phosphate and calcitriol [^shimada-2004-fgf23-vitamin-d]. Gutierrez et al. (2008) then demonstrated that extremely elevated FGF23 levels in hemodialysis patients independently predicted mortality — identifying FGF23 as a major cardiovascular risk factor in chronic kidney disease (CKD) [^gutierrez-2008-fgf23-mortality].

**FGF23 in disease — a spectrum from deficiency to excess:**

| State | FGF23 level | Phosphate | Calcitriol | Consequence |
|---|---|---|---|---|
| X-linked hypophosphatemia (XLH) | Very high | Low (renal loss) | Low | Rickets/osteomalacia, fractures |
| Tumor-induced osteomalacia | High | Low | Low | Renal phosphate wasting |
| CKD G3-G5 | 10–1000× elevated | High (retained) | Low | CKD-MBD, LVH, mortality |
| Hypoparathyroidism (treated) | Low | Normal | Normal | FGF23 suppresses PTH independently |
| Tumoral calcinosis (GALNT3/KL mutation) | Very low | High | High | Ectopic calcification |

## Structure

FGF23 is a 251 amino acid protein with three distinct domains:

**N-terminal FGF homology domain (aa 1–180):**
- Contains the receptor-binding region; shares structural homology with other FGF family members
- Binds FGFR1c (and FGFR3c, FGFR4) in the presence of the co-receptor αKlotho
- **αKlotho (KL):** A single-pass transmembrane protein expressed highly in kidney distal tubule and parathyroid gland; αKlotho acts as a scaffold to form a ternary complex with FGF23 and FGFR — dramatically enhancing binding affinity (Kd shift from µM to nM)
- In the **heart**, αKlotho expression is very low → FGF23 activates FGFR4 (which has detectable expression without requiring αKlotho) → downstream HDAC4/NFAT → cardiac hypertrophy

**C-terminal tail (aa 181–251):**
- Contains the O-glycosylation site Thr178 (GALNT3-modified) — protects from furin cleavage
- **Furin cleavage site (Arg176–Ile177↓Thr178):** Furin endoprotease cleaves FGF23 into inactive N- and C-terminal fragments; O-glycosylation at Thr178 blocks furin — regulating the ratio of intact bioactive to inactive cleaved FGF23
- **FGF23 mutations (XLH/ADHR):** R176Q/R179Q mutations abolish furin cleavage → accumulation of intact FGF23 → chronic phosphaturia
- **GALNT3 mutations:** Reduce O-glycosylation → increased furin cleavage → low intact FGF23 → hyperphosphatemia → tumoral calcinosis

## Function

**Renal phosphate regulation (proximal tubule):**
- FGF23 binds FGFR1c/αKlotho on apical membrane of proximal tubule S1 segment
- FGF23/FGFR1/αKlotho → Ras/ERK1/2 → NHERF1 phosphorylation → internalization of NaPi-IIa (SLC34A1) and NaPi-IIc (SLC34A3) from the brush border → reduced renal phosphate reabsorption → **phosphaturia**
- Net effect: FGF23 is the primary hormone controlling renal phosphate excretion (analogous to PTH's role in calcium)

**Vitamin D suppression (proximal tubule):**
- FGF23 → reduces CYP27B1 (1α-hydroxylase) expression → less conversion of 25-OH-D₃ to 1,25-OH₂-D₃ (calcitriol)
- FGF23 → induces CYP24A1 (24-hydroxylase) → increased calcitriol catabolism
- Net: FGF23 actively suppresses calcitriol — creating a feedback that prevents hypervitaminosis D during phosphate excess

**Parathyroid regulation:**
- FGF23 binds FGFR1/αKlotho on parathyroid chief cells → directly suppresses PTH secretion
- In CKD: elevated FGF23 initially suppresses PTH (protective), but as renal αKlotho expression falls (CKD depletes Klotho) → FGF23 resistance in parathyroid → PTH escapes → secondary hyperparathyroidism despite very high FGF23

**Bone mineralization:**
- FGF23 is produced by osteocytes in response to dietary phosphate load and circulating PTH/calcitriol
- Phosphate → stimulates FGF23 secretion → phosphaturia → normalizes serum phosphate (negative feedback)
- Calcitriol → potent stimulator of FGF23 production (a counter-regulatory loop)
- PTH → enhances FGF23 production → limits PTH-driven calcitriol excess

## Mechanism

**FGF23 signaling cascade:**

1. FGF23 (intact, O-glycosylated) → binds FGFR1c extracellular Ig domains → αKlotho co-receptor bridges FGFR and FGF23 C-terminal domain
2. FGFR1 kinase domain activation → autophosphorylation → FRS2α (FGFR substrate 2α) phosphorylation
3. FRS2α → Grb2/SOS → Ras/RAF/MEK → **ERK1/2 activation** — dominant signaling pathway in kidney
4. Parallel: PI3K/Akt activation → mTORC1 — regulates some downstream gene expression
5. In proximal tubule: ERK1/2 → NHERF1 phosphorylation → NaPi-IIa/IIc internalization → phosphaturia
6. In proximal tubule: ERK1/2 → Sp1/VDRE → CYP27B1 suppression

**Cardiac pathway (FGFR4/Klotho-independent):**
- High FGF23 (as in CKD) → binds FGFR4 on cardiomyocytes (low affinity, requires high concentrations)
- FGFR4 → PLCγ → calcineurin/NFAT pathway → fetal gene program (β-MHC, ANP, BNP re-expression) → **concentric LVH**
- Independently: FGF23 → FGFR4 → HDAC4 nuclear entry → CaMKII/calmodulin → transcriptional regulation of Ca²⁺ handling genes → impaired SR Ca²⁺ reuptake → diastolic dysfunction

**FGF23 and CKD-cardiovascular axis:**
In CKD, phosphate retention is the earliest metabolic derangement (even when GFR is >60 mL/min):
- Phosphate → FGF23 ↑ (compensatory phosphaturia, maintains normal serum phosphate)
- Elevated FGF23 → suppresses calcitriol → Ca²⁺ malabsorption → secondary hyperparathyroidism
- Very high FGF23 (CKD G4-G5) → directly toxic to cardiomyocytes (FGFR4) → LVH
- FGF23 predicts all-cause mortality and cardiovascular events in CKD patients more strongly than PTH or phosphate alone

**Therapeutic targets:**
- **Burosumab (Crysvita; anti-FGF23 mAb):** FDA-approved for XLH (children ≥1 year and adults) and tumor-induced osteomalacia; normalizes serum phosphate, heals rickets, improves bone density; SC every 2 weeks
- **Phosphate binders (sevelamer, calcium carbonate, lanthanum carbonate):** Reduce intestinal phosphate absorption → lower FGF23 in CKD; sevelamer also binds bile acids → may have pleiotropic anti-inflammatory effects
- **Calcimimetics (cinacalcet, etelcalcetide):** Suppress PTH → secondarily reduce FGF23 in CKD-MBD
- **Active vitamin D analogues (calcitriol, paricalcitol):** Must be used cautiously — increase FGF23 production as a counter-regulatory effect; titrate to avoid worsening FGF23 excess

## Connections

FGF23 rises 100-1000× in CKD → suppresses 1α-hydroxylase → reduced calcitriol → secondary hyperparathyroidism and CKD-MBD; very high FGF23 predicts LVH, heart failure, and mortality in dialysis patients independent of traditional risk factors.

Elevated FGF23 in CKD activates cardiac FGFR4 independent of αKlotho → HDAC4 nuclear translocation → cardiac hypertrophic gene program → LVH and HF; FGF23 is an independent predictor of incident heart failure and cardiovascular death in CKD and the general population.

FGF23 inhibits 1α-hydroxylase → reduces calcitriol → decreases intestinal calcium absorption → bone demineralization; genetic FGF23 excess (XLH, ARHR) causes hypophosphatemic rickets; burosumab (anti-FGF23 mAb) corrects hypophosphatemia and heals rickets in XLH.

FGF23 stimulates aldosterone secretion from the adrenal gland via FGFR1 independently of the RAAS; elevated FGF23 in CKD → hyperaldosteronism → volume expansion and hypertension; FGF23-aldosterone axis may amplify cardiovascular risk in CKD beyond RAAS blockade.

[^shimada-2004-fgf23-vitamin-d]: Shimada T, Hasegawa H, Yamazaki Y, et al. FGF-23 is a potent regulator of vitamin D metabolism and phosphate homeostasis. *J Bone Miner Res.* 2004;19(3):429-435. [doi:10.1359/JBMR.0301264](https://doi.org/10.1359/JBMR.0301264) · [PubMed 15040830](https://pubmed.ncbi.nlm.nih.gov/15040830/)
[^gutierrez-2008-fgf23-mortality]: Gutierrez OM, Mannstadt M, Isakova T, et al. Fibroblast growth factor 23 and mortality among patients undergoing hemodialysis. *N Engl J Med.* 2008;359(6):584-592. [doi:10.1056/NEJMoa0706130](https://doi.org/10.1056/NEJMoa0706130) · [PubMed 18687639](https://pubmed.ncbi.nlm.nih.gov/18687639/)
