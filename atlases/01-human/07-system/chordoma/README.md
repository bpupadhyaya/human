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

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^stacchiotti-2012-imatinib-chordoma]: Stacchiotti S, Longhi A, Ferraresi V, et al. Phase II study of imatinib in advanced chordoma. *J Clin Oncol.* 2012;30(9):914-920. [doi:10.1200/JCO.2011.35.3656](https://doi.org/10.1200/JCO.2011.35.3656) · [PubMed 22330157](https://pubmed.ncbi.nlm.nih.gov/22330157/)
[^yang-2009-tbxt-chordoma]: Yang XR, Ng D, Alcorta DA, et al. T (brachyury) gene duplication confers major susceptibility to familial chordoma. *Nat Genet.* 2009;41(11):1176-1178. [doi:10.1038/ng.454](https://doi.org/10.1038/ng.454) · [PubMed 19801977](https://pubmed.ncbi.nlm.nih.gov/19801977/)
