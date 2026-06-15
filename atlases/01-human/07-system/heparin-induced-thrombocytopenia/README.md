---
schema: human-scale-entry/v1
id: heparin-induced-thrombocytopenia
name: Heparin-Induced Thrombocytopenia
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-08
summary: "Heparin-induced thrombocytopenia (HIT type 2) is an immune thrombocytopenia from anti-PF4/heparin IgG; platelet activation → paradoxical thrombosis. Stop heparin; switch to argatroban/bivalirudin/fondaparinux; avoid warfarin initially. 4T score guides clinical probability."
aliases: ["HIT", "heparin-induced thrombocytopenia", "HIT type 2", "HITT", "heparin thrombocytopenia", "anti-PF4 antibody", "PF4-heparin antibody", "VITT"]
sources:
  - id: warkentin-2007-hit-review
    type: peer-reviewed
    cite: "Warkentin TE, Greinacher A. Heparin-induced thrombocytopenia: recognition, treatment, and prevention: the Seventh ACCP Conference on Antithrombotic and Thrombolytic Therapy. Chest. 2004;126(3 Suppl):311S-337S."
    doi: "10.1378/chest.126.3_suppl.311S"
    pmid: "15383477"
    url: "https://doi.org/10.1378/chest.126.3_suppl.311S"
  - id: greinacher-2021-vitt-nejm
    type: peer-reviewed
    cite: "Greinacher A, Thiele T, Warkentin TE, et al. Thrombotic thrombocytopenia after ChAdOx1 nCov-19 vaccination. N Engl J Med. 2021;384(22):2092-2101."
    doi: "10.1056/NEJMoa2104840"
    pmid: "33835769"
    url: "https://doi.org/10.1056/NEJMoa2104840"
  - id: linkins-2012-hit-chest
    type: clinical-guideline
    cite: "Linkins LA, Dans AL, Moores LK, et al. Treatment and prevention of heparin-induced thrombocytopenia: Antithrombotic Therapy and Prevention of Thrombosis, 9th ed: American College of Chest Physicians Evidence-Based Clinical Practice Guidelines. Chest. 2012;141(2 Suppl):e495S-e530S."
    doi: "10.1378/chest.11-2303"
    pmid: "22315270"
    url: "https://doi.org/10.1378/chest.11-2303"
