---
schema: human-scale-entry/v1
id: ptch1
name: PTCH1
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-06
summary: "PTCH1 (Patched 1) is the HH receptor; LOF → constitutive SMO → GLI1/2 transcription; germline PTCH1 mutations cause Gorlin syndrome (BCCs, SHH medulloblastoma); somatic PTCH1 LOF in ~90% sporadic BCC; SMO inhibitors (vismodegib, sonidegib) restore PTCH1-like SMO inhibition."
aliases: ["PTCH1", "Patched 1", "PTCH", "hedgehog receptor", "PTCH1 Gorlin", "basal cell nevus syndrome", "PTCH1 medulloblastoma", "sonic hedgehog pathway"]
sources:
  - id: johnson-1996-ptch1-gorlin
    type: peer-reviewed
    cite: "Johnson RL, Rothman AL, Xie J, et al. Human homolog of patched, a candidate gene for the basal cell nevus syndrome. Science. 1996;272(5268):1668-1671."
    doi: "10.1126/science.272.5268.1668"
    pmid: "8658145"
    url: "https://doi.org/10.1126/science.272.5268.1668"
  - id: tang-2012-vismodegib-gorlin
    type: peer-reviewed
    cite: "Tang JY, Mackay-Wiggan JM, Aszterbaum M, et al. Inhibiting the hedgehog pathway in patients with the basal-cell nevus syndrome. N Engl J Med. 2012;366(23):2180-2188."
    doi: "10.1056/NEJMoa1113538"
    pmid: "22670901"
    url: "https://doi.org/10.1056/NEJMoa1113538"
cross_links:
  - target: 01-human/03-molecular/smo
    relation: connects-to
    note: "PTCH1 constitutively inhibits SMO (Smoothened, 7-TM receptor); SHH binding to PTCH1 → PTCH1 inhibition → SMO derepression → GLI activation; SMO inhibitors (vismodegib, sonidegib) mimic PTCH1 re-activation → GLI repression; PTCH1 LOF = constitutive SMO activation."
  - target: 01-human/03-molecular/myc
    relation: connects-to
    note: "SHH-activated medulloblastoma with MYCN amplification and TP53 mutation → highest-risk SHH-MB (5-year OS ~40%); MYCN is a downstream GLI1/2 target; MYC amplification in Group 3 MB is distinct from MYCN in SHH-MB; GLI1 transcriptionally activates MYC in Hh-driven tumors."
  - target: 01-human/03-molecular/rb1
    relation: connects-to
    note: "PTCH1 LOF → GLI1/2 → CCND1 upregulation → CDK4/6 phosphorylation of RB1 → E2F release → S-phase entry; CDK4/6 inhibitors explored in SHH-MB and Gorlin syndrome BCCs; RB1 mutation is rare in BCC/MB but CDK→Rb mediates Hh proliferative signals."
  - target: 01-human/03-molecular/bcl-2
    relation: connects-to
    note: "GLI1/2 transcriptionally activate BCL2 → resistance to apoptosis in Hh-driven tumors (BCC, SHH-MB); BCL2 overexpression in vismodegib-resistant BCC correlates with acquired resistance; venetoclax explored in combination with SMO inhibitors in preclinical BCC models."
---

# PTCH1

## Overview

