---
schema: human-scale-entry/v1
id: osteoporosis
name: Osteoporosis
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-06
summary: "Skeletal disease of low bone density and microarchitectural deterioration → fragility fractures. Driven by estrogen deficiency and osteoclast-osteoblast uncoupling; bisphosphonates, denosumab (RANKL inhibitor), and romosozumab (anti-sclerostin) reduce fracture risk."
aliases: ["osteopenia", "metabolic bone disease", "fragility fracture", "postmenopausal osteoporosis", "glucocorticoid-induced osteoporosis", "secondary osteoporosis"]
sources:
  - id: kanis-2019-who-osteoporosis
    type: peer-reviewed
    cite: "Kanis JA, Cooper C, Rizzoli R, Reginster JY; Scientific Advisory Board of the European Society for Clinical and Economic Aspects of Osteoporosis (ESCEO) and Committees of Scientific Advisors and National Societies of the International Osteoporosis Foundation (IOF). European guidance for the diagnosis and management of osteoporosis in postmenopausal women. Osteoporos Int. 2019;30(1):3-44."
    doi: "10.1007/s00198-018-4704-5"
    pmid: "30324412"
    url: "https://doi.org/10.1007/s00198-018-4704-5"
  - id: cosman-2016-romosozumab
    type: peer-reviewed
    cite: "Cosman F, Crittenden DB, Adachi JD, et al. Romosozumab treatment in postmenopausal women with osteoporosis. N Engl J Med. 2016;375(16):1532-1543."
    doi: "10.1056/NEJMoa1607948"
    pmid: "27641143"
    url: "https://doi.org/10.1056/NEJMoa1607948"
  - id: cummings-2009-denosumab-freedom
    type: peer-reviewed
    cite: "Cummings SR, San Martin J, McClung MR, et al. Denosumab for prevention of fractures in postmenopausal women with osteoporosis. N Engl J Med. 2009;361(8):756-765."
    doi: "10.1056/NEJMoa0809493"
    pmid: "19671655"
    url: "https://doi.org/10.1056/NEJMoa0809493"
