---
schema: medicine-entry/v1
id: aspirin
name: Aspirin
atlas: 03-medicine
scale: 01-modern
status: draft
last_reviewed: 2026-06-03
summary: "Aspirin (acetylsalicylic acid, ASA) — irreversible COX-1/COX-2 inhibitor. At 75–325 mg, irreversibly acetylates platelet COX-1, blocking TXA₂ for platelet lifetime (~10 days) → antiplatelet effect. Cornerstone of acute MI/stroke; secondary prevention reduces CV events ~25%."
aliases: ["aspirin", "acetylsalicylic acid", "ASA", "salicylate"]
sources:
  - id: vane-1971-cox-inhibition
    type: peer-reviewed
    cite: "Vane JR. Inhibition of prostaglandin synthesis as a mechanism of action for aspirin-like drugs. Nat New Biol. 1971;231(25):232-5."
    doi: "10.1038/newbio231232a0"
    pmid: "5284360"
    url: "https://doi.org/10.1038/newbio231232a0"
  - id: isis-2-1988
    type: peer-reviewed
    cite: "ISIS-2 (Second International Study of Infarct Survival) Collaborative Group. Randomised trial of intravenous streptokinase, oral aspirin, both, or neither among 17,187 cases of suspected acute myocardial infarction. Lancet. 1988;2(8607):349-60."
    doi: "10.1016/S0140-6736(88)92833-4"
    pmid: "2899772"
    url: "https://doi.org/10.1016/S0140-6736(88)92833-4"
  - id: atc-2002-meta
    type: peer-reviewed
    cite: "Antithrombotic Trialists' Collaboration. Collaborative meta-analysis of randomised trials of antiplatelet therapy for prevention of death, myocardial infarction, and stroke in high risk patients. BMJ. 2002;324(7329):71-86."
    doi: "10.1136/bmj.324.7329.71"
    pmid: "11786451"
    url: "https://doi.org/10.1136/bmj.324.7329.71"
  - id: mcneil-2018-aspirin-primary
    type: peer-reviewed
    cite: "McNeil JJ, Woods RL, Nelson MR, et al. Effect of aspirin on disability-free survival in the healthy elderly. N Engl J Med. 2018;379(16):1499-508."
    doi: "10.1056/NEJMoa1800722"
    pmid: "30133574"
    url: "https://doi.org/10.1056/NEJMoa1800722"
cross_links:
  - target: 01-human/07-system/cardiovascular-system
    relation: acts-on
    note: "Aspirin's antiplatelet effect reduces thrombotic events (MI, stroke, stent thrombosis) in the systemic and coronary circulations; its anti-inflammatory effect modulates atherosclerotic plaque."
---

# Aspirin

## Overview

Aspirin (acetylsalicylic acid, ASA) is one of the oldest and most prescribed drugs in the world, with a history spanning from willow bark preparations to the modern antiplatelet therapy that saves millions of lives annually. Chemically, it is the **acetyl ester of salicylic acid** — a simple modification that confers the ability to **irreversibly acetylate cyclooxygenase (COX) enzymes** [^vane-1971-cox-inhibition].

The pharmacological action of aspirin depends critically on dose:

- **Low dose (75–325 mg):** Irreversibly inactivates platelet COX-1 → blocks thromboxane A₂ (TXA₂) synthesis for the platelet's lifetime (~10 days) → **antiplatelet effect** without significantly affecting vascular prostacyclin (PGI₂) production in endothelium (which regenerates COX-2)
- **Intermediate dose (0.5–2 g):** Analgesic and antipyretic
- **High dose (2–6 g):** Anti-inflammatory (used historically in rheumatic fever)

The antiplatelet action of low-dose aspirin is the basis for its role in:
- **Acute coronary syndrome (ACS):** Loading dose 162–325 mg then 75–100 mg daily — cornerstone of STEMI/NSTEMI management [^isis-2-1988]
- **Secondary cardiovascular prevention** (post-MI, post-stroke, peripheral arterial disease, stable CAD): 75–100 mg daily; reduces MACE by ~25% [^atc-2002-meta]
- **Dual antiplatelet therapy (DAPT)** after coronary stenting: aspirin + P2Y₁₂ inhibitor (clopidogrel, ticagrelor, prasugrel)

## Mechanism

### Irreversible COX Inhibition

Cyclooxygenase (PGHS — prostaglandin H synthase) exists as two isoforms:

| Isoform | Expression | Products | Aspirin sensitivity |
|:---|:---|:---|:---|
| **COX-1** | Constitutive (platelets, gastric mucosa, kidney, endothelium) | TXA₂ (platelet aggregation, vasoconstriction); PGI₂ (antiplatelet, vasodilatory in endothelium); PGE₂ (gastroprotection) | Irreversibly inhibited; platelets cannot regenerate COX |
| **COX-2** | Inducible (inflammation, endothelium, kidney under certain conditions) | PGI₂ (endothelium); prostaglandins of inflammation | Irreversibly inhibited; cells that can synthesise COX-2 de novo recover faster |

The mechanism of aspirin's irreversible action:
1. Aspirin enters the COX active site channel
2. The acetyl group is covalently transferred to **Ser530** (COX-1) or **Ser516** (COX-2) — a serine residue in the channel
3. This bulky acetyl group blocks access of arachidonic acid to the catalytic Tyr385
4. The covalent acetylation is **permanent** — unlike NSAIDs, aspirin cannot be displaced by competitive inhibitors

