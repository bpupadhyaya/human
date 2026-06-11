---
schema: human-scale-entry/v1
id: opioid-use-disorder
name: Opioid Use Disorder
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-08
summary: "Opioid use disorder (~2.7M US; ~80K deaths/year fentanyl) involves μ-opioid-mediated VTA disinhibition → NAcc dopamine surge, tolerance, and LC rebound withdrawal; MOUD: buprenorphine, methadone, naltrexone; naloxone reverses overdose."
aliases: ["opioid use disorder", "OUD", "heroin addiction", "opioid dependence", "buprenorphine", "methadone", "naltrexone", "Suboxone", "MOUD", "COWS", "opioid overdose", "naloxone", "fentanyl"]
sources:
  - id: volkow-2016-opioid-crisis
    type: peer-reviewed
    cite: "Volkow ND, Collins FS. The role of science in addressing the opioid crisis. N Engl J Med. 2017;377(4):391-394."
    doi: "10.1056/NEJMsr1706626"
    pmid: "28723324"
    url: "https://doi.org/10.1056/NEJMsr1706626"
    accessed: "2026-06-08"
  - id: mattick-2009-bupe-meta
    type: peer-reviewed
    cite: "Mattick RP, Breen C, Kimber J, Davoli M. Buprenorphine maintenance versus placebo or methadone maintenance for opioid dependence. Cochrane Database Syst Rev. 2014;2:CD002207."
    doi: "10.1002/14651858.CD002207.pub4"
    pmid: "24500948"
    url: "https://doi.org/10.1002/14651858.CD002207.pub4"
    accessed: "2026-06-08"
  - id: kreek-2002-opioid-neuroscience
    type: peer-reviewed
    cite: "Kreek MJ, Koob GF. Drug dependence: stress and dysregulation of brain reward pathways. Drug Alcohol Depend. 1998;51(1-2):23-47."
    doi: "10.1016/S0376-8716(98)00064-7"
    pmid: "9716926"
    url: "https://doi.org/10.1016/S0376-8716(98)00064-7"
    accessed: "2026-06-08"
cross_links:
  - target: 01-human/03-molecular/dopamine
    relation: connects-to
    note: "μ-opioid receptor activation on VTA GABAergic interneurons → disinhibition → increased VTA DA firing → NAcc dopamine surge → euphoria; chronic use → reward circuit hypofunction → anhedonia; naltrexone (MOR antagonist) blocks this disinhibition → reduces opioid reward."
  - target: 01-human/03-molecular/gaba
    relation: connects-to
    note: "μ-opioid receptors on VTA GABAergic interneurons mediate euphoric disinhibition; chronic opioid → tolerance at MOR on GABA interneurons → blunted inhibition; buprenorphine (partial MOR agonist) provides stable DA tone without the high-reinforcement surge of full agonists."
  - target: 01-human/03-molecular/glutamate
    relation: connects-to
    note: "Chronic opioid potentiates corticostriatal glutamatergic synapses → LTP underlying craving and drug-cue reactivity; AMPA receptor upregulation in NAcc drives relapse-associated excitability; mGluR5 antagonists reduce cue-triggered reinstatement of opioid seeking in rodents."
  - target: 01-human/03-molecular/bdnf
    relation: connects-to
    note: "Chronic opioid drives ΔFosB accumulation in NAcc → altered BDNF expression and reward circuit plasticity; BDNF in VTA sensitizes opioid-induced reinforcement; withdrawal-phase BDNF surge in NAcc contributes to aversion; BDNF/TrkB signaling is a therapeutic target in relapse."
  - target: 01-human/03-molecular/norepinephrine
    relation: connects-to
    note: "μ-opioid receptors on LC suppress NE during opioid use; abrupt cessation → LC rebound → excess NE → withdrawal (diaphoresis, piloerection, tachycardia, diarrhea, anxiety); clonidine and lofexidine (α2 agonists) reduce LC hyperactivation and are FDA-approved for opioid withdrawal."
  - target: 01-human/06-organ/brain
    relation: targets
    note: "OUD remodels VTA-NAcc reward circuits (MOR disinhibition), LC (NE rebound withdrawal), PFC control circuits (craving-driven approach), and amygdala (conditioned fear of withdrawal); buprenorphine and naltrexone normalize these circuit abnormalities over months of treatment."
  - target: 01-human/03-molecular/mu-opioid-receptor
    relation: connects-to
    note: "Opioid use disorder centers on the μ-opioid receptor: on VTA GABA interneurons it disinhibits dopamine, on the locus coeruleus it sets up rebound withdrawal, and in the brainstem it drives respiratory depression — the target of buprenorphine, methadone, and naloxone."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "Injecting opioids seeds the bloodstream with skin and needle bacteria, which lodge on heart valves — classically the tricuspid — to cause infective endocarditis, a high-mortality complication of injection drug use that may need valve surgery alongside OUD treatment."
  - target: 01-human/07-system/stimulant-use-disorder
    relation: connects-to
    note: "Opioid and stimulant use disorders share the VTA-NAcc dopamine reward circuitry but pull in opposite directions, and are increasingly fatal together: 'speedball' combinations and fentanyl-contaminated stimulants drive a rising share of overdose deaths."
