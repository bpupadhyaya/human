---
schema: human-scale-entry/v1
id: nmo
name: NMOSD
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-07
summary: "NMOSD: AQP4-IgG+ (85%) or MOG-IgG+ attacks on optic nerves, spinal cord, and brainstem (area postrema); relapsing; high morbidity. Eculizumab (PREVENT; FDA Jun 2019), inebilizumab (N-MOmentum; FDA Jun 2020), satralizumab (SAkuraStar; FDA Aug 2020) approved."
aliases: ["NMOSD", "neuromyelitis optica spectrum disorder", "NMO", "Devic's disease", "neuromyelitis optica", "AQP4-IgG neuropathy", "anti-AQP4 disease", "MOG-IgG disease"]
sources:
  - id: wingerchuk-2015-nmosd-criteria
    type: peer-reviewed
    cite: "Wingerchuk DM, Banwell B, Bennett JL, et al. International consensus diagnostic criteria for neuromyelitis optica spectrum disorders. Neurology. 2015;85(2):177-189."
    doi: "10.1212/WNL.0000000000001729"
    pmid: "26092914"
    url: "https://doi.org/10.1212/WNL.0000000000001729"
  - id: pittock-2019-eculizumab-prevent
    type: peer-reviewed
    cite: "Pittock SJ, Berthele A, Fujihara K, et al. Eculizumab in Aquaporin-4-Positive Neuromyelitis Optica Spectrum Disorder. N Engl J Med. 2019;381(7):614-625."
    doi: "10.1056/NEJMoa1900866"
    pmid: "31050279"
    url: "https://doi.org/10.1056/NEJMoa1900866"
  - id: cree-2019-inebilizumab-nmomentum
    type: peer-reviewed
    cite: "Cree BAC, Bennett JL, Kim HJ, et al. Inebilizumab for the treatment of neuromyelitis optica spectrum disorder (N-MOmentum). Lancet. 2019;394(10206):1352-1363."
    doi: "10.1016/S0140-6736(19)31817-3"
    pmid: "31495497"
    url: "https://doi.org/10.1016/S0140-6736(19)31817-3"
  - id: yamamura-2020-satralizumab-sakurastar
    type: peer-reviewed
    cite: "Yamamura T, Kleiter I, Fujihara K, et al. Trial of Satralizumab in Neuromyelitis Optica Spectrum Disorder. N Engl J Med. 2019;381(22):2114-2124."
    doi: "10.1056/NEJMoa1901747"
    pmid: "31774951"
    url: "https://doi.org/10.1056/NEJMoa1901747"
