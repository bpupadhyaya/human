---
schema: human-scale-entry/v1
id: btk
name: BTK
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-06
summary: "BTK (Bruton's tyrosine kinase) is the critical BCR signaling kinase activating PLCγ2-Ca²⁺ and NF-κB → B-cell survival; germline BTK loss causes X-linked agammaglobulinemia; ibrutinib (covalent BTK inhibitor) and zanubrutinib are approved for CLL, MCL, WM, and MZL."
aliases: ["BTK", "Bruton's tyrosine kinase", "BTK inhibitor", "ibrutinib", "zanubrutinib", "acalabrutinib", "pirtobrutinib", "X-linked agammaglobulinemia", "XLA", "BCR signaling kinase"]
sources:
  - id: byrd-2013-ibrutinib-cll
    type: peer-reviewed
    cite: "Byrd JC, Furman RR, Coutre SE, et al. Targeting BTK with ibrutinib in relapsed chronic lymphocytic leukemia. N Engl J Med. 2013;369(1):32-42."
    doi: "10.1056/NEJMoa1215637"
    pmid: "23782158"
    url: "https://doi.org/10.1056/NEJMoa1215637"
  - id: wang-2013-ibrutinib-mcl
    type: peer-reviewed
    cite: "Wang ML, Rule S, Martin P, et al. Targeting BTK with ibrutinib in relapsed or refractory mantle-cell lymphoma. N Engl J Med. 2013;369(6):507-516."
    doi: "10.1056/NEJMoa1306220"
    pmid: "23782157"
    url: "https://doi.org/10.1056/NEJMoa1306220"
cross_links:
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "BCR engagement → LYN/SYK → BLNK/BTK → PLCγ2 → PKCβ → IKK → NF-κB → B-cell survival; BTK is the central kinase linking BCR activation to NF-κB in CLL, MCL, and WM; ibrutinib blocks BTK-NF-κB → apoptosis in BCR-dependent malignancies."
  - target: 01-human/03-molecular/bcl-2
    relation: connects-to
    note: "BTK inhibition → reduced PI3K-AKT → decreased BCL-2 expression; ibrutinib+venetoclax (BCL-2 inhibitor) is highly active in CLL (CAPTIVATE: undetectable MRD ~50%) and R/R MCL; BTK+BCL-2 co-inhibition achieves deeper responses than either alone."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "BCR → SYK → PI3K-δ (PIK3CD) and BTK → AKT → mTOR → B-cell survival; PI3K-δ inhibitors (idelalisib, duvelisib) are approved for CLL as BTK inhibitor alternatives; PI3K-δ/BTK dual inhibitors under development; PTEN loss activates PI3K bypassing BTK inhibition."
  - target: 01-human/03-molecular/cyclin-d1
    relation: connects-to
    note: "t(11;14) CCND1-IGH → cyclin D1 overexpression → CDK4/6-RB phosphorylation → S-phase entry is the hallmark of MCL; BTK/NF-κB → cyclin D1 transcription cooperates with t(11;14); CDK4/6 inhibitors (palbociclib) + BTK inhibitors studied in MCL as CDK4/6-BTK synthetic targeting."
  - target: 01-human/04-cellular/b-cell
    relation: connects-to
    note: "BTK is the central BCR signaling kinase in B-cell development and survival; BTK PH domain recruits BTK to PIP3 at the membrane → LYN/SYK phosphorylate Tyr551 → BTK activates PLCγ2-NF-κB; BTK loss (XLA) → failure of B-cell maturation at pro-B stage; BTK gain → autoimmunity."
  - target: 01-human/07-system/cll
    relation: connects-to
    note: "Ibrutinib and zanubrutinib are first-line standards for CLL/SLL; BTK inhibition blocks BCR-NF-κB → CLL cell egress from nodes (transient lymphocytosis) then sustained reduction; pirtobrutinib (non-covalent) active after covalent BTK inhibitor resistance (BTK C481S)."
  - target: 01-human/07-system/mantle-cell-lymphoma
    relation: connects-to
    note: "Ibrutinib (ORR ~68%) and zanubrutinib are approved for R/R MCL; BTK/NF-κB amplifies cyclin D1 from t(11;14); BTK C481S acquired resistance in ~30% of MCL after covalent BTK inhibitors; pirtobrutinib overcomes C481S; BTK+venetoclax combinations achieve deep MRD negativity."
---

# BTK

## Overview

