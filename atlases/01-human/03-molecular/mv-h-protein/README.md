---
schema: human-scale-entry/v1
id: mv-h-protein
name: MV-H Protein
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-08
summary: "Measles hemagglutinin (H; type II transmembrane; 617 aa) binds SLAM/CD150 on immune cells and nectin-4 on airway epithelium; SLAM tropism explains immune amnesia; H-F fusion complex drives syncytia; N-glycan shield on H is a barrier to vaccine-elicited neutralizing antibodies."
aliases: ["MV-H protein", "measles hemagglutinin", "measles H protein", "MV hemagglutinin", "SLAM receptor", "CD150 measles", "nectin-4 measles", "measles H", "measles surface glycoprotein H", "morbillivirus hemagglutinin"]
sources:
  - id: tatsuo-2000-slam-receptor
    type: peer-reviewed
    cite: "Tatsuo H, Ono N, Tanaka K, Yanagi Y. SLAM (CDw150) is a cellular receptor for measles virus. Nature. 2000;406(6798):893-897."
    doi: "10.1038/35022579"
    pmid: "10972291"
    url: "https://doi.org/10.1038/35022579"
    accessed: "2026-06-08"
  - id: muhlebach-2011-nectin4-receptor
    type: peer-reviewed
    cite: "Mühlebach MD, Mateo M, Sinn PL, et al. Adherens junction protein nectin-4 is the epithelial receptor for measles virus. Nature. 2011;480(7378):530-533."
    doi: "10.1038/nature10639"
    pmid: "22048310"
    url: "https://doi.org/10.1038/nature10639"
    accessed: "2026-06-08"
cross_links:
  - target: 01-human/07-system/measles
    relation: connects-to
    note: "MV-H hemagglutinin drives measles tropism: SLAM/CD150 on T/B cells and DCs → immune amnesia; nectin-4 on airway epithelium → shedding; H-F fusion complex forms Warthin-Finkeldey syncytia; H head domain is the primary target of measles-neutralizing antibodies."
  - target: 01-human/03-molecular/mavs
    relation: connects-to
    note: "MV-H binding to SLAM/CD150 on dendritic cells → DC infection → impaired IL-12/IFN-α; MV replication generates 5′ppp RNA → RIG-I → MAVS → IFN-β; MV V protein sequesters MDA5 → blocks MAVS; H-driven DC tropism impairs early innate immune activation and T cell priming."
  - target: 01-human/03-molecular/rsv-f-protein
    relation: connects-to
    note: "MV-H (β-propeller; SLAM/CD150 receptor; nectin-4) triggers MV-F for fusion, unlike RSV-F which does both receptor binding and fusion; anti-H antibodies are primary measles vaccine protection; anti-prefusion F site Ø (nirsevimab) is the RSV functional analogue."
  - target: 01-human/03-molecular/influenza-ha
    relation: analogue-of
    note: "MV-H and influenza HA are viral attachment glycoproteins: HA binds sialic acid, H binds SLAM/CD150 and nectin-4; both trigger RIG-I/MAVS innate signaling; both undergo antigenic variation; anti-H and anti-HA IgG are the primary mechanism of vaccine-induced protection."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "MV-H binds SLAM/CD150 on DCs → productive DC infection → impaired IL-12/IFN-α production and reduced T cell priming; DC functional impairment is a core mechanism of measles immune amnesia (loss of pre-existing pathogen-specific memory lasting 2–3 years post-infection)."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "MV-H SLAM/CD150 tropism infects CD150+ T cells, B cells, and DCs → deletion of pre-existing immune memory (measles immune amnesia); epidemiological studies show measles raises all-cause child mortality for 2–3 years; MMR vaccination prevents this prolonged immunological harm."
---

# MV-H Protein

## Overview

The **measles virus hemagglutinin (MV-H protein)** is one of two surface glycoproteins of measles virus (MV), functioning as the **receptor-binding protein** that initiates cellular attachment and, together with the fusion protein (MV-F), drives viral entry and cell-cell fusion. Unlike influenza hemagglutinin (which recognizes sialic acid) or RSV-F (which performs both receptor binding and membrane fusion independently), MV-H has **no sialidase or hemagglutinin activity against red blood cells** despite its historical name — it was named hemagglutinin before its receptor was identified. MV-H is a **type II transmembrane protein** forming a homodimer-of-dimers (tetramer) on the viral surface, with a large C-terminal ectodomain built around a **six-bladed β-propeller (sialidase-fold)** that acts as the receptor-binding platform.

