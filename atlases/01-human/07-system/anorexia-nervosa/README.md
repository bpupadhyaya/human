---
schema: human-scale-entry/v1
id: anorexia-nervosa
name: Anorexia Nervosa
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-08
summary: "Anorexia nervosa (0.9% female lifetime; highest mortality of any psychiatric disorder ~5-10%/decade) involves reward circuit dysregulation, leptin deficiency, cortisol excess, and 5-HT dysregulation; only evidence-based treatment: nutritional rehabilitation + FBT or CBT-E."
aliases: ["anorexia nervosa", "AN", "anorexia", "restrictive AN", "purging AN", "EDE-Q", "EDE", "FBT", "CBT-E", "ARFID", "refeeding syndrome", "amenorrhea", "weight restoration"]
sources:
  - id: treasure-2010-an-lancet
    type: peer-reviewed
    cite: "Treasure J, Claudino AM, Zucker N. Eating disorders. Lancet. 2010;375(9714):583-593."
    doi: "10.1016/S0140-6736(09)61748-7"
    pmid: "19931176"
    url: "https://doi.org/10.1016/S0140-6736(09)61748-7"
    accessed: "2026-06-08"
  - id: lock-2010-fbt-an
    type: peer-reviewed
    cite: "Lock J, Le Grange D, Agras WS, et al. Randomized clinical trial comparing family-based treatment with adolescent-focused individual therapy for adolescents with anorexia nervosa. Arch Gen Psychiatry. 2010;67(10):1025-1032."
    doi: "10.1001/archgenpsychiatry.2010.128"
    pmid: "20921118"
    url: "https://doi.org/10.1001/archgenpsychiatry.2010.128"
    accessed: "2026-06-08"
  - id: frank-2004-an-neuroimaging
    type: peer-reviewed
    cite: "Frank GK, Bailer UF, Henry SE, et al. Increased dopamine D2/D3 receptor binding after recovery from anorexia nervosa measured by positron emission tomography and [11C]raclopride. Biol Psychiatry. 2005;58(11):908-912."
    doi: "10.1016/j.biopsych.2005.05.003"
    pmid: "16005437"
    url: "https://doi.org/10.1016/j.biopsych.2005.05.003"
    accessed: "2026-06-08"
cross_links:
  - target: 01-human/03-molecular/serotonin
    relation: connects-to
    note: "5-HT2A receptor hyperactivation in frontal cortex contributes to heightened harm avoidance and rigidity in AN; 5-HT dysregulation is present pre-morbidly and persists after recovery; olanzapine (5-HT2A antagonist) modestly aids weight gain; SSRIs are ineffective at low weight."
  - target: 01-human/03-molecular/dopamine
    relation: connects-to
    note: "Striatal D2/D3 receptor binding is increased in recovered AN patients (PET), suggesting reduced dopamine tone; anorexia patients show reduced reward salience of food cues (fMRI); altered dopamine reward circuits may explain why food restriction feels 'rewarding' in AN."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Leptin falls sharply with fat mass loss in AN → amenorrhea, bone loss, immune suppression, and cognitive impairment; paradoxically, some AN patients have modestly elevated leptin relative to weight → false satiety signal; normalizes with weight restoration."
  - target: 01-human/03-molecular/cortisol
    relation: connects-to
    note: "HPA axis hyperactivation in AN → elevated cortisol → bone loss (reduced osteoblast activity), impaired cognition, and immune suppression; hypercortisolemia is present even when BMI partially normalizes; normalizes with sustained weight restoration and nutritional rehabilitation."
  - target: 01-human/03-molecular/bdnf
    relation: connects-to
    note: "BDNF Val66Met SNP is associated with severe early-onset AN; BDNF in hypothalamic PVN regulates appetite — low BDNF promotes feeding but high BDNF reduces food intake via TrkB; serum BDNF is reduced in acute AN and partially normalizes with weight restoration."
  - target: 01-human/06-organ/brain
    relation: targets
    note: "AN shows gray matter reduction in OFC, insular cortex, and cingulate; fMRI reveals altered insula processing of food cues and reduced striatal reward responses; OFC hyperactivation drives cognitive rigidity; much gray matter recovers with weight restoration over 1-2 years."
---

# Anorexia Nervosa

## Overview

**Anorexia nervosa (AN)** is a severe, life-threatening psychiatric and medical disorder characterized by restriction of caloric intake relative to needs, intense fear of gaining weight, and distorted body image — leading to significantly low body weight (BMI < 17.5 kg/m² in adults; < 85% expected weight in children/adolescents).

