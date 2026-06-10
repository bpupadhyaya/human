---
schema: medicine-entry/v1
id: ibuprofen
name: Ibuprofen
atlas: 03-medicine
scale: 01-modern
status: draft
last_reviewed: 2026-06-06
summary: "Prototype non-selective NSAID; reversibly inhibits COX-1 and COX-2 → ↓ prostaglandin and thromboxane synthesis. Analgesic, antipyretic, anti-inflammatory. Most-consumed OTC analgesic globally. GI and cardiovascular risks limit chronic use. Advil, Nurofen."
aliases: ["ibuprofen", "Advil", "Nurofen", "Motrin", "Brufen", "(RS)-2-(4-(2-methylpropyl)phenyl)propanoic acid"]
sources:
  - id: adams-1969-ibuprofen
    type: peer-reviewed
    cite: "Adams SS, Bough RG, Cliffe EE, Lessel B, Mills RF. Absorption, distribution and toxicity of ibuprofen. Toxicol Appl Pharmacol. 1969;15(2):310-30."
    doi: "10.1016/0041-008X(69)90100-0"
    pmid: "5351312"
    url: "https://doi.org/10.1016/0041-008X(69)90100-0"
  - id: vane-1971-aspirin-mechanism
    type: peer-reviewed
    cite: "Vane JR. Inhibition of prostaglandin synthesis as a mechanism of action for aspirin-like drugs. Nat New Biol. 1971;231(25):232-5."
    doi: "10.1038/newbio231232a0"
    pmid: "5284360"
    url: "https://doi.org/10.1038/newbio231232a0"
  - id: nussmeier-2005-cox-cardiovascular
    type: peer-reviewed
    cite: "Nussmeier NA, Whelton AA, Brown MT, et al. Complications of the COX-2 inhibitors parecoxib and valdecoxib after cardiac surgery. N Engl J Med. 2005;352(11):1081-91."
    doi: "10.1056/NEJMoa050330"
    pmid: "15713945"
    url: "https://doi.org/10.1056/NEJMoa050330"
  - id: hernandez-diaz-2000-nsaid-gi
    type: peer-reviewed
    cite: "Hernandez-Diaz S, Rodriguez LA. Association between nonsteroidal anti-inflammatory drugs and upper gastrointestinal tract bleeding/perforation: an overview of epidemiologic studies published in the 1990s. Arch Intern Med. 2000;160(14):2093-9."
    doi: "10.1001/archinte.160.14.2093"
    pmid: "10904451"
    url: "https://doi.org/10.1001/archinte.160.14.2093"
cross_links:
  - target: 01-human/03-molecular/prostaglandins
    relation: modulates
    evidence: vane-1971-aspirin-mechanism
    note: "Ibuprofen reversibly occupies the cyclooxygenase channel of both COX-1 (PTGS1) and COX-2 (PTGS2) → prevents arachidonic acid access to the catalytic tyrosine (Tyr385) → ↓ PGE₂, PGI₂, PGD₂, PGF₂α, TXA₂ synthesis — reducing inflammation, pain sensitization, fever, and platelet aggregation."
  - target: 01-human/07-system/gout
    relation: treats
    note: "Ibuprofen and NSAIDs are first-line for acute gout: COX-2-driven PGE₂ amplifies NLRP3-IL-1β neutrophil recruitment to MSU crystal deposits; 600–800 mg TDS × 7–10 days; contraindicated in eGFR <30; colchicine preferred when CKD coexists."
  - target: 01-human/07-system/rheumatoid-arthritis
    relation: treats
    note: "NSAIDs were first-line RA therapy before DMARDs; COX-2-driven synovial PGE₂ drives joint pain, swelling, and stiffness; ibuprofen reduces RA symptoms but not radiographic progression; now adjunct to MTX/biologics; PPI required for long-term use."
  - target: 01-human/07-system/stroke
    relation: connects-to
    note: "Non-selective NSAIDs including ibuprofen increase ischemic stroke/MI risk ~1.3–1.5× via ↓ endothelial PGI₂; ibuprofen taken before aspirin blocks irreversible COX-1 acetylation → ↓ cardioprotective antiplatelet effect; naproxen shows lowest CV risk among NSAIDs."
---

# Ibuprofen

## Overview