The discovery of MV-H's two sequential receptors — **SLAM/CD150** in 2000 [^tatsuo-2000-slam-receptor] and **nectin-4** in 2011 [^muhlebach-2011-nectin4-receptor] — explained the paradox of measles pathogenesis: why does a respiratory virus cause profound systemic immune suppression? The answer is that MV-H first binds SLAM/CD150 on **T cells, B cells, dendritic cells, and macrophages** → replicates in lymphoid tissue → depletes and infects memory immune cells (immune amnesia) → then spreads to the respiratory epithelium via nectin-4 for amplification and transmission.

**Key insight for vaccinology:** Since anti-H neutralizing antibodies are the primary mechanism of protective immunity (complemented by anti-F antibodies), the MMR vaccine must elicit strong anti-H IgG. The N-glycan shield on H represents a major barrier — viral H accumulates glycans that hide receptor-binding sites from the humoral response, analogous to N-glycan shielding of HIV gp120 and RSV-G.

## Structure

### Primary architecture (617 amino acids)

MV-H is a **type II single-pass transmembrane protein**:
- **N-terminal cytoplasmic tail** (aa 1-34): Short; required for transport and H-F interaction; contains the **di-leucine motif** for Golgi trafficking
- **Transmembrane domain** (aa 35-58): Single-pass; anchors H in viral envelope; dimerization occurs at TM helix
- **Stalk domain** (aa 59-154): α-helical coiled-coil; forms the **H tetramer** (dimer-of-dimers); **triggers F protein by contact**: when H binds receptor, the stalk domain transmits a conformational signal to pre-F → F activates → fusion
- **Head domain (β-propeller ectodomain, aa 155-617):** Six-bladed β-propeller; structurally homologous to sialidase but catalytically inactive; contains all receptor binding sites; primary target of neutralizing antibodies

**H tetramer structure:** Four H monomers assemble as two homodimers that interact head-to-head; the tetramer is the functional entry unit — both H homodimers must engage receptor simultaneously to trigger F.

### Receptor binding sites

**SLAM/CD150 binding site** (primary receptor; immune cells):
- Contact residues: **Y481, P497, L500, I527, S548** in H head domain — the "canyon" on one face of the β-propeller
- SLAM (signaling lymphocytic activation molecule; CD150; *SLAMF1*, chr1q23.3): Self-ligand on T and B lymphocytes; co-stimulatory receptor; expressed on memory T cells, germinal center B cells, DCs, and monocytes — all with high SLAM density vs. naive cells; this explains selective immune cell targeting and memory B cell depletion (immune amnesia)
- SLAM binding triggers H-stalk → F activation

**Nectin-4 binding site** (secondary receptor; airway epithelium):
- Contact residues: **Y481, L500, P502, Y553** — partially overlapping with SLAM site but distinct orientation
- Nectin-4 (PVRL4; Poliovirus Receptor-Like 4; chr1q24.1): Adherens junction protein; expressed on basolateral surface of polarized bronchial epithelium, alveolar type II cells, and some cancer cells (nectin-4 is an oncofetal antigen; Enfortumab vedotin — anti-nectin-4 ADC — approved for urothelial cancer)
- MV reaches nectin-4 only after SLAM-dependent systemic spread to lung → nectin-4 drives final amplification and basolateral-to-apical transcytosis → release into airway lumen → transmission

**Historical receptor (obsolete):** CD46 (membrane cofactor protein, complement regulatory protein) — binds only **Edmonston laboratory strain** H via distinct site; not used by WT measles virus clinical isolates; binding artifact of lab passage

### N-glycan shield

MV-H ectodomain contains **13 N-linked glycans** (N-X-S/T sequons) that:
- Mask receptor-binding site residues from antibody recognition
- Contribute ~40% of H molecular weight
- Evolve to accumulate glycans around immunodominant epitopes (similar to HIV gp120, HCV E2, and influenza HA)
- **Vaccine implication**: MMR vaccine H induces antibodies to relatively exposed epitopes (stalk epitopes, partial head); broadly neutralizing anti-H antibodies recognizing conserved receptor-binding sites are rare (analogous to broadly neutralizing HIV antibodies)

