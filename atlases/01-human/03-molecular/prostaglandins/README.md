---
schema: human-scale-entry/v1
id: prostaglandins
name: Prostaglandins (Eicosanoids)
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-05
summary: "C20 lipid mediators derived from arachidonic acid via COX-1/COX-2. PGE2 mediates fever, pain, and inflammation; PGI2 vasodilates and inhibits platelets; TXA2 promotes vasoconstriction and aggregation. NSAIDs and coxibs inhibit these pathways."
aliases: ["prostaglandins", "eicosanoids", "PGE2", "PGI2", "prostacyclin", "TXA2", "thromboxane", "PGD2", "PGF2alpha", "COX-1", "COX-2", "cyclooxygenase", "prostaglandin H synthase", "arachidonic acid", "PTGS1", "PTGS2"]
sources:
  - id: stryer-biochemistry
    type: textbook
    cite: "Berg JM, Tymoczko JL, Stryer L. Biochemistry. 9th ed. W.H. Freeman; 2019."
    url: "https://www.macmillanlearning.com/college/us/product/Biochemistry/p/131911467X"
    accessed: "2026-06-05"
  - id: guyton-hall
    type: textbook
    cite: "Hall JE, Hall ME. Guyton and Hall Textbook of Medical Physiology. 14th ed. Elsevier; 2021."
    url: "https://www.elsevier.com/books/guyton-and-hall-textbook-of-medical-physiology/hall/978-0-323-59712-8"
    accessed: "2026-06-05"
  - id: ricciotti-2011-prostaglandins-review
    type: peer-reviewed
    cite: "Ricciotti E, FitzGerald GA. Prostaglandins and inflammation. Arterioscler Thromb Vasc Biol. 2011;31(5):986-1000."
    doi: "10.1161/ATVBAHA.110.207449"
    pmid: "21508345"
    url: "https://doi.org/10.1161/ATVBAHA.110.207449"
    accessed: "2026-06-05"
  - id: funk-2001-prostaglandin-system
    type: peer-reviewed
    cite: "Funk CD. Prostaglandins and leukotrienes: advances in eicosanoid biology. Science. 2001;294(5548):1871-5."
    doi: "10.1126/science.294.5548.1871"
    pmid: "11729303"
    url: "https://doi.org/10.1126/science.294.5548.1871"
    accessed: "2026-06-05"
cross_links:
  - target: 01-human/07-system/immune-system
    relation: modulates
    note: "PGE2 (EP2/EP4) and PGD2 (DP1) modulate dendritic cell maturation, T-cell polarization (PGE2 suppresses Th1, promotes Th17/Treg), and mast cell degranulation. COX-2 prostanoids amplify acute inflammation; NSAIDs reduce fever (hypothalamic PGE2) and pain via PGE2 suppression."
  - target: 01-human/04-cellular/macrophage
    relation: expresses
    note: "Macrophages express COX-2 upon LPS/cytokine stimulation (NF-κB/AP-1) and are major sources of PGE2 and TXA2 in inflamed tissue. COX-2-derived PGE2 feeds back via EP2/EP4 to limit macrophage NLRP3 inflammasome activation; excessive macrophage PGE2 can suppress anti-tumor immunity."
  - target: 01-human/07-system/cardiovascular-system
    relation: modulates
    note: "TXA2 (platelet COX-1) promotes aggregation and vasoconstriction; PGI2 (endothelial COX-1/2) counters via vasodilation and platelet inhibition. Aspirin irreversibly acetylates COX-1 → ↓TXA2 > PGI2 (antithrombotic). Selective COX-2 inhibition ↓PGI2 → ↑CV risk."
  - target: 01-human/03-molecular/nf-kb
    relation: modulates
    note: "NF-κB drives COX-2 transcription upon inflammatory stimulation; COX-2-derived PGE2 reciprocally activates NF-κB via EP1/EP3 → PKC → IKK (amplification loop). PGE2 also activates CREB and β-catenin, contributing to immune evasion in COX-2-overexpressing tumors."
---

# Prostaglandins (Eicosanoids)

## Overview

**Prostaglandins** are a family of **C20 oxygenated lipid mediators** (eicosanoids — from Greek *eicosa* = twenty) derived from polyunsaturated fatty acids, predominantly **arachidonic acid (AA, 20:4 Δ5,8,11,14)**. They are not stored pre-formed but are **synthesized on demand** within seconds-to-minutes from membrane phospholipid-derived AA upon cell activation. They act primarily as local (autocrine/paracrine) mediators with half-lives of seconds-to-minutes.