**Ibuprofen** (Advil, Nurofen, Motrin) is the world's most widely used **non-steroidal anti-inflammatory drug (NSAID)** and OTC analgesic — consumed by an estimated 30 million people daily. Developed by Boots Company chemists (Adams, Nicholson, Halliday, Moss and colleagues) in the early 1960s as a safer alternative to aspirin, it was first prescribed in the UK in 1969 and became OTC in 1983. The Nobel Prize-winning discovery of prostaglandin synthesis inhibition as the mechanism of aspirin-like drugs (Vane 1971) [^vane-1971-aspirin-mechanism] explained ibuprofen's triad of effects: **analgesic, antipyretic, and anti-inflammatory**.

Ibuprofen is a racemic propionic acid NSAID: the S(+)-enantiomer is pharmacologically active; the R(−)-enantiomer is pharmacologically inactive but partially converted to S(+) in vivo by unidirectional chiral inversion. Both COX-1 and COX-2 are reversibly inhibited.

## Mechanism

**Cyclooxygenase (COX) biology:**
- **COX-1 (PTGS1):** Constitutively expressed in most tissues; generates prostaglandins for homeostatic functions — gastric mucosal protection (PGE₂, PGI₂ stimulate mucus and bicarbonate secretion, reduce acid secretion, maintain mucosal blood flow), platelet aggregation (TXA₂ in platelets), renal blood flow regulation
- **COX-2 (PTGS2):** Inducible; upregulated by inflammatory stimuli (IL-1β, TNFα, LPS) in macrophages, synoviocytes, and other cells → produces PGE₂ and PGI₂ that:
  - Sensitize nociceptors (TRPV1, Nav1.7/1.8) → peripheral sensitization → pain
  - Act on hypothalamus (EP3 receptor) → ↑ body temperature set-point → fever
  - Mediate vasodilation and edema at inflammatory sites

**COX inhibition mechanism:**
1. Arachidonic acid (20:4 n-6) is liberated from membrane phospholipids by phospholipase A2 (PLA2) in response to inflammatory signals
2. COX enzymes catalyze the cyclooxygenase reaction (2 O₂ + arachidonic acid → PGG₂) and peroxidase reaction (PGG₂ → PGH₂) — using a tyrosyl radical at Tyr385 in the catalytic channel
3. **Ibuprofen:** Occupies the hydrophobic cyclooxygenase channel, sterically blocking arachidonic acid access to Tyr385; binding is **reversible** (non-covalent) and competitive — unlike aspirin's irreversible acetylation; IC₅₀ COX-1 ~1–3 μM, COX-2 ~15–30 μM (modest COX-1 selectivity in practice)
4. Net effect: ↓ PGG₂ → ↓ PGH₂ → ↓ all downstream prostaglandins (PGE₂, PGI₂, PGD₂, PGF₂α) and thromboxane A₂ (TXA₂) [^vane-1971-aspirin-mechanism]

**Pharmacokinetics:**
- Oral bioavailability: ~80–90%
- Protein binding: ~99% (albumin)
- Onset of effect: 30–60 min; peak 1–2 h
- Half-life: ~2 h (short — requires q6–8h dosing)
- Metabolized by CYP2C9 (hydroxylation); renal elimination; no active metabolites

## Clinical Use

**Pain:**
- Mild-moderate pain: 200–400 mg q4–6h PO (OTC); max 1200 mg/day OTC, 3200 mg/day prescription
- Comparable or superior to paracetamol (acetaminophen) for acute musculoskeletal pain and dental pain; equivalent to codeine combinations without opioid risks

**Fever:**
- 5–10 mg/kg q6–8h in children (superior to paracetamol in some fever severity comparisons); adult 400 mg q6–8h

**Inflammatory Conditions:**
- Rheumatoid arthritis, osteoarthritis: 400–800 mg TDS-QDS (prescription doses)
- Acute gout: NSAIDs (including ibuprofen) are first-line for acute attack (COX-2-mediated NLRP3 inflammasome involvement)
- Primary dysmenorrhea: 400–600 mg q4h; highly effective (PGE₂/PGF₂α cause uterine contractions)

