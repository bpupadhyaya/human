---
schema: human-scale-entry/v1
id: ewing-sarcoma
name: Ewing Sarcoma
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-06
summary: "Ewing sarcoma is an EWSR1-ETS fusion-driven small round blue cell tumor of bone/soft tissue; peak age 10-20 years; EWSR1-FLI1 ~85%; localized 5-year EFS ~60-70%; metastatic ~15-25%; VCD/IE or VIDE induction; local control by surgery ± RT; HDCT+auto-SCT for high-risk."
aliases: ["Ewing sarcoma", "ESFT", "Ewing's sarcoma", "primitive neuroectodermal tumor", "PNET bone", "EWS", "Ewing sarcoma family tumors", "extraskeletal Ewing"]
sources:
  - id: grier-2003-ewing-vdc-ie
    type: peer-reviewed
    cite: "Grier HE, Krailo MD, Tarbell NJ, et al. Addition of ifosfamide and etoposide to standard chemotherapy for Ewing's sarcoma and primitive neuroectodermal tumor of bone. N Engl J Med. 2003;348(8):694-701."
    doi: "10.1056/NEJMoa020890"
    pmid: "12594313"
    url: "https://doi.org/10.1056/NEJMoa020890"
  - id: ladenstein-2010-euro-ewing99-r3
    type: peer-reviewed
    cite: "Ladenstein R, Potschger U, Le Deley MC, et al. Primary disseminated multifocal Ewing sarcoma: results of the Euro-EWING 99 trial. J Clin Oncol. 2010;28(20):3284-3291."
    doi: "10.1200/JCO.2009.22.9864"
    pmid: "20498398"
    url: "https://doi.org/10.1200/JCO.2009.22.9864"
