---
schema: human-scale-entry/v1
id: norovirus-vp1
name: Norovirus VP1
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-08
summary: "Norovirus VP1 (530 aa; T=3 icosahedral; 90 dimers) is the major capsid protein with S-domain (inner shell) and P-domain (P1/P2); P2 subdomain binds HBGAs (FUT2 H antigen) and carries all major neutralizing epitopes; GII.4 P2 antigenic drift drives pandemic emergence."
aliases: ["VP1", "norovirus capsid protein", "norovirus VP1", "VP1 P-domain", "NV VP1", "Norwalk VP1", "GII.4 VP1", "norovirus VLP"]
sources:
  - id: prasad-1999-norwalk-structure
    type: peer-reviewed
    cite: "Prasad BVV, Hardy ME, Dokland T, Bella J, Rossmann MG, Estes MK. X-ray crystallographic structure of the Norwalk virus capsid. Science. 1999;286(5438):287-290."
    doi: "10.1126/science.286.5438.287"
    pmid: "10514371"
    url: "https://doi.org/10.1126/science.286.5438.287"
    accessed: "2026-06-08"
  - id: tan-2005-hbga-review
    type: peer-reviewed
    cite: "Tan M, Jiang X. Norovirus and its histo-blood group antigen receptors: an answer to a historical puzzle. Trends Microbiol. 2005;13(6):285-293."
    doi: "10.1016/j.tim.2005.04.005"
    pmid: "15936186"
    url: "https://doi.org/10.1016/j.tim.2005.04.005"
    accessed: "2026-06-08"
  - id: lindesmith-2008-gii4-evolution
    type: peer-reviewed
    cite: "Lindesmith LC, Costantini V, Swanstrom J, et al. Emergence of a norovirus GII.4 strain correlates with changes in evolving blockade epitopes. J Virol. 2008;82(23):11648-11660."
    doi: "10.1128/JVI.01566-08"
    pmid: "18842720"
    url: "https://doi.org/10.1128/JVI.01566-08"
    accessed: "2026-06-08"
  - id: bhatt-2024-norovirus-vaccine
    type: peer-reviewed
    cite: "Atmar RL, Bernstein DI, Harro CD, et al. Norovirus vaccine against experimental human GI.1 illness. N Engl J Med. 2011;365(23):2178-2187."
    doi: "10.1056/NEJMoa1101245"
    pmid: "22150036"
    url: "https://doi.org/10.1056/NEJMoa1101245"
    accessed: "2026-06-08"
cross_links:
  - target: 01-human/07-system/norovirus
    relation: connects-to
    note: "VP1 P2 subdomain mediates HBGA binding on intestinal epithelium and B cells; GII.4 pandemic strains arise from P2 antigenic drift enabling herd immunity escape; all norovirus VLP vaccines (TAK-214, HIL-214) and mRNA vaccines (mRNA-1403) encode VP1 as the sole immunogen."
  - target: 01-human/04-cellular/b-cell
    relation: connects-to
    note: "Norovirus VP1 P2 subdomain binds HBGA-like carbohydrates on B cell surfaces → direct B cell infection (Jones 2014); anti-VP1 secretory IgA is the primary correlate of protection; blocking anti-VP1 IgA is the endpoint of all norovirus vaccine trials."
  - target: 01-human/03-molecular/rsv-f-protein
    relation: connects-to
    note: "Both norovirus VP1 and RSV F are sole viral surface antigens serving as vaccine immunogens; mRNA-LNP encodes both (mRNA-1403/norovirus; mResvia/RSV); VP1 VLP self-assembly and DS-Cav1 RSV-F proline locking are parallel structure-based vaccine design strategies."
---

# Norovirus VP1

## Overview

**Norovirus VP1** is the major (and sole neutralization-relevant) structural protein of the norovirus virion. As a **homotrimeric — actually homodimeric** building block, VP1 self-assembles into the T=3 icosahedral capsid that encloses the ~7.7 kb +ssRNA genome. VP1 simultaneously performs three critical functions: (1) forming the protective capsid shell; (2) mediating attachment to host cell surface receptors (histo-blood group antigens, HBGAs); and (3) serving as the target of all neutralizing antibodies and the immunogen for all vaccine candidates in development.

The first high-resolution structure of Norwalk virus (GI.1) VP1 was obtained by X-ray crystallography at 3.4 Å by Prasad et al. in 1999 [^prasad-1999-norwalk-structure], revealing the S-domain/P-domain architecture that is now understood to define all calicivirus capsid proteins. Subsequent cryo-EM and crystallography studies of GII.4 and other genotypes defined the HBGA binding sites in the hypervariable P2 subdomain [^tan-2005-hbga-review], explaining the molecular basis of secretor-status-dependent susceptibility and the antigenic evolution underlying successive GII.4 pandemic waves [^lindesmith-2008-gii4-evolution].

## Structure

### Domain architecture

VP1 (~530 aa in GI.1 Norwalk; varies slightly by genotype) consists of two major structural domains:

| Domain | Residue range (approx., GI.1) | Structure | Function |
|:---|:---|:---|:---|
| **Shell (S) domain** | 1–225 | β-jellyroll fold; highly conserved within genogroup | Forms the icosahedral T=3 inner shell; mediates VP1 dimerization at the quasi-3-fold symmetry axes; preserves overall capsid geometry |
| **P1 subdomain** | 226–278, 399–520 (discontinuous) | Extended β-barrel; flanks P2 | Moderately conserved; cross-reactive antibody epitopes; forms the arch-like protrusion stalk; dimerization contacts |
| **P2 subdomain** | 279–398 (approx.) | β-barrel, protruding outward | Hypervariable across genotypes; outermost capsid surface; carries HBGA binding pocket; dominant neutralizing antibody target |

**Capsid assembly:** 180 VP1 monomers associate as 90 dimers to form the T=3 icosahedron (~38 nm outer diameter). Three quasi-equivalent VP1 positions in the asymmetric unit (A, B, C) create the icosahedral lattice. The P-domain dimers project outward from the shell, forming the arch-like protrusions visible in cryo-EM reconstructions.

**VP2 minor capsid protein:** ~1–4 copies of VP2 per virion are located internally, interacting with the VP1 S-domain and genome RNA. VP2 enhances VP1 stability and capsid assembly efficiency; its basic N-terminus may facilitate RNA packaging.

### Virus-like particles (VLPs)

When VP1 is expressed in baculovirus (Sf9 cells) or mammalian cells (HEK293), it self-assembles into **VLPs** (virus-like particles) that are structurally and antigenically indistinguishable from native virions but lack the RNA genome — rendering them non-infectious. VLPs:
- Are the basis of VLP-based vaccine candidates (TAK-214, HIL-214)
- Display authentic HBGA-binding conformation and native neutralizing epitopes
- Elicit strong mucosal IgA and systemic IgG responses in clinical trials
- Can be produced as bivalent formulations (GI.1 + GII.4 VLPs)

### Glycan features

VP1 carries **2-3 N-linked glycosylation sites** depending on genotype; glycosylation is less extensive than influenza HA or HIV gp120 — there is no dense "glycan shield." Most of the VP1 surface is protein-accessible to antibodies, explaining why VLPs are highly immunogenic and why anti-P2 antibodies can efficiently block HBGA binding.

## Function

### HBGA binding

The P2 subdomain contains the **HBGA binding site** — a shallow pocket on the outermost surface of each P-domain protrusion [^tan-2005-hbga-review]:

- **GII.4 HBGAs bound:** H-type 1, H-type 3, Lewis b, A antigen, B antigen
- **GI.1 (Norwalk) HBGAs bound:** H-type 1, H-type 3, A antigen (Lewis b and GII-type HBGAs not bound)
- **Secretor status:** FUT2 (α-1,2-fucosyltransferase) generates the H antigen (α-1,2-linked fucose on type 1 chain Galβ1-3GlcNAc) — the primary HBGA for most GII.4 strains; FUT2 nonsecretors (~20% of Europeans, ~2% of Asians) lack gut H antigen → resistant to most GII.4 strains
- **Lewis blood group:** FUT3 generates Lewis a and Lewis b antigens; Lewis b (expressed on secretor intestinal epithelium) is bound by many GII and GI strains independently of ABO blood group

The HBGA binding interaction does not require a protein receptor analog — the carbohydrate alone is sufficient for initial attachment. The binding affinity is relatively low (Kd ~mM range for individual HBGA molecules, with avidity effects from multivalent VP1 protrusions enhancing effective binding to glycan-decorated cell surfaces).

### Immune recognition and neutralizing antibodies

VP1 is the **exclusive target of neutralizing antibodies** against norovirus. Antibody responses target primarily:

| Antigenic site | Location | Blocking mechanism |
|:---|:---|:---|
| **P2 HBGA-blocking antibodies** | P2 subdomain | Sterically block VP1-HBGA interaction → prevent cell attachment |
| **P1 cross-reactive antibodies** | P1 subdomain | Partially cross-reactive across genotypes; lower titer in most infected individuals |
| **S-domain antibodies** | S-domain | Accessible post-disassembly; non-neutralizing for intact virions |

**Blocking ELISA (HBGA blocking assay):** The primary surrogate neutralization assay for norovirus — measures ability of serum IgA or IgG to block VP1 VLP binding to synthetic HBGA-expressing red blood cells or HBGA-conjugated surfaces. 50% blocking titer (BT50) correlates with protection in human challenge studies.

**Correlate of protection:** Anti-VP1 serum IgA and stool/jejunal secretory IgA (sIgA) blocking titers correlate with reduced susceptibility to re-infection. The duration of immunity is limited — effective immunity wanes within 6–24 months, explaining why adults can be re-infected repeatedly over their lifetime.

## Mechanism

### GII.4 antigenic evolution [^lindesmith-2008-gii4-evolution]

