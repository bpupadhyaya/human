---
schema: human-scale-entry/v1
id: neutrophil
name: Neutrophil
atlas: 01-human
scale: 04-cellular
status: draft
last_reviewed: 2026-06-05
summary: "Most abundant circulating leukocyte (50–70% of WBC); first-responder innate immune cell produced at ~10¹¹/day in bone marrow. Kills bacteria and fungi via phagocytosis, respiratory burst (NADPH oxidase/MPO/HOCl), degranulation, and neutrophil extracellular traps (NETs)."
aliases: ["PMN", "polymorphonuclear leukocyte", "granulocyte", "poly"]
sources:
  - id: alberts-mol-cell-biology
    type: textbook
    cite: "Alberts B, Johnson A, Lewis J, et al. Molecular Biology of the Cell. 7th ed. W.W. Norton; 2022."
    url: "https://www.ncbi.nlm.nih.gov/books/NBK26880/"
    accessed: "2026-06-05"
  - id: janeway-immunobiology
    type: textbook
    cite: "Murphy K, Weaver C. Janeway's Immunobiology. 9th ed. Garland Science; 2017."
    url: "https://www.garlandscience.com/product/isbn/9780815345053"
    accessed: "2026-06-05"
cross_links:
  - target: 01-human/05-tissue/bone-marrow
    relation: part-of
    note: "Neutrophils are produced at ~10¹¹/day from myeloid progenitors in bone marrow (CFU-GM → myeloblast → promyelocyte → myelocyte → metamyelocyte → band → neutrophil); G-CSF (CSF3) drives terminal maturation."
  - target: 01-human/07-system/immune-system
    relation: part-of
    note: "Neutrophils are the first-responder innate immune cells; they arrive at infection sites within minutes, deploying phagocytosis, respiratory burst, degranulation, and NETs against bacteria and fungi."
  - target: 01-human/04-cellular/macrophage
    relation: modulates
    note: "Neutrophil-derived CXCL8 and azurocidin recruit monocytes; apoptotic neutrophils are cleared by macrophage efferocytosis; neutrophil–macrophage crosstalk shapes the transition from acute to chronic inflammation."
  - target: 01-human/06-organ/liver
    relation: modulates
    note: "Hepatic neutrophil infiltration (via CXCL1/CXCL2/CXCL8) drives acute liver injury in ischaemia-reperfusion, alcoholic hepatitis, and NASH; NET components activate Kupffer cells via TLR4/TLR9, amplifying inflammation."
  - target: 02-pathogen/02-bacteria/streptococcus-pyogenes
    relation: infected-by
    note: "Infected by Streptococcus pyogenes."
  - target: 02-pathogen/02-bacteria/clostridioides-difficile
    relation: damaged-by
    note: "Damaged by Clostridioides difficile."
  - target: 02-pathogen/02-bacteria/neisseria-meningitidis
    relation: infected-by
    note: "Infected by Neisseria meningitidis."
  - target: 01-human/03-molecular/g6pd
    relation: connects-to
    note: "Neutrophil NOX2 requires G6PD-derived NADPH to generate superoxide for oxidative burst; G6PD-deficient patients have impaired neutrophil bactericidal killing; severe G6PD deficiency (Class I) may present with recurrent bacterial infections from NOX2 substrate deficit."
---

# Neutrophil

## Overview

The neutrophil (polymorphonuclear leukocyte, PMN) is the most abundant circulating white blood cell, comprising 50–70% of all leukocytes (2–7.5×10⁹/L in adult blood). It is the central first-responder of innate immunity, recruited within minutes of tissue infection or injury. Neutrophils are short-lived but are produced in vast numbers — approximately 10¹¹ cells per day — from myeloid progenitors in the bone marrow.[^alberts-mol-cell-biology] Their name reflects the neutral (weakly eosinophilic) staining of their cytoplasm with Romanowsky-type dyes.[^janeway-immunobiology]

Neutrophils occupy a critical position at the interface of early pathogen containment: they deploy a multi-layered antimicrobial arsenal — phagocytosis, oxidative burst via NADPH oxidase, granule-mediated enzymatic killing, and the expulsion of neutrophil extracellular traps (NETs) — while simultaneously orchestrating subsequent monocyte and macrophage recruitment. Their dysregulation contributes to sterile inflammatory injury (ARDS, ischaemia-reperfusion), autoimmune vasculitis (ANCA-associated vasculitides), and immunodeficiency (chronic granulomatous disease, CGD).[^janeway-immunobiology]

