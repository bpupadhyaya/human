---
schema: human-scale-entry/v1
id: calcineurin
name: Calcineurin
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-07
summary: "Calcineurin (PP2B) is a Ca²⁺/calmodulin-activated phosphatase; dephosphorylates NFAT → nuclear entry → IL-2, IL-4, IFN-γ transcription in T cells. Blocked by cyclosporine·cyclophilin-A and tacrolimus·FKBP12 complexes; voclosporin FDA 2021 for lupus nephritis."
aliases: ["calcineurin", "PP2B", "protein phosphatase 2B", "PPP3CA", "PPP3CB", "calcineurin-NFAT", "NFAT signaling", "calcineurin inhibitor", "CNI", "cyclosporine target", "tacrolimus target", "FK506 target"]
sources:
  - id: liu-1991-tacrolimus-fkbp12
    type: peer-reviewed
    cite: "Liu J, Farmer JD Jr, Lane WS, et al. Calcineurin is a common target of cyclophilin-cyclosporin A and FKBP-FK506 complexes. Cell. 1991;66(4):807-815."
    doi: "10.1016/0092-8674(91)90124-H"
    pmid: "1715244"
    url: "https://doi.org/10.1016/0092-8674(91)90124-H"
  - id: crabtree-2002-nfat-calcium
    type: peer-reviewed
    cite: "Crabtree GR, Olson EN. NFAT signaling: choreography of a transcriptional dance. Cell. 2002;109 Suppl:S67-79."
    doi: "10.1016/S0092-8674(02)00699-2"
    pmid: "11983154"
    url: "https://doi.org/10.1016/S0092-8674(02)00699-2"
  - id: rovin-2021-voclosporin-aurora
    type: peer-reviewed
    cite: "Rovin BH, Teng YKO, Ginzler EM, et al. Efficacy and safety of voclosporin versus placebo for lupus nephritis (AURORA 1). Lancet. 2021;397(10279):2070-2080."
    doi: "10.1016/S0140-6736(21)00234-0"
    pmid: "33971155"
    url: "https://doi.org/10.1016/S0140-6736(21)00234-0"
  - id: schreiber-1992-cni-mechanism
    type: peer-reviewed
    cite: "Schreiber SL, Crabtree GR. The mechanism of action of cyclosporin A and FK506. Immunol Today. 1992;13(4):136-142."
    doi: "10.1016/0167-5699(92)90111-J"
    pmid: "1374689"
    url: "https://doi.org/10.1016/0167-5699(92)90111-J"
cross_links:
  - target: 01-human/04-cellular/t-helper-cell
    relation: modulates
    note: "Calcineurin dephosphorylates NFATc1-4 in activated T helper cells → nuclear entry → IL-2, IL-4, IFN-γ, TNF-α transcription; cyclosporine·cyclophilin and tacrolimus·FKBP12 inhibit calcineurin → block T cell cytokine production."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: modulates
    note: "NFAT/calcineurin drives FoxP3 expression in Tregs; CNIs at trough suppress effector T cells more than Tregs, but high-dose CNI reduces FoxP3 and Treg function; NFAT cooperates with FoxP3 at Treg-specific enhancers to maintain suppressive identity."
  - target: 01-human/03-molecular/il-2
    relation: connects-to
    note: "NFAT (dephosphorylated by calcineurin) + AP-1 + NF-κB combinatorially drive IL-2 transcription; cyclosporine/tacrolimus block calcineurin → NFAT remains phosphorylated/cytoplasmic → abolish IL-2 production → prevent T cell expansion."
  - target: 01-human/07-system/dermatomyositis
    relation: connects-to
    note: "Tacrolimus (FK506·FKBP12) inhibits calcineurin → NFAT suppression → reduced CD4+/Th17-driven muscle inflammation; used as steroid-sparing DM therapy, particularly in anti-MDA5-associated rapidly progressive ILD."
  - target: 01-human/07-system/systemic-lupus-erythematosus
    relation: connects-to
    note: "Voclosporin (CNI; FDA Jan 2021) added to MMF + low-dose steroids achieved complete renal response 40.8% vs 22.5% (AURORA-1 Lancet 2021) for lupus nephritis; CNIs also stabilize podocyte actin cytoskeleton → reduce proteinuria independently."
  - target: 01-human/07-system/gvhd
    relation: connects-to
    note: "Cyclosporine + methotrexate and tacrolimus + methotrexate are standard GVHD prophylaxis post-allogeneic HSCT; calcineurin inhibition prevents donor T cell alloreactivity by blocking IL-2 → T cell expansion; CNI tapering is timed to immune reconstitution."