cross_links:
  - target: 01-human/03-molecular/ewsr1
    relation: connects-to
    note: "EWSR1-FLI1 t(11;22) (~85%) and EWSR1-ERG t(21;22) (~10%) are the defining fusions; EWSR1 break-apart FISH confirms rearrangement; RNA-seq specifies fusion partner; EWSR1-FLI1 activates GGAA microsatellite neo-enhancers driving a unique neuroectodermal program."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "EWSR1-FLI1 transcriptionally activates IGF1R → autocrine IGF loop → PI3K-AKT-mTOR → survival; mTOR inhibitors have modest single-agent activity in Ewing; dual IGF1R+mTOR inhibition explored; IGF1R antibodies (ganitumab) had ~10-15% ORR in R/R Ewing."
  - target: 01-human/03-molecular/p53
    relation: connects-to
    note: "TP53 mutations are rare at Ewing diagnosis (<5%) but acquired in ~20-30% at relapse; CDKN2A/ARF deletion in ~15% primary Ewing; MDM2 amplification ~3%; idasanutlin (MDM2 inhibitor) + chemotherapy explored in pediatric solid tumors including R/R Ewing."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "EWSR1-FLI1 activates IGF1R/RAS → ERK1/2 → Ewing survival and NKX2-2 transcription; RAS/MAPK pathway mutations (KRAS, NRAS, NF1) are acquired at relapse in ~30% Ewing; MEK inhibitors explored in refractory disease; ERK1/2 co-activates the neuroectodermal blast program."
  - target: 01-human/03-molecular/pten
    relation: connects-to
    note: "PTEN loss enhances IGF1R→PI3K-AKT signaling in Ewing; PTEN deletions uncommon at diagnosis but acquired at relapse; mTOR inhibitors + IGF1R antibodies show synergy in preclinical Ewing; PI3K/AKT/mTOR inhibitors (temsirolimus) explored in R/R Ewing and pediatric solid tumors."
  - target: 01-human/03-molecular/cdkn2a
    relation: connects-to
    note: "CDKN2A/ARF deletion in ~15% of primary Ewing sarcoma; ARF loss → MDM2 unchecked → p53 suppressed → apoptosis evasion; CDKN2A deletion co-occurs with poor histologic response; MDM2 inhibitors (idasanutlin) + VDC/IE under study; CDKN2A deletion acquired in ~25% at relapse."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "Ewing sarcoma is angiogenic; cabozantinib (VEGFR2+MET+RET) showed ORR ~20% in R/R Ewing; EWSR1-FLI1 upregulates VEGF expression; regorafenib (VEGFR+KIT) active in some R/R pediatric sarcomas; anti-angiogenic strategies combined with VEGFR inhibition under investigation."
  - target: 01-human/07-system/chordoma
    relation: connects-to
    note: "Ewing sarcoma and chordoma are both fusion/lineage-defined bone tumors but opposites: Ewing a fast small-round-blue-cell tumor of children driven by EWSR1-FLI1, chordoma a slow midline notochordal tumor of adults driven by TBXT — one genetic lesion specifying an entire sarcoma."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "The lung is the most common metastatic site in Ewing sarcoma, and isolated pulmonary metastases carry a better prognosis than bone or marrow spread; whole-lung irradiation is added for lung-only metastatic disease, and metastasectomy of residual nodules is considered after chemo."
  - target: 01-human/07-system/osteosarcoma
    relation: connects-to
    note: "Ewing sarcoma and osteosarcoma are the two main pediatric bone cancers but differ fundamentally: osteosarcoma is an osteoid-producing tumor of the metaphysis, Ewing a small-round-cell tumor of the diaphysis driven by EWSR1-FLI1 — and unlike osteosarcoma, Ewing is radiosensitive."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "Ewing sarcoma is a small-round-blue-cell malignancy of the musculoskeletal system: it arises in bone (pelvis, femur, ribs) or soft tissue of children and young adults with pain and a mass, driven by the EWSR1-FLI1 fusion rather than the osteoid production of osteosarcoma."
  - target: 01-human/07-system/rhabdomyosarcoma
    relation: connects-to
    note: "Ewing sarcoma and rhabdomyosarcoma are the two commonest pediatric small-round-blue-cell sarcomas and key differentials: both need molecular work-up—Ewing has EWSR1-FLI1 and CD99, rhabdomyosarcoma shows myogenic markers (desmin, myogenin) and PAX-FOXO1—since treatment differs."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Ewing sarcoma is notably radiosensitive: unlike most bone sarcomas, radiotherapy is a primary local-control option (with surgery) for tumors in unresectable sites like the pelvis or spine, integrated with intensive multi-agent chemotherapy—photon/proton radiation exploits it."
  - target: 01-human/07-system/neuroblastoma
    relation: connects-to
    note: "Ewing sarcoma and neuroblastoma are both 'small round blue cell' childhood tumors that can look alike on biopsy but are biologically distinct: Ewing is driven by the EWSR1-FLI1 fusion in bone, neuroblastoma by MYCN-amplified sympathetic neuroblasts—IHC separates them."
  - target: 01-human/04-cellular/osteoblast
    relation: connects-to
    note: "Ewing sarcoma's cell of origin is debated between mesenchymal stem cells and the neural-crest/osteoblast lineage: unlike osteosarcoma it makes no bone matrix, so the EWSR1-FLI1 fusion—not an osteoblast program—defines it, arising within bone yet producing no osteoid."
  - target: 01-human/07-system/li-fraumeni-syndrome
    relation: connects-to
    note: "Ewing sarcoma and Li-Fraumeni syndrome intersect at TP53: germline p53 loss in Li-Fraumeni predisposes to many sarcomas, and somatic TP53 mutation worsens Ewing's prognosis—both show how losing the genome's guardian fuels these aggressive bone and soft-tissue cancers."
---

# Ewing Sarcoma

## Overview