The prostaglandin family belongs to the broader **eicosanoid superfamily**, which encompasses:
- **Prostanoids** (prostaglandins + thromboxanes + prostacyclin) — via cyclooxygenase (COX) pathway
- **Leukotrienes** — via 5-lipoxygenase (5-LOX) pathway (not covered in this entry)
- **Lipoxins, resolvins, protectins, maresins** — specialized pro-resolving mediators (SPMs) — anti-inflammatory/pro-resolving

**Historical landmarks:**
- 1930s: Ulf von Euler (later Nobel laureate) identified the contractile factor in human seminal fluid as "prostaglandin" (mistakenly believed to originate from the prostate gland)
- 1964-1971: Bergström, Samuelsson, and Vane (jointly awarded 1982 Nobel Prize in Physiology or Medicine) determined the chemical structures of PGE₁, PGF₂α, elucidated the COX pathway, and discovered that aspirin inhibits prostaglandin synthesis — one of the most impactful discoveries in pharmacology

**Physiological roles span virtually every organ system:** inflammation, fever, pain sensitization, hemostasis, vascular tone, renal blood flow regulation, gastric mucosal cytoprotection, uterine contraction, parturition, sleep, allergic responses, bone resorption, and cancer biology.

## Structure

### Arachidonic Acid: The Precursor

**Arachidonic acid (AA):** C20:4 Δ5,8,11,14 (all *cis* double bonds) — 20-carbon polyunsaturated fatty acid; a **ω-6** fatty acid. AA is the dominant eicosanoid precursor in most human tissues. (Other precursors: EPA/eicosapentaenoic acid [ω-3] → less inflammatory prostanoids and resolvins; DGLA/dihomo-γ-linolenic acid → 1-series prostanoids)

AA is stored esterified at the **sn-2 position of membrane phospholipids** (predominantly phosphatidylcholine and phosphatidylethanolamine), concentrated in the inner leaflet of the plasma membrane. Free AA must be released before it can be metabolized.

**Liberation of AA:**
- **cPLA₂ (cytosolic phospholipase A₂α, Group IVA):** The primary AA-releasing phospholipase; activated by intracellular Ca²⁺ (C2 domain) + ERK/MAPK phosphorylation → translocates to the nuclear and ER membranes → cleaves the *sn-2* acyl ester bond → releases free AA + lysophospholipid
- **Triggers:** cytokines (TNF-α, IL-1β), growth factors, receptor-linked Ca²⁺ signals (via PLC → IP₃ → Ca²⁺), phorbol esters, mechanical stress, LPS
- Secreted sPLA₂ (Group IIA, V) amplifies extracellular AA release in inflammation

### Prostaglandin H Synthase (PGHS/COX): Bifunctional Enzyme

The **cyclooxygenase enzyme** (PGHS) is a membrane-bound homodimer (each monomer: ~70 kDa) anchored to the ER and nuclear envelope via N-terminal signal peptide and monotopic membrane-binding domain. Each monomer contains two distinct active sites: [^ricciotti-2011-prostaglandins-review]

**1. Cyclooxygenase active site (COX activity):**
- Located in a hydrophobic channel in the enzyme core
- AA enters the channel and binds in a specific conformation
- **Tyr385** is the catalytic radical center — oxidized by the heme iron (peroxidase activity generates the Tyr385 radical to initiate cyclooxygenase catalysis)
- Incorporates **two molecules of O₂** into AA → forms the unstable endoperoxide **PGG₂** (prostaglandin G₂)
- **Arg120 and Ser530** are key residues: aspirin acetylates Ser530, blocking AA access to Tyr385 (irreversible COX-1/2 inhibition); ibuprofen reversibly occupies the channel; celecoxib fits the larger COX-2 channel (due to Val523 vs. Ile523 in COX-1 — the basis of COX-2 selectivity)

**2. Peroxidase active site:**
- Located near the heme group
- Reduces **PGG₂ → PGH₂** (prostaglandin H₂, the common intermediate) by removing the 15-hydroperoxy group
- Requires a co-reductant (e.g., glutathione)

**COX-1 vs. COX-2 (PTGS1 vs. PTGS2):**

