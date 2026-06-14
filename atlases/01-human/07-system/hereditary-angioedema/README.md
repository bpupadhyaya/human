---
schema: human-scale-entry/v1
id: hereditary-angioedema
name: Hereditary Angioedema
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-07
summary: "Hereditary angioedema (HAE) is recurrent bradykinin-mediated swelling from C1-INH deficiency; laryngeal HAE causes asphyxiation. Icatibant (B2R antagonist) and C1-INH concentrate for acute attacks; berotralstat and lanadelumab for long-term prophylaxis."
aliases: ["HAE", "hereditary angioedema", "HAE type I", "HAE type II", "HAE type III", "C1 inhibitor deficiency", "SERPING1 deficiency", "bradykinin angioedema", "Quincke's edema"]
sources:
  - id: cicardi-2010-icatibant-nejm
    type: peer-reviewed
    cite: "Cicardi M, Banerji A, Bracho F, et al. Icatibant, a new bradykinin-receptor antagonist, in hereditary angioedema. N Engl J Med. 2010;363(6):532-541."
    doi: "10.1056/NEJMoa0906393"
    pmid: "20818873"
    url: "https://doi.org/10.1056/NEJMoa0906393"
  - id: maurer-2018-lanadelumab-help
    type: peer-reviewed
    cite: "Banerji A, Riedl MA, Bernstein JA, et al. Effect of lanadelumab compared with placebo on prevention of hereditary angioedema attacks: a randomized clinical trial. JAMA. 2018;320(20):2108-2121."
    doi: "10.1001/jama.2018.16773"
    pmid: "30480729"
    url: "https://doi.org/10.1001/jama.2018.16773"
  - id: zuraw-2020-berotralstat-apex2
    type: peer-reviewed
    cite: "Zuraw BL, Busse PJ, White M, et al. Berotralstat (BCX7353) for the prevention of hereditary angioedema. N Engl J Med. 2021;384(23):2186-2195."
    doi: "10.1056/NEJMoa2103679"
    pmid: "34077648"
    url: "https://doi.org/10.1056/NEJMoa2103679"
