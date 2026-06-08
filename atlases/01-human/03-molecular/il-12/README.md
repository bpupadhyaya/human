---
schema: human-scale-entry/v1
id: il-12
name: IL-12
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-08
summary: "IL-12 (p70; IL12A+IL12B heterodimer) is the master Th1-polarizing cytokine; produced by dendritic cells → JAK2/TYK2/STAT4 → IFN-γ from NK/T cells; IL12B/IL12RB1 loss → Mendelian susceptibility to mycobacterial disease; ustekinumab (anti-p40) → TB reactivation risk."
aliases: ["interleukin-12", "IL-12p70", "IL12A", "IL12B", "p35/p40 heterodimer", "NKSF", "natural killer cell stimulatory factor", "CLMF", "cytotoxic lymphocyte maturation factor"]
sources:
  - id: trinchieri-2003-il12-review
    type: peer-reviewed
    cite: "Trinchieri G. Interleukin-12 and the regulation of innate resistance and adaptive immunity. Nat Rev Immunol. 2003;3(2):133-146."
    doi: "10.1038/nri1001"
    pmid: "12563297"
    url: "https://doi.org/10.1038/nri1001"
    accessed: "2026-06-08"
  - id: altare-1998-il12r-msmd
    type: peer-reviewed
    cite: "Altare F, Durandy A, Lammas D, et al. Inherited interleukin 12 deficiency in a child with bacille Calmette-Guérin and Salmonella enteritidis disseminated infection. J Clin Invest. 1998;102(12):2035-2040."
    doi: "10.1172/JCI4950"
    pmid: "9854042"
    url: "https://doi.org/10.1172/JCI4950"
    accessed: "2026-06-08"
cross_links:
  - target: 01-human/07-system/tuberculosis
    relation: connects-to
    note: "IL-12/IFN-γ axis is essential for TB immunity; IL12B or IL12RB1 loss → MSMD (recurrent BCG/NTM disease); granuloma integrity requires sustained IL-12 + TNF-α; ustekinumab (anti-IL-12/23 p40) → latent TB reactivation risk; IGRA screening mandatory before therapy."
  - target: 01-human/03-molecular/ifn-gamma
    relation: modulates
    note: "IL-12 is the primary inducer of IFN-γ from NK and T cells: IL-12 → JAK2/TYK2 → STAT4 → T-bet → IFN-γ; IFN-γ feeds back to activate macrophages → more IL-12 (positive loop); disrupting the IL-12/IFN-γ axis → susceptibility to intracellular pathogens (MTB, Leishmania)."
  - target: 01-human/07-system/anemia-of-chronic-disease
    relation: connects-to
    note: "IL-12 drives Th1 activation → IFN-γ + TNF-α → macrophage activation → IL-6 → hepcidin; chronic infections driving IL-12/IFN-γ (TB, HIV, leishmaniasis) cause ACD; IL-12-mediated Th1 inflammation restricts iron from intracellular pathogens via nutritional immunity."
  - target: 01-human/07-system/immune-system
    relation: modulates
    note: "IL-12 is a master regulator of Th1 adaptive immunity: drives T-bet/IFN-γ polarization, activates NK cytotoxicity, promotes CTL development; required for effective immunity against intracellular bacteria (MTB, Listeria), dimorphic fungi, and some viruses; counterbalanced by IL-10."
  - target: 01-human/07-system/hiv-aids
    relation: connects-to
    note: "HIV-AIDS depletes CD4+ Th1 cells and impairs IL-12/IFN-γ axis: DCs from AIDS patients produce less IL-12; IL-12 deficiency underlies susceptibility to TB, NTM, Leishmania, and dimorphic fungi; ART + IFN-γ supplementation may partially restore Th1 immunity."
  - target: 01-human/07-system/leishmaniasis
    relation: connects-to
    note: "Leishmania resistance is determined by IL-12-driven Th1 polarization: IL-12 → STAT4 → IFN-γ → iNOS → NO kills intracellular amastigotes; IL-12 polymorphisms (IL12B) influence VL susceptibility; L. donovani subverts TLR2 to suppress IL-12 production and evade Th1 immunity."
---

# IL-12

## Overview

