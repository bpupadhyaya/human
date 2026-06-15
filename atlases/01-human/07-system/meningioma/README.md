---
schema: human-scale-entry/v1
id: meningioma
name: Meningioma
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-06
summary: "Meningioma is the most common intracranial tumor; WHO grades 1-3; NF2 LOF ~50-60%, AKT1 E17K ~10-12%, TRAF7 ~25%; grade 1 5-year recurrence: GTR ~7%; grade 2 ~40%; grade 3 ~80%; surgery ± SRS for grade 1-2; RT for grade 3; bevacizumab and mTOR inhibitors for recurrent disease."
aliases: ["meningioma", "intracranial meningioma", "benign meningioma", "atypical meningioma", "anaplastic meningioma", "NF2 meningioma", "skull base meningioma", "convexity meningioma", "spinal meningioma"]
sources:
  - id: brastianos-2013-akt1-meningioma
    type: peer-reviewed
    cite: "Brastianos PK, Horowitz PM, Santagata S, et al. Genomic sequencing of meningiomas identifies oncogenic SMO and AKT1 mutations. Nat Genet. 2013;45(3):285-289."
    doi: "10.1038/ng.2526"
    pmid: "23334667"
    url: "https://doi.org/10.1038/ng.2526"
  - id: nassiri-2021-meningioma-classification
    type: peer-reviewed
    cite: "Nassiri F, Liu J, Patil V, et al. A clinically applicable integrative molecular classification of meningiomas. Nature. 2021;597(7874):119-125."
    doi: "10.1038/s41586-021-03850-3"
    pmid: "34385709"
    url: "https://doi.org/10.1038/s41586-021-03850-3"
