---
schema: human-scale-entry/v1
id: il-23
name: IL-23
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-07
summary: "IL-23 is a heterodimeric cytokine (IL-23p19/p40) produced by DCs and macrophages; IL-23 → IL-23R/JAK1/TYK2/STAT3 → Th17 cell maintenance and IL-17 production; IL-23 drives psoriasis and IBD; anti-IL-23p19 antibodies (risankizumab, guselkumab) are first-line biologics."
aliases: ["IL-23", "interleukin-23", "IL-23p19", "IL23A", "IL-23/IL-17 axis", "IL-23 cytokine", "anti-IL-23", "risankizumab target", "Th17 cytokine", "IL-23 IBD"]
cross_links:
  - target: 01-human/07-system/inflammatory-bowel-disease
    relation: connects-to
    note: "IL-23 drives Th17 polarization in the gut lamina propria → IL-17A, IL-22, and TNF-α → disruption of epithelial barrier and transmural inflammation in Crohn's disease; risankizumab (anti-IL-23p19) is FDA-approved for moderate-to-severe Crohn's disease and ulcerative colitis."
  - target: 01-human/07-system/psoriasis
    relation: connects-to
    note: "IL-23 from dermal DCs activates Th17 and γδ T cells → IL-17A/F and IL-22 → keratinocyte hyperproliferation, acanthosis, and neutrophil recruitment in psoriatic plaques; anti-IL-23p19 antibodies (risankizumab, guselkumab) achieve PASI 90 response in ~50% of patients."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "IL-23 signals via IL-23R/IL-12Rβ1 → JAK1/TYK2 → STAT3 homodimerization and nuclear translocation → transcription of IL-17A, IL-17F, IL-22, and RORγt; STAT3 is the master downstream effector of IL-23; JAK inhibitors (tofacitinib) block IL-23 signaling in psoriasis and IBD."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "IL-23 and IL-6 cooperate to drive Th17 cells: IL-6 + TGF-β initiates Th17 polarization from naive T cells; IL-23 amplifies and stabilizes the effector Th17 program; both cytokines are elevated in IBD, psoriasis, and RA; IL-6 blockade (tocilizumab) reduces Th17 responses in RA."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "IL-23 maintains the Th17 effector program and drives IL-17A via STAT3 → RORγt; anti-IL-23p19 antibodies (risankizumab) suppress IL-17A and achieve superior long-term psoriasis clearance vs anti-IL-17A antibodies; IL-23 sits upstream of IL-17A in the Th17 axis."
sources:
  - id: oppmann-2000-il23-p19
    type: peer-reviewed
    cite: "Oppmann B, Lesley R, Blom B, et al. Novel p19 protein engages IL-12p40 to form a cytokine, IL-23, with biological activities similar as well as distinct from IL-12. Immunity. 2000;13(5):715-725."
    doi: "10.1016/S1074-7613(00)00055-6"
    pmid: "11057895"
    url: "https://doi.org/10.1016/S1074-7613(00)00055-6"
  - id: gordon-2018-risankizumab-psoriasis
    type: peer-reviewed
    cite: "Gordon KB, Strober B, Lebwohl M, et al. Efficacy and safety of risankizumab in moderate-to-severe plaque psoriasis (UltIMMa-1 and UltIMMa-2). Lancet. 2018;392(10148):650-661."
    doi: "10.1016/S0140-6736(18)31713-6"
    pmid: "30097359"
    url: "https://doi.org/10.1016/S0140-6736(18)31713-6"
---

# IL-23

## Overview

**IL-23** (interleukin-23) is a heterodimeric cytokine composed of a unique **IL-23p19 subunit** (encoded by *IL23A*, 19 kDa) covalently linked to the **IL-12p40 subunit** (encoded by *IL12B*, 40 kDa) shared with IL-12. Oppmann et al. (2000) identified IL-23p19 and demonstrated that the IL-23 heterodimer has partially overlapping but functionally distinct activities compared to IL-12 [^oppmann-2000-il23-p19]. IL-12 drives IFN-γ and Th1 responses; IL-23 preferentially promotes and maintains **Th17 cells** — the key effectors of inflammatory bowel disease, psoriasis, ankylosing spondylitis, and psoriatic arthritis.

IL-23 is produced primarily by **dendritic cells, macrophages, and Langerhans cells** in response to pathogen-associated molecular patterns (TLR4, TLR9 ligands), cytokines (IL-1β, TNF-α), and danger signals. Blocking IL-23p19 with monoclonal antibodies (risankizumab, guselkumab, tildrakizumab) or the shared p40 subunit (ustekinumab, for both IL-12 and IL-23) is among the most effective therapeutic strategies in dermatology and gastroenterology. Selective p19 blockade is preferred over p40 blockade as it spares IL-12-driven Th1 immunity — reducing infection risk compared to dual IL-12/23 inhibition [^gordon-2018-risankizumab-psoriasis].

**IL-23 versus IL-12 comparison:**

| Feature | IL-12 | IL-23 |
|---|---|---|
| Unique subunit | p35 (IL12A) | p19 (IL23A) |
| Shared subunit | p40 (IL12B) | p40 (IL12B) |
| Receptor | IL-12Rβ1 + IL-12Rβ2 | IL-23R + IL-12Rβ1 |
| Primary effect | Th1 differentiation, IFN-γ | Th17 maintenance, IL-17 |
| Disease relevance | Anti-tumor, anti-mycobacterial | Psoriasis, IBD, SpA |
| Anti-p40 Abs | Ustekinumab (dual IL-12/23) | Ustekinumab (dual IL-12/23) |
| Anti-unique Ab | — | Risankizumab, guselkumab, tildrakizumab |

