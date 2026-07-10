---
schema: human-scale-entry/v1
id: gut-microbiome
name: Gut Microbiome
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-06
summary: "~10¹³ microorganisms (Firmicutes, Bacteroidetes, Actinobacteria) colonizing the GI tract. Functions: SCFA production (butyrate, propionate), vitamin synthesis, colonization resistance, immune education, bile acid metabolism, gut-brain axis serotonin."
aliases: ["gut microbiome", "gut microbiota", "intestinal microbiome", "gut flora", "microbiota", "human microbiome"]
sources:
  - id: sender-2016-microbiome-census
    type: peer-reviewed
    cite: "Sender R, Fuchs S, Milo R. Revised Estimates for the Number of Human and Bacteria Cells in the Body. Cell. 2016;164(3):337-340."
    doi: "10.1016/j.cell.2016.01.013"
    pmid: "26824647"
    url: "https://doi.org/10.1016/j.cell.2016.01.013"
  - id: turnbaugh-2006-microbiome-nature
    type: peer-reviewed
    cite: "Turnbaugh PJ, Ley RE, Mahowald MA, Magrini V, Mardis ER, Gordon JI. An obesity-associated gut microbiome with increased capacity for energy harvest. Nature. 2006;444(7122):1027-1031."
    doi: "10.1038/nature05414"
    pmid: "17183312"
    url: "https://doi.org/10.1038/nature05414"
