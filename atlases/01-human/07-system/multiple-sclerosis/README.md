---
schema: human-scale-entry/v1
id: multiple-sclerosis
name: Multiple Sclerosis
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-06
summary: "Autoimmune demyelinating CNS disease mediated by autoreactive Th1/Th17 and CD8+ T cells attacking myelin; relapsing-remitting in 85% at onset. Natalizumab, ocrelizumab, and cladribine are high-efficacy DMTs; early aggressive therapy improves long-term disability outcomes."
aliases: ["MS", "multiple sclerosis", "RRMS", "PPMS", "clinically isolated syndrome", "CIS"]
sources:
  - id: compston-2008-ms-review
    type: peer-reviewed
    cite: "Compston A, Coles A. Multiple sclerosis. Lancet. 2008;372(9648):1502-1517."
    doi: "10.1016/S0140-6736(08)61620-7"
    pmid: "18970977"
    url: "https://doi.org/10.1016/S0140-6736(08)61620-7"
  - id: kappos-2006-natalizumab
    type: peer-reviewed
    cite: "Polman CH, O'Connor PW, Havrdova E, et al. A randomized, placebo-controlled trial of natalizumab for relapsing multiple sclerosis. N Engl J Med. 2006;354(9):899-910."
    doi: "10.1056/NEJMoa044397"
    pmid: "16510744"
    url: "https://doi.org/10.1056/NEJMoa044397"
  - id: montalban-2017-ocrelizumab-ppms
    type: peer-reviewed
    cite: "Montalban X, Hauser SL, Kappos L, et al. Ocrelizumab versus Placebo in Primary Progressive Multiple Sclerosis. N Engl J Med. 2017;376(3):209-220."
    doi: "10.1056/NEJMoa1606468"
    pmid: "28002688"
    url: "https://doi.org/10.1056/NEJMoa1606468"
