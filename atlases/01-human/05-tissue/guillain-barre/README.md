---
schema: human-scale-entry/v1
id: guillain-barre
name: Guillain-Barré Syndrome
atlas: 01-human
scale: 05-tissue
status: draft
last_reviewed: 2026-06-06
summary: "Acute immune-mediated polyradiculoneuropathy; leading cause of acute flaccid paralysis globally. AIDP: T-cell/antibody attack on peripheral myelin. Axonal subtypes (AMAN): anti-ganglioside antibodies post-Campylobacter. Treatment: IVIg or plasmapheresis."
aliases: ["GBS", "Guillain-Barré syndrome", "AIDP", "AMAN", "acute inflammatory demyelinating polyneuropathy"]
sources:
  - id: willison-2016-gbs-lancet
    type: peer-reviewed
    cite: "Willison HJ, Jacobs BC, van Doorn PA. Guillain-Barré syndrome. Lancet. 2016;388(10045):717-727."
    doi: "10.1016/S0140-6736(16)00339-1"
    pmid: "26948435"
    url: "https://doi.org/10.1016/S0140-6736(16)00339-1"
  - id: vandoorn-2008-gbs-review
    type: peer-reviewed
    cite: "van Doorn PA, Ruts L, Jacobs BC. Clinical features, pathogenesis, and treatment of Guillain-Barré syndrome. Lancet Neurol. 2008;7(10):939-950."
    doi: "10.1016/S1474-4422(08)70215-1"
    pmid: "18848313"
    url: "https://doi.org/10.1016/S1474-4422(08)70215-1"
cross_links:
  - target: 01-human/04-cellular/macrophage
    relation: modulated-by
    note: "In AIDP, macrophages invade the peripheral nerve, strip myelin from axons, and contribute to demyelination; macrophage-mediated myelin phagocytosis is a key histopathological feature of GBS nerve biopsies."
  - target: 01-human/03-molecular/immunoglobulin-g
    relation: modulated-by
    note: "Anti-ganglioside IgG antibodies (anti-GM1, anti-GD1a in AMAN; anti-GQ1b in Miller Fisher syndrome) mediate axonal injury via complement activation and macrophage FcγR-mediated attack on nodes of Ranvier."
---

# Guillain-Barré Syndrome

## Overview

Guillain-Barré Syndrome (GBS) is the **leading cause of acute flaccid paralysis worldwide**, with a global annual incidence of ~1–2 per 100,000 population. It is an acute, usually monophasic, immune-mediated disorder of the peripheral nervous system (PNS), characterized by rapidly progressive limb weakness, areflexia, and in severe cases, respiratory failure requiring mechanical ventilation (~25% of patients) [^willison-2016-gbs-lancet].

GBS encompasses a spectrum of subtypes with distinct pathophysiology, nerve fiber targets, and geographic distributions:

| Subtype | Mechanism | Frequency |
|:---|:---|:---|
| **AIDP** (Acute Inflammatory Demyelinating Polyneuropathy) | T-cell + macrophage attack on peripheral myelin | ~85% Western countries |
| **AMAN** (Acute Motor Axonal Neuropathy) | Anti-ganglioside IgG (GM1/GD1a) → complement + macrophage attack on axolemma at nodes of Ranvier | Dominant in Asia, ~30-65% in China |
| **AMSAN** (Acute Motor and Sensory Axonal Neuropathy) | As AMAN but includes sensory axons | ~5% |
| **MFS** (Miller Fisher Syndrome) | Anti-GQ1b IgG; ophthalmoplegia + ataxia + areflexia | ~5% |

GBS typically follows a **preceding infection by 1–4 weeks**: Campylobacter jejuni (~30%), cytomegalovirus, EBV, SARS-CoV-2, influenza, and others. The molecular basis is **molecular mimicry** — bacterial or viral antigens share structural homology with peripheral nerve gangliosides, causing cross-reactive immune responses that target the PNS.

## Structure

### Peripheral Nerve Pathology by Subtype

**AIDP histopathology:**
- **Lymphocytic infiltration** of spinal roots and peripheral nerves (primarily T cells and macrophages)
- **Macrophage-mediated myelin stripping** — macrophages insert processes between axon and myelin sheath, phagocytosing intact myelin (primary demyelination)
- **Segmental demyelination** → slowed nerve conduction, conduction block
- **Complement deposition** on the outer myelin lamellae (C3d, C5b-9)
- Relative **axon sparing** (distinguishes AIDP from axonal variants)

