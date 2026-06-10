---
schema: human-scale-entry/v1
id: ctla-4
name: CTLA-4
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-06
summary: "CD152; inhibitory receptor on T cells competing with CD28 for B7-1/B7-2 co-stimulation — suppresses T cell priming in lymph nodes. Blocked by ipilimumab (anti-CTLA-4 IgG1); combined with anti-PD-1 (nivolumab) as standard of care in advanced melanoma and RCC."
aliases: ["CD152", "cytotoxic T-lymphocyte-associated protein 4", "CTLA4", "CD152 checkpoint"]
sources:
  - id: leach-1996-ctla4
    type: peer-reviewed
    cite: "Leach DR, Krummel MF, Allison JP. Enhancement of antitumor immunity by CTLA-4 blockade. Science. 1996;271(5256):1734-1736."
    doi: "10.1126/science.271.5256.1734"
    pmid: "8596936"
    url: "https://doi.org/10.1126/science.271.5256.1734"
  - id: hodi-2010-ipilimumab
    type: peer-reviewed
    cite: "Hodi FS, O'Day SJ, McDermott DF, et al. Improved survival with ipilimumab in patients with metastatic melanoma. N Engl J Med. 2010;363(8):711-723."
    doi: "10.1056/NEJMoa1003466"
    pmid: "20525992"
    url: "https://doi.org/10.1056/NEJMoa1003466"
  - id: larkin-2015-checkmate067
    type: peer-reviewed
    cite: "Larkin J, Chiarion-Sileni V, Gonzalez R, et al. Combined Nivolumab and Ipilimumab or Monotherapy in Untreated Melanoma. N Engl J Med. 2015;373(1):23-34."
    doi: "10.1056/NEJMoa1504030"
    pmid: "26027431"
    url: "https://doi.org/10.1056/NEJMoa1504030"
cross_links:
  - target: 01-human/04-cellular/t-helper-cell
    relation: modulated-by
    note: "CTLA-4 is upregulated on activated CD4+ Th cells and constitutively expressed on Tregs; Treg CTLA-4 trans-endocytoses B7 from APCs → depletes co-stimulatory ligands → reduces Th and CTL priming in draining lymph nodes; ipilimumab restores CD28-mediated co-stimulation."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: modulated-by
    note: "Activated CTLs upregulate CTLA-4 which competes with CD28 for B7-1/B7-2 → dampens CTL priming in lymph nodes; CTLA-4 blockade (ipilimumab) acts primarily at the priming stage, complementing PD-1 blockade (effector stage) — mechanistic basis for anti-CTLA-4 + anti-PD-1 synergy."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: modulated-by
    note: "Tregs constitutively express high CTLA-4 → trans-endocytose B7 from DCs → peripheral tolerance; ipilimumab depletes intratumoral Tregs via ADCC → relieves TME immunosuppression; Treg depletion is the key mechanistic distinction between CTLA-4 and PD-1 blockade."
  - target: 01-human/03-molecular/pd-1
    relation: connects-to
    note: "CTLA-4 acts at the priming stage (lymph nodes); PD-1 at the effector stage (tumor microenvironment) — mechanistic basis for synergy; ipilimumab + nivolumab: 5-year OS ~52% in melanoma; approved for melanoma, RCC, NSCLC, and MSI-H colorectal cancer."
  - target: 01-human/07-system/melanoma
    relation: connects-to
    note: "Ipilimumab transformed metastatic melanoma: MDX-010-20 showed first OS benefit (10.1 vs 6.4 months vs gp100); CheckMate 067: nivo+ipi achieves 5-year OS of 52%; ipilimumab is also standard adjuvant therapy for resected stage III melanoma (EORTC 18071: RFS 40.8 vs 30.3%)."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "Treg CTLA-4 trans-endocytoses B7-1/B7-2 from DCs → depletes co-stimulatory ligands from DCs → DCs cannot prime new anti-tumor T cells in tumor-draining lymph nodes; ipilimumab prevents trans-endocytosis → restores DC B7 → enables new CTL priming against tumor neoantigens."
  - target: 03-medicine/01-modern/13-cancer/checkpoint-inhibitors
    relation: target-of
    note: "Ipilimumab (anti-CTLA-4 IgG1) is the founding checkpoint inhibitor; CTLA-4 blockade at the priming stage synergizes with PD-1 blockade at the effector stage; ipilimumab + nivolumab is standard of care for melanoma, RCC, NSCLC, and MSI-H colorectal cancer."