---

# Opioid Use Disorder

## Overview

**Opioid use disorder (OUD)** is a chronic, relapsing condition characterized by compulsive opioid use despite harmful consequences. It represents one of the most lethal substance use disorders: in the US, opioid-related overdose deaths have risen to approximately **80,000/year** (2022), primarily driven by illicitly manufactured fentanyl and fentanyl analogs — a 9-fold increase since 1999 and now the leading cause of death in Americans aged 18–45.

**Epidemiology:**
- ~2.7 million Americans with OUD (DSM-5); global opioid misuse ~56 million
- Heroin use disorder: ~750,000; prescription opioid use disorder: ~2 million; overlap significant
- Fentanyl now present in >80% of heroin samples in the US — most overdose deaths involve fentanyl
- Overdose mortality: ~80,000/year US (2022); naloxone has reversed >300,000 overdoses
- Treatment gap: Only ~20% of people with OUD receive medication-assisted treatment (MOUD)

**Opioids of abuse:**
- **Heroin:** Diacetylmorphine; rapid onset IV/nasal → euphoria; short half-life (~3h) → withdrawal within 6-12h
- **Fentanyl:** 50-100× more potent than morphine; illicit supply ("pressed pills") has replaced heroin; carfentanil (10,000× morphine): veterinary agent used as adulterant
- **Prescription opioids:** Oxycodone (OxyContin), hydrocodone (Vicodin), oxymorphone, hydromorphone, morphine; diverted or obtained via pill mills
- **Buprenorphine:** Partial agonist; used for treatment; ceiling effect on respiratory depression
- **Methadone:** Full agonist; used for treatment; long half-life; QTc risk

**DSM-5 Criteria:** Same 11-criterion framework as AUD, applied to opioids; ≥2 in 12 months; physiological indicators (tolerance, withdrawal) count toward mild even when prescribed medically (with important caveats for pain management patients).

**COWS (Clinical Opioid Withdrawal Scale):** 11-item bedside tool (heart rate, sweating, gooseflesh, pupil size, yawning, anxiety, GI, tremor, restlessness, bone/joint ache, cold/hot flashes); score 5-12: mild; 13-24: moderate; 25-36: moderately severe; ≥37: severe.

## Structure

### Opioid receptor biology

**Three main opioid receptor subtypes (GPCRs):**

| Receptor | Gene | Coupling | Endogenous ligands | Key locations | Effects |
|:---|:---|:---|:---|:---|:---|
| **μ (MOR)** | OPRM1 | Gi/Go → ↓cAMP, GIRK K⁺, ↓VGCC | β-endorphin, endomorphin | VTA, NAcc, LC, amygdala, PAG, dorsal horn | Euphoria, analgesia, respiratory depression |
| **κ (KOR)** | OPRK1 | Gi → ↓cAMP | Dynorphin | Striatum, limbic system, spinal cord | Dysphoria, analgesia, psychomimetic effects |
| **δ (DOR)** | OPRD1 | Gi | Enkephalins | Cortex, basal ganglia, limbic | Mood, reward, analgesia |

