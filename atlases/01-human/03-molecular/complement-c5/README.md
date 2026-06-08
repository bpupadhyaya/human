---
schema: human-scale-entry/v1
id: complement-c5
name: Complement C5
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-07
summary: "Complement C5 (C5, chr9q33.2) is cleaved by C5 convertase → C5a (potent anaphylatoxin) + C5b (MAC assembly initiator); eculizumab and ravulizumab (anti-C5 mAbs) block terminal complement → approved for PNH, aHUS, gMG, NMOSD, and HSCT-TMA."
aliases: ["C5", "complement component 5", "C5a", "C5b", "C5b-9", "MAC", "terminal complement", "anaphylatoxin"]
cross_links:
  - target: 01-human/07-system/pnh
    relation: connects-to
    note: "In PNH, GPI-anchor-deficient RBCs lack CD55/CD59 → uncontrolled C5 cleavage → MAC (C5b-9) → hemolysis; C5a → neutrophil activation → thrombosis; eculizumab (C5 mAb) reduces hemolysis and thrombosis; ravulizumab (Q8W) achieves sustained C5 inhibition."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "C5a (C5aR1/C5aR2) → neutrophil/monocyte chemotaxis + NLRP3 inflammasome priming + Th1/Th17 polarization; C5b-9 MAC → cell lysis; dysregulated terminal complement → autoimmune injury in gMG (NMJ), NMOSD (astrocytes), aHUS (glomerular endothelium)."
  - target: 01-human/07-system/myasthenia-gravis
    relation: connects-to
    note: "Anti-AChR IgG in MG activates classical complement → C5a (inflammation) + C5b-9 MAC → AChR destruction at motor endplate → NMJ dysfunction; eculizumab (REGAIN trial) and ravulizumab (CHAMPION MG) block C5 cleavage → prevent MAC at the NMJ → reduce AChR+ MG severity."
  - target: 01-human/07-system/nmo
    relation: connects-to
    note: "AQP4-IgG+ NMOSD: classical complement → C5 → C5a + MAC → astrocyte lysis in CNS; eculizumab (PREVENT: ARR 0.02 vs 0.35; FDA Jun 2019) and ravulizumab (CHAMPION-NMOSD; FDA Jun 2023) block C5 → prevent astrocyte attack; C5 inhibition not effective in MOG-IgG+ NMOSD."
  - target: 01-human/03-molecular/aquaporin-4
    relation: connects-to
    note: "AQP4-IgG activates classical complement at astrocyte endfeet → C5 cleavage → C5b-9 MAC → astrocyte necrosis; blocking C5 (eculizumab, ravulizumab) prevents MAC formation on AQP4-expressing astrocytes and halts NMOSD attacks; OAP clustering amplifies C1q binding efficiency."
  - target: 01-human/03-molecular/c5ar1
    relation: connects-to
    note: "C5a is cleaved from C5 by C5 convertase; C5a binds C5aR1 (Kd ~1 nM) on neutrophils/macrophages → Gαi signaling → chemotaxis, degranulation, ROS, NETosis; avacopan (C5aR1 antagonist; ADVOCATE; FDA Oct 2021) blocks C5a–C5aR1 signaling without affecting C5b-9 MAC formation."
  - target: 01-human/07-system/anca-vasculitis
    relation: connects-to
    note: "C5a generated during ANCA vasculitis complement activation primes neutrophils via C5aR1 → surface PR3/MPO translocation → ANCA crosslinking → NETosis → pauci-immune vasculitis; avacopan (C5aR1 antagonist; FDA Oct 2021) enables steroid-sparing remission in GPA/MPA."
  - target: 01-human/03-molecular/beta2-glycoprotein-1
    relation: connects-to
    note: "Anti-B2GPI → complement activation (C3b deposition → C5a → neutrophil/platelet activation → thrombus amplification); eculizumab (anti-C5; FDA-approved for other indications) is used off-label for catastrophic APS (CAPS) refractory to anticoagulation and plasma exchange."
  - target: 01-human/07-system/antiphospholipid-syndrome
    relation: connects-to
    note: "Complement activation is central to APS thrombosis: anti-B2GPI → C3b → C5a → neutrophil/platelet priming and TF expression; C5 inhibition (eculizumab) is used off-label for catastrophic APS (CAPS; ~37% mortality) refractory to anticoagulation and plasmapheresis."
  - target: 01-human/07-system/ahus
    relation: connects-to
    note: "Uncontrolled alternative complement in aHUS (CFH/CFI mutations) generates C5 convertase → C5a (inflammatory) + MAC (endothelial injury → TMA); eculizumab/ravulizumab (anti-C5) are standard of care for aHUS; meningococcal prophylaxis mandatory with C5 blockade."
