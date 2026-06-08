---
schema: human-scale-entry/v1
id: thrombin
name: Thrombin
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-07
summary: "Thrombin (Factor IIa) is the central coagulation serine protease cleaving fibrinogen to fibrin, activating platelets via PAR-1, and amplifying the clotting cascade; arterial thrombi cause ischemic stroke and MI; dabigatran (direct thrombin inhibitor) prevents thrombotic events."
aliases: ["thrombin", "Factor IIa", "prothrombin", "F2", "serine protease", "coagulation cascade", "dabigatran", "PAR-1", "direct thrombin inhibitor", "DTI", "fibrin clot", "anticoagulant"]
cross_links:
  - target: 01-human/07-system/stroke
    relation: connects-to
    note: "Thrombin generates fibrin clots in cerebral arteries → ischemic stroke; AF→ atrial thrombus → embolism → cardioembolic stroke; ICH → thrombin release → perihematomal inflammation and edema; dabigatran (direct thrombin inhibitor) and apixaban/rivaroxaban prevent AF-related stroke."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "Thrombin cleaves fibrinogen → fibrin clot in coronary arteries → ACS/MI; thrombin activates PAR-1 on platelets → thrombus propagation; vorapaxar (PAR-1 antagonist) reduces recurrent MI; warfarin and DOACs prevent VTE and AF-related stroke."
  - target: 01-human/03-molecular/nlrp3-inflammasome
    relation: connects-to
    note: "Thrombin activates PAR-1 on macrophages and endothelial cells → NF-κB → NLRP3 priming and pro-IL-1β synthesis; ICH-derived thrombin in perihematomal brain tissue → NLRP3 → IL-1β → secondary brain injury and edema."
  - target: 01-human/03-molecular/fibrinogen
    relation: connects-to
    note: "Thrombin cleaves fibrinopeptides A and B from fibrinogen → fibrin monomers → spontaneous polymerization → branching fibrin network; Factor XIIIa (activated by thrombin) cross-links fibrin → lysis-resistant clot; fibrinogen is rate-limiting for clot formation in coagulopathy."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "Thrombin is the central effector of venous thrombus formation: stasis → contact activation (FXI→FIXa) → FX → thrombin → fibrin; DOACs (dabigatran: direct thrombin inhibitor; rivaroxaban/apixaban: FXa inhibitors) prevent and treat DVT/PE; LMWH inhibits thrombin via antithrombin."
  - target: 01-human/07-system/disseminated-intravascular-coagulation
    relation: connects-to
    note: "Systemic TF/thrombin activation is the central mechanism of DIC: infection → cytokines → TF → FVIIa/TF → FX → thrombin → fibrin microthrombi; thrombin also exhausts protein C/S and antithrombin → feedback amplification; dabigatran/heparin block thrombin but treat cause first."
  - target: 01-human/03-molecular/c1-esterase-inhibitor
    relation: connects-to
    note: "C1-INH inhibits FXII (Hageman factor) and FXIa, dampening contact activation that can also trigger thrombin generation; in HAE, FXII activation → kallikrein → bradykinin (not thrombin) dominates; C1-INH and thrombin pathways share FXII/FXIa as regulatory nodes."
  - target: 01-human/03-molecular/protein-c
    relation: connects-to
    note: "Thrombin-thrombomodulin complex activates protein C → APC; APC + protein S inactivate FVa/FVIIIa → halts thrombin generation; APC has anti-inflammatory effects via EPCR/PAR-1 signaling; FV Leiden R506Q blocks APC cleavage at Arg506 → APC resistance → thrombophilia."
  - target: 01-human/07-system/inherited-thrombophilia
    relation: connects-to
    note: "FV Leiden (5% Europeans; APC resistance) and prothrombin G20210A (~2-3%) are the most common inherited thrombophilias downstream of thrombin; FVL blocks APC cleavage of FVa → persistent thrombin generation; prothrombin G20210A → elevated prothrombin → excess thrombin."
