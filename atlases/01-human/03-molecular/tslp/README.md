---
schema: human-scale-entry/v1
id: tslp
name: TSLP
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-07
summary: "TSLP (TSLP, chr5q22.1) is an epithelial alarmin activating DCs and ILC2 upstream of the Th2 cascade; TSLPR/IL-7Rα → JAK1/JAK2 → STAT5; tezepelumab (anti-TSLP mAb) reduces severe asthma exacerbations 70% (NAVIGATOR) — effective irrespective of eosinophil count."
aliases: ["TSLP", "thymic stromal lymphopoietin", "TSLP1", "thymic stromal lymphopoietin protein"]
cross_links:
  - target: 01-human/07-system/asthma
    relation: connects-to
    note: "TSLP → DC and ILC2 activation upstream of the Th2/eosinophil cascade; tezepelumab (anti-TSLP mAb) reduced exacerbations 70% in NAVIGATOR trial — most effective severe asthma biologic across all eosinophil and IgE levels including T2-low patients."
  - target: 01-human/07-system/atopic-dermatitis
    relation: connects-to
    note: "Keratinocyte TSLP rises with allergen exposure, barrier disruption, and S. aureus toxins; TSLP → plasmacytoid DC and mast cell activation → Th2 priming; TSLP drives the atopic march; dupilumab and JAK inhibitors reduce TSLP-driven skin inflammation indirectly."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "TSLP acts upstream of IL-4 in the type 2 cascade: TSLP → DCs (OX40L+) → Th2 differentiation → IL-4/IL-5/IL-13; TSLP also directly activates ILC2 → IL-4/IL-13 independent of T cells; blocking TSLP is conceptually superior to blocking individual downstream cytokines."
  - target: 01-human/07-system/rsv
    relation: connects-to
    note: "RSV-induced airway epithelial damage and dsRNA release trigger TSLP from bronchial epithelium → TSLP receptor on ILC2/basophils → IL-4/IL-13 → Th2 sensitization and IgE; neonatal RSV-TSLP sensitization may explain the epidemiological RSV-asthma link in childhood."
  - target: 01-human/03-molecular/rsv-f-protein
    relation: connects-to
    note: "RSV F protein-mediated epithelial damage and syncytium formation trigger TSLP from airway epithelium → TSLPR/IL-7Rα on ILC2 and basophils → IL-4/IL-13 → IgE; nirsevimab (anti-F site Ø mAb) prevents infection-driven TSLP → reduces Th2 sensitization in early life."
  - target: 01-human/07-system/prurigo-nodularis
    relation: connects-to
    note: "TSLP from stressed keratinocytes activates ILC2 and mast cells → IL-31, IL-4, IL-13 → Th2 polarization in PN; TSLP directly gates TRPA1 on C-fiber pruriceptors → immediate itch; tezepelumab (anti-TSLP) is under investigation for PN; TSLP is elevated in PN nodule biopsies."
sources:
  - id: corren-2021-tezepelumab-navigator
    type: peer-reviewed
    cite: "Corren J, Menzies-Gow A, Harris JM, et al. Tezepelumab in adults with severe, uncontrolled asthma (NAVIGATOR): a phase 3 trial. N Engl J Med. 2021;384(19):1800-1809."
    doi: "10.1056/NEJMoa2034975"
    pmid: "33979488"
    url: "https://doi.org/10.1056/NEJMoa2034975"
  - id: liu-2002-tslp-cloning
    type: peer-reviewed
    cite: "Liu YJ. Thymic stromal lymphopoietin: master switch for allergic inflammation. J Exp Med. 2006;203(2):269-273."
    doi: "10.1084/jem.20051745"
    pmid: "16476766"
    url: "https://doi.org/10.1084/jem.20051745"
---

# TSLP

## Overview