cross_links:
  - target: 01-human/03-molecular/pf4
    relation: connects-to
    note: "Anti-PF4/heparin IgG (predominantly IgG4) is the diagnostic antigen of HIT; formed when PF4-heparin complex → neo-antigen → IgG production; ELISA detects anti-PF4/heparin IgG (sensitive, ~97%; not specific); SRA (serotonin release assay) is the confirmatory gold standard."
  - target: 01-human/04-cellular/platelet
    relation: connects-to
    note: "Anti-PF4/heparin IgG crosslinks FcγRIIA on platelets → Gαq → IP3/DAG → Ca²⁺ → dense granule release (ADP, serotonin) + TXA2 → further platelet activation loop; platelet activation fragments generate procoagulant microparticles → thrombin → arterial and venous thrombosis."
  - target: 01-human/03-molecular/thrombin
    relation: connects-to
    note: "HIT causes paradoxical thrombosis: activated platelets generate procoagulant microparticles → thrombin generation; argatroban (DTI) and bivalirudin block thrombin in HIT; warfarin is contraindicated initially (protein C drops first → warfarin-induced limb gangrene risk)."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "HIT causes paradoxical DVT/PE (venous) and arterial thrombosis (HITT); occurs 5-10 days after heparin exposure; anti-PF4/heparin IgG → platelet activation → thrombin; argatroban, bivalirudin, and fondaparinux replace heparin in HIT; DOACs used for bridging to warfarin."
  - target: 01-human/03-molecular/antithrombin
    relation: connects-to
    note: "UFH and LMWH anticoagulate via AT (heparin binds AT → 1000× accelerated thrombin/FXa inhibition); AT is bypassed by direct thrombin inhibitors (argatroban, bivalirudin) used in HIT; fondaparinux (FXa inhibitor via AT) is an alternative in HIT."
  - target: 01-human/03-molecular/immunoglobulin-g
    relation: connects-to
    note: "HIT is driven by a transient IgG against the PF4-heparin complex; this antibody cross-links FcγRIIA on platelets to activate them, so detection rests on an anti-PF4/heparin IgG ELISA confirmed by a serotonin-release assay — and the IgG typically fades within 3-6 months."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "Beyond platelets, anti-PF4/heparin IgG activates endothelial cells: PF4 binds endothelial heparan sulfate, and immune-complex engagement induces tissue factor expression, amplifying thrombin generation — why HIT is so intensely prothrombotic despite falling platelet counts."
  - target: 01-human/07-system/inherited-thrombophilia
    relation: connects-to
    note: "HIT is a severe acquired thrombophilia that, unlike most inherited thrombophilias, threatens arteries as well as veins and can take limbs; co-existing inherited thrombophilia or recent VTE further raises the risk of HIT-associated thrombosis."
  - target: 01-human/07-system/pnh
    relation: connects-to
    note: "HIT and PNH are acquired, intensely prothrombotic disorders with opposite mechanisms: HIT is anti-PF4/heparin IgG activating platelets, PNH is complement-mediated hemolysis from GPI-anchor loss; both clot despite platelet consumption and need targeted therapy, not heparin alone."
  - target: 01-human/07-system/antiphospholipid-syndrome
    relation: connects-to
    note: "HIT and antiphospholipid syndrome are antibody-mediated acquired thrombophilias threatening arteries and veins: anti-PF4 IgG and antiphospholipid antibodies each activate platelets and endothelium; both can cause catastrophic multisite thrombosis and avoid reliance on heparin."
  - target: 01-human/07-system/stroke
    relation: connects-to
    note: "Unlike most thrombophilias, HIT causes arterial as well as venous thrombosis: anti-PF4/heparin immune complexes activate platelets and endothelium → arterial 'white clots' causing stroke, MI and limb ischemia; suspected HIT mandates a non-heparin anticoagulant."
  - target: 01-human/07-system/immune-thrombocytopenia
    relation: connects-to
    note: "HIT and immune thrombocytopenia are both antibody-mediated low-platelet states with opposite effects: ITP antibodies destroy platelets and bleed, while HIT's anti-PF4 antibodies activate platelets and clot—so HIT means stopping heparin, not transfusing."
  - target: 01-human/07-system/disseminated-intravascular-coagulation
    relation: connects-to
    note: "HIT and DIC both cause inpatient thrombocytopenia but differ: DIC consumes factors and platelets with prolonged PT/PTT, while HIT activates platelets via antibody with normal clotting times—4T score and anti-PF4 testing distinguish them."
  - target: 01-human/07-system/covid-19-disease
    relation: connects-to
    note: "HIT is the template for vaccine-induced thrombotic thrombocytopenia (VITT) after COVID-19 adenoviral vaccines: both feature anti-PF4 antibodies that activate platelets to cause thrombosis with thrombocytopenia, treated alike with non-heparin anticoagulation and IVIG."
  - target: 01-human/07-system/thrombotic-thrombocytopenic-purpura
    relation: connects-to
    note: "HIT and TTP are both life-threatening thrombocytopenias: HIT is antibody-mediated platelet activation by PF4-heparin complexes causing paradoxical thrombosis, while TTP is ADAMTS13 deficiency forming microthrombi—both drop platelets, but cause and treatment differ."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Complement amplifies the prothrombotic immunity of HIT: the IgG-PF4-heparin immune complexes that activate platelets also engage complement, fueling endothelial activation and thrombosis—linking an antibody reaction to heparin with the innate complement cascade."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "HIT is paradoxical—low platelets cause clots, not bleeds: PF4-heparin antibodies activate platelets and endothelium, triggering arterial and venous thrombosis across the cardiovascular system—so heparin is stopped and a non-heparin anticoagulant started."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Macrophages execute the paradox of HIT: Fc receptors on macrophages and platelets bind PF4-heparin-IgG immune complexes, clearing platelets (thrombocytopenia) while activating them to clot—so the same antibody both lowers the count and causes thrombosis."
  - target: 01-human/03-molecular/complement-c5
    relation: connects-to
    note: "Complement amplifies the thrombosis of HIT and its cousin VITT: PF4-antibody complexes activate complement on platelets and endothelium, boosting clot formation—so complement and the anti-PF4 antibody together explain why HIT clots despite a falling platelet count."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "Pulmonary embolism is a major HIT complication: the paradoxical clotting strikes veins, throwing clots to the lung, so a heparin-treated patient with a falling platelet count and new dyspnea needs heparin stopped and a non-heparin anticoagulant urgently."
  - target: 01-human/04-cellular/b-cell
    relation: connects-to
    note: "HIT is driven by B-cell antibodies: B cells rapidly make IgG against platelet-factor-4/heparin complexes, and these antibodies cross-link platelet Fc receptors to trigger the paradoxical clotting—so the culprit is a transient, T-independent antibody response."
  - target: 01-human/06-organ/spleen
    relation: connects-to
    note: "The spleen helps cause HIT's low platelet count: its macrophages clear antibody-coated platelets from the circulation, so even as clots form, platelet numbers fall—the 'thrombocytopenia with thrombosis' paradox that defines the syndrome."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "Neutrophils amplify the thrombosis of HIT: activated by anti-PF4 immune complexes, they release neutrophil extracellular traps (NETs) that provide a scaffold for clot formation—linking HIT to the same NET-driven immunothrombosis seen in VITT and severe COVID."
  - target: 01-human/03-molecular/serotonin
    relation: connects-to
    note: "The serotonin release assay confirms HIT: activated platelets dump their serotonin stores, so measuring heparin-dependent serotonin release from donor platelets is the gold-standard functional test distinguishing true HIT from harmless anti-PF4 antibodies."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "HIT can announce itself in the skin: heparin injection sites may develop painful necrotic lesions from local thrombosis, a recognized skin sign of the paradoxical clotting that defines the syndrome despite falling platelets."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "HIT's anti-PF4/heparin antibodies arise with T-helper-cell support: helper T cells license B cells to produce the pathogenic IgG, an unusually rapid immune response that can recur on heparin re-exposure."
  - target: 01-human/03-molecular/fibrinogen
    relation: connects-to
    note: "HIT is a paradoxical clotting storm consuming fibrinogen: the activated platelets generate massive thrombin that converts fibrinogen to fibrin, so a low-platelet state causes thrombosis rather than bleeding—the trap that defines the disease."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "HIT platelets activate through a calcium surge: antibody clustering of platelet Fc receptors triggers calcium influx that drives the granule release and aggregation behind the prothrombotic state—the cellular step that makes HIT dangerous."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "HIT starts when dendritic cells flag PF4-heparin as foreign: heparin reshapes platelet factor 4 into a neo-antigen these sentinels recognize and present, kicking off the rapid immune reaction that turns a blood thinner into a clotting trigger."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "HIT clots can strike the brain: despite the falling platelet count it is a prothrombotic state, causing arterial strokes and cerebral vein thrombosis, so HIT is treated with non-heparin anticoagulants rather than transfusion."
  - target: 01-human/06-organ/adrenal-gland
    relation: connects-to
    note: "HIT can destroy the adrenal glands: bilateral adrenal vein thrombosis leads to hemorrhagic infarction and acute adrenal insufficiency, a rare but catastrophic complication of the syndrome's paradoxical clotting."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "HIT chokes tissues of oxygen through thrombosis: clots in arteries and veins block blood flow, causing limb ischemia that can require amputation, so the hypoxic damage—not bleeding—is HIT's central threat."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Once HIT is suspected, imaging hunts the clots: CT and lung scans read in X-ray photons find the pulmonary emboli and limb thromboses that make the syndrome dangerous despite the low platelets."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "HIT clots arteries as well as veins: coronary thrombosis can cause a heart attack, part of the arterial thrombosis that distinguishes this paradoxical, clot-prone low-platelet state."
  - target: 01-human/03-molecular/von-willebrand-factor
    relation: connects-to
    note: "HIT inflames the vessel wall: the immune complexes activate endothelium to release von Willebrand factor, which grabs platelets and amplifies the prothrombotic storm beyond the platelets' own activation."
  - target: 01-human/05-tissue/bone-marrow
    relation: connects-to
    note: "HIT's low platelets do not come from a failing marrow: the megakaryocytes keep producing normally, but the antibody-coated platelets are consumed in clots and cleared by the spleen, a destruction rather than a production problem."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "HIT's clotting can strike the kidney: thrombosis of the renal veins or microvasculature, part of the body-wide prothrombotic storm, can cause acute kidney injury even as the platelet count falls."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy reveals HIT's trigger: heparin and platelet factor 4 assemble into large ultralarge complexes that the antibodies cross-link on the platelet surface, the molecular scaffolding that ignites the whole prothrombotic cascade."
