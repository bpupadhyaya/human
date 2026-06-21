---
schema: human-scale-entry/v1
id: prurigo-nodularis
name: Prurigo Nodularis
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-07
summary: "Prurigo nodularis is a chronic neuro-inflammatory skin disease with hyperkeratotic nodules driven by an itch-scratch cycle; Th2/Th22 inflammation and IL-31/IL-4/IL-13 signaling; nemolizumab (anti-IL-31RA) and dupilumab (anti-IL-4Rα) are FDA-approved treatments."
aliases: ["PN", "prurigo nodularis Hyde", "nodular prurigo", "chronic prurigo", "lichen obtusus"]
sources:
  - id: stander-2020-nemolizumab-pn
    type: peer-reviewed
    cite: "Ständer S, Yosipovitch G, Legat FJ, et al. Trial of nemolizumab in moderate-to-severe prurigo nodularis. N Engl J Med. 2020;382(8):706-716."
    doi: "10.1056/NEJMoa1908316"
    pmid: "32053299"
    url: "https://doi.org/10.1056/NEJMoa1908316"
  - id: briggs-2022-dupilumab-pn-liberty
    type: peer-reviewed
    cite: "Briggs JN, Cho YY, Khanna R, et al. Dupilumab for prurigo nodularis: the LIBERTY-PN PRIME and PRIME2 trials. N Engl J Med. 2022;387(18):1683-1693."
    doi: "10.1056/NEJMoa2205093"
    pmid: "36300905"
    url: "https://doi.org/10.1056/NEJMoa2205093"
