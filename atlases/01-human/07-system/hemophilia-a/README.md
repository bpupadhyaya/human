---
schema: human-scale-entry/v1
id: hemophilia-a
name: Hemophilia A
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-07
summary: "Hemophilia A is X-linked FVIII deficiency (F8 gene; Xq28); severe <1 IU/dL → joint/muscle hemorrhage. Emicizumab (bispecific FIXa/FX mAb; HAVEN-3: ABR 0.3 vs 22.9; FDA 2017) replaced prophylactic FVIII as standard of care in inhibitor and non-inhibitor severe HA."
aliases: ["hemophilia A", "HA", "factor VIII deficiency", "FVIII deficiency", "hemophilia A with inhibitors", "haemophilia A", "congenital FVIII deficiency"]
sources:
  - id: oldenburg-2017-emicizumab-haven1
    type: peer-reviewed
    cite: "Oldenburg J, Mahlangu JN, Kim B, et al. Emicizumab prophylaxis in hemophilia A with inhibitors. N Engl J Med. 2017;377(9):809-818."
    doi: "10.1056/NEJMoa1703068"
    pmid: "28691557"
    url: "https://doi.org/10.1056/NEJMoa1703068"
  - id: mahlangu-2018-emicizumab-haven3
    type: peer-reviewed
    cite: "Mahlangu J, Oldenburg J, Paz-Priel I, et al. Emicizumab prophylaxis in patients who have hemophilia A without inhibitors. N Engl J Med. 2018;379(9):811-822."
    doi: "10.1056/NEJMoa1803550"
    pmid: "30157389"
    url: "https://doi.org/10.1056/NEJMoa1803550"
  - id: pipe-2023-fitusiran-atlas
    type: peer-reviewed
    cite: "Pipe SW, Leebeek FW, Recht M, et al. Once-monthly subcutaneous fitusiran versus on-demand bypassing agent for haemophilia A or B with inhibitors (ATLAS-INH): a multicentre, open-label, randomised phase 3 trial. Lancet. 2023;401(10386):1427-1439."
    doi: "10.1016/S0140-6736(23)00284-2"
    pmid: "37003297"
    url: "https://doi.org/10.1016/S0140-6736(23)00284-2"