cross_links:
  - target: 01-human/03-molecular/c1-esterase-inhibitor
    relation: connects-to
    note: "C1-INH deficiency (type I: low antigen + activity; type II: low activity, normal antigen) → uncontrolled FXII/kallikrein → bradykinin excess → B2R-mediated vascular permeability → HAE attacks; icatibant, C1-INH concentrate, berotralstat, and lanadelumab are therapeutic targets."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "C1-INH deficiency → chronic C1 complex activation → C4 consumed even between attacks (key screening test); low C4 + low C1-INH activity = HAE type I/II diagnosis; C3 usually normal; C1q normal (distinguishes HAE from acquired angioedema with anti-C1q antibodies)."
  - target: 01-human/03-molecular/bradykinin
    relation: connects-to
    note: "HAE is the paradigmatic bradykinin-excess disease: C1-INH deficiency → uncontrolled FXII/kallikrein → bradykinin generation from HMWK; bradykinin binds B2R on postcapillary venules → Gαq/Ca²⁺ → eNOS/NO → vascular permeability; icatibant (B2R antagonist) aborts HAE attacks."
  - target: 01-human/03-molecular/angiotensin-ii
    relation: connects-to
    note: "ACE (kininase II) degrades bradykinin; ACEi block catabolism → bradykinin accumulation → angioedema (~0.1-0.7% of users); ACEi contraindicated in HAE; Ang-II and bradykinin are both ACE substrates → RAAS and kinin-kallikrein systems are mechanistically linked."
  - target: 01-human/03-molecular/thrombin
    relation: connects-to
    note: "Trauma/surgery → thrombin generation → FXII activation → contact cascade → kallikrein → bradykinin → HAE attack; surgical trauma triggers ~25-50% of HAE attacks; short-term C1-INH concentrate or icatibant before high-risk procedures prevents peri-operative attacks."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "Every HAE attack ends at the endothelial cell: bradykinin binds its B2 receptor on postcapillary venule endothelium → Gαq/Ca²⁺ → eNOS-derived NO loosens inter-endothelial junctions → plasma leaks into tissue as non-urticarial swelling; icatibant blocks B2R to abort this."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "HAE swelling is subcutaneous or submucosal and looks unlike allergic hives: ~50% of attacks are tense, non-pitting, non-urticarial skin swelling that lasts 2-5 days and does not itch or respond to antihistamines — reflecting its bradykinin (not histamine) mechanism."
  - target: 01-human/03-molecular/estrogen
    relation: connects-to
    note: "Estrogen worsens HAE by upregulating prekallikrein, boosting bradykinin generation; estrogen-containing contraceptives and pregnancy trigger attacks, and FXII (type III) HAE is largely a disease of women on the pill — so progestin-only contraception is advised."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "HAE is a disorder of complement regulation: C1-inhibitor normally restrains the classical complement pathway and the contact (kinin) system, so its deficiency consumes C4 (a diagnostic clue) and unleashes bradykinin; it sits between complement and innate immune control."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "HAE is the key bradykinin-mediated mimic of mast-cell angioedema: unlike histaminergic allergic angioedema (urticaria, itch, antihistamine response), HAE swelling is non-itchy, urticaria-free and unresponsive to antihistamines or epinephrine—telling them apart is life-saving."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "The liver synthesizes C1-inhibitor and most complement and contact-system proteins, so it underlies HAE: types I/II HAE reflect deficient or dysfunctional hepatic C1-INH, and siRNA therapy (donidalorsen targeting prekallikrein) acts on hepatic production to prevent attacks."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "Abdominal attacks are a major, often misdiagnosed feature of hereditary angioedema: bradykinin-driven edema of the bowel wall causes severe colicky pain, vomiting, and ascites that mimic a surgical abdomen, so recurrent crises with C1-inhibitor deficiency point to HAE."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "Laryngeal edema is the lethal manifestation of hereditary angioedema: bradykinin-mediated upper-airway swelling can cause asphyxiation, so patients carry on-demand C1-inhibitor or icatibant—and unlike histaminergic angioedema, it ignores epinephrine and antihistamines."
  - target: 01-human/07-system/hypertension
    relation: connects-to
    note: "ACE inhibitors can trigger bradykinin-mediated angioedema like HAE: ACE normally degrades bradykinin, so blocking it raises bradykinin and causes angioedema (especially in HAE patients), which is why ACE inhibitors are contraindicated in hereditary angioedema."
  - target: 01-human/03-molecular/complement-c5
    relation: connects-to
    note: "Hereditary angioedema reflects loss of C1-inhibitor's brake on the contact and complement systems: without it, kallikrein generates bradykinin while the classical complement pathway runs unchecked, consuming C4—so low C4 is the screening clue to HAE."
  - target: 01-human/07-system/asthma
    relation: connects-to
    note: "Hereditary angioedema and asthma both cause acute airway emergencies: HAE's bradykinin-driven laryngeal edema obstructs the upper airway and ignores bronchodilators and steroids, unlike asthma's smooth-muscle bronchospasm—so the distinction is life-saving."
  - target: 01-human/07-system/atopic-dermatitis
    relation: connects-to
    note: "Hereditary angioedema is the bradykinin-mediated counterpart to histamine-driven (allergic) angioedema seen with atopic dermatitis and urticaria: HAE lacks hives and ignores antihistamines, steroids and epinephrine—needing C1-INH or bradykinin-pathway drugs instead."
  - target: 01-human/06-organ/small-intestine
    relation: connects-to
    note: "Hereditary angioedema attacks the gut wall: bradykinin-driven edema of the small intestine causes severe colicky pain, vomiting and even obstruction, so HAE can mimic a surgical abdomen—and unexplained recurrent abdominal attacks should prompt C1-inhibitor testing."
  - target: 01-human/03-molecular/nitric-oxide
    relation: connects-to
    note: "Bradykinin drives HAE swelling through nitric oxide and vascular leak: it binds endothelial B2 receptors to release NO and open intercellular junctions, flooding tissue with fluid—the same vasodilator pathway behind blood-pressure control produces the edema."
  - target: 01-human/07-system/systemic-lupus-erythematosus
    relation: connects-to
    note: "Acquired C1-inhibitor deficiency mimics hereditary angioedema in autoimmune or lymphoproliferative disease: SLE and lymphomas can consume or block C1-INH, causing bradykinin angioedema later in life—so adult-onset angioedema without family history needs a workup."
  - target: 01-human/03-molecular/histamine
    relation: connects-to
    note: "Hereditary angioedema is bradykinin-, not histamine-driven—and that distinction is everything: unlike allergic angioedema and hives, HAE swelling does not respond to antihistamines, steroids, or epinephrine, so recognizing the non-histaminergic mechanism saves airways."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "Hereditary angioedema is shaped by the reproductive system: estrogen worsens attacks, so puberty, pregnancy, and the contraceptive Pill can trigger flares—and an estrogen-dependent FXII-linked form affects mainly women, making hormone choices central to care."
  - target: 01-human/04-cellular/smooth-muscle-cell
    relation: connects-to
    note: "HAE attacks hinge on smooth muscle: bradykinin relaxes vascular smooth muscle and opens endothelial junctions, flooding tissue with fluid—and in the gut, submucosal edema with smooth-muscle spasm causes severe abdominal pain that mimics a surgical abdomen."
