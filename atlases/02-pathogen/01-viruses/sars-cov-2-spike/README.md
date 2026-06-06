---
schema: pathogen-entry/v1
id: sars-cov-2-spike
name: SARS-CoV-2 Spike Glycoprotein
atlas: 02-pathogen
scale: 01-viruses
status: draft
last_reviewed: 2026-06-06
summary: "Homotrimeric class I fusion glycoprotein of SARS-CoV-2 (~180 kDa/protomer). S1 RBD binds ACE2 with high affinity; S2 mediates membrane fusion via 6-helix bundle. Primary target of neutralizing antibodies and all approved COVID-19 vaccines."
aliases: ["spike protein", "S protein", "SARS-CoV-2 S", "spike glycoprotein", "S1", "S2", "RBD"]
sources:
  - id: wrapp-2020-spike-cryo-em
    type: peer-reviewed
    cite: "Wrapp D, Wang N, Corbett KS, et al. Cryo-EM structure of the 2019-nCoV spike in the prefusion conformation. Science. 2020;367(6483):1260-1263."
    doi: "10.1126/science.abb2507"
    pmid: "32075877"
  - id: hoffmann-2020-ace2-tmprss2
    type: peer-reviewed
    cite: "Hoffmann M, Kleine-Weber H, Schroeder S, et al. SARS-CoV-2 Cell Entry Depends on ACE2 and TMPRSS2 and Is Blocked by a Clinically Proven Protease Inhibitor. Cell. 2020;181(2):271-280."
    doi: "10.1016/j.cell.2020.02.052"
    pmid: "32142651"
  - id: cai-2020-s2-fusion
    type: peer-reviewed
    cite: "Cai Y, Zhang J, Xiao T, et al. Distinct conformational states of SARS-CoV-2 spike protein. Science. 2020;369(6511):1586-1592."
    doi: "10.1126/science.abd4251"
    pmid: "32694201"
  - id: walls-2020-spike-structure-function
    type: peer-reviewed
    cite: "Walls AC, Park YJ, Tortorici MA, Wall A, McGuire AT, Veesler D. Structure, Function, and Antigenicity of the SARS-CoV-2 Spike Glycoprotein. Cell. 2020;181(2):281-292."
    doi: "10.1016/j.cell.2020.02.058"
    pmid: "32155444"
cross_links:
  - target: 01-human/03-molecular/ace2
    relation: targets
    note: "Spike S1 RBD binds human ACE2 (Kd ~15 nM) as the obligate entry receptor; 17 ACE2 residues contact 18 RBD residues at the interface. High-affinity ACE2 binding enabled SARS-CoV-2 pandemic spread."
  - target: 01-human/03-molecular/immunoglobulin-g
    relation: target-of
    note: "Neutralizing IgG antibodies targeting RBD (Class I–IV epitopes) and NTD (supersite) block ACE2 binding or spike conformational change; anti-spike IgG titer is primary correlate of COVID-19 vaccine efficacy."
  - target: 01-human/04-cellular/type-ii-pneumocyte
    relation: targets
    note: "Type II pneumocytes express high ACE2 and TMPRSS2, making them the primary lung target for spike-mediated SARS-CoV-2 entry and replication."
  - target: 01-human/04-cellular/cardiomyocyte
    relation: targets
    note: "Cardiomyocyte ACE2 expression enables spike-mediated SARS-CoV-2 cardiac entry; direct viral myocarditis confirmed in autopsy studies."
  - target: 01-human/04-cellular/dendritic-cell
    relation: targets
    note: "DCs express ACE2 and CLEC4M/DC-SIGN enabling spike-mediated SARS-CoV-2 infection and immune evasion; DC infection impairs type I IFN production and antigen presentation."
---

# SARS-CoV-2 Spike Glycoprotein

## Overview

The SARS-CoV-2 spike (S) protein is a **homotrimeric class I viral fusion glycoprotein** that coats the outer surface of the coronavirus particle, giving it the characteristic "corona" (crown) appearance in electron micrographs. Spike is the sole viral protein responsible for host cell receptor recognition and membrane fusion — and therefore the **primary target of the entire human adaptive immune response** to SARS-CoV-2, as well as all approved COVID-19 vaccines worldwide.

