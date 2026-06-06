---
schema: human-scale-entry/v1
id: rad51
name: RAD51
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-06
summary: "RecA-family recombinase at the core of homologous recombination; BRCA2 loads RAD51 onto resected ssDNA ends, displacing RPA to form the presynaptic filament for strand invasion. Overexpression confers drug resistance; RAD51 inhibitors (RI-1, B02) sensitize HR-proficient tumors."
aliases: ["RAD51 recombinase", "HsRad51", "RECA homolog", "RAD51A", "HR recombinase"]
sources:
  - id: baumann-1996-rad51
    type: peer-reviewed
    cite: "Baumann P, Benson FE, West SC. Human Rad51 protein promotes ATP-dependent homologous pairing and strand transfer reactions in vitro. Cell. 1996;87(4):757-766."
    doi: "10.1016/S0092-8674(00)81394-X"
    pmid: "8929543"
    url: "https://doi.org/10.1016/S0092-8674(00)81394-X"
  - id: pellegrini-2002-brca2-rad51
    type: peer-reviewed
    cite: "Pellegrini L, Yu DS, Lo T, et al. Insights into DNA recombination from the structure of a RAD51-BRCA2 complex. Nature. 2002;420(6913):287-293."
    doi: "10.1038/nature01230"
    pmid: "12442171"
    url: "https://doi.org/10.1038/nature01230"
  - id: mason-2019-rad51-inhibitor
    type: peer-reviewed
    cite: "Mason JM, Chan YL, Weichselbaum RW, Bishop DK. Non-enzymatic roles of human RAD51 at stalled replication forks. Nat Commun. 2019;10(1):4410."
    doi: "10.1038/s41467-019-12297-0"
    pmid: "31562337"
    url: "https://doi.org/10.1038/s41467-019-12297-0"
cross_links:
  - target: 01-human/03-molecular/brca1
    relation: connects-to
    note: "BRCA1 promotes resection (via CtIP) and recruits BRCA2 (via PALB2) → RAD51 loading at DSBs; BRCA1-mutant cells fail to form RAD51 foci → defective HR → error-prone NHEJ → genome instability and PARP inhibitor synthetic lethality."
  - target: 01-human/03-molecular/p53
    relation: connects-to
    note: "p53 represses RAD51 transcription via p53-binding site in the RAD51 promoter; p53 loss → elevated RAD51 → enhanced HR → genome plasticity; RAD51 overexpression in p53-null cancers promotes survival under replication stress from oncogene activation."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Autophagy and HR are co-regulated in the DNA damage response; in BRCA1/2-mutant tumors, autophagy inhibition combined with PARP inhibition shows synergistic lethality — autophagy sustains tumor viability under HR-deficiency-induced replication stress."
---

# RAD51

## Overview

**RAD51** is the primary recombinase of mammalian **homologous recombination (HR)** — the high-fidelity DNA double-strand break (DSB) repair pathway that uses an intact sister chromatid as a template for error-free repair. The direct eukaryotic homolog of bacterial RecA, RAD51 forms a helical nucleoprotein filament on single-stranded DNA (ssDNA) at resected DSB ends and catalyzes the central chemical step of HR: **strand invasion** of the homologous duplex and **strand exchange** to initiate repair synthesis.

RAD51 is at the intersection of genome stability, cancer susceptibility, and therapeutic resistance:
- **BRCA2** is the primary RAD51 loader — it displaces RPA (replication protein A, which coats resected ssDNA) and facilitates RAD51 filament formation [^pellegrini-2002-brca2-rad51]
- **BRCA1** acts upstream by promoting DNA end resection and recruiting PALB2 → BRCA2 → RAD51
- Loss of BRCA1/2 → impaired RAD51 loading → HR deficiency → synthetic lethality with PARP inhibitors
- **RAD51 overexpression** (in some cancers) → enhanced HR → resistance to DNA-damaging agents (cisplatin, olaparib) and radiation — a therapeutic challenge
- **RAD51 inhibitors** (RI-1, B02, CAM833) — in preclinical/early clinical development to sensitize HR-proficient cancers to DNA damage

## Structure

### RAD51 protein [^baumann-1996-rad51]

RAD51 is a **339 amino acid, 37 kDa ATPase** belonging to the RecA/RAD51 superfamily — the most evolutionarily conserved DNA repair proteins:

- **N-terminal domain (aa 1-97):** Winged-helix domain; mediates RAD54 binding; not required for ssDNA binding but important for filament stability and HR regulation; also mediates self-assembly into rings (inactive state)
- **ATPase domain (aa 97-339):** RecA fold (P-loop ATPase); contains:
  - **Walker A motif (P-loop, aa 130-138):** ATP phosphate binding (GxxxxGKT)
  - **Walker B motif:** ATP hydrolysis coordination (DExH/D)
  - **L1 loop:** DNA binding; contacts phosphate backbone of ssDNA
  - **L2 loop:** DNA binding and strand exchange; Tyr315 in L2 critical for strand exchange activity
  - **Rad51-specific insert (BRC-binding region):** The surface recognized by BRCA2 BRC repeats

