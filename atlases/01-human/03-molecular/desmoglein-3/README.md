---
schema: human-scale-entry/v1
id: desmoglein-3
name: Desmoglein-3
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-07
summary: "Desmoglein-3 (DSG3; chr18q12.1) is a desmosomal cadherin in stratified epithelia; anti-Dsg3 IgG4 causes pemphigus vulgaris (mucosal) and anti-Dsg1 IgG4 causes pemphigus foliaceus (superficial). Rituximab (FDA 2018) and efgartigimod (FDA 2023) are approved treatments."
aliases: ["DSG3", "desmoglein-3", "desmoglein 3", "Dsg3", "anti-Dsg3", "pemphigus antigen"]
sources:
  - id: amagai-1991-dsg3-pemphigus
    type: peer-reviewed
    cite: "Amagai M, Klaus-Kovtun V, Stanley JR. Autoantibodies against a novel epithelial cadherin in pemphigus vulgaris, a disease of cell adhesion. Cell. 1991;67(5):869-877."
    doi: "10.1016/0092-8674(91)90360-B"
    pmid: "1959133"
    url: "https://doi.org/10.1016/0092-8674(91)90360-B"
  - id: joly-2017-rituximab-pemphix
    type: peer-reviewed
    cite: "Joly P, Maho-Vaillant M, Prost-Squarcioni C, et al. First-line rituximab combined with short-term prednisone versus prednisone alone for the treatment of pemphigus (Ritux 3): a prospective, multicentre, parallel-group, open-label randomised trial. Lancet. 2017;389(10083):2031-2040."
    doi: "10.1016/S0140-6736(17)30070-3"
    pmid: "28342637"
    url: "https://doi.org/10.1016/S0140-6736(17)30070-3"
cross_links:
  - target: 01-human/07-system/pemphigus-vulgaris
    relation: connects-to
    note: "Anti-Dsg3 IgG4 (mucosal pemphigus) and anti-Dsg3+Dsg1 IgG4 (mucocutaneous pemphigus) are the pathogenic autoantibodies; steric hindrance of Dsg3 trans-adhesion → desmosome disruption → suprabasal acantholysis → flaccid blisters; Dsg3 titer correlates with disease activity."
  - target: 01-human/03-molecular/immunoglobulin-g
    relation: connects-to
    note: "Pathogenic anti-Dsg3 antibodies are predominantly IgG4 (non-complement-fixing) with some IgG1 (complement-fixing); IgG4 steric hindrance is the dominant mechanism; IgG4 titers track disease activity and remission; IVIG can temporarily dilute pathogenic antibodies."
  - target: 01-human/03-molecular/cd20
    relation: connects-to
    note: "Rituximab (anti-CD20) depletes anti-Dsg3-producing B cells; Ritux 3/PEMPHIX Phase 3 (N=90; rituximab + short prednisone vs. long prednisone): 90% vs. 28% CR at month 24; FDA approved June 2018 as first-line pemphigus therapy; obinutuzumab under investigation."
  - target: 01-human/03-molecular/fcrn
    relation: connects-to
    note: "Anti-Dsg3 IgG4 is recycled by FcRn → prolonged half-life sustains blister formation; efgartigimod alfa (anti-FcRn; ADHERE-SC Phase 3: CR 58% vs 23%; FDA Oct 2023) reduces total IgG including anti-Dsg3; batoclimab (anti-FcRn) and rozanolixizumab under investigation."
  - target: 01-human/06-organ/skin
    relation: part-of
    note: "Dsg3 is expressed in suprabasal layers of stratified epithelia — restricted to lower epidermis in skin, throughout mucosal epithelium; Dsg1 is expressed in the superficial granular layer (absent Dsg3), explaining why anti-Dsg1 alone causes subcorneal pemphigus foliaceus."
---

# Desmoglein-3

## Overview

**Desmoglein-3 (DSG3)** is a **calcium-dependent transmembrane glycoprotein** of the cadherin superfamily that constitutes a critical component of **desmosomes** — the intercellular adhesion junctions that mechanically couple adjacent keratinocytes in stratified squamous epithelia [^amagai-1991-dsg3-pemphigus]. Dsg3 is the primary autoantigen in **pemphigus vulgaris (PV)**, one of the most serious autoimmune blistering diseases in medicine.

The discovery by Amagai et al. (1991) that pemphigus IgG autoantibodies target Dsg3 was a watershed moment in autoimmune disease research — it definitively identified the molecular target, established the direct pathogenicity of IgG, and ultimately enabled the rational development of targeted therapies including rituximab and FcRn inhibitors.

**Clinical significance:**
- Anti-Dsg3 IgG4 → pemphigus vulgaris (mucosal dominant) or pemphigus vulgaris mucocutaneous (Dsg3+Dsg1)
- Anti-Dsg1 IgG4 only → pemphigus foliaceus (superficial cutaneous blistering)
- Rituximab (anti-CD20; FDA **June 2018**) and efgartigimod (anti-FcRn; FDA **October 2023**) are approved for PV — both work upstream of the DSG3–antibody interface