---

# Hereditary Angioedema

## Overview

**Hereditary angioedema (HAE)** is an **autosomal dominant** disease of recurrent, self-limited, potentially life-threatening swelling caused by **bradykinin excess** secondary to **C1-esterase inhibitor (C1-INH) deficiency or dysfunction** [^cicardi-2010-icatibant-nejm]. Unlike allergic angioedema (which is IgE-mediated/histamine-driven and responds to antihistamines and epinephrine), HAE is **bradykinin-mediated** — antihistamines, corticosteroids, and epinephrine are largely ineffective. HAE affects approximately 1 in 50,000 people worldwide, without racial predilection, and typically presents in the first or second decade of life.

**The defining clinical triad of HAE:**
1. **Recurrent episodes** of non-pitting, non-urticarial subcutaneous or submucosal swelling
2. **Self-limited** attacks lasting 2-5 days without treatment (72-96 hours typical)
3. **Bradykinin-mediated** mechanism: no urticaria, no response to antihistamines/steroids
4. **Family history** in ~75% (25% are de novo SERPING1 mutations)

**Mortality:** Untreated laryngeal HAE has a historical mortality of ~30-40% — asphyxiation from upper airway swelling is the leading cause of HAE death. With modern therapy (icatibant, C1-INH concentrate) and patient education, laryngeal attacks can be managed safely if treated early.

**HAE classification:**

| Type | Mechanism | C1-INH antigen | C1-INH activity | C4 | C1q |
|:-----|:----------|:--------------|:----------------|:---|:----|
| **Type I** (~80%) | SERPING1 loss-of-function → insufficient C1-INH production | Low (<30%) | Low (<50%) | Low | Normal |
| **Type II** (~15%) | SERPING1 missense → dysfunctional protein | Normal or high | Low (<50%) | Low | Normal |
| **Type III** (<5%) | FXII gain-of-function (F12 p.Thr309Lys/Arg) → excess kallikrein activity | Normal | Normal | Normal | Normal |
| **Acquired angioedema** | Anti-C1q antibodies (lymphoma, autoimmune) | Low | Low | Low | **Low** |

## Structure

### Pathophysiological framework

**The bradykinin cascade in HAE:**

```
Contact activation trigger
        ↓
   FXII activation → FXIIa
        ↓ ← [C1-INH blocks here]
Prekallikrein → Plasma kallikrein ← [berotralstat, lanadelumab, ecallantide block here]
        ↓
High-molecular-weight kininogen (HMWK) → Bradykinin (9 aa) + Kinin-free HMWK
        ↓ ← [icatibant blocks here (B2R antagonist)]
Bradykinin B2 receptor (endothelium)
        ↓
Gαq → IP₃ → Ca²⁺ → eNOS → NO + PGI₂
        ↓
↑Vascular permeability (postcapillary venules)
        ↓
Fluid extravasation → ANGIOEDEMA
```

