---
schema: human-scale-entry/v1
id: il-4
name: IL-4
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-07
summary: "IL-4 (Th2 cytokine) drives B cell IgE class switching, Th2 differentiation via STAT6/GATA-3, and epithelial barrier suppression; dupilumab (anti-IL-4Rα) blocks IL-4 and IL-13 signaling and is FDA-approved for atopic dermatitis, asthma, and CRSwNP."
aliases: ["IL-4", "interleukin-4", "IL4", "Th2 cytokine", "STAT6", "dupilumab", "IL-4Rα", "IL-13Rα1", "type 2 immunity"]
cross_links:
  - target: 01-human/07-system/atopic-dermatitis
    relation: connects-to
    note: "IL-4 → IL-4Rα/STAT6 → suppresses filaggrin, claudin-1, and loricrin → epithelial barrier dysfunction; drives Th2 polarization and IgE class switching; dupilumab (anti-IL-4Rα) blocks IL-4 and IL-13 → 51% EASI-75 in moderate-severe atopic dermatitis."
  - target: 01-human/07-system/asthma
    relation: connects-to
    note: "IL-4 drives Th2 airway inflammation, IgE production, and eosinophil recruitment in allergic asthma; type II receptor (IL-4Rα + IL-13Rα1) mediates mucus and AHR; dupilumab reduces severe asthma exacerbations by ~50% in patients with elevated eosinophils or FeNO."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "IL-4 is the principal driver of B cell IgE class switching: IL-4 → STAT6 → ε germline transcription → AID-mediated switch recombination → IgE-secreting plasma cells; IL-13 shares this function via the type II IL-4Rα/IL-13Rα1 receptor."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "IL-4 signals via JAK1 + JAK3 (type I, lymphocytes) or JAK1 + TYK2/JAK2 (type II, epithelium) → STAT6; baricitinib and upadacitinib (JAK1 inhibitors) reduce atopic dermatitis severity by blocking IL-4 and IL-13 downstream signaling."
  - target: 01-human/07-system/prurigo-nodularis
    relation: connects-to
    note: "PN shares Th2/Th22 axis with AD; IL-4 and IL-13 drive Th2 polarization in PN nodular skin; dupilumab (anti-IL-4Rα, blocking both IL-4 and IL-13) is FDA-approved for PN; LIBERTY-PN PRIME2: IGA success 37% vs. 22% placebo at 24 weeks."
sources:
  - id: brown-2004-il4-review
    type: peer-reviewed
    cite: "Brown MA, Hural J. Functions of IL-4 and control of its expression. Crit Rev Immunol. 1997;17(1):1-32."
    doi: "10.1615/CritRevImmunol.v17.i1.10"
    pmid: "9003261"
    url: "https://doi.org/10.1615/CritRevImmunol.v17.i1.10"
  - id: simpson-2016-dupilumab-ad
    type: peer-reviewed
    cite: "Simpson EL, Bieber T, Guttman-Yassky E, et al. Two Phase 3 Trials of Dupilumab versus Placebo in Atopic Dermatitis. N Engl J Med. 2016;375(24):2335-2348."
    doi: "10.1056/NEJMoa1610020"
    pmid: "27690741"
    url: "https://doi.org/10.1056/NEJMoa1610020"
---

# IL-4

## Overview

**IL-4** (gene *IL4*, chromosome 5q31.1) is a **15 kDa pleiotropic cytokine** produced by **Th2 cells, mast cells, basophils, NKT cells, and ILC2s** that is the **master regulator of type 2 (Th2) immune responses**. IL-4 sits within the chromosome 5 Th2 cytokine cluster (also containing *IL5*, *IL13*, *IL3*, and *GMCSF*), which is coordinately regulated by GATA-3 — reflecting the evolutionary integration of these cytokines into a single parasitic defense and wound-healing module that is pathologically activated in atopy.

IL-4 operates through **two receptor complexes:**
- **Type I receptor** (IL-4Rα + common γ chain/γc): Expressed on hematopoietic cells (T cells, B cells, NK cells, mast cells); signals through JAK1 (IL-4Rα) + JAK3 (γc) → STAT6
- **Type II receptor** (IL-4Rα + IL-13Rα1): Expressed on non-hematopoietic cells (epithelial cells, smooth muscle, fibroblasts, endothelium, goblet cells); signals through JAK1 + TYK2 → STAT6; also binds IL-13 (with higher affinity than IL-4)

The type II receptor is why **dupilumab** — a monoclonal antibody targeting **IL-4Rα** — blocks **both IL-4 and IL-13 signaling** through a single therapeutic target. Dupilumab (Dupixent) has achieved blockbuster status across multiple type 2 inflammatory diseases: atopic dermatitis, asthma, chronic rhinosinusitis with nasal polyps (CRSwNP), eosinophilic esophagitis, prurigo nodularis, and COPD with eosinophilia [^simpson-2016-dupilumab-ad].

