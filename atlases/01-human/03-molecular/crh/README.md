---
schema: human-scale-entry/v1
id: crh
name: CRH
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-08
summary: "Hypothalamic neuropeptide (CRH gene, chr8q13) initiating the HPA axis: PVN → CRHR1 → ACTH → cortisol. Extra-hypothalamic CRH in amygdala/BNST drives stress arousal via LC-NE activation; CRHR1 antagonists investigated for AUD, PTSD, and MDD."
aliases: ["CRH", "CRF", "corticotropin-releasing hormone", "corticotropin-releasing factor", "CRHR1", "CRHR2", "PVN", "HPA axis"]
cross_links:
  - target: 01-human/03-molecular/cortisol
    relation: modulates
    note: "CRH from hypothalamic PVN → pituitary CRHR1 → ACTH → adrenal cortisol synthesis; glucocorticoid negative feedback suppresses CRH/ACTH at pituitary and hypothalamic levels; together CRH-ACTH-cortisol form the canonical HPA axis stress response cascade."
  - target: 01-human/03-molecular/norepinephrine
    relation: modulates
    note: "Extra-hypothalamic CRH activates CRHR1 on LC neurons → NE release → cortical arousal and stress vigilance; LC in turn sends NE projections back to PVN to amplify CRH release, forming a feedforward CRH-NE stress loop; CRH-LC drive underlies stress-induced hyperarousal."
  - target: 01-human/03-molecular/gaba
    relation: connects-to
    note: "GABA interneurons in PVN inhibit CRH-releasing neurons; benzodiazepines (GABA-A PAMs) attenuate CRH release and reduce stress-induced HPA activation; GABA-B agonists also suppress PVN CRH; the CRH-GABA balance in amygdala/BNST regulates anxiety-like states."
  - target: 01-human/06-organ/brain
    relation: modulates
    note: "CRH neurons in lateral amygdala/CeA, BNST, and hippocampus act independent of the HPA axis to coordinate fear, anxiety, and stress memory; CeA CRH → downstream anxiety circuits; BNST CRH mediates sustained anticipatory anxiety ('sustained vs. phasic fear' distinction)."
  - target: 01-human/07-system/alcohol-use-disorder
    relation: connects-to
    note: "CRH mediates the negative reinforcement model of AUD: withdrawal/stress → CeA/BNST CRH excess → aversion and anxiety → drinking to alleviate; CRHR1 antagonists (antalarmin, pexacerfont) reduce stress-induced drinking in animal models and were trialed for AUD."
  - target: 01-human/07-system/ptsd
    relation: connects-to
    note: "PTSD involves CRH excess in CSF and elevated ACTH but paradoxically low cortisol (enhanced glucocorticoid negative feedback); CRH hyperdrive in amygdala/BNST contributes to hyperarousal and re-experiencing; CRHR1 antagonists proposed for PTSD pharmacotherapy."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "MDD features CRH hyperdrive: PVN and CeA CRH excess → elevated ACTH + hypercortisolemia → hippocampal atrophy; blunted DST is the most replicated biological finding in MDD; CRHR1 antagonists (pexacerfont) and mifepristone show antidepressant potential in trials."
  - target: 01-human/03-molecular/acth
    relation: modulates
    note: "CRH (CRHR1/Gs/cAMP/PKA) is the primary ACTH secretagogue; AVP (V1bR) synergistically potentiates CRH-driven ACTH release; the CRH stimulation test (1 µg/kg IV) assesses pituitary-adrenal reserve and can distinguish pituitary from ectopic ACTH sources in Cushing's syndrome."
sources:
  - id: vale-1981-crh-discovery
    type: peer-reviewed
    cite: "Vale W, Spiess J, Rivier C, Rivier J. Characterization of a 41-residue ovine hypothalamic peptide that stimulates secretion of corticotropin and beta-endorphin. Science. 1981;213(4514):1394-1397."
    doi: "10.1126/science.6267699"
    pmid: "6267699"
    url: "https://doi.org/10.1126/science.6267699"
  - id: koob-2010-crh-addiction
    type: peer-reviewed
    cite: "Koob GF. The role of CRF and CRF-related peptides in the dark side of addiction. Brain Res. 2010;1314:3-14."
    doi: "10.1016/j.brainres.2009.11.008"
    pmid: "19912996"
    url: "https://doi.org/10.1016/j.brainres.2009.11.008"
---

# CRH

## Overview