**Filament assembly:**
- RAD51 monomers assemble on ssDNA in the presence of ATP → right-handed helical filament; ~6.4 Å rise per monomer, 6 monomers/helical repeat; extends DNA by ~50% relative to B-form dsDNA
- ATP hydrolysis after strand exchange → filament disassembly (RAD54 ATPase accelerates disassembly)
- The presynaptic filament is the catalytically active form: ssDNA-RAD51-ATP → searches dsDNA for homology by 3D diffusion and 1D sliding

### BRCA2-RAD51 interaction [^pellegrini-2002-brca2-rad51]

BRCA2 (3418 aa) has **8 BRC repeats** (aa 1002-2085) and a **C-terminal DNA binding domain (OB folds)**:
- Each BRC repeat (~35 aa) mimics a RAD51 interface motif → binds the RAD51 monomer-monomer interface in the filament → sequesters RAD51 monomers → allows regulated delivery to RPA-coated ssDNA at the DSB
- BRCA2 delivers RAD51 to RPA-ssDNA → RAD51 displaces RPA → forms presynaptic filament
- Crystal structure (Pellegrini 2002): BRC4 repeat of human BRCA2 mimicking a RAD51 monomer-monomer contact → explains how BRC repeats chaperone RAD51 without inhibiting filament assembly once at ssDNA

**Fanconi anemia and RAD51 paralogs:**
- RAD51 paralogs (RAD51B, RAD51C, RAD51D, XRCC2, XRCC3): form BCDX2 and CX3 complexes → assist RAD51 filament assembly, stabilization, and disassembly; mutations in RAD51C and RAD51D → Fanconi anemia complementation groups O/R and elevated ovarian cancer risk

## Function

### The HR mechanism: RAD51 at center stage

After DSB formation (by ionizing radiation, replication fork collapse, topoisomerase II, chemotherapy):

1. **DSB recognition:** MRN (MRE11-RAD50-NBS1) senses DSB → ATM activation → γH2AX spreading (Mb-scale)
2. **Resection:** CtIP (BRCA1-stimulated) → short-range resection; ExoI/BLM-RPA → long-range ssDNA (1-5 kb); RPA coats ssDNA → activates ATR-ATRIP
3. **BRCA1/PALB2/BRCA2 cascade:** BRCA1 recruits PALB2 → PALB2 bridges to BRCA2 → BRCA2 BRC repeats engage RAD51 monomers → BRCA2 delivers RAD51 to RPA-ssDNA → RPA displaced → **RAD51 presynaptic filament**
4. **Strand invasion:** RAD51 filament searches homologous dsDNA (sister chromatid in S/G2 phase) → finds homology → strand invasion → displacement loop (D-loop) formation; requires RAD54 (ATP-dependent chromatin remodeling and filament disassembly stimulation)
5. **DNA synthesis:** D-loop → 3' end primed → DNA synthesis by Polδ/ε → restore missing sequence
6. **Resolution:** SDSA (synthesis-dependent strand annealing, no crossover → predominant in somatic cells) or dHJ (double Holliday junction resolution, can produce crossovers → important in meiosis)

**Cell cycle restriction of HR:** HR requires a sister chromatid → restricted to S and G2 phases; CDK2 phosphorylates CtIP → promotes resection; CDK1 phosphorylates BRCA1 → RAD51 loading; in G1 → NHEJ dominates; in S/G2 → HR preferred

### RAD51 at stalled replication forks [^mason-2019-rad51-inhibitor]

RAD51 has critical **non-catalytic roles** at stalled replication forks beyond DSB repair:
- RAD51 filament stabilizes the nascent strand on stalled forks → **fork protection** against MRE11-mediated nucleolytic degradation ("fork reversal stabilization")
- BRCA2-deficient cells: RAD51 not loaded correctly → unprotected forks → MRE11 degrades nascent strands → genome instability even without DSBs
- Implication: some BRCA2-mutant cancer chemosensitivity arises from fork protection failure, not just HR deficiency

### RAD51 in cancer

**RAD51 overexpression:**
- Observed in breast, lung, head and neck, pancreatic cancers — often correlates with TP53 mutation (p53 represses RAD51 transcription; p53 loss → elevated RAD51)
- Enhanced HR in RAD51-overexpressing cancers → resistance to:
  - Platinum-based chemotherapy (cisplatin, carboplatin — induce crosslinks repaired by HR)
  - PARP inhibitors (enhanced HR bypasses PARP-inhibitor-induced SSBs)
  - Radiation therapy

