---
schema: human-scale-entry/v1
id: stat1
name: STAT1
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-08
summary: "STAT1 transduces type I IFN (IFNAR → JAK1/TYK2 → STAT1/STAT2/IRF9 → ISGF3 → ISGs) and IFN-γ (IFNGR → JAK1/JAK2 → STAT1 homodimer → GAS → IRF1 → iNOS); STAT1 GOF mutations → chronic mucocutaneous candidiasis (CMC); STAT1 LOF → MSMD and viral susceptibility."
aliases: ["STAT1", "signal transducer and activator of transcription 1", "ISGF3", "GAF", "GAS element", "ISRE", "JAK-STAT signaling", "interferon signaling", "ISG induction", "MSMD-STAT1", "CMC-STAT1"]
sources:
  - id: darnell-1994-stat-discovery
    type: peer-reviewed
    cite: "Darnell JE Jr, Kerr IM, Stark GR. Jak-STAT pathways and transcriptional activation in response to IFNs and other extracellular signaling proteins. Science. 1994;264(5164):1415-1421."
    doi: "10.1126/science.8197455"
    pmid: "8197455"
    url: "https://doi.org/10.1126/science.8197455"
    accessed: "2026-06-08"
  - id: liu-2011-stat1-gof-cmc
    type: peer-reviewed
    cite: "Liu L, Okada S, Kong XF, et al. Gain-of-function human STAT1 mutations impair IL-17 immunity and underlie chronic mucocutaneous candidiasis. J Exp Med. 2011;208(8):1635-1648."
    doi: "10.1084/jem.20110958"
    pmid: "21727188"
    url: "https://doi.org/10.1084/jem.20110958"
    accessed: "2026-06-08"
cross_links:
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Type I IFN → IFNAR1/2 → JAK1/TYK2 → STAT1/STAT2 phosphorylation → ISGF3 (STAT1/STAT2/IRF9) → ISRE → ISGs (MX1, OAS1, IFIT1, PKR); IFN-γ → IFNGR → JAK1/JAK2 → STAT1 homodimer (GAF) → GAS → IRF1; STAT1 is the shared nuclear endpoint of antiviral and antimicrobial IFN signaling."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "IFN-γ → IFNGR1/2 → JAK1/JAK2 → STAT1 homodimer (GAF) → GAS → IRF1/iNOS/MHC-II; STAT1 GOF (R274Q, C324Y) → impaired Th17 → CMC (chronic mucocutaneous candidiasis); STAT1 LOF → absent IFN-γ signaling → MSMD — disseminated BCG after vaccination and NTM susceptibility."
  - target: 01-human/07-system/dengue-fever
    relation: connects-to
    note: "DENV NS5 degrades STAT2 via UBR4 → ISGF3 (STAT1/STAT2/IRF9) cannot form → ISG transcription blocked; NS5 selectively targets human STAT2 (not mouse) → human-specific IFN evasion; STAT2 degradation is a major determinant of dengue viremia and is absent in murine dengue models."
  - target: 01-human/07-system/tuberculosis
    relation: connects-to
    note: "IFN-γ → STAT1 → GAS → IRF1 → iNOS → NO kills intracellular Mtb; Mtb ManLAM and phenolic glycolipid suppress STAT1 signaling; STAT1 LOF → MSMD with disseminated BCG after vaccination and NTM infections — demonstrating STAT1 is non-redundant for mycobacterial defense."
  - target: 01-human/07-system/influenza
    relation: connects-to
    note: "Influenza NS1 blocks ISGF3 by dsRNA sequestration and TRIM25 inhibition; PA-X degrades host mRNAs; H5N1 drives cytokine storm by overwhelming STAT1/SOCS1 feedback; NS1 IFN antagonism is the virulence determinant distinguishing pandemic from seasonal influenza strains."
  - target: 01-human/07-system/hepatitis-c
    relation: connects-to
    note: "Chronic HCV drives ISG pre-activation via low-grade IFN-α → STAT1/STAT2/ISGF3 saturated → pegIFN-α fails to induce additional antiviral ISGs; IL28B TT genotype = high baseline ISG expression → pegIFN non-response; DAAs achieve SVR regardless of STAT1/ISG baseline."
  - target: 01-human/07-system/zika-virus
    relation: connects-to
    note: "ZIKV NS5 degrades STAT2 via ubiquitin-proteasomal pathway → ISGF3 (STAT1/STAT2/IRF9) cannot form → ISG transcription blocked; NS5 specifically targets human STAT2 (not mouse) → explains mouse resistance to ZIKV-induced microcephaly without IFNAR/STAT2 knockout in animal models."
  - target: 01-human/07-system/west-nile-virus
    relation: connects-to
    note: "WNV NS5 blocks STAT1 Tyr701 phosphorylation and targets STAT1 for proteasomal degradation → ISGF3 (STAT1/STAT2/IRF9) cannot form → ISG transcription blocked; NS5-mediated STAT1 antagonism enables WNV to evade type I IFN antiviral defense; distinguishes WNV from many RNA viruses."
