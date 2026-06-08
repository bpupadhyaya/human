---
schema: human-scale-entry/v1
id: immunoglobulin-g
name: Immunoglobulin G
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-04
summary: "Y-shaped tetrameric antibody (2 heavy + 2 light chains) — the most abundant serum immunoglobulin (~10–15 mg/mL), with ~21-day half-life. Four subclasses (IgG1–4). Principal mediator of humoral immunity and vaccine-elicited protection."
aliases: ["IgG", "gamma-globulin", "antibody IgG"]
sources:
  - id: abbas-immunology-9e
    type: textbook
    cite: "Abbas AK, Lichtman AH, Pillai S. Cellular and Molecular Immunology. 9th ed. Elsevier; 2018."
    url: "https://www.elsevier.com/books/cellular-and-molecular-immunology/abbas/978-0-323-52323-3"
    accessed: "2026-06-04"
  - id: schroeder-cavacini-2010-igg
    type: peer-reviewed
    cite: "Schroeder HW Jr, Cavacini L. Structure and function of immunoglobulins. J Allergy Clin Immunol. 2010;125(2 Suppl 2):S41-52."
    doi: "10.1016/j.jaci.2009.09.046"
    pmid: "20176268"
  - id: ward-bhatt-2020-fcrn
    type: peer-reviewed
    cite: "Ward ES, Bhatt DL, Bhatt DL, et al. The role of FcRn in immunity and its therapeutic implications. Nat Rev Immunol. 2020;20(7):399-407."
    doi: "10.1038/s41577-019-0260-y"
    pmid: "32015434"
  - id: subbarao-2021-vaccine-igg
    type: peer-reviewed
    cite: "Subbarao K. The success of SARS-CoV-2 vaccines and prospects for the future. Nat Rev Immunol. 2021;21(8):469-470."
    doi: "10.1038/s41577-021-00573-4"
    pmid: "34155386"
  - id: who-igg-reference
    type: regulatory
    cite: "World Health Organization. The WHO International Standard for anti-SARS-CoV-2 immunoglobulin. WHO/BS/2020.2403."
    url: "https://www.who.int/publications/m/item/WHO-BS-2020.2403"
    accessed: "2026-06-04"
cross_links:
  - target: 01-human/04-cellular/plasma-cell
    relation: expressed-by
    note: "IgG is produced and secreted by terminally differentiated plasma cells; long-lived plasma cells in bone marrow maintain durable serum IgG titers."
  - target: 02-pathogen/01-viruses/sars-cov-2
    relation: targets
    note: "Vaccine-elicited and infection-induced IgG binds SARS-CoV-2 spike protein, neutralizing virus entry and mediating ADCC via FcγRIII on NK cells and macrophages."
  - target: 02-pathogen/01-viruses/influenza-a
    relation: targets
    note: "Anti-hemagglutinin IgG prevents receptor binding; anti-neuraminidase IgG limits viral spread; both contribute to sterilizing immunity after vaccination."
  - target: 01-human/07-system/immune-system
    relation: part-of
    note: "IgG is the principal soluble effector molecule of the humoral adaptive immune system, circulating in blood and extravascular spaces."
  - target: 02-pathogen/01-viruses/hiv-1
    relation: targets
    note: "Neutralizing IgG targeting HIV-1 gp120/gp41 provides partial protection; broadly neutralizing antibodies (bNAbs) against the CD4-binding site and V3 loop are under investigation for prevention and therapy."
  - target: 02-pathogen/01-viruses/hepatitis-b-virus
    relation: targets
    note: "Anti-HBsAg IgG (anti-HBs titer ≥10 mIU/mL) is the correlate of protection from HBV vaccination; anti-HBc IgG marks prior infection; therapeutic monoclonal anti-HBs (HBIG) is used for post-exposure prophylaxis."
  - target: 02-pathogen/02-bacteria/streptococcus-pneumoniae
    relation: targets
    note: "Serotype-specific IgG against the pneumococcal polysaccharide capsule is the primary correlate of vaccine-mediated protection; PCV13-elicited T-dependent IgG persists longer than PPSV23-elicited T-independent responses."
  - target: 01-human/07-system/myasthenia-gravis
    relation: connects-to
    note: "Anti-AChR IgG1/IgG3 and anti-MuSK IgG4 are pathogenic in MG; IgG1/IgG3 activate complement → MAC-mediated AChR destruction; IgG4 blocks MuSK function; FcRn inhibitors (efgartigimod, rozanolixizumab) reduce total IgG including pathogenic anti-AChR antibodies."
  - target: 01-human/03-molecular/fcrn
    relation: connects-to
    note: "FcRn rescues IgG from lysosomal degradation by pH-dependent binding in endosomes → IgG t½ ~21 days; FcRn inhibitors (efgartigimod, rozanolixizumab) compete for or block FcRn → accelerate IgG catabolism → reduce pathogenic IgG titers in MG, ITP, pemphigus, and CIDP."
  - target: 01-human/07-system/immune-thrombocytopenia
    relation: connects-to
    note: "Anti-GPIIb/IIIa IgG1/IgG3 and anti-GPIb/IX IgG are pathogenic in ITP; opsonizes platelets for FcγRIII-mediated splenic phagocytosis; IVIG blocks Fc receptors; FcRn inhibitors (efgartigimod; FDA Jun 2023) reduce total IgG including anti-platelet antibodies."
  - target: 01-human/07-system/cidp
    relation: connects-to
    note: "IVIG (2 g/kg loading; 1 g/kg q4w) is first-line CIDP therapy; pathogenic IgG4 anti-NF155 and anti-CNTN1 disrupt paranodal axo-glial junctions; FcRn inhibitors (efgartigimod ADHERE; FDA Jun 2024) reduce total IgG catabolism → lower anti-paranodal antibody titers."
  - target: 01-human/07-system/dermatomyositis
    relation: connects-to
    note: "IVIG (2 g/kg monthly; FDA Oct 2021) is the first approved DM therapy (ProDERM: CDASI-A improvement 58% vs 29%); MSA autoantibodies (anti-MDA5, anti-TIF1γ, anti-NXP2, anti-Mi-2) are IgG subclasses that stratify DM subtypes and prognosis."
  - target: 01-human/07-system/anca-vasculitis
    relation: connects-to
    note: "Anti-PR3 IgG (c-ANCA) and anti-MPO IgG (p-ANCA) are pathogenic in GPA and MPA; IgG crosslinks surface PR3/MPO on C5a-primed neutrophils → FcγRIIa activation → NETosis → pauci-immune vasculitis; rituximab (RAVE; FDA Apr 2011) depletes B cells producing pathogenic ANCA IgG."
