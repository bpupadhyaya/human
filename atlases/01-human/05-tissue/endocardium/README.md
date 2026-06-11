---
schema: human-scale-entry/v1
id: endocardium
name: Endocardium
atlas: 01-human
scale: 05-tissue
status: draft
last_reviewed: 2026-06-03
summary: "Innermost lining of all four cardiac chambers and valves — a blood-contacting endothelial monolayer and paracrine hub (ET-1, NO) modulating subjacent cardiomyocytes. Embryological origin of valves via EndMT. Site of infective endocarditis and Loeffler endocarditis."
aliases: ["cardiac endothelium", "endocardial endothelium"]
sources:
  - id: brutsaert-2003-endocardial-endothelium
    type: peer-reviewed
    cite: "Brutsaert DL. Cardiac endothelial-myocardial signaling: its role in cardiac growth, contractile performance, and rhythmicity. Physiol Rev. 2003;83(1):59-115."
    doi: "10.1152/physrev.00017.2002"
    pmid: "12506127"
    url: "https://doi.org/10.1152/physrev.00017.2002"
  - id: openstax-anatomy-19-1
    type: textbook
    cite: "OpenStax. Anatomy & Physiology 2e, Ch. 19.1: Heart Anatomy."
    url: "https://openstax.org/books/anatomy-and-physiology-2e/pages/19-1-heart-anatomy"
    accessed: "2026-06-03"
cross_links:
  - target: 01-human/06-organ/heart
    relation: part-of
    note: "The endocardium is the innermost wall layer of the heart, lining all four chambers and the valve leaflets."
  - target: 01-human/05-tissue/myocardium
    relation: connects-to
    note: "Endocardial endothelium sits directly above the subendocardial layer and myocardium; paracrine mediators (NO, ET-1, NRG-1) cross the short distance to regulate cardiomyocyte contractility and lusitropy; endocardial injury (eosinophils, inflammation) → myocardial dysfunction."
  - target: 01-human/05-tissue/cardiac-conduction-system
    relation: contains
    note: "Purkinje fibers run through the subendocardial layer — the inner connective tissue zone of the endocardium; Purkinje cells deliver the cardiac impulse to working cardiomyocytes; endocardium is the anatomical housing of the distal conduction network."
  - target: 01-human/03-molecular/endothelin-1
    relation: connects-to
    note: "Endocardial ECs secrete ET-1 in response to shear stress, thrombin, and hypoxia → ETA/ETB on cardiomyocytes → positive inotropy and coronary vasoconstriction; ET-1 promotes cardiac hypertrophy; endotheliins amplify myocardial remodeling in heart failure."
  - target: 01-human/03-molecular/nitric-oxide
    relation: connects-to
    note: "Endocardial eNOS → NO → cGMP → PKG → negative inotropy and positive lusitropy in cardiomyocytes; NO modulates L-type Ca²⁺ channels and RyR2; endocardial NO contributes to the Frank-Starling response; eNOS uncoupling in inflammation reduces NO → impaired cardiac relaxation."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "TGF-β drives EndMT during cardiac valve formation; TGF-β → SMAD2/3 → endothelial cells gain mesenchymal invasion → endocardial cushion remodelling into valve leaflets; pathological EndMT reactivation contributes to calcific aortic valve disease and myxomatous mitral degeneration."
  - target: 01-human/04-cellular/cardiomyocyte
    relation: connects-to
    note: "Endocardial endothelium lies ≤5 µm from cardiomyocytes; ET-1, NO, NRG-1, and PGI₂ regulate cardiomyocyte contractility via paracrine signalling; Loeffler endocarditis → endocardial damage → restrictive cardiomyopathy; NRG-1 activates ErbB4 on cardiomyocytes → survival."
---

# Endocardium

## Overview

The endocardium is the **innermost tissue layer of the heart**, lining all four chambers (right atrium, right ventricle, left atrium, left ventricle), the valve leaflets and their tendinous attachments, and the papillary muscles. It is continuous with the endothelium of the great vessels (aorta, pulmonary artery, pulmonary veins, venae cavae) — a single, uninterrupted endothelial lining that interfaces with blood throughout the cardiovascular system [^openstax-anatomy-19-1].

The endocardium is not merely a passive lining. It is an active signaling layer that communicates continuously with the underlying myocardium through paracrine mediators, modulates contraction and relaxation, and serves as the embryological progenitor of the cardiac valves [^brutsaert-2003-endocardial-endothelium].

## Structure

### Layers