cross_links:
  - target: 01-human/06-organ/brain
    relation: targets
    note: "MS lesions develop in periventricular white matter and cortical grey matter; demyelination disrupts saltatory conduction; chronic inflammation causes axonal transection and atrophy; brain volume loss on MRI correlates with long-term disability."
  - target: 01-human/04-cellular/oligodendrocyte
    relation: connects-to
    note: "Oligodendrocytes are the primary MS target; autoreactive T cells and complement attack myelin sheaths → demyelination and OPC exhaustion; remyelination is incomplete in progressive MS due to OPC failure and inhibitory myelin debris accumulation."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "Th1 (IFN-gamma) and Th17 (IL-17) cells are the primary MS pathogenic T cells; Th17 breach the BBB via CCR6/CCL20; both subsets attack myelin directly and activate resident microglia; natalizumab blocks VLA-4→VCAM-1, preventing T cell CNS trafficking."
  - target: 01-human/04-cellular/astrocyte
    relation: connects-to
    note: "Astrocytes form glial scar in MS lesions (GFAP+), impeding OPC remyelination; but astrocytes also sustain BBB integrity and produce CNTF/LIF supporting oligodendrocyte survival; astrocyte dysfunction drives progressive MS and lesion repair failure."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "IL-17A is elevated in MS lesions and CSF; Th17 cells breach the blood-brain barrier via CXCR6 → demyelination; secukinumab (anti-IL-17A) paradoxically worsened MS relapse rates in phase 2 trials — suggesting complex compensatory roles of IL-17A/Treg balance in CNS disease."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5+ Th1 cells are recruited to CNS white matter lesions in MS; CCR5-Δ32 carriers have modestly reduced MS severity in some cohorts; CCR5 ligands (CCL3/CCL4/CCL5) are elevated in MS CSF; CCR5 antagonism (maraviroc) is being explored in neuroinflammation trials."
  - target: 02-pathogen/01-viruses/epstein-barr-virus
    relation: connects-to
    note: "Epstein-Barr virus is now considered a necessary cause of multiple sclerosis: a 10-million-person cohort showed MS risk jumps ~32-fold after EBV seroconversion, and EBV's EBNA-1 protein cross-reacts with the myelin protein GlialCAM — making EBV a leading target for MS prevention."
  - target: 01-human/07-system/myasthenia-gravis
    relation: connects-to
    note: "Multiple sclerosis and myasthenia gravis are both autoimmune neurological diseases: MS is a T-cell-driven demyelination of central myelin, whereas MG is an antibody attack on the neuromuscular junction — CNS versus peripheral, T-cell versus B-cell/complement."
  - target: 03-medicine/03-food/vitamin-d
    relation: connects-to
    note: "Low vitamin D is a consistent, modifiable multiple-sclerosis risk factor: the latitude gradient of MS tracks sunlight, a vitamin-D-response element sits in the HLA-DRB1*15:01 promoter, and supplementation is being studied for prevention."
  - target: 01-human/07-system/nmo
    relation: connects-to
    note: "MS and NMOSD were long conflated until AQP4-IgG distinguished them: MS is T-cell/myelin-directed with small CNS plaques and a relapsing course, while NMOSD is AQP4-IgG astrocyte attack with severe optic neuritis and extensive myelitis—and MS drugs like interferon-β worsen NMOSD."
  - target: 01-human/04-cellular/b-cell
    relation: connects-to
    note: "B cells are now central to multiple sclerosis: beyond antibody they present antigen and form meningeal follicles driving cortical damage, and anti-CD20 therapies (ocrelizumab, ofatumumab) that deplete B cells are among the most effective treatments for MS."
  - target: 01-human/06-organ/eye
    relation: connects-to
    note: "The eye is a frequent first window into multiple sclerosis: optic neuritis—painful monocular vision loss—is a common presenting attack, and internuclear ophthalmoplegia from a brainstem plaque is highly suggestive; OCT retinal thinning now tracks neurodegeneration in MS."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "Depression is the commonest psychiatric comorbidity of multiple sclerosis: it stems both from demyelinating lesions in mood circuits and from the burden of chronic disability—often underrecognized, it degrades quality of life and warrants active screening."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Type I interferon was the first disease-modifying therapy for multiple sclerosis: interferon-β shifts immunity away from the pro-inflammatory Th17/Th1 pattern driving demyelination, reducing relapses—paradoxically, since the same cytokine family drives autoimmunity."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "Multiple sclerosis is increasingly a neurodegenerative as well as demyelinating disease: beyond myelin loss, axonal and neuronal injury accumulates and underlies progressive disability, so neuroprotection—not just anti-inflammatory therapy—is a key unmet goal."
  - target: 01-human/04-cellular/microglia
    relation: connects-to
    note: "Microglia are central to MS lesions: they strip myelin and present antigen to drive demyelination, but also clear debris to permit remyelination—the same brain-resident macrophages both damage and repair, making microglial phenotype a target in progressive MS."
  - target: 01-human/07-system/rheumatoid-arthritis
    relation: connects-to
    note: "Multiple sclerosis and rheumatoid arthritis are both autoimmune diseases driven by Th17 and autoreactive lymphocytes, but target different tissues—CNS myelin vs synovial joints—yet share genetic risk and respond to overlapping immunomodulators."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Cytotoxic T cells contribute to MS damage: though CD4 Th cells initiate the attack, CD8 cytotoxic T cells dominate MS lesions and directly kill oligodendrocytes and neurons, helping explain the axonal loss that drives irreversible progressive disability."
  - target: 01-human/03-molecular/cd20
    relation: connects-to
    note: "CD20-targeted therapy transformed MS treatment: depleting CD20+ B cells with ocrelizumab or rituximab sharply cuts relapses, proving B cells—not just T cells—drive the disease, and giving the first effective drug for progressive MS."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "Multiple sclerosis is the prototypical demyelinating disease of the central nervous system: immune attack strips myelin from brain, spinal cord and optic nerve in scattered plaques, so its protean symptoms reflect lesions dispersed in space and time."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "MS is fundamentally an autoimmune disease: self-reactive lymphocytes breach the blood-brain barrier to attack myelin, so it overlaps with other autoimmunity and is treated by immunomodulation—shifting MS care from symptom control to immune-directed therapy."
  - target: 01-human/07-system/gut-microbiome
    relation: connects-to
    note: "The gut microbiome shapes multiple sclerosis risk and activity: altered gut flora can tip the balance between inflammatory and regulatory T cells that attack myelin, so diet and the microbiome are emerging factors in an autoimmune disease of the brain."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: connects-to
    note: "MS reflects failed immune tolerance: regulatory T cells that should restrain autoreactive cells are deficient or dysfunctional, letting myelin-attacking T and B cells run unchecked—so restoring regulatory balance is a goal of MS therapy."
  - target: 01-human/04-cellular/plasma-cell
    relation: connects-to
    note: "Plasma cells leave MS's diagnostic signature: B cells mature into plasma cells inside the CNS and secrete antibodies detected as oligoclonal bands in spinal fluid, a hallmark that supports diagnosis and reflects the intrathecal immune response."
  - target: 01-human/03-molecular/mhc-class-ii
    relation: connects-to
    note: "MS's strongest genetic risk is an MHC class II allele: HLA-DRB1*15:01 shapes how myelin peptides are presented to T cells, the genetic basis tying the immune system's antigen presentation to attacks on the central nervous system."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Macrophages strip myelin in active MS lesions: drawn into the CNS, they (with microglia) phagocytose myelin and damage oligodendrocytes, so myelin-laden macrophages are the histologic signature of an active demyelinating plaque."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Iron rims mark MS's smoldering lesions: iron-laden microglia ring chronic active plaques, visible as paramagnetic rim lesions on MRI that flag ongoing, treatment-resistant inflammation driving progression."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "Sodium channels betray the demyelinated MS axon: stripped of myelin, the axon scatters sodium channels to keep firing, but this leaky, energy-hungry state lets sodium and calcium flood in, driving the axonal degeneration behind permanent disability."
  - target: 01-human/03-molecular/nitric-oxide
    relation: connects-to
    note: "Nitric oxide is a hidden axon-killer in MS: activated microglia and macrophages pour out NO that blocks nerve conduction and poisons mitochondria in demyelinated axons, contributing to both the symptoms and the slow neurodegeneration."
  - target: 01-human/03-molecular/glutamate
    relation: connects-to
    note: "Glutamate excitotoxicity widens MS damage: inflamed lesions spill excess glutamate that overexcites and kills oligodendrocytes and neurons, so beyond immune attack, this neurotransmitter helps turn inflammation into lasting tissue loss."
  - target: 01-human/05-tissue/synapse
    relation: connects-to
    note: "MS damage reaches the synapse: beyond stripping myelin, the disease erodes gray-matter synapses, and this synaptic loss tracks the cognitive decline and disability that demyelination alone does not explain."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Calcium executes the axon loss in MS: demyelinated axons overload with sodium, which reverses the sodium-calcium exchanger and floods them with calcium, the influx that degrades the axon and drives permanent disability."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "Mast cells help open the brain to MS attack: in lesions they release mediators that breach the blood-brain barrier and amplify demyelination, linking an allergic-type immune cell to the autoimmune assault on myelin."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "MS is diagnosed and tracked by MRI: its photons reveal the white-matter plaques scattered in space and time, and gadolinium enhancement flags the active, inflamed lesions."
  - target: 01-human/02-atomic/potassium
    relation: connects-to
    note: "MS exposes axonal potassium channels: demyelination uncovers them and leaks current, so the drug dalfampridine blocks potassium channels to restore conduction and improve walking."
  - target: 01-human/05-tissue/bone-marrow
    relation: connects-to
    note: "Aggressive MS can be reset from the bone marrow: autologous hematopoietic stem-cell transplant wipes out and rebuilds the immune system, halting relapses in selected severe cases."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy shows MS stripping the nerves bare: in the plaque, immune cells peel the myelin sheath off axons, leaving naked fibers that conduct poorly — and patchy, often incomplete, remyelination by surviving oligodendrocytes."
  - target: 01-human/06-organ/large-intestine
    relation: connects-to
    note: "MS disconnects the bowel: lesions in the spinal cord disrupt the nerves controlling defecation, so neurogenic constipation and incontinence are common, disabling, and often under-discussed symptoms."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "MS endangers the kidney through the bladder: cord lesions cause a neurogenic bladder that retains urine, breeding recurrent infections and back-pressure that, untreated, can damage the kidneys over time."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "Antibodies both reveal and treat MS: oligoclonal IgG bands in the spinal fluid support the diagnosis, and B-cell-depleting monoclonal antibodies (ocrelizumab, rituximab) are among its most effective disease-modifying therapies."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "MS bends to reproductive hormones: it strikes women far more often, relapses quiet during pregnancy then rebound after delivery, and family planning shapes the choice and timing of disease-modifying drugs."
  - target: 01-human/04-cellular/smooth-muscle-cell
    relation: connects-to
    note: "Demyelination disconnects the body's smooth muscle: cord lesions disrupt the autonomic control of the bowel into constipation and of the bladder's detrusor, the dysmotility behind much of the disability between relapses."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "MS plays out in the muscles it can no longer command: demyelinated motor pathways cause spasticity, weakness, and a faltering gait, and the disuse and immobility that follow waste muscle and stiffen joints."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "The disease-modifying drugs reshape the blood counts: agents like cladribine and fingolimod cause lymphopenia and can drop neutrophils, so counts are monitored and infection risk weighed against relapse control."
  - target: 01-human/06-organ/thyroid
    relation: connects-to
    note: "Treatment can turn the immunity on the thyroid: the MS drug alemtuzumab notoriously triggers autoimmune thyroid disease, often Graves', months to years later — one of several autoimmunities that follow immune reconstitution."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "Natural killer cells help police MS: their regulatory subsets restrain autoreactive T cells, and expanding them is how the antibody daclizumab worked — a reminder that innate lymphocytes, not just T and B cells, shape the disease."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Complement scars the progressive brain: C3 and the membrane-attack complex deposit in MS lesions, especially in the slow-burning cortical and progressive disease, marking a tissue-damage arm beyond the T-cell attack."
  - target: 01-human/05-tissue/peripheral-nerve
    relation: connects-to
    note: "MS spares the peripheral nerves, which sharpens the diagnosis: it demyelinates only the central oligodendrocyte myelin, so peripheral conduction stays normal — the line that separates it from CIDP and Guillain-Barré, though rare combined forms exist."
  - target: 01-human/03-molecular/nlrp3-inflammasome
    relation: connects-to
    note: "The inflammasome fuels the smouldering side of MS: NLRP3 in microglia and macrophages releases IL-1β and IL-18 that amplify Th17 demyelination and chronic active-lesion damage, making it a target for progressive disease."
  - target: 01-human/03-molecular/bdnf
    relation: connects-to
    note: "Repair in MS rides on BDNF: immune cells and neurons secrete this neurotrophin to support oligodendrocyte survival and remyelination, so boosting it is a neuroprotective strategy beyond suppressing the autoimmune attack."
  - target: 01-human/07-system/neuropathic-pain
    relation: connects-to
    note: "Pain in MS is largely neuropathic: demyelinating lesions in sensory pathways and the spinal cord generate central neuropathic pain, trigeminal neuralgia, and Lhermitte's sign — among the disease's most disabling non-motor symptoms."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "NF-κB sits at the genetic heart of MS: several MS risk variants converge on NF-κB signaling, the pathway through which activated T cells and microglia drive the inflammatory demyelination of the disease."
  - target: 01-human/07-system/sepsis
    relation: connects-to
    note: "A neurogenic bladder opens the way to deadly infection: urinary retention from spinal-cord lesions causes recurrent UTIs, and urosepsis — worsened by immunosuppressive disease-modifying therapy — is a leading cause of death in advanced MS."
  - target: 01-human/07-system/insomnia-disorder
    relation: connects-to
    note: "Sleep is broken on many fronts: pain, spasticity, nocturia and depression fragment sleep in MS, so insomnia is common and deepens the fatigue that is among the disease's most pervasive complaints."
  - target: 01-human/07-system/osteoporosis
    relation: connects-to
    note: "Immobility, steroids and low vitamin D thin the bone: reduced mobility, repeated corticosteroid courses for relapses and the vitamin D deficiency tied to MS itself accelerate bone loss and fracture risk."
  - target: 02-pathogen/03-fungi/pneumocystis-jirovecii
    relation: connects-to
    note: "Its potent therapies open the lung: the immunosuppressive disease-modifying drugs and steroids used in MS can drop T-cell defenses enough to risk Pneumocystis pneumonia, weighed during high-intensity treatment."
  - target: 01-human/07-system/epilepsy
    relation: connects-to
    note: "Cortical lesions can spark seizures: demyelinating plaques reaching the cerebral cortex make seizures and epilepsy several-fold more common in MS than in the general population."
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "A neurogenic bladder endangers the kidneys: spinal demyelination in MS impairs bladder control, and the recurrent urinary infections and back-pressure that follow can progress over years to chronic kidney disease."
  - target: 02-pathogen/03-fungi/aspergillus-fumigatus
    relation: connects-to
    note: "Its disease-modifying drugs blunt immunity: the immunosuppressive and B-cell-depleting therapies for MS, like ocrelizumab and fingolimod, can permit opportunistic infections including invasive aspergillosis."
  - target: 01-human/07-system/wound-healing
    relation: connects-to
    note: "Immobility and lost sensation break down the skin: as MS advances to wheelchair or bedbound disability with impaired sensation, pressure ulcers form and heal slowly over insensate, poorly perfused skin."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "Spinal demyelination wrecks bladder control: neurogenic bladder is one of the most common and disabling features of MS, causing urgency, incontinence and retention with recurrent UTIs and upper-tract damage."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "It disrupts the bowel too: MS commonly causes neurogenic bowel with constipation and faecal incontinence, and brainstem lesions can produce dysphagia with aspiration risk."
  - target: 02-pathogen/01-viruses/varicella-zoster-virus
    relation: connects-to
    note: "Its immunotherapies reawaken shingles: the B-cell-depleting and S1P-modulator disease-modifying therapies for MS, especially fingolimod, raise the risk of herpes-zoster reactivation."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "Advanced disease weakens breathing: brainstem and high cervical lesions impair respiratory muscles and swallowing, so aspiration and respiratory failure become a leading cause of death in late MS."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "Nerves and drugs unsettle the heart: autonomic dysfunction causes orthostatic hypotension and arrhythmia, and starting fingolimod causes first-dose bradycardia and heart block requiring monitoring."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "Immobility and injections mark the skin: pressure sores arise with reduced mobility, while injectable disease-modifying therapies cause injection-site reactions and lipoatrophy."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "Its strong therapies disturb hormones: alemtuzumab commonly triggers autoimmune thyroid disease, and the high-dose steroids used for relapses bring their own endocrine effects."
  - target: 01-human/07-system/lymphatic-system
    relation: connects-to
    note: "Modern treatment works through the lymphocytes: natalizumab blocks their entry to the brain, fingolimod traps them in lymph nodes and ocrelizumab depletes B cells, reshaping the immune traffic that drives MS."
  - target: 02-pathogen/01-viruses/herpesvirus
    relation: connects-to
    note: "Herpesviruses are implicated alongside EBV: human herpesvirus-6 has been studied as a co-factor in multiple sclerosis, and reactivation under immunosuppressive therapy is a clinical concern."
  - target: 03-medicine/01-modern/02-respiratory/corticosteroids
    relation: connects-to
    note: "Steroids cut short the relapse: high-dose corticosteroids speed recovery from acute MS relapses by damping CNS inflammation, though they do not change the long-term course of the disease."
  - target: 01-human/07-system/migraine
    relation: connects-to
    note: "Headache shadows demyelination: migraine is more common in multiple sclerosis than in the general population, the two sharing neuroinflammatory and vascular mechanisms."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "They present the myelin antigen: dendritic cells in lymph nodes and the inflamed CNS activate the autoreactive T cells that attack myelin, a key step in initiating and sustaining multiple sclerosis."
  - target: 03-medicine/01-modern/13-cancer/targeted-therapy
    relation: connects-to
    note: "Targeted DMTs reshaped its course: anti-CD20 antibodies (ocrelizumab), natalizumab against VLA-4, S1P modulators and BTK inhibitors suppress the relapses of multiple sclerosis far more effectively than older interferons."
  - target: 01-human/05-tissue/axonal-transport
    relation: connects-to
    note: "Axonal loss drives disability: beyond demyelination, MS transects and degenerates axons whose disrupted transport underlies the irreversible progressive disability that current immunotherapies only partly prevent."
  - target: 03-medicine/01-modern/13-cancer/cancer-chemotherapy
    relation: connects-to
    note: "Chemo and transplant for aggressive disease: cladribine and mitoxantrone deplete lymphocytes in MS, and autologous haematopoietic stem-cell transplant after intense conditioning can halt highly active relapsing disease."
  - target: 01-human/05-tissue/germinal-center
    relation: connects-to
    note: "EBV and B cells behind MS: Epstein-Barr infection is now a near-prerequisite, and ectopic B-cell follicles resembling germinal centres form in the meninges of progressive MS—the compartmentalised inflammation that anti-CD20 therapy targets."
  - target: 01-human/07-system/cidp
    relation: connects-to
    note: "Central versus peripheral demyelination: MS strips myelin in the CNS while CIDP strips it from peripheral nerves—autoimmune attacks on the same insulating sheath in two compartments."
  - target: 01-human/07-system/inflammatory-bowel-disease
    relation: connects-to
    note: "A shared autoimmune axis: MS and inflammatory bowel disease co-occur and share Th17/IL-17 biology and gut-microbiome influences, and some MS therapies can unmask or worsen colitis."
  - target: 01-human/07-system/covid-19-disease
    relation: connects-to
    note: "Immunotherapy meets infection: the B-cell-depleting MS therapies like ocrelizumab blunt the antibody response to COVID-19 vaccination and raise the risk of severe COVID-19, complicating treatment."
  - target: 01-human/07-system/bipolar-disorder
    relation: connects-to
    note: "Mood disorder in demyelinating disease: multiple sclerosis raises the risk of bipolar disorder and mania, from demyelinating lesions in mood circuits and from corticosteroid treatment of relapses."
  - target: 01-human/05-tissue/hippocampus
    relation: connects-to
    note: "Cognition in MS: demyelination and atrophy of the hippocampus contribute to the memory impairment and 'cog fog' that affect many MS patients, beyond the classic motor and sensory deficits."
  - target: 01-human/07-system/obsessive-compulsive-disorder
    relation: connects-to
    note: "Lesion-driven OCD: demyelinating plaques in frontal and basal-ganglia circuits can produce secondary obsessive-compulsive symptoms, one of the neuropsychiatric manifestations of multiple sclerosis."
  - target: 01-human/07-system/hepatitis-b
    relation: connects-to
    note: "Reactivation risk from anti-CD20: the B-cell-depleting therapies (ocrelizumab, rituximab) central to MS treatment can reactivate latent hepatitis B, mandating screening and antiviral prophylaxis."
  - target: 01-human/05-tissue/intestinal-epithelium
    relation: connects-to
    note: "The gut-brain axis in MS: the microbiome and intestinal-barrier integrity shape MS susceptibility and relapse activity through immune signalling, an emerging influence on the demyelinating disease."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Th1 demyelination: IFN-γ from autoreactive T-helper cells activates microglia and macrophages to attack myelin, a central cytokine of the inflammatory lesions of multiple sclerosis."
  - target: 01-human/03-molecular/tnf-alpha
    relation: connects-to
    note: "Inflammatory injury: TNF-α contributes to the oligodendrocyte damage and blood-brain-barrier breakdown of MS lesions, though paradoxically anti-TNF therapy worsens the disease."
  - target: 01-human/03-molecular/osteopontin
    relation: connects-to
    note: "Relapse biomarker: osteopontin is elevated in MS lesions and CSF, promoting the survival of autoreactive T cells and tracking with relapse and disease activity."
  - target: 01-human/03-molecular/baff
    relation: connects-to
    note: "B-cell survival: BAFF supports the autoreactive B cells and meningeal lymphoid follicles increasingly recognised in MS, part of the rationale behind the dramatic efficacy of anti-CD20 B-cell depletion."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "Th17 differentiation: IL-6 with TGF-beta drives the pathogenic Th17 cells that breach the blood-brain barrier and orchestrate the demyelinating attacks of multiple sclerosis."
  - target: 01-human/03-molecular/ccl2
    relation: connects-to
    note: "CNS trafficking: CCL2 helps recruit monocytes and autoreactive leukocytes across the blood-brain barrier into MS lesions, contributing to the inflammatory demyelination."
  - target: 01-human/03-molecular/btk
    relation: connects-to
    note: "B-cell and microglial signalling: BTK transduces B-cell-receptor and Fc-receptor signals in the B cells and microglia driving MS, the target of CNS-penetrant BTK inhibitors (tolebrutinib) developed for progressive disease."
  - target: 01-human/03-molecular/perforin
    relation: connects-to
    note: "Cytotoxic plaque injury: CD8 T cells, which actually outnumber CD4 cells in MS lesions, use perforin-mediated cytotoxicity to injure oligodendrocytes and axons, contributing to the irreversible damage of progression."
  - target: 01-human/03-molecular/il-2
    relation: connects-to
    note: "Treg and genetic risk: IL2RA (CD25) is an established MS susceptibility gene, and impaired IL-2-dependent regulatory-T-cell function lets autoreactive T cells escape control, a basis for low-dose IL-2 approaches."
  - target: 01-human/03-molecular/lmp1
    relation: connects-to
    note: "EBV trigger: Epstein-Barr virus is the leading environmental cause of MS, with EBV-infected B cells expressing latency proteins persisting in patients and EBV antigens cross-reacting with myelin (molecular mimicry), a basis for the efficacy of B-cell depletion."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Axonal degeneration: in the demyelinated axon, dysregulated sodium and calcium influx drives the calcium overload that destroys mitochondria and axons, the mechanism of the progressive neurodegeneration underlying irreversible MS disability."
  - target: 01-human/03-molecular/igf-1
    relation: connects-to
    note: "Remyelination support: IGF-1 promotes the survival and differentiation of oligodendrocyte precursors that remyelinate stripped axons, a trophic axis whose insufficiency contributes to the failed remyelination of chronic MS lesions."
  - target: 01-human/03-molecular/nfe2l2
    relation: connects-to
    note: "NRF2 therapy: dimethyl fumarate, a first-line MS therapy, activates the NRF2 antioxidant pathway to protect oligodendrocytes and neurons from the oxidative injury that drives demyelination and neurodegeneration."
  - target: 01-human/03-molecular/caspase-3
    relation: connects-to
    note: "Apoptotic demyelination: caspase-3-mediated apoptosis of oligodendrocytes and neurons contributes to the demyelination and the progressive axonal loss that underlies disability accumulation in multiple sclerosis."
  - target: 01-human/03-molecular/connexin43
    relation: connects-to
    note: "Panglial disruption: loss of astrocyte-oligodendrocyte connexin-43 gap junctions in MS plaques impairs the panglial network that supports myelin, contributing to lesion formation and expansion."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17 maintenance: IL-23 sustains the pathogenic Th17 cells (IL-17A already mapped) that cross the blood-brain barrier and drive the demyelinating inflammation of multiple sclerosis."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "Cytokine signal transduction: inflammatory-cytokine and type-I-interferon signalling through JAK-STAT (type-I IFN already mapped) governs the autoreactive T-cell responses of MS, the axis through which IFN-β therapy partly acts."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "Treg-Th17 balance: TGF-β drives regulatory T-cell differentiation that restrains CNS autoimmunity, and its balance against the IL-6/IL-23 milieu (both mapped) sets the Treg-Th17 equilibrium central to MS."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "STAT3 signalling downstream of IL-6 and IL-23 (both mapped) drives the pathogenic Th17 differentiation central to multiple sclerosis."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "PI3K-AKT signalling supports oligodendrocyte survival and remyelination, processes whose failure contributes to progressive multiple sclerosis."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Microglial galectin-3 promotes the demyelinating neuroinflammation of multiple sclerosis lesions."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "IFN-STAT1 signalling underlies both the antiviral interferon response and the mechanism of IFN-β disease-modifying therapy in multiple sclerosis."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "Cytosolic DNA sensing through cGAS-STING contributes to the innate neuroinflammation that drives demyelinating lesion formation in multiple sclerosis."
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "TGF-β-SMAD signalling (TGF-β already mapped) governs the regulatory-T-cell balance and remyelination responses relevant to multiple sclerosis."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "FOXO transcription factors regulate the T-cell tolerance and oligodendrocyte oxidative-stress responses relevant to the autoimmune demyelination of multiple sclerosis."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "ERK-MAPK signaling transduces the cytokine and T-cell-receptor stimuli driving the autoreactive T-cell activation of multiple sclerosis."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "S100A8/A9 alarmins amplify the myeloid-driven neuroinflammation of the demyelinating lesions of multiple sclerosis."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "GSK-3β modulates the Th17-driven autoimmune and neuroinflammatory signaling of multiple sclerosis."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "PI3K (PIK3CA)-AKT signaling (AKT already mapped) supports the survival and activation of the autoreactive T and B cells of multiple sclerosis."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "HIF-1α in the hypoxic demyelinated lesion contributes to the metabolic injury and immune-cell metabolism of multiple sclerosis."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK-linked immunometabolic signaling shapes the autoreactive T-cell metabolism of multiple sclerosis."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Autophagy modulates the survival of autoreactive lymphocytes and the antigen presentation of multiple sclerosis."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "DNMT3A-mediated DNA methylation contributes to the epigenetic dysregulation of the autoreactive immune response in multiple sclerosis."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "CXCL12-CXCR4 signaling participates in the leukocyte trafficking across the blood-brain barrier in multiple sclerosis."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "IL-33 alarmin signaling participates in the neuroinflammatory and demyelinating responses of multiple sclerosis."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC-family kinase signaling participates in the immune-cell and glial signaling of multiple sclerosis."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "IL-1β-driven inflammation participates in the neuroinflammation and demyelination of multiple sclerosis."
  - target: 01-human/03-molecular/arid1a
    relation: connects-to
    note: "ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic regulation of the immune responses of multiple sclerosis."
  - target: 01-human/03-molecular/calcineurin
    relation: connects-to
    note: "Calcineurin-NFAT signaling participates in the autoreactive T-cell activation of multiple sclerosis."
  - target: 01-human/03-molecular/estrogen
    relation: connects-to
    note: "Sex and pregnancy: multiple sclerosis is far more common in women, and relapses fall sharply in the third trimester when estrogen and progesterone are high, implicating sex hormones in disease modulation and inspiring estriol trials."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Obesity risk: adolescent obesity raises the risk of multiple sclerosis, and the proinflammatory adipokine leptin promotes the Th17 responses (IL-17A already mapped) that drive autoimmune demyelination."
  - target: 01-human/03-molecular/bcl-2
    relation: connects-to
    note: "Autoreactive survival: anti-apoptotic BCL-2 family proteins prolong the survival of the autoreactive lymphocytes that attack myelin, and shifting this balance toward apoptosis is one way immune-reconstitution therapies reset the disease."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "Th2 counter-response: IL-4 drives the protective type-2 T-cell response, and shifting the balance away from the pathogenic Th17 and Th1 arms (IL-17/IFN-gamma already mapped) toward IL-4-driven immunity is a long-sought therapeutic aim in multiple sclerosis."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "Regulatory suppression: IL-10 from regulatory B and T cells restrains the autoimmune attack on myelin, and deficient IL-10-mediated regulation contributes to the unchecked inflammation of multiple sclerosis."
  - target: 01-human/03-molecular/progesterone
    relation: connects-to
    note: "Pregnancy protection: relapses fall markedly in the third trimester of pregnancy, when progesterone and estrogen (already mapped) are high, implicating these neurosteroids in the immune modulation and remyelination potential in multiple sclerosis."
  - target: 01-human/03-molecular/xanthine-oxidase
    relation: connects-to
    note: "Oxidative axonal injury: reactive oxygen species, to which xanthine oxidase contributes, drive the mitochondrial and axonal injury (NRF2 already mapped) that underlies the progressive, demyelination-independent neurodegeneration of multiple sclerosis."
  - target: 01-human/03-molecular/cholesterol
    relation: connects-to
    note: "Myelin lipid and repair: cholesterol is a major component of myelin and is required for remyelination by oligodendrocytes (already mapped), so its metabolism shapes both the injury and the repair capacity in multiple sclerosis."
  - target: 01-human/03-molecular/prostaglandins
    relation: connects-to
    note: "Lesion eicosanoids: prostaglandins from the activated microglia (already mapped) and infiltrating cells contribute to the neuroinflammation (IL-6, TNF and IL-1 already mapped) of the active demyelinating lesion in multiple sclerosis."
  - target: 01-human/04-cellular/astrocyte
    relation: connects-to
    note: "Astrogliosis and the glial scar: the reactive astrocytes form the sclerotic glial scar that names multiple sclerosis, and their gap junctions (connexin43 already mapped) and gliotransmission shape both the lesion and the impaired repair."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Axonal calcium overload: the glutamate (already mapped) excitotoxicity and the energy failure of the demyelinated axon load it with calcium, driving the axonal degeneration that underlies the progressive disability of multiple sclerosis."
  - target: 03-medicine/03-food/omega-3-fatty-acids
    relation: connects-to
    note: "Omega-3 and myelin: the omega-3 fatty acids are structural lipids of myelin (cholesterol already mapped) and give rise to pro-resolving mediators, the basis of dietary interest in omega-3 for multiple sclerosis."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "Type-2 counter-arm: IL-13, with IL-4 (already mapped), is part of the Th2/anti-inflammatory arm (IL-10 already mapped) that counters the Th17 and Th1 (IL-17, IL-23 and IFN-γ already mapped) drive of multiple sclerosis."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Adipokine and MS risk: adiponectin, with leptin (already mapped), is part of the adipokine dimension of the obesity that is a risk factor for multiple sclerosis, the metabolic-immune crosstalk shaping the disease."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), links the adipose-inflammatory milieu (IL-6 already mapped) to the obesity-associated risk and activity of multiple sclerosis."
  - target: 01-human/04-cellular/microglia
    relation: connects-to
    note: "Smouldering plaque: the microglia and macrophages (CCL2 already mapped) strip the myelin and drive the smouldering (the chronic active plaques) neuroinflammation of multiple sclerosis."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "Axonal degeneration: the axonal and neuronal loss (glutamate excitotoxicity already mapped) underlies the progressive, irreversible disability of multiple sclerosis."
  - target: 03-medicine/03-food/vitamin-d
    relation: connects-to
    note: "Vitamin-D risk: the low vitamin D (the latitude gradient, the EBV/LMP1 already mapped interaction) is a modifiable multiple-sclerosis risk factor and a candidate modifier of the disease course."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm that, with the Th17 (IL-17 and IL-23 already mapped), drives the CNS autoimmunity of multiple sclerosis."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Type-2 counter-arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension balancing the Th1/Th17 drive of multiple sclerosis."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Type-2 IgE: the IgE (with IL-4 and IL-13 already mapped) reflects the type-2 immune dimension of the immune dysregulation of multiple sclerosis."
  - target: 01-human/03-molecular/histamine
    relation: connects-to
    note: "Mast-cell/remyelination axis: the histamine, from the mast cells (already mapped), modulates the blood-brain-barrier and the demyelination; the antihistamine clemastine is trialed to promote remyelination in multiple sclerosis."
  - target: 01-human/02-atomic/selenium
    relation: connects-to
    note: "Antioxidant micronutrient: selenium, a cofactor of the antioxidant selenoproteins, is part of the oxidative-stress and micronutrient dimension (with vitamin D already mapped) studied in multiple sclerosis."
  - target: 01-human/07-system/systemic-lupus-erythematosus
    relation: connects-to
    note: "Autoimmune comorbidity: multiple sclerosis shares the autoimmune susceptibility with systemic lupus erythematosus, and the two can co-occur or enter the differential of CNS demyelination."
  - target: 01-human/03-molecular/complement-c5
    relation: connects-to
    note: "Terminal complement: the complement C5 and its activation (with C3 already mapped) contribute to the demyelinating injury within the multiple-sclerosis lesion."
  - target: 01-human/03-molecular/c5ar1
    relation: connects-to
    note: "C5a receptor: the C5aR1 signalling links the complement to the microglial (already mapped) and myeloid activation of the active multiple-sclerosis lesion."
  - target: 01-human/03-molecular/factor-h
    relation: connects-to
    note: "Complement regulation: factor H regulates the alternative complement pathway (complement C3, C5 and C5aR1 already mapped), and its dysregulation is part of the complement contribution to the demyelination of multiple sclerosis."
  - target: 01-human/03-molecular/c1-esterase-inhibitor
    relation: connects-to
    note: "Classical-pathway regulation: the C1-esterase inhibitor regulates the classical complement pathway activated by the anti-myelin antibodies (immunoglobulin already mapped) that contribute to the demyelination of multiple sclerosis."
  - target: 01-human/03-molecular/transferrin
    relation: connects-to
    note: "Brain iron: transferrin, the iron carrier, reflects the disordered brain-iron handling that drives the oxidative injury and the oligodendrocyte ferroptosis of the demyelination of multiple sclerosis."
  - target: 01-human/03-molecular/periostin
    relation: connects-to
    note: "Lesion matricellular: periostin, a matricellular mediator, is part of the tissue remodelling and the astrocytic (already mapped) scarring of the chronic multiple-sclerosis lesion."
  - target: 01-human/03-molecular/tslp
    relation: connects-to
    note: "Alarmin-BBB axis: TSLP, from choroid-plexus and CNS-border epithelium disrupted in MS, primes dendritic cells (already mapped) toward Th17 (already mapped) priming and amplifies the BBB breach driving the lesion formation of multiple sclerosis."
  - target: 01-human/03-molecular/bradykinin
    relation: connects-to
    note: "Kinin-demyelination axis: bradykinin, via B2R on CNS neurons (already mapped) and oligodendrocytes (already mapped), amplifies the BBB permeability and the neuroinflammation contributing to the oligodendrocyte loss and the demyelination of multiple sclerosis."
  - target: 01-human/03-molecular/erythropoietin
    relation: connects-to
    note: "Neuroprotective EPO: erythropoietin, via EpoR on neurons (already mapped) and oligodendrocytes (already mapped), promotes remyelination and exerts anti-inflammatory neuroprotection relevant to the relapsing-remitting course of multiple sclerosis."
  - target: 01-human/03-molecular/melatonin
    relation: connects-to
    note: "Circadian-immune axis: melatonin has immunomodulatory and neuroprotective effects on T-cell (already mapped) and microglial (already mapped) activity; disrupted melatonin rhythm is associated with MS relapse rate and the circadian immune dysregulation of multiple sclerosis."
  - target: 01-human/03-molecular/testosterone
    relation: connects-to
    note: "Neuroprotective androgen: testosterone exerts neuroprotective and anti-inflammatory effects on oligodendrocytes (already mapped) and T cells (already mapped); low testosterone is associated with faster MS disability progression and the male sex-hormone dimension of MS."
  - target: 01-human/03-molecular/prolactin
    relation: connects-to
    note: "Immune-neuroendocrine modulation: prolactin modulates T-cell (already mapped) and B-cell (already mapped) autoimmune activation and postpartum rebound is linked to MS relapse, placing prolactin in the hormonal sex-immune dimension of multiple sclerosis."
  - target: 01-human/03-molecular/serotonin
    relation: connects-to
    note: "MS serotonin: serotonin, via 5-HT receptors on microglia (already mapped) and oligodendrocytes (already mapped), modulates neuroinflammation and remyelination; serotonin dysregulation amplifies the IL-6 (already mapped) and NLRP3 (already mapped) cascade of multiple sclerosis."
  - target: 01-human/03-molecular/oxytocin
    relation: connects-to
    note: "MS oxytocin: oxytocin, via OXTR on microglia (already mapped) and regulatory T cells (already mapped), attenuates neuroinflammation and promotes remyelination; oxytocin deficiency amplifies the IL-17a (already mapped) and IL-6 (already mapped) cascade of multiple sclerosis."
  - target: 01-human/03-molecular/vasopressin
    relation: connects-to
    note: "MS vasopressin: vasopressin, via V1aR on microglia (already mapped) and oligodendrocytes (already mapped), modulates BBB osmolality and neuroinflammation; vasopressin dysregulation amplifies NLRP3 (already mapped) and IL-6 (already mapped) cascade of multiple sclerosis."
  - target: 01-human/02-atomic/iodine
    relation: connects-to
    note: "MS iodine: iodine-dependent thyroid hormones regulate oligodendrocyte (already mapped) differentiation and myelin synthesis; iodine deficiency amplifies the remyelination failure and IL-6 (already mapped) neuroinflammatory cascade of multiple sclerosis."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "MS magnesium: magnesium, via NMDA-receptor (already mapped) blockade on oligodendrocytes (already mapped), reduces glutamate-driven excitotoxicity; magnesium deficiency amplifies the NLRP3 (already mapped) and IL-17a (already mapped) cascade of multiple sclerosis."
  - target: 01-human/02-atomic/copper
    relation: connects-to
    note: "MS copper: copper, as cofactor of cytochrome-c oxidase in oligodendrocytes (already mapped) and superoxide dismutase (already mapped), is essential for myelin synthesis; copper deficiency recapitulates the demyelinating cascade of multiple sclerosis."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "MS zinc: zinc cofactors NRF2 (already mapped) antioxidant defence in oligodendrocytes (already mapped); zinc deficiency amplifies NF-κB (already mapped) and IL-17a (already mapped) and NLRP3 (already mapped) neuroinflammation and demyelinating cascade in multiple sclerosis."
  - target: 01-human/02-atomic/phosphorus
    relation: connects-to
    note: "MS phosphorus: phosphorus fuels oligodendrocyte (already mapped) ATP and myelin biosynthesis; phosphorus deficiency impairs remyelination and amplifies NF-κB (already mapped) and microglia (already mapped)-driven neuroinflammation in multiple sclerosis."
  - target: 01-human/02-atomic/chloride
    relation: connects-to
    note: "MS chloride: chloride channels regulate macrophage (already mapped) and mast-cell (already mapped) ion homeostasis in the CNS; chloride imbalance amplifies NF-κB (already mapped) and IL-6 (already mapped) neuroinflammatory cascade of multiple sclerosis."
  - target: 01-human/02-atomic/sulfur
    relation: connects-to
    note: "MS sulfur: sulfur-containing amino acids in microglia (already mapped) and macrophages (already mapped) sustain CNS redox buffering; sulfur depletion amplifies NF-κB (already mapped) and IL-6 (already mapped) demyelinating cascade of multiple sclerosis."
  - target: 01-human/02-atomic/carbon
    relation: connects-to
    note: "MS carbon: carbon as backbone of myelin basic protein and NF-κB (already mapped) structural proteins in oligodendrocytes (already mapped) sustains remyelination; carbon depletion amplifies NF-κB (already mapped) and IL-6 (already mapped) cascade of multiple sclerosis."
  - target: 01-human/02-atomic/hydrogen
    relation: connects-to
    note: "MS hydrogen: hydrogen, via water and redox homeostasis in microglia (already mapped) and oligodendrocytes (already mapped), supports CNS remyelination; hydrogen dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) demyelinating cascade of multiple sclerosis."
  - target: 01-human/02-atomic/nitrogen
    relation: connects-to
    note: "MS nitrogen: nitrogen in amino-acid scaffold of myelin proteins and NF-κB (already mapped) transcription factors modulates oligodendrocyte (already mapped) remyelination; nitrogen dysregulation amplifies IL-6 (already mapped) cascade of multiple sclerosis."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "MS oxygen: oxygen supports aerobic metabolism in oligodendrocytes (already mapped) and microglia (already mapped) for remyelination; oxygen deficit amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) demyelinating cascade of multiple sclerosis."
  - target: 01-human/03-molecular/pd-1
    relation: connects-to
    note: "MS PD-1: PD-1 checkpoint on T-cells (already mapped) and microglia (already mapped) modulates CNS immune tolerance; PD-1 dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) autoimmune demyelinating cascade of multiple sclerosis."
  - target: 01-human/03-molecular/glp-1
    relation: connects-to
    note: "MS GLP-1: GLP-1 signalling in neurons (already mapped) and microglia (already mapped) promotes neuroprotection and oligodendrocyte (already mapped) survival; GLP-1 deficit amplifies NF-κB (already mapped) and IL-6 (already mapped) demyelinating cascade of multiple sclerosis."
  - target: 01-human/03-molecular/angiotensin-ii
    relation: connects-to
    note: "MS angiotensin-ii: angiotensin-II from astrocytes (already mapped) and macrophages (already mapped) drives vascular neuroinflammation; angiotensin-ii excess amplifies nf-kb (already mapped) and il-6 (already mapped) and tnf-alpha (already mapped) demyelinating cascade of MS."
  - target: 01-human/03-molecular/wnt-beta-catenin
    relation: connects-to
    note: "MS wnt-beta-catenin: WNT/β-catenin on neurons (already mapped) and astrocytes (already mapped) regulates oligodendrocyte survival; wnt-beta-catenin dysregulation amplifies nf-kb (already mapped) and il-6 (already mapped) and tnf-alpha (already mapped) MS cascade."
  - target: 01-human/03-molecular/rankl
    relation: connects-to
    note: "MS rankl: RANKL from microglia (already mapped) and astrocytes (already mapped) promotes CNS neuroinflammation; rankl excess amplifies nf-kb (already mapped) and il-6 (already mapped) and tnf-alpha (already mapped) demyelinating cascade of MS."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "MS vegf: VEGF from microglia (already mapped) and astrocytes (already mapped) promotes neuroinflammatory angiogenesis; vegf excess amplifies nf-kb (already mapped) and il-6 (already mapped) and tnf-alpha (already mapped) demyelinating cascade of MS."
  - target: 01-human/03-molecular/fibronectin
    relation: connects-to
    note: "MS fibronectin: fibronectin in microglia (already mapped) and astrocytes (already mapped) promotes CNS ECM remodelling; fibronectin excess amplifies nf-kb (already mapped) and il-6 (already mapped) and tnf-alpha (already mapped) demyelinating cascade of MS."
  - target: 01-human/03-molecular/notch
    relation: connects-to
    note: "MS notch: Notch signalling on microglia (already mapped) and astrocytes (already mapped) regulates oligodendrocyte fate; notch dysregulation amplifies nf-kb (already mapped) and il-6 (already mapped) and tnf-alpha (already mapped) demyelinating cascade of MS."
  - target: 01-human/03-molecular/activin-a
    relation: connects-to
    note: "MS activin-a: activin-A from microglia (already mapped) and astrocytes (already mapped) promotes CNS fibrotic remodelling; activin-a excess amplifies nf-kb (already mapped) and il-6 (already mapped) and tnf-alpha (already mapped) demyelinating cascade of MS."
  - target: 01-human/03-molecular/cgrp
    relation: connects-to
    note: "MS cgrp: CGRP from microglia (already mapped) and astrocytes (already mapped) modulates CNS neuroimmune tone; cgrp excess amplifies nf-kb (already mapped) and il-6 (already mapped) and tnf-alpha (already mapped) demyelinating cascade of MS."
  - target: 01-human/03-molecular/calcitonin
    relation: connects-to
    note: "MS calcitonin: calcitonin from microglia (already mapped) and astrocytes (already mapped) modulates CNS calcium balance; calcitonin excess amplifies nf-kb (already mapped) and il-6 (already mapped) and tnf-alpha (already mapped) demyelinating cascade of MS."
  - target: 01-human/03-molecular/substance-p
    relation: connects-to
    note: "MS substance-p: substance-P from microglia (already mapped) and astrocytes (already mapped) modulates CNS pain tone; substance-p excess amplifies nf-kb (already mapped) and il-6 (already mapped) and tnf-alpha (already mapped) demyelinating cascade of MS."
  - target: 01-human/03-molecular/insulin-receptor
    relation: connects-to
    note: "MS insulin-receptor: insulin receptor on microglia (already mapped) and astrocytes (already mapped) drives CNS metabolic repair; insulin-receptor loss amplifies nf-kb (already mapped) and il-6 (already mapped) and tnf-alpha (already mapped) demyelinating cascade of MS."
  - target: 01-human/03-molecular/aldosterone
    relation: connects-to
    note: "MS aldosterone: aldosterone from microglia (already mapped) and astrocytes (already mapped) modulates CNS ion balance; aldosterone excess amplifies nf-kb (already mapped) and il-6 (already mapped) and tnf-alpha (already mapped) demyelinating cascade of MS."
