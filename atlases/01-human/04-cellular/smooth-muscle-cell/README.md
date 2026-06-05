---
schema: human-scale-entry/v1
id: smooth-muscle-cell
name: Smooth Muscle Cell
atlas: 01-human
scale: 04-cellular
status: draft
last_reviewed: 2026-06-05
summary: "Involuntary, non-striated, mononucleated cells lining blood vessels, airways, GI tract, bladder, and uterus. Contraction via Ca²⁺-calmodulin-MLCK axis and Rho kinase; relaxation by NO/cGMP/PKG. Phenotype switching from contractile to synthetic drives atherosclerosis and PAH."
aliases: ["SMC", "vascular smooth muscle cell", "VSMC", "visceral smooth muscle", "myometrium cell"]
sources:
  - id: alberts-mol-cell-biology
    type: textbook
    cite: "Alberts B, Johnson A, Lewis J, et al. Molecular Biology of the Cell. 7th ed. W.W. Norton; 2022."
    url: "https://www.ncbi.nlm.nih.gov/books/NBK26880/"
    accessed: "2026-06-05"
  - id: guyton-hall
    type: textbook
    cite: "Hall JE, Hall ME. Guyton and Hall Textbook of Medical Physiology. 14th ed. Elsevier; 2021."
    url: "https://www.elsevier.com/books/guyton-and-hall-textbook-of-medical-physiology/hall/978-0-323-59712-8"
    accessed: "2026-06-05"
cross_links:
  - target: 01-human/07-system/cardiovascular-system
    relation: part-of
    note: "Vascular SMCs in the tunica media regulate vascular tone via MLC20 phosphorylation/MLCK; phenotype switching from contractile to synthetic drives atherosclerotic plaque formation and neointimal hyperplasia."
  - target: 01-human/03-molecular/nitric-oxide
    relation: modulates
    note: "eNOS-derived NO diffuses from endothelial cells to vascular SMCs → activates soluble guanylyl cyclase → cGMP → PKG → MLCP activation → MLC20 dephosphorylation → relaxation; NO is the primary vasodilatory signal."
  - target: 03-medicine/01-modern/04-cardio/calcium-channel-blockers
    relation: modulated-by
    note: "Dihydropyridine CCBs (amlodipine, nifedipine) block L-type Cav1.2 on vascular SMCs → ↓Ca²⁺ entry → ↓MLCK activation → vasodilation → ↓TPR → ↓BP; vascular selectivity via tissue-specific splicing."
  - target: 01-human/07-system/respiratory-system
    relation: modulates
    note: "Airway SMCs in tracheal/bronchial walls control airway calibre; β2-AR agonists → cAMP → PKA → ↓MLCK → bronchodilation; muscarinic M3 → contraction → bronchoconstriction in asthma."
---

# Smooth Muscle Cell

## Overview

Smooth muscle cells (SMCs) are involuntary, non-striated, mononucleated cells that constitute the contractile layer of hollow visceral organs and blood vessels throughout the body. Unlike skeletal and cardiac muscle, smooth muscle lacks sarcomeric organisation and troponin-based regulation; instead, contraction is governed by calcium-calmodulin activation of myosin light chain kinase (MLCK) and augmented by the Rho kinase (ROCK) pathway. SMCs respond to autonomic neural input, circulating hormones, local paracrine mediators, and mechanical stretch, making them essential integrators of vascular tone, airway resistance, gastrointestinal motility, urinary and reproductive function.[^alberts-mol-cell-biology][^guyton-hall]

SMCs are found in the tunica media of arteries and veins, the muscularis layer of airways (tracheobronchial), the muscularis externa of the gastrointestinal tract, the ureter, bladder detrusor, uterine myometrium, iris dilator/sphincter, ciliary body, and arrector pili of hair follicles. Vascular SMCs (VSMCs) are of particular clinical relevance: their contractile state determines peripheral vascular resistance and blood pressure, and their capacity for phenotypic switching underlies major vascular diseases including atherosclerosis, pulmonary arterial hypertension (PAH), and restenosis.