cross_links:
  - target: 01-human/03-molecular/il-31
    relation: connects-to
    note: "IL-31 from Th2 cells/mast cells → IL-31RA on sensory DRG neurons → JAK1 → TRPV1/TRPA1 sensitization → itch → scratching → nodule formation; nemolizumab (anti-IL-31RA, 30 mg SC Q4W) → IGA success 26% vs. 0% and NRS itch reduction 58% vs. 16% (OLYMPIA 2)."
  - target: 01-human/07-system/atopic-dermatitis
    relation: connects-to
    note: "PN and AD share Th2/Th22 axis and IL-4/IL-13/IL-31 milieu; ~50-70% of PN patients have comorbid or preceding AD; dupilumab (approved for both PN and AD) targets shared IL-4Rα; PN nodules have more fibrotic stroma and denser neural proliferation than AD plaques."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "IL-4 and IL-13 drive Th2 polarization in PN skin; dupilumab (anti-IL-4Rα) reduces IGA success 37% vs. 22% and NRS itch ≥4 response 60% vs. 18% (LIBERTY-PN PRIME2); Th2 cytokines suppress periostin and collagen crosslinking → paradoxically fibrotic nodule response."
  - target: 01-human/03-molecular/tslp
    relation: connects-to
    note: "TSLP from stressed keratinocytes activates ILC2 and mast cells → IL-31, IL-4, IL-13 → Th2 polarization in PN; TSLP directly gates TRPA1 on C-fiber pruriceptors → immediate itch; tezepelumab (anti-TSLP) is under investigation for PN; TSLP is elevated in PN nodule biopsies."
  - target: 01-human/03-molecular/substance-p
    relation: connects-to
    note: "Substance P (SP) from CGRP+/SP+ dermal nerve fibers in PN nodules → NK1R (neurokinin 1 receptor) on mast cells and keratinocytes → histamine/tryptase release and TSLP secretion → itch amplification; aprepitant (oral NK1R antagonist) reduces PN pruritus in open-label studies."
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "CKD-associated pruritus (formerly uremic pruritus) causes PN-like nodules in dialysis patients; uremic toxins activate μ-opioid and κ-opioid receptors on pruriceptors; difelikefalin (κ-opioid agonist; FDA 2021 for CKD-aP on HD) reduces itch and may prevent PN nodule formation."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "Prurigo nodularis is a skin disease built by scratching: relentless itch drives mechanical trauma that, over weeks, raises firm hyperkeratotic nodules with thickened epidermis, dense dermal fibrosis, and — distinctively — a proliferation of nerve fibers within the skin."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "Prurigo nodularis is as much a neural as an inflammatory disease: sensory neurons proliferate in the nodules and their itch channels (TRPV1/TRPA1) are sensitized by IL-31, TSLP, and NGF, while repeated firing drives spinal central sensitization so that even light touch itches."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "Mast cells sit at the heart of the prurigo-nodularis itch loop: substance P from dermal nerves triggers them through NK1R to release histamine, tryptase, and TSLP, and they are a source of IL-31 — feeding the sensory neurons that drive scratching."
  - target: 01-human/07-system/neuropathic-pain
    relation: connects-to
    note: "Prurigo nodularis is a neuroimmune disorder straddling itch and pain: chronic scratching and a sensitized cutaneous nerve network (raised substance P and NGF) drive itch through the same peripheral and central sensitization as neuropathic pain, and both respond to gabapentinoids."
  - target: 01-human/07-system/psoriasis
    relation: connects-to
    note: "Prurigo nodularis and psoriasis are both chronic inflammatory skin diseases with thickened plaques/nodules but differ immunologically: PN is itch-dominant and Th2/IL-31-driven (dupilumab, nemolizumab), psoriasis Th17/IL-17-driven; distinguishing them guides biologic choice."
  - target: 01-human/07-system/hiv-aids
    relation: connects-to
    note: "Prurigo nodularis is a recognized cutaneous marker of HIV/AIDS: it is far more common and severe in people with HIV, especially at low CD4 counts, as part of HIV-associated pruritus; its appearance can prompt HIV testing, and antiretroviral immune restoration often improves it."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "Prurigo nodularis is driven by a type-2 (Th2) immune response: Th2 cytokines IL-4, IL-13, and especially IL-31 from helper T cells fuel the intense itch and nodule formation, which is why the IL-4/13 blocker dupilumab and IL-31 inhibitors are effective new treatments."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "Prurigo nodularis and depression are bidirectionally entwined: relentless itch and disfiguring nodules cause sleep loss and depression, while depression lowers the itch threshold and fuels scratching—so the itch-scratch cycle and mood disorder reinforce each other."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "Dendritic cells help orchestrate the neuroimmune itch of prurigo nodularis: dermal dendritic cells present antigen and amplify the Th2 response that, with sensory nerves and mast cells, sustains chronic itch—part of the skin-immune-nerve crosstalk behind the nodules."
  - target: 01-human/03-molecular/histamine
    relation: connects-to
    note: "Histamine is the classic itch mediator, but prurigo nodularis itch is largely non-histaminergic: driven by IL-31, substance P and nerve sensitization rather than mast-cell histamine, which is why antihistamines usually fail and IL-31/Th2-targeted drugs work."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "IL-13 helps drive prurigo nodularis: this type 2 cytokine, alongside IL-4 and IL-31, sustains the itch and skin inflammation, which is why dupilumab (blocking IL-4/IL-13 signaling) is now an approved, effective therapy for the disease."
  - target: 01-human/07-system/insomnia-disorder
    relation: connects-to
    note: "Prurigo nodularis devastates sleep: relentless nocturnal itch and scratching fragment sleep, and the resulting insomnia worsens itch perception and mood—a vicious itch-scratch-sleep cycle that makes the disease far more disabling than the skin lesions alone suggest."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "JAK inhibition is an emerging treatment for prurigo nodularis: the itch-driving cytokines IL-31, IL-4 and IL-13 signal through JAK, so JAK inhibitors (and the IL-4/13 blocker dupilumab) can break the itch-scratch cycle that perpetuates the nodules."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "Prurigo nodularis is a disease of the integumentary system gone into an itch-scratch loop: chronic scratching thickens skin into hard nodules dense with nerve fibers and immune cells, so the skin's neuroimmune wiring sustains the disease."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "Prurigo nodularis sits at the skin-nerve interface: sensitized cutaneous nerve fibers and central itch pathways amplify pruritus, so it behaves partly like neuropathic itch—why neuromodulators like gabapentinoids help alongside anti-inflammatory drugs."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "Liver disease can drive prurigo nodularis: cholestasis (as in primary biliary cholangitis) causes intense, intractable itch, and the repeated scratching of that itch builds the hard nodules—so unexplained prurigo prompts a check of liver and bile function."
  - target: 01-human/07-system/hodgkin-lymphoma
    relation: connects-to
    note: "Relentless itch can herald lymphoma: Hodgkin lymphoma classically causes paraneoplastic pruritus, and prurigo nodularis appearing without clear cause warrants screening for underlying malignancy—so the skin sometimes signals a hidden cancer."
  - target: 01-human/04-cellular/fibroblast
    relation: connects-to
    note: "The nodule in prurigo nodularis is built by fibroblasts: relentless scratching drives dermal fibroblast proliferation and collagen deposition, thickening the skin into the hard, dome-shaped nodules—so chronic mechanical trauma, not just inflammation, sculpts the lesion."
  - target: 01-human/03-molecular/mu-opioid-receptor
    relation: connects-to
    note: "Prurigo nodularis itch runs through the opioid system: an imbalance of mu (itch-promoting) versus kappa opioid signaling drives chronic itch, so the kappa-agonist difelikefalin and opioid-modulating drugs are used to break the itch-scratch cycle."
  - target: 01-human/06-organ/thyroid
    relation: connects-to
    note: "Chronic itch like prurigo nodularis can signal the thyroid: thyroid dysfunction causes generalized pruritus, so evaluating PN includes checking the thyroid (and kidney, liver) for a systemic cause behind the relentless itching."
  - target: 01-human/07-system/type-2-diabetes
    relation: connects-to
    note: "Chronic itch drives prurigo nodularis, and diabetes is a common systemic trigger: diabetic neuropathy and metabolic skin changes cause itch that, when scratched, builds nodules—so screening for diabetes joins thyroid, kidney and liver in the PN workup."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "Prurigo nodularis is not purely a Th2 disease: alongside the itch cytokines, a Th17 component with IL-17 adds to the skin inflammation, broadening the immune picture and the rationale for targeting multiple cytokine pathways."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: connects-to
    note: "Weak regulatory T-cell control lets prurigo nodularis smolder: reduced Treg restraint allows the itch-driving inflammation to persist, so the failure to switch off the immune and scratch response helps the nodules entrench."
  - target: 01-human/03-molecular/collagen
    relation: connects-to
    note: "Prurigo nodularis nodules are built of collagen: relentless scratching drives fibroblasts to pile up collagen, thickening the dermis into the firm, raised lumps that define the disease and outlast the original itch trigger."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Light can calm prurigo nodularis: narrowband UVB phototherapy uses controlled photons to dampen the skin's inflammation and itch nerves, shrinking nodules in stubborn cases."
  - target: 01-human/05-tissue/fibrosis
    relation: connects-to
    note: "Prurigo nodularis nodules are scratch-driven fibrosis: relentless scratching pushes fibroblasts to lay down dense collagen, scarring the dermis into the firm lumps that persist long after the original itch."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "Failing kidneys can ignite prurigo nodularis: uremic pruritus from chronic kidney disease is a major itch trigger, and the relentless scratching it provokes builds the nodules."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Iron deficiency can itch: low iron is a recognized cause of generalized pruritus that, when scratched, seeds prurigo nodules, so checking iron is part of the workup for unexplained itch."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "Chronic itch becomes wired in the brain: central sensitization of itch-processing pathways keeps prurigo nodularis itching even after skin triggers fade, and its heavy depression burden reflects this brain involvement."
  - target: 01-human/05-tissue/peripheral-nerve
    relation: connects-to
    note: "Prurigo nodules sprout extra nerve fibers: the dermal peripheral nerves proliferate and sensitize, so the lumps themselves become itch generators that lock in the scratch-itch cycle."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy reveals the nodule's nerve overgrowth: the thickened skin teems with proliferated dermal nerve endings and degranulating mast cells alongside it, the cellular machinery that turns a scratch into a self-sustaining itch."
  - target: 03-medicine/03-food/vitamin-d
    relation: connects-to
    note: "Vitamin D deficiency stokes the itch: low levels are common in chronic pruritus and prurigo, and the vitamin's role in skin-barrier repair and immune regulation has made supplementation a studied adjunct."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "Zinc shortage can drive itchy skin: deficiency produces a scaly, itch-prone dermatitis and impairs barrier repair, so correcting low zinc is part of addressing the relentless scratching behind prurigo."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "Prurigo's breakthrough treatments are antibodies: dupilumab blocks IL-4/IL-13 signaling and nemolizumab the itch cytokine IL-31's receptor, monoclonal antibodies that finally break the itch-scratch cycle that topical steroids could not."
  - target: 01-human/06-organ/eye
    relation: connects-to
    note: "The biologics bring an ocular catch: dupilumab, used for prurigo and atopic disease, commonly causes conjunctivitis, so a red, irritated eye is a side effect watched for during treatment."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "Relentless scratching breaches the barrier: the excoriated nodules become impetiginized, drawing neutrophils as secondary bacterial infection sets in — a complication that itself worsens the itch."
  - target: 01-human/03-molecular/endocannabinoid
    relation: connects-to
    note: "The endocannabinoid system can dial down itch: cannabinoid receptors on skin nerves and immune cells modulate the itch signal, so topical and systemic cannabinoids are studied as antipruritics for the relentless scratching of prurigo."
  - target: 01-human/07-system/gut-microbiome
    relation: connects-to
    note: "A gut-skin axis may feed the itch: dysbiosis and altered microbial metabolites shape the systemic inflammation behind chronic pruritic skin disease, tying the gut to the neuroimmune itch of prurigo nodularis."
  - target: 01-human/04-cellular/erythrocyte
    relation: connects-to
    note: "Relentless itch can signal the blood: polycythemia vera and iron deficiency are recognized systemic causes of chronic pruritus, so a blood disorder is sought when scratching builds prurigo nodules without an obvious skin cause."
  - target: 01-human/07-system/hepatitis-c
    relation: connects-to
    note: "Chronic infection can itch the skin into nodules: hepatitis C and the cholestatic liver disease it causes are recognized systemic drivers of pruritus, so an unexplained prurigo nodularis prompts a look at the liver and a viral screen."
  - target: 01-human/03-molecular/cgrp
    relation: connects-to
    note: "Sensory nerves inflame their own territory: CGRP released from the skin's itch fibers drives the neurogenic inflammation and nerve sensitization that, with chronic scratching, build the thickened nodules of the disease."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Macrophages help build the nodule: drawn into the lesion, they sustain the type-2 and neuroimmune inflammation and the fibrosis that hardens prurigo nodularis into its characteristic firm bumps."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Eosinophils answer IL-5 in the nodule: this type-2 cytokine recruits and activates the eosinophils found in prurigo lesions, part of the Th2 milieu that anti-type-2 biologics aim to quiet."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "A damaged skin barrier releases IL-33: this alarmin from stressed keratinocytes ignites the type-2 and neuroimmune cascade, both amplifying itch-driving sensory nerves and the Th2 inflammation that builds prurigo nodules."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "The itch-scratch cycle and the mind feed each other: the relentless pruritus of prurigo nodularis drives anxiety and sleep loss, while stress lowers the itch threshold — a psychodermatologic loop that worsens both conditions."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "The itch cytokines all funnel through JAK-STAT3: IL-31, IL-13 and IL-4 signal via STAT3 in sensory neurons and immune cells to drive pruritus and nodule formation, which is why JAK inhibitors quiet prurigo nodularis."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "Chronic scratching and inflammation feed NF-κB: repeated skin trauma and type-2 cytokines activate NF-κB in keratinocytes and immune cells, sustaining the inflammation that thickens the nodules of the disease."
  - target: 01-human/07-system/opioid-use-disorder
    relation: connects-to
    note: "Opioids and itch are entwined: chronic opioid use causes pruritus that can drive a prurigo-like picture through the mu-opioid system, while kappa-opioid-modulating drugs are used to treat the intractable itch."
  - target: 01-human/07-system/hiv
    relation: connects-to
    note: "It can be a marker of HIV: severe, treatment-resistant prurigo nodularis is a recognized cutaneous sign of HIV, the immune dysregulation amplifying the itch-scratch cycle, sometimes prompting HIV testing."
  - target: 01-human/07-system/obsessive-compulsive-disorder
    relation: connects-to
    note: "The scratching can take on a compulsive quality: the relentless itch-scratch cycle of prurigo nodularis overlaps with skin-picking and obsessive-compulsive-spectrum behavior, each reinforcing the other."
  - target: 01-human/07-system/hcc
    relation: connects-to
    note: "Cholestatic liver disease drives the itch: bile-salt retention from advanced liver disease and biliary obstruction in hepatocellular carcinoma causes intense pruritus that can manifest as prurigo nodularis."
  - target: 02-pathogen/02-bacteria/staphylococcus-aureus
    relation: connects-to
    note: "Relentless scratching opens the skin to Staph: the excoriated nodules of prurigo nodularis are repeatedly broken open, readily colonized and infected by Staphylococcus aureus, which in turn intensifies the itch."
  - target: 01-human/07-system/wound-healing
    relation: connects-to
    note: "Constant scratching defeats repair: the compulsive scratching of prurigo nodularis reopens lesions faster than they can heal, perpetuating the thickened, eroded nodules in an itch-scratch cycle."
  - target: 01-human/07-system/dlbcl
    relation: connects-to
    note: "Severe itch can flag a lymphoma: persistent prurigo nodularis is a recognized paraneoplastic sign of underlying lymphoma, prompting evaluation for Hodgkin and non-Hodgkin lymphomas such as DLBCL."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "It is a neuroimmune itch disorder: prurigo nodularis is driven by Th2 cytokines and IL-31 sensitising itch nerves, which is why the immune-targeting biologic dupilumab is now an effective treatment."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "Endocrine disease can drive the itch: thyroid dysfunction and diabetes are among the systemic causes of the chronic pruritus that seeds prurigo nodularis, so endocrine screening is part of its work-up."
  - target: 01-human/07-system/iron-deficiency-anemia
    relation: connects-to
    note: "Low iron can itch: iron deficiency is a recognised systemic cause of generalised pruritus, and correcting it can relieve the itch that perpetuates prurigo nodularis."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "It shares the atopic, type-2 inflammatory pathway: prurigo nodularis is enriched for atopy and asthma, and the IL-4/IL-13 axis it shares with airway disease is why dupilumab treats both."
  - target: 01-human/07-system/lymphatic-system
    relation: connects-to
    note: "Relentless itch can flag a lymphoma: severe chronic pruritus and prurigo nodularis can be a paraneoplastic sign of Hodgkin and other lymphomas, prompting nodal examination and screening."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "Pregnancy complicates its itch and care: chronic pruritus can flare in pregnancy, where the systemic immunomodulators used for prurigo nodularis are restricted, limiting treatment options."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "Liver and bile drive the itch: cholestatic liver disease floods the skin with bile salts and pruritogens, a systemic cause of the relentless itch that builds prurigo nodularis."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "Chronic inflammatory skin disease tracks with cardiovascular risk: like psoriasis and atopic dermatitis, severe prurigo nodularis is associated with a higher burden of cardiovascular and metabolic comorbidity."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "Its strong systemic treatments cost the skeleton: prolonged corticosteroids and immunosuppressants used for severe refractory prurigo nodularis drive bone loss and muscle weakness."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "Kidney failure drives the itch: chronic kidney disease causes uraemic pruritus that can evolve into prurigo nodularis, one of the strongest systemic associations of the condition."
  - target: 03-medicine/01-modern/02-respiratory/corticosteroids
    relation: connects-to
    note: "First-line calms the nodule: potent topical and intralesional corticosteroids reduce the inflammation and itch of prurigo nodularis, used before stepping up to biologics like dupilumab."
  - target: 01-human/07-system/cholangiocarcinoma
    relation: connects-to
    note: "Cholestatic itch can underlie it: bile-duct obstruction from cholangiocarcinoma causes intense cholestatic pruritus, and the relentless scratching it provokes can produce prurigo nodularis."
  - target: 03-medicine/01-modern/13-cancer/targeted-therapy
    relation: connects-to
    note: "Type-2 and itch cytokines are the targets: dupilumab against IL-4Rα and nemolizumab against the IL-31 receptor — the 'itch cytokine' — are the first approved biologics for prurigo nodularis, with JAK inhibitors close behind."
  - target: 03-medicine/01-modern/13-cancer/cancer-chemotherapy
    relation: connects-to
    note: "It can be a paraneoplastic clue: severe new prurigo nodularis can herald an underlying lymphoma or solid cancer, where treating the malignancy with chemotherapy resolves the otherwise refractory itch."
  - target: 01-human/07-system/dermatomyositis
    relation: connects-to
    note: "Another intensely itchy dermatosis: like prurigo nodularis, dermatomyositis causes severe pruritus and can be paraneoplastic, both reminding clinicians that relentless itch may signal systemic or malignant disease."
  - target: 01-human/07-system/asthma
    relation: connects-to
    note: "Type-2 atopy connection: prurigo nodularis shares the IL-4/IL-13 type-2 inflammation of asthma and atopic disease, and the anti-IL-4-receptor biologic dupilumab treats both conditions."
  - target: 01-human/07-system/polycythemia-vera
    relation: connects-to
    note: "Itch from the blood: aquagenic pruritus is a classic feature of polycythaemia vera, and relentless scratching can raise prurigo-like nodules—severe itch as a clue to a myeloproliferative cause."
  - target: 01-human/03-molecular/bdnf
    relation: connects-to
    note: "Neurotrophins and the itch nerve: BDNF and nerve growth factor drive the dermal nerve-fibre hyperplasia and neuronal sensitisation that make prurigo nodularis so intensely and persistently itchy."
  - target: 01-human/07-system/myelofibrosis
    relation: connects-to
    note: "Myeloproliferative itch: like polycythaemia vera, myelofibrosis causes severe aquagenic and chronic pruritus that can drive prurigo nodularis, the itch a clue to an underlying myeloproliferative neoplasm."
  - target: 01-human/07-system/pancreatic-cancer
    relation: connects-to
    note: "Cholestatic and paraneoplastic itch: a pancreatic head cancer obstructing the bile duct causes intense cholestatic pruritus, and generalised itch can be a paraneoplastic clue presenting as prurigo nodularis."
  - target: 01-human/07-system/ptsd
    relation: connects-to
    note: "The psychodermatology link: prurigo nodularis is strongly tied to anxiety, depression and trauma (PTSD), the itch-scratch cycle both worsened by and worsening psychological distress."
  - target: 01-human/07-system/ptcl
    relation: connects-to
    note: "A malignant itch to exclude: cutaneous T-cell lymphoma (mycosis fungoides) is intensely pruritic and can produce prurigo-like nodules, a malignant mimic of prurigo nodularis warranting biopsy in atypical cases."
  - target: 01-human/07-system/social-anxiety-disorder
    relation: connects-to
    note: "The visible, stigmatising lesions: the excoriated nodules of prurigo nodularis are disfiguring and carry social stigma, driving social anxiety and avoidance much as other visible skin diseases do."
  - target: 01-human/07-system/covid-19-disease
    relation: connects-to
    note: "Stress and post-viral itch: pandemic stress worsened the itch-scratch cycle, and chronic pruritus has been reported as a post-COVID symptom, flaring prurigo nodularis."
  - target: 01-human/03-molecular/periostin
    relation: connects-to
    note: "Type-2 matrix signal: periostin, induced by IL-4 and IL-13, deposits in the dermis of prurigo nodularis and directly activates sensory neurons to amplify the itch-scratch cycle."
  - target: 01-human/03-molecular/tnf-alpha
    relation: connects-to
    note: "Mixed inflammation: TNF-α contributes to the mixed Th2/Th17/Th22 inflammatory milieu of prurigo nodularis lesions, sustaining the chronic skin inflammation behind the nodules."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "Fibrosis and itch: IL-6 promotes the dermal fibrosis and neural proliferation of prurigo nodularis nodules, linking chronic inflammation to the thickened, intensely itchy lesions."
  - target: 01-human/03-molecular/ccl2
    relation: connects-to
    note: "Myeloid recruitment: CCL2 draws monocytes and macrophages into prurigo nodularis lesions, sustaining the dermal inflammatory infiltrate that feeds the itch-scratch cycle and nodule formation."
  - target: 01-human/03-molecular/pdgf
    relation: connects-to
    note: "Nodule fibroblasts: PDGF drives the dermal fibroblast proliferation that builds the firm, hyperplastic nodules of prurigo nodularis, the structural correlate of the chronic scratching."
  - target: 01-human/03-molecular/serotonin
    relation: connects-to
    note: "Systemic pruritus pathway: serotonin contributes to the itch of the uraemic and cholestatic conditions that underlie many cases of prurigo nodularis, the rationale for 5-HT3-antagonist antipruritics."
  - target: 01-human/03-molecular/ntrk
    relation: connects-to
    note: "Neural hyperplasia: nerve growth factor signalling through TrkA drives the dermal nerve-fibre proliferation characteristic of prurigo nodularis, sensitising the skin and perpetuating the chronic itch-scratch cycle."
  - target: 01-human/03-molecular/kit
    relation: connects-to
    note: "Mast-cell involvement: KIT-dependent mast cells accumulate in prurigo nodularis lesions, releasing pruritogens and neuropeptides that feed the neuroimmune itch and the dermal inflammatory infiltrate."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "Innate amplification: IL-1β from activated keratinocytes and myeloid cells adds an innate inflammatory arm to the dominant type-2 cytokine response in prurigo nodularis lesions, reinforcing the chronic inflammation."
