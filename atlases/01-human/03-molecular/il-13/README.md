---
schema: human-scale-entry/v1
id: il-13
name: Interleukin-13
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-07
summary: "IL-13 (IL13, chr5q31.1) signals via IL-13Rα1/IL-4Rα type II receptor → JAK1/TYK2 → STAT6; drives goblet cell metaplasia, airway hyperresponsiveness, skin barrier disruption, and fibrosis; tralokinumab and lebrikizumab (anti-IL-13 mAbs) are FDA-approved for atopic dermatitis."
aliases: ["IL-13", "interleukin-13", "IL13", "ALRH", "P600", "NC30 cytokine"]
cross_links:
  - target: 01-human/07-system/atopic-dermatitis
    relation: connects-to
    note: "IL-13 → IL-13Rα1/IL-4Rα → STAT6 → FLG, claudin-1, loricrin suppression → barrier failure; IL-13 is the dominant effector in chronic AD lichenification and fibrosis; tralokinumab (ECZTRA 1/2: 38% IGA 0/1) and lebrikizumab (ADVOCATE: 43% IGA 0/1) target IL-13 specifically."
  - target: 01-human/07-system/asthma
    relation: connects-to
    note: "IL-13 → STAT6 → MUC5AC transcription (goblet cell metaplasia) and eotaxin production → airway eosinophilia and mucus plugging; IL-13 directly induces airway smooth muscle hyperresponsiveness via Gq receptor upregulation; FeNO is an indirect read-out of IL-13 airway activity."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "IL-13 and IL-4 share the type II receptor (IL-4Rα/IL-13Rα1) on non-hematopoietic cells → both activate STAT6; IL-4 additionally activates type I (IL-4Rα/γc) on lymphocytes driving Th2 differentiation; dupilumab (anti-IL-4Rα) blocks both IL-4 and IL-13 signaling simultaneously."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "IL-13 is the dominant type 2 pro-fibrotic cytokine: IL-13 → IL-13Rα1/STAT6 → TGF-β1 induction in fibroblasts and macrophages → myofibroblast differentiation → collagen deposition; IL-13/TGF-β synergy drives lung fibrosis in asthma remodeling and idiopathic pulmonary fibrosis."
sources:
  - id: wills-karp-1998-il13-asthma
    type: peer-reviewed
    cite: "Wills-Karp M, Luyimbazi J, Xu X, et al. Interleukin-13: central mediator of allergic asthma. Science. 1998;282(5397):2258-2261."
    doi: "10.1126/science.282.5397.2258"
    pmid: "9856949"
    url: "https://doi.org/10.1126/science.282.5397.2258"
  - id: wollenberg-2021-tralokinumab
    type: peer-reviewed
    cite: "Wollenberg A, Blauvelt A, Guttman-Yassky E, et al. Tralokinumab for moderate-to-severe atopic dermatitis: results from two 52-week, randomized, double-blind, multicentre, placebo-controlled phase III trials (ECZTRA 1 and ECZTRA 2). Br J Dermatol. 2021;184(3):437-449."
    doi: "10.1111/bjd.19574"
    pmid: "33000465"
    url: "https://doi.org/10.1111/bjd.19574"
---

# Interleukin-13

## Overview

**Interleukin-13 (IL-13)** (gene *IL13*, chromosome 5q31.1) is a **12 kDa Th2 cytokine** that shares approximately 25% amino acid identity with IL-4 and signals through a **partially shared receptor complex** — the type II receptor (IL-4Rα/IL-13Rα1) expressed on **non-hematopoietic cells** including airway epithelium, smooth muscle, fibroblasts, and keratinocytes. This shared signaling explains the biological overlap between IL-4 and IL-13 in driving **goblet cell hyperplasia, IgE production, and fibrosis**, and underpins the success of dupilumab (which blocks IL-4Rα, neutralizing both cytokines simultaneously) in T2-high inflammatory diseases.

Encoded within the **Th2 cytokine cluster** on chromosome 5q31.1 alongside IL-4, IL-5, IL-3, and GM-CSF, IL-13 is produced predominantly by **Th2 cells, ILC2 (innate lymphoid cells type 2), mast cells, basophils, and NKT cells**. Unlike IL-4 (which acts primarily on lymphocytes to drive Th2 differentiation), IL-13 is the **dominant effector cytokine** in established type 2 inflammation — driving the tissue-level pathology of asthma, atopic dermatitis, and fibrosis.

