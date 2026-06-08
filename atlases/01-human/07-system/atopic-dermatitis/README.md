---
schema: human-scale-entry/v1
id: atopic-dermatitis
name: Atopic Dermatitis
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-07
summary: "Chronic relapsing type 2 inflammatory skin disease; IL-4/IL-13 → STAT6 → filaggrin and barrier protein suppression → epidermal barrier failure and Th2 sensitization; dupilumab (anti-IL-4Rα) and JAK1 inhibitors (upadacitinib) are first-line biologics."
aliases: ["atopic dermatitis", "AD", "eczema", "atopic eczema", "IgE-mediated dermatitis"]
sources:
  - id: weidinger-2018-atopic-dermatitis
    type: peer-reviewed
    cite: "Weidinger S, Beck LA, Bieber T, Kabashima K, Steinhoff M. Atopic dermatitis. Nat Rev Dis Primers. 2018;4(1):1."
    doi: "10.1038/s41572-018-0001-z"
    pmid: "30464227"
    url: "https://doi.org/10.1038/s41572-018-0001-z"
  - id: simpson-2016-dupilumab-ad
    type: peer-reviewed
    cite: "Simpson EL, Bieber T, Guttman-Yassky E, et al. Two Phase 3 Trials of Dupilumab versus Placebo in Atopic Dermatitis. N Engl J Med. 2016;375(24):2335-2348."
    doi: "10.1056/NEJMoa1610020"
    pmid: "27690741"
    url: "https://doi.org/10.1056/NEJMoa1610020"
cross_links:
  - target: 01-human/03-molecular/il-4
    relation: modulated-by
    note: "IL-4 → IL-4Rα/STAT6 → filaggrin (FLG), claudin-1, and loricrin suppression → barrier dysfunction; Th2 polarization and IgE class switching; dupilumab (anti-IL-4Rα) blocks IL-4 and IL-13 → 51% EASI-75 at 16 weeks in Phase 3 trials."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Atopic dermatitis initiates the atopic march: IL-4/IL-13 drives IgE class switching and mast cell sensitization; mast cell FcεRI → histamine and PGD2 on allergen exposure; systemic IgE sensitization to food/aeroallergens predisposes to allergic rhinitis and asthma."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "Chronic AD scratching cycles → IL-4/IL-13 → TGF-β from keratinocytes and fibroblasts → skin fibrosis (lichenification); TGF-β also promotes peripheral Treg induction and restrains the acute phase; elevated skin TGF-β1 is a marker of chronic-phase barrier fibrosis."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "Pediatric and Asian-predominant AD phenotypes have increased Th17 (IL-17A/IL-22) inflammation alongside Th2; IL-17A → antimicrobial peptide induction but also barrier disruption synergy with IL-4/IL-13; lebrikizumab, tralokinumab (anti-IL-13) provide IL-13-selective blockade."
  - target: 01-human/03-molecular/il-13
    relation: modulated-by
    note: "IL-13 → IL-13Rα1/IL-4Rα → STAT6 → FLG, claudin-1, loricrin suppression → barrier failure; IL-13 is the dominant effector in chronic AD lichenification and fibrosis; tralokinumab (ECZTRA 1/2: 38% IGA 0/1) and lebrikizumab (ADVOCATE: 43% IGA 0/1) target IL-13 specifically."
---

# Atopic Dermatitis

## Overview

**Atopic dermatitis (AD)** is a **chronic, relapsing, pruritic inflammatory skin disease** affecting approximately **230 million people** worldwide — the most prevalent non-communicable skin disease globally [^weidinger-2018-atopic-dermatitis]. Prevalence is 15–30% in children and 2–10% in adults in developed countries. AD is the initiating disease of the **atopic march**: sensitized individuals progress through AD → allergic rhinitis → asthma in a sequence driven by systemic Th2 immune activation beginning in early childhood.

