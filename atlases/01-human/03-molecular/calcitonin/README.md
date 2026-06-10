---
schema: human-scale-entry/v1
id: calcitonin
name: Calcitonin
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-07
summary: "Calcitonin is a 32-aa thyroid C-cell peptide that inhibits osteoclasts via CTR → cAMP → cytoskeletal collapse; salmon calcitonin treats Paget's disease and hypercalcemia; serum calcitonin is the primary biomarker for medullary thyroid carcinoma (MTC)."
aliases: ["calcitonin", "CT", "CALCA", "salmon calcitonin", "calcitonin receptor", "CTR", "medullary thyroid carcinoma", "MTC", "Paget's disease", "hypercalcemia"]
cross_links:
  - target: 01-human/07-system/osteoporosis
    relation: connects-to
    note: "Calcitonin → CTR → cAMP → osteoclast cytoskeletal collapse → reduced bone resorption; intranasal salmon calcitonin (200 IU/day) reduces vertebral fractures 36% (PROOF trial) but is less effective than bisphosphonates; reserved for acute pain of recent vertebral fracture."
  - target: 01-human/03-molecular/pth
    relation: connects-to
    note: "Calcitonin and PTH are opposing calcium regulators: PTH → bone resorption and renal calcium retention (raises Ca²⁺); calcitonin → osteoclast inhibition and renal calciuric effect (lowers Ca²⁺); hypercalcemia → C-cell calcitonin secretion counters PTH-driven Ca²⁺ elevation."
  - target: 01-human/07-system/thyroid-cancer
    relation: connects-to
    note: "MTC arises from parafollicular C-cells → secretes calcitonin; serum calcitonin >100 pg/mL strongly suggests MTC; stimulated calcitonin screens RET mutation carriers; normalization post-surgery = curative resection."
  - target: 01-human/03-molecular/fgf23
    relation: connects-to
    note: "Calcitonin receptor (CTR) is expressed on osteoclasts and renal tubular cells; calcitonin → renal CTR → cAMP → inhibits 1α-hydroxylase (reduces calcitriol synthesis); FGF23 also inhibits 1α-hydroxylase — both calcitonin and FGF23 converge on phosphate/calcitriol regulation."
  - target: 01-human/04-cellular/osteoclast
    relation: connects-to
    note: "Calcitonin binds CTR on osteoclasts → Gs → cAMP → PKA → cytoskeletal collapse within minutes halting bone resorption; tachyphylaxis from CTR internalization limits chronic use; osteoclasts express the highest CTR density; acute inhibition underpins hypercalcemia therapy."
  - target: 01-human/06-organ/thyroid
    relation: connects-to
    note: "Calcitonin is synthesized by parafollicular C-cells of the thyroid; C-cell hyperplasia → elevated calcitonin signals RET mutation carrier status or early MTC; thyroidectomy is curative in localized MTC; rising postoperative calcitonin indicates persistent or recurrent disease."
  - target: 01-human/03-molecular/cgrp
    relation: connects-to
    note: "CALCA (chr11p15.2) encodes both calcitonin (thyroid C-cell splice) and α-CGRP (neural splice, 37 aa); CGRP → CLR/RAMP1 → vasodilation and migraine; erenumab and atogepant target CGRP/CLR-RAMP1 for migraine prevention, a clinical extension of CALCA alternative splicing."
sources:
  - id: copp-1962-calcitonin
    type: peer-reviewed
    cite: "Copp DH, Cameron EC, Cheney BA, Davidson AG, Henze KG. Evidence for calcitonin — a new hormone from the parathyroid that lowers blood calcium. Endocrinology. 1962;70:638-649."
    doi: "10.1210/endo-70-5-638"
    pmid: "13881931"
    url: "https://doi.org/10.1210/endo-70-5-638"
  - id: chesnut-2000-calcitonin-proof
    type: peer-reviewed
    cite: "Chesnut CH 3rd, Silverman S, Andriano K, et al. A randomized trial of nasal spray salmon calcitonin in postmenopausal women with established osteoporosis: the prevent recurrence of osteoporotic fractures study. Am J Med. 2000;109(4):267-276."
    doi: "10.1016/S0002-9343(00)00490-3"
    pmid: "10996576"
    url: "https://doi.org/10.1016/S0002-9343(00)00490-3"
---

# Calcitonin

## Overview

