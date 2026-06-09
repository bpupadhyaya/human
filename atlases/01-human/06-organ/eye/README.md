---
schema: human-scale-entry/v1
id: eye
name: Eye
atlas: 01-human
scale: 06-organ
status: draft
last_reviewed: 2026-06-06
summary: "Paired visual organ (~24 mm diameter); converts light into neural signals via rods (scotopic) and cones (photopic/color) in the retina. Outer tunic: cornea/sclera; uvea: iris/ciliary body/choroid; retina: 10 neural layers. ~1 million axons per optic nerve."
aliases: ["ocular organ", "eyeball", "globe", "oculus", "visual organ"]
sources:
  - id: kolb-webvision
    type: regulatory
    cite: "Kolb H, Fernandez E, Nelson R, eds. Webvision: The Organization of the Retina and Visual System. University of Utah Health Sciences; 2011."
    url: "https://webvision.med.utah.edu/"
    accessed: "2026-06-06"
  - id: forrester-eye-basic-sciences
    type: textbook
    cite: "Forrester JV, Dick AD, McMenamin PG, Roberts F, Pearlman E. The Eye: Basic Sciences in Practice. 4th ed. Elsevier; 2015."
    url: "https://www.elsevier.com/books/the-eye/forrester/978-0-7020-5554-6"
    accessed: "2026-06-06"
  - id: purves-neuroscience
    type: textbook
    cite: "Purves D, Augustine GJ, Fitzpatrick D, et al. Neuroscience. 6th ed. Sinauer Associates; 2018."
    url: "https://www.sinauer.com/neuroscience"
    accessed: "2026-06-06"
cross_links:
  - target: 01-human/04-cellular/neuron
    relation: contains
    note: "The retina contains ~6 million cone photoreceptors and ~120 million rod photoreceptors (specialized neurons), plus bipolar, amacrine, horizontal, and ~1 million retinal ganglion cells whose axons form the optic nerve."
  - target: 01-human/07-system/nervous-system
    relation: part-of
    note: "The retina is developmental brain tissue (diencephalon outgrowth); the optic nerve is a CNS tract (not peripheral nerve); the visual pathway extends from retina through LGN to primary visual cortex (V1). The eye is functionally part of the CNS visual system."
  - target: 01-human/07-system/diabetic-retinopathy
    relation: connects-to
    note: "Diabetic retinopathy targets the retina: pericyte loss → microaneurysms → exudates → macular edema → neovascularization → vitreous hemorrhage → tractional retinal detachment; foveal photoreceptors are most critical for central vision and most vulnerable to DME-driven damage."
  - target: 01-human/03-molecular/factor-h
    relation: connects-to
    note: "Factor H Y402H (SCR7; ~35% of Europeans) → reduced Bruch membrane heparan sulfate binding → local complement dysregulation → drusen accumulation → AMD; Y402H homozygotes have ~7× relative AMD risk; pegcetacoplan (C3 inhibitor) approved for geographic atrophy in AMD (FDA 2023)."
---

# Eye

## Overview

The eye is the **primary sensory organ for vision** — converting electromagnetic radiation (light, 380–760 nm) into electrochemical neural signals that are processed by the brain into visual percepts. Paired structures, each approximately 24 mm in anterior-posterior diameter and weighing ~7.5 g, the eyes are housed in the bony orbits of the skull, connected to the brain via the **optic nerves** (cranial nerve II), and controlled by six extraocular muscles per orbit [^forrester-eye-basic-sciences].

Approximately **80% of all sensory information** processed by the human brain is visual in origin, reflecting the extraordinarily high neural investment in vision — roughly 30% of the cerebral cortex is devoted to visual processing (compared to ~8% for somatosensation and ~3% for audition).

