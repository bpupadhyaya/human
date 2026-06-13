---
schema: human-scale-entry/v1
id: myasthenia-gravis
name: Myasthenia Gravis
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-07
summary: "Myasthenia gravis (MG) is an autoimmune NMJ disease; AChR antibodies (85%) activate complement → AChR destruction → fatigable weakness; MuSK antibodies (6%) cause IgG4-mediated dysfunction. Pyridostigmine, steroids, thymectomy, eculizumab, and efgartigimod are treatments."
aliases: ["MG", "myasthenia gravis", "generalised myasthenia gravis", "gMG", "AChR antibody", "MuSK antibody", "seronegative MG", "myasthenic crisis", "ocular MG", "neuromuscular junction disease", "fatigable weakness", "ptosis", "diplopia"]
sources:
  - id: gilhus-2016-mg-review
    type: peer-reviewed
    cite: "Gilhus NE. Myasthenia Gravis. N Engl J Med. 2016;375(26):2570-2581."
    doi: "10.1056/NEJMra1602678"
    pmid: "28029925"
    url: "https://doi.org/10.1056/NEJMra1602678"
  - id: howard-2021-efgartigimod-adapt
    type: peer-reviewed
    cite: "Howard JF Jr, Bril V, Vu T, et al. Safety, efficacy, and tolerability of efgartigimod in patients with generalised myasthenia gravis (ADAPT). Lancet Neurol. 2021;20(7):526-536."
    doi: "10.1016/S1474-4422(21)00159-9"
    pmid: "34146511"
    url: "https://doi.org/10.1016/S1474-4422(21)00159-9"
  - id: howard-2017-eculizumab-regain
    type: peer-reviewed
    cite: "Howard JF Jr, Utsugisawa K, Benatar M, et al. Safety and efficacy of eculizumab in anti-acetylcholine receptor antibody-positive refractory generalised myasthenia gravis (REGAIN). Lancet Neurol. 2017;16(12):976-986."
    doi: "10.1016/S1474-4422(17)30369-1"
    pmid: "29066163"
    url: "https://doi.org/10.1016/S1474-4422(17)30369-1"