**Key IL-4 effector functions:**

| Cell type | IL-4 receptor | Key effect |
|---|---|---|
| B cells | Type I (IL-4Rα/γc) | IgE class switch; germinal center entry; CD23 (FcεRII) upregulation |
| Th2 precursors (naive T cells) | Type I | GATA-3 induction → Th2 differentiation; STAT6 → IL-4 autocrine amplification |
| Mast cells/basophils | Type I | FcεRI upregulation; survival and priming |
| Keratinocytes/epithelium | Type II (IL-4Rα/IL-13Rα1) | Filaggrin (FLG) suppression → barrier dysfunction; antimicrobial peptide suppression |
| Airway smooth muscle | Type II | Hyperresponsiveness; goblet cell mucus induction |
| Macrophages | Type II | M2 (alternative) polarization; IL-10, arginase, fibronectin production |

## Structure

**IL-4 protein (153 aa, ~15 kDa after signal peptide cleavage):**
- **Four-helix bundle** (αA-αB-αC-αD topology): short-chain topology; same structural class as IL-2, IL-7, IL-9, IL-15, IL-21 (γc-utilizing cytokines)
- Three disulfide bonds (Cys3-Cys127, Cys24-Cys65, Cys46-Cys99) — stabilize the compact bundle; essential for receptor binding
- N-glycosylation at Asn38; heavily O-glycosylated forms exist in some species (murine differs from human in N-glycosylation pattern)
- **Site I** on IL-4 (helix D face): contacts IL-4Rα α-subunit → high-affinity binding (Kd ~10⁻¹⁰ M)
- **Site II** on IL-4: contacts γc (type I) or IL-13Rα1 (type II) after IL-4Rα binding (induced fit); lower intrinsic affinity

**IL-4Rα (IL4R gene, chr16p12.1):**
- 140 kDa type I transmembrane glycoprotein; fibronectin type III extracellular domains (D1, D2) form a WSXWS-like motif characteristic of cytokine receptors
- Polymorphisms (R576 allele, Ile75Val): associated with atopic disease — enhance STAT6 signaling duration by reducing receptor downregulation rate
- Shed as **soluble IL-4Rα (sIL-4Rα)**: acts as a decoy receptor; pitakinra (IL-4 mutein) activates sIL-4Rα without γc engagement

**Common γ chain (γc; IL2RG gene, chr Xq13.1):**
- Shared by IL-2, IL-4, IL-7, IL-9, IL-15, IL-21 receptors; mutations → X-linked severe combined immunodeficiency (X-SCID)
- Constitutively associates with JAK3 at the cytoplasmic FERM domain

## Function

**IgE class switching (B cells):**
1. Th2 cell → IL-4 → B cell IL-4Rα/γc → STAT6 phosphorylation (Tyr641) → nuclear translocation
2. STAT6 → *Iε* (ε germline) transcription → AID (activation-induced cytidine deaminase) targets the Sμ→Sε switch region → DNA double-strand breaks → class switch recombination → IgE heavy chain expression
3. IL-4 also drives CD40L (on Th2 cells) + CD40 (on B cells) co-stimulation for B cell activation and germinal center entry
4. Plasma cells: secrete allergen-specific IgE → circulates → loads mast cells and basophils via FcεRI → sensitization

**Th2 differentiation:**
1. STAT6 → directly induces *GATA3* transcription → GATA-3 protein → binds *IL4*, *IL5*, *IL13* promoters → Th2 cytokine locus accessibility
2. GATA-3 also suppresses *IFNG* locus (Th1 commitment) and *TBX21* (T-bet expression) → mutual exclusivity with Th1
3. IL-4 inhibits Th1 differentiation: suppresses IL-12 signaling and IFN-γ production
4. IL-4 inhibits Th17 differentiation: suppresses RORγt; reduces IL-17A and IL-17F production

**Epithelial barrier suppression:**
- IL-4 + IL-13 → epithelial type II receptor → STAT6 → downregulation of *FLG* (filaggrin), *CLDN1* (claudin-1), *LOR* (loricrin), and *SPINK5* → weakened tight junctions and cornified envelope
- Suppression of β-defensin 2/3 and LL-37 → increased Staphylococcus aureus colonization (Staph aureus worsens AD in a vicious cycle)
- Increased TSLP and IL-33 secretion → ILC2 activation → more IL-4/IL-13 amplification (feedforward loop)

**M2 macrophage polarization:**
- IL-4 → macrophage type II receptor → STAT6 → arginase-1 (competes with iNOS for arginine) → reduced NO; IL-10, TGF-β, fibronectin, CD163, CD206 (mannose receptor) induction
- M2 macrophages promote wound healing, parasite expulsion, and fibrosis — and in pathology drive allergic tissue remodeling

## Mechanism

