---
schema: human-scale-entry/v1
id: antithrombin
name: Antithrombin
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-08
summary: "Antithrombin (SERPINC1; AT-III; chr1q25.1) is the primary serine protease inhibitor of thrombin and FXa; heparin accelerates AT inhibition ~1000×; AT deficiency (rare; 1:5000) is the most thrombogenic inherited thrombophilia; consumed in DIC; bivalirudin bypasses AT."
aliases: ["antithrombin", "AT-III", "antithrombin III", "SERPINC1", "heparin cofactor I", "antithrombin-III"]
sources:
  - id: bauer-2001-thrombophilias
    type: peer-reviewed
    cite: "Bauer KA. The thrombophilias: well-defined risk factors with uncertain therapeutic implications. Ann Intern Med. 2001;135(5):367-373."
    doi: "10.7326/0003-4819-135-5-200109040-00015"
    pmid: "11529699"
    url: "https://doi.org/10.7326/0003-4819-135-5-200109040-00015"
  - id: hirsh-2008-parenteral-anticoagulants
    type: clinical-guideline
    cite: "Hirsh J, Bauer KA, Donati MB, et al. Parenteral anticoagulants: American College of Chest Physicians Evidence-Based Clinical Practice Guidelines (8th Edition). Chest. 2008;133(6 Suppl):141S-159S."
    doi: "10.1378/chest.08-0689"
    pmid: "18574271"
    url: "https://doi.org/10.1378/chest.08-0689"
cross_links:
  - target: 01-human/03-molecular/thrombin
    relation: connects-to
    note: "Antithrombin is the primary physiological inhibitor of thrombin (FIIa): AT forms a covalent suicide complex with thrombin → irreversible inhibition; rate constant 7×10³ M⁻¹s⁻¹ without heparin, accelerated ~1000× with UFH (heparin template effect)."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "AT deficiency (type I: ↓ quantity; type II: ↓ function) is the most severe inherited thrombophilia (25-50× lifetime VTE risk); heterozygous AT deficiency: 1:2,000-5,000 prevalence; AT concentrate needed when UFH fails in AT-deficient patients."
  - target: 01-human/07-system/inherited-thrombophilia
    relation: connects-to
    note: "AT deficiency carries 25-50× lifetime VTE risk; type IIa reactive-site mutations (Arg393His) most thrombogenic; combined AT + FV Leiden → very high VTE risk; functional AT activity assay (not immunologic) required for diagnosis."
  - target: 01-human/07-system/disseminated-intravascular-coagulation
    relation: connects-to
    note: "AT is consumed in DIC by ongoing thrombin generation; AT levels <60% correlate with DIC severity (ISTH DIC score); AT concentrate studied in sepsis-DIC (KyberSept trial: no mortality benefit); low AT + prolonged PT + thrombocytopenia = DIC triad."
  - target: 01-human/07-system/heparin-induced-thrombocytopenia
    relation: connects-to
    note: "UFH and LMWH exert anticoagulant effects via AT (heparin binds AT → conformational change → 1000× accelerated thrombin/FXa inhibition); in HIT, heparin must be stopped; direct thrombin inhibitors (argatroban, bivalirudin) bypass AT entirely."
---

# Antithrombin

## Overview

**Antithrombin (AT; formerly antithrombin III; gene *SERPINC1*, chromosome 1q25.1)** is the most important physiological anticoagulant in the coagulation cascade. It is a member of the **serpin superfamily** (serine protease inhibitor) — a 58 kDa single-chain glycoprotein synthesized by the liver and circulating in plasma at ~150 μg/mL (2.3 μM) [^bauer-2001-thrombophilias].

AT continuously scavenges activated coagulation proteases from the circulation, primarily:
- **Thrombin (FIIa):** Primary target; inhibition dramatically accelerated by heparin
- **Factor Xa (FXa):** Second most important target
- **Factor IXa, XIa, XIIa, VIIa-TF:** Inhibited at slower rates; collectively important for dampening contact-pathway and extrinsic pathway activation

