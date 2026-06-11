---
schema: human-scale-entry/v1
id: sjogrens-syndrome
name: Sjögren's Syndrome
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-07
summary: "Primary Sjögren's syndrome (pSS): systemic lymphocytic exocrinopathy; xerostomia, xerophthalmia, anti-Ro/SSA (80%); type I IFN signature; 40× elevated lymphoma risk; BAFF drives B-cell hyperactivation. Ianalumab (anti-BAFFR; TWINSS 2023) and rituximab are active biologics."
aliases: ["Sjögren's syndrome", "primary Sjögren's syndrome", "pSS", "Sjogrens", "sicca syndrome", "autoimmune exocrinopathy", "anti-Ro/SSA disease"]
sources:
  - id: shiboski-2017-sjogrens-criteria
    type: peer-reviewed
    cite: "Shiboski CH, Shiboski SC, Seror R, et al. 2016 American College of Rheumatology/European League Against Rheumatism classification criteria for primary Sjögren's syndrome. Arthritis Rheumatol. 2017;69(1):35-45."
    doi: "10.1002/art.39859"
    pmid: "27785888"
    url: "https://doi.org/10.1002/art.39859"
  - id: dorner-2023-ianalumab-twinss
    type: peer-reviewed
    cite: "Dörner T, Bowman SJ, Fox R, et al. Ianalumab (VAY736) in patients with primary Sjögren's syndrome: a multicentre, randomised, double-blind, placebo-controlled, phase 3 trial (TWINSS). Lancet. 2023;402(10400):477-489."
    doi: "10.1016/S0140-6736(23)00454-4"
    pmid: "37499657"
    url: "https://doi.org/10.1016/S0140-6736(23)00454-4"
  - id: seror-2019-eular-sjogrens
    type: peer-reviewed
    cite: "Seror R, Ravaud P, Mariette X, et al. EULAR Sjögren's Syndrome Disease Activity Index and Patient Reported Index. Ann Rheum Dis. 2019;78(11):1554-1560."
    doi: "10.1136/annrheumdis-2019-215024"
    pmid: "31462415"
    url: "https://doi.org/10.1136/annrheumdis-2019-215024"
cross_links:
  - target: 01-human/03-molecular/baff
    relation: connects-to
    note: "BAFF overexpressed in Sjögren's salivary glands → B-cell hyperactivation → anti-Ro/SSA production, ectopic GC formation, lymphoma risk; ianalumab (anti-BAFFR; TWINSS: ESSDAI –5.1 vs –2.7 at week 24; Lancet 2023) is the first Phase 3 positive biologic in pSS."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Type I IFN signature is present in ~75% of pSS patients and is highest in anti-Ro/SSA+ disease; pDCs in salivary glands produce IFN-α driven by TLR7 (ssRNA–anti-Ro complexes) and TLR9 (DNA–anti-La complexes); IFN signature correlates with disease activity and systemic features."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "IL-6 is elevated in Sjögren's glands and serum; drives plasma cell differentiation → anti-Ro/SSA and RF production; supports ectopic GC formation; salivary gland epithelial cells produce IL-6 locally → autocrine B-cell hyperactivation and lymphoma risk."
  - target: 01-human/03-molecular/cd20
    relation: connects-to
    note: "Rituximab (anti-CD20) depletes B cells in pSS; Phase 3 TEARS/TRACTISS had mixed results; used off-label for severe extraglandular pSS (vasculitis, cryoglobulinemia); CD20+ ectopic GC B cells are the key pathogenic and lymphoma-risk population in salivary glands."
  - target: 01-human/04-cellular/b-cell
    relation: connects-to
    note: "pSS B-cell hyperactivation (BAFF-driven) → anti-Ro/SSA, anti-La/SSB autoantibodies; ectopic germinal center formation in salivary glands; CD27+ memory B cells expanded; rituximab (anti-CD20) targets B cells in refractory pSS; 40× lymphoma risk from chronic B-cell stimulation."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: connects-to
    note: "Treg frequency and suppressive function reduced in pSS; Treg/Th17 imbalance drives salivary gland inflammation; impaired peripheral tolerance permits autoreactive B- and T-cell activation; low FoxP3+ Tregs in minor salivary gland biopsies correlate with disease activity scores."
  - target: 01-human/07-system/dlbcl
    relation: connects-to
    note: "pSS carries 15-40× population-level NHL risk; MALT lymphoma most common (parotid gland), progressing to DLBCL in ~10-15%; cryoglobulinemia, low C4, parotid swelling predict lymphoma transformation; R-CHOP for DLBCL; pSS-associated lymphoma has better prognosis than de novo DLBCL."
