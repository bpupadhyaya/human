---
schema: human-scale-entry/v1
id: systemic-sclerosis
name: Systemic Sclerosis
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-07
summary: "Systemic sclerosis (SSc) is an autoimmune CTD with vasculopathy (Raynaud's), autoantibodies (anti-Scl-70, anti-centromere, anti-RNA pol III), and progressive fibrosis of skin and viscera; limited (lcSSc) vs. diffuse (dcSSc); ILD and PAH are leading causes of death."
aliases: ["SSc", "scleroderma", "systemic scleroderma", "diffuse cutaneous systemic sclerosis", "dcSSc", "limited cutaneous systemic sclerosis", "lcSSc", "CREST syndrome", "anti-Scl-70", "anti-centromere antibody", "SSc-ILD", "SSc-PAH", "scleroderma renal crisis"]
sources:
  - id: denton-2017-ssc-review
    type: peer-reviewed
    cite: "Denton CP, Khanna D. Systemic sclerosis. Lancet. 2017;390(10103):1685-1699."
    doi: "10.1016/S0140-6736(17)30933-9"
    pmid: "28413064"
    url: "https://doi.org/10.1016/S0140-6736(17)30933-9"
  - id: distler-2019-nintedanib-senscis
    type: peer-reviewed
    cite: "Distler O, Highland KB, Gahlemann M, et al. Nintedanib for Systemic Sclerosis-Associated Interstitial Lung Disease. N Engl J Med. 2019;380(26):2518-2528."
    doi: "10.1056/NEJMoa1903076"
    pmid: "31112379"
    url: "https://doi.org/10.1056/NEJMoa1903076"
  - id: khanna-2016-tocilizumab-ssc
    type: peer-reviewed
    cite: "Khanna D, Denton CP, Jahreis A, et al. Safety and efficacy of subcutaneous tocilizumab in adults with systemic sclerosis (faSScinate): a phase 2, randomised, controlled trial. Lancet. 2016;387(10038):2630-2640."
    doi: "10.1016/S0140-6736(16)00932-X"
    pmid: "27156007"
    url: "https://doi.org/10.1016/S0140-6736(16)00932-X"
