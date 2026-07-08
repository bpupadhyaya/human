---
schema: human-scale-entry/v1
id: marfan-syndrome
name: Marfan Syndrome
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-07
summary: "Marfan syndrome is caused by germline FBN1 mutations; aortic root dilation (risk of dissection), ectopia lentis, tall stature with long limbs and arachnodactyly; losartan and beta-blockers slow aortic growth; prophylactic aortic surgery when root diameter reaches 5.0 cm."
aliases: ["Marfan syndrome", "Marfan's syndrome", "FBN1 syndrome", "fibrillin-1 Marfan", "Marfan aortic aneurysm", "Marfan aortic dissection", "Marfan ectopia lentis", "Marfan connective tissue", "MFS", "Marfan cardiovascular"]
sources:
  - id: dietz-1991-fbn1-marfan
    type: peer-reviewed
    cite: "Dietz HC, Cutting GR, Pyeritz RE, et al. Marfan syndrome caused by a recurrent de novo missense mutation in the fibrillin gene. Nature. 1991;352(6333):337-339."
    doi: "10.1038/352337a0"
    pmid: "1852208"
    url: "https://doi.org/10.1038/352337a0"
  - id: loeys-2010-ghent-criteria
    type: peer-reviewed
    cite: "Loeys BL, Dietz HC, Braverman AC, et al. The revised Ghent nosology for the Marfan syndrome. J Med Genet. 2010;47(7):476-485."
    doi: "10.1136/jmg.2009.072785"
    pmid: "20591885"
    url: "https://doi.org/10.1136/jmg.2009.072785"
