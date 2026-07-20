---
schema: human-scale-entry/v1
id: sickle-cell-disease
name: Sickle Cell Disease
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-08
summary: "Sickle cell disease (SCD; HbS β-globin E6V; chr11p15.4) is a haemoglobinopathy causing HbS polymerization → RBC sickling → haemolytic anaemia, vaso-occlusion, end-organ damage; hydroxyurea ↑ HbF and reduces crises; voxelotor and crizanlizumab are newer FDA-approved therapies."
aliases: ["SCD", "sickle cell disease", "sickle cell anemia", "sickle cell anaemia", "HbSS", "HbSC disease", "haemoglobin S disease", "sickle-cell anaemia", "SCA"]
sources:
  - id: steinberg-1999-scd-management
    type: peer-reviewed
    cite: "Steinberg MH. Management of sickle cell disease. N Engl J Med. 1999;340(13):1021-1030."
    doi: "10.1056/NEJM199904013401307"
    pmid: "10099145"
    url: "https://doi.org/10.1056/NEJM199904013401307"
  - id: vichinsky-2000-acs-scd
    type: peer-reviewed
    cite: "Vichinsky EP, Neumayr LD, Earles AN, et al. Causes and outcomes of the acute chest syndrome in sickle cell disease. N Engl J Med. 2000;342(25):1855-1865."
    doi: "10.1056/NEJM200006223422502"
    pmid: "10861320"
    url: "https://doi.org/10.1056/NEJM200006223422502"
  - id: niaid-2014-scd-guidelines
    type: clinical-guideline
    cite: "Yawn BP, Buchanan GR, Afenyi-Annan AN, et al. Management of sickle cell disease: summary of the 2014 evidence-based report by expert panel members. JAMA. 2014;312(10):1033-1048."
    doi: "10.1001/jama.2014.10517"
    pmid: "25205765"
    url: "https://doi.org/10.1001/jama.2014.10517"