**Dupilumab pharmacology:**
- **Target:** IL-4Rα subunit (the shared component of both type I and type II receptors)
- **Mechanism:** Blocks IL-4Rα from assembling with either γc (type I) or IL-13Rα1 (type II) → prevents both IL-4 and IL-13 signaling simultaneously
- **Why this works:** IL-4 and IL-13 are the two dominant epithelial and B cell activators in type 2 inflammation; simultaneous blockade is more effective than blocking either alone

**Atopic dermatitis (SOLO 1/SOLO 2, LIBERTY AD trials) [^simpson-2016-dupilumab-ad]:**
- Dupilumab 300 mg SC Q2W: 51% EASI-75 (75% improvement in eczema area and severity index) vs. 15% placebo at 16 weeks
- Significant improvements in IGA 0/1 (clear/almost clear skin), pruritus NRS, sleep, and quality of life (DLQI)
- FDA approved 2017 for moderate-severe AD (inadequate response to topical therapy); age ≥6 months since expanded

**Asthma (LIBERTY Asthma QUEST trial):**
- Dupilumab 200/300 mg Q2W: 48-67% reduction in severe exacerbations vs. placebo in patients with baseline blood eosinophils ≥300/μL or FeNO ≥25 ppb
- Significant improvement in FEV₁ (0.32 L mean improvement)
- FDA approved as add-on maintenance for moderate-severe asthma ≥12 years; no requirement for elevated eosinophil biomarker

**JAK inhibitors as alternative IL-4 pathway blockade:**
- **Baricitinib** (JAK1/2 inhibitor): FDA approved for atopic dermatitis; 60% BREEZE-AD7 EASI-75 at 16 weeks with TCS
- **Upadacitinib** (JAK1 inhibitor): FDA approved; superior efficacy to dupilumab in head-to-head Heads Up trial (71% EASI-75 vs. 61%)
- **Abrocitinib** (JAK1 inhibitor): FDA approved; rapid itch relief (mechanism: JAK1 blockade reduces IL-31 and IL-4/IL-13 signaling on itch neurons)
- Trade-off: JAKi have broader immunosuppression (BOXED WARNING: malignancy, thrombosis, infection) vs. dupilumab's targeted IL-4Rα blockade

**IL-4 in GATA-3-driven oncogenesis:**
- Cutaneous T cell lymphoma (CTCL/MF, SS): GATA-3+ malignant T cells produce IL-4/IL-13 → immunosuppressive TME; IL-4 drives malignant T cell survival via STAT6 → Bcl-2/Bcl-xL
- AML and B-ALL: IL-4 can be pro-survival in some B cell malignancies via STAT6

## Connections

IL-4 → IL-4Rα/STAT6 → suppresses filaggrin, claudin-1, and loricrin → epithelial barrier dysfunction; drives Th2 polarization and IgE class switching; dupilumab (anti-IL-4Rα) blocks IL-4 and IL-13 → 51% EASI-75 in moderate-severe atopic dermatitis.

IL-4 drives Th2 airway inflammation, IgE production, and eosinophil recruitment in allergic asthma; type II receptor (IL-4Rα + IL-13Rα1) mediates mucus and AHR; dupilumab reduces severe asthma exacerbations by ~50% in patients with elevated eosinophils or FeNO.

IL-4 is the principal driver of B cell IgE class switching: IL-4 → STAT6 → ε germline transcription → AID-mediated switch recombination → IgE-secreting plasma cells; IL-13 shares this function via the type II IL-4Rα/IL-13Rα1 receptor.

IL-4 signals via JAK1 + JAK3 (type I, lymphocytes) or JAK1 + TYK2/JAK2 (type II, epithelium) → STAT6; baricitinib and upadacitinib (JAK1 inhibitors) reduce atopic dermatitis severity by blocking IL-4 and IL-13 downstream signaling.

PN shares Th2/Th22 axis with AD; IL-4 and IL-13 drive Th2 polarization in PN nodular skin; dupilumab (anti-IL-4Rα, blocking both IL-4 and IL-13) is FDA-approved for PN; LIBERTY-PN PRIME2: IGA success 37% vs. 22% placebo at 24 weeks.

[^brown-2004-il4-review]: Brown MA, Hural J. Functions of IL-4 and control of its expression. *Crit Rev Immunol.* 1997;17(1):1-32. [doi:10.1615/CritRevImmunol.v17.i1.10](https://doi.org/10.1615/CritRevImmunol.v17.i1.10) · [PubMed 9003261](https://pubmed.ncbi.nlm.nih.gov/9003261/)
[^simpson-2016-dupilumab-ad]: Simpson EL, Bieber T, Guttman-Yassky E, et al. Two Phase 3 Trials of Dupilumab versus Placebo in Atopic Dermatitis. *N Engl J Med.* 2016;375(24):2335-2348. [doi:10.1056/NEJMoa1610020](https://doi.org/10.1056/NEJMoa1610020) · [PubMed 27690741](https://pubmed.ncbi.nlm.nih.gov/27690741/)
