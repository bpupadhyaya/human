---
schema: medicine-entry/v1
id: ashwagandha
name: Ashwagandha
atlas: 03-medicine
scale: 02-traditional
status: draft
last_reviewed: 2026-06-05
summary: "Withania somnifera (ashwagandha). Ayurvedic rasayana adaptogen. Active withanolides reduce cortisol by 14–32% (RCT), improve anxiety (GAD-7 −6 points), and increase testosterone/VO₂max in trials. Also used in Unani (asgandh). GABA-A receptor modulation proposed mechanism."
aliases: ["ashwagandha", "Withania somnifera", "Indian ginseng", "winter cherry", "asgandh", "ajagandha", "kanaje Hindi", "WS", "KSM-66", "Sensoril"]
sources:
  - id: chandrasekhar-2012-ashwagandha-stress
    type: peer-reviewed
    cite: "Chandrasekhar K, Kapoor J, Anishetty S. A prospective, randomized double-blind, placebo-controlled study of safety and efficacy of a high-concentration full-spectrum extract of ashwagandha root in reducing stress and anxiety in adults. Indian J Psychol Med. 2012;34(3):255-62."
    doi: "10.4103/0253-7176.106022"
    pmid: "23439798"
    url: "https://doi.org/10.4103/0253-7176.106022"
  - id: pratte-2014-ashwagandha-anxiety-review
    type: peer-reviewed
    cite: "Pratte MA, Nanavati KB, Young V, Morley CP. An alternative treatment for anxiety: a systematic review of human trial results reported for the Ayurvedic herb ashwagandha (Withania somnifera). J Altern Complement Med. 2014;20(12):901-8."
    doi: "10.1089/acm.2014.0177"
    pmid: "25405876"
    url: "https://doi.org/10.1089/acm.2014.0177"
  - id: wankhede-2015-ashwagandha-muscle
    type: peer-reviewed
    cite: "Wankhede S, Langade D, Joshi K, et al. Examining the effect of Withania somnifera supplementation on muscle strength and recovery: a randomized controlled trial. J Int Soc Sports Nutr. 2015;12:43."
    doi: "10.1186/s12970-015-0104-9"
    pmid: "26609282"
    url: "https://doi.org/10.1186/s12970-015-0104-9"
cross_links:
  - target: 01-human/03-molecular/cortisol
    relation: modulates
    evidence: chandrasekhar-2012-ashwagandha-stress
    note: "Root extract standardised to withanolides reduces serum cortisol by 14–32% in placebo-controlled RCTs; mechanism involves withanolide action on the hypothalamic-pituitary-adrenal axis, suppressing corticotropin-releasing hormone (CRH) signalling and reducing adrenocortical sensitivity. DHEA-S is preserved or increased, suggesting selective modulation rather than adrenal suppression."
  - target: 01-human/07-system/nervous-system
    relation: modulates
    evidence: pratte-2014-ashwagandha-anxiety-review
    note: "Adaptogen: modulates the HPA axis and autonomic nervous system. Withanolides (particularly withaferin A and withanolide D) have GABA-mimetic activity at GABA-A receptors, reducing neuronal excitability. RCTs show reductions in anxiety scales (GAD-7, Hamilton Anxiety Scale). Triethylene glycol found in leaf extract contributes to sleep induction in animal models."
  - target: 01-human/07-system/immune-system
    relation: treats
    evidence: pratte-2014-ashwagandha-anxiety-review
    note: "Ayurvedic rasayana use includes immune enhancement. Withanolides enhance NK cell activity, macrophage phagocytosis, and IFN-γ production in human studies. Withaferin A inhibits NF-κB in macrophages — a dual immunomodulatory (enhancing innate, dampening excessive inflammatory) profile consistent with rasayana rejuvenation protocols. Note: clinical immunology data are less robust than cortisol data."
  - target: 01-human/04-cellular/macrophage
    relation: modulates
    note: "Withanolides enhance macrophage phagocytic activity, NK cytotoxicity, and IFN-γ (rasayana innate enhancement); withaferin A inhibits IKKβ → NF-κB suppression → reduced TNF-α/IL-6/IL-1β; dual immunostimulatory + anti-inflammatory profile consistent with Ayurvedic rasayana use."
  - target: 01-human/03-molecular/nf-kb
    relation: inhibits
    note: "Withaferin A inhibits IKKβ (IκB kinase β) → blocks NF-κB nuclear translocation → reduced transcription of TNF-α, IL-6, IL-1β, and COX-2; also binds Hsp90 and disrupts pro-inflammatory signalling scaffolds; primary anti-inflammatory mechanism in vitro and animal models."
  - target: 01-human/03-molecular/testosterone
    relation: modulates
    note: "Ashwagandha 600 mg/day KSM-66 (8 weeks) raises serum testosterone ~15% and LH ~34% in males with low-normal levels; mechanism: reduced cortisol relieves Leydig cell testosterone suppression; also reduces exercise-induced creatine kinase and improves VO₂max (Wankhede 2015 JISSN)."