**Common attack triggers:**
- **Trauma/surgery** (most common; 25-50% of attacks): dental procedures, endoscopy, surgical intubation — jaw/throat/oral edema are especially dangerous
- **Psychological stress** (emotionally stressful events → catecholamines → FXII activation)
- **Infections** (upper respiratory infections, GI infections)
- **Estrogen exposure** (oral contraceptives, hormone replacement, pregnancy): estrogen upregulates prekallikrein and HMWK → increased bradykinin generation; type III HAE is predominantly a disease of women taking OCP or pregnant
- **ACE inhibitors**: ACE (kininase II) degrades bradykinin; ACE inhibitors → bradykinin accumulation → can both unmask latent HAE and cause angioedema de novo (ACE inhibitor–induced angioedema is also bradykinin-mediated)
- **Idiopathic** (30-40% of attacks): no identifiable trigger

### Distribution of swelling (attack phenotype)

| Location | Frequency | Clinical features |
|:---------|:----------|:------------------|
| **Subcutaneous** (extremities, trunk, face) | ~50% | Tense, non-pitting swelling; no urticaria; may be disfiguring; self-resolves |
| **Abdominal (intestinal wall)** | ~25-30% | Severe colicky abdominal pain, nausea, vomiting, diarrhea; can mimic acute abdomen; ascites on imaging; may lead to unnecessary laparotomy |
| **Laryngeal/oropharyngeal** | ~10-15% | Throat tightness, voice changes, stridor → life-threatening asphyxiation; rapidly progressing attacks require emergent treatment |
| **Genital/urinary** | ~5% | Self-limited; painful |
| **CNS** (rare) | <1% | Headache; cerebral edema rare |

## Function

### Diagnosis

**Diagnostic workup:**

1. **Clinical suspicion:** Recurrent non-urticarial angioedema + family history ± abdominal attacks ± failure of antihistamines; often misdiagnosed as allergic angioedema or recurrent abdominal pain for years

2. **Laboratory confirmation:**
   - **C4 level:** Consistently low (<30% of normal) even between attacks — the single best screening test; reflects chronic low-level C1 activation
   - **C1-INH antigen:** Low in type I (normal/elevated in type II)
   - **C1-INH functional activity:** Low in both type I and II (<50% of normal; typically <30%); the definitive test
   - **C1q:** Normal in HAE types I, II, III (differentiates from acquired angioedema where anti-C1q antibodies consume C1q)

3. **Confirm with genetic testing:** *SERPING1* sequencing confirms type I/II; *F12* mutations confirm type III

4. **FXII gene testing:** If HAE suspected but C4/C1-INH normal, especially in women with estrogen-related attacks

**Differential diagnosis of angioedema:**

| Feature | HAE | ACE inhibitor angioedema | Allergic angioedema | Acquired angioedema |
|:--------|:----|:------------------------|:--------------------|:--------------------|
| Urticaria | No | No | Usually yes | No |
| C4 | Low | Normal | Normal | Low |
| C1-INH activity | Low | Normal | Normal | Low |
| C1q | Normal | Normal | Normal | **Low** |
| Onset | Childhood/teen | Any age (months after ACEi) | Minutes after trigger | Adult onset |
| Family history | Yes | No | Variable | No |
| Response to antihistamine/steroid | No | No | Yes | No |

## Pathology

### Acute treatment [^cicardi-2010-icatibant-nejm]

**Principle: treat every laryngeal attack, all abdominal attacks, and facial attacks as emergencies. Goal: abort attack as fast as possible.**

**First-line options (self-administration available):**
- **Icatibant (Firazyr):** Bradykinin B2R competitive antagonist; SC injection 30 mg; approved EU 2008, FDA 2011; FAST-3 trial: time to significant symptom relief 2.0 h vs 19.8 h with placebo; can self-administer; repeat dose q6h if needed (max 3 doses/24h); works even with normal C1-INH (also first-line for ACE inhibitor–induced angioedema)
- **Plasma-derived C1-INH (Berinert) IV:** 20 IU/kg IV; rapid IV infusion; fast onset (1-2h); first-line in many centers; most proven safety profile; also used in obstetric emergencies (pregnancy-associated HAE)
- **Recombinant C1-INH (Ruconest):** 50 IU/kg IV (max 4200 IU); faster production than plasma-derived; effective; bovine allergenicity risk (cattle-allergic patients)
- **Ecallantide (Kalbitor):** SC kallikrein inhibitor; 30 mg SC (3 × 10 mg injections); US only; healthcare provider must administer (anaphylaxis risk ~4%)

