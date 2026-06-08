---
schema: human-scale-entry/v1
id: rsv-f-protein
name: RSV F Protein
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-08
summary: "RSV fusion (F) protein (class I viral fusogen; 574 aa; pre-F and post-F conformations) mediates RSV-host membrane fusion → syncytia; prefusion site Ø is the dominant neutralizing epitope targeted by nirsevimab and mRNA vaccines; DS-Cav1 proline locks F in prefusion for vaccines."
aliases: ["RSV F protein", "RSV fusion protein", "prefusion F", "post-fusion F", "site Ø", "DS-Cav1", "nirsevimab target", "RSV F glycoprotein", "RSVpreF", "respiratory syncytial virus fusion glycoprotein"]
sources:
  - id: mclellan-2013-prefusion-f-structure
    type: peer-reviewed
    cite: "McLellan JS, Chen M, Leung S, et al. Structure-based design of a fusion glycoprotein vaccine for respiratory syncytial virus. Science. 2013;342(6158):592-598."
    doi: "10.1126/science.1234914"
    pmid: "23618766"
    url: "https://doi.org/10.1126/science.1234914"
    accessed: "2026-06-08"
  - id: mazur-2018-rsv-vaccine-landscape
    type: peer-reviewed
    cite: "Mazur NI, Higgins D, Nunes MC, et al. The respiratory syncytial virus vaccine landscape: lessons from the graveyard and promising candidates. Lancet Infect Dis. 2018;18(10):e295-e311."
    doi: "10.1016/S1473-3099(18)30292-5"
    pmid: "29954680"
    url: "https://doi.org/10.1016/S1473-3099(18)30292-5"
    accessed: "2026-06-08"
cross_links:
  - target: 01-human/07-system/rsv
    relation: connects-to
    note: "RSV F protein mediates attachment and viral-cell membrane fusion → syncytium formation; F is cleaved by furin → F1+F2 subunits; site Ø (prefusion F) is the dominant neutralizing epitope; nirsevimab and mRNA vaccines (mRNA-1345, mResvia) target prefusion F to prevent RSV."
  - target: 01-human/03-molecular/mavs
    relation: connects-to
    note: "RSV replication generates 5′ppp RNA → RIG-I → MAVS → IFN-β; RSV F protein activates TLR4 → MyD88 → NF-κB independently of MAVS; NS1 degrades TRIM25 → blocks RIG-I/MAVS; NS2 blocks STAT2; F protein-driven TLR4 signaling amplifies airway neutrophilic inflammation."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "RSV F protein-mediated syncytium formation → mechanical stress and ATP release → P2X4/P2Y receptor activation → IL-33 release from epithelial nuclei; IL-33 signals via ST2 on ILC2 → IL-4/IL-5/IL-13; anti-F antibodies (nirsevimab) prevent syncytia → prevent F-driven IL-33 release."
  - target: 01-human/03-molecular/tslp
    relation: connects-to
    note: "RSV F protein-mediated airway epithelial damage → TSLP release; prefusion F triggers TSLP via pattern recognition receptor signaling; TSLP → TSLP receptor on ILC2/basophils → IL-4/IL-13 → IgE; nirsevimab (anti-F mAb) preventing RSV infection reduces TSLP-driven Th2 sensitization."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Prefusion RSV F stabilized by proline substitutions (DS-Cav1 design) induces high-titer site Ø neutralizing antibodies — basis of nirsevimab and mRNA vaccines; RSV NS1/NS2 block type I IFN (NS1→TRIM25/IRF3, NS2→STAT2); recombinant IFN-λ protects immunocompromised hosts from RSV."
  - target: 01-human/03-molecular/hiv-gp120
    relation: connects-to
    note: "gp41 (triggered by gp120-CD4 binding) is a class I viral fusogen with HR1/HR2 six-helix bundle analogous to RSV-F and SARS-CoV-2 S2; gp41 MPER targeted by 10E8 bNAbs analogous to anti-preF site Ø antibodies; SOSIP IP proline mutation parallels DS-Cav1 preF locking strategy."
  - target: 01-human/03-molecular/sars-cov-2-spike
    relation: connects-to
    note: "SARS-CoV-2 S2 and RSV F are both class I viral fusogens with HR1/HR2 six-helix bundles driving membrane merger; 2P proline stabilization of SARS-CoV-2 prefusion Spike (K986P/V987P) structurally parallels DS-Cav1 RSV preF locking; mRNA vaccine platforms encode both antigens."
  - target: 01-human/03-molecular/norovirus-vp1
    relation: connects-to
    note: "Both RSV F and Norovirus VP1 are sole viral surface antigens serving as vaccine immunogens; mRNA-LNP encodes both (mResvia/RSV; mRNA-1403/norovirus); DS-Cav1 RSV-F proline locking and VP1 VLP self-assembly are parallel structure-based vaccine design strategies."
  - target: 01-human/03-molecular/influenza-ha
    relation: connects-to
    note: "RSV F and influenza HA are class I viral fusogens sharing 6-helix bundle post-fusion mechanism; conserved HA2 stalk BNAbs parallel site Ø anti-F antibodies; both are mRNA-LNP vaccine immunogens (mResvia RSV F; mRNA-1073 influenza HA) enabling rapid pandemic reformulation."