The retina — the light-sensitive neural tissue lining the posterior globe — is developmentally derived from the **diencephalon** (embryonic brain), making the eye a direct outgrowth of the central nervous system. The optic nerve is histologically a CNS tract (surrounded by meninges, not a peripheral nerve sheath), and elevated intracranial pressure transmits directly to the optic nerve head (papilledema).

## Structure

### Ocular Layers (Tunics)

The eye is organized into three concentric layers [^kolb-webvision]:

**Outer fibrous tunic:**
- **Cornea** (anterior 1/6): Transparent, avascular, 5-layered structure (~0.5–0.6 mm central thickness). Layers: epithelium (6–7 cell stratified squamous; rapidly regenerating, 5–7 day turnover) → Bowman's layer (acellular condensed collagen; does not regenerate) → Stroma (~90% of corneal thickness; highly ordered orthogonal collagen I fibrils in a keratan sulfate PG matrix → transparency via destructive interference of scattered light) → Descemet's membrane (thick basement membrane) → Endothelium (single layer; ~3,500–4,000 cells/mm²; pump Na⁺/K⁺-ATPase drives water out → corneal dehydration → transparency; non-regenerating in humans). The cornea is responsible for **~70% of the eye's total refractive power** (~43 diopters).
- **Sclera** (posterior 5/6): Opaque, white, tough fibrous coat (collagen I; irregular arrangement → opaque unlike cornea); provides structural rigidity; attachment point for extraocular muscles; contains intrascleral aqueous humor drainage channels.

**Middle vascular tunic (Uvea):**
- **Iris**: Pigmented diaphragm; regulates pupil diameter (sphincter pupillae: parasympathetic/muscarinic → miosis; dilator pupillae: sympathetic/α₁ → mydriasis); pupil size modulates retinal light exposure (2–8 mm diameter range = 16-fold light adjustment).
- **Ciliary body**: Produces aqueous humor (non-pigmented ciliary epithelium via active secretion and ultrafiltration, ~2–3 μL/min); contains ciliary muscle (smooth muscle; contracts → zonule relaxation → lens rounds → ↑power → near accommodation; parasympathetic innervation via CN III, muscarinic).
- **Choroid**: Highly vascularized; supplies outer retina (photoreceptors) via diffusion (retina lacks its own capillaries in the outer layers); contains Bruch's membrane adjacent to RPE.

**Inner neural tunic:**
- **Retina**: Described in detail below.

### The Retina — 10-Layer Structure

| Layer (outermost to innermost) | Contents |
|:---|:---|
| **Retinal Pigment Epithelium (RPE)** | Monolayer; outer blood-retinal barrier; phagocytoses shed photoreceptor outer segments; visual cycle (retinal recycling); secretes VEGF (basal) and PEDF (apical) |
| **Photoreceptor outer segments** | Rod and cone outer segment discs containing opsin pigments |
| **Photoreceptor inner segments** | Metabolic machinery; mitochondria-rich |
| **External limiting membrane** | Adherens junctions between Müller glia and photoreceptors |
| **Outer nuclear layer (ONL)** | Rod and cone cell bodies (~126 million photoreceptors total) |
| **Outer plexiform layer (OPL)** | Synapses: photoreceptor → bipolar and horizontal cell contacts |
| **Inner nuclear layer (INL)** | Bipolar cells, horizontal cells, amacrine cells, Müller glia cell bodies |
| **Inner plexiform layer (IPL)** | Synapses: bipolar cell and amacrine cell → retinal ganglion cell contacts |
| **Retinal ganglion cell layer (GCL)** | ~1.2 million retinal ganglion cells (RGCs); axons exit as optic nerve |
| **Nerve fiber layer (NFL)** | RGC axons sweeping to optic disc |

