---
schema: human-scale-entry/v1
id: giant-cell-arteritis
name: Giant Cell Arteritis
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-07
summary: "Giant cell arteritis (GCA) is the most common primary vasculitis in adults >50; granulomatous inflammation of temporal arteries and aortic branches; IL-6 and IL-1β drive pathogenesis. Tocilizumab (anti-IL-6R; GiACTA; FDA May 2017) is the first approved steroid-sparing therapy."
aliases: ["GCA", "giant cell arteritis", "temporal arteritis", "cranial arteritis", "Horton disease", "polymyalgia rheumatica"]
sources:
  - id: stone-2017-giact
    type: peer-reviewed
    cite: "Stone JH, Tuckwell K, Dimonaco S, et al. Trial of tocilizumab in giant-cell arteritis. N Engl J Med. 2017;377(4):317-328."
    doi: "10.1056/NEJMoa1613849"
    pmid: "28745999"
    url: "https://doi.org/10.1056/NEJMoa1613849"
  - id: weyand-2014-gca-review
    type: peer-reviewed
    cite: "Weyand CM, Goronzy JJ. Clinical practice. Giant-cell arteritis and polymyalgia rheumatica. N Engl J Med. 2014;371(1):50-57."
    doi: "10.1056/NEJMcp1214926"
    pmid: "24988557"
    url: "https://doi.org/10.1056/NEJMcp1214926"
cross_links:
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "IL-1β, released by activated macrophages in the adventitia and media, amplifies vascular NF-κB activation and macrophage recruitment in GCA; anakinra and canakinumab (IL-1 blockers) are in Phase 2/3 investigation for GCA as steroid-sparing alternatives."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "IL-6 is the dominant systemic effector in GCA — drives CRP/ESR elevation, fever, and constitutional symptoms; tocilizumab (anti-IL-6R; GiACTA: 56% vs 18% sustained remission at 52 weeks; FDA May 2017) is the cornerstone biologic for GCA."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "GCA involves Th17 (IL-17A) and Th1 (IFN-γ) CD4+ T cell infiltrate in the arterial adventitia; IL-17A amplifies macrophage/neutrophil recruitment and intimal hyperplasia; secukinumab (anti-IL-17A) and upadacitinib (JAK1 inhibitor; SELECT-GCA) are under investigation."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "IFN-γ from Th1 CD4+ T cells drives macrophage activation → multinucleated giant cell formation and intimal hyperplasia in GCA; high IFN-γ in arterial tissue correlates with GCA activity and distinguishes GCA from Takayasu arteritis histologically."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "GCA is named for the multinucleated giant cells formed when IFN-γ-activated M1 macrophages fuse at the intima-media junction; these macrophages secrete IL-6, VEGF, PDGF, and IGF-1, driving the acute-phase response, neovascularization, and intimal hyperplasia."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "Adventitial CD4+ T cells drive the adaptive phase of GCA: Th1 cells secrete IFN-γ (macrophage activation, giant cells) and Th17 cells secrete IL-17A (constitutional symptoms); both arms resist steroids, motivating IL-6R (tocilizumab) and JAK (upadacitinib) blockade."
  - target: 01-human/04-cellular/smooth-muscle-cell
    relation: connects-to
    note: "Macrophage-derived PDGF and IGF-1 drive vascular smooth muscle cell migration from media to intima with myofibroblast proliferation → intimal hyperplasia → luminal occlusion → the ischemia behind headache, jaw claudication, and irreversible anterior ischemic optic neuropathy."
  - target: 01-human/07-system/anca-vasculitis
    relation: connects-to
    note: "Giant cell arteritis and ANCA vasculitis are vasculitides contrasted by vessel caliber: GCA strikes large arteries with granulomatous giant-cell inflammation, AAV small vessels with pauci-immune necrosis — poles of the vasculitis spectrum sharing IL-6-driven inflammation."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "GCA inflammation centers on the artery wall: macrophage VEGF drives neovascularization of the normally avascular media, while intimal endothelial and myofibroblast proliferation narrows the lumen, producing the ischemic optic neuropathy and jaw claudication that define it."
  - target: 01-human/07-system/stroke
    relation: connects-to
    note: "GCA of the vertebral and carotid arteries can cause posterior-circulation (vertebrobasilar) stroke — distinct from the more common anterior ischemic optic neuropathy; prompt high-dose glucocorticoids reduce this risk, making GCA a treatable cause of stroke in the elderly."
  - target: 01-human/06-organ/eye
    relation: connects-to
    note: "Sudden permanent blindness is the feared emergency of giant-cell arteritis: inflammatory occlusion of the posterior ciliary arteries causes anterior ischemic optic neuropathy, often after jaw claudication and amaurosis fugax; suspected GCA gets immediate high-dose steroids."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "Giant-cell arteritis is a large-vessel vasculitis of the cardiovascular system: granulomatous inflammation of the aorta and its branches can cause aneurysm, dissection and arm claudication years after the cranial phase, so long-term vascular imaging surveillance is recommended."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "Dendritic cells ignite giant-cell arteritis: resident vascular dendritic cells in the artery's adventitia activate and recruit the CD4+ T cells and macrophages that form the granulomas and giant cells, making them the proposed initiator of the arterial attack."
  - target: 01-human/07-system/rheumatoid-arthritis
    relation: connects-to
    note: "Giant cell arteritis and rheumatoid arthritis are both IL-6-driven autoimmune diseases of older adults that respond to tocilizumab: GCA inflames large arteries while RA destroys synovial joints—shared cytokine biology lets one biologic treat both."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "IL-12 helps polarize the T-cell response in giant cell arteritis: dendritic cells in the arterial wall secrete IL-12 to push T cells toward Th1, generating IFN-γ-producing cells whose granulomatous infiltrate, with giant cells, destroys the artery's elastic lamina."
  - target: 01-human/03-molecular/jak2
    relation: connects-to
    note: "JAK-STAT signaling is a therapeutic target in giant cell arteritis: the IL-6 and IFN-γ driving arterial inflammation act through JAK kinases, so JAK inhibitors are in trials to spare steroids—linking GCA to the node mutated in myeloproliferative disease."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "VEGF helps GCA both damage and compensate: inflammatory cytokines drive VEGF that promotes neovascularization in the inflamed artery wall, while ischemia downstream stimulates collateral vessels—so angiogenesis is part of both injury and response in GCA."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "Giant cell arteritis is a large-vessel disease that threatens the aorta: beyond the temporal artery, granulomatous inflammation can involve the aorta and its branches, causing thoracic aortic aneurysm and dissection years later—so GCA needs vascular surveillance."
  - target: 01-human/07-system/systemic-lupus-erythematosus
    relation: connects-to
    note: "Giant cell arteritis and lupus are both autoimmune but differ sharply: GCA is a granulomatous large-vessel vasculitis of the elderly driven by Th1/Th17 and IL-6, while SLE is an immune-complex multisystem disease of the young—contrasting mechanisms of autoimmunity."