The endocardium consists of two distinct layers:

1. **Endocardial endothelium (innermost):** A single monolayer of flat, squamous endothelial cells directly facing the cardiac blood pool. Morphologically similar to vascular endothelium but with distinct gene expression patterns (higher expression of cardiac-specific transcription factors during development; distinct mechanosensing profile due to bidirectional blood-wall shear stresses during filling and ejection).

2. **Subendocardial layer:** Below the endothelium lies a thin layer of connective tissue (collagen, elastic fibers, smooth muscle cells, small vessels) that contains:
   - The **Purkinje fiber network** — the distal branches of the cardiac conduction system (see [Cardiac Conduction System](../cardiac-conduction-system/README.md))
   - Small coronary branches supplying the inner one-third of the myocardium
   - Fibroblasts and occasional adipocytes

| Layer | Composition | Function |
|:---|:---|:---|
| **Endothelium** | Endothelial cells, tight junctions | Blood-tissue barrier; paracrine signaling; thromboresistance |
| **Subendocardium** | Connective tissue, Purkinje fibers, vessels | Mechanical support; conduction pathway; coronary supply to inner wall |

### Valve Leaflets

The four cardiac valves (tricuspid, mitral, pulmonary, aortic) are **specialized endocardial structures** — folds of endocardium enclosing a connective tissue core (spongiosa, fibrosa, ventricularis layers), populated by **valve interstitial cells** (VICs, quiescent fibroblast-like cells) and covered on both surfaces by **valve endothelial cells** (VECs). VECs have distinct gene expression from endocardial endothelium elsewhere, adapted to the unique shear stress and pressure environments of valve surfaces.

## Function

### Blood-Contacting Barrier and Thromboresistance

The endocardial endothelium maintains **thromboresistance** through:
- Continuous prostacyclin (PGI₂) and nitric oxide (NO) production — both potent platelet aggregation inhibitors and vasodilators
- Heparan sulfate proteoglycans (activating antithrombin III)
- Thrombomodulin expression (converts thrombin from a procoagulant to an activator of protein C, which inactivates clotting factors Va and VIIIa)

Disruption of the endocardium (by infection, trauma, turbulent flow) exposes the subendocardial matrix and triggers platelet adhesion and fibrin deposition — the basis of **infective endocarditis** (bacterial colonization on disrupted valve endocardium) and thromboembolism.

### Paracrine Signaling to Cardiomyocytes

The proximity of endocardial endothelial cells to subjacent cardiomyocytes (as close as 1–5 µm in some regions) enables paracrine regulation of myocardial function [^brutsaert-2003-endocardial-endothelium]:

| Mediator | Produced by | Effect on cardiomyocytes |
|:---|:---|:---|
| **Nitric oxide (NO)** | eNOS activation | Negative inotropy via cGMP/PKG; positive lusitropy (faster relaxation); modulates L-type Ca²⁺ channel and RyR2 |
| **Endothelin-1 (ET-1)** | Endocardial ECs | Positive inotropy; vasoconstriction of coronary vessels; promotes hypertrophy |
| **Prostaglandins (PGE₂, PGI₂)** | Endocardial ECs | Modulate contractility, platelet function, and vascular tone |
| **Neuregulin-1 (NRG-1)** | Endocardial ECs | Activates ErbB2/ErbB4 on cardiomyocytes → promotes survival, hypertrophy (physiological) |

This signaling network means that endocardial injury — as in inflammatory conditions — does not merely affect the lining itself but alters the contractile state of the subjacent myocardium.

### Embryological Origin of Valves (EndMT)

During cardiac development, specialized regions of the endocardium undergo **endocardial-to-mesenchymal transition (EndMT)**: endothelial cells lose their endothelial identity, gain migratory and invasive mesenchymal properties, and populate the endocardial cushions that remodel into the four cardiac valves. This process, driven by TGF-β and NOTCH signaling, is recapitulated (pathologically) in adult life during valve disease — particularly calcific aortic stenosis and myxomatous mitral valve disease, where VICs undergo pathological re-activation of EndMT-like programs.

## Connections