cross_links:
  - target: 01-human/07-system/immune-system
    relation: modulates
    note: "The gut microbiome is the primary educator of the mucosal and systemic immune system: drives IgA production, Treg induction, colonization resistance, and patterns innate immune responses; dysbiosis leads to immune dysregulation and susceptibility to inflammatory diseases."
  - target: 02-pathogen/06-microbiome/bacteroides-fragilis
    relation: contains
    note: "Bacteroides fragilis (non-toxigenic strains) is a key Bacteroidetes member; polysaccharide A (PSA) drives Treg induction and IL-10 production; ETBF toxin disrupts epithelial barrier and promotes dysbiosis."
  - target: 02-pathogen/06-microbiome/akkermansia-muciniphila
    relation: contains
    note: "Akkermansia muciniphila is a mucin-degrading Verrucomicrobia member of the gut microbiome associated with metabolic health; reduced in obesity and T2DM; its Amuc_1100 outer membrane protein activates TLR2, improving gut barrier integrity and insulin sensitivity."
  - target: 01-human/07-system/obesity
    relation: connects-to
    note: "Dysbiosis in obesity — increased Firmicutes/Bacteroidetes, reduced Akkermansia muciniphila — increases energy harvest and drives metabolic endotoxemia (LPS → TLR4 → systemic inflammation); gut microbiome transfer from obese to germ-free mice transfers the adiposity phenotype."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Microbiome dysbiosis → LPS → TLR4 → TNF-α/IL-6 → adiponectin suppression; butyrate-producing bacteria (Akkermansia, Bifidobacterium) → SCFA → PPARγ → ADIPOQ induction; probiotics and prebiotics modestly raise adiponectin in metabolic syndrome and obesity trials."
  - target: 01-human/03-molecular/secretory-iga
    relation: connects-to
    note: "SIgA shapes host-microbiome homeostasis: coats commensal bacteria to prevent translocation; IgA-seq identifies pathobiont-specific SIgA coating; SIgA deficiency → bacterial translocation and dysbiosis; Akkermansia and Bifidobacterium are high-SIgA-coating commensals."
  - target: 03-medicine/01-modern/08-gi/omeprazole
    relation: modulated-by
    note: "Chronic PPI (omeprazole) → suppressed gastric acid → altered upper GI microbiome: ↑ Streptococcus/Rothia/Veillonella colonize stomach; ↑ SIBO; disrupts lower GI microbiome; reversible on discontinuation; contributes to pneumonia and C. diff risk."
  - target: 03-medicine/01-modern/06-antimicrobial/vancomycin
    relation: modulated-by
    note: "Oral vancomycin dramatically disrupts gut anaerobes (Bacteroidetes, Bifidobacterium, Lactobacillus) while sparing aerobic gram-positive cocci; microbiome recovery takes 3–6 months; vancomycin-driven dysbiosis increases VRE and C. diff colonization risk in hospital settings."
  - target: 03-medicine/01-modern/06-antimicrobial/amoxicillin
    relation: modulated-by
    note: "Amoxicillin reduces gram-positive and gram-negative gut microbiota diversity; Enterobacteriaceae bloom during treatment; microbiome recovery takes 1–2 months post-course; repeated courses associate with persistent dysbiosis."
  - target: 02-pathogen/06-microbiome/lactobacillus-rhamnosus
    relation: modulated-by
    note: "L. rhamnosus GG is the most-studied probiotic modulator of gut microbiome composition: lactic acid cross-feeds butyrate producers (Faecalibacterium prausnitzii); SpaCBA pili exclude pathogens from mucus; reduces AAD and infantile eczema risk."
  - target: 02-pathogen/03-fungi/candida-albicans
    relation: connects-to
    note: "C. albicans is a commensal gut fungus (70% of healthy adults); core microbiome (Bacteroidetes, Lactobacillus) and sIgA suppress hyphal transition; antibiotic dysbiosis removes this barrier → Candida overgrowth, gut translocation, and candidemia."
  - target: 01-human/02-atomic/carbon
    relation: connects-to
    note: "Colonic bacteria ferment dietary fibre (complex carbon polymers) → SCFAs: acetate (C2), propionate (C3), butyrate (C4); butyrate fuels ~70% of colonocyte energy; microbiome carbon fermentation links dietary carbon intake to host metabolic health."
  - target: 01-human/02-atomic/nitrogen
    relation: connects-to
    note: "Gut bacteria perform nitrogen cycling: urease-positive species hydrolyse urea; amino acid fermentation → ammonia and branched-chain SCFAs; dietary protein nitrogen is the primary driver of microbiome composition; nitrogen balance determines colonocyte renewal."
  - target: 02-pathogen/06-environmental/diarrheal-disease
    relation: damaged-by
    note: "Enteric pathogens (Salmonella, C. diff, rotavirus) disrupt gut microbiome via invasion and diarrhea-driven washout of commensal species; post-diarrheal dysbiosis delays mucosal recovery; FMT (fecal microbiota transplant) is curative for recurrent C. difficile colitis."
  - target: 01-human/07-system/inflammatory-bowel-disease
    relation: connects-to
    note: "The gut microbiome is central to inflammatory bowel disease: loss of diversity and a shift toward pro-inflammatory species breaches the mucosal barrier and provokes the immune attack of Crohn's and colitis—so the microbiome is both a driver and a treatment target."
  - target: 01-human/07-system/parkinsons-disease
    relation: connects-to
    note: "The gut microbiome links to Parkinson's disease via the gut-brain axis: α-synuclein pathology may begin in the enteric nervous system and ascend the vagus, gut dysbiosis is common, and constipation precedes motor symptoms by years—Parkinson's may start in the gut."
  - target: 02-pathogen/02-bacteria/clostridioides-difficile
    relation: connects-to
    note: "Clostridioides difficile infection is the disease of a disrupted microbiome: antibiotics wipe out protective gut flora, letting C. difficile overgrow, and restoring the microbiome by fecal transplant cures cases—proof that the microbial community is protective."
  - target: 01-human/06-organ/large-intestine
    relation: connects-to
    note: "The gut microbiome lives mainly in the large intestine: trillions of anaerobes ferment dietary fiber there into short-chain fatty acids that nourish the colonic lining, so colonic health and microbial ecology are inseparable."
  - target: 01-human/05-tissue/intestinal-epithelium
    relation: connects-to
    note: "The microbiome and intestinal epithelium are mutual keepers: bacterial short-chain fatty acids feed colonocytes and tighten the barrier, while a healthy epithelium confines microbes—dysbiosis breaches this, leaking endotoxin and driving inflammation."
  - target: 01-human/03-molecular/serotonin
    relation: connects-to
    note: "The gut microbiome shapes serotonin and the gut-brain axis: most of the body's serotonin is made by gut enterochromaffin cells, and microbial metabolites tune its production, linking the flora to motility, mood and bidirectional gut-brain signaling."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "The gut and liver are wired together: microbial products and bile acids flow up the portal vein, so a leaky, dysbiotic gut delivers bacterial endotoxin to the liver—fueling fatty liver and NASH—while the liver's bile in turn reshapes which microbes thrive."
  - target: 01-human/07-system/type-2-diabetes
    relation: connects-to
    note: "Gut microbes influence type 2 diabetes risk: fermentation makes short-chain fatty acids that improve insulin sensitivity, while dysbiosis raises inflammation and energy harvest—so the microbiome is a metabolic organ that helps tip the balance toward insulin resistance."
  - target: 01-human/07-system/rheumatoid-arthritis
    relation: connects-to
    note: "The gut microbiome is implicated in rheumatoid arthritis: dysbiosis (e.g., expansion of Prevotella) may prime mucosal immunity and citrullination that later attacks joints—supporting the idea that some autoimmunity begins at gut and other mucosal surfaces."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: connects-to
    note: "The gut microbiome teaches the immune system tolerance via regulatory T cells: bacterial short-chain fatty acids induce colonic Tregs that restrain inflammation, so a healthy microbiome supports immune balance and dysbiosis tips toward autoimmunity and allergy."
  - target: 01-human/03-molecular/dopamine
    relation: connects-to
    note: "Gut microbes influence dopamine and the gut-brain axis: bacteria produce dopamine and its precursors and shape its metabolism, contributing to mood and movement signaling—part of why the microbiome is implicated in Parkinson's and psychiatric disease."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "The gut-brain axis links the microbiome to depression: microbial metabolites and immune signals reaching the brain influence mood, and people with depression show altered gut flora—fueling interest in diet and probiotics as adjuncts."
  - target: 01-human/03-molecular/gaba
    relation: connects-to
    note: "Gut bacteria make GABA and talk to the brain: certain species synthesize this calming neurotransmitter (and others), part of the gut-brain axis through which the microbiome influences mood, anxiety, and stress alongside serotonin and dopamine."
  - target: 01-human/07-system/atherosclerosis
    relation: connects-to
    note: "The gut microbiome promotes atherosclerosis through TMAO: bacteria convert dietary choline and carnitine into TMAO, a metabolite that accelerates plaque and clotting—so what microbes make from red meat and eggs reaches the arteries."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "Dendritic cells read the gut microbiome to set immunity: they sample bacteria across the gut lining and decide between tolerance and attack, so the microbes present shape whether the immune system stays calm or inflames."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "The gut microbiome talks to the brain: its bacteria make neurotransmitters and metabolites and signal along the vagus nerve, a gut-brain axis now linked to mood, behavior and neurodegeneration like Parkinson's."
  - target: 01-human/02-atomic/hydrogen
    relation: connects-to
    note: "The gut microbiome runs on fermentation that makes gas: bacteria breaking down fiber release hydrogen and methane, the gases measured in breath tests to detect malabsorption and small-intestinal bacterial overgrowth."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Gut macrophages keep an uneasy peace with the microbiome: lining the bowel wall, they tolerate friendly bacteria while staying ready to attack invaders, so this restraint is central to keeping the trillions of microbes from triggering inflammation."
  - target: 01-human/06-organ/small-intestine
    relation: connects-to
    note: "The small intestine normally holds few microbes; when they overgrow—SIBO—the result is bloating, gas and malabsorption, a disorder of the microbiome appearing in the wrong place."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "The microbiome trains the immune system: some bacteria drive Th17 helper cells while others expand regulatory T cells, so the microbes tune the balance between defense and tolerance."
  - target: 01-human/02-atomic/sulfur
    relation: connects-to
    note: "Sulfate-reducing gut bacteria make hydrogen sulfide: this pungent gas, at high levels, is toxic to the colon lining and has been implicated in ulcerative colitis, a darker side of microbial metabolism."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "Oxygen's near-absence defines the gut's microbial world: the colon is anaerobic, and cells lining it burn oxygen to keep it that way, favoring the beneficial anaerobes — when oxygen leaks in, harmful facultative bacteria bloom in dysbiosis."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy reveals the microbial city up close: it shows bacterial flagella and pili, the dense biofilms clinging to the gut wall, and the protective mucus layer separating the microbes from the cells beneath."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "The gut and kidney trade toxins: microbes turn dietary compounds into indoxyl sulfate, p-cresyl sulfate, and TMAO that the kidney must clear, so in kidney failure these gut-derived toxins build up and worsen cardiovascular damage."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "The microbiome talks to the brain: along the gut-brain axis it signals through the vagus nerve, microbial metabolites, and immune messengers, shaping mood, stress responses, and behavior — the basis of its links to depression and Parkinson's."
  - target: 03-medicine/03-food/dietary-fiber
    relation: connects-to
    note: "Fiber is the microbiome's fuel: colonic bacteria ferment indigestible dietary fiber into short-chain fatty acids like butyrate that feed the gut lining, calm inflammation, and reward a fiber-rich diet with a healthier microbial community."
  - target: 03-medicine/03-food/vitamin-d
    relation: connects-to
    note: "Vitamin D and the gut flora shape each other: vitamin D and its receptor in the gut tune the microbial community and barrier, while the microbiome in turn influences vitamin D metabolism — a two-way tie linking sunlight, diet, and gut health."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "The flora tune antibodies beyond the gut: germ-free animals make poor antibody and respond weakly to vaccines, showing the microbiome calibrates the whole systemic humoral response, not just the secretory IgA bathing the mucosa."
  - target: 01-human/07-system/colorectal-cancer
    relation: connects-to
    note: "Some microbes turn carcinogenic: a dysbiotic flora enriched in Fusobacterium nucleatum and toxin-making bacteria fosters colorectal cancer, inflaming the mucosa and damaging DNA, while a fiber-fed, butyrate-rich community protects against it."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "A gut-skin axis links the two surfaces: dysbiosis and a leaky gut feed inflammatory skin disease — acne, eczema, psoriasis, and rosacea — through immune and metabolite signals, which is why diet and probiotics are studied for the skin."
  - target: 01-human/03-molecular/estrogen
    relation: connects-to
    note: "Gut bacteria recycle the body's estrogen: the estrobolome — microbial enzymes that deconjugate estrogens excreted in bile so they re-enter circulation — sets how much estrogen the body keeps, linking dysbiosis to breast cancer and menopausal health."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "Microbes talk to the nervous system: bacterial metabolites and vagal signaling from the gut reach enteric and brain neurons, shaping mood, appetite and pain in the gut-brain axis that underlies the microbiome's effects on behavior."
  - target: 01-human/07-system/nash
    relation: connects-to
    note: "A leaky gut inflames the liver: dysbiosis lets bacterial endotoxin reach the liver through the portal vein, fueling the inflammation that turns fatty liver into NASH — the gut-liver axis behind much metabolic liver disease."
  - target: 02-pathogen/06-microbiome/faecalibacterium-prausnitzii
    relation: connects-to
    note: "One species is a keystone of gut health: Faecalibacterium prausnitzii is a major butyrate producer that feeds the colon lining and calms inflammation, and its depletion is a consistent marker of dysbiosis in IBD and metabolic disease."
  - target: 02-pathogen/02-bacteria/escherichia-coli
    relation: connects-to
    note: "Dysbiosis lets pathobionts bloom: commensal E. coli normally sits as a minor member, but expansions of proteobacteria like it mark a disturbed microbiome and can tip the balance toward inflammation and even cancer-promoting genotoxins."
  - target: 01-human/07-system/multiple-sclerosis
    relation: connects-to
    note: "The gut helps tune brain autoimmunity: microbiome composition shapes the regulatory and Th17 balance that drives multiple sclerosis, one of the clearest examples of the gut-immune-brain axis in an autoimmune disease far from the bowel."
  - target: 01-human/03-molecular/histamine
    relation: connects-to
    note: "Some gut bacteria make histamine themselves: histamine-producing species decarboxylate dietary histidine in the lumen, and an overgrowth of them is thought to underlie histamine intolerance with its flushing, headaches and gut upset."
  - target: 01-human/07-system/asthma
    relation: connects-to
    note: "The gut shapes the airways through a gut-lung axis: early-life microbial diversity trains immune tolerance, and dysbiosis in infancy is linked to a higher risk of developing asthma and allergic airway disease."
  - target: 02-pathogen/02-bacteria/salmonella-typhi
    relation: connects-to
    note: "A healthy flora is a barrier against invaders: the resident microbiome provides colonization resistance, and antibiotics or dysbiosis that thin it leave the gut open to enteric pathogens like Salmonella to take hold."
  - target: 01-human/07-system/alzheimers-disease
    relation: connects-to
    note: "Dysbiosis may stoke the aging brain: gut bacteria shape systemic inflammation and amyloid metabolism along the gut-brain axis, and altered microbiomes are increasingly linked to the neuroinflammation of Alzheimer's disease."
  - target: 01-human/07-system/atopic-dermatitis
    relation: connects-to
    note: "The gut tunes the skin's immunity: a gut-skin axis means early-life dysbiosis biases the immune system toward allergy, and reduced microbial diversity in infancy is associated with developing atopic dermatitis."
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "A gut-kidney axis runs both ways: dysbiosis lets the gut generate uremic toxins like indoxyl sulfate that injure the kidney, while failing kidneys in turn reshape the flora, a vicious cycle in chronic kidney disease."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "The gut-brain axis shapes anxiety: microbial metabolites and vagal signaling modulate GABA and the stress axis, and dysbiosis is linked to heightened anxiety, with probiotics under study to ease it."
  - target: 01-human/07-system/autism-spectrum-disorder
    relation: connects-to
    note: "Microbes and behavior intertwine in development: GI symptoms are common in autism, and altered gut flora and its metabolites are implicated through the gut-brain axis in the behavioral phenotype."
  - target: 01-human/07-system/gout
    relation: connects-to
    note: "Bacteria help handle the body's urate: the gut microbiome degrades a meaningful share of purines and uric acid, and dysbiosis that impairs this disposal contributes to the hyperuricemia behind gout."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "It lives in and shapes the gut it inhabits: the microbiome ferments fibre into short-chain fatty acids that feed colonocytes, metabolises bile acids and trains gut immunity, fundamentally shaping digestion."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "The microbes act as an endocrine organ: gut bacteria produce and modulate hormones, regulate the estrobolome that recycles oestrogen and shape insulin and appetite signalling through their metabolites."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "Gut and genital microbiomes are linked: the gut seeds the vaginal flora and shapes systemic oestrogen via the estrobolome, while birth and breastfeeding transfer the founding microbiome to the newborn."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "Its metabolites reach the heart and vessels: gut microbes generate TMAO that promotes atherosclerosis and short-chain fatty acids that help set blood pressure, linking the microbiome to cardiovascular risk."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "A gut-lung axis shapes the airways: the intestinal microbiome trains systemic and mucosal immunity, influencing susceptibility to respiratory infection and the development of asthma and allergy."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "A gut-bone axis tunes the skeleton: short-chain fatty acids, immune signalling and the absorption of calcium and vitamin K let the microbiome modulate bone density and osteoporosis risk."
  - target: 01-human/07-system/lymphatic-system
    relation: connects-to
    note: "It trains the body's largest lymphoid mass: the gut wall holds gut-associated lymphoid tissue and Peyer's patches, which the microbiome shapes to educate systemic immunity from birth."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "A gut-skin axis reaches the surface: microbial metabolites and immune signalling link the gut microbiome to acne, rosacea, atopic dermatitis and psoriasis."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "A gut-kidney axis carries toxins: microbial metabolites such as indoxyl sulfate, p-cresyl sulfate and TMAO are uraemic toxins that accumulate and accelerate damage in chronic kidney disease."
  - target: 02-pathogen/06-microbiome/bifidobacterium-longum
    relation: connects-to
    note: "A keystone commensal: Bifidobacterium longum is an early-life and adult gut symbiont that ferments fibre, trains the immune system and is widely used as a probiotic."
  - target: 02-pathogen/02-bacteria/helicobacter-pylori
    relation: connects-to
    note: "A disruptor at the top of the tract: Helicobacter pylori colonises the stomach, reshaping the gastric microbiome and acid environment, with both pathogenic and possibly protective effects."
  - target: 03-medicine/03-food/omega-3-fatty-acids
    relation: connects-to
    note: "Diet reshapes the community: dietary fats including omega-3s alter microbial composition and the short-chain-fatty-acid and inflammatory output of the gut microbiome."
  - target: 03-medicine/01-modern/13-cancer/checkpoint-inhibitors
    relation: connects-to
    note: "It tunes cancer immunotherapy: the gut microbiome powerfully shapes response to checkpoint blockade — species like Akkermansia and Faecalibacterium predict who responds, and antibiotics or faecal transplant can blunt or restore efficacy."
  - target: 01-human/05-tissue/peyers-patches
    relation: connects-to
    note: "It is sampled by gut immunity: Peyer's patches and their M cells continuously survey the microbiome, training the regulatory T cells and IgA responses that keep commensals tolerated while excluding pathogens."
  - target: 01-human/07-system/type-1-diabetes
    relation: connects-to
    note: "Early flora shape autoimmunity: reduced microbial diversity and altered short-chain-fatty-acid producers in infancy are linked to the development of type 1 diabetes, implicating the microbiome in the loss of immune tolerance to beta cells."
  - target: 01-human/05-tissue/hepatic-lobule
    relation: connects-to
    note: "The gut-liver axis: microbial metabolites and translocated endotoxin travel up the portal vein to the hepatic lobule, driving the inflammation and fat accumulation of NAFLD/NASH and shaping bile-acid metabolism."
  - target: 03-medicine/01-modern/07-metabolic/metformin
    relation: connects-to
    note: "The microbiome mediates its action: metformin reshapes gut bacterial composition, and that shift contributes both to its glucose-lowering effect and to the GI side effects that limit its use."
  - target: 01-human/07-system/gvhd
    relation: connects-to
    note: "It steers transplant immunity: after stem-cell transplant, loss of intestinal microbial diversity worsens gut graft-versus-host disease and mortality, making the microbiome a target for protecting the new immune system."
  - target: 01-human/07-system/epilepsy
    relation: connects-to
    note: "Diet, microbes and seizures: the ketogenic diet's anticonvulsant effect in drug-resistant epilepsy is partly mediated by gut-microbiome shifts that raise GABA and lower glutamate, a striking gut-brain link."
  - target: 01-human/07-system/ankylosing-spondylitis
    relation: connects-to
    note: "The gut-joint axis: subclinical gut inflammation and a distinct dysbiosis are central to ankylosing spondylitis, where HLA-B27 shapes a microbiome that helps drive the spondyloarthritis."
  - target: 01-human/07-system/sepsis
    relation: connects-to
    note: "The gut as motor of sepsis: a depleted microbiome and leaky epithelium let gut bacteria translocate, and the dysbiosis of critical illness worsens multi-organ failure and mortality."
  - target: 01-human/07-system/covid-19-disease
    relation: connects-to
    note: "Dysbiosis and COVID: the gut microbiome is altered in acute COVID-19 and shapes its severity, and persistent dysbiosis is implicated in the gastrointestinal and fatigue symptoms of long COVID."
  - target: 01-human/07-system/schizophrenia
    relation: connects-to
    note: "Gut-brain axis in psychosis: microbiome alterations communicate with the brain via immune, metabolic and vagal routes and are increasingly implicated in schizophrenia, extending the gut's reach into psychotic illness."
  - target: 01-human/07-system/hcc
    relation: connects-to
    note: "The gut-liver axis to cancer: dysbiosis and bacterial-product translocation through the portal vein inflame the liver and, via NASH and cirrhosis, contribute to hepatocellular carcinoma."
  - target: 01-human/03-molecular/glp-1
    relation: connects-to
    note: "SCFA-driven incretin: short-chain fatty acids produced by gut bacteria stimulate enteroendocrine GLP-1 secretion, linking the microbiome to appetite and glucose control."
  - target: 01-human/04-cellular/b-cell
    relation: connects-to
    note: "Shaping mucosal antibodies: the gut microbiome drives the development of mucosal B cells and their secretory IgA, tuning the antibody repertoire that polices the gut."
  - target: 01-human/07-system/fibromyalgia
    relation: connects-to
    note: "Gut-brain pain axis: gut dysbiosis is increasingly implicated in fibromyalgia, with altered microbiome composition linked to its central pain and fatigue through the gut-brain axis."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "Th17 induction: segmented filamentous and other commensal bacteria drive intestinal Th17 cells and IL-17A, a microbiome-tuned arm of mucosal defence that, when dysregulated, fuels autoimmune and inflammatory disease."
  - target: 01-human/03-molecular/bdnf
    relation: connects-to
    note: "Gut-brain signalling: germ-free and dysbiotic states alter hippocampal BDNF expression, one molecular link by which the microbiome shapes mood, anxiety and cognition along the gut-brain axis."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Metabolic crosstalk: microbial composition and short-chain fatty acids modulate leptin levels and central leptin sensitivity, tying the gut microbiome to appetite regulation and obesity."
  - target: 01-human/03-molecular/tlr4
    relation: connects-to
    note: "Innate interface: TLR4 sensing of bacterial LPS is the principal microbiome-innate-immune interface, and leakage of LPS across a compromised barrier drives the 'metabolic endotoxemia' linking dysbiosis to systemic inflammation."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "Tolerance induction: commensal bacteria and their short-chain fatty acids drive TGF-β-dependent differentiation of intestinal regulatory T cells, the mechanism by which the microbiome teaches the immune system tolerance to harmless antigens."
  - target: 01-human/03-molecular/nlrp3-inflammasome
    relation: connects-to
    note: "Reciprocal regulation: the NLRP3 and related inflammasomes both shape microbiota composition and are activated by microbial signals, a feedback loop whose disruption promotes the dysbiosis underlying inflammatory bowel and metabolic disease."
  - target: 01-human/03-molecular/cholesterol
    relation: connects-to
    note: "Bile-acid metabolism: gut bacteria deconjugate and transform host bile acids made from cholesterol into secondary bile acids that signal through FXR and TGR5, a microbial arm of cholesterol and metabolic regulation linking the microbiome to host lipid handling."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "Commensal tolerance: commensal bacteria and their metabolites induce IL-10-producing regulatory T cells in the gut, the tolerogenic response that keeps the immune system from attacking the resident microbiota and whose failure underlies inflammatory bowel disease."
  - target: 01-human/03-molecular/acetylcholine
    relation: connects-to
    note: "Gut-brain vagal axis: microbial metabolites signal to vagal afferents that use acetylcholine, a neural limb of the microbiota-gut-brain axis through which the microbiome influences mood, appetite and the cholinergic anti-inflammatory reflex."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "Barrier hypoxia: microbial butyrate is consumed by colonocytes, lowering epithelial oxygen and stabilising HIF-1α, a physiological hypoxia signal that maintains the gut barrier and the anaerobic niche favouring beneficial commensals."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "Tolerance set-point: microbial signals sensed through pattern-recognition receptors tune epithelial NF-κB activity, balancing antimicrobial defence against tolerance to the commensal microbiota that prevents inappropriate inflammation."
  - target: 01-human/03-molecular/wnt-beta-catenin
    relation: connects-to
    note: "Epithelial renewal: the microbiota influences Wnt/β-catenin signalling in the intestinal crypt, modulating the stem-cell-driven regeneration that continuously renews the gut lining the microbiome inhabits."
  - target: 01-human/03-molecular/myd88
    relation: connects-to
    note: "Innate sensing hub: microbiota-derived molecular patterns signal through TLRs (TLR4 mapped) and MyD88 to NF-κB (mapped), the core innate pathway by which the host senses and tolerates its commensal microbiome."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Immune education: the microbiota calibrates the balance between IFN-γ-producing Th1 cells and regulatory T cells during the development of mucosal immunity, shaping systemic immune tone."
  - target: 01-human/03-molecular/ghrelin
    relation: connects-to
    note: "Metabolic axis: the gut microbiome modulates appetite-regulating hormones including ghrelin (with leptin and GLP-1 mapped), part of the microbiome's influence on host energy balance and metabolism."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "Metabolite nutrient sensing: microbial metabolites such as short-chain fatty acids and amino acids signal through mTOR in host epithelial and immune cells, linking the gut microbiome to host nutrient sensing and immune-cell differentiation."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "Systemic cytokine tone: the gut microbiota tunes systemic IL-6 and inflammatory-cytokine tone, a route by which dysbiosis influences host inflammation beyond the gut."
  - target: 01-human/03-molecular/ntrk
    relation: connects-to
    note: "Gut-brain neurotrophin axis: the microbiome modulates BDNF and its TrkB receptor (NTRK) signalling in the gut-brain axis (BDNF already mapped), influencing enteric and central neural function."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Galectin-3 at the mucosal interface helps shape the host immune recognition of commensal and pathobiont bacteria, linking the microbiome to mucosal immunity."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "Microbiota-derived signals drive IL-6/IL-23-STAT3 activation that programmes intestinal Th17 responses and epithelial homeostasis in the gut."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "Microbial and damage-associated cytosolic DNA engages cGAS-STING in the gut mucosa, coupling the microbiome to innate inflammatory tone."
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "TGF-β-SMAD signaling (TGF-β already mapped) mediates the microbial-metabolite-driven regulatory T-cell induction and epithelial homeostasis of the gut."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "IFN-STAT1 signaling links microbiota-shaped interferon tone to mucosal immune homeostasis and antimicrobial defense in the gut."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "FOXO transcription factors integrate microbial-metabolite and nutrient signals to regulate gut epithelial and immune homeostasis."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "Microbial metabolites and pattern-recognition signals feed into host PI3K-AKT signaling that governs the intestinal epithelial homeostasis shaped by the gut microbiome."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "ERK-MAPK signaling transduces the microbial and metabolite stimuli that modulate the epithelial and immune responses to the gut microbiome."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "GSK-3β integrates microbial pattern-recognition signaling to modulate the NF-κB inflammatory tone and Wnt-dependent epithelial renewal shaped by the gut microbiome."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK, activated by microbiota-derived short-chain fatty acids, links the gut microbiome to host energy metabolism."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "PI3K (PIK3CA)-AKT signaling (AKT already mapped) in the intestinal epithelium responds to the microbial signals of the gut microbiome."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Autophagy in intestinal epithelial and immune cells shapes the host response to and tolerance of the gut microbiome."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC-family kinase signaling participates in the epithelial-barrier junction dynamics at the host-microbiome interface of the gut."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "DNMT3A-mediated DNA methylation, shaped by microbial metabolites, participates in the epigenetic host-microbiome crosstalk of the gut."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-driven leukocyte recruitment participates in the mucosal immune responses shaped by the gut microbiome."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "CXCL12-CXCR4 signaling participates in the epithelial-immune interactions shaped by the gut microbiome."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "IL-1β-driven inflammation participates in the microbiome-immune signaling of the gut microbiome."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "IL-33 alarmin signaling participates in the mucosal immune responses shaped by the gut microbiome."
  - target: 01-human/03-molecular/insulin
    relation: connects-to
    note: "Metabolic axis: microbiome composition and its short-chain fatty acids influence host insulin sensitivity and energy harvest, so dysbiosis is mechanistically linked to obesity and type 2 diabetes through altered insulin signalling."
  - target: 01-human/03-molecular/mu-opioid-receptor
    relation: connects-to
    note: "Gut-brain visceral pain: the microbiome shapes enteric opioid signalling and visceral nociception, and germ-free or antibiotic-altered states change mu-opioid-mediated analgesia, part of the microbiome-gut-brain axis governing pain in disorders like IBS."
  - target: 03-medicine/03-food/omega-3-fatty-acids
    relation: connects-to
    note: "Diet-microbiome interaction: omega-3 fatty acids shift microbiome composition toward anti-inflammatory, short-chain-fatty-acid-producing taxa, illustrating the reciprocal diet-microbiome relationship that modulates host inflammation."
  - target: 01-human/06-organ/pancreas
    relation: connects-to
    note: "Islet autoimmunity: the gut microbiome influences the development of type-1-diabetes (already mapped) by shaping mucosal immunity and permeability, linking microbial dysbiosis in early life to the islet autoimmunity of the pancreas."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Luminal iron competition: dietary and unabsorbed iron in the gut lumen shapes the microbiome, favouring some pathobionts, so iron supplementation can worsen dysbiosis, a nutrient-microbe interaction relevant to anaemia treatment."
  - target: 01-human/03-molecular/oxytocin
    relation: connects-to
    note: "Microbe-driven oxytocin: specific commensals such as Lactobacillus reuteri raise systemic oxytocin through the vagus, influencing social behaviour and wound healing, a striking example of the microbiome-gut-brain axis reaching neuroendocrine signalling."
  - target: 01-human/03-molecular/nitric-oxide
    relation: connects-to
    note: "Luminal nitric oxide: bacterial and host nitric oxide in the gut lumen shapes the microbial community and regulates the mucosal blood flow, part of the chemical crosstalk between the microbiome and its epithelial habitat."
  - target: 01-human/03-molecular/melatonin
    relation: connects-to
    note: "Circadian microbiome: gut-derived melatonin and the host circadian clock impose a diurnal rhythm on the microbiome (serotonin already mapped), and disrupted sleep or shift work perturbs the community and its metabolic output."
  - target: 01-human/03-molecular/prostaglandins
    relation: connects-to
    note: "Mucosal barrier eicosanoids: prostaglandins maintain the mucosal barrier and blood flow that the microbiome modulates (short-chain fatty acids already GLP-1-mapped), part of how commensals and the epithelium co-regulate gut homeostasis."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: connects-to
    note: "SCFA-induced Tregs: the short-chain fatty acids of the microbiome induce regulatory T cells (TGF-β and IL-10 already mapped) in the gut, a central mechanism by which the commensal community maintains immune tolerance."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Gut macrophage sampling: the intestinal macrophages continuously sample the microbiota (TLR4 already mapped) and maintain a tolerant, anti-inflammatory tone, part of the immune dialogue between the host and its commensals."
  - target: 01-human/07-system/obesity
    relation: connects-to
    note: "Microbiome and energy harvest: the composition of the gut microbiome influences energy harvest from the diet and the low-grade inflammation (leptin and adiponectin already mapped) of obesity, linking dysbiosis to metabolic disease."
  - target: 01-human/03-molecular/tnf-alpha
    relation: connects-to
    note: "Endotoxin-driven inflammation: the microbial LPS (TLR4 already mapped) drives the TNF of the gut and systemic inflammation, and the dysbiosis-driven TNF underlies much of the inflammation of gut and metabolic disease."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "Type-2 balance: the IL-4/Th2 (anti-helminth) arm (IL-10 already mapped) is shaped by the microbiome and balances the Th17 (IL-17 already mapped) and regulatory arms of the mucosal immune response to the commensals."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "Anti-helminth type-2 arm: IL-13, with IL-4 (already mapped), mediates the type-2 (anti-helminth) response that both shapes and is shaped by the gut microbiome, part of the host-microbe immune dialogue."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Metabolic adipokine: resistin, with leptin and adiponectin (already mapped), is the adipokine of the microbiome-host metabolic (insulin already mapped) crosstalk and the dysbiosis-associated inflammation."
  - target: 01-human/04-cellular/plasma-cell
    relation: connects-to
    note: "IgA plasma cells: the microbiome drives the expansion of the intestinal plasma cells that secrete the secretory IgA (already mapped) shaping the commensal community of the gut."
  - target: 01-human/03-molecular/hepcidin
    relation: connects-to
    note: "Microbiome iron: the gut microbiome influences the intestinal iron absorption and competes for the luminal iron, interacting with the hepcidin (IL-6 already mapped) iron regulation."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "Microbiome-NK tuning: the gut microbiome (via its metabolites and the tonic signals) tunes the NK-cell (perforin already mapped) function and the systemic innate immunity."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Tonic interferon priming: the commensal microbiome sets the tonic type-I interferon (cGAS-STING already mapped) that primes the antiviral and antitumour immunity of the host."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 induction: the microbiome-conditioned dendritic cells (already mapped) produce IL-12 to drive the Th1 (IFN-γ already mapped) arm of the gut-shaped systemic immunity."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Type-2/eosinophil arm: the microbiome shapes the IL-5 and the type-2 (IL-4 and IL-13 already mapped) immunity, tuning the gut eosinophils and the anti-parasite response of the host."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17 induction: the segmented-filamentous and other commensal bacteria induce the IL-23/Th17 (IL-17 already mapped) axis of the gut-shaped systemic immunity."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "IgE regulation: the commensal microbiome restrains the baseline IgE (with IL-4 and IL-13 already mapped), and the dysbiosis/germ-free state raises the IgE and the allergic susceptibility."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Microbiome-shaped CD8: the commensal microbiome shapes the intraepithelial and systemic cytotoxic T cells (perforin pathway), and the dysbiosis alters the anti-tumour and anti-viral CD8 response."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "Mast-cell crosstalk: the gut mast cells are educated by the commensal microbiome and, in dysbiosis, contribute to the barrier dysfunction and the type-2 (IgE already mapped) sensitisation of the gut-shaped immunity."
  - target: 01-human/05-tissue/bone-marrow
    relation: connects-to
    note: "Gut-marrow axis: the commensal microbiome, via the microbial metabolites and signals, conditions the haematopoiesis and the myeloid output of the bone marrow, a systemic arm of the gut-shaped immunity."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Microbiome-primed complement: the commensal microbiome tunes the steady-state complement C3 expression (locally and systemically), part of the microbiome-shaped innate immunity of the host."
  - target: 01-human/03-molecular/c5ar1
    relation: connects-to
    note: "C5a receptor: the C5aR1 signalling (with the complement C3 already mapped) links the microbiome-tuned complement to the neutrophil recruitment of the intestinal mucosa."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "Microbiome-primed neutrophils: the commensal microbiome primes the neutrophils (the ageing and antimicrobial function), a systemic arm of the gut-shaped innate immunity."
  - target: 01-human/03-molecular/tslp
    relation: connects-to
    note: "Epithelial barrier crosstalk: TSLP, secreted by intestinal epithelial cells, educates dendritic cells (already mapped) toward mucosal tolerance and acts as the alarmin linking barrier stress to the gut-microbiome immune interface."
  - target: 01-human/03-molecular/bradykinin
    relation: connects-to
    note: "Kinin-microbiome axis: bradykinin, generated by the intestinal contact pathway, modulates intestinal permeability and lamina propria vasodilation, part of the kinin regulation of the gut-microbiome environment."
  - target: 01-human/03-molecular/c1-esterase-inhibitor
    relation: connects-to
    note: "Complement/kinin gate: C1-esterase inhibitor limits classical complement (complement C3 and C5aR1 already mapped) and bradykinin overactivation in the intestinal lumen, gating the inflammatory response to the commensal microbiome."
  - target: 01-human/03-molecular/erythropoietin
    relation: connects-to
    note: "Gut EPO axis: erythropoietin, produced by intestinal epithelium under hypoxic stress (HIF-1α already mapped), supports epithelial repair and modulates the enteric immune tone, linking gut oxygenation to the systemic haematopoietic response."
  - target: 01-human/03-molecular/periostin
    relation: connects-to
    note: "Crypt stromal ECM: periostin, secreted by subepithelial fibroblasts of the intestinal crypt niche, maintains basement-membrane integrity and supports epithelial regeneration and stem-cell quiescence of the gut-microbiome ecosystem."
  - target: 01-human/03-molecular/complement-c5
    relation: connects-to
    note: "Terminal complement gating: complement C5 cleavage in the intestinal lamina propria generates C5a (C5aR1 already mapped) and C5b-9 MAC, amplifying inflammatory responses to dysbiosis and shaping the innate defence of the gut-microbiome ecosystem."
  - target: 01-human/03-molecular/testosterone
    relation: connects-to
    note: "GM testosterone: testosterone shapes gut-microbiome composition via regulatory-T-cell (already mapped) and B-cell (already mapped) modulation; androgen signalling suppresses IL-6 (already mapped) and TNF-α (already mapped) intestinal inflammation (IBD already mapped)."
  - target: 01-human/03-molecular/prolactin
    relation: connects-to
    note: "GM prolactin: prolactin receptors on intestinal epithelium (already mapped) and liver (already mapped) modulate mucosal immunity; prolactin drives IL-6 (already mapped) production in mast cells (already mapped) and shapes regulatory-T-cell (already mapped) gut tolerance."
  - target: 01-human/03-molecular/vasopressin
    relation: connects-to
    note: "GM vasopressin: vasopressin (ADH) acts on intestinal epithelium (already mapped) to modulate fluid transport and barrier integrity; vasopressin also suppresses IL-1β (already mapped) and TNF-α (already mapped) intestinal inflammation (IBD already mapped)."
  - target: 01-human/02-atomic/selenium
    relation: connects-to
    note: "GM selenium: selenoproteins in intestinal epithelium (already mapped) counter NF-κB (already mapped) oxidative stress; selenium deficiency impairs Akkermansia (already mapped) colonisation resistance and amplifies macrophage (already mapped) mucosal inflammation."
  - target: 01-human/02-atomic/iodine
    relation: connects-to
    note: "GM iodine: intestinal lactoperoxidase (iodine-dependent) limits pathogen colonisation in the epithelium (already mapped); iodine deficiency amplifies NF-κB (already mapped) driven IL-6 (already mapped) mucosal inflammation and impairs macrophage (already mapped) homeostasis."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "GM sodium: high dietary sodium depletes Lactobacillus (already mapped) and amplifies IL-17A (already mapped) responses; sodium-driven NF-κB (already mapped) activation impairs intestinal epithelium (already mapped) barrier integrity and macrophage (already mapped) homeostasis."