**If above unavailable (fresh frozen plasma):**
- FFP: 2-4 units IV; contains C1-INH, C4, C2; used as rescue therapy when specific agents unavailable; paradoxically may transiently worsen attack (HMWK and kallikrein in FFP) before helping — rarely used now

**Laryngeal HAE: immediate treatment + prepare for intubation/tracheotomy:**
- Secure airway assessment; ENT/anesthesia on standby
- Administer icatibant + C1-INH concentrate IMMEDIATELY (both if available)
- Endotracheal intubation may be required if symptoms progress despite treatment

### Long-term prophylaxis

**Indications:** >1 attack/month, severe/poorly controlled attacks, occupational/social impairment, high-risk procedures planned, prior laryngeal attacks.

**Options:**
- **Lanadelumab (Takhzyro; SC q2-4 weeks):** Humanized anti-kallikrein IgG4 mAb; 300 mg SC q4 weeks (or q2 weeks for more severe disease); HELP OLE trial: 87% reduction in HAE attacks (from mean 3.0/month to 0.4/month) [^maurer-2018-lanadelumab-help]; FDA approved Aug 2018; most effective prophylaxis available
- **Berotralstat (Orladeyo; 110 mg/day oral):** Oral plasma kallikrein inhibitor; APeX-2: 44% reduction in monthly HAE attacks vs placebo [^zuraw-2020-berotralstat-apex2]; FDA approved Dec 2020; first oral once-daily prophylaxis; also available 150 mg/day
- **SC C1-INH (Haegarda):** 60 IU/kg SC twice weekly; self-administered; effective; useful in patients who prefer replacement therapy
- **Danazol (attenuated androgen):** Stimulates C1-INH synthesis (SERPING1 upregulation via androgen receptor); now rarely used — virilization, hepatotoxicity, contraindicated in children and pregnancy; replaced by targeted therapies
- **Tranexamic acid:** Antifibrinolytic (inhibits plasmin); modest efficacy; mechanism unclear (reduced FXII activation?); alternative when other therapies unavailable

**Short-term prophylaxis (for planned procedures):**
- High-risk (dental work, surgery, intubation): 1-2 units C1-INH concentrate 30-60 min before procedure; OR icatibant held on standby

**Special populations:**
- **Children:** C1-INH concentrate (no dose restrictions); berotralstat FDA-approved ≥12 years; lanadelumab FDA-approved ≥12 years; danazol contraindicated
- **Pregnancy:** C1-INH concentrate is preferred (safe in pregnancy); icatibant (FDA category C — limited data but widely used); avoid danazol (virilization of female fetus), tranexamic acid (VTE risk)
- **HAE type III (FXII mutation):** Avoid estrogen-containing OCP; progestogen-only contraception + tranexamic acid for milder cases; C1-INH and icatibant for acute attacks; lanadelumab for prophylaxis

## Connections