cross_links:
  - target: 01-human/03-molecular/fbn1
    relation: connects-to
    note: "Germline FBN1 haploinsufficiency or dominant-negative mutations → Marfan syndrome; FBN1 LOF reduces microfibril scaffold → less TGF-β sequestration → excess TGF-β signaling → SMAD2/3 activation → aortic smooth muscle cell phenotypic switch → progressive aortic root aneurysm."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "FBN1 microfibrils bind LTBP (latent TGF-β binding protein) → sequester TGF-β in ECM; FBN1 LOF → reduced TGF-β sequestration → excess TGF-β → ERK and SMAD2/3 activation in aortic SMCs → MMP production → elastic lamina fragmentation → aneurysm formation."
  - target: 01-human/03-molecular/smad4
    relation: connects-to
    note: "FBN1 LOF → excess TGF-β signaling → SMAD2/3 phosphorylation → nuclear translocation → aortic gene expression changes driving aneurysm; SMAD4 is the common SMAD that co-activates SMAD2/3 transcription; SMAD4 mutations in juvenile polyposis syndrome also cause aortic aneurysm."
  - target: 01-human/03-molecular/collagen
    relation: connects-to
    note: "FBN1 fibrillin-1 microfibrils and collagen fibers are the two major structural components of the arterial wall ECM; fibrillin-1 provides elastic recoil; collagen provides tensile strength; Marfan syndrome (FBN1) and OI (COL1A1/2) both affect connective tissue integrity."
  - target: 01-human/03-molecular/angiotensin-ii
    relation: connects-to
    note: "Losartan (AT1R blocker) reduces angiotensin II → attenuated TGF-β signaling in aortic SMCs → slower aortic root growth in MFS (COMPARE trial); AT1R-TGF-β crosstalk: angiotensin II stimulates TGF-β1 production and SMAD2/3 activation → MMP-mediated ECM degradation in aortic wall."
  - target: 01-human/03-molecular/fibronectin
    relation: connects-to
    note: "Fibronectin and fibrillin-1 are both major aortic ECM scaffolding proteins; fibronectin provides SMC adhesion substrate; fibrillin-1 provides elastic recoil; fibronectin deposition increases in Marfan aortic tissue as a compensatory response to fibrillin-1 microfibril failure."
  - target: 01-human/07-system/hypertension
    relation: connects-to
    note: "Hypertension management is critical in Marfan syndrome: elevated SBP increases aortic wall shear stress → accelerated root aneurysm growth; beta-blockers (atenolol) reduce HR + BP + aortic pulsatility; losartan provides additional AT1R/TGF-β inhibition; target SBP <120 mmHg."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "The heart and aorta carry Marfan's lethal risk: FBN1 deficiency lets excess TGF-β weaken the aortic media, producing progressive aortic-root dilatation that can dissect or rupture; β-blockers and losartan slow root growth, and prophylactic root replacement at ~5 cm prevents it."
  - target: 01-human/06-organ/eye
    relation: connects-to
    note: "The lens betrays Marfan syndrome: ectopia lentis — upward dislocation of the lens from stretched, failing zonular fibers (made of fibrillin-1) — is a cardinal diagnostic criterion present in ~60%; Marfan eyes are also myopic and prone to retinal detachment and early glaucoma."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "The skeleton makes Marfan visible: tall stature with disproportionately long limbs and fingers (arachnodactyly), arm-span-to-height >1.05, pectus deformity, scoliosis, and joint hypermobility all stem from fibrillin-1's role in connective tissue — scored in the Ghent criteria."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "The cardiovascular system carries Marfan's lethal risk: fibrillin-1 deficiency weakens the aortic media, so progressive aortic-root dilatation leads to dissection or rupture—the main cause of death—while mitral valve prolapse adds regurgitation; β-blockers/ARBs and surgery help."
  - target: 01-human/04-cellular/smooth-muscle-cell
    relation: connects-to
    note: "Marfan is a disease of the aortic smooth-muscle-cell environment: fibrillin-1 loss frees excess TGF-β in the media, so vascular smooth muscle cells lose elastic-fiber anchorage and undergo apoptosis and phenotype switching—weakening the aortic wall toward aneurysm and dissection."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "The lung is an underrecognized Marfan target: weakened connective tissue predisposes to apical blebs and spontaneous pneumothorax (in ~5-10%), and emphysematous changes and restrictive disease from chest-wall deformity (pectus, scoliosis) can further impair breathing."
  - target: 01-human/04-cellular/fibroblast
    relation: connects-to
    note: "Fibroblasts build Marfan's failing scaffold: they secrete fibrillin-1 to assemble microfibrils that lend connective tissue elasticity and sequester TGF-β, so FBN1 mutations leave microfibrils defective—weakening aorta, lens zonules and ligaments and unleashing TGF-β."
  - target: 01-human/06-organ/skin
    relation: connects-to
    note: "The skin shows Marfan's connective-tissue defect: deficient fibrillin-1 microfibrils reduce dermal elasticity, producing striae atrophicae (stretch marks) and sometimes thin, hyperextensible skin—visible clues to a disorder whose real danger lies in the aorta."
  - target: 01-human/07-system/stroke
    relation: connects-to
    note: "Marfan syndrome raises stroke risk through vascular fragility: aortic root disease can throw cardioembolic clots, and the same fibrillin-1 weakness predisposes to cervical artery dissection—so an aortic disease can also strike the brain."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "Marfan syndrome weakens the lungs: fibrillin-deficient connective tissue forms apical blebs that rupture, causing spontaneous pneumothorax, and chest-wall deformity restricts breathing—so respiratory complications add to the cardiovascular and skeletal features."
  - target: 01-human/04-cellular/osteoblast
    relation: connects-to
    note: "Marfan's skeletal overgrowth reflects disordered bone formation: excess TGF-beta signaling from fibrillin-1 loss drives long-bone overgrowth, giving tall stature and arachnodactyly—so bone-forming cells build too much skeleton on a faulty connective scaffold."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "Dural ectasia is a hallmark Marfan feature: weakened connective tissue lets the dura around the lower spine balloon out, causing back pain and headaches and serving as a diagnostic criterion—showing Marfan's reach into the nervous system's coverings."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "Marfan syndrome shows in the skin and soft tissue: fibrillin-1 loss weakens connective tissue throughout, producing striae (stretch marks) without weight change, thin skin and hernias—visible signs of the same defect that endangers the aorta."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "Pregnancy is dangerous in Marfan syndrome: the hemodynamic load and hormonal softening of connective tissue sharply raise the risk of aortic dissection, so the reproductive years demand careful cardiac monitoring and counseling in affected women."
  - target: 01-human/03-molecular/growth-hormone
    relation: connects-to
    note: "Marfan's tall stature is not from growth hormone: unlike pituitary gigantism, the overgrowth comes from defective fibrillin-1 connective tissue, so patients are tall with long limbs and arachnodactyly despite normal growth-hormone levels—a key diagnostic distinction."
  - target: 01-human/04-cellular/cardiomyocyte
    relation: connects-to
    note: "Marfan can weaken heart muscle itself: beyond valve and aortic disease, excess TGF-beta signaling produces an intrinsic cardiomyopathy in which cardiomyocyte dysfunction mildly dilates and weakens the left ventricle, so the heart is monitored even when valves look normal."
  - target: 01-human/05-tissue/fibrosis
    relation: connects-to
    note: "The Marfan aorta fails through medial degeneration: fibrillin loss and unleashed TGF-beta fragment elastic fibers and drive fibrosis in the vessel wall, weakening it until the aortic root dilates and risks dissection—the syndrome's lethal complication."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "Marfan vessels show endothelial dysfunction: the abnormal fibrillin matrix and altered TGF-beta signaling impair the endothelial cells lining the aorta, reducing flow-mediated dilation and adding to the wall stress that drives aneurysm."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "Marfan's weak connective tissue threatens oxygen supply through pneumothorax: fragile apical lung blebs rupture and collapse the lung, cutting off air exchange—a recurrent emergency in tall, Marfan-bodied patients."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "Mast cells help weaken the Marfan aorta: they infiltrate the aneurysmal aortic wall and release proteases that chew through the elastic media, adding to the matrix breakdown that drives dilation toward dissection."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "Marfan aneurysms are fueled by overactive mTOR: disrupted fibrillin and TGF-β signaling ramp up mTOR in the aortic wall, driving the smooth-muscle changes behind aortic dilation—so rapamycin-class drugs are studied to slow it."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "Marfan often enlarges the spinal dura around the brain's continuation: dural ectasia—ballooning of the dural sac—is a common, weakly symptomatic feature that, found on imaging, helps confirm the diagnosis."
  - target: 01-human/03-molecular/akt
    relation: connects-to
    note: "Marfan aortas grow weak partly through AKT signaling: disrupted fibrillin and TGF-beta ramp up AKT alongside mTOR in the vessel wall, driving the smooth-muscle changes behind aneurysm, so this growth axis is studied as a drug target."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "Inflammation via NF-kB worsens the Marfan aorta: the failing elastic wall activates this inflammatory switch, recruiting cells and enzymes that degrade the matrix further, accelerating the dilation toward dissection."
  - target: 01-human/02-atomic/nitrogen
    relation: connects-to
    note: "Marfan lungs can burst air into the chest: weak connective tissue forms apical blebs that rupture, spilling air—mostly nitrogen—into the pleural space as a spontaneous pneumothorax, a recurrent Marfan event."
  - target: 01-human/05-tissue/alveolus
    relation: connects-to
    note: "Marfan weakens the alveoli: faulty fibrillin leaves the lung's elastic walls fragile, so emphysematous change and apical blebs form in the air sacs, setting up the collapse-prone lung."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "Marfan can stretch the nerves through dural ectasia: the weakened dura around the spinal cord balloons, compressing nerve roots to cause low back pain, headaches, and leg symptoms, a diagnostic Marfan feature."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Marfan is monitored by imaging: echocardiography and CT/MR angiography photons track the aortic root's slow dilation, the measurement that decides when to operate before it dissects."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Marfan's floppy mitral valve calcifies early: mitral annular calcification is part of the Ghent diagnostic score, adding to the valve prolapse and aortic disease of the connective-tissue disorder."
  - target: 01-human/03-molecular/pdgf
    relation: connects-to
    note: "Growth-factor signaling beyond TGF-β weakens the Marfan aorta: PDGF among others drives the smooth-muscle changes in the dilating wall, part of the biology that aneurysm treatments target."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy exposes the failing Marfan aorta: defective fibrillin leaves the elastic fibers of the arterial wall fragmented and frayed — cystic medial degeneration — the structural rot that lets the aorta balloon and tear."
  - target: 01-human/06-organ/large-intestine
    relation: connects-to
    note: "Weak connective tissue gives way throughout the body: Marfan brings hernias, diverticula, and rectal prolapse, the lax collagen and elastin of the gut wall and abdominal wall failing under everyday pressure."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "The kidney's moorings loosen in Marfan: with its supporting connective tissue lax, the kidney can drop out of position (nephroptosis), one of the quieter manifestations of the body-wide tissue weakness."
  - target: 01-human/04-cellular/osteoclast
    relation: connects-to
    note: "Marfan bones grow long but thin: excess TGF-β signaling tilts remodeling toward osteoclast resorption, so despite the overgrowth of the long limbs many patients carry reduced bone density and an osteopenia that belies their tall frame."
  - target: 01-human/06-organ/placenta
    relation: connects-to
    note: "Pregnancy is the Marfan aorta's danger window: the volume load and hormone-softened vessels needed to perfuse the placenta peak the risk of aortic dissection around delivery, demanding echo monitoring and sometimes pre-pregnancy aortic repair."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "The floppy Marfan mitral valve flutters the rhythm: mitral valve prolapse is associated with magnesium deficiency, and magnesium repletion can ease the palpitations and arrhythmias these prolapsing valves so often provoke."
  - target: 01-human/07-system/osteoporosis
    relation: connects-to
    note: "The long Marfan bones are also thin: despite their height, patients often have reduced bone mineral density and osteopenia, likely tied to the disturbed fibrillin-TGF-beta signaling that governs bone as well as connective tissue."
  - target: 01-human/04-cellular/adipocyte
    relation: connects-to
    note: "Marfan bodies carry little fat: the classic tall, slender build comes with scant subcutaneous adipose and low muscle mass, the lean habitus that — with long limbs and arachnodactyly — helps flag the syndrome on sight."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "Living with a fragile aorta weighs on the mind: rates of anxiety and depression run high in Marfan, driven by the constant threat of dissection, lifelong activity limits and body-image concerns, so psychological support is part of comprehensive care."
  - target: 01-human/03-molecular/erk1-2
    relation: connects-to
    note: "The damage runs through a side channel: the excess TGF-β freed by fibrillin-1 loss fires the non-canonical ERK1/2 (MAPK) pathway in the aortic wall, a driver of aneurysm growth that losartan helps blunt — explaining why an angiotensin blocker protects the aorta."
  - target: 01-human/07-system/heart-failure
    relation: connects-to
    note: "The valves can wear the heart out: chronic aortic and mitral regurgitation from Marfan's stretched valve tissue overloads the ventricle for years, so beyond the dissection threat the disease can drift into heart failure if the leaks go uncorrected."
  - target: 01-human/07-system/copd
    relation: connects-to
    note: "The lung's scaffolding fails diffusely too: beyond the dramatic spontaneous pneumothorax, defective elastin leaves the airspaces prone to emphysema-like destruction and accelerated decline in lung function, a quieter respiratory toll of the connective-tissue defect."
  - target: 01-human/03-molecular/nitric-oxide
    relation: connects-to
    note: "The aortic endothelium loses its NO balance: dysregulated endothelial nitric-oxide signaling in Marfan contributes to the stiffening and weakening of the aortic wall, part of the vascular dysfunction behind aneurysm formation."
  - target: 01-human/03-molecular/endothelin-1
    relation: connects-to
    note: "Vasoactive signaling remodels the wall: raised endothelin-1 promotes smooth-muscle and matrix changes in the Marfan aorta, adding a vasoconstrictor-driven arm to the TGF-β-led remodeling that grows the aneurysm."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "Major aortic surgery brings clot risk: the prophylactic aortic root and valve operations central to Marfan care carry a perioperative venous thromboembolism risk requiring prophylaxis."
  - target: 01-human/03-molecular/connexin43
    relation: connects-to
    note: "The Marfan heart can beat erratically: gap-junction remodeling and a primary myopathy predispose to ventricular arrhythmia and sudden cardiac death, a risk in Marfan beyond the aortic and valve disease."
  - target: 01-human/03-molecular/troponin-complex
    relation: connects-to
    note: "The heart muscle itself is affected: Marfan can cause a primary cardiomyopathy independent of valve and aortic disease, with subclinical myocardial dysfunction reflected in troponin and impaired contractility."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "Living with a life-threatening syndrome weighs on the mind: the activity restrictions, body-image concerns and fear of aortic dissection in Marfan drive elevated rates of depression alongside its anxiety."
  - target: 01-human/07-system/sepsis
    relation: connects-to
    note: "Abnormal valves and aortic grafts invite infection: Marfan's mitral and aortic valve disease predisposes to infective endocarditis, and prosthetic aortic grafts can become infected, both able to seed sepsis."
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "Aortic dissection can starve the kidneys: a dissection extending to the renal arteries causes renal malperfusion and infarction, and the perioperative injury of major aortic surgery can leave chronic kidney impairment."
  - target: 01-human/07-system/pulmonary-arterial-hypertension
    relation: connects-to
    note: "Chest deformity and lung disease strain the right heart: severe scoliosis, pectus deformity and apical bullae in Marfan restrict the lungs and, with chronic hypoxia, can raise pulmonary pressures toward cor pulmonale."
  - target: 01-human/07-system/wound-healing
    relation: connects-to
    note: "Faulty connective tissue heals poorly: the fibrillin defect of Marfan weakens the matrix that wounds rebuild, so surgical incisions — including major aortic operations — and skin are prone to poor healing and hernia."
  - target: 01-human/07-system/neuropathic-pain
    relation: connects-to
    note: "Dural ectasia presses on the nerves: the ballooning of the dural sac, a characteristic Marfan feature, stretches lumbosacral nerve roots and causes chronic low back and radicular neuropathic pain."
  - target: 01-human/07-system/insomnia-disorder
    relation: connects-to
    note: "Its craniofacial build disturbs sleep: the high-arched palate and retrognathia of Marfan predispose to obstructive sleep apnea, fragmenting sleep and worsening daytime function and cardiovascular strain."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "Weak connective tissue herniates and tears: Marfan brings recurrent inguinal and incisional hernias, and an aortic dissection that extends to the mesenteric arteries can starve the bowel of blood."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "Aortic dissection threatens the kidneys: a dissection extending along the aorta can occlude a renal artery, causing renal malperfusion and acute kidney injury, a feared complication in Marfan."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "Its protective therapy works through a hormone axis: losartan and other ARBs used to slow aortic growth in Marfan block the angiotensin II of the renin-angiotensin endocrine system, dampening TGF-β signalling."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "Its defect unleashes a regulatory cytokine: fibrillin-1 normally sequesters TGF-β in the matrix, so its deficiency releases excess TGF-β — a key immunoregulatory growth factor — that drives the tissue weakening of Marfan."
  - target: 02-pathogen/02-bacteria/staphylococcus-aureus
    relation: connects-to
    note: "Its valves and grafts invite infection: damaged valves and prosthetic aortic grafts after surgery raise the risk of infective endocarditis, classically from Staphylococcus aureus and viridans streptococci."
  - target: 03-medicine/01-modern/04-cardio/beta-blockers
    relation: connects-to
    note: "Beta-blockers protect its aorta: by lowering heart rate and the force of ejection, beta-blockers reduce aortic wall stress and slow aneurysm growth, a mainstay of Marfan management alongside ARBs."
  - target: 03-medicine/01-modern/04-cardio/arbs
    relation: connects-to
    note: "They blunt the underlying signal: angiotensin-receptor blockers like losartan reduce the excess TGF-β signalling that drives aortic-root dilation in Marfan syndrome, slowing its enlargement."
  - target: 03-medicine/01-modern/09-hematology/warfarin
    relation: connects-to
    note: "A mechanical valve needs lifelong anticoagulation: after aortic-root replacement with a mechanical valve for Marfan syndrome, warfarin prevents valve thrombosis and embolic stroke."
  - target: 03-medicine/01-modern/04-cardio/aspirin
    relation: connects-to
    note: "Bioprosthetic repairs take antiplatelet cover: patients with a tissue aortic valve or vascular stent for Marfan-related disease use aspirin, a lighter alternative to the warfarin that mechanical valves require."
  - target: 01-human/05-tissue/arterial-wall
    relation: connects-to
    note: "It weakens the aorta's wall: loss of fibrillin microfibrils and excess TGF-β cause cystic medial degeneration of the aortic wall, driving the progressive aortic-root aneurysm and dissection that are Marfan's lethal hallmark."
  - target: 03-medicine/01-modern/04-cardio/calcium-channel-blockers
    relation: connects-to
    note: "A drug class to avoid: unlike beta-blockers and ARBs, calcium-channel blockers are associated with faster aortic growth and worse outcomes in Marfan syndrome and are generally avoided."
  - target: 01-human/05-tissue/cortical-bone
    relation: connects-to
    note: "It overgrows and thins the skeleton: fibrillin loss lengthens the long bones (arachnodactyly, tall stature) while reducing cortical bone density, contributing to scoliosis and chest-wall deformity."
  - target: 01-human/05-tissue/endocardium
    relation: connects-to
    note: "It loosens the heart valves: fibrillin-1 loss and excess TGF-β weaken the valve leaflets, producing the myxomatous mitral valve prolapse and aortic regurgitation that, with aortic root dilatation, define Marfan's cardiac disease."
  - target: 01-human/05-tissue/cardiac-conduction-system
    relation: connects-to
    note: "Beyond the aorta, an electrical risk: Marfan syndrome carries ventricular arrhythmias and a small risk of sudden cardiac death independent of valve and aortic disease, linked to conduction abnormalities and fibrillin-related myocardial changes."
  - target: 01-human/07-system/juvenile-polyposis-syndrome
    relation: connects-to
    note: "Opposite ends of one signalling axis: Marfan stems from FBN1 loss that unleashes excess TGF-β, while SMAD4-type juvenile polyposis loses the TGF-β/BMP transducer itself—two diseases dysregulating the same pathway from opposite directions."
  - target: 01-human/05-tissue/myocardium
    relation: connects-to
    note: "Primary Marfan cardiomyopathy: beyond valve and aortic disease, FBN1 loss causes an intrinsic dilated cardiomyopathy of the myocardium, a less-recognised cause of heart failure in Marfan syndrome."
  - target: 01-human/05-tissue/peripheral-nerve
    relation: connects-to
    note: "Dural ectasia: the enlarging dural sac of Marfan erodes vertebrae and stretches nerve roots, causing low-back and radicular pain and headaches—a major diagnostic criterion."
  - target: 01-human/07-system/systemic-sclerosis
    relation: connects-to
    note: "Two connective-tissue disorders via TGF-β: Marfan's fibrillin loss unleashes excess TGF-β signalling, while systemic sclerosis is autoimmune TGF-β-driven fibrosis—structural versus inflammatory routes to matrix dysregulation."
  - target: 01-human/07-system/atherosclerosis
    relation: connects-to
    note: "Two roads to an aortic aneurysm: Marfan's fibrillin-1 loss causes cystic medial degeneration of the young aorta, distinct from the lipid-driven atherosclerotic aneurysm of older age—same catastrophic endpoint, different wall pathology."
  - target: 01-human/03-molecular/bnp
    relation: connects-to
    note: "Volume-loading the heart: chronic aortic and mitral regurgitation in Marfan stretches the ventricle, raising BNP as a marker of the heart failure that valve and aortic-root disease eventually cause."
  - target: 01-human/03-molecular/igf-1
    relation: connects-to
    note: "The overgrowth axis: the tall stature and arachnodactyly of Marfan reflect dysregulated TGF-β interacting with GH/IGF-1 growth signalling, driving the excessive long-bone growth characteristic of the syndrome."
  - target: 01-human/03-molecular/caspase-3
    relation: connects-to
    note: "Medial degeneration: apoptosis of aortic smooth-muscle cells via caspase-3 thins and weakens the aortic media in Marfan, a core mechanism behind aneurysm and dissection."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Wall inflammation: cytotoxic T cells infiltrate the degenerating aortic wall in Marfan and other aneurysmal aortopathies, contributing to medial breakdown."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "Adventitial neovessels: VEGF-driven vasa-vasorum proliferation accompanies the medial degeneration of the Marfan aorta, a feature of the remodelling aneurysmal wall."
  - target: 01-human/03-molecular/ccl2
    relation: connects-to
    note: "Macrophage recruitment: CCL2 draws macrophages into the degenerating Marfan aortic wall, where their proteases accelerate the medial breakdown that drives aneurysm."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "Aortic inflammation: IL-6 within the Marfan aortic wall amplifies the inflammatory remodelling that weakens the media and predicts aneurysm progression."
  - target: 01-human/03-molecular/tnf-alpha
    relation: connects-to
    note: "Inflammatory medial breakdown: TNF-α contributes to the smooth-muscle apoptosis and matrix degradation of the Marfan aorta, compounding the primary fibrillin defect."
  - target: 01-human/03-molecular/aldosterone
    relation: connects-to
    note: "Mineralocorticoid remodelling: aldosterone and mineralocorticoid-receptor signalling promote aortic fibrosis and stiffening, and MR antagonists are studied alongside ARBs to slow aortic dilatation in Marfan syndrome."
  - target: 01-human/03-molecular/rankl
    relation: connects-to
    note: "Reduced bone density: Marfan syndrome is associated with low bone mineral density, with RANKL-driven osteoclast activity contributing to the osteopenia that adds to its skeletal manifestations."
  - target: 01-human/03-molecular/adrenomedullin
    relation: connects-to
    note: "Vascular peptide: adrenomedullin, a fibrillin-associated vasodilator peptide, is dysregulated in Marfan syndrome, contributing to the abnormal vascular tone and wall homeostasis of the dilating aorta."
  - target: 01-human/03-molecular/beta1-adrenergic-receptor
    relation: connects-to
    note: "Hemodynamic protection: beta-blockers acting on β1-adrenergic receptors lower heart rate and the rate of aortic-pressure rise (dP/dt), reducing wall stress to slow aortic-root dilation — the longstanding mainstay of Marfan aortic protection."
  - target: 01-human/03-molecular/estrogen
    relation: connects-to
    note: "Pregnancy aortic risk: pregnancy markedly raises the risk of aortic dissection in Marfan syndrome through combined hemodynamic and hormonal effects on the already weakened aortic wall, demanding intensive cardiac surveillance."
  - target: 01-human/03-molecular/il-1b
    relation: connects-to
    note: "Inflammatory medial degeneration: IL-1β and inflammatory signalling contribute to the medial degeneration and matrix breakdown of the Marfan aorta, an inflammatory arm of aneurysm formation layered on the excess TGF-β signalling."
  - target: 01-human/03-molecular/periostin
    relation: connects-to
    note: "Aortic remodelling: periostin is upregulated in the Marfan aortic wall, where this matricellular protein participates in the maladaptive medial remodelling and matrix disorganisation that weaken the aorta and predispose it to aneurysm and dissection."
  - target: 01-human/03-molecular/galectin-3
    relation: connects-to
    note: "Aortic fibrosis: galectin-3 promotes the inflammation and fibrosis of the degenerating Marfan aortic media, a profibrotic lectin studied as a biomarker of aortic-wall disease and risk of aneurysm progression."
  - target: 01-human/03-molecular/renin
    relation: connects-to
    note: "RAAS-TGF-β crosstalk: angiotensin signalling downstream of renin amplifies aortic TGF-β activity, the rationale for the angiotensin-receptor blocker losartan, which slows aortic-root dilatation in Marfan beyond simple blood-pressure lowering."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "PI3K-mTOR limb: dysregulated TGF-β and IGF-1 signalling (both mapped) engages PI3K-AKT-mTOR (AKT and mTOR already mapped), driving the smooth-muscle-cell changes of the Marfan aortic wall and a candidate target in aneurysm."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "Aortic inflammation: a Th17/IL-17 inflammatory infiltrate in the aortic media contributes to the wall remodelling and progression of aneurysm in Marfan syndrome."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Complement in the wall: complement activation generating C3 fragments amplifies the inflammatory injury of the Marfan aortic media, adding to the matrix breakdown that predisposes to dissection."
  - target: 01-human/03-molecular/kras
    relation: connects-to
    note: "Non-canonical TGF-β: non-canonical TGF-β signalling activates RAS-ERK (ERK1/2 already mapped), a driver of the aortic-wall degeneration in Marfan syndrome that complements the canonical SMAD pathway."
  - target: 01-human/03-molecular/nfe2l2
    relation: connects-to
    note: "Aortic oxidative stress: NRF2 antioxidant defence counters the oxidative stress accompanying the smooth-muscle-cell dysfunction and matrix breakdown of the Marfan aorta."
  - target: 01-human/03-molecular/myd88
    relation: connects-to
    note: "Inflammatory remodelling: macrophage TLR-MyD88-NF-κB signalling (NF-κB already mapped) contributes the inflammatory component of aortic-wall remodelling and aneurysm progression in Marfan syndrome."
  - target: 01-human/03-molecular/jak1-2
    relation: connects-to
    note: "IL-6-JAK-STAT signalling (IL-6 mapped) contributes to the medial inflammation accompanying aortic-wall degeneration in Marfan syndrome."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "STAT3-driven inflammatory signalling participates in the vascular-smooth-muscle and inflammatory response of the Marfan aortopathy."
  - target: 01-human/03-molecular/pten
    relation: connects-to
    note: "PTEN regulation of PI3K-AKT-mTOR signalling (AKT, PIK3CA and mTOR mapped) modulates the vascular-smooth-muscle phenotype in the aortic wall affected by Marfan syndrome."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "Cytosolic DNA sensing through cGAS-STING contributes to the vascular-wall inflammation that accompanies the aortic aneurysm progression of Marfan syndrome."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "IFN-STAT1 signalling shapes the immune-cell infiltration of the aortic wall in the aneurysmal disease of Marfan syndrome."
  - target: 01-human/03-molecular/foxo
    relation: connects-to
    note: "FOXO transcription factors regulate the oxidative-stress resistance and contractile phenotype of the aortic smooth-muscle cells weakened in Marfan syndrome."
  - target: 01-human/03-molecular/gsk-3b
    relation: connects-to
    note: "GSK-3β participates in the vascular smooth-muscle signaling and TGF-β crosstalk relevant to the aortic remodeling of Marfan syndrome."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "HIF-1α in the mechanically stressed aortic wall contributes to the vascular remodeling and matrix dysregulation of Marfan syndrome."
  - target: 01-human/03-molecular/s100a8-a9
    relation: connects-to
    note: "S100A8/A9 alarmins reflect the inflammatory component of the aortic-wall remodeling in Marfan syndrome."
  - target: 01-human/03-molecular/ampk
    relation: connects-to
    note: "AMPK-linked metabolic and mechanotransduction signaling participates in the vascular smooth-muscle homeostasis disrupted in the aortic wall of Marfan syndrome."
  - target: 01-human/03-molecular/autophagy
    relation: connects-to
    note: "Autophagy modulates the vascular smooth-muscle-cell survival and phenotypic switching in the aortic aneurysm of Marfan syndrome."
  - target: 01-human/03-molecular/src-kinase
    relation: connects-to
    note: "SRC-family kinase signaling downstream of angiotensin-II and TGF-β receptors (both already mapped) contributes to the aortic-wall remodeling of Marfan syndrome."
  - target: 01-human/03-molecular/ccr5
    relation: connects-to
    note: "CCR5-driven leukocyte recruitment into the aortic wall contributes to the inflammatory component of the aortopathy of Marfan syndrome."
  - target: 01-human/03-molecular/dnmt3a
    relation: connects-to
    note: "DNMT3A-mediated DNA methylation participates in the epigenetic regulation of the vascular-smooth-muscle-cell phenotype in Marfan syndrome."
  - target: 01-human/03-molecular/notch
    relation: connects-to
    note: "NOTCH signaling participates in the vascular-smooth-muscle-cell differentiation and aortic-wall homeostasis dysregulated in Marfan syndrome."
  - target: 01-human/03-molecular/cxcl12
    relation: connects-to
    note: "CXCL12-CXCR4 signaling participates in the vascular smooth-muscle-cell and endothelial responses of the aortopathy of Marfan syndrome."
  - target: 01-human/03-molecular/arid1a
    relation: connects-to
    note: "ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic regulation of the connective-tissue gene programs relevant to Marfan syndrome."
  - target: 01-human/03-molecular/il-33
    relation: connects-to
    note: "IL-33 alarmin signaling participates in the vascular inflammation relevant to the aortopathy of Marfan syndrome."
  - target: 01-human/03-molecular/calcineurin
    relation: connects-to
    note: "Calcineurin-NFAT signaling participates in the cardiovascular-smooth-muscle and immune responses relevant to Marfan syndrome."
  - target: 01-human/03-molecular/adenosine
    relation: connects-to
    note: "Adenosine signaling participates in the vascular-tone regulation relevant to the aortopathy of Marfan syndrome."
  - target: 01-human/03-molecular/osteopontin
    relation: connects-to
    note: "Osteopontin participates in the aortic extracellular-matrix remodeling and aneurysm pathology of Marfan syndrome."
  - target: 01-human/03-molecular/xanthine-oxidase
    relation: connects-to
    note: "Oxidative aortic degeneration: oxidative stress in the Marfan aortic wall, to which xanthine oxidase contributes, activates matrix metalloproteinases and promotes the smooth-muscle (already mapped) loss and elastic-fibre fragmentation that drive aneurysm formation."
  - target: 01-human/03-molecular/insulin-receptor
    relation: connects-to
    note: "Growth axis: the tall stature and long limbs of Marfan syndrome reflect the growth-hormone/IGF-1 axis (both already mapped) signalling through the insulin/IGF receptors, and modulating this overgrowth has been explored to limit skeletal disproportion."
  - target: 01-human/03-molecular/progesterone
    relation: connects-to
    note: "Pregnancy aortic risk: pregnancy sharply raises the risk of aortic dissection in Marfan syndrome, as the haemodynamic load and the hormonal effects of progesterone and estrogen (already mapped) on the vessel wall weaken the already-fragile aorta."
  - target: 01-human/03-molecular/von-willebrand-factor
    relation: connects-to
    note: "Endothelial dysfunction: the abnormal aortic wall of Marfan syndrome disturbs the endothelium (nitric oxide already mapped), raising von Willebrand factor, a marker of the endothelial activation that accompanies the aortopathy and its thrombotic risk during dissection."
  - target: 01-human/03-molecular/prostaglandins
    relation: connects-to
    note: "Vascular eicosanoids: prostaglandins modulate the tone and inflammation of the aortic wall, contributing with the cytokines already mapped to the vascular remodelling that, driven by dysregulated TGF-beta (already mapped), weakens the Marfan aorta."
  - target: 01-human/03-molecular/il-10
    relation: connects-to
    note: "Inflammatory balance: the anti-inflammatory IL-10 counters the TNF, IL-6 and IL-1 (already mapped) infiltrating the dilating aortic wall, and this cytokine balance shapes the inflammatory component of the aneurysm formation in Marfan syndrome."
  - target: 01-human/03-molecular/serotonin
    relation: connects-to
    note: "Myxomatous valve degeneration: serotonergic signalling, interacting with the dysregulated TGF-beta (already mapped), contributes to the myxomatous mitral-valve degeneration and prolapse that accompanies the aortic disease of Marfan syndrome."
  - target: 01-human/03-molecular/il-13
    relation: connects-to
    note: "Fibrotic remodelling: IL-13, a profibrotic cytokine acting through TGF-beta (already mapped), contributes to the fibrotic remodelling of the aortic wall, part of the connective-tissue dysregulation of Marfan syndrome."
  - target: 01-human/02-atomic/copper
    relation: connects-to
    note: "Lysyl-oxidase crosslinking: copper is the cofactor for lysyl oxidase, the enzyme that crosslinks collagen and elastin (collagen already mapped) into strong fibres, so this metal is essential to the connective-tissue integrity deranged in Marfan syndrome."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "Matrix metalloproteinases: zinc is the cofactor of the matrix metalloproteinases that degrade the elastin and collagen (already mapped) of the aortic media, the MMP activity contributing to the aneurysm and dissection of Marfan syndrome."
  - target: 01-human/03-molecular/il-4
    relation: connects-to
    note: "Pro-fibrotic type-2: IL-4, with IL-13 (already mapped), drives the type-2/pro-fibrotic (TGF-β already mapped) programme in the remodelling of the aortic wall of Marfan syndrome."
  - target: 01-human/03-molecular/histamine
    relation: connects-to
    note: "Mast-cell aortopathy: mast cells accumulate in the aneurysmal aortic wall of Marfan syndrome, releasing histamine and proteases that contribute, with the matrix metalloproteinases, to the medial degeneration."
  - target: 01-human/02-atomic/zinc
    relation: connects-to
    note: "Matrix metalloproteinases: the zinc-dependent matrix metalloproteinases degrade the elastin and collagen (already mapped) of the aortic media, contributing, with the fibrillin (FBN1 already mapped) defect, to the aneurysm of Marfan syndrome."
  - target: 01-human/03-molecular/leptin
    relation: connects-to
    note: "Lean-habitus adipokine: leptin reflects the reduced fat mass and the metabolic profile of the tall, thin (dolichostenomelia) habitus of Marfan syndrome."
  - target: 01-human/03-molecular/adiponectin
    relation: connects-to
    note: "Body-composition adipokine: adiponectin, with leptin (already mapped), is part of the adipokine profile of the altered body composition and metabolism of Marfan syndrome."
  - target: 01-human/03-molecular/resistin
    relation: connects-to
    note: "Body-composition adipokine: resistin, with leptin and adiponectin (already mapped), completes the adipokine profile of the altered body composition and metabolism of Marfan syndrome."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Aortic-wall macrophages: the macrophage infiltration and the inflammation (CCL2 and IL-6 already mapped) of the aortic media contribute to the aneurysm progression of Marfan syndrome."
  - target: 01-human/03-molecular/ifn-gamma
    relation: connects-to
    note: "Aortic Th1 inflammation: the IFN-γ of the T cells infiltrating the aortic wall is part of the immune-inflammatory (TGF-β already mapped) dimension of the Marfan aneurysm."
  - target: 01-human/03-molecular/il-12
    relation: connects-to
    note: "Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the immune-inflammatory dimension of the Marfan aortic-wall disease."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Innate vascular interferon: the type-I interferon, downstream of the cGAS-STING (already mapped) pathway, is part of the innate-immune vascular inflammation of the Marfan aortic aneurysm."
  - target: 01-human/03-molecular/il-5
    relation: connects-to
    note: "Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune milieu of the Marfan aortic wall."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the immune-inflammatory dimension of the Marfan aortic wall degeneration."
  - target: 01-human/03-molecular/ige
    relation: connects-to
    note: "Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the immune milieu of the Marfan aortic wall."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "CD4 helper source: the CD4 T-helper cells of the inflamed aortic wall are the source of the Th1/Th2/Th17 (IFN-γ, IL-4 and IL-17 already mapped) cytokines of the vascular inflammation of Marfan syndrome."
  - target: 01-human/03-molecular/c5ar1
    relation: connects-to
    note: "C5a receptor: the C5aR1 signalling (with the complement C3 already mapped) drives the myeloid recruitment into the inflamed, medial-degenerating aortic wall of Marfan syndrome."
  - target: 01-human/03-molecular/complement-c5
    relation: connects-to
    note: "Terminal complement: the complement C5 and its activation (with C3 already mapped) contribute to the inflammatory injury of the aortic wall of Marfan syndrome."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "Innate infiltrate: the NK cells (perforin pathway) are part of the innate immune infiltrate of the inflamed aortic wall of Marfan syndrome."