---

# Ashwagandha

## Overview

**Ashwagandha** (*Withania somnifera*, family Solanaceae) is a small woody shrub native to the Indian subcontinent, North Africa, and the Mediterranean. It has been used in **Ayurvedic medicine** for over 3,000 years as a *rasayana* — a rejuvenative tonic intended to promote longevity, vitality, and resilience. The Sanskrit name *ashwagandha* ("smell of horse") refers both to the root's odour and to the traditional belief that the herb imparts the strength and vitality of a horse.

The plant is also known in **Unani medicine** as *asgandh* and is used across North African and Middle Eastern herbal traditions. In contemporary Western markets it is one of the best-selling herbal supplements, with primary uses marketed around stress, sleep, and athletic performance.

**Active constituents** are concentrated in the root and to a lesser extent leaves:
- **Withanolides** — a class of steroidal lactones (C₂₈) unique to *Withania* spp; >40 identified, including withaferin A, withanolide A, withanolide D, and withanoside IV/VI as most pharmacologically characterised
- **Alkaloids** — isopelletierine, anaferine, cuseohygrine, anahygrine
- **Saponins** (sitoindosides VII–X) — contribute to adaptogenic and immunomodulatory effects
- **Triethylene glycol** — identified in leaf extracts; sleep-promoting effects in mice

Commercial extracts are standardised by withanolide content: **KSM-66** (5% withanolides, root only), **Sensoril** (10% withanolides, root + leaf), and **Shoden** (35% withanosides + withanolides) are the most clinically studied proprietary forms.

## Mechanism

### HPA Axis and Cortisol Modulation

Withanolides structurally resemble glucocorticoids (steroidal backbone) and have been proposed to act at multiple nodes of the hypothalamic-pituitary-adrenal (HPA) axis:

1. **Hypothalamic level:** Animal studies show reduced CRH (corticotropin-releasing hormone) expression in the paraventricular nucleus under chronic stress conditions with ashwagandha treatment; the precise receptor mediating this is not confirmed in humans
2. **Adrenal level:** Withanolides reduce cortisol secretion from adrenocortical cells in vitro; whether this constitutes true adrenal suppression or normalisation of excessive output is debated — DHEA-S levels are maintained or increased in RCTs, suggesting selective modulation
3. **Net effect in RCTs:** Serum cortisol reduced **14–32%** from baseline compared with placebo in participants with chronic stress [^chandrasekhar-2012-ashwagandha-stress]

### GABAergic and Anxiolytic Mechanisms

- Withanolides bind GABA-A receptors with modest affinity, mimicking the anxiolytic effects of benzodiazepines without the addiction liability; the binding site is distinct from the benzodiazepine allosteric site (α-subunit rather than α/γ interface)
- Withaferin A inhibits **GABA transaminase** (GABA-T), the enzyme that degrades GABA, increasing synaptic GABA availability
- Withanoside IV promotes axon and dendrite regeneration in hippocampal neurons and reverses memory deficits in scopolamine-treated mice — a proposed neuroprotective mechanism

### Anti-inflammatory and Immunomodulatory Mechanisms