| Feature | COX-1 | COX-2 |
|:---|:---|:---|
| Gene | PTGS1 (chromosome 9q32) | PTGS2 (chromosome 1q31) |
| Expression | Constitutive (most tissues, especially platelets, gastric mucosa, kidney) | Inducible by LPS, cytokines, growth factors, phorbol esters; constitutive in brain, kidney macula densa, reproductive tract |
| Active site volume | ~390 Å³ (smaller) | ~520 Å³ (larger — due to Ile523Val substitution) |
| Protein half-life | Stable (~12 hours in platelets; permanent since platelets lack nuclei) | ~2-4 hours (short — allows rapid on/off expression) |
| Primary roles | Hemostasis (TXA₂ in platelets), gastroprotection (PGE₂/PGI₂), renal autoregulation | Inflammation, fever, pain, ovulation, parturition, renal medulla |
| Inhibited by aspirin | Yes — irreversible; 100–325 mg/day for antiplatelet | Yes — at higher doses of aspirin |
| Inhibited by ibuprofen/naproxen | Yes — reversible, competitive | Yes — reversible, competitive |
| Inhibited by coxibs (celecoxib, etoricoxib) | No (selectivity ratio ~300:1) | Yes |

### Downstream Prostaglandin Synthases: Tissue-Specific Products

**PGH₂** is the common intermediate; terminal synthases convert it to the active prostanoid based on which enzyme is expressed in each cell type:

| Enzyme | Product | Receptors | Primary expressing cells |
|:---|:---|:---|:---|
| mPGES-1/2, cPGES | **PGE₂** | EP1, EP2, EP3, EP4 | Macrophages, mast cells, DRG neurons, endothelium, kidney |
| PGD₂ synthase (hematopoietic H-PGDS; lipocalin L-PGDS) | **PGD₂** | DP1, DP2/CRTH2 | Mast cells, Th2 cells, brain (L-PGDS), platelets |
| PGF₂α synthase (AKR1C3) | **PGF₂α** | FP | Uterus, ovary, lung, eye |
| PGIS (prostacyclin synthase, CYP8A1) | **PGI₂ (prostacyclin)** | IP, also PPARδ | Vascular endothelium, lung, kidney, heart |
| TXAS (thromboxane synthase, CYP5A1) | **TXA₂** | TP | Platelets (COX-1 + TXAS); macrophages (COX-2 + TXAS) |

## Function

### PGE₂: The Master Inflammatory Prostanoid

**PGE₂** is the most studied and most pathophysiologically important prostaglandin. Its diverse effects are mediated by four GPCRs with different coupling and expression patterns:

| Receptor | G protein | Effect |
|:---|:---|:---|
| EP1 | Gq → ↑IP₃/Ca²⁺ | Pain sensitization, bronchoconstriction, smooth muscle contraction |
| EP2 | Gs → ↑cAMP | Bronchodilation, vasodilation, ↓platelet aggregation, Th2 polarization |
| EP3 | Gi → ↓cAMP (dominant isoform) | Gastric mucus/bicarbonate secretion, ↓renin release, uterine contraction |
| EP4 | Gs → ↑cAMP | Vasodilation, ↑bone resorption, immune modulation, ↑PI3K-Akt (anti-apoptotic in cancer) |

**Key physiological and pathological roles of PGE₂:**
- **Fever (pyrexia):** IL-1β/IL-6/TNF-α → hypothalamic PGE₂ synthesis (COX-2 in perivascular microglia and endothelium of OVLT) → EP3 receptors on hypothalamic warm-sensitive neurons → ↑set-point temperature → fever; NSAIDs reduce fever by blocking hypothalamic COX-2-derived PGE₂
- **Pain sensitization:** PGE₂ (via EP1 and EP2 on DRG neurons and spinal cord) → ↑TRPV1 (capsaicin receptor) sensitivity, ↓TREK-1 K⁺ channel conductance → peripheral and central sensitization (hyperalgesia, allodynia)
- **Gastric cytoprotection:** Constitutive EP3/EP4-mediated mucus and HCO₃⁻ secretion from gastric surface epithelium and ↓gastric acid (↓H⁺/K⁺-ATPase activity) → protects gastric mucosa. This is why NSAIDs (blocking COX-1-derived PGE₂ in the stomach) cause gastric ulcers: loss of mucosal protection
- **Uterine contraction:** EP1/EP3 → smooth muscle contraction; PGE₂ is used pharmaceutically to ripen the cervix (cervical softening via EP2/EP4) and stimulate labor (dinoprostone = PGE₂ cervical gel)
- **Renal medullary blood flow:** PGE₂ (EP2/EP4) and PGI₂ maintain renal medullary blood flow during states of high RAAS/sympathetic tone; NSAIDs reduce renal PGE₂ → renal ischemia → acute kidney injury, especially in volume-depleted or heart failure patients