**Photoreceptors [^kolb-webvision]:**
- **Rods**: ~120 million; distributed across the peripheral retina; absent from fovea; contain **rhodopsin** (opsin + 11-cis retinal); spectral peak ~498 nm; scotopic (dim light) vision; single photon detection; saturate in daylight.
- **Cones**: ~6–7 million; concentrated in the central retina (**fovea centralis** contains ~50,000 cones in ~0.35 mm diameter, no rods); three types: S-cones (short/blue, ~420 nm peak, ~5%), M-cones (medium/green, ~530 nm, ~32%), L-cones (long/red, ~560 nm, ~63%); photopic (daylight) vision; color vision via opponent-color processing.

### Lens, Vitreous, and Aqueous Compartments

**Crystalline lens**: Biconvex, avascular, ~10 mm diameter; entirely enclosed in a capsule; composed of lens fiber cells (filled with crystallins — water-soluble proteins maintaining transparency); accommodates by changing shape (young lens: ~14 diopter accommodation range; presbyopia by age 45–50 from increasing lens rigidity). Zonule fibers (derived from ciliary body) suspend the lens.

**Vitreous humor**: Posterior segment gel filling ~80% of globe volume; 99% water, type II collagen fibrils + hyaluronic acid; optically clear; provides structural support; no turnover in adults (degenerates with age → floaters → posterior vitreous detachment).

**Aqueous humor**: Clear fluid filling anterior and posterior chambers (~0.25 mL); produced by ciliary epithelium → posterior chamber → pupil → anterior chamber → trabecular meshwork drainage → Schlemm's canal → episcleral veins. Intraocular pressure (IOP) = 10–21 mmHg. Outflow resistance at trabecular meshwork is the primary determinant of IOP.

## Function

### Phototransduction

The visual signal cascade in rods [^purves-neuroscience]:

1. **Dark state**: Cyclic GMP (cGMP) keeps CNG (cyclic nucleotide-gated) channels open → Na⁺/Ca²⁺ influx → depolarized membrane potential (~-40 mV) → continuous glutamate release from photoreceptor terminal.
2. **Photon absorption**: 11-cis retinal isomerizes → all-trans retinal → conformational change in opsin → activated rhodopsin (R*).
3. **G protein amplification**: R* activates ~500 transducin (Gαt) molecules → each activates a phosphodiesterase (PDE6) → PDE6 hydrolyzes cGMP → cGMP ↓.
4. **Channel closure**: CNG channels close → reduced Na⁺ influx → hyperpolarization (-70 mV) → reduced glutamate release.
5. **Signal transmission**: Reduced glutamate → bipolar cell activation (ON-bipolar: depolarize; OFF-bipolar: hyperpolarize) → retinal ganglion cell → optic nerve action potentials → lateral geniculate nucleus (LGN) → primary visual cortex (V1, area 17).
6. **Recovery**: R* inactivation by rhodopsin kinase (GRK1) + arrestin; PDE6 inactivation; cGMP resynthesis by guanylyl cyclase (GC); visual cycle: all-trans retinal → all-trans retinol → transport to RPE → 11-cis retinal regeneration → return to rod outer segment.

### Accommodation and Depth of Focus

Near focus (accommodation): parasympathetic CN III → ciliary muscle contraction → zonule tension decreases → lens rounds → refractive power increases (up to +14 diopters in young adults) → near objects focused on fovea. **Presbyopia**: progressive loss after ~40 years due to increasing lens crystallin cross-linking and reduced elasticity.

### Aqueous Humor Dynamics and IOP

Intraocular pressure homeostasis: production rate = outflow rate at IOP equilibrium. IOP depends on: (1) ciliary body secretion rate, (2) trabecular meshwork outflow resistance, (3) uveoscleral outflow. Normal IOP: 10–21 mmHg. Elevated IOP (>21 mmHg) is the primary modifiable risk factor for glaucomatous optic neuropathy.

## Connections

