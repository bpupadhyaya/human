---
schema: human-scale-entry/v1
id: sars-cov-2-spike
name: SARS-CoV-2 Spike
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-08
summary: "SARS-CoV-2 Spike (class I fusogen; 1273 aa; homotrimer; furin site PRRAR absent in SARS-CoV-1) binds ACE2 (Kd ~15 nM) via RBD; 2P (K986P/V987P) proline stabilization locks prefusion conformation for mRNA vaccines; Omicron BA.1 carries 37 Spike mutations driving antibody escape."
aliases: ["SARS-CoV-2 Spike", "Spike protein", "SARS-CoV-2 S protein", "Spike glycoprotein", "prefusion Spike", "S1 RBD", "RBD", "2P Spike", "coronavirus fusion protein", "mRNA vaccine antigen"]
sources:
  - id: wrapp-2020-spike-cryo-em
    type: peer-reviewed
    cite: "Wrapp D, Wang N, Corbett KS, et al. Cryo-EM structure of the 2019-nCoV spike in the prefusion conformation. Science. 2020;367(6483):1260-1263."
    doi: "10.1126/science.abb2507"
    pmid: "32075877"
    url: "https://doi.org/10.1126/science.abb2507"
    accessed: "2026-06-08"
  - id: hoffmann-2020-ace2-tmprss2
    type: peer-reviewed
    cite: "Hoffmann M, Kleine-Weber H, Schroeder S, et al. SARS-CoV-2 Cell Entry Depends on ACE2 and TMPRSS2 and Is Blocked by a Clinically Proven Protease Inhibitor. Cell. 2020;181(2):271-280."
    doi: "10.1016/j.cell.2020.02.052"
    pmid: "32142651"
    url: "https://doi.org/10.1016/j.cell.2020.02.052"
    accessed: "2026-06-08"
  - id: walls-2020-spike-structure
    type: peer-reviewed
    cite: "Walls AC, Park YJ, Tortorici MA, Wall A, McGuire AT, Veesler D. Structure, Function, and Antigenicity of the SARS-CoV-2 Spike Glycoprotein. Cell. 2020;181(2):281-292."
    doi: "10.1016/j.cell.2020.02.058"
    pmid: "32155444"
    url: "https://doi.org/10.1016/j.cell.2020.02.058"
    accessed: "2026-06-08"
  - id: hsieh-2020-6p-stabilization
    type: peer-reviewed
    cite: "Hsieh CL, Goldsmith JA, Schaub JM, et al. Structure-based design of prefusion-stabilized SARS-CoV-2 spikes. Science. 2020;369(6510):1501-1505."
    doi: "10.1126/science.abd0826"
    pmid: "32703906"
    url: "https://doi.org/10.1126/science.abd0826"
    accessed: "2026-06-08"
