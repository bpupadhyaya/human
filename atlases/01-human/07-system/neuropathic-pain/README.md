---
schema: human-scale-entry/v1
id: neuropathic-pain
name: Neuropathic Pain
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-08
summary: "Neuropathic pain arises from peripheral nerve injury or CNS lesion; ectopic discharge, spinal wind-up (NMDA/SP), and central sensitization maintain pain beyond healing. FDA-approved treatments: duloxetine, pregabalin, gabapentin, and topical agents."
aliases: ["neuropathic pain", "peripheral neuropathy pain", "diabetic neuropathy", "postherpetic neuralgia", "central sensitization pain", "allodynia", "hyperalgesia", "ectopic discharge"]
cross_links:
  - target: 01-human/03-molecular/glutamate
    relation: connects-to
    note: "Peripheral nerve injury → spinal NMDA sensitization and AMPA upregulation → central sensitization; ectopic glutamate from injured axons; ketamine (NMDA antagonist) reduces refractory neuropathic pain; mGluR5 antagonists reduce allodynia in rodent neuropathy models."
  - target: 01-human/03-molecular/substance-p
    relation: connects-to
    note: "SP released from injured C-fibers drives NK1R dorsal horn sensitization; peripheral nerve injury → ↑ SP in DRG → amplified spinal wind-up; NK1R-NMDA synergy underlies central sensitization in neuropathic pain states; SP-driven allodynia and hyperalgesia are NK1R-mediated."
  - target: 01-human/03-molecular/bdnf
    relation: connects-to
    note: "Activated microglia release BDNF in spinal dorsal horn after nerve injury; microglial BDNF-TrkB on lamina I neurons downregulates KCC2 → GABA becomes depolarizing → allodynia; microglial BDNF is required for nerve-injury pain hypersensitivity in rodent models."
  - target: 01-human/03-molecular/serotonin
    relation: connects-to
    note: "Descending serotonergic inhibition is disrupted in neuropathic pain; duloxetine (SNRI) restores 5-HT/NE descending inhibition and is FDA-approved for diabetic neuropathy; 5-HT3 receptors on dorsal horn neurons facilitate pain; 5-HT3 antagonists do not improve neuropathic pain."
  - target: 01-human/03-molecular/norepinephrine
    relation: connects-to
    note: "Descending NE from LC to dorsal horn is deficient in neuropathic pain; SNRIs (duloxetine) and TCAs increase NE in descending inhibitory pathways — the primary analgesic mechanism; α2 agonists (intrathecal clonidine) reduce allodynia via spinal NE receptors."
  - target: 01-human/06-organ/brain
    relation: targets
    note: "Neuropathic pain involves thalamic sensitization, ACC/insula hyperactivation, and somatosensory cortex reorganization; chronic pain reduces gray matter in ACC and dlPFC; CNS changes explain pain persistence despite peripheral healing and underlie maladaptive neuroplasticity."
  - target: 01-human/07-system/fibromyalgia
    relation: connects-to
    note: "FM and neuropathic pain share central sensitization (NMDA wind-up, descending inhibition failure) but differ: neuropathic pain requires nerve injury while FM is nociplastic; both respond to SNRIs and α2δ ligands; small fiber neuropathy co-occurs in ~40% of FM patients."
  - target: 01-human/04-cellular/microglia
    relation: connects-to
    note: "Spinal microglia drive neuropathic pain: nerve injury → P2X4R/P2X7R → p38 MAPK → BDNF secretion → neuronal TrkB → KCC2 downregulation → GABA becomes depolarizing → allodynia; minocycline (microglial inhibitor) attenuates pain in rodent neuropathy models."
  - target: 01-human/05-tissue/peripheral-nerve
    relation: connects-to
    note: "Neuropathic pain most often begins with a peripheral-nerve lesion: trauma, diabetes, chemotherapy or compression damages axons → ectopic firing, Nav1.7 remodeling and loss of large-fiber inhibition → spontaneous pain and allodynia; nerve conduction and skin biopsy localize it."
  - target: 01-human/07-system/type-2-diabetes
    relation: connects-to
    note: "Diabetes is the leading cause of neuropathic pain worldwide: chronic hyperglycemia and microvascular injury damage small sensory fibers → distal symmetric painful polyneuropathy with burning feet; glucose control slows it, and duloxetine, pregabalin and gabapentin treat the pain."
  - target: 01-human/07-system/parkinsons-disease
    relation: connects-to
    note: "Pain is a frequent non-motor symptom of Parkinson's, including a central component from altered nociceptive processing in dopaminergic circuits; this PD pain often varies with medication 'on/off' states and can respond to dopaminergic therapy, unlike peripheral neuropathic pain."
  - target: 01-human/07-system/migraine
    relation: connects-to
    note: "Migraine and neuropathic pain share central sensitization and CGRP biology: trigeminovascular and peripheral nerves both amplify pain, and CGRP and sodium-channel mechanisms overlap—so anti-CGRP and anticonvulsant drugs help both chronic migraine and neuropathic pain."
  - target: 01-human/07-system/multiple-sclerosis
    relation: connects-to
    note: "Neuropathic pain is common in multiple sclerosis: demyelinating lesions along central pain pathways cause trigeminal neuralgia, Lhermitte's sign, and the burning MS hug—a major, often undertreated symptom managed with anticonvulsants and antidepressants."
  - target: 01-human/04-cellular/astrocyte
    relation: connects-to
    note: "Astrocytes, with microglia, sustain chronic neuropathic pain: after nerve injury reactive astrocytes in the spinal dorsal horn release cytokines and disturb glutamate handling—so glial activation, not just neurons, maintains the chronic pain state."
  - target: 01-human/05-tissue/guillain-barre
    relation: connects-to
    note: "Guillain-Barré syndrome can leave chronic neuropathic pain: acute autoimmune demyelination of peripheral nerves causes severe pain during the illness, and damaged, abnormally firing nerves can produce lasting neuropathic pain even after motor recovery."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "Neuropathic pain arises from maladaptive changes in neurons: injured sensory neurons become hyperexcitable, fire spontaneously and rewire their connections, so pain persists without ongoing tissue damage—the nervous system generating pain from its own circuitry."
  - target: 01-human/07-system/opioid-use-disorder
    relation: connects-to
    note: "Neuropathic pain is the setting where opioids both disappoint and endanger: opioids work poorly for neuropathic pain yet are often prescribed, fueling tolerance, dependence and opioid use disorder—so guidelines favor antidepressants and gabapentinoids."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Voltage-gated calcium channels are the target of first-line neuropathic-pain drugs: gabapentin and pregabalin bind the alpha-2-delta subunit, cutting calcium-driven release of pain neurotransmitters from overexcitable sensory neurons—linking calcium to pain control."
  - target: 01-human/03-molecular/gaba
    relation: connects-to
    note: "Neuropathic pain partly reflects lost GABAergic inhibition: nerve injury weakens inhibitory GABA signaling in the spinal dorsal horn, so normally innocuous touch is read as pain (allodynia)—restoring this inhibitory tone is a key analgesic strategy."
  - target: 02-pathogen/01-viruses/varicella-zoster-virus
    relation: connects-to
    note: "Varicella-zoster virus is a leading cause of neuropathic pain: after shingles, virus-damaged sensory nerves can fire abnormally for months as postherpetic neuralgia, the classic post-infectious neuropathic pain—now largely preventable by zoster vaccination."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "Voltage-gated sodium channels generate neuropathic pain: after nerve injury, damaged neurons over-express Nav1.7 and Nav1.8 and fire spontaneously, so sodium-channel blockers—local anesthetics, mexiletine, and the new Nav1.8 inhibitor suzetrigine—are core analgesics."
  - target: 01-human/02-atomic/potassium
    relation: connects-to
    note: "Potassium channels are the brakes on pain firing: by setting resting voltage and repolarizing neurons, Kv/KCNQ channels limit excitability, so their loss after nerve injury leaves neurons hyperexcitable—making potassium-channel openers a target for nerve pain."
  - target: 01-human/03-molecular/endocannabinoid
    relation: connects-to
    note: "The endocannabinoid system dampens neuropathic pain: cannabinoid receptors on neurons and microglia suppress pain transmission and neuroinflammation, which is why cannabinoids are tried for nerve pain—though benefit is modest and tempered by side effects."
  - target: 01-human/03-molecular/cgrp
    relation: connects-to
    note: "CGRP is a key pain neuropeptide alongside substance P: released from sensory nerves, it sensitizes pain pathways and dilates vessels, and blocking it controls migraine—illustrating how neuropeptides amplify the signaling that becomes chronic neuropathic pain."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "Magnesium dampens neuropathic pain at the NMDA receptor: it normally plugs the channel that drives central sensitization, so low magnesium unmasks pain amplification and magnesium infusion is used to blunt it—linking a simple ion to chronic pain."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "Small-fiber neuropathic pain is diagnosed in the skin: a skin biopsy measuring intraepidermal nerve-fiber density reveals the loss of tiny pain fibers, and capsaicin patches treat the skin's overactive nociceptors—making skin both a diagnostic and therapeutic site."
  - target: 01-human/03-molecular/tnf-alpha
    relation: connects-to
    note: "Neuropathic pain is sustained by TNF and neuroinflammation: injured nerves and activated glia release TNF-alpha that sensitizes pain neurons, turning a transient injury into chronic pain—why the immune system is a target for hard-to-treat pain."
  - target: 01-human/03-molecular/dopamine
    relation: connects-to
    note: "Dopamine sets the brain's pain volume: descending dopamine pathways and the reward system modulate how much pain is felt and how much it bothers, so low dopamine (as in Parkinson's) lowers the pain threshold and worsens chronic pain."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "Mast cells inflame injured nerves into pain: clustered around peripheral nerves, they release histamine, proteases, and cytokines that sensitize nociceptors, linking the immune system to the burning pain of nerve injury and CRPS."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Nerve injury summons macrophages that sustain pain: they swarm the damaged nerve and dorsal-root ganglion, releasing cytokines that sensitize sensory neurons, so this neuroimmune attack helps turn a transient injury into chronic neuropathic pain."
  - target: 01-human/05-tissue/synapse
    relation: connects-to
    note: "Neuropathic pain is burned in at the synapse: relentless input strengthens spinal dorsal-horn synapses (central sensitization), so the cord amplifies signals and even gentle touch is read as pain long after the injury heals."
  - target: 01-human/03-molecular/atp
    relation: connects-to
    note: "ATP is a pain signal outside the cell: released from damaged tissue and nerves, it fires purinergic receptors on sensory neurons and microglia, a key trigger that switches on the spinal microglia driving neuropathic pain."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Small-fiber neuropathy is confirmed under the microscope: a skin punch biopsy, immunostained and read in light, counts the thinned nerve endings behind unexplained burning pain that routine tests miss."
  - target: 01-human/03-molecular/mu-opioid-receptor
    relation: connects-to
    note: "Neuropathic pain resists opioids: nerve injury strips mu-opioid receptors from damaged neurons and stirs glia, so morphine-type drugs work poorly here, pushing treatment toward gabapentinoids and antidepressants."
  - target: 01-human/04-cellular/oligodendrocyte
    relation: connects-to
    note: "Lost myelin makes nerves misfire: when oligodendrocytes and their peripheral counterparts fail, demyelinated axons fire ectopically and cross-talk, generating the shooting, electric pains of conditions like MS."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy shows the damaged nerve behind the pain: demyelinated and degenerating axons, and the dropout of fine unmyelinated fibers in small-fiber neuropathy, leave bared, hyperexcitable membranes that fire on their own."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "Nerve damage can silence the heart's warnings: diabetic cardiac autonomic neuropathy blunts the pain of a heart attack into a 'silent' one and destabilizes heart rate and blood pressure, a dangerous extension of peripheral nerve disease."
  - target: 03-medicine/03-food/vitamin-d
    relation: connects-to
    note: "Vitamin D deficiency frays the nerves: low levels are tied to more severe diabetic and other peripheral neuropathies, and the vitamin's role in nerve growth factor and repair makes supplementation a studied adjunct for the pain."
  - target: 01-human/03-molecular/adenosine
    relation: connects-to
    note: "Adenosine quiets pain at the spinal cord: acting on A1 receptors it hyperpolarizes pain neurons and dampens transmission, a built-in analgesic brake that drugs and even acupuncture are thought to recruit against neuropathic pain."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Neuropathic pain is partly an immune disease: T cells infiltrate injured nerves and dorsal root ganglia, releasing cytokines that sensitize pain neurons — which is why the pain outlasts the injury and resists ordinary painkillers."
  - target: 01-human/03-molecular/acetylcholine
    relation: connects-to
    note: "Cholinergic signaling soothes the pain pathway: spinal muscarinic and nicotinic receptors blunt pain transmission, so boosting acetylcholine is one mechanism behind certain analgesics and a target explored for neuropathic pain."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "Antibodies both cause and treat nerve pain: autoantibodies against gangliosides and MAG drive the painful neuropathies of GBS and CIDP, while anti-NGF monoclonal antibodies like tanezumab were developed to silence pain at its growth-factor source."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "Pain and mood share circuits and drugs: chronic neuropathic pain breeds depression, the two amplifying each other through overlapping serotonin-noradrenaline pathways, which is why SNRIs and tricyclics treat both at once."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "The kidney both causes and constrains: uremic neuropathy makes the nerves ache in kidney failure, and because gabapentin and pregabalin are cleared renally, their doses must be cut to avoid toxic accumulation in these patients."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "Cytokines sensitize the injured nerve: IL-6 released after nerve damage lowers the firing threshold of pain neurons and recruits immune cells, helping turn a transient injury into the persistent firing of neuropathic pain."
  - target: 01-human/07-system/sjogrens-syndrome
    relation: connects-to
    note: "Autoimmune dryness can attack the nerves: Sjögren's syndrome causes a sensory neuronopathy and small-fiber neuropathy, the immune assault on dorsal root ganglia producing burning, painful numbness even with little joint disease."
  - target: 01-human/07-system/hiv-aids
    relation: connects-to
    note: "HIV is a global cause of painful neuropathy: the virus and some antiretroviral drugs both damage long sensory axons, producing a distal symmetric polyneuropathy with burning feet that is among the infection's most common neurologic complications."
