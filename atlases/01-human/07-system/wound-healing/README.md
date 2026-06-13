---
schema: human-scale-entry/v1
id: wound-healing
name: Wound Healing
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-07
summary: "Wound healing: hemostasis → inflammation → proliferation (granulation + re-epithelialization) → remodeling. PDGF, TGF-β, VEGF, FN, and EGF orchestrate each phase. Chronic wounds arise from impaired M1→M2 switch; diabetic ulcers are the leading cause of non-traumatic amputation."
aliases: ["wound repair", "cutaneous wound healing", "tissue repair", "skin healing", "chronic wound", "diabetic wound"]
sources:
  - id: singer-1999-wound-healing-review
    type: peer-reviewed
    cite: "Singer AJ, Clark RA. Cutaneous wound healing. N Engl J Med. 1999;341(10):738-746."
    doi: "10.1056/NEJM199909023411006"
    pmid: "10471461"
    url: "https://doi.org/10.1056/NEJM199909023411006"
  - id: gurtner-2008-wound-repair-regeneration
    type: peer-reviewed
    cite: "Gurtner GC, Werner S, Barrandon Y, Longaker MT. Wound repair and regeneration. Nature. 2008;453(7193):314-321."
    doi: "10.1038/nature07039"
    pmid: "18480812"
    url: "https://doi.org/10.1038/nature07039"
  - id: eming-2014-wound-repair-mechanisms
    type: peer-reviewed
    cite: "Eming SA, Martin P, Tomic-Canic M. Wound repair and regeneration: mechanisms, signaling, and translation. Sci Transl Med. 2014;6(265):265sr6."
    doi: "10.1126/scitranslmed.3009337"
    pmid: "25473038"
    url: "https://doi.org/10.1126/scitranslmed.3009337"