cross_links:
  - target: 01-human/03-molecular/von-willebrand-factor
    relation: connects-to
    note: "VWF binds and protects FVIII in plasma → t½ ~12 h (VWF-bound) vs. ~2 h (free); VWF deficiency in VWD type 3 → secondary FVIII <10 IU/dL (resembles mild hemophilia A); VWD type 2N: FVIII-binding domain mutations → FVIII deficiency with normal VWF antigen levels."
  - target: 01-human/03-molecular/immunoglobulin-g
    relation: connects-to
    note: "Anti-FVIII inhibitor antibodies are predominantly IgG4 (non-complement-fixing); IgG4 neutralizes FVIII infused as replacement therapy; inhibitor titer (Bethesda units) determines immune tolerance induction strategy; emicizumab bypasses FVIII → effective despite IgG4 inhibitors."
  - target: 01-human/03-molecular/thrombin
    relation: connects-to
    note: "Thrombin cleaves FVIII at Arg372/Arg740/Arg1689 → generates FVIIIa cofactor for intrinsic tenase; APC (thrombomodulin-thrombin product) cleaves FVIIIa at Arg336/Arg562 → inactivation; in HA, extrinsic-pathway thrombin is intact but amplification (intrinsic tenase) fails."
  - target: 01-human/03-molecular/protein-c
    relation: connects-to
    note: "APC inactivates FVIIIa by cleavage at Arg336 and Arg562; APC + protein S → efficient FVIIIa proteolysis → limits thrombin amplification; FV Leiden co-inheritance with mild HA creates a clinical paradox — APC resistance partially counteracts the hemophilic bleeding tendency."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "Severe HA (FVIII <1%) confers significant VTE protection; historical VTE rate in HA ~0.5/1000 PY vs. ~1.5-3/1000 general population; emicizumab reconstitutes intrinsic tenase; avoid high-dose APCC with emicizumab → TMA; gene therapy raising FVIII >150% increases VTE risk."
  - target: 01-human/04-cellular/hepatocyte
    relation: connects-to
    note: "Gene therapy for hemophilia A delivers an AAV-packaged F8 transgene to hepatocytes, which then secrete factor VIII; valoctocogene roxaparvovec raised FVIII toward normal, but expression wanes ~50%/year as episomal AAV DNA dilutes with hepatocyte turnover."
  - target: 01-human/03-molecular/antithrombin
    relation: connects-to
    note: "Fitusiran flips hemophilia A treatment around: instead of replacing factor VIII, this siRNA lowers antithrombin to rebalance hemostasis and restore clotting in FVIII- or FIX-deficient patients, including those with inhibitors; overcorrection risks thrombosis."
  - target: 01-human/07-system/inherited-thrombophilia
    relation: connects-to
    note: "Hemophilia A and inherited thrombophilia are mirror images — too little clotting versus too much; strikingly, co-inheriting factor V Leiden can soften a hemophiliac's bleeding because APC resistance keeps FVa active longer, compensating for the missing factor VIII amplification."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "Recurrent hemarthrosis is the defining morbidity of hemophilia A: bleeding into knees, ankles and elbows triggers synovitis, cartilage loss and destructive 'hemophilic arthropathy' → chronic pain and disability; prophylaxis and emicizumab aim to prevent these joint bleeds."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "Factor VIII is synthesized largely by liver sinusoidal endothelial cells and circulates protected by endothelial von Willebrand factor; injury exposing the subendothelial matrix starts hemostasis—context for FVIII deficiency, and a target for hemophilia gene therapy."
  - target: 01-human/04-cellular/platelet
    relation: connects-to
    note: "Hemophilia A spares primary hemostasis—platelets still form the plug—but lacks the FVIIIa/FIXa 'tenase' complex that assembles on the activated platelet surface to burst-generate thrombin; without it the plug is unstable and rebleeds, hence delayed deep-tissue and joint bleeding."
  - target: 01-human/07-system/disseminated-intravascular-coagulation
    relation: connects-to
    note: "Hemophilia A and DIC cause bleeding by opposite mechanisms: hemophilia is isolated factor VIII deficiency (long aPTT, normal PT and platelets) bleeding into joints, while DIC consumes all factors and platelets at once—the lab pattern tells inherited from acquired."
  - target: 01-human/07-system/immune-thrombocytopenia
    relation: connects-to
    note: "Hemophilia A and immune thrombocytopenia bleed by different mechanisms: hemophilia is a factor VIII deficit causing deep joint and muscle bleeds, while ITP is platelet destruction causing mucocutaneous petechiae—the pattern hints which arm of hemostasis failed."
  - target: 01-human/07-system/thrombotic-thrombocytopenic-purpura
    relation: connects-to
    note: "Hemophilia A and TTP sit at opposite poles of hemostasis: hemophilia fails to clot from factor VIII deficiency and bleeds, while TTP clots pathologically from ADAMTS13 deficiency, consuming platelets in microthrombi—both too little and too much clotting cause disease."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "The liver is central to hemophilia A: hepatocytes make clotting factors, and liver-directed gene therapy now delivers a working factor VIII gene to hepatocytes, enabling them to produce the missing factor—turning the factor-making organ into the cure."
  - target: 01-human/07-system/stroke
    relation: connects-to
    note: "Intracranial hemorrhage is the most feared bleed in hemophilia A: deficient factor VIII can't stabilize clots, so brain bleeding is a leading cause of death—hemorrhagic stroke here is the mirror image of the ischemic stroke that clotting disorders cause."
  - target: 01-human/07-system/antiphospholipid-syndrome
    relation: connects-to
    note: "Hemophilia A and antiphospholipid syndrome are mirror-image coagulation disorders—bleeding versus clotting: hemophilia lacks factor VIII, while APS has thrombosis-driving antiphospholipid antibodies; an acquired factor VIII inhibitor rarely bridges them."
  - target: 01-human/03-molecular/fibrinogen
    relation: connects-to
    note: "Hemophilia A spares fibrinogen but fails to reach it: factor VIII deficiency cripples the intrinsic pathway's thrombin burst, so although fibrinogen is normal, too little thrombin forms to convert it to a stable fibrin clot—hence delayed, recurrent bleeding."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "Intracranial hemorrhage is the most feared hemophilia A complication: minor head trauma can cause life-threatening brain bleeding because clot formation is delayed, so prophylactic factor replacement and urgent dosing after head injury are central to care."
  - target: 01-human/07-system/hepatitis-c
    relation: connects-to
    note: "Hemophilia A is historically tied to hepatitis C and HIV: before viral screening, pooled factor concentrates infected most treated patients with HCV and HIV—a tragedy that drove recombinant factor development, so older hemophiliacs carry a heavy chronic-viral burden."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "Hemophilia A is X-linked: the factor VIII gene sits on the X chromosome, so it overwhelmingly affects males while carrier mothers pass it on—making family history, carrier testing, and genetic counseling central to the reproductive side of the disease."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "The immune system is hemophilia A's biggest treatment hurdle: some patients form neutralizing antibodies (inhibitors) against infused factor VIII, making replacement fail—so immune tolerance regimens and inhibitor-bypassing agents like emicizumab are needed."
  - target: 01-human/04-cellular/erythrocyte
    relation: connects-to
    note: "Bleeding in hemophilia A drains red cells: recurrent joint and muscle bleeds, plus dangerous internal hemorrhage, cause iron-deficiency or acute anemia, so falling hemoglobin and the need for transfusion track the severity of uncontrolled bleeding."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Calcium is the silent partner of the clotting cascade hemophilia disrupts: as coagulation Factor IV, calcium ions are needed to assemble the tenase and prothrombinase complexes—so clotting depends on calcium, and citrate that binds it blocks coagulation in stored blood."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "The feared complication of hemophilia A is inhibitors, driven by T-helper cells: in some patients, helper T cells license B cells to make anti-Factor-VIII antibodies that neutralize replacement therapy, forcing bypassing agents or immune tolerance induction."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Repeated joint bleeds in hemophilia damage joints through macrophages: blood in the joint loads synovial macrophages with iron, driving inflammatory synovitis that erodes cartilage—the hemophilic arthropathy that prophylactic factor aims to prevent."
  - target: 01-human/03-molecular/collagen
    relation: connects-to
    note: "Hemophilia A forms the collagen-triggered platelet plug but can't stabilize it: exposed collagen still recruits platelets into an initial plug, but without factor VIII the secondary fibrin clot never reinforces it, so bleeding restarts hours later."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: connects-to
    note: "Hemophilia A's worst complication is immune, needing regulatory T cells: about a third of severe patients make anti-factor-VIII antibodies (inhibitors), and immune tolerance induction works to restore the Tregs that should accept the infused factor."
  - target: 01-human/04-cellular/b-cell
    relation: connects-to
    note: "Hemophilia A's inhibitors come from B cells: in patients who make anti-factor-VIII antibodies, B cells produce the neutralizing IgG that defeats replacement therapy—so B-cell-depleting rituximab is used to help eradicate stubborn inhibitors."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Hemophilia's joint bleeds leave iron behind: blood pooling in a joint deposits iron as hemosiderin that inflames the synovium and erodes cartilage, driving the crippling hemophilic arthropathy—and repeated bleeds also cause iron-loss anemia."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "Hemophilia often bleeds into the urinary tract: painless hematuria is common, and clots can obstruct the ureter, so kidney and bladder bleeding is a recognized, usually self-limited feature managed cautiously to avoid clot retention."
  - target: 01-human/06-organ/large-intestine
    relation: connects-to
    note: "Hemophilia can bleed dangerously into the gut: gastrointestinal hemorrhage, sometimes massive, is a serious complication, so dark or bloody stools in a hemophiliac demand urgent factor replacement and evaluation."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Imaging tracks hemophilia's joint damage: X-ray and MRI photons reveal the arthropathy from repeated bleeds, and radiosynovectomy uses radiation to quiet a chronically bleeding joint."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "Hemophilia shows on the skin: easy bruising and large, deep hematomas are often the first sign in a toddler learning to walk, hinting at the clotting defect beneath the surface."
  - target: 01-human/05-tissue/bone-marrow
    relation: connects-to
    note: "Chronic bleeding taxes the marrow: ongoing blood and iron loss in hemophilia push the bone marrow to ramp up red-cell production to keep pace, and anemia results when the losses outstrip it."
  - target: 01-human/07-system/hiv-aids
    relation: connects-to
    note: "Hemophilia carries a tragic medical legacy: before viral screening and recombinant factor, the pooled plasma concentrates that treated it infected a large share of patients with HIV and hepatitis C, a catastrophe that reshaped blood-product safety."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy shows why hemophilia's clots fail: lacking factor VIII to drive thrombin, the fibrin mesh forms with fewer, thinner, loosely woven fibers, a fragile structure that cannot hold against ongoing bleeding."
  - target: 01-human/06-organ/eye
    relation: connects-to
    note: "Bleeding into the eye threatens sight in hemophilia: spontaneous or traumatic intraocular and retinal hemorrhages, like bleeds into other closed spaces, can raise pressure and damage vision if not promptly treated with factor replacement."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "Hemophilia's bleeds can crush nerves: a deep muscle bleed — the classic iliopsoas hematoma — compresses the femoral nerve into palsy, while an intracranial hemorrhage destroys neurons directly, the most feared complication."
  - target: 01-human/04-cellular/osteoblast
    relation: connects-to
    note: "Hemophilia quietly weakens the skeleton: recurrent joint bleeds destroy cartilage and bone, and reduced activity plus chronic inflammation tip the osteoblast-osteoclast balance toward the low bone density common in these patients."
  - target: 01-human/04-cellular/smooth-muscle-cell
    relation: connects-to
    note: "Why hemophilia bleeds late, not instantly: the first response to injury — reflex constriction of the vessel's smooth muscle and the platelet plug — is intact, so small cuts seal, but the missing factor VIII fails the later step, letting deep bleeds well up hours afterward."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "Antibodies are hemophilia's nemesis and its newest cure: inhibitor alloantibodies against infused factor VIII are the dreaded complication that neutralizes treatment, while emicizumab, a bispecific antibody bridging factors IXa and X, now prevents bleeds without it."
  - target: 01-human/05-tissue/peripheral-nerve
    relation: connects-to
    note: "A deep bleed can crush a nerve: a tense hematoma in the iliopsoas or forearm compresses the peripheral nerve running through it, causing a compartment syndrome with numbness, weakness, and palsy that needs urgent factor replacement."
  - target: 01-human/07-system/hepatitis-b
    relation: connects-to
    note: "The old treatment carried hidden viruses: before viral inactivation, plasma-derived factor VIII concentrates transmitted hepatitis B and C and HIV to a generation of patients, a tragedy that drove the shift to recombinant factor and vaccination."
