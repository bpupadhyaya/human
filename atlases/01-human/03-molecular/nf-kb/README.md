---
schema: human-scale-entry/v1
id: nf-kb
name: NF-κB
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-05
summary: "Master transcription factor of inflammation. IKKβ phosphorylates IκBα → proteasomal degradation → p65/p50 nuclear translocation → TNF-α, IL-6, IL-1β, COX-2 transcription. Activated by LPS, TNF-α, IL-1β, oxidative stress, and viral dsRNA."
aliases: ["NF-κB", "nuclear factor kappa B", "NFKB", "p65/p50", "RelA/p50", "NF-kB"]
taxonomy:
  gene_symbol: "RELA"
  uniprot: "Q04206"
sources:
  - id: sen-1986-nfkb-discovery
    type: peer-reviewed
    cite: "Sen R, Baltimore D. Multiple nuclear factors interact with the immunoglobulin enhancer sequences. Cell. 1986;46(5):705-16."
    doi: "10.1016/0092-8674(86)90346-6"
    pmid: "3091258"
  - id: karin-2000-nfkb-cancer-inflammation
    type: peer-reviewed
    cite: "Karin M, Cao Y, Greten FR, Li ZW. NF-κB in cancer: from innocent bystander to major culprit. Nat Rev Cancer. 2002;2(4):301-10."
    doi: "10.1038/nrc780"
    pmid: "12001991"
  - id: hayden-2012-nfkb-signaling
    type: peer-reviewed
    cite: "Hayden MS, Ghosh S. NF-κB, the first quarter-century: remarkable progress and outstanding questions. Genes Dev. 2012;26(3):203-34."
    doi: "10.1101/gad.183434.111"
    pmid: "22302935"
  - id: liu-2017-nfkb-inflammation
    type: peer-reviewed
    cite: "Liu T, Zhang L, Joo D, Sun SC. NF-κB signaling in inflammation. Signal Transduct Target Ther. 2017;2:17023."
    doi: "10.1038/sigtrans.2017.23"
    pmid: "29158945"
cross_links:
  - target: 01-human/03-molecular/tnf-alpha
    relation: modulates
    evidence: hayden-2012-nfkb-signaling
    note: "NF-κB p65/p50 binds κB sites in the TNF promoter driving TNF-α transcription; TNF-α in turn activates NF-κB in a positive-feedback loop."
  - target: 01-human/03-molecular/il-6
    relation: modulates
    evidence: hayden-2012-nfkb-signaling
    note: "NF-κB is the dominant transcriptional activator of the IL-6 gene via two κB sites in the IL-6 promoter; blocked by IκBα or GR transrepression."
  - target: 01-human/04-cellular/macrophage
    relation: modulates
    evidence: liu-2017-nfkb-inflammation
    note: "In M1 macrophages, LPS→TLR4→MyD88→IKKβ→NF-κB drives the pro-inflammatory gene program including TNF-α, IL-6, IL-12, and iNOS."
  - target: 03-medicine/03-food/curcumin
    relation: modulated-by
    evidence: liu-2017-nfkb-inflammation
    note: "Curcumin inhibits IKKβ, preventing IκBα phosphorylation and NF-κB nuclear translocation; demonstrated in cancer cell lines and inflammatory disease models."
  - target: 01-human/03-molecular/nitric-oxide
    relation: modulated-by
    note: "Modulated by Nitric Oxide."
  - target: 01-human/03-molecular/prostaglandins
    relation: modulated-by
    note: "Modulated by Prostaglandins (Eicosanoids)."
  - target: 02-pathogen/01-viruses/zika-virus
    relation: modulated-by
    note: "Modulated by Zika Virus (ZIKV)."
  - target: 03-medicine/03-food/sulforaphane
    relation: modulated-by
    note: "Modulated by Sulforaphane."
  - target: 03-medicine/03-food/resveratrol
    relation: modulated-by
    note: "Modulated by Resveratrol."
  - target: 03-medicine/03-food/quercetin
    relation: modulated-by
    note: "Modulated by Quercetin."
  - target: 03-medicine/02-traditional/milk-thistle
    relation: modulated-by
    note: "Modulated by Milk Thistle / Silymarin (Silybum marianum)."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "NF-κB (p65/p50) is required for IFN-β enhanceosome assembly with IRF3 + AP-1; TLR7/9 signals activate both NF-κB and IRF7 via MyD88 → parallel IFN-α/β and inflammatory cytokine production; type I IFN-induced SOCS1 provides negative feedback on NF-κB."
  - target: 01-human/03-molecular/il-36
    relation: modulated-by
    note: "IL-36α/β/γ signal via IL-36R/IL-1RAcP → MyD88 → IRAK4 → TRAF6 → TAK1 → IKKβ → NF-κB p65; downstream: IL-6, CXCL1/8, CCL20, S100A proteins — key mediators of neutrophil recruitment in pustular psoriasis; IL-36Ra (IL36RN) limits this signaling."
