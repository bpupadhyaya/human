---
schema: human-scale-entry/v1
id: pf4
name: PF4
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-08
summary: "Platelet Factor 4 (PF4/CXCL4; chr4q13.3) is a CXC chemokine released from platelet alpha-granules; neutralizes heparin; PF4-heparin complexes are the HIT antigen: IgG → FcγRIIA → platelet activation → thrombosis despite thrombocytopenia. Also anti-angiogenic."
aliases: ["PF4", "CXCL4", "platelet factor 4", "platelet factor-4", "CXC chemokine 4", "PF-4", "heparin-neutralizing protein"]
sources:
  - id: warkentin-2007-hit-review
    type: peer-reviewed
    cite: "Warkentin TE, Greinacher A. Heparin-induced thrombocytopenia: recognition, treatment, and prevention: the Seventh ACCP Conference on Antithrombotic and Thrombolytic Therapy. Chest. 2004;126(3 Suppl):311S-337S."
    doi: "10.1378/chest.126.3_suppl.311S"
    pmid: "15383477"
    url: "https://doi.org/10.1378/chest.126.3_suppl.311S"
  - id: greinacher-2021-vitt-nejm
    type: peer-reviewed
    cite: "Greinacher A, Thiele T, Warkentin TE, et al. Thrombotic thrombocytopenia after ChAdOx1 nCov-19 vaccination. N Engl J Med. 2021;384(22):2092-2101."
    doi: "10.1056/NEJMoa2104840"
    pmid: "33835769"
    url: "https://doi.org/10.1056/NEJMoa2104840"
  - id: sachais-2011-pf4-biology
    type: peer-reviewed
    cite: "Sachais BS, Higazi AAR, Cines DB, Poncz M, Kowalska MA. Interactions of platelet factor 4 with the vessel wall. Semin Thromb Hemost. 2004;30(3):351-358."
    doi: "10.1055/s-2004-831048"
    pmid: "15246229"
    url: "https://doi.org/10.1055/s-2004-831048"
cross_links:
  - target: 01-human/07-system/heparin-induced-thrombocytopenia
    relation: connects-to
    note: "PF4-heparin complex forms when heparin binds platelet-released PF4 → conformational change → neo-antigen → IgG anti-PF4/heparin → FcγRIIA on platelets → activation → TXA2 + PF4 release → amplification loop → thrombocytopenia + paradoxical thrombosis (HIT type 2)."
  - target: 01-human/04-cellular/platelet
    relation: connects-to
    note: "PF4 is stored in platelet alpha-granules at ~25 μM and released upon platelet activation (thrombin, collagen, ADP); PF4 concentration around activated platelets → 100-1000× local heparin neutralization; PF4-mediated feedback inhibits megakaryocyte maturation (TPO antagonism)."
  - target: 01-human/03-molecular/thrombin
    relation: connects-to
    note: "HIT causes paradoxical thrombosis: activated platelets generate procoagulant microparticles → thrombin generation; argatroban (DTI) and bivalirudin block thrombin in HIT; warfarin is contraindicated initially (protein C drops first → warfarin-induced limb gangrene risk)."
---

# PF4

## Overview

**Platelet Factor 4 (PF4, gene *CXCL4*, chromosome 4q13.3)** is a **CXC chemokine** constitutively expressed in megakaryocytes and stored at very high concentration (~25 μM) in **platelet alpha-granules**. It is one of the most abundant platelet-released proteins, released immediately upon platelet activation by thrombin, collagen, ADP, or epinephrine [^sachais-2011-pf4-biology].

PF4 occupies a paradoxical central role in hemostasis:
1. **Physiologically:** Localizes anti-heparin activity to the platelet plug, amplifies the coagulation response, and recruits neutrophils/monocytes
2. **Pathologically:** When heparin is administered therapeutically, PF4-heparin complexes form the **immunogenic neo-antigen of heparin-induced thrombocytopenia (HIT)** — the most dangerous drug-induced immune thrombocytopenia, causing paradoxical thrombosis in the setting of low platelet counts

Beyond hemostasis, PF4 is a potent **anti-angiogenic factor**: it lacks the ELR motif required for angiogenic signaling and directly competes with FGF2 and VEGF for receptor binding. PF4 variants have been investigated as anti-tumor agents.