sources:
  - id: jensen-2011-neuropathic-pain-review
    type: peer-reviewed
    cite: "Jensen TS, Baron R, Haanpää M, et al. A new definition of neuropathic pain. Pain. 2011;152(10):2204-2205."
    doi: "10.1016/j.pain.2011.06.017"
    pmid: "21764514"
    url: "https://doi.org/10.1016/j.pain.2011.06.017"
    accessed: "2026-06-08"
  - id: dworkin-2010-neuropathic-pain-treatment
    type: peer-reviewed
    cite: "Dworkin RH, O'Connor AB, Audette J, et al. Recommendations for the pharmacological management of neuropathic pain: an overview and literature update. Mayo Clin Proc. 2010;85(3 Suppl):S3-14."
    doi: "10.4065/mcp.2009.0649"
    pmid: "20194146"
    url: "https://doi.org/10.4065/mcp.2009.0649"
    accessed: "2026-06-08"
  - id: scholz-2002-neuropathic-pain-mechanisms
    type: peer-reviewed
    cite: "Scholz J, Woolf CJ. Can we conquer pain? Nat Neurosci. 2002;5(Suppl):1062-1067."
    doi: "10.1038/nn942"
    pmid: "12403987"
    url: "https://doi.org/10.1038/nn942"
    accessed: "2026-06-08"