---

# NF-κB

## Overview

NF-κB (Nuclear Factor kappa-light-chain-enhancer of activated B cells) is the **master transcription factor of inflammation**, infection-response, and cell survival. Discovered in 1986 by Sen and Baltimore as a nuclear factor binding the κ light-chain immunoglobulin enhancer in activated B cells [^sen-1986-nfkb-discovery], NF-κB is now known to be a ubiquitous, inducible regulator of hundreds of target genes across virtually all mammalian cell types. It integrates upstream danger signals — bacterial LPS, viral nucleic acids, pro-inflammatory cytokines, oxidative stress, DNA damage, and antigen receptor activation — into a rapid, powerful transcriptional response that upregulates cytokines, chemokines, cell adhesion molecules, anti-apoptotic proteins, and immune effector enzymes.

NF-κB is not a single protein but a **family of five related transcription factors** (RelA/p65, RelB, c-Rel, p50/NF-κB1, p52/NF-κB2) that form homo- and heterodimers. The most abundant and best-characterized form in inflammatory signaling is the **p65/p50 heterodimer** (RelA/p50), which drives canonical NF-κB pathway activation. In unstimulated cells, this dimer is sequestered in the cytoplasm by inhibitory IκB proteins (principally IκBα). Activation via the canonical pathway requires IκB kinase (IKK) complex-mediated phosphorylation and proteasomal degradation of IκBα, releasing p65/p50 to translocate to the nucleus and activate target gene transcription [^hayden-2012-nfkb-signaling].

The clinical importance of NF-κB spans virtually every inflammatory disease: rheumatoid arthritis, Crohn's disease, atherosclerosis, septic shock, cancer, and neurodegenerative conditions. It is simultaneously a validated therapeutic target and a master survival factor — complicating drug development, as complete inhibition causes immune suppression and oncogenesis from impaired apoptosis.

## Structure

### NF-κB Family Members

All five NF-κB/Rel proteins share a highly conserved **Rel homology domain (RHD, ~300 aa)** responsible for:
- DNA binding to κB sites (5′-GGGRNNTCC-3′ consensus)
- Dimerization
- IκB protein binding (masking nuclear localization signal)
- Nuclear translocation signal (NLS)

| Subunit | Gene | Features | Preferred dimer |
|:---|:---|:---|:---|
| **RelA (p65)** | *RELA* | Strong transactivation domain (TAD); canonical pathway | p65/p50 |
| **RelB** | *RELB* | Leucine zipper; non-canonical pathway | RelB/p52 |
| **c-Rel** | *REL* | Lymphocyte-specific; lymphoma driver | c-Rel/p50 |
| **p50 (NF-κB1)** | *NFKB1* | Lacks TAD; derived from p105 precursor by proteasomal processing; forms repressive homodimers | p65/p50 |
| **p52 (NF-κB2)** | *NFKB2* | Lacks TAD; derived from p100 precursor; non-canonical pathway | RelB/p52 |

### IκB Inhibitor Family

IκB proteins share a series of ankyrin repeats that mask the NLS of NF-κB dimers. The principal members are:

| IκB | Gene | Features |
|:---|:---|:---|
| **IκBα** | *NFKBIA* | Primary canonical pathway inhibitor; rapid degradation and resynthesis; NF-κB target gene (negative feedback) |
| **IκBβ** | *NFKBIB* | Slower degradation; persistent NF-κB activation |
| **IκBε** | *NFKBIE* | Delayed kinetics; fine-tunes oscillation |
| **p105/p100** | *NFKB1/2* | Precursors with ankyrin repeats; processed to p50/p52 by proteasome |

### IKK Complex (Signal Integrator)

The IκB kinase (IKK) complex is the critical signal-integration hub of canonical NF-κB activation:
- **IKKα (IKK1)** — catalytic; non-canonical and some canonical signaling
- **IKKβ (IKK2)** — principal catalytic subunit of canonical NF-κB activation; phosphorylates IκBα at Ser32 and Ser36
- **NEMO (IKKγ)** — regulatory scaffold; essential for canonical activation; polyubiquitin-binding domain links upstream signals to IKK

## Function

### Canonical (Classical) NF-κB Pathway

The canonical pathway is the dominant mechanism in innate immune activation:

**Target genes of canonical NF-κB:**
- **Cytokines**: TNF-α, IL-6, IL-1β, IL-8 (CXCL8), IL-12, IL-18
- **Chemokines**: MCP-1 (CCL2), RANTES (CCL5), IP-10 (CXCL10)
- **Enzymes**: COX-2 (PTGS2), iNOS (NOS2)
- **Cell adhesion**: ICAM-1 (CD54), VCAM-1, E-selectin (CD62E)
- **Anti-apoptotic**: BCL-2, BCL-XL, cIAP1/2, XIAP, A20 (TNFAIP3)
- **Immune effectors**: MHC-I, MHC-II, complement components

### Non-Canonical (Alternative) NF-κB Pathway

Activated by a subset of TNF superfamily receptors (BAFF-R, CD40, LTβR, RANK):
1. **NIK** (NF-κB-inducing kinase) accumulates (escaping TRAF3-mediated degradation)
2. NIK phosphorylates and activates **IKKα homodimers**
3. IKKα phosphorylates **p100** → partial proteasomal processing → **p52**
4. **RelB/p52** translocates to nucleus → target genes for lymphoid organogenesis, B-cell survival, bone biology

### NF-κB in Cell Survival and Apoptosis

Beyond inflammation, NF-κB is a major **anti-apoptotic survival factor**:
- Induces BCL-2, BCL-XL, XIAP, cIAPs → blocks mitochondrial apoptosis
- Induces c-FLIP → blocks death receptor (TNFR1/TRAIL-R)-mediated caspase-8 activation
- This survival function explains why constitutive NF-κB activation is oncogenic and why NF-κB inhibition sensitizes cancer cells to chemotherapy-induced apoptosis

## Mechanism

### Canonical Pathway: Signal → Transcription

**Activation triggers** (upstream sensors):
- **TLR4/LPS** → MyD88/TRIF → TRAF6 → LUBAC/TAK1 → IKKβ
- **TNF-α/TNFR1** → TRADD → TRAF2 → RIP1 → IKKβ (classic positive feedback)
- **IL-1β/IL-1R1** → MyD88 → IRAK4 → TRAF6 → TAK1 → IKKβ
- **BCR/TCR** → PKCβ/θ → CBM complex → IKKβ
- **Viral dsRNA/RIG-I/MDA5** → MAVS → TRAF3/6 → IKKβ
- **Oxidative stress, genotoxic stress** → ATM → NEMO → IKKβ

**Canonical signaling cascade:**

1. Upstream signals activate IKKβ (phospho-Ser177/Ser181 in activation loop)
2. **IKKβ phosphorylates IκBα** at Ser32 and Ser36
3. Phospho-IκBα is recognized by the **SCF-βTrCP E3 ubiquitin ligase** → K48-linked polyubiquitylation
4. **26S proteasome degrades IκBα** (within 15–30 min of stimulation)
5. **p65/p50 NLS exposed** → importin-α3/α4 binds → nuclear import
6. p65/p50 binds κB sites in target gene promoters/enhancers → recruits CBP/p300, SRC-1, Mediator complex → RNA Pol II initiation
7. **IκBα resynthesis** (IκBα is itself an NF-κB target gene) → new IκBα enters nucleus → strips p65/p50 from DNA → nuclear export → **negative feedback oscillation** (NF-κB pulses with ~90-min period in cells)

### Oscillatory Dynamics

Single-cell live imaging studies revealed that NF-κB does not activate in a simple binary on/off fashion but oscillates between nucleus and cytoplasm in repeated ~90-min cycles driven by the IκBα negative feedback loop. The number and amplitude of NF-κB pulses (not simply total nuclear NF-κB) encodes signal identity and determines differential target gene expression — a remarkable information-encoding mechanism using oscillation rather than amplitude modulation.

### Post-Translational Regulation of p65

Beyond IκBα, p65/RelA is extensively regulated by post-translational modifications:
- **Phosphorylation**: PKAc at Ser276 (enhances CBP binding); IKKβ at Ser536 (activation); GSK3β at Ser468 (repression)
- **Acetylation**: CBP/p300 acetylate Lys218/221 (enhances DNA binding), Lys310 (required for full transcriptional activity); HDAC3/SIRT1 deacetylate → nuclear export
- **Methylation**: SETD6 monomethylates Lys310 → represses activity; KDM2A demethylates → activates
- **SUMOylation** and **ubiquitylation** fine-tune nuclear p65 levels and transcriptional output

## Connections