---

# Immunoglobulin G

## Overview

Immunoglobulin G (IgG) is the most abundant antibody class in human serum and the primary mediator of long-term humoral immunity [^schroeder-cavacini-2010-igg]. At a steady-state concentration of approximately 10–15 mg/mL, it constitutes roughly 75 % of all serum immunoglobulins in healthy adults. IgG is the antibody that crosses the placenta to confer passive neonatal immunity, that fixes complement to opsonize pathogens, that engages Fc receptors on effector cells to trigger antibody-dependent cellular cytotoxicity (ADCC), and that is the direct molecular target of modern mRNA vaccine design — the goal of BNT162b2 and mRNA-1273 against SARS-CoV-2 spike is precisely the elicitation of durable, high-affinity IgG titers [^subbarao-2021-vaccine-igg].

Four subclasses exist — IgG1, IgG2, IgG3, and IgG4 — each with distinct heavy-chain constant regions, effector-function profiles, and typical abundance. IgG1 is the most prevalent (~60 % of total IgG) and the most potent activator of complement and ADCC; IgG3 has the strongest complement activation but a shorter half-life; IgG2 is the major subclass responding to polysaccharide antigens; IgG4 is poorly functional in complement activation but is induced by chronic antigen exposure.

## Structure

### Domain architecture

IgG is a **tetrameric glycoprotein** consisting of two identical heavy chains (γ-chains, ~50 kDa each) and two identical light chains (κ or λ, ~25 kDa each), joined by disulfide bonds and non-covalent interactions into a Y-shaped molecule with a total molecular weight of approximately 150 kDa [^schroeder-cavacini-2010-igg].

| Region | Chains | Domains | Function |
|:---|:---|:---|:---|
| **Fab** (fragment antigen-binding) | VH + CH1 + VL + CL | VH, VL (CDRs contact antigen); CH1, CL | Antigen binding; two per molecule |
| **Hinge** | Heavy chain only | Flexible proline/cysteine-rich sequence | Connects Fab to Fc; allows Fab arm articulation; inter-heavy-chain disulfide bonds here |
| **Fc** (fragment crystallizable) | Two CH2 + two CH3 | CH2: complement (C1q) and FcγR binding; CH3: FcRn binding | Effector functions; half-life regulation |

### Binding sites

