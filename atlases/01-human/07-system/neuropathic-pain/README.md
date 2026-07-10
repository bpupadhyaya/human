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
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "Failing kidneys poison the nerves: uremic toxins that build up in chronic kidney disease damage peripheral axons, producing a uremic polyneuropathy with burning, restless legs that improves only with dialysis or transplant."
  - target: 01-human/03-molecular/prostaglandins
    relation: connects-to
    note: "Inflammation lowers the firing threshold: prostaglandins released at injured tissue sensitize nociceptor endings, a peripheral sensitization that primes the nerves and feeds the central amplification of neuropathic pain."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: connects-to
    note: "The immune system can also quiet pain: regulatory T cells help resolve neuropathic pain by damping the neuroinflammation around injured nerves, so their relative deficiency lets pain persist — a neuroimmune lever for new therapies."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "Glial inflammation runs on NF-κB: activated microglia and astrocytes around injured nerves switch on NF-κB to pour out the cytokines that sensitize pain pathways, a central engine of the chronic neuroinflammation behind neuropathic pain."
  - target: 01-human/07-system/type-1-diabetes
    relation: connects-to
    note: "Even tightly controlled diabetes can hurt the nerves: type 1 diabetes causes a distal sensorimotor polyneuropathy through chronic hyperglycemia and microvascular nerve injury, one of the commonest sources of painful peripheral neuropathy."
  - target: 01-human/07-system/insomnia-disorder
    relation: connects-to
    note: "Pain and sleeplessness feed each other: neuropathic pain flares at night and fragments sleep, while the resulting insomnia lowers pain tolerance the next day, a vicious cycle that worsens both."
  - target: 01-human/07-system/stroke
    relation: connects-to
    note: "A brain infarct can itself become a pain generator: damage to the thalamus or spinothalamic pathways produces central post-stroke pain (Dejerine-Roussy), a relentless neuropathic pain arising from the injured central nervous system."
  - target: 01-human/07-system/diabetic-retinopathy
    relation: connects-to
    note: "Two faces of the same microvascular damage: painful diabetic neuropathy and diabetic retinopathy arise from the same chronic hyperglycemic injury to small vessels and nerves, so they commonly travel together in long-standing diabetes."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "Anxiety turns up the pain volume: chronic worry heightens attention to pain and lowers its threshold, and persistent neuropathic pain in turn fuels anxiety — a two-way amplification rooted in shared limbic circuitry."
  - target: 01-human/07-system/alcohol-use-disorder
    relation: connects-to
    note: "Heavy drinking poisons the peripheral nerves: chronic alcohol use, with its associated thiamine and B-vitamin deficiency, causes a length-dependent axonal neuropathy that produces burning neuropathic pain in the feet."
  - target: 01-human/07-system/multiple-myeloma
    relation: connects-to
    note: "Its plasma-cell disease and treatment both hit nerves: amyloid deposition and tumor can injure nerves in multiple myeloma, and the bortezomib used to treat it causes a painful, dose-limiting peripheral neuropathy."
  - target: 01-human/07-system/colorectal-cancer
    relation: connects-to
    note: "Its chemotherapy leaves nerves raw: the oxaliplatin in colorectal-cancer regimens causes a cold-triggered and chronic peripheral neuropathy, a leading example of chemotherapy-induced neuropathic pain."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "It is a disease of the nervous system itself: neuropathic pain arises from damage or dysfunction anywhere along the somatosensory pathway, from peripheral nerves to the spinal cord and brain, with central sensitisation amplifying it."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "Spine disease pinches the nerves: a herniated disc or degenerative stenosis compressing a nerve root causes radiculopathy and sciatica, a very common musculoskeletal source of neuropathic pain."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "Its mainstay drugs constipate the gut: the opioids, tricyclics and gabapentinoids used to treat neuropathic pain all slow intestinal transit, making constipation a common, limiting side effect."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "It is read and treated through the skin: small-fibre neuropathy is diagnosed by skin biopsy, postherpetic neuralgia and CRPS bring skin allodynia and trophic changes, and topical capsaicin and lidocaine patches relieve it."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "The immune system can attack nerves: immune-mediated neuropathies such as Guillain-Barré, CIDP and vasculitic neuropathy damage peripheral nerves and are important, treatable causes of neuropathic pain."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "Autonomic and vascular nerve injury intertwine: autonomic neuropathy causes orthostatic hypotension, while ischaemia from peripheral vascular disease itself injures nerves and produces painful neuropathy."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "Hormonal disease is its leading cause: diabetes is the commonest cause of peripheral neuropathy worldwide, and hypothyroidism and other endocrine disorders also damage nerves."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "Its drugs can suppress breathing: the gabapentinoids and opioids used to treat neuropathic pain cause respiratory depression, especially when combined or in older patients."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "The kidney both causes and constrains it: uraemia causes a peripheral neuropathy, and renal impairment mandates dose reduction of the renally-cleared gabapentin and pregabalin."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "It strikes the pelvis too: pudendal neuralgia and other pelvic neuropathic pain syndromes affect sexual and urinary function, a distressing and under-recognised form."
  - target: 03-medicine/01-modern/10-mental-health/fluoxetine
    relation: connects-to
    note: "Antidepressants are core analgesics: SNRIs like duloxetine and tricyclics relieve neuropathic pain by boosting descending serotonin-noradrenaline inhibition, the pathway SSRIs like fluoxetine also touch."
  - target: 01-human/07-system/cidp
    relation: connects-to
    note: "A treatable demyelinating cause: chronic inflammatory demyelinating polyneuropathy causes neuropathic pain that, unlike most, responds to immunotherapy rather than analgesics alone."
  - target: 03-medicine/01-modern/13-cancer/cancer-chemotherapy
    relation: connects-to
    note: "Chemo is a leading iatrogenic cause: platinum, taxane, vincristine and bortezomib chemotherapies produce chemotherapy-induced peripheral neuropathy, a dose-limiting, often lasting neuropathic pain in cancer survivors."
  - target: 01-human/05-tissue/axonal-transport
    relation: connects-to
    note: "Failing axons fire abnormally: many neuropathic pains arise from a dying-back axonopathy where disrupted axonal transport starves the distal nerve, generating ectopic impulses felt as burning, length-dependent pain."
  - target: 01-human/07-system/cannabis-use-disorder
    relation: connects-to
    note: "Cannabinoids are sought for refractory pain: medical cannabis is widely used for neuropathic pain via the endocannabinoid system, with modest evidence and the attendant risk of cannabis use disorder."
  - target: 01-human/07-system/epilepsy
    relation: connects-to
    note: "Shared neuronal hyperexcitability: neuropathic pain and epilepsy both arise from over-excitable neurons with disordered sodium-channel and GABA signalling, which is why anticonvulsants like gabapentin, pregabalin and carbamazepine treat both."
  - target: 01-human/07-system/anca-vasculitis
    relation: connects-to
    note: "It inflames the nerves' blood supply: ANCA-associated vasculitis causes a vasculitic neuropathy (mononeuritis multiplex) by occluding the small vessels feeding peripheral nerves, a painful cause of neuropathic pain."
  - target: 01-human/07-system/hepatitis-c
    relation: connects-to
    note: "Cryoglobulins attack the nerves: chronic hepatitis C generates cryoglobulin immune complexes that inflame the vasa nervorum, causing a painful sensorimotor neuropathy—an infectious driver of neuropathic pain."
  - target: 01-human/07-system/sickle-cell-disease
    relation: connects-to
    note: "Pain that turns neuropathic: recurrent vaso-occlusive crises in sickle cell disease drive central sensitisation and a peripheral neuropathy, so chronic sickle pain acquires a neuropathic character needing adjuvant agents."
  - target: 01-human/07-system/breast-cancer
    relation: connects-to
    note: "Chemotherapy-induced neuropathy: the taxane and platinum regimens used for cancers like breast cancer commonly cause a dose-limiting, painful peripheral neuropathy (CIPN) that can persist long after treatment."
  - target: 01-human/07-system/hereditary-pancreatitis
    relation: connects-to
    note: "Neuropathic visceral pain: chronic and hereditary pancreatitis cause severe pain partly through neuropathic mechanisms—perineural inflammation and pancreatic nerve remodelling—not just ductal obstruction."
  - target: 01-human/07-system/nmo
    relation: connects-to
    note: "Central neuropathic pain: neuromyelitis optica causes painful tonic spasms and severe central pain from its longitudinally extensive spinal-cord lesions, a disabling neuropathic-pain syndrome distinct from peripheral causes."
  - target: 01-human/07-system/covid-19-disease
    relation: connects-to
    note: "Post-viral neuropathy: both acute COVID-19 and long COVID can cause a small-fibre neuropathy and new neuropathic pain, adding SARS-CoV-2 to the viral triggers of painful nerve injury alongside shingles and HIV."
  - target: 01-human/05-tissue/hippocampus
    relation: connects-to
    note: "Pain's emotional brain: chronic neuropathic pain remodels the hippocampus and limbic circuits, driving the memory impairment, depression and catastrophising that accompany it as central sensitisation engages emotional centres."
  - target: 01-human/03-molecular/nlrp3-inflammasome
    relation: connects-to
    note: "Glial inflammasome: NLRP3-inflammasome activation in microglia and macrophages around injured nerves sustains the neuroinflammation that drives neuropathic pain."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "Neuronal sensitisation: IL-1β released by activated glia sensitises nociceptive neurons, lowering their firing threshold to produce the hypersensitivity of neuropathic pain."
  - target: 01-human/03-molecular/npy
    relation: connects-to
    note: "Injured-neuron signal: neuropeptide Y is strongly upregulated in injured sensory neurons and modulates the abnormal signalling underlying neuropathic pain."
  - target: 01-human/03-molecular/ccl2
    relation: connects-to
    note: "Microglial recruitment: nerve injury drives CCL2 release that recruits and activates spinal microglia and monocytes through CCR2, a key chemokine axis initiating the neuroinflammation behind neuropathic pain."
  - target: 01-human/03-molecular/tlr4
    relation: connects-to
    note: "Danger-signal sensing: TLR4 on glia detects DAMPs released by injured nerves, triggering the microglial activation and cytokine release that establish central sensitisation in neuropathic pain."
  - target: 01-human/03-molecular/serotonin-transporter
    relation: connects-to
    note: "Descending modulation: serotonin-transporter activity sets serotonergic tone in descending pain pathways, the target of SNRIs like duloxetine that are first-line drugs for neuropathic pain."
  - target: 01-human/03-molecular/ntrk
    relation: connects-to
    note: "NGF sensitisation: nerve growth factor signalling through TrkA sensitises and upregulates nociceptors after nerve injury, the mechanism that anti-NGF antibodies (tanezumab) target to relieve chronic pain."
  - target: 01-human/03-molecular/nitric-oxide
    relation: connects-to
    note: "Central amplification: NMDA-receptor activation in the dorsal horn drives nNOS-derived nitric oxide that potentiates synaptic transmission, a positive-feedback loop reinforcing the central sensitisation of neuropathic pain."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "Chemokine sensitisation: CXCL12 acting on CXCR4 in the dorsal-root ganglia and spinal cord directly excites and sensitises nociceptive neurons, a neuro-glial signal sustaining chronic neuropathic pain after nerve injury."
  - target: 01-human/03-molecular/oxytocin
    relation: connects-to
    note: "Descending analgesia: oxytocinergic projections from the hypothalamic paraventricular nucleus to the spinal dorsal horn inhibit nociceptive transmission, an endogenous analgesic pathway being explored therapeutically for neuropathic pain."
  - target: 01-human/03-molecular/rage
    relation: connects-to
    note: "Diabetic neuropathy: advanced glycation end-products signalling through RAGE injure peripheral nerves and sensitise nociceptors, a central mechanism of the painful diabetic neuropathy that is among the commonest causes of neuropathic pain."
  - target: 01-human/03-molecular/perforin
    relation: connects-to
    note: "Adaptive-immune pain: infiltrating CD8 T cells releasing perforin and granzyme contribute to the maintenance of neuropathic pain after nerve injury, a T-cell arm of neuroimmune sensitisation distinct from the better-known microglial component."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "Resolution cytokine: anti-inflammatory IL-10 suppresses the glial pro-inflammatory cytokines (IL-1β, IL-6 and TNF-α already mapped) that sustain neuropathic pain, the rationale for IL-10-based pain-resolution strategies."
  - target: 01-human/03-molecular/connexin43
    relation: connects-to
    note: "Astrocytic spread: astrocytic connexin-43 gap junctions and hemichannels propagate central sensitisation across the spinal dorsal horn, releasing ATP and glutamate (already mapped) that amplify and spread neuropathic pain."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "Analgesic restraint: TGF-β exerts a neuroprotective, analgesic influence that restrains microglial activation in neuropathic pain, and its loss permits the neuroinflammation that maintains the chronic pain state."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "Central sensitization: BDNF-TrkB (BDNF and NTRK mapped) and inflammatory signalling activate MAPK-ERK in dorsal-horn neurons and microglia, driving the central sensitization that amplifies neuropathic pain."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "Translation-dependent maintenance: spinal mTOR-driven protein synthesis sustains the long-term central sensitization that maintains the chronic neuropathic pain state."
  - target: 01-human/03-molecular/myd88
    relation: connects-to
    note: "Microglial activation: TLR4 (mapped) signalling through MyD88 activates spinal microglia after nerve injury, a key neuroinflammatory amplifier of neuropathic pain."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "PI3K-AKT signalling downstream of neurotrophin (NTRK/BDNF mapped) and cytokine receptors drives the central and peripheral sensitisation underlying neuropathic pain."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "Glial JAK-STAT signalling transduces the IL-6/cytokine milieu (IL-6 mapped) into the reactive astro-microgliosis that sustains neuropathic pain."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "IL-17A from infiltrating T cells sensitises nociceptors and amplifies spinal glial activation, contributing to chronic neuropathic pain."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Galectin-3 released by activated spinal microglia amplifies the neuroinflammation and central sensitisation that sustain chronic neuropathic pain."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "JAK-STAT3 signalling (JAK1/2 already mapped) in spinal glia drives the reactive gliosis that maintains chronic neuropathic pain."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "GSK-3β signalling in dorsal-horn neurons contributes to the synaptic plasticity underlying the central sensitisation of neuropathic pain."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "Cytosolic DNA sensing through cGAS-STING in spinal microglia and macrophages contributes to the neuroinflammation that sustains neuropathic pain."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "IFN-STAT1 signaling in spinal microglia drives the neuroinflammatory sensitization that maintains neuropathic pain."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "FOXO regulates neuronal oxidative-stress and survival pathways relevant to the maladaptive plasticity of neuropathic pain."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "PI3K (PIK3CA)-AKT signaling (AKT already mapped) in dorsal-horn neurons and glia contributes to the central sensitization of neuropathic pain."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "S100A8/A9 alarmins released after nerve injury amplify the neuroinflammation underlying neuropathic pain."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "HIF-1α in injured nerve and dorsal-root ganglia contributes to the metabolic and inflammatory adaptation driving neuropathic pain."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK-linked metabolic signaling modulates the neuronal and glial responses underlying the central sensitization of neuropathic pain."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC-family kinase signaling, via microglial P2X4 and NMDA-receptor phosphorylation, participates in the central sensitization of neuropathic pain."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "DNMT3A-mediated DNA methylation contributes to the epigenetic reprogramming of the dorsal-root-ganglion neurons in neuropathic pain."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Autophagy modulates the neuronal and glial homeostasis and the Wallerian degeneration implicated in neuropathic pain."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-driven microglial and macrophage recruitment participates in the neuroinflammation driving neuropathic pain."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Complement C3 signaling participates in the microglial synaptic remodeling and neuroinflammation of neuropathic pain."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "IL-33 alarmin signaling participates in the glial and neuroinflammatory responses of neuropathic pain."
  - target: 01-human/03-molecular/arid1a
    relation: connects-to
    note: "ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic regulation of the pain-sensitization gene programs of neuropathic pain."
  - target: 01-human/03-molecular/calcineurin
    relation: connects-to
    note: "Calcineurin-NFAT signaling participates in the neuroimmune and glial activation of neuropathic pain."
  - target: 01-human/03-molecular/insulin
    relation: connects-to
    note: "Diabetic neuropathy: the most common cause of neuropathic pain is diabetic peripheral neuropathy, where hyperglycaemia and impaired insulin signalling injure sensory axons through metabolic and microvascular mechanisms (RAGE already mapped)."
  - target: 01-human/03-molecular/estrogen
    relation: connects-to
    note: "Sex differences: chronic and neuropathic pain are more prevalent and often more severe in women, and estrogen modulates nociceptive processing and glial activity, contributing to the sex differences in pain sensitivity and treatment response."
  - target: 01-human/03-molecular/glucocorticoid-receptor
    relation: connects-to
    note: "Anti-inflammatory therapy: corticosteroids acting through the glucocorticoid receptor are used, including as epidural injections, to relieve the inflammatory and compressive components of radicular neuropathic pain by dampening neuroinflammation."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "Reparative immunity: IL-4 polarises macrophages toward a reparative M2 phenotype and, with IL-10 (already mapped), dampens the neuroinflammation after nerve injury, so the type-2 immune arm helps resolve neuropathic pain."
  - target: 01-human/03-molecular/xanthine-oxidase
    relation: connects-to
    note: "Oxidative sensitisation: reactive oxygen species from xanthine oxidase and other sources accumulate after nerve injury and sensitise nociceptive pathways, an oxidative mechanism contributing to the persistence of neuropathic pain."
  - target: 01-human/03-molecular/histamine
    relation: connects-to
    note: "Histaminergic modulation: histamine acting on H1 and H3 receptors modulates both itch and pain signalling in sensory pathways, one of the neuromodulator systems (substance P already mapped) that shape the neuropathic pain and itch of nerve injury."
  - target: 01-human/03-molecular/bradykinin
    relation: connects-to
    note: "Nociceptor sensitisation: bradykinin acting on B1 and B2 receptors, induced after nerve injury and inflammation, sensitises nociceptors and lowers their firing threshold (prostaglandins and substance P already mapped), amplifying neuropathic pain."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "Type-2 neuroimmune resolution: IL-13, with IL-4 (already mapped), polarises macrophages toward a reparative phenotype at the injured nerve, part of the neuroimmune balance that influences whether pain resolves or becomes chronic."
  - target: 01-human/03-molecular/melatonin
    relation: connects-to
    note: "Analgesia and sleep: melatonin has analgesic and anti-inflammatory effects and restores the sleep disrupted by chronic pain (serotonin already mapped), and the pain-sleep loop it addresses is central to the burden of neuropathic pain."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Calcium channels and the α2δ target: voltage-gated calcium channels drive the neurotransmitter release (glutamate already mapped) of pain signalling, and their α2δ subunit is the target of gabapentin and pregabalin used for neuropathic pain."
  - target: 01-human/04-cellular/astrocyte
    relation: connects-to
    note: "Astrocytic sensitisation: reactive astrocytes, with the microglia (already mapped), sustain central sensitisation in the dorsal horn through gap junctions (connexin43 already mapped) and gliotransmitters, maintaining chronic neuropathic pain."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "Central pain and affect: the brain reorganises in chronic neuropathic pain, with thalamocortical changes and the affective and cognitive dimensions (serotonin and noradrenaline already mapped) that the SNRIs and psychological therapies address."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "Zinc and NMDA modulation: zinc modulates the NMDA receptor of the glutamate (already mapped) signalling of central sensitisation, and disturbed zinc handling affects the pain processing of neuropathic pain."
  - target: 01-human/02-atomic/potassium
    relation: connects-to
    note: "Potassium-channel excitability: the downregulation of the voltage-gated potassium (Kv) channels after nerve injury raises the neuronal (already mapped) excitability and drives the ectopic firing of neuropathic pain."
  - target: 01-human/07-system/stroke
    relation: connects-to
    note: "Central post-stroke pain: the thalamic and other central lesions of stroke cause central post-stroke pain, a classic central neuropathic pain arising from the reorganised brain (already mapped)."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Metabolic-pain adipokine: leptin modulates the pain via the leptin-driven microglial (already mapped) activation, linking the metabolic state to the central sensitization of neuropathic pain."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Metabolic adipokine: adiponectin, with leptin (already mapped), modulates the neuroinflammation (TNF and IL-6 already mapped) and the pain of neuropathic pain."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), is the pro-inflammatory adipokine linking the metabolic state to the neuroinflammation of neuropathic pain."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Innate neuroinflammation: the type-I interferon, downstream of the cGAS-STING (already mapped) pathway, contributes to the glial (microglia already mapped) neuroinflammation that sustains neuropathic pain."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Th1 neuroinflammation: the IFN-γ of the infiltrating T cells is the type-II interferon arm of the immune contribution (TNF and IL-1 already mapped) to the central sensitisation of neuropathic pain."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the immune-inflammatory dimension of neuropathic pain."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the neuroimmune interaction in neuropathic pain."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the neuroimmune contribution to the central sensitisation of neuropathic pain."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the neuroimmune interaction in neuropathic pain."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "CD4 neuroimmune arm: the CD4 T-helper cells infiltrate the injured nerve and dorsal-root ganglion and, via the Th1/Th2/Th17 (IFN-γ, IL-4 and IL-17 already mapped) cytokines, modulate the neuropathic pain."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "NK nerve clearance: the NK cells (perforin already mapped) infiltrate the injured nerve and, by clearing the damaged sensory neurons (already mapped), modulate the resolution or persistence of neuropathic pain."
  - target: 01-human/03-molecular/c5ar1
    relation: connects-to
    note: "Complement C5a receptor: the C5aR1 signalling (with the complement C3 already mapped), activated after nerve injury, drives the myeloid recruitment and the neuroinflammation that sensitises the nociceptors of neuropathic pain."
  - target: 01-human/03-molecular/complement-c5
    relation: connects-to
    note: "Terminal complement: the complement C5 and its C5a (with C3 and C5aR1 already mapped) are generated after nerve injury and drive the membrane-attack and the neuroinflammation that sensitises the nociceptors of neuropathic pain."
  - target: 01-human/03-molecular/factor-h
    relation: connects-to
    note: "Complement regulation: factor H regulates the alternative complement pathway (complement C3, C5 and C5aR1 already mapped) of the post-nerve-injury complement activation of neuropathic pain."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "Nerve antigen presentation: the dendritic cells of the injured nerve and CNS-border compartments present antigen to the T cells (already mapped) in the neuroinflammation of neuropathic pain."
  - target: 01-human/03-molecular/tslp
    relation: connects-to
    note: "Neuro-epithelial alarmin: TSLP, released from keratinocytes (skin already mapped) and glial cells under neuropathic insult, activates mast cells (already mapped) and dendritic cells (already mapped), amplifying the peripheral sensitisation of neuropathic pain."
  - target: 01-human/03-molecular/c1-esterase-inhibitor
    relation: connects-to
    note: "Complement/kinin gate: C1-esterase inhibitor limits classical complement (C3, C5 and C5aR1 already mapped) and contact-kinin activation in the injured nerve microenvironment, restraining complement-driven neuroinflammation of neuropathic pain."
  - target: 01-human/03-molecular/erythropoietin
    relation: connects-to
    note: "Neuroprotective cytokine: erythropoietin, acting via EPOR on neurons and Schwann cells (peripheral nerve already mapped), promotes axonal survival and remyelination and attenuates the neuro-inflammatory sensitisation of neuropathic pain."
  - target: 01-human/03-molecular/periostin
    relation: connects-to
    note: "ECM-repair scaffold: periostin, expressed in injured peripheral nerve endoneurium and DRG supporting cells, promotes the re-organisation of the extracellular matrix and glial scar and modulates the fibrotic neuroinflammatory microenvironment of neuropathic pain."
  - target: 01-human/03-molecular/prolactin
    relation: connects-to
    note: "Immune-endocrine pain modulator: prolactin, acting via PRLR on DRG neurons and immune cells in the nerve injury site, sensitises peripheral nociceptors and amplifies the pro-inflammatory cytokine (IL-6 and TNF-α already mapped) signalling of neuropathic pain."
  - target: 01-human/03-molecular/testosterone
    relation: connects-to
    note: "Androgen neuroprotection: testosterone, acting via androgen receptors on DRG neurons and Schwann cells (peripheral nerve already mapped), promotes axonal repair and attenuates the neuro-inflammatory sensitisation underlying the sex-differential severity of neuropathic pain."
  - target: 01-human/03-molecular/vasopressin
    relation: connects-to
    note: "NP vasopressin: vasopressin V1A receptors in dorsal horn neurons modulate spinal nociception; vasopressin interacts with oxytocin (already mapped) antinociceptive circuits and attenuates the serotonin (already mapped) descending pain-inhibitory dysfunction of neuropathic pain."
  - target: 01-human/03-molecular/transferrin
    relation: connects-to
    note: "NP transferrin: transferrin-mediated iron transport is essential for myelin synthesis and axonal function (peripheral nerve already mapped); iron dyshomeostasis amplifies the oxidative stress driving the neuroinflammatory sensitisation and axonal damage of neuropathic pain."
  - target: 01-human/02-atomic/copper
    relation: connects-to
    note: "NP copper: copper deficiency impairs the myelination of peripheral nerves (already mapped) and reduces superoxide dismutase-mediated antioxidant protection; copper dyshomeostasis amplifies the neuroinflammatory sensitisation and oxidative injury of neuropathic pain."
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
- `connects-to` → **[Chronic Kidney Disease](../ckd/README.md)** — Failing kidneys poison the nerves: uremic toxins that build up in chronic kidney disease damage peripheral axons, producing a uremic polyneuropathy with burning, restless legs that improves only with dialysis or transplant.
- `connects-to` → **[Prostaglandins (Eicosanoids)](../../03-molecular/prostaglandins/README.md)** — Inflammation lowers the firing threshold: prostaglandins released at injured tissue sensitize nociceptor endings, a peripheral sensitization that primes the nerves and feeds the central amplification of neuropathic pain.
- `connects-to` → **[Regulatory T Cell](../../04-cellular/regulatory-t-cell/README.md)** — The immune system can also quiet pain: regulatory T cells help resolve neuropathic pain by damping the neuroinflammation around injured nerves, so their relative deficiency lets pain persist — a neuroimmune lever for new therapies.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — Glial inflammation runs on NF-κB: activated microglia and astrocytes around injured nerves switch on NF-κB to pour out the cytokines that sensitize pain pathways, a central engine of the chronic neuroinflammation behind neuropathic pain.
- `connects-to` → **[Type 1 Diabetes](../type-1-diabetes/README.md)** — Even tightly controlled diabetes can hurt the nerves: type 1 diabetes causes a distal sensorimotor polyneuropathy through chronic hyperglycemia and microvascular nerve injury, one of the commonest sources of painful peripheral neuropathy.
- `connects-to` → **[Insomnia Disorder](../insomnia-disorder/README.md)** — Pain and sleeplessness feed each other: neuropathic pain flares at night and fragments sleep, while the resulting insomnia lowers pain tolerance the next day, a vicious cycle that worsens both.
- `connects-to` → **[Stroke](../stroke/README.md)** — A brain infarct can itself become a pain generator: damage to the thalamus or spinothalamic pathways produces central post-stroke pain (Dejerine-Roussy), a relentless neuropathic pain arising from the injured central nervous system.
- `connects-to` → **[Diabetic Retinopathy](../diabetic-retinopathy/README.md)** — Two faces of the same microvascular damage: painful diabetic neuropathy and diabetic retinopathy arise from the same chronic hyperglycemic injury to small vessels and nerves, so they commonly travel together in long-standing diabetes.
- `connects-to` → **[Generalized Anxiety Disorder](../generalized-anxiety-disorder/README.md)** — Anxiety turns up the pain volume: chronic worry heightens attention to pain and lowers its threshold, and persistent neuropathic pain in turn fuels anxiety — a two-way amplification rooted in shared limbic circuitry.
- `connects-to` → **[Alcohol Use Disorder](../alcohol-use-disorder/README.md)** — Heavy drinking poisons the peripheral nerves: chronic alcohol use, with its associated thiamine and B-vitamin deficiency, causes a length-dependent axonal neuropathy that produces burning neuropathic pain in the feet.
- `connects-to` → **[Multiple Myeloma](../multiple-myeloma/README.md)** — Its plasma-cell disease and treatment both hit nerves: amyloid deposition and tumor can injure nerves in multiple myeloma, and the bortezomib used to treat it causes a painful, dose-limiting peripheral neuropathy.
- `connects-to` → **[Colorectal Cancer](../colorectal-cancer/README.md)** — Its chemotherapy leaves nerves raw: the oxaliplatin in colorectal-cancer regimens causes a cold-triggered and chronic peripheral neuropathy, a leading example of chemotherapy-induced neuropathic pain.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — It is a disease of the nervous system itself: neuropathic pain arises from damage or dysfunction anywhere along the somatosensory pathway, from peripheral nerves to the spinal cord and brain, with central sensitisation amplifying it.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — Spine disease pinches the nerves: a herniated disc or degenerative stenosis compressing a nerve root causes radiculopathy and sciatica, a very common musculoskeletal source of neuropathic pain.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — Its mainstay drugs constipate the gut: the opioids, tricyclics and gabapentinoids used to treat neuropathic pain all slow intestinal transit, making constipation a common, limiting side effect.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — It is read and treated through the skin: small-fibre neuropathy is diagnosed by skin biopsy, postherpetic neuralgia and CRPS bring skin allodynia and trophic changes, and topical capsaicin and lidocaine patches relieve it.
- `connects-to` → **[Immune System](../immune-system/README.md)** — The immune system can attack nerves: immune-mediated neuropathies such as Guillain-Barré, CIDP and vasculitic neuropathy damage peripheral nerves and are important, treatable causes of neuropathic pain.
- `connects-to` → **[Cardiovascular System](../cardiovascular-system/README.md)** — Autonomic and vascular nerve injury intertwine: autonomic neuropathy causes orthostatic hypotension, while ischaemia from peripheral vascular disease itself injures nerves and produces painful neuropathy.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — Hormonal disease is its leading cause: diabetes is the commonest cause of peripheral neuropathy worldwide, and hypothyroidism and other endocrine disorders also damage nerves.
- `connects-to` → **[Respiratory System](../respiratory-system/README.md)** — Its drugs can suppress breathing: the gabapentinoids and opioids used to treat neuropathic pain cause respiratory depression, especially when combined or in older patients.
- `connects-to` → **[Renal System](../renal-system/README.md)** — The kidney both causes and constrains it: uraemia causes a peripheral neuropathy, and renal impairment mandates dose reduction of the renally-cleared gabapentin and pregabalin.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — It strikes the pelvis too: pudendal neuralgia and other pelvic neuropathic pain syndromes affect sexual and urinary function, a distressing and under-recognised form.
- `connects-to` → **[Fluoxetine](../../../03-medicine/01-modern/10-mental-health/fluoxetine/README.md)** — Antidepressants are core analgesics: SNRIs like duloxetine and tricyclics relieve neuropathic pain by boosting descending serotonin-noradrenaline inhibition, the pathway SSRIs like fluoxetine also touch.
- `connects-to` → **[CIDP](../cidp/README.md)** — A treatable demyelinating cause: chronic inflammatory demyelinating polyneuropathy causes neuropathic pain that, unlike most, responds to immunotherapy rather than analgesics alone.
- `connects-to` → **[Cancer Chemotherapy](../../../03-medicine/01-modern/13-cancer/cancer-chemotherapy/README.md)** — Chemo is a leading iatrogenic cause: platinum, taxane, vincristine and bortezomib chemotherapies produce chemotherapy-induced peripheral neuropathy, a dose-limiting, often lasting neuropathic pain in cancer survivors.
- `connects-to` → **[Axonal Transport](../../05-tissue/axonal-transport/README.md)** — Failing axons fire abnormally: many neuropathic pains arise from a dying-back axonopathy where disrupted axonal transport starves the distal nerve, generating ectopic impulses felt as burning, length-dependent pain.
- `connects-to` → **[Cannabis Use Disorder](../cannabis-use-disorder/README.md)** — Cannabinoids are sought for refractory pain: medical cannabis is widely used for neuropathic pain via the endocannabinoid system, with modest evidence and the attendant risk of cannabis use disorder.
- `connects-to` → **[Epilepsy](../epilepsy/README.md)** — Shared neuronal hyperexcitability: neuropathic pain and epilepsy both arise from over-excitable neurons with disordered sodium-channel and GABA signalling, which is why anticonvulsants like gabapentin, pregabalin and carbamazepine treat both.
- `connects-to` → **[ANCA Vasculitis](../anca-vasculitis/README.md)** — It inflames the nerves' blood supply: ANCA-associated vasculitis causes a vasculitic neuropathy (mononeuritis multiplex) by occluding the small vessels feeding peripheral nerves, a painful cause of neuropathic pain.
- `connects-to` → **[Hepatitis C](../hepatitis-c/README.md)** — Cryoglobulins attack the nerves: chronic hepatitis C generates cryoglobulin immune complexes that inflame the vasa nervorum, causing a painful sensorimotor neuropathy—an infectious driver of neuropathic pain.
- `connects-to` → **[Sickle Cell Disease](../sickle-cell-disease/README.md)** — Pain that turns neuropathic: recurrent vaso-occlusive crises in sickle cell disease drive central sensitisation and a peripheral neuropathy, so chronic sickle pain acquires a neuropathic character needing adjuvant agents.
- `connects-to` → **[Breast Cancer](../breast-cancer/README.md)** — Chemotherapy-induced neuropathy: the taxane and platinum regimens used for cancers like breast cancer commonly cause a dose-limiting, painful peripheral neuropathy (CIPN) that can persist long after treatment.
- `connects-to` → **[Hereditary Pancreatitis](../hereditary-pancreatitis/README.md)** — Neuropathic visceral pain: chronic and hereditary pancreatitis cause severe pain partly through neuropathic mechanisms—perineural inflammation and pancreatic nerve remodelling—not just ductal obstruction.
- `connects-to` → **[NMO](../nmo/README.md)** — Central neuropathic pain: neuromyelitis optica causes painful tonic spasms and severe central pain from its longitudinally extensive spinal-cord lesions, a disabling neuropathic-pain syndrome distinct from peripheral causes.
- `connects-to` → **[COVID-19 Disease](../covid-19-disease/README.md)** — Post-viral neuropathy: both acute COVID-19 and long COVID can cause a small-fibre neuropathy and new neuropathic pain, adding SARS-CoV-2 to the viral triggers of painful nerve injury alongside shingles and HIV.
- `connects-to` → **[Hippocampus](../../05-tissue/hippocampus/README.md)** — Pain's emotional brain: chronic neuropathic pain remodels the hippocampus and limbic circuits, driving the memory impairment, depression and catastrophising that accompany it as central sensitisation engages emotional centres.
- `connects-to` → **[NLRP3 Inflammasome](../../03-molecular/nlrp3-inflammasome/README.md)** — Glial inflammasome: NLRP3-inflammasome activation in microglia and macrophages around injured nerves sustains the neuroinflammation that drives neuropathic pain.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — Neuronal sensitisation: IL-1β released by activated glia sensitises nociceptive neurons, lowering their firing threshold to produce the hypersensitivity of neuropathic pain.
- `connects-to` → **[Neuropeptide Y](../../03-molecular/npy/README.md)** — Injured-neuron signal: neuropeptide Y is strongly upregulated in injured sensory neurons and modulates the abnormal signalling underlying neuropathic pain.
- `connects-to` → **[CCL2](../../03-molecular/ccl2/README.md)** — Microglial recruitment: nerve injury drives CCL2 release that recruits and activates spinal microglia and monocytes through CCR2, a key chemokine axis initiating the neuroinflammation behind neuropathic pain.
- `connects-to` → **[TLR4](../../03-molecular/tlr4/README.md)** — Danger-signal sensing: TLR4 on glia detects DAMPs released by injured nerves, triggering the microglial activation and cytokine release that establish central sensitisation in neuropathic pain.
- `connects-to` → **[Serotonin Transporter](../../03-molecular/serotonin-transporter/README.md)** — Descending modulation: serotonin-transporter activity sets serotonergic tone in descending pain pathways, the target of SNRIs like duloxetine that are first-line drugs for neuropathic pain.
- `connects-to` → **[NTRK / TrkA](../../03-molecular/ntrk/README.md)** — Nerve growth factor signaling through TrkA sensitizes and upregulates nociceptors after nerve injury, the peripheral mechanism that anti-NGF antibodies such as tanezumab target to relieve chronic neuropathic and osteoarthritic pain.
- `connects-to` → **[Nitric oxide](../../03-molecular/nitric-oxide/README.md)** — NMDA-receptor activation in the dorsal horn drives nNOS-derived nitric oxide that potentiates synaptic transmission, a positive-feedback loop reinforcing the central sensitization that makes neuropathic pain self-sustaining.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — CXCL12 acting on CXCR4 in the dorsal-root ganglia and spinal cord directly excites and sensitizes nociceptive neurons, a neuro-glial chemokine signal that sustains chronic neuropathic pain long after the initial nerve injury.
- `connects-to` → **[Oxytocin](../../03-molecular/oxytocin/README.md)** — Oxytocinergic projections from the hypothalamic paraventricular nucleus to the spinal dorsal horn inhibit nociceptive transmission, an endogenous analgesic pathway being explored therapeutically for neuropathic pain.
- `connects-to` → **[RAGE](../../03-molecular/rage/README.md)** — Advanced glycation end-products signaling through RAGE injure peripheral nerves and sensitize nociceptors, a central mechanism of the painful diabetic neuropathy that is among the commonest causes of neuropathic pain.
- `connects-to` → **[Perforin](../../03-molecular/perforin/README.md)** — Infiltrating CD8 T cells releasing perforin and granzyme contribute to the maintenance of neuropathic pain after nerve injury, a T-cell arm of neuroimmune sensitization distinct from the better-known microglial component.
- `connects-to` → **[Interleukin-10](../../03-molecular/il-10/README.md)** — Anti-inflammatory IL-10 suppresses the glial pro-inflammatory cytokines (IL-1β, IL-6 and TNF-α already mapped) that sustain neuropathic pain, the rationale for IL-10-based pain-resolution strategies.
- `connects-to` → **[Connexin-43](../../03-molecular/connexin43/README.md)** — Astrocytic connexin-43 gap junctions and hemichannels propagate central sensitization across the spinal dorsal horn, releasing ATP and glutamate (already mapped) that amplify and spread neuropathic pain.
- `connects-to` → **[Transforming Growth Factor Beta](../../03-molecular/tgf-beta/README.md)** — TGF-β exerts a neuroprotective, analgesic influence that restrains microglial activation in neuropathic pain, and its loss permits the neuroinflammation that maintains the chronic pain state.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — BDNF-TrkB (BDNF and NTRK mapped) and inflammatory signaling activate MAPK-ERK in dorsal-horn neurons and microglia, driving the central sensitization that amplifies neuropathic pain.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — Spinal mTOR-driven protein synthesis sustains the long-term central sensitization that maintains the chronic neuropathic pain state.
- `connects-to` → **[MYD88](../../03-molecular/myd88/README.md)** — TLR4 (mapped) signaling through MyD88 activates spinal microglia after nerve injury, a key neuroinflammatory amplifier of neuropathic pain.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — PI3K-AKT signaling downstream of neurotrophin (NTRK/BDNF mapped) and cytokine receptors drives the central and peripheral sensitization underlying neuropathic pain.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — Glial JAK-STAT signaling transduces the IL-6/cytokine milieu (IL-6 mapped) into the reactive astro-microgliosis that sustains neuropathic pain.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — IL-17A from infiltrating T cells sensitizes nociceptors and amplifies spinal glial activation, contributing to chronic neuropathic pain.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Galectin-3 released by activated spinal microglia amplifies the neuroinflammation and central sensitization that sustain chronic neuropathic pain.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — JAK-STAT3 signaling (JAK1/2 already mapped) in spinal glia drives the reactive gliosis that maintains chronic neuropathic pain.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β signaling in dorsal-horn neurons contributes to the synaptic plasticity underlying the central sensitization of neuropathic pain.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — Cytosolic DNA sensing through cGAS-STING in spinal microglia and macrophages contributes to the neuroinflammation that sustains neuropathic pain.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — IFN-STAT1 signaling in spinal microglia drives the neuroinflammatory sensitization that maintains neuropathic pain.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — FOXO regulates neuronal oxidative-stress and survival pathways relevant to the maladaptive plasticity of neuropathic pain.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — PI3K (PIK3CA)-AKT signaling (AKT already mapped) in dorsal-horn neurons and glia contributes to the central sensitization of neuropathic pain.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — S100A8/A9 alarmins released after nerve injury amplify the neuroinflammation underlying neuropathic pain.
- `connects-to` → **[HIF-1alpha](../../03-molecular/hif-1alpha/README.md)** — HIF-1α in injured nerve and dorsal-root ganglia contributes to the metabolic and inflammatory adaptation driving neuropathic pain.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK-linked metabolic signaling modulates the neuronal and glial responses underlying the central sensitization of neuropathic pain.
- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — SRC-family kinase signaling, via microglial P2X4 and NMDA-receptor phosphorylation, participates in the central sensitization of neuropathic pain.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — DNMT3A-mediated DNA methylation contributes to the epigenetic reprogramming of the dorsal-root-ganglion neurons in neuropathic pain.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — Autophagy modulates the neuronal and glial homeostasis and the Wallerian degeneration implicated in neuropathic pain.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-driven microglial and macrophage recruitment participates in the neuroinflammation driving neuropathic pain.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Complement C3 signaling participates in the microglial synaptic remodeling and neuroinflammation of neuropathic pain.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — IL-33 alarmin signaling participates in the glial and neuroinflammatory responses of neuropathic pain.
- `connects-to` → **[ARID1A](../../03-molecular/arid1a/README.md)** — ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic regulation of the pain-sensitization gene programs of neuropathic pain.
- `connects-to` → **[Calcineurin](../../03-molecular/calcineurin/README.md)** — Calcineurin-NFAT signaling participates in the neuroimmune and glial activation of neuropathic pain.
- `connects-to` → **[Insulin](../../03-molecular/insulin/README.md)** — Diabetic neuropathy: the most common cause of neuropathic pain is diabetic peripheral neuropathy, where hyperglycaemia and impaired insulin signalling injure sensory axons through metabolic and microvascular mechanisms (RAGE already mapped).
- `connects-to` → **[Estrogen](../../03-molecular/estrogen/README.md)** — Sex differences: chronic and neuropathic pain are more prevalent and often more severe in women, and estrogen modulates nociceptive processing and glial activity, contributing to the sex differences in pain sensitivity and treatment response.
- `connects-to` → **[Glucocorticoid receptor](../../03-molecular/glucocorticoid-receptor/README.md)** — Anti-inflammatory therapy: corticosteroids acting through the glucocorticoid receptor are used, including as epidural injections, to relieve the inflammatory and compressive components of radicular neuropathic pain by dampening neuroinflammation.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — Reparative immunity: IL-4 polarises macrophages toward a reparative M2 phenotype and, with IL-10 (already mapped), dampens the neuroinflammation after nerve injury, so the type-2 immune arm helps resolve neuropathic pain.
- `connects-to` → **[Xanthine oxidase](../../03-molecular/xanthine-oxidase/README.md)** — Oxidative sensitisation: reactive oxygen species from xanthine oxidase and other sources accumulate after nerve injury and sensitise nociceptive pathways, an oxidative mechanism contributing to the persistence of neuropathic pain.
- `connects-to` → **[Histamine](../../03-molecular/histamine/README.md)** — Histaminergic modulation: histamine acting on H1 and H3 receptors modulates both itch and pain signalling in sensory pathways, one of the neuromodulator systems (substance P already mapped) that shape the neuropathic pain and itch of nerve injury.
- `connects-to` → **[Bradykinin](../../03-molecular/bradykinin/README.md)** — Nociceptor sensitisation: bradykinin acting on B1 and B2 receptors, induced after nerve injury and inflammation, sensitises nociceptors and lowers their firing threshold (prostaglandins and substance P already mapped), amplifying neuropathic pain.
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — Type-2 neuroimmune resolution: IL-13, with IL-4 (already mapped), polarises macrophages toward a reparative phenotype at the injured nerve, part of the neuroimmune balance that influences whether pain resolves or becomes chronic.
- `connects-to` → **[Melatonin](../../03-molecular/melatonin/README.md)** — Analgesia and sleep: melatonin has analgesic and anti-inflammatory effects and restores the sleep disrupted by chronic pain (serotonin already mapped), and the pain-sleep loop it addresses is central to the burden of neuropathic pain.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Calcium channels and the α2δ target: voltage-gated calcium channels drive the neurotransmitter release (glutamate already mapped) of pain signalling, and their α2δ subunit is the target of gabapentin and pregabalin used for neuropathic pain.
- `connects-to` → **[Astrocyte](../../04-cellular/astrocyte/README.md)** — Astrocytic sensitisation: reactive astrocytes, with the microglia (already mapped), sustain central sensitisation in the dorsal horn through gap junctions (connexin43 already mapped) and gliotransmitters, maintaining chronic neuropathic pain.
- `connects-to` → **[Brain](../../06-organ/brain/README.md)** — Central pain and affect: the brain reorganises in chronic neuropathic pain, with thalamocortical changes and the affective and cognitive dimensions (serotonin and noradrenaline already mapped) that the SNRIs and psychological therapies address.
- `connects-to` → **[Zinc](../../02-atomic/zinc/README.md)** — Zinc and NMDA modulation: zinc modulates the NMDA receptor of the glutamate (already mapped) signalling of central sensitisation, and disturbed zinc handling affects the pain processing of neuropathic pain.
- `connects-to` → **[Potassium](../../02-atomic/potassium/README.md)** — Potassium-channel excitability: the downregulation of the voltage-gated potassium (Kv) channels after nerve injury raises the neuronal (already mapped) excitability and drives the ectopic firing of neuropathic pain.
- `connects-to` → **[Stroke](../stroke/README.md)** — Central post-stroke pain: the thalamic and other central lesions of stroke cause central post-stroke pain, a classic central neuropathic pain arising from the reorganised brain (already mapped).
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Metabolic-pain adipokine: leptin modulates the pain via the leptin-driven microglial (already mapped) activation, linking the metabolic state to the central sensitization of neuropathic pain.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — Metabolic adipokine: adiponectin, with leptin (already mapped), modulates the neuroinflammation (TNF and IL-6 already mapped) and the pain of neuropathic pain.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), is the pro-inflammatory adipokine linking the metabolic state to the neuroinflammation of neuropathic pain.
- `connects-to` → **[Type I interferon](../../03-molecular/type-i-interferon/README.md)** — Innate neuroinflammation: the type-I interferon, downstream of the cGAS-STING (already mapped) pathway, contributes to the glial (microglia already mapped) neuroinflammation that sustains neuropathic pain.
- `connects-to` → **[IFN-gamma](../../03-molecular/ifn-gamma/README.md)** — Th1 neuroinflammation: the IFN-γ of the infiltrating T cells is the type-II interferon arm of the immune contribution (TNF and IL-1 already mapped) to the central sensitisation of neuropathic pain.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the immune-inflammatory dimension of neuropathic pain.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the neuroimmune interaction in neuropathic pain.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the neuroimmune contribution to the central sensitisation of neuropathic pain.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the neuroimmune interaction in neuropathic pain.
- `connects-to` → **[T-helper cell](../../04-cellular/t-helper-cell/README.md)** — CD4 neuroimmune arm: the CD4 T-helper cells infiltrate the injured nerve and dorsal-root ganglion and, via the Th1/Th2/Th17 (IFN-γ, IL-4 and IL-17 already mapped) cytokines, modulate the neuropathic pain.
- `connects-to` → **[Natural killer cell](../../04-cellular/natural-killer-cell/README.md)** — NK nerve clearance: the NK cells (perforin already mapped) infiltrate the injured nerve and, by clearing the damaged sensory neurons (already mapped), modulate the resolution or persistence of neuropathic pain.
- `connects-to` → **[C5aR1](../../03-molecular/c5ar1/README.md)** — Complement C5a receptor: the C5aR1 signalling (with the complement C3 already mapped), activated after nerve injury, drives the myeloid recruitment and the neuroinflammation that sensitises the nociceptors of neuropathic pain.
- `connects-to` → **[Complement C5](../../03-molecular/complement-c5/README.md)** — Terminal complement: the complement C5 and its C5a (with C3 and C5aR1 already mapped) are generated after nerve injury and drive the membrane-attack and the neuroinflammation that sensitises the nociceptors of neuropathic pain.
- `connects-to` → **[Factor H](../../03-molecular/factor-h/README.md)** — Complement regulation: factor H regulates the alternative complement pathway (complement C3, C5 and C5aR1 already mapped) of the post-nerve-injury complement activation of neuropathic pain.
- `connects-to` → **[Dendritic cell](../../04-cellular/dendritic-cell/README.md)** — Nerve antigen presentation: the dendritic cells of the injured nerve and CNS-border compartments present antigen to the T cells (already mapped) in the neuroinflammation of neuropathic pain.
- `connects-to` → **[TSLP](../../03-molecular/tslp/README.md)** — Neuro-epithelial alarmin: TSLP, released from keratinocytes (skin already mapped) and glial cells under neuropathic insult, activates mast cells (already mapped) and dendritic cells (already mapped), amplifying the peripheral sensitisation of neuropathic pain.
- `connects-to` → **[C1-Esterase Inhibitor](../../03-molecular/c1-esterase-inhibitor/README.md)** — Complement/kinin gate: C1-esterase inhibitor limits classical complement (C3, C5 and C5aR1 already mapped) and contact-kinin activation in the injured nerve microenvironment, restraining complement-driven neuroinflammation of neuropathic pain.
- `connects-to` → **[Erythropoietin](../../03-molecular/erythropoietin/README.md)** — Neuroprotective cytokine: erythropoietin, acting via EPOR on neurons and Schwann cells (peripheral nerve already mapped), promotes axonal survival and remyelination and attenuates the neuro-inflammatory sensitisation of neuropathic pain.
- `connects-to` → **[Periostin](../../03-molecular/periostin/README.md)** — ECM-repair scaffold: periostin, expressed in injured peripheral nerve endoneurium and DRG supporting cells, promotes the re-organisation of the extracellular matrix and glial scar and modulates the fibrotic neuroinflammatory microenvironment of neuropathic pain.
- `connects-to` → **[Prolactin](../../03-molecular/prolactin/README.md)** — Immune-endocrine pain modulator: prolactin, acting via PRLR on DRG neurons and immune cells in the nerve injury site, sensitises peripheral nociceptors and amplifies the pro-inflammatory cytokine (IL-6 and TNF-α already mapped) signalling of neuropathic pain.
- `connects-to` → **[Testosterone](../../03-molecular/testosterone/README.md)** — Androgen neuroprotection: testosterone, acting via androgen receptors on DRG neurons and Schwann cells (peripheral nerve already mapped), promotes axonal repair and attenuates the neuro-inflammatory sensitisation underlying the sex-differential severity of neuropathic pain.
- `connects-to` → **[Vasopressin](../../03-molecular/vasopressin/README.md)** — NP vasopressin: vasopressin V1A receptors in dorsal horn neurons modulate spinal nociception; vasopressin interacts with oxytocin (already mapped) antinociceptive circuits and attenuates the serotonin (already mapped) descending pain-inhibitory dysfunction of neuropathic pain.
- `connects-to` → **[Transferrin](../../03-molecular/transferrin/README.md)** — NP transferrin: transferrin-mediated iron transport is essential for myelin synthesis and axonal function (peripheral nerve already mapped); iron dyshomeostasis amplifies the oxidative stress driving the neuroinflammatory sensitisation and axonal damage of neuropathic pain.
- `connects-to` → **[Copper](../../02-atomic/copper/README.md)** — NP copper: copper deficiency impairs the myelination of peripheral nerves (already mapped) and reduces superoxide dismutase-mediated antioxidant protection; copper dyshomeostasis amplifies the neuroinflammatory sensitisation and oxidative injury of neuropathic pain.

[^jensen-2011-neuropathic-pain-review]: Jensen TS, Baron R, Haanpää M, et al. A new definition of neuropathic pain. *Pain.* 2011;152(10):2204-2205. [doi:10.1016/j.pain.2011.06.017](https://doi.org/10.1016/j.pain.2011.06.017) · [PubMed 21764514](https://pubmed.ncbi.nlm.nih.gov/21764514/)
[^dworkin-2010-neuropathic-pain-treatment]: Dworkin RH, O'Connor AB, Audette J, et al. Recommendations for the pharmacological management of neuropathic pain. *Mayo Clin Proc.* 2010;85(3 Suppl):S3-14. [doi:10.4065/mcp.2009.0649](https://doi.org/10.4065/mcp.2009.0649) · [PubMed 20194146](https://pubmed.ncbi.nlm.nih.gov/20194146/)
[^scholz-2002-neuropathic-pain-mechanisms]: Scholz J, Woolf CJ. Can we conquer pain? *Nat Neurosci.* 2002;5(Suppl):1062-1067. [doi:10.1038/nn942](https://doi.org/10.1038/nn942) · [PubMed 12403987](https://pubmed.ncbi.nlm.nih.gov/12403987/)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
