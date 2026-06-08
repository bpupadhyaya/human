---
schema: human-scale-entry/v1
id: irf3
name: IRF3
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-08
summary: "IRF3 (interferon regulatory factor 3) is activated by TBK1/IKKε (downstream of MAVS or STING) → C-terminal Ser396/398/402/405 phosphorylation → IRF3 homodimerization → nuclear translocation → IFN-β enhanceosome (IRF3 + NF-κB + AP-1); HCV NS5A and picornavirus 3C inhibit IRF3."
aliases: ["IRF3", "interferon regulatory factor 3", "IFN-beta transcription factor", "TBK1-IRF3 axis", "IRF3 phosphorylation", "IFN-beta enhanceosome", "PRDI-III", "innate transcription factor"]
sources:
  - id: fitzgerald-2003-tbk1-irf3
    type: peer-reviewed
    cite: "Fitzgerald KA, McWhirter SM, Faia KL, et al. IKKε and TBK1 are essential components of the IRF-3 signaling pathway. Nat Immunol. 2003;4(5):491-496."
    doi: "10.1038/ni921"
    pmid: "12692549"
    url: "https://doi.org/10.1038/ni921"
    accessed: "2026-06-08"
  - id: lin-1998-irf3-phosphorylation
    type: peer-reviewed
    cite: "Lin R, Heylbroeck C, Pitha PM, Hiscott J. Virus-dependent phosphorylation of the IRF-3 transcription factor regulates nuclear translocation, transactivation potential, and proteasome-mediated degradation. Mol Cell Biol. 1998;18(5):2986-2996."
    doi: "10.1128/MCB.18.5.2986"
    pmid: "9566918"
    url: "https://doi.org/10.1128/MCB.18.5.2986"
    accessed: "2026-06-08"
cross_links:
  - target: 01-human/03-molecular/mavs
    relation: connects-to
    note: "MAVS filament → TRAF3 → TBK1/IKKε → IRF3 C-terminal phosphorylation (Ser396, Ser398, Ser402) → IRF3 homodimerization → nuclear translocation → IFN-β; HCV NS3/4A cleaves MAVS → IRF3 not activated → viral chronicity; MAVS-TBK1-IRF3 is the antiviral RNA sensing axis."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "cGAS → cGAMP → STING → TBK1 → IRF3 Ser396 phosphorylation → IRF3 dimerization → nuclear import → IFN-β promoter binding; STING Golgi trafficking positions TBK1 to phosphorylate IRF3; IRF3 is the shared transcription factor endpoint of both MAVS and cGAS-STING innate sensing."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "IRF3 is the master transcription factor for IFN-β: phospho-IRF3 dimers bind PRDI/III elements on the IFN-β promoter; IRF3 + NF-κB (p65/p50) + AP-1 (ATF-2/c-Jun) form the IFN-β enhanceosome; IRF7 (induced by IFN-β autocrine feedback) amplifies IFN-α in the second wave response."
  - target: 01-human/07-system/hepatitis-c
    relation: connects-to
    note: "HCV NS3/4A cleaves MAVS → TBK1-IRF3 not activated; NS5A blocks TBK1 directly; selective IRF3 inactivation with preserved NF-κB → pro-survival hepatocyte signals persist; IRF3 pathway suppression is the dominant mechanism of HCV immune evasion and chronicity."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "IFN-β enhanceosome: IRF3 (PRDI/PRDIII) + NF-κB (PRDII) + AP-1 (PRDIV) cooperatively bind the IFN-β promoter; CBP/p300 bridges all three → histone acetylation; NF-κB co-activation is required for maximal IRF3-driven IFN-β transcription."
---

# IRF3

## Overview

**IRF3** (interferon regulatory factor 3) is the **principal transcription factor** that translates innate pathogen detection into IFN-β gene transcription. Unlike most of the nine IRF family members (IRF1-9), IRF3 is constitutively expressed in virtually all cell types, maintained in an inactive cytoplasmic form, and activated exclusively through phosphorylation by the innate kinase **TBK1** (TANK-binding kinase 1) or the related kinase **IKKε** — making it the dedicated transcriptional arm of both the **MAVS** (RNA sensing) and **cGAS-STING** (DNA sensing) innate immunity pathways.

Identified by Hiscott and colleagues in the late 1990s [^lin-1998-irf3-phosphorylation], IRF3's central role was confirmed when Fitzgerald et al. showed that TBK1 and IKKε were essential for IRF3 activation and IFN-β induction [^fitzgerald-2003-tbk1-irf3]. IRF3 is now recognized as the **convergence point** of most antiviral innate sensing pathways: diverse sensors (RIG-I, MDA5, cGAS, TLR3, TLR4 endosomal TRIF pathway) all ultimately activate TBK1 → IRF3.