cross_links:
  - target: 01-human/07-system/sars-cov-2
    relation: connects-to
    note: "Spike (S1/S2; class I fusogen; furin site PRRAR absent in SARS-CoV-1) is SARS-CoV-2's sole surface antigen (~25 trimers/virion); NSP5 Mpro (nirmatrelvir) and NSP12 RdRp (remdesivir) are the drug targets; Omicron carries progressive RBD mutations driving immune escape."
  - target: 01-human/03-molecular/ace2
    relation: connects-to
    note: "SARS-CoV-2 RBD:ACE2 interface buries ~1700 Å² (17 ACE2 + 18 RBD contact residues); Kd ~15 nM vs ~325 nM for SARS-CoV-1; N501Y (Alpha) increases ACE2 affinity ~10×; furin cleaves S1/S2 in producer cell Golgi → pre-activated spike maximizes TMPRSS2-mediated lung entry."
  - target: 01-human/03-molecular/rsv-f-protein
    relation: connects-to
    note: "SARS-CoV-2 S2 and RSV F are class I viral fusogens: HR1/HR2 six-helix bundle drives membrane merger in both; 2P proline stabilization (K986P/V987P) of SARS-CoV-2 prefusion Spike parallels DS-Cav1 RSV-F locking; both are the structural basis of approved mRNA vaccines."
  - target: 01-human/03-molecular/hiv-gp120
    relation: connects-to
    note: "SARS-CoV-2 S2 and HIV gp41 are class I viral fusogens — HR1/HR2 six-helix bundles drive membrane merger; 2P proline locking of prefusion Spike parallels SOSIP IP stabilization of HIV Env; Spike and gp120 both carry N-glycan shields masking conserved neutralizing epitopes."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "SARS-CoV-2 Spike activates TLR2/TLR4 → NF-κB on epithelial cells; Spike-mediated syncytium formation generates apoptotic debris → cGAS-STING → IFN-β; NSP1 blocks type I IFN translation; Spike mRNA vaccines activate ISGs via IFNAR; IFN-λ3 is the dominant mucosal innate barrier."
  - target: 01-human/03-molecular/mavs
    relation: connects-to
    note: "SARS-CoV-2 +ssRNA replication intermediates and defective interfering particles (5′ppp RNA) activate RIG-I → MAVS → TBK1/IRF3 → IFN-β; NSP6 sequesters MAVS; NSP13 disrupts TBK1; NSP16 2′-O-methylation evades MDA5; impaired RIG-I/MAVS correlates with COVID-19 severity."
  - target: 01-human/03-molecular/influenza-ha
    relation: connects-to
    note: "Influenza HA and SARS-CoV-2 Spike are class I viral fusogens: both cleaved by TMPRSS2; HA2 stalk and S2 heptad repeats form analogous 6-helix bundle post-fusion; conserved stalk/stem BNAbs parallel conserved RBD-targeting mAbs; both are primary mRNA-LNP vaccine immunogens."
---

# SARS-CoV-2 Spike

## Overview

The **SARS-CoV-2 Spike (S) glycoprotein** is the sole surface-exposed trimeric protein of SARS-CoV-2 virions and the **exclusive target of all protective neutralizing antibodies** against COVID-19. As a **class I viral fusogen** — a homotrimeric type I transmembrane glycoprotein — Spike undergoes irreversible conformational refolding from a metastable **prefusion** state to a thermodynamically stable **postfusion** state to drive ACE2-mediated receptor engagement and viral-host membrane fusion. Every approved COVID-19 vaccine worldwide encodes or delivers Spike as the immunogen.

The structure of SARS-CoV-2 Spike was determined by cryo-EM within weeks of the pandemic onset by Wrapp et al. [^wrapp-2020-spike-cryo-em] and Walls et al. [^walls-2020-spike-structure], revealing the **receptor-binding domain (RBD)** — ACE2 interface and identifying the **2P proline mutations (K986P/V987P)** [^hsieh-2020-6p-stabilization] that lock the prefusion conformation. These structural insights enabled unprecedented vaccine development speed: BNT162b2 and mRNA-1273 achieved >90% efficacy within ~10 months of viral genome publication.

**Key distinguishing feature**: SARS-CoV-2 Spike contains a **furin cleavage site (RRAR↓S at aa 681-685)** at the S1/S2 boundary — present in no other sarbecovirus or known bat coronavirus progenitor — which allows Golgi furin to pre-cleave Spike in the producer cell, providing virions with non-covalently tethered S1/S2 subunits that dramatically increase TMPRSS2-mediated entry efficiency and upper respiratory transmissibility.

## Structure

### Primary sequence and domain organization (1273 aa)