cross_links:
  - target: 01-human/03-molecular/aquaporin-4
    relation: connects-to
    note: "AQP4-IgG binds AQP4 on astrocyte endfeet → classical complement → MAC (C5b-9) → astrocyte lysis → secondary demyelination; pathognomonic in ~85% of NMOSD; ELISA and cell-based assays detect AQP4-IgG; titer correlates with disease activity."
  - target: 01-human/03-molecular/complement-c5
    relation: connects-to
    note: "Eculizumab (anti-C5; PREVENT: ARR 0.02 vs 0.35; FDA Jun 2019) and ravulizumab (CHAMPION-NMOSD; FDA Jun 2023) block C5 → prevent MAC formation on astrocytes → halt AQP4-IgG-driven attacks; effective only in AQP4-IgG+ NMOSD, not MOG-IgG+."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "Satralizumab (anti-IL-6R; FDA Aug 2020) reduced ARR ~55% vs placebo (SAkuraStar monotherapy); IL-6 promotes plasmablast expansion → AQP4-IgG production; IL-6 also amplifies Th17 responses; tocilizumab (anti-IL-6R) is used off-label."
  - target: 01-human/03-molecular/cd20
    relation: connects-to
    note: "Rituximab (anti-CD20) depletes B cells → reduces AQP4-IgG; widely used off-label as first-line NMOSD prevention (~70-80% ARR reduction); inebilizumab (anti-CD19; N-MOmentum: 88% vs 63% attack-free; FDA Jun 2020) also approved for NMOSD."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "IFN-β is CONTRAINDICATED in AQP4-IgG+ NMOSD — clinical trials showed IFN-β increases attack frequency; IFN-β may promote plasmablast differentiation → higher AQP4-IgG; this differentiates NMOSD from MS (where IFN-β is first-line)."
  - target: 01-human/04-cellular/astrocyte
    relation: connects-to
    note: "NMOSD is an astrocytopathy: AQP4-IgG binds the aquaporin-4 channels clustered on astrocyte endfeet → classical complement → membrane-attack complex → astrocyte lysis, and only then does secondary demyelination follow — unlike multiple sclerosis, where myelin is hit first."
  - target: 01-human/07-system/multiple-sclerosis
    relation: connects-to
    note: "NMOSD was long mistaken for multiple sclerosis until AQP4-IgG split them apart; NMOSD brings more severe, longitudinally extensive cord lesions and complete optic neuritis, lacks CSF oligoclonal bands, and crucially is worsened by the interferon-β and natalizumab that treat MS."
  - target: 01-human/06-organ/eye
    relation: connects-to
    note: "Optic neuritis is a defining NMOSD attack and is far more destructive than in MS: patients lose vision often to light-perception or worse, recover poorly, and show severe retinal nerve fiber layer thinning on OCT; bilateral or chiasmal involvement favours NMOSD over MS."
  - target: 01-human/07-system/west-nile-virus
    relation: connects-to
    note: "NMOSD and West Nile virus both attack the cord to cause myelitis but by opposite routes: NMOSD is autoimmune AQP4-IgG complement attack on astrocytes, while WNV is a neurotropic flavivirus infecting anterior-horn neurons → acute flaccid paralysis."
  - target: 01-human/04-cellular/b-cell
    relation: connects-to
    note: "NMOSD is antibody-driven: CD19+ plasmablasts produce the pathogenic AQP4-IgG and IL-6 sustains them; this B-cell dependence is why anti-CD20 (rituximab) and anti-CD19 (inebilizumab) deplete B cells and anti-IL-6R (satralizumab) work, while T-cell-directed MS drugs fail."
  - target: 01-human/07-system/sjogrens-syndrome
    relation: connects-to
    note: "NMOSD frequently coexists with systemic autoimmunity, especially Sjögren's and lupus: AQP4-IgG-positive patients often carry anti-Ro/SSA, anti-La or ANA, and the myelitis/optic neuritis is the neurological face of NMOSD, not a direct effect of the connective-tissue disease."
  - target: 01-human/07-system/systemic-lupus-erythematosus
    relation: connects-to
    note: "When neuromyelitis optica coexists with lupus, the myelitis is NMO, not CNS lupus: AQP4-IgG-positive NMO can occur alongside SLE, so transverse myelitis or optic neuritis in a lupus patient should prompt AQP4 testing rather than assuming neuropsychiatric lupus."
  - target: 01-human/07-system/myasthenia-gravis
    relation: connects-to
    note: "Neuromyelitis optica and myasthenia gravis are antibody-mediated diseases that co-occur more than by chance: both are driven by pathogenic IgG (anti-AQP4 vs anti-AChR) and a tendency to further autoimmunity, and NMO can emerge after thymectomy for myasthenia."
  - target: 01-human/04-cellular/plasma-cell
    relation: connects-to
    note: "Plasma cells make the pathogenic antibody of neuromyelitis optica: long-lived plasma cells and plasmablasts secrete anti-aquaporin-4 IgG that, with complement, destroys astrocytes—so therapy targets the B-cell/plasma-cell axis (rituximab, satralizumab, eculizumab)."
  - target: 01-human/05-tissue/guillain-barre
    relation: connects-to
    note: "NMO and Guillain-Barré are both antibody-mediated demyelinating diseases but of different compartments: NMO's anti-aquaporin-4 antibodies attack CNS astrocytes, while GBS antibodies attack peripheral nerve myelin—central versus peripheral autoimmune demyelination."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Complement drives the astrocyte destruction of NMO: anti-aquaporin-4 antibodies bound to astrocytes activate the complement cascade, whose membrane attack complex lyses them—so complement inhibitors are now NMO therapy, treating the disease at its effector step."
  - target: 01-human/04-cellular/oligodendrocyte
    relation: connects-to
    note: "NMO and MS are distinguished by their cellular target: MS attacks oligodendrocytes and myelin, while NMO attacks astrocytes via aquaporin-4—so NMO is an astrocytopathy, not a demyelinating disease per se, and MS drugs can worsen it, making the distinction critical."
  - target: 01-human/03-molecular/immunoglobulin-g
    relation: connects-to
    note: "NMO is defined by a pathogenic IgG autoantibody: AQP4-IgG binds astrocyte water channels and fixes complement, so this IgG is both the diagnostic test and the direct cause of the astrocyte destruction—distinguishing NMO from multiple sclerosis."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "T helper cells drive the NMO attack: Th17 cells and the IL-6 they help sustain promote AQP4-specific antibody production and open the blood-brain barrier, so the antibody response depends on T-cell help—rationale for IL-6-pathway therapy."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "NMO is a systemic autoimmune disease that strikes the CNS: it clusters with lupus and Sjogren's, reflecting broad loss of self-tolerance, and is controlled by immunosuppression and B-cell depletion rather than the immunomodulators used in MS."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "NMO is not just an eye-and-cord disease—it strikes the brain: lesions in the area postrema cause intractable hiccups, nausea, and vomiting, and diencephalic or brainstem attacks add narcolepsy or other signs, so AQP4-rich brain regions are characteristic NMO targets."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: connects-to
    note: "NMO reflects a breakdown of immune tolerance: regulatory T cells that should restrain self-reactivity are deficient or dysfunctional, allowing AQP4-specific T and B cells to mature—so failed Treg control underlies the autoimmunity against astrocyte water channels."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "Natural killer cells help execute NMO's astrocyte damage: once anti-AQP4 antibodies coat astrocytes, NK cells (and complement) destroy them by antibody-dependent cytotoxicity, so innate effectors translate the autoantibody into the actual tissue injury."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "Neutrophils mark NMO lesions, unlike MS: the antibody-and-complement attack on astrocytes draws in neutrophils and eosinophils, so the inflammatory infiltrate and CSF granulocytes help distinguish neuromyelitis optica from multiple sclerosis."
  - target: 01-human/03-molecular/glutamate
    relation: connects-to
    note: "NMO unleashes glutamate excitotoxicity: anti-AQP4 antibodies kill astrocytes whose glutamate transporters normally clear the synapse, so glutamate floods and poisons oligodendrocytes and neurons—why astrocyte loss cascades into demyelination."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "NMO is treated by blocking IL-6 signaling through JAK: satralizumab targets the IL-6 receptor whose JAK-STAT signal drives the AQP4-antibody-producing plasmablasts, one of several approved therapies that have transformed NMO prognosis."
  - target: 01-human/03-molecular/fcrn
    relation: connects-to
    note: "NMO is driven by pathogenic IgG that FcRn keeps alive: the anti-AQP4 antibody attacks astrocytes, and because FcRn recycles IgG to prolong its life, blocking FcRn (efgartigimod) is a strategy to clear the harmful antibody."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "NMO recruits Th17 and IL-17 to breach the brain barrier: IL-17 helps open the blood-brain barrier and inflame lesions, letting anti-AQP4 antibody reach astrocytes—part of why IL-6 blockade (which curbs Th17) prevents relapses."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "NMO lesions are finished off by macrophages: after anti-AQP4 antibody and complement attack astrocytes, macrophages clear the debris and demyelinate, producing the destructive, longitudinally extensive cord and optic-nerve lesions."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "NMO kills cells through calcium: when astrocytes die and can no longer clear glutamate, the flood overexcites neurons and oligodendrocytes, opening channels that let lethal calcium pour in—the excitotoxicity behind the tissue destruction."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "NMO ultimately destroys neurons: though astrocytes are the first target, the complement-driven inflammatory attack severs axons and kills neurons in the cord and optic nerve, causing the lasting paralysis and blindness of relapses."
  - target: 01-human/05-tissue/synapse
    relation: connects-to
    note: "NMO poisons the synapse by silencing astrocytes: these cells normally clear glutamate from synapses through transporters tied to aquaporin-4, so destroying them lets glutamate linger and excitotoxically damage the surrounding tissue."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "NMO is mapped by MRI: its hallmark is a long spinal-cord lesion spanning three or more segments, plus optic-nerve enhancement, all read in the photons of magnetic-resonance imaging."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "NMO lesions in the brain's area postrema and hypothalamus can derange sodium balance, causing SIADH and low blood sodium alongside the intractable vomiting and hiccups that flag the disease."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "NMO breaches the blood-brain barrier where astrocyte foot processes meet endothelial cells: the antibody and complement attack on this interface opens the door for the wider immune assault on the cord."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy distinguishes NMO from MS at the lesion: it is the astrocyte that dies first — its foot processes stripped of aquaporin-4 and coated with complement — rather than the myelin, a primary astrocytopathy unlike MS demyelination."
  - target: 01-human/06-organ/stomach
    relation: connects-to
    note: "NMO can present from the stomach's control center: lesions in the area postrema of the brainstem trigger intractable hiccups, nausea, and vomiting — a characteristic syndrome that often heralds the disease before the cord or optic nerve is hit."
  - target: 01-human/02-atomic/potassium
    relation: connects-to
    note: "Destroying aquaporin-4 unsettles potassium balance: the water channel sits beside the astrocyte channels that mop up potassium released by firing neurons, so the NMO attack disrupts the ion buffering that keeps the cord's neurons stable."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "NMO turns on a single self-protein: the AQP4-IgG autoantibody is both its cause and its diagnostic hallmark, distinguishing it from MS, and the related MOG antibody defines a separate but overlapping demyelinating disease."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "A high cord attack can stop the breath: NMO's longitudinally extensive myelitis or brainstem lesions can knock out the nerves driving the diaphragm, causing neurogenic respiratory failure that is a leading cause of death."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "A puzzle of where the channel lives: aquaporin-4 is abundant in the kidney's collecting ducts and the stomach too, yet NMO spares them and strikes the CNS — a selectivity set by how the blood-brain barrier and complement expose the target."
  - target: 01-human/06-organ/large-intestine
    relation: connects-to
    note: "Cord lesions sever the bowel's controls: NMO's transverse myelitis disrupts the spinal pathways to the rectum and bladder, leaving neurogenic bowel and bladder dysfunction — constipation, incontinence, and retention — among its lasting disabilities."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "Pregnancy can stir NMO, unlike MS: relapse risk rises in the months after delivery, and active disease threatens the pregnancy, so timing conception and choosing pregnancy-safe immunotherapy are central to managing affected women."
  - target: 01-human/05-tissue/hippocampus
    relation: connects-to
    note: "NMO can reach the memory circuits: aquaporin-4 is dense in the hippocampus, and some patients develop cognitive impairment and limbic lesions, widening the disease beyond the optic nerve and spinal cord it is named for."
  - target: 01-human/04-cellular/microglia
    relation: connects-to
    note: "When astrocytes die, microglia take over the damage: AQP4-antibody attack strips away astrocytes, and the reactive microglia that move in pour out inflammatory mediators that injure neurons and oligodendrocytes in the secondary wave of an NMO lesion."
  - target: 01-human/03-molecular/baff
    relation: connects-to
    note: "NMO is a B-cell disease fed by BAFF: this survival cytokine keeps alive the plasmablasts that pump out aquaporin-4 antibody, so high BAFF marks active disease and B-cell-targeted therapy is a mainstay."
  - target: 01-human/07-system/rheumatoid-arthritis
    relation: connects-to
    note: "NMO travels with systemic autoimmunity: patients carry higher rates of coexisting diseases like rheumatoid arthritis, reflecting a shared autoimmune diathesis and overlapping B-cell- and IL-6-targeted treatments."
  - target: 01-human/07-system/neuropathic-pain
    relation: connects-to
    note: "Its myelitis leaves searing pain: damage to the spinal cord in NMO causes severe neuropathic pain and painful tonic spasms that often persist between attacks, a leading driver of disability between relapses."
  - target: 01-human/07-system/epilepsy
    relation: connects-to
    note: "When it reaches the brain it can spark seizures: although NMO favors the optic nerves and cord, cerebral lesions — common in AQP4-rich regions and in pediatric disease — can irritate the cortex and provoke epilepsy."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "The autoimmune attack must first be taught: dendritic cells present aquaporin-4 peptides to T cells, licensing the helper response that drives B cells to make the pathogenic anti-AQP4 antibody."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "The antibody attack inflames through NF-κB: AQP4-IgG binding and complement on astrocytes drive NF-κB-dependent cytokine and chemokine release, amplifying the neutrophil-rich inflammation that destroys tissue in an NMO lesion."
  - target: 01-human/07-system/sepsis
    relation: connects-to
    note: "Complement-blocking therapy opens a dangerous door: eculizumab, used to prevent NMO relapses, blocks the membrane attack complex and sharply raises the risk of meningococcal and other encapsulated-organism infection and sepsis, mandating vaccination."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "Paralyzing attacks bring clot risk: a severe transverse myelitis relapse can leave a patient immobile for weeks, and the resulting venous stasis raises the risk of deep-vein thrombosis and pulmonary embolism."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "Relapsing disability weighs on mood: the unpredictable attacks of blindness and paralysis, chronic pain, and the lifelong threat of relapse give NMO a heavy psychological burden with high rates of depression."
  - target: 02-pathogen/03-fungi/pneumocystis-jirovecii
    relation: connects-to
    note: "Its B-cell-depleting therapy opens the lung: rituximab and the chronic immunosuppression used to prevent NMO relapses can drop T-cell defenses enough to risk Pneumocystis pneumonia, sometimes warranting prophylaxis."
  - target: 01-human/07-system/osteoporosis
    relation: connects-to
    note: "Steroids and immobility thin the bone: the repeated high-dose corticosteroids for NMO attacks, plus reduced mobility from myelitis, accelerate bone loss and raise the risk of osteoporotic fracture."
  - target: 01-human/07-system/wound-healing
    relation: connects-to
    note: "Paralysis from myelitis breaks down the skin: severe transverse myelitis in NMO can leave patients immobile and insensate, predisposing to pressure ulcers that are slow to heal over bony prominences."
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "A neurogenic bladder threatens the kidneys: spinal-cord attacks in NMO impair bladder control, and the recurrent urinary infections and back-pressure that follow can progress to chronic kidney disease."
  - target: 02-pathogen/03-fungi/aspergillus-fumigatus
    relation: connects-to
    note: "Its potent immunotherapy opens the lung to mold: rituximab and other B-cell-depleting and immunosuppressive treatments for NMO can permit invasive Aspergillus infection."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "It is an antibody attack on the CNS: NMO targets aquaporin-4 on astrocytes, causing optic neuritis and longitudinally extensive transverse myelitis that blind and paralyse, a defining nervous-system autoimmune disease."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "High cord attacks can stop breathing: an NMO lesion in the cervical spinal cord or brainstem can paralyse the diaphragm and respiratory drive, causing neurogenic respiratory failure."
  - target: 02-pathogen/02-bacteria/neisseria-meningitidis
    relation: connects-to
    note: "Its complement-blocking drug invites meningococcus: eculizumab, used to prevent NMO relapses, blocks the terminal complement that defends against Neisseria meningitidis, so vaccination is mandatory before treatment."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "It announces itself through the gut: area postrema syndrome — intractable hiccups, nausea and vomiting from a medullary lesion — is a classic and often first manifestation of NMO."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "It targets the hypothalamus: AQP4-rich diencephalic regions are vulnerable, so NMO can cause SIADH, narcolepsy, hypothermia and other endocrine disturbances from hypothalamic lesions."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "Severe myelitis disables the limbs: longitudinally extensive transverse myelitis causes paralysis with spasticity and contractures, while long-term corticosteroids add bone and muscle complications."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "High cord lesions destabilise the circulation: cervical transverse myelitis can cause autonomic dysreflexia with dangerous blood-pressure swings and arrhythmia."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "Its therapies and overlaps touch the skin: immunosuppression with rituximab, eculizumab and steroids brings skin and infection problems, and NMO overlaps autoimmune connective-tissue skin disease."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "Overlap autoimmunity and drugs strain the kidney: NMO coexists with systemic lupus that can cause nephritis, and its long-term immunosuppression requires renal monitoring."
  - target: 03-medicine/01-modern/13-cancer/targeted-therapy
    relation: connects-to
    note: "Monoclonal antibodies transformed its care: eculizumab (anti-C5), satralizumab (anti-IL-6R) and inebilizumab (anti-CD19) prevent the relapses of AQP4-antibody neuromyelitis optica."
  - target: 03-medicine/01-modern/02-respiratory/corticosteroids
    relation: connects-to
    note: "High-dose steroids treat the attack: intravenous corticosteroids, with plasma exchange, are first-line for acute optic neuritis and transverse myelitis relapses in NMO."
  - target: 02-pathogen/01-viruses/epstein-barr-virus
    relation: connects-to
    note: "Viruses may help trigger it: like other CNS autoimmunity, neuromyelitis optica has been linked to prior Epstein-Barr virus infection shaping the aberrant antibody response."
  - target: 03-medicine/01-modern/13-cancer/cancer-chemotherapy
    relation: connects-to
    note: "Cytotoxic immunosuppression and a cancer link: azathioprine, mycophenolate and cyclophosphamide serve as steroid-sparing maintenance in NMO, and a minority of AQP4-positive disease is paraneoplastic, declaring an underlying cancer."
  - target: 03-medicine/01-modern/13-cancer/checkpoint-inhibitors
    relation: connects-to
    note: "Immunotherapy can unmask it: cancer checkpoint inhibitors occasionally trigger AQP4-antibody neuromyelitis optica and other CNS demyelinating syndromes as severe immune-related adverse events."
  - target: 01-human/05-tissue/axonal-transport
    relation: connects-to
    note: "Astrocyte attack severs axons: although NMO primarily destroys aquaporin-4-bearing astrocytes, the resulting lesions disrupt axonal transport and cause the secondary axonal loss behind permanent optic and spinal-cord disability."
  - target: 01-human/07-system/pemphigus-vulgaris
    relation: connects-to
    note: "Antibody-and-complement disease in common: like pemphigus vulgaris, neuromyelitis optica is driven by pathogenic IgG and complement and responds to B-cell depletion (rituximab, inebilizumab)—autoimmunity striking the CNS rather than the skin."
  - target: 01-human/07-system/breast-cancer
    relation: connects-to
    note: "It can be paraneoplastic: aquaporin-4 neuromyelitis optica is occasionally a paraneoplastic syndrome, reported with breast and lung cancers, so new NMO in an older adult may prompt a malignancy search."
  - target: 01-human/07-system/immune-thrombocytopenia
    relation: connects-to
    note: "Antibody-mediated autoimmunity that can coexist: like immune thrombocytopenia, NMO is an organ-specific autoantibody disease cleared by B-cell depletion, and the two can occur together in autoimmune-prone patients."
  - target: 01-human/05-tissue/germinal-center
    relation: connects-to
    note: "Where the autoantibody is made: AQP4-IgG in neuromyelitis optica is produced by plasmablasts from germinal-centre B-cell responses, the target of B-cell-depleting and IL-6 (Tfh) therapies like rituximab and satralizumab."
  - target: 01-human/07-system/antiphospholipid-syndrome
    relation: connects-to
    note: "Clustering autoimmunity: neuromyelitis optica frequently coexists with systemic autoimmune diseases including antiphospholipid syndrome and lupus, reflecting a shared predisposition to pathogenic autoantibody production."
  - target: 01-human/07-system/sclc
    relation: connects-to
    note: "A paraneoplastic trigger: AQP4-antibody NMO is occasionally paraneoplastic, reported with cancers including small-cell lung cancer, so a new diagnosis in an older smoker can prompt a tumour search."
  - target: 01-human/07-system/covid-19-disease
    relation: connects-to
    note: "An infectious trigger: NMOSD attacks have been reported after SARS-CoV-2 infection and, rarely, vaccination, fitting the pattern of immune activation precipitating relapses of this antibody-mediated disease."
  - target: 01-human/07-system/type-1-diabetes
    relation: connects-to
    note: "Autoimmune clustering: NMOSD frequently coexists with other organ-specific autoimmune diseases such as type 1 diabetes, thyroiditis and myasthenia, reflecting a shared predisposition to autoimmunity."
  - target: 01-human/07-system/narcolepsy
    relation: connects-to
    note: "Diencephalic syndrome: AQP4-rich hypothalamic lesions in NMO can cause symptomatic narcolepsy and hypersomnia along with SIADH, the antibody attacking the same brain regions that govern sleep and water balance."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Th1 cytokine: IFN-γ from pathogenic T-helper cells amplifies the inflammatory, complement-fixing environment that drives the astrocyte destruction of NMO lesions."
  - target: 01-human/03-molecular/perforin
    relation: connects-to
    note: "Cytotoxic killing: AQP4-IgG recruits NK cells and CD8 T cells whose perforin-mediated antibody-dependent cellular cytotoxicity adds to complement in destroying astrocytes."
  - target: 01-human/03-molecular/nlrp3-inflammasome
    relation: connects-to
    note: "Glial inflammasome: NLRP3-inflammasome activation in microglia and macrophages within NMO lesions amplifies IL-1β-driven neuroinflammation and tissue damage."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Eosinophilic lesions: IL-5 recruits eosinophils, whose granule proteins are a distinctive feature of NMO lesions, adding eosinophil-mediated astrocyte injury that helps distinguish NMO from multiple sclerosis."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "Th17/Treg imbalance: a TGF-beta- and IL-6-shaped shift away from regulatory T cells toward pathogenic Th17 responses helps license the AQP4-reactive autoimmunity that drives NMO."
  - target: 01-human/03-molecular/mhc-class-ii
    relation: connects-to
    note: "Autoantigen presentation: MHC class II presentation of aquaporin-4 peptides primes the CD4 helper T cells that provide help for the pathogenic AQP4-IgG response in NMO."
  - target: 01-human/03-molecular/ccl2
    relation: connects-to
    note: "Monocyte recruitment: CCL2 draws monocytes and macrophages into the AQP4-targeted astrocytic lesions of NMO, amplifying the inflammatory injury beyond the initial complement-mediated astrocyte destruction."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "Granulocytic inflammation: IL-1β released by activated myeloid cells and the inflammasome recruits the neutrophils and eosinophils that give NMO lesions their characteristic granulocyte-rich pathology, distinct from MS."
  - target: 01-human/03-molecular/tnf-alpha
    relation: connects-to
    note: "Astrocyte injury amplifier: TNF-α from activated microglia and macrophages compounds the astrocyte and oligodendrocyte damage in NMO lesions, contributing to the severe, often necrotic tissue destruction of the disease."
  - target: 01-human/03-molecular/c5ar1
    relation: connects-to
    note: "Anaphylatoxin recruitment: complement activation on AQP4-bound astrocytes generates C5a, which through C5aR1 recruits the neutrophils and eosinophils that inflict the necrotic tissue damage of NMO lesions — downstream of the C5 blockade achieved by eculizumab."
  - target: 01-human/03-molecular/connexin43
    relation: connects-to
    note: "Astrocyte uncoupling: AQP4 and connexin-43 are co-concentrated at astrocyte endfeet, so the AQP4-targeted attack disrupts connexin-43 gap-junction coupling between astrocytes, helping the lesion spread along the astroglial network of the spinal cord and optic nerve."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "Barrier breakdown: VEGF released from injured astrocytes increases blood-brain-barrier permeability in NMO, letting more pathogenic anti-AQP4 antibody and complement reach the CNS and amplifying the lesion."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "IL-6 effector: IL-6 signalling (already mapped, the target of satralizumab) acts through STAT3 to drive the pathogenic plasmablasts and Th17 cells that produce the AQP4-IgG of neuromyelitis optica."
  - target: 01-human/03-molecular/caspase-3
    relation: connects-to
    note: "Astrocyte death: complement- and antibody-mediated astrocyte injury in NMO triggers caspase-3 apoptosis of astrocytes and bystander neurons, the cell death underlying its destructive optic-nerve and spinal-cord lesions."
  - target: 01-human/03-molecular/bdnf
    relation: connects-to
    note: "Lost trophic support: AQP4-IgG-mediated astrocyte injury strips the BDNF and other trophic factors that astrocytes normally supply, contributing to the neuronal and oligodendrocyte damage of NMO lesions."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17 maintenance: IL-23 sustains the pathogenic Th17 cells whose IL-17A (mapped) helps disrupt the blood-brain barrier and recruit neutrophils to the AQP4-targeted lesions of NMO."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "Eosinophilic component: IL-13, with the IL-5 already mapped, recruits the eosinophils that are a characteristic feature of the inflammatory infiltrate in NMO lesions."
  - target: 01-human/03-molecular/ctla-4
    relation: connects-to
    note: "Tolerance breakdown: loss of CTLA-4-dependent regulatory control underlies the anti-AQP4 autoantibody response, and checkpoint-inhibitor therapy can trigger NMO-like autoimmunity."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "BAFF-driven PI3K-AKT signalling (BAFF mapped) sustains the autoreactive B-cell/plasmablast pool that produces pathogenic AQP4-IgG in NMO."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "The mTOR-regulated metabolic program supports antibody-secreting plasmablast expansion in NMO and is an investigational therapeutic target."
  - target: 01-human/03-molecular/myd88
    relation: connects-to
    note: "TLR-MyD88 innate signalling amplifies the astrocytic and microglial inflammatory response that follows AQP4-IgG/complement attack in NMO."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Galectin-3 released by reactive astrocytes and microglia amplifies the neuroinflammation that follows the AQP4-IgG astrocytopathy of NMO."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "IFN-STAT1 signalling shapes the interferon-driven component of the immune response in the astrocyte-targeted inflammation of NMO."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "Cytosolic DNA released by astrocyte injury can engage cGAS-STING, contributing to the innate inflammatory amplification of NMO lesions."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "FOXO regulates the oxidative-stress and survival responses of the astrocytes targeted by AQP4-IgG in neuromyelitis optica."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "S100A8/A9 alarmins released by infiltrating granulocytes amplify the inflammatory tissue damage of the eosinophil- and neutrophil-rich lesions of neuromyelitis optica."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "ERK-MAPK signaling downstream of cytokine and complement stimuli contributes to the astrocyte and immune-cell activation of neuromyelitis optica."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "GSK-3β modulates the NF-κB-driven inflammatory and B-cell survival signaling of neuromyelitis optica."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "HIF-1α in the hypoxic, astrocyte-damaged CNS lesion contributes to the tissue injury of neuromyelitis optica."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "PI3K (PIK3CA)-AKT signaling (AKT already mapped) supports the survival of the autoreactive plasmablasts that produce anti-AQP4 antibodies in neuromyelitis optica."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC-family (LYN) kinase signaling downstream of the B-cell receptor participates in the autoreactive anti-AQP4 B-cell response of neuromyelitis optica."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Autophagy modulates the astrocyte and immune-cell responses relevant to neuromyelitis optica."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK-linked metabolic signaling participates in the astrocyte metabolic stress of neuromyelitis optica."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-driven leukocyte recruitment into the CNS contributes to the astrocyte and neural injury of neuromyelitis optica."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "DNMT3A-mediated DNA methylation participates in the epigenetic regulation of the autoreactive immune response of neuromyelitis optica."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "CXCL12-CXCR4 signaling participates in the leukocyte trafficking across the blood-brain barrier in neuromyelitis optica."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "IL-33 alarmin signaling participates in the astrocyte and neuroinflammatory responses of neuromyelitis optica."
  - target: 01-human/03-molecular/arid1a
    relation: connects-to
    note: "ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic regulation of the immune responses of neuromyelitis optica."
  - target: 01-human/03-molecular/calcineurin
    relation: connects-to
    note: "Calcineurin-NFAT signaling participates in the T-cell activation (T-follicular-helper-driven anti-AQP4 response) of neuromyelitis optica."
  - target: 01-human/02-atomic/potassium
    relation: connects-to
    note: "Astrocyte ion homeostasis: AQP4 water channels co-localise with the Kir4.1 potassium channel at astrocyte endfeet, so the anti-AQP4 attack of NMO disrupts both water and potassium buffering, contributing to the oedema and neuronal dysfunction of lesions."
  - target: 01-human/03-molecular/estrogen
    relation: connects-to
    note: "Female predominance: neuromyelitis optica shows a striking roughly ninefold female predominance with relapse patterns tied to pregnancy and the postpartum period, implicating estrogen and sex hormones in disease susceptibility."
  - target: 01-human/03-molecular/il-2
    relation: connects-to
    note: "T-cell expansion: IL-2-driven proliferation of the follicular helper T cells that provide help for anti-AQP4 antibody production sustains the autoreactive B-cell response, complementing the checkpoint and antigen-presentation controls already mapped."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "Th2 antibody help: IL-4 and type-2 T-cell help support the B-cell production of the pathogenic anti-AQP4 IgG (immunoglobulin G already mapped), part of the humoral response that drives the astrocyte-targeting autoimmunity of neuromyelitis optica."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "Regulatory balance: deficient IL-10-mediated regulatory B- and T-cell control contributes to the unchecked anti-AQP4 response in neuromyelitis optica, and restoring this regulatory arm is a goal of tolerising therapies."
  - target: 01-human/03-molecular/progesterone
    relation: connects-to
    note: "Pregnancy relapse pattern: falling progesterone and estrogen (already mapped) postpartum coincides with a rise in neuromyelitis optica attacks, implicating sex-hormone fluctuation in the timing of relapses in this female-predominant disease."
  - target: 01-human/03-molecular/nitric-oxide
    relation: connects-to
    note: "Excitotoxic injury: nitric oxide, generated in the inflamed lesion, contributes with glutamate excitotoxicity (already mapped) to the astrocyte and secondary neuronal injury of neuromyelitis optica after the antibody and complement attack."
  - target: 01-human/03-molecular/xanthine-oxidase
    relation: connects-to
    note: "Oxidative lesion injury: reactive oxygen species, to which xanthine oxidase contributes, amplify the tissue damage in the acute neuromyelitis optica lesion, adding oxidative stress to the complement-mediated (already mapped) astrocyte destruction."
  - target: 01-human/03-molecular/prostaglandins
    relation: connects-to
    note: "Inflammatory eicosanoids: prostaglandins from the acute inflammatory infiltrate (IL-6 and TNF already mapped) of the neuromyelitis optica lesion contribute to the inflammation and blood-brain-barrier disruption of an attack."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "Magnesium and excitotoxicity: magnesium blocks the NMDA receptor and buffers the glutamate (already mapped) excitotoxicity released when astrocytes (already mapped) are destroyed in the neuromyelitis optica lesion, a neuroprotective ion."
  - target: 03-medicine/03-food/vitamin-d
    relation: connects-to
    note: "Vitamin D and autoimmunity: low vitamin D status is associated with neuromyelitis optica and other autoimmune demyelinating disease, its immunomodulation of the T- and B-cell response (type-I interferon already mapped) influencing risk and activity."
  - target: 03-medicine/03-food/omega-3-fatty-acids
    relation: connects-to
    note: "Omega-3 and inflammation resolution: the omega-3 fatty acids give rise to specialised pro-resolving mediators that counter the inflammatory eicosanoids (prostaglandins already mapped), studied as an adjunct in autoimmune neuroinflammation such as neuromyelitis optica."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Adipokine and autoimmunity: leptin, elevated in neuromyelitis optica, promotes the Th17 (IL-17 already mapped) and autoreactive responses, linking the metabolic-inflammatory state to the disease activity."
  - target: 01-human/03-molecular/pd-1
    relation: connects-to
    note: "Checkpoint tolerance: the PD-1 checkpoint and the peripheral-tolerance mechanisms, when dysfunctional, permit the anti-AQP4 (already mapped) autoreactivity that drives neuromyelitis optica."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Counter-regulatory adipokine: adiponectin, the anti-inflammatory counterpart of leptin (already mapped), is part of the adipokine-immune crosstalk whose imbalance shapes the autoimmune neuroinflammation of neuromyelitis optica."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), is the pro-inflammatory adipokine of the adipokine-immune crosstalk of the autoimmune neuroinflammation of neuromyelitis optica."
  - target: 01-human/04-cellular/oligodendrocyte
    relation: connects-to
    note: "Secondary demyelination: the astrocyte (already mapped) destruction of NMO causes the secondary oligodendrocyte loss and demyelination, distinct from the primary oligodendrocyte demyelination of multiple sclerosis (already mapped)."
  - target: 01-human/07-system/systemic-lupus-erythematosus
    relation: connects-to
    note: "Autoimmune overlap: neuromyelitis optica co-occurs with systemic lupus erythematosus and Sjögren's, sharing the autoantibody and type-I interferon (already mapped) autoimmunity."
  - target: 01-human/07-system/systemic-sclerosis
    relation: connects-to
    note: "Connective-tissue overlap: neuromyelitis optica can co-occur with systemic sclerosis and the other connective-tissue diseases (systemic lupus already mapped), part of the shared autoantibody autoimmunity."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm complementing the Th17 (IL-17 and IL-23 already mapped) drive of the AQP4 (already mapped) autoimmunity of neuromyelitis optica."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Eosinophil/type-2 IgE: the IgE, with the type-2 cytokines (IL-4, IL-5 and IL-13 already mapped), reflects the eosinophil-rich type-2 dimension of the NMO lesions."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "Mast cells in lesions: the mast cells, with the eosinophils (IL-5 already mapped), infiltrate the perivascular NMO lesions and contribute to the type-2 inflammation and the characteristic pruritus."
  - target: 01-human/03-molecular/il-31
    relation: connects-to
    note: "Pruritus cytokine: IL-31, a type-2 (IL-4 and IL-13 already mapped) cytokine, mediates the paroxysmal neuropathic itch that is a characteristic feature of the myelitis of neuromyelitis optica."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "CD8 infiltrate: the cytotoxic T cells (perforin already mapped) infiltrate the NMO lesions, contributing to the tissue damage alongside the complement-mediated (already mapped) astrocytopathy."
  - target: 01-human/03-molecular/factor-h
    relation: connects-to
    note: "Complement regulation: factor H regulates the alternative complement pathway (complement C3, C5 and C5aR1 already mapped) whose unchecked activation drives the astrocyte (already mapped) destruction targeted by the anti-C5 (eculizumab) therapy of neuromyelitis optica."
  - target: 01-human/03-molecular/tslp
    relation: connects-to
    note: "Type-2 alarmin: TSLP, an epithelial/stromal alarmin, contributes to the type-2 (IL-4, IL-5, IL-13 and IL-31 already mapped) dimension of the immune profile of neuromyelitis optica."
  - target: 01-human/02-atomic/selenium
    relation: connects-to
    note: "Autoimmune micronutrient: selenium, a selenoprotein antioxidant cofactor, is part of the micronutrient dimension (with vitamin D already mapped) of the autoimmune susceptibility of neuromyelitis optica."
  - target: 01-human/03-molecular/c1-esterase-inhibitor
    relation: connects-to
    note: "Classical-pathway regulation: the C1-esterase inhibitor regulates the classical complement pathway activated by the anti-AQP4 IgG (immunoglobulin already mapped) that drives the C5 (eculizumab target)-mediated astrocyte (already mapped) destruction of neuromyelitis optica."
  - target: 01-human/03-molecular/osteopontin
    relation: connects-to
    note: "Neuroinflammation matricellular: osteopontin, elevated in the NMO lesions and CSF, is a matricellular cytokine amplifying the astrocyte (already mapped) and myeloid neuroinflammation of neuromyelitis optica."
  - target: 01-human/03-molecular/transferrin
    relation: connects-to
    note: "CNS iron: transferrin, the iron carrier, reflects the disordered iron handling accompanying the demyelinating and necrotic CNS lesions of neuromyelitis optica."
  - target: 01-human/03-molecular/bradykinin
    relation: connects-to
    note: "Kinin-permeability axis: bradykinin, generated via the contact system activated by anti-AQP4 IgG (immunoglobulin already mapped) immune complexes, augments blood-brain-barrier permeability and oedema in the NMO lesions of neuromyelitis optica."
  - target: 01-human/03-molecular/erythropoietin
    relation: connects-to
    note: "Neuroprotective signal: erythropoietin, acting via EPOR on astrocytes (already mapped) and oligodendrocytes (already mapped), promotes CNS repair and limits the necrotic lesion expansion of neuromyelitis optica."
  - target: 01-human/03-molecular/histamine
    relation: connects-to
    note: "Mast-cell mediator: histamine, released from the perivascular mast cells (already mapped) recruited to NMO lesions, amplifies blood-brain-barrier disruption and leukocyte infiltration of neuromyelitis optica."
  - target: 01-human/03-molecular/periostin
    relation: connects-to
    note: "ECM remodelling in CNS lesions: periostin, expressed by reactive astrocytes (already mapped) and fibroblasts in NMO spinal cord lesions, promotes the fibrotic extracellular matrix remodelling and necrotic cavity formation of neuromyelitis optica."
  - target: 01-human/03-molecular/melatonin
    relation: connects-to
    note: "Circadian neuroprotection: melatonin, via MT1/MT2 receptors on astrocytes (already mapped) and T regulatory cells (already mapped), suppresses the AQP4-IgG-driven complement cascade and promotes lesion repair in neuromyelitis optica."
  - target: 01-human/03-molecular/prolactin
    relation: connects-to
    note: "Immune-endocrine modulation: prolactin, elevated under stress and during relapse in NMO, potentiates the B-cell (already mapped) and plasmablast (plasma-cell already mapped) responses that produce AQP4-IgG and drives the female-predominant autoimmune skew of NMO."
  - target: 01-human/03-molecular/testosterone
    relation: connects-to
    note: "NMO testosterone: testosterone suppresses the B-cell (already mapped) AQP4-IgG production and plasma-cell (already mapped) autoantibody responses; androgen deficiency amplifies the complement C5 (already mapped) tissue injury and the female-predominant relapse risk of NMO."
  - target: 01-human/03-molecular/serotonin
    relation: connects-to
    note: "NMO serotonin: serotonin, via 5-HT receptors on astrocytes (already mapped) and microglia (already mapped), modulates the neuroinflammatory activation of NMO lesions; 5-HT also suppresses the B-cell (already mapped) autoimmune skew driving AQP4-IgG production in NMO."
  - target: 01-human/03-molecular/oxytocin
    relation: connects-to
    note: "NMO oxytocin: oxytocin, via OXTR on astrocytes (already mapped) and regulatory T cells (already mapped), attenuates the neuroinflammatory cascade and promotes AQP4-IgG-mediated lesion repair; oxytocin also modulates the B-cell (already mapped) autoimmune skew of NMO."
  - target: 01-human/03-molecular/vasopressin
    relation: connects-to
    note: "NMO vasopressin: vasopressin, via V1a receptors on astrocytes, amplifies the AQP4-mediated oedema and NF-κB (already mapped) neuroinflammatory cascade of NMO lesions; V2-receptor signalling modulates fluid dysregulation and worsens spinal-cord injury in NMOSD."
  - target: 01-human/02-atomic/iodine
    relation: connects-to
    note: "NMO iodine: iodine-dependent thyroid hormones regulate myelination of astrocytes (already mapped) and oligodendrocytes in the spinal cord; thyroid-hormone deficiency amplifies the NF-κB (already mapped) cascade and AQP4-IgG-mediated demyelination of NMO lesions."
  - target: 01-human/02-atomic/copper
    relation: connects-to
    note: "NMO copper: copper-dependent superoxide dismutase controls the oxidative stress amplifying AQP4-IgG-mediated astrocyte (already mapped) injury; copper deficiency impairs myelin synthesis and exacerbates the NF-κB (already mapped) neuroinflammation of NMO lesions."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "NMO zinc: zinc, as co-factor of SOD3 in astrocytes (already mapped) and macrophages (already mapped), scavenges ROS at the blood-brain barrier; zinc deficiency amplifies the NF-κB (already mapped) and TNF-α (already mapped) astrocytopathic cascade of NMO."
  - target: 01-human/02-atomic/phosphorus
    relation: connects-to
    note: "NMO phosphorus: phosphorus, as ATP precursor in neurons (already mapped) and macrophages (already mapped), supports astrocyte (already mapped) energy; phosphorus deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) pro-inflammatory cascade of NMO."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "NMO iron: iron, as cofactor of cytochrome c in astrocytes (already mapped) and macrophages (already mapped), supports mitochondrial function; iron deficiency amplifies the NF-κB (already mapped) and TNF-α (already mapped) inflammatory cascade of NMO."
  - target: 01-human/02-atomic/chloride
    relation: connects-to
    note: "NMO chloride: chloride channels regulate macrophage (already mapped) and mast-cell (already mapped) ion homeostasis at the blood-brain barrier; chloride imbalance amplifies NF-κB (already mapped) and IL-6 (already mapped) astrocytopathic cascade of NMO."
  - target: 01-human/02-atomic/nitrogen
    relation: connects-to
    note: "NMO nitrogen: nitrogen, as nitric oxide in astrocytes (already mapped) and macrophages (already mapped), drives CNS inflammatory stress; nitrogen dysregulation amplifies NF-κB (already mapped) and TNF-α (already mapped) and IL-6 (already mapped) cascade of NMO."
  - target: 01-human/02-atomic/carbon
    relation: connects-to
    note: "NMO carbon: carbon as backbone of AQP4 (already mapped) and NF-κB (already mapped) proteins in astrocytes (already mapped) sustains blood-brain barrier integrity; carbon depletion amplifies NF-κB (already mapped) and IL-6 (already mapped) astrocytopathic cascade of NMO."
  - target: 01-human/02-atomic/hydrogen
    relation: connects-to
    note: "NMO hydrogen: hydrogen, via redox homeostasis in astrocytes (already mapped) and macrophages (already mapped), supports AQP4 (already mapped) channel function; hydrogen dysregulation amplifies NF-κB (already mapped) and TNF-α (already mapped) astrocytopathic cascade of NMO."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "NMO oxygen: mitochondrial oxygen sustains ATP in astrocytes (already mapped) and oligodendrocytes (already mapped) for AQP4 (already mapped) channel homeostasis; hypoxia amplifies NF-κB (already mapped) and IL-6 (already mapped) demyelinating cascade of NMO."
  - target: 01-human/02-atomic/sulfur
    relation: connects-to
    note: "NMO sulfur: sulfur in cysteine residues of AQP4 (already mapped) and complement proteins in astrocytes (already mapped) sustains blood-brain barrier integrity; sulfur depletion amplifies NF-κB (already mapped) and IL-6 (already mapped) astrocytopathic cascade of NMO."
  - target: 01-human/03-molecular/glp-1
    relation: connects-to
    note: "NMO GLP-1: GLP-1 receptor agonism on astrocytes (already mapped) and macrophages (already mapped) modulates neuroinflammatory AQP4 autoimmune cascade; GLP-1 deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) demyelinating cascade of NMO."
  - target: 01-human/03-molecular/angiotensin-ii
    relation: connects-to
    note: "NMO angiotensin-II: angiotensin-II via AT1R on astrocytes (already mapped) and macrophages (already mapped) drives blood-brain barrier disruption and AQP4 complement attack; angiotensin-II excess amplifies NF-κB (already mapped) and IL-6 (already mapped) cascade of NMO."
  - target: 01-human/03-molecular/wnt-beta-catenin
    relation: connects-to
    note: "NMO wnt-beta-catenin: WNT/β-catenin on astrocytes (already mapped) and macrophages (already mapped) regulates AQP4 neuroinflammation; wnt-beta-catenin dysregulation amplifies nf-kb (already mapped) and il-6 (already mapped) and tnf-alpha (already mapped) cascade of NMO."
  - target: 01-human/03-molecular/rankl
    relation: connects-to
    note: "NMO rankl: RANKL from macrophages (already mapped) and astrocytes (already mapped) promotes AQP4-mediated CNS immune evasion; rankl excess amplifies nf-kb (already mapped) and il-6 (already mapped) and tnf-alpha (already mapped) cascade of NMO."
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "NMO smad4: SMAD4 in astrocytes (already mapped) and macrophages (already mapped) mediates TGF-β neuroinflammatory repair; smad4 dysregulation amplifies nf-kb (already mapped) and il-6 (already mapped) and tnf-alpha (already mapped) cascade of NMO."
  - target: 01-human/03-molecular/fibronectin
    relation: connects-to
    note: "NMO fibronectin: fibronectin in astrocytes (already mapped) and macrophages (already mapped) promotes CNS ECM remodelling in NMOSD; fibronectin excess amplifies nf-kb (already mapped) and il-6 (already mapped) and tnf-alpha (already mapped) cascade of NMO."
  - target: 01-human/03-molecular/notch
    relation: connects-to
    note: "NMO notch: Notch signalling in astrocytes (already mapped) and macrophages (already mapped) regulates glial fate in NMOSD; notch dysregulation amplifies nf-kb (already mapped) and il-6 (already mapped) and tnf-alpha (already mapped) cascade of NMO."
  - target: 01-human/03-molecular/igf-1
    relation: connects-to
    note: "NMO igf-1: IGF-1 from astrocytes (already mapped) and macrophages (already mapped) promotes neuroprotective repair in NMOSD; igf-1 dysregulation amplifies nf-kb (already mapped) and il-6 (already mapped) and tnf-alpha (already mapped) cascade of NMO."
  - target: 01-human/03-molecular/activin-a
    relation: connects-to
    note: "NMO activin-a: activin-A from astrocytes (already mapped) and macrophages (already mapped) modulates CNS neuroinflammatory tone; activin-a excess amplifies nf-kb (already mapped) and il-6 (already mapped) and tnf-alpha (already mapped) cascade of NMO."
  - target: 01-human/03-molecular/calcitonin
    relation: connects-to
    note: "NMO calcitonin: calcitonin from astrocytes (already mapped) and macrophages (already mapped) modulates CNS calcium balance; calcitonin excess amplifies nf-kb (already mapped) and il-6 (already mapped) and tnf-alpha (already mapped) cascade of NMO."
  - target: 01-human/03-molecular/cgrp
    relation: connects-to
    note: "NMO cgrp: CGRP from astrocytes (already mapped) and macrophages (already mapped) modulates CNS neuroimmune tone; cgrp excess amplifies nf-kb (already mapped) and il-6 (already mapped) and tnf-alpha (already mapped) cascade of NMO."