---

# Hemophilia A

## Overview

**Hemophilia A (HA)** is an **X-linked recessive bleeding disorder** caused by deficiency or dysfunction of **coagulation factor VIII (FVIII)**, encoded by the *F8* gene on chromosome Xq28 [^oldenburg-2017-emicizumab-haven1]. FVIII is the essential cofactor for factor IXa (FIXa) in the **intrinsic tenase complex** (FIXa + FVIIIa + Ca²⁺ + phospholipid → activates factor X → thrombin generation → fibrin clot); without adequate FVIII, the coagulation cascade is severely impaired.

Hemophilia A is the **most common severe hereditary bleeding disorder**, affecting ~1 in 5,000-10,000 male births. Females are typically carriers (heterozygous; may have mild bleeding due to lyonization) or rarely have clinically significant disease (compound heterozygous; Turner syndrome).

**Severity classification:**

| Severity | FVIII level | Clinical phenotype |
|:---------|:-----------|:-------------------|
| Severe | <1 IU/dL (<1% normal) | Spontaneous joint/muscle hemorrhage; hemarthroses without provocation; life-threatening bleeds |
| Moderate | 1-5 IU/dL | Bleeds with minor trauma; rare spontaneous bleeds; occasional hemarthrosis |
| Mild | 5-40 IU/dL | Bleeds only with significant trauma/surgery; often undiagnosed until adult life |

