---
schema: human-scale-entry/v1
id: hereditary-angioedema
name: Hereditary Angioedema
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-07
summary: "Hereditary angioedema (HAE) is recurrent bradykinin-mediated swelling from C1-INH deficiency; laryngeal HAE causes asphyxiation. Icatibant (B2R antagonist) and C1-INH concentrate for acute attacks; berotralstat and lanadelumab for long-term prophylaxis."
aliases: ["HAE", "hereditary angioedema", "HAE type I", "HAE type II", "HAE type III", "C1 inhibitor deficiency", "SERPING1 deficiency", "bradykinin angioedema", "Quincke's edema"]
sources:
  - id: cicardi-2010-icatibant-nejm
    type: peer-reviewed
    cite: "Cicardi M, Banerji A, Bracho F, et al. Icatibant, a new bradykinin-receptor antagonist, in hereditary angioedema. N Engl J Med. 2010;363(6):532-541."
    doi: "10.1056/NEJMoa0906393"
    pmid: "20818873"
    url: "https://doi.org/10.1056/NEJMoa0906393"
  - id: maurer-2018-lanadelumab-help
    type: peer-reviewed
    cite: "Banerji A, Riedl MA, Bernstein JA, et al. Effect of lanadelumab compared with placebo on prevention of hereditary angioedema attacks: a randomized clinical trial. JAMA. 2018;320(20):2108-2121."
    doi: "10.1001/jama.2018.16773"
    pmid: "30480729"
    url: "https://doi.org/10.1001/jama.2018.16773"
  - id: zuraw-2020-berotralstat-apex2
    type: peer-reviewed
    cite: "Zuraw BL, Busse PJ, White M, et al. Berotralstat (BCX7353) for the prevention of hereditary angioedema. N Engl J Med. 2021;384(23):2186-2195."
    doi: "10.1056/NEJMoa2103679"
    pmid: "34077648"
    url: "https://doi.org/10.1056/NEJMoa2103679"