---

# NMOSD

## Overview

**Neuromyelitis optica spectrum disorder (NMOSD)** is a rare, relapsing inflammatory CNS disease characterized by attacks on the **optic nerves** (optic neuritis), **spinal cord** (transverse myelitis), and **brainstem** (area postrema syndrome — intractable hiccups, nausea, vomiting) [^wingerchuk-2015-nmosd-criteria]. It was historically confused with multiple sclerosis (MS) until the discovery of **AQP4-IgG (anti-aquaporin-4 antibody)** in 2004, which established NMOSD as a distinct disease — an **astrocytopathy** rather than a primary demyelinating disease.

**Epidemiology:**
- Prevalence: ~1–4 per 100,000 globally; higher in non-White populations (African, Asian descent)
- Sex ratio: F:M ~9:1 (even more female-predominant than MS)
- Mean age of onset: 30–45 years; can occur in children and the elderly
- Course: Relapsing in >95% (monophasic in a minority); each attack may cause permanent disability

**Biomarker subgroups:**
- **AQP4-IgG+:** ~75–85% of NMOSD; most severe; responds well to complement and IL-6R inhibitors
- **MOG-IgG+:** ~10–15%; overlapping phenotype but distinct immunopathology (primary demyelination, not astrocyte loss); often milder and sometimes monophasic; MOGAD (MOG antibody-associated disease) increasingly recognized as separate entity
- **Double-seronegative:** ~5–10%; may have undetected antibodies or represent a heterogeneous group