cross_links:
  - target: 01-human/03-molecular/nf2
    relation: connects-to
    note: "NF2 biallelic LOF in ~50-60% sporadic meningioma; NF2 loss → Hippo inactivation → YAP/TAZ nuclear → TEAD-driven proliferation; NF2-mutant meningiomas are convexity-predominant; germline NF2 → bilateral VS, meningiomas, ependymomas; TEAD inhibitors in Phase 1 trials."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "AKT1 E17K (~10-12% skull base meningioma, grade 1) directly activates mTORC1/mTORC2; NF2 loss → Hippo off → YAP/TAZ nuclear → upstream mTOR activators; mTOR inhibitors (everolimus/sirolimus) in NF2 syndrome VS (REACT trial, 2012): volumetric reduction of VS in 30-44% of patients."
  - target: 01-human/03-molecular/egfr
    relation: connects-to
    note: "AKT1 E17K and NF2 loss both engage EGFR/ErbB signaling in meningioma; NF2-null → ErbB2 surface overexpression → sustained RAS/MAPK; erlotinib and gefitinib explored in recurrent meningioma with modest activity; ErbB2 amplification is rare in meningioma."
  - target: 01-human/03-molecular/pten
    relation: connects-to
    note: "PTEN loss in ~10-15% meningioma; NF2 and PTEN both suppress PI3K/AKT/mTOR → NF2+PTEN co-loss is synergistic; AKT1 E17K (skull base meningioma, ~10-12%) activates PI3K/mTOR without PTEN loss; mTOR inhibitors target the convergent PI3K/mTOR axis in meningioma."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "Meningioma is the most common intracranial tumor, arising not from brain but from arachnoid cap cells of the meninges; it compresses brain and cranial nerves, and location (convexity, skull base, parasagittal) dictates resectability and surgical morbidity more than grade."
  - target: 01-human/07-system/neurofibromatosis-type-2
    relation: connects-to
    note: "Germline NF2 loss (neurofibromatosis type 2) predisposes to multiple meningiomas alongside bilateral vestibular schwannomas and ependymomas; sporadic meningiomas carry biallelic NF2 loss in ~50-60%, making merlin/Hippo inactivation the central driver in both settings."
  - target: 01-human/03-molecular/progesterone
    relation: connects-to
    note: "Grade 1 meningiomas show a 2-3:1 female predominance and express progesterone receptors, with growth during pregnancy and on medroxyprogesterone exposure; yet anti-progesterone mifepristone failed in Phase 3, so PR positivity does not predict hormone-blockade response."
  - target: 01-human/07-system/mesothelioma
    relation: connects-to
    note: "Meningioma and mesothelioma are unrelated tumors united by one driver: biallelic NF2/merlin loss inactivates Hippo, freeing YAP/TAZ-TEAD to drive proliferation in ~50-60% of meningiomas and ~40% of mesotheliomas — making both lead indications for TEAD inhibitors now in trials."
  - target: 01-human/03-molecular/yap1
    relation: connects-to
    note: "Meningioma growth runs through YAP: NF2/merlin loss releases YAP/TAZ to partner with TEAD and transcribe proliferative genes; this Hippo-YAP axis, not a classic oncogene, drives most meningiomas, and TEAD-palmitoylation inhibitors are the first targeted therapy in trials."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "Meningioma is the most common primary CNS tumor, but it arises from the meninges (arachnoid cap cells), not neural tissue — growing outside the brain and spinal cord and causing symptoms by compression; its dural-based, extra-axial location makes many curable by resection."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Ionizing radiation is the best-established environmental cause of meningioma: prior cranial radiotherapy (even low-dose scalp irradiation) markedly raises risk, often producing higher-grade, multiple tumors decades later—while focused radiosurgery also treats inaccessible ones."
  - target: 01-human/07-system/glioblastoma
    relation: connects-to
    note: "Meningioma and glioblastoma are the two commonest primary brain tumors but opposite: meningioma is an extra-axial, dural-based, usually benign and resectable tumor of arachnoid cells, while glioblastoma is intra-axial, diffusely infiltrative and malignant—distinguished on MRI."
  - target: 01-human/07-system/breast-cancer
    relation: connects-to
    note: "Meningioma and breast cancer are linked through hormones and co-occurrence: most meningiomas express progesterone (and some estrogen) receptors, grow in pregnancy and the luteal phase, and the two are epidemiologically associated—a breast-cancer history can accompany meningioma."
  - target: 01-human/07-system/chordoma
    relation: connects-to
    note: "Meningioma and chordoma are both slow-growing extra-axial tumors of the skull base and spine: meningioma arises from arachnoid cap cells, chordoma from notochord remnants in the clivus or sacrum—both treated by resection plus radiotherapy and prone to local recurrence."
  - target: 01-human/07-system/pcnsl
    relation: connects-to
    note: "Meningioma and primary CNS lymphoma can both appear as enhancing masses but differ: meningioma is an extra-axial dural tumor cured by resection, while PCNSL is an intra-axial B-cell lymphoma treated with methotrexate, not surgery—so location and biopsy decide."
  - target: 01-human/07-system/idh-mutant-glioma
    relation: connects-to
    note: "Meningioma and IDH-mutant glioma sit in opposite brain compartments: meningioma is extra-axial, dural-based and usually benign, while IDH-mutant glioma is intra-axial and infiltrative—MRI location (the dural tail) distinguishes the resectable from the diffuse."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "Meningiomas threaten the brain by compression, not invasion: arising from arachnoid cap cells of the meninges, they grow slowly and push on neurons and cortex, causing seizures and focal deficits—so symptoms come from mass effect, not infiltration of the brain."
  - target: 01-human/07-system/schwannomatosis
    relation: connects-to
    note: "Meningioma sits in the NF2/schwannomatosis tumor family: NF2 (merlin) loss drives sporadic meningiomas and the multiple meningiomas, schwannomas and ependymomas of NF2, so a young patient with several meningiomas should prompt NF2-spectrum genetic testing."
  - target: 01-human/03-molecular/estrogen
    relation: connects-to
    note: "Meningiomas are often hormone-responsive: many express progesterone and estrogen receptors, can enlarge during pregnancy or with hormonal therapy, and are commoner in women—so hormonal status influences their growth and is weighed in management."
  - target: 01-human/01-subatomic/proton
    relation: connects-to
    note: "Proton therapy refines radiation for meningioma: many sit at the skull base wrapped around nerves and vessels, so protons' sharp dose stop point delivers high dose to the tumor while sparing the adjacent brain, optic nerves and brainstem."
  - target: 01-human/04-cellular/fibroblast
    relation: connects-to
    note: "Some meningiomas are fibroblastic: arising from arachnoid cap cells, these benign tumors can take a spindle-cell, collagen-rich (fibroblastic) form, one of several histologic subtypes that, with grade and location, guide whether surgery alone or added radiation is needed."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "VEGF drives the brain swelling around meningiomas: tumor VEGF makes vessels leaky, producing the peritumoral edema that often causes symptoms more than the mass itself, so anti-VEGF bevacizumab is tried for edema and recurrent disease."
  - target: 01-human/03-molecular/sstr2
    relation: connects-to
    note: "Meningiomas light up with somatostatin imaging: they strongly express SSTR2, so 68Ga-DOTATATE PET pinpoints tumor and residual disease better than MRI alone, and somatostatin analogues are tried in tumors that recur after surgery and radiation."
  - target: 01-human/03-molecular/tert
    relation: connects-to
    note: "TERT marks the dangerous meningiomas: TERT promoter mutations reactivate telomerase and now define a higher WHO grade, flagging tumors likely to recur aggressively regardless of how benign they look under the microscope."
  - target: 01-human/04-cellular/osteoblast
    relation: connects-to
    note: "Meningiomas can remodel the overlying skull: en plaque tumors signal osteoblasts to thicken adjacent bone (hyperostosis), a radiologic clue to the diagnosis and a reason surgery sometimes must remove involved bone."
  - target: 01-human/03-molecular/smo
    relation: connects-to
    note: "A subset of meningiomas is driven by Hedgehog through SMO: skull-base tumors often carry SMO mutations rather than NF2 loss, defining a molecular subgroup that—like basal cell carcinoma—might respond to smoothened inhibitors."
  - target: 01-human/03-molecular/cdkn2a
    relation: connects-to
    note: "CDKN2A deletion marks the most dangerous meningiomas: losing this tumor-suppressor now defines WHO grade 3 regardless of how the cells look, so molecular testing for CDKN2A reclassifies aggressive tumors that histology alone would underestimate."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Meningiomas are infiltrated mainly by macrophages: these tumor-associated immune cells are the dominant inflammatory population in the tumor and may support its growth, making the meningioma's immune niche a target of interest."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Meningiomas lay down calcium as psammoma bodies: these concentric calcified whorls are a histologic hallmark and make many meningiomas visibly calcified on imaging, a clue that helps distinguish them from other brain tumors."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "Some meningiomas are driven by AKT mutations: recurrent AKT1 changes switch on the PI3K-AKT-mTOR growth pathway in non-NF2 tumors, defining a molecular subgroup that AKT and mTOR inhibitors are being tested against."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Meningiomas largely evade cytotoxic T cells: beyond their dominant macrophages, they keep a T-cell-poor, immunosuppressive microenvironment, which is part of why checkpoint immunotherapy has had limited success in the tumor."
  - target: 01-human/06-organ/eye
    relation: connects-to
    note: "Meningiomas can blind through the eye: those arising on the optic nerve sheath or near the orbit compress the nerve and push the eye forward (proptosis), causing slow, painless vision loss."
  - target: 01-human/02-atomic/phosphorus
    relation: connects-to
    note: "Meningiomas calcify with calcium phosphate: their hallmark psammoma bodies are concentric whorls of calcium-phosphate mineral, a histologic signature also visible as flecks of calcification on imaging."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "Meningiomas are vascular tumors fed by endothelial cells: they recruit a rich blood supply, giving the bright contrast enhancement and 'dural tail' seen on MRI, and making them prone to bleed during surgery."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy fingerprints meningiomas: their meningothelial cells interlock through elaborate interdigitating processes joined by desmosomes — an ultrastructural signature that confirms the diagnosis when light microscopy is ambiguous."
  - target: 01-human/03-molecular/pdgf
    relation: connects-to
    note: "Meningiomas run on a PDGF autocrine loop: the tumor cells make platelet-derived growth factor and carry its receptor, driving their own proliferation — a pathway studied as a target for the aggressive grades that resist surgery and radiation."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "When a meningioma defies expectation and metastasizes, the lung is its commonest destination: though nearly all are benign and stay local, malignant variants spread hematogenously, with pulmonary deposits the classic distant site."
  - target: 01-human/05-tissue/bone-marrow
    relation: connects-to
    note: "Meningiomas can thicken the skull they sit against: en plaque tumors provoke reactive hyperostosis of the overlying bone, and some arise within the marrow-bearing skull itself as intraosseous meningiomas."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "Rarely a meningioma breaks through to the scalp: extracranial extension or a primary cutaneous meningioma forms a firm scalp nodule, the tumor reaching the skin from the meninges beneath the skull."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "If a malignant meningioma spreads, the liver is among its targets: after the lungs, hematogenous metastases can lodge in the liver and bone, the unusual distant spread of an aggressive grade."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "Antibodies grade and target the tumor: EMA, SSTR2, and progesterone-receptor stains confirm a meningioma and a high Ki-67 antibody index flags the aggressive grades, while the SSTR2 it displays makes it visible on DOTATATE imaging and a peptide-therapy target."
  - target: 01-human/04-cellular/astrocyte
    relation: connects-to
    note: "Though it grows outside the brain, a meningioma still irritates it: the slow dural mass compresses cortex and provokes peritumoral edema and reactive astrocyte gliosis in the underlying brain, the swelling that causes seizures and focal deficits."
  - target: 01-human/06-organ/placenta
    relation: connects-to
    note: "Pregnancy can wake a meningioma: many carry progesterone receptors and visibly enlarge under the hormone surge that the placenta drives, sometimes turning symptomatic in the third trimester and shrinking again after delivery."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "Hormones explain meningioma's female slant: it is far commoner in women, and long-term high-dose progestins like cyproterone acetate are now a recognized, dose-dependent cause — an iatrogenic link that has reshaped how these drugs are prescribed."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "Few cancers clot like a brain tumor patient: meningioma carries a high risk of deep-vein thrombosis and pulmonary embolism from the tumor's procoagulant tissue factor, the immobility around craniotomy, and steroid use, demanding careful prophylaxis."
  - target: 01-human/04-cellular/platelet
    relation: connects-to
    note: "Platelets feed the meningioma's clotting tendency: the tumor's tissue factor activates them into the hypercoagulable state behind its thrombosis risk, and they also help build the rich vasculature that makes these tumors bleed at surgery."