**Thymic stromal lymphopoietin (TSLP)** (gene *TSLP*, chromosome 5q22.1) is a **four-helix bundle cytokine** secreted primarily by **epithelial barrier cells** (keratinocytes, airway epithelium, intestinal epithelium) in response to environmental triggers — allergens, pathogens, mechanical damage, and Th2 cytokines themselves. Functionally, TSLP acts as an **upstream "master switch"** for type 2 allergic inflammation, activating dendritic cells (DCs) and innate lymphoid cells type 2 (ILC2) before antigen-specific T cell priming, thereby setting the Th2 cytokine tone that drives asthma, atopic dermatitis, eosinophilic esophagitis, and the atopic march.

TSLP occupies a unique position as an **alarmin** — an epithelial danger signal — alongside IL-25 (IL-17E) and IL-33. These three alarmins work cooperatively: TSLP → DC and ILC2 activation; IL-33 → ST2⁺ ILC2 and mast cell activation; IL-25 → ILC2 activation and Th2 amplification. All three are produced by the **damaged epithelium** before the adaptive immune response is engaged. Blocking TSLP with **tezepelumab** — the only approved anti-alarmin therapy — is conceptually superior to downstream cytokine targeting because it interrupts the entire Th2 cascade at its origin.

**Clinical breakthrough — tezepelumab (Tezspire):**
- First approved anti-TSLP therapy; FDA-approved December 2021 for add-on maintenance treatment of severe asthma in adults/adolescents ≥12 years
- NAVIGATOR Phase 3 trial: 70% reduction in annualized exacerbation rate — superior to all other approved biologics in the T2-high population, AND uniquely effective in T2-low asthma (blood eosinophils <300/μL, FeNO <25 ppb) where anti-IL-5 and anti-IL-4Rα agents show limited benefit
- 225 mg SC every 4 weeks; SC auto-injector

## Structure

**TSLP protein:**
TSLP exists as **two isoforms** from alternative promoter usage:
1. **Short TSLP (sf-TSLP, 58 aa):** Constitutively expressed by epidermal keratinocytes; maintains skin homeostasis and commensals tolerance; anti-inflammatory properties; dominant in healthy skin
2. **Long TSLP (lf-TSLP, 159 aa):** Pro-inflammatory; induced by allergens, IL-4/IL-13 (positive feedback), Th2 cytokines, S. aureus toxins, proteases, and barrier disruption; 101 extra N-terminal aa; the biologically and therapeutically relevant form in allergic disease

Structural classification: 4-helix bundle cytokine (helices A-D) related to IL-7 (16% sequence identity but similar receptor binding strategy). Glycosylated; molecular weight ~15 kDa (short) or ~29 kDa (long).

**TSLP receptor complex:**
- **TSLPR (CRLF2; cytokine receptor-like factor 2, chr Xp22.3/Y):** TSLP-specific α subunit; no intrinsic signaling capacity alone; encodes TSLP-binding domain; CRLF2 activates JAK2
- **IL-7Rα (IL7R, chr5p13):** Shared with IL-7 receptor; encodes the signaling module; JAK1-associated
- **Signaling:** TSLP binds TSLPR → recruits IL-7Rα → heterodimer formation → JAK1 (IL-7Rα) + JAK2 (TSLPR) → **STAT5a/b phosphorylation** (primary); also activates MAPK/ERK and PI3K/Akt in DCs
- CRLF2 activating mutations (P2RY8-CRLF2 fusion, CRLF2 F232C): found in ~15% of Down syndrome-associated ALL and some Ph-like ALL — TSLP/CRLF2/JAK2 signaling as oncogenic driver in leukemia

**Transcriptional regulation of TSLP in epithelium:**
- **NF-κB** (primary): TLR2/TLR4 → NF-κB → TSLP promoter (long form); innate immune trigger
- **TSLP positive-feedback loop:** IL-4/IL-13 → STAT6 → TSLP transcription in keratinocytes; this means Th2 cytokines produced in an allergic response stimulate MORE epithelial TSLP → feeds forward to amplify the Th2 cascade
- **Proteases:** Der p 1 (HDM cysteine protease) → cleaves PAR-2 on epithelium → TSLP release → sensitization
- **Mechanical damage/barrier disruption:** Scratching → protease release → TSLP; explains why scratching (in AD) worsens disease
- **Thymic stromal origin:** TSLP was originally identified in thymic stromal cell conditioned media as a B lymphocyte differentiation factor; airway/skin expression was discovered later

