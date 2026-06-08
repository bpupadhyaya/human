---
schema: human-scale-entry/v1
id: ptsd
name: PTSD
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-08
summary: "PTSD (7-10% lifetime risk after trauma) involves amygdala hyperreactivity, hippocampal atrophy, noradrenergic hyperarousal, and hypocortisolemia; first-line: trauma-focused CBT and SSRIs (sertraline, paroxetine); prazosin (α1 antagonist) reduces nightmares."
aliases: ["PTSD", "post-traumatic stress disorder", "trauma", "combat PTSD", "complex PTSD", "fear extinction", "prazosin PTSD", "EMDR", "prolonged exposure", "TRD PTSD"]
sources:
  - id: yehuda-2015-ptsd-review
    type: peer-reviewed
    cite: "Yehuda R, Hoge CW, McFarlane AC, et al. Post-traumatic stress disorder. Nat Rev Dis Primers. 2015;1:15057."
    doi: "10.1038/nrdp.2015.57"
    pmid: "27189040"
    url: "https://doi.org/10.1038/nrdp.2015.57"
    accessed: "2026-06-08"
  - id: foa-2019-ptsd-treatments
    type: peer-reviewed
    cite: "Foa EB, McLean CP. The efficacy of exposure therapy for anxiety and related disorders and its underlying mechanisms: the emotional processing theory. Annu Rev Clin Psychol. 2016;12:1-28."
    doi: "10.1146/annurev-clinpsy-021815-093533"
    pmid: "26928206"
    url: "https://doi.org/10.1146/annurev-clinpsy-021815-093533"
    accessed: "2026-06-08"
  - id: mitchell-2021-mdma-ptsd
    type: peer-reviewed
    cite: "Mitchell JM, Bogenschutz M, Lilienstein A, et al. MDMA-assisted therapy for severe PTSD: a randomized, double-blind, placebo-controlled phase 3 trial. Nat Med. 2021;27(6):1025-1033."
    doi: "10.1038/s41591-021-01336-3"
    url: "https://doi.org/10.1038/s41591-021-01336-3"
    accessed: "2026-06-08"
cross_links:
  - target: 01-human/03-molecular/norepinephrine
    relation: connects-to
    note: "Locus coeruleus hyperactivation in PTSD → excess NE → amygdala hyperreactivity, hyperarousal, and intrusive re-experiencing; prazosin (α1 antagonist) reduces NE-driven nightmares; propranolol may reduce fear memory reconsolidation when given within hours of trauma."
  - target: 01-human/03-molecular/cortisol
    relation: connects-to
    note: "PTSD exhibits paradoxical hypocortisolemia — elevated CRH but enhanced GR sensitivity → excess negative feedback; low cortisol impairs fear extinction; hydrocortisone given within hours of trauma shows prophylactic benefit in some randomized trials."
  - target: 01-human/03-molecular/bdnf
    relation: connects-to
    note: "Reduced hippocampal BDNF in PTSD mirrors findings in MDD; chronic stress → glucocorticoid-mediated BDNF suppression → hippocampal volume loss (~8% in chronic PTSD); SSRIs normalize BDNF and partially restore hippocampal volume with sustained treatment."
  - target: 01-human/03-molecular/glutamate
    relation: connects-to
    note: "NMDA receptor-mediated processes underlie fear memory consolidation and extinction in amygdala and vmPFC; D-cycloserine (partial NMDA agonist) enhances extinction in CBT; ketamine reduces PTSD symptoms via rapid BDNF/mTOR signaling and disrupted fear memory reconsolidation."
  - target: 01-human/06-organ/brain
    relation: targets
    note: "PTSD features amygdala hyperreactivity and reduced vmPFC control over fear responses; hippocampal volume is reduced ~8%; anterior cingulate shows reduced activation; normalization of amygdala-vmPFC connectivity predicts treatment response on fMRI."
---

# PTSD

## Overview

**Post-traumatic stress disorder (PTSD)** is a trauma- and stressor-related psychiatric condition that develops in a subset of individuals following exposure to actual or threatened death, serious injury, or sexual violence. It affects approximately **7–10% of individuals** who experience qualifying traumatic events over their lifetimes — with higher rates in certain exposed groups (veterans: 15–30%; sexual assault survivors: 30–50%; disaster workers: 10–20%). Globally, an estimated 3.9–5.6% of adults have lifetime PTSD, with women affected at 2× the rate of men.