cross_links:
  - target: 01-human/03-molecular/acetylcholine
    relation: connects-to
    note: "Anti-AChR IgG1/IgG3 in MG activates classical complement → C3b opsonization + MAC-mediated AChR destruction at the NMJ; reduces AChR density → impaired NMJ transmission → fatigable weakness; pyridostigmine (AChE inhibitor) increases ACh dwell time at the NMJ."
  - target: 01-human/03-molecular/complement-c5
    relation: connects-to
    note: "Complement-mediated AChR destruction drives AChR+ MG; eculizumab (anti-C5; REGAIN trial) and zilucoplan (subcutaneous anti-C5 peptide; RAISE trial; FDA Oct 2023) block terminal complement → prevent MAC formation at NMJ → reduce AChR destruction and MG severity."
  - target: 01-human/03-molecular/fcrn
    relation: connects-to
    note: "Efgartigimod (Vyvgart; ADAPT trial: 68% vs. 30% minimal symptom expression at week 12) and rozanolixizumab (Rystiggo) target FcRn → block IgG recycling → accelerate anti-AChR IgG catabolism; efgartigimod FDA Dec 2021, rozanolixizumab FDA Jun 2023 for generalized AChR+ MG."
  - target: 01-human/06-organ/thymus
    relation: connects-to
    note: "Thymic hyperplasia (germinal centers with AChR-reactive Th cells) in ~70% of AChR+ MG; thymoma (10-15%) produces AChR-reactive T cells escaping tolerance; MGTX trial (NEJM 2016) showed thymectomy + prednisone reduces disability in non-thymomatous AChR+ gMG."
  - target: 01-human/04-cellular/b-cell
    relation: connects-to
    note: "B cells differentiate into plasma cells that secrete anti-AChR IgG1/IgG3; rituximab (anti-CD20) depletes B cells → durable remission especially in MuSK+ MG; plasmablast-derived anti-AChR IgG levels guide treatment decisions in AChR+ vs. MuSK+ subsets."
  - target: 01-human/03-molecular/snare-complex
    relation: connects-to
    note: "The SNARE complex (VAMP2/synaptobrevin + SNAP-25 + syntaxin-1) at the motor nerve terminal mediates ACh vesicle fusion; ACh release via SNARE is intact in MG (disease is postsynaptic); BoNT cleaves SNARE → NMJ blockade that mimics but differs mechanistically from MG."
  - target: 01-human/07-system/multiple-sclerosis
    relation: connects-to
    note: "Myasthenia gravis and multiple sclerosis are both autoimmune neurological diseases on opposite sides of the synapse and the immune system: MG is an antibody-and-complement attack on the neuromuscular junction (peripheral), while MS is T-cell demyelination of central myelin."
  - target: 01-human/03-molecular/immunoglobulin-g
    relation: connects-to
    note: "Antibody subclass dictates myasthenia gravis: AChR+ MG runs on complement-fixing IgG1/IgG3 (so eculizumab works), whereas MuSK+ MG is driven by non-complement IgG4 that blocks MuSK signaling; FcRn inhibitors like efgartigimod treat both by speeding IgG breakdown."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "Myasthenia gravis is a postsynaptic disease: the motor neuron terminal releases acetylcholine normally, but antibody-mediated loss of muscle AChRs blunts the endplate response — distinguishing it from Lambert-Eaton syndrome, where antibodies block presynaptic calcium channels."
  - target: 01-human/05-tissue/neuromuscular-junction
    relation: connects-to
    note: "Myasthenia gravis is the prototypical neuromuscular-junction disease: anti-AChR (or MuSK) autoantibodies plus complement destroy the folded postsynaptic endplate, so repeated firing fatigues transmission → fluctuating weakness; AChE inhibitors raise available ACh."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "Myasthenia gravis is a T-cell-dependent autoimmune disease: CD4+ T helper cells, often primed in a hyperplastic or thymomatous thymus, drive B cells to make high-affinity anti-AChR IgG; this T-cell help is why thymectomy and broad immunosuppression are therapeutic."
  - target: 01-human/07-system/cidp
    relation: connects-to
    note: "Myasthenia gravis and CIDP are both antibody/complement-mediated, treatable autoimmune neuromuscular disorders at different sites: MG hits the postsynaptic junction (fatigable weakness, normal reflexes), CIDP attacks nerve myelin (areflexia, sensory loss); both improve with IVIG."
  - target: 01-human/07-system/nmo
    relation: connects-to
    note: "Myasthenia gravis and neuromyelitis optica are antibody-mediated diseases that co-occur more than chance: both are driven by pathogenic IgG (anti-AChR vs anti-AQP4) and a tendency to further autoimmunity, and NMO can emerge after thymectomy for myasthenia."
  - target: 01-human/07-system/pemphigus-vulgaris
    relation: connects-to
    note: "Myasthenia gravis and pemphigus vulgaris are paradigm IgG autoantibody diseases against a cell-surface protein: anti-acetylcholine-receptor in MG versus anti-desmoglein in pemphigus, both can associate with thymoma, and both respond to plasma exchange, IVIG, and rituximab."
  - target: 01-human/04-cellular/plasma-cell
    relation: connects-to
    note: "Plasma cells sustain myasthenia gravis by making anti-acetylcholine-receptor antibodies: they secrete the IgG that blocks and destroys neuromuscular AChRs, and because they resist rituximab, plasma-cell-directed and FcRn-blocking therapies are used in refractory disease."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Macrophages execute the antibody attack in myasthenia gravis: anti-AChR IgG fixes complement and recruits macrophages that phagocytose the postsynaptic membrane, so innate effectors translate the autoantibody into loss of acetylcholine receptors at the neuromuscular junction."
  - target: 01-human/07-system/rheumatoid-arthritis
    relation: connects-to
    note: "Myasthenia gravis and rheumatoid arthritis are both antibody-mediated autoimmune diseases, but MG targets a single neuromuscular receptor while RA attacks the synovium broadly—yet both respond to B-cell depletion, reflecting shared autoreactive antibody-producing cells."
  - target: 01-human/06-organ/eye
    relation: connects-to
    note: "The eye is where myasthenia gravis usually begins: ptosis and diplopia from fatigable extraocular and eyelid muscles are the presenting sign in most patients, and ocular MG may stay confined to the eye or generalize—making the eye both first clue and prognostic marker."
  - target: 01-human/03-molecular/cd20
    relation: connects-to
    note: "B-cell-depleting therapy is increasingly used in myasthenia gravis: rituximab against CD20 is especially effective in MuSK-antibody MG, removing the B cells that mature into the plasma cells making pathogenic acetylcholine-receptor antibodies."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "Myasthenia gravis is a classic antibody-mediated autoimmune disease: autoantibodies against the acetylcholine receptor (or MuSK) and complement attack the neuromuscular junction, so it overlaps with other autoimmunity and responds to immunosuppression and thymectomy."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "Myasthenia gravis sits at the nervous system's output: it spares nerve and muscle themselves but attacks the neuromuscular junction where they meet, so signals fail to reach muscle—causing the fatigable weakness, ptosis and diplopia that define it."