## Structure

### DSG3 protein architecture

Desmoglein-3 belongs to the **desmocollin/desmoglein** subfamily of classical cadherins:

| Feature | Detail |
|:--------|:-------|
| Gene | *DSG3*, chromosome 18q12.1 |
| Protein | 999 amino acids; ~130 kDa (mature glycoprotein) |
| Signal peptide | Cleaved during ER processing |
| Propeptide domain | Short N-terminal pro-region cleaved in Golgi (activates adhesion competence) |
| Extracellular domains | EC1-EC5 (cadherin repeat domains); Ca²⁺-binding between each repeat → rigid rod |
| Transmembrane | Single-pass helix |
| Intracellular domain | Intracellular anchor domain (IA), intracellular cadherin-like segment (ICS), desmosomal plaque-binding domain (DPBD) → binds desmoplakin, plakophilin, plakoglobin |

**Trans-adhesion mechanism:** Dsg3 on adjacent keratinocytes forms *trans* dimers via Ca²⁺-dependent EC1-EC1 interactions — a "strand-swap" mechanism where the conserved N-terminal tryptophan (Trp2) of one Dsg3 inserts into the hydrophobic pocket of the partner molecule. This provides the primary adhesive force within the desmosome.

**The desmosome:** A multiprotein adhesion complex:
- Extracellular: Dsg3/Dsg1 trans-adhesion + desmocollin (Dsc) trans-adhesion
- Outer dense plaque: plakoglobin (γ-catenin) + plakophilin 1/2/3
- Inner dense plaque: **desmoplakin** (DP) — links desmosome to intermediate filaments (keratin)
- Keratin intermediate filaments (KRT5/KRT14 in basal layer) → cytoplasmic anchorage

### DSG3 expression pattern

| Tissue/Layer | Dsg3 Expression | Dsg1 Expression | Clinical relevance |
|:-------------|:----------------|:----------------|:------------------|
| Mucosa (oropharynx, esophagus) | High (throughout epithelium) | Low | Anti-Dsg3 alone → mucosal PV |
| Epidermis — lower layers (basal/suprabasal) | Moderate | Moderate | Anti-Dsg3+Dsg1 → mucocutaneous PV |
| Epidermis — upper layers (granular) | Absent | High | Anti-Dsg1 alone → pemphigus foliaceus |
| Thymic epithelium | Present | Present | Dsg3 tolerance broken in PV (thymic selection failure) |

## Function

### Desmosome function in epithelial integrity

Desmosomes are the primary mechanical coupling structures in stratified epithelia, transmitting tensile forces between keratinocytes and distributing them through the intermediate filament network. **DSG3 is essential for mucosal integrity**: Dsg3-knockout mice develop mucosal erosions recapitulating pemphigus vulgaris, confirming DSG3's non-redundant role at mucosal surfaces. In skin, Dsg1 can partially compensate for Dsg3 loss (explaining why mucosal involvement is an invariant feature of PV regardless of Dsg1 status, while skin involvement requires additional Dsg1 autoantibodies).

### Signal transduction from the desmosome

Beyond adhesion, Dsg3 participates in signaling:
- **Dsg3 clustering** → phosphorylation of plakophilin → modulation of Rho GTPases → cytoskeletal dynamics
- **Anti-Dsg3 IgG binding** → EGFR/ErbB2 transactivation → PLC-γ → PKC → phosphorylation of desmoplakin → desmosome disassembly (signaling arm of acantholysis, in addition to steric hindrance)
- **p38 MAPK pathway:** Anti-Dsg3 IgG → Dsg3-mediated p38 MAPK activation → heat shock protein 27 (HSP27) phosphorylation → keratin filament retraction → cell rounding

## Mechanism

### Pemphigus pathogenesis — steric hindrance + signaling

**Two-model framework for anti-Dsg3-mediated acantholysis:**

**Model 1 — Steric hindrance:**
- Anti-Dsg3 IgG4 binds EC1/EC2 domains of Dsg3 → physically blocks the EC1–EC1 trans-adhesion interaction → prevents Dsg3 bridge formation → desmosome disassembly → acantholysis
- Pure steric hindrance: demonstrated by monoclonal anti-Dsg3 Fabs that cause acantholysis without crosslinking
- Antibody titer × epitope proximity to adhesive interface = pathogenic potential

**Model 2 — Signaling:**
- Crosslinking by IgG (bivalent) → Dsg3 clustering → EGFR/Src activation → PLC-γ/PKC → desmoplakin phosphorylation → desmosome internalization → pemphigus lesion formation
- These two mechanisms are not mutually exclusive; both likely operate simultaneously

**Dsg3 compensation hypothesis:** Anti-Dsg3 alone (without anti-Dsg1) causes blistering only at mucosal sites because Dsg1 (abundantly expressed in superficial epidermis, where Dsg3 is absent) maintains epidermal adhesion. This explains the strict correlation: mucosal-only PV = anti-Dsg3 only; mucocutaneous PV = anti-Dsg3 + anti-Dsg1.