**Ewing sarcoma** is the second most common primary malignant bone tumor in children and young adults (after osteosarcoma), and the most common **soft tissue sarcoma** in the first decade of life. It belongs to the **Ewing Sarcoma Family of Tumors (ESFT)**, defined by chromosomal translocations fusing **EWSR1 (22q12)** to an **ETS family transcription factor** — most commonly FLI1 [t(11;22), ~85%] or ERG [t(21;22), ~10%] — creating a fusion oncoprotein that drives a pathological neuroectodermal transcriptional program. Ewing sarcoma is a **small round blue cell tumor (SRBCT)** with characteristic CD99+ immunophenotype and molecular confirmation required by FISH or RNA sequencing. Peak incidence occurs at ages 10-20 years; it is notably rare in African Americans (possibly due to GGAA microsatellite repeat frequency differences in African genomic backgrounds). Treatment is multimodal: **VCD/IE chemotherapy** (vincristine+cyclophosphamide+doxorubicin alternating with ifosfamide+etoposide), established as superior to VCD alone by the landmark INT-0091 trial [^grier-2003-ewing-vdc-ie], followed by **local control** (surgery, RT, or both) and consolidation; **high-risk/metastatic disease** benefits from **high-dose chemotherapy + autologous SCT** (Euro-EWING99: HDCT achieved 3-year EFS ~27% vs ~6% conventional consolidation in multifocal Ewing) [^ladenstein-2010-euro-ewing99-r3].

**Epidemiology:**
- ~250-300 cases/year in the USA; ~2,000-2,500/year globally
- Median age 15 years; second pediatric bone tumor peak (osteosarcoma is the first); rare after age 40
- Nearly exclusively affects people of European descent (~4:1 White:Black incidence; African Americans rarely develop Ewing)
- Slight male predominance (~1.5:1)
- Primary sites: diaphysis/metadiaphysis of long bones (~50%), pelvis (~25%), chest wall (~15%), spine (~10%)
- Extraskeletal Ewing (extraosseous): ~20% of all Ewing; same biology, management, prognosis as skeletal

## Structure

### Molecular landscape

**EWSR1-FLI1 t(11;22)(q24;q12) (~85%):**
Most common Ewing fusion; Type 1 (EWSR1 exon 7 – FLI1 exon 6) ~60%; Type 2 (EWSR1 exon 7 – FLI1 exon 5) ~25%; less common fusion types; EWSR1-FLI1 is virtually pathognomonic for Ewing sarcoma (distinguishes from other SRBCTs).

**EWSR1-ERG t(21;22)(q22;q12) (~10%):**
ERG is an ETS factor also involved in prostate cancer (ERG fusions via TMPRSS2); EWSR1-ERG and EWSR1-FLI1 drive nearly identical transcriptional programs (same ETS domain biology); clinically equivalent prognosis; both bind GGAA microsatellite neo-enhancers.

**Rare fusions (<5%):** EWSR1-ETV1, EWSR1-ETV4, EWSR1-FEV — all ETS family; similar but subtle biologic distinctions.

**EWSR1-negative Ewing-like sarcomas (now separate WHO entities):**
- **CIC-rearranged sarcoma** (CIC::DUX4, CIC::FOXO4): EWSR1 FISH negative; CD99 variable; more aggressive than Ewing
- **BCOR-rearranged sarcoma** (BCOR::CCNB3, BCOR::MAML3): EWSR1 FISH negative; bone/soft tissue; EFS inferior to typical Ewing
These are classified separately in WHO Classification of Soft Tissue and Bone Tumours 2020.

**Acquired mutations at relapse:**
RAS/MAPK pathway mutations (KRAS, NRAS, NF1, BRAF): ~30% at relapse; TP53 mutations: ~20-30% at relapse; CDKN2A deletion: ~15% primary Ewing; BRG1 (SMARCA4) loss: rare (<5%); chemotherapy resistance mediated largely through RAS/MAPK and p53 pathway derangements.

### Histology and immunophenotype