cross_links:
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "TGF-beta released from bone matrix during osteoclastic resorption → chemoattractant for osteoblast precursors → bone formation coupling signal; excess TGF-beta (PTH-driven or tumor-derived) → uncoupled osteoclast activation → metastasis-associated bone destruction."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "IL-6 drives RANKL-independent osteoclastogenesis via JAK-STAT3 → osteoclast precursor differentiation; elevated IL-6 in postmenopausal women, RA, and multiple myeloma → accelerated bone loss; tocilizumab reduces bone erosion in RA as a bone-protective effect."
  - target: 01-human/03-molecular/collagen
    relation: connects-to
    note: "Collagen type I is the dominant organic bone matrix component; osteoblasts synthesize type I collagen → osteoid → mineralization; osteoclastic resorption → CTX and NTX (collagen telopeptides) → serum biomarkers of bone resorption used to monitor osteoporosis therapy."
  - target: 01-human/04-cellular/osteoclast
    relation: connects-to
    note: "Osteoclasts are the primary drivers of bone loss: RANKL (from osteoblasts/stromal cells) → RANK on osteoclast precursors → differentiation and lacunar resorption → BMD loss; denosumab (anti-RANKL) neutralizes RANKL → osteoclast suppression → fracture risk reduction."
  - target: 01-human/03-molecular/fgf23
    relation: connects-to
    note: "FGF23 inhibits 1α-hydroxylase → reduces calcitriol → decreases intestinal calcium absorption → bone demineralization; genetic FGF23 excess (XLH, ARHR) causes hypophosphatemic rickets; burosumab (anti-FGF23 mAb) corrects hypophosphatemia and heals rickets in XLH."
  - target: 01-human/03-molecular/pth
    relation: connects-to
    note: "Continuous PTH → RANKL → osteoclast activation and bone resorption; intermittent PTH 1-34 (teriparatide, SC daily) preferentially activates Wnt signaling in osteoblasts → net anabolic effect; FPT trial: 65% RRR for vertebral fractures; PTH 1-84 treats hypoparathyroidism."
  - target: 01-human/03-molecular/calcitonin
    relation: connects-to
    note: "Calcitonin → CTR → cAMP → osteoclast cytoskeletal collapse → reduced bone resorption; intranasal salmon calcitonin (200 IU/day) reduces vertebral fractures 36% (PROOF trial) but is less effective than bisphosphonates; reserved for acute pain of recent vertebral fracture."
  - target: 01-human/03-molecular/rankl
    relation: connects-to
    note: "RANKL (TNFSF11) from osteoblasts/T cells → RANK on osteoclast precursors → TRAF6 → NF-κB → NFATc1 → osteoclast differentiation; OPG decoy ratio governs bone mass; denosumab (anti-RANKL) → 68% vertebral and 40% hip fracture risk reduction (FREEDOM trial)."
  - target: 01-human/03-molecular/sclerostin
    relation: connects-to
    note: "Sclerostin (SOST) from osteocytes → LRP5/6 Wnt antagonism → osteoblast suppression → net bone loss; mechanical loading suppresses sclerostin → anabolic response; romosozumab (anti-sclerostin) → +13% lumbar spine BMD at 12 months; 73% vertebral fracture RRR (FRAME)."
  - target: 01-human/03-molecular/testosterone
    relation: connects-to
    note: "Male hypogonadism (T <300 ng/dL) is a leading cause of secondary male osteoporosis; testosterone maintains BMD via AR on osteoblasts and aromatization to estradiol; ADT causes 2-5% BMD loss/year; denosumab or zoledronate co-administered with ADT prevents fractures."
  - target: 01-human/03-molecular/estrogen
    relation: connects-to
    note: "Estrogen deficiency at menopause → reduced OPG → RANKL excess → osteoclast hyperactivation → 3-5% trabecular bone loss/year; HRT reduces fracture risk ~35%; SERMs (raloxifene) preserve bone without uterine stimulation; bisphosphonates preferred over HRT for fracture prevention."
  - target: 01-human/03-molecular/thyroid-hormones
    relation: connects-to
    note: "Hyperthyroidism accelerates bone remodeling → 10-20% BMD loss at trabecular sites; TSH receptors on osteoblasts exert bone-protective effects; Graves disease → osteoporosis risk; anti-thyroid treatment normalizes bone loss; bisphosphonates co-administered when BMD is low."
  - target: 01-human/04-cellular/osteoblast
    relation: connects-to
    note: "Osteoporosis is a failure of the osteoblast-osteoclast balance: bone-resorbing osteoclasts outpace bone-forming osteoblasts (estrogen loss, aging, steroids), so bone mass and microarchitecture deteriorate—anabolic drugs reverse it by favoring osteoblasts."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "Osteoporosis is the commonest disease of the aging musculoskeletal system: silent bone loss until a fragility fracture (hip, vertebra, wrist) reveals it, and because fractures cause disability and death, bone-density screening and antiresorptives are core to skeletal health."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "Menopause is the leading cause of osteoporosis: the sharp fall in ovarian estrogen accelerates osteoclast-driven bone resorption, so women lose bone rapidly after menopause—linking the reproductive system's hormonal shift to skeletal fragility and fracture risk."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Calcium is the mineral osteoporosis depletes: bone is the body's calcium reservoir, and when intake or absorption falls, parathyroid hormone pulls calcium from bone to keep blood levels constant—so chronic deficiency drives the net bone loss that weakens the skeleton."
  - target: 03-medicine/03-food/vitamin-d
    relation: connects-to
    note: "Vitamin D is essential to prevent osteoporosis: it drives intestinal calcium absorption, so deficiency causes secondary hyperparathyroidism that strips bone, and adequate vitamin D plus calcium is the foundation on which osteoporosis drug therapy is built."
  - target: 01-human/03-molecular/cortisol
    relation: connects-to
    note: "Cortisol excess is a major cause of osteoporosis: glucocorticoids suppress osteoblasts, promote osteoclast survival and reduce calcium absorption, so both Cushing's syndrome and long-term steroid therapy cause rapid bone loss—the most common drug-induced osteoporosis."
  - target: 01-human/05-tissue/bone-marrow
    relation: connects-to
    note: "Bone is remodeled in concert with the marrow it houses: osteoporosis reflects an imbalance between osteoclasts and osteoblasts at the bone-marrow interface, and with age red marrow gives way to fat as bone is lost—linking declining marrow and skeletal mass."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "Magnesium is an underappreciated factor in bone health: about half the body's magnesium sits in bone, and it is needed for vitamin D activation and PTH secretion, so chronic magnesium deficiency impairs mineralization and contributes to osteoporosis."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "Osteoporosis is largely an endocrine disease: estrogen, testosterone, thyroid hormone, parathyroid hormone and cortisol all govern bone turnover, so hormonal shifts (menopause, hyperthyroidism, steroid excess) are leading causes of bone loss."
  - target: 01-human/02-atomic/phosphorus
    relation: connects-to
    note: "Bone is calcium-phosphate crystal, so phosphorus is as structural as calcium: hydroxyapatite needs balanced phosphate, and disordered phosphate handling—too little (osteomalacia) or the excess of kidney disease—weakens or distorts bone alongside calcium loss."
  - target: 01-human/07-system/rheumatoid-arthritis
    relation: connects-to
    note: "Rheumatoid arthritis is a double hit to bone: chronic inflammation (and RANKL) accelerates bone loss, and the glucocorticoids used to treat it cause steroid-induced osteoporosis—so inflammatory arthritis is a leading secondary cause of fragile bones."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "Healthy bone depends on the gut: the intestine absorbs the calcium and vitamin D bone needs, so malabsorption from celiac disease, inflammatory bowel disease, or bariatric surgery is an under-recognized cause of osteoporosis."
  - target: 01-human/04-cellular/adipocyte
    relation: connects-to
    note: "Bone loss in aging tips marrow toward fat: the mesenchymal stem cells that should become bone-building osteoblasts instead become adipocytes, so marrow fills with fat as bone thins—linking the adipocyte-osteoblast balance to osteoporosis."
  - target: 01-human/07-system/multiple-myeloma
    relation: connects-to
    note: "Multiple myeloma masquerades as severe osteoporosis: malignant plasma cells activate osteoclasts (via RANKL) to carve lytic lesions and cause fractures, so unexplained bone loss with anemia or high calcium prompts a myeloma workup."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "Failing kidneys weaken bone—renal osteodystrophy: CKD disturbs phosphate, vitamin D and PTH, deranging bone turnover into a complex osteoporosis-plus-osteomalacia that standard bone drugs can worsen, so diagnosis must come first."
