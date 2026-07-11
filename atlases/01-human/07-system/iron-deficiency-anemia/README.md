---
schema: human-scale-entry/v1
id: iron-deficiency-anemia
name: Iron Deficiency Anemia
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-08
summary: "Iron deficiency anemia (IDA) is the world's most common nutritional disorder (~2B affected); chronic blood loss, inadequate intake, or malabsorption → depleted iron stores → microcytic hypochromic anemia; treat with ferrous sulfate orally or IV iron carboxymaltose."
aliases: ["IDA", "iron deficiency anemia", "iron deficiency anaemia", "iron-deficiency anemia", "microcytic anemia", "hypochromic anemia", "sideropenic anemia", "nutritional anemia"]
sources:
  - id: camaschella-2015-iron-deficiency
    type: peer-reviewed
    cite: "Camaschella C. Iron-deficiency anemia. N Engl J Med. 2015;372(19):1832-1843."
    doi: "10.1056/NEJMra1401038"
    pmid: "25946282"
    url: "https://doi.org/10.1056/NEJMra1401038"
  - id: who-ferritin-guideline-2020
    type: clinical-guideline
    cite: "World Health Organization. WHO guideline on use of ferritin concentrations to assess iron status in individuals and populations. WHO; 2020."
    url: "https://www.who.int/publications/i/item/9789240000124"
    accessed: "2026-06-08"