**PTCH1 (Patched 1)** is the principal ligand-binding receptor of the **Sonic Hedgehog (SHH/HH) signaling pathway**, functioning as a constitutive inhibitor of **Smoothened (SMO)** in the absence of HH ligands. PTCH1 is a 12-transmembrane domain protein that resides in the primary cilium membrane and sterically/biochemically suppresses SMO — a 7-transmembrane domain GPCR-like effector; when HH ligands (SHH, DHH, IHH) bind PTCH1 → PTCH1 is internalized → SMO is derepressed → SMO accumulates in primary cilia → activates GLI transcription factors (GLI1/2/3) → drives target gene expression including PTCH1 (negative feedback), GLI1, CCND1, BCL2, VEGF, and SNAI1. PTCH1 loss-of-function (LOF) mutations — germline or somatic — eliminate this inhibitory brake → constitutive SMO activity and HH pathway activation regardless of ligand. Germline PTCH1 mutations cause **Gorlin syndrome (basal cell nevus syndrome)** — an autosomal dominant cancer predisposition syndrome featuring hundreds of BCCs, jaw keratocysts, and ~5% risk of SHH medulloblastoma — first genetically characterized by Johnson et al. in 1996 [^johnson-1996-ptch1-gorlin]. Somatic PTCH1 LOF occurs in ~90% of sporadic basal cell carcinoma (BCC). The clinical importance of PTCH1 is amplified by the development of **SMO inhibitors** (vismodegib, sonidegib) — the first FDA-approved targeted therapy for BCC — which suppress the constitutive SMO activity that PTCH1 normally provides [^tang-2012-vismodegib-gorlin].

**PTCH1 in disease:**
- **Sporadic BCC:** PTCH1 somatic LOF ~90%; UV-induced (C→T transitions at dipyrimidines); SMO inhibitors FDA-approved for locally advanced/metastatic BCC
- **Gorlin syndrome (BCNS):** Germline PTCH1 LOF (haploinsufficiency); ~50% spontaneous mutations; manifestations: numerous BCCs (beginning in 2nd-3rd decade), odontogenic keratocysts, calcified falx cerebri, bifid ribs, macrocephaly, frontal bossing, ~5% SHH medulloblastoma (infant onset, desmoplastic/nodular), cardiac fibromas, ovarian fibromas; vismodegib reduces BCC burden in Gorlin (Tang 2012: 50% reduction in new BCCs vs placebo, p<0.001) [^tang-2012-vismodegib-gorlin]
- **SHH-activated medulloblastoma:** PTCH1 LOF and/or SMO GOF and/or SUFU LOF and/or GLI2 amplification; ~28-38% of all MB; vismodegib in adult SHH-MB
- **Other HH-driven cancers:** Hepatocellular carcinoma (~30-50%), rhabdomyosarcoma (~10%), esophageal squamous cell carcinoma, colorectal cancer — HH pathway activation (not always via PTCH1 mutation; can be ligand-dependent paracrine signaling from stroma)

## Structure

### PTCH1 protein architecture

PTCH1 is a 1,447-amino-acid 12-transmembrane domain glycoprotein (~160 kDa):

**Transmembrane topology:**
12 TM helices organized in two hexahelical bundles (TM1-6 and TM7-12) flanking a large extracellular loop; two large extracellular domains (ECD1 between TM1-2, ECD2 between TM7-8) form the ligand-binding interface for SHH; PTCH1 is structurally related to bacterial Resistance-Nodulation-Division (RND) family transporters → PTCH1 may pump cholesterol or sterols that are required for SMO activity → PTCH1 inhibits SMO by depleting accessible cholesterol in the primary cilium membrane.

**Sterol transport model of PTCH1-SMO regulation:**
Cryo-EM structures (2018-2019): PTCH1 adopts an RND-transporter conformation; SMO is activated by oxysterols/cholesterol at its cysteine-rich domain (CRD); PTCH1 is proposed to deplete accessible cholesterol/oxysterols in the inner leaflet of the ciliary membrane → SMO CRD cannot access activating sterols → SMO inactive; SHH binding to PTCH1 → PTCH1 transporter activity inhibited → cholesterol accumulates → SMO CRD bound → SMO active; this mechanistic model explains why lipid modifications to SHH (palmitoylation and cholesterol modification) are required for full ligand activity.

