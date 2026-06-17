---
schema: human-scale-entry/v1
id: diffuse-midline-glioma
name: Diffuse Midline Glioma
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-07
summary: "Diffuse midline glioma (H3K27M+) is a WHO Grade 4 pediatric/young adult brain tumor defined by H3K27M mutation; DIPG, thalamic, and spinal cord locations; median OS 12-15 months; ONC201 (imipridone) FDA-approved for relapsed/refractory H3K27M+ DMG; no curative systemic therapy."
aliases: ["DMG", "diffuse midline glioma", "DIPG", "diffuse intrinsic pontine glioma", "H3K27M glioma", "thalamic glioma H3K27M", "H3K27M-altered glioma", "pediatric midline glioma", "pontine glioma", "H3.3K27M brain tumor"]
sources:
  - id: schwartzentruber-2012-h3f3a-glioma
    type: peer-reviewed
    cite: "Schwartzentruber J, Korshunov A, Liu XY, et al. Driver mutations in histone H3.3 and chromatin remodelling genes in paediatric glioblastoma. Nature. 2012;482(7384):226-231."
    doi: "10.1038/nature10833"
    pmid: "22286061"
    url: "https://doi.org/10.1038/nature10833"
  - id: khuong-quang-2012-h3k27m-dipg
    type: peer-reviewed
    cite: "Khuong-Quang DA, Buczkowicz P, Rakopoulos P, et al. K27M mutation in histone H3.3 defines clinically and biologically distinct subgroups of pediatric diffuse intrinsic pontine gliomas. Acta Neuropathol. 2012;124(3):439-447."
    doi: "10.1007/s00401-012-0998-0"
    pmid: "22661320"
    url: "https://doi.org/10.1007/s00401-012-0998-0"