AD is a **biologically heterogeneous disease** unified by two interdependent defects:
1. **Epidermal barrier failure** — driven by genetic loss-of-function in filaggrin (*FLG*), claudin-1, and other structural proteins, amplified by IL-4/IL-13 suppression of barrier genes
2. **Type 2 (Th2) immune dysregulation** — allergen penetration through the disrupted barrier → Th2 polarization → IL-4, IL-5, IL-13, IL-31 → amplified itch (IL-31 → dorsal root ganglion neurons), IgE sensitization, and further barrier damage

The discovery that **IL-4Rα blockade** with dupilumab breaks this cycle provided the first targeted treatment and confirmed that IL-4/IL-13 is the central pathogenic axis [^simpson-2016-dupilumab-ad].

**Phenotypic subtypes of AD:**

| Phenotype | Dominant cytokines | Features |
|---|---|---|
| European/adult-onset intrinsic | Th2 (IL-4/IL-13) + Th22 | Flexural/lichenified; high IgE; FLG mutations |
| Asian/pediatric | Th2 + Th17 (IL-17A/IL-22) | Nummular; seborrheic distribution; less IgE |
| Pediatric US/Black skin | Th2 + Th17 | Follicular; papular; annular; discoid patterns |
| Elderly-onset | Th2 + Th1 (IFN-γ) | Thicker lichenification; lower IgE; itch-scratch |

## Structure

### Epidermal Barrier Architecture

The epidermal barrier is a multi-layered structural and biochemical defense:

**Stratum corneum (SC):**
- "Brick and mortar" model: corneocytes (anucleate, keratin-filled, cornified envelope) embedded in a lamellar lipid matrix (ceramides, free fatty acids, cholesterol)
- **Tight junctions** (claudin-1, occludin, ZO-1): paracellular seal in stratum granulosum
- **Natural moisturizing factor (NMF):** filaggrin degradation products (urocanic acid, pyrrolidone carboxylic acid) → humectants → retain SC hydration

**Filaggrin (FLG) — the central barrier protein:**
- 400 kDa profilaggrin → processed into 10-12 individual filaggrin monomers in the granular layer
- Filaggrin monomers: bundle and aggregate keratin intermediate filaments → compact corneocytes
- Degradation → NMF components; filaggrin loss → reduced NMF → reduced water-binding → xerosis (dry skin)
- **FLG loss-of-function mutations** (R501X, 2282del4, and ≥50 others): present in 50% of European AD patients; 10% of European population carries ≥1 FLG LOF variant; the single largest genetic risk factor for AD (OR 3–5)
- IL-4 and IL-13 → STAT6 → *FLG* promoter suppression → acquired filaggrin deficiency even in non-FLG mutation carriers

**Lipid barrier:**
- Lamellar bodies (membrane-coating granules) secreted at the SG-SC junction → ceramides, free fatty acids, cholesterol → lipid lamellae
- AD: abnormal ceramide composition (increased short-chain ceramides; reduced ceramide/cholesterol ratio) → impaired lamellar bilayer → transepidermal water loss (TEWL) ↑

### Immunological Compartments in AD Skin

**Acute-phase (2-3 days after allergen challenge):**
- Keratinocyte TSLP, IL-33, IL-25 → ILC2 and mast cell activation → IL-4, IL-5, IL-13 immediate wave
- Th2 infiltration → IL-4/IL-13 → STAT6 → TARC/CCL17 and MDC/CCL22 → additional Th2 recruitment
- Dendritic cells with surface IgE (via FcεRI) → antigen capture → Th2 priming

**Chronic-phase:**
- Persistent Th2 + Th22 (IL-22 → epidermal hyperplasia → acanthosis and lichenification) + some Th1 (IFN-γ)
- Reduced Th17 (relative to psoriasis) in European adults — a key immunological distinction from psoriasis
- IL-31 (Th2 cell-derived): acts on IL-31RA/OSMR on cutaneous sensory neurons → JAK1 → TRPA1 upregulation → intractable itch (prurigo axis)

## Function

### Pathogenic Cascade