| Domain | Residues | Function |
|:---|:---|:---|
| Signal peptide | 1–12 | ER targeting |
| **S1 — NTD** | 13–303 | N-terminal domain; alternate receptor binding; supersite for NTD-targeting antibodies |
| **S1 — RBD** | 319–541 | Receptor-binding domain; core of ACE2-binding interface |
| **S1 — RBM** | 437–508 | Receptor-binding motif within RBD; direct ACE2 contact surface |
| **S1 — SD1/SD2** | 542–685 | Subdomain 1/2; structural support connecting RBD to S2 |
| **S1/S2 furin site** | 681–685 (RRAR↓S) | Furin cleavage in producer cell Golgi — **unique to SARS-CoV-2** among sarbecoviruses |
| **S2 — FP** | ~816–833 | Fusion peptide; inserts into host membrane after TMPRSS2 S2' cleavage (R815) |
| **S2 — HR1** | ~912–984 | Heptad repeat 1; inner core of 6-helix bundle (6HB) |
| **S2 — CH** | ~986–1035 | Central helix; 2P (K986P/V987P) and 6P proline sites reside here |
| **S2 — HR2** | ~1163–1213 | Heptad repeat 2; antiparallel against HR1 in 6HB |
| **TM** | ~1214–1234 | Transmembrane anchor |
| **CT** | 1235–1273 | Cytoplasmic tail; palmitoylation sites; ERGIC retention signal |

### Glycosylation shield

Each Spike protomer carries **~22 N-linked glycans** (total ~66 per homotrimer) covering ~40% of the protein surface area. This glycan shield evolved to conceal conserved functional epitopes from antibody recognition — a convergent strategy shared with HIV gp120 (~27 N-glycans). Key glycan positions:
- **N343**: "Glycan gate" adjacent to the RBM; partially shields Class III epitopes but RBM itself remains exposed for ACE2 access and antibody targeting
- **N234, N165**: Stabilize the "RBD-up" conformation required for ACE2 binding by interacting with the adjacent protomer

### Prefusion conformational states

Spike exists in a conformational equilibrium critical for both function and immunogenicity:
1. **Prefusion closed** (all 3 RBDs "down"): Compact trimer; RBMs shielded by inter-protomer contacts; thermodynamically metastable; vaccine-optimal conformation
2. **Prefusion open** (1–3 RBDs "up"): One or more RBDs rotate ~60°, exposing RBM for ACE2 binding; kinetically accessible transiently
3. **Receptor-engaged**: ACE2-bound Spike; exposes S2' site for TMPRSS2 cleavage
4. **Postfusion**: After S1 shedding → S2 refolds → HR1/HR2 form irreversible 6HB → membrane merger

## Function

### ACE2 receptor engagement

The SARS-CoV-2 RBD:ACE2 interface [^hoffmann-2020-ace2-tmprss2]:
- **Buried surface area**: ~1,700 Å² (17 ACE2 residues + 18 RBD residues in contact)
- **Key ACE2 contacts**: K31, Y41, Q42, K353, R357 (critical for binding; polymorphisms in non-human ACE2 reduce susceptibility)
- **Key RBD contacts (RBM)**: Y449, L452, Y489, Q493, G496, Q498, T500, N501, G502, Y505
- **Binding affinity**: Kd ~15 nM (vs ~325 nM for SARS-CoV-1); ~10–20× higher affinity enables greater transmissibility
- **N501Y (Alpha variant)**: Enhances ACE2 affinity ~10× by adding van der Waals contact with Y41 of ACE2

### Entry pathway

1. **Furin cleavage** (Golgi of producer cell): Cleaves RRAR↓S at S1/S2 → non-covalent S1/S2 on virion; provides ready-to-fuse conformation
2. **ACE2 binding** (target cell): RBD flips "up" → binds ACE2; conformational strain exposes S2' site at R815
3. **TMPRSS2 cleavage** (cell surface, preferred in lung): S2' cleavage at Arg815 → releases S1; activates FP insertion — kinetically fast, ~60-fold more efficient than endosomal route
4. **Endosomal entry** (TMPRSS2-low cells, preferred by Omicron): Endocytosis → cathepsin B/L cleavage at S2' in late endosomes — broader tropism but slower kinetics; explains Omicron's increased upper airway but reduced deep lung tropism vs Delta
5. **6HB formation**: HR1 and HR2 zipper antiparallel → stable postfusion hairpin → viral and host membranes apposed → fusion pore → genome release