**DSM-5 PTSD** (requires exposure to trauma + symptoms from all 4 clusters ≥1 month):

**Criterion A (Trauma):** Exposure to death, serious injury, or sexual violence (direct, witnessed, learned about, or repeated first-responder exposure)

**4 Symptom clusters:**

| Cluster | Examples | Neural correlate |
|:---|:---|:---|
| **B — Intrusion** | Flashbacks, nightmares, psychological/physiological distress to cues | Amygdala hyperreactivity; context-independent fear retrieval |
| **C — Avoidance** | Avoiding trauma-related thoughts, feelings, places, people | vmPFC failure to suppress amygdala; anhedonia |
| **D — Negative cognitions/mood** | Persistent negative beliefs, distorted blame, emotional numbing, dissociation | Hippocampal memory encoding failure; PFC hypofunction |
| **E — Hyperarousal** | Hypervigilance, exaggerated startle, irritability, sleep disturbance, reckless behavior | Locus coeruleus-NE hyperactivation; amygdala sensitization |

**Complex PTSD (ICD-11):** Includes three additional domains — emotional dysregulation, negative self-concept, and relationship disturbances — typical of prolonged childhood trauma (complex developmental trauma).

## Structure

### Neurobiology of fear circuits

PTSD represents a pathological state of the **amygdala-hippocampus-prefrontal fear circuit**:

**Basolateral amygdala (BLA):**
- Core site of **fear memory acquisition and storage** — Pavlovian fear conditioning occurs here: CS (conditioned stimulus, e.g., sound) + US (unconditioned stimulus, shock) → CS-US association encoded via CaMKII/CREB-dependent plasticity
- In PTSD: heightened BLA activity, reduced threshold for fear acquisition, overgeneralization of conditioned fear to non-threatening cues (conceptually similar to gun exposure → freeze in a patient with combat PTSD)
- BLA → downstream nuclei: central amygdala (CeA) → fear expression (freezing, HR increase, cortisol); basal amygdala → vHPC → avoidance behavior

**Ventromedial prefrontal cortex (vmPFC, includes infralimbic cortex):**
- Source of **fear extinction** — vmPFC neurons send GABAergic projections to amygdala intercalated cells (ITC) → inhibit CeA → safety signal; extinction learning is vmPFC-dependent
- In PTSD: reduced vmPFC volume and activation → inadequate suppression of BLA → persistence of conditioned fear → failure of extinction → PTSD maintenance
- Target of MDMA-assisted therapy: MDMA restores vmPFC control over amygdala

**Hippocampus:**
- Essential for **contextual fear discrimination** — allows fear response to be appropriately limited to the original danger context (not generalized)
- In PTSD: hippocampal volume reduced ~8% (bilateral; predominantly CA3 and dentate gyrus); impaired contextual encoding → fear triggered in "safe" contexts
- Mechanism: chronic stress → glucocorticoid excess → reduced BDNF → CA3 dendritic retraction; SSRI treatment partially restores hippocampal volume over 6–12 months

**Locus coeruleus (LC):**
- Source of CNS norepinephrine; projects widely to cortex, amygdala, hippocampus, spinal cord
- In PTSD: hyperactivated LC → elevated tonic and phasic NE → chronic hyperarousal, exaggerated startle, sleep disruption
- Target of prazosin (α1 antagonist, reduces nightmares) and clonidine (α2 agonist, reduces LC firing)

## Function

### HPA axis in PTSD: the cortisol paradox

Unlike MDD (which features **hypercortisolemia**), PTSD — particularly chronic PTSD — paradoxically shows **hypocortisolemia** [^yehuda-2015-ptsd-review]:

- **Acute trauma response:** Cortisol surge (normal) → should suppress traumatic memory consolidation and aid resolution
- **Chronic PTSD:** Cortisol levels are often **below normal**, combined with:
  - Enhanced negative feedback sensitivity (lower dexamethasone dose required for cortisol suppression)
  - Upregulated glucocorticoid receptors on lymphocytes
  - Elevated CRH in CSF despite low cortisol