sources:
  - id: connolly-2009-re-ly
    type: peer-reviewed
    cite: "Connolly SJ, Ezekowitz MD, Yusuf S, et al. Dabigatran versus warfarin in patients with atrial fibrillation. N Engl J Med. 2009;361(12):1139-1151."
    doi: "10.1056/NEJMoa0905561"
    pmid: "19717844"
    url: "https://doi.org/10.1056/NEJMoa0905561"
  - id: mackman-2008-coagulation
    type: peer-reviewed
    cite: "Mackman N. Triggers, targets and treatments for thrombosis. Nature. 2008;451(7181):914-918."
    doi: "10.1038/nature06797"
    pmid: "18288180"
    url: "https://doi.org/10.1038/nature06797"
---

# Thrombin

## Overview

**Thrombin** (Factor IIa; gene *F2*, chromosome 11p11.2) is the **central serine protease of the coagulation cascade** — the enzyme that converts soluble **fibrinogen** to insoluble **fibrin**, activates platelets, amplifies upstream coagulation factors, and triggers both pro- and anti-coagulant feedback loops. Circulating as its inactive precursor **prothrombin** (Factor II), thrombin is activated by the **prothrombinase complex** (Factor Xa + Va + phospholipid membrane + Ca²⁺), which cleaves the Arg274–Thr275 and Arg323–Ile324 bonds to release the two-chain active enzyme.

Thrombin is simultaneously one of the most potent pro-thrombotic molecules in the body and the trigger for the natural anticoagulant response (protein C/S pathway) — its net effect depends on the vascular context. In the normal vessel lumen, thrombomodulin-bound thrombin activates protein C → anticoagulation and anti-fibrinolysis. At sites of vascular injury, exposed subendothelium amplifies thrombin → fibrin clot and platelet plug. Dysregulation of this balance causes thrombotic events (stroke, MI, DVT/PE) or coagulopathic bleeding [^mackman-2008-coagulation].

**Thrombin inhibition — clinical drug classes:**

| Drug class | Examples | Target | Indication |
|---|---|---|---|
| Vitamin K antagonist | Warfarin | Prothrombin synthesis (FII, FVII, FIX, FX) | AF, VTE, mechanical valves |
| Indirect thrombin inhibitor | Heparin, LMWH | Thrombin via antithrombin III | ACS, VTE, HIT prevention |
| Direct thrombin inhibitor (oral) | Dabigatran | Thrombin active site | AF stroke prevention, VTE |
| Direct thrombin inhibitor (IV) | Argatroban, bivalirudin | Thrombin | HIT, PCI |
| Factor Xa inhibitors | Rivaroxaban, apixaban, edoxaban | FXa (upstream of thrombin) | AF, VTE, ACS |
| PAR-1 antagonist | Vorapaxar | PAR-1 on platelets | Secondary prevention post-MI |

The **RE-LY trial** (Connolly 2009) demonstrated that dabigatran 150 mg twice daily was superior to warfarin for stroke prevention in AF (RR 0.66, P<0.001) with similar major bleeding and significantly less intracranial hemorrhage — establishing direct thrombin inhibition as a safer alternative to warfarin for AF [^connolly-2009-re-ly].

## Structure

Thrombin is a **72 kDa heterodimer** (A-chain 6 kDa + B-chain 31 kDa, linked by a single disulfide bond) derived from single-chain prothrombin (72 kDa) by prothrombinase cleavage:

**Active site (catalytic triad):**
- **Ser195–His57–Asp102** (chymotrypsin numbering) — the conserved serine protease catalytic triad; thrombin is a trypsin-like protease cleaving C-terminal to Arg residues (Arg-X bonds)
- Fibrinogen Aα and Bβ chains contain the thrombin cleavage sites (Arg16-Gly17 and Arg14-Gly15, respectively)
- Dabigatran (and other DTIs) bind the active site cleft via a bivalent interaction: one moiety occupies the S1 pocket (arginino-like interaction) + a second moiety occupies the S2 or fibrinogen-binding exosite

**Exosites:**
- **Exosite I (fibrin-binding exosite):** Basic residue surface; binds fibrin, hirudin C-terminus, thrombomodulin — mediates substrate recognition and fibrinolysis inhibition
- **Exosite II (heparin-binding exosite):** Positively charged; binds heparin sulfate proteoglycans — mediates thrombin localization on vessel surface and the thrombin-antithrombin III (AT-III) complex formation with heparin

