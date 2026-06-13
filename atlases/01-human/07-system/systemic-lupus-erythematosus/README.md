---
schema: human-scale-entry/v1
id: systemic-lupus-erythematosus
name: Systemic Lupus Erythematosus
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-06
summary: "Systemic autoimmune disease from loss of tolerance to nucleic acid antigens; type I IFN signature and complement activation define pathogenesis. Anti-dsDNA and low complement are diagnostic. Hydroxychloroquine is mainstay; belimumab and anifrolumab are approved biologics."
aliases: ["SLE", "lupus", "systemic lupus", "lupus erythematosus", "LN", "lupus nephritis"]
sources:
  - id: tsokos-2011-sle-review
    type: peer-reviewed
    cite: "Tsokos GC. Systemic lupus erythematosus. N Engl J Med. 2011;365(22):2110-2121."
    doi: "10.1056/NEJMra1100359"
    pmid: "22129253"
    url: "https://doi.org/10.1056/NEJMra1100359"
  - id: furie-2011-belimumab
    type: peer-reviewed
    cite: "Furie R, Petri M, Zamani O, et al. A phase III, randomized, placebo-controlled study of belimumab, a monoclonal antibody that inhibits B lymphocyte stimulator, in patients with systemic lupus erythematosus. Arthritis Rheum. 2011;63(12):3918-3930."
    doi: "10.1002/art.30613"
    pmid: "22127708"
    url: "https://doi.org/10.1002/art.30613"
  - id: morand-2020-anifrolumab
    type: peer-reviewed
    cite: "Morand EF, Furie R, Tanaka Y, et al. Trial of anifrolumab in active systemic lupus erythematosus. N Engl J Med. 2020;382(3):211-221."
    doi: "10.1056/NEJMoa1912196"
    pmid: "31851795"
    url: "https://doi.org/10.1056/NEJMoa1912196"