- `connects-to` → **[C1-Esterase Inhibitor](../../03-molecular/c1-esterase-inhibitor/README.md)** — C1-INH deficiency (type I: low antigen + activity; type II: low activity, normal antigen) → uncontrolled FXII/kallikrein → bradykinin excess → B2R-mediated vascular permeability → HAE attacks; icatibant, C1-INH concentrate, berotralstat, and lanadelumab are therapeutic targets.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — C1-INH deficiency → chronic low-level C1 complex activation → C4/C2 cleavage → C4 consumed even between attacks; low C4 + low C1-INH functional activity = diagnostic criteria for HAE type I/II; C3 is usually normal (C3 convertase limited); C1q is normal (distinguishes from acquired angioedema).
- `connects-to` → **[Bradykinin](../../03-molecular/bradykinin/README.md)** — HAE is the paradigmatic bradykinin-excess disease: C1-INH deficiency → uncontrolled FXII/kallikrein → bradykinin generation from HMWK; bradykinin binds B2R on postcapillary venules → Gαq/Ca²⁺ → eNOS/NO → vascular permeability; icatibant (B2R antagonist) aborts HAE attacks.
- `connects-to` → **[Angiotensin II](../../03-molecular/angiotensin-ii/README.md)** — ACE (kininase II) degrades bradykinin; ACEi block catabolism → bradykinin accumulation → angioedema (~0.1-0.7% of users); ACEi contraindicated in HAE; Ang-II and bradykinin are both ACE substrates → RAAS and kinin-kallikrein systems are mechanistically linked.
- `connects-to` → **[Thrombin](../../03-molecular/thrombin/README.md)** — Trauma/surgery → thrombin generation → FXII activation → contact cascade → kallikrein → bradykinin → HAE attack; surgical trauma triggers ~25-50% of HAE attacks; short-term C1-INH concentrate or icatibant before high-risk procedures prevents peri-operative attacks.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — Every HAE attack ends at the endothelial cell: bradykinin binds its B2 receptor on postcapillary venule endothelium → Gαq/Ca²⁺ → eNOS-derived NO loosens inter-endothelial junctions → plasma leaks into tissue as non-urticarial swelling; icatibant blocks B2R to abort this.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — HAE swelling is subcutaneous or submucosal and looks unlike allergic hives: ~50% of attacks are tense, non-pitting, non-urticarial skin swelling that lasts 2-5 days and does not itch or respond to antihistamines — reflecting its bradykinin (not histamine) mechanism.
- `connects-to` → **[Estrogen](../../03-molecular/estrogen/README.md)** — Estrogen worsens HAE by upregulating prekallikrein, boosting bradykinin generation; estrogen-containing contraceptives and pregnancy trigger attacks, and FXII (type III) HAE is largely a disease of women on the pill — so progestin-only contraception is advised.
- `connects-to` → **[Immune System](../immune-system/README.md)** — HAE is a disorder of complement regulation: C1-inhibitor normally restrains the classical complement pathway and the contact (kinin) system, so its deficiency consumes C4 (a diagnostic clue) and unleashes bradykinin; it sits between complement and innate immune control.
- `connects-to` → **[Mast Cell](../../04-cellular/mast-cell/README.md)** — HAE is the key bradykinin-mediated mimic of mast-cell angioedema: unlike histaminergic allergic angioedema (urticaria, itch, antihistamine response), HAE swelling is non-itchy, urticaria-free and unresponsive to antihistamines or epinephrine—telling them apart is life-saving.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — The liver synthesizes C1-inhibitor and most complement and contact-system proteins, so it underlies HAE: types I/II HAE reflect deficient or dysfunctional hepatic C1-INH, and siRNA therapy (donidalorsen targeting prekallikrein) acts on hepatic production to prevent attacks.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — Abdominal attacks are a major, often misdiagnosed feature of hereditary angioedema: bradykinin-driven edema of the bowel wall causes severe colicky pain, vomiting, and ascites that mimic a surgical abdomen, so recurrent crises with C1-inhibitor deficiency point to HAE.
- `connects-to` → **[Respiratory system](../respiratory-system/README.md)** — Laryngeal edema is the lethal manifestation of hereditary angioedema: bradykinin-mediated upper-airway swelling can cause asphyxiation, so patients carry on-demand C1-inhibitor or icatibant—and unlike histaminergic angioedema, it ignores epinephrine and antihistamines.
- `connects-to` → **[Hypertension](../hypertension/README.md)** — ACE inhibitors can trigger bradykinin-mediated angioedema like HAE: ACE normally degrades bradykinin, so blocking it raises bradykinin and causes angioedema (especially in HAE patients), which is why ACE inhibitors are contraindicated in hereditary angioedema.
- `connects-to` → **[Complement C5](../../03-molecular/complement-c5/README.md)** — Hereditary angioedema reflects loss of C1-inhibitor's brake on the contact and complement systems: without it, kallikrein generates bradykinin while the classical complement pathway runs unchecked, consuming C4—so low C4 is the screening clue to HAE.
- `connects-to` → **[Asthma](../asthma/README.md)** — Hereditary angioedema and asthma both cause acute airway emergencies: HAE's bradykinin-driven laryngeal edema obstructs the upper airway and ignores bronchodilators and steroids, unlike asthma's smooth-muscle bronchospasm—so the distinction is life-saving.
- `connects-to` → **[Atopic Dermatitis](../atopic-dermatitis/README.md)** — Hereditary angioedema is the bradykinin-mediated counterpart to histamine-driven (allergic) angioedema seen with atopic dermatitis and urticaria: HAE lacks hives and ignores antihistamines, steroids and epinephrine—needing C1-INH or bradykinin-pathway drugs instead.
- `connects-to` → **[Small Intestine](../../06-organ/small-intestine/README.md)** — Hereditary angioedema attacks the gut wall: bradykinin-driven edema of the small intestine causes severe colicky pain, vomiting and even obstruction, so HAE can mimic a surgical abdomen—and unexplained recurrent abdominal attacks should prompt C1-inhibitor testing.
- `connects-to` → **[Nitric Oxide](../../03-molecular/nitric-oxide/README.md)** — Bradykinin drives HAE swelling through nitric oxide and vascular leak: it binds endothelial B2 receptors to release NO and open intercellular junctions, flooding tissue with fluid—the same vasodilator pathway behind blood-pressure control produces the edema.
- `connects-to` → **[Systemic Lupus Erythematosus](../systemic-lupus-erythematosus/README.md)** — Acquired C1-inhibitor deficiency mimics hereditary angioedema in autoimmune or lymphoproliferative disease: SLE and lymphomas can consume or block C1-INH, causing bradykinin angioedema later in life—so adult-onset angioedema without family history needs a workup.
- `connects-to` → **[Histamine](../../03-molecular/histamine/README.md)** — Hereditary angioedema is bradykinin-, not histamine-driven—and that distinction is everything: unlike allergic angioedema and hives, HAE swelling does not respond to antihistamines, steroids, or epinephrine, so recognizing the non-histaminergic mechanism saves airways.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — Hereditary angioedema is shaped by the reproductive system: estrogen worsens attacks, so puberty, pregnancy, and the contraceptive Pill can trigger flares—and an estrogen-dependent FXII-linked form affects mainly women, making hormone choices central to care.
- `connects-to` → **[Smooth Muscle Cell](../../04-cellular/smooth-muscle-cell/README.md)** — HAE attacks hinge on smooth muscle: bradykinin relaxes vascular smooth muscle and opens endothelial junctions, flooding tissue with fluid—and in the gut, submucosal edema with smooth-muscle spasm causes severe abdominal pain that mimics a surgical abdomen.