---

# STAT1

## Overview

**STAT1** (signal transducer and activator of transcription 1) is the central transcription factor of the **interferon signaling cascade** — the shared nuclear endpoint of type I IFN (IFN-α/β), type II IFN (IFN-γ), and type III IFN (IFN-λ) pathways. Identified by Darnell, Kerr, and Stark in 1994 as part of the landmark discovery of JAK-STAT signaling [^darnell-1994-stat-discovery], STAT1 translates extracellular interferon signals into transcriptional programs that drive antiviral, antibacterial, and immunostimulatory gene expression within minutes of receptor engagement.

STAT1 operates as a **dual-mode transcription factor**: in the type I/III IFN pathway, it forms the **ISGF3 complex** (STAT1 + STAT2 + IRF9) that binds interferon-stimulated response elements (ISRE) to induce interferon-stimulated genes (ISGs); in the IFN-γ pathway, it homodimerizes as the **GAF complex** (gamma-activated factor) to bind gamma-activated sequences (GAS) and activate inflammatory and antimicrobial programs including IRF1 and iNOS.

**Clinical significance:** STAT1 gain-of-function (GOF) mutations cause **chronic mucocutaneous candidiasis (CMC)** — recurrent *Candida* infections of skin, nails, and mucous membranes — by enhanced STAT1 activity that suppresses Th17 differentiation, impairing anti-fungal mucosal immunity [^liu-2011-stat1-gof-cmc]. STAT1 loss-of-function (LOF) mutations cause **Mendelian susceptibility to mycobacterial disease (MSMD)** — disseminated BCG after vaccination and non-tuberculous mycobacterial infections — demonstrating that STAT1 is non-redundant for IFN-γ-mediated defense against intracellular pathogens.

## Structure

### STAT1 protein (750 aa, ~91 kDa)

STAT1 shares the conserved STAT domain architecture:

- **N-terminal domain (NTD, 1–130)**: Promotes STAT1 oligomerization and cooperative DNA binding; stabilizes dimer-dimer interactions on adjacent GAS sites; mediates nuclear export via CRM1
- **Coiled-coil domain (CCD, 135–315)**: Anti-parallel four-helix bundle; binds IRF9 (for ISGF3 formation); GOF mutations (C324Y, K344E, R274Q, T385M) cluster here and impair TC45 phosphatase access → prolonged nuclear pSTAT1
- **DNA-binding domain (DBD, 315–490)**: Recognizes GAS motif (TTCN₂₋₄GAA) as a homodimer; ISGF3 binds ISRE (TTTCNNTTTC) cooperatively via STAT1/STAT2 DBDs and IRF9 DBIRBD
- **SH2 domain (570–660)**: Binds phosphotyrosine on activated receptor-associated JAKs → STAT1 recruitment to activated receptors; also mediates pTyr701-SH2 homodimerization
- **Transactivation domain (TAD, 690–750)**: Recruits CBP/p300 coactivators; requires Ser727 phosphorylation (by CDK8, MAPK) for full transcriptional activity; tumor suppressor function partly via this domain

**Key phosphorylation sites:**
- **Tyr701** (by JAK1, JAK2, or TYK2 depending on receptor): Required for dimerization and nuclear translocation; dephosphorylated by TC45 nuclear phosphatase → cytoplasmic recycling
- **Ser727** (by CDK8, DNAPK): Enhances transcriptional output of the TAD without affecting nuclear translocation

**Isoforms:** STAT1α (full-length, dominant) vs STAT1β (truncated TAD, acts as dominant-negative competitor in some contexts)

## Function