**BTK (Bruton's Tyrosine Kinase)** is a member of the Tec family of non-receptor protein tyrosine kinases and the central effector of **B-cell receptor (BCR) signaling** — the pathway that controls B-cell development, activation, proliferation, and survival. Upon BCR cross-linking by antigen, LYN and SYK phosphorylate the ITAMs of CD79a/b → SYK phosphorylates adaptor BLNK → BTK is recruited via its PH domain (binds PIP3) and phosphorylated at Tyr551 (by LYN/SYK) and auto-phosphorylated at Tyr223 → active BTK phosphorylates **PLCγ2** → IP3 → Ca²⁺ release → calcineurin → NFAT; DAG → PKCβ → IKK → **NF-κB**; and BTK also activates PI3K-AKT-mTOR and RAS-ERK pathways. Germline **BTK loss-of-function** mutations cause **X-linked agammaglobulinemia (XLA, Bruton's disease)** — the prototypic primary immunodeficiency characterized by absence of mature B-cells and immunoglobulins, with recurrent bacterial infections in male infants. The landmark discovery that lymphoma cells have constitutive BCR-BTK signaling led to ibrutinib — the first approved covalent BTK inhibitor (2013) — revolutionizing treatment of CLL, MCL, and WM [^byrd-2013-ibrutinib-cll] [^wang-2013-ibrutinib-mcl].

**BTK inhibitors — approved indications:**
- **CLL/SLL:** Ibrutinib, zanubrutinib, acalabrutinib (first-line and R/R); pirtobrutinib (R/R CLL/SLL after ≥2 prior lines including BTK inhibitor)
- **MCL:** Ibrutinib (R/R), zanubrutinib (R/R), acalabrutinib (R/R); pirtobrutinib (R/R after ≥2 prior lines)
- **WM:** Ibrutinib, zanubrutinib (first-line and R/R)
- **MZL:** Zanubrutinib, ibrutinib (R/R after anti-CD20)
- **Primary CNS lymphoma (PCNSL):** Ibrutinib, tirabrutinib (Japan); high CNS penetration required

**BTK inhibitors — mechanism classes:**
- **Covalent-irreversible (C481 targeting):** Ibrutinib, acalabrutinib, zanubrutinib — bind BTK Cys481 in ATP-binding site → irreversible inhibition; resistance via BTK C481S mutation (Ser substitution prevents covalent bond)
- **Non-covalent-reversible:** Pirtobrutinib (LOXO-305) — binds ATP pocket without covalent bond → active against BTK C481S; approved 2023 for R/R CLL/SLL and MCL post-covalent BTK inhibitor

## Structure

### BTK protein architecture

BTK is a 659-amino-acid, 76 kDa Tec-family kinase with five functional domains:

**PH domain (1-117, Pleckstrin Homology):**
- Binds PIP3 (phosphatidylinositol-3,4,5-trisphosphate) → membrane recruitment following PI3K activation downstream of BCR
- PH domain mutation R28C/H (XLA mutation) → BTK cannot translocate to membrane → no signaling
- Resting BTK is cytoplasmic; activation requires PI3K-generated PIP3 → PH-PIP3 interaction → membrane-proximal LYN/SYK phosphorylation of Tyr551

**TH domain (118-215, Tec Homology):**
- Proline-rich region (PXXP) → SH3-domain binding sites; pseudo-kinase zinc finger; regulates BTK function

**SH3 domain (216-266):**
- Binds proline-rich sequences; protein-protein interaction; engages BLNK, PLCγ2; contributes to autoregulation of BTK activity

**SH2 domain (267-361):**
- Phosphotyrosine-binding; engages phospho-Y from upstream kinases; required for Tyr551 recognition by LYN/SYK

**Kinase domain (362-659):**
- Activation loop: Tyr551 phosphorylation (by LYN/SYK) → kinase activation; Tyr223 (in N-lobe, outside activation loop) → auto-phosphorylation → full activation
- **Cys481:** Targeted by ibrutinib, zanubrutinib, acalabrutinib; located in ATP-binding site hinge region; forms covalent bond with Michael acceptor warhead → irreversible BTK inhibition
- **BTK C481S resistance:** Ser substitution eliminates covalent binding site → ibrutinib/zanubrutinib/acalabrutinib inactive; pirtobrutinib (non-covalent) retains activity

### BCR signaling cascade