---

# Heparin-Induced Thrombocytopenia

## Overview

**Heparin-induced thrombocytopenia (HIT)** exists in two forms:
- **Type 1 HIT** (non-immune; "heparin effect"): Direct heparin-mediated platelet sequestration; mild thrombocytopenia (<30% drop) within 1-4 days of heparin; self-limited; no treatment needed; resolves despite continued heparin
- **Type 2 HIT** (immune-mediated; the clinically dangerous form): **Anti-PF4/heparin IgG** → platelet activation → severe thrombocytopenia (>50% drop) on days 5-10 + **paradoxical thrombosis**; life- and limb-threatening [^warkentin-2007-hit-review]

**The HIT paradox:** Unlike typical thrombocytopenias where low platelets → bleeding risk, HIT causes **thrombosis** — the IgG-activated platelets are procoagulant, and the thromboembolic risk (30-50% if untreated) vastly outweighs the bleeding risk.

**Epidemiology (Type 2 HIT):**
- Incidence: ~0.5-5% with UFH; ~0.1-0.5% with LMWH; <0.01% with fondaparinux
- Highest risk: Orthopedic and cardiac surgery patients receiving UFH for ≥5 days
- Temporal pattern: Platelet drop at days 5-10 after first heparin exposure (earlier — within 24h — if re-exposed within 3 months: "rapid-onset HIT")
- Anti-PF4/heparin seroconversion: ~7-17% of exposed surgical patients; only ~1-3% develop clinical HIT
- Female sex: ~2× risk vs. male (estrogen-related immune response?)

