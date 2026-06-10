---
schema: human-scale-entry/v1
id: apoe
name: APOE
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-07
summary: "APOE encodes apolipoprotein E, a lipid transport protein with three isoforms; APOE4 is the strongest genetic risk factor for late-onset Alzheimer disease (3-12x risk vs APOE3); APOE4 impairs amyloid-beta clearance and promotes tau pathology via LRP1-mediated mechanisms."
aliases: ["APOE", "apolipoprotein E", "APOE4", "ApoE4", "APOE epsilon4", "APOE2", "APOE3", "ApoE Alzheimer", "apoE4 risk", "APOE lipid"]
cross_links:
  - target: 01-human/07-system/alzheimers-disease
    relation: connects-to
    note: "APOE4 (frequency ~15%) confers 3-4x heterozygous and 8-12x homozygous risk for late-onset AD; APOE4 impairs microglial Aβ phagocytosis, promotes Aβ aggregation, and worsens tau pathology; APOE4 homozygotes develop AD ~10 years earlier than APOE3 carriers."
  - target: 01-human/03-molecular/cholesterol
    relation: connects-to
    note: "APOE is the primary cholesterol transport protein in the CNS; astrocytes secrete APOE-HDL particles that deliver cholesterol to neurons for synapse formation and myelin repair; APOE4 forms smaller, cholesterol-poor lipoprotein particles → impaired synaptic repair after injury."
  - target: 01-human/03-molecular/nlrp3-inflammasome
    relation: connects-to
    note: "APOE4 activates the NLRP3 inflammasome in microglia via impaired lipid efflux → excess intracellular cholesterol → lysosomal damage → caspase-1 activation → IL-1β and IL-18 release; APOE4-driven neuroinflammation amplifies amyloid and tau pathology in late-onset AD."
  - target: 01-human/03-molecular/mtor
    relation: connects-to
    note: "APOE4 impairs TFEB nuclear translocation (via APOE4-mediated mTORC1 hyperactivation) → reduced lysosomal biogenesis → defective Aβ clearance by microglia; mTOR inhibition with rapamycin restores APOE4 microglial function and reduces amyloid plaque load in mouse models."
  - target: 01-human/04-cellular/microglia
    relation: connects-to
    note: "Microglia are primary APOE-responsive cells in the brain; APOE4 impairs microglial Aβ phagocytosis (defective LRP1 internalization and lysosomal acidification) and activates NLRP3 → IL-1β/IL-18; TREM2 amplifies APOE4-driven microglial dysfunction in late-onset AD."
  - target: 01-human/04-cellular/astrocyte
    relation: connects-to
    note: "Astrocytes are dominant APOE producers in the brain; astrocytic APOE-HDL particles (via ABCA1) deliver cholesterol to neurons via LRP1/LDLR for synaptogenesis; APOE4 astrocytes produce smaller, less lipidated particles → impaired cholesterol delivery → synaptic deficits."
  - target: 01-human/03-molecular/mapt
    relation: connects-to
    note: "APOE4 independently promotes tau pathology: directly binds tau and accelerates aggregation in vitro; reduces autophagic tau clearance; amplifies tau-mediated neurodegeneration independent of amyloid; isoform conversion APOE4→APOE3 reduces tangle burden in mouse models."
sources:
  - id: corder-1993-apoe4-ad
    type: peer-reviewed
    cite: "Corder EH, Saunders AM, Strittmatter WJ, et al. Gene dose of apolipoprotein E type 4 allele and the risk of Alzheimer's disease in late onset families. Science. 1993;261(5123):921-923."
    doi: "10.1126/science.8346443"
    pmid: "8346443"
    url: "https://doi.org/10.1126/science.8346443"
  - id: kanekiyo-2014-apoe-ab-clearance
    type: peer-reviewed
    cite: "Kanekiyo T, Xu H, Bu G. ApoE and Aβ in Alzheimer's disease: accidental encounters or partners? Neuron. 2014;81(4):740-754."
    doi: "10.1016/j.neuron.2014.01.045"
    pmid: "24559670"
    url: "https://doi.org/10.1016/j.neuron.2014.01.045"
---

# APOE

## Overview