## Structure

**Morphology.** SMCs are spindle-shaped with tapered ends, ranging from 20 µm (arteriole) to 500 µm (pregnant uterus) in length and 5–10 µm in diameter. Each cell has a single, central, elongated nucleus that becomes corkscrew-shaped when the cell contracts — a distinguishing histological feature. The cytoplasm contains abundant thin and thick filaments without regular Z-line alignment.[^alberts-mol-cell-biology]

**Contractile apparatus.** Thin filaments are composed of α-smooth muscle actin (αSMA, ACTA2) and tropomyosin (without a troponin complex — the key difference from striated muscle). Thick filaments are formed by smooth muscle myosin II (SMMHC, MYH11). Instead of sarcomeres, SMCs organise filaments around **dense bodies** (cytoplasmic, contain α-actinin) and **dense plaques** (membrane-associated, contain α-actinin, vinculin, talin, and integrins that anchor to the extracellular matrix). Intermediate filaments (desmin in visceral, vimentin in vascular SMC) connect dense bodies to the sarcolemma, transmitting contractile force to the cell exterior.

**Specialised membrane domains.** The SMC plasma membrane contains abundant caveolae (caveolin-1, 50–100 nm flask-shaped invaginations), which act as Ca²⁺ signalling microdomains and scaffolds for signalling proteins (eNOS, Gα subunits, PKC). Gap junctions (connexin 43, 40) couple adjacent SMCs electrically and metabolically in the vascular wall.[^guyton-hall]

**Ca²⁺ handling organelles.** The sarcoplasmic reticulum (SR) is less developed than in cardiac muscle but contains IP₃ receptors (IP₃R) and ryanodine receptors (RyR) for Ca²⁺ release. Plasma membrane L-type voltage-gated Ca²⁺ channels (Cav1.2), receptor-operated channels (TRPC), and store-operated channels (STIM1/Orai1) mediate Ca²⁺ entry. SERCA2b and plasma membrane Ca²⁺ ATPase (PMCA) return Ca²⁺ to SR and extracellular space.

## Function

**Contraction mechanism.** Cytosolic Ca²⁺ rise ([Ca²⁺]i ↑ from ~100 nM to 600–1000 nM) triggers:
1. Ca²⁺ + calmodulin (CaM, 4:1 complex) → Ca²⁺-CaM → binds and activates MLCK (myosin light chain kinase).
2. MLCK phosphorylates MLC₂₀ at Ser19 (and secondarily Thr18) of regulatory myosin light chain → myosin ATPase activation → cross-bridge cycling → force generation.
3. **Rho kinase (ROCK) pathway:** Vasoconstrictor agonists (ET-1, Ang II, norepinephrine) activate Gα₁₂/₁₃ → RhoGEF → RhoA-GTP → activates ROCK (ROCK1/2) → phosphorylates MYPT1 (myosin phosphatase targeting subunit 1) → inhibits myosin light chain phosphatase (MLCP) → sustained MLC₂₀ phosphorylation at any given [Ca²⁺] ("Ca²⁺ sensitisation").[^guyton-hall]

**Relaxation.** ↓[Ca²⁺]i (SERCA pumps Ca²⁺ into SR; PMCA extrudes Ca²⁺) → CaM dissociates from MLCK → MLCK inactivation; simultaneously, MLCP (PP1cδ/MYPT1/M20 complex) dephosphorylates MLC₂₀ → cross-bridge detachment → relaxation. Pharmacological relaxation: NO → soluble guanylyl cyclase (sGC) → cGMP → PKG → (a) MYPT1 phosphorylation at Ser695 → ↑MLCP activity; (b) phosphorylates BKCa → hyperpolarisation → ↓Cav1.2 → ↓Ca²⁺ entry; (c) phosphorylates MLCK at Ser512 → ↓MLCK affinity for Ca²⁺-CaM.[^alberts-mol-cell-biology]