---

# Osteoporosis

## Overview

**Osteoporosis** is a **systemic skeletal disease** characterized by **low bone mineral density (BMD)** and **microarchitectural deterioration of bone tissue** leading to enhanced bone fragility and susceptibility to **fragility fractures** — fractures that occur with minimal trauma (fall from standing height or less). It represents an imbalance in bone remodeling where **osteoclast-mediated resorption exceeds osteoblast-mediated formation**, resulting in net bone loss [^kanis-2019-who-osteoporosis].

**Definition:**
- WHO diagnostic criteria: BMD T-score ≤ −2.5 standard deviations below the young adult mean (peak bone mass) at the lumbar spine, femoral neck, or total hip by DXA (dual-energy X-ray absorptiometry); T-score −1.0 to −2.5 = osteopenia; T-score ≤ −2.5 = osteoporosis
- **Clinical (operational) definition:** Fragility fracture in the absence of an alternative cause (metastatic disease, multiple myeloma, Paget's disease) regardless of T-score

**Epidemiology:**
- **Burden:** Affects ~200 million people worldwide; 1 in 3 women and 1 in 5 men over age 50 will sustain an osteoporotic fracture in their lifetime; 8.9 million fractures per year globally; hip fractures are the most severe (30-40% 1-year mortality in the elderly; 50% never return to pre-fracture ambulatory status)
- **Geography and risk factors:**
  - Peak bone mass achieved at ~25-30 years; determined by genetics (~60-80%), nutrition (calcium, vitamin D), physical activity, and hormonal factors
  - Bone loss begins in the 4th decade; accelerates sharply at menopause (women lose 3-5% trabecular bone/year in first 5-10 years post-menopause)
  - **FRAX (WHO Fracture Risk Assessment Tool):** 10-year probability of major osteoporotic fracture (MOF) — hip, clinical spine, forearm, humerus — from 12 clinical risk factors ± BMD; threshold-based treatment recommendations by country (UK NICE/NOGG, US NOF)

**Risk factors:**
- **Major:** Prior fragility fracture (strongest predictor — 2-3× increased risk for subsequent fracture), family history of hip fracture, glucocorticoid use ≥5 mg prednisolone ≥3 months, early menopause (<45 years), hypogonadism (male), malabsorption (celiac disease, inflammatory bowel disease), low BMI (<20 kg/m²)
- **Modifiable:** Smoking (increases bone resorption, reduces bone formation), alcohol >3 units/day, low calcium/vitamin D intake, physical inactivity, low body weight
- **Secondary causes:** Glucocorticoid-induced osteoporosis (GIO, most common secondary cause), hyperparathyroidism (PTH → RANKL → osteoclast activation), hyperthyroidism (thyroid hormones → accelerated bone turnover), multiple myeloma (RANK-L overproduction by plasma cells → osteolysis), CKD-MBD, rheumatoid arthritis, liver cirrhosis

**Types:**
- **Primary:** Type 1 (postmenopausal — high turnover, trabecular bone predominantly): estrogen deficiency → increased RANKL expression → osteoclast hyperactivation; Type 2 (age-related/senile — both sexes, 70+ years): reduced osteoblast number and function, reduced intestinal calcium absorption, secondary hyperparathyroidism → cortical + trabecular bone loss
- **Secondary:** GIO (glucocorticoids → Wnt inhibition via DKK-1, sclerostin → reduced osteoblast function + increased RANKL → dual anabolic + anti-resorptive impairment)

## Structure

### Bone remodeling — cellular biology of bone loss

**Bone remodeling units (BMUs):**
- Bone is continuously remodeled — ~10% of adult skeleton replaced per year; individual remodeling cycles take ~3-6 months; BMUs consist of osteoclasts and osteoblasts working in sequence on bone surfaces

**Remodeling sequence:**
1. **Activation:** Mechanical strain, microdamage, paracrine signals → osteocyte (mechanosensor, 90% of bone cells, embedded in mineralized matrix) → signaling via RANKL, sclerostin (Wnt inhibitor), DKK-1 → osteoclast precursor recruitment
2. **Resorption (osteoclast phase):** Monocyte-derived osteoclast precursors → RANKL (on osteoblast/stromal cell surface) → RANK (on osteoclast precursor) → TRAF6 → NF-kB, AP-1, NFATc1 → osteoclast differentiation → polarized multinucleated osteoclast → ruffled border → V-ATPase → H⁺ → acidification of resorption lacuna → dissolution of hydroxyapatite → cathepsin K → collagen type I degradation → CTX, NTX release → lacunar pit formation (3-4 weeks)
3. **Reversal phase:** Osteoclast apoptosis; reversal cells (monocytes/macrophages) clean lacunar surface; bone lining cells prepare surface for osteoblast attachment; coupling signals released from bone matrix: TGF-beta, IGF-1, BMP2/4/7 → osteoblast precursor recruitment
4. **Formation (osteoblast phase):** MSC-derived osteoblast precursors → Wnt-beta-catenin signaling → osteoblast differentiation → RUNX2, SP7/Osterix → collagen I synthesis, osteocalcin, bone sialoprotein → osteoid → mineralization (3-4 months) → some osteoblasts become osteocytes (embedded), some become bone lining cells, some undergo apoptosis
5. **Quiescence:** Mineralized bone; osteocytes monitor mechanical loading via lacuno-canalicular network

**RANKL-RANK-OPG axis (master regulator):**
- **RANKL (TNFSF11, expressed by osteoblasts, stromal cells, T cells, osteocytes):** Binds RANK on osteoclast precursors → osteoclast differentiation, activation, and survival
- **OPG (osteoprotegerin, TNFRSF11B, secreted by osteoblasts):** Decoy receptor for RANKL → binds RANKL → blocks RANK binding → inhibits osteoclastogenesis; OPG/RANKL ratio determines bone resorption rate; estrogen → OPG expression → anti-resorptive; estrogen deficiency → reduced OPG → increased RANKL/OPG ratio → osteoclast hyperactivation
- **Denosumab:** Fully human anti-RANKL monoclonal antibody → mimics OPG → blocks RANKL → osteoclast suppression

**Sclerostin-Wnt axis (bone formation master regulator):**
- **Sclerostin (SOST, secreted by osteocytes):** Binds LRP5/6 co-receptors → blocks Wnt-beta-catenin in osteoblasts → inhibits osteoblast differentiation, proliferation, and survival → net anti-anabolic; sclerostin is the brake on bone formation
- Mechanical loading → suppresses sclerostin → Wnt de-repression → bone formation at sites of load; immobilization → sclerostin → bone loss
- **Romosozumab (Evenity):** Anti-sclerostin monoclonal antibody → de-represses Wnt in osteoblasts → increased bone formation + modest anti-resorptive effect (via increased OPG from osteoblasts) → dual anabolic + anti-resorptive; unique mechanism among osteoporosis drugs

## Function

### Clinical presentation and fractures

**Fragility fracture sites (in order of clinical impact):**
- **Hip fracture (femoral neck, intertrochanteric):** Most severe; 30-40% 1-year mortality in elderly; 50% lose prior ambulatory function; ~1.5 million/year globally; requires surgery (hip replacement or ORIF); osteoporosis is the dominant modifiable risk factor
- **Vertebral fractures:** Most common osteoporotic fracture (~700,000/year in US); often asymptomatic ("silent fractures" — only 30% come to clinical attention); progressive vertebral collapse → kyphosis (Dowager's hump), height loss, restrictive lung disease, chronic pain; each vertebral fracture increases risk of subsequent vertebral fracture 5×
- **Distal radius fracture (Colles fracture):** Common in perimenopausal women; fall on outstretched hand; "sentinel fracture" signaling developing osteoporosis; often under-evaluated for bone health
- **Humerus fracture:** Fall on outstretched arm; surgical neck most common; 1-2% of fragility fractures

**Diagnosis:**
- **DXA scan:** Gold standard for BMD; lumbar spine L1-L4 and hip (femoral neck, total hip); peripheral DXA (wrist, calcaneus) less accurate for treatment decisions
- **FRAX:** WHO tool integrating clinical risk factors → 10-year fracture probability; triggers treatment at country-specific intervention thresholds (e.g., US: FRAX ≥20% MOF or ≥3% hip → treatment)
- **Trabecular bone score (TBS):** DXA-derived microarchitectural assessment; adds information beyond T-score alone; useful in secondary osteoporosis (e.g., GIO)
- **Bone turnover markers:** CTX (resorption), P1NP/osteocalcin (formation) → monitor treatment response and adherence; fastest response within 3-6 months of initiating therapy

## Pathology

### Secondary causes — screening

All newly diagnosed osteoporosis should be evaluated for secondary causes: CBC (myeloma, anemia), CMP (calcium, phosphate, renal function, liver function), TSH (hyperthyroidism), serum PTH and calcium (hyperparathyroidism), 25-OH vitamin D (deficiency), celiac antibodies (if indicated), serum/urine protein electrophoresis (myeloma), sex hormones (premature hypogonadism), 24h urine calcium (hypercalciuria — consider thiazide diuretics).

### Treatment [^cosman-2016-romosozumab] [^cummings-2009-denosumab-freedom]

**Non-pharmacological:**
- **Calcium:** 1000-1200 mg/day total (food + supplement); supplements associated with modest GI side effects and possible CV risk (controversial) — prefer dietary sources; dairy, fortified foods, leafy greens
- **Vitamin D:** 800-2000 IU/day to maintain 25-OH-D >30 ng/mL; critical for calcium absorption; cholecalciferol (D3) preferred; deficiency common in elderly, northern latitudes, institutionalized
- **Weight-bearing exercise:** Reduces fall risk, improves balance and muscle mass; resistance training → mechanical loading → sclerostin suppression → bone formation; no direct fracture prevention evidence from exercise RCTs but strong observational data
- **Fall prevention:** Home assessment, PT/balance training, vision correction, medication review (sedatives, antihypertensives → orthostatic hypotension), vitamin D supplementation → reduces fall risk ~20%

**Antiresorptive therapy:**

*Bisphosphonates (first-line):*
- **Alendronate (Fosamax), risedronate (Actonel):** Weekly oral; nitrogen-containing bisphosphonates → farnesyl pyrophosphate synthase inhibition → prenylation failure → osteoclast apoptosis; reduce vertebral fracture ~50%, hip fracture ~40-50%; FIT trial (alendronate: hip fracture RR 0.49); generally well tolerated; GI side effects (esophageal irritation → take upright, 30 min before food); musculoskeletal pain
- **Zoledronic acid (Reclast, Zometa):** IV annually; HORIZON-PFT trial: vertebral fracture RR 0.30, hip RR 0.59, all clinical fracture RR 0.67; also reduces mortality in hip fracture patients; acute phase reaction (flu-like symptoms after first infusion, pretreat with acetaminophen)
- **Adverse effects (rare):** ONJ (osteonecrosis of the jaw) — primarily with high-dose IV bisphosphonates in cancer patients; atypical femur fractures — subtrochanteric or femoral shaft stress fractures with prodromal thigh pain; risk increases with >5-10 years use; drug holiday (2-5 years) after 5 years oral/3 years IV bisphosphonate considered for low-risk patients

*Denosumab (Prolia, 60 mg SC every 6 months):*
- Anti-RANKL monoclonal antibody → osteoclast suppression; FREEDOM trial: vertebral fracture RR 0.32, hip fracture RR 0.60; superior to alendronate in head-to-head (DECIDE trial); can use in CKD (no renal dosing adjustment unlike bisphosphonates); **critical: rebound resorption on discontinuation** → bone loss accelerates and multiple vertebral fractures can occur rapidly if denosumab stopped without transition to bisphosphonate — must transition [^cummings-2009-denosumab-freedom]

*SERMs (selective estrogen receptor modulators):*
- **Raloxifene (Evista):** ER agonist in bone → reduces vertebral fracture ~36% (MORE trial); no hip fracture benefit; reduces invasive breast cancer risk (off-label prevention); increases VTE and hot flashes; NOT for primary hip fracture prevention

**Anabolic therapy (for severe osteoporosis, ≥2 vertebral fractures, or very low T-score):**

*PTH analogues (stimulate osteoblasts):*
- **Teriparatide (Forteo, PTH 1-34):** SC daily × max 2 years; stimulates bone formation > resorption; FPT trial: vertebral fracture RR 0.35, non-vertebral fracture RR 0.47; must transition to antiresorptive after completing course (bone resorbs rapidly without maintenance); risk: osteosarcoma (Sprague-Dawley rats at high doses — black box warning; not confirmed in humans); contraindicated in Paget's disease, prior bone radiation
- **Abaloparatide (Tymlos, PTHrP 1-34):** Similar efficacy and mechanism; ACTIVE trial; slightly different receptor selectivity from teriparatide

*Romosozumab (Evenity, anti-sclerostin):*
- 210 mg SC monthly × 12 months; ARCH trial vs. alendronate: vertebral fracture RR 0.27, hip RR 0.38 vs. alendronate; FRAME trial vs. placebo: vertebral RR 0.27; dual anabolic + anti-resorptive mechanism; **black box warning: possible increased CV risk** (ARCH trial: non-significant increase in MACE vs. alendronate); contraindicated within 12 months of MI or stroke; must transition to antiresorptive after 12 months [^cosman-2016-romosozumab]

**Treatment sequencing:**
- Severe osteoporosis: romosozumab or teriparatide → bisphosphonate or denosumab (anabolic then antiresorptive = anabolic first paradigm → greater BMD gain than antiresorptive first)
- Moderate osteoporosis: bisphosphonate or denosumab first-line
- Denosumab → must transition to bisphosphonate on stopping (rebound fracture risk)

## Connections

- `connects-to` → **[TGF-beta](../../03-molecular/tgf-beta/README.md)** — TGF-beta released from bone matrix during osteoclastic resorption → chemoattractant for osteoblast precursors → bone formation coupling signal; excess TGF-beta (PTH-driven or tumor-derived) → uncoupled osteoclast activation → metastasis-associated bone destruction.
- `connects-to` → **[IL-6](../../03-molecular/il-6/README.md)** — IL-6 drives RANKL-independent osteoclastogenesis via JAK-STAT3 → osteoclast precursor differentiation; elevated IL-6 in postmenopausal women, RA, and multiple myeloma → accelerated bone loss; tocilizumab reduces bone erosion in RA as a secondary bone-protective effect.
- `connects-to` → **[Collagen](../../03-molecular/collagen/README.md)** — Collagen type I is the dominant organic bone matrix component; osteoblasts synthesize type I collagen → osteoid → mineralization; osteoclastic resorption → CTX and NTX (type I collagen telopeptides) → serum biomarkers of bone resorption used to monitor osteoporosis therapy.
- `connects-to` → **[Osteoclast](../../04-cellular/osteoclast/README.md)** — Osteoclasts are the primary drivers of bone loss: RANKL → RANK on osteoclast precursors → differentiation and lacunar resorption → BMD loss; denosumab (anti-RANKL) neutralizes RANKL → osteoclast suppression → fracture risk reduction 40-60%.
- `connects-to` → **[FGF23](../../03-molecular/fgf23/README.md)** — FGF23 inhibits 1α-hydroxylase → reduces calcitriol → decreases intestinal calcium absorption → bone demineralization; genetic FGF23 excess (XLH, ARHR) causes hypophosphatemic rickets; burosumab (anti-FGF23 mAb) corrects hypophosphatemia and heals rickets in XLH.
- `connects-to` → **[PTH](../../03-molecular/pth/README.md)** — Continuous PTH → RANKL → osteoclast activation and bone resorption; intermittent PTH 1-34 (teriparatide, SC daily) preferentially activates Wnt signaling in osteoblasts → net anabolic effect; FPT trial: 65% RRR for vertebral fractures; PTH 1-84 treats hypoparathyroidism.
- `connects-to` → **[Calcitonin](../../03-molecular/calcitonin/README.md)** — calcitonin inhibits osteoclast activity → CTR → cAMP → cytoskeletal collapse and loss of ruffled border → reduced bone resorption; intranasal salmon calcitonin (200 IU/day) reduces vertebral fractures 36% (PROOF trial) but is less effective than bisphosphonates; now reserved for acute pain of recent vertebral fracture.
- `connects-to` → **[RANKL](../../03-molecular/rankl/README.md)** — RANKL (TNFSF11) from osteoblasts/T cells → RANK on osteoclast precursors → TRAF6 → NF-κB → NFATc1 → osteoclast differentiation; OPG decoy ratio governs bone mass; denosumab (anti-RANKL) → 68% vertebral and 40% hip fracture risk reduction (FREEDOM trial).
- `connects-to` → **[Sclerostin](../../03-molecular/sclerostin/README.md)** — Sclerostin (SOST) from osteocytes → LRP5/6 Wnt antagonism → osteoblast suppression → net bone loss; mechanical loading suppresses sclerostin → anabolic response; romosozumab (anti-sclerostin) → +13% lumbar spine BMD at 12 months; 73% vertebral fracture RRR (FRAME).
- `connects-to` → **[Testosterone](../../03-molecular/testosterone/README.md)** — Male hypogonadism (T <300 ng/dL) is a leading cause of secondary male osteoporosis; testosterone maintains BMD via AR on osteoblasts and aromatization to estradiol; ADT causes 2-5% BMD loss/year; denosumab or zoledronate co-administered with ADT prevents fractures.
- `connects-to` → **[Estrogen](../../03-molecular/estrogen/README.md)** — Estrogen deficiency at menopause → reduced OPG → RANKL excess → osteoclast hyperactivation → 3-5% trabecular bone loss/year; HRT reduces fracture risk ~35%; SERMs (raloxifene) preserve bone without uterine stimulation; bisphosphonates preferred over HRT for fracture prevention.
- `connects-to` → **[Thyroid Hormones](../../03-molecular/thyroid-hormones/README.md)** — Hyperthyroidism accelerates bone remodeling → 10-20% BMD loss at trabecular sites; TSH receptors on osteoblasts exert bone-protective effects; Graves disease → osteoporosis risk; anti-thyroid treatment normalizes bone loss; bisphosphonates co-administered when BMD is low.
- `connects-to` → **[Osteoblast](../../04-cellular/osteoblast/README.md)** — Osteoporosis is a failure of the osteoblast-osteoclast balance: bone-resorbing osteoclasts outpace bone-forming osteoblasts (estrogen loss, aging, steroids), so bone mass and microarchitecture deteriorate—anabolic drugs reverse it by favoring osteoblasts.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — Osteoporosis is the commonest disease of the aging musculoskeletal system: silent bone loss until a fragility fracture (hip, vertebra, wrist) reveals it, and because fractures cause disability and death, bone-density screening and antiresorptives are core to skeletal health.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — Menopause is the leading cause of osteoporosis: the sharp fall in ovarian estrogen accelerates osteoclast-driven bone resorption, so women lose bone rapidly after menopause—linking the reproductive system's hormonal shift to skeletal fragility and fracture risk.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Calcium is the mineral osteoporosis depletes: bone is the body's calcium reservoir, and when intake or absorption falls, parathyroid hormone pulls calcium from bone to keep blood levels constant—so chronic deficiency drives the net bone loss that weakens the skeleton.
- `connects-to` → **[Vitamin D (Calciferol)](../../../03-medicine/03-food/vitamin-d/README.md)** — Vitamin D is essential to prevent osteoporosis: it drives intestinal calcium absorption, so deficiency causes secondary hyperparathyroidism that strips bone, and adequate vitamin D plus calcium is the foundation on which osteoporosis drug therapy is built.
- `connects-to` → **[Cortisol](../../03-molecular/cortisol/README.md)** — Cortisol excess is a major cause of osteoporosis: glucocorticoids suppress osteoblasts, promote osteoclast survival and reduce calcium absorption, so both Cushing's syndrome and long-term steroid therapy cause rapid bone loss—the most common drug-induced osteoporosis.
- `connects-to` → **[Bone Marrow](../../05-tissue/bone-marrow/README.md)** — Bone is remodeled in concert with the marrow it houses: osteoporosis reflects an imbalance between osteoclasts and osteoblasts at the bone-marrow interface, and with age red marrow gives way to fat as bone is lost—linking declining marrow and skeletal mass.
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — Magnesium is an underappreciated factor in bone health: about half the body's magnesium sits in bone, and it is needed for vitamin D activation and PTH secretion, so chronic magnesium deficiency impairs mineralization and contributes to osteoporosis.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — Osteoporosis is largely an endocrine disease: estrogen, testosterone, thyroid hormone, parathyroid hormone and cortisol all govern bone turnover, so hormonal shifts (menopause, hyperthyroidism, steroid excess) are leading causes of bone loss.
- `connects-to` → **[Phosphorus](../../02-atomic/phosphorus/README.md)** — Bone is calcium-phosphate crystal, so phosphorus is as structural as calcium: hydroxyapatite needs balanced phosphate, and disordered phosphate handling—too little (osteomalacia) or the excess of kidney disease—weakens or distorts bone alongside calcium loss.
- `connects-to` → **[Rheumatoid Arthritis](../rheumatoid-arthritis/README.md)** — Rheumatoid arthritis is a double hit to bone: chronic inflammation (and RANKL) accelerates bone loss, and the glucocorticoids used to treat it cause steroid-induced osteoporosis—so inflammatory arthritis is a leading secondary cause of fragile bones.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — Healthy bone depends on the gut: the intestine absorbs the calcium and vitamin D bone needs, so malabsorption from celiac disease, inflammatory bowel disease, or bariatric surgery is an under-recognized cause of osteoporosis.
- `connects-to` → **[Adipocyte](../../04-cellular/adipocyte/README.md)** — Bone loss in aging tips marrow toward fat: the mesenchymal stem cells that should become bone-building osteoblasts instead become adipocytes, so marrow fills with fat as bone thins—linking the adipocyte-osteoblast balance to osteoporosis.
- `connects-to` → **[Multiple Myeloma](../multiple-myeloma/README.md)** — Multiple myeloma masquerades as severe osteoporosis: malignant plasma cells activate osteoclasts (via RANKL) to carve lytic lesions and cause fractures, so unexplained bone loss with anemia or high calcium prompts a myeloma workup.
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — Failing kidneys weaken bone—renal osteodystrophy: CKD disturbs phosphate, vitamin D and PTH, deranging bone turnover into a complex osteoporosis-plus-osteomalacia that standard bone drugs can worsen, so diagnosis must come first.

[^kanis-2019-who-osteoporosis]: Kanis JA, Cooper C, Rizzoli R, Reginster JY. European guidance for the diagnosis and management of osteoporosis in postmenopausal women. *Osteoporos Int.* 2019;30(1):3-44. [doi:10.1007/s00198-018-4704-5](https://doi.org/10.1007/s00198-018-4704-5) · [PubMed 30324412](https://pubmed.ncbi.nlm.nih.gov/30324412/)
[^cosman-2016-romosozumab]: Cosman F, Crittenden DB, Adachi JD, et al. Romosozumab treatment in postmenopausal women with osteoporosis. *N Engl J Med.* 2016;375(16):1532-1543. [doi:10.1056/NEJMoa1607948](https://doi.org/10.1056/NEJMoa1607948) · [PubMed 27641143](https://pubmed.ncbi.nlm.nih.gov/27641143/)
[^cummings-2009-denosumab-freedom]: Cummings SR, San Martin J, McClung MR, et al. Denosumab for prevention of fractures in postmenopausal women with osteoporosis. *N Engl J Med.* 2009;361(8):756-765. [doi:10.1056/NEJMoa0809493](https://doi.org/10.1056/NEJMoa0809493) · [PubMed 19671655](https://pubmed.ncbi.nlm.nih.gov/19671655/)