---

# RSV F Protein

## Overview

The **RSV fusion (F) protein** is the primary surface glycoprotein of respiratory syncytial virus (RSV) responsible for **viral-host membrane fusion** and is the central target of protective immunity, prophylaxis, and all approved RSV vaccines. F is a **class I viral fusogen** — a homotrimeric type I transmembrane glycoprotein that undergoes an irreversible conformational transition from a metastable **prefusion (pre-F)** state to a thermodynamically stable **postfusion (post-F)** state to drive membrane merger. This conformational change is the mechanistic basis for both viral entry and the critical distinction between protective (pre-F-directed) and non-protective (post-F-directed) antibody responses.

The RSV F protein story represents one of the most instructive chapters in modern structural vaccinology: the 1960s **formalin-inactivated RSV (FI-RSV)** vaccine failure — which caused vaccine-enhanced disease (VED) in two-year-old children — was ultimately traced to generation of post-fusion F antibodies with poor neutralizing capacity plus a Th2-biased immune response [^mazur-2018-rsv-vaccine-landscape]. Decades later, the **McLellan laboratory's prefusion F crystal structure** in 2013 [^mclellan-2013-prefusion-f-structure] revealed site Ø — a prefusion-specific epitope that is >10× more potently neutralized than site II (the palivizumab site present on both conformations). This structural insight directly enabled engineering of prefusion-stabilized F (DS-Cav1 design) that is the basis of nirsevimab, Abrysvo, Arexvy, and mResvia.

**Clinical impact:** Nirsevimab (Beyfortus), targeting site Ø on prefusion F, was approved in 2023 for universal infant RSV prophylaxis — providing single-dose, season-long protection (77% reduction in RSV hospitalization in the NIRSEVIMAB-MEDICALLY ATTENDED trial). Simultaneously, three prefusion F-based vaccines were approved for adults ≥60 years.

## Structure

### RSV F protein primary structure (574 aa)

The RSV F protein is synthesized as a **F0 precursor** (70 kDa) that is cleaved at **two furin consensus sequences** (RKKR at site I, aa 109; RARR at site II, aa 136) by furin-like proteases in the trans-Golgi network → releases a 27-aa intervening peptide (pep27) → generates:
- **F2 subunit** (N-terminal; aa 1-109): Heavily glycosylated ectodomain; holds together F1 + F2 via a disulfide bond (Cys37-Cys439); plays limited role in membrane fusion
- **F1 subunit** (C-terminal; aa 137-574): Contains the **fusion peptide** (FP, hydrophobic N-terminus of F1; inserts into host membrane), **heptad repeat A (HRA)** and **heptad repeat B (HRB)** domains, **transmembrane domain (TM)**, and cytoplasmic tail; drives the conformational transition

### Pre-F vs. post-F conformations

| Feature | Prefusion F (pre-F) | Postfusion F (post-F) |
|---|---|---|
| **Thermodynamic state** | Metastable; kinetically trapped by inter-subunit contacts | Stable minimum energy hairpin |
| **Shape** | Compact, globular trimer; ~11 nm tall | Extended rod-like trimer; ~15 nm tall |
| **HRA** | Packed at base of trimer; not a coiled coil | Zips against HRB → 6-helix bundle (6HB) |
| **Fusion peptide** | Tucked inside trimer; not exposed | Projected outward (or cleaved/rearranged) |
| **Key difference** | Exposes site Ø and other prefusion-specific epitopes | Site Ø abolished; site II accessible |
| **Trigger for transition** | Receptor binding (?); pH-independent for RSV; also occurs spontaneously | Irreversible once initiated |

