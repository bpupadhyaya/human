---
schema: human-scale-entry/v1
id: glucocorticoid-receptor
name: Glucocorticoid Receptor
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-05
summary: "Nuclear receptor (NR3C1) mediating cortisol and synthetic glucocorticoid responses. Cytoplasmic until ligand-bound → nuclear translocation → GRE transactivation and NF-κB/AP-1 transrepression → anti-inflammatory gene program. Therapeutic target in asthma, IBD, and RA."
aliases: ["GR", "NR3C1", "glucocorticoid receptor alpha", "GRα", "nuclear receptor 3C1"]
taxonomy:
  gene_symbol: "NR3C1"
  uniprot: "P04150"
sources:
  - id: hollenberg-1985-gr-cloning
    type: peer-reviewed
    cite: "Hollenberg SM, Weinberger C, Ong ES, et al. Primary structure and expression of a functional human glucocorticoid receptor cDNA. Nature. 1985;318(6047):635-41."
    doi: "10.1038/318635a0"
    pmid: "2867473"
  - id: cato-2002-gr-mechanism
    type: peer-reviewed
    cite: "Cato ACB, Wade E. Molecular mechanisms of anti-inflammatory action of glucocorticoids. BioEssays. 1996;18(5):371-8."
    doi: "10.1002/bies.950180507"
    pmid: "8639162"
  - id: rhen-2005-anti-inflammatory
    type: peer-reviewed
    cite: "Rhen T, Cidlowski JA. Antiinflammatory action of glucocorticoids — new mechanisms for old drugs. N Engl J Med. 2005;353(16):1711-23."
    doi: "10.1056/NEJMra050541"
    pmid: "16236742"
  - id: barnes-2006-gr-asthma
    type: peer-reviewed
    cite: "Barnes PJ. How corticosteroids control inflammation: quintiles prize lecture 2005. Br J Pharmacol. 2006;148(3):245-54."
    doi: "10.1038/sj.bjp.0706736"
    pmid: "16604091"
cross_links:
  - target: 01-human/03-molecular/tnf-alpha
    relation: modulates
    evidence: rhen-2005-anti-inflammatory
    note: "GR transrepresses TNF-α transcription via direct protein-protein interaction with NF-κB p65, preventing coactivator recruitment to the TNF promoter."
  - target: 01-human/03-molecular/il-6
    relation: modulates
    evidence: rhen-2005-anti-inflammatory
    note: "GR-mediated transrepression of NF-κB and AP-1 reduces IL-6 transcription in macrophages and hepatocytes without direct GRE binding."
  - target: 01-human/03-molecular/cortisol
    relation: target-of
    evidence: rhen-2005-anti-inflammatory
    note: "Cortisol is the endogenous GR ligand; binding Kd ~5 nM triggers dissociation of the HSP90/HSP70 chaperone complex and nuclear translocation."
  - target: 01-human/07-system/immune-system
    relation: modulates
    evidence: barnes-2006-gr-asthma
    note: "GR activation suppresses innate and adaptive immunity via GRE transactivation (IκBα, GILZ, Annexin-A1) and transrepression of NF-κB and AP-1 target genes."
---

# Glucocorticoid Receptor

## Overview

The glucocorticoid receptor (GR, gene *NR3C1*) is a **ligand-activated transcription factor** of the nuclear receptor superfamily, and the principal intracellular mediator of glucocorticoid hormone action. It is ubiquitously expressed across virtually every human cell type, making it one of the most broadly influential regulatory proteins in biology. When bound to its endogenous ligand cortisol (or synthetic glucocorticoids such as dexamethasone, prednisone, or budesonide), GR undergoes a dramatic conformational change, translocates from the cytoplasm to the nucleus, and orchestrates a transcriptional program that simultaneously upregulates metabolic adaptation genes and suppresses pro-inflammatory gene networks.

