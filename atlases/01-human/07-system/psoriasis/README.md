---
schema: human-scale-entry/v1
id: psoriasis
name: Psoriasis
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-06
summary: "Chronic skin disease driven by Th17/IL-17 axis, TNF-alpha, and keratinocyte hyperproliferation; thickened scaly erythematous plaques. IL-17 inhibitors (secukinumab, ixekizumab), IL-23 inhibitors (risankizumab), and anti-TNF (adalimumab) provide near-complete skin clearance."
aliases: ["plaque psoriasis", "psoriasis vulgaris", "PsO", "PsA", "psoriatic arthritis", "palmoplantar psoriasis"]
sources:
  - id: nestle-2009-psoriasis-review
    type: peer-reviewed
    cite: "Nestle FO, Kaplan DH, Barker J. Psoriasis. N Engl J Med. 2009;361(5):496-509."
    doi: "10.1056/NEJMra0804595"
    pmid: "19641206"
    url: "https://doi.org/10.1056/NEJMra0804595"
  - id: langley-2014-secukinumab
    type: peer-reviewed
    cite: "Langley RG, Elewski BE, Lebwohl M, et al. Secukinumab in plaque psoriasis — results of two phase 3 trials. N Engl J Med. 2014;371(4):326-338."
    doi: "10.1056/NEJMoa1406095"
    pmid: "25007392"
    url: "https://doi.org/10.1056/NEJMoa1406095"
  - id: gordon-2018-risankizumab
    type: peer-reviewed
    cite: "Gordon KB, Strober B, Lebwohl M, et al. Efficacy and safety of risankizumab in moderate-to-severe plaque psoriasis (UltIMMa-1 and UltIMMa-2): results from two double-blind, randomised, placebo-controlled and ustekinumab-controlled phase 3 trials. Lancet. 2018;392(10148):650-661."
    doi: "10.1016/S0140-6736(18)31713-6"
    pmid: "30097359"
    url: "https://doi.org/10.1016/S0140-6736(18)31713-6"
