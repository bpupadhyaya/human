---
schema: human-scale-entry/v1
id: synovial-sarcoma
name: Synovial Sarcoma
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-06
summary: "Synovial sarcoma is defined by SS18-SSX1/SSX2 fusion (t(X;18)) → SMARCB1 displacement from BAF → EZH2 dependency; ~800/year USA; biphasic/monophasic histology; TLE1 IHC positive; ifosfamide-based chemotherapy; tazemetostat (SARC057 ORR ~22%) and trabectedin active."
aliases: ["synovial sarcoma", "SS18-SSX sarcoma", "biphasic synovial sarcoma", "monophasic synovial sarcoma", "t(X;18) sarcoma", "TLE1-positive sarcoma", "translocation sarcoma SYT-SSX", "synovial cell sarcoma"]
sources:
  - id: kadoch-2013-ss18-ssx-baf
    type: peer-reviewed
    cite: "Kadoch C, Crabtree GR. Reversible disruption of mSWI/SNF (BAF) complexes by the SS18-SSX oncogenic fusion in synovial sarcoma. Cell. 2013;153(1):71-85."
    doi: "10.1016/j.cell.2013.02.036"
    pmid: "23540691"
    url: "https://doi.org/10.1016/j.cell.2013.02.036"
  - id: kawai-2015-trabectedin-synovial
    type: peer-reviewed
    cite: "Kawai A, Araki N, Sugiura H, et al. Trabectedin monotherapy after standard chemotherapy versus best supportive care in patients with advanced, translocation-related sarcoma: a randomised, open-label, phase 2 study. Lancet Oncol. 2015;16(4):406-416."
    doi: "10.1016/S1470-2045(15)70098-7"
    pmid: "25795407"
    url: "https://doi.org/10.1016/S1470-2045(15)70098-7"
cross_links:
  - target: 01-human/03-molecular/ss18
    relation: connects-to
    note: "SS18-SSX1/SSX2 fusion (t(X;18)(p11;q11)) is the pathognomonic alteration of synovial sarcoma (100% of cases); FISH for SS18 rearrangement or RT-PCR for SS18-SSX transcript is the diagnostic standard; SSX2 predominates in monophasic SS; SSX1 in biphasic SS."
  - target: 01-human/03-molecular/ezh2
    relation: connects-to
    note: "SS18-SSX displaces SMARCB1 from BAF → PRC2/EZH2 unrestricted → H3K27me3 at CDKN2A, KLF4, and differentiation loci; synovial sarcoma is EZH2-dependent; tazemetostat (EZH2 inhibitor, SARC057): ORR 22% in pretreated SS; FDA breakthrough therapy designation granted for SS."
  - target: 01-human/03-molecular/smarcb1
    relation: connects-to
    note: "SS18-SSX displaces SMARCB1 from canonical BAF without SMARCB1 mutation → SMARCB1 degraded → BAF destabilized → PRC2 access; SMARCB1 IHC remains intact in SS (contrast AT/RT where SMARCB1 is lost); SS18-SSX knockdown → SMARCB1 re-occupies BAF → G1 arrest; shared EZH2 dependency."
  - target: 01-human/03-molecular/cdkn2a
    relation: connects-to
    note: "Homozygous CDKN2A deletion in ~10-15% synovial sarcoma predicts poor prognosis; EZH2/H3K27me3 epigenetically silences CDKN2A even without deletion → absent p16 → CDK4/6 hyperactivation → E2F-driven S-phase; CDK4/6 inhibitors (palbociclib) under evaluation in CDKN2A-deleted SS."
---

# Synovial Sarcoma

## Overview

**Synovial sarcoma (SS)** is a malignant soft tissue sarcoma universally defined by the chromosomal translocation **t(X;18)(p11;q11)** generating a **SS18-SSX1, SS18-SSX2, or SS18-SSX4 fusion protein**. Despite its name, synovial sarcoma does not arise from synovial tissue — it originates from undifferentiated mesenchymal/neural crest precursors. SS is the **second most common soft tissue sarcoma in adolescents and young adults** (after rhabdomyosarcoma) and one of the few sarcomas with a pathognomonic chromosomal translocation [^ladanyi note via kadoch-2013-ss18-ssx-baf].