**Mechanistic interpretation:**
- Enhanced GR sensitivity → more powerful negative feedback → greater cortisol suppression
- Low cortisol in PTSD impairs extinction: cortisol normally facilitates extinction memory consolidation; without it, fear memories cannot be adequately resolved
- Yehuda's model: PTSD is not an excess of cortisol but a dysregulation — the normal post-trauma cortisol surge fails to suppress trauma memory → persistent fear encoding

**Implications:** Hydrocortisone given acutely (within hours of trauma) in ICU patients or combat settings reduces PTSD incidence in some RCTs — by rescuing the normal cortisol surge needed for memory resolution.

### Noradrenergic system

The **norepinephrine hyperactivation model of PTSD** explains hyperarousal symptoms:
- LC hyperactivation → elevated NE → increased amygdala reactivity (BLA has dense α1-NE receptors → NE enhances fear memory acquisition and intrusive retrieval)
- Sleep disruption: NE during REM sleep normally decreases → in PTSD, high NE during REM → nightmares
- Startle: NE lowers the sensory threshold for CeA-mediated startle
- Exaggerated cardiovascular response to trauma reminders: sympathetic surge

**Pharmacological targets:**
- **Prazosin (α1 antagonist):** Reduces nightmares and overall PTSD severity in multiple RCTs; blocks NE signaling in amygdala and brainstem circuits during sleep
- **Propranolol (β-blocker):** May reduce fear memory reconsolidation when given within 1–6 hours of reactivating a trauma memory (controversial; reconsolidation blockade hypothesis)
- **Clonidine (α2 agonist):** Reduces LC firing → decreases NE release → reduces hyperarousal; used in children with PTSD/complex PTSD

## Pathology

### Trauma characteristics and risk factors

Not all trauma leads to PTSD. Risk and resilience factors include:

**Risk factors:**
- Trauma type: interpersonal violence (sexual assault, combat) > accidents > natural disasters
- Peritraumatic dissociation (strongest predictor of PTSD development)
- Prior trauma (especially childhood adversity — sensitizes amygdala and HPA axis)
- Genetic factors: heritability ~40%; Val66Met BDNF, FKBP5 (GR co-chaperone variants alter cortisol sensitivity), RELN (reelin)
- Female sex; poverty; lack of social support

**Resilience factors:**
- Strong social support (most protective modifiable factor)
- Prior mastery experiences; sense of agency
- High BDNF (exercise, social engagement)
- Rapid cortisol normalization after trauma (adequate glucocorticoid response)

### Treatment

**First-line evidence-based treatments:**

**Trauma-focused psychotherapy (superior to pharmacotherapy in most trials):**
- **Prolonged Exposure (PE):** Imaginal and in vivo exposure to trauma memories and avoided situations; disrupts conditioned fear through extinction learning; 50-60% remission [^foa-2019-ptsd-treatments]
- **Cognitive Processing Therapy (CPT):** Modifies maladaptive cognitions about trauma (stuck points); equivalent to PE; used widely in VA system
- **EMDR (Eye Movement Desensitization and Reprocessing):** Bilateral sensory stimulation during trauma memory processing; equivalent efficacy to PE/CPT; mechanism debated (eye movements may be inert — exposure component may drive benefit)

**Pharmacotherapy:**
- **SSRIs (sertraline, paroxetine):** FDA-approved for PTSD; moderate efficacy (~30-40% response); normalize serotonin and BDNF; useful for comorbid depression/anxiety
- **Venlafaxine (SNRI):** Off-label but evidence-based; addresses NE hyperarousal component
- **Prazosin (α1 antagonist):** For nightmares and sleep disruption; addresses NE-driven dream pathology
- **Benzodiazepines:** NOT recommended in PTSD — impair fear extinction learning (GABA-A-mediated amnesia blocks extinction consolidation); worsen long-term course despite short-term symptom reduction

**Novel/Emerging:**