cross_links:
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "TGF-β1 is the master profibrotic driver in SSc; dermal fibroblasts in dcSSc show constitutive pSMAD2/3 activation → ↑COL1A1, COL3A1, fibronectin, and CTGF; nintedanib (SENSCIS trial) targets PDGFR/VEGFR/FGFR; TGF-β blockade remains a therapeutic target."
  - target: 01-human/07-system/pulmonary-arterial-hypertension
    relation: connects-to
    note: "PAH occurs in 10-15% of SSc (especially lcSSc with anti-centromere antibodies); SSc-PAH is treated identically to IPAH with ERAs + PDE5i; macitentan, ambrisentan, and tadalafil are first-line; SSc-PAH has worse prognosis than IPAH due to concurrent cardiac and pulmonary fibrosis."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "IL-6 is elevated in SSc serum and drives fibrosis via STAT3 → ↑TGF-β and connective tissue growth factor; tocilizumab (anti-IL-6R) slowed FVC decline in SSc-ILD in the focuSSed trial; IL-6 levels correlate with skin score and ILD activity."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Type I IFN signature elevated in ~50% of SSc, especially anti-RNA pol III+ dcSSc; IFN-α activates plasmacytoid DCs → amplifies anti-nuclear antibodies; type I IFN + TGF-β cooperate to drive SSc fibroblast activation and ILD progression."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "Skin fibrosis names systemic sclerosis: TGF-β-activated myofibroblasts deposit collagen, producing taut, hide-bound dermis graded by the modified Rodnan skin score; limited cutaneous SSc spares the trunk while diffuse SSc thickens proximal limbs, predicting organ involvement."
  - target: 01-human/04-cellular/fibroblast
    relation: connects-to
    note: "The effector cell of systemic sclerosis is the myofibroblast (α-SMA+, contractile), driven by TGF-β/SMAD2-3 to oversecrete collagen; in SSc it becomes autonomously fibrogenic through epigenetic FLI1 silencing and persists even without ongoing TGF-β, sustaining fibrosis."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "Scleroderma renal crisis strikes ~10-15% of diffuse SSc (especially anti-RNA-pol-III+) as malignant hypertension with onion-skin arterioles and hemolytic anemia; ACE inhibitors are the only proven therapy, and corticosteroids must be avoided as they can precipitate it."
  - target: 01-human/07-system/sjogrens-syndrome
    relation: connects-to
    note: "Systemic sclerosis and Sjögren's are overlapping connective-tissue autoimmune diseases: secondary Sjögren occurs in up to ~20% of SSc, adding sicca to the fibrosis, and both share a type-I-interferon signature — but SSc is defined by vasculopathy and collagen deposition."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "The lung is the leading cause of death in systemic sclerosis: interstitial lung disease (fibrotic NSIP, worst with anti-Scl-70) scars the lower lobes and pulmonary arterial hypertension narrows vessels; nintedanib and tocilizumab slow the ILD, so CT and PFT surveillance matter."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "Endothelial injury is the first event in systemic sclerosis: damaged microvascular endothelium triggers Raynaud's phenomenon, digital ulcers, and capillary dropout (on nailfold capillaroscopy), then activates fibroblasts — making vasculopathy the initiating arm of the SSc triad."
  - target: 01-human/07-system/systemic-lupus-erythematosus
    relation: connects-to
    note: "Systemic sclerosis and lupus are both ANA-positive connective tissue diseases that can overlap as mixed connective tissue disease: SSc is dominated by fibrosis (anti-Scl-70), lupus by immune-complex inflammation (anti-dsDNA), but both share Raynaud's and interferon."
  - target: 01-human/07-system/dermatomyositis
    relation: connects-to
    note: "Systemic sclerosis and dermatomyositis overlap in scleromyositis: some patients have both skin fibrosis and inflammatory myopathy, marked by anti-PM/Scl antibodies, so muscle weakness in a scleroderma patient prompts evaluation for a myositis overlap."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "The gut is involved in most systemic sclerosis: fibrosis and smooth-muscle atrophy cause esophageal dysmotility and reflux, gastric antral vascular ectasia, small-bowel bacterial overgrowth, and pseudo-obstruction—a major source of morbidity beyond the skin."
  - target: 01-human/07-system/rheumatoid-arthritis
    relation: connects-to
    note: "Systemic sclerosis and rheumatoid arthritis are both systemic autoimmune connective-tissue diseases but differ in target: SSc is dominated by fibrosis and vasculopathy (skin, lung, gut), while RA is an inflammatory synovitis—though the two can overlap in some patients."
  - target: 01-human/03-molecular/collagen
    relation: connects-to
    note: "Systemic sclerosis is fundamentally a disease of excess collagen: TGF-β-activated fibroblasts overproduce and deposit collagen in skin, lung and other organs, hardening tissue and strangling small vessels—a structural protein becoming the agent of organ failure."
  - target: 01-human/04-cellular/smooth-muscle-cell
    relation: connects-to
    note: "Vascular smooth muscle drives the vasculopathy of systemic sclerosis: endothelial injury and smooth-muscle proliferation narrow small arteries, producing Raynaud's, pulmonary hypertension and renal crisis—the vascular, not just fibrotic, face of the disease."
  - target: 01-human/05-tissue/fibrosis
    relation: connects-to
    note: "Systemic sclerosis is the prototypical multi-organ fibrosis: the same fibroblast-driven scarring that heals a wound runs unchecked across skin, lung and gut, so SSc anchors the broader family of fibrotic diseases and is a testbed for antifibrotic drugs like nintedanib."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "The heart is a hidden but lethal systemic sclerosis target: myocardial fibrosis and microvascular disease cause arrhythmias, conduction block and heart failure, often silent until advanced—so cardiac involvement is a leading cause of death in scleroderma."
  - target: 01-human/03-molecular/endothelin-1
    relation: connects-to
    note: "Endothelin-1 drives the vasculopathy of systemic sclerosis: this potent vasoconstrictor, overproduced by injured endothelium, fuels Raynaud's phenomenon and pulmonary hypertension—so endothelin-receptor blockers (bosentan) treat the vascular side of the disease."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "Systemic sclerosis is fundamentally autoimmune: specific autoantibodies (anti-Scl-70, anti-centromere) define subsets and predict organ risk, and severe cases are treated by resetting the immune system with autologous stem-cell transplant."
  - target: 01-human/04-cellular/b-cell
    relation: connects-to
    note: "B cells drive systemic sclerosis beyond autoantibodies: they secrete pro-fibrotic IL-6 and activate fibroblasts, so rituximab (anti-CD20 B-cell depletion) is increasingly used to slow skin and lung fibrosis in progressive disease."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "Helper T cells orchestrate the fibrosis of systemic sclerosis: Th2 and Th17 cytokines (IL-4, IL-13, IL-17) push fibroblasts toward collagen overproduction, linking the adaptive immune response directly to the tissue scarring that defines the disease."
  - target: 01-human/03-molecular/angiotensin-ii
    relation: connects-to
    note: "Scleroderma renal crisis is an angiotensin-II emergency: sudden malignant hypertension and kidney failure from activated renin-angiotensin once killed many patients, but ACE inhibitors blocking angiotensin II converted it into a treatable complication."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Calcinosis is the 'C' of CREST in systemic sclerosis: calcium deposits in skin and soft tissue form painful, sometimes ulcerating nodules, one of the hallmark features of limited cutaneous disease alongside Raynaud's and esophageal involvement."
  - target: 01-human/03-molecular/nitric-oxide
    relation: connects-to
    note: "Systemic sclerosis vasculopathy reflects lost nitric oxide: damaged endothelium makes too little NO and too much endothelin, so vessels constrict—driving Raynaud's, digital ulcers and pulmonary hypertension treated with vasodilators that restore NO signaling."
  - target: 01-human/03-molecular/pdgf
    relation: connects-to
    note: "Systemic sclerosis fibrosis is driven by PDGF: the growth factor (and stimulatory anti-PDGFR antibodies) push fibroblasts into collagen-spewing myofibroblasts, so PDGFR-blocking drugs like nintedanib slow the lung scarring."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Systemic sclerosis is fibrosed by M2 macrophages: alternatively-activated macrophages flood the skin and lung and secrete TGF-beta and other signals that drive the relentless collagen deposition central to the disease."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "Mast cells mark early systemic sclerosis: they accumulate in affected skin and release mediators that activate fibroblasts and inflame vessels, contributing to both the fibrosis and the Raynaud's vasculopathy of the disease."
  - target: 01-human/06-organ/large-intestine
    relation: connects-to
    note: "Systemic sclerosis most often strikes inside at the gut: fibrosis and nerve damage slow the intestine, causing reflux, bloating, bacterial overgrowth and malabsorption—the commonest internal-organ involvement of the disease."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "Plasmacytoid dendritic cells pour out the interferon that drives systemic sclerosis: their type-I interferon signature activates fibroblasts and inflames vessels, sitting near the top of the cascade that scleroderma therapies target."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "Systemic sclerosis chokes the fingers of oxygen: Raynaud's and a damaged microvasculature cut blood flow, so digital ischemia and ulcers—and tissue hypoxia that feeds more fibrosis—are hallmarks of the vascular side of the disease."
  - target: 01-human/02-atomic/hydrogen
    relation: connects-to
    note: "Scleroderma drowns the esophagus in acid: it weakens the esophageal muscle so reflux floods up, and the hydrogen-ion exposure scars the lining into strictures and Barrett's change."
  - target: 01-human/06-organ/stomach
    relation: connects-to
    note: "Scleroderma marks the stomach with 'watermelon' stripes: it causes gastric antral vascular ectasia (GAVE), rows of dilated vessels that ooze and cause chronic iron-deficiency anemia."
  - target: 01-human/05-tissue/bone-marrow
    relation: connects-to
    note: "Severe scleroderma is reset from the bone marrow: autologous hematopoietic stem-cell transplant wipes and rebuilds the immune system, halting the relentless fibrosis in carefully selected patients."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "A beam of light reads scleroderma at the fingertip: nailfold capillaroscopy magnifies the nailbed to reveal the dilated, dropout-riddled capillaries that flag the vasculopathy early, while HRCT photons map the lung fibrosis it causes."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "The limited form often drags in the liver: CREST-pattern scleroderma overlaps strongly with primary biliary cholangitis, so anti-mitochondrial antibodies and a slow autoimmune attack on the bile ducts frequently accompany it."
  - target: 01-human/04-cellular/platelet
    relation: connects-to
    note: "Platelets stoke scleroderma's vascular fire: activated on the damaged vessel lining, they pour out PDGF and serotonin that drive the smooth-muscle growth and fibrosis narrowing the arteries, feeding the Raynaud's and pulmonary hypertension."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "Scleroderma's autoantibodies predict its course: anti-Scl-70 flags diffuse disease with lung fibrosis, anticentromere the limited CREST form with pulmonary hypertension, and anti-RNA-polymerase-III the dreaded scleroderma renal crisis."
  - target: 01-human/06-organ/small-intestine
    relation: connects-to
    note: "Fibrosis stalls the small bowel: scleroderma replaces gut smooth muscle with scar, so the small intestine loses its propulsion — breeding bacterial overgrowth, malabsorption, and at worst a pseudo-obstruction that mimics a surgical blockage."
  - target: 01-human/04-cellular/erythrocyte
    relation: connects-to
    note: "Scleroderma bleeds and shears the red cells: the gastric 'watermelon stomach' (GAVE) leaks chronic iron-deficiency anemia, while renal crisis can shred erythrocytes into a microangiopathic hemolytic anemia."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "Scleroderma scars the sexual organs too: erectile dysfunction from vascular and fibrotic damage is common and often early in men, while women face vaginal dryness and tightening, and pregnancy carries added risk of renal crisis."
  - target: 01-human/05-tissue/peripheral-nerve
    relation: connects-to
    note: "The fibrosis can pinch and starve nerves: scleroderma causes trigeminal sensory neuropathy and entrapment syndromes like carpal tunnel, as thickened tissue and a damaged microvasculature injure the peripheral nerves."
  - target: 03-medicine/03-food/vitamin-d
    relation: connects-to
    note: "Vitamin D runs low in scleroderma: gut malabsorption, sun avoidance over fragile skin, and the disease itself leave most patients deficient, a shortfall linked to worse skin and lung fibrosis and to the bone loss they accrue."
  - target: 01-human/03-molecular/wnt-beta-catenin
    relation: connects-to
    note: "Wnt keeps the fibroblasts switched on: persistent Wnt/beta-catenin signaling drives the fibroblast-to-myofibroblast transition that lays down relentless collagen, a pathway that helps explain why scleroderma's fibrosis self-perpetuates."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: connects-to
    note: "Broken immune restraint feeds the fibrosis: a shortfall and dysfunction of regulatory T cells lets profibrotic Th2 and Th17 responses run unchecked, tying the autoimmunity of scleroderma to its scarring."
  - target: 01-human/06-organ/thyroid
    relation: connects-to
    note: "Scleroderma keeps autoimmune company: autoimmune thyroid disease, both Hashimoto's hypothyroidism and Graves', is over-represented in systemic sclerosis, so thyroid function is part of the routine workup."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "Allergy-type cytokines turn fibrotic here: IL-13 with IL-4 from a Th2-skewed response goads fibroblasts into making collagen, an arm of the fibrotic drive alongside TGF-β that is a target for the antifibrotic strategies in scleroderma."
  - target: 01-human/04-cellular/cardiomyocyte
    relation: connects-to
    note: "The heart muscle scars from within: microvascular damage and fibrosis lay down collagen between cardiomyocytes, producing the myocardial fibrosis, conduction problems and heart failure that make cardiac involvement a leading cause of death in scleroderma."
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "The kidneys can fail abruptly or slowly: scleroderma renal crisis brings sudden hypertensive kidney failure, while chronic vascular injury erodes function over time, leaving chronic kidney disease as a lasting toll of the vasculopathy."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "STAT3 links inflammation to fibrosis: downstream of IL-6, STAT3 activation in fibroblasts and immune cells drives the collagen-producing program, making it a studied node in scleroderma's self-sustaining fibrotic loop."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "The vasculopathy raises clot risk: systemic sclerosis carries an increased rate of deep-vein thrombosis and pulmonary embolism, layered on top of its hallmark microvascular and pulmonary-arterial disease."
  - target: 01-human/07-system/sepsis
    relation: connects-to
    note: "Skin and lung breaches invite infection: digital ulcers from Raynaud-driven ischemia and aspiration into fibrotic lungs from esophageal dysmotility give scleroderma several routes to serious infection and sepsis."
  - target: 02-pathogen/03-fungi/candida-albicans
    relation: connects-to
    note: "Its stiff esophagus is a niche for the yeast: the esophageal dysmotility, acid reflux and chronic PPI use of scleroderma favor Candida esophagitis, adding fungal infection to the swallowing difficulty the fibrosis already causes."
  - target: 01-human/07-system/heart-failure
    relation: connects-to
    note: "Fibrosis can stiffen the heart itself: myocardial scarring and microvascular disease in scleroderma cause a primary cardiomyopathy, and combined with its pulmonary hypertension this drives both right- and left-sided heart failure."
  - target: 01-human/07-system/anemia-of-chronic-disease
    relation: connects-to
    note: "Inflammation and gut bleeding lower the count: chronic IL-6-driven inflammation plus blood loss from gastric antral vascular ectasia (watermelon stomach) combine to produce the anemia of chronic disease common in scleroderma."
  - target: 01-human/07-system/stroke
    relation: connects-to
    note: "Its vasculopathy reaches the brain's arteries: the obliterative small-vessel disease and accelerated atherosclerosis of systemic sclerosis extend beyond the skin and lungs, raising the long-term risk of ischemic stroke."
  - target: 02-pathogen/03-fungi/aspergillus-fumigatus
    relation: connects-to
    note: "Its lung disease and immunosuppression invite mold: scleroderma-associated interstitial lung disease, treated with mycophenolate, cyclophosphamide or rituximab, leaves scarred and immune-suppressed lungs vulnerable to invasive aspergillosis."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "A disfiguring, progressive disease wears on mood: the visible skin tightening, disability, pain and poor prognosis of systemic sclerosis substantially impair quality of life and carry high rates of depression."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "The skin is its defining organ: systemic sclerosis hardens and thickens the skin through excess collagen, with sclerodactyly, calcinosis, telangiectasia and Raynaud's, the visible hallmark of the disease."
  - target: 01-human/07-system/wound-healing
    relation: connects-to
    note: "Fibrosis and ischaemia cripple healing: the Raynaud's and microvascular damage of systemic sclerosis cause painful digital ulcers over the fingertips that are notoriously slow to heal and can gangrene."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "A progressive, disfiguring multi-organ disease breeds worry: the relentless skin and organ involvement, painful ulcers and uncertain prognosis of systemic sclerosis foster chronic health anxiety alongside depression."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "It scars the lungs: interstitial lung disease from progressive pulmonary fibrosis is the leading cause of death in systemic sclerosis, alongside the pulmonary hypertension it also drives."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "It can strike the kidneys abruptly: scleroderma renal crisis brings malignant hypertension and acute kidney injury, a once-fatal emergency now treated with ACE inhibitors."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "Fibrosis stiffens joints and deposits calcium: systemic sclerosis causes joint contractures, tendon friction rubs, calcinosis of the soft tissues and an inflammatory myopathy."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "It spasms the small vessels and scars the heart: Raynaud's phenomenon — episodic digital vasospasm — is an almost universal early feature, and myocardial fibrosis causes arrhythmia and heart failure."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "It has a signature nerve sign: trigeminal neuralgia is a characteristic neurological association of systemic sclerosis, alongside carpal tunnel syndrome and autonomic and peripheral neuropathy."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "It clusters with thyroid disease: autoimmune hypothyroidism is a common association, and fibrosis of the thyroid gland can further impair its function."
  - target: 03-medicine/01-modern/04-cardio/ace-inhibitors
    relation: connects-to
    note: "They are life-saving in renal crisis: ACE inhibitors are the treatment for scleroderma renal crisis, the malignant hypertension and acute kidney injury that once made it fatal."
  - target: 03-medicine/01-modern/04-cardio/calcium-channel-blockers
    relation: connects-to
    note: "They ease the cold fingers: calcium-channel blockers like nifedipine are first-line for the Raynaud's phenomenon that nearly always accompanies systemic sclerosis."
  - target: 03-medicine/01-modern/02-respiratory/corticosteroids
    relation: connects-to
    note: "Steroids must be used with caution: high-dose corticosteroids can precipitate scleroderma renal crisis, so they are limited despite the inflammation of early diffuse systemic sclerosis."
  - target: 03-medicine/01-modern/13-cancer/cancer-chemotherapy
    relation: connects-to
    note: "Cyclophosphamide and transplant for severe disease: cyclophosphamide is used for progressive scleroderma lung and skin fibrosis, and autologous haematopoietic stem-cell transplant can halt rapidly diffuse disease by resetting the autoimmune system."
  - target: 03-medicine/01-modern/13-cancer/targeted-therapy
    relation: connects-to
    note: "Antifibrotics and cytokine blockade: nintedanib, an anti-fibrotic multikinase inhibitor, slows scleroderma-associated interstitial lung disease, while tocilizumab against IL-6 and rituximab against B cells temper the fibrosing inflammation."
  - target: 01-human/05-tissue/arterial-wall
    relation: connects-to
    note: "A vasculopathy as much as a fibrosis: systemic sclerosis remodels small arteries with intimal proliferation and luminal narrowing — the onion-skin lesions of scleroderma renal crisis and the digital-artery disease behind Raynaud's and digital ulcers."
  - target: 01-human/05-tissue/myocardium
    relation: connects-to
    note: "It silently scars the heart muscle: systemic sclerosis lays down primary myocardial fibrosis and microvascular ischaemia that cause arrhythmias, conduction block and heart failure—often clinically silent until advanced, and a leading cause of death."
  - target: 01-human/05-tissue/glomerulus
    relation: connects-to
    note: "Scleroderma renal crisis starves the filter: renin-driven malignant hypertension and arteriolar thrombotic microangiopathy cut blood flow to the glomeruli, causing acute kidney injury that prompt ACE inhibition can reverse."
  - target: 01-human/07-system/thrombotic-thrombocytopenic-purpura
    relation: connects-to
    note: "A thrombotic microangiopathy of its own: scleroderma renal crisis produces microangiopathic haemolysis and thrombocytopenia that mimic thrombotic thrombocytopenic purpura, but with normal ADAMTS13—a key distinction in the TMA differential."
  - target: 01-human/05-tissue/alveolus
    relation: connects-to
    note: "The leading cause of death: SSc-associated interstitial lung disease scars the alveolar walls into a stiff, fibrotic lung, and progressive fibrosis here now kills more scleroderma patients than renal crisis."
  - target: 01-human/05-tissue/cortical-bone
    relation: connects-to
    note: "Bone and soft-tissue destruction: SSc causes acro-osteolysis—resorption of the distal phalangeal cortical bone—alongside subcutaneous calcinosis, deforming the fingertips."
  - target: 01-human/07-system/gvhd
    relation: connects-to
    note: "A fibrosis it imitates: chronic sclerodermatous graft-versus-host disease reproduces SSc's skin tightening and fibrosis, showing how alloimmune and autoimmune injury converge on the same fibrotic endpoint."
  - target: 01-human/07-system/esophageal-cancer
    relation: connects-to
    note: "Reflux to malignancy: severe oesophageal dysmotility and chronic acid reflux in systemic sclerosis drive Barrett's metaplasia, raising the long-term risk of oesophageal adenocarcinoma."
  - target: 01-human/07-system/breast-cancer
    relation: connects-to
    note: "Cancer-triggered autoimmunity: anti-RNA-polymerase-III-positive systemic sclerosis is associated with a synchronous cancer, often breast or lung, within a few years—a paraneoplastic scleroderma where the tumour appears to spark the disease."
  - target: 01-human/05-tissue/cardiac-conduction-system
    relation: connects-to
    note: "Fibrosis hits the wiring: patchy myocardial fibrosis in systemic sclerosis scars the cardiac conduction system, causing heart block and ventricular arrhythmias that are a leading cause of sudden death in the disease."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "Disordered angiogenesis: dysregulated VEGF underlies the vasculopathy of systemic sclerosis—capillary dropout and dilated telangiectasias reflecting failed, abnormal new-vessel growth."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "Th2 profibrotic axis: IL-4, with IL-13, drives the Th2-skewed immune response that activates fibroblasts and lays down the excess collagen of systemic sclerosis."
  - target: 01-human/07-system/anca-vasculitis
    relation: connects-to
    note: "Scleroderma-ANCA overlap: a subset of systemic sclerosis patients are MPO-ANCA positive and develop an overlapping ANCA-associated vasculitis with glomerulonephritis, distinct from scleroderma renal crisis."
  - target: 01-human/03-molecular/ccl2
    relation: connects-to
    note: "Monocyte recruitment: CCL2 draws monocytes and profibrotic macrophages into the skin and lung of systemic sclerosis, fuelling the inflammation that precedes fibrosis."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "Th17 fibrosis: IL-17 from Th17 cells contributes to the inflammatory and profibrotic response of systemic sclerosis, modulating fibroblast activation."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "Vascular hypoxia: the obliterative vasculopathy of systemic sclerosis creates tissue hypoxia that stabilises HIF-1α, paradoxically failing to restore perfusion while driving fibrosis."
  - target: 01-human/03-molecular/cd20
    relation: connects-to
    note: "B-cell depletion: rituximab targets CD20+ B cells in systemic sclerosis, reducing skin and lung fibrosis — evidence that autoreactive B cells and their autoantibodies (anti-Scl70, anti-RNA-pol III) drive the disease, not just fibroblasts."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "Signalling convergence: the IFN and IL-6 signatures of systemic sclerosis act through JAK-STAT, making JAK1/2 inhibitors (tofacitinib) a candidate to dampen both the inflammatory and profibrotic arms of the disease."
  - target: 01-human/03-molecular/serotonin
    relation: connects-to
    note: "Serotonergic fibrosis: platelet-derived serotonin acting on 5-HT2B receptors stimulates dermal fibroblasts to make collagen and contributes to the vasoconstriction of Raynaud's, linking platelet activation to scleroderma fibrosis."
  - target: 01-human/03-molecular/periostin
    relation: connects-to
    note: "Matricellular fibrosis: periostin is upregulated in the skin and lung of systemic sclerosis, where this matricellular protein crosslinks collagen and amplifies TGF-β-driven fibroblast activation, and serum periostin tracks the extent of fibrosis."
  - target: 01-human/03-molecular/angiopoietin
    relation: connects-to
    note: "Vasculopathy: an imbalance of angiopoietin-Tie2 signalling destabilises the microvasculature of systemic sclerosis, contributing to the capillary loss, digital ulcers and pulmonary arterial hypertension that mark its obliterative vasculopathy."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "Profibrotic alarmin: IL-33 released from damaged endothelium and epithelium in systemic sclerosis activates type-2 innate lymphoid cells and amplifies the IL-13/IL-4 axis, driving the Th2-skewed fibrotic response in skin and lung."
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "TGF-β-SMAD fibrosis: TGF-β signals through the SMAD pathway (common mediator SMAD4) to drive the fibroblast activation and excess collagen deposition central to systemic sclerosis, the core fibrotic mechanism of the disease."
  - target: 01-human/03-molecular/pf4
    relation: connects-to
    note: "CXCL4 biomarker: CXCL4/platelet factor 4, released by plasmacytoid dendritic cells, is a leading systemic-sclerosis biomarker that drives the type-I interferon response and fibrosis, linking platelet and innate-immune activation to the disease."
  - target: 01-human/03-molecular/baff
    relation: connects-to
    note: "B-cell activation: BAFF-driven B-cell survival and autoantibody production contribute to systemic sclerosis, the rationale for the B-cell-depleting therapy (rituximab against the CD20 already mapped) used in skin and lung disease."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "Fibroblast proliferation: PDGFR and FGFR signalling (PDGF mapped) drives the MAPK-ERK cascade that activates fibroblasts in systemic sclerosis, the axis blocked by the antifibrotic TKI nintedanib."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "Myofibroblast differentiation: mTOR signalling promotes the differentiation of fibroblasts into collagen-secreting myofibroblasts (collagen mapped), driving the progressive fibrosis of systemic sclerosis."
  - target: 01-human/03-molecular/myd88
    relation: connects-to
    note: "TLR-driven fibrosis: endogenous DAMPs activate TLR4 on fibroblasts, signalling through MyD88 to sustain TGF-β-driven (mapped) collagen production and the persistent fibrosis of systemic sclerosis."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "Inflammation-fibrosis loop: NF-κB-driven inflammatory transcription amplifies the cytokine production and fibroblast activation that perpetuate the inflammation-fibrosis loop of systemic sclerosis."
  - target: 01-human/03-molecular/nfe2l2
    relation: connects-to
    note: "Oxidative vasculopathy: NRF2 antioxidant defence counters the oxidative stress driving the endothelial injury and fibroblast activation central to the vasculopathy and fibrosis of systemic sclerosis."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "Myofibroblast survival: PI3K-AKT signalling promotes the activation, survival and matrix production of the myofibroblasts (alongside TGF-β/SMAD already mapped) that drive the fibrosis of systemic sclerosis."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Galectin-3 is a key profibrotic mediator and biomarker driving the skin and lung fibrosis of systemic sclerosis."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "Type-I-interferon signalling through STAT1 (type-I-interferon mapped) underlies the interferon signature characteristic of systemic sclerosis."
  - target: 01-human/03-molecular/pten
    relation: connects-to
    note: "Loss of PTEN in systemic-sclerosis fibroblasts releases the PI3K-AKT-mTOR signalling (AKT and mTOR mapped) that drives myofibroblast activation and fibrosis."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "Cytosolic DNA sensing through cGAS-STING drives the type-I-interferon signature (type-I interferon already mapped) central to the autoimmunity of systemic sclerosis."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "FOXO transcription factors modulate the oxidative-stress and survival balance of the activated myofibroblasts that drive the fibrosis of systemic sclerosis."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "GSK-3β signalling regulates the fibroblast-to-myofibroblast transition and the persistent fibrosis of systemic sclerosis."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "S100A8/A9 alarmins amplify the innate inflammation driving the fibrosis of systemic sclerosis."
  - target: 01-human/03-molecular/perforin
    relation: connects-to
    note: "Perforin-mediated cytotoxicity contributes to the endothelial injury underlying the vasculopathy of systemic sclerosis."
  - target: 01-human/03-molecular/cdk4-6
    relation: connects-to
    note: "CDK4/6-driven proliferation of myofibroblasts contributes to the fibrotic tissue expansion of systemic sclerosis."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "PI3K (PIK3CA)-AKT signaling (AKT already mapped) drives the fibroblast activation and myofibroblast differentiation of systemic sclerosis."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC-family kinase signaling downstream of PDGFR (PDGF already mapped) drives the fibroblast activation and fibrosis of systemic sclerosis."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Autophagy modulates the myofibroblast differentiation and fibrotic responses of systemic sclerosis."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK-linked metabolic signaling participates in the myofibroblast and immune-cell metabolism of systemic sclerosis."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-driven leukocyte recruitment contributes to the inflammatory and fibrotic tissue infiltration of systemic sclerosis."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "DNMT3A-mediated DNA methylation participates in the epigenetic dysregulation of the fibroblast and immune-cell responses of systemic sclerosis."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "CXCL12-CXCR4 signaling participates in the vasculopathy and fibrotic-cell recruitment of systemic sclerosis."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "IL-1β-driven inflammation participates in the inflammatory and fibrotic processes of systemic sclerosis."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Complement C3 participates in the vascular injury and immune activation of systemic sclerosis."
  - target: 01-human/03-molecular/immunoglobulin-g
    relation: connects-to
    note: "Autoantibody serology: systemic sclerosis is defined serologically by IgG autoantibodies, anti-topoisomerase-1 (Scl-70), anti-centromere and anti-RNA-polymerase-III, that stratify the risk of diffuse skin, lung fibrosis and renal crisis."
  - target: 01-human/03-molecular/prostaglandins
    relation: connects-to
    note: "Vascular therapy: prostacyclin, a prostaglandin, and its analogues such as iloprost dilate vessels and inhibit platelets to treat the digital ischaemia, ulcers and pulmonary hypertension of the systemic-sclerosis vasculopathy."
  - target: 01-human/03-molecular/bnp
    relation: connects-to
    note: "Pulmonary hypertension screening: systemic sclerosis is a leading cause of connective-tissue-disease pulmonary arterial hypertension, and BNP/NT-proBNP release from the strained right ventricle guides the annual screening that detects this lethal complication."
  - target: 01-human/03-molecular/hemoglobin
    relation: connects-to
    note: "Gut bleeding and haemolysis: gastric antral vascular ectasia (watermelon stomach) causes chronic gastrointestinal bleeding in systemic sclerosis, and scleroderma renal crisis brings microangiopathic haemolysis, both lowering haemoglobin."
  - target: 01-human/03-molecular/troponin-complex
    relation: connects-to
    note: "Myocardial fibrosis: systemic sclerosis can directly fibrose the myocardium and conduction system, and troponin elevation marks the primary cardiac involvement that, alongside pulmonary hypertension (BNP already mapped), contributes to its mortality."
  - target: 01-human/03-molecular/mhc-class-ii
    relation: connects-to
    note: "HLA and autoantibodies: specific HLA class II alleles determine which autoantibody a patient develops (anti-topoisomerase, anti-centromere or anti-RNA-polymerase III), and MHC class II antigen presentation drives the autoimmunity of systemic sclerosis."
  - target: 01-human/03-molecular/adamts13
    relation: connects-to
    note: "Renal-crisis microangiopathy: scleroderma renal crisis causes a thrombotic microangiopathy with normal ADAMTS13 (unlike thrombotic thrombocytopenic purpura), the endothelial injury driving the haemolysis and acute kidney failure."
  - target: 01-human/03-molecular/xanthine-oxidase
    relation: connects-to
    note: "Oxidative fibrosis: reactive oxygen species, to which xanthine oxidase contributes, are generated in the hypoxic, inflamed tissues of systemic sclerosis, and this oxidative stress (NRF2 already mapped) helps drive the endothelial injury and fibroblast activation."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "Immunoregulatory balance: the anti-inflammatory IL-10 counters the profibrotic type-2 and type-17 responses (IL-4, IL-13 and IL-17 already mapped), and the imbalance between them shapes the autoimmunity and fibrosis of systemic sclerosis."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Anaemia and GI bleeding: the chronic inflammation and the gastric antral vascular ectasia (watermelon stomach) of systemic sclerosis cause anaemia (haemoglobin already mapped) from iron loss and sequestration, a common systemic complication."
  - target: 01-human/03-molecular/histamine
    relation: connects-to
    note: "Mast-cell involvement: mast cells release histamine in the early inflammatory, pruritic phase of the skin (already mapped) fibrosis of systemic sclerosis, contributing to the itch and the fibroblast-activating (already mapped) inflammation."
  - target: 01-human/03-molecular/renin
    relation: connects-to
    note: "Scleroderma renal crisis: the renin-angiotensin system (angiotensin II already mapped) is dramatically activated in scleroderma renal crisis, and ACE inhibitors blocking it transformed this once-fatal complication of systemic sclerosis."
  - target: 01-human/03-molecular/hepcidin
    relation: connects-to
    note: "Anaemia of chronic disease: the IL-6-driven (already mapped) hepcidin sequesters iron (already mapped) to produce the anaemia of chronic disease that, with the GAVE blood loss, causes the anaemia of systemic sclerosis."
  - target: 01-human/03-molecular/von-willebrand-factor
    relation: connects-to
    note: "Endothelial injury marker: the endothelial injury of the vasculopathy (endothelin-1 already mapped) raises von Willebrand factor, a marker of the endothelial activation that drives the Raynaud's and vascular disease of systemic sclerosis."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Anti-fibrotic adipokine: adiponectin is an anti-fibrotic adipokine, and its fall as the dermal adipose is lost to fibrosis removes a brake on the fibroblast (already mapped) activation, promoting the fibrosis of systemic sclerosis."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Pro-fibrotic adipokine: leptin, opposite to the anti-fibrotic adiponectin (already mapped), is a pro-fibrotic adipokine that promotes the fibroblast (already mapped) activation and the fibrosis of systemic sclerosis."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Adipose-inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), is the adipose-inflammatory adipokine of the immune-metabolic milieu of systemic sclerosis."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "Wound-healing zinc: the disturbed zinc homeostasis and the impaired wound healing of the fibrotic, ulcer-prone (digital ulcers) skin (already mapped) of systemic sclerosis."
  - target: 01-human/04-cellular/plasma-cell
    relation: connects-to
    note: "Autoantibody plasma cells: the plasma cells (from the B cells — CD20 and BAFF already mapped) secrete the anti-Scl-70/centromere autoantibodies (immunoglobulin already mapped) of systemic sclerosis."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Th1 arm: the IFN-γ of the T cells (with the type-I interferon already mapped) is the type-II interferon arm of the immune dysregulation of systemic sclerosis."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm balancing the Th2 (IL-4 and IL-13 already mapped) profibrotic drive of systemic sclerosis."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Type-2 profibrotic arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the profibrotic immune drive of systemic sclerosis."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the inflammatory-fibrotic dimension of systemic sclerosis."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the profibrotic autoimmunity of systemic sclerosis."
  - target: 01-human/03-molecular/tslp
    relation: connects-to
    note: "Profibrotic alarmin: TSLP, an epithelial alarmin, initiates and amplifies the type-2 (IL-4 and IL-13 already mapped) immunity that drives the fibroblast (already mapped) activation and periostin (already mapped) remodelling of systemic sclerosis."
  - target: 01-human/03-molecular/c5ar1
    relation: connects-to
    note: "Complement C5a receptor: the C5aR1 signalling (with the complement C3 already mapped) contributes to the microvascular injury and the inflammatory dimension of the vasculopathy of systemic sclerosis."
  - target: 01-human/03-molecular/il-31
    relation: connects-to
    note: "Pruritus cytokine: IL-31, a type-2 (IL-4 and IL-13 already mapped) cytokine, is the pruritogenic effector of the frequent and burdensome itch of the sclerotic skin of systemic sclerosis."
  - target: 01-human/03-molecular/complement-c5
    relation: connects-to
    note: "Terminal complement: the complement C5 and its activation (with C3 and C5aR1 already mapped) contribute to the microvascular injury and the inflammatory vasculopathy of systemic sclerosis."
  - target: 01-human/03-molecular/factor-h
    relation: connects-to
    note: "Complement regulation: factor H regulates the alternative complement pathway (complement C3, C5 and C5aR1 already mapped) whose dysregulation contributes to the endothelial (already mapped) injury of systemic sclerosis."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Cytotoxic infiltrate: the cytotoxic T cells (perforin already mapped) infiltrate the sclerotic skin and lung and contribute to the endothelial injury and the fibroblast (already mapped) activation of systemic sclerosis."
  - target: 01-human/03-molecular/bradykinin
    relation: connects-to
    note: "Vasomotor mediator: bradykinin, released by kallikrein activation in the ischaemia-reperfusion cycles of Raynaud's phenomenon, amplifies the vascular permeability and digital pain that accompany the microvascular disease of systemic sclerosis."
  - target: 01-human/03-molecular/c1-esterase-inhibitor
    relation: connects-to
    note: "Classical complement brake: C1-esterase inhibitor modulates the classical complement pathway (C3, C5 and C5aR1 already mapped) activated by the anti-endothelial autoantibodies on the sclerotic vascular wall of systemic sclerosis."
  - target: 01-human/03-molecular/erythropoietin
    relation: connects-to
    note: "Scleroderma anaemia: erythropoietin addresses the anaemia of chronic inflammation and the renal-crisis-driven erythropoietin deficiency of systemic sclerosis; EPO may also modulate the pulmonary-artery vascular remodelling (PAH already mapped)."
  - target: 01-human/03-molecular/melatonin
    relation: connects-to
    note: "Circadian antifibrotic: melatonin is reduced in systemic sclerosis and exerts antifibrotic effects by suppressing TGF-β (already mapped) signalling and fibroblast (already mapped) collagen production, while modulating the Th1/Th2 imbalance."
  - target: 01-human/03-molecular/prolactin
    relation: connects-to
    note: "Profibrotic autoimmune amplifier: prolactin is elevated in a subset of systemic sclerosis patients and modulates the B-cell (BAFF already mapped) and T-cell autoimmunity driving the fibrosis and endothelial injury of the disease."
  - target: 01-human/03-molecular/oxytocin
    relation: connects-to
    note: "Vascular neuromodulator: oxytocin receptors on endothelial and smooth-muscle cells (already mapped) modulate vascular tone; oxytocin deficiency may contribute to the Raynaud's vasospasm and the endothelial dysfunction of systemic sclerosis."
  - target: 01-human/03-molecular/testosterone
    relation: connects-to
    note: "SSc testosterone: testosterone exerts anti-fibrotic effects in systemic sclerosis; androgen deficiency contributes to the female sex predominance, and androgen-receptor signalling on fibroblasts (already mapped) modulates TGF-β (already mapped)-driven collagen deposition."
  - target: 01-human/03-molecular/vasopressin
    relation: connects-to
    note: "SSc vasopressin: vasopressin (ADH) modulates renal water retention (kidney already mapped) and vascular tone in systemic sclerosis; in scleroderma renal crisis, AVP-mediated vasoconstriction amplifies the angiotensin-II (already mapped)-driven hypertensive emergency."
  - target: 01-human/02-atomic/selenium
    relation: connects-to
    note: "SSc selenium: selenium selenoproteins counter the oxidative stress driving endothelial injury and fibroblast (already mapped) activation in systemic sclerosis; selenium deficiency amplifies NF-κB (already mapped) inflammation and worsens the pulmonary fibrosis of the disease."
  - target: 01-human/02-atomic/iodine
    relation: connects-to
    note: "SSc iodine: iodine-dependent thyroid hormones modulate fibroblast (already mapped) and TGF-β (already mapped)-driven collagen deposition in systemic sclerosis; autoimmune thyroid disease (Hashimoto thyroiditis) coexists in SSc and amplifies fibrotic and vascular manifestations."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "SSc sodium: sodium-driven osmotic Th17 polarisation amplifies NF-κB (already mapped) and IL-17A (already mapped)-mediated vascular and fibroblast (already mapped) activation in systemic sclerosis; high dietary sodium worsens inflammatory and fibrotic phases of scleroderma."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "SSc magnesium: magnesium deficiency amplifies NF-κB (already mapped) and TGF-β (already mapped)-driven fibroblast (already mapped) activation in systemic sclerosis; magnesium-dependent enzymes regulate collagen cross-linking and fibrotic remodelling of scleroderma."
  - target: 01-human/02-atomic/copper
    relation: connects-to
    note: "SSc copper: copper, as lysyl oxidase cofactor in fibroblasts (already mapped), drives collagen cross-linking; copper amplifies VEGF (already mapped); copper excess amplifies TGF-β (already mapped) and NF-κB (already mapped) cascade of systemic sclerosis."
  - target: 01-human/02-atomic/potassium
    relation: connects-to
    note: "SSc potassium: potassium efflux via NLRP3 inflammasome in macrophages (already mapped) and mast-cell (already mapped) drives IL-6 (already mapped) secretion; potassium dysregulation amplifies TGF-β (already mapped) and NF-κB (already mapped) cascade of SSc."
  - target: 01-human/02-atomic/phosphorus
    relation: connects-to
    note: "SSc phosphorus: phosphorus, as ATP precursor in fibroblasts (already mapped) and endothelial-cell (already mapped), fuels TGF-β (already mapped) collagen synthesis; phosphorus deficiency impairs dendritic-cell (already mapped) and amplifies NF-κB (already mapped) cascade of SSc."
  - target: 01-human/02-atomic/chloride
    relation: connects-to
    note: "SSc chloride: chloride channels in fibroblasts (already mapped) and endothelial-cell (already mapped) regulate stromal fluid balance; chloride dysregulation amplifies TGF-β (already mapped) and NF-κB (already mapped) fibrotic cascade and worsens pulmonary hypertension of SSc."
  - target: 01-human/02-atomic/sulfur
    relation: connects-to
    note: "SSc sulfur: hydrogen sulfide from endothelial-cell (already mapped) and fibroblasts (already mapped) promotes vasodilation; sulfur deficiency amplifies TGF-β (already mapped) and NF-κB (already mapped) fibrotic cascade and worsens pulmonary vascular remodelling of SSc."
  - target: 01-human/02-atomic/nitrogen
    relation: connects-to
    note: "SSc nitrogen: nitric oxide from endothelial-cell (already mapped) and macrophages (already mapped) maintains vascular tone; nitrogen imbalance amplifies TGF-β (already mapped) and NF-κB (already mapped) fibrotic cascade and pulmonary hypertension of SSc."
  - target: 01-human/02-atomic/carbon
    relation: connects-to
    note: "SSc carbon: carbon, as metabolic backbone of TGF-β (already mapped) and NF-κB (already mapped) in fibroblasts (already mapped) and endothelial-cell (already mapped), drives fibrotic signalling; carbon dysregulation amplifies IL-6 (already mapped) cascade of SSc."
  - target: 01-human/03-molecular/pd-1
    relation: connects-to
    note: "SSc PD-1: PD-1 checkpoint on T-cytotoxic cells (already mapped) and macrophages (already mapped) modulates autoimmune surveillance of fibroblasts (already mapped); PD-1 dysregulation amplifies TGF-β (already mapped) and IL-6 (already mapped) fibrotic cascade of SSc."
  - target: 01-human/03-molecular/glp-1
    relation: connects-to
    note: "SSc GLP-1: GLP-1 signalling in endothelial-cell (already mapped) and macrophages (already mapped) modulates metabolic-immune homeostasis; GLP-1 dysregulation amplifies TGF-β (already mapped) and NF-κB (already mapped) and IL-6 (already mapped) cascade of SSc."
  - target: 01-human/03-molecular/rankl
    relation: connects-to
    note: "SSc RANKL: RANKL signalling in macrophages (already mapped) and fibroblasts (already mapped) modulates bone-immune axis; RANKL excess amplifies NF-κB (already mapped) and angiotensin-II (already mapped) and IL-6 (already mapped) fibrotic cascade of systemic sclerosis."
  - target: 01-human/03-molecular/il-2
    relation: connects-to
    note: "SSc IL-2: IL-2 signalling in T-cells (already mapped) and fibroblasts (already mapped) modulates immune homeostasis; IL-2 deficiency amplifies NF-κB (already mapped) and angiotensin-II (already mapped) and IL-6 (already mapped) fibrotic cascade of systemic sclerosis."
  - target: 01-human/03-molecular/fibronectin
    relation: connects-to
    note: "SSc fibronectin: fibronectin in fibroblasts (already mapped) and macrophages (already mapped) promotes ECM accumulation; fibronectin excess amplifies NF-κB (already mapped) and angiotensin-II (already mapped) and IL-6 (already mapped) fibrotic cascade of systemic sclerosis."
  - target: 01-human/03-molecular/notch
    relation: connects-to
    note: "SSc notch: NOTCH on fibroblasts (already mapped) and macrophages (already mapped) regulates dermal fibrotic remodelling; notch dysregulation amplifies nf-kb (already mapped) and il-6 (already mapped) and tgf-beta (already mapped) fibrotic cascade of systemic sclerosis."
  - target: 01-human/03-molecular/igf-1
    relation: connects-to
    note: "SSc igf-1: IGF-1 from fibroblasts (already mapped) and macrophages (already mapped) promotes dermal fibroblast proliferation; igf-1 excess amplifies nf-kb (already mapped) and il-6 (already mapped) and tgf-beta (already mapped) fibrotic cascade of systemic sclerosis."
  - target: 01-human/03-molecular/activin-a
    relation: connects-to
    note: "SSc activin-a: activin-A from fibroblasts (already mapped) and macrophages (already mapped) regulates fibrotic ECM remodelling; activin-a excess amplifies nf-kb (already mapped) and il-6 (already mapped) and tgf-beta (already mapped) fibrotic cascade of systemic sclerosis."
  - target: 01-human/03-molecular/cgrp
    relation: connects-to
    note: "SSc cgrp: CGRP from macrophages (already mapped) and fibroblasts (already mapped) modulates SSc vascular tone; cgrp excess amplifies nf-kb (already mapped) and il-6 (already mapped) and tgf-beta (already mapped) fibrotic cascade of systemic sclerosis."
  - target: 01-human/03-molecular/calcitonin
    relation: connects-to
    note: "SSc calcitonin: calcitonin from macrophages (already mapped) and fibroblasts (already mapped) modulates SSc calcium balance; calcitonin dysregulation amplifies nf-kb (already mapped) and il-6 (already mapped) and tgf-beta (already mapped) fibrotic cascade of systemic sclerosis."
  - target: 01-human/03-molecular/substance-p
    relation: connects-to
    note: "SSc substance-p: substance-P from macrophages (already mapped) and fibroblasts (already mapped) modulates SSc neuroimmune tone; substance-p excess amplifies nf-kb (already mapped) and il-6 (already mapped) and tgf-beta (already mapped) fibrotic cascade of systemic sclerosis."
  - target: 01-human/03-molecular/insulin-receptor
    relation: connects-to
    note: "SSc insulin-receptor: insulin receptor on macrophages (already mapped) and fibroblasts (already mapped) modulates SSc metabolic fibrosis; insulin-receptor loss amplifies nf-kb (already mapped) and il-6 (already mapped) and tgf-beta (already mapped) fibrotic cascade of SSc."
  - target: 01-human/03-molecular/aldosterone
    relation: connects-to
    note: "SSc aldosterone: aldosterone from macrophages (already mapped) and fibroblasts (already mapped) amplifies SSc salt-fluid fibrosis; aldosterone excess amplifies nf-kb (already mapped) and il-6 (already mapped) and tgf-beta (already mapped) fibrotic cascade of SSc."
  - target: 01-human/03-molecular/androgen-receptor
    relation: connects-to
    note: "SSc androgen-receptor: androgen receptor on macrophages (already mapped) and fibroblasts (already mapped) modulates SSc hormonal fibrosis; androgen-receptor loss amplifies nf-kb (already mapped) and il-6 (already mapped) and tgf-beta (already mapped) fibrotic cascade of SSc."
  - target: 01-human/03-molecular/norepinephrine
    relation: connects-to
    note: "SSc norepinephrine: norepinephrine from macrophages (already mapped) and fibroblasts (already mapped) modulates SSc adrenergic vascular tone; norepinephrine excess amplifies nf-kb (already mapped) and il-6 (already mapped) and tgf-beta (already mapped) fibrotic cascade of SSc."
  - target: 01-human/03-molecular/adrenomedullin
    relation: connects-to
    note: "SSc adrenomedullin: adrenomedullin from macrophages (already mapped) and fibroblasts (already mapped) modulates SSc vascular tone; adrenomedullin excess amplifies nf-kb (already mapped) and il-6 (already mapped) and tgf-beta (already mapped) fibrotic cascade of SSc."
  - target: 01-human/03-molecular/bdnf
    relation: connects-to
    note: "SSc bdnf: BDNF from macrophages (already mapped) and fibroblasts (already mapped) modulates SSc neuroimmune fibrotic tone; bdnf loss amplifies nf-kb (already mapped) and il-6 (already mapped) and tgf-beta (already mapped) fibrotic cascade of SSc."