**Canonical BCR activation:**
1. Antigen → crosslinks surface IgM/IgD (BCR) → ITAM phosphorylation of CD79a/b by LYN
2. SYK recruited via SH2-phospho-ITAM → SYK kinase activation
3. SYK phosphorylates BLNK (B-cell linker protein, adaptor) → scaffold for BTK and PLCγ2
4. BTK recruited via PH domain (PIP3 from PI3K-δ) → phosphorylated by LYN/SYK at Tyr551
5. BTK phosphorylates PLCγ2 → PLCγ2 cleaves PIP2 → IP3 + DAG
   - IP3 → ER Ca²⁺ release → NFAT dephosphorylation → nuclear translocation → gene expression
   - DAG → PKCβ → TAK1 → IKKβ → IκBα degradation → NF-κB
6. BTK → RAS-MAPK and PI3K-AKT additional signaling → proliferation and survival

**Tonic BCR signaling:**
In addition to antigen-stimulated BCR signaling, mature B-cells require low-level tonic (antigen-independent) BCR signaling for survival — dependent on SYK, BTK, and PI3K-δ. CLL and MCL cells depend on amplified tonic BCR-BTK signaling rather than classical antigen-induced activation.

## Function

### BTK in normal B-cell development

**B-cell developmental checkpoint:**
BTK is essential at the pro-B to pre-B transition (requires pre-BCR signaling) and for mature naïve B-cell survival (requires tonic BCR-BTK). In XLA, absent BTK → failure of B-cell maturation at pro-B stage → no circulating B-cells or immunoglobulins → susceptibility to encapsulated bacteria (Streptococcus, Haemophilus) and enteroviruses.

**BCR specificity threshold:**
BTK activity sets the threshold for BCR signaling in B-cell selection. BTK gain-of-function → lower threshold → autoreactive B-cells escape negative selection → autoimmunity (animal models); BTK inhibitors → immune tolerance restoration → being studied in autoimmune diseases (rheumatoid arthritis, SLE, multiple sclerosis, pemphigus vulgaris).

### BTK in malignant B-cells

**CLL BTK dependency:**
CLL cells express high surface BCR and have constitutive LYN/BTK activity driven by BCR clustering; ibrutinib blocks BTK → rapid reduction in BCR signaling → lymphocyte redistribution (CLL cells egress from BM and nodes into blood — transient lymphocytosis in first 1-3 months, not progression) → durable lymphocyte reduction → remission; ibrutinib does not require direct cytotoxicity (no CR typically) — acts via disrupting CLL-microenvironment interaction.

**MCL BTK dependency:**
MCL cells have t(11;14) CCND1-IGH + constitutive BCR-BTK signaling → NF-κB → cyclin D1 amplification and BCL-2; ibrutinib blocks BCR-BTK-NF-κB → apoptosis in MCL; high ORR (~68%) in R/R MCL with ibrutinib; BTK C481S acquired resistance occurs in ~30% of MCL patients who relapse on covalent BTK inhibitors.

## Mechanism

### BTK inhibitor resistance

**Primary resistance:**
- Non-BCR-dependent survival: CARD11 mutations (NF-κB pathway activated independently of BCR); alternative NF-κB activation (BCL10/MALT1 axis)
- BRAF V600E: In 5-10% of CLL; provides RAS-ERK survival signal independent of BTK
- PLC-γ2 gain-of-function: PLCγ2 R665W/S707Y/L845F → activating mutations downstream of BTK → bypasses BTK inhibition

**Acquired resistance (C481S mutation):**
- BTK C481S (Cys481Ser) in >80% of ibrutinib-resistant cases → Ser cannot form covalent bond → ibrutinib/zanubrutinib/acalabrutinib ineffective; pirtobrutinib (LOXO-305) overcomes C481S with non-covalent binding; BRUIN trial (pirtobrutinib in R/R CLL after BTK inhibitor): ORR ~73%

**Covalent vs. non-covalent BTK inhibitor comparison:**
| Feature | Ibrutinib | Zanubrutinib | Acalabrutinib | Pirtobrutinib |
|---------|----------|--------------|---------------|---------------|
| Mechanism | Covalent C481 | Covalent C481 | Covalent C481 | Non-covalent |
| BTK selectivity | Moderate (ITK, EGFR off-targets) | High | High | High |
| C481S activity | No | No | No | Yes |
| AFib rate | ~10-15% | ~2% | ~4% | ~2% |
| CLL approval | Yes | Yes | Yes | Yes (post-BTKi) |
| Approved 1st-line | Yes | Yes | Yes | No |

### BTK inhibitor toxicities and management