1. **Antiviral ISG induction** (type I IFN pathway): IFN-α/β → ISGF3 → ISRE → MX1 (dynamin-like GTPase blocks viral RdRp), OAS1/RNase L (RNA degradation), PKR (eIF2α phosphorylation → translation block), IFIT1/2/3 (cap-structure binding), ISG15 (ubiquitin-like modifier), BST2/tetherin (viral budding block), TRIM25

2. **Antimicrobial program** (IFN-γ pathway): IFN-γ → STAT1 homodimer → GAS → IRF1 → iNOS → NO → kills intracellular *Leishmania*, *Mycobacteria*, *Salmonella*; STAT1 also drives MHC-I/II upregulation and antigen presentation

3. **Apoptosis/tumor suppression**: STAT1 promotes caspase-1/3, Fas/FasL, and TRAIL expression → antitumor cytostasis and immune-mediated tumor clearance; STAT1 LOF is permissive for spontaneous tumor growth in murine models

4. **T cell differentiation bias**: STAT1 promotes Th1 and suppresses Th17 differentiation; excess STAT1 (GOF) → reduced IL-17A/F → impaired mucosal anti-*Candida* defense

5. **Feedback regulation**: STAT1 drives SOCS1 and SOCS3 transcription → feedback inhibition of JAK kinase activity; USP18 (ISG15 protease) also suppresses IFNAR1/JAK1 signaling → terminates type I IFN responses after viral clearance

## Mechanism

### Type I IFN → ISGF3 pathway

1. IFN-α/β binds IFNAR2 (high affinity subunit) → IFNAR1 co-receptor recruitment → receptor dimerization
2. IFNAR2-associated **JAK1** and IFNAR1-associated **TYK2** trans-phosphorylate and activate each other
3. Activated JAK1/TYK2 phosphorylate IFNAR1 and IFNAR2 cytoplasmic tails → SH2 docking sites
4. **STAT2** binds phospho-IFNAR1 → JAK1/TYK2 phosphorylate STAT2 Tyr689; **STAT1** recruited via STAT2 → phosphorylated on Tyr701
5. pSTAT1/pSTAT2 heterodimer assembles → recruits **IRF9** via STAT2 coiled-coil domain → **ISGF3 complex** forms
6. ISGF3 translocates to nucleus via importin-α5 → binds **ISRE** (5′-AGTTTN₃TTTCC-3′) → ~300 ISGs transcribed within 30–60 min
7. Nuclear phosphatase **TC45** dephosphorylates STAT1 Tyr701 → STAT1 monomer exported to cytoplasm via CRM1 → recycled for next IFN cycle

### IFN-γ → GAF pathway

1. IFN-γ dimer binds **IFNGR1** (two molecules) → **IFNGR2** recruitment → tetrameric signaling complex
2. IFNGR1-associated **JAK1** and IFNGR2-associated **JAK2** trans-activate
3. Phospho-IFNGR1 Tyr440 recruits STAT1 via SH2 → JAK1/JAK2 phosphorylate STAT1 Tyr701
4. pSTAT1 dissociates from receptor → forms **STAT1 homodimer (GAF)** via reciprocal pTyr701-SH2 interactions
5. GAF translocates to nucleus → binds **GAS** (5′-TTCN₂₋₄GAA-3′) → **IRF1**, CIITA, iNOS, CXCL10, MHC-I/II, ICAM-1 transcription (within 15–30 min)

### STAT1 GOF → CMC mechanism

GOF mutations in the CCD (C324Y, R274Q, K344E, T385M) → TC45 phosphatase cannot efficiently dephosphorylate pTyr701 in the nucleus → prolonged nuclear STAT1 activity → sustained ISG and GAF-driven transcription → enhanced IFN-γ/IFN-α signaling → chronically elevated STAT1 → suppressed IL-17 pathway → impaired mucosal *Candida* clearance → CMC

Treatment: JAK inhibitors (ruxolitinib, baricitinib) can reduce excess STAT1 signaling in CMC.

### STAT1 LOF → MSMD mechanism

Null or dominant-negative LOF mutations → absent/non-functional STAT1 → IFN-γ signaling absent → macrophage cannot upregulate iNOS, IRF1, or MHC-II after Toll-like receptor or T cell activation → intracellular mycobacteria survive → disseminated BCG after routine vaccination and disseminated NTM; autosomal recessive null alleles are more severe than heterozygous dominant-negative forms