- `part-of` → **[Heart](../../06-organ/heart/README.md)** — The endocardium is the innermost layer of the heart wall, continuous across all four chambers and all valve surfaces.
- `connects-to` → **[Myocardium](../myocardium/README.md)** — Endocardial endothelium sits directly above the subendocardial layer and myocardium; paracrine mediators (NO, ET-1, NRG-1) cross the short distance to regulate cardiomyocyte contractility and lusitropy; endocardial injury (eosinophils, inflammation) → myocardial dysfunction.
- `contains` → **[Cardiac Conduction System](../cardiac-conduction-system/README.md)** — Purkinje fibers run through the subendocardial layer — the inner connective tissue zone of the endocardium; Purkinje cells deliver the cardiac impulse to working cardiomyocytes; endocardium is the anatomical housing of the distal conduction network.
- `connects-to` → **[Endothelin-1](../../03-molecular/endothelin-1/README.md)** — Endocardial ECs secrete ET-1 in response to shear stress, thrombin, and hypoxia → ETA/ETB on cardiomyocytes → positive inotropy and coronary vasoconstriction; ET-1 promotes cardiac hypertrophy; endotheliins amplify myocardial remodeling in heart failure.
- `connects-to` → **[Nitric Oxide](../../03-molecular/nitric-oxide/README.md)** — Endocardial eNOS → NO → cGMP → PKG → negative inotropy and positive lusitropy in cardiomyocytes; NO modulates L-type Ca²⁺ channels and RyR2; endocardial NO contributes to the Frank-Starling response; eNOS uncoupling in inflammation reduces NO → impaired cardiac relaxation.
- `connects-to` → **[TGF-β](../../03-molecular/tgf-beta/README.md)** — TGF-β drives EndMT during cardiac valve formation; TGF-β → SMAD2/3 → endothelial cells gain mesenchymal invasion → endocardial cushion remodelling into valve leaflets; pathological EndMT reactivation contributes to calcific aortic valve disease and myxomatous mitral degeneration.
- `connects-to` → **[Cardiomyocyte](../../04-cellular/cardiomyocyte/README.md)** — Endocardial endothelium lies ≤5 µm from cardiomyocytes; ET-1, NO, NRG-1, and PGI₂ regulate cardiomyocyte contractility via paracrine signalling; Loeffler endocarditis → endocardial damage → restrictive cardiomyopathy; NRG-1 activates ErbB4 on cardiomyocytes → survival.

## Pathology

| Disease | Endocardium mechanism |
|:---|:---|
| **Infective endocarditis (IE)** | Bacterial colonization of disrupted valve endocardium (turbulent flow, prior damage). Common organisms: *S. viridans* (damaged valves), *S. aureus* (structurally normal valves). Vegetation = fibrin-platelet matrix with embedded bacteria on valve surface. |
| **Loeffler endocarditis** | Eosinophilic infiltration and endocardial damage (from major basic protein and eosinophil peroxidase released by activated eosinophils). Produces restrictive cardiomyopathy. Associated with hypereosinophilic syndrome. |
| **Non-bacterial thrombotic endocarditis (NBTE, marantic endocarditis)** | Sterile fibrin-platelet vegetations on valve endocardium in cachexia, malignancy, or hypercoagulable states. Major embolic risk without infection. |
| **Endocardial fibroelastosis (EFE)** | Abnormal collagen and elastin deposition in the endocardium — most often a complication of congenital heart disease (aortic stenosis, HLHS) or viral infection in infancy. Produces stiff, thickened inner wall, restricting filling. |

## Open Questions

- **EndMT in adult valve disease.** Can EndMT inhibition (NOTCH activators, TGF-β blockade) prevent or reverse early calcific valve disease?
- **Endocardial NO regulation of arrhythmia.** Whether endocardial-derived NO directly modulates the electrical coupling of Purkinje fibers to working cardiomyocytes is not fully characterized.
- **Endocardial heterogeneity across chambers.** Single-cell RNA-seq data from human hearts reveals distinct endocardial endothelial subpopulations in each chamber and valve — the functional consequences of this diversity are only beginning to be understood.

## See Also

- [Heart](../../06-organ/heart/README.md)
- [Myocardium](../myocardium/README.md)
- [Cardiac Conduction System](../cardiac-conduction-system/README.md)

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^brutsaert-2003-endocardial-endothelium]: Brutsaert DL. Cardiac endothelial-myocardial signaling. *Physiol Rev.* 2003;83(1):59-115. [doi:10.1152/physrev.00017.2002](https://doi.org/10.1152/physrev.00017.2002) · [PubMed 12506127](https://pubmed.ncbi.nlm.nih.gov/12506127/)
[^openstax-anatomy-19-1]: OpenStax. *Anatomy & Physiology 2e*, Ch. 19.1: Heart Anatomy. [Read online →](https://openstax.org/books/anatomy-and-physiology-2e/pages/19-1-heart-anatomy)