**Why platelets are especially vulnerable:** Platelets are anucleate — they cannot synthesise new proteins. Once platelet COX-1 is acetylated, that platelet permanently lacks TXA₂ synthesis capacity for its ~10-day lifespan. New platelets (~10% replaced/day) gradually restore TXA₂ capacity over 5–10 days after stopping aspirin — hence the 5–7 day hold before surgery recommendation.

### Platelet Aggregation and TXA₂

Platelet COX-1 converts arachidonic acid → prostaglandin G₂ → prostaglandin H₂ → **TXA₂** (via thromboxane synthase). TXA₂:
- Acts via TP receptors on adjacent platelets → Gq signalling → ↑[Ca²⁺] → platelet activation/aggregation
- Causes vasoconstriction (TP receptors on smooth muscle)
- Amplifies platelet activation synergistically with ADP, thrombin, and collagen

By blocking TXA₂ synthesis irreversibly, aspirin prevents this amplification loop — reducing platelet aggregation at sites of vascular injury (e.g., ruptured atherosclerotic plaques).

### Anti-inflammatory Mechanism

At higher doses, aspirin inhibits COX-2 at sites of inflammation → ↓PGE₂, PGI₂, PGD₂ → ↓vasodilation, ↓oedema, ↓sensitisation of pain receptors → classic NSAID anti-inflammatory effect. Salicylate (hydrolysis product) also has aspirin-independent anti-inflammatory effects via NF-κB inhibition and upregulation of lipoxins.

## Clinical Use

### Acute MI (STEMI/NSTEMI)

- **ISIS-2 (1988):** Aspirin 162 mg/day for 1 month in 17,187 suspected MI patients → **23% reduction in 5-week vascular mortality** — equal in magnitude to streptokinase (thrombolysis), and additive when combined [^isis-2-1988]
- **Standard dosing:** 300–325 mg chewed immediately (loading dose for rapid absorption — chewing achieves peak plasma levels ~30 min vs. ~60 min swallowed)
- **Dual antiplatelet therapy:** Aspirin + ticagrelor (PLATO trial) or aspirin + prasugrel (TRITON-TIMI 38) superior to aspirin + clopidogrel in ACS; standard for 12 months post-ACS/stenting

### Secondary Prevention

- **Antithrombotic Trialists' Collaboration (2002):** Meta-analysis of 287 trials, 135,000 patients with prior MI, stroke, or high cardiovascular risk → **22% proportional reduction in serious vascular events** with antiplatelet therapy; absolute benefit ~1–2% per year → number needed to treat ~40–50/year to prevent 1 event [^atc-2002-meta]

### Primary Prevention — Changed Landscape

- **ARRIVE, ASCEND, ASPREE (2018):** Three large RCTs in primary prevention (patients without established ASCVD) showed NO significant reduction in MACE and INCREASED risk of major bleeding (GI, intracranial) with aspirin
- **Current guidelines (ACC/AHA 2019):** Aspirin **not routinely recommended for primary prevention** in most adults; may be considered in selected individuals aged 40–70 with high 10-year ASCVD risk AND low bleeding risk, after shared decision-making [^mcneil-2018-aspirin-primary]

## Evidence

### Key Trials

| Trial | Population | Aspirin regimen | Key result |
|:---|:---|:---|:---|
| **ISIS-2 (1988)** | 17,187 suspected AMI | 162 mg/d for 1 month | 23% reduction in 5-week vascular mortality [^isis-2-1988] |
| **ATC meta-analysis (2002)** | 135,000 high-risk patients | Various | 22% reduction in serious vascular events in secondary prevention [^atc-2002-meta] |
| **ASPREE (2018)** | 19,114 healthy elderly ≥70 | 100 mg/d | No reduction in disability-free survival; increased major bleeding [^mcneil-2018-aspirin-primary] |

## Connections

- **Acts on** → [Cardiovascular system](../../../../01-human/07-system/cardiovascular-system/README.md): By inhibiting platelet TXA₂ synthesis, aspirin reduces arterial thrombosis risk at the system level — preventing coronary and cerebrovascular thrombo-occlusive events.

[^vane-1971-cox-inhibition]: Vane JR. Inhibition of prostaglandin synthesis as a mechanism of action for aspirin-like drugs. *Nat New Biol.* 1971;231(25):232-5. [doi:10.1038/newbio231232a0](https://doi.org/10.1038/newbio231232a0) · [PubMed 5284360](https://pubmed.ncbi.nlm.nih.gov/5284360/)
[^isis-2-1988]: ISIS-2 Collaborative Group. Randomised trial of intravenous streptokinase, oral aspirin, both, or neither among 17,187 cases of suspected acute myocardial infarction. *Lancet.* 1988;2(8607):349-60. [doi:10.1016/S0140-6736(88)92833-4](https://doi.org/10.1016/S0140-6736(88)92833-4) · [PubMed 2899772](https://pubmed.ncbi.nlm.nih.gov/2899772/)
[^atc-2002-meta]: Antithrombotic Trialists' Collaboration. Collaborative meta-analysis of randomised trials of antiplatelet therapy. *BMJ.* 2002;324(7329):71-86. [doi:10.1136/bmj.324.7329.71](https://doi.org/10.1136/bmj.324.7329.71) · [PubMed 11786451](https://pubmed.ncbi.nlm.nih.gov/11786451/)
[^mcneil-2018-aspirin-primary]: McNeil JJ, Woods RL, Nelson MR, et al. Effect of aspirin on disability-free survival in the healthy elderly (ASPREE). *N Engl J Med.* 2018;379(16):1499-508. [doi:10.1056/NEJMoa1800722](https://doi.org/10.1056/NEJMoa1800722) · [PubMed 30133574](https://pubmed.ncbi.nlm.nih.gov/30133574/)