cross_links:
  - target: 01-human/03-molecular/hemoglobin
    relation: connects-to
    note: "HbS (α2βS2; β-globin E6V GAG→GTG) polymerizes when deoxygenated → long fibres → RBC sickling; HbF (α2γ2) inhibits HbS polymerization; HbSC (one HbS + HbC E6K allele) → milder but significant disease; HbSβ-thalassemia → intermediate severity."
  - target: 01-human/07-system/stroke
    relation: connects-to
    note: "SCD is the most common cause of stroke in children <10 years (cerebral vasculopathy; large vessel stenosis from repetitive sickling → moyamoya pattern); transcranial Doppler screening + chronic RBC transfusion reduces stroke risk by 92% (STOP trial)."
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "Renal medullary sickling (high osmolarity + low pO2 in vasa recta) → hyposthenuria; progressive CKD in ~30% HbSS by age 40; albuminuria → nephrotic syndrome; ACE inhibitors + hydroxyurea slow CKD progression; sickle cell nephropathy is a distinct histological entity."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "Chronic haemolysis → NO scavenging by free haemoglobin → pulmonary hypertension (PAH; tricuspid regurgitation velocity >2.5 m/s predicts mortality); cardiomegaly + high-output failure from chronic anaemia; sildenafil for SCD-PAH; echocardiographic screening at age 10."
  - target: 01-human/03-molecular/transferrin
    relation: connects-to
    note: "Chronic transfusion in SCD (stroke prevention, recurrent ACS; target HbS <30%) causes transfusional iron overload; serum ferritin >1,000 ng/mL → deferasirox chelation required; cardiac MRI T2* monitors iron deposition; TSAT 100% → NTBI → cardiomyopathy risk."
  - target: 01-human/07-system/thalassemia
    relation: connects-to
    note: "HbSβ-thalassemia (HbS + β-thal allele) is a common SCD genotype; β⁰ allele severity = HbSS; β⁺ = milder; shared gene therapy targets: Casgevy (CRISPR BCL11A derepression of γ-globin/HbF) is FDA-approved for both β-thal major and sickle cell disease."
  - target: 01-human/03-molecular/g6pd
    relation: connects-to
    note: "G6PD A− deficiency (10-20% sub-Saharan Africans) co-occurs with HbSS in ~5-10% of SCD patients; G6PD deficiency + SCD → additive oxidant haemolysis risk; avoid dapsone, rasburicase, and nitrofurantoin in G6PD-deficient SCD; G6PD screening recommended."
  - target: 01-human/07-system/malaria
    relation: connects-to
    note: "HbAS (sickle trait) confers ~60% protection against severe malaria (balanced polymorphism); HbSS patients in endemic regions face compounded risk: fever + dehydration → sickling crises; antimalarial prophylaxis planning is essential for HbSS in endemic areas."
  - target: 01-human/03-molecular/protein-c
    relation: connects-to
    note: "Acquired protein C deficiency is common in SCD: vaso-occlusive crisis → local thrombin burst → APC consumption; protein C levels inversely correlate with VOC frequency; SCD patients have reduced EPCR expression on ECs → impaired APC generation during hemolytic crises."
  - target: 01-human/04-cellular/erythrocyte
    relation: connects-to
    note: "Sickle cell disease is fundamentally a red-cell disease: HbS polymerizes when deoxygenated, distorting erythrocytes into rigid sickle shapes that hemolyze (anemia) and jam microvessels (vaso-occlusion); dehydration and adhesion molecules make the cells sticky and short-lived."
  - target: 01-human/06-organ/spleen
    relation: connects-to
    note: "The spleen is an early casualty of sickle cell disease: repeated sickling infarcts it, causing splenic sequestration crises in children then autosplenectomy in adults; the resulting functional asplenia raises infection risk, mandating vaccines and penicillin prophylaxis."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "Sickle cell disease is a hypercoagulable state: chronic hemolysis exposes phosphatidylserine and frees hemoglobin, activating platelets and coagulation while consuming protein C/S; VTE and pulmonary embolism are markedly increased atop the in-situ thrombosis of vaso-occlusion."
  - target: 01-human/07-system/pulmonary-arterial-hypertension
    relation: connects-to
    note: "Pulmonary hypertension is a deadly complication of sickle cell disease: chronic hemolysis scavenges nitric oxide and releases free hemoglobin and arginase, raising pulmonary vascular tone—an elevated tricuspid regurgitant jet marks much higher mortality."
  - target: 01-human/07-system/neuropathic-pain
    relation: connects-to
    note: "Pain in sickle cell disease is not only ischemic but increasingly neuropathic: repeated vaso-occlusive crises sensitize central and peripheral pain pathways, so chronic SCD pain takes on a neuropathic, opioid-resistant quality—calling for anticonvulsant adjuncts."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Splenic macrophages drive the extravascular hemolysis of sickle cell disease: they recognize and destroy rigid, sickled red cells, and recurrent splenic sequestration and infarction eventually leave patients functionally asplenic—hence lifelong sepsis risk."
  - target: 01-human/03-molecular/nitric-oxide
    relation: connects-to
    note: "Nitric oxide depletion drives sickle-cell vasculopathy: free hemoglobin from hemolysis scavenges NO, so vessels lose vasodilation and platelets activate—linking chronic hemolysis to pulmonary hypertension, stroke and leg ulcers beyond the acute vaso-occlusive crises."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "Oxygen tension triggers the sickling itself: deoxygenated HbS polymerizes and deforms red cells, so hypoxia, dehydration and acidosis precipitate vaso-occlusive crises—which is why low oxygen at altitude or in infection can set off a painful sickle crisis."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "The kidney is a major target of sickle-cell disease: the hypoxic, acidic renal medulla promotes sickling that damages the concentrating mechanism and glomeruli, causing impaired urine concentration, hematuria and progressive sickle nephropathy toward chronic kidney disease."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "Sickle cell disease is a disease of the endothelium as much as the red cell: sickled cells and free hemoglobin scavenge nitric oxide and inflame the vessel lining, so endothelial activation and adhesion trigger the painful vaso-occlusive crises."
  - target: 01-human/05-tissue/bone-marrow
    relation: connects-to
    note: "Sickle cell disease drives the bone marrow into overdrive: chronic hemolysis spurs erythroid hyperplasia that expands marrow and can cause aplastic crises when parvovirus halts it—and replacing the marrow by transplant or gene therapy can cure the disease."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "Sickle cell disease causes functional asplenia and immune vulnerability: repeated splenic infarction destroys the organ early in childhood, so patients are dangerously prone to encapsulated-bacterial sepsis—why prophylactic penicillin and vaccination are lifesaving."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "The lung is sickle cell disease's deadliest battleground: acute chest syndrome—sickling and infection in the pulmonary vessels—causes fever, chest pain, and hypoxia and is a leading cause of death, so it is treated urgently with transfusion and antibiotics."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "Sickle cell disease attacks the musculoskeletal system: vaso-occlusion infarcts bone, causing painful crises, dactylitis in infants, and avascular necrosis of the hip, so the skeleton bears much of the chronic damage and disability of the disease."
  - target: 01-human/06-organ/eye
    relation: connects-to
    note: "Sickle cell disease threatens sight: sickling in the tiny retinal vessels causes ischemia and proliferative sickle retinopathy with fragile new vessels that bleed or detach the retina—so regular eye screening protects vision in older patients."
  - target: 01-human/02-atomic/iron
    relation: connects-to
    note: "Chronic transfusions for sickle cell load the body with iron: repeated red-cell transfusions for stroke prevention and anemia deposit iron in the heart, liver and endocrine organs, so iron chelation is needed to prevent overload damage."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "Neutrophils help trigger sickle cell pain crises: activated neutrophils and adhesion molecules glue sickled cells to vessel walls, starting the vaso-occlusion behind painful crises—so anti-adhesion therapy (crizanlizumab) targets this step."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "Sickle cell disease burdens the liver: chronic hemolysis forms pigment gallstones, and sickling in hepatic vessels can cause sequestration and crises, so right-upper-quadrant pain in sickle cell needs evaluation of gallbladder and liver."
  - target: 01-human/04-cellular/platelet
    relation: connects-to
    note: "Sickle cell disease makes blood prone to clot: hemolysis and inflamed vessels activate platelets that clump with sickled cells and white cells, helping plug small vessels and adding a thrombotic layer to the painful vaso-occlusive crises."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "The brain is a prime casualty of sickle cell: blocked and narrowed vessels cause overt strokes and silent infarcts that erode cognition in children, which is why transcranial Doppler screening and transfusion are used to prevent them."
  - target: 01-human/02-atomic/potassium
    relation: connects-to
    note: "Potassium loss is a hidden driver of sickling: the red cell's Gardos channel lets potassium and water leak out, dehydrating the cell and concentrating hemoglobin S so it polymerizes faster—making the channel a drug target in sickle cell."
  - target: 01-human/02-atomic/hydrogen
    relation: connects-to
    note: "Acid speeds the sickling in sickle cell: a drop in blood pH (from exercise, infection, or dehydration) lowers hemoglobin's oxygen affinity and pushes HbS to polymerize, so acidosis helps tip a vaso-occlusive crisis."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "Sickle cell strains the heart two ways: lifelong anemia forces high-output work that enlarges it, and the iron from repeated transfusions deposits in the muscle, together driving heart failure over time."
  - target: 01-human/04-cellular/smooth-muscle-cell
    relation: connects-to
    note: "Sickle cell deranges vascular smooth muscle: free hemoglobin scavenges nitric oxide, the relaxant these cells depend on, so vessels constrict—causing the priapism and pulmonary hypertension that mark its vasculopathy."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Imaging guards against sickle cell's silent damage: MRI catches the brain's silent infarcts, and X-rays reveal the bone infarcts and acute chest syndrome that mark vaso-occlusive crises."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "Sickle cell ulcerates the skin: chronic leg ulcers around the ankles, from poor blood flow and sickling in small vessels, are a painful, slow-healing hallmark in adults."
  - target: 01-human/05-tissue/fibrosis
    relation: connects-to
    note: "Repeated sickling scars the organs: chronic microvascular ischemia drives fibrosis in the spleen (autosplenectomy), kidney and liver, the cumulative end-organ damage of the disease."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy shows why the cell sickles: when oxygen drops, hemoglobin S polymerizes into long stiff fibers that warp the red cell into a rigid crescent, the molecular event that jams the microvasculature."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "Sickle cell disease runs short on zinc: chronic hemolysis and high turnover deplete it, and because zinc supports growth and immunity, supplementation can reduce infections and pain crises in deficient patients."
  - target: 01-human/06-organ/large-intestine
    relation: connects-to
    note: "Sickling can choke the gut: vaso-occlusion in the mesenteric vessels causes the abdominal 'girdle syndrome' of pain and ileus, while chronic hemolysis breeds the pigment gallstones that trouble many patients."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "Sickling strikes the reproductive organs: priapism — a painful, prolonged erection from vaso-occlusion in the penis — is a urologic emergency, and the disease complicates fertility and raises the risks of pregnancy."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "Transfusions stir up antibodies: repeatedly transfused patients form alloantibodies against donor red-cell antigens, making future cross-matching hard — while the newer drug crizanlizumab is itself an anti-P-selectin antibody that blocks vaso-occlusion."
  - target: 01-human/04-cellular/osteoblast
    relation: connects-to
    note: "Sickling starves the bones: vaso-occlusion infarcts the marrow and kills the femoral head in avascular necrosis, while in children it swells the hands and feet as the dactylitis that is often the first sign."
  - target: 02-pathogen/02-bacteria/streptococcus-pneumoniae
    relation: connects-to
    note: "Lose the spleen, lose the defense: repeated infarction autosplenectomizes sickle-cell patients, leaving them prey to encapsulated bacteria like Streptococcus pneumoniae and overwhelming sepsis — countered by penicillin prophylaxis and vaccination."
  - target: 01-human/04-cellular/osteoclast
    relation: connects-to
    note: "The infarcted skeleton remodels and weakens: chronic marrow expansion and bone infarction rev up osteoclast resorption into low bone density, and the dead, infarcted bone is uniquely prone to Salmonella osteomyelitis."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "Magnesium guards the red cell's water: sickle erythrocytes leak magnesium and potassium and dehydrate, which concentrates hemoglobin S and speeds sickling, so magnesium repletion is studied to keep the cells hydrated."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "Sickle disease smolders with inflammation: even between crises IL-6 and other cytokines run high, priming the endothelium and white cells that drive the vaso-occlusion at the heart of the disease."
  - target: 01-human/07-system/aplastic-anemia
    relation: connects-to
    note: "A virus can stall the marrow's overdrive: parvovirus B19 shuts down red-cell production for days, and in sickle disease — where survival depends on furious red-cell turnover — this triggers a sudden, dangerous aplastic crisis."
  - target: 01-human/06-organ/small-intestine
    relation: connects-to
    note: "Vaso-occlusion can strike the gut: sickled cells clog the mesenteric vessels in a crisis, starving the bowel into the ischemic abdominal pain of the 'girdle syndrome,' a visceral face of the disease."
  - target: 01-human/03-molecular/adenosine
    relation: connects-to
    note: "Adenosine has a double role in sickle disease: signaling through the A2B receptor it raises red-cell 2,3-BPG and promotes sickling, while via A2A it dampens the inflammatory pain of crises — a pathway probed for new therapies."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "Mast cells stoke the pain of sickle crises: activated in the vaso-occlusive milieu they release substance P and inflammatory mediators that sensitize nerves and worsen the neurogenic component of sickle pain."
  - target: 01-human/07-system/sepsis
    relation: connects-to
    note: "Functional asplenia makes sepsis the great killer in sickle disease: repeated infarction destroys the spleen, so encapsulated bacteria can cause overwhelming sepsis — the reason for penicillin prophylaxis and pneumococcal vaccination from infancy."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "Vaso-occlusion runs on NF-κB-driven stickiness: hemolysis and hypoxia activate NF-κB in endothelium and leukocytes, switching on the adhesion molecules that glue sickled cells to vessel walls and ignite the painful crisis."
  - target: 02-pathogen/02-bacteria/salmonella-typhi
    relation: connects-to
    note: "A classic pairing of infarcted bone and an unusual bug: in sickle cell disease, Salmonella is the characteristic cause of osteomyelitis, seeding bone made dead by vaso-occlusion in a patient whose spleen no longer clears it."
  - target: 01-human/07-system/hcc
    relation: connects-to
    note: "Transfusions and liver injury raise the cancer stakes: repeated transfusion causes iron overload while intrahepatic sickling damages the liver, and the resulting fibrosis can, over time, give rise to hepatocellular carcinoma."
  - target: 01-human/07-system/osteoporosis
    relation: connects-to
    note: "The marrow and infarcts weaken the skeleton: chronic marrow hyperplasia, bone infarction and delayed growth in sickle cell disease leave low bone density and a high rate of osteoporosis and avascular necrosis."
  - target: 01-human/07-system/heart-failure
    relation: connects-to
    note: "Anemia and iron strain the heart: the chronic high-output state of sickle anemia, transfusional iron loading of the myocardium and pulmonary hypertension together drive a cardiomyopathy and heart failure."
  - target: 01-human/07-system/opioid-use-disorder
    relation: connects-to
    note: "A lifetime of pain crises courts dependence: the recurrent severe vaso-occlusive pain of sickle cell disease requires repeated and long-term opioids, carrying a real risk of tolerance and opioid use disorder."
  - target: 01-human/07-system/wound-healing
    relation: connects-to
    note: "Vaso-occlusion ulcerates the legs: chronic ischemia and impaired perfusion in sickle cell disease produce the painful, recurrent leg ulcers over the ankles that are notoriously slow to heal."
  - target: 02-pathogen/02-bacteria/neisseria-meningitidis
    relation: connects-to
    note: "Autosplenectomy strips defense against encapsulated bacteria: repeated splenic infarction leaves sickle cell patients functionally asplenic and vulnerable to meningococcus, alongside pneumococcus and Salmonella."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "Lifelong pain and disease weigh on mood: the recurrent crises, hospitalizations, stigma and chronic pain of sickle cell disease carry a substantial burden of depression and reduced quality of life."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "Acute chest syndrome is its great killer: vaso-occlusion in the pulmonary vasculature causes acute chest syndrome with hypoxia and infiltrates, the leading cause of death in sickle cell disease."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "Chronic haemolysis stones the gallbladder: the constant red-cell breakdown of sickle cell disease forms pigment gallstones, and splenic and hepatic sequestration crises swell and threaten these organs."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "It carves chronic ulcers into the skin: sickle cell disease causes intractable leg ulcers over the ankles from microvascular occlusion and poor healing, a painful, recurring cutaneous complication."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "It silently scars the brain: beyond overt stroke, sickle cell disease causes silent cerebral infarcts, cognitive impairment and a moyamoya-like cerebral vasculopathy, especially in children."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "It stunts growth and hormones: chronic anaemia delays growth and puberty, and transfusional iron overload damages the pituitary and gonads, causing hypogonadism and hypopituitarism."
  - target: 01-human/07-system/lymphatic-system
    relation: connects-to
    note: "It destroys its own spleen: repeated splenic infarction causes autosplenectomy and functional asplenia, leaving lifelong vulnerability to encapsulated bacteria and the need for vaccination."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "Sickle cell nephropathy is near-universal: sickling in the renal medulla causes hyposthenuria, papillary necrosis and haematuria, progressing through proteinuric FSGS to chronic kidney disease."
  - target: 03-medicine/01-modern/04-cardio/ace-inhibitors
    relation: connects-to
    note: "They protect the sickle kidney: ACE inhibitors reduce the proteinuria of sickle cell nephropathy, slowing the decline towards kidney failure."
  - target: 03-medicine/03-food/zinc-dietary
    relation: connects-to
    note: "Chronic haemolysis drains zinc: urinary zinc loss in sickle cell disease contributes to growth retardation, delayed puberty and impaired immunity, and supplementation can help."
  - target: 03-medicine/01-modern/06-antimicrobial/amoxicillin
    relation: connects-to
    note: "Daily antibiotic shields the child: because sickle cell disease destroys the spleen early, prophylactic penicillin or amoxicillin is given through childhood to prevent overwhelming pneumococcal sepsis."
  - target: 02-pathogen/02-bacteria/staphylococcus-aureus
    relation: connects-to
    note: "It seeds infarcted bone: alongside Salmonella, Staphylococcus aureus is a leading cause of the osteomyelitis that complicates the bone infarcts of sickle cell disease."
  - target: 01-human/07-system/iron-deficiency-anemia
    relation: connects-to
    note: "Opposite iron problems: unlike iron-deficiency anaemia, sickle cell is a haemolytic anaemia where repeated transfusion brings iron overload, so the two need opposite iron management."
  - target: 03-medicine/01-modern/13-cancer/cancer-chemotherapy
    relation: connects-to
    note: "Hydroxyurea is the cornerstone: the chemotherapy agent hydroxyurea raises fetal haemoglobin in sickle cell disease, reducing the painful crises, acute chest syndrome and need for transfusion — its first disease-modifying drug."
  - target: 03-medicine/01-modern/13-cancer/targeted-therapy
    relation: connects-to
    note: "New molecular and gene therapies: crizanlizumab against P-selectin and voxelotor stabilising oxygenated haemoglobin reduce crises, while CRISPR (exa-cel) and lentiviral gene therapies now offer a one-time cure by reactivating fetal haemoglobin."
  - target: 01-human/05-tissue/cortical-bone
    relation: connects-to
    note: "Vaso-occlusion infarcts bone: sickling blocks the bone microcirculation, causing dactylitis, painful bone infarcts, avascular necrosis of the femoral head and a predisposition to Salmonella osteomyelitis."
  - target: 01-human/05-tissue/alveolus
    relation: connects-to
    note: "Acute chest syndrome: vaso-occlusion and fat embolism in the pulmonary alveoli cause acute chest syndrome with hypoxaemia and infiltrates, the leading cause of death in sickle cell disease."
  - target: 01-human/05-tissue/glomerulus
    relation: connects-to
    note: "Sickle nephropathy: sickling in the renal medulla and chronic hyperfiltration injure the glomerulus, causing proteinuria, papillary necrosis and progression to chronic kidney disease."
  - target: 01-human/06-organ/placenta
    relation: connects-to
    note: "Sickling in pregnancy: vaso-occlusion and poor oxygen delivery damage the placenta, raising the risk of miscarriage, growth restriction and pre-eclampsia in sickle cell pregnancies."
  - target: 01-human/05-tissue/arterial-wall
    relation: connects-to
    note: "Vasculopathy and stroke: sickle cell disease damages the arterial wall, narrowing cerebral arteries into a moyamoya pattern that causes the strokes screened for with transcranial Doppler in children."
  - target: 01-human/05-tissue/myocardium
    relation: connects-to
    note: "Iron-overload cardiomyopathy: repeated transfusions for sickle cell disease deposit iron in the myocardium, causing cardiomyopathy and arrhythmia unless removed by chelation."
  - target: 01-human/05-tissue/germinal-center
    relation: connects-to
    note: "Functional asplenia and immunity: autoinfarction of the spleen removes a key site of germinal-centre responses to encapsulated bacteria, mandating vaccination and penicillin prophylaxis in sickle cell disease."
  - target: 01-human/07-system/rsv
    relation: connects-to
    note: "Acute chest syndrome trigger: RSV and other respiratory viruses precipitate acute chest syndrome—the vaso-occlusive lung crisis that is a leading cause of death in sickle cell disease."
  - target: 01-human/07-system/gvhd
    relation: connects-to
    note: "A curative transplant's risk: allogeneic stem-cell transplant can cure sickle cell disease but carries graft-versus-host disease, the key trade-off alongside newer gene therapies."
  - target: 01-human/05-tissue/cardiac-conduction-system
    relation: connects-to
    note: "Iron and rhythm: chronic haemolysis and transfusional iron load the heart in sickle cell disease, scarring the myocardium and conduction system toward arrhythmia and sudden death."
  - target: 01-human/03-molecular/endothelin-1
    relation: connects-to
    note: "Vaso-occlusive vasoconstriction: free haemoglobin and endothelial injury raise endothelin-1 in sickle cell disease, whose vasoconstriction aggravates vaso-occlusion and pulmonary hypertension."
  - target: 01-human/03-molecular/tnf-alpha
    relation: connects-to
    note: "Inflammatory adhesion: TNF-α from the chronic inflammation of sickle cell disease upregulates endothelial adhesion molecules, promoting the sickle-cell and leukocyte adhesion that triggers vaso-occlusion."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "Hypoxic response: tissue hypoxia from vaso-occlusion stabilises HIF-1α, driving the erythropoietin surge and angiogenic and inflammatory responses of sickle cell disease."
  - target: 01-human/03-molecular/tlr4
    relation: connects-to
    note: "Heme danger signal: free heme released by intravascular haemolysis acts as a TLR4 agonist, driving the sterile inflammation and endothelial activation that initiate vaso-occlusive crises."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "Neutrophil alarmin: S100A8/A9 from activated neutrophils amplifies the inflammation and adhesion of sickle cell disease, contributing to the leukocyte-driven vaso-occlusion of painful crises."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "Ischaemic angiogenesis: chronic hypoxia drives VEGF-mediated neovascularisation, underlying the proliferative sickle retinopathy and aberrant vessel growth that threaten vision in the disease."
  - target: 01-human/03-molecular/von-willebrand-factor
    relation: connects-to
    note: "Adhesive vaso-occlusion: endothelial activation in sickle cell disease releases ultra-large von Willebrand factor multimers that, with relatively reduced ADAMTS13, promote platelet and sickle-cell adhesion in the microvasculature."
  - target: 01-human/03-molecular/pf4
    relation: connects-to
    note: "Platelet thromboinflammation: chronically activated platelets in sickle cell disease release platelet factor 4 and procoagulant mediators that contribute to the thrombo-inflammation driving vaso-occlusive crises."
  - target: 01-human/03-molecular/hepcidin
    relation: connects-to
    note: "Transfusional iron overload: repeated red-cell transfusions load the body with iron, and the resulting parenchymal iron deposition (with dysregulated hepcidin) damages heart, liver and endocrine organs unless chelated."
  - target: 01-human/03-molecular/rage
    relation: connects-to
    note: "Free-heme inflammation: the chronic intravascular haemolysis of sickle-cell disease releases free haem that, as a DAMP signalling through RAGE, drives the sterile vascular inflammation amplifying endothelial activation and vaso-occlusion."
  - target: 01-human/03-molecular/xanthine-oxidase
    relation: connects-to
    note: "Oxidative stress: cycles of ischaemia and reperfusion during vaso-occlusion drive xanthine-oxidase-derived reactive oxygen species, the oxidative injury that damages the sickle endothelium and consumes the nitric oxide already depleted by haemolysis."
  - target: 01-human/03-molecular/complement-c5
    relation: connects-to
    note: "Complement amplification: heme and ischaemia activate the complement system in sickle-cell disease, and C5-driven inflammation contributes to vaso-occlusion and to the severe delayed haemolytic transfusion reactions seen in these patients."
  - target: 01-human/03-molecular/nfe2l2
    relation: connects-to
    note: "Heme oxidative stress: free heme from intravascular haemolysis imposes severe oxidative stress in sickle-cell disease, against which NRF2 is the antioxidant defence; NRF2 activation also induces protective fetal haemoglobin."
  - target: 01-human/03-molecular/nlrp3-inflammasome
    relation: connects-to
    note: "Sterile inflammation: heme and DAMPs from sickle-cell haemolysis activate the NLRP3 inflammasome and IL-1β, driving the sterile inflammation that fuels vaso-occlusive crises."
  - target: 01-human/03-molecular/ferroportin
    relation: connects-to
    note: "Transfusional iron overload: chronic transfusion and haemolysis cause iron overload in sickle-cell disease, with hepcidin-mediated degradation of ferroportin governing the macrophage iron handling behind it."
  - target: 01-human/03-molecular/myd88
    relation: connects-to
    note: "Heme-driven sterile inflammation: free heme released by intravascular haemolysis acts as a TLR4 agonist signalling through MyD88 to NF-κB (both already mapped), driving the sterile inflammation that promotes vaso-occlusion in sickle-cell disease."
  - target: 01-human/03-molecular/thrombin
    relation: connects-to
    note: "Hypercoagulable state: chronic activation of coagulation generates thrombin and a prothrombotic milieu (protein C already mapped) that contributes to the thrombotic complications and elevated stroke risk of sickle-cell disease."
  - target: 01-human/03-molecular/angiopoietin
    relation: connects-to
    note: "Endothelial dysfunction: disruption of the angiopoietin-Tie2 axis that maintains endothelial barrier integrity promotes the endothelial activation and vascular leak underlying the vaso-occlusive injury of sickle-cell disease."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "PI3K-AKT-eNOS signalling regulates endothelial nitric-oxide production (NO mapped), a vasoprotective axis impaired by the hemolysis and oxidative stress of sickle-cell disease."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "ERK-MAPK signalling in activated endothelium and leukocytes amplifies the adhesion and inflammatory responses driving vaso-occlusion in sickle-cell disease."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Galectin-3 amplifies the sterile inflammation of haemolysis and vaso-occlusion, contributing to the chronic vascular injury of sickle-cell disease."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "DNA within neutrophil extracellular traps and from haemolysis-stressed cells engages cGAS-STING, amplifying the sterile thromboinflammation of sickle-cell vaso-occlusion."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "IL-6-STAT3 signalling transduces the chronic inflammatory tone that accompanies the recurrent haemolysis and vaso-occlusion of sickle-cell disease."
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "TGF-β-SMAD signalling drives the organ fibrosis (renal, pulmonary) that follows the repeated ischaemic injury of sickle-cell disease."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "FOXO regulates the erythroid and endothelial oxidative-stress responses to the chronic hemolysis and ischemia-reperfusion of sickle-cell disease."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "IFN-STAT1 signaling shapes the chronic inflammatory and endothelial activation underlying the vaso-occlusion of sickle-cell disease."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "JAK1/2-STAT cytokine signaling (IL-6-STAT3 already mapped) amplifies the inflammatory endothelial activation driving the vaso-occlusive crises of sickle-cell disease."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "GSK-3β modulates the endothelial and platelet activation signaling relevant to the vaso-occlusion of sickle-cell disease."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "PI3K (PIK3CA)-AKT signaling (AKT already mapped) participates in the endothelial activation and adhesion that drive the vaso-occlusive crises of sickle-cell disease."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK metabolic signaling participates in the response to the hypoxic-ischemic tissue stress of sickle-cell disease."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Autophagy (including erythroid mitophagy) participates in the red-cell maturation and oxidative-stress responses of sickle cell disease."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC-family kinase signaling participates in the endothelial activation and platelet responses driving the vaso-occlusion of sickle cell disease."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-driven leukocyte recruitment contributes to the vaso-occlusive inflammation of sickle cell disease."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "DNMT3A-mediated DNA methylation participates in the epigenetic regulation of fetal-hemoglobin and erythroid gene programs relevant to sickle cell disease."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "CXCL12-CXCR4 signaling participates in the leukocyte and erythroid-cell adhesion and marrow interactions relevant to sickle cell disease."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Complement C3 activation participates in the hemolysis-associated inflammation and vaso-occlusion of sickle cell disease."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "IL-1β-driven inflammation participates in the vaso-occlusive and inflammatory crises of sickle cell disease."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "IL-33 alarmin signaling participates in the endothelial and immune activation of sickle cell disease."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "IL-17A signaling participates in the chronic inflammation of sickle cell disease."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Red-cell dehydration: sickling opens a calcium-permeable pathway (Psickle) whose calcium influx activates the Gardos potassium channel (potassium already mapped), driving the water loss that concentrates HbS and accelerates polymerisation."
  - target: 01-human/03-molecular/mu-opioid-receptor
    relation: connects-to
    note: "Pain crisis: recurrent vaso-occlusive pain is the dominant symptom of sickle cell disease and is managed with opioids acting on the mu-opioid receptor, creating a difficult balance between analgesia and dependence."
  - target: 01-human/03-molecular/mhc-class-ii
    relation: connects-to
    note: "Transfusion alloimmunisation: chronic red-cell transfusion in sickle cell disease provokes alloantibodies against minor blood-group antigens presented on MHC, a major complication that complicates future transfusion."
  - target: 03-medicine/03-food/vitamin-d
    relation: connects-to
    note: "Deficiency and bone disease: vitamin D deficiency is very common in sickle cell disease and worsens the bone pain and low bone density, so supplementation is a routine part of comprehensive care."
  - target: 03-medicine/03-food/omega-3-fatty-acids
    relation: connects-to
    note: "Membrane and inflammation: omega-3 fatty acids reduce the frequency of vaso-occlusive crises in trials, acting on red-cell membrane composition and the endothelial inflammation (already mapped) that drives sickle vaso-occlusion."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "Anti-inflammatory balance: the anti-inflammatory cytokine IL-10 counters the chronic elevation of TNF, IL-6 and IL-1 (already mapped) that sustains the inflammatory, adhesive vasculopathy of sickle cell disease."
  - target: 01-human/03-molecular/substance-p
    relation: connects-to
    note: "Neurogenic pain: substance P released from sensory nerves contributes to the central and peripheral sensitisation of the sickle vaso-occlusive pain crisis (mu-opioid receptor already mapped), part of the neurogenic component of the intractable pain."
  - target: 01-human/03-molecular/prostaglandins
    relation: connects-to
    note: "Inflammatory crisis pain: prostaglandins from the inflammation of vaso-occlusion (IL-6, TNF and IL-1 already mapped) drive the pain of the sickle crisis, and non-steroidal anti-inflammatory drugs are used alongside opioids in its management."
  - target: 01-human/03-molecular/bradykinin
    relation: connects-to
    note: "Kinin pain and permeability: bradykinin generated in the ischaemic, inflamed tissue of vaso-occlusion sensitises nociceptors and raises vascular permeability, contributing to the pain and swelling of the sickle cell crisis."
  - target: 01-human/03-molecular/erythropoietin
    relation: connects-to
    note: "Compensatory erythropoiesis: the chronic haemolytic anaemia (haemoglobin already mapped) of sickle cell disease drives a high erythropoietin and reticulocytosis, the marrow expansion straining the skeleton and iron demand."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "M2 macrophage milieu: IL-4 polarises macrophages toward an M2 phenotype (IL-10 already mapped) that clears the haemolysed red cells, part of the immune and haemolytic microenvironment of sickle cell disease."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Growth and metabolism: leptin and the altered energy balance reflect the growth delay and raised metabolic expenditure of sickle cell disease, driven by the chronic haemolysis and inflammation (IL-6 already mapped)."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "M2 haemolytic milieu: IL-13, with IL-4 (already mapped), supports the M2 macrophage (already mapped) phenotype that clears the haemolysed red cells, part of the immune and haemolytic microenvironment of sickle cell disease."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Adipokine and growth: adiponectin, with leptin (already mapped), reflects the altered energy balance and adipokine milieu of the growth delay and raised metabolic expenditure of sickle cell disease."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), links the adipose-inflammatory milieu to the chronic haemolytic-inflammatory (IL-6 already mapped) state of sickle cell disease."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "Vaso-occlusion: the sickled cells (haemoglobin already mapped) and the leukocytes adhere to the activated endothelium (VWF and endothelin already mapped), the vaso-occlusion that causes the pain crises and the organ damage."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "Adhesion neutrophils: the neutrophils adhere (P-selectin — the crizanlizumab target) and initiate the vaso-occlusion of sickle cell disease."
  - target: 01-human/07-system/stroke
    relation: connects-to
    note: "Sickle stroke: the vaso-occlusion and the cerebral vasculopathy cause the childhood stroke of sickle cell disease, prevented by the transfusion and the transcranial-Doppler screening."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Innate haemolytic interferon: the type-I interferon, downstream of the cGAS-STING (already mapped) sensing of the free haem and cell-free DNA of the haemolysis, contributes to the chronic inflammation of sickle cell disease."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Th1 inflammation: the IFN-γ of the T cells is the type-II interferon arm of the chronic sterile inflammation (IL-6 and TNF already mapped) of the vaso-occlusion of sickle cell disease."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the immune-inflammatory dimension of sickle cell disease."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune dysregulation of the chronic inflammation of sickle cell disease."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the chronic sterile inflammation of the vaso-occlusion of sickle cell disease."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the immune dysregulation of sickle cell disease."
  - target: 01-human/03-molecular/c5ar1
    relation: connects-to
    note: "C5a receptor: the C5aR1 signalling (with the complement C3 and C5 already mapped) drives the haemolysis-triggered complement activation that amplifies the endothelial and neutrophil (already mapped) activation of the vaso-occlusion of sickle cell disease."
  - target: 01-human/03-molecular/factor-h
    relation: connects-to
    note: "Complement dysregulation: factor H regulates the alternative complement pathway (complement C3, C5 and C5aR1 already mapped) whose control is impaired by the cell-free haem, contributing to the complement-driven inflammation of sickle cell disease."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "CD4 helper source: the CD4 T-helper cells are the source of the Th17 (IL-17 and IL-23 already mapped) cytokines of the chronic sterile inflammation of sickle cell disease."
  - target: 01-human/03-molecular/c1-esterase-inhibitor
    relation: connects-to
    note: "Complement/contact regulation: the C1-esterase inhibitor regulates the classical complement and the contact-coagulation systems co-activated by the cell-free haem in the thromboinflammation of sickle cell disease."
  - target: 01-human/03-molecular/osteopontin
    relation: connects-to
    note: "Vaso-occlusion matricellular: osteopontin, released by the activated platelets (already mapped) and myeloid cells, is a matricellular mediator amplifying the endothelial (already mapped) adhesion and vaso-occlusion of sickle cell disease."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Adaptive/alloimmune arm: the cytotoxic T cells (perforin pathway) are part of the chronic inflammation and the transfusion alloimmunisation of sickle cell disease."
  - target: 01-human/03-molecular/tslp
    relation: connects-to
    note: "Alarmin-vascular axis: TSLP, from activated endothelium (already mapped) and mast cells (already mapped) in sickle cell disease, primes dendritic cells (already mapped) and amplifies the Th2/eosinophil (already mapped) vascular inflammation of sickle cell disease."
  - target: 01-human/03-molecular/histamine
    relation: connects-to
    note: "Mast-cell pain axis: histamine, from the mast cells (already mapped) degranulated by sickle-erythrocyte (already mapped) contact, amplifies the vaso-occlusive pain, the pruritus, and the neurogenic inflammation of the pain crises of sickle cell disease."
  - target: 01-human/03-molecular/periostin
    relation: connects-to
    note: "Fibrotic remodelling: periostin, downstream of the IL-13 (already mapped) and TGF-β (already mapped) signalling in the sickle-cell organ injury, contributes to the pulmonary fibrosis and the renal (already mapped) remodelling of sickle cell disease."
  - target: 01-human/03-molecular/melatonin
    relation: connects-to
    note: "Circadian pain-immune axis: melatonin, with its antioxidant and vascular effects on the sickle-erythrocyte (already mapped) fragile endothelium (already mapped), modulates the nocturnal pain-crisis pattern and the oxidative stress of sickle cell disease."
  - target: 01-human/03-molecular/testosterone
    relation: connects-to
    note: "Sex-hormone haematopoietic: testosterone stimulates erythropoiesis (EPO already mapped) and modulates the bone-marrow (already mapped) production of red blood cells (already mapped); the sex-hormone erythropoietic axis is relevant to the severity of sickle cell disease."
  - target: 01-human/03-molecular/serotonin
    relation: connects-to
    note: "Platelet-serotonin vaso-occlusion: serotonin, released by platelets (already mapped) upon the sickle-erythrocyte-damaged endothelium (already mapped), amplifies the vasoconstriction and microvascular thrombosis of the vaso-occlusive crises of sickle cell disease."
  - target: 01-human/03-molecular/prolactin
    relation: connects-to
    note: "SCD prolactin: prolactin, via PRLR on macrophages (already mapped) and erythrocytes (already mapped), modulates haematopoiesis; hyperprolactinaemia amplifies the IL-6 (already mapped) and TNF-α (already mapped) vaso-occlusive cascade of sickle cell disease."
  - target: 01-human/03-molecular/oxytocin
    relation: connects-to
    note: "SCD oxytocin: oxytocin, via OXTR on endothelial cells (already mapped) and macrophages (already mapped), attenuates vaso-occlusive inflammation; oxytocin deficiency amplifies the IL-6 (already mapped) and NF-κB (already mapped) crisis cascade of sickle cell disease."
  - target: 01-human/03-molecular/vasopressin
    relation: connects-to
    note: "SCD vasopressin: vasopressin, via V2 receptors on erythrocytes (already mapped) and endothelial cells (already mapped), modulates red-cell hydration; vasopressin excess amplifies haemolysis and the nitric-oxide (already mapped) vascular cascade of sickle cell disease."
  - target: 01-human/02-atomic/selenium
    relation: connects-to
    note: "SCD selenium: selenium, as GPx in erythrocytes (already mapped) and macrophages (already mapped), limits the haemolysis-driven ROS burden; selenium deficiency amplifies the NLRP3 (already mapped) and NF-κB (already mapped) vaso-occlusive cascade of sickle cell disease."
  - target: 01-human/02-atomic/iodine
    relation: connects-to
    note: "SCD iodine: iodine-dependent thyroid hormones regulate erythropoiesis (erythropoietin already mapped) and erythrocyte (already mapped) deformability; iodine deficiency amplifies the IL-6 (already mapped) and NLRP3 (already mapped) haemolytic cascade of sickle cell disease."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "SCD sodium: sodium, via Na⁺/K⁺-ATPase on erythrocytes (already mapped) and endothelial cells (already mapped), regulates red-cell hydration; sodium dysregulation amplifies sickling and the nitric-oxide (already mapped) vascular cascade of sickle cell disease."
  - target: 01-human/02-atomic/copper
    relation: connects-to
    note: "SCD copper: copper, via ceruloplasmin and SOD in endothelial cells (already mapped) and macrophages (already mapped), scavenges ROS; copper deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and NLRP3 (already mapped) haemolytic inflammation in SCD."
  - target: 01-human/02-atomic/phosphorus
    relation: connects-to
    note: "SCD phosphorus: phosphorus, as ATP precursor in erythrocytes (already mapped) and macrophages (already mapped), sustains sickling resistance; phosphorus deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and NLRP3 (already mapped) haemolytic cascade of SCD."
  - target: 01-human/02-atomic/chloride
    relation: connects-to
    note: "SCD chloride: chloride, via KCC1 in erythrocytes (already mapped) and endothelial cells (already mapped), regulates red-cell volume; chloride dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) sickling and haemolytic cascade of SCD."
  - target: 01-human/02-atomic/sulfur
    relation: connects-to
    note: "SCD sulfur: hydrogen sulfide from endothelial cells (already mapped) and macrophages (already mapped) promotes vasodilation; sulfur deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and NLRP3 (already mapped) vaso-occlusive cascade of SCD."
  - target: 01-human/02-atomic/carbon
    relation: connects-to
    note: "SCD carbon: carbon, as metabolic backbone of erythrocytes (already mapped) and macrophages (already mapped), fuels haemoglobin (already mapped) synthesis; carbon dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) sickling cascade of SCD."
  - target: 01-human/02-atomic/nitrogen
    relation: connects-to
    note: "SCD nitrogen: nitric oxide from endothelial cells (already mapped) and macrophages (already mapped) promotes vasodilation; nitrogen dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and NLRP3 (already mapped) vaso-occlusive cascade of SCD."
  - target: 01-human/03-molecular/pd-1
    relation: connects-to
    note: "SCD PD-1: PD-1 checkpoint on macrophages (already mapped) and T-cytotoxic cells (already mapped) modulates immune surveillance of haemolytic erythrocytes; PD-1 dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) cascade of SCD."
  - target: 01-human/03-molecular/glp-1
    relation: connects-to
    note: "SCD GLP-1: GLP-1 receptor signalling in macrophages (already mapped) and endothelial cells (already mapped) modulates metabolic and inflammatory vaso-occlusive risk; GLP-1 deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) cascade of SCD."
  - target: 01-human/03-molecular/angiotensin-ii
    relation: connects-to
    note: "SCD angiotensin-II: angiotensin-II signalling in endothelial cells (already mapped) and macrophages (already mapped) promotes vascular inflammation; angiotensin-II excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade of SCD."
  - target: 01-human/03-molecular/wnt-beta-catenin
    relation: connects-to
    note: "SCD Wnt/β-catenin: Wnt/β-catenin signalling in erythrocytes (already mapped) and macrophages (already mapped) modulates erythropoiesis; Wnt dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) sickling cascade of SCD."
  - target: 01-human/03-molecular/rankl
    relation: connects-to
    note: "SCD rankl: RANKL from macrophages (already mapped) and endothelial cells (already mapped) promotes vaso-occlusive bone remodelling; rankl excess amplifies nf-kb (already mapped) and il-6 (already mapped) and vegf (already mapped) sickling cascade of SCD."
  - target: 01-human/03-molecular/il-2
    relation: connects-to
    note: "SCD il-2: IL-2 from T-cells (already mapped) and macrophages (already mapped) regulates immune surveillance of haemolytic erythrocytes; il-2 dysregulation amplifies nf-kb (already mapped) and il-6 (already mapped) and vegf (already mapped) sickling cascade of SCD."
  - target: 01-human/03-molecular/fibronectin
    relation: connects-to
    note: "SCD fibronectin: fibronectin in fibroblasts (already mapped) and macrophages (already mapped) scaffolds vaso-occlusive ECM; fibronectin excess amplifies nf-kb (already mapped) and il-6 (already mapped) and vegf (already mapped) sickling cascade of SCD."
  - target: 01-human/03-molecular/notch
    relation: connects-to
    note: "SCD notch: Notch signalling in macrophages (already mapped) and endothelial cells (already mapped) regulates vaso-occlusive cell fate in SCD; notch dysregulation amplifies nf-kb (already mapped) and il-6 (already mapped) and vegf (already mapped) sickling cascade of SCD."
  - target: 01-human/03-molecular/igf-1
    relation: connects-to
    note: "SCD igf-1: IGF-1 from macrophages (already mapped) and endothelial cells (already mapped) promotes vascular cell survival in SCD; igf-1 dysregulation amplifies nf-kb (already mapped) and il-6 (already mapped) and vegf (already mapped) sickling cascade of SCD."
  - target: 01-human/03-molecular/activin-a
    relation: connects-to
    note: "SCD activin-a: activin-A from macrophages (already mapped) and endothelial cells (already mapped) drives vascular fibrosis in SCD; activin-a excess amplifies nf-kb (already mapped) and il-6 (already mapped) and vegf (already mapped) sickling cascade of SCD."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "SCD tgf-beta: TGF-β from macrophages (already mapped) and endothelial cells (already mapped) drives vascular fibrosis in SCD; tgf-beta excess amplifies nf-kb (already mapped) and il-6 (already mapped) and vegf (already mapped) sickling cascade of SCD."
  - target: 01-human/03-molecular/cgrp
    relation: connects-to
    note: "SCD cgrp: CGRP from macrophages (already mapped) and endothelial cells (already mapped) modulates vaso-occlusive vascular tone in SCD; cgrp excess amplifies nf-kb (already mapped) and il-6 (already mapped) and vegf (already mapped) sickling cascade of SCD."
  - target: 01-human/03-molecular/calcitonin
    relation: connects-to
    note: "SCD calcitonin: calcitonin from macrophages (already mapped) and endothelial cells (already mapped) modulates calcium balance in SCD; calcitonin excess amplifies nf-kb (already mapped) and il-6 (already mapped) and vegf (already mapped) sickling cascade of SCD."
  - target: 01-human/03-molecular/substance-p
    relation: connects-to
    note: "SCD substance-p: substance P from macrophages (already mapped) and endothelial cells (already mapped) modulates vaso-occlusive neuroimmune tone; substance-p excess amplifies nf-kb (already mapped) and il-6 (already mapped) and vegf (already mapped) sickling cascade of SCD."
  - target: 01-human/03-molecular/insulin-receptor
    relation: connects-to
    note: "SCD insulin-receptor: insulin receptor on macrophages (already mapped) and endothelial cells (already mapped) drives SCD metabolic repair; insulin-receptor loss amplifies nf-kb (already mapped) and il-6 (already mapped) and vegf (already mapped) sickling cascade of SCD."
  - target: 01-human/03-molecular/aldosterone
    relation: connects-to
    note: "SCD aldosterone: aldosterone from macrophages (already mapped) and endothelial cells (already mapped) modulates SCD ion balance; aldosterone excess amplifies nf-kb (already mapped) and il-6 (already mapped) and vegf (already mapped) sickling cascade of SCD."
  - target: 01-human/03-molecular/androgen-receptor
    relation: connects-to
    note: "SCD androgen-receptor: androgen receptor on macrophages (already mapped) and endothelial cells (already mapped) modulates SCD hormonal tone; androgen excess amplifies nf-kb (already mapped) and il-6 (already mapped) and vegf (already mapped) sickling cascade of SCD."
  - target: 01-human/03-molecular/norepinephrine
    relation: connects-to
    note: "SCD norepinephrine: norepinephrine from macrophages (already mapped) and endothelial cells (already mapped) modulates vascular tone in sickle crises; norepinephrine excess amplifies nf-kb (already mapped) and il-6 (already mapped) and vegf (already mapped) cascade of SCD."
  - target: 01-human/03-molecular/adrenomedullin
    relation: connects-to
    note: "SCD adrenomedullin: adrenomedullin from macrophages (already mapped) and endothelial cells (already mapped) modulates vascular tone in sickle crises; adrenomedullin loss amplifies nf-kb (already mapped) and il-6 (already mapped) and vegf (already mapped) sickling cascade of SCD."
  - target: 01-human/03-molecular/bdnf
    relation: connects-to
    note: "SCD bdnf: BDNF from macrophages (already mapped) and endothelial cells (already mapped) modulates neuroinflammatory tone in SCD; bdnf loss amplifies nf-kb (already mapped) and il-6 (already mapped) and vegf (already mapped) sickling cascade of SCD."
  - target: 01-human/03-molecular/fgfr
    relation: connects-to
    note: "SCD fgfr: FGFR on macrophages (already mapped) and endothelial cells (already mapped) drives SCD vascular remodelling; fgfr dysregulation amplifies nf-kb (already mapped) and il-6 (already mapped) and vegf (already mapped) sickling cascade of SCD."
  - target: 01-human/03-molecular/epinephrine
    relation: connects-to
    note: "SCD epinephrine: epinephrine from macrophages (already mapped) and endothelial cells (already mapped) modulates SCD adrenergic tone; epinephrine excess amplifies nf-kb (already mapped) and il-6 (already mapped) and vegf (already mapped) sickling cascade of SCD."