---

# Sjögren's Syndrome

## Overview

**Primary Sjögren's syndrome (pSS)** is a **systemic autoimmune disease** characterized by chronic lymphocytic infiltration of exocrine glands — primarily the salivary and lacrimal glands — leading to the hallmark symptoms of **xerostomia (dry mouth)** and **xerophthalmia (dry eyes)** [^shiboski-2017-sjogrens-criteria]. pSS is one of the most common autoimmune diseases, affecting approximately **0.1–0.6% of the adult population**, with a striking **female predominance (9:1 F:M)** and median onset in the 4th–5th decade.

Sjögren's syndrome can occur:
- **Primary (pSS):** Isolated autoimmune exocrinopathy without another connective tissue disease
- **Secondary (sSS):** Complicating another systemic autoimmune disease — most commonly RA, SLE, systemic sclerosis, and polymyositis/dermatomyositis; anti-Ro/SSA and anti-La/SSB are frequently shared

**Clinical significance:**
- **Systemic disease:** Despite the name, pSS causes significant extraglandular manifestations in 30-40% of patients — peripheral neuropathy, interstitial nephritis, interstitial lung disease, vasculitis, and cytopenias
- **Lymphoma:** pSS carries the **highest lymphoma risk of any autoimmune disease** — approximately 40× the general population risk; predominantly marginal zone B-cell lymphoma (MALT-type) arising in salivary glands or other extranodal sites
- **No FDA-approved biologic until recently:** Sjögren's had no approved biologic therapy — this changed with the positive TWINSS Phase 3 trial of **ianalumab (anti-BAFFR; Novartis; 2023)**, which met its primary endpoint

## Structure

### Immunopathogenesis

**Salivary gland infiltration:**
- Autoreactive CD4+ T cells (predominantly Th1 and Th17) and B cells infiltrate periductal regions of salivary (parotid, submandibular, minor labial) and lacrimal glands
- **Focal lymphocytic sialadenitis (FLS):** The pathological hallmark — dense lymphocytic aggregates (focus score ≥1 per 4 mm² of tissue) on minor salivary gland biopsy; lower lip biopsy is the diagnostic standard (Chisholm-Mason grading)
- **Ectopic germinal centers (EGC):** ~25% of pSS patients have organized lymphoid structures with B cell follicles, T follicular helper cells, and follicular dendritic cell networks forming *in situ* within glands → local autoantibody production and lymphomagenesis risk (EGC-positive patients have highest lymphoma risk)

**Type I IFN axis:**
- Anti-Ro complexes (Ro60/Ro52-bound RNA) or nucleic acid debris → FcγRIIa uptake by pDCs → TLR7 (ssRNA) and TLR9 (DNA–protein complexes) → IFN-α/β production
- **IFN signature** (elevated ISG expression: MX1, IFI44, IFIT3) present in ~75% of pSS, highest in anti-Ro/SSA+ patients; correlates with ESSDAI (systemic disease activity)
- IFN-α → BAFF production by DCs and macrophages → B-cell hyperactivation loop
- IFN-α → upregulates MHC class II → increased antigen presentation → T cell activation

**B-cell hyperactivation:**
- Polyclonal B-cell hyperactivation drives: hypergammaglobulinemia, rheumatoid factor (RF; ~60-70%), anti-Ro/SSA (~80%), anti-La/SSB (~50%), cryoglobulinemia (~10-15%)
- **BAFF elevation:** BAFF overexpression in glands and serum → autoreactive B cell survival → anti-Ro/SSA production → immune complex formation → TLR7 activation → IFN-α → more BAFF (amplification loop)
- Long-lived plasma cells in gland-associated niches maintain autoantibody titers independent of B-cell depletion

**Ductal epithelial cells — the "activated epithelium":**
- Salivary gland ductal epithelial cells in pSS are not innocent bystanders — they produce IL-6, IL-1β, CCL2, CXCL13, and BAFF; express MHC class II for antigen presentation; may present Ro/La antigens → autoreactive T cell activation
- Muscarinic receptor (M3R) dysfunction: Autoantibodies to M3R inhibit Gq-coupled Ca²⁺ → fluid secretion block → xerostomia independent of glandular destruction

