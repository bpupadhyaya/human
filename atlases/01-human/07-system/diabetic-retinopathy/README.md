---
schema: human-scale-entry/v1
id: diabetic-retinopathy
name: Diabetic Retinopathy
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-07
summary: "Diabetic retinopathy (DR) is the leading cause of blindness in working-age adults; hyperglycemia → pericyte loss → microaneurysms → neovascularization (PDR) → vitreous hemorrhage. VEGF + Ang-2 drive macular edema; anti-VEGF and faricimab are the treatment standard."
aliases: ["DR", "diabetic eye disease", "non-proliferative DR", "NPDR", "proliferative DR", "PDR", "diabetic macular edema", "DME", "center-involving DME"]
sources:
  - id: fong-2004-dr-review
    type: peer-reviewed
    cite: "Fong DS, Aiello L, Gardner TW, et al. Diabetic retinopathy. Diabetes Care. 2004;27(10):2540-2553."
    doi: "10.2337/diacare.27.10.2540"
    pmid: "15451934"
    url: "https://doi.org/10.2337/diacare.27.10.2540"
  - id: brown-2015-aflibercept-protocol-t
    type: peer-reviewed
    cite: "Diabetic Retinopathy Clinical Research Network; Wells JA, Glassman AR, Ayala AR, et al. Aflibercept, Bevacizumab, or Ranibizumab for Diabetic Macular Edema. N Engl J Med. 2015;372(13):1193-1203."
    doi: "10.1056/NEJMoa1414264"
    pmid: "25692915"
    url: "https://doi.org/10.1056/NEJMoa1414264"
  - id: wykoff-2022-faricimab-dr
    type: peer-reviewed
    cite: "Wykoff CC, Abreu F, Adamis AP, et al. Efficacy, durability, and safety of intravitreal faricimab with extended dosing up to every 16 weeks in patients with diabetic macular oedema (YOSEMITE and RHINE). Lancet. 2022;399(10326):741-755."
    doi: "10.1016/S0140-6736(22)00018-6"
    pmid: "35085503"
    url: "https://doi.org/10.1016/S0140-6736(22)00018-6"