---

# Sickle Cell Disease

## Overview

**Sickle cell disease (SCD)** is the most common serious monogenic haemoglobinopathy worldwide, affecting ~100,000 people in the United States and 5–8 million globally. It is caused by a point mutation in the **β-globin gene (*HBB*, chromosome 11p15.4)**: a Glu→Val substitution at position 6 (E6V; GAG→GTG codon) — creating **haemoglobin S (HbS)**. The disease is inherited as an autosomal recessive disorder; disease manifestations require at least one HbS allele plus a second defective β-globin allele [^steinberg-1999-scd-management].

**Pathophysiological mechanism:**
1. Deoxygenated HbS polymerizes into long rigid fibres within red blood cells (RBCs)
2. Polymer formation distorts RBCs into the characteristic sickle shape
3. Sickled RBCs are rigid, adherent, and prone to haemolysis and vascular occlusion
4. Result: chronic haemolytic anaemia + acute vaso-occlusive crises + progressive end-organ damage

**Genotypes causing SCD:**

| Genotype | HbS% | HbA% | HbF% | Severity |
|:---------|:-----|:-----|:-----|:---------|
| HbSS (classic SCA) | 85-95% | 0% | 2-20% | Most severe |
| HbSC | ~50% HbS, ~50% HbC | 0% | 1-5% | Moderate; retinal/AVN complications |
| HbSβ⁰-thalassemia | 80-90% | 0% | 5-15% | Severe (similar to HbSS) |
| HbSβ⁺-thalassemia | 60-75% | 10-30% | 5-15% | Mild-moderate |
| HbSS + hereditary persistence of HbF | ~70% HbS | 0% | >25% | Milder course |
| HbS trait (carrier) | 35-40% | 55-60% | 1-2% | No haemolysis; exertional rhabdomyolysis risk |