---

# Marfan Syndrome

## Overview

**Marfan syndrome (MFS)** is a systemic **connective tissue disorder** caused by autosomal dominant germline mutations in **FBN1** (15q21.1), encoding fibrillin-1 — the principal structural protein of elastic microfibrils in the extracellular matrix. Marfan syndrome was first described by Antoine Marfan in 1896 (a patient named Gabrielle, with arachnodactyly and long limbs); the FBN1 gene was identified as the causative gene by Dietz et al. in 1991 [^dietz-1991-fbn1-marfan]. Marfan syndrome affects approximately **1 in 5,000-10,000** individuals worldwide (~200,000 in the United States), with equal sex distribution and autosomal dominant inheritance; ~25% of cases arise from de novo FBN1 mutations with no family history.

MFS is a **multi-system disorder** defined by cardiovascular, ocular, and skeletal features arising from fibrillin-1 microfibril dysfunction in multiple tissues. The **life-threatening complication** is **aortic root aneurysm** (present in ~70-80% of adults) → aortic dissection (Type A, involving ascending aorta) — the historical primary cause of premature death in Marfan syndrome (median survival ~40-50 years pre-1970). Modern management — beta-blockers, losartan, and prophylactic aortic root replacement — has extended median survival to >70 years. Revised Ghent criteria (Loeys et al. 2010) provide systematic diagnostic criteria integrating aortic measurements, ectopia lentis, FBN1 genotype, and systemic features [^loeys-2010-ghent-criteria].