sources:
  - id: hillmen-2004-eculizumab-pnh
    type: peer-reviewed
    cite: "Hillmen P, Hall C, Marsh JC, et al. Effect of eculizumab on hemolysis and transfusion requirements in patients with paroxysmal nocturnal hemoglobinuria. N Engl J Med. 2004;350(6):552-559."
    doi: "10.1056/NEJMoa031688"
    pmid: "14762182"
    url: "https://doi.org/10.1056/NEJMoa031688"
  - id: brodsky-2008-eculizumab-triumph
    type: peer-reviewed
    cite: "Brodsky RA, Young NS, Antonioli E, et al. Multicenter phase 3 study of the complement inhibitor eculizumab for the treatment of patients with paroxysmal nocturnal hemoglobinuria. Blood. 2008;111(4):1840-1847."
    doi: "10.1182/blood-2007-06-094136"
    pmid: "18055865"
    url: "https://doi.org/10.1182/blood-2007-06-094136"
  - id: lee-2019-ravulizumab-pnh
    type: peer-reviewed
    cite: "Lee JW, Sicre de Fontbrune F, Wong Lee Lee L, et al. Ravulizumab (ALXN1210) vs eculizumab in adult patients with PNH naive to complement inhibitors. Blood. 2019;133(6):530-539."
    doi: "10.1182/blood-2018-09-876136"
    pmid: "30510080"
    url: "https://doi.org/10.1182/blood-2018-09-876136"
---

# Complement C5

## Overview

**Complement component C5** (gene *C5*, chromosome 9q33.2) is the **pivotal branchpoint protein of the terminal complement pathway**, positioned at the convergence of the three complement activation routes (classical, lectin, alternative). C5 is cleaved by **C5 convertase** — either classical/lectin (C4b2a3b) or alternative (C3bBbC3b) — into two biologically distinct fragments:

- **C5a (74 aa; 10 kDa):** The most potent endogenous anaphylatoxin; rapidly cleared by carboxypeptidase B → desArg-C5a (stable); signals via **C5aR1** (CD88; Gαi + Gαq → MAPK + PLCβ → Ca²⁺ flux + actin polymerization → chemotaxis, degranulation) and **C5aR2** (C5L2; β-arrestin-biased; modulatory role; may dampen inflammatory C5aR1 signaling); C5a drives neutrophil/monocyte chemotaxis, oxidative burst, NLRP3 inflammasome priming, mast cell degranulation, Th1/Th17 polarization, and vascular permeability increase
- **C5b (167 kDa; residual large fragment):** Noncovalently associates with C6 → C5b6 → recruits C7 → C5b67 inserts into bilayer → C8 → C9 polymerization (typically 12-18 C9 monomers) → **Membrane Attack Complex (MAC; C5b-9)** — a ~1 MDa amphipathic pore (~10 nm internal diameter) in the target cell membrane → osmotic lysis; sublytic MAC triggers intracellular signaling (Ca²⁺ influx, PI3K, complement receptor 3/integrin crosstalk) without killing