cross_links:
  - target: 01-human/03-molecular/c1-esterase-inhibitor
    relation: connects-to
    note: "C1-INH deficiency (type I: low antigen + activity; type II: low activity, normal antigen) → uncontrolled FXII/kallikrein → bradykinin excess → B2R-mediated vascular permeability → HAE attacks; icatibant, C1-INH concentrate, berotralstat, and lanadelumab are therapeutic targets."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "C1-INH deficiency → chronic C1 complex activation → C4 consumed even between attacks (key screening test); low C4 + low C1-INH activity = HAE type I/II diagnosis; C3 usually normal; C1q normal (distinguishes HAE from acquired angioedema with anti-C1q antibodies)."
  - target: 01-human/03-molecular/bradykinin
    relation: connects-to
    note: "HAE is the paradigmatic bradykinin-excess disease: C1-INH deficiency → uncontrolled FXII/kallikrein → bradykinin generation from HMWK; bradykinin binds B2R on postcapillary venules → Gαq/Ca²⁺ → eNOS/NO → vascular permeability; icatibant (B2R antagonist) aborts HAE attacks."
  - target: 01-human/03-molecular/angiotensin-ii
    relation: connects-to
    note: "ACE (kininase II) degrades bradykinin; ACEi block catabolism → bradykinin accumulation → angioedema (~0.1-0.7% of users); ACEi contraindicated in HAE; Ang-II and bradykinin are both ACE substrates → RAAS and kinin-kallikrein systems are mechanistically linked."
  - target: 01-human/03-molecular/thrombin
    relation: connects-to
    note: "Trauma/surgery → thrombin generation → FXII activation → contact cascade → kallikrein → bradykinin → HAE attack; surgical trauma triggers ~25-50% of HAE attacks; short-term C1-INH concentrate or icatibant before high-risk procedures prevents peri-operative attacks."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "Every HAE attack ends at the endothelial cell: bradykinin binds its B2 receptor on postcapillary venule endothelium → Gαq/Ca²⁺ → eNOS-derived NO loosens inter-endothelial junctions → plasma leaks into tissue as non-urticarial swelling; icatibant blocks B2R to abort this."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "HAE swelling is subcutaneous or submucosal and looks unlike allergic hives: ~50% of attacks are tense, non-pitting, non-urticarial skin swelling that lasts 2-5 days and does not itch or respond to antihistamines — reflecting its bradykinin (not histamine) mechanism."
  - target: 01-human/03-molecular/estrogen
    relation: connects-to
    note: "Estrogen worsens HAE by upregulating prekallikrein, boosting bradykinin generation; estrogen-containing contraceptives and pregnancy trigger attacks, and FXII (type III) HAE is largely a disease of women on the pill — so progestin-only contraception is advised."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "HAE is a disorder of complement regulation: C1-inhibitor normally restrains the classical complement pathway and the contact (kinin) system, so its deficiency consumes C4 (a diagnostic clue) and unleashes bradykinin; it sits between complement and innate immune control."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "HAE is the key bradykinin-mediated mimic of mast-cell angioedema: unlike histaminergic allergic angioedema (urticaria, itch, antihistamine response), HAE swelling is non-itchy, urticaria-free and unresponsive to antihistamines or epinephrine—telling them apart is life-saving."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "The liver synthesizes C1-inhibitor and most complement and contact-system proteins, so it underlies HAE: types I/II HAE reflect deficient or dysfunctional hepatic C1-INH, and siRNA therapy (donidalorsen targeting prekallikrein) acts on hepatic production to prevent attacks."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "Abdominal attacks are a major, often misdiagnosed feature of hereditary angioedema: bradykinin-driven edema of the bowel wall causes severe colicky pain, vomiting, and ascites that mimic a surgical abdomen, so recurrent crises with C1-inhibitor deficiency point to HAE."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "Laryngeal edema is the lethal manifestation of hereditary angioedema: bradykinin-mediated upper-airway swelling can cause asphyxiation, so patients carry on-demand C1-inhibitor or icatibant—and unlike histaminergic angioedema, it ignores epinephrine and antihistamines."
  - target: 01-human/07-system/hypertension
    relation: connects-to
    note: "ACE inhibitors can trigger bradykinin-mediated angioedema like HAE: ACE normally degrades bradykinin, so blocking it raises bradykinin and causes angioedema (especially in HAE patients), which is why ACE inhibitors are contraindicated in hereditary angioedema."
  - target: 01-human/03-molecular/complement-c5
    relation: connects-to
    note: "Hereditary angioedema reflects loss of C1-inhibitor's brake on the contact and complement systems: without it, kallikrein generates bradykinin while the classical complement pathway runs unchecked, consuming C4—so low C4 is the screening clue to HAE."
  - target: 01-human/07-system/asthma
    relation: connects-to
    note: "Hereditary angioedema and asthma both cause acute airway emergencies: HAE's bradykinin-driven laryngeal edema obstructs the upper airway and ignores bronchodilators and steroids, unlike asthma's smooth-muscle bronchospasm—so the distinction is life-saving."
  - target: 01-human/07-system/atopic-dermatitis
    relation: connects-to
    note: "Hereditary angioedema is the bradykinin-mediated counterpart to histamine-driven (allergic) angioedema seen with atopic dermatitis and urticaria: HAE lacks hives and ignores antihistamines, steroids and epinephrine—needing C1-INH or bradykinin-pathway drugs instead."
  - target: 01-human/06-organ/small-intestine
    relation: connects-to
    note: "Hereditary angioedema attacks the gut wall: bradykinin-driven edema of the small intestine causes severe colicky pain, vomiting and even obstruction, so HAE can mimic a surgical abdomen—and unexplained recurrent abdominal attacks should prompt C1-inhibitor testing."
  - target: 01-human/03-molecular/nitric-oxide
    relation: connects-to
    note: "Bradykinin drives HAE swelling through nitric oxide and vascular leak: it binds endothelial B2 receptors to release NO and open intercellular junctions, flooding tissue with fluid—the same vasodilator pathway behind blood-pressure control produces the edema."
  - target: 01-human/07-system/systemic-lupus-erythematosus
    relation: connects-to
    note: "Acquired C1-inhibitor deficiency mimics hereditary angioedema in autoimmune or lymphoproliferative disease: SLE and lymphomas can consume or block C1-INH, causing bradykinin angioedema later in life—so adult-onset angioedema without family history needs a workup."
  - target: 01-human/03-molecular/histamine
    relation: connects-to
    note: "Hereditary angioedema is bradykinin-, not histamine-driven—and that distinction is everything: unlike allergic angioedema and hives, HAE swelling does not respond to antihistamines, steroids, or epinephrine, so recognizing the non-histaminergic mechanism saves airways."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "Hereditary angioedema is shaped by the reproductive system: estrogen worsens attacks, so puberty, pregnancy, and the contraceptive Pill can trigger flares—and an estrogen-dependent FXII-linked form affects mainly women, making hormone choices central to care."
  - target: 01-human/04-cellular/smooth-muscle-cell
    relation: connects-to
    note: "HAE attacks hinge on smooth muscle: bradykinin relaxes vascular smooth muscle and opens endothelial junctions, flooding tissue with fluid—and in the gut, submucosal edema with smooth-muscle spasm causes severe abdominal pain that mimics a surgical abdomen."
  - target: 01-human/03-molecular/testosterone
    relation: connects-to
    note: "Androgens are a classic hereditary angioedema prophylaxis: attenuated androgens like danazol raise C1-inhibitor levels to prevent attacks—a striking contrast with estrogen, which worsens HAE—so sex hormones swing the disease in opposite directions."
  - target: 01-human/04-cellular/plasma-cell
    relation: connects-to
    note: "Acquired angioedema mimics HAE but comes from plasma cells: monoclonal gammopathy and lymphoproliferative disorders consume or autoantibody-target C1-inhibitor, so late-onset angioedema without family history prompts a search for a plasma-cell clone."
  - target: 01-human/07-system/lymphatic-system
    relation: connects-to
    note: "Angioedema overwhelms lymphatic fluid clearance: bradykinin makes deep dermal and submucosal vessels leak faster than the lymphatic system can drain, producing the firm, non-pitting swelling of HAE—unlike the histamine-driven hives of allergy."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "Hereditary angioedema's swelling is a permeability problem like VEGF's: bradykinin (and VEGF) pry apart endothelial junctions to let plasma flood into tissue, so the attacks are leaky-vessel edema, not the mast-cell hives of allergy."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Hereditary angioedema runs through the calcium-dependent contact system: factor XII and kallikrein activation that generates bradykinin needs calcium, the same cofactor of the clotting cascade—linking the kinin and coagulation pathways."
  - target: 01-human/03-molecular/cortisol
    relation: connects-to
    note: "Hereditary angioedema ignores cortisol—unlike allergic swelling: because the attacks are bradykinin-driven, not histamine-driven, steroids and antihistamines don't work, so the key is recognizing it and using C1-inhibitor or bradykinin blockers instead."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "A laryngeal hereditary angioedema attack can choke off oxygen: swelling of the throat and voice box obstructs the airway, the disease's most feared event, causing asphyxia that demands emergency airway management."
  - target: 01-human/06-organ/large-intestine
    relation: connects-to
    note: "Hereditary angioedema swells the bowel wall: attacks edema the gut, including the large intestine, causing severe colicky pain, vomiting, and wall thickening that can mimic a surgical abdomen and trigger needless operations."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "Hereditary angioedema hinges on bradykinin clearance in tissues like the kidney: enzymes (ACE, neprilysin) that degrade bradykinin act here, which is why ACE-inhibitor blood-pressure drugs can unmask or worsen bradykinin angioedema."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "The deadliest hereditary angioedema attacks swell the larynx and airway, threatening asphyxiation, which is why patients carry on-demand bradykinin-blocking rescue therapy for laryngeal attacks."
  - target: 01-human/04-cellular/hepatocyte
    relation: connects-to
    note: "C1-esterase inhibitor is made by hepatocytes, so the liver is the source of the very protein whose deficiency causes hereditary angioedema—and the target of newer liver-directed gene therapies."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "During a gut attack, CT and ultrasound photons reveal the telltale bowel-wall edema and free fluid, helping distinguish hereditary angioedema from a true surgical abdomen and avert needless operations."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy shows how the swelling forms: bradykinin pries open the junctions between endothelial cells, widening the gaps so plasma floods out into the tissue — the leak that makes the deep, non-itchy edema of an attack."
  - target: 01-human/06-organ/eye
    relation: connects-to
    note: "Attacks often disfigure the face and eyes: bradykinin-driven swelling balloons the lips and eyelids, sometimes closing the eyes entirely, a dramatic but self-limited facial angioedema that warns a laryngeal attack may follow."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "Rarely the swelling reaches the brain: case reports describe cerebral edema during severe attacks, with headaches, transient deficits, or seizures from bradykinin acting on the brain's blood vessels."
  - target: 01-human/06-organ/stomach
    relation: connects-to
    note: "Gut attacks masquerade as a surgical emergency: angioedema of the bowel wall brings severe cramping abdominal pain, vomiting, and even shock, mimicking an acute abdomen and leading to needless operations before the diagnosis is known."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "Antibodies enter on both sides of angioedema: the acquired form can be driven by autoantibodies against C1-inhibitor, while modern prophylaxis uses lanadelumab, a monoclonal antibody that blocks the kallikrein generating bradykinin."
  - target: 01-human/03-molecular/albumin
    relation: connects-to
    note: "An attack is plasma escaping the vessels: bradykinin opens the endothelial junctions so intravascular fluid floods the tissues, and severe abdominal attacks shift enough volume to cause hemoconcentration and a drop in blood pressure."
  - target: 01-human/06-organ/pancreas
    relation: connects-to
    note: "An abdominal attack mimics a surgical emergency: bradykinin swells the bowel wall into cramping pain, vomiting, and ascites that look like acute pancreatitis or appendicitis, leading to needless operations before HAE is recognized."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "Bradykinin is also a pain signal: the same kinin that swells the tissues excites sensory neurons, contributing to the tingling, prickling prodrome that warns of an attack and the visceral pain of abdominal episodes."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "Living under threat exacts a mental toll: the unpredictable, potentially fatal laryngeal attacks breed chronic anxiety and depression, and the resulting hypervigilance and impaired quality of life are now recognized as part of the disease burden."
  - target: 02-pathogen/02-bacteria/helicobacter-pylori
    relation: connects-to
    note: "A stomach bug can set off the belly attacks: Helicobacter pylori infection is linked to more frequent abdominal angioedema attacks in hereditary angioedema, and eradicating it can reduce them — a treatable trigger worth seeking."
  - target: 01-human/07-system/cll
    relation: connects-to
    note: "A lymphoma can mimic the hereditary disease: acquired C1-inhibitor deficiency, producing identical bradykinin-driven angioedema, arises in B-cell disorders like CLL, so adult-onset angioedema without family history prompts a search for an underlying lymphoproliferative tumor."
  - target: 01-human/04-cellular/b-cell
    relation: connects-to
    note: "B cells can turn on the body's own brake: in acquired angioedema, B-cell clones make autoantibodies against C1-inhibitor or consume it, depleting the very protein whose hereditary deficiency causes the inherited form."
  - target: 01-human/03-molecular/prostaglandins
    relation: connects-to
    note: "Bradykinin works partly through downstream vasodilators: at the endothelium it triggers release of prostaglandins and nitric oxide that widen vessels and leak fluid, amplifying the swelling that defines an attack."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "Innate inflammation feeds into the kinin system: neutrophil-derived proteases can cleave kininogen and activate the contact pathway, so the inflammation of an intercurrent infection can help tip a patient into an angioedema attack."
  - target: 01-human/07-system/panic-disorder
    relation: connects-to
    note: "Unpredictable suffocation breeds fear: the threat of sudden, potentially fatal laryngeal swelling drives high rates of anxiety and panic in patients, a psychological toll that, like the depression already linked, is part of living with the disease."
  - target: 01-human/05-tissue/intestinal-epithelium
    relation: connects-to
    note: "Attacks swell the gut wall from within: bradykinin-driven edema of the intestinal submucosa beneath the epithelium causes cramping pain, vomiting and even bowel obstruction, abdominal attacks so severe they are often mistaken for a surgical emergency."
  - target: 01-human/03-molecular/ace2
    relation: connects-to
    note: "A second enzyme helps clear the trigger: ACE2 degrades the active bradykinin metabolite des-Arg9-bradykinin, so its activity helps terminate attacks — a counterpart to the ACE inhibition that, by blocking bradykinin breakdown, can precipitate angioedema."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "Living between attacks breeds chronic worry: beyond acute fear, the constant vigilance over triggers, rescue medication and the unpredictability of the next swelling fosters a persistent generalized anxiety that constrains daily life."
  - target: 01-human/07-system/hcc
    relation: connects-to
    note: "Its old prophylactic drug can grow liver tumors: long-term attenuated androgens like danazol, once a mainstay of HAE prevention, cause hepatic adenomas that can transform, a reason these agents are now used cautiously."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "Both the disease's treatments raise clot risk: attenuated androgens used for prophylaxis and C1-inhibitor concentrate given for attacks each carry a recognized thrombotic risk, so venous thromboembolism is a treatment hazard in HAE."
  - target: 01-human/07-system/type-2-diabetes
    relation: connects-to
    note: "Androgen prophylaxis skews metabolism: the weight gain, dyslipidemia and insulin resistance from long-term attenuated androgens like danazol push HAE patients toward type 2 diabetes, part of why safer therapies are preferred."
  - target: 01-human/07-system/atherosclerosis
    relation: connects-to
    note: "Its androgen prophylaxis worsens the arteries: long-term danazol lowers HDL and raises LDL, and this drug-induced dyslipidemia accelerates atherosclerosis, another reason attenuated androgens are now second-line in HAE."
  - target: 01-human/07-system/ptsd
    relation: connects-to
    note: "Near-fatal swelling can traumatize: surviving laryngeal attacks that threaten suffocation, sometimes with emergency airway procedures, can leave HAE patients with post-traumatic stress on top of their anxiety."
  - target: 01-human/07-system/sepsis
    relation: connects-to
    note: "Its attacks invite risky intervention: laryngeal swelling can force emergency intubation or surgical airways, and abdominal attacks mimicking a surgical abdomen can lead to unnecessary operations, each carrying infection and sepsis risk."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "Its hallmark is swelling of the skin: HAE produces recurrent non-itchy subcutaneous angioedema of the face, limbs and genitals, often preceded by the rash-like prodrome of erythema marginatum."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "Hormones both trigger and treat it: oestrogen from the pill or pregnancy worsens HAE attacks, while attenuated androgens like danazol have long been used as prophylaxis, tying the disease to the endocrine system."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "It runs on the bradykinin pathway shared with blood-pressure drugs: HAE swelling is bradykinin-mediated, so ACE inhibitors, which block bradykinin breakdown, are contraindicated and can precipitate severe attacks."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "It can rarely reach the brain: cerebral angioedema is an uncommon but serious HAE attack causing headache, seizures and transient neurological deficits, and bradykinin itself is a potent driver of pain."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "Attacks can swell the urinary tract: bradykinin-mediated angioedema of the bladder and urethra during an HAE attack can cause painful dysuria and acute urinary retention."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "Deep limb attacks disable and deceive: HAE swelling of the hands, feet and limbs can be painful and disabling and is often mistaken for cellulitis, compartment syndrome or arthritis, delaying correct treatment."
  - target: 03-medicine/01-modern/04-cardio/ace-inhibitors
    relation: connects-to
    note: "One drug class is forbidden: ACE inhibitors are contraindicated in HAE because they block the breakdown of bradykinin, the mediator of its swelling, and can precipitate severe attacks."
  - target: 02-pathogen/02-bacteria/helicobacter-pylori
    relation: connects-to
    note: "A stomach bug can stoke its attacks: Helicobacter pylori infection is associated with more frequent HAE attacks, and eradicating it can reduce attack frequency in some patients."
  - target: 01-human/07-system/multiple-myeloma
    relation: connects-to
    note: "Its acquired mimic flags a blood cancer: acquired C1-inhibitor deficiency, which mimics HAE, is associated with B-cell lymphoproliferative disorders and monoclonal gammopathy."
  - target: 03-medicine/01-modern/13-cancer/targeted-therapy
    relation: connects-to
    note: "Modern prophylaxis is a targeted antibody: lanadelumab, a monoclonal antibody against plasma kallikrein, prevents the bradykinin-driven attacks of hereditary angioedema."
  - target: 03-medicine/01-modern/04-cardio/arbs
    relation: connects-to
    note: "A cautious alternative to ACE inhibitors: angiotensin-receptor blockers are preferred over ACE inhibitors in hereditary angioedema, as ACE inhibition raises bradykinin and can precipitate severe attacks."
  - target: 03-medicine/01-modern/02-respiratory/corticosteroids
    relation: connects-to
    note: "Allergy drugs do not work here: unlike histamine-mediated angioedema, the bradykinin-driven swelling of hereditary angioedema does not respond to corticosteroids, antihistamines or adrenaline — a crucial distinction."
  - target: 01-human/07-system/covid-19-disease
    relation: connects-to
    note: "A shared bradykinin axis: HAE is driven by unchecked bradykinin, and the same kinin pathway — amplified when SARS-CoV-2 disrupts ACE2 — was proposed to drive the vascular leak of severe COVID-19, prompting trials of HAE drugs like icatibant."
  - target: 03-medicine/01-modern/13-cancer/cancer-chemotherapy
    relation: connects-to
    note: "Treating the cause of acquired angioedema: an acquired C1-inhibitor deficiency mimicking HAE arises in CLL, myeloma and lymphoma, where chemotherapy or rituximab against the underlying clone can resolve the angioedema."
  - target: 03-medicine/01-modern/04-cardio/aspirin
    relation: connects-to
    note: "Bradykinin, not prostaglandin, drives it: unlike ACE inhibitors, which raise bradykinin and are contraindicated, aspirin and NSAIDs do not trigger hereditary angioedema and are generally tolerated — a useful point in analgesic choice."
  - target: 01-human/07-system/hereditary-pancreatitis
    relation: connects-to
    note: "Diseases of an unchecked protease cascade: hereditary angioedema unleashes the kallikrein-bradykinin cascade when C1-inhibitor fails, much as hereditary pancreatitis unleashes trypsin when its SPINK1 inhibitor fails—each a missing brake on a destructive enzyme."
  - target: 01-human/07-system/dlbcl
    relation: connects-to
    note: "Acquired angioedema points to lymphoma: acquired C1-inhibitor deficiency arises with B-cell lymphoproliferative disorders such as diffuse large B-cell lymphoma and autoantibodies, causing bradykinin angioedema in older adults without a family history."
  - target: 01-human/05-tissue/arterial-wall
    relation: connects-to
    note: "Bradykinin makes the vessels leak: in hereditary angioedema, unopposed bradykinin acts on B2 receptors of the vascular endothelium to increase permeability, so plasma escapes the vessel wall into tissue as the non-itchy, non-pitting swelling."
  - target: 01-human/05-tissue/hepatic-lobule
    relation: connects-to
    note: "Where the missing protein is made: C1-inhibitor is synthesised by hepatocytes in the liver lobule, which is why attenuated androgens that boost hepatic synthesis—and emerging liver-targeted RNA and gene therapies—act here."
  - target: 01-human/07-system/waldenstrom-macroglobulinemia
    relation: connects-to
    note: "Acquired angioedema's clue: new-onset angioedema in an older adult without family history suggests acquired C1-inhibitor deficiency, classically from a lymphoproliferative clone such as Waldenström macroglobulinaemia or an MGUS."
  - target: 01-human/05-tissue/germinal-center
    relation: connects-to
    note: "Autoantibodies behind acquired disease: acquired angioedema can arise from anti-C1-inhibitor autoantibodies produced by germinal-centre-derived B-cell clones, distinguishing it from the purely genetic hereditary form."
  - target: 01-human/07-system/follicular-lymphoma
    relation: connects-to
    note: "An indolent lymphoma trigger: follicular lymphoma is among the low-grade B-cell neoplasms that consume C1-inhibitor and cause acquired angioedema, which can improve when the lymphoma is treated."
  - target: 01-human/07-system/mantle-cell-lymphoma
    relation: connects-to
    note: "Another lymphoproliferative cause: mantle-cell lymphoma joins the B-cell malignancies that can produce acquired C1-inhibitor deficiency, so new late-onset angioedema warrants a search for occult lymphoma."
  - target: 01-human/06-organ/spleen
    relation: connects-to
    note: "A splenic source: splenic marginal-zone lymphoma is a classic cause of acquired angioedema, the clone consuming C1-inhibitor, and treating the lymphoma or removing the spleen can resolve the attacks."
  - target: 01-human/03-molecular/angiopoietin
    relation: connects-to
    note: "Endothelial barrier control: the angiopoietin-Tie2 axis governs endothelial junction stability, and its dysregulation contributes to the vascular leak that produces angioedema swelling."
  - target: 01-human/03-molecular/fibrinogen
    relation: connects-to
    note: "Contact-system crosstalk: activated factor XII in hereditary angioedema triggers both bradykinin generation and the coagulation cascade, so fibrinogen turnover and D-dimer rise during attacks."
  - target: 01-human/03-molecular/von-willebrand-factor
    relation: connects-to
    note: "Endothelial activation marker: angioedema attacks activate the endothelium to release von Willebrand factor from Weibel-Palade bodies, reflecting the vascular disturbance driving the swelling."
  - target: 01-human/04-cellular/platelet
    relation: connects-to
    note: "Contact-system amplifier: activated platelets release inorganic polyphosphate that triggers factor XII autoactivation, feeding the kallikrein-kinin cascade that generates the bradykinin driving HAE swelling."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Distinguishing mechanism: HAE is bradykinin-mediated, not IgE/mast-cell-mediated like allergic angioedema, which is why antihistamines, epinephrine and steroids fail and B2R/kallikrein-targeted drugs are needed."
  - target: 01-human/03-molecular/glucocorticoid-receptor
    relation: connects-to
    note: "Why steroids fail: corticosteroids acting through the glucocorticoid receptor relieve histaminergic angioedema but not bradykinin-mediated HAE attacks, a key clinical contrast underscoring the disease's distinct pathophysiology."
  - target: 01-human/03-molecular/antithrombin
    relation: connects-to
    note: "Serpin co-regulation: antithrombin and C1-esterase-inhibitor are both serpins that restrain the contact-pathway proteases (factor XIIa, factor XIa); the loss of the C1-INH arm in HAE leaves the kallikrein-kinin cascade unchecked."
  - target: 01-human/03-molecular/adrenomedullin
    relation: connects-to
    note: "Barrier counter-regulation: adrenomedullin tightens endothelial cell junctions to stabilise the vascular barrier, the opposite of the bradykinin-driven junctional opening that produces the deep tissue swelling of HAE."
  - target: 01-human/03-molecular/renin
    relation: connects-to
    note: "RAAS crosstalk: the kallikrein-kinin and renin-angiotensin systems converge on ACE, which both degrades bradykinin and generates angiotensin II — the reason ACE inhibitors precipitate dangerous attacks and are contraindicated in HAE."
  - target: 01-human/03-molecular/fcrn
    relation: connects-to
    note: "Long-acting prophylaxis: the IgG anti-plasma-kallikrein antibody lanadelumab relies on FcRn recycling for its weeks-long half-life, enabling subcutaneous prophylaxis that suppresses kallikrein and prevents the bradykinin generation driving HAE attacks."
  - target: 01-human/03-molecular/c5ar1
    relation: connects-to
    note: "Complement dysregulation: C1-inhibitor is the main brake on the classical-complement C1 complex as well as the contact system, so its deficiency causes the chronic complement consumption and low C4 that are diagnostic, even though the swelling itself is bradykinin-mediated."
  - target: 01-human/03-molecular/endothelin-1
    relation: connects-to
    note: "Endothelial effector: the angioedema of HAE is produced at the vascular endothelium, where bradykinin opens inter-endothelial junctions to let plasma leak — the same endothelial barrier whose baseline tone and integrity endothelin-1 helps regulate."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "Endothelial activation: bradykinin signalling through the B2 receptor activates endothelial NF-κB, amplifying the vascular inflammation and permeability that drive the swelling of a hereditary-angioedema attack."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "Attack acute-phase: HAE attacks are accompanied by a systemic acute-phase response with rising IL-6, reflecting the contact-system activation and endothelial inflammation that accompany the bradykinin-driven swelling."
  - target: 01-human/03-molecular/tnf-alpha
    relation: connects-to
    note: "Permeability cytokine: TNF-α released during the endothelial activation of HAE attacks further loosens inter-endothelial junctions, compounding the bradykinin-driven vascular leak that produces the angioedema."
  - target: 01-human/03-molecular/substance-p
    relation: connects-to
    note: "Shared permeability peptide: like bradykinin (mapped), substance P is a vascular-permeability neuropeptide degraded by ACE, and the overlap explains why ACE inhibitors precipitate bradykinin-mediated angioedema."
  - target: 01-human/03-molecular/cgrp
    relation: connects-to
    note: "Vasodilatory peptide: CGRP is a potent vasodilator and permeability mediator that contributes to the tissue swelling of an angioedema attack alongside bradykinin."
  - target: 01-human/03-molecular/protein-c
    relation: connects-to
    note: "Contact-coagulation crosstalk: C1-esterase inhibitor (mapped) also restrains the intrinsic coagulation cascade (FXIIa, FXIa), so its deficiency in HAE perturbs the coagulation balance that the protein-C anticoagulant system normally maintains."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "Bradykinin acting on the B2 receptor activates PI3K-AKT-eNOS signalling (nitric oxide mapped) that increases the endothelial permeability driving HAE swelling attacks."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "Bradykinin B2-receptor signalling engages ERK-MAPK in endothelial cells, contributing to the vascular-permeability response of hereditary angioedema attacks."
  - target: 01-human/03-molecular/nlrp3-inflammasome
    relation: connects-to
    note: "Contact-system and bradykinin activation can engage the NLRP3 inflammasome, an inflammatory amplifier increasingly implicated in the pathophysiology of angioedema attacks."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "PI3K signalling downstream of the bradykinin B2 receptor on endothelial cells contributes to the eNOS activation and vascular permeability of the angioedema attacks in hereditary angioedema."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Galectin-3 modulates endothelial activation and vascular inflammation relevant to the localised permeability that produces the swelling of hereditary angioedema."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "IL-6-STAT3 signalling transduces the acute-phase inflammatory response that accompanies the attacks of hereditary angioedema."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "JAK1/2-STAT cytokine signaling (IL-6 already mapped) modulates the endothelial inflammatory tone that influences attack susceptibility in hereditary angioedema."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "HIF-1α-VEGF signaling (VEGF already mapped) heightens the vascular permeability that underlies the bradykinin-driven swelling of hereditary angioedema."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "FOXO downstream of bradykinin-PI3K-AKT signaling (AKT and PIK3CA already mapped) regulates the endothelial oxidative-stress and barrier responses in hereditary angioedema."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "GSK-3β modulates the endothelial and inflammatory signaling relevant to the vascular permeability of hereditary angioedema attacks."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "S100A8/A9 alarmins reflect the inflammatory activation accompanying hereditary angioedema attacks."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "mTOR signaling downstream of PI3K-AKT (AKT already mapped) participates in the endothelial-barrier regulation relevant to the swelling of hereditary angioedema."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC-family kinase signaling downstream of the bradykinin B2 receptor participates in the VE-cadherin disruption and endothelial-barrier breakdown of hereditary angioedema."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "IFN-STAT1 signaling participates in the endothelial and immune context modulating the attacks of hereditary angioedema."
  - target: 01-human/03-molecular/nfe2l2
    relation: connects-to
    note: "NRF2 (NFE2L2)-mediated oxidative-stress defense modulates the endothelial responses relevant to hereditary angioedema."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK-linked metabolic and eNOS-coupled signaling participates in the endothelial homeostasis relevant to the vascular permeability of hereditary angioedema."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Autophagy modulates the endothelial-cell homeostasis and stress responses relevant to hereditary angioedema."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "DNMT3A-mediated DNA methylation participates in the epigenetic modulation of the contact-system and endothelial gene expression relevant to hereditary angioedema."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "CXCL12-CXCR4 signaling participates in the endothelial and vascular responses relevant to hereditary angioedema."
  - target: 01-human/03-molecular/adenosine
    relation: connects-to
    note: "Adenosine signaling participates in the vascular-tone and permeability modulation relevant to hereditary angioedema."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "IL-1β-driven inflammation participates in the inflammatory amplification of the angioedema attacks of hereditary angioedema."
  - target: 01-human/03-molecular/progesterone
    relation: connects-to
    note: "Hormonal modulation: estrogen worsens hereditary angioedema (already mapped) while progestins and attenuated androgens (testosterone already mapped) reduce attacks, so progesterone-based contraception is a preferred option in the estrogen-sensitive and type III forms."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "Endothelial alarmin: IL-33 released from activated or injured endothelium increases vascular permeability, a mechanism that can amplify the bradykinin-driven endothelial leak underlying the swelling of an angioedema attack."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "Inflammatory amplification: IL-17A-driven inflammation participates in the endothelial activation and inflammatory milieu that can aggravate the severity of hereditary angioedema attacks beyond the core bradykinin pathway."
  - target: 01-human/03-molecular/immunoglobulin-g
    relation: connects-to
    note: "Acquired C1-INH deficiency: an acquired angioedema mimicking the hereditary disease arises from IgG autoantibodies against C1-inhibitor (already mapped), usually with an underlying B-cell lymphoproliferative disorder, a key differential of bradykinin-mediated swelling."
  - target: 01-human/03-molecular/mhc-class-ii
    relation: connects-to
    note: "Autoantibody presentation: in acquired C1-inhibitor deficiency, MHC class II-restricted T-cell help underlies the anti-C1-INH autoantibody response, distinguishing this immune-mediated form from the genetic deficiency of hereditary angioedema."
  - target: 01-human/03-molecular/il-2
    relation: connects-to
    note: "Lymphoproliferative association: IL-2-driven lymphocyte proliferation underlies the B-cell disorders linked to acquired C1-inhibitor deficiency, the clonal expansions that consume C1-inhibitor or generate the autoantibodies causing acquired angioedema."
  - target: 01-human/03-molecular/aldosterone
    relation: connects-to
    note: "Kinin-RAAS crosstalk: angiotensin-converting enzyme both generates angiotensin II (already mapped) toward aldosterone and degrades bradykinin (already mapped), so ACE inhibitors raise bradykinin and can precipitate angioedema attacks, contraindicated in hereditary angioedema."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "Immune regulation in acquired disease: IL-10 and immunoregulatory signals shape the autoreactive response of acquired C1-inhibitor deficiency (IL-6 already mapped), the immune-mediated form distinct from the genetic deficiency of hereditary angioedema."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "Autoantibody help: CD4 T-cell help (MHC class II and IL-2 already mapped) supports the B cells producing the anti-C1-inhibitor autoantibodies of acquired angioedema, distinguishing it from the inherited C1-inhibitor deficiency."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "Contact-system activation: zinc is required for the assembly of factor XII and high-molecular-weight kininogen on surfaces that triggers the kallikrein-kinin cascade generating the bradykinin (already mapped) of hereditary angioedema."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "Histaminergic differential: IL-4 drives the mast-cell (already mapped) type-2 response of the far commoner histamine-mediated (already mapped) allergic angioedema, the differential that must be excluded before treating the bradykinin-mediated hereditary form."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "Type-2 differential: IL-13, with IL-4 (already mapped), supports the type-2 mast-cell (already mapped) response of the allergic angioedema differential, which unlike hereditary angioedema responds to antihistamines and steroids."
  - target: 01-human/03-molecular/baff
    relation: connects-to
    note: "Acquired C1-INH deficiency: BAFF supports the B cells of the lymphoproliferative disorders (CLL and lymphomas already mapped) that cause acquired C1-inhibitor deficiency, the key acquired-angioedema differential of the hereditary form."
  - target: 01-human/03-molecular/cd20
    relation: connects-to
    note: "Rituximab in acquired AAE: the CD20 B cells of the underlying lymphoproliferative disorder are targeted by rituximab to treat the acquired C1-inhibitor deficiency, distinguishing its therapy from that of hereditary angioedema."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Autoimmune-associated angioedema: the type-I interferon of the autoimmune diseases (systemic lupus already mapped) associated with acquired C1-inhibitor deficiency reflects the immune dysregulation and complement (C3 already mapped) consumption of that differential."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Metabolic-hormonal adipokine: leptin is the adipokine of the metabolic-inflammatory milieu; the oestrogen (already mapped) and metabolic modulation of the attack frequency of hereditary angioedema."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Metabolic adipokine: adiponectin, with leptin (already mapped), is part of the adipokine dimension of the metabolic milieu of hereditary angioedema."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), is the adipose-inflammatory adipokine of the metabolic-inflammatory milieu of hereditary angioedema."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "Innate immune modulation: the NK cells (perforin already mapped) are part of the broader innate immune context of hereditary angioedema, distinct from the complement (C3 already mapped) and bradykinin (already mapped) core mechanism."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Th1 arm: the IFN-γ of the T cells is the type-II interferon arm (with the type-I interferon already mapped) of the subtle immune-inflammatory dimension of hereditary angioedema."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the immune-inflammatory dimension accompanying hereditary angioedema."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune milieu, distinguishing the bradykinin-mediated (already mapped) angioedema from the type-2/mast-cell (histamine already mapped) angioedema."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the subtle immune-inflammatory dimension accompanying hereditary angioedema."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "Antigen presentation: the dendritic cells present antigen (MHC already mapped) within the immune microenvironment accompanying hereditary angioedema."
  - target: 01-human/03-molecular/factor-h
    relation: connects-to
    note: "Complement regulation: factor H regulates the alternative complement pathway, complementing the C1-esterase-inhibitor (already mapped) control of the classical/lectin pathways and the contact (bradykinin already mapped) system dysregulated in hereditary angioedema."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Innate modulation: the macrophages, whose function the broadly anti-inflammatory C1-esterase inhibitor (already mapped) also modulates, are part of the innate-immune context of hereditary angioedema."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Adaptive context: the cytotoxic T cells (perforin pathway) are part of the subtle adaptive-immune dimension accompanying the complement/contact-system disorder of hereditary angioedema."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: connects-to
    note: "Immune tolerance: the regulatory T cells are part of the adaptive-immune context that the broadly anti-inflammatory C1-esterase inhibitor (already mapped) helps shape, relevant to the acquired autoimmune forms of angioedema."
  - target: 01-human/03-molecular/osteopontin
    relation: connects-to
    note: "Vascular matricellular: osteopontin, a matricellular cytokine of the vascular wall, is part of the endothelial (already mapped) and vascular-inflammation context of the bradykinin-mediated permeability of hereditary angioedema."
  - target: 01-human/03-molecular/transferrin
    relation: connects-to
    note: "Acute-phase iron: transferrin, the iron carrier, is part of the acute-phase and vascular-permeability context accompanying the recurrent attacks of hereditary angioedema."
  - target: 01-human/03-molecular/tslp
    relation: connects-to
    note: "Mast-cell independent alarmin: TSLP, released by epithelial cells during the oedematous attacks, amplifies the type-2 polarisation of the dendritic cells (already mapped) independently of histamine (already mapped) in the immune landscape of hereditary angioedema."
  - target: 01-human/03-molecular/erythropoietin
    relation: connects-to
    note: "Androgen-EPO axis: erythropoietin synthesis in the liver (already mapped) is enhanced by the androgen therapies (testosterone and danazol) used as prophylaxis in hereditary angioedema, linking the hormonal prevention strategy to the hepatic EPO production of the disease."
  - target: 01-human/03-molecular/periostin
    relation: connects-to
    note: "Submucosal remodelling: periostin, induced by the IL-4 and IL-13 (already mapped) released during oedematous attacks in the submucosal connective tissue, promotes the matricellular remodelling of the swollen tissues in hereditary angioedema."