**Initiating events:**
1. Genetic predisposition: FLG LOF + immune gene variants (*IL4*, *IL13*, *IL4R*, *SPINK5*, *EMID1*, *OVOL1*, *KIF3A*, *LRCH4* GWAS loci)
2. Environmental exposures: early life microbial dysbiosis, hard water (calcium carbonate → surfactant deposition), detergent exposure, low humidity
3. FLG/barrier gene deficiency → TEWL ↑ → dry skin → mechanical micro-injury from scratching → hapten/allergen penetration

**Sensitization and amplification:**
1. Barrier breach → allergen contact with epidermal DCs and ILC2s
2. Keratinocytes release alarmins (TSLP, IL-33, IL-25) → ILC2 → IL-4, IL-13, IL-5 in hours (innate wave)
3. DCs migrate to regional LN → allergen presentation to naive T cells → IL-4 milieu → Th2 differentiation (GATA-3 induction)
4. Allergen-specific Th2 cells → skin homing (CCR4+ via TARC gradient) → IL-4/IL-13 production → STAT6 → IL-4/IL-13 amplification loop
5. IgE class switching (B cells via IL-4) → systemic IgE → mast cell sensitization in skin and airways → atopic march initiation

**Itch-scratch cycle:**
- IL-31 → IL-31RA on sensory neurons → JAK1/TYK2 → TRPA1/TRPV1 upregulation → itch
- Thymic stromal lymphopoietin (TSLP) also acts directly on sensory neurons via TRPA1 → itch (non-histamine mediated — explains why H1 antihistamines fail in AD)
- Scratching → keratinocyte injury → TSLP, IL-33 release → more immune activation → more itch (vicious cycle)

### Staphylococcus aureus in AD

S. aureus colonizes >90% of AD lesional skin (vs. 20% normal skin):
- **Mechanism:** IL-4/IL-13 → suppresses FLG and β-defensin-2/3, LL-37 → S. aureus ecological advantage
- **Amplification:** S. aureus toxins (alpha toxin, V8 protease, staphylococcal superantigens) → TLR2/TLR4 → TSLP, IL-33 → Th2 amplification; superantigens activate Th2 cells non-specifically → polyclonal IgE production
- **Dupilumab effect:** Reduces S. aureus colonization by restoring barrier protein expression → one mechanism of AD improvement

## Pathology

### Assessment Tools