**Three critical IL-13-specific biological effects not shared with IL-4:**
1. **Goblet cell metaplasia and mucus hypersecretion** — STAT6 → MUC5AC transcription in airway and esophageal epithelium; mucus plugging in fatal asthma; eosinophilic esophagitis (EoE) eotaxin-3 production
2. **Direct airway smooth muscle hyperresponsiveness (AHR)** — IL-13 receptor on smooth muscle → TGF-β and calcium channel upregulation → intrinsic contractility increase independent of neural/mast cell signals
3. **Dominant pro-fibrotic type 2 cytokine** — TGF-β1 induction in fibroblasts and M2 macrophages → collagen deposition; drives liver, lung, and skin fibrosis in chronic T2 diseases

**Therapeutic landscape — IL-13-specific biologics:**
- **Tralokinumab (Adbry):** Anti-IL-13 IgG4 mAb; FDA-approved 2021 for moderate-severe AD; ECZTRA 1/2 trials: 15-16 weeks IGA 0/1 in 16-22%; 52-week 38-40% IGA 0/1 with TCS rescue
- **Lebrikizumab (Ebglyss):** Anti-IL-13 IgG4 mAb with high IL-13 affinity; FDA-approved 2023; ADVOCATE 1/2: 43% IGA 0/1 at 16 weeks (Q2W dosing — highest AD biologic response rates reported)
- **Cendakimab:** Small-molecule IL-13Rα2 signaling blocker; Phase 2 for EoE

## Structure

**IL-13 protein architecture:**
IL-13 is a **monomeric 132-aa glycoprotein** (after 20-aa signal peptide cleavage; mature form 112 aa, ~12 kDa) adopting a **4-helix bundle** fold (helices A–D) shared with IL-4, IL-5, GM-CSF, and other hematopoietin family cytokines. Two disulfide bonds (Cys49-Cys74, Cys86-Cys90) stabilize the bundle structure. The sequence divergence from IL-4 at sites I and III (receptor-binding surfaces) explains the differential receptor binding despite shared topology.

**Receptor system:**
- **IL-13Rα1 (IL13RA1, chr9p24):** Moderate-affinity IL-13 binding (Kd ~30 nM alone); assembles with IL-4Rα → high-affinity **type II signaling complex** (Kd ~5 pM); expressed on epithelium, smooth muscle, endothelium, fibroblasts, monocytes/macrophages — NOT on T/B cells or eosinophils
- **IL-4Rα (IL4RA, chr16p12):** Shared subunit; binds IL-13Rα1 → type II complex; binds γc → type I complex (IL-4-only); the signaling subunit that activates JAK1
- **Type II signaling:** IL-13 binds IL-13Rα1 (site II) → recruits IL-4Rα → JAK1 (IL-4Rα-associated) + TYK2 (IL-13Rα1-associated, some sources report JAK2) → **STAT6 Tyr641 phosphorylation** → STAT6 homodimerization → nuclear translocation → gene transcription
- **IL-13Rα2 (IL13RA2, chr Xq23):** High-affinity IL-13 decoy receptor (Kd ~0.5 nM); does NOT couple to JAK/STAT6; historically considered a pure decoy; newer data indicate IL-13Rα2 may activate AP-1/TGF-β in some contexts; expressed on fibroblasts and cancer cells; functions as feedback inhibitor of IL-13 signaling
- **IL-4Rα blockade (dupilumab):** Blocks both type I (IL-4 signaling in lymphocytes) and type II (IL-13 and IL-4 in non-hematopoietic cells) → broadest T2 suppression; mechanistically superior to targeting either IL-4 or IL-13 alone for diseases with both lymphocyte and epithelial pathology

**STAT6 target genes (key IL-13/IL-4 transcriptional outputs on epithelium/fibroblasts):**
- *MUC5AC*: goblet cell mucin → mucus hypersecretion (asthma, EoE)
- *CCL26* (eotaxin-3): eosinophil chemoattractant → eosinophilic disease
- *PERIOSTIN* (POSTN): ECM protein; fibroblast-derived; serum periostin = T2 asthma biomarker
- *FLG* (filaggrin): STAT6 *suppresses* FLG → barrier dysfunction (skin)
- *TGF-β1*: pro-fibrotic signaling (lung, skin, esophagus)
- *ARG1* (arginase-1): M2 macrophage polarization → tissue repair / pro-fibrotic phenotype

## Function