cross_links:
  - target: 01-human/03-molecular/angiopoietin
    relation: connects-to
    note: "Ang-2 elevated in diabetic retinas → Tie2 destabilization → pericyte loss → endothelial junction opening → macular edema + neovascularization; faricimab (anti-Ang-2 + anti-VEGF-A) achieves Q16W dosing with non-inferior VA gains vs. aflibercept Q8W (YOSEMITE/RHINE)."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "VEGF-A drives DME and PDR neovascularization; hypoxic retina → HIF-1α → VEGF → VEGFR-2 → endothelial proliferation and barrier disruption; anti-VEGF (ranibizumab, aflibercept, bevacizumab) is the first-line treatment for center-involving DME and PDR."
  - target: 01-human/07-system/hypertension
    relation: connects-to
    note: "Hypertension accelerates DR through retinal arteriolar pressure, shear stress, and RAAS activation; BP control to <130/80 mmHg reduces DR progression by ~30% (UKPDS); hypertensive retinopathy and DR frequently coexist and share pathophysiology."
  - target: 01-human/06-organ/eye
    relation: targets
    note: "Diabetic retinopathy targets the retina: pericyte loss → microaneurysms → exudates → macular edema → neovascularization → vitreous hemorrhage → tractional retinal detachment; the retina is the primary organ affected, with foveal photoreceptors most critical for central vision."
  - target: 01-human/07-system/wound-healing
    relation: connects-to
    note: "Diabetes impairs wound healing through AGE accumulation, pericyte dysfunction, impaired neutrophil function, and reduced HIF-1α/VEGF response; diabetic foot ulcers affect ~15% of people with diabetes and are the leading cause of non-traumatic amputation."
  - target: 01-human/07-system/type-1-diabetes
    relation: connects-to
    note: "Diabetic retinopathy is the leading microvascular complication of type 1 diabetes, present in nearly all patients after 20 years; the DCCT proved that intensive glycemic control reduces retinopathy onset by 76% and progression by 54%, so screening begins 5 years after diagnosis."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "Diabetic retinopathy is fundamentally a failure of retinal vascular endothelial cells: hyperglycemia and pericyte dropout disrupt their inner blood-retinal-barrier tight junctions → leak and macular edema, then hypoxia drives them to proliferate into the vitreous."
  - target: 01-human/03-molecular/hif-1alpha
    relation: connects-to
    note: "As diabetic capillary closure starves the retina of oxygen, HIF-1α stabilizes and transcribes VEGF (and EPO, Ang-2), triggering the neovascularization of proliferative DR; panretinal photocoagulation works by ablating ischemic retina to lower this HIF-driven VEGF output."
  - target: 01-human/07-system/type-2-diabetes
    relation: connects-to
    note: "Although classically tied to type 1, most diabetic retinopathy occurs in type 2 diabetes because T2D is far more prevalent; many T2D patients already have retinopathy at diagnosis after years of silent hyperglycemia, so screening begins at T2D diagnosis (vs 5 years in T1D)."
  - target: 01-human/07-system/ckd
    relation: connects-to
    note: "Diabetic retinopathy and diabetic kidney disease are parallel microvascular complications: both stem from hyperglycemic endothelial injury, retinopathy strongly predicts nephropathy, and its presence supports a diabetic etiology when a diabetic patient develops proteinuric CKD."
  - target: 01-human/07-system/neuropathic-pain
    relation: connects-to
    note: "Retinopathy, nephropathy and neuropathy form the diabetic microvascular triad: the same hyperglycemic, polyol- and AGE-mediated microvascular damage that injures the retina also damages peripheral nerves → painful diabetic neuropathy; glycemic control reduces all three together."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Laser photons treat diabetic retinopathy: pan-retinal photocoagulation burns ischemic peripheral retina to suppress VEGF and halt neovascularization, while focal laser seals leaking microaneurysms—an older mainstay now complemented by anti-VEGF injections."
  - target: 01-human/07-system/atherosclerosis
    relation: connects-to
    note: "Diabetic retinopathy is the microvascular mirror of atherosclerosis's macrovascular disease: the same hyperglycemia, dyslipidemia, and hypertension that clog large arteries damage retinal capillaries, so retinopathy on fundoscopy flags systemic vascular risk."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "Diabetic retinopathy is now seen as a neurovascular disease, not purely vascular: retinal neurons and glia are injured early—before visible microaneurysms—as hyperglycemia disrupts neuronal metabolism, so subtle vision loss can precede vascular lesions."
  - target: 01-human/03-molecular/rage
    relation: connects-to
    note: "Advanced glycation end products and their receptor RAGE drive diabetic retinopathy: chronic hyperglycemia glycates proteins that bind RAGE on retinal vessels, triggering inflammation and pericyte loss—a core mechanism translating high glucose into microvascular damage."
  - target: 01-human/07-system/obesity
    relation: connects-to
    note: "Obesity feeds diabetic retinopathy through type 2 diabetes: the insulin resistance and hyperglycemia of obesity-driven diabetes damage retinal microvessels over years, so the obesity epidemic expands the population at risk for the leading cause of working-age blindness."
  - target: 01-human/07-system/sickle-cell-disease
    relation: connects-to
    note: "Diabetic retinopathy and sickle cell retinopathy are both proliferative retinopathies: both occlude retinal capillaries—by hyperglycemic microangiopathy versus sickled-cell vaso-occlusion—driving VEGF-fueled neovascularization that can bleed and detach the retina."
  - target: 01-human/02-atomic/oxygen
    relation: connects-to
    note: "Retinal ischemia drives proliferative diabetic retinopathy: capillary damage starves the retina of oxygen, so the hypoxic tissue pours out VEGF that grows fragile new vessels which bleed and detach the retina—why anti-VEGF injections and laser are the mainstay."
  - target: 01-human/03-molecular/insulin
    relation: connects-to
    note: "Glycemic control is the key lever against diabetic retinopathy: chronic high glucose damages retinal microvessels, so insulin and other glucose-lowering therapy slow progression—though rapid correction can transiently worsen it, demanding careful monitoring."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "Diabetic retinopathy and nephropathy are paired microvascular complications: the same chronic hyperglycemia that damages retinal capillaries injures the glomerulus, so retinopathy often signals coexisting kidney disease—a shared small-vessel toll of diabetes."
  - target: 01-human/04-cellular/platelet
    relation: connects-to
    note: "Platelets help close off the diabetic retina: hyperglycemia makes them stickier, so microthrombi plug retinal capillaries and create the non-perfused, ischemic patches that drive VEGF release—turning a clotting tendency into the engine of new vessel growth."
  - target: 01-human/04-cellular/microglia
    relation: connects-to
    note: "Diabetic retinopathy is partly neuroinflammatory: retinal microglia activate early, releasing cytokines that damage neurons and vessels before classic lesions appear—so the disease begins as inflammation and neurodegeneration, not just leaky blood vessels."
  - target: 01-human/05-tissue/fibrosis
    relation: connects-to
    note: "Advanced diabetic retinopathy ends in fibrosis: fragile new vessels grow with fibrous tissue across the retina, and when these fibrovascular membranes contract they pull the retina off—tractional retinal detachment, a major cause of blindness in the disease."
  - target: 01-human/03-molecular/pdgf
    relation: connects-to
    note: "Pericyte loss is the earliest lesion of diabetic retinopathy, and PDGF maintains pericytes: hyperglycemia disrupts PDGF-B signaling that normally keeps pericytes wrapping retinal capillaries, so they drop off, weakening vessels into microaneurysms and leaks."
  - target: 01-human/03-molecular/complement-c3
    relation: connects-to
    note: "Complement activation contributes to diabetic retinopathy: C3 and downstream complement deposit in retinal vessels, adding inflammatory injury to the high-glucose damage—an emerging arm of disease beyond the classic VEGF-driven angiogenesis."
  - target: 01-human/04-cellular/astrocyte
    relation: connects-to
    note: "Diabetic retinopathy is a neurovascular disease, not just vascular: retinal astrocytes and Müller glia that support neurons and the blood-retinal barrier dysfunction early, so neural and glial injury precede the visible vessel changes."
  - target: 01-human/03-molecular/collagen
    relation: connects-to
    note: "Diabetic retinopathy starts by thickening collagen: high glucose stiffens the retinal capillary basement membrane (collagen IV), an early change that weakens vessels into microaneurysms, and later fibrovascular collagen sheets can wrinkle and detach the retina."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Diabetic retinopathy is inflamed by macrophages: recruited myeloid cells and activated retinal microglia pour out cytokines that damage the blood-retinal barrier, adding low-grade inflammation to the classic microvascular picture."
  - target: 01-human/03-molecular/nitric-oxide
    relation: connects-to
    note: "Diabetic retinopathy reflects lost nitric oxide: damaged retinal endothelium makes too little NO to dilate vessels and autoregulate flow, so the retina swings between poor perfusion and leak—worsening the ischemia that drives VEGF."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "High glucose inflames the retina through NF-kB: hyperglycemia and AGE-RAGE signaling switch it on in retinal cells, driving the cytokines and adhesion molecules that damage capillaries—an inflammatory layer atop the vascular disease."
  - target: 01-human/06-organ/pancreas
    relation: connects-to
    note: "Diabetic retinopathy traces back to the pancreas: the failing insulin supply that defines diabetes drives the chronic high glucose that injures retinal vessels, so retinopathy is the eye's record of the pancreas's long shortfall."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "Mast cells join the inflamed diabetic retina: they degranulate near retinal vessels, releasing mediators that increase leakiness and inflammation, an emerging contributor to the macular edema that threatens vision."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "The retina is a window on the brain's vessels: diabetic retinopathy signals similar cerebral small-vessel damage, so its severity predicts stroke and cognitive decline elsewhere in the body."
  - target: 01-human/04-cellular/erythrocyte
    relation: connects-to
    note: "Diabetes stiffens red blood cells and makes them clump: less deformable erythrocytes struggle through the retina's tiny capillaries, slowing flow and feeding the ischemia that drives new-vessel growth."
  - target: 01-human/03-molecular/erythropoietin
    relation: connects-to
    note: "Erythropoietin is a hidden driver of proliferative retinopathy: the ischemic retina pours EPO into the vitreous where, alongside VEGF, it independently spurs the fragile new vessels that bleed and scar."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy shows where diabetic retinopathy begins: retinal capillaries thicken their basement membrane and lose the supporting mural cells, leaving the weakened, leaky walls that bulge into the first microaneurysms."
  - target: 01-human/04-cellular/smooth-muscle-cell
    relation: connects-to
    note: "The loss of the capillaries' mural cells starts the damage: pericytes — the contractile, smooth-muscle-like cells wrapping retinal vessels — die off early in diabetes, leaving outpouchings and leaky, unstable capillaries behind."
  - target: 01-human/02-atomic/magnesium
    relation: connects-to
    note: "Low magnesium tracks with worsening eyes: magnesium deficiency is common in diabetes and is linked to faster progression of retinopathy, likely through its effects on insulin sensitivity and the vascular endothelium."
  - target: 01-human/03-molecular/hemoglobin
    relation: connects-to
    note: "The eyes pay for the sugar logged on hemoglobin: HbA1c, glucose stuck to the red-cell protein, is the single best predictor of retinopathy risk and progression, which is why tight glucose control protects sight."
  - target: 01-human/03-molecular/fibronectin
    relation: connects-to
    note: "High sugar thickens the retina's vessel walls with matrix: fibronectin and other proteins pile into the capillary basement membrane, stiffening and narrowing the microvessels in the early structural damage of diabetic retinopathy."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "White cells help clog the retina: in diabetes, activated neutrophils and monocytes stick to the retinal capillary walls (leukostasis), plugging vessels and dropping out capillaries to create the ischemia that drives new-vessel growth."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "Antibody injections are the modern cure: intravitreal anti-VEGF agents (ranibizumab, aflibercept, bevacizumab) neutralize the VEGF driving leaky new vessels, reversing macular edema and proliferative retinopathy that laser once only slowed."
  - target: 01-human/04-cellular/fibroblast
    relation: connects-to
    note: "Late retinopathy pulls the retina loose: the fibrovascular membranes of proliferative disease contract as fibroblasts and myofibroblasts lay down scar, tugging the retina into a tractional detachment that threatens sudden vision loss."
  - target: 01-human/07-system/reproductive-system
    relation: connects-to
    note: "Pregnancy speeds the damage: diabetic retinopathy can progress rapidly during pregnancy, so diabetic women are screened more often through gestation and treated promptly to protect sight against the accelerated course."
  - target: 01-human/07-system/stroke
    relation: connects-to
    note: "The retina is a window on the whole vasculature: diabetic retinopathy marks systemic microvascular damage and independently predicts stroke and cardiovascular events, so finding it should prompt aggressive control of blood pressure and glucose."
  - target: 01-human/03-molecular/il-6
    relation: connects-to
    note: "Inflammation, not just sugar, harms the retina: IL-6 and other cytokines rise in the diabetic eye, driving the vascular leak behind macular edema — why intravitreal steroids help when anti-VEGF alone does not."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "Low-grade immune activation joins the damage: T cells and leukostasis contribute to the chronic inflammation that injures the retinal capillaries, an immune dimension layered on the metabolic insult of hyperglycemia."
  - target: 01-human/05-tissue/peripheral-nerve
    relation: connects-to
    note: "It travels with its neural cousin: diabetic retinopathy and peripheral neuropathy are parallel microvascular complications of the same hyperglycemia, so finding one should prompt screening for the other across the diabetic body."
  - target: 01-human/03-molecular/tnf-alpha
    relation: connects-to
    note: "Inflammatory cytokines stoke the leak: TNF-α released in the diabetic retina breaks down the blood-retinal barrier and drives leukostasis, adding an inflammatory push to the VEGF-driven vascular damage."
  - target: 01-human/07-system/cardiovascular-system
    relation: connects-to
    note: "The eye is a window on the arteries: diabetic retinopathy signals widespread microvascular disease, so its presence flags a markedly higher risk of heart attack, stroke and other cardiovascular events body-wide."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "STAT3 links inflammation to the leaking vessels: driven by IL-6 and high glucose in the retina, STAT3 activation in endothelial and glial cells stokes the inflammation and VEGF output behind the barrier breakdown of diabetic retinopathy."
  - target: 01-human/03-molecular/glp-1
    relation: connects-to
    note: "Rapid glucose-lowering can transiently worsen it: GLP-1 receptor agonists like semaglutide sharply improve control but carry a noted signal of early retinopathy progression, the same paradox seen with any abrupt tightening of blood sugar."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "It is a neural disease as much as a vascular one: diabetic retinal neurodegeneration damages the retina's neurons and glia — part of the nervous system — before vessels visibly fail, so neural dysfunction can precede classic retinopathy."
  - target: 01-human/07-system/anemia-of-chronic-disease
    relation: connects-to
    note: "Low hemoglobin starves the retina of oxygen: the anemia accompanying diabetic kidney disease and chronic inflammation worsens retinal hypoxia, and anemia is an independent risk factor for retinopathy progression."
  - target: 01-human/07-system/heart-failure
    relation: connects-to
    note: "It flags wider microvascular disease: diabetic retinopathy severity tracks with the small-vessel damage and diabetic cardiomyopathy that drive heart failure, making the retina a visible window onto systemic microvascular risk."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "Losing sight weighs on the mind: progressive vision loss and the threat of blindness from diabetic retinopathy carry a substantial psychological burden, with high rates of depression among affected patients."
  - target: 01-human/07-system/generalized-anxiety-disorder
    relation: connects-to
    note: "Fear of going blind breeds chronic worry: the threat of irreversible vision loss and the burden of repeated injections and laser treatment in diabetic retinopathy fuel persistent anxiety alongside depression."
  - target: 02-pathogen/03-fungi/candida-albicans
    relation: connects-to
    note: "Diabetes and intravitreal injections risk fungal eye infection: poorly controlled diabetes predisposes to endogenous Candida endophthalmitis, and the repeated intravitreal anti-VEGF injections for retinopathy add a route for infection of the eye."
  - target: 01-human/07-system/alzheimers-disease
    relation: connects-to
    note: "Retinal microvascular damage mirrors the brain's: diabetic retinopathy is a window onto systemic small-vessel disease, and its presence tracks with the cerebral microvascular injury that contributes to vascular and Alzheimer-type dementia."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "It is a direct readout of glycaemic control: diabetic retinopathy is driven by the chronic hyperglycaemia of the endocrine diabetic state, and hormonal surges of puberty and pregnancy can accelerate it."
  - target: 02-pathogen/02-bacteria/staphylococcus-aureus
    relation: connects-to
    note: "Each anti-VEGF injection risks acute endophthalmitis: the repeated intravitreal injections that treat diabetic retinopathy can introduce skin bacteria like Staphylococcus aureus, causing sight-threatening bacterial endophthalmitis."
  - target: 01-human/07-system/musculoskeletal-system
    relation: connects-to
    note: "Losing vision means losing footing: the visual impairment of advanced diabetic retinopathy is a major risk factor for falls and the fractures that follow, especially in older diabetics."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "Inflammation drives the damage and the cure: leukostasis and cytokines such as VEGF inflame and occlude retinal capillaries, which is why intravitreal anti-VEGF and corticosteroid injections treat diabetic macular oedema."
  - target: 01-human/07-system/integumentary-system
    relation: connects-to
    note: "It is a window onto systemic small-vessel disease: the same diabetic microangiopathy that scars the retina injures the skin's microcirculation, so retinopathy severity tracks diabetic dermopathy and foot microvascular damage."
  - target: 01-human/07-system/digestive-system
    relation: connects-to
    note: "It clusters with autonomic gut damage: advanced retinopathy marks long-standing, poorly-controlled diabetes, so it commonly accompanies diabetic gastroparesis and other autonomic gastrointestinal complications."
  - target: 01-human/07-system/respiratory-system
    relation: connects-to
    note: "Sleep apnoea worsens it: obstructive sleep apnoea and its intermittent nocturnal hypoxia independently aggravate diabetic retinopathy and macular oedema."
  - target: 01-human/07-system/lymphatic-system
    relation: connects-to
    note: "The eye has no lymphatics to clear it: the immune-privileged retina lacks conventional lymphatic drainage, so VEGF and oedema fluid accumulate rather than being carried away, driving the disease."
  - target: 02-pathogen/02-bacteria/staphylococcus-aureus
    relation: connects-to
    note: "Its treatment carries an infection risk: the repeated intravitreal anti-VEGF injections used for diabetic macular oedema can rarely introduce endophthalmitis, often from skin staphylococci."
  - target: 01-human/07-system/renal-system
    relation: connects-to
    note: "It travels with diabetic kidney disease: retinopathy and nephropathy are parallel microvascular complications, so retinal changes predict and mirror diabetic kidney damage."
  - target: 03-medicine/01-modern/13-cancer/targeted-therapy
    relation: connects-to
    note: "Anti-VEGF injections save sight: intravitreal anti-VEGF agents (ranibizumab, aflibercept) and steroids treat the macular oedema and neovascularisation of diabetic retinopathy."
  - target: 03-medicine/01-modern/07-metabolic/metformin
    relation: connects-to
    note: "Glycaemic control prevents it: tight glucose control with metformin and other agents slows the onset and progression of diabetic retinopathy, the leading cause of blindness in working-age adults."
  - target: 03-medicine/01-modern/12-anti-inflammatory/dexamethasone
    relation: connects-to
    note: "Sustained-release steroids for the oedema: intravitreal dexamethasone implants and triamcinolone reduce diabetic macular oedema by calming inflammation and VEGF, a second-line option when repeated anti-VEGF injections are insufficient."
  - target: 01-human/05-tissue/glomerulus
    relation: connects-to
    note: "The retina and kidney share a microangiopathy: the same hyperglycaemic capillary damage — basement-membrane thickening, pericyte loss and leak — strikes the retina and the renal glomerulus together, so retinopathy predicts diabetic nephropathy."
  - target: 03-medicine/01-modern/04-cardio/ace-inhibitors
    relation: connects-to
    note: "Blocking the renin system slows it: tight blood-pressure control, particularly with ACE inhibitors that also blunt local renin-angiotensin signalling in the retina, reduces the progression of diabetic retinopathy."
  - target: 01-human/07-system/polycythemia-vera
    relation: connects-to
    note: "Thick blood blurs the retina too: polycythaemia vera and other hyperviscosity states cause a retinopathy with engorged tortuous veins and haemorrhages that resembles diabetic retinopathy—different cause, similar retinal vascular damage."
  - target: 01-human/05-tissue/synapse
    relation: connects-to
    note: "It is also a neurodegeneration: before the microvascular signs, diabetic retinopathy quietly kills retinal neurons and their synapses, an early neurodegenerative component now recognised alongside the vascular leak and ischaemia."
  - target: 01-human/05-tissue/arterial-wall
    relation: connects-to
    note: "The retina mirrors the arteries: diabetic retinal microvascular damage signals systemic vascular injury, and retinopathy predicts stroke and coronary disease, making the eye a window onto the health of the arterial wall."
  - target: 01-human/07-system/vhl-disease
    relation: connects-to
    note: "Two VEGF-driven retinal diseases: like the retinal haemangioblastomas of von Hippel-Lindau, diabetic retinopathy proliferates and leaks under HIF-driven VEGF, and both are managed with laser photocoagulation and anti-VEGF injections."
  - target: 01-human/05-tissue/bone-marrow
    relation: connects-to
    note: "Diabetic mobilopathy: diabetes blunts the bone marrow's release of endothelial progenitor cells that repair retinal vessels, so a marrow defect compounds the eye's failure to mend damaged capillaries."
  - target: 01-human/05-tissue/myocardium
    relation: connects-to
    note: "An eye-heart axis: the microvascular disease seen as diabetic retinopathy parallels diabetic cardiomyopathy, and retinopathy independently predicts heart failure and stiffening of the myocardium."