- Withaferin A inhibits **IKKβ** (IκB kinase β), suppressing NF-κB nuclear translocation → reduced transcription of TNF-α, IL-6, IL-1β, COX-2
- Paradoxically, ashwagandha also enhances innate immunity: increases NK cell cytotoxicity, macrophage phagocytic activity, and IFN-γ production — consistent with immunomodulation rather than simple immunosuppression
- Withanolides bind **Hsp90** and inhibit its ATPase activity, disrupting pro-inflammatory signalling scaffolds

### Testosterone and Physical Performance

- In male participants with low-to-normal testosterone, ashwagandha (600 mg/day KSM-66, 8 weeks) increased serum testosterone by **~15%** and LH by ~34% in one RCT; proposed mechanism is cortisol-mediated inhibition of Leydig cell testosterone synthesis — reducing cortisol relieves this suppression
- Creatine kinase recovery is improved, suggesting reduced exercise-induced muscle damage; direct anabolic mechanisms (myostatin inhibition) proposed but not confirmed in humans [^wankhede-2015-ashwagandha-muscle]

## Clinical Use

### Indications and Dosing

| Indication | Dose (standardised extract) | Duration studied | Evidence quality |
|:---|:---|:---|:---|
| Chronic stress / anxiety | 300–600 mg/day (5% withanolides) | 8–12 weeks | Moderate (several RCTs) |
| Sleep quality | 300–600 mg/day (KSM-66) | 8–10 weeks | Moderate |
| Athletic performance / VO₂max | 500–600 mg/day | 8–12 weeks | Moderate |
| Testosterone / male fertility | 675 mg/day (root) | 90 days | Low-moderate |
| Thyroid (subclinical hypothyroidism) | 600 mg/day | 8 weeks | Low (single trial) |

**Traditional Ayurvedic dosing:** 3–6 g of raw root powder per day (*churna*) taken with milk, honey, or ghee; significantly higher dose than modern extracts, but withanolide content of raw powder (~0.1–0.5%) is much lower than standardised extracts.

### Formulations

- **Root powder** (*churna*): traditional form; 3–6 g/day
- **Aqueous root extract** (standardised to withanolides): KSM-66 (5%), Sensoril (10%), Shoden (35%)
- **Ashwagandha ghrita**: root extract in clarified butter — traditional lipid formulation that may improve bioavailability (withanolides are lipophilic)

### Safety and Drug Interactions

- Generally well-tolerated at doses ≤600 mg/day; most common side effects are GI upset, drowsiness, loose stools
- **Thyroid interactions:** Ashwagandha elevates T3 and T4 in euthyroid subjects in one trial; **caution in hyperthyroidism or patients on levothyroxine**
- **Sedative potentiation:** Additive CNS depression with benzodiazepines, barbiturates, alcohol; clinical significance unclear at standard doses
- **Immunosuppressant interactions:** Theoretical antagonism (immunoenhancing effects); avoid in transplant patients on calcineurin inhibitors without medical supervision
- **Pregnancy:** Contraindicated — traditionally used as an abortifacient; uterotonic activity in animal models
- **Autoimmune disease:** Use with caution — immunostimulatory effects could theoretically exacerbate autoimmune flares; human data lacking
- Rare cases of liver injury (5 published case reports 2019–2023, all with other confounders); FDA has not issued a warning but cases highlight monitoring need in high-dose use

## Evidence

### Key RCTs and Systematic Reviews

**Stress and anxiety (primary evidence base):**

Chandrasekhar et al. (2012) [^chandrasekhar-2012-ashwagandha-stress] — double-blind RCT, n=64, KSM-66 300 mg twice daily vs placebo for 60 days in chronically stressed adults:
- Serum cortisol: **−27.9%** (treatment) vs. **−7.9%** (placebo); p<0.0001
- PSS (Perceived Stress Scale): −44.0% vs. −5.9%; p<0.0001
- Serum CRP: significant reduction; anxiety scales improved
- **Limitation:** Single site, industry-adjacent investigators; short follow-up; proprietary extract

Pratte et al. (2014) systematic review [^pratte-2014-ashwagandha-anxiety-review] — 5 human trials meeting inclusion criteria:
- Consistent improvement in stress, anxiety, and fatigue outcomes across trials
- GRADE assessment: **Low to Moderate** — all trials have risk of bias concerns (small n, industry funding, heterogeneous populations)