**Regulatory proteins protecting host cells from MAC:**
- **CD59 (protectin; MIRL):** GPI-anchored; binds C8 and C9 → prevents C9 polymerization → blocks MAC assembly; expressed on virtually all cell types; absent in PNH clone
- **CD55 (DAF, decay-accelerating factor):** GPI-anchored; accelerates decay of C3/C5 convertases → prevents C3b/C5 cleavage amplification; absent in PNH clone
- **Clusterin, vitronectin:** Soluble regulators that bind C5b-9 in fluid phase → inhibit membrane insertion

The clinical consequence of CD55/CD59 absence in **PNH (paroxysmal nocturnal hemoglobinuria)** — where a PIGA-mutant stem cell clone generates GPI-anchor-deficient RBCs, WBCs, and platelets — established terminal complement as a master therapeutic target. **Eculizumab** (Soliris; Alexion/AstraZeneca), a humanized anti-C5 IgG4/IgG2 hybrid mAb approved in 2007, was the first effective PNH treatment and transformed complement medicine [^hillmen-2004-eculizumab-pnh].

## Structure

**C5 protein:**
- Synthesized as 1676 aa pre-pro-C5; signal peptide cleavage → 1668 aa pro-C5; N-linked glycosylation → single-chain form processed by furin-like proprotein convertase → **mature heterodimer**: α-chain (999 aa, ~115 kDa) + β-chain (655 aa, ~75 kDa) linked by a disulfide bond; total ~190 kDa; circulates at 75-80 µg/mL (400 nM) — highest concentration of any terminal complement component
- **Domain structure:** α-chain contains the C5a anaphylatoxin domain (N-terminal, aa 1-74 of mature α) and the C5b fragment; β-chain contains MG (macroglobulin) domains 1-6; the mature heterodimer has MG1-6 (β-chain + N-terminal α-chain) + linker domains (LNK) + CUB + thioester-like domain (TED) — similar overall to C3/C4 architecture but lacks an active thioester
- **C5 convertase cleavage site:** Arg751 in the α-chain (between Arg751 and Leu752) → releases C5a (aa 1-74 of α-chain) + C5b (remainder of α-chain + intact β-chain)

**C5a receptor:**
- **C5aR1 (CD88; gene *C5AR1*, chr19q13.32):** Canonical Class A GPCR (7TM rhodopsin family); Gαi → ↓cAMP + Gαq → PLCβ → IP₃ + DAG → Ca²⁺ + PKC; β-arrestin → ERK, internalization; expressed on neutrophils (highest), monocytes/macrophages, mast cells, basophils, dendritic cells, microglia, astrocytes, cardiomyocytes, hepatocytes
- **C5aR2 (C5L2):** Does not couple to G-proteins; acts as scavenger/decoy receptor and potential modulatory co-receptor; expressed on neutrophils and monocytes; controversial biology — some studies show pro-inflammatory, others anti-inflammatory roles

**Eculizumab and ravulizumab structure:**
- **Eculizumab (Soliris):** Humanized IgG2/IgG4 chimeric mAb (variable region from murine anti-C5 clone; constant region engineered to reduce Fc effector function — Fc cannot bind C1q or activate classical pathway); binds C5 α-chain β-hairpin loop (CUB domain/TED domain interface) → allosterically blocks C5 convertase cleavage → cannot generate C5a or C5b; Kd ~20 pM; t½ ~12 days; 900 mg IV Q2W maintenance (after 600 mg Q1W induction × 4 weeks)
- **Ravulizumab (Ultomiris):** Engineered derivative of eculizumab with 4 amino acid substitutions (in FcRn-binding region to increase t½; in C5-binding CDRs to improve pH-dependent recycling) → t½ ~50 days vs. ~12 days for eculizumab; 3000 mg IV Q8W (body weight ≥100 kg) or 2700 mg Q8W — Q8W vs. Q2W dosing is major practical advantage

## Function