Interleukin-12 (IL-12) is the master Th1-polarizing cytokine — the molecular bridge between innate pattern recognition and adaptive cell-mediated immunity. First described in 1989 by Stern et al. as "natural killer cell stimulatory factor" (NKSF) and independently as "cytotoxic lymphocyte maturation factor" (CLMF), IL-12 is a heterodimeric glycoprotein (~70 kDa) produced primarily by dendritic cells (DCs) and macrophages in response to microbial stimuli [^trinchieri-2003-il12-review].

Its central role is to couple innate sensing of intracellular pathogens — particularly *Mycobacterium tuberculosis*, *Leishmania*, *Listeria*, and dimorphic fungi — to the polarization of CD4⁺ T cells toward the IFN-γ-producing Th1 phenotype required for macrophage activation and pathogen killing.

Two clinical implications define IL-12's translational significance:
- **MSMD (Mendelian susceptibility to mycobacterial disease):** Loss-of-function mutations in *IL12B* or *IL12RB1* → profound susceptibility to BCG, non-tuberculous mycobacteria (NTM), and *Salmonella* in otherwise healthy children [^altare-1998-il12r-msmd]
- **Iatrogenic immunosuppression:** Ustekinumab (anti-p40, blocking both IL-12 and IL-23) used in psoriasis, psoriatic arthritis, and IBD carries latent TB reactivation risk comparable to anti-TNF agents

## Structure

IL-12 is a **disulfide-linked heterodimer** composed of two subunits encoded by distinct genes on separate chromosomes:

| Subunit | Gene | Chromosome | Molecular weight | Name |
|:--------|:-----|:-----------|:-----------------|:-----|
| **p35** | *IL12A* | 3p12.3 | 35 kDa | α-chain |
| **p40** | *IL12B* | 5q33.3 | 40 kDa | β-chain |

**IL-12p70** (p35+p40 disulfide-linked) is the biologically active form. The p40 subunit also exists as a **p40 homodimer** (IL-12p80) that competitively antagonises IL-12 signalling at the receptor level.

### IL-12 Receptor Complex

The IL-12 receptor is a **heterodimer of IL-12Rβ1 (IL12RB1) + IL-12Rβ2 (IL12RB2)**:
- IL-12Rβ1 binds the p40 subunit (chain shared with IL-23, explaining why mutations in IL12RB1 affect both IL-12 and IL-23 signalling)
- IL-12Rβ2 confers high-affinity p35 binding and is the signalling chain (associates with TYK2)
- Expression: induced on T cells and NK cells following TCR/cytokine activation; low or absent on naïve T cells → IL-12 signalling depends on prior priming

### IL-12 Family

IL-12 is the founding member of a cytokine family that shares subunits:

| Cytokine | Subunits | Principal Source | Primary Function |
|:---------|:---------|:-----------------|:----------------|
| **IL-12** | p35 + p40 | DC, macrophage | Th1 polarization, IFN-γ induction |
| **IL-23** | p19 + p40 | DC, macrophage | Th17 maintenance, mucosal immunity |
| **IL-27** | EBI3 + p28 | DC | Early Th1 priming; also anti-inflammatory via IL-10 |
| **IL-35** | EBI3 + p35 | Treg | Immunosuppressive; promotes IL-35+ Treg expansion |
| **IL-39** | IL-23A + EBI3 | B cells | B cell activation; role unclear |