---

# Multiple Sclerosis

## Overview

**Multiple sclerosis (MS)** is the most common **autoimmune demyelinating disease of the central nervous system** — a chronic, inflammatory condition in which autoreactive T cells and B cells breach the blood-brain barrier and attack **myelin**, the lipid-rich insulating sheath produced by oligodendrocytes. The result is **demyelinating plaques** (sclerotic lesions) in white matter and grey matter, causing disrupted saltatory conduction → neurological symptoms; over time, axonal loss and cortical atrophy → permanent disability [^compston-2008-ms-review].

MS affects approximately **2.8 million people worldwide** (~1 million in the US), with an incidence of ~20-30 per 100,000 in high-risk regions (Northern Europe, Canada, New Zealand). Female:male ratio ~3:1; peak onset 20-40 years. It is the leading non-traumatic cause of neurological disability in young adults.

**MS subtypes:**
- **Relapsing-remitting MS (RRMS, ~85% at onset):** Discrete episodes (relapses/exacerbations) of neurological worsening over days-weeks → partial or complete recovery; MRI shows new or enhancing lesions; treatable with disease-modifying therapies (DMTs)
- **Secondary progressive MS (SPMS):** Develops in 50-80% of RRMS after 20+ years; steady accumulation of disability with or without relapses; less MRI activity but ongoing axonal loss; some DMTs (siponimod, cladribine) modestly effective
- **Primary progressive MS (PPMS, ~15%):** Insidious, continuous neurological deterioration from onset without clear relapses; predominantly spinal cord involvement → progressive paraplegia; until 2017, no approved therapy; ocrelizumab FDA approved 2017 [^montalban-2017-ocrelizumab-ppms]
- **Clinically isolated syndrome (CIS):** First clinical event consistent with MS (optic neuritis, myelitis, brainstem/cerebellar syndrome); 70-80% progress to MS within 20 years if MRI reveals disseminated lesions; early DMT initiation after CIS reduces conversion