**AMAN/AMSAN histopathology:**
- **Complement activation** at the nodes of Ranvier — anti-GM1/GD1a IgG binds gangliosides at nodal axolemma → C1q → MAC deposition → axolemmal disruption
- **Macrophage invasion** through the node into the periaxonal space (without entering the myelin sheath)
- **Reversible conduction failure** (early: Na⁺ channel disruption) → axonal degeneration (severe cases)
- Myelin sheath may be relatively preserved (pure motor in AMAN)

### Electrophysiological Correlates

| Finding | AIDP | AMAN |
|:---|:---|:---|
| Conduction velocity | Reduced (<75% normal) | Normal or slightly reduced |
| F-wave latency | Prolonged | Normal or prolonged |
| Distal CMAP amplitude | Usually preserved early | Reduced (axonal loss) |
| Conduction block | Present | Absent |
| Sensory NCS | Abnormal | Normal (AMAN) |

## Function

### Clinical Progression

GBS follows a characteristic temporal pattern [^vandoorn-2008-gbs-review]:

1. **Prodromal infection** (1–4 weeks prior) — triggering immune activation against PNS antigens via molecular mimicry
2. **Acute progressive phase** (days to 4 weeks) — ascending limb weakness (starts distally → proximal), areflexia, pain (often prominent and early), autonomic dysfunction (cardiac arrhythmias, BP lability, ileus, urinary retention)
3. **Plateau phase** (days to weeks) — maximum deficit; respiratory failure in ~25% requiring ICU admission; dysautonomia most dangerous
4. **Recovery phase** (weeks to months) — remyelination → restoration of conduction; axonal regeneration in axonal subtypes (slower, less complete)

**Nadir of illness:** Most patients reach maximum disability by 4 weeks (by definition — progression beyond 8 weeks = CIDP, chronic inflammatory demyelinating polyneuropathy, a different entity).

### Respiratory Involvement

Respiratory failure is the most life-threatening complication:
- Phrenic nerve and intercostal nerve demyelination → diaphragm and respiratory muscle weakness
- Bulbar dysfunction (CN IX/X) → aspiration risk
- Monitoring: **20/30/40 rule** for intubation threshold (FVC <20 mL/kg, MIP <30 cmH₂O, MEP <40 cmH₂O)

### Autonomic Dysfunction

Autonomic involvement occurs in ~70% of hospitalized GBS patients:
- Cardiac: bradycardia, tachycardia, heart block, asystole (cause of sudden death)
- Vascular: labile BP (hyper- and hypotension), orthostatic hypotension
- Gastrointestinal: ileus, urinary retention

## Connections

- `modulated-by` → **[Macrophage](../../04-cellular/macrophage/README.md)** — primary effector of myelin stripping in AIDP; invades peripheral nerve, strips and phagocytoses myelin via FcγR-mediated and complement-mediated mechanisms
- `modulated-by` → **[Immunoglobulin G](../../03-molecular/immunoglobulin-g/README.md)** — pathogenic anti-ganglioside IgG antibodies (anti-GM1, anti-GD1a, anti-GQ1b) mediate axonal subtypes and Miller Fisher syndrome; therapeutic IVIg neutralizes pathogenic antibodies and modulates Fc-receptor signaling

[^willison-2016-gbs-lancet]: Willison HJ, Jacobs BC, van Doorn PA. Guillain-Barré syndrome. *Lancet.* 2016;388(10045):717-727. [doi:10.1016/S0140-6736(16)00339-1](https://doi.org/10.1016/S0140-6736(16)00339-1) · [PubMed 26948435](https://pubmed.ncbi.nlm.nih.gov/26948435/)
[^vandoorn-2008-gbs-review]: van Doorn PA, Ruts L, Jacobs BC. Clinical features, pathogenesis, and treatment of Guillain-Barré syndrome. *Lancet Neurol.* 2008;7(10):939-950. [doi:10.1016/S1474-4422(08)70215-1](https://doi.org/10.1016/S1474-4422(08)70215-1) · [PubMed 18848313](https://pubmed.ncbi.nlm.nih.gov/18848313/)