---

# Prurigo Nodularis

## Overview

**Prurigo nodularis (PN)** is a chronic, intensely pruritic neuro-inflammatory skin disease characterized by symmetrically distributed, firm, **hyperkeratotic nodules** — typically 1–3 cm in diameter — scattered predominantly on the extensor surfaces of the extremities, trunk, and occasionally the face and scalp. The defining clinical feature is an **itch-scratch-inflammation cycle**: intense pruritus (often rated 8-10/10) drives compulsive scratching → mechanical trauma to skin → inflammation → more pruritus → more scratching → formation of fibrotic, hyperkeratotic nodules [^stander-2020-nemolizumab-pn].

PN was historically considered a rare, treatment-refractory condition with limited pharmacological options (topical steroids, tacrolimus, thalidomide, gabapentin — all with modest efficacy). The discovery that PN shares the **Th2/Th22 inflammatory signature** of atopic dermatitis — with IL-4, IL-13, IL-31, and IL-22 as dominant cytokines — transformed PN into a therapeutically actionable target. Two biologics are now FDA approved:
- **Nemolizumab** (anti-IL-31RA, August 2023): first-in-class itch-specific therapy; first drug specifically approved for PN
- **Dupilumab** (anti-IL-4Rα, September 2022): IL-4/IL-13 dual blockade; broader anti-inflammatory mechanism