**Calcitonin** (CT; gene *CALCA*, chromosome 11p15.2) is a **32-amino acid peptide hormone** secreted by **parafollicular C-cells (clear cells)** of the thyroid gland in response to elevated plasma calcium. Discovered in 1962 by Copp et al. as a "calcitonin" (calcium-toning) factor that rapidly lowered blood calcium [^copp-1962-calcitonin], it is evolutionarily conserved across vertebrates — with salmon calcitonin (from Pacific salmon) being 10–40× more potent in humans than human calcitonin, due to greater receptor affinity and slower clearance.

Calcitonin belongs to the **CALCA gene family** — which encodes both calcitonin (thyroid C-cell transcript) and **α-CGRP** (α-calcitonin gene-related peptide; neural transcript) via alternative RNA splicing from the same gene. This CALCA gene produces calcitonin when spliced in thyroid tissue, and CGRP when spliced in neural tissue — a classic example of tissue-specific alternative splicing determining completely different biologies.

**Three clinical contexts for calcitonin:**
1. **Osteoporosis treatment** — salmon calcitonin (intranasal or SC) reduces osteoclast activity → reduces vertebral fracture risk; substantially less effective than bisphosphonates or denosumab; primary niche is now **acute vertebral fracture pain** (analgesic via central CGRP receptor effects)
2. **Hypercalcemia management** — calcitonin rapidly but transiently lowers calcium (tachyphylaxis within 48 hours); used as adjunct to bisphosphonates or denosumab in severe hypercalcemia
3. **MTC biomarker** — serum calcitonin is the primary biomarker for medullary thyroid carcinoma; used for screening in RET mutation carriers, post-surgical follow-up, and recurrence monitoring

**CALCA gene context:**
- **Thyroid C-cell transcript:** Exons 1–4 included → calcitonin mRNA → calcitonin peptide (bone/calcium regulation)
- **Neural transcript:** Exons 1–3 + exon 5 included → α-CGRP mRNA → CGRP (37 aa; vasodilation; migraine mediator; CLR/RAMP1 receptor; erenumab/atogepant targets CGRP/CGRP receptor for migraine prophylaxis)

## Structure

**Pre-pro-calcitonin → calcitonin processing:**
**Pre-pro-calcitonin (136 aa)** → signal peptide cleavage → **Pro-calcitonin (115 aa)** → prohormone convertase 1/3 → **Calcitonin-N-propeptide (N-ProCT; 57 aa)** + **Calcitonin (32 aa)** + **Katacalcin/C-terminal PDN-21-amide (21 aa)**

**Mature calcitonin (32 aa):**
- **Cys1-Cys7 disulfide bond:** N-terminal ring; essential for receptor binding (N-terminal 8 aa required for CTR activation)
- **N-terminal ring (aa 1–7):** Interacts with the CTR extracellular domain I
- **Central helix (aa 8–22):** Amphipathic α-helix in membrane-mimetic environments; receptor transmembrane domain interaction
- **C-terminal Pro-amide (aa 32-ProNH₂):** Required for high-affinity CTR binding; the amide group is generated by PAM enzyme (as with all C-terminal amidated peptides — ADM, PTH, GLP-1)

**Salmon calcitonin vs. human calcitonin:**
- Salmon CT (sCT): 32 aa; 16/32 residues differ from human CT; the α-helix region is more stable → slower aggregation; Kd for human CTR ~0.1 nM (vs. ~10 nM for human CT in some assays)
- sCT has longer plasma half-life (~70 min vs. ~10 min for human CT)
- sCT is the clinically used therapeutic form (Miacalcic® intranasal 200 IU/day; Calcimar® SC/IM)

**Calcitonin receptor (CTR; CALCR gene, chr7q21.3):**
- Class B GPCR (secretin receptor family); large extracellular domain (ECD) for ligand binding
- Gs-coupled → adenylyl cyclase → cAMP → PKA (primary, dominant pathway in osteoclasts)
- Gq-coupled → PLC → IP₃ → Ca²⁺ (secondary pathway — mediates cytoskeletal effects in some cell types)
- CTR isoforms: CTR-I (with 37-aa insert in second intracellular loop) and CTR-II (no insert) — expressed differentially across tissues
- RAMPs modify CTR specificity → CTR/RAMP1 = amylin₁ receptor; CTR/RAMP2 = amylin₂ receptor; CTR/RAMP3 = amylin₃ receptor (demonstrating that CTR, like CLR, is a RAMP-regulated receptor)
- CTR expression: osteoclasts (highest), kidney tubular cells, brain (hypothalamus, area postrema), gut, lung

