---
schema: human-scale-entry/v1
id: androgen-receptor
name: Androgen Receptor
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-06
summary: "Nuclear receptor activated by testosterone and DHT; ligand binding → nuclear translocation → androgen response elements → PSA and TMPRSS2 induction. Amplified and mutated in castration-resistant prostate cancer; enzalutamide, apalutamide, and abiraterone target the AR pathway."
aliases: ["AR", "NR3C4", "nuclear androgen receptor", "AR signaling", "AR-V7", "androgen receptor splice variant"]
sources:
  - id: beer-2014-prevail
    type: peer-reviewed
    cite: "Beer TM, Armstrong AJ, Rathkopf D, et al. Enzalutamide in metastatic prostate cancer before chemotherapy. N Engl J Med. 2014;371(5):424-433."
    doi: "10.1056/NEJMoa1405095"
    pmid: "24881730"
    url: "https://doi.org/10.1056/NEJMoa1405095"
  - id: ryan-2013-cougar302
    type: peer-reviewed
    cite: "Ryan CJ, Smith MR, de Bono JS, et al. Abiraterone in metastatic prostate cancer without previous chemotherapy. N Engl J Med. 2013;368(2):138-148."
    doi: "10.1056/NEJMoa1209096"
    pmid: "23228172"
    url: "https://doi.org/10.1056/NEJMoa1209096"
cross_links:
  - target: 01-human/03-molecular/pten
    relation: connects-to
    note: "PTEN loss occurs in ~50% of prostate cancer → AKT-mTOR activation and AR crosstalk; PTEN-null tumors upregulate AR target genes via AKT-FOXO; co-loss of PTEN and RB1 drives neuroendocrine differentiation; ipatasertib + abiraterone is approved for PTEN-null mCRPC."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "AR signaling drives mTORC1 via AKT; mTOR inhibitors showed limited activity in CRPC alone; mTORC2 phosphorylates AKT-S473 → AR nuclear translocation; dual PI3K-mTOR inhibition under study for PTEN-null CRPC with enzalutamide or abiraterone."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "IL-6 activates AR in a ligand-independent manner in CRPC via JAK-STAT3 → nuclear AR translocation; elevated serum IL-6 correlates with CRPC progression and poor prognosis; IL-6 drives EMT and immune suppression in the prostate tumor microenvironment."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "AKT is constitutively activated by PTEN loss in prostate cancer → AR phosphorylation → nuclear localization and ligand-independent AR activity in CRPC; ipatasertib and capivasertib (AKT inhibitors) show activity in PTEN-null mCRPC combined with abiraterone."
---

# Androgen Receptor

## Overview

The **androgen receptor (AR, NR3C4)** is a ligand-activated nuclear transcription factor of the steroid hormone receptor superfamily. In normal physiology, AR mediates the effects of **testosterone** and its more potent derivative **5α-dihydrotestosterone (DHT)** in driving prostate development, spermatogenesis, muscle anabolism, and bone density. In prostate cancer (PCa), AR is the central oncogenic driver across all disease stages — from hormone-sensitive disease (CSPC) through castration-resistant prostate cancer (CRPC), where AR remains active despite castrate testosterone levels [^beer-2014-prevail].

AR is one of the most validated and successfully drugged targets in oncology: androgen deprivation therapy (ADT, medical or surgical castration) has been a mainstay of advanced PCa treatment since 1941 (Huggins and Hodges). Modern next-generation AR-pathway inhibitors — abiraterone, enzalutamide, apalutamide, and darolutamide — extend survival in both hormone-sensitive and castration-resistant disease [^ryan-2013-cougar302].

**AR in normal tissues:**
- **Prostate:** AR drives PSA (KLK3), TMPRSS2, NKX3-1, FKBP5, and hundreds of luminal differentiation genes; normal prostate luminal cells require AR for survival (AR-dependent luminal epithelium)
- **Bone:** AR promotes osteoblast function and restrains osteoclastogenesis; androgen deficiency → accelerated bone loss (a key ADT side effect)
- **Muscle:** AR drives myogenesis (anabolic effects); AR loss → sarcopenia with ADT
- **Hematopoiesis:** AR promotes erythropoiesis; ADT → anemia in some patients