**Small round blue cells:** Uniform, tightly packed cells with round nuclei, finely dispersed chromatin, inconspicuous nucleoli, scant clear cytoplasm; no matrix production (absent osteoid or chondroid); sheets of cells without geographic necrosis (compared to central necrosis in osteosarcoma); Homer-Wright rosettes visible in PNET variant (attempt at neural-tube rosette formation).

**Immunophenotype:**
- **CD99 (MIC2):** ~95-100% strong membranous positivity — most sensitive marker; not specific (positive in T-LBL, synovial sarcoma, poorly differentiated synovial sarcoma)
- **NKX2-2:** ~90-95% nuclear positive — best available specific marker for Ewing (downstream EWSR1-FLI1 target); negative in most other SRBCTs
- **FLI1:** Nuclear positive (~85%) but also positive in vascular tumors (angiosarcoma, hemangioma) — specificity limited
- **Synaptophysin, CD56 (NCAM):** Variable (~50%); reflects neural crest/neuroectodermal origin
- **TdT:** Negative (distinguishes from T-LBL/lymphoma)
- **Desmin, myogenin:** Negative (distinguishes from rhabdomyosarcoma)

**Differential diagnosis of SRBCTs:**
- Ewing sarcoma
- Rhabdomyosarcoma (desmin+, myogenin+, FOXO1 or PAX3/7 fusions)
- Poorly differentiated synovial sarcoma (SS18-SSX fusion)
- Neuroblastoma (MYCN amp, TH+, synaptophysin+, neural features)
- Desmoplastic small round cell tumor (DSRCT, EWSR1-WT1, desmoplastic stroma)
- CIC-rearranged sarcoma

## Function

### Pathophysiology

**Ewing sarcoma cell of origin:**
Still debated; most evidence supports **mesenchymal stem cell** (bone marrow stromal/progenitor) as origin — EWSR1-FLI1 expression in MSC → reprogramming toward neuroectodermal state; some evidence for neural crest cell of origin in extraskeletal Ewing; key: the cell-of-origin must tolerate EWSR1-FLI1 without immediate apoptosis; in most cell types, forced EWSR1-FLI1 expression → massive apoptosis; MSCs are uniquely tolerant → selective outgrowth.

**EWSR1-FLI1 → NKX2-2 → arrested differentiation:**
The cardinal downstream event: EWSR1-FLI1 activates NKX2-2 from a GGAA microsatellite neo-enhancer ~60 kb upstream of NKX2-2 → NKX2-2 is a homeodomain TF that normally programs pancreatic β-cell and neural identity; in Ewing, NKX2-2 suppresses mesenchymal/adipogenic differentiation genes (PPARG, CEBPA) → arrests cells in a progenitor state; NKX2-2 is the single most diagnostic IHC marker for Ewing and the mechanistically central EWSR1-FLI1 target.

**IGF autocrine loop:**
EWSR1-FLI1 transcriptionally activates IGF1R and suppresses IGFBP3 (negative IGF regulator) → high free IGF2 + high IGF1R → constitutive IGF1R → JAK2/STAT5, PI3K-AKT-mTOR, MAPK → proliferation, survival, resistance to apoptosis; this loop is why IGF1R antibodies were tested (and showed partial activity) in Ewing.

## Pathology

### Staging

**ESFT staging (COG and EURO-EWING):**
- **Localized:** Primary tumor without distant metastases (~50-60% at diagnosis); includes tumors with local extension (soft tissue mass around bone, no distant mets)
- **Regional:** Pathologically involved regional lymph nodes (uncommon in bone primaries)
- **Metastatic:** Distant hematogenous metastases → lung (~40% of metastatic), bone (~30%), bone marrow (~10%), combinations; multiple bone/BM sites = "multifocal" (worst prognosis)
- **Extent of disease by site:** Pelvic primary → adverse (large, unresectable); axial primary → worse than extremity; pulmonary metastases only → intermediate prognosis; bone/BM metastases → poorest prognosis

### Treatment