**APOE** (apolipoprotein E) encodes a 299 amino acid lipid transport glycoprotein with a critical role in cholesterol homeostasis throughout the body and, critically, in the brain. APOE is the predominant apolipoprotein of the central nervous system. Three common isoforms are defined by two SNPs at codons 112 and 158 (rs429358 and rs7412): **APOE2** (Cys112, Cys158), **APOE3** (Cys112, Arg158; most common, ~77% frequency), and **APOE4** (Arg112, Arg158, ~15% frequency). APOE2 is rare (~8%) and protective.

APOE4 is the **strongest common genetic risk factor for late-onset Alzheimer disease (LOAD)**, as demonstrated by Corder et al. in 1993 [^corder-1993-apoe4-ad]: one APOE4 allele confers ~3–4× risk; two APOE4 alleles confer ~8–12× risk relative to APOE3/3 homozygotes. APOE4 homozygotes represent ~2% of the European population but account for ~15–20% of AD cases. APOE4 lowers mean age of AD onset by ~7–10 years per allele. Conversely, APOE2 reduces AD risk ~2–3-fold below APOE3/3 baseline.

**APOE isoform comparison:**

| Isoform | Residue 112 | Residue 158 | Frequency | AD risk (vs APOE3/3) |
|---|---|---|---|---|
| APOE2 | Cys | Cys | ~8% | 0.4–0.6× (protective) |
| APOE3 | Cys | Arg | ~77% | 1× (reference) |
| APOE4 | Arg | Arg | ~15% | 3–4× (het), 8–12× (hom) |

## Structure

APOE folds into two structural domains separated by a flexible hinge region:

**N-terminal domain (aa 1–167):** A four-helix bundle (helices 1–4) that contains the **LDL receptor-binding region** (aa 136–150; Arg150, Arg158 make critical electrostatic contacts with LDL receptor and LRP1). In APOE4, the Arg112 substitution (vs Cys112 in APOE2/3) creates an intramolecular salt bridge with Glu109 (also called the Arg61 interaction in prior nomenclature), repositioning helix 4. This shifts the C-terminal lipid-binding domain relative to the receptor-binding domain, causing APOE4 to form **smaller, less lipidated lipoprotein particles** compared to APOE3.

**C-terminal domain (aa 206–299):** An amphipathic α-helix that mediates binding to phospholipid membranes and HDL-like particles. The Arg112→Cys112 difference in APOE4 indirectly alters lipid-binding geometry through inter-domain interaction, reducing lipoprotein particle size and cholesterol loading capacity.

**Post-translational modifications:** O-linked glycosylation at Thr194 (in APOE3/4) affects receptor affinity. Sialylation of the O-glycan present in CSF APOE particles modulates Aβ binding.

## Function

**CNS lipid transport (primary function):** Astrocytes and microglia are the principal producers of APOE in the brain. APOE-associated HDL-like particles export cholesterol and phospholipids to neurons via LDLR, LRP1, and VLDLR receptors, supporting:
- **Synapse formation and plasticity**: Adequate cholesterol supply is essential for synaptogenesis and dendritic spine maintenance; APOE-lipid particles delivered via LRP1 support postsynaptic membrane remodeling.
- **Myelin repair**: Oligodendrocytes depend on APOE-mediated cholesterol delivery for remyelination after injury.
- **Axon regeneration**: Schwann cells secrete APOE-rich particles after peripheral nerve injury to support cholesterol recycling during axon regrowth.

**Amyloid-beta metabolism:** APOE directly binds soluble Aβ and influences its clearance. APOE3 and APOE2 facilitate Aβ degradation by microglia (via TREM2-APOE axis), IDE, and neprilysin. APOE4 has reduced Aβ-binding affinity and promotes Aβ fibril nucleation rather than clearance → net increase in parenchymal and vascular amyloid deposition.

**Immune modulation:** APOE suppresses microglial activation and dampens inflammatory responses. APOE4 has reduced anti-inflammatory activity relative to APOE3; APOE4 microglia adopt a pro-inflammatory state more readily, with increased NLRP3 inflammasome activation.

## Mechanism

APOE4 contributes to AD pathogenesis through at least four non-exclusive mechanisms:

**1. Impaired Aβ clearance:** APOE4 binds Aβ with lower affinity than APOE3 and directs Aβ toward insoluble fibril formation rather than degradation. APOE4-Aβ complexes are less efficiently internalized by LRP1 at the blood-brain barrier, reducing Aβ efflux to the periphery. Microglial Aβ phagocytosis is APOE4-isoform-dependent: APOE4-expressing microglia show impaired lysosomal acidification → defective Aβ degradation → plaque accumulation.