## Structure

### AR domain architecture

AR is a 919-amino-acid protein with four functional domains:

**N-terminal domain (NTD, residues 1-555, ~58 kDa):**
- Largest and most structurally disordered AR domain; intrinsically unstructured (IDR) that folds on coactivator binding
- Contains the **activation function 1 (AF-1)** — the major transcriptional activation domain; AF-1 activity is ligand-independent (unlike AF-2 in the LBD) → key reason AR-V7 (which lacks the LBD) remains transcriptionally active
- **N/C interaction:** AF-1 contains the FQNLF motif that interacts with AF-2 in the LBD → intramolecular interaction that stabilizes ligand-bound AR and protects the LBD from antagonist; this N/C interaction is disrupted by enzalutamide but not directly blocked
- Polyglutamine (polyQ) repeat (18-22 Qs in wild-type): longer repeats → weaker AR activity; expansion of polyQ (Kennedy disease / spinal and bulbar muscular atrophy) → AR loss-of-function and motor neuron disease; shorter repeats → higher AR activity → increased PCa risk (modest effect)

**DNA-binding domain (DBD, residues 556-623):**
- Two zinc fingers (C4-type): first zinc finger confers DNA specificity (P-box: CGSCKV → recognizes ARE half-sites); second zinc finger (D-box) mediates AR homodimerization at ARE
- ARE consensus: 5'-GnACAnnnTGTnCn-3' (two inverted half-sites separated by 3 bp); AR binds ARE as a homodimer
- DBD is highly conserved across steroid receptors; mutations rare in PCa (unlike LBD)

**Hinge region (residues 624-663):**
- Contains the nuclear localization signal (NLS) — bipartite NLS recognized by importin-alpha; hinge region also subject to acetylation (K630/632/633) and SUMOylation, which modulate AR activity; phosphorylation at T654 (by CDK5) impairs ligand-independent activity

**Ligand-binding domain (LBD, residues 664-919, ~25 kDa):**
- 12-helix bundle (H1-H12) forming the ligand-binding pocket; testosterone and DHT bind within the hydrophobic pocket; helix 12 (H12) closes over the LBD after agonist binding → stable closed conformation → AF-2 surface exposed → coactivator (LXXLL motif) binding → transcription
- **Antagonist mechanism:** Enzalutamide, bicalutamide bind the LBD pocket → H12 adopts open/"antagonist" conformation → AF-2 surface occluded → corepressor recruitment and reduced nuclear localization
- **CRPC LBD mutations:** F877L (enzalutamide resistance), T878A (converts anti-androgens to agonists), W742C/L (bicalutamide resistance); LBD point mutations broaden ligand promiscuity (glucocorticoids, progestins → AR agonists in CRPC)

### Androgen metabolism

**Testosterone biosynthesis and conversion:**
- Primary source: Leydig cells of the testes (~95% of circulating testosterone, regulated by LH from pituitary)
- Adrenal source (~5%): DHEA and androstenedione → peripheral conversion; this residual adrenal androgen drives CRPC in castrate patients → rationale for abiraterone (CYP17A1 inhibitor)
- **5α-reductase:** Converts testosterone → DHT in prostate (and scalp); DHT binds AR with ~3× higher affinity and dissociates more slowly than testosterone → stronger AR activation; type 2 5α-reductase is the dominant isoform in prostate; finasteride/dutasteride inhibit 5α-reductase → prevent DHT in prostate
- **Intratumoral androgen synthesis:** CRPC tumors express CYP17A1, AKR1C3, and HSD17B3 → de novo androgen synthesis from cholesterol and adrenal precursors within the tumor → autocrine/paracrine AR activation despite castrate serum testosterone

## Function

### AR transcriptional program in prostate cancer

**Classical AR activation pathway:**
1. Testosterone or DHT diffuses into the cell → binds LBD → conformational change (H12 closure)
2. Chaperone dissociation: HSP90 releases AR (HSP90 maintains unliganded AR in inactive cytoplasmic complex with HSP70, FKBP51, and p23)
3. AR homodimerization via DBD D-box interactions
4. Nuclear import via NLS-importin-alpha
5. ARE binding: AR dimer binds AREs → recruitment of coactivators (SRC-1/NCoA1, SRC-2/GRIP1, SRC-3/NCOA3, CBP/p300, MEDIATOR)
6. Chromatin remodeling → target gene transcription