cross_links:
  - target: 01-human/03-molecular/fibronectin
    relation: connects-to
    note: "Plasma FN is cross-linked into fibrin clots → provisional scaffold for platelets, neutrophils, and fibroblasts; cellular FN from fibroblasts drives granulation tissue; FN-integrin α5β1 → fibroblast migration and myofibroblast differentiation → wound contraction and closure."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "TGF-β1 from platelets and macrophages drives myofibroblast differentiation (α-SMA+ → wound contraction), collagen I synthesis, and re-epithelialization; excess TGF-β → hypertrophic scar and keloid; TGF-β3 promotes scarless fetal healing; pirfenidone inhibits fibrogenic signaling."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "VEGF-A from keratinocytes and macrophages drives angiogenesis into the wound bed; HIF-1α (hypoxic wound center) → VEGF → new vessel formation in granulation tissue; anti-VEGF therapy impairs wound healing — a known adverse effect of bevacizumab and other anti-VEGF agents."
  - target: 01-human/07-system/diabetic-retinopathy
    relation: connects-to
    note: "Diabetes impairs wound healing through AGE accumulation, pericyte dysfunction, impaired neutrophil function, and reduced HIF-1α/VEGF response; diabetic foot ulcers affect ~15% of people with diabetes and are the leading cause of non-traumatic amputation."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Macrophages orchestrate wound healing's inflammatory-to-proliferative switch: M1 cells clear debris, then become M2 cells that secrete TGF-β1, PDGF, VEGF, and IGF-1 to drive fibroblasts, angiogenesis, and re-epithelialization; a failed M1→M2 switch defines chronic wounds."
  - target: 01-human/04-cellular/fibroblast
    relation: connects-to
    note: "Wound fibroblasts migrate along the fibronectin scaffold and lay down the type III collagen of granulation tissue; TGF-β1 plus tension converts them into α-SMA+ myofibroblasts that contract the wound and, failing to apoptose, produce hypertrophic scars and keloids."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "Cutaneous repair is the canonical wound-healing model — hemostasis, inflammation, proliferation, remodeling — restoring the skin barrier with a fibrotic scar rather than regeneration; chronic non-healing ulcers (diabetic, venous, pressure) carry a ~$31 billion annual US burden."
  - target: 01-human/04-cellular/platelet
    relation: connects-to
    note: "Platelets fire the starting gun of wound healing: at injury they form the hemostatic plug and degranulate, releasing PDGF, TGF-β, and VEGF that recruit neutrophils and macrophages and prime fibroblasts — the growth-factor surge launching the inflammatory phase."
  - target: 01-human/03-molecular/collagen
    relation: connects-to
    note: "Collagen is the structural endpoint of wound healing: fibroblasts first lay down weak type III collagen in granulation tissue, which remodeling replaces with cross-linked type I collagen regaining ~80% of tensile strength over months; dysregulated turnover yields keloids."
  - target: 01-human/07-system/systemic-sclerosis
    relation: connects-to
    note: "Systemic sclerosis is wound healing that never stops: the TGF-β-driven myofibroblast activation and collagen deposition that should close a wound and resolve becomes self-sustaining and widespread, scarring skin and organs — fibrosis is dysregulated persistent repair."
  - target: 01-human/07-system/type-2-diabetes
    relation: connects-to
    note: "Diabetes is the leading cause of chronic non-healing wounds: hyperglycemia impairs every healing phase—blunting neutrophil and macrophage function, stiffening capillaries, adding neuropathy—so diabetic foot ulcers stall and drive most non-traumatic amputations."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "Angiogenesis by endothelial cells is essential to wound healing: VEGF from the wound bed drives endothelial sprouting that forms granulation tissue's capillaries, restoring oxygen—when this fails (ischemia, diabetes), the wound cannot progress to repair."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "Wound healing is the integumentary system restoring its barrier: hemostasis, inflammation, proliferation, and remodeling rebuild epidermis and dermis after injury, but imperfectly—scar replaces the original architecture, lacking hair follicles and full strength."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "Neutrophils lead the inflammatory phase of wound healing: arriving within hours, they kill bacteria and clear debris, but their proteases also damage tissue—so timely resolution is essential, and persistent neutrophilia underlies chronic non-healing wounds."
  - target: 01-human/03-molecular/pdgf
    relation: connects-to
    note: "PDGF is a master growth factor of wound repair: released by degranulating platelets, it recruits and activates fibroblasts and smooth muscle, driving granulation tissue and collagen deposition—and recombinant PDGF (becaplermin) treats diabetic foot ulcers."
  - target: 01-human/07-system/obesity
    relation: connects-to
    note: "Obesity impairs wound healing: poor tissue perfusion, chronic low-grade inflammation, and frequent coexisting diabetes slow each phase of repair, so obese and diabetic patients suffer more wound dehiscence, infection and chronic ulcers—a major surgical burden."
---

# Wound Healing

## Overview

**Wound healing** is the fundamental biological process by which multicellular organisms restore tissue integrity after injury. In mammals, cutaneous wound healing (skin) is the most studied model and proceeds through **four overlapping, coordinated phases** [^singer-1999-wound-healing-review]:

1. **Hemostasis (seconds to hours):** Platelet activation, fibrin clot formation, and provisional matrix deposition
2. **Inflammation (hours to days):** Neutrophil and macrophage infiltration; debridement, antimicrobial defense, and growth factor release
3. **Proliferation (days to weeks):** Fibroblast migration, granulation tissue formation, angiogenesis, re-epithelialization, and wound contraction
4. **Remodeling (weeks to years):** Scar maturation, collagen crosslinking and reorganization, and vasculature regression

**Evolutionary context:** Complete regeneration (scarless repair with restoration of hair follicles, glands, and full tissue architecture) occurs in some vertebrates (axolotl, zebrafish) and in mammalian fetal wounds (<18 weeks gestation). Adult mammalian repair is predominantly fibrotic and scar-forming — a trade-off favoring rapid barrier restoration over perfect structural restoration.

**Clinical burden of impaired healing:**
- **Chronic wounds** (non-healing >3 months): Diabetic foot ulcers (~6.4 million US), venous leg ulcers (~2.5 million US), pressure ulcers (~2 million US); total burden ~$31 billion/year in the US
- **Hypertrophic scars and keloids:** Pathological fibroproliferative responses; affected by genetic predisposition (darker skin types), wound location (sternum, shoulder, earlobe), and infection
- **Pathological under-healing:** Anastomotic dehiscence post-surgery; pressure ulcers in the spinal cord injured; radiation-induced impaired healing