cross_links:
  - target: 01-human/03-molecular/h3k27m
    relation: connects-to
    note: "H3K27M mutation in H3F3A or HIST1H3B defines WHO Grade 4 diffuse midline glioma (100% diagnostic criterion since 2021 WHO CNS classification); H3K27M IHC (anti-H3.3K27M, clone D5E7) is the diagnostic standard; TBXT-negative; H3K27M identifies tumor in CSF liquid biopsy."
  - target: 01-human/03-molecular/ezh2
    relation: connects-to
    note: "H3K27M inhibits EZH2/PRC2 activity in trans → global H3K27me3 loss; this dominant-negative epigenetic mechanism is the oncogenic hallmark of DMG; paradoxically, EZH2 protein is intact and overexpressed in H3K27M DMG; panobinostat (HDAC inhibitor) partially restores H3K27me3."
  - target: 01-human/03-molecular/cdkn2a
    relation: connects-to
    note: "CDKN2A deletion in ~15-25% H3K27M DMG (higher in DIPG/thalamic subtypes); NF1+H3K27M co-alteration common in spinal DMG; CDKN2A loss → CDK4/6 → RB1 → E2F proliferation; palbociclib + ONC201 combination being explored in H3K27M+CDKN2A-deleted DMG."
  - target: 01-human/03-molecular/pdgf
    relation: connects-to
    note: "PDGFRA point mutations and amplification occur in ~25-35% of H3K27M DMG; PDGFRA → MAPK/PI3K → glioma proliferation; PDGFRA co-mutation with H3K27M accelerates malignancy; avapritinib and imatinib explored in PDGFRA-mutant DMG subsets."
  - target: 01-human/03-molecular/nf1
    relation: connects-to
    note: "NF1 mutations in ~10% of H3K27M DMG, enriched at spinal cord location; NF1 LOF → constitutive RAS-MAPK → MEK-ERK proliferation; NF1+H3K27M spinal DMG shows high macrophage infiltration; selumetinib and trametinib (MEK inhibitors) explored in NF1-mutant H3K27M spinal DMG."
  - target: 01-human/03-molecular/pik3ca
    relation: connects-to
    note: "PIK3CA/PIK3R1 mutations in ~15% of H3K27M DMG; PI3K-AKT-mTOR cooperates with H3K27M epigenetic reprogramming; alpelisib (PI3Kα inhibitor) and copanlisib in combination with ONC201 under investigation; PTEN loss is an alternative PI3K pathway activation mechanism in DMG."
  - target: 01-human/07-system/glioblastoma
    relation: connects-to
    note: "H3K27M DMG and IDH-wildtype GBM are both WHO Grade 4 but molecularly distinct; GBM shows EGFR amplification/EGFRvIII, TERT promoter mutation, CDK4/6 amplification absent in DMG; ONC201 active in DMG but not GBM; bevacizumab benefits GBM (PFS) but not H3K27M DMG."
  - target: 01-human/06-organ/brain
    relation: connects-to
    note: "Diffuse midline glioma grows in the brain's midline — pons (DIPG), thalamus, and spinal cord — where infiltrative spread makes surgery impossible; the pontine location compresses cranial nerve nuclei and long tracts, and radiation is the only treatment that briefly helps."
  - target: 01-human/04-cellular/oligodendrocyte
    relation: connects-to
    note: "DMG arises from oligodendrocyte precursor cells (OPCs) of the developing midline: the H3K27M mutation freezes these cells in a proliferative, stem-like state by stalling differentiation, which is why the tumor peaks at ages 5-10 when OPCs are most active in the pons."
  - target: 01-human/04-cellular/microglia
    relation: connects-to
    note: "The DMG microenvironment is rich in microglia and macrophages, especially NF1-mutant spinal tumors, but these are immunosuppressive rather than tumoricidal — one reason checkpoint inhibitors have largely failed and GD2-directed CAR-T is being explored instead."
  - target: 01-human/07-system/medulloblastoma
    relation: connects-to
    note: "Diffuse midline glioma and medulloblastoma are the two great malignant pediatric brain tumors at opposite poles: DMG is an unresectable, fatal H3 K27M brainstem glioma, while medulloblastoma is a resectable cerebellar tumor often cured by surgery plus craniospinal radiotherapy."
  - target: 01-human/04-cellular/astrocyte
    relation: connects-to
    note: "Diffuse midline glioma arises from an OPC-like glial precursor of the astrocyte/oligodendrocyte lineage: the H3 K27M oncohistone freezes these cells in a stem-like state by collapsing H3K27 methylation, so the tumor infiltrates the pons diffusely rather than forming a mass."
  - target: 01-human/01-subatomic/photon
    relation: connects-to
    note: "Photon radiotherapy is the only treatment that reliably helps diffuse midline glioma: focal irradiation of the pons gives transient symptom relief and a few months' benefit, but the H3 K27M tumor inevitably regrows—no chemo, surgery, or re-irradiation is curative."
  - target: 01-human/07-system/idh-mutant-glioma
    relation: connects-to
    note: "Diffuse midline glioma and IDH-mutant glioma are epigenetically opposite gliomas: DMG's H3 K27M oncohistone collapses methylation in children with dismal outcomes, while adult IDH-mutant gliomas accumulate 2-HG and fare far better—chromatin reprogramming, not oncogenes."
  - target: 01-human/07-system/atypical-teratoid-rhabdoid-tumor
    relation: connects-to
    note: "Diffuse midline glioma and ATRT are aggressive pediatric brain tumors driven by epigenetic dysregulation: DMG by the H3 K27M histone mutation, ATRT by SMARCB1/SWI-SNF loss—both reprogram chromatin and carry a grim prognosis."
  - target: 01-human/04-cellular/neuron
    relation: connects-to
    note: "Diffuse midline glioma forms synapses with neurons to grow: the tumor's OPC-like cells receive glutamatergic input through real neuron-to-glioma synapses that drive proliferation—so neuronal activity feeds the cancer, making activity-blocking drugs a therapeutic idea."
  - target: 01-human/03-molecular/p53
    relation: connects-to
    note: "TP53 mutation frequently accompanies the H3K27M driver in DMG: loss of p53 removes the damage checkpoint atop the epigenetic catastrophe of histone mutation, accelerating this fatal pediatric brainstem tumor—a partnership of epigenetic and tumor-suppressor failure."
  - target: 01-human/03-molecular/cdk4-6
    relation: connects-to
    note: "CDK4/6 amplification helps drive DMG's relentless growth: alongside H3K27M, gains in the cell-cycle machinery push tumor cells past the G1 checkpoint, making CDK4/6 inhibitors one of the targeted strategies tested against this otherwise untreatable tumor."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "DMG often activates the PI3K/AKT/mTOR pathway: mutations in PIK3CA and related genes switch on mTOR-driven growth alongside the H3K27M epigenetic driver, so mTOR-pathway inhibitors are explored as targeted therapy for this lethal midline glioma."
  - target: 01-human/07-system/nervous-system
    relation: connects-to
    note: "Diffuse midline glioma is the deadliest pediatric tumor of the nervous system: it infiltrates the brainstem (as DIPG), thalamus or spinal cord diffusely, so it cannot be resected and disrupts the very structures that control breathing, movement and consciousness."
  - target: 01-human/07-system/li-fraumeni-syndrome
    relation: connects-to
    note: "Germline TP53 loss in Li-Fraumeni syndrome predisposes to midline gliomas: while most diffuse midline gliomas are sporadic H3K27M-driven, the syndrome shows how inherited tumor-suppressor loss can also seed these lethal childhood brain cancers."
  - target: 01-human/01-subatomic/proton
    relation: connects-to
    note: "Proton therapy has been tried in diffuse midline glioma to spare the developing brain: its sharp dose falloff limits collateral damage near the brainstem, but because the tumor infiltrates diffusely and resists treatment, it has not improved the grim prognosis."
  - target: 01-human/05-tissue/synapse
    relation: connects-to
    note: "Diffuse midline glioma hijacks the synapse: tumor cells form real synapses with neurons and grow in response to neuronal activity, so brain electrical signaling literally feeds the cancer—a discovery opening neuroscience-based therapies for this lethal childhood tumor."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "Diffuse midline glioma is a frontier for T-cell therapy: GD2-directed CAR-T cells have shrunk these previously untreatable pontine tumors in early trials, so engineered cytotoxic T cells offer the first real hope against a near-uniformly fatal cancer."
  - target: 01-human/03-molecular/glutamate
    relation: connects-to
    note: "Glutamate drives diffuse midline glioma growth: neuron-released glutamate acting on tumor AMPA receptors stimulates proliferation, so the same excitatory signaling that runs the brain fuels the cancer—making glutamate pathways a therapeutic target."
  - target: 01-human/03-molecular/dopamine
    relation: connects-to
    note: "Diffuse midline glioma's most promising drug works on dopamine signaling: ONC201 (dordaviprone) antagonizes the dopamine D2 receptor (and mitochondrial ClpP) and has produced rare responses in H3K27M tumors, a surprising therapeutic angle in an otherwise fatal cancer."
  - target: 01-human/03-molecular/egfr
    relation: connects-to
    note: "A thalamic subset of diffuse midline glioma is driven by EGFR: bithalamic H3-wildtype midline gliomas carry EGFR mutations rather than H3K27M, so molecular testing splits these tumors into biologically distinct, differently-targetable groups."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "Diffuse midline glioma is a target for NK and cell therapies: because it is so hard to resect or irradiate, engineered NK cells and GD2 CAR-T are being tested to attack the tumor immunologically where surgery and drugs fail."
  - target: 01-human/02-atomic/calcium
    relation: connects-to
    note: "Diffuse midline glioma grows on calcium from neuron-glioma synapses: real synapses form between neurons and tumor cells, and the glutamate-driven calcium influx through them spurs the cancer to proliferate—a striking link between brain activity and tumor growth."
  - target: 01-human/03-molecular/vegf
    relation: connects-to
    note: "Diffuse midline glioma recruits blood supply via VEGF: though infiltrative, the tumor releases VEGF to coax new vessels and loosen the blood-brain barrier, a process studied as a target in a cancer that resists almost all therapy."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "Tumor-associated microglia feed diffuse midline glioma through NF-kB: this inflammatory switch in the brain's immune cells drives cytokines that support the glioma's growth, part of the supportive niche around this lethal pediatric tumor."
  - target: 01-human/06-organ/eye
    relation: connects-to
    note: "Diffuse midline glioma announces itself in the eyes: a pontine tumor first palsies the cranial nerves that move the eyes and face, so double vision, a crossed eye, and facial droop are classic early signs of DIPG."
  - target: 01-human/06-organ/lung
    relation: connects-to
    note: "Diffuse midline glioma ultimately stops the breath: as it destroys the brainstem's control of breathing and swallowing, patients lose airway protection and respiratory drive, the failure that ends this lethal disease."
  - target: 01-human/04-cellular/endothelial-cell
    relation: connects-to
    note: "Diffuse midline glioma works on endothelial cells: VEGF from the tumor loosens the blood-brain barrier these cells form and recruits new vessels, both feeding growth and complicating drug delivery to the brainstem."
  - target: 01-human/06-organ/heart
    relation: connects-to
    note: "Diffuse midline glioma destabilizes the brainstem's autonomic control: infiltrating the pons it disrupts the centers governing heart rate and blood pressure, causing dangerous swings late in the disease."
  - target: 01-human/05-tissue/peripheral-nerve
    relation: connects-to
    note: "Diffuse midline glioma picks off the cranial nerves: invading the pons it palsies the nerves controlling eye movement, the face and swallowing, the cranial-nerve deficits that often herald it."
  - target: 01-human/03-molecular/activin-a
    relation: connects-to
    note: "Some diffuse midline gliomas are driven by activin signaling: ACVR1 mutations switch on the activin-A/BMP pathway, a recurrent driver in the pontine tumors of young children and a drug target."
  - target: 01-human/01-subatomic/electron
    relation: connects-to
    note: "Electron microscopy made a startling discovery: real synapses form between healthy neurons and glioma cells, the neuron's terminal wiring directly onto the tumor — an electrical hijacking that drives the cancer's growth."
  - target: 01-human/02-atomic/potassium
    relation: connects-to
    note: "The tumor plugs into the brain's electricity: glioma cells carry potassium and other ion channels that let them depolarize in response to neuronal firing, the electrical excitability that the neuron-glioma synapse feeds and that spurs invasion."
  - target: 01-human/02-atomic/sodium
    relation: connects-to
    note: "Glutamate from the neuron-glioma synapse pours sodium into the tumor: AMPA-receptor currents flood the glioma cell with sodium and calcium, the depolarizing signal by which neural activity literally powers the cancer's spread."
  - target: 01-human/03-molecular/antibody
    relation: connects-to
    note: "Engineered antibody-based cells offer new hope: GD2-directed CAR-T cells have shrunk H3K27M-mutant diffuse midline gliomas in early trials, the first therapy to dent a tumor that radiation only briefly holds."
  - target: 01-human/06-organ/stomach
    relation: connects-to
    note: "Its pontine home wrecks swallowing: the tumor infiltrates the brainstem's bulbar centers, so dysphagia and impaired airway protection bring aspiration and the need for feeding tubes as the disease advances."
  - target: 01-human/04-cellular/neutrophil
    relation: connects-to
    note: "Radiation and chemotherapy thin the blood: the craniospinal radiation and any added chemotherapy suppress the marrow, dropping neutrophils and raising the infection risk during the months of treatment."
  - target: 01-human/07-system/endocrine-system
    relation: connects-to
    note: "A midline tumor sits beside the master glands: thalamic and pontine gliomas and the radiation aimed at them border the hypothalamus and pituitary, so survivors face deficits of growth, thyroid and sex hormones that need lifelong endocrine follow-up."
  - target: 01-human/03-molecular/myc
    relation: connects-to
    note: "A subset of these gliomas amplify MYC: alongside the defining H3K27M mutation, MYC or PVT1 amplification drives some diffuse midline gliomas, adding a proliferative push that marks particularly aggressive, fast-growing tumors."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: connects-to
    note: "The tumor is immunologically cold: it carries few mutations to flag and recruits regulatory T cells that suppress attack, an immune-evasive microenvironment that has frustrated immunotherapy and shapes the GD2 CAR-T trials now under way."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "TGF-β helps the glioma spread and hide: it drives the diffuse invasion through the brainstem and dampens the local immune response, part of why these tumors are unresectable and immune-resistant."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Macrophages fill the tumor but don't fight it: monocyte-derived macrophages, alongside microglia, dominate the DMG microenvironment in an immunosuppressive state that helps the cancer evade attack."
  - target: 01-human/07-system/neurofibromatosis-type-1
    relation: connects-to
    note: "An NF1 background can seed the glioma: loss of the NF1 tumor suppressor is a recurrent driver of diffuse midline glioma, and the syndrome's lifelong predisposition to gliomas links it to this lethal childhood tumor."
  - target: 01-human/03-molecular/atrx
    relation: connects-to
    note: "ATRX loss often joins the H3K27M hit: especially in thalamic and spinal diffuse midline gliomas, ATRX mutation accompanies the histone mutation, driving alternative lengthening of telomeres and genomic instability."
  - target: 01-human/07-system/epilepsy
    relation: connects-to
    note: "The infiltrating glioma irritates the cortex: as diffuse midline glioma spreads from the pons or thalamus it can trigger seizures, and seizure control is part of the supportive care for these children."
  - target: 01-human/07-system/neuropathic-pain
    relation: connects-to
    note: "Brainstem and spinal infiltration brings pain: tumor invasion of sensory pathways causes neuropathic pain and, in spinal diffuse midline glioma, radicular pain — a symptom burden central to palliative management."
  - target: 01-human/03-molecular/stat3
    relation: connects-to
    note: "STAT3 supports the H3K27M-driven tumor: diffuse midline glioma cells show STAT3 activation that backs proliferation and immune evasion, a pathway studied for this almost uniformly fatal childhood brainstem tumor."
  - target: 01-human/07-system/venous-thromboembolism
    relation: connects-to
    note: "Brain tumors are strongly prothrombotic: like other high-grade gliomas, diffuse midline glioma raises venous thromboembolism risk through tumor tissue factor and the immobility that progressive brainstem disease brings."
  - target: 01-human/07-system/sepsis
    relation: connects-to
    note: "Brainstem failure routes food to the lungs: as the tumor disables swallowing and airway protection, aspiration pneumonia becomes common, and it with the immunosuppression of high-dose steroids can progress to sepsis."
  - target: 01-human/07-system/stroke
    relation: connects-to
    note: "Its radiation can scar the brain's vessels: the high-dose radiotherapy that is the mainstay of palliation for diffuse midline glioma injures cerebral vessels, causing a delayed vasculopathy and stroke risk in longer survivors."
  - target: 01-human/07-system/major-depressive-disorder
    relation: connects-to
    note: "An almost uniformly fatal childhood tumor devastates: the relentless brainstem decline and dismal prognosis of diffuse midline glioma impose profound depression and grief on patients and families."
  - target: 01-human/07-system/anemia-of-chronic-disease
    relation: connects-to
    note: "Advanced disease and its therapy blunt the marrow: progressive tumor burden with its inflammation, plus any chemotherapy and radiation, depress erythropoiesis into an anemia of chronic disease late in the course."