- `modulates` → **[TNF-α](../tnf-alpha/README.md)** — NF-κB p65/p50 binds κB sites in the TNF promoter; TNF-α reciprocally activates NF-κB
- `modulates` → **[IL-6](../il-6/README.md)** — dominant transcriptional activator of IL-6 via two promoter κB sites
- `modulates` → **[macrophage](../../04-cellular/macrophage/README.md)** — LPS→TLR4→IKKβ→NF-κB drives the entire M1 macrophage pro-inflammatory gene program
- `modulated-by` → **[curcumin](../../../03-medicine/03-food/curcumin/README.md)** — curcumin inhibits IKKβ, preventing IκBα phosphorylation and NF-κB nuclear translocation
- `connects-to` → **[Type I Interferon](../type-i-interferon/README.md)** — NF-κB (p65/p50) is required for IFN-β enhanceosome assembly with IRF3 + AP-1; TLR7/9 signals activate both NF-κB and IRF7 via MyD88 → parallel IFN-α/β and inflammatory cytokine production; type I IFN-induced SOCS1 provides negative feedback on NF-κB.
- `modulated-by` → **[IL-36](../il-36/README.md)** — IL-36α/β/γ signal via IL-36R/IL-1RAcP → MyD88 → IRAK4 → TRAF6 → TAK1 → IKKβ → NF-κB p65; downstream: IL-6, CXCL1/8, CCL20, S100A proteins — key mediators of neutrophil recruitment in pustular psoriasis; IL-36Ra (IL36RN) limits this signaling.

## Pathology

| Disease | NF-κB role | Therapeutic implication |
|:---|:---|:---|
| **Rheumatoid arthritis** | Synovial fibroblasts and macrophages: constitutive NF-κB → TNF-α, IL-6, MMP production → synovitis and joint destruction | Anti-TNF biologics (adalimumab, infliximab) indirectly target NF-κB output; bortezomib tested in refractory cases |
| **Inflammatory bowel disease** | Mucosal macrophages + epithelium: NF-κB drives IL-6, IL-12, TNF-α → chronic intestinal inflammation | Anti-TNF (infliximab/adalimumab) and anti-IL-12/23 (ustekinumab) approved; budesonide locally suppresses NF-κB |
| **Septic shock** | LPS → macrophage TLR4 → massive NF-κB → cytokine storm → multi-organ failure | Dexamethasone, hydrocortisone for adrenal insufficiency; direct NF-κB inhibition too immunosuppressive |
| **Atherosclerosis** | Endothelial NF-κB (activated by oxidized LDL, disturbed flow) → VCAM-1, MCP-1 → monocyte recruitment → foam cell formation | Statins reduce NF-κB activity partly via reduced isoprenoid depletion of Ras; no direct NF-κB inhibitors approved |
| **Multiple myeloma** | Constitutive non-canonical NF-κB (NIK/IKKα) → plasma cell survival via BCL-2, XIAP | Bortezomib (proteasome inhibitor) accumulates IκBα → NF-κB suppression; approved first-line |
| **DLBCL (ABC subtype)** | Constitutive canonical NF-κB via CARD11/MALT1 mutations or chronic BCR activation | BTK inhibitor ibrutinib; MALT1 inhibitor investigation |
| **Alzheimer's disease** | Microglial NF-κB drives neuroinflammation (TNF-α, IL-6, IL-1β, iNOS) → neuronal damage | Experimental anti-neuroinflammatory strategies targeting NF-κB pathway |
| **Cancer (general)** | Constitutive NF-κB promotes tumor cell survival, angiogenesis (VEGF), invasion (MMP-9), and immune evasion (PD-L1) | Indirect inhibition via proteasome inhibitors, anti-cytokines; direct IKKβ inhibitors in clinical trials |

[^sen-1986-nfkb-discovery]: Sen R, Baltimore D. Multiple nuclear factors interact with the immunoglobulin enhancer sequences. *Cell.* 1986;46(5):705-16. [doi:10.1016/0092-8674(86)90346-6](https://doi.org/10.1016/0092-8674(86)90346-6)
[^karin-2000-nfkb-cancer-inflammation]: Karin M, Cao Y, Greten FR, Li ZW. NF-κB in cancer: from innocent bystander to major culprit. *Nat Rev Cancer.* 2002;2(4):301-10. [doi:10.1038/nrc780](https://doi.org/10.1038/nrc780)
[^hayden-2012-nfkb-signaling]: Hayden MS, Ghosh S. NF-κB, the first quarter-century: remarkable progress and outstanding questions. *Genes Dev.* 2012;26(3):203-34. [doi:10.1101/gad.183434.111](https://doi.org/10.1101/gad.183434.111)
[^liu-2017-nfkb-inflammation]: Liu T, Zhang L, Joo D, Sun SC. NF-κB signaling in inflammation. *Signal Transduct Target Ther.* 2017;2:17023. [doi:10.1038/sigtrans.2017.23](https://doi.org/10.1038/sigtrans.2017.23)