**Epidemiology:**
- Incidence: ~800 cases/year USA; ~7-10% of all soft tissue sarcomas
- Peak age: 15-40 years (median ~26-30 years); rare in children <5 and adults >60
- Slight male predominance (~1.2:1 M:F)
- No established environmental risk factors; not associated with radiation or NF2 syndrome

**Anatomic locations:**
- Lower extremity (knee/thigh/popliteal fossa): ~50-60% — most common
- Upper extremity (shoulder, elbow, wrist, hand): ~15-20%
- Head and neck (pharynx, tongue, larynx): ~5-10%
- Trunk wall, mediastinum, pleura, lung (primary): ~5-10%
- Intra-abdominal, retroperitoneal: rare; worse prognosis
- Joint space involvement is uncommon despite the name

**Key clinical features:**
- Most present as a painless or mildly painful soft tissue mass, often near (but not within) a joint
- Many are initially misdiagnosed as a benign cyst or ganglion; delay in diagnosis 2-4 years is common
- ~20-25% present with calcifications on plain radiograph (stippled, "egg-shell" calcification characteristic)
- MRI: heterogeneous mass with "triple signal" appearance (hemorrhage, necrosis, calcification); T2 bright heterogeneous; invades fascial planes but rarely bone (unlike osteosarcoma)

## Structure

### Histological subtypes

**Biphasic synovial sarcoma (~30%):**
Two morphologically distinct components:
- **Epithelial component**: glandular/tubular structures lined by cuboidal-to-columnar cells with round nuclei, prominent nucleoli; positive for cytokeratin, EMA, CD34 (focal)
- **Spindle cell component**: fascicular spindle cells with scant cytoplasm, overlapping nuclei, minimal pleomorphism; characteristic hemangiopericytoma-like vessels
- SS18-SSX1 predominates in biphasic type
- Higher rate of epithelial marker positivity; diagnosis is more straightforward

**Monophasic synovial sarcoma (~65%):**
Exclusively spindle cell morphology; can mimic solitary fibrous tumor, malignant peripheral nerve sheath tumor (MPNST), or poorly differentiated carcinoma; TLE1 IHC + and SS18 FISH are critical for diagnosis in monophasic type; SS18-SSX2 predominates

**Poorly differentiated/high-grade synovial sarcoma (~5%):**
Round to large pleomorphic cells; loss of spindle cell morphology; >10 mitoses/10 HPF; rapid growth; worst prognosis; CDKN2A deletion common; all subtypes can have focal poorly differentiated areas

### IHC panel and diagnostic workup

**TLE1 (transducin-like enhancer protein 1):** nuclear positivity in ~85-90% of SS; most sensitive and specific single marker for SS among soft tissue tumors; however, focal TLE1 positivity also in MPNST, solitary fibrous tumor, desmoplastic small round cell tumor — context required

**Keratin (AE1/AE3, MNF116, CAM5.2):** positive in epithelial component of biphasic SS (~70%); focal (25-50%) in monophasic; variable

**EMA (epithelial membrane antigen):** positive in 85% of biphasic; 50% monophasic

**CD34:** focal in some SS; helps distinguish from SFT (CD34 diffuse in SFT)

**SOX2:** strongly positive in most SS (EZH2-driven SOX2 re-expression in SS); synergizes with TLE1 positivity

**SS18 FISH**: confirmatory; SS18 break-apart probe; sensitivity ~95%

## Function

### SS18-SSX oncogenic mechanism

