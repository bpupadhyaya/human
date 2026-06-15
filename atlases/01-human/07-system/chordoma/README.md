---
schema: human-scale-entry/v1
id: chordoma
name: Chordoma
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-06
summary: "Chordoma arises from notochordal remnants; skull base (~35%), sacrococcygeal (~50%), mobile spine (~15%); TBXT overexpression in >95%; physaliferous cell histology; proton RT + surgery standard; no FDA-approved systemic agent; imatinib, sorafenib, mTOR inhibitors active."
aliases: ["chordoma", "skull base chordoma", "sacral chordoma", "clival chordoma", "spinal chordoma", "brachyury chordoma", "notochordal tumor", "chordoma TBXT", "physaliferous cell tumor", "chordoma dedifferentiated"]
sources:
  - id: stacchiotti-2012-imatinib-chordoma
    type: peer-reviewed
    cite: "Stacchiotti S, Longhi A, Ferraresi V, et al. Phase II study of imatinib in advanced chordoma. J Clin Oncol. 2012;30(9):914-920."
    doi: "10.1200/JCO.2011.35.3656"
    pmid: "22330157"
    url: "https://doi.org/10.1200/JCO.2011.35.3656"
  - id: yang-2009-tbxt-chordoma
    type: peer-reviewed
    cite: "Yang XR, Ng D, Alcorta DA, et al. T (brachyury) gene duplication confers major susceptibility to familial chordoma. Nat Genet. 2009;41(11):1176-1178."
    doi: "10.1038/ng.454"
    pmid: "19801977"
    url: "https://doi.org/10.1038/ng.454"