---

# Myasthenia Gravis

## Overview

**Myasthenia gravis (MG)** is an autoimmune disease of the **neuromuscular junction (NMJ)** characterized by **fatigable muscle weakness** — weakness that worsens with repeated activity and improves with rest [^gilhus-2016-mg-review]. MG is the most common primary disorder of neuromuscular transmission and affects approximately 150-200 per 100,000 people globally (prevalence increasing with aging populations).

**The defining feature** is autoantibody-mediated impairment of acetylcholine receptor (AChR) function at the motor endplate, resulting in insufficient neuromuscular transmission. With each nerve impulse, acetylcholine (ACh) release is normal, but fewer AChRs are available to respond → reduced end-plate potential → failure to reach action potential threshold → impaired muscle contraction, especially with repetitive stimulation.

**Serological classification (critical for treatment decisions):**

| Antibody type | Prevalence | Target | Mechanism | Thymus |
|---|---|---|---|---|
| Anti-AChR (IgG1/IgG3) | ~85% | AChR α-subunit (main immunogenic region, MIR) | Complement activation → MAC → AChR destruction; receptor internalization; functional blockade | Thymic hyperplasia (70%); thymoma (10-15%) |
| Anti-MuSK (IgG4) | ~6% | Muscle-specific kinase (MuSK; agrin receptor) | IgG4 blocks MuSK-agrin signaling → AChR clustering failure; NO complement activation | Normal thymus usually |
| Anti-LRP4 (IgG1/2) | ~2-3% | LDL receptor-related protein 4 | Blocks LRP4-agrin-MuSK signaling → AChR clustering | Normal |
| Anti-agrin | ~2% | Agrin (muscle-specific) | Disrupts NMJ architecture | Normal |
| Seronegative | ~10% | Unknown (may have low-titer AChR or novel targets) | Unknown | Thymic hyperplasia may be present |

**Clinical subtypes:**
- **Ocular MG (OMG):** Restricted to levator palpebrae (ptosis) and extraocular muscles (diplopia); ~50% of patients at onset; 15% remain purely ocular after 2 years; high risk of progression to generalized
- **Generalized MG (gMG):** Limb, bulbar (dysphagia, dysarthria), axial, or respiratory muscle involvement; severity graded by MGFA classification (Class I ocular to Class V intubated)

## Structure

### NMJ anatomy and MG pathophysiology

**Normal NMJ:**
- Motor nerve terminal → releases ACh from synaptic vesicles (via SNARE complex: VAMP/synaptobrevin + SNAP-25 + syntaxin)
- ACh diffuses 50 nm across synaptic cleft → binds **AChR** (nicotinic α1β1γδ or α1β1εδ in adult) on muscle endplate → Na⁺ influx → depolarization → action potential → muscle contraction
- AChE (acetylcholinesterase) in basal lamina terminates ACh signal

**Pathogenesis in AChR+ MG:**