**Risk factors:**
- **HLA-DRB1*15:01:** Strongest genetic risk factor (~3× increased risk); in linkage disequilibrium with HLA-DQB1*06:02; presents myelin peptides (MBP, MOG, PLP) to autoreactive CD4+ T cells
- **Epstein-Barr virus (EBV):** Nearly all MS patients are EBV+; longitudinal military cohort: EBV seroconversion → 32× increased MS risk; molecular mimicry between EBNA-1 and GlialCAM (myelin antigen) proposed mechanism; anti-EBNA-1 antibodies cross-react with CNS proteins
- **Vitamin D deficiency:** Low 25-OH-vitamin D → increased MS risk; VDR binding site in HLA-DRB1*15:01 promoter; latitude gradient of MS correlates with sunlight exposure
- **Smoking:** 1.5× increased MS risk; accelerates disability progression
- **Gut microbiome:** Dysbiosis in MS patients; Akkermansia muciniphila and Prevotella overrepresented; germ-free mice with MS-prone T cells develop disease with MS-patient microbiome transfer

## Structure

### MS lesion anatomy [^compston-2008-ms-review]

**Acute active plaque:**
- T cells (CD4+, CD8+) and macrophages infiltrate white matter via VCAM-1/ICAM-1 on activated BBB endothelium
- BBB disruption: gadolinium-enhancing on MRI (contrast T1) → first 4-6 weeks of plaque activity
- Macrophages and microglia phagocytose myelin → intracellular lipid droplets (foamy macrophages)
- Oligodendrocyte apoptosis → demyelinated axons
- Axonal transection can occur even in early acute lesions → irreversible damage

**Chronic inactive plaque:**
- Hypocellular center — demyelinated, gliotic; surrounded by sharp lesion edge
- Shadow plaques: partial remyelination by OPCs → thin, irregular myelin → "shadows" on histology; vulnerable to re-attack
- Slowly expanding plaques (SEL): Smoldering microglia activation at plaque edge → ongoing axonal damage in progressive MS

**Grey matter lesions (often underestimated):**
- Cortical lesions (leukocortical, intracortical, subpial) — not detected by conventional MRI; require double inversion recovery (DIR) or 7T MRI; correlate strongly with cognitive impairment
- **Meningeal inflammation:** Follicle-like B-cell aggregates in meninges in some PPMS patients → produce antibodies and cytokines → cortical demyelination (subpial spread)

### MS immunopathology

**Peripheral sensitization (lymph nodes):**
- Molecular mimicry or bystander activation → autoreactive CD4+ Th1/Th17 cells escape thymic deletion (low-affinity TCR for myelin antigens)
- EBV-infected B cells may present myelin antigens (EBNA-1/GlialCAM cross-reactivity) → autoreactive B cells persist

**CNS trafficking:**
- Activated Th1 (CCR5+) and Th17 (CCR6+) cells upregulate VLA-4 (alpha-4 beta-1 integrin) → bind VCAM-1 on inflamed BBB endothelium → transmigrate
- **Natalizumab:** Anti-alpha-4 integrin (VLA-4) antibody → blocks T cell and B cell CNS entry → 68% relapse rate reduction [^kappos-2006-natalizumab]
- Inside CNS: Reactivation of T cells by local APCs (microglia, dendritic cells) presenting myelin peptides (MBP 83-99, MOG 35-55, PLP 139-151) → effector T cell attack

**B cell role in MS:**
- RRMS: CSF oligoclonal bands (OCBs) in >95%; IgG produced by intrathecal B cells and plasma cells
- B cells present antigen to T cells, produce cytokines (IL-6, TNF-alpha, lymphotoxin), and activate complement → ocrelizumab (anti-CD20) highly effective
- Progressive MS: Meningeal B-cell follicles drive cortical demyelination

## Function

### Clinical presentation

**Relapse characteristics:**
- Subacute onset over hours-days → plateau → recovery over weeks-months
- Symptoms determined by lesion location: optic neuritis (pain with eye movement + central visual loss, optic nerve); myelitis (weakness/sensory deficit at/below a spinal level + bladder dysfunction, spinal cord); Lhermitte's sign (electric shock down spine with neck flexion, dorsal column); internuclear ophthalmoplegia (MLF lesion → dysconjugate gaze); cerebellar (Charcot's triad: dysarthria, nystagmus, intention tremor); Uhthoff's phenomenon (transient worsening with heat or exercise)

**Disability measures:**
- **EDSS (Expanded Disability Status Scale):** 0-10; 0 = normal; 4.0 = fully ambulatory without aid, limited by MS symptoms; 6.0 = requires walking aid; 7.0 = essentially restricted to wheelchair; 10.0 = death from MS; half-integer steps; primary endpoint in MS trials

**Cognitive symptoms:**
- Present in 40-65% of MS patients; processing speed and working memory most affected; correlates with grey matter atrophy and thalamic volume loss; no FDA-approved therapy for MS cognitive impairment