cross_links:
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "Th17 cells are the primary psoriasis pathogenic T cells; IL-17A/F activate keratinocyte NF-kB and STAT3 → CXCL8 and S100 proteins → neutrophil recruitment and epidermal hyperproliferation; IL-22 drives keratinocyte proliferation and anti-apoptosis."
  - target: 01-human/03-molecular/tnf-alpha
    relation: connects-to
    note: "TNF-alpha activates keratinocyte NF-kB → CXCL1/IL-8, ICAM-1, and survival genes → epidermal thickening; adalimumab, infliximab, etanercept, and certolizumab achieve ~60% PASI 75 in moderate-severe psoriasis and treat psoriatic arthritis."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "IL-6 amplifies Th17 polarization (with TGF-beta) in psoriasis; STAT3-driven keratinocyte hyperproliferation; elevated serum IL-6 correlates with psoriasis severity and psoriatic arthritis; tocilizumab has limited psoriasis efficacy vs. Th17-targeting biologics."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "NF-kB is activated in psoriatic keratinocytes by TNF-alpha and IL-17A → drives AMP expression (LL-37, beta-defensins), CXCL8 (neutrophil chemotaxis), IL-6, and CCL20 (DC recruitment); NF-kB inhibition is a downstream convergence point of most anti-psoriasis biologics."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "IL-23 from dermal DCs activates Th17 and γδ T cells → IL-17A/F and IL-22 → keratinocyte hyperproliferation, acanthosis, and neutrophil recruitment in psoriatic plaques; anti-IL-23p19 antibodies (risankizumab, guselkumab) achieve PASI 90 response in ~50% of patients."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "IL-17A from skin Th17 and γδ T cells activates keratinocyte IL-17RA/RC → NF-kB → CXCL8, S100A proteins, and AMPs → neutrophil influx and epidermal hyperproliferation; secukinumab (anti-IL-17A) and ixekizumab achieve PASI 90 in ~60% of plaque psoriasis patients at 16 weeks."
  - target: 01-human/03-molecular/il-31
    relation: connects-to
    note: "IL-31 contributes to pruritus in psoriasis despite the Th17 cytokine environment; psoriatic skin ILC2 cells produce IL-31; IL-31 correlates with itch VAS independently of PASI; JAK inhibitors (deucravacitinib, upadacitinib) reduce psoriatic inflammation and IL-31-mediated itch."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Narrow-band UVB (311–313 nm) phototherapy induces T-cell apoptosis in psoriatic plaques and suppresses the Th17/IL-17A axis; NBUVB achieves PASI 75 in 50–70% of patients; safe in pregnancy; requires 2–3 sessions/week for 6–10 weeks induction."
  - target: 01-human/07-system/ankylosing-spondylitis
    relation: connects-to
    note: "Psoriasis and AS sit on the spondyloarthritis spectrum, sharing the IL-23/Th17→IL-17A axis and responding to IL-17 (secukinumab, ixekizumab) and IL-23 blockade; ~20-30% of psoriasis patients develop inflammatory arthritis, and axial psoriatic arthritis overlaps with AS."
  - target: 01-human/07-system/psoriatic-arthritis
    relation: connects-to
    note: "Up to ~30% of plaque-psoriasis patients develop psoriatic arthritis, usually years after skin disease; both share the IL-23/Th17→IL-17A/TNF axis, so IL-17, IL-23 and TNF inhibitors treat skin and joints together; nail and scalp psoriasis flag higher PsA risk."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "Psoriasis is the archetypal immune-mediated skin disease: Th17-derived IL-17A/IL-22 drive keratinocyte hyperproliferation → thickened scaly plaques with parakeratosis and acanthosis; epidermal turnover shortens from ~28 to ~4 days, and skin is the primary treated site."
  - target: 01-human/07-system/atopic-dermatitis
    relation: connects-to
    note: "Psoriasis and atopic dermatitis are the two major inflammatory skin diseases but immunologically opposite: psoriasis is Th17/IL-23-driven with sharp scaly plaques, while atopic dermatitis is Th2-driven with itchy, ill-defined eczema—dictating different biologics."
  - target: 01-human/07-system/inflammatory-bowel-disease
    relation: connects-to
    note: "Psoriasis and inflammatory bowel disease share the IL-23/Th17 axis and co-occur: both respond to anti-IL-23 and anti-TNF biologics, though anti-IL-17 can paradoxically worsen Crohn's—so the shared pathway also constrains drug choice across the two diseases."
  - target: 01-human/07-system/atherosclerosis
    relation: connects-to
    note: "Psoriasis is an independent cardiovascular risk factor: chronic systemic Th17 inflammation accelerates atherosclerosis, so severe psoriasis raises heart attack and stroke risk beyond shared metabolic factors—and effective skin treatment may lower vascular inflammation."
  - target: 01-human/07-system/obesity
    relation: connects-to
    note: "Psoriasis and obesity are bidirectionally linked through inflammation: adipose-derived cytokines worsen psoriatic inflammation, while psoriasis raises metabolic-syndrome risk, so obese psoriasis patients have more severe disease and weight loss improves it."
  - target: 01-human/07-system/type-2-diabetes
    relation: connects-to
    note: "Psoriasis raises the risk of type 2 diabetes: shared systemic inflammation (TNF, IL-6, IL-17) drives insulin resistance, so psoriasis is an independent cardiometabolic risk factor—part of why it is now treated as a systemic, not just skin, disease."
  - target: 03-medicine/03-food/vitamin-d
    relation: connects-to
    note: "Vitamin D both treats and modulates psoriasis: topical vitamin D analogs slow the hyperproliferation of psoriatic keratinocytes and are first-line therapy, while the immunomodulatory role of vitamin D ties skin immunity to this hormone—a vitamin used as a drug."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "Psoriasis is an independent cardiovascular risk factor: systemic IL-17/TNF inflammation accelerates atherosclerosis, so severe psoriasis raises heart-attack and stroke risk beyond its shared metabolic-syndrome links—reframing it as more than a skin disease."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "Plasmacytoid dendritic cells ignite psoriasis: they sense self-DNA and release type I interferon that, with myeloid dendritic cells, launches the IL-23/Th17 cascade—so dendritic cells sit at the very start of the inflammatory loop that thickens the skin."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "IL-12/IL-23 sit at the heart of psoriasis: their shared p40 subunit drives the Th1/Th17 response that fuels keratinocyte hyperproliferation, which is why ustekinumab (anti-p40) and IL-23-specific biologics clear psoriasis plaques so effectively."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "Neutrophils mark the psoriatic plaque: they swarm into the epidermis to form Munro microabscesses, and in pustular psoriasis they fill visible pustules—so although T cells drive the disease, neutrophils are its histologic signature and dominate its pustular forms."
  - target: 02-pathogen/02-bacteria/streptococcus-pyogenes
    relation: connects-to
    note: "Strep throat can ignite psoriasis: streptococcal infection classically triggers guttate psoriasis, especially in children, as bacterial superantigens activate T cells that cross-react with skin—one of the clearest infection-to-autoimmunity links in dermatology."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "Psoriasis carries a heavy mental-health toll: visible plaques, stigma, and chronic inflammation roughly double the risk of depression and suicidal thoughts, so screening for depression is part of good psoriasis care—and clearing skin often lifts mood."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "Oral JAK and TYK2 inhibitors now treat psoriasis: blocking JAK-family signaling downstream of IL-23 and other cytokines (e.g., deucravacitinib targeting TYK2) controls plaques without injections, extending the IL-23/IL-17-targeted revolution to pills."
  - target: 01-human/07-system/nash
    relation: connects-to
    note: "Psoriasis and fatty-liver disease travel together: shared systemic inflammation and metabolic syndrome raise the risk of MASH in psoriasis patients, part of why psoriasis is now seen as a systemic inflammatory disease, not just skin-deep."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Psoriasis plaques recur in the same spots because of cytotoxic T cells: epidermal resident-memory CD8 T cells persist after lesions clear, forming a 'disease memory' that reignites plaques at old sites—why the disease relapses where it was."
  - target: 01-human/03-molecular/cortisol
    relation: connects-to
    note: "Psoriasis is first treated with cortisol's kin: topical corticosteroids calm the IL-17/Th17 inflammation driving the plaques, the most-used therapy—though rebound on stopping and skin thinning limit long-term potent use."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Psoriasis is treated by restoring keratinocyte calcium signaling: vitamin D analogs (calcipotriol) normalize the calcium-dependent differentiation that runs amok in psoriatic skin, slowing the overgrowth—often paired with a steroid."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: connects-to
    note: "Psoriasis reflects failed restraint by regulatory T cells: dysfunctional Tregs let the IL-23/Th17 axis run unchecked against the skin, so the imbalance between effector and regulatory T cells underlies the chronic plaques."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "Psoriasis travels with fatty liver: its systemic inflammation and shared metabolic syndrome make non-alcoholic fatty liver disease common, and the methotrexate used to treat psoriasis can itself scar the liver, so liver health must be watched."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "Psoriatic plaques are richly vascular: VEGF drives dermal endothelial cells to build dilated, leaky capillaries near the surface, which is why scraping a plaque produces pinpoint bleeding (the Auspitz sign)."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "Salt may inflame psoriasis: high sodium accumulates in skin and pushes naive T cells toward the IL-17-producing Th17 lineage that drives psoriatic plaques, a dietary link between salt and the disease's core immune axis."
  - target: 01-human/05-tissue/peripheral-nerve
    relation: connects-to
    note: "Psoriasis itches and reacts through nerves: sensory peripheral-nerve fibers, fired by IL-31 and inflammation, carry the itch, and nerve injury can clear plaques in a denervated patch—evidence the skin's nerves help sustain the disease."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "Psoriasis is more than skin-deep: its systemic inflammation accelerates atherosclerosis, so severe disease raises the risk of heart attack independently of the usual cardiovascular risk factors."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "Mast cells lurk in psoriatic skin: degranulating near nerves and vessels, they release mediators that amplify the early inflammation and itch, linking neurogenic triggers to the plaque."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy shows the psoriatic plaque's hyperdrive: keratinocytes pile up far too fast with retained nuclei in the surface scale, and neutrophils collect into Munro microabscesses, the ultrastructure of runaway epidermal turnover."
  - target: 01-human/06-organ/eye
    relation: connects-to
    note: "Psoriasis can inflame the eye: it is associated with uveitis, conjunctivitis, and dry, scaly blepharitis of the lids, ocular involvement that parallels the immune attack on the skin and joints."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "Zinc matters to the psoriatic skin: levels often run low in the rapidly shedding epidermis, and because the mineral fuels skin repair and tempers inflammation, its deficiency can aggravate the plaques."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "Psoriasis itches and flares through the nerves: sensory neurons in the plaque release substance P and CGRP that fuel neurogenic inflammation, the same wiring behind the stress-triggered flares and the maddening itch."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "Treating psoriasis keeps an eye on the lungs: methotrexate can rarely cause a hypersensitivity pneumonitis, and the TNF and IL-17 biologics that clear the plaques raise the risk of pneumonia and reactivated tuberculosis."
  - target: 01-human/04-cellular/adipocyte
    relation: connects-to
    note: "Psoriasis and fat inflame each other: enlarged adipocytes pour out the same cytokines that drive the plaques, so obesity worsens psoriasis and blunts treatment — a metabolic link in the 'psoriatic march' toward heart disease."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "Antibodies revolutionized psoriasis care: monoclonal antibodies against TNF, IL-17, and IL-23 (secukinumab, guselkumab, ustekinumab) clear the plaques by neutralizing the exact cytokines driving them, often where older drugs failed."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "Skin disease reaches intimate places: genital psoriasis and the visible plaques impair sexual health and self-image, while pregnancy often calms psoriasis through its immune shift, only for it to flare again after delivery."
  - target: 01-human/07-system/gut-microbiome
    relation: connects-to
    note: "A gut-skin axis links plaque to flora: psoriasis patients show gut dysbiosis and a high overlap with inflammatory bowel disease, the shared mucosal-barrier and IL-23 immunology tying the bowel's microbes to the skin's inflammation."
  - target: 01-human/03-molecular/il-36
    relation: connects-to
    note: "A different cytokine drives the pustular form: in generalized pustular psoriasis, loss of the IL-36 receptor antagonist unleashes IL-36, flooding the skin with neutrophils into sterile pustules — now treatable by the IL-36 blocker spesolimab."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Plaques keep their own inflammatory engine: dermal macrophages pour out TNF and recruit more immune cells, sustaining the lesion and feeding the systemic inflammation that links psoriasis to heart and metabolic disease."
  - target: 01-human/07-system/hiv-aids
    relation: connects-to
    note: "HIV paradoxically ignites psoriasis: as immunity collapses the disease often appears or turns severe and treatment-resistant, a striking exception to its T-cell-driven model that improves with antiretroviral therapy."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "A transcription hub turns on the plaque: IL-23 signals through STAT3 to sustain the Th17/IL-17 response and the keratinocyte overgrowth of psoriasis, the node that TYK2-JAK inhibitors like deucravacitinib block."
  - target: 02-pathogen/03-fungi/candida-albicans
    relation: connects-to
    note: "A fungus can light the fuse: like streptococcal throat infection, Candida colonization acts as a microbial trigger and superantigen that flares psoriasis, and patients carry the yeast more often."
  - target: 01-human/07-system/stroke
    relation: connects-to
    note: "The skin disease reaches the brain's arteries: psoriasis's systemic inflammation accelerates atherosclerosis, raising the risk of stroke and heart attack independently of the usual cardiovascular risk factors."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "Chronic inflammation clots the veins too: beyond its arterial risk, severe psoriasis is independently linked to a higher rate of deep-vein thrombosis and pulmonary embolism, part of the prothrombotic state of systemic inflammatory disease."
  - target: 01-human/07-system/alcohol-use-disorder
    relation: connects-to
    note: "Drink and disease worsen each other: alcohol use disorder is over-represented in psoriasis and both triggers flares and blunts treatment response, a bidirectional link tangled with the disease's psychological burden."
  - target: 01-human/07-system/sepsis
    relation: connects-to
    note: "Severe forms strip the skin's defense: erythrodermic and generalized pustular psoriasis breach the barrier across most of the body, letting bacteria invade — a route to bloodstream infection and sepsis compounded by immunosuppressive therapy."
  - target: 01-human/07-system/gout
    relation: connects-to
    note: "Rapid skin turnover floods the blood with urate: the accelerated epidermal proliferation of psoriasis raises uric acid production, so hyperuricemia and gout are notably more common in people with the disease."
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "Systemic inflammation reaches the kidney: moderate-to-severe psoriasis is independently associated with chronic kidney disease, and some of its systemic and biologic therapies add their own renal considerations."
  - target: 02-pathogen/01-viruses/hepatitis-b-virus
    relation: connects-to
    note: "Its biologics can reactivate the virus: the TNF inhibitors and other immunosuppressants used for psoriasis can reawaken latent hepatitis B, so screening and antiviral prophylaxis precede starting these therapies."
  - target: 01-human/07-system/tuberculosis
    relation: connects-to
    note: "TNF blockade can wake latent TB: the anti-TNF biologics used for moderate-to-severe psoriasis disable the cytokine that walls off tuberculosis, so screening and treatment of latent infection precede therapy."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "Visible disease feeds chronic worry: the stigma, unpredictability and social impact of psoriasis drive anxiety alongside its well-known depression, worsening quality of life independent of skin severity."
  - target: 01-human/07-system/dlbcl
    relation: connects-to
    note: "Severe disease and its therapy nudge lymphoma risk: chronic immune activation in severe psoriasis, and the immunosuppressants used to treat it, are associated with a modestly raised risk of lymphoma."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "It is the archetypal skin disease: psoriasis drives hyperproliferation of the epidermis into well-demarcated scaly plaques, with nail pitting and scalp involvement, the visible core of the disorder."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "It travels with metabolic and thyroid disease: psoriasis is strongly tied to the insulin resistance and metabolic syndrome of endocrine dysfunction and shows raised rates of autoimmune thyroid disease."
  - target: 02-pathogen/01-viruses/varicella-zoster-virus
    relation: connects-to
    note: "Its biologics reawaken shingles: the TNF, IL-17/23 and especially JAK inhibitors used for moderate-to-severe psoriasis blunt antiviral immunity and raise the risk of herpes-zoster reactivation."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "It runs on the IL-23/IL-17 axis: psoriasis is a T-cell-driven autoinflammatory disease in which dendritic cells, IL-23 and IL-17 inflame the skin — the pathway every modern biologic targets."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "A core drug can scar the lungs: methotrexate, a mainstay systemic therapy for psoriasis, can cause hypersensitivity pneumonitis and pulmonary fibrosis, requiring vigilance for new breathlessness."
  - target: 01-human/07-system/lymphatic-system
    relation: connects-to
    note: "Extensive disease swells the nodes: erythrodermic and widespread psoriasis causes reactive dermatopathic lymphadenopathy, and severe disease carries a modestly increased lymphoma risk."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "Nails and entheses warn of joint disease: nail pitting, enthesitis and dactylitis are early musculoskeletal signs that herald the psoriatic arthritis affecting up to a third of patients."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "It shares a path with bowel disease and its drugs hit the liver: psoriasis overlaps inflammatory bowel disease through shared inflammation, and methotrexate therapy for it is hepatotoxic."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "Severe disease and its drugs reach the kidney: extensive psoriasis independently raises chronic kidney disease risk, and cyclosporine used to control it is nephrotoxic."
  - target: 03-medicine/01-modern/11-biologics/adalimumab
    relation: connects-to
    note: "Biologics clear severe disease: anti-TNF agents like adalimumab, with IL-17 and IL-23 inhibitors, are transformative for moderate-to-severe psoriasis and its arthritis."
  - target: 03-medicine/01-modern/02-respiratory/corticosteroids
    relation: connects-to
    note: "Topical steroids are first-line, systemic ones risky: potent topical corticosteroids treat plaques, but systemic steroids are avoided as withdrawal can trigger life-threatening pustular psoriasis flares."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "Stress and the skin talk both ways: psychological stress triggers psoriasis flares through the brain-skin neuroimmune axis, and the visible disease in turn drives anxiety and depression."
  - target: 03-medicine/01-modern/13-cancer/targeted-therapy
    relation: connects-to
    note: "Cytokine-targeted biologics transformed it: monoclonals against IL-17 and IL-23 (secukinumab, guselkumab), anti-TNF, and oral TYK2/JAK inhibitors now clear severe psoriasis by blocking the IL-23/IL-17 axis that drives it."
  - target: 03-medicine/01-modern/13-cancer/cancer-chemotherapy
    relation: connects-to
    note: "Methotrexate is the classic systemic DMARD: low-dose methotrexate, a chemotherapy antimetabolite, has long treated extensive psoriasis and psoriatic arthritis, used before or alongside the newer biologics."
  - target: 01-human/05-tissue/arterial-wall
    relation: connects-to
    note: "Skin inflammation reaches the arteries: the systemic inflammation of psoriasis accelerates atherosclerosis of the arterial wall — the 'psoriatic march' — raising cardiovascular risk independent of traditional factors."
  - target: 01-human/07-system/multiple-sclerosis
    relation: connects-to
    note: "A caution for its TNF blockers: the anti-TNF biologics used for psoriasis can unmask or worsen demyelination, so multiple sclerosis contraindicates them—and paradoxically anti-TNF therapy can itself induce psoriasis."
  - target: 01-human/07-system/iga-nephropathy
    relation: connects-to
    note: "A skin-kidney axis: psoriasis is associated with IgA nephropathy through shared mucosal IL-17/IL-23 immunity, and its TNF-inhibitor therapy can also trigger IgAN."
  - target: 01-human/07-system/hepatitis-b
    relation: connects-to
    note: "Immunosuppression reawakens the virus: TNF inhibitors and methotrexate used for psoriasis can reactivate hepatitis B and are hepatotoxic, so HBV screening precedes systemic therapy."
  - target: 01-human/07-system/type-1-diabetes
    relation: connects-to
    note: "Shared autoimmune ground: psoriasis is associated with a higher risk of type 1 diabetes, the two sharing immune-regulatory susceptibility loci beyond psoriasis's better-known link to type 2 diabetes."
  - target: 01-human/07-system/heart-failure
    relation: connects-to
    note: "Inflammation and the failing heart: severe psoriasis independently raises the risk of heart failure, its chronic systemic inflammation contributing beyond shared cardiovascular risk factors."
  - target: 01-human/07-system/social-anxiety-disorder
    relation: connects-to
    note: "The psychosocial wound: visible psoriatic plaques carry stigma that drives social anxiety, avoidance and depression, a quality-of-life burden disproportionate to the body-surface area involved."
  - target: 01-human/07-system/ptcl
    relation: connects-to
    note: "A great mimic: cutaneous T-cell lymphoma (mycosis fungoides) produces scaly erythematous plaques that imitate psoriasis and is sometimes mistreated as it for years, a malignant differential to keep in mind."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "Dermal angiogenesis: psoriatic plaques are richly vascularised through VEGF-driven new vessel growth in the dermal papillae, the basis of the pinpoint bleeding (Auspitz sign) when a scale is removed."
  - target: 01-human/07-system/covid-19-disease
    relation: connects-to
    note: "Flares and immunosuppression: COVID-19 and its vaccines can trigger psoriasis flares, while the biologics that control it raised questions about infection risk during the pandemic."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "Innate amplifier: IL-1β released by keratinocytes and myeloid cells helps ignite the IL-23/IL-17 axis, linking innate immune activation to the inflammatory loop of psoriasis."
  - target: 01-human/03-molecular/nlrp3-inflammasome
    relation: connects-to
    note: "Inflammasome trigger: NLRP3-inflammasome activation in psoriatic skin drives IL-1β maturation, with the autoantigen LL-37 among the signals that prime this innate response."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "Hypoxic plaques: thickened, hyperproliferative psoriatic epidermis becomes hypoxic, stabilising HIF-1α to drive the VEGF angiogenesis and metabolic shift of the lesions."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Disease initiation: plasmacytoid dendritic cells sensing LL-37–self-DNA complexes pour out type I interferon, the early event that ignites the dendritic-cell activation launching the psoriasis cascade."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "Keratinocyte alarmin: S100A8/A9 (calprotectin) is massively upregulated in psoriatic keratinocytes, amplifying neutrophil recruitment and inflammation and serving as a biomarker of disease activity."
  - target: 01-human/03-molecular/egfr
    relation: connects-to
    note: "Epidermal hyperproliferation: EGFR signalling drives the rapid keratinocyte proliferation that thickens psoriatic plaques, the cellular basis of the scaling and accelerated epidermal turnover."
  - target: 01-human/03-molecular/ccl2
    relation: connects-to
    note: "Myeloid recruitment: CCL2 produced in psoriatic skin draws monocytes and dendritic-cell precursors into the plaque, replenishing the antigen-presenting cells that sustain the IL-23/IL-17 inflammatory loop."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "Self-DNA sensing: keratinocyte and dendritic-cell cGAS-STING activation by self-DNA amplifies the type-I-interferon response, reinforcing the innate ignition phase that initiates and perpetuates psoriatic inflammation."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "Keratinocyte dysregulation: TGF-β1 is overexpressed in psoriatic skin where, alongside its angiogenic effects, it contributes paradoxically to the abnormal keratinocyte proliferation and inflammatory milieu of the plaque."
  - target: 01-human/03-molecular/glucocorticoid-receptor
    relation: connects-to
    note: "Topical mainstay: corticosteroids acting through the glucocorticoid receptor are the most widely used topical therapy for psoriasis, broadly suppressing the keratinocyte and immune inflammation of the plaque, often combined with vitamin-D analogues."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Differentiation therapy: vitamin-D analogues like calcipotriol act on the keratinocyte calcium-differentiation programme that is disordered in psoriasis, normalising the abnormal proliferation and maturation of the epidermis in the plaque."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Metabolic comorbidity: leptin is elevated in psoriasis and promotes Th17 responses, mechanistically tying the disease to the obesity, metabolic syndrome and cardiovascular risk that are its major systemic comorbidities."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "Keratinocyte hyperproliferation: EGFR-driven ERK signalling (EGFR already mapped) propels the keratinocyte hyperproliferation that thickens the psoriatic plaque, the epidermal response to the inflammatory cytokine milieu."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Th1 arm: Th1-derived IFN-γ contributes to the early and chronic inflammation of psoriasis alongside the dominant IL-23/IL-17 axis already mapped, activating keratinocytes and dendritic cells."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "Lost regulation: a relative deficiency of regulatory IL-10 in psoriatic skin fails to restrain the Th17 inflammation, an imbalance that helps sustain the chronic plaque."
  - target: 01-human/03-molecular/myd88
    relation: connects-to
    note: "Innate amplification: the IL-36 and IL-1 receptors (IL-36 and IL-1β mapped) and TLRs signal through MyD88 to NF-κB (mapped), amplifying the innate inflammation that drives psoriatic plaques, especially pustular psoriasis."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "Keratinocyte hyperproliferation: PI3K-AKT-mTOR signalling drives the keratinocyte hyperproliferation that thickens the psoriatic epidermis into its characteristic scaly plaque."
  - target: 01-human/03-molecular/e2f1
    relation: connects-to
    note: "Accelerated turnover: cyclin-D-CDK4/6 release of E2F1 shortens keratinocyte cell-cycle time, compressing epidermal turnover from weeks to days in the psoriatic plaque."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "PI3K-AKT-mTOR signalling (mTOR mapped) drives the keratinocyte hyperproliferation and survival that thickens the psoriatic epidermis."
  - target: 01-human/03-molecular/nfe2l2
    relation: connects-to
    note: "NRF2 antioxidant signalling is dysregulated in psoriatic keratinocytes, linking the oxidative-stress milieu of the plaque to barrier and inflammatory abnormalities."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Complement activation with C3 deposition contributes to neutrophil recruitment and the innate inflammatory amplification of psoriatic lesions."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Galectin-3 modulates keratinocyte and immune-cell crosstalk and amplifies the innate inflammation of psoriatic plaques."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "IFN-STAT1 signalling (type-I interferon already mapped) drives the early interferon-skewed innate activation that precedes the Th17 inflammation of psoriasis."
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "TGF-β-SMAD signalling (TGF-β already mapped) shapes the dysregulated keratinocyte proliferation and differentiation of the psoriatic epidermis."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "FOXO regulates keratinocyte differentiation and oxidative-stress balance, programs disrupted in the hyperproliferative epidermis of psoriasis."
  - target: 01-human/03-molecular/cdk4-6
    relation: connects-to
    note: "CDK4/6-driven cell-cycle entry (E2F1 already mapped) sustains the keratinocyte hyperproliferation that builds the psoriatic plaque."
  - target: 01-human/03-molecular/perforin
    relation: connects-to
    note: "Perforin-expressing cytotoxic CD8 (Tc17) T cells in the epidermis contribute to the keratinocyte targeting and lesion formation of psoriasis."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "GSK-3β modulates the NF-κB-driven inflammatory and keratinocyte-proliferative signaling of psoriasis."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "PI3K (PIK3CA)-AKT signaling (AKT already mapped) drives the keratinocyte hyperproliferation and immune-cell activation of psoriasis."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC-family kinase signaling participates in the keratinocyte and immune-cell activation of the psoriatic plaque."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK-linked immunometabolic signaling shapes the keratinocyte and T-cell metabolism of psoriasis."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Autophagy modulates the keratinocyte differentiation and innate immune responses of psoriasis."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "DNMT3A-mediated DNA methylation contributes to the epigenetic dysregulation of the keratinocyte and immune-cell programs of psoriasis."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-driven leukocyte recruitment into the skin contributes to the inflammatory infiltrate of psoriasis."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "CXCL12-CXCR4 signaling participates in the leukocyte trafficking and angiogenesis of psoriatic skin lesions."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "IL-33 alarmin signaling participates in the keratinocyte-driven inflammatory amplification of psoriasis."
  - target: 01-human/03-molecular/arid1a
    relation: connects-to
    note: "ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic regulation of the keratinocyte and immune gene programs of psoriasis."
  - target: 01-human/03-molecular/calcineurin
    relation: connects-to
    note: "Calcineurin-NFAT signaling, a target of ciclosporin, participates in the T-cell activation of psoriasis."
  - target: 01-human/03-molecular/adenosine
    relation: connects-to
    note: "Adenosine signaling, a mechanism of methotrexate's anti-inflammatory action, participates in the immunomodulation of psoriasis."
  - target: 01-human/03-molecular/mhc-class-ii
    relation: connects-to
    note: "HLA-C association: the strongest genetic risk factor for psoriasis is HLA-C*06:02 (PSORS1), an MHC allele, and antigen presentation to T cells, including of the autoantigen LL-37, initiates the IL-23/IL-17 cascade already mapped."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Metabolic comorbidity: psoriasis clusters with metabolic syndrome, and reduced levels of the protective adipokine adiponectin accompany the leptin excess already mapped, linking the systemic inflammation of psoriasis to its cardiometabolic risk."
  - target: 01-human/03-molecular/angiopoietin
    relation: connects-to
    note: "Plaque angiogenesis: psoriatic plaques show dilated, tortuous dermal capillaries driven by angiopoietin-Tie2 and VEGF (VEGF already mapped), the vascular change underlying the Auspitz sign of pinpoint bleeding on scale removal."
  - target: 01-human/03-molecular/il-2
    relation: connects-to
    note: "T-cell activation: IL-2-driven T-cell activation and expansion sustain the pathogenic Th17 response of psoriasis, and calcineurin inhibitors (already mapped) that block IL-2 production, like ciclosporin, are effective systemic therapies."
  - target: 01-human/03-molecular/troponin-complex
    relation: connects-to
    note: "Cardiovascular comorbidity: the systemic inflammation of psoriasis accelerates atherosclerosis (already mapped), and troponin elevation marks the myocardial injury of the increased cardiovascular events that shorten life in severe disease."
  - target: 01-human/03-molecular/xanthine-oxidase
    relation: connects-to
    note: "Hyperuricaemia: the rapid epidermal turnover of psoriasis raises purine catabolism through xanthine oxidase, elevating serum urate and increasing the risk of gout that accompanies the disease."
  - target: 01-human/03-molecular/cholesterol
    relation: connects-to
    note: "Metabolic dyslipidaemia: psoriasis is associated with an atherogenic dyslipidaemia as part of its metabolic syndrome (leptin and adiponectin already mapped), contributing to the accelerated atherosclerosis (already mapped) and cardiovascular risk of severe disease."
  - target: 01-human/03-molecular/insulin
    relation: connects-to
    note: "Insulin resistance: the systemic inflammation of psoriasis (TNF and IL-6 already mapped) promotes insulin resistance, and psoriasis is associated with an increased risk of type 2 diabetes (already mapped), part of its metabolic comorbidity."
  - target: 01-human/03-molecular/nitric-oxide
    relation: connects-to
    note: "Endothelial dysfunction: the chronic inflammation of psoriasis impairs endothelial nitric oxide, contributing to the vascular dysfunction and the increased cardiovascular events (troponin already mapped) that shorten life in severe disease."
  - target: 01-human/03-molecular/prostaglandins
    relation: connects-to
    note: "Inflammatory eicosanoids: prostaglandins and other arachidonic-acid metabolites in the psoriatic plaque (IL-6 and TNF already mapped) contribute to the inflammation and vascular changes of the lesion, part of its eicosanoid dimension."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "Type-2 counter-axis: IL-4 drives the type-2 immunity that opposes the Th17 (IL-17 and IL-23 already mapped) axis of psoriasis, and blocking IL-4 for atopic dermatitis can paradoxically unmask psoriasis, revealing the balance between the two."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "Th2-Th17 balance: IL-13, with IL-4 (already mapped), defines the type-2 pole opposite the Th17 axis of psoriasis, the reciprocal relationship distinguishing it from the atopic dermatitis at the other end of the spectrum."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Metabolic adipokine: resistin, with leptin and adiponectin (already mapped), is part of the adipokine milieu linking psoriasis to the metabolic syndrome (insulin and cholesterol already mapped) and its systemic inflammation."
  - target: 01-human/03-molecular/hepcidin
    relation: connects-to
    note: "Anaemia of chronic disease: the IL-6-driven (already mapped) hepcidin sequesters iron to produce the anaemia of chronic disease that can accompany the systemic inflammation of severe psoriasis."
  - target: 01-human/02-atomic/selenium
    relation: connects-to
    note: "Selenium and skin oxidative defence: selenium supports the antioxidant selenoprotein defence of the skin, and low selenium status, common in psoriasis, is part of the oxidative and immune imbalance of the inflamed skin."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "Skin-barrier zinc: the zinc essential for the skin barrier and immunity; the zinc status is altered in psoriasis, and topical zinc is used in its management."
  - target: 01-human/07-system/atherosclerosis
    relation: connects-to
    note: "Psoriatic march: psoriasis carries an increased atherosclerosis (cholesterol already mapped) and cardiovascular risk from the systemic inflammation (TNF and IL-6 already mapped), the 'psoriatic march'."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Dermal macrophages: the dermal macrophages (TNF and IL-6 already mapped) contribute to the psoriatic skin inflammation and the systemic inflammatory comorbidity."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "Cutaneous NK/NKT: the NK and NKT cells (perforin already mapped) of the psoriatic skin contribute to the innate inflammation of the IL-17 (already mapped) axis of psoriasis."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Type-2 counter-arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 arm balancing the dominant Th17 (IL-17 and IL-23 already mapped) drive of psoriasis."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Type-2 IgE: the IgE (with IL-4 and IL-13 already mapped) reflects the type-2 immune dimension present in a subset of psoriasis."
  - target: 01-human/03-molecular/complement-c5
    relation: connects-to
    note: "Complement in plaques: the C5 and its C5a fragment (with C3 already mapped) recruit the neutrophils of the Munro microabscesses and amplify the innate inflammation of the psoriatic plaque."
  - target: 01-human/04-cellular/b-cell
    relation: connects-to
    note: "Regulatory B-cell arm: the B cells, including the dysregulated regulatory B cells, are an increasingly recognised adaptive-immune component of psoriasis alongside the dominant Th17 (IL-17 and IL-23 already mapped) axis."
  - target: 01-human/04-cellular/plasma-cell
    relation: connects-to
    note: "Lesional plasma cells: the plasma cells secreting the antibodies (already mapped) are found in the psoriatic lesions and contribute to the humoral dimension of psoriasis."
  - target: 01-human/03-molecular/c5ar1
    relation: connects-to
    note: "C5a receptor: the C5aR1 signalling (with the complement C3 and C5 already mapped) drives the neutrophil (already mapped) recruitment into the epidermis (the Munro microabscesses) of psoriasis."
  - target: 01-human/03-molecular/tslp
    relation: connects-to
    note: "Keratinocyte alarmin: TSLP, released by the injured keratinocytes, is part of the alarmin (IL-33 already mapped) signalling that helps initiate the dendritic-cell (already mapped) activation of psoriasis."
  - target: 01-human/03-molecular/periostin
    relation: connects-to
    note: "Dermal matricellular: periostin, in the psoriatic dermis, is part of the matricellular remodelling and amplification loop that sustains the chronic plaque inflammation of psoriasis."
  - target: 01-human/03-molecular/factor-h
    relation: connects-to
    note: "Complement regulation: factor H regulates the alternative complement pathway (complement C3, C5 and C5aR1 already mapped) active in the inflamed psoriatic skin."
  - target: 01-human/03-molecular/osteopontin
    relation: connects-to
    note: "Dermal matricellular: osteopontin, elevated in the psoriatic skin and serum, amplifies the Th17 (IL-17 and IL-23 already mapped) and myeloid inflammation of the psoriatic plaque."
  - target: 01-human/03-molecular/transferrin
    relation: connects-to
    note: "Chronic-disease iron: transferrin, the iron carrier, reflects the disordered iron handling (hepcidin already mapped) of the anaemia of the chronic systemic inflammation of psoriasis."
  - target: 01-human/03-molecular/bradykinin
    relation: connects-to
    note: "Kinin-itch axis: bradykinin, released in the inflamed psoriatic skin by the kallikrein-kinin system, activates B2 receptors on keratinocytes (skin already mapped) and sensory neurons (already mapped), amplifying itch and the neuro-inflammatory dimension of psoriasis."
  - target: 01-human/03-molecular/c1-esterase-inhibitor
    relation: connects-to
    note: "Complement/kinin gate: C1-esterase inhibitor limits classical complement (C3, C5 and C5aR1 already mapped) and contact-kinin (bradykinin already mapped) over-activation in the inflamed psoriatic skin, moderating the immune-driven keratinocyte proliferation of psoriasis."
  - target: 01-human/03-molecular/erythropoietin
    relation: connects-to
    note: "Erythropoiesis support: erythropoietin counteracts the anaemia of chronic disease (hepcidin and transferrin already mapped) driven by the sustained systemic inflammation and the cytokine (IL-6 already mapped) burden of psoriasis."
  - target: 01-human/03-molecular/histamine
    relation: connects-to
    note: "Mast-cell skin effector: histamine, released by mast cells (already mapped) in psoriatic skin, promotes keratinocyte (already mapped) proliferation via H1/H4 receptors and amplifies the vascular permeability and pruritogenic signalling of psoriasis."
  - target: 01-human/03-molecular/melatonin
    relation: connects-to
    note: "Circadian anti-inflammatory protection: melatonin, via MT1/MT2 receptors on keratinocytes (already mapped) and T cells (already mapped), suppresses the NF-κB/TNF-α axis (already mapped) and reduces the oxidative stress driving the inflammatory plaque of psoriasis."
  - target: 01-human/03-molecular/prolactin
    relation: connects-to
    note: "Immune-endocrine skin axis: prolactin, acting via PRLR on keratinocytes (already mapped) and T-helper cells (already mapped), potentiates the Th17/IL-17 axis (already mapped) and the female-predominant hormonal amplification of the chronic plaque inflammation of psoriasis."
  - target: 01-human/03-molecular/testosterone
    relation: connects-to
    note: "PsO testosterone: testosterone, via androgen receptors on skin (already mapped) keratinocytes, suppresses the IL-17A (already mapped)/NF-κB (already mapped) axis; androgen deficiency amplifies T-helper-cell (already mapped) Th17 activation and the plaque burden of psoriasis."
  - target: 01-human/03-molecular/serotonin
    relation: connects-to
    note: "PsO serotonin: serotonin, via 5-HT2 on skin (already mapped) keratinocytes, amplifies keratinocyte hyperproliferation and T-helper-cell (already mapped) Th17 activation; 5-HT also promotes NF-κB (already mapped) plaque inflammation and the vascular permeability of psoriasis."
  - target: 01-human/03-molecular/oxytocin
    relation: connects-to
    note: "PsO oxytocin: oxytocin, via OXTR on regulatory T cells (already mapped) and dendritic cells (already mapped), attenuates IL-23 (already mapped)/Th17 axis; oxytocin also suppresses NF-κB (already mapped) and skin (already mapped) keratinocyte hyperproliferation of psoriasis."
  - target: 01-human/03-molecular/vasopressin
    relation: connects-to
    note: "PsO vasopressin: vasopressin, via V1a receptors on keratinocytes and dendritic cells (already mapped), amplifies NF-κB (already mapped) plaque inflammation; vasopressin also modulates vascular permeability and the IL-17A (already mapped) Th17 axis of psoriasis."
  - target: 01-human/02-atomic/iodine
    relation: connects-to
    note: "PsO iodine: iodine-dependent thyroid hormones regulate keratinocyte (already mapped) proliferation and skin (already mapped) barrier; thyroid-hormone deficiency amplifies the NF-κB (already mapped) plaque inflammation and the IL-17A (already mapped) Th17 axis of psoriasis."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "PsO magnesium: magnesium regulates NF-κB (already mapped) activity and mast-cell (already mapped) degranulation driving psoriatic plaque formation; magnesium deficiency amplifies keratinocyte hyperproliferation and the IL-17A (already mapped) inflammatory axis of psoriasis."
