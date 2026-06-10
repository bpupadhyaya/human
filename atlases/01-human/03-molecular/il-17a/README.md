---
schema: human-scale-entry/v1
id: il-17a
name: IL-17A
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-07
summary: "IL-17A is produced by Th17 cells and ILC3; signals via IL-17RA/RC → NF-kB → neutrophil recruitment, AMP expression, and keratinocyte proliferation; drives psoriasis, ankylosing spondylitis, and psoriatic arthritis; secukinumab and ixekizumab are approved first-line biologics."
aliases: ["IL-17A", "interleukin-17A", "IL17A", "CTLA-8", "IL-17", "Th17 cytokine", "anti-IL-17A", "secukinumab target", "ixekizumab target", "IL-17A biologics"]
sources:
  - id: langrish-2005-il17-autoimmunity
    type: peer-reviewed
    cite: "Langrish CL, Chen Y, Blumenschein WM, et al. IL-23 drives a pathogenic T cell population that induces autoimmune inflammation. J Exp Med. 2005;201(2):233-240."
    doi: "10.1084/jem.20041257"
    pmid: "15657292"
    url: "https://doi.org/10.1084/jem.20041257"
  - id: langley-2014-secukinumab
    type: peer-reviewed
    cite: "Langley RG, Elewski BE, Lebwohl M, et al. Secukinumab in plaque psoriasis — results of two phase 3 trials. N Engl J Med. 2014;371(4):326-338."
    doi: "10.1056/NEJMoa1406095"
    pmid: "25007392"
    url: "https://doi.org/10.1056/NEJMoa1406095"
cross_links:
  - target: 01-human/07-system/psoriasis
    relation: connects-to
    note: "IL-17A from skin Th17 and γδ T cells activates keratinocyte IL-17RA/RC → NF-kB → CXCL8, S100A proteins, and AMPs → neutrophil influx and epidermal hyperproliferation; secukinumab (anti-IL-17A) and ixekizumab achieve PASI 90 in ~60% of plaque psoriasis patients at 16 weeks."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "IL-23 maintains the Th17 effector program and drives IL-17A via STAT3 → RORγt; anti-IL-23p19 antibodies (risankizumab) suppress IL-17A and achieve superior long-term psoriasis clearance vs anti-IL-17A antibodies; IL-23 sits upstream of IL-17A in the Th17 axis."
  - target: 01-human/07-system/rheumatoid-arthritis
    relation: connects-to
    note: "IL-17A is present in RA synovium but secondary to TNF-alpha and IL-6; IL-17A promotes osteoclastogenesis via RANKL induction; IL-17A inhibitors (secukinumab) failed pivotal RA trials; bimekizumab (anti-IL-17A/F) showed marginal RA benefit vs established TNF/IL-6 blockade."
  - target: 01-human/07-system/multiple-sclerosis
    relation: connects-to
    note: "IL-17A is elevated in MS lesions and CSF; Th17 cells breach the blood-brain barrier via CXCR6 → demyelination; secukinumab (anti-IL-17A) paradoxically worsened MS relapse rates in phase 2 trials — suggesting complex compensatory roles of IL-17A/Treg balance in CNS disease."
  - target: 01-human/07-system/ankylosing-spondylitis
    relation: connects-to
    note: "IL-17A drives enthesitis in AS: ILC3 and Th17 cells at entheses produce IL-17A → RANKL + MMP → bone erosion; WNT-driven new bone formation follows (syndesmophytes); secukinumab (MEASURE-1: ASAS20 61% vs. 29%) and ixekizumab (COAST-V) are FDA-approved for AS."
  - target: 01-human/07-system/psoriatic-arthritis
    relation: connects-to
    note: "IL-17A is a central driver of PsA enthesitis, synovitis, and new bone formation; secukinumab (FUTURE 2: ACR20 54% vs 15%; FDA 2016) and ixekizumab (SPIRIT-P1/2; FDA 2017) are approved; entheseal ILC3 produce IL-17A independently of IL-23 in some PsA patients."
  - target: 01-human/07-system/giant-cell-arteritis
    relation: connects-to
    note: "GCA involves Th17 (IL-17A) and Th1 (IFN-γ) CD4+ T cell infiltrate in the arterial adventitia; IL-17A amplifies macrophage/neutrophil recruitment and intimal hyperplasia; secukinumab (anti-IL-17A) and upadacitinib (JAK1 inhibitor; SELECT-GCA) are under investigation."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "IL-17A drives neutrophil recruitment via CXCL1/CXCL5/CXCL8 from keratinocytes and fibroblasts; neutrophilic infiltration is the hallmark of psoriatic plaques; IL-17A + TNF-α synergise to amplify AMP expression; IL-17A LOF mutations → mucocutaneous candidiasis."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "Th17 cells (CD4+ RORγt+ IL-17RA+) are the primary IL-17A producers; IL-6 + TGF-β initiate Th17 differentiation; IL-23 maintains the effector Th17 program; tissue-resident Th17 cells sustain chronic inflammation in psoriasis and AS after systemic T cell depletion."
  - target: 01-human/07-system/inflammatory-bowel-disease
    relation: connects-to
    note: "IL-17A is elevated in IBD mucosa but anti-IL-17A therapy (secukinumab) paradoxically worsens IBD in AS/PsA patients; gut epithelial IL-17A may protect barrier integrity; this dual role distinguishes mucosal IL-17A function from systemic Th17 pathogenicity."
