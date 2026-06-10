---
schema: human-scale-entry/v1
id: arterial-wall
name: Arterial Wall
atlas: 01-human
scale: 05-tissue
status: draft
last_reviewed: 2026-06-05
summary: "Multi-layered vascular wall (intima, media, adventitia) regulating blood pressure and flow. Elastic arteries buffer pulsatile flow (Windkessel); muscular arteries control regional resistance; endothelial eNOS-NO and SMC tone determine vascular diameter."
aliases: ["tunica intima", "tunica media", "tunica adventitia", "aortic wall", "vascular wall", "blood vessel wall"]
sources:
  - id: guyton-hall
    type: textbook
    cite: "Hall JE, Hall ME. Guyton and Hall Textbook of Medical Physiology. 14th ed. Elsevier; 2021."
    url: "https://www.elsevier.com/books/guyton-and-hall-textbook-of-medical-physiology/hall/978-0-323-59712-8"
    accessed: "2026-06-05"
  - id: alberts-mol-cell-biology
    type: textbook
    cite: "Alberts B, Johnson A, Lewis J, et al. Molecular Biology of the Cell. 7th ed. W.W. Norton; 2022."
    url: "https://www.ncbi.nlm.nih.gov/books/NBK26880/"
    accessed: "2026-06-05"
cross_links:
  - target: 01-human/07-system/cardiovascular-system
    relation: part-of
    note: "Arterial wall provides structural integrity and vasoregulatory function; tunica media SMC tone determines SVR; Windkessel elastin in aorta sustains diastolic pressure for continuous coronary perfusion."
  - target: 01-human/03-molecular/nitric-oxide
    relation: modulates
    note: "Endothelial eNOS produces NO under shear stress → SMC sGC→cGMP→MLCP→vasodilation; disturbed shear at atherosclerosis-prone sites reduces eNOS activity and promotes oxidative NO scavenging."
  - target: 01-human/03-molecular/cholesterol
    relation: modulates
    note: "Subendothelial LDL retention and oxidation (MPO/lipoxygenase/LOX-1) in tunica intima initiates atherogenesis; macrophage SR-A1/CD36 oxLDL uptake forms foam cells; statins reduce intimal LDL accumulation."
  - target: 01-human/04-cellular/macrophage
    relation: modulates
    note: "Monocytes cross activated endothelium via VCAM-1/MCP-1 and become plaque macrophages; foam cells form the necrotic core; MMP-2/9 degrade fibrous cap collagen → cap thinning → plaque rupture risk."
  - target: 01-human/04-cellular/smooth-muscle-cell
    relation: contains
    note: "SMC dominate the tunica media; phenotypic switching from contractile to synthetic SMC initiates atherogenesis; hypertension → SMC hypertrophy + collagen deposition → stiffening; SMC apoptosis in the fibrous cap → cap thinning → plaque vulnerability and rupture."
  - target: 01-human/04-cellular/endothelial-cell
    relation: contains
    note: "Endothelial cells line the tunica intima; under laminar shear → eNOS-NO + PGI₂ + thrombomodulin → anti-thrombotic, anti-inflammatory state; disturbed flow at bifurcations → NF-κB → VCAM-1/ICAM-1/MCP-1 → monocyte adhesion → atherogenesis initiation at predisposed sites."
  - target: 01-human/07-system/atherosclerosis
    relation: connects-to
    note: "The arterial wall is the primary site of atherogenesis; endothelial dysfunction → LDL retention and oxidation in tunica intima → foam cell necrotic core; fibrous cap thinning by MMP-2/9 → rupture → thrombus → ACS and stroke; statins + antiplatelet therapy are standard prevention."
---

# Arterial Wall

## Overview

