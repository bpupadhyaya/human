---
schema: human-scale-entry/v1
id: thalassemia
name: Thalassemia
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-08
summary: "Thalassaemias are haemoglobinopathies from α- or β-globin chain imbalance; β-thalassaemia major requires lifelong transfusion; ineffective erythropoiesis → iron overload despite anaemia; betibeglogene autotemcel (Zynteglo) and CRISPR-based Casgevy are approved gene therapies."
aliases: ["thalassaemia", "thalassemia", "beta-thalassemia", "alpha-thalassemia", "β-thalassaemia major", "Cooley's anaemia", "thal major", "HbH disease", "hydrops fetalis", "thal trait"]
sources:
  - id: weatherall-2008-thalassemia-review
    type: peer-reviewed
    cite: "Weatherall DJ. The inherited diseases of hemoglobin are an emerging global health burden. Blood. 2010;115(22):4331-4336."
    doi: "10.1182/blood-2010-01-251348"
    pmid: "20233970"
    url: "https://doi.org/10.1182/blood-2010-01-251348"
  - id: cappellini-2014-thalassemia-guidelines
    type: clinical-guideline
    cite: "Cappellini MD, Cohen A, Porter J, et al. (eds). Guidelines for the Management of Transfusion Dependent Thalassaemia (TDT). 3rd ed. Thalassaemia International Federation; 2014."
    url: "https://thalassaemia.org.cy/publications/tif-publications/guidelines-management-transfusion-dependent-thalassaemia-tdt-3rd-edition-2014/"
    accessed: "2026-06-08"
  - id: thompson-2018-zynteglo-nejm
    type: peer-reviewed
    cite: "Thompson AA, Walters MC, Kwiatkowski J, et al. Gene therapy in patients with transfusion-dependent β-thalassemia. N Engl J Med. 2018;378(16):1479-1493."
    doi: "10.1056/NEJMoa1705342"
    pmid: "29669226"
    url: "https://doi.org/10.1056/NEJMoa1705342"