cross_links:
  - target: 01-human/03-molecular/ferroportin
    relation: connects-to
    note: "Ferroportin (SLC40A1) is the basolateral iron exporter on duodenal enterocytes; in IDA, hepcidin falls to near zero → FPN expression maximized → increased duodenal iron absorption and macrophage iron release; FPN is the final gateway of iron delivery to plasma."
  - target: 01-human/03-molecular/transferrin
    relation: connects-to
    note: "In IDA, serum iron falls → apotransferrin rises (TIBC elevated) → TSAT drops <20% → TFR1 upregulated on erythroid progenitors; reticulocyte Hgb (CHr) falls before morphological change; TSAT and ferritin together diagnose and stage iron deficiency."
  - target: 01-human/03-molecular/hepcidin
    relation: connects-to
    note: "IDA suppresses hepcidin to near zero via ERFE from erythroid progenitors and hypoxia signaling; low hepcidin → FPN stabilization → maximal duodenal iron absorption; hepcidin measurement distinguishes IDA (very low) from ACD (elevated) in overlapping cases."
  - target: 01-human/03-molecular/erythropoietin
    relation: connects-to
    note: "Iron deficiency limits erythropoiesis despite adequate EPO: iron-restricted erythroid progenitors cannot synthesize haem → EPO-resistant microcytic anemia; elevated EPO in IDA reflects compensatory drive; IV iron + ESA combined is more effective than either alone."
  - target: 01-human/03-molecular/hemoglobin
    relation: connects-to
    note: "IDA's defining feature is microcytic hypochromic anemia from insufficient haem synthesis; iron depletion → reduced haem → smaller, paler RBCs (↓MCV, ↓MCH); Hgb electrophoresis may show elevated HbA₂ if concurrent β-thalassaemia trait makes IDA appear milder."
  - target: 01-human/07-system/malaria
    relation: connects-to
    note: "Iron deficiency partially protective against P. falciparum (iron-restricted parasites grow less vigorously); iron supplementation in endemic areas should follow malaria treatment to avoid feeding parasites; IDA and malaria co-exist in sub-Saharan Africa."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Iron deficiency anaemia is, at root, a shortage of the element iron: each haemoglobin tetramer needs four iron atoms, so when absorbed iron (~1-2 mg/day) cannot keep up with loss or demand, stores empty (low ferritin) and haem synthesis stalls, yielding small, pale red cells."
  - target: 01-human/07-system/colorectal-cancer
    relation: connects-to
    note: "In a man or postmenopausal woman, unexplained iron deficiency anaemia is colorectal cancer until proven otherwise: a slow-bleeding right-sided tumour drips occult blood into the gut, so guidelines mandate colonoscopy to find the source before treating the anaemia."
  - target: 02-pathogen/02-bacteria/helicobacter-pylori
    relation: connects-to
    note: "Helicobacter pylori is an under-recognised cause of refractory iron deficiency: chronic gastritis lowers the stomach acid needed to reduce Fe³⁺ for absorption and the bacterium competes for iron, so eradicating H. pylori can reverse a deficiency that resisted oral iron."
  - target: 01-human/07-system/anemia-of-chronic-disease
    relation: connects-to
    note: "IDA and anemia of chronic disease are the two commonest anemias and key differentials: both can be microcytic with low serum iron, but IDA has low ferritin and high transferrin from true iron lack, while ACD has normal/high ferritin with hepcidin-locked iron; they often coexist."
  - target: 01-human/04-cellular/erythrocyte
    relation: connects-to
    note: "Iron deficiency starves erythropoiesis of heme: developing red cells undergo extra divisions, producing small (microcytic), pale (hypochromic) erythrocytes with raised red-cell distribution width; the low hemoglobin defines the anemia, and iron repletion restores red-cell size."
  - target: 01-human/07-system/thalassemia
    relation: connects-to
    note: "Iron-deficiency anemia and thalassemia trait are the classic microcytic-anemia differentials: both lower MCV, but IDA shows low ferritin and high RDW while thalassemia has normal/high iron and raised HbA2—crucially, giving iron to thalassemia trait misdiagnosed as IDA is harmful."
  - target: 01-human/07-system/inflammatory-bowel-disease
    relation: connects-to
    note: "Iron deficiency is the commonest systemic complication of inflammatory bowel disease: chronic gut bleeding plus impaired absorption and inflammation-raised hepcidin deplete iron, so IBD anemia is typically mixed iron-deficiency and chronic-disease anemia, often needing IV iron."
  - target: 01-human/07-system/gastric-cancer
    relation: connects-to
    note: "Iron deficiency anemia in an older adult is a red flag for GI malignancy including gastric cancer: chronic occult blood loss from an ulcerating tumor depletes iron, so unexplained iron-deficiency anemia mandates upper and lower endoscopy to exclude gastric or colorectal cancer."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "Heavy menstrual bleeding makes iron deficiency anemia the commonest anemia in women of reproductive age: monthly blood loss, plus the iron demands of pregnancy, outpaces dietary intake—so menorrhagia and pregnancy are leading causes of iron deficiency worldwide."
  - target: 01-human/07-system/mds
    relation: connects-to
    note: "Iron-deficiency anemia and MDS are opposite causes of anemia: IDA is a microcytic anemia from depleted iron that corrects with replacement, while MDS is a clonal marrow-failure anemia with normal or high iron—so iron studies and marrow biopsy distinguish them."
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "Iron deficiency is common and treatable in chronic kidney disease: both absolute iron loss and functional deficiency from inflammation-driven hepcidin limit erythropoiesis, so IV iron plus erythropoietin-stimulating agents are mainstays of CKD anemia management."
  - target: 01-human/07-system/heart-failure
    relation: connects-to
    note: "Iron deficiency is a key treatable comorbidity in heart failure—even without anemia: low iron impairs muscle and cardiac energetics, worsening symptoms and outcomes, so intravenous iron improves exercise capacity in iron-deficient HFrEF patients."
  - target: 01-human/05-tissue/bone-marrow
    relation: connects-to
    note: "Iron deficiency starves the bone marrow's red-cell factory: without iron, erythroblasts cannot make hemoglobin, so the marrow turns out small, pale (microcytic, hypochromic) red cells—the morphologic signature that distinguishes iron-deficiency anemia."
  - target: 01-human/06-organ/large-intestine
    relation: connects-to
    note: "The large intestine is a key clue in iron-deficiency anemia: in adults, occult bleeding from colonic lesions—especially colorectal cancer—is a leading cause, so unexplained iron deficiency in an older adult mandates colonoscopy to find the source."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "Iron-deficiency anemia is often a window into the digestive system: iron is absorbed in the duodenum, so malabsorption (celiac disease, gastric surgery) or chronic GI blood loss commonly causes it—making the gut the first place to investigate."
  - target: 01-human/06-organ/placenta
    relation: connects-to
    note: "Pregnancy strains iron balance through the placenta: the growing fetus and placenta draw heavily on maternal iron, so iron-deficiency anemia is common in pregnancy and, untreated, raises risks of preterm birth and low birth weight—prompting routine supplementation."
  - target: 01-human/04-cellular/platelet
    relation: connects-to
    note: "Iron deficiency oddly raises the platelet count: lacking iron, the marrow over-produces platelets (reactive thrombocytosis), so an unexplained high platelet count with microcytic anemia points to iron deficiency—and corrects once iron is replaced."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "Iron deficiency reaches the nervous system: iron is needed for myelin and neurotransmitter synthesis, so deficiency impairs attention and child development and causes restless legs syndrome—showing anemia harms neurons, not just red cells."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Most of the body's iron comes from macrophages recycling old red cells: they engulf senescent erythrocytes and return the iron via ferroportin, so this recycling—not diet—supplies most daily iron, and its disruption shapes both iron-deficiency and overload."
  - target: 01-human/02-atomic/copper
    relation: connects-to
    note: "Iron needs copper to move: copper-dependent enzymes (ceruloplasmin, hephaestin) oxidize iron so transferrin can carry it, so copper deficiency causes an anemia that looks like iron deficiency but won't respond to iron alone."
  - target: 01-human/06-organ/stomach
    relation: connects-to
    note: "The stomach gatekeeps iron absorption: acid frees dietary iron for uptake downstream, so atrophic gastritis, H. pylori, acid-blocking drugs or gastric surgery cause iron-deficiency anemia by impairing this first step."
  - target: 01-human/06-organ/small-intestine
    relation: connects-to
    note: "The small intestine is where iron deficiency is won or lost: the duodenum absorbs dietary iron, so celiac disease, bypass surgery or fast transit there cuts uptake and is a leading cause of iron-deficiency anemia."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "Iron deficiency ultimately means too little oxygen delivered: without iron, hemoglobin falls and blood carries less oxygen, producing the fatigue, breathlessness and even the odd cravings (pica) that drive patients to seek care."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "HIF senses the iron-oxygen shortfall and ramps up absorption: in the oxygen-starved gut lining, HIF-2alpha switches on the duodenal iron-uptake machinery, so this sensor links low iron and low oxygen to the body's effort to claw iron back."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "Severe iron-deficiency anemia overworks the heart: with too little hemoglobin to carry oxygen, the heart races and pumps harder, so prolonged anemia can enlarge it and tip toward high-output heart failure."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "Iron deficiency shows on the surface: pallor, brittle spoon-shaped nails (koilonychia), cracked mouth corners, and a smooth sore tongue are classic outward signs that point to the diagnosis."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "Iron deficiency weakens the immune T cells: iron is needed for lymphocytes to proliferate and function, so deficiency blunts cell-mediated immunity and can leave a person more prone to infection."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Unexplained iron deficiency sends doctors looking with light: endoscopy and colonoscopy hunt the gut for a bleeding source, and a marrow iron stain under the microscope confirms depleted stores."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "Zinc and iron compete for absorption: high doses of one interfere with the other in the gut, so supplements must be balanced lest correcting one mineral deepen deficiency of the other."
  - target: 01-human/05-tissue/intestinal-epithelium
    relation: connects-to
    note: "Iron enters through the gut lining: the duodenal epithelium absorbs dietary iron, so celiac disease or any damage to this lining causes iron deficiency that no amount of dietary iron can fix."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy shows iron starvation in the red cell: the erythrocytes come out small and pale with a widened central hollow, microcytic and hypochromic because too little iron is left to fill them with hemoglobin."
  - target: 01-human/06-organ/eye
    relation: connects-to
    note: "The eye reveals the anemia at a glance: pulling down the lower lid shows pale conjunctiva instead of healthy pink, a classic bedside sign, and severe deficiency can scatter retinal hemorrhages across the back of the eye."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "Iron is fuel for the brain: its lack dulls attention and, in children, impairs lasting cognitive development, while in adults it stirs the irresistible urge of restless legs and the strange cravings of pica."
  - target: 03-medicine/03-food/dietary-fiber
    relation: connects-to
    note: "Fiber-bound phytates blunt iron uptake: the phytic acid in whole grains, legumes, and nuts chelates non-heme iron in the gut, which is why heavily plant-based diets can struggle to maintain iron despite ample intake."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Calcium competes with iron at the gut wall: taken together, calcium-rich dairy and supplements inhibit iron absorption, so iron tablets are best spaced away from milk and calcium pills."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "Iron deficiency saps the muscles: beyond the oxygen-carrying hemoglobin, low iron starves the muscle's own myoglobin and aerobic enzymes, causing the exercise intolerance, weakness, and fatigue that mark the anemia."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "Autoimmunity is a hidden cause: antibodies in autoimmune atrophic gastritis and the anti-transglutaminase antibodies of celiac disease block iron absorption, so these antibody tests are part of working up unexplained iron deficiency."
  - target: 01-human/06-organ/thyroid
    relation: connects-to
    note: "The thyroid tangles with iron: hypothyroidism both causes its own anemia and drives the heavy menstrual bleeding that depletes iron, while iron deficiency in turn impairs thyroid hormone synthesis — a two-way tie checked together."
  - target: 01-human/07-system/gut-microbiome
    relation: connects-to
    note: "Iron and the gut flora shape each other: the microbiome aids iron handling, and unabsorbed oral iron feeds pathogenic gut bacteria and disturbs the flora, a reason supplementation can upset the gut and is being rethought."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "The liver is the body's iron bank and gatekeeper: it stores iron as ferritin and makes the hepcidin and transferrin that govern its traffic, so falling liver iron stores are the first stage of deficiency, well before the anemia shows."
  - target: 01-human/06-organ/spleen
    relation: connects-to
    note: "The spleen recycles the body's iron: its macrophages dismantle worn-out red cells and return their iron to the marrow, so this salvage loop normally dwarfs dietary intake and its failure or loss strains the iron balance."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "The lung can hide the bleeding: pulmonary hemosiderosis and Goodpasture trap iron in alveolar bleeds rather than recycling it, an occult internal loss that causes iron-deficiency anemia without any visible blood."
  - target: 01-human/07-system/esophageal-cancer
    relation: connects-to
    note: "Chronic iron lack can scar the swallowing tube: Plummer-Vinson syndrome pairs long-standing iron deficiency with esophageal webs and dysphagia, a premalignant state that raises the risk of esophageal squamous cell carcinoma."
  - target: 02-pathogen/04-parasites/giardia-lamblia
    relation: connects-to
    note: "A gut parasite can starve the body of iron: Giardia and other intestinal infections damage the absorptive lining and cause malabsorption, a common cause of iron deficiency where these infections are endemic."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "Defense needs iron too: iron is required for neutrophils' oxidative burst and proliferation, so iron deficiency subtly impairs these front-line cells — even as withholding iron is itself a defense against bacteria."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "The brain runs short on iron too: iron is needed for myelination and dopamine synthesis, so deficiency impairs cognition and attention in children and drives restless legs syndrome in adults."
  - target: 01-human/04-cellular/cardiomyocyte
    relation: connects-to
    note: "It strains and starves the heart muscle: chronic anemia forces a high-output state while iron deficiency itself impairs cardiomyocyte mitochondrial energetics, which is why iron repletion improves symptoms in heart failure."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "Low iron can paradoxically clot: iron deficiency triggers a reactive thrombocytosis and is a recognized risk factor for venous thromboembolism, including the unusual cerebral venous sinus thrombosis."
  - target: 01-human/07-system/endometrial-cancer
    relation: connects-to
    note: "Uterine bleeding bleeds the iron away: heavy or postmenopausal uterine bleeding from endometrial cancer is a classic cause of iron-deficiency anemia, and unexplained IDA in a postmenopausal woman prompts its search."
  - target: 01-human/07-system/bladder-cancer
    relation: connects-to
    note: "Blood lost in the urine drains the stores: chronic or intermittent hematuria from bladder cancer steadily depletes iron, so iron-deficiency anemia with microscopic hematuria warrants urologic evaluation."
  - target: 01-human/07-system/stroke
    relation: connects-to
    note: "Severe deficiency can reach the brain: iron deficiency drives reactive thrombocytosis and reduces oxygen delivery, and is a recognized — if uncommon — cause of ischemic stroke and cerebral venous thrombosis, especially in the young."
  - target: 01-human/07-system/attention-deficit-hyperactivity-disorder
    relation: connects-to
    note: "Low iron disturbs the developing brain: iron is a cofactor for dopamine synthesis, and deficiency in children is linked to attention problems, restless legs and the symptoms of ADHD, sometimes improving with repletion."
  - target: 01-human/07-system/wound-healing
    relation: connects-to
    note: "Iron-starved tissue repairs poorly: iron is needed for collagen cross-linking and oxygen delivery to the wound bed, so deficiency slows healing alongside the reduced perfusion of anemia."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "Iron shortage saps mood and energy: by impairing dopamine and serotonin synthesis and oxygen delivery, iron deficiency produces fatigue, poor concentration and depressive symptoms that can lift with treatment."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "Low iron shows on skin, nails and hair: iron deficiency causes pallor, brittle spoon-shaped koilonychia, diffuse hair loss, angular cheilitis and a smooth, sore glossitis of the tongue."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "Iron is double-edged for immunity: it is essential for lymphocyte and neutrophil function so deficiency impairs immune defence, yet the body deliberately withholds iron during infection to starve pathogens."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "Iron is needed to make thyroid hormone: thyroid peroxidase is a heme enzyme, so iron deficiency blunts thyroid-hormone synthesis and worsens hypothyroidism, tying the deficiency to the endocrine system."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "It forces the heart to overwork: to deliver oxygen with fewer red cells, iron-deficiency anaemia drives a high-output state with tachycardia and a flow murmur, and worsens angina in severe cases."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "It starves tissues of oxygen: reduced haemoglobin lowers oxygen-carrying capacity, producing exertional breathlessness and fatigue out of proportion to any lung disease."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "Kidney disease drives and complicates it: chronic kidney disease causes anaemia through low erythropoietin and functional iron deficiency, so intravenous iron is central to its management."
  - target: 03-medicine/01-modern/12-anti-inflammatory/ibuprofen
    relation: connects-to
    note: "NSAIDs erode the gut lining: ibuprofen and related drugs cause gastric and duodenal ulcers whose slow bleeding is a leading drug-induced cause of iron-deficiency anemia."
  - target: 03-medicine/01-modern/04-cardio/aspirin
    relation: connects-to
    note: "Antiplatelet therapy bleeds slowly: regular aspirin promotes chronic occult gastrointestinal blood loss, a frequent and easily missed source of iron-deficiency anemia in older adults."
  - target: 01-human/07-system/lymphatic-system
    relation: connects-to
    note: "The spleen recycles most of the body's iron: its reticuloendothelial macrophages salvage iron from worn-out red cells, and these stores are drawn down before the marrow runs short."
  - target: 01-human/07-system/sickle-cell-disease
    relation: connects-to
    note: "Opposite iron problems: unlike iron-deficiency anaemia, sickle cell is a haemolytic anaemia where repeated transfusion causes iron overload, so the two demand opposite iron management."
  - target: 01-human/07-system/pancreatic-cancer
    relation: connects-to
    note: "A red flag for hidden malignancy: unexplained iron-deficiency anaemia from occult gastrointestinal blood loss can signal pancreatic, ampullary or other gut cancers, prompting endoscopic and imaging work-up."
  - target: 02-pathogen/04-parasites/plasmodium-falciparum
    relation: connects-to
    note: "Malaria drains the blood and iron: falciparum malaria causes anaemia through haemolysis and inflammatory iron sequestration, and iron supplementation in endemic areas must be balanced against infection risk."
  - target: 01-human/05-tissue/hepatic-lobule
    relation: connects-to
    note: "The liver gauges iron need: hepatocytes in the liver lobule make hepcidin, the master iron-regulatory hormone, which is appropriately suppressed in iron deficiency to maximise dietary absorption and release of stored iron."
  - target: 03-medicine/01-modern/08-gi/omeprazole
    relation: connects-to
    note: "Acid suppression starves iron uptake: proton-pump inhibitors like omeprazole reduce the gastric acid needed to absorb dietary non-haem iron, a recognised contributor to iron-deficiency anaemia with long-term use."
  - target: 01-human/07-system/obesity
    relation: connects-to
    note: "Obesity causes a functional deficiency: chronic low-grade inflammation in obesity raises hepcidin, trapping iron and impairing its absorption, so iron deficiency is common despite adequate intake and stores."
  - target: 01-human/05-tissue/myocardium
    relation: connects-to
    note: "When anaemia strains the heart: severe iron deficiency forces a high-output state and, chronically, an anaemic cardiomyopathy, and iron itself is needed for cardiomyocyte energetics—worsening any heart failure."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "The body's oxygen sensor: the kidney detects the low oxygen delivery of anaemia and releases erythropoietin to drive red-cell production, the compensatory loop that iron deficiency tries to outrun."
  - target: 01-human/07-system/aplastic-anemia
    relation: connects-to
    note: "Two anaemias, opposite causes: iron-deficiency anaemia comes from too little iron for haemoglobin while aplastic anaemia comes from marrow failure—a key contrast when the blood count and iron studies don't add up."
  - target: 01-human/07-system/renal-cell-carcinoma
    relation: connects-to
    note: "Haematuria as a clue: renal cell carcinoma classically presents with haematuria that can cause iron-deficiency anaemia, one of the urological cancers uncovered during an unexplained-anaemia workup."
  - target: 01-human/07-system/rheumatoid-arthritis
    relation: connects-to
    note: "Two anaemias in one disease: rheumatoid arthritis causes anaemia of chronic disease and, through NSAID-induced gastrointestinal bleeding, a superimposed iron-deficiency anaemia."
  - target: 01-human/05-tissue/cardiac-conduction-system
    relation: connects-to
    note: "A fast, high-output heart: severe iron-deficiency anaemia drives compensatory tachycardia and palpitations through the cardiac conduction system, and can precipitate high-output heart failure."
  - target: 01-human/07-system/insomnia-disorder
    relation: connects-to
    note: "Restless legs and sleep: iron deficiency causes restless legs syndrome, a major driver of sleep-onset insomnia that improves with iron repletion—iron being a cofactor for dopamine synthesis in the brain."
  - target: 01-human/07-system/pulmonary-arterial-hypertension
    relation: connects-to
    note: "Iron and the pulmonary vasculature: iron deficiency is common in pulmonary arterial hypertension and independently worsens symptoms and outcomes, prompting trials of intravenous iron repletion."
  - target: 01-human/07-system/covid-19-disease
    relation: connects-to
    note: "Dysregulated iron in infection: COVID-19 disturbs iron metabolism with hyperferritinaemia and functional iron deficiency, and post-COVID anaemia and fatigue are increasingly recognised."
  - target: 01-human/03-molecular/von-willebrand-factor
    relation: connects-to
    note: "Bleeding-driven loss: von Willebrand disease, from defective von Willebrand factor, causes mucosal bleeding and heavy menstruation that is a common occult cause of iron-deficiency anaemia."
  - target: 01-human/07-system/hemophilia-a
    relation: connects-to
    note: "Chronic blood loss: recurrent bleeding in haemophilia A depletes body iron over time, a coagulation-disorder route to iron-deficiency anaemia distinct from the more common GI and menstrual losses."
  - target: 01-human/07-system/immune-thrombocytopenia
    relation: connects-to
    note: "Platelet-loss bleeding: the mucocutaneous and menstrual bleeding of immune thrombocytopenia can drain iron stores, layering iron-deficiency anaemia onto the underlying low platelet count."
  - target: 01-human/03-molecular/dopamine
    relation: connects-to
    note: "Restless legs and cognition: iron is a cofactor for tyrosine hydroxylase in dopamine synthesis, so iron deficiency disrupts dopaminergic signalling, causing restless legs syndrome and the attention deficits of low iron."
  - target: 01-human/03-molecular/atp
    relation: connects-to
    note: "Bioenergetic failure: iron is essential to the cytochromes and iron-sulfur clusters of oxidative phosphorylation, so iron deficiency impairs cellular ATP production, a molecular basis for the fatigue of the anaemia."
  - target: 01-human/03-molecular/thrombopoietin
    relation: connects-to
    note: "Reactive thrombocytosis: iron deficiency commonly raises platelet counts, with thrombopoietin and erythropoietin cross-signalling implicated in the reactive thrombocytosis that accompanies the anaemia."
  - target: 01-human/03-molecular/epas1
    relation: connects-to
    note: "Iron-absorption master switch: HIF-2α (EPAS1) is stabilised in the iron-starved duodenal enterocyte, where it transcriptionally upregulates DMT1 and ferroportin to maximise dietary iron absorption in iron deficiency."
  - target: 01-human/03-molecular/thyroid-hormones
    relation: connects-to
    note: "Iron-dependent thyroid synthesis: thyroid peroxidase is a haem enzyme, so iron deficiency impairs thyroid hormone synthesis, the basis for the overlap between iron-deficiency anaemia and hypothyroid symptoms like fatigue and cold intolerance."
  - target: 01-human/03-molecular/serotonin
    relation: connects-to
    note: "Monoamine cofactor: iron is a cofactor for tryptophan hydroxylase in serotonin synthesis, so iron deficiency lowers serotonergic signalling, contributing to the mood disturbance and fatigue that accompany the anaemia."
  - target: 01-human/03-molecular/norepinephrine
    relation: connects-to
    note: "Catecholamine synthesis: iron is the cofactor for tyrosine hydroxylase, the rate-limiting enzyme for noradrenaline and dopamine, so iron deficiency blunts catecholamine signalling — a basis for the poor concentration, fatigue and attention problems beyond the anaemia."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Absorption interaction: dietary calcium competitively inhibits non-heme iron uptake at the enterocyte, a clinically important interaction explaining why calcium supplements and dairy taken with meals can worsen iron deficiency."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "Hypoxic compensation: the tissue hypoxia of anaemia stabilises HIF and drives VEGF release, the angiogenic and erythropoietic compensatory response that the body mounts to the reduced oxygen-carrying capacity of iron-deficient blood."
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "Hepcidin suppression: the BMP-SMAD pathway (SMAD4) driving hepcidin transcription is downregulated when iron is scarce, lowering hepcidin to maximise iron absorption — the appropriate response distinguishing iron-deficiency anaemia from the anaemia of inflammation."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "Diagnostic contrast: IL-6 raises hepcidin to sequester iron, and its absence in true iron-deficiency anaemia keeps hepcidin low — the key mechanistic distinction from the iron-restricted anaemia of chronic disease."
  - target: 01-human/03-molecular/caspase-3
    relation: connects-to
    note: "Ineffective erythropoiesis: iron deficiency impairs erythroid maturation and increases caspase-3 apoptosis of developing erythroblasts, contributing to the ineffective erythropoiesis of severe iron deficiency."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "Hepcidin master switch: BMP/TGF-β-superfamily signalling through SMAD (SMAD4 already mapped) is the central hepatocyte pathway that transcriptionally tunes hepcidin to iron stores, governing the iron availability that iron-deficiency anemia depletes."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "Inflammatory iron restriction: IL-1β, alongside IL-6 (already mapped), induces hepcidin and the functional iron sequestration that compounds iron-deficiency anemia when inflammation coexists."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "Erythroid translation: mTOR couples iron and nutrient availability to protein synthesis in developing erythroblasts, so iron deficiency restrains mTOR-dependent translation and limits haemoglobinisation."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "The erythropoietin receptor signals through JAK2 (EPO mapped); iron-restricted erythropoiesis blunts the output of this pathway in iron deficiency anemia."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "EPO-driven PI3K-AKT signalling supports erythroid progenitor survival, a response constrained by the iron limitation of iron deficiency anemia."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "EPO-ERK-MAPK signalling drives erythroid progenitor proliferation, which iron restriction limits in iron deficiency anemia."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK energy sensing responds to the impaired mitochondrial respiration of iron-deficient cells, linking iron deficiency to the metabolic and exercise-intolerance symptoms of the anemia."
  - target: 01-human/03-molecular/nfe2l2
    relation: connects-to
    note: "NRF2 governs the heme- and iron-handling antioxidant response (including HO-1), shaping the cellular adaptation to the iron restriction of iron deficiency anemia."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "FOXO transcription factors integrate the oxidative and metabolic stress of iron-restricted erythropoiesis, modulating erythroid progenitor survival in iron deficiency anemia."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "IL-6-STAT3 signaling (IL-6 already mapped) induces hepcidin, the inflammatory axis that compounds iron restriction when inflammation accompanies iron deficiency anemia."
  - target: 01-human/03-molecular/cdk4-6
    relation: connects-to
    note: "CDK4/6-driven erythroid progenitor cell-cycle progression is constrained by the limited iron available for hemoglobinization in iron deficiency anemia."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "Class I PI3K (PIK3CA) signaling transduces the erythropoietin survival and proliferation signal in the iron-restricted erythroid progenitors of iron deficiency anemia (AKT already mapped)."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "GSK-3β modulates the erythropoietin and metabolic signaling in erythroid progenitors relevant to the impaired erythropoiesis of iron deficiency anemia."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "S100A8/A9 alarmins reflect the inflammatory context that can contribute to the functional iron restriction overlapping with iron deficiency anemia."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "IFN-STAT1 signaling links inflammatory stimuli to the hepcidin regulation and iron sequestration that overlaps with iron deficiency anemia."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Autophagy (including the erythroid mitophagy of reticulocyte maturation) participates in the erythropoiesis impaired in iron deficiency anemia."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC-family kinase signaling downstream of the EPO and cytokine receptors participates in the erythroid signaling disrupted in iron deficiency anemia."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "DNMT3A-mediated DNA methylation participates in the transcriptional regulation of erythroid differentiation relevant to iron deficiency anemia."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-family chemokine signaling participates in the bone-marrow niche and inflammatory interactions relevant to iron deficiency anemia."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "CXCL12-CXCR4 signaling participates in the erythroid bone-marrow-niche interactions relevant to iron deficiency anemia."
  - target: 01-human/03-molecular/kit
    relation: connects-to
    note: "KIT (stem-cell-factor receptor) signaling participates in the erythroid-progenitor proliferation and survival compromised in iron deficiency anemia."
  - target: 01-human/03-molecular/runx1
    relation: connects-to
    note: "RUNX1 transcription-factor activity participates in the erythroid and hematopoietic differentiation impaired in iron deficiency anemia."
  - target: 01-human/03-molecular/bcl-2
    relation: connects-to
    note: "BCL-2 anti-apoptotic signaling participates in the erythroblast survival (dependent on adequate iron and erythropoietin) relevant to iron deficiency anemia."
  - target: 01-human/03-molecular/notch
    relation: connects-to
    note: "NOTCH signaling participates in the hematopoietic-stem-cell and erythroid-progenitor regulation relevant to iron deficiency anemia."
  - target: 01-human/01-subatomic/proton
    relation: connects-to
    note: "Acid-dependent absorption: dietary ferric iron is reduced and absorbed only in the acidic duodenum, so gastric proton secretion is required for uptake, and achlorhydria or proton-pump inhibitors cause or worsen iron deficiency."
  - target: 01-human/03-molecular/estrogen
    relation: connects-to
    note: "Menstrual blood loss: heavy menstrual bleeding from the estrogen-driven endometrial cycle is the leading cause of iron deficiency anaemia in premenopausal women, and its cessation at menopause shifts the differential toward gastrointestinal loss."
  - target: 01-human/02-atomic/copper
    relation: connects-to
    note: "Copper-iron interaction: copper-dependent ferroxidases such as ceruloplasmin load iron onto transferrin (already mapped), so copper deficiency produces an iron-deficiency-like anaemia despite adequate iron, a key differential."
  - target: 01-human/03-molecular/testosterone
    relation: connects-to
    note: "Androgen erythropoiesis: testosterone stimulates erythropoiesis and suppresses hepcidin (already mapped), so androgens raise the baseline haemoglobin, and hypogonadism worsens the anaemia against which iron deficiency develops."
  - target: 01-human/03-molecular/progesterone
    relation: connects-to
    note: "Pregnancy iron demand: pregnancy, sustained by progesterone, sharply raises iron requirements for the expanding red-cell mass and the fetus, making iron-deficiency anaemia common in pregnancy and a target for routine supplementation."
  - target: 01-human/03-molecular/secretory-iga
    relation: connects-to
    note: "Coeliac malabsorption: coeliac disease is a common cause of iron malabsorption and refractory iron-deficiency anaemia, screened for with anti-transglutaminase IgA, linking the disorder to mucosal immunity of the small intestine (already mapped)."
  - target: 01-human/03-molecular/histamine
    relation: connects-to
    note: "Gastric acid and absorption: gastric acid, driven by histamine, reduces dietary iron to the absorbable ferrous form, so acid suppression with proton-pump inhibitors and atrophic gastritis impair iron absorption and can cause iron-deficiency anaemia."
  - target: 01-human/03-molecular/prostaglandins
    relation: connects-to
    note: "NSAID gastrointestinal bleeding: non-steroidal anti-inflammatory drugs block the protective mucosal prostaglandins, causing the gastric erosions and chronic occult gastrointestinal bleeding that are a common cause of iron-deficiency anaemia."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Metabolic interplay: iron deficiency alters leptin signalling and appetite, and it is associated with pica and restless-legs symptoms (dopamine already mapped), part of the systemic effects of iron-deficiency anaemia beyond the red cells."
  - target: 01-human/06-organ/stomach
    relation: connects-to
    note: "Gastric absorption and loss: the stomach's acid aids iron absorption — lost in atrophic gastritis, H. pylori and acid-suppressing drugs — and gastric erosions cause the occult bleeding that is a common source of iron-deficiency anaemia."
  - target: 01-human/02-atomic/copper
    relation: connects-to
    note: "Copper ferroxidases: copper is required by ceruloplasmin and hephaestin, the ferroxidases that oxidise iron for loading onto transferrin (already mapped), so copper deficiency causes an iron-deficiency-like anaemia despite adequate iron."
  - target: 01-human/07-system/colorectal-cancer
    relation: connects-to
    note: "Occult malignancy: iron-deficiency anaemia from occult gastrointestinal blood loss in an older adult mandates investigation for colorectal cancer, of which it is often the presenting sign."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Adipokine-iron crosstalk: adiponectin, with leptin (already mapped), participates in the adipokine crosstalk with the iron metabolism (hepcidin already mapped) and erythropoiesis altered in iron-deficiency anaemia."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), is part of the adipokine-inflammatory milieu that intersects with the iron and erythropoietic regulation in anaemia."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Dietary iron interaction: dietary calcium inhibits the absorption of non-haem iron in the duodenum, a dietary interaction relevant to the timing of the iron supplementation that treats iron-deficiency anaemia."
  - target: 01-human/05-tissue/bone-marrow
    relation: connects-to
    note: "Iron-restricted erythropoiesis: the bone-marrow erythropoiesis is limited by the iron supply (transferrin already mapped) in iron-deficiency anaemia, the iron-restricted erythropoiesis producing the microcytic red cells."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Iron-recycling macrophages: the macrophages recycle the iron from the senescent red cells (ferroportin already mapped); their iron release (blocked in the anaemia of chronic disease) is the differential of iron-deficiency anaemia."
  - target: 01-human/07-system/colorectal-cancer
    relation: connects-to
    note: "Occult-bleeding cause: the iron-deficiency anaemia from the chronic occult GI bleeding (transferrin already mapped) is a classic presenting sign of colorectal cancer, mandating investigation."
  - target: 01-human/04-cellular/hepatocyte
    relation: connects-to
    note: "Hepatic iron sensing: the hepatocytes produce the hepcidin (already mapped) and store the ferritin iron; the low iron of iron-deficiency anaemia suppresses the hepcidin to maximise the absorption."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Inflammation-restricted erythropoiesis: the IFN-γ of the T cells suppresses the erythropoiesis and, in the mixed iron-deficiency/inflammatory anaemias, compounds the iron-restricted erythropoiesis."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "Type-2 immune modulation: IL-4 and the type-2 arm modulate the macrophage (already mapped) iron handling that intersects with the iron-deficiency anaemia."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "Type-2 arm: IL-13, with IL-4 (already mapped), completes the type-2 immune arm whose M2-macrophage (already mapped) polarisation shapes the iron handling intersecting with iron-deficiency anaemia."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Eosinophil/hookworm arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), drives the eosinophil response to the hookworm and other parasites that are a leading cause of the iron-deficiency anaemia through gut blood loss."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 arm: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the inflammatory milieu that, in the mixed anaemias, compounds the iron-restricted erythropoiesis of iron-deficiency anaemia."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Antiparasite IgE: IgE, with the type-2 cytokines (IL-4, IL-5 and IL-13 already mapped), mediates the antiparasite response to the hookworm and other helminths whose gut blood loss is a leading global cause of iron-deficiency anaemia."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "Epithelial alarmin: IL-33, released by the injured gut epithelium, initiates the type-2 (IL-5 already mapped) antiparasite response to the intestinal helminths that cause the blood-loss iron-deficiency anaemia."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "Intestinal mast cells: the mast cells of the gut, armed by the IgE (already mapped), are effectors of the antiparasite type-2 response to the hookworm blood loss underlying much iron-deficiency anaemia."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Antiparasite complement: the complement C3 opsonises the intestinal helminths (hookworm), part of the innate mucosal defence against the blood-loss cause of much iron-deficiency anaemia."
  - target: 01-human/03-molecular/c5ar1
    relation: connects-to
    note: "C5a receptor: the C5aR1 signalling (with the complement C3 already mapped) recruits the myeloid cells to the intestinal mucosa in the antiparasite response underlying the blood-loss iron-deficiency anaemia."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "Mucosal antigen presentation: the dendritic cells of the gut present the helminth antigen to the T-helper (already mapped) cells, priming the type-2 antiparasite response to the hookworm blood loss of iron-deficiency anaemia."
  - target: 01-human/03-molecular/tslp
    relation: connects-to
    note: "Alarmin-gut axis: TSLP, from intestinal epithelium (already mapped) under the hookworm or blood-loss mucosal injury of iron-deficiency anaemia, primes mast cells (already mapped) and dendritic cells (already mapped) toward the type-2 antiparasite and mucosal repair response."
  - target: 01-human/03-molecular/bradykinin
    relation: connects-to
    note: "Kinin-GI axis: bradykinin, via the kallikrein-kinin system activated by the gastrointestinal mucosal (already mapped) injury and blood loss underlying iron-deficiency anaemia, amplifies the local vascular permeability and the inflammatory response."
  - target: 01-human/03-molecular/c1-esterase-inhibitor
    relation: connects-to
    note: "Complement brake: C1-esterase inhibitor regulates the classical-complement pathway (C3 and C5aR1 already mapped) and the contact system (bradykinin) activated during the mucosal injury and the hookworm-driven blood loss of iron-deficiency anaemia."
  - target: 01-human/03-molecular/factor-h
    relation: connects-to
    note: "Complement regulation: factor H limits alternative-pathway activation on erythrocytes (already mapped) and gut mucosal surfaces, regulating the complement (C3 and C5aR1 already mapped) contribution to the haemolytic and mucosal injury of iron-deficiency anaemia."
  - target: 01-human/03-molecular/complement-c5
    relation: connects-to
    note: "Terminal complement: complement C5 activation (with C3 already mapped) contributes to the intravascular haemolysis and the complement-driven mucosal injury that aggravate blood loss and iron malabsorption in iron-deficiency anaemia."
  - target: 01-human/03-molecular/periostin
    relation: connects-to
    note: "Gut-mucosal fibrosis matrix: periostin, from intestinal fibroblasts at the hookworm-damaged gut mucosa (intestinal-epithelium already mapped) of iron-deficiency anaemia, promotes type-2 mucosal repair and is a Th2/type-2 biomarker of the helminth response."
  - target: 01-human/03-molecular/prolactin
    relation: connects-to
    note: "IDA prolactin: prolactin, via PRLR on macrophages (already mapped) and intestinal epithelium (already mapped), modulates iron absorption and immune responses; hyperprolactinaemia amplifies the IL-6 (already mapped) and hepcidin (already mapped) axis of iron sequestration in IDA."
  - target: 01-human/03-molecular/oxytocin
    relation: connects-to
    note: "IDA oxytocin: oxytocin, via OXTR on macrophages (already mapped) and intestinal epithelium (already mapped), attenuates gut inflammation and promotes mucosal iron absorption; oxytocin reduces the IL-6 (already mapped) and hepcidin (already mapped) iron sequestration in IDA."
  - target: 01-human/03-molecular/vasopressin
    relation: connects-to
    note: "IDA vasopressin: vasopressin, via V2 receptors on macrophages (already mapped) and renal tubular cells, modulates fluid-iron homeostasis; elevated vasopressin in anaemic states amplifies the hepcidin (already mapped) and IL-6 (already mapped) iron-sequestration response of IDA."
  - target: 01-human/02-atomic/selenium
    relation: connects-to
    note: "IDA selenium: selenium, via GPx and NRF2 (already mapped) antioxidant systems, protects erythrocytes (already mapped) from oxidative haemolysis; selenium deficiency amplifies the hepcidin (already mapped) and IL-6 (already mapped) iron-sequestration response, worsening IDA."
  - target: 01-human/02-atomic/iodine
    relation: connects-to
    note: "IDA iodine: iodine-dependent thyroid hormones regulate erythropoietin (already mapped) and erythropoiesis in bone marrow (already mapped); hypothyroidism amplifies the hepcidin (already mapped) and IL-6 (already mapped) iron-withholding cascade of iron-deficiency anaemia."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "IDA sodium: sodium, via osmotic balance, regulates erythrocyte (already mapped) hydration and survival; dysregulated sodium amplifies oxidative stress in the transferrin (already mapped)-depleted and hepcidin (already mapped) iron-sequestered state of iron-deficiency anaemia."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "IDA magnesium: magnesium, as a cofactor for erythropoiesis enzymes in macrophages (already mapped) and erythrocytes (already mapped), supports haem synthesis; magnesium deficiency amplifies the hepcidin (already mapped) and IL-6 (already mapped) iron-sequestration cascade of IDA."
  - target: 01-human/02-atomic/potassium
    relation: connects-to
    note: "IDA potassium: potassium channels regulate erythrocyte (already mapped) hydration and mast-cell (already mapped) activation; potassium depletion amplifies the IL-6 (already mapped) and hepcidin (already mapped) iron-sequestration cascade of iron-deficiency anaemia."
  - target: 01-human/02-atomic/phosphorus
    relation: connects-to
    note: "IDA phosphorus: phosphorus, as ATP precursor in erythrocytes (already mapped) and macrophages (already mapped), supports haemoglobin synthesis; phosphorus deficiency amplifies the IL-6 (already mapped) and hepcidin (already mapped) iron-sequestration cascade of IDA."
  - target: 01-human/02-atomic/chloride
    relation: connects-to
    note: "IDA chloride: chloride via band-3 anion exchanger regulates erythrocyte (already mapped) membrane hydration; chloride dysregulation amplifies mast-cell (already mapped) and IL-6 (already mapped) and hepcidin (already mapped) iron-sequestration in iron-deficiency anaemia."
  - target: 01-human/02-atomic/carbon
    relation: connects-to
    note: "IDA carbon: carbon as backbone of haem (already mapped) and transferrin (already mapped) sustains erythropoiesis (already mapped); carbon depletion in reticulocytes (already mapped) and macrophages (already mapped) amplifies IL-6 (already mapped) anaemic cascade of IDA."
  - target: 01-human/02-atomic/hydrogen
    relation: connects-to
    note: "IDA hydrogen: hydrogen-ion acidosis in iron-deficient erythrocytes (already mapped) and macrophages (already mapped) impairs haemoglobin (already mapped) oxygen transport; hydrogen dysregulation amplifies NF-κB (already mapped) and EPO (already mapped) cascade of IDA."
  - target: 01-human/02-atomic/nitrogen
    relation: connects-to
    note: "IDA nitrogen: nitrogen in amino-acid precursors of haem (already mapped) and transferrin (already mapped) sustains erythropoiesis (already mapped); nitrogen deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and EPO (already mapped) cascade of IDA."