**Epidemiology:**
- Highest prevalence: Sub-Saharan Africa (Nigeria, DRC, Ghana), Middle East, Mediterranean, India
- US: ~100,000 patients; predominantly African-American ancestry; prevalence 1:365 births
- Malaria protection: HbAS trait confers ~60% protection against severe *P. falciparum* malaria (balanced polymorphism explaining high allele frequency)

## Structure

### Molecular basis of HbS polymerization

**HbS structure:** Normal adult haemoglobin (HbA) is α2β2 tetramer; HbS is α2βS2 where β-globin Glu6→Val replaces a charged residue with a hydrophobic one on the outer surface of the β-globin chain.

**Polymerization mechanism:**
- In oxygenated HbS: T→R quaternary shift; Val6 is partially buried → minimal polymerization
- In deoxygenated HbS (T state): Val6 fully exposed → inserts into a hydrophobic "acceptor pocket" on an adjacent HbS molecule (Ala70, Phe85, Leu88 of β-globin) → nucleation of double-stranded protofibrils → lateral aggregation → long 14-stranded polymer fibres (~12.7 nm diameter)
- **Critical concentration (Cs):** HbS polymerization is sigmoidal with a delay period (nucleation phase); delay time is exquisitely sensitive to HbS concentration (log-linear relationship): ~30× faster at MCHC 37 g/dL vs. 35 g/dL
- **HbF inhibition:** γ-globin chains (HbF: α2γ2) cannot participate in the polymer acceptor pocket → HbF dilutes HbS concentration within the cell → dramatically prolongs delay time → prevents sickling

**Sickling cascade in vivo:**
1. In capillaries (pO2 ~40 mmHg), HbS deoxygenation exceeds Cs → polymer nucleation → sickling
2. Sickled cells: rigid, low deformability → mechanical haemolysis in spleen/marrow; adhesion to endothelium (via VLA-4/VCAM-1, P-selectin/PSGL-1)
3. Repeated sickling-unsickling → membrane oxidative damage → irreversibly sickled cells (ISCs): permanently deformed even when reoxygenated; rapidly haemolysed (RBC lifespan ~15-20 days vs. 120 days normally)
4. ISCs contribute to vaso-occlusion, dense cell formation, and free haemoglobin release

### Vaso-occlusion: multi-cellular mechanism

SCD vaso-occlusion is not just from sickled RBCs mechanically blocking vessels — it involves a complex multi-cellular cascade:
- **Activated endothelium:** Thrombin, inflammatory cytokines (TNF-α, IL-1β) → endothelial P-selectin, VCAM-1, tissue factor upregulation
- **Neutrophil-platelet-RBC aggregates:** HbS RBCs → oxidative stress → endothelial NADPH oxidase → ROS → NF-κB → inflammatory adhesion molecules; neutrophils bind endothelium → trap flowing sickle RBCs
- **Nitric oxide (NO) depletion:** Free haemoglobin from haemolysis → reacts with NO at near-diffusion-limited rates → converts vasodilatory NO to nitrate → vasoconstriction, platelet activation, endothelial dysfunction
- **Coagulation activation:** Phosphatidylserine exposure on sickle RBC membranes → procoagulant surface → thrombin generation → fibrin deposition in microvessels

## Function

### Acute complications

**Vaso-occlusive (painful) crisis (VOC):**
- Most common SCD complication; accounts for >90% of acute care visits
- Mechanism: microvascular obstruction → tissue ischaemia → acute pain (bone marrow infarction is primary source: ribs, vertebrae, femur, humerus)
- Precipitants: cold, dehydration, infection, stress, altitude
- Treatment: Aggressive IV hydration, IV opioids (morphine, hydromorphone, patient-controlled analgesia), NSAIDs for adjunctive analgesia, supplemental oxygen if hypoxic, incentive spirometry to prevent ACS

**Acute Chest Syndrome (ACS) [^vichinsky-2000-acs-scd]:**
- Definition: New pulmonary infiltrate on CXR + respiratory symptoms (fever, cough, hypoxia, chest pain) in a patient with SCD
- Mechanisms: Fat embolism from infarcted bone marrow (most common in adults), pulmonary vaso-occlusion, infection (*Chlamydophila*, *Mycoplasma*, viral — most common in children)
- Most dangerous acute complication; leading cause of SCD mortality
- Treatment: Broad-spectrum antibiotics (macrolide + cephalosporin), bronchodilators, incentive spirometry, **simple transfusion** (target Hb ~10 g/dL) or **exchange transfusion** for severe ACS; mechanical ventilation for respiratory failure
- Prevention: Hydroxyurea (reduces ACS by 50%); incentive spirometry during painful crises

**Stroke:**
- Ischaemic stroke: Most common <10 years (cerebral vasculopathy from repetitive sickling → large vessel narrowing/occlusion → moyamoya pattern); haemorrhagic stroke more common in adults
- **STOP trial:** Transcranial Doppler (TCD) velocity >200 cm/s → chronic transfusion (monthly exchange/simple transfusion; target HbS <30%) → 92% relative risk reduction in primary stroke
- **STOP II:** Stopping transfusion → 50% stroke recurrence within 30 months → indefinite chronic transfusion or HCT (haematopoietic cell transplant) required
- Hydroxyurea alone insufficient for high-TCD-velocity primary prevention; chronic transfusion is standard

**Splenic sequestration:**
- Acute: Sickle RBCs trapped in spleen → sudden massive splenomegaly + anaemia (Hb drop >2 g/dL from baseline) → circulatory shock; treat: blood transfusion; splenectomy for recurrent episodes
- Chronic: Repeated microinfarction → functional asplenia by age 4-5 in HbSS → loss of IgM-mediated opsonisation → susceptibility to encapsulated bacteria (*Streptococcus pneumoniae*, *Haemophilus influenzae*, *Neisseria meningitidis*) → overwhelming post-splenectomy infection (OPSI)
- Prevention: Pneumococcal vaccines (PCV13 + PPSV23), meningococcal vaccines, penicillin prophylaxis until age 5 (or indefinitely in high-risk patients)

**Aplastic crisis:**
- Parvovirus B19 infects erythroid progenitors → transient reticulocytopenia → rapid anaemia in patients with baseline high RBC turnover; self-limited (1-2 weeks); transfuse if symptomatic

**Priapism:**
- Uncontrolled, ischaemic erection > 4 hours; NO depletion → failure of penile smooth muscle relaxation; treat: hydration + analgesics; aspiration + phenylephrine injection for >4h; exchange transfusion; prevention: hydroxyurea, PDE5 inhibitors (sildenafil, tadalafil)