---

# Meningioma

## Overview

**Meningioma** is the most common primary intracranial tumor in adults, accounting for ~37-40% of all primary brain tumors. Approximately 40,000 new cases are diagnosed per year in the USA. Meningiomas arise from **arachnoidal cap cells** (meningothelial cells of the arachnoid layer) and are most commonly benign (WHO grade 1); however, grade 2 (atypical) and grade 3 (anaplastic) variants carry significant morbidity and mortality. The female-to-male ratio is ~2-3:1 for grade 1 (suggesting hormonal influence via progesterone receptor expression), equalizing at grade 2 and reversing at grade 3 (~1.5:1 M:F for grade 3).

**Epidemiology and risk factors:**
- **Radiation**: prior cranial or head/neck radiation → radiation-induced meningioma at latency 10-35 years; higher incidence of grade 2-3; multiple synchronous lesions
- **NF2 syndrome** (germline NF2 mutation): ~50% develop multiple meningiomas; usually grade 1-2; often skull base and spinal; bilateral vestibular schwannomas are the hallmark
- **Schwannomatosis** (SMARCB1 or LZTR1 germline): rare meningiomas
- **Female hormonal factors**: breast cancer and meningioma co-occurrence (shared PR/ER signaling); medroxyprogesterone acetate exposure → meningioma growth; postmenopausal HRT association
- **Incidental meningiomas** (~1-2% of adult brain MRIs): overwhelming majority grade 1; active surveillance unless symptomatic or growing