PN affects approximately **72,000 patients** in the US; true prevalence is likely underestimated due to historical lack of diagnostic criteria and treatment nihilism. It causes severe quality of life impairment (sleep disruption, anxiety, depression, social withdrawal) disproportionate even to other chronic pruritic diseases.

**Epidemiology and risk factors:**
- Median age of onset ~50 years; but can occur at any age; slight female predominance
- **Skin of color disproportionately affected:** African American patients have ~3-4× higher prevalence than White patients; more common in lower socioeconomic settings; historically undertreated and underdiagnosed in this population
- **Strong association with atopic dermatitis:** 50-70% of PN patients have personal or family history of AD; PN can represent a chronic neurologically driven phase of AD in which itch becomes deeply ingrained via central sensitization
- **Comorbidities:** CKD (uremic pruritus → PN-like nodules), HIV (immune dysregulation), hepatic disease (cholestatic pruritus), thyroid disease, hematologic malignancy (CTCL, lymphoma — must exclude), psychiatric conditions (OCD, anxiety, body dysmorphic disorder)

## Structure

**Nodule histopathology:**
- **Epidermis:** Marked irregular acanthosis (epidermal thickening), hypergranulosis, compact orthokeratotic or parakeratotic hyperkeratosis; "pseudoepitheliomatous hyperplasia" pattern mimicking squamous cell carcinoma; keratinocyte hyperproliferation (Ki67⁺)
- **Dermis:** Dense superficial and deep mixed inflammatory infiltrate (eosinophils, mast cells, CD4⁺ Th2 T cells, Th22 T cells, macrophages); **neural proliferation** — increased nerve fiber density (PGP9.5⁺ nerve fibers), thickened nerve bundles (Schwann cell proliferation), TRPV1⁺/CGRP⁺/Substance P⁺ fibers; fibroblast activation → **stellate fibrosis** (dense dermal fibrosis with fibroblast/myofibroblast cords — the fibrous "core" of nodules)
- **Cytokine milieu:** IL-4, IL-13, IL-31 (dominant in Th2 infiltrate); IL-22, IL-17A (Th22/Th17 minority component); TSLP and IL-33 from keratinocytes → ILC2 activation → further IL-31 production; TNF-α and IL-1β from macrophages → inflammation perpetuation
- **Neural sensitization:** IL-31 + TSLP + NGF (nerve growth factor) → upregulate TRPV1, TRPA1, and IL-31RA on pruriceptors; decreased threshold for itch signals; central sensitization (spinal cord wind-up) → allodynia (itch from normally non-pruritic stimuli like light touch)

**Itch-scratch cycle biology:**
- **Peripheral sensitization:** Damaged keratinocytes → HMGB1, ATP, IL-33 → mast cell/ILC2 activation → IL-31, histamine, tryptase release → C-fiber sensitization
- **Central sensitization (spinal):** Repeated C-fiber activation → spinal cord dorsal horn → NK1R (neurokinin 1 receptor for Substance P) → NMDA receptor activation → wind-up → long-term potentiation of itch circuits → itch without adequate peripheral stimulus
- **Psychological reinforcement:** Scratch reflex becomes automatic (habit/compulsion); limbic system involvement → scratch becomes pleasurable relief (opioid-like reward); this is why itch in PN is so refractory to peripheral anti-inflammatory therapy alone

## Function

**Diagnosis:**
- PN is clinical: ≥20 hyperkeratotic nodules of >1 cm; bilateral symmetric distribution; pruritus VAS ≥7; duration >6 weeks; exclude secondary causes (CTCL, CKD, HIV, liver disease, thyroid disease, lymphoma)
- **IFSI classification (International Forum for the Study of Itch):** Chronic prurigo of the nodular type = PN; standardized diagnostic criteria (IFSI consensus 2018)
- **Biomarkers:** Elevated serum IgE (60%), elevated eosinophil count, elevated serum IL-31 and periostin; none are diagnostic but support Th2 endotype characterization for biologic selection
- **Biopsy:** Not required for diagnosis but useful to exclude malignancy; shows characteristic pseudoepitheliomatous hyperplasia + mixed Th2 infiltrate + neural proliferation