**Key AR transcriptional targets in prostate:**
- **PSA (KLK3):** AR-driven serine protease; major clinical biomarker; PSA AREs are the canonical AR target sites used to validate AR activity; PSA promoter contains functional AREs at -170 bp and -394 bp
- **TMPRSS2:** Serine protease; AR-regulated; TMPRSS2-ERG fusion (~50% of PCa) places the ETS transcription factor ERG under AR control → ETS-driven invasion program
- **NKX3-1:** Homeobox transcription factor → luminal differentiation; AR-dependent luminal identity maintenance
- **CDK1/CDC2:** AR-driven mitosis genes → proliferation in CRPC; AR drives a proliferative transcriptional program in CRPC beyond luminal differentiation
- **FKBP5:** Cochaperone for HSP90-AR complex; FKBP5 expression is a reliable AR activity readout; glucocorticoid resistance mediated in part via FKBP5

### Non-genomic AR signaling

Beyond nuclear transcription, AR exerts rapid non-genomic effects:
- **Cytoplasmic AR-src kinase:** Testosterone → AR-SRC complex → MAPK activation within minutes (independent of nuclear AR)
- **PI3K/AKT:** AR can activate PI3K in a ligand-independent manner; this is reciprocal with PTEN loss effects
- **EGF receptor transactivation:** Liganded AR → EGFR → MEK-ERK → rapid proliferative signaling in CRPC

## Mechanism

### Castration-resistant mechanisms

CRPC develops in virtually all patients after prolonged ADT. Despite castrate testosterone levels (<50 ng/dL), AR remains transcriptionally active through multiple mechanisms:

**1. AR amplification (10-30% of CRPC):**
- AR gene on chromosome Xq11-12 is amplified → massively increased AR protein → low residual androgen (even castrate levels) saturates the abundant AR → transcription proceeds; AR amplification is the earliest CRPC resistance mechanism (detected in ~5-10% of pre-treatment tumors → 30% in CRPC)

**2. AR point mutations (10-20% of CRPC):**
- **T878A** (formerly T877A): Most common LBD mutation; found in patients treated with flutamide → promiscuous AR that is activated by flutamide (anti-androgen to agonist switch); also activated by progesterone and glucocorticoids
- **F877L:** Enzalutamide resistance mutation; converted enzalutamide from antagonist to partial agonist; less common (2-5%)
- **W742C/L:** Bicalutamide resistance; bicalutamide → agonist switch; rare with enzalutamide treatment
- **L702H:** Glucocorticoid-activatable AR mutation; found in abiraterone-treated patients; cortisol/dexamethasone → AR agonist via L702H

**3. AR-V7 splice variant (30-40% of enzalutamide/abiraterone-resistant CRPC):**
- AR-V7 (AR splice variant 7): Splices from exon 3 (DBD) to a cryptic exon CE3 in intron 3, generating a truncated AR containing NTD + DBD but **lacking the LBD and hinge region entirely**
- AR-V7 is constitutively nuclear (no LBD = no cytoplasmic retention by HSP90), constitutively active (AF-1 in NTD drives transcription without ligand), and **insensitive to all LBD-targeting agents** (enzalutamide, apalutamide, darolutamide, bicalutamide, abiraterone)
- AR-V7 detected in circulating tumor cells (CTC-based assays — Oncotype DX AR-V7 Nucleus Detect); AR-V7 positivity predicts resistance to AR-pathway therapy → taxane chemotherapy preferred; cabazitaxel superior to cabazitaxel in AR-V7-positive CRPC (CARD trial)
- **AR-V7 interacts with full-length AR** as heterodimer → dominant negative effect on full-length AR transcriptional specificity; AR-V7 also drives a distinct transcriptional program (proliferative but less differentiation-focused)