## Structure

### The 4T Score — Pre-test clinical probability

The **4T score** (0-8 points) stratifies HIT probability before diagnostic testing:

| Criterion | 2 points | 1 point | 0 points |
|:---------|:---------|:--------|:---------|
| **T**hrombocytopenia | >50% fall + nadir ≥20×10⁹/L | 30-50% fall OR nadir 10-19×10⁹/L | <30% fall OR nadir <10×10⁹/L |
| **T**iming of platelet fall | Days 5-10 (or ≤1 day if prior heparin in past 3 months) | >10 days OR timing unclear | ≤4 days without prior heparin exposure |
| **T**hrombosis | New thrombosis; skin necrosis at injection sites; acute anaphylactic reaction after IV UFH | Progressive/recurrent thrombosis; erythematous skin lesions | None |
| Other causes of **T**hrombocytopenia | None apparent | Possible other cause | Definite other cause |

**Score interpretation:**
- 0-3 (low): <5% HIT probability → HIT very unlikely, continue heparin
- 4-5 (intermediate): ~14% probability → start alternate anticoagulation, send HIT antibody testing
- 6-8 (high): >80% probability → stop heparin immediately, start non-heparin anticoagulant, send HIT testing

**Do NOT wait for lab results to stop heparin in high-probability patients.**

### Diagnostic testing

| Test | Sensitivity | Specificity | Role |
|:-----|:-----------|:------------|:-----|
| **Anti-PF4/heparin IgG ELISA** | ~97% | ~74% | First-line screening; negative ELISA virtually excludes HIT; high optical density (OD >2.0) strongly predictive |
| **Serotonin Release Assay (SRA)** | ~95% | ~97% | Gold standard confirmatory test; measures ¹⁴C-serotonin release from washed platelets in presence of patient serum + therapeutic heparin |
| **Heparin-Induced Platelet Activation (HIPA)** | ~95% | ~98% | Functional assay; visual assessment of platelet aggregation |
| **PIFA (platelet immunofluorescence assay)** | Variable | Variable | Less standardized; not preferred |

**Testing caveat:** SRA is available only at reference labs — results may take 3-5 days. Do NOT wait for SRA to treat high-probability HIT. Act on clinical probability + ELISA.

**The IgG-specific ELISA matters:** Total Ig (IgG + IgM + IgA) ELISA has higher sensitivity but lower specificity; IgG-specific ELISA correlates better with functional (SRA-positive) HIT and thrombotic risk.

## Function

### Pathophysiological cascade

**The HIT thrombosis paradox — step by step:**

```
Heparin (UFH/LMWH) administration
        ↓
PF4 released from platelet alpha-granules → binds heparin
        ↓
PF4-heparin complex → neo-antigen exposed on PF4
        ↓  (days 5-14: IgG production)
Anti-PF4/heparin IgG (predominantly IgG4)
        ↓
IgG-PF4-heparin → FcγRIIA (CD32a) on platelets
        ↓
Gαq → IP₃/DAG → Ca²⁺ flux
        ↓
Dense granule release: ADP, serotonin, PF4
TXA₂ synthesis (COX-1 → thromboxane A₂)
        ↓
Platelet activation loop: more PF4 → more complex → more IgG crosslinking
        ↓
Platelet microparticles (PS-exposing) → phospholipid surface for coagulation
        ↓
Prothrombin → THROMBIN → fibrin clot + platelet recruitment
        ↓
Arterial thrombi (limb, coronary, cerebral) + venous thrombi (DVT/PE, CVST)
  SIMULTANEOUSLY with
Platelet consumption → thrombocytopenia (paradox: clotting despite low platelets)
```

