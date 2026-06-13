---
schema: human-scale-entry/v1
id: anca-vasculitis
name: ANCA Vasculitis
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-07
summary: "ANCA vasculitis (GPA, MPA, EGPA): small-vessel necrotizing vasculitis; anti-PR3 or anti-MPO IgG primes neutrophils via C5a/C5aR1 → NET formation → endothelial injury. Cyclophosphamide/rituximab induction; avacopan (steroid-sparing; FDA Oct 2021) and rituximab maintenance."
aliases: ["ANCA vasculitis", "AAV", "GPA", "MPA", "EGPA", "granulomatosis with polyangiitis", "microscopic polyangiitis", "eosinophilic granulomatosis", "Wegener's granulomatosis", "Churg-Strauss syndrome", "pauci-immune vasculitis", "anti-PR3 vasculitis", "anti-MPO vasculitis"]
sources:
  - id: jayne-2021-avacopan-advocate
    type: peer-reviewed
    cite: "Jayne DRW, Merkel PA, Schall TJ, Bekker P. Avacopan for the Treatment of ANCA-Associated Vasculitis. N Engl J Med. 2021;384(7):599-609."
    doi: "10.1056/NEJMoa2021349"
    pmid: "33596356"
    url: "https://doi.org/10.1056/NEJMoa2021349"
  - id: stone-2010-rituximab-gpa-rave
    type: peer-reviewed
    cite: "Stone JH, Merkel PA, Spiera R, et al. Rituximab versus cyclophosphamide for ANCA-associated vasculitis. N Engl J Med. 2010;363(3):221-232."
    doi: "10.1056/NEJMoa0909905"
    pmid: "20647199"
    url: "https://doi.org/10.1056/NEJMoa0909905"
  - id: specks-2013-rituximab-anca-maintenance
    type: peer-reviewed
    cite: "Charles P, Terrier B, Perrodeau É, et al. Comparison of individually tailored versus fixed-schedule rituximab regimen to maintain ANCA-associated vasculitis remission. Ann Rheum Dis. 2018;77(8):1143-1149."
    doi: "10.1136/annrheumdis-2017-212862"
    pmid: "29549154"
    url: "https://doi.org/10.1136/annrheumdis-2017-212862"
  - id: yates-2022-anca-review
    type: peer-reviewed
    cite: "Yates M, Watts RA, Bajema IM, et al. EULAR/ERA-EDTA recommendations for the management of ANCA-associated vasculitis. Ann Rheum Dis. 2016;75(9):1583-1594."
    doi: "10.1136/annrheumdis-2016-209133"
    pmid: "27338776"
    url: "https://doi.org/10.1136/annrheumdis-2016-209133"