**Key adverse effects and contraindications:**
- **GI toxicity (COX-1 mediated):** Gastric mucosal injury — peptic ulcers, GI bleeding. Risk 3–5× increased vs non-users; ~1/1000 patient-years serious GI event [^hernandez-diaz-2000-nsaid-gi]. Mitigate with PPI co-prescription in high-risk patients (age >65, prior PUD, anticoagulants)
- **Cardiovascular risk (COX-2 mediated):** All non-selective NSAIDs and COX-2 inhibitors increase MI/stroke risk via imbalance: ↓ endothelial PGI₂ (anti-thrombotic, vasodilatory) while platelet TXA₂ persists; risk ~1.3–1.6× relative risk vs non-users; higher at doses ≥1200 mg/day [^nussmeier-2005-cox-cardiovascular]
- **Renal:** ↓ renal prostaglandins → ↓ GFR in volume-depleted patients; acute kidney injury with dehydration/diuretics/ACE inhibitors ("triple whammy" combination); contraindicated in eGFR <30 mL/min
- **Platelet function:** Reversible platelet COX-1 inhibition; returns to normal within 24–48h of last dose (unlike aspirin's irreversible inhibition)
- **Drug interactions:** Competes with aspirin for COX-1 binding — ibuprofen taken before aspirin can block aspirin's antiplatelet effect; avoid regular ibuprofen use in patients on cardioprotective aspirin
- **Pregnancy:** Avoid after 20 weeks (premature ductus arteriosus closure, oligohydramnios); contraindicated after 30 weeks
- **Asthma:** NSAID-exacerbated respiratory disease (AERD/Samter's triad) in ~10% of asthmatics — COX-1 inhibition redirects arachidonic acid to lipoxygenase pathway → ↑ cysteinyl leukotrienes → bronchospasm

## Evidence

| Study | Population | Key Finding |
|:---|:---|:---|
| VIGOR / CLASS trials (rofecoxib/celecoxib) | Arthritis populations | Selective COX-2 inhibitors reduce GI events ~50% vs non-selective NSAIDs; rofecoxib increased MI risk → withdrawal 2004; confirmed CV risk class effect for all NSAIDs |
| Pharmacoepidemiology (Hernandez-Diaz 2000) [^hernandez-diaz-2000-nsaid-gi] | Population-based case-control | NSAIDs increase upper GI bleeding/perforation 3.7× vs non-users; ibuprofen lower risk than indomethacin/naproxen at equivalent doses |
| Meta-analysis (Coxib and traditional NSAID trialists) | 280,000 patients | NSAIDs increase MI risk ~30% (RR 1.3–1.5); ibuprofen comparable to diclofenac and naproxen; naproxen shows lower CV risk in some analyses |
| Mechanism discovery (Vane 1971) [^vane-1971-aspirin-mechanism] | Landmark biochemistry | Cyclooxygenase inhibition demonstrated as mechanism of aspirin/ibuprofen class; Nobel Prize 1982 |

## Connections

- **Modulates** → [Prostaglandins](../../../../../01-human/03-molecular/prostaglandins/README.md): Reversible COX-1/COX-2 inhibition → ↓ all prostanoids; ↓ PGE₂ reduces pain sensitization and fever; ↓ TXA₂ reduces platelet aggregation.
- **Targets** → [COX-2](../../../../../01-human/03-molecular/cox-2/README.md): COX-2 inhibition is the anti-inflammatory mechanism; COX-2-derived PGE₂ drives peripheral pain sensitization and hypothalamic fever response; inducible by IL-1β/TNFα in inflammatory cells.
- **Treats** → [Gout](../../../../../01-human/07-system/gout/README.md): First-line NSAID for acute gout flares; COX-2-driven PGE₂ amplifies NLRP3-IL-1β neutrophil recruitment to MSU crystal deposits; 600–800 mg TDS × 7–10 days; contraindicated in eGFR <30; colchicine preferred when CKD coexists.
- **Treats** → [Rheumatoid Arthritis](../../../../../01-human/07-system/rheumatoid-arthritis/README.md): COX-2-driven synovial PGE₂ drives joint pain, swelling, and stiffness; ibuprofen reduces RA symptoms but not radiographic progression; now adjunct to MTX/biologics; PPI required for long-term use.
- **Connects-to** → [Stroke](../../../../../01-human/07-system/stroke/README.md): NSAIDs including ibuprofen increase ischemic stroke/MI risk ~1.3–1.5× via ↓ endothelial PGI₂; ibuprofen blocks aspirin's irreversible COX-1 acetylation → ↓ cardioprotective antiplatelet effect; naproxen shows lowest CV risk among NSAIDs.

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