---

# Calcineurin

## Overview

**Calcineurin** (protein phosphatase 2B; PP2B) is a Ca²⁺/calmodulin-dependent serine-threonine phosphatase that serves as the **essential molecular link between T cell receptor activation and gene transcription** — most critically, the transcription of IL-2, the primary T cell growth factor [^crabtree-2002-nfat-calcium]. It is the shared molecular target of two of the most impactful drugs in transplant medicine and autoimmune therapy: **cyclosporine A** and **tacrolimus (FK506)**.

The calcineurin-NFAT axis is deployed broadly across biology — in cardiac hypertrophy, osteoclastogenesis, skeletal muscle fiber-type specification, neuronal plasticity, and pancreatic β-cell insulin secretion — but its role in T cell activation is the best-characterized and most clinically relevant.

## Structure

### Protein architecture

Calcineurin is an obligate **heterodimer**:

| Subunit | Genes | Function |
|:--------|:------|:---------|
| **Calcineurin A** (CNA; catalytic) | *PPP3CA* (CNA1), *PPP3CB* (CNA2), *PPP3CC* (CNA3) | Contains catalytic phosphatase domain, calcineurin B-binding domain (BBH), calmodulin-binding domain (CaM-BD), autoinhibitory domain (AID) |
| **Calcineurin B** (CNB; regulatory) | *PPP3R1* (CNB1), *PPP3R2* (CNB2) | Four EF-hand Ca²⁺-binding domains; constitutively binds CNA; conformational change on Ca²⁺ binding activates CNA |

**Activation mechanism:**
1. TCR stimulation → PLCγ1 → IP₃ → ER Ca²⁺ release → CRAC channels (ORAI1/STIM1) → sustained Ca²⁺ influx → [Ca²⁺]i rises from ~100 nM to ~500–1000 nM
2. Ca²⁺ binds calmodulin (4 Ca²⁺ per CaM) → Ca²⁺/CaM binds CNA CaM-BD → displaces autoinhibitory domain → active phosphatase site exposed
3. Calcineurin dephosphorylates **multiple serine residues** on the NFAT regulatory domain → unmasks nuclear localization sequence (NLS)
4. NFAT imports to nucleus via importins → cooperates with Fos/Jun (AP-1) and NF-κB at composite elements → transcription of IL-2, IL-4, IL-13, TNF-α, FasL, CD40L, IFN-γ

**NFAT rephosphorylation and export:**
When Ca²⁺ falls (antigen cleared), DYRK1A and GSK-3β rephosphorylate NFAT → nuclear export via CRM1 → return to cytoplasm. Sustained calcineurin activity (sustained antigen) maintains nuclear NFAT → long-term gene transcription.

### NFATc family

| Isoform | Expression | Primary function |
|:--------|:-----------|:----------------|
| NFATc1 | T cells, B cells, osteoclasts | Master TF for osteoclastogenesis; also Th2/Tfh effector genes |
| NFATc2 | T cells, mast cells | IL-2, IL-4 transcription; T cell activation |
| NFATc3 | Ubiquitous | Cardiac hypertrophy; T cell activation backup |
| NFATc4 | Brain, heart | Neuronal and cardiac NFAT responses |

## Function

### T cell transcriptional control

The calcineurin-NFAT axis controls **hundreds of genes** in activated T cells. Most critical for immunity:

**IL-2 promoter:** An "AND gate" requiring NFAT + AP-1 + NF-κB simultaneously. NFAT alone (without costimulation-driven AP-1) results in anergy induction rather than full activation. Calcineurin inhibitors block NFAT → prevent IL-2 transcription → T cell cannot undergo antigen-driven clonal expansion.

**Effector cytokines:**
- NFAT + AP-1 → IFN-γ (Th1), IL-4 (Th2), IL-13 (Th2), IL-17A (Th17 — NFAT + RORγt)
- Bcl-xL (survival), FasL (effector function), CD40L (B cell help)

### Cardiac hypertrophy

Pathological Ca²⁺ overload (pressure overload, ischemia) activates calcineurin → NFATc3/c4 → drive re-expression of fetal genes: β-MHC (*MYH7*), skeletal α-actin (*ACTA1*), ANP (*NPPA*), BNP (*NPPB*). **RCAN1** (regulator of calcineurin 1; also DSCR1) is an endogenous feedback inhibitor of calcineurin — encoded on chromosome 21, explaining the increased cardiac calcineurin-NFAT signaling in Down syndrome.

### Osteoclastogenesis

RANKL → TRAF6 → PLC → Ca²⁺ oscillations → calcineurin → NFATc1 (master osteoclast TF) → cathepsin K, TRAP, integrin αV, MMP-9 → mature osteoclast. A positive feedback loop: NFATc1 transcribes more *NFATC1* → amplification.

## Mechanism

### Calcineurin inhibitor mechanism

The discovery that **cyclosporine** and **tacrolimus** share the same enzymatic target — calcineurin — despite having completely different chemical structures and binding to different immunophilins was a landmark finding [^liu-1991-tacrolimus-fkbp12]:

**Cyclosporine A (CsA):**
- Cyclic undecapeptide from *Tolypocladium inflatum*
- Binds **cyclophilin A** (CyPA; *PPIA*): peptidyl-prolyl isomerase (PPIase); CsA occupies the PPIase active site
- CsA·CyPA complex presents a new surface that inserts into calcineurin's catalytic site → steric blockade of phosphatase activity
- Does NOT inhibit CyPA PPIase activity per se — the complex is the active inhibitor

**Tacrolimus (FK506):**
- Macrolide lactone from *Streptomyces tsukubaensis*; binds **FKBP12** (FK506-binding protein; PPIase)
- FK506·FKBP12 complex → binds calcineurin at same composite site as CsA·CyPA → same phosphatase blockade
- ~10–100× more potent than CsA for calcineurin inhibition on a molar basis

**Voclosporin:**
- Semi-synthetic CsA analog (one-carbon elongation at position 4 of the α-aminobutyric acid residue)
- ~3× higher calcineurin affinity than CsA with reduced nephrotoxic profile
- Additional mechanism: stabilizes **synaptopodin** (podocyte actin-binding protein) → prevents cathepsin L-mediated cleavage → preserves podocyte foot process architecture → reduces proteinuria via T-cell-independent mechanism
- Approved FDA January 2021 for active lupus nephritis; given as oral capsule with MMF + low-dose prednisone [^rovin-2021-voclosporin-aurora]

**Topical CNIs (pimecrolimus, tacrolimus ointment):**
- Penetrate skin, block calcineurin in dermal T cells and mast cells → reduce atopic dermatitis inflammation without skin atrophy (unlike topical corticosteroids)
- FDA 2001 (pimecrolimus/Elidel) and 2000 (tacrolimus/Protopic); second-line for AD after topical steroids

### NFAT-independent calcineurin functions

Calcineurin also dephosphorylates:
- **Drp1** (dynamin-like GTPase) → promotes mitochondrial fission; relevant in cardiac failure
- **Synaptophysin** and other synaptic vesicle proteins → neuronal function
- **BAD** (BCL-2 family) → Ca²⁺-regulated apoptosis control

## Connections