**Key consequence:** HIT can cause **any thrombotic event** — DVT/PE most common (HITT = HIT + thrombosis), but also arterial limb ischemia (often requiring amputation), MI, ischemic stroke, mesenteric ischemia, adrenal hemorrhage/necrosis (adrenal vein thrombosis).

### HIT without thrombosis vs. HITT

- **HIT without thrombosis:** Positive antibody + thrombocytopenia alone; thrombotic risk ~30% over next 30 days without treatment
- **HITT (HIT + Thrombosis):** ~50% of HIT cases; treatment urgency even higher; higher mortality (~5-10%) and amputation risk

## Pathology

### Acute treatment [^linkins-2012-hit-chest]

**Immediate (high-priority) actions:**
1. **STOP all heparin** — including heparin flushes, LMWH, heparin-coated catheters, heparin in TPN; heparin-bonded lines
2. **Start non-heparin anticoagulation IMMEDIATELY** — do not wait for lab confirmation in high-probability patients
3. **Do NOT give platelet transfusions** — adds "fuel to the fire" (more PF4 released) → may worsen thrombosis
4. **Do NOT start warfarin until platelets recover** (>150×10⁹/L) — warfarin-induced limb gangrene from protein C deficiency

**Non-heparin anticoagulants (choose based on clinical context):**

| Drug | Class | MOA | Half-life | Clearance | Monitoring | Notes |
|:-----|:------|:----|:----------|:----------|:-----------|:------|
| **Argatroban** (preferred) | Direct thrombin inhibitor | Reversible active-site DTI | ~45 min | Hepatic (safe in renal failure) | aPTT target 1.5-3× baseline | Falsely prolongs INR — challenge when bridging to warfarin |
| **Bivalirudin** | Direct thrombin inhibitor | Bivalent reversible DTI | ~25 min | 80% enzymatic (plasma); 20% renal | aPTT or ACT | Short half-life → useful in procedural settings (PCI, CABG) |
| **Fondaparinux** | Factor Xa inhibitor (indirect) | Anti-Xa via antithrombin | ~17-21 h | Renal (contraindicated CrCl <30) | Anti-Xa level (optional) | Very low HIT risk; not FDA-approved for HIT but widely used off-label |
| **Danaparoid** | Heparanoid (anti-Xa) | Inhibits Xa via antithrombin | ~24 h | Renal | Anti-Xa level | FDA-approved for HIT in Europe; ~5% cross-reactivity with HIT antibodies; monitor |
| **DOACs (rivaroxaban, apixaban)** | FXa inhibitors | Direct oral anti-Xa | 8-12 h | Renal + hepatic | Anti-Xa assay | Increasing use after acute phase; rivaroxaban has most HIT evidence (SWITCH study) |

**Transitioning to warfarin:**
- Wait until platelets recover to >150×10⁹/L before starting warfarin
- Overlap warfarin with non-heparin anticoagulant for ≥5 days AND until INR ≥2.0 for ≥2 consecutive days
- **Reason:** Warfarin drops protein C first (shortest half-life among vitamin K–dependent factors → 8h) → transient hypercoagulable state → warfarin-induced limb gangrene (venous limb gangrene) in HIT patients with already-thrombosed veins

**Duration:** At least 3 months anticoagulation for HITT; at least 1 month for HIT without thrombosis.

### Prevention and future heparin exposure

- **HIT antibodies typically become undetectable within 3-6 months** (IgG half-life)
- **Future heparin exposure after HIT:**
  - If SRA-negative and >3-6 months since prior HIT: brief re-exposure may be acceptable in life-saving situations (e.g., cardiac bypass) under monitoring
  - If SRA-positive: absolute avoidance of all heparin; use alternative anticoagulants; bivalirudin for cardiac bypass procedures
- **Document allergy in medical records:** Alert patient, future providers

### VITT (Vaccine-Induced Immune Thrombocytopenia with Thrombosis) [^greinacher-2021-vitt-nejm]

**Key differences from classic HIT:**
- Triggered by adenoviral vector COVID-19 vaccines (ChAdOx1, Ad26.COV2.S), NOT by heparin
- Anti-PF4 antibodies form without heparin — bind PF4 directly
- Onset: 4-28 days after vaccination
- Characteristic thromboses: CVST (cerebral venous sinus thrombosis), splanchnic vein thrombosis (portal, mesenteric), adrenal vein thrombosis — unusual sites
- Platelet count may be severely low (<30×10⁹/L); D-dimer markedly elevated