---

# Psoriasis

## Overview

**Psoriasis** is a **chronic, immune-mediated inflammatory skin disease** affecting approximately **125 million people worldwide** (~2-4% of Western populations; 1-2% in Asia). It presents most commonly as **plaque psoriasis** — well-demarcated, erythematous, silvery-scaled plaques on extensor surfaces (elbows, knees), scalp, and lumbosacral region — resulting from epidermal hyperproliferation driven by a dysregulated **Th17/IL-17 axis** [^nestle-2009-psoriasis-review].

Psoriasis is now understood as a **systemic inflammatory disease** with skin manifestations — associated with significant comorbidities including psoriatic arthritis (~30%), cardiovascular disease (increased MACE ~25-50%), metabolic syndrome, inflammatory bowel disease, depression/anxiety, and uveitis. The **psoriatic disease** concept encompasses the full spectrum of these manifestations.

**Psoriasis subtypes:**
- **Plaque psoriasis (psoriasis vulgaris, ~85-90%):** Chronic, most common; stable thick plaques
- **Guttate psoriasis (~10%):** Small droplet-like lesions; often post-streptococcal (streptococcal pharyngitis → guttate flare); commoner in children/young adults; may evolve to plaque
- **Palmoplantar psoriasis:** Palms and soles; functionally debilitating; pustular variant
- **Nail psoriasis (~80% with PsA):** Pitting, onycholysis, oil drop, subungual hyperkeratosis; predictive of PsA development
- **Scalp psoriasis:** ~70% of plaque psoriasis; resistant to treatment due to hair; dandruff-like or thick plaques
- **Inverse psoriasis (flexural):** Intertriginous areas (groin, axillae, submammary); no scale (macerated); diagnostic challenge
- **Erythrodermic psoriasis:** Full body skin involvement (>90% BSA); rare but severe; thermoregulatory failure, protein loss; medical emergency
- **Generalized pustular psoriasis (GPP):** Sterile neutrophilic pustules on erythematous skin; IL-36 pathway mutations (IL36RN, CARD14); spesolimab (anti-IL-36R) FDA approved 2022