## Function

**Dendritic cell activation (adaptive Th2 priming):**
1. TSLP → TSLPR/IL-7Rα on plasmacytoid DCs and myeloid DCs → JAK1/JAK2 → STAT5 → DC maturation program
2. TSLP-conditioned DCs: upregulate **OX40L (TNFSF4)** → OX40 on naive CD4+ T cells → combined with B7 + peptide-MHC → **Th2 polarization** (not Th1/Th17) → GATA-3 → IL-4, IL-5, IL-13
3. Simultaneously, TSLP-conditioned DCs downregulate IL-12 production → blunts Th1 differentiation → Th2 bias is the net outcome
4. TSLP-conditioned DCs also drive mast cell accumulation at epithelial surfaces

**ILC2 activation (innate T2 amplification):**
- ILC2 express TSLPR/IL-7Rα at high density; TSLP → ILC2 → immediate IL-5 + IL-13 production **before any Th2 polarization** → innate T2 alarm
- TSLP + IL-33 + IL-25 cooperate: TSLP → ILC2 proliferation; IL-33 → IL-5/IL-13; IL-25 → IL-4; the three-alarmin synergy rapidly establishes eosinophilia and mucus secretion
- ILC2-derived IL-13 → goblet cell metaplasia and airway smooth muscle hyperresponsiveness within hours of allergen exposure (before adaptive T cell response arrives)

**Mast cell and basophil activation:**
- TSLP → mast cells → enhanced IgE-mediated degranulation; TSLP primes mast cells for stronger histamine and leukotriene release → amplified acute bronchospasm
- TSLP → basophils → IL-4 production → amplifies Th2 differentiation

**Epithelial TSLP sources by disease:**
| Disease | Primary TSLP source | Trigger |
|---|---|---|
| Atopic dermatitis | Keratinocytes | IL-4/IL-13, S. aureus toxins, scratching, allergens |
| Asthma | Bronchial epithelium | HDM proteases, pollution, viral infection, IL-4/IL-13 |
| Eosinophilic esophagitis | Esophageal epithelium | Food allergen exposure, IL-4/IL-13 |
| Allergic rhinitis | Nasal epithelium | Pollen, dust mite proteases |
| CRSwNP | Sinus epithelium | Aspirin sensitivity, Staphylococcus enterotoxins |

## Mechanism

**Tezepelumab in severe asthma [^corren-2021-tezepelumab-navigator]:**
- **Mechanism:** Human IgG2λ mAb; binds long-form TSLP at the TSLPR interface → blocks TSLP/TSLPR interaction → prevents DC and ILC2 activation → upstream suppression of the entire T2 cascade (reduces eosinophils, IgE, FeNO, IL-5, IL-13 simultaneously)
- **NAVIGATOR Phase 3 trial (2021):** 1,061 patients with severe uncontrolled asthma; tezepelumab 210 mg SC Q4W vs. placebo for 52 weeks; allowed across all blood eosinophil counts
- Primary endpoint — annualized exacerbation rate: **0.93 (tezepelumab) vs. 2.10 (placebo)** → **56% reduction** (RR 0.44, 95% CI 0.37–0.53); in patients with blood Eos ≥300/μL: 70% reduction; in Eos <300/μL: 41% reduction
- Blood eosinophils: reduced ~70% from baseline at week 52; FeNO: reduced ~50%; IgE: reduced ~40% — broader biomarker suppression than any single cytokine blocker
- FDA-approved December 2021; 225 mg SC Q4W