**CRH** (corticotropin-releasing hormone; also called **CRF**, corticotropin-releasing factor) is a 41-amino acid neuropeptide discovered in 1981 by Vale et al. [^vale-1981-crh-discovery] that serves as the **master initiator of the hypothalamic-pituitary-adrenal (HPA) axis** — the principal hormonal stress response system. Encoded by the *CRH* gene on chromosome 8q13, CRH is synthesized primarily in **parvocellular neurons of the paraventricular nucleus (PVN)** of the hypothalamus, from which it is released into the hypothalamic-pituitary portal circulation to drive pituitary ACTH secretion.

Beyond the classic HPA axis role, CRH functions as a **neuromodulator throughout the brain** — particularly in the central amygdala (CeA), bed nucleus of the stria terminalis (BNST), locus coeruleus (LC), hippocampus, and prefrontal cortex — where it coordinates the behavioral, autonomic, and cognitive aspects of the stress response independently of peripheral cortisol. This dual role (endocrine vs. neurocircuit) makes CRH pivotal to anxiety disorders, PTSD, depression, and substance use disorders.

**Three major clinical contexts:**
1. **Stress-related disorders** — CRH excess in CSF/amygdala seen in MDD, PTSD, and anxiety; CRHR1 antagonists have entered clinical trials
2. **Alcohol Use Disorder** — CRH drives the negative reinforcement cycle of addiction; CeA CRH is central to stress-induced relapse
3. **Cushing's disease** — pituitary ACTH-secreting adenoma (corticotropinoma) driven by excess CRH/ACTH signaling; ketoconazole, mifepristone, pasireotide used

## Structure

**CRH peptide:**
- 41 amino acids (human); alpha-helical C-terminal domain essential for CRHR1 binding; N-terminal region required for receptor activation
- Processed from a 196-aa prepro-CRH by prohormone convertase 1/3 (PC1/3) in dense-core vesicles
- Highly conserved across mammals; rat/ovine CRH is identical to human CRH except for the first characterized ovine CRH (1 aa difference in rodent)
- Half-life in circulation: ~5-10 min (rapidly degraded by circulating peptidases)

**CRH Receptors:**

| Receptor | Gene | Chromosome | Coupling | Distribution | Function |
|:---|:---|:---|:---|:---|:---|
| **CRHR1** | CRHR1 | 17q21.31 | Gs → ↑cAMP → PKA | Pituitary corticotrophs, amygdala, LC, cortex, cerebellum | HPA axis drive, anxiety, stress response |
| **CRHR2** | CRHR2 | 7p14.3 | Gs → ↑cAMP (also Gi in some tissues) | Lateral septum, hypothalamus (VMH), skeletal muscle, heart, GI | Stress recovery/termination, appetite, cardiovascular |

- **CRHR1** is the primary mediator of stress responses and the target for psychiatric drug development
- **CRHR2** may oppose CRHR1 — its activation in lateral septum contributes to stress recovery; selective CRHR2 agonists are of interest for post-stress termination

**Urocortins (CRH family):**
- **Urocortin 1 (UCN1):** highest affinity for both CRHR1 and CRHR2; stress-recovery and appetite suppression
- **Urocortin 2 (UCN2; Stresscopin-related peptide):** CRHR2-selective; cardiovascular protection and stress adaptation
- **Urocortin 3 (UCN3; Stresscopin):** CRHR2-selective; anxiolytic role; expressed in medial amygdala

## Function

### HPA Axis Cascade

The canonical CRH neuroendocrine pathway:

1. **Acute stressor** → sensory/limbic input to PVN (glutamate from parabrachial nucleus, brainstem; cortical top-down) → CRH neuron activation
2. **CRH → portal blood** → median eminence → anterior pituitary corticotrophs → **CRHR1 → Gs → cAMP → PKA** → proopiomelanocortin (POMC) processing → **ACTH release** into systemic circulation
3. **ACTH → adrenal cortex** (zona fasciculata) → MC2R → StAR protein → cortisol synthesis and secretion
4. **Cortisol negative feedback:**
   - Fast feedback: membrane GR on pituitary corticotrophs → endocannabinoid (2-AG) retrograde suppression of CRH presynaptic release
   - Slow feedback: nuclear GR/MR in hippocampus, PVN → reduces CRH transcription (GRE in CRH promoter)
5. **HPA termination:** glucocorticoid → PVN → reduced CRH synthesis; pituitary → reduced ACTH sensitivity; hippocampal GR → top-down HPA inhibition