**Inhibitor development:** The most serious complication of hemophilia A treatment; anti-FVIII IgG4 antibodies develop in ~25-30% of severe HA patients after FVIII exposure (typically within the first 50 exposure days). Inhibitors neutralize replacement FVIII, making standard therapy ineffective. Inhibitor titer is measured in Bethesda units (BU): high-titer inhibitors >5 BU require bypassing agents or immune tolerance induction (ITI).

**Revolutionary shift — emicizumab era:** Since the HAVEN-1 and HAVEN-3 trials (2017-2018), **emicizumab** (Hemlibra; Roche/Genentech) — a bispecific antibody bridging FIXa and FX — has replaced prophylactic FVIII infusions as the standard of care for most patients with severe HA (with or without inhibitors), reducing the treatment burden from frequent IV infusions to weekly/biweekly/monthly SC injections.

## Structure

### F8 gene and FVIII protein

| Feature | Detail |
|:--------|:-------|
| Gene | *F8*, chromosome Xq28; 186 kb, 26 exons — one of the largest genes in the human genome |
| mRNA | 9 kb; alternative splicing of exon 16 generates B-domain variants |
| FVIII protein | 2332 aa; domain structure: A1-A2-B-A3-C1-C2 (6 domains) |
| A domains (A1, A2, A3) | Copper-binding TRP domains; thrombin cleavage sites (Arg372, Arg740, Arg1689); FIXa binding (A2) and FX binding (A2, A3) |
| B domain | Heavily glycosylated (~100 kDa); no known cofactor function; removed during FVIII activation; absent in recombinant B-domain-deleted FVIII (rFVIIIBDD) products |
| C1-C2 domains (light chain) | Phospholipid membrane binding (C2: GRP48/phosphatidylserine); VWF binding (C1, C2) |
| Active form (FVIIIa) | Thrombin cleaves FVIII at Arg372/Arg740/Arg1689 → releases B domain → A1/A2/A3-C1-C2 trimer → FVIIIa cofactor; FVIIIa is unstable → rapid inactivation by APC/protein S or spontaneous A2 domain dissociation |

### Common F8 mutations

| Mutation type | Frequency | Severity |
|:-------------|:---------|:---------|
| Intron 22 inversion (inv22) | ~40-50% of severe HA | Severe |
| Intron 1 inversion (inv1) | ~5% of severe HA | Severe |
| Large deletions | ~5-10% | Severe; high inhibitor risk |
| Nonsense mutations | ~15% | Severe |
| Missense mutations | ~40% (all severities) | Mild to severe depending on domain |
| Splice site mutations | ~10% | Variable |

**Inhibitor risk:** Inversely related to residual FVIII epitope sharing with infused product. Patients with inv22 or large deletions have no FVIII protein → highest inhibitor risk (~35-40%). Missense mutations in mild-moderate HA: low inhibitor risk (shared epitopes with normal FVIII).

## Function

### FVIII in coagulation

FVIII is a critical **amplifier** of the coagulation cascade at the junction between the intrinsic pathway initiation and the common pathway:

1. **FVIII in plasma:** Circulates as an inactive procofactor bound to VWF (protects FVIII from LRP1-mediated clearance and APC cleavage); plasma concentration ~0.1-0.2 µg/mL (~1 nM)

2. **Activation:** At sites of vascular injury, thrombin (generated by the extrinsic pathway via TF-VIIa) cleaves VWF-bound FVIII → releases FVIIIa; alternatively, FXa cleaves FVIII less efficiently

3. **Intrinsic tenase complex:** FVIIIa binds FIXa on the phospholipid surface of activated platelets (PS exposed) → FIXa/FVIIIa complex = "intrinsic tenase" → activates FX → FXa → prothrombinase → thrombin generation increases by ~10⁵-fold vs. FIXa alone (this amplification = "coagulation burst")

4. **Inactivation:** APC (activated protein C) + protein S cleave FVIIIa at Arg336 and Arg562 (A1 domain); FVIIIa also spontaneously inactivates by A2 domain dissociation; thrombomodulin-thrombin generates APC

**Without FVIII:** TF-VIIa initiates thrombin generation but the amplification loop (intrinsic tenase) is absent → clot forms slowly or not at all → hemarthrosis, intramuscular hematoma, potentially life-threatening CNS or retroperitoneal hemorrhage in severe HA.

## Pathology

### Clinical manifestations

**Hemarthrosis (joint bleeding; ~75% of hemorrhagic events in severe HA):**
- Knees, ankles, elbows most commonly affected
- Acute: pain, swelling, warmth, limited range of motion
- Chronic: synovitis → iron deposition → reactive synovial proliferation → cartilage destruction → **hemophilic arthropathy** (radiographic changes, chronic pain, contracture)
- **Target joint:** A joint with ≥3 bleeds in 6 months; most at risk for chronic damage; primary target for prophylaxis monitoring
- MRI scoring (IPSG MRI score) or ultrasound (Haemophilia Early Arthropathy Detection; HEAD-US) monitors joint damage