cross_links:
  - target: 01-human/03-molecular/tbxt
    relation: connects-to
    note: "TBXT (brachyury) overexpression in >95% chordomas defines lineage identity; tandem TBXT duplication at 6q27 → familial chordoma; TBXT FISH or IHC (strong nuclear brachyury) is the diagnostic confirmatory test; TBXT knockdown → chordoma cell growth arrest and apoptosis in vitro."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "PTEN loss in ~15-20% chordomas → AKT/mTOR hyperactivation; mTOR pathway activated downstream of FGFR/PDGFR in chordoma; everolimus achieves stable disease in ~50% (Schwab 2015, Phase 2); mTOR + FGFR combinations under investigation; lapatinib + everolimus Phase 2 showed activity."
  - target: 01-human/03-molecular/fgfr
    relation: connects-to
    note: "FGFR1/2/3 overexpressed in ~50% chordomas; FGFR-driven MAPK/PI3K → tumor growth; erdafitinib (pan-FGFR) active in FGFR-altered chordoma (Phase 2); FGF4/FGF8 autocrine loop driven by TBXT transcription; FGFR inhibitors synergize with mTOR inhibitors in preclinical models."
  - target: 01-human/03-molecular/pdgf
    relation: connects-to
    note: "PDGFRA/PDGFRB overexpressed in >80% chordomas; imatinib (PDGFR inhibitor) achieves stable disease in ~35-40% (Stacchiotti 2012, Phase 2); PDGF-BB autocrine loop in chordoma cells; erlotinib + imatinib combination achieves partial response in small Phase 2 series."
  - target: 01-human/03-molecular/pten
    relation: connects-to
    note: "PTEN loss in ~15-20% chordomas → AKT-mTOR hyperactivation + increased VEGF; PI3K inhibitors studied in PTEN-deficient chordoma; PTEN co-deletion with CDKN2A in ~8-10% → simultaneous CDK4/6 and mTOR hyperactivation; PTEN loss correlates with worse prognosis in chordoma."
  - target: 01-human/03-molecular/cdk4-6
    relation: connects-to
    note: "CDKN2A deletion in ~30-40% of chordomas → CDK4/6 hyperactivation → RB1 phosphorylation → S-phase entry; palbociclib Phase 2 (NCT03110744) in CDKN2A-deleted chordoma; dedifferentiated chordoma shows CDK4 amplification and MDM2 co-amplification as hallmarks."
  - target: 01-human/03-molecular/cdkn2a
    relation: connects-to
    note: "CDKN2A homozygous deletion in ~30-40% chordomas; eliminates both p16 (CDK4/6 checkpoint) and ARF (p53 stabilization); deletion at 9p21 is among the earliest molecular events in chordoma progression; CDKN2A loss correlates with worse prognosis and dedifferentiated transformation."
  - target: 01-human/07-system/ewing-sarcoma
    relation: connects-to
    note: "Chordoma and Ewing sarcoma are both rare bone tumors with one defining genetic lesion — chordoma's TBXT/brachyury overexpression versus Ewing's EWSR1-FLI1 fusion — but chordoma is a slow midline tumor of adults from notochord remnants, Ewing a small-cell tumor of children."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "Chordoma arises along the axial skeleton from embryonic notochord remnants — ~50% sacrum, ~35% skull base (clivus), the rest mobile spine; this midline bony location, often diagnosed late and abutting critical structures, makes en-bloc resection the mainstay yet often incomplete."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "Skull-base (clival) chordomas grow against the brainstem, cavernous sinus, and cranial nerves, causing diplopia, headache, and cranial-nerve palsies; their proximity to brain and vessels limits margins, making proton-beam radiotherapy central to controlling residual tumor."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Chordoma is defined by its radiotherapy needs: nestled against the brainstem and cord at the skull base and sacrum, it needs very high radiation doses that proton-beam therapy delivers while sparing neural tissue—central since complete resection is often impossible."
  - target: 01-human/07-system/osteosarcoma
    relation: connects-to
    note: "Chordoma and osteosarcoma are both primary bone malignancies but differ fundamentally: chordoma is a slow-growing notochord-remnant tumor of the axial skeleton (skull base/sacrum) driven by brachyury, while osteosarcoma is an aggressive osteoid-producing tumor of long bones."
  - target: 01-human/04-cellular/osteoblast
    relation: connects-to
    note: "Chordoma's relationship to bone-forming cells is distinctive: although it grows within and destroys bone, it does not arise from osteoblasts but from notochord remnants, producing a lytic, gelatinous mass rather than the bone matrix osteoblasts lay down—imaging shows destruction."
  - target: 01-human/07-system/meningioma
    relation: connects-to
    note: "Chordoma and meningioma are both slow-growing skull-base/spinal tumors in the same differential: chordoma is a destructive midline tumor of notochord remnants, while meningioma is a dural-based extra-axial tumor—told apart by location, imaging, and immunostains."
  - target: 01-human/04-cellular/fibroblast
    relation: connects-to
    note: "Chordoma's characteristic histology is a myxoid, fibroblast-like stroma studded with physaliphorous (bubbly) cells: the matrix and spindle-cell background give a deceptively bland, cartilage-like look, so brachyury immunostaining confirms its notochordal origin."
  - target: 01-human/07-system/synovial-sarcoma
    relation: connects-to
    note: "Chordoma and synovial sarcoma are rare tumors of young adults with aggressive local behavior needing wide resection plus radiotherapy: chordoma is brachyury-driven from notochord remnants, synovial sarcoma SS18-SSX-fusion-driven—different drivers, similar challenge."
  - target: 01-human/03-molecular/egfr
    relation: connects-to
    note: "EGFR is a therapeutic target in chordoma: these slow-growing notochordal tumors often activate EGFR signaling, so EGFR inhibitors like erlotinib are used off-label in advanced disease where surgery and radiation fail—chordoma resists conventional chemotherapy."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "Chordoma threatens neurons by location: arising along the spine and skull base from notochord remnants, it compresses the brainstem, spinal cord and cranial nerves, so neurological deficits—not metastasis—drive its morbidity despite slow growth."
  - target: 01-human/03-molecular/collagen
    relation: connects-to
    note: "Chordoma's hallmark cells sit in a collagen-rich matrix: physaliphorous bubble cells float in a myxoid, collagenous stroma recapitulating the notochord, giving the tumor its distinctive histology that, with brachyury staining, confirms the diagnosis."
  - target: 01-human/01-subatomic/proton
    relation: connects-to
    note: "Proton therapy is the radiation mainstay for chordoma: these radioresistant skull-base and sacral tumors sit against the brainstem and spinal cord, so protons' sharp dose falloff delivers high tumor dose while sparing critical neural structures."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "Chordoma threatens the nervous system by location: arising along the spine and skull base from notochord remnants, it compresses the brainstem, cranial nerves and spinal cord, so its slow growth still causes severe neurological deficits and demands aggressive local control."
  - target: 01-human/02-atomic/carbon
    relation: connects-to
    note: "Carbon-ion radiotherapy is an alternative for chordoma: heavy carbon ions deliver dense, highly damaging dose to these notoriously radioresistant tumors, useful when surgery is incomplete or the tumor abuts neural structures—an option in specialized particle centers."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "Chordoma spreads most often to the lung: though it grows slowly and locally along the spine and skull base, late metastasis favors the lungs, so chest imaging is part of follow-up for this notochord-derived bone tumor."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "Chordoma is a target for vaccine immunotherapy: nearly all chordomas express brachyury (TBXT), and a brachyury-directed cancer vaccine trains the immune system against this otherwise hard-to-drug developmental transcription factor."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "Chordoma's radioresistance is partly an oxygen problem: poorly oxygenated tumor regions resist conventional X-rays, so high-dose proton and carbon-ion radiotherapy—less dependent on oxygen and more precise near the spinal cord—are used instead."
  - target: 01-human/04-cellular/osteoclast
    relation: connects-to
    note: "Chordoma destroys bone through osteoclasts: as it grows in the skull base or sacrum it recruits bone-resorbing osteoclasts that erode the surrounding skeleton, so anti-resorptive drugs are explored to slow the local destruction this hard-to-resect tumor causes."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "Chordoma is a vascular tumor that responds to anti-VEGF therapy: it expresses VEGF to grow blood vessels, which is why multi-target TKIs that block VEGF receptors (like sunitinib) can stall this otherwise treatment-resistant cancer."
  - target: 01-human/03-molecular/p53
    relation: connects-to
    note: "Losing p53 makes chordoma more aggressive: while most chordomas grow slowly on brachyury, TP53 mutation marks the dangerous shift toward dedifferentiated, fast-growing tumors with a far worse prognosis."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "Chordoma leans on the PI3K-AKT-mTOR growth axis: AKT signaling is frequently active and, with PTEN loss, drives proliferation in these brachyury-dependent tumors, so AKT-mTOR inhibitors are studied for a cancer resistant to chemotherapy."
  - target: 01-human/03-molecular/met
    relation: connects-to
    note: "MET signaling can drive aggressive chordoma: amplification or activation of this receptor promotes invasion and growth, adding to the brachyury-driven biology and offering another targetable kinase in a notoriously treatment-resistant bone tumor."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Chordoma is a target for T-cell immunotherapy against brachyury: because the tumor depends on this lineage antigen, vaccines and engineered cytotoxic T cells aim to direct a killing response at a protein cancer cells cannot easily discard."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Chordoma eats away calcium-rich bone: arising in the skull base and sacrum, it destroys the bony matrix as it grows, dissolving the calcium scaffold and threatening the spine and cranial nerves it surrounds."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Chordoma shelters in a macrophage-rich stroma: tumor-associated macrophages populate its microenvironment and dampen immunity, part of why this slow but stubborn tumor resists treatment and recurs."
  - target: 01-human/06-organ/large-intestine
    relation: connects-to
    note: "Sacral chordoma presses on the bowel: the most common chordoma site sits against the rectum and pelvic nerves, so large tumors cause constipation, bowel and bladder dysfunction, and low back pain."
  - target: 01-human/05-tissue/peripheral-nerve
    relation: connects-to
    note: "Chordoma grows against the nerves: skull-base and sacral tumors compress cranial nerves and the cauda equina, causing the neuropathic pain, weakness and bowel-bladder dysfunction that often first signal it."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "Chordoma metastasizes late: though slow-growing and locally destructive, it can seed the lungs, liver and bone over years, especially after repeated local recurrences."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "Chordoma builds its own vasculature: VEGF recruits endothelial cells to feed the tumor, and anti-angiogenic drugs are among the systemic options for this radiation- and surgery-dependent cancer."