**Psychiatric:**
- Depression: ~50% lifetime prevalence; bidirectional (neuroinflammation → depression; MS diagnosis → reactive depression)
- Fatigue: Most common symptom; pathological fatigue (not purely mood or sleep-related); inflammatory mediators (IL-6, TNF-alpha) contribute; amantadine, modafinil modestly helpful

### Diagnosis (McDonald criteria 2017)

**Dissemination in space (DIS):** ≥1 T2 lesion in ≥2 of 4 areas: periventricular (≥3 lesions), juxtacortical/cortical, infratentorial, spinal cord

**Dissemination in time (DIT):** Gadolinium-enhancing lesion (active) AND non-enhancing lesion at same time point, OR new T2/enhancing lesion on follow-up MRI, OR OCBs in CSF

**CSF:** Oligoclonal IgG bands in CSF (not serum) in >95% of MS; elevated IgG index; pleocytosis (<50 cells/μL, predominantly lymphocytes); MOG-IgG and AQP4-IgG testing to exclude MOGAD and NMOSD

## Pathology

### Treatment [^montalban-2017-ocrelizumab-ppms]

**Disease-modifying therapies (DMTs) — platform therapies (moderate efficacy):**
- **Beta-interferons (IFN-beta-1a/1b):** Immunomodulatory; ~30% relapse reduction; SC or IM injection; flu-like symptoms, injection site reactions; first-line, safest in pregnancy after delivery
- **Glatiramer acetate (GA, Copaxone):** Random amino acid polymer; antigen competition or immunomodulation via Th2 shift; ~30% relapse reduction; daily SC; no systemic side effects; safe in pregnancy; antibody formation does not affect efficacy
- **Teriflunomide (Aubagio):** Oral; inhibits DHODH → proliferating lymphocytes; ~36% relapse reduction; teratogenic (accelerated elimination with cholestyramine needed pre-pregnancy)
- **Dimethyl fumarate (Tecfidera, BG-12):** Oral; activates Nrf2 → antioxidant pathway; shifts Th1 → Th2; reduces relapses ~50%; PML risk in lymphopenic patients (monitor lymphocyte count)

**High-efficacy DMTs:**
- **Natalizumab (Tysabri, anti-VLA-4):** IV monthly; 68% relapse reduction vs. placebo (AFFIRM trial); reserved for high-activity RRMS; **PML risk** (JC virus reactivation) in JC antibody+ patients (especially >2 years) — risk stratification by JC antibody index; switch to different therapy if index >0.9-1.5
- **Ocrelizumab (Ocrevus, anti-CD20):** IV every 6 months; 46-47% relapse reduction vs. IFN in RRMS; first approved for PPMS (25% reduction in 12-week confirmed disability progression, ORATORIO trial) [^montalban-2017-ocrelizumab-ppms]; infusion reactions; HBV reactivation screening; PML rare; check IgG levels; approved for RRMS and PPMS
- **Ofatumumab (Kesimpta, anti-CD20):** SC monthly then quarterly; non-inferior to teriflunomide in ASCLEPIOS I/II; self-administered SC injection; lower infection risk than IV ocrelizumab
- **Cladribine (Mavenclad):** Oral; purine analog → lymphocyte depletion → DNA strand breaks in lymphocytes; 2 short courses (4-5 days each, year 1 and year 2) → 5+ years of benefit; 58% relapse reduction vs. placebo; PML risk; lymphocyte monitoring required
- **Ublituximab (Briumvi, anti-CD20):** IV; quarterly after initial doses; ULTIMATE I/II vs. teriflunomide; similar mechanism to ocrelizumab
- **Alemtuzumab (Lemtrada, anti-CD52):** IV; severe B and T cell depletion → immune reconstitution; 49-55% superiority over beta-interferon in relapse reduction; reserved for highly active RRMS due to serious autoimmune AEs (thyroid disease ~30%, ITP, anti-GBM nephritis); risk-management program required

**Symptomatic treatment:**
- **Relapses:** IV methylprednisolone 1 g × 3-5 days → accelerates recovery (no long-term benefit); plasmapheresis for steroid-refractory severe relapses
- **Spasticity:** Baclofen (GABA-B agonist), tizanidine (alpha-2 agonist), oral or intrathecal
- **Bladder dysfunction:** Anticholinergics (oxybutynin, darifenacin) for overactive bladder; self-catheterization for retention; desmopressin for nocturia
- **Fatigue:** Amantadine (modest benefit), modafinil, exercise; treat underlying sleep disorders and depression
- **Pain:** Neuropathic pain — gabapentin, pregabalin, TCAs; trigeminal neuralgia → carbamazepine, oxcarbazepine
- **Walking:** Dalfampridine (4-aminopyridine, extended-release) — potassium channel blocker → improved nerve conduction in demyelinated axons; 10 mg BID; improves walking speed in ~35% of patients

## Connections