**Terminal complement in immunity:**
- **Bactericidal:** MAC is essential for killing encapsulated Gram-negative bacteria (*Neisseria meningitidis*, *N. gonorrhoeae*, *Haemophilus influenzae*); C5-deficient individuals and patients on anti-C5 therapy have markedly elevated risk of invasive meningococcal disease → **meningococcal vaccination mandatory before eculizumab/ravulizumab**; C5a also enhances opsonophagocytosis
- **Antiviral:** C5a and MAC contribute to antiviral defense; paradoxically, excessive complement activation in COVID-19 → cytokine storm + MAC on pneumocytes
- **Sterile inflammation:** C5a is a major driver of sterile inflammatory injury: myocardial ischemia-reperfusion → complement activation → C5a → neutrophil infiltration → injury; ARDS; sepsis (excessive C5a → immunoparalysis — neutrophils undergo apoptosis); AMD (age-related macular degeneration) → drusen activate complement → C5a/MAC → RPE injury

**C5 in disease:**

*Neuromuscular junction — Generalized Myasthenia Gravis (gMG):*
- Anti-AChR (acetylcholine receptor) IgG1/IgG3 antibodies → Fc → C1q → classical pathway → C3b deposition on NMJ → C5 convertase → C5a (neutrophil recruitment) + MAC → NMJ destruction → muscle weakness; complement-mediated NMJ injury is the dominant mechanism in anti-AChR gMG (vs. anti-MuSK gMG which uses IgG4 — no Fc effector)
- **Ravulizumab (CHAMPION-MG, 2022):** Phase 3 trial in anti-AChR+ gMG; ravulizumab 60 mg/kg IV Q8W vs. placebo; ADL composite score improvement –2.5 vs. –0.8 (p<0.001); 34% MG Activities of Daily Living responders vs. 22%; FDA approved April 2022
- **Eculizumab (REGAIN trial):** Phase 3 gMG; 26.4% vs. 14.7% MG-ADL responder rate; approved 2017 for gMG

*Neuromyelitis Optica Spectrum Disorder (NMOSD):*
- Anti-AQP4 (aquaporin-4) IgG → complement-mediated astrocyte destruction → optic neuritis, myelitis; complement is essential in anti-AQP4+ NMOSD (IgG1/IgG3 activate classical pathway → C5 → MAC on astrocytes → neuroinflammation)
- **Ravulizumab (CHAMPION-NMOSD, 2023):** Phase 3; 0 relapses vs. 20.3% placebo-relapse rate; FDA approved August 2023
- **Eculizumab (PREVENT trial, 2019):** 97.9% relapse-free vs. 63% placebo; FDA approved for AQP4+ NMOSD

## Mechanism

**PNH — complement-mediated hemolysis and thrombosis [^brodsky-2008-eculizumab-triumph]:**
- Alternative pathway spontaneously activates on any cell surface (tick-over hydrolysis of C3 → C3b deposition) → amplification by properdin + factor B + factor D → C3 convertase (C3bBb) → C3b → C5 convertase (C3bBbC3b) → C5 cleavage
- Normal cells: CD55 decays C3bBb; CD59 blocks MAC; GPI-anchored → protected
- PNH clone (PIGA mutation): No GPI synthesis → no CD55/CD59 → susceptibility to MAC lysis + C5a-driven thrombosis

**TRIUMPH and SHEPHERD trials (eculizumab in PNH) [^brodsky-2008-eculizumab-triumph]:**
- Hemolysis reduction: LDH (lactate dehydrogenase, intravascular hemolysis marker) ↓87% vs. placebo
- Transfusion independence: 49% vs. 0%; quality of life normalization
- Thrombosis: ~90% reduction in thrombotic events vs. historical controls
- Complement evasion: "Breakthrough hemolysis" occurs at end of dosing interval (C5 not completely suppressed) or with complement amplification triggers (infections) → ravulizumab's longer t½ minimizes this