**Marfan syndrome vs. related heritable thoracic aortic aneurysm syndromes (HTAAS):**

| Syndrome | Gene | Cardiac | Ocular | Skeletal | Distinguishing |
|---|---|---|---|---|---|
| Marfan (MFS) | FBN1 | Aortic root dilation, MVP | Ectopia lentis (~60%) | Tall, arachnodactyly, scoliosis | Fibrillin-1 LOF |
| Loeys-Dietz type 1 (LDS1) | TGFBR1 | Aortic root + branch vessel | Hypertelorism, cleft palate | Severe scoliosis, craniosynostosis | More aggressive aneurysm |
| Loeys-Dietz type 2 (LDS2) | TGFBR2 | Similar to LDS1 | Normal | Similar | Bifid uvula |
| Vascular EDS (vEDS) | COL3A1 | Aortic dissection, arterial rupture | Normal | Normal | No aortic root dilation; rupture |
| MASS phenotype | FBN1 | No aortic dilation | No ectopia lentis | Marfanoid | Subclinical FBN1 mutations |

## Structure

### Genetic basis of Marfan syndrome

**FBN1 mutation spectrum:**
- Over 3,000 distinct FBN1 mutations catalogued; most are unique to individual families (private mutations)
- Missense (~35%), nonsense/frameshift (~25%), splice site (~20%), large rearrangements (~10-15%), in-frame insertions/deletions (~5%)
- **Cysteine substitutions in cbEGF domains**: most common pathogenic missense type; disrupts disulfide bonding → dominant-negative protein misincorporated into microfibrils → most severe phenotype
- **Neonatal Marfan zone (exons 24-32)**: cysteine substitutions in cbEGF domains 14-20 → neonatal Marfan syndrome: severe mitral and tricuspid valve disease at birth, pulmonary emphysema, hyperflexible joints, arachnodactyly; cardiac failure in infancy; poorest prognosis; no significant aortic dilation at birth
- De novo mutations: ~25% of MFS; parents unaffected; recurrence risk low for unaffected parents (<1%); offspring of affected individual = 50% risk

**FBN1-related conditions (allelic to MFS):**
- **Ectopia lentis syndrome**: FBN1 mutations causing isolated lens dislocation without systemic features; may be early/attenuated Marfan; Ghent criteria classify separately
- **MASS phenotype**: myopia, MVP, aortic dilation (borderline), striae, skeletal features — incomplete Marfan phenotype; some FBN1 variants; normal life expectancy
- **Familial thoracic aortic aneurysm**: subset caused by FBN1 mutations with predominantly cardiovascular features; classified separately from MFS

**Molecular pathogenesis:**
- Structural: FBN1 haploinsufficiency → 50% normal microfibril scaffold → mechanically weaker elastic fibers → greater wall stress per cycle → fatigue failure → aneurysm
- Biochemical (TGF-β excess): FBN1 microfibrils tether LTBP1/3 → sequester latent TGF-β in ECM; FBN1 LOF → less TGF-β sequestration → elevated TGF-β activity in aortic media → SMAD2/3 + ERK1/2 → MMP9 overexpression → elastic laminae fragmentation → vascular smooth muscle cell (vSMC) apoptosis → aortic wall weakening
- TGF-β excess confirmed in human MFS aortic tissue: pSMAD2 elevated 2-4x vs. control; correlates with aneurysm severity

## Function

### Cardiovascular manifestations (primary morbidity and mortality)

**Aortic root aneurysm:**
- Dilation of the sinuses of Valsalva (the aortic root); detected by echocardiography
- Present in ~70-80% of adult MFS patients; progressive over time; growth rate ~0.5-1.5 mm/year (varies)
- **Aortic Z-score**: age- and BSA-adjusted measurement; Z-score ≥2 at any aortic site is Ghent criterion A; Z-score ≥3 is highly significant
- Risk of Type A aortic dissection (ascending aorta): rises sharply at root diameter >5.0 cm; catastrophic if untreated; emergent surgical repair mortality ~25-30%; predicted by root diameter + rate of growth
- **Type B dissection** (descending aorta): less common in Marfan; may complicate preexisting aortic dilation or after Type A repair

**Mitral valve disease:**
- MVP (mitral valve prolapse) in ~80% of MFS; fibrillin-1 microfibrils normally support mitral leaflet structure; FBN1 LOF → myxomatous valve changes → leaflet redundancy, chordal elongation
- Mitral regurgitation (MR): mild in most; severe MR requiring repair in ~10-20% of patients over a lifetime; most common cardiac complication requiring intervention in childhood
- Management: echocardiography every 1-2 years; beta-blocker (also slows MR progression and aortic growth)

**Arrhythmias:**
- Atrial fibrillation: elevated risk from mitral regurgitation, aortic dilation; may occur at younger age than general population
- Ventricular arrhythmia: rarely reported; sudden cardiac death very rare in MFS (unlike CPVT, HCM)

### Ocular manifestations

**Ectopia lentis (lens subluxation, ~60% of MFS):**
- Fibrillin-1 is the primary structural protein of ocular zonular fibers (the suspensory ligaments of the lens); FBN1 LOF → zonular weakness → lens subluxation
- Direction: classically superotemporal (upward-outward) in Marfan; contrast with homocystinuria (inferotemporal) and Weill-Marchesani (inferior, microspherophakia)
- Detected by slit-lamp examination (dilation required); present from childhood; may be stable or progressive
- Complications: phacodonesis (tremulous lens), monocular diplopia, high myopia (from axial length increase + refractive error), complete dislocation (zonulysis) → pupillary block → acute glaucoma
- Management: optical correction of myopia/astigmatism; amblyopia treatment in children; surgical lensectomy (pars plana lensectomy/vitrectomy) for severe dislocation or reduced vision; avoid hard contact lens in dislocation

**Myopia:**
- Axial myopia in ~70% of MFS (elongated globe); often severe (−5 to −20 D)
- Increased risk of retinal detachment from high myopia; annual dilated fundus exam essential

**Other ocular features:**
- Flat cornea (cornea plana): flattened corneal curvature → reduced refracting power
- Increased risk of glaucoma (open angle) even without lens subluxation
- Reduced pupil dilation (miosis) from iris hypoplasia

### Skeletal manifestations