---

# Gut Microbiome

## Overview

The gut microbiome is the **vast ecological community of microorganisms** inhabiting the human gastrointestinal tract — comprising approximately **10¹³ bacterial cells** (comparable to human somatic cell number [^sender-2016-microbiome-census]), plus archaea, fungi (mycobiome), viruses (virome), and protozoa. The collective genome of these microorganisms — the **metagenome** — encodes approximately 150-fold more genes than the human genome, providing metabolic capabilities that human enzymes cannot perform independently.

The microbiome is not uniformly distributed: microbial density increases dramatically from stomach (~10¹–10³ cells/mL) to terminal ileum (~10⁷–10⁸/mL) to colon (~10¹¹–10¹²/mL), where the vast majority of the microbiome resides. The colon is dominated by **obligate anaerobes** from two major phyla: **Firmicutes** (~60%, includes Clostridia, Lactobacillus, Ruminococcus) and **Bacteroidetes** (~30%, includes Bacteroides, Prevotella). Actinobacteria (Bifidobacterium), Proteobacteria, and Verrucomicrobia (Akkermansia) comprise smaller but functionally important fractions.

The microbiome is now recognized as an integral functional organ, contributing to digestion, immune education, metabolic homeostasis, and even neurological function (gut-brain axis). Dysbiosis — compositional or functional disruption of the microbiome — is associated with inflammatory bowel disease, obesity, type 2 diabetes, colorectal cancer, depression, and Clostridioides difficile infection.

