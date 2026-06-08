---
schema: human-scale-entry/v1
id: mavs
name: MAVS
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-08
summary: "MAVS (mitochondrial antiviral signaling protein; VISA/IPS-1/CARDIF) is the central adaptor for RIG-I and MDA5 RNA virus sensing: 5′ppp/dsRNA → RIG-I/MDA5 → MAVS CARD-CARD interaction → filamentous MAVS aggregation → TBK1/IKKε → IRF3 → IFN-β + NF-κB; HCV NS3/4A cleaves MAVS."
aliases: ["MAVS", "IPS-1", "VISA", "CARDIF", "mitochondrial antiviral signaling protein", "RIG-I signaling", "MDA5 pathway", "MAVS signaling", "RIG-I/MDA5", "innate RNA sensing", "antiviral CARD adaptor"]
sources:
  - id: seth-2005-mavs-discovery
    type: peer-reviewed
    cite: "Seth RB, Sun L, Ea CK, Chen ZJ. Identification and characterization of MAVS, a mitochondrial antiviral signaling protein that activates NF-κB and IRF3. Cell. 2005;122(5):669-682."
    doi: "10.1016/j.cell.2005.08.012"
    pmid: "16125763"
    url: "https://doi.org/10.1016/j.cell.2005.08.012"
    accessed: "2026-06-08"
  - id: kell-2015-rig-i-review
    type: peer-reviewed
    cite: "Kell AM, Gale M Jr. RIG-I in RNA virus recognition. Virology. 2015;479-480:110-121."
    doi: "10.1016/j.virol.2015.02.017"
    pmid: "25749629"
    url: "https://doi.org/10.1016/j.virol.2015.02.017"
    accessed: "2026-06-08"
cross_links:
  - target: 01-human/07-system/dengue-fever
    relation: connects-to
    note: "Dengue virus RNA is sensed by RIG-I and MDA5 → MAVS → TBK1/IRF3 → IFN-β; DENV NS4B and NS2B/3 protease cleave MAVS to evade innate immunity; NS5 targets STAT2 for proteasomal degradation downstream of IFN signaling; strong early IFN-β correlates with mild dengue outcome."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "MAVS is the central adaptor linking cytosolic RNA sensing (RIG-I/MDA5) to type I IFN production: 5′ppp-dsRNA → RIG-I CARDs exposed → binds MAVS TM domain → MAVS prion-like filament propagation → TRAF3/TBK1 → IRF3/IRF7 → IFN-α/β; MAVS acts on outer mitochondrial membrane."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "MAVS (RNA sensing) and cGAS-STING (DNA sensing) are the two major parallel innate sensing axes converging on TBK1-IRF3-IFN-β; both are targeted by the same viral immune evasion proteases (flavivirus NS3, HCV NS3/4A); MAVS-STING co-signaling occurs during DNA virus infections."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "MAVS activates NF-κB in parallel with IRF3: MAVS → TRAF6 → TAK1 → IKKβ → IκBα degradation → NF-κB → TNF-α, IL-6, and inflammatory gene expression; NF-κB activation by MAVS is important for the pro-inflammatory arm of antiviral innate immunity distinct from IFN production."
  - target: 01-human/07-system/influenza
    relation: connects-to
    note: "Influenza 5′ppp ssRNA activates RIG-I → TRIM25 → MAVS → TBK1/IRF3 → IFN-β; NS1 blocks TRIM25-mediated RIG-I ubiquitination and sequesters dsRNA → impairs MAVS activation; RIG-I/MAVS is the primary innate sensor for influenza A in respiratory epithelium."
  - target: 01-human/03-molecular/irf3
    relation: connects-to
    note: "MAVS filament → TRAF3 → TBK1/IKKε → IRF3 C-terminal phosphorylation → homodimerization → nuclear translocation → IFN-β; HCV NS3/4A cleaves MAVS → IRF3 not activated → chronicity; MAVS-TBK1-IRF3 is the canonical antiviral RNA sensing axis."
  - target: 01-human/07-system/hepatitis-c
    relation: connects-to
    note: "HCV NS3/4A cleaves MAVS at Cys508 → soluble MAVS cannot activate TBK1/IRF3; NS3/4A also cleaves TRIF → TLR3 signaling blocked; dual evasion of cytosolic and endosomal RNA sensing; MAVS cleavage is the paradigmatic mechanism by which an RNA virus establishes chronicity."
  - target: 01-human/03-molecular/rig-i
    relation: connects-to
    note: "RIG-I CARD domains (K63-ubiquitinated by TRIM25 at Lys172) bind MAVS CARD → nucleate MAVS prion-like filament on outer mitochondrial membrane → TRAF3 → TBK1 → IRF3 → IFN-β; MAVS is the essential downstream adaptor: all RIG-I and MDA5 signaling requires MAVS."
  - target: 01-human/07-system/zika-virus
    relation: connects-to
    note: "ZIKV dsRNA replication intermediates activate RIG-I/MDA5 → MAVS → TBK1/IRF3 → IFN-β; fetal neural progenitor cells have reduced RIG-I/MAVS → impaired IFN-β → ZIKV amplifies unchecked in fetal brain; MAVS is required for adult innate control limiting ZIKV viremia."