**Key distinguishing features from MS:**
- NMOSD attacks are more severe (complete optic neuritis, longitudinally extensive myelitis ≥3 vertebral segments)
- No oligoclonal bands in CSF (vs. present in ~90% of MS)
- Brain MRI may be normal or show periventricular, area postrema lesions (not MS-typical Dawson's fingers)
- IFN-β and natalizumab are **contraindicated or potentially harmful** in NMOSD

## Structure

### Clinical attack phenotypes

**Optic neuritis (ON):**
- Unilateral or bilateral simultaneous visual loss; pain on eye movement
- More severe than MS-ON: greater visual loss (often to light perception or no light perception), slower/incomplete recovery
- Retinal nerve fiber layer (RNFL) thinning on OCT is more severe than in MS-ON
- Posterior/chiasmal involvement (perineural optic nerve sheath enhancement on MRI with gadolinium)

**Longitudinally extensive transverse myelitis (LETM):**
- Spinal cord lesion spanning ≥3 vertebral segments (vs. MS ≤2 segments)
- Involves central cord grey matter → severe incomplete motor deficit, sensory level, bowel/bladder dysfunction
- Spinal MRI: T2-bright signal spanning 3–20 segments; "bright spotty lesion" in grey matter
- High risk of permanent paraparesis/quadriparesis after severe attacks

**Area postrema syndrome:**
- Pathognomonic: intractable hiccups, nausea, vomiting lasting >48 hours
- Caused by lesions at dorsal medulla/area postrema (AQP4-rich region)
- Often precedes or accompanies other NMOSD attacks
- MRI: dorsal medullary T2 signal; difficult to distinguish from vomiting of other causes

**Diencephalic/brainstem syndromes:**
- Narcolepsy-like hypersomnolence (hypothalamic lesions)
- Symptomatic bradycardia or respiratory failure (brainstem involvement in severe attacks)
- SIADH (hypothalamic lesions)

### 2015 International Consensus Diagnostic Criteria

Diagnosis of NMOSD with AQP4-IgG requires ≥1 core clinical characteristic:
1. Optic neuritis
2. Acute myelitis (LETM or central cord pattern)
3. Area postrema syndrome
4. Acute brainstem syndrome
5. Symptomatic narcolepsy or diencephalic syndrome
6. Symptomatic cerebral syndrome with typical NMOSD brain MRI lesion

**For AQP4-IgG+ patients:** ≥1 core clinical characteristic + AQP4-IgG confirmatory testing (cell-based assay preferred) is sufficient for diagnosis.

**For AQP4-IgG− patients:** ≥2 core clinical characteristics (including optic neuritis OR LETM OR area postrema syndrome) + MRI criteria + exclusion of alternative diagnoses.

## Function

NMOSD impairs CNS function through three attack-related mechanisms:

1. **Astrocyte destruction** — AQP4-IgG-mediated complement attack on astrocyte endfeet → loss of astrocyte support for oligodendrocytes → secondary demyelination → axonal loss; irreversible neurological deficit accumulates with each relapse (unlike MS where gradual decline is the norm; NMOSD is relapse-driven)

2. **Demyelination cascade** — Oligodendrocyte death secondary to astrocyte loss → extensive demyelination especially in optic nerve, spinal cord white matter; remyelination is poor given astrocyte scaffold loss; Wallerian degeneration follows

3. **Inflammatory cascade** — C5a attracts eosinophils (NMOSD lesions are eosinophil-rich, unlike MS), macrophages, and neutrophils → cytokine amplification → tissue destruction beyond the primary antibody-mediated event

## Pathology

### Immunopathogenesis

**AQP4-IgG production:**
- Origin: Long-lived plasma cells (resistant to anti-CD20 therapy) in bone marrow produce AQP4-IgG; plasmablasts in peripheral blood are acutely elevated during attacks; IL-6 drives plasmablast expansion
- AQP4-IgG crosses the blood-brain barrier at sites of transient BBB disruption → binds AQP4 OAPs on astrocyte endfeet

**Complement effector phase:**
- Classical pathway activation: IgG1 anti-AQP4 → C1q → C4 → C3 → C5 → C5b-9 (MAC) → astrocyte lysis
- C5a chemokine gradient → eosinophil and neutrophil influx → secondary tissue damage
- This complement dependence is the mechanistic basis for **eculizumab** and **ravulizumab** efficacy

**Astrocyte loss signature (NMOSD vs. MS):**
- NMOSD lesion: loss of GFAP and AQP4 immunoreactivity (astrocyte necrosis); MAC deposition on vessels; eosinophil/granulocyte infiltration; relatively preserved myelin initially, then secondary demyelination
- MS lesion: reactive astrocytosis (↑GFAP); primary demyelination; perivenular CD8+ T cells; lymphocytic infiltration

### Role of IL-6 and B cell axis

- IL-6 drives **plasmablast differentiation** from B cells → AQP4-IgG production
- Circulating plasmablasts are elevated during NMOSD attacks and correlate with AQP4-IgG titer
- IL-6R blockade (satralizumab, tocilizumab) reduces plasmablast expansion → lower AQP4-IgG titers → fewer attacks
- CD19+ B cells (and plasmablasts) are depleted by **inebilizumab** (anti-CD19); broader spectrum than rituximab (anti-CD20), which spares CD19+CD20− plasmablasts

### MOG-IgG+ NMOSD (MOGAD) — distinct mechanism

- MOG (myelin oligodendrocyte glycoprotein) is expressed on outer surface of compact myelin and oligodendrocyte soma
- MOG-IgG (predominantly IgG1) binds MOG → direct myelin/oligodendrocyte attack → primary demyelination without astrocyte destruction
- MOGAD lesions: GFAP preserved; AQP4 preserved; T cell-rich inflammation; cortical involvement common
- **Clinical implications:** Eculizumab NOT approved for MOGAD; complement is less central; B cell depletion may be less effective than in AQP4-IgG+ NMOSD; MOGAD has better prognosis in many patients

## Treatment

### Acute attack management

**High-dose IV methylprednisolone** (IVMP): 1 g/d × 5 days → standard first-line for acute attacks; limits attack severity but does not prevent future relapses

**Plasma exchange (PLEX):** 5–7 sessions every other day → removes AQP4-IgG and complement components → highly effective for steroid-refractory attacks; reduces complement-mediated astrocyte destruction; often combined with IVMP in severe attacks (optic nerve threat or paraparesis)

### Long-term attack prevention — approved therapies

**Eculizumab (Soliris; Alexion):**
- Monoclonal anti-C5 antibody; blocks C5 → prevents C5a and C5b-9 formation
- **PREVENT trial** (N=143, randomized, double-blind; AQP4-IgG+ NMOSD): annualized relapse rate (ARR) **0.02 vs. 0.35** placebo (94% reduction); 98% attack-free at 48 weeks; FDA approved **June 2019** [^pittock-2019-eculizumab-prevent]
- Requires meningococcal vaccination; PML risk low but reported

**Ravulizumab (Ultomiris; Alexion):**
- Long-acting anti-C5 (CHAMPION-NMOSD); q8w dosing vs. eculizumab q2w; FDA approved June 2023
- Same mechanism as eculizumab; convenient dosing; comparable efficacy

**Inebilizumab (Uplizna; Amgen):**
- Anti-CD19 mAb → depletes broader B cell compartment including plasmablasts (CD19+CD20−)
- **N-MOmentum trial** (N=230; AQP4-IgG+ NMOSD): 88% inebilizumab vs. 63% placebo attack-free at 197 days; FDA approved **June 2020** [^cree-2019-inebilizumab-nmomentum]
- Also approved for NMOSD — now dual approved for both NMOSD and CIDP (different indications)

**Satralizumab (Enspryng; Roche):**
- Anti-IL-6R mAb (recycling engineered antibody with extended t½); SC q4w
- **SAkuraStar** (monotherapy; AQP4-IgG+ subgroup): ARR reduction ~55% vs. placebo; FDA approved **August 2020** [^yamamura-2020-satralizumab-sakurastar]
- **SAkuraSky** (add-on to baseline IS): similar efficacy; SC self-injection enables home administration

### Off-label prevention (widely used)

**Rituximab** (anti-CD20): 375 mg/m² × 4 doses or 1000 mg × 2 doses; widely used as first-line off-label; ARR reduction ~70-80%; readministered when CD19+ B cells repopulate (typically q6m); risk: PML (< 1:10,000 at exposure levels typical in NMOSD)

**Azathioprine + prednisolone:** Widely used in resource-limited settings; modestly effective

**Mycophenolate mofetil:** Alternative steroid-sparing agent

**Contraindicated/harmful agents:**
- **IFN-β:** May increase attack frequency in AQP4-IgG+ NMOSD — do NOT use
- **Natalizumab:** Case series suggest possible worsening in NMOSD
- **Fingolimod:** Not established; potentially harmful

## Connections

- `connects-to` → **[Aquaporin-4](../../03-molecular/aquaporin-4/README.md)** — AQP4-IgG binds AQP4 on astrocyte endfeet → classical complement → MAC (C5b-9) → astrocyte lysis → secondary demyelination; pathognomonic in ~85% of NMOSD; ELISA and cell-based assays detect AQP4-IgG; titer correlates with disease activity.
- `connects-to` → **[Complement C5](../../03-molecular/complement-c5/README.md)** — Eculizumab (anti-C5; PREVENT: ARR 0.02 vs 0.35; FDA Jun 2019) and ravulizumab (CHAMPION-NMOSD; FDA Jun 2023) block C5 → prevent MAC on astrocytes → halt AQP4-IgG-driven attacks; effective only in AQP4-IgG+ NMOSD, not MOG-IgG+.
- `connects-to` → **[IL-6](../../03-molecular/il-6/README.md)** — Satralizumab (anti-IL-6R; SAkuraStar; FDA Aug 2020) reduced ARR ~55% vs placebo; IL-6 promotes plasmablast expansion → AQP4-IgG production; IL-6 also amplifies Th17 responses; tocilizumab used off-label.
- `connects-to` → **[CD20](../../03-molecular/cd20/README.md)** — Rituximab (anti-CD20) depletes B cells → reduces AQP4-IgG; widely used off-label as first-line NMOSD prevention (~70-80% ARR reduction); inebilizumab (anti-CD19; N-MOmentum: 88% vs 63% attack-free; FDA Jun 2020) also approved.
- `connects-to` → **[Type I Interferon](../../03-molecular/type-i-interferon/README.md)** — IFN-β is CONTRAINDICATED in AQP4-IgG+ NMOSD — trials showed IFN-β increases attack frequency; IFN-β may promote plasmablast differentiation → higher AQP4-IgG; this differentiates NMOSD from MS where IFN-β is first-line.
- `connects-to` → **[Astrocyte](../../04-cellular/astrocyte/README.md)** — NMOSD is an astrocytopathy: AQP4-IgG binds the aquaporin-4 channels clustered on astrocyte endfeet → classical complement → membrane-attack complex → astrocyte lysis, and only then does secondary demyelination follow — unlike multiple sclerosis, where myelin is hit first.
- `connects-to` → **[Multiple Sclerosis](../multiple-sclerosis/README.md)** — NMOSD was long mistaken for multiple sclerosis until AQP4-IgG split them apart; NMOSD brings more severe, longitudinally extensive cord lesions and complete optic neuritis, lacks CSF oligoclonal bands, and crucially is worsened by the interferon-β and natalizumab that treat MS.
- `connects-to` → **[Eye](../../06-organ/eye/README.md)** — Optic neuritis is a defining NMOSD attack and is far more destructive than in MS: patients lose vision often to light-perception or worse, recover poorly, and show severe retinal nerve fiber layer thinning on OCT; bilateral or chiasmal involvement favours NMOSD over MS.
- `connects-to` → **[West Nile Virus](../west-nile-virus/README.md)** — NMOSD and West Nile virus both attack the cord to cause myelitis but by opposite routes: NMOSD is autoimmune AQP4-IgG complement attack on astrocytes, while WNV is a neurotropic flavivirus infecting anterior-horn neurons → acute flaccid paralysis.
- `connects-to` → **[B Cell](../../04-cellular/b-cell/README.md)** — NMOSD is antibody-driven: CD19+ plasmablasts produce the pathogenic AQP4-IgG and IL-6 sustains them; this B-cell dependence is why anti-CD20 (rituximab) and anti-CD19 (inebilizumab) deplete B cells and anti-IL-6R (satralizumab) work, while T-cell-directed MS drugs fail.
- `connects-to` → **[Sjögren's Syndrome](../sjogrens-syndrome/README.md)** — NMOSD frequently coexists with systemic autoimmunity, especially Sjögren's and lupus: AQP4-IgG-positive patients often carry anti-Ro/SSA, anti-La or ANA, and the myelitis/optic neuritis is the neurological face of NMOSD, not a direct effect of the connective-tissue disease.
- `connects-to` → **[Systemic Lupus Erythematosus](../systemic-lupus-erythematosus/README.md)** — When neuromyelitis optica coexists with lupus, the myelitis is NMO, not CNS lupus: AQP4-IgG-positive NMO can occur alongside SLE, so transverse myelitis or optic neuritis in a lupus patient should prompt AQP4 testing rather than assuming neuropsychiatric lupus.
- `connects-to` → **[Myasthenia Gravis](../myasthenia-gravis/README.md)** — Neuromyelitis optica and myasthenia gravis are antibody-mediated diseases that co-occur more than by chance: both are driven by pathogenic IgG (anti-AQP4 vs anti-AChR) and a tendency to further autoimmunity, and NMO can emerge after thymectomy for myasthenia.
- `connects-to` → **[Plasma Cell](../../04-cellular/plasma-cell/README.md)** — Plasma cells make the pathogenic antibody of neuromyelitis optica: long-lived plasma cells and plasmablasts secrete anti-aquaporin-4 IgG that, with complement, destroys astrocytes—so therapy targets the B-cell/plasma-cell axis (rituximab, satralizumab, eculizumab).
- `connects-to` → **[Guillain-Barré Syndrome](../../05-tissue/guillain-barre/README.md)** — NMO and Guillain-Barré are both antibody-mediated demyelinating diseases but of different compartments: NMO's anti-aquaporin-4 antibodies attack CNS astrocytes, while GBS antibodies attack peripheral nerve myelin—central versus peripheral autoimmune demyelination.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Complement drives the astrocyte destruction of NMO: anti-aquaporin-4 antibodies bound to astrocytes activate the complement cascade, whose membrane attack complex lyses them—so complement inhibitors are now NMO therapy, treating the disease at its effector step.
- `connects-to` → **[Oligodendrocyte](../../04-cellular/oligodendrocyte/README.md)** — NMO and MS are distinguished by their cellular target: MS attacks oligodendrocytes and myelin, while NMO attacks astrocytes via aquaporin-4—so NMO is an astrocytopathy, not a demyelinating disease per se, and MS drugs can worsen it, making the distinction critical.
- `connects-to` → **[Immunoglobulin G](../../03-molecular/immunoglobulin-g/README.md)** — NMO is defined by a pathogenic IgG autoantibody: AQP4-IgG binds astrocyte water channels and fixes complement, so this IgG is both the diagnostic test and the direct cause of the astrocyte destruction—distinguishing NMO from multiple sclerosis.
- `connects-to` → **[T Helper Cell](../../04-cellular/t-helper-cell/README.md)** — T helper cells drive the NMO attack: Th17 cells and the IL-6 they help sustain promote AQP4-specific antibody production and open the blood-brain barrier, so the antibody response depends on T-cell help—rationale for IL-6-pathway therapy.
- `connects-to` → **[Immune System](../immune-system/README.md)** — NMO is a systemic autoimmune disease that strikes the CNS: it clusters with lupus and Sjogren's, reflecting broad loss of self-tolerance, and is controlled by immunosuppression and B-cell depletion rather than the immunomodulators used in MS.
- `connects-to` → **[Brain](../../06-organ/brain/README.md)** — NMO is not just an eye-and-cord disease—it strikes the brain: lesions in the area postrema cause intractable hiccups, nausea, and vomiting, and diencephalic or brainstem attacks add narcolepsy or other signs, so AQP4-rich brain regions are characteristic NMO targets.
- `connects-to` → **[Regulatory T Cell](../../04-cellular/regulatory-t-cell/README.md)** — NMO reflects a breakdown of immune tolerance: regulatory T cells that should restrain self-reactivity are deficient or dysfunctional, allowing AQP4-specific T and B cells to mature—so failed Treg control underlies the autoimmunity against astrocyte water channels.
- `connects-to` → **[Natural Killer Cell](../../04-cellular/natural-killer-cell/README.md)** — Natural killer cells help execute NMO's astrocyte damage: once anti-AQP4 antibodies coat astrocytes, NK cells (and complement) destroy them by antibody-dependent cytotoxicity, so innate effectors translate the autoantibody into the actual tissue injury.
- `connects-to` → **[Neutrophil](../../04-cellular/neutrophil/README.md)** — Neutrophils mark NMO lesions, unlike MS: the antibody-and-complement attack on astrocytes draws in neutrophils and eosinophils, so the inflammatory infiltrate and CSF granulocytes help distinguish neuromyelitis optica from multiple sclerosis.
- `connects-to` → **[Glutamate](../../03-molecular/glutamate/README.md)** — NMO unleashes glutamate excitotoxicity: anti-AQP4 antibodies kill astrocytes whose glutamate transporters normally clear the synapse, so glutamate floods and poisons oligodendrocytes and neurons—why astrocyte loss cascades into demyelination.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — NMO is treated by blocking IL-6 signaling through JAK: satralizumab targets the IL-6 receptor whose JAK-STAT signal drives the AQP4-antibody-producing plasmablasts, one of several approved therapies that have transformed NMO prognosis.
- `connects-to` → **[FcRn](../../03-molecular/fcrn/README.md)** — NMO is driven by pathogenic IgG that FcRn keeps alive: the anti-AQP4 antibody attacks astrocytes, and because FcRn recycles IgG to prolong its life, blocking FcRn (efgartigimod) is a strategy to clear the harmful antibody.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — NMO recruits Th17 and IL-17 to breach the brain barrier: IL-17 helps open the blood-brain barrier and inflame lesions, letting anti-AQP4 antibody reach astrocytes—part of why IL-6 blockade (which curbs Th17) prevents relapses.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — NMO lesions are finished off by macrophages: after anti-AQP4 antibody and complement attack astrocytes, macrophages clear the debris and demyelinate, producing the destructive, longitudinally extensive cord and optic-nerve lesions.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — NMO kills cells through calcium: when astrocytes die and can no longer clear glutamate, the flood overexcites neurons and oligodendrocytes, opening channels that let lethal calcium pour in—the excitotoxicity behind the tissue destruction.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — NMO ultimately destroys neurons: though astrocytes are the first target, the complement-driven inflammatory attack severs axons and kills neurons in the cord and optic nerve, causing the lasting paralysis and blindness of relapses.
- `connects-to` → **[Synapse](../../05-tissue/synapse/README.md)** — NMO poisons the synapse by silencing astrocytes: these cells normally clear glutamate from synapses through transporters tied to aquaporin-4, so destroying them lets glutamate linger and excitotoxically damage the surrounding tissue.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — NMO is mapped by MRI: its hallmark is a long spinal-cord lesion spanning three or more segments, plus optic-nerve enhancement, all read in the photons of magnetic-resonance imaging.
- `connects-to` → **[Sodium](../../02-atomic/sodium/README.md)** — NMO lesions in the brain's area postrema and hypothalamus can derange sodium balance, causing SIADH and low blood sodium alongside the intractable vomiting and hiccups that flag the disease.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — NMO breaches the blood-brain barrier where astrocyte foot processes meet endothelial cells: the antibody and complement attack on this interface opens the door for the wider immune assault on the cord.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy distinguishes NMO from MS at the lesion: it is the astrocyte that dies first — its foot processes stripped of aquaporin-4 and coated with complement — rather than the myelin, a primary astrocytopathy unlike MS demyelination.
- `connects-to` → **[Stomach](../../06-organ/stomach/README.md)** — NMO can present from the stomach's control center: lesions in the area postrema of the brainstem trigger intractable hiccups, nausea, and vomiting — a characteristic syndrome that often heralds the disease before the cord or optic nerve is hit.
- `connects-to` → **[Potassium](../../02-atomic/potassium/README.md)** — Destroying aquaporin-4 unsettles potassium balance: the water channel sits beside the astrocyte channels that mop up potassium released by firing neurons, so the NMO attack disrupts the ion buffering that keeps the cord's neurons stable.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — NMO turns on a single self-protein: the AQP4-IgG autoantibody is both its cause and its diagnostic hallmark, distinguishing it from MS, and the related MOG antibody defines a separate but overlapping demyelinating disease.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — A high cord attack can stop the breath: NMO's longitudinally extensive myelitis or brainstem lesions can knock out the nerves driving the diaphragm, causing neurogenic respiratory failure that is a leading cause of death.
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — A puzzle of where the channel lives: aquaporin-4 is abundant in the kidney's collecting ducts and the stomach too, yet NMO spares them and strikes the CNS — a selectivity set by how the blood-brain barrier and complement expose the target.
- `connects-to` → **[Large Intestine](../../06-organ/large-intestine/README.md)** — Cord lesions sever the bowel's controls: NMO's transverse myelitis disrupts the spinal pathways to the rectum and bladder, leaving neurogenic bowel and bladder dysfunction — constipation, incontinence, and retention — among its lasting disabilities.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — Pregnancy can stir NMO, unlike MS: relapse risk rises in the months after delivery, and active disease threatens the pregnancy, so timing conception and choosing pregnancy-safe immunotherapy are central to managing affected women.
- `connects-to` → **[Hippocampus](../../05-tissue/hippocampus/README.md)** — NMO can reach the memory circuits: aquaporin-4 is dense in the hippocampus, and some patients develop cognitive impairment and limbic lesions, widening the disease beyond the optic nerve and spinal cord it is named for.
- `connects-to` → **[Microglia](../../04-cellular/microglia/README.md)** — When astrocytes die, microglia take over the damage: AQP4-antibody attack strips away astrocytes, and the reactive microglia that move in pour out inflammatory mediators that injure neurons and oligodendrocytes in the secondary wave of an NMO lesion.
- `connects-to` → **[BAFF](../../03-molecular/baff/README.md)** — NMO is a B-cell disease fed by BAFF: this survival cytokine keeps alive the plasmablasts that pump out aquaporin-4 antibody, so high BAFF marks active disease and B-cell-targeted therapy is a mainstay.
- `connects-to` → **[Rheumatoid Arthritis](../rheumatoid-arthritis/README.md)** — NMO travels with systemic autoimmunity: patients carry higher rates of coexisting diseases like rheumatoid arthritis, reflecting a shared autoimmune diathesis and overlapping B-cell- and IL-6-targeted treatments.
- `connects-to` → **[Neuropathic Pain](../neuropathic-pain/README.md)** — Its myelitis leaves searing pain: damage to the spinal cord in NMO causes severe neuropathic pain and painful tonic spasms that often persist between attacks, a leading driver of disability between relapses.
- `connects-to` → **[Epilepsy](../epilepsy/README.md)** — When it reaches the brain it can spark seizures: although NMO favors the optic nerves and cord, cerebral lesions — common in AQP4-rich regions and in pediatric disease — can irritate the cortex and provoke epilepsy.
- `connects-to` → **[Dendritic Cell](../../04-cellular/dendritic-cell/README.md)** — The autoimmune attack must first be taught: dendritic cells present aquaporin-4 peptides to T cells, licensing the helper response that drives B cells to make the pathogenic anti-AQP4 antibody.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — The antibody attack inflames through NF-κB: AQP4-IgG binding and complement on astrocytes drive NF-κB-dependent cytokine and chemokine release, amplifying the neutrophil-rich inflammation that destroys tissue in an NMO lesion.
- `connects-to` → **[Sepsis](../sepsis/README.md)** — Complement-blocking therapy opens a dangerous door: eculizumab, used to prevent NMO relapses, blocks the membrane attack complex and sharply raises the risk of meningococcal and other encapsulated-organism infection and sepsis, mandating vaccination.
- `connects-to` → **[Venous Thromboembolism](../venous-thromboembolism/README.md)** — Paralyzing attacks bring clot risk: a severe transverse myelitis relapse can leave a patient immobile for weeks, and the resulting venous stasis raises the risk of deep-vein thrombosis and pulmonary embolism.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — Relapsing disability weighs on mood: the unpredictable attacks of blindness and paralysis, chronic pain, and the lifelong threat of relapse give NMO a heavy psychological burden with high rates of depression.
- `connects-to` → **[Pneumocystis jirovecii](../../../02-pathogen/03-fungi/pneumocystis-jirovecii/README.md)** — Its B-cell-depleting therapy opens the lung: rituximab and the chronic immunosuppression used to prevent NMO relapses can drop T-cell defenses enough to risk Pneumocystis pneumonia, sometimes warranting prophylaxis.
- `connects-to` → **[Osteoporosis](../osteoporosis/README.md)** — Steroids and immobility thin the bone: the repeated high-dose corticosteroids for NMO attacks, plus reduced mobility from myelitis, accelerate bone loss and raise the risk of osteoporotic fracture.
- `connects-to` → **[Wound Healing](../wound-healing/README.md)** — Paralysis from myelitis breaks down the skin: severe transverse myelitis in NMO can leave patients immobile and insensate, predisposing to pressure ulcers that are slow to heal over bony prominences.
- `connects-to` → **[Chronic Kidney Disease](../ckd/README.md)** — A neurogenic bladder threatens the kidneys: spinal-cord attacks in NMO impair bladder control, and the recurrent urinary infections and back-pressure that follow can progress to chronic kidney disease.
- `connects-to` → **[Aspergillus fumigatus](../../../02-pathogen/03-fungi/aspergillus-fumigatus/README.md)** — Its potent immunotherapy opens the lung to mold: rituximab and other B-cell-depleting and immunosuppressive treatments for NMO can permit invasive Aspergillus infection.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — It is an antibody attack on the CNS: NMO targets aquaporin-4 on astrocytes, causing optic neuritis and longitudinally extensive transverse myelitis that blind and paralyse, a defining nervous-system autoimmune disease.
- `connects-to` → **[Respiratory System](../respiratory-system/README.md)** — High cord attacks can stop breathing: an NMO lesion in the cervical spinal cord or brainstem can paralyse the diaphragm and respiratory drive, causing neurogenic respiratory failure.
- `connects-to` → **[Neisseria meningitidis](../../../02-pathogen/02-bacteria/neisseria-meningitidis/README.md)** — Its complement-blocking drug invites meningococcus: eculizumab, used to prevent NMO relapses, blocks the terminal complement that defends against Neisseria meningitidis, so vaccination is mandatory before treatment.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — It announces itself through the gut: area postrema syndrome — intractable hiccups, nausea and vomiting from a medullary lesion — is a classic and often first manifestation of NMO.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — It targets the hypothalamus: AQP4-rich diencephalic regions are vulnerable, so NMO can cause SIADH, narcolepsy, hypothermia and other endocrine disturbances from hypothalamic lesions.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — Severe myelitis disables the limbs: longitudinally extensive transverse myelitis causes paralysis with spasticity and contractures, while long-term corticosteroids add bone and muscle complications.
- `connects-to` → **[Cardiovascular System](../cardiovascular-system/README.md)** — High cord lesions destabilise the circulation: cervical transverse myelitis can cause autonomic dysreflexia with dangerous blood-pressure swings and arrhythmia.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — Its therapies and overlaps touch the skin: immunosuppression with rituximab, eculizumab and steroids brings skin and infection problems, and NMO overlaps autoimmune connective-tissue skin disease.
- `connects-to` → **[Renal System](../renal-system/README.md)** — Overlap autoimmunity and drugs strain the kidney: NMO coexists with systemic lupus that can cause nephritis, and its long-term immunosuppression requires renal monitoring.
- `connects-to` → **[Targeted Therapy](../../../03-medicine/01-modern/13-cancer/targeted-therapy/README.md)** — Monoclonal antibodies transformed its care: eculizumab (anti-C5), satralizumab (anti-IL-6R) and inebilizumab (anti-CD19) prevent the relapses of AQP4-antibody neuromyelitis optica.
- `connects-to` → **[Corticosteroids](../../../03-medicine/01-modern/02-respiratory/corticosteroids/README.md)** — High-dose steroids treat the attack: intravenous corticosteroids, with plasma exchange, are first-line for acute optic neuritis and transverse myelitis relapses in NMO.
- `connects-to` → **[Epstein-Barr Virus](../../../02-pathogen/01-viruses/epstein-barr-virus/README.md)** — Viruses may help trigger it: like other CNS autoimmunity, neuromyelitis optica has been linked to prior Epstein-Barr virus infection shaping the aberrant antibody response.
- `connects-to` → **[Cancer Chemotherapy](../../../03-medicine/01-modern/13-cancer/cancer-chemotherapy/README.md)** — Cytotoxic immunosuppression and a cancer link: azathioprine, mycophenolate and cyclophosphamide serve as steroid-sparing maintenance in NMO, and a minority of AQP4-positive disease is paraneoplastic, declaring an underlying cancer.
- `connects-to` → **[Checkpoint Inhibitors](../../../03-medicine/01-modern/13-cancer/checkpoint-inhibitors/README.md)** — Immunotherapy can unmask it: cancer checkpoint inhibitors occasionally trigger AQP4-antibody neuromyelitis optica and other CNS demyelinating syndromes as severe immune-related adverse events.
- `connects-to` → **[Axonal Transport](../../05-tissue/axonal-transport/README.md)** — Astrocyte attack severs axons: although NMO primarily destroys aquaporin-4-bearing astrocytes, the resulting lesions disrupt axonal transport and cause the secondary axonal loss behind permanent optic and spinal-cord disability.
- `connects-to` → **[Pemphigus Vulgaris](../pemphigus-vulgaris/README.md)** — Antibody-and-complement disease in common: like pemphigus vulgaris, neuromyelitis optica is driven by pathogenic IgG and complement and responds to B-cell depletion (rituximab, inebilizumab)—autoimmunity striking the CNS rather than the skin.
- `connects-to` → **[Breast Cancer](../breast-cancer/README.md)** — It can be paraneoplastic: aquaporin-4 neuromyelitis optica is occasionally a paraneoplastic syndrome, reported with breast and lung cancers, so new NMO in an older adult may prompt a malignancy search.
- `connects-to` → **[Immune Thrombocytopenia](../immune-thrombocytopenia/README.md)** — Antibody-mediated autoimmunity that can coexist: like immune thrombocytopenia, NMO is an organ-specific autoantibody disease cleared by B-cell depletion, and the two can occur together in autoimmune-prone patients.
- `connects-to` → **[Germinal Center](../../05-tissue/germinal-center/README.md)** — Where the autoantibody is made: AQP4-IgG in neuromyelitis optica is produced by plasmablasts from germinal-centre B-cell responses, the target of B-cell-depleting and IL-6 (Tfh) therapies like rituximab and satralizumab.
- `connects-to` → **[Antiphospholipid Syndrome](../antiphospholipid-syndrome/README.md)** — Clustering autoimmunity: neuromyelitis optica frequently coexists with systemic autoimmune diseases including antiphospholipid syndrome and lupus, reflecting a shared predisposition to pathogenic autoantibody production.
- `connects-to` → **[SCLC](../sclc/README.md)** — A paraneoplastic trigger: AQP4-antibody NMO is occasionally paraneoplastic, reported with cancers including small-cell lung cancer, so a new diagnosis in an older smoker can prompt a tumour search.
- `connects-to` → **[COVID-19 Disease](../covid-19-disease/README.md)** — An infectious trigger: NMOSD attacks have been reported after SARS-CoV-2 infection and, rarely, vaccination, fitting the pattern of immune activation precipitating relapses of this antibody-mediated disease.
- `connects-to` → **[Type 1 Diabetes](../type-1-diabetes/README.md)** — Autoimmune clustering: NMOSD frequently coexists with other organ-specific autoimmune diseases such as type 1 diabetes, thyroiditis and myasthenia, reflecting a shared predisposition to autoimmunity.
- `connects-to` → **[Narcolepsy](../narcolepsy/README.md)** — Diencephalic syndrome: AQP4-rich hypothalamic lesions in NMO can cause symptomatic narcolepsy and hypersomnia along with SIADH, the antibody attacking the same brain regions that govern sleep and water balance.
- `connects-to` → **[IFN-γ](../../03-molecular/ifn-gamma/README.md)** — Th1 cytokine: IFN-γ from pathogenic T-helper cells amplifies the inflammatory, complement-fixing environment that drives the astrocyte destruction of NMO lesions.
- `connects-to` → **[Perforin](../../03-molecular/perforin/README.md)** — Cytotoxic killing: AQP4-IgG recruits NK cells and CD8 T cells whose perforin-mediated antibody-dependent cellular cytotoxicity adds to complement in destroying astrocytes.
- `connects-to` → **[NLRP3 Inflammasome](../../03-molecular/nlrp3-inflammasome/README.md)** — Glial inflammasome: NLRP3-inflammasome activation in microglia and macrophages within NMO lesions amplifies IL-1β-driven neuroinflammation and tissue damage.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Eosinophilic lesions: IL-5 recruits eosinophils, whose granule proteins are a distinctive feature of NMO lesions, adding eosinophil-mediated astrocyte injury that helps distinguish NMO from multiple sclerosis.
- `connects-to` → **[TGF-β](../../03-molecular/tgf-beta/README.md)** — Th17/Treg imbalance: a TGF-beta- and IL-6-shaped shift away from regulatory T cells toward pathogenic Th17 responses helps license the AQP4-reactive autoimmunity that drives NMO.
- `connects-to` → **[MHC Class II](../../03-molecular/mhc-class-ii/README.md)** — Autoantigen presentation: MHC class II presentation of aquaporin-4 peptides primes the CD4 helper T cells that provide help for the pathogenic AQP4-IgG response in NMO.
- `connects-to` → **[CCL2](../../03-molecular/ccl2/README.md)** — CCL2 draws monocytes and macrophages into the AQP4-targeted astrocytic lesions of NMO, amplifying the inflammatory injury beyond the initial complement-mediated astrocyte destruction that defines the disease.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — IL-1β released by activated myeloid cells and the inflammasome recruits the neutrophils and eosinophils that give NMO lesions their characteristic granulocyte-rich pathology, a feature distinguishing them from the lesions of multiple sclerosis.
- `connects-to` → **[TNF-α](../../03-molecular/tnf-alpha/README.md)** — TNF-α from activated microglia and macrophages compounds the astrocyte and oligodendrocyte damage in NMO lesions, contributing to the severe, often necrotic tissue destruction that drives the disabling attacks.
- `connects-to` → **[C5aR1](../../03-molecular/c5ar1/README.md)** — Complement activation on AQP4-bound astrocytes generates C5a, which through C5aR1 recruits the neutrophils and eosinophils that inflict the necrotic tissue damage of NMO lesions—downstream of the C5 blockade achieved by eculizumab.
- `connects-to` → **[Connexin-43](../../03-molecular/connexin43/README.md)** — AQP4 and connexin-43 are co-concentrated at astrocyte endfeet, so the AQP4-targeted attack disrupts connexin-43 gap-junction coupling between astrocytes, helping the lesion spread along the astroglial network of the spinal cord and optic nerve.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — VEGF released from injured astrocytes increases blood-brain-barrier permeability in NMO, letting more pathogenic anti-AQP4 antibody and complement reach the CNS and amplifying the lesion.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — IL-6 signaling (already mapped, the target of satralizumab) acts through STAT3 to drive the pathogenic plasmablasts and Th17 cells that produce the AQP4-IgG of neuromyelitis optica.
- `connects-to` → **[Caspase-3](../../03-molecular/caspase-3/README.md)** — Complement- and antibody-mediated astrocyte injury in NMO triggers caspase-3 apoptosis of astrocytes and bystander neurons, the cell death underlying its destructive optic-nerve and spinal-cord lesions.
- `connects-to` → **[BDNF](../../03-molecular/bdnf/README.md)** — AQP4-IgG-mediated astrocyte injury strips the BDNF and other trophic factors that astrocytes normally supply, contributing to the neuronal and oligodendrocyte damage of NMO lesions.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — IL-23 sustains the pathogenic Th17 cells whose IL-17A (mapped) helps disrupt the blood-brain barrier and recruit neutrophils to the AQP4-targeted lesions of NMO.
- `connects-to` → **[Interleukin-13](../../03-molecular/il-13/README.md)** — IL-13, with the IL-5 already mapped, recruits the eosinophils that are a characteristic feature of the inflammatory infiltrate in NMO lesions.
- `connects-to` → **[CTLA-4](../../03-molecular/ctla-4/README.md)** — Loss of CTLA-4-dependent regulatory control underlies the anti-AQP4 autoantibody response, and checkpoint-inhibitor therapy can trigger NMO-like autoimmunity.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — BAFF-driven PI3K-AKT signaling (BAFF mapped) sustains the autoreactive B-cell/plasmablast pool that produces pathogenic AQP4-IgG in NMO.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — The mTOR-regulated metabolic program supports antibody-secreting plasmablast expansion in NMO and is an investigational therapeutic target.
- `connects-to` → **[MYD88](../../03-molecular/myd88/README.md)** — TLR-MyD88 innate signaling amplifies the astrocytic and microglial inflammatory response that follows AQP4-IgG/complement attack in NMO.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Galectin-3 released by reactive astrocytes and microglia amplifies the neuroinflammation that follows the AQP4-IgG astrocytopathy of NMO.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — IFN-STAT1 signaling shapes the interferon-driven component of the immune response in the astrocyte-targeted inflammation of NMO.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — Cytosolic DNA released by astrocyte injury can engage cGAS-STING, contributing to the innate inflammatory amplification of NMO lesions.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — FOXO regulates the oxidative-stress and survival responses of the astrocytes targeted by AQP4-IgG in neuromyelitis optica.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — S100A8/A9 alarmins released by infiltrating granulocytes amplify the inflammatory tissue damage of the eosinophil- and neutrophil-rich lesions of neuromyelitis optica.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — ERK-MAPK signaling downstream of cytokine and complement stimuli contributes to the astrocyte and immune-cell activation of neuromyelitis optica.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β modulates the NF-κB-driven inflammatory and B-cell survival signaling of neuromyelitis optica.
- `connects-to` → **[HIF-1alpha](../../03-molecular/hif-1alpha/README.md)** — HIF-1α in the hypoxic, astrocyte-damaged CNS lesion contributes to the tissue injury of neuromyelitis optica.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — PI3K (PIK3CA)-AKT signaling (AKT already mapped) supports the survival of the autoreactive plasmablasts that produce anti-AQP4 antibodies in neuromyelitis optica.
- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — SRC-family (LYN) kinase signaling downstream of the B-cell receptor participates in the autoreactive anti-AQP4 B-cell response of neuromyelitis optica.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — Autophagy modulates the astrocyte and immune-cell responses relevant to neuromyelitis optica.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK-linked metabolic signaling participates in the astrocyte metabolic stress of neuromyelitis optica.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-driven leukocyte recruitment into the CNS contributes to the astrocyte and neural injury of neuromyelitis optica.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — DNMT3A-mediated DNA methylation participates in the epigenetic regulation of the autoreactive immune response of neuromyelitis optica.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — CXCL12-CXCR4 signaling participates in the leukocyte trafficking across the blood-brain barrier in neuromyelitis optica.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — IL-33 alarmin signaling participates in the astrocyte and neuroinflammatory responses of neuromyelitis optica.
- `connects-to` → **[ARID1A](../../03-molecular/arid1a/README.md)** — ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic regulation of the immune responses of neuromyelitis optica.
- `connects-to` → **[Calcineurin](../../03-molecular/calcineurin/README.md)** — Calcineurin-NFAT signaling participates in the T-cell activation (T-follicular-helper-driven anti-AQP4 response) of neuromyelitis optica.
- `connects-to` → **[Potassium](../../02-atomic/potassium/README.md)** — Astrocyte ion homeostasis: AQP4 water channels co-localise with the Kir4.1 potassium channel at astrocyte endfeet, so the anti-AQP4 attack of NMO disrupts both water and potassium buffering, contributing to the oedema and neuronal dysfunction of lesions.
- `connects-to` → **[Estrogen](../../03-molecular/estrogen/README.md)** — Female predominance: neuromyelitis optica shows a striking roughly ninefold female predominance with relapse patterns tied to pregnancy and the postpartum period, implicating estrogen and sex hormones in disease susceptibility.
- `connects-to` → **[IL-2](../../03-molecular/il-2/README.md)** — T-cell expansion: IL-2-driven proliferation of the follicular helper T cells that provide help for anti-AQP4 antibody production sustains the autoreactive B-cell response, complementing the checkpoint and antigen-presentation controls already mapped.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — Th2 antibody help: IL-4 and type-2 T-cell help support the B-cell production of the pathogenic anti-AQP4 IgG (immunoglobulin G already mapped), part of the humoral response that drives the astrocyte-targeting autoimmunity of neuromyelitis optica.
- `connects-to` → **[IL-10](../../03-molecular/il-10/README.md)** — Regulatory balance: deficient IL-10-mediated regulatory B- and T-cell control contributes to the unchecked anti-AQP4 response in neuromyelitis optica, and restoring this regulatory arm is a goal of tolerising therapies.
- `connects-to` → **[Progesterone](../../03-molecular/progesterone/README.md)** — Pregnancy relapse pattern: falling progesterone and estrogen (already mapped) postpartum coincides with a rise in neuromyelitis optica attacks, implicating sex-hormone fluctuation in the timing of relapses in this female-predominant disease.
- `connects-to` → **[Nitric oxide](../../03-molecular/nitric-oxide/README.md)** — Excitotoxic injury: nitric oxide, generated in the inflamed lesion, contributes with glutamate excitotoxicity (already mapped) to the astrocyte and secondary neuronal injury of neuromyelitis optica after the antibody and complement attack.
- `connects-to` → **[Xanthine oxidase](../../03-molecular/xanthine-oxidase/README.md)** — Oxidative lesion injury: reactive oxygen species, to which xanthine oxidase contributes, amplify the tissue damage in the acute neuromyelitis optica lesion, adding oxidative stress to the complement-mediated (already mapped) astrocyte destruction.
- `connects-to` → **[Prostaglandins](../../03-molecular/prostaglandins/README.md)** — Inflammatory eicosanoids: prostaglandins from the acute inflammatory infiltrate (IL-6 and TNF already mapped) of the neuromyelitis optica lesion contribute to the inflammation and blood-brain-barrier disruption of an attack.
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — Magnesium and excitotoxicity: magnesium blocks the NMDA receptor and buffers the glutamate (already mapped) excitotoxicity released when astrocytes (already mapped) are destroyed in the neuromyelitis optica lesion, a neuroprotective ion.
- `connects-to` → **[Vitamin D](../../../03-medicine/03-food/vitamin-d/README.md)** — Vitamin D and autoimmunity: low vitamin D status is associated with neuromyelitis optica and other autoimmune demyelinating disease, its immunomodulation of the T- and B-cell response (type-I interferon already mapped) influencing risk and activity.
- `connects-to` → **[Omega-3 fatty acids](../../../03-medicine/03-food/omega-3-fatty-acids/README.md)** — Omega-3 and inflammation resolution: the omega-3 fatty acids give rise to specialised pro-resolving mediators that counter the inflammatory eicosanoids (prostaglandins already mapped), studied as an adjunct in autoimmune neuroinflammation such as neuromyelitis optica.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Adipokine and autoimmunity: leptin, elevated in neuromyelitis optica, promotes the Th17 (IL-17 already mapped) and autoreactive responses, linking the metabolic-inflammatory state to the disease activity.
- `connects-to` → **[PD-1](../../03-molecular/pd-1/README.md)** — Checkpoint tolerance: the PD-1 checkpoint and the peripheral-tolerance mechanisms, when dysfunctional, permit the anti-AQP4 (already mapped) autoreactivity that drives neuromyelitis optica.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — Counter-regulatory adipokine: adiponectin, the anti-inflammatory counterpart of leptin (already mapped), is part of the adipokine-immune crosstalk whose imbalance shapes the autoimmune neuroinflammation of neuromyelitis optica.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), is the pro-inflammatory adipokine of the adipokine-immune crosstalk of the autoimmune neuroinflammation of neuromyelitis optica.
- `connects-to` → **[Oligodendrocyte](../../04-cellular/oligodendrocyte/README.md)** — Secondary demyelination: the astrocyte (already mapped) destruction of NMO causes the secondary oligodendrocyte loss and demyelination, distinct from the primary oligodendrocyte demyelination of multiple sclerosis (already mapped).
- `connects-to` → **[Systemic lupus erythematosus](../systemic-lupus-erythematosus/README.md)** — Autoimmune overlap: neuromyelitis optica co-occurs with systemic lupus erythematosus and Sjögren's, sharing the autoantibody and type-I interferon (already mapped) autoimmunity.
- `connects-to` → **[Systemic sclerosis](../systemic-sclerosis/README.md)** — Connective-tissue overlap: neuromyelitis optica can co-occur with systemic sclerosis and the other connective-tissue diseases (systemic lupus already mapped), part of the shared autoantibody autoimmunity.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm complementing the Th17 (IL-17 and IL-23 already mapped) drive of the AQP4 (already mapped) autoimmunity of neuromyelitis optica.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — Eosinophil/type-2 IgE: the IgE, with the type-2 cytokines (IL-4, IL-5 and IL-13 already mapped), reflects the eosinophil-rich type-2 dimension of the NMO lesions.
- `connects-to` → **[Mast cell](../../04-cellular/mast-cell/README.md)** — Mast cells in lesions: the mast cells, with the eosinophils (IL-5 already mapped), infiltrate the perivascular NMO lesions and contribute to the type-2 inflammation and the characteristic pruritus.
- `connects-to` → **[IL-31](../../03-molecular/il-31/README.md)** — Pruritus cytokine: IL-31, a type-2 (IL-4 and IL-13 already mapped) cytokine, mediates the paroxysmal neuropathic itch that is a characteristic feature of the myelitis of neuromyelitis optica.
- `connects-to` → **[Cytotoxic T cell](../../04-cellular/t-cytotoxic-cell/README.md)** — CD8 infiltrate: the cytotoxic T cells (perforin already mapped) infiltrate the NMO lesions, contributing to the tissue damage alongside the complement-mediated (already mapped) astrocytopathy.
- `connects-to` → **[Factor H](../../03-molecular/factor-h/README.md)** — Complement regulation: factor H regulates the alternative complement pathway (complement C3, C5 and C5aR1 already mapped) whose unchecked activation drives the astrocyte (already mapped) destruction targeted by the anti-C5 (eculizumab) therapy of neuromyelitis optica.
- `connects-to` → **[TSLP](../../03-molecular/tslp/README.md)** — Type-2 alarmin: TSLP, an epithelial/stromal alarmin, contributes to the type-2 (IL-4, IL-5, IL-13 and IL-31 already mapped) dimension of the immune profile of neuromyelitis optica.
- `connects-to` → **[Selenium](../../02-atomic/selenium/README.md)** — Autoimmune micronutrient: selenium, a selenoprotein antioxidant cofactor, is part of the micronutrient dimension (with vitamin D already mapped) of the autoimmune susceptibility of neuromyelitis optica.
- `connects-to` → **[C1-esterase inhibitor](../../03-molecular/c1-esterase-inhibitor/README.md)** — Classical-pathway regulation: the C1-esterase inhibitor regulates the classical complement pathway activated by the anti-AQP4 IgG (immunoglobulin already mapped) that drives the C5 (eculizumab target)-mediated astrocyte (already mapped) destruction of neuromyelitis optica.
- `connects-to` → **[Osteopontin](../../03-molecular/osteopontin/README.md)** — Neuroinflammation matricellular: osteopontin, elevated in the NMO lesions and CSF, is a matricellular cytokine amplifying the astrocyte (already mapped) and myeloid neuroinflammation of neuromyelitis optica.
- `connects-to` → **[Transferrin](../../03-molecular/transferrin/README.md)** — CNS iron: transferrin, the iron carrier, reflects the disordered iron handling accompanying the demyelinating and necrotic CNS lesions of neuromyelitis optica.
- `connects-to` → **[Bradykinin](../../03-molecular/bradykinin/README.md)** — Kinin-permeability axis: bradykinin, generated via the contact system activated by anti-AQP4 IgG (immunoglobulin already mapped) immune complexes, augments blood-brain-barrier permeability and oedema in the NMO lesions of neuromyelitis optica.
- `connects-to` → **[Erythropoietin](../../03-molecular/erythropoietin/README.md)** — Neuroprotective signal: erythropoietin, acting via EPOR on astrocytes (already mapped) and oligodendrocytes (already mapped), promotes CNS repair and limits the necrotic lesion expansion of neuromyelitis optica.
- `connects-to` → **[Histamine](../../03-molecular/histamine/README.md)** — Mast-cell mediator: histamine, released from the perivascular mast cells (already mapped) recruited to NMO lesions, amplifies blood-brain-barrier disruption and leukocyte infiltration of neuromyelitis optica.
- `connects-to` → **[Periostin](../../03-molecular/periostin/README.md)** — ECM remodelling in CNS lesions: periostin, expressed by reactive astrocytes (already mapped) and fibroblasts in NMO spinal cord lesions, promotes the fibrotic extracellular matrix remodelling and necrotic cavity formation of neuromyelitis optica.
- `connects-to` → **[Melatonin](../../03-molecular/melatonin/README.md)** — Circadian neuroprotection: melatonin, via MT1/MT2 receptors on astrocytes (already mapped) and T regulatory cells (already mapped), suppresses the AQP4-IgG-driven complement cascade and promotes lesion repair in neuromyelitis optica.
- `connects-to` → **[Prolactin](../../03-molecular/prolactin/README.md)** — Immune-endocrine modulation: prolactin, elevated under stress and during relapse in NMO, potentiates the B-cell (already mapped) and plasmablast (plasma-cell already mapped) responses that produce AQP4-IgG and drives the female-predominant autoimmune skew of NMO.
- `connects-to` → **[Testosterone](../../03-molecular/testosterone/README.md)** — NMO testosterone: testosterone suppresses the B-cell (already mapped) AQP4-IgG production and plasma-cell (already mapped) autoantibody responses; androgen deficiency amplifies the complement C5 (already mapped) tissue injury and the female-predominant relapse risk of NMO.
- `connects-to` → **[Serotonin](../../03-molecular/serotonin/README.md)** — NMO serotonin: serotonin, via 5-HT receptors on astrocytes (already mapped) and microglia (already mapped), modulates the neuroinflammatory activation of NMO lesions; 5-HT also suppresses the B-cell (already mapped) autoimmune skew driving AQP4-IgG production in NMO.
- `connects-to` → **[Oxytocin](../../03-molecular/oxytocin/README.md)** — NMO oxytocin: oxytocin, via OXTR on astrocytes (already mapped) and regulatory T cells (already mapped), attenuates the neuroinflammatory cascade and promotes AQP4-IgG-mediated lesion repair; oxytocin also modulates the B-cell (already mapped) autoimmune skew of NMO.
- `connects-to` → **[Vasopressin](../../03-molecular/vasopressin/README.md)** — NMO vasopressin: vasopressin, via V1a receptors on astrocytes, amplifies the AQP4-mediated oedema and NF-κB (already mapped) neuroinflammatory cascade of NMO lesions; V2-receptor signalling modulates fluid dysregulation and worsens spinal-cord injury in NMOSD.
- `connects-to` → **[Iodine](../../02-atomic/iodine/README.md)** — NMO iodine: iodine-dependent thyroid hormones regulate myelination of astrocytes (already mapped) and oligodendrocytes in the spinal cord; thyroid-hormone deficiency amplifies the NF-κB (already mapped) cascade and AQP4-IgG-mediated demyelination of NMO lesions.
- `connects-to` → **[Copper](../../02-atomic/copper/README.md)** — NMO copper: copper-dependent superoxide dismutase controls the oxidative stress amplifying AQP4-IgG-mediated astrocyte (already mapped) injury; copper deficiency impairs myelin synthesis and exacerbates the NF-κB (already mapped) neuroinflammation of NMO lesions.
- `connects-to` → **[Zinc](../../02-atomic/zinc/README.md)** — NMO zinc: zinc, as co-factor of SOD3 in astrocytes (already mapped) and macrophages (already mapped), scavenges ROS at the blood-brain barrier; zinc deficiency amplifies the NF-κB (already mapped) and TNF-α (already mapped) astrocytopathic cascade of NMO.
- `connects-to` → **[Phosphorus](../../02-atomic/phosphorus/README.md)** — NMO phosphorus: phosphorus, as ATP precursor in neurons (already mapped) and macrophages (already mapped), supports astrocyte (already mapped) energy; phosphorus deficiency amplifies the NF-κB (already mapped) and IL-6 (already mapped) pro-inflammatory cascade of NMO.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — NMO iron: iron, as cofactor of cytochrome c in astrocytes (already mapped) and macrophages (already mapped), supports mitochondrial function; iron deficiency amplifies the NF-κB (already mapped) and TNF-α (already mapped) inflammatory cascade of NMO.
- `connects-to` → **[Chloride](../../02-atomic/chloride/README.md)** — NMO chloride: chloride channels regulate macrophage (already mapped) and mast-cell (already mapped) ion homeostasis at the blood-brain barrier; chloride imbalance amplifies NF-κB (already mapped) and IL-6 (already mapped) astrocytopathic cascade of NMO.
- `connects-to` → **[Nitrogen](../../02-atomic/nitrogen/README.md)** — NMO nitrogen: nitrogen, as nitric oxide in astrocytes (already mapped) and macrophages (already mapped), drives CNS inflammatory stress; nitrogen dysregulation amplifies NF-κB (already mapped) and TNF-α (already mapped) and IL-6 (already mapped) cascade of NMO.
- `connects-to` → **[Carbon](../../02-atomic/carbon/README.md)** — NMO carbon: carbon as backbone of AQP4 (already mapped) and NF-κB (already mapped) proteins in astrocytes (already mapped) sustains blood-brain barrier integrity; carbon depletion amplifies NF-κB (already mapped) and IL-6 (already mapped) astrocytopathic cascade of NMO.
- `connects-to` → **[Hydrogen](../../02-atomic/hydrogen/README.md)** — NMO hydrogen: hydrogen, via redox homeostasis in astrocytes (already mapped) and macrophages (already mapped), supports AQP4 (already mapped) channel function; hydrogen dysregulation amplifies NF-κB (already mapped) and TNF-α (already mapped) astrocytopathic cascade of NMO.
- `connects-to` → **[Oxygen](../../02-atomic/oxygen/README.md)** — NMO oxygen: mitochondrial oxygen sustains ATP in astrocytes (already mapped) and oligodendrocytes (already mapped) for AQP4 (already mapped) channel homeostasis; hypoxia amplifies NF-κB (already mapped) and IL-6 (already mapped) demyelinating cascade of NMO.
- `connects-to` → **[Sulfur](../../02-atomic/sulfur/README.md)** — NMO sulfur: sulfur in cysteine residues of AQP4 (already mapped) and complement proteins in astrocytes (already mapped) sustains blood-brain barrier integrity; sulfur depletion amplifies NF-κB (already mapped) and IL-6 (already mapped) astrocytopathic cascade of NMO.
- `connects-to` → **[GLP-1](../../03-molecular/glp-1/README.md)** — NMO GLP-1: GLP-1 receptor agonism on astrocytes (already mapped) and macrophages (already mapped) modulates neuroinflammatory AQP4 autoimmune cascade; GLP-1 deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) demyelinating cascade of NMO.
- `connects-to` → **[Angiotensin-II](../../03-molecular/angiotensin-ii/README.md)** — NMO angiotensin-II: angiotensin-II via AT1R on astrocytes (already mapped) and macrophages (already mapped) drives blood-brain barrier disruption and AQP4 complement attack; angiotensin-II excess amplifies NF-κB (already mapped) and IL-6 (already mapped) cascade of NMO.
- `connects-to` → **[WNT-β-catenin](../../03-molecular/wnt-beta-catenin/README.md)** — NMO wnt-beta-catenin: WNT/β-catenin on astrocytes (already mapped) and macrophages (already mapped) regulates AQP4 neuroinflammation; wnt-beta-catenin dysregulation amplifies nf-kb (already mapped) and il-6 (already mapped) and tnf-alpha (already mapped) cascade of NMO.
- `connects-to` → **[RANKL](../../03-molecular/rankl/README.md)** — NMO rankl: RANKL from macrophages (already mapped) and astrocytes (already mapped) promotes AQP4-mediated CNS immune evasion; rankl excess amplifies nf-kb (already mapped) and il-6 (already mapped) and tnf-alpha (already mapped) cascade of NMO.
- `connects-to` → **[SMAD4](../../03-molecular/smad4/README.md)** — NMO smad4: SMAD4 in astrocytes (already mapped) and macrophages (already mapped) mediates TGF-β neuroinflammatory repair; smad4 dysregulation amplifies nf-kb (already mapped) and il-6 (already mapped) and tnf-alpha (already mapped) cascade of NMO.
- `connects-to` → **[Fibronectin](../../03-molecular/fibronectin/README.md)** — NMO fibronectin: fibronectin in astrocytes (already mapped) and macrophages (already mapped) promotes CNS ECM remodelling in NMOSD; fibronectin excess amplifies nf-kb (already mapped) and il-6 (already mapped) and tnf-alpha (already mapped) cascade of NMO.
- `connects-to` → **[NOTCH](../../03-molecular/notch/README.md)** — NMO notch: Notch signalling in astrocytes (already mapped) and macrophages (already mapped) regulates glial fate in NMOSD; notch dysregulation amplifies nf-kb (already mapped) and il-6 (already mapped) and tnf-alpha (already mapped) cascade of NMO.
- `connects-to` → **[IGF-1](../../03-molecular/igf-1/README.md)** — NMO igf-1: IGF-1 from astrocytes (already mapped) and macrophages (already mapped) promotes neuroprotective repair in NMOSD; igf-1 dysregulation amplifies nf-kb (already mapped) and il-6 (already mapped) and tnf-alpha (already mapped) cascade of NMO.
- `connects-to` → **[Activin-A](../../03-molecular/activin-a/README.md)** — NMO activin-a: activin-A from astrocytes (already mapped) and macrophages (already mapped) modulates CNS neuroinflammatory tone; activin-a excess amplifies nf-kb (already mapped) and il-6 (already mapped) and tnf-alpha (already mapped) cascade of NMO.
- `connects-to` → **[Calcitonin](../../03-molecular/calcitonin/README.md)** — NMO calcitonin: calcitonin from astrocytes (already mapped) and macrophages (already mapped) modulates CNS calcium balance; calcitonin excess amplifies nf-kb (already mapped) and il-6 (already mapped) and tnf-alpha (already mapped) cascade of NMO.
- `connects-to` → **[CGRP](../../03-molecular/cgrp/README.md)** — NMO cgrp: CGRP from astrocytes (already mapped) and macrophages (already mapped) modulates CNS neuroimmune tone; cgrp excess amplifies nf-kb (already mapped) and il-6 (already mapped) and tnf-alpha (already mapped) cascade of NMO.