**Arginine vasopressin (AVP) co-regulation:**
- Many PVN CRH neurons also synthesize AVP; CRH + AVP synergistically amplify ACTH release (AVP acts via V1b receptor on pituitary corticotrophs → Gq → IP3/DAG → PKC → ACTH release)
- Chronic stress → shift from CRH-dominant to CRH/AVP co-dominant stimulation → sustained HPA activation

### Extra-Hypothalamic CRH

**Central amygdala (CeA) CRH:**
- CeA CRH neurons project to BNST, brainstem, and spinal cord → orchestrate fear expression, threat response, and motivational aspects of stress
- In addiction (Koob's "dark side" model [^koob-2010-crh-addiction]): CeA CRH is recruited during drug withdrawal → negative affective state → compulsive drinking/drug use to reduce aversion (negative reinforcement)

**BNST CRH:**
- BNST receives CRH input from CeA and projects broadly to VTA, LC, PVN, PAG
- Mediates **sustained/contextual anxiety** (as opposed to phasic/cue fear mediated by BLA): BNST CRH activation → prolonged anxiety states, vigilance, uncertain threat

**Locus Coeruleus CRH:**
- CRHR1 on LC NE neurons → direct CRH-driven NE release
- CRH → LC → widespread NE release → cortical arousal, hypervigilance, startle sensitization
- This mechanism contributes to stress-induced hyperarousal in PTSD and panic

### CRH in Appetite Regulation

- CRH/UCN via CRHR1 and CRHR2 reduce food intake (stress anorexia)
- UCN3 in arcuate nucleus → CRHR2 → reduced NPY/AgRP → anorexigenic
- Opposite to ghrelin (orexigenic): CRH and ghrelin serve as competing hunger/satiety stress signals

## Mechanism

### CRHR1 Signal Transduction

1. CRH binds CRHR1 extracellular N-terminal domain (large N-terminal ECD, class B GPCR)
2. Conformational change → Gαs dissociation → adenylyl cyclase → **↑cAMP**
3. cAMP → PKA → phosphorylation of CREB, ion channels, POMC promoter → ACTH synthesis
4. cAMP → EPAC (exchange protein activated by cAMP) → alternative signaling including small GTPase Rap1 → gene regulation
5. β-arrestin recruitment → CRHR1 internalization → desensitization

**Pituitary specificity:** In pituitary corticotrophs, CRHR1 cAMP → PKA → phosphorylation of CREB → POMC gene transcription → increased ACTH precursor; PKA also phosphorylates voltage-gated K⁺ channels → membrane depolarization → Ca²⁺ influx → ACTH vesicle exocytosis

### CRHR1 Antagonists in Development

| Compound | Selectivity | Status | Target indication |
|:---|:---|:---|:---|
| Antalarmin | CRHR1 | Preclinical/Phase 1 | AUD, anxiety |
| Pexacerfont | CRHR1 | Phase 2 (inconclusive) | MDD, GAD, AUD |
| Verucerfont | CRHR1 | Phase 2 | AUD (stress-induced drinking) |
| CP-316,311 | CRHR1 | Phase 2 (negative) | MDD |
| NBI-34041 | CRHR1 | Phase 1 | Anxiety |

**Why CRHR1 antagonists haven't succeeded clinically:** Most trials targeted MDD/anxiety patients without biomarker selection for CRH hyperdrive; HPA normalization may not map directly to symptom reduction; AUD targeting patients with stress-driven drinking may be most appropriate.

### CRH in Addiction Neuroscience (Koob's Model)

The "opponent process" and "allostatic" models of addiction propose:
1. **Binge/intoxication:** Reward circuit activation (NAcc DA, opioid, GABA)
2. **Withdrawal/negative affect:** Counter-adaptation → CeA/BNST CRH recruitment → dysphoria, anxiety
3. **Preoccupation/anticipation:** Prefrontal craving + stress-cue reactivity

The CeA CRH system becomes **"sensitized"** with repeated withdrawal cycles → increasingly severe negative affect states → compulsive drug use to restore homeostasis.

## Pathology

| Condition | CRH axis state | Clinical implication |
|:---|:---|:---|
| **Major Depression** | PVN CRH mRNA↑; CSF CRH↑; CRH hyperdrive | HPA hyperactivation; high cortisol; CRHR1 antagonist trials |
| **PTSD** | CSF CRH↑; ACTH↑; but cortisol LOW (enhanced feedback) | Unique HPA phenotype; CRH antagonism a proposed target |
| **Anxiety disorders** | CeA/BNST CRH excess → sustained fear | Target for CRHR1 antagonists; benzodiazepines inhibit CRH |
| **AUD** | CeA CRH recruitment during withdrawal | Negative reinforcement drinking; CRHR1 antagonists reduce stress-drinking |
| **Cushing's disease** | Pituitary corticotropinoma (ACTH) → CRH-independent cortisol excess | Pasireotide, ketoconazole, mifepristone; surgical resection |
| **Anorexia nervosa** | CRH↑ → appetite suppression; HPA hyperactivation | Weight restoration → HPA normalization |

## Connections

- `modulates` → **[Cortisol](../cortisol/README.md)** — CRH from PVN → pituitary CRHR1 → ACTH → adrenal cortisol synthesis; glucocorticoid negative feedback suppresses CRH/ACTH at pituitary and hypothalamic levels; together they form the HPA axis stress cascade; disruption underlies MDD, PTSD, and Cushing's.

- `modulates` → **[Norepinephrine](../norepinephrine/README.md)** — extra-hypothalamic CRH activates CRHR1 on LC neurons → NE release → cortical arousal and stress vigilance; LC NE projections to PVN amplify CRH release, forming a feedforward CRH-NE stress loop; this drive underlies stress-induced hyperarousal in PTSD and panic.

- `connects-to` → **[GABA](../gaba/README.md)** — GABA interneurons in PVN inhibit CRH neurons; benzodiazepines (GABA-A PAMs) attenuate CRH release and HPA activation; GABA-B agonists suppress PVN CRH; the CRH-GABA balance in amygdala/BNST regulates anxiety-like states and stress responses.

- `modulates` → **[Brain](../../06-organ/brain/README.md)** — CRH neurons in CeA, BNST, and LC act independent of the HPA axis to coordinate fear, anxiety, and stress memory; CeA CRH mediates fear expression; BNST CRH drives sustained anticipatory anxiety; hippocampal glucocorticoid receptors mediate slow negative feedback on CRH synthesis.

- `connects-to` → **[Alcohol Use Disorder](../../07-system/alcohol-use-disorder/README.md)** — CRH mediates the negative reinforcement model of AUD: withdrawal/stress → CeA/BNST CRH excess → aversion and anxiety → drinking to alleviate; CRHR1 antagonists (antalarmin, verucerfont) reduce stress-induced drinking in animal models.

- `connects-to` → **[PTSD](../../07-system/ptsd/README.md)** — PTSD shows CSF CRH excess and elevated ACTH but paradoxically low cortisol (enhanced glucocorticoid feedback); CRH hyperdrive in amygdala/BNST contributes to hyperarousal and re-experiencing; CRHR1 antagonism is a proposed pharmacotherapy approach.

- `connects-to` → **[Major Depressive Disorder](../../07-system/major-depressive-disorder/README.md)** — MDD features CRH hyperdrive from PVN and CeA → elevated ACTH + hypercortisolemia → hippocampal atrophy via BDNF suppression; blunted DST suppression is the most replicated biological finding in MDD; CRHR1 antagonists (pexacerfont) and mifepristone show antidepressant activity in trials.

- `modulates` → **[ACTH](../acth/README.md)** — CRH (CRHR1/Gs/cAMP/PKA on pituitary corticotrophs) is the primary ACTH secretagogue driving both acute ACTH exocytosis and sustained POMC transcription; AVP (V1bR) synergistically potentiates CRH-driven ACTH release during acute stress; the CRH stimulation test (1 µg/kg IV → ACTH measured at 15, 30, 60 min) assesses pituitary-adrenal reserve.

[^vale-1981-crh-discovery]: Vale W, Spiess J, Rivier C, Rivier J. Characterization of a 41-residue ovine hypothalamic peptide that stimulates secretion of corticotropin and beta-endorphin. *Science.* 1981;213(4514):1394-1397. [doi:10.1126/science.6267699](https://doi.org/10.1126/science.6267699) · [PubMed 6267699](https://pubmed.ncbi.nlm.nih.gov/6267699/)
[^koob-2010-crh-addiction]: Koob GF. The role of CRF and CRF-related peptides in the dark side of addiction. *Brain Res.* 2010;1314:3-14. [doi:10.1016/j.brainres.2009.11.008](https://doi.org/10.1016/j.brainres.2009.11.008) · [PubMed 19912996](https://pubmed.ncbi.nlm.nih.gov/19912996/)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
