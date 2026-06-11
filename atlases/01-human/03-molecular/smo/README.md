---
schema: human-scale-entry/v1
id: smo
name: SMO
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-06
summary: "Smoothened receptor in the Hedgehog pathway; activated when PTCH1 releases SMO repression after HH ligand binding → GLI transcription factors → BCL-2, cyclin D1, and MYC. Mutated in ~40% of sporadic BCC; vismodegib and sonidegib are approved SMO inhibitors for advanced BCC."
aliases: ["SMO", "Smoothened", "SMOH", "Hedgehog pathway", "GLI signaling", "Hh signaling", "SHH pathway receptor", "frizzled-class GPCR"]
sources:
  - id: sekulic-2012-vismodegib
    type: peer-reviewed
    cite: "Sekulic A, Migden MR, Oro AE, et al. Efficacy and safety of vismodegib in advanced basal-cell carcinoma. N Engl J Med. 2012;366(23):2171-2179."
    doi: "10.1056/NEJMoa1113600"
    pmid: "22670902"
    url: "https://doi.org/10.1056/NEJMoa1113600"
  - id: tang-2012-vismodegib
    type: peer-reviewed
    cite: "Tang JY, Mackay-Wiggan JM, Aszterbaum M, et al. Inhibiting the hedgehog pathway in patients with the basal-cell nevus syndrome. N Engl J Med. 2012;366(23):2180-2188."
    doi: "10.1056/NEJMoa1113538"
    pmid: "22670904"
    url: "https://doi.org/10.1056/NEJMoa1113538"
cross_links:
  - target: 01-human/03-molecular/wnt-beta-catenin
    relation: connects-to
    note: "Hedgehog and Wnt pathways are frequently co-activated; SMO → GLI → promotes CTNNB1 stabilization; GLI transcription factors share target genes with β-catenin/TCF (MYC, cyclin D1, SNAIL); crosstalk relevant in medulloblastoma and BCC; combined HH+Wnt inhibition under study."
  - target: 01-human/03-molecular/notch
    relation: connects-to
    note: "Hedgehog and Notch pathways interact during embryonic development and cancer; SMO → GLI → activates NOTCH target genes (HES1, HEY1) → cooperative self-renewal in Hh/Notch-active tumor stem cells; both pathways activated in medulloblastoma SHH subgroup and basal cell carcinoma."
  - target: 01-human/03-molecular/myc
    relation: connects-to
    note: "SMO → GLI → direct transcription of MYC at the GLI-binding site in the MYC promoter; GLI-MYC axis drives proliferation in BCC and medulloblastoma; MYC amplification in medulloblastoma SHH-high-risk subgroup; cyclin D1 is also a GLI target → CDK4/6-RB pathway engagement."
  - target: 01-human/03-molecular/bcl-2
    relation: connects-to
    note: "GLI1/GLI2 transcription factors directly bind and activate the BCL-2 promoter → resistance to apoptosis in BCC; BCL-2 overexpression in BCC (~90%) contributes to resistance to vismodegib; BCL-2 inhibitors (venetoclax) under study in vismodegib-resistant or advanced BCC."
  - target: 01-human/03-molecular/ptch1
    relation: connects-to
    note: "PTCH1 inhibits SMO by depleting cholesterol from the ciliary membrane; HH binding to PTCH1 → PTCH1 internalized → SMO accumulates in cilium; PTCH1 LOF (germline Gorlin, somatic BCC) = constitutive SMO; PTCH1 and SMO are the dominant BCC driver genes (~90% and ~40% respectively)."
  - target: 01-human/07-system/basal-cell-carcinoma
    relation: connects-to
    note: "SMO activating mutations (D473H, W535L, V321M) in ~40-50% sporadic BCC; PTCH1 LOF in ~85-90% of BCC; vismodegib and sonidegib target the 7TM allosteric pocket of SMO; cemiplimab (anti-PD-1) approved after SMO inhibitor failure in advanced BCC; BCC is the most common human cancer."
  - target: 01-human/03-molecular/sufu
    relation: connects-to
    note: "SMO activation → SUFU-GLI targeted to cilium tip → SUFU-GLI dissociation → GLI2/3 full-length activators released to nucleus; SUFU LOF mimics constitutive SMO (both yield GLI nuclear) but is SMO-inhibitor-resistant; SMO → KIF7 kinase → promotes SUFU-GLI separation at cilium."
---

# SMO

## Overview