## Structure

**Morphology.** Mature neutrophils are 12–15 µm in diameter. The defining morphological feature is the multilobed nucleus: 3–5 nuclear lobes connected by thin chromatin filaments visible on peripheral blood smear — the basis of the "polymorphonuclear" descriptor. Female neutrophils may display a drumstick-shaped Barr body appendage on one lobe (inactive X chromosome).[^alberts-mol-cell-biology]

**Granule types.** The neutrophil cytoplasm is packed with four granule subsets, each released in a hierarchically ordered fashion (secretory vesicles first, then tertiary, secondary, and finally primary granules):

- **Primary (azurophil) granules** (~0.4 µm; released into phagosome): myeloperoxidase (MPO), neutrophil elastase (ELANE), cathepsin G, proteinase 3 (PR3), α-defensins (HNP1–4), azurocidin, bactericidal/permeability-increasing protein (BPI). These fuse with the phagosome to deliver enzymatic killing.
- **Secondary (specific) granules** (~0.3 µm; most numerous): lactoferrin, collagenase (MMP-8), hCAP18/LL-37 (cathelicidin), vitamin B12-binding protein (transcobalamin I), NGAL (lipocalin-2). Their membranes carry CR3 (CD11b/CD18) and CXCR2, which are rapidly translocated to the plasma membrane upon activation, enhancing adhesion and chemotaxis.
- **Tertiary (gelatinase) granules**: gelatinase/MMP-9, leukolysin (MT6-MMP), acetyltransferase; easily mobilised to aid basement-membrane penetration during transendothelial migration.
- **Secretory vesicles**: albumin-containing endocytic vesicles; most readily mobilised; deliver fMLP receptor (FPR1) and CR3 to the surface upon even low-level stimulation, priming the cell for chemotaxis.[^janeway-immunobiology]

**Plasma membrane receptors.** Key surface molecules include FcγRIIA (CD32) and FcγRIII (CD16) for IgG-opsonised targets; CR1 (CD35) and CR3 (CD11b/CD18) for complement-opsonised targets; CXCR1/CXCR2 for IL-8 (CXCL8) and CXCL1/2; FPR1 for formyl peptides (fMLF, bacterial signal); C5aR1 (CD88); TLR4 and other pattern-recognition receptors.[^alberts-mol-cell-biology]

## Function

**Recruitment cascade.** Neutrophils exit the bone marrow and enter the bloodstream, marginating along post-capillary venules at sites of inflammation through a coordinated adhesion cascade:

1. **Rolling**: P-selectin (endothelium, constitutive on Weibel-Palade bodies; also platelets) and E-selectin (endothelium, induced within 1–2 h by IL-1β/TNF-α) bind PSGL-1 (CD162) and L-selectin on neutrophils, decelerating them from free flow to rolling (~1–50 µm/s).[^janeway-immunobiology]
2. **Chemokine activation**: CXCL8 (IL-8), C5a, and fMLF presented on heparan-sulphate proteoglycans on the endothelial surface bind their respective GPCRs on the rolling neutrophil → Gαi signalling → PI3Kγ → PIP3 → PLC → IP₃ → Ca²⁺ → inside-out integrin activation.
3. **Firm adhesion**: LFA-1 (αLβ2/CD11a-CD18) and Mac-1 (αMβ2/CD11b-CD18) extend to high-affinity conformation and bind ICAM-1/ICAM-2 on endothelium, arresting the neutrophil.[^alberts-mol-cell-biology]
4. **Transmigration (diapedesis)**: PECAM-1 (CD31) homophilic interactions and JAM proteins guide paracellular or transcellular migration; MMP-9 and MMP-8 from tertiary/secondary granules degrade the basement membrane collagen IV and laminin.
5. **Chemotaxis**: directed migration up CXCL8, C5a, LTB4, and fMLF gradients via MAPK, PI3K, and Rho GTPase-driven cytoskeletal F-actin polymerisation at the leading edge and myosin II-driven retraction at the uropod.[^janeway-immunobiology]

**Phagocytosis.** Recognition of opsonised targets (IgG via FcγRII/III; C3b via CR1/CR3) triggers pseudopod extension, phagosome formation, and phagolysosome fusion. Granule contents flood the phagosomal lumen.[^alberts-mol-cell-biology]