---

# Hereditary Angioedema

## Overview

**Hereditary angioedema (HAE)** is an **autosomal dominant** disease of recurrent, self-limited, potentially life-threatening swelling caused by **bradykinin excess** secondary to **C1-esterase inhibitor (C1-INH) deficiency or dysfunction** [^cicardi-2010-icatibant-nejm]. Unlike allergic angioedema (which is IgE-mediated/histamine-driven and responds to antihistamines and epinephrine), HAE is **bradykinin-mediated** — antihistamines, corticosteroids, and epinephrine are largely ineffective. HAE affects approximately 1 in 50,000 people worldwide, without racial predilection, and typically presents in the first or second decade of life.

**The defining clinical triad of HAE:**
1. **Recurrent episodes** of non-pitting, non-urticarial subcutaneous or submucosal swelling
2. **Self-limited** attacks lasting 2-5 days without treatment (72-96 hours typical)
3. **Bradykinin-mediated** mechanism: no urticaria, no response to antihistamines/steroids
4. **Family history** in ~75% (25% are de novo SERPING1 mutations)

**Mortality:** Untreated laryngeal HAE has a historical mortality of ~30-40% — asphyxiation from upper airway swelling is the leading cause of HAE death. With modern therapy (icatibant, C1-INH concentrate) and patient education, laryngeal attacks can be managed safely if treated early.