### Rituximab — depletion of anti-Dsg3 B cells

**Rituximab (Rituxan; anti-CD20 mAb):**
- Depletes CD20+ B cells → reduces Dsg3-reactive plasma cell precursors → anti-Dsg3 IgG4 titer falls over weeks-months (long-lived plasma cells may persist; plasma cell-directed strategies such as atacicept are being studied)
- **Ritux 3 trial** (France; N=90; rituximab 1000 mg IV × 2 with short-course prednisone vs. prednisone alone): CR at month 24: **90% vs. 28%** (p<0.0001); anti-Dsg3 titers fell significantly faster with rituximab [^joly-2017-rituximab-pemphix]
- FDA approved **June 2018** for moderate-to-severe PV — first FDA indication for pemphigus
- Dosing: 1000 mg IV at weeks 0 and 2 (induction); 500 mg at 6 and 12 months (maintenance)
- Remission durability: 85% remain off systemic steroids at 24 months (vs. 14% with prednisone alone)

### Efgartigimod — FcRn blockade to reduce anti-Dsg3 IgG

**Efgartigimod alfa (Vyvgart; Argenx):**
- Neonatal Fc receptor (FcRn) blockade → accelerates IgG catabolism → reduces all IgG subclasses including pathogenic anti-Dsg3 IgG4
- **ADHERE-SC Phase 3** (N=214; efgartigimod SC 1000 mg Q1W × 4 cycles vs. placebo): Complete remission at cycle 4: **58% vs. 23%** (p<0.001); anti-Dsg3 titer reduction >70%
- FDA approved **October 2023** for pemphigus vulgaris (IV form also studied; SC approved)
- Works faster than rituximab for acute disease control; does not cause long-term B-cell depletion
- Limitation: IgG returns after stopping → maintenance strategy needed

## Connections

- `connects-to` → **[Pemphigus Vulgaris](../../07-system/pemphigus-vulgaris/README.md)** — Anti-Dsg3 IgG4 is the pathogenic autoantibody in PV; steric hindrance of Dsg3 trans-adhesion + p38 MAPK/EGFR signaling → suprabasal acantholysis → flaccid blisters at mucosal (Dsg3 alone) and cutaneous (Dsg3+Dsg1) sites; Dsg3 titer tracks disease activity and guides treatment response monitoring.
- `connects-to` → **[Immunoglobulin G](../immunoglobulin-g/README.md)** — Anti-Dsg3 autoantibodies are predominantly IgG4 (steric hindrance-mediated, non-complement-fixing) + IgG1 (complement-activating); IgG4 is the dominant pathogenic subclass in established disease; IVIG can dilute pathogenic IgG temporarily; IgG4 titer correlates with PV disease activity.
- `connects-to` → **[CD20](../cd20/README.md)** — Rituximab (anti-CD20) depletes Dsg3-reactive B cell precursors → anti-Dsg3 IgG4 titer reduction → sustained remission; Ritux 3 trial (90% vs. 28% CR at 24 months; FDA Jun 2018) established rituximab as first-line PV therapy, replacing long-term high-dose corticosteroids.
- `connects-to` → **[FcRn](../fcrn/README.md)** — FcRn recycles anti-Dsg3 IgG4 → prolongs pathogenic antibody half-life; efgartigimod (anti-FcRn; ADHERE-SC: 58% vs. 23% CR; FDA Oct 2023) accelerates IgG catabolism → rapid reduction of anti-Dsg3 IgG4 → disease control without B-cell depletion.
- `part-of` → **[Skin](../../06-organ/skin/README.md)** — Dsg3 is expressed in suprabasal epidermis and throughout mucosal epithelia; its expression gradient (high in mucosa, restricted to lower epidermis, absent in upper epidermis) dictates the blister location in each pemphigus subtype and explains the Dsg compensation principle.

[^amagai-1991-dsg3-pemphigus]: Amagai M, Klaus-Kovtun V, Stanley JR. Autoantibodies against a novel epithelial cadherin in pemphigus vulgaris, a disease of cell adhesion. *Cell.* 1991;67(5):869-877. [doi:10.1016/0092-8674(91)90360-B](https://doi.org/10.1016/0092-8674(91)90360-B) · [PubMed 1959133](https://pubmed.ncbi.nlm.nih.gov/1959133/)
[^joly-2017-rituximab-pemphix]: Joly P, Maho-Vaillant M, Prost-Squarcioni C, et al. First-line rituximab combined with short-term prednisone versus prednisone alone for the treatment of pemphigus (Ritux 3): a prospective, multicentre, parallel-group, open-label randomised trial. *Lancet.* 2017;389(10083):2031-2040. [doi:10.1016/S0140-6736(17)30070-3](https://doi.org/10.1016/S0140-6736(17)30070-3) · [PubMed 28342637](https://pubmed.ncbi.nlm.nih.gov/28342637/)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