## Structure

### Microbial Composition and Ecology

**Major phyla and representative genera:**

| Phylum | % Gut | Key genera | Functions |
|:---|:---|:---|:---|
| **Firmicutes** | ~60% | Ruminococcus, Faecalibacterium, Clostridium, Lactobacillus, Enterococcus | Butyrate production (F. prausnitzii); starch fermentation; colonization resistance |
| **Bacteroidetes** | ~25–30% | Bacteroides (B. thetaiotaomicron), Prevotella | Polysaccharide degradation; propionate and acetate production; PSA immunomodulation |
| **Actinobacteria** | ~5–10% | Bifidobacterium | HMO utilization (infants); IgA stimulation; butyrate precursors |
| **Verrucomicrobia** | ~1–3% | Akkermansia muciniphila | Mucin degradation; gut barrier maintenance; metabolic health |
| **Proteobacteria** | ~1–2% | E. coli, Helicobacter, Salmonella | Mostly minor commensals; can bloom in dysbiosis (bloom = overgrowth) |

**Biogeographic compartments:**
- **Mucosa-associated microbiome**: Lactobacillus, Bifidobacterium, Akkermansia — direct interaction with epithelium; shapes mucosal immunity
- **Luminal microbiome**: dominated by Bacteroides, Ruminococcus, Faecalibacterium — primary fermenters
- **Spatial gradients**: crypts are largely microorganism-free (antimicrobial peptides from Paneth cells); villi and crypts differ in microbial composition

### Microbiome Development

The microbiome undergoes characteristic developmental phases:
1. **Neonatal colonization** — seeded by maternal vaginal/fecal microbiota (vaginal birth) or skin/environment (C-section); cord microbiome is essentially sterile
2. **First 3 years** — most critical window; composition influenced by birth mode, breastfeeding (HMO → Bifidobacterium enrichment), antibiotics, and diet; period of immune system "programming"
3. **Adult microbiome** — relatively stable "core" composition; resilient to perturbation but recovers slowly from antibiotics
4. **Elderly microbiome** — reduced diversity, reduced Firmicutes/Bacteroidetes ratio, increased Proteobacteria; associated with inflammaging

## Function

### Short-Chain Fatty Acid (SCFA) Production

The signature metabolic output of gut fermentation: dietary fiber → anaerobic fermentation → SCFAs (predominantly butyrate, propionate, acetate in ~3:1:6 ratio):

| SCFA | Primary producer organisms | Primary functions |
|:---|:---|:---|
| **Butyrate** | Faecalibacterium prausnitzii, Roseburia, Eubacterium rectale | Primary fuel for colonocytes (~70% of colonocyte energy from butyrate); HDAC inhibitor → anti-inflammatory gene expression; strengthens tight junctions; suppresses colorectal cancer cell proliferation |
| **Propionate** | Bacteroides, Veillonella, Phascolarctobacterium | Gluconeogenesis substrate in liver; promotes satiety via free fatty acid receptor (FFAR3) on enteroendocrine cells; reduces hepatic lipogenesis |
| **Acetate** | Bifidobacterium, Akkermansia, many species | Systemic energy substrate; lipogenesis in adipose; conversion to butyrate by cross-feeding species; signaling via FFAR2 |

SCFAs are absorbed by SMCT1 (sodium-coupled monocarboxylate transporter) and MCT4 on colonocytes. Systemic SCFA levels (portal and systemic) regulate adipose, liver, muscle, and immune function.

### Immune System Education

The gut microbiome is the **primary driver of postnatal immune development**:

- **IgA production**: Microbiota-induced germinal center reactions in Peyer's patches and isolated lymphoid follicles → lamina propria IgA-committed plasma cells → 3–5 g/day SIgA secreted into gut lumen; IgA repertoire shaped by commensal antigens
- **Treg induction**: Clostridium clusters IV and XIVa produce SCFAs and other factors that induce colonic Foxp3+ Treg differentiation (butyrate → HDAC inhibition → Foxp3 gene induction); PSA from B. fragilis induces IL-10-producing Tregs
- **Innate priming**: LPS and flagellin from commensals set baseline TLR signaling thresholds; germ-free animals have hypersensitive innate responses
- **Colonization resistance**: competitive exclusion of pathogens via physical (niche occupancy) and chemical (bacteriocins, SCFAs, secondary bile acids) mechanisms — loss of colonization resistance after antibiotics → C. difficile bloom

### Bile Acid Metabolism