---

# Neuropathic Pain

## Overview

**Neuropathic pain** is defined (IASP 2011) as pain arising as a direct consequence of a **lesion or disease affecting the somatosensory nervous system** [^jensen-2011-neuropathic-pain-review] — distinguishing it from nociceptive pain (arising from activation of intact nociceptors in response to tissue damage) and nociplastic pain (fibromyalgia, IBS — altered nociception without demonstrable nerve lesion or tissue damage).

Neuropathic pain is mechanistically distinct: it **persists beyond the healing of the original injury** and is maintained by ectopic nerve discharge, spinal cord sensitization, and cortical/thalamic reorganization — central nervous system changes that remain active even if the peripheral trigger resolves.

**Prevalence and clinical significance:**
- Prevalence: 7–10% of the general population; 25–50% of chronic pain clinic patients
- Major etiologies: diabetic peripheral neuropathy (most common, ~25% of diabetics), postherpetic neuralgia (after shingles), chemotherapy-induced peripheral neuropathy (CIPN), post-surgical neuropathy, trigeminal neuralgia, complex regional pain syndrome (CRPS), central post-stroke pain, multiple sclerosis-related pain, HIV neuropathy

**Why it matters:**
- Neuropathic pain is **poorly treated** — standard analgesics (NSAIDs, opioids) are largely ineffective; mechanisms require mechanism-specific drugs
- The concept of **central sensitization** in neuropathic pain was foundational for understanding chronic pain generally and was later extended to fibromyalgia (nociplastic pain)
- Identifying the neuropathic mechanism guides drug choice: SNRIs and TCAs for descending inhibition failure; α2δ ligands for ectopic discharge; topical agents for peripheral sensitization; NMDA antagonists for central sensitization