### PGI₂ (Prostacyclin): The Endothelial Guardian

Synthesized by vascular endothelium (primarily via COX-1 + PGIS) — the natural antagonist of TXA₂:

- **IP receptor (Gs → ↑cAMP):** Vasodilation (smooth muscle relaxation via ↓Ca²⁺/↑K⁺ channels), inhibition of platelet aggregation (↑cAMP → PKA → inhibits platelet shape change and TXA₂ synthesis), anti-proliferative effect on vascular smooth muscle
- Epoprostenol (IV PGI₂ analog) and iloprost (inhaled/oral analog) are used to treat pulmonary arterial hypertension (PAH)
- **The COX-2 selectivity paradox:** Vascular endothelium expresses COX-2 to generate PGI₂; platelets express only COX-1 to generate TXA₂. Selective COX-2 inhibitors (coxibs) → ↓endothelial PGI₂ → unopposed platelet TXA₂ → ↑thrombotic risk → ↑MI and stroke (demonstrated with rofecoxib in VIGOR trial → withdrew from market in 2004)

### TXA₂: The Platelet Activator

- Half-life ~30 seconds in aqueous solution (spontaneously hydrolyzes to inactive TXB₂)
- TP receptor (Gq + G12/13 → ↑IP₃/Ca²⁺ + RhoGEF) → platelet shape change, GPIIb/IIIa activation (fibrinogen binding), granule secretion (ADP, serotonin) — amplifies platelet aggregation; vasoconstriction (TP on vascular smooth muscle)
- **Aspirin's mechanism:** Low-dose aspirin (75-100 mg/day) irreversibly acetylates COX-1 Ser530 in circulating platelets (anucleate → cannot synthesize new COX-1 → permanently inhibited for the platelet's 7-10 day lifespan). Endothelial cells regenerate COX-2-derived PGI₂ within hours. Net effect: TXA₂ suppressed >> PGI₂ suppressed → antithrombotic. Demonstrated in ISIS-2 (n=17,187): aspirin reduced 5-week vascular mortality by 23% in acute MI

### PGD₂: Sleep and Allergy

- **L-PGDS (lipocalin-type PGD₂ synthase) in the brain:** Produces PGD₂ that accumulates in CSF during waking → acts on DP1 receptors in the basal forebrain/subarachnoid space → adenosine release → promotes non-REM sleep; the best-characterized endogenous sleep-promoting prostaglandin
- **H-PGDS in mast cells/Th2 cells:** PGD₂ → CRTH2 (DP2) on eosinophils, basophils, and Th2 cells → chemotaxis, cytokine release → allergy/asthma amplification. CRTH2 antagonists (fevipiprant) have been investigated for asthma

### PGF₂α: Luteolysis and Uterine Function

- **FP receptor (Gq → ↑IP₃/Ca²⁺):** Uterine smooth muscle contraction (luteolysis in non-pregnant females), raised intraocular pressure reduction (bimatoprost, latanoprost — prostaglandin F analogs — are the most effective topical ocular hypotensive drugs for glaucoma), bronchoconstriction
- Dinoprost (PGF₂α) is used to induce labor and for veterinary estrus synchronization

## Mechanism

### COX Catalytic Mechanism: Stepwise Oxygenation

1. **Initiation:** The PGHS peroxidase active site oxidizes a lipid hydroperoxide → generates Fe(IV)=O porphyrin π-cation radical → oxidizes **Tyr385** (in the COX active site) to a tyrosyl radical
2. **AA positioning:** AA enters the COX hydrophobic channel in an L-shaped conformation, with C-11 positioned adjacent to Tyr385
3. **H-abstraction from C-13:** Tyr385 radical abstracts a hydrogen atom from C-13 of AA → AA carbon radical at C-13 → bis-allylic system rearranges
4. **O₂ insertion at C-11:** First O₂ molecule adds at C-11 (from the same face as Tyr385) → peroxy radical at C-11
5. **Endoperoxide bridge formation:** The C-11 peroxy radical attacks C-9 (intramolecular cyclization) → forms the cyclopentane ring (the "prostane" ring) + radical at C-8
6. **O₂ insertion at C-15:** Second O₂ molecule adds at C-15 → hydroperoxide at C-15 + rearrangement → **PGG₂** (9,11-endoperoxide, 15-hydroperoxide)
7. **Peroxidase reduction:** The peroxidase active site reduces the C-15 hydroperoxide of PGG₂ → hydroxyl → **PGH₂**