---

# CTLA-4

## Overview

**CTLA-4 (cytotoxic T-lymphocyte-associated protein 4, CD152)** is an **inhibitory immune checkpoint receptor** expressed on activated T cells and constitutively on regulatory T cells (Tregs). As the founding member of the CD28 family of co-stimulatory receptors, CTLA-4 binds the same ligands as its activating counterpart CD28 — **B7-1 (CD80) and B7-2 (CD86)** on antigen-presenting cells — but with approximately 20-fold higher affinity, thereby **outcompeting CD28** for co-stimulation and delivering a potent **inhibitory signal** that terminates T cell priming.

CTLA-4's physiological role is to maintain peripheral tolerance and prevent autoimmunity by limiting the amplitude and duration of T cell activation in lymph nodes and the thymus:
- **CTLA-4 knockout mice** (Waterhouse 1995, Tivol 1995): develop fatal lymphoproliferative disorder with multi-organ autoimmunity → demonstrates CTLA-4 is essential for immune self-tolerance
- **Treg constitutive CTLA-4:** Required for Treg suppressor function; Treg-specific CTLA-4 deletion → autoimmunity phenotype resembling CTLA-4 KO

The discovery that CTLA-4 blockade enhances anti-tumor immunity (Allison and Leach 1996, Science) [^leach-1996-ctla4] — and that blocking this checkpoint restores T cell attack on tumors — established the proof-of-concept for immune checkpoint therapy and earned James Allison the 2018 Nobel Prize in Physiology or Medicine (shared with Tasuku Honjo, who discovered PD-1).

**Ipilimumab (Yervoy, Bristol Myers Squibb):** Anti-CTLA-4 IgG1 antibody; FDA approved 2011 for metastatic melanoma — the first immune checkpoint inhibitor approved and the first to demonstrate improved OS in metastatic melanoma [^hodi-2010-ipilimumab]. The OS curves show a distinctive "plateau" at ~20% at 3+ years (long-term survivors), unlike cytotoxic chemotherapy.

## Structure

### CTLA-4 protein

CTLA-4 is a **223 amino acid type I transmembrane glycoprotein** of the immunoglobulin superfamily, structurally homologous to CD28:
- **Signal peptide (aa 1-35):** ER targeting
- **Extracellular IgV-like domain (aa 36-161):** Contains the MYPPPY motif (conserved with CD28) — the critical B7 contact interface; CTLA-4 binds B7-1 with Kd ~0.4 μM and B7-2 with Kd ~1.1 μM (vs. CD28: ~4 μM and ~20 μM respectively)
- **Transmembrane domain (aa 162-182):** Single pass; CTLA-4 is primarily held in intracellular vesicles (endosomal/lysosomal) and rapidly cycled to the surface upon TCR activation via Lck-dependent exocytosis
- **Cytoplasmic tail (aa 183-223):** 36 aa; contains GVYVKM and YFIP motifs; critical for trafficking (AP-2 and AP-1 clathrin adaptor binding → rapid endocytosis after surface expression); also recruits PP2A (protein phosphatase 2A) → dephosphorylates CD28 and PI3K → inhibitory signaling

**Homodimerization:** Unlike CD28 (monomer), CTLA-4 forms a **disulfide-linked homodimer** via Cys120 → CTLA-4 dimer binds bivalently to B7-1 or B7-2 dimers → "zippering" of B7 on the APC surface → trans-endocytosis of B7 into T cell → reduces available B7 for CD28 co-stimulation on neighboring cells

## Function

### CTLA-4 mechanisms of immune inhibition

**1. CD28 competition — quantitative model:**
CTLA-4 and CD28 both bind B7-1 and B7-2, but CTLA-4's higher affinity (20×) and homodimeric bivalent binding (avidity enhancement) allow it to effectively outcompete CD28 when CTLA-4 is expressed at sufficient levels (≥ hours after T cell activation). CD28 requires co-stimulation for IL-2 production and T cell cycle progression (G1→S); CTLA-4 competition → reduced CD28 signaling → less PI3K-Akt → less CD28-mediated survival → T cell inactivation or anergy.