- `contains` → **[Neuron](../../04-cellular/neuron/README.md)** — ~6 million cones, ~120 million rods, and ~1.2 million retinal ganglion cells are the photoreceptor and output neurons of the retina; the optic nerve carries ~1 million axons to the LGN
- `part-of` → **[Nervous System](../../07-system/nervous-system/README.md)** — the retina is developmentally diencephalic; the optic nerve is a CNS tract; the eye is the sensory peripheral component of the CNS visual system
- `connects-to` → **[Diabetic Retinopathy](../../07-system/diabetic-retinopathy/README.md)** — Diabetic retinopathy targets the retina: pericyte loss → microaneurysms → exudates → macular edema → neovascularization → vitreous hemorrhage → tractional retinal detachment; foveal photoreceptors are most critical for central vision and most vulnerable to DME-driven damage.
- `connects-to` → **[Factor H](../../03-molecular/factor-h/README.md)** — Factor H Y402H (SCR7; ~35% of Europeans) → reduced Bruch membrane heparan sulfate binding → local complement dysregulation → drusen accumulation → AMD; Y402H homozygotes have ~7× relative AMD risk; pegcetacoplan (C3 inhibitor) approved for geographic atrophy in AMD (FDA 2023).

## Pathology

### Age-Related Macular Degeneration (AMD)

Most common cause of irreversible vision loss in adults >50 in high-income countries. **Dry AMD**: geographic atrophy of RPE → cone photoreceptor death in the macula → central scotoma. **Wet AMD**: subretinal neovascularization (CNV) — VEGF-driven; rapid vision loss from hemorrhage and exudate. Anti-VEGF (ranibizumab, aflibercept, bevacizumab) injections have revolutionized wet AMD treatment. Drusen (extracellular deposits beneath RPE/Bruch's membrane) are the hallmark of early AMD.

### Glaucoma

Optic neuropathy characterized by progressive loss of RGC axons → visual field defects → blindness if untreated. ~80 million people affected worldwide; #1 cause of irreversible blindness globally. **Primary open-angle glaucoma (POAG)**: elevated IOP → mechanical optic nerve head damage + impaired axoplasmic flow → RGC apoptosis. Treatment: IOP-lowering (prostaglandin analogues, β-blockers, carbonic anhydrase inhibitors, alpha-2 agonists, mesh trabecular stents, trabeculectomy).

### Diabetic Retinopathy (DR)

Most common cause of blindness in working-age adults in high-income countries. Hyperglycemia → pericyte loss → microaneurysms → non-proliferative DR → ischemia → VEGF↑ → proliferative DR (neovascularization → vitreous hemorrhage, tractional retinal detachment). Pan-retinal photocoagulation (PRP) + anti-VEGF for proliferative DR; anti-VEGF/steroids for diabetic macular edema (DME).

### Cataracts

Opacification of the crystalline lens; #1 cause of reversible blindness globally (~50% of blindness). UV exposure, oxidative stress, steroid use, diabetes → crystallin protein aggregation → light scattering. Phacoemulsification with intraocular lens (IOL) implantation: one of the most common and cost-effective surgical procedures globally.

### Herpesvirus Ocular Disease

HSV-1 keratitis is the leading cause of infectious corneal blindness in high-income countries; HSV stromal keratitis (immune-mediated) causes scarring and loss of transparency. VZV ophthalmicus (herpes zoster V1 dermatomal reactivation) → acute retinal necrosis. CMV retinitis in HIV/AIDS (CD4 <50) → full-thickness retinal necrosis → retinal detachment.

[^kolb-webvision]: Kolb H, Fernandez E, Nelson R, eds. *Webvision: The Organization of the Retina and Visual System.* University of Utah Health Sciences; 2011. [webvision.med.utah.edu](https://webvision.med.utah.edu/)
[^forrester-eye-basic-sciences]: Forrester JV, Dick AD, McMenamin PG, Roberts F, Pearlman E. *The Eye: Basic Sciences in Practice.* 4th ed. Elsevier; 2015.
[^purves-neuroscience]: Purves D et al. *Neuroscience.* 6th ed. Sinauer Associates; 2018.

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