### H-F fusion complex

MV-H and MV-F form a **pre-fusion complex** at the viral surface before receptor engagement:
- H stalk domain (specifically residues in the α-helix-rich stalk, particularly **L137** and **L139**) contacts the F protein trimer
- Upon receptor binding: conformational change propagates from H-head → H-stalk → H-F interface → **F protein is "triggered"** (analogous to a spring release): F pre-fusion state → 6-helix bundle post-fusion state → membrane merger
- Receptor binding is **required** to trigger F: unliganded MV-H holds F in pre-fusion state; SLAM or nectin-4 binding licenses fusion
- MV-F (class I fusogen; F1/F2 subunits from furin cleavage; HRA and HRB domains form 6-HB) is analogous in mechanism to RSV-F, SARS-CoV-2 S, HIV gp41 — all class I viral fusogens

## Function

### Immune amnesia — the SLAM tropism consequence

The mechanistic basis of measles immune amnesia (Mina et al., 2019; *Science*):
1. MV-H binds SLAM/CD150 on **memory B cells** (highest SLAM density among lymphocytes) → MV infects memory B cells preferentially
2. Memory B cell infection → cell death or functional impairment + bystander killing → loss of antigen-specific immunological memory
3. Memory T cells (CD4+ and CD8+ SLAM+) are also depleted
4. Naive B and T cells (lower SLAM density) are less susceptible → the pool of naive cells expands but cannot compensate for loss of antigen-specific memory
5. **Net result**: 20-70% of pre-existing antibody diversity (VirScan quantification) is erased; child is re-susceptible to pathogens previously controlled by immune memory for 2-3 years

**DC infection consequence:** MV-H-SLAM engagement on DCs → MV replication in DCs → impaired IL-12 and IFN-α production → biased Th2 priming in the post-measles period → susceptibility to intracellular bacterial infections (TB reactivation) that require Th1 immunity.

### Syncytium formation

MV-H (still expressed on infected cell surface) + MV-F (on same cell) → contacts SLAM/CD150 or nectin-4 on neighboring cells → cell-cell fusion → **multinucleated syncytia (Warthin-Finkeldey giant cells)**:
- Pathognomonic histology in lymph nodes, tonsils, appendix, intestinal Peyer's patches, and lung (giant cell pneumonitis)
- Syncytia enable virus to spread directly from cell to cell without free virion → immune evasion (antibodies cannot neutralize cell-associated spread)
- Syncytium formation = H is required (anti-H antibodies prevent syncytia; anti-F antibodies less effective at preventing cell-cell spread if H is not blocked)

### SSPE — H mutations in persistent infection

In SSPE (subacute sclerosing panencephalitis), the MV H protein accumulates specific mutations that alter tropism and enable CNS persistence:
- **Cytoplasmic tail mutations** (T461I, Y504H): alter H intracellular trafficking → retention in endoplasmic reticulum/Golgi → impaired surface expression → neurons cannot export H → virus spread only by syncytium without free virus
- **Hyperfusogenic H variants**: SSPE H mutations (combined with SSPE F hyperfusogenic mutations) → lower threshold for H-F triggering → enhanced cell-cell fusion in neurons
- **Receptor independence:** Some SSPE strains lose SLAM binding ability and may have acquired ability to use unknown neuronal receptor(s) or become receptor-independent at the single-amino-acid-variant H level

## Mechanism

### Anti-H antibody neutralization

MV neutralization primarily involves anti-H antibodies that:
1. **Block SLAM binding**: Antibodies to the SLAM-binding site on H head → steric block → no receptor engagement → no F triggering → no fusion (most potent neutralization)
2. **Block nectin-4 binding**: Less potent; relevant for preventing transmission
3. **Block H-F interaction (stalk antibodies)**: Bind H stalk → prevent H from triggering F even after SLAM binding → broad but weaker neutralization
4. **Block tetramer formation**: Rare epitopes at the H dimer-dimer interface; disrupt functional H tetramer