## Structure

### Classification by mechanism

| Mechanism | Description | Clinically relevant example |
|:---|:---|:---|
| **Peripheral sensitization** | Lowered nociceptor threshold → hyperalgesia at injury site | Post-herpetic allodynia at dermatomal site |
| **Ectopic discharge** | Injured axons fire spontaneously → burning, electric pain | Neuroma; diabetic neuropathy spontaneous pain |
| **Central sensitization** | Spinal NMDA/SP wind-up → allodynia; spread of sensitivity | CRPS; post-surgical spreading pain |
| **Loss of inhibition** | Reduced GABAergic/glycinergic interneurons in dorsal horn | Central post-stroke pain; allodynia without inflammation |
| **Descending facilitation** | RVM ON-cells amplify spinal pain signals | Chronic postsurgical pain; persistent central activation |
| **Cortical reorganization** | Somatosensory cortex maladaptive remapping | Phantom limb pain; amputation neuromas |

### Clinical phenotypes and grading

**NeuPSIG grading system (2016):**
- **Possible** neuropathic pain: pain with neuroanatomically plausible distribution + relevant history
- **Probable** neuropathic pain: + sensory examination confirms negative or positive signs in the distribution
- **Definite** neuropathic pain: + diagnostic test confirming nerve lesion

**Cardinal sensory signs:**
| Sign | Meaning | Test |
|:---|:---|:---|
| Allodynia | Pain from normally non-painful stimuli | Light touch (cotton wool), brush, cold (acetone) |
| Hyperalgesia | Enhanced pain from noxious stimuli | Von Frey filaments, pinprick |
| Spontaneous pain | Pain without identifiable stimulus | Patient report |
| Wind-up | Temporal summation — pain increases with repeated stimuli | Repeated pinprick |
| Sensory loss | Damage to small or large fibers | Quantitative sensory testing (QST); EMG/NCS |

### Key etiologies

| Condition | Mechanism | Distinguishing features |
|:---|:---|:---|
| **Diabetic peripheral neuropathy** | Metabolic axonopathy (sorbitol, AGE products, oxidative stress) → length-dependent | Stocking-glove pattern; symmetric; distal |
| **Postherpetic neuralgia** | VZV reactivation → DRG ganglionitis → central sensitization | Dermatomal allodynia; burning; brush-evoked pain |
| **Trigeminal neuralgia** | Vascular compression of trigeminal nerve root | Lancinating; triggered by touch/eating; not burning |
| **CRPS (Type I/II)** | Complex peripheral + autonomic + central sensitization | Edema, color/temperature change, spreading allodynia |
| **Chemotherapy-induced (CIPN)** | Axonopathy (platinum, taxanes, vinca alkaloids) | Length-dependent; painful or painless |
| **Central post-stroke pain** | Thalamic/spinothalamic lesion → disinhibition | Burning; ipsilateral to sensory loss; MSO-resistant |

## Function

### Peripheral mechanisms of neuropathic pain

**Ectopic discharge:**
- Damaged nerve fibers (demyelinated or severed) develop spontaneous action potential firing from injured membrane segments
- Nav1.7, Nav1.8 sodium channel upregulation at injury sites → lowered threshold → spontaneous discharge
- Ectopic discharge → burning, electric-shock, lancinating pain characteristic of neuropathic syndromes
- **Clinical correlate:** Carbamazepine blocks Nav1.7 → effective for trigeminal neuralgia (predominantly ectopic discharge mechanism)