**Key mutational hotspots:**
- Truncating mutations throughout the gene (LOF): splice-site, nonsense, frameshift; loss of one PTCH1 allele (haploinsufficiency) drives Gorlin; second somatic hit (Knudson two-hit model) required for BCC and medulloblastoma in Gorlin patients
- Missense mutations in ECD1/ECD2: impair SHH binding or PTCH1 function
- UV-signature mutations (C>T at CC/CT dipyrimidines): common in sporadic BCC; frequent UVB mutagenesis at PTCH1

### HH pathway architecture

**"Off" state (no HH ligand):**
PTCH1 in primary cilium → SMO excluded from cilium (retains in cytoplasmic vesicles) → SUFU-GLI complex → GLI3 (and GLI2) proteolytically processed by PKA/CK1/GSK3β at the cilium base → truncated GLI repressor (GLI3R) enters nucleus → represses HH target genes; GLI1 has no repressor form — GLI1 is absent in "Off" state.

**"On" state (HH ligand present):**
SHH binds PTCH1 (+ CDON/BOC co-receptors) → PTCH1 internalized/degraded → SMO traffics into primary cilium → SMO activates KIF7 and suppresses SUFU → full-length GLI2A (activator form) enters nucleus → transcribes PTCH1 (feedback), GLI1, CCND1, SNAI1, BCL2, VEGF; GLI1 amplifies the signal (feed-forward transcriptional loop).

## Function

### Normal HH pathway roles

**Embryonic development:**
HH signaling is essential for: neural tube (dorsal-ventral patterning → floor plate induction by SHH → motor neuron specification), limb development (zone of polarizing activity → anterior-posterior limb patterning), hair follicle cycling, and gut endoderm patterning; PTCH1-null mice are lethal (embryonic day 9.5); PTCH1 heterozygous mice develop spontaneous BCC and rhabdomyosarcoma → confirms haploinsufficiency model.

**Adult tissue homeostasis:**
HH pathway maintains stem cell niches in: hair follicle bulge (epidermal stem cells), intestinal crypts (via Lgr5+ stem cells supported by mesenchymal HH), cerebellum (granule cell progenitor expansion in neonatal cerebellum via SHH from Purkinje cells → granule neuron proliferation; PTCH1 LOF → GCP hyperproliferation → SHH medulloblastoma).

**Sonic Hedgehog and cerebellar development:**
Purkinje cells secrete SHH → SHH binds PTCH1 on cerebellar granule cell progenitors (GCPs) → PTCH1 inhibited → SMO active → GLI2 → CCND2 (cyclin D2) → GCP proliferation in external granule layer → GCPs differentiate and migrate inward to form internal granular layer → PTCH1 LOF in GCPs → sustained proliferation → SHH medulloblastoma arises from undifferentiated GCPs.

### HH in cancer — non-BCC/MB contexts

**Paracrine signaling (ligand-dependent):**
In many carcinomas (pancreatic, colorectal, prostate), tumor cells secrete SHH → stimulates stroma (fibroblasts, endothelium) expressing SMO → stroma-derived factors support tumor growth; SMO inhibitors suppress stromal HH → tumor microenvironment remodeling; direct tumor cell effects in ligand-dependent signaling are weaker.

## Mechanism

### SMO inhibitors (vismodegib, sonidegib)

**Mechanism:**
Both bind to the SMO transmembrane domain (allosteric site distinct from SMO CRD); specifically antagonize SMO by disrupting its ciliary trafficking and/or blocking SMO-downstream signaling; pharmacologically mimic PTCH1 re-establishment → GLI repression.

**Vismodegib (Erivedge, FDA 2012):**
First SMO inhibitor approved; metastatic BCC (ORR ~30% visceral, ~48% locally advanced); locally advanced BCC (LaBCC: ORR ~47%, CR ~21%); Gorlin syndrome: Tang 2012 (N=41): new BCCs per year 2 vs 29 (p<0.001); 50% reduction in existing BCC size; side effects: muscle cramps (~68%), alopecia, dysgeusia, weight loss, amenorrhea (women) — substantially limit tolerability; requires continuous therapy; contraindicated in pregnancy (severe teratogenicity, fetal death).