**Disease burden:**
- **Pruritus:** Constant or near-constant itch (NRS median 8/10 in trials); nocturnal itch → severe sleep disruption → chronic sleep debt → exacerbated inflammation (cortisol dysregulation, NK cell suppression)
- **QoL:** DLQI (Dermatology Life Quality Index) scores 12-18 (severe range); comparable to severe psoriasis and systemic sclerosis; high rates of anxiety (40-60%) and depression (30-50%); social isolation, occupational dysfunction, inability to wear certain clothing
- **Treatment nihilism:** Historically, most patients received inadequate treatment due to poor understanding of disease biology; many waited >5-10 years for diagnosis; now reversing with biologic era

## Pathology

**Treatment approach:**

*Non-pharmacological:*
- **Skin barrier repair:** Emollients (reduce barrier disruption → less irritant entry → less itch); wet wrap therapy; avoidance of scratching tools (nail covers, behavioral therapy)
- **Cool compresses, distraction:** Non-pharmacological itch interruption

*Topical therapies:*
- **Topical corticosteroids (TCS):** Class I-III under occlusion; reduce inflammation within nodules; temporary relief; steroid atrophy limits use
- **Calcineurin inhibitors (tacrolimus 0.1%, pimecrolimus):** Off-label; modestly effective; no atrophy risk
- **Topical doxepin:** Antihistamine + tricyclic; applied to nodules for local itch block; modest effect

*Systemic therapies (pre-biologic era):*
- **Gabapentin/pregabalin:** α2δ-1 subunit blockers → reduce central sensitization; modest itch reduction (NRS –2 to –3); sedation limits use
- **Thalidomide:** TNF-α suppression + anti-angiogenic; effective (~50% itch reduction) but peripheral neuropathy limits use; reserved for severe refractory cases
- **Naltrexone (low-dose, 4.5 mg/day):** μ-opioid receptor blockade → reduces opioid-mediated itch reward cycle; modest evidence
- **Cyclosporine:** IL-2/T-cell suppression; off-label; nephrotoxicity limits long-term use
- **Narrow-band UVB (NB-UVB):** Induces skin immunosuppression + kills IL-31-producing T cells; 30-50% response; requires 2-3× weekly visits → poor adherence

*Biologic therapies:*

**Nemolizumab (Galderma; anti-IL-31RA) [^stander-2020-nemolizumab-pn]:**
- 30 mg SC Q4W; FDA approved August 2023 for PN in adults ≥18 years
- **OLYMPIA 2:** IGA 0/1 success 26% vs. 0% placebo; PP-NRS ≥4-point improvement 58% vs. 16% (both p<0.001); DLQI improvement –8.0 vs. –3.5; rapid onset (NRS itch reduction by week 4)
- **OLYMPIA 1:** Similar results; NRS ≥4-point improvement 56% vs. 21%
- Safety: injection site reactions; nausea; generally well tolerated; no increased infection signal
- Mechanism advantage: directly interrupts itch-scratch cycle at the neuronal level → prevents mechanical trauma → nodule regression; complementary to dupilumab (targets different pathway)

**Dupilumab (Sanofi/Regeneron; anti-IL-4Rα) [^briggs-2022-dupilumab-pn-liberty]:**
- 300 mg SC Q2W; FDA approved September 2022 for PN in adults ≥18 years
- **LIBERTY-PN PRIME2:** IGA 0/1 at 24 weeks 37% vs. 22% placebo; PP-NRS ≥4-point 60% vs. 18%
- **LIBERTY-PN PRIME:** Similar outcomes; both trials statistically significant
- Mechanism: blocks IL-4 and IL-13 via shared IL-4Rα subunit → reduces Th2 inflammation → less TSLP/IL-31 production → itch reduction; also restores barrier (indirectly)
- Shared mechanism with AD approval (dupilumab approved for AD 2017); many PN patients have comorbid AD — dupilumab treats both simultaneously

## Connections