**VITT diagnosis:** Thrombocytopenia + unusual thrombosis + positive anti-PF4 antibody (ELISA or SRA) in appropriate post-vaccination time window; heparin NOT required

**VITT treatment:**
1. **High-dose IVIG (1 g/kg × 2 days):** Saturates FcγR on platelets + monocytes; provides anti-idiotypic antibodies → reduces platelet activation
2. **Non-heparin anticoagulation:** Fondaparinux, argatroban, or DOACs; **avoid heparin** (may worsen VITT by forming PF4-heparin-IgG triple complex)
3. **Avoid platelet transfusion** (worsens thrombosis)
4. **Avoid warfarin initially** (same protein C rationale as HIT)
5. **Corticosteroids:** Considered in refractory VITT

## Connections

- `connects-to` → **[PF4](../../03-molecular/pf4/README.md)** — Anti-PF4/heparin IgG (predominantly IgG4) is the diagnostic antigen of HIT; formed when PF4-heparin complex → neo-antigen → IgG production; ELISA detects anti-PF4/heparin IgG (sensitive, ~97%; not specific); SRA (serotonin release assay) is the confirmatory gold standard.
- `connects-to` → **[Platelet](../../04-cellular/platelet/README.md)** — Anti-PF4/heparin IgG crosslinks FcγRIIA on platelets → Gαq → IP3/DAG → Ca²⁺ → dense granule release (ADP, serotonin) + TXA2 → further platelet activation loop; platelet activation fragments generate procoagulant microparticles → thrombin → arterial and venous thrombosis.
- `connects-to` → **[Thrombin](../../03-molecular/thrombin/README.md)** — HIT causes paradoxical thrombosis: activated platelets generate procoagulant microparticles → thrombin generation; argatroban (DTI) and bivalirudin block thrombin in HIT; warfarin is contraindicated initially (protein C drops first → warfarin-induced limb gangrene risk).
- `connects-to` → **[Venous Thromboembolism](../venous-thromboembolism/README.md)** — HIT causes paradoxical DVT/PE (venous) and arterial thrombosis (HITT); occurs 5-10 days after heparin exposure; anti-PF4/heparin IgG → platelet activation → thrombin; argatroban, bivalirudin, and fondaparinux replace heparin in HIT; DOACs used for bridging to warfarin.
- `connects-to` → **[Antithrombin](../../03-molecular/antithrombin/README.md)** — UFH and LMWH anticoagulate via AT (heparin binds AT → 1000× accelerated thrombin/FXa inhibition); AT is bypassed by direct thrombin inhibitors (argatroban, bivalirudin) used in HIT; fondaparinux (FXa inhibitor via AT) is an alternative in HIT.
- `connects-to` → **[Immunoglobulin G](../../03-molecular/immunoglobulin-g/README.md)** — HIT is driven by a transient IgG against the PF4-heparin complex; this antibody cross-links FcγRIIA on platelets to activate them, so detection rests on an anti-PF4/heparin IgG ELISA confirmed by a serotonin-release assay — and the IgG typically fades within 3-6 months.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — Beyond platelets, anti-PF4/heparin IgG activates endothelial cells: PF4 binds endothelial heparan sulfate, and immune-complex engagement induces tissue factor expression, amplifying thrombin generation — why HIT is so intensely prothrombotic despite falling platelet counts.
- `connects-to` → **[Inherited Thrombophilia](../inherited-thrombophilia/README.md)** — HIT is a severe acquired thrombophilia that, unlike most inherited thrombophilias, threatens arteries as well as veins and can take limbs; co-existing inherited thrombophilia or recent VTE further raises the risk of HIT-associated thrombosis.
- `connects-to` → **[Paroxysmal Nocturnal Hemoglobinuria](../pnh/README.md)** — HIT and PNH are acquired, intensely prothrombotic disorders with opposite mechanisms: HIT is anti-PF4/heparin IgG activating platelets, PNH is complement-mediated hemolysis from GPI-anchor loss; both clot despite platelet consumption and need targeted therapy, not heparin alone.
- `connects-to` → **[Antiphospholipid Syndrome](../antiphospholipid-syndrome/README.md)** — HIT and antiphospholipid syndrome are antibody-mediated acquired thrombophilias threatening arteries and veins: anti-PF4 IgG and antiphospholipid antibodies each activate platelets and endothelium; both can cause catastrophic multisite thrombosis and avoid reliance on heparin.
- `connects-to` → **[Stroke](../stroke/README.md)** — Unlike most thrombophilias, HIT causes arterial as well as venous thrombosis: anti-PF4/heparin immune complexes activate platelets and endothelium → arterial 'white clots' causing stroke, MI and limb ischemia; suspected HIT mandates a non-heparin anticoagulant.
- `connects-to` → **[Immune Thrombocytopenia](../immune-thrombocytopenia/README.md)** — HIT and immune thrombocytopenia are both antibody-mediated low-platelet states with opposite effects: ITP antibodies destroy platelets and bleed, while HIT's anti-PF4 antibodies activate platelets and clot—so HIT means stopping heparin, not transfusing.
- `connects-to` → **[Disseminated Intravascular Coagulation](../disseminated-intravascular-coagulation/README.md)** — HIT and DIC both cause inpatient thrombocytopenia but differ: DIC consumes factors and platelets with prolonged PT/PTT, while HIT activates platelets via antibody with normal clotting times—4T score and anti-PF4 testing distinguish them.
- `connects-to` → **[COVID-19 Disease](../covid-19-disease/README.md)** — HIT is the template for vaccine-induced thrombotic thrombocytopenia (VITT) after COVID-19 adenoviral vaccines: both feature anti-PF4 antibodies that activate platelets to cause thrombosis with thrombocytopenia, treated alike with non-heparin anticoagulation and IVIG.
- `connects-to` → **[Thrombotic Thrombocytopenic Purpura](../thrombotic-thrombocytopenic-purpura/README.md)** — HIT and TTP are both life-threatening thrombocytopenias: HIT is antibody-mediated platelet activation by PF4-heparin complexes causing paradoxical thrombosis, while TTP is ADAMTS13 deficiency forming microthrombi—both drop platelets, but cause and treatment differ.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Complement amplifies the prothrombotic immunity of HIT: the IgG-PF4-heparin immune complexes that activate platelets also engage complement, fueling endothelial activation and thrombosis—linking an antibody reaction to heparin with the innate complement cascade.
- `connects-to` → **[Cardiovascular System](../cardiovascular-system/README.md)** — HIT is paradoxical—low platelets cause clots, not bleeds: PF4-heparin antibodies activate platelets and endothelium, triggering arterial and venous thrombosis across the cardiovascular system—so heparin is stopped and a non-heparin anticoagulant started.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Macrophages execute the paradox of HIT: Fc receptors on macrophages and platelets bind PF4-heparin-IgG immune complexes, clearing platelets (thrombocytopenia) while activating them to clot—so the same antibody both lowers the count and causes thrombosis.
- `connects-to` → **[Complement C5](../../03-molecular/complement-c5/README.md)** — Complement amplifies the thrombosis of HIT and its cousin VITT: PF4-antibody complexes activate complement on platelets and endothelium, boosting clot formation—so complement and the anti-PF4 antibody together explain why HIT clots despite a falling platelet count.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — Pulmonary embolism is a major HIT complication: the paradoxical clotting strikes veins, throwing clots to the lung, so a heparin-treated patient with a falling platelet count and new dyspnea needs heparin stopped and a non-heparin anticoagulant urgently.
- `connects-to` → **[B Cell](../../04-cellular/b-cell/README.md)** — HIT is driven by B-cell antibodies: B cells rapidly make IgG against platelet-factor-4/heparin complexes, and these antibodies cross-link platelet Fc receptors to trigger the paradoxical clotting—so the culprit is a transient, T-independent antibody response.
- `connects-to` → **[Spleen](../../06-organ/spleen/README.md)** — The spleen helps cause HIT's low platelet count: its macrophages clear antibody-coated platelets from the circulation, so even as clots form, platelet numbers fall—the 'thrombocytopenia with thrombosis' paradox that defines the syndrome.
- `connects-to` → **[Neutrophil](../../04-cellular/neutrophil/README.md)** — Neutrophils amplify the thrombosis of HIT: activated by anti-PF4 immune complexes, they release neutrophil extracellular traps (NETs) that provide a scaffold for clot formation—linking HIT to the same NET-driven immunothrombosis seen in VITT and severe COVID.
- `connects-to` → **[Serotonin](../../03-molecular/serotonin/README.md)** — The serotonin release assay confirms HIT: activated platelets dump their serotonin stores, so measuring heparin-dependent serotonin release from donor platelets is the gold-standard functional test distinguishing true HIT from harmless anti-PF4 antibodies.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — HIT can announce itself in the skin: heparin injection sites may develop painful necrotic lesions from local thrombosis, a recognized skin sign of the paradoxical clotting that defines the syndrome despite falling platelets.
- `connects-to` → **[T Helper Cell](../../04-cellular/t-helper-cell/README.md)** — HIT's anti-PF4/heparin antibodies arise with T-helper-cell support: helper T cells license B cells to produce the pathogenic IgG, an unusually rapid immune response that can recur on heparin re-exposure.
- `connects-to` → **[Fibrinogen](../../03-molecular/fibrinogen/README.md)** — HIT is a paradoxical clotting storm consuming fibrinogen: the activated platelets generate massive thrombin that converts fibrinogen to fibrin, so a low-platelet state causes thrombosis rather than bleeding—the trap that defines the disease.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — HIT platelets activate through a calcium surge: antibody clustering of platelet Fc receptors triggers calcium influx that drives the granule release and aggregation behind the prothrombotic state—the cellular step that makes HIT dangerous.
- `connects-to` → **[Dendritic Cell](../../04-cellular/dendritic-cell/README.md)** — HIT starts when dendritic cells flag PF4-heparin as foreign: heparin reshapes platelet factor 4 into a neo-antigen these sentinels recognize and present, kicking off the rapid immune reaction that turns a blood thinner into a clotting trigger.
- `connects-to` → **[Brain](../../06-organ/brain/README.md)** — HIT clots can strike the brain: despite the falling platelet count it is a prothrombotic state, causing arterial strokes and cerebral vein thrombosis, so HIT is treated with non-heparin anticoagulants rather than transfusion.
- `connects-to` → **[Adrenal Gland](../../06-organ/adrenal-gland/README.md)** — HIT can destroy the adrenal glands: bilateral adrenal vein thrombosis leads to hemorrhagic infarction and acute adrenal insufficiency, a rare but catastrophic complication of the syndrome's paradoxical clotting.
- `connects-to` → **[Oxygen](../../02-atomic/oxygen/README.md)** — HIT chokes tissues of oxygen through thrombosis: clots in arteries and veins block blood flow, causing limb ischemia that can require amputation, so the hypoxic damage—not bleeding—is HIT's central threat.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Once HIT is suspected, imaging hunts the clots: CT and lung scans read in X-ray photons find the pulmonary emboli and limb thromboses that make the syndrome dangerous despite the low platelets.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — HIT clots arteries as well as veins: coronary thrombosis can cause a heart attack, part of the arterial thrombosis that distinguishes this paradoxical, clot-prone low-platelet state.
- `connects-to` → **[Von Willebrand Factor](../../03-molecular/von-willebrand-factor/README.md)** — HIT inflames the vessel wall: the immune complexes activate endothelium to release von Willebrand factor, which grabs platelets and amplifies the prothrombotic storm beyond the platelets' own activation.
- `connects-to` → **[Bone Marrow](../../05-tissue/bone-marrow/README.md)** — HIT's low platelets do not come from a failing marrow: the megakaryocytes keep producing normally, but the antibody-coated platelets are consumed in clots and cleared by the spleen, a destruction rather than a production problem.
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — HIT's clotting can strike the kidney: thrombosis of the renal veins or microvasculature, part of the body-wide prothrombotic storm, can cause acute kidney injury even as the platelet count falls.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy reveals HIT's trigger: heparin and platelet factor 4 assemble into large ultralarge complexes that the antibodies cross-link on the platelet surface, the molecular scaffolding that ignites the whole prothrombotic cascade.