The arterial wall is a multi-layered tubular structure that composes all arteries and arterioles in the systemic and pulmonary circulations. Organised into three concentric tunics — intima, media, and adventitia — its composition and mechanical properties are tuned to vessel type and location.[^guyton-hall] Elastic arteries (aorta and major branches) act as Windkessel reservoirs, storing 40–60% of left ventricular stroke volume energy during systole and releasing it during diastole to maintain continuous coronary and cerebral perfusion. Muscular arteries (coronary, femoral, renal) regulate regional blood flow through smooth muscle cell (SMC) tone. Arterioles (10–100 µm diameter) are the primary resistance vessels that determine capillary perfusion pressure and, collectively, systemic vascular resistance (SVR).

The endothelium lining the tunica intima is a critical signalling organ: it constitutively secretes anti-thrombotic, anti-inflammatory, and vasodilatory mediators under physiological shear stress, and switches to a pro-inflammatory, pro-thrombotic phenotype under disturbed flow — the mechanistic basis of site-specific atherosclerosis at bifurcations and curvatures.[^alberts-mol-cell-biology]

## Structure

**Tunica intima (innermost layer).** A single monolayer of endothelial cells (EC) aligned with the direction of blood flow, resting on a thin subendothelial connective tissue layer (type IV collagen, fibronectin, laminin basement membrane; sparse SMCs in larger arteries). ECs are flat, elongated cells (~50 × 10 µm) with tight junctions (claudin-5, occludin, ZO-1) that maintain selective permeability. Under atheroprotective laminar shear (>15 dynes/cm²), ECs upregulate KLF2, KLF4, and eNOS, and downregulate inflammatory adhesion molecules. At bifurcations and inner curvatures, disturbed/oscillatory flow (<4 dynes/cm²) drives NF-κB activation, ICAM-1/VCAM-1 expression, oxidised LDL accumulation, and leukocyte adhesion — initiating atherosclerosis.[^alberts-mol-cell-biology] The endothelium is constitutively anti-thrombotic via thrombomodulin (converts thrombin from pro-coagulant to anticoagulant — activates Protein C), TFPI, tPA, prostacyclin (PGI₂), and eNOS-derived NO (↓platelet aggregation, ↓vascular SMC proliferation).