**Ibrutinib-specific off-target toxicities (EGFR, ITK, CSK, BLK, TEC):**
- **Atrial fibrillation:** ~5-15% of patients (cumulative); likely ITK off-target in cardiac cells; baseline cardiac evaluation; rhythm monitoring; consider zanubrutinib or acalabrutinib for cardiac-risk patients
- **Bleeding:** BTK in platelets (GPVI signaling) → platelet dysfunction; avoid antiplatelet/anticoagulants when possible; surgical hold ≥3-7 days
- **Hypertension:** ~20-25%; manage pharmacologically; ACE inhibitors or calcium channel blockers
- **Arthralgias/myalgias:** ~15%; class effect; can dose-reduce or switch to zanubrutinib/acalabrutinib
- **Rash, diarrhea, nail changes:** Class effect

## Connections

- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — BCR engagement → LYN/SYK → BLNK/BTK → PLCγ2 → PKCβ → IKK → NF-κB → B-cell survival; BTK is the central kinase linking BCR activation to NF-κB in CLL, MCL, and WM; ibrutinib blocks BTK-NF-κB → apoptosis in BCR-dependent malignancies.
- `connects-to` → **[BCL-2](../../03-molecular/bcl-2/README.md)** — BTK inhibition → reduced PI3K-AKT → decreased BCL-2 expression; ibrutinib+venetoclax (BCL-2 inhibitor) is highly active in CLL (CAPTIVATE: undetectable MRD ~50%) and R/R MCL; BTK+BCL-2 co-inhibition achieves deeper responses than either alone.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — BCR → SYK → PI3K-δ (PIK3CD) and BTK → AKT → mTOR → B-cell survival; PI3K-δ inhibitors (idelalisib, duvelisib) are approved for CLL as BTK inhibitor alternatives; PI3K-δ/BTK dual inhibitors under development; PTEN loss activates PI3K bypassing BTK inhibition.
- `connects-to` → **[Cyclin D1](../../03-molecular/cyclin-d1/README.md)** — t(11;14) CCND1-IGH → cyclin D1 overexpression → CDK4/6-RB phosphorylation → S-phase entry is the hallmark of MCL; BTK/NF-κB → cyclin D1 transcription cooperates with t(11;14); CDK4/6 inhibitors (palbociclib) + BTK inhibitors studied in MCL as CDK4/6-BTK synthetic targeting.
- `connects-to` → **[B Cell](../../04-cellular/b-cell/README.md)** — BTK is the central BCR signaling kinase in B-cell development and survival; BTK PH domain recruits BTK to PIP3 → LYN/SYK phosphorylate Tyr551 → BTK activates PLCγ2-NF-κB; BTK loss (XLA) → failure of B-cell maturation at pro-B stage; BTK gain → autoimmunity.
- `connects-to` → **[CLL](../../07-system/cll/README.md)** — Ibrutinib and zanubrutinib are first-line standards for CLL/SLL; BTK inhibition blocks BCR-NF-κB → CLL cell egress from nodes (transient lymphocytosis) then sustained reduction; pirtobrutinib (non-covalent) active after covalent BTK inhibitor resistance (BTK C481S).
- `connects-to` → **[Mantle Cell Lymphoma](../../07-system/mantle-cell-lymphoma/README.md)** — Ibrutinib (ORR ~68%) and zanubrutinib are approved for R/R MCL; BTK/NF-κB amplifies cyclin D1 from t(11;14); BTK C481S acquired resistance in ~30% of MCL after covalent BTK inhibitors; pirtobrutinib overcomes C481S; BTK+venetoclax achieve deep MRD negativity.

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^byrd-2013-ibrutinib-cll]: Byrd JC, Furman RR, Coutre SE, et al. Targeting BTK with ibrutinib in relapsed chronic lymphocytic leukemia. *N Engl J Med.* 2013;369(1):32-42. [doi:10.1056/NEJMoa1215637](https://doi.org/10.1056/NEJMoa1215637) · [PubMed 23782158](https://pubmed.ncbi.nlm.nih.gov/23782158/)
[^wang-2013-ibrutinib-mcl]: Wang ML, Rule S, Martin P, et al. Targeting BTK with ibrutinib in relapsed or refractory mantle-cell lymphoma. *N Engl J Med.* 2013;369(6):507-516. [doi:10.1056/NEJMoa1306220](https://doi.org/10.1056/NEJMoa1306220) · [PubMed 23782157](https://pubmed.ncbi.nlm.nih.gov/23782157/)