---

# Systemic Sclerosis

## Overview

**Systemic sclerosis (SSc; scleroderma)** is a systemic autoimmune connective tissue disease characterized by the triad of **vasculopathy**, **autoimmunity** (antinuclear antibodies), and **progressive fibrosis** of the skin and internal organs [^denton-2017-ssc-review]. It is the most severe of the systemic rheumatic diseases, with a standardized mortality ratio 3-5× the general population due to cardiopulmonary complications.

**Epidemiology:**
- Incidence: 2-10 per 100,000 per year; prevalence ~250-300 per 100,000 in the US
- Female predominance (F:M ~4:1); peak onset age 30-50 years
- Higher prevalence in Black women (earlier onset, more severe dcSSc)
- Choctaw Native Americans: highest known prevalence (~469/100,000) due to founder FIBRILLIN-1 variant

**Classification — two major subtypes:**

| Feature | Limited SSc (lcSSc) | Diffuse SSc (dcSSc) |
|---|---|---|
| Skin involvement | Distal to elbows/knees; face | Trunk, proximal limbs; face |
| Time from Raynaud's to fibrosis | Years (Raynaud's may precede by decades) | Months |
| Key autoantibodies | Anti-centromere (anti-CENP-B, 70-80%) | Anti-Scl-70 (anti-topo I, 20-40%); anti-RNA pol III (10-25%) |
| Pulmonary hypertension | PAH more common (~15%) | SSc-ILD more severe |
| Renal crisis | Rare | 10-15% (especially anti-RNA pol III+) |
| Calcinosis | Common (CREST) | Less common |
| Prognosis | Slower progression; better 10-year survival | More rapid organ damage |