**WHO 2021 histological grades:**
- **Grade 1** (~75-80%): 15 recognized histological subtypes; fibrous, meningothelial, transitional, psammomatous (calcified whorl-forming), angiomatous, microcystic, lymphoplasmacyte-rich, secretory (CEA+ intracytoplasmic lumina), metaplastic; 5-year recurrence GTR ~7%, STR ~25%
- **Grade 2 / Atypical** (~18-22%): mitoses ≥4/10 HPF, OR brain invasion, OR ≥3 of: increased cellularity, small cells with high N:C ratio, prominent nucleoli, sheet-like growth, necrosis (not around blood vessels); 5-year recurrence GTR ~30-40%, STR ~60-70%
- **Grade 3 / Anaplastic** (~1-3%): mitoses ≥20/10 HPF, OR focal dedifferentiation (loss of meningothelial morphology), OR carcinoma/melanoma/high-grade sarcoma histology; 5-year OS ~35-60%
- **WHO 2021 molecular upgrades**: TERT promoter mutation → grade 3 regardless of histology; H3K27me3 loss by IHC (EZH2 mutation) → methylation class-defined aggressive meningioma treated as grade 3

## Structure

### Neuroanatomical locations

**Convexity (~25-30%)**: parasagittal, over cerebral hemispheres; most accessible surgically; >90% NF2-mutant

**Skull base (~30-35%)**: 
- Sphenoid ridge: medial (encasing carotid/MCA), lateral (more resectable)
- Sella/suprasellar: AKT1 E17K, TRAF7 mutations predominant; high PR expression; women >men (~4:1)
- Cerebellopontine angle (CPA): usually NF2-mutant; must distinguish from VS (VS has no arachnoid cap cells on histology)
- Olfactory groove: often large at diagnosis; anosmia (often unnoticed); AKT1 or NF2

**Posterior fossa (~20%)**: petroclival (POLR2A mutations), cerebellar convexity (NF2-mutant)

**Spinal (~5-10%)**: thoracic > cervical; women >> men; fibrous/psammomatous; NF2-mutant; usually grade 1; complete resection curative in ~90%

**Intraventricular (~2%)**: trigone of lateral ventricle; often large, difficult resection; NF2-mutant

### WHO 2021 Molecular classification

DNA methylation profiling (Nassiri 2021) [^nassiri-2021-meningioma-classification] defines **6 methylation classes** that predict recurrence risk better than histologic grade alone:

| Methylation class | Molecular features | 12-year PFS | Key histology |
|---|---|---|---|
| Merlin-intact | NF2 intact; TRAF7/AKT1/KLF4/SMO | ~95% | Meningothelial/transitional/secretory |
| Immune-enriched | Lymphocyte-rich TME; NF2 varied | ~90% | Lymphoplasmacyte-rich |
| Hypermetabolic | High metabolic activity | ~80% | Varied |
| Merlin-lost | NF2 LOF, 22q loss | ~55% | Fibrous/transitional/grade 2 |
| CDKN2A-del | CDKN2A/B deletion | ~15% | Grade 2-3, anaplastic |
| TERT/EZH2 | TERT pC228T/C250T or EZH2/H3K27me3-loss | ~5% | Grade 3, anaplastic |