**Dabigatran binding:**
- Reversible competitive inhibitor; directly occupies the thrombin active site; does not require AT-III cofactor (unlike heparin); predictable pharmacokinetics → fixed dosing without monitoring
- Reversed by **idarucizumab** (specific Fab fragment; binds dabigatran with ~350× higher affinity than thrombin; complete reversal within 4h)

## Function

**Procoagulant functions:**

1. **Fibrin generation:** Thrombin cleaves fibrinopeptide A (Aα chain) and fibrinopeptide B (Bβ chain) from fibrinogen → fibrin monomers → lateral aggregation (protofibrils) → branching fibrin network; half-staggered overlapping strands stabilized by Factor XIIIa (cross-links γ-γ and α-α chains)

2. **Platelet activation (PAR signaling):**
   - Thrombin cleaves and activates **PAR-1** and **PAR-4** on human platelets (PAR-1 primary, high-affinity; PAR-4 secondary, low-affinity)
   - PAR-1: tethered ligand mechanism — thrombin cleaves Arg41–Ser42 on PAR-1 → Ser42 becomes a new tethered agonist → Gαq + Gα₁₂/₁₃ → IP₃/DAG → Ca²⁺ + PKC → platelet shape change, granule secretion (ADP, serotonin, TXA₂), and integrin αIIbβ3 activation (fibrinogen binding → platelet aggregation)
   - **Vorapaxar (Zontivity):** Competitive PAR-1 antagonist; reduces recurrent MI by 13% and stroke by 17% in post-MI patients (TRA 2°P-TIMI 50 trial); increases intracranial hemorrhage → contraindicated in prior stroke/TIA

3. **Coagulation amplification:**
   - Activates Factor V → FVa (prothrombinase complex co-factor × 3000-fold acceleration)
   - Activates Factor VIII → FVIIIa (tenase complex co-factor)
   - Activates Factor XI → FXIa → intrinsic pathway amplification (relevant in contact activation and deep venous thrombosis)
   - Activates Factor XIII → FXIIIa (transglutaminase → fibrin cross-linking)

**Anticoagulant functions (Protein C pathway):**

1. Thrombin binds **thrombomodulin** (endothelial surface receptor) → conformational change → thrombin now activates **protein C** instead of fibrinogen/platelets
2. Activated protein C (APC) + protein S → inactivates **FVa** and **FVIIIa** → halts thrombin generation
3. APC also stimulates **fibrinolysis** and is anti-inflammatory (inhibits NF-κB, endothelial apoptosis)
4. **TAFI (Thrombin-Activatable Fibrinolysis Inhibitor):** Thrombin-thrombomodulin complex activates TAFI → TAFIa removes fibrin C-terminal Lys residues → blocks plasminogen binding → inhibits clot lysis; relevant to the balance of thrombosis vs. fibrinolysis

## Mechanism

**Coagulation cascade in stroke and cardiovascular disease:**

*Ischemic stroke:*
1. **Large vessel:** Carotid/vertebrobasilar atherosclerosis → plaque rupture → collagen/TF exposed → FVIIa/TF complex → FX → Xa → thrombin → fibrin → embolus → cerebral artery occlusion
2. **Cardioembolic (AF):** Atrial fibrillation → stasis → Virchow's triad → atrial thrombus (fibrin-rich, from slow flow; DOACs > warfarin for prevention) → embolism → ischemic stroke
3. **Small vessel:** Lipohyalinosis of penetrating arteries → thrombosis in situ → lacunar infarct (anticoagulants not indicated here; antiplatelet preferred)

*Hemorrhagic stroke (ICH):*
- Intracerebral hemorrhage → hematoma → thrombin released from lysed RBCs and clot dissolution
- Thrombin → **PAR-1** on microglia → NF-κB → TNF-α, IL-6 → perihematomal edema (peaks at 24-72h)
- Thrombin → direct neurotoxicity (apoptosis via Rho/ROCK pathway, ERK activation)
- Hematoma expansion (20-30% of ICH) → worsened prognosis; coagulopathy risk factors

**Direct thrombin inhibitors vs. Factor Xa inhibitors:**