- `connects-to` → **[IL-31](../../03-molecular/il-31/README.md)** — IL-31 from Th2 cells/mast cells → IL-31RA on sensory DRG neurons → JAK1 → TRPV1/TRPA1 sensitization → itch → scratching → nodule formation; nemolizumab (anti-IL-31RA, 30 mg SC Q4W) → IGA success 26% vs. 0% and NRS itch reduction 58% vs. 16% (OLYMPIA 2).
- `connects-to` → **[Atopic Dermatitis](../atopic-dermatitis/README.md)** — PN and AD share Th2/Th22 inflammatory axis and IL-4/IL-13/IL-31 cytokine milieu; ~50-70% of PN patients have comorbid or preceding AD; dupilumab (approved for both PN and AD) targets shared IL-4Rα; PN nodules show more fibrotic stroma and denser neural proliferation than AD plaques.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — IL-4 and IL-13 drive Th2 polarization in PN skin; dupilumab (anti-IL-4Rα blocking both IL-4 and IL-13) reduces IGA success 37% vs. 22% and NRS itch ≥4 response 60% vs. 18% (LIBERTY-PN PRIME2); Th2 cytokines suppress periostin and collagen crosslinking → paradoxically fibrotic nodule response.
- `connects-to` → **[TSLP](../../03-molecular/tslp/README.md)** — TSLP from stressed keratinocytes activates ILC2 and mast cells → IL-31, IL-4, IL-13 → Th2 polarization in PN; TSLP directly gates TRPA1 on C-fiber pruriceptors → immediate itch; tezepelumab (anti-TSLP) is under investigation for PN; TSLP is elevated in PN nodule biopsies.
- `connects-to` → **[Substance P](../../03-molecular/substance-p/README.md)** — Substance P (SP) from CGRP+/SP+ dermal nerve fibers in PN nodules → NK1R on mast cells and keratinocytes → histamine/tryptase release and TSLP secretion → itch amplification; aprepitant (oral NK1R antagonist) reduces PN pruritus in open-label studies.
- `connects-to` → **[CKD](../ckd/README.md)** — CKD-associated pruritus (formerly uremic pruritus) causes PN-like nodules in dialysis patients; uremic toxins activate μ-opioid and κ-opioid receptors on pruriceptors; difelikefalin (κ-opioid agonist; FDA 2021 for CKD-aP on HD) reduces itch and may prevent PN nodule formation.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — Prurigo nodularis is a skin disease built by scratching: relentless itch drives mechanical trauma that, over weeks, raises firm hyperkeratotic nodules with thickened epidermis, dense dermal fibrosis, and — distinctively — a proliferation of nerve fibers within the skin.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — Prurigo nodularis is as much a neural as an inflammatory disease: sensory neurons proliferate in the nodules and their itch channels (TRPV1/TRPA1) are sensitized by IL-31, TSLP, and NGF, while repeated firing drives spinal central sensitization so that even light touch itches.
- `connects-to` → **[Mast Cell](../../04-cellular/mast-cell/README.md)** — Mast cells sit at the heart of the prurigo-nodularis itch loop: substance P from dermal nerves triggers them through NK1R to release histamine, tryptase, and TSLP, and they are a source of IL-31 — feeding the sensory neurons that drive scratching.
- `connects-to` → **[Neuropathic Pain](../neuropathic-pain/README.md)** — Prurigo nodularis is a neuroimmune disorder straddling itch and pain: chronic scratching and a sensitized cutaneous nerve network (raised substance P and NGF) drive itch through the same peripheral and central sensitization as neuropathic pain, and both respond to gabapentinoids.
- `connects-to` → **[Psoriasis](../psoriasis/README.md)** — Prurigo nodularis and psoriasis are both chronic inflammatory skin diseases with thickened plaques/nodules but differ immunologically: PN is itch-dominant and Th2/IL-31-driven (dupilumab, nemolizumab), psoriasis Th17/IL-17-driven; distinguishing them guides biologic choice.
- `connects-to` → **[HIV/AIDS](../hiv-aids/README.md)** — Prurigo nodularis is a recognized cutaneous marker of HIV/AIDS: it is far more common and severe in people with HIV, especially at low CD4 counts, as part of HIV-associated pruritus; its appearance can prompt HIV testing, and antiretroviral immune restoration often improves it.
- `connects-to` → **[T Helper Cell](../../04-cellular/t-helper-cell/README.md)** — Prurigo nodularis is driven by a type-2 (Th2) immune response: Th2 cytokines IL-4, IL-13, and especially IL-31 from helper T cells fuel the intense itch and nodule formation, which is why the IL-4/13 blocker dupilumab and IL-31 inhibitors are effective new treatments.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — Prurigo nodularis and depression are bidirectionally entwined: relentless itch and disfiguring nodules cause sleep loss and depression, while depression lowers the itch threshold and fuels scratching—so the itch-scratch cycle and mood disorder reinforce each other.
- `connects-to` → **[Dendritic Cell](../../04-cellular/dendritic-cell/README.md)** — Dendritic cells help orchestrate the neuroimmune itch of prurigo nodularis: dermal dendritic cells present antigen and amplify the Th2 response that, with sensory nerves and mast cells, sustains chronic itch—part of the skin-immune-nerve crosstalk behind the nodules.
- `connects-to` → **[Histamine](../../03-molecular/histamine/README.md)** — Histamine is the classic itch mediator, but prurigo nodularis itch is largely non-histaminergic: driven by IL-31, substance P and nerve sensitization rather than mast-cell histamine, which is why antihistamines usually fail and IL-31/Th2-targeted drugs work.
- `connects-to` → **[Interleukin-13](../../03-molecular/il-13/README.md)** — IL-13 helps drive prurigo nodularis: this type 2 cytokine, alongside IL-4 and IL-31, sustains the itch and skin inflammation, which is why dupilumab (blocking IL-4/IL-13 signaling) is now an approved, effective therapy for the disease.
- `connects-to` → **[Insomnia Disorder](../insomnia-disorder/README.md)** — Prurigo nodularis devastates sleep: relentless nocturnal itch and scratching fragment sleep, and the resulting insomnia worsens itch perception and mood—a vicious itch-scratch-sleep cycle that makes the disease far more disabling than the skin lesions alone suggest.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — JAK inhibition is an emerging treatment for prurigo nodularis: the itch-driving cytokines IL-31, IL-4 and IL-13 signal through JAK, so JAK inhibitors (and the IL-4/13 blocker dupilumab) can break the itch-scratch cycle that perpetuates the nodules.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — Prurigo nodularis is a disease of the integumentary system gone into an itch-scratch loop: chronic scratching thickens skin into hard nodules dense with nerve fibers and immune cells, so the skin's neuroimmune wiring sustains the disease.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — Prurigo nodularis sits at the skin-nerve interface: sensitized cutaneous nerve fibers and central itch pathways amplify pruritus, so it behaves partly like neuropathic itch—why neuromodulators like gabapentinoids help alongside anti-inflammatory drugs.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — Liver disease can drive prurigo nodularis: cholestasis (as in primary biliary cholangitis) causes intense, intractable itch, and the repeated scratching of that itch builds the hard nodules—so unexplained prurigo prompts a check of liver and bile function.
- `connects-to` → **[Hodgkin Lymphoma](../hodgkin-lymphoma/README.md)** — Relentless itch can herald lymphoma: Hodgkin lymphoma classically causes paraneoplastic pruritus, and prurigo nodularis appearing without clear cause warrants screening for underlying malignancy—so the skin sometimes signals a hidden cancer.
- `connects-to` → **[Fibroblast](../../04-cellular/fibroblast/README.md)** — The nodule in prurigo nodularis is built by fibroblasts: relentless scratching drives dermal fibroblast proliferation and collagen deposition, thickening the skin into the hard, dome-shaped nodules—so chronic mechanical trauma, not just inflammation, sculpts the lesion.
- `connects-to` → **[Mu-Opioid Receptor](../../03-molecular/mu-opioid-receptor/README.md)** — Prurigo nodularis itch runs through the opioid system: an imbalance of mu (itch-promoting) versus kappa opioid signaling drives chronic itch, so the kappa-agonist difelikefalin and opioid-modulating drugs are used to break the itch-scratch cycle.
- `connects-to` → **[Thyroid Gland](../../06-organ/thyroid/README.md)** — Chronic itch like prurigo nodularis can signal the thyroid: thyroid dysfunction causes generalized pruritus, so evaluating PN includes checking the thyroid (and kidney, liver) for a systemic cause behind the relentless itching.
- `connects-to` → **[Type 2 Diabetes](../type-2-diabetes/README.md)** — Chronic itch drives prurigo nodularis, and diabetes is a common systemic trigger: diabetic neuropathy and metabolic skin changes cause itch that, when scratched, builds nodules—so screening for diabetes joins thyroid, kidney and liver in the PN workup.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — Prurigo nodularis is not purely a Th2 disease: alongside the itch cytokines, a Th17 component with IL-17 adds to the skin inflammation, broadening the immune picture and the rationale for targeting multiple cytokine pathways.
- `connects-to` → **[Regulatory T Cell](../../04-cellular/regulatory-t-cell/README.md)** — Weak regulatory T-cell control lets prurigo nodularis smolder: reduced Treg restraint allows the itch-driving inflammation to persist, so the failure to switch off the immune and scratch response helps the nodules entrench.
- `connects-to` → **[Collagen](../../03-molecular/collagen/README.md)** — Prurigo nodularis nodules are built of collagen: relentless scratching drives fibroblasts to pile up collagen, thickening the dermis into the firm, raised lumps that define the disease and outlast the original itch trigger.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Light can calm prurigo nodularis: narrowband UVB phototherapy uses controlled photons to dampen the skin's inflammation and itch nerves, shrinking nodules in stubborn cases.
- `connects-to` → **[Fibrosis](../../05-tissue/fibrosis/README.md)** — Prurigo nodularis nodules are scratch-driven fibrosis: relentless scratching pushes fibroblasts to lay down dense collagen, scarring the dermis into the firm lumps that persist long after the original itch.
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — Failing kidneys can ignite prurigo nodularis: uremic pruritus from chronic kidney disease is a major itch trigger, and the relentless scratching it provokes builds the nodules.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Iron deficiency can itch: low iron is a recognized cause of generalized pruritus that, when scratched, seeds prurigo nodules, so checking iron is part of the workup for unexplained itch.
- `connects-to` → **[Brain](../../06-organ/brain/README.md)** — Chronic itch becomes wired in the brain: central sensitization of itch-processing pathways keeps prurigo nodularis itching even after skin triggers fade, and its heavy depression burden reflects this brain involvement.
- `connects-to` → **[Peripheral Nerve](../../05-tissue/peripheral-nerve/README.md)** — Prurigo nodules sprout extra nerve fibers: the dermal peripheral nerves proliferate and sensitize, so the lumps themselves become itch generators that lock in the scratch-itch cycle.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy reveals the nodule's nerve overgrowth: the thickened skin teems with proliferated dermal nerve endings and degranulating mast cells alongside it, the cellular machinery that turns a scratch into a self-sustaining itch.
- `connects-to` → **[Vitamin D (Calciferol)](../../../03-medicine/03-food/vitamin-d/README.md)** — Vitamin D deficiency stokes the itch: low levels are common in chronic pruritus and prurigo, and the vitamin's role in skin-barrier repair and immune regulation has made supplementation a studied adjunct.
- `connects-to` → **[Zinc](../../02-atomic/zinc/README.md)** — Zinc shortage can drive itchy skin: deficiency produces a scaly, itch-prone dermatitis and impairs barrier repair, so correcting low zinc is part of addressing the relentless scratching behind prurigo.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — Prurigo's breakthrough treatments are antibodies: dupilumab blocks IL-4/IL-13 signaling and nemolizumab the itch cytokine IL-31's receptor, monoclonal antibodies that finally break the itch-scratch cycle that topical steroids could not.
- `connects-to` → **[Eye](../../06-organ/eye/README.md)** — The biologics bring an ocular catch: dupilumab, used for prurigo and atopic disease, commonly causes conjunctivitis, so a red, irritated eye is a side effect watched for during treatment.
- `connects-to` → **[Neutrophil](../../04-cellular/neutrophil/README.md)** — Relentless scratching breaches the barrier: the excoriated nodules become impetiginized, drawing neutrophils as secondary bacterial infection sets in — a complication that itself worsens the itch.
- `connects-to` → **[Endocannabinoid System](../../03-molecular/endocannabinoid/README.md)** — The endocannabinoid system can dial down itch: cannabinoid receptors on skin nerves and immune cells modulate the itch signal, so topical and systemic cannabinoids are studied as antipruritics for the relentless scratching of prurigo.
- `connects-to` → **[Gut Microbiome](../gut-microbiome/README.md)** — A gut-skin axis may feed the itch: dysbiosis and altered microbial metabolites shape the systemic inflammation behind chronic pruritic skin disease, tying the gut to the neuroimmune itch of prurigo nodularis.
- `connects-to` → **[Erythrocyte](../../04-cellular/erythrocyte/README.md)** — Relentless itch can signal the blood: polycythemia vera and iron deficiency are recognized systemic causes of chronic pruritus, so a blood disorder is sought when scratching builds prurigo nodules without an obvious skin cause.
- `connects-to` → **[Hepatitis C](../hepatitis-c/README.md)** — Chronic infection can itch the skin into nodules: hepatitis C and the cholestatic liver disease it causes are recognized systemic drivers of pruritus, so an unexplained prurigo nodularis prompts a look at the liver and a viral screen.
- `connects-to` → **[CGRP](../../03-molecular/cgrp/README.md)** — Sensory nerves inflame their own territory: CGRP released from the skin's itch fibers drives the neurogenic inflammation and nerve sensitization that, with chronic scratching, build the thickened nodules of the disease.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Macrophages help build the nodule: drawn into the lesion, they sustain the type-2 and neuroimmune inflammation and the fibrosis that hardens prurigo nodularis into its characteristic firm bumps.
- `connects-to` → **[Interleukin-5](../../03-molecular/il-5/README.md)** — Eosinophils answer IL-5 in the nodule: this type-2 cytokine recruits and activates the eosinophils found in prurigo lesions, part of the Th2 milieu that anti-type-2 biologics aim to quiet.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — A damaged skin barrier releases IL-33: this alarmin from stressed keratinocytes ignites the type-2 and neuroimmune cascade, both amplifying itch-driving sensory nerves and the Th2 inflammation that builds prurigo nodules.
- `connects-to` → **[Generalized Anxiety Disorder](../generalized-anxiety-disorder/README.md)** — The itch-scratch cycle and the mind feed each other: the relentless pruritus of prurigo nodularis drives anxiety and sleep loss, while stress lowers the itch threshold — a psychodermatologic loop that worsens both conditions.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — The itch cytokines all funnel through JAK-STAT3: IL-31, IL-13 and IL-4 signal via STAT3 in sensory neurons and immune cells to drive pruritus and nodule formation, which is why JAK inhibitors quiet prurigo nodularis.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — Chronic scratching and inflammation feed NF-κB: repeated skin trauma and type-2 cytokines activate NF-κB in keratinocytes and immune cells, sustaining the inflammation that thickens the nodules of the disease.
- `connects-to` → **[Opioid Use Disorder](../opioid-use-disorder/README.md)** — Opioids and itch are entwined: chronic opioid use causes pruritus that can drive a prurigo-like picture through the mu-opioid system, while kappa-opioid-modulating drugs are used to treat the intractable itch.
- `connects-to` → **[HIV](../hiv/README.md)** — It can be a marker of HIV: severe, treatment-resistant prurigo nodularis is a recognized cutaneous sign of HIV, the immune dysregulation amplifying the itch-scratch cycle, sometimes prompting HIV testing.
- `connects-to` → **[Obsessive-Compulsive Disorder](../obsessive-compulsive-disorder/README.md)** — The scratching can take on a compulsive quality: the relentless itch-scratch cycle of prurigo nodularis overlaps with skin-picking and obsessive-compulsive-spectrum behavior, each reinforcing the other.
- `connects-to` → **[Hepatocellular Carcinoma](../hcc/README.md)** — Cholestatic liver disease drives the itch: bile-salt retention from advanced liver disease and biliary obstruction in hepatocellular carcinoma causes intense pruritus that can manifest as prurigo nodularis.
- `connects-to` → **[Staphylococcus aureus](../../../02-pathogen/02-bacteria/staphylococcus-aureus/README.md)** — Relentless scratching opens the skin to Staph: the excoriated nodules of prurigo nodularis are repeatedly broken open, readily colonized and infected by Staphylococcus aureus, which in turn intensifies the itch.
- `connects-to` → **[Wound Healing](../wound-healing/README.md)** — Constant scratching defeats repair: the compulsive scratching of prurigo nodularis reopens lesions faster than they can heal, perpetuating the thickened, eroded nodules in an itch-scratch cycle.
- `connects-to` → **[DLBCL](../dlbcl/README.md)** — Severe itch can flag a lymphoma: persistent prurigo nodularis is a recognized paraneoplastic sign of underlying lymphoma, prompting evaluation for Hodgkin and non-Hodgkin lymphomas such as DLBCL.
- `connects-to` → **[Immune System](../immune-system/README.md)** — It is a neuroimmune itch disorder: prurigo nodularis is driven by Th2 cytokines and IL-31 sensitising itch nerves, which is why the immune-targeting biologic dupilumab is now an effective treatment.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — Endocrine disease can drive the itch: thyroid dysfunction and diabetes are among the systemic causes of the chronic pruritus that seeds prurigo nodularis, so endocrine screening is part of its work-up.
- `connects-to` → **[Iron-Deficiency Anemia](../iron-deficiency-anemia/README.md)** — Low iron can itch: iron deficiency is a recognised systemic cause of generalised pruritus, and correcting it can relieve the itch that perpetuates prurigo nodularis.
- `connects-to` → **[Respiratory System](../respiratory-system/README.md)** — It shares the atopic, type-2 inflammatory pathway: prurigo nodularis is enriched for atopy and asthma, and the IL-4/IL-13 axis it shares with airway disease is why dupilumab treats both.
- `connects-to` → **[Lymphatic System](../lymphatic-system/README.md)** — Relentless itch can flag a lymphoma: severe chronic pruritus and prurigo nodularis can be a paraneoplastic sign of Hodgkin and other lymphomas, prompting nodal examination and screening.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — Pregnancy complicates its itch and care: chronic pruritus can flare in pregnancy, where the systemic immunomodulators used for prurigo nodularis are restricted, limiting treatment options.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — Liver and bile drive the itch: cholestatic liver disease floods the skin with bile salts and pruritogens, a systemic cause of the relentless itch that builds prurigo nodularis.
- `connects-to` → **[Cardiovascular System](../cardiovascular-system/README.md)** — Chronic inflammatory skin disease tracks with cardiovascular risk: like psoriasis and atopic dermatitis, severe prurigo nodularis is associated with a higher burden of cardiovascular and metabolic comorbidity.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — Its strong systemic treatments cost the skeleton: prolonged corticosteroids and immunosuppressants used for severe refractory prurigo nodularis drive bone loss and muscle weakness.
- `connects-to` → **[Renal System](../renal-system/README.md)** — Kidney failure drives the itch: chronic kidney disease causes uraemic pruritus that can evolve into prurigo nodularis, one of the strongest systemic associations of the condition.
- `connects-to` → **[Corticosteroids](../../../03-medicine/01-modern/02-respiratory/corticosteroids/README.md)** — First-line calms the nodule: potent topical and intralesional corticosteroids reduce the inflammation and itch of prurigo nodularis, used before stepping up to biologics like dupilumab.
- `connects-to` → **[Cholangiocarcinoma](../cholangiocarcinoma/README.md)** — Cholestatic itch can underlie it: bile-duct obstruction from cholangiocarcinoma causes intense cholestatic pruritus, and the relentless scratching it provokes can produce prurigo nodularis.
- `connects-to` → **[Targeted Therapy](../../../03-medicine/01-modern/13-cancer/targeted-therapy/README.md)** — Type-2 and itch cytokines are the targets: dupilumab against IL-4Rα and nemolizumab against the IL-31 receptor — the 'itch cytokine' — are the first approved biologics for prurigo nodularis, with JAK inhibitors close behind.
- `connects-to` → **[Cancer Chemotherapy](../../../03-medicine/01-modern/13-cancer/cancer-chemotherapy/README.md)** — It can be a paraneoplastic clue: severe new prurigo nodularis can herald an underlying lymphoma or solid cancer, where treating the malignancy with chemotherapy resolves the otherwise refractory itch.
- `connects-to` → **[Dermatomyositis](../dermatomyositis/README.md)** — Another intensely itchy dermatosis: like prurigo nodularis, dermatomyositis causes severe pruritus and can be paraneoplastic, both reminding clinicians that relentless itch may signal systemic or malignant disease.
- `connects-to` → **[Asthma](../asthma/README.md)** — Type-2 atopy connection: prurigo nodularis shares the IL-4/IL-13 type-2 inflammation of asthma and atopic disease, and the anti-IL-4-receptor biologic dupilumab treats both conditions.
- `connects-to` → **[Polycythemia Vera](../polycythemia-vera/README.md)** — Itch from the blood: aquagenic pruritus is a classic feature of polycythaemia vera, and relentless scratching can raise prurigo-like nodules—severe itch as a clue to a myeloproliferative cause.
- `connects-to` → **[BDNF](../../03-molecular/bdnf/README.md)** — Neurotrophins and the itch nerve: BDNF and nerve growth factor drive the dermal nerve-fibre hyperplasia and neuronal sensitisation that make prurigo nodularis so intensely and persistently itchy.
- `connects-to` → **[Myelofibrosis](../myelofibrosis/README.md)** — Myeloproliferative itch: like polycythaemia vera, myelofibrosis causes severe aquagenic and chronic pruritus that can drive prurigo nodularis, the itch a clue to an underlying myeloproliferative neoplasm.
- `connects-to` → **[Pancreatic Cancer](../pancreatic-cancer/README.md)** — Cholestatic and paraneoplastic itch: a pancreatic head cancer obstructing the bile duct causes intense cholestatic pruritus, and generalised itch can be a paraneoplastic clue presenting as prurigo nodularis.
- `connects-to` → **[PTSD](../ptsd/README.md)** — The psychodermatology link: prurigo nodularis is strongly tied to anxiety, depression and trauma (PTSD), the itch-scratch cycle both worsened by and worsening psychological distress.
- `connects-to` → **[PTCL](../ptcl/README.md)** — A malignant itch to exclude: cutaneous T-cell lymphoma (mycosis fungoides) is intensely pruritic and can produce prurigo-like nodules, a malignant mimic of prurigo nodularis warranting biopsy in atypical cases.
- `connects-to` → **[Social Anxiety Disorder](../social-anxiety-disorder/README.md)** — The visible, stigmatising lesions: the excoriated nodules of prurigo nodularis are disfiguring and carry social stigma, driving social anxiety and avoidance much as other visible skin diseases do.
- `connects-to` → **[COVID-19 Disease](../covid-19-disease/README.md)** — Stress and post-viral itch: pandemic stress worsened the itch-scratch cycle, and chronic pruritus has been reported as a post-COVID symptom, flaring prurigo nodularis.
- `connects-to` → **[Periostin](../../03-molecular/periostin/README.md)** — Type-2 matrix signal: periostin, induced by IL-4 and IL-13, deposits in the dermis of prurigo nodularis and directly activates sensory neurons to amplify the itch-scratch cycle.
- `connects-to` → **[TNF-α](../../03-molecular/tnf-alpha/README.md)** — Mixed inflammation: TNF-α contributes to the mixed Th2/Th17/Th22 inflammatory milieu of prurigo nodularis lesions, sustaining the chronic skin inflammation behind the nodules.
- `connects-to` → **[IL-6](../../03-molecular/il-6/README.md)** — Fibrosis and itch: IL-6 promotes the dermal fibrosis and neural proliferation of prurigo nodularis nodules, linking chronic inflammation to the thickened, intensely itchy lesions.
- `connects-to` → **[CCL2](../../03-molecular/ccl2/README.md)** — Myeloid recruitment: CCL2 draws monocytes and macrophages into prurigo nodularis lesions, sustaining the dermal inflammatory infiltrate that feeds the itch-scratch cycle and nodule formation.
- `connects-to` → **[PDGF](../../03-molecular/pdgf/README.md)** — Nodule fibroblasts: PDGF drives the dermal fibroblast proliferation that builds the firm, hyperplastic nodules of prurigo nodularis, the structural correlate of the chronic scratching.
- `connects-to` → **[Serotonin](../../03-molecular/serotonin/README.md)** — Systemic pruritus pathway: serotonin contributes to the itch of the uraemic and cholestatic conditions that underlie many cases of prurigo nodularis, the rationale for 5-HT3-antagonist antipruritics.
- `connects-to` → **[NTRK / TrkA](../../03-molecular/ntrk/README.md)** — Nerve growth factor signaling through TrkA drives the dermal nerve-fiber proliferation characteristic of prurigo nodularis, sensitizing the skin and perpetuating the chronic itch-scratch cycle that builds the nodules.
- `connects-to` → **[KIT](../../03-molecular/kit/README.md)** — KIT-dependent mast cells accumulate in prurigo nodularis lesions, releasing pruritogens and neuropeptides that feed the neuroimmune itch and contribute to the dermal inflammatory infiltrate of the nodules.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — IL-1β from activated keratinocytes and myeloid cells adds an innate inflammatory arm to the dominant type-2 cytokine response in prurigo nodularis, reinforcing the chronic inflammation that sustains the lesions.

[^stander-2020-nemolizumab-pn]: Ständer S, Yosipovitch G, Legat FJ, et al. Trial of nemolizumab in moderate-to-severe prurigo nodularis. *N Engl J Med.* 2020;382(8):706-716. [doi:10.1056/NEJMoa1908316](https://doi.org/10.1056/NEJMoa1908316) · [PubMed 32053299](https://pubmed.ncbi.nlm.nih.gov/32053299/)
[^briggs-2022-dupilumab-pn-liberty]: Briggs JN, Cho YY, Khanna R, et al. Dupilumab for prurigo nodularis: the LIBERTY-PN PRIME and PRIME2 trials. *N Engl J Med.* 2022;387(18):1683-1693. [doi:10.1056/NEJMoa2205093](https://doi.org/10.1056/NEJMoa2205093) · [PubMed 36300905](https://pubmed.ncbi.nlm.nih.gov/36300905/)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