---

# Diabetic Retinopathy

## Overview

**Diabetic retinopathy (DR)** is the most common microvascular complication of diabetes mellitus and the **leading cause of new blindness in working-age adults (20-74 years)** in developed countries [^fong-2004-dr-review]. It affects approximately **103 million adults globally** (2020 estimate), with prevalence rising proportionally to diabetes duration — present in virtually all patients with T1DM after 20 years and in >60% of patients with T2DM after 20 years.

DR encompasses a spectrum from subtle vascular changes to sight-threatening neovascularization:
1. **Non-proliferative DR (NPDR):** Microaneurysms, dot-blot hemorrhages, hard exudates, cotton-wool spots, venous beading — graded mild, moderate, severe (4-2-1 rule: hemorrhages in 4 quadrants, venous beading in 2, intraretinal microvascular abnormalities in 1)
2. **Proliferative DR (PDR):** Neovascularization (NV) of the disc (NVD) or elsewhere (NVE) on the retinal surface and into the vitreous; fibrovascular proliferation → tractional retinal detachment; vitreous hemorrhage causing sudden vision loss
3. **Diabetic macular edema (DME):** Vascular permeability increase → fluid accumulation in the macula (fovea-involving = center-involving DME = vision-threatening); present at any stage of NPDR/PDR; affects ~7% of all diabetic patients

