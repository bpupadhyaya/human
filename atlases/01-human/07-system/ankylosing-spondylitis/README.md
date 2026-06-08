---
schema: human-scale-entry/v1
id: ankylosing-spondylitis
name: Ankylosing Spondylitis
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-07
summary: "Ankylosing spondylitis (AS; radiographic axSpA) is a chronic inflammatory spondyloarthropathy with sacroiliitis and spinal ankylosis; HLA-B27+ in ~90%; IL-17A/IL-23 and TNF pathways drive enthesitis; anti-TNF and anti-IL-17A (secukinumab, ixekizumab) are first-line therapy."
aliases: ["AS", "ankylosing spondylitis", "axial spondyloarthritis", "axSpA", "radiographic axSpA", "r-axSpA", "non-radiographic axSpA", "nr-axSpA", "Bechterew disease", "Marie-Strümpell disease", "spondyloarthropathy", "SpA", "BASDAI", "ASDAS", "bamboo spine"]
sources:
  - id: sieper-2015-ankylosing-spondylitis-review
    type: peer-reviewed
    cite: "Sieper J, Poddubnyy D. Ankylosing spondylitis. Lancet. 2017;390(10089):73-84."
    doi: "10.1016/S0140-6736(16)31591-4"
    pmid: "28110981"
    url: "https://doi.org/10.1016/S0140-6736(16)31591-4"
  - id: baeten-2015-secukinumab-as
    type: peer-reviewed
    cite: "Baeten D, Sieper J, Braun J, et al. Secukinumab, an Interleukin-17A Inhibitor, in Ankylosing Spondylitis. N Engl J Med. 2015;373(26):2534-2548."
    doi: "10.1056/NEJMoa1505066"
    pmid: "26699169"
    url: "https://doi.org/10.1056/NEJMoa1505066"
  - id: van-der-heijde-2018-adalimumab-as
    type: peer-reviewed
    cite: "van der Heijde D, Ramiro S, Landewé R, et al. 2016 update of the ASAS-EULAR management recommendations for axial spondyloarthritis. Ann Rheum Dis. 2017;76(6):978-991."
    doi: "10.1136/annrheumdis-2016-210770"
    pmid: "28087505"
    url: "https://doi.org/10.1136/annrheumdis-2016-210770"
cross_links:
  - target: 01-human/03-molecular/hla-b27
    relation: connects-to
    note: "HLA-B27 is the strongest genetic risk factor for AS (carried in ~90% of AS patients vs. 8% of Europeans); B*27:05 confers highest AS risk; HLA-B27 misfolding in ER → UPR → IL-23 → Th17/ILC3 → IL-17A → enthesitis; HLA-B27 also predicts uveitis and familial clustering."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "IL-17A is the central effector cytokine in AS enthesitis: ILC3 and Th17 cells at entheses produce IL-17A → RANKL + MMP → bone erosion + osteoblast activation → new bone (syndesmophytes); secukinumab (MEASURE-1) achieved ASAS20 ~61% vs. 29% placebo; ixekizumab also approved."
  - target: 01-human/03-molecular/rankl
    relation: connects-to
    note: "Entheseal IL-17A + TNF-α → RANKL on stromal cells → osteoclast activation → bone erosion at sacroiliac joints and vertebral corners; new bone formation (syndesmophytes) follows via WNT pathway; denosumab (anti-RANKL) reduces erosion but does not halt new bone formation."
  - target: 01-human/03-molecular/tnf-alpha
    relation: connects-to
    note: "TNF-α drives entheseal and synovial inflammation in AS; anti-TNF biologics (adalimumab, etanercept, infliximab, certolizumab, golimumab) achieve ASAS40 ~50-60% in active AS; TNF inhibition reduces MRI inflammation but does not halt radiographic progression (new bone)."
  - target: 01-human/07-system/psoriatic-arthritis
    relation: connects-to
    note: "Axial PsA and AS share HLA-B27, sacroiliitis imaging, and IL-17A/TNF-α pathobiology; distinguished by concurrent psoriasis, DIP involvement, and asymmetric periostitis; anti-IL-17A and anti-TNF are effective in both; IL-23 inhibitors diverge in efficacy."
---

# Ankylosing Spondylitis

## Overview