**Induction chemotherapy (14-17 weeks):**
Two equivalent induction regimens (center-dependent):
- **VCD/IE (COG):** Vincristine+cyclophosphamide+doxorubicin (VCD) alternating with ifosfamide+etoposide (IE) every 2 weeks × 14 cycles total; 5-year EFS for localized disease: ~70%; addition of IE to VC+D improved 5-year EFS from ~54% to ~69% (INT-0091/Grier 2003) [^grier-2003-ewing-vdc-ie]; G-CSF support required for 14-day intervals
- **VIDE (EURO-EWING):** Vincristine+ifosfamide+doxorubicin+etoposide × 6 cycles (21-day) as induction; roughly equivalent outcomes; more ifosfamide per cycle

**Histologic response assessment:**
After induction → surgical specimen assessed for percent tumor necrosis (Salzer-Kuntschik grading or Huvos grading); **>90% necrosis = good histologic response** → independent favorable prognostic factor; poor response (<90% necrosis) → consider consolidation intensification or HDCT.

**Local control:**
- **Surgery (preferred if R0 achievable):** Wide resection with negative margins; reconstruction (endoprosthesis, allograft, recycled autograft); if R0 achieved → no additional RT required; R1/R2 resection → adjuvant RT
- **Definitive RT (for unresectable tumors):** 45-55.8 Gy involved-field RT; for spine/sacrum (unresectable sites); RT alone for local control inferior to surgery but achieves local control in ~70%
- **Combined surgery+RT:** For incomplete margins or specific anatomical sites (pelvis with soft tissue involvement)

**Consolidation:**
- **Localized, good response:** VCD/IE maintenance × additional 8-10 cycles → 5-year EFS ~70%; no HDCT for most localized good-response Ewing
- **Localized, poor response or high-risk features (pelvic, large tumor >200 mL):** Consider HDCT+auto-SCT (busulfan+melphalan myeloablative; some centers use treosulfan+melphalan to reduce hepatotoxicity)
- **Metastatic (pulmonary only):** Standard VCD/IE + local control + whole-lung irradiation (WLI, 15-18 Gy) → 5-year EFS ~25-35%; WLI significantly improves pulmonary EFS
- **Multifocal/disseminated metastatic:** Euro-EWING99-R3: HDCT (busulfan+melphalan) vs conventional therapy in primary disseminated multifocal Ewing → 3-year EFS 27% vs 6% (HR 0.60, p=0.005) [^ladenstein-2010-euro-ewing99-r3]; tandem HDCT exploring in worst-risk group

**Novel and investigational agents:**
- **TK216 (OBI-3424 analog):** EWS-FLI1-interfering agent; Phase 1/2: modest single-agent activity; Phase 2 ongoing
- **Olaparib + temozolomide:** HR deficiency rationale (EWSR1 loss reduces HR); pediatric Phase 1/2 (SARC024): ORR ~30% in relapsed Ewing
- **Anti-GD2 (dinutuximab):** GD2 expressed on Ewing; Phase 2 AEWS0821 (dinutuximab + VDC/IE): not superior to VDC/IE alone in localized disease; ongoing refinement in metastatic disease
- **Alisertib (AURKA):** Phase 2 in R/R pediatric solid tumors including Ewing: ORR ~10-20%
- **Cabozantinib (VEGFR/MET/RET):** Phase 2 in R/R Ewing: ORR ~20% (modest); some molecular responses
- **CAR-T (anti-GD2, anti-CD99):** Phase 1 trials; manufacturing challenges in pediatric patients

**Relapsed Ewing sarcoma:**
- If ≥12 months from prior ifosfamide/etoposide: topotecan+cyclophosphamide (TC) or irinotecan+temozolomide (IT); ORR ~30-40%
- If <12 months (early relapse): gemcitabine+docetaxel; ORR ~15-25%
- Overall salvage: 5-year OS <10-20% for relapsed metastatic Ewing; salvage surgery for isolated pulmonary relapse most likely to achieve cure
- Allo-SCT: some centers after second remission; limited data; associated with high TRM