## Mechanism

### Neutralizing antibody epitopes

Four structural classes of RBD-targeting neutralizing antibodies plus NTD antibodies:

| Class | Epitope | Mechanism | Key antibodies | Omicron escape |
|:---|:---|:---|:---|:---|
| **Class I** | RBM; ACE2-overlapping | Block ACE2 binding; bind "RBD-up" only | VH3-53/VH3-66 germline (CB6, P2B-2F6) | K417N/T, E484K strongly escape |
| **Class II** | RBM; partial ACE2 overlap | Block ACE2 binding; bind both "up" and "down" | LY-CoV555 (bamlanivimab), C121 | E484K/A, L452R escape |
| **Class III** | Core RBD; non-RBM | Block conformational change; accessible in "down" | S309 (sotrovimab), CR3022 | Partially retained |
| **Class IV** | Core RBD; internal | Mechanism unclear; only "up" RBD | CR3022 alone | Minimal escape |
| **NTD supersite** | NTD N3+N5 loops | Block post-attachment entry | 4A8, S2L20 | Extensive (NTD mutations W152R, etc.) |

### Prefusion stabilization strategies

| Strategy | Mutations | Used in |
|:---|:---|:---|
| **2P** | K986P + V987P (CH helix) | BNT162b2 (Pfizer), mRNA-1273 (Moderna), all early mRNA vaccines |
| **6P** | 2P + F817P + A892P + A899P + A942P | NVX-CoV2373 (Novavax), updated mRNA-1273.214, RSVpreF parallel strategy |
| **Furin site KO** | 682-685 GSAS or RRAR→GSAS | J&J Ad26.COV2.S; some subunit vaccines |
| **Disulfide (SD1)** | V987P + F817C/A892C | Experimental; further stabilization |

The 2P strategy (K986P/V987P at the CH domain just N-terminal to HR1) introduces backbone rigidity that prevents the CH from initiating the HR1 zipping reaction required for 6HB formation — kinetically trapping the prefusion state.

### Structural comparison to other class I viral fusogens

| Feature | SARS-CoV-2 S2 | RSV F | HIV gp41 |
|:---|:---|:---|:---|
| Fusogen class | Class I homotrimer | Class I homotrimer | Class I homotrimer |
| 6HB formation | HR1 + HR2 antiparallel | HRA + HRB antiparallel | HR1 + HR2 antiparallel |
| Prefusion lock | 2P/6P prolines | DS-Cav1 (S155C/S290C + N67I/S215P) | SOSIP (SOS disulfide + IP proline) |
| Key NAb epitope | Prefusion RBD (Class I-IV) | Prefusion site Ø | CD4bs, V1V2 apex |
| Glycan shield | ~22 N-glycans/protomer | 5–7 N-glycans | ~27 N-glycans (50% MW) |

## Connections

**→ [SARS-CoV-2](../../../07-system/sars-cov-2/)**: Spike is SARS-CoV-2's sole surface antigen encoded in the viral genome; furin site PRRAR (absent in SARS-CoV-1) enables producer-cell Golgi cleavage providing pre-activated Spike; NSP5 Mpro (nirmatrelvir) and NSP12 RdRp (remdesivir) are the virus's other key therapeutic targets; Omicron carries progressive RBD mutations.

**→ [ACE2](../ace2/)**: RBD binds ACE2 (17 ACE2 + 18 RBD contact residues; ~1700 Å²; Kd ~15 nM); N501Y (Alpha) enhances affinity ~10×; furin-cleavage in producer-cell Golgi pre-activates Spike → maximizes TMPRSS2-mediated lung entry; Spike binding triggers ACE2 internalization → RAAS imbalance → Ang II excess → ARDS amplification.

