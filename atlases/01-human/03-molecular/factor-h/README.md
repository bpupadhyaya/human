---
schema: human-scale-entry/v1
id: factor-h
name: Factor H
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-08
summary: "Factor H (CFH; chr1q31.3) is the primary soluble regulator of the alternative complement pathway; 20 SCR domains; binds C3b on host surfaces → decay-acceleration + Factor I cofactor → C3b inactivation. CFH mutations → aHUS; Y402H polymorphism → macular degeneration risk."
aliases: ["Factor H", "CFH", "complement Factor H", "FH", "complement regulator", "alternative pathway inhibitor"]
sources:
  - id: fakhouri-2017-ahus-lancet
    type: peer-reviewed
    cite: "Fakhouri F, Zuber J, Frémeaux-Bacchi V, Loirat C. Haemolytic uraemic syndrome. Lancet. 2017;390(10095):681-696."
    doi: "10.1016/S0140-6736(17)30062-4"
    pmid: "28242109"
    url: "https://doi.org/10.1016/S0140-6736(17)30062-4"
  - id: chen-2010-cfh-y402h-amd
    type: peer-reviewed
    cite: "Chen LJ, Liu DT, Tam PO, et al. Association of complement factor H polymorphisms with exudative age-related macular degeneration. Mol Vis. 2006;12:1536-1542."
    doi: "10.1016/j.ophtha.2005.06.031"
    pmid: "17046868"
    url: "https://doi.org/10.1016/j.ophtha.2005.06.031"
  - id: zipfel-2009-factor-h-review
    type: peer-reviewed
    cite: "Zipfel PF, Skerka C. Complement regulators and inhibitory proteins. Nat Rev Immunol. 2009;9(10):729-740."
    doi: "10.1038/nri2620"
    pmid: "19756009"
    url: "https://doi.org/10.1038/nri2620"
cross_links:
  - target: 01-human/07-system/ahus
    relation: connects-to
    note: "CFH loss-of-function mutations (SCR19-20 clustering) impair surface C3b regulation on renal endothelium → uncontrolled alternative pathway → TMA; anti-CFH antibodies cause aHUS in ~6-10% (especially CFHR1-CFHR3 deletion); eculizumab/ravulizumab are curative."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Factor H accelerates decay of C3bBb (alternative C3 convertase) and acts as cofactor for Factor I-mediated C3b cleavage → iC3b; dysregulated alternative C3 convertase (CFH deficiency or C3NeF) → hypocomplementemia C3, aHUS, and C3 glomerulopathy."
  - target: 01-human/03-molecular/complement-c5
    relation: connects-to
    note: "Uncontrolled alternative C3 convertase (from CFH deficiency) generates C3b → assembly of alternative C5 convertase (C3bBbC3b) → C5 cleavage → C5a (inflammation) + MAC (endothelial injury); eculizumab blocks C5 cleavage → prevents TMA in aHUS even without restoring CFH."
---

# Factor H

## Overview

**Factor H** (gene *CFH*, chromosome 1q31.3; plasma concentration ~500 μg/mL) is the **primary soluble regulator of the alternative complement pathway** and the most abundant complement regulatory protein in plasma [^zipfel-2009-factor-h-review]. It controls the spontaneous "tick-over" activation of the alternative pathway — the low-level C3 hydrolysis that occurs constitutively in plasma and on all surfaces — by restricting amplification to foreign or pathogen surfaces while protecting host cells.

The central biological principle of Factor H is **self vs. non-self discrimination at the C3b level**: Factor H binds C3b deposited on host cell surfaces (which display polyanionic markers: sialic acid, glycosaminoglycans/heparan sulfate) and triggers its inactivation, while C3b deposited on pathogen surfaces (lacking these host markers) is NOT inactivated → amplification loop → opsonization and lysis. This elegant surface-sensing mechanism is encoded in distinct regions of Factor H's SCR domain array.

**Clinical significance:** CFH mutations are the single most common genetic cause of atypical HUS (aHUS; ~20-30% of cases) [^fakhouri-2017-ahus-lancet]. The Y402H polymorphism in SCR7 is the strongest common genetic risk factor for **age-related macular degeneration (AMD)** — present in ~35% of Europeans and conferring ~2.5-4× AMD risk. Anti-CFH autoantibodies cause ~6-10% of aHUS, predominantly in children with CFHR1-CFHR3 gene deletion.

## Structure

### SCR domain architecture

Factor H is a **155 kDa plasma glycoprotein** composed entirely of 20 **short consensus repeat (SCR) domains** (also called complement control protein [CCP] modules), each ~60 amino acids, arranged in a beads-on-a-string flexible structure:

| SCR domain(s) | Function | Disease relevance |
|:-------------|:---------|:-----------------|
| **SCR1-4** | Factor I cofactor activity; C3b binding (primary); alternative C3 convertase decay | Loss-of-function mutations → aHUS |
| **SCR6-8** | Polyanion binding (heparin sulfate, sialic acid); C-reactive protein binding; AMD-associated **Y402H** polymorphism in SCR7 → reduced Bruch's membrane binding → drusen accumulation | Common AMD susceptibility variant |
| **SCR9-15** | Flexible linker; few characterized functions | Some rare aHUS variants |
| **SCR16-20** | C3b binding on host cell surfaces; major site of aHUS-associated mutations; CFHR1 binding (SCR19-20) | Hotspot for aHUS gain-of-function mutations that disrupt surface-specific regulation |

**Two C3b binding sites with distinct functions:**
- **SCR1-4:** High-affinity fluid-phase C3b binding; Factor I cofactor activity; does not discriminate host from foreign
- **SCR19-20:** Host-surface–specific C3b binding (requires polyanion co-recognition); provides the surface-discrimination that protects host cells

Most aHUS-associated CFH mutations cluster in **SCR19-20** — they selectively abolish surface-specific regulation while leaving fluid-phase regulation intact. Cells (endothelium, platelets) cannot recruit Factor H → uncontrolled complement activation on their surfaces → TMA. Paradoxically, these patients have normal total complement and C3 levels.

### Factor H-Related Proteins (CFHRs)

Five Factor H-Related proteins (CFHR1-5) are encoded by genes on chromosome 1q31.3 adjacent to CFH:

- **CFHR1:** Inhibits MAC (C5b-9) assembly; abundant in plasma; **CFHR1 deletion → anti-CFH antibodies** (autoimmune aHUS)
- **CFHR3:** Expressed with CFHR1; **CFHR1-CFHR3 deletion** (homozygous) is the strongest predisposing factor for anti-CFH antibody-associated aHUS in children
- **CFHR5:** Regulates complement on glomerular basement membrane; mutations → CFHR5 nephropathy (C3 glomerulopathy variant in Cypriots)
- **CFH/CFHR1 fusion gene:** Gain-of-function → dysregulated complement → some aHUS and C3G cases

### Factor I — the catalytic partner

Factor H acts exclusively as a **cofactor** — it has no intrinsic protease activity. The actual cleavage of C3b to iC3b is performed by **Factor I** (CFI), a serine protease. Factor H (SCR1-4) binds C3b → recruits Factor I → Factor I cleaves C3b α-chain at Arg1281 and Arg1298 → iC3b (can still opsonize via CR3/CR4, but can no longer form C3 convertase).

CFI mutations → aHUS (~5-10% of cases), indistinguishable from CFH-aHUS clinically.

## Function

### Alternative pathway regulation mechanism

**Without Factor H (foreign surface):**
1. Spontaneous C3 hydrolysis: C3 → C3(H₂O) + Bb → C3(H₂O)Bb (fluid-phase C3 convertase)
2. C3(H₂O)Bb cleaves more C3 → C3b deposits on surface
3. C3b + Factor B (cleaved by Factor D) → C3bBb (surface C3 convertase) → Properdin stabilizes
4. Amplification loop: C3bBb generates more C3b → more C3bBb → exponential amplification
5. Accumulation of C3b → C5 convertase (C3bBbC3b) → C5 cleavage → C5a + C5b → MAC

**With Factor H (host cell surface):**
1. C3b deposits on host cell
2. Factor H (SCR19-20) binds host polyanions AND C3b simultaneously → displaces Factor Bb (decay acceleration) → inactivates C3bBb
3. Factor H (SCR1-4) acts as Factor I cofactor → C3b → iC3b → C3d (each step loses convertase-forming ability)
4. Net result: C3b rapidly inactivated on host surface → no amplification → no MAC → host cell protected

**Factor H concentration and activation threshold:**
At 500 μg/mL, Factor H is present at ~10-100× the concentration of complement activating components — the pathway is under continuous active suppression. Any reduction in Factor H below ~20-30% of normal → loss of threshold control → breakthrough activation.

### AMD and drusen biology

**AMD mechanism (Y402H):**
- Bruch's membrane (between RPE and choroid) is rich in heparan sulfate proteoglycans
- Factor H Y402H variant (SCR7) → reduced binding affinity to heparan sulfate on Bruch's membrane
- Reduced local Factor H → complement activation → C3 fragments + MAC deposition → RPE damage → drusen accumulation → AMD
- AMD risk: Y402H homozygotes ~7× relative risk; heterozygotes ~2.5×
- **Pegcetacoplan** (APL2; C3 inhibitor) — approved for GA (geographic atrophy) in AMD (FDA 2023); avacopan and C5 inhibitors under investigation