cross_links:
  - target: 01-human/03-molecular/c5ar1
    relation: connects-to
    note: "C5a primes neutrophils via C5aR1 → surface PR3/MPO → ANCA IgG crosslinking → NETosis + ROS → endothelial injury; avacopan (C5aR1 antagonist; ADVOCATE trial: 65.7% vs 54.9% sustained remission; FDA Oct 2021) blocks neutrophil priming."
  - target: 01-human/03-molecular/complement-c5
    relation: connects-to
    note: "Complement activation generates C5a in ANCA vasculitis; C5a–C5aR1 primes neutrophils for ANCA-triggered NETosis; C5b-9 MAC contributes to endothelial injury; avacopan (C5aR1) allows glucocorticoid sparing without inhibiting C5b-9-mediated pathogen defense."
  - target: 01-human/03-molecular/cd20
    relation: connects-to
    note: "Rituximab (anti-CD20) is non-inferior to cyclophosphamide for ANCA vasculitis induction (RAVE trial: 64% vs 53% complete remission; FDA Apr 2011 for GPA/MPA) and is preferred for maintenance; rituximab reduces ANCA-producing B cells and PR3/MPO autoantibody titers."
  - target: 01-human/03-molecular/immunoglobulin-g
    relation: connects-to
    note: "ANCA (anti-neutrophil cytoplasmic antibodies) are IgG autoantibodies (IgG3 > IgG1) against PR3 (cANCA; GPA) or MPO (pANCA; MPA/EGPA); ANCA IgG Fc engages FcγRIIa on neutrophils → full effector activation; ANCA titers correlate with disease activity and relapse risk."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "Neutrophils are the primary effector cells in ANCA vasculitis; ANCA IgG (anti-PR3 or anti-MPO) crosslinks surface PR3/MPO on C5a-primed neutrophils → FcγRIIa → exuberant NETosis + respiratory burst → fibrinoid necrosis of small vessel walls and pauci-immune crescentic GN."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "Crescentic pauci-immune GN in GPA/MPA → rapidly progressive kidney failure; untreated AAV → ESRD within weeks-months; avacopan (ADVOCATE) preserves eGFR significantly better than prednisone at 52 weeks; ANCA GN is a leading cause of vasculitis-related dialysis."
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "AAV renal involvement progresses to CKD in up to 40% at 5 years; ESRD in 20-25% over 10 years; creatinine at diagnosis and % crescents on biopsy predict CKD trajectory; avacopan eGFR advantage at 52 weeks may translate to reduced long-term CKD progression."
  - target: 01-human/07-system/giant-cell-arteritis
    relation: connects-to
    note: "ANCA vasculitis and giant cell arteritis sit at opposite ends of the vessel spectrum: AAV attacks small vessels with pauci-immune necrotizing inflammation, GCA the large arteries with granulomatous giant cells — contrasting poles classified by vessel caliber and histology."
  - target: 01-human/04-cellular/b-cell
    relation: connects-to
    note: "B cells are the source of ANCA: they become plasma cells secreting IgG against PR3 or MPO, which is why anti-CD20 rituximab (RAVE trial) — depleting B cells and lowering autoantibody titers — is non-inferior to cyclophosphamide for induction and preferred for maintenance."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "AAV is a pulmonary-renal syndrome: small-vessel inflammation in the alveolar capillaries causes diffuse alveolar hemorrhage (hemoptysis, hypoxemia) alongside crescentic glomerulonephritis, and GPA additionally produces necrotizing granulomas of the upper and lower airways."
  - target: 01-human/07-system/asthma
    relation: connects-to
    note: "Asthma defines one ANCA-vasculitis subtype: eosinophilic granulomatosis with polyangiitis (EGPA, Churg-Strauss) arises in patients with adult-onset asthma and eosinophilia who then develop vasculitis; only ~40% are ANCA-positive, and anti-IL-5 (mepolizumab) treats it."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "The skin is a common, accessible window on ANCA-vasculitis: small-vessel inflammation produces palpable purpura, livedo, nodules and ulcers, and a skin biopsy showing leukocytoclastic vasculitis helps confirm the diagnosis while sparing the patient an organ biopsy."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Macrophages build the granulomas of ANCA-vasculitis: in granulomatosis with polyangiitis, neutrophil activation and necrosis recruit macrophages that organize into the necrotizing granulomas of lung and sinuses, distinguishing GPA from non-granulomatous microscopic polyangiitis."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "ANCA vasculitis is not purely antibody-driven—T-helper cells orchestrate it: autoreactive Th1 and Th17 cells help B cells make ANCA and form GPA granulomas, so T-cell- and B-cell-directed therapies both work, and relapse tracks T-cell inflammation."
  - target: 01-human/04-cellular/plasma-cell
    relation: connects-to
    note: "Plasma cells make the pathogenic ANCA antibodies (anti-PR3, anti-MPO): these autoantibodies activate primed neutrophils to injure small vessels, and because long-lived plasma cells resist rituximab, persistent autoantibody helps explain relapse and refractory disease."
  - target: 01-human/07-system/hepatitis-b
    relation: connects-to
    note: "ANCA vasculitis must be distinguished from hepatitis-B-associated vasculitis: HBV classically causes polyarteritis nodosa—an immune-complex, ANCA-negative medium-vessel vasculitis—so vasculitis workup checks viral serologies, since antivirals treat HBV disease."
---

# ANCA Vasculitis

## Overview

**ANCA-associated vasculitis (AAV)** is a group of systemic autoimmune small-vessel vasculitides characterized by **anti-neutrophil cytoplasmic antibody (ANCA)** production and **pauci-immune necrotizing vasculitis** — vascular inflammation without immune complex deposition, distinguishing it from lupus nephritis or IgA nephropathy [^yates-2022-anca-review]. AAV encompasses three clinically distinct entities unified by ANCA serology and shared pathomechanism:

| Entity | Former name | ANCA specificity | Primary targets | Key features |
|:-------|:-----------|:----------------|:----------------|:------------|
| **GPA** | Wegener's | Anti-PR3 (cANCA, ~80%) | Upper/lower airways, kidneys | Granulomatous ENT disease, saddle nose, cavitating lung nodules |
| **MPA** | — | Anti-MPO (pANCA, ~60%) | Kidneys, lungs | Rapidly progressive GN; diffuse alveolar hemorrhage |
| **EGPA** | Churg-Strauss | Anti-MPO (pANCA, ~40%) | Lungs, heart, PNS, skin | Eosinophilia (>10%); asthma; cardiac involvement |

**Epidemiology:**
- Combined AAV prevalence: ~150–200/million; incidence ~20/million/year
- GPA most common in northern Europe; MPA more prevalent in Asia
- Age of onset: 50–70 years; slight male predominance
- 5-year survival before modern immunosuppression: <30%; with current treatment: ~80%

**ANCA biology:**
- **cANCA (cytoplasmic pattern):** Anti-PR3 (proteinase 3; encoded by *PRTN3*, chromosome 19p13.3); granular cytoplasmic staining by IIF; associated with GPA
- **pANCA (perinuclear pattern):** Anti-MPO (myeloperoxidase; encoded by *MPO*, chromosome 17q21-q23); perinuclear IIF pattern; associated with MPA and EGPA
- ANCA are IgG autoantibodies (predominantly IgG3) that bind neutrophil granule proteins translocated to the cell surface after cytokine priming

## Structure

### Disease phenotypes

**Granulomatosis with Polyangiitis (GPA):**
- **ENT involvement (>90%):** Chronic sinusitis, epistaxis, nasal septal perforation, saddle-nose deformity (cartilage destruction), subglottic stenosis (tracheal narrowing — life-threatening), otitis media/sensorineural hearing loss
- **Lung:** Pulmonary nodules (often cavitary; may be misdiagnosed as malignancy or infection), diffuse alveolar hemorrhage, pleuritis
- **Kidney:** Pauci-immune crescentic glomerulonephritis (rapidly progressive GN; proteinuria, hematuria, rising creatinine; no immune deposits on IF — pauci-immune)
- **Eye:** Scleritis, orbital pseudotumor (proptosis), episcleritis, retinal vasculitis
- **Skin:** Palpable purpura, ulcers (leukocytoclastic vasculitis)

**Microscopic Polyangiitis (MPA):**
- No granulomas; no upper airway disease
- Rapidly progressive GN (most common cause of dialysis in AAV)
- Pulmonary capillaritis → diffuse alveolar hemorrhage (hemoptysis, hypoxemia)
- Mononeuritis multiplex (vasculitic neuropathy)

**EGPA:**
- **Phase 1 (prodromal):** Allergic rhinitis, asthma (often severe, adult-onset)
- **Phase 2 (eosinophilic):** Peripheral eosinophilia (>10%, >1.5×10⁹/L), eosinophilic pneumonia, eosinophilic gastroenteritis
- **Phase 3 (vasculitic):** Mononeuritis multiplex, purpura, cardiac (eosinophilic myocarditis — major cause of mortality, ~50% of AAV deaths in EGPA)

### ANCA testing

**Indirect immunofluorescence (IIF):**
- cANCA: cytoplasmic granular pattern → send anti-PR3 ELISA
- pANCA: perinuclear pattern → send anti-MPO ELISA

**ELISA:** Anti-PR3 and anti-MPO; quantitative; correlates with disease activity; rising titer predicts relapse (but not reliably in all patients)

**Birmingham Vasculitis Activity Score (BVAS):** Validated composite disease activity score; guides treatment decisions

## Function

ANCA vasculitis causes injury through three parallel mechanisms:

1. **Neutrophil-mediated vascular necrosis** — ANCA IgG binds surface PR3/MPO on C5a-primed neutrophils → Fc receptor (FcγRIIa) crosslinking → exuberant respiratory burst + NETosis → endothelial damage → fibrinoid necrosis, thrombosis

2. **Granuloma formation (GPA)** — PR3 on macrophages activates CD4+ Th1 cells → IFN-γ → macrophage activation → granuloma assembly (epithelioid macrophages, giant cells, lymphocytes); granulomas destroy cartilage, bone, and tissue at ENT, orbital, and pulmonary sites