## Structure

### Four-phase molecular framework

**Phase 1 — Hemostasis (seconds to ~30 min):**
- Vascular injury → sub-endothelial collagen exposed → **von Willebrand factor (vWF)** bridges collagen to platelet GPIbα → platelet adherence → **platelet activation** (shape change, degranulation)
- Platelet α-granule contents released: **fibrinogen, FN, vWF, thrombospondin, PDGF-AB/BB, TGF-β1, EGF, FGF-2** — the initial growth factor payload at wound sites
- Extrinsic coagulation cascade: tissue factor (TF) from injured fibroblasts/endothelium → VIIa → Xa/Va → thrombin → fibrinogen → **fibrin clot**; cross-linked by FXIIIa (transglutaminase) → fibrin-FN provisional matrix
- **Provisional matrix composition:** Fibrin + fibronectin + vitronectin + tenascin-C; serves as scaffold for neutrophil and macrophage migration and as a reservoir for growth factors (PDGF, TGF-β, FGF bound to matrix)

**Phase 2 — Inflammation (hours to days 1-5):**

*Neutrophil phase (0-72h):*
- Platelet-derived **CXCL4 (PF4), CXCL7 (NAP-2), CCL3** + mast cell histamine → neutrophil recruitment
- Neutrophils: phagocytosis of bacteria, debris; **NETs (neutrophil extracellular traps)** in infected wounds; elastase + MMP-8 debridement; ROS generation (respiratory burst)
- Resolution: neutrophil apoptosis → efferocytosis by macrophages → switch from M1 → M2 phenotype

*Macrophage phase (day 2-5):*
- **M1 macrophages** (classically activated): CCL2 + CXCL8-driven recruitment → TNF-α, IL-1β, IL-6, MMP-9 → antimicrobial; remove neutrophil corpses
- **M2 macrophages** (alternatively activated): IL-4/IL-13 (from eosinophils/mast cells) → Arg-1, CD163, TGF-β1, PDGF, VEGF, IGF-1 → transition to proliferative phase; impaired M1→M2 switch = hallmark of chronic wounds
- Macrophage VEGF → capillary ingrowth; macrophage TGF-β1 → fibroblast activation; macrophage IGF-1 → keratinocyte proliferation

**Phase 3 — Proliferation (day 4 to week 3):**

*Fibroblast activation and granulation tissue:*
- PDGF-BB (from platelets + macrophages) + TGF-β1 → fibroblast chemotaxis into wound via α5β1-FN haptotaxis → fibroblast proliferation (FGF-2) → **granulation tissue**: type III collagen + fibronectin + hyaluronic acid + abundant capillaries (from VEGF-driven angiogenesis)
- **Myofibroblast differentiation** (critical event): TGF-β1 + mechanical tension + EDA-FN → α-SMA incorporation into stress fibers → **wound contraction** (~30-40% of wound closure area reduction) via myofibroblast isometric contraction; myofibroblasts produce type I/III collagen, FN, fibrillin

*Re-epithelialization:*
- Within hours of injury, leading-edge keratinocytes dissolve hemidesmosomes, extend lamellipodia, and migrate across the provisional matrix (integrin αvβ5-FN, α5β1-FN, α2β1-collagen)
- EGF (from platelets) + KGF/FGF-7 (from fibroblasts) + HGF → keratinocyte migration and proliferation; MMP-1 (collagenase) cleaves type I collagen for keratinocyte path-clearing
- Contact inhibition and TGF-β1 → regeneration of stratified epidermis and basement membrane (laminin-5, collagen IV) once wound surface is covered
- **Stem cell contribution:** Bulge stem cells of hair follicles → accelerate re-epithelialization; important in deep partial-thickness burns

*Angiogenesis:*
- Wound hypoxia → HIF-1α → VEGF-A + PDGF-B + Ang-2 → endothelial tip cells sprout from wound margins; pericyte recruitment (PDGF-B/PDGFR-β) → vessel stabilization
- Granulation tissue is among the most vascularized tissues transiently; vasculature density ~50% higher than normal dermis