**Peripheral sensitization:**
- Inflammatory mediators (bradykinin, PGE2, NGF) at injured nerve → sensitize nociceptors → peripheral hyperalgesia
- TRPV1 upregulation → heat allodynia; TRPA1 upregulation → cold allodynia
- **Clinically:** Topical lidocaine patches and capsaicin 8% (high-concentration TRPV1 depletion) target peripheral sensitization

### Spinal mechanisms (central sensitization in neuropathic context)

**SP-NMDA wind-up:**
- Ongoing C-fiber ectopic discharge → sustained SP release at dorsal horn → NK1R + NMDA co-activation → Ca²⁺ influx → PKC-ε activation → reduced NMDA threshold → wind-up
- Once established, dorsal horn sensitization is maintained even if peripheral input reduces — explaining chronic pain without ongoing injury

**Loss of inhibitory control:**
- Peripheral nerve injury → loss of spinal GABAergic and glycinergic interneurons in lamina II
- **KCC2 downregulation** (by microglial BDNF via TrkB): K⁺-Cl⁻ cotransporter loss → intracellular Cl⁻ rises → GABA becomes depolarizing (excitatory) rather than inhibitory → allodynia
- This BDNF-KCC2-GABA polarity reversal is among the most important discoveries in neuropathic pain neuroscience [^scholz-2002-neuropathic-pain-mechanisms]

**Descending facilitation:**
- Sustained peripheral nociceptive input → activates brainstem RVM ON-cells → descending facilitation of spinal pain transmission
- This self-amplifying loop is a key mechanism in chronic postsurgical pain and CRPS

## Pathology

### Medical comorbidities and impact

Chronic neuropathic pain carries significant psychological burden:
- Depression (40–50%): bidirectional — pain causes depression; depression amplifies pain via serotonin/NE pathway failure
- Anxiety (40–60%): anticipatory anxiety about pain episodes; kinesiophobia (fear of movement causing pain)
- Sleep disruption (>70%): pain disrupts sleep → reduced descending inhibition → more pain → worsened sleep
- Suicidal ideation (20–30% in refractory cases): neuropathic pain is a major driver of chronic pain-related suicidality

**Cortical reorganization:**
- Chronic neuropathic pain → maladaptive somatosensory cortex reorganization (Flor phantom limb studies)
- Cortical remapping maintains pain phantom even after amputation
- Effective pain treatment (dorsal root ganglion stimulation, mirror therapy) can partially reverse cortical reorganization

### Treatment

**First-line (NeuPSIG guidelines):**

| Drug | Mechanism | Indication |
|:---|:---|:---|
| **Duloxetine (30–120mg)** | SNRI; ↑ NE/5-HT descending inhibition | FDA: diabetic neuropathy; strong for CIPN |
| **Pregabalin (150–600mg)** | α2δ VGCC ligand; reduces ectopic discharge and SP release | FDA: diabetic neuropathy, postherpetic neuralgia, fibromyalgia, spinal cord injury pain |
| **Gabapentin (1800–3600mg)** | α2δ VGCC ligand | FDA: postherpetic neuralgia; widely used off-label for all neuropathic pain |
| **Amitriptyline/nortriptyline (10–75mg)** | TCA; NE/5-HT reuptake + sodium channel block | Strong evidence; first-line in UK NICE guidelines; limited by anticholinergic side effects |

**Second-line:**
| Drug | Mechanism | Notes |
|:---|:---|:---|
| **Topical lidocaine (5% patch)** | Na+ channel block; peripheral target | Postherpetic neuralgia; focal allodynia; no systemic effect |
| **Topical capsaicin 8% (Qutenza)** | TRPV1 agonist → C-fiber depletion | Single 60-min application → 3 months relief; postherpetic neuralgia; HIV neuropathy |
| **Tramadol** | Weak opioid + NE/5-HT reuptake | Moderate evidence; useful when SNRIs fail |
| **Venlafaxine** | SNRI | Strong evidence for diabetic neuropathy; less so for other types |

**Third-line (specialty use):**
- **Standard opioids:** Limited evidence; not first-line due to side effects and addiction risk; reserved for severe refractory cases
- **Ketamine IV infusions:** NMDA antagonist; effective for CRPS and refractory central sensitization; off-label; specialist setting
- **Lidocaine IV infusions:** Na+ channel stabilization; post-VATS surgery pain, CRPS
- **Spinal cord stimulation (SCS):** High-frequency or burst stimulation; FDA-approved for failed back surgery syndrome and CRPS; superior to medical therapy in controlled trials

## Connections

- `connects-to` → **[Glutamate](../../../03-molecular/glutamate/README.md)** — peripheral nerve injury → spinal NMDA receptor sensitization via substance P + glutamate co-release → central sensitization; ectopic glutamate from injured axons amplifies dorsal horn excitability; NMDA antagonists (ketamine) reduce refractory neuropathic pain; mGluR5 antagonists reduce allodynia in animal models.