3. **Crescentic glomerulonephritis** — Glomerular capillary necrosis → fibrin + proliferating parietal epithelial cells form crescents; loss of glomerular filtration units → rapid GFR decline; without treatment → ESRD within weeks to months

## Pathology

### Two-hit pathomechanism (C5a + ANCA)

The prevailing model requires **two sequential stimuli**:

**Hit 1 — Complement-mediated neutrophil priming:**
- Low-level complement activation (from infection, DAMPs, or alternative pathway background) → C5a
- C5a binds **C5aR1** on neutrophils → Gαi → PI3K/ERK/p38 → cytoskeletal reorganization, surface PR3/MPO upregulation, adhesion molecule expression, primed respiratory burst

**Hit 2 — ANCA-mediated full activation:**
- ANCA IgG binds surface PR3 or MPO → FcγRIIa crosslinking + concomitant C5aR1 → synergistic activation → massive NETosis + respiratory burst
- NETs provide a template: citrullinated histones + PR3/MPO on NETs → amplify ANCA production (autoantigen spread) + activate endothelium (thrombosis)

**Complement evidence in human disease:**
- C3a and C5a elevated in urine and serum during active AAV
- Complement deposition identified in renal biopsies despite "pauci-immune" pattern (immunocomplex deposition absent, but terminal complement detectable)
- Avacopan (C5aR1 blocker) achieves remission comparable to prednisone — proving C5a/C5aR1 is the key inflammatory signal driving AAV [^jayne-2021-avacopan-advocate]

### EGPA — IL-5/IL-4 and eosinophil axis

EGPA is mechanistically distinct — eosinophils, not neutrophils, mediate tissue damage:
- IL-5 drives eosinophilopoiesis and survival; **mepolizumab** (anti-IL-5; MIRRA trial: relapse-free survival; FDA Sep 2017) is approved for EGPA
- Th2 cytokines (IL-4, IL-13) drive IgE production, airway remodeling, and eosinophil trafficking
- ANCA (anti-MPO) present in ~40% of EGPA (vasculitic phase) but absent in eosinophilic phase
- **Benralizumab** (anti-IL-5Rα): Phase 3 MANDARA trial (vs. mepolizumab) — showed similar efficacy; potential for deeper eosinophil depletion

## Treatment

### Remission induction

**Rituximab + glucocorticoids (preferred for severe GPA/MPA):**
- **RAVE trial** [^stone-2010-rituximab-gpa-rave]: Rituximab 375 mg/m² × 4 doses + glucocorticoids vs. cyclophosphamide + glucocorticoids; **64% complete remission (rituximab) vs. 53% (CYC)** at 6 months; non-inferior overall; superior in relapsing disease
- FDA approved rituximab for GPA and MPA: **April 2011**
- Mechanism: depletes PR3-specific and MPO-specific B cell clones + B cell precursors → reduces ANCA production; does NOT deplete plasma cells (ANCA titers fall slowly over months)

**Cyclophosphamide + glucocorticoids (alternative):**
- IV pulse CYC (15 mg/kg q3w × 3–6 pulses) preferred over oral CYC to reduce bladder toxicity
- Oral CYC 2 mg/kg/d for severe/refractory; cystitis, malignancy risk (mesna co-administration required for bladder protection)
- Largely replaced by rituximab in GPA; still used for severe MPA with renal involvement and for EGPA

**Avacopan + standard of care (glucocorticoid sparing):**
- **ADVOCATE trial** (N=331) [^jayne-2021-avacopan-advocate]: Avacopan (30 mg BID) vs. prednisone taper (60 mg/d tapered to 0 over 20 weeks) — both added to rituximab or CYC:
  - **Remission at week 26:** 72.3% (avacopan) vs. 70.1% (prednisone) — avacopan **non-inferior**
  - **Sustained remission at week 52:** **65.7% (avacopan) vs. 54.9% (prednisone)** — avacopan **superior** (p<0.05)
  - eGFR preservation at 52 weeks significantly better with avacopan
  - FDA approved for GPA and MPA: **October 2021**

**Plasma exchange (PLEX):** Previously used for rapidly progressive GN (serum creatinine >500 μmol/L or dialysis dependence); the PEXIVAS trial (2020) showed PLEX did NOT reduce ESRD or mortality → no longer routine standard of care