---

# Iron Deficiency Anemia

## Overview

**Iron deficiency anemia (IDA)** is the most prevalent nutritional deficiency and most common cause of anemia worldwide. The WHO estimates that approximately **2 billion people** — one-quarter of the global population — are affected by anemia, with IDA responsible for ~50% of cases. Globally, IDA contributes substantially to maternal and childhood mortality, impaired cognitive development, reduced work capacity, and adverse pregnancy outcomes [^camaschella-2015-iron-deficiency].

Iron deficiency exists on a spectrum from **depleted stores** (no clinical anemia) to **iron-restricted erythropoiesis** (partial functional deficit) to **frank IDA** (anaemia with characteristic morphological and laboratory changes):

**Stage 1 — Iron depletion:** Bone marrow iron stores absent (Prussian blue stain); serum ferritin falls (<12 ng/mL is diagnostic threshold; <30 ng/mL = probable depletion in inflammatory states); haemoglobin, TSAT, and MCV still normal.

**Stage 2 — Iron-restricted erythropoiesis:** Reticulocyte haemoglobin content (CHr) falls; elevated soluble TFR1 (sTFR); hypochromic reticulocytes; hepcidin falls to near zero; TSAT <20%; haemoglobin begins to decline; MCV still normal or borderline.

**Stage 3 — Frank IDA:** Haemoglobin below reference range; MCV <80 fL (microcytosis); MCH <27 pg (hypochromia); target cells, pencil cells, and anisocytosis on blood smear; TSAT <15%; serum ferritin <12 ng/mL; sTFR high [^who-ferritin-guideline-2020].