**Ankylosing spondylitis (AS)** — also termed **radiographic axial spondyloarthritis (r-axSpA)** in current classification — is a chronic, progressive, inflammatory arthritis primarily affecting the **axial skeleton** (sacroiliac joints and spine), leading to characteristic spinal fusion ("bamboo spine") in advanced disease [^sieper-2015-ankylosing-spondylitis-review]. AS is the prototypical member of the **spondyloarthropathy (SpA)** family, which also includes reactive arthritis, psoriatic arthritis (PsA), enteropathic arthritis (IBD-SpA), and undifferentiated SpA — united by shared genetic associations (HLA-B27), enthesitis, and characteristic extra-articular manifestations.

**Epidemiology:**
- Prevalence: 0.1-1.4% in European populations (population prevalence depends on HLA-B27 frequency)
- Male predominance: ~2-3:1 M:F (though females are often underdiagnosed with less classic radiographic changes)
- Age of onset: typically teens to 30s (90% of patients have symptom onset before age 45)
- The broader category of **axial SpA (axSpA)** includes non-radiographic axSpA (nr-axSpA) — active sacroiliac inflammation on MRI without established radiographic changes; prevalence ~0.5-1.5%

**Current classification framework:**
- **ASAS (Assessment of SpondyloArthritis international Society) axSpA criteria:** Imaging arm (sacroiliitis on MRI or X-ray + ≥1 SpA feature) OR clinical arm (HLA-B27+ + ≥2 SpA features); SpA features include IBP, arthritis, enthesitis, uveitis, dactylitis, psoriasis, IBD, family history, HLA-B27, elevated CRP, sacroiliitis
- **Modified New York criteria (for radiographic AS):** Sacroiliitis grade ≥2 bilateral or ≥3 unilateral PLUS ≥1 of: IBP ≥3 months (improves with exercise, not rest), restricted lumbar spine movement, limited chest expansion

## Structure

### Pathogenesis — enthesitis as the disease origin

AS originates at the **enthesis** — the site where tendons, ligaments, and joint capsules attach to bone. Enthesitis (entheseal inflammation) is the pathognomonic lesion of SpA and explains the clinical distribution of disease (sacroiliac joints, discovertebral junctions, Achilles tendon, plantar fascia).

**Enthesis anatomy and vulnerability:**
- Fibrocartilaginous entheses at the sacroiliac joint and discovertebral junction are anatomically avascular zones → normally immune-privileged
- Mechanical micro-trauma at entheses → local DAMP release → activation of resident macrophages and ILC3 cells
- Gut microbiome dysbiosis (60% of AS patients have subclinical intestinal inflammation) → bacterial antigen translocation → entheseal innate immune activation

**Cellular pathogenesis:**
1. HLA-B27 ER misfolding (in macrophages/DCs) → UPR → ↑IL-23 production
2. Gut dysbiosis → mucosal ILC3 and Th17 cell activation → systemic IL-17A and IL-22
3. Entheseal resident ILC3 cells (IL-17A+ CD3−) respond to IL-23 → local IL-17A/IL-22 burst
4. IL-17A + TNF-α → RANKL upregulation on bone stromal cells → osteoclast activation → bone erosion at sacroiliac joints and vertebral "corners" (Romanus lesions)
5. Paradoxically, post-erosion repair drives osteoblast-mediated new bone formation via **WNT pathway** (DKK1 suppression + WNT ligand upregulation) → syndesmophytes → eventual spinal fusion

**Radiographic progression:** Vertebral corner erosion → sclerosis (shiny corners) → ossification → syndesmophyte formation → spinal ankylosis ("bamboo spine" on plain film). TNF and IL-17A inhibition reduces inflammation markers but has less certain effect on radiographic progression — possibly because bone formation has its own autonomous WNT-driven program.

### Genetic architecture

- **HLA-B27:** >70% of AS heritability; OR ~90 — dominant genetic risk
- **ERAP1 and ERAP2:** ER aminopeptidases that trim peptides for HLA-I loading; ERAP1 polymorphisms modify AS risk specifically in HLA-B27+ background (epistasis)
- **IL23R, STAT3, TYK2, PTPN22, TNFRSF1A:** Additional GWAS loci confirming IL-23/Th17 and TNF pathway centrality
- Concordance in identical twins: ~60-65% (suggesting additional environmental factors, particularly gut microbiome)

## Function

### Clinical features