cross_links:
  - target: 01-human/03-molecular/hemoglobin
    relation: connects-to
    note: "Thalassaemias arise from imbalanced α- or β-globin chain synthesis; excess unpaired chains precipitate → ineffective erythropoiesis and haemolysis; HbA₂ (α2δ2) elevation >3.5% diagnoses β-thal trait; HbH (β4 tetramers) is the signature of 3-gene α-thal deletion."
  - target: 01-human/03-molecular/transferrin
    relation: connects-to
    note: "β-thal major: ineffective erythropoiesis → ERFE ↑ → hepcidin suppression → unconstrained iron absorption → TSAT 100% → NTBI → tissue deposition; deferasirox (oral) and deferoxamine (parenteral) are the mainstay chelators targeting transferrin-bound and NTBI iron."
  - target: 01-human/03-molecular/hepcidin
    relation: connects-to
    note: "Ineffective erythropoiesis in β-thalassaemia → ERFE (erythroferrone from stress erythroblasts) → suppresses BMP-SMAD → ↓ hepcidin → ↑ ferroportin → unconstrained iron absorption despite anemia; luspatercept (ActRIIA ligand trap) ↑ ERFE pathway and ↓ ineffective erythropoiesis."
  - target: 01-human/07-system/sickle-cell-disease
    relation: connects-to
    note: "HbSβ-thalassemia (HbS + β-thal allele) is a common SCD genotype; severity depends on β-thal allele type (β⁰ = severe SCA-like; β⁺ = milder); gene therapy approaches (Zynteglo, Casgevy) target both SCD and β-thal major as overlapping haemoglobinopathies."
  - target: 01-human/03-molecular/g6pd
    relation: connects-to
    note: "Thalassaemia (HbE/β-thal most common in SEA) co-occurs with G6PD Mahidol/Viangchan; G6PD deficiency + beta-thalassaemia → additive oxidant haemolysis; G6PD screening is recommended in thalassaemia; both adaptations cluster in malaria-endemic regions by balanced selection."
  - target: 01-human/03-molecular/activin-a
    relation: connects-to
    note: "Activin A/B → ActRIIB on late erythroblasts → SMAD2/3 → maturation block → ineffective erythropoiesis in beta-thalassemia; luspatercept (BELIEVE trial: 21% achieved ≥33% transfusion reduction vs. 4.5% placebo) traps activin A/B → accelerates terminal erythroid differentiation."
  - target: 01-human/04-cellular/erythrocyte
    relation: connects-to
    note: "In thalassemia the imbalance of α and β globin leaves unpaired chains that precipitate inside red cells, so most erythroblasts die in the marrow before maturing (ineffective erythropoiesis) and survivors are microcytic, hypochromic target cells that haemolyse."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Thalassemia causes iron overload despite anaemia: ineffective erythropoiesis releases erythroferrone that suppresses hepcidin, so dietary iron pours in unchecked and transfusions add more; the excess poisons heart, liver, and endocrine glands, making chelation lifesaving."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "Iron-loaded cardiomyocytes make the heart the leading killer in undertreated thalassaemia major: NTBI enters via calcium channels → Fenton free radicals → arrhythmia and cardiomyopathy; cardiac MRI T2* (<10 ms = severe) guides chelation before heart failure."
  - target: 01-human/07-system/malaria
    relation: connects-to
    note: "Thalassemia, like sickle trait, is a malaria-protective hemoglobinopathy: its high gene frequency across the Mediterranean, Middle East and Asia reflects balancing selection, as α- and β-thalassemia carriers resist severe Plasmodium falciparum—matching the historic malaria map."
  - target: 01-human/05-tissue/bone-marrow
    relation: connects-to
    note: "Thalassemia is driven by ineffective erythropoiesis: unbalanced globin chains precipitate and kill red-cell precursors in the marrow, which expands massively (skeletal deformities, extramedullary hematopoiesis); luspatercept eases this block and transfusions suppress the marrow."
  - target: 01-human/07-system/iron-deficiency-anemia
    relation: connects-to
    note: "Thalassemia trait is the key differential of iron-deficiency anemia: both cause microcytic, hypochromic cells, but thalassemia has normal/high iron, a low Mentzer index and raised HbA2 while IDA shows low ferritin—mislabeling it as IDA causes harmful needless iron use."
  - target: 01-human/06-organ/spleen
    relation: connects-to
    note: "The spleen bears the brunt of thalassemia: it works overtime clearing defective red cells and hosts extramedullary hematopoiesis, enlarging massively and worsening anemia by trapping blood—so splenectomy is sometimes needed but leaves patients prone to sepsis."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "The liver is a major casualty of transfusion-dependent thalassemia: lifelong transfusions and increased gut iron absorption load the liver with iron, causing cirrhosis unless iron chelation is maintained—and hepatic iron quantified by MRI guides chelation therapy."
  - target: 01-human/07-system/osteoporosis
    relation: connects-to
    note: "Thalassemia causes a distinctive osteoporosis: marrow expansion from chronic anemia thins cortical bone, while iron overload and endocrine damage impair osteoblasts and sex hormones—so fragility fractures are common and bone-density monitoring is part of care."
  - target: 01-human/03-molecular/erythropoietin
    relation: connects-to
    note: "Erythropoietin runs high in thalassemia: severe anemia drives massive EPO release, but defective globin chains make erythropoiesis ineffective, so the marrow expands uselessly—causing skeletal deformities and extramedullary hematopoiesis instead of functional red cells."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "Thalassemia impairs oxygen delivery at its root: too few normal hemoglobin tetramers mean less oxygen per red cell, so tissues stay hypoxic despite a racing marrow—and the hypoxic drive fuels the bone expansion and high-output cardiac strain of severe disease."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "Iron overload makes thalassemia an endocrine disease: transfusion and gut iron deposit in glands, causing diabetes, hypogonadism, hypothyroidism and growth failure, so the endocrine system bears much of the chronic morbidity—and iron chelation aims to prevent it."
  - target: 01-human/03-molecular/ferroportin
    relation: connects-to
    note: "Ferroportin sits at the heart of thalassemia's iron overload: ineffective erythropoiesis suppresses hepcidin, freeing ferroportin to pump excess dietary iron into blood, so iron accumulates in heart and liver—the main cause of death in transfused patients."
  - target: 01-human/07-system/heart-failure
    relation: connects-to
    note: "Iron-overload cardiomyopathy is the leading killer in thalassemia: years of transfusion and gut iron absorption deposit iron in the myocardium, causing heart failure and arrhythmia, so iron chelation and cardiac MRI monitoring are central to survival."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "Thalassemia reshapes the skeleton: chronic anemia drives massive marrow expansion that thins and deforms bones—frontal bossing, a 'hair-on-end' skull and fracture-prone osteoporosis—so the musculoskeletal changes are a visible signature of untreated disease."
  - target: 01-human/06-organ/placenta
    relation: connects-to
    note: "The placenta marks thalassemia's most severe form: alpha-thalassemia major (loss of all four genes) leaves the fetus unable to make functional hemoglobin, causing hydrops fetalis and stillbirth—so prenatal screening and intrauterine transfusion are how it is managed."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "Thalassemia shapes reproductive choices and function: carrier screening and genetic counseling guide family planning, while iron overload from transfusions damages the pituitary and gonads, causing delayed puberty and infertility—so fertility care is part of treatment."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Thalassemia's anemia is largely macrophage-driven: defective red cells and their precursors are destroyed by splenic and marrow macrophages (extravascular hemolysis and ineffective erythropoiesis), so splenomegaly and iron recycling stem from this clearance."
  - target: 01-human/06-organ/pancreas
    relation: connects-to
    note: "Iron overload in thalassemia poisons the pancreas: transfused and over-absorbed iron deposits in pancreatic islets, causing diabetes—one of the endocrine failures (with thyroid and gonads) that iron chelation aims to prevent."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Thalassemia can be cured by replacing the marrow: an allogeneic stem-cell transplant—relying on donor cytotoxic T cells to engraft—or gene therapy gives patients a source of normal red cells, ending lifelong transfusions."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Iron overload disturbs calcium in thalassemia: iron-damaged parathyroids cause hypoparathyroidism and low calcium, while ineffective erythropoiesis and endocrinopathy weaken bone—so calcium and bone health are watched closely."
  - target: 01-human/04-cellular/cardiomyocyte
    relation: connects-to
    note: "Iron poisons the heart muscle in thalassemia: repeated transfusions deposit iron in cardiomyocytes, where it drives oxidative damage and arrhythmia, and this iron-overload cardiomyopathy is the leading cause of death—why iron chelation is lifesaving."
  - target: 01-human/06-organ/thyroid
    relation: connects-to
    note: "Transfusional iron scars the thyroid: deposits in the gland cause hypothyroidism, one of the endocrine failures of chronic thalassemia, so thyroid function is monitored alongside the heart and pancreas in iron-overloaded patients."
  - target: 01-human/03-molecular/growth-hormone
    relation: connects-to
    note: "Iron damage to the pituitary stunts growth in thalassemia: overload harms the gland that makes growth hormone, so children can fail to grow and enter puberty late—endocrine complications that shape lifelong care beyond the anemia itself."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "Thalassemia treatment can strip away zinc: iron chelators that remove the excess iron also bind zinc, so deficiency is common and contributes to the poor growth and weakened immunity of chronically treated patients."
  - target: 01-human/04-cellular/osteoclast
    relation: connects-to
    note: "Thalassemia weakens bone through osteoclasts: marrow expansion and hormone deficiencies tip the balance toward these bone-resorbing cells, driving the osteoporosis and fractures that complicate even well-transfused patients."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "Thalassemia shows in the skin: iron overload bronzes and greys the skin, while chronic anemia and poor circulation cause stubborn leg ulcers, outward marks of the disease's iron and oxygen problems."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "MRI now measures the iron itself: cardiac and liver T2* imaging in radiofrequency photons quantifies the overload that drives thalassemia's organ damage, guiding how hard to chelate."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "Thalassemia is prothrombotic: damaged red-cell membranes injure the endothelium and promote clotting, so venous thromboembolism is a real risk, especially after the spleen is removed."
  - target: 01-human/05-tissue/fibrosis
    relation: connects-to
    note: "Iron overload scars the organs: deposited iron drives fibrosis in the liver toward cirrhosis and stiffens the heart, the cumulative damage that iron chelation aims to prevent."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy shows thalassemia's broken red cells: thin, pale target cells and precipitated unpaired globin chains clumped into inclusion bodies, the wreckage of ineffective erythropoiesis that destroys cells before they leave the marrow."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "Both the disease and its cure stress the kidney: chronic iron overload and the very chelators used to remove it can injure the renal tubules, so kidney function is watched closely during lifelong treatment."
  - target: 01-human/06-organ/eye
    relation: connects-to
    note: "The chelation drugs can dim the eye: deferoxamine and related iron chelators are toxic to the retina and optic nerve, so regular eye exams guard the vision of patients on long-term treatment."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "Lifelong transfusions stir up antibodies: chronically transfused thalassemia patients form alloantibodies against donor red-cell antigens, making each future cross-match harder and the anemia more dangerous to treat."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "Blood-making spills outside the marrow and presses on nerves: extramedullary hematopoiesis forms paraspinal masses that can compress the spinal cord, a rare but reversible cause of weakness if caught early."
  - target: 01-human/04-cellular/platelet
    relation: connects-to
    note: "Removing the spleen tips the blood toward clotting: splenectomized thalassemia patients develop a reactive thrombocytosis and a hypercoagulable state, raising the risk of thrombosis and pulmonary hypertension."
  - target: 01-human/06-organ/adrenal-gland
    relation: connects-to
    note: "Iron overload poisons the endocrine glands: transfusional iron deposits in the adrenal as well as the pituitary, gonads, and pancreas, so adrenal insufficiency joins the diabetes and hypogonadism of poorly chelated thalassemia."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "Splenectomy strips a layer of defense: without the spleen's filtering, thalassemia patients face overwhelming infection by encapsulated bacteria despite their neutrophils, requiring vaccination and prompt antibiotics for fevers."
  - target: 03-medicine/03-food/vitamin-d
    relation: connects-to
    note: "Thalassemic bone is fragile and vitamin-D-poor: marrow expansion, iron's endocrine damage, and frequent vitamin D deficiency combine into the osteoporosis these patients carry, so vitamin D and calcium are part of bone care."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "Thalassemia tips the blood toward clotting: abnormal red-cell membranes and the loss of the spleen's filtering leave a hypercoagulable state, so non-transfusion-dependent and splenectomized patients carry a raised risk of venous thrombosis."
  - target: 01-human/04-cellular/osteoblast
    relation: connects-to
    note: "Thalassemic bone disease starts in the builder cell: iron and marrow expansion suppress osteoblasts while osteoclasts run on, tipping the balance to the early, severe osteoporosis characteristic of the disease."
  - target: 01-human/06-organ/small-intestine
    relation: connects-to
    note: "The gut over-absorbs iron in thalassemia: the expanded, ineffective erythropoiesis suppresses hepcidin, so the small intestine keeps drinking in dietary iron and drives overload even in patients who are never transfused."
  - target: 01-human/07-system/pulmonary-arterial-hypertension
    relation: connects-to
    note: "Chronic hemolysis pushes thalassemia toward pulmonary hypertension: free hemoglobin scavenges nitric oxide and the hypercoagulable, post-splenectomy state remodels the lung vessels, making PAH a leading cause of right heart failure and death."
  - target: 01-human/07-system/hepatitis-c
    relation: connects-to
    note: "Decades of transfusion brought hepatitis C: before reliable blood screening, transfusion-dependent thalassemia carried high HCV rates, and the resulting chronic hepatitis compounds the iron overload that already injures the liver."
  - target: 01-human/03-molecular/nitric-oxide
    relation: connects-to
    note: "Hemolysis robs the vessels of nitric oxide: cell-free hemoglobin released by fragile thalassemic red cells scavenges NO, so the vasodilator runs short — driving the endothelial dysfunction, pulmonary hypertension, and thrombosis of the disease."
  - target: 01-human/07-system/hcc
    relation: connects-to
    note: "Iron and viral hepatitis turn the liver malignant: decades of transfusional iron overload, often with chronic hepatitis C, scar the liver into cirrhosis and a markedly raised risk of hepatocellular carcinoma."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "Iron overload inflames the organs through NF-κB: excess free iron generates reactive oxygen species that activate NF-κB in liver and heart, driving the inflammation behind the iron-laden organ damage of thalassemia."
  - target: 01-human/07-system/sepsis
    relation: connects-to
    note: "Splenectomy and iron feed infection: removal of the spleen plus iron overload that nourishes bacteria like Yersinia leave thalassemia patients prone to severe infection and sepsis, a leading cause of death."
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "Iron and chronic anemia wear on the kidney: iron-overload injury, the chelating drugs' nephrotoxicity and longstanding anemic hyperfiltration can leave a slow decline toward chronic kidney disease in thalassemia."
  - target: 01-human/07-system/gout
    relation: connects-to
    note: "High cell turnover floods the blood with urate: the ineffective erythropoiesis and hemolysis of thalassemia generate excess purine breakdown, raising uric acid and predisposing to hyperuricemia and gout."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "Lifelong transfusion dependence weighs on mood: the burden of regular transfusions, iron chelation and a chronic inherited disease gives transfusion-dependent thalassemia a high rate of depression."
  - target: 01-human/07-system/type-2-diabetes
    relation: connects-to
    note: "Transfusional iron poisons the pancreas: repeated transfusions in thalassemia deposit iron in the islets, and the resulting beta-cell damage produces a secondary diabetes that is a classic endocrine complication."
  - target: 02-pathogen/02-bacteria/neisseria-meningitidis
    relation: connects-to
    note: "Splenectomy strips defense against encapsulated bacteria: many thalassemia patients undergo splenectomy for hypersplenism, leaving them vulnerable to meningococcus and other encapsulated organisms."
  - target: 01-human/07-system/stroke
    relation: connects-to
    note: "It carries a hidden clot risk: thalassemia, especially after splenectomy, is a hypercoagulable state with abnormal red cells and platelet activation that raises the risk of ischemic stroke."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "Iron overload and haemolysis hit the gut organs: transfusional iron scars the liver toward cirrhosis, chronic haemolysis forms pigment gallstones, and extramedullary haematopoiesis enlarges the spleen and liver."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "Iron and anaemia mark the skin: transfusional iron overload bronzes the skin like haemochromatosis, and chronic anaemia and poor perfusion cause leg ulcers over the ankles."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "A lifelong transfusion-dependent disease breeds worry: the endless transfusions, iron-chelation burden and inherited nature of thalassemia foster chronic health anxiety alongside depression."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "Iron poisons the heart: transfusional iron overload deposits in the myocardium, causing a cardiomyopathy and arrhythmias that are the leading cause of death in thalassemia major."
  - target: 01-human/07-system/lymphatic-system
    relation: connects-to
    note: "It swells the spleen: extramedullary haematopoiesis and ongoing red-cell destruction cause massive splenomegaly, often requiring splenectomy that then raises infection risk."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "Blood-making can compress the cord: paraspinal masses of extramedullary haematopoiesis in thalassemia can grow into the spinal canal and cause cord compression."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "Asplenia and iron overload weaken defence: splenectomy leaves vulnerability to encapsulated bacteria, while iron overload itself impairs immunity, making infection a leading cause of death in thalassemia."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "Disease and chelators both reach the kidney: chronic anaemia and iron overload cause tubular dysfunction, and the iron chelator deferasirox can be nephrotoxic, demanding renal monitoring."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "Iron and anaemia burden the lungs: chronic transfusion and haemolysis drive pulmonary hypertension and a restrictive ventilatory defect in thalassemia."
  - target: 02-pathogen/02-bacteria/streptococcus-pneumoniae
    relation: connects-to
    note: "Splenectomy invites encapsulated bacteria: removing the iron-overloaded, enlarged spleen leaves thalassaemia patients at lifelong risk of overwhelming pneumococcal sepsis, needing vaccination and prophylaxis."
  - target: 01-human/04-cellular/hepatocyte
    relation: connects-to
    note: "Iron overload poisons the liver: transfusional and absorptive iron loading deposits in hepatocytes, driving fibrosis, cirrhosis and hepatocellular carcinoma in chronically transfused thalassaemia."
  - target: 01-human/07-system/mds
    relation: connects-to
    note: "A shared failure of red-cell making: like the myelodysplastic syndromes, thalassaemia features ineffective erythropoiesis, and the maturation agent luspatercept is now used to reduce transfusion needs in both."
  - target: 03-medicine/01-modern/13-cancer/targeted-therapy
    relation: connects-to
    note: "Gene therapy now offers a cure: lentiviral beti-cel and CRISPR-edited exa-cel restore functional haemoglobin and free transfusion-dependent β-thalassaemia patients from transfusions, alongside the iron-chelators that prevent organ damage."
  - target: 03-medicine/01-modern/13-cancer/cancer-chemotherapy
    relation: connects-to
    note: "Hydroxyurea and transplant conditioning: hydroxyurea raises fetal haemoglobin to ease some thalassaemias, and intensive conditioning chemotherapy precedes the allogeneic stem-cell transplant that can cure the disease."
  - target: 01-human/05-tissue/cortical-bone
    relation: connects-to
    note: "Marrow expansion deforms the skeleton: ineffective erythropoiesis drives massive marrow hyperplasia that thins cortical bone, causing frontal bossing, the 'hair-on-end' skull, pathological fractures and osteoporosis."
  - target: 01-human/05-tissue/myocardium
    relation: connects-to
    note: "Iron-overload cardiomyopathy: transfusional iron deposits in the myocardium, causing the heart failure and arrhythmias that are the leading cause of death in transfusion-dependent thalassaemia—the target of iron chelation."
  - target: 01-human/05-tissue/hepatic-lobule
    relation: connects-to
    note: "Iron scars the liver: deposition of transfusional iron in the hepatic lobule drives fibrosis and cirrhosis, compounded by hepatitis C, a major complication tracked by liver iron quantification."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "Extramedullary haematopoiesis: ineffective marrow pushes blood formation into masses outside the marrow, including paraspinal and intracranial deposits that can compress the cord or brain."
  - target: 01-human/07-system/gvhd
    relation: connects-to
    note: "A curative transplant: allogeneic stem-cell transplant can cure transfusion-dependent thalassemia, but graft-versus-host disease is a major risk—now joined by gene therapy as a cure."
  - target: 01-human/05-tissue/germinal-center
    relation: connects-to
    note: "Alloimmunisation from transfusion: chronic red-cell transfusions in thalassemia drive germinal-centre antibody responses against donor red-cell antigens, complicating future cross-matching."
  - target: 01-human/05-tissue/cardiac-conduction-system
    relation: connects-to
    note: "Iron and arrhythmia: transfusional iron overload injures the cardiac conduction system as well as the myocardium, causing arrhythmias that, with cardiomyopathy, are a leading cause of death in thalassemia."
  - target: 01-human/05-tissue/intestinal-epithelium
    relation: connects-to
    note: "Duodenal iron absorption: thalassemia's ineffective erythropoiesis suppresses hepcidin, driving the intestinal epithelium to over-absorb dietary iron and worsening overload even without transfusion."
  - target: 01-human/07-system/aplastic-anemia
    relation: connects-to
    note: "Aplastic crisis: parvovirus B19 infection or folate deficiency can abruptly shut down red-cell production in thalassemia's chronically haemolytic marrow, the same marrow-failure vulnerability central to aplastic anaemia."
  - target: 01-human/07-system/wound-healing
    relation: connects-to
    note: "Poor-healing leg ulcers: chronic anaemia, tissue hypoxia and sluggish perfusion in thalassemia produce stubborn lower-limb ulcers, a chronic wound-healing failure shared with sickle cell disease."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "Erythropoietic drive: chronic anaemia and hypoxia stabilise HIF-1α in thalassemia, driving the erythropoietin surge and marrow expansion behind its skeletal deformities and extramedullary haematopoiesis."
  - target: 01-human/03-molecular/endothelin-1
    relation: connects-to
    note: "Vascular complication: haemolysis and endothelial dysfunction raise endothelin-1 in thalassemia, contributing to the pulmonary hypertension that complicates the chronic anaemia."
  - target: 01-human/03-molecular/tnf-alpha
    relation: connects-to
    note: "Marrow inflammation: TNF-α from the chronically stressed, expanded marrow of thalassemia contributes to its ineffective erythropoiesis and the inflammatory disturbance of iron handling."
  - target: 01-human/03-molecular/tlr4
    relation: connects-to
    note: "Heme danger signal: chronic haemolysis and ineffective erythropoiesis in thalassemia release free heme that engages TLR4, driving the sterile inflammation that compounds tissue and endothelial injury."
  - target: 01-human/03-molecular/rankl
    relation: connects-to
    note: "Thalassemic bone disease: marrow expansion and endocrine dysfunction drive RANKL-mediated osteoclast activation, causing the osteoporosis and fractures that are a major morbidity of thalassemia."
  - target: 01-human/03-molecular/bnp
    relation: connects-to
    note: "Iron cardiomyopathy: transfusional iron overload damages the myocardium, and natriuretic peptides like BNP rise as the resulting cardiomyopathy and heart failure develop — the leading cause of death in thalassemia."
  - target: 01-human/03-molecular/caspase-3
    relation: connects-to
    note: "Ineffective erythropoiesis: unpaired globin chains precipitate in maturing erythroblasts, triggering caspase-3-mediated apoptosis in the marrow — the ineffective erythropoiesis that, more than haemolysis, drives the anaemia of thalassemia."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "Extramedullary haematopoiesis: the erythropoietic drive of thalassemia expands marrow and seeds extramedullary haematopoiesis, with VEGF-driven angiogenesis supporting these masses and the skeletal expansion that deforms bone."
  - target: 01-human/03-molecular/von-willebrand-factor
    relation: connects-to
    note: "Thrombophilia: thalassemia, especially after splenectomy, is a hypercoagulable state in which abnormal red cells and endothelial activation with von Willebrand factor promote the venous and pulmonary thrombosis of the disease."
  - target: 01-human/03-molecular/bcl-2
    relation: connects-to
    note: "Ineffective erythropoiesis: the apoptosis of maturing erythroid precursors, governed by the balance of BCL-2-family survival proteins, is the core of the ineffective erythropoiesis of thalassemia, where most red-cell precursors die in the marrow before reaching the circulation."
  - target: 01-human/03-molecular/xanthine-oxidase
    relation: connects-to
    note: "Oxidative haemolysis: unpaired globin chains and free iron in thalassemic red cells generate reactive oxygen species, compounded by xanthine-oxidase activity, the oxidative damage that destabilises membranes and drives the chronic haemolysis."
  - target: 01-human/03-molecular/rage
    relation: connects-to
    note: "Iron-DAMP inflammation: chronic haemolysis and iron overload in thalassemia release free haem that signals through RAGE as a DAMP, sustaining the vascular inflammation that contributes to the endothelial dysfunction and thrombotic risk of the disease."
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "Iron-overload axis: expanded ineffective erythropoiesis in thalassemia suppresses hepcidin via erythroferrone and shifts the BMP-SMAD set-point, derepressing ferroportin (already mapped) to drive the iron overload that dominates non-transfusional disease."
  - target: 01-human/03-molecular/nfe2l2
    relation: connects-to
    note: "Oxidative defence: unpaired globin chains and excess iron generate severe oxidative stress in thalassemic erythroid cells, and the NRF2 antioxidant response is the key defence against this damage."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "Inflammatory iron block: chronic inflammation with IL-6 contributes to dysregulated iron homeostasis and an anaemia-of-chronic-disease component overlying the inherited anaemia of thalassemia."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "Ineffective erythropoiesis: TGF-β-superfamily ligands (activin-A already mapped) suppress late erythroid maturation through SMAD signalling (SMAD4 mapped), the axis blocked by luspatercept to relieve the ineffective erythropoiesis of thalassemia."
  - target: 01-human/03-molecular/myd88
    relation: connects-to
    note: "Heme-driven inflammation: TLR-MyD88-NF-κB innate signalling (TLR4 and NF-κB already mapped), driven by haemolysis-derived heme and oxidative damage, sustains the chronic inflammation that compounds the anaemia of thalassemia."
  - target: 01-human/03-molecular/thrombin
    relation: connects-to
    note: "Hypercoagulable state: chronic platelet and coagulation activation generates a thrombin-rich prothrombotic state (von Willebrand factor already mapped) underlying the thrombotic risk of thalassemia, especially after splenectomy."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "The erythropoietin receptor signals through JAK2 (EPO mapped); the markedly elevated EPO of thalassemia drives the expanded but ineffective erythropoiesis via this axis."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "EPO-driven PI3K-AKT signalling promotes erythroid progenitor survival, dysregulated in the ineffective erythropoiesis of thalassemia."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "EPO-ERK-MAPK signalling drives the erythroid proliferation that expands the marrow in thalassemia, contributing to its skeletal complications."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Galectin-3 amplifies the macrophage inflammation that accompanies iron overload and contributes to the organ fibrosis of thalassemia."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "IL-6-STAT3 signalling links the chronic inflammation of thalassemia to hepcidin regulation and the iron-loading anaemia."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "Cytosolic DNA released by the apoptosis of ineffective erythroid precursors can engage cGAS-STING, contributing to the inflammatory milieu of thalassemia."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "FOXO regulates the erythroid progenitor oxidative-stress and survival programs disrupted in the ineffective erythropoiesis of thalassemia."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "IFN-STAT1 signaling shapes the inflammatory tone accompanying the chronic hemolysis and transfusion exposure of thalassemia."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "S100A8/A9 alarmins reflect the chronic myeloid inflammatory activation linked to the iron overload of thalassemia."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "GSK-3β modulates the erythroid-progenitor survival and metabolic signaling relevant to the ineffective erythropoiesis of thalassemia."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "PI3K (PIK3CA)-AKT signaling (AKT already mapped) transduces the erythropoietin survival signal in the expanded but ineffective erythroid precursors of thalassemia."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK metabolic signaling participates in the oxidative and iron-overload stress responses of thalassemia."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Autophagy (including erythroid mitophagy and clearance of excess globin chains) participates in the ineffective erythropoiesis of thalassemia."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC-family kinase signaling downstream of EPO and cytokine receptors participates in the erythroid signaling of thalassemia."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "DNMT3A-mediated DNA methylation participates in the epigenetic regulation of globin genes and erythroid differentiation relevant to thalassemia."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-family chemokine signaling participates in the bone-marrow niche and inflammatory interactions of thalassemia."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "CXCL12-CXCR4 signaling participates in the erythroid bone-marrow-niche interactions and extramedullary hematopoiesis of thalassemia."
  - target: 01-human/03-molecular/kit
    relation: connects-to
    note: "KIT (stem-cell-factor receptor) signaling participates in the erythroid-progenitor proliferation and the ineffective erythropoiesis of thalassemia."
  - target: 01-human/03-molecular/runx1
    relation: connects-to
    note: "RUNX1 transcription-factor activity participates in the erythroid differentiation dysregulated in the ineffective erythropoiesis of thalassemia."
  - target: 01-human/03-molecular/notch
    relation: connects-to
    note: "NOTCH signaling participates in the hematopoietic-stem-cell and erythroid-progenitor regulation relevant to thalassemia."
  - target: 01-human/03-molecular/arid1a
    relation: connects-to
    note: "ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic regulation of globin-gene switching and erythroid gene programs relevant to thalassemia."
  - target: 01-human/03-molecular/insulin
    relation: connects-to
    note: "Iron-induced diabetes: iron deposition in the pancreatic islets of transfusion-dependent thalassaemia impairs insulin secretion, producing a secondary diabetes that is a common endocrine complication of the iron overload."
  - target: 01-human/03-molecular/testosterone
    relation: connects-to
    note: "Hypogonadism: iron loading of the pituitary and gonads causes hypogonadotropic hypogonadism with delayed puberty and infertility, among the most frequent endocrine complications of thalassaemia and its iron burden."
  - target: 01-human/03-molecular/mhc-class-ii
    relation: connects-to
    note: "Transfusion alloimmunisation: lifelong red-cell transfusion in thalassaemia provokes alloantibodies against blood-group antigens presented on MHC, complicating future cross-matching and transfusion support."
  - target: 01-human/03-molecular/thyroid-hormones
    relation: connects-to
    note: "Iron hypothyroidism: iron deposition in the thyroid causes hypothyroidism, one of the endocrinopathies of transfusional iron overload (already mapped) in thalassaemia that mandate regular endocrine surveillance."
  - target: 01-human/03-molecular/estrogen
    relation: connects-to
    note: "Hypogonadism in women: iron loading of the pituitary and gonads causes hypogonadotropic hypogonadism with estrogen deficiency (testosterone already mapped), delayed puberty and infertility, a frequent complication of thalassaemia."
  - target: 01-human/03-molecular/pth
    relation: connects-to
    note: "Iron hypoparathyroidism: iron deposition in the parathyroid glands can cause hypoparathyroidism with hypocalcaemia, another endocrine consequence of the iron overload that, with the bone disease (RANKL already mapped), harms the skeleton."
  - target: 01-human/03-molecular/protein-c
    relation: connects-to
    note: "Hypercoagulable state: thalassaemia, especially after splenectomy, carries a prothrombotic tendency from abnormal red-cell membranes and reduced natural anticoagulants such as protein C, contributing to the venous and pulmonary thrombosis seen in the disease."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "Inflammatory erythropoiesis: IL-1 and the inflammatory cytokines (TNF and IL-6 already mapped) accompany the ineffective erythropoiesis and iron overload of thalassaemia, part of the inflammatory milieu that also dysregulates hepcidin (already mapped)."
  - target: 01-human/03-molecular/cholesterol
    relation: connects-to
    note: "Low cholesterol: thalassaemia is characteristically associated with low serum cholesterol, attributed to the massively expanded erythropoiesis consuming cholesterol for red-cell membranes, an unusual lipid finding of the disease."
  - target: 01-human/05-tissue/cortical-bone
    relation: connects-to
    note: "Skeletal expansion: the massive marrow (already mapped) expansion of the ineffective erythropoiesis thins and deforms the cortical bone, causing the frontal bossing and the osteoporosis (RANKL and PTH already mapped) of untreated thalassaemia."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "M2 macrophage clearance: IL-4 polarises macrophages toward an M2 phenotype that clears the haemolysed and defective red cells, part of the immune and haemolytic microenvironment of thalassaemia (IL-6 and TNF already mapped)."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "Zinc depletion: zinc deficiency is common in thalassaemia, from the increased red-cell turnover and the iron-chelation therapy that also chelates zinc, contributing to the growth delay and immune dysfunction of the disease."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "M2 haemolytic clearance: IL-13, with IL-4 (already mapped), supports the M2 macrophage phenotype that clears the haemolysed and defective red cells, part of the immune and haemolytic microenvironment of thalassaemia."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Growth and endocrine axis: leptin reflects the growth delay and altered energy balance (growth hormone already mapped) of the ineffective erythropoiesis and endocrine dysfunction of thalassaemia."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Adipokine and iron-diabetes: adiponectin, with leptin (already mapped), is part of the adipokine dimension of the iron-induced diabetes (insulin already mapped) and metabolic complications of thalassaemia."
  - target: 01-human/04-cellular/erythrocyte
    relation: connects-to
    note: "Microcytic red cells: the globin (haemoglobin already mapped) imbalance precipitates in the erythrocytes, causing the ineffective erythropoiesis and the microcytic haemolytic anaemia of thalassaemia."
  - target: 01-human/06-organ/spleen
    relation: connects-to
    note: "Splenomegaly: the spleen enlarges (the extramedullary haematopoiesis, the red-cell destruction), the splenectomy sometimes needed in thalassaemia."
  - target: 01-human/07-system/malaria
    relation: connects-to
    note: "Malaria protection: the thalassaemia trait (haemoglobin already mapped), like sickle-cell, confers the malaria protection, the balancing selection of the endemic regions."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), is the adipose-inflammatory adipokine of the chronic-inflammatory and iron-overload (hepcidin already mapped) milieu of thalassaemia."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Th1 inflammation: the IFN-γ of the T cells is the type-II interferon arm of the chronic inflammation (IL-6 and TNF already mapped) of the ineffective erythropoiesis and iron overload of thalassaemia."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the immune-inflammatory dimension of thalassaemia."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune dysregulation of the ineffective erythropoiesis of thalassaemia."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "Th17 axis: IL-17A drives the Th17 arm of the chronic inflammation (IL-6 and TNF already mapped) of the iron overload and ineffective erythropoiesis of thalassaemia."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17 induction: IL-23 sustains the Th17 (IL-17 already mapped) arm of the chronic immune-inflammatory dimension of thalassaemia."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Haemolytic complement: the complement C3 activation contributes to the extravascular haemolysis and the transfusion alloimmunisation of thalassaemia."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "CD4 helper source: the CD4 T-helper cells are the source of the Th17 (IL-17 and IL-23 already mapped) cytokines of the chronic inflammation of the iron overload and ineffective erythropoiesis of thalassaemia."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the immune dysregulation of thalassaemia."
  - target: 01-human/03-molecular/complement-c5
    relation: connects-to
    note: "Terminal complement: the complement C5 and its C5a (with C3 already mapped) contribute to the complement activation on the haem-damaged red cells and the chronic inflammation of thalassaemia."
  - target: 01-human/03-molecular/c5ar1
    relation: connects-to
    note: "C5a receptor: the C5aR1 signalling (with the complement C3 and C5 already mapped) links the complement to the myeloid (macrophage already mapped) inflammation of the iron overload and ineffective erythropoiesis of thalassaemia."
  - target: 01-human/03-molecular/factor-h
    relation: connects-to
    note: "Complement regulation: factor H regulates the alternative complement pathway (complement C3, C5 and C5aR1 already mapped) whose control is challenged by the cell-free haem of thalassaemia."
  - target: 01-human/03-molecular/tslp
    relation: connects-to
    note: "Alarmin-erythroid axis: TSLP, from barrier epithelium and mast cells (already mapped), primes dendritic cells (already mapped) and amplifies the Th2/Treg imbalance of the chronic inflammation of the ineffective erythropoiesis of thalassaemia."
  - target: 01-human/03-molecular/bradykinin
    relation: connects-to
    note: "Kinin-haemolytic axis: bradykinin, via B1/B2 receptors on mast cells (already mapped) and endothelium, amplifies the vascular inflammation and the iron-overload vasculopathy of thalassaemia."
  - target: 01-human/03-molecular/c1-esterase-inhibitor
    relation: connects-to
    note: "Contact/complement brake: the C1-esterase inhibitor regulates the classical complement pathway (complement C3 already mapped) whose activation is challenged by the cell-free haem and the haemolytic vasculopathy of thalassaemia."
  - target: 01-human/03-molecular/histamine
    relation: connects-to
    note: "Mast-cell haemolytic effector: mast cells (already mapped), activated by cell-free haem from ineffective erythropoiesis, release histamine that amplifies the endothelial (already mapped) vasodilation and the vascular inflammation of the haemolytic vasculopathy of thalassaemia."
  - target: 01-human/03-molecular/melatonin
    relation: connects-to
    note: "Iron-overload antioxidant: melatonin, with its potent antioxidant and iron-chelation-related properties, is studied in thalassaemia for protection against the ROS-driven cardiac (already mapped) and hepatic (liver already mapped) iron-overload injury of thalassaemia."
  - target: 01-human/03-molecular/serotonin
    relation: connects-to
    note: "Platelet-serotonin thrombosis: serotonin, released by the hyperactivated platelets (already mapped) of thalassaemia, amplifies the vasoconstriction and the microvascular thrombosis of the thromboembolism (venous-thromboembolism already mapped) risk of thalassaemia."
  - target: 01-human/03-molecular/prolactin
    relation: connects-to
    note: "Thalassaemia prolactin: prolactin, via PRLR on macrophages (already mapped) and erythrocyte (already mapped) precursors, modulates haematopoiesis; hyperprolactinaemia amplifies the hepcidin (already mapped) and IL-6 (already mapped) iron-sequestration of thalassaemia."
  - target: 01-human/03-molecular/oxytocin
    relation: connects-to
    note: "Thalassaemia oxytocin: oxytocin, via OXTR on macrophages (already mapped) and erythrocyte (already mapped) precursors, attenuates haemolytic inflammation; oxytocin deficiency amplifies the IL-6 (already mapped) and TNF-α (already mapped) vasculopathy of thalassaemia."
  - target: 01-human/03-molecular/vasopressin
    relation: connects-to
    note: "Thalassaemia vasopressin: vasopressin, via V2 receptors on erythrocytes (already mapped) and endothelial cells (already mapped), modulates red-cell hydration; vasopressin excess amplifies haemolysis and the nitric-oxide (already mapped) vascular cascade of thalassaemia."
  - target: 01-human/02-atomic/selenium
    relation: connects-to
    note: "Thalassaemia selenium: selenium, as GPx in erythrocytes (already mapped) and macrophages (already mapped), limits haemolysis-driven ROS; selenium deficiency amplifies the NLRP3 (already mapped) and NF-κB (already mapped) iron-loading and vasculopathy cascade of thalassaemia."
  - target: 01-human/02-atomic/iodine
    relation: connects-to
    note: "Thalassaemia iodine: iodine-dependent thyroid hormones regulate erythropoiesis (erythropoietin already mapped) and bone-marrow (already mapped) haematopoietic activity; iodine deficiency amplifies the hepcidin (already mapped) and IL-6 (already mapped) cascade of thalassaemia."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "Thalassaemia sodium: sodium, via Na⁺/K⁺-ATPase on erythrocytes (already mapped) and endothelial cells (already mapped), regulates red-cell hydration; sodium dysregulation amplifies haemolysis and the nitric-oxide (already mapped) vascular cascade of thalassaemia."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "Thal magnesium: magnesium supports erythrocyte (already mapped) membrane integrity and macrophage (already mapped) anti-inflammatory resolution; magnesium deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) haemolytic inflammation in thalassemia."
  - target: 01-human/02-atomic/copper
    relation: connects-to
    note: "Thal copper: copper, via ceruloplasmin and SOD in erythrocytes (already mapped) and macrophages (already mapped), scavenges ROS; copper deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and iron (already mapped) overload haemolytic cascade in thalassemia."
  - target: 01-human/02-atomic/potassium
    relation: connects-to
    note: "Thal potassium: potassium efflux gates macrophage (already mapped) NLRP3; potassium loss amplifies NF-κB (already mapped) and IL-6 (already mapped) haemolytic inflammation and worsens erythrocyte (already mapped) membrane fragility in thalassemia."
  - target: 01-human/02-atomic/phosphorus
    relation: connects-to
    note: "Thal phosphorus: phosphorus, as ATP precursor in erythrocytes (already mapped) and macrophages (already mapped), maintains red-cell membrane integrity; phosphorus deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) haemolytic cascade of thalassemia."
  - target: 01-human/02-atomic/carbon
    relation: connects-to
    note: "Thal carbon: carbon, as metabolic backbone of erythrocytes (already mapped) and macrophages (already mapped), drives haemoglobin (already mapped) synthesis; carbon dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) haemolytic cascade of thalassemia."
  - target: 01-human/02-atomic/chloride
    relation: connects-to
    note: "Thal chloride: chloride, via KCC1 in erythrocytes (already mapped) and macrophages (already mapped), regulates red-cell volume; chloride dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and haemolytic cascade of thalassemia."
  - target: 01-human/02-atomic/hydrogen
    relation: connects-to
    note: "Thal hydrogen: hydrogen, via redox homeostasis in erythrocytes (already mapped) and macrophages (already mapped), quenches haemolytic ROS; hydrogen dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) haemolytic-inflammatory cascade of thalassemia."
  - target: 01-human/02-atomic/nitrogen
    relation: connects-to
    note: "Thal nitrogen: nitric oxide from erythrocytes (already mapped) and macrophages (already mapped) modulates vascular tone; nitrogen imbalance amplifies NF-κB (already mapped) and IL-6 (already mapped) and erythropoietin (already mapped) cascade of thalassemia."
  - target: 01-human/02-atomic/sulfur
    relation: connects-to
    note: "Thal sulfur: hydrogen sulfide from erythrocytes (already mapped) and macrophages (already mapped) modulates vascular tone; sulfur deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and erythropoietin (already mapped) cascade of thalassemia."
  - target: 01-human/03-molecular/pd-1
    relation: connects-to
    note: "Thal PD-1: PD-1 checkpoint signalling in T-cells (already mapped) and macrophages (already mapped) modulates immune tolerance; PD-1 dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and erythropoietin (already mapped) cascade of thalassemia."
  - target: 01-human/03-molecular/glp-1
    relation: connects-to
    note: "Thal glp-1: GLP-1 from macrophages (already mapped) and fibroblasts (already mapped) modulates thalassaemia metabolic tone; glp-1 dysregulation amplifies nf-kb (already mapped) and il-6 (already mapped) and hepcidin (already mapped) cascade of thalassemia."
  - target: 01-human/03-molecular/angiotensin-ii
    relation: connects-to
    note: "Thal angiotensin-ii: angiotensin-II from endothelial cells (already mapped) and macrophages (already mapped) drives haemolytic inflammation; angiotensin-ii excess amplifies nf-kb (already mapped) and il-6 (already mapped) and hepcidin (already mapped) cascade of thalassemia."
  - target: 01-human/03-molecular/wnt-beta-catenin
    relation: connects-to
    note: "Thal wnt-beta-catenin: WNT/β-catenin on erythrocytes (already mapped) and macrophages (already mapped) regulates haematopoietic recovery; wnt-beta-catenin loss amplifies nf-kb (already mapped) and il-6 (already mapped) and hepcidin (already mapped) cascade of thalassemia."