| Property | Dabigatran (DTI) | Apixaban/Rivaroxaban (FXa-I) |
|---|---|---|
| Target | Thrombin (FIIa) | Factor Xa |
| Renal clearance | ~80% | ~25-33% |
| CKD dose adjustment | Required (avoid <15 mL/min) | Yes (limited use <15 mL/min) |
| Reversal agent | Idarucizumab | Andexanet alfa |
| Drug interactions | P-gp substrate | CYP3A4 + P-gp substrate |
| Measurement | Ecarin clotting time, TT | Anti-Xa assay |

## Connections

Thrombin generates fibrin clots in cerebral arteries → ischemic stroke; AF→ atrial thrombus → embolism → cardioembolic stroke; ICH → thrombin release → perihematomal inflammation and edema; dabigatran (direct thrombin inhibitor) and apixaban/rivaroxaban prevent AF-related stroke.

Thrombin cleaves fibrinogen → fibrin clot in coronary arteries → ACS/MI; thrombin activates PAR-1 on platelets → thrombus propagation; vorapaxar (PAR-1 antagonist) reduces recurrent MI; warfarin and DOACs prevent VTE and AF-related stroke.

Thrombin activates PAR-1 on macrophages and endothelial cells → NF-κB → NLRP3 priming and pro-IL-1β synthesis; ICH-derived thrombin in perihematomal brain tissue → NLRP3 → IL-1β → secondary brain injury and edema.

Thrombin cleaves fibrinopeptides A and B from fibrinogen → fibrin monomers → spontaneous polymerization → branching fibrin network; Factor XIIIa (activated by thrombin) cross-links fibrin → lysis-resistant clot; fibrinogen is rate-limiting for clot formation in coagulopathy.

- `connects-to` → **[Venous Thromboembolism](../../07-system/venous-thromboembolism/README.md)** — Thrombin is the central effector of venous thrombus formation: stasis → contact activation (FXI→FIXa) → FX → thrombin → fibrin; DOACs (dabigatran: direct thrombin inhibitor; rivaroxaban/apixaban: FXa inhibitors) prevent and treat DVT/PE; LMWH/UFH inhibit thrombin via antithrombin.
- `connects-to` → **[Disseminated Intravascular Coagulation](../../07-system/disseminated-intravascular-coagulation/README.md)** — Systemic TF/thrombin activation is the central mechanism of DIC: infection → cytokines → TF → FVIIa/TF → FX → thrombin → fibrin microthrombi; thrombin also exhausts protein C/S and antithrombin → feedback amplification; treat underlying cause first, heparin for thrombosis-dominant DIC.
- `connects-to` → **[C1-Esterase Inhibitor](../c1-esterase-inhibitor/README.md)** — C1-INH inhibits FXII (Hageman factor) and FXIa, dampening contact activation that can also trigger thrombin generation; in HAE, FXII activation → kallikrein → bradykinin (not thrombin) dominates; C1-INH and thrombin pathways share FXII/FXIa as regulatory nodes.
- `connects-to` → **[Protein C](../protein-c/README.md)** — Thrombin-thrombomodulin complex activates protein C → APC; APC + protein S inactivate FVa/FVIIIa → halts thrombin generation; APC has anti-inflammatory effects via EPCR/PAR-1 signaling; FV Leiden R506Q blocks APC cleavage at Arg506 → APC resistance → thrombophilia.
- `connects-to` → **[Inherited Thrombophilia](../../07-system/inherited-thrombophilia/README.md)** — FV Leiden (5% Europeans; APC resistance) and prothrombin G20210A (~2-3%) are the most common inherited thrombophilias downstream of thrombin; FVL blocks APC cleavage of FVa → persistent thrombin generation; prothrombin G20210A → elevated prothrombin → excess thrombin.

[^connolly-2009-re-ly]: Connolly SJ, Ezekowitz MD, Yusuf S, et al. Dabigatran versus warfarin in patients with atrial fibrillation. *N Engl J Med.* 2009;361(12):1139-1151. [doi:10.1056/NEJMoa0905561](https://doi.org/10.1056/NEJMoa0905561) · [PubMed 19717844](https://pubmed.ncbi.nlm.nih.gov/19717844/)
[^mackman-2008-coagulation]: Mackman N. Triggers, targets and treatments for thrombosis. *Nature.* 2008;451(7181):914-918. [doi:10.1038/nature06797](https://doi.org/10.1038/nature06797) · [PubMed 18288180](https://pubmed.ncbi.nlm.nih.gov/18288180/)