**SMO (Smoothened)** is a 7-transmembrane Frizzled-class GPCR-like protein that serves as the obligate signal transducer of the **canonical Hedgehog (HH) signaling pathway**. SMO is constitutively inhibited by PTCH1 (Patched 1) in the absence of Hedgehog ligand; HH ligand binding relieves PTCH1-mediated SMO suppression → SMO activation → GLI transcription factor nuclear translocation → HH target gene expression. In cancer, SMO is aberrantly activated by mutations that mimic the ligand-activated conformation (sporadic basal cell carcinoma) or by upstream PTCH1 loss-of-function [^sekulic-2012-vismodegib].

**SMO in cancer:**
- **Basal cell carcinoma (BCC):** SMO activating mutations in ~40-50% of sporadic BCC; PTCH1 inactivating mutations in >90% of BCC (upstream pathway activation); vismodegib and sonidegib (SMO inhibitors) approved for locally advanced/metastatic BCC
- **Medulloblastoma (SHH subgroup, ~28% of MB):** PTCH1 mutations (~40%), SMO mutations (~10%), SUFU mutations (~25%); adult patients with SHH-MB respond to vismodegib; pediatric SHH-MB may have different molecular drivers (amplification vs. mutation); vismodegib/sonidegib in select adult SHH-MB
- **Gorlin syndrome (Basal Cell Nevus Syndrome):** Germline PTCH1 mutation → multiple BCCs starting in young adulthood + medulloblastoma + jaw keratocysts + skeletal anomalies; vismodegib reduces new BCC development in Gorlin syndrome [^tang-2012-vismodegib]
- **Other cancers with HH pathway activation:** Rhabdomyosarcoma (~20%), hepatocellular carcinoma, lung squamous cell carcinoma, Merkel cell carcinoma (occasional); SMO inhibitors have variable efficacy in ligand-driven HH activation vs. cell-autonomous SMO/PTCH1 mutations

**Canonical vs. non-canonical HH signaling:**
- Canonical: SHH/DHH/IHH → PTCH1 → SMO → SUFU degradation → GLI2/GLI3 processing → GLI target gene transcription
- Non-canonical: HH-independent GLI activation via KRAS-ERK → can bypass SMO → SMO inhibitors ineffective; highly relevant in pancreatic cancer where Hh signaling is primarily paracrine (stromal, not epithelial) — vismodegib failed in PDAC

## Structure

### SMO protein architecture

SMO is a 787-amino-acid, ~90 kDa GPCR-like protein with a distinct topology:

**N-terminal extracellular domain (ECD, 1-220):**
- **Cysteine-rich domain (CRD, 1-67):** Structurally similar to Frizzled CRDs; directly binds small molecules (including cholesterol and inhibitors); the binding pocket formed by CRD + linker domain is the oxysterol/cholesterol regulatory site; HH-PTCH1 interaction modulates cholesterol flux to this site
- **Linker domain (68-220):** Connects CRD to 7TM bundle; partially flexible; contributes to ligand binding pocket extension

**7-transmembrane (7TM) helical bundle (221-537):**
- Class F GPCR-like topology (shared with Frizzled family)
- Forms the primary drug-binding pocket: vismodegib and sonidegib bind within the 7TM bundle, locking SMO in the inactive conformation (blocking conformational changes needed for activation)
- **D473 (TM5):** Key residue for vismodegib binding; D473H/Y mutation → resistance to vismodegib and sonidegib; V321M, E518K → additional resistance mutations that alter drug-binding pocket

**Intracellular loops (ICL) and tail:**
- ICL3 → G protein coupling (Gαi); SMO couples to Gαi to activate downstream PI3K/Akt (non-canonical)
- C-terminal intracellular tail: Phosphorylation by CK1α/GRK2 → β-arrestin recruitment → SMO internalization (negative feedback); also mediates interaction with HHIP (Hedgehog-interacting protein)

### GLI transcription factors (downstream effectors)

**GLI1 (transcriptional activator):** Strongly activated by SMO; amplified in glioma and BCC; functions as oncogenic transcription factor; no repressor form; marks Hh pathway-active cells
**GLI2 (activator/repressor):** Primary activator in Hh signaling; processed to repressor (GLI2-R) by PKA phosphorylation in Hh-OFF state; required for medulloblastoma development
**GLI3 (primarily repressor):** Processed to strong repressor (GLI3-R) → represses Hh target genes in anterior structures; GLI3 gain-of-function (activator mutations) in some cancers