---

# Thalassemia

## Overview

**Thalassaemias** are the most common single-gene disorders globally, affecting ~5% of the world's population as carriers and causing significant morbidity in ~300,000 new cases annually [^weatherall-2008-thalassemia-review]. They arise from mutations or deletions in the **α-globin genes (*HBA1, HBA2*, chromosome 16p13.3)** or **β-globin gene (*HBB*, chromosome 11p15.4)** that reduce or abolish synthesis of the corresponding globin chains, creating an imbalance in the α:β chain ratio.

**Pathophysiological principle:** Normal haemoglobin requires stoichiometric synthesis of α and β chains. When one chain is reduced:
- **Excess unpaired chains:** The remaining chains form unstable homotetramers (e.g., HbH = β₄ in α-thalassaemia; γ₄ = Hb Bart's in hydrops fetalis) or precipitate as inclusion bodies (excess α chains in β-thalassaemia) → membrane damage → premature RBC destruction
- **Ineffective erythropoiesis:** In β-thalassaemia major, 70-80% of erythroblasts die in the bone marrow before maturing (vs. ~5-10% normally) → massive compensatory erythropoietic expansion → extramedullary haematopoiesis (liver, spleen) → bone marrow expansion → facial/skull deformity (chipmunk facies, frontal bossing)
- **Haemolytic anaemia:** Surviving abnormal RBCs haemolyse in circulation → chronic anaemia → high-output cardiac failure if untransfused

**Global distribution:**
- Highest prevalence: Mediterranean, Middle East, South/Southeast Asia, Africa (malaria-endemic regions — heterozygous advantage)
- β-thal carrier frequency: ~3-5% in Mediterranean; ~1-2% in UK South Asian population; ~15-20% in Cyprus and Sardinia
- α-thal gene deletions: highest in Southeast Asia (up to 30% carrier frequency); significant in sub-Saharan Africa

## Structure

### α-Thalassemia: Deletion subtypes

Normal: 4 α-globin genes (2 per chromosome 16: αα/αα)

| Genotype | Deletion | Phenotype | Hb findings |
|:---------|:---------|:---------|:-----------|
| **α-Thal trait (2-gene deletion)** | -α/-α (trans) or --/αα (cis) | Mild microcytic anaemia; usually asymptomatic | HbA₂ normal; MCV ↓; MCH ↓ |
| **HbH disease (3-gene deletion)** | --/-α | Moderate haemolytic anaemia (Hb 7-10 g/dL); splenomegaly | HbH (β₄) on Hb HPLC; Heinz bodies |
| **Hydrops fetalis (4-gene deletion)** | --/-- | Severe fetal anaemia + hydrops → stillbirth or early neonatal death | Hb Bart's (γ₄) ~80-90%; requires in utero transfusion |
| **Silent carrier (1-gene deletion)** | -α/αα | Normal; occasional MCH/MCV borderline ↓ | Normal Hb HPLC |

**Cis vs trans deletions:**
- **Cis (--/αα):** Both deletions on same chromosome → high risk of hydrops fetalis if partner also carries cis deletion; common in Southeast Asian and Chinese populations
- **Trans (-α/-α):** One deletion per chromosome → cannot produce hydrops; common in African populations

**Non-deletion α-thalassaemia:** Point mutations in HBA2 (e.g., Hb Constant Spring, Hb Paksé) → frameshift → elongated α-chain that is unstable; found in Southeast Asia; similar phenotype to HbH disease

### β-Thalassemia: Severity spectrum

| Severity | Genotype | Hb without transfusion | Clinical features |
|:---------|:---------|:-----------------------|:-----------------|
| **β-Thal trait (minor)** | β/β⁰ or β/β⁺ | Normal or mildly ↓ (10-13 g/dL) | Microcytic hypochromic; HbA₂ >3.5%; no treatment needed |
| **β-Thal intermedia** | β⁺/β⁺ (mild alleles) or β/β⁰ with HbF inducers | 7-10 g/dL | Moderate; splenomegaly; episodic transfusion; iron overload from GI absorption |
| **β-Thal major** | β⁰/β⁰ or β⁰/β⁺ (severe) | 3-6 g/dL without Tx | Severe; transfusion-dependent; iron overload; skeletal deformity; hydroxyurea or luspatercept to ↑HbF or ↓ineffective erythropoiesis |

**Common HBB mutations by population:**
- IVS1-110 (G→A): Mediterranean; severe β⁺
- Codon 39 (C→T): Sardinian, Algerian; β⁰
- IVS1-1 (G→T): Indian subcontinent, Chinese; β⁰
- IVS2-1 (G→A): South Asian; β⁰
- -28 (A→G): Chinese; mild β⁺

**β⁰ = no β-globin production; β⁺ = reduced β-globin production; β++ = very mildly reduced**

### Hb F induction — the therapeutic target

Foetal haemoglobin (HbF, α₂γ₂) is normally silenced after birth by BCL11A (downregulates γ-globin genes) and ZBTB7A/LRF. HbF:
- Compensates for HbS (dilutes polymer fraction) and HbβS (provides functional Hb)
- HbF >30% of total Hb → significantly ameliorates clinical course in both SCD and β-thal
- Spontaneously high HbF producers (hereditary persistence of fetal haemoglobin, HPFH) have very mild β-thal major or SCD

## Function

### Pathophysiology of iron overload in β-Thalassemia

**Mechanism of paradoxical iron overload despite anaemia:**
1. Severe anaemia + hypoxia → massive EPO secretion → stress erythropoiesis (BFU-E and CFU-E expansion in bone marrow + liver/spleen)
2. Stressed erythroblasts secrete **ERFE (erythroferrone; FAMP-domain protein)** → ERFE binds and sequesters BMPs (BMP2, BMP6) in liver → suppresses BMP-SMAD signaling → ↓ hepcidin transcription
3. Low hepcidin → ferroportin maintained on duodenal enterocytes + macrophages → unconstrained iron absorption (3-5× normal) and recycling
4. In transfused β-thal major patients: transfusion iron + GI absorption → combined overload
5. Once TSAT approaches 100%: NTBI forms → ZIP14-mediated uptake by hepatocytes, cardiomyocytes, pituitary → Fenton chemistry → ROS → fibrosis and cell death

**Target organs of iron overload:**
- **Liver:** Hepatic fibrosis → cirrhosis; monitor with serum ferritin + liver iron concentration (MRI T2* or R2)
- **Heart (most critical):** Cardiac iron deposition → arrhythmia, LV dysfunction, heart failure → most common cause of death in inadequately chelated thal major; monitor cardiac MRI T2* (>20 ms = normal; <10 ms = severe)
- **Endocrine glands:** Pituitary → hypogonadotropic hypogonadism (most common; delayed puberty, infertility); pancreas → diabetes mellitus; thyroid → hypothyroidism; parathyroids → hypoparathyroidism
- **Bone:** Osteoporosis from marrow expansion + reduced sex hormones; vertebral fractures

### Skeletal complications

Untransfused or undertransfused β-thal major:
- Erythroid marrow expansion into cortical bone → bone marrow hypertrophy → frontal bossing, maxillary overgrowth (chipmunk facies), widened diploe on skull X-ray (hair-on-end pattern)
- Spinal cord compression from paraspinal extramedullary haematopoiesis
- Fractures from cortical thinning + low bone density

## Pathology

### Diagnosis

**Haematological:**
- CBC: Microcytic hypochromic anaemia; MCV typically 60-75 fL in thal major; RBC count elevated relative to Hb (distinguishes from IDA)
- Blood smear: Target cells, hypochromic microcytic cells, nucleated RBCs, Heinz bodies (HbH), basophilic stippling
- Reticulocyte count: Elevated (compensatory) but lower than expected for degree of anaemia (ineffective erythropoiesis)

**Haemoglobin HPLC/electrophoresis:**
- β-thal trait: HbA₂ >3.5% (normal 2.0-3.5%); HbF mildly elevated (1-3%)
- β-thal major: HbF >90% (if β⁰/β⁰); HbA absent or reduced; HbA₂ variable
- α-thal trait (2-gene deletion): Normal HPLC (no diagnostic Hb variant); diagnosis by α-globin gene deletion PCR
- HbH disease: HbH (β₄) detectable on HPLC; brilliant cresyl blue stain → HbH inclusion bodies in RBCs

**Molecular diagnosis:**
- HBA1/HBA2 deletion PCR (gap-PCR) or multiplex MLPA for common α-thal deletions
- HBB sequencing or targeted mutation panel for β-thalassaemia mutations
- Essential for carrier screening, prenatal diagnosis (CVS or amniocentesis)

### Treatment

**Transfusion therapy [^cappellini-2014-thalassemia-guidelines]:**
- **Target Hb:** Pre-transfusion Hb ≥9-10 g/dL (some centers target ≥10-11 g/dL for better suppression of endogenous ineffective erythropoiesis); leucocyte-depleted packed RBCs
- **Frequency:** Every 2-5 weeks; HbS-negative blood for SCD/HbSβ patients; antigen-matched blood (at least Rh + Kell) to minimize alloimmunization
- **Alloimmunization:** Major complication; occurs in 20-30% of chronically transfused patients; antibodies to Rh, Kell, Kidd, Duffy antigens; complicates future transfusion; screen before each transfusion
- **Delayed haemolytic transfusion reaction (DHTR):** Severe complication in alloimmunized patients — bystander haemolysis → acute anaemia; treat with IVIG, rituximab, eculizumab; avoid further transfusion if possible

**Chelation therapy (iron overload management):**
- Begin when: serum ferritin >1,000 ng/mL OR ≥10-20 transfusion episodes; cardiac MRI T2* <20 ms
- **Deferoxamine (DFO):** SC infusion 8-12h, 5-7 nights/week; most evidence base; audiometry and ophthalmology monitoring annually; growth and endocrine monitoring in children
- **Deferasirox (Exjade/Jadenu):** 14-28 mg/kg/day PO once daily; most widely used; renal and hepatic monitoring; effective for liver and cardiac iron
- **Deferiprone (Ferriprox):** 75-100 mg/kg/day PO in divided doses; superior for cardiac iron chelation (crosses cell membranes); weekly CBC for agranulocytosis; often combined with DFO
- **Target:** Ferritin <1,000 ng/mL; cardiac MRI T2* >20 ms; liver iron concentration <5 mg/g dry weight

**Luspatercept (Reblozyl; FDA 2020 for β-thal):**
- Mechanism: Recombinant ActRIIA ligand trap → binds TGF-β superfamily ligands (GDF11, activin B) → reduces SMAD2/3 signaling → relieves late-stage erythroid differentiation block → improved erythropoiesis and ↓ transfusion burden
- BELIEVE trial: 21% reduction in transfusion burden vs. placebo in transfusion-dependent β-thal major; ~50% of patients reduced transfusions by >33%
- Dosing: 1.0 mg/kg SC every 21 days; can increase to 1.25 mg/kg; for non-transfusion-dependent thal intermedia (BEYOND trial: 74% achieved ≥1 g/dL Hb increase)

**Hydroxyurea:**
- Increases HbF synthesis; more effective in β-thal intermedia than major (residual β-chain synthesis required); reduces transfusion need in carefully selected patients; combined with erythropoietin in some protocols

**Haematopoietic cell transplantation (HCT):**
- Only established cure; best results in children <7 years, low hepatomegaly/fibrosis (Pesaro class I/II): ~90% event-free survival with MSD (matched sibling donor)
- Pesaro class III (older, hepatomegaly, irregular chelation): ~80% EFS with intensive conditioning
- Matched unrelated donor (MUD): Increasingly feasible; ~75-85% EFS in class I/II patients with experienced centers
- Haploidentical: Emerging; post-transplant cyclophosphamide reduces GvHD; ~75-80% EFS in recent series

**Gene therapy (transformative) [^thompson-2018-zynteglo-nejm]:**
- **Betibeglogene autotemcel (Zynteglo; FDA August 2022):** Lentiviral vector encoding βA-T87Q-globin → integrated into autologous HSCs; HGB-207/HGB-212 trials: 89% of patients with non-β⁰/β⁰ genotypes became transfusion-independent (Hb ≥9 g/dL without transfusion); β⁰/β⁰ patients: reduced transfusion burden; durable responses at 7+ years follow-up
- **Exagamglogene autotemcel (Casgevy; FDA December 2023):** CRISPR-Cas9 edits BCL11A erythroid enhancer → BCL11A silenced in erythroid cells → γ-globin de-repressed → HbF re-expression >25-30% → compensates for absent β-globin; CLIMB-THAL-111 trial: 39/42 patients became transfusion-independent with Hb ≥11 g/dL; also FDA-approved for SCD
- **Limitations:** Very expensive (Zynteglo ~$2.8M; Casgevy ~$2.2M per patient); requires busulfan myeloablative conditioning; academic centers with expertise; access inequities

### Prenatal diagnosis and prevention

- Carrier couples (both β-thal trait): 25% probability of thal major in each pregnancy
- Prenatal testing: Chorionic villus sampling (CVS) at 10-13 weeks → HBB molecular analysis; amniocentesis at 15-18 weeks; pre-implantation genetic diagnosis (PGD) with IVF
- Prevention programs: Cyprus, Sardinia, Iran have national programs → dramatically reduced thal major births; carrier screening in Mediterranean, South Asian, Chinese communities

## Connections

- `connects-to` → **[Hemoglobin](../../03-molecular/hemoglobin/README.md)** — Thalassaemias arise from imbalanced α- or β-globin chain synthesis; excess unpaired chains precipitate → ineffective erythropoiesis and haemolysis; HbA₂ (α2δ2) elevation >3.5% diagnoses β-thal trait; HbH (β4 tetramers) is the signature of 3-gene α-thal deletion.
- `connects-to` → **[Transferrin](../../03-molecular/transferrin/README.md)** — β-thal major: ineffective erythropoiesis → ERFE ↑ → hepcidin suppression → unconstrained iron absorption → TSAT 100% → NTBI → tissue deposition; deferasirox (oral) and deferoxamine (parenteral) are the mainstay chelators targeting transferrin-bound and NTBI iron.
- `connects-to` → **[Hepcidin](../../03-molecular/hepcidin/README.md)** — Ineffective erythropoiesis in β-thalassaemia → ERFE from stress erythroblasts → suppresses BMP-SMAD → ↓ hepcidin → ↑ ferroportin → unconstrained iron absorption despite anemia; luspatercept (ActRIIA ligand trap) reduces ineffective erythropoiesis and partially restores hepcidin.
- `connects-to` → **[Sickle Cell Disease](../sickle-cell-disease/README.md)** — HbSβ-thalassemia (HbS + β-thal allele) is a common SCD genotype; severity depends on β-thal allele type (β⁰ = severe SCA-like; β⁺ = milder); gene therapy approaches (Zynteglo, Casgevy) target both SCD and β-thal major as overlapping haemoglobinopathies.
- `connects-to` → **[G6PD](../../03-molecular/g6pd/README.md)** — Thalassaemia (HbE/β-thal most common in SEA) co-occurs with G6PD Mahidol/Viangchan; G6PD deficiency + beta-thalassaemia → additive oxidant haemolysis; G6PD screening is recommended in thalassaemia; both adaptations cluster in malaria-endemic regions by balanced selection.
- `connects-to` → **[Activin A](../../03-molecular/activin-a/README.md)** — Activin A/B → ActRIIB on late erythroblasts → SMAD2/3 → maturation block → ineffective erythropoiesis in beta-thalassemia; luspatercept (BELIEVE trial: 21% achieved ≥33% transfusion reduction vs. 4.5% placebo) traps activin A/B → accelerates terminal erythroid differentiation.
- `connects-to` → **[Erythrocyte](../../04-cellular/erythrocyte/README.md)** — In thalassemia the imbalance of α and β globin leaves unpaired chains that precipitate inside red cells, so most erythroblasts die in the marrow before maturing (ineffective erythropoiesis) and survivors are microcytic, hypochromic target cells that haemolyse.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Thalassemia causes iron overload despite anaemia: ineffective erythropoiesis releases erythroferrone that suppresses hepcidin, so dietary iron pours in unchecked and transfusions add more; the excess poisons heart, liver, and endocrine glands, making chelation lifesaving.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — Iron-loaded cardiomyocytes make the heart the leading killer in undertreated thalassaemia major: NTBI enters via calcium channels → Fenton free radicals → arrhythmia and cardiomyopathy; cardiac MRI T2* (<10 ms = severe) guides chelation before heart failure.
- `connects-to` → **[Malaria](../malaria/README.md)** — Thalassemia, like sickle trait, is a malaria-protective hemoglobinopathy: its high gene frequency across the Mediterranean, Middle East and Asia reflects balancing selection, as α- and β-thalassemia carriers resist severe Plasmodium falciparum—matching the historic malaria map.
- `connects-to` → **[Bone Marrow](../../05-tissue/bone-marrow/README.md)** — Thalassemia is driven by ineffective erythropoiesis: unbalanced globin chains precipitate and kill red-cell precursors in the marrow, which expands massively (skeletal deformities, extramedullary hematopoiesis); luspatercept eases this block and transfusions suppress the marrow.
- `connects-to` → **[Iron Deficiency Anemia](../iron-deficiency-anemia/README.md)** — Thalassemia trait is the key differential of iron-deficiency anemia: both cause microcytic, hypochromic cells, but thalassemia has normal/high iron, a low Mentzer index and raised HbA2 while IDA shows low ferritin—mislabeling it as IDA causes harmful needless iron use.
- `connects-to` → **[Spleen](../../06-organ/spleen/README.md)** — The spleen bears the brunt of thalassemia: it works overtime clearing defective red cells and hosts extramedullary hematopoiesis, enlarging massively and worsening anemia by trapping blood—so splenectomy is sometimes needed but leaves patients prone to sepsis.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — The liver is a major casualty of transfusion-dependent thalassemia: lifelong transfusions and increased gut iron absorption load the liver with iron, causing cirrhosis unless iron chelation is maintained—and hepatic iron quantified by MRI guides chelation therapy.
- `connects-to` → **[Osteoporosis](../osteoporosis/README.md)** — Thalassemia causes a distinctive osteoporosis: marrow expansion from chronic anemia thins cortical bone, while iron overload and endocrine damage impair osteoblasts and sex hormones—so fragility fractures are common and bone-density monitoring is part of care.
- `connects-to` → **[Erythropoietin](../../03-molecular/erythropoietin/README.md)** — Erythropoietin runs high in thalassemia: severe anemia drives massive EPO release, but defective globin chains make erythropoiesis ineffective, so the marrow expands uselessly—causing skeletal deformities and extramedullary hematopoiesis instead of functional red cells.
- `connects-to` → **[Oxygen](../../02-atomic/oxygen/README.md)** — Thalassemia impairs oxygen delivery at its root: too few normal hemoglobin tetramers mean less oxygen per red cell, so tissues stay hypoxic despite a racing marrow—and the hypoxic drive fuels the bone expansion and high-output cardiac strain of severe disease.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — Iron overload makes thalassemia an endocrine disease: transfusion and gut iron deposit in glands, causing diabetes, hypogonadism, hypothyroidism and growth failure, so the endocrine system bears much of the chronic morbidity—and iron chelation aims to prevent it.
- `connects-to` → **[Ferroportin](../../03-molecular/ferroportin/README.md)** — Ferroportin sits at the heart of thalassemia's iron overload: ineffective erythropoiesis suppresses hepcidin, freeing ferroportin to pump excess dietary iron into blood, so iron accumulates in heart and liver—the main cause of death in transfused patients.
- `connects-to` → **[Heart Failure](../heart-failure/README.md)** — Iron-overload cardiomyopathy is the leading killer in thalassemia: years of transfusion and gut iron absorption deposit iron in the myocardium, causing heart failure and arrhythmia, so iron chelation and cardiac MRI monitoring are central to survival.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — Thalassemia reshapes the skeleton: chronic anemia drives massive marrow expansion that thins and deforms bones—frontal bossing, a 'hair-on-end' skull and fracture-prone osteoporosis—so the musculoskeletal changes are a visible signature of untreated disease.
- `connects-to` → **[Placenta](../../06-organ/placenta/README.md)** — The placenta marks thalassemia's most severe form: alpha-thalassemia major (loss of all four genes) leaves the fetus unable to make functional hemoglobin, causing hydrops fetalis and stillbirth—so prenatal screening and intrauterine transfusion are how it is managed.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — Thalassemia shapes reproductive choices and function: carrier screening and genetic counseling guide family planning, while iron overload from transfusions damages the pituitary and gonads, causing delayed puberty and infertility—so fertility care is part of treatment.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Thalassemia's anemia is largely macrophage-driven: defective red cells and their precursors are destroyed by splenic and marrow macrophages (extravascular hemolysis and ineffective erythropoiesis), so splenomegaly and iron recycling stem from this clearance.
- `connects-to` → **[Pancreas](../../06-organ/pancreas/README.md)** — Iron overload in thalassemia poisons the pancreas: transfused and over-absorbed iron deposits in pancreatic islets, causing diabetes—one of the endocrine failures (with thyroid and gonads) that iron chelation aims to prevent.
- `connects-to` → **[Cytotoxic T Cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Thalassemia can be cured by replacing the marrow: an allogeneic stem-cell transplant—relying on donor cytotoxic T cells to engraft—or gene therapy gives patients a source of normal red cells, ending lifelong transfusions.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Iron overload disturbs calcium in thalassemia: iron-damaged parathyroids cause hypoparathyroidism and low calcium, while ineffective erythropoiesis and endocrinopathy weaken bone—so calcium and bone health are watched closely.
- `connects-to` → **[Cardiomyocyte](../../04-cellular/cardiomyocyte/README.md)** — Iron poisons the heart muscle in thalassemia: repeated transfusions deposit iron in cardiomyocytes, where it drives oxidative damage and arrhythmia, and this iron-overload cardiomyopathy is the leading cause of death—why iron chelation is lifesaving.
- `connects-to` → **[Thyroid Gland](../../06-organ/thyroid/README.md)** — Transfusional iron scars the thyroid: deposits in the gland cause hypothyroidism, one of the endocrine failures of chronic thalassemia, so thyroid function is monitored alongside the heart and pancreas in iron-overloaded patients.
- `connects-to` → **[Growth Hormone](../../03-molecular/growth-hormone/README.md)** — Iron damage to the pituitary stunts growth in thalassemia: overload harms the gland that makes growth hormone, so children can fail to grow and enter puberty late—endocrine complications that shape lifelong care beyond the anemia itself.
- `connects-to` → **[Zinc](../../02-atomic/zinc/README.md)** — Thalassemia treatment can strip away zinc: iron chelators that remove the excess iron also bind zinc, so deficiency is common and contributes to the poor growth and weakened immunity of chronically treated patients.
- `connects-to` → **[Osteoclast](../../04-cellular/osteoclast/README.md)** — Thalassemia weakens bone through osteoclasts: marrow expansion and hormone deficiencies tip the balance toward these bone-resorbing cells, driving the osteoporosis and fractures that complicate even well-transfused patients.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — Thalassemia shows in the skin: iron overload bronzes and greys the skin, while chronic anemia and poor circulation cause stubborn leg ulcers, outward marks of the disease's iron and oxygen problems.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — MRI now measures the iron itself: cardiac and liver T2* imaging in radiofrequency photons quantifies the overload that drives thalassemia's organ damage, guiding how hard to chelate.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — Thalassemia is prothrombotic: damaged red-cell membranes injure the endothelium and promote clotting, so venous thromboembolism is a real risk, especially after the spleen is removed.
- `connects-to` → **[Fibrosis](../../05-tissue/fibrosis/README.md)** — Iron overload scars the organs: deposited iron drives fibrosis in the liver toward cirrhosis and stiffens the heart, the cumulative damage that iron chelation aims to prevent.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy shows thalassemia's broken red cells: thin, pale target cells and precipitated unpaired globin chains clumped into inclusion bodies, the wreckage of ineffective erythropoiesis that destroys cells before they leave the marrow.
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — Both the disease and its cure stress the kidney: chronic iron overload and the very chelators used to remove it can injure the renal tubules, so kidney function is watched closely during lifelong treatment.
- `connects-to` → **[Eye](../../06-organ/eye/README.md)** — The chelation drugs can dim the eye: deferoxamine and related iron chelators are toxic to the retina and optic nerve, so regular eye exams guard the vision of patients on long-term treatment.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — Lifelong transfusions stir up antibodies: chronically transfused thalassemia patients form alloantibodies against donor red-cell antigens, making each future cross-match harder and the anemia more dangerous to treat.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — Blood-making spills outside the marrow and presses on nerves: extramedullary hematopoiesis forms paraspinal masses that can compress the spinal cord, a rare but reversible cause of weakness if caught early.
- `connects-to` → **[Platelet](../../04-cellular/platelet/README.md)** — Removing the spleen tips the blood toward clotting: splenectomized thalassemia patients develop a reactive thrombocytosis and a hypercoagulable state, raising the risk of thrombosis and pulmonary hypertension.
- `connects-to` → **[Adrenal Gland](../../06-organ/adrenal-gland/README.md)** — Iron overload poisons the endocrine glands: transfusional iron deposits in the adrenal as well as the pituitary, gonads, and pancreas, so adrenal insufficiency joins the diabetes and hypogonadism of poorly chelated thalassemia.
- `connects-to` → **[Neutrophil](../../04-cellular/neutrophil/README.md)** — Splenectomy strips a layer of defense: without the spleen's filtering, thalassemia patients face overwhelming infection by encapsulated bacteria despite their neutrophils, requiring vaccination and prompt antibiotics for fevers.
- `connects-to` → **[Vitamin D](../../../03-medicine/03-food/vitamin-d/README.md)** — Thalassemic bone is fragile and vitamin-D-poor: marrow expansion, iron's endocrine damage, and frequent vitamin D deficiency combine into the osteoporosis these patients carry, so vitamin D and calcium are part of bone care.
- `connects-to` → **[Venous Thromboembolism](../venous-thromboembolism/README.md)** — Thalassemia tips the blood toward clotting: abnormal red-cell membranes and the loss of the spleen's filtering leave a hypercoagulable state, so non-transfusion-dependent and splenectomized patients carry a raised risk of venous thrombosis.
- `connects-to` → **[Osteoblast](../../04-cellular/osteoblast/README.md)** — Thalassemic bone disease starts in the builder cell: iron and marrow expansion suppress osteoblasts while osteoclasts run on, tipping the balance to the early, severe osteoporosis characteristic of the disease.
- `connects-to` → **[Small Intestine](../../06-organ/small-intestine/README.md)** — The gut over-absorbs iron in thalassemia: the expanded, ineffective erythropoiesis suppresses hepcidin, so the small intestine keeps drinking in dietary iron and drives overload even in patients who are never transfused.
- `connects-to` → **[Pulmonary Arterial Hypertension](../pulmonary-arterial-hypertension/README.md)** — Chronic hemolysis pushes thalassemia toward pulmonary hypertension: free hemoglobin scavenges nitric oxide and the hypercoagulable, post-splenectomy state remodels the lung vessels, making PAH a leading cause of right heart failure and death.
- `connects-to` → **[Hepatitis C](../hepatitis-c/README.md)** — Decades of transfusion brought hepatitis C: before reliable blood screening, transfusion-dependent thalassemia carried high HCV rates, and the resulting chronic hepatitis compounds the iron overload that already injures the liver.
- `connects-to` → **[Nitric Oxide](../../03-molecular/nitric-oxide/README.md)** — Hemolysis robs the vessels of nitric oxide: cell-free hemoglobin released by fragile thalassemic red cells scavenges NO, so the vasodilator runs short — driving the endothelial dysfunction, pulmonary hypertension, and thrombosis of the disease.
- `connects-to` → **[Hepatocellular Carcinoma](../hcc/README.md)** — Iron and viral hepatitis turn the liver malignant: decades of transfusional iron overload, often with chronic hepatitis C, scar the liver into cirrhosis and a markedly raised risk of hepatocellular carcinoma.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — Iron overload inflames the organs through NF-κB: excess free iron generates reactive oxygen species that activate NF-κB in liver and heart, driving the inflammation behind the iron-laden organ damage of thalassemia.
- `connects-to` → **[Sepsis](../sepsis/README.md)** — Splenectomy and iron feed infection: removal of the spleen plus iron overload that nourishes bacteria like Yersinia leave thalassemia patients prone to severe infection and sepsis, a leading cause of death.
- `connects-to` → **[Chronic Kidney Disease](../ckd/README.md)** — Iron and chronic anemia wear on the kidney: iron-overload injury, the chelating drugs' nephrotoxicity and longstanding anemic hyperfiltration can leave a slow decline toward chronic kidney disease in thalassemia.
- `connects-to` → **[Gout](../gout/README.md)** — High cell turnover floods the blood with urate: the ineffective erythropoiesis and hemolysis of thalassemia generate excess purine breakdown, raising uric acid and predisposing to hyperuricemia and gout.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — Lifelong transfusion dependence weighs on mood: the burden of regular transfusions, iron chelation and a chronic inherited disease gives transfusion-dependent thalassemia a high rate of depression.
- `connects-to` → **[Type 2 Diabetes](../type-2-diabetes/README.md)** — Transfusional iron poisons the pancreas: repeated transfusions in thalassemia deposit iron in the islets, and the resulting beta-cell damage produces a secondary diabetes that is a classic endocrine complication.
- `connects-to` → **[Neisseria meningitidis](../../../02-pathogen/02-bacteria/neisseria-meningitidis/README.md)** — Splenectomy strips defense against encapsulated bacteria: many thalassemia patients undergo splenectomy for hypersplenism, leaving them vulnerable to meningococcus and other encapsulated organisms.
- `connects-to` → **[Stroke](../stroke/README.md)** — It carries a hidden clot risk: thalassemia, especially after splenectomy, is a hypercoagulable state with abnormal red cells and platelet activation that raises the risk of ischemic stroke.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — Iron overload and haemolysis hit the gut organs: transfusional iron scars the liver toward cirrhosis, chronic haemolysis forms pigment gallstones, and extramedullary haematopoiesis enlarges the spleen and liver.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — Iron and anaemia mark the skin: transfusional iron overload bronzes the skin like haemochromatosis, and chronic anaemia and poor perfusion cause leg ulcers over the ankles.
- `connects-to` → **[Generalized Anxiety Disorder](../generalized-anxiety-disorder/README.md)** — A lifelong transfusion-dependent disease breeds worry: the endless transfusions, iron-chelation burden and inherited nature of thalassemia foster chronic health anxiety alongside depression.
- `connects-to` → **[Cardiovascular System](../cardiovascular-system/README.md)** — Iron poisons the heart: transfusional iron overload deposits in the myocardium, causing a cardiomyopathy and arrhythmias that are the leading cause of death in thalassemia major.
- `connects-to` → **[Lymphatic System](../lymphatic-system/README.md)** — It swells the spleen: extramedullary haematopoiesis and ongoing red-cell destruction cause massive splenomegaly, often requiring splenectomy that then raises infection risk.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — Blood-making can compress the cord: paraspinal masses of extramedullary haematopoiesis in thalassemia can grow into the spinal canal and cause cord compression.
- `connects-to` → **[Immune System](../immune-system/README.md)** — Asplenia and iron overload weaken defence: splenectomy leaves vulnerability to encapsulated bacteria, while iron overload itself impairs immunity, making infection a leading cause of death in thalassemia.
- `connects-to` → **[Renal System](../renal-system/README.md)** — Disease and chelators both reach the kidney: chronic anaemia and iron overload cause tubular dysfunction, and the iron chelator deferasirox can be nephrotoxic, demanding renal monitoring.
- `connects-to` → **[Respiratory System](../respiratory-system/README.md)** — Iron and anaemia burden the lungs: chronic transfusion and haemolysis drive pulmonary hypertension and a restrictive ventilatory defect in thalassemia.
- `connects-to` → **[Streptococcus pneumoniae](../../../02-pathogen/02-bacteria/streptococcus-pneumoniae/README.md)** — Splenectomy invites encapsulated bacteria: removing the iron-overloaded, enlarged spleen leaves thalassaemia patients at lifelong risk of overwhelming pneumococcal sepsis, needing vaccination and prophylaxis.
- `connects-to` → **[Hepatocyte](../../04-cellular/hepatocyte/README.md)** — Iron overload poisons the liver: transfusional and absorptive iron loading deposits in hepatocytes, driving fibrosis, cirrhosis and hepatocellular carcinoma in chronically transfused thalassaemia.
- `connects-to` → **[MDS](../mds/README.md)** — A shared failure of red-cell making: like the myelodysplastic syndromes, thalassaemia features ineffective erythropoiesis, and the maturation agent luspatercept is now used to reduce transfusion needs in both.
- `connects-to` → **[Targeted Therapy](../../../03-medicine/01-modern/13-cancer/targeted-therapy/README.md)** — Gene therapy now offers a cure: lentiviral beti-cel and CRISPR-edited exa-cel restore functional haemoglobin and free transfusion-dependent β-thalassaemia patients from transfusions, alongside the iron-chelators that prevent organ damage.
- `connects-to` → **[Cancer Chemotherapy](../../../03-medicine/01-modern/13-cancer/cancer-chemotherapy/README.md)** — Hydroxyurea and transplant conditioning: hydroxyurea raises fetal haemoglobin to ease some thalassaemias, and intensive conditioning chemotherapy precedes the allogeneic stem-cell transplant that can cure the disease.
- `connects-to` → **[Cortical Bone](../../05-tissue/cortical-bone/README.md)** — Marrow expansion deforms the skeleton: ineffective erythropoiesis drives massive marrow hyperplasia that thins cortical bone, causing frontal bossing, the 'hair-on-end' skull, pathological fractures and osteoporosis.
- `connects-to` → **[Myocardium](../../05-tissue/myocardium/README.md)** — Iron-overload cardiomyopathy: transfusional iron deposits in the myocardium, causing the heart failure and arrhythmias that are the leading cause of death in transfusion-dependent thalassaemia—the target of iron chelation.
- `connects-to` → **[Hepatic Lobule](../../05-tissue/hepatic-lobule/README.md)** — Iron scars the liver: deposition of transfusional iron in the hepatic lobule drives fibrosis and cirrhosis, compounded by hepatitis C, a major complication tracked by liver iron quantification.
- `connects-to` → **[Brain](../../06-organ/brain/README.md)** — Extramedullary haematopoiesis: ineffective marrow pushes blood formation into masses outside the marrow, including paraspinal and intracranial deposits that can compress the cord or brain.
- `connects-to` → **[GVHD](../gvhd/README.md)** — A curative transplant: allogeneic stem-cell transplant can cure transfusion-dependent thalassemia, but graft-versus-host disease is a major risk—now joined by gene therapy as a cure.
- `connects-to` → **[Germinal Center](../../05-tissue/germinal-center/README.md)** — Alloimmunisation from transfusion: chronic red-cell transfusions in thalassemia drive germinal-centre antibody responses against donor red-cell antigens, complicating future cross-matching.
- `connects-to` → **[Cardiac Conduction System](../../05-tissue/cardiac-conduction-system/README.md)** — Iron and arrhythmia: transfusional iron overload injures the cardiac conduction system as well as the myocardium, causing arrhythmias that, with cardiomyopathy, are a leading cause of death in thalassemia.
- `connects-to` → **[Intestinal Epithelium](../../05-tissue/intestinal-epithelium/README.md)** — Duodenal iron absorption: thalassemia's ineffective erythropoiesis suppresses hepcidin, driving the intestinal epithelium to over-absorb dietary iron and worsening overload even without transfusion.
- `connects-to` → **[Aplastic Anemia](../aplastic-anemia/README.md)** — Aplastic crisis: parvovirus B19 infection or folate deficiency can abruptly shut down red-cell production in thalassemia's chronically haemolytic marrow, the same marrow-failure vulnerability central to aplastic anaemia.
- `connects-to` → **[Wound Healing](../wound-healing/README.md)** — Poor-healing leg ulcers: chronic anaemia, tissue hypoxia and sluggish perfusion in thalassemia produce stubborn lower-limb ulcers, a chronic wound-healing failure shared with sickle cell disease.
- `connects-to` → **[HIF-1α](../../03-molecular/hif-1alpha/README.md)** — Erythropoietic drive: chronic anaemia and hypoxia stabilise HIF-1α in thalassemia, driving the erythropoietin surge and marrow expansion behind its skeletal deformities and extramedullary haematopoiesis.
- `connects-to` → **[Endothelin-1](../../03-molecular/endothelin-1/README.md)** — Vascular complication: haemolysis and endothelial dysfunction raise endothelin-1 in thalassemia, contributing to the pulmonary hypertension that complicates the chronic anaemia.
- `connects-to` → **[TNF-α](../../03-molecular/tnf-alpha/README.md)** — Marrow inflammation: TNF-α from the chronically stressed, expanded marrow of thalassemia contributes to its ineffective erythropoiesis and the inflammatory disturbance of iron handling.
- `connects-to` → **[TLR4](../../03-molecular/tlr4/README.md)** — Heme danger signal: chronic haemolysis and ineffective erythropoiesis in thalassemia release free heme that engages TLR4, driving the sterile inflammation that compounds tissue and endothelial injury.
- `connects-to` → **[RANKL](../../03-molecular/rankl/README.md)** — Thalassemic bone disease: marrow expansion and endocrine dysfunction drive RANKL-mediated osteoclast activation, causing the osteoporosis and fractures that are a major morbidity of thalassemia.
- `connects-to` → **[BNP](../../03-molecular/bnp/README.md)** — Iron cardiomyopathy: transfusional iron overload damages the myocardium, and natriuretic peptides like BNP rise as the resulting cardiomyopathy and heart failure develop — the leading cause of death in thalassemia.
- `connects-to` → **[Caspase-3](../../03-molecular/caspase-3/README.md)** — Unpaired globin chains precipitate in maturing erythroblasts, triggering caspase-3-mediated apoptosis in the marrow—the ineffective erythropoiesis that, more than peripheral hemolysis, drives the anemia of thalassemia.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — The erythropoietic drive of thalassemia expands the marrow and seeds extramedullary hematopoiesis, with VEGF-driven angiogenesis supporting these masses and the skeletal expansion that deforms the skull and face.
- `connects-to` → **[von Willebrand factor](../../03-molecular/von-willebrand-factor/README.md)** — Thalassemia, especially after splenectomy, is a hypercoagulable state in which abnormal red cells and endothelial activation with von Willebrand factor promote the venous and pulmonary thrombosis that complicates the disease.
- `connects-to` → **[BCL-2](../../03-molecular/bcl-2/README.md)** — The apoptosis of maturing erythroid precursors, governed by the balance of BCL-2-family survival proteins, is the core of the ineffective erythropoiesis of thalassemia, where most red-cell precursors die in the marrow before reaching the circulation.
- `connects-to` → **[Xanthine Oxidase](../../03-molecular/xanthine-oxidase/README.md)** — Unpaired globin chains and free iron in thalassemic red cells generate reactive oxygen species, compounded by xanthine-oxidase activity, the oxidative damage that destabilizes membranes and drives the chronic hemolysis.
- `connects-to` → **[RAGE](../../03-molecular/rage/README.md)** — Chronic hemolysis and iron overload in thalassemia release free heme that signals through RAGE as a DAMP, sustaining the vascular inflammation that contributes to the endothelial dysfunction and thrombotic risk of the disease.
- `connects-to` → **[SMAD4](../../03-molecular/smad4/README.md)** — Expanded ineffective erythropoiesis in thalassemia suppresses hepcidin via erythroferrone and shifts the BMP-SMAD set-point, derepressing ferroportin (already mapped) to drive the iron overload that dominates non-transfusional disease.
- `connects-to` → **[NRF2](../../03-molecular/nfe2l2/README.md)** — Unpaired globin chains and excess iron generate severe oxidative stress in thalassemic erythroid cells, and the NRF2 antioxidant response is the key defense against this damage.
- `connects-to` → **[Interleukin-6](../../03-molecular/il-6/README.md)** — Chronic inflammation with IL-6 contributes to dysregulated iron homeostasis and an anemia-of-chronic-disease component overlying the inherited anemia of thalassemia.
- `connects-to` → **[Transforming Growth Factor Beta](../../03-molecular/tgf-beta/README.md)** — TGF-β-superfamily ligands (activin-A already mapped) suppress late erythroid maturation through SMAD signaling (SMAD4 mapped), the axis blocked by luspatercept to relieve the ineffective erythropoiesis of thalassemia.
- `connects-to` → **[MYD88](../../03-molecular/myd88/README.md)** — TLR-MyD88-NF-κB innate signaling (TLR4 and NF-κB already mapped), driven by hemolysis-derived heme and oxidative damage, sustains the chronic inflammation that compounds the anemia of thalassemia.
- `connects-to` → **[Thrombin](../../03-molecular/thrombin/README.md)** — Chronic platelet and coagulation activation generates a thrombin-rich prothrombotic state (von Willebrand factor already mapped) underlying the thrombotic risk of thalassemia, especially after splenectomy.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — The erythropoietin receptor signals through JAK2 (EPO mapped); the markedly elevated EPO of thalassemia drives the expanded but ineffective erythropoiesis via this axis.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — EPO-driven PI3K-AKT signaling promotes erythroid progenitor survival, dysregulated in the ineffective erythropoiesis of thalassemia.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — EPO-ERK-MAPK signaling drives the erythroid proliferation that expands the marrow in thalassemia, contributing to its skeletal complications.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Galectin-3 amplifies the macrophage inflammation that accompanies iron overload and contributes to the organ fibrosis of thalassemia.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — IL-6-STAT3 signaling links the chronic inflammation of thalassemia to hepcidin regulation and the iron-loading anemia.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — Cytosolic DNA released by the apoptosis of ineffective erythroid precursors can engage cGAS-STING, contributing to the inflammatory milieu of thalassemia.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — FOXO regulates the erythroid progenitor oxidative-stress and survival programs disrupted in the ineffective erythropoiesis of thalassemia.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — IFN-STAT1 signaling shapes the inflammatory tone accompanying the chronic hemolysis and transfusion exposure of thalassemia.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — S100A8/A9 alarmins reflect the chronic myeloid inflammatory activation linked to the iron overload of thalassemia.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β modulates the erythroid-progenitor survival and metabolic signaling relevant to the ineffective erythropoiesis of thalassemia.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — PI3K (PIK3CA)-AKT signaling (AKT already mapped) transduces the erythropoietin survival signal in the expanded but ineffective erythroid precursors of thalassemia.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK metabolic signaling participates in the oxidative and iron-overload stress responses of thalassemia.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — Autophagy (including erythroid mitophagy and clearance of excess globin chains) participates in the ineffective erythropoiesis of thalassemia.
- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — SRC-family kinase signaling downstream of EPO and cytokine receptors participates in the erythroid signaling of thalassemia.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — DNMT3A-mediated DNA methylation participates in the epigenetic regulation of globin genes and erythroid differentiation relevant to thalassemia.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-family chemokine signaling participates in the bone-marrow niche and inflammatory interactions of thalassemia.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — CXCL12-CXCR4 signaling participates in the erythroid bone-marrow-niche interactions and extramedullary hematopoiesis of thalassemia.
- `connects-to` → **[KIT](../../03-molecular/kit/README.md)** — KIT (stem-cell-factor receptor) signaling participates in the erythroid-progenitor proliferation and the ineffective erythropoiesis of thalassemia.
- `connects-to` → **[RUNX1](../../03-molecular/runx1/README.md)** — RUNX1 transcription-factor activity participates in the erythroid differentiation dysregulated in the ineffective erythropoiesis of thalassemia.
- `connects-to` → **[NOTCH](../../03-molecular/notch/README.md)** — NOTCH signaling participates in the hematopoietic-stem-cell and erythroid-progenitor regulation relevant to thalassemia.
- `connects-to` → **[ARID1A](../../03-molecular/arid1a/README.md)** — ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic regulation of globin-gene switching and erythroid gene programs relevant to thalassemia.
- `connects-to` → **[Insulin](../../03-molecular/insulin/README.md)** — Iron-induced diabetes: iron deposition in the pancreatic islets of transfusion-dependent thalassaemia impairs insulin secretion, producing a secondary diabetes that is a common endocrine complication of the iron overload.
- `connects-to` → **[Testosterone](../../03-molecular/testosterone/README.md)** — Hypogonadism: iron loading of the pituitary and gonads causes hypogonadotropic hypogonadism with delayed puberty and infertility, among the most frequent endocrine complications of thalassaemia and its iron burden.
- `connects-to` → **[MHC class II](../../03-molecular/mhc-class-ii/README.md)** — Transfusion alloimmunisation: lifelong red-cell transfusion in thalassaemia provokes alloantibodies against blood-group antigens presented on MHC, complicating future cross-matching and transfusion support.
- `connects-to` → **[Thyroid hormones](../../03-molecular/thyroid-hormones/README.md)** — Iron hypothyroidism: iron deposition in the thyroid causes hypothyroidism, one of the endocrinopathies of transfusional iron overload (already mapped) in thalassaemia that mandate regular endocrine surveillance.
- `connects-to` → **[Estrogen](../../03-molecular/estrogen/README.md)** — Hypogonadism in women: iron loading of the pituitary and gonads causes hypogonadotropic hypogonadism with estrogen deficiency (testosterone already mapped), delayed puberty and infertility, a frequent complication of thalassaemia.
- `connects-to` → **[PTH](../../03-molecular/pth/README.md)** — Iron hypoparathyroidism: iron deposition in the parathyroid glands can cause hypoparathyroidism with hypocalcaemia, another endocrine consequence of the iron overload that, with the bone disease (RANKL already mapped), harms the skeleton.
- `connects-to` → **[Protein C](../../03-molecular/protein-c/README.md)** — Hypercoagulable state: thalassaemia, especially after splenectomy, carries a prothrombotic tendency from abnormal red-cell membranes and reduced natural anticoagulants such as protein C, contributing to the venous and pulmonary thrombosis seen in the disease.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — Inflammatory erythropoiesis: IL-1 and the inflammatory cytokines (TNF and IL-6 already mapped) accompany the ineffective erythropoiesis and iron overload of thalassaemia, part of the inflammatory milieu that also dysregulates hepcidin (already mapped).
- `connects-to` → **[Cholesterol](../../03-molecular/cholesterol/README.md)** — Low cholesterol: thalassaemia is characteristically associated with low serum cholesterol, attributed to the massively expanded erythropoiesis consuming cholesterol for red-cell membranes, an unusual lipid finding of the disease.
- `connects-to` → **[Cortical bone](../../05-tissue/cortical-bone/README.md)** — Skeletal expansion: the massive marrow (already mapped) expansion of the ineffective erythropoiesis thins and deforms the cortical bone, causing the frontal bossing and the osteoporosis (RANKL and PTH already mapped) of untreated thalassaemia.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — M2 macrophage clearance: IL-4 polarises macrophages toward an M2 phenotype that clears the haemolysed and defective red cells, part of the immune and haemolytic microenvironment of thalassaemia (IL-6 and TNF already mapped).
- `connects-to` → **[Zinc](../../02-atomic/zinc/README.md)** — Zinc depletion: zinc deficiency is common in thalassaemia, from the increased red-cell turnover and the iron-chelation therapy that also chelates zinc, contributing to the growth delay and immune dysfunction of the disease.
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — M2 haemolytic clearance: IL-13, with IL-4 (already mapped), supports the M2 macrophage phenotype that clears the haemolysed and defective red cells, part of the immune and haemolytic microenvironment of thalassaemia.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Growth and endocrine axis: leptin reflects the growth delay and altered energy balance (growth hormone already mapped) of the ineffective erythropoiesis and endocrine dysfunction of thalassaemia.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — Adipokine and iron-diabetes: adiponectin, with leptin (already mapped), is part of the adipokine dimension of the iron-induced diabetes (insulin already mapped) and metabolic complications of thalassaemia.
- `connects-to` → **[Erythrocyte](../../04-cellular/erythrocyte/README.md)** — Microcytic red cells: the globin (haemoglobin already mapped) imbalance precipitates in the erythrocytes, causing the ineffective erythropoiesis and the microcytic haemolytic anaemia of thalassaemia.
- `connects-to` → **[Spleen](../../06-organ/spleen/README.md)** — Splenomegaly: the spleen enlarges (the extramedullary haematopoiesis, the red-cell destruction), the splenectomy sometimes needed in thalassaemia.
- `connects-to` → **[Malaria](../malaria/README.md)** — Malaria protection: the thalassaemia trait (haemoglobin already mapped), like sickle-cell, confers the malaria protection, the balancing selection of the endemic regions.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), is the adipose-inflammatory adipokine of the chronic-inflammatory and iron-overload (hepcidin already mapped) milieu of thalassaemia.
- `connects-to` → **[IFN-gamma](../../03-molecular/ifn-gamma/README.md)** — Th1 inflammation: the IFN-γ of the T cells is the type-II interferon arm of the chronic inflammation (IL-6 and TNF already mapped) of the ineffective erythropoiesis and iron overload of thalassaemia.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the immune-inflammatory dimension of thalassaemia.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune dysregulation of the ineffective erythropoiesis of thalassaemia.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — Th17 axis: IL-17A drives the Th17 arm of the chronic inflammation (IL-6 and TNF already mapped) of the iron overload and ineffective erythropoiesis of thalassaemia.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — Th17 induction: IL-23 sustains the Th17 (IL-17 already mapped) arm of the chronic immune-inflammatory dimension of thalassaemia.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Haemolytic complement: the complement C3 activation contributes to the extravascular haemolysis and the transfusion alloimmunisation of thalassaemia.
- `connects-to` → **[T-helper cell](../../04-cellular/t-helper-cell/README.md)** — CD4 helper source: the CD4 T-helper cells are the source of the Th17 (IL-17 and IL-23 already mapped) cytokines of the chronic inflammation of the iron overload and ineffective erythropoiesis of thalassaemia.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the immune dysregulation of thalassaemia.
- `connects-to` → **[Complement C5](../../03-molecular/complement-c5/README.md)** — Terminal complement: the complement C5 and its C5a (with C3 already mapped) contribute to the complement activation on the haem-damaged red cells and the chronic inflammation of thalassaemia.
- `connects-to` → **[C5aR1](../../03-molecular/c5ar1/README.md)** — C5a receptor: the C5aR1 signalling (with the complement C3 and C5 already mapped) links the complement to the myeloid (macrophage already mapped) inflammation of the iron overload and ineffective erythropoiesis of thalassaemia.
- `connects-to` → **[Factor H](../../03-molecular/factor-h/README.md)** — Complement regulation: factor H regulates the alternative complement pathway (complement C3, C5 and C5aR1 already mapped) whose control is challenged by the cell-free haem of thalassaemia.
- `connects-to` → **[TSLP](../../03-molecular/tslp/README.md)** — Alarmin-erythroid axis: TSLP, from barrier epithelium and mast cells (already mapped), primes dendritic cells (already mapped) and amplifies the Th2/Treg imbalance of the chronic inflammation of the ineffective erythropoiesis of thalassaemia.
- `connects-to` → **[Bradykinin](../../03-molecular/bradykinin/README.md)** — Kinin-haemolytic axis: bradykinin, via B1/B2 receptors on mast cells (already mapped) and endothelium, amplifies the vascular inflammation and the iron-overload vasculopathy of thalassaemia.
- `connects-to` → **[C1-Esterase Inhibitor](../../03-molecular/c1-esterase-inhibitor/README.md)** — Contact/complement brake: the C1-esterase inhibitor regulates the classical complement pathway (complement C3 already mapped) whose activation is challenged by the cell-free haem and the haemolytic vasculopathy of thalassaemia.
- `connects-to` → **[Histamine](../../03-molecular/histamine/README.md)** — Mast-cell haemolytic effector: mast cells (already mapped), activated by cell-free haem from ineffective erythropoiesis, release histamine that amplifies the endothelial (already mapped) vasodilation and the vascular inflammation of the haemolytic vasculopathy of thalassaemia.
- `connects-to` → **[Melatonin](../../03-molecular/melatonin/README.md)** — Iron-overload antioxidant: melatonin, with its potent antioxidant and iron-chelation-related properties, is studied in thalassaemia for protection against the ROS-driven cardiac (already mapped) and hepatic (liver already mapped) iron-overload injury of thalassaemia.
- `connects-to` → **[Serotonin](../../03-molecular/serotonin/README.md)** — Platelet-serotonin thrombosis: serotonin, released by the hyperactivated platelets (already mapped) of thalassaemia, amplifies the vasoconstriction and the microvascular thrombosis of the thromboembolism (venous-thromboembolism already mapped) risk of thalassaemia.
- `connects-to` → **[Prolactin](../../03-molecular/prolactin/README.md)** — Thalassaemia prolactin: prolactin, via PRLR on macrophages (already mapped) and erythrocyte (already mapped) precursors, modulates haematopoiesis; hyperprolactinaemia amplifies the hepcidin (already mapped) and IL-6 (already mapped) iron-sequestration of thalassaemia.
- `connects-to` → **[Oxytocin](../../03-molecular/oxytocin/README.md)** — Thalassaemia oxytocin: oxytocin, via OXTR on macrophages (already mapped) and erythrocyte (already mapped) precursors, attenuates haemolytic inflammation; oxytocin deficiency amplifies the IL-6 (already mapped) and TNF-α (already mapped) vasculopathy of thalassaemia.
- `connects-to` → **[Vasopressin](../../03-molecular/vasopressin/README.md)** — Thalassaemia vasopressin: vasopressin, via V2 receptors on erythrocytes (already mapped) and endothelial cells (already mapped), modulates red-cell hydration; vasopressin excess amplifies haemolysis and the nitric-oxide (already mapped) vascular cascade of thalassaemia.
- `connects-to` → **[Selenium](../../02-atomic/selenium/README.md)** — Haemolysis ROS scavenger: selenium, as GPx in erythrocytes (already mapped) and macrophages (already mapped), limits haemolysis-driven ROS; selenium deficiency amplifies the NLRP3 (already mapped) and NF-κB (already mapped) iron-loading and vasculopathy cascade of thalassaemia.
- `connects-to` → **[Iodine](../../02-atomic/iodine/README.md)** — Thyroid-erythropoiesis axis: iodine-dependent thyroid hormones regulate erythropoiesis (erythropoietin already mapped) and bone-marrow (already mapped) haematopoietic activity; iodine deficiency amplifies the hepcidin (already mapped) and IL-6 (already mapped) cascade of thalassaemia.
- `connects-to` → **[Sodium](../../02-atomic/sodium/README.md)** — Red-cell hydration: sodium, via Na⁺/K⁺-ATPase on erythrocytes (already mapped) and endothelial cells (already mapped), regulates red-cell hydration; sodium dysregulation amplifies haemolysis and the nitric-oxide (already mapped) vascular cascade of thalassaemia.
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — Thal magnesium: magnesium supports erythrocyte (already mapped) membrane integrity and macrophage (already mapped) anti-inflammatory resolution; magnesium deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) haemolytic inflammation in thalassemia.
- `connects-to` → **[Copper](../../02-atomic/copper/README.md)** — Thal copper: copper, via ceruloplasmin and SOD in erythrocytes (already mapped) and macrophages (already mapped), scavenges ROS; copper deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and iron (already mapped) overload haemolytic cascade in thalassemia.
- `connects-to` → **[Potassium](../../02-atomic/potassium/README.md)** — Thal potassium: potassium efflux gates macrophage (already mapped) NLRP3; potassium loss amplifies NF-κB (already mapped) and IL-6 (already mapped) haemolytic inflammation and worsens erythrocyte (already mapped) membrane fragility in thalassemia.
- `connects-to` → **[Phosphorus](../../02-atomic/phosphorus/README.md)** — Thal phosphorus: phosphorus, as ATP precursor in erythrocytes (already mapped) and macrophages (already mapped), maintains red-cell membrane integrity; phosphorus deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) haemolytic cascade of thalassemia.
- `connects-to` → **[Carbon](../../02-atomic/carbon/README.md)** — Thal carbon: carbon, as metabolic backbone of erythrocytes (already mapped) and macrophages (already mapped), drives haemoglobin (already mapped) synthesis; carbon dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) haemolytic cascade of thalassemia.
- `connects-to` → **[Chloride](../../02-atomic/chloride/README.md)** — Thal chloride: chloride, via KCC1 in erythrocytes (already mapped) and macrophages (already mapped), regulates red-cell volume; chloride dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and haemolytic cascade of thalassemia.
- `connects-to` → **[Hydrogen](../../02-atomic/hydrogen/README.md)** — Thal hydrogen: hydrogen, via redox homeostasis in erythrocytes (already mapped) and macrophages (already mapped), quenches haemolytic ROS; hydrogen dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) haemolytic-inflammatory cascade of thalassemia.
- `connects-to` → **[Nitrogen](../../02-atomic/nitrogen/README.md)** — Thal nitrogen: nitric oxide from erythrocytes (already mapped) and macrophages (already mapped) modulates vascular tone; nitrogen imbalance amplifies NF-κB (already mapped) and IL-6 (already mapped) and erythropoietin (already mapped) cascade of thalassemia.
- `connects-to` → **[Sulfur](../../02-atomic/sulfur/README.md)** — Thal sulfur: hydrogen sulfide from erythrocytes (already mapped) and macrophages (already mapped) modulates vascular tone; sulfur deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and erythropoietin (already mapped) cascade of thalassemia.
- `connects-to` → **[PD-1](../../03-molecular/pd-1/README.md)** — Thal PD-1: PD-1 checkpoint signalling in T-cells (already mapped) and macrophages (already mapped) modulates immune tolerance; PD-1 dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and erythropoietin (already mapped) cascade of thalassemia.
- `connects-to` → **[GLP-1](../../03-molecular/glp-1/README.md)** — Thal glp-1: GLP-1 from macrophages (already mapped) and fibroblasts (already mapped) modulates thalassaemia metabolic tone; glp-1 dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and Hepcidin (already mapped) cascade of thalassemia.
- `connects-to` → **[Angiotensin-II](../../03-molecular/angiotensin-ii/README.md)** — Thal angiotensin-ii: angiotensin-II from endothelial cells (already mapped) and macrophages (already mapped) drives haemolytic inflammation; angiotensin-ii excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and Hepcidin (already mapped) cascade of thalassemia.
- `connects-to` → **[Wnt/β-catenin](../../03-molecular/wnt-beta-catenin/README.md)** — Thal wnt-beta-catenin: WNT/β-catenin on erythrocytes (already mapped) and macrophages (already mapped) regulates haematopoietic recovery; wnt-beta-catenin loss amplifies NF-κB (already mapped) and IL-6 (already mapped) and Hepcidin (already mapped) cascade of thalassemia.

[^weatherall-2008-thalassemia-review]: Weatherall DJ. The inherited diseases of hemoglobin are an emerging global health burden. *Blood.* 2010;115(22):4331-4336. [doi:10.1182/blood-2010-01-251348](https://doi.org/10.1182/blood-2010-01-251348) · [PubMed 20233970](https://pubmed.ncbi.nlm.nih.gov/20233970/)
[^cappellini-2014-thalassemia-guidelines]: Cappellini MD, Cohen A, Porter J, et al. (eds). Guidelines for the Management of Transfusion Dependent Thalassaemia (TDT). 3rd ed. Thalassaemia International Federation; 2014.
[^thompson-2018-zynteglo-nejm]: Thompson AA, Walters MC, Kwiatkowski J, et al. Gene therapy in patients with transfusion-dependent β-thalassemia. *N Engl J Med.* 2018;378(16):1479-1493. [doi:10.1056/NEJMoa1705342](https://doi.org/10.1056/NEJMoa1705342) · [PubMed 29669226](https://pubmed.ncbi.nlm.nih.gov/29669226/)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