**Procalcitonin (PCT):**
- The immediate precursor, pro-calcitonin (115 aa), circulates at very low levels in health (~0.05 ng/mL) — C-cells efficiently process it to calcitonin
- In **sepsis**: non-thyroidal cells (liver, monocytes, adipose, muscle) massively upregulate PCT transcription via NF-κB (IL-1β, TNF-α, LPS stimulus) → PCT released without processing to calcitonin → serum PCT rises dramatically (>10 ng/mL in severe bacterial sepsis)
- PCT is the gold-standard biomarker for bacterial (not viral) infection and guides antibiotic de-escalation (ProHOSP, SAPS II studies); distinct from calcitonin's bone biology

## Function

**Osteoclast inhibition (dominant anti-resorptive mechanism):**
1. Calcitonin → CTR on mature osteoclasts → Gs → cAMP → PKA → **cytoskeletal collapse**: osteoclast ruffled border (the resorptive membrane) disassembles; actin ring disrupted → osteoclast detaches from bone surface
2. PKA also phosphorylates **VASP** (vasodilator-stimulated phosphoprotein) → stabilizes cortical actin → prevents re-attachment of active osteoclasts
3. Result: osteoclasts enter a quiescent "resting" state within minutes of calcitonin exposure → immediate reduction in bone resorption markers (CTX, NTX fall within 4–6 hours of SC calcitonin injection)
4. Tachyphylaxis: CTR downregulates (internalization, desensitization) within 24–48 hours of continuous calcitonin exposure → loss of anti-resorptive effect; this limits calcitonin's utility in chronic osteoporosis management
5. Note: calcitonin does NOT stimulate osteoblast bone formation (unlike PTH); purely anti-resorptive (in contrast with anabolic agents)

**Renal calcium handling:**
- CTR on renal tubular cells → cAMP → inhibits calcium reabsorption in the loop of Henle and distal tubule → **calciuric effect** (calcium excretion increases)
- This opposes PTH's calcium-retaining effect → complementary calcium-lowering mechanism in hypercalcemia

**Central effects (analgesic — clinical importance):**
- Calcitonin receptors in brain hypothalamus and spinal cord dorsal horn
- Intranasal salmon calcitonin → analgesic effect in vertebral fracture pain (VAS pain score reduction); mechanism involves spinal β-endorphin release and central modulation of pain signaling via CTR → cAMP → enkephalin release
- This central analgesic effect, independent of bone biology, is the primary reason calcitonin is retained in clinical guidelines for **acute vertebral fracture pain management** (while its anti-fracture efficacy is modest vs. bisphosphonates)

**Satiety and appetite regulation:**
- CTR/RAMP1/2/3 in area postrema and hypothalamus → amylin-like satiety signaling; calcitonin itself has satiety effects in pharmacological doses
- Cross-reactivity with amylin receptor → weight loss effects reported with high-dose calcitonin

## Mechanism

**Osteoporosis treatment (PROOF trial) [^chesnut-2000-calcitonin-proof]:**
- **PROOF (Prevent Recurrence of Osteoporotic Fractures)** trial: intranasal salmon calcitonin 200 IU/day vs. 100 IU/day vs. 400 IU/day vs. placebo in 1,255 postmenopausal women with osteoporosis (5-year follow-up)
- Primary result: 200 IU/day → **36% RRR for new vertebral fractures** (RR 0.64; 95% CI 0.47–0.87 vs. placebo); 100 IU and 400 IU showed no significant benefit (anomalous dose-response)
- No significant reduction in non-vertebral or hip fractures (underpowered; small BMD gains)
- Limitations: high dropout rate (~50%), anomalous dose-response, and survival bias concerns
- Context: PROOF established calcitonin as an osteoporosis treatment but subsequent meta-analyses and the availability of more potent agents (bisphosphonates, denosumab, teriparatide, romosozumab) have relegated calcitonin to adjunct use

**Current clinical indications:**
| Indication | Formulation | Rationale |
|---|---|---|
| Acute vertebral fracture pain | Intranasal sCT 200 IU/day × 4 weeks | Central analgesic; pain control while fracture heals |
| Paget's disease of bone | SC/IM sCT 100 IU/day | Anti-osteoclastic; reduces alkaline phosphatase and pain; now largely replaced by bisphosphonates |
| Hypercalcemia of malignancy | SC/IM sCT 4–8 IU/kg Q6–12h | Rapid (hours) calciuric effect; used as bridge while zoledronate or denosumab onset is delayed |
| MTC follow-up | Serum calcitonin measurement | Calcitonin normalization = complete remission; rising CT = recurrence |