**BRCA1/2-mutant (HR-deficient) tumors:**
- Impaired RAD51 foci formation at DSBs is the **functional biomarker of HR deficiency**
- **RAD51 foci assay:** Cells with hydroxyurea-induced DSBs → immunofluorescence for RAD51 foci → ≥5 foci in >10% of cells = HR proficient; used in clinical trials to predict PARP inhibitor sensitivity beyond BRCA mutation status
- **Reversion mutations:** BRCA1/2-mutant cancers under PARP inhibitor selection pressure develop reversion mutations (restoring BRCA1/2 reading frame) → RAD51 loading restored → HR active → PARP inhibitor resistance; or RAD51 paralogs or other HR factors compensate

## Mechanism

### Strand exchange mechanism

The RAD51-catalyzed strand exchange reaction is a multi-step process:
1. **Presynaptic assembly:** RAD51 + ATP binds ssDNA → extended helical filament (~41 Å pitch, ~100 Å diameter); ATP-RAD51 binds ssDNA tighter than ADP-RAD51
2. **Homology search:** RAD51-ssDNA filament samples dsDNA by Brownian motion → identifies complementary 8-nt segments ("sampling windows") → 3D diffusion to find homology
3. **Strand invasion:** Complementary ssDNA base-pairs with one strand of dsDNA → displaces other strand → D-loop formation → heteroduplex DNA
4. **Branch migration:** RAD54 translocase moves D-loop → extends heteroduplex → allows polymerase access
5. **Disassembly:** ATP hydrolysis → RAD51 undergoes conformational change → filament disassembly; RAD54 and anti-recombinase helicases (FANCM, RTEL1) disassemble RAD51 from dsDNA

### Therapeutic targeting

**RAD51 inhibitors in development:**
- **RI-1 (RAD51 inhibitor 1):** Covalently alkylates RAD51 Cys319 → disrupts RAD51 oligomerization → impairs filament formation; sensitizes cells to cisplatin and PARP inhibitors in vitro
- **B02:** Non-covalent; inhibits RAD51-ssDNA binding by binding RAD51 protein; reduces HR by ~60-75% in human cell lines; sensitizes cancer cells to cisplatin and doxorubicin
- **CAM833:** Disrupts RAD51-BRCA2 BRC interaction → impairs RAD51 loading at DSBs; structure-guided optimization ongoing

**Rationale for combination therapy:**
- HR-proficient tumors (expressing RAD51 normally) are resistant to PARP inhibitors → combine RAD51 inhibitor + PARP inhibitor → create "BRCAness" phenotype in HR-proficient tumors → extend PARP inhibitor utility beyond BRCA-mutant cancers
- Radiation + RAD51 inhibitor: impairs HR-mediated repair of radiation-induced DSBs → radiosensitization in brain tumors (preclinical GBM models)

## Connections

- `connects-to` → **[BRCA1](../brca1/README.md)** — BRCA1 promotes DNA end resection and recruits PALB2 → BRCA2 → RAD51; BRCA1-mutant cells fail to form RAD51 foci at DSBs → defective HR → genome instability and PARP inhibitor sensitivity.
- `connects-to` → **[p53](../p53/README.md)** — p53 represses RAD51 transcription; p53 loss → elevated RAD51 → enhanced HR → genome plasticity; paradoxically, RAD51 overexpression in p53-null cancers promotes aberrant HR contributing to chromosomal rearrangements.
- `connects-to` → **[Autophagy](../autophagy/README.md)** — autophagy and HR share regulation in the DNA damage response; in BRCA1/2-mutant tumors, autophagy inhibition combined with PARP inhibition shows synergistic lethality, suggesting autophagy sustains viability under HR-deficiency-induced stress.

[^baumann-1996-rad51]: Baumann P, Benson FE, West SC. Human Rad51 protein promotes ATP-dependent homologous pairing and strand transfer reactions in vitro. *Cell.* 1996;87(4):757-766. [doi:10.1016/S0092-8674(00)81394-X](https://doi.org/10.1016/S0092-8674(00)81394-X) · [PubMed 8929543](https://pubmed.ncbi.nlm.nih.gov/8929543/)
[^pellegrini-2002-brca2-rad51]: Pellegrini L, Yu DS, Lo T, et al. Insights into DNA recombination from the structure of a RAD51-BRCA2 complex. *Nature.* 2002;420(6913):287-293. [doi:10.1038/nature01230](https://doi.org/10.1038/nature01230) · [PubMed 12442171](https://pubmed.ncbi.nlm.nih.gov/12442171/)
[^mason-2019-rad51-inhibitor]: Mason JM, Chan YL, Weichselbaum RW, Bishop DK. Non-enzymatic roles of human RAD51 at stalled replication forks. *Nat Commun.* 2019;10(1):4410. [doi:10.1038/s41467-019-12297-0](https://doi.org/10.1038/s41467-019-12297-0) · [PubMed 31562337](https://pubmed.ncbi.nlm.nih.gov/31562337/)
