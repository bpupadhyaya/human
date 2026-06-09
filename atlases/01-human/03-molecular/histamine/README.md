---
schema: human-scale-entry/v1
id: histamine
name: Histamine
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-05
summary: "Biogenic amine (MW 111) derived from histidine by HDC. Stored in mast cells, basophils, ECL cells, and TMN neurons. Acts on H1–H4 GPCRs mediating allergy, gastric acid secretion, wakefulness, and neuroinflammation."
aliases: ["histamine", "2-(4-imidazolyl)ethylamine", "β-imidazolylethylamine"]
sources:
  - id: stryer-biochemistry
    type: textbook
    cite: "Berg JM, Tymoczko JL, Stryer L. Biochemistry. 9th ed. W.H. Freeman; 2019."
    url: "https://www.macmillanlearning.com/college/us/product/Biochemistry/p/131911467X"
    accessed: "2026-06-05"
  - id: janeway-immunobiology
    type: textbook
    cite: "Murphy K, Weaver C. Janeway's Immunobiology. 9th ed. Garland Science; 2017."
    url: "https://www.garlandscience.com/product/isbn/9780815345053"
    accessed: "2026-06-05"
cross_links:
  - target: 01-human/04-cellular/macrophage
    relation: modulates
    note: "H4R on macrophages mediates chemotaxis; H2R activation via cAMP suppresses TNF-α and IL-12 production. Histamine shapes macrophage polarisation, creating an anti-inflammatory paradox at sustained H2R stimulation."
  - target: 01-human/07-system/immune-system
    relation: modulates
    note: "Primary mediator of type I hypersensitivity. IgE-FcεRI crosslinking on mast cells triggers degranulation; H1/H2/H4 receptors coordinate vascular permeability, chemotaxis, smooth muscle tone, and lymphocyte trafficking."
  - target: 01-human/07-system/nervous-system
    relation: modulates
    note: "Tuberomammillary nucleus histaminergic neurons project to the entire cortex promoting wakefulness. H3 autoreceptors regulate release. Sedating antihistamines (diphenhydramine) cross BBB blocking H1 to cause drowsiness."
  - target: 01-human/04-cellular/dendritic-cell
    relation: modulates
    note: "H1/H2 on DCs modulate Th1/Th2 polarisation: H1 promotes IL-12 and Th1, H2 promotes Th2 tolerance. H4 drives DC chemotaxis; histamine promotes DC migration to lymph nodes during allergic responses."
  - target: 03-medicine/03-food/quercetin
    relation: modulated-by
    note: "Modulated by Quercetin."
  - target: 01-human/03-molecular/orexin
    relation: modulated-by
    note: "Orexin neurons in lateral hypothalamus excite TMN histamine neurons via OX2R → H1-mediated cortical wakefulness; orexin is upstream activator of histamine; reduced orexin in narcolepsy → impaired TMN drive → fragmented wakefulness; DORAs block orexin input to TMN indirectly."
  - target: 01-human/07-system/insomnia-disorder
    relation: connects-to
    note: "H1 receptors on cortical neurons maintain arousal via TMN projections; low-dose doxepin (3-6mg) is FDA-approved for sleep-maintenance insomnia via selective H1 blockade; OTC diphenhydramine blocks H1 but causes next-day grogginess and anticholinergic effects in elderly."
---

# Histamine

## Overview

Histamine is a **biogenic amine** (MW 111 Da, chemical formula C₅H₉N₃) derived from the amino acid L-histidine by a single decarboxylation step catalyzed by **histidine decarboxylase (HDC)**, a pyridoxal-5'-phosphate (PLP)-dependent enzyme [^stryer-biochemistry]. It is one of the earliest discovered chemical mediators, recognized in the early 20th century as the principal mediator of immediate hypersensitivity reactions and later understood as a far more pleiotropic signaling molecule spanning immunity, gastric physiology, CNS wakefulness, and neuroinflammation.

