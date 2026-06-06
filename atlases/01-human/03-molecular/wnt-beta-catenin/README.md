---
schema: human-scale-entry/v1
id: wnt-beta-catenin
name: Wnt/beta-catenin
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-06
summary: "Canonical Wnt pathway; Wnt ligands inhibit β-catenin destruction complex (APC/Axin/GSK-3β/CK1) → nuclear β-catenin → TCF/LEF target genes (MYC, CCND1). APC mutation initiates >80% of colorectal cancers; porcupine inhibitors block Wnt secretion for therapy."
aliases: ["Wnt signaling", "canonical Wnt pathway", "beta-catenin pathway", "Wnt/β-catenin", "APC pathway"]
sources:
  - id: clevers-2006-wnt
    type: peer-reviewed
    cite: "Clevers H. Wnt/beta-catenin signaling in development and disease. Cell. 2006;127(3):469-480."
    doi: "10.1016/j.cell.2006.10.018"
    pmid: "17081971"
    url: "https://doi.org/10.1016/j.cell.2006.10.018"
  - id: nusse-2017-wnt
    type: peer-reviewed
    cite: "Nusse R, Clevers H. Wnt/β-Catenin Signaling, Disease, and Emerging Therapeutic Modalities. Cell. 2017;169(6):985-999."
    doi: "10.1016/j.cell.2017.05.016"
    pmid: "28575679"
    url: "https://doi.org/10.1016/j.cell.2017.05.016"
  - id: fearon-1990-apc
    type: peer-reviewed
    cite: "Fearon ER, Vogelstein B. A genetic model for colorectal tumorigenesis. Cell. 1990;61(5):759-767."
    doi: "10.1016/0092-8674(90)90186-I"
    pmid: "2188735"
    url: "https://doi.org/10.1016/0092-8674(90)90186-I"
cross_links:
  - target: 01-human/06-organ/large-intestine
    relation: modulates
    note: "Wnt/β-catenin is the master regulator of intestinal stem cell self-renewal in colonic crypts; APC loss (adenomatous polyposis coli gene) is the initiating mutation in >80% of colorectal cancers — the first step in the Fearon-Vogelstein adenoma-carcinoma sequence."
  - target: 01-human/03-molecular/kras
    relation: connects-to
    note: "APC/Wnt loss and KRAS mutation cooperate in CRC progression: Wnt activation maintains intestinal stem cell identity (step 1), KRAS drives proliferation and survival (step 2); combined Wnt inhibition and KRAS G12D inhibition shows synergistic anti-tumor activity in CRC models."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "TGF-β and Wnt/β-catenin have context-dependent crosstalk: TGF-β can activate β-catenin in SMAD-independent manner in EMT; simultaneously TGF-β activates SMAD4 which represses Wnt target genes in normal epithelium; SMAD4 loss (late-stage CRC, ~55%) removes this Wnt brake."
  - target: 01-human/04-cellular/fibroblast
    relation: modulates
    note: "Wnt signals from tumor cells activate stromal fibroblasts → myofibroblast differentiation → desmoplasia; CAF-secreted Wnt ligands also feed back onto tumor cells; Wnt-driven fibroblast activation is a key mediator of the immunosuppressive stroma in CRC and PDAC."
---

# Wnt/beta-catenin

## Overview

The **Wnt/β-catenin pathway** (canonical Wnt signaling) is one of the most evolutionarily ancient and conserved cell-to-cell communication systems in metazoans — essential for embryonic patterning, stem cell self-renewal, and tissue homeostasis throughout adult life. Discovered via oncovirus studies and Drosophila segment polarity genetics in the 1980s, the pathway centers on the dual-function protein **β-catenin (CTNNB1)**: a structural component of adherens junctions (linking E-cadherin to the actin cytoskeleton) and, when Wnt-activated, a **transcriptional co-activator** that binds TCF/LEF transcription factors to drive proliferative target gene programs.