**Phase 4 — Remodeling (week 3 to 1-2 years):**
- Type III collagen (flexible, rapid; predominates in granulation tissue) → replaced by type I collagen (stronger, stiffer) via MMP-1/3/13 + TIMP-1/2 balance
- Collagen fiber reorganization: random fibers (in early scar) → parallel arrays (in mature scar; tensile strength returns to ~80% of unwounded skin by 12 months — never reaches 100%)
- **Myofibroblast apoptosis:** TGF-β withdrawal + mechanical unloading → myofibroblast apoptosis; failure of apoptosis → hypertrophic scar or keloid (persistent α-SMA+ fibroblasts)
- Vasculature regression: Ang-1/Tie2 stabilization + VEGF withdrawal → capillary pruning → mature scar is less vascular than granulation tissue

## Function

### Key growth factor axes in wound healing

| Growth Factor | Source | Primary wound effect |
|:---|:---|:---|
| **PDGF-BB** | Platelets, macrophages | Fibroblast/pericyte chemotaxis and proliferation; most potent fibroblast mitogen |
| **TGF-β1** | Platelets, macrophages, fibroblasts | Myofibroblast differentiation; collagen synthesis; re-epithelialization; scar formation |
| **EGF/EGFR** | Platelets, macrophages | Keratinocyte migration and proliferation; re-epithelialization |
| **VEGF-A** | Macrophages, keratinocytes | Angiogenesis into granulation tissue; wound vasculature formation |
| **FGF-2 (bFGF)** | Fibroblasts, endothelium | Fibroblast and endothelial proliferation; angiogenesis; basement membrane reconstitution |
| **KGF/FGF-7** | Fibroblasts (paracrine) | Keratinocyte-specific mitogen; re-epithelialization |
| **IGF-1** | Macrophages, fibroblasts | Fibroblast and keratinocyte proliferation; synergizes with PDGF/EGF |

### Therapeutic interventions

**Topical growth factors (approved):**
- **Becaplermin (Regranex; recombinant PDGF-BB):** FDA-approved for diabetic foot ulcers; 30% complete healing improvement vs. placebo; Black Box Warning: increased cancer risk at ≥3 tube applications (controversial, epidemiologic signal)
- **Epidermal growth factor (EGF) topical:** Approved in some countries for diabetic and burn wounds; accelerates re-epithelialization

**Advanced wound dressings:**
- **Negative pressure wound therapy (NPWT; VAC therapy):** Mechanical suction removes exudate, reduces edema, promotes granulation tissue by increasing local perfusion; standard of care for complex wounds, dehiscence, and diabetic foot ulcers
- **Collagen/ORC matrix dressings:** Provide provisional ECM scaffold; promote FN deposition; inhibit excess MMPs in chronic wounds
- **Skin substitutes:** Apligraf (bilayered living cell construct — allogeneic fibroblasts + keratinocytes) and Dermagraft (fibroblast-seeded scaffold) — FDA-approved for venous leg ulcers and diabetic foot ulcers; temporary coverage and growth factor delivery

**Gene and cell therapy (investigational):**
- Adipose-derived MSC and bone marrow MSC: Paracrine VEGF/PDGF/FGF secretion → accelerated neovascularization; Phase 2/3 trials in diabetic foot ulcers
- HIF-1α gene therapy: Increased VEGF expression → angiogenesis; studied in critical limb ischemia + wound healing

### Impaired wound healing — chronic wounds

**Diabetic wounds:**
- Hyperglycemia → AGE → RAGE activation → NF-κB → inflammatory cytokines; impaired neutrophil function (reduced phagocytosis); impaired keratinocyte EGFR signaling; reduced HIF-1α (prolyl hydroxylase overactive in high glucose) → reduced VEGF → poor angiogenesis
- Peripheral neuropathy → insensate foot → repetitive trauma; peripheral vascular disease → ischemia
- **Diabetic foot ulcers:** Texas classification (depth, infection, ischemia); off-loading is critical; MDT (vascular surgery, orthotics, wound care, endocrinology)