**2. Active inhibitory signaling:**
CTLA-4 cytoplasmic tail recruits:
- **PP2A (protein phosphatase 2A):** Dephosphorylates CD28 (Tyr191) and Akt → attenuates T cell survival signals
- **SHP-2 (partially):** Dephosphorylates TCR signaling intermediates; less important than for PD-1

**3. Trans-endocytosis of B7:**
CTLA-4 homodimer binds B7-1/2 on APCs → CTLA-4 internalized rapidly by clathrin → B7 dragged into T cell (trans-endocytosis) → B7 degraded in lysosomes → reduced APC B7 → neighboring T cells cannot receive CD28 co-stimulation → reduced priming of new T cells (dominant mechanism for Treg suppression of immune responses)

**4. Treg suppressor mechanism:**
Tregs constitutively express CTLA-4 at high levels (driven by FoxP3 → CTLA-4 transcription); Treg CTLA-4 → trans-endocytoses B7 from DCs → quantitative depletion of B7 → DCs cannot activate effector T cells → peripheral tolerance. This mechanism operates in tumor-draining lymph nodes (Tregs from tumor → drain to LN → deplete B7 → prevent new anti-tumor T cell priming) → tumor immune escape.

### CTLA-4 vs. PD-1: complementary mechanisms [^larkin-2015-checkmate067]

| Feature | CTLA-4 | PD-1 |
|:---|:---|:---|
| Primary expression | All activated T cells; Tregs (constitutive) | Activated T cells (effector/memory); also B cells, NK cells |
| Ligands | B7-1/B7-2 (on APCs) | PD-L1/PD-L2 (on tumor cells, APCs, tissues) |
| Site of action | Lymph nodes, thymus (priming) | Peripheral tissues, tumor microenvironment (effector) |
| Mechanism | CD28 competition, trans-endocytosis of B7 | SHP-2 dephosphorylation of CD28 and TCR intermediates |
| irAE profile | Colitis, hypophysitis, hepatitis (high grade ~20%) | Colitis, pneumonitis, endocrinopathies (high grade ~5-15%) |
| Combination logic | Priming + effector = synergistic dual blockade | — |

## Mechanism

### Ipilimumab anti-tumor mechanism and clinical data [^hodi-2010-ipilimumab]

**Ipilimumab (anti-CTLA-4 IgG1):**
- **Tumor microenvironment:** IgG1 Fc → ADCC-mediated depletion of intratumoral Tregs (FcγRIII on NK cells, macrophages) → removes major immune suppressor in TME → releases effector CTLs; this Treg depletion is a distinguishing feature of ipilimumab vs. PD-1 blockade
- **Lymph node:** Blocks CTLA-4 trans-endocytosis → restores B7 availability → de-novo T cell priming against tumor neoantigens

**Clinical trials:**
- **MDX-010-20 (ipilimumab vs gp100 peptide vaccine, metastatic melanoma, 2010):** Ipilimumab improved OS vs gp100 alone (10.1 vs 6.4 months) — first OS improvement in metastatic melanoma; ~20% 3-year survivors
- **CheckMate 067 (nivolumab + ipilimumab vs monotherapy, untreated melanoma, 2015):** Combination vs monotherapy: ORR 57.6% vs 43.7% (nivo alone) vs 19.0% (ipi alone); **5-year OS 52% (combination) vs 44% (nivo) vs 26% (ipi)** — combination is standard of care for advanced melanoma [^larkin-2015-checkmate067]
- **CheckMate 214 (nivolumab + ipilimumab vs sunitinib, intermediate/poor risk RCC):** PFS 11.6 vs 8.4 months, OS 47.0 vs 26.6 months (ipi+nivo) — combination standard of care for intermediate/poor risk RCC
- **CheckMate 227 (nivolumab + ipilimumab in TMB-H or PD-L1+ NSCLC):** Improved OS in TMB-high patients (21.2 vs 14.9 months, chemotherapy)