**Oxidative (respiratory) burst.** NOX2 NADPH oxidase (gp91phox/p22phox heterodimer in membrane; cytosolic p47phox, p67phox, p40phox, Rac2) assembles at the phagosomal membrane → superoxide (O₂•⁻) → dismutation to H₂O₂ → MPO catalyses H₂O₂ + Cl⁻ → hypochlorous acid (HOCl), the most potent neutrophil antimicrobial. Hydroxyl radical (OH•, Fenton) and singlet oxygen (¹O₂) also contribute.[^janeway-immunobiology]

**Degranulation.** Granules fuse sequentially with the phagosomal or plasma membrane, releasing elastase, MPO, defensins, lactoferrin, and MMP-8/9 into either the phagolysosomal compartment (contained killing) or the extracellular space (bystander tissue damage).[^alberts-mol-cell-biology]

**Neutrophil extracellular traps (NETs).** Stimulated by PMA, LPS, IL-8, activated platelets, or fungi: neutrophils expel decondensed DNA scaffolded with histones (citrullinated at H3Cit4 by PAD4), MPO, elastase, and LL-37, forming extracellular mesh structures that immobilise and kill bacteria/fungi. "Suicidal" NETosis involves cell lysis (ROS-dependent PAD4 activation); "vital" NETosis releases NETs while the neutrophil survives (via vesicle extrusion).[^janeway-immunobiology]

**Cytokine production.** Beyond antimicrobial killing, neutrophils secrete IL-1β (NLRP3 inflammasome-dependent), TNF-α, CXCL8 (autocrine amplification), G-CSF (CSF3), IL-12 (p70), and VEGF, shaping the inflammatory milieu and bridging innate to adaptive responses.[^alberts-mol-cell-biology]

## Lifecycle

**Granulopoiesis.** In the bone marrow, haematopoietic stem cells (HSCs) commit via CFU-GM (granulocyte-monocyte progenitor) → myeloblast → promyelocyte (primary granule synthesis) → myelocyte (secondary granule synthesis) → metamyelocyte → band neutrophil → segmented (mature) neutrophil. The entire maturation takes ~14 days. G-CSF (CSF3) binding to its receptor (G-CSFR, encoded by CSF3R) is the primary driver of terminal maturation and release. The bone marrow maintains a large reserve of post-mitotic neutrophils (~10× the circulating pool) that can be rapidly mobilised by G-CSF, CXCR4 antagonism (AMD3100), or C3a.[^alberts-mol-cell-biology]

**Circulating phase.** Once released, neutrophils circulate for 6–8 hours (half-life). CXCR4:CXCL12 interactions retain neutrophils in bone marrow; CXCR2:CXCL1/2 on endothelium drive egress. Ageing neutrophils downregulate CXCR2 and upregulate CXCR4, causing them to return to bone marrow for disposal ("neutrophil ageing").[^janeway-immunobiology]

**Tissue phase and apoptosis.** In infected or inflamed tissues, neutrophils survive 1–4 days (G-CSF, GM-CSF, IL-8, and hypoxia extend survival by inhibiting Mcl-1 degradation). After performing their effector functions, they undergo spontaneous or activation-induced apoptosis — caspase-3/9-mediated, regulated by Mcl-1/Bcl-xL balance. Apoptotic neutrophils display phosphatidylserine (PS) and calreticulin "eat-me" signals.[^alberts-mol-cell-biology]

**Efferocytosis and resolution.** Apoptotic neutrophils are cleared by tissue macrophages (via MerTK, LRP1, TIM-4, and PS receptors) in a process called efferocytosis. This triggers the macrophage to switch toward an anti-inflammatory/pro-resolving phenotype (↑IL-10, TGF-β, ↓TNF-α), driving resolution. Defective efferocytosis leads to secondary necrosis and chronic inflammation.[^janeway-immunobiology]

## Connections