### Viral STAT2/STAT1 evasion

- **Dengue NS5**: Recruits UBR4 E3 ligase → STAT2 K48-polyubiquitination → proteasomal degradation → ISGF3 cannot form → ISG transcription blocked; species-specific (human STAT2, not mouse)
- **Influenza NS1**: Sequesters dsRNA and blocks TRIM25-mediated RIG-I ubiquitination → prevents upstream IRF3/IFN-β; also reported to directly interact with STAT2; PA-X additionally cleaves host mRNAs
- **SARS-CoV-2**: NSP1 blocks mRNA translation (reduces STAT1/STAT2 protein levels); ORF6 blocks STAT1 nuclear import via binding of importin-α; NSP3 is a deubiquitinase that counteracts ISG15

## Connections

**→ [Type I Interferon](../type-i-interferon/)**: Type I IFN → IFNAR1/2 → JAK1/TYK2 → STAT1/STAT2 phosphorylation → ISGF3 (STAT1/STAT2/IRF9) → ISRE → ISGs (MX1, OAS1, IFIT1, PKR); IFN-γ → IFNGR → JAK1/JAK2 → STAT1 homodimer (GAF) → GAS → IRF1; STAT1 is the shared nuclear endpoint of antiviral and antimicrobial IFN signaling.

**→ [IFN-γ](../ifn-gamma/)**: IFN-γ → IFNGR1/2 → JAK1/JAK2 → pSTAT1 homodimer (GAF) → GAS elements → IRF1, iNOS, MHC-II; STAT1 GOF mutations (R274Q, C324Y) → impaired Th17 differentiation → chronic mucocutaneous candidiasis (CMC); STAT1 LOF → absent IFN-γ signaling → MSMD (disseminated BCG and NTM infections).

**→ [Dengue Fever](../../../07-system/dengue-fever/)**: DENV NS5 targets STAT2 for proteasomal degradation via UBR4 → ISGF3 assembly fails → ISG transcription blocked; NS5 selectively degrades human (not murine) STAT2 → explains human-specific IFN evasion; STAT2 degradation is the dominant IFN antagonism mechanism in dengue and correlates with viremia.

**→ [Tuberculosis](../../../07-system/tuberculosis/)**: IFN-γ → STAT1 → GAS → IRF1 → iNOS → NO kills intracellular Mtb; Mtb ManLAM and phenolic glycolipid suppress STAT1 signaling; STAT1 LOF → MSMD with disseminated BCG after vaccination and NTM infections — demonstrating STAT1 is non-redundant for mycobacterial defense.

**→ [Influenza](../../../07-system/influenza/)**: Influenza NS1 blocks ISGF3 (STAT1/STAT2/IRF9) by dsRNA sequestration and TRIM25 inhibition; PA-X protein degrades host mRNAs; H5N1 avian influenza drives cytokine storm by overwhelming STAT1/SOCS1 negative feedback; NS1 IFN antagonism is the key virulence determinant distinguishing pandemic from seasonal strains.

**→ [Hepatitis C](../../../07-system/hepatitis-c/)**: Chronic HCV drives ISG pre-activation via low-grade IFN-α → STAT1/STAT2/ISGF3 saturated → pegIFN-α fails to induce additional antiviral ISGs; IL28B TT genotype = high baseline ISG expression → pegIFN non-response; DAAs achieve SVR regardless of STAT1/ISG baseline.

**→ [Zika Virus](../../../07-system/zika-virus/)**: ZIKV NS5 degrades STAT2 via ubiquitin-proteasomal pathway → ISGF3 (STAT1/STAT2/IRF9) cannot form → ISG transcription blocked; NS5 specifically targets human STAT2 (not mouse) → explains mouse resistance to ZIKV-induced microcephaly without IFNAR/STAT2 knockout in animal models.

**→ [West Nile Virus](../../../07-system/west-nile-virus/)**: WNV NS5 blocks STAT1 Tyr701 phosphorylation and targets STAT1 for proteasomal degradation → ISGF3 (STAT1/STAT2/IRF9) cannot form → ISG transcription blocked; NS5-mediated STAT1 antagonism enables WNV to evade type I IFN antiviral defense; distinguishes WNV from many RNA viruses.