---

# Chordoma

## Overview

**Chordoma** is a rare, locally aggressive, low-to-intermediate grade malignant tumor arising from notochordal remnants that persist in the axial skeleton. Despite a typically slow growth rate, chordoma is associated with high rates of local recurrence, late metastases, and significant morbidity from its location adjacent to critical neural structures. TBXT (brachyury), expressed in >95% of chordomas, defines tumor identity and is the diagnostic hallmark [^yang-2009-tbxt-chordoma].

**Epidemiology:**
- Incidence: ~1-2 per million/year; ~300-400 cases/year USA; one of the rarest primary bone tumors
- Peak age: 50-60 years (skull base ~40-50 years; sacral ~55-65 years); male predominance ~1.8:1
- Median OS: skull base ~10-14 years; sacral ~7-10 years; mobile spine ~6-8 years
- Metastases at diagnosis: ~5-10%; eventual metastases in ~30-40% of patients over the disease course; lung (most common), bone, lymph node, liver

**Sites and locations:**

| Location | Frequency | Key features |
|---|---|---|
| Sacrococcygeal | ~50% | Largest at presentation (often >10 cm); late symptoms; S3/S4 roots → bowel/bladder; en bloc sacrectomy |
| Skull base (clivus) | ~35% | Cranial nerve palsies (VI most common); encases basilar artery; radical resection difficult; endoscopic endonasal approach |
| Mobile spine (C/T/L) | ~15% | Cervical > lumbar; cord compression; multilevel resection; highest local recurrence |