---

# Diffuse Midline Glioma

## Overview

**Diffuse midline glioma (DMG), H3K27M-altered** is a WHO Grade 4 primary brain tumor defined by the presence of the **H3K27M oncohistone mutation** in a diffuse infiltrating glioma arising at a midline neuroanatomical location. Since the 2021 WHO Classification of CNS Tumors (5th edition), the H3K27M mutation is the defining molecular criterion — replacing histological grade for diagnosis. DMG encompasses the clinically defined **diffuse intrinsic pontine glioma (DIPG)** and H3K27M-mutant gliomas of the thalamus, cerebellum, and spinal cord. DMG is uniformly lethal, with no curative treatment; it is the **leading cause of brain tumor-related mortality in children** [^schwartzentruber-2012-h3f3a-glioma] [^khuong-quang-2012-h3k27m-dipg].

**Epidemiology:**
- Incidence: ~300-400 DIPG cases/year USA; ~100-150 additional thalamic/spinal H3K27M DMG
- Peak age: 5-10 years for DIPG; 10-15 years for thalamic; young adults (20-40 years) for ~15-20% of cases
- No sex predominance; no known germline predisposition; no environmental risk factors identified
- Rarely familial; somatic H3K27M always

**Sites:**

| Location | Frequency of H3K27M+ | Key features |
|---|---|---|
| Pons (DIPG) | ~80% | Peak age 6-9 yr; cranial nerve palsies (VI, VII most common); long tract signs; Parinaud syndrome rare |
| Thalamus | ~50% | Unilateral thalamic mass → hydrocephalus; older pediatric age; some resectable; worse prognosis than DIPG in adults |
| Spinal cord | ~30% | Cervical > thoracic; NF1 co-mutations common; ~15% adult patients; more amenable to biopsy |
| Cerebellum | ~15% | Often H3.3 K27M; frequently adult; mass lesion; partial resection possible |