**MOR signaling (Gi-coupled):**
1. Inhibits adenylyl cyclase → ↓cAMP → reduced PKA activity
2. Activates GIRK K⁺ channels → hyperpolarization → reduced neuronal firing
3. Inhibits voltage-gated Ca²⁺ channels → reduced neurotransmitter release
4. **Arrestin pathway:** β-arrestin recruitment → receptor desensitization → endocytosis → tolerance

### VTA disinhibition mechanism

The primary mechanism by which opioids produce euphoria:

1. **Baseline:** GABAergic interneurons in VTA tonically suppress DA neuron firing via MOR on GABA interneurons
2. **Opioid administration:** MOR activation on GABA interneurons → Gi → hyperpolarizes GABA interneurons → reduces GABA release → VTA DA neurons are **disinhibited** → increased firing
3. **NAcc:** Elevated VTA DA firing → increased NAcc DA release → D1/D2 stimulation → euphoria, reinforcement
4. **Acute effect:** High-amplitude DA surge (heroin/fentanyl) >> natural rewards → powerful positive reinforcement

### Tolerance and dependence mechanisms

**Tolerance:**
- Chronic MOR activation → GRK (G protein-coupled receptor kinase) phosphorylation → β-arrestin recruitment → MOR desensitization and internalization
- Adenylyl cyclase **superactivation** (compensatory upregulation) → elevated cAMP baseline; requires increasing doses to achieve same inhibition
- Results in the same MOR-activating dose producing progressively less effect

**Physical dependence and withdrawal:**
- **LC hyperactivation:** During opioid use, MOR on LC neurons → Gi → suppressed cAMP → suppressed LC firing → reduced NE; adenylyl cyclase superactivation occurs; abrupt cessation → cAMP surge → LC hyperactivation → NE storm → withdrawal syndrome
- Withdrawal timeline:
  - **Short-acting opioids (heroin, oxycodone):** Onset 6-12h after last use; peak 36-72h; resolution 5-7 days
  - **Long-acting opioids (methadone):** Onset 24-48h; peak 72-96h; resolution 10-21 days

**Opioid overdose mechanism:**
- MOR in brainstem (pre-Bötzinger complex): respiratory rhythm generator; MOR activation → hyperpolarization → respiratory depression → death
- **Fentanyl:** Highly lipophilic → rapid CNS penetration → faster respiratory depression than heroin; multiple doses of naloxone often required
- **Naloxone (Narcan):** Competitive MOR antagonist; 2-8 mg intranasal or 0.4-2 mg IM; onset 1-2 min; duration 30-90 min (shorter than fentanyl) → repeat dosing required

## Function

### Reward circuit alterations in OUD

**Positive reinforcement → Negative reinforcement transition (Koob model):**

**Early OUD (positive reinforcement):**
- Opioid → VTA DA disinhibition → NAcc DA surge → euphoria ("high")
- Extended amygdala NOT yet dominant; goal is to achieve pleasure

**Chronic OUD (negative reinforcement — more clinically important):**
- Reward threshold rises (tolerance); same dose produces less euphoria
- Abstinence → **withdrawal dysphoria** — anhedonia, anxiety, dysphoria (kappa-opioid-mediated dynorphin release from NAcc neurons suppresses dopamine)
- **Drinking/using to feel normal** — not for pleasure but to avoid withdrawal
- CRF hyperactivation in CeA (similar to AUD) → anxiety drives opioid-seeking
- This shift from positive to negative reinforcement explains why "willpower" fails — the drug is maintaining homeostasis, not causing pleasure

**Craving and relapse (PFC-limbic imbalance):**
- Drug cues (paraphernalia, people, places) activate OFC → craving → impaired PFC inhibitory control
- Glutamatergic corticostriatal projections are potentiated by chronic opioid use → drug-cue reactivity persists for years
- PFC (dlPFC) hypofunction → impaired inhibitory control over limbic drive
- NAcc glutamate (from PFC/amygdala) during cue exposure triggers reinstatement

## Pathology

### Opioid-related complications