**Familial chordoma:** ~5% of patients have a family history; tandem germline TBXT duplication at 6q27 is the most common predisposing variant [^yang-2009-tbxt-chordoma]; other predisposing conditions include tuberous sclerosis complex (TSC1/TSC2 germline) and rarely NF2 syndrome

## Structure

### Histological subtypes

**Conventional (classic) chordoma (~85%):**
- **Physaliferous cells** ("bubble-bearing" cells): large vacuolated cells with intracytoplasmic mucin inclusions pushing the nucleus to one side; cytoplasm has "soap bubble" appearance on H&E
- Mucoid/myxoid stroma (chondromucin)
- Lobular architecture separated by fibrous septa
- Low mitotic rate (<2/10 HPF); necrosis absent in most cases

**Chondroid chordoma (~5-10%):**
- Mixed chordoma + hyaline cartilage; predominantly skull base
- Better prognosis than conventional; lower rate of metastasis
- Must be distinguished from chondrosarcoma (chondrosarcoma is TBXT-negative)

**Dedifferentiated chordoma (~5%):**
- Biphasic: classic chordoma + high-grade sarcomatous component
- Abrupt junction between components
- CDK4 amplification, MDM2 amplification common in dedifferentiated component
- 5-year OS ~10-15%; aggressive systemic metastases; worst prognosis variant

**Poorly differentiated chordoma:**
- SMARCB1/INI1 loss in ~75% (biallelic loss, distinct from conventional); primarily pediatric; skull base; rhabdoid morphology; treated similarly to AT/RT

### IHC panel

- **TBXT (brachyury)**: strong nuclear positivity — pathognomonic; ~95-100% of conventional chordoma; negative in chondrosarcoma, meningeal tumors, and carcinoma
- **S100**: positive in ~95% of chordoma; nuclear and cytoplasmic
- **Cytokeratin (AE1/AE3, CAM5.2)**: positive in ~85%; differentiates from chondrosarcoma (CK-negative)
- **EMA**: positive in ~60-70%
- **GFAP**: positive in ~25-35%; notochordal origin
- **SOX9**: positive in most chordomas
- **SMARCB1/INI1**: intact in conventional; LOST in poorly differentiated chordoma variant

## Function

### Notochordal biology and chordoma origin

The notochord is a transient axial structure in all chordate embryos; in humans:
- Forms during gastrulation (week 3); provides mechanical support and signaling
- Regresses completely by week 8-12 as vertebral bodies form
- Notochordal remnants (benign notochordal cell tumors, BNCTs) persist in nucleus pulposus (intervertebral discs) and occasionally in vertebral bodies (ecchordosis physaliphora)
- BNCT: asymptomatic incidental finding; TBXT-positive but no somatic mutations or atypia; may be the precursor lesion for chordoma

**Chordoma oncogenesis:** TBXT-overexpressing notochordal cells escape senescence (via CDK4/cyclin D1, anti-apoptotic BCL-2) → acquire somatic mutations in CDKN2A (~30-40% deletion), PIK3CA, TP53, PTEN, ATRX → invasive chordoma; the transformation from BNCT to chordoma may take decades