**Key molecular alterations by location:**
- **Convexity/parasagittal**: NF2 biallelic LOF (~70-75%); 22q deletion; CDKN2A/B deletion in grade 2-3
- **Skull base / meningothelial**: AKT1 E17K (~25-35% of non-NF2 skull base), TRAF7 (~50% of AKT1-mutant co-mutated), KLF4 K409Q (secretory meningioma), SMO (~5%), PIK3CA (~5%)
- **Petroclival**: POLR2A mutations (RNA Pol II largest subunit, WHO grade 1, non-recurrent)
- **Pediatric meningioma**: YAP1-MAML2 fusions, TRAF7 mutations; distinct biology from adult; often require molecular testing
- **Rhabdoid meningioma** (WHO grade 3): BAP1 mutations, SMARCB1 loss rare; H3K27me3 loss; worst OS (~15% 5-year)

## Function

### Normal arachnoid cap cell biology

Arachnoid cap cells are epithelioid cells forming arachnoid granulations (Pacchionian bodies) that protrude into dural sinuses → facilitate CSF resorption into venous blood via vesicular transcytosis. Normal arachnoid cap cells:
- Express vimentin, EMA, PR (progesterone receptor), somatostatin receptors (SSTR2-5) — the latter explaining octreotide uptake on PET
- Form whorls → psammoma bodies (calcium deposition within necrotic whorl centers)
- Are highly adherent and contact-inhibited (NF2-Hippo pathway active in normal state)
- Do not cross the dura (making meningiomas non-infiltrative in grade 1)

Meningioma genesis: NF2 LOF or oncogenic activation (AKT1 E17K, SMO) → Hippo off (NF2 pathway) or PI3K/mTOR on (AKT1) → unchecked proliferation while retaining arachnoid cap cell identity.

## Pathology

### Treatment

**Surgery:**
Maximal safe resection is the cornerstone; Simpson grading of resection:
- Simpson grade 1 (GTR + coagulation of dural attachment + bone excision): lowest recurrence
- Simpson grade 2 (GTR + coagulation): adequate for most convexity tumors
- Simpson grade 3 (GTR, no dural treatment): acceptable if dura not involved
- Simpson grade 4 (STR/debulking): deliberate STR for skull base to preserve neurovascular structures; followed by SRS or observation
- Simpson grade 5 (biopsy only): very rare; for inaccessible deep lesions

Surgical morbidity is location-dependent: skull base (CN palsy, CSF leak), parasagittal (venous thrombosis if SSS invaded), cavernous sinus (CN III/IV/VI/V1/V2; often intentionally subtotally resected).

**Stereotactic radiosurgery (SRS):**
- Gamma Knife / CyberKnife / LINAC-based SRS; single fraction 12-16 Gy (grade 1) or 15-18 Gy (grade 2-3)
- Grade 1 residual after STR: SRS achieves ~92-95% local control at 5 years
- Primary SRS (for small symptomatic meningiomas not amenable to surgery): 5-year control ~95%
- NF2-associated VS: SRS 11-13 Gy → 97% tumor control at 5 years; hearing preservation in ~50%
- Limitations: max diameter ~3-3.5 cm; proximity to optic apparatus, brainstem

**Fractionated radiotherapy (FSRT/IMRT/proton):**
- Grade 2 post-op STR or recurrent grade 1: FSRT 54 Gy/30 fx
- Grade 3 post-op: FSRT 60 Gy/30 fx ± boost; adjuvant RT regardless of extent of resection
- Proton for skull base (reduce dose to optic chiasm, brainstem, cochlea); PTCOG studies ongoing

**Bevacizumab:**
VEGF overexpression in meningioma (YAP target); Phase 2 COMBIT (Huang 2019, N=40): ORR 40%, PFS 18.7 months (vs historical 6 months); predominantly grade 2-3 refractory; not FDA-approved for meningioma; used off-label.

**Systemic therapies (investigational):**
- Nivolumab/pembrolizumab: ~10-15% ORR in grade 3; PD-L1 variable expression; low TMB limits immunotherapy
- Octreotide/pasireotide: SSTR2-positive meningiomas; octreotide PET (Ga-68-DOTATATE) for staging/recurrence; SSA as palliative therapy for symptom control but not proven anti-tumor in controlled trials
- Mifepristone (anti-progesterone): SWOG-S9005 Phase 3: no benefit in unresectable PR+ meningioma vs placebo; PR expression does not predict hormone-blocking response
- AKT inhibitors (capivasertib): AKT1 E17K meningioma → Phase 2 (ACNS1920 for NF2 with AKT1 mutation; Lumiere trial)
- mTOR inhibitors: everolimus for NF2-associated VS (REACT, off-label); CERN Foundation trials in recurrent grade 2-3 meningioma ongoing
- TEAD inhibitors (VT3989, IAG933, TED-347): Phase 1 in NF2-null mesothelioma (most advanced) → expansion into NF2-null meningioma anticipated
- CDK4/6 inhibitors (palbociclib): CDKN2A-deleted grade 2-3 meningioma → Phase 2 (NCT04452214); CDKN2A/B deletions confer worst prognosis