**Ravulizumab vs. eculizumab (non-inferiority) [^lee-2019-ravulizumab-pnh]:**
- 301-301 in complement-naive PNH patients; LDH normalization rate: ravulizumab 53.6% vs. eculizumab 49.4% (non-inferior); transfusion avoidance: 73.6% vs. 66.1%; Q8W vs. Q2W dosing → 95% patient preference for ravulizumab
- Now first-choice for most PNH indications in treatment-naive patients

**Other C5 inhibitors:**
- **Iptacopan (Fabhalta; oral factor B inhibitor, not anti-C5):** Alternative pathway-selective complement inhibitor; oral QD; 2023 FDA approved for PNH → first oral complement inhibitor; 82% transfusion independence vs. 2% placebo; inhibits upstream of C5 (at C3 level) → also reduces C3 opsonin-mediated extravascular hemolysis (which anti-C5 agents miss)
- **Crovalimab (anti-C5 subcutaneous):** Monthly SC dosing; COMMODORE 1/2: non-inferior to eculizumab; FDA approved 2023; self-administration
- **Zilucoplan (anti-C5 subcutaneous peptide; SelfD for gMG):** SC QD self-injection; RAISE trial gMG; FDA approved 2023; convenient for non-infusion patients
- **Danicopan (oral factor D inhibitor):** Add-on to eculizumab/ravulizumab for PNH patients with residual extravascular hemolysis (C3b-mediated); FDA approved 2023

## Connections

In PNH, GPI-anchor-deficient RBCs lack CD55/CD59 → uncontrolled C5 cleavage → MAC (C5b-9) → hemolysis; C5a → neutrophil activation → thrombosis; eculizumab (C5 mAb) reduces hemolysis and thrombosis; ravulizumab (Q8W) achieves sustained C5 inhibition.

C5 links innate complement to adaptive immunity: C5a (C5aR1/C5aR2) → neutrophil/monocyte chemotaxis + NLRP3 priming + Th1/Th17 polarization; C5b-9 MAC → cell lysis; dysregulated C5 activation → autoimmune injury in gMG (neuromuscular junction), NMOSD (astrocytes), aHUS (glomerular endothelium).