**Step 1 — Thymic sensitization:**
- Thymic myoid cells normally express AChR (function: clonal deletion of self-reactive T cells)
- In MG thymus (hyperplastic germinal centers): AChR-specific CD4+ T cells escaping deletion interact with thymic B cells → anti-AChR IgG production
- **Thymoma** (10-15% of MG): tumor produces AChR-reactive T cells that escape tolerance → systemic anti-AChR humoral immunity; thymoma patients often have more refractory disease

**Step 2 — Anti-AChR IgG effector mechanisms:**
1. **Complement-mediated destruction:** Anti-AChR IgG1/IgG3 → Fc-mediated C1q binding → classical complement cascade → C3b → C5 → MAC (C5b-9) → membrane attack on motor endplate → AChR degradation and structural endplate damage (simplified postsynaptic membrane)
2. **Receptor internalization (antigenic modulation):** Cross-linking of AChRs by bivalent IgG → accelerated receptor internalization and lysosomal degradation → loss of surface AChR
3. **Direct functional blockade:** Some anti-AChR antibodies bind at or near the ACh-binding site → competitive inhibition of ACh binding

**Step 3 — Impaired NMJ safety factor:**
- Normal NMJ: ACh release → EPP amplitude ~60-70 mV; action potential threshold ~-45 mV → large "safety factor"
- In MG: reduced AChR density → EPP amplitude reduced → may fall below action potential threshold with repetitive stimulation → fatigable weakness (classical electrophysiological correlate: ≥10% decrement on 3 Hz RNS)

**MuSK+ MG mechanism:**
- MuSK normally clusters AChRs at the endplate via the agrin-LRP4-MuSK signaling axis
- IgG4 anti-MuSK → blocks agrin binding to MuSK → disrupts AChR clustering → dispersed, fewer AChRs
- No complement activation (IgG4 does not activate C1q) → complement inhibitors (eculizumab) less effective
- Clinical phenotype: bulbar-predominant, facial/neck weakness, respiratory vulnerability; worse prognosis; not improved by thymectomy

## Function

### Diagnosis

**Antibody testing:**
- Anti-AChR (ELISA binding assay): sensitivity ~85% generalized, ~50-60% ocular MG
- Anti-MuSK (cell-based assay or ELISA): ordered if AChR-negative gMG
- Anti-LRP4, anti-agrin: specialized labs
- AChR blocking assay: ~20% additional positivity in AChR-binding–negative generalized MG

**Pharmacological testing:**
- **Edrophonium test (Tensilon test):** Ultra-short–acting reversible AChE inhibitor; transient dramatic improvement of ptosis/diplopia; sensitivity ~80-95% but false positives possible; rarely used now given ab testing

**Neurophysiology:**
- **Repetitive nerve stimulation (3 Hz RNS):** ≥10% decrement in compound muscle action potential amplitude is diagnostic; most sensitive in proximal/facial muscles
- **Single-fiber EMG (SFEMG):** Most sensitive test (~96-100%); measures jitter (variability of inter-potential interval); elevated jitter = impaired NMJ transmission; gold standard for seronegative MG

**Imaging:**
- **CT chest:** All MG patients screened for thymoma; MRI chest for equivocal CT
- **PET-CT:** Occasionally used for thymoma staging

**Clinical scores:**
- **QMG (Quantitative MG Score):** 13-item semi-quantitative scale; used as primary endpoint in MG trials; range 0-39
- **MGFA Classification (Class I-V):** Severity classification system
- **MG Activities of Daily Living (MG-ADL):** Patient-reported; 8 items; used in trials

## Pathology

### Therapies

**Symptomatic:**
- **Pyridostigmine (Mestinon):** Reversible AChE inhibitor (carbamate); increases ACh concentration at NMJ; 30-60 mg PO Q3-6H; rapid onset; does NOT modify disease course; avoidance in MuSK+ (may worsen bulbar symptoms)