In the **absence of Wnt ligands (OFF state):**
- β-catenin is constitutively phosphorylated by the **destruction complex** (APC scaffold protein + Axin + GSK-3β + CK1α) → phospho-β-catenin (Ser33/Ser37/Thr41/Ser45) → β-TrCP E3 ligase → ubiquitination → proteasomal degradation
- TCF/LEF transcription factors are bound by Groucho repressors → target gene silence

In the **presence of Wnt ligands (ON state):**
- Wnt glycolipoproteins bind Frizzled receptor + LRP5/6 co-receptor → Dishevelled (Dvl) recruited → inhibits GSK-3β (via axin recruitment to LRP5/6) → destruction complex disassembled → β-catenin phosphorylation blocked → **β-catenin accumulates** → translocates to nucleus → displaces Groucho from TCF/LEF → co-activator recruitment (CBP/p300) → target gene transcription

**Wnt target genes** include: MYC (proto-oncogene), CCND1 (cyclin D1, cell cycle), AXIN2 (negative feedback), LGR5 (intestinal stem cell marker), MMP7 (invasion), CD44 (cancer stem cell marker), survivin (anti-apoptosis), fibronectin.

**Clinical significance:**
- APC (adenomatous polyposis coli, the destruction complex scaffold) is mutated in ~80% of colorectal cancers (CRC) — the founding step of the Fearon-Vogelstein adenoma-carcinoma sequence [^fearon-1990-apc]
- β-catenin (CTNNB1) activating mutations (exon 3 phosphorylation site) occur in ~5% of CRC, hepatocellular carcinoma, ovarian, endometrial, and Wilms tumor
- Familial adenomatous polyposis (FAP): germline APC mutations → hundreds to thousands of polyps → near-certain CRC by age 40

## Structure

### The destruction complex [^clevers-2006-wnt]

The **β-catenin destruction complex** is a macromolecular scaffold with four core components:

- **APC (adenomatous polyposis coli, 2843 aa):** Scaffold for β-catenin binding and presentation to GSK-3β; multiple β-catenin binding repeats (20-aa repeats and SAMP repeats for Axin binding); largest tumor suppressor in the human genome (chromosome 5q22)
- **Axin (Axin1, 862 aa):** Scaffold organizing the complex; RGS domain (binds APC), β-catenin binding domain, GSK-3β binding domain, DIX domain (dimerization and Dvl interaction); rate-limiting component of the complex (low endogenous expression)
- **GSK-3β (glycogen synthase kinase 3β):** Serine/threonine kinase; phosphorylates β-catenin Thr41 and Ser37 (followed by CK1α priming at Ser45 and Ser33/37 by GSK-3β) → phospho-degron for β-TrCP recognition
- **CK1α (casein kinase 1α):** Initiating kinase; phosphorylates β-catenin Ser45 first → creates GSK-3β recognition site; also phosphorylates APC and Axin to maintain complex integrity

### β-catenin protein

β-catenin (781 aa) has a tripartite structure:
- **N-terminal domain (aa 1-130):** Contains the phosphorylation degron (Ser33/37/Thr41/Ser45); site of APC binding; p300/CBP interaction when transcriptionally active
- **Central armadillo repeat domain (aa 130-666):** 12 armadillo repeats forming a superhelix; the main protein-protein interaction platform; binds E-cadherin (structural), TCF/LEF (transcriptional), APC, Axin, α-catenin
- **C-terminal domain (aa 667-781):** Transcriptional activation domain; recruits Pygo (Pygopus), BCL9, and BRG1 (SWI/SNF chromatin remodeling) for target gene activation

### Non-canonical Wnt pathways

Beyond canonical (β-catenin-dependent) signaling, Wnt ligands activate:
- **Wnt/PCP (planar cell polarity):** Via Dvl→RhoA/Rac1→JNK → cytoskeletal reorganization, cell motility, convergent extension during gastrulation
- **Wnt/Ca²⁺ pathway:** Via Dvl→G proteins→PLC→IP3→Ca²⁺ → CaMKII → NF-κB, NFAT; roles in neural development and tumor invasion

## Function