**Medullary thyroid carcinoma (MTC) biomarker:**
- MTC arises from thyroid C-cells → constitutively secretes calcitonin → serum calcitonin (normal <10 pg/mL in women, <18.5 pg/mL in men)
- MTC: basal calcitonin typically >100 pg/mL; often >1,000 pg/mL in advanced disease
- **Stimulated calcitonin** (calcium gluconate IV or pentagastrin): used to unmask occult MTC in RET mutation carriers (screen before thyroidectomy); peak calcitonin >100 pg/mL → surgical referral
- **RET mutations** (MEN2A/2B, FMTC): calcitonin screening begins in childhood; prophylactic thyroidectomy before MTC develops; vandetanib and cabozantinib (RET inhibitors) treat unresectable/metastatic MTC

## Connections

- `connects-to` → **[Osteoporosis](../../07-system/osteoporosis/README.md)** — calcitonin → CTR → cAMP → osteoclast cytoskeletal collapse → reduced bone resorption; intranasal salmon calcitonin (200 IU/day) reduces vertebral fractures 36% (PROOF trial) but is less effective than bisphosphonates; reserved for acute pain of recent vertebral fracture.
- `connects-to` → **[PTH](../pth/README.md)** — calcitonin and PTH are opposing calcium regulators: PTH → bone resorption and renal calcium retention (raises Ca²⁺); calcitonin → osteoclast inhibition and renal calciuric effect (lowers Ca²⁺); hypercalcemia → C-cell calcitonin secretion counters PTH-driven Ca²⁺ elevation.
- `connects-to` → **[Thyroid Cancer](../../07-system/thyroid-cancer/README.md)** — MTC arises from parafollicular C-cells → secretes calcitonin; serum calcitonin >100 pg/mL strongly suggests MTC; stimulated calcitonin screens RET mutation carriers; normalization post-surgery = curative resection.
- `connects-to` → **[FGF23](../fgf23/README.md)** — calcitonin → renal CTR → cAMP → inhibits 1α-hydroxylase (reduces calcitriol synthesis); FGF23 also inhibits 1α-hydroxylase — both calcitonin and FGF23 converge on phosphate/calcitriol regulation; renal CTR is expressed on tubular cells.
- `connects-to` → **[Osteoclast](../../04-cellular/osteoclast/README.md)** — calcitonin binds CTR on osteoclasts → Gs → cAMP → PKA → cytoskeletal collapse within minutes halting bone resorption; tachyphylaxis from CTR internalization limits chronic use; osteoclasts express the highest CTR density; acute inhibition underpins hypercalcemia therapy.
- `connects-to` → **[Thyroid](../../06-organ/thyroid/README.md)** — calcitonin is synthesized by parafollicular C-cells of the thyroid; C-cell hyperplasia → elevated calcitonin signals RET mutation carrier status or early MTC; thyroidectomy is curative in localized MTC; rising postoperative calcitonin indicates persistent or recurrent disease.
- `connects-to` → **[CGRP](../cgrp/README.md)** — CALCA (chr11p15.2) encodes both calcitonin (thyroid C-cell splice) and α-CGRP (neural splice, 37 aa); CGRP → CLR/RAMP1 → vasodilation and migraine; erenumab and atogepant target CGRP/CLR-RAMP1 for migraine prevention, a clinical extension of CALCA alternative splicing.

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^copp-1962-calcitonin]: Copp DH, Cameron EC, Cheney BA, Davidson AG, Henze KG. Evidence for calcitonin — a new hormone from the parathyroid that lowers blood calcium. *Endocrinology.* 1962;70:638-649. [doi:10.1210/endo-70-5-638](https://doi.org/10.1210/endo-70-5-638) · [PubMed 13881931](https://pubmed.ncbi.nlm.nih.gov/13881931/)
[^chesnut-2000-calcitonin-proof]: Chesnut CH 3rd, Silverman S, Andriano K, et al. A randomized trial of nasal spray salmon calcitonin in postmenopausal women with established osteoporosis: the prevent recurrence of osteoporotic fractures study. *Am J Med.* 2000;109(4):267-276. [doi:10.1016/S0002-9343(00)00490-3](https://doi.org/10.1016/S0002-9343(00)00490-3) · [PubMed 10996576](https://pubmed.ncbi.nlm.nih.gov/10996576/)