### Chronic complications

**Pulmonary arterial hypertension (PAH):**
- Mechanism: Chronic haemolysis → free haemoglobin → NO scavenging → reduced prostacyclin → vasoconstriction + endothelial proliferation → PAH
- Prevalence: ~6-10% HbSS patients have echocardiographic PAH (TRV >2.5 m/s); RHC-confirmed PAH ~10% of elevated TRV cases
- Mortality: PAH is a major contributor to premature death; TRV >2.5 m/s → HR 10.6 for death in 2 years
- Treatment: Hydroxyurea; chronic transfusion; sildenafil (PDE5 inhibitor; improves exercise capacity in SCD-PAH); endothelin receptor antagonists; HSCT curative

**Avascular necrosis (AVN):**
- Bilateral femoral and humeral head AVN from vascular occlusion of nutrient arteries
- Prevalence: ~50% HbSS by age 35
- Management: Conservative (PT, analgesia, crutches); core decompression; total hip/shoulder arthroplasty

**Sickle nephropathy (CKD):**
- Renal medullary microenvironment (high osmolarity, low pH, low pO2) → sickling in vasa recta → renal medullary ischaemia → hyposthenuria, haematuria, renal papillary necrosis
- Progressive glomerulopathy (hyperfiltration, podocyte injury) → proteinuria → nephrotic syndrome → CKD (ESRD in ~30% by age 40)
- Management: ACE inhibitors for proteinuria; hydroxyurea; avoid nephrotoxic agents; dialysis/transplant for ESRD

**Leg ulcers:**
- Chronic medial malleolar ulcers from haemolysis (low NO) + vascular occlusion
- Painful, slow-healing; treat with wound care, pain control, hydroxyurea; exchange transfusion for refractory ulcers

## Pathology

### Diagnosis

**Newborn screening (gold standard):** Haemoglobin electrophoresis (isoelectric focusing or HPLC) in first week of life; all US states mandate SCD screening; early detection allows penicillin prophylaxis initiation by age 3 months.

**Laboratory findings:**
- Anaemia: Hb 6-9 g/dL (HbSS); 10-12 g/dL (HbSC)
- Reticulocytosis: 5-25% (compensatory; absent in aplastic crisis)
- Blood smear: Sickle cells (drepanocytes), target cells, polychromasia, Howell-Jolly bodies (functional asplenia)
- LDH elevated (haemolysis marker); unconjugated bilirubin elevated
- Haemoglobin electrophoresis: Confirms HbS genotype

### Treatment

**Disease-modifying therapies:**

**Hydroxyurea (hydroxycarbamide) [^niaid-2014-scd-guidelines]:**
- Mechanism: ↑ HbF synthesis (via ↑ γ-globin gene expression, S-nitrosylation of sGC → cGMP → Hb switching); NO-donor activity → vasodilation; ↓ neutrophil/platelet counts → reduced vaso-occlusion
- Dosing: Start 15 mg/kg/day PO → titrate to maximum tolerated dose (MTD; typically 20-35 mg/kg/day); monitor CBC (target ANC >2,000/μL, platelets >80,000/μL)
- Efficacy: MSH trial — hydroxyurea reduced painful crisis rate by 44%, ACS by 50%, transfusions by 50%, hospitalizations by 40%; 17-year follow-up showed 40% mortality reduction
- Indication: All HbSS and HbSβ⁰ patients ≥9 months old (NHLBI 2014 guidelines); HbSC/HbSβ⁺ with severe complications

**Voxelotor (Oxbryta; FDA 2019):**
- Mechanism: Covalently binds HbS in the oxygenated state → shifts oxygen affinity → prevents T-state deoxygenation → inhibits HbS polymerization
- Efficacy (HOPE trial): 72% of patients achieved Hb increase ≥1 g/dL; reduced haemolysis markers; did not reduce VOC in pivotal trial
- Dosing: 1,500 mg PO once daily; withdrawn from US market in 2024 due to HOPE-KIDS 2 interim analysis showing trend toward higher mortality — ongoing regulatory evaluation
- Note: Voxelotor's status should be verified with current regulatory guidance

**Crizanlizumab (Adakveo; FDA 2019):**
- Mechanism: Monoclonal antibody targeting P-selectin on activated platelets and endothelium → blocks P-selectin/PSGL-1 interactions → prevents neutrophil-platelet-RBC aggregate formation → reduces vaso-occlusion
- Efficacy (SUSTAIN trial): 45% reduction in annual pain crisis rate vs. placebo; beneficial regardless of hydroxyurea use
- Dosing: 5 mg/kg IV every 4 weeks; can be combined with hydroxyurea
- Note: FDA reviewing postmarket data

**Chronic transfusion therapy:**
- **Simple transfusion:** Raises Hb, dilutes HbS%; used for ACS, priapism, pre-surgical preparation (target HbS <30% for major surgery), acute stroke treatment
- **Exchange transfusion (erythrocytapheresis):** Removes HbS RBCs while adding HbA RBCs; targets HbS <30%; avoids hyperviscosity; gold standard for acute stroke, severe ACS, peri-operative preparation
- **Chronic monthly transfusion:** Primary and secondary stroke prevention (target HbS <30%); iron overload is the main complication → iron chelation (deferasirox, deferoxamine)

**Haematopoietic cell transplantation (HCT):**
- Only currently available cure for SCD
- **Matched sibling donor HCT:** ~90% event-free survival in children without end-organ damage; ideal for high-risk children (prior stroke, frequent VOC despite hydroxyurea, multiple ACS episodes)
- **Haploidentical/matched unrelated donor:** Higher graft-versus-host disease risk; increasingly feasible with improved conditioning regimens (reduced-intensity conditioning for adults)
- **Gene therapy/gene editing (emerging):**
  - **Betibeglogene autotemcel (Zynteglo; FDA 2023):** Lentiviral vector adding anti-sickling βA-T87Q-globin gene to autologous HSCs; 94% of HbSS patients became transfusion-independent in the HGB-206 trial
  - **Exagamglogene autotemcel (Casgevy; FDA 2023):** First CRISPR-Cas9 gene editing therapy approved; reactivates HbF by disrupting BCL11A enhancer → BCL11A silenced → γ-globin re-expressed → HbF >20% → suppresses HbS polymerization; durable responses

## Connections