cross_links:
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Complement deficiencies (C1q, C4) → impaired apoptotic cell clearance → nuclear antigen exposure → autoimmunity; C3/C4 consumption during active SLE flares is diagnostic; C3a/C5a → tissue inflammation and immune complex deposition in lupus nephritis."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "Tfh cells drive anti-dsDNA B cell responses in germinal centers; Th17 cells produce IL-17 in lupus nephritis; Tregs are numerically reduced and functionally impaired in SLE; TCR signaling rewiring and mitochondrial hyperpolarization are hallmark T-cell defects."
  - target: 01-human/03-molecular/nlrp3-inflammasome
    relation: connects-to
    note: "TLR7/9 in pDCs sense nucleic acid-containing immune complexes → massive type I IFN production (IFN signature present in 75% of SLE patients); NLRP3 activated by uric acid crystals and mitochondrial DNA in macrophages → IL-1beta → tissue inflammation in SLE."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "NF-kB activated in SLE B cells by BAFF (B-cell activating factor); belimumab (anti-BAFF) reduces BAFF-driven B-cell survival and NF-kB activation; TLR/IFN signaling also activates NF-kB in myeloid cells → amplifies cytokine cascade in active SLE."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Type I IFN signature (↑MX1, ↑OAS1, ↑ISG15) is present in ~75% of SLE patients and correlates with disease activity; IFN-α amplifies pDC activation and anti-dsDNA production; anifrolumab (anti-IFNAR1; TULIP-2) is FDA-approved for moderate-to-severe SLE."
  - target: 01-human/03-molecular/fcrn
    relation: connects-to
    note: "Anti-dsDNA and other pathogenic SLE autoantibodies are IgG → recycled by FcRn; FcRn blockade (efgartigimod, nipocalimab) reduces SLE autoantibody titers ~60-70%; efgartigimod Phase 3 in SLE ongoing; FcRn blockade complements BLyS/BAFF inhibition by targeting IgG homeostasis."
  - target: 01-human/03-molecular/calcineurin
    relation: connects-to
    note: "Voclosporin (CNI; FDA Jan 2021) added to MMF achieved complete renal response 40.8% vs 22.5% (AURORA-1 Lancet 2021) for lupus nephritis; CNIs also stabilize podocyte synaptopodin → reduce proteinuria independently of T cell effects."
  - target: 01-human/03-molecular/c5ar1
    relation: connects-to
    note: "C5a/C5aR1 amplifies glomerular inflammation in lupus nephritis; C5a engages C5aR1 on neutrophils → NETosis → NET-derived DNA → TLR9 → pDC IFN-α → SLE amplification loop; avacopan (C5aR1 antagonist) under investigation for lupus nephritis."
  - target: 01-human/03-molecular/beta2-glycoprotein-1
    relation: connects-to
    note: "~50% of SLE patients have aPL antibodies (anti-B2GPI, aCL, LA); 30% of aPL-positive SLE patients develop APS; anti-B2GPI IgG may drive SLE nephritis through complement and endothelial activation; hydroxychloroquine reduces aPL titers and thrombotic risk in SLE."
  - target: 01-human/07-system/antiphospholipid-syndrome
    relation: connects-to
    note: "Secondary APS occurs in ~30% of SLE patients with persistent aPL; SLE+APS patients have higher stroke/DVT risk than either condition alone; hydroxychloroquine is recommended in all SLE+aPL patients; the 2023 ACR/EULAR APS criteria incorporate SLE as a risk modifier."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "cGAS-STING sensing of self-DNA drives the type I IFN signature in SLE: NETs, late apoptotic cells, and mtDNA activate cGAS in pDCs/macrophages → cGAMP → STING → IFN-β; TREX1 LOF mutations → monogenic lupus; STING antagonists (H-151, SN-011) are investigated for SLE."
  - target: 01-human/07-system/sjogrens-syndrome
    relation: connects-to
    note: "Lupus and Sjögren's are overlapping autoantibody diseases sharing anti-Ro/SSA, anti-La, and a type-I-interferon signature: secondary Sjögren's commonly complicates SLE, and both can cause neonatal lupus and congenital heart block via placental anti-Ro transfer."
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "Lupus nephritis is the kidney face of SLE and a major driver of chronic kidney disease: immune-complex deposition inflames the glomerulus across six histologic classes, so proteinuria or rising creatinine in a lupus patient prompts biopsy and immunosuppression."
  - target: 01-human/04-cellular/plasma-cell
    relation: connects-to
    note: "Plasma cells make the autoantibodies that drive lupus: long-lived plasma cells secrete anti-dsDNA and antinuclear antibodies that form tissue-damaging immune complexes, and because they resist rituximab, plasma-cell-directed strategies and CAR-T are explored in refractory SLE."
  - target: 01-human/07-system/rheumatoid-arthritis
    relation: connects-to
    note: "Lupus and rheumatoid arthritis are archetypal systemic autoimmune diseases that overlap yet differ: both inflame joints, but RA causes erosive symmetric synovitis with anti-CCP antibodies, while SLE's antinuclear antibodies injure many organs with non-erosive arthritis."
  - target: 01-human/04-cellular/b-cell
    relation: connects-to
    note: "B cells are central to lupus: they produce the antinuclear and anti-dsDNA autoantibodies that form tissue-damaging immune complexes, and present self-antigen to T cells—so B-cell-targeted therapy (belimumab against BAFF, rituximab) treats the disease at its source."
  - target: 01-human/07-system/immune-thrombocytopenia
    relation: connects-to
    note: "Immune thrombocytopenia is a common hematologic feature of lupus: autoantibodies against platelets cause low counts that can be the presenting sign, and SLE must be excluded in new ITP—one of the autoimmune cytopenias that define lupus blood involvement."
---

# Systemic Lupus Erythematosus

## Overview

**Systemic lupus erythematosus (SLE)** is a **multisystem autoimmune disease** characterized by loss of self-tolerance to nuclear antigens — particularly double-stranded DNA (dsDNA), histones, ribonucleoproteins (RNPs, Smith antigen), and phospholipids — leading to immune complex formation, complement activation, and end-organ damage across virtually any tissue [^tsokos-2011-sle-review].