**Axial disease:**
- **Inflammatory back pain (IBP):** Insidious onset, age <45, morning stiffness >30 min, improves with exercise, worsens with rest; nocturnal pain waking patient in second half of night — characteristic SpA feature
- **Sacroiliitis:** Bilateral symmetric (AS) vs. asymmetric/unilateral (ReA, PsA); buttock pain; positive FABER/FADIR tests; MRI detects pre-radiographic bone marrow edema at SI joints
- **Spinal involvement:** Restriction of lumbar flexion (Schober test: <5 cm increase from 15 cm mark in full forward flexion is abnormal); cervical restriction; kyphotic deformity in advanced disease
- **Chest expansion:** Costovertebral joint involvement → restricted chest expansion (<5 cm in men); lung function may be mildly reduced

**Extra-articular manifestations (EAMs):**

| Manifestation | Prevalence | HLA-B27 relationship |
|---|---|---|
| **Anterior uveitis (AU)** | 20-30% lifetime | HLA-B27+ patients have more AU episodes; AU is the most common EAM |
| **Psoriasis** | 10% | Some HLA overlap with PsA; skin disease often mild |
| **IBD (Crohn's, UC)** | 5-10% overt; 60% subclinical | Subclinical gut inflammation in majority of AS; axSpA and IBD share IL-23R and other GWAS loci |
| **Cardiac** | ~2-10% | Aortic regurgitation (aortitis); conduction abnormalities (AV block) |
| **Respiratory** | <5% | Apical lung fibrosis (very late disease); restricted ventilation |
| **Osteoporosis** | 30-50% | Inflammation + immobility → vertebral fragility fractures (Anderson lesions) |

**Disease activity scores:**
- **BASDAI (Bath AS Disease Activity Index):** 0-10; based on patient-reported pain, fatigue, peripheral joint symptoms, enthesitis, morning stiffness; ≥4 = active disease requiring biologic therapy
- **ASDAS (AS Disease Activity Score):** Incorporates CRP (or ESR); ASDAS-CRP >2.1 = high disease activity; >3.5 = very high; preferred for clinical trials and biologic therapy decisions

**Imaging:**
- **Plain radiograph:** Gold standard for radiographic AS (sacroiliac grading, syndesmophytes, bamboo spine)
- **MRI sacroiliac joints (STIR or T2 fat-sat):** Active inflammation = bone marrow edema (BME) at SI joints — detects pre-radiographic disease; SPARCC score quantifies activity
- **Low-dose CT:** Precise structural damage assessment at SI joints (erosions, sclerosis, ankylosis)

## Pathology

### Therapies

**NSAIDs (first-line, all patients):**
- COX-1/COX-2 inhibition → ↓prostaglandin-driven entheseal inflammation; diclofenac, naproxen, indomethacin, celecoxib
- Continuous NSAID use associated with slowing of radiographic progression in some studies (controversial)
- Gastric protection (PPI) with non-selective NSAIDs

**Physical therapy:**
- Essential; maintains spinal mobility; swimming and extension exercises; disease-specific PT programs reduce BASDAI and improve function

**Anti-TNF biologics (biologic first-line):**
- **Indications:** BASDAI ≥4 + inadequate NSAID response ×2 NSAIDs over 4 weeks
- **Agents:** Adalimumab (Humira), etanercept (Enbrel), infliximab (Remicade), certolizumab pegol (Cimzia), golimumab (Simponi)
- **Efficacy:** ASAS40 response ~45-55%; rapid MRI inflammation reduction within weeks
- **Limitation:** Does not clearly reduce radiographic progression (new bone); reactivation of latent TB (screen before initiation)

**Anti-IL-17A biologics:**
- **Secukinumab (Cosentyx; anti-IL-17A mAb; Novartis):** MEASURE-1 (n=371): ASAS20 at 16 weeks — 61% (10 mg/kg IV load) vs. 29% placebo; ASAS40 ~41% vs. 12%; FDA approved 2016 for AS [^baeten-2015-secukinumab-as]
- **Ixekizumab (Taltz; anti-IL-17A mAb; Eli Lilly):** COAST-V (biologic-naive AS): ASAS40 52% vs. 18% placebo at week 16; FDA approved 2019 for AS
- **Bimekizumab (anti-IL-17A/F dual mAb):** Superior to secukinumab in PsA; Phase 3 in AS completed (higher ASAS40 responses)

**Anti-IL-23 biologics:**
- Risankizumab, guselkumab: approved in PsA; **disappointing results in AS** — SURPASS trial (risankizumab) did not meet primary endpoint at week 16; ongoing research into why IL-23 blockade is less effective despite its upstream role (possible IL-23-independent ILC3 IL-17A production at entheses)

**JAK inhibitors:**
- **Tofacitinib (Xeljanz; JAK1/3):** SELECT-AXIS-1: ASAS40 52% vs. 26% at week 16 in biologic-naive AS; FDA approved 2021 for AS
- **Upadacitinib (Rinvoq; JAK1):** SELECT-AXIS-2: ASAS40 64% vs. 44% (anti-TNF failure); FDA approved 2022 for AS; particularly useful for IL-17A/anti-TNF dual failures

**Biologic monitoring:**
- Screen for TB (IGRA/Mantoux), HBV, HCV, HIV before initiating biologics
- No live vaccines while on biologics
- Pregnancy: certolizumab pegol (anti-TNF) is preferred (minimal placental transfer); biologics generally held in 3rd trimester for other agents

## Connections

- `connects-to` → **[HLA-B27](../../03-molecular/hla-b27/README.md)** — HLA-B27 is the strongest genetic risk factor for AS (carried in ~90% of AS patients vs. 8% of Europeans); B*27:05 confers highest AS risk; HLA-B27 misfolding in ER → UPR → IL-23 → Th17/ILC3 → IL-17A → enthesitis; HLA-B27 also predicts uveitis and familial clustering.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — IL-17A is the central effector cytokine in AS enthesitis: ILC3 and Th17 cells at entheses produce IL-17A → RANKL + MMP → bone erosion + osteoblast activation → new bone (syndesmophytes); secukinumab (MEASURE-1) achieved ASAS20 ~61% vs. 29% placebo; ixekizumab also approved.
- `connects-to` → **[RANKL](../../03-molecular/rankl/README.md)** — Entheseal IL-17A + TNF-α → RANKL on stromal cells → osteoclast activation → bone erosion at sacroiliac joints and vertebral corners; new bone formation (syndesmophytes) follows via WNT pathway; denosumab (anti-RANKL) reduces erosion but does not halt new bone formation.
- `connects-to` → **[TNF-α](../../03-molecular/tnf-alpha/README.md)** — TNF-α drives entheseal and synovial inflammation in AS; anti-TNF biologics (adalimumab, etanercept, infliximab, certolizumab, golimumab) achieve ASAS40 ~50-60% in active AS; TNF inhibition reduces MRI inflammation but does not halt radiographic progression (new bone).
- `connects-to` → **[Psoriatic Arthritis](../psoriatic-arthritis/README.md)** — Axial PsA and AS share HLA-B27, sacroiliitis imaging, and IL-17A/TNF-α pathobiology; distinguished by concurrent psoriasis, DIP involvement, and asymmetric periostitis; anti-IL-17A and anti-TNF are effective in both; IL-23 inhibitors diverge in efficacy.

[^sieper-2015-ankylosing-spondylitis-review]: Sieper J, Poddubnyy D. Ankylosing spondylitis. *Lancet.* 2017;390(10089):73-84. [doi:10.1016/S0140-6736(16)31591-4](https://doi.org/10.1016/S0140-6736(16)31591-4) · [PubMed 28110981](https://pubmed.ncbi.nlm.nih.gov/28110981/)
[^baeten-2015-secukinumab-as]: Baeten D, Sieper J, Braun J, et al. Secukinumab, an Interleukin-17A Inhibitor, in Ankylosing Spondylitis. *N Engl J Med.* 2015;373(26):2534-2548. [doi:10.1056/NEJMoa1505066](https://doi.org/10.1056/NEJMoa1505066) · [PubMed 26699169](https://pubmed.ncbi.nlm.nih.gov/26699169/)
[^van-der-heijde-2018-adalimumab-as]: van der Heijde D, Ramiro S, Landewé R, et al. 2016 update of the ASAS-EULAR management recommendations for axial spondyloarthritis. *Ann Rheum Dis.* 2017;76(6):978-991. [doi:10.1136/annrheumdis-2016-210770](https://doi.org/10.1136/annrheumdis-2016-210770) · [PubMed 28087505](https://pubmed.ncbi.nlm.nih.gov/28087505/)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