- `connects-to` → **[Hemoglobin](../../03-molecular/hemoglobin/README.md)** — HbS (α2βS2; β-globin E6V GAG→GTG) polymerizes when deoxygenated → long fibres → RBC sickling; HbF (α2γ2) inhibits HbS polymerization; HbSC (one HbS + HbC E6K allele) → milder but significant disease; HbSβ-thalassemia → intermediate severity.
- `connects-to` → **[Stroke](../stroke/README.md)** — SCD is the most common cause of stroke in children <10 years (cerebral vasculopathy; large vessel stenosis from repetitive sickling → moyamoya pattern); transcranial Doppler screening + chronic RBC transfusion reduces stroke risk by 92% (STOP trial).
- `connects-to` → **[CKD](../ckd/README.md)** — Renal medullary sickling (high osmolarity + low pO2 in vasa recta) → hyposthenuria; progressive CKD in ~30% HbSS by age 40; albuminuria → nephrotic syndrome; ACE inhibitors + hydroxyurea slow CKD progression; sickle cell nephropathy is a distinct histological entity.
- `connects-to` → **[Cardiovascular System](../cardiovascular-system/README.md)** — Chronic haemolysis → NO scavenging by free haemoglobin → pulmonary hypertension (PAH; tricuspid regurgitation velocity >2.5 m/s predicts mortality); cardiomegaly + high-output failure from chronic anaemia; sildenafil for SCD-PAH; echocardiographic screening at age 10.
- `connects-to` → **[Transferrin](../../03-molecular/transferrin/README.md)** — Chronic transfusion in SCD (stroke prevention, recurrent ACS; target HbS <30%) causes transfusional iron overload; serum ferritin >1,000 ng/mL → deferasirox chelation required; cardiac MRI T2* monitors iron deposition; TSAT 100% → NTBI → cardiomyopathy risk.
- `connects-to` → **[Thalassemia](../thalassemia/README.md)** — HbSβ-thalassemia (HbS + β-thal allele) is a common SCD genotype; β⁰ allele severity = HbSS; β⁺ = milder; shared gene therapy targets: Casgevy (CRISPR BCL11A derepression of γ-globin/HbF) is FDA-approved for both β-thal major and sickle cell disease.
- `connects-to` → **[G6PD](../../03-molecular/g6pd/README.md)** — G6PD A− deficiency (10-20% sub-Saharan Africans) co-occurs with HbSS in ~5-10% of SCD patients; G6PD deficiency + SCD → additive oxidant haemolysis risk; avoid dapsone, rasburicase, and nitrofurantoin in G6PD-deficient SCD; G6PD screening recommended.
- `connects-to` → **[Malaria](../malaria/README.md)** — HbAS (sickle trait) confers ~60% protection against severe malaria (balanced polymorphism); HbSS patients in endemic regions face compounded risk: fever + dehydration → sickling crises; antimalarial prophylaxis planning is essential for HbSS in endemic areas.
- `connects-to` → **[Protein C](../../03-molecular/protein-c/README.md)** — Acquired protein C deficiency is common in SCD: vaso-occlusive crisis → local thrombin burst → APC consumption; protein C levels inversely correlate with VOC frequency; SCD patients have reduced EPCR expression on ECs → impaired APC generation during hemolytic crises.
- `connects-to` → **[Erythrocyte](../../04-cellular/erythrocyte/README.md)** — Sickle cell disease is fundamentally a red-cell disease: HbS polymerizes when deoxygenated, distorting erythrocytes into rigid sickle shapes that hemolyze (anemia) and jam microvessels (vaso-occlusion); dehydration and adhesion molecules make the cells sticky and short-lived.
- `connects-to` → **[Spleen](../../06-organ/spleen/README.md)** — The spleen is an early casualty of sickle cell disease: repeated sickling infarcts it, causing splenic sequestration crises in children then autosplenectomy in adults; the resulting functional asplenia raises infection risk, mandating vaccines and penicillin prophylaxis.
- `connects-to` → **[Venous Thromboembolism](../venous-thromboembolism/README.md)** — Sickle cell disease is a hypercoagulable state: chronic hemolysis exposes phosphatidylserine and frees hemoglobin, activating platelets and coagulation while consuming protein C/S; VTE and pulmonary embolism are markedly increased atop the in-situ thrombosis of vaso-occlusion.
- `connects-to` → **[Pulmonary Arterial Hypertension](../pulmonary-arterial-hypertension/README.md)** — Pulmonary hypertension is a deadly complication of sickle cell disease: chronic hemolysis scavenges nitric oxide and releases free hemoglobin and arginase, raising pulmonary vascular tone—an elevated tricuspid regurgitant jet marks much higher mortality.
- `connects-to` → **[Neuropathic Pain](../neuropathic-pain/README.md)** — Pain in sickle cell disease is not only ischemic but increasingly neuropathic: repeated vaso-occlusive crises sensitize central and peripheral pain pathways, so chronic SCD pain takes on a neuropathic, opioid-resistant quality—calling for anticonvulsant adjuncts.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Splenic macrophages drive the extravascular hemolysis of sickle cell disease: they recognize and destroy rigid, sickled red cells, and recurrent splenic sequestration and infarction eventually leave patients functionally asplenic—hence lifelong sepsis risk.
- `connects-to` → **[Nitric Oxide](../../03-molecular/nitric-oxide/README.md)** — Nitric oxide depletion drives sickle-cell vasculopathy: free hemoglobin from hemolysis scavenges NO, so vessels lose vasodilation and platelets activate—linking chronic hemolysis to pulmonary hypertension, stroke and leg ulcers beyond the acute vaso-occlusive crises.
- `connects-to` → **[Oxygen](../../02-atomic/oxygen/README.md)** — Oxygen tension triggers the sickling itself: deoxygenated HbS polymerizes and deforms red cells, so hypoxia, dehydration and acidosis precipitate vaso-occlusive crises—which is why low oxygen at altitude or in infection can set off a painful sickle crisis.
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — The kidney is a major target of sickle-cell disease: the hypoxic, acidic renal medulla promotes sickling that damages the concentrating mechanism and glomeruli, causing impaired urine concentration, hematuria and progressive sickle nephropathy toward chronic kidney disease.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — Sickle cell disease is a disease of the endothelium as much as the red cell: sickled cells and free hemoglobin scavenge nitric oxide and inflame the vessel lining, so endothelial activation and adhesion trigger the painful vaso-occlusive crises.
- `connects-to` → **[Bone Marrow](../../05-tissue/bone-marrow/README.md)** — Sickle cell disease drives the bone marrow into overdrive: chronic hemolysis spurs erythroid hyperplasia that expands marrow and can cause aplastic crises when parvovirus halts it—and replacing the marrow by transplant or gene therapy can cure the disease.
- `connects-to` → **[Immune System](../immune-system/README.md)** — Sickle cell disease causes functional asplenia and immune vulnerability: repeated splenic infarction destroys the organ early in childhood, so patients are dangerously prone to encapsulated-bacterial sepsis—why prophylactic penicillin and vaccination are lifesaving.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — The lung is sickle cell disease's deadliest battleground: acute chest syndrome—sickling and infection in the pulmonary vessels—causes fever, chest pain, and hypoxia and is a leading cause of death, so it is treated urgently with transfusion and antibiotics.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — Sickle cell disease attacks the musculoskeletal system: vaso-occlusion infarcts bone, causing painful crises, dactylitis in infants, and avascular necrosis of the hip, so the skeleton bears much of the chronic damage and disability of the disease.
- `connects-to` → **[Eye](../../06-organ/eye/README.md)** — Sickle cell disease threatens sight: sickling in the tiny retinal vessels causes ischemia and proliferative sickle retinopathy with fragile new vessels that bleed or detach the retina—so regular eye screening protects vision in older patients.
- `connects-to` → **[Iron](../../02-atomic/iron/README.md)** — Chronic transfusions for sickle cell load the body with iron: repeated red-cell transfusions for stroke prevention and anemia deposit iron in the heart, liver and endocrine organs, so iron chelation is needed to prevent overload damage.
- `connects-to` → **[Neutrophil](../../04-cellular/neutrophil/README.md)** — Neutrophils help trigger sickle cell pain crises: activated neutrophils and adhesion molecules glue sickled cells to vessel walls, starting the vaso-occlusion behind painful crises—so anti-adhesion therapy (crizanlizumab) targets this step.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — Sickle cell disease burdens the liver: chronic hemolysis forms pigment gallstones, and sickling in hepatic vessels can cause sequestration and crises, so right-upper-quadrant pain in sickle cell needs evaluation of gallbladder and liver.
- `connects-to` → **[Platelet](../../04-cellular/platelet/README.md)** — Sickle cell disease makes blood prone to clot: hemolysis and inflamed vessels activate platelets that clump with sickled cells and white cells, helping plug small vessels and adding a thrombotic layer to the painful vaso-occlusive crises.
- `connects-to` → **[Brain](../../06-organ/brain/README.md)** — The brain is a prime casualty of sickle cell: blocked and narrowed vessels cause overt strokes and silent infarcts that erode cognition in children, which is why transcranial Doppler screening and transfusion are used to prevent them.
- `connects-to` → **[Potassium](../../02-atomic/potassium/README.md)** — Potassium loss is a hidden driver of sickling: the red cell's Gardos channel lets potassium and water leak out, dehydrating the cell and concentrating hemoglobin S so it polymerizes faster—making the channel a drug target in sickle cell.
- `connects-to` → **[Hydrogen](../../02-atomic/hydrogen/README.md)** — Acid speeds the sickling in sickle cell: a drop in blood pH (from exercise, infection, or dehydration) lowers hemoglobin's oxygen affinity and pushes HbS to polymerize, so acidosis helps tip a vaso-occlusive crisis.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — Sickle cell strains the heart two ways: lifelong anemia forces high-output work that enlarges it, and the iron from repeated transfusions deposits in the muscle, together driving heart failure over time.
- `connects-to` → **[Smooth Muscle Cell](../../04-cellular/smooth-muscle-cell/README.md)** — Sickle cell deranges vascular smooth muscle: free hemoglobin scavenges nitric oxide, the relaxant these cells depend on, so vessels constrict—causing the priapism and pulmonary hypertension that mark its vasculopathy.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Imaging guards against sickle cell's silent damage: MRI catches the brain's silent infarcts, and X-rays reveal the bone infarcts and acute chest syndrome that mark vaso-occlusive crises.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — Sickle cell ulcerates the skin: chronic leg ulcers around the ankles, from poor blood flow and sickling in small vessels, are a painful, slow-healing hallmark in adults.
- `connects-to` → **[Fibrosis](../../05-tissue/fibrosis/README.md)** — Repeated sickling scars the organs: chronic microvascular ischemia drives fibrosis in the spleen (autosplenectomy), kidney and liver, the cumulative end-organ damage of the disease.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy shows why the cell sickles: when oxygen drops, hemoglobin S polymerizes into long stiff fibers that warp the red cell into a rigid crescent, the molecular event that jams the microvasculature.
- `connects-to` → **[Zinc](../../02-atomic/zinc/README.md)** — Sickle cell disease runs short on zinc: chronic hemolysis and high turnover deplete it, and because zinc supports growth and immunity, supplementation can reduce infections and pain crises in deficient patients.
- `connects-to` → **[Large Intestine](../../06-organ/large-intestine/README.md)** — Sickling can choke the gut: vaso-occlusion in the mesenteric vessels causes the abdominal 'girdle syndrome' of pain and ileus, while chronic hemolysis breeds the pigment gallstones that trouble many patients.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — Sickling strikes the reproductive organs: priapism — a painful, prolonged erection from vaso-occlusion in the penis — is a urologic emergency, and the disease complicates fertility and raises the risks of pregnancy.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — Transfusions stir up antibodies: repeatedly transfused patients form alloantibodies against donor red-cell antigens, making future cross-matching hard — while the newer drug crizanlizumab is itself an anti-P-selectin antibody that blocks vaso-occlusion.
- `connects-to` → **[Osteoblast](../../04-cellular/osteoblast/README.md)** — Sickling starves the bones: vaso-occlusion infarcts the marrow and kills the femoral head in avascular necrosis, while in children it swells the hands and feet as the dactylitis that is often the first sign.
- `connects-to` → **[Streptococcus pneumoniae](../../../02-pathogen/02-bacteria/streptococcus-pneumoniae/README.md)** — Lose the spleen, lose the defense: repeated infarction autosplenectomizes sickle-cell patients, leaving them prey to encapsulated bacteria like Streptococcus pneumoniae and overwhelming sepsis — countered by penicillin prophylaxis and vaccination.
- `connects-to` → **[Osteoclast](../../04-cellular/osteoclast/README.md)** — The infarcted skeleton remodels and weakens: chronic marrow expansion and bone infarction rev up osteoclast resorption into low bone density, and the dead, infarcted bone is uniquely prone to Salmonella osteomyelitis.
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — Magnesium guards the red cell's water: sickle erythrocytes leak magnesium and potassium and dehydrate, which concentrates hemoglobin S and speeds sickling, so magnesium repletion is studied to keep the cells hydrated.
- `connects-to` → **[Interleukin-6](../../03-molecular/il-6/README.md)** — Sickle disease smolders with inflammation: even between crises IL-6 and other cytokines run high, priming the endothelium and white cells that drive the vaso-occlusion at the heart of the disease.
- `connects-to` → **[Aplastic Anemia](../aplastic-anemia/README.md)** — A virus can stall the marrow's overdrive: parvovirus B19 shuts down red-cell production for days, and in sickle disease — where survival depends on furious red-cell turnover — this triggers a sudden, dangerous aplastic crisis.
- `connects-to` → **[Small Intestine](../../06-organ/small-intestine/README.md)** — Vaso-occlusion can strike the gut: sickled cells clog the mesenteric vessels in a crisis, starving the bowel into the ischemic abdominal pain of the 'girdle syndrome,' a visceral face of the disease.
- `connects-to` → **[Adenosine](../../03-molecular/adenosine/README.md)** — Adenosine has a double role in sickle disease: signaling through the A2B receptor it raises red-cell 2,3-BPG and promotes sickling, while via A2A it dampens the inflammatory pain of crises — a pathway probed for new therapies.
- `connects-to` → **[Mast Cell](../../04-cellular/mast-cell/README.md)** — Mast cells stoke the pain of sickle crises: activated in the vaso-occlusive milieu they release substance P and inflammatory mediators that sensitize nerves and worsen the neurogenic component of sickle pain.
- `connects-to` → **[Sepsis](../sepsis/README.md)** — Functional asplenia makes sepsis the great killer in sickle disease: repeated infarction destroys the spleen, so encapsulated bacteria can cause overwhelming sepsis — the reason for penicillin prophylaxis and pneumococcal vaccination from infancy.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — Vaso-occlusion runs on NF-κB-driven stickiness: hemolysis and hypoxia activate NF-κB in endothelium and leukocytes, switching on the adhesion molecules that glue sickled cells to vessel walls and ignite the painful crisis.
- `connects-to` → **[Salmonella typhi](../../../02-pathogen/02-bacteria/salmonella-typhi/README.md)** — A classic pairing of infarcted bone and an unusual bug: in sickle cell disease, Salmonella is the characteristic cause of osteomyelitis, seeding bone made dead by vaso-occlusion in a patient whose spleen no longer clears it.
- `connects-to` → **[Hepatocellular Carcinoma](../hcc/README.md)** — Transfusions and liver injury raise the cancer stakes: repeated transfusion causes iron overload while intrahepatic sickling damages the liver, and the resulting fibrosis can, over time, give rise to hepatocellular carcinoma.
- `connects-to` → **[Osteoporosis](../osteoporosis/README.md)** — The marrow and infarcts weaken the skeleton: chronic marrow hyperplasia, bone infarction and delayed growth in sickle cell disease leave low bone density and a high rate of osteoporosis and avascular necrosis.
- `connects-to` → **[Heart Failure](../heart-failure/README.md)** — Anemia and iron strain the heart: the chronic high-output state of sickle anemia, transfusional iron loading of the myocardium and pulmonary hypertension together drive a cardiomyopathy and heart failure.
- `connects-to` → **[Opioid Use Disorder](../opioid-use-disorder/README.md)** — A lifetime of pain crises courts dependence: the recurrent severe vaso-occlusive pain of sickle cell disease requires repeated and long-term opioids, carrying a real risk of tolerance and opioid use disorder.
- `connects-to` → **[Wound Healing](../wound-healing/README.md)** — Vaso-occlusion ulcerates the legs: chronic ischemia and impaired perfusion in sickle cell disease produce the painful, recurrent leg ulcers over the ankles that are notoriously slow to heal.
- `connects-to` → **[Neisseria meningitidis](../../../02-pathogen/02-bacteria/neisseria-meningitidis/README.md)** — Autosplenectomy strips defense against encapsulated bacteria: repeated splenic infarction leaves sickle cell patients functionally asplenic and vulnerable to meningococcus, alongside pneumococcus and Salmonella.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — Lifelong pain and disease weigh on mood: the recurrent crises, hospitalizations, stigma and chronic pain of sickle cell disease carry a substantial burden of depression and reduced quality of life.
- `connects-to` → **[Respiratory System](../respiratory-system/README.md)** — Acute chest syndrome is its great killer: vaso-occlusion in the pulmonary vasculature causes acute chest syndrome with hypoxia and infiltrates, the leading cause of death in sickle cell disease.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — Chronic haemolysis stones the gallbladder: the constant red-cell breakdown of sickle cell disease forms pigment gallstones, and splenic and hepatic sequestration crises swell and threaten these organs.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — It carves chronic ulcers into the skin: sickle cell disease causes intractable leg ulcers over the ankles from microvascular occlusion and poor healing, a painful, recurring cutaneous complication.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — It silently scars the brain: beyond overt stroke, sickle cell disease causes silent cerebral infarcts, cognitive impairment and a moyamoya-like cerebral vasculopathy, especially in children.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — It stunts growth and hormones: chronic anaemia delays growth and puberty, and transfusional iron overload damages the pituitary and gonads, causing hypogonadism and hypopituitarism.
- `connects-to` → **[Lymphatic System](../lymphatic-system/README.md)** — It destroys its own spleen: repeated splenic infarction causes autosplenectomy and functional asplenia, leaving lifelong vulnerability to encapsulated bacteria and the need for vaccination.
- `connects-to` → **[Renal System](../renal-system/README.md)** — Sickle cell nephropathy is near-universal: sickling in the renal medulla causes hyposthenuria, papillary necrosis and haematuria, progressing through proteinuric FSGS to chronic kidney disease.
- `connects-to` → **[ACE inhibitors](../../../03-medicine/01-modern/04-cardio/ace-inhibitors/README.md)** — They protect the sickle kidney: ACE inhibitors reduce the proteinuria of sickle cell nephropathy, slowing the decline towards kidney failure.
- `connects-to` → **[Dietary Zinc](../../../03-medicine/03-food/zinc-dietary/README.md)** — Chronic haemolysis drains zinc: urinary zinc loss in sickle cell disease contributes to growth retardation, delayed puberty and impaired immunity, and supplementation can help.
- `connects-to` → **[Amoxicillin](../../../03-medicine/01-modern/06-antimicrobial/amoxicillin/README.md)** — Daily antibiotic shields the child: because sickle cell disease destroys the spleen early, prophylactic penicillin or amoxicillin is given through childhood to prevent overwhelming pneumococcal sepsis.
- `connects-to` → **[Staphylococcus aureus](../../../02-pathogen/02-bacteria/staphylococcus-aureus/README.md)** — It seeds infarcted bone: alongside Salmonella, Staphylococcus aureus is a leading cause of the osteomyelitis that complicates the bone infarcts of sickle cell disease.
- `connects-to` → **[Iron-Deficiency Anemia](../iron-deficiency-anemia/README.md)** — Opposite iron problems: unlike iron-deficiency anaemia, sickle cell is a haemolytic anaemia where repeated transfusion brings iron overload, so the two need opposite iron management.
- `connects-to` → **[Cancer Chemotherapy](../../../03-medicine/01-modern/13-cancer/cancer-chemotherapy/README.md)** — Hydroxyurea is the cornerstone: the chemotherapy agent hydroxyurea raises fetal haemoglobin in sickle cell disease, reducing the painful crises, acute chest syndrome and need for transfusion — its first disease-modifying drug.
- `connects-to` → **[Targeted Therapy](../../../03-medicine/01-modern/13-cancer/targeted-therapy/README.md)** — New molecular and gene therapies: crizanlizumab against P-selectin and voxelotor stabilising oxygenated haemoglobin reduce crises, while CRISPR (exa-cel) and lentiviral gene therapies now offer a one-time cure by reactivating fetal haemoglobin.
- `connects-to` → **[Cortical Bone](../../05-tissue/cortical-bone/README.md)** — Vaso-occlusion infarcts bone: sickling blocks the bone microcirculation, causing dactylitis, painful bone infarcts, avascular necrosis of the femoral head and a predisposition to Salmonella osteomyelitis.
- `connects-to` → **[Alveolus](../../05-tissue/alveolus/README.md)** — Acute chest syndrome: vaso-occlusion and fat embolism in the pulmonary alveoli cause acute chest syndrome with hypoxaemia and infiltrates, the leading cause of death in sickle cell disease.
- `connects-to` → **[Glomerulus](../../05-tissue/glomerulus/README.md)** — Sickle nephropathy: sickling in the renal medulla and chronic hyperfiltration injure the glomerulus, causing proteinuria, papillary necrosis and progression to chronic kidney disease.
- `connects-to` → **[Placenta](../../06-organ/placenta/README.md)** — Sickling in pregnancy: vaso-occlusion and poor oxygen delivery damage the placenta, raising the risk of miscarriage, growth restriction and pre-eclampsia in sickle cell pregnancies.
- `connects-to` → **[Arterial Wall](../../05-tissue/arterial-wall/README.md)** — Vasculopathy and stroke: sickle cell disease damages the arterial wall, narrowing cerebral arteries into a moyamoya pattern that causes the strokes screened for with transcranial Doppler in children.
- `connects-to` → **[Myocardium](../../05-tissue/myocardium/README.md)** — Iron-overload cardiomyopathy: repeated transfusions for sickle cell disease deposit iron in the myocardium, causing cardiomyopathy and arrhythmia unless removed by chelation.
- `connects-to` → **[Germinal Center](../../05-tissue/germinal-center/README.md)** — Functional asplenia and immunity: autoinfarction of the spleen removes a key site of germinal-centre responses to encapsulated bacteria, mandating vaccination and penicillin prophylaxis in sickle cell disease.
- `connects-to` → **[RSV](../rsv/README.md)** — Acute chest syndrome trigger: RSV and other respiratory viruses precipitate acute chest syndrome—the vaso-occlusive lung crisis that is a leading cause of death in sickle cell disease.
- `connects-to` → **[GVHD](../gvhd/README.md)** — A curative transplant's risk: allogeneic stem-cell transplant can cure sickle cell disease but carries graft-versus-host disease, the key trade-off alongside newer gene therapies.
- `connects-to` → **[Cardiac Conduction System](../../05-tissue/cardiac-conduction-system/README.md)** — Iron and rhythm: chronic haemolysis and transfusional iron load the heart in sickle cell disease, scarring the myocardium and conduction system toward arrhythmia and sudden death.
- `connects-to` → **[Endothelin-1](../../03-molecular/endothelin-1/README.md)** — Vaso-occlusive vasoconstriction: free haemoglobin and endothelial injury raise endothelin-1 in sickle cell disease, whose vasoconstriction aggravates vaso-occlusion and pulmonary hypertension.
- `connects-to` → **[TNF-α](../../03-molecular/tnf-alpha/README.md)** — Inflammatory adhesion: TNF-α from the chronic inflammation of sickle cell disease upregulates endothelial adhesion molecules, promoting the sickle-cell and leukocyte adhesion that triggers vaso-occlusion.
- `connects-to` → **[HIF-1α](../../03-molecular/hif-1alpha/README.md)** — Hypoxic response: tissue hypoxia from vaso-occlusion stabilises HIF-1α, driving the erythropoietin surge and angiogenic and inflammatory responses of sickle cell disease.
- `connects-to` → **[TLR4](../../03-molecular/tlr4/README.md)** — Heme danger signal: free heme released by intravascular haemolysis acts as a TLR4 agonist, driving the sterile inflammation and endothelial activation that initiate vaso-occlusive crises.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — Neutrophil alarmin: S100A8/A9 from activated neutrophils amplifies the inflammation and adhesion of sickle cell disease, contributing to the leukocyte-driven vaso-occlusion of painful crises.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — Ischaemic angiogenesis: chronic hypoxia drives VEGF-mediated neovascularisation, underlying the proliferative sickle retinopathy and aberrant vessel growth that threaten vision in the disease.
- `connects-to` → **[von Willebrand factor](../../03-molecular/von-willebrand-factor/README.md)** — Endothelial activation in sickle cell disease releases ultra-large von Willebrand factor multimers that, with relatively reduced ADAMTS13 activity, promote the platelet and sickle-cell adhesion that occludes the microvasculature.
- `connects-to` → **[PF4](../../03-molecular/pf4/README.md)** — Chronically activated platelets in sickle cell disease release platelet factor 4 and procoagulant mediators that contribute to the thrombo-inflammation and hypercoagulability driving vaso-occlusive crises and stroke risk.
- `connects-to` → **[Hepcidin](../../03-molecular/hepcidin/README.md)** — Repeated red-cell transfusions load the body with iron, and the resulting parenchymal iron deposition damages the heart, liver, and endocrine organs unless removed by chelation—a major long-term complication of transfusion-dependent disease.
- `connects-to` → **[RAGE](../../03-molecular/rage/README.md)** — The chronic intravascular hemolysis of sickle-cell disease releases free heme that, as a DAMP signaling through RAGE, drives the sterile vascular inflammation amplifying endothelial activation and vaso-occlusion.
- `connects-to` → **[Xanthine Oxidase](../../03-molecular/xanthine-oxidase/README.md)** — Cycles of ischemia and reperfusion during vaso-occlusion drive xanthine-oxidase-derived reactive oxygen species, the oxidative injury that damages the sickle endothelium and consumes the nitric oxide already depleted by hemolysis.
- `connects-to` → **[Complement C5](../../03-molecular/complement-c5/README.md)** — Heme and ischemia activate the complement system in sickle-cell disease, and C5-driven inflammation contributes to vaso-occlusion and to the severe delayed hemolytic transfusion reactions seen in these patients.
- `connects-to` → **[NRF2](../../03-molecular/nfe2l2/README.md)** — Free heme from intravascular hemolysis imposes severe oxidative stress in sickle-cell disease, against which NRF2 is the antioxidant defense; NRF2 activation also induces protective fetal hemoglobin.
- `connects-to` → **[NLRP3 Inflammasome](../../03-molecular/nlrp3-inflammasome/README.md)** — Heme and DAMPs from sickle-cell hemolysis activate the NLRP3 inflammasome and IL-1β, driving the sterile inflammation that fuels vaso-occlusive crises.
- `connects-to` → **[Ferroportin](../../03-molecular/ferroportin/README.md)** — Chronic transfusion and hemolysis cause iron overload in sickle-cell disease, with hepcidin-mediated degradation of ferroportin governing the macrophage iron handling behind it.
- `connects-to` → **[MYD88](../../03-molecular/myd88/README.md)** — Free heme released by intravascular hemolysis acts as a TLR4 agonist signaling through MyD88 to NF-κB (both already mapped), driving the sterile inflammation that promotes vaso-occlusion in sickle-cell disease.
- `connects-to` → **[Thrombin](../../03-molecular/thrombin/README.md)** — Chronic activation of coagulation generates thrombin and a prothrombotic milieu (protein C already mapped) that contributes to the thrombotic complications and elevated stroke risk of sickle-cell disease.
- `connects-to` → **[Angiopoietin](../../03-molecular/angiopoietin/README.md)** — Disruption of the angiopoietin-Tie2 axis that maintains endothelial barrier integrity promotes the endothelial activation and vascular leak underlying the vaso-occlusive injury of sickle-cell disease.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — PI3K-AKT-eNOS signaling regulates endothelial nitric-oxide production (NO mapped), a vasoprotective axis impaired by the hemolysis and oxidative stress of sickle-cell disease.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — ERK-MAPK signaling in activated endothelium and leukocytes amplifies the adhesion and inflammatory responses driving vaso-occlusion in sickle-cell disease.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Galectin-3 amplifies the sterile inflammation of hemolysis and vaso-occlusion, contributing to the chronic vascular injury of sickle-cell disease.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — DNA within neutrophil extracellular traps and from hemolysis-stressed cells engages cGAS-STING, amplifying the sterile thromboinflammation of sickle-cell vaso-occlusion.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — IL-6-STAT3 signaling transduces the chronic inflammatory tone that accompanies the recurrent hemolysis and vaso-occlusion of sickle-cell disease.
- `connects-to` → **[SMAD4](../../03-molecular/smad4/README.md)** — TGF-β-SMAD signaling drives the organ fibrosis (renal, pulmonary) that follows the repeated ischemic injury of sickle-cell disease.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — FOXO regulates the erythroid and endothelial oxidative-stress responses to the chronic hemolysis and ischemia-reperfusion of sickle-cell disease.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — IFN-STAT1 signaling shapes the chronic inflammatory and endothelial activation underlying the vaso-occlusion of sickle-cell disease.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — JAK1/2-STAT cytokine signaling (IL-6-STAT3 already mapped) amplifies the inflammatory endothelial activation driving the vaso-occlusive crises of sickle-cell disease.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β modulates the endothelial and platelet activation signaling relevant to the vaso-occlusion of sickle-cell disease.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — PI3K (PIK3CA)-AKT signaling (AKT already mapped) participates in the endothelial activation and adhesion that drive the vaso-occlusive crises of sickle-cell disease.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK metabolic signaling participates in the response to the hypoxic-ischemic tissue stress of sickle-cell disease.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — Autophagy (including erythroid mitophagy) participates in the red-cell maturation and oxidative-stress responses of sickle cell disease.
- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — SRC-family kinase signaling participates in the endothelial activation and platelet responses driving the vaso-occlusion of sickle cell disease.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-driven leukocyte recruitment contributes to the vaso-occlusive inflammation of sickle cell disease.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — DNMT3A-mediated DNA methylation participates in the epigenetic regulation of fetal-hemoglobin and erythroid gene programs relevant to sickle cell disease.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — CXCL12-CXCR4 signaling participates in the leukocyte and erythroid-cell adhesion and marrow interactions relevant to sickle cell disease.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Complement C3 activation participates in the hemolysis-associated inflammation and vaso-occlusion of sickle cell disease.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — IL-1β-driven inflammation participates in the vaso-occlusive and inflammatory crises of sickle cell disease.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — IL-33 alarmin signaling participates in the endothelial and immune activation of sickle cell disease.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — IL-17A signaling participates in the chronic inflammation of sickle cell disease.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Red-cell dehydration: sickling opens a calcium-permeable pathway (Psickle) whose calcium influx activates the Gardos potassium channel (potassium already mapped), driving the water loss that concentrates HbS and accelerates polymerisation.
- `connects-to` → **[Mu-opioid receptor](../../03-molecular/mu-opioid-receptor/README.md)** — Pain crisis: recurrent vaso-occlusive pain is the dominant symptom of sickle cell disease and is managed with opioids acting on the mu-opioid receptor, creating a difficult balance between analgesia and dependence.
- `connects-to` → **[MHC class II](../../03-molecular/mhc-class-ii/README.md)** — Transfusion alloimmunisation: chronic red-cell transfusion in sickle cell disease provokes alloantibodies against minor blood-group antigens presented on MHC, a major complication that complicates future transfusion.
- `connects-to` → **[Vitamin D](../../../03-medicine/03-food/vitamin-d/README.md)** — Deficiency and bone disease: vitamin D deficiency is very common in sickle cell disease and worsens the bone pain and low bone density, so supplementation is a routine part of comprehensive care.
- `connects-to` → **[Omega-3 Fatty Acids](../../../03-medicine/03-food/omega-3-fatty-acids/README.md)** — Membrane and inflammation: omega-3 fatty acids reduce the frequency of vaso-occlusive crises in trials, acting on red-cell membrane composition and the endothelial inflammation (already mapped) that drives sickle vaso-occlusion.
- `connects-to` → **[IL-10](../../03-molecular/il-10/README.md)** — Anti-inflammatory balance: the anti-inflammatory cytokine IL-10 counters the chronic elevation of TNF, IL-6 and IL-1 (already mapped) that sustains the inflammatory, adhesive vasculopathy of sickle cell disease.
- `connects-to` → **[Substance P](../../03-molecular/substance-p/README.md)** — Neurogenic pain: substance P released from sensory nerves contributes to the central and peripheral sensitisation of the sickle vaso-occlusive pain crisis (mu-opioid receptor already mapped), part of the neurogenic component of the intractable pain.
- `connects-to` → **[Prostaglandins](../../03-molecular/prostaglandins/README.md)** — Inflammatory crisis pain: prostaglandins from the inflammation of vaso-occlusion (IL-6, TNF and IL-1 already mapped) drive the pain of the sickle crisis, and non-steroidal anti-inflammatory drugs are used alongside opioids in its management.
- `connects-to` → **[Bradykinin](../../03-molecular/bradykinin/README.md)** — Kinin pain and permeability: bradykinin generated in the ischaemic, inflamed tissue of vaso-occlusion sensitises nociceptors and raises vascular permeability, contributing to the pain and swelling of the sickle cell crisis.
- `connects-to` → **[Erythropoietin](../../03-molecular/erythropoietin/README.md)** — Compensatory erythropoiesis: the chronic haemolytic anaemia (haemoglobin already mapped) of sickle cell disease drives a high erythropoietin and reticulocytosis, the marrow expansion straining the skeleton and iron demand.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — M2 macrophage milieu: IL-4 polarises macrophages toward an M2 phenotype (IL-10 already mapped) that clears the haemolysed red cells, part of the immune and haemolytic microenvironment of sickle cell disease.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Growth and metabolism: leptin and the altered energy balance reflect the growth delay and raised metabolic expenditure of sickle cell disease, driven by the chronic haemolysis and inflammation (IL-6 already mapped).
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — M2 haemolytic milieu: IL-13, with IL-4 (already mapped), supports the M2 macrophage (already mapped) phenotype that clears the haemolysed red cells, part of the immune and haemolytic microenvironment of sickle cell disease.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — Adipokine and growth: adiponectin, with leptin (already mapped), reflects the altered energy balance and adipokine milieu of the growth delay and raised metabolic expenditure of sickle cell disease.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Inflammatory adipokine: resistin, with leptin and adiponectin (already mapped), links the adipose-inflammatory milieu to the chronic haemolytic-inflammatory (IL-6 already mapped) state of sickle cell disease.
- `connects-to` → **[Endothelial cell](../../04-cellular/endothelial-cell/README.md)** — Vaso-occlusion: the sickled cells (haemoglobin already mapped) and the leukocytes adhere to the activated endothelium (VWF and endothelin already mapped), the vaso-occlusion that causes the pain crises and the organ damage.
- `connects-to` → **[Neutrophil](../../04-cellular/neutrophil/README.md)** — Adhesion neutrophils: the neutrophils adhere (P-selectin — the crizanlizumab target) and initiate the vaso-occlusion of sickle cell disease.
- `connects-to` → **[Stroke](../stroke/README.md)** — Sickle stroke: the vaso-occlusion and the cerebral vasculopathy cause the childhood stroke of sickle cell disease, prevented by the transfusion and the transcranial-Doppler screening.
- `connects-to` → **[Type I interferon](../../03-molecular/type-i-interferon/README.md)** — Innate haemolytic interferon: the type-I interferon, downstream of the cGAS-STING (already mapped) sensing of the free haem and cell-free DNA of the haemolysis, contributes to the chronic inflammation of sickle cell disease.
- `connects-to` → **[IFN-gamma](../../03-molecular/ifn-gamma/README.md)** — Th1 inflammation: the IFN-γ of the T cells is the type-II interferon arm of the chronic sterile inflammation (IL-6 and TNF already mapped) of the vaso-occlusion of sickle cell disease.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the immune-inflammatory dimension of sickle cell disease.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune dysregulation of the chronic inflammation of sickle cell disease.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the chronic sterile inflammation of the vaso-occlusion of sickle cell disease.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the immune dysregulation of sickle cell disease.
- `connects-to` → **[C5aR1](../../03-molecular/c5ar1/README.md)** — C5a receptor: the C5aR1 signalling (with the complement C3 and C5 already mapped) drives the haemolysis-triggered complement activation that amplifies the endothelial and neutrophil (already mapped) activation of the vaso-occlusion of sickle cell disease.
- `connects-to` → **[Factor H](../../03-molecular/factor-h/README.md)** — Complement dysregulation: factor H regulates the alternative complement pathway (complement C3, C5 and C5aR1 already mapped) whose control is impaired by the cell-free haem, contributing to the complement-driven inflammation of sickle cell disease.
- `connects-to` → **[T-helper cell](../../04-cellular/t-helper-cell/README.md)** — CD4 helper source: the CD4 T-helper cells are the source of the Th17 (IL-17 and IL-23 already mapped) cytokines of the chronic sterile inflammation of sickle cell disease.
- `connects-to` → **[C1-esterase inhibitor](../../03-molecular/c1-esterase-inhibitor/README.md)** — Complement/contact regulation: the C1-esterase inhibitor regulates the classical complement and the contact-coagulation systems co-activated by the cell-free haem in the thromboinflammation of sickle cell disease.
- `connects-to` → **[Osteopontin](../../03-molecular/osteopontin/README.md)** — Vaso-occlusion matricellular: osteopontin, released by the activated platelets (already mapped) and myeloid cells, is a matricellular mediator amplifying the endothelial (already mapped) adhesion and vaso-occlusion of sickle cell disease.
- `connects-to` → **[Cytotoxic T cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Adaptive/alloimmune arm: the cytotoxic T cells (perforin pathway) are part of the chronic inflammation and the transfusion alloimmunisation of sickle cell disease.
- `connects-to` → **[TSLP](../../03-molecular/tslp/README.md)** — Alarmin-vascular axis: TSLP, from activated endothelium (already mapped) and mast cells (already mapped) in sickle cell disease, primes dendritic cells (already mapped) and amplifies the Th2/eosinophil (already mapped) vascular inflammation of sickle cell disease.
- `connects-to` → **[Histamine](../../03-molecular/histamine/README.md)** — Mast-cell pain axis: histamine, from the mast cells (already mapped) degranulated by sickle-erythrocyte (already mapped) contact, amplifies the vaso-occlusive pain, the pruritus, and the neurogenic inflammation of the pain crises of sickle cell disease.
- `connects-to` → **[Periostin](../../03-molecular/periostin/README.md)** — Fibrotic remodelling: periostin, downstream of the IL-13 (already mapped) and TGF-β (already mapped) signalling in the sickle-cell organ injury, contributes to the pulmonary fibrosis and the renal (already mapped) remodelling of sickle cell disease.
- `connects-to` → **[Melatonin](../../03-molecular/melatonin/README.md)** — Circadian pain-immune axis: melatonin, with its antioxidant and vascular effects on the sickle-erythrocyte (already mapped) fragile endothelium (already mapped), modulates the nocturnal pain-crisis pattern and the oxidative stress of sickle cell disease.
- `connects-to` → **[Testosterone](../../03-molecular/testosterone/README.md)** — Sex-hormone haematopoietic: testosterone stimulates erythropoiesis (EPO already mapped) and modulates the bone-marrow (already mapped) production of red blood cells (already mapped); the sex-hormone erythropoietic axis is relevant to the severity of sickle cell disease.
- `connects-to` → **[Serotonin](../../03-molecular/serotonin/README.md)** — Platelet-serotonin vaso-occlusion: serotonin, released by the activated platelets (already mapped) upon the sickle-erythrocyte-damaged endothelium (already mapped), amplifies the vasoconstriction and the microvascular thrombosis of the vaso-occlusive crises of sickle cell disease.
- `connects-to` → **[Prolactin](../../03-molecular/prolactin/README.md)** — Haematopoietic neuroendocrine: prolactin, via PRLR on macrophages (already mapped) and erythrocytes (already mapped), modulates haematopoiesis; hyperprolactinaemia amplifies the IL-6 (already mapped) and TNF-α (already mapped) vaso-occlusive cascade of sickle cell disease.
- `connects-to` → **[Oxytocin](../../03-molecular/oxytocin/README.md)** — Vaso-occlusion attenuator: oxytocin, via OXTR on endothelial cells (already mapped) and macrophages (already mapped), attenuates vaso-occlusive inflammation; oxytocin deficiency amplifies the IL-6 (already mapped) and NF-κB (already mapped) crisis cascade of sickle cell disease.
- `connects-to` → **[Vasopressin](../../03-molecular/vasopressin/README.md)** — Red-cell hydration modulator: vasopressin, via V2 receptors on erythrocytes (already mapped) and endothelial cells (already mapped), modulates red-cell hydration; vasopressin excess amplifies haemolysis and the nitric-oxide (already mapped) vascular cascade of sickle cell disease.
- `connects-to` → **[Selenium](../../02-atomic/selenium/README.md)** — Haemolysis ROS scavenger: selenium, as GPx in erythrocytes (already mapped) and macrophages (already mapped), limits the haemolysis-driven ROS burden; selenium deficiency amplifies the NLRP3 (already mapped) and NF-κB (already mapped) vaso-occlusive cascade of sickle cell disease.
- `connects-to` → **[Iodine](../../02-atomic/iodine/README.md)** — Thyroid-erythropoiesis axis: iodine-dependent thyroid hormones regulate erythropoiesis (erythropoietin already mapped) and erythrocyte (already mapped) deformability; iodine deficiency amplifies the IL-6 (already mapped) and NLRP3 (already mapped) haemolytic cascade of sickle cell disease.
- `connects-to` → **[Sodium](../../02-atomic/sodium/README.md)** — Red-cell hydration: sodium, via Na⁺/K⁺-ATPase on erythrocytes (already mapped) and endothelial cells (already mapped), regulates red-cell hydration; sodium dysregulation amplifies sickling and the nitric-oxide (already mapped) vascular cascade of sickle cell disease.
- `connects-to` → **[Copper](../../02-atomic/copper/README.md)** — SCD copper: copper, via ceruloplasmin and SOD in endothelial cells (already mapped) and macrophages (already mapped), scavenges ROS; copper deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and NLRP3 (already mapped) haemolytic inflammation in SCD.
- `connects-to` → **[Phosphorus](../../02-atomic/phosphorus/README.md)** — SCD phosphorus: phosphorus, as ATP precursor in erythrocytes (already mapped) and macrophages (already mapped), sustains sickling resistance; phosphorus deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and NLRP3 (already mapped) haemolytic cascade of SCD.
- `connects-to` → **[Chloride](../../02-atomic/chloride/README.md)** — SCD chloride: chloride, via KCC1 in erythrocytes (already mapped) and endothelial cells (already mapped), regulates red-cell volume; chloride dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) sickling and haemolytic cascade of SCD.
- `connects-to` → **[Sulfur](../../02-atomic/sulfur/README.md)** — SCD sulfur: hydrogen sulfide from endothelial cells (already mapped) and macrophages (already mapped) promotes vasodilation; sulfur deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) and NLRP3 (already mapped) vaso-occlusive cascade of SCD.
- `connects-to` → **[Carbon](../../02-atomic/carbon/README.md)** — SCD carbon: carbon, as metabolic backbone of erythrocytes (already mapped) and macrophages (already mapped), fuels haemoglobin (already mapped) synthesis; carbon dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) sickling cascade of SCD.
- `connects-to` → **[Nitrogen](../../02-atomic/nitrogen/README.md)** — SCD nitrogen: nitric oxide from endothelial cells (already mapped) and macrophages (already mapped) promotes vasodilation; nitrogen dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and NLRP3 (already mapped) vaso-occlusive cascade of SCD.
- `connects-to` → **[PD-1](../../03-molecular/pd-1/README.md)** — SCD PD-1: PD-1 checkpoint on macrophages (already mapped) and T-cytotoxic cells (already mapped) modulates immune surveillance of haemolytic erythrocytes; PD-1 dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) cascade of SCD.
- `connects-to` → **[GLP-1](../../03-molecular/glp-1/README.md)** — SCD GLP-1: GLP-1 receptor signalling in macrophages (already mapped) and endothelial cells (already mapped) modulates metabolic and inflammatory vaso-occlusive risk; GLP-1 deficiency amplifies NF-κB (already mapped) and IL-6 (already mapped) cascade of SCD.
- `connects-to` → **[Angiotensin-II](../../03-molecular/angiotensin-ii/README.md)** — SCD angiotensin-II: angiotensin-II signalling in endothelial cells (already mapped) and macrophages (already mapped) promotes vascular inflammation; angiotensin-II excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) cascade of SCD.
- `connects-to` → **[Wnt/β-catenin](../../03-molecular/wnt-beta-catenin/README.md)** — SCD Wnt/β-catenin: Wnt/β-catenin signalling in erythrocytes (already mapped) and macrophages (already mapped) modulates erythropoiesis; Wnt dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) sickling cascade of SCD.
- `connects-to` → **[RANKL](../../03-molecular/rankl/README.md)** — SCD rankl: RANKL from macrophages (already mapped) and endothelial cells (already mapped) promotes vaso-occlusive bone remodelling; rankl excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) sickling cascade of SCD.
- `connects-to` → **[IL-2](../../03-molecular/il-2/README.md)** — SCD il-2: IL-2 from T-cells (already mapped) and macrophages (already mapped) regulates immune surveillance of haemolytic erythrocytes; il-2 dysregulation amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) sickling cascade of SCD.
- `connects-to` → **[Fibronectin](../../03-molecular/fibronectin/README.md)** — SCD fibronectin: fibronectin in fibroblasts (already mapped) and macrophages (already mapped) scaffolds vaso-occlusive ECM; fibronectin excess amplifies NF-κB (already mapped) and IL-6 (already mapped) and VEGF (already mapped) sickling cascade of SCD.
- `connects-to` → **[NOTCH](../../03-molecular/notch/README.md)** — SCD notch: Notch signalling in macrophages (already mapped) and endothelial cells (already mapped) regulates vaso-occlusive cell fate in SCD; notch dysregulation amplifies nf-kb (already mapped) and il-6 (already mapped) and vegf (already mapped) sickling cascade of SCD.
- `connects-to` → **[IGF-1](../../03-molecular/igf-1/README.md)** — SCD igf-1: IGF-1 from macrophages (already mapped) and endothelial cells (already mapped) promotes vascular cell survival in SCD; igf-1 dysregulation amplifies nf-kb (already mapped) and il-6 (already mapped) and vegf (already mapped) sickling cascade of SCD.
- `connects-to` → **[Activin-A](../../03-molecular/activin-a/README.md)** — SCD activin-a: activin-A from macrophages (already mapped) and endothelial cells (already mapped) drives vascular fibrosis in SCD; activin-a excess amplifies nf-kb (already mapped) and il-6 (already mapped) and vegf (already mapped) sickling cascade of SCD.
- `connects-to` → **[TGF-β](../../03-molecular/tgf-beta/README.md)** — SCD tgf-beta: TGF-β from macrophages (already mapped) and endothelial cells (already mapped) drives vascular fibrosis in SCD; tgf-beta excess amplifies nf-kb (already mapped) and il-6 (already mapped) and vegf (already mapped) sickling cascade of SCD.
- `connects-to` → **[CGRP](../../03-molecular/cgrp/README.md)** — SCD cgrp: CGRP from macrophages (already mapped) and endothelial cells (already mapped) modulates vaso-occlusive vascular tone in SCD; cgrp excess amplifies nf-kb (already mapped) and il-6 (already mapped) and vegf (already mapped) sickling cascade of SCD.
- `connects-to` → **[Calcitonin](../../03-molecular/calcitonin/README.md)** — SCD calcitonin: calcitonin from macrophages (already mapped) and endothelial cells (already mapped) modulates calcium balance in SCD; calcitonin excess amplifies nf-kb (already mapped) and il-6 (already mapped) and vegf (already mapped) sickling cascade of SCD.
- `connects-to` → **[Substance P](../../03-molecular/substance-p/README.md)** — SCD substance-p: substance P from macrophages (already mapped) and endothelial cells (already mapped) modulates vaso-occlusive neuroimmune tone; substance-p excess amplifies nf-kb (already mapped) and il-6 (already mapped) and vegf (already mapped) sickling cascade of SCD.
- `connects-to` → **[Insulin Receptor](../../03-molecular/insulin-receptor/README.md)** — SCD insulin-receptor: insulin receptor on macrophages (already mapped) and endothelial cells (already mapped) drives SCD metabolic repair; insulin-receptor loss amplifies nf-kb (already mapped) and il-6 (already mapped) and vegf (already mapped) sickling cascade of SCD.
- `connects-to` → **[Aldosterone](../../03-molecular/aldosterone/README.md)** — SCD aldosterone: aldosterone from macrophages (already mapped) and endothelial cells (already mapped) modulates SCD ion balance; aldosterone excess amplifies nf-kb (already mapped) and il-6 (already mapped) and vegf (already mapped) sickling cascade of SCD.
- `connects-to` → **[Androgen Receptor](../../03-molecular/androgen-receptor/README.md)** — SCD androgen-receptor: androgen receptor on macrophages (already mapped) and endothelial cells (already mapped) modulates SCD hormonal tone; androgen excess amplifies nf-kb (already mapped) and il-6 (already mapped) and vegf (already mapped) sickling cascade of SCD.
- `connects-to` → **[Norepinephrine](../../03-molecular/norepinephrine/README.md)** — SCD norepinephrine: norepinephrine from macrophages (already mapped) and endothelial cells (already mapped) modulates vascular tone in sickle crises; norepinephrine excess amplifies nf-kb (already mapped) and il-6 (already mapped) and vegf (already mapped) cascade of SCD.
- `connects-to` → **[Adrenomedullin](../../03-molecular/adrenomedullin/README.md)** — SCD adrenomedullin: adrenomedullin from macrophages (already mapped) and endothelial cells (already mapped) modulates vascular tone in sickle crises; adrenomedullin loss amplifies nf-kb (already mapped) and il-6 (already mapped) and vegf (already mapped) sickling cascade of SCD.
- `connects-to` → **[BDNF](../../03-molecular/bdnf/README.md)** — SCD bdnf: BDNF from macrophages (already mapped) and endothelial cells (already mapped) modulates neuroinflammatory tone in SCD; bdnf loss amplifies nf-kb (already mapped) and il-6 (already mapped) and vegf (already mapped) sickling cascade of SCD.
- `connects-to` → **[FGFR](../../03-molecular/fgfr/README.md)** — SCD fgfr: FGFR on macrophages (already mapped) and endothelial cells (already mapped) drives SCD vascular remodelling; fgfr dysregulation amplifies nf-kb (already mapped) and il-6 (already mapped) and vegf (already mapped) sickling cascade of SCD.
- `connects-to` → **[Epinephrine](../../03-molecular/epinephrine/README.md)** — SCD epinephrine: epinephrine from macrophages (already mapped) and endothelial cells (already mapped) modulates SCD adrenergic tone; epinephrine excess amplifies nf-kb (already mapped) and il-6 (already mapped) and vegf (already mapped) sickling cascade of SCD.

[^steinberg-1999-scd-management]: Steinberg MH. Management of sickle cell disease. *N Engl J Med.* 1999;340(13):1021-1030. [doi:10.1056/NEJM199904013401307](https://doi.org/10.1056/NEJM199904013401307) · [PubMed 10099145](https://pubmed.ncbi.nlm.nih.gov/10099145/)
[^vichinsky-2000-acs-scd]: Vichinsky EP, Neumayr LD, Earles AN, et al. Causes and outcomes of the acute chest syndrome in sickle cell disease. *N Engl J Med.* 2000;342(25):1855-1865. [doi:10.1056/NEJM200006223422502](https://doi.org/10.1056/NEJM200006223422502) · [PubMed 10861320](https://pubmed.ncbi.nlm.nih.gov/10861320/)
[^niaid-2014-scd-guidelines]: Yawn BP, Buchanan GR, Afenyi-Annan AN, et al. Management of sickle cell disease: summary of the 2014 evidence-based report by expert panel members. *JAMA.* 2014;312(10):1033-1048. [doi:10.1001/jama.2014.10517](https://doi.org/10.1001/jama.2014.10517) · [PubMed 25205765](https://pubmed.ncbi.nlm.nih.gov/25205765/)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