### Antigenic sites on RSV F

Six major antigenic sites have been characterized, with critical differences in accessibility and neutralization potency:

| Site | Location | Antibodies | Notes |
|---|---|---|---|
| **Site Ø** | Apex of prefusion trimer; aa 196-209, 62-69 | D25, AM22, nirsevimab | **Prefusion-specific**; highest neutralization potency; >10× more potent than site II; target of all leading RSV vaccines |
| **Site I** | aa 422-438 (F1) | 131-2A | Present on both conformations; weak neutralization |
| **Site II** | aa 254-277 (F1, Cys at 262 and 277) | Palivizumab, motavizumab | Present on both pre-F and post-F; 5-7 mg/kg monthly dosing (palivizumab) |
| **Site III** | aa 46-52 + 214-225 | MPE8 | Quaternary site; present on both conformations; conservative mutations escape |
| **Site IV** | aa 417-429 (F2-F1 interface) | 101F | Both conformations; moderate neutralization |
| **Site V** | aa 161-167 | 1129 | Shared; cross-reactive with hMPV F |
| **Site Ø′** (sub-site) | Adjacent to site Ø | RSD5 | Overlapping with Ø; prefusion-specific |

### DS-Cav1 prefusion stabilization

**DS-Cav1** (McLellan et al. 2013) [^mclellan-2013-prefusion-f-structure]: Introduced four mutations into the F1 ectodomain to lock F in the prefusion conformation:
1. **S155C + S290C**: Engineered disulfide bond (cavity-filling) between the cavity between HRA and the body — covalently locks HRA against spontaneous refolding
2. **S190F + V207L**: Cavity-filling hydrophobic substitutions at the trimer interface — increase packing at the prefusion apex → prevent spontaneous transition

DS-Cav1-stabilized pre-F induces **25-fold higher site Ø neutralizing antibodies** compared to unmodified recombinant F and ~3-fold higher than palivizumab site II antibodies. Vaccine manufacturers have each developed proprietary stabilization strategies on this framework:
- **Abrysvo (Pfizer RSVpreF)**: Bivalent formulation (RSV-A + RSV-B pre-F); two additional proline mutations; formaldehyde-cross-linked
- **Arexvy (GSK RSVPreF3-AS01E)**: Truncated ectodomain; specific cavity-filling mutations; AS01E adjuvant (MPL + QS-21)
- **mResvia (Moderna mRNA-1345)**: mRNA encoding prefusion-stabilized F with proprietary prolines; LNP delivery; administered IM

## Function

### Membrane fusion mechanism

1. **Attachment**: RSV G protein attaches to CX3CR1 on airway epithelium; F protein also directly binds **nucleolin** (overexpressed on basal surface of polarized epithelium) and **IGFR1** as co-receptors
2. **Pre-F triggering**: Receptor contact and/or acidification induces conformational change in the F0/F trimer → fusion peptide released from trimer core → **inserts into host membrane lipid bilayer**
3. **HRA-HRB zipping (6-helix bundle formation)**: HRA (extending from fusion peptide) and HRB (anchoring TM domain in viral membrane) fold together → antiparallel 6-HB → pulls viral and host membranes together → **membrane fusion**
4. **Syncytium formation**: F remains on cell surface after infection → HLA-A/B/C-independent cell-cell fusion → formation of large multinucleated syncytia (giant cells); characteristic RSV histopathology

### TLR4 activation by RSV F

RSV F protein directly activates **TLR4** on macrophages and airway epithelial cells via a mechanism independent of RIG-I/MAVS and RIG-I RNA sensing:
- F protein → TLR4/CD14/MD-2 complex → MyD88 → IRAK4 → TRAF6 → NF-κB → IL-6, TNF-α, CXCL8 (neutrophil chemokine)
- This innate TLR4 activation contributes to the neutrophilic component of RSV bronchiolitis even in the absence of complete IFN-β production (since NS1/NS2 suppress MAVS-driven IFN)
- **Clinical implication**: RSV bronchiolitis has two innate inflammatory arms: (1) MAVS-IFN-β (partially blocked by NS1/NS2) and (2) TLR4-NF-κB (not blocked by NS1/NS2)

### Role in type 2 immunopathology