**Median OS by location and subtype:**
- DIPG (children): 9-11 months from diagnosis without modern therapy; 14-17 months with RT + ONC201 era
- Thalamic DMG (pediatric): 12-18 months
- Thalamic/spinal DMG (adult): 14-24 months (slightly better)
- Adult cerebellar DMG: 18-28 months (most favorable H3K27M DMG subgroup)

## Structure

### Molecular subtypes and co-driver mutations

**H3.3K27M (H3F3A)** — ~75% of all H3K27M DMG:
- Pontine and thalamic locations
- Co-mutations: PDGFRA (amplification or D842V/N659K point mutations ~25-35%), PIK3CA/R1 (~15%), NF1 (~10%), ATRX (~15%)
- Slightly older pediatric/young adult age (median 8-10 years for DIPG, 15-20 years for thalamic)
- Slightly worse prognosis than H3.1K27M

**H3.1K27M (HIST1H3B/HIST1H3C)** — ~25% of all H3K27M DMG:
- Exclusively pontine (DIPG); the "pure DIPG" subtype
- Co-mutations: ACVR1 gain-of-function mutations (~40-50%, activating BMP signaling), PPM1D (~20%), HIST1H3B Q86R/H3.1K36M (rare)
- Younger age (median 5-7 years)
- Slightly longer OS than H3.3K27M DIPG (~11-13 months vs ~9-11 months)

**H3.2K27M (HIST2H3C)** — rare: similar biology to H3.1; predominantly pontine

**H3K27M-altered DMG, NOS:** small subset where H3K27M is confirmed but histone subtype undetermined

### Imaging and diagnosis

**MRI features of DIPG:**
- T1: hypointense, iso/hypointense; poorly marginated; encompasses >50% of pons in classic DIPG
- T2/FLAIR: hyperintense; engulfs basilar artery without encasing
- Enhancement: ring enhancement or heterogeneous enhancement (may indicate transformation); non-enhancing ~60% of classic DIPG
- DWI: variable; restricted diffusion in higher-grade regions
- MR spectroscopy: elevated choline:NAA ratio; elevated lactate in high-grade areas

**Biopsy:**
- Stereotactic biopsy of DIPG: historically avoided; now standard for molecular diagnosis and trial eligibility
- Pontine biopsy safety: <1% permanent neurological deficit in experienced centers; typically 2-3 core biopsies
- H3K27M IHC (clone D5E7): performed on biopsy; sensitivity ~95% for H3K27M+ DMG
- Liquid biopsy: CSF cfDNA H3K27M detection; plasma ctDNA (lower sensitivity); H3K27M ddPCR for monitoring

### IHC and molecular workup

**H3K27M IHC (D5E7 clone):** strong nuclear positivity; diagnostic; approved diagnostic antibody
**H3K27me3 IHC:** globally reduced/lost (contrast with normal brain parenchyma which is strongly H3K27me3+)
**EZH2 IHC:** expressed/overexpressed in tumor cells despite functional inactivation by H3K27M
**PDGFRA IHC:** overexpressed in ~40-50%; does not predict response without mutation confirmation
**Next-generation sequencing panel:** confirms H3K27M variant allele, identifies co-driver mutations (ACVR1, PIK3CA, NF1, PDGFRA) for clinical trial stratification
**FISH:** PDGFRA amplification, CDK6 amplification, MYCN amplification

## Function

### Oncogenesis: H3K27M epigenetic reprogramming