SLE affects approximately **5 million people worldwide** with a striking **female predominance (~9:1 F:M)** and peak onset in reproductive age (15-45 years). Prevalence and severity are higher in people of African, Asian, and Hispanic descent compared to Europeans. SLE is the prototypical type III hypersensitivity disorder (immune complex-mediated), distinct from organ-specific autoimmune diseases like type 1 diabetes.

**Mortality:** SLE mortality has significantly improved (5-year survival from ~50% in 1950s to >95% in high-income countries); leading causes of death are now **lupus nephritis**, infection (from disease and treatment), and cardiovascular disease (accelerated atherosclerosis from chronic inflammation + corticosteroids).

**Pathological hallmarks:**
- **ANA (antinuclear antibodies):** Present in >95% of SLE; highly sensitive but non-specific (also positive in other autoimmune diseases, healthy elderly, and some medications)
- **Anti-dsDNA:** Specific for SLE (~70% sensitivity, >95% specificity); correlates with disease activity and nephritis; fluctuates with flares (monitor for nephritis prediction)
- **Anti-Sm (Smith antigen):** 25-30% sensitive, nearly 100% specific for SLE
- **Anti-phospholipid antibodies (anti-cardiolipin, anti-beta-2-glycoprotein-1, lupus anticoagulant):** Present in ~30-40% → antiphospholipid syndrome (APS) with thrombosis and pregnancy loss
- **Low complement (C3, C4):** Consumed during immune complex formation; low C3/C4 + elevated anti-dsDNA = active lupus nephritis

## Structure

### SLE immunopathogenesis [^tsokos-2011-sle-review]

**Step 1: Failure of apoptotic cell clearance**
- Normal: Apoptotic cells are rapidly phagocytosed by macrophages → nuclear antigens remain intracellular → self-tolerance maintained
- SLE: C1q deficiency (strong genetic risk factor for SLE) → impaired phagocytosis of apoptotic cells → secondary necrosis → nuclear antigens (dsDNA, histones, RNPs) released extracellularly → available for ANA production
- **DNase I** deficiency (accelerated apoptotic DNA release): Contributes to nuclear antigen exposure in SLE patients

**Step 2: Innate immune activation — pDC/type I IFN axis**
- Released nuclear antigens form complexes with autoantibodies (anti-RNA, anti-DNA) → immune complexes (ICs) activate **plasmacytoid dendritic cells (pDCs)** via FcγRIIa (IC uptake) → endosomal TLR7 (RNA) and TLR9 (DNA) → **type I IFN (IFN-alpha/beta)** production → "IFN signature"
- **IFN signature:** 50-75% of SLE patients have elevated expression of type I IFN-stimulated genes (ISGs) in blood — correlates with disease activity, anti-dsDNA, and complement
- Type I IFN → activates DCs and B cells → breaks peripheral tolerance → promotes autoreactive B and T cell survival and activation
- **Neutrophil extracellular traps (NETs):** SLE neutrophils undergo NETosis → release nuclear material (DNA + histone + neutrophil elastase) → TLR9 activation → IFN-alpha production → amplifies IFN signature

**Step 3: Adaptive immune activation**
- DCs present nucleosomal antigens to autoreactive CD4+ T cells (escaped thymic deletion due to low-affinity TCR for self antigens) → T cell activation
- **Tfh cells:** Required for GC formation → autoreactive B cell somatic hypermutation → high-affinity ANA production; aberrant IL-21 production in SLE-associated Tfh → germinal center hyperactivity
- **BAFF (B lymphocyte stimulator, BLyS):** Elevated in SLE → promotes autoreactive B cell survival (normally deleted by negative selection) → plasma cell differentiation → ANA secretion
- **Autoreactive plasma cells:** Long-lived plasma cells in bone marrow niches produce ANAs continuously → end-organ IC deposition

**Step 4: Complement activation and tissue injury**
- IgG and IgM ANAs bind nuclear antigens in tissues (kidney glomeruli, skin, synovium, choroid plexus) → classical complement pathway activation (C1q → C4 → C3 → C5 → MAC) → tissue inflammation
- **Lupus nephritis:** IC deposition in mesangium/subendothelium/subepithelium → glomerulonephritis; complement activation → neutrophil and macrophage recruitment → crescentic nephritis in severe cases