## Mechanism

### aHUS — molecular pathophysiology

**Why renal endothelium is the primary target:**
Glomerular endothelium is fenestrated (lacks continuous basement membrane coverage) and directly exposed to blood at high surface-to-volume ratio → high complement activation pressure. Glomerular endothelial cells are particularly dependent on Factor H surface recruitment to suppress alternative pathway. SCR19-20 mutations → selective vulnerability of renal endothelium.

**TMA cascade:**
1. CFH mutation → loss of surface C3b regulation on GE cells
2. C3b amplification → C5 convertase → C5a + C5b-9
3. C5a → neutrophil/platelet priming, endothelial TF expression, MCP-1 (monocyte recruitment)
4. MAC (C5b-9) → sublytic endothelial injury → von Willebrand Factor (VWF) release → platelet adhesion/aggregation → thrombosis
5. Fibrin microthrombi in glomerular capillaries → occlusion → GFR drop → AKI
6. RBC fragmentation through fibrin strands → MAHA (microangiopathic hemolytic anemia)
7. Platelet consumption → thrombocytopenia
8. Repeated episodes → glomerular fibrosis → CKD → ESRD

### Complement regulatory drug targets

| Drug | Target | MOA | Indication |
|:-----|:-------|:----|:-----------|
| Eculizumab (Soliris) | C5 | Anti-C5 mAb; blocks C5 cleavage → no C5a + no MAC | aHUS, PNH, gMG, NMOSD |
| Ravulizumab (Ultomiris) | C5 | Long-acting anti-C5 mAb (Q8W); same MOA | aHUS, PNH, gMG |
| Iptacopan (Fabhalta) | Factor B | Oral Factor B inhibitor; blocks C3bBb assembly | PNH (FDA 2023); aHUS under study |
| Pegcetacoplan (Empaveli) | C3 | Pegylated C3 inhibitor; blocks all 3 pathways at C3 | PNH (geographic atrophy) |
| Danicopan | Factor D | Oral Factor D inhibitor; proximal alternative pathway | PNH adjunct (FDA 2024) |

## Connections

- `connects-to` → **[Atypical HUS](../../07-system/ahus/README.md)** — CFH loss-of-function mutations (SCR19-20 clustering) impair surface C3b regulation on renal endothelium → uncontrolled alternative pathway → TMA; anti-CFH antibodies cause aHUS in ~6-10% (especially CFHR1-CFHR3 deletion); eculizumab/ravulizumab are curative.
- `connects-to` → **[Complement C3](../complement-c3/README.md)** — Factor H accelerates decay of C3bBb (alternative C3 convertase) and acts as cofactor for Factor I-mediated C3b cleavage → iC3b; dysregulated alternative C3 convertase (CFH deficiency or C3NeF) → hypocomplementemia C3, aHUS, and C3 glomerulopathy.
- `connects-to` → **[Complement C5](../complement-c5/README.md)** — Uncontrolled alternative C3 convertase (from CFH deficiency) generates C3b → assembly of alternative C5 convertase (C3bBbC3b) → C5 cleavage → C5a (inflammation) + MAC (endothelial injury); eculizumab blocks C5 cleavage → prevents TMA in aHUS even without restoring CFH.

[^fakhouri-2017-ahus-lancet]: Fakhouri F, Zuber J, Frémeaux-Bacchi V, Loirat C. Haemolytic uraemic syndrome. *Lancet.* 2017;390(10095):681-696. [doi:10.1016/S0140-6736(17)30062-4](https://doi.org/10.1016/S0140-6736(17)30062-4) · [PubMed 28242109](https://pubmed.ncbi.nlm.nih.gov/28242109/)
[^chen-2010-cfh-y402h-amd]: Chen LJ, Liu DT, Tam PO, et al. Association of complement factor H polymorphisms with exudative age-related macular degeneration. *Ophthalmology.* 2006;113(3):516-519. [doi:10.1016/j.ophtha.2005.06.031](https://doi.org/10.1016/j.ophtha.2005.06.031) · [PubMed 17046868](https://pubmed.ncbi.nlm.nih.gov/17046868/)
[^zipfel-2009-factor-h-review]: Zipfel PF, Skerka C. Complement regulators and inhibitory proteins. *Nat Rev Immunol.* 2009;9(10):729-740. [doi:10.1038/nri2620](https://doi.org/10.1038/nri2620) · [PubMed 19756009](https://pubmed.ncbi.nlm.nih.gov/19756009/)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