**Athletic performance:**

Wankhede et al. (2015) [^wankhede-2015-ashwagandha-muscle] — RCT, n=57 young men, 300 mg KSM-66 twice daily × 8 weeks:
- Bench press 1-RM: +46.0 kg (treatment) vs. +26.4 kg (placebo); p=0.001
- Leg extension 1-RM: +14.5 kg vs. +9.8 kg; p=0.04
- Serum testosterone: +96.2 ng/dL vs. +18.0 ng/dL; p=0.004
- **Limitation:** Relatively small n; industry-funded; effect sizes are large and warrant independent replication

**Evidence gaps:**
- Long-term safety (>6 months) has not been formally evaluated in RCTs
- Mechanisms in humans remain largely extrapolated from animal studies
- Most RCTs use proprietary standardised extracts; traditional raw-root-powder preparations have minimal clinical trial data
- No head-to-head comparisons with established anxiolytics or adaptogens

## Connections

- **Modulates** → [Cortisol](../../../../../01-human/03-molecular/cortisol/README.md): Withanolides act on the HPA axis, reducing cortisol output by 14–32% in stress RCTs. The mechanism likely involves HPA sensitisation modulation and direct adrenocortical effects, while preserving or increasing DHEA-S — suggesting normalisation of dysregulated stress responses rather than blanket adrenal suppression.

- **Modulates** → [Nervous System](../../../../../01-human/07-system/nervous-system/README.md): GABAergic activity (GABA-A partial agonism, GABA-T inhibition), HPA axis normalisation, and neuroprotective withanosides collectively explain anxiolytic, sleep-promoting, and neuroprotective effects observed in trials. These mechanisms are better characterised in animal models; direct human neuroimaging evidence is limited.

- **Treats** → [Immune System](../../../../../01-human/07-system/immune-system/README.md): Ayurvedic rasayana use aligns with a dual immunomodulatory profile — enhancing innate surveillance (NK cells, macrophage phagocytosis, IFN-γ) while dampening excessive NF-κB-driven inflammation via withaferin A. Clinical immunology data are less robust than the stress and performance evidence base; most immune studies are small and preclinical.
- `modulates` → **[Macrophage](../../../../../01-human/04-cellular/macrophage/README.md)** — Withanolides enhance macrophage phagocytic activity, NK cytotoxicity, and IFN-γ (rasayana innate enhancement); withaferin A inhibits IKKβ → NF-κB suppression → reduced TNF-α/IL-6/IL-1β; dual immunostimulatory + anti-inflammatory profile consistent with Ayurvedic rasayana use.
- `inhibits` → **[NF-κB](../../../../../01-human/03-molecular/nf-kb/README.md)** — Withaferin A inhibits IKKβ → blocks NF-κB nuclear translocation → reduced TNF-α, IL-6, IL-1β, COX-2 transcription; also binds Hsp90 and disrupts pro-inflammatory signalling scaffolds; the primary anti-inflammatory mechanism in vitro and animal models.
- `modulates` → **[Testosterone](../../../../../01-human/03-molecular/testosterone/README.md)** — Ashwagandha 600 mg/day KSM-66 (8 weeks) raises serum testosterone ~15% and LH ~34% in males with low-normal levels; mechanism: reduced cortisol relieves Leydig cell testosterone suppression; also reduces exercise-induced creatine kinase and improves VO₂max (Wankhede 2015 JISSN).

[^chandrasekhar-2012-ashwagandha-stress]: Chandrasekhar K et al. Indian J Psychol Med. 2012;34(3):255-62. doi:10.4103/0253-7176.106022
[^pratte-2014-ashwagandha-anxiety-review]: Pratte MA et al. J Altern Complement Med. 2014;20(12):901-8. doi:10.1089/acm.2014.0177
[^wankhede-2015-ashwagandha-muscle]: Wankhede S et al. J Int Soc Sports Nutr. 2015;12:43. doi:10.1186/s12970-015-0104-9

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