### Genetic architecture of SLE

Highly polygenic disease with >100 susceptibility loci; heritability ~66%:
- **HLA:** HLA-DRB1*0301, HLA-DQB1*0201 → Ro/La antibodies; HLA-DRB1*1501 → anti-dsDNA in Europeans
- **Complement genes:** C1q deficiency (rare, autosomal recessive) → 90% develop lupus-like disease; C4A null allele → mild risk increase (most common)
- **TREX1:** DNase mutations → failure to clear cytosolic DNA → cGAS-STING → type I IFN production → Aicardi-Goutières syndrome/SLE overlap
- **IRF5, IRAK1, TLR7:** Type I IFN pathway SNPs → higher IFN production → SLE risk
- **PTPN22, STAT4, BLK, BANK1:** T and B cell signaling; PTPN22 C1858T (hypomorphic LYP phosphatase) → enhanced TCR/BCR signaling → shared risk with RA, T1DM

## Function

### Clinical presentation

**2019 EULAR/ACR classification criteria:** Score ≥10 for classification (not diagnosis); ANA ≥1:80 required as entry criterion; domains: constitutional (fever), hematological (cytopenias), neuropsychiatric, mucocutaneous, serosal, musculoskeletal, renal, immunological (anti-dsDNA, anti-Sm, complement, antiphospholipid)

**Common clinical features:**
- **Malar (butterfly) rash:** Fixed erythema over cheeks and nose, sparing nasolabial folds; photosensitive; present in ~50%
- **Discoid lupus:** Scarring, follicular plugging, hypopigmented scarring on face, scalp (alopecia), and extremities; often ANA-negative; 5% progress to SLE
- **Photosensitivity:** Rash with UV exposure → important patient education (sunscreen, UV avoidance)
- **Oral ulcers:** Painless, palatal; often overlooked
- **Non-scarring alopecia:** Diffuse hair thinning; active disease; reversible
- **Serositis:** Pleuritis (chest pain, pleural effusion), pericarditis; correlates with disease activity
- **Arthritis:** Non-destructive, non-erosive polyarthritis (vs. RA); often migratory; Jaccoud's arthropathy (reversible subluxations in chronic disease)
- **Raynaud's phenomenon:** Vasospastic in ~20%

**Lupus nephritis (LN):**
- Present in 30-50% of SLE patients, most frequently early in disease course
- ISN/RPS classification (I-VI): Class III (focal) and IV (diffuse) proliferative → most aggressive; Class V (membranous) → nephrotic syndrome; Class VI → end-stage
- Kidney biopsy guides therapy: IV nephritis → IV cyclophosphamide (Euro-Lupus protocol) or MMF induction → MMF or azathioprine maintenance; voclosporin or obinutuzumab (anti-CD20) added for refractory cases
- EULAR 2023 target: <0.5 g/day proteinuria, normal eGFR at 12 months (complete renal response)

**Neuropsychiatric SLE (NPSLE):**
- Occurs in 25-75% (wide range depending on case definition); most common: cognitive dysfunction, headache, mood disorders
- Severe manifestations: psychosis, seizures, stroke (often thrombotic in APS), transverse myelitis, cranial neuropathies
- Pathophysiology: NMO-IgG-negative longitudinal myelitis, anti-ribosomal P antibodies → psychosis, intrathecal IC deposition

**Cardiovascular:**
- **Libman-Sacks endocarditis:** Sterile verrucous vegetations on mitral/aortic valves; embolic risk; associated with APS
- **Atherosclerosis:** 10-30× increased MI risk in young women with SLE (Framingham study) → chronic inflammation + steroids + traditional CV risk factors
- **Antiphospholipid syndrome (APS):** Thrombosis (DVT/PE, stroke), pregnancy morbidity (recurrent miscarriage, preeclampsia, IUFD) in patients with antiphospholipid antibodies; treatment: anticoagulation (warfarin, INR 2-3; rivaroxaban inferior in APS triple-positive patients)