**Net reaction:** AA + 2O₂ → PGH₂ (via PGG₂ intermediate)

### Receptor Signaling and Duration of Action

All prostanoid receptors (EP1-4, DP1-2, FP, IP, TP) are **GPCRs**. Upon prostanoid binding:
- Gs-coupled (EP2, EP4, IP, DP1): ↑cAMP → PKA → varied downstream effects (generally anti-inflammatory, vasodilatory, anti-platelet)
- Gi-coupled (EP3 primarily): ↓cAMP → reduced PKA activation (often pro-contractile, anti-secretory)
- Gq-coupled (EP1, FP, TP): ↑IP₃ → Ca²⁺ mobilization, ↑DAG → PKC (generally pro-contractile, pro-inflammatory, pro-aggregatory)

Prostanoids are rapidly inactivated (~30 seconds to ~5 minutes depending on compound):
- Spontaneous hydrolysis (TXA₂: t₁/₂ ~30 sec; PGI₂: t₁/₂ ~2 min at physiological pH)
- 15-hydroxy prostaglandin dehydrogenase (15-PGDH): oxidizes the C-15 hydroxyl → 15-ketoprostanoids (biologically inactive) — major inactivation pathway in lung
- β-oxidation (after ω-oxidation) in liver and kidney

## Connections

- **Modulates** → [Immune System](../../../../../01-human/07-system/immune-system/README.md): PGE₂ (EP2/EP4) and PGD₂ (DP1) modulate dendritic cell maturation, T-cell polarization (PGE₂ suppresses Th1/NK cell function, promotes Th17 and IL-10-producing regulatory T cells), and mast cell degranulation. Hypothalamic COX-2-derived PGE₂ mediates IL-1β/IL-6-driven fever. NSAIDs reduce fever, pain sensitization, and acute inflammation by blocking both COX isoforms. [^funk-2001-prostaglandin-system]

- **Expresses** → [Macrophage](../../../../../01-human/04-cellular/macrophage/README.md): Macrophages are the primary non-vascular, non-platelet cellular source of prostanoids. LPS/TNF-α/IL-1β stimulation → NF-κB/AP-1 → COX-2 induction → massive PGE₂ production → amplifies local inflammation. COX-2-derived PGE₂ creates a negative feedback via EP2/EP4 → ↑cAMP → ↓NLRP3 → limits inflammasome activation. Macrophage PGE₂ also suppresses NK cell and CD8+ T-cell anti-tumor activity in the tumor microenvironment. [^ricciotti-2011-prostaglandins-review]

- **Modulates** → [Cardiovascular System](../../../../../01-human/07-system/cardiovascular-system/README.md): The TXA₂/PGI₂ balance is the central prostanoid cardiovascular axis. Platelet COX-1-derived TXA₂ (TP → Gq → platelet activation, vasoconstriction) is opposed by endothelial COX-1/2-derived PGI₂ (IP → Gs → vasodilation, ↓platelet aggregation). Aspirin's antithrombotic mechanism exploits the differential regeneration kinetics between anucleate platelets and nucleated endothelium.

- **Modulates** → [NF-κB](../../../../../01-human/03-molecular/nf-kb/README.md): NF-κB (p65/p50) is the master transcriptional activator of COX-2 gene expression upon inflammatory stimulation. COX-2-derived PGE₂ reciprocally activates NF-κB via EP1/EP3 → Gq → PKC → IKK cascade, creating a feed-forward inflammatory amplification loop. This positive feedback loop — NF-κB → COX-2 → PGE₂ → NF-κB — is a major reason NSAIDs and COX-2 inhibitors have broad anti-inflammatory efficacy beyond simple eicosanoid suppression.

[^ricciotti-2011-prostaglandins-review]: Ricciotti E, FitzGerald GA. Arterioscler Thromb Vasc Biol. 2011;31(5):986-1000. doi:10.1161/ATVBAHA.110.207449
[^funk-2001-prostaglandin-system]: Funk CD. Science. 2001;294(5548):1871-5. doi:10.1126/science.294.5548.1871

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