**Vascular tone regulation.**
- *Vasoconstrictors:* Norepinephrine (α₁R → Gq → PLC → IP₃ → ER Ca²⁺ release), angiotensin II (AT₁R → Gq), endothelin-1 (ETA → Gq), serotonin (5-HT₂A → Gq), thromboxane A₂ (TP → Gq), ROCK amplification.
- *Vasodilators:* NO (sGC → cGMP → PKG), prostacyclin/PGI₂ (IP → Gs → cAMP → PKA → MLCK inhibition + BKCa opening), adenosine (A₂A → Gs), β₂-adrenergic agonists (Gs → cAMP → PKA), ANP (GC-A → cGMP), EDHF (endothelium-derived hyperpolarising factor via gap junctions and K⁺ channels).[^guyton-hall]

**Phenotype switching (key concept).** VSMCs exist on a phenotypic continuum:
- *Contractile/quiescent:* Low proliferation; high expression of αSMA, SMMHC (MYH11), calponin (CNN1), SM22α (TAGLN). This is the normal adult vascular phenotype.
- *Synthetic/proliferative:* Downregulation of contractile markers; ↑collagen/ECM synthesis, ↑growth factor receptors (PDGFR-β), ↑migration capacity; driven by PDGF-BB, oxidised LDL, angiotensin II, TGF-β, inflammatory cytokines.

Switching is a core mechanism in vascular disease: in atherosclerosis, synthetic SMCs migrate from media to intima, proliferate, produce ECM, and engulf lipids (SMC-derived foam cells comprise ~50% of advanced plaques); in PAH, medial SMC hypertrophy and proliferation narrow pulmonary arterioles.[^alberts-mol-cell-biology]

## Lifecycle

SMCs are derived from multiple developmental origins depending on location: neural crest (head/neck vessels, cardiac outflow tract), lateral plate mesoderm (limb and trunk vessels), paraxial mesoderm (dorsal aorta), and secondary heart field. Adult SMCs are long-lived (months to years) and are normally quiescent (low turnover). They retain remarkable plasticity:

1. **Quiescent SMC (contractile):** High MRTFs (myocardin, MRTF-A/B) drive CArG-box-dependent expression of contractile genes (αSMA, MYH11, CNN1, TAGLN) in concert with serum response factor (SRF).
2. **Phenotypic switch:** Growth factors (PDGF-BB via PDGFR-β → ERK/Akt) and KLF4 upregulation → represses myocardin → downregulates contractile markers → activates synthetic programme. This is reversible.
3. **Foam cell differentiation:** In atherosclerosis, SMCs expressing KLF4 and downregulating ACTA2/MYH11 can take up modified LDL via macropinocytosis, becoming lipid-laden "foam cells" that are SMC rather than macrophage in origin — a paradigm shift from the classical macrophage-centric foam cell model.
4. **Calcification:** Synthetic SMCs may undergo osteoblastic transdifferentiation (Runx2/Osterix upregulation → matrix vesicle-mediated calcification), a major feature of medial arterial calcification (Mönckeberg sclerosis) in diabetes and CKD.
5. **Apoptosis:** Excessive ROS, inflammatory cytokines (TNF-α, IFN-γ), or lipid accumulation trigger SMC apoptosis in advanced plaques → thin fibrous cap → plaque vulnerability → acute coronary syndrome.

## Connections

- **Part-of cardiovascular system [^guyton-hall]:** Vascular SMCs in the tunica media of arteries regulate vascular tone and blood pressure via MLC₂₀ phosphorylation/MLCK; phenotype switching from contractile to synthetic drives atherosclerotic plaque formation and neointimal hyperplasia.
- **Modulates nitric oxide [^alberts-mol-cell-biology]:** eNOS-derived NO diffuses from endothelial cells to vascular SMCs, activating sGC → cGMP → PKG → MLCP activation → MLC₂₀ dephosphorylation → relaxation; NO is the primary endothelium-derived vasodilatory signal.
- **Modulated-by calcium-channel-blockers [^guyton-hall]:** Dihydropyridine CCBs (amlodipine, nifedipine) block L-type Cav1.2 on vascular SMCs → ↓Ca²⁺ entry → ↓MLCK activation → vasodilation → ↓TPR → ↓BP; vascular selectivity arises from tissue-specific splicing of Cav1.2.
- **Modulates respiratory system [^alberts-mol-cell-biology]:** Airway SMCs in tracheal and bronchial walls control airway calibre; β₂-AR agonists (salbutamol) → cAMP → PKA → ↓MLCK activity → relaxation → bronchodilation; muscarinic M₃ receptor activation → IP₃ → Ca²⁺ → contraction → bronchoconstriction in asthma.