## Pathology

### Diagnosis

**Laboratory:**
- ANA (IIF, HEp-2 cells) ≥1:80: Entry criterion; high sensitivity; confirmatory ANAs: anti-dsDNA (Farr or Crithidia assay), anti-Sm, anti-Ro/La, anti-RNP, anti-phospholipid
- CBC: Lymphopenia (<1000/μL; most common SLE cytopenia), leukopenia, hemolytic anemia (Coombs+, <5%), thrombocytopenia (anti-platelet antibodies)
- Urinalysis: Hematuria, proteinuria, casts (red cell casts → nephritis)
- Complement: C3, C4 consumed during active disease; monitor serially
- CRP: Usually normal or minimally elevated in SLE activity (unlike RA); elevated CRP in SLE suggests superimposed infection — important diagnostic clue

**Disease activity:** SLEDAI-2K (SLE Disease Activity Index), BILAG (British Isles Lupus Assessment Group); guide treatment escalation

### Treatment

**Hydroxychloroquine (HCQ, Plaquenil):**
- First-line for all SLE patients without contraindication; TLR7/9 inhibitor in endosomes → reduces type I IFN production; 200-400 mg/day; CV benefit (reduces thrombosis), reduces flares and organ damage, reduces mortality; retinal toxicity at cumulative dose (baseline ophthalmology, annual screening after 5 years at high dose/long duration)

**Glucocorticoids:**
- For acute flares; minimize long-term use; prednisone >7.5 mg/day associated with organ damage accrual; target <5 mg/day for maintenance or off if possible; IV methylprednisolone pulses (500-1000 mg × 3 days) for severe LN, NPSLE, or cytopenias

**Immunosuppressants:**
- **Azathioprine (AZA):** Maintenance therapy for LN and arthritis/serositis; TPMT/NUDT15 genotyping; anti-malarial + AZA → flare prevention
- **Mycophenolate mofetil (MMF/Cellcept):** Euro-Lupus and ALMS trials — MMF non-inferior to cyclophosphamide for LN induction; preferred for LN class III/IV maintenance; teratogenic → contraception required
- **Cyclophosphamide (CYC):** IV pulse (Euro-Lupus: 500 mg every 2 weeks × 6 doses) for LN induction; also for severe NPSLE, vasculitis, pulmonary hemorrhage; hemorrhagic cystitis (MESNA), gonadotoxicity (ovarian preservation with GnRH agonist before treatment)
- **Calcineurin inhibitors (tacrolimus, cyclosporin):** Class V membranous LN; voclosporin (calcineurin inhibitor) + MMF = superior to MMF alone in AURORA-1 trial → FDA approved 2021 for active LN

**Biologics:**
- **Belimumab (Benlysta, anti-BAFF/BLyS):** Anti-BAFF mAb → reduces autoreactive B cell survival; IV or SC monthly; BLISS-52/76 trials: modest but significant reduction in flares (~15-20%); FDA approved for active SLE (renal and CNS excluded initially); BLISS-LN: IV belimumab + SoC → 43% vs. 32% primary renal response at week 104; FDA approved for LN 2021 [^furie-2011-belimumab]
- **Anifrolumab (Saphnelo, anti-IFNAR1):** Blocks type I IFN receptor → eliminates IFN signature; TULIP-2: 47.8% vs. 31.5% BICLA response at week 52; FDA approved 2021 for moderate-severe SLE [^morand-2020-anifrolumab]; most active in IFN-high patients (biomarker-driven use)
- **Voclosporin (Lupkynis):** Non-immunosuppressant calcineurin inhibitor; AURORA-1 trial → LN; see above
- **Obinutuzumab (anti-CD20, NOBILITY trial):** Superior to placebo in active LN; rituximab also used off-label for refractory cytopenias and lupus nephritis
- **Daratumumab (anti-CD38, depletes plasma cells):** Case series and trials in refractory SLE; eliminates long-lived plasma cells that produce ANAs — potential for "reset" in refractory disease