### Remission maintenance

**Rituximab maintenance (preferred):**
- Fixed schedule: 500 mg q6m × 2 years; or tailored to ANCA titer/B cell reconstitution
- **MAINRITSAN trial** showed rituximab superior to azathioprine for maintaining remission (5% vs 29% major relapse at 28 months)

**Azathioprine 2 mg/kg/d:** Alternative for patients who cannot receive rituximab; less effective than rituximab in PR3-ANCA patients

**Mycophenolate mofetil 3 g/d:** Second-line alternative

**EGPA-specific:** Mepolizumab (anti-IL-5; FDA Sep 2017) for relapsing/refractory EGPA; reduces oral glucocorticoid dependence

### Special considerations

- **Prophylaxis:** TMP-SMX for Pneumocystis jirovecii pneumonia during immunosuppression; osteoporosis prophylaxis during glucocorticoid therapy; bisphosphonate + calcium/vitamin D
- **Monitoring:** ANCA titers (imperfect; rising PR3-ANCA more predictive of relapse than rising MPO-ANCA); eGFR; urinalysis; BVAS
- **Relapse:** More common in GPA (50% at 5 years) than MPA; re-treat with rituximab preferred; escalate glucocorticoids acutely

## Connections

- `connects-to` → **[C5aR1](../../03-molecular/c5ar1/README.md)** — C5a primes neutrophils via C5aR1 → surface PR3/MPO translocation → ANCA IgG crosslinking → NETosis + ROS → endothelial injury; avacopan (C5aR1 antagonist; ADVOCATE: 65.7% vs 54.9% sustained remission; FDA Oct 2021) blocks neutrophil priming.
- `connects-to` → **[Complement C5](../../03-molecular/complement-c5/README.md)** — Complement activation generates C5a in AAV; C5a–C5aR1 primes neutrophils for ANCA-triggered NETosis; C5b-9 MAC contributes to endothelial injury; avacopan allows glucocorticoid sparing without inhibiting C5b-9-mediated pathogen defense.
- `connects-to` → **[CD20](../../03-molecular/cd20/README.md)** — Rituximab (anti-CD20) is non-inferior to cyclophosphamide for AAV induction (RAVE trial: 64% vs 53% remission; FDA Apr 2011 for GPA/MPA) and is preferred for maintenance; rituximab depletes ANCA-producing B cells and reduces PR3/MPO autoantibody titers.
- `connects-to` → **[Immunoglobulin G](../../03-molecular/immunoglobulin-g/README.md)** — ANCA are IgG autoantibodies (IgG3 > IgG1) against PR3 (cANCA; GPA) or MPO (pANCA; MPA/EGPA); ANCA IgG Fc engages FcγRIIa on neutrophils → full effector activation; ANCA titers correlate with disease activity and relapse risk.
- `connects-to` → **[Neutrophil](../../04-cellular/neutrophil/README.md)** — neutrophils are the primary effector cells in ANCA vasculitis; ANCA IgG crosslinks surface PR3/MPO on C5a-primed neutrophils → FcγRIIa → NETosis + respiratory burst → fibrinoid necrosis of small vessel walls and pauci-immune crescentic GN.
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — crescentic pauci-immune GN in GPA/MPA causes rapidly progressive kidney failure; untreated AAV → ESRD within weeks-months; avacopan (ADVOCATE) preserves eGFR significantly better than prednisone at 52 weeks; ANCA GN is a leading cause of vasculitis-related dialysis.
- `connects-to` → **[CKD](../../07-system/ckd/README.md)** — AAV renal involvement progresses to CKD in up to 40% at 5 years; ESRD in 20-25% over 10 years; creatinine at diagnosis and percentage crescents on biopsy predict CKD trajectory; avacopan eGFR advantage at 52 weeks may translate to reduced long-term CKD progression.
- `connects-to` → **[Giant Cell Arteritis](../giant-cell-arteritis/README.md)** — ANCA vasculitis and giant cell arteritis sit at opposite ends of the vessel spectrum: AAV attacks small vessels with pauci-immune necrotizing inflammation, GCA the large arteries with granulomatous giant cells — contrasting poles classified by vessel caliber and histology.
- `connects-to` → **[B Cell](../../04-cellular/b-cell/README.md)** — B cells are the source of ANCA: they become plasma cells secreting IgG against PR3 or MPO, which is why anti-CD20 rituximab (RAVE trial) — depleting B cells and lowering autoantibody titers — is non-inferior to cyclophosphamide for induction and preferred for maintenance.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — AAV is a pulmonary-renal syndrome: small-vessel inflammation in the alveolar capillaries causes diffuse alveolar hemorrhage (hemoptysis, hypoxemia) alongside crescentic glomerulonephritis, and GPA additionally produces necrotizing granulomas of the upper and lower airways.
- `connects-to` → **[Asthma](../asthma/README.md)** — Asthma defines one ANCA-vasculitis subtype: eosinophilic granulomatosis with polyangiitis (EGPA, Churg-Strauss) arises in patients with adult-onset asthma and eosinophilia who then develop vasculitis; only ~40% are ANCA-positive, and anti-IL-5 (mepolizumab) treats it.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — The skin is a common, accessible window on ANCA-vasculitis: small-vessel inflammation produces palpable purpura, livedo, nodules and ulcers, and a skin biopsy showing leukocytoclastic vasculitis helps confirm the diagnosis while sparing the patient an organ biopsy.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Macrophages build the granulomas of ANCA-vasculitis: in granulomatosis with polyangiitis, neutrophil activation and necrosis recruit macrophages that organize into the necrotizing granulomas of lung and sinuses, distinguishing GPA from non-granulomatous microscopic polyangiitis.
- `connects-to` → **[T Helper Cell](../../04-cellular/t-helper-cell/README.md)** — ANCA vasculitis is not purely antibody-driven—T-helper cells orchestrate it: autoreactive Th1 and Th17 cells help B cells make ANCA and form GPA granulomas, so T-cell- and B-cell-directed therapies both work, and relapse tracks T-cell inflammation.
- `connects-to` → **[Plasma Cell](../../04-cellular/plasma-cell/README.md)** — Plasma cells make the pathogenic ANCA antibodies (anti-PR3, anti-MPO): these autoantibodies activate primed neutrophils to injure small vessels, and because long-lived plasma cells resist rituximab, persistent autoantibody helps explain relapse and refractory disease.
- `connects-to` → **[Hepatitis B](../hepatitis-b/README.md)** — ANCA vasculitis must be distinguished from hepatitis-B-associated vasculitis: HBV classically causes polyarteritis nodosa—an immune-complex, ANCA-negative medium-vessel vasculitis—so vasculitis workup checks viral serologies, since antivirals treat HBV disease.