**HAE classification:**

| Type | Mechanism | C1-INH antigen | C1-INH activity | C4 | C1q |
|:-----|:----------|:--------------|:----------------|:---|:----|
| **Type I** (~80%) | SERPING1 loss-of-function → insufficient C1-INH production | Low (<30%) | Low (<50%) | Low | Normal |
| **Type II** (~15%) | SERPING1 missense → dysfunctional protein | Normal or high | Low (<50%) | Low | Normal |
| **Type III** (<5%) | FXII gain-of-function (F12 p.Thr309Lys/Arg) → excess kallikrein activity | Normal | Normal | Normal | Normal |
| **Acquired angioedema** | Anti-C1q antibodies (lymphoma, autoimmune) | Low | Low | Low | **Low** |

## Structure

### Pathophysiological framework

**The bradykinin cascade in HAE:**

```
Contact activation trigger
        ↓
   FXII activation → FXIIa
        ↓ ← [C1-INH blocks here]
Prekallikrein → Plasma kallikrein ← [berotralstat, lanadelumab, ecallantide block here]
        ↓
High-molecular-weight kininogen (HMWK) → Bradykinin (9 aa) + Kinin-free HMWK
        ↓ ← [icatibant blocks here (B2R antagonist)]
Bradykinin B2 receptor (endothelium)
        ↓
Gαq → IP₃ → Ca²⁺ → eNOS → NO + PGI₂
        ↓
↑Vascular permeability (postcapillary venules)
        ↓
Fluid extravasation → ANGIOEDEMA
```

**Common attack triggers:**
- **Trauma/surgery** (most common; 25-50% of attacks): dental procedures, endoscopy, surgical intubation — jaw/throat/oral edema are especially dangerous
- **Psychological stress** (emotionally stressful events → catecholamines → FXII activation)
- **Infections** (upper respiratory infections, GI infections)
- **Estrogen exposure** (oral contraceptives, hormone replacement, pregnancy): estrogen upregulates prekallikrein and HMWK → increased bradykinin generation; type III HAE is predominantly a disease of women taking OCP or pregnant
- **ACE inhibitors**: ACE (kininase II) degrades bradykinin; ACE inhibitors → bradykinin accumulation → can both unmask latent HAE and cause angioedema de novo (ACE inhibitor–induced angioedema is also bradykinin-mediated)
- **Idiopathic** (30-40% of attacks): no identifiable trigger

### Distribution of swelling (attack phenotype)

| Location | Frequency | Clinical features |
|:---------|:----------|:------------------|
| **Subcutaneous** (extremities, trunk, face) | ~50% | Tense, non-pitting swelling; no urticaria; may be disfiguring; self-resolves |
| **Abdominal (intestinal wall)** | ~25-30% | Severe colicky abdominal pain, nausea, vomiting, diarrhea; can mimic acute abdomen; ascites on imaging; may lead to unnecessary laparotomy |
| **Laryngeal/oropharyngeal** | ~10-15% | Throat tightness, voice changes, stridor → life-threatening asphyxiation; rapidly progressing attacks require emergent treatment |
| **Genital/urinary** | ~5% | Self-limited; painful |
| **CNS** (rare) | <1% | Headache; cerebral edema rare |

## Function

### Diagnosis

**Diagnostic workup:**

1. **Clinical suspicion:** Recurrent non-urticarial angioedema + family history ± abdominal attacks ± failure of antihistamines; often misdiagnosed as allergic angioedema or recurrent abdominal pain for years

2. **Laboratory confirmation:**
   - **C4 level:** Consistently low (<30% of normal) even between attacks — the single best screening test; reflects chronic low-level C1 activation
   - **C1-INH antigen:** Low in type I (normal/elevated in type II)
   - **C1-INH functional activity:** Low in both type I and II (<50% of normal; typically <30%); the definitive test
   - **C1q:** Normal in HAE types I, II, III (differentiates from acquired angioedema where anti-C1q antibodies consume C1q)

3. **Confirm with genetic testing:** *SERPING1* sequencing confirms type I/II; *F12* mutations confirm type III

4. **FXII gene testing:** If HAE suspected but C4/C1-INH normal, especially in women with estrogen-related attacks

**Differential diagnosis of angioedema:**

| Feature | HAE | ACE inhibitor angioedema | Allergic angioedema | Acquired angioedema |
|:--------|:----|:------------------------|:--------------------|:--------------------|
| Urticaria | No | No | Usually yes | No |
| C4 | Low | Normal | Normal | Low |
| C1-INH activity | Low | Normal | Normal | Low |
| C1q | Normal | Normal | Normal | **Low** |
| Onset | Childhood/teen | Any age (months after ACEi) | Minutes after trigger | Adult onset |
| Family history | Yes | No | Variable | No |
| Response to antihistamine/steroid | No | No | Yes | No |