**Venous leg ulcers:**
- Chronic venous hypertension → fibrin/fibronectin pericapillary cuffing → diffusion barrier + growth factor trapping → impaired wound healing; elevated MMP-1/MMP-9 in wound fluid degrades provisional matrix faster than it can be deposited

**Pressure ulcers:**
- Sustained pressure > capillary closing pressure → ischemia → necrosis; common over bony prominences (sacrum, heel, trochanter); staged I-IV by NPIAP classification; reactive oxygen species burst upon reperfusion → additional injury

## Pathology

**Hypertrophic scars:**
- Elevated scar confined to wound margins; TGF-β1 excess → persistent myofibroblasts; type III collagen dominance; spontaneous resolution possible (12-24 months); treatment: intralesional triamcinolone, silicone sheets, pressure garments

**Keloids:**
- Scar tissue extends beyond original wound margins; genetic predisposition (particularly Fitzpatrick IV-VI skin types; Chr15q21, FN1, NEDD4 risk variants); MMP-1↓ + TIMP-2↑ → collagen accumulation; myofibroblasts resist apoptosis; treatment difficult: triamcinolone ± 5-FU ± surgery ± radiation; 50-80% recurrence without adjuvant therapy

**Wound infection:**
- Biofilm formation (Staphylococcus aureus, Pseudomonas aeruginosa) prevents healing; S. aureus virulence factors degrade FN (staphylokinase, SplA/B proteases) → disrupts provisional matrix; biofilm-embedded bacteria resist antibiotics (100-1000× higher MIC); require mechanical debridement + biofilm-disrupting agents (cadexomer iodine, DACC dressings)

**Scarless fetal healing:**
- Fetal wounds (<18-20 weeks gestation) heal without scar; high hyaluronic acid → anti-inflammatory; TGF-β3 > TGF-β1/2 → less myofibroblast activation; robust inflammation resolution; therapeutic target: TGF-β3 analogs (avotermin — Phase 2; failed Phase 3 vs. placebo for improved scar appearance)

## Connections