[^wingerchuk-2015-nmosd-criteria]: Wingerchuk DM, Banwell B, Bennett JL, et al. International consensus diagnostic criteria for neuromyelitis optica spectrum disorders. *Neurology.* 2015;85(2):177-189. [doi:10.1212/WNL.0000000000001729](https://doi.org/10.1212/WNL.0000000000001729) · [PubMed 26092914](https://pubmed.ncbi.nlm.nih.gov/26092914/)
[^pittock-2019-eculizumab-prevent]: Pittock SJ, Berthele A, Fujihara K, et al. Eculizumab in Aquaporin-4-Positive Neuromyelitis Optica Spectrum Disorder. *N Engl J Med.* 2019;381(7):614-625. [doi:10.1056/NEJMoa1900866](https://doi.org/10.1056/NEJMoa1900866) · [PubMed 31050279](https://pubmed.ncbi.nlm.nih.gov/31050279/)
[^cree-2019-inebilizumab-nmomentum]: Cree BAC, Bennett JL, Kim HJ, et al. Inebilizumab for the treatment of neuromyelitis optica spectrum disorder (N-MOmentum). *Lancet.* 2019;394(10206):1352-1363. [doi:10.1016/S0140-6736(19)31817-3](https://doi.org/10.1016/S0140-6736(19)31817-3) · [PubMed 31495497](https://pubmed.ncbi.nlm.nih.gov/31495497/)
[^yamamura-2020-satralizumab-sakurastar]: Yamamura T, Kleiter I, Fujihara K, et al. Trial of Satralizumab in Neuromyelitis Optica Spectrum Disorder. *N Engl J Med.* 2019;381(22):2114-2124. [doi:10.1056/NEJMoa1901747](https://doi.org/10.1056/NEJMoa1901747) · [PubMed 31774951](https://pubmed.ncbi.nlm.nih.gov/31774951/)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