- `targets` → **[Brain](../../06-organ/brain/README.md)** — MS demyelinating plaques develop in periventricular white matter and cortical grey matter; brain volume loss (atrophy) correlates with long-term disability; meningeal B-cell follicles drive cortical demyelination in progressive MS via subpial spread.
- `connects-to` → **[Oligodendrocyte](../../04-cellular/oligodendrocyte/README.md)** — oligodendrocytes and their myelin sheaths are the primary MS targets; autoreactive T cells and complement attack myelin, causing demyelination; incomplete OPC remyelination in progressive MS drives permanent axonal loss and disability.
- `connects-to` → **[T Helper Cell](../../04-cellular/t-helper-cell/README.md)** — Th1 and Th17 cells are the primary MS pathogenic effectors; Th17 (CCR6+) breach the BBB via CCL20; both subsets attack myelin and activate microglia; natalizumab blocks VLA-4 integrin on T cells, preventing CNS trafficking.
- `connects-to` → **[Astrocyte](../../04-cellular/astrocyte/README.md)** — reactive astrocytes form glial scar in MS lesions, impeding OPC remyelination; astrocytes also sustain BBB integrity and produce neuroprotective factors (CNTF, LIF); astrocyte dysfunction is a primary driver of progressive MS and lesion repair failure.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — IL-17A is elevated in MS lesions and CSF; Th17 cells breach the blood-brain barrier via CXCR6 → demyelination; secukinumab (anti-IL-17A) paradoxically worsened MS relapse rates in phase 2 trials — suggesting complex compensatory roles of IL-17A/Treg balance in CNS disease.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5⁺ Th1 cells are recruited to CNS white matter MS lesions via CCL3/CCL4/CCL5 chemokines; CCR5-Δ32 heterozygosity is associated with modestly reduced MS severity in some epidemiological cohorts; CCR5 antagonism (maraviroc) is being explored as adjunct anti-inflammatory therapy in neuroinflammation.
- `connects-to` → **[Epstein-Barr Virus](../../../02-pathogen/01-viruses/epstein-barr-virus/README.md)** — Epstein-Barr virus is now considered a necessary cause of multiple sclerosis: a 10-million-person cohort showed MS risk jumps ~32-fold after EBV seroconversion, and EBV's EBNA-1 protein cross-reacts with the myelin protein GlialCAM — making EBV a leading target for MS prevention.
- `connects-to` → **[Myasthenia Gravis](../myasthenia-gravis/README.md)** — Multiple sclerosis and myasthenia gravis are both autoimmune neurological diseases: MS is a T-cell-driven demyelination of central myelin, whereas MG is an antibody attack on the neuromuscular junction — CNS versus peripheral, T-cell versus B-cell/complement.
- `connects-to` → **[Vitamin D](../../../03-medicine/03-food/vitamin-d/README.md)** — Low vitamin D is a consistent, modifiable multiple-sclerosis risk factor: the latitude gradient of MS tracks sunlight, a vitamin-D-response element sits in the HLA-DRB1*15:01 promoter, and supplementation is being studied for prevention.
- `connects-to` → **[NMOSD](../nmo/README.md)** — MS and NMOSD were long conflated until AQP4-IgG distinguished them: MS is T-cell/myelin-directed with small CNS plaques and a relapsing course, while NMOSD is AQP4-IgG astrocyte attack with severe optic neuritis and extensive myelitis—and MS drugs like interferon-β worsen NMOSD.
- `connects-to` → **[B Cell](../../04-cellular/b-cell/README.md)** — B cells are now central to multiple sclerosis: beyond antibody they present antigen and form meningeal follicles driving cortical damage, and anti-CD20 therapies (ocrelizumab, ofatumumab) that deplete B cells are among the most effective treatments for MS.
- `connects-to` → **[Eye](../../06-organ/eye/README.md)** — The eye is a frequent first window into multiple sclerosis: optic neuritis—painful monocular vision loss—is a common presenting attack, and internuclear ophthalmoplegia from a brainstem plaque is highly suggestive; OCT retinal thinning now tracks neurodegeneration in MS.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — Depression is the commonest psychiatric comorbidity of multiple sclerosis: it stems both from demyelinating lesions in mood circuits and from the burden of chronic disability—often underrecognized, it degrades quality of life and warrants active screening.
- `connects-to` → **[Type I Interferon](../../03-molecular/type-i-interferon/README.md)** — Type I interferon was the first disease-modifying therapy for multiple sclerosis: interferon-β shifts immunity away from the pro-inflammatory Th17/Th1 pattern driving demyelination, reducing relapses—paradoxically, since the same cytokine family drives autoimmunity.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — Multiple sclerosis is increasingly a neurodegenerative as well as demyelinating disease: beyond myelin loss, axonal and neuronal injury accumulates and underlies progressive disability, so neuroprotection—not just anti-inflammatory therapy—is a key unmet goal.
- `connects-to` → **[Microglia](../../04-cellular/microglia/README.md)** — Microglia are central to MS lesions: they strip myelin and present antigen to drive demyelination, but also clear debris to permit remyelination—the same brain-resident macrophages both damage and repair, making microglial phenotype a target in progressive MS.
- `connects-to` → **[Rheumatoid Arthritis](../rheumatoid-arthritis/README.md)** — Multiple sclerosis and rheumatoid arthritis are both autoimmune diseases driven by Th17 and autoreactive lymphocytes, but target different tissues—CNS myelin vs synovial joints—yet share genetic risk and respond to overlapping immunomodulators.
- `connects-to` → **[Cytotoxic T Cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Cytotoxic T cells contribute to MS damage: though CD4 Th cells initiate the attack, CD8 cytotoxic T cells dominate MS lesions and directly kill oligodendrocytes and neurons, helping explain the axonal loss that drives irreversible progressive disability.
- `connects-to` → **[CD20](../../03-molecular/cd20/README.md)** — CD20-targeted therapy transformed MS treatment: depleting CD20+ B cells with ocrelizumab or rituximab sharply cuts relapses, proving B cells—not just T cells—drive the disease, and giving the first effective drug for progressive MS.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — Multiple sclerosis is the prototypical demyelinating disease of the central nervous system: immune attack strips myelin from brain, spinal cord and optic nerve in scattered plaques, so its protean symptoms reflect lesions dispersed in space and time.
- `connects-to` → **[Immune System](../immune-system/README.md)** — MS is fundamentally an autoimmune disease: self-reactive lymphocytes breach the blood-brain barrier to attack myelin, so it overlaps with other autoimmunity and is treated by immunomodulation—shifting MS care from symptom control to immune-directed therapy.
- `connects-to` → **[Gut Microbiome](../gut-microbiome/README.md)** — The gut microbiome shapes multiple sclerosis risk and activity: altered gut flora can tip the balance between inflammatory and regulatory T cells that attack myelin, so diet and the microbiome are emerging factors in an autoimmune disease of the brain.
- `connects-to` → **[Regulatory T Cell](../../04-cellular/regulatory-t-cell/README.md)** — MS reflects failed immune tolerance: regulatory T cells that should restrain autoreactive cells are deficient or dysfunctional, letting myelin-attacking T and B cells run unchecked—so restoring regulatory balance is a goal of MS therapy.
- `connects-to` → **[Plasma Cell](../../04-cellular/plasma-cell/README.md)** — Plasma cells leave MS's diagnostic signature: B cells mature into plasma cells inside the CNS and secrete antibodies detected as oligoclonal bands in spinal fluid, a hallmark that supports diagnosis and reflects the intrathecal immune response.
- `connects-to` → **[NLRP3 Inflammasome](../../03-molecular/nlrp3-inflammasome/README.md)** — The inflammasome fuels the smouldering side of MS: NLRP3 in microglia and macrophages releases IL-1β and IL-18 that amplify Th17 demyelination and chronic active-lesion damage, making it a target for progressive disease.
- `connects-to` → **[BDNF](../../03-molecular/bdnf/README.md)** — Repair in MS rides on BDNF: immune cells and neurons secrete this neurotrophin to support oligodendrocyte survival and remyelination, so boosting it is a neuroprotective strategy beyond suppressing the autoimmune attack.
- `connects-to` → **[Neuropathic Pain](../neuropathic-pain/README.md)** — Pain in MS is largely neuropathic: demyelinating lesions in sensory pathways and the spinal cord generate central neuropathic pain, trigeminal neuralgia, and Lhermitte's sign — among the disease's most disabling non-motor symptoms.
- `connects-to` → **[MHC Class II](../../03-molecular/mhc-class-ii/README.md)** — MS's strongest genetic risk is an MHC class II allele: HLA-DRB1*15:01 shapes how myelin peptides are presented to T cells, the genetic basis tying the immune system's antigen presentation to attacks on the central nervous system.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Macrophages strip myelin in active MS lesions: drawn into the CNS, they (with microglia) phagocytose myelin and damage oligodendrocytes, so myelin-laden macrophages are the histologic signature of an active demyelinating plaque.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Iron rims mark MS's smoldering lesions: iron-laden microglia ring chronic active plaques, visible as paramagnetic rim lesions on MRI that flag ongoing, treatment-resistant inflammation driving progression.
- `connects-to` → **[Sodium](../../02-atomic/sodium/README.md)** — Sodium channels betray the demyelinated MS axon: stripped of myelin, the axon scatters sodium channels to keep firing, but this leaky, energy-hungry state lets sodium and calcium flood in, driving the axonal degeneration behind permanent disability.
- `connects-to` → **[Nitric Oxide](../../03-molecular/nitric-oxide/README.md)** — Nitric oxide is a hidden axon-killer in MS: activated microglia and macrophages pour out NO that blocks nerve conduction and poisons mitochondria in demyelinated axons, contributing to both the symptoms and the slow neurodegeneration.
- `connects-to` → **[Glutamate](../../03-molecular/glutamate/README.md)** — Glutamate excitotoxicity widens MS damage: inflamed lesions spill excess glutamate that overexcites and kills oligodendrocytes and neurons, so beyond immune attack, this neurotransmitter helps turn inflammation into lasting tissue loss.
- `connects-to` → **[Synapse](../../05-tissue/synapse/README.md)** — MS damage reaches the synapse: beyond stripping myelin, the disease erodes gray-matter synapses, and this synaptic loss tracks the cognitive decline and disability that demyelination alone does not explain.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Calcium executes the axon loss in MS: demyelinated axons overload with sodium, which reverses the sodium-calcium exchanger and floods them with calcium, the influx that degrades the axon and drives permanent disability.
- `connects-to` → **[Mast Cell](../../04-cellular/mast-cell/README.md)** — Mast cells help open the brain to MS attack: in lesions they release mediators that breach the blood-brain barrier and amplify demyelination, linking an allergic-type immune cell to the autoimmune assault on myelin.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — MS is diagnosed and tracked by MRI: its photons reveal the white-matter plaques scattered in space and time, and gadolinium enhancement flags the active, inflamed lesions.
- `connects-to` → **[Potassium](../../02-atomic/potassium/README.md)** — MS exposes axonal potassium channels: demyelination uncovers them and leaks current, so the drug dalfampridine blocks potassium channels to restore conduction and improve walking.
- `connects-to` → **[Bone Marrow](../../05-tissue/bone-marrow/README.md)** — Aggressive MS can be reset from the bone marrow: autologous hematopoietic stem-cell transplant wipes out and rebuilds the immune system, halting relapses in selected severe cases.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy shows MS stripping the nerves bare: in the plaque, immune cells peel the myelin sheath off axons, leaving naked fibers that conduct poorly — and patchy, often incomplete, remyelination by surviving oligodendrocytes.
- `connects-to` → **[Large Intestine](../../06-organ/large-intestine/README.md)** — MS disconnects the bowel: lesions in the spinal cord disrupt the nerves controlling defecation, so neurogenic constipation and incontinence are common, disabling, and often under-discussed symptoms.
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — MS endangers the kidney through the bladder: cord lesions cause a neurogenic bladder that retains urine, breeding recurrent infections and back-pressure that, untreated, can damage the kidneys over time.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — Antibodies both reveal and treat MS: oligoclonal IgG bands in the spinal fluid support the diagnosis, and B-cell-depleting monoclonal antibodies (ocrelizumab, rituximab) are among its most effective disease-modifying therapies.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — MS bends to reproductive hormones: it strikes women far more often, relapses quiet during pregnancy then rebound after delivery, and family planning shapes the choice and timing of disease-modifying drugs.
- `connects-to` → **[Smooth Muscle Cell](../../04-cellular/smooth-muscle-cell/README.md)** — Demyelination disconnects the body's smooth muscle: cord lesions disrupt the autonomic control of the bowel into constipation and of the bladder's detrusor, the dysmotility behind much of the disability between relapses.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — MS plays out in the muscles it can no longer command: demyelinated motor pathways cause spasticity, weakness, and a faltering gait, and the disuse and immobility that follow waste muscle and stiffen joints.
- `connects-to` → **[Neutrophil](../../04-cellular/neutrophil/README.md)** — The disease-modifying drugs reshape the blood counts: agents like cladribine and fingolimod cause lymphopenia and can drop neutrophils, so counts are monitored and infection risk weighed against relapse control.
- `connects-to` → **[Thyroid Gland](../../06-organ/thyroid/README.md)** — Treatment can turn the immunity on the thyroid: the MS drug alemtuzumab notoriously triggers autoimmune thyroid disease, often Graves', months to years later — one of several autoimmunities that follow immune reconstitution.
- `connects-to` → **[Natural Killer Cell](../../04-cellular/natural-killer-cell/README.md)** — Natural killer cells help police MS: their regulatory subsets restrain autoreactive T cells, and expanding them is how the antibody daclizumab worked — a reminder that innate lymphocytes, not just T and B cells, shape the disease.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Complement scars the progressive brain: C3 and the membrane-attack complex deposit in MS lesions, especially in the slow-burning cortical and progressive disease, marking a tissue-damage arm beyond the T-cell attack.
- `connects-to` → **[Peripheral Nerve](../../05-tissue/peripheral-nerve/README.md)** — MS spares the peripheral nerves, which sharpens the diagnosis: it demyelinates only the central oligodendrocyte myelin, so peripheral conduction stays normal — the line that separates it from CIDP and Guillain-Barré, though rare combined forms exist.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — NF-κB sits at the genetic heart of MS: several MS risk variants converge on NF-κB signaling, the pathway through which activated T cells and microglia drive the inflammatory demyelination of the disease.
- `connects-to` → **[Sepsis](../sepsis/README.md)** — A neurogenic bladder opens the way to deadly infection: urinary retention from spinal-cord lesions causes recurrent UTIs, and urosepsis — worsened by immunosuppressive disease-modifying therapy — is a leading cause of death in advanced MS.
- `connects-to` → **[Insomnia Disorder](../insomnia-disorder/README.md)** — Sleep is broken on many fronts: pain, spasticity, nocturia and depression fragment sleep in MS, so insomnia is common and deepens the fatigue that is among the disease's most pervasive complaints.
- `connects-to` → **[Osteoporosis](../osteoporosis/README.md)** — Immobility, steroids and low vitamin D thin the bone: reduced mobility, repeated corticosteroid courses for relapses and the vitamin D deficiency tied to MS itself accelerate bone loss and fracture risk.
- `connects-to` → **[Pneumocystis jirovecii](../../../02-pathogen/03-fungi/pneumocystis-jirovecii/README.md)** — Its potent therapies open the lung: the immunosuppressive disease-modifying drugs and steroids used in MS can drop T-cell defenses enough to risk Pneumocystis pneumonia, weighed during high-intensity treatment.
- `connects-to` → **[Epilepsy](../epilepsy/README.md)** — Cortical lesions can spark seizures: demyelinating plaques reaching the cerebral cortex make seizures and epilepsy several-fold more common in MS than in the general population.
- `connects-to` → **[Chronic Kidney Disease](../ckd/README.md)** — A neurogenic bladder endangers the kidneys: spinal demyelination in MS impairs bladder control, and the recurrent urinary infections and back-pressure that follow can progress over years to chronic kidney disease.
- `connects-to` → **[Aspergillus fumigatus](../../../02-pathogen/03-fungi/aspergillus-fumigatus/README.md)** — Its disease-modifying drugs blunt immunity: the immunosuppressive and B-cell-depleting therapies for MS, like ocrelizumab and fingolimod, can permit opportunistic infections including invasive aspergillosis.
- `connects-to` → **[Wound Healing](../wound-healing/README.md)** — Immobility and lost sensation break down the skin: as MS advances to wheelchair or bedbound disability with impaired sensation, pressure ulcers form and heal slowly over insensate, poorly perfused skin.
- `connects-to` → **[Renal System](../renal-system/README.md)** — Spinal demyelination wrecks bladder control: neurogenic bladder is one of the most common and disabling features of MS, causing urgency, incontinence and retention with recurrent UTIs and upper-tract damage.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — It disrupts the bowel too: MS commonly causes neurogenic bowel with constipation and faecal incontinence, and brainstem lesions can produce dysphagia with aspiration risk.
- `connects-to` → **[Varicella-Zoster Virus](../../../02-pathogen/01-viruses/varicella-zoster-virus/README.md)** — Its immunotherapies reawaken shingles: the B-cell-depleting and S1P-modulator disease-modifying therapies for MS, especially fingolimod, raise the risk of herpes-zoster reactivation.
- `connects-to` → **[Respiratory System](../respiratory-system/README.md)** — Advanced disease weakens breathing: brainstem and high cervical lesions impair respiratory muscles and swallowing, so aspiration and respiratory failure become a leading cause of death in late MS.
- `connects-to` → **[Cardiovascular System](../cardiovascular-system/README.md)** — Nerves and drugs unsettle the heart: autonomic dysfunction causes orthostatic hypotension and arrhythmia, and starting fingolimod causes first-dose bradycardia and heart block requiring monitoring.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — Immobility and injections mark the skin: pressure sores arise with reduced mobility, while injectable disease-modifying therapies cause injection-site reactions and lipoatrophy.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — Its strong therapies disturb hormones: alemtuzumab commonly triggers autoimmune thyroid disease, and the high-dose steroids used for relapses bring their own endocrine effects.
- `connects-to` → **[Lymphatic System](../lymphatic-system/README.md)** — Modern treatment works through the lymphocytes: natalizumab blocks their entry to the brain, fingolimod traps them in lymph nodes and ocrelizumab depletes B cells, reshaping the immune traffic that drives MS.
- `connects-to` → **[Herpesvirus](../../../02-pathogen/01-viruses/herpesvirus/README.md)** — Herpesviruses are implicated alongside EBV: human herpesvirus-6 has been studied as a co-factor in multiple sclerosis, and reactivation under immunosuppressive therapy is a clinical concern.
- `connects-to` → **[Corticosteroids](../../../03-medicine/01-modern/02-respiratory/corticosteroids/README.md)** — Steroids cut short the relapse: high-dose corticosteroids speed recovery from acute MS relapses by damping CNS inflammation, though they do not change the long-term course of the disease.
- `connects-to` → **[Migraine](../migraine/README.md)** — Headache shadows demyelination: migraine is more common in multiple sclerosis than in the general population, the two sharing neuroinflammatory and vascular mechanisms.
- `connects-to` → **[Dendritic Cell](../../04-cellular/dendritic-cell/README.md)** — They present the myelin antigen: dendritic cells in lymph nodes and the inflamed CNS activate the autoreactive T cells that attack myelin, a key step in initiating and sustaining multiple sclerosis.
- `connects-to` → **[Targeted Therapy](../../../03-medicine/01-modern/13-cancer/targeted-therapy/README.md)** — Targeted DMTs reshaped its course: anti-CD20 antibodies (ocrelizumab), natalizumab against VLA-4, S1P modulators and BTK inhibitors suppress the relapses of multiple sclerosis far more effectively than older interferons.
- `connects-to` → **[Axonal Transport](../../05-tissue/axonal-transport/README.md)** — Axonal loss drives disability: beyond demyelination, MS transects and degenerates axons whose disrupted transport underlies the irreversible progressive disability that current immunotherapies only partly prevent.
- `connects-to` → **[Cancer Chemotherapy](../../../03-medicine/01-modern/13-cancer/cancer-chemotherapy/README.md)** — Chemo and transplant for aggressive disease: cladribine and mitoxantrone deplete lymphocytes in MS, and autologous haematopoietic stem-cell transplant after intense conditioning can halt highly active relapsing disease.
- `connects-to` → **[Germinal Center](../../05-tissue/germinal-center/README.md)** — EBV and B cells behind MS: Epstein-Barr infection is now a near-prerequisite, and ectopic B-cell follicles resembling germinal centres form in the meninges of progressive MS—the compartmentalised inflammation that anti-CD20 therapy targets.
- `connects-to` → **[CIDP](../cidp/README.md)** — Central versus peripheral demyelination: MS strips myelin in the CNS while CIDP strips it from peripheral nerves—autoimmune attacks on the same insulating sheath in two compartments.
- `connects-to` → **[Inflammatory Bowel Disease](../inflammatory-bowel-disease/README.md)** — A shared autoimmune axis: MS and inflammatory bowel disease co-occur and share Th17/IL-17 biology and gut-microbiome influences, and some MS therapies can unmask or worsen colitis.
- `connects-to` → **[COVID-19 Disease](../covid-19-disease/README.md)** — Immunotherapy meets infection: the B-cell-depleting MS therapies like ocrelizumab blunt the antibody response to COVID-19 vaccination and raise the risk of severe COVID-19, complicating treatment.
- `connects-to` → **[Bipolar Disorder](../bipolar-disorder/README.md)** — Mood disorder in demyelinating disease: multiple sclerosis raises the risk of bipolar disorder and mania, from demyelinating lesions in mood circuits and from corticosteroid treatment of relapses.
- `connects-to` → **[Hippocampus](../../05-tissue/hippocampus/README.md)** — Cognition in MS: demyelination and atrophy of the hippocampus contribute to the memory impairment and 'cog fog' that affect many MS patients, beyond the classic motor and sensory deficits.
- `connects-to` → **[Obsessive-Compulsive Disorder](../obsessive-compulsive-disorder/README.md)** — Lesion-driven OCD: demyelinating plaques in frontal and basal-ganglia circuits can produce secondary obsessive-compulsive symptoms, one of the neuropsychiatric manifestations of multiple sclerosis.
- `connects-to` → **[Hepatitis B](../hepatitis-b/README.md)** — Reactivation risk from anti-CD20: the B-cell-depleting therapies (ocrelizumab, rituximab) central to MS treatment can reactivate latent hepatitis B, mandating screening and antiviral prophylaxis.
- `connects-to` → **[Intestinal Epithelium](../../05-tissue/intestinal-epithelium/README.md)** — The gut-brain axis in MS: the microbiome and intestinal-barrier integrity shape MS susceptibility and relapse activity through immune signalling, an emerging influence on the demyelinating disease.
- `connects-to` → **[IFN-γ](../../03-molecular/ifn-gamma/README.md)** — Th1 demyelination: IFN-γ from autoreactive T-helper cells activates microglia and macrophages to attack myelin, a central cytokine of the inflammatory lesions of multiple sclerosis.
- `connects-to` → **[TNF-α](../../03-molecular/tnf-alpha/README.md)** — Inflammatory injury: TNF-α contributes to the oligodendrocyte damage and blood-brain-barrier breakdown of MS lesions, though paradoxically anti-TNF therapy worsens the disease.
- `connects-to` → **[Osteopontin](../../03-molecular/osteopontin/README.md)** — Relapse biomarker: osteopontin is elevated in MS lesions and CSF, promoting the survival of autoreactive T cells and tracking with relapse and disease activity.
- `connects-to` → **[BAFF](../../03-molecular/baff/README.md)** — B-cell survival: BAFF supports the autoreactive B cells and meningeal lymphoid follicles increasingly recognised in MS, part of the rationale behind the dramatic efficacy of anti-CD20 B-cell depletion.
- `connects-to` → **[Interleukin-6](../../03-molecular/il-6/README.md)** — Th17 differentiation: IL-6 with TGF-beta drives the pathogenic Th17 cells that breach the blood-brain barrier and orchestrate the demyelinating attacks of multiple sclerosis.
- `connects-to` → **[CCL2](../../03-molecular/ccl2/README.md)** — CNS trafficking: CCL2 helps recruit monocytes and autoreactive leukocytes across the blood-brain barrier into MS lesions, contributing to the inflammatory demyelination.
- `connects-to` → **[BTK](../../03-molecular/btk/README.md)** — BTK transduces B-cell-receptor and Fc-receptor signals in the B cells and microglia driving MS, the target of CNS-penetrant BTK inhibitors (tolebrutinib) developed to address the smouldering inflammation of progressive disease.
- `connects-to` → **[Perforin](../../03-molecular/perforin/README.md)** — CD8 T cells, which actually outnumber CD4 cells in MS plaques, use perforin-mediated cytotoxicity to injure oligodendrocytes and transect axons, contributing to the irreversible neurodegeneration of disease progression.
- `connects-to` → **[IL-2](../../03-molecular/il-2/README.md)** — IL2RA (CD25) is an established MS susceptibility gene, and impaired IL-2-dependent regulatory-T-cell function lets autoreactive T cells escape control—a genetic and mechanistic basis for low-dose IL-2 strategies in MS.
- `connects-to` → **[LMP1](../../03-molecular/lmp1/README.md)** — Epstein-Barr virus is the leading environmental cause of MS, with EBV-infected B cells expressing latency proteins persisting in patients and EBV antigens cross-reacting with myelin (molecular mimicry), a basis for the efficacy of B-cell depletion.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — In the demyelinated axon, dysregulated sodium and calcium influx drives the calcium overload that destroys mitochondria and axons, the mechanism of the progressive neurodegeneration underlying irreversible MS disability.
- `connects-to` → **[IGF-1](../../03-molecular/igf-1/README.md)** — IGF-1 promotes the survival and differentiation of oligodendrocyte precursors that remyelinate stripped axons, a trophic axis whose insufficiency contributes to the failed remyelination of chronic MS lesions.
- `connects-to` → **[NRF2](../../03-molecular/nfe2l2/README.md)** — Dimethyl fumarate, a first-line MS therapy, activates the NRF2 antioxidant pathway to protect oligodendrocytes and neurons from the oxidative injury that drives demyelination and neurodegeneration.
- `connects-to` → **[Caspase-3](../../03-molecular/caspase-3/README.md)** — Caspase-3-mediated apoptosis of oligodendrocytes and neurons contributes to the demyelination and the progressive axonal loss that underlies disability accumulation in multiple sclerosis.
- `connects-to` → **[Connexin-43](../../03-molecular/connexin43/README.md)** — Loss of astrocyte-oligodendrocyte connexin-43 gap junctions in MS plaques impairs the panglial network that supports myelin, contributing to lesion formation and expansion.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — IL-23 sustains the pathogenic Th17 cells (IL-17A already mapped) that cross the blood-brain barrier and drive the demyelinating inflammation of multiple sclerosis.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — Inflammatory-cytokine and type-I-interferon signaling through JAK-STAT (type-I IFN already mapped) governs the autoreactive T-cell responses of MS, the axis through which IFN-β therapy partly acts.
- `connects-to` → **[Transforming Growth Factor Beta](../../03-molecular/tgf-beta/README.md)** — TGF-β drives regulatory T-cell differentiation that restrains CNS autoimmunity, and its balance against the IL-6/IL-23 milieu (both mapped) sets the Treg-Th17 equilibrium central to MS.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — STAT3 signaling downstream of IL-6 and IL-23 (both mapped) drives the pathogenic Th17 differentiation central to multiple sclerosis.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — PI3K-AKT signaling supports oligodendrocyte survival and remyelination, processes whose failure contributes to progressive multiple sclerosis.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Microglial galectin-3 promotes the demyelinating neuroinflammation of multiple sclerosis lesions.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — IFN-STAT1 signaling underlies both the antiviral interferon response and the mechanism of IFN-β disease-modifying therapy in multiple sclerosis.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — Cytosolic DNA sensing through cGAS-STING contributes to the innate neuroinflammation that drives demyelinating lesion formation in multiple sclerosis.
- `connects-to` → **[SMAD4](../../03-molecular/smad4/README.md)** — TGF-β-SMAD signaling (TGF-β already mapped) governs the regulatory-T-cell balance and remyelination responses relevant to multiple sclerosis.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — FOXO transcription factors regulate the T-cell tolerance and oligodendrocyte oxidative-stress responses relevant to the autoimmune demyelination of multiple sclerosis.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — ERK-MAPK signaling transduces the cytokine and T-cell-receptor stimuli driving the autoreactive T-cell activation of multiple sclerosis.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — S100A8/A9 alarmins amplify the myeloid-driven neuroinflammation of the demyelinating lesions of multiple sclerosis.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β modulates the Th17-driven autoimmune and neuroinflammatory signaling of multiple sclerosis.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — PI3K (PIK3CA)-AKT signaling (AKT already mapped) supports the survival and activation of the autoreactive T and B cells of multiple sclerosis.
- `connects-to` → **[HIF-1alpha](../../03-molecular/hif-1alpha/README.md)** — HIF-1α in the hypoxic demyelinated lesion contributes to the metabolic injury and immune-cell metabolism of multiple sclerosis.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK-linked immunometabolic signaling shapes the autoreactive T-cell metabolism of multiple sclerosis.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — Autophagy modulates the survival of autoreactive lymphocytes and the antigen presentation of multiple sclerosis.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — DNMT3A-mediated DNA methylation contributes to the epigenetic dysregulation of the autoreactive immune response in multiple sclerosis.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — CXCL12-CXCR4 signaling participates in the leukocyte trafficking across the blood-brain barrier in multiple sclerosis.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — IL-33 alarmin signaling participates in the neuroinflammatory and demyelinating responses of multiple sclerosis.
- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — SRC-family kinase signaling participates in the immune-cell and glial signaling of multiple sclerosis.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — IL-1β-driven inflammation participates in the neuroinflammation and demyelination of multiple sclerosis.
- `connects-to` → **[ARID1A](../../03-molecular/arid1a/README.md)** — ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic regulation of the immune responses of multiple sclerosis.
- `connects-to` → **[Calcineurin](../../03-molecular/calcineurin/README.md)** — Calcineurin-NFAT signaling participates in the autoreactive T-cell activation of multiple sclerosis.
- `connects-to` → **[Estrogen](../../03-molecular/estrogen/README.md)** — Sex and pregnancy: multiple sclerosis is far more common in women, and relapses fall sharply in the third trimester when estrogen and progesterone are high, implicating sex hormones in disease modulation and inspiring estriol trials.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Obesity risk: adolescent obesity raises the risk of multiple sclerosis, and the proinflammatory adipokine leptin promotes the Th17 responses (IL-17A already mapped) that drive autoimmune demyelination.
- `connects-to` → **[BCL-2](../../03-molecular/bcl-2/README.md)** — Autoreactive survival: anti-apoptotic BCL-2 family proteins prolong the survival of the autoreactive lymphocytes that attack myelin, and shifting this balance toward apoptosis is one way immune-reconstitution therapies reset the disease.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — Th2 counter-response: IL-4 drives the protective type-2 T-cell response, and shifting the balance away from the pathogenic Th17 and Th1 arms (IL-17/IFN-gamma already mapped) toward IL-4-driven immunity is a long-sought therapeutic aim in multiple sclerosis.
- `connects-to` → **[IL-10](../../03-molecular/il-10/README.md)** — Regulatory suppression: IL-10 from regulatory B and T cells restrains the autoimmune attack on myelin, and deficient IL-10-mediated regulation contributes to the unchecked inflammation of multiple sclerosis.
- `connects-to` → **[Progesterone](../../03-molecular/progesterone/README.md)** — Pregnancy protection: relapses fall markedly in the third trimester of pregnancy, when progesterone and estrogen (already mapped) are high, implicating these neurosteroids in the immune modulation and remyelination potential in multiple sclerosis.
- `connects-to` → **[Xanthine oxidase](../../03-molecular/xanthine-oxidase/README.md)** — Oxidative axonal injury: reactive oxygen species, to which xanthine oxidase contributes, drive the mitochondrial and axonal injury (NRF2 already mapped) that underlies the progressive, demyelination-independent neurodegeneration of multiple sclerosis.
- `connects-to` → **[Cholesterol](../../03-molecular/cholesterol/README.md)** — Myelin lipid and repair: cholesterol is a major component of myelin and is required for remyelination by oligodendrocytes (already mapped), so its metabolism shapes both the injury and the repair capacity in multiple sclerosis.
- `connects-to` → **[Prostaglandins](../../03-molecular/prostaglandins/README.md)** — Lesion eicosanoids: prostaglandins from the activated microglia (already mapped) and infiltrating cells contribute to the neuroinflammation (IL-6, TNF and IL-1 already mapped) of the active demyelinating lesion in multiple sclerosis.
- `connects-to` → **[Astrocyte](../../04-cellular/astrocyte/README.md)** — Astrogliosis and the glial scar: the reactive astrocytes form the sclerotic glial scar that names multiple sclerosis, and their gap junctions (connexin43 already mapped) and gliotransmission shape both the lesion and the impaired repair.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Axonal calcium overload: the glutamate (already mapped) excitotoxicity and the energy failure of the demyelinated axon load it with calcium, driving the axonal degeneration that underlies the progressive disability of multiple sclerosis.
- `connects-to` → **[Omega-3 fatty acids](../../../03-medicine/03-food/omega-3-fatty-acids/README.md)** — Omega-3 and myelin: the omega-3 fatty acids are structural lipids of myelin (cholesterol already mapped) and give rise to pro-resolving mediators, the basis of dietary interest in omega-3 for multiple sclerosis.
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — Type-2 counter-arm: IL-13, with IL-4 (already mapped), is part of the Th2/anti-inflammatory arm (IL-10 already mapped) that counters the Th17 and Th1 (IL-17, IL-23 and IFN-γ already mapped) drive of multiple sclerosis.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — Adipokine and MS risk: adiponectin, with leptin (already mapped), is part of the adipokine dimension of the obesity that is a risk factor for multiple sclerosis, the metabolic-immune crosstalk shaping the disease.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), links the adipose-inflammatory milieu (IL-6 already mapped) to the obesity-associated risk and activity of multiple sclerosis.
- `connects-to` → **[Microglia](../../04-cellular/microglia/README.md)** — Smouldering plaque: the microglia and macrophages (CCL2 already mapped) strip the myelin and drive the smouldering (the chronic active plaques) neuroinflammation of multiple sclerosis.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — Axonal degeneration: the axonal and neuronal loss (glutamate excitotoxicity already mapped) underlies the progressive, irreversible disability of multiple sclerosis.
- `connects-to` → **[Vitamin D](../../../03-medicine/03-food/vitamin-d/README.md)** — Vitamin-D risk: the low vitamin D (the latitude gradient, the EBV/LMP1 already mapped interaction) is a modifiable multiple-sclerosis risk factor and a candidate modifier of the disease course.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm that, with the Th17 (IL-17 and IL-23 already mapped), drives the CNS autoimmunity of multiple sclerosis.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Type-2 counter-arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension balancing the Th1/Th17 drive of multiple sclerosis.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — Type-2 IgE: the IgE (with IL-4 and IL-13 already mapped) reflects the type-2 immune dimension of the immune dysregulation of multiple sclerosis.
- `connects-to` → **[Histamine](../../03-molecular/histamine/README.md)** — Mast-cell/remyelination axis: the histamine, from the mast cells (already mapped), modulates the blood-brain-barrier and the demyelination; the antihistamine clemastine is trialed to promote remyelination in multiple sclerosis.
- `connects-to` → **[Selenium](../../02-atomic/selenium/README.md)** — Antioxidant micronutrient: selenium, a cofactor of the antioxidant selenoproteins, is part of the oxidative-stress and micronutrient dimension (with vitamin D already mapped) studied in multiple sclerosis.
- `connects-to` → **[Systemic lupus erythematosus](../systemic-lupus-erythematosus/README.md)** — Autoimmune comorbidity: multiple sclerosis shares the autoimmune susceptibility with systemic lupus erythematosus, and the two can co-occur or enter the differential of CNS demyelination.
- `connects-to` → **[Complement C5](../../03-molecular/complement-c5/README.md)** — Terminal complement: the complement C5 and its activation (with C3 already mapped) contribute to the demyelinating injury within the multiple-sclerosis lesion.
- `connects-to` → **[C5aR1](../../03-molecular/c5ar1/README.md)** — C5a receptor: the C5aR1 signalling links the complement to the microglial (already mapped) and myeloid activation of the active multiple-sclerosis lesion.
- `connects-to` → **[Factor H](../../03-molecular/factor-h/README.md)** — Complement regulation: factor H regulates the alternative complement pathway (complement C3, C5 and C5aR1 already mapped), and its dysregulation is part of the complement contribution to the demyelination of multiple sclerosis.
- `connects-to` → **[C1-esterase inhibitor](../../03-molecular/c1-esterase-inhibitor/README.md)** — Classical-pathway regulation: the C1-esterase inhibitor regulates the classical complement pathway activated by the anti-myelin antibodies (immunoglobulin already mapped) that contribute to the demyelination of multiple sclerosis.
- `connects-to` → **[Transferrin](../../03-molecular/transferrin/README.md)** — Brain iron: transferrin, the iron carrier, reflects the disordered brain-iron handling that drives the oxidative injury and the oligodendrocyte ferroptosis of the demyelination of multiple sclerosis.
- `connects-to` → **[Periostin](../../03-molecular/periostin/README.md)** — Lesion matricellular: periostin, a matricellular mediator, is part of the tissue remodelling and the astrocytic (already mapped) scarring of the chronic multiple-sclerosis lesion.
- `connects-to` → **[TSLP](../../03-molecular/tslp/README.md)** — Alarmin-BBB axis: TSLP, from choroid-plexus and CNS-border epithelium disrupted in MS, primes dendritic cells (already mapped) toward Th17 (already mapped) priming and amplifies the BBB breach driving the lesion formation of multiple sclerosis.
- `connects-to` → **[Bradykinin](../../03-molecular/bradykinin/README.md)** — Kinin-demyelination axis: bradykinin, via B2R on CNS neurons (already mapped) and oligodendrocytes (already mapped), amplifies the BBB permeability and the neuroinflammation contributing to the oligodendrocyte loss and the demyelination of multiple sclerosis.
- `connects-to` → **[Erythropoietin](../../03-molecular/erythropoietin/README.md)** — Neuroprotective EPO: erythropoietin, via EpoR on neurons (already mapped) and oligodendrocytes (already mapped), promotes remyelination and exerts anti-inflammatory neuroprotection relevant to the relapsing-remitting course of multiple sclerosis.
- `connects-to` → **[Melatonin](../../03-molecular/melatonin/README.md)** — Circadian-immune axis: melatonin has immunomodulatory and neuroprotective effects on T-cell (already mapped) and microglial (already mapped) activity; disrupted melatonin rhythm is associated with MS relapse rate and the circadian immune dysregulation of multiple sclerosis.
- `connects-to` → **[Testosterone](../../03-molecular/testosterone/README.md)** — Neuroprotective androgen: testosterone exerts neuroprotective and anti-inflammatory effects on oligodendrocytes (already mapped) and T cells (already mapped); low testosterone is associated with faster MS disability progression and the male sex-hormone dimension of MS.
- `connects-to` → **[Prolactin](../../03-molecular/prolactin/README.md)** — Immune-neuroendocrine modulation: prolactin modulates T-cell (already mapped) and B-cell (already mapped) autoimmune activation and postpartum rebound is linked to MS relapse, placing prolactin in the hormonal sex-immune dimension of multiple sclerosis.
- `connects-to` → **[Serotonin](../../03-molecular/serotonin/README.md)** — Neuroinflammatory modulator: serotonin, via 5-HT receptors on microglia (already mapped) and oligodendrocytes (already mapped), modulates neuroinflammation and remyelination; serotonin dysregulation amplifies the IL-6 (already mapped) and NLRP3 (already mapped) cascade of multiple sclerosis.
- `connects-to` → **[Oxytocin](../../03-molecular/oxytocin/README.md)** — Anti-inflammatory remyelination: oxytocin, via OXTR on microglia (already mapped) and regulatory T cells (already mapped), attenuates neuroinflammation and promotes remyelination; oxytocin deficiency amplifies the IL-17a (already mapped) and IL-6 (already mapped) cascade of multiple sclerosis.
- `connects-to` → **[Vasopressin](../../03-molecular/vasopressin/README.md)** — BBB osmolality modulator: vasopressin, via V1aR on microglia (already mapped) and oligodendrocytes (already mapped), modulates BBB osmolality and neuroinflammation; vasopressin dysregulation amplifies NLRP3 (already mapped) and IL-6 (already mapped) cascade of multiple sclerosis.
- `connects-to` → **[Iodine](../../02-atomic/iodine/README.md)** — Thyroid-myelin axis: iodine-dependent thyroid hormones regulate oligodendrocyte (already mapped) differentiation and myelin synthesis; iodine deficiency amplifies the remyelination failure and IL-6 (already mapped) neuroinflammatory cascade of multiple sclerosis.
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — Glutamate-excitotoxicity brake: magnesium, via NMDA-receptor (already mapped) blockade on oligodendrocytes (already mapped), reduces glutamate-driven excitotoxicity; magnesium deficiency amplifies the NLRP3 (already mapped) and IL-17a (already mapped) cascade of multiple sclerosis.
- `connects-to` → **[Copper](../../02-atomic/copper/README.md)** — Myelin-synthesis cofactor: copper, as cofactor of cytochrome-c oxidase in oligodendrocytes (already mapped) and superoxide dismutase (already mapped), is essential for myelin synthesis; copper deficiency recapitulates the demyelinating cascade of multiple sclerosis.
- `connects-to` → **[Zinc](../../02-atomic/zinc/README.md)** — MS zinc: zinc cofactors NRF2 (already mapped) antioxidant defence in oligodendrocytes (already mapped); zinc deficiency amplifies NF-κB (already mapped) and IL-17a (already mapped) and NLRP3 (already mapped) neuroinflammation and demyelinating cascade in multiple sclerosis.
- `connects-to` → **[Phosphorus](../../02-atomic/phosphorus/README.md)** — MS phosphorus: phosphorus fuels oligodendrocyte (already mapped) ATP and myelin biosynthesis; phosphorus deficiency impairs remyelination and amplifies NF-κB (already mapped) and microglia (already mapped)-driven neuroinflammation in multiple sclerosis.
- `connects-to` → **[Chloride](../../02-atomic/chloride/README.md)** — MS chloride: chloride channels regulate macrophage (already mapped) and mast-cell (already mapped) ion homeostasis in the CNS; chloride imbalance amplifies NF-κB (already mapped) and IL-6 (already mapped) neuroinflammatory cascade of multiple sclerosis.
- `connects-to` → **[Sulfur](../../02-atomic/sulfur/README.md)** — MS sulfur: sulfur-containing amino acids in microglia (already mapped) and macrophages (already mapped) sustain CNS redox buffering; sulfur depletion amplifies NF-κB (already mapped) and IL-6 (already mapped) demyelinating cascade of multiple sclerosis.
- `connects-to` → **[Carbon](../../02-atomic/carbon/README.md)** — MS carbon: carbon as backbone of myelin basic protein and NF-κB (already mapped) structural proteins in oligodendrocytes (already mapped) sustains remyelination; carbon depletion amplifies NF-κB (already mapped) and IL-6 (already mapped) cascade of multiple sclerosis.
- `connects-to` → **[Hydrogen](../../02-atomic/hydrogen/README.md)** — MS hydrogen: hydrogen, via water and redox homeostasis in microglia (already mapped) and oligodendrocytes (already mapped), supports CNS remyelination; hydrogen dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) demyelinating cascade of multiple sclerosis.
- `connects-to` → **[Nitrogen](../../02-atomic/nitrogen/README.md)** — MS nitrogen: nitrogen in amino-acid scaffold of myelin proteins and NF-κB (already mapped) transcription factors modulates oligodendrocyte (already mapped) remyelination; nitrogen dysregulation amplifies IL-6 (already mapped) cascade of multiple sclerosis.
- `connects-to` → **[Oxygen](../../02-atomic/oxygen/README.md)** — MS oxygen: oxygen supports aerobic metabolism in oligodendrocytes (already mapped) and microglia (already mapped) for remyelination; oxygen deficit amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) demyelinating cascade of multiple sclerosis.
- `connects-to` → **[PD-1](../../03-molecular/pd-1/README.md)** — MS PD-1: PD-1 checkpoint on T-cells (already mapped) and microglia (already mapped) modulates CNS immune tolerance; PD-1 dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and TNF-α (already mapped) autoimmune demyelinating cascade of multiple sclerosis.
- `connects-to` → **[GLP-1](../../03-molecular/glp-1/README.md)** — MS GLP-1: GLP-1 signalling in neurons (already mapped) and microglia (already mapped) promotes neuroprotection and oligodendrocyte (already mapped) survival; GLP-1 deficit amplifies NF-κB (already mapped) and IL-6 (already mapped) demyelinating cascade of multiple sclerosis.
- `connects-to` → **[Angiotensin-II](../../03-molecular/angiotensin-ii/README.md)** — MS angiotensin-ii: angiotensin-II from astrocytes (already mapped) and macrophages (already mapped) drives vascular neuroinflammation; angiotensin-ii excess amplifies nf-kb (already mapped) and il-6 (already mapped) and tnf-alpha (already mapped) demyelinating cascade of MS.
- `connects-to` → **[WNT-β-catenin](../../03-molecular/wnt-beta-catenin/README.md)** — MS wnt-beta-catenin: WNT/β-catenin on neurons (already mapped) and astrocytes (already mapped) regulates oligodendrocyte survival; wnt-beta-catenin dysregulation amplifies nf-kb (already mapped) and il-6 (already mapped) and tnf-alpha (already mapped) MS cascade.
- `connects-to` → **[RANKL](../../03-molecular/rankl/README.md)** — MS rankl: RANKL from microglia (already mapped) and astrocytes (already mapped) promotes CNS neuroinflammation; rankl excess amplifies nf-kb (already mapped) and il-6 (already mapped) and tnf-alpha (already mapped) demyelinating cascade of MS.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — MS vegf: VEGF from microglia (already mapped) and astrocytes (already mapped) promotes neuroinflammatory angiogenesis; vegf excess amplifies nf-kb (already mapped) and il-6 (already mapped) and tnf-alpha (already mapped) demyelinating cascade of MS.
- `connects-to` → **[Fibronectin](../../03-molecular/fibronectin/README.md)** — MS fibronectin: fibronectin in microglia (already mapped) and astrocytes (already mapped) promotes CNS ECM remodelling; fibronectin excess amplifies nf-kb (already mapped) and il-6 (already mapped) and tnf-alpha (already mapped) demyelinating cascade of MS.
- `connects-to` → **[Notch](../../03-molecular/notch/README.md)** — MS notch: Notch signalling on microglia (already mapped) and astrocytes (already mapped) regulates oligodendrocyte fate; notch dysregulation amplifies nf-kb (already mapped) and il-6 (already mapped) and tnf-alpha (already mapped) demyelinating cascade of MS.
- `connects-to` → **[Activin-A](../../03-molecular/activin-a/README.md)** — MS activin-a: activin-A from microglia (already mapped) and astrocytes (already mapped) promotes CNS fibrotic remodelling; activin-a excess amplifies nf-kb (already mapped) and il-6 (already mapped) and tnf-alpha (already mapped) demyelinating cascade of MS.
- `connects-to` → **[CGRP](../../03-molecular/cgrp/README.md)** — MS cgrp: CGRP from microglia (already mapped) and astrocytes (already mapped) modulates CNS neuroimmune tone; cgrp excess amplifies nf-kb (already mapped) and il-6 (already mapped) and tnf-alpha (already mapped) demyelinating cascade of MS.
- `connects-to` → **[Calcitonin](../../03-molecular/calcitonin/README.md)** — MS calcitonin: calcitonin from microglia (already mapped) and astrocytes (already mapped) modulates CNS calcium balance; calcitonin excess amplifies nf-kb (already mapped) and il-6 (already mapped) and tnf-alpha (already mapped) demyelinating cascade of MS.
- `connects-to` → **[Substance-P](../../03-molecular/substance-p/README.md)** — MS substance-p: substance-P from microglia (already mapped) and astrocytes (already mapped) modulates CNS pain tone; substance-p excess amplifies nf-kb (already mapped) and il-6 (already mapped) and tnf-alpha (already mapped) demyelinating cascade of MS.
- `connects-to` → **[Insulin receptor](../../03-molecular/insulin-receptor/README.md)** — MS insulin-receptor: insulin receptor on microglia (already mapped) and astrocytes (already mapped) drives CNS metabolic repair; insulin-receptor loss amplifies nf-kb (already mapped) and il-6 (already mapped) and tnf-alpha (already mapped) demyelinating cascade of MS.
- `connects-to` → **[Aldosterone](../../03-molecular/aldosterone/README.md)** — MS aldosterone: aldosterone from microglia (already mapped) and astrocytes (already mapped) modulates CNS ion balance; aldosterone excess amplifies nf-kb (already mapped) and il-6 (already mapped) and tnf-alpha (already mapped) demyelinating cascade of MS.

[^compston-2008-ms-review]: Compston A, Coles A. Multiple sclerosis. *Lancet.* 2008;372(9648):1502-1517. [doi:10.1016/S0140-6736(08)61620-7](https://doi.org/10.1016/S0140-6736(08)61620-7) · [PubMed 18970977](https://pubmed.ncbi.nlm.nih.gov/18970977/)
[^kappos-2006-natalizumab]: Polman CH, O'Connor PW, Havrdova E, et al. A randomized, placebo-controlled trial of natalizumab for relapsing multiple sclerosis. *N Engl J Med.* 2006;354(9):899-910. [doi:10.1056/NEJMoa044397](https://doi.org/10.1056/NEJMoa044397) · [PubMed 16510744](https://pubmed.ncbi.nlm.nih.gov/16510744/)
[^montalban-2017-ocrelizumab-ppms]: Montalban X, Hauser SL, Kappos L, et al. Ocrelizumab versus Placebo in Primary Progressive Multiple Sclerosis. *N Engl J Med.* 2017;376(3):209-220. [doi:10.1056/NEJMoa1606468](https://doi.org/10.1056/NEJMoa1606468) · [PubMed 28002688](https://pubmed.ncbi.nlm.nih.gov/28002688/)