The molecular cloning of the GR in 1985 by Hollenberg and Evans [^hollenberg-1985-gr-cloning] was a landmark in endocrinology and pharmacology, providing the mechanistic foundation for understanding how glucocorticoids — the most widely prescribed anti-inflammatory drug class in medicine — exert their effects. GR is the direct target of synthetic corticosteroids used to treat asthma, COPD, rheumatoid arthritis, inflammatory bowel disease, multiple sclerosis relapses, organ transplant rejection, and a vast range of other inflammatory and immune-mediated conditions.

Two major mechanisms account for GR's anti-inflammatory actions [^rhen-2005-anti-inflammatory]:
1. **Transactivation** — GR homodimerizes and binds palindromic glucocorticoid response elements (GREs) to induce anti-inflammatory genes (IκBα, GILZ, Annexin-A1, MKP-1)
2. **Transrepression** — GR monomers physically interact with NF-κB and AP-1 transcription factors, preventing them from activating pro-inflammatory target genes (TNF-α, IL-6, IL-1β, COX-2) — without GR binding DNA directly

## Structure

### Domain Architecture

GR is an **87 kDa protein of 777 amino acids** (GRα isoform) organized into three principal functional domains — the canonical nuclear receptor architecture:

| Domain | Residues (human) | Function |
|:---|:---|:---|
| **N-terminal domain (NTD / AF-1)** | 1–420 | Constitutive transactivation; binds coactivators SRC-1, TIF2; disordered by X-ray crystallography |
| **DNA-binding domain (DBD)** | 421–486 | Two zinc-finger modules; dimerizes on palindromic GREs; zinc coordinated by C4 cysteines |
| **Hinge region** | 487–526 | Contains nuclear localization signal (NLS1); flexible linker |
| **Ligand-binding domain (LBD / AF-2)** | 527–777 | Cortisol-binding pocket (Kd ~5 nM); 12-helix sandwich; helix 12 repositions on ligand binding to create AF-2 coactivator groove |

### GRα vs. GRβ Isoforms

Alternative splicing of exon 9 generates two major isoforms:
- **GRα**: the canonical, ligand-responsive, transcriptionally active isoform expressed in virtually all cells
- **GRβ**: incorporates an alternative exon 9β; cannot bind glucocorticoids but acts as a dominant-negative inhibitor of GRα — overexpressed in glucocorticoid-resistant inflammatory states (steroid-resistant asthma, certain RA patients)

### Chaperone Complex (Unliganded State)

In the absence of ligand, GR resides in the **cytoplasm** bound to a large multi-protein chaperone complex that maintains it in a high-affinity, ligand-receptive conformation:

- **HSP90 dimer** — occupies the LBD groove, keeps the ligand-binding pocket open; essential for glucocorticoid binding
- **HSP70** — assists early GR folding and chaperoning
- **p23 (PTGES3)** — stabilizes the mature GR–HSP90 complex
- **FKBP51 (FKBP5)** — immunophilin co-chaperone; reduces cortisol binding affinity (Kd ~10 nM when bound); FKBP5 is a GR target gene, forming a negative feedback loop
- **FKBP52** — competes with FKBP51; increases GR nuclear transport efficiency via dynein interaction

## Function

### Genomic Mechanisms

GR's primary function is regulation of gene transcription. After cortisol (or a synthetic glucocorticoid) binds the LBD:

1. HSP90 dissociates, exposing the nuclear localization signal
2. GR is transported to the nucleus via importin-α/β and Ran-GTPase-dependent mechanisms
3. In the nucleus, GR operates via four distinct modes:

**Mode 1 — Homodimer GRE transactivation:** GR binds palindromic GREs (consensus: GGTACAnnnTGTTCT) as a homodimer → recruits coactivator complexes (SRC-1/TIF2, CBP/p300, Mediator) → RNA Pol II recruitment → gene induction. Key targets:
- *GILZ* (glucocorticoid-induced leucine zipper) — suppresses NF-κB and AP-1 downstream
- *DUSP1/MKP-1* — MAPK phosphatase; inactivates p38 MAPK and JNK
- *IKBA* (*IκBα*) — NF-κB inhibitor; indirect anti-inflammatory
- *ANXA1* (Annexin-A1/Lipocortin-1) — inhibits phospholipase A2; reduces eicosanoid production