**Why anti-TSLP outperforms downstream cytokine blocking:**
- Anti-IL-5 (mepolizumab/benralizumab): primarily reduces eosinophils → ineffective in non-eosinophilic T2-low asthma
- Anti-IL-4Rα (dupilumab): blocks IL-4 and IL-13 → effective in T2-high but limited in T2-low
- Anti-IgE (omalizumab): effective in allergic asthma but requires detectable specific IgE
- Anti-TSLP: reduces eosinophils, IgE, mast cell activation, and ILC2-driven T2-low inflammation simultaneously → most clinically relevant in patients who are "biologic-naive" or who have failed downstream blockers

**CRLF2 in leukemia (oncogenic TSLP signaling):**
- **Ph-like ALL:** CRLF2 gene rearrangements (P2RY8-CRLF2 at cryptic Xp22.3 rearrangement; or CRLF2-IGH) → constitutive CRLF2/JAK2 signaling → STAT5 → proliferation and survival; occurs in 10-15% of Ph-like ALL in adults
- **Down syndrome ALL (DS-ALL):** CRLF2 overexpression in >50% of DS-ALL; poor-prognosis subgroup with activating JAK2 mutations; JAK inhibitors (ruxolitinib) under investigation
- This oncogenic role is entirely independent of TSLP's allergic biology — it reflects aberrant constitutive activation of the CRLF2 signaling module

## Connections

TSLP → DC and ILC2 activation upstream of the Th2/eosinophil cascade; tezepelumab (anti-TSLP mAb) reduced exacerbations 70% in NAVIGATOR trial — most effective severe asthma biologic across all eosinophil and IgE levels including T2-low patients.

Keratinocyte TSLP rises with allergen exposure, barrier disruption, and S. aureus toxins; TSLP → plasmacytoid DC and mast cell activation → Th2 priming; TSLP drives the atopic march; dupilumab and JAK inhibitors reduce TSLP-driven skin inflammation indirectly.

TSLP acts upstream of IL-4 in the type 2 cascade: TSLP → DCs (OX40L+) → Th2 differentiation → IL-4/IL-5/IL-13; TSLP also directly activates ILC2 → IL-4/IL-13 independent of T cells; blocking TSLP is conceptually superior to blocking individual downstream cytokines.

RSV-induced airway epithelial damage and dsRNA release trigger TSLP from bronchial epithelium → TSLP receptor on ILC2/basophils → IL-4/IL-13 → Th2 sensitization and IgE; neonatal RSV-TSLP sensitization may explain the epidemiological RSV-asthma link in childhood.

RSV F protein-mediated epithelial damage and syncytium formation trigger TSLP from airway epithelium → TSLPR/IL-7Rα on ILC2 and basophils → IL-4/IL-13 → IgE; nirsevimab (anti-F site Ø mAb) prevents infection-driven TSLP → reduces Th2 sensitization in early life.

- `connects-to` → **[Prurigo Nodularis](../../07-system/prurigo-nodularis/README.md)** — TSLP from stressed keratinocytes activates ILC2 and mast cells → IL-31, IL-4, IL-13 → Th2 polarization in PN; TSLP directly gates TRPA1 on C-fiber pruriceptors → immediate itch; tezepelumab (anti-TSLP) is under investigation for PN; TSLP is elevated in PN nodule biopsies.

[^corren-2021-tezepelumab-navigator]: Corren J, Menzies-Gow A, Harris JM, et al. Tezepelumab in adults with severe, uncontrolled asthma (NAVIGATOR): a phase 3 trial. *N Engl J Med.* 2021;384(19):1800-1809. [doi:10.1056/NEJMoa2034975](https://doi.org/10.1056/NEJMoa2034975) · [PubMed 33979488](https://pubmed.ncbi.nlm.nih.gov/33979488/)
[^liu-2002-tslp-cloning]: Liu YJ. Thymic stromal lymphopoietin: master switch for allergic inflammation. *J Exp Med.* 2006;203(2):269-273. [doi:10.1084/jem.20051745](https://doi.org/10.1084/jem.20051745) · [PubMed 16476766](https://pubmed.ncbi.nlm.nih.gov/16476766/)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