**Prognosis:**
- WHO grade 1: 10-year OS ~90%; death often from co-morbidities
- WHO grade 2: 10-year OS ~65-70%; death from tumor progression or PTBE
- WHO grade 3: 5-year OS ~35-60%; median OS ~24-36 months from grade 3 diagnosis
- CDKN2A/B-deleted meningioma (any grade): median OS ~5 years
- TERT/EZH2 methylation class: median OS ~2-3 years

## Connections

- `connects-to` → **[NF2](../../03-molecular/nf2/README.md)** — NF2 biallelic LOF in ~50-60% sporadic meningioma; NF2 loss → Hippo inactivation → YAP/TAZ nuclear → TEAD-driven proliferation; NF2-mutant meningiomas are convexity-predominant; germline NF2 → bilateral VS, meningiomas, ependymomas; TEAD inhibitors in Phase 1 trials.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — AKT1 E17K (~10-12% skull base meningioma, grade 1) directly activates mTORC1/mTORC2; NF2 loss → Hippo off → YAP/TAZ nuclear → upstream mTOR activators; mTOR inhibitors (everolimus/sirolimus) in NF2 syndrome VS (REACT trial, 2012): volumetric reduction of VS in 30-44% of patients.
- `connects-to` → **[EGFR](../../03-molecular/egfr/README.md)** — AKT1 E17K and NF2 loss both engage EGFR/ErbB signaling in meningioma; NF2-null → ErbB2 surface overexpression → sustained RAS/MAPK; erlotinib and gefitinib explored in recurrent meningioma with modest activity; ErbB2 amplification is rare in meningioma.
- `connects-to` → **[PTEN](../../03-molecular/pten/README.md)** — PTEN loss in ~10-15% meningioma; NF2 and PTEN both suppress PI3K/AKT/mTOR → NF2+PTEN co-loss is synergistic; AKT1 E17K (skull base meningioma, ~10-12%) activates PI3K/mTOR without PTEN loss; mTOR inhibitors target the convergent PI3K/mTOR axis in meningioma.
- `connects-to` → **[Brain](../../06-organ/brain/README.md)** — Meningioma is the most common intracranial tumor, arising not from brain but from arachnoid cap cells of the meninges; it compresses brain and cranial nerves, and location (convexity, skull base, parasagittal) dictates resectability and surgical morbidity more than grade.
- `connects-to` → **[Neurofibromatosis Type 2](../neurofibromatosis-type-2/README.md)** — Germline NF2 loss (neurofibromatosis type 2) predisposes to multiple meningiomas alongside bilateral vestibular schwannomas and ependymomas; sporadic meningiomas carry biallelic NF2 loss in ~50-60%, making merlin/Hippo inactivation the central driver in both settings.
- `connects-to` → **[Progesterone](../../03-molecular/progesterone/README.md)** — Grade 1 meningiomas show a 2-3:1 female predominance and express progesterone receptors, with growth during pregnancy and on medroxyprogesterone exposure; yet anti-progesterone mifepristone failed in Phase 3, so PR positivity does not predict hormone-blockade response.
- `connects-to` → **[Mesothelioma](../mesothelioma/README.md)** — Meningioma and mesothelioma are unrelated tumors united by one driver: biallelic NF2/merlin loss inactivates Hippo, freeing YAP/TAZ-TEAD to drive proliferation in ~50-60% of meningiomas and ~40% of mesotheliomas — making both lead indications for TEAD inhibitors now in trials.
- `connects-to` → **[YAP1](../../03-molecular/yap1/README.md)** — Meningioma growth runs through YAP: NF2/merlin loss releases YAP/TAZ to partner with TEAD and transcribe proliferative genes; this Hippo-YAP axis, not a classic oncogene, drives most meningiomas, and TEAD-palmitoylation inhibitors are the first targeted therapy in trials.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — Meningioma is the most common primary CNS tumor, but it arises from the meninges (arachnoid cap cells), not neural tissue — growing outside the brain and spinal cord and causing symptoms by compression; its dural-based, extra-axial location makes many curable by resection.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Ionizing radiation is the best-established environmental cause of meningioma: prior cranial radiotherapy (even low-dose scalp irradiation) markedly raises risk, often producing higher-grade, multiple tumors decades later—while focused radiosurgery also treats inaccessible ones.
- `connects-to` → **[Glioblastoma](../glioblastoma/README.md)** — Meningioma and glioblastoma are the two commonest primary brain tumors but opposite: meningioma is an extra-axial, dural-based, usually benign and resectable tumor of arachnoid cells, while glioblastoma is intra-axial, diffusely infiltrative and malignant—distinguished on MRI.
- `connects-to` → **[Breast Cancer](../breast-cancer/README.md)** — Meningioma and breast cancer are linked through hormones and co-occurrence: most meningiomas express progesterone (and some estrogen) receptors, grow in pregnancy and the luteal phase, and the two are epidemiologically associated—a breast-cancer history can accompany meningioma.
- `connects-to` → **[Chordoma](../chordoma/README.md)** — Meningioma and chordoma are both slow-growing extra-axial tumors of the skull base and spine: meningioma arises from arachnoid cap cells, chordoma from notochord remnants in the clivus or sacrum—both treated by resection plus radiotherapy and prone to local recurrence.
- `connects-to` → **[Primary CNS Lymphoma](../pcnsl/README.md)** — Meningioma and primary CNS lymphoma can both appear as enhancing masses but differ: meningioma is an extra-axial dural tumor cured by resection, while PCNSL is an intra-axial B-cell lymphoma treated with methotrexate, not surgery—so location and biopsy decide.
- `connects-to` → **[IDH-Mutant Glioma](../idh-mutant-glioma/README.md)** — Meningioma and IDH-mutant glioma sit in opposite brain compartments: meningioma is extra-axial, dural-based and usually benign, while IDH-mutant glioma is intra-axial and infiltrative—MRI location (the dural tail) distinguishes the resectable from the diffuse.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — Meningiomas threaten the brain by compression, not invasion: arising from arachnoid cap cells of the meninges, they grow slowly and push on neurons and cortex, causing seizures and focal deficits—so symptoms come from mass effect, not infiltration of the brain.
- `connects-to` → **[Schwannomatosis](../schwannomatosis/README.md)** — Meningioma sits in the NF2/schwannomatosis tumor family: NF2 (merlin) loss drives sporadic meningiomas and the multiple meningiomas, schwannomas and ependymomas of NF2, so a young patient with several meningiomas should prompt NF2-spectrum genetic testing.
- `connects-to` → **[Estrogen](../../03-molecular/estrogen/README.md)** — Meningiomas are often hormone-responsive: many express progesterone and estrogen receptors, can enlarge during pregnancy or with hormonal therapy, and are commoner in women—so hormonal status influences their growth and is weighed in management.
- `connects-to` → **[Proton](../../01-subatomic/proton/README.md)** — Proton therapy refines radiation for meningioma: many sit at the skull base wrapped around nerves and vessels, so protons' sharp dose stop point delivers high dose to the tumor while sparing the adjacent brain, optic nerves and brainstem.
- `connects-to` → **[Fibroblast](../../04-cellular/fibroblast/README.md)** — Some meningiomas are fibroblastic: arising from arachnoid cap cells, these benign tumors can take a spindle-cell, collagen-rich (fibroblastic) form, one of several histologic subtypes that, with grade and location, guide whether surgery alone or added radiation is needed.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — VEGF drives the brain swelling around meningiomas: tumor VEGF makes vessels leaky, producing the peritumoral edema that often causes symptoms more than the mass itself, so anti-VEGF bevacizumab is tried for edema and recurrent disease.
- `connects-to` → **[SSTR2](../../03-molecular/sstr2/README.md)** — Meningiomas light up with somatostatin imaging: they strongly express SSTR2, so 68Ga-DOTATATE PET pinpoints tumor and residual disease better than MRI alone, and somatostatin analogues are tried in tumors that recur after surgery and radiation.
- `connects-to` → **[TERT](../../03-molecular/tert/README.md)** — TERT marks the dangerous meningiomas: TERT promoter mutations reactivate telomerase and now define a higher WHO grade, flagging tumors likely to recur aggressively regardless of how benign they look under the microscope.
- `connects-to` → **[Osteoblast](../../04-cellular/osteoblast/README.md)** — Meningiomas can remodel the overlying skull: en plaque tumors signal osteoblasts to thicken adjacent bone (hyperostosis), a radiologic clue to the diagnosis and a reason surgery sometimes must remove involved bone.
- `connects-to` → **[SMO](../../03-molecular/smo/README.md)** — A subset of meningiomas is driven by Hedgehog through SMO: skull-base tumors often carry SMO mutations rather than NF2 loss, defining a molecular subgroup that—like basal cell carcinoma—might respond to smoothened inhibitors.
- `connects-to` → **[CDKN2A](../../03-molecular/cdkn2a/README.md)** — CDKN2A deletion marks the most dangerous meningiomas: losing this tumor-suppressor now defines WHO grade 3 regardless of how the cells look, so molecular testing for CDKN2A reclassifies aggressive tumors that histology alone would underestimate.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Meningiomas are infiltrated mainly by macrophages: these tumor-associated immune cells are the dominant inflammatory population in the tumor and may support its growth, making the meningioma's immune niche a target of interest.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Meningiomas lay down calcium as psammoma bodies: these concentric calcified whorls are a histologic hallmark and make many meningiomas visibly calcified on imaging, a clue that helps distinguish them from other brain tumors.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — Some meningiomas are driven by AKT mutations: recurrent AKT1 changes switch on the PI3K-AKT-mTOR growth pathway in non-NF2 tumors, defining a molecular subgroup that AKT and mTOR inhibitors are being tested against.
- `connects-to` → **[Cytotoxic T Cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Meningiomas largely evade cytotoxic T cells: beyond their dominant macrophages, they keep a T-cell-poor, immunosuppressive microenvironment, which is part of why checkpoint immunotherapy has had limited success in the tumor.
- `connects-to` → **[Eye](../../06-organ/eye/README.md)** — Meningiomas can blind through the eye: those arising on the optic nerve sheath or near the orbit compress the nerve and push the eye forward (proptosis), causing slow, painless vision loss.
- `connects-to` → **[Phosphorus](../../02-atomic/phosphorus/README.md)** — Meningiomas calcify with calcium phosphate: their hallmark psammoma bodies are concentric whorls of calcium-phosphate mineral, a histologic signature also visible as flecks of calcification on imaging.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — Meningiomas are vascular tumors fed by endothelial cells: they recruit a rich blood supply, giving the bright contrast enhancement and 'dural tail' seen on MRI, and making them prone to bleed during surgery.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy fingerprints meningiomas: their meningothelial cells interlock through elaborate interdigitating processes joined by desmosomes — an ultrastructural signature that confirms the diagnosis when light microscopy is ambiguous.
- `connects-to` → **[PDGF](../../03-molecular/pdgf/README.md)** — Meningiomas run on a PDGF autocrine loop: the tumor cells make platelet-derived growth factor and carry its receptor, driving their own proliferation — a pathway studied as a target for the aggressive grades that resist surgery and radiation.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — When a meningioma defies expectation and metastasizes, the lung is its commonest destination: though nearly all are benign and stay local, malignant variants spread hematogenously, with pulmonary deposits the classic distant site.
- `connects-to` → **[Bone Marrow](../../05-tissue/bone-marrow/README.md)** — Meningiomas can thicken the skull they sit against: en plaque tumors provoke reactive hyperostosis of the overlying bone, and some arise within the marrow-bearing skull itself as intraosseous meningiomas.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — Rarely a meningioma breaks through to the scalp: extracranial extension or a primary cutaneous meningioma forms a firm scalp nodule, the tumor reaching the skin from the meninges beneath the skull.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — If a malignant meningioma spreads, the liver is among its targets: after the lungs, hematogenous metastases can lodge in the liver and bone, the unusual distant spread of an aggressive grade.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — Antibodies grade and target the tumor: EMA, SSTR2, and progesterone-receptor stains confirm a meningioma and a high Ki-67 antibody index flags the aggressive grades, while the SSTR2 it displays makes it visible on DOTATATE imaging and a peptide-therapy target.
- `connects-to` → **[Astrocyte](../../04-cellular/astrocyte/README.md)** — Though it grows outside the brain, a meningioma still irritates it: the slow dural mass compresses cortex and provokes peritumoral edema and reactive astrocyte gliosis in the underlying brain, the swelling that causes seizures and focal deficits.
- `connects-to` → **[Placenta](../../06-organ/placenta/README.md)** — Pregnancy can wake a meningioma: many carry progesterone receptors and visibly enlarge under the hormone surge that the placenta drives, sometimes turning symptomatic in the third trimester and shrinking again after delivery.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — Hormones explain meningioma's female slant: it is far commoner in women, and long-term high-dose progestins like cyproterone acetate are now a recognized, dose-dependent cause — an iatrogenic link that has reshaped how these drugs are prescribed.
- `connects-to` → **[Venous Thromboembolism](../venous-thromboembolism/README.md)** — Few cancers clot like a brain tumor patient: meningioma carries a high risk of deep-vein thrombosis and pulmonary embolism from the tumor's procoagulant tissue factor, the immobility around craniotomy, and steroid use, demanding careful prophylaxis.
- `connects-to` → **[Platelet](../../04-cellular/platelet/README.md)** — Platelets feed the meningioma's clotting tendency: the tumor's tissue factor activates them into the hypercoagulable state behind its thrombosis risk, and they also help build the rich vasculature that makes these tumors bleed at surgery.

[^brastianos-2013-akt1-meningioma]: Brastianos PK, Horowitz PM, Santagata S, et al. Genomic sequencing of meningiomas identifies oncogenic SMO and AKT1 mutations. *Nat Genet.* 2013;45(3):285-289. [doi:10.1038/ng.2526](https://doi.org/10.1038/ng.2526) · [PubMed 23334667](https://pubmed.ncbi.nlm.nih.gov/23334667/)
[^nassiri-2021-meningioma-classification]: Nassiri F, Liu J, Patil V, et al. A clinically applicable integrative molecular classification of meningiomas. *Nature.* 2021;597(7874):119-125. [doi:10.1038/s41586-021-03850-3](https://doi.org/10.1038/s41586-021-03850-3) · [PubMed 34385709](https://pubmed.ncbi.nlm.nih.gov/34385709/)