### Autoantibody profile

| Antibody | Sensitivity | Specificity | Clinical notes |
|:---------|:------------|:------------|:---------------|
| **Anti-Ro/SSA (Ro60)** | ~80% | ~70% | TROVE2 protein; binds Ro-associated RNAs; neonatal lupus/CHB with anti-Ro52 |
| **Anti-Ro/SSA (Ro52/TRIM21)** | ~75% | ~60% | E3 ubiquitin ligase; also in myositis, SLE; associated with ILD in pSS/myositis |
| **Anti-La/SSB** | ~50% | ~90% | RNA-associated protein; usually concurrent with anti-Ro60; protective against SLE nephritis |
| **Rheumatoid factor (IgM-RF)** | ~60-70% | ~50% | IgM anti-IgG Fc; cryoglobulinemia; lymphoma risk marker |
| **ANA** | ~90% | Low | Speckled or homogeneous pattern; non-specific |
| **Anti-α-fodrin IgG** | ~50% | ~60% | Cytoskeletal protein; research use |
| **Anti-M3R (muscarinic)** | ~30-40% | Variable | Blocks glandular secretion; functional xerostomia mechanism |

### Genetic architecture

- **HLA:** HLA-DRB1*0301 and HLA-DQA1*0501 → anti-Ro/La production (shared risk with SLE); HLA-B08 (8.1 ancestral haplotype) in Europeans
- **IRF5 and STAT4:** Type I IFN pathway → elevated IFN production
- **BLK, BANK1:** B-cell signaling; shared risk with SLE
- **CXCR5:** Tfh/B-cell homing → ectopic GC formation

## Function

### Clinical manifestations

**Glandular features:**
- **Xerostomia (dry mouth):** Reduced salivary flow → dental caries (cervical caries), dysgeusia, dysphagia; parotid gland swelling (episodic or persistent) in ~50%
- **Xerophthalmia (dry eyes):** Keratoconjunctivitis sicca (KCS); foreign body sensation, photosensitivity, mucous discharge; corneal erosions, filamentary keratitis in severe cases
- **Other glands:** Nose (nasal dryness), trachea (dry cough), vagina (dyspareunia), skin (xeroderma)

**Extraglandular manifestations (~30-40%):**
- **Musculoskeletal:** Arthralgia (most common), non-erosive arthritis (25%); overlap with RA possible
- **Peripheral neuropathy:** Small fiber neuropathy (burning pain, autonomic dysfunction) is the most common neurological feature; sensory ataxic neuropathy (anti-Ro-associated, ganglionopathy); cranial neuropathy (trigeminal most common); mononeuritis multiplex in cryoglobulinemic vasculitis
- **Renal:** Tubulointerstitial nephritis (TIN; 5-10%): type 1 (distal) renal tubular acidosis (RTA) → hypokalemic paralysis, nephrolithiasis, nephrocalcinosis; membranous nephropathy, MPGN in cryoglobulinemia
- **Pulmonary:** ILD (5-10%); OP (organizing pneumonia), LIP (lymphoid interstitial pneumonia); pleural effusions; pulmonary hypertension (rare)
- **Lymphoma:** 5-10% lifetime risk (40× general population); predominantly **marginal zone B-cell lymphoma (MALT)** in salivary gland, stomach, lung; DLBCL transformation possible; risk factors: parotid swelling, cryoglobulinemia, C4 hypocomplementemia, palpable purpura, lymphadenopathy, CD4+ lymphopenia

