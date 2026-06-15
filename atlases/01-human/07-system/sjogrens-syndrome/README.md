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
  - target: 01-human/07-system/systemic-sclerosis
    relation: connects-to
    note: "Sjögren's and systemic sclerosis are overlapping connective-tissue autoimmune diseases that often coexist and share a type-I-interferon signature, but Sjögren is a lymphocytic exocrine-gland disease causing sicca while SSc is a fibrosing vasculopathy — dryness versus scarring."
  - target: 01-human/06-organ/eye
    relation: connects-to
    note: "The eye bears the brunt of Sjögren's: lymphocytic destruction of lacrimal glands causes aqueous-deficient dry eye (keratoconjunctivitis sicca) — gritty, burning eyes with corneal damage on Schirmer testing — which with dry mouth forms the sicca complex that defines the disease."
  - target: 01-human/07-system/systemic-lupus-erythematosus
    relation: connects-to
    note: "Sjögren's and lupus are closely related autoimmune diseases sharing anti-Ro/SSA and anti-La/SSB antibodies and a type-I-interferon signature; secondary Sjögren commonly complicates lupus, and anti-Ro can cross the placenta to cause neonatal lupus and congenital heart block."
  - target: 01-human/07-system/rheumatoid-arthritis
    relation: connects-to
    note: "Sjögren's syndrome most often appears as secondary Sjögren's atop rheumatoid arthritis or lupus: shared autoimmune mechanisms extend inflammation to lacrimal and salivary glands, so any RA patient with dry eyes and mouth (sicca) is evaluated for the overlap."
  - target: 01-human/04-cellular/plasma-cell
    relation: connects-to
    note: "Sjögren's syndrome is a B-cell/plasma-cell-driven disease: BAFF-fueled clonal B and plasma cells make anti-Ro/La autoantibodies and hypergammaglobulinemia, and persistent germinal-center activity in salivary glands is what drives the high MALT-lymphoma risk."
  - target: 01-human/07-system/follicular-lymphoma
    relation: connects-to
    note: "Sjögren's syndrome carries the highest lymphoma risk of any autoimmune disease: chronic salivary B-cell activation predisposes mainly to MALT marginal-zone lymphoma but also to follicular and other B-cell lymphomas—so persistent parotid swelling demands biopsy."
  - target: 01-human/07-system/mantle-cell-lymphoma
    relation: connects-to
    note: "Sjögren's lymphomas differ from mantle cell lymphoma in origin: Sjögren's drives antigen-stimulated marginal-zone lymphomas in inflamed glands, whereas MCL is a t(11;14) cyclin-D1 tumor of naive B cells—both B-NHL, but one inflammation-driven, one translocation-driven."
  - target: 01-human/07-system/lymphatic-system
    relation: connects-to
    note: "Sjögren's syndrome is a lymphoproliferative disease of exocrine glands: lymphocytes infiltrate and destroy salivary and lacrimal glands, and the chronic lymphoid activation causing dryness also drives its lymphoma risk—tying it to lymphatic-system biology."
  - target: 01-human/07-system/dermatomyositis
    relation: connects-to
    note: "Sjögren's syndrome overlaps with connective-tissue autoimmune diseases like dermatomyositis: both share sicca symptoms, autoantibodies and sometimes myositis, and secondary Sjögren's often accompanies inflammatory myopathy—so an overlap syndrome must be considered."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "T helper cells orchestrate the gland destruction of Sjögren's: infiltrating CD4 T cells and the cytokines they drive (with B cells and interferon) attack salivary and lacrimal glands, so the autoimmune assault that dries eyes and mouth is T-cell-coordinated."
  - target: 01-human/06-organ/thyroid
    relation: connects-to
    note: "Sjögren's clusters with autoimmune thyroid disease: it frequently coexists with Hashimoto's thyroiditis, reflecting a shared tendency to organ-specific autoimmunity, so thyroid function is checked in Sjögren's patients who develop fatigue or weight change."
  - target: 01-human/05-tissue/peripheral-nerve
    relation: connects-to
    note: "Sjögren's commonly damages peripheral nerves: lymphocytic infiltration and vasculitis cause sensory neuropathy and sometimes ganglionopathy, so numbness and pain are frequent extra-glandular features—occasionally the presenting sign before sicca symptoms."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "Sjögren's affects the kidney as tubulointerstitial nephritis: lymphocytic infiltration of tubules causes distal renal tubular acidosis with hypokalemia and stones, a classic extra-glandular complication distinct from the glomerular disease of lupus."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "Sjögren's involves the lung as interstitial lung disease: lymphocytic infiltration (NSIP, LIP) and airway dryness cause cough and dyspnea, a leading cause of morbidity that overlaps the pulmonary fibrosis of related connective-tissue diseases."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "Beyond peripheral nerves, Sjögren's can strike the central nervous system: white-matter lesions may mimic multiple sclerosis and autonomic dysfunction worsens the dryness—so neurological disease ranges from brain to autonomic, not just sensory neuropathy."
  - target: 01-human/06-organ/placenta
    relation: connects-to
    note: "Sjögren's anti-Ro/SSA antibodies cross the placenta: they can cause neonatal lupus and congenital heart block in the fetus, so anti-Ro-positive pregnancies are monitored with fetal heart surveillance—an autoimmune disease reaching the next generation."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "Plasmacytoid dendritic cells fuel Sjögren's interferon signature: they pour out type I interferon that drives the autoimmune attack on exocrine glands, linking the disease's hallmark IFN signature to a specific immune cell."
  - target: 01-human/03-molecular/mhc-class-ii
    relation: connects-to
    note: "Sjögren's syndrome is HLA-associated: MHC class II HLA-DR/DQ variants shape presentation of the Ro and La autoantigens to T cells, the genetic basis for the anti-SSA/SSB antibodies that define the disease."
  - target: 01-human/03-molecular/acetylcholine
    relation: connects-to
    note: "Sjögren's dries glands by blocking acetylcholine: antibodies against the M3 muscarinic receptor stop acetylcholine from triggering saliva and tears, so beyond gland destruction the secretion machinery is jammed—why cholinergic drugs like pilocarpine help."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Falling complement warns of severe Sjögren's: low C3/C4 from immune-complex consumption marks aggressive disease and flags the patients at highest risk of progressing to lymphoma, making complement a prognostic blood test."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Sjögren's glands fill with immune cells including macrophages: lymphocytic foci and macrophages infiltrate and destroy the salivary and lacrimal glands, the histologic lesion seen on lip biopsy that confirms the diagnosis."
  - target: 01-human/02-atomic/potassium
    relation: connects-to
    note: "Sjogren's can drain potassium through the kidney: immune attack on the renal tubules causes distal renal tubular acidosis, which wastes potassium and can cause hypokalemic muscle paralysis—a striking renal manifestation of the disease."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "Sjogren's reaches the nervous system, including the brain: it can cause CNS lesions, cognitive change and cranial neuropathies beyond the peripheral nerve damage, so neurologic symptoms are part of its systemic reach."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Cytotoxic T cells help destroy the Sjogren's glands: alongside the B cells that drive the autoantibodies, CD8 T cells infiltrate and kill the salivary and lacrimal gland cells, contributing to the dryness that defines the disease."
  - target: 01-human/02-atomic/hydrogen
    relation: connects-to
    note: "Sjogren's acidifies the blood through the kidney: its attack on the renal tubules causes distal renal tubular acidosis—a failure to excrete hydrogen ions—so acid builds up despite normal lungs."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "Sjogren's dries and inflames the skin: beyond dry eyes and mouth, it parches the skin and can cause a cutaneous small-vessel vasculitis with palpable purpura, part of its systemic reach."
  - target: 01-human/05-tissue/germinal-center
    relation: connects-to
    note: "Sjogren's builds germinal centers where they don't belong: its inflamed salivary glands grow ectopic germinal centers, chronic B-cell factories that explain the syndrome's notable risk of MALT lymphoma."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Photons gauge Sjogren's dryness at its source: salivary gland ultrasound shows the patchy, pitted glands, and scintigraphy times how sluggishly they take up and release tracer — imaging that documents the failing secretory tissue behind the dry mouth."
  - target: 01-human/06-organ/pancreas
    relation: connects-to
    note: "Sjogren's is a disease of all exocrine glands, the pancreas included: the same lymphocytic attack that dries the mouth and eyes can scar the pancreas, causing exocrine insufficiency and overlapping with autoimmune pancreatitis."
  - target: 03-medicine/03-food/vitamin-d
    relation: connects-to
    note: "Vitamin D runs low in Sjogren's and seems to matter: deficiency is common and tracks with the peripheral neuropathy and the lymphoma risk that mark more severe disease, hinting at the vitamin's role in restraining the autoimmunity."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "Sjogren's is written in its autoantibodies: anti-Ro/SSA and anti-La/SSB are the serologic hallmarks used to diagnose it, and anti-Ro crossing the placenta can give the fetus congenital heart block — making the antibody a clinical signature in its own right."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "Sjogren's keeps autoimmune company in the liver: it overlaps notably with primary biliary cholangitis and autoimmune hepatitis, so dry eyes and mouth may arrive alongside the anti-mitochondrial antibodies and cholestasis of liver autoimmunity."
  - target: 01-human/04-cellular/erythrocyte
    relation: connects-to
    note: "The autoimmunity spills into the blood counts: Sjogren's commonly brings anemia and other cytopenias, from the anemia of chronic inflammation to occasional autoimmune hemolysis that strips red cells from the circulation."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "The same immune dysregulation can drop the neutrophils: a mild autoimmune neutropenia is common in Sjogren's, part of the cytopenia picture alongside the anemia and low platelets that reflect the disease's reach into the blood."
  - target: 01-human/06-organ/stomach
    relation: connects-to
    note: "Dryness and autoimmunity reach the gut: lost saliva makes swallowing hard and unprotected, while Sjogren's overlaps with autoimmune atrophic gastritis, thinning the stomach lining and impairing acid and intrinsic-factor secretion."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "Exocrine failure dries more than eyes and mouth: vaginal dryness and dyspareunia are common in Sjogren's, and the anti-Ro/La antibodies can cross the placenta to cause neonatal lupus and congenital heart block."
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
- `connects-to` → **[Systemic Sclerosis](../systemic-sclerosis/README.md)** — Sjögren's and systemic sclerosis are overlapping connective-tissue autoimmune diseases that often coexist and share a type-I-interferon signature, but Sjögren is a lymphocytic exocrine-gland disease causing sicca while SSc is a fibrosing vasculopathy — dryness versus scarring.
- `connects-to` → **[Eye](../../06-organ/eye/README.md)** — The eye bears the brunt of Sjögren's: lymphocytic destruction of lacrimal glands causes aqueous-deficient dry eye (keratoconjunctivitis sicca) — gritty, burning eyes with corneal damage on Schirmer testing — which with dry mouth forms the sicca complex that defines the disease.
- `connects-to` → **[Systemic Lupus Erythematosus](../systemic-lupus-erythematosus/README.md)** — Sjögren's and lupus are closely related autoimmune diseases sharing anti-Ro/SSA and anti-La/SSB antibodies and a type-I-interferon signature; secondary Sjögren commonly complicates lupus, and anti-Ro can cross the placenta to cause neonatal lupus and congenital heart block.
- `connects-to` → **[Rheumatoid Arthritis](../rheumatoid-arthritis/README.md)** — Sjögren's syndrome most often appears as secondary Sjögren's atop rheumatoid arthritis or lupus: shared autoimmune mechanisms extend inflammation to lacrimal and salivary glands, so any RA patient with dry eyes and mouth (sicca) is evaluated for the overlap.
- `connects-to` → **[Plasma Cell](../../04-cellular/plasma-cell/README.md)** — Sjögren's syndrome is a B-cell/plasma-cell-driven disease: BAFF-fueled clonal B and plasma cells make anti-Ro/La autoantibodies and hypergammaglobulinemia, and persistent germinal-center activity in salivary glands is what drives the high MALT-lymphoma risk.
- `connects-to` → **[Follicular Lymphoma](../follicular-lymphoma/README.md)** — Sjögren's syndrome carries the highest lymphoma risk of any autoimmune disease: chronic salivary B-cell activation predisposes mainly to MALT marginal-zone lymphoma but also to follicular and other B-cell lymphomas—so persistent parotid swelling demands biopsy.
- `connects-to` → **[Mantle Cell Lymphoma](../mantle-cell-lymphoma/README.md)** — Sjögren's lymphomas differ from mantle cell lymphoma in origin: Sjögren's drives antigen-stimulated marginal-zone lymphomas in inflamed glands, whereas MCL is a t(11;14) cyclin-D1 tumor of naive B cells—both B-NHL, but one inflammation-driven, one translocation-driven.
- `connects-to` → **[Lymphatic System](../lymphatic-system/README.md)** — Sjögren's syndrome is a lymphoproliferative disease of exocrine glands: lymphocytes infiltrate and destroy salivary and lacrimal glands, and the chronic lymphoid activation causing dryness also drives its lymphoma risk—tying it to lymphatic-system biology.
- `connects-to` → **[Dermatomyositis](../dermatomyositis/README.md)** — Sjögren's syndrome overlaps with connective-tissue autoimmune diseases like dermatomyositis: both share sicca symptoms, autoantibodies and sometimes myositis, and secondary Sjögren's often accompanies inflammatory myopathy—so an overlap syndrome must be considered.
- `connects-to` → **[T Helper Cell](../../04-cellular/t-helper-cell/README.md)** — T helper cells orchestrate the gland destruction of Sjögren's: infiltrating CD4 T cells and the cytokines they drive (with B cells and interferon) attack salivary and lacrimal glands, so the autoimmune assault that dries eyes and mouth is T-cell-coordinated.
- `connects-to` → **[Thyroid Gland](../../06-organ/thyroid/README.md)** — Sjögren's clusters with autoimmune thyroid disease: it frequently coexists with Hashimoto's thyroiditis, reflecting a shared tendency to organ-specific autoimmunity, so thyroid function is checked in Sjögren's patients who develop fatigue or weight change.
- `connects-to` → **[Peripheral Nerve](../../05-tissue/peripheral-nerve/README.md)** — Sjögren's commonly damages peripheral nerves: lymphocytic infiltration and vasculitis cause sensory neuropathy and sometimes ganglionopathy, so numbness and pain are frequent extra-glandular features—occasionally the presenting sign before sicca symptoms.
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — Sjögren's affects the kidney as tubulointerstitial nephritis: lymphocytic infiltration of tubules causes distal renal tubular acidosis with hypokalemia and stones, a classic extra-glandular complication distinct from the glomerular disease of lupus.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — Sjögren's involves the lung as interstitial lung disease: lymphocytic infiltration (NSIP, LIP) and airway dryness cause cough and dyspnea, a leading cause of morbidity that overlaps the pulmonary fibrosis of related connective-tissue diseases.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — Beyond peripheral nerves, Sjögren's can strike the central nervous system: white-matter lesions may mimic multiple sclerosis and autonomic dysfunction worsens the dryness—so neurological disease ranges from brain to autonomic, not just sensory neuropathy.
- `connects-to` → **[Placenta](../../06-organ/placenta/README.md)** — Sjögren's anti-Ro/SSA antibodies cross the placenta: they can cause neonatal lupus and congenital heart block in the fetus, so anti-Ro-positive pregnancies are monitored with fetal heart surveillance—an autoimmune disease reaching the next generation.
- `connects-to` → **[Dendritic Cell](../../04-cellular/dendritic-cell/README.md)** — Plasmacytoid dendritic cells fuel Sjögren's interferon signature: they pour out type I interferon that drives the autoimmune attack on exocrine glands, linking the disease's hallmark IFN signature to a specific immune cell.
- `connects-to` → **[MHC Class II](../../03-molecular/mhc-class-ii/README.md)** — Sjögren's syndrome is HLA-associated: MHC class II HLA-DR/DQ variants shape presentation of the Ro and La autoantigens to T cells, the genetic basis for the anti-SSA/SSB antibodies that define the disease.
- `connects-to` → **[Acetylcholine](../../03-molecular/acetylcholine/README.md)** — Sjögren's dries glands by blocking acetylcholine: antibodies against the M3 muscarinic receptor stop acetylcholine from triggering saliva and tears, so beyond gland destruction the secretion machinery is jammed—why cholinergic drugs like pilocarpine help.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Falling complement warns of severe Sjögren's: low C3/C4 from immune-complex consumption marks aggressive disease and flags the patients at highest risk of progressing to lymphoma, making complement a prognostic blood test.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Sjögren's glands fill with immune cells including macrophages: lymphocytic foci and macrophages infiltrate and destroy the salivary and lacrimal glands, the histologic lesion seen on lip biopsy that confirms the diagnosis.
- `connects-to` → **[Potassium](../../02-atomic/potassium/README.md)** — Sjogren's can drain potassium through the kidney: immune attack on the renal tubules causes distal renal tubular acidosis, which wastes potassium and can cause hypokalemic muscle paralysis—a striking renal manifestation of the disease.
- `connects-to` → **[Brain](../../06-organ/brain/README.md)** — Sjogren's reaches the nervous system, including the brain: it can cause CNS lesions, cognitive change and cranial neuropathies beyond the peripheral nerve damage, so neurologic symptoms are part of its systemic reach.
- `connects-to` → **[Cytotoxic T Cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Cytotoxic T cells help destroy the Sjogren's glands: alongside the B cells that drive the autoantibodies, CD8 T cells infiltrate and kill the salivary and lacrimal gland cells, contributing to the dryness that defines the disease.
- `connects-to` → **[Hydrogen](../../02-atomic/hydrogen/README.md)** — Sjogren's acidifies the blood through the kidney: its attack on the renal tubules causes distal renal tubular acidosis—a failure to excrete hydrogen ions—so acid builds up despite normal lungs.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — Sjogren's dries and inflames the skin: beyond dry eyes and mouth, it parches the skin and can cause a cutaneous small-vessel vasculitis with palpable purpura, part of its systemic reach.
- `connects-to` → **[Germinal Center](../../05-tissue/germinal-center/README.md)** — Sjogren's builds germinal centers where they don't belong: its inflamed salivary glands grow ectopic germinal centers, chronic B-cell factories that explain the syndrome's notable risk of MALT lymphoma.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Photons gauge Sjogren's dryness at its source: salivary gland ultrasound shows the patchy, pitted glands, and scintigraphy times how sluggishly they take up and release tracer — imaging that documents the failing secretory tissue behind the dry mouth.
- `connects-to` → **[Pancreas](../../06-organ/pancreas/README.md)** — Sjogren's is a disease of all exocrine glands, the pancreas included: the same lymphocytic attack that dries the mouth and eyes can scar the pancreas, causing exocrine insufficiency and overlapping with autoimmune pancreatitis.
- `connects-to` → **[Vitamin D (Calciferol)](../../../03-medicine/03-food/vitamin-d/README.md)** — Vitamin D runs low in Sjogren's and seems to matter: deficiency is common and tracks with the peripheral neuropathy and the lymphoma risk that mark more severe disease, hinting at the vitamin's role in restraining the autoimmunity.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — Sjogren's is written in its autoantibodies: anti-Ro/SSA and anti-La/SSB are the serologic hallmarks used to diagnose it, and anti-Ro crossing the placenta can give the fetus congenital heart block — making the antibody a clinical signature in its own right.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — Sjogren's keeps autoimmune company in the liver: it overlaps notably with primary biliary cholangitis and autoimmune hepatitis, so dry eyes and mouth may arrive alongside the anti-mitochondrial antibodies and cholestasis of liver autoimmunity.
- `connects-to` → **[Erythrocyte](../../04-cellular/erythrocyte/README.md)** — The autoimmunity spills into the blood counts: Sjogren's commonly brings anemia and other cytopenias, from the anemia of chronic inflammation to occasional autoimmune hemolysis that strips red cells from the circulation.
- `connects-to` → **[Neutrophil](../../04-cellular/neutrophil/README.md)** — The same immune dysregulation can drop the neutrophils: a mild autoimmune neutropenia is common in Sjogren's, part of the cytopenia picture alongside the anemia and low platelets that reflect the disease's reach into the blood.
- `connects-to` → **[Stomach](../../06-organ/stomach/README.md)** — Dryness and autoimmunity reach the gut: lost saliva makes swallowing hard and unprotected, while Sjogren's overlaps with autoimmune atrophic gastritis, thinning the stomach lining and impairing acid and intrinsic-factor secretion.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — Exocrine failure dries more than eyes and mouth: vaginal dryness and dyspareunia are common in Sjogren's, and the anti-Ro/La antibodies can cross the placenta to cause neonatal lupus and congenital heart block.

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^shiboski-2017-sjogrens-criteria]: Shiboski CH, Shiboski SC, Seror R, et al. 2016 American College of Rheumatology/European League Against Rheumatism classification criteria for primary Sjögren's syndrome. *Arthritis Rheumatol.* 2017;69(1):35-45. [doi:10.1002/art.39859](https://doi.org/10.1002/art.39859) · [PubMed 27785888](https://pubmed.ncbi.nlm.nih.gov/27785888/)
[^dorner-2023-ianalumab-twinss]: Dörner T, Bowman SJ, Fox R, et al. Ianalumab (VAY736) in patients with primary Sjögren's syndrome: a multicentre, randomised, double-blind, placebo-controlled, phase 3 trial (TWINSS). *Lancet.* 2023;402(10400):477-489. [doi:10.1016/S0140-6736(23)00454-4](https://doi.org/10.1016/S0140-6736(23)00454-4) · [PubMed 37499657](https://pubmed.ncbi.nlm.nih.gov/37499657/)
[^seror-2019-eular-sjogrens]: Seror R, Ravaud P, Mariette X, et al. EULAR Sjögren's Syndrome Disease Activity Index and Patient Reported Index. *Ann Rheum Dis.* 2019;78(11):1554-1560. [doi:10.1136/annrheumdis-2019-215024](https://doi.org/10.1136/annrheumdis-2019-215024) · [PubMed 31462415](https://pubmed.ncbi.nlm.nih.gov/31462415/)