**Genetics:**
- **PSORS1 (HLA-Cw*0602):** Strongest genetic signal; ~65% of early-onset psoriasis; presents HLA-C-restricted peptides to CD8+ T cells; associated with guttate subtype and streptococcal trigger
- **IL23R, IL12B, TNFAIP3, CARD14:** Multiple IL-23/IL-17 axis and NF-kB pathway GWAS loci
- **CARD14 mutations:** Gain-of-function → NF-kB activation in keratinocytes → psoriasis-like skin inflammation

## Structure

### Psoriatic plaque histology [^nestle-2009-psoriasis-review]

Normal skin: Ordered stratified squamous epithelium; 28-day epidermal turnover; differentiation from basal layer to stratum corneum.

**Psoriatic plaque:**
- **Acanthosis:** Markedly thickened epidermis (4-5× normal) due to keratinocyte hyperproliferation; epidermal turnover reduced to 3-4 days from 28 days
- **Parakeratosis:** Retention of nuclei in stratum corneum (incomplete differentiation → hallmark of psoriasis histology)
- **Munro microabscesses:** Accumulation of neutrophils in stratum corneum (neutrophil-driven by IL-17A/CXCL8)
- **Dilated blood vessels (dermal papillae):** Angiogenesis (VEGF, TNF-alpha) → tortuous vessels → erythema; visible as Auspitz sign (pinpoint bleeding when scale removed)
- **Dense T cell and DC infiltrate:** CD8+ T cells in epidermis; CD4+ T cells and DCs (mDC1+) in dermis; plasmacytoid DCs (pDCs) produce IFN-alpha initially; mDC1s sustain chronic Th17 response

### Immunopathogenesis

**Initiation phase:**
1. Trigger (physical trauma = Koebner phenomenon, streptococcal infection, stress, drugs [beta-blockers, lithium, antimalarials]) → epithelial damage → release of LL-37 (cathelicidin, an AMP)
2. LL-37 complexes with self-DNA/RNA → activates pDCs via TLR7/9 → type I IFN production → activation of skin mDCs
3. mDCs mature → upregulate IL-12 and IL-23 (shared p40 subunit targeted by ustekinumab; IL-23 p19 targeted by risankizumab, guselkumab, tildrakizumab)
4. IL-23 → Th17 cell differentiation and maintenance → IL-17A, IL-17F, IL-22 production

**Chronic maintenance phase (perpetuating Th17/17 loop):**
- Th17 IL-17A/IL-17F → bind IL-17RA/IL-17RC on keratinocytes → NF-kB and MAPK → S100 proteins (S100A7/A8/A9) → activate more DCs, trigger further IL-23 production → self-amplifying loop
- IL-17 → CXCL1/IL-8 → neutrophil recruitment → Munro microabscesses
- IL-22 → JAK1/STAT3 → keratinocyte hyperproliferation and anti-apoptosis → acanthosis
- TNF-alpha (from DCs, macrophages, keratinocytes) → ICAM-1, VCAM-1 on vasculature → further T cell recruitment; synergizes with IL-17 → additive/synergistic keratinocyte activation
- **Memory T-resident (Trm) cells in skin:** CD8+ Trm cells maintain psoriasis between flares and drive rapid plaque recurrence at previously affected sites upon trigger exposure — explains the "memory" of psoriatic plaques

## Function

### Clinical presentation