- `connects-to` → **[Fibronectin](../../03-molecular/fibronectin/README.md)** — Plasma FN is cross-linked into fibrin clots → provisional scaffold for platelets, neutrophils, and fibroblasts; cellular FN from fibroblasts drives granulation tissue; FN-integrin α5β1 → fibroblast migration and myofibroblast differentiation → wound contraction and closure.
- `connects-to` → **[TGF-β](../../03-molecular/tgf-beta/README.md)** — TGF-β1 from platelets and macrophages drives myofibroblast differentiation (α-SMA+ → wound contraction), collagen I synthesis, and re-epithelialization; excess TGF-β → hypertrophic scar and keloid; TGF-β3 promotes scarless fetal healing; pirfenidone inhibits fibrogenic signaling.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — VEGF-A from keratinocytes and macrophages drives angiogenesis into the wound bed; HIF-1α (hypoxic wound center) → VEGF → new vessel formation in granulation tissue; anti-VEGF therapy impairs wound healing — a known adverse effect of bevacizumab and other anti-VEGF agents.
- `connects-to` → **[Diabetic Retinopathy](../diabetic-retinopathy/README.md)** — Diabetes impairs wound healing through AGE accumulation, pericyte dysfunction, impaired neutrophil function, and reduced HIF-1α/VEGF response; diabetic foot ulcers affect ~15% of people with diabetes and are the leading cause of non-traumatic amputation.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Macrophages orchestrate wound healing's inflammatory-to-proliferative switch: M1 cells clear debris, then become M2 cells that secrete TGF-β1, PDGF, VEGF, and IGF-1 to drive fibroblasts, angiogenesis, and re-epithelialization; a failed M1→M2 switch defines chronic wounds.
- `connects-to` → **[Fibroblast](../../04-cellular/fibroblast/README.md)** — Wound fibroblasts migrate along the fibronectin scaffold and lay down the type III collagen of granulation tissue; TGF-β1 plus tension converts them into α-SMA+ myofibroblasts that contract the wound and, failing to apoptose, produce hypertrophic scars and keloids.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — Cutaneous repair is the canonical wound-healing model — hemostasis, inflammation, proliferation, remodeling — restoring the skin barrier with a fibrotic scar rather than regeneration; chronic non-healing ulcers (diabetic, venous, pressure) carry a ~$31 billion annual US burden.
- `connects-to` → **[Platelet](../../04-cellular/platelet/README.md)** — Platelets fire the starting gun of wound healing: at injury they form the hemostatic plug and degranulate, releasing PDGF, TGF-β, and VEGF that recruit neutrophils and macrophages and prime fibroblasts — the growth-factor surge launching the inflammatory phase.
- `connects-to` → **[Collagen](../../03-molecular/collagen/README.md)** — Collagen is the structural endpoint of wound healing: fibroblasts first lay down weak type III collagen in granulation tissue, which remodeling replaces with cross-linked type I collagen regaining ~80% of tensile strength over months; dysregulated turnover yields keloids.
- `connects-to` → **[Systemic Sclerosis](../systemic-sclerosis/README.md)** — Systemic sclerosis is wound healing that never stops: the TGF-β-driven myofibroblast activation and collagen deposition that should close a wound and resolve becomes self-sustaining and widespread, scarring skin and organs — fibrosis is dysregulated persistent repair.
- `connects-to` → **[Type 2 Diabetes](../type-2-diabetes/README.md)** — Diabetes is the leading cause of chronic non-healing wounds: hyperglycemia impairs every healing phase—blunting neutrophil and macrophage function, stiffening capillaries, adding neuropathy—so diabetic foot ulcers stall and drive most non-traumatic amputations.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — Angiogenesis by endothelial cells is essential to wound healing: VEGF from the wound bed drives endothelial sprouting that forms granulation tissue's capillaries, restoring oxygen—when this fails (ischemia, diabetes), the wound cannot progress to repair.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — Wound healing is the integumentary system restoring its barrier: hemostasis, inflammation, proliferation, and remodeling rebuild epidermis and dermis after injury, but imperfectly—scar replaces the original architecture, lacking hair follicles and full strength.
- `connects-to` → **[Neutrophil](../../04-cellular/neutrophil/README.md)** — Neutrophils lead the inflammatory phase of wound healing: arriving within hours, they kill bacteria and clear debris, but their proteases also damage tissue—so timely resolution is essential, and persistent neutrophilia underlies chronic non-healing wounds.
- `connects-to` → **[PDGF](../../03-molecular/pdgf/README.md)** — PDGF is a master growth factor of wound repair: released by degranulating platelets, it recruits and activates fibroblasts and smooth muscle, driving granulation tissue and collagen deposition—and recombinant PDGF (becaplermin) treats diabetic foot ulcers.
- `connects-to` → **[Obesity](../obesity/README.md)** — Obesity impairs wound healing: poor tissue perfusion, chronic low-grade inflammation, and frequent coexisting diabetes slow each phase of repair, so obese and diabetic patients suffer more wound dehiscence, infection and chronic ulcers—a major surgical burden.

[^singer-1999-wound-healing-review]: Singer AJ, Clark RA. Cutaneous wound healing. *N Engl J Med.* 1999;341(10):738-746. [doi:10.1056/NEJM199909023411006](https://doi.org/10.1056/NEJM199909023411006) · [PubMed 10471461](https://pubmed.ncbi.nlm.nih.gov/10471461/)
[^gurtner-2008-wound-repair-regeneration]: Gurtner GC, Werner S, Barrandon Y, Longaker MT. Wound repair and regeneration. *Nature.* 2008;453(7193):314-321. [doi:10.1038/nature07039](https://doi.org/10.1038/nature07039) · [PubMed 18480812](https://pubmed.ncbi.nlm.nih.gov/18480812/)
[^eming-2014-wound-repair-mechanisms]: Eming SA, Martin P, Tomic-Canic M. Wound repair and regeneration: mechanisms, signaling, and translation. *Sci Transl Med.* 2014;6(265):265sr6. [doi:10.1126/scitranslmed.3009337](https://doi.org/10.1126/scitranslmed.3009337) · [PubMed 25473038](https://pubmed.ncbi.nlm.nih.gov/25473038/)