**Clinical significance:** IRF3 is a prime target of viral immune evasion. HCV NS3/4A protease indirectly suppresses IRF3 by cleaving its upstream adapter MAVS; HCV NS5A additionally inhibits TBK1. Picornavirus 3Cpro and SARS-CoV-2 NSP13 directly target TBK1 or IRF3. These evasion mechanisms convert what should be an acute, self-limited infection into a chronic state — making IRF3 pathway restoration a therapeutic target.

## Structure

### IRF3 protein (427 aa, ~47 kDa)

IRF3 is the prototypical inhibited IRF:

- **DNA-binding domain (DBD, 1–113)**: Helix-turn-helix structure with a tryptophan cluster; recognizes ISRE-related sequences (PRDI/III on IFN-β promoter); in resting cells, DBD is locked against the regulatory domain (autoinhibited)
- **Linker region (113–197)**: Connects DBD to CC2-domain
- **CC2-domain (197–240)**: Coiled-coil; contributes to dimerization surface after activation; contains regulatory interactions with importin-α (nuclear import)
- **IRF association domain (IAD, 240–380)**: Mediates homo- and heterodimerization; autoinhibitory contacts with DBD in resting state; the core activation platform
- **Signal-responsive domain (SRD, 380–427)**: C-terminal regulatory region; contains the **serine cluster** (Ser396, Ser398, Ser402, Ser404, Ser405) phosphorylated by TBK1/IKKε; phosphorylation releases autoinhibitory contacts → allows IAD dimerization

**Activation model:**
- Resting IRF3: IAD contacts DBD → autoinhibited monomers
- TBK1 phosphorylates Ser396 → conformational change → exposes IAD dimerization surface
- Full activation requires phosphorylation at multiple serines → CBP/p300 binding → transactivation

### TBK1 (TANK-binding kinase 1, 729 aa)

TBK1 is the dedicated IRF3 kinase:
- Kinase domain (KD), ubiquitin-like domain (ULD), scaffold/dimerization domain (SDD)
- Activated by TRAF3 K63-polyubiquitin scaffolding after MAVS or STING signaling
- Trans-autophosphorylation (Ser172) → activation; then phosphorylates IRF3
- IKKε is the inducible TBK1 paralog (expressed after IFN stimulation)

### The IFN-β enhanceosome

The IFN-β promoter integrates three transcription factor signals:
- **PRDI/III** (positions −77 to −65, −95 to −85): Binds IRF3 dimer (and IRF7 in secondary response)
- **PRDII** (positions −77 to −65): Binds NF-κB (p65/p50)
- **PRDIV** (positions −102 to −91): Binds AP-1 (ATF-2/c-Jun)
- **CBP/p300** histone acetyltransferase: Recruited by all three → H3K27ac at IFN-β locus → transcription initiation

## Function

1. **Primary IFN-β induction**: IRF3 drives immediate-early IFN-β transcription (within 1–2 h of infection) in nearly all cell types; critical for autocrine and paracrine antiviral defense before adaptive immunity
2. **IRF7 amplification**: IFN-β → IFNAR → ISGF3 → IRF7 (ISG) → IRF7 phosphorylated by TBK1 → IRF3/IRF7 heterodimers → amplified IFN-α production (14 subtypes); plasmacytoid DCs constitutively express high IRF7 → rapid massive IFN-α secretion
3. **CXCL10 and CCL5 induction**: IRF3 directly drives CXCL10 (IP-10) and CCL5 (RANTES) chemokine expression → NK cell and T cell recruitment; IRF3 contributes to adaptive immune priming
4. **Apoptosis**: Activated IRF3 can interact with the pro-apoptotic protein Bax → mitochondrial apoptosis pathway in infected cells; ensures elimination of viral factories
5. **NF-κB coordination**: IRF3 and NF-κB are co-activated by MAVS and STING signaling → form the enhanceosome; IRF3 biases toward IFN production, NF-κB biases toward cytokine inflammation; the ratio determines antiviral vs. inflammatory outcome

## Mechanism

### MAVS → TBK1 → IRF3