**Pathophysiology cascade:** Chronic hyperglycemia → (1) advanced glycation end-products (AGEs) → receptor for AGE (RAGE) activation → oxidative stress + NF-κB; (2) polyol pathway flux → sorbitol accumulation → osmotic and oxidative stress; (3) PKC-β activation → VEGF upregulation → VEGFR-2 → vascular leak; (4) pericyte apoptosis (mechanism: selective pericyte glucose overload + PDGF-B resistance) → loss of vascular autoregulation → microaneurysm formation → hemostatic breakdown.

**Ang-2/VEGF cooperative axis in DR:** Diabetes → elevated circulating and retinal Ang-2 (from activated endothelial Weibel-Palade bodies) → Tie2 destabilization → pericyte detachment → capillary non-perfusion zones → retinal hypoxia → HIF-1α → VEGF-A overexpression → VEGFR-2 activation → macular edema + PDR neovascularization. Ang-2 and VEGF act synergistically: Ang-2 primes the endothelium for VEGF-driven leak at lower VEGF concentrations than would otherwise be needed.

## Structure

### Classification and staging (ETDRS/DRCR.net)

**NPDR severity scale (Early Treatment Diabetic Retinopathy Study):**

| Grade | Features |
|:---|:---|
| Mild NPDR | Microaneurysms only |
| Moderate NPDR | More than mild but less than severe; dot/blot hemorrhages, hard exudates, cotton-wool spots |
| Severe NPDR | ≥1 of: hemorrhages 4 quadrants; venous beading 2 quadrants; IRMA 1 quadrant (4-2-1 rule); 15% progress to PDR within 1 year |
| Very severe NPDR | 2 or more of the above criteria; 45% progress to PDR within 1 year |

**PDR:**
- High-risk PDR: NVD ≥1/3 disc area; or any NVD with vitreous hemorrhage; or NVE ≥1/2 disc area with vitreous hemorrhage → immediate panretinal photocoagulation (PRP) or anti-VEGF indicated
- Advanced PDR: Tractional retinal detachment; vitreous hemorrhage preventing examination → vitrectomy required

**Clinically significant macular edema (CSME — ETDRS definition):**
- Retinal thickening at or within 500 µm of the fovea center
- Hard exudates at or within 500 µm with adjacent thickening
- A zone of retinal thickening ≥1 disc area within 1 disc diameter of the fovea
- **Center-involving DME (CI-DME):** OCT-defined fluid in the foveal center subfield; primary treatment indication for anti-VEGF

### Retinal anatomy relevant to DR

**Retinal vasculature:** Three-layer capillary plexuses — superficial, intermediate, deep — derived from the central retinal artery; capillary pericytes are unique in providing direct glucose metabolic support and autoregulatory tone to retinal capillaries; pericyte:endothelial cell ratio ~1:1 (highest in the body, reflecting metabolic demand)

**Blood-retinal barrier (BRB):**
- **Inner BRB:** Tight junctions (claudin-5, occludin, ZO-1) between retinal vascular endothelial cells; pericytes maintain endothelial tight junction integrity via PDGF-B/PDGFR-β and Ang-1/Tie2 signaling
- **Outer BRB:** Tight junctions of the retinal pigment epithelium (RPE) and the choroid-RPE interface; less affected in early DR; becomes important in exudative AMD

**OCT imaging:** Spectral-domain optical coherence tomography (SD-OCT) measures central subfield thickness (CST; normal ~240-260 µm in foveal center); CI-DME defined as CST ≥300 µm + foveal fluid on OCT; OCT angiography (OCTA) provides non-invasive imaging of retinal capillary plexuses and quantifies foveal avascular zone (FAZ) area

## Function

### Screening and prevention