---

# IL-17A

## Overview

**IL-17A** (interleukin-17A; also CTLA-8) is the founding member of the IL-17 cytokine family, encoded by *IL17A* on chromosome 6p12. It is a disulfide-linked homodimeric glycoprotein produced primarily by **Th17 cells**, **innate lymphoid cells group 3 (ILC3)**, γδ T cells, mast cells, and neutrophils. IL-17A is the principal effector cytokine of mucosal and cutaneous immunity — amplifying neutrophil-mediated defense against extracellular pathogens, particularly fungi (*Candida albicans*) and bacteria. Dysregulated IL-17A signaling drives **psoriasis, ankylosing spondylitis (AS), psoriatic arthritis (PsA)**, and contributes to other Th17-mediated conditions.

Anti-IL-17A biologics were the breakthrough in psoriasis therapy: secukinumab (fully human anti-IL-17A; Novartis) was approved for plaque psoriasis in 2015, achieving ~PASI 75 in 75–80% and PASI 90 in ~60% of patients at week 16 — markedly superior to prior anti-TNF therapy [^langley-2014-secukinumab]. Ixekizumab (Eli Lilly), bimekizumab (anti-IL-17A/F dual; UCB), and netakimab followed. Secukinumab and ixekizumab are also approved for AS and PsA.

**IL-17 family overview:**

| Cytokine | Predominant producer | Primary target | Key disease |
|---|---|---|---|
| IL-17A | Th17, ILC3, γδ T | Epithelial, fibroblasts | Psoriasis, AS, PsA |
| IL-17F | Th17, ILC3 | Epithelial | Psoriasis (weaker than IL-17A) |
| IL-17A/F | Th17 | Epithelial | Psoriasis (heterodimer) |
| IL-17C | Epithelial | Epithelial (autocrine) | Atopic dermatitis |
| IL-17D | NK cells | Epithelial | Unclear |
| IL-17E (IL-25) | Epithelial, ILC2 | ILC2, Th2 | Allergic inflammation |

## Structure

IL-17A is a **28 kDa homodimer** (14 kDa monomers) stabilized by an inter-chain disulfide bond at Cys106 and an intra-chain disulfide at Cys26–Cys106. Each monomer adopts a cystine-knot fold (four β-strands in an antiparallel arrangement) similar to nerve growth factor. The **receptor-binding interface** involves the loop between strands 1 and 2 and the C-terminal segment; key contacts are made with IL-17RA (Arg197, Tyr200, Pro201 on IL-17A).