---

# MAVS

## Overview

**MAVS** (mitochondrial antiviral signaling protein; also known as IPS-1, VISA, and CARDIF — named by four independent groups who discovered it simultaneously in 2005) is the critical **adaptor protein** that bridges **cytosolic RNA sensing** to innate immune activation. Identified by Chen and colleagues at UT Southwestern in 2005 [^seth-2005-mavs-discovery], MAVS sits on the **outer mitochondrial membrane** and transmits signals from the RNA helicases RIG-I and MDA5 to downstream kinases (TBK1/IKKε) and transcription factors (IRF3, NF-κB) that drive type I interferon production.

MAVS is remarkable for its **prion-like self-polymerization**: upon viral RNA sensing, activated RIG-I/MDA5 transfer an activating signal to a single MAVS molecule → MAVS forms amyloid-like filaments on the mitochondrial surface → filamentous MAVS recruits TRAF3/TBK1 → IRF3 phosphorylation/dimerization → **IFN-β production**. This self-amplifying aggregation mechanism ensures rapid, irreversible commitment to an antiviral state.

**Clinical significance:** MAVS cleavage is a central immune evasion strategy of RNA viruses: HCV NS3/4A protease cleaves MAVS at Cys508 — releasing it from the mitochondria and disabling IFN induction — a mechanism directly responsible for HCV's ability to establish chronic infection.

## Structure

### RIG-I (DDX58, ~106 kDa)

The primary upstream activator for short dsRNA and 5′-triphosphate (5′ppp) RNA:

- **N-terminal CARD domains** (×2): Autoinhibited by C-terminal domain; exposed after RNA binding; bind MAVS CARD
- **DExD/H-box helicase domain**: ATP-dependent dsRNA unwinding; translocates along dsRNA
- **C-terminal regulatory domain (CTD)**: Ligand-binding; detects 5′-triphosphate and blunt-ended dsRNA (≥8 bp)
- **Activation**: Poly-ubiquitination of CARD domains by TRIM25 (K63-linked) → conformational opening → MAVS binding
- **Key ligands**: Influenza RNA, Sendai virus, SARS-CoV-2 defective-interfering particles, in vitro transcribed RNA with 5′ppp

### MDA5 (IFIH1, ~135 kDa)

Primary sensor for long dsRNA (>1 kb):

- **CARD domains** (×2): Bind MAVS CARD
- **Helicase domain**: Assembles cooperatively along long dsRNA; forms filamentous oligomers
- **CTD**: Less selective for 5′ppp than RIG-I; binds internal dsRNA structure
- **Key ligands**: Picornaviruses (EMCV, poliovirus), MRE (reovirus), synthetic poly(I:C) long, AGS-causing self-dsRNA (Alu elements in ADAR1 deficiency)

### MAVS protein (540 aa)

- **N-terminal CARD** (aa 1-100): Homotypic binding to RIG-I/MDA5 CARDs
- **Proline-rich region** (aa 100-400): Scaffold for TRAF2/TRAF3/TRAF6 binding
- **Transmembrane domain** (aa 514-535): Anchors MAVS to **outer mitochondrial membrane (OMM)**; critical for signaling (cytosolic MAVS is non-functional)
- **HCV NS3/4A cleavage site**: Cys508 — cleavage releases MAVS from OMM → disables signaling

## Function

1. **Antiviral IFN induction**: RIG-I or MDA5 senses viral RNA → binds MAVS CARD → MAVS filament formation → TRAF3 → TBK1 → IRF3-Ser396 phosphorylation → IRF3 dimerization → nuclear translocation → IFN-β (and ISGs: MX1, OAS1, PKR, IFIT1)
2. **Inflammatory cytokine induction**: MAVS → TRAF6 → TAK1 → IKKβ → NF-κB → TNF-α, IL-6, IL-12 (parallel to IRF3 arm)
3. **Apoptosis regulation**: MAVS → caspase-8 → apoptosis in virally infected cells; regulated by FADD and RIPK1
4. **Mitochondrial and peroxisomal localization**: MAVS exists on mitochondria AND peroxisomes; peroxisomal MAVS generates rapid but transient IFN-β; mitochondrial MAVS generates sustained IFN responses
5. **Cross-talk with cGAS-STING**: During DNA virus infection, cGAS-STING and MAVS can synergize; MAVS also localizes to mitochondria-associated membranes (MAM) in proximity to ER-resident STING