**VITT (Vaccine-Induced Immune Thrombocytopenia with Thrombosis):** A 2021 pandemic-era discovery [^greinacher-2021-vitt-nejm] — adenoviral vector COVID-19 vaccines (ChAdOx1 nCoV-19/AstraZeneca, Ad26.COV2.S/Janssen) trigger anti-PF4 antibodies WITHOUT heparin exposure, causing a HIT-like syndrome with cerebral venous sinus thrombosis (CVST), splanchnic vein thrombosis, DVT/PE, and thrombocytopenia. Treatment: IVIG + non-heparin anticoagulant + avoid heparin/platelet transfusion.

## Structure

### PF4 monomer and tetramer

PF4 is a **70 amino acid, 7.8 kDa** protein with the canonical CXC chemokine fold:
- **N-terminal loop** (1-9 aa): flexible; contains the anti-heparin-binding lysine residues
- **Three-stranded antiparallel β-sheet** (core)
- **C-terminal α-helix** (46-70 aa): amphipathic; drives dimerization
- **Disulfide bonds:** Cys10-Cys36 and Cys12-Cys52 (conserved in CXC family)

**Tetramer formation:** PF4 exists as a **dimer in solution** and rapidly forms **tetramers** (two dimers stacked face-to-face) at physiological concentrations. The tetramer is the heparin-binding unit:
- **Heparin-binding site:** Ring of positively charged lysine/arginine residues (K61, K65, K66, R42, R49) on the outer surface of the tetramer
- Binds heparin with Kd ~10 nM; stoichiometry: ~1 heparin chain : 1 PF4 tetramer (at optimal heparin length ≥12-18 saccharide units)

### PF4-heparin complex — the HIT antigen

**Critical structural insight:** When PF4 tetramers bind to heparin (or other polyanionic molecules), a **conformational rearrangement** exposes a neo-epitope on the PF4 surface (particularly the region around Lys61-Lys66 and adjacent residues). This neo-epitope is not present on free PF4 — it is created only when PF4 is complexed with polyanions. Anti-PF4/heparin IgG recognizes this complex, not free PF4.

**Why different heparin types vary in HIT risk:**
- **Unfractionated heparin (UFH):** Long chains (mean MW ~15,000 Da; 45-50 saccharides) → optimal PF4-heparin complex formation → highest HIT risk (~0.5-5%)
- **Low molecular weight heparin (LMWH):** Shorter chains (MW ~4,500-5,000 Da; 15-20 saccharides) → less optimal complex formation → lower HIT risk (~0.1-0.5%)
- **Fondaparinux (pentasaccharide):** 5 saccharides; too short to form stable PF4 complex → minimal HIT risk (~<0.01%)

## Function

### Heparin neutralization at the platelet plug

After platelet activation, the local PF4 concentration around the platelet plug rises to ~100-1,000× the plasma concentration (~10 μg/mL):
1. PF4 binds heparin sulfate on endothelial surfaces → displaces antithrombin → locally reduces heparin anticoagulant activity
2. Prevents premature inhibition of thrombin at the clot site
3. Also binds to chondroitin sulfate on platelet membranes → concentrates PF4 at the platelet surface

### Chemokine functions

PF4 interacts with **CXCR3-B** (an isoform of CXCR3 with opposite signaling polarity to CXCR3-A) on endothelial cells and tumor vasculature:
- **Anti-angiogenic:** Blocks VEGFR2 binding of VEGF; competes with FGF2 for heparan sulfate (required for FGF2 signaling); inhibits endothelial cell proliferation and migration → inhibits tumor angiogenesis
- **Neutrophil recruitment:** Binds CXCR3-A on neutrophils → chemotaxis (weaker than CXCL8)
- **Monocyte differentiation:** PF4 promotes monocyte-to-dendritic cell differentiation; modulates macrophage function

### Megakaryocyte feedback inhibition

PF4 acts as a **negative regulator of megakaryopoiesis** — high PF4 levels in the platelet-rich marrow microenvironment suppress TPO signaling (c-Mpl desensitization) and directly inhibit megakaryocyte differentiation. This creates a feedback loop: high platelet mass → high PF4 → suppressed new platelet production.

## Mechanism

### HIT immunopathogenesis — the PF4-heparin amplification loop

**Step-by-step HIT mechanism:**

1. **Heparin exposure → PF4-heparin complex:** Heparin (administered therapeutically) binds platelet-released PF4 → PF4 tetramer conformational change → exposes neo-epitope → anti-PF4/heparin IgG generated (onset: 5-14 days, earlier if prior heparin exposure)

2. **IgG-PF4-heparin → FcγRIIA activation:** IgG Fc domain crosslinks FcγRIIA (CD32a) on platelets → Gαq → IP₃/DAG → Ca²⁺ → dense granule release (ADP, serotonin) + thromboxane A₂ (TXA₂) → platelet activation and aggregation