### Intestinal homeostasis: the crypt-villus axis [^clevers-2006-wnt]

The intestinal epithelium is the fastest self-renewing tissue in the body (~4 days turnover), powered by a Wnt gradient:
- **Crypt base:** LGR5+ stem cells; high Wnt signal from Paneth cells (crypts in small intestine) and stromal cells → β-catenin active → MYC, CCND1 expression → proliferation, self-renewal
- **Lower crypt:** Transit-amplifying cells; intermediate Wnt → rapid proliferation
- **Crypt-villus junction and villus:** Low Wnt → BMP pathway dominant → differentiation into absorptive enterocytes, goblet cells, enteroendocrine cells → apoptosis at villus tip
- **Colon:** Similar gradient in surface crypts; LGR5+ stem cells at crypt base → EPHB/Ephrin gradients compartmentalize differentiation

**APC as tumor suppressor:**
- APC haploinsufficiency → mildly elevated β-catenin → increased stem cell number but still regulated
- Loss of second APC allele (LOH at 5q22) → destruction complex collapses → constitutive β-catenin → MYC, CCND1, survivin → adenoma formation
- Subsequent KRAS, SMAD4/TGF-β, and TP53 mutations → CRC progression (Fearon-Vogelstein model)

### Wnt in development

- **Embryonic axis determination:** Wnt gradient specifies dorsal-ventral axis (amphibian cortical rotation → β-catenin stabilization on dorsal side → Spemann organizer); anterior-posterior patterning in all bilaterians
- **Stem cell maintenance:** Hematopoietic stem cells (HSC), neural stem cells, hair follicle stem cells — all depend on Wnt for self-renewal
- **Bone remodeling:** LRP5/6-mediated Wnt signaling promotes osteoblast differentiation; loss-of-function LRP5 mutations → osteoporosis-pseudoglioma syndrome; gain-of-function → high bone mass

### Wnt in cancer beyond CRC [^nusse-2017-wnt]

- **Hepatocellular carcinoma (HCC):** CTNNB1 exon 3 mutations in ~33%; associated with macrotrabecular HCC morphology; CTNNB1 mutation predicts poor response to immunotherapy (immune exclusion)
- **Medulloblastoma:** WNT subtype (most favorable prognosis); APC or CTNNB1 mutations; activated nuclear β-catenin
- **Triple-negative breast cancer (TNBC):** Wnt5a/b, FZD7 expression; Wnt drives cancer stem cell maintenance in TNBC
- **Desmoid tumors (aggressive fibromatosis):** CTNNB1 point mutations (T41A, S45F) or APC germline → stromal β-catenin → aggressive fibrotic proliferation; treated with sulindac (NSAID, lowers PGE2 → Wnt attenuation) or sorafenib

## Mechanism

### Wnt pathway activation and nuclear signaling [^nusse-2017-wnt]

**Wnt ligand biogenesis:**
- Wnt proteins are palmitoylated at two conserved cysteines by Porcupine (PORCN) O-acyltransferase in the ER → lipid modification required for Frizzled binding and secretion
- Wntless (WLS) chaperone transports lipid-Wnt from ER through Golgi to cell surface → secretion into extracellular matrix; heparan sulfate proteoglycans (HSPG) facilitate diffusion gradients

**LRP5/6 phosphorylation — the ON switch:**
Wnt binding → Frizzled clusters LRP5/6 → LRP5/6 PPXY/PPPSP motifs phosphorylated by CK1γ and GSK-3β → phospho-LRP5/6 recruits Axin directly → pulls Axin out of destruction complex → complex disintegrates → β-catenin phosphorylation ceases → accumulated β-catenin translocates to nucleus

**Nuclear β-catenin activity:**
β-catenin binds TCF7L2 (TCF4, the dominant transcriptional TCF in intestine) → displaces Groucho/TLE repressor → recruits BCL9/Pygo → recruits Mediator and SWI/SNF → chromatin remodeling at Wnt target gene enhancers → MYC, CCND1, LGR5, AXIN2, EPHB2 activation