### Long-term effects

- **Secondary malignancy:** RT field → secondary bone sarcoma (osteosarcoma, fibrosarcoma) in ~5% at 20 years; alkylator/etoposide → secondary AML/MDS
- **Infertility:** Cyclophosphamide+ifosfamide → gonadal damage; fertility preservation (sperm cryopreservation, oocyte preservation) strongly recommended before therapy
- **Orthopedic:** Endoprosthetic reconstruction → infection risk, mechanical failure at ~15-20 years; physeal damage from RT → limb length discrepancy
- **Pulmonary:** WLI → restrictive lung disease; bleomycin not used in Ewing (unlike older regimens)
- **Cardiac:** Doxorubicin → cardiomyopathy (standard cumulative dose limits ~375-450 mg/m²); cardiac surveillance post-therapy

## Connections

- `connects-to` → **[EWSR1](../../03-molecular/ewsr1/README.md)** — EWSR1-FLI1 t(11;22) (~85%) and EWSR1-ERG t(21;22) (~10%) are the defining fusions; EWSR1 break-apart FISH confirms rearrangement; RNA-seq specifies fusion partner; EWSR1-FLI1 activates GGAA microsatellite neo-enhancers driving a unique neuroectodermal program.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — EWSR1-FLI1 transcriptionally activates IGF1R → autocrine IGF loop → PI3K-AKT-mTOR → survival; mTOR inhibitors have modest single-agent activity in Ewing; dual IGF1R+mTOR inhibition explored; IGF1R antibodies (ganitumab) had ~10-15% ORR in R/R Ewing.
- `connects-to` → **[P53](../../03-molecular/p53/README.md)** — TP53 mutations are rare at Ewing diagnosis (<5%) but acquired in ~20-30% at relapse; CDKN2A/ARF deletion in ~15% primary Ewing; MDM2 amplification ~3%; idasanutlin (MDM2 inhibitor) + chemotherapy explored in pediatric solid tumors including R/R Ewing.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — EWSR1-FLI1 activates IGF1R/RAS → ERK1/2 → Ewing survival and NKX2-2 transcription; RAS/MAPK pathway mutations (KRAS, NRAS, NF1) are acquired at relapse in ~30% Ewing; MEK inhibitors explored in refractory disease; ERK1/2 co-activates the neuroectodermal blast program.
- `connects-to` → **[PTEN](../../03-molecular/pten/README.md)** — PTEN loss enhances IGF1R→PI3K-AKT signaling in Ewing; PTEN deletions uncommon at diagnosis but acquired at relapse; mTOR inhibitors + IGF1R antibodies show synergy in preclinical Ewing; PI3K/AKT/mTOR inhibitors (temsirolimus) explored in R/R Ewing and pediatric solid tumors.
- `connects-to` → **[CDKN2A](../../03-molecular/cdkn2a/README.md)** — CDKN2A/ARF deletion in ~15% of primary Ewing sarcoma; ARF loss → MDM2 unchecked → p53 suppressed → apoptosis evasion; CDKN2A deletion co-occurs with poor histologic response; MDM2 inhibitors (idasanutlin) + VDC/IE under study; CDKN2A deletion acquired in ~25% at relapse.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — Ewing sarcoma is angiogenic; cabozantinib (VEGFR2+MET+RET) showed ORR ~20% in R/R Ewing; EWSR1-FLI1 upregulates VEGF expression; regorafenib (VEGFR+KIT) active in some R/R pediatric sarcomas; anti-angiogenic strategies combined with VEGFR inhibition under investigation.
- `connects-to` → **[Chordoma](../chordoma/README.md)** — Ewing sarcoma and chordoma are both fusion/lineage-defined bone tumors but opposites: Ewing a fast small-round-blue-cell tumor of children driven by EWSR1-FLI1, chordoma a slow midline notochordal tumor of adults driven by TBXT — one genetic lesion specifying an entire sarcoma.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — The lung is the most common metastatic site in Ewing sarcoma, and isolated pulmonary metastases carry a better prognosis than bone or marrow spread; whole-lung irradiation is added for lung-only metastatic disease, and metastasectomy of residual nodules is considered after chemo.
- `connects-to` → **[Osteosarcoma](../osteosarcoma/README.md)** — Ewing sarcoma and osteosarcoma are the two main pediatric bone cancers but differ fundamentally: osteosarcoma is an osteoid-producing tumor of the metaphysis, Ewing a small-round-cell tumor of the diaphysis driven by EWSR1-FLI1 — and unlike osteosarcoma, Ewing is radiosensitive.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — Ewing sarcoma is a small-round-blue-cell malignancy of the musculoskeletal system: it arises in bone (pelvis, femur, ribs) or soft tissue of children and young adults with pain and a mass, driven by the EWSR1-FLI1 fusion rather than the osteoid production of osteosarcoma.
- `connects-to` → **[Rhabdomyosarcoma](../rhabdomyosarcoma/README.md)** — Ewing sarcoma and rhabdomyosarcoma are the two commonest pediatric small-round-blue-cell sarcomas and key differentials: both need molecular work-up—Ewing has EWSR1-FLI1 and CD99, rhabdomyosarcoma shows myogenic markers (desmin, myogenin) and PAX-FOXO1—since treatment differs.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Ewing sarcoma is notably radiosensitive: unlike most bone sarcomas, radiotherapy is a primary local-control option (with surgery) for tumors in unresectable sites like the pelvis or spine, integrated with intensive multi-agent chemotherapy—photon/proton radiation exploits it.
- `connects-to` → **[Neuroblastoma](../neuroblastoma/README.md)** — Ewing sarcoma and neuroblastoma are both 'small round blue cell' childhood tumors that can look alike on biopsy but are biologically distinct: Ewing is driven by the EWSR1-FLI1 fusion in bone, neuroblastoma by MYCN-amplified sympathetic neuroblasts—IHC separates them.
- `connects-to` → **[Osteoblast](../../04-cellular/osteoblast/README.md)** — Ewing sarcoma's cell of origin is debated between mesenchymal stem cells and the neural-crest/osteoblast lineage: unlike osteosarcoma it makes no bone matrix, so the EWSR1-FLI1 fusion—not an osteoblast program—defines it, arising within bone yet producing no osteoid.
- `connects-to` → **[Li-Fraumeni Syndrome](../li-fraumeni-syndrome/README.md)** — Ewing sarcoma and Li-Fraumeni syndrome intersect at TP53: germline p53 loss in Li-Fraumeni predisposes to many sarcomas, and somatic TP53 mutation worsens Ewing's prognosis—both show how losing the genome's guardian fuels these aggressive bone and soft-tissue cancers.

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^grier-2003-ewing-vdc-ie]: Grier HE, Krailo MD, Tarbell NJ, et al. Addition of ifosfamide and etoposide to standard chemotherapy for Ewing's sarcoma and primitive neuroectodermal tumor of bone. *N Engl J Med.* 2003;348(8):694-701. [doi:10.1056/NEJMoa020890](https://doi.org/10.1056/NEJMoa020890) · [PubMed 12594313](https://pubmed.ncbi.nlm.nih.gov/12594313/)
[^ladenstein-2010-euro-ewing99-r3]: Ladenstein R, Potschger U, Le Deley MC, et al. Primary disseminated multifocal Ewing sarcoma: results of the Euro-EWING 99 trial. *J Clin Oncol.* 2010;28(20):3284-3291. [doi:10.1200/JCO.2009.22.9864](https://doi.org/10.1200/JCO.2009.22.9864) · [PubMed 20498398](https://pubmed.ncbi.nlm.nih.gov/20498398/)