The SS18-SSX fusion protein drives synovial sarcoma through BAF complex subversion [^kadoch-2013-ss18-ssx-baf]:
- SS18-SSX incorporates into cBAF complex, displacing wild-type SS18 → SMARCB1 evicted → BAF destabilized
- EZH2/PRC2 gains chromatin access → H3K27me3 spreads over differentiation loci → CDKN2A, KLF4, neural differentiation genes silenced
- QPGY activation domain (from SS18) drives ETV4, VEGF, and MYC target gene transcription
- Net result: tumor cells are locked in a proliferative, undifferentiated, vascular state with features of both epithelial and mesenchymal lineages

Normal cell (with wild-type BAF-SS18): BAF → SMARCB1 intact → PRC2 excluded from BAF target loci → CDKN2A transcribed → G1 arrest maintained; differentiation programs active

SS cell (with SS18-SSX): cBAF disrupted → SMARCB1 evicted → PRC2 silences CDKN2A + differentiation → proliferative state; paradoxically retains some epithelial features via ETV4/SOX2 de-repression

## Pathology

### Staging and risk stratification

**FNCLCC grading:**
- SS is uniformly high grade (FNCLCC grade 2-3); grading matters less for SS than for other STS
- Poor differentiation, CDKN2A deletion, high mitotic rate → grade 3

**Prognostic factors:**
- **Tumor size**: most important prognostic variable; ≤5 cm → 5-year OS ~85%; >5 cm → ~50%
- **CDKN2A deletion** (~10-15%): associated with >50% reduction in 5-year OS; worst prognostic marker in SS
- **Location**: extremity better than axial/pleural/intra-abdominal; head-neck intermediate
- **Extent of resection**: R0 (negative margin) resection → curative intent; R2 → high recurrence
- **Histological subtype**: poorly differentiated confers worst prognosis within SS
- **Metastases at diagnosis**: ~20-25% have metastases; lung (80%), lymph node (5-10%), bone

### Treatment

**Surgery:**
Wide local excision with ≥1 cm margins is the cornerstone; amputation rarely necessary with modern limb-salvage; compartmental resection when feasible; en-bloc resection of adjacent structures (nerve, vessel) when invaded; regional lymph node dissection for pathologically positive nodes (rare)

**Radiation therapy:**
- Adjuvant RT for high-risk features: tumor >5 cm, positive/close margins (<1 mm), deep location, recurrence
- Standard dose: 50-54 Gy preoperative or 60-66 Gy postoperative (IMRT preferred); equivalent local control in randomized VORTEX trial
- Preoperative RT preferred by most centers (smaller volume, better wound healing in selected cases)

**Chemotherapy — ifosfamide-based regimens:**
SS is one of the most chemotherapy-sensitive sarcomas:
- **First-line**: AI (doxorubicin 75 mg/m² + ifosfamide 10 g/m²) or AIM (AI + mesna) — ORR ~40-60%; PFS ~6-8 months in metastatic SS
- **Ifosfamide monotherapy**: ORR ~25-30% in SS; higher single-agent activity than in other STS subtypes
- **High-dose ifosfamide** (14-21 g/m²): ORR ~30-35% in ifosfamide-pretreated SS (unique ifosfamide sensitivity in SS vs other STS)

**Trabectedin:**
KAWAI 2015 (Phase 2 vs BSC) [^kawai-2015-trabectedin-synovial]: N=73 translocation-positive sarcomas (SS + myxoid liposarcoma); trabectedin 1.5 mg/m² q21d vs BSC; primary endpoint PFS; HR 0.07 (p<0.0001); 12-week PFS 60% vs 21%; OS benefit trending; ORR 17%; approved in Japan for translocation-related sarcoma; used off-label in USA; proposed mechanism: trabectedin directly disrupts SS18-SSX from chromatin

**Pazopanib:**
PALETTE Phase 3: PFS benefit in non-adipocytic STS including SS; HR 0.35; FDA-approved for advanced STS after prior chemotherapy; ORR ~5-10% in SS; PFS benefit more reliable than objective response