**IL-17 receptor complex:** IL-17A binds the **IL-17RA/IL-17RC heterodimer**. IL-17RA (shared across IL-17A, B, C, E, F) provides high-affinity binding; IL-17RC provides specificity. Both chains contain the SEFIR (SEF/IL-17R) domain that recruits ACT1 (Act1, CIKS/MAP3K14) — the obligate signaling adaptor. IL-17RA is expressed on epithelial cells, keratinocytes, fibroblasts, osteoblasts, and endothelial cells; neuronal IL-17RA expression explains pain sensitization in psoriatic arthritis.

**Bimekizumab targeting:** Bimekizumab binds the IL-17A/IL-17F homodimer binding sites on both IL-17A and IL-17F — blocking all three heterodimeric and homodimeric forms. By neutralizing IL-17F in addition to IL-17A, bimekizumab achieves higher skin clearance rates (PASI 90 ~85% in NICKEL/BE VIVID trials) vs. anti-IL-17A-only antibodies.

## Function

**Antimicrobial defense:** IL-17A on mucosal surfaces drives expression of defensins (β-defensins 2, 3), S100A7/8/9 proteins, LL-37, and CXCL1/CXCL8 in epithelial cells → neutrophil recruitment and direct anti-fungal/bacterial activity. Patients with IL-17 pathway LOF mutations (IL17A, IL17RA, IL17RC, ACT1, STAT3) have chronic mucocutaneous candidiasis (CMCC) — demonstrating the essential role of IL-17A in *Candida* clearance.

**Keratinocyte activation:** IL-17A → IL-17RA/RC → ACT1 → TRAF6 → TAK1 → IKKβ → NF-κB AND MAPK (JNK, p38) → transcription of:
- CXCL1, CXCL5, CXCL8 → neutrophil chemotaxis
- S100A7 (psoriasin), S100A8/A9 → antimicrobial, pro-inflammatory amplification
- IL-19, IL-36 → keratinocyte autocrine loops
- CCL20 → plasmacytoid DC recruitment
- β-defensin-2/3 → direct antimicrobial

**Bone erosion:** IL-17A stimulates fibroblasts and osteoblasts to produce RANKL → osteoclast differentiation → bone erosion. This explains erosive arthritis in PsA and AS and underpins the efficacy of anti-IL-17A in joint disease.

**Synergy with TNF-alpha:** IL-17A and TNF-alpha act synergistically — TNF-alpha primes epithelial cells (via NF-κB) and IL-17A maintains chronic inflammation; the combination is far more potent than either alone in stimulating AMP and chemokine production.

## Mechanism

**Th17 polarization (upstream):** Naive CD4⁺ T cells differentiate into Th17 cells in the presence of IL-6 + TGF-β (initiation), IL-21 (amplification), and IL-23 (maintenance/effector function). The master Th17 transcription factor RORγt binds the IL17A promoter to drive IL-17A expression. STAT3 (downstream of IL-6, IL-21, IL-23) cooperates with RORγt.

**IL-17A signaling (downstream):**
1. IL-17A dimers bind IL-17RA (pre-formed at cell surface), recruit IL-17RC
2. SEFIR domains of both receptor chains recruit ACT1 via homotypic SEFIR-SEFIR interaction
3. ACT1 acts as an E3 ubiquitin ligase → K63-Ub on TRAF6 → TAK1 → IKKβ/IKKγ → IκBα phosphorylation/degradation → NF-κB nuclear translocation
4. ACT1 also recruits HuR (mRNA stabilizer) to AU-rich elements in CXCL1/8 mRNAs → mRNA stabilization → prolonged inflammatory gene expression (post-transcriptional amplification)

**Clinical paradox in MS:** Anti-IL-17A therapy (secukinumab) in RRMS Phase 2 trial (CAMS337) showed worsening relapse rates, requiring early termination. Mechanistic explanation: IL-17A may suppress CNS-damaging CD8⁺ T cell responses or regulate Treg function in the brain; alternatively, increased susceptibility to CNS infections confounds the picture. This result sharply distinguishes MS from other Th17-driven diseases and argues against a straightforward Th17-driven pathogenesis in MS.