Histamine is stored preformed in secretory granules of **mast cells** (tissue-resident) and **basophils** (circulating), enterochromaffin-like (ECL) cells of the gastric oxyntic mucosa, and in neurons of the **tuberomammillary nucleus (TMN)** of the posterior hypothalamus. Its rapid release from mast cell granules — within seconds of receptor crosslinking — makes it the fastest-acting immune mediator. The diverse biology of histamine is largely determined by four GPCRs (H1R–H4R) with distinct G-protein coupling, tissue distribution, and functional consequences [^janeway-immunobiology].

## Structure

### Chemical structure

Histamine consists of an **imidazole ring** (4-membered ring with two nitrogens) attached via an ethylamine side chain. The two nitrogens of the imidazole (Nτ and Nπ) are critical for receptor binding:

| Property | Value |
|:---|:---|
| Molecular formula | C₅H₉N₃ |
| Molecular weight | 111.15 Da |
| Precursor | L-Histidine |
| Biosynthetic enzyme | Histidine decarboxylase (HDC, PLP-dependent) |
| pKa | ~5.9 (imidazole Nτ), ~9.4 (ammonium) |
| At physiological pH | Predominantly monocationic |

### Receptors

Histamine acts on four GPCRs with distinct coupling and distribution:

| Receptor | Coupling | Key locations | Primary functions |
|:---|:---|:---|:---|
| **H1R** | Gq → PLC → IP3/DAG → ↑Ca²⁺ | Smooth muscle, endothelium, CNS neurons, bronchi | Allergy (bronchoconstriction, vasodilatation, itch), wakefulness |
| **H2R** | Gs → adenylyl cyclase → ↑cAMP → PKA | Gastric parietal cells, cardiac myocytes, vascular SM | HCl secretion, positive chronotropy, gastric vasodilation |
| **H3R** | Gi (presynaptic autoreceptor) | CNS histaminergic neurons, enteric NS | ↓Histamine release; modulates DA, NE, ACh, 5-HT in CNS |
| **H4R** | Gi/Gq | Mast cells, eosinophils, DCs, bone marrow | Chemotaxis, pruritus, immune cell trafficking |

## Function

### Allergy and type I hypersensitivity

The dominant role of histamine in allergy is mast cell/basophil degranulation releasing preformed histamine into tissue and circulation [^janeway-immunobiology]:

1. **Sensitization**: Antigen exposure → IgE production (B cell + Th2) → IgE binds FcεRI on mast cells/basophils
2. **Re-exposure**: Antigen crosslinks FcεRI-bound IgE → Syk kinase activation → PLC → IP3 → Ca²⁺ surge → granule exocytosis (seconds)
3. **Histamine effects** via H1R:
   - **Venule endothelium**: gap junction opening → vascular permeability → wheal (local edema) and flare (erythema via axon reflex)
   - **Bronchial smooth muscle**: contraction → bronchoconstriction
   - **Itch**: activation of C-fiber nociceptors expressing TRPV1 and H1R
   - **Rhinorrhoea**: goblet cell mucus secretion, submucosal gland stimulation

### Gastric acid secretion (H2R)

ECL cells in the gastric oxyntic mucosa store and release histamine in response to:
- Gastrin (from G cells) via CCK2 receptor → ECL cell histamine release
- Vagal ACh stimulation

Histamine → **H2R on gastric parietal cells** → Gs → ↑cAMP → PKA phosphorylation → canalicular trafficking of H⁺/K⁺-ATPase → HCl secretion (intraluminal pH ≈ 1–2). H2R is the dominant paracrine amplifier of the gastrin-parietal cell axis; H2 blockers (famotidine, ranitidine) reduce basal and meal-stimulated acid by ~70%.

### CNS: wakefulness and cognition

TMN neurons (posterior hypothalamus) are the sole source of CNS histamine [^stryer-biochemistry]. They project diffusely to the **entire cortex, striatum, hippocampus**, and brainstem, with peak firing during wakefulness:

- H1R activation on cortical neurons → ↑arousal, attention, cognition
- H3R (presynaptic) autoreceptors → negative feedback on histamine release; also modulate release of DA, NE, ACh, 5-HT (H3 antagonists/inverse agonists investigated as cognition enhancers)
- Antihistamines crossing the BBB (diphenhydramine, promethazine — first generation) → H1 blockade → sedation; second-generation antihistamines (cetirizine, loratadine) are non-sedating due to poor BBB penetration
- Hypothalamic histamine also suppresses appetite via H1R on NPY/AgRP neurons

### Neurogenic inflammation and itch

Histamine stimulates unmyelinated C-fibers (expressing H1R and TRPV1) directly and also triggers axon reflexes causing local vasodilation (flare). In the spinal cord, histamine contributes to central sensitization of itch pathways (spinal interneurons expressing H1/H3R). H4R antagonists are under investigation for chronic itch (atopic dermatitis, uraemic pruritus) by targeting peripheral mast cell–nerve interactions [^janeway-immunobiology].

## Mechanism

### Biosynthesis and storage

```
L-Histidine ─(HDC, PLP)─► Histamine + CO₂
```

HDC is expressed constitutively in ECL cells and mast cells/basophils (upregulated by gastrin and cytokines). Histamine is stored in acidic secretory granules complexed with heparin and chondroitin sulfate proteoglycans (ionic interaction). Neuronal histamine is resynthesized rapidly (no re-uptake mechanism analogous to monoamines); metabolism occurs at the synapse and peripherally.

### Metabolism

Histamine is inactivated by two main routes:
1. **Methylation**: Histamine N-methyltransferase (HNMT, cytosolic) → N-methylhistamine → MAO-B → N-methylimidazole acetic acid (primary CNS route)
2. **Oxidation**: Diamine oxidase (DAO, extracellular, gut/placenta) → imidazole acetaldehyde → imidazole acetic acid (primary peripheral route)

### H1R signaling cascade

H1R (Gq) → Gαq activates **PLC-β** → PIP2 → IP3 (→ ER Ca²⁺ release) + DAG (→ PKC activation) → myosin light chain kinase (smooth muscle contraction) and NF-κB activation (pro-inflammatory gene transcription).

### H2R signaling cascade

H2R (Gs) → Gαs → **adenylyl cyclase** → ↑cAMP → **PKA** → phosphorylation of canalicular proteins → H⁺/K⁺-ATPase trafficking to apical membrane of parietal cell → HCl secretion. PKA also phosphorylates voltage-gated Ca²⁺ channels in the SA node → positive chronotropy.

### Release triggers beyond IgE

- **Complement anaphylatoxins**: C5a and C3a directly trigger mast cell degranulation via C5aR1/C3aR (Gi, Gq → Ca²⁺)
- **Substance P**: neuropeptide (neurogenic inflammation) → non-IgE mast cell degranulation
- **Physical stimuli**: cold, pressure, UV (dermographism, cold urticaria)
- **Opioids**: morphine/codeine → direct mast cell C48/80-like pathway (non-immunological)

## Connections

- `modulates` → **[macrophage](../../04-cellular/macrophage/README.md)** — H4R mediates macrophage chemotaxis; H2R/cAMP suppresses TNF-α and IL-12; histamine shapes M1/M2 polarisation balance [^janeway-immunobiology]
- `modulates` → **[immune-system](../../07-system/immune-system/README.md)** — primary mediator of type I hypersensitivity; IgE-FcεRI→degranulation; H1/H2/H4 coordinate vascular permeability, chemotaxis, smooth muscle tone, and lymphocyte trafficking [^janeway-immunobiology]
- `modulates` → **[nervous-system](../../07-system/nervous-system/README.md)** — TMN histaminergic projection to cortex promotes wakefulness; H3 autoreceptors regulate release; sedating first-generation antihistamines cross BBB and block H1 [^stryer-biochemistry]
- `modulates` → **[dendritic-cell](../../04-cellular/dendritic-cell/README.md)** — H1/H2 receptors on DCs modulate Th1/Th2 polarisation; H4 drives chemotaxis; histamine promotes DC migration to lymph nodes in allergic responses [^janeway-immunobiology]
- `modulated-by` → **[Orexin](../orexin/README.md)** — orexin neurons excite TMN histamine neurons via OX2R → H1-mediated cortical wakefulness; orexin is the primary upstream activator of histamine's wake-promoting function; DORAs (suvorexant, lemborexant) indirectly reduce TMN histamine drive.
- `connects-to` → **[Insomnia Disorder](../../07-system/insomnia-disorder/README.md)** — H1 receptors on cortical neurons maintain arousal via TMN projections; low-dose doxepin (3-6mg) is FDA-approved for sleep-maintenance insomnia via selective H1 blockade; OTC diphenhydramine blocks H1 but causes grogginess and anticholinergic effects in elderly.