- `connects-to` → **[Substance P](../../../03-molecular/substance-p/README.md)** — SP released from injured C-fibers drives NK1R-mediated dorsal horn sensitization; peripheral nerve damage → upregulated SP expression in DRG neurons → amplified spinal wind-up; SP-NMDA synergy maintains central sensitization in neuropathic pain even after peripheral healing; NK1R antagonists reduce allodynia in preclinical neuropathy models.

- `connects-to` → **[BDNF](../../../03-molecular/bdnf/README.md)** — activated microglia release BDNF in spinal dorsal horn following peripheral nerve injury; microglial BDNF activates TrkB on lamina I neurons → downregulates KCC2 → GABA becomes excitatory (depolarizing) → allodynia; this BDNF-KCC2 mechanism is one of the most important discoveries explaining neuropathic pain persistence.

- `connects-to` → **[Serotonin](../../../03-molecular/serotonin/README.md)** — descending serotonergic inhibition from raphe nuclei to spinal dorsal horn is disrupted in neuropathic pain states; duloxetine (SNRI) restores 5-HT/NE descending inhibitory tone and is FDA-approved for diabetic peripheral neuropathy; serotonergic ON-cell activity in RVM can facilitate (not just inhibit) pain signals.

- `connects-to` → **[Norepinephrine](../../../03-molecular/norepinephrine/README.md)** — descending NE inhibitory pathways from LC to spinal dorsal horn are deficient in neuropathic pain; duloxetine and TCAs (amitriptyline) achieve analgesia primarily by increasing NE in descending pain inhibitory pathways; intrathecal clonidine (α2 agonist) directly activates spinal NE receptors to reduce allodynia.

- `targets` → **[Brain](../../../06-organ/brain/README.md)** — neuropathic pain involves thalamic sensitization (reduced thalamic inhibition), ACC and posterior insula hyperactivation to pain stimuli, and maladaptive somatosensory cortex reorganization; chronic neuropathic pain reduces gray matter in ACC and dlPFC; effective treatment (SCS, mirror therapy) can partially reverse cortical reorganization.

- `connects-to` → **[Fibromyalgia](../fibromyalgia/README.md)** — FM and neuropathic pain share central sensitization mechanisms (SP-NMDA wind-up, descending inhibition failure, allodynia) but differ in origin: neuropathic pain requires a demonstrable nerve lesion while FM is classified as nociplastic pain; both respond to SNRIs (duloxetine) and α2δ VGCC ligands (pregabalin, gabapentin); small fiber neuropathy co-occurs in ~30–50% of FM patients, bridging the two categories.