The shared p40 subunit is the target of **ustekinumab** (Stelara), which blocks both IL-12 and IL-23, explaining its efficacy in Th1- and Th17-driven diseases (psoriasis, Crohn's disease, ulcerative colitis) and its risk of impairing IL-12-dependent antimycobacterial immunity.

## Function

IL-12 executes four major immunological functions:

1. **Th1 polarization** — IL-12 binding to IL-12Rβ1+IL-12Rβ2 on primed CD4⁺ T cells → STAT4 → T-bet → IFN-γ production; T-bet also represses GATA-3 (Th2) and RORγt (Th17), locking in Th1 fate
2. **NK cell activation** — IL-12 + IL-18 → synergistic IFN-γ burst from NK cells within hours of infection; NK-derived IFN-γ provides early macrophage activation before adaptive T cell responses mature
3. **CD8⁺ CTL expansion** — IL-12 promotes cytotoxic T lymphocyte (CTL) differentiation and memory CD8⁺ T cell formation; STAT4 drives perforin and granzyme B expression
4. **Macrophage-DC feedback loop** — IFN-γ activated macrophages produce more IL-12 → amplified Th1 response; TNF-α cooperates with IL-12 to sustain granuloma integrity

**Antimycobacterial immunity** — IL-12 → IFN-γ → macrophage activation → phagosome acidification, ROS burst, reactive nitrogen intermediates, cathelicidin (LL-37) production → MTB killing. This circuit is indispensable: humans lacking any component (IL12B, IL12RB1, IFNGR1, IFNGR2, STAT1, IRF8) develop MSMD.

## Mechanism

### JAK2/TYK2/STAT4 Signalling

IL-12 receptor signalling:

1. IL-12p70 binds IL-12Rβ1 (via p40) + IL-12Rβ2 (via p35) → receptor dimerisation
2. **JAK2** (constitutively associated with IL-12Rβ2) + **TYK2** (associated with IL-12Rβ1) transphosphorylate each other
3. Activated JAK2/TYK2 phosphorylate receptor cytoplasmic tyrosines → docking sites for **STAT4**
4. **STAT4** phosphorylation (Tyr693) → dimerisation → nuclear translocation → **T-bet**, **IFN-γ**, **IL-18Rα** gene transactivation
5. STAT4 also induces **RUNX3** → CTL differentiation
6. **Negative regulation:** IL-10 (via STAT3) suppresses DC IL-12 production; IL-27 (via STAT1) can inhibit Th17 but also modulates Th1; SOCS1/SOCS3 (induced by IFN-γ) provide negative feedback on JAK signalling

### Dendritic Cell IL-12 Production

DCs produce IL-12p70 upon stimulation via:
- **TLR4** (LPS, gram-negative bacteria)
- **TLR2** (mycobacterial cell wall components; though ManLAM signals via TLR2 → IL-10, inhibiting IL-12)
- **TLR9** (CpG DNA)
- **NOD2** (muramyl dipeptide)
- **CD40L–CD40 interaction** — T cell help amplifies DC IL-12 production

Importantly, **DCs produce IL-12p70 only transiently** during the first 24–48 hours of activation; IL-12 production is then suppressed by IL-10 and prostaglandin E2 — a feature that limits immunopathology but means early IL-12 priming is irreplaceable.

### MSMD Genetic Architecture

Mendelian susceptibility to mycobacterial disease (MSMD; OMIM 614592, 615978) includes:
- **IL12B (p40 loss-of-function):** Autosomal recessive; AR-complete; absent IL-12p70 and IL-23; most common single-gene MSMD cause; BCG disease, NTM, *Salmonella*
- **IL12RB1 loss-of-function:** AR; affects both IL-12 and IL-23 signalling; similar phenotype; ~40% of all MSMD cases in the Casanova cohort
- Treatment: IFN-γ supplementation (exogenous replacement for absent IL-12-driven IFN-γ); lifelong antimycobacterial prophylaxis in severe cases

### Ustekinumab and TB Reactivation

Ustekinumab blocks the p40 shared subunit → inhibits both IL-12 and IL-23. Clinical consequence:
- Reduces Th1 IFN-γ → impairs MTB containment in latent TB
- Phase III trials (UNIFI, CERTIFI): TB reactivation rate ~0.1–0.3 per 100 patient-years (comparable to anti-TNF mAbs)
- **Pre-therapy screening:** IGRA (preferred) or TST; if positive → isoniazid prophylaxis × 9 months before or concurrent with ustekinumab start
- Guselkumab, risankizumab (anti-p19, IL-23 selective) have lower TB risk since IL-12 is preserved

## Connections

- `connects-to` → **[Tuberculosis](../../07-system/tuberculosis/README.md)** — IL-12/IFN-γ axis is essential for granuloma formation and MTB containment; IL12B or IL12RB1 loss → MSMD with recurrent BCG/NTM disease; ustekinumab (anti-p40) and IL-12 pathway inhibitors → latent TB reactivation risk; IGRA screening mandatory before anti-IL-12 therapy.
- `modulates` → **[IFN-γ](../ifn-gamma/README.md)** — IL-12 is the primary upstream inducer of IFN-γ from NK cells and T cells via JAK2/TYK2/STAT4/T-bet; IFN-γ feeds back to activate macrophages which produce more IL-12 (positive amplification loop); the IL-12/IFN-γ axis is required for immunity against intracellular pathogens (MTB, Leishmania, Listeria).
- `connects-to` → **[Anemia of Chronic Disease](../../07-system/anemia-of-chronic-disease/README.md)** — IL-12 drives Th1 activation → IFN-γ + TNF-α → macrophage activation → IL-6 → hepcidin; chronic infections sustaining IL-12/IFN-γ (TB, HIV, leishmaniasis) are classic ACD causes; IL-12-mediated nutritional immunity restricts iron from intracellular pathogens via hepcidin-mediated sequestration.
- `modulates` → **[Immune System](../../07-system/immune-system/README.md)** — IL-12 is the master regulator of Th1 adaptive immunity, driving T-bet/IFN-γ polarization, NK cytotoxicity, and CTL development; required for effective immunity against intracellular bacteria (MTB, Listeria), dimorphic fungi, and certain viruses; its action is counterbalanced by IL-10 and IL-27.
- `connects-to` → **[HIV/AIDS](../../07-system/hiv-aids/README.md)** — HIV-AIDS profoundly impairs the IL-12/IFN-γ axis: depletion of CD4⁺ Th1 cells reduces IFN-γ production; HIV-infected DCs produce less IL-12; the resulting Th1 deficiency underlies susceptibility to TB, NTM, Leishmania, and dimorphic fungi in AIDS patients; ART partially restores IL-12 pathway responsiveness.
- `connects-to` → **[Leishmaniasis](../../07-system/leishmaniasis/README.md)** — Leishmania resistance is determined by IL-12-driven Th1 polarization: IL-12 → STAT4 → IFN-γ → iNOS → NO kills intracellular amastigotes; IL-12 polymorphisms (IL12B) influence VL susceptibility; L. donovani subverts TLR2 to suppress IL-12 production and evade Th1 immunity.

## Pathology

| Condition | Mechanism | Clinical Features |
|:---|:---|:---|
| **MSMD (IL12B/IL12RB1 deficiency)** | AR loss-of-function → absent IL-12p70 (and IL-23) → no Th1/IFN-γ response | Recurrent BCG disease after vaccination, NTM infections, Salmonella bacteraemia; otherwise healthy children; IGRA falsely negative; treat with IFN-γ + antimycobacterials |
| **MSMD (IL12RB2 deficiency)** | Rare; AR; impaired IL-12 but not IL-23 signalling | Milder than IL12RB1 deficiency; mycobacterial disease less severe |
| **Ustekinumab-related TB reactivation** | Anti-p40 → ↓IL-12 + ↓IL-23 → impaired IFN-γ + Th17 → granuloma destabilisation | Latent TB reactivation; screen with IGRA before therapy; prophylaxis if IGRA positive |
| **Leishmaniasis susceptibility** | IL-12 → IFN-γ → nitric oxide kills Leishmania; IL-12 deficiency → visceral leishmaniasis (kala-azar) in endemic regions | Co-occurs with IL12RB1 mutations in MSMD; anti-IL-12 therapy carries Leishmania risk in endemic areas |
| **Recombinant IL-12 toxicity** | Phase I cancer trials (1990s): rHuIL-12 → IFN-γ storm → fatal systemic toxicity (12 deaths) | Ended systemic rHuIL-12 as therapeutic; intratumoral IL-12 delivery (mRNA, gene therapy) under investigation |

## See Also

- [^trinchieri-2003-il12-review] Trinchieri G. Interleukin-12 and the regulation of innate resistance and adaptive immunity. *Nat Rev Immunol.* 2003;3(2):133-146. [doi:10.1038/nri1001](https://doi.org/10.1038/nri1001) · [PubMed 12563297](https://pubmed.ncbi.nlm.nih.gov/12563297/)
- [^altare-1998-il12r-msmd] Altare F et al. Inherited interleukin 12 deficiency in a child with BCG and Salmonella disseminated infection. *J Clin Invest.* 1998;102(12):2035-2040. [doi:10.1172/JCI4950](https://doi.org/10.1172/JCI4950) · [PubMed 9854042](https://pubmed.ncbi.nlm.nih.gov/9854042/)
- Related entries: [tuberculosis](../../07-system/tuberculosis/README.md), [ifn-gamma](../ifn-gamma/README.md), [tnf-alpha](../tnf-alpha/README.md), [il-23](../il-23/README.md), [il-10](../il-10/README.md)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