**Intramuscular hematoma:**
- Iliopsoas hematoma: mimics appendicitis; femoral nerve compression → hip flexion deformity; requires urgent FVIII
- Compartment syndrome: forearm, calf bleeds → treat aggressively before compartment compromise

**Life-threatening bleeds:**
- CNS hemorrhage (3-10% lifetime risk in severe HA): intracranial, subdural, subarachnoid; any head trauma → immediate FVIII prophylaxis + urgent CT
- Retroperitoneal hematoma
- Upper airway compromise (neck/pharyngeal hematoma)
- GI bleeding

### Diagnosis

**Laboratory:**
- **aPTT prolonged**; PT/INR normal (FVIII is intrinsic pathway only); fibrinogen normal; platelets normal
- **FVIII activity assay (1-stage aPTT-based or 2-stage chromogenic):** Quantifies FVIII function; chronic discrepancy between 1-stage and 2-stage (2-stage higher) suggests mild hemophilia A with specific F8 mutations (e.g., Arg531His)
- **FVIII antigen (FVIII:Ag):** Normal in mild HA with dysfunctional FVIII (missense mutations)
- **VWF:Ag and VWF:RCo:** Exclude VWD type 2N (FVIII-binding domain mutation — presents like mild HA but VWF antigen normal, FVIII reduced)
- **Inhibitor screen (Bethesda assay / Nijmegen modification):** Heat-inactivated patient plasma mixed with normal plasma at 50:50 → incubate 2 hours at 37°C → measure residual FVIII; ≥0.6 BU/mL = positive inhibitor

### Treatment

**Prophylaxis — standard of care (severe and moderate HA):**

**Emicizumab (Hemlibra; Roche/Genentech; bispecific FIXa/FX mAb):**
- Mechanism: Binds FIXa (via one arm) and FX (via other arm) → mimics FVIIIa cofactor function → reconstitutes intrinsic tenase activity independent of FVIII
- Structure: Asymmetric bispecific antibody (two different Fab arms); IgG4 Fc with half-life extension modifications → t½ ~4 weeks; SC injection
- **HAVEN-1 (inhibitor HA):** Emicizumab SC QW vs. BPA prophylaxis (APCC; FEIBA): ABR 2.9 vs. 23.3 (p<0.001); 63% zero bleeds [^oldenburg-2017-emicizumab-haven1]; FDA approved November 2017 for inhibitor HA
- **HAVEN-3 (non-inhibitor severe HA):** Emicizumab SC QW vs. no prophylaxis: ABR 1.5 vs. 38.2 (87% reduction); vs. prior FVIII prophylaxis (within-arm cross-over): ABR 1.5 vs. 4.8 (68% reduction) [^mahlangu-2018-emicizumab-haven3]; FDA approved October 2018 for non-inhibitor severe HA; extended to all HA regardless of inhibitor status
- Dosing: 3 mg/kg SC Q1W × 4 (loading) → 1.5 mg/kg Q1W or 3 mg/kg Q2W or 6 mg/kg Q4W (all equivalent maintenance)
- **Key limitation:** DOES NOT replace FVIII for breakthrough bleeds or surgery → still need FVIII (or bypassing agents in inhibitor patients) for acute hemostasis; **AVOID high-dose APCC (>100 IU/kg/day × 24h) with emicizumab** → thrombotic microangiopathy risk (HAVEN-1 signal)

**FVIII replacement (non-inhibitor HA; surgical prophylaxis; breakthrough bleeds):**
- Standard half-life (SHL) rFVIII: Advate, Kogenate, Helixate — t½ ~8-12 h; dosing Q8-12h for continuous prophylaxis
- Extended half-life (EHL) rFVIII: Efanesoctocog alfa (Altuviiio; Sanofi; FDA Apr 2023) — rFVIII fused to XTEN + VWF D'D3 domain → t½ ~96 h; Q1W dosing; XTEND-1 trial: ABR 0.71 (prophylaxis) → first once-weekly FVIII approved; Damoctocog alfa pegol (Jivi) — PEGylated EHL rFVIII; Q2W dosing
- Factor VIII dose formula: FVIII increment (%) = dose (IU) / body weight (kg) × 2; target levels: minor bleeds 30-50%; major bleeds 80-100%; surgery 100% perioperative → 50-80% for 7-14 days

**Inhibitor management:**
- **Immune tolerance induction (ITI):** High-dose FVIII (100-200 IU/kg/day IV) given daily until inhibitor eradicated (<0.6 BU/mL); success rate ~60-70% in high-titer inhibitors; 12-33 months median; now often preceded by rituximab to deplete B cells and shorten ITI duration
- **Bypassing agents (acute bleeding in inhibitor HA with breakthrough bleeds):**
  - APCC (anti-inhibitor coagulant complex; FEIBA; Shire): Activated prothrombin complex concentrate; 50-100 IU/kg Q12h; avoid with emicizumab (TMA risk)
  - Recombinant FVIIa (NovoSeven; Novo Nordisk): 90-270 µg/kg IV bolus Q2-3h; activates TF-FVIIa pathway to generate thrombin despite absent FVIII