**4. Ligand-independent AR activation by other pathways:**
- **IL-6 → STAT3 → AR:** IL-6-STAT3 → AR nuclear translocation and phosphorylation at S727 → ligand-independent AR transcriptional activity; serum IL-6 elevated in CRPC and correlates with prognosis
- **EGF-EGFR → MAPK → AR:** EGF → SRC → AR phosphorylation at Y534 → nuclear AR; EGFR-AR bypass loop active in some CRPC
- **AKT → AR:** AKT phosphorylates AR at S213 and S790 → nuclear localization; PTEN loss → constitutive AKT → ligand-independent AR in CRPC; explains why PTEN-null tumors progress rapidly to CRPC
- **CDK5/CDK9 → AR:** CDK5 phosphorylates AR hinge at T654 → modulates activity; CDK9 phosphorylates AR-AF1 → enhanced coactivator recruitment; CDK9 inhibition reduces AR transcriptional output

**5. Adrenal/intratumoral androgen synthesis:**
- CRPC tumors express a full steroidogenic enzyme complement → synthesize androgens from cholesterol or adrenal DHEA/androstenedione intracellularly; abiraterone (CYP17A1 inhibitor) blocks this pathway; approved in both CRPC and mCSPC (with prednisone) [^ryan-2013-cougar302]

### AR-pathway inhibitors

| Agent | Mechanism | Indication | Key data |
|-------|-----------|-----------|----------|
| **Enzalutamide** | AR antagonist (LBD) + nuclear entry inhibitor | mCSPC, nmCRPC, mCRPC | PREVAIL: OS benefit pre-chemo CRPC; ARCHES: mCSPC |
| **Apalutamide** | AR antagonist (LBD) | nmCRPC, mCSPC | SPARTAN: nmCRPC MFS; TITAN: mCSPC OS |
| **Darolutamide** | AR antagonist (distinct binding mode, low CNS penetration) | nmCRPC, mCRPC | ARAMIS: nmCRPC; ARASENS: mCSPC + docetaxel |
| **Abiraterone** | CYP17A1 inhibitor (androgen synthesis) | mCSPC, mCRPC | COU-AA-301/302: CRPC; LATITUDE: mCSPC |
| **Bicalutamide** | AR antagonist (LBD, weak) | Localized, adjuvant | Largely superseded by novel AR agents |

## Connections

- `connects-to` → **[PTEN](../../03-molecular/pten/README.md)** — PTEN loss occurs in ~50% of prostate cancer → AKT-mTOR activation and AR crosstalk; PTEN-null tumors upregulate AR target genes via AKT-FOXO; co-loss of PTEN and RB1 drives neuroendocrine differentiation; ipatasertib + abiraterone is approved for PTEN-null mCRPC.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — AR signaling drives mTORC1 via AKT; mTOR inhibitors showed limited activity in CRPC alone; mTORC2 phosphorylates AKT-S473 → AR nuclear translocation; dual PI3K-mTOR inhibition under study for PTEN-null CRPC with enzalutamide or abiraterone.
- `connects-to` → **[IL-6](../../03-molecular/il-6/README.md)** — IL-6 activates AR in a ligand-independent manner in CRPC via JAK-STAT3 → nuclear AR translocation; elevated serum IL-6 correlates with CRPC progression and poor prognosis; IL-6 drives EMT and immune suppression in the prostate tumor microenvironment.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — AKT is constitutively activated by PTEN loss in prostate cancer → AR phosphorylation → nuclear localization and ligand-independent AR activity in CRPC; ipatasertib and capivasertib (AKT inhibitors) show activity in PTEN-null mCRPC combined with abiraterone.

[^beer-2014-prevail]: Beer TM, Armstrong AJ, Rathkopf D, et al. Enzalutamide in metastatic prostate cancer before chemotherapy. *N Engl J Med.* 2014;371(5):424-433. [doi:10.1056/NEJMoa1405095](https://doi.org/10.1056/NEJMoa1405095) · [PubMed 24881730](https://pubmed.ncbi.nlm.nih.gov/24881730/)
[^ryan-2013-cougar302]: Ryan CJ, Smith MR, de Bono JS, et al. Abiraterone in metastatic prostate cancer without previous chemotherapy. *N Engl J Med.* 2013;368(2):138-148. [doi:10.1056/NEJMoa1209096](https://doi.org/10.1056/NEJMoa1209096) · [PubMed 23228172](https://pubmed.ncbi.nlm.nih.gov/23228172/)