**Tazemetostat (EZH2 inhibitor):**
SARC057 (Phase 2): ORR ~22%, DCR ~67% in relapsed/refractory SS; FDA breakthrough therapy designation; ongoing Phase 1/2 combination studies (tazemetostat + ifosfamide; tazemetostat + pembrolizumab); represents first molecularly targeted therapy in SS

**Pembrolizumab/nivolumab:**
SS has low TMB (~1-2 mut/Mb) and variable PD-L1 expression; ICB response rates ~10-15% (lower than expected); MSS phenotype (no mismatch repair deficiency); combination with tazemetostat under investigation (EZH2 inhibition may restore IFN-γ response via epigenetic de-repression)

**Prognosis:**
- Localized SS (≤5 cm, R0 resection, no poor-differentiation): 5-year OS ~80-85%
- Localized SS (>5 cm, positive margin, or grade 3): 5-year OS ~50-60%
- Metastatic SS at diagnosis: 5-year OS ~20-25%; median OS ~18-24 months
- CDKN2A-deleted SS: 5-year OS ~30-40% regardless of stage
- Local recurrence: ~20-30% at 5 years; re-resection feasible if technically possible
- Lung metastases: surgical resection if oligometastatic; 5-year OS after resection ~30%

## Connections

- `connects-to` → **[SS18](../../03-molecular/ss18/README.md)** — SS18-SSX1/SSX2 fusion (t(X;18)(p11;q11)) is the pathognomonic alteration of synovial sarcoma (100% of cases); FISH for SS18 rearrangement or RT-PCR for SS18-SSX transcript is the diagnostic standard; SSX2 predominates in monophasic SS; SSX1 in biphasic SS.
- `connects-to` → **[EZH2](../../03-molecular/ezh2/README.md)** — SS18-SSX displaces SMARCB1 from BAF → PRC2/EZH2 unrestricted → H3K27me3 at CDKN2A, KLF4, and differentiation loci; synovial sarcoma is EZH2-dependent; tazemetostat (EZH2 inhibitor, SARC057): ORR 22% in pretreated SS; FDA breakthrough therapy designation granted for SS.
- `connects-to` → **[SMARCB1](../../03-molecular/smarcb1/README.md)** — SS18-SSX displaces SMARCB1 from canonical BAF without SMARCB1 mutation → SMARCB1 degraded → BAF destabilized → PRC2 access; SMARCB1 IHC remains intact in SS (contrast AT/RT where SMARCB1 is lost); SS18-SSX knockdown → SMARCB1 re-occupies BAF → G1 arrest; shared EZH2 dependency.
- `connects-to` → **[CDKN2A](../../03-molecular/cdkn2a/README.md)** — Homozygous CDKN2A deletion in ~10-15% synovial sarcoma predicts poor prognosis; EZH2/H3K27me3 epigenetically silences CDKN2A even without deletion → absent p16 → CDK4/6 hyperactivation → E2F-driven S-phase; CDK4/6 inhibitors (palbociclib) under evaluation in CDKN2A-deleted SS.

[^kadoch-2013-ss18-ssx-baf]: Kadoch C, Crabtree GR. Reversible disruption of mSWI/SNF (BAF) complexes by the SS18-SSX oncogenic fusion in synovial sarcoma. *Cell.* 2013;153(1):71-85. [doi:10.1016/j.cell.2013.02.036](https://doi.org/10.1016/j.cell.2013.02.036) · [PubMed 23540691](https://pubmed.ncbi.nlm.nih.gov/23540691/)
[^kawai-2015-trabectedin-synovial]: Kawai A, Araki N, Sugiura H, et al. Trabectedin monotherapy after standard chemotherapy versus best supportive care in patients with advanced, translocation-related sarcoma: a randomised, open-label, phase 2 study. *Lancet Oncol.* 2015;16(4):406-416. [doi:10.1016/S1470-2045(15)70098-7](https://doi.org/10.1016/S1470-2045(15)70098-7) · [PubMed 25795407](https://pubmed.ncbi.nlm.nih.gov/25795407/)