1. Viral RNA → RIG-I/MDA5 activation → MAVS prion-like filament formation on OMM
2. MAVS filament recruits **TRAF3** via TRAF-binding motifs → TRAF3 K63-ubiquitin chain scaffolding
3. K63-Ub recruits **TBK1/IKKε** → TBK1 trans-autophosphorylation (Ser172)
4. Active TBK1 phosphorylates **IRF3** at Ser396 (primary) → additional phosphorylation at Ser398/402/405 → conformational change exposing IAD surface
5. IRF3 homodimerizes (or IRF3/IRF7 heterodimerizes) → binds importin-α → nuclear import
6. Dimer binds **PRDI/III** on IFN-β promoter → recruits CBP/p300 → IFN-β transcription
7. **MAVS dephosphorylation**: PP2A phosphatase dephosphorylates IRF3 after translocation → cytoplasmic pool recycled

### cGAS-STING → TBK1 → IRF3

1. Cytosolic dsDNA → cGAS → 2′3′-cGAMP → STING activation → ER exit
2. STING-TBK1 complex traffics through ERGIC → Golgi; STING CTT recruits IRF3 and TBK1 simultaneously
3. TBK1 trans-autophosphorylation on STING scaffold → phosphorylates IRF3 → same pathway as MAVS
4. STING is subsequently palmitoylated (Golgi) and eventually ubiquitinated → degradation terminates signaling

### Viral IRF3 evasion

| Virus | Strategy | Mechanism |
|-------|----------|-----------|
| HCV | Upstream MAVS cleavage | NS3/4A cleaves MAVS Cys508; NS5A blocks TBK1 |
| Influenza | Upstream RIG-I block | NS1 sequesters dsRNA + blocks TRIM25 |
| SARS-CoV-2 | TBK1 disruption | NSP13 (helicase) inhibits TBK1 autophosphorylation |
| Picornaviruses | IRF3 direct cleavage | 3Cpro cleaves IRF3; L-protein cleaves IRF3 |
| KSHV | IRF3 decoy | vIRF-2 (viral IRF homolog) competes with IRF3 for DNA binding |
| Vaccinia virus | IRF3 block | E3L dsRNA-binding protein blocks RIG-I/TLR3 activation |
| Adenovirus | IRF3 block | E1A protein suppresses IRF3 transactivation |

### IRF3 termination

- **Ubiquitin-proteasomal degradation**: Activated (pSer396) IRF3 is K48-ubiquitinated by RBCC-containing protein RAUL/UBR5 → proteasomal degradation (signal termination ~6–12 h after activation)
- **Pin1 and CHIP**: Prolyl isomerase Pin1 targets Ser339 phospho-IRF3 for proteasomal degradation; CHIP E3 ligase degrades misfolded IRF3
- **Autophagy**: p62/SQSTM1 sequesters IRF3 aggregates for autophagic degradation

## Connections

**→ [MAVS](../mavs/)**: MAVS filament → TRAF3 → TBK1/IKKε → IRF3 C-terminal phosphorylation (Ser396, Ser398, Ser402) → IRF3 homodimerization → nuclear translocation → IFN-β; HCV NS3/4A cleaves MAVS → IRF3 not activated → viral chronicity; MAVS-TBK1-IRF3 is the antiviral RNA sensing axis.

**→ [cGAS-STING](../cgas-sting/)**: cGAS → cGAMP → STING → TBK1 → IRF3 Ser396 phosphorylation → IRF3 dimerization → nuclear import → IFN-β promoter binding; STING Golgi trafficking positions TBK1 to phosphorylate IRF3; IRF3 is the shared transcription factor endpoint of both MAVS and cGAS-STING innate sensing.

**→ [Type I Interferon](../type-i-interferon/)**: IRF3 is the master transcription factor for IFN-β: phospho-IRF3 dimers bind PRDI/III elements on the IFN-β promoter; IRF3 + NF-κB (p65/p50) + AP-1 (ATF-2/c-Jun) form the IFN-β enhanceosome; IRF7 (induced by IFN-β autocrine feedback) amplifies IFN-α in the second wave response.

**→ [Hepatitis C](../../../07-system/hepatitis-c/)**: HCV NS3/4A protease cleaves MAVS → TBK1-IRF3 not activated; HCV NS5A blocks TBK1 activity directly; net result: selective IRF3 inactivation with preserved NF-κB → pro-survival signals persist; IRF3 pathway suppression is the dominant mechanism of HCV immune evasion and chronicity.

**→ [NF-κB](../nf-kb/)**: IFN-β enhanceosome requires cooperative assembly of IRF3 + NF-κB + AP-1 on the IFN-β promoter; IRF3 occupies PRDI/PRDIII, NF-κB occupies PRDII, AP-1 occupies PRDIV; CBP/p300 is recruited to acetylate histones; NF-κB co-activation is required for maximal IRF3-driven IFN-β transcription.