**Key GLI target genes:**
- *PTCH1* (negative feedback)
- *HHIP* (negative feedback)
- *MYC, MYCN* → proliferation
- *CCND1* (cyclin D1) → G1/S progression
- *BCL-2, BCL-XL* → survival
- *SNAIL* → EMT
- *VEGF* → angiogenesis
- *FOXM1* → cell cycle progression

## Function

### HH pathway signaling mechanism

**HH-OFF state (primary cilia, no ligand):**
1. PTCH1 localizes to primary cilia; inhibits SMO by preventing its ciliary localization (mechanism: PTCH1 acts as a cholesterol transporter that removes cholesterol/oxysterol from the inner leaflet of the ciliary membrane → SMO cannot transition to active conformation)
2. SUFU (Suppressor of Fused) binds GLI proteins in cytoplasm → recruits PKA, CK1, GSK3β → phosphorylates GLI2/3 → proteasomal processing → repressor forms (GLI2-R/GLI3-R) → nuclear import → repress Hh target genes
3. No GLI1 transcription (GLI1 is a HH target gene, not expressed in HH-off cells)

**HH-ON state (HH ligand present):**
1. HH ligand (SHH, DHH, IHH) → binds PTCH1 → PTCH1 inactivation + cilia exit → SMO free
2. SMO accumulates in primary cilia → SMO active conformation (cholesterol/oxysterols now accessible)
3. SUFU releases GLI2/3 in the ciliary tip → full-length GLI2/3 activator forms
4. GLI activators translocate to nucleus → activate Hh target genes (PTCH1, GLI1, CCND1, MYC, BCL-2)

**Primary cilia are essential for canonical Hh signaling:**
Most cancer cells lose primary cilia during dedifferentiation → may lose canonical Hh signaling capacity; this explains why non-canonical (KRAS-GLI) Hh activation is more relevant in some tumors.

### Normal HH pathway roles

**Embryonic development:**
- Pattern formation: SHH from floor plate → dorsoventral patterning of neural tube (SHH gradient → ventral cell types); SHH from notochord → limb patterning (anteroposterior axis); HH from endoderm → pancreatic and gut development
- **SHH mutations:** Holoprosencephaly (HPE-3, midface cleft); loss of midline neural tube patterning
- **PTCH1 germline mutations (Gorlin syndrome):** Multiple BCC + cerebellar medulloblastoma + ovarian fibroma + jaw keratocysts + skeletal defects

**Stem cell maintenance:**
- Hair follicle bulge → SHH from specialized hair cells → Hh maintains stem cell pool; hair follicle cycling requires periodic Hh signaling; BCC may arise from Hh-activated follicle stem cells
- Intestinal stem cells: Minor role compared to Wnt
- Lung and prostate: HH ligand from stroma → Hh maintains epithelial progenitors (paracrine Hh)

## Mechanism

### SMO inhibitors

**Vismodegib (GDC-0449, Erivedge — Genentech/Roche):** [^sekulic-2012-vismodegib]
- First approved SMO inhibitor (FDA 2012); binds 7TM bundle of SMO → allosteric inhibition of SMO → GLI repression
- **ERASER (advanced BCC):** ORR 43% (metastatic), 30% (locally advanced); median DOR 7.6 months
- **Gorlin syndrome (BOLT trial):** Reduces new BCC formation by >75%; tumor regression
- Toxicities: Muscle cramps (68%), alopecia (64%), dysgeusia (51%), weight loss, fatigue; highly teratogenic (category X — causes midline defects via HH pathway role in embryogenesis)
- Acquired resistance: D473H/G/Y, V321M (SMO mutations); GLI2 amplification; KRAS activation (bypass); SMO splice variants

**Sonidegib (LDE225, Odomzo — Novartis):**
- Selective SMO inhibitor; binds same pocket as vismodegib but different binding contacts → partially active against some vismodegib-resistant mutations
- **BOLT trial (advanced BCC):** ORR 43% (locally advanced), 15% (metastatic) at 200 mg dose
- FDA approved 2015 for locally advanced BCC
- Similar toxicity profile to vismodegib

**Glasdegib (PF-04449913, Daurismo — Pfizer):**
- SMO inhibitor approved for AML (not BCC) in combination with low-dose cytarabine; active in AML with HH pathway activation
- BCC trials ongoing

### SMO inhibitor resistance mechanisms

**On-target resistance:**
- **D473H:** Most common; ~50% of resistant BCC; disrupts critical hydrogen bond with vismodegib's carboxamide; maintains partial signaling despite drug binding
- **V321M, E518K:** Less common mutations in 7TM bundle; structural changes reducing drug affinity
- SMO mutations can be identified in resistant BCC by sequencing; some respond to sonidegib if vismodegib-resistant (incomplete cross-resistance for some mutations)