| Complication | Mechanism/Notes |
|:---|:---|
| **Overdose** | Respiratory depression via MOR on pre-Bötzinger; fentanyl: multiple naloxone doses; skin-popping → abscesses |
| **Infective endocarditis** | IV drug use → bacteremia; tricuspid valve most common; Staph aureus; high mortality if untreated |
| **Hepatitis C (HCV)** | Transmitted via needle sharing; 50-80% of PWID (people who inject drugs) HCV-seropositive; DAA therapy (ledipasvir, sofosbuvir) highly effective |
| **HIV** | Needle sharing; 10% of new HIV diagnoses in US linked to injection drug use |
| **Skin and soft tissue infections** | Abscesses, necrotizing fasciitis, wound botulism |
| **Neonatal opioid withdrawal syndrome (NOWS)** | In utero opioid exposure → withdrawal after birth; managed with morphine or methadone; prolonged NICU stays |
| **Opioid-induced hyperalgesia** | Paradoxical increased pain sensitivity with chronic opioid; NR2B NMDA receptor sensitization |
| **Constipation** | Peripheral MOR in GI → reduced motility; methylnaltrexone (peripherally restricted MOR antagonist) treats opioid-induced constipation |

### Treatment — MOUD (Medications for OUD)

**Evidence base:** MOUD reduces opioid use, overdose mortality (~50-70%), HIV/HCV transmission, crime, and improves social functioning [^mattick-2009-bupe-meta].

**Buprenorphine:**
- Partial μ-agonist + κ-antagonist; ceiling effect on respiratory depression (much safer than full agonists)
- **Suboxone** (buprenorphine + naloxone): naloxone prevents IV misuse — inactive sublingually, precipitates withdrawal if injected
- Sublingual or buccal; weekly/monthly injectable (Sublocade) and implants (Probuphine) available
- **Induction:** Start when COWS ≥8-12 (mild-moderate withdrawal); premature induction → precipitated withdrawal; modified low-dose induction (Bernese method) allows starting without prior withdrawal
- Superior to methadone for patient autonomy (office-based); no QTc risk

**Methadone:**
- Full μ-agonist; long half-life (24-36h) → smooth opioid maintenance without peaks
- Dispensed from federally licensed opioid treatment programs (OTPs) — requires daily attendance initially
- QTc prolongation (baseline ECG required); drug interactions via CYP3A4
- Highly effective for severe OUD, patients who fail buprenorphine, or pregnant women (reduces NOWS severity vs. illicit use)

**Naltrexone (extended-release injectable, Vivitrol):**
- Competitive MOR antagonist; monthly injection → ~100% compliance during injection period
- No abuse potential; no dependency; no diversion risk
- Requires opioid-free period (7 days short-acting; 10-14 days long-acting/methadone) before induction — barrier in US system
- Equally effective to buprenorphine when initiated; inferior retention rate due to induction challenge

**Naloxone (harm reduction):**
- Broad OTC availability (US 2023); co-prescribed with opioids; community distribution programs
- 4mg IN formulation (Narcan); 8mg IN (Kloxxado) for fentanyl; 10mg autoinjector
- Take-home naloxone programs: 2-3 doses recommended given high fentanyl naloxone resistance

**Psychosocial treatments:**
- **Contingency management (CM):** Voucher-based or monetary incentives for opioid-negative urine screens; strongest evidence base in SUD treatment (effect sizes d=0.5-0.8); not widely implemented due to funding barriers
- **Motivational interviewing (MI):** Enhances readiness to engage in treatment
- **12-step (NA, Narcotics Anonymous):** Abstinence-only model; limited evidence vs. MOUD; some conflict between NA culture and MOUD acceptance
- **Recovery housing:** Peer support; medication-friendly environments reduce relapse risk

**Harm reduction (beyond naloxone):**
- Syringe services programs (SSPs): Reduce HIV/HCV; link to treatment; legally complex
- Supervised consumption sites (SCS): North America (Vancouver, Toronto, New York 2021); no overdose deaths on site; reduce emergency department visits
- Fentanyl test strips: detect fentanyl contamination; reduce overdose risk; legal in most US states
- Medication-assisted low-threshold access (vending machines, telemedicine prescribing): Increase treatment uptake

## Connections

- `connects-to` → **[Dopamine](../../../03-molecular/dopamine/README.md)** — μ-opioid receptor activation on VTA GABAergic interneurons → disinhibition → increased VTA DA firing → NAcc dopamine surge → euphoria; chronic use → reward hypofunction → anhedonia; naltrexone (MOR antagonist) blocks this disinhibition → reduces opioid reward.