[^yates-2022-anca-review]: Yates M, Watts RA, Bajema IM, et al. EULAR/ERA-EDTA recommendations for the management of ANCA-associated vasculitis. *Ann Rheum Dis.* 2016;75(9):1583-1594. [doi:10.1136/annrheumdis-2016-209133](https://doi.org/10.1136/annrheumdis-2016-209133) · [PubMed 27338776](https://pubmed.ncbi.nlm.nih.gov/27338776/)
[^stone-2010-rituximab-gpa-rave]: Stone JH, Merkel PA, Spiera R, et al. Rituximab versus cyclophosphamide for ANCA-associated vasculitis. *N Engl J Med.* 2010;363(3):221-232. [doi:10.1056/NEJMoa0909905](https://doi.org/10.1056/NEJMoa0909905) · [PubMed 20647199](https://pubmed.ncbi.nlm.nih.gov/20647199/)
[^jayne-2021-avacopan-advocate]: Jayne DRW, Merkel PA, Schall TJ, Bekker P. Avacopan for the Treatment of ANCA-Associated Vasculitis. *N Engl J Med.* 2021;384(7):599-609. [doi:10.1056/NEJMoa2021349](https://doi.org/10.1056/NEJMoa2021349) · [PubMed 33596356](https://pubmed.ncbi.nlm.nih.gov/33596356/)
[^specks-2013-rituximab-anca-maintenance]: Charles P, Terrier B, Perrodeau É, et al. Comparison of individually tailored versus fixed-schedule rituximab regimen to maintain ANCA-associated vasculitis remission. *Ann Rheum Dis.* 2018;77(8):1143-1149. [doi:10.1136/annrheumdis-2017-212862](https://doi.org/10.1136/annrheumdis-2017-212862) · [PubMed 29549154](https://pubmed.ncbi.nlm.nih.gov/29549154/)

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