**Disease activity assessment:**
- **ESSDAI (EULAR Sjögren's Syndrome Disease Activity Index):** Physician-assessed; 12 domains (pulmonary, renal, joint, skin, peripheral nervous system, CNS, lymphadenopathy, biological, glandular, constitutional, hematological, muscular); total 0-123; clinically active ≥5 [^seror-2019-eular-sjogrens]
- **ESSPRI (EULAR Sjögren's Syndrome Patient Reported Index):** Patient-reported; dryness, fatigue, pain; 0-10 each; mean ≥5 = patient-significant burden

### Diagnosis

**2016 ACR/EULAR Classification Criteria** (score ≥4 for classification) [^shiboski-2017-sjogrens-criteria]:

| Item | Weight |
|:-----|:-------|
| Anti-Ro/SSA positive | 3 |
| Labial salivary gland biopsy: focal lymphocytic sialadenitis (focus score ≥1/4mm²) | 3 |
| Ocular staining score (OSS) ≥5 | 1 |
| Schirmer test ≤5 mm/5 min in at least one eye | 1 |
| Unstimulated whole saliva flow ≤0.1 mL/min | 1 |

**Exclusion criteria:** Active hepatitis C (must test), IgG4-related disease (mimics Sjögren's with gland enlargement; biopsy shows IgG4+ plasma cells), sarcoidosis (granulomatous sialadenitis), prior radiation to head/neck, anticholinergic drugs, GvHD.

**Key diagnostic investigations:**
- **Schirmer test:** Strips of filter paper in the lower conjunctival fornix; ≤5 mm wetting in 5 min = abnormal
- **Rose Bengal / lissamine green / fluorescein staining:** Corneal + conjunctival staining; ocular surface damage score
- **Minor salivary gland biopsy (lower lip):** Gold standard for histological diagnosis; 3-5 glands sampled; focus score (lymphocyte foci >50 cells per 4 mm²)
- **Salivary scintigraphy / parotid ultrasound:** Echogenicity changes (inhomogeneous) correlated with disease severity

## Pathology

### Treatment

**Symptomatic — sicca:**
- **Artificial tears:** Preservative-free; mainstay for KCS; cyclosporine 0.05% eye drops (Restasis), lifitegrast 5% (Xiidra; LFA-1 inhibitor) reduce ocular inflammation → improve tear production
- **Pilocarpine (Salagen; muscarinic M1/M3 agonist):** Stimulates residual secretory function; 5 mg TID-QID; improves xerostomia and xerophthalmia; SE: sweating, urinary frequency, nausea
- **Cevimeline (Evoxac):** M1/M3 agonist; longer t½ than pilocarpine; 30 mg TID; approved for pSS xerostomia
- **Oral hygiene:** Fluoride supplementation, remineralizing toothpaste, regular dental care (cervical caries prevention)
- **Vaginal lubricants:** For dyspareunia

**Systemic — extraglandular disease:**
- **Hydroxychloroquine (HCQ):** Most commonly used DMARD in pSS; modestly reduces fatigue and arthralgia; limited evidence for systemic efficacy; TLR7/9 inhibition theoretically reduces type I IFN production; 200-400 mg/day
- **Corticosteroids:** For acute extraglandular flares (neuropathy, vasculitis, TIN, ILD); minimize long-term use
- **Immunosuppressants:**
  - Methotrexate, azathioprine: For arthritis and mild systemic disease
  - Mycophenolate mofetil: For ILD, renal disease
  - Cyclophosphamide: Severe vasculitis, cryoglobulinemia, rapidly progressive neuropathy

**Biologics:**
- **Rituximab (anti-CD20):** Widely used off-label; TEARS (2010) and TRACTISS (2015) Phase 3 trials failed primary endpoints (ESSPRI reduction); however, objective improvements in salivary flow and RF/IgG levels; used for severe extraglandular manifestations (vasculitis, cryoglobulinemia, lymphoma)
- **Ianalumab (VAY736; anti-BAFFR; Novartis):** Phase 3 **TWINSS** (N=290; pSS with ESSDAI ≥5; SC 300 mg Q4W vs. placebo): ESSDAI improvement at week 24 **–5.1 vs. –2.7** (p<0.001); ESSPRI improvement –2.1 vs. –1.3 (p<0.001); improved salivary flow and anti-Ro/SSA reduction [^dorner-2023-ianalumab-twinss]; first Phase 3 success in pSS; regulatory review ongoing
- **Abatacept (CTLA4-Ig; anti-CD80/86):** ASAP Phase 3 trial (2023): did NOT meet primary endpoint (ESSDAI ≥3 improvement); however, pre-specified subgroups showed some benefit
- **Iscalimab (anti-CD40L; Novartis):** Phase 2 trial (TWINSS Lite); CD40-CD40L blockade interrupts T–B cell cognate interaction → reduces GC formation; further development planned

**Cryoglobulinemia management:**
- Type II mixed cryoglobulinemia (RF-IgM + polyclonal IgG) in 10-15% → vasculitic purpura, peripheral neuropathy, glomerulonephritis; treat with rituximab ± plasmapheresis for severe manifestations; LMWH for thrombotic events; DVC (doxorubicin, vincristine, cyclophosphamide) for lymphoma

**Lymphoma surveillance:**
- Annual clinical exam; imaging if lymphadenopathy or parotid mass; PET/CT if lymphoma suspected; FNA or core biopsy; watch for B-symptoms, rapidly enlarging mass, rising LDH

## Connections

- `connects-to` → **[BAFF](../../03-molecular/baff/README.md)** — BAFF is overexpressed in pSS salivary glands → B-cell hyperactivation, ectopic GC formation, and anti-Ro/SSA production; ianalumab (anti-BAFFR; TWINSS Phase 3; ESSDAI –5.1 vs –2.7; Lancet 2023) is the first Phase 3-positive biologic in primary Sjögren's syndrome.
- `connects-to` → **[Type I Interferon](../../03-molecular/type-i-interferon/README.md)** — Type I IFN signature (~75% of pSS) is driven by TLR7/9 sensing of anti-Ro RNA complexes in pDCs; IFN-α upregulates BAFF and MHC class II → B- and T-cell activation loop; IFN signature correlates with anti-Ro/SSA positivity and systemic disease activity.
- `connects-to` → **[IL-6](../../03-molecular/il-6/README.md)** — IL-6 from salivary gland epithelial cells drives plasma cell differentiation → anti-Ro/SSA and RF production; supports ectopic GC formation; serum IL-6 correlates with hypergammaglobulinemia and RF titer in pSS.
- `connects-to` → **[CD20](../../03-molecular/cd20/README.md)** — Rituximab (anti-CD20) depletes B cells in pSS; Phase 3 TEARS/TRACTISS did not meet primary ESSPRI endpoint but improved objective salivary/lacrimal parameters; used for severe extraglandular pSS (cryoglobulinemic vasculitis, lymphoma); CD20+ ectopic GC B cells are the key pathogenic and lymphoma-risk population.
- `connects-to` → **[B Cell](../../04-cellular/b-cell/README.md)** — pSS B-cell hyperactivation (BAFF-driven) → anti-Ro/SSA, anti-La/SSB autoantibodies; ectopic germinal center formation in salivary glands; CD27+ memory B cells expanded; rituximab (anti-CD20) targets B cells in refractory pSS; 40× lymphoma risk from chronic B-cell stimulation.
- `connects-to` → **[Regulatory T Cell](../../04-cellular/regulatory-t-cell/README.md)** — Treg frequency and suppressive function reduced in pSS; Treg/Th17 imbalance drives salivary gland inflammation; impaired peripheral tolerance permits autoreactive B- and T-cell activation; low FoxP3+ Tregs in minor salivary gland biopsies correlate with disease activity scores.
- `connects-to` → **[DLBCL](../dlbcl/README.md)** — pSS carries 15-40× population-level NHL risk; MALT lymphoma most common (parotid gland), progressing to DLBCL in ~10-15%; cryoglobulinemia, low C4, parotid swelling predict lymphoma transformation; R-CHOP for DLBCL; pSS-associated lymphoma has better prognosis than de novo DLBCL.

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^shiboski-2017-sjogrens-criteria]: Shiboski CH, Shiboski SC, Seror R, et al. 2016 American College of Rheumatology/European League Against Rheumatism classification criteria for primary Sjögren's syndrome. *Arthritis Rheumatol.* 2017;69(1):35-45. [doi:10.1002/art.39859](https://doi.org/10.1002/art.39859) · [PubMed 27785888](https://pubmed.ncbi.nlm.nih.gov/27785888/)
[^dorner-2023-ianalumab-twinss]: Dörner T, Bowman SJ, Fox R, et al. Ianalumab (VAY736) in patients with primary Sjögren's syndrome: a multicentre, randomised, double-blind, placebo-controlled, phase 3 trial (TWINSS). *Lancet.* 2023;402(10400):477-489. [doi:10.1016/S0140-6736(23)00454-4](https://doi.org/10.1016/S0140-6736(23)00454-4) · [PubMed 37499657](https://pubmed.ncbi.nlm.nih.gov/37499657/)
[^seror-2019-eular-sjogrens]: Seror R, Ravaud P, Mariette X, et al. EULAR Sjögren's Syndrome Disease Activity Index and Patient Reported Index. *Ann Rheum Dis.* 2019;78(11):1554-1560. [doi:10.1136/annrheumdis-2019-215024](https://doi.org/10.1136/annrheumdis-2019-215024) · [PubMed 31462415](https://pubmed.ncbi.nlm.nih.gov/31462415/)