**Screening guidelines:**
- T1DM: First eye exam 5 years after diagnosis; annual thereafter
- T2DM: Eye exam at diagnosis; annually thereafter
- Pregnancy with diabetes: First trimester + Q trimester monitoring (rapid DR progression in pregnancy)
- Telemedicine screening: AI-based retinal image grading (IDx-DR, EyeArt) — FDA-cleared; 91% sensitivity, 94% specificity for >mild NPDR

**Prevention — systemic glycemic and BP control:**
- DCCT (T1DM): Intensive glycemic control (HbA1c ~7.2% vs. 9.1%) → 76% reduction in DR onset, 54% reduction in progression
- UKPDS (T2DM): Each 1% reduction in HbA1c → 35% reduction in DR progression; BP control to <150/85 → 34% reduction in DR progression
- Fenofibrate (ACCORD-Eye): +anti-VEGF effect via PPARα → ↓DR progression rate by 40% in T2DM with dyslipidemia; now recommended as adjunct in T2DM with NPDR + elevated triglycerides

### Treatment — Diabetic Macular Edema

**Anti-VEGF therapy (first-line for CI-DME):** [^brown-2015-aflibercept-protocol-t]

**Protocol T (DRCR.net):** Head-to-head comparison of bevacizumab 1.25 mg, ranibizumab 0.3 mg, and aflibercept 2 mg intravitreal for CI-DME:
- At 1 year: Aflibercept +13.3 letters, ranibizumab +11.2 letters, bevacizumab +9.7 letters
- For baseline BCVA <69 letters (worse vision): Aflibercept significantly superior to bevacizumab and ranibizumab
- At 2 years: Differences largely resolved with PRN dosing; aflibercept still superior in worse baseline VA group
- **Dosing burden:** All require Q4-8W injections — significant patient and system burden

**Faricimab (Vabysmo) — dual Ang-2/VEGF blockade:** [^wykoff-2022-faricimab-dr]
- **YOSEMITE (N=940) + RHINE (N=951):** Faricimab 6 mg Q8W or PTI (up to Q16W) vs. aflibercept 2 mg Q8W
- BCVA: Non-inferior to aflibercept at 1 year (+10.7 to +11.6 vs. +10.9 letters); similar at 2 years
- **Durability (key advantage):** At 1 year, 53% (YOSEMITE) and 60% (RHINE) of PTI patients on Q12W or Q16W intervals; at 2 years ~50% remain at ≤Q16W
- Anatomical: Greater CST reduction with faricimab; higher rates of complete fluid resolution on OCT
- **FDA approval:** January 2022 for DME; also approved for nAMD simultaneously
- Significance: First retinal therapy to demonstrate Ang-2 pathway targeting translates to clinical benefit with extended durability

**Other approved anti-VEGF agents for DME:**
- **Ranibizumab (Lucentis):** Anti-VEGF Fab; 0.3 mg Q4W × 6 months; FDA-approved
- **Aflibercept (Eylea):** VEGF-trap (VEGFR1/2-Fc fusion); 2 mg Q4W × 5 → Q8W; FDA-approved; high-dose aflibercept 8 mg (PHOTON trial, Q12-16W) — FDA-approved 2023
- **Bevacizumab (Avastin):** Off-label; cost ~$50/vial vs. ~$1,800-2,000 for ranibizumab/aflibercept; comparable efficacy in most baseline VA groups

### Treatment — Proliferative DR

**Panretinal photocoagulation (PRP):**
- 1200-1600 argon laser burns in peripheral retina → ablation of ischemic retina → reduced VEGF production → NV regression
- DRS + ETDRS: PRP reduces severe vision loss by >50% in high-risk PDR
- Complications: Loss of peripheral visual field, reduced night vision, exacerbation of DME (laser-induced fluid)
- **Anti-VEGF + PRP:** Protocol S (DRCR.net): Ranibizumab non-inferior to PRP for PDR at 2 years; lower rates of DME, better peripheral visual field preservation; BUT: requires sustained monthly injections — loss to follow-up can be catastrophic

**Vitrectomy for advanced PDR:**
- Tractional retinal detachment + vitreous hemorrhage obscuring the macula
- Pars plana vitrectomy (PPV): 23G or 25G; membrane peeling, intraocular tamponade (gas/silicone oil)
- Pre-operative anti-VEGF injection (bevacizumab 48-72h before) → reduces intraoperative bleeding and fibrovascular proliferation

## Pathology

**Diabetic papillopathy:** Optic disc edema in diabetes, usually self-limited; hyperemic, swollen disc; must be differentiated from ischemic optic neuropathy

**Diabetic cataracts:** Sorbitol accumulation in the lens → osmotic lens swelling → cortical cataract; earlier onset in poorly controlled DM; snowflake cataract (vacuolar) pathognomonic but rare

**Retinal vein occlusion comorbidity:** Diabetic patients have 2-4× higher risk of branch and central retinal vein occlusion (same endothelial + VEGF pathophysiology); both conditions respond to anti-VEGF

**Neovascular glaucoma (NVG):** Retinal ischemia → VEGF → iris and angle neovascularization (rubeosis iridis) → secondary angle-closure glaucoma; complication of severe PDR; treated with anti-VEGF injection + PRP ± glaucoma surgery; a leading cause of painful blind eye in DM

## Connections