H3K27M-driven global H3K27me3 loss creates a fundamentally permissive chromatin state in DMG:

**De-repressed target programs:**
- **PDGFRA super-enhancer**: H3K27ac gain at PDGFRA locus → PDGFRA overexpression (even without genetic amplification); PDGFRA → MAPK/PI3K → proliferation
- **CDK6 enhancer de-repression**: CDK6 overexpression → RB1 hyperphosphorylation → E2F-driven cell cycle
- **Stem cell programs**: SOX2, OLIG2, NESTIN, ID1 maintained by loss of H3K27me3-mediated silencing → neural stem cell identity preserved; DMG cells remain in a progenitor state unable to terminally differentiate
- **HOX gene dysregulation**: posterior HOX genes de-repressed → aberrant positional identity
- **EMT programs**: CDH2 (N-cadherin), fibronectin, MMP9 → diffuse infiltration pattern (histological hallmark: "diffuse")

**The developmental timing hypothesis:**
H3K27M is only oncogenic in specific progenitor populations at specific developmental windows — during peak pontine/thalamic oligodendrogenesis. H3K27M in mature neurons or mature glia does not produce glioma. This explains: (1) the pediatric age peak of DIPG, (2) the pontine/thalamic predilection, (3) why adult H3K27M DMGs are less common (fewer susceptible progenitors exist).

## Pathology

### Treatment

**Radiation therapy (standard of care, first-line):**
- DIPG: 54 Gy in 30 fractions (1.8 Gy/fx) focal RT; conformal RT (IMRT or proton); whole-brain RT NOT used
- Radiological response: ~85% show T2/FLAIR reduction at 6-8 weeks post-RT; most are transient
- Median TTP after RT: 6-8 months; RT is palliative, not curative
- Re-irradiation at progression: 21-30 Gy additional; used in most centers; extends OS ~3-5 months
- Hypofractionated RT (39 Gy/13 fr or 54 Gy/18 fr): equivalent outcomes; preferred in young children or those unable to tolerate conventional fractionation

**ONC201 (imipridone) — FDA approved April 2024:**
First FDA-approved drug for H3K27M-mutant diffuse glioma; approved for adults and pediatric patients ≥1 year:
- Mechanism: DRD2/DRD5 antagonism → ISR/ATF4 activation + ClpP mitochondrial agonist → bioenergetic collapse selectively in H3K27M cells
- Dosing: 625 mg weekly (adult); pediatric weight-based weekly dosing
- Phase 2 (ACTION study): ORR ~22-30%; DCR ~60%; median OS ~15-17 months in H3F3A K27M cohort
- ONC201 crosses blood-brain barrier well (CNS penetrance ~40-60% relative to plasma)
- Toxicity: nausea, fatigue, elevated transaminases (grade 1-2); well tolerated
- Ongoing Phase 3 confirmatory trial

**Panobinostat (HDAC inhibitor):**
- Mechanism: H3K27ac reduction → partial H3K27me3 restoration at polycomb target loci
- Phase 1 PBTC-047: MTD established; CNS penetrance adequate at MTD; stable disease signals
- Phase 2 PBTC-047b (with RT): ongoing; primary endpoint: 12-month OS vs historical control
- Combination panobinostat + ONC201: synergistic in preclinical DMG models

**Targeted therapy (co-driver directed):**
- **ACVR1 inhibitors** (for ACVR1-mutant H3.1K27M DIPG): LDN-212854, M4K2009; preclinical activity; Phase 1 trials ongoing
- **PDGFRA inhibitors** (for PDGFRA-amplified/mutant DMG): avapritinib (PDGFRA D842V), dasatinib, imatinib; Phase 1/2 in PDGFRA-altered DMG
- **PI3K/mTOR inhibitors** (for PIK3CA/R1-mutant DMG): copanlisib, alpelisib; combination with ONC201 under investigation
- **MEK inhibitors** (for NF1-mutant DMG): selumetinib, trametinib; Phase 1 in NF1+H3K27M spinal DMG

**Immunotherapy:**
- DMG is immunologically cold: low TMB (~1-2 mut/Mb), minimal TILs, immunosuppressive microenvironment
- Anti-PD-1 (nivolumab, pembrolizumab): ORR <5% in single-agent trials
- CAR-T therapy targeting H3K27M peptide-MHC complex: preclinical; GD2-CAR-T (GD2 expressed on DIPG cells); B7H3-CAR-T; Phase 1 trials open (intrathecal delivery explored)
- Vaccine targeting H3K27M neoepitope: H3K27M is an ideal neoantigen target; Phase 1 peptide vaccine in H3K27M DMG ongoing (NCT03299309)

**Convection-enhanced delivery (CED):**
Direct infusion of drugs into the pons via stereotactic catheter; bypasses BBB; explored with panobinostat, ONC201, gemcitabine; early Phase 1 data; logistically complex; neurotoxicity at high doses

**Prognosis:**
- Median OS without treatment: ~3-5 months (DIPG untreated historic controls)
- Median OS with RT alone: ~9-11 months (DIPG); ~12-18 months (thalamic)
- Median OS with RT + ONC201 (post-RT maintenance): ~14-17 months (emerging data)
- 2-year OS: ~5-10% in DIPG; ~15-20% in thalamic DMG
- Long-term survivors (>3 years): ~5% of DIPG; often harbor specific molecular features (ACVR1 co-mutation, H3.1K27M)
- Predictors of longer OS: H3.1K27M (vs H3.3K27M), adult age, spinal location, no PDGFRA amplification, ONC201 response at 12 weeks by MRI

## Connections