## Connections

- `connects-to` → **[Psoriasis](../../07-system/psoriasis/README.md)** — IL-17A from skin Th17 and γδ T cells activates keratinocyte IL-17RA/RC → NF-kB → CXCL8, S100A proteins, and AMPs → neutrophil influx and epidermal hyperproliferation; secukinumab and ixekizumab achieve PASI 90 in ~60% of patients at 16 weeks.
- `connects-to` → **[IL-23](../il-23/README.md)** — IL-23 maintains the Th17 effector program and drives IL-17A via STAT3 → RORγt; risankizumab (anti-IL-23p19) achieves superior long-term psoriasis clearance vs anti-IL-17A antibodies; IL-23 sits upstream of IL-17A in the Th17 axis.
- `connects-to` → **[Rheumatoid Arthritis](../../07-system/rheumatoid-arthritis/README.md)** — IL-17A is present in RA synovium but secondary to TNF-α and IL-6; promotes osteoclastogenesis via RANKL; IL-17A inhibitors (secukinumab) failed pivotal RA trials; bimekizumab (anti-IL-17A/F) showed marginal RA benefit.
- `connects-to` → **[Multiple Sclerosis](../../07-system/multiple-sclerosis/README.md)** — IL-17A is elevated in MS lesions and CSF; Th17 cells breach the blood-brain barrier via CXCR6 → demyelination; secukinumab paradoxically worsened MS relapse rates in phase 2 trials — suggesting complex Th17/Treg balance in CNS disease.
- `connects-to` → **[Ankylosing Spondylitis](../../07-system/ankylosing-spondylitis/README.md)** — IL-17A drives enthesitis: ILC3/Th17 at entheses → RANKL + MMP → bone erosion; WNT-driven new bone formation → syndesmophytes; secukinumab (MEASURE-1: ASAS20 61%) and ixekizumab (COAST-V) are FDA-approved for AS.
- `connects-to` → **[Psoriatic Arthritis](../../07-system/psoriatic-arthritis/README.md)** — IL-17A drives PsA enthesitis, synovitis, and new bone formation; secukinumab (FUTURE 2: ACR20 54%; FDA 2016) and ixekizumab (SPIRIT-P1/2; FDA 2017) approved; entheseal ILC3 produce IL-17A independently of IL-23 in some patients.
- `connects-to` → **[Giant Cell Arteritis](../../07-system/giant-cell-arteritis/README.md)** — GCA involves Th17 (IL-17A) and Th1 (IFN-γ) CD4+ T cell infiltrate in the arterial adventitia; IL-17A amplifies macrophage/neutrophil recruitment and intimal hyperplasia; secukinumab and upadacitinib (SELECT-GCA) are under investigation.
- `connects-to` → **[Neutrophil](../../04-cellular/neutrophil/README.md)** — IL-17A drives neutrophil recruitment via CXCL1/CXCL5/CXCL8 from keratinocytes and fibroblasts; neutrophilic infiltration is the hallmark of psoriatic plaques; IL-17A + TNF-α synergise to amplify AMP expression; IL-17A LOF mutations → mucocutaneous candidiasis.
- `connects-to` → **[T Helper Cell](../../04-cellular/t-helper-cell/README.md)** — Th17 cells (CD4+ RORγt+) are the primary IL-17A producers; IL-6 + TGF-β initiate Th17 differentiation; IL-23 maintains the effector Th17 program; tissue-resident Th17 cells sustain chronic inflammation in psoriasis and AS after systemic T cell depletion.
- `connects-to` → **[Inflammatory Bowel Disease](../../07-system/inflammatory-bowel-disease/README.md)** — IL-17A is elevated in IBD mucosa but anti-IL-17A therapy (secukinumab) paradoxically worsens IBD in AS/PsA patients; gut epithelial IL-17A may protect barrier integrity — a dual role distinguishing mucosal from systemic Th17 pathogenicity.

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