[^warkentin-2007-hit-review]: Warkentin TE, Greinacher A. Heparin-induced thrombocytopenia: recognition, treatment, and prevention. *Chest.* 2004;126(3 Suppl):311S-337S. [doi:10.1378/chest.126.3_suppl.311S](https://doi.org/10.1378/chest.126.3_suppl.311S) · [PubMed 15383477](https://pubmed.ncbi.nlm.nih.gov/15383477/)
[^greinacher-2021-vitt-nejm]: Greinacher A, Thiele T, Warkentin TE, et al. Thrombotic thrombocytopenia after ChAdOx1 nCov-19 vaccination. *N Engl J Med.* 2021;384(22):2092-2101. [doi:10.1056/NEJMoa2104840](https://doi.org/10.1056/NEJMoa2104840) · [PubMed 33835769](https://pubmed.ncbi.nlm.nih.gov/33835769/)
[^linkins-2012-hit-chest]: Linkins LA, Dans AL, Moores LK, et al. Treatment and prevention of heparin-induced thrombocytopenia: ACCP 9th ed. Guidelines. *Chest.* 2012;141(2 Suppl):e495S-e530S. [doi:10.1378/chest.11-2303](https://doi.org/10.1378/chest.11-2303) · [PubMed 22315270](https://pubmed.ncbi.nlm.nih.gov/22315270/)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