**Tunica media (middle layer).** The mechanically dominant layer, composed predominantly of SMCs and extracellular matrix:
- *Elastic arteries* (aorta, pulmonary artery, common carotid): 50–60 concentric fenestrated lamellae of elastin, collagen (type I/III), and SMCs. Elastin (Young's modulus ~0.6 MPa) confers resilience — stores pulse energy and passively recoils in diastole (Windkessel effect). The internal elastic lamina (IEL) separates intima from media; the external elastic lamina (EEL) separates media from adventitia.
- *Muscular arteries* (coronary, femoral, mesenteric): 3–40 layers of circumferentially arranged SMCs; less elastin, more collagen. SMC tone is regulated by sympathetic adrenergic input (α₁AR → Gq → IP₃ → Ca²⁺ → MLCK → contraction; β₂AR → Gs → cAMP → PKA → MLCP → relaxation), vasoactive hormones (angiotensin II, vasopressin, endothelin-1 → contraction; atrial natriuretic peptide, eNOS-NO → relaxation), and local metabolites (hypercapnia, hypoxia, adenosine → vasodilation).[^guyton-hall]
- *Vasa vasorum*: Small vessels within the wall of large arteries (aorta, pulmonary artery) that supply the outer media and adventitia; the inner media and intima are nourished by luminal diffusion.

**Tunica adventitia (outermost layer).** Loose connective tissue (type I collagen, elastin fibrils, fibroblasts, adipocytes) containing sympathetic adrenergic nerve fibres (norepinephrine → α₁AR on medial SMC → vasoconstriction), lymphatic capillaries, vasa vasorum arteries and veins, and adventitial progenitor/pericyte cells. Collagen in the adventitia is crimped at low pressures, becomes taut at high pressures — providing a strain-limiting outer jacket that prevents vessel rupture.[^alberts-mol-cell-biology]

**Haemodynamic relationships.** Wall stress (σ) obeys the Law of Laplace for thick-walled tubes: σ = P × r / (2h), where P = transmural pressure, r = vessel radius, h = wall thickness. Pulse pressure (PP = SBP − DBP) reflects arterial stiffness: ageing increases collagen:elastin ratio → ↑stiffness → ↑PP → ↑LV afterload (isolated systolic hypertension in the elderly).[^guyton-hall]

## Function

**Mechanical buffering (Windkessel).** During systole, the elastic aorta distends to accept 60–70 mL of stroke volume; stored elastic energy is released in diastole, propelling blood forward continuously even as the LV is in diastole. This converts pulsatile LV output into near-continuous peripheral perfusion — critical for coronary (fills in diastole) and cerebral flow. Loss of aortic elasticity (ageing, atherosclerosis) increases pulse pressure, transmits excessive pulsatile stress to small vessels → cerebral small-vessel disease, glomerular injury.[^guyton-hall]

**Vascular tone regulation.** The arteriolar media controls capillary bed perfusion by adjusting lumen diameter:
- Myogenic response: ↑intraluminal pressure → SMC stretch → voltage-gated Ca²⁺ channel → contraction (autoregulation in brain, kidney, heart).
- Neural: sympathetic α₁AR tone sets basal SVR; withdrawal → vasodilation (e.g., skeletal muscle during exercise).
- Endocrine: catecholamines, angiotensin II, vasopressin → vasoconstriction; ANP, BNP, eNOS-NO, PGI₂ → vasodilation.
- Metabolic: adenosine, CO₂, H⁺, K⁺, hypoxia → vasodilation (functional hyperaemia in exercising muscle).

**Endothelial barrier and transport.** The endothelium selectively transports nutrients, hormones, and immune cells across the vessel wall via transcytosis (caveolae) and regulated paracellular permeability (VE-cadherin, tight junctions). During inflammation, cytokine-driven opening of paracellular pores (histamine, VEGF, thrombin → VE-cadherin phosphorylation) increases permeability → oedema.[^alberts-mol-cell-biology]

**Atherogenesis (mechanistic sequence).**
1. Endothelial activation at disturbed-flow sites → NF-κB → VCAM-1/ICAM-1/MCP-1 expression → monocyte adhesion and transmigration.
2. Subendothelial LDL retention (proteoglycan binding) → oxidation by MPO/lipoxygenase/LOX-1 → oxLDL.
3. Macrophage differentiation → foam cell via SR-A1/CD36-mediated oxLDL uptake → cholesterol ester (CE) droplet accumulation → necrotic core formation upon apoptosis.
4. T-cell (Th1 → IFN-γ, TNF-α) and mast cell activation → SMC inhibition, ↑MMP secretion.
5. Medial SMC migration into intima → proliferation → fibrous cap synthesis (type I/III collagen).
6. Plaque vulnerability: thin fibrous cap (<65 µm), large necrotic core, ↑MMP-2/9 (matrix metalloproteinases degrade cap collagen) → cap rupture → thrombus → ACS, stroke.[^guyton-hall]

## Connections

- `part-of` → **[Cardiovascular System](../../07-system/cardiovascular-system/README.md)** — arterial wall provides structural integrity and vasoregulatory function; tunica media SMC tone determines SVR; Windkessel elastin in aorta sustains diastolic pressure for continuous coronary perfusion.
- `modulates` → **[Nitric Oxide](../../03-molecular/nitric-oxide/README.md)** — endothelial eNOS produces NO under shear stress → SMC sGC→cGMP→MLCP→vasodilation; disturbed shear at atherosclerosis-prone sites reduces eNOS activity and promotes oxidative NO scavenging.
- `modulates` → **[Cholesterol](../../03-molecular/cholesterol/README.md)** — subendothelial LDL retention and oxidation (MPO/lipoxygenase/LOX-1) in tunica intima initiates atherogenesis; macrophage SR-A1/CD36 oxLDL uptake forms foam cells; statins reduce intimal LDL accumulation.
- `modulates` → **[Macrophage](../../04-cellular/macrophage/README.md)** — monocytes cross activated endothelium via VCAM-1/MCP-1 and become plaque macrophages; foam cells form the necrotic core; MMP-2/9 degrade fibrous cap collagen → cap thinning → plaque rupture risk.
- `contains` → **[Smooth Muscle Cell](../../04-cellular/smooth-muscle-cell/README.md)** — SMC dominate the tunica media; phenotypic switching from contractile to synthetic SMC initiates atherogenesis; hypertension → SMC hypertrophy + collagen deposition → stiffening; SMC apoptosis in the fibrous cap → cap thinning → plaque vulnerability and rupture.
- `contains` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — endothelial cells line the tunica intima; under laminar shear → eNOS-NO + PGI₂ + thrombomodulin → anti-thrombotic, anti-inflammatory state; disturbed flow → NF-κB → VCAM-1/ICAM-1/MCP-1 → monocyte adhesion → atherogenesis at predisposed sites.
- `connects-to` → **[Atherosclerosis](../../07-system/atherosclerosis/README.md)** — the arterial wall is the primary site of atherogenesis; endothelial dysfunction → LDL retention and oxidation in tunica intima → foam cell necrotic core; fibrous cap thinning by MMP-2/9 → rupture → thrombus → ACS and stroke; statins + antiplatelet therapy are standard prevention.

## Pathology

**Atherosclerosis.** Lipid-driven, fibro-inflammatory plaque disease initiated at disturbed-flow sites (coronary bifurcations, carotid sinus, aorto-iliac junction). Foam cell necrotic core + thin fibrous cap → plaque rupture → thrombus → myocardial infarction, ischaemic stroke, mesenteric ischaemia. Risk factors: ↑LDL-C, smoking (↑oxLDL, ↑VCAM-1), hypertension (↑shear-mediated damage), diabetes (↑AGE-RAGE → ↑NF-κB). Management: statins (↓LDL, plaque stabilisation via ↑cap collagen, ↓MMP), PCSK9 inhibitors, antiplatelet therapy, revascularisation (PCI, CABG).[^guyton-hall]

**Hypertensive vascular remodelling.** Chronic ↑wall stress → medial SMC hypertrophy + ↑collagen deposition → ↑wall thickness (↓r/h ratio → ↓wall stress, adapts) + ↑stiffness → ↑PP → ↑LV afterload → LV hypertrophy → heart failure with preserved ejection fraction (HFpEF). Small-vessel remodelling (arteriolar wall thickening) amplifies BP elevation (structural autoregulation shift).

**Aortic aneurysm.** Elastin degradation by macrophage MMP-2/9, inflammatory infiltration → ↑aortic diameter → Laplace: larger r → ↑wall stress → progressive dilation → rupture. Abdominal aortic aneurysm (AAA): repair indicated at >5.5 cm (EVAR or open surgery); screening by ultrasound in men >65 who smoked. Thoracic aortic aneurysm: associated with Marfan syndrome (FBN1 → ↓fibrillin-1 + ↑TGF-β → aortic root dilation → type A dissection), bicuspid aortic valve, hypertension.

**Vasculitis.** Immune-mediated arterial wall inflammation: Takayasu arteritis (large vessel, granulomatous, young women, ↑ESR, ↑CRP, subclavian/aortic involvement); Giant cell arteritis (temporal artery, >50 yr, ↑CRP, headache, jaw claudication, blindness risk → urgent high-dose steroids); Kawasaki disease (medium vessel, children, coronary artery aneurysms, mucocutaneous syndrome → IV immunoglobulin + aspirin); polyarteritis nodosa (medium vessel, ANCA-negative, renal/mesenteric arteries, p-ANCA in microscopic polyangiitis).

**Marfan syndrome.** FBN1 mutation → defective fibrillin-1 → impaired elastin assembly + ↑TGF-β signalling → progressive aortic root dilation → type A aortic dissection. Management: losartan (TGF-β blockade), β-blockers (↓dP/dt), prophylactic aortic root replacement at >4.5–5.0 cm.

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
