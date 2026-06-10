---
schema: human-scale-entry/v1
id: cardiomyocyte
name: Cardiomyocyte
atlas: 01-human
scale: 04-cellular
status: draft
last_reviewed: 2026-06-03
summary: "The contractile cell of the heart — a branched, striated, electrically coupled muscle cell that converts every depolarization wave into a coordinated mechanical contraction via excitation–contraction coupling."
aliases: ["cardiac muscle cell", "cardiac myocyte"]
sources:
  - id: openstax-anatomy-19-2
    type: textbook
    cite: "OpenStax. Anatomy & Physiology 2e, Ch. 19.2: Cardiac Muscle and Electrical Activity."
    url: "https://openstax.org/books/anatomy-and-physiology-2e/pages/19-2-cardiac-muscle-and-electrical-activity"
    accessed: "2026-06-03"
  - id: bers-2002-cardiac-ec-coupling
    type: peer-reviewed
    cite: "Bers DM. Cardiac excitation-contraction coupling. Nature. 2002;415(6868):198-205."
    doi: "10.1038/415198a"
    pmid: "11805843"
  - id: bergmann-2009-cardiomyocyte-renewal
    type: peer-reviewed
    cite: "Bergmann O, Bhardwaj RD, Bernard S, et al. Evidence for cardiomyocyte renewal in humans. Science. 2009;324(5923):98-102."
    doi: "10.1126/science.1164680"
    pmid: "19342590"
  - id: cell-ontology-cardiomyocyte
    type: database
    cite: "Cell Ontology — cardiac muscle cell (CL:0000746)."
    url: "https://www.ebi.ac.uk/ols4/ontologies/cl/classes/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FCL_0000746"
    accessed: "2026-06-03"