- `connects-to` → **[H3K27M](../../03-molecular/h3k27m/README.md)** — H3K27M mutation in H3F3A or HIST1H3B defines WHO Grade 4 diffuse midline glioma (100% diagnostic criterion since 2021 WHO CNS classification); H3K27M IHC (anti-H3.3K27M, clone D5E7) is the diagnostic standard; TBXT-negative; H3K27M identifies tumor in CSF liquid biopsy.
- `connects-to` → **[EZH2](../../03-molecular/ezh2/README.md)** — H3K27M inhibits EZH2/PRC2 activity in trans → global H3K27me3 loss; this dominant-negative epigenetic mechanism is the oncogenic hallmark of DMG; paradoxically, EZH2 protein is intact and overexpressed in H3K27M DMG; panobinostat (HDAC inhibitor) partially restores H3K27me3.
- `connects-to` → **[CDKN2A](../../03-molecular/cdkn2a/README.md)** — CDKN2A deletion in ~15-25% H3K27M DMG (higher in DIPG/thalamic subtypes); NF1+H3K27M co-alteration common in spinal DMG; CDKN2A loss → CDK4/6 → RB1 → E2F proliferation; palbociclib + ONC201 combination being explored in H3K27M+CDKN2A-deleted DMG.
- `connects-to` → **[PDGF](../../03-molecular/pdgf/README.md)** — PDGFRA point mutations and amplification occur in ~25-35% of H3K27M DMG; PDGFRA → MAPK/PI3K → glioma proliferation; PDGFRA co-mutation with H3K27M accelerates malignancy; avapritinib and imatinib explored in PDGFRA-mutant DMG subsets.
- `connects-to` → **[NF1](../../03-molecular/nf1/README.md)** — NF1 mutations in ~10% of H3K27M DMG, enriched at spinal cord location; NF1 LOF → constitutive RAS-MAPK → MEK-ERK proliferation; NF1+H3K27M spinal DMG shows high macrophage infiltration; selumetinib and trametinib (MEK inhibitors) explored in NF1-mutant H3K27M spinal DMG.
- `connects-to` → **[PIK3CA](../../03-molecular/pik3ca/README.md)** — PIK3CA/PIK3R1 mutations in ~15% of H3K27M DMG; PI3K-AKT-mTOR cooperates with H3K27M epigenetic reprogramming; alpelisib (PI3Kα inhibitor) and copanlisib in combination with ONC201 under investigation; PTEN loss is an alternative PI3K pathway activation mechanism in DMG.
- `connects-to` → **[Glioblastoma](../glioblastoma/README.md)** — H3K27M DMG and IDH-wildtype GBM are both WHO Grade 4 but molecularly distinct; GBM shows EGFR amplification/EGFRvIII, TERT promoter mutation, CDK4/6 amplification absent in DMG; ONC201 active in DMG but not GBM; bevacizumab benefits GBM (PFS) but not H3K27M DMG.
- `connects-to` → **[Brain](../../06-organ/brain/README.md)** — Diffuse midline glioma grows in the brain's midline — pons (DIPG), thalamus, and spinal cord — where infiltrative spread makes surgery impossible; the pontine location compresses cranial nerve nuclei and long tracts, and radiation is the only treatment that briefly helps.
- `connects-to` → **[Oligodendrocyte](../../04-cellular/oligodendrocyte/README.md)** — DMG arises from oligodendrocyte precursor cells (OPCs) of the developing midline: the H3K27M mutation freezes these cells in a proliferative, stem-like state by stalling differentiation, which is why the tumor peaks at ages 5-10 when OPCs are most active in the pons.
- `connects-to` → **[Microglia](../../04-cellular/microglia/README.md)** — The DMG microenvironment is rich in microglia and macrophages, especially NF1-mutant spinal tumors, but these are immunosuppressive rather than tumoricidal — one reason checkpoint inhibitors have largely failed and GD2-directed CAR-T is being explored instead.
- `connects-to` → **[Medulloblastoma](../medulloblastoma/README.md)** — Diffuse midline glioma and medulloblastoma are the two great malignant pediatric brain tumors at opposite poles: DMG is an unresectable, fatal H3 K27M brainstem glioma, while medulloblastoma is a resectable cerebellar tumor often cured by surgery plus craniospinal radiotherapy.
- `connects-to` → **[Astrocyte](../../04-cellular/astrocyte/README.md)** — Diffuse midline glioma arises from an OPC-like glial precursor of the astrocyte/oligodendrocyte lineage: the H3 K27M oncohistone freezes these cells in a stem-like state by collapsing H3K27 methylation, so the tumor infiltrates the pons diffusely rather than forming a mass.
- `connects-to` → **[Photon](../../01-subatomic/photon/README.md)** — Photon radiotherapy is the only treatment that reliably helps diffuse midline glioma: focal irradiation of the pons gives transient symptom relief and a few months' benefit, but the H3 K27M tumor inevitably regrows—no chemo, surgery, or re-irradiation is curative.
- `connects-to` → **[IDH-mutant glioma](../idh-mutant-glioma/README.md)** — Diffuse midline glioma and IDH-mutant glioma are epigenetically opposite gliomas: DMG's H3 K27M oncohistone collapses methylation in children with dismal outcomes, while adult IDH-mutant gliomas accumulate 2-HG and fare far better—chromatin reprogramming, not oncogenes.
- `connects-to` → **[Atypical teratoid/rhabdoid tumor](../atypical-teratoid-rhabdoid-tumor/README.md)** — Diffuse midline glioma and ATRT are aggressive pediatric brain tumors driven by epigenetic dysregulation: DMG by the H3 K27M histone mutation, ATRT by SMARCB1/SWI-SNF loss—both reprogram chromatin and carry a grim prognosis.
- `connects-to` → **[Neuron](../../04-cellular/neuron/README.md)** — Diffuse midline glioma forms synapses with neurons to grow: the tumor's OPC-like cells receive glutamatergic input through real neuron-to-glioma synapses that drive proliferation—so neuronal activity feeds the cancer, making activity-blocking drugs a therapeutic idea.
- `connects-to` → **[p53](../../03-molecular/p53/README.md)** — TP53 mutation frequently accompanies the H3K27M driver in DMG: loss of p53 removes the damage checkpoint atop the epigenetic catastrophe of histone mutation, accelerating this fatal pediatric brainstem tumor—a partnership of epigenetic and tumor-suppressor failure.
- `connects-to` → **[CDK4/6](../../03-molecular/cdk4-6/README.md)** — CDK4/6 amplification helps drive DMG's relentless growth: alongside H3K27M, gains in the cell-cycle machinery push tumor cells past the G1 checkpoint, making CDK4/6 inhibitors one of the targeted strategies tested against this otherwise untreatable tumor.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — DMG often activates the PI3K/AKT/mTOR pathway: mutations in PIK3CA and related genes switch on mTOR-driven growth alongside the H3K27M epigenetic driver, so mTOR-pathway inhibitors are explored as targeted therapy for this lethal midline glioma.
- `connects-to` → **[Nervous System](../nervous-system/README.md)** — Diffuse midline glioma is the deadliest pediatric tumor of the nervous system: it infiltrates the brainstem (as DIPG), thalamus or spinal cord diffusely, so it cannot be resected and disrupts the very structures that control breathing, movement and consciousness.
- `connects-to` → **[Li-Fraumeni Syndrome](../li-fraumeni-syndrome/README.md)** — Germline TP53 loss in Li-Fraumeni syndrome predisposes to midline gliomas: while most diffuse midline gliomas are sporadic H3K27M-driven, the syndrome shows how inherited tumor-suppressor loss can also seed these lethal childhood brain cancers.
- `connects-to` → **[Proton](../../01-subatomic/proton/README.md)** — Proton therapy has been tried in diffuse midline glioma to spare the developing brain: its sharp dose falloff limits collateral damage near the brainstem, but because the tumor infiltrates diffusely and resists treatment, it has not improved the grim prognosis.
- `connects-to` → **[Synapse](../../05-tissue/synapse/README.md)** — Diffuse midline glioma hijacks the synapse: tumor cells form real synapses with neurons and grow in response to neuronal activity, so brain electrical signaling literally feeds the cancer—a discovery opening neuroscience-based therapies for this lethal childhood tumor.
- `connects-to` → **[Cytotoxic T Cell](../../04-cellular/t-cytotoxic-cell/README.md)** — Diffuse midline glioma is a frontier for T-cell therapy: GD2-directed CAR-T cells have shrunk these previously untreatable pontine tumors in early trials, so engineered cytotoxic T cells offer the first real hope against a near-uniformly fatal cancer.
- `connects-to` → **[Glutamate](../../03-molecular/glutamate/README.md)** — Glutamate drives diffuse midline glioma growth: neuron-released glutamate acting on tumor AMPA receptors stimulates proliferation, so the same excitatory signaling that runs the brain fuels the cancer—making glutamate pathways a therapeutic target.
- `connects-to` → **[Dopamine](../../03-molecular/dopamine/README.md)** — Diffuse midline glioma's most promising drug works on dopamine signaling: ONC201 (dordaviprone) antagonizes the dopamine D2 receptor (and mitochondrial ClpP) and has produced rare responses in H3K27M tumors, a surprising therapeutic angle in an otherwise fatal cancer.
- `connects-to` → **[EGFR](../../03-molecular/egfr/README.md)** — A thalamic subset of diffuse midline glioma is driven by EGFR: bithalamic H3-wildtype midline gliomas carry EGFR mutations rather than H3K27M, so molecular testing splits these tumors into biologically distinct, differently-targetable groups.
- `connects-to` → **[Natural Killer Cell](../../04-cellular/natural-killer-cell/README.md)** — Diffuse midline glioma is a target for NK and cell therapies: because it is so hard to resect or irradiate, engineered NK cells and GD2 CAR-T are being tested to attack the tumor immunologically where surgery and drugs fail.
- `connects-to` → **[Calcium](../../02-atomic/calcium/README.md)** — Diffuse midline glioma grows on calcium from neuron-glioma synapses: real synapses form between neurons and tumor cells, and the glutamate-driven calcium influx through them spurs the cancer to proliferate—a striking link between brain activity and tumor growth.
- `connects-to` → **[VEGF](../../03-molecular/vegf/README.md)** — Diffuse midline glioma recruits blood supply via VEGF: though infiltrative, the tumor releases VEGF to coax new vessels and loosen the blood-brain barrier, a process studied as a target in a cancer that resists almost all therapy.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — Tumor-associated microglia feed diffuse midline glioma through NF-kB: this inflammatory switch in the brain's immune cells drives cytokines that support the glioma's growth, part of the supportive niche around this lethal pediatric tumor.
- `connects-to` → **[Eye](../../06-organ/eye/README.md)** — Diffuse midline glioma announces itself in the eyes: a pontine tumor first palsies the cranial nerves that move the eyes and face, so double vision, a crossed eye, and facial droop are classic early signs of DIPG.
- `connects-to` → **[Lung](../../06-organ/lung/README.md)** — Diffuse midline glioma ultimately stops the breath: as it destroys the brainstem's control of breathing and swallowing, patients lose airway protection and respiratory drive, the failure that ends this lethal disease.
- `connects-to` → **[Endothelial Cell](../../04-cellular/endothelial-cell/README.md)** — Diffuse midline glioma works on endothelial cells: VEGF from the tumor loosens the blood-brain barrier these cells form and recruits new vessels, both feeding growth and complicating drug delivery to the brainstem.
- `connects-to` → **[Heart](../../06-organ/heart/README.md)** — Diffuse midline glioma destabilizes the brainstem's autonomic control: infiltrating the pons it disrupts the centers governing heart rate and blood pressure, causing dangerous swings late in the disease.
- `connects-to` → **[Peripheral Nerve](../../05-tissue/peripheral-nerve/README.md)** — Diffuse midline glioma picks off the cranial nerves: invading the pons it palsies the nerves controlling eye movement, the face and swallowing, the cranial-nerve deficits that often herald it.
- `connects-to` → **[Activin A](../../03-molecular/activin-a/README.md)** — Some diffuse midline gliomas are driven by activin signaling: ACVR1 mutations switch on the activin-A/BMP pathway, a recurrent driver in the pontine tumors of young children and a drug target.
- `connects-to` → **[Electron](../../01-subatomic/electron/README.md)** — Electron microscopy made a startling discovery: real synapses form between healthy neurons and glioma cells, the neuron's terminal wiring directly onto the tumor — an electrical hijacking that drives the cancer's growth.
- `connects-to` → **[Potassium](../../02-atomic/potassium/README.md)** — The tumor plugs into the brain's electricity: glioma cells carry potassium and other ion channels that let them depolarize in response to neuronal firing, the electrical excitability that the neuron-glioma synapse feeds and that spurs invasion.
- `connects-to` → **[Sodium](../../02-atomic/sodium/README.md)** — Glutamate from the neuron-glioma synapse pours sodium into the tumor: AMPA-receptor currents flood the glioma cell with sodium and calcium, the depolarizing signal by which neural activity literally powers the cancer's spread.
- `connects-to` → **[Antibody](../../03-molecular/antibody/README.md)** — Engineered antibody-based cells offer new hope: GD2-directed CAR-T cells have shrunk H3K27M-mutant diffuse midline gliomas in early trials, the first therapy to dent a tumor that radiation only briefly holds.
- `connects-to` → **[Stomach](../../06-organ/stomach/README.md)** — Its pontine home wrecks swallowing: the tumor infiltrates the brainstem's bulbar centers, so dysphagia and impaired airway protection bring aspiration and the need for feeding tubes as the disease advances.
- `connects-to` → **[Neutrophil](../../04-cellular/neutrophil/README.md)** — Radiation and chemotherapy thin the blood: the craniospinal radiation and any added chemotherapy suppress the marrow, dropping neutrophils and raising the infection risk during the months of treatment.
- `connects-to` → **[Endocrine System](../endocrine-system/README.md)** — A midline tumor sits beside the master glands: thalamic and pontine gliomas and the radiation aimed at them border the hypothalamus and pituitary, so survivors face deficits of growth, thyroid and sex hormones that need lifelong endocrine follow-up.
- `connects-to` → **[MYC](../../03-molecular/myc/README.md)** — A subset of these gliomas amplify MYC: alongside the defining H3K27M mutation, MYC or PVT1 amplification drives some diffuse midline gliomas, adding a proliferative push that marks particularly aggressive, fast-growing tumors.
- `connects-to` → **[Regulatory T Cell](../../04-cellular/regulatory-t-cell/README.md)** — The tumor is immunologically cold: it carries few mutations to flag and recruits regulatory T cells that suppress attack, an immune-evasive microenvironment that has frustrated immunotherapy and shapes the GD2 CAR-T trials now under way.
- `connects-to` → **[Transforming Growth Factor Beta](../../03-molecular/tgf-beta/README.md)** — TGF-β helps the glioma spread and hide: it drives the diffuse invasion through the brainstem and dampens the local immune response, part of why these tumors are unresectable and immune-resistant.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Macrophages fill the tumor but don't fight it: monocyte-derived macrophages, alongside microglia, dominate the DMG microenvironment in an immunosuppressive state that helps the cancer evade attack.
- `connects-to` → **[Neurofibromatosis Type 1](../neurofibromatosis-type-1/README.md)** — An NF1 background can seed the glioma: loss of the NF1 tumor suppressor is a recurrent driver of diffuse midline glioma, and the syndrome's lifelong predisposition to gliomas links it to this lethal childhood tumor.
- `connects-to` → **[ATRX](../../03-molecular/atrx/README.md)** — ATRX loss often joins the H3K27M hit: especially in thalamic and spinal diffuse midline gliomas, ATRX mutation accompanies the histone mutation, driving alternative lengthening of telomeres and genomic instability.
- `connects-to` → **[Epilepsy](../epilepsy/README.md)** — The infiltrating glioma irritates the cortex: as diffuse midline glioma spreads from the pons or thalamus it can trigger seizures, and seizure control is part of the supportive care for these children.
- `connects-to` → **[Neuropathic Pain](../neuropathic-pain/README.md)** — Brainstem and spinal infiltration brings pain: tumor invasion of sensory pathways causes neuropathic pain and, in spinal diffuse midline glioma, radicular pain — a symptom burden central to palliative management.
- `connects-to` → **[STAT3](../../03-molecular/stat3/README.md)** — STAT3 supports the H3K27M-driven tumor: diffuse midline glioma cells show STAT3 activation that backs proliferation and immune evasion, a pathway studied for this almost uniformly fatal childhood brainstem tumor.
- `connects-to` → **[Venous Thromboembolism](../venous-thromboembolism/README.md)** — Brain tumors are strongly prothrombotic: like other high-grade gliomas, diffuse midline glioma raises venous thromboembolism risk through tumor tissue factor and the immobility that progressive brainstem disease brings.
- `connects-to` → **[Sepsis](../sepsis/README.md)** — Brainstem failure routes food to the lungs: as the tumor disables swallowing and airway protection, aspiration pneumonia becomes common, and it with the immunosuppression of high-dose steroids can progress to sepsis.
- `connects-to` → **[Stroke](../stroke/README.md)** — Its radiation can scar the brain's vessels: the high-dose radiotherapy that is the mainstay of palliation for diffuse midline glioma injures cerebral vessels, causing a delayed vasculopathy and stroke risk in longer survivors.
- `connects-to` → **[Major Depressive Disorder](../major-depressive-disorder/README.md)** — An almost uniformly fatal childhood tumor devastates: the relentless brainstem decline and dismal prognosis of diffuse midline glioma impose profound depression and grief on patients and families.
- `connects-to` → **[Anemia of Chronic Disease](../anemia-of-chronic-disease/README.md)** — Advanced disease and its therapy blunt the marrow: progressive tumor burden with its inflammation, plus any chemotherapy and radiation, depress erythropoiesis into an anemia of chronic disease late in the course.

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^schwartzentruber-2012-h3f3a-glioma]: Schwartzentruber J, Korshunov A, Liu XY, et al. Driver mutations in histone H3.3 and chromatin remodelling genes in paediatric glioblastoma. *Nature.* 2012;482(7384):226-231. [doi:10.1038/nature10833](https://doi.org/10.1038/nature10833) · [PubMed 22286061](https://pubmed.ncbi.nlm.nih.gov/22286061/)
[^khuong-quang-2012-h3k27m-dipg]: Khuong-Quang DA, Buczkowicz P, Rakopoulos P, et al. K27M mutation in histone H3.3 defines clinically and biologically distinct subgroups of pediatric diffuse intrinsic pontine gliomas. *Acta Neuropathol.* 2012;124(3):439-447. [doi:10.1007/s00401-012-0998-0](https://doi.org/10.1007/s00401-012-0998-0) · [PubMed 22661320](https://pubmed.ncbi.nlm.nih.gov/22661320/)