---

# Giant Cell Arteritis

## Overview

**Giant cell arteritis (GCA)** is the **most common primary systemic vasculitis** in adults over 50 years, with a prevalence of approximately 200 per 100,000 in populations of Northern European ancestry. It is a **granulomatous, large-to-medium vessel vasculitis** predominantly affecting the extracranial branches of the carotid artery — especially the **temporal arteries** — as well as the **aorta and its primary branches** [^weyand-2014-gca-review].

GCA is a medical urgency: **permanent visual loss** occurs in 15–20% of untreated patients within days to weeks of symptom onset due to ischemic optic neuropathy. Immediate initiation of high-dose corticosteroids is mandatory before diagnostic confirmation. The FDA approval of **tocilizumab** (anti-IL-6R; GiACTA trial; May 2017) established the first biologic therapy for GCA and demonstrated the centrality of IL-6 in its pathogenesis [^stone-2017-giact].

**Key facts:**
- Age: virtually all patients >50; peak incidence 70–80 years; F:M ratio ~3:1
- Ethnicity: highest prevalence in Northern European (Scandinavian) populations; rare in East Asian populations
- **PMR overlap:** ~50% of GCA patients have concurrent polymyalgia rheumatica (PMR); 15–20% of isolated PMR patients develop GCA over time
- **Large-vessel involvement:** 20–40% of GCA patients have aortic or subclavian/axillary artery involvement detectable by PET-CT; aortic aneurysm risk 17× baseline

## Structure

### Classification and variants

| Subtype | Features |
|:--------|:---------|
| **Cranial GCA** | Temporal/superficial scalp arteries; jaw claudication; visual symptoms; most common presentation |
| **Large-vessel GCA (LV-GCA)** | Aorta, subclavian, axillary arteries; limb claudication; decreased pulses; PET-CT/MRA detectable; aortic aneurysm risk; may lack cranial symptoms |
| **Occult GCA** | FUO + elevated inflammatory markers; diagnosed incidentally on biopsy or PET-CT; no cranial/visual symptoms |
| **GCA + PMR** | ~50% overlap; PMR: symmetric proximal shoulder/pelvic girdle pain/stiffness >45 min, ESR >40; responds rapidly to lower prednisone doses (10-20 mg/day) than cranial GCA |