- **Fitusiran (anti-antithrombin siRNA; ATLAS-INH trial):** Monthly SC injection; reduces antithrombin (AT) → lowers threshold for thrombin generation → bypasses FVIII; ATLAS-INH: ABR 0 vs. 17.8 vs. BPA on-demand (p<0.001) [^pipe-2023-fitusiran-atlas]; FDA approved 2024 for HA and HB with inhibitors

**Gene therapy:**
- **Valoctocogene roxaparvovec (BMGene-001; BioMarin; FDA Aug 2023):** AAV5-F8-SQ; single IV infusion → hepatocyte FVIII expression; FVIII levels 40-150 IU/dL at 2 years in ~60% of patients; GENEr8-1 trial: ABR reduced from 4.1 to 0.8; durability concern: FVIII levels decline ~50%/year (AAV episomal DNA diluted with hepatocyte proliferation); approved for adults with severe HA without pre-existing AAV5 neutralizing antibodies

## Connections

- `connects-to` → **[Von Willebrand Factor](../../03-molecular/von-willebrand-factor/README.md)** — VWF binds and protects FVIII in plasma → t½ ~12 h (VWF-bound) vs. ~2 h (free); VWF deficiency in VWD type 3 → secondary FVIII <10 IU/dL (resembles mild hemophilia A); VWD type 2N: FVIII-binding domain mutations → FVIII deficiency with normal VWF antigen levels.
- `connects-to` → **[Immunoglobulin G](../../03-molecular/immunoglobulin-g/README.md)** — Anti-FVIII inhibitor antibodies are predominantly IgG4 (non-complement-fixing); IgG4 neutralizes FVIII infused as replacement therapy; inhibitor titer (Bethesda units) determines ITI strategy; emicizumab bypasses FVIII → effective despite IgG4 inhibitors.
- `connects-to` → **[Thrombin](../../03-molecular/thrombin/README.md)** — Thrombin cleaves FVIII at Arg372/Arg740/Arg1689 → generates FVIIIa cofactor for intrinsic tenase; APC (thrombomodulin-thrombin product) cleaves FVIIIa at Arg336/Arg562 → inactivation; in HA, extrinsic-pathway thrombin is intact but amplification (intrinsic tenase) fails.
- `connects-to` → **[Protein C](../../03-molecular/protein-c/README.md)** — APC inactivates FVIIIa by cleavage at Arg336 and Arg562; APC + protein S → efficient FVIIIa proteolysis → limits thrombin amplification; FV Leiden co-inheritance with mild HA creates a clinical paradox — APC resistance partially counteracts the hemophilic bleeding tendency.
- `connects-to` → **[Venous Thromboembolism](../../07-system/venous-thromboembolism/README.md)** — Severe HA (FVIII <1%) confers significant VTE protection; historical VTE rate in HA ~0.5/1000 PY vs. ~1.5-3/1000 general population; emicizumab reconstitutes intrinsic tenase; avoid high-dose APCC with emicizumab → TMA; gene therapy raising FVIII >150% increases VTE risk.
- `connects-to` → **[Hepatocyte](../../04-cellular/hepatocyte/README.md)** — Gene therapy for hemophilia A delivers an AAV-packaged F8 transgene to hepatocytes, which then secrete factor VIII; valoctocogene roxaparvovec raised FVIII toward normal, but expression wanes ~50%/year as episomal AAV DNA dilutes with hepatocyte turnover.
- `connects-to` → **[Antithrombin](../../03-molecular/antithrombin/README.md)** — Fitusiran flips hemophilia A treatment around: instead of replacing factor VIII, this siRNA lowers antithrombin to rebalance hemostasis and restore clotting in FVIII- or FIX-deficient patients, including those with inhibitors; overcorrection risks thrombosis.
- `connects-to` → **[Inherited Thrombophilia](../inherited-thrombophilia/README.md)** — Hemophilia A and inherited thrombophilia are mirror images — too little clotting versus too much; strikingly, co-inheriting factor V Leiden can soften a hemophiliac's bleeding because APC resistance keeps FVa active longer, compensating for the missing factor VIII amplification.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — Recurrent hemarthrosis is the defining morbidity of hemophilia A: bleeding into knees, ankles and elbows triggers synovitis, cartilage loss and destructive 'hemophilic arthropathy' → chronic pain and disability; prophylaxis and emicizumab aim to prevent these joint bleeds.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — Factor VIII is synthesized largely by liver sinusoidal endothelial cells and circulates protected by endothelial von Willebrand factor; injury exposing the subendothelial matrix starts hemostasis—context for FVIII deficiency, and a target for hemophilia gene therapy.
- `connects-to` → **[Platelet](../../04-cellular/platelet/README.md)** — Hemophilia A spares primary hemostasis—platelets still form the plug—but lacks the FVIIIa/FIXa 'tenase' complex that assembles on the activated platelet surface to burst-generate thrombin; without it the plug is unstable and rebleeds, hence delayed deep-tissue and joint bleeding.
- `connects-to` → **[Disseminated Intravascular Coagulation](../disseminated-intravascular-coagulation/README.md)** — Hemophilia A and DIC cause bleeding by opposite mechanisms: hemophilia is isolated factor VIII deficiency (long aPTT, normal PT and platelets) bleeding into joints, while DIC consumes all factors and platelets at once—the lab pattern tells inherited from acquired.
- `connects-to` → **[Immune Thrombocytopenia](../immune-thrombocytopenia/README.md)** — Hemophilia A and immune thrombocytopenia bleed by different mechanisms: hemophilia is a factor VIII deficit causing deep joint and muscle bleeds, while ITP is platelet destruction causing mucocutaneous petechiae—the pattern hints which arm of hemostasis failed.
- `connects-to` → **[Thrombotic Thrombocytopenic Purpura](../thrombotic-thrombocytopenic-purpura/README.md)** — Hemophilia A and TTP sit at opposite poles of hemostasis: hemophilia fails to clot from factor VIII deficiency and bleeds, while TTP clots pathologically from ADAMTS13 deficiency, consuming platelets in microthrombi—both too little and too much clotting cause disease.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — The liver is central to hemophilia A: hepatocytes make clotting factors, and liver-directed gene therapy now delivers a working factor VIII gene to hepatocytes, enabling them to produce the missing factor—turning the factor-making organ into the cure.
- `connects-to` → **[Stroke](../stroke/README.md)** — Intracranial hemorrhage is the most feared bleed in hemophilia A: deficient factor VIII can't stabilize clots, so brain bleeding is a leading cause of death—hemorrhagic stroke here is the mirror image of the ischemic stroke that clotting disorders cause.
- `connects-to` → **[Antiphospholipid Syndrome](../antiphospholipid-syndrome/README.md)** — Hemophilia A and antiphospholipid syndrome are mirror-image coagulation disorders—bleeding versus clotting: hemophilia lacks factor VIII, while APS has thrombosis-driving antiphospholipid antibodies; an acquired factor VIII inhibitor rarely bridges them.
- `connects-to` → **[Fibrinogen](../../03-molecular/fibrinogen/README.md)** — Hemophilia A spares fibrinogen but fails to reach it: factor VIII deficiency cripples the intrinsic pathway's thrombin burst, so although fibrinogen is normal, too little thrombin forms to convert it to a stable fibrin clot—hence delayed, recurrent bleeding.
- `connects-to` → **[Brain](../../06-organ/brain/README.md)** — Intracranial hemorrhage is the most feared hemophilia A complication: minor head trauma can cause life-threatening brain bleeding because clot formation is delayed, so prophylactic factor replacement and urgent dosing after head injury are central to care.
- `connects-to` → **[Hepatitis C](../hepatitis-c/README.md)** — Hemophilia A is historically tied to hepatitis C and HIV: before viral screening, pooled factor concentrates infected most treated patients with HCV and HIV—a tragedy that drove recombinant factor development, so older hemophiliacs carry a heavy chronic-viral burden.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — Hemophilia A is X-linked: the factor VIII gene sits on the X chromosome, so it overwhelmingly affects males while carrier mothers pass it on—making family history, carrier testing, and genetic counseling central to the reproductive side of the disease.
- `connects-to` → **[Immune System](../immune-system/README.md)** — The immune system is hemophilia A's biggest treatment hurdle: some patients form neutralizing antibodies (inhibitors) against infused factor VIII, making replacement fail—so immune tolerance regimens and inhibitor-bypassing agents like emicizumab are needed.
- `connects-to` → **[Erythrocyte](../../04-cellular/erythrocyte/README.md)** — Bleeding in hemophilia A drains red cells: recurrent joint and muscle bleeds, plus dangerous internal hemorrhage, cause iron-deficiency or acute anemia, so falling hemoglobin and the need for transfusion track the severity of uncontrolled bleeding.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Calcium is the silent partner of the clotting cascade hemophilia disrupts: as coagulation Factor IV, calcium ions are needed to assemble the tenase and prothrombinase complexes—so clotting depends on calcium, and citrate that binds it blocks coagulation in stored blood.
- `connects-to` → **[T Helper Cell](../../04-cellular/t-helper-cell/README.md)** — The feared complication of hemophilia A is inhibitors, driven by T-helper cells: in some patients, helper T cells license B cells to make anti-Factor-VIII antibodies that neutralize replacement therapy, forcing bypassing agents or immune tolerance induction.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Repeated joint bleeds in hemophilia damage joints through macrophages: blood in the joint loads synovial macrophages with iron, driving inflammatory synovitis that erodes cartilage—the hemophilic arthropathy that prophylactic factor aims to prevent.
- `connects-to` → **[Collagen](../../03-molecular/collagen/README.md)** — Hemophilia A forms the collagen-triggered platelet plug but can't stabilize it: exposed collagen still recruits platelets into an initial plug, but without factor VIII the secondary fibrin clot never reinforces it, so bleeding restarts hours later.
- `connects-to` → **[Regulatory T Cell](../../04-cellular/regulatory-t-cell/README.md)** — Hemophilia A's worst complication is immune, needing regulatory T cells: about a third of severe patients make anti-factor-VIII antibodies (inhibitors), and immune tolerance induction works to restore the Tregs that should accept the infused factor.
- `connects-to` → **[B Cell](../../04-cellular/b-cell/README.md)** — Hemophilia A's inhibitors come from B cells: in patients who make anti-factor-VIII antibodies, B cells produce the neutralizing IgG that defeats replacement therapy—so B-cell-depleting rituximab is used to help eradicate stubborn inhibitors.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Hemophilia's joint bleeds leave iron behind: blood pooling in a joint deposits iron as hemosiderin that inflames the synovium and erodes cartilage, driving the crippling hemophilic arthropathy—and repeated bleeds also cause iron-loss anemia.
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — Hemophilia often bleeds into the urinary tract: painless hematuria is common, and clots can obstruct the ureter, so kidney and bladder bleeding is a recognized, usually self-limited feature managed cautiously to avoid clot retention.
- `connects-to` → **[Large Intestine](../../06-organ/large-intestine/README.md)** — Hemophilia can bleed dangerously into the gut: gastrointestinal hemorrhage, sometimes massive, is a serious complication, so dark or bloody stools in a hemophiliac demand urgent factor replacement and evaluation.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Imaging tracks hemophilia's joint damage: X-ray and MRI photons reveal the arthropathy from repeated bleeds, and radiosynovectomy uses radiation to quiet a chronically bleeding joint.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — Hemophilia shows on the skin: easy bruising and large, deep hematomas are often the first sign in a toddler learning to walk, hinting at the clotting defect beneath the surface.
- `connects-to` → **[Bone Marrow](../../05-tissue/bone-marrow/README.md)** — Chronic bleeding taxes the marrow: ongoing blood and iron loss in hemophilia push the bone marrow to ramp up red-cell production to keep pace, and anemia results when the losses outstrip it.
- `connects-to` → **[HIV/AIDS](../hiv-aids/README.md)** — Hemophilia carries a tragic medical legacy: before viral screening and recombinant factor, the pooled plasma concentrates that treated it infected a large share of patients with HIV and hepatitis C, a catastrophe that reshaped blood-product safety.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy shows why hemophilia's clots fail: lacking factor VIII to drive thrombin, the fibrin mesh forms with fewer, thinner, loosely woven fibers, a fragile structure that cannot hold against ongoing bleeding.
- `connects-to` → **[Eye](../../06-organ/eye/README.md)** — Bleeding into the eye threatens sight in hemophilia: spontaneous or traumatic intraocular and retinal hemorrhages, like bleeds into other closed spaces, can raise pressure and damage vision if not promptly treated with factor replacement.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — Hemophilia's bleeds can crush nerves: a deep muscle bleed — the classic iliopsoas hematoma — compresses the femoral nerve into palsy, while an intracranial hemorrhage destroys neurons directly, the most feared complication.
- `connects-to` → **[Osteoblast](../../04-cellular/osteoblast/README.md)** — Hemophilia quietly weakens the skeleton: recurrent joint bleeds destroy cartilage and bone, and reduced activity plus chronic inflammation tip the osteoblast-osteoclast balance toward the low bone density common in these patients.
- `connects-to` → **[Smooth Muscle Cell](../../04-cellular/smooth-muscle-cell/README.md)** — Why hemophilia bleeds late, not instantly: the first response to injury — reflex constriction of the vessel's smooth muscle and the platelet plug — is intact, so small cuts seal, but the missing factor VIII fails the later step, letting deep bleeds well up hours afterward.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — Antibodies are hemophilia's nemesis and its newest cure: inhibitor alloantibodies against infused factor VIII are the dreaded complication that neutralizes treatment, while emicizumab, a bispecific antibody bridging factors IXa and X, now prevents bleeds without it.
- `connects-to` → **[Peripheral Nerve](../../05-tissue/peripheral-nerve/README.md)** — A deep bleed can crush a nerve: a tense hematoma in the iliopsoas or forearm compresses the peripheral nerve running through it, causing a compartment syndrome with numbness, weakness, and palsy that needs urgent factor replacement.
- `connects-to` → **[Hepatitis B](../hepatitis-b/README.md)** — The old treatment carried hidden viruses: before viral inactivation, plasma-derived factor VIII concentrates transmitted hepatitis B and C and HIV to a generation of patients, a tragedy that drove the shift to recombinant factor and vaccination.