**Global epidemiology:**
- Most prevalent in: South Asia, sub-Saharan Africa, parts of Southeast Asia
- Highest-risk groups: premenopausal women (menstrual blood loss), infants and young children (rapid growth + low dietary iron density), pregnant women (dramatically increased demand), adolescent girls
- Estimated 1.2 billion people have IDA specifically (vs. 2 billion with anaemia of any cause)
- Leading cause of years lived with disability (YLDs) among nutritional disorders

## Structure

### Causes and pathophysiology of iron depletion

Iron balance is maintained at ~1–2 mg/day (absorbed = lost). IDA develops when this equilibrium is chronically disrupted:

**A. Chronic blood loss (most common cause in adults):**
- **Gastrointestinal:** peptic ulcer disease, colorectal cancer, colonic polyps, angiodysplasia, NSAIDs/aspirin-induced gastritis, hookworm infection (Necator/Ancylostoma, endemic in tropics)
- **Menstrual:** normal menstruation ~15 mg Fe/cycle; heavy menstrual bleeding (HMB, >80 mL/cycle) → 30-45 mg/cycle → depletes stores within months without dietary compensation
- **Occult GI bleeding:** most important to exclude in men and postmenopausal women — colonoscopy/upper endoscopy mandatory; colorectal cancer and gastric cancer classically present with IDA

**B. Inadequate dietary intake:**
- Strict vegetarian/vegan diets: non-haem plant iron has 5-10% bioavailability vs. 20-30% for haem iron
- Food insecurity, poverty: cereal-dominant diets low in iron-rich foods (meat, fish, legumes)
- Infants: cow's milk formula (low iron) or late introduction of iron-rich foods; human breast milk has low iron content but high bioavailability (~50%); premature infants especially vulnerable (missed third-trimester iron transfer)