**→ [RSV F Protein](../rsv-f-protein/)**: SARS-CoV-2 S2 and RSV F are both class I viral fusogens — HR1/HR2 six-helix bundles drive membrane merger; 2P proline stabilization (K986P/V987P) of SARS-CoV-2 prefusion Spike is structurally analogous to DS-Cav1 RSV-F locking; both antigens are encoded by approved mRNA vaccines using the same LNP platform.

**→ [HIV gp120](../hiv-gp120/)**: SARS-CoV-2 S2 and HIV gp41 are class I viral fusogens — HR1/HR2 six-helix bundles drive membrane merger; 2P proline locking of prefusion Spike is conceptually parallel to SOSIP IP stabilization of the HIV Env trimer; Spike and gp120 both deploy N-glycan shields that mask conserved neutralizing epitopes from the humoral immune response.

**→ [Type I Interferon](../type-i-interferon/)**: SARS-CoV-2 Spike activates TLR2/TLR4 → NF-κB on epithelial cells; Spike-mediated syncytium formation generates apoptotic debris → cGAS-STING → IFN-β; NSP1 blocks type I IFN translation; Spike mRNA vaccines activate ISGs via IFNAR; IFN-λ3 is the dominant mucosal innate barrier.

**→ [MAVS](../mavs/)**: SARS-CoV-2 +ssRNA replication intermediates and 5′ppp DI-particle RNA activate RIG-I → MAVS → TBK1/IRF3 → IFN-β downstream of Spike-mediated entry; NSP6 sequesters MAVS; NSP13 disrupts TBK1; NSP16 2′-O-methyltransferase prevents MDA5 recognition; impaired MAVS-IFN correlates with COVID-19 severity.

**→ [Influenza Hemagglutinin](../influenza-ha/)**: Influenza HA and SARS-CoV-2 Spike are class I viral fusogens: both cleaved by TMPRSS2; HA2 stalk and S2 heptad repeats form analogous 6-helix bundle post-fusion; conserved stalk/stem BNAbs parallel conserved RBD-targeting mAbs; both are primary mRNA-LNP vaccine immunogens.

[^wrapp-2020-spike-cryo-em]: Wrapp D, Wang N, Corbett KS, et al. Cryo-EM structure of the 2019-nCoV spike in the prefusion conformation. *Science.* 2020;367(6483):1260-1263. [doi:10.1126/science.abb2507](https://doi.org/10.1126/science.abb2507) · [PubMed 32075877](https://pubmed.ncbi.nlm.nih.gov/32075877/)
[^hoffmann-2020-ace2-tmprss2]: Hoffmann M, Kleine-Weber H, Schroeder S, et al. SARS-CoV-2 Cell Entry Depends on ACE2 and TMPRSS2 and Is Blocked by a Clinically Proven Protease Inhibitor. *Cell.* 2020;181(2):271-280. [doi:10.1016/j.cell.2020.02.052](https://doi.org/10.1016/j.cell.2020.02.052) · [PubMed 32142651](https://pubmed.ncbi.nlm.nih.gov/32142651/)
[^walls-2020-spike-structure]: Walls AC, Park YJ, Tortorici MA, Wall A, McGuire AT, Veesler D. Structure, Function, and Antigenicity of the SARS-CoV-2 Spike Glycoprotein. *Cell.* 2020;181(2):281-292. [doi:10.1016/j.cell.2020.02.058](https://doi.org/10.1016/j.cell.2020.02.058) · [PubMed 32155444](https://pubmed.ncbi.nlm.nih.gov/32155444/)
[^hsieh-2020-6p-stabilization]: Hsieh CL, Goldsmith JA, Schaub JM, et al. Structure-based design of prefusion-stabilized SARS-CoV-2 spikes. *Science.* 2020;369(6510):1501-1505. [doi:10.1126/science.abd0826](https://doi.org/10.1126/science.abd0826) · [PubMed 32703906](https://pubmed.ncbi.nlm.nih.gov/32703906/)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