Gut bacteria perform critical modifications of host-derived primary bile acids:
- **Primary bile acids** (cholic acid, chenodeoxycholic acid) → secreted into gut → **7α-dehydroxylation** by Clostridium scindens and related Firmicutes → secondary bile acids (deoxycholic acid, lithocholic acid)
- Secondary bile acids activate **FXR** (farnesoid X receptor) and **TGR5** on intestinal and hepatic cells → regulate bile acid synthesis (FXR-FGF-19 feedback), glucagon-like peptide-1 (GLP-1) secretion (TGR5 on L-cells), and innate immunity
- Bile acid dysmetabolism in dysbiosis → Clostridioides difficile susceptibility (secondary bile acids are bacteriostatic for C. diff spore germination)

### Gut-Brain Axis

The microbiome influences CNS function via multiple pathways:
- **Serotonin production**: ~90% of body serotonin is produced in the gut; colonic enterochromaffin cells produce serotonin in response to SCFA/tryptophan signals from microbiota; affects intestinal motility and vagal signaling
- **Tryptophan metabolism**: Gut bacteria convert tryptophan to indole and indole derivatives → aryl hydrocarbon receptor (AhR) agonists → mucosal immune regulation
- **Vagal nerve signaling**: SCFA-activated FFAR3 on enteroendocrine cells → afferent vagal signals → hypothalamus; germ-free animals show altered vagal tone
- **Systemic metabolites**: TMAO (trimethylamine N-oxide) from choline/carnitine fermentation → systemic circulation → cardiovascular risk; uremic toxins (indoxyl sulfate, p-cresyl sulfate) in CKD

## Connections