**Height and body proportions:**
- Tall stature: mean adult height ~191 cm (males), ~175 cm (females) in classical MFS; usually above 95th percentile
- **Dolichostenomelia** (long, thin limbs): arm span > height by >1.05× ratio; reduced upper/lower segment ratio (<0.85 in adults); measured clinically
- **Arachnodactyly** (long, slender fingers and toes): Walker-Murdoch wrist sign (thumb and little finger overlap when wrapped around contralateral wrist; a sign with ~87% sensitivity); Steinberg thumb sign (thumb extends beyond ulnar border of hand when folded into palm)

**Chest wall deformities:**
- Pectus excavatum (sunken chest, ~50%) or pectus carinatum (prominent sternum, ~15%)
- Pectus excavatum can impair cardiac function if severe (reduced venous return); correctable surgically (Nuss procedure) or cosmetically

**Spinal features:**
- Scoliosis: ~60-70%; often progressive in adolescence; bracing in mild-moderate curves; spinal fusion for severe curves
- Spondylolisthesis (vertebral slippage): L5-S1 most common; pain, radiculopathy
- Dural ectasia: widening of the dural sac in lumbar spine (from dural weakness); present in ~90% of MFS adults; detected by MRI; causes low back pain, neurologic symptoms from nerve root impingement

**Craniofacial features:**
- Dolichocephaly (long, narrow skull), malar hypoplasia, deep-set eyes, high-arched palate, crowded teeth
- Retrognathia (recessed jaw); temporomandibular joint pain

**Foot:**
- Pes planus (flat feet) from ligamentous laxity; hindfoot valgus; custom orthotics

## Pathology

### Diagnosis — Revised Ghent criteria (2010)

**Core criteria:**
- **Aortic root dilation** (Z-score ≥2 or aortic dissection) — major cardiac criterion
- **Ectopia lentis** — major ocular criterion
- **FBN1 pathogenic variant** — genetic criterion
- **Systemic score** ≥7 (scoring: wrist + thumb sign 3; wrist OR thumb sign 1; pectus carinatum 2; pectus excavatum 1; hindfoot deformity 2; pes planus 1; pneumothorax 2; dural ectasia 2; protrusio acetabulae 2; reduced US/LS ratio AND arm span >1.05 × height AND no severe scoliosis 1; scoliosis/thoracolumbar kyphosis 1; reduced elbow extension 1; 3/5 facial features 1; skin striae 1; myopia 1; MVP 1)

**Diagnostic pathways (Ghent 2010):**
1. **Definite MFS in index patient**: aortic root dilation (Z≥2) + ectopia lentis; OR aortic root dilation + FBN1 pathogenic variant; OR aortic root dilation + systemic score ≥7; OR ectopia lentis + FBN1 pathogenic variant (with aortic root dilation known in other family members)
2. **Definite MFS in relative of diagnosed proband**: ectopia lentis; OR aortic root dilation (Z≥2 or dissection); OR systemic score ≥7

**Differential diagnosis:**
- Loeys-Dietz syndrome (TGFBR1/2, SMAD3, TGFB2/3): aortic aneurysm; hypertelorism, bifid uvula, cleft palate; more aggressive vascular disease; TGFBR1/2 sequencing
- Homocystinuria (CBS gene defect): inferior ectopia lentis, Marfanoid body habitus, intellectual disability, thrombosis; plasma homocysteine elevated; AR inheritance; betaine/B6 treatment
- Congenital contractural arachnodactyly (FBN2): arachnodactyly, camptodactyly (flexion contractures), ear crumpling; no aortic dilation; FBN2 mutations
- MASS phenotype (FBN1): borderline aortic measurements; no ectopia lentis; below threshold for MFS diagnosis
- Ehlers-Danlos syndrome hypermobile type (hEDS): joint hypermobility, skin extensibility; no aortic root dilation; COL5A1/2 genes for classical EDS

**Surveillance and management:**
- **Annual echocardiography**: aortic root and ascending aorta measurements; more frequent if root ≥4.5 cm or growing rapidly
- **CT/MRI aorta** (baseline and then every 3-5 years): assess full aorta + branch vessels; at time of aortic dissection, annually post-dissection
- **Beta-blocker (atenolol, propranolol)**: reduce hemodynamic shear stress on aortic root; proven to slow root growth rate; lifelong
- **Losartan (25-100 mg/day)**: AT1R blockade → reduces TGF-β signaling → slows aortic root growth; often combined with beta-blocker; COMPARE trial data support this approach
- **Prophylactic aortic root replacement**:
  - Trigger diameter: ≥5.0 cm (standard); ≥4.5 cm with family history of dissection/rapid growth; ≥4.0 cm if concurrent pregnancy planned or severe AR
  - **David valve-sparing root replacement**: preferred in young patients with competent aortic valve — preserves native valve, avoids anticoagulation; excellent long-term freedom from reoperation (~90% at 10 years)
  - **Bentall procedure** (composite graft + valve): for significant aortic regurgitation or elderly; mechanical valve → lifelong anticoagulation; tissue valve → risk of structural deterioration
- **Avoid isometric exercise and contact sports**: high-impact, breath-holding, or competitive sports increase aortic shear stress → increased dissection risk; swimming, cycling, golf generally permitted; individualize with cardiology
- **MRI rather than CT** where feasible: avoid radiation for serial surveillance (MFS patients require decades of imaging)
- **Pregnancy in Marfan syndrome**: high-risk pregnancy; aortic root ≥4.0 cm → increased dissection risk during labor and postpartum; cesarean delivery recommended for root ≥4.0 cm; losartan discontinued (teratogenic; switch to labetalol); surveillance echocardiography monthly in 3rd trimester + 6 months postpartum
- **Genetic counseling**: AD inheritance; 50% risk per child; prenatal diagnosis available; PGT for couples who wish to avoid transmission
- **Ophthalmology**: annual dilated eye exam; refractive correction; amblyopia treatment in children; glaucoma monitoring; retinal detachment surveillance

## Connections