GII.4 pandemic strain emergence follows a pattern analogous to influenza antigenic drift:

1. Circulating GII.4 variant accumulates new point mutations in P2 antigenic sites A, B, C, D, and E over 2–4 years
2. Sufficient P2 mutations cause reduced binding by existing anti-VP1 antibodies in seropositive individuals
3. A new pandemic variant emerges with sufficient antigenic distance to infect individuals immune to the prior variant
4. The new variant spreads globally within 6–12 months (GII.4 Sydney 2012, GII.4 Sydney 2015 successors)

**Key P2 antigenic sites:**
- **Site A** (~residues 294-298): Hypervariable; major determinant of GII.4 pandemic emergence
- **Site B** (~residues 333-336): Moderately variable; cross-reactive antibody targets
- **Site C/D** (~residues 370-378): HBGA binding-adjacent; mutations here alter both antigenicity and receptor specificity

This evolutionary pressure creates a vaccination challenge analogous to influenza seasonal strain updates — vaccine antigens may need updating as new GII.4 variants emerge, though GI.1 representation remains stable across decades.

### VLP vaccine immunogenicity

Intranasal or intramuscular administration of VP1 VLPs (±adjuvant) in human challenge studies:
- Elicits serum IgG anti-VP1 (geometric mean titer 4-10× over baseline)
- Elicits salivary and stool secretory IgA
- HBGA blocking titers achieved at BT50 >1:100 correlate with 47-64% reduction in illness in human challenge studies [^bhatt-2024-norovirus-vaccine]
- Immunity is detectable for 6 months to ≥2 years but wanes; booster strategies under investigation

**mRNA platform (mRNA-1403):** Moderna's bivalent mRNA-LNP encoding GI.1 + GII.4 VP1 shows robust VLP-specific IgG responses (>90% seroconversion) and HBGA blocking in Phase 1/2 — similar immunogenicity to VLP vaccines with the manufacturing advantage of mRNA platform scalability and potential for rapid updating with emerging GII.4 variants.

## Connections

**→ [Norovirus](../../../07-system/norovirus/)**: VP1 is the sole capsid protein and immunogen of norovirus; HBGA binding via the P2 subdomain initiates infection of gut enterocytes and B cells; GII.4 antigenic drift in VP1 P2 drives pandemic emergence every 2–4 years; VLP (TAK-214, HIL-214) and mRNA vaccines (mRNA-1403) both encode VP1 as primary immunogen.

**→ [B Cell](../../04-cellular/b-cell/)**: Norovirus VP1 binds HBGA-like carbohydrates on B cell surfaces enabling direct B cell infection (Jones 2014); B cells are required for the anti-VP1 IgA response that correlates with protection; anti-VP1 secretory IgA blocking titer is the primary immunological endpoint for all norovirus vaccine candidates.

**→ [RSV F Protein](../rsv-f-protein/)**: Both RSV F and Norovirus VP1 are the sole relevant surface antigens of their respective viruses and the basis of recently approved or late-stage vaccines; RSV uses prefusion-stabilized F protein (DS-Cav1) while norovirus uses VLP self-assembly of VP1 — both are structure-based vaccine design triumphs; mRNA-LNP platform encodes both antigens (mResvia = RSV F; mRNA-1403 = norovirus VP1).

[^prasad-1999-norwalk-structure]: Prasad BVV, Hardy ME, Dokland T, Bella J, Rossmann MG, Estes MK. X-ray crystallographic structure of the Norwalk virus capsid. *Science.* 1999;286(5438):287-290. [doi:10.1126/science.286.5438.287](https://doi.org/10.1126/science.286.5438.287) · [PubMed 10514371](https://pubmed.ncbi.nlm.nih.gov/10514371/)
[^tan-2005-hbga-review]: Tan M, Jiang X. Norovirus and its histo-blood group antigen receptors: an answer to a historical puzzle. *Trends Microbiol.* 2005;13(6):285-293. [doi:10.1016/j.tim.2005.04.005](https://doi.org/10.1016/j.tim.2005.04.005) · [PubMed 15936186](https://pubmed.ncbi.nlm.nih.gov/15936186/)
[^lindesmith-2008-gii4-evolution]: Lindesmith LC, Costantini V, Swanstrom J, et al. Emergence of a norovirus GII.4 strain correlates with changes in evolving blockade epitopes. *J Virol.* 2008;82(23):11648-11660. [doi:10.1128/JVI.01566-08](https://doi.org/10.1128/JVI.01566-08) · [PubMed 18842720](https://pubmed.ncbi.nlm.nih.gov/18842720/)
[^bhatt-2024-norovirus-vaccine]: Atmar RL, Bernstein DI, Harro CD, et al. Norovirus vaccine against experimental human GI.1 illness. *N Engl J Med.* 2011;365(23):2178-2187. [doi:10.1056/NEJMoa1101245](https://doi.org/10.1056/NEJMoa1101245) · [PubMed 22150036](https://pubmed.ncbi.nlm.nih.gov/22150036/)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