- `modulates` → **[T Helper Cell](../../04-cellular/t-helper-cell/README.md)** — Calcineurin dephosphorylates NFATc1-4 in activated T helper cells → nuclear entry → IL-2, IL-4, IFN-γ, TNF-α transcription; cyclosporine·cyclophilin and tacrolimus·FKBP12 inhibit calcineurin → block T cell cytokine production.
- `modulates` → **[Regulatory T Cell](../../04-cellular/regulatory-t-cell/README.md)** — NFAT/calcineurin drives FoxP3 expression in Tregs; CNIs at trough suppress effector T cells more than Tregs, but high-dose CNI reduces FoxP3 and Treg function; NFAT cooperates with FoxP3 at Treg-specific enhancers.
- `connects-to` → **[IL-2](../il-2/README.md)** — NFAT (dephosphorylated by calcineurin) + AP-1 + NF-κB combinatorially drive IL-2 transcription; cyclosporine/tacrolimus block calcineurin → NFAT remains phosphorylated → abolish IL-2 production → prevent T cell expansion.
- `connects-to` → **[Dermatomyositis](../../07-system/dermatomyositis/README.md)** — Tacrolimus (FK506·FKBP12) inhibits calcineurin → NFAT suppression → reduced CD4+/Th17-driven muscle inflammation; used as steroid-sparing DM therapy, particularly in anti-MDA5-associated rapidly progressive ILD.
- `connects-to` → **[Systemic Lupus Erythematosus](../../07-system/systemic-lupus-erythematosus/README.md)** — Voclosporin (CNI; FDA Jan 2021) added to MMF + low-dose steroids achieved complete renal response 40.8% vs 22.5% (AURORA-1 Lancet 2021) for lupus nephritis; CNIs also stabilize podocyte actin cytoskeleton → reduce proteinuria independently.
- `connects-to` → **[GVHD](../../07-system/gvhd/README.md)** — Cyclosporine + methotrexate and tacrolimus + methotrexate are standard GVHD prophylaxis post-allogeneic HSCT; calcineurin inhibition prevents donor T cell alloreactivity by blocking IL-2 → T cell expansion; CNI tapering is timed to immune reconstitution.

[^liu-1991-tacrolimus-fkbp12]: Liu J, Farmer JD Jr, Lane WS, et al. Calcineurin is a common target of cyclophilin-cyclosporin A and FKBP-FK506 complexes. *Cell.* 1991;66(4):807-815. [doi:10.1016/0092-8674(91)90124-H](https://doi.org/10.1016/0092-8674(91)90124-H) · [PubMed 1715244](https://pubmed.ncbi.nlm.nih.gov/1715244/)
[^crabtree-2002-nfat-calcium]: Crabtree GR, Olson EN. NFAT signaling: choreography of a transcriptional dance. *Cell.* 2002;109 Suppl:S67-79. [doi:10.1016/S0092-8674(02)00699-2](https://doi.org/10.1016/S0092-8674(02)00699-2) · [PubMed 11983154](https://pubmed.ncbi.nlm.nih.gov/11983154/)
[^rovin-2021-voclosporin-aurora]: Rovin BH, Teng YKO, Ginzler EM, et al. Efficacy and safety of voclosporin versus placebo for lupus nephritis (AURORA 1). *Lancet.* 2021;397(10279):2070-2080. [doi:10.1016/S0140-6736(21)00234-0](https://doi.org/10.1016/S0140-6736(21)00234-0) · [PubMed 33971155](https://pubmed.ncbi.nlm.nih.gov/33971155/)
[^schreiber-1992-cni-mechanism]: Schreiber SL, Crabtree GR. The mechanism of action of cyclosporin A and FK506. *Immunol Today.* 1992;13(4):136-142. [doi:10.1016/0167-5699(92)90111-J](https://doi.org/10.1016/0167-5699(92)90111-J) · [PubMed 1374689](https://pubmed.ncbi.nlm.nih.gov/1374689/)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