The anticoagulant mechanism of **unfractionated heparin (UFH)**, **low-molecular-weight heparin (LMWH)**, and **fondaparinux** is mediated entirely through AT. Without AT, these drugs have no anticoagulant activity — a critical consideration in AT deficiency states.

**AT deficiency** is rare (~1:2,000–5,000 heterozygotes) but carries the highest thrombotic risk of any inherited thrombophilia: lifetime VTE risk is 25–50× the population baseline, compared to 3–5× for FV Leiden. AT deficiency is an independent indication for indefinite anticoagulation after any VTE event [^bauer-2001-thrombophilias].

## Structure

AT is a **432-amino acid, 58 kDa** single-chain glycoprotein with four N-linked oligosaccharide chains (N96, N135, N155, N192) that contribute ~30% of molecular weight and influence heparin binding affinity. The protein adopts the canonical serpin fold:

**Reactive Site Loop (RSL):**
- The RSL (residues ~385–400) contains the **P1 residue Arg393** — the target of coagulation proteases
- AT acts as a "suicide substrate": the protease (thrombin, FXa) attacks the RSL → forms a covalent acyl-enzyme intermediate → AT undergoes a large conformational change (RSL inserts as a strand into the central β-sheet A) → traps the protease irreversibly
- The AT-protease complex is then cleared by the reticuloendothelial system (half-life ~minutes, vs. free AT half-life ~60–70 hours)

**Heparin-Binding Domain:**
- N-terminal region contains a cluster of positively charged residues (K11, R13, R24, R47, K125, K133, K136) that form the heparin-binding exosite
- Heparin binds AT with Kd ~50 nM; binding induces a conformational change in the RSL (RSL extension) that dramatically increases the rate of protease recognition

**AT variants by type:**

| Type | AT antigen | AT activity | Mechanism | Notes |
|:-----|:----------|:------------|:---------|:------|
| Type I | Reduced | Reduced | Quantitative deficiency (deletions, frameshifts, splice-site mutations) | Most common; ~50% activity |
| Type IIa (RS) | Normal | Reduced | Reactive-site mutations (Arg393His, Arg393Cys) | Most thrombogenic type |
| Type IIb (HBS) | Normal | Normal vs. thrombin, ↓ with heparin | Heparin-binding site mutations | Moderate thrombotic risk |
| Type IIc (PE) | Normal | Reduced (pleiotropic) | Rare; multiple functional defects | |

Type IIa (reactive-site) variants are the most dangerous: AT fails to inhibit thrombin or FXa even at baseline concentrations.

## Function

### Physiological anticoagulation

AT maintains vascular patency through continuous first-order inhibition of activated coagulation factors. In the unperturbed circulation:
- **Baseline rate constants:** AT + thrombin: ~7×10³ M⁻¹s⁻¹; AT + FXa: ~2×10³ M⁻¹s⁻¹ — sufficient to prevent pathological thrombin accumulation
- Endothelial heparan sulfate proteoglycans (HSPGs) serve as a physiological template, providing low-level acceleration of AT-thrombin/FXa reactions on the endothelial surface
- AT also possesses **anti-inflammatory properties**: AT-heparan sulfate binding on endothelial cells activates prostacyclin (PGI₂) synthesis → vasodilation + platelet inhibition; AT fragments inhibit TNF-α and IL-6 (relevant in sepsis-DIC)

### Heparin cofactor mechanism

Exogenous heparin dramatically accelerates AT inhibition by two mechanisms:

**Conformational activation (pentasaccharide mechanism — FXa inhibition):**
1. A specific pentasaccharide sequence within heparin binds the AT heparin-binding domain → conformational change in AT → RSL extension → P1 Arg393 now optimally positioned for FXa recognition
2. FXa attacks the RSL → acyl-enzyme intermediate → AT conformational collapse → stable AT-FXa complex; heparin released (catalytic cycle)
3. Rate enhancement: ~7×10³ → ~5×10⁶ M⁻¹s⁻¹ (700-fold acceleration)
4. **Only the pentasaccharide** is required for FXa inhibition → **fondaparinux** (synthetic pentasaccharide) selectively inhibits FXa via this mechanism

**Template (bridging) mechanism — thrombin inhibition:**
1. Heparin must simultaneously bind AT (via pentasaccharide) AND thrombin (via an additional electrostatic interaction site, requiring heparin ≥18 saccharide units)
2. Heparin acts as a molecular scaffold bringing AT and thrombin into proximity → dramatically accelerated AT-thrombin encounter → covalent complex
3. Rate enhancement: ~7×10³ → ~2×10⁷ M⁻¹s⁻¹ (~3,000-fold acceleration)
4. Requires heparin chains ≥13-18 saccharides → fondaparinux (5 saccharides) **cannot** inhibit thrombin
5. This explains the LMWH anti-Xa:anti-IIa ratio: shorter LMWH chains (~15 saccharides) can bridge AT-thrombin less efficiently than UFH → predominantly FXa inhibition

**Heparin type comparison:**

| Agent | Chain length | Anti-Xa | Anti-IIa | HIT risk | Monitoring |
|:------|:------------|:-------|:--------|:--------|:----------|
| UFH | 45-50 saccharides (~15 kDa) | Yes | Yes (1:1 ratio) | 0.5-5% | aPTT or anti-Xa |
| Enoxaparin (LMWH) | ~15-18 saccharides (~4.5 kDa) | Yes | Partial (~4:1 ratio) | 0.1-0.5% | Anti-Xa level |
| Fondaparinux | 5 saccharides (1.7 kDa) | Yes (only) | No | ~<0.01% | None (predictable) |
| Argatroban/bivalirudin | — | No | Yes (direct) | 0% (bypass AT) | aPTT or ECT |

## Mechanism

### AT deficiency — clinical presentation

**Hereditary AT deficiency:**
- **Prevalence:** Heterozygous ~1:2,000–5,000; homozygous ~1:500,000 (usually incompatible with survival; stillbirth or early childhood thrombosis)
- **Presentation:** First VTE often provoked (surgery, pregnancy) but earlier in life (25–35 years) than FV Leiden; unprovoked VTE in young patients; recurrent VTE
- **Pregnancy:** Very high-risk — AT levels fall further during pregnancy; LMWH prophylaxis + AT concentrate peri-delivery mandatory
- **Heparin resistance:** AT-deficient patients may require higher-than-expected UFH doses (or fail to anticoagulate); AT concentrate restores heparin responsiveness

**Acquired AT depletion:**
- **Disseminated intravascular coagulation (DIC):** Continuous thrombin generation consumes AT; AT <60% is part of the ISTH DIC scoring criteria
- **Nephrotic syndrome:** AT lost in urine (~58 kDa; below glomerular filtration threshold is disrupted in heavy proteinuria); AT levels 30-60% of normal → significant thrombophilia
- **L-asparaginase therapy:** L-asparaginase (used in ALL treatment) suppresses liver protein synthesis → ↓ AT, fibrinogen, protein C/S → coagulopathy; AT concentrate prophylaxis sometimes used
- **Prolonged UFH therapy:** AT consumption by ongoing heparin-mediated complexes; relevant in cardiopulmonary bypass (up to 40% AT depletion)
- **Liver failure:** ↓ AT synthesis → combined coagulopathy

### AT concentrate in clinical practice

**AT concentrate (Atryn® — recombinant, from transgenic goats; Thrombate III® — plasma-derived):**