**Pregnancy in SLE:**
- High-risk; planned conception during disease quiescence (≥6 months)
- HCQ is safe in pregnancy; AZA permitted; MMF teratogenic → switch to AZA before conception
- Fetal risks: neonatal lupus (anti-Ro/La → congenital heart block — monitor weekly cardiac echo from 16-26 weeks), IUGR, preterm birth
- APS in pregnancy: LMWH + aspirin (anticoagulation maintains pregnancy)

## Connections

- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — C1q and C4 deficiencies impair apoptotic cell clearance → nuclear antigen exposure → ANA production; C3/C4 consumption during immune complex deposition in lupus nephritis is the primary diagnostic and monitoring biomarker; complement activation drives glomerular and tissue injury in SLE.
- `connects-to` → **[T Helper Cell](../../04-cellular/t-helper-cell/README.md)** — Tfh cells drive germinal center hyperactivity and anti-dsDNA B-cell differentiation; Th17 cells contribute to lupus nephritis via IL-17; Treg depletion removes suppression; TCR signaling rewiring and mitochondrial hyperpolarization are hallmark T-cell defects in SLE.
- `connects-to` → **[NLRP3 Inflammasome](../../03-molecular/nlrp3-inflammasome/README.md)** — TLR7/9 activation by nucleic acid immune complexes drives type I IFN production in pDCs (IFN signature in 75% of patients); NLRP3 activated by mitochondrial DNA and NETs in macrophages → IL-1beta → tissue inflammation; anifrolumab blocks the downstream IFN receptor (IFNAR1).
- `connects-to` → **[NF-kB](../../03-molecular/nf-kb/README.md)** — BAFF activates NF-kB in SLE B cells, promoting autoreactive B cell survival and ANA production; belimumab (anti-BAFF) reduces BAFF-driven B-cell NF-kB activation; TLR and IFN signaling also activate NF-kB in SLE myeloid cells amplifying the cytokine cascade.
- `connects-to` → **[Type I Interferon](../../03-molecular/type-i-interferon/README.md)** — Type I IFN signature (↑MX1, ↑OAS1, ↑ISG15) is present in ~75% of SLE patients and correlates with disease activity; IFN-α amplifies pDC activation and anti-dsDNA production; anifrolumab (anti-IFNAR1; TULIP-2) is FDA-approved for moderate-to-severe SLE.
- `connects-to` → **[FcRn](../../03-molecular/fcrn/README.md)** — Anti-dsDNA and other pathogenic SLE autoantibodies are IgG → recycled by FcRn; FcRn blockade (efgartigimod, nipocalimab) reduces SLE autoantibody titers ~60-70%; efgartigimod Phase 3 in SLE ongoing; FcRn blockade complements BLyS/BAFF inhibition by targeting IgG homeostasis.
- `connects-to` → **[Calcineurin](../../03-molecular/calcineurin/README.md)** — Voclosporin (CNI; FDA Jan 2021) added to MMF achieved complete renal response 40.8% vs 22.5% (AURORA-1 Lancet 2021) for lupus nephritis; CNIs also stabilize podocyte synaptopodin → reduce proteinuria independently of T cell effects.
- `connects-to` → **[C5aR1](../../03-molecular/c5ar1/README.md)** — C5a/C5aR1 amplifies glomerular inflammation in lupus nephritis; C5a engages C5aR1 on neutrophils → NETosis → NET-derived DNA → TLR9 → pDC IFN-α → SLE amplification loop; avacopan (C5aR1 antagonist) under investigation for lupus nephritis.
- `connects-to` → **[Beta-2 Glycoprotein I](../../03-molecular/beta2-glycoprotein-1/README.md)** — ~50% of SLE patients have aPL antibodies (anti-B2GPI, aCL, LA); 30% of aPL-positive SLE patients develop APS; anti-B2GPI IgG may drive SLE nephritis through complement and endothelial activation; hydroxychloroquine reduces aPL titers and thrombotic risk in SLE.
- `connects-to` → **[Antiphospholipid Syndrome](../antiphospholipid-syndrome/README.md)** — Secondary APS occurs in ~30% of SLE patients with persistent aPL; SLE+APS patients have higher stroke/DVT risk than either condition alone; hydroxychloroquine is recommended in all SLE+aPL patients; the 2023 ACR/EULAR APS criteria incorporate SLE as a risk modifier.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — cGAS-STING sensing of self-DNA drives the type I IFN signature in SLE: NETs, late apoptotic cells, and mtDNA activate cGAS in pDCs/macrophages → cGAMP → STING → IFN-β; TREX1 LOF mutations → monogenic lupus; STING antagonists (H-151, SN-011) are investigated for SLE.
- `connects-to` → **[Sjögren's Syndrome](../sjogrens-syndrome/README.md)** — Lupus and Sjögren's are overlapping autoantibody diseases sharing anti-Ro/SSA, anti-La, and a type-I-interferon signature: secondary Sjögren's commonly complicates SLE, and both can cause neonatal lupus and congenital heart block via placental anti-Ro transfer.
- `connects-to` → **[Chronic Kidney Disease](../ckd/README.md)** — Lupus nephritis is the kidney face of SLE and a major driver of chronic kidney disease: immune-complex deposition inflames the glomerulus across six histologic classes, so proteinuria or rising creatinine in a lupus patient prompts biopsy and immunosuppression.
- `connects-to` → **[Plasma Cell](../../04-cellular/plasma-cell/README.md)** — Plasma cells make the autoantibodies that drive lupus: long-lived plasma cells secrete anti-dsDNA and antinuclear antibodies that form tissue-damaging immune complexes, and because they resist rituximab, plasma-cell-directed strategies and CAR-T are explored in refractory SLE.
- `connects-to` → **[Rheumatoid Arthritis](../rheumatoid-arthritis/README.md)** — Lupus and rheumatoid arthritis are archetypal systemic autoimmune diseases that overlap yet differ: both inflame joints, but RA causes erosive symmetric synovitis with anti-CCP antibodies, while SLE's antinuclear antibodies injure many organs with non-erosive arthritis.
- `connects-to` → **[B Cell](../../04-cellular/b-cell/README.md)** — B cells are central to lupus: they produce the antinuclear and anti-dsDNA autoantibodies that form tissue-damaging immune complexes, and present self-antigen to T cells—so B-cell-targeted therapy (belimumab against BAFF, rituximab) treats the disease at its source.
- `connects-to` → **[Immune Thrombocytopenia](../immune-thrombocytopenia/README.md)** — Immune thrombocytopenia is a common hematologic feature of lupus: autoantibodies against platelets cause low counts that can be the presenting sign, and SLE must be excluded in new ITP—one of the autoimmune cytopenias that define lupus blood involvement.

[^tsokos-2011-sle-review]: Tsokos GC. Systemic lupus erythematosus. *N Engl J Med.* 2011;365(22):2110-2121. [doi:10.1056/NEJMra1100359](https://doi.org/10.1056/NEJMra1100359) · [PubMed 22129253](https://pubmed.ncbi.nlm.nih.gov/22129253/)
[^furie-2011-belimumab]: Furie R, Petri M, Zamani O, et al. A phase III, randomized, placebo-controlled study of belimumab, a monoclonal antibody that inhibits B lymphocyte stimulator, in patients with systemic lupus erythematosus. *Arthritis Rheum.* 2011;63(12):3918-3930. [doi:10.1002/art.30613](https://doi.org/10.1002/art.30613) · [PubMed 22127708](https://pubmed.ncbi.nlm.nih.gov/22127708/)
[^morand-2020-anifrolumab]: Morand EF, Furie R, Tanaka Y, et al. Trial of anifrolumab in active systemic lupus erythematosus. *N Engl J Med.* 2020;382(3):211-221. [doi:10.1056/NEJMoa1912196](https://doi.org/10.1056/NEJMoa1912196) · [PubMed 31851795](https://pubmed.ncbi.nlm.nih.gov/31851795/)