**C. Malabsorption:**
- **Coeliac disease:** commonest cause of malabsorption-related IDA in developed countries; villous atrophy in proximal duodenum (highest FPN expression site) → severe IDA often presenting feature of coeliac disease
- **Helicobacter pylori gastritis:** reduces gastric acid (needed to reduce Fe³⁺ → Fe²⁺ for DMT1) and competes for iron; H. pylori eradication can reverse refractory IDA
- **Bariatric surgery:** gastric bypass diverts food past the duodenum → dramatically reduces iron absorption; ~50% of bariatric patients develop IDA within 2 years; IV iron often required indefinitely
- **Inflammatory bowel disease (IBD):** duodenal/jejunal inflammation (Crohn's) reduces absorption; concurrent ACD (hepcidin elevation) compounds deficiency
- **Achlorhydria:** proton pump inhibitor (PPI) long-term use, autoimmune gastritis → reduced Fe³⁺ reduction → impaired absorption

**D. Increased demand:**
- **Pregnancy:** fetal-placental iron requirement ~700 mg per pregnancy; average dietary iron insufficient; all pregnant women require iron supplementation
- **Rapid growth:** infancy, adolescence; increased RBC mass demands outpace intake
- **Intense endurance exercise:** "foot strike" haemolysis; increased GI losses; elevated hepcidin post-exercise transiently reduces absorption
- **Erythropoiesis-stimulating agents (ESA):** rHuEPO dramatically increases erythroid iron demand → functional IDA (iron needs outpace supply even if stores present); requires concurrent IV iron

## Function

### Why iron deficiency causes disease beyond anaemia

Iron is essential for:
1. **Haemoglobin synthesis:** 4 haem groups per tetramer require 4 Fe²⁺; haem synthesis is rate-limited by iron availability → microcytic, hypochromic RBCs
2. **Mitochondrial respiration:** cytochromes (Complex I-IV), Fe-S cluster proteins in the electron transport chain; iron deficiency → mitochondrial dysfunction → fatigue out of proportion to anaemia
3. **Thyroid peroxidase:** TPO requires haem; iron deficiency → impaired T4 synthesis → hypothyroid features may co-exist
4. **Ribonucleotide reductase:** iron-dependent rate-limiting enzyme in DNA synthesis → IDA affects rapidly proliferating cells (gut epithelium, immune cells)
5. **Neurotransmitter synthesis:** monoamine oxidase and tyrosine hydroxylase are iron-dependent → dopamine and serotonin deficiency → cognitive impairment, restless legs syndrome (RLS), mood changes
6. **Phagocyte function:** NADPH oxidase (NOX2) requires iron; IDA → impaired neutrophil oxidative burst → ↑ infection susceptibility

**Non-anaemic symptoms of iron deficiency (Stage 1-2):** Fatigue, cold intolerance, pica (craving for ice/clay/starch — particularly pagophagia/ice craving), koilonychia (spoon nails), angular cheilitis, glossitis, Plummer-Vinson syndrome (oesophageal webs + dysphagia), restless legs syndrome, cognitive impairment, reduced exercise tolerance, hair loss.

## Pathology

### Diagnosis

**Step 1 — Confirm anaemia:** CBC (Hb below gender-specific reference), MCV <80 fL, MCH <27 pg, RDW elevated (anisocytosis). Blood smear: hypochromic microcytes, target cells, pencil cells.

**Step 2 — Iron studies:**

| Test | IDA | ACD | ACD + IDA |
|:-----|:----|:----|:----------|
| Serum ferritin | <12 ng/mL (diagnostic); <30 ng/mL (probable) | ↑ (acute-phase reactant) | Normal (may be falsely normal in inflammation) |
| TSAT | <15-20% | Low-normal | Low |
| TIBC (transferrin) | ↑ | ↓ or normal | Variable |
| Serum iron | ↓ | ↓ | ↓ |
| sTFR (soluble TFR1) | ↑ (>28.1 nmol/L) | Normal | ↑ |
| sTFR/log ferritin index | >2 (IDA likely) | <1 | >2 |
| Reticulocyte Hgb (CHr) | <28 pg | <28 pg | <28 pg |
| Hepcidin | Very low (<3 ng/mL) | Elevated | Intermediate |

**Key diagnostic challenge:** Ferritin is an acute-phase reactant — rises during infection, inflammation, or malignancy even when iron stores are depleted. **Threshold adjustments:** ferritin <30 ng/mL = probable IDA when CRP <5 mg/L; ferritin <70 ng/mL = probable IDA when CRP >5 mg/L (WHO 2020). sTFR/log ferritin ratio (>2 suggests IDA component) is least affected by inflammation.

**Step 3 — Identify the cause:** Occult GI blood loss is mandatory investigation in men and postmenopausal women. Coeliac serology (TTG-IgA, total IgA), H. pylori testing, dietary history, menstrual history. Colonoscopy + OGD for any adult with unexplained IDA — colorectal cancer must be excluded.

### Treatment [^camaschella-2015-iron-deficiency]

**1. Oral iron:**
- **Ferrous sulfate** (65 mg elemental Fe per 325 mg tablet): standard of care; 1-2 tablets daily fasting for maximal absorption; side effects: nausea, constipation, black stools
- **Ferrous fumarate, ferrous gluconate:** lower elemental iron but better tolerability
- **Dosing principle:** Once daily is as effective as twice daily and reduces side effects (hepcidin spike 6-8 h post-dose blunts afternoon dose absorption → alternate days is equally effective)
- **Duration:** 3-6 months after Hb normalizes to replete stores; confirm with repeat ferritin >30 ng/mL

**2. Intravenous iron:**
- **Indications:** Oral iron intolerance; malabsorption (coeliac, bariatric surgery, IBD); ongoing losses exceed oral absorption capacity; pre-operative anaemia optimization; CKD/ESA therapy; pregnancy (2nd/3rd trimester when oral fails)
- **Formulations:**
  - **Ferric carboxymaltose (Ferinject):** 500-1000 mg as single infusion (15 min); minimal anaphylaxis risk; can give 1000 mg dose → fewest infusions; FDA-approved
  - **Iron sucrose (Venofer):** 200 mg per infusion × 3-5 doses; well-tolerated; preferred in dialysis patients
  - **Low-molecular-weight iron dextran:** large doses possible (total dose infusion); higher anaphylaxis rate
  - **Ferric gluconate:** lower dose per infusion; safe; multiple infusions needed
- **Response:** Reticulocytosis within 3-5 days; Hb rise 1-2 g/dL per week; normalize stores within 2-3 months
- **Caution:** Hypophosphataemia after ferric carboxymaltose (FGFR-mediated FGF23 elevation → phosphaturia); monitor serum phosphate; rare anaphylaxis with dextran preparations

**3. Dietary counselling:**
- Increase haem iron: red meat, fish, poultry (20-30% bioavailability)
- Enhance non-haem iron absorption: concurrent vitamin C (ascorbate reduces Fe³⁺ → Fe²⁺)
- Avoid: tea, coffee, calcium supplements, phytates (whole grains, legumes) — all inhibit non-haem iron absorption

**4. Treat the underlying cause:** H. pylori eradication → ~90% Hb improvement in H. pylori-associated IDA; coeliac diet → normalizes duodenal absorption; NSAID/aspirin discontinuation or switch to PPI cover; colonoscopy for polyp/cancer removal.

**Special situations:**
- **Pregnancy:** IV iron ferric carboxymaltose after 12 weeks preferred over oral iron if Hb <9-10 g/dL or intolerance; targets Hb >11 g/dL for delivery
- **IBD:** IV iron preferred (oral worsens bowel disease); ferric carboxymaltose 500-1000 mg initial dose
- **Heart failure:** IV iron improves exercise capacity and quality of life even without anaemia in HF patients with ferritin <100 ng/mL or TSAT <20% (FAIR-HF, AFFIRM-AHF trials)
- **Pre-operative:** Oral or IV iron 4-6 weeks pre-op; IV iron 1-2 weeks pre-op for urgent surgery; targets Hb >13 g/dL males, >12 g/dL females before elective major surgery

## Connections

- `connects-to` → **[Ferroportin](../../03-molecular/ferroportin/README.md)** — Ferroportin (SLC40A1) is the basolateral iron exporter on duodenal enterocytes; in IDA, hepcidin falls to near zero → FPN expression maximized → increased duodenal iron absorption and macrophage iron release; FPN is the final gateway of iron delivery to plasma.
- `connects-to` → **[Transferrin](../../03-molecular/transferrin/README.md)** — In IDA, serum iron falls → apotransferrin rises (TIBC elevated) → TSAT drops <20% → TFR1 upregulated on erythroid progenitors; reticulocyte Hgb (CHr) falls before morphological change; TSAT and ferritin together diagnose and stage iron deficiency.
- `connects-to` → **[Hepcidin](../../03-molecular/hepcidin/README.md)** — IDA suppresses hepcidin to near zero via ERFE from erythroid progenitors and hypoxia signaling; low hepcidin → FPN stabilization → maximal duodenal iron absorption; hepcidin measurement distinguishes IDA (very low) from ACD (elevated) in overlapping cases.
- `connects-to` → **[Erythropoietin](../../03-molecular/erythropoietin/README.md)** — Iron deficiency limits erythropoiesis despite adequate EPO: iron-restricted erythroid progenitors cannot synthesize haem → EPO-resistant microcytic anemia; elevated EPO in IDA reflects compensatory drive; IV iron + ESA combined is more effective than either alone.
- `connects-to` → **[Hemoglobin](../../03-molecular/hemoglobin/README.md)** — IDA's defining feature is microcytic hypochromic anemia from insufficient haem synthesis; iron depletion → reduced haem → smaller, paler RBCs (↓MCV, ↓MCH); Hgb electrophoresis may show elevated HbA₂ if concurrent β-thalassaemia trait makes IDA appear milder.
- `connects-to` → **[Malaria](../malaria/README.md)** — Iron deficiency partially protective against P. falciparum (iron-restricted parasites grow less vigorously); iron supplementation in endemic areas should follow malaria treatment to avoid feeding parasites; IDA and malaria co-exist in sub-Saharan Africa.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Iron deficiency anaemia is, at root, a shortage of the element iron: each haemoglobin tetramer needs four iron atoms, so when absorbed iron (~1-2 mg/day) cannot keep up with loss or demand, stores empty (low ferritin) and haem synthesis stalls, yielding small, pale red cells.
- `connects-to` → **[Colorectal Cancer](../colorectal-cancer/README.md)** — In a man or postmenopausal woman, unexplained iron deficiency anaemia is colorectal cancer until proven otherwise: a slow-bleeding right-sided tumour drips occult blood into the gut, so guidelines mandate colonoscopy to find the source before treating the anaemia.
- `connects-to` → **[Helicobacter pylori](../../../02-pathogen/02-bacteria/helicobacter-pylori/README.md)** — Helicobacter pylori is an under-recognised cause of refractory iron deficiency: chronic gastritis lowers the stomach acid needed to reduce Fe³⁺ for absorption and the bacterium competes for iron, so eradicating H. pylori can reverse a deficiency that resisted oral iron.
- `connects-to` → **[Anemia of Chronic Disease](../anemia-of-chronic-disease/README.md)** — IDA and anemia of chronic disease are the two commonest anemias and key differentials: both can be microcytic with low serum iron, but IDA has low ferritin and high transferrin from true iron lack, while ACD has normal/high ferritin with hepcidin-locked iron; they often coexist.
- `connects-to` → **[Erythrocyte](../../04-cellular/erythrocyte/README.md)** — Iron deficiency starves erythropoiesis of heme: developing red cells undergo extra divisions, producing small (microcytic), pale (hypochromic) erythrocytes with raised red-cell distribution width; the low hemoglobin defines the anemia, and iron repletion restores red-cell size.
- `connects-to` → **[Thalassemia](../thalassemia/README.md)** — Iron-deficiency anemia and thalassemia trait are the classic microcytic-anemia differentials: both lower MCV, but IDA shows low ferritin and high RDW while thalassemia has normal/high iron and raised HbA2—crucially, giving iron to thalassemia trait misdiagnosed as IDA is harmful.
- `connects-to` → **[Inflammatory Bowel Disease](../inflammatory-bowel-disease/README.md)** — Iron deficiency is the commonest systemic complication of inflammatory bowel disease: chronic gut bleeding plus impaired absorption and inflammation-raised hepcidin deplete iron, so IBD anemia is typically mixed iron-deficiency and chronic-disease anemia, often needing IV iron.
- `connects-to` → **[Gastric Cancer](../gastric-cancer/README.md)** — Iron deficiency anemia in an older adult is a red flag for GI malignancy including gastric cancer: chronic occult blood loss from an ulcerating tumor depletes iron, so unexplained iron-deficiency anemia mandates upper and lower endoscopy to exclude gastric or colorectal cancer.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — Heavy menstrual bleeding makes iron deficiency anemia the commonest anemia in women of reproductive age: monthly blood loss, plus the iron demands of pregnancy, outpaces dietary intake—so menorrhagia and pregnancy are leading causes of iron deficiency worldwide.
- `connects-to` → **[Myelodysplastic Syndromes](../mds/README.md)** — Iron-deficiency anemia and MDS are opposite causes of anemia: IDA is a microcytic anemia from depleted iron that corrects with replacement, while MDS is a clonal marrow-failure anemia with normal or high iron—so iron studies and marrow biopsy distinguish them.
- `connects-to` → **[Chronic Kidney Disease](../ckd/README.md)** — Iron deficiency is common and treatable in chronic kidney disease: both absolute iron loss and functional deficiency from inflammation-driven hepcidin limit erythropoiesis, so IV iron plus erythropoietin-stimulating agents are mainstays of CKD anemia management.
- `connects-to` → **[Heart Failure](../heart-failure/README.md)** — Iron deficiency is a key treatable comorbidity in heart failure—even without anemia: low iron impairs muscle and cardiac energetics, worsening symptoms and outcomes, so intravenous iron improves exercise capacity in iron-deficient HFrEF patients.
- `connects-to` → **[Bone Marrow](../../05-tissue/bone-marrow/README.md)** — Iron deficiency starves the bone marrow's red-cell factory: without iron, erythroblasts cannot make hemoglobin, so the marrow turns out small, pale (microcytic, hypochromic) red cells—the morphologic signature that distinguishes iron-deficiency anemia.
- `connects-to` → **[Large Intestine](../../06-organ/large-intestine/README.md)** — The large intestine is a key clue in iron-deficiency anemia: in adults, occult bleeding from colonic lesions—especially colorectal cancer—is a leading cause, so unexplained iron deficiency in an older adult mandates colonoscopy to find the source.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — Iron-deficiency anemia is often a window into the digestive system: iron is absorbed in the duodenum, so malabsorption (celiac disease, gastric surgery) or chronic GI blood loss commonly causes it—making the gut the first place to investigate.
- `connects-to` → **[Placenta](../../06-organ/placenta/README.md)** — Pregnancy strains iron balance through the placenta: the growing fetus and placenta draw heavily on maternal iron, so iron-deficiency anemia is common in pregnancy and, untreated, raises risks of preterm birth and low birth weight—prompting routine supplementation.
- `connects-to` → **[Platelet](../../04-cellular/platelet/README.md)** — Iron deficiency oddly raises the platelet count: lacking iron, the marrow over-produces platelets (reactive thrombocytosis), so an unexplained high platelet count with microcytic anemia points to iron deficiency—and corrects once iron is replaced.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — Iron deficiency reaches the nervous system: iron is needed for myelin and neurotransmitter synthesis, so deficiency impairs attention and child development and causes restless legs syndrome—showing anemia harms neurons, not just red cells.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Most of the body's iron comes from macrophages recycling old red cells: they engulf senescent erythrocytes and return the iron via ferroportin, so this recycling—not diet—supplies most daily iron, and its disruption shapes both iron-deficiency and overload.
- `connects-to` → **[Copper](../../02-atomic/copper/README.md)** — Iron needs copper to move: copper-dependent enzymes (ceruloplasmin, hephaestin) oxidize iron so transferrin can carry it, so copper deficiency causes an anemia that looks like iron deficiency but won't respond to iron alone.
- `connects-to` → **[Stomach](../../06-organ/stomach/README.md)** — The stomach gatekeeps iron absorption: acid frees dietary iron for uptake downstream, so atrophic gastritis, H. pylori, acid-blocking drugs or gastric surgery cause iron-deficiency anemia by impairing this first step.
- `connects-to` → **[Small Intestine](../../06-organ/small-intestine/README.md)** — The small intestine is where iron deficiency is won or lost: the duodenum absorbs dietary iron, so celiac disease, bypass surgery or fast transit there cuts uptake and is a leading cause of iron-deficiency anemia.
- `connects-to` → **[Oxygen](../../02-atomic/oxygen/README.md)** — Iron deficiency ultimately means too little oxygen delivered: without iron, hemoglobin falls and blood carries less oxygen, producing the fatigue, breathlessness and even the odd cravings (pica) that drive patients to seek care.
- `connects-to` → **[HIF-1alpha](../../03-molecular/hif-1alpha/README.md)** — HIF senses the iron-oxygen shortfall and ramps up absorption: in the oxygen-starved gut lining, HIF-2alpha switches on the duodenal iron-uptake machinery, so this sensor links low iron and low oxygen to the body's effort to claw iron back.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — Severe iron-deficiency anemia overworks the heart: with too little hemoglobin to carry oxygen, the heart races and pumps harder, so prolonged anemia can enlarge it and tip toward high-output heart failure.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — Iron deficiency shows on the surface: pallor, brittle spoon-shaped nails (koilonychia), cracked mouth corners, and a smooth sore tongue are classic outward signs that point to the diagnosis.
- `connects-to` → **[T Helper Cell](../../04-cellular/t-helper-cell/README.md)** — Iron deficiency weakens the immune T cells: iron is needed for lymphocytes to proliferate and function, so deficiency blunts cell-mediated immunity and can leave a person more prone to infection.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Unexplained iron deficiency sends doctors looking with light: endoscopy and colonoscopy hunt the gut for a bleeding source, and a marrow iron stain under the microscope confirms depleted stores.
- `connects-to` → **[Zinc](../../02-atomic/zinc/README.md)** — Zinc and iron compete for absorption: high doses of one interfere with the other in the gut, so supplements must be balanced lest correcting one mineral deepen deficiency of the other.
- `connects-to` → **[Intestinal Epithelium](../../05-tissue/intestinal-epithelium/README.md)** — Iron enters through the gut lining: the duodenal epithelium absorbs dietary iron, so celiac disease or any damage to this lining causes iron deficiency that no amount of dietary iron can fix.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy shows iron starvation in the red cell: the erythrocytes come out small and pale with a widened central hollow, microcytic and hypochromic because too little iron is left to fill them with hemoglobin.
- `connects-to` → **[Eye](../../06-organ/eye/README.md)** — The eye reveals the anemia at a glance: pulling down the lower lid shows pale conjunctiva instead of healthy pink, a classic bedside sign, and severe deficiency can scatter retinal hemorrhages across the back of the eye.
- `connects-to` → **[Brain](../../06-organ/brain/README.md)** — Iron is fuel for the brain: its lack dulls attention and, in children, impairs lasting cognitive development, while in adults it stirs the irresistible urge of restless legs and the strange cravings of pica.
- `connects-to` → **[Dietary Fiber and Butyrate](../../../03-medicine/03-food/dietary-fiber/README.md)** — Fiber-bound phytates blunt iron uptake: the phytic acid in whole grains, legumes, and nuts chelates non-heme iron in the gut, which is why heavily plant-based diets can struggle to maintain iron despite ample intake.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Calcium competes with iron at the gut wall: taken together, calcium-rich dairy and supplements inhibit iron absorption, so iron tablets are best spaced away from milk and calcium pills.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — Iron deficiency saps the muscles: beyond the oxygen-carrying hemoglobin, low iron starves the muscle's own myoglobin and aerobic enzymes, causing the exercise intolerance, weakness, and fatigue that mark the anemia.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — Autoimmunity is a hidden cause: antibodies in autoimmune atrophic gastritis and the anti-transglutaminase antibodies of celiac disease block iron absorption, so these antibody tests are part of working up unexplained iron deficiency.
- `connects-to` → **[Thyroid Gland](../../06-organ/thyroid/README.md)** — The thyroid tangles with iron: hypothyroidism both causes its own anemia and drives the heavy menstrual bleeding that depletes iron, while iron deficiency in turn impairs thyroid hormone synthesis — a two-way tie checked together.
- `connects-to` → **[Gut Microbiome](../gut-microbiome/README.md)** — Iron and the gut flora shape each other: the microbiome aids iron handling, and unabsorbed oral iron feeds pathogenic gut bacteria and disturbs the flora, a reason supplementation can upset the gut and is being rethought.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — The liver is the body's iron bank and gatekeeper: it stores iron as ferritin and makes the hepcidin and transferrin that govern its traffic, so falling liver iron stores are the first stage of deficiency, well before the anemia shows.
- `connects-to` → **[Spleen](../../06-organ/spleen/README.md)** — The spleen recycles the body's iron: its macrophages dismantle worn-out red cells and return their iron to the marrow, so this salvage loop normally dwarfs dietary intake and its failure or loss strains the iron balance.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — The lung can hide the bleeding: pulmonary hemosiderosis and Goodpasture trap iron in alveolar bleeds rather than recycling it, an occult internal loss that causes iron-deficiency anemia without any visible blood.
- `connects-to` → **[Esophageal Cancer](../esophageal-cancer/README.md)** — Chronic iron lack can scar the swallowing tube: Plummer-Vinson syndrome pairs long-standing iron deficiency with esophageal webs and dysphagia, a premalignant state that raises the risk of esophageal squamous cell carcinoma.
- `connects-to` → **[Giardia lamblia](../../../02-pathogen/04-parasites/giardia-lamblia/README.md)** — A gut parasite can starve the body of iron: Giardia and other intestinal infections damage the absorptive lining and cause malabsorption, a common cause of iron deficiency where these infections are endemic.
- `connects-to` → **[Neutrophil](../../04-cellular/neutrophil/README.md)** — Defense needs iron too: iron is required for neutrophils' oxidative burst and proliferation, so iron deficiency subtly impairs these front-line cells — even as withholding iron is itself a defense against bacteria.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — The brain runs short on iron too: iron is needed for myelination and dopamine synthesis, so deficiency impairs cognition and attention in children and drives restless legs syndrome in adults.
- `connects-to` → **[Cardiomyocyte](../../04-cellular/cardiomyocyte/README.md)** — It strains and starves the heart muscle: chronic anemia forces a high-output state while iron deficiency itself impairs cardiomyocyte mitochondrial energetics, which is why iron repletion improves symptoms in heart failure.
- `connects-to` → **[Venous Thromboembolism](../venous-thromboembolism/README.md)** — Low iron can paradoxically clot: iron deficiency triggers a reactive thrombocytosis and is a recognized risk factor for venous thromboembolism, including the unusual cerebral venous sinus thrombosis.
- `connects-to` → **[Endometrial Cancer](../endometrial-cancer/README.md)** — Uterine bleeding bleeds the iron away: heavy or postmenopausal uterine bleeding from endometrial cancer is a classic cause of iron-deficiency anemia, and unexplained IDA in a postmenopausal woman prompts its search.
- `connects-to` → **[Bladder Cancer](../bladder-cancer/README.md)** — Blood lost in the urine drains the stores: chronic or intermittent hematuria from bladder cancer steadily depletes iron, so iron-deficiency anemia with microscopic hematuria warrants urologic evaluation.
- `connects-to` → **[Stroke](../stroke/README.md)** — Severe deficiency can reach the brain: iron deficiency drives reactive thrombocytosis and reduces oxygen delivery, and is a recognized — if uncommon — cause of ischemic stroke and cerebral venous thrombosis, especially in the young.
- `connects-to` → **[ADHD](../attention-deficit-hyperactivity-disorder/README.md)** — Low iron disturbs the developing brain: iron is a cofactor for dopamine synthesis, and deficiency in children is linked to attention problems, restless legs and the symptoms of ADHD, sometimes improving with repletion.
- `connects-to` → **[Wound Healing](../wound-healing/README.md)** — Iron-starved tissue repairs poorly: iron is needed for collagen cross-linking and oxygen delivery to the wound bed, so deficiency slows healing alongside the reduced perfusion of anemia.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — Iron shortage saps mood and energy: by impairing dopamine and serotonin synthesis and oxygen delivery, iron deficiency produces fatigue, poor concentration and depressive symptoms that can lift with treatment.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — Low iron shows on skin, nails and hair: iron deficiency causes pallor, brittle spoon-shaped koilonychia, diffuse hair loss, angular cheilitis and a smooth, sore glossitis of the tongue.
- `connects-to` → **[Immune System](../immune-system/README.md)** — Iron is double-edged for immunity: it is essential for lymphocyte and neutrophil function so deficiency impairs immune defence, yet the body deliberately withholds iron during infection to starve pathogens.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — Iron is needed to make thyroid hormone: thyroid peroxidase is a heme enzyme, so iron deficiency blunts thyroid-hormone synthesis and worsens hypothyroidism, tying the deficiency to the endocrine system.
- `connects-to` → **[Cardiovascular System](../cardiovascular-system/README.md)** — It forces the heart to overwork: to deliver oxygen with fewer red cells, iron-deficiency anaemia drives a high-output state with tachycardia and a flow murmur, and worsens angina in severe cases.
- `connects-to` → **[Respiratory System](../respiratory-system/README.md)** — It starves tissues of oxygen: reduced haemoglobin lowers oxygen-carrying capacity, producing exertional breathlessness and fatigue out of proportion to any lung disease.
- `connects-to` → **[Renal System](../renal-system/README.md)** — Kidney disease drives and complicates it: chronic kidney disease causes anaemia through low erythropoietin and functional iron deficiency, so intravenous iron is central to its management.
- `connects-to` → **[Ibuprofen](../../../03-medicine/01-modern/12-anti-inflammatory/ibuprofen/README.md)** — NSAIDs erode the gut lining: ibuprofen and related drugs cause gastric and duodenal ulcers whose slow bleeding is a leading drug-induced cause of iron-deficiency anemia.
- `connects-to` → **[Aspirin](../../../03-medicine/01-modern/04-cardio/aspirin/README.md)** — Antiplatelet therapy bleeds slowly: regular aspirin promotes chronic occult gastrointestinal blood loss, a frequent and easily missed source of iron-deficiency anemia in older adults.
- `connects-to` → **[Lymphatic System](../lymphatic-system/README.md)** — The spleen recycles most of the body's iron: its reticuloendothelial macrophages salvage iron from worn-out red cells, and these stores are drawn down before the marrow runs short.
- `connects-to` → **[Sickle Cell Disease](../sickle-cell-disease/README.md)** — Opposite iron problems: unlike iron-deficiency anaemia, sickle cell is a haemolytic anaemia where repeated transfusion causes iron overload, so the two demand opposite iron management.
- `connects-to` → **[Pancreatic Cancer](../pancreatic-cancer/README.md)** — A red flag for hidden malignancy: unexplained iron-deficiency anaemia from occult gastrointestinal blood loss can signal pancreatic, ampullary or other gut cancers, prompting endoscopic and imaging work-up.
- `connects-to` → **[Plasmodium falciparum](../../../02-pathogen/04-parasites/plasmodium-falciparum/README.md)** — Malaria drains the blood and iron: falciparum malaria causes anaemia through haemolysis and inflammatory iron sequestration, and iron supplementation in endemic areas must be balanced against infection risk.
- `connects-to` → **[Hepatic Lobule](../../05-tissue/hepatic-lobule/README.md)** — The liver gauges iron need: hepatocytes in the liver lobule make hepcidin, the master iron-regulatory hormone, which is appropriately suppressed in iron deficiency to maximise dietary absorption and release of stored iron.
- `connects-to` → **[Omeprazole](../../../03-medicine/01-modern/08-gi/omeprazole/README.md)** — Acid suppression starves iron uptake: proton-pump inhibitors like omeprazole reduce the gastric acid needed to absorb dietary non-haem iron, a recognised contributor to iron-deficiency anaemia with long-term use.
- `connects-to` → **[Obesity](../obesity/README.md)** — Obesity causes a functional deficiency: chronic low-grade inflammation in obesity raises hepcidin, trapping iron and impairing its absorption, so iron deficiency is common despite adequate intake and stores.
- `connects-to` → **[Myocardium](../../05-tissue/myocardium/README.md)** — When anaemia strains the heart: severe iron deficiency forces a high-output state and, chronically, an anaemic cardiomyopathy, and iron itself is needed for cardiomyocyte energetics—worsening any heart failure.
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — The body's oxygen sensor: the kidney detects the low oxygen delivery of anaemia and releases erythropoietin to drive red-cell production, the compensatory loop that iron deficiency tries to outrun.
- `connects-to` → **[Aplastic Anemia](../aplastic-anemia/README.md)** — Two anaemias, opposite causes: iron-deficiency anaemia comes from too little iron for haemoglobin while aplastic anaemia comes from marrow failure—a key contrast when the blood count and iron studies don't add up.
- `connects-to` → **[Renal Cell Carcinoma](../renal-cell-carcinoma/README.md)** — Haematuria as a clue: renal cell carcinoma classically presents with haematuria that can cause iron-deficiency anaemia, one of the urological cancers uncovered during an unexplained-anaemia workup.
- `connects-to` → **[Rheumatoid Arthritis](../rheumatoid-arthritis/README.md)** — Two anaemias in one disease: rheumatoid arthritis causes anaemia of chronic disease and, through NSAID-induced gastrointestinal bleeding, a superimposed iron-deficiency anaemia.
- `connects-to` → **[Cardiac Conduction System](../../05-tissue/cardiac-conduction-system/README.md)** — A fast, high-output heart: severe iron-deficiency anaemia drives compensatory tachycardia and palpitations through the cardiac conduction system, and can precipitate high-output heart failure.
- `connects-to` → **[Insomnia Disorder](../insomnia-disorder/README.md)** — Restless legs and sleep: iron deficiency causes restless legs syndrome, a major driver of sleep-onset insomnia that improves with iron repletion—iron being a cofactor for dopamine synthesis in the brain.
- `connects-to` → **[Pulmonary Arterial Hypertension](../pulmonary-arterial-hypertension/README.md)** — Iron and the pulmonary vasculature: iron deficiency is common in pulmonary arterial hypertension and independently worsens symptoms and outcomes, prompting trials of intravenous iron repletion.
- `connects-to` → **[COVID-19 Disease](../covid-19-disease/README.md)** — Dysregulated iron in infection: COVID-19 disturbs iron metabolism with hyperferritinaemia and functional iron deficiency, and post-COVID anaemia and fatigue are increasingly recognised.
- `connects-to` → **[Von Willebrand Factor](../../03-molecular/von-willebrand-factor/README.md)** — Bleeding-driven loss: von Willebrand disease, from defective von Willebrand factor, causes mucosal bleeding and heavy menstruation that is a common occult cause of iron-deficiency anaemia.
- `connects-to` → **[Hemophilia A](../hemophilia-a/README.md)** — Chronic blood loss: recurrent bleeding in haemophilia A depletes body iron over time, a coagulation-disorder route to iron-deficiency anaemia distinct from the more common GI and menstrual losses.
- `connects-to` → **[Immune Thrombocytopenia](../immune-thrombocytopenia/README.md)** — Platelet-loss bleeding: the mucocutaneous and menstrual bleeding of immune thrombocytopenia can drain iron stores, layering iron-deficiency anaemia onto the underlying low platelet count.
- `connects-to` → **[Dopamine](../../03-molecular/dopamine/README.md)** — Restless legs and cognition: iron is a cofactor for tyrosine hydroxylase in dopamine synthesis, so iron deficiency disrupts dopaminergic signalling, causing restless legs syndrome and the attention deficits of low iron.
- `connects-to` → **[ATP](../../03-molecular/atp/README.md)** — Bioenergetic failure: iron is essential to the cytochromes and iron-sulfur clusters of oxidative phosphorylation, so iron deficiency impairs cellular ATP production, a molecular basis for the fatigue of the anaemia.
- `connects-to` → **[Thrombopoietin](../../03-molecular/thrombopoietin/README.md)** — Reactive thrombocytosis: iron deficiency commonly raises platelet counts, with thrombopoietin and erythropoietin cross-signalling implicated in the reactive thrombocytosis that accompanies the anaemia.
- `connects-to` → **[EPAS1 (HIF-2α)](../../03-molecular/epas1/README.md)** — HIF-2α is stabilized in the iron-starved duodenal enterocyte, where it transcriptionally upregulates DMT1 and ferroportin to maximize dietary iron absorption—the master switch the body uses to compensate for iron deficiency.
- `connects-to` → **[Thyroid hormones](../../03-molecular/thyroid-hormones/README.md)** — Thyroid peroxidase is a haem enzyme, so iron deficiency impairs thyroid hormone synthesis—the basis for the overlap between iron-deficiency anemia and hypothyroid symptoms like fatigue and cold intolerance.
- `connects-to` → **[Serotonin](../../03-molecular/serotonin/README.md)** — Iron is a cofactor for tryptophan hydroxylase in serotonin synthesis, so iron deficiency lowers serotonergic signaling, contributing to the mood disturbance and fatigue that accompany the anemia beyond the lack of oxygen delivery.
- `connects-to` → **[Norepinephrine](../../03-molecular/norepinephrine/README.md)** — Iron is the cofactor for tyrosine hydroxylase, the rate-limiting enzyme for noradrenaline and dopamine, so iron deficiency blunts catecholamine signaling—a basis for the poor concentration, fatigue and attention problems beyond the anemia.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Dietary calcium competitively inhibits non-heme iron uptake at the enterocyte, a clinically important interaction explaining why calcium supplements and dairy taken with meals can worsen iron deficiency.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — The tissue hypoxia of anemia stabilizes HIF and drives VEGF release, the angiogenic and erythropoietic compensatory response that the body mounts to the reduced oxygen-carrying capacity of iron-deficient blood.
- `connects-to` → **[SMAD4](../../03-molecular/smad4/README.md)** — The BMP-SMAD pathway (SMAD4) driving hepcidin transcription is downregulated when iron is scarce, lowering hepcidin to maximize iron absorption—the appropriate response distinguishing iron-deficiency anemia from the anemia of inflammation.
- `connects-to` → **[Interleukin-6](../../03-molecular/il-6/README.md)** — IL-6 raises hepcidin to sequester iron, and its absence in true iron-deficiency anemia keeps hepcidin low—the key mechanistic distinction from the iron-restricted anemia of chronic disease.
- `connects-to` → **[Caspase-3](../../03-molecular/caspase-3/README.md)** — Iron deficiency impairs erythroid maturation and increases caspase-3 apoptosis of developing erythroblasts, contributing to the ineffective erythropoiesis of severe iron deficiency.
- `connects-to` → **[Transforming Growth Factor Beta](../../03-molecular/tgf-beta/README.md)** — BMP/TGF-β-superfamily signaling through SMAD (SMAD4 already mapped) is the central hepatocyte pathway that transcriptionally tunes hepcidin to iron stores, governing the iron availability that iron-deficiency anemia depletes.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — IL-1β, alongside IL-6 (already mapped), induces hepcidin and the functional iron sequestration that compounds iron-deficiency anemia when inflammation coexists.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — mTOR couples iron and nutrient availability to protein synthesis in developing erythroblasts, so iron deficiency restrains mTOR-dependent translation and limits hemoglobinization.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — The erythropoietin receptor signals through JAK2 (EPO mapped); iron-restricted erythropoiesis blunts the output of this pathway in iron deficiency anemia.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — EPO-driven PI3K-AKT signaling supports erythroid progenitor survival, a response constrained by the iron limitation of iron deficiency anemia.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — EPO-ERK-MAPK signaling drives erythroid progenitor proliferation, which iron restriction limits in iron deficiency anemia.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK energy sensing responds to the impaired mitochondrial respiration of iron-deficient cells, linking iron deficiency to the metabolic and exercise-intolerance symptoms of the anemia.
- `connects-to` → **[NRF2](../../03-molecular/nfe2l2/README.md)** — NRF2 governs the heme- and iron-handling antioxidant response (including HO-1), shaping the cellular adaptation to the iron restriction of iron deficiency anemia.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — FOXO transcription factors integrate the oxidative and metabolic stress of iron-restricted erythropoiesis, modulating erythroid progenitor survival in iron deficiency anemia.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — IL-6-STAT3 signaling (IL-6 already mapped) induces hepcidin, the inflammatory axis that compounds iron restriction when inflammation accompanies iron deficiency anemia.
- `connects-to` → **[CDK4/6](../../03-molecular/cdk4-6/README.md)** — CDK4/6-driven erythroid progenitor cell-cycle progression is constrained by the limited iron available for hemoglobinization in iron deficiency anemia.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — Class I PI3K (PIK3CA) signaling transduces the erythropoietin survival and proliferation signal in the iron-restricted erythroid progenitors of iron deficiency anemia (AKT already mapped).
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β modulates the erythropoietin and metabolic signaling in erythroid progenitors relevant to the impaired erythropoiesis of iron deficiency anemia.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — S100A8/A9 alarmins reflect the inflammatory context that can contribute to the functional iron restriction overlapping with iron deficiency anemia.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — IFN-STAT1 signaling links inflammatory stimuli to the hepcidin regulation and iron sequestration that overlaps with iron deficiency anemia.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — Autophagy (including the erythroid mitophagy of reticulocyte maturation) participates in the erythropoiesis impaired in iron deficiency anemia.
- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — SRC-family kinase signaling downstream of the EPO and cytokine receptors participates in the erythroid signaling disrupted in iron deficiency anemia.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — DNMT3A-mediated DNA methylation participates in the transcriptional regulation of erythroid differentiation relevant to iron deficiency anemia.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-family chemokine signaling participates in the bone-marrow niche and inflammatory interactions relevant to iron deficiency anemia.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — CXCL12-CXCR4 signaling participates in the erythroid bone-marrow-niche interactions relevant to iron deficiency anemia.
- `connects-to` → **[KIT](../../03-molecular/kit/README.md)** — KIT (stem-cell-factor receptor) signaling participates in the erythroid-progenitor proliferation and survival compromised in iron deficiency anemia.
- `connects-to` → **[RUNX1](../../03-molecular/runx1/README.md)** — RUNX1 transcription-factor activity participates in the erythroid and hematopoietic differentiation impaired in iron deficiency anemia.
- `connects-to` → **[BCL-2](../../03-molecular/bcl-2/README.md)** — BCL-2 anti-apoptotic signaling participates in the erythroblast survival (dependent on adequate iron and erythropoietin) relevant to iron deficiency anemia.
- `connects-to` → **[NOTCH](../../03-molecular/notch/README.md)** — NOTCH signaling participates in the hematopoietic-stem-cell and erythroid-progenitor regulation relevant to iron deficiency anemia.
- `connects-to` → **[Proton](../../01-subatomic/proton/README.md)** — Acid-dependent absorption: dietary ferric iron is reduced and absorbed only in the acidic duodenum, so gastric proton secretion is required for uptake, and achlorhydria or proton-pump inhibitors cause or worsen iron deficiency.
- `connects-to` → **[Estrogen](../../03-molecular/estrogen/README.md)** — Menstrual blood loss: heavy menstrual bleeding from the estrogen-driven endometrial cycle is the leading cause of iron deficiency anaemia in premenopausal women, and its cessation at menopause shifts the differential toward gastrointestinal loss.
- `connects-to` → **[Copper](../../02-atomic/copper/README.md)** — Copper-iron interaction: copper-dependent ferroxidases such as ceruloplasmin load iron onto transferrin (already mapped), so copper deficiency produces an iron-deficiency-like anaemia despite adequate iron, a key differential.
- `connects-to` → **[Testosterone](../../03-molecular/testosterone/README.md)** — Androgen erythropoiesis: testosterone stimulates erythropoiesis and suppresses hepcidin (already mapped), so androgens raise the baseline haemoglobin, and hypogonadism worsens the anaemia against which iron deficiency develops.
- `connects-to` → **[Progesterone](../../03-molecular/progesterone/README.md)** — Pregnancy iron demand: pregnancy, sustained by progesterone, sharply raises iron requirements for the expanding red-cell mass and the fetus, making iron-deficiency anaemia common in pregnancy and a target for routine supplementation.
- `connects-to` → **[Secretory IgA](../../03-molecular/secretory-iga/README.md)** — Coeliac malabsorption: coeliac disease is a common cause of iron malabsorption and refractory iron-deficiency anaemia, screened for with anti-transglutaminase IgA, linking the disorder to mucosal immunity of the small intestine (already mapped).
- `connects-to` → **[Histamine](../../03-molecular/histamine/README.md)** — Gastric acid and absorption: gastric acid, driven by histamine, reduces dietary iron to the absorbable ferrous form, so acid suppression with proton-pump inhibitors and atrophic gastritis impair iron absorption and can cause iron-deficiency anaemia.
- `connects-to` → **[Prostaglandins](../../03-molecular/prostaglandins/README.md)** — NSAID gastrointestinal bleeding: non-steroidal anti-inflammatory drugs block the protective mucosal prostaglandins, causing the gastric erosions and chronic occult gastrointestinal bleeding that are a common cause of iron-deficiency anaemia.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Metabolic interplay: iron deficiency alters leptin signalling and appetite, and it is associated with pica and restless-legs symptoms (dopamine already mapped), part of the systemic effects of iron-deficiency anaemia beyond the red cells.
- `connects-to` → **[Stomach](../../06-organ/stomach/README.md)** — Gastric absorption and loss: the stomach's acid aids iron absorption — lost in atrophic gastritis, H. pylori and acid-suppressing drugs — and gastric erosions cause the occult bleeding that is a common source of iron-deficiency anaemia.
- `connects-to` → **[Copper](../../02-atomic/copper/README.md)** — Copper ferroxidases: copper is required by ceruloplasmin and hephaestin, the ferroxidases that oxidise iron for loading onto transferrin (already mapped), so copper deficiency causes an iron-deficiency-like anaemia despite adequate iron.
- `connects-to` → **[Colorectal cancer](../colorectal-cancer/README.md)** — Occult malignancy: iron-deficiency anaemia from occult gastrointestinal blood loss in an older adult mandates investigation for colorectal cancer, of which it is often the presenting sign.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — Adipokine-iron crosstalk: adiponectin, with leptin (already mapped), participates in the adipokine crosstalk with the iron metabolism (hepcidin already mapped) and erythropoiesis altered in iron-deficiency anaemia.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), is part of the adipokine-inflammatory milieu that intersects with the iron and erythropoietic regulation in anaemia.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Dietary iron interaction: dietary calcium inhibits the absorption of non-haem iron in the duodenum, a dietary interaction relevant to the timing of the iron supplementation that treats iron-deficiency anaemia.
- `connects-to` → **[Bone marrow](../../05-tissue/bone-marrow/README.md)** — Iron-restricted erythropoiesis: the bone-marrow erythropoiesis is limited by the iron supply (transferrin already mapped) in iron-deficiency anaemia, the iron-restricted erythropoiesis producing the microcytic red cells.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Iron-recycling macrophages: the macrophages recycle the iron from the senescent red cells (ferroportin already mapped); their iron release (blocked in the anaemia of chronic disease) is the differential of iron-deficiency anaemia.
- `connects-to` → **[Colorectal cancer](../colorectal-cancer/README.md)** — Occult-bleeding cause: the iron-deficiency anaemia from the chronic occult GI bleeding (transferrin already mapped) is a classic presenting sign of colorectal cancer, mandating investigation.
- `connects-to` → **[Hepatocyte](../../04-cellular/hepatocyte/README.md)** — Hepatic iron sensing: the hepatocytes produce the hepcidin (already mapped) and store the ferritin iron; the low iron of iron-deficiency anaemia suppresses the hepcidin to maximise the absorption.
- `connects-to` → **[IFN-gamma](../../03-molecular/ifn-gamma/README.md)** — Inflammation-restricted erythropoiesis: the IFN-γ of the T cells suppresses the erythropoiesis and, in the mixed iron-deficiency/inflammatory anaemias, compounds the iron-restricted erythropoiesis.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — Type-2 immune modulation: IL-4 and the type-2 arm modulate the macrophage (already mapped) iron handling that intersects with the iron-deficiency anaemia.
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — Type-2 arm: IL-13, with IL-4 (already mapped), completes the type-2 immune arm whose M2-macrophage (already mapped) polarisation shapes the iron handling intersecting with iron-deficiency anaemia.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Eosinophil/hookworm arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), drives the eosinophil response to the hookworm and other parasites that are a leading cause of the iron-deficiency anaemia through gut blood loss.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — Th1 arm: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the inflammatory milieu that, in the mixed anaemias, compounds the iron-restricted erythropoiesis of iron-deficiency anaemia.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — Antiparasite IgE: IgE, with the type-2 cytokines (IL-4, IL-5 and IL-13 already mapped), mediates the antiparasite response to the hookworm and other helminths whose gut blood loss is a leading global cause of iron-deficiency anaemia.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — Epithelial alarmin: IL-33, released by the injured gut epithelium, initiates the type-2 (IL-5 already mapped) antiparasite response to the intestinal helminths that cause the blood-loss iron-deficiency anaemia.
- `connects-to` → **[Mast cell](../../04-cellular/mast-cell/README.md)** — Intestinal mast cells: the mast cells of the gut, armed by the IgE (already mapped), are effectors of the antiparasite type-2 response to the hookworm blood loss underlying much iron-deficiency anaemia.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Antiparasite complement: the complement C3 opsonises the intestinal helminths (hookworm), part of the innate mucosal defence against the blood-loss cause of much iron-deficiency anaemia.
- `connects-to` → **[C5aR1](../../03-molecular/c5ar1/README.md)** — C5a receptor: the C5aR1 signalling (with the complement C3 already mapped) recruits the myeloid cells to the intestinal mucosa in the antiparasite response underlying the blood-loss iron-deficiency anaemia.
- `connects-to` → **[Dendritic cell](../../04-cellular/dendritic-cell/README.md)** — Mucosal antigen presentation: the dendritic cells of the gut present the helminth antigen to the T-helper (already mapped) cells, priming the type-2 antiparasite response to the hookworm blood loss of iron-deficiency anaemia.
- `connects-to` → **[TSLP](../../03-molecular/tslp/README.md)** — Alarmin-gut axis: TSLP, from intestinal epithelium (already mapped) under the hookworm or blood-loss mucosal injury of iron-deficiency anaemia, primes mast cells (already mapped) and dendritic cells (already mapped) toward the type-2 antiparasite and mucosal repair response.
- `connects-to` → **[Bradykinin](../../03-molecular/bradykinin/README.md)** — Kinin-GI axis: bradykinin, via the kallikrein-kinin system activated by the gastrointestinal mucosal (already mapped) injury and blood loss underlying iron-deficiency anaemia, amplifies the local vascular permeability and the inflammatory response.
- `connects-to` → **[C1-Esterase Inhibitor](../../03-molecular/c1-esterase-inhibitor/README.md)** — Complement brake: C1-esterase inhibitor regulates the classical-complement pathway (C3 and C5aR1 already mapped) and the contact system (bradykinin) activated during the mucosal injury and the hookworm-driven blood loss of iron-deficiency anaemia.
- `connects-to` → **[Factor H](../../03-molecular/factor-h/README.md)** — Complement regulation: factor H limits alternative-pathway activation on erythrocytes (already mapped) and gut mucosal surfaces, regulating the complement (C3 and C5aR1 already mapped) contribution to the haemolytic and mucosal injury of iron-deficiency anaemia.
- `connects-to` → **[Complement C5](../../03-molecular/complement-c5/README.md)** — Terminal complement: complement C5 activation (with C3 already mapped) contributes to the intravascular haemolysis and the complement-driven mucosal injury that aggravate blood loss and iron malabsorption in iron-deficiency anaemia.
- `connects-to` → **[Periostin](../../03-molecular/periostin/README.md)** — Gut-mucosal fibrosis matrix: periostin, from intestinal fibroblasts at the hookworm-damaged gut mucosa (intestinal-epithelium already mapped) of iron-deficiency anaemia, promotes type-2 mucosal repair and is a Th2/type-2 biomarker of the helminth response.
- `connects-to` → **[Prolactin](../../03-molecular/prolactin/README.md)** — Iron-immune neuroendocrine: prolactin, via PRLR on macrophages (already mapped) and intestinal epithelium (already mapped), modulates iron absorption and immune responses; hyperprolactinaemia amplifies the IL-6 (already mapped) and hepcidin (already mapped) axis of iron sequestration in IDA.
- `connects-to` → **[Oxytocin](../../03-molecular/oxytocin/README.md)** — Gut mucosal oxytocin: oxytocin, via OXTR on macrophages (already mapped) and intestinal epithelium (already mapped), attenuates gut inflammation and promotes mucosal iron absorption; oxytocin reduces the IL-6 (already mapped) and hepcidin (already mapped) iron sequestration in IDA.
- `connects-to` → **[Vasopressin](../../03-molecular/vasopressin/README.md)** — Fluid-iron homeostasis: vasopressin, via V2 receptors on macrophages (already mapped) and renal tubular cells, modulates fluid-iron homeostasis; elevated vasopressin in anaemic states amplifies the hepcidin (already mapped) and IL-6 (already mapped) iron-sequestration response of IDA.
- `connects-to` → **[Selenium](../../02-atomic/selenium/README.md)** — IDA selenium: selenium, via GPx and NRF2 (already mapped) antioxidant systems, protects erythrocytes (already mapped) from oxidative haemolysis; selenium deficiency amplifies the hepcidin (already mapped) and IL-6 (already mapped) iron-sequestration response, worsening IDA.
- `connects-to` → **[Iodine](../../02-atomic/iodine/README.md)** — IDA iodine: iodine-dependent thyroid hormones regulate erythropoietin (already mapped) and erythropoiesis in bone marrow (already mapped); hypothyroidism amplifies the hepcidin (already mapped) and IL-6 (already mapped) iron-withholding cascade of iron-deficiency anaemia.
- `connects-to` → **[Sodium](../../02-atomic/sodium/README.md)** — IDA sodium: sodium, via osmotic balance, regulates erythrocyte (already mapped) hydration and survival; dysregulated sodium amplifies oxidative stress in the transferrin (already mapped)-depleted and hepcidin (already mapped) iron-sequestered state of iron-deficiency anaemia.
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — IDA magnesium: magnesium, as a cofactor for erythropoiesis enzymes in macrophages (already mapped) and erythrocytes (already mapped), supports haem synthesis; magnesium deficiency amplifies the hepcidin (already mapped) and IL-6 (already mapped) iron-sequestration cascade of IDA.
- `connects-to` → **[Potassium](../../02-atomic/potassium/README.md)** — IDA potassium: potassium channels regulate erythrocyte (already mapped) hydration and mast-cell (already mapped) activation; potassium depletion amplifies the IL-6 (already mapped) and hepcidin (already mapped) iron-sequestration cascade of iron-deficiency anaemia.
- `connects-to` → **[Phosphorus](../../02-atomic/phosphorus/README.md)** — IDA phosphorus: phosphorus, as ATP precursor in erythrocytes (already mapped) and macrophages (already mapped), supports haemoglobin synthesis; phosphorus deficiency amplifies the IL-6 (already mapped) and hepcidin (already mapped) iron-sequestration cascade of IDA.
- `connects-to` → **[Chloride](../../02-atomic/chloride/README.md)** — IDA chloride: chloride via band-3 anion exchanger regulates erythrocyte (already mapped) membrane hydration; chloride dysregulation amplifies mast-cell (already mapped) and IL-6 (already mapped) and hepcidin (already mapped) iron-sequestration in iron-deficiency anaemia.
- `connects-to` → **[Carbon](../../02-atomic/carbon/README.md)** — IDA carbon: carbon as backbone of haem (already mapped) and transferrin (already mapped) sustains erythropoiesis (already mapped); carbon depletion in reticulocytes (already mapped) and macrophages (already mapped) amplifies IL-6 (already mapped) anaemic cascade of IDA.
- `connects-to` → **[Hydrogen](../../02-atomic/hydrogen/README.md)** — IDA hydrogen: hydrogen-ion acidosis in iron-deficient erythrocytes (already mapped) and macrophages (already mapped) impairs haemoglobin (already mapped) oxygen transport; hydrogen dysregulation amplifies NF-κB (already mapped) and EPO (already mapped) cascade of IDA.
- `connects-to` → **[Nitrogen](../../02-atomic/nitrogen/README.md)** — IDA nitrogen: nitrogen in amino-acid precursors of haem (already mapped) and transferrin (already mapped) sustains erythropoiesis (already mapped); nitrogen deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and EPO (already mapped) cascade of IDA.

[^camaschella-2015-iron-deficiency]: Camaschella C. Iron-deficiency anemia. *N Engl J Med.* 2015;372(19):1832-1843. [doi:10.1056/NEJMra1401038](https://doi.org/10.1056/NEJMra1401038) · [PubMed 25946282](https://pubmed.ncbi.nlm.nih.gov/25946282/)
[^who-ferritin-guideline-2020]: World Health Organization. WHO guideline on use of ferritin concentrations to assess iron status in individuals and populations. WHO; 2020. [WHO publication](https://www.who.int/publications/i/item/9789240000124)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