**Downstream bypass:**
- **GLI2 amplification:** Bypasses SMO → constitutive GLI transcription regardless of SMO inhibition
- **KRAS/BRAF activation:** → ERK-mediated Gli stabilization
- **SUFU loss:** Releases full-length GLI → constitutive nuclear GLI activity

**Treatment strategy after SMO inhibitor resistance:**
- Cemiplimab (anti-PD-1): ~30% ORR; FDA approved for advanced BCC after SMO inhibitor progression
- Clinical trials of Gli inhibitors (GANT61 analogues, arsenic trioxide) in SMO-resistant BCC
- Surgery/radiation for localized resistant lesions

## Connections

- `connects-to` → **[Wnt/β-catenin](../../03-molecular/wnt-beta-catenin/README.md)** — Hedgehog and Wnt pathways are frequently co-activated; SMO → GLI → promotes CTNNB1 stabilization; GLI transcription factors share target genes with β-catenin/TCF (MYC, cyclin D1, SNAIL); crosstalk is particularly relevant in medulloblastoma and BCC; combined HH+Wnt inhibition under study.
- `connects-to` → **[Notch](../../03-molecular/notch/README.md)** — Hedgehog and Notch pathways interact during embryonic development and cancer; SMO → GLI → activates NOTCH target genes (HES1, HEY1) → cooperative self-renewal in Hh/Notch-active tumor stem cells; both pathways activated in medulloblastoma SHH subgroup and basal cell carcinoma.
- `connects-to` → **[MYC](../../03-molecular/myc/README.md)** — SMO → GLI → direct transcription of MYC at the GLI-binding site in the MYC promoter; GLI-MYC axis drives proliferation in BCC and medulloblastoma; MYC amplification in medulloblastoma SHH-high-risk subgroup; cyclin D1 is also a GLI target → CDK4/6-RB pathway engagement.
- `connects-to` → **[BCL-2](../../03-molecular/bcl-2/README.md)** — GLI1/GLI2 transcription factors directly bind and activate the BCL-2 promoter → resistance to apoptosis in BCC; BCL-2 overexpression in BCC (~90%) contributes to resistance to vismodegib; BCL-2 inhibitors (venetoclax) under study in vismodegib-resistant or advanced BCC.
- `connects-to` → **[PTCH1](../../03-molecular/ptch1/README.md)** — PTCH1 inhibits SMO by depleting cholesterol from the ciliary membrane; HH binding to PTCH1 → PTCH1 internalized → SMO accumulates in cilium; PTCH1 LOF (germline Gorlin, somatic BCC) = constitutive SMO; PTCH1 and SMO are the dominant BCC driver genes (~90% and ~40% respectively).
- `connects-to` → **[Basal Cell Carcinoma](../../07-system/basal-cell-carcinoma/README.md)** — SMO activating mutations (D473H, W535L, V321M) in ~40-50% sporadic BCC; PTCH1 LOF in ~85-90% of BCC; vismodegib and sonidegib target the 7TM allosteric pocket of SMO; cemiplimab (anti-PD-1) approved after SMO inhibitor failure in advanced BCC; BCC is the most common human cancer.
- `connects-to` → **[SUFU](../../03-molecular/sufu/README.md)** — SMO activation → SUFU-GLI targeted to cilium tip → SUFU-GLI dissociation → GLI2/3 full-length activators released to nucleus; SUFU LOF mimics constitutive SMO (both yield GLI nuclear) but is SMO-inhibitor-resistant; SMO → KIF7 kinase → promotes SUFU-GLI separation at cilium.

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^sekulic-2012-vismodegib]: Sekulic A, Migden MR, Oro AE, et al. Efficacy and safety of vismodegib in advanced basal-cell carcinoma. *N Engl J Med.* 2012;366(23):2171-2179. [doi:10.1056/NEJMoa1113600](https://doi.org/10.1056/NEJMoa1113600) · [PubMed 22670902](https://pubmed.ncbi.nlm.nih.gov/22670902/)
[^tang-2012-vismodegib]: Tang JY, Mackay-Wiggan JM, Aszterbaum M, et al. Inhibiting the hedgehog pathway in patients with the basal-cell nevus syndrome. *N Engl J Med.* 2012;366(23):2180-2188. [doi:10.1056/NEJMoa1113538](https://doi.org/10.1056/NEJMoa1113538) · [PubMed 22670904](https://pubmed.ncbi.nlm.nih.gov/22670904/)