## Pathology

**Atherosclerosis.** SMC phenotype switching is a necessary step in plaque formation. Contractile VSMCs respond to endothelial injury signals (ox-LDL, Ang II, PDGF-BB) by switching to synthetic phenotype, migrating to the intima, proliferating, and secreting collagen to form the fibrous cap. Paradoxically, SMC-derived foam cells (formerly thought to be exclusively macrophage) constitute ~50% of cells in advanced human coronary plaques. Cap thinning due to SMC apoptosis and MMP-mediated collagen degradation renders plaques vulnerable to rupture → acute MI.

**Pulmonary arterial hypertension (PAH).** Hyperproliferation and hypertrophy of pulmonary arteriole SMCs (driven by BMPR2 loss-of-function, serotonin, ET-1) → progressive obliteration of pulmonary arterioles → ↑pulmonary vascular resistance → right ventricular pressure overload → right heart failure. Treatment targets include endothelin receptor antagonists (bosentan, ambrisentan), PDE5 inhibitors (sildenafil, tadalafil — ↑cGMP → PKG → relaxation), and prostacyclin analogues (epoprostenol, iloprost).

**Vascular spasm.** ROCK hyperactivation in coronary artery SMCs → MLC₂₀ phosphorylation without ↑[Ca²⁺]i → coronary artery spasm → Prinzmetal (variant) angina. Treated with CCBs (diltiazem, verapamil) or nitrates (→ NO → cGMP). ROCK inhibitor fasudil is used in Japan and China for vasospasm.

**Bronchospasm / Asthma.** Allergen → IgE-FcεRI → mast cell degranulation → histamine, LTD₄, PGD₂ → airway SMC contraction → bronchoconstriction; chronic inflammation → airway SMC hypertrophy and hyperplasia → airway remodelling → fixed airflow limitation. Treatment: β₂-agonists (salbutamol, salmeterol) → cAMP → SMC relaxation; anticholinergics (ipratropium) → block M₃R; corticosteroids (beclomethasone) → ↓inflammatory mediators.

**Leiomyoma (uterine fibroid).** Benign SMC tumour of uterine myometrium; most common tumour in women of reproductive age (prevalence up to 70%). Driven by oestrogen and progesterone; MED12 exon 1/2 somatic mutations in ~70%. Symptoms: menorrhagia, pelvic pressure, infertility. Treatment: GnRH analogues (↓oestrogen → tumour regression), uterine artery embolisation, myomectomy/hysterectomy.

**Leiomyosarcoma.** Malignant SMC tumour; most common in uterus, retroperitoneum, GI tract. Aggressive; characterised by TP53, RB1, PTEN mutations and chromosomal instability. Treatment: resection + doxorubicin-based chemotherapy.

## See Also

- `../../07-system/cardiovascular-system/README.md` — systemic context for vascular SMC function
- `../../07-system/respiratory-system/README.md` — airway SMC and bronchospasm pathophysiology
- `../../03-molecular/nitric-oxide/README.md` — NO–sGC–cGMP–PKG relaxation pathway
- `../endothelial-cell/README.md` — endothelial-SMC crosstalk (eNOS, EDHF, ET-1, PGI₂)
- `../../../03-medicine/01-modern/04-cardio/calcium-channel-blockers/README.md` — pharmacological vascular SMC relaxation