### Arterial anatomy preferentially targeted

GCA affects **medium and large elastic arteries** above the aortic bifurcation with a rich adventitial vasa vasorum — the hypothesized entry point for dendritic cells and T cells that initiate inflammation. Vessels commonly involved:
- **Temporal arteries** (superficial temporal branches of external carotid)
- **Posterior ciliary arteries** → ischemic optic neuropathy → blindness
- **Ophthalmic artery** → amaurosis fugax
- **Subclavian/axillary arteries** → arm claudication, subclavian steal
- **Aorta** → aneurysm (thoracic > abdominal in GCA)
- **Internal carotid spared** (no vasa vasorum in intradural segment)

## Function

### Normal temporal artery and aortic physiology disrupted in GCA

The temporal arteries supply scalp, temporalis muscle, and dura. In GCA, transmural granulomatous inflammation:
- **Narrows lumen** (intimal hyperplasia → myofibroblast proliferation) → ischemia → headache, jaw claudication, visual loss
- **Destroys media** → aneurysm formation (aortic and large vessel)
- **Activates endothelium** → VEGF → neovascularization (adventitial vessels visible on ultrasound — "halo sign")

## Pathology

### Pathogenesis: two-phase innate-adaptive model

**Phase 1 — Innate activation (adventitial gate):**
- Dendritic cells (pDCs and mDCs) resident in arterial adventitia are activated by an unidentified trigger → mature DCs express CD83, CD86
- Mature DCs produce CXCL9/CXCL10 (CXCR3 ligands) → recruit circulating CD4+ T cells to the arterial wall

**Phase 2 — Adaptive inflammation:**
- **Th1 arm (IFN-γ):** DCs → IL-12 → Th1 CD4+ T cells → IFN-γ → macrophage M1 activation → IL-1β, TNF-α, reactive oxygen species; IFN-γ correlates with vessel inflammation and visual symptoms
- **Th17 arm (IL-17A):** IL-6 + TGF-β → Th17 differentiation → IL-17A → neutrophil/macrophage amplification; IL-17A correlates with systemic constitutional symptoms
- **Macrophage effectors:** M1 macrophages fuse → **multinucleated giant cells** at intima-media junction; produce:
  - **IL-6** → systemic acute-phase response (CRP, ESR, fever, constitutional symptoms)
  - **VEGF** → adventitial neovascularization
  - **PDGF + IGF-1** → VSMC migration and proliferation → **intimal hyperplasia** → luminal occlusion → ischemia

**Skip lesions:** Segmental inflammation in temporal arteries → ~30% false-negative biopsy rate (requires ≥2 cm specimen).

### Clinical features

| Feature | Prevalence | Pathomechanism |
|:--------|:----------|:--------------|
| New headache (temporal, occipital) | ~65–70% | Temporal artery inflammation → pain |
| Jaw claudication | ~35–50% | Masseter ischemia (facial artery branch); pathognomonic for GCA |
| Scalp tenderness | ~40% | Superficial temporal and scalp artery inflammation |
| Visual symptoms (amaurosis fugax) | ~20–25% | Ophthalmic/posterior ciliary artery occlusion |
| Permanent visual loss | ~15–20% untreated | Anterior ischemic optic neuropathy (AION) |
| Constitutional (fever, fatigue, weight loss) | ~50% | IL-6/IL-1β → acute-phase response |
| PMR symptoms (shoulder/pelvic girdle stiffness) | ~50% | Proximal synovitis + periarticular inflammation |

**Visual loss is irreversible** — an ophthalmologic emergency. Start IV methylprednisolone 1 g/day × 3 days immediately when visual symptoms are present.

### Diagnostic workup

| Test | Findings | Notes |
|:-----|:---------|:------|
| ESR | >50 mm/h (often 80–120) | Elevated >95%; driven by fibrinogen (IL-1β/IL-6 dependent) |
| CRP | >10 mg/L (often >50 mg/L) | More sensitive than ESR; suppressed on tocilizumab (misleading) |
| Temporal artery biopsy (TAB) | Granulomatous transmural inflammation; giant cells; fragmentation of internal elastic lamina | ≥2 cm required; treat first to save vision |
| Ultrasound (temporal artery) | "Halo sign" — hypoechoic edema ring around lumen | Sensitivity ~75%, specificity ~83%; operator-dependent |
| PET-CT | FDG uptake in aorta/subclavian arteries | Best for large-vessel GCA; suppressed on corticosteroids within 3–4 days |
| MRA/CTA | Wall thickening and stenosis of temporal arteries + aorta | Alternative to TAB + large-vessel assessment |