**EASI (Eczema Area and Severity Index):** 0–72; grades erythema, infiltration, excoriation, lichenification; area-weighted; primary endpoint in clinical trials
- EASI-50/75/90/100: 50%/75%/90%/100% improvement = meaningful clinical thresholds
- IGA (Investigator's Global Assessment) 0/1 = clear or almost clear; secondary endpoint

**SCORAD:** 0–103; combines objective (103-point) + subjective (itch + sleep)

**NRS (Numerical Rating Scale):** 0–10; patient-reported pruritus severity

### Drug Classes

**Dupilumab (Dupixent; anti-IL-4Rα mAb):**
- Blocks both IL-4 and IL-13 via IL-4Rα blockade — the shared receptor component
- SOLO 1/SOLO 2 (Phase 3): 300 mg Q2W → 51% EASI-75; 36% IGA 0/1 vs. 10% placebo at 16 weeks [^simpson-2016-dupilumab-ad]
- Generally well-tolerated; conjunctivitis (15–20%) is the main adverse effect; no immunosuppression-related serious infections
- FDA approved 2017 for moderate-severe AD ≥18 years; subsequently expanded to ≥6 months; also adolescents 12–17 and 6–11 years

**IL-13-selective biologics:**
- **Tralokinumab (Adbry):** Anti-IL-13 mAb; binds IL-13 directly (does not block IL-4); ECZTRA Phase 3: 25% IGA 0/1 at 16 weeks as monotherapy
- **Lebrikizumab (Ebglyss):** Anti-IL-13 mAb; ADvocate Phase 3: 43% IGA 0/1; faster onset than dupilumab claimed; FDA approved 2023

**JAK inhibitors:**
- **Upadacitinib (Rinvoq; JAK1i):** Heads Up trial vs. dupilumab: 71% EASI-75 vs. 61% (superior); FDA approved for moderate-severe AD ≥12 years; BOXED WARNING: malignancy, thrombosis, infections, MACE
- **Baricitinib (Olumiant; JAK1/2i):** BREEZE-AD Phase 3: 40% EASI-75 at 16 weeks; FDA approved; limited to ≥18 years
- **Abrocitinib (Cibinqo; JAK1i):** JADE Phase 3: 63% EASI-75; rapid itch relief (day 2-4); FDA approved; BOXED WARNING shared with class

**IL-31 pathway:**
- **Nemolizumab (anti-IL-31RA):** FDA approved 2024 for prurigo nodularis (first approval); Phase 3 AD trials (ARCADIA): 68% EASI-75 vs. 25% placebo; primarily targets itch; combined with TCS

**Topical therapies:**
- **Topical corticosteroids (TCS):** First-line for flares; tachyphylaxis and skin atrophy with overuse
- **Tacrolimus/pimecrolimus** (topical calcineurin inhibitors): Anti-inflammatory without atrophy; face/folds; BOXED WARNING for rare lymphoma (epidemiological data weak)
- **Ruxolitinib cream (Opzelura; topical JAK1/2i):** FDA approved for mild-moderate AD ≥12 years; avoids systemic toxicity
- **Crisaborole (Eucrisa; PDE4i):** FDA approved for mild-moderate; modest efficacy; now somewhat superseded by topical JAKi

## Connections

- `modulated-by` → **[IL-4](../../03-molecular/il-4/README.md)** — IL-4 → IL-4Rα/STAT6 → filaggrin (FLG), claudin-1, and loricrin suppression → barrier dysfunction; Th2 polarization and IgE class switching; dupilumab (anti-IL-4Rα) blocks IL-4 and IL-13 → 51% EASI-75 at 16 weeks in Phase 3 trials.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — atopic dermatitis is the cardinal atopic disease: IL-4/IL-13-driven IgE class switching and elevated total IgE correlate with AD severity; sensitized mast cells and basophils release histamine and PGD2; IgE-mediated sensitization predisposes to allergic rhinitis and asthma (atopic march).
- `connects-to` → **[TGF-β](../../03-molecular/tgf-beta/README.md)** — chronic AD scratching cycles → IL-4/IL-13 → TGF-β from keratinocytes and fibroblasts → skin fibrosis (lichenification); TGF-β also promotes peripheral Treg induction and restrains the acute phase; elevated skin TGF-β1 is a marker of chronic-phase barrier fibrosis.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — pediatric and Asian-predominant AD phenotypes have increased Th17 (IL-17A/IL-22) inflammation alongside Th2; IL-17A → antimicrobial peptide induction but also barrier disruption synergy with IL-4/IL-13; lebrikizumab, tralokinumab (anti-IL-13) provide IL-13-selective blockade.
- `modulated-by` → **[IL-13](../../03-molecular/il-13/README.md)** — IL-13 → IL-13Rα1/IL-4Rα → STAT6 → FLG, claudin-1, loricrin suppression → barrier failure; IL-13 is the dominant effector in chronic AD lichenification and fibrosis; tralokinumab (ECZTRA 1/2: 38% IGA 0/1) and lebrikizumab (ADVOCATE: 43% IGA 0/1) target IL-13 specifically.

[^weidinger-2018-atopic-dermatitis]: Weidinger S, Beck LA, Bieber T, Kabashima K, Steinhoff M. Atopic dermatitis. *Nat Rev Dis Primers.* 2018;4(1):1. [doi:10.1038/s41572-018-0001-z](https://doi.org/10.1038/s41572-018-0001-z) · [PubMed 30464227](https://pubmed.ncbi.nlm.nih.gov/30464227/)
[^simpson-2016-dupilumab-ad]: Simpson EL, Bieber T, Guttman-Yassky E, et al. Two Phase 3 Trials of Dupilumab versus Placebo in Atopic Dermatitis. *N Engl J Med.* 2016;375(24):2335-2348. [doi:10.1056/NEJMoa1610020](https://doi.org/10.1056/NEJMoa1610020) · [PubMed 27690741](https://pubmed.ncbi.nlm.nih.gov/27690741/)