Each Fab arm contains a **complementarity-determining region (CDR)** — six hypervariable loops (three on VH, three on VL) that fold together to form the antigen-binding site. CDR3 of VH is the most variable and typically the key contact with epitope. The two Fab arms move independently on the flexible hinge, allowing bivalent crosslinking of antigen arrays (e.g., repeating epitopes on viral coat proteins).

### Glycosylation

A single N-linked oligosaccharide at Asn297 of each CH2 domain is **essential** for Fc effector function. The glycan composition (sialylation, fucosylation, galactosylation) modulates C1q binding, FcγR affinity, and — importantly — anti-inflammatory vs. pro-inflammatory bias. Vaccines and therapeutic antibodies are engineered for specific glycoforms to tune these properties.

### FcRn — the half-life recycling receptor

The neonatal Fc receptor (FcRn) is responsible for the extraordinarily long ~21-day serum half-life of IgG. In acidic endosomes of vascular endothelial cells, FcRn binds Fc at histidines 310 and 435 of each CH2–CH3 interface [^ward-bhatt-2020-fcrn]. This rescues IgG from lysosomal degradation; at neutral pH at the cell surface, the lower affinity releases IgG back into circulation. This salvage mechanism is the basis for prolonged therapeutic antibody half-lives and underpins strategies to engineer long-lasting vaccine-elicited titers.

## Function

### Neutralization

IgG neutralizes pathogens by:
- **Steric blockade** — Fab arms physically block receptor-binding domains (e.g., SARS-CoV-2 RBD binding to ACE2; influenza HA binding to sialic acid).
- **Aggregation** — bivalent IgG can crosslink virions or bacteria, reducing effective infectious dose.
- **Conformational disruption** — some epitopes, when bound, lock surface proteins in non-functional states (class I/II/III neutralizing antibodies against spike).

### Opsonization and phagocytosis

IgG-coated particles are recognized by FcγRI (CD64), FcγRII (CD32), and FcγRIII (CD16) on macrophages and neutrophils. Engagement triggers internalization (phagocytosis) and respiratory burst.

### Complement activation

IgG1 and IgG3 (especially arrays cross-linked by antigen) bind C1q in the CH2 region, activating the classical complement pathway. This generates the membrane attack complex (MAC) for direct pathogen lysis and deposits C3b for complement-mediated opsonization.

### ADCC — antibody-dependent cellular cytotoxicity

Fc tails of IgG bound to target cells (e.g., virus-infected cells displaying spike on surface) engage FcγRIII (CD16) on NK cells. NK cells are activated and release perforin and granzymes, lysing the infected cell without the NK cell needing to recognize MHC.

### Placental transfer

IgG is the only antibody class that crosses the placenta via FcRn expressed on syncytiotrophoblasts. Maternal IgG protects the neonate from birth until the infant's own adaptive immunity matures (~6 months). This is why maternal vaccination during pregnancy (influenza, pertussis, COVID-19) is recommended.

## Mechanism

### Class-switch recombination and somatic hypermutation

IgG arises in germinal centers when antigen-activated B cells (initially producing IgM) undergo:
1. **Class-switch recombination (CSR)** — AID (activation-induced cytidine deaminase) introduces double-strand breaks at switch regions upstream of Cγ constant genes; VDJ exon is recombined to lie upstream of Cγ rather than Cμ. CD40L from Tfh and cytokines (IL-4 → IgG1/IgE; IFN-γ → IgG3/IgG2a in mice; complex in humans) specify which IgG subclass is produced.
2. **Somatic hypermutation (SHM)** — AID introduces point mutations in the V regions at high rate (~10⁻³/bp/division, 10⁶× baseline). B cell clones with higher-affinity BCRs outcompete others for limiting antigen on follicular dendritic cells — **affinity maturation**. The result is IgG with dissociation constants often in the picomolar to nanomolar range, far higher than the naïve IgM precursor.

### FcγR signaling

FcγRI and FcγRIII contain ITAMs (immunoreceptor tyrosine-based activation motifs) in their cytoplasmic tails or associated γ-chains. Crosslinking by IgG-immune complexes triggers Syk kinase activation, PLCγ, Ca²⁺ flux, and downstream gene activation for phagocytosis, cytokine release, or degranulation. FcγRIIB is an inhibitory receptor bearing an ITIM — the balance of activating vs. inhibitory FcγR engagement shapes the magnitude of the response.

## Connections