## Pathology

### Acute treatment [^cicardi-2010-icatibant-nejm]

**Principle: treat every laryngeal attack, all abdominal attacks, and facial attacks as emergencies. Goal: abort attack as fast as possible.**

**First-line options (self-administration available):**
- **Icatibant (Firazyr):** Bradykinin B2R competitive antagonist; SC injection 30 mg; approved EU 2008, FDA 2011; FAST-3 trial: time to significant symptom relief 2.0 h vs 19.8 h with placebo; can self-administer; repeat dose q6h if needed (max 3 doses/24h); works even with normal C1-INH (also first-line for ACE inhibitor–induced angioedema)
- **Plasma-derived C1-INH (Berinert) IV:** 20 IU/kg IV; rapid IV infusion; fast onset (1-2h); first-line in many centers; most proven safety profile; also used in obstetric emergencies (pregnancy-associated HAE)
- **Recombinant C1-INH (Ruconest):** 50 IU/kg IV (max 4200 IU); faster production than plasma-derived; effective; bovine allergenicity risk (cattle-allergic patients)
- **Ecallantide (Kalbitor):** SC kallikrein inhibitor; 30 mg SC (3 × 10 mg injections); US only; healthcare provider must administer (anaphylaxis risk ~4%)

**If above unavailable (fresh frozen plasma):**
- FFP: 2-4 units IV; contains C1-INH, C4, C2; used as rescue therapy when specific agents unavailable; paradoxically may transiently worsen attack (HMWK and kallikrein in FFP) before helping — rarely used now

**Laryngeal HAE: immediate treatment + prepare for intubation/tracheotomy:**
- Secure airway assessment; ENT/anesthesia on standby
- Administer icatibant + C1-INH concentrate IMMEDIATELY (both if available)
- Endotracheal intubation may be required if symptoms progress despite treatment

### Long-term prophylaxis

**Indications:** >1 attack/month, severe/poorly controlled attacks, occupational/social impairment, high-risk procedures planned, prior laryngeal attacks.

**Options:**
- **Lanadelumab (Takhzyro; SC q2-4 weeks):** Humanized anti-kallikrein IgG4 mAb; 300 mg SC q4 weeks (or q2 weeks for more severe disease); HELP OLE trial: 87% reduction in HAE attacks (from mean 3.0/month to 0.4/month) [^maurer-2018-lanadelumab-help]; FDA approved Aug 2018; most effective prophylaxis available
- **Berotralstat (Orladeyo; 110 mg/day oral):** Oral plasma kallikrein inhibitor; APeX-2: 44% reduction in monthly HAE attacks vs placebo [^zuraw-2020-berotralstat-apex2]; FDA approved Dec 2020; first oral once-daily prophylaxis; also available 150 mg/day
- **SC C1-INH (Haegarda):** 60 IU/kg SC twice weekly; self-administered; effective; useful in patients who prefer replacement therapy
- **Danazol (attenuated androgen):** Stimulates C1-INH synthesis (SERPING1 upregulation via androgen receptor); now rarely used — virilization, hepatotoxicity, contraindicated in children and pregnancy; replaced by targeted therapies
- **Tranexamic acid:** Antifibrinolytic (inhibits plasmin); modest efficacy; mechanism unclear (reduced FXII activation?); alternative when other therapies unavailable

**Short-term prophylaxis (for planned procedures):**
- High-risk (dental work, surgery, intubation): 1-2 units C1-INH concentrate 30-60 min before procedure; OR icatibant held on standby

**Special populations:**
- **Children:** C1-INH concentrate (no dose restrictions); berotralstat FDA-approved ≥12 years; lanadelumab FDA-approved ≥12 years; danazol contraindicated
- **Pregnancy:** C1-INH concentrate is preferred (safe in pregnancy); icatibant (FDA category C — limited data but widely used); avoid danazol (virilization of female fetus), tranexamic acid (VTE risk)
- **HAE type III (FXII mutation):** Avoid estrogen-containing OCP; progestogen-only contraception + tranexamic acid for milder cases; C1-INH and icatibant for acute attacks; lanadelumab for prophylaxis

## Connections