- `connects-to` → **[FBN1](../../03-molecular/fbn1/README.md)** — Germline FBN1 haploinsufficiency or dominant-negative mutations → Marfan syndrome; FBN1 LOF reduces microfibril scaffold → less TGF-β sequestration → excess TGF-β signaling → SMAD2/3 activation → aortic smooth muscle cell phenotypic switch → progressive aortic root aneurysm.
- `connects-to` → **[TGF-β](../../03-molecular/tgf-beta/README.md)** — FBN1 microfibrils bind LTBP (latent TGF-β binding protein) → sequester TGF-β in ECM; FBN1 LOF → reduced TGF-β sequestration → excess TGF-β → ERK and SMAD2/3 activation in aortic SMCs → MMP production → elastic lamina fragmentation → aneurysm formation.
- `connects-to` → **[SMAD4](../../03-molecular/smad4/README.md)** — FBN1 LOF → excess TGF-β signaling → SMAD2/3 phosphorylation → nuclear translocation → aortic gene expression changes driving aneurysm; SMAD4 is the common SMAD that co-activates SMAD2/3 transcription; SMAD4 mutations in juvenile polyposis syndrome also cause aortic aneurysm.
- `connects-to` → **[Collagen](../../03-molecular/collagen/README.md)** — FBN1 fibrillin-1 microfibrils and collagen fibers are the two major structural components of the arterial wall ECM; fibrillin-1 provides elastic recoil; collagen provides tensile strength; Marfan syndrome (FBN1) and OI (COL1A1/2) both affect connective tissue integrity.
- `connects-to` → **[Angiotensin II](../../03-molecular/angiotensin-ii/README.md)** — losartan (AT1R blocker) reduces angiotensin II → attenuated TGF-β signaling in aortic SMCs → slower aortic root growth in MFS (COMPARE trial); AT1R-TGF-β crosstalk: angiotensin II stimulates TGF-β1 production and SMAD2/3 activation → MMP-mediated ECM degradation in aortic wall.
- `connects-to` → **[Fibronectin](../../03-molecular/fibronectin/README.md)** — fibronectin and fibrillin-1 are both major aortic ECM scaffolding proteins; fibronectin provides SMC adhesion substrate; fibrillin-1 provides elastic recoil; fibronectin deposition increases in Marfan aortic tissue as a compensatory response to fibrillin-1 microfibril failure.
- `connects-to` → **[Hypertension](../hypertension/README.md)** — hypertension management is critical in Marfan syndrome: elevated SBP increases aortic wall shear stress → accelerated root aneurysm growth; beta-blockers (atenolol) reduce HR + BP + aortic pulsatility; losartan provides additional AT1R/TGF-β inhibition; target SBP <120 mmHg.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — The heart and aorta carry Marfan's lethal risk: FBN1 deficiency lets excess TGF-β weaken the aortic media, producing progressive aortic-root dilatation that can dissect or rupture; β-blockers and losartan slow root growth, and prophylactic root replacement at ~5 cm prevents it.
- `connects-to` → **[Eye](../../06-organ/eye/README.md)** — The lens betrays Marfan syndrome: ectopia lentis — upward dislocation of the lens from stretched, failing zonular fibers (made of fibrillin-1) — is a cardinal diagnostic criterion present in ~60%; Marfan eyes are also myopic and prone to retinal detachment and early glaucoma.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — The skeleton makes Marfan visible: tall stature with disproportionately long limbs and fingers (arachnodactyly), arm-span-to-height >1.05, pectus deformity, scoliosis, and joint hypermobility all stem from fibrillin-1's role in connective tissue — scored in the Ghent criteria.
- `connects-to` → **[Cardiovascular system](../cardiovascular-system/README.md)** — The cardiovascular system carries Marfan's lethal risk: fibrillin-1 deficiency weakens the aortic media, so progressive aortic-root dilatation leads to dissection or rupture—the main cause of death—while mitral valve prolapse adds regurgitation; β-blockers/ARBs and surgery help.
- `connects-to` → **[Smooth Muscle Cell](../../04-cellular/smooth-muscle-cell/README.md)** — Marfan is a disease of the aortic smooth-muscle-cell environment: fibrillin-1 loss frees excess TGF-β in the media, so vascular smooth muscle cells lose elastic-fiber anchorage and undergo apoptosis and phenotype switching—weakening the aortic wall toward aneurysm and dissection.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — The lung is an underrecognized Marfan target: weakened connective tissue predisposes to apical blebs and spontaneous pneumothorax (in ~5-10%), and emphysematous changes and restrictive disease from chest-wall deformity (pectus, scoliosis) can further impair breathing.
- `connects-to` → **[Fibroblast](../../04-cellular/fibroblast/README.md)** — Fibroblasts build Marfan's failing scaffold: they secrete fibrillin-1 to assemble microfibrils that lend connective tissue elasticity and sequester TGF-β, so FBN1 mutations leave microfibrils defective—weakening aorta, lens zonules and ligaments and unleashing TGF-β.
- `connects-to` → **[Skin](../../06-organ/skin/README.md)** — The skin shows Marfan's connective-tissue defect: deficient fibrillin-1 microfibrils reduce dermal elasticity, producing striae atrophicae (stretch marks) and sometimes thin, hyperextensible skin—visible clues to a disorder whose real danger lies in the aorta.
- `connects-to` → **[Stroke](../stroke/README.md)** — Marfan syndrome raises stroke risk through vascular fragility: aortic root disease can throw cardioembolic clots, and the same fibrillin-1 weakness predisposes to cervical artery dissection—so an aortic disease can also strike the brain.
- `connects-to` → **[Respiratory system](../respiratory-system/README.md)** — Marfan syndrome weakens the lungs: fibrillin-deficient connective tissue forms apical blebs that rupture, causing spontaneous pneumothorax, and chest-wall deformity restricts breathing—so respiratory complications add to the cardiovascular and skeletal features.
- `connects-to` → **[Osteoblast](../../04-cellular/osteoblast/README.md)** — Marfan's skeletal overgrowth reflects disordered bone formation: excess TGF-beta signaling from fibrillin-1 loss drives long-bone overgrowth, giving tall stature and arachnodactyly—so bone-forming cells build too much skeleton on a faulty connective scaffold.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — Dural ectasia is a hallmark Marfan feature: weakened connective tissue lets the dura around the lower spine balloon out, causing back pain and headaches and serving as a diagnostic criterion—showing Marfan's reach into the nervous system's coverings.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — Marfan syndrome shows in the skin and soft tissue: fibrillin-1 loss weakens connective tissue throughout, producing striae (stretch marks) without weight change, thin skin and hernias—visible signs of the same defect that endangers the aorta.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — Pregnancy is dangerous in Marfan syndrome: the hemodynamic load and hormonal softening of connective tissue sharply raise the risk of aortic dissection, so the reproductive years demand careful cardiac monitoring and counseling in affected women.
- `connects-to` → **[Growth Hormone](../../03-molecular/growth-hormone/README.md)** — Marfan's tall stature is not from growth hormone: unlike pituitary gigantism, the overgrowth comes from defective fibrillin-1 connective tissue, so patients are tall with long limbs and arachnodactyly despite normal growth-hormone levels—a key diagnostic distinction.
- `connects-to` → **[Cardiomyocyte](../../04-cellular/cardiomyocyte/README.md)** — Marfan can weaken heart muscle itself: beyond valve and aortic disease, excess TGF-beta signaling produces an intrinsic cardiomyopathy in which cardiomyocyte dysfunction mildly dilates and weakens the left ventricle, so the heart is monitored even when valves look normal.
- `connects-to` → **[Fibrosis](../../05-tissue/fibrosis/README.md)** — The Marfan aorta fails through medial degeneration: fibrillin loss and unleashed TGF-beta fragment elastic fibers and drive fibrosis in the vessel wall, weakening it until the aortic root dilates and risks dissection—the syndrome's lethal complication.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — Marfan vessels show endothelial dysfunction: the abnormal fibrillin matrix and altered TGF-beta signaling impair the endothelial cells lining the aorta, reducing flow-mediated dilation and adding to the wall stress that drives aneurysm.
- `connects-to` → **[Oxygen](../../02-atomic/oxygen/README.md)** — Marfan's weak connective tissue threatens oxygen supply through pneumothorax: fragile apical lung blebs rupture and collapse the lung, cutting off air exchange—a recurrent emergency in tall, Marfan-bodied patients.
- `connects-to` → **[Mast Cell](../../04-cellular/mast-cell/README.md)** — Mast cells help weaken the Marfan aorta: they infiltrate the aneurysmal aortic wall and release proteases that chew through the elastic media, adding to the matrix breakdown that drives dilation toward dissection.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — Marfan aneurysms are fueled by overactive mTOR: disrupted fibrillin and TGF-β signaling ramp up mTOR in the aortic wall, driving the smooth-muscle changes behind aortic dilation—so rapamycin-class drugs are studied to slow it.
- `connects-to` → **[Brain](../../06-organ/brain/README.md)** — Marfan often enlarges the spinal dura around the brain's continuation: dural ectasia—ballooning of the dural sac—is a common, weakly symptomatic feature that, found on imaging, helps confirm the diagnosis.
- `connects-to` → **[AKT](../../03-molecular/akt/README.md)** — Marfan aortas grow weak partly through AKT signaling: disrupted fibrillin and TGF-beta ramp up AKT alongside mTOR in the vessel wall, driving the smooth-muscle changes behind aneurysm, so this growth axis is studied as a drug target.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — Inflammation via NF-kB worsens the Marfan aorta: the failing elastic wall activates this inflammatory switch, recruiting cells and enzymes that degrade the matrix further, accelerating the dilation toward dissection.
- `connects-to` → **[Nitrogen](../../02-atomic/nitrogen/README.md)** — Marfan lungs can burst air into the chest: weak connective tissue forms apical blebs that rupture, spilling air—mostly nitrogen—into the pleural space as a spontaneous pneumothorax, a recurrent Marfan event.
- `connects-to` → **[Alveolus](../../05-tissue/alveolus/README.md)** — Marfan weakens the alveoli: faulty fibrillin leaves the lung's elastic walls fragile, so emphysematous change and apical blebs form in the air sacs, setting up the collapse-prone lung.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — Marfan can stretch the nerves through dural ectasia: the weakened dura around the spinal cord balloons, compressing nerve roots to cause low back pain, headaches, and leg symptoms, a diagnostic Marfan feature.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Marfan is monitored by imaging: echocardiography and CT/MR angiography photons track the aortic root's slow dilation, the measurement that decides when to operate before it dissects.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Marfan's floppy mitral valve calcifies early: mitral annular calcification is part of the Ghent diagnostic score, adding to the valve prolapse and aortic disease of the connective-tissue disorder.
- `connects-to` → **[PDGF](../../03-molecular/pdgf/README.md)** — Growth-factor signaling beyond TGF-β weakens the Marfan aorta: PDGF among others drives the smooth-muscle changes in the dilating wall, part of the biology that aneurysm treatments target.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy exposes the failing Marfan aorta: defective fibrillin leaves the elastic fibers of the arterial wall fragmented and frayed — cystic medial degeneration — the structural rot that lets the aorta balloon and tear.
- `connects-to` → **[Large Intestine](../../06-organ/large-intestine/README.md)** — Weak connective tissue gives way throughout the body: Marfan brings hernias, diverticula, and rectal prolapse, the lax collagen and elastin of the gut wall and abdominal wall failing under everyday pressure.
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — The kidney's moorings loosen in Marfan: with its supporting connective tissue lax, the kidney can drop out of position (nephroptosis), one of the quieter manifestations of the body-wide tissue weakness.
- `connects-to` → **[Osteoclast](../../04-cellular/osteoclast/README.md)** — Marfan bones grow long but thin: excess TGF-β signaling tilts remodeling toward osteoclast resorption, so despite the overgrowth of the long limbs many patients carry reduced bone density and an osteopenia that belies their tall frame.
- `connects-to` → **[Placenta](../../06-organ/placenta/README.md)** — Pregnancy is the Marfan aorta's danger window: the volume load and hormone-softened vessels needed to perfuse the placenta peak the risk of aortic dissection around delivery, demanding echo monitoring and sometimes pre-pregnancy aortic repair.
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — The floppy Marfan mitral valve flutters the rhythm: mitral valve prolapse is associated with magnesium deficiency, and magnesium repletion can ease the palpitations and arrhythmias these prolapsing valves so often provoke.
- `connects-to` → **[Osteoporosis](../osteoporosis/README.md)** — The long Marfan bones are also thin: despite their height, patients often have reduced bone mineral density and osteopenia, likely tied to the disturbed fibrillin-TGF-beta signaling that governs bone as well as connective tissue.
- `connects-to` → **[Adipocyte](../../04-cellular/adipocyte/README.md)** — Marfan bodies carry little fat: the classic tall, slender build comes with scant subcutaneous adipose and low muscle mass, the lean habitus that — with long limbs and arachnodactyly — helps flag the syndrome on sight.
- `connects-to` → **[Generalized Anxiety Disorder](../generalized-anxiety-disorder/README.md)** — Living with a fragile aorta weighs on the mind: rates of anxiety and depression run high in Marfan, driven by the constant threat of dissection, lifelong activity limits and body-image concerns, so psychological support is part of comprehensive care.
- `connects-to` → **[ERK1/2](../../03-molecular/erk1-2/README.md)** — The damage runs through a side channel: the excess TGF-β freed by fibrillin-1 loss fires the non-canonical ERK1/2 (MAPK) pathway in the aortic wall, a driver of aneurysm growth that losartan helps blunt — explaining why an angiotensin blocker protects the aorta.
- `connects-to` → **[Heart Failure](../heart-failure/README.md)** — The valves can wear the heart out: chronic aortic and mitral regurgitation from Marfan's stretched valve tissue overloads the ventricle for years, so beyond the dissection threat the disease can drift into heart failure if the leaks go uncorrected.
- `connects-to` → **[COPD](../copd/README.md)** — The lung's scaffolding fails diffusely too: beyond the dramatic spontaneous pneumothorax, defective elastin leaves the airspaces prone to emphysema-like destruction and accelerated decline in lung function, a quieter respiratory toll of the connective-tissue defect.
- `connects-to` → **[Nitric Oxide](../../03-molecular/nitric-oxide/README.md)** — The aortic endothelium loses its NO balance: dysregulated endothelial nitric-oxide signaling in Marfan contributes to the stiffening and weakening of the aortic wall, part of the vascular dysfunction behind aneurysm formation.
- `connects-to` → **[Endothelin-1](../../03-molecular/endothelin-1/README.md)** — Vasoactive signaling remodels the wall: raised endothelin-1 promotes smooth-muscle and matrix changes in the Marfan aorta, adding a vasoconstrictor-driven arm to the TGF-β-led remodeling that grows the aneurysm.
- `connects-to` → **[Venous Thromboembolism](../venous-thromboembolism/README.md)** — Major aortic surgery brings clot risk: the prophylactic aortic root and valve operations central to Marfan care carry a perioperative venous thromboembolism risk requiring prophylaxis.
- `connects-to` → **[Connexin-43](../../03-molecular/connexin43/README.md)** — The Marfan heart can beat erratically: gap-junction remodeling and a primary myopathy predispose to ventricular arrhythmia and sudden cardiac death, a risk in Marfan beyond the aortic and valve disease.
- `connects-to` → **[Troponin complex](../../03-molecular/troponin-complex/README.md)** — The heart muscle itself is affected: Marfan can cause a primary cardiomyopathy independent of valve and aortic disease, with subclinical myocardial dysfunction reflected in troponin and impaired contractility.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — Living with a life-threatening syndrome weighs on the mind: the activity restrictions, body-image concerns and fear of aortic dissection in Marfan drive elevated rates of depression alongside its anxiety.
- `connects-to` → **[Sepsis](../sepsis/README.md)** — Abnormal valves and aortic grafts invite infection: Marfan's mitral and aortic valve disease predisposes to infective endocarditis, and prosthetic aortic grafts can become infected, both able to seed sepsis.
- `connects-to` → **[Chronic Kidney Disease](../ckd/README.md)** — Aortic dissection can starve the kidneys: a dissection extending to the renal arteries causes renal malperfusion and infarction, and the perioperative injury of major aortic surgery can leave chronic kidney impairment.
- `connects-to` → **[Pulmonary Arterial Hypertension](../pulmonary-arterial-hypertension/README.md)** — Chest deformity and lung disease strain the right heart: severe scoliosis, pectus deformity and apical bullae in Marfan restrict the lungs and, with chronic hypoxia, can raise pulmonary pressures toward cor pulmonale.
- `connects-to` → **[Wound Healing](../wound-healing/README.md)** — Faulty connective tissue heals poorly: the fibrillin defect of Marfan weakens the matrix that wounds rebuild, so surgical incisions — including major aortic operations — and skin are prone to poor healing and hernia.
- `connects-to` → **[Neuropathic Pain](../neuropathic-pain/README.md)** — Dural ectasia presses on the nerves: the ballooning of the dural sac, a characteristic Marfan feature, stretches lumbosacral nerve roots and causes chronic low back and radicular neuropathic pain.
- `connects-to` → **[Insomnia Disorder](../insomnia-disorder/README.md)** — Its craniofacial build disturbs sleep: the high-arched palate and retrognathia of Marfan predispose to obstructive sleep apnea, fragmenting sleep and worsening daytime function and cardiovascular strain.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — Weak connective tissue herniates and tears: Marfan brings recurrent inguinal and incisional hernias, and an aortic dissection that extends to the mesenteric arteries can starve the bowel of blood.
- `connects-to` → **[Renal System](../renal-system/README.md)** — Aortic dissection threatens the kidneys: a dissection extending along the aorta can occlude a renal artery, causing renal malperfusion and acute kidney injury, a feared complication in Marfan.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — Its protective therapy works through a hormone axis: losartan and other ARBs used to slow aortic growth in Marfan block the angiotensin II of the renin-angiotensin endocrine system, dampening TGF-β signalling.
- `connects-to` → **[Immune System](../immune-system/README.md)** — Its defect unleashes a regulatory cytokine: fibrillin-1 normally sequesters TGF-β in the matrix, so its deficiency releases excess TGF-β — a key immunoregulatory growth factor — that drives the tissue weakening of Marfan.
- `connects-to` → **[Staphylococcus aureus](../../../02-pathogen/02-bacteria/staphylococcus-aureus/README.md)** — Its valves and grafts invite infection: damaged valves and prosthetic aortic grafts after surgery raise the risk of infective endocarditis, classically from Staphylococcus aureus and viridans streptococci.
- `connects-to` → **[Beta-Blockers](../../../03-medicine/01-modern/04-cardio/beta-blockers/README.md)** — Beta-blockers protect its aorta: by lowering heart rate and the force of ejection, beta-blockers reduce aortic wall stress and slow aneurysm growth, a mainstay of Marfan management alongside ARBs.
- `connects-to` → **[ARBs](../../../03-medicine/01-modern/04-cardio/arbs/README.md)** — They blunt the underlying signal: angiotensin-receptor blockers like losartan reduce the excess TGF-β signalling that drives aortic-root dilation in Marfan syndrome, slowing its enlargement.
- `connects-to` → **[Warfarin](../../../03-medicine/01-modern/09-hematology/warfarin/README.md)** — A mechanical valve needs lifelong anticoagulation: after aortic-root replacement with a mechanical valve for Marfan syndrome, warfarin prevents valve thrombosis and embolic stroke.
- `connects-to` → **[Aspirin](../../../03-medicine/01-modern/04-cardio/aspirin/README.md)** — Bioprosthetic repairs take antiplatelet cover: patients with a tissue aortic valve or vascular stent for Marfan-related disease use aspirin, a lighter alternative to the warfarin that mechanical valves require.
- `connects-to` → **[Arterial Wall](../../05-tissue/arterial-wall/README.md)** — It weakens the aorta's wall: loss of fibrillin microfibrils and excess TGF-β cause cystic medial degeneration of the aortic wall, driving the progressive aortic-root aneurysm and dissection that are Marfan's lethal hallmark.
- `connects-to` → **[Calcium-Channel Blockers](../../../03-medicine/01-modern/04-cardio/calcium-channel-blockers/README.md)** — A drug class to avoid: unlike beta-blockers and ARBs, calcium-channel blockers are associated with faster aortic growth and worse outcomes in Marfan syndrome and are generally avoided.
- `connects-to` → **[Cortical Bone](../../05-tissue/cortical-bone/README.md)** — It overgrows and thins the skeleton: fibrillin loss lengthens the long bones (arachnodactyly, tall stature) while reducing cortical bone density, contributing to scoliosis and chest-wall deformity.
- `connects-to` → **[Endocardium](../../05-tissue/endocardium/README.md)** — It loosens the heart valves: fibrillin-1 loss and excess TGF-β weaken the valve leaflets, producing the myxomatous mitral valve prolapse and aortic regurgitation that, with aortic root dilatation, define Marfan's cardiac disease.
- `connects-to` → **[Cardiac Conduction System](../../05-tissue/cardiac-conduction-system/README.md)** — Beyond the aorta, an electrical risk: Marfan syndrome carries ventricular arrhythmias and a small risk of sudden cardiac death independent of valve and aortic disease, linked to conduction abnormalities and fibrillin-related myocardial changes.
- `connects-to` → **[Juvenile Polyposis Syndrome](../juvenile-polyposis-syndrome/README.md)** — Opposite ends of one signalling axis: Marfan stems from FBN1 loss that unleashes excess TGF-β, while SMAD4-type juvenile polyposis loses the TGF-β/BMP transducer itself—two diseases dysregulating the same pathway from opposite directions.
- `connects-to` → **[Myocardium](../../05-tissue/myocardium/README.md)** — Primary Marfan cardiomyopathy: beyond valve and aortic disease, FBN1 loss causes an intrinsic dilated cardiomyopathy of the myocardium, a less-recognised cause of heart failure in Marfan syndrome.
- `connects-to` → **[Peripheral Nerve](../../05-tissue/peripheral-nerve/README.md)** — Dural ectasia: the enlarging dural sac of Marfan erodes vertebrae and stretches nerve roots, causing low-back and radicular pain and headaches—a major diagnostic criterion.
- `connects-to` → **[Systemic Sclerosis](../systemic-sclerosis/README.md)** — Two connective-tissue disorders via TGF-β: Marfan's fibrillin loss unleashes excess TGF-β signalling, while systemic sclerosis is autoimmune TGF-β-driven fibrosis—structural versus inflammatory routes to matrix dysregulation.
- `connects-to` → **[Atherosclerosis](../atherosclerosis/README.md)** — Two roads to an aortic aneurysm: Marfan's fibrillin-1 loss causes cystic medial degeneration of the young aorta, distinct from the lipid-driven atherosclerotic aneurysm of older age—same catastrophic endpoint, different wall pathology.
- `connects-to` → **[BNP](../../03-molecular/bnp/README.md)** — Volume-loading the heart: chronic aortic and mitral regurgitation in Marfan stretches the ventricle, raising BNP as a marker of the heart failure that valve and aortic-root disease eventually cause.
- `connects-to` → **[IGF-1](../../03-molecular/igf-1/README.md)** — The overgrowth axis: the tall stature and arachnodactyly of Marfan reflect dysregulated TGF-β interacting with GH/IGF-1 growth signalling, driving the excessive long-bone growth characteristic of the syndrome.
- `connects-to` → **[Caspase-3](../../03-molecular/caspase-3/README.md)** — Medial degeneration: apoptosis of aortic smooth-muscle cells via caspase-3 thins and weakens the aortic media in Marfan, a core mechanism behind aneurysm and dissection.
- `connects-to` → **[T Cytotoxic Cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Wall inflammation: cytotoxic T cells infiltrate the degenerating aortic wall in Marfan and other aneurysmal aortopathies, contributing to medial breakdown.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — Adventitial neovessels: VEGF-driven vasa-vasorum proliferation accompanies the medial degeneration of the Marfan aorta, a feature of the remodelling aneurysmal wall.
- `connects-to` → **[CCL2](../../03-molecular/ccl2/README.md)** — Macrophage recruitment: CCL2 draws macrophages into the degenerating Marfan aortic wall, where their proteases accelerate the medial breakdown that drives aneurysm.
- `connects-to` → **[IL-6](../../03-molecular/il-6/README.md)** — Aortic inflammation: IL-6 within the Marfan aortic wall amplifies the inflammatory remodelling that weakens the media and predicts aneurysm progression.
- `connects-to` → **[TNF-α](../../03-molecular/tnf-alpha/README.md)** — Inflammatory medial breakdown: TNF-α contributes to the smooth-muscle apoptosis and matrix degradation of the Marfan aorta, compounding the primary fibrillin defect.
- `connects-to` → **[Aldosterone](../../03-molecular/aldosterone/README.md)** — Mineralocorticoid remodelling: aldosterone and mineralocorticoid-receptor signalling promote aortic fibrosis and stiffening, and MR antagonists are studied alongside ARBs to slow aortic dilatation in Marfan syndrome.
- `connects-to` → **[RANKL](../../03-molecular/rankl/README.md)** — Reduced bone density: Marfan syndrome is associated with low bone mineral density, with RANKL-driven osteoclast activity contributing to the osteopenia that adds to its skeletal manifestations.
- `connects-to` → **[Adrenomedullin](../../03-molecular/adrenomedullin/README.md)** — Vascular peptide: adrenomedullin, a fibrillin-associated vasodilator peptide, is dysregulated in Marfan syndrome, contributing to the abnormal vascular tone and wall homeostasis of the dilating aorta.
- `connects-to` → **[β1-adrenergic receptor](../../03-molecular/beta1-adrenergic-receptor/README.md)** — Beta-blockers acting on β1-adrenergic receptors lower heart rate and the rate of aortic-pressure rise (dP/dt), reducing wall stress to slow aortic-root dilation—the longstanding mainstay of aortic protection in Marfan syndrome.
- `connects-to` → **[Estrogen](../../03-molecular/estrogen/README.md)** — Pregnancy markedly raises the risk of aortic dissection in Marfan syndrome through combined hemodynamic and hormonal effects on the already weakened aortic wall, demanding intensive cardiac surveillance through gestation.
- `connects-to` → **[IL-1β](../../03-molecular/il-1b/README.md)** — IL-1β and inflammatory signaling contribute to the medial degeneration and matrix breakdown of the Marfan aorta, an inflammatory arm of aneurysm formation layered on the excess TGF-β signaling that fibrillin loss unleashes.
- `connects-to` → **[Periostin](../../03-molecular/periostin/README.md)** — Periostin is upregulated in the Marfan aortic wall, where this matricellular protein participates in the maladaptive medial remodeling and matrix disorganization that weaken the aorta and predispose it to aneurysm and dissection.
- `connects-to` → **[Galectin-3](../../03-molecular/galectin-3/README.md)** — Galectin-3 promotes the inflammation and fibrosis of the degenerating Marfan aortic media, a profibrotic lectin studied as a biomarker of aortic-wall disease and risk of aneurysm progression.
- `connects-to` → **[Renin](../../03-molecular/renin/README.md)** — Angiotensin signaling downstream of renin amplifies aortic TGF-β activity, the rationale for the angiotensin-receptor blocker losartan, which slows aortic-root dilatation in Marfan beyond simple blood-pressure lowering.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — Dysregulated TGF-β and IGF-1 signaling (both mapped) engages PI3K-AKT-mTOR (AKT and mTOR already mapped), driving the smooth-muscle-cell changes of the Marfan aortic wall and a candidate target in aneurysm.
- `connects-to` → **[IL-17A](../../03-molecular/il-17a/README.md)** — A Th17/IL-17 inflammatory infiltrate in the aortic media contributes to the wall remodeling and progression of aneurysm in Marfan syndrome.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Complement activation generating C3 fragments amplifies the inflammatory injury of the Marfan aortic media, adding to the matrix breakdown that predisposes to dissection.
- `connects-to` → **[KRAS](../../03-molecular/kras/README.md)** — Non-canonical TGF-β signaling activates RAS-ERK (ERK1/2 already mapped), a driver of the aortic-wall degeneration in Marfan syndrome that complements the canonical SMAD pathway.
- `connects-to` → **[NRF2](../../03-molecular/nfe2l2/README.md)** — NRF2 antioxidant defense counters the oxidative stress accompanying the smooth-muscle-cell dysfunction and matrix breakdown of the Marfan aorta.
- `connects-to` → **[MYD88](../../03-molecular/myd88/README.md)** — Macrophage TLR-MyD88-NF-κB signaling (NF-κB already mapped) contributes the inflammatory component of aortic-wall remodeling and aneurysm progression in Marfan syndrome.
- `connects-to` → **[JAK1/2](../../03-molecular/jak1-2/README.md)** — IL-6-JAK-STAT signaling (IL-6 mapped) contributes to the medial inflammation accompanying aortic-wall degeneration in Marfan syndrome.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — STAT3-driven inflammatory signaling participates in the vascular-smooth-muscle and inflammatory response of the Marfan aortopathy.
- `connects-to` → **[PTEN](../../03-molecular/pten/README.md)** — PTEN regulation of PI3K-AKT-mTOR signaling (AKT, PIK3CA and mTOR mapped) modulates the vascular-smooth-muscle phenotype in the aortic wall affected by Marfan syndrome.
- `connects-to` → **[cGAS-STING](../../03-molecular/cgas-sting/README.md)** — Cytosolic DNA sensing through cGAS-STING contributes to the vascular-wall inflammation that accompanies the aortic aneurysm progression of Marfan syndrome.
- `connects-to` → **[STAT1](../../03-molecular/stat1/README.md)** — IFN-STAT1 signaling shapes the immune-cell infiltration of the aortic wall in the aneurysmal disease of Marfan syndrome.
- `connects-to` → **[FOXO](../../03-molecular/foxo/README.md)** — FOXO transcription factors regulate the oxidative-stress resistance and contractile phenotype of the aortic smooth-muscle cells weakened in Marfan syndrome.
- `connects-to` → **[GSK-3β](../../03-molecular/gsk-3b/README.md)** — GSK-3β participates in the vascular smooth-muscle signaling and TGF-β crosstalk relevant to the aortic remodeling of Marfan syndrome.
- `connects-to` → **[HIF-1alpha](../../03-molecular/hif-1alpha/README.md)** — HIF-1α in the mechanically stressed aortic wall contributes to the vascular remodeling and matrix dysregulation of Marfan syndrome.
- `connects-to` → **[S100A8/A9](../../03-molecular/s100a8-a9/README.md)** — S100A8/A9 alarmins reflect the inflammatory component of the aortic-wall remodeling in Marfan syndrome.
- `connects-to` → **[AMPK](../../03-molecular/ampk/README.md)** — AMPK-linked metabolic and mechanotransduction signaling participates in the vascular smooth-muscle homeostasis disrupted in the aortic wall of Marfan syndrome.
- `connects-to` → **[Autophagy](../../03-molecular/autophagy/README.md)** — Autophagy modulates the vascular smooth-muscle-cell survival and phenotypic switching in the aortic aneurysm of Marfan syndrome.
- `connects-to` → **[SRC Kinase](../../03-molecular/src-kinase/README.md)** — SRC-family kinase signaling downstream of angiotensin-II and TGF-β receptors (both already mapped) contributes to the aortic-wall remodeling of Marfan syndrome.
- `connects-to` → **[CCR5](../../03-molecular/ccr5/README.md)** — CCR5-driven leukocyte recruitment into the aortic wall contributes to the inflammatory component of the aortopathy of Marfan syndrome.
- `connects-to` → **[DNMT3A](../../03-molecular/dnmt3a/README.md)** — DNMT3A-mediated DNA methylation participates in the epigenetic regulation of the vascular-smooth-muscle-cell phenotype in Marfan syndrome.
- `connects-to` → **[NOTCH](../../03-molecular/notch/README.md)** — NOTCH signaling participates in the vascular-smooth-muscle-cell differentiation and aortic-wall homeostasis dysregulated in Marfan syndrome.
- `connects-to` → **[CXCL12](../../03-molecular/cxcl12/README.md)** — CXCL12-CXCR4 signaling participates in the vascular smooth-muscle-cell and endothelial responses of the aortopathy of Marfan syndrome.
- `connects-to` → **[ARID1A](../../03-molecular/arid1a/README.md)** — ARID1A-containing SWI/SNF chromatin remodeling participates in the epigenetic regulation of the connective-tissue gene programs relevant to Marfan syndrome.
- `connects-to` → **[IL-33](../../03-molecular/il-33/README.md)** — IL-33 alarmin signaling participates in the vascular inflammation relevant to the aortopathy of Marfan syndrome.
- `connects-to` → **[Calcineurin](../../03-molecular/calcineurin/README.md)** — Calcineurin-NFAT signaling participates in the cardiovascular-smooth-muscle and immune responses relevant to Marfan syndrome.
- `connects-to` → **[Adenosine](../../03-molecular/adenosine/README.md)** — Adenosine signaling participates in the vascular-tone regulation relevant to the aortopathy of Marfan syndrome.
- `connects-to` → **[Osteopontin](../../03-molecular/osteopontin/README.md)** — Osteopontin participates in the aortic extracellular-matrix remodeling and aneurysm pathology of Marfan syndrome.
- `connects-to` → **[Xanthine oxidase](../../03-molecular/xanthine-oxidase/README.md)** — Oxidative aortic degeneration: oxidative stress in the Marfan aortic wall, to which xanthine oxidase contributes, activates matrix metalloproteinases and promotes the smooth-muscle (already mapped) loss and elastic-fibre fragmentation that drive aneurysm formation.
- `connects-to` → **[Insulin receptor](../../03-molecular/insulin-receptor/README.md)** — Growth axis: the tall stature and long limbs of Marfan syndrome reflect the growth-hormone/IGF-1 axis (both already mapped) signalling through the insulin/IGF receptors, and modulating this overgrowth has been explored to limit skeletal disproportion.
- `connects-to` → **[Progesterone](../../03-molecular/progesterone/README.md)** — Pregnancy aortic risk: pregnancy sharply raises the risk of aortic dissection in Marfan syndrome, as the haemodynamic load and the hormonal effects of progesterone and estrogen (already mapped) on the vessel wall weaken the already-fragile aorta.
- `connects-to` → **[Von Willebrand factor](../../03-molecular/von-willebrand-factor/README.md)** — Endothelial dysfunction: the abnormal aortic wall of Marfan syndrome disturbs the endothelium (nitric oxide already mapped), raising von Willebrand factor, a marker of the endothelial activation that accompanies the aortopathy and its thrombotic risk during dissection.
- `connects-to` → **[Prostaglandins](../../03-molecular/prostaglandins/README.md)** — Vascular eicosanoids: prostaglandins modulate the tone and inflammation of the aortic wall, contributing with the cytokines already mapped to the vascular remodelling that, driven by dysregulated TGF-beta (already mapped), weakens the Marfan aorta.
- `connects-to` → **[IL-10](../../03-molecular/il-10/README.md)** — Inflammatory balance: the anti-inflammatory IL-10 counters the TNF, IL-6 and IL-1 (already mapped) infiltrating the dilating aortic wall, and this cytokine balance shapes the inflammatory component of the aneurysm formation in Marfan syndrome.
- `connects-to` → **[Serotonin](../../03-molecular/serotonin/README.md)** — Myxomatous valve degeneration: serotonergic signalling, interacting with the dysregulated TGF-beta (already mapped), contributes to the myxomatous mitral-valve degeneration and prolapse that accompanies the aortic disease of Marfan syndrome.
- `connects-to` → **[IL-13](../../03-molecular/il-13/README.md)** — Fibrotic remodelling: IL-13, a profibrotic cytokine acting through TGF-beta (already mapped), contributes to the fibrotic remodelling of the aortic wall, part of the connective-tissue dysregulation of Marfan syndrome.
- `connects-to` → **[Copper](../../02-atomic/copper/README.md)** — Lysyl-oxidase crosslinking: copper is the cofactor for lysyl oxidase, the enzyme that crosslinks collagen and elastin (collagen already mapped) into strong fibres, so this metal is essential to the connective-tissue integrity deranged in Marfan syndrome.
- `connects-to` → **[Zinc](../../02-atomic/zinc/README.md)** — Matrix metalloproteinases: zinc is the cofactor of the matrix metalloproteinases that degrade the elastin and collagen (already mapped) of the aortic media, the MMP activity contributing to the aneurysm and dissection of Marfan syndrome.
- `connects-to` → **[IL-4](../../03-molecular/il-4/README.md)** — Pro-fibrotic type-2: IL-4, with IL-13 (already mapped), drives the type-2/pro-fibrotic (TGF-β already mapped) programme in the remodelling of the aortic wall of Marfan syndrome.
- `connects-to` → **[Histamine](../../03-molecular/histamine/README.md)** — Mast-cell aortopathy: mast cells accumulate in the aneurysmal aortic wall of Marfan syndrome, releasing histamine and proteases that contribute, with the matrix metalloproteinases, to the medial degeneration.
- `connects-to` → **[Zinc](../../02-atomic/zinc/README.md)** — Matrix metalloproteinases: the zinc-dependent matrix metalloproteinases degrade the elastin and collagen (already mapped) of the aortic media, contributing, with the fibrillin (FBN1 already mapped) defect, to the aneurysm of Marfan syndrome.
- `connects-to` → **[Leptin](../../03-molecular/leptin/README.md)** — Lean-habitus adipokine: leptin reflects the reduced fat mass and the metabolic profile of the tall, thin (dolichostenomelia) habitus of Marfan syndrome.
- `connects-to` → **[Adiponectin](../../03-molecular/adiponectin/README.md)** — Body-composition adipokine: adiponectin, with leptin (already mapped), is part of the adipokine profile of the altered body composition and metabolism of Marfan syndrome.
- `connects-to` → **[Resistin](../../03-molecular/resistin/README.md)** — Body-composition adipokine: resistin, with leptin and adiponectin (already mapped), completes the adipokine profile of the altered body composition and metabolism of Marfan syndrome.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Aortic-wall macrophages: the macrophage infiltration and the inflammation (CCL2 and IL-6 already mapped) of the aortic media contribute to the aneurysm progression of Marfan syndrome.
- `connects-to` → **[IFN-gamma](../../03-molecular/ifn-gamma/README.md)** — Aortic Th1 inflammation: the IFN-γ of the T cells infiltrating the aortic wall is part of the immune-inflammatory (TGF-β already mapped) dimension of the Marfan aneurysm.
- `connects-to` → **[IL-12](../../03-molecular/il-12/README.md)** — Th1 polarisation: IL-12 polarises the Th1 (IFN-γ already mapped) arm of the immune-inflammatory dimension of the Marfan aortic-wall disease.
- `connects-to` → **[Type I interferon](../../03-molecular/type-i-interferon/README.md)** — Innate vascular interferon: the type-I interferon, downstream of the cGAS-STING (already mapped) pathway, is part of the innate-immune vascular inflammation of the Marfan aortic aneurysm.
- `connects-to` → **[IL-5](../../03-molecular/il-5/README.md)** — Type-2 arm: IL-5, with the type-2 cytokines (IL-4 and IL-13 already mapped), is the eosinophil/Th2 dimension of the immune milieu of the Marfan aortic wall.
- `connects-to` → **[IL-23](../../03-molecular/il-23/README.md)** — Th17 axis: IL-23 sustains the Th17 (IL-17 already mapped) arm of the immune-inflammatory dimension of the Marfan aortic wall degeneration.
- `connects-to` → **[IgE](../../03-molecular/ige/README.md)** — Type-2 arm: IgE, with the type-2 cytokines (IL-4 and IL-13 already mapped), reflects the type-2 immune dimension of the immune milieu of the Marfan aortic wall.
- `connects-to` → **[T-helper cell](../../04-cellular/t-helper-cell/README.md)** — CD4 helper source: the CD4 T-helper cells of the inflamed aortic wall are the source of the Th1/Th2/Th17 (IFN-γ, IL-4 and IL-17 already mapped) cytokines of the vascular inflammation of Marfan syndrome.
- `connects-to` → **[C5aR1](../../03-molecular/c5ar1/README.md)** — C5a receptor: the C5aR1 signalling (with the complement C3 already mapped) drives the myeloid recruitment into the inflamed, medial-degenerating aortic wall of Marfan syndrome.
- `connects-to` → **[Complement C5](../../03-molecular/complement-c5/README.md)** — Terminal complement: the complement C5 and its activation (with C3 already mapped) contribute to the inflammatory injury of the aortic wall of Marfan syndrome.
- `connects-to` → **[Natural killer cell](../../04-cellular/natural-killer-cell/README.md)** — Innate infiltrate: the NK cells (perforin pathway) are part of the innate immune infiltrate of the inflamed aortic wall of Marfan syndrome.

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^dietz-1991-fbn1-marfan]: Dietz HC, Cutting GR, Pyeritz RE, et al. Marfan syndrome caused by a recurrent de novo missense mutation in the fibrillin gene. *Nature.* 1991;352(6333):337-339. [doi:10.1038/352337a0](https://doi.org/10.1038/352337a0) · [PubMed 1852208](https://pubmed.ncbi.nlm.nih.gov/1852208/)
[^loeys-2010-ghent-criteria]: Loeys BL, Dietz HC, Braverman AC, et al. The revised Ghent nosology for the Marfan syndrome. *J Med Genet.* 2010;47(7):476-485. [doi:10.1136/jmg.2009.072785](https://doi.org/10.1136/jmg.2009.072785) · [PubMed 20591885](https://pubmed.ncbi.nlm.nih.gov/20591885/)