- **Part of Bone Marrow** (`../../05-tissue/bone-marrow/README.md`): Neutrophils are produced at ~10¹¹/day from myeloid progenitors in bone marrow (CFU-GM → myeloblast → promyelocyte → myelocyte → metamyelocyte → band → neutrophil); G-CSF (CSF3) drives terminal maturation.[^alberts-mol-cell-biology]
- **Part of Immune System** (`../../07-system/immune-system/README.md`): Neutrophils are the first-responder innate immune cells; they arrive at infection sites within minutes, deploying phagocytosis, respiratory burst, degranulation, and NETs against bacteria and fungi.[^janeway-immunobiology]
- **Modulates Macrophage** (`../macrophage/README.md`): Neutrophil-derived CXCL8 and azurocidin recruit monocytes; apoptotic neutrophils are cleared by macrophage efferocytosis; neutrophil–macrophage crosstalk shapes the transition from acute to chronic inflammation.[^alberts-mol-cell-biology]
- **Modulates Liver** (`../../06-organ/liver/README.md`): Hepatic neutrophil infiltration (via CXCL1/CXCL2/CXCL8) drives acute liver injury in ischaemia-reperfusion, alcoholic hepatitis, and NASH; NET components activate Kupffer cells via TLR4/TLR9, amplifying inflammation.[^janeway-immunobiology]
- `connects-to` → **[G6PD](../../03-molecular/g6pd/README.md)** — Neutrophil NOX2 requires G6PD-derived NADPH to generate superoxide for oxidative burst; G6PD-deficient patients have impaired neutrophil bactericidal killing; severe G6PD deficiency (Class I) may present with recurrent bacterial infections from NOX2 substrate deficit.

## Pathology

**Neutropenia.** Absolute neutrophil count (ANC) below 1.5×10⁹/L; severe neutropenia (ANC <0.5×10⁹/L) causes febrile neutropenia — life-threatening susceptibility to gram-negative bacteraemia and invasive fungal infections. Causes include chemotherapy myelosuppression, aplastic anaemia, cyclic neutropenia (ELANE mutations), autoimmune neutropenia.[^janeway-immunobiology]

**Chronic granulomatous disease (CGD).** X-linked (gp91phox/CYBB mutations, 70%) or autosomal recessive (p47phox/NCF1, p67phox/NCF2, p22phox/CYBA subunit mutations). NOX2 NADPH oxidase non-functional → absent oxidative burst → recurrent infections with catalase-positive organisms (Staphylococcus aureus, Aspergillus, Nocardia, Burkholderia cepacia) and granuloma formation. Diagnose with dihydrorhodamine (DHR) flow cytometry. Treat with IFN-γ prophylaxis, TMP-SMX; cure with HSCT or gene therapy.[^alberts-mol-cell-biology]

**MPO deficiency.** Most common primary neutrophil disorder; usually asymptomatic (compensatory prolonged respiratory burst); increased risk of Candida infections in concurrent diabetes mellitus. Detected by automated haematology analysers (MPO channel).[^janeway-immunobiology]

**ANCA-associated vasculitis (AAV).** NET-derived MPO and PR3 serve as autoantigens; anti-MPO (p-ANCA) and anti-PR3 (c-ANCA) antibodies bind primed neutrophils → FcγR activation → NETosis → vascular injury in glomerulonephritis (MPA, GPA), eosinophilic GPA (EGPA).[^janeway-immunobiology]

**COVID-19 hyperactivation.** SARS-CoV-2 infection drives excessive NETosis; NET-derived DNA/histones trigger endothelial damage, complement activation, platelet activation, and microvascular thrombosis. NET burden correlates with COVID-19 severity and ARDS.[^alberts-mol-cell-biology]

**Leukemoid reaction / CML.** Extreme neutrophilia (>25×10⁹/L) with left shift; distinguish from CML by leukocyte alkaline phosphatase (LAP) score (high in leukemoid, low in CML) and BCR-ABL testing.[^janeway-immunobiology]

## See Also

- [`../../05-tissue/bone-marrow/README.md`](../../05-tissue/bone-marrow/README.md) — site of neutrophil production and maturation
- [`../../07-system/immune-system/README.md`](../../07-system/immune-system/README.md) — innate immune system context
- [`../macrophage/README.md`](../macrophage/README.md) — innate immune partner; efferocytosis and resolution
- [`../../06-organ/liver/README.md`](../../06-organ/liver/README.md) — neutrophil-driven hepatic injury
- [`../dendritic-cell/README.md`](../dendritic-cell/README.md) — DC activation by neutrophil-derived alarmins
- [`../../03-molecular/il-6/README.md`](../../03-molecular/il-6/README.md) — cytokine amplifying neutrophil-driven inflammation
- [`../../03-molecular/tnf-alpha/README.md`](../../03-molecular/tnf-alpha/README.md) — TNF-α upregulates endothelial E-selectin and ICAM-1 driving neutrophil recruitment

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