## Pathology

| Condition | Mechanism | Clinically relevant |
|:---|:---|:---|
| **Anaphylaxis** | Systemic IgE-mediated mast cell/basophil degranulation → massive histamine release → vasodilation, bronchospasm, hypotension, urticaria | Epinephrine IM (first-line), IV fluids, H1+H2 antihistamines adjunct |
| **Allergic rhinitis** | Aeroallergen → IgE crosslinking → local mast cell histamine → H1R → sneezing, rhinorrhea, nasal congestion, itch | Intranasal corticosteroids (first-line), oral/intranasal H1 antihistamines, allergen immunotherapy |
| **Urticaria / Angioedema** | Mast cell histamine → H1R on dermal venules → wheal and flare; deeper angioedema involves bradykinin too | Second-gen antihistamines (bilastine, cetirizine); omalizumab for chronic spontaneous urticaria |
| **Asthma** | H1R-mediated bronchoconstriction (contributing factor, not dominant — cysteinyl leukotrienes and prostaglandins more important) | Antihistamines not first-line; ICS + bronchodilators preferred |
| **Peptic ulcer disease** | H2R-driven parietal cell HCl secretion contributes to mucosal injury (especially in H. pylori context) | H2 blockers (famotidine) or PPIs (omeprazole — more effective, block H⁺/K⁺-ATPase directly) |
| **Mastocytosis** | ↑Mast cell burden → ↑histamine → flushing, urticaria, peptic ulcers, diarrhea, anaphylaxis; serum tryptase elevated | Antihistamines; midostaurin (KIT inhibitor) for advanced SM |
| **Scombroid fish poisoning** | Bacterial HDC converts histidine in inadequately refrigerated fish → histamine-rich flesh → ingestion → pseudo-allergic reaction (flushing, headache, diarrhea) | Antihistamines; not true allergy; no IgE involved |
| **Systemic mast cell activation syndrome (MCAS)** | Recurrent multisystem symptoms (skin, GI, cardiovascular) consistent with mast cell mediator release; low-grade KIT variants | H1+H2 antihistamines, cromolyn sodium, omalizumab |

## See Also

- [Nitric oxide](../nitric-oxide/README.md) — vascular co-mediator; NO and histamine act in opposing/complementary ways on vascular tone
- [IL-6](../il-6/README.md) — inflammatory cytokine coordinating systemic response; mast cells produce IL-6 after degranulation
- [TNF-alpha](../tnf-alpha/README.md) — co-released with histamine in late-phase allergic responses; drives further mast cell priming
- [Immune system](../../07-system/immune-system/README.md) — overarching system context
- [Macrophage](../../04-cellular/macrophage/README.md) — downstream effector; H4R expressed on tissue macrophages

[^stryer-biochemistry]: Berg JM, Tymoczko JL, Stryer L. *Biochemistry.* 9th ed. W.H. Freeman; 2019. [Macmillan Learning](https://www.macmillanlearning.com/college/us/product/Biochemistry/p/131911467X)
[^janeway-immunobiology]: Murphy K, Weaver C. *Janeway's Immunobiology.* 9th ed. Garland Science; 2017. [Garland Science](https://www.garlandscience.com/product/isbn/9780815345053)