## Mechanism

### MAVS prion-like signaling

1. Viral RNA → RIG-I (5′ppp dsRNA) or MDA5 (long dsRNA) binding
2. Helicase conformational change → CARD domains exposed
3. TRIM25 K63-ubiquitination of RIG-I CARD → binds unanchored K63 polyubiquitin chains
4. RIG-I/MDA5 CARD-CARD interaction with monomeric MAVS on OMM
5. **Seed-template propagation**: Activated MAVS monomer nucleates filament growth — new MAVS monomers adopt the activated conformation along the mitochondrial surface
6. Filamentous MAVS recruits **TRAF3** → TBK1/IKKε oligomerization → trans-autophosphorylation → IRF3-Ser396 phosphorylation
7. IRF3 homodimerization → nuclear import → IFN-β gene transcription (IFN-β enhanceosome: IRF3 + NF-κB + AP-1)

### Viral cleavage of MAVS

- **HCV NS3/4A**: Cleaves Cys508 in MAVS TM anchor → soluble cytosolic MAVS unable to signal; mechanism of HCV persistence
- **Picornavirus 3Cpro**: Cleaves MAVS; enteroviruses use this to block IFN production
- **Dengue/Zika NS2B/NS3**: Proposed to cleave MAVS or disrupt MAVS-STING interactions
- **SARS-CoV-2**: Multiple IFN evasion mechanisms converge on MAVS-TBK1 axis (NSP6 sequesters MAVS, NSP13 disrupts TBK1)

### Regulation

- **Negative regulation**: NLRX1 (mitochondrial NLR protein) inhibits MAVS by competing for RIG-I binding; PCBP2 and AIP4 ubiquitinate MAVS (K48-linked) for proteasomal degradation after antiviral activation
- **Autophagy**: CALCOCO2 (NDP52) and optineurin recruit autophagy machinery to mitochondria → mitophagy of MAVS-containing OMM → signal termination

## Connections

**→ [Dengue Fever](../../../07-system/dengue-fever/)**: Dengue virus RNA is sensed by RIG-I and MDA5 → MAVS → TBK1/IRF3 → IFN-β; DENV NS4B and NS2B/3 protease cleave MAVS to evade innate immunity; NS5 targets STAT2 for proteasomal degradation downstream of IFN signaling; strong early IFN-β correlates with mild dengue outcome.

**→ [Type I Interferon](../type-i-interferon/)**: MAVS is the central adaptor linking cytosolic RNA sensing (RIG-I/MDA5) to type I IFN production: 5′ppp-dsRNA → RIG-I CARDs exposed → binds MAVS TM domain → MAVS prion-like filament propagation → TRAF3/TBK1 → IRF3/IRF7 → IFN-α/β; MAVS acts on outer mitochondrial membrane.

**→ [cGAS-STING](../cgas-sting/)**: MAVS (RNA sensing) and cGAS-STING (DNA sensing) are the two major parallel innate sensing axes converging on TBK1-IRF3-IFN-β; both are targeted by the same viral immune evasion proteases (flavivirus NS3, HCV NS3/4A); MAVS-STING co-signaling occurs during DNA virus infections.

**→ [NF-κB](../nf-kb/)**: MAVS activates NF-κB in parallel with IRF3: MAVS → TRAF6 → TAK1 → IKKβ → IκBα degradation → NF-κB → TNF-α, IL-6, and inflammatory gene expression; NF-κB activation by MAVS is important for the pro-inflammatory arm of antiviral innate immunity distinct from IFN production.

**→ [Influenza](../../../07-system/influenza/)**: Influenza 5′ppp ssRNA activates RIG-I → TRIM25 → MAVS → TBK1/IRF3 → IFN-β; NS1 blocks TRIM25-mediated RIG-I ubiquitination and sequesters dsRNA → impairs MAVS activation; RIG-I/MAVS is the primary innate sensor for influenza A in respiratory epithelium.

**→ [IRF3](../irf3/)**: MAVS filament → TRAF3 → TBK1/IKKε → IRF3 C-terminal phosphorylation → homodimerization → nuclear translocation → IFN-β; HCV NS3/4A cleaves MAVS → IRF3 not activated → chronicity; MAVS-TBK1-IRF3 is the canonical antiviral RNA sensing axis.

**→ [Hepatitis C](../../../07-system/hepatitis-c/)**: HCV NS3/4A serine protease cleaves MAVS at Cys508 → soluble cytoplasmic MAVS cannot activate TBK1/IRF3; NS3/4A also cleaves TRIF; dual evasion of cytosolic and endosomal RNA sensing; MAVS cleavage by HCV is the paradigmatic example of viral innate immune subversion for chronicity.