**CREST syndrome** (Calcinosis, Raynaud's, Esophageal dysmotility, Sclerodactyly, Telangiectasia) — now considered a subset of lcSSc; anti-centromere antibody characteristic.

## Structure

### Pathogenesis — the triad of vasculopathy, autoimmunity, and fibrosis

SSc pathogenesis proceeds through three interconnected arms:

**1. Vasculopathy — Raynaud's phenomenon and beyond:**
- **Raynaud's phenomenon (RP):** Episodic vasospasm of digital arteries in response to cold or stress → triphasic color change (white/blue/red); >95% of SSc patients; often the presenting symptom, preceding other manifestations by months-decades
- Structural vascular damage: endothelial cell apoptosis → subintimal fibrosis → luminal narrowing → fixed ischemia → digital ulcers, pitting scars, gangrene
- **Nailfold capillaroscopy:** Hallmark diagnostic tool; "SSc pattern" = enlarged/giant capillaries + avascular areas + hemorrhages; distinguishes SSc-RP from primary RP
- Mediators: ET-1 ↑, NO ↓ (impaired eNOS), VEGF paradoxically elevated but ineffective due to receptor downregulation

**2. Autoimmunity — antinuclear antibodies:**
- **Anti-Scl-70 (anti-topoisomerase I; anti-topo I):** Target: DNA topoisomerase I (130 kDa nuclear protein); ~20-40% of SSc; strongly predicts diffuse skin disease and ILD; mutually exclusive with anti-centromere
- **Anti-centromere antibody (ACA; anti-CENP-B):** Target: centromere protein B; ~70-80% of lcSSc; predicts PAH and primary biliary cholangitis overlap
- **Anti-RNA polymerase III (anti-RNAP III):** Target: RNA pol III largest subunit; ~10-25% of SSc; strongly predicts scleroderma renal crisis and rapid dcSSc skin progression; associated with cancer-triggered SSc (coincident cancer ~18%)
- **Anti-fibrillarin (anti-U3-RNP):** Severe dcSSc with musculoskeletal and cardiac involvement
- **Anti-PM/Scl:** SSc-myositis overlap; anti-NOR-90, anti-Th/To: SSc-PAH overlap

**3. Fibrosis — myofibroblast activation:**
- Sequence: Injury/autoimmunity → macrophage M2 polarization → TGF-β1/PDGF secretion → fibroblast → **myofibroblast** (α-SMA+, contractile, high collagen secretion)
- TGF-β1 → SMAD2/3 phosphorylation → SMAD2/3-SMAD4 complex → nucleus → ↑COL1A1, COL1A2, COL3A1, fibronectin (EDA-FN), connective tissue growth factor (CTGF/CCN2)
- **Myofibroblast persistence** in SSc: epigenetic silencing of FLI1 (transcription factor that suppresses collagen) + DNMT3A-mediated hypomethylation of TGF-β-responsive genes → autonomous fibrogenic program even without ongoing TGF-β stimulus
- Type I IFN amplifies this process by activating pDCs → more autoantibody production → more tissue injury → more TGF-β

### Modified Rodnan Skin Score (mRSS)

Standard clinical measure: 17 body areas each scored 0-3 (0 = normal, 3 = hide-bound) → maximum score 51; primary endpoint in dcSSc trials. mRSS correlates with PVR, FVC, and mortality in dcSSc.

## Function

### Organ manifestations and treatment

**Interstitial Lung Disease (SSc-ILD):**
- Most common cause of death in SSc (~35% of SSc deaths); prevalence ~60% of dcSSc, ~35% of lcSSc by HRCT
- Pattern: Non-specific interstitial pneumonia (NSIP) most common (ground-glass + fine reticulation, spares periphery); UIP pattern in ~10-15% (worse prognosis)
- Treatment:
  - **Mycophenolate mofetil (MMF):** SLS-II trial (equivalent to oral cyclophosphamide with better tolerability); current first-line for SSc-ILD
  - **Nintedanib (Ofev):** Tyrosine kinase inhibitor targeting PDGFR-α/β, VEGFR-1/2/3, FGFR-1/2/3; SENSCIS trial (576 patients): −44.9 mL/year FVC decline vs. −87.9 mL/year placebo (p<0.001); FDA approved for SSc-ILD in 2019 [^distler-2019-nintedanib-senscis]
  - **Tocilizumab (Actemra):** Anti-IL-6R; faSScinate Phase 2 (skin score improvement, trend toward FVC benefit); focuSSed Phase 3: slowed FVC decline −4.2 vs. −6.3 mL/year (not statistically significant primary endpoint but numerically meaningful)
  - **Rituximab:** Anti-CD20; observational data suggesting SSc-ILD stabilization; SLS-III Phase 3 ongoing

**Pulmonary Arterial Hypertension (SSc-PAH):**
- 10-15% of SSc patients; SSc is the most common cause of CTD-PAH
- Annual echocardiographic screening for all SSc patients; confirmed by RHC (mPAP >20 mmHg + PVR ≥2 WU + PAWP ≤15 mmHg)
- Treatment: ERAs + PDE5i (same as IPAH); macitentan, ambrisentan + tadalafil (AMBITION regimen)
- SSc-PAH prognosis worse than IPAH: 3-year survival ~55-60% vs. >80% in IPAH

**Scleroderma Renal Crisis (SRC):**
- ~10-15% of dcSSc, especially anti-RNA pol III+ patients; onset typically within 5 years of diagnosis
- Pathophysiology: renal arteriolar intimal proliferation (onion-skin lesion) → ischemia → renin release → accelerated hypertension → microangiopathic hemolytic anemia
- Presentation: acute hypertensive emergency (often sudden severe HTN), AKI, microangiopathy (thrombocytopenia, schistocytes)
- **Treatment: ACE inhibitors** (captopril, enalapril) — the only therapy proven to improve outcomes; 50% still progress to ESRD despite treatment; avoid corticosteroids (precipitate SRC)

**Gastrointestinal:**
- Esophageal dysmotility: most common GI manifestation (>90%); smooth muscle atrophy → impaired LES function → GERD → Barrett's esophagus risk; treat with PPI + prokinetics
- Small bowel: dysmotility → bacterial overgrowth (chronic diarrhea, malabsorption, weight loss); antibiotic rotation (rifaximin, metronidazole, ciprofloxacin)
- Gastric antral vascular ectasia (GAVE; "watermelon stomach"): endoscopic ablation

**Musculoskeletal:**
- Inflammatory arthritis, tendon friction rubs (hallmark of active dcSSc — "leather rubbing" on exam), myopathy, calcinosis cutis (CREST)

**Cardiac:**
- Pericardial effusion; myocardial fibrosis → diastolic dysfunction → arrhythmias; coronary vasospasm

## Pathology

**Skin fibrosis (dcSSc):**
Dermis shows marked collagen accumulation, loss of adnexal structures (sweat glands, hair follicles), and perivascular lymphocytic infiltrate in early stages. Late stage: "hide-bound" dermis — grossly thickened, tethered skin; impairs joint mobility.

**Pulmonary NSIP pattern:**
HRCT: Bilateral basal-predominant ground-glass opacity with fine reticulation; traction bronchiectasis in established fibrosis; subpleural sparing distinguishes NSIP from UIP. Histology: temporally uniform inflammation and fibrosis.

**SSc-PAH vascular pathology:**
Identical to IPAH: medial hypertrophy, intimal fibrosis, concentric laminar intimal fibrosis, plexiform lesions. SSc-PAH additionally shows pericapillary fibrosis.

**Autoantibody-associated disease risk (clinical use):**

| Autoantibody | SSc subtype | Associated manifestation |
|---|---|---|
| Anti-Scl-70 (topo I) | dcSSc | ILD (high risk); FVC monitoring required |
| Anti-centromere (CENP-B) | lcSSc | PAH; primary biliary cholangitis overlap |
| Anti-RNA pol III | dcSSc | Scleroderma renal crisis; cancer association |
| Anti-fibrillarin (U3-RNP) | dcSSc | Severe multiorgan; musculoskeletal |
| Anti-PM/Scl | SSc-myositis overlap | Myositis; ILD |
| Anti-Th/To | lcSSc | PAH; SSc-PBC overlap |

## Connections

- `connects-to` → **[TGF-β](../../03-molecular/tgf-beta/README.md)** — TGF-β1 is the master profibrotic driver in SSc; dermal fibroblasts in dcSSc show constitutive pSMAD2/3 activation → ↑COL1A1, COL3A1, fibronectin, and CTGF; nintedanib (SENSCIS trial) targets PDGFR/VEGFR/FGFR; TGF-β blockade remains a therapeutic target.
- `connects-to` → **[Pulmonary Arterial Hypertension](../pulmonary-arterial-hypertension/README.md)** — PAH occurs in 10-15% of SSc (especially lcSSc with anti-centromere antibodies); SSc-PAH is treated identically to IPAH with ERAs + PDE5i; macitentan, ambrisentan, and tadalafil are first-line; SSc-PAH has worse prognosis than IPAH due to concurrent cardiac and pulmonary fibrosis.
- `connects-to` → **[IL-6](../../03-molecular/il-6/README.md)** — IL-6 is elevated in SSc serum and drives fibrosis via STAT3 → ↑TGF-β and connective tissue growth factor; tocilizumab (anti-IL-6R) slowed FVC decline in SSc-ILD in the focuSSed trial; IL-6 levels correlate with skin score and ILD activity.
- `connects-to` → **[Type I Interferon](../../03-molecular/type-i-interferon/README.md)** — Type I IFN signature elevated in ~50% of SSc, especially anti-RNA pol III+ dcSSc; IFN-α activates plasmacytoid DCs → amplifies anti-nuclear antibodies; type I IFN + TGF-β cooperate to drive SSc fibroblast activation and ILD progression.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — Skin fibrosis names systemic sclerosis: TGF-β-activated myofibroblasts deposit collagen, producing taut, hide-bound dermis graded by the modified Rodnan skin score; limited cutaneous SSc spares the trunk while diffuse SSc thickens proximal limbs, predicting organ involvement.
- `connects-to` → **[Fibroblast](../../04-cellular/fibroblast/README.md)** — The effector cell of systemic sclerosis is the myofibroblast (α-SMA+, contractile), driven by TGF-β/SMAD2-3 to oversecrete collagen; in SSc it becomes autonomously fibrogenic through epigenetic FLI1 silencing and persists even without ongoing TGF-β, sustaining fibrosis.
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — Scleroderma renal crisis strikes ~10-15% of diffuse SSc (especially anti-RNA-pol-III+) as malignant hypertension with onion-skin arterioles and hemolytic anemia; ACE inhibitors are the only proven therapy, and corticosteroids must be avoided as they can precipitate it.
- `connects-to` → **[Sjögren's Syndrome](../sjogrens-syndrome/README.md)** — Systemic sclerosis and Sjögren's are overlapping connective-tissue autoimmune diseases: secondary Sjögren occurs in up to ~20% of SSc, adding sicca to the fibrosis, and both share a type-I-interferon signature — but SSc is defined by vasculopathy and collagen deposition.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — The lung is the leading cause of death in systemic sclerosis: interstitial lung disease (fibrotic NSIP, worst with anti-Scl-70) scars the lower lobes and pulmonary arterial hypertension narrows vessels; nintedanib and tocilizumab slow the ILD, so CT and PFT surveillance matter.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — Endothelial injury is the first event in systemic sclerosis: damaged microvascular endothelium triggers Raynaud's phenomenon, digital ulcers, and capillary dropout (on nailfold capillaroscopy), then activates fibroblasts — making vasculopathy the initiating arm of the SSc triad.
- `connects-to` → **[Systemic Lupus Erythematosus](../systemic-lupus-erythematosus/README.md)** — Systemic sclerosis and lupus are both ANA-positive connective tissue diseases that can overlap as mixed connective tissue disease: SSc is dominated by fibrosis (anti-Scl-70), lupus by immune-complex inflammation (anti-dsDNA), but both share Raynaud's and interferon.
- `connects-to` → **[Dermatomyositis](../dermatomyositis/README.md)** — Systemic sclerosis and dermatomyositis overlap in scleromyositis: some patients have both skin fibrosis and inflammatory myopathy, marked by anti-PM/Scl antibodies, so muscle weakness in a scleroderma patient prompts evaluation for a myositis overlap.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — The gut is involved in most systemic sclerosis: fibrosis and smooth-muscle atrophy cause esophageal dysmotility and reflux, gastric antral vascular ectasia, small-bowel bacterial overgrowth, and pseudo-obstruction—a major source of morbidity beyond the skin.
- `connects-to` → **[Rheumatoid Arthritis](../rheumatoid-arthritis/README.md)** — Systemic sclerosis and rheumatoid arthritis are both systemic autoimmune connective-tissue diseases but differ in target: SSc is dominated by fibrosis and vasculopathy (skin, lung, gut), while RA is an inflammatory synovitis—though the two can overlap in some patients.
- `connects-to` → **[Collagen](../../03-molecular/collagen/README.md)** — Systemic sclerosis is fundamentally a disease of excess collagen: TGF-β-activated fibroblasts overproduce and deposit collagen in skin, lung and other organs, hardening tissue and strangling small vessels—a structural protein becoming the agent of organ failure.
- `connects-to` → **[Smooth Muscle Cell](../../04-cellular/smooth-muscle-cell/README.md)** — Vascular smooth muscle drives the vasculopathy of systemic sclerosis: endothelial injury and smooth-muscle proliferation narrow small arteries, producing Raynaud's, pulmonary hypertension and renal crisis—the vascular, not just fibrotic, face of the disease.
- `connects-to` → **[Fibrosis](../../05-tissue/fibrosis/README.md)** — Systemic sclerosis is the prototypical multi-organ fibrosis: the same fibroblast-driven scarring that heals a wound runs unchecked across skin, lung and gut, so SSc anchors the broader family of fibrotic diseases and is a testbed for antifibrotic drugs like nintedanib.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — The heart is a hidden but lethal systemic sclerosis target: myocardial fibrosis and microvascular disease cause arrhythmias, conduction block and heart failure, often silent until advanced—so cardiac involvement is a leading cause of death in scleroderma.
- `connects-to` → **[Endothelin-1](../../03-molecular/endothelin-1/README.md)** — Endothelin-1 drives the vasculopathy of systemic sclerosis: this potent vasoconstrictor, overproduced by injured endothelium, fuels Raynaud's phenomenon and pulmonary hypertension—so endothelin-receptor blockers (bosentan) treat the vascular side of the disease.
- `connects-to` → **[Immune System](../immune-system/README.md)** — Systemic sclerosis is fundamentally autoimmune: specific autoantibodies (anti-Scl-70, anti-centromere) define subsets and predict organ risk, and severe cases are treated by resetting the immune system with autologous stem-cell transplant.
- `connects-to` → **[B Cell](../../04-cellular/b-cell/README.md)** — B cells drive systemic sclerosis beyond autoantibodies: they secrete pro-fibrotic IL-6 and activate fibroblasts, so rituximab (anti-CD20 B-cell depletion) is increasingly used to slow skin and lung fibrosis in progressive disease.
- `connects-to` → **[T Helper Cell](../../04-cellular/t-helper-cell/README.md)** — Helper T cells orchestrate the fibrosis of systemic sclerosis: Th2 and Th17 cytokines (IL-4, IL-13, IL-17) push fibroblasts toward collagen overproduction, linking the adaptive immune response directly to the tissue scarring that defines the disease.
- `connects-to` → **[Angiotensin II](../../03-molecular/angiotensin-ii/README.md)** — Scleroderma renal crisis is an angiotensin-II emergency: sudden malignant hypertension and kidney failure from activated renin-angiotensin once killed many patients, but ACE inhibitors blocking angiotensin II converted it into a treatable complication.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Calcinosis is the 'C' of CREST in systemic sclerosis: calcium deposits in skin and soft tissue form painful, sometimes ulcerating nodules, one of the hallmark features of limited cutaneous disease alongside Raynaud's and esophageal involvement.
- `connects-to` → **[Nitric Oxide](../../03-molecular/nitric-oxide/README.md)** — Systemic sclerosis vasculopathy reflects lost nitric oxide: damaged endothelium makes too little NO and too much endothelin, so vessels constrict—driving Raynaud's, digital ulcers and pulmonary hypertension treated with vasodilators that restore NO signaling.
- `connects-to` → **[PDGF](../../03-molecular/pdgf/README.md)** — Systemic sclerosis fibrosis is driven by PDGF: the growth factor (and stimulatory anti-PDGFR antibodies) push fibroblasts into collagen-spewing myofibroblasts, so PDGFR-blocking drugs like nintedanib slow the lung scarring.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Systemic sclerosis is fibrosed by M2 macrophages: alternatively-activated macrophages flood the skin and lung and secrete TGF-beta and other signals that drive the relentless collagen deposition central to the disease.
- `connects-to` → **[Mast Cell](../../04-cellular/mast-cell/README.md)** — Mast cells mark early systemic sclerosis: they accumulate in affected skin and release mediators that activate fibroblasts and inflame vessels, contributing to both the fibrosis and the Raynaud's vasculopathy of the disease.
- `connects-to` → **[Large Intestine](../../06-organ/large-intestine/README.md)** — Systemic sclerosis most often strikes inside at the gut: fibrosis and nerve damage slow the intestine, causing reflux, bloating, bacterial overgrowth and malabsorption—the commonest internal-organ involvement of the disease.
- `connects-to` → **[Dendritic Cell](../../04-cellular/dendritic-cell/README.md)** — Plasmacytoid dendritic cells pour out the interferon that drives systemic sclerosis: their type-I interferon signature activates fibroblasts and inflames vessels, sitting near the top of the cascade that scleroderma therapies target.
- `connects-to` → **[Oxygen](../../02-atomic/oxygen/README.md)** — Systemic sclerosis chokes the fingers of oxygen: Raynaud's and a damaged microvasculature cut blood flow, so digital ischemia and ulcers—and tissue hypoxia that feeds more fibrosis—are hallmarks of the vascular side of the disease.
- `connects-to` → **[Hydrogen](../../02-atomic/hydrogen/README.md)** — Scleroderma drowns the esophagus in acid: it weakens the esophageal muscle so reflux floods up, and the hydrogen-ion exposure scars the lining into strictures and Barrett's change.
- `connects-to` → **[Stomach](../../06-organ/stomach/README.md)** — Scleroderma marks the stomach with 'watermelon' stripes: it causes gastric antral vascular ectasia (GAVE), rows of dilated vessels that ooze and cause chronic iron-deficiency anemia.
- `connects-to` → **[Bone Marrow](../../05-tissue/bone-marrow/README.md)** — Severe scleroderma is reset from the bone marrow: autologous hematopoietic stem-cell transplant wipes and rebuilds the immune system, halting the relentless fibrosis in carefully selected patients.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — A beam of light reads scleroderma at the fingertip: nailfold capillaroscopy magnifies the nailbed to reveal the dilated, dropout-riddled capillaries that flag the vasculopathy early, while HRCT photons map the lung fibrosis it causes.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — The limited form often drags in the liver: CREST-pattern scleroderma overlaps strongly with primary biliary cholangitis, so anti-mitochondrial antibodies and a slow autoimmune attack on the bile ducts frequently accompany it.
- `connects-to` → **[Platelet](../../04-cellular/platelet/README.md)** — Platelets stoke scleroderma's vascular fire: activated on the damaged vessel lining, they pour out PDGF and serotonin that drive the smooth-muscle growth and fibrosis narrowing the arteries, feeding the Raynaud's and pulmonary hypertension.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — Scleroderma's autoantibodies predict its course: anti-Scl-70 flags diffuse disease with lung fibrosis, anticentromere the limited CREST form with pulmonary hypertension, and anti-RNA-polymerase-III the dreaded scleroderma renal crisis.
- `connects-to` → **[Small Intestine](../../06-organ/small-intestine/README.md)** — Fibrosis stalls the small bowel: scleroderma replaces gut smooth muscle with scar, so the small intestine loses its propulsion — breeding bacterial overgrowth, malabsorption, and at worst a pseudo-obstruction that mimics a surgical blockage.
- `connects-to` → **[Erythrocyte](../../04-cellular/erythrocyte/README.md)** — Scleroderma bleeds and shears the red cells: the gastric 'watermelon stomach' (GAVE) leaks chronic iron-deficiency anemia, while renal crisis can shred erythrocytes into a microangiopathic hemolytic anemia.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — Scleroderma scars the sexual organs too: erectile dysfunction from vascular and fibrotic damage is common and often early in men, while women face vaginal dryness and tightening, and pregnancy carries added risk of renal crisis.
- `connects-to` → **[Peripheral Nerve](../../05-tissue/peripheral-nerve/README.md)** — The fibrosis can pinch and starve nerves: scleroderma causes trigeminal sensory neuropathy and entrapment syndromes like carpal tunnel, as thickened tissue and a damaged microvasculature injure the peripheral nerves.
- `connects-to` → **[Vitamin D](../../../03-medicine/03-food/vitamin-d/README.md)** — Vitamin D runs low in scleroderma: gut malabsorption, sun avoidance over fragile skin, and the disease itself leave most patients deficient, a shortfall linked to worse skin and lung fibrosis and to the bone loss they accrue.
- `connects-to` → **[Wnt/beta-catenin](../../03-molecular/wnt-beta-catenin/README.md)** — Wnt keeps the fibroblasts switched on: persistent Wnt/beta-catenin signaling drives the fibroblast-to-myofibroblast transition that lays down relentless collagen, a pathway that helps explain why scleroderma's fibrosis self-perpetuates.
- `connects-to` → **[Regulatory T Cell](../../04-cellular/regulatory-t-cell/README.md)** — Broken immune restraint feeds the fibrosis: a shortfall and dysfunction of regulatory T cells lets profibrotic Th2 and Th17 responses run unchecked, tying the autoimmunity of scleroderma to its scarring.
- `connects-to` → **[Thyroid Gland](../../06-organ/thyroid/README.md)** — Scleroderma keeps autoimmune company: autoimmune thyroid disease, both Hashimoto's hypothyroidism and Graves', is over-represented in systemic sclerosis, so thyroid function is part of the routine workup.
- `connects-to` → **[Interleukin-13](../../03-molecular/il-13/README.md)** — Allergy-type cytokines turn fibrotic here: IL-13 with IL-4 from a Th2-skewed response goads fibroblasts into making collagen, an arm of the fibrotic drive alongside TGF-β that is a target for the antifibrotic strategies in scleroderma.
- `connects-to` → **[Cardiomyocyte](../../04-cellular/cardiomyocyte/README.md)** — The heart muscle scars from within: microvascular damage and fibrosis lay down collagen between cardiomyocytes, producing the myocardial fibrosis, conduction problems and heart failure that make cardiac involvement a leading cause of death in scleroderma.
- `connects-to` → **[Chronic Kidney Disease](../ckd/README.md)** — The kidneys can fail abruptly or slowly: scleroderma renal crisis brings sudden hypertensive kidney failure, while chronic vascular injury erodes function over time, leaving chronic kidney disease as a lasting toll of the vasculopathy.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — STAT3 links inflammation to fibrosis: downstream of IL-6, STAT3 activation in fibroblasts and immune cells drives the collagen-producing program, making it a studied node in scleroderma's self-sustaining fibrotic loop.
- `connects-to` → **[Venous Thromboembolism](../venous-thromboembolism/README.md)** — The vasculopathy raises clot risk: systemic sclerosis carries an increased rate of deep-vein thrombosis and pulmonary embolism, layered on top of its hallmark microvascular and pulmonary-arterial disease.
- `connects-to` → **[Sepsis](../sepsis/README.md)** — Skin and lung breaches invite infection: digital ulcers from Raynaud-driven ischemia and aspiration into fibrotic lungs from esophageal dysmotility give scleroderma several routes to serious infection and sepsis.
- `connects-to` → **[Candida albicans](../../../02-pathogen/03-fungi/candida-albicans/README.md)** — Its stiff esophagus is a niche for the yeast: the esophageal dysmotility, acid reflux and chronic PPI use of scleroderma favor Candida esophagitis, adding fungal infection to the swallowing difficulty the fibrosis already causes.
- `connects-to` → **[Heart Failure](../heart-failure/README.md)** — Fibrosis can stiffen the heart itself: myocardial scarring and microvascular disease in scleroderma cause a primary cardiomyopathy, and combined with its pulmonary hypertension this drives both right- and left-sided heart failure.
- `connects-to` → **[Anemia of Chronic Disease](../anemia-of-chronic-disease/README.md)** — Inflammation and gut bleeding lower the count: chronic IL-6-driven inflammation plus blood loss from gastric antral vascular ectasia (watermelon stomach) combine to produce the anemia of chronic disease common in scleroderma.
- `connects-to` → **[Stroke](../stroke/README.md)** — Its vasculopathy reaches the brain's arteries: the obliterative small-vessel disease and accelerated atherosclerosis of systemic sclerosis extend beyond the skin and lungs, raising the long-term risk of ischemic stroke.
- `connects-to` → **[Aspergillus fumigatus](../../../02-pathogen/03-fungi/aspergillus-fumigatus/README.md)** — Its lung disease and immunosuppression invite mold: scleroderma-associated interstitial lung disease, treated with mycophenolate, cyclophosphamide or rituximab, leaves scarred and immune-suppressed lungs vulnerable to invasive aspergillosis.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — A disfiguring, progressive disease wears on mood: the visible skin tightening, disability, pain and poor prognosis of systemic sclerosis substantially impair quality of life and carry high rates of depression.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — The skin is its defining organ: systemic sclerosis hardens and thickens the skin through excess collagen, with sclerodactyly, calcinosis, telangiectasia and Raynaud's, the visible hallmark of the disease.
- `connects-to` → **[Wound Healing](../wound-healing/README.md)** — Fibrosis and ischaemia cripple healing: the Raynaud's and microvascular damage of systemic sclerosis cause painful digital ulcers over the fingertips that are notoriously slow to heal and can gangrene.
- `connects-to` → **[Generalized Anxiety Disorder](../generalized-anxiety-disorder/README.md)** — A progressive, disfiguring multi-organ disease breeds worry: the relentless skin and organ involvement, painful ulcers and uncertain prognosis of systemic sclerosis foster chronic health anxiety alongside depression.
- `connects-to` → **[Respiratory System](../respiratory-system/README.md)** — It scars the lungs: interstitial lung disease from progressive pulmonary fibrosis is the leading cause of death in systemic sclerosis, alongside the pulmonary hypertension it also drives.
- `connects-to` → **[Renal System](../renal-system/README.md)** — It can strike the kidneys abruptly: scleroderma renal crisis brings malignant hypertension and acute kidney injury, a once-fatal emergency now treated with ACE inhibitors.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — Fibrosis stiffens joints and deposits calcium: systemic sclerosis causes joint contractures, tendon friction rubs, calcinosis of the soft tissues and an inflammatory myopathy.
- `connects-to` → **[Cardiovascular System](../cardiovascular-system/README.md)** — It spasms the small vessels and scars the heart: Raynaud's phenomenon — episodic digital vasospasm — is an almost universal early feature, and myocardial fibrosis causes arrhythmia and heart failure.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — It has a signature nerve sign: trigeminal neuralgia is a characteristic neurological association of systemic sclerosis, alongside carpal tunnel syndrome and autonomic and peripheral neuropathy.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — It clusters with thyroid disease: autoimmune hypothyroidism is a common association, and fibrosis of the thyroid gland can further impair its function.
- `connects-to` → **[ACE inhibitors](../../../03-medicine/01-modern/04-cardio/ace-inhibitors/README.md)** — They are life-saving in renal crisis: ACE inhibitors are the treatment for scleroderma renal crisis, the malignant hypertension and acute kidney injury that once made it fatal.
- `connects-to` → **[Calcium-channel Blockers](../../../03-medicine/01-modern/04-cardio/calcium-channel-blockers/README.md)** — They ease the cold fingers: calcium-channel blockers like nifedipine are first-line for the Raynaud's phenomenon that nearly always accompanies systemic sclerosis.
- `connects-to` → **[Corticosteroids](../../../03-medicine/01-modern/02-respiratory/corticosteroids/README.md)** — Steroids must be used with caution: high-dose corticosteroids can precipitate scleroderma renal crisis, so they are limited despite the inflammation of early diffuse systemic sclerosis.
- `connects-to` → **[Cancer Chemotherapy](../../../03-medicine/01-modern/13-cancer/cancer-chemotherapy/README.md)** — Cyclophosphamide and transplant for severe disease: cyclophosphamide is used for progressive scleroderma lung and skin fibrosis, and autologous haematopoietic stem-cell transplant can halt rapidly diffuse disease by resetting the autoimmune system.
- `connects-to` → **[Targeted Therapy](../../../03-medicine/01-modern/13-cancer/targeted-therapy/README.md)** — Antifibrotics and cytokine blockade: nintedanib, an anti-fibrotic multikinase inhibitor, slows scleroderma-associated interstitial lung disease, while tocilizumab against IL-6 and rituximab against B cells temper the fibrosing inflammation.
- `connects-to` → **[Arterial Wall](../../05-tissue/arterial-wall/README.md)** — A vasculopathy as much as a fibrosis: systemic sclerosis remodels small arteries with intimal proliferation and luminal narrowing — the onion-skin lesions of scleroderma renal crisis and the digital-artery disease behind Raynaud's and digital ulcers.
- `connects-to` → **[Myocardium](../../05-tissue/myocardium/README.md)** — It silently scars the heart muscle: systemic sclerosis lays down primary myocardial fibrosis and microvascular ischaemia that cause arrhythmias, conduction block and heart failure—often clinically silent until advanced, and a leading cause of death.
- `connects-to` → **[Glomerulus](../../05-tissue/glomerulus/README.md)** — Scleroderma renal crisis starves the filter: renin-driven malignant hypertension and arteriolar thrombotic microangiopathy cut blood flow to the glomeruli, causing acute kidney injury that prompt ACE inhibition can reverse.
- `connects-to` → **[Thrombotic Thrombocytopenic Purpura](../thrombotic-thrombocytopenic-purpura/README.md)** — A thrombotic microangiopathy of its own: scleroderma renal crisis produces microangiopathic haemolysis and thrombocytopenia that mimic thrombotic thrombocytopenic purpura, but with normal ADAMTS13—a key distinction in the TMA differential.
- `connects-to` → **[Alveolus](../../05-tissue/alveolus/README.md)** — The leading cause of death: SSc-associated interstitial lung disease scars the alveolar walls into a stiff, fibrotic lung, and progressive fibrosis here now kills more scleroderma patients than renal crisis.
- `connects-to` → **[Cortical Bone](../../05-tissue/cortical-bone/README.md)** — Bone and soft-tissue destruction: SSc causes acro-osteolysis—resorption of the distal phalangeal cortical bone—alongside subcutaneous calcinosis, deforming the fingertips.
- `connects-to` → **[GVHD](../gvhd/README.md)** — A fibrosis it imitates: chronic sclerodermatous graft-versus-host disease reproduces SSc's skin tightening and fibrosis, showing how alloimmune and autoimmune injury converge on the same fibrotic endpoint.
- `connects-to` → **[Esophageal Cancer](../esophageal-cancer/README.md)** — Reflux to malignancy: severe oesophageal dysmotility and chronic acid reflux in systemic sclerosis drive Barrett's metaplasia, raising the long-term risk of oesophageal adenocarcinoma.
- `connects-to` → **[Breast Cancer](../breast-cancer/README.md)** — Cancer-triggered autoimmunity: anti-RNA-polymerase-III-positive systemic sclerosis is associated with a synchronous cancer, often breast or lung, within a few years—a paraneoplastic scleroderma where the tumour appears to spark the disease.
- `connects-to` → **[Cardiac Conduction System](../../05-tissue/cardiac-conduction-system/README.md)** — Fibrosis hits the wiring: patchy myocardial fibrosis in systemic sclerosis scars the cardiac conduction system, causing heart block and ventricular arrhythmias that are a leading cause of sudden death in the disease.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — Disordered angiogenesis: dysregulated VEGF underlies the vasculopathy of systemic sclerosis—capillary dropout and dilated telangiectasias reflecting failed, abnormal new-vessel growth.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — Th2 profibrotic axis: IL-4, with IL-13, drives the Th2-skewed immune response that activates fibroblasts and lays down the excess collagen of systemic sclerosis.
- `connects-to` → **[ANCA Vasculitis](../anca-vasculitis/README.md)** — Scleroderma-ANCA overlap: a subset of systemic sclerosis patients are MPO-ANCA positive and develop an overlapping ANCA-associated vasculitis with glomerulonephritis, distinct from scleroderma renal crisis.
- `connects-to` → **[CCL2](../../03-molecular/ccl2/README.md)** — Monocyte recruitment: CCL2 draws monocytes and profibrotic macrophages into the skin and lung of systemic sclerosis, fuelling the inflammation that precedes fibrosis.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — Th17 fibrosis: IL-17 from Th17 cells contributes to the inflammatory and profibrotic response of systemic sclerosis, modulating fibroblast activation.
- `connects-to` → **[HIF-1α](../../03-molecular/hif-1alpha/README.md)** — Vascular hypoxia: the obliterative vasculopathy of systemic sclerosis creates tissue hypoxia that stabilises HIF-1α, paradoxically failing to restore perfusion while driving fibrosis.
- `connects-to` → **[CD20](../../03-molecular/cd20/README.md)** — Rituximab targets CD20+ B cells in systemic sclerosis, reducing skin and lung fibrosis—evidence that autoreactive B cells and their autoantibodies (anti-Scl70, anti-RNA-pol III), not just activated fibroblasts, drive the disease.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — The interferon and IL-6 signatures of systemic sclerosis act through JAK-STAT, making JAK1/2 inhibitors such as tofacitinib a candidate to dampen both the inflammatory and the profibrotic arms of the disease at once.
- `connects-to` → **[Serotonin](../../03-molecular/serotonin/README.md)** — Platelet-derived serotonin acting on 5-HT2B receptors stimulates dermal fibroblasts to produce collagen and contributes to the vasoconstriction of Raynaud's phenomenon—linking the platelet activation of SSc vasculopathy directly to its fibrosis.
- `connects-to` → **[Periostin](../../03-molecular/periostin/README.md)** — Periostin is upregulated in the skin and lung of systemic sclerosis, where this matricellular protein crosslinks collagen and amplifies TGF-β-driven fibroblast activation, and serum periostin tracks the extent of fibrosis.
- `connects-to` → **[Angiopoietin](../../03-molecular/angiopoietin/README.md)** — An imbalance of angiopoietin-Tie2 signaling destabilizes the microvasculature of systemic sclerosis, contributing to the capillary loss, digital ulcers and pulmonary arterial hypertension that mark its obliterative vasculopathy.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — IL-33 released from damaged endothelium and epithelium in systemic sclerosis activates type-2 innate lymphoid cells and amplifies the IL-13/IL-4 axis, driving the Th2-skewed fibrotic response in skin and lung.
- `connects-to` → **[SMAD4](../../03-molecular/smad4/README.md)** — TGF-β signals through the SMAD pathway (common mediator SMAD4) to drive the fibroblast activation and excess collagen deposition central to systemic sclerosis, the core fibrotic mechanism of the disease.
- `connects-to` → **[PF4](../../03-molecular/pf4/README.md)** — CXCL4/platelet factor 4, released by plasmacytoid dendritic cells, is a leading systemic-sclerosis biomarker that drives the type-I interferon response and fibrosis, linking platelet and innate-immune activation to the disease.
- `connects-to` → **[BAFF](../../03-molecular/baff/README.md)** — BAFF-driven B-cell survival and autoantibody production contribute to systemic sclerosis, the rationale for the B-cell-depleting therapy (rituximab against the CD20 already mapped) used in skin and lung disease.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — PDGFR and FGFR signaling (PDGF mapped) drives the MAPK-ERK cascade that activates fibroblasts in systemic sclerosis, the axis blocked by the antifibrotic TKI nintedanib.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — mTOR signaling promotes the differentiation of fibroblasts into collagen-secreting myofibroblasts (collagen mapped), driving the progressive fibrosis of systemic sclerosis.
- `connects-to` → **[MYD88](../../03-molecular/myd88/README.md)** — Endogenous DAMPs activate TLR4 on fibroblasts, signaling through MyD88 to sustain TGF-β-driven (mapped) collagen production and the persistent fibrosis of systemic sclerosis.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — NF-κB-driven inflammatory transcription amplifies the cytokine production and fibroblast activation that perpetuate the inflammation-fibrosis loop of systemic sclerosis.
- `connects-to` → **[NRF2](../../03-molecular/nfe2l2/README.md)** — NRF2 antioxidant defense counters the oxidative stress driving the endothelial injury and fibroblast activation central to the vasculopathy and fibrosis of systemic sclerosis.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — PI3K-AKT signaling promotes the activation, survival and matrix production of the myofibroblasts (alongside TGF-β/SMAD already mapped) that drive the fibrosis of systemic sclerosis.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Galectin-3 is a key profibrotic mediator and biomarker driving the skin and lung fibrosis of systemic sclerosis.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — Type-I-interferon signaling through STAT1 (type-I-interferon mapped) underlies the interferon signature characteristic of systemic sclerosis.
- `connects-to` → **[PTEN](../../03-molecular/pten/README.md)** — Loss of PTEN in systemic-sclerosis fibroblasts releases the PI3K-AKT-mTOR signaling (AKT and mTOR mapped) that drives myofibroblast activation and fibrosis.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — Cytosolic DNA sensing through cGAS-STING drives the type-I-interferon signature (type-I interferon already mapped) central to the autoimmunity of systemic sclerosis.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — FOXO transcription factors modulate the oxidative-stress and survival balance of the activated myofibroblasts that drive the fibrosis of systemic sclerosis.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β signaling regulates the fibroblast-to-myofibroblast transition and the persistent fibrosis of systemic sclerosis.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — S100A8/A9 alarmins amplify the innate inflammation driving the fibrosis of systemic sclerosis.
- `connects-to` → **[Perforin](../../03-molecular/perforin/README.md)** — Perforin-mediated cytotoxicity contributes to the endothelial injury underlying the vasculopathy of systemic sclerosis.
- `connects-to` → **[CDK4/6](../../03-molecular/cdk4-6/README.md)** — CDK4/6-driven proliferation of myofibroblasts contributes to the fibrotic tissue expansion of systemic sclerosis.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — PI3K (PIK3CA)-AKT signaling (AKT already mapped) drives the fibroblast activation and myofibroblast differentiation of systemic sclerosis.
- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — SRC-family kinase signaling downstream of PDGFR (PDGF already mapped) drives the fibroblast activation and fibrosis of systemic sclerosis.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — Autophagy modulates the myofibroblast differentiation and fibrotic responses of systemic sclerosis.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK-linked metabolic signaling participates in the myofibroblast and immune-cell metabolism of systemic sclerosis.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-driven leukocyte recruitment contributes to the inflammatory and fibrotic tissue infiltration of systemic sclerosis.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — DNMT3A-mediated DNA methylation participates in the epigenetic dysregulation of the fibroblast and immune-cell responses of systemic sclerosis.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — CXCL12-CXCR4 signaling participates in the vasculopathy and fibrotic-cell recruitment of systemic sclerosis.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — IL-1β-driven inflammation participates in the inflammatory and fibrotic processes of systemic sclerosis.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Complement C3 participates in the vascular injury and immune activation of systemic sclerosis.
- `connects-to` → **[Immunoglobulin G](../../03-molecular/immunoglobulin-g/README.md)** — Autoantibody serology: systemic sclerosis is defined serologically by IgG autoantibodies, anti-topoisomerase-1 (Scl-70), anti-centromere and anti-RNA-polymerase-III, that stratify the risk of diffuse skin, lung fibrosis and renal crisis.
- `connects-to` → **[Prostaglandins](../../03-molecular/prostaglandins/README.md)** — Vascular therapy: prostacyclin, a prostaglandin, and its analogues such as iloprost dilate vessels and inhibit platelets to treat the digital ischaemia, ulcers and pulmonary hypertension of the systemic-sclerosis vasculopathy.
- `connects-to` → **[BNP](../../03-molecular/bnp/README.md)** — Pulmonary hypertension screening: systemic sclerosis is a leading cause of connective-tissue-disease pulmonary arterial hypertension, and BNP/NT-proBNP release from the strained right ventricle guides the annual screening that detects this lethal complication.
- `connects-to` → **[Hemoglobin](../../03-molecular/hemoglobin/README.md)** — Gut bleeding and haemolysis: gastric antral vascular ectasia (watermelon stomach) causes chronic gastrointestinal bleeding in systemic sclerosis, and scleroderma renal crisis brings microangiopathic haemolysis, both lowering haemoglobin.
- `connects-to` → **[Troponin complex](../../03-molecular/troponin-complex/README.md)** — Myocardial fibrosis: systemic sclerosis can directly fibrose the myocardium and conduction system, and troponin elevation marks the primary cardiac involvement that, alongside pulmonary hypertension (BNP already mapped), contributes to its mortality.
- `connects-to` → **[MHC class II](../../03-molecular/mhc-class-ii/README.md)** — HLA and autoantibodies: specific HLA class II alleles determine which autoantibody a patient develops (anti-topoisomerase, anti-centromere or anti-RNA-polymerase III), and MHC class II antigen presentation drives the autoimmunity of systemic sclerosis.
- `connects-to` → **[ADAMTS13](../../03-molecular/adamts13/README.md)** — Renal-crisis microangiopathy: scleroderma renal crisis causes a thrombotic microangiopathy with normal ADAMTS13 (unlike thrombotic thrombocytopenic purpura), the endothelial injury driving the haemolysis and acute kidney failure.
- `connects-to` → **[Xanthine oxidase](../../03-molecular/xanthine-oxidase/README.md)** — Oxidative fibrosis: reactive oxygen species, to which xanthine oxidase contributes, are generated in the hypoxic, inflamed tissues of systemic sclerosis, and this oxidative stress (NRF2 already mapped) helps drive the endothelial injury and fibroblast activation.
- `connects-to` → **[IL-10](../../03-molecular/il-10/README.md)** — Immunoregulatory balance: the anti-inflammatory IL-10 counters the profibrotic type-2 and type-17 responses (IL-4, IL-13 and IL-17 already mapped), and the imbalance between them shapes the autoimmunity and fibrosis of systemic sclerosis.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Anaemia and GI bleeding: the chronic inflammation and the gastric antral vascular ectasia (watermelon stomach) of systemic sclerosis cause anaemia (haemoglobin already mapped) from iron loss and sequestration, a common systemic complication.
- `connects-to` → **[Histamine](../../03-molecular/histamine/README.md)** — Mast-cell involvement: mast cells release histamine in the early inflammatory, pruritic phase of the skin (already mapped) fibrosis of systemic sclerosis, contributing to the itch and the fibroblast-activating (already mapped) inflammation.
- `connects-to` → **[Renin](../../03-molecular/renin/README.md)** — Scleroderma renal crisis: the renin-angiotensin system (angiotensin II already mapped) is dramatically activated in scleroderma renal crisis, and ACE inhibitors blocking it transformed this once-fatal complication of systemic sclerosis.
- `connects-to` → **[Hepcidin](../../03-molecular/hepcidin/README.md)** — Anaemia of chronic disease: the IL-6-driven (already mapped) hepcidin sequesters iron (already mapped) to produce the anaemia of chronic disease that, with the GAVE blood loss, causes the anaemia of systemic sclerosis.
- `connects-to` → **[Von Willebrand factor](../../03-molecular/von-willebrand-factor/README.md)** — Endothelial injury marker: the endothelial injury of the vasculopathy (endothelin-1 already mapped) raises von Willebrand factor, a marker of the endothelial activation that drives the Raynaud's and vascular disease of systemic sclerosis.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — Anti-fibrotic adipokine: adiponectin is an anti-fibrotic adipokine, and its fall as the dermal adipose is lost to fibrosis removes a brake on the fibroblast (already mapped) activation, promoting the fibrosis of systemic sclerosis.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Pro-fibrotic adipokine: leptin, opposite to the anti-fibrotic adiponectin (already mapped), is a pro-fibrotic adipokine that promotes the fibroblast (already mapped) activation and the fibrosis of systemic sclerosis.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Adipose-inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), is the adipose-inflammatory adipokine of the immune-metabolic milieu of systemic sclerosis.
- `connects-to` → **[Zinc](../../02-atomic/zinc/README.md)** — Wound-healing zinc: the disturbed zinc homeostasis and the impaired wound healing of the fibrotic, ulcer-prone (digital ulcers) skin (already mapped) of systemic sclerosis.
- `connects-to` → **[Plasma cell](../../04-cellular/plasma-cell/README.md)** — Autoantibody plasma cells: the plasma cells (from the B cells — CD20 and BAFF already mapped) secrete the anti-Scl-70/centromere autoantibodies (immunoglobulin already mapped) of systemic sclerosis.
- `connects-to` → **[IFN-gamma](../../03-molecular/ifn-gamma/README.md)** — Th1 arm: the IFN-γ of the T cells (with the type-I interferon already mapped) is the type-II interferon arm of the immune dysregulation of systemic sclerosis.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm balancing the Th2 (IL-4 and IL-13 already mapped) profibrotic drive of systemic sclerosis.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Type-2 profibrotic arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the profibrotic immune drive of systemic sclerosis.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the inflammatory-fibrotic dimension of systemic sclerosis.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the profibrotic autoimmunity of systemic sclerosis.
- `connects-to` → **[TSLP](../../03-molecular/tslp/README.md)** — Profibrotic alarmin: TSLP, an epithelial alarmin, initiates and amplifies the type-2 (IL-4 and IL-13 already mapped) immunity that drives the fibroblast (already mapped) activation and periostin (already mapped) remodelling of systemic sclerosis.
- `connects-to` → **[C5aR1](../../03-molecular/c5ar1/README.md)** — Complement C5a receptor: the C5aR1 signalling (with the complement C3 already mapped) contributes to the microvascular injury and the inflammatory dimension of the vasculopathy of systemic sclerosis.
- `connects-to` → **[IL-31](../../03-molecular/il-31/README.md)** — Pruritus cytokine: IL-31, a type-2 (IL-4 and IL-13 already mapped) cytokine, is the pruritogenic effector of the frequent and burdensome itch of the sclerotic skin of systemic sclerosis.
- `connects-to` → **[Complement C5](../../03-molecular/complement-c5/README.md)** — Terminal complement: the complement C5 and its activation (with C3 and C5aR1 already mapped) contribute to the microvascular injury and the inflammatory vasculopathy of systemic sclerosis.
- `connects-to` → **[Factor H](../../03-molecular/factor-h/README.md)** — Complement regulation: factor H regulates the alternative complement pathway (complement C3, C5 and C5aR1 already mapped) whose dysregulation contributes to the endothelial (already mapped) injury of systemic sclerosis.
- `connects-to` → **[Cytotoxic T cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Cytotoxic infiltrate: the cytotoxic T cells (perforin already mapped) infiltrate the sclerotic skin and lung and contribute to the endothelial injury and the fibroblast (already mapped) activation of systemic sclerosis.
- `connects-to` → **[Bradykinin](../../03-molecular/bradykinin/README.md)** — Vasomotor mediator: bradykinin, released by kallikrein activation in the ischaemia-reperfusion cycles of Raynaud's phenomenon, amplifies the vascular permeability and digital pain that accompany the microvascular disease of systemic sclerosis.
- `connects-to` → **[C1-Esterase Inhibitor](../../03-molecular/c1-esterase-inhibitor/README.md)** — Classical complement brake: C1-esterase inhibitor modulates the classical complement pathway (C3, C5 and C5aR1 already mapped) activated by the anti-endothelial autoantibodies on the sclerotic vascular wall of systemic sclerosis.
- `connects-to` → **[Erythropoietin](../../03-molecular/erythropoietin/README.md)** — Scleroderma anaemia: erythropoietin addresses the anaemia of chronic inflammation and the renal-crisis-driven erythropoietin deficiency of systemic sclerosis; EPO may also modulate the pulmonary-artery vascular remodelling (PAH already mapped).
- `connects-to` → **[Melatonin](../../03-molecular/melatonin/README.md)** — Circadian antifibrotic: melatonin is reduced in systemic sclerosis and exerts antifibrotic effects by suppressing TGF-β (already mapped) signalling and fibroblast (already mapped) collagen production, while modulating the Th1/Th2 imbalance.
- `connects-to` → **[Prolactin](../../03-molecular/prolactin/README.md)** — Profibrotic autoimmune amplifier: prolactin is elevated in a subset of systemic sclerosis patients and modulates the B-cell (BAFF already mapped) and T-cell autoimmunity driving the fibrosis and endothelial injury of the disease.
- `connects-to` → **[Oxytocin](../../03-molecular/oxytocin/README.md)** — Vascular neuromodulator: oxytocin receptors on endothelial and smooth-muscle cells (already mapped) modulate vascular tone; oxytocin deficiency may contribute to the Raynaud's vasospasm and the endothelial dysfunction of systemic sclerosis.
- `connects-to` → **[Testosterone](../../03-molecular/testosterone/README.md)** — SSc testosterone: testosterone exerts anti-fibrotic effects in systemic sclerosis; androgen deficiency contributes to the female sex predominance, and androgen-receptor signalling on fibroblasts (already mapped) modulates TGF-β (already mapped)-driven collagen deposition.
- `connects-to` → **[Vasopressin](../../03-molecular/vasopressin/README.md)** — SSc vasopressin: vasopressin (ADH) modulates renal water retention (kidney already mapped) and vascular tone in systemic sclerosis; in scleroderma renal crisis, AVP-mediated vasoconstriction amplifies the angiotensin-II (already mapped)-driven hypertensive emergency.
- `connects-to` → **[Selenium](../../02-atomic/selenium/README.md)** — SSc selenium: selenium selenoproteins counter the oxidative stress driving endothelial injury and fibroblast (already mapped) activation in systemic sclerosis; selenium deficiency amplifies NF-κB (already mapped) inflammation and worsens the pulmonary fibrosis of the disease.
- `connects-to` → **[Iodine](../../02-atomic/iodine/README.md)** — SSc iodine: iodine-dependent thyroid hormones modulate fibroblast (already mapped) and TGF-β (already mapped)-driven collagen deposition in systemic sclerosis; autoimmune thyroid disease (Hashimoto thyroiditis) coexists in SSc and amplifies fibrotic and vascular manifestations.
- `connects-to` → **[Sodium](../../02-atomic/sodium/README.md)** — SSc sodium: sodium-driven osmotic Th17 polarisation amplifies NF-κB (already mapped) and IL-17A (already mapped)-mediated vascular and fibroblast (already mapped) activation in systemic sclerosis; high dietary sodium worsens inflammatory and fibrotic phases of scleroderma.
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — SSc magnesium: magnesium deficiency amplifies NF-κB (already mapped) and TGF-β (already mapped)-driven fibroblast (already mapped) activation in systemic sclerosis; magnesium-dependent enzymes regulate collagen cross-linking and fibrotic remodelling of scleroderma.
- `connects-to` → **[Copper](../../02-atomic/copper/README.md)** — SSc copper: copper, as lysyl oxidase cofactor in fibroblasts (already mapped), drives collagen cross-linking; copper amplifies VEGF (already mapped); copper excess amplifies TGF-β (already mapped) and NF-κB (already mapped) cascade of systemic sclerosis.
- `connects-to` → **[Potassium](../../02-atomic/potassium/README.md)** — SSc potassium: potassium efflux via NLRP3 inflammasome in macrophages (already mapped) and mast-cell (already mapped) drives IL-6 (already mapped) secretion; potassium dysregulation amplifies TGF-β (already mapped) and NF-κB (already mapped) cascade of SSc.
- `connects-to` → **[Phosphorus](../../02-atomic/phosphorus/README.md)** — SSc phosphorus: phosphorus, as ATP precursor in fibroblasts (already mapped) and endothelial-cell (already mapped), fuels TGF-β (already mapped) collagen synthesis; phosphorus deficiency impairs dendritic-cell (already mapped) and amplifies NF-κB (already mapped) cascade of SSc.
- `connects-to` → **[Chloride](../../02-atomic/chloride/README.md)** — SSc chloride: chloride channels in fibroblasts (already mapped) and endothelial-cell (already mapped) regulate stromal fluid balance; chloride dysregulation amplifies TGF-β (already mapped) and NF-κB (already mapped) fibrotic cascade and worsens pulmonary hypertension of SSc.
- `connects-to` → **[Sulfur](../../02-atomic/sulfur/README.md)** — SSc sulfur: hydrogen sulfide from endothelial-cell (already mapped) and fibroblasts (already mapped) promotes vasodilation; sulfur deficiency amplifies TGF-β (already mapped) and NF-κB (already mapped) fibrotic cascade and worsens pulmonary vascular remodelling of SSc.
- `connects-to` → **[Nitrogen](../../02-atomic/nitrogen/README.md)** — SSc nitrogen: nitric oxide from endothelial-cell (already mapped) and macrophages (already mapped) maintains vascular tone; nitrogen imbalance amplifies TGF-β (already mapped) and NF-κB (already mapped) fibrotic cascade and pulmonary hypertension of SSc.
- `connects-to` → **[Carbon](../../02-atomic/carbon/README.md)** — SSc carbon: carbon, as metabolic backbone of TGF-β (already mapped) and NF-κB (already mapped) in fibroblasts (already mapped) and endothelial-cell (already mapped), drives fibrotic signalling; carbon dysregulation amplifies IL-6 (already mapped) cascade of SSc.
- `connects-to` → **[PD-1](../../03-molecular/pd-1/README.md)** — SSc PD-1: PD-1 checkpoint on T-cytotoxic cells (already mapped) and macrophages (already mapped) modulates autoimmune surveillance of fibroblasts (already mapped); PD-1 dysregulation amplifies TGF-β (already mapped) and IL-6 (already mapped) fibrotic cascade of SSc.
- `connects-to` → **[GLP-1](../../03-molecular/glp-1/README.md)** — SSc GLP-1: GLP-1 signalling in endothelial-cell (already mapped) and macrophages (already mapped) modulates metabolic-immune homeostasis; GLP-1 dysregulation amplifies TGF-β (already mapped) and NF-κB (already mapped) and IL-6 (already mapped) cascade of SSc.
- `connects-to` → **[RANKL](../../03-molecular/rankl/README.md)** — SSc RANKL: RANKL signalling in macrophages (already mapped) and fibroblasts (already mapped) modulates bone-immune axis; RANKL excess amplifies NF-κB (already mapped) and angiotensin-II (already mapped) and IL-6 (already mapped) fibrotic cascade of systemic sclerosis.
- `connects-to` → **[IL-2](../../03-molecular/il-2/README.md)** — SSc IL-2: IL-2 signalling in T-cells (already mapped) and fibroblasts (already mapped) modulates immune homeostasis; IL-2 deficiency amplifies NF-κB (already mapped) and angiotensin-II (already mapped) and IL-6 (already mapped) fibrotic cascade of systemic sclerosis.
- `connects-to` → **[Fibronectin](../../03-molecular/fibronectin/README.md)** — SSc fibronectin: fibronectin in fibroblasts (already mapped) and macrophages (already mapped) promotes ECM accumulation; fibronectin excess amplifies NF-κB (already mapped) and angiotensin-II (already mapped) and IL-6 (already mapped) fibrotic cascade of systemic sclerosis.
- `connects-to` → **[NOTCH](../../03-molecular/notch/README.md)** — SSc notch: NOTCH on fibroblasts (already mapped) and macrophages (already mapped) regulates dermal fibrotic remodelling; notch dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and TGF-β (already mapped) fibrotic cascade of systemic sclerosis.
- `connects-to` → **[IGF-1](../../03-molecular/igf-1/README.md)** — SSc igf-1: IGF-1 from fibroblasts (already mapped) and macrophages (already mapped) promotes dermal fibroblast proliferation; igf-1 excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and TGF-β (already mapped) fibrotic cascade of systemic sclerosis.
- `connects-to` → **[Activin-A](../../03-molecular/activin-a/README.md)** — SSc activin-a: activin-A from fibroblasts (already mapped) and macrophages (already mapped) regulates fibrotic ECM remodelling; activin-a excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and TGF-β (already mapped) fibrotic cascade of systemic sclerosis.
- `connects-to` → **[CGRP](../../03-molecular/cgrp/README.md)** — SSc cgrp: CGRP from macrophages (already mapped) and fibroblasts (already mapped) modulates SSc vascular tone; cgrp excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and TGF-β (already mapped) fibrotic cascade of systemic sclerosis.
- `connects-to` → **[Calcitonin](../../03-molecular/calcitonin/README.md)** — SSc calcitonin: calcitonin from macrophages (already mapped) and fibroblasts (already mapped) modulates SSc calcium balance; calcitonin dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and TGF-β (already mapped) fibrotic cascade of systemic sclerosis.
- `connects-to` → **[Substance-P](../../03-molecular/substance-p/README.md)** — SSc substance-p: substance-P from macrophages (already mapped) and fibroblasts (already mapped) modulates SSc neuroimmune tone; substance-p excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and TGF-β (already mapped) fibrotic cascade of systemic sclerosis.
- `connects-to` → **[Insulin-Receptor](../../03-molecular/insulin-receptor/README.md)** — SSc insulin-receptor: insulin receptor on macrophages (already mapped) and fibroblasts (already mapped) modulates SSc metabolic fibrosis; insulin-receptor loss amplifies NF-κB (already mapped) and IL-6 (already mapped) and TGF-β (already mapped) fibrotic cascade of SSc.
- `connects-to` → **[Aldosterone](../../03-molecular/aldosterone/README.md)** — SSc aldosterone: aldosterone from macrophages (already mapped) and fibroblasts (already mapped) amplifies SSc salt-fluid fibrosis; aldosterone excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and TGF-β (already mapped) fibrotic cascade of SSc.
- `connects-to` → **[Androgen-Receptor](../../03-molecular/androgen-receptor/README.md)** — SSc androgen-receptor: androgen receptor on macrophages (already mapped) and fibroblasts (already mapped) modulates SSc hormonal fibrosis; androgen-receptor loss amplifies NF-κB (already mapped) and IL-6 (already mapped) and TGF-β (already mapped) fibrotic cascade of SSc.
- `connects-to` → **[Norepinephrine](../../03-molecular/norepinephrine/README.md)** — SSc norepinephrine: norepinephrine from macrophages (already mapped) and fibroblasts (already mapped) modulates SSc adrenergic vascular tone; norepinephrine excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and TGF-β (already mapped) fibrotic cascade of SSc.
- `connects-to` → **[Adrenomedullin](../../03-molecular/adrenomedullin/README.md)** — SSc adrenomedullin: adrenomedullin from macrophages (already mapped) and fibroblasts (already mapped) modulates SSc vascular tone; adrenomedullin excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and TGF-β (already mapped) fibrotic cascade of SSc.
- `connects-to` → **[BDNF](../../03-molecular/bdnf/README.md)** — SSc bdnf: BDNF from macrophages (already mapped) and fibroblasts (already mapped) modulates SSc neuroimmune fibrotic tone; bdnf loss amplifies NF-κB (already mapped) and IL-6 (already mapped) and TGF-β (already mapped) fibrotic cascade of SSc.

[^denton-2017-ssc-review]: Denton CP, Khanna D. Systemic sclerosis. *Lancet.* 2017;390(10103):1685-1699. [doi:10.1016/S0140-6736(17)30933-9](https://doi.org/10.1016/S0140-6736(17)30933-9) · [PubMed 28413064](https://pubmed.ncbi.nlm.nih.gov/28413064/)
[^distler-2019-nintedanib-senscis]: Distler O, Highland KB, Gahlemann M, et al. Nintedanib for Systemic Sclerosis-Associated Interstitial Lung Disease. *N Engl J Med.* 2019;380(26):2518-2528. [doi:10.1056/NEJMoa1903076](https://doi.org/10.1056/NEJMoa1903076) · [PubMed 31112379](https://pubmed.ncbi.nlm.nih.gov/31112379/)
[^khanna-2016-tocilizumab-ssc]: Khanna D, Denton CP, Jahreis A, et al. Safety and efficacy of subcutaneous tocilizumab in adults with systemic sclerosis (faSScinate): a phase 2, randomised, controlled trial. *Lancet.* 2016;387(10038):2630-2640. [doi:10.1016/S0140-6736(16)00932-X](https://doi.org/10.1016/S0140-6736(16)00932-X) · [PubMed 27156007](https://pubmed.ncbi.nlm.nih.gov/27156007/)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