**Typical somatic alterations in chordoma:**
- CDKN2A homozygous deletion: ~30-40%; worst prognosis; CDK4/6 hyperactivation
- PIK3CA mutations: ~15-20%; mTOR pathway activation
- PTEN loss: ~15%; AKT/mTOR
- ATRX mutations: ~15%; alternative lengthening of telomeres
- TP53 mutations: ~5-10%; usually late event
- LYST, SETD2, BRCA2: rare; identified in chordoma genome sequencing
- Chromosome arm losses: 1p, 3p, 4, 9p (CDKN2A), 10 (PTEN), 13q (RB1) common

## Pathology

### Surgical management

**Skull base chordoma:**
- Endoscopic endonasal approach (EEA): minimally invasive, direct clival access; standard for midline/paramedian clivus lesions; combined with neurosurgery team
- Craniotomy: lateral tumors, extensive lateral extension, cavernous sinus involvement
- Extent of resection: GTR correlated with better PFS (5-year local control ~60-70% with GTR + proton)
- Critical structures: basilar artery, CN VI (most commonly affected), CN III, carotid siphon, brainstem; incomplete resection for safety → adjuvant proton beam

**Sacral chordoma:**
- En bloc resection: wide margins essential; preserve S1-S2 (bilateral) for ambulatory function and S2-S3 (bilateral) for bladder/bowel continence; sacrifice below S3 acceptable with continent function
- High sacral (S1-S2) tumors: combined anterior (laparoscopic) + posterior approach; major morbidity
- Recurrence rate: ~50-60% at 5 years even after R0 resection; proton boost reduces recurrence
- Lumbopelvic stability: instrumented fusion required if sacroiliac joint disrupted

**Mobile spine chordoma:**
- Cervical: highest rate of incomplete resection due to vertebral artery, esophagus, trachea
- Thoracic/lumbar: en bloc spondylectomy (total vertebrectomy) with reconstruction; spinal cord monitoring
- Circumferential resection: requires anterior + posterior staged approach or single-stage

### Radiation therapy

**Proton beam radiotherapy (PBRT) / Carbon ion radiotherapy (CIRT):**
- Superior to photon RT due to sharp Bragg peak → maximal dose at tumor with minimal exit dose
- Skull base standard: 74-78 Gy (RBE) in 35-40 fractions; local control at 5 years: ~70-75%
- Sacral: 70-77.4 Gy (RBE) combined with surgery; local control 5-year: ~55-65%
- CIRT (carbon ion): available in Japan and Germany; superior biological effectiveness → may achieve ~80% local control in skull base; head-to-head vs proton ongoing

### Systemic therapy (no FDA-approved agent exists)

**Imatinib (PDGFR/KIT/ABL inhibitor):** [^stacchiotti-2012-imatinib-chordoma]
Phase 2 (Stacchiotti 2012, N=50): ORR 0% (partial response in 0), stable disease 70% (35/50); median PFS 9.9 months; PDGFRA/B expression predicts stable disease; used as standard-of-care systemic option for progressive chordoma despite no objective responses

**Sorafenib (multikinase: VEGFR/PDGFR/BRAF/RAF):**
Phase 2 (Bompas 2015, N=27): ORR 7% (2/27 PR), SD 70%; PFS 5.8 months; modest activity; toxicity includes hand-foot syndrome

**Erlotinib + imatinib:**
Phase 2 (Stacchiotti 2013): ORR 10% (PR); combination tolerated; activity mainly stable disease; EGFR overexpressed in ~75% of chordoma cells

**mTOR inhibitors (everolimus, rapamycin):**
Rationale: PTEN loss/PI3K/AKT hyperactivation → mTOR; everolimus Phase 2 (Schwab 2015): SD in ~50%, no objective responses; lapatinib + everolimus Phase 2: similar results; rapamycin retrospective series: SD in recurrent disease; combination with FGFR inhibitors preferred investigational approach

**Pembrolizumab/nivolumab:**
Low TMB (~1-2 mut/Mb); PD-L1 expressed in ~20-30%; anti-PD-1 ORR ~10-15% in case series; chordoma TME is immune-cold; combination with radiation (immune priming) under investigation