- `connects-to` → **[Microglia](../../../04-cellular/microglia/README.md)** — spinal microglia are the key cellular driver of neuropathic pain: peripheral nerve injury activates microglial P2X4R → p38 MAPK phosphorylation → BDNF secretion into the dorsal horn → TrkB on lamina I neurons → KCC2 downregulation → GABA depolarizing rather than inhibitory → allodynia; CSF1R inhibitors (PLX5622, PLX3397) that ablate microglia prevent and reverse allodynia in multiple rodent neuropathy models.
- `connects-to` → **[Peripheral Nerve](../../05-tissue/peripheral-nerve/README.md)** — Neuropathic pain most often begins with a peripheral-nerve lesion: trauma, diabetes, chemotherapy or compression damages axons → ectopic firing, Nav1.7 remodeling and loss of large-fiber inhibition → spontaneous pain and allodynia; nerve conduction and skin biopsy localize it.
- `connects-to` → **[Type 2 Diabetes](../type-2-diabetes/README.md)** — Diabetes is the leading cause of neuropathic pain worldwide: chronic hyperglycemia and microvascular injury damage small sensory fibers → distal symmetric painful polyneuropathy with burning feet; glucose control slows it, and duloxetine, pregabalin and gabapentin treat the pain.
- `connects-to` → **[Parkinson's Disease](../parkinsons-disease/README.md)** — Pain is a frequent non-motor symptom of Parkinson's, including a central component from altered nociceptive processing in dopaminergic circuits; this PD pain often varies with medication 'on/off' states and can respond to dopaminergic therapy, unlike peripheral neuropathic pain.
- `connects-to` → **[Migraine](../migraine/README.md)** — Migraine and neuropathic pain share central sensitization and CGRP biology: trigeminovascular and peripheral nerves both amplify pain, and CGRP and sodium-channel mechanisms overlap—so anti-CGRP and anticonvulsant drugs help both chronic migraine and neuropathic pain.
- `connects-to` → **[Multiple Sclerosis](../multiple-sclerosis/README.md)** — Neuropathic pain is common in multiple sclerosis: demyelinating lesions along central pain pathways cause trigeminal neuralgia, Lhermitte's sign, and the burning MS hug—a major, often undertreated symptom managed with anticonvulsants and antidepressants.
- `connects-to` → **[Astrocyte](../../04-cellular/astrocyte/README.md)** — Astrocytes, with microglia, sustain chronic neuropathic pain: after nerve injury reactive astrocytes in the spinal dorsal horn release cytokines and disturb glutamate handling—so glial activation, not just neurons, maintains the chronic pain state.
- `connects-to` → **[Guillain-Barré Syndrome](../../05-tissue/guillain-barre/README.md)** — Guillain-Barré syndrome can leave chronic neuropathic pain: acute autoimmune demyelination of peripheral nerves causes severe pain during the illness, and damaged, abnormally firing nerves can produce lasting neuropathic pain even after motor recovery.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — Neuropathic pain arises from maladaptive changes in neurons: injured sensory neurons become hyperexcitable, fire spontaneously and rewire their connections, so pain persists without ongoing tissue damage—the nervous system generating pain from its own circuitry.
- `connects-to` → **[Opioid Use Disorder](../opioid-use-disorder/README.md)** — Neuropathic pain is the setting where opioids both disappoint and endanger: opioids work poorly for neuropathic pain yet are often prescribed, fueling tolerance, dependence and opioid use disorder—so guidelines favor antidepressants and gabapentinoids.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Voltage-gated calcium channels are the target of first-line neuropathic-pain drugs: gabapentin and pregabalin bind the alpha-2-delta subunit, cutting calcium-driven release of pain neurotransmitters from overexcitable sensory neurons—linking calcium to pain control.
- `connects-to` → **[GABA](../../03-molecular/gaba/README.md)** — Neuropathic pain partly reflects lost GABAergic inhibition: nerve injury weakens inhibitory GABA signaling in the spinal dorsal horn, so normally innocuous touch is read as pain (allodynia)—restoring this inhibitory tone is a key analgesic strategy.
- `connects-to` → **[Varicella-Zoster Virus](../../../02-pathogen/01-viruses/varicella-zoster-virus/README.md)** — Varicella-zoster virus is a leading cause of neuropathic pain: after shingles, virus-damaged sensory nerves can fire abnormally for months as postherpetic neuralgia, the classic post-infectious neuropathic pain—now largely preventable by zoster vaccination.
- `connects-to` → **[Sodium](../../02-atomic/sodium/README.md)** — Voltage-gated sodium channels generate neuropathic pain: after nerve injury, damaged neurons over-express Nav1.7 and Nav1.8 and fire spontaneously, so sodium-channel blockers—local anesthetics, mexiletine, and the new Nav1.8 inhibitor suzetrigine—are core analgesics.
- `connects-to` → **[Potassium](../../02-atomic/potassium/README.md)** — Potassium channels are the brakes on pain firing: by setting resting voltage and repolarizing neurons, Kv/KCNQ channels limit excitability, so their loss after nerve injury leaves neurons hyperexcitable—making potassium-channel openers a target for nerve pain.
- `connects-to` → **[Endocannabinoid System](../../03-molecular/endocannabinoid/README.md)** — The endocannabinoid system dampens neuropathic pain: cannabinoid receptors on neurons and microglia suppress pain transmission and neuroinflammation, which is why cannabinoids are tried for nerve pain—though benefit is modest and tempered by side effects.
- `connects-to` → **[CGRP](../../03-molecular/cgrp/README.md)** — CGRP is a key pain neuropeptide alongside substance P: released from sensory nerves, it sensitizes pain pathways and dilates vessels, and blocking it controls migraine—illustrating how neuropeptides amplify the signaling that becomes chronic neuropathic pain.
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — Magnesium dampens neuropathic pain at the NMDA receptor: it normally plugs the channel that drives central sensitization, so low magnesium unmasks pain amplification and magnesium infusion is used to blunt it—linking a simple ion to chronic pain.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — Small-fiber neuropathic pain is diagnosed in the skin: a skin biopsy measuring intraepidermal nerve-fiber density reveals the loss of tiny pain fibers, and capsaicin patches treat the skin's overactive nociceptors—making skin both a diagnostic and therapeutic site.
- `connects-to` → **[TNF-α (Tumor Necrosis Factor-alpha)](../../03-molecular/tnf-alpha/README.md)** — Neuropathic pain is sustained by TNF and neuroinflammation: injured nerves and activated glia release TNF-alpha that sensitizes pain neurons, turning a transient injury into chronic pain—why the immune system is a target for hard-to-treat pain.
- `connects-to` → **[Dopamine](../../03-molecular/dopamine/README.md)** — Dopamine sets the brain's pain volume: descending dopamine pathways and the reward system modulate how much pain is felt and how much it bothers, so low dopamine (as in Parkinson's) lowers the pain threshold and worsens chronic pain.
- `connects-to` → **[Mast Cell](../../04-cellular/mast-cell/README.md)** — Mast cells inflame injured nerves into pain: clustered around peripheral nerves, they release histamine, proteases, and cytokines that sensitize nociceptors, linking the immune system to the burning pain of nerve injury and CRPS.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Nerve injury summons macrophages that sustain pain: they swarm the damaged nerve and dorsal-root ganglion, releasing cytokines that sensitize sensory neurons, so this neuroimmune attack helps turn a transient injury into chronic neuropathic pain.
- `connects-to` → **[Synapse](../../05-tissue/synapse/README.md)** — Neuropathic pain is burned in at the synapse: relentless input strengthens spinal dorsal-horn synapses (central sensitization), so the cord amplifies signals and even gentle touch is read as pain long after the injury heals.
- `connects-to` → **[ATP (Adenosine Triphosphate)](../../03-molecular/atp/README.md)** — ATP is a pain signal outside the cell: released from damaged tissue and nerves, it fires purinergic receptors on sensory neurons and microglia, a key trigger that switches on the spinal microglia driving neuropathic pain.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Small-fiber neuropathy is confirmed under the microscope: a skin punch biopsy, immunostained and read in light, counts the thinned nerve endings behind unexplained burning pain that routine tests miss.
- `connects-to` → **[Mu-Opioid Receptor](../../03-molecular/mu-opioid-receptor/README.md)** — Neuropathic pain resists opioids: nerve injury strips mu-opioid receptors from damaged neurons and stirs glia, so morphine-type drugs work poorly here, pushing treatment toward gabapentinoids and antidepressants.
- `connects-to` → **[Oligodendrocyte](../../04-cellular/oligodendrocyte/README.md)** — Lost myelin makes nerves misfire: when oligodendrocytes and their peripheral counterparts fail, demyelinated axons fire ectopically and cross-talk, generating the shooting, electric pains of conditions like MS.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy shows the damaged nerve behind the pain: demyelinated and degenerating axons, and the dropout of fine unmyelinated fibers in small-fiber neuropathy, leave bared, hyperexcitable membranes that fire on their own.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — Nerve damage can silence the heart's warnings: diabetic cardiac autonomic neuropathy blunts the pain of a heart attack into a 'silent' one and destabilizes heart rate and blood pressure, a dangerous extension of peripheral nerve disease.
- `connects-to` → **[Vitamin D (Calciferol)](../../../03-medicine/03-food/vitamin-d/README.md)** — Vitamin D deficiency frays the nerves: low levels are tied to more severe diabetic and other peripheral neuropathies, and the vitamin's role in nerve growth factor and repair makes supplementation a studied adjunct for the pain.
- `connects-to` → **[Adenosine](../../03-molecular/adenosine/README.md)** — Adenosine quiets pain at the spinal cord: acting on A1 receptors it hyperpolarizes pain neurons and dampens transmission, a built-in analgesic brake that drugs and even acupuncture are thought to recruit against neuropathic pain.
- `connects-to` → **[Cytotoxic T Cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Neuropathic pain is partly an immune disease: T cells infiltrate injured nerves and dorsal root ganglia, releasing cytokines that sensitize pain neurons — which is why the pain outlasts the injury and resists ordinary painkillers.
- `connects-to` → **[Acetylcholine](../../03-molecular/acetylcholine/README.md)** — Cholinergic signaling soothes the pain pathway: spinal muscarinic and nicotinic receptors blunt pain transmission, so boosting acetylcholine is one mechanism behind certain analgesics and a target explored for neuropathic pain.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — Antibodies both cause and treat nerve pain: autoantibodies against gangliosides and MAG drive the painful neuropathies of GBS and CIDP, while anti-NGF monoclonal antibodies like tanezumab were developed to silence pain at its growth-factor source.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — Pain and mood share circuits and drugs: chronic neuropathic pain breeds depression, the two amplifying each other through overlapping serotonin-noradrenaline pathways, which is why SNRIs and tricyclics treat both at once.
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — The kidney both causes and constrains: uremic neuropathy makes the nerves ache in kidney failure, and because gabapentin and pregabalin are cleared renally, their doses must be cut to avoid toxic accumulation in these patients.
- `connects-to` → **[Interleukin-6](../../03-molecular/il-6/README.md)** — Cytokines sensitize the injured nerve: IL-6 released after nerve damage lowers the firing threshold of pain neurons and recruits immune cells, helping turn a transient injury into the persistent firing of neuropathic pain.
- `connects-to` → **[Sjögren's Syndrome](../sjogrens-syndrome/README.md)** — Autoimmune dryness can attack the nerves: Sjögren's syndrome causes a sensory neuronopathy and small-fiber neuropathy, the immune assault on dorsal root ganglia producing burning, painful numbness even with little joint disease.
- `connects-to` → **[HIV/AIDS](../hiv-aids/README.md)** — HIV is a global cause of painful neuropathy: the virus and some antiretroviral drugs both damage long sensory axons, producing a distal symmetric polyneuropathy with burning feet that is among the infection's most common neurologic complications.

[^jensen-2011-neuropathic-pain-review]: Jensen TS, Baron R, Haanpää M, et al. A new definition of neuropathic pain. *Pain.* 2011;152(10):2204-2205. [doi:10.1016/j.pain.2011.06.017](https://doi.org/10.1016/j.pain.2011.06.017) · [PubMed 21764514](https://pubmed.ncbi.nlm.nih.gov/21764514/)
[^dworkin-2010-neuropathic-pain-treatment]: Dworkin RH, O'Connor AB, Audette J, et al. Recommendations for the pharmacological management of neuropathic pain. *Mayo Clin Proc.* 2010;85(3 Suppl):S3-14. [doi:10.4065/mcp.2009.0649](https://doi.org/10.4065/mcp.2009.0649) · [PubMed 20194146](https://pubmed.ncbi.nlm.nih.gov/20194146/)
[^scholz-2002-neuropathic-pain-mechanisms]: Scholz J, Woolf CJ. Can we conquer pain? *Nat Neurosci.* 2002;5(Suppl):1062-1067. [doi:10.1038/nn942](https://doi.org/10.1038/nn942) · [PubMed 12403987](https://pubmed.ncbi.nlm.nih.gov/12403987/)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