**Epidemiology:**
- Lifetime prevalence: 0.9% in women; 0.3% in men (likely underdiagnosed in males)
- Peak onset: 15–19 years (90% female); second peak in mid-twenties
- Crude mortality rate: ~5–10% per decade of illness — **the highest standardized mortality ratio of any psychiatric disorder** (SMR ~5-10×); 50% from medical complications, 50% from suicide
- Recovery: ~50% full recovery, ~30% partial, ~20% chronic course

**DSM-5 Subtypes:**
1. **Restricting type:** Weight loss via dieting, fasting, exercise only
2. **Binge-purge type:** Weight loss via restriction PLUS binge eating and/or compensatory behaviors (purging, laxatives) at least once/week in past 3 months

**Severity (based on BMI in adults):**
- Mild: BMI ≥ 17
- Moderate: BMI 16–16.99
- Severe: BMI 15–15.99
- Extreme: BMI < 15

**Assessment:**
- **EDE-Q (Eating Disorder Examination Questionnaire):** 28-item self-report; 4 subscales (restraint, eating, weight, shape concern); gold standard for research
- **SCOFF questionnaire:** 5-item brief screen
- Physical examination: lanugo hair, bradycardia, orthostasis, parotid hypertrophy (if purging), dental erosions (if purging), peripheral edema (on refeeding), callused knuckles (Russell's sign, if purging)

## Structure

### Neurobiological circuits in AN

**Reward circuit dysfunction (the "anorexia paradox"):**

In healthy individuals, food cues activate the mesolimbic reward circuit (VTA → NAcc → OFC) → approach motivation → eating. In AN:
- **Striatal hypoactivation** to food stimuli (fMRI): NAcc fails to activate to appetizing foods, or activates to body image-related stimuli instead
- **Increased D2/D3 receptor binding** in striatum of recovered AN patients (PET) [^frank-2004-an-neuroimaging]: suggests chronically low dopamine release → upregulated receptor sensitivity; food restriction may actually reduce aversive interoceptive signals → becomes negatively reinforcing
- **Insula hyperactivation:** The insula (interoceptive cortex) is hyperactivated to food stimuli → exaggerated aversive body-state signals from food → food avoidance reinforced by anxiety reduction
- **OFC hyperactivation:** The orbitofrontal cortex — critical for flexible reward valuation — shows increased activation in AN → rigid overvaluation of thinness and food restriction rules; reduced cognitive flexibility (set-shifting deficits on WCST)

**Serotonin system:**
- 5-HT2A receptor signaling in prefrontal and frontal cortex appears hyperactivated in AN — contributing to heightened harm avoidance, perfectionism, and rigidity (temperamental traits that predate illness and persist after recovery)
- 5-HT1A receptor density is reduced in raphe and cortex (PET studies in recovered AN)
- **Starvation paradox:** Serotonin synthesis requires tryptophan; starvation → reduced plasma tryptophan → reduced 5-HT; this may temporarily reduce 5-HT2A-mediated distress → reinforcing restriction
- SSRIs: INEFFECTIVE in acute AN (too little tryptophan substrate); may be mildly helpful in weight-restored patients for relapse prevention

**Cortisol and HPA axis:**
- Elevated cortisol (plasma + 24h UFC) in proportion to weight loss; partially driven by reduced cortisol clearance (not just increased production)
- CRH elevated in CSF → increased sympathetic tone → drives hyperactivity
- Cortisol → bone loss: reduced osteoblast activity, increased osteoclast activity → osteopenia/osteoporosis even in young patients (a primary medical concern)

**Leptin and metabolic adaptation:**
- Leptin falls precipitously with fat mass loss — triggers "starvation adaptation":
  - Amenorrhea (leptin threshold for LH pulsatility not met → anovulation)
  - Bone loss (leptin regulates osteoblasts)
  - Reduced thyroid hormone (T3) → lowered metabolic rate (protective adaptation)
  - Cognitive impairment
- Paradox: some AN patients show leptin levels modestly elevated relative to their very low body fat percentage — possibly reflecting reduced leptin receptor sensitivity or adipose distribution factors

### Genetics and temperament

- Heritability: ~50–70% for AN (twin studies); strongly genetic relative to environmental factors
- **GWAS 2019 (Watson et al., Nature Genetics):** First significant AN locus on chromosome 12 (12q13.2); genetic correlation with metabolic traits (type 2 diabetes — negative; BMI — inverse); AN shows genetic overlap with schizophrenia, neuroticism, and educational attainment
- **BDNF Val66Met SNP:** Over-represented in severe early-onset AN; BDNF dysregulation in hypothalamic circuits contributes to appetite suppression
- **Temperamental predictors:** Harm avoidance, perfectionism, obsessionality, anxiety pre-date onset by years → trait markers, not state markers

## Function

### Medical complications

| System | Complication | Mechanism |
|:---|:---|:---|
| **Cardiac** | Bradycardia, QTc prolongation, mitral valve prolapse | Low catecholamines; electrolyte abnormalities (K+, Mg2+) |
| **Bone** | Osteopenia/osteoporosis (50-80% of AN patients); stress fractures | Low estrogen + cortisol excess + low IGF-1; irreversible in some |
| **Endocrine** | Hypothalamic amenorrhea; euthyroid sick syndrome (low T3) | Low leptin → GnRH suppression; reduced conversion T4→T3 |
| **Renal** | Hypokalemia (purging); renal failure (dehydration) | Vomiting/laxatives → K+ loss; rhabdomyolysis |
| **Hematologic** | Leukopenia, anemia, thrombocytopenia | Bone marrow hypoplasia (gelatinous marrow transformation) |
| **Neurological** | Cortical atrophy (pseudo-atrophy; partially reversible); peripheral neuropathy | Nutritional deficiency; thiamine; central glucose deprivation |
| **GI** | Gastroparesis; superior mesenteric artery syndrome; constipation | Reduced gut motility; loss of mesenteric fat pad compresses duodenum |

**Refeeding syndrome:** Medical emergency when severely malnourished patients receive rapid nutritional support:
- Cellular phosphate uptake → severe hypophosphatemia → cardiac arrhythmia, respiratory failure, heart failure, seizures
- Prevention: start feeds at 10-20 kcal/kg/day; supplement phosphate, potassium, magnesium; daily electrolytes; slow escalation; ECG monitoring

**Bone health:** Unique to AN vs. other low-weight conditions — AN patients have significantly worse bone density than expected from weight alone, because the estrogen-leptin-IGF-1 triad is disrupted. The only proven bone-protective intervention is weight restoration. Bisphosphonates are NOT recommended (still growing; pregnancy risk later).

## Pathology

### Differential diagnosis

- **ARFID (Avoidant/Restrictive Food Intake Disorder):** Low weight/malnutrition but NO fear of weight gain or distorted body image; driven by sensory aversion, fear of choking/vomiting, or lack of interest in eating
- **MDD with appetite suppression:** Weight loss but distress about low weight (desire to eat more)
- **Medical conditions:** Inflammatory bowel disease, celiac disease, malignancy, diabetes insipidus — exclude with workup before diagnosing AN
- **OCD/anxiety:** Obsessive food rituals overlap; distinguish by content (fear of weight vs. contamination); high AN-OCD comorbidity (~40%)

### Treatment

**Nutritional rehabilitation is the primary treatment:**
- Goal: weight restoration to a healthy BMI for age/sex; this is the prerequisite for brain normalization and psychological treatment to be effective
- Medical hospitalization criteria: BMI < 14 or rapidly declining, severe electrolyte abnormalities, cardiac instability, unable to engage with outpatient treatment
- Nasogastric (NG) feeds: may be necessary; ethically complex; nasogastric but NOT parenteral nutrition preferred (preserve gut mucosa)

**Evidence-based psychotherapy:**

**Family-Based Treatment (FBT, "Maudsley approach"):**
- Best-studied treatment for adolescent AN [^lock-2010-fbt-an]; ~50% full remission at 1 year
- Three phases: Phase 1 — parents take control of refeeding; Phase 2 — return control to adolescent; Phase 3 — identity development
- Fundamentally behavioral — treats weight restoration as the primary goal, not insight into underlying psychology

**Cognitive-Behavioral Therapy for Eating Disorders (CBT-E):**
- Evidence-based for adults; Fairburn's enhanced CBT model; 40 sessions over 40 weeks
- Targets: dietary restraint, overvaluation of shape/weight, perfectionism, low self-esteem, interpersonal difficulties; most effective at higher weight (BMI > 16)

**Pharmacotherapy (limited evidence):**
- **Olanzapine (atypical antipsychotic):** 2.5-10mg — modest weight gain facilitation; reduces obsessional food-related thoughts (5-HT2A + D2 antagonism); evidence-based in severe AN (2016 RCT, Attia et al.); off-label
- **Dronabinol (THC):** CB1 agonist → stimulates appetite; modest weight gain in small RCTs
- **Cyproheptadine:** 5-HT + H1 antagonist; appetite stimulation; weak evidence
- **SSRIs, antidepressants:** NOT effective in acute AN (starvation state); may help prevent relapse in weight-restored patients if comorbid depression/OCD present
- **No FDA-approved pharmacotherapy for AN exists**

**Emerging treatments:**
- **MANTRA (Maudsley Anorexia Nervosa Treatment for Adults):** Cognitive interpersonal model; focuses on neuropsychological features (set-shifting, central coherence)
- **Muscle-strengthening interventions:** Supervised resistance training → preserves muscle mass and may improve body image
- **Psilocybin:** Phase 2 trial (Johns Hopkins, UCSF) exploring psilocybin-assisted therapy for chronic refractory AN — preliminary results positive
- **Olanzapine LAI:** Monthly injectable being studied for treatment-resistant AN
- **rTMS:** Low-frequency TMS over left DLPFC may reduce food-related anxiety; Phase 2 trials

**Stepped care levels:**
1. Outpatient: weekly therapy + dietitian; BMI ≥ 17; medically stable
2. Intensive outpatient (IOP): 3 meals, group therapy, 9-20h/week; BMI 15-17
3. Partial hospitalization (PHP): Day programs; structured meals
4. Residential: 24h supervised; medically stable but severe illness
5. Medical inpatient: For medical emergencies (refeeding, cardiac, renal)

## Connections

- `connects-to` → **[Serotonin](../../../03-molecular/serotonin/README.md)** — 5-HT2A receptor hyperactivation in PFC contributes to heightened harm avoidance and rigidity in AN; serotonin dysregulation is present pre-morbidly and persists after recovery; SSRIs are ineffective at low weight (insufficient tryptophan substrate); olanzapine (5-HT2A antagonist) modestly aids weight gain.

- `connects-to` → **[Dopamine](../../../03-molecular/dopamine/README.md)** — increased striatal D2/D3 receptor binding in recovered AN patients (PET) suggests reduced dopamine tone; anorexia patients show reduced reward salience of food cues; altered DA reward circuits may explain why food restriction becomes negatively reinforcing and food avoidance feels "safe."

- `connects-to` → **[Leptin](../../../03-molecular/leptin/README.md)** — leptin falls sharply with fat mass loss in AN → amenorrhea, bone loss, immune suppression, and cognitive impairment; paradoxically, some AN patients show modestly elevated leptin relative to weight → false satiety signal; normalizes with weight restoration.

- `connects-to` → **[Cortisol](../../../03-molecular/cortisol/README.md)** — HPA axis hyperactivation in AN → elevated cortisol → bone loss, impaired cognition, and immune suppression; hypercortisolemia persists even when BMI partially normalizes; normalizes with sustained weight restoration.

- `connects-to` → **[BDNF](../../../03-molecular/bdnf/README.md)** — BDNF Val66Met SNP associated with severe early-onset AN; hypothalamic BDNF regulates appetite via PVN-TrkB signaling; serum BDNF is reduced in acute AN and partially normalizes with weight restoration; BDNF dysregulation may contribute to AN's appetite circuit dysfunction.

- `targets` → **[Brain](../../../06-organ/brain/README.md)** — AN shows gray matter reduction (OFC, insula, cingulate); fMRI reveals altered insula processing of food cues, reduced striatal reward responses, and OFC hyperactivation driving cognitive rigidity; much gray matter recovers with weight restoration over 1-2 years.

[^treasure-2010-an-lancet]: Treasure J, Claudino AM, Zucker N. Eating disorders. *Lancet.* 2010;375(9714):583-593. [doi:10.1016/S0140-6736(09)61748-7](https://doi.org/10.1016/S0140-6736(09)61748-7) · [PubMed 19931176](https://pubmed.ncbi.nlm.nih.gov/19931176/)
[^lock-2010-fbt-an]: Lock J, Le Grange D, Agras WS, et al. Randomized clinical trial comparing family-based treatment with adolescent-focused individual therapy for adolescents with anorexia nervosa. *Arch Gen Psychiatry.* 2010;67(10):1025-1032. [doi:10.1001/archgenpsychiatry.2010.128](https://doi.org/10.1001/archgenpsychiatry.2010.128) · [PubMed 20921118](https://pubmed.ncbi.nlm.nih.gov/20921118/)
[^frank-2004-an-neuroimaging]: Frank GK, Bailer UF, Henry SE, et al. Increased dopamine D2/D3 receptor binding after recovery from anorexia nervosa. *Biol Psychiatry.* 2005;58(11):908-912. [doi:10.1016/j.biopsych.2005.05.003](https://doi.org/10.1016/j.biopsych.2005.05.003) · [PubMed 16005437](https://pubmed.ncbi.nlm.nih.gov/16005437/)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