[^oldenburg-2017-emicizumab-haven1]: Oldenburg J, Mahlangu JN, Kim B, et al. Emicizumab prophylaxis in hemophilia A with inhibitors. *N Engl J Med.* 2017;377(9):809-818. [doi:10.1056/NEJMoa1703068](https://doi.org/10.1056/NEJMoa1703068) · [PubMed 28691557](https://pubmed.ncbi.nlm.nih.gov/28691557/)
[^mahlangu-2018-emicizumab-haven3]: Mahlangu J, Oldenburg J, Paz-Priel I, et al. Emicizumab prophylaxis in patients who have hemophilia A without inhibitors. *N Engl J Med.* 2018;379(9):811-822. [doi:10.1056/NEJMoa1803550](https://doi.org/10.1056/NEJMoa1803550) · [PubMed 30157389](https://pubmed.ncbi.nlm.nih.gov/30157389/)
[^pipe-2023-fitusiran-atlas]: Pipe SW, Leebeek FW, Recht M, et al. Once-monthly subcutaneous fitusiran versus on-demand bypassing agent for haemophilia A or B with inhibitors (ATLAS-INH). *Lancet.* 2023;401(10386):1427-1439. [doi:10.1016/S0140-6736(23)00284-2](https://doi.org/10.1016/S0140-6736(23)00284-2) · [PubMed 37003297](https://pubmed.ncbi.nlm.nih.gov/37003297/)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