cross_links:
  - target: 01-human/05-tissue/myocardium
    relation: part-of
    note: "Cardiomyocytes constitute the contractile cell population of the myocardium."
  - target: 01-human/03-molecular/troponin-complex
    relation: expresses
    note: "Cardiac isoforms TnC (TNNC1), TnI (TNNI3), TnT (TNNT2) on the thin filament."
  - target: 01-human/03-molecular/beta1-adrenergic-receptor
    relation: expresses
    note: "Primary β-adrenergic receptor on working cardiomyocytes; relays sympathetic input to contractility and heart rate."
  - target: 01-human/02-atomic/calcium
    relation: modulated-by
    note: "The cytosolic Ca²⁺ transient (100 nM → ~1 µM during systole) is the direct trigger of EC coupling in every cardiomyocyte."
  - target: 02-pathogen/01-viruses/coxsackievirus-b
    relation: infected-by
    note: "CVB serotypes 1–6 enter cardiomyocytes via the CAR receptor; cytolytic replication and protease-mediated dystrophin cleavage cause acute viral myocarditis."
  - target: 02-pathogen/01-viruses/sars-cov-2
    relation: infected-by
    note: "SARS-CoV-2 enters ACE2-expressing cardiomyocytes; direct infection and immune-mediated injury contribute to COVID-19-associated myocarditis."
  - target: 01-human/03-molecular/ryr2
    relation: expresses
    note: "Cardiomyocytes express RyR2 as the primary SR Ca²⁺ release channel, positioned at junctional SR facing Cav1.2 in T-tubule dyads."
  - target: 01-human/03-molecular/serca2a
    relation: expresses
    note: "SERCA2a is the dominant Ca²⁺ reuptake pump of the cardiac SR, expressed in the longitudinal SR of ventricular and atrial cardiomyocytes."
  - target: 01-human/03-molecular/connexin43
    relation: expresses
    note: "Connexin-43 (Cx43/GJA1) is the primary gap junction protein at the intercalated discs of working ventricular cardiomyocytes, enabling electrical coupling."
  - target: 01-human/03-molecular/ncx1
    relation: expresses
    note: "NCX1 (SLC8A1) is expressed in the sarcolemma and T-tubule membrane of cardiomyocytes; it extrudes ~28% of Ca²⁺ per beat and shapes the action potential."
  - target: 01-human/02-atomic/oxygen
    relation: modulated-by
    note: "Cardiomyocytes are obligate aerobic cells; oxygen delivery (via haemoglobin and the coronary circulation) directly sets mitochondrial ETC flux and ATP production, governing contractile capacity."
  - target: 01-human/03-molecular/atp
    relation: expresses
    note: "Cardiomyocytes sustain the highest ATP turnover of any mammalian cell — ~2×10⁻¹² mol ATP per beat, ~40 kg recycled per day across the adult heart; F₀F₁-ATP synthase drives continuous mitochondrial synthesis essential for contractile and ion-transport work."
  - target: 01-human/02-atomic/sodium
    relation: modulated-by
    evidence: bers-2002-cardiac-ec-coupling
    note: "Nav1.5 INa drives Phase 0; Na⁺/K⁺-ATPase gradient powers NCX1 Ca²⁺ extrusion; Na⁺ overload in ischaemia reverses NCX1 causing Ca²⁺ overload."
  - target: 01-human/04-cellular/erythrocyte
    relation: modulated-by
    evidence: bers-2002-cardiac-ec-coupling
    note: "Erythrocytes deliver O₂ to cardiomyocytes; reduced O₂ delivery triggers ischaemic signalling and metabolic shift to anaerobic glycolysis."
  - target: 01-human/03-molecular/cholesterol
    relation: modulated-by
    note: "Modulated by Cholesterol."
  - target: 01-human/02-atomic/magnesium
    relation: modulated-by
    note: "Modulated by Magnesium."
  - target: 02-pathogen/04-parasites/trypanosoma-cruzi
    relation: damaged-by
    note: "Damaged by Trypanosoma cruzi."
  - target: 01-human/02-atomic/potassium
    relation: connects-to
    note: "IKr (hERG), IKs (KCNQ1), IK1 (Kir2.1), and Ito (Kv4.3) K⁺ currents repolarise the cardiomyocyte AP; hypokalaemia shifts EK negative → prolongs AP → EADs → torsades de pointes; IKATP (Kir6.2/SUR2A) opens during ischaemia as an AP-shortening protective mechanism."
  - target: 01-human/02-atomic/selenium
    relation: connects-to
    note: "Keshan disease (Se-deficient China) is dilated cardiomyopathy caused by GPx4/TrxR2 deficiency, with Coxsackievirus B as co-factor; GPx4 prevents ferroptosis by reducing lipid hydroperoxides; TrxR2 (selenoprotein, mitochondrial) maintains cardiomyocyte redox homeostasis."
  - target: 01-human/05-tissue/cardiac-conduction-system
    relation: connects-to
    note: "Purkinje fibers are specialized cardiomyocytes expressing connexin-40/45 and HCN4 automaticity channel; action potentials are passed to working cardiomyocytes via connexin-43 gap junctions at the Purkinje–myocardial junction; LBBB delays this coupling → ventricular dyssynchrony."
taxonomy:
  cell_ontology: "CL:0000746"
  lineage: "mesoderm — lateral plate (cardiogenic mesoderm)"
---

# Cardiomyocyte

## Overview

The cardiomyocyte is the contractile cell of the heart — a striated muscle cell, branched and joined to its neighbors at intercalated discs, whose sole job is to convert each electrical depolarization into a coordinated mechanical contraction [^openstax-anatomy-19-2]. It is the unit on which heart function is built: every heartbeat is the synchronous shortening of roughly two to three billion of these cells in the adult ventricles, executed within a few hundred milliseconds of the SA node firing.

Three properties make the cardiomyocyte distinct from other muscle cells:

1. **Electrical excitability** — like neurons and skeletal muscle, but with a uniquely long action potential (~200–400 ms in ventricular cells), shaped to allow time for full mechanical contraction before re-excitation is possible.
2. **Coupled excitation–contraction via SR-mediated calcium-induced calcium release** — the same logic as skeletal muscle, but modulated by external Ca²⁺ entry through L-type channels rather than direct DHPR–RyR mechanical coupling [^bers-2002-cardiac-ec-coupling].
3. **Functional syncytium** — gap junctions at the intercalated discs (predominantly connexin-43) electrically link every cell to its neighbors, so a wavefront started by the SA node spreads cell-to-cell across the whole myocardium without any synapse.

## Structure

### Morphology

| Feature | Typical value |
|:---|:---|
| Diameter | 10–20 µm |
| Length | 50–100 µm |
| Shape | Branched, end-to-end joined |
| Nuclei | Often binucleated (~25–50 % in adult human ventricle); polyploidy common |
| Volume | ~15–40 pL |
| Mitochondrial fraction | 30–40 % of cell volume — among the highest of any human cell |

### Subcellular architecture

- **Sarcomeres** are the contractile units, repeating along the cell with ~2 µm spacing at rest. Each sarcomere is bounded by **Z-discs** (anchor for thin filaments and titin's anchoring end), traversed by interdigitating thin (actin) and thick (myosin) filaments, and centered on the **M-line**. The regulatory **[troponin complex](../../03-molecular/troponin-complex/README.md)** sits on the thin filament every seven actins.
- **Sarcolemma** — the plasma membrane — is continuous with the **T-tubule system**, deep invaginations that penetrate to the level of every Z-disc. T-tubules carry the action potential into the cell interior so that depolarization reaches the sarcoplasmic reticulum simultaneously throughout the cell.
- **Sarcoplasmic reticulum (SR)** is the cardiomyocyte's intracellular Ca²⁺ store. The **junctional SR** apposes T-tubules to form **dyads** — the locale of excitation–contraction coupling. RyR2 (ryanodine receptor type 2) clusters face inward toward L-type Ca²⁺ channels (Cav1.2) on the T-tubule. **Longitudinal SR** carries SERCA2a, which pumps Ca²⁺ back in for relaxation.
- **Intercalated discs** — at each end. Three structural elements: **fascia adherens** (anchors thin filaments cell-to-cell), **desmosomes** (anchor intermediate filaments), and **gap junctions** (connexin-43 hemichannels, transmitting depolarization).
- **Mitochondria** — densely packed between myofibrils, providing the ATP needed to sustain continuous contraction. Cardiomyocytes are intolerant of oxidative phosphorylation interruption: ATP depletion disrupts both contraction and ion-pump function within minutes.

### Key molecules expressed

| Category | Examples |
|:---|:---|
| Contractile proteins | Cardiac myosin heavy chain (`MYH7`, β-MHC; `MYH6`, α-MHC), cardiac actin (`ACTC1`), titin (`TTN`), tropomyosin (`TPM1`), **troponin complex** (`TNNT2`, `TNNI3`, `TNNC1`) |
| Voltage-gated ion channels | **Nav1.5** (`SCN5A`, fast Na⁺ — phase 0); **Cav1.2** (`CACNA1C`, L-type Ca²⁺ — phase 2); Kv4.3 (Ito, phase 1); hERG/Kv11.1 (`KCNH2`, IKr, phase 3); KvLQT1 (`KCNQ1`, IKs, phase 3); Kir2.1 (`KCNJ2`, IK1, phase 4) |
| Pacemaker channels | **HCN4** (`HCN4`, "funny current" If) — high in SA-nodal cells, low in working cardiomyocytes |
| Calcium handling | RyR2 (`RYR2`), SERCA2a (`ATP2A2`), phospholamban (`PLN`), calsequestrin-2 (`CASQ2`), NCX1 (`SLC8A1`) |
| Receptors | **β1-adrenergic** (`ADRB1`, see [β1-adrenergic receptor](../../03-molecular/beta1-adrenergic-receptor/README.md)), β2-adrenergic, M2 muscarinic, AT1 angiotensin, endothelin, opioid |
| Junctional proteins | Connexin-43 (`GJA1`), N-cadherin, plakoglobin, desmoplakin |

### Specialized variants

The cardiomyocyte is not one cell type but a family:

- **Working (contractile) cardiomyocytes** — atrial and ventricular. The bulk of the myocardium. Atrial cells are smaller, with shorter action potentials and a different repolarization profile.
- **Pacemaker cells** — SA and AV node. No stable resting potential; spontaneous diastolic depolarization driven by HCN4 and L-type/T-type Ca²⁺ currents. Set the heart rate.
- **Conduction-system cells** — bundle of His, bundle branches, **Purkinje fibers**. Fast-conducting (~2–4 m/s vs. ~0.3–1 m/s in working myocardium); long; strategically routed to ensure rapid, orderly ventricular depolarization.

## Function

### The action potential

A working ventricular cardiomyocyte at rest sits at about **−85 mV**. When depolarization arrives via gap junctions from a neighbor, the sequence is:

| Phase | What happens | Dominant currents |
|:---|:---|:---|
| **Phase 0** — upstroke (~1 ms) | Voltage-gated Nav1.5 channels open; rapid Na⁺ influx; membrane swings to ~+30 mV | INa |
| **Phase 1** — early repolarization | Nav1.5 inactivates; transient outward K⁺ current (Ito) brings membrane down briefly | Ito |
| **Phase 2** — plateau (~200 ms) | L-type Cav1.2 channels are open (ICaL inward) balanced by delayed-rectifier K⁺ outflow (IKs) → membrane near 0 mV; this is when calcium-induced calcium release happens | ICaL, IKs |
| **Phase 3** — repolarization | ICaL inactivates; IKr (hERG) and IKs together drive membrane back negative | IKr, IKs |
| **Phase 4** — resting | IK1 stabilizes the cell at ~−85 mV until the next wavefront arrives | IK1 |

The long plateau is what makes cardiac muscle different. It enforces a **refractory period** much longer than the contraction itself — preventing tetanus (sustained un-relaxing contraction) and giving the chamber time to fill.

### Excitation–contraction coupling

Once phase 2 brings calcium in through the L-type channels [^bers-2002-cardiac-ec-coupling]:

1. **Trigger:** Ca²⁺ entering through Cav1.2 in the T-tubule lifts local [Ca²⁺] in the dyadic cleft.
2. **Amplification:** RyR2 channels in the apposed junctional SR sense this rise and open, releasing a much larger pulse of Ca²⁺ from the SR — **calcium-induced calcium release (CICR)**.
3. **Activation:** the cytosolic Ca²⁺ transient (peaks at ~1 µM, up from ~100 nM at rest) saturates **troponin C** on the thin filament, displacing tropomyosin, exposing myosin-binding sites on actin.
4. **Force:** myosin cross-bridges cycle (ATP-dependent), pulling thin filaments inward; the sarcomere shortens by 10–20 %; the cell contracts.
5. **Relaxation:** Ca²⁺ is removed — primarily by **SERCA2a** back into the SR (~70 % of the flux in human myocyte) and **NCX1** out across the sarcolemma (~28 %), with smaller contributions from the sarcolemmal Ca²⁺-ATPase and mitochondrial uniporter.

### Modulation

The cardiomyocyte's contractile output and rhythm are tunable:

- **β-adrenergic stimulation** (via [β1-adrenergic receptor](../../03-molecular/beta1-adrenergic-receptor/README.md)): Gs → adenylyl cyclase → cAMP → PKA. PKA phosphorylates Cav1.2 (more Ca²⁺ in), phospholamban (relieves SERCA inhibition — faster Ca²⁺ uptake, faster relaxation), troponin I (reduces myofilament Ca²⁺ sensitivity, hastens relaxation), and RyR2. Net: faster, stronger, faster-relaxing beat.
- **Muscarinic (parasympathetic) stimulation** via M2 → Gi: reduces cAMP, opens GIRK K⁺ channels in nodal cells (slows pacemaker), counteracts β-adrenergic signaling.
- **Stretch** activates length-dependent calcium sensitivity (Frank–Starling at the cell scale) and stretch-activated channels.

## Lifecycle

### Origin

Cardiomyocytes arise during embryogenesis from **cardiogenic mesoderm** (lateral plate mesoderm), specified by signaling from BMPs, Wnts, and FGFs. Two progenitor populations contribute:

- **First heart field** — gives rise primarily to the left ventricle.
- **Second heart field** — contributes to the right ventricle, outflow tract, and parts of the atria.

Master transcription factors include **NKX2-5**, **GATA4**, **TBX5**, **MEF2C**, **HAND1/2** — mutations in any of these cause congenital heart disease.

### Postnatal growth

Mammalian cardiomyocytes lose proliferative capacity shortly after birth. Subsequent heart growth is achieved primarily by **hypertrophy** (increased cell size) rather than **hyperplasia** (increased cell number). Many human cardiomyocytes become **binucleated** or **polyploid** (4n, 8n DNA content) without completing cell division — a hallmark of terminal differentiation in this lineage.

### Adult turnover

Adult human cardiomyocytes turn over very slowly. The best evidence — from ¹⁴C bomb-pulse dating — places annual renewal at **~1 % per year in the young adult heart, declining to <0.5 % per year past age 50** [^bergmann-2009-cardiomyocyte-renewal]. This means the heart you have at 60 contains many cells you were born with.

### Death

After significant injury (most commonly **ischemic**, secondary to coronary occlusion), cardiomyocytes die by:

- **Necrosis** — energy failure, membrane disruption, release of intracellular contents (including troponin — the basis for the troponin assay used to diagnose acute MI).
- **Apoptosis** — programmed; observed at the infarct border zone and in heart failure.
- **Pyroptosis / necroptosis** — inflammasome-driven cell death; relevant in myocarditis and sterile inflammation post-MI.

Lost cardiomyocytes are **not replaced**. The void fills with collagenous scar produced by activated fibroblasts. This is why cardiac injury becomes chronic disease.

## Connections

- **Up (containing tissue):** the cardiomyocyte is `part-of` the **[myocardium](../../05-tissue/myocardium/README.md)**.
- **Down (expressed molecules):** the cardiomyocyte `expresses` the **[troponin complex](../../03-molecular/troponin-complex/README.md)**, the **[β1-adrenergic receptor](../../03-molecular/beta1-adrenergic-receptor/README.md)**, and many other ion channels, contractile proteins, and signaling molecules — entries to come.
- **Cross-atlas (planned in Phase 3):** the cardiomyocyte is the cellular target of **Coxsackievirus B** (cytolytic infection via the coxsackievirus and adenovirus receptor, CAR) and the cellular site at which β-blockers like **metoprolol** exert their effect (via β1-adrenergic blockade).
- `connects-to` → **[Potassium](../../02-atomic/potassium/README.md)** — IKr (hERG), IKs (KCNQ1), IK1 (Kir2.1), and Ito (Kv4.3) K⁺ currents repolarise the cardiomyocyte AP; hypokalaemia shifts EK negative → prolongs AP → EADs → torsades de pointes; IKATP (Kir6.2/SUR2A) opens during ischaemia as an AP-shortening protective mechanism.
- `connects-to` → **[Selenium](../../02-atomic/selenium/README.md)** — Keshan disease (dilated cardiomyopathy in Se-deficient China) involves GPx4 and TrxR2 deficiency in cardiomyocytes, with Coxsackievirus B as co-factor; GPx4 prevents ferroptosis by reducing lipid hydroperoxides; TrxR2 maintains mitochondrial redox homeostasis.
- `connects-to` → **[Cardiac Conduction System](../../05-tissue/cardiac-conduction-system/README.md)** — Purkinje fibers are specialized cardiomyocytes (connexin-40/45, HCN4); action potentials pass to working cardiomyocytes via connexin-43 gap junctions at the Purkinje–myocardial junction; LBBB causes dyssynchronous E-C coupling reducing ejection fraction.

## Pathology

Diseases at the cardiomyocyte scale:

- **Ischemic injury** — necrosis after sustained coronary occlusion; the irreversibility threshold is ~20–40 minutes of complete ischemia.
- **Hypertrophic cardiomyopathy (HCM)** — sarcomeric protein mutations (`MYH7`, `MYBPC3`, etc.) cause cellular disarray, asymmetric hypertrophy, and propensity to fatal arrhythmia.
- **Dilated cardiomyopathy (DCM)** — sarcomeric, cytoskeletal, or nuclear-envelope mutations (e.g., `TTN`, `LMNA`); cells weaken, chambers dilate, EF falls.
- **Long-QT syndromes** — ion-channel mutations (`KCNQ1`, `KCNH2`, `SCN5A`, others) prolong phase 3 repolarization, predisposing to polymorphic VT (torsades).
- **Catecholaminergic polymorphic VT (CPVT)** — RyR2 or calsequestrin mutations cause Ca²⁺ leak during diastole, triggering arrhythmia under adrenergic stress.
- **Viral cytolysis** — direct lysis by cardiotropic viruses (Coxsackievirus B, parvovirus B19, SARS-CoV-2 — variable contributions).

## Variation

- **Atrial vs. ventricular** cells differ in size, action-potential shape, and gene expression (atrial natriuretic peptide is atrial-specific in adults).
- **Pacemaker vs. working** cells differ profoundly — pacemaker cells lack stable Phase 4, have HCN-driven spontaneous depolarization, and rely on Ca²⁺-clock + membrane-clock coupling.
- **Polyploidy** — the proportion of binucleated and polyploid cardiomyocytes varies between individuals and increases with age.
- **Sex.** Some sex-specific differences in repolarization (women have longer QTc on average) and in calcium handling have been characterized.

## Open questions

- **Why does proliferation stop?** Adult cardiomyocyte cell-cycle exit is not fully understood — Hippo (YAP/TAZ), Erbb2, Meis1, and metabolic switches (fatty-acid oxidation, ROS) all play roles. Whether these can be safely re-engaged for regeneration is a major research goal.
- **Heterogeneity.** Single-cell sequencing reveals more cardiomyocyte subtypes than the classical atrial/ventricular/conduction trichotomy. Functional consequences are still being mapped.
- **Direct reprogramming.** Forced expression of GATA4/MEF2C/TBX5 (and refinements) can convert fibroblasts into cardiomyocyte-like cells in vitro and (less efficiently) in vivo — clinical translation is unsettled.

## See also

- [`myocardium`](../../05-tissue/myocardium/README.md) — the tissue this cell forms.
- [`troponin-complex`](../../03-molecular/troponin-complex/README.md) — calcium switch.
- [`beta1-adrenergic-receptor`](../../03-molecular/beta1-adrenergic-receptor/README.md) — β1AR signaling.
- [`heart`](../../06-organ/heart/README.md) — the organ.

[^openstax-anatomy-19-2]: OpenStax. *Anatomy & Physiology 2e*, Ch. 19.2: Cardiac Muscle and Electrical Activity. [Read online →](https://openstax.org/books/anatomy-and-physiology-2e/pages/19-2-cardiac-muscle-and-electrical-activity)
[^bers-2002-cardiac-ec-coupling]: Bers DM. Cardiac excitation-contraction coupling. *Nature.* 2002;415(6868):198-205. [doi:10.1038/415198a](https://doi.org/10.1038/415198a) · [PubMed 11805843](https://pubmed.ncbi.nlm.nih.gov/11805843/)
[^bergmann-2009-cardiomyocyte-renewal]: Bergmann O, Bhardwaj RD, Bernard S, et al. Evidence for cardiomyocyte renewal in humans. *Science.* 2009;324(5923):98-102. [doi:10.1126/science.1164680](https://doi.org/10.1126/science.1164680) · [PubMed 19342590](https://pubmed.ncbi.nlm.nih.gov/19342590/)