**Goblet cell metaplasia and mucus hypersecretion:**
- IL-13 → STAT6 → **MUC5AC** and **MUC5B** transcription in airway goblet cells → gel-forming mucins → mucus plugging of small airways → major cause of mortality in fatal asthma (post-mortem: mucus plugs in 80%+ of fatal asthma airways)
- IL-13 → STAT6 → **SPDEF** (SAM pointed domain ETS factor) → goblet cell differentiation gene program; SPDEF knockout mice resist IL-13-driven goblet cell metaplasia
- In **eosinophilic esophagitis (EoE):** food allergen sensitization → IL-13 from local Th2/mast cells → STAT6 → **CCL26 (eotaxin-3)** from esophageal epithelium → eosinophil recruitment → >15 eos/hpf (diagnostic threshold); EoE is arguably the purest IL-13-driven disease

**Airway smooth muscle and AHR:**
- IL-13 receptors on airway smooth muscle (ASM) → STAT6 → upregulates **Gq-coupled receptors** (muscarinic M3, histamine H1, bradykinin B2) → increased contractile response per stimulus → BHR independent of airway inflammation
- IL-13 → STAT6 → **TGF-β2** in ASM cells → SMC hypertrophy → increased ASM mass → chronic BHR amplification
- FeNO (fractional exhaled nitric oxide): IL-13 → STAT6 → **iNOS** in airway epithelium → NO production → FeNO elevation; FeNO >25 ppb correlates with IL-13-mediated T2 airway inflammation and biologic response

**Fibrosis and tissue remodeling:**
- IL-13 is the primary type 2 pro-fibrotic cytokine: IL-13 → IL-13Rα1/STAT6 → **TGF-β1 and TGF-β2** induction in fibroblasts and M2 macrophages → SMAD2/3 → myofibroblast differentiation → collagen I/III deposition
- IL-13 + TGF-β1 synergy: IL-13 drives M2 macrophage polarization (arginase-1+, CCL17+, CCL18+ phenotype) → macrophages produce TGF-β1 → amplifies fibrosis; IL-13 also directly activates fibroblasts independent of TGF-β
- **Skin:** IL-13 → STAT6 suppresses FLG, claudin-1, loricrin → barrier failure → allergen penetration → sensitization cycle; chronic IL-13 → TGF-β → skin lichenification in chronic AD
- **Lung:** IL-13 → subepithelial fibrosis and smooth muscle hypertrophy in asthma remodeling; IL-13 is implicated in early-stage IPF through M2 macrophage activation (not IL-4, which is not elevated in IPF)

**IgE class switching:**
- IL-13 drives B cell IgE class switching via the same STAT6 → ε germline transcript mechanism as IL-4, though with lower potency than IL-4; IL-13Rα1 is expressed on B cells in mice but weakly in humans — the IgE-switching role is primarily mediated through IL-4 in human disease, with IL-13 providing additional activity at high concentrations

**Type 2 macrophage (M2) polarization:**
- IL-13 (and IL-4) → STAT6 → M2 macrophage marker induction: arginase-1 (*ARG1*), *MRC1* (CD206 mannose receptor), *CCL17* (TARC), *CCL18*, *FIZZ1/RELM-α*, *YM1/CHI3L3* → wound healing phenotype; M2 macrophages → TGF-β and matrix metalloproteinase secretion → fibrosis progression

## Mechanism

**Tralokinumab mechanism (anti-IL-13 IgG4κ) [^wollenberg-2021-tralokinumab]:**
- Binds IL-13 with high affinity → prevents IL-13 binding to both IL-13Rα1 (signaling) and IL-13Rα2 (decoy); IgG4 backbone → minimal immune effector function
- **ECZTRA 1 (n=802) and ECZTRA 2 (n=794):** 52-week, double-blind, placebo-controlled trials in moderate-severe AD; tralokinumab 300 mg SC Q2W vs. placebo
- Primary endpoint (IGA 0/1 at 16 weeks): ECZTRA 1: 15.8% vs. 7.1% placebo; ECZTRA 2: 22.2% vs. 10.9% placebo (both p<0.001); EASI-75: ~25%
- Responders at 16 weeks re-randomized to Q2W vs. Q4W maintenance: similar sustained response at 52 weeks with Q4W → less frequent dosing option for maintenance
- FDA-approved December 2021 for adults with moderate-severe AD