Spike encodes two functionally distinct subunits: **S1** (receptor-binding, ~680 aa) and **S2** (membrane fusion, ~588 aa), derived by cleavage at the S1/S2 boundary. The S1 receptor-binding domain (RBD) binds **angiotensin-converting enzyme 2 (ACE2)** with nanomolar affinity — the critical interaction that determines SARS-CoV-2 tissue tropism and host range. The S2 subunit drives membrane merger through a **6-helix bundle (6HB) fusion mechanism** conserved across class I viral fusion proteins (HIV gp41, influenza HA2, Ebola GP2).

The rapid elucidation of spike structure by cryo-EM [^wrapp-2020-spike-cryo-em] [^walls-2020-spike-structure-function] within weeks of the pandemic onset enabled unprecedented vaccine development speed — with mRNA vaccines encoding a **proline-stabilized prefusion spike** (2P mutation: K986P/V987P) achieving >90% efficacy.

## Structure

### Primary sequence and cleavage sites

| Region | Residues | Function |
|:---|:---|:---|
| Signal peptide | 1–12 | ER targeting |
| **S1 — NTD** | 13–303 | N-terminal domain; alternate binding site; supersite for NTD-targeting antibodies |
| **S1 — RBD** | 319–541 | Core subdomain that binds ACE2; includes receptor-binding motif (RBM: 437–508) |
| **S1 — SD1/SD2** | 542–685 | Subdomain 1/2; structural support; connects RBD to S2 |
| **S1/S2 furin site** | 681–685 (PRRAR↓S) | Furin cleavage site — unique to SARS-CoV-2 vs SARS-CoV-1; processed in producer cell Golgi |
| **S2 — FP** | ~816–833 | Fusion peptide: inserts into host membrane after TMPRSS2 cleavage at S2' (R815) |
| **S2 — HR1** | ~912–984 | Heptad repeat 1; forms inner core of 6HB |
| **S2 — HR2** | ~1163–1213 | Heptad repeat 2; antiparallel coiled-coil wraps HR1 in 6HB |
| **TM** | ~1214–1234 | Transmembrane anchor |
| **CT** | 1235–1273 | Cytoplasmic tail; palmitoylation sites; ERGIC retention signal |

### Glycosylation shield

Each spike protomer carries **~22 N-linked glycans** and 3 O-linked glycans (total ~29 per protomer). These glycans form a dense shield covering ~40% of the protein surface — masking conserved epitopes from antibody recognition (immune evasion) while being required for proper folding, ACE2 binding, and TMPRSS2 processing.

The RBM itself is partially shielded by glycans at N343 (acts as a "glycan gate") but the ACE2 contact surface remains exposed — both for receptor binding and as a vulnerable neutralization target.

### Prefusion to postfusion conformational states

Spike exists in dynamic conformational equilibrium [^cai-2020-s2-fusion]:

1. **Prefusion closed** (all RBDs down): Compact trimer; RBMs shielded by inter-protomer contacts; predominant resting state; targeted by 2P vaccine design
2. **Prefusion open** (1–3 RBDs up): One or more RBDs rotate up ~60°, exposing RBM; required for ACE2 binding; more immunogenic
3. **Post-receptor-binding**: ACE2-bound spike (S1 engagement); vulnerable to TMPRSS2 cleavage at S2' site
4. **Postfusion** (hairpin / 6HB): After S1 shedding, S2 refolds — HR1 and HR2 form antiparallel 6-helix bundle; irreversible; drives membrane merger

## Infection Mechanism

### Host receptor recognition

The SARS-CoV-2 RBD binds ACE2 via a concave surface on the RBM [^hoffmann-2020-ace2-tmprss2]:
- **Interface area**: ~1,700 Å² buried surface
- **ACE2 contact residues**: 17 ACE2 residues involved (K31, E35, E37, D38, Y41, Q42, L45, L79, M82, Y83, K353, G354, D355, R357, R393, E329 — key subset)
- **RBD contact residues**: Y449, G496, T500, N501, G502, Y505 are critical; N501Y (Alpha variant) enhances ACE2 affinity ~10-fold
- **Binding affinity**: Kd ~15 nM (vs. ~325 nM for SARS-CoV-1 RBD); higher affinity contributes to greater transmissibility