- `connects-to` → **[PNH](../../07-system/pnh/README.md)** — In PNH, GPI-anchor-deficient RBCs lack CD55/CD59 → uncontrolled C5 cleavage → MAC (C5b-9) → hemolysis; C5a → neutrophil activation → thrombosis; eculizumab (C5 mAb) reduces hemolysis and thrombosis; ravulizumab (Q8W) achieves sustained C5 inhibition.
- `connects-to` → **[Immune System](../../07-system/immune-system/README.md)** — C5 links innate complement to adaptive immunity: C5a (C5aR1/C5aR2) → neutrophil/monocyte chemotaxis + NLRP3 priming + Th1/Th17 polarization; C5b-9 MAC → cell lysis; dysregulated C5 activation → autoimmune injury in gMG (neuromuscular junction), NMOSD (astrocytes), aHUS (glomerular endothelium).
- `connects-to` → **[Myasthenia Gravis](../../07-system/myasthenia-gravis/README.md)** — Anti-AChR IgG in MG activates classical complement → C5a (inflammation) + C5b-9 MAC → AChR destruction at motor endplate → NMJ dysfunction; eculizumab (REGAIN trial) and ravulizumab (CHAMPION MG) block C5 cleavage → prevent MAC at the NMJ → reduce AChR+ MG severity.
- `connects-to` → **[NMOSD](../../07-system/nmo/README.md)** — AQP4-IgG+ NMOSD: classical complement → C5 → C5a + MAC → astrocyte lysis in CNS; eculizumab (PREVENT: ARR 0.02 vs 0.35; FDA Jun 2019) and ravulizumab (CHAMPION-NMOSD; FDA Jun 2023) block C5 → prevent astrocyte attack; not effective in MOG-IgG+ NMOSD.
- `connects-to` → **[Aquaporin-4](../aquaporin-4/README.md)** — AQP4-IgG activates classical complement at astrocyte endfeet → C5 cleavage → C5b-9 MAC → astrocyte necrosis; blocking C5 (eculizumab, ravulizumab) prevents MAC formation on AQP4-expressing astrocytes; OAP clustering amplifies C1q binding efficiency.
- `connects-to` → **[C5aR1](../c5ar1/README.md)** — C5a binds C5aR1 (Kd ~1 nM) on neutrophils/macrophages → Gαi → chemotaxis, degranulation, ROS, NETosis; avacopan (C5aR1 antagonist; ADVOCATE; FDA Oct 2021) blocks C5a–C5aR1 signaling downstream of C5 without affecting C5b-9 MAC formation.
- `connects-to` → **[ANCA Vasculitis](../../07-system/anca-vasculitis/README.md)** — C5a primes neutrophils via C5aR1 → surface PR3/MPO translocation → ANCA crosslinking → NETosis → pauci-immune vasculitis; avacopan (C5aR1 antagonist; FDA Oct 2021) enables steroid-sparing remission in GPA/MPA by blocking C5a signaling.
- `connects-to` → **[Beta-2 Glycoprotein I](../beta2-glycoprotein-1/README.md)** — Anti-B2GPI → complement activation (C3b deposition → C5a → neutrophil/platelet activation → thrombus amplification); eculizumab (anti-C5; FDA-approved for other indications) is used off-label for catastrophic APS (CAPS) refractory to anticoagulation and plasma exchange.
- `connects-to` → **[Antiphospholipid Syndrome](../../07-system/antiphospholipid-syndrome/README.md)** — Complement activation is central to APS thrombosis: anti-B2GPI → C3b → C5a → neutrophil/platelet priming and TF expression; C5 inhibition (eculizumab) is used off-label for catastrophic APS (CAPS; ~37% mortality) refractory to anticoagulation and plasmapheresis.
- `connects-to` → **[Atypical HUS](../../07-system/ahus/README.md)** — Uncontrolled alternative complement in aHUS (CFH/CFI mutations) generates C5 convertase → C5a (inflammatory) + MAC (endothelial injury → TMA); eculizumab/ravulizumab (anti-C5) are standard of care for aHUS; meningococcal prophylaxis mandatory with C5 blockade.

[^hillmen-2004-eculizumab-pnh]: Hillmen P, Hall C, Marsh JC, et al. Effect of eculizumab on hemolysis and transfusion requirements in patients with paroxysmal nocturnal hemoglobinuria. *N Engl J Med.* 2004;350(6):552-559. [doi:10.1056/NEJMoa031688](https://doi.org/10.1056/NEJMoa031688) · [PubMed 14762182](https://pubmed.ncbi.nlm.nih.gov/14762182/)
[^brodsky-2008-eculizumab-triumph]: Brodsky RA, Young NS, Antonioli E, et al. Multicenter phase 3 study of the complement inhibitor eculizumab for the treatment of patients with paroxysmal nocturnal hemoglobinuria. *Blood.* 2008;111(4):1840-1847. [doi:10.1182/blood-2007-06-094136](https://doi.org/10.1182/blood-2007-06-094136) · [PubMed 18055865](https://pubmed.ncbi.nlm.nih.gov/18055865/)
[^lee-2019-ravulizumab-pnh]: Lee JW, Sicre de Fontbrune F, Wong Lee Lee L, et al. Ravulizumab (ALXN1210) vs eculizumab in adult patients with PNH naive to complement inhibitors. *Blood.* 2019;133(6):530-539. [doi:10.1182/blood-2018-09-876136](https://doi.org/10.1182/blood-2018-09-876136) · [PubMed 30510080](https://pubmed.ncbi.nlm.nih.gov/30510080/)