**irAEs with ipilimumab:** Higher grade 3-4 irAEs (~20-30%) than PD-1 blockade alone:
- **Immune-related colitis:** Most common (30%); dose-related; treat with high-dose corticosteroids (prednisone 1-2 mg/kg); if refractory: infliximab (anti-TNF)
- **Immune-related hypophysitis (pituitary inflammation):** 5-10%; causes hypopituitarism (secondary hypothyroidism, hypogonadism, adrenal insufficiency) — requires lifelong hormone replacement; MRI: enlarged pituitary
- **Immune-related hepatitis:** 5-10%; transaminase elevation; treat with steroids ± mycophenolate mofetil
- **Combination with nivolumab:** Grade 3-4 irAEs in ~55% → require vigilant monitoring and prompt immunosuppression

## Connections

- `modulated-by` → **[T Helper Cell](../../04-cellular/t-helper-cell/README.md)** — CD4+ T helper cells upregulate CTLA-4 after activation; CTLA-4 competes with CD28 for B7 co-stimulation → dampens Th-driven immune responses; Tregs constitutively express CTLA-4 to suppress neighboring T cells.
- `modulated-by` → **[T Cytotoxic Cell](../../04-cellular/t-cytotoxic-cell/README.md)** — activated CTLs express CTLA-4 which suppresses their priming in lymph nodes; ipilimumab blocks CTLA-4 on CTLs → restores co-stimulation → enhanced CTL priming against tumor antigens.
- `modulated-by` → **[Regulatory T Cell](../../04-cellular/regulatory-t-cell/README.md)** — Tregs constitutively express high CTLA-4 which trans-endocytoses B7 from DCs → peripheral tolerance; ipilimumab also depletes intratumoral Tregs via ADCC (IgG1 Fc) → relieves TME immunosuppression.
- `connects-to` → **[PD-1](../pd-1/README.md)** — CTLA-4 (priming stage) and PD-1 (effector stage) are complementary checkpoints; combined ipilimumab + nivolumab achieves synergistic tumor control; 5-year OS ~52% in melanoma; approved for melanoma, RCC, NSCLC, and MSI-H colorectal cancer.
- `connects-to` → **[Melanoma](../../07-system/melanoma/README.md)** — ipilimumab transformed metastatic melanoma; MDX-010-20 showed first OS benefit; CheckMate 067: nivo+ipi 5-year OS 52%; ipilimumab also approved as adjuvant therapy for resected stage III melanoma (EORTC 18071: 5-year RFS 40.8 vs 30.3%).
- `connects-to` → **[Dendritic Cell](../../04-cellular/dendritic-cell/README.md)** — Treg CTLA-4 trans-endocytoses B7-1/B7-2 from DCs → depletes co-stimulatory ligands → DCs cannot prime new anti-tumor T cells; ipilimumab prevents trans-endocytosis → restores DC B7 availability → enables new CTL priming against tumor neoantigens.
- `target-of` → **[Checkpoint Inhibitors](../../../03-medicine/01-modern/13-cancer/checkpoint-inhibitors/README.md)** — ipilimumab (anti-CTLA-4 IgG1) is the founding checkpoint inhibitor; CTLA-4 blockade synergizes with PD-1 blockade; ipilimumab + nivolumab is standard of care for melanoma, RCC, NSCLC, and MSI-H colorectal cancer.

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^leach-1996-ctla4]: Leach DR, Krummel MF, Allison JP. Enhancement of antitumor immunity by CTLA-4 blockade. *Science.* 1996;271(5256):1734-1736. [doi:10.1126/science.271.5256.1734](https://doi.org/10.1126/science.271.5256.1734) · [PubMed 8596936](https://pubmed.ncbi.nlm.nih.gov/8596936/)
[^hodi-2010-ipilimumab]: Hodi FS, O'Day SJ, McDermott DF, et al. Improved survival with ipilimumab in patients with metastatic melanoma. *N Engl J Med.* 2010;363(8):711-723. [doi:10.1056/NEJMoa1003466](https://doi.org/10.1056/NEJMoa1003466) · [PubMed 20525992](https://pubmed.ncbi.nlm.nih.gov/20525992/)
[^larkin-2015-checkmate067]: Larkin J, Chiarion-Sileni V, Gonzalez R, et al. Combined Nivolumab and Ipilimumab or Monotherapy in Untreated Melanoma. *N Engl J Med.* 2015;373(1):23-34. [doi:10.1056/NEJMoa1504030](https://doi.org/10.1056/NEJMoa1504030) · [PubMed 26027431](https://pubmed.ncbi.nlm.nih.gov/26027431/)