RSV F protein is the direct mechanistic driver of airway IL-33 and TSLP release:
- **F-mediated syncytium formation** → mechanical stress on epithelial junctions + ATP release → P2X4/P2Y purinergic receptor activation → IL-33 exocytosis from epithelial nuclei → ST2+ ILC2 activation → IL-4/IL-5/IL-13 cascade
- **F TLR4 signaling** → NF-κB → TSLP transcription from bronchial epithelium → TSLPR/IL-7Rα on ILC2 and basophils → Th2 sensitization
- **Anti-F antibodies (nirsevimab)** that prevent RSV attachment and fusion also prevent syncytium formation → prevent F-driven IL-33 and TSLP release → reduced type 2 airway sensitization

## Mechanism

### Nirsevimab (Beyfortus) — site Ø mAb

- **Epitope**: Cryptic helix-loop-helix at the apex of prefusion F trimer (site Ø, aa 196-209 loop); inaccessible in postfusion F
- **Neutralization mechanism**: Binds prefusion F trimer → steric block of the conformational transition → F cannot insert fusion peptide into host membrane → virus cannot fuse
- **Half-life engineering**: Three Fc mutations — **M252Y/S254T/T256E (YTE)** — increase FcRn binding at acidic pH → extend serum half-life from ~20 days (palivizumab) to **~70 days**; single IM injection provides 5-month protection (one RSV season)
- **Palivizumab comparison**: Palivizumab (Synagis) binds site II on both pre-F and post-F; 5-6 mg/kg monthly; limited to high-risk infants; replaced by nirsevimab for universal infant prophylaxis
- **Efficacy (MELODY trial)**: 74.5% against medically attended RSV LRTI; **77% reduction in RSV hospitalization** (NIRSEVIMAB-MEDICALLY ATTENDED trial in higher-risk infants); 2023 FDA approval; universal ACIP recommendation

### Prefusion F vaccines

All three approved adult RSV vaccines exploit DS-Cav1-type stabilization [^mazur-2018-rsv-vaccine-landscape]:

| Vaccine | Manufacturer | Platform | Pre-F stabilization | Key trial | Efficacy |
|---|---|---|---|---|---|
| **Abrysvo (RSVpreF)** | Pfizer | Bivalent protein subunit (A+B) | Two proprietary prolines + S155C/S290C variant | RENOIR/MATISSE | 88.9% vs severe LRTI; 82% vs infant (maternal) |
| **Arexvy (RSVPreF3-AS01E)** | GSK | Protein subunit + AS01E adjuvant | Truncated ectodomain, cavity-filling mutations | AReSVi-006 | 82.6% vs RSV-LRTD |
| **mResvia (mRNA-1345)** | Moderna | Lipid nanoparticle mRNA | mRNA-encoded prefusion-stabilized F (4 mutations) | RENOIR | 83.7% vs RSV-LRTD |

**Key scientific basis**: All three vaccines generate high-titer **site Ø-directed neutralizing antibodies** — consistent with the McLellan et al. 2013 insight that the pre-F conformation exposes the most potently neutralized RSV epitope. In contrast, the failed FI-RSV vaccine of the 1960s generated exclusively post-F antibodies (site II) with inadequate neutralization and Th2-skewed memory → VED.

### FI-RSV vaccine-enhanced disease (VED) — mechanistic lessons

The FI-RSV disaster (Chin et al. 1969) taught four principles now embedded in vaccine design:
1. **Conformation matters**: Post-fusion F antibodies fail to neutralize; pre-fusion F antibodies neutralize potently
2. **Th1/Th2 balance is critical**: Formalin inactivation generates Th2-biased responses; prefusion protein + adjuvant generates Th1/Th2-balanced responses
3. **Eosinophilic immunopathology**: FI-RSV primed eosinophilic lung disease upon RSV challenge (high IL-5, ECP in biopsied children); current vaccines show no such priming in trials
4. **No VED signal with prefusion F vaccines**: MELODY, MATISSE, AReSVi-006 trials showed no eosinophilia or enhanced disease in any vaccine recipient

## Connections

**→ [RSV](../../../07-system/rsv/)**: RSV F protein mediates attachment and viral-host membrane fusion → syncytium formation; prefusion F (site Ø) is the dominant neutralizing epitope; nirsevimab (site Ø mAb), Abrysvo (Pfizer bivalent preF), Arexvy (GSK preF3 + AS01E), and mResvia (Moderna mRNA-1345) all target prefusion F to prevent RSV disease.