**MDMA-assisted therapy:**
- Phase 3 trial (Mitchell et al., Nat Med 2021) [^mitchell-2021-mdma-ptsd]: MDMA-assisted therapy → 67% no longer met PTSD criteria vs. 32% placebo at 18-week endpoint; large effect size (d=0.9)
- Mechanism: MDMA releases serotonin, oxytocin, and NE → dampens amygdala reactivity while enabling emotional processing within therapy session; facilitates "therapeutic window" — processing trauma without overwhelming anxiety; may restore vmPFC-amygdala connectivity
- FDA Advisory Committee rejected approval (2024) on manufacturing and data integrity grounds; Phase 3b trial ongoing; widely available in clinical settings outside the US (Australia approved 2023)

**Stellate ganglion block:**
- Single injection of local anesthetic into cervical sympathetic ganglion; appears to reduce LC-sympathetic outflow; ~50-60% responder rate in RCTs for combat PTSD; mechanism may involve NGF-driven sympathetic hyperinnervation of LC

**Cannabis and cannabinoids:**
- Endocannabinoid system (CB1 receptors in amygdala and hippocampus) regulates fear extinction; THC reduces nightmare severity; synthetic nabilone approved in Canada for PTSD nightmares; clinical use outpacing evidence base

## Connections

- `connects-to` → **[Norepinephrine](../../../03-molecular/norepinephrine/README.md)** — locus coeruleus hyperactivation in PTSD drives excess NE → amygdala hyperreactivity, hyperarousal, and intrusive re-experiencing; prazosin (α1 antagonist) reduces NE-driven nightmares; propranolol given acutely after trauma may reduce fear memory reconsolidation.

- `connects-to` → **[Cortisol](../../../03-molecular/cortisol/README.md)** — PTSD exhibits paradoxical hypocortisolemia with enhanced GR sensitivity → excess negative feedback; low cortisol impairs fear extinction; hydrocortisone given within hours of trauma shows prophylactic benefit; opposite HPA profile from MDD despite clinical overlap.

- `connects-to` → **[BDNF](../../../03-molecular/bdnf/README.md)** — chronic stress-induced glucocorticoid BDNF suppression causes hippocampal volume loss (~8%) in PTSD; reduced BDNF impairs contextual fear discrimination; SSRIs normalize hippocampal BDNF and partially restore volume; Val66Met SNP increases PTSD risk.

- `connects-to` → **[Glutamate](../../../03-molecular/glutamate/README.md)** — NMDA receptors mediate fear memory consolidation and extinction in amygdala and vmPFC; D-cycloserine (partial NMDA agonist) enhances extinction learning in prolonged exposure therapy; ketamine reduces PTSD symptoms via BDNF/mTOR-mediated synaptic remodeling.

- `targets` → **[Brain](../../../06-organ/brain/README.md)** — PTSD features BLA hyperreactivity, reduced vmPFC-amygdala suppression, ~8% hippocampal volume reduction, and reduced anterior cingulate activation; normalization of amygdala-vmPFC functional connectivity is a biomarker of treatment response on task-based fMRI.

[^yehuda-2015-ptsd-review]: Yehuda R, Hoge CW, McFarlane AC, et al. Post-traumatic stress disorder. *Nat Rev Dis Primers.* 2015;1:15057. [doi:10.1038/nrdp.2015.57](https://doi.org/10.1038/nrdp.2015.57) · [PubMed 27189040](https://pubmed.ncbi.nlm.nih.gov/27189040/)
[^foa-2019-ptsd-treatments]: Foa EB, McLean CP. The efficacy of exposure therapy for anxiety and related disorders. *Annu Rev Clin Psychol.* 2016;12:1-28. [doi:10.1146/annurev-clinpsy-021815-093533](https://doi.org/10.1146/annurev-clinpsy-021815-093533) · [PubMed 26928206](https://pubmed.ncbi.nlm.nih.gov/26928206/)
[^mitchell-2021-mdma-ptsd]: Mitchell JM, Bogenschutz M, Lilienstein A, et al. MDMA-assisted therapy for severe PTSD: a randomized, double-blind, placebo-controlled phase 3 trial. *Nat Med.* 2021;27(6):1025-1033. [doi:10.1038/s41591-021-01336-3](https://doi.org/10.1038/s41591-021-01336-3)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