**Skin disease:**
- Well-demarcated erythematous plaques with thick adherent silvery scales; pruritus variable (25-70%); Koebner phenomenon (new lesions at trauma sites); Auspitz sign (pinpoint bleeding after scale removal)
- **BSA (body surface area) assessment:** Mild <3%, moderate 3-10%, severe >10%; also PASI (Psoriasis Area and Severity Index), IGA (Investigator's Global Assessment), DLQI (quality of life)
- Scalp, nails, palmoplantar, and genital involvement are high-impact sites regardless of BSA

**Psoriatic arthritis (PsA):**
- ~30% of psoriasis patients; inflammatory arthritis with distinctive features: asymmetric oligoarthritis, DIP joint involvement, dactylitis ("sausage digit"), enthesitis (Achilles tendon, plantar fascia), spondylitis, arthritis mutilans (severe deforming)
- CASPAR criteria: Inflammatory arthritis + 3 points from: psoriasis (current=2, history=1), nail changes, RF-negative, dactylitis, periarticular bone formation on X-ray
- Treatment: MTX (peripheral joints only), anti-TNF, anti-IL-17 (secukinumab, ixekizumab), anti-IL-12/23 (ustekinumab), JAK inhibitors (upadacitinib, tofacitinib, filgotinib), PDE-4 inhibitor (apremilast)

**Cardiovascular comorbidity:**
- ~1.4× increased MACE in moderate-severe psoriasis; chronic systemic inflammation → atherosclerosis acceleration; psoriasis patients have higher CRP, IL-6, TNF-alpha → endothelial dysfunction; anti-TNF and IL-17 biologics reduce cardiovascular inflammation and event rates
- Screen and treat cardiovascular risk factors aggressively in moderate-severe psoriasis

## Pathology

### Diagnosis

Clinical diagnosis in most cases; biopsy if uncertain (psoriasiform dermatitis pattern: acanthosis, parakeratosis, Munro microabscesses, dilated papillary vessels); rule out tinea (KOH prep), seborrheic dermatitis (more greasy, ill-defined), nummular eczema (pruritic vesicles).

Differential: Seborrheic dermatitis (common), pityriasis rosea (herald patch, Christmas tree pattern), mycosis fungoides (patch/plaque, epidermotropism), reactive arthritis (Reiter syndrome — skin lesions + urethritis + arthritis).

### Treatment [^langley-2014-secukinumab] [^gordon-2018-risankizumab]

**Topical therapy (mild psoriasis):**
- High-potency corticosteroids (clobetasol) — first-line; rapid efficacy; skin atrophy with chronic use; taper after control
- Vitamin D analogues (calcipotriol/calcipotriene): Anti-proliferative; combined with corticosteroid (Taclonex/Dovobet) → superior; non-atrophogenic; first-line maintenance
- Calcineurin inhibitors (tacrolimus, pimecrolimus): Face, flexures, genital; avoid atrophy-prone areas; no steroid adverse effects
- Roflumilast cream (Zoryve, PDE-4 inhibitor): New approval 2022; non-steroidal option including for intertriginous psoriasis

**Phototherapy (moderate psoriasis or topical-refractory):**
- **Narrowband UVB (NB-UVB, 311 nm):** First-line phototherapy; suppresses Th17 cells; 3× weekly × 3-4 months; 70-80% clearance; home units available; minimal systemic effects
- **PUVA (psoralen + UVA):** More effective than NB-UVB; psoralen photosensitizer + UVA → DNA cross-links in keratinocytes; increased squamous cell carcinoma risk with cumulative exposure; less commonly used now

**Systemic conventional therapy (moderate-severe):**
- **Methotrexate:** Folate antagonist → anti-proliferative and anti-inflammatory; 15-25 mg/week; effective but teratogenic; hepatotoxicity (transient elastography instead of routine liver biopsy); baseline PFTs
- **Cyclosporine:** Calcineurin inhibitor → T cell suppression; rapid clearance; reserved for short-term (≤1 year) for severe flares; hypertension and renal toxicity limit long-term use
- **Acitretin:** Oral retinoid; anti-proliferative; pustular psoriasis preferred; teratogenic (avoid 3 years post-treatment in women); dyslipidemia; liver toxicity
- **Apremilast (Otezla, PDE-4 inhibitor):** Oral; cAMP elevation → reduced TNF-alpha and IL-17 production; 33% PASI 75 at week 16; safer profile (no labs beyond baseline); mild efficacy; particularly useful for mild-moderate or biologic-contraindicated patients

**Biologic therapies:**

*Anti-TNF (first generation):*
- Adalimumab, infliximab, etanercept, certolizumab: ~60% PASI 75; well-established safety; screen TB; avoid live vaccines; second-line now in many guidelines due to superior efficacy of anti-IL-17/IL-23

*Anti-IL-12/23 (targeting p40 subunit):*
- **Ustekinumab (Stelara):** SC Q12W maintenance; ~70% PASI 75; excellent safety; but less efficacious than anti-IL-17/IL-23 in direct comparisons; dual approval for psoriasis and PsA

*Anti-IL-17 (most efficacious skin class):*
- **Secukinumab (Cosentyx, anti-IL-17A):** SC weekly × 5 then monthly; ERASURE/FIXTURE trials: ~77% PASI 90 at week 16; 59% PASI 100 at week 52 — first biologic to reach >50% complete clearance in trials [^langley-2014-secukinumab]; approved psoriasis, PsA, AS, nr-axSpA
- **Ixekizumab (Taltz, anti-IL-17A):** SC biweekly × 3 then monthly; slightly superior to secukinumab in IXORA-S head-to-head; ~81% PASI 90 at week 12
- **Bimekizumab (Bimzelx, anti-IL-17A/F):** Dual IL-17A and IL-17F blockade; BE READY trial: 67% PASI 100 (complete clearance) at week 16 — highest complete clearance rate; oral candidiasis higher (~10%) due to dual IL-17 blockade; SC monthly after initial doses; EU approved 2023, FDA approved 2023

*Anti-IL-23 p19 (most selective, best-in-class durability):*
- **Risankizumab (Skyrizi):** Anti-IL-23 p19; SC Q12W after 2 Q4W doses; UltIMMa-1/2: 75% PASI 90 at week 16; 56% PASI 100 at 52 weeks; superior to ustekinumab and adalimumab in head-to-heads; approved psoriasis, PsA, CD, UC [^gordon-2018-risankizumab]
- **Guselkumab (Tremfya):** Anti-IL-23 p19; SC Q8W; VOYAGE trials: 73% PASI 90 at week 24
- **Tildrakizumab (Ilumya):** Anti-IL-23 p19; Q12W; approved moderate-severe plaque psoriasis
- **Deucravacitinib (Sotyktu, TYK2 inhibitor):** Oral; inhibits TYK2 pseudokinase (allosteric) → reduces IL-23 and IL-12 signaling; POETYK PSO-1/2: 53-58% PASI 75 vs. 35% apremilast; FDA approved 2022; oral biologic-like efficacy; no VTE/MACE boxed warning unlike pan-JAK inhibitors

## Connections

- `connects-to` → **[T Helper Cell](../../04-cellular/t-helper-cell/README.md)** — Th17 cells are the primary psoriasis pathogenic effectors; IL-17A/F activate keratinocyte NF-kB and STAT3 → AMP expression, CXCL8, and S100 proteins → neutrophil recruitment and epidermal hyperproliferation; IL-22 drives keratinocyte proliferation and anti-apoptotic programs.
- `connects-to` → **[TNF-alpha](../../03-molecular/tnf-alpha/README.md)** — TNF-alpha activates keratinocyte NF-kB → CXCL1/IL-8, ICAM-1, and survival genes → epidermal thickening and vascular activation; adalimumab, infliximab, etanercept, and certolizumab achieve ~60% PASI 75 in plaque psoriasis and treat psoriatic arthritis.
- `connects-to` → **[IL-6](../../03-molecular/il-6/README.md)** — IL-6 amplifies Th17 polarization (with TGF-beta) in psoriasis; STAT3-dependent keratinocyte hyperproliferation; elevated serum IL-6 correlates with psoriasis severity and psoriatic arthritis activity; IL-6 trans-signaling drives systemic cardiovascular risk.
- `connects-to` → **[NF-kB](../../03-molecular/nf-kb/README.md)** — NF-kB activated in psoriatic keratinocytes by TNF-alpha and IL-17A → AMP expression (LL-37, beta-defensins), CXCL8 (neutrophil chemotaxis), and CCL20 (DC recruitment); CARD14 gain-of-function mutations constitutively activate keratinocyte NF-kB → psoriasis without external trigger.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — IL-23 from dermal DCs activates Th17 and γδ T cells → IL-17A/F and IL-22 → keratinocyte hyperproliferation, acanthosis, and neutrophil recruitment in psoriatic plaques; anti-IL-23p19 antibodies (risankizumab, guselkumab) achieve PASI 90 response in ~50% of patients.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — IL-17A from skin Th17 and γδ T cells activates keratinocyte IL-17RA/RC → NF-kB → CXCL8, S100A proteins, and AMPs → neutrophil influx and epidermal hyperproliferation; secukinumab (anti-IL-17A) and ixekizumab achieve PASI 90 in ~60% of plaque psoriasis patients at 16 weeks.
- `connects-to` → **[IL-31](../../03-molecular/il-31/README.md)** — IL-31 contributes to pruritus in psoriasis despite the Th17 cytokine environment; psoriatic skin ILC2 cells produce IL-31; IL-31 correlates with itch VAS independently of PASI; JAK inhibitors (deucravacitinib, upadacitinib) reduce psoriatic inflammation and IL-31-mediated itch.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Narrow-band UVB (311–313 nm) phototherapy induces T-cell apoptosis in psoriatic plaques and suppresses the Th17/IL-17A axis; NBUVB achieves PASI 75 in 50–70% of patients; safe in pregnancy; requires 2–3 sessions/week for 6–10 weeks induction.
- `connects-to` → **[Ankylosing Spondylitis](../ankylosing-spondylitis/README.md)** — Psoriasis and AS sit on the spondyloarthritis spectrum, sharing the IL-23/Th17→IL-17A axis and responding to IL-17 (secukinumab, ixekizumab) and IL-23 blockade; ~20-30% of psoriasis patients develop inflammatory arthritis, and axial psoriatic arthritis overlaps with AS.
- `connects-to` → **[Psoriatic Arthritis](../psoriatic-arthritis/README.md)** — Up to ~30% of plaque-psoriasis patients develop psoriatic arthritis, usually years after skin disease; both share the IL-23/Th17→IL-17A/TNF axis, so IL-17, IL-23 and TNF inhibitors treat skin and joints together; nail and scalp psoriasis flag higher PsA risk.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — Psoriasis is the archetypal immune-mediated skin disease: Th17-derived IL-17A/IL-22 drive keratinocyte hyperproliferation → thickened scaly plaques with parakeratosis and acanthosis; epidermal turnover shortens from ~28 to ~4 days, and skin is the primary treated site.
- `connects-to` → **[Atopic Dermatitis](../atopic-dermatitis/README.md)** — Psoriasis and atopic dermatitis are the two major inflammatory skin diseases but immunologically opposite: psoriasis is Th17/IL-23-driven with sharp scaly plaques, while atopic dermatitis is Th2-driven with itchy, ill-defined eczema—dictating different biologics.
- `connects-to` → **[Inflammatory Bowel Disease](../inflammatory-bowel-disease/README.md)** — Psoriasis and inflammatory bowel disease share the IL-23/Th17 axis and co-occur: both respond to anti-IL-23 and anti-TNF biologics, though anti-IL-17 can paradoxically worsen Crohn's—so the shared pathway also constrains drug choice across the two diseases.
- `connects-to` → **[Atherosclerosis](../atherosclerosis/README.md)** — Psoriasis is an independent cardiovascular risk factor: chronic systemic Th17 inflammation accelerates atherosclerosis, so severe psoriasis raises heart attack and stroke risk beyond shared metabolic factors—and effective skin treatment may lower vascular inflammation.
- `connects-to` → **[Obesity](../obesity/README.md)** — Psoriasis and obesity are bidirectionally linked through inflammation: adipose-derived cytokines worsen psoriatic inflammation, while psoriasis raises metabolic-syndrome risk, so obese psoriasis patients have more severe disease and weight loss improves it.
- `connects-to` → **[Type 2 Diabetes](../type-2-diabetes/README.md)** — Psoriasis raises the risk of type 2 diabetes: shared systemic inflammation (TNF, IL-6, IL-17) drives insulin resistance, so psoriasis is an independent cardiometabolic risk factor—part of why it is now treated as a systemic, not just skin, disease.
- `connects-to` → **[Vitamin D (Calciferol)](../../../03-medicine/03-food/vitamin-d/README.md)** — Vitamin D both treats and modulates psoriasis: topical vitamin D analogs slow the hyperproliferation of psoriatic keratinocytes and are first-line therapy, while the immunomodulatory role of vitamin D ties skin immunity to this hormone—a vitamin used as a drug.
- `connects-to` → **[Cardiovascular system](../cardiovascular-system/README.md)** — Psoriasis is an independent cardiovascular risk factor: systemic IL-17/TNF inflammation accelerates atherosclerosis, so severe psoriasis raises heart-attack and stroke risk beyond its shared metabolic-syndrome links—reframing it as more than a skin disease.
- `connects-to` → **[Dendritic Cell](../../04-cellular/dendritic-cell/README.md)** — Plasmacytoid dendritic cells ignite psoriasis: they sense self-DNA and release type I interferon that, with myeloid dendritic cells, launches the IL-23/Th17 cascade—so dendritic cells sit at the very start of the inflammatory loop that thickens the skin.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — IL-12/IL-23 sit at the heart of psoriasis: their shared p40 subunit drives the Th1/Th17 response that fuels keratinocyte hyperproliferation, which is why ustekinumab (anti-p40) and IL-23-specific biologics clear psoriasis plaques so effectively.
- `connects-to` → **[Neutrophil](../../04-cellular/neutrophil/README.md)** — Neutrophils mark the psoriatic plaque: they swarm into the epidermis to form Munro microabscesses, and in pustular psoriasis they fill visible pustules—so although T cells drive the disease, neutrophils are its histologic signature and dominate its pustular forms.
- `connects-to` → **[Streptococcus pyogenes](../../../02-pathogen/02-bacteria/streptococcus-pyogenes/README.md)** — Strep throat can ignite psoriasis: streptococcal infection classically triggers guttate psoriasis, especially in children, as bacterial superantigens activate T cells that cross-react with skin—one of the clearest infection-to-autoimmunity links in dermatology.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — Psoriasis carries a heavy mental-health toll: visible plaques, stigma, and chronic inflammation roughly double the risk of depression and suicidal thoughts, so screening for depression is part of good psoriasis care—and clearing skin often lifts mood.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — Oral JAK and TYK2 inhibitors now treat psoriasis: blocking JAK-family signaling downstream of IL-23 and other cytokines (e.g., deucravacitinib targeting TYK2) controls plaques without injections, extending the IL-23/IL-17-targeted revolution to pills.
- `connects-to` → **[NASH](../nash/README.md)** — Psoriasis and fatty-liver disease travel together: shared systemic inflammation and metabolic syndrome raise the risk of MASH in psoriasis patients, part of why psoriasis is now seen as a systemic inflammatory disease, not just skin-deep.
- `connects-to` → **[Cytotoxic T Cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Psoriasis plaques recur in the same spots because of cytotoxic T cells: epidermal resident-memory CD8 T cells persist after lesions clear, forming a 'disease memory' that reignites plaques at old sites—why the disease relapses where it was.
- `connects-to` → **[Cortisol](../../03-molecular/cortisol/README.md)** — Psoriasis is first treated with cortisol's kin: topical corticosteroids calm the IL-17/Th17 inflammation driving the plaques, the most-used therapy—though rebound on stopping and skin thinning limit long-term potent use.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Psoriasis is treated by restoring keratinocyte calcium signaling: vitamin D analogs (calcipotriol) normalize the calcium-dependent differentiation that runs amok in psoriatic skin, slowing the overgrowth—often paired with a steroid.
- `connects-to` → **[Regulatory T Cell](../../04-cellular/regulatory-t-cell/README.md)** — Psoriasis reflects failed restraint by regulatory T cells: dysfunctional Tregs let the IL-23/Th17 axis run unchecked against the skin, so the imbalance between effector and regulatory T cells underlies the chronic plaques.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — Psoriasis travels with fatty liver: its systemic inflammation and shared metabolic syndrome make non-alcoholic fatty liver disease common, and the methotrexate used to treat psoriasis can itself scar the liver, so liver health must be watched.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — Psoriatic plaques are richly vascular: VEGF drives dermal endothelial cells to build dilated, leaky capillaries near the surface, which is why scraping a plaque produces pinpoint bleeding (the Auspitz sign).
- `connects-to` → **[Sodium](../../02-atomic/sodium/README.md)** — Salt may inflame psoriasis: high sodium accumulates in skin and pushes naive T cells toward the IL-17-producing Th17 lineage that drives psoriatic plaques, a dietary link between salt and the disease's core immune axis.
- `connects-to` → **[Peripheral Nerve](../../05-tissue/peripheral-nerve/README.md)** — Psoriasis itches and reacts through nerves: sensory peripheral-nerve fibers, fired by IL-31 and inflammation, carry the itch, and nerve injury can clear plaques in a denervated patch—evidence the skin's nerves help sustain the disease.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — Psoriasis is more than skin-deep: its systemic inflammation accelerates atherosclerosis, so severe disease raises the risk of heart attack independently of the usual cardiovascular risk factors.
- `connects-to` → **[Mast Cell](../../04-cellular/mast-cell/README.md)** — Mast cells lurk in psoriatic skin: degranulating near nerves and vessels, they release mediators that amplify the early inflammation and itch, linking neurogenic triggers to the plaque.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy shows the psoriatic plaque's hyperdrive: keratinocytes pile up far too fast with retained nuclei in the surface scale, and neutrophils collect into Munro microabscesses, the ultrastructure of runaway epidermal turnover.
- `connects-to` → **[Eye](../../06-organ/eye/README.md)** — Psoriasis can inflame the eye: it is associated with uveitis, conjunctivitis, and dry, scaly blepharitis of the lids, ocular involvement that parallels the immune attack on the skin and joints.
- `connects-to` → **[Zinc](../../02-atomic/zinc/README.md)** — Zinc matters to the psoriatic skin: levels often run low in the rapidly shedding epidermis, and because the mineral fuels skin repair and tempers inflammation, its deficiency can aggravate the plaques.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — Psoriasis itches and flares through the nerves: sensory neurons in the plaque release substance P and CGRP that fuel neurogenic inflammation, the same wiring behind the stress-triggered flares and the maddening itch.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — Treating psoriasis keeps an eye on the lungs: methotrexate can rarely cause a hypersensitivity pneumonitis, and the TNF and IL-17 biologics that clear the plaques raise the risk of pneumonia and reactivated tuberculosis.
- `connects-to` → **[Adipocyte](../../04-cellular/adipocyte/README.md)** — Psoriasis and fat inflame each other: enlarged adipocytes pour out the same cytokines that drive the plaques, so obesity worsens psoriasis and blunts treatment — a metabolic link in the 'psoriatic march' toward heart disease.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — Antibodies revolutionized psoriasis care: monoclonal antibodies against TNF, IL-17, and IL-23 (secukinumab, guselkumab, ustekinumab) clear the plaques by neutralizing the exact cytokines driving them, often where older drugs failed.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — Skin disease reaches intimate places: genital psoriasis and the visible plaques impair sexual health and self-image, while pregnancy often calms psoriasis through its immune shift, only for it to flare again after delivery.
- `connects-to` → **[Gut Microbiome](../gut-microbiome/README.md)** — A gut-skin axis links plaque to flora: psoriasis patients show gut dysbiosis and a high overlap with inflammatory bowel disease, the shared mucosal-barrier and IL-23 immunology tying the bowel's microbes to the skin's inflammation.
- `connects-to` → **[IL-36](../../03-molecular/il-36/README.md)** — A different cytokine drives the pustular form: in generalized pustular psoriasis, loss of the IL-36 receptor antagonist unleashes IL-36, flooding the skin with neutrophils into sterile pustules — now treatable by the IL-36 blocker spesolimab.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Plaques keep their own inflammatory engine: dermal macrophages pour out TNF and recruit more immune cells, sustaining the lesion and feeding the systemic inflammation that links psoriasis to heart and metabolic disease.
- `connects-to` → **[HIV/AIDS](../hiv-aids/README.md)** — HIV paradoxically ignites psoriasis: as immunity collapses the disease often appears or turns severe and treatment-resistant, a striking exception to its T-cell-driven model that improves with antiretroviral therapy.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — A transcription hub turns on the plaque: IL-23 signals through STAT3 to sustain the Th17/IL-17 response and the keratinocyte overgrowth of psoriasis, the node that TYK2-JAK inhibitors like deucravacitinib block.
- `connects-to` → **[Candida albicans](../../../02-pathogen/03-fungi/candida-albicans/README.md)** — A fungus can light the fuse: like streptococcal throat infection, Candida colonization acts as a microbial trigger and superantigen that flares psoriasis, and patients carry the yeast more often.
- `connects-to` → **[Stroke](../stroke/README.md)** — The skin disease reaches the brain's arteries: psoriasis's systemic inflammation accelerates atherosclerosis, raising the risk of stroke and heart attack independently of the usual cardiovascular risk factors.
- `connects-to` → **[Venous Thromboembolism](../venous-thromboembolism/README.md)** — Chronic inflammation clots the veins too: beyond its arterial risk, severe psoriasis is independently linked to a higher rate of deep-vein thrombosis and pulmonary embolism, part of the prothrombotic state of systemic inflammatory disease.
- `connects-to` → **[Alcohol Use Disorder](../alcohol-use-disorder/README.md)** — Drink and disease worsen each other: alcohol use disorder is over-represented in psoriasis and both triggers flares and blunts treatment response, a bidirectional link tangled with the disease's psychological burden.
- `connects-to` → **[Sepsis](../sepsis/README.md)** — Severe forms strip the skin's defense: erythrodermic and generalized pustular psoriasis breach the barrier across most of the body, letting bacteria invade — a route to bloodstream infection and sepsis compounded by immunosuppressive therapy.
- `connects-to` → **[Gout](../gout/README.md)** — Rapid skin turnover floods the blood with urate: the accelerated epidermal proliferation of psoriasis raises uric acid production, so hyperuricemia and gout are notably more common in people with the disease.
- `connects-to` → **[Chronic Kidney Disease](../ckd/README.md)** — Systemic inflammation reaches the kidney: moderate-to-severe psoriasis is independently associated with chronic kidney disease, and some of its systemic and biologic therapies add their own renal considerations.
- `connects-to` → **[Hepatitis B Virus](../../../02-pathogen/01-viruses/hepatitis-b-virus/README.md)** — Its biologics can reactivate the virus: the TNF inhibitors and other immunosuppressants used for psoriasis can reawaken latent hepatitis B, so screening and antiviral prophylaxis precede starting these therapies.
- `connects-to` → **[Tuberculosis](../tuberculosis/README.md)** — TNF blockade can wake latent TB: the anti-TNF biologics used for moderate-to-severe psoriasis disable the cytokine that walls off tuberculosis, so screening and treatment of latent infection precede therapy.
- `connects-to` → **[Generalized Anxiety Disorder](../generalized-anxiety-disorder/README.md)** — Visible disease feeds chronic worry: the stigma, unpredictability and social impact of psoriasis drive anxiety alongside its well-known depression, worsening quality of life independent of skin severity.
- `connects-to` → **[DLBCL](../dlbcl/README.md)** — Severe disease and its therapy nudge lymphoma risk: chronic immune activation in severe psoriasis, and the immunosuppressants used to treat it, are associated with a modestly raised risk of lymphoma.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — It is the archetypal skin disease: psoriasis drives hyperproliferation of the epidermis into well-demarcated scaly plaques, with nail pitting and scalp involvement, the visible core of the disorder.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — It travels with metabolic and thyroid disease: psoriasis is strongly tied to the insulin resistance and metabolic syndrome of endocrine dysfunction and shows raised rates of autoimmune thyroid disease.
- `connects-to` → **[Varicella-Zoster Virus](../../../02-pathogen/01-viruses/varicella-zoster-virus/README.md)** — Its biologics reawaken shingles: the TNF, IL-17/23 and especially JAK inhibitors used for moderate-to-severe psoriasis blunt antiviral immunity and raise the risk of herpes-zoster reactivation.
- `connects-to` → **[Immune System](../immune-system/README.md)** — It runs on the IL-23/IL-17 axis: psoriasis is a T-cell-driven autoinflammatory disease in which dendritic cells, IL-23 and IL-17 inflame the skin — the pathway every modern biologic targets.
- `connects-to` → **[Respiratory System](../respiratory-system/README.md)** — A core drug can scar the lungs: methotrexate, a mainstay systemic therapy for psoriasis, can cause hypersensitivity pneumonitis and pulmonary fibrosis, requiring vigilance for new breathlessness.
- `connects-to` → **[Lymphatic System](../lymphatic-system/README.md)** — Extensive disease swells the nodes: erythrodermic and widespread psoriasis causes reactive dermatopathic lymphadenopathy, and severe disease carries a modestly increased lymphoma risk.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — Nails and entheses warn of joint disease: nail pitting, enthesitis and dactylitis are early musculoskeletal signs that herald the psoriatic arthritis affecting up to a third of patients.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — It shares a path with bowel disease and its drugs hit the liver: psoriasis overlaps inflammatory bowel disease through shared inflammation, and methotrexate therapy for it is hepatotoxic.
- `connects-to` → **[Renal System](../renal-system/README.md)** — Severe disease and its drugs reach the kidney: extensive psoriasis independently raises chronic kidney disease risk, and cyclosporine used to control it is nephrotoxic.
- `connects-to` → **[Adalimumab](../../../03-medicine/01-modern/11-biologics/adalimumab/README.md)** — Biologics clear severe disease: anti-TNF agents like adalimumab, with IL-17 and IL-23 inhibitors, are transformative for moderate-to-severe psoriasis and its arthritis.
- `connects-to` → **[Corticosteroids](../../../03-medicine/01-modern/02-respiratory/corticosteroids/README.md)** — Topical steroids are first-line, systemic ones risky: potent topical corticosteroids treat plaques, but systemic steroids are avoided as withdrawal can trigger life-threatening pustular psoriasis flares.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — Stress and the skin talk both ways: psychological stress triggers psoriasis flares through the brain-skin neuroimmune axis, and the visible disease in turn drives anxiety and depression.
- `connects-to` → **[Targeted Therapy](../../../03-medicine/01-modern/13-cancer/targeted-therapy/README.md)** — Cytokine-targeted biologics transformed it: monoclonals against IL-17 and IL-23 (secukinumab, guselkumab), anti-TNF, and oral TYK2/JAK inhibitors now clear severe psoriasis by blocking the IL-23/IL-17 axis that drives it.
- `connects-to` → **[Cancer Chemotherapy](../../../03-medicine/01-modern/13-cancer/cancer-chemotherapy/README.md)** — Methotrexate is the classic systemic DMARD: low-dose methotrexate, a chemotherapy antimetabolite, has long treated extensive psoriasis and psoriatic arthritis, used before or alongside the newer biologics.
- `connects-to` → **[Arterial Wall](../../05-tissue/arterial-wall/README.md)** — Skin inflammation reaches the arteries: the systemic inflammation of psoriasis accelerates atherosclerosis of the arterial wall — the 'psoriatic march' — raising cardiovascular risk independent of traditional factors.
- `connects-to` → **[Multiple Sclerosis](../multiple-sclerosis/README.md)** — A caution for its TNF blockers: the anti-TNF biologics used for psoriasis can unmask or worsen demyelination, so multiple sclerosis contraindicates them—and paradoxically anti-TNF therapy can itself induce psoriasis.
- `connects-to` → **[IgA Nephropathy](../iga-nephropathy/README.md)** — A skin-kidney axis: psoriasis is associated with IgA nephropathy through shared mucosal IL-17/IL-23 immunity, and its TNF-inhibitor therapy can also trigger IgAN.
- `connects-to` → **[Hepatitis B](../hepatitis-b/README.md)** — Immunosuppression reawakens the virus: TNF inhibitors and methotrexate used for psoriasis can reactivate hepatitis B and are hepatotoxic, so HBV screening precedes systemic therapy.
- `connects-to` → **[Type 1 Diabetes](../type-1-diabetes/README.md)** — Shared autoimmune ground: psoriasis is associated with a higher risk of type 1 diabetes, the two sharing immune-regulatory susceptibility loci beyond psoriasis's better-known link to type 2 diabetes.
- `connects-to` → **[Heart Failure](../heart-failure/README.md)** — Inflammation and the failing heart: severe psoriasis independently raises the risk of heart failure, its chronic systemic inflammation contributing beyond shared cardiovascular risk factors.
- `connects-to` → **[Social Anxiety Disorder](../social-anxiety-disorder/README.md)** — The psychosocial wound: visible psoriatic plaques carry stigma that drives social anxiety, avoidance and depression, a quality-of-life burden disproportionate to the body-surface area involved.
- `connects-to` → **[PTCL](../ptcl/README.md)** — A great mimic: cutaneous T-cell lymphoma (mycosis fungoides) produces scaly erythematous plaques that imitate psoriasis and is sometimes mistreated as it for years, a malignant differential to keep in mind.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — Dermal angiogenesis: psoriatic plaques are richly vascularised through VEGF-driven new vessel growth in the dermal papillae, the basis of the pinpoint bleeding (Auspitz sign) when a scale is removed.
- `connects-to` → **[COVID-19 Disease](../covid-19-disease/README.md)** — Flares and immunosuppression: COVID-19 and its vaccines can trigger psoriasis flares, while the biologics that control it raised questions about infection risk during the pandemic.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — Innate amplifier: IL-1β released by keratinocytes and myeloid cells helps ignite the IL-23/IL-17 axis, linking innate immune activation to the inflammatory loop of psoriasis.
- `connects-to` → **[NLRP3 Inflammasome](../../03-molecular/nlrp3-inflammasome/README.md)** — Inflammasome trigger: NLRP3-inflammasome activation in psoriatic skin drives IL-1β maturation, with the autoantigen LL-37 among the signals that prime this innate response.
- `connects-to` → **[HIF-1α](../../03-molecular/hif-1alpha/README.md)** — Hypoxic plaques: thickened, hyperproliferative psoriatic epidermis becomes hypoxic, stabilising HIF-1α to drive the VEGF angiogenesis and metabolic shift of the lesions.
- `connects-to` → **[Type I Interferon](../../03-molecular/type-i-interferon/README.md)** — Disease initiation: plasmacytoid dendritic cells sensing LL-37–self-DNA complexes pour out type I interferon, the early event that ignites the dendritic-cell activation launching the psoriasis cascade.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — Keratinocyte alarmin: S100A8/A9 (calprotectin) is massively upregulated in psoriatic keratinocytes, amplifying neutrophil recruitment and inflammation and serving as a biomarker of disease activity.
- `connects-to` → **[EGFR](../../03-molecular/egfr/README.md)** — Epidermal hyperproliferation: EGFR signalling drives the rapid keratinocyte proliferation that thickens psoriatic plaques, the cellular basis of the scaling and accelerated epidermal turnover.
- `connects-to` → **[CCL2](../../03-molecular/ccl2/README.md)** — CCL2 produced in psoriatic skin draws monocytes and dendritic-cell precursors into the plaque, replenishing the antigen-presenting cells that sustain the IL-23/IL-17 inflammatory loop driving the disease.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — Keratinocyte and dendritic-cell cGAS-STING activation by self-DNA amplifies the type-I-interferon response, reinforcing the innate ignition phase (with LL-37–DNA complexes) that initiates and perpetuates psoriatic inflammation.
- `connects-to` → **[TGF-β](../../03-molecular/tgf-beta/README.md)** — TGF-β1 is overexpressed in psoriatic skin where, alongside its angiogenic effects, it contributes paradoxically to the abnormal keratinocyte proliferation and the inflammatory milieu of the plaque rather than its usual growth-suppressive role.
- `connects-to` → **[Glucocorticoid receptor](../../03-molecular/glucocorticoid-receptor/README.md)** — Corticosteroids acting through the glucocorticoid receptor are the most widely used topical therapy for psoriasis, broadly suppressing the keratinocyte and immune inflammation of the plaque, often combined with vitamin-D analogues.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Vitamin-D analogues like calcipotriol act on the keratinocyte calcium-differentiation program that is disordered in psoriasis, normalizing the abnormal proliferation and maturation of the epidermis in the plaque.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Leptin is elevated in psoriasis and promotes Th17 responses, mechanistically tying the disease to the obesity, metabolic syndrome and cardiovascular risk that are its major systemic comorbidities.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — EGFR-driven ERK signaling (EGFR already mapped) propels the keratinocyte hyperproliferation that thickens the psoriatic plaque, the epidermal response to the inflammatory cytokine milieu.
- `connects-to` → **[IFN-gamma](../../03-molecular/ifn-gamma/README.md)** — Th1-derived IFN-γ contributes to the early and chronic inflammation of psoriasis alongside the dominant IL-23/IL-17 axis already mapped, activating keratinocytes and dendritic cells.
- `connects-to` → **[Interleukin-10](../../03-molecular/il-10/README.md)** — A relative deficiency of regulatory IL-10 in psoriatic skin fails to restrain the Th17 inflammation, an imbalance that helps sustain the chronic plaque.
- `connects-to` → **[MYD88](../../03-molecular/myd88/README.md)** — The IL-36 and IL-1 receptors (IL-36 and IL-1β mapped) and TLRs signal through MyD88 to NF-κB (mapped), amplifying the innate inflammation that drives psoriatic plaques, especially pustular psoriasis.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — PI3K-AKT-mTOR signaling drives the keratinocyte hyperproliferation that thickens the psoriatic epidermis into its characteristic scaly plaque.
- `connects-to` → **[E2F1](../../03-molecular/e2f1/README.md)** — Cyclin-D-CDK4/6 release of E2F1 shortens keratinocyte cell-cycle time, compressing epidermal turnover from weeks to days in the psoriatic plaque.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — PI3K-AKT-mTOR signaling (mTOR mapped) drives the keratinocyte hyperproliferation and survival that thickens the psoriatic epidermis.
- `connects-to` → **[NRF2](../../03-molecular/nfe2l2/README.md)** — NRF2 antioxidant signaling is dysregulated in psoriatic keratinocytes, linking the oxidative-stress milieu of the plaque to barrier and inflammatory abnormalities.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Complement activation with C3 deposition contributes to neutrophil recruitment and the innate inflammatory amplification of psoriatic lesions.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Galectin-3 modulates keratinocyte and immune-cell crosstalk and amplifies the innate inflammation of psoriatic plaques.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — IFN-STAT1 signaling (type-I interferon already mapped) drives the early interferon-skewed innate activation that precedes the Th17 inflammation of psoriasis.
- `connects-to` → **[SMAD4](../../03-molecular/smad4/README.md)** — TGF-β-SMAD signaling (TGF-β already mapped) shapes the dysregulated keratinocyte proliferation and differentiation of the psoriatic epidermis.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — FOXO regulates keratinocyte differentiation and oxidative-stress balance, programs disrupted in the hyperproliferative epidermis of psoriasis.
- `connects-to` → **[CDK4/6](../../03-molecular/cdk4-6/README.md)** — CDK4/6-driven cell-cycle entry (E2F1 already mapped) sustains the keratinocyte hyperproliferation that builds the psoriatic plaque.
- `connects-to` → **[Perforin](../../03-molecular/perforin/README.md)** — Perforin-expressing cytotoxic CD8 (Tc17) T cells in the epidermis contribute to the keratinocyte targeting and lesion formation of psoriasis.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β modulates the NF-κB-driven inflammatory and keratinocyte-proliferative signaling of psoriasis.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — PI3K (PIK3CA)-AKT signaling (AKT already mapped) drives the keratinocyte hyperproliferation and immune-cell activation of psoriasis.
- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — SRC-family kinase signaling participates in the keratinocyte and immune-cell activation of the psoriatic plaque.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK-linked immunometabolic signaling shapes the keratinocyte and T-cell metabolism of psoriasis.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — Autophagy modulates the keratinocyte differentiation and innate immune responses of psoriasis.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — DNMT3A-mediated DNA methylation contributes to the epigenetic dysregulation of the keratinocyte and immune-cell programs of psoriasis.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-driven leukocyte recruitment into the skin contributes to the inflammatory infiltrate of psoriasis.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — CXCL12-CXCR4 signaling participates in the leukocyte trafficking and angiogenesis of psoriatic skin lesions.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — IL-33 alarmin signaling participates in the keratinocyte-driven inflammatory amplification of psoriasis.
- `connects-to` → **[ARID1A](../../03-molecular/arid1a/README.md)** — ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic regulation of the keratinocyte and immune gene programs of psoriasis.
- `connects-to` → **[Calcineurin](../../03-molecular/calcineurin/README.md)** — Calcineurin-NFAT signaling, a target of ciclosporin, participates in the T-cell activation of psoriasis.
- `connects-to` → **[Adenosine](../../03-molecular/adenosine/README.md)** — Adenosine signaling, a mechanism of methotrexate's anti-inflammatory action, participates in the immunomodulation of psoriasis.
- `connects-to` → **[MHC class II](../../03-molecular/mhc-class-ii/README.md)** — HLA-C association: the strongest genetic risk factor for psoriasis is HLA-C*06:02 (PSORS1), an MHC allele, and antigen presentation to T cells, including of the autoantigen LL-37, initiates the IL-23/IL-17 cascade already mapped.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — Metabolic comorbidity: psoriasis clusters with metabolic syndrome, and reduced levels of the protective adipokine adiponectin accompany the leptin excess already mapped, linking the systemic inflammation of psoriasis to its cardiometabolic risk.
- `connects-to` → **[Angiopoietin](../../03-molecular/angiopoietin/README.md)** — Plaque angiogenesis: psoriatic plaques show dilated, tortuous dermal capillaries driven by angiopoietin-Tie2 and VEGF (VEGF already mapped), the vascular change underlying the Auspitz sign of pinpoint bleeding on scale removal.
- `connects-to` → **[IL-2](../../03-molecular/il-2/README.md)** — T-cell activation: IL-2-driven T-cell activation and expansion sustain the pathogenic Th17 response of psoriasis, and calcineurin inhibitors (already mapped) that block IL-2 production, like ciclosporin, are effective systemic therapies.
- `connects-to` → **[Troponin complex](../../03-molecular/troponin-complex/README.md)** — Cardiovascular comorbidity: the systemic inflammation of psoriasis accelerates atherosclerosis (already mapped), and troponin elevation marks the myocardial injury of the increased cardiovascular events that shorten life in severe disease.
- `connects-to` → **[Xanthine oxidase](../../03-molecular/xanthine-oxidase/README.md)** — Hyperuricaemia: the rapid epidermal turnover of psoriasis raises purine catabolism through xanthine oxidase, elevating serum urate and increasing the risk of gout that accompanies the disease.
- `connects-to` → **[Cholesterol](../../03-molecular/cholesterol/README.md)** — Metabolic dyslipidaemia: psoriasis is associated with an atherogenic dyslipidaemia as part of its metabolic syndrome (leptin and adiponectin already mapped), contributing to the accelerated atherosclerosis (already mapped) and cardiovascular risk of severe disease.
- `connects-to` → **[Insulin](../../03-molecular/insulin/README.md)** — Insulin resistance: the systemic inflammation of psoriasis (TNF and IL-6 already mapped) promotes insulin resistance, and psoriasis is associated with an increased risk of type 2 diabetes (already mapped), part of its metabolic comorbidity.
- `connects-to` → **[Nitric oxide](../../03-molecular/nitric-oxide/README.md)** — Endothelial dysfunction: the chronic inflammation of psoriasis impairs endothelial nitric oxide, contributing to the vascular dysfunction and the increased cardiovascular events (troponin already mapped) that shorten life in severe disease.
- `connects-to` → **[Prostaglandins](../../03-molecular/prostaglandins/README.md)** — Inflammatory eicosanoids: prostaglandins and other arachidonic-acid metabolites in the psoriatic plaque (IL-6 and TNF already mapped) contribute to the inflammation and vascular changes of the lesion, part of its eicosanoid dimension.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — Type-2 counter-axis: IL-4 drives the type-2 immunity that opposes the Th17 (IL-17 and IL-23 already mapped) axis of psoriasis, and blocking IL-4 for atopic dermatitis can paradoxically unmask psoriasis, revealing the balance between the two.
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — Th2-Th17 balance: IL-13, with IL-4 (already mapped), defines the type-2 pole opposite the Th17 axis of psoriasis, the reciprocal relationship distinguishing it from the atopic dermatitis at the other end of the spectrum.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Metabolic adipokine: resistin, with leptin and adiponectin (already mapped), is part of the adipokine milieu linking psoriasis to the metabolic syndrome (insulin and cholesterol already mapped) and its systemic inflammation.
- `connects-to` → **[Hepcidin](../../03-molecular/hepcidin/README.md)** — Anaemia of chronic disease: the IL-6-driven (already mapped) hepcidin sequesters iron to produce the anaemia of chronic disease that can accompany the systemic inflammation of severe psoriasis.
- `connects-to` → **[Selenium](../../02-atomic/selenium/README.md)** — Selenium and skin oxidative defence: selenium supports the antioxidant selenoprotein defence of the skin, and low selenium status, common in psoriasis, is part of the oxidative and immune imbalance of the inflamed skin.
- `connects-to` → **[Zinc](../../02-atomic/zinc/README.md)** — Skin-barrier zinc: the zinc essential for the skin barrier and immunity; the zinc status is altered in psoriasis, and topical zinc is used in its management.
- `connects-to` → **[Atherosclerosis](../atherosclerosis/README.md)** — Psoriatic march: psoriasis carries an increased atherosclerosis (cholesterol already mapped) and cardiovascular risk from the systemic inflammation (TNF and IL-6 already mapped), the 'psoriatic march'.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Dermal macrophages: the dermal macrophages (TNF and IL-6 already mapped) contribute to the psoriatic skin inflammation and the systemic inflammatory comorbidity.
- `connects-to` → **[Natural killer cell](../../04-cellular/natural-killer-cell/README.md)** — Cutaneous NK/NKT: the NK and NKT cells (perforin already mapped) of the psoriatic skin contribute to the innate inflammation of the IL-17 (already mapped) axis of psoriasis.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Type-2 counter-arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 arm balancing the dominant Th17 (IL-17 and IL-23 already mapped) drive of psoriasis.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — Type-2 IgE: the IgE (with IL-4 and IL-13 already mapped) reflects the type-2 immune dimension present in a subset of psoriasis.
- `connects-to` → **[Complement C5](../../03-molecular/complement-c5/README.md)** — Complement in plaques: the C5 and its C5a fragment (with C3 already mapped) recruit the neutrophils of the Munro microabscesses and amplify the innate inflammation of the psoriatic plaque.
- `connects-to` → **[B cell](../../04-cellular/b-cell/README.md)** — Regulatory B-cell arm: the B cells, including the dysregulated regulatory B cells, are an increasingly recognised adaptive-immune component of psoriasis alongside the dominant Th17 (IL-17 and IL-23 already mapped) axis.
- `connects-to` → **[Plasma cell](../../04-cellular/plasma-cell/README.md)** — Lesional plasma cells: the plasma cells secreting the antibodies (already mapped) are found in the psoriatic lesions and contribute to the humoral dimension of psoriasis.
- `connects-to` → **[C5aR1](../../03-molecular/c5ar1/README.md)** — C5a receptor: the C5aR1 signalling (with the complement C3 and C5 already mapped) drives the neutrophil (already mapped) recruitment into the epidermis (the Munro microabscesses) of psoriasis.
- `connects-to` → **[TSLP](../../03-molecular/tslp/README.md)** — Keratinocyte alarmin: TSLP, released by the injured keratinocytes, is part of the alarmin (IL-33 already mapped) signalling that helps initiate the dendritic-cell (already mapped) activation of psoriasis.
- `connects-to` → **[Periostin](../../03-molecular/periostin/README.md)** — Dermal matricellular: periostin, in the psoriatic dermis, is part of the matricellular remodelling and amplification loop that sustains the chronic plaque inflammation of psoriasis.
- `connects-to` → **[Factor H](../../03-molecular/factor-h/README.md)** — Complement regulation: factor H regulates the alternative complement pathway (complement C3, C5 and C5aR1 already mapped) active in the inflamed psoriatic skin.
- `connects-to` → **[Osteopontin](../../03-molecular/osteopontin/README.md)** — Dermal matricellular: osteopontin, elevated in the psoriatic skin and serum, amplifies the Th17 (IL-17 and IL-23 already mapped) and myeloid inflammation of the psoriatic plaque.
- `connects-to` → **[Transferrin](../../03-molecular/transferrin/README.md)** — Chronic-disease iron: transferrin, the iron carrier, reflects the disordered iron handling (hepcidin already mapped) of the anaemia of the chronic systemic inflammation of psoriasis.
- `connects-to` → **[Bradykinin](../../03-molecular/bradykinin/README.md)** — Kinin-itch axis: bradykinin, released in the inflamed psoriatic skin by the kallikrein-kinin system, activates B2 receptors on keratinocytes (skin already mapped) and sensory neurons (already mapped), amplifying itch and the neuro-inflammatory dimension of psoriasis.
- `connects-to` → **[C1-Esterase Inhibitor](../../03-molecular/c1-esterase-inhibitor/README.md)** — Complement/kinin gate: C1-esterase inhibitor limits classical complement (C3, C5 and C5aR1 already mapped) and contact-kinin (bradykinin already mapped) over-activation in the inflamed psoriatic skin, moderating the immune-driven keratinocyte proliferation of psoriasis.
- `connects-to` → **[Erythropoietin](../../03-molecular/erythropoietin/README.md)** — Erythropoiesis support: erythropoietin counteracts the anaemia of chronic disease (hepcidin and transferrin already mapped) driven by the sustained systemic inflammation and the cytokine (IL-6 already mapped) burden of psoriasis.
- `connects-to` → **[Histamine](../../03-molecular/histamine/README.md)** — Mast-cell skin effector: histamine, released by mast cells (already mapped) in psoriatic skin, promotes keratinocyte (already mapped) proliferation via H1/H4 receptors and amplifies the vascular permeability and pruritogenic signalling of psoriasis.
- `connects-to` → **[Melatonin](../../03-molecular/melatonin/README.md)** — Circadian anti-inflammatory protection: melatonin, via MT1/MT2 receptors on keratinocytes (already mapped) and T cells (already mapped), suppresses the NF-κB/TNF-α axis (already mapped) and reduces the oxidative stress driving the inflammatory plaque of psoriasis.
- `connects-to` → **[Prolactin](../../03-molecular/prolactin/README.md)** — Immune-endocrine skin axis: prolactin, acting via PRLR on keratinocytes (already mapped) and T-helper cells (already mapped), potentiates the Th17/IL-17 axis (already mapped) and the female-predominant hormonal amplification of the chronic plaque inflammation of psoriasis.
- `connects-to` → **[Testosterone](../../03-molecular/testosterone/README.md)** — PsO testosterone: testosterone, via androgen receptors on skin (already mapped) keratinocytes, suppresses the IL-17A (already mapped)/NF-κB (already mapped) axis; androgen deficiency amplifies T-helper-cell (already mapped) Th17 activation and the plaque burden of psoriasis.
- `connects-to` → **[Serotonin](../../03-molecular/serotonin/README.md)** — PsO serotonin: serotonin, via 5-HT2 on skin (already mapped) keratinocytes, amplifies keratinocyte hyperproliferation and T-helper-cell (already mapped) Th17 activation; 5-HT also promotes NF-κB (already mapped) plaque inflammation and the vascular permeability of psoriasis.
- `connects-to` → **[Oxytocin](../../03-molecular/oxytocin/README.md)** — PsO oxytocin: oxytocin, via OXTR on regulatory T cells (already mapped) and dendritic cells (already mapped), attenuates IL-23 (already mapped)/Th17 axis; oxytocin also suppresses NF-κB (already mapped) and skin (already mapped) keratinocyte hyperproliferation of psoriasis.
- `connects-to` → **[Vasopressin](../../03-molecular/vasopressin/README.md)** — PsO vasopressin: vasopressin, via V1a receptors on keratinocytes and dendritic cells (already mapped), amplifies NF-κB (already mapped) plaque inflammation; vasopressin also modulates vascular permeability and the IL-17A (already mapped) Th17 axis of psoriasis.
- `connects-to` → **[Iodine](../../02-atomic/iodine/README.md)** — PsO iodine: iodine-dependent thyroid hormones regulate keratinocyte (already mapped) proliferation and skin (already mapped) barrier; thyroid-hormone deficiency amplifies the NF-κB (already mapped) plaque inflammation and the IL-17A (already mapped) Th17 axis of psoriasis.
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — PsO magnesium: magnesium regulates NF-κB (already mapped) activity and mast-cell (already mapped) degranulation driving psoriatic plaque formation; magnesium deficiency amplifies keratinocyte hyperproliferation and the IL-17A (already mapped) inflammatory axis of psoriasis.

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^nestle-2009-psoriasis-review]: Nestle FO, Kaplan DH, Barker J. Psoriasis. *N Engl J Med.* 2009;361(5):496-509. [doi:10.1056/NEJMra0804595](https://doi.org/10.1056/NEJMra0804595) · [PubMed 19641206](https://pubmed.ncbi.nlm.nih.gov/19641206/)
[^langley-2014-secukinumab]: Langley RG, Elewski BE, Lebwohl M, et al. Secukinumab in plaque psoriasis — results of two phase 3 trials. *N Engl J Med.* 2014;371(4):326-338. [doi:10.1056/NEJMoa1406095](https://doi.org/10.1056/NEJMoa1406095) · [PubMed 25007392](https://pubmed.ncbi.nlm.nih.gov/25007392/)
[^gordon-2018-risankizumab]: Gordon KB, Strober B, Lebwohl M, et al. Efficacy and safety of risankizumab in moderate-to-severe plaque psoriasis (UltIMMa-1 and UltIMMa-2). *Lancet.* 2018;392(10148):650-661. [doi:10.1016/S0140-6736(18)31713-6](https://doi.org/10.1016/S0140-6736(18)31713-6) · [PubMed 30097359](https://pubmed.ncbi.nlm.nih.gov/30097359/)