**→ [MAVS](../mavs/)**: RSV F protein activates TLR4 → MyD88 → NF-κB inflammatory signaling independently of RIG-I/MAVS; RSV replication generates 5′ppp RNA → RIG-I → MAVS → IFN-β (partially blocked by NS1); NS1 degrades TRIM25 → prevents RIG-I/MAVS; NS2 blocks STAT2/ISG induction; F TLR4 signaling drives the neutrophilic component of RSV bronchiolitis.

**→ [IL-33](../il-33/)**: RSV F protein-mediated syncytium formation → mechanical stress and ATP release → purinergic receptor activation → IL-33 release from epithelial nuclei; IL-33 → ST2/ILC2 → IL-4/IL-5/IL-13 → eosinophilia and airway hyperresponsiveness; nirsevimab prevents syncytia, eliminating F-driven IL-33 release.

**→ [TSLP](../tslp/)**: RSV F protein-mediated epithelial damage and TLR4/NF-κB signaling trigger TSLP from airway epithelium → TSLPR/IL-7Rα on ILC2 and basophils → IL-4/IL-13 → Th2 sensitization and IgE production; nirsevimab (anti-F mAb) prevents infection-driven TSLP release → reduces Th2 sensitization in early life.

**→ [Type I Interferon](../type-i-interferon/)**: RSV NS1/NS2 collectively suppress type I IFN at multiple levels (NS1→TRIM25/IRF3; NS2→STAT2); prefusion-stabilized F vaccines (DS-Cav1 design) induce high-titer site Ø neutralizing antibodies without relying on IFN-amplified immunity; IFN-λ (type III) at mucosal surfaces remains the dominant innate antiviral defense that NS1/NS2 cannot fully block.

**→ [HIV gp120](../hiv-gp120/)**: gp41 (triggered by gp120-CD4 binding) is a class I viral fusogen with HR1/HR2 six-helix bundle analogous to RSV-F and SARS-CoV-2 S2; gp41 MPER targeted by 10E8 bNAbs analogous to anti-preF site Ø antibodies; SOSIP IP proline mutation parallels DS-Cav1 preF locking strategy.

**→ [SARS-CoV-2 Spike](../sars-cov-2-spike/)**: SARS-CoV-2 S2 and RSV F are both class I viral fusogens with HR1/HR2 six-helix bundles driving membrane merger; 2P proline stabilization of prefusion SARS-CoV-2 Spike (K986P/V987P) structurally parallels DS-Cav1 RSV-F locking; mRNA-LNP vaccine platforms encode both antigens using the same LNP delivery technology.

**→ [Norovirus VP1](../norovirus-vp1/)**: Both RSV F (prefusion, site Ø) and Norovirus VP1 (P2 subdomain) are the sole viral surface antigens and vaccine immunogens of their respective viruses; mRNA-LNP platforms encode both (mResvia for RSV F; mRNA-1403 for norovirus VP1); DS-Cav1 RSV-F proline locking and VP1 VLP self-assembly are parallel structure-based vaccine design strategies.

**→ [Influenza Hemagglutinin](../influenza-ha/)**: RSV F and influenza HA are class I viral fusogens sharing 6-helix bundle post-fusion mechanism; conserved HA2 stalk BNAbs parallel site Ø anti-F antibodies; both are mRNA-LNP vaccine immunogens (mResvia RSV F; mRNA-1073 influenza HA) enabling rapid pandemic reformulation.

[^mclellan-2013-prefusion-f-structure]: McLellan JS, Chen M, Leung S, et al. Structure-based design of a fusion glycoprotein vaccine for respiratory syncytial virus. *Science.* 2013;342(6158):592-598. [doi:10.1126/science.1234914](https://doi.org/10.1126/science.1234914) · [PubMed 23618766](https://pubmed.ncbi.nlm.nih.gov/23618766/)
[^mazur-2018-rsv-vaccine-landscape]: Mazur NI, Higgins D, Nunes MC, et al. The respiratory syncytial virus vaccine landscape: lessons from the graveyard and promising candidates. *Lancet Infect Dis.* 2018;18(10):e295-e311. [doi:10.1016/S1473-3099(18)30292-5](https://doi.org/10.1016/S1473-3099(18)30292-5) · [PubMed 29954680](https://pubmed.ncbi.nlm.nih.gov/29954680/)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