**Comparison with SARS-CoV-1**: SARS-CoV-2 RBD binds human ACE2 with ~10–20× higher affinity than SARS-CoV-1 spike due to optimized contact residues. The furin site at S1/S2 (absent in SARS-CoV-1) enables processing in the producer cell, providing pre-activated spike on virions.

### Membrane fusion mechanism

Entry follows a well-defined sequence [^hoffmann-2020-ace2-tmprss2]:

1. **Furin cleavage** (S1/S2, producer cell Golgi): Generates non-covalently associated S1+S2 heterodimer on virion
2. **ACE2 binding** (target cell surface): RBD flips up and engages ACE2; conformational change exposes S2' site
3. **TMPRSS2 cleavage** (S2', R815, at target cell surface): Releases S1; activates fusion peptide insertion — this is the preferred, kinetically fast pathway for lung infection
4. **Endosomal pathway** (TMPRSS2-low cells): Endocytosed virus is cleaved by cathepsin B/L at S2' in late endosomes — slower but operational in many cell types
5. **6-helix bundle formation**: HR1 collapses and HR2 folds back antiparallel → thermodynamically stable postfusion conformation → brings viral and host membranes into apposition → fusion pore formation → genome release

### Antigenic sites and immune evasion

Major neutralizing antibody epitopes on the spike:

| Site | Location | Mechanism |
|:---|:---|:---|
| **Class I/II (RBM)** | RBM, ACE2 contact surface | Block ACE2 binding directly |
| **Class III (cryptic)** | Core RBD, non-RBM | Block conformational change needed for ACE2 binding |
| **Class IV (internal)** | Core RBD, only when RBD "up" | Block spike function indirectly |
| **NTD supersite** | NTD N3/N5 loops | Block post-attachment steps; neutralize via unknown mechanism |

VOC mutations (Alpha N501Y, Beta K417N/E484K/N501Y, Delta L452R/T478K, Omicron BA.1 15 RBD mutations) primarily target Class I/II and NTD supersite to evade vaccine- and infection-elicited antibodies while maintaining or enhancing ACE2 affinity.

## Host Interactions

### Vaccine antigen design

All approved COVID-19 vaccines encode or deliver spike as the immunogen:

| Platform | Vaccine | Spike modification | Efficacy |
|:---|:---|:---|:---|
| **mRNA-LNP** | Pfizer-BioNTech (BNT162b2) | 2P (K986P/V987P) stabilized prefusion | ~95% (ancestral) |
| **mRNA-LNP** | Moderna (mRNA-1273) | 2P stabilized prefusion | ~94% (ancestral) |
| **Adenoviral vector** | J&J (Ad26.COV2.S) | 2P + furin site mutation | ~85% (severe disease) |
| **Adenoviral vector** | AstraZeneca (ChAdOx1-S) | Wild-type spike | ~70–90% |
| **Protein subunit** | Novavax (NVX-CoV2373) | 2P-stabilized recombinant + Matrix-M adjuvant | ~90% |

The **2P mutation** (K986P/V987P in the HR1 hinge region) locks spike in the prefusion conformation — the target of neutralizing antibodies — preventing the entropic collapse to the non-immunogenic postfusion form that occurs spontaneously at 37°C.

### Variant evolution of spike

SARS-CoV-2 spike shows continuous evolution under immune selection:

- **Receptor affinity optimization**: N501Y (Alpha, Beta, Gamma) → increased ACE2 affinity → improved transmission
- **Antibody escape**: E484K (Beta, Gamma) → escapes Class II Abs; K417N (Beta) → escapes Class I Abs
- **Furin site optimization**: Progressive enhancement of furin cleavage efficiency across variants
- **Omicron BA.1**: 37 spike mutations (15 in RBD), dramatically reducing neutralization by ancestral-strain vaccine antibodies while maintaining ACE2 binding via compensatory changes

## Connections

- `targets` → **[ACE2](../../../01-human/03-molecular/ace2/README.md)** — high-affinity RBD:ACE2 binding is the obligate first step of SARS-CoV-2 cellular entry
- `target-of` → **[Immunoglobulin G](../../../01-human/03-molecular/immunoglobulin-g/README.md)** — neutralizing anti-spike IgG is the primary adaptive defense and vaccine correlate of protection
- `targets` → **[Type II Pneumocyte](../../../01-human/04-cellular/type-ii-pneumocyte/README.md)** — primary lung infection target via high ACE2/TMPRSS2 co-expression
- `targets` → **[Cardiomyocyte](../../../01-human/04-cellular/cardiomyocyte/README.md)** — cardiac ACE2-mediated entry underlying COVID-19 myocarditis

## Pathology

### Spike-mediated pathology beyond viral entry

Beyond facilitating viral entry, spike protein itself contributes to COVID-19 pathophysiology via:

1. **ACE2 downregulation**: Spike binding → ACE2 internalization → local Ang II excess → vascular inflammation, cardiac injury, ARDS exacerbation
2. **Endothelial injury**: Spike (at subinfectious concentrations) activates TLR4 on endothelial cells → NF-κB → proinflammatory cytokines; promotes mitochondrial fragmentation; impairs NO signaling
3. **Platelet activation**: Spike directly activates platelets via ACE2 and FcγRIIA → microthrombi in COVID-19 coagulopathy
4. **Neurological effects**: Spike interacts with pericyte ACE2 in the blood-brain barrier, potentially contributing to neuroinflammation and Long COVID neurological symptoms

### Variant impact on disease severity

| Variant | Key spike mutations | Immune evasion | Clinical severity |
|:---|:---|:---|:---|
| **Wild-type (Wuhan)** | — | Baseline | Index case/pandemic seeding |
| **Alpha (B.1.1.7)** | N501Y, D614G | Minimal | ↑transmissibility, ~50% ↑mortality |
| **Delta (B.1.617.2)** | L452R, T478K, P681R | Moderate | Highest pre-Omicron severity |
| **Omicron BA.1** | 37 mutations (15 RBD) | Extensive | ↓severity vs. Delta; ↑immune escape |
| **Omicron XBB/JN.1** | Additional RBD mutations | Maximal | Ongoing immune evasion evolution |

[^wrapp-2020-spike-cryo-em]: Wrapp D, Wang N, Corbett KS, et al. Cryo-EM structure of the 2019-nCoV spike in the prefusion conformation. *Science.* 2020;367(6483):1260-1263. [doi:10.1126/science.abb2507](https://doi.org/10.1126/science.abb2507) · [PubMed 32075877](https://pubmed.ncbi.nlm.nih.gov/32075877/)
[^hoffmann-2020-ace2-tmprss2]: Hoffmann M, Kleine-Weber H, Schroeder S, et al. SARS-CoV-2 Cell Entry Depends on ACE2 and TMPRSS2 and Is Blocked by a Clinically Proven Protease Inhibitor. *Cell.* 2020;181(2):271-280. [doi:10.1016/j.cell.2020.02.052](https://doi.org/10.1016/j.cell.2020.02.052) · [PubMed 32142651](https://pubmed.ncbi.nlm.nih.gov/32142651/)
[^cai-2020-s2-fusion]: Cai Y, Zhang J, Xiao T, et al. Distinct conformational states of SARS-CoV-2 spike protein. *Science.* 2020;369(6511):1586-1592. [doi:10.1126/science.abd4251](https://doi.org/10.1126/science.abd4251) · [PubMed 32694201](https://pubmed.ncbi.nlm.nih.gov/32694201/)
[^walls-2020-spike-structure-function]: Walls AC, Park YJ, Tortorici MA, Wall A, McGuire AT, Veesler D. Structure, Function, and Antigenicity of the SARS-CoV-2 Spike Glycoprotein. *Cell.* 2020;181(2):281-292. [doi:10.1016/j.cell.2020.02.058](https://doi.org/10.1016/j.cell.2020.02.058) · [PubMed 32155444](https://pubmed.ncbi.nlm.nih.gov/32155444/)