- `connects-to` → **[Angiopoietin](../../03-molecular/angiopoietin/README.md)** — Ang-2 elevated in diabetic retinas → Tie2 destabilization → pericyte loss → endothelial junction opening → macular edema + neovascularization; faricimab (anti-Ang-2 + anti-VEGF-A) achieves Q16W dosing with non-inferior VA gains vs. aflibercept Q8W (YOSEMITE/RHINE).
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — VEGF-A drives DME and PDR neovascularization; hypoxic retina → HIF-1α → VEGF → VEGFR-2 → endothelial proliferation and barrier disruption; anti-VEGF (ranibizumab, aflibercept, bevacizumab) is the first-line treatment for center-involving DME and PDR.
- `connects-to` → **[Hypertension](../hypertension/README.md)** — Hypertension accelerates DR through retinal arteriolar pressure, shear stress, and RAAS activation; BP control to <130/80 mmHg reduces DR progression by ~30% (UKPDS); hypertensive retinopathy and DR frequently coexist and share pathophysiology.
- `targets` → **[Eye](../../06-organ/eye/README.md)** — Diabetic retinopathy targets the retina: pericyte loss → microaneurysms → exudates → macular edema → neovascularization → vitreous hemorrhage → tractional retinal detachment; the retina is the primary organ affected, with foveal photoreceptors most critical for central vision.
- `connects-to` → **[Wound Healing](../wound-healing/README.md)** — Diabetes impairs wound healing through AGE accumulation, pericyte dysfunction, impaired neutrophil function, and reduced HIF-1α/VEGF response; diabetic foot ulcers affect ~15% of people with diabetes and are the leading cause of non-traumatic amputation.
- `connects-to` → **[Type 1 Diabetes](../type-1-diabetes/README.md)** — Diabetic retinopathy is the leading microvascular complication of type 1 diabetes, present in nearly all patients after 20 years; the DCCT proved that intensive glycemic control reduces retinopathy onset by 76% and progression by 54%, so screening begins 5 years after diagnosis.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — Diabetic retinopathy is fundamentally a failure of retinal vascular endothelial cells: hyperglycemia and pericyte dropout disrupt their inner blood-retinal-barrier tight junctions → leak and macular edema, then hypoxia drives them to proliferate into the vitreous.
- `connects-to` → **[HIF-1alpha](../../03-molecular/hif-1alpha/README.md)** — As diabetic capillary closure starves the retina of oxygen, HIF-1α stabilizes and transcribes VEGF (and EPO, Ang-2), triggering the neovascularization of proliferative DR; panretinal photocoagulation works by ablating ischemic retina to lower this HIF-driven VEGF output.
- `connects-to` → **[Type 2 Diabetes](../type-2-diabetes/README.md)** — Although classically tied to type 1, most diabetic retinopathy occurs in type 2 diabetes because T2D is far more prevalent; many T2D patients already have retinopathy at diagnosis after years of silent hyperglycemia, so screening begins at T2D diagnosis (vs 5 years in T1D).
- `connects-to` → **[Chronic Kidney Disease](../ckd/README.md)** — Diabetic retinopathy and diabetic kidney disease are parallel microvascular complications: both stem from hyperglycemic endothelial injury, retinopathy strongly predicts nephropathy, and its presence supports a diabetic etiology when a diabetic patient develops proteinuric CKD.
- `connects-to` → **[Neuropathic Pain](../neuropathic-pain/README.md)** — Retinopathy, nephropathy and neuropathy form the diabetic microvascular triad: the same hyperglycemic, polyol- and AGE-mediated microvascular damage that injures the retina also damages peripheral nerves → painful diabetic neuropathy; glycemic control reduces all three together.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Laser photons treat diabetic retinopathy: pan-retinal photocoagulation burns ischemic peripheral retina to suppress VEGF and halt neovascularization, while focal laser seals leaking microaneurysms—an older mainstay now complemented by anti-VEGF injections.
- `connects-to` → **[Atherosclerosis](../atherosclerosis/README.md)** — Diabetic retinopathy is the microvascular mirror of atherosclerosis's macrovascular disease: the same hyperglycemia, dyslipidemia, and hypertension that clog large arteries damage retinal capillaries, so retinopathy on fundoscopy flags systemic vascular risk.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — Diabetic retinopathy is now seen as a neurovascular disease, not purely vascular: retinal neurons and glia are injured early—before visible microaneurysms—as hyperglycemia disrupts neuronal metabolism, so subtle vision loss can precede vascular lesions.
- `connects-to` → **[RAGE](../../03-molecular/rage/README.md)** — Advanced glycation end products and their receptor RAGE drive diabetic retinopathy: chronic hyperglycemia glycates proteins that bind RAGE on retinal vessels, triggering inflammation and pericyte loss—a core mechanism translating high glucose into microvascular damage.
- `connects-to` → **[Obesity](../obesity/README.md)** — Obesity feeds diabetic retinopathy through type 2 diabetes: the insulin resistance and hyperglycemia of obesity-driven diabetes damage retinal microvessels over years, so the obesity epidemic expands the population at risk for the leading cause of working-age blindness.
- `connects-to` → **[Sickle Cell Disease](../sickle-cell-disease/README.md)** — Diabetic retinopathy and sickle cell retinopathy are both proliferative retinopathies: both occlude retinal capillaries—by hyperglycemic microangiopathy versus sickled-cell vaso-occlusion—driving VEGF-fueled neovascularization that can bleed and detach the retina.
- `connects-to` → **[Oxygen](../../02-atomic/oxygen/README.md)** — Retinal ischemia drives proliferative diabetic retinopathy: capillary damage starves the retina of oxygen, so the hypoxic tissue pours out VEGF that grows fragile new vessels which bleed and detach the retina—why anti-VEGF injections and laser are the mainstay.
- `connects-to` → **[Insulin](../../03-molecular/insulin/README.md)** — Glycemic control is the key lever against diabetic retinopathy: chronic high glucose damages retinal microvessels, so insulin and other glucose-lowering therapy slow progression—though rapid correction can transiently worsen it, demanding careful monitoring.
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — Diabetic retinopathy and nephropathy are paired microvascular complications: the same chronic hyperglycemia that damages retinal capillaries injures the glomerulus, so retinopathy often signals coexisting kidney disease—a shared small-vessel toll of diabetes.
- `connects-to` → **[Platelet](../../04-cellular/platelet/README.md)** — Platelets help close off the diabetic retina: hyperglycemia makes them stickier, so microthrombi plug retinal capillaries and create the non-perfused, ischemic patches that drive VEGF release—turning a clotting tendency into the engine of new vessel growth.
- `connects-to` → **[Microglia](../../04-cellular/microglia/README.md)** — Diabetic retinopathy is partly neuroinflammatory: retinal microglia activate early, releasing cytokines that damage neurons and vessels before classic lesions appear—so the disease begins as inflammation and neurodegeneration, not just leaky blood vessels.
- `connects-to` → **[Fibrosis](../../05-tissue/fibrosis/README.md)** — Advanced diabetic retinopathy ends in fibrosis: fragile new vessels grow with fibrous tissue across the retina, and when these fibrovascular membranes contract they pull the retina off—tractional retinal detachment, a major cause of blindness in the disease.
- `connects-to` → **[PDGF](../../03-molecular/pdgf/README.md)** — Pericyte loss is the earliest lesion of diabetic retinopathy, and PDGF maintains pericytes: hyperglycemia disrupts PDGF-B signaling that normally keeps pericytes wrapping retinal capillaries, so they drop off, weakening vessels into microaneurysms and leaks.
- `connects-to` → **[Complement C3](../../03-molecular/complement-c3/README.md)** — Complement activation contributes to diabetic retinopathy: C3 and downstream complement deposit in retinal vessels, adding inflammatory injury to the high-glucose damage—an emerging arm of disease beyond the classic VEGF-driven angiogenesis.
- `connects-to` → **[Astrocyte](../../04-cellular/astrocyte/README.md)** — Diabetic retinopathy is a neurovascular disease, not just vascular: retinal astrocytes and Müller glia that support neurons and the blood-retinal barrier dysfunction early, so neural and glial injury precede the visible vessel changes.
- `connects-to` → **[Collagen](../../03-molecular/collagen/README.md)** — Diabetic retinopathy starts by thickening collagen: high glucose stiffens the retinal capillary basement membrane (collagen IV), an early change that weakens vessels into microaneurysms, and later fibrovascular collagen sheets can wrinkle and detach the retina.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Diabetic retinopathy is inflamed by macrophages: recruited myeloid cells and activated retinal microglia pour out cytokines that damage the blood-retinal barrier, adding low-grade inflammation to the classic microvascular picture.
- `connects-to` → **[Nitric Oxide](../../03-molecular/nitric-oxide/README.md)** — Diabetic retinopathy reflects lost nitric oxide: damaged retinal endothelium makes too little NO to dilate vessels and autoregulate flow, so the retina swings between poor perfusion and leak—worsening the ischemia that drives VEGF.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — High glucose inflames the retina through NF-kB: hyperglycemia and AGE-RAGE signaling switch it on in retinal cells, driving the cytokines and adhesion molecules that damage capillaries—an inflammatory layer atop the vascular disease.
- `connects-to` → **[Pancreas](../../06-organ/pancreas/README.md)** — Diabetic retinopathy traces back to the pancreas: the failing insulin supply that defines diabetes drives the chronic high glucose that injures retinal vessels, so retinopathy is the eye's record of the pancreas's long shortfall.
- `connects-to` → **[Mast Cell](../../04-cellular/mast-cell/README.md)** — Mast cells join the inflamed diabetic retina: they degranulate near retinal vessels, releasing mediators that increase leakiness and inflammation, an emerging contributor to the macular edema that threatens vision.
- `connects-to` → **[Brain](../../06-organ/brain/README.md)** — The retina is a window on the brain's vessels: diabetic retinopathy signals similar cerebral small-vessel damage, so its severity predicts stroke and cognitive decline elsewhere in the body.
- `connects-to` → **[Erythrocyte](../../04-cellular/erythrocyte/README.md)** — Diabetes stiffens red blood cells and makes them clump: less deformable erythrocytes struggle through the retina's tiny capillaries, slowing flow and feeding the ischemia that drives new-vessel growth.
- `connects-to` → **[Erythropoietin](../../03-molecular/erythropoietin/README.md)** — Erythropoietin is a hidden driver of proliferative retinopathy: the ischemic retina pours EPO into the vitreous where, alongside VEGF, it independently spurs the fragile new vessels that bleed and scar.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy shows where diabetic retinopathy begins: retinal capillaries thicken their basement membrane and lose the supporting mural cells, leaving the weakened, leaky walls that bulge into the first microaneurysms.
- `connects-to` → **[Smooth Muscle Cell](../../04-cellular/smooth-muscle-cell/README.md)** — The loss of the capillaries' mural cells starts the damage: pericytes — the contractile, smooth-muscle-like cells wrapping retinal vessels — die off early in diabetes, leaving outpouchings and leaky, unstable capillaries behind.
- `connects-to` → **[Magnesium](../../02-atomic/magnesium/README.md)** — Low magnesium tracks with worsening eyes: magnesium deficiency is common in diabetes and is linked to faster progression of retinopathy, likely through its effects on insulin sensitivity and the vascular endothelium.
- `connects-to` → **[Hemoglobin](../../03-molecular/hemoglobin/README.md)** — The eyes pay for the sugar logged on hemoglobin: HbA1c, glucose stuck to the red-cell protein, is the single best predictor of retinopathy risk and progression, which is why tight glucose control protects sight.
- `connects-to` → **[Fibronectin](../../03-molecular/fibronectin/README.md)** — High sugar thickens the retina's vessel walls with matrix: fibronectin and other proteins pile into the capillary basement membrane, stiffening and narrowing the microvessels in the early structural damage of diabetic retinopathy.
- `connects-to` → **[Neutrophil](../../04-cellular/neutrophil/README.md)** — White cells help clog the retina: in diabetes, activated neutrophils and monocytes stick to the retinal capillary walls (leukostasis), plugging vessels and dropping out capillaries to create the ischemia that drives new-vessel growth.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — Antibody injections are the modern cure: intravitreal anti-VEGF agents (ranibizumab, aflibercept, bevacizumab) neutralize the VEGF driving leaky new vessels, reversing macular edema and proliferative retinopathy that laser once only slowed.
- `connects-to` → **[Fibroblast](../../04-cellular/fibroblast/README.md)** — Late retinopathy pulls the retina loose: the fibrovascular membranes of proliferative disease contract as fibroblasts and myofibroblasts lay down scar, tugging the retina into a tractional detachment that threatens sudden vision loss.
- `connects-to` → **[Reproductive System](../reproductive-system/README.md)** — Pregnancy speeds the damage: diabetic retinopathy can progress rapidly during pregnancy, so diabetic women are screened more often through gestation and treated promptly to protect sight against the accelerated course.
- `connects-to` → **[Stroke](../stroke/README.md)** — The retina is a window on the whole vasculature: diabetic retinopathy marks systemic microvascular damage and independently predicts stroke and cardiovascular events, so finding it should prompt aggressive control of blood pressure and glucose.
- `connects-to` → **[Interleukin-6](../../03-molecular/il-6/README.md)** — Inflammation, not just sugar, harms the retina: IL-6 and other cytokines rise in the diabetic eye, driving the vascular leak behind macular edema — why intravitreal steroids help when anti-VEGF alone does not.
- `connects-to` → **[T Helper Cell](../../04-cellular/t-helper-cell/README.md)** — Low-grade immune activation joins the damage: T cells and leukostasis contribute to the chronic inflammation that injures the retinal capillaries, an immune dimension layered on the metabolic insult of hyperglycemia.
- `connects-to` → **[Peripheral Nerve](../../05-tissue/peripheral-nerve/README.md)** — It travels with its neural cousin: diabetic retinopathy and peripheral neuropathy are parallel microvascular complications of the same hyperglycemia, so finding one should prompt screening for the other across the diabetic body.
- `connects-to` → **[TNF-α](../../03-molecular/tnf-alpha/README.md)** — Inflammatory cytokines stoke the leak: TNF-α released in the diabetic retina breaks down the blood-retinal barrier and drives leukostasis, adding an inflammatory push to the VEGF-driven vascular damage.
- `connects-to` → **[Cardiovascular system](../cardiovascular-system/README.md)** — The eye is a window on the arteries: diabetic retinopathy signals widespread microvascular disease, so its presence flags a markedly higher risk of heart attack, stroke and other cardiovascular events body-wide.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — STAT3 links inflammation to the leaking vessels: driven by IL-6 and high glucose in the retina, STAT3 activation in endothelial and glial cells stokes the inflammation and VEGF output behind the barrier breakdown of diabetic retinopathy.
- `connects-to` → **[GLP-1](../../03-molecular/glp-1/README.md)** — Rapid glucose-lowering can transiently worsen it: GLP-1 receptor agonists like semaglutide sharply improve control but carry a noted signal of early retinopathy progression, the same paradox seen with any abrupt tightening of blood sugar.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — It is a neural disease as much as a vascular one: diabetic retinal neurodegeneration damages the retina's neurons and glia — part of the nervous system — before vessels visibly fail, so neural dysfunction can precede classic retinopathy.
- `connects-to` → **[Anemia of Chronic Disease](../anemia-of-chronic-disease/README.md)** — Low hemoglobin starves the retina of oxygen: the anemia accompanying diabetic kidney disease and chronic inflammation worsens retinal hypoxia, and anemia is an independent risk factor for retinopathy progression.
- `connects-to` → **[Heart Failure](../heart-failure/README.md)** — It flags wider microvascular disease: diabetic retinopathy severity tracks with the small-vessel damage and diabetic cardiomyopathy that drive heart failure, making the retina a visible window onto systemic microvascular risk.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — Losing sight weighs on the mind: progressive vision loss and the threat of blindness from diabetic retinopathy carry a substantial psychological burden, with high rates of depression among affected patients.
- `connects-to` → **[Generalized Anxiety Disorder](../generalized-anxiety-disorder/README.md)** — Fear of going blind breeds chronic worry: the threat of irreversible vision loss and the burden of repeated injections and laser treatment in diabetic retinopathy fuel persistent anxiety alongside depression.
- `connects-to` → **[Candida albicans](../../../02-pathogen/03-fungi/candida-albicans/README.md)** — Diabetes and intravitreal injections risk fungal eye infection: poorly controlled diabetes predisposes to endogenous Candida endophthalmitis, and the repeated intravitreal anti-VEGF injections for retinopathy add a route for infection of the eye.
- `connects-to` → **[Alzheimer's Disease](../alzheimers-disease/README.md)** — Retinal microvascular damage mirrors the brain's: diabetic retinopathy is a window onto systemic small-vessel disease, and its presence tracks with the cerebral microvascular injury that contributes to vascular and Alzheimer-type dementia.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — It is a direct readout of glycaemic control: diabetic retinopathy is driven by the chronic hyperglycaemia of the endocrine diabetic state, and hormonal surges of puberty and pregnancy can accelerate it.
- `connects-to` → **[Staphylococcus aureus](../../../02-pathogen/02-bacteria/staphylococcus-aureus/README.md)** — Each anti-VEGF injection risks acute endophthalmitis: the repeated intravitreal injections that treat diabetic retinopathy can introduce skin bacteria like Staphylococcus aureus, causing sight-threatening bacterial endophthalmitis.
- `connects-to` → **[Musculoskeletal System](../musculoskeletal-system/README.md)** — Losing vision means losing footing: the visual impairment of advanced diabetic retinopathy is a major risk factor for falls and the fractures that follow, especially in older diabetics.
- `connects-to` → **[Immune System](../immune-system/README.md)** — Inflammation drives the damage and the cure: leukostasis and cytokines such as VEGF inflame and occlude retinal capillaries, which is why intravitreal anti-VEGF and corticosteroid injections treat diabetic macular oedema.
- `connects-to` → **[Integumentary System](../integumentary-system/README.md)** — It is a window onto systemic small-vessel disease: the same diabetic microangiopathy that scars the retina injures the skin's microcirculation, so retinopathy severity tracks diabetic dermopathy and foot microvascular damage.
- `connects-to` → **[Digestive System](../digestive-system/README.md)** — It clusters with autonomic gut damage: advanced retinopathy marks long-standing, poorly-controlled diabetes, so it commonly accompanies diabetic gastroparesis and other autonomic gastrointestinal complications.
- `connects-to` → **[Respiratory System](../respiratory-system/README.md)** — Sleep apnoea worsens it: obstructive sleep apnoea and its intermittent nocturnal hypoxia independently aggravate diabetic retinopathy and macular oedema.
- `connects-to` → **[Lymphatic System](../lymphatic-system/README.md)** — The eye has no lymphatics to clear it: the immune-privileged retina lacks conventional lymphatic drainage, so VEGF and oedema fluid accumulate rather than being carried away, driving the disease.
- `connects-to` → **[Staphylococcus aureus](../../../02-pathogen/02-bacteria/staphylococcus-aureus/README.md)** — Its treatment carries an infection risk: the repeated intravitreal anti-VEGF injections used for diabetic macular oedema can rarely introduce endophthalmitis, often from skin staphylococci.
- `connects-to` → **[Renal System](../renal-system/README.md)** — It travels with diabetic kidney disease: retinopathy and nephropathy are parallel microvascular complications, so retinal changes predict and mirror diabetic kidney damage.
- `connects-to` → **[Targeted Therapy](../../../03-medicine/01-modern/13-cancer/targeted-therapy/README.md)** — Anti-VEGF injections save sight: intravitreal anti-VEGF agents (ranibizumab, aflibercept) and steroids treat the macular oedema and neovascularisation of diabetic retinopathy.
- `connects-to` → **[Metformin](../../../03-medicine/01-modern/07-metabolic/metformin/README.md)** — Glycaemic control prevents it: tight glucose control with metformin and other agents slows the onset and progression of diabetic retinopathy, the leading cause of blindness in working-age adults.
- `connects-to` → **[Dexamethasone](../../../03-medicine/01-modern/12-anti-inflammatory/dexamethasone/README.md)** — Sustained-release steroids for the oedema: intravitreal dexamethasone implants and triamcinolone reduce diabetic macular oedema by calming inflammation and VEGF, a second-line option when repeated anti-VEGF injections are insufficient.
- `connects-to` → **[Glomerulus](../../05-tissue/glomerulus/README.md)** — The retina and kidney share a microangiopathy: the same hyperglycaemic capillary damage — basement-membrane thickening, pericyte loss and leak — strikes the retina and the renal glomerulus together, so retinopathy predicts diabetic nephropathy.
- `connects-to` → **[ACE Inhibitors](../../../03-medicine/01-modern/04-cardio/ace-inhibitors/README.md)** — Blocking the renin system slows it: tight blood-pressure control, particularly with ACE inhibitors that also blunt local renin-angiotensin signalling in the retina, reduces the progression of diabetic retinopathy.
- `connects-to` → **[Polycythemia Vera](../polycythemia-vera/README.md)** — Thick blood blurs the retina too: polycythaemia vera and other hyperviscosity states cause a retinopathy with engorged tortuous veins and haemorrhages that resembles diabetic retinopathy—different cause, similar retinal vascular damage.
- `connects-to` → **[Synapse](../../05-tissue/synapse/README.md)** — It is also a neurodegeneration: before the microvascular signs, diabetic retinopathy quietly kills retinal neurons and their synapses, an early neurodegenerative component now recognised alongside the vascular leak and ischaemia.
- `connects-to` → **[Arterial Wall](../../05-tissue/arterial-wall/README.md)** — The retina mirrors the arteries: diabetic retinal microvascular damage signals systemic vascular injury, and retinopathy predicts stroke and coronary disease, making the eye a window onto the health of the arterial wall.
- `connects-to` → **[VHL Disease](../vhl-disease/README.md)** — Two VEGF-driven retinal diseases: like the retinal haemangioblastomas of von Hippel-Lindau, diabetic retinopathy proliferates and leaks under HIF-driven VEGF, and both are managed with laser photocoagulation and anti-VEGF injections.
- `connects-to` → **[Bone Marrow](../../05-tissue/bone-marrow/README.md)** — Diabetic mobilopathy: diabetes blunts the bone marrow's release of endothelial progenitor cells that repair retinal vessels, so a marrow defect compounds the eye's failure to mend damaged capillaries.
- `connects-to` → **[Myocardium](../../05-tissue/myocardium/README.md)** — An eye-heart axis: the microvascular disease seen as diabetic retinopathy parallels diabetic cardiomyopathy, and retinopathy independently predicts heart failure and stiffening of the myocardium.

[^fong-2004-dr-review]: Fong DS, Aiello L, Gardner TW, et al. Diabetic retinopathy. *Diabetes Care.* 2004;27(10):2540-2553. [doi:10.2337/diacare.27.10.2540](https://doi.org/10.2337/diacare.27.10.2540) · [PubMed 15451934](https://pubmed.ncbi.nlm.nih.gov/15451934/)
[^brown-2015-aflibercept-protocol-t]: Diabetic Retinopathy Clinical Research Network; Wells JA, Glassman AR, et al. Aflibercept, Bevacizumab, or Ranibizumab for Diabetic Macular Edema. *N Engl J Med.* 2015;372(13):1193-1203. [doi:10.1056/NEJMoa1414264](https://doi.org/10.1056/NEJMoa1414264) · [PubMed 25692915](https://pubmed.ncbi.nlm.nih.gov/25692915/)
[^wykoff-2022-faricimab-dr]: Wykoff CC, Abreu F, Adamis AP, et al. Efficacy, durability, and safety of intravitreal faricimab with extended dosing up to every 16 weeks in patients with diabetic macular oedema. *Lancet.* 2022;399(10326):741-755. [doi:10.1016/S0140-6736(22)00018-6](https://doi.org/10.1016/S0140-6736(22)00018-6) · [PubMed 35085503](https://pubmed.ncbi.nlm.nih.gov/35085503/)