### Treatment

**1. Corticosteroids (start immediately — before biopsy):**
- Cranial GCA without visual symptoms: prednisone 40–60 mg/day orally
- Visual symptoms or recent vision loss: IV methylprednisolone 1 g/day × 3 days → oral prednisone
- PMR without GCA: prednisone 15–20 mg/day
- Slow taper over 12–24 months; relapse in ~50% on taper requiring dose escalation

**2. Tocilizumab (Actemra; anti-IL-6R; Roche):** [^stone-2017-giact]
- **GiACTA Phase 3** (N=251; weekly SC tocilizumab 162 mg + 26-week prednisone taper vs. placebo + 26- or 52-week taper):
  - Weekly TCZ + 26-week taper: **56% sustained remission at week 52** (vs. 18% placebo 26-week; p<0.0001)
  - 50% of TCZ patients achieved sustained remission without any prednisone by week 52
  - TCZ significantly reduced flare rate and cumulative corticosteroid dose
- FDA approved **May 2017** for giant cell arteritis — the first FDA-approved biologic for GCA
- Dosing: SC 162 mg weekly or every 2 weeks (Q2W)
- Limitation: **CRP becomes unreliable** as disease activity biomarker on tocilizumab (IL-6 drives CRP; blocking IL-6R suppresses CRP regardless of disease activity)

**3. Aspirin (75–100 mg/day):** Reduces ischemic complications (visual loss, TIA/stroke) by ~50% in observational data; recommended as adjunct to corticosteroids in all GCA patients without contraindication.

**4. Emerging therapies:**
- **Upadacitinib** (JAK1 inhibitor; SELECT-GCA Phase 3; final results pending): targets JAK1-STAT signaling downstream of IL-6R, IL-17R, and IFN-γR; oral once-daily administration advantage
- **Secukinumab** (anti-IL-17A; Phase 2 trials): targets Th17 arm
- **Abatacept** (CTLA4-Ig; ABAACTA Phase 3): T cell co-stimulation blockade; did not meet primary endpoint in GCA (2023)
- **IL-1 blockade** (anakinra, canakinumab; Phase 2): emerging evidence for IL-1β role in vascular inflammation

## Connections

- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — IL-1β, released by activated macrophages in the adventitia and media, amplifies vascular NF-κB activation and macrophage recruitment in GCA; anakinra and canakinumab (IL-1 blockers) are in Phase 2/3 investigation for GCA as steroid-sparing alternatives.
- `connects-to` → **[IL-6](../../03-molecular/il-6/README.md)** — IL-6 is the dominant systemic effector in GCA — drives CRP/ESR elevation, fever, and constitutional symptoms; tocilizumab (anti-IL-6R; GiACTA: 56% vs 18% sustained remission at 52 weeks; FDA May 2017) is the cornerstone biologic for GCA.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — GCA involves Th17 (IL-17A) and Th1 (IFN-γ) CD4+ T cell infiltrate in the arterial adventitia; IL-17A amplifies macrophage/neutrophil recruitment and intimal hyperplasia; secukinumab (anti-IL-17A) and upadacitinib (JAK1 inhibitor; SELECT-GCA) are under investigation.
- `connects-to` → **[IFN-γ](../../03-molecular/ifn-gamma/README.md)** — IFN-γ from Th1 CD4+ T cells drives macrophage activation → multinucleated giant cell formation and intimal hyperplasia in GCA; high IFN-γ in arterial tissue correlates with GCA activity and distinguishes GCA from Takayasu arteritis histologically.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — GCA is named for the multinucleated giant cells formed when IFN-γ-activated M1 macrophages fuse at the intima-media junction; these macrophages secrete IL-6, VEGF, PDGF, and IGF-1, driving the acute-phase response, neovascularization, and intimal hyperplasia.
- `connects-to` → **[T Helper Cell](../../04-cellular/t-helper-cell/README.md)** — Adventitial CD4+ T cells drive the adaptive phase of GCA: Th1 cells secrete IFN-γ (macrophage activation, giant cells) and Th17 cells secrete IL-17A (constitutional symptoms); both arms resist steroids, motivating IL-6R (tocilizumab) and JAK (upadacitinib) blockade.
- `connects-to` → **[Smooth Muscle Cell](../../04-cellular/smooth-muscle-cell/README.md)** — Macrophage-derived PDGF and IGF-1 drive vascular smooth muscle cell migration from media to intima with myofibroblast proliferation → intimal hyperplasia → luminal occlusion → the ischemia behind headache, jaw claudication, and irreversible anterior ischemic optic neuropathy.
- `connects-to` → **[ANCA Vasculitis](../anca-vasculitis/README.md)** — Giant cell arteritis and ANCA vasculitis are vasculitides contrasted by vessel caliber: GCA strikes large arteries with granulomatous giant-cell inflammation, AAV small vessels with pauci-immune necrosis — poles of the vasculitis spectrum sharing IL-6-driven inflammation.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — GCA inflammation centers on the artery wall: macrophage VEGF drives neovascularization of the normally avascular media, while intimal endothelial and myofibroblast proliferation narrows the lumen, producing the ischemic optic neuropathy and jaw claudication that define it.
- `connects-to` → **[Stroke](../stroke/README.md)** — GCA of the vertebral and carotid arteries can cause posterior-circulation (vertebrobasilar) stroke — distinct from the more common anterior ischemic optic neuropathy; prompt high-dose glucocorticoids reduce this risk, making GCA a treatable cause of stroke in the elderly.
- `connects-to` → **[Eye](../../06-organ/eye/README.md)** — Sudden permanent blindness is the feared emergency of giant-cell arteritis: inflammatory occlusion of the posterior ciliary arteries causes anterior ischemic optic neuropathy, often after jaw claudication and amaurosis fugax; suspected GCA gets immediate high-dose steroids.
- `connects-to` → **[Cardiovascular system](../cardiovascular-system/README.md)** — Giant-cell arteritis is a large-vessel vasculitis of the cardiovascular system: granulomatous inflammation of the aorta and its branches can cause aneurysm, dissection and arm claudication years after the cranial phase, so long-term vascular imaging surveillance is recommended.
- `connects-to` → **[Dendritic Cell](../../04-cellular/dendritic-cell/README.md)** — Dendritic cells ignite giant-cell arteritis: resident vascular dendritic cells in the artery's adventitia activate and recruit the CD4+ T cells and macrophages that form the granulomas and giant cells, making them the proposed initiator of the arterial attack.
- `connects-to` → **[Rheumatoid Arthritis](../rheumatoid-arthritis/README.md)** — Giant cell arteritis and rheumatoid arthritis are both IL-6-driven autoimmune diseases of older adults that respond to tocilizumab: GCA inflames large arteries while RA destroys synovial joints—shared cytokine biology lets one biologic treat both.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — IL-12 helps polarize the T-cell response in giant cell arteritis: dendritic cells in the arterial wall secrete IL-12 to push T cells toward Th1, generating IFN-γ-producing cells whose granulomatous infiltrate, with giant cells, destroys the artery's elastic lamina.
- `connects-to` → **[JAK2](../../03-molecular/jak2/README.md)** — JAK-STAT signaling is a therapeutic target in giant cell arteritis: the IL-6 and IFN-γ driving arterial inflammation act through JAK kinases, so JAK inhibitors are in trials to spare steroids—linking GCA to the node mutated in myeloproliferative disease.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — VEGF helps GCA both damage and compensate: inflammatory cytokines drive VEGF that promotes neovascularization in the inflamed artery wall, while ischemia downstream stimulates collateral vessels—so angiogenesis is part of both injury and response in GCA.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — Giant cell arteritis is a large-vessel disease that threatens the aorta: beyond the temporal artery, granulomatous inflammation can involve the aorta and its branches, causing thoracic aortic aneurysm and dissection years later—so GCA needs vascular surveillance.
- `connects-to` → **[Systemic Lupus Erythematosus](../systemic-lupus-erythematosus/README.md)** — Giant cell arteritis and lupus are both autoimmune but differ sharply: GCA is a granulomatous large-vessel vasculitis of the elderly driven by Th1/Th17 and IL-6, while SLE is an immune-complex multisystem disease of the young—contrasting mechanisms of autoimmunity.

[^stone-2017-giact]: Stone JH, Tuckwell K, Dimonaco S, et al. Trial of tocilizumab in giant-cell arteritis. *N Engl J Med.* 2017;377(4):317-328. [doi:10.1056/NEJMoa1613849](https://doi.org/10.1056/NEJMoa1613849) · [PubMed 28745999](https://pubmed.ncbi.nlm.nih.gov/28745999/)
[^weyand-2014-gca-review]: Weyand CM, Goronzy JJ. Clinical practice. Giant-cell arteritis and polymyalgia rheumatica. *N Engl J Med.* 2014;371(1):50-57. [doi:10.1056/NEJMcp1214926](https://doi.org/10.1056/NEJMcp1214926) · [PubMed 24988557](https://pubmed.ncbi.nlm.nih.gov/24988557/)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