### Therapeutic targeting of Wnt signaling

Direct Wnt pathway inhibition has been challenging due to the pathway's essential role in normal stem cell biology:

**Porcupine (PORCN) inhibitors:** Block Wnt palmitoylation → prevent Wnt secretion → reduce autocrine/paracrine Wnt signaling:
- WNT974 (LGK-974, Novartis): Phase I in Wnt-addicted cancers, pancreatic cancer
- ETC-159 (PORCN inhibitor): Phase I/II in desmoid tumors (CTNNB1 mutant); significant activity in CTNNB1-mutant HCC
- Limitation: bone toxicity (inhibits osteoblast Wnt) — dose-limiting in trials

**Tankyrase inhibitors:** Tankyrase (TNKS1/2) poly-ADP-ribosylates Axin → ubiquitination → degradation → reduced destruction complex → elevated β-catenin; Tankyrase inhibitors (XAV939, G007-LK) stabilize Axin → restore destruction complex → reduce β-catenin
- Limited clinical development due to GI toxicity (intestinal Wnt dependence)

**CTNNB1-targeted therapies:** Small molecules targeting β-catenin/TCF interface (PKF115-584, iCRT14) or β-catenin/CBP interface (ICG-001/CWP232291) → disrupt transcriptional co-activation; PRI-724 (CBP/β-catenin inhibitor): Phase II AML (modest activity)

**Indirect approaches:**
- **Sulindac (NSAID):** Reduces polyp burden in FAP; mechanism partly via PGE2/EP2/β-catenin inhibition; not anti-cancer curative but effective as chemoprevention
- **Celecoxib (COX-2 inhibitor):** Also reduces FAP polyp burden; FDA-approved as adjunct to surveillance in FAP

## Connections

- `modulates` → **[Large Intestine](../../06-organ/large-intestine/README.md)** — Wnt/β-catenin is the master regulator of intestinal crypt stem cell self-renewal; APC mutation constitutively activates β-catenin and initiates the adenoma-carcinoma sequence in >80% of colorectal cancers.
- `connects-to` → **[KRAS](../kras/README.md)** — Wnt and KRAS mutations cooperate in CRC: Wnt drives stem cell identity (step 1), KRAS drives proliferation (step 2); combined inhibition is synergistic in CRC preclinical models.
- `connects-to` → **[TGF-β](../tgf-beta/README.md)** — TGF-β and Wnt pathways have context-dependent crosstalk; SMAD4 loss in late-stage CRC removes TGF-β-mediated repression of Wnt target genes → accelerated Wnt-driven invasion and metastasis.
- `modulates` → **[Fibroblast](../../04-cellular/fibroblast/README.md)** — Wnt signals activate stromal fibroblasts to myofibroblasts → desmoplasia; CAF-secreted Wnt ligands feed back onto tumor cells; Wnt-driven stromal activation promotes immune exclusion in CRC and PDAC.

[^clevers-2006-wnt]: Clevers H. Wnt/beta-catenin signaling in development and disease. *Cell.* 2006;127(3):469-480. [doi:10.1016/j.cell.2006.10.018](https://doi.org/10.1016/j.cell.2006.10.018) · [PubMed 17081971](https://pubmed.ncbi.nlm.nih.gov/17081971/)
[^nusse-2017-wnt]: Nusse R, Clevers H. Wnt/β-Catenin Signaling, Disease, and Emerging Therapeutic Modalities. *Cell.* 2017;169(6):985-999. [doi:10.1016/j.cell.2017.05.016](https://doi.org/10.1016/j.cell.2017.05.016) · [PubMed 28575679](https://pubmed.ncbi.nlm.nih.gov/28575679/)
[^fearon-1990-apc]: Fearon ER, Vogelstein B. A genetic model for colorectal tumorigenesis. *Cell.* 1990;61(5):759-767. [doi:10.1016/0092-8674(90)90186-I](https://doi.org/10.1016/0092-8674(90)90186-I) · [PubMed 2188735](https://pubmed.ncbi.nlm.nih.gov/2188735/)