- `modulates` → **[Immune System](../immune-system/README.md)** — primary educator of mucosal and systemic immunity via IgA induction, Treg programming, innate immune threshold-setting, and colonization resistance
- `contains` → **[Bacteroides fragilis](../../../../02-pathogen/06-microbiome/bacteroides-fragilis/README.md)** — key Bacteroidetes member; PSA from commensal B. fragilis induces Treg and IL-10 (immunoprotective); ETBF toxin disrupts epithelial barrier
- `contains` → **[Akkermansia muciniphila](../../../../02-pathogen/06-microbiome/akkermansia-muciniphila/README.md)** — mucin-degrading species associated with metabolic health; reduced in obesity and T2DM; Amuc_1100 strengthens gut barrier via TLR2
- `connects-to` → **[Obesity](../obesity/README.md)** — dysbiosis in obesity — increased Firmicutes/Bacteroidetes, reduced Akkermansia muciniphila — increases energy harvest and drives metabolic endotoxemia (LPS → TLR4 → systemic inflammation); gut microbiome transfer from obese to germ-free mice transfers the adiposity phenotype.
- `connects-to` → **[Adiponectin](../../../03-molecular/adiponectin/README.md)** — Microbiome dysbiosis → LPS → TLR4 → TNF-α/IL-6 → adiponectin suppression; butyrate-producing bacteria (Akkermansia, Bifidobacterium) → SCFA → PPARγ → ADIPOQ induction; probiotics and prebiotics modestly raise adiponectin in metabolic syndrome and obesity trials.
- `connects-to` → **[Secretory IgA](../../../03-molecular/secretory-iga/README.md)** — SIgA shapes host-microbiome homeostasis: coats commensal bacteria to prevent translocation; IgA-seq identifies pathobiont-specific SIgA coating; SIgA deficiency → bacterial translocation and dysbiosis; Akkermansia and Bifidobacterium are high-SIgA-coating commensals.
- `modulated-by` → **[Omeprazole](../../../03-medicine/01-modern/08-gi/omeprazole/README.md)** — Chronic PPI → suppressed gastric acid → altered upper GI microbiome: ↑ Streptococcus/Rothia/Veillonella colonize stomach; ↑ SIBO; disrupts lower GI microbiome; reversible on discontinuation; contributes to pneumonia and C. diff risk.
- `modulated-by` → **[Vancomycin](../../../03-medicine/01-modern/06-antimicrobial/vancomycin/README.md)** — Oral vancomycin dramatically disrupts gut anaerobes (Bacteroidetes, Bifidobacterium, Lactobacillus) while sparing gram-positive cocci; microbiome recovery takes 3–6 months; vancomycin-driven dysbiosis increases VRE and C. diff colonization risk in hospital settings.
- `modulated-by` → **[Amoxicillin](../../../03-medicine/01-modern/06-antimicrobial/amoxicillin/README.md)** — Amoxicillin reduces gram-positive and gram-negative gut microbiota diversity; Enterobacteriaceae bloom during treatment; microbiome recovery takes 1–2 months post-course; repeated courses associate with persistent dysbiosis.
- `modulated-by` → **[Lactobacillus rhamnosus](../../../../02-pathogen/06-microbiome/lactobacillus-rhamnosus/README.md)** — *L. rhamnosus* GG is the most-studied probiotic modulator of gut microbiome composition: lactic acid cross-feeds butyrate producers (*Faecalibacterium prausnitzii*); SpaCBA pili exclude pathogens from mucus; reduces AAD and infantile eczema risk.
- `connects-to` → **[Candida albicans](../../../../02-pathogen/03-fungi/candida-albicans/README.md)** — C. albicans is a commensal gut fungus (70% of healthy adults); core microbiome (Bacteroidetes, Lactobacillus) and sIgA suppress hyphal transition; antibiotic dysbiosis removes this barrier → Candida overgrowth, gut translocation, and candidemia.
- `connects-to` → **[Carbon](../../02-atomic/carbon/README.md)** — Colonic bacteria ferment dietary fibre (complex carbon polymers) → SCFAs: acetate (C2), propionate (C3), butyrate (C4); butyrate fuels ~70% of colonocyte energy; microbiome carbon fermentation links dietary carbon intake to host metabolic health.
- `connects-to` → **[Nitrogen](../../02-atomic/nitrogen/README.md)** — Gut bacteria perform nitrogen cycling: urease-positive species hydrolyse urea; amino acid fermentation → ammonia and branched-chain SCFAs; dietary protein nitrogen is the primary driver of microbiome composition; nitrogen balance determines colonocyte renewal.
- `damaged-by` → **[Diarrheal Disease](../../../../02-pathogen/06-environmental/diarrheal-disease/README.md)** — Enteric pathogens (Salmonella, C. diff, rotavirus) disrupt gut microbiome via invasion and diarrhea-driven washout of commensal species; post-diarrheal dysbiosis delays mucosal recovery; FMT (fecal microbiota transplant) is curative for recurrent C. difficile colitis.
- `connects-to` → **[Inflammatory Bowel Disease](../inflammatory-bowel-disease/README.md)** — The gut microbiome is central to inflammatory bowel disease: loss of diversity and a shift toward pro-inflammatory species breaches the mucosal barrier and provokes the immune attack of Crohn's and colitis—so the microbiome is both a driver and a treatment target.
- `connects-to` → **[Parkinson's Disease](../parkinsons-disease/README.md)** — The gut microbiome links to Parkinson's disease via the gut-brain axis: α-synuclein pathology may begin in the enteric nervous system and ascend the vagus, gut dysbiosis is common, and constipation precedes motor symptoms by years—Parkinson's may start in the gut.
- `connects-to` → **[Clostridioides difficile](../../../02-pathogen/02-bacteria/clostridioides-difficile/README.md)** — Clostridioides difficile infection is the disease of a disrupted microbiome: antibiotics wipe out protective gut flora, letting C. difficile overgrow, and restoring the microbiome by fecal transplant cures cases—proof that the microbial community is protective.
- `connects-to` → **[Large Intestine](../../06-organ/large-intestine/README.md)** — The gut microbiome lives mainly in the large intestine: trillions of anaerobes ferment dietary fiber there into short-chain fatty acids that nourish the colonic lining, so colonic health and microbial ecology are inseparable.
- `connects-to` → **[Intestinal Epithelium](../../05-tissue/intestinal-epithelium/README.md)** — The microbiome and intestinal epithelium are mutual keepers: bacterial short-chain fatty acids feed colonocytes and tighten the barrier, while a healthy epithelium confines microbes—dysbiosis breaches this, leaking endotoxin and driving inflammation.
- `connects-to` → **[Serotonin](../../03-molecular/serotonin/README.md)** — The gut microbiome shapes serotonin and the gut-brain axis: most of the body's serotonin is made by gut enterochromaffin cells, and microbial metabolites tune its production, linking the flora to motility, mood and bidirectional gut-brain signaling.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — The gut and liver are wired together: microbial products and bile acids flow up the portal vein, so a leaky, dysbiotic gut delivers bacterial endotoxin to the liver—fueling fatty liver and NASH—while the liver's bile in turn reshapes which microbes thrive.
- `connects-to` → **[Type 2 Diabetes](../type-2-diabetes/README.md)** — Gut microbes influence type 2 diabetes risk: fermentation makes short-chain fatty acids that improve insulin sensitivity, while dysbiosis raises inflammation and energy harvest—so the microbiome is a metabolic organ that helps tip the balance toward insulin resistance.
- `connects-to` → **[Rheumatoid Arthritis](../rheumatoid-arthritis/README.md)** — The gut microbiome is implicated in rheumatoid arthritis: dysbiosis (e.g., expansion of Prevotella) may prime mucosal immunity and citrullination that later attacks joints—supporting the idea that some autoimmunity begins at gut and other mucosal surfaces.
- `connects-to` → **[Regulatory T Cell](../../04-cellular/regulatory-t-cell/README.md)** — The gut microbiome teaches the immune system tolerance via regulatory T cells: bacterial short-chain fatty acids induce colonic Tregs that restrain inflammation, so a healthy microbiome supports immune balance and dysbiosis tips toward autoimmunity and allergy.
- `connects-to` → **[Dopamine](../../03-molecular/dopamine/README.md)** — Gut microbes influence dopamine and the gut-brain axis: bacteria produce dopamine and its precursors and shape its metabolism, contributing to mood and movement signaling—part of why the microbiome is implicated in Parkinson's and psychiatric disease.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — The gut-brain axis links the microbiome to depression: microbial metabolites and immune signals reaching the brain influence mood, and people with depression show altered gut flora—fueling interest in diet and probiotics as adjuncts.
- `connects-to` → **[GABA](../../03-molecular/gaba/README.md)** — Gut bacteria make GABA and talk to the brain: certain species synthesize this calming neurotransmitter (and others), part of the gut-brain axis through which the microbiome influences mood, anxiety, and stress alongside serotonin and dopamine.
- `connects-to` → **[Atherosclerosis](../atherosclerosis/README.md)** — The gut microbiome promotes atherosclerosis through TMAO: bacteria convert dietary choline and carnitine into TMAO, a metabolite that accelerates plaque and clotting—so what microbes make from red meat and eggs reaches the arteries.
- `connects-to` → **[Dendritic Cell](../../04-cellular/dendritic-cell/README.md)** — Dendritic cells read the gut microbiome to set immunity: they sample bacteria across the gut lining and decide between tolerance and attack, so the microbes present shape whether the immune system stays calm or inflames.
- `connects-to` → **[Brain](../../06-organ/brain/README.md)** — The gut microbiome talks to the brain: its bacteria make neurotransmitters and metabolites and signal along the vagus nerve, a gut-brain axis now linked to mood, behavior and neurodegeneration like Parkinson's.
- `connects-to` → **[Hydrogen](../../02-atomic/hydrogen/README.md)** — The gut microbiome runs on fermentation that makes gas: bacteria breaking down fiber release hydrogen and methane, the gases measured in breath tests to detect malabsorption and small-intestinal bacterial overgrowth.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Gut macrophages keep an uneasy peace with the microbiome: lining the bowel wall, they tolerate friendly bacteria while staying ready to attack invaders, so this restraint is central to keeping the trillions of microbes from triggering inflammation.
- `connects-to` → **[Small Intestine](../../06-organ/small-intestine/README.md)** — The small intestine normally holds few microbes; when they overgrow—SIBO—the result is bloating, gas and malabsorption, a disorder of the microbiome appearing in the wrong place.
- `connects-to` → **[T Helper Cell](../../04-cellular/t-helper-cell/README.md)** — The microbiome trains the immune system: some bacteria drive Th17 helper cells while others expand regulatory T cells, so the microbes tune the balance between defense and tolerance.
- `connects-to` → **[Sulfur](../../02-atomic/sulfur/README.md)** — Sulfate-reducing gut bacteria make hydrogen sulfide: this pungent gas, at high levels, is toxic to the colon lining and has been implicated in ulcerative colitis, a darker side of microbial metabolism.
- `connects-to` → **[Oxygen](../../02-atomic/oxygen/README.md)** — Oxygen's near-absence defines the gut's microbial world: the colon is anaerobic, and cells lining it burn oxygen to keep it that way, favoring the beneficial anaerobes — when oxygen leaks in, harmful facultative bacteria bloom in dysbiosis.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy reveals the microbial city up close: it shows bacterial flagella and pili, the dense biofilms clinging to the gut wall, and the protective mucus layer separating the microbes from the cells beneath.
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — The gut and kidney trade toxins: microbes turn dietary compounds into indoxyl sulfate, p-cresyl sulfate, and TMAO that the kidney must clear, so in kidney failure these gut-derived toxins build up and worsen cardiovascular damage.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — The microbiome talks to the brain: along the gut-brain axis it signals through the vagus nerve, microbial metabolites, and immune messengers, shaping mood, stress responses, and behavior — the basis of its links to depression and Parkinson's.
- `connects-to` → **[Dietary Fiber and Butyrate](../../../03-medicine/03-food/dietary-fiber/README.md)** — Fiber is the microbiome's fuel: colonic bacteria ferment indigestible dietary fiber into short-chain fatty acids like butyrate that feed the gut lining, calm inflammation, and reward a fiber-rich diet with a healthier microbial community.
- `connects-to` → **[Vitamin D (Calciferol)](../../../03-medicine/03-food/vitamin-d/README.md)** — Vitamin D and the gut flora shape each other: vitamin D and its receptor in the gut tune the microbial community and barrier, while the microbiome in turn influences vitamin D metabolism — a two-way tie linking sunlight, diet, and gut health.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — The flora tune antibodies beyond the gut: germ-free animals make poor antibody and respond weakly to vaccines, showing the microbiome calibrates the whole systemic humoral response, not just the secretory IgA bathing the mucosa.
- `connects-to` → **[Colorectal Cancer](../colorectal-cancer/README.md)** — Some microbes turn carcinogenic: a dysbiotic flora enriched in Fusobacterium nucleatum and toxin-making bacteria fosters colorectal cancer, inflaming the mucosa and damaging DNA, while a fiber-fed, butyrate-rich community protects against it.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — A gut-skin axis links the two surfaces: dysbiosis and a leaky gut feed inflammatory skin disease — acne, eczema, psoriasis, and rosacea — through immune and metabolite signals, which is why diet and probiotics are studied for the skin.
- `connects-to` → **[Estrogen](../../03-molecular/estrogen/README.md)** — Gut bacteria recycle the body's estrogen: the estrobolome — microbial enzymes that deconjugate estrogens excreted in bile so they re-enter circulation — sets how much estrogen the body keeps, linking dysbiosis to breast cancer and menopausal health.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — Microbes talk to the nervous system: bacterial metabolites and vagal signaling from the gut reach enteric and brain neurons, shaping mood, appetite and pain in the gut-brain axis that underlies the microbiome's effects on behavior.
- `connects-to` → **[NASH](../nash/README.md)** — A leaky gut inflames the liver: dysbiosis lets bacterial endotoxin reach the liver through the portal vein, fueling the inflammation that turns fatty liver into NASH — the gut-liver axis behind much metabolic liver disease.
- `connects-to` → **[Faecalibacterium prausnitzii](../../../02-pathogen/06-microbiome/faecalibacterium-prausnitzii/README.md)** — One species is a keystone of gut health: Faecalibacterium prausnitzii is a major butyrate producer that feeds the colon lining and calms inflammation, and its depletion is a consistent marker of dysbiosis in IBD and metabolic disease.
- `connects-to` → **[Escherichia coli](../../../02-pathogen/02-bacteria/escherichia-coli/README.md)** — Dysbiosis lets pathobionts bloom: commensal E. coli normally sits as a minor member, but expansions of proteobacteria like it mark a disturbed microbiome and can tip the balance toward inflammation and even cancer-promoting genotoxins.
- `connects-to` → **[Multiple Sclerosis](../multiple-sclerosis/README.md)** — The gut helps tune brain autoimmunity: microbiome composition shapes the regulatory and Th17 balance that drives multiple sclerosis, one of the clearest examples of the gut-immune-brain axis in an autoimmune disease far from the bowel.
- `connects-to` → **[Histamine](../../03-molecular/histamine/README.md)** — Some gut bacteria make histamine themselves: histamine-producing species decarboxylate dietary histidine in the lumen, and an overgrowth of them is thought to underlie histamine intolerance with its flushing, headaches and gut upset.
- `connects-to` → **[Asthma](../asthma/README.md)** — The gut shapes the airways through a gut-lung axis: early-life microbial diversity trains immune tolerance, and dysbiosis in infancy is linked to a higher risk of developing asthma and allergic airway disease.
- `connects-to` → **[Salmonella typhi](../../../02-pathogen/02-bacteria/salmonella-typhi/README.md)** — A healthy flora is a barrier against invaders: the resident microbiome provides colonization resistance, and antibiotics or dysbiosis that thin it leave the gut open to enteric pathogens like Salmonella to take hold.
- `connects-to` → **[Alzheimer's Disease](../alzheimers-disease/README.md)** — Dysbiosis may stoke the aging brain: gut bacteria shape systemic inflammation and amyloid metabolism along the gut-brain axis, and altered microbiomes are increasingly linked to the neuroinflammation of Alzheimer's disease.
- `connects-to` → **[Atopic Dermatitis](../atopic-dermatitis/README.md)** — The gut tunes the skin's immunity: a gut-skin axis means early-life dysbiosis biases the immune system toward allergy, and reduced microbial diversity in infancy is associated with developing atopic dermatitis.
- `connects-to` → **[Chronic Kidney Disease](../ckd/README.md)** — A gut-kidney axis runs both ways: dysbiosis lets the gut generate uremic toxins like indoxyl sulfate that injure the kidney, while failing kidneys in turn reshape the flora, a vicious cycle in chronic kidney disease.
- `connects-to` → **[Generalized Anxiety Disorder](../generalized-anxiety-disorder/README.md)** — The gut-brain axis shapes anxiety: microbial metabolites and vagal signaling modulate GABA and the stress axis, and dysbiosis is linked to heightened anxiety, with probiotics under study to ease it.
- `connects-to` → **[Autism Spectrum Disorder](../autism-spectrum-disorder/README.md)** — Microbes and behavior intertwine in development: GI symptoms are common in autism, and altered gut flora and its metabolites are implicated through the gut-brain axis in the behavioral phenotype.
- `connects-to` → **[Gout](../gout/README.md)** — Bacteria help handle the body's urate: the gut microbiome degrades a meaningful share of purines and uric acid, and dysbiosis that impairs this disposal contributes to the hyperuricemia behind gout.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — It lives in and shapes the gut it inhabits: the microbiome ferments fibre into short-chain fatty acids that feed colonocytes, metabolises bile acids and trains gut immunity, fundamentally shaping digestion.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — The microbes act as an endocrine organ: gut bacteria produce and modulate hormones, regulate the estrobolome that recycles oestrogen and shape insulin and appetite signalling through their metabolites.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — Gut and genital microbiomes are linked: the gut seeds the vaginal flora and shapes systemic oestrogen via the estrobolome, while birth and breastfeeding transfer the founding microbiome to the newborn.
- `connects-to` → **[Cardiovascular System](../cardiovascular-system/README.md)** — Its metabolites reach the heart and vessels: gut microbes generate TMAO that promotes atherosclerosis and short-chain fatty acids that help set blood pressure, linking the microbiome to cardiovascular risk.
- `connects-to` → **[Respiratory System](../respiratory-system/README.md)** — A gut-lung axis shapes the airways: the intestinal microbiome trains systemic and mucosal immunity, influencing susceptibility to respiratory infection and the development of asthma and allergy.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — A gut-bone axis tunes the skeleton: short-chain fatty acids, immune signalling and the absorption of calcium and vitamin K let the microbiome modulate bone density and osteoporosis risk.
- `connects-to` → **[Lymphatic System](../lymphatic-system/README.md)** — It trains the body's largest lymphoid mass: the gut wall holds gut-associated lymphoid tissue and Peyer's patches, which the microbiome shapes to educate systemic immunity from birth.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — A gut-skin axis reaches the surface: microbial metabolites and immune signalling link the gut microbiome to acne, rosacea, atopic dermatitis and psoriasis.
- `connects-to` → **[Renal System](../renal-system/README.md)** — A gut-kidney axis carries toxins: microbial metabolites such as indoxyl sulfate, p-cresyl sulfate and TMAO are uraemic toxins that accumulate and accelerate damage in chronic kidney disease.
- `connects-to` → **[Bifidobacterium longum](../../../02-pathogen/06-microbiome/bifidobacterium-longum/README.md)** — A keystone commensal: Bifidobacterium longum is an early-life and adult gut symbiont that ferments fibre, trains the immune system and is widely used as a probiotic.
- `connects-to` → **[Helicobacter pylori](../../../02-pathogen/02-bacteria/helicobacter-pylori/README.md)** — A disruptor at the top of the tract: Helicobacter pylori colonises the stomach, reshaping the gastric microbiome and acid environment, with both pathogenic and possibly protective effects.
- `connects-to` → **[Omega-3 fatty acids](../../../03-medicine/03-food/omega-3-fatty-acids/README.md)** — Diet reshapes the community: dietary fats including omega-3s alter microbial composition and the short-chain-fatty-acid and inflammatory output of the gut microbiome.
- `connects-to` → **[Checkpoint Inhibitors](../../../03-medicine/01-modern/13-cancer/checkpoint-inhibitors/README.md)** — It tunes cancer immunotherapy: the gut microbiome powerfully shapes response to checkpoint blockade — species like Akkermansia and Faecalibacterium predict who responds, and antibiotics or faecal transplant can blunt or restore efficacy.
- `connects-to` → **[Peyer's Patches](../../05-tissue/peyers-patches/README.md)** — It is sampled by gut immunity: Peyer's patches and their M cells continuously survey the microbiome, training the regulatory T cells and IgA responses that keep commensals tolerated while excluding pathogens.
- `connects-to` → **[Type 1 Diabetes](../type-1-diabetes/README.md)** — Early flora shape autoimmunity: reduced microbial diversity and altered short-chain-fatty-acid producers in infancy are linked to the development of type 1 diabetes, implicating the microbiome in the loss of immune tolerance to beta cells.
- `connects-to` → **[Hepatic Lobule](../../05-tissue/hepatic-lobule/README.md)** — The gut-liver axis: microbial metabolites and translocated endotoxin travel up the portal vein to the hepatic lobule, driving the inflammation and fat accumulation of NAFLD/NASH and shaping bile-acid metabolism.
- `connects-to` → **[Metformin](../../../03-medicine/01-modern/07-metabolic/metformin/README.md)** — The microbiome mediates its action: metformin reshapes gut bacterial composition, and that shift contributes both to its glucose-lowering effect and to the GI side effects that limit its use.
- `connects-to` → **[GvHD](../gvhd/README.md)** — It steers transplant immunity: after stem-cell transplant, loss of intestinal microbial diversity worsens gut graft-versus-host disease and mortality, making the microbiome a target for protecting the new immune system.
- `connects-to` → **[Epilepsy](../epilepsy/README.md)** — Diet, microbes and seizures: the ketogenic diet's anticonvulsant effect in drug-resistant epilepsy is partly mediated by gut-microbiome shifts that raise GABA and lower glutamate, a striking gut-brain link.
- `connects-to` → **[Ankylosing Spondylitis](../ankylosing-spondylitis/README.md)** — The gut-joint axis: subclinical gut inflammation and a distinct dysbiosis are central to ankylosing spondylitis, where HLA-B27 shapes a microbiome that helps drive the spondyloarthritis.
- `connects-to` → **[Sepsis](../sepsis/README.md)** — The gut as motor of sepsis: a depleted microbiome and leaky epithelium let gut bacteria translocate, and the dysbiosis of critical illness worsens multi-organ failure and mortality.
- `connects-to` → **[COVID-19 Disease](../covid-19-disease/README.md)** — Dysbiosis and COVID: the gut microbiome is altered in acute COVID-19 and shapes its severity, and persistent dysbiosis is implicated in the gastrointestinal and fatigue symptoms of long COVID.
- `connects-to` → **[Schizophrenia](../schizophrenia/README.md)** — Gut-brain axis in psychosis: microbiome alterations communicate with the brain via immune, metabolic and vagal routes and are increasingly implicated in schizophrenia, extending the gut's reach into psychotic illness.
- `connects-to` → **[HCC](../hcc/README.md)** — The gut-liver axis to cancer: dysbiosis and bacterial-product translocation through the portal vein inflame the liver and, via NASH and cirrhosis, contribute to hepatocellular carcinoma.
- `connects-to` → **[GLP-1](../../03-molecular/glp-1/README.md)** — SCFA-driven incretin: short-chain fatty acids produced by gut bacteria stimulate enteroendocrine GLP-1 secretion, linking the microbiome to appetite and glucose control.
- `connects-to` → **[B Cell](../../04-cellular/b-cell/README.md)** — Shaping mucosal antibodies: the gut microbiome drives the development of mucosal B cells and their secretory IgA, tuning the antibody repertoire that polices the gut.
- `connects-to` → **[Fibromyalgia](../fibromyalgia/README.md)** — Gut-brain pain axis: gut dysbiosis is increasingly implicated in fibromyalgia, with altered microbiome composition linked to its central pain and fatigue through the gut-brain axis.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — Th17 induction: segmented filamentous and other commensal bacteria drive intestinal Th17 cells and IL-17A, a microbiome-tuned arm of mucosal defence that, when dysregulated, fuels autoimmune and inflammatory disease.
- `connects-to` → **[BDNF](../../03-molecular/bdnf/README.md)** — Gut-brain signalling: germ-free and dysbiotic states alter hippocampal BDNF expression, one molecular link by which the microbiome shapes mood, anxiety and cognition along the gut-brain axis.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Metabolic crosstalk: microbial composition and short-chain fatty acids modulate leptin levels and central leptin sensitivity, tying the gut microbiome to appetite regulation and obesity.
- `connects-to` → **[TLR4](../../03-molecular/tlr4/README.md)** — TLR4 sensing of bacterial LPS is the principal microbiome-innate-immune interface, and leakage of LPS across a compromised gut barrier drives the "metabolic endotoxemia" that links dysbiosis to systemic, low-grade inflammation.
- `connects-to` → **[TGF-β](../../03-molecular/tgf-beta/README.md)** — Commensal bacteria and their short-chain fatty acids drive TGF-β-dependent differentiation of intestinal regulatory T cells—the mechanism by which the microbiome teaches the developing immune system tolerance to harmless food and microbial antigens.
- `connects-to` → **[NLRP3 Inflammasome](../../03-molecular/nlrp3-inflammasome/README.md)** — The NLRP3 and related inflammasomes both shape microbiota composition and are activated by microbial signals, a feedback loop whose disruption promotes the dysbiosis underlying inflammatory bowel disease and metabolic syndrome.
- `connects-to` → **[Cholesterol](../../03-molecular/cholesterol/README.md)** — Gut bacteria deconjugate and transform host bile acids made from cholesterol into secondary bile acids that signal through FXR and TGR5, a microbial arm of cholesterol and metabolic regulation linking the microbiome to host lipid handling.
- `connects-to` → **[IL-10](../../03-molecular/il-10/README.md)** — Commensal bacteria and their metabolites induce IL-10-producing regulatory T cells in the gut, the tolerogenic response that keeps the immune system from attacking the resident microbiota and whose failure underlies inflammatory bowel disease.
- `connects-to` → **[Acetylcholine](../../03-molecular/acetylcholine/README.md)** — Microbial metabolites signal to vagal afferents that use acetylcholine, a neural limb of the microbiota-gut-brain axis through which the microbiome influences mood, appetite and the cholinergic anti-inflammatory reflex.
- `connects-to` → **[HIF-1alpha](../../03-molecular/hif-1alpha/README.md)** — Microbial butyrate is consumed by colonocytes, lowering epithelial oxygen and stabilizing HIF-1α, a physiological hypoxia signal that maintains the gut barrier and the anaerobic niche favoring beneficial commensals.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — Microbial signals sensed through pattern-recognition receptors tune epithelial NF-κB activity, balancing antimicrobial defense against tolerance to the commensal microbiota that prevents inappropriate inflammation.
- `connects-to` → **[Wnt/beta-catenin](../../03-molecular/wnt-beta-catenin/README.md)** — The microbiota influences Wnt/β-catenin signaling in the intestinal crypt, modulating the stem-cell-driven regeneration that continuously renews the gut lining the microbiome inhabits.
- `connects-to` → **[MYD88](../../03-molecular/myd88/README.md)** — Microbiota-derived molecular patterns signal through TLRs (TLR4 mapped) and MyD88 to NF-κB (mapped), the core innate pathway by which the host senses and tolerates its commensal microbiome.
- `connects-to` → **[IFN-gamma](../../03-molecular/ifn-gamma/README.md)** — The microbiota calibrates the balance between IFN-γ-producing Th1 cells and regulatory T cells during the development of mucosal immunity, shaping systemic immune tone.
- `connects-to` → **[Ghrelin](../../03-molecular/ghrelin/README.md)** — The gut microbiome modulates appetite-regulating hormones including ghrelin (with leptin and GLP-1 mapped), part of the microbiome's influence on host energy balance and metabolism.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — Microbial metabolites such as short-chain fatty acids and amino acids signal through mTOR in host epithelial and immune cells, linking the gut microbiome to host nutrient sensing and immune-cell differentiation.
- `connects-to` → **[Interleukin-6](../../03-molecular/il-6/README.md)** — The gut microbiota tunes systemic IL-6 and inflammatory-cytokine tone, a route by which dysbiosis influences host inflammation beyond the gut.
- `connects-to` → **[NTRK](../../03-molecular/ntrk/README.md)** — The microbiome modulates BDNF and its TrkB receptor (NTRK) signaling in the gut-brain axis (BDNF already mapped), influencing enteric and central neural function.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Galectin-3 at the mucosal interface helps shape the host immune recognition of commensal and pathobiont bacteria, linking the microbiome to mucosal immunity.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — Microbiota-derived signals drive IL-6/IL-23-STAT3 activation that programs intestinal Th17 responses and epithelial homeostasis in the gut.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — Microbial and damage-associated cytosolic DNA engages cGAS-STING in the gut mucosa, coupling the microbiome to innate inflammatory tone.
- `connects-to` → **[SMAD4](../../03-molecular/smad4/README.md)** — TGF-β-SMAD signaling (TGF-β already mapped) mediates the microbial-metabolite-driven regulatory T-cell induction and epithelial homeostasis of the gut.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — IFN-STAT1 signaling links microbiota-shaped interferon tone to mucosal immune homeostasis and antimicrobial defense in the gut.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — FOXO transcription factors integrate microbial-metabolite and nutrient signals to regulate gut epithelial and immune homeostasis.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — Microbial metabolites and pattern-recognition signals feed into host PI3K-AKT signaling that governs the intestinal epithelial homeostasis shaped by the gut microbiome.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — ERK-MAPK signaling transduces the microbial and metabolite stimuli that modulate the epithelial and immune responses to the gut microbiome.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β integrates microbial pattern-recognition signaling to modulate the NF-κB inflammatory tone and Wnt-dependent epithelial renewal shaped by the gut microbiome.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK, activated by microbiota-derived short-chain fatty acids, links the gut microbiome to host energy metabolism.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — PI3K (PIK3CA)-AKT signaling (AKT already mapped) in the intestinal epithelium responds to the microbial signals of the gut microbiome.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — Autophagy in intestinal epithelial and immune cells shapes the host response to and tolerance of the gut microbiome.
- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — SRC-family kinase signaling participates in the epithelial-barrier junction dynamics at the host-microbiome interface of the gut.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — DNMT3A-mediated DNA methylation, shaped by microbial metabolites, participates in the epigenetic host-microbiome crosstalk of the gut.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-driven leukocyte recruitment participates in the mucosal immune responses shaped by the gut microbiome.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — CXCL12-CXCR4 signaling participates in the epithelial-immune interactions shaped by the gut microbiome.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — IL-1β-driven inflammation participates in the microbiome-immune signaling of the gut microbiome.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — IL-33 alarmin signaling participates in the mucosal immune responses shaped by the gut microbiome.
- `connects-to` → **[Insulin](../../03-molecular/insulin/README.md)** — Metabolic axis: microbiome composition and its short-chain fatty acids influence host insulin sensitivity and energy harvest, so dysbiosis is mechanistically linked to obesity and type 2 diabetes through altered insulin signalling.
- `connects-to` → **[Mu-opioid receptor](../../03-molecular/mu-opioid-receptor/README.md)** — Gut-brain visceral pain: the microbiome shapes enteric opioid signalling and visceral nociception, and germ-free or antibiotic-altered states change mu-opioid-mediated analgesia, part of the microbiome-gut-brain axis governing pain in disorders like IBS.
- `connects-to` → **[Omega-3 fatty acids](../../../03-medicine/03-food/omega-3-fatty-acids/README.md)** — Diet-microbiome interaction: omega-3 fatty acids shift microbiome composition toward anti-inflammatory, short-chain-fatty-acid-producing taxa, illustrating the reciprocal diet-microbiome relationship that modulates host inflammation.
- `connects-to` → **[Pancreas](../../06-organ/pancreas/README.md)** — Islet autoimmunity: the gut microbiome influences the development of type-1-diabetes (already mapped) by shaping mucosal immunity and permeability, linking microbial dysbiosis in early life to the islet autoimmunity of the pancreas.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Luminal iron competition: dietary and unabsorbed iron in the gut lumen shapes the microbiome, favouring some pathobionts, so iron supplementation can worsen dysbiosis, a nutrient-microbe interaction relevant to anaemia treatment.
- `connects-to` → **[Oxytocin](../../03-molecular/oxytocin/README.md)** — Microbe-driven oxytocin: specific commensals such as Lactobacillus reuteri raise systemic oxytocin through the vagus, influencing social behaviour and wound healing, a striking example of the microbiome-gut-brain axis reaching neuroendocrine signalling.
- `connects-to` → **[Nitric oxide](../../03-molecular/nitric-oxide/README.md)** — Luminal nitric oxide: bacterial and host nitric oxide in the gut lumen shapes the microbial community and regulates the mucosal blood flow, part of the chemical crosstalk between the microbiome and its epithelial habitat.
- `connects-to` → **[Melatonin](../../03-molecular/melatonin/README.md)** — Circadian microbiome: gut-derived melatonin and the host circadian clock impose a diurnal rhythm on the microbiome (serotonin already mapped), and disrupted sleep or shift work perturbs the community and its metabolic output.
- `connects-to` → **[Prostaglandins](../../03-molecular/prostaglandins/README.md)** — Mucosal barrier eicosanoids: prostaglandins maintain the mucosal barrier and blood flow that the microbiome modulates (short-chain fatty acids already GLP-1-mapped), part of how commensals and the epithelium co-regulate gut homeostasis.
- `connects-to` → **[Regulatory T cell](../../04-cellular/regulatory-t-cell/README.md)** — SCFA-induced Tregs: the short-chain fatty acids of the microbiome induce regulatory T cells (TGF-β and IL-10 already mapped) in the gut, a central mechanism by which the commensal community maintains immune tolerance.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Gut macrophage sampling: the intestinal macrophages continuously sample the microbiota (TLR4 already mapped) and maintain a tolerant, anti-inflammatory tone, part of the immune dialogue between the host and its commensals.
- `connects-to` → **[Obesity](../obesity/README.md)** — Microbiome and energy harvest: the composition of the gut microbiome influences energy harvest from the diet and the low-grade inflammation (leptin and adiponectin already mapped) of obesity, linking dysbiosis to metabolic disease.
- `connects-to` → **[TNF-alpha](../../03-molecular/tnf-alpha/README.md)** — Endotoxin-driven inflammation: the microbial LPS (TLR4 already mapped) drives the TNF of the gut and systemic inflammation, and the dysbiosis-driven TNF underlies much of the inflammation of gut and metabolic disease.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — Type-2 balance: the IL-4/Th2 (anti-helminth) arm (IL-10 already mapped) is shaped by the microbiome and balances the Th17 (IL-17 already mapped) and regulatory arms of the mucosal immune response to the commensals.
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — Anti-helminth type-2 arm: IL-13, with IL-4 (already mapped), mediates the type-2 (anti-helminth) response that both shapes and is shaped by the gut microbiome, part of the host-microbe immune dialogue.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Metabolic adipokine: resistin, with leptin and adiponectin (already mapped), is the adipokine of the microbiome-host metabolic (insulin already mapped) crosstalk and the dysbiosis-associated inflammation.
- `connects-to` → **[Plasma cell](../../04-cellular/plasma-cell/README.md)** — IgA plasma cells: the microbiome drives the expansion of the intestinal plasma cells that secrete the secretory IgA (already mapped) shaping the commensal community of the gut.
- `connects-to` → **[Hepcidin](../../03-molecular/hepcidin/README.md)** — Microbiome iron: the gut microbiome influences the intestinal iron absorption and competes for the luminal iron, interacting with the hepcidin (IL-6 already mapped) iron regulation.
- `connects-to` → **[Natural killer cell](../../04-cellular/natural-killer-cell/README.md)** — Microbiome-NK tuning: the gut microbiome (via its metabolites and the tonic signals) tunes the NK-cell (perforin already mapped) function and the systemic innate immunity.
- `connects-to` → **[Type I interferon](../../03-molecular/type-i-interferon/README.md)** — Tonic interferon priming: the commensal microbiome sets the tonic type-I interferon (cGAS-STING already mapped) that primes the antiviral and antitumour immunity of the host.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — Th1 induction: the microbiome-conditioned dendritic cells (already mapped) produce IL-12 to drive the Th1 (IFN-γ already mapped) arm of the gut-shaped systemic immunity.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Type-2/eosinophil arm: the microbiome shapes the IL-5 and the type-2 (IL-4 and IL-13 already mapped) immunity, tuning the gut eosinophils and the anti-parasite response of the host.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — Th17 induction: the segmented-filamentous and other commensal bacteria induce the IL-23/Th17 (IL-17 already mapped) axis of the gut-shaped systemic immunity.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — IgE regulation: the commensal microbiome restrains the baseline IgE (with IL-4 and IL-13 already mapped), and the dysbiosis/germ-free state raises the IgE and the allergic susceptibility.
- `connects-to` → **[Cytotoxic T cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Microbiome-shaped CD8: the commensal microbiome shapes the intraepithelial and systemic cytotoxic T cells (perforin pathway), and the dysbiosis alters the anti-tumour and anti-viral CD8 response.
- `connects-to` → **[Mast cell](../../04-cellular/mast-cell/README.md)** — Mast-cell crosstalk: the gut mast cells are educated by the commensal microbiome and, in dysbiosis, contribute to the barrier dysfunction and the type-2 (IgE already mapped) sensitisation of the gut-shaped immunity.
- `connects-to` → **[Bone marrow](../../05-tissue/bone-marrow/README.md)** — Gut-marrow axis: the commensal microbiome, via the microbial metabolites and signals, conditions the haematopoiesis and the myeloid output of the bone marrow, a systemic arm of the gut-shaped immunity.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Microbiome-primed complement: the commensal microbiome tunes the steady-state complement C3 expression (locally and systemically), part of the microbiome-shaped innate immunity of the host.
- `connects-to` → **[C5aR1](../../03-molecular/c5ar1/README.md)** — C5a receptor: the C5aR1 signalling (with the complement C3 already mapped) links the microbiome-tuned complement to the neutrophil recruitment of the intestinal mucosa.
- `connects-to` → **[Neutrophil](../../04-cellular/neutrophil/README.md)** — Microbiome-primed neutrophils: the commensal microbiome primes the neutrophils (the ageing and antimicrobial function), a systemic arm of the gut-shaped innate immunity.
- `connects-to` → **[TSLP](../../03-molecular/tslp/README.md)** — Epithelial barrier crosstalk: TSLP, secreted by intestinal epithelial cells, educates dendritic cells (already mapped) toward mucosal tolerance and acts as the alarmin linking barrier stress to the gut-microbiome immune interface.
- `connects-to` → **[Bradykinin](../../03-molecular/bradykinin/README.md)** — Kinin-microbiome axis: bradykinin, generated by the intestinal contact pathway, modulates intestinal permeability and lamina propria vasodilation, part of the kinin regulation of the gut-microbiome environment.
- `connects-to` → **[C1-Esterase Inhibitor](../../03-molecular/c1-esterase-inhibitor/README.md)** — Complement/kinin gate: C1-esterase inhibitor limits classical complement (complement C3 and C5aR1 already mapped) and bradykinin overactivation in the intestinal lumen, gating the inflammatory response to the commensal microbiome.
- `connects-to` → **[Erythropoietin](../../03-molecular/erythropoietin/README.md)** — Gut EPO axis: erythropoietin, produced by intestinal epithelium under hypoxic stress (HIF-1α already mapped), supports epithelial repair and modulates the enteric immune tone, linking gut oxygenation to the systemic haematopoietic response.
- `connects-to` → **[Periostin](../../03-molecular/periostin/README.md)** — Crypt stromal ECM: periostin, secreted by subepithelial fibroblasts of the intestinal crypt niche, maintains basement-membrane integrity and supports epithelial regeneration and stem-cell quiescence of the gut-microbiome ecosystem.
- `connects-to` → **[Complement C5](../../03-molecular/complement-c5/README.md)** — Terminal complement gating: complement C5 cleavage in the intestinal lamina propria generates C5a (C5aR1 already mapped) and C5b-9 MAC, amplifying inflammatory responses to dysbiosis and shaping the innate defence of the gut-microbiome ecosystem.
- `connects-to` → **[Testosterone](../../03-molecular/testosterone/README.md)** — GM testosterone: testosterone shapes gut-microbiome composition via regulatory-T-cell (already mapped) and B-cell (already mapped) modulation; androgen signalling suppresses IL-6 (already mapped) and TNF-α (already mapped) intestinal inflammation (IBD already mapped).
- `connects-to` → **[Prolactin](../../03-molecular/prolactin/README.md)** — GM prolactin: prolactin receptors on intestinal epithelium (already mapped) and liver (already mapped) modulate mucosal immunity; prolactin drives IL-6 (already mapped) production in mast cells (already mapped) and shapes regulatory-T-cell (already mapped) gut tolerance.
- `connects-to` → **[Vasopressin](../../03-molecular/vasopressin/README.md)** — GM vasopressin: vasopressin (ADH) acts on intestinal epithelium (already mapped) to modulate fluid transport and barrier integrity; vasopressin also suppresses IL-1β (already mapped) and TNF-α (already mapped) intestinal inflammation (IBD already mapped).
- `connects-to` → **[Selenium](../../02-atomic/selenium/README.md)** — GM selenium: selenoproteins in intestinal epithelium (already mapped) counter NF-κB (already mapped) oxidative stress; selenium deficiency impairs Akkermansia (already mapped) colonisation resistance and amplifies macrophage (already mapped) mucosal inflammation.
- `connects-to` → **[Iodine](../../02-atomic/iodine/README.md)** — GM iodine: intestinal lactoperoxidase (iodine-dependent) limits pathogen colonisation in the epithelium (already mapped); iodine deficiency amplifies NF-κB (already mapped) driven IL-6 (already mapped) mucosal inflammation and impairs macrophage (already mapped) homeostasis.
- `connects-to` → **[Sodium](../../02-atomic/sodium/README.md)** — GM sodium: high dietary sodium depletes Lactobacillus (already mapped) and amplifies IL-17A (already mapped) responses; sodium-driven NF-κB (already mapped) activation impairs intestinal epithelium (already mapped) barrier integrity and macrophage (already mapped) homeostasis.

## Pathology

### Dysbiosis

Dysbiosis — the pathological alteration of microbiome composition or function — is associated with multiple diseases:

**Inflammatory Bowel Disease (IBD — Crohn's and UC):**
- Reduced microbial diversity; loss of Faecalibacterium prausnitzii (primary butyrate producer)
- Increased Proteobacteria (E. coli, Bacteroides fragilis ETBF)
- CARD15/NOD2 mutations impair innate sensing of muramyl dipeptide → Paneth cell dysfunction → antimicrobial peptide deficiency → microbial invasion of epithelium
- FMT (fecal microbiota transplant) can achieve remission in UC; limited efficacy in Crohn's

**Clostridioides difficile Infection (CDI):**
- Antibiotics destroy colonization resistance → C. difficile spore germination (secondary bile acid loss)
- Toxin A (TcdA) and Toxin B (TcdB) → glucosylation of Rho GTPases → epithelial cytoskeletal disruption → pseudomembranous colitis
- FMT: ~90% efficacy for recurrent CDI — the highest-evidence microbiome intervention; now FDA-approved (RBX2660, SER-109)

**Metabolic Disease:**
- Turnbaugh et al. (2006) demonstrated that obesity-associated microbiomes have increased capacity for dietary energy harvest [^turnbaugh-2006-microbiome-nature]
- Reduced butyrate producers → impaired gut barrier → metabolic endotoxemia (low-level LPS translocation → chronic low-grade inflammation → insulin resistance)
- TMAO from Prevotella/Fusobacterium fermentation of dietary choline → enhanced platelet aggregation → cardiovascular risk

**Dysbiosis and CNS:**
- Reduced Lactobacillus and Bifidobacterium associated with depression and anxiety (bidirectional causality uncertain)
- Germ-free rodents show reduced neurogenesis, abnormal HPA axis reactivity, and social behavior deficits reversed by microbiome colonization

### Microbiome-Based Therapeutics

| Intervention | Target | Mechanism | Evidence |
|:---|:---|:---|:---|
| **FMT (Fecal Microbiota Transplant)** | Recurrent CDI; UC | Restoration of colonization resistance + diverse microbiome | ~90% CDI cure; ~30% UC remission |
| **Live biotherapeutics (SER-109)** | Recurrent CDI | Spore-forming Firmicutes consortium restores colonization resistance | Phase III: ~68% efficacy vs. ~58% placebo (ECOSPOR IV) |
| **Probiotics (Lactobacillus, Bifidobacterium)** | IBD, IBS, CDI prevention | Colonization resistance, mucosal IgA, Treg induction | Moderate evidence in UC, IBS; limited in Crohn's |
| **Dietary fiber (prebiotic)** | Metabolic disease, IBD | Selective enrichment of SCFA producers; butyrate → colonocyte health | Strong mechanistic; emerging clinical evidence |

[^sender-2016-microbiome-census]: Sender R, Fuchs S, Milo R. Revised Estimates for the Number of Human and Bacteria Cells in the Body. *Cell.* 2016;164(3):337-340. [doi:10.1016/j.cell.2016.01.013](https://doi.org/10.1016/j.cell.2016.01.013) · [PubMed 26824647](https://pubmed.ncbi.nlm.nih.gov/26824647/)
[^turnbaugh-2006-microbiome-nature]: Turnbaugh PJ et al. An obesity-associated gut microbiome with increased capacity for energy harvest. *Nature.* 2006;444(7122):1027-1031. [doi:10.1038/nature05414](https://doi.org/10.1038/nature05414) · [PubMed 17183312](https://pubmed.ncbi.nlm.nih.gov/17183312/)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