## Structure

**IL-23p19 subunit:** A four-helix bundle cytokine (α-helices A–D) with a short-chain cytokine fold. Contains an unpaired Cys54 that forms a disulfide with p40 (Cys177) in the heterodimer. Two N-linked glycosylation sites (Asn80, Asn143) are required for secretion. The p19-specific region forms the IL-23R binding interface; this is the target of risankizumab (anti-p19), guselkumab, and tildrakizumab.

**IL-12p40 subunit:** A large cytokine receptor–like molecule with immunoglobulin-like and fibronectin type III domains; acts as a scaffolding/secretion partner. Also forms p40 homodimers (IL-12p80) that can act as IL-12/23 antagonists.

**IL-23 receptor complex:** IL-23 binds the IL-23R extracellular domain via p19, and the IL-12Rβ1 chain via p40. IL-23R expression is restricted to activated T cells, ILCs (innate lymphoid cells group 3 = ILC3), γδ T cells, and NK cells — explaining the tissue specificity of IL-23 responses.

## Function

**Th17 cell maintenance:** IL-6 + TGF-β initiate Th17 differentiation from naive CD4⁺ T cells via STAT3 and RORγt. IL-23 does not initiate Th17 differentiation but is essential for the expansion and long-term maintenance of effector Th17 cells and Th17 memory cells. Th17 cells stimulated by IL-23 produce:
- **IL-17A and IL-17F** → act on epithelial cells and fibroblasts → CXCL1/8 (neutrophil recruitment), S100A7/8/9 (antimicrobial), keratinocyte proliferation
- **IL-22** → epithelial cell proliferation and survival, anti-bacterial defense (β-defensins, RegIII)
- **GM-CSF** → promotes myeloid cell survival and activation

**ILC3 activation:** IL-23 activates group 3 innate lymphoid cells (ILC3) and γδ T cells in the gut and skin → innate IL-17 and IL-22 production → amplifies mucosal inflammation before adaptive T cell responses develop.

**Pathogenic tissue-resident T cells:** IL-23 programs tissue-resident memory Th17 cells (Trm17) in psoriatic skin and IBD mucosa; these cells sustain inflammation even after systemic Th17 suppression, explaining partial non-response to anti-TNF biologics.

## Mechanism

**IL-23 signaling cascade:**
1. IL-23 binds IL-23R (via p19) → recruits IL-12Rβ1 (via p40) to form ternary complex
2. Pre-associated JAK2 (IL-23R) and TYK2 (IL-12Rβ1) trans-phosphorylate each other
3. JAK1/TYK2-phosphorylated receptor ITAMs recruit STAT3 → STAT3 Tyr705 phosphorylation → STAT3 homodimerization → nuclear translocation
4. Nuclear STAT3 binds SIE/TTCNNNGAA elements → transcription of *RORC* (RORγt), *IL17A*, *IL17F*, *IL22*, *IL23R* (positive feedback loop)
5. RORγt co-activates IL-17A/F and IL-22 promoters, establishing the Th17 effector program

**Negative regulation:** SOCS3 (STAT3-induced suppressor of cytokine signaling) provides delayed negative feedback by inhibiting JAK2/TYK2. IL-10 and TGF-β suppress IL-23R expression. The immunosuppressive cytokine IL-35 (EBI3/IL-12A heterodimer) and regulatory T cells (Treg) counterbalance IL-23/Th17 pathways in healthy tissue.

**Therapeutic agents:**
- **Ustekinumab** (anti-p40; Janssen): approved for psoriasis, Crohn's, UC, PsA; blocks both IL-12 and IL-23
- **Risankizumab** (anti-p19; AbbVie): approved for psoriasis, Crohn's (2022), UC (2023); PASI 90 in ~57% at week 52
- **Guselkumab** (anti-p19; Janssen): approved for psoriasis and PsA; long-term remission after withdrawal
- **Tildrakizumab** (anti-p19; Sun/Almirall): approved for psoriasis
- **Mirikizumab** (anti-p19; Lilly): approved for UC (2023)

## Connections

IL-23 drives Th17 polarization in the gut lamina propria → IL-17A, IL-22, and TNF-α → disruption of epithelial barrier and transmural inflammation in Crohn's disease; risankizumab (anti-IL-23p19) is FDA-approved for moderate-to-severe Crohn's disease and ulcerative colitis.

IL-23 from dermal DCs activates Th17 and γδ T cells → IL-17A/F and IL-22 → keratinocyte hyperproliferation, acanthosis, and neutrophil recruitment in psoriatic plaques; anti-IL-23p19 antibodies (risankizumab, guselkumab) achieve PASI 90 response in ~50% of patients.

IL-23 signals via IL-23R/IL-12Rβ1 → JAK1/TYK2 → STAT3 homodimerization and nuclear translocation → transcription of IL-17A, IL-17F, IL-22, and RORγt; STAT3 is the master downstream effector of IL-23; JAK inhibitors (tofacitinib) block IL-23 signaling in psoriasis and IBD.

IL-23 and IL-6 cooperate to drive Th17 cells: IL-6 + TGF-β initiates Th17 polarization from naive T cells; IL-23 amplifies and stabilizes the effector Th17 program; both cytokines are elevated in IBD, psoriasis, and RA; IL-6 blockade (tocilizumab) reduces Th17 responses in RA.

IL-23 maintains the Th17 effector program and drives IL-17A via STAT3 → RORγt; anti-IL-23p19 antibodies (risankizumab) suppress IL-17A and achieve superior long-term psoriasis clearance vs anti-IL-17A antibodies; IL-23 sits upstream of IL-17A in the Th17 axis.