- **Produced by:** [plasma-cell](../../04-cellular/plasma-cell/README.md) (expressed-by)
- **Targets:** [sars-cov-2](../../../../02-pathogen/01-viruses/sars-cov-2/README.md) — spike-targeting IgG is the protective correlate of COVID-19 vaccination
- **Targets:** [influenza-a](../../../../02-pathogen/01-viruses/influenza-a/README.md) — anti-HA and anti-NA IgG drive vaccine protection
- **Part of:** [immune-system](../../07-system/immune-system/README.md) — key circulating humoral effector
- `connects-to` → **[Myasthenia Gravis](../../07-system/myasthenia-gravis/README.md)** — Anti-AChR IgG1/IgG3 and anti-MuSK IgG4 are pathogenic in MG; IgG1/IgG3 activate complement → MAC-mediated AChR destruction; IgG4 blocks MuSK function; FcRn inhibitors (efgartigimod, rozanolixizumab) reduce total IgG including pathogenic anti-AChR antibodies.
- `connects-to` → **[FcRn](../fcrn/README.md)** — FcRn rescues IgG from lysosomal degradation by pH-dependent binding in endosomes → IgG t½ ~21 days; FcRn inhibitors (efgartigimod, rozanolixizumab) compete for or block FcRn → accelerate IgG catabolism → reduce pathogenic IgG titers in MG, ITP, pemphigus, and CIDP.
- `connects-to` → **[Immune Thrombocytopenia](../../07-system/immune-thrombocytopenia/README.md)** — Anti-GPIIb/IIIa IgG1/IgG3 and anti-GPIb/IX IgG are pathogenic in ITP; opsonizes platelets for FcγRIII-mediated splenic phagocytosis; IVIG blocks Fc receptors; FcRn inhibitors (efgartigimod; FDA Jun 2023) reduce total IgG including anti-platelet antibodies.
- `connects-to` → **[CIDP](../../07-system/cidp/README.md)** — IVIG (2 g/kg; ICE trial Lancet Neurol 2008) is first-line CIDP therapy; pathogenic IgG4 anti-NF155 and anti-CNTN1 disrupt paranodal junctions; FcRn inhibitors (efgartigimod ADHERE; FDA Jun 2024) reduce total IgG catabolism.
- `connects-to` → **[Dermatomyositis](../../07-system/dermatomyositis/README.md)** — IVIG (2 g/kg monthly; FDA Oct 2021) is the first approved DM therapy (ProDERM: CDASI-A improvement 58% vs 29%); MSA autoantibodies (anti-MDA5, anti-TIF1γ, anti-NXP2, anti-Mi-2) are IgG subclasses that stratify DM subtypes and prognosis.
- `connects-to` → **[ANCA Vasculitis](../../07-system/anca-vasculitis/README.md)** — Anti-PR3 IgG (c-ANCA) and anti-MPO IgG (p-ANCA) are pathogenic in GPA and MPA; IgG crosslinks surface PR3/MPO on C5a-primed neutrophils → FcγRIIa activation → NETosis → pauci-immune vasculitis; rituximab (RAVE; FDA Apr 2011) depletes B cells producing pathogenic ANCA IgG.

[^schroeder-cavacini-2010-igg]: Schroeder HW Jr, Cavacini L. Structure and function of immunoglobulins. *J Allergy Clin Immunol.* 2010;125(2 Suppl 2):S41-52. [doi:10.1016/j.jaci.2009.09.046](https://doi.org/10.1016/j.jaci.2009.09.046) · [PubMed 20176268](https://pubmed.ncbi.nlm.nih.gov/20176268/)
[^ward-bhatt-2020-fcrn]: Ward ES, Bhatt DL, et al. The role of FcRn in immunity and its therapeutic implications. *Nat Rev Immunol.* 2020;20(7):399-407. [doi:10.1038/s41577-019-0260-y](https://doi.org/10.1038/s41577-019-0260-y) · [PubMed 32015434](https://pubmed.ncbi.nlm.nih.gov/32015434/)
[^subbarao-2021-vaccine-igg]: Subbarao K. The success of SARS-CoV-2 vaccines and prospects for the future. *Nat Rev Immunol.* 2021;21(8):469-470. [doi:10.1038/s41577-021-00573-4](https://doi.org/10.1038/s41577-021-00573-4) · [PubMed 34155386](https://pubmed.ncbi.nlm.nih.gov/34155386/)
[^abbas-immunology-9e]: Abbas AK, Lichtman AH, Pillai S. *Cellular and Molecular Immunology.* 9th ed. Elsevier; 2018.
[^who-igg-reference]: World Health Organization. The WHO International Standard for anti-SARS-CoV-2 immunoglobulin. WHO/BS/2020.2403. [Read online →](https://www.who.int/publications/m/item/WHO-BS-2020.2403)