**Immunosuppression (disease-modifying):**
- **Corticosteroids:** Prednisone 1 mg/kg/day; initial transient worsening in first 2-4 weeks (mechanism uncertain — may reduce ACh release); taper after remission; steroid-sparing agents needed for chronic therapy
- **Azathioprine (AZA):** 6-MP prodrug; purine synthesis inhibitor → lymphocyte suppression; steroid-sparing; onset 6-12 months (delayed efficacy); ~50% require combination; thiopurine methyltransferase (TPMT) genotyping before starting
- **Mycophenolate mofetil (MMF):** IMDPH inhibitor → lymphocyte suppression; onset 6-12 months; equivalent efficacy to AZA; preferred when TPMT-deficient
- **Rituximab (anti-CD20):** Effective particularly in **MuSK+ MG** (IgG4-mediated, B-cell dependent); 375 mg/m² × 4 weekly or 1g × 2; durable response in many patients; no RCT evidence in AChR+ MG but used

**Thymectomy:**
- **MGTX trial (Wolfe et al., NEJM 2016):** 126 patients, non-thymomatous AChR+ gMG age 18-65; thymectomy + prednisolone vs. prednisolone alone; 3-year minimal manifestation status: thymectomy 67% vs. 47%; lower steroid requirement; FDA guidance updated to recommend for non-thymomatous AChR+ MG
- **Thymoma:** All thymoma-associated MG requires thymectomy regardless of disease severity; thymoma resection does not reliably improve MG

**Acute/Crisis management:**
- **IVIG (2 g/kg over 2-5 days):** Rapid efficacy (days); non-specific immunomodulation; preferred in myasthenic crisis
- **Plasma exchange (PLEX):** Faster onset than IVIG; removes pathogenic anti-AChR IgG directly; 5-7 exchanges over 10-14 days; preferred if rapid intubation at risk
- **Myasthenic crisis triggers:** Infections (especially respiratory); surgery/anesthesia; aminoglycosides; fluoroquinolones; beta-blockers; magnesium; chloroquine/hydroxychloroquine; D-penicillamine

**Complement inhibitors:**
- **Eculizumab (Soliris; anti-C5 mAb; Alexion/AZ):** REGAIN trial (n=125; refractory AChR+ gMG): 26.3% vs. 13.5% QMG responders; Muppidi re-analysis: substantial functional improvement; FDA approved October 2017; IV Q2W; requires meningococcal vaccination [^howard-2017-eculizumab-regain]
- **Ravulizumab (Ultomiris; anti-C5; Alexion/AZ):** Extended half-life anti-C5 (Q8W IV); CHAMPION MG trial (n=175): 29.7% vs. 11.5% QMG response; FDA approved April 2022; superior convenience vs. eculizumab
- **Zilucoplan (Zilbrysq; anti-C5 peptidomimetic macrocycle; UCB):** Subcutaneous daily self-injection; RAISE trial (n=174): QMG -4.39 vs. -2.30 (p=0.0005); FDA approved October 2023; first SC complement inhibitor for MG

**FcRn inhibitors:**
- **Efgartigimod (Vyvgart; argenx):** Engineered Fc fragment competing with IgG for FcRn → ~75% IgG reduction → reduces anti-AChR titers; ADAPT trial (n=167, AChR+ subgroup): 68% vs. 30% minimal symptom expression (MG-ADL ≥4 improvement maintained); FDA approved December 2021 for AChR+ gMG; IV Q1W ×4 cycles [^howard-2021-efgartigimod-adapt]; SC formulation (Vyvgart Hytrulo) approved 2023
- **Rozanolixizumab (Rystiggo; UCB):** Humanized anti-FcRn mAb; ~70% IgG reduction; MG0002 Phase 3: primary endpoint met; FDA approved June 2023 for AChR+ or MuSK+ gMG

## Connections