**Mode 2 — Monomer tethering/transrepression:** GR monomers interact with the Rel homology domain of **NF-κB p65** and the bZIP domain of **AP-1 (c-Fos/c-Jun)** via protein-protein tethering. This prevents these transcription factors from activating their target promoters — the primary mechanism underlying glucocorticoid suppression of TNF-α, IL-6, IL-1β, ICAM-1, and COX-2 [^rhen-2005-anti-inflammatory].

**Mode 3 — Composite GRE:** GR monomers cooperate with other transcription factors at composite regulatory elements; context-dependent activation or repression.

**Mode 4 — Half-GRE monomer binding:** GR monomers bind single GRE half-sites; mediates some metabolic gene induction.

### Non-Genomic Mechanisms

Rapid glucocorticoid effects (seconds–minutes, too fast for transcription) involve:
- Membrane-associated GR (mGR) → activates eNOS, PI3K/Akt → vasodilation
- Cytoplasmic GR–HSP90 complex interactions with kinases (Src, PI3K)
- Displacement of arachidonic acid from membrane phospholipids

These non-genomic effects are particularly relevant at high (pharmacological) glucocorticoid doses used in acute settings (pulse methylprednisolone, IV hydrocortisone for septic shock).

### Metabolic Functions

Beyond anti-inflammation, GR drives the classical metabolic stress response:
- **Liver**: Induces PEPCK, G6Pase → hepatic gluconeogenesis; glycogen synthesis
- **Skeletal muscle**: Protein catabolism via ubiquitin-proteasome activation; reduces GLUT4
- **Adipose**: Visceral fat differentiation; lipolysis in peripheral depots
- **Bone**: Suppresses osteoblast Wnt/IGF-1 signaling → osteoporosis with chronic excess

## Mechanism

### Ligand Binding and Activation Cascade

The step-by-step activation of GR proceeds as follows:

1. **Cortisol diffuses across the plasma membrane** (lipophilic steroid; passive diffusion; serum-bound fraction 90% to CBG + albumin; only free ~3% enters cells)
2. **Cortisol binds GR-LBD** in the cytoplasm (Kd ~5 nM for cortisol; synthetic glucocorticoids vary: dexamethasone Kd ~0.5 nM, budesonide ~1 nM) → helix 12 of LBD repositions ("mousetrap" closure) → conformational change propagated through entire receptor
3. **HSP90 + co-chaperones dissociate** → FKBP51 replaced by FKBP52 → dynein motor protein associates with GR
4. **Retrograde nuclear transport**: Dynein–GR complex travels along microtubules; importin-α binds NLS1 → importin-β docks on nuclear pore complex → GR translocates into nucleus within 30–60 minutes
5. **Nuclear actions** (transactivation or transrepression, depending on chromatin context and GR partner proteins)
6. **Termination**: SUMO modification, ubiquitylation, and proteasomal degradation of nuclear GR after DNA dissociation; FKBP51 (a GR target gene) re-associates with newly synthesized GR → negative feedback attenuating further signaling

### Transrepression of NF-κB: Molecular Detail

The anti-inflammatory transrepression of NF-κB is the most clinically important GR mechanism [^cato-2002-gr-mechanism]:

1. In the absence of glucocorticoids, activated NF-κB p65/p50 binds κB sites in pro-inflammatory gene promoters and recruits coactivators (CBP/p300) → productive transcription of TNF-α, IL-6, COX-2
2. Liganded GR enters the nucleus and binds directly to the Rel homology domain of p65 via the GR-DBD/LBD interface
3. GR competes for CBP/p300 (GR and p65 require the same coactivator surface) → transcriptional silencing without GR displacing p65 from DNA
4. Additionally, GR induces IκBα (via GRE) → IκBα exports p65 from the nucleus → long-term dampening of NF-κB activity

### Glucocorticoid Pharmacology

Synthetic glucocorticoids exploit these mechanisms for therapeutic benefit:

| Drug | Glucocorticoid potency (vs. cortisol = 1) | Mineralocorticoid activity | Key uses |
|:---|:---|:---|:---|
| **Hydrocortisone** | 1 | 1 | Addison's disease replacement; acute adrenal crisis; septic shock |
| **Prednisone/prednisolone** | 4–5 | 0.6 | RA, IBD, asthma, autoimmune diseases |
| **Methylprednisolone** | 5–6 | 0.5 | MS relapses, organ transplant, IV pulse therapy |
| **Dexamethasone** | 25–30 | ~0 | Cerebral edema, croup, COVID-19 (RECOVERY trial), chemotherapy antiemesis |
| **Budesonide** | ~200 (inhaled) | Low | Asthma (inhaled), Crohn's disease (local) |

## Connections

- `target-of` → **[cortisol](../cortisol/README.md)** — GR is the intracellular receptor for cortisol (Kd ~5 nM); unliganded GR is held cytoplasmic by HSP90/HSP70 chaperone complex
- `modulates` → **[TNF-α](../tnf-alpha/README.md)** — GR transrepresses TNF-α via direct NF-κB p65 interaction, blocking coactivator recruitment
- `modulates` → **[IL-6](../il-6/README.md)** — GR transrepression of NF-κB and AP-1 reduces IL-6 transcription in macrophages and hepatocytes
- `modulates` → **[immune-system](../../07-system/immune-system/README.md)** — GR activation broadly suppresses innate and adaptive immunity via GRE-driven anti-inflammatory genes and NF-κB/AP-1 transrepression

## Pathology

| Condition | GR mechanism | Clinical features |
|:---|:---|:---|
| **Steroid-resistant asthma** | GRβ overexpression dominates over GRα; impaired transrepression; oxidative stress inactivates GR via HDAC2 deacetylation | Continued airway inflammation despite high-dose inhaled corticosteroids; requires add-on therapy (LABA, omalizumab, biologics) |
| **Glucocorticoid-induced osteoporosis** | GR suppresses Wnt/β-catenin and IGF-1 in osteoblasts; promotes osteoclast survival | Vertebral fractures with chronic oral corticosteroid use; requires bisphosphonate prophylaxis |
| **Cushing's syndrome** | Excess cortisol → chronic GR activation → metabolic, immune, musculoskeletal effects | Central obesity, hyperglycemia, hypertension, immunosuppression, proximal myopathy, psychiatric disturbance |
| **Adrenal insufficiency** | GR activation absent → inability to suppress inflammatory responses and mount metabolic stress adaptation | Adrenal crisis under physiological stress; rescued by hydrocortisone replacement |
| **PTSD / HPA dysregulation** | Augmented GR sensitivity (enhanced negative feedback) → low basal cortisol, paradoxically exaggerated GR response | Low diurnal cortisol, enhanced dexamethasone suppression; linked to trauma-induced epigenetic GR methylation |
| **NR3C1 mutations** | Loss-of-function → familial glucocorticoid resistance (Chrousos syndrome) | Hypertension, hypokalemia, mineralocorticoid excess, androgen excess; requires supraphysiological glucocorticoids |

[^hollenberg-1985-gr-cloning]: Hollenberg SM, Weinberger C, Ong ES, et al. Primary structure and expression of a functional human glucocorticoid receptor cDNA. *Nature.* 1985;318(6047):635-41. [doi:10.1038/318635a0](https://doi.org/10.1038/318635a0)
[^cato-2002-gr-mechanism]: Cato ACB, Wade E. Molecular mechanisms of anti-inflammatory action of glucocorticoids. *BioEssays.* 1996;18(5):371-8. [doi:10.1002/bies.950180507](https://doi.org/10.1002/bies.950180507)
[^rhen-2005-anti-inflammatory]: Rhen T, Cidlowski JA. Antiinflammatory action of glucocorticoids — new mechanisms for old drugs. *N Engl J Med.* 2005;353(16):1711-23. [doi:10.1056/NEJMra050541](https://doi.org/10.1056/NEJMra050541)
[^barnes-2006-gr-asthma]: Barnes PJ. How corticosteroids control inflammation: quintiles prize lecture 2005. *Br J Pharmacol.* 2006;148(3):245-54. [doi:10.1038/sj.bjp.0706736](https://doi.org/10.1038/sj.bjp.0706736)