- `connects-to` → **[GABA](../../../03-molecular/gaba/README.md)** — μ-opioid receptors on VTA GABAergic interneurons mediate euphoric disinhibition; chronic opioid → tolerance at MOR on GABA interneurons; buprenorphine (partial MOR agonist) provides stable DA tone without the high-reinforcement surge of full agonists.

- `connects-to` → **[Glutamate](../../../03-molecular/glutamate/README.md)** — chronic opioid potentiates corticostriatal glutamatergic synapses → LTP underlying craving and drug-cue reactivity; AMPA receptor upregulation in NAcc drives relapse-associated excitability; mGluR5 antagonists reduce cue-triggered reinstatement of opioid seeking in rodents.

- `connects-to` → **[BDNF](../../../03-molecular/bdnf/README.md)** — chronic opioid drives ΔFosB accumulation in NAcc → altered BDNF expression and reward circuit plasticity; BDNF in VTA sensitizes opioid-induced reinforcement; withdrawal-phase BDNF surge in NAcc contributes to aversion; BDNF/TrkB signaling is a therapeutic target in relapse prevention.

- `connects-to` → **[Norepinephrine](../../../03-molecular/norepinephrine/README.md)** — μ-opioid receptors on LC suppress NE during opioid use; abrupt cessation → LC rebound → excess NE → withdrawal (diaphoresis, piloerection, tachycardia, diarrhea, anxiety); clonidine and lofexidine (α2 agonists) reduce LC hyperactivation and are FDA-approved for opioid withdrawal.

- `targets` → **[Brain](../../../06-organ/brain/README.md)** — OUD remodels VTA-NAcc reward circuits (MOR disinhibition), LC (NE rebound withdrawal), PFC control circuits (craving-driven approach behavior), and amygdala (conditioned fear of withdrawal); buprenorphine and naltrexone normalize these circuit abnormalities over months of treatment.

- `connects-to` → **[Mu-Opioid Receptor](../../03-molecular/mu-opioid-receptor/README.md)** — Opioid use disorder centers on the μ-opioid receptor: on VTA GABA interneurons it disinhibits dopamine, on the locus coeruleus it sets up rebound withdrawal, and in the brainstem it drives respiratory depression — the target of buprenorphine, methadone, and naloxone.

- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — Injecting opioids seeds the bloodstream with skin and needle bacteria, which lodge on heart valves — classically the tricuspid — to cause infective endocarditis, a high-mortality complication of injection drug use that may need valve surgery alongside OUD treatment.

- `connects-to` → **[Stimulant Use Disorder](../stimulant-use-disorder/README.md)** — Opioid and stimulant use disorders share the VTA-NAcc dopamine reward circuitry but pull in opposite directions, and are increasingly fatal together: 'speedball' combinations and fentanyl-contaminated stimulants drive a rising share of overdose deaths.

[^volkow-2016-opioid-crisis]: Volkow ND, Collins FS. The role of science in addressing the opioid crisis. *N Engl J Med.* 2017;377(4):391-394. [doi:10.1056/NEJMsr1706626](https://doi.org/10.1056/NEJMsr1706626) · [PubMed 28723324](https://pubmed.ncbi.nlm.nih.gov/28723324/)
[^mattick-2009-bupe-meta]: Mattick RP, Breen C, Kimber J, Davoli M. Buprenorphine maintenance versus placebo or methadone maintenance for opioid dependence. *Cochrane Database Syst Rev.* 2014;2:CD002207. [doi:10.1002/14651858.CD002207.pub4](https://doi.org/10.1002/14651858.CD002207.pub4) · [PubMed 24500948](https://pubmed.ncbi.nlm.nih.gov/24500948/)
[^kreek-2002-opioid-neuroscience]: Kreek MJ, Koob GF. Drug dependence: stress and dysregulation of brain reward pathways. *Drug Alcohol Depend.* 1998;51(1-2):23-47. [doi:10.1016/S0376-8716(98)00064-7](https://doi.org/10.1016/S0376-8716(98)00064-7) · [PubMed 9716926](https://pubmed.ncbi.nlm.nih.gov/9716926/)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