- `connects-to` → **[Acetylcholine](../../03-molecular/acetylcholine/README.md)** — Anti-AChR IgG1/IgG3 in MG activates classical complement → C3b opsonization + MAC-mediated AChR destruction at the NMJ; reduces AChR density → impaired NMJ transmission → fatigable weakness; pyridostigmine (AChE inhibitor) increases ACh dwell time at the NMJ.
- `connects-to` → **[Complement C5](../../03-molecular/complement-c5/README.md)** — Complement-mediated AChR destruction drives AChR+ MG; eculizumab (anti-C5; REGAIN trial) and zilucoplan (subcutaneous anti-C5 peptide; RAISE trial; FDA Oct 2023) block terminal complement → prevent MAC formation at NMJ → reduce AChR destruction and MG severity.
- `connects-to` → **[FcRn](../../03-molecular/fcrn/README.md)** — Efgartigimod (Vyvgart; ADAPT trial: 68% vs. 30% minimal symptom expression at week 12) and rozanolixizumab (Rystiggo) target FcRn → block IgG recycling → accelerate anti-AChR IgG catabolism; efgartigimod FDA Dec 2021, rozanolixizumab FDA Jun 2023 for generalized AChR+ MG.
- `connects-to` → **[Thymus](../../06-organ/thymus/README.md)** — thymic hyperplasia (germinal centers with AChR-reactive Th cells) in ~70% of AChR+ MG; thymoma (10-15%) produces AChR-reactive T cells escaping tolerance; MGTX trial (NEJM 2016) showed thymectomy + prednisone reduces disability in non-thymomatous AChR+ gMG.
- `connects-to` → **[B Cell](../../04-cellular/b-cell/README.md)** — B cells differentiate into plasma cells that secrete anti-AChR IgG1/IgG3; rituximab (anti-CD20) depletes B cells → durable remission especially in MuSK+ MG; plasmablast-derived anti-AChR IgG levels guide treatment decisions in AChR+ vs. MuSK+ subsets.
- `connects-to` → **[SNARE Complex](../../03-molecular/snare-complex/README.md)** — the SNARE complex (VAMP2/synaptobrevin + SNAP-25 + syntaxin-1) at the motor nerve terminal mediates ACh vesicle fusion; ACh release via SNARE is intact in MG (disease is postsynaptic); BoNT cleaves SNARE → NMJ blockade that mimics but differs mechanistically from MG.
- `connects-to` → **[Multiple Sclerosis](../multiple-sclerosis/README.md)** — Myasthenia gravis and multiple sclerosis are both autoimmune neurological diseases on opposite sides of the synapse and the immune system: MG is an antibody-and-complement attack on the neuromuscular junction (peripheral), while MS is T-cell demyelination of central myelin.
- `connects-to` → **[Immunoglobulin G](../../03-molecular/immunoglobulin-g/README.md)** — Antibody subclass dictates myasthenia gravis: AChR+ MG runs on complement-fixing IgG1/IgG3 (so eculizumab works), whereas MuSK+ MG is driven by non-complement IgG4 that blocks MuSK signaling; FcRn inhibitors like efgartigimod treat both by speeding IgG breakdown.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — Myasthenia gravis is a postsynaptic disease: the motor neuron terminal releases acetylcholine normally, but antibody-mediated loss of muscle AChRs blunts the endplate response — distinguishing it from Lambert-Eaton syndrome, where antibodies block presynaptic calcium channels.
- `connects-to` → **[Neuromuscular Junction](../../05-tissue/neuromuscular-junction/README.md)** — Myasthenia gravis is the prototypical neuromuscular-junction disease: anti-AChR (or MuSK) autoantibodies plus complement destroy the folded postsynaptic endplate, so repeated firing fatigues transmission → fluctuating weakness; AChE inhibitors raise available ACh.
- `connects-to` → **[T Helper Cell](../../04-cellular/t-helper-cell/README.md)** — Myasthenia gravis is a T-cell-dependent autoimmune disease: CD4+ T helper cells, often primed in a hyperplastic or thymomatous thymus, drive B cells to make high-affinity anti-AChR IgG; this T-cell help is why thymectomy and broad immunosuppression are therapeutic.
- `connects-to` → **[CIDP](../cidp/README.md)** — Myasthenia gravis and CIDP are both antibody/complement-mediated, treatable autoimmune neuromuscular disorders at different sites: MG hits the postsynaptic junction (fatigable weakness, normal reflexes), CIDP attacks nerve myelin (areflexia, sensory loss); both improve with IVIG.
- `connects-to` → **[NMOSD](../nmo/README.md)** — Myasthenia gravis and neuromyelitis optica are antibody-mediated diseases that co-occur more than chance: both are driven by pathogenic IgG (anti-AChR vs anti-AQP4) and a tendency to further autoimmunity, and NMO can emerge after thymectomy for myasthenia.
- `connects-to` → **[Pemphigus Vulgaris](../pemphigus-vulgaris/README.md)** — Myasthenia gravis and pemphigus vulgaris are paradigm IgG autoantibody diseases against a cell-surface protein: anti-acetylcholine-receptor in MG versus anti-desmoglein in pemphigus, both can associate with thymoma, and both respond to plasma exchange, IVIG, and rituximab.
- `connects-to` → **[Plasma Cell](../../04-cellular/plasma-cell/README.md)** — Plasma cells sustain myasthenia gravis by making anti-acetylcholine-receptor antibodies: they secrete the IgG that blocks and destroys neuromuscular AChRs, and because they resist rituximab, plasma-cell-directed and FcRn-blocking therapies are used in refractory disease.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Macrophages execute the antibody attack in myasthenia gravis: anti-AChR IgG fixes complement and recruits macrophages that phagocytose the postsynaptic membrane, so innate effectors translate the autoantibody into loss of acetylcholine receptors at the neuromuscular junction.
- `connects-to` → **[Rheumatoid Arthritis](../rheumatoid-arthritis/README.md)** — Myasthenia gravis and rheumatoid arthritis are both antibody-mediated autoimmune diseases, but MG targets a single neuromuscular receptor while RA attacks the synovium broadly—yet both respond to B-cell depletion, reflecting shared autoreactive antibody-producing cells.
- `connects-to` → **[Eye](../../06-organ/eye/README.md)** — The eye is where myasthenia gravis usually begins: ptosis and diplopia from fatigable extraocular and eyelid muscles are the presenting sign in most patients, and ocular MG may stay confined to the eye or generalize—making the eye both first clue and prognostic marker.
- `connects-to` → **[CD20](../../03-molecular/cd20/README.md)** — B-cell-depleting therapy is increasingly used in myasthenia gravis: rituximab against CD20 is especially effective in MuSK-antibody MG, removing the B cells that mature into the plasma cells making pathogenic acetylcholine-receptor antibodies.
- `connects-to` → **[Immune System](../immune-system/README.md)** — Myasthenia gravis is a classic antibody-mediated autoimmune disease: autoantibodies against the acetylcholine receptor (or MuSK) and complement attack the neuromuscular junction, so it overlaps with other autoimmunity and responds to immunosuppression and thymectomy.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — Myasthenia gravis sits at the nervous system's output: it spares nerve and muscle themselves but attacks the neuromuscular junction where they meet, so signals fail to reach muscle—causing the fatigable weakness, ptosis and diplopia that define it.