**Palbociclib (CDK4/6 inhibitor):**
CDKN2A deletion in ~30-40% → CDK4/6 hyperactivation → RB1 phosphorylation; palbociclib Phase 2 in CDKN2A-deleted chordoma (NCT03110744): ongoing; rationale strong for CDK4/6-deleted subset

**Prognosis:**
- 5-year OS: skull base ~70-80%; sacral ~65-75%; mobile spine ~55-65%; dedifferentiated ~10-15%
- 10-year OS: skull base ~45-60%; sacral ~40-55%
- Local recurrence: major cause of morbidity and mortality; most patients undergo multiple surgeries
- Late metastases (>5 years from diagnosis): ~25-30%; lung most common; may respond temporarily to imatinib or sorafenib

## Connections

- `connects-to` → **[TBXT](../../03-molecular/tbxt/README.md)** — TBXT (brachyury) overexpression in >95% chordomas defines lineage identity; tandem TBXT duplication at 6q27 → familial chordoma; TBXT FISH or IHC (strong nuclear brachyury) is the diagnostic confirmatory test; TBXT knockdown → chordoma cell growth arrest and apoptosis in vitro.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — PTEN loss in ~15-20% chordomas → AKT/mTOR hyperactivation; mTOR pathway activated downstream of FGFR/PDGFR in chordoma; everolimus achieves stable disease in ~50% (Schwab 2015, Phase 2); mTOR + FGFR combinations under investigation; lapatinib + everolimus Phase 2 showed activity.
- `connects-to` → **[FGFR](../../03-molecular/fgfr/README.md)** — FGFR1/2/3 overexpressed in ~50% chordomas; FGFR-driven MAPK/PI3K → tumor growth; erdafitinib (pan-FGFR) active in FGFR-altered chordoma (Phase 2); FGF4/FGF8 autocrine loop driven by TBXT transcription; FGFR inhibitors synergize with mTOR inhibitors in preclinical models.
- `connects-to` → **[PDGF](../../03-molecular/pdgf/README.md)** — PDGFRA/PDGFRB overexpressed in >80% chordomas; imatinib (PDGFR inhibitor) achieves stable disease in ~35-40% (Stacchiotti 2012, Phase 2); PDGF-BB autocrine loop in chordoma cells; erlotinib + imatinib combination achieves partial response in small Phase 2 series.
- `connects-to` → **[PTEN](../../03-molecular/pten/README.md)** — PTEN loss in ~15-20% chordomas → AKT-mTOR hyperactivation + increased VEGF; PI3K inhibitors studied in PTEN-deficient chordoma; PTEN co-deletion with CDKN2A in ~8-10% → simultaneous CDK4/6 and mTOR hyperactivation; PTEN loss correlates with worse prognosis in chordoma.
- `connects-to` → **[CDK4/6](../../03-molecular/cdk4-6/README.md)** — CDKN2A deletion in ~30-40% of chordomas → CDK4/6 hyperactivation → RB1 phosphorylation → S-phase entry; palbociclib Phase 2 (NCT03110744) in CDKN2A-deleted chordoma; dedifferentiated chordoma shows CDK4 amplification and MDM2 co-amplification as hallmarks.
- `connects-to` → **[CDKN2A](../../03-molecular/cdkn2a/README.md)** — CDKN2A homozygous deletion in ~30-40% chordomas; eliminates both p16 (CDK4/6 checkpoint) and ARF (p53 stabilization); deletion at 9p21 is among the earliest molecular events in chordoma progression; CDKN2A loss correlates with worse prognosis and dedifferentiated transformation.
- `connects-to` → **[Ewing Sarcoma](../ewing-sarcoma/README.md)** — Chordoma and Ewing sarcoma are both rare bone tumors with one defining genetic lesion — chordoma's TBXT/brachyury overexpression versus Ewing's EWSR1-FLI1 fusion — but chordoma is a slow midline tumor of adults from notochord remnants, Ewing a small-cell tumor of children.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — Chordoma arises along the axial skeleton from embryonic notochord remnants — ~50% sacrum, ~35% skull base (clivus), the rest mobile spine; this midline bony location, often diagnosed late and abutting critical structures, makes en-bloc resection the mainstay yet often incomplete.
- `connects-to` → **[Brain](../../06-organ/brain/README.md)** — Skull-base (clival) chordomas grow against the brainstem, cavernous sinus, and cranial nerves, causing diplopia, headache, and cranial-nerve palsies; their proximity to brain and vessels limits margins, making proton-beam radiotherapy central to controlling residual tumor.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Chordoma is defined by its radiotherapy needs: nestled against the brainstem and cord at the skull base and sacrum, it needs very high radiation doses that proton-beam therapy delivers while sparing neural tissue—central since complete resection is often impossible.
- `connects-to` → **[Osteosarcoma](../osteosarcoma/README.md)** — Chordoma and osteosarcoma are both primary bone malignancies but differ fundamentally: chordoma is a slow-growing notochord-remnant tumor of the axial skeleton (skull base/sacrum) driven by brachyury, while osteosarcoma is an aggressive osteoid-producing tumor of long bones.
- `connects-to` → **[Osteoblast](../../04-cellular/osteoblast/README.md)** — Chordoma's relationship to bone-forming cells is distinctive: although it grows within and destroys bone, it does not arise from osteoblasts but from notochord remnants, producing a lytic, gelatinous mass rather than the bone matrix osteoblasts lay down—imaging shows destruction.
- `connects-to` → **[Meningioma](../meningioma/README.md)** — Chordoma and meningioma are both slow-growing skull-base/spinal tumors in the same differential: chordoma is a destructive midline tumor of notochord remnants, while meningioma is a dural-based extra-axial tumor—told apart by location, imaging, and immunostains.
- `connects-to` → **[Fibroblast](../../04-cellular/fibroblast/README.md)** — Chordoma's characteristic histology is a myxoid, fibroblast-like stroma studded with physaliphorous (bubbly) cells: the matrix and spindle-cell background give a deceptively bland, cartilage-like look, so brachyury immunostaining confirms its notochordal origin.
- `connects-to` → **[Synovial Sarcoma](../synovial-sarcoma/README.md)** — Chordoma and synovial sarcoma are rare tumors of young adults with aggressive local behavior needing wide resection plus radiotherapy: chordoma is brachyury-driven from notochord remnants, synovial sarcoma SS18-SSX-fusion-driven—different drivers, similar challenge.
- `connects-to` → **[EGFR](../../03-molecular/egfr/README.md)** — EGFR is a therapeutic target in chordoma: these slow-growing notochordal tumors often activate EGFR signaling, so EGFR inhibitors like erlotinib are used off-label in advanced disease where surgery and radiation fail—chordoma resists conventional chemotherapy.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — Chordoma threatens neurons by location: arising along the spine and skull base from notochord remnants, it compresses the brainstem, spinal cord and cranial nerves, so neurological deficits—not metastasis—drive its morbidity despite slow growth.
- `connects-to` → **[Collagen](../../03-molecular/collagen/README.md)** — Chordoma's hallmark cells sit in a collagen-rich matrix: physaliphorous bubble cells float in a myxoid, collagenous stroma recapitulating the notochord, giving the tumor its distinctive histology that, with brachyury staining, confirms the diagnosis.
- `connects-to` → **[Proton](../../01-subatomic/proton/README.md)** — Proton therapy is the radiation mainstay for chordoma: these radioresistant skull-base and sacral tumors sit against the brainstem and spinal cord, so protons' sharp dose falloff delivers high tumor dose while sparing critical neural structures.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — Chordoma threatens the nervous system by location: arising along the spine and skull base from notochord remnants, it compresses the brainstem, cranial nerves and spinal cord, so its slow growth still causes severe neurological deficits and demands aggressive local control.
- `connects-to` → **[Carbon](../../02-atomic/carbon/README.md)** — Carbon-ion radiotherapy is an alternative for chordoma: heavy carbon ions deliver dense, highly damaging dose to these notoriously radioresistant tumors, useful when surgery is incomplete or the tumor abuts neural structures—an option in specialized particle centers.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — Chordoma spreads most often to the lung: though it grows slowly and locally along the spine and skull base, late metastasis favors the lungs, so chest imaging is part of follow-up for this notochord-derived bone tumor.
- `connects-to` → **[Immune System](../immune-system/README.md)** — Chordoma is a target for vaccine immunotherapy: nearly all chordomas express brachyury (TBXT), and a brachyury-directed cancer vaccine trains the immune system against this otherwise hard-to-drug developmental transcription factor.
- `connects-to` → **[Oxygen](../../02-atomic/oxygen/README.md)** — Chordoma's radioresistance is partly an oxygen problem: poorly oxygenated tumor regions resist conventional X-rays, so high-dose proton and carbon-ion radiotherapy—less dependent on oxygen and more precise near the spinal cord—are used instead.
- `connects-to` → **[Osteoclast](../../04-cellular/osteoclast/README.md)** — Chordoma destroys bone through osteoclasts: as it grows in the skull base or sacrum it recruits bone-resorbing osteoclasts that erode the surrounding skeleton, so anti-resorptive drugs are explored to slow the local destruction this hard-to-resect tumor causes.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — Chordoma is a vascular tumor that responds to anti-VEGF therapy: it expresses VEGF to grow blood vessels, which is why multi-target TKIs that block VEGF receptors (like sunitinib) can stall this otherwise treatment-resistant cancer.
- `connects-to` → **[p53](../../03-molecular/p53/README.md)** — Losing p53 makes chordoma more aggressive: while most chordomas grow slowly on brachyury, TP53 mutation marks the dangerous shift toward dedifferentiated, fast-growing tumors with a far worse prognosis.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — Chordoma leans on the PI3K-AKT-mTOR growth axis: AKT signaling is frequently active and, with PTEN loss, drives proliferation in these brachyury-dependent tumors, so AKT-mTOR inhibitors are studied for a cancer resistant to chemotherapy.
- `connects-to` → **[MET](../../03-molecular/met/README.md)** — MET signaling can drive aggressive chordoma: amplification or activation of this receptor promotes invasion and growth, adding to the brachyury-driven biology and offering another targetable kinase in a notoriously treatment-resistant bone tumor.
- `connects-to` → **[Cytotoxic T Cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Chordoma is a target for T-cell immunotherapy against brachyury: because the tumor depends on this lineage antigen, vaccines and engineered cytotoxic T cells aim to direct a killing response at a protein cancer cells cannot easily discard.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Chordoma eats away calcium-rich bone: arising in the skull base and sacrum, it destroys the bony matrix as it grows, dissolving the calcium scaffold and threatening the spine and cranial nerves it surrounds.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Chordoma shelters in a macrophage-rich stroma: tumor-associated macrophages populate its microenvironment and dampen immunity, part of why this slow but stubborn tumor resists treatment and recurs.
- `connects-to` → **[Large Intestine](../../06-organ/large-intestine/README.md)** — Sacral chordoma presses on the bowel: the most common chordoma site sits against the rectum and pelvic nerves, so large tumors cause constipation, bowel and bladder dysfunction, and low back pain.
- `connects-to` → **[Peripheral Nerve](../../05-tissue/peripheral-nerve/README.md)** — Chordoma grows against the nerves: skull-base and sacral tumors compress cranial nerves and the cauda equina, causing the neuropathic pain, weakness and bowel-bladder dysfunction that often first signal it.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — Chordoma metastasizes late: though slow-growing and locally destructive, it can seed the lungs, liver and bone over years, especially after repeated local recurrences.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — Chordoma builds its own vasculature: VEGF recruits endothelial cells to feed the tumor, and anti-angiogenic drugs are among the systemic options for this radiation- and surgery-dependent cancer.

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^stacchiotti-2012-imatinib-chordoma]: Stacchiotti S, Longhi A, Ferraresi V, et al. Phase II study of imatinib in advanced chordoma. *J Clin Oncol.* 2012;30(9):914-920. [doi:10.1200/JCO.2011.35.3656](https://doi.org/10.1200/JCO.2011.35.3656) · [PubMed 22330157](https://pubmed.ncbi.nlm.nih.gov/22330157/)
[^yang-2009-tbxt-chordoma]: Yang XR, Ng D, Alcorta DA, et al. T (brachyury) gene duplication confers major susceptibility to familial chordoma. *Nat Genet.* 2009;41(11):1176-1178. [doi:10.1038/ng.454](https://doi.org/10.1038/ng.454) · [PubMed 19801977](https://pubmed.ncbi.nlm.nih.gov/19801977/)