**Sonidegib (Odomzo, FDA 2015):**
SMO inhibitor; locally advanced BCC (BOLT trial: ORR 56% at 200 mg/day; simpler dosing, slightly better tolerability than vismodegib); approved for LaBCC after surgery/radiation failure or not appropriate for surgery/radiation.

**SMO resistance mechanisms:**
- SMO mutations (D473H in the vismodegib binding pocket ~30%): SMO allosteric pocket altered → drug cannot bind; other SMO mutations: W535L, V321M
- Downstream GLI2 amplification: constitutive GLI2 activation independent of SMO → SMO inhibitor resistance
- Non-canonical HH activation (KRAS-MAPK driving GLI1 independent of SMO)

**Post-SMO inhibitor therapy for BCC:**
- Cemiplimab (anti-PD-1): FDA approved 2021 for locally advanced/metastatic BCC after SMO inhibitor failure; ORR ~29% in LaBCC (EMPOWER-BCC 1 trial); durable responses; PD-L1 expression variable but not required for response (high UV mutational burden → T-cell infiltration in BCC)
- Hedgehog pathway downstream targeting (GLI inhibitors): GLI1/2 antagonists (GANT61, OGX-427): preclinical; challenge: transcription factor targeting; ATO (arsenic trioxide): suppresses GLI at the cilia; Phase 2 data in BCC and medulloblastoma

## Connections

- `connects-to` → **[SMO](../../03-molecular/smo/README.md)** — PTCH1 constitutively inhibits SMO (Smoothened, 7-TM receptor); SHH binding to PTCH1 → PTCH1 inhibition → SMO derepression → GLI activation; SMO inhibitors (vismodegib, sonidegib) mimic PTCH1 re-activation → GLI repression; PTCH1 LOF = constitutive SMO activation.
- `connects-to` → **[MYC](../../03-molecular/myc/README.md)** — SHH-activated medulloblastoma with MYCN amplification and TP53 mutation → highest-risk SHH-MB (5-year OS ~40%); MYCN is a downstream GLI1/2 target; MYC amplification in Group 3 MB is distinct from MYCN in SHH-MB; GLI1 transcriptionally activates MYC in Hh-driven tumors.
- `connects-to` → **[RB1](../../03-molecular/rb1/README.md)** — PTCH1 LOF → GLI1/2 → CCND1 upregulation → CDK4/6 phosphorylation of RB1 → E2F release → S-phase entry; CDK4/6 inhibitors explored in SHH-MB and Gorlin syndrome BCCs; RB1 mutation is rare in BCC/MB but CDK→Rb mediates Hh proliferative signals.
- `connects-to` → **[BCL-2](../../03-molecular/bcl-2/README.md)** — GLI1/2 transcriptionally activate BCL2 → resistance to apoptosis in Hh-driven tumors (BCC, SHH-MB); BCL2 overexpression in vismodegib-resistant BCC correlates with acquired resistance; venetoclax explored in combination with SMO inhibitors in preclinical BCC models.

[^johnson-1996-ptch1-gorlin]: Johnson RL, Rothman AL, Xie J, et al. Human homolog of patched, a candidate gene for the basal cell nevus syndrome. *Science.* 1996;272(5268):1668-1671. [doi:10.1126/science.272.5268.1668](https://doi.org/10.1126/science.272.5268.1668) · [PubMed 8658145](https://pubmed.ncbi.nlm.nih.gov/8658145/)
[^tang-2012-vismodegib-gorlin]: Tang JY, Mackay-Wiggan JM, Aszterbaum M, et al. Inhibiting the hedgehog pathway in patients with the basal-cell nevus syndrome. *N Engl J Med.* 2012;366(23):2180-2188. [doi:10.1056/NEJMoa1113538](https://doi.org/10.1056/NEJMoa1113538) · [PubMed 22670901](https://pubmed.ncbi.nlm.nih.gov/22670901/)