- `connects-to` → **[C1-Esterase Inhibitor](../../03-molecular/c1-esterase-inhibitor/README.md)** — C1-INH deficiency (type I: low antigen + activity; type II: low activity, normal antigen) → uncontrolled FXII/kallikrein → bradykinin excess → B2R-mediated vascular permeability → HAE attacks; icatibant, C1-INH concentrate, berotralstat, and lanadelumab are therapeutic targets.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — C1-INH deficiency → chronic low-level C1 complex activation → C4/C2 cleavage → C4 consumed even between attacks; low C4 + low C1-INH functional activity = diagnostic criteria for HAE type I/II; C3 is usually normal (C3 convertase limited); C1q is normal (distinguishes from acquired angioedema).
- `connects-to` → **[Bradykinin](../../03-molecular/bradykinin/README.md)** — HAE is the paradigmatic bradykinin-excess disease: C1-INH deficiency → uncontrolled FXII/kallikrein → bradykinin generation from HMWK; bradykinin binds B2R on postcapillary venules → Gαq/Ca²⁺ → eNOS/NO → vascular permeability; icatibant (B2R antagonist) aborts HAE attacks.
- `connects-to` → **[Angiotensin II](../../03-molecular/angiotensin-ii/README.md)** — ACE (kininase II) degrades bradykinin; ACEi block catabolism → bradykinin accumulation → angioedema (~0.1-0.7% of users); ACEi contraindicated in HAE; Ang-II and bradykinin are both ACE substrates → RAAS and kinin-kallikrein systems are mechanistically linked.
- `connects-to` → **[Thrombin](../../03-molecular/thrombin/README.md)** — Trauma/surgery → thrombin generation → FXII activation → contact cascade → kallikrein → bradykinin → HAE attack; surgical trauma triggers ~25-50% of HAE attacks; short-term C1-INH concentrate or icatibant before high-risk procedures prevents peri-operative attacks.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — Every HAE attack ends at the endothelial cell: bradykinin binds its B2 receptor on postcapillary venule endothelium → Gαq/Ca²⁺ → eNOS-derived NO loosens inter-endothelial junctions → plasma leaks into tissue as non-urticarial swelling; icatibant blocks B2R to abort this.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — HAE swelling is subcutaneous or submucosal and looks unlike allergic hives: ~50% of attacks are tense, non-pitting, non-urticarial skin swelling that lasts 2-5 days and does not itch or respond to antihistamines — reflecting its bradykinin (not histamine) mechanism.
- `connects-to` → **[Estrogen](../../03-molecular/estrogen/README.md)** — Estrogen worsens HAE by upregulating prekallikrein, boosting bradykinin generation; estrogen-containing contraceptives and pregnancy trigger attacks, and FXII (type III) HAE is largely a disease of women on the pill — so progestin-only contraception is advised.
- `connects-to` → **[Immune System](../immune-system/README.md)** — HAE is a disorder of complement regulation: C1-inhibitor normally restrains the classical complement pathway and the contact (kinin) system, so its deficiency consumes C4 (a diagnostic clue) and unleashes bradykinin; it sits between complement and innate immune control.
- `connects-to` → **[Mast Cell](../../04-cellular/mast-cell/README.md)** — HAE is the key bradykinin-mediated mimic of mast-cell angioedema: unlike histaminergic allergic angioedema (urticaria, itch, antihistamine response), HAE swelling is non-itchy, urticaria-free and unresponsive to antihistamines or epinephrine—telling them apart is life-saving.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — The liver synthesizes C1-inhibitor and most complement and contact-system proteins, so it underlies HAE: types I/II HAE reflect deficient or dysfunctional hepatic C1-INH, and siRNA therapy (donidalorsen targeting prekallikrein) acts on hepatic production to prevent attacks.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — Abdominal attacks are a major, often misdiagnosed feature of hereditary angioedema: bradykinin-driven edema of the bowel wall causes severe colicky pain, vomiting, and ascites that mimic a surgical abdomen, so recurrent crises with C1-inhibitor deficiency point to HAE.
- `connects-to` → **[Respiratory system](../respiratory-system/README.md)** — Laryngeal edema is the lethal manifestation of hereditary angioedema: bradykinin-mediated upper-airway swelling can cause asphyxiation, so patients carry on-demand C1-inhibitor or icatibant—and unlike histaminergic angioedema, it ignores epinephrine and antihistamines.
- `connects-to` → **[Hypertension](../hypertension/README.md)** — ACE inhibitors can trigger bradykinin-mediated angioedema like HAE: ACE normally degrades bradykinin, so blocking it raises bradykinin and causes angioedema (especially in HAE patients), which is why ACE inhibitors are contraindicated in hereditary angioedema.
- `connects-to` → **[Complement C5](../../03-molecular/complement-c5/README.md)** — Hereditary angioedema reflects loss of C1-inhibitor's brake on the contact and complement systems: without it, kallikrein generates bradykinin while the classical complement pathway runs unchecked, consuming C4—so low C4 is the screening clue to HAE.
- `connects-to` → **[Asthma](../asthma/README.md)** — Hereditary angioedema and asthma both cause acute airway emergencies: HAE's bradykinin-driven laryngeal edema obstructs the upper airway and ignores bronchodilators and steroids, unlike asthma's smooth-muscle bronchospasm—so the distinction is life-saving.
- `connects-to` → **[Atopic Dermatitis](../atopic-dermatitis/README.md)** — Hereditary angioedema is the bradykinin-mediated counterpart to histamine-driven (allergic) angioedema seen with atopic dermatitis and urticaria: HAE lacks hives and ignores antihistamines, steroids and epinephrine—needing C1-INH or bradykinin-pathway drugs instead.
- `connects-to` → **[Small Intestine](../../06-organ/small-intestine/README.md)** — Hereditary angioedema attacks the gut wall: bradykinin-driven edema of the small intestine causes severe colicky pain, vomiting and even obstruction, so HAE can mimic a surgical abdomen—and unexplained recurrent abdominal attacks should prompt C1-inhibitor testing.
- `connects-to` → **[Nitric Oxide](../../03-molecular/nitric-oxide/README.md)** — Bradykinin drives HAE swelling through nitric oxide and vascular leak: it binds endothelial B2 receptors to release NO and open intercellular junctions, flooding tissue with fluid—the same vasodilator pathway behind blood-pressure control produces the edema.
- `connects-to` → **[Systemic Lupus Erythematosus](../systemic-lupus-erythematosus/README.md)** — Acquired C1-inhibitor deficiency mimics hereditary angioedema in autoimmune or lymphoproliferative disease: SLE and lymphomas can consume or block C1-INH, causing bradykinin angioedema later in life—so adult-onset angioedema without family history needs a workup.
- `connects-to` → **[Histamine](../../03-molecular/histamine/README.md)** — Hereditary angioedema is bradykinin-, not histamine-driven—and that distinction is everything: unlike allergic angioedema and hives, HAE swelling does not respond to antihistamines, steroids, or epinephrine, so recognizing the non-histaminergic mechanism saves airways.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — Hereditary angioedema is shaped by the reproductive system: estrogen worsens attacks, so puberty, pregnancy, and the contraceptive Pill can trigger flares—and an estrogen-dependent FXII-linked form affects mainly women, making hormone choices central to care.
- `connects-to` → **[Smooth Muscle Cell](../../04-cellular/smooth-muscle-cell/README.md)** — HAE attacks hinge on smooth muscle: bradykinin relaxes vascular smooth muscle and opens endothelial junctions, flooding tissue with fluid—and in the gut, submucosal edema with smooth-muscle spasm causes severe abdominal pain that mimics a surgical abdomen.
- `connects-to` → **[Testosterone](../../03-molecular/testosterone/README.md)** — Androgens are a classic hereditary angioedema prophylaxis: attenuated androgens like danazol raise C1-inhibitor levels to prevent attacks—a striking contrast with estrogen, which worsens HAE—so sex hormones swing the disease in opposite directions.
- `connects-to` → **[Plasma Cell](../../04-cellular/plasma-cell/README.md)** — Acquired angioedema mimics HAE but comes from plasma cells: monoclonal gammopathy and lymphoproliferative disorders consume or autoantibody-target C1-inhibitor, so late-onset angioedema without family history prompts a search for a plasma-cell clone.
- `connects-to` → **[Lymphatic System](../lymphatic-system/README.md)** — Angioedema overwhelms lymphatic fluid clearance: bradykinin makes deep dermal and submucosal vessels leak faster than the lymphatic system can drain, producing the firm, non-pitting swelling of HAE—unlike the histamine-driven hives of allergy.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — Hereditary angioedema's swelling is a permeability problem like VEGF's: bradykinin (and VEGF) pry apart endothelial junctions to let plasma flood into tissue, so the attacks are leaky-vessel edema, not the mast-cell hives of allergy.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Hereditary angioedema runs through the calcium-dependent contact system: factor XII and kallikrein activation that generates bradykinin needs calcium, the same cofactor of the clotting cascade—linking the kinin and coagulation pathways.
- `connects-to` → **[Cortisol](../../03-molecular/cortisol/README.md)** — Hereditary angioedema ignores cortisol—unlike allergic swelling: because the attacks are bradykinin-driven, not histamine-driven, steroids and antihistamines don't work, so the key is recognizing it and using C1-inhibitor or bradykinin blockers instead.
- `connects-to` → **[Oxygen](../../02-atomic/oxygen/README.md)** — A laryngeal hereditary angioedema attack can choke off oxygen: swelling of the throat and voice box obstructs the airway, the disease's most feared event, causing asphyxia that demands emergency airway management.
- `connects-to` → **[Large Intestine](../../06-organ/large-intestine/README.md)** — Hereditary angioedema swells the bowel wall: attacks edema the gut, including the large intestine, causing severe colicky pain, vomiting, and wall thickening that can mimic a surgical abdomen and trigger needless operations.
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — Hereditary angioedema hinges on bradykinin clearance in tissues like the kidney: enzymes (ACE, neprilysin) that degrade bradykinin act here, which is why ACE-inhibitor blood-pressure drugs can unmask or worsen bradykinin angioedema.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — The deadliest hereditary angioedema attacks swell the larynx and airway, threatening asphyxiation, which is why patients carry on-demand bradykinin-blocking rescue therapy for laryngeal attacks.
- `connects-to` → **[Hepatocyte](../../04-cellular/hepatocyte/README.md)** — C1-esterase inhibitor is made by hepatocytes, so the liver is the source of the very protein whose deficiency causes hereditary angioedema—and the target of newer liver-directed gene therapies.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — During a gut attack, CT and ultrasound photons reveal the telltale bowel-wall edema and free fluid, helping distinguish hereditary angioedema from a true surgical abdomen and avert needless operations.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy shows how the swelling forms: bradykinin pries open the junctions between endothelial cells, widening the gaps so plasma floods out into the tissue — the leak that makes the deep, non-itchy edema of an attack.
- `connects-to` → **[Eye](../../06-organ/eye/README.md)** — Attacks often disfigure the face and eyes: bradykinin-driven swelling balloons the lips and eyelids, sometimes closing the eyes entirely, a dramatic but self-limited facial angioedema that warns a laryngeal attack may follow.
- `connects-to` → **[Brain](../../06-organ/brain/README.md)** — Rarely the swelling reaches the brain: case reports describe cerebral edema during severe attacks, with headaches, transient deficits, or seizures from bradykinin acting on the brain's blood vessels.
- `connects-to` → **[Stomach](../../06-organ/stomach/README.md)** — Gut attacks masquerade as a surgical emergency: angioedema of the bowel wall brings severe cramping abdominal pain, vomiting, and even shock, mimicking an acute abdomen and leading to needless operations before the diagnosis is known.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — Antibodies enter on both sides of angioedema: the acquired form can be driven by autoantibodies against C1-inhibitor, while modern prophylaxis uses lanadelumab, a monoclonal antibody that blocks the kallikrein generating bradykinin.
- `connects-to` → **[Albumin](../../03-molecular/albumin/README.md)** — An attack is plasma escaping the vessels: bradykinin opens the endothelial junctions so intravascular fluid floods the tissues, and severe abdominal attacks shift enough volume to cause hemoconcentration and a drop in blood pressure.
- `connects-to` → **[Pancreas](../../06-organ/pancreas/README.md)** — An abdominal attack mimics a surgical emergency: bradykinin swells the bowel wall into cramping pain, vomiting, and ascites that look like acute pancreatitis or appendicitis, leading to needless operations before HAE is recognized.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — Bradykinin is also a pain signal: the same kinin that swells the tissues excites sensory neurons, contributing to the tingling, prickling prodrome that warns of an attack and the visceral pain of abdominal episodes.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — Living under threat exacts a mental toll: the unpredictable, potentially fatal laryngeal attacks breed chronic anxiety and depression, and the resulting hypervigilance and impaired quality of life are now recognized as part of the disease burden.
- `connects-to` → **[Helicobacter pylori](../../../02-pathogen/02-bacteria/helicobacter-pylori/README.md)** — A stomach bug can set off the belly attacks: Helicobacter pylori infection is linked to more frequent abdominal angioedema attacks in hereditary angioedema, and eradicating it can reduce them — a treatable trigger worth seeking.
- `connects-to` → **[CLL](../cll/README.md)** — A lymphoma can mimic the hereditary disease: acquired C1-inhibitor deficiency, producing identical bradykinin-driven angioedema, arises in B-cell disorders like CLL, so adult-onset angioedema without family history prompts a search for an underlying lymphoproliferative tumor.
- `connects-to` → **[B Cell](../../04-cellular/b-cell/README.md)** — B cells can turn on the body's own brake: in acquired angioedema, B-cell clones make autoantibodies against C1-inhibitor or consume it, depleting the very protein whose hereditary deficiency causes the inherited form.
- `connects-to` → **[Prostaglandins (Eicosanoids)](../../03-molecular/prostaglandins/README.md)** — Bradykinin works partly through downstream vasodilators: at the endothelium it triggers release of prostaglandins and nitric oxide that widen vessels and leak fluid, amplifying the swelling that defines an attack.
- `connects-to` → **[Neutrophil](../../04-cellular/neutrophil/README.md)** — Innate inflammation feeds into the kinin system: neutrophil-derived proteases can cleave kininogen and activate the contact pathway, so the inflammation of an intercurrent infection can help tip a patient into an angioedema attack.
- `connects-to` → **[Panic Disorder](../panic-disorder/README.md)** — Unpredictable suffocation breeds fear: the threat of sudden, potentially fatal laryngeal swelling drives high rates of anxiety and panic in patients, a psychological toll that, like the depression already linked, is part of living with the disease.
- `connects-to` → **[Intestinal Epithelium](../../05-tissue/intestinal-epithelium/README.md)** — Attacks swell the gut wall from within: bradykinin-driven edema of the intestinal submucosa beneath the epithelium causes cramping pain, vomiting and even bowel obstruction, abdominal attacks so severe they are often mistaken for a surgical emergency.
- `connects-to` → **[ACE2](../../03-molecular/ace2/README.md)** — A second enzyme helps clear the trigger: ACE2 degrades the active bradykinin metabolite des-Arg9-bradykinin, so its activity helps terminate attacks — a counterpart to the ACE inhibition that, by blocking bradykinin breakdown, can precipitate angioedema.
- `connects-to` → **[Generalized Anxiety Disorder](../generalized-anxiety-disorder/README.md)** — Living between attacks breeds chronic worry: beyond acute fear, the constant vigilance over triggers, rescue medication and the unpredictability of the next swelling fosters a persistent generalized anxiety that constrains daily life.
- `connects-to` → **[Hepatocellular Carcinoma](../hcc/README.md)** — Its old prophylactic drug can grow liver tumors: long-term attenuated androgens like danazol, once a mainstay of HAE prevention, cause hepatic adenomas that can transform, a reason these agents are now used cautiously.
- `connects-to` → **[Venous Thromboembolism](../venous-thromboembolism/README.md)** — Both the disease's treatments raise clot risk: attenuated androgens used for prophylaxis and C1-inhibitor concentrate given for attacks each carry a recognized thrombotic risk, so venous thromboembolism is a treatment hazard in HAE.
- `connects-to` → **[Type 2 Diabetes](../type-2-diabetes/README.md)** — Androgen prophylaxis skews metabolism: the weight gain, dyslipidemia and insulin resistance from long-term attenuated androgens like danazol push HAE patients toward type 2 diabetes, part of why safer therapies are preferred.
- `connects-to` → **[Atherosclerosis](../atherosclerosis/README.md)** — Its androgen prophylaxis worsens the arteries: long-term danazol lowers HDL and raises LDL, and this drug-induced dyslipidemia accelerates atherosclerosis, another reason attenuated androgens are now second-line in HAE.
- `connects-to` → **[PTSD](../ptsd/README.md)** — Near-fatal swelling can traumatize: surviving laryngeal attacks that threaten suffocation, sometimes with emergency airway procedures, can leave HAE patients with post-traumatic stress on top of their anxiety.
- `connects-to` → **[Sepsis](../sepsis/README.md)** — Its attacks invite risky intervention: laryngeal swelling can force emergency intubation or surgical airways, and abdominal attacks mimicking a surgical abdomen can lead to unnecessary operations, each carrying infection and sepsis risk.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — Its hallmark is swelling of the skin: HAE produces recurrent non-itchy subcutaneous angioedema of the face, limbs and genitals, often preceded by the rash-like prodrome of erythema marginatum.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — Hormones both trigger and treat it: oestrogen from the pill or pregnancy worsens HAE attacks, while attenuated androgens like danazol have long been used as prophylaxis, tying the disease to the endocrine system.
- `connects-to` → **[Cardiovascular System](../cardiovascular-system/README.md)** — It runs on the bradykinin pathway shared with blood-pressure drugs: HAE swelling is bradykinin-mediated, so ACE inhibitors, which block bradykinin breakdown, are contraindicated and can precipitate severe attacks.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — It can rarely reach the brain: cerebral angioedema is an uncommon but serious HAE attack causing headache, seizures and transient neurological deficits, and bradykinin itself is a potent driver of pain.
- `connects-to` → **[Renal System](../renal-system/README.md)** — Attacks can swell the urinary tract: bradykinin-mediated angioedema of the bladder and urethra during an HAE attack can cause painful dysuria and acute urinary retention.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — Deep limb attacks disable and deceive: HAE swelling of the hands, feet and limbs can be painful and disabling and is often mistaken for cellulitis, compartment syndrome or arthritis, delaying correct treatment.
- `connects-to` → **[ACE Inhibitors](../../../03-medicine/01-modern/04-cardio/ace-inhibitors/README.md)** — One drug class is forbidden: ACE inhibitors are contraindicated in HAE because they block the breakdown of bradykinin, the mediator of its swelling, and can precipitate severe attacks.
- `connects-to` → **[Helicobacter pylori](../../../02-pathogen/02-bacteria/helicobacter-pylori/README.md)** — A stomach bug can stoke its attacks: Helicobacter pylori infection is associated with more frequent HAE attacks, and eradicating it can reduce attack frequency in some patients.
- `connects-to` → **[Multiple Myeloma](../multiple-myeloma/README.md)** — Its acquired mimic flags a blood cancer: acquired C1-inhibitor deficiency, which mimics HAE, is associated with B-cell lymphoproliferative disorders and monoclonal gammopathy.
- `connects-to` → **[Targeted Therapy](../../../03-medicine/01-modern/13-cancer/targeted-therapy/README.md)** — Modern prophylaxis is a targeted antibody: lanadelumab, a monoclonal antibody against plasma kallikrein, prevents the bradykinin-driven attacks of hereditary angioedema.
- `connects-to` → **[ARBs](../../../03-medicine/01-modern/04-cardio/arbs/README.md)** — A cautious alternative to ACE inhibitors: angiotensin-receptor blockers are preferred over ACE inhibitors in hereditary angioedema, as ACE inhibition raises bradykinin and can precipitate severe attacks.
- `connects-to` → **[Corticosteroids](../../../03-medicine/01-modern/02-respiratory/corticosteroids/README.md)** — Allergy drugs do not work here: unlike histamine-mediated angioedema, the bradykinin-driven swelling of hereditary angioedema does not respond to corticosteroids, antihistamines or adrenaline — a crucial distinction.
- `connects-to` → **[COVID-19 Disease](../covid-19-disease/README.md)** — A shared bradykinin axis: HAE is driven by unchecked bradykinin, and the same kinin pathway — amplified when SARS-CoV-2 disrupts ACE2 — was proposed to drive the vascular leak of severe COVID-19, prompting trials of HAE drugs like icatibant.
- `connects-to` → **[Cancer Chemotherapy](../../../03-medicine/01-modern/13-cancer/cancer-chemotherapy/README.md)** — Treating the cause of acquired angioedema: an acquired C1-inhibitor deficiency mimicking HAE arises in CLL, myeloma and lymphoma, where chemotherapy or rituximab against the underlying clone can resolve the angioedema.
- `connects-to` → **[Aspirin](../../../03-medicine/01-modern/04-cardio/aspirin/README.md)** — Bradykinin, not prostaglandin, drives it: unlike ACE inhibitors, which raise bradykinin and are contraindicated, aspirin and NSAIDs do not trigger hereditary angioedema and are generally tolerated — a useful point in analgesic choice.
- `connects-to` → **[Hereditary Pancreatitis](../hereditary-pancreatitis/README.md)** — Diseases of an unchecked protease cascade: hereditary angioedema unleashes the kallikrein-bradykinin cascade when C1-inhibitor fails, much as hereditary pancreatitis unleashes trypsin when its SPINK1 inhibitor fails—each a missing brake on a destructive enzyme.
- `connects-to` → **[DLBCL](../dlbcl/README.md)** — Acquired angioedema points to lymphoma: acquired C1-inhibitor deficiency arises with B-cell lymphoproliferative disorders such as diffuse large B-cell lymphoma and autoantibodies, causing bradykinin angioedema in older adults without a family history.
- `connects-to` → **[Arterial Wall](../../05-tissue/arterial-wall/README.md)** — Bradykinin makes the vessels leak: in hereditary angioedema, unopposed bradykinin acts on B2 receptors of the vascular endothelium to increase permeability, so plasma escapes the vessel wall into tissue as the non-itchy, non-pitting swelling.
- `connects-to` → **[Hepatic Lobule](../../05-tissue/hepatic-lobule/README.md)** — Where the missing protein is made: C1-inhibitor is synthesised by hepatocytes in the liver lobule, which is why attenuated androgens that boost hepatic synthesis—and emerging liver-targeted RNA and gene therapies—act here.
- `connects-to` → **[Waldenström Macroglobulinemia](../waldenstrom-macroglobulinemia/README.md)** — Acquired angioedema's clue: new-onset angioedema in an older adult without family history suggests acquired C1-inhibitor deficiency, classically from a lymphoproliferative clone such as Waldenström macroglobulinaemia or an MGUS.
- `connects-to` → **[Germinal Center](../../05-tissue/germinal-center/README.md)** — Autoantibodies behind acquired disease: acquired angioedema can arise from anti-C1-inhibitor autoantibodies produced by germinal-centre-derived B-cell clones, distinguishing it from the purely genetic hereditary form.
- `connects-to` → **[Follicular Lymphoma](../follicular-lymphoma/README.md)** — An indolent lymphoma trigger: follicular lymphoma is among the low-grade B-cell neoplasms that consume C1-inhibitor and cause acquired angioedema, which can improve when the lymphoma is treated.
- `connects-to` → **[Mantle Cell Lymphoma](../mantle-cell-lymphoma/README.md)** — Another lymphoproliferative cause: mantle-cell lymphoma joins the B-cell malignancies that can produce acquired C1-inhibitor deficiency, so new late-onset angioedema warrants a search for occult lymphoma.
- `connects-to` → **[Spleen](../../06-organ/spleen/README.md)** — A splenic source: splenic marginal-zone lymphoma is a classic cause of acquired angioedema, the clone consuming C1-inhibitor, and treating the lymphoma or removing the spleen can resolve the attacks.
- `connects-to` → **[Angiopoietin](../../03-molecular/angiopoietin/README.md)** — Endothelial barrier control: the angiopoietin-Tie2 axis governs endothelial junction stability, and its dysregulation contributes to the vascular leak that produces angioedema swelling.
- `connects-to` → **[Fibrinogen](../../03-molecular/fibrinogen/README.md)** — Contact-system crosstalk: activated factor XII in hereditary angioedema triggers both bradykinin generation and the coagulation cascade, so fibrinogen turnover and D-dimer rise during attacks.
- `connects-to` → **[Von Willebrand Factor](../../03-molecular/von-willebrand-factor/README.md)** — Endothelial activation marker: angioedema attacks activate the endothelium to release von Willebrand factor from Weibel-Palade bodies, reflecting the vascular disturbance driving the swelling.
- `connects-to` → **[Platelet](../../04-cellular/platelet/README.md)** — Contact-system amplifier: activated platelets release inorganic polyphosphate that triggers factor XII autoactivation, feeding the kallikrein-kinin cascade that generates the bradykinin driving HAE swelling.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — Distinguishing mechanism: HAE is bradykinin-mediated, not IgE/mast-cell-mediated like allergic angioedema, which is why antihistamines, epinephrine and steroids fail and B2R/kallikrein-targeted drugs are needed.
- `connects-to` → **[Glucocorticoid Receptor](../../03-molecular/glucocorticoid-receptor/README.md)** — Why steroids fail: corticosteroids acting through the glucocorticoid receptor relieve histaminergic angioedema but not bradykinin-mediated HAE attacks, a key clinical contrast underscoring the disease's distinct pathophysiology.
- `connects-to` → **[Antithrombin](../../03-molecular/antithrombin/README.md)** — Antithrombin and C1-esterase-inhibitor are both serpins that restrain the contact-pathway proteases (factor XIIa, factor XIa); the loss of the C1-INH arm in HAE leaves the kallikrein-kinin cascade unchecked, generating bradykinin unopposed.
- `connects-to` → **[Adrenomedullin](../../03-molecular/adrenomedullin/README.md)** — Adrenomedullin tightens endothelial cell junctions to stabilize the vascular barrier—the physiological opposite of the bradykinin-driven junctional opening that produces the deep, non-pitting tissue swelling characteristic of HAE attacks.
- `connects-to` → **[Renin](../../03-molecular/renin/README.md)** — The kallikrein-kinin and renin-angiotensin systems converge on ACE, which both degrades bradykinin and generates angiotensin II—the reason ACE inhibitors precipitate dangerous, sometimes laryngeal attacks and are absolutely contraindicated in HAE.
- `connects-to` → **[FcRn](../../03-molecular/fcrn/README.md)** — The IgG anti-plasma-kallikrein antibody lanadelumab relies on FcRn recycling for its weeks-long half-life, enabling subcutaneous prophylaxis that suppresses kallikrein and prevents the bradykinin generation driving HAE attacks.
- `connects-to` → **[C5aR1](../../03-molecular/c5ar1/README.md)** — C1-inhibitor is the main brake on the classical-complement C1 complex as well as the contact system, so its deficiency causes the chronic complement consumption and low C4 that are diagnostic, even though the swelling itself is bradykinin-mediated.
- `connects-to` → **[Endothelin-1](../../03-molecular/endothelin-1/README.md)** — The angioedema of HAE is produced at the vascular endothelium, where bradykinin opens inter-endothelial junctions to let plasma leak—the same endothelial barrier whose baseline tone and integrity endothelin-1 helps regulate.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — Bradykinin signaling through the B2 receptor activates endothelial NF-κB, amplifying the vascular inflammation and permeability that drive the swelling of a hereditary-angioedema attack.
- `connects-to` → **[Interleukin-6](../../03-molecular/il-6/README.md)** — HAE attacks are accompanied by a systemic acute-phase response with rising IL-6, reflecting the contact-system activation and endothelial inflammation that accompany the bradykinin-driven swelling.
- `connects-to` → **[TNF-α (Tumor Necrosis Factor-alpha)](../../03-molecular/tnf-alpha/README.md)** — TNF-α released during the endothelial activation of HAE attacks further loosens inter-endothelial junctions, compounding the bradykinin-driven vascular leak that produces the angioedema.
- `connects-to` → **[Substance P](../../03-molecular/substance-p/README.md)** — Like bradykinin (mapped), substance P is a vascular-permeability neuropeptide degraded by ACE, and the overlap explains why ACE inhibitors precipitate bradykinin-mediated angioedema.
- `connects-to` → **[CGRP](../../03-molecular/cgrp/README.md)** — CGRP is a potent vasodilator and permeability mediator that contributes to the tissue swelling of an angioedema attack alongside bradykinin.
- `connects-to` → **[Protein C](../../03-molecular/protein-c/README.md)** — C1-esterase inhibitor (mapped) also restrains the intrinsic coagulation cascade (FXIIa, FXIa), so its deficiency in HAE perturbs the coagulation balance that the protein-C anticoagulant system normally maintains.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — Bradykinin acting on the B2 receptor activates PI3K-AKT-eNOS signaling (nitric oxide mapped) that increases the endothelial permeability driving HAE swelling attacks.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — Bradykinin B2-receptor signaling engages ERK-MAPK in endothelial cells, contributing to the vascular-permeability response of hereditary angioedema attacks.
- `connects-to` → **[NLRP3 Inflammasome](../../03-molecular/nlrp3-inflammasome/README.md)** — Contact-system and bradykinin activation can engage the NLRP3 inflammasome, an inflammatory amplifier increasingly implicated in the pathophysiology of angioedema attacks.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — PI3K signaling downstream of the bradykinin B2 receptor on endothelial cells contributes to the eNOS activation and vascular permeability of the angioedema attacks in hereditary angioedema.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Galectin-3 modulates endothelial activation and vascular inflammation relevant to the localized permeability that produces the swelling of hereditary angioedema.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — IL-6-STAT3 signaling transduces the acute-phase inflammatory response that accompanies the attacks of hereditary angioedema.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — JAK1/2-STAT cytokine signaling (IL-6 already mapped) modulates the endothelial inflammatory tone that influences attack susceptibility in hereditary angioedema.
- `connects-to` → **[HIF-1alpha](../../03-molecular/hif-1alpha/README.md)** — HIF-1α-VEGF signaling (VEGF already mapped) heightens the vascular permeability that underlies the bradykinin-driven swelling of hereditary angioedema.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — FOXO downstream of bradykinin-PI3K-AKT signaling (AKT and PIK3CA already mapped) regulates the endothelial oxidative-stress and barrier responses in hereditary angioedema.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β modulates the endothelial and inflammatory signaling relevant to the vascular permeability of hereditary angioedema attacks.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — S100A8/A9 alarmins reflect the inflammatory activation accompanying hereditary angioedema attacks.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — mTOR signaling downstream of PI3K-AKT (AKT already mapped) participates in the endothelial-barrier regulation relevant to the swelling of hereditary angioedema.
- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — SRC-family kinase signaling downstream of the bradykinin B2 receptor participates in the VE-cadherin disruption and endothelial-barrier breakdown of hereditary angioedema.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — IFN-STAT1 signaling participates in the endothelial and immune context modulating the attacks of hereditary angioedema.
- `connects-to` → **[NRF2](../../03-molecular/nfe2l2/README.md)** — NRF2 (NFE2L2)-mediated oxidative-stress defense modulates the endothelial responses relevant to hereditary angioedema.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK-linked metabolic and eNOS-coupled signaling participates in the endothelial homeostasis relevant to the vascular permeability of hereditary angioedema.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — Autophagy modulates the endothelial-cell homeostasis and stress responses relevant to hereditary angioedema.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — DNMT3A-mediated DNA methylation participates in the epigenetic modulation of the contact-system and endothelial gene expression relevant to hereditary angioedema.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — CXCL12-CXCR4 signaling participates in the endothelial and vascular responses relevant to hereditary angioedema.
- `connects-to` → **[Adenosine](../../03-molecular/adenosine/README.md)** — Adenosine signaling participates in the vascular-tone and permeability modulation relevant to hereditary angioedema.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — IL-1β-driven inflammation participates in the inflammatory amplification of the angioedema attacks of hereditary angioedema.
- `connects-to` → **[Progesterone](../../03-molecular/progesterone/README.md)** — Hormonal modulation: estrogen worsens hereditary angioedema (already mapped) while progestins and attenuated androgens (testosterone already mapped) reduce attacks, so progesterone-based contraception is a preferred option in the estrogen-sensitive and type III forms.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — Endothelial alarmin: IL-33 released from activated or injured endothelium increases vascular permeability, a mechanism that can amplify the bradykinin-driven endothelial leak underlying the swelling of an angioedema attack.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — Inflammatory amplification: IL-17A-driven inflammation participates in the endothelial activation and inflammatory milieu that can aggravate the severity of hereditary angioedema attacks beyond the core bradykinin pathway.
- `connects-to` → **[Immunoglobulin G](../../03-molecular/immunoglobulin-g/README.md)** — Acquired C1-INH deficiency: an acquired angioedema mimicking the hereditary disease arises from IgG autoantibodies against C1-inhibitor (already mapped), usually with an underlying B-cell lymphoproliferative disorder, a key differential of bradykinin-mediated swelling.
- `connects-to` → **[MHC class II](../../03-molecular/mhc-class-ii/README.md)** — Autoantibody presentation: in acquired C1-inhibitor deficiency, MHC class II-restricted T-cell help underlies the anti-C1-INH autoantibody response, distinguishing this immune-mediated form from the genetic deficiency of hereditary angioedema.
- `connects-to` → **[IL-2](../../03-molecular/il-2/README.md)** — Lymphoproliferative association: IL-2-driven lymphocyte proliferation underlies the B-cell disorders linked to acquired C1-inhibitor deficiency, the clonal expansions that consume C1-inhibitor or generate the autoantibodies causing acquired angioedema.
- `connects-to` → **[Aldosterone](../../03-molecular/aldosterone/README.md)** — Kinin-RAAS crosstalk: angiotensin-converting enzyme both generates angiotensin II (already mapped) toward aldosterone and degrades bradykinin (already mapped), so ACE inhibitors raise bradykinin and can precipitate angioedema attacks, contraindicated in hereditary angioedema.
- `connects-to` → **[IL-10](../../03-molecular/il-10/README.md)** — Immune regulation in acquired disease: IL-10 and immunoregulatory signals shape the autoreactive response of acquired C1-inhibitor deficiency (IL-6 already mapped), the immune-mediated form distinct from the genetic deficiency of hereditary angioedema.
- `connects-to` → **[T-helper cell](../../04-cellular/t-helper-cell/README.md)** — Autoantibody help: CD4 T-cell help (MHC class II and IL-2 already mapped) supports the B cells producing the anti-C1-inhibitor autoantibodies of acquired angioedema, distinguishing it from the inherited C1-inhibitor deficiency.
- `connects-to` → **[Zinc](../../02-atomic/zinc/README.md)** — Contact-system activation: zinc is required for the assembly of factor XII and high-molecular-weight kininogen on surfaces that triggers the kallikrein-kinin cascade generating the bradykinin (already mapped) of hereditary angioedema.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — Histaminergic differential: IL-4 drives the mast-cell (already mapped) type-2 response of the far commoner histamine-mediated (already mapped) allergic angioedema, the differential that must be excluded before treating the bradykinin-mediated hereditary form.
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — Type-2 differential: IL-13, with IL-4 (already mapped), supports the type-2 mast-cell (already mapped) response of the allergic angioedema differential, which unlike hereditary angioedema responds to antihistamines and steroids.
- `connects-to` → **[BAFF](../../03-molecular/baff/README.md)** — Acquired C1-INH deficiency: BAFF supports the B cells of the lymphoproliferative disorders (CLL and lymphomas already mapped) that cause acquired C1-inhibitor deficiency, the key acquired-angioedema differential of the hereditary form.
- `connects-to` → **[CD20](../../03-molecular/cd20/README.md)** — Rituximab in acquired AAE: the CD20 B cells of the underlying lymphoproliferative disorder are targeted by rituximab to treat the acquired C1-inhibitor deficiency, distinguishing its therapy from that of hereditary angioedema.
- `connects-to` → **[Type I interferon](../../03-molecular/type-i-interferon/README.md)** — Autoimmune-associated angioedema: the type-I interferon of the autoimmune diseases (systemic lupus already mapped) associated with acquired C1-inhibitor deficiency reflects the immune dysregulation and complement (C3 already mapped) consumption of that differential.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Metabolic-hormonal adipokine: leptin is the adipokine of the metabolic-inflammatory milieu; the oestrogen (already mapped) and metabolic modulation of the attack frequency of hereditary angioedema.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — Metabolic adipokine: adiponectin, with leptin (already mapped), is part of the adipokine dimension of the metabolic milieu of hereditary angioedema.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), is the adipose-inflammatory adipokine of the metabolic-inflammatory milieu of hereditary angioedema.
- `connects-to` → **[Natural killer cell](../../04-cellular/natural-killer-cell/README.md)** — Innate immune modulation: the NK cells (perforin already mapped) are part of the broader innate immune context of hereditary angioedema, distinct from the complement (C3 already mapped) and bradykinin (already mapped) core mechanism.
- `connects-to` → **[IFN-gamma](../../03-molecular/ifn-gamma/README.md)** — Th1 arm: the IFN-γ of the T cells is the type-II interferon arm (with the type-I interferon already mapped) of the subtle immune-inflammatory dimension of hereditary angioedema.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the immune-inflammatory dimension accompanying hereditary angioedema.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune milieu, distinguishing the bradykinin-mediated (already mapped) angioedema from the type-2/mast-cell (histamine already mapped) angioedema.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the subtle immune-inflammatory dimension accompanying hereditary angioedema.
- `connects-to` → **[Dendritic cell](../../04-cellular/dendritic-cell/README.md)** — Antigen presentation: the dendritic cells present antigen (MHC already mapped) within the immune microenvironment accompanying hereditary angioedema.
- `connects-to` → **[Factor H](../../03-molecular/factor-h/README.md)** — Complement regulation: factor H regulates the alternative complement pathway, complementing the C1-esterase-inhibitor (already mapped) control of the classical/lectin pathways and the contact (bradykinin already mapped) system dysregulated in hereditary angioedema.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Innate modulation: the macrophages, whose function the broadly anti-inflammatory C1-esterase inhibitor (already mapped) also modulates, are part of the innate-immune context of hereditary angioedema.
- `connects-to` → **[Cytotoxic T cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Adaptive context: the cytotoxic T cells (perforin pathway) are part of the subtle adaptive-immune dimension accompanying the complement/contact-system disorder of hereditary angioedema.
- `connects-to` → **[Regulatory T cell](../../04-cellular/regulatory-t-cell/README.md)** — Immune tolerance: the regulatory T cells are part of the adaptive-immune context that the broadly anti-inflammatory C1-esterase inhibitor (already mapped) helps shape, relevant to the acquired autoimmune forms of angioedema.
- `connects-to` → **[Osteopontin](../../03-molecular/osteopontin/README.md)** — Vascular matricellular: osteopontin, a matricellular cytokine of the vascular wall, is part of the endothelial (already mapped) and vascular-inflammation context of the bradykinin-mediated permeability of hereditary angioedema.
- `connects-to` → **[Transferrin](../../03-molecular/transferrin/README.md)** — Acute-phase iron: transferrin, the iron carrier, is part of the acute-phase and vascular-permeability context accompanying the recurrent attacks of hereditary angioedema.
- `connects-to` → **[TSLP](../../03-molecular/tslp/README.md)** — Mast-cell independent alarmin: TSLP, released by epithelial cells during the oedematous attacks, amplifies the type-2 polarisation of dendritic cells (already mapped) independently of histamine (already mapped) in the immune landscape of hereditary angioedema.
- `connects-to` → **[Erythropoietin](../../03-molecular/erythropoietin/README.md)** — Androgen-EPO axis: erythropoietin synthesis in the liver (already mapped) is enhanced by the androgen therapies (testosterone and danazol) used as prophylaxis in hereditary angioedema, linking the hormonal prevention strategy to the hepatic EPO production of the disease.
- `connects-to` → **[Periostin](../../03-molecular/periostin/README.md)** — Submucosal remodelling: periostin, induced by IL-4 and IL-13 (already mapped) released during oedematous attacks in the submucosal connective tissue, promotes the matricellular remodelling of the swollen tissues in hereditary angioedema.

[^cicardi-2010-icatibant-nejm]: Cicardi M, Banerji A, Bracho F, et al. Icatibant, a new bradykinin-receptor antagonist, in hereditary angioedema. *N Engl J Med.* 2010;363(6):532-541. [doi:10.1056/NEJMoa0906393](https://doi.org/10.1056/NEJMoa0906393) · [PubMed 20818873](https://pubmed.ncbi.nlm.nih.gov/20818873/)
[^maurer-2018-lanadelumab-help]: Banerji A, Riedl MA, Bernstein JA, et al. Effect of lanadelumab compared with placebo on prevention of hereditary angioedema attacks. *JAMA.* 2018;320(20):2108-2121. [doi:10.1001/jama.2018.16773](https://doi.org/10.1001/jama.2018.16773) · [PubMed 30480729](https://pubmed.ncbi.nlm.nih.gov/30480729/)
[^zuraw-2020-berotralstat-apex2]: Zuraw BL, Busse PJ, White M, et al. Berotralstat (BCX7353) for the prevention of hereditary angioedema. *N Engl J Med.* 2021;384(23):2186-2195. [doi:10.1056/NEJMoa2103679](https://doi.org/10.1056/NEJMoa2103679) · [PubMed 34077648](https://pubmed.ncbi.nlm.nih.gov/34077648/)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