| Indication | Goal AT level | Duration |
|:-----------|:-------------|:---------|
| AT deficiency + surgery | >120% intraoperative → >80% postoperative | Until ambulation/full anticoagulation |
| AT deficiency + obstetric delivery | >80-100% during labor/delivery | 2-3 days postpartum |
| Heparin resistance (acquired AT depletion) | >80% | Until heparin responsiveness restored |
| Sepsis-DIC (investigational) | >150% | No proven mortality benefit (KyberSept trial) |

**KyberSept Trial (2001):** AT concentrate 30,000 IU over 4 days vs. placebo in severe sepsis-DIC → no 28-day mortality reduction overall; significant bleeding increase in patients receiving heparin — illustrates that AT supplementation in sepsis-DIC has limited clinical benefit.

### Monitoring AT activity

- **Chromogenic assay (functional):** Preferred; measures AT inhibition of excess thrombin or FXa; not affected by immunologic AT variants
- **Immunological assay:** Measures AT antigen; misses type IIa/IIb variants where AT antigen is normal but activity reduced
- **Reference range:** 80–120% of normal plasma; <80% = mild deficiency; <60% = significant; <30% = severe (critical care context)
- **When to test:** After acute VTE resolved and ≥3 months off anticoagulation (acute thrombosis and anticoagulants confound AT levels)

## Connections

- `connects-to` → **[Thrombin](../thrombin/README.md)** — Antithrombin is the primary physiological inhibitor of thrombin (FIIa): AT forms a covalent suicide complex with thrombin → irreversible inhibition; rate constant 7×10³ M⁻¹s⁻¹ without heparin, accelerated ~1000× with UFH (heparin template effect).
- `connects-to` → **[Venous Thromboembolism](../../07-system/venous-thromboembolism/README.md)** — AT deficiency (type I: ↓ quantity; type II: ↓ function) is the most severe inherited thrombophilia (25-50× lifetime VTE risk); heterozygous AT deficiency: 1:2,000-5,000 prevalence; AT concentrate needed when UFH fails in AT-deficient patients.
- `connects-to` → **[Inherited Thrombophilia](../../07-system/inherited-thrombophilia/README.md)** — AT deficiency carries 25-50× lifetime VTE risk; type IIa reactive-site mutations (Arg393His) most thrombogenic; combined AT + FV Leiden → very high VTE risk; functional AT activity assay (not immunologic) required for diagnosis.
- `connects-to` → **[Disseminated Intravascular Coagulation](../../07-system/disseminated-intravascular-coagulation/README.md)** — AT is consumed in DIC by ongoing thrombin generation; AT levels <60% correlate with DIC severity (ISTH DIC score); AT concentrate studied in sepsis-DIC (KyberSept trial: no mortality benefit); low AT + prolonged PT + thrombocytopenia = DIC triad.
- `connects-to` → **[Heparin-Induced Thrombocytopenia](../../07-system/heparin-induced-thrombocytopenia/README.md)** — UFH and LMWH exert anticoagulant effects via AT (heparin binds AT → conformational change → 1000× accelerated thrombin/FXa inhibition); in HIT, heparin must be stopped; direct thrombin inhibitors (argatroban, bivalirudin) bypass AT entirely.

[^bauer-2001-thrombophilias]: Bauer KA. The thrombophilias: well-defined risk factors with uncertain therapeutic implications. *Ann Intern Med.* 2001;135(5):367-373. [doi:10.7326/0003-4819-135-5-200109040-00015](https://doi.org/10.7326/0003-4819-135-5-200109040-00015) · [PubMed 11529699](https://pubmed.ncbi.nlm.nih.gov/11529699/)
[^hirsh-2008-parenteral-anticoagulants]: Hirsh J, Bauer KA, Donati MB, et al. Parenteral anticoagulants: American College of Chest Physicians Evidence-Based Clinical Practice Guidelines (8th Edition). *Chest.* 2008;133(6 Suppl):141S-159S. [doi:10.1378/chest.08-0689](https://doi.org/10.1378/chest.08-0689) · [PubMed 18574271](https://pubmed.ncbi.nlm.nih.gov/18574271/)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