**2. Tau pathology promotion:** APOE4 independently exacerbates tau hyperphosphorylation and neurofibrillary tangle formation. Mechanistically: APOE4 directly binds tau and promotes its aggregation in vitro; APOE4 also reduces tau clearance via impaired autophagy; in mouse models, APOE4 amplifies tau-mediated neurodegeneration independent of amyloid status.

**3. Synaptic dysfunction:** APOE4 forms smaller, less cholesterol-rich HDL particles → neurons receive insufficient cholesterol → impaired synaptic vesicle recycling, reduced synaptophysin, and fewer dendritic spines. APOE4 knockout or isoform conversion (APOE4→APOE3 via structure-correctors) improves synaptic density in mouse models.

**4. Neuroinflammation and mitochondrial dysfunction:** APOE4 activates NLRP3 inflammasome in microglia via excessive intracellular cholesterol accumulation (impaired lipid efflux). APOE4 also promotes mitochondrial fragmentation and reduces oxidative phosphorylation in neurons, contributing to the bioenergetic failure characteristic of AD.

**Therapeutic targeting:** APOE4 structure-correctors (small molecules that restore APOE4 conformation toward APOE3-like structure: PH002, APOE4 correctors from Aperion Bio) are in preclinical/early clinical development. APOE-directed antisense oligonucleotides reducing APOE4 expression are in early trials. Stem cell-derived gene correction of APOE4→APOE3 has been validated in human iPSC-derived neurons.

## Connections

- `connects-to` → **[Alzheimer's Disease](../../07-system/alzheimers-disease/README.md)** — APOE4 (~15% frequency) confers 3-4× heterozygous and 8-12× homozygous risk for late-onset AD; APOE4 impairs microglial Aβ phagocytosis, promotes Aβ aggregation, and worsens tau pathology; APOE4 homozygotes develop AD ~10 years earlier than APOE3 carriers.
- `connects-to` → **[Cholesterol](../../03-molecular/cholesterol/README.md)** — APOE is the primary cholesterol transport protein in the CNS; astrocytes secrete APOE-HDL particles that deliver cholesterol to neurons for synapse formation and myelin repair; APOE4 forms smaller, cholesterol-poor lipoprotein particles → impaired synaptic repair after injury.
- `connects-to` → **[NLRP3 Inflammasome](../../03-molecular/nlrp3-inflammasome/README.md)** — APOE4 activates the NLRP3 inflammasome in microglia via impaired lipid efflux → excess intracellular cholesterol → lysosomal damage → caspase-1 → IL-1β/IL-18; APOE4-driven neuroinflammation amplifies amyloid and tau pathology in late-onset AD.
- `connects-to` → **[mTOR](../../03-molecular/mtor/README.md)** — APOE4 impairs TFEB nuclear translocation via mTORC1 hyperactivation → reduced lysosomal biogenesis → defective Aβ clearance by microglia; mTOR inhibition with rapamycin restores APOE4 microglial function and reduces amyloid plaque load in mouse models.
- `connects-to` → **[Microglia](../../04-cellular/microglia/README.md)** — microglia are primary APOE-responsive cells in the brain; APOE4 impairs microglial Aβ phagocytosis (defective LRP1 internalization and lysosomal acidification) and activates NLRP3 → IL-1β/IL-18; TREM2 amplifies APOE4-driven microglial dysfunction in late-onset AD.
- `connects-to` → **[Astrocyte](../../04-cellular/astrocyte/README.md)** — astrocytes are dominant APOE producers in the brain; astrocytic APOE-HDL particles (via ABCA1) deliver cholesterol to neurons via LRP1/LDLR for synaptogenesis; APOE4 astrocytes produce smaller, less lipidated particles → impaired cholesterol delivery → synaptic deficits.
- `connects-to` → **[MAPT/Tau](../../03-molecular/mapt/README.md)** — APOE4 independently promotes tau pathology: directly binds tau and accelerates aggregation in vitro; reduces autophagic tau clearance; amplifies tau-mediated neurodegeneration independent of amyloid; isoform conversion APOE4→APOE3 reduces tangle burden in mouse models.

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