**Lebrikizumab mechanism (anti-IL-13 IgG4κ, Ebglyss):**
- High-affinity IL-13 binding (Kd ~1 pM) → blocks site I of IL-13/IL-13Rα1 interaction specifically; does not bind IL-13Rα2; IgG4 backbone
- **ADVOCATE 1 and 2 trials:** Lebrikizumab 250 mg Q2W (after 2 loading doses 500 mg) vs. placebo in moderate-severe AD; primary endpoint: IGA 0/1 at 16 weeks
- ADVOCATE 1: 43.1% vs. 12.7% placebo; ADVOCATE 2: 33.2% vs. 10.8% — highest AD biologic trial response rates reported
- FDA-approved September 2023; Q2W dosing (less frequent than dupilumab initially, comparable with Q4W maintenance)

**Why block IL-13 specifically vs. dupilumab (IL-4Rα)?**
- Both tralokinumab/lebrikizumab and dupilumab are effective in AD; direct head-to-head data limited
- IL-13-specific blockade spares IL-4 signaling on lymphocytes → theoretically preserves some Treg/IL-10 function; IL-4Rα blockade (dupilumab) is broader (blocks both) → may be more effective for severe disease with prominent lymphocyte/IgE component
- Choice is often driven by prior biologic history, dosing preference, and cost

**Biomarkers predicting IL-13 activity:**
| Biomarker | Source | IL-13 connection |
|---|---|---|
| FeNO (>25 ppb) | Airway epithelium NO | IL-13 → iNOS → FeNO (T2 asthma marker) |
| Serum periostin (>25 ng/mL) | Fibroblasts | IL-13/IL-4 → POSTN transcription |
| Blood eosinophils (≥300/μL) | Bone marrow/IL-5 | IL-13 drives CCL26 → eotaxin-3 → eosinophil recruitment; indirect correlation |
| Total IgE (>150 IU/mL) | B cells via STAT6 | IL-13 (and IL-4) class switching |
| Serum CCL17/TARC (>350 ng/L) | M2 macrophages, DCs | Direct IL-13 → STAT6 → CCL17 induction; AD disease activity biomarker |

## Connections

IL-13 → IL-13Rα1/IL-4Rα → STAT6 → FLG, claudin-1, loricrin suppression → barrier failure; IL-13 is the dominant effector in chronic AD lichenification and fibrosis; tralokinumab (ECZTRA 1/2: 38% IGA 0/1) and lebrikizumab (ADVOCATE: 43% IGA 0/1) target IL-13 specifically.

IL-13 → STAT6 → MUC5AC transcription (goblet cell metaplasia) and eotaxin production → airway eosinophilia and mucus plugging; IL-13 directly induces airway smooth muscle hyperresponsiveness via Gq receptor upregulation; FeNO is an indirect read-out of IL-13 airway activity.

IL-13 and IL-4 share the type II receptor (IL-4Rα/IL-13Rα1) on non-hematopoietic cells → both activate STAT6; IL-4 additionally activates type I (IL-4Rα/γc) on lymphocytes driving Th2 differentiation; dupilumab (anti-IL-4Rα) blocks both IL-4 and IL-13 signaling simultaneously.

IL-13 is the dominant type 2 pro-fibrotic cytokine: IL-13 → IL-13Rα1/STAT6 → TGF-β1 induction in fibroblasts and macrophages → myofibroblast differentiation → collagen deposition; IL-13/TGF-β synergy drives lung fibrosis in asthma remodeling and idiopathic pulmonary fibrosis.

[^wills-karp-1998-il13-asthma]: Wills-Karp M, Luyimbazi J, Xu X, et al. Interleukin-13: central mediator of allergic asthma. *Science.* 1998;282(5397):2258-2261. [doi:10.1126/science.282.5397.2258](https://doi.org/10.1126/science.282.5397.2258) · [PubMed 9856949](https://pubmed.ncbi.nlm.nih.gov/9856949/)
[^wollenberg-2021-tralokinumab]: Wollenberg A, Blauvelt A, Guttman-Yassky E, et al. Tralokinumab for moderate-to-severe atopic dermatitis: results from two 52-week, randomized, double-blind, multicentre, placebo-controlled phase III trials (ECZTRA 1 and ECZTRA 2). *Br J Dermatol.* 2021;184(3):437-449. [doi:10.1111/bjd.19574](https://doi.org/10.1111/bjd.19574) · [PubMed 33000465](https://pubmed.ncbi.nlm.nih.gov/33000465/)