[^gilhus-2016-mg-review]: Gilhus NE. Myasthenia Gravis. *N Engl J Med.* 2016;375(26):2570-2581. [doi:10.1056/NEJMra1602678](https://doi.org/10.1056/NEJMra1602678) · [PubMed 28029925](https://pubmed.ncbi.nlm.nih.gov/28029925/)
[^howard-2021-efgartigimod-adapt]: Howard JF Jr, Bril V, Vu T, et al. Safety, efficacy, and tolerability of efgartigimod in patients with generalised myasthenia gravis (ADAPT). *Lancet Neurol.* 2021;20(7):526-536. [doi:10.1016/S1474-4422(21)00159-9](https://doi.org/10.1016/S1474-4422(21)00159-9) · [PubMed 34146511](https://pubmed.ncbi.nlm.nih.gov/34146511/)
[^howard-2017-eculizumab-regain]: Howard JF Jr, Utsugisawa K, Benatar M, et al. Safety and efficacy of eculizumab in anti-acetylcholine receptor antibody-positive refractory generalised myasthenia gravis (REGAIN). *Lancet Neurol.* 2017;16(12):976-986. [doi:10.1016/S1474-4422(17)30369-1](https://doi.org/10.1016/S1474-4422(17)30369-1) · [PubMed 29066163](https://pubmed.ncbi.nlm.nih.gov/29066163/)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