**MMR vaccine antibodies:** The live attenuated Edmonston/Schwarz H generates antibodies primarily to **H head epitopes** near the receptor-binding site; minimum protective titer = ≥120 mIU/mL anti-H IgG; titers >500 mIU/mL correlate with reliable protection; titers wane over decades (boosted by natural exposure or booster dose).

### Anti-F complement

While anti-H is primary, anti-F antibodies contribute:
- Target F1 (HRA/HRB junction and fusion peptide) → prevent 6-HB formation → block membrane fusion
- Anti-F antibodies from MMR generally lower titer than anti-H but provide synergistic protection
- **Critical difference from RSV**: In RSV, anti-pre-F (site Ø) is the dominant protective antibody class; in measles, anti-H is dominant with anti-F as supplementary

### Cross-reactivity with related Morbilliviruses

MV-H is genetically related to hemagglutinin/attachment proteins of:
- **CDV-H** (Canine distemper virus): Also uses SLAM receptor (canine SLAM); the H proteins share structural fold → some cross-reactive antibodies
- **Nipah/Hendra-G** (Henipaviruses): Also use SLAM-like receptor (EFNB2/EFNB3 ephrin ligands, not SLAM); analogous H/G protein class but different receptor family — not cross-reactive
- **Rinderpest virus**: Eradicated 2011; used cattle SLAM/CD150; H closely related to MV-H; rinderpest eradication by cattle vaccination used MV-H cross-reactive responses historically

## Connections

**→ [Measles](../../../07-system/measles/)**: MV-H hemagglutinin drives measles tropism: SLAM/CD150 on T/B cells and DCs → immune amnesia; nectin-4 on airway epithelium → shedding; H-F fusion complex forms Warthin-Finkeldey syncytia; H head domain is the primary target of measles-neutralizing antibodies.

**→ [MAVS](../mavs/)**: MV-H binding to SLAM/CD150 on dendritic cells → DC infection → impaired IL-12/IFN-α production; MV replication generates 5′ppp RNA → RIG-I → MAVS → IFN-β; MV V protein (not H) sequesters MDA5 → blocks MAVS; H-driven DC tropism impairs early innate immune activation and T cell priming.

**→ [RSV F Protein](../rsv-f-protein/)**: MV-H (β-propeller; SLAM/CD150 receptor; nectin-4) triggers MV-F for fusion, unlike RSV-F which performs both receptor binding and membrane fusion independently; anti-H antibodies are the primary measles vaccine-induced protection mechanism; anti-prefusion F site Ø (nirsevimab) is the RSV functional analogue.

**→ [Influenza Hemagglutinin](../influenza-ha/)**: MV-H and HA are viral attachment glycoproteins: HA binds sialic acid, H binds SLAM/CD150 and nectin-4; both trigger RIG-I/MAVS innate signaling; both undergo antigenic variation; anti-H and anti-HA IgG are the primary mechanism of vaccine-induced protection.

**→ [Dendritic Cell](../../04-cellular/dendritic-cell/)**: MV-H binds SLAM/CD150 on DCs → productive DC infection → impaired IL-12/IFN-α and reduced T cell priming; DC functional impairment is a core mechanism of measles immune amnesia (loss of pre-existing pathogen-specific memory lasting 2–3 years post-infection).

**→ [Immune System](../../07-system/immune-system/)**: MV-H SLAM/CD150 tropism infects CD150+ T cells, B cells, and DCs → loss of pre-existing pathogen-specific immune memory (measles immune amnesia); measles raises all-cause child mortality for 2–3 years post-infection; MMR vaccination prevents this immunological harm.

[^tatsuo-2000-slam-receptor]: Tatsuo H, Ono N, Tanaka K, Yanagi Y. SLAM (CDw150) is a cellular receptor for measles virus. *Nature.* 2000;406(6798):893-897. [doi:10.1038/35022579](https://doi.org/10.1038/35022579) · [PubMed 10972291](https://pubmed.ncbi.nlm.nih.gov/10972291/)
[^muhlebach-2011-nectin4-receptor]: Mühlebach MD, Mateo M, Sinn PL, et al. Adherens junction protein nectin-4 is the epithelial receptor for measles virus. *Nature.* 2011;480(7378):530-533. [doi:10.1038/nature10639](https://doi.org/10.1038/nature10639) · [PubMed 22048310](https://pubmed.ncbi.nlm.nih.gov/22048310/)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