[^cicardi-2010-icatibant-nejm]: Cicardi M, Banerji A, Bracho F, et al. Icatibant, a new bradykinin-receptor antagonist, in hereditary angioedema. *N Engl J Med.* 2010;363(6):532-541. [doi:10.1056/NEJMoa0906393](https://doi.org/10.1056/NEJMoa0906393) · [PubMed 20818873](https://pubmed.ncbi.nlm.nih.gov/20818873/)
[^maurer-2018-lanadelumab-help]: Banerji A, Riedl MA, Bernstein JA, et al. Effect of lanadelumab compared with placebo on prevention of hereditary angioedema attacks. *JAMA.* 2018;320(20):2108-2121. [doi:10.1001/jama.2018.16773](https://doi.org/10.1001/jama.2018.16773) · [PubMed 30480729](https://pubmed.ncbi.nlm.nih.gov/30480729/)
[^zuraw-2020-berotralstat-apex2]: Zuraw BL, Busse PJ, White M, et al. Berotralstat (BCX7353) for the prevention of hereditary angioedema. *N Engl J Med.* 2021;384(23):2186-2195. [doi:10.1056/NEJMoa2103679](https://doi.org/10.1056/NEJMoa2103679) · [PubMed 34077648](https://pubmed.ncbi.nlm.nih.gov/34077648/)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