3. **Amplification loop:** Activated platelets release more PF4 → more PF4-heparin complexes form → more antibody bridging → exponential platelet consumption → thrombocytopenia

4. **Procoagulant state despite thrombocytopenia:** Activated platelets release microparticles → phosphatidylserine exposure → thrombin generation → fibrin clot formation → paradoxical thrombosis (venous AND arterial)

5. **Monocyte/endothelial activation:** Anti-PF4/heparin IgG-FcγRII on monocytes → TF expression → further thrombin generation; endothelial activation → VWF release → platelet adhesion

**Why thrombosis occurs paradoxically:** Unlike most thrombocytopenic states where bleeding dominates, HIT platelets are maximally activated — they function as procoagulant microparticles even as they are being consumed. The ratio of clot-generating activity per platelet is dramatically elevated.

### VITT — HIT without heparin [^greinacher-2021-vitt-nejm]

**VITT mechanism:**
- Adenoviral vector vaccine DNA → cell nucleus → expression of spike antigen → adenoviral proteins (or DNA-protein complexes) reach platelet alpha-granule pathway
- Alternatively: vaccine-induced B cell activation directly generates anti-PF4 antibodies without polyanion dependence
- Anti-PF4 antibodies (at lower titer than HIT) bind PF4 even without heparin → SAME FcγRIIA-mediated platelet activation pathway as HIT
- **Key distinction:** VITT antibodies bind PF4 WITHOUT heparin; HIT antibodies require the PF4-heparin complex
- **Diagnosis:** ELISA positive + SRA positive + thrombocytopenia + thrombosis (especially CVST, splanchnic) within 4-28 days of adenoviral vaccine
- **Treatment:** High-dose IVIG (1 g/kg IV × 2 days) → saturates FcγR + provides anti-idiotypic antibodies; non-heparin anticoagulation (argatroban, fondaparinux, DOACs); avoid heparin AND platelet transfusions

## Connections

- `connects-to` → **[Heparin-Induced Thrombocytopenia](../../07-system/heparin-induced-thrombocytopenia/README.md)** — PF4-heparin complex forms when heparin binds platelet-released PF4 → conformational change → neo-antigen → IgG anti-PF4/heparin → FcγRIIA on platelets → activation → TXA2 + PF4 release → amplification loop → thrombocytopenia + paradoxical thrombosis (HIT type 2).
- `connects-to` → **[Platelet](../../04-cellular/platelet/README.md)** — PF4 is stored in platelet alpha-granules at ~25 μM and released upon platelet activation (thrombin, collagen, ADP); PF4 concentration around activated platelets → 100-1000× local heparin neutralization; PF4-mediated feedback inhibits megakaryocyte maturation (TPO antagonism).
- `connects-to` → **[Thrombin](../thrombin/README.md)** — HIT causes paradoxical thrombosis: activated platelets generate procoagulant microparticles → thrombin generation; argatroban (DTI) and bivalirudin block thrombin in HIT; warfarin is contraindicated initially (protein C drops first → warfarin-induced limb gangrene risk).

[^warkentin-2007-hit-review]: Warkentin TE, Greinacher A. Heparin-induced thrombocytopenia: recognition, treatment, and prevention. *Chest.* 2004;126(3 Suppl):311S-337S. [doi:10.1378/chest.126.3_suppl.311S](https://doi.org/10.1378/chest.126.3_suppl.311S) · [PubMed 15383477](https://pubmed.ncbi.nlm.nih.gov/15383477/)
[^greinacher-2021-vitt-nejm]: Greinacher A, Thiele T, Warkentin TE, et al. Thrombotic thrombocytopenia after ChAdOx1 nCov-19 vaccination. *N Engl J Med.* 2021;384(22):2092-2101. [doi:10.1056/NEJMoa2104840](https://doi.org/10.1056/NEJMoa2104840) · [PubMed 33835769](https://pubmed.ncbi.nlm.nih.gov/33835769/)
[^sachais-2011-pf4-biology]: Sachais BS, Higazi AAR, Cines DB, Poncz M, Kowalska MA. Interactions of platelet factor 4 with the vessel wall. *Semin Thromb Hemost.* 2004;30(3):351-358. [doi:10.1055/s-2004-831048](https://doi.org/10.1055/s-2004-831048) · [PubMed 15246229](https://pubmed.ncbi.nlm.nih.gov/15246229/)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
