---
schema: human-scale-entry/v1
id: ctnna1
name: CTNNA1
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-07
summary: "CTNNA1 (alpha-E-catenin) links E-cadherin–β-catenin to F-actin to maintain epithelial adhesion; LOF → loss of cadherin-cytoskeleton coupling → diffuse growth pattern; somatic CTNNA1 loss drives signet ring cell GC; germline CTNNA1 = HDGC in CDH1-negative families."
aliases: ["CTNNA1", "alpha-E-catenin", "alpha-catenin", "CTNNA1 HDGC", "CTNNA1 gastric cancer", "alpha-catenin E-cadherin", "CTNNA1 tumor suppressor", "alpha-catenin actin", "cadherin-catenin complex"]
sources:
  - id: majewski-2013-ctnna1
    type: peer-reviewed
    cite: "Majewski IJ, Kluijt I, Cats A, et al. An alpha-E-catenin (CTNNA1) mutation in hereditary diffuse gastric cancer. J Pathol. 2013;229(5):621-629."
    doi: "10.1002/path.4155"
    pmid: "23225153"
    url: "https://doi.org/10.1002/path.4155"
  - id: hansford-2015-hdgc
    type: peer-reviewed
    cite: "Hansford S, Kaurah P, Li-Chang H, et al. Hereditary Diffuse Gastric Cancer Syndrome: CDH1 Mutations and Beyond. JAMA Oncol. 2015;1(1):23-32."
    doi: "10.1001/jamaoncol.2014.168"
    pmid: "26182300"
    url: "https://doi.org/10.1001/jamaoncol.2014.168"
cross_links:
  - target: 01-human/03-molecular/cdh1
    relation: connects-to
    note: "CTNNA1 (alpha-E-catenin) and CDH1 (E-cadherin) function in the same cadherin-catenin complex; CDH1 LOF or CTNNA1 LOF both disrupt epithelial adhesion → diffuse gastric cancer; germline CDH1 (~25%) and CTNNA1 (~2-5%) cause HDGC; CDH1 is the primary HDGC gene."
  - target: 01-human/03-molecular/ctnnb1
    relation: connects-to
    note: "CTNNA1 binds β-catenin (CTNNB1) at the cadherin-catenin complex and links it to F-actin; CTNNA1 LOF uncouples the cytoskeleton from the complex; distinct from CTNNB1 Wnt oncogenic role; CTNNA1 does not participate in Wnt/TCF signaling — its function is mechanical adhesion."
  - target: 01-human/07-system/gastric-cancer
    relation: connects-to
    note: "CTNNA1 somatic loss drives signet ring cell gastric cancer via epithelial adhesion loss; somatic CTNNA1 LOH in CDH1-germline HDGC tumors as the second hit; Lauren diffuse-type GC driven by loss of E-cadherin/alpha-catenin axis; somatic CTNNA1 loss in ~5-10% sporadic GC."
  - target: 01-human/07-system/hereditary-diffuse-gastric-cancer
    relation: connects-to
    note: "Germline CTNNA1 LOF causes HDGC in CDH1-negative families (~2-5% of HDGC); prophylactic gastrectomy is recommended for pathogenic CTNNA1 carriers; penetrance estimated similar to CDH1; somatic CTNNA1 serves as the second hit in CDH1-germline HDGC tumors."
  - target: 01-human/07-system/breast-cancer
    relation: connects-to
    note: "Germline CTNNA1 LOF → elevated lobular breast carcinoma risk; same E-cadherin-alpha-catenin axis disrupted in sporadic lobular BC; annual breast MRI from age 30 recommended for CTNNA1 carriers; CTNNA1 loss → epithelial cohesion failure → invasive lobular cancer pattern."
  - target: 01-human/03-molecular/wnt-beta-catenin
    relation: connects-to
    note: "CTNNA1 binds β-catenin at adherens junctions but does NOT activate Wnt/TCF nuclear signaling; CTNNA1 LOF causes adhesion loss without activating Wnt targets (MYC, CCND1); this mechanistic distinction separates CTNNA1 from CTNNB1 GOF — purely adhesion-dependent tumourigenesis."
  - target: 01-human/03-molecular/apc
    relation: connects-to
    note: "APC scaffolds the β-catenin destruction complex; CTNNA1 LOF is mechanistically distinct: CTNNA1 tumors lack nuclear β-catenin; APC germline (FAP) causes CRC/desmoid vs CTNNA1 germline causes diffuse GC/lobular BC — complementary tumor suppressors in the catenin axis."
---

# CTNNA1

## Overview

**CTNNA1** (Catenin Alpha 1; also called **alpha-E-catenin**) is a 906 amino acid (100 kDa) cytoplasmic protein that serves as a **structural and mechanosensory linker** between the **E-cadherin–β-catenin adhesion complex** at the plasma membrane and the **F-actin cytoskeleton**. CTNNA1 is the canonical alpha-catenin expressed in epithelial cells; it converts cell–cell mechanical tension into cytoskeletal organization and maintains the integrity of adherens junctions. Unlike β-catenin (CTNNB1), which has a dual role in both adhesion and Wnt/TCF signaling, CTNNA1 functions exclusively in **epithelial adhesion and mechanotransduction** — it does not enter the nucleus or participate in transcriptional regulation. CTNNA1 was linked to hereditary diffuse gastric cancer in CDH1-negative families by Majewski et al. in 2013 [^majewski-2013-ctnna1] [^hansford-2015-hdgc].

**E-cadherin–catenin complex (canonical model):**

```
E-cadherin (CDH1) extracellular — homotypic cell-cell adhesion
    │
    ▼  (cytoplasmic tail)
β-catenin (CTNNB1) — binds E-cadherin cytoplasmic tail
    │
    ▼  (α-catenin binding)
CTNNA1 (alpha-E-catenin) — tension-dependent F-actin binding
    │
    ▼
F-actin cytoskeleton — mechanical coupling, junctional stability
```

CTNNA1 exists in two states: a **monomeric, open** conformation (lower F-actin affinity; β-catenin-bound) and a **homodimeric** conformation (higher F-actin affinity; tension-induced). The tension-dependent switch allows the complex to sense mechanical force and reinforce junctions under stress.

## Structure

### CTNNA1 protein domains

**N-terminal domain (aa 1-270) — Dimerization and β-catenin binding:**
- Contains the primary **β-catenin binding interface**: a coiled-coil interaction surface engages the arm-repeat domain of CTNNB1
- Also mediates CTNNA1 homodimerization: the N-terminal VH1 helix bundle dimerizes with a symmetry-related helix from a second CTNNA1 molecule
- Mutually exclusive: CTNNA1 cannot simultaneously bind β-catenin and homodimerize — the two interfaces partially overlap at the α1 helix; monomer is the β-catenin-bound state; homodimer is the free, F-actin-high state
- VINCULIN-binding site (VH1): under mechanical tension, the N-terminal bundle opens to expose the M domain binding site for vinculin (VCL); vinculin reinforces actin linkage under high tension

**Middle domain (aa 271-630) — Mechanosensory and regulation:**
- Contains a series of coiled-coil bundles (M domain: M1-M2-M3) that form a catch-bond with F-actin under tension
- The M1-M2 bundle masks the vinculin-binding helix in the relaxed (low-tension) state; actomyosin-driven tension exposes the vinculin binding site → vinculin recruitment → F-actin clamping
- This mechanical allosteric switch makes the cadherin-catenin complex a **force-sensor**: weak tension = dynamic junction; strong tension = reinforced, stable junction

**C-terminal domain (aa 631-906) — F-actin binding:**
- Primary direct F-actin-binding activity resides in the C-terminal ABD (actin-binding domain)
- Two separate actin-binding interfaces: one contacts the actin filament surface; one promotes F-actin bundling
- ABD binding to F-actin is not force-dependent per se but is enhanced in the context of tension-opened middle domain conformation

**Pathogenic variant spectrum (germline CTNNA1 LOF):**
- Frameshift, nonsense, and canonical splice variants → protein truncation → loss of C-terminal ABD → failed actin linkage
- Missense in the β-catenin-binding interface: disrupts E-cadherin complex assembly
- Large deletions: MLPA-detectable
- Penetrance: incompletely established; HDGC families with CTNNA1 pathogenic variants show incomplete penetrance (some carriers reach age 50-60 without gastric cancer); prophylactic gastrectomy reveals early SRCC foci in most carriers

## Function

### CTNNA1 in epithelial homeostasis

**Adherens junction maintenance:**
CTNNA1 is essential for stable, force-bearing adherens junctions. In epithelial monolayers:
1. E-cadherin (CDH1) mediates homotypic cell–cell adhesion via extracellular Ca²⁺-dependent binding
2. The CDH1 cytoplasmic tail recruits CTNNB1 and p120-catenin
3. CTNNB1 recruits CTNNA1 → CTNNA1 ABD → F-actin → junction stabilized
4. Actomyosin tension at the junction opens CTNNA1 → vinculin binding → belt-like actin cable reinforced (zonula adherens)

Without CTNNA1:
- CDH1-CTNNB1 complex at plasma membrane but mechanically uncoupled from cytoskeleton
- Cells lose cohesive epithelial organization → adopt mesenchymal, migratory phenotype
- In vivo: cells detach and invade as single cells → **diffuse growth pattern** (distinct from glandular/intestinal growth of CDH1-expressing carcinoma)

**CTNNA1 and cell polarity:**
Alpha-catenin coordinates with Par complex (PARD3-PARD6-aPKC) and Scribble polarity complex to establish apical-basolateral polarity. CTNNA1 LOF → polarity disruption → loss of epithelial architecture contributing to signet ring cell morphology (cells lose apical-basolateral identity; mucin accumulates).

**CTNNA1 vs CTNNB1 signaling — an important distinction:**
| Feature | CTNNA1 | CTNNB1 (β-catenin) |
|---|---|---|
| Location | Cytoplasm/junctions | Cytoplasm, nucleus (Wnt) |
| Wnt signaling | No role | TCF transcriptional activator |
| APC interaction | None | APC destruction complex member |
| Tumor function | Tumor suppressor (LOF) | Oncogene (GOF) in CRC |
| Mutation in cancer | LOF (frameshift, deletion) | GOF (missense Ser/Thr) |

### CTNNA1 as a tumor suppressor

**Somatic CTNNA1 loss in gastric cancer:**
- CTNNA1 LOH (loss of heterozygosity at 5q31.2) detected in ~5-10% of sporadic diffuse-type gastric cancers
- In CDH1-germline HDGC tumors: CTNNA1 is occasionally the **second somatic hit** that inactivates the remaining CDH1-CTNNA1 axis in cells that have already lost CDH1 function, or vice versa
- Signet ring cell carcinoma (SRCC) is the histological correlate: individual malignant cells with mucin-filled cytoplasm and peripherally displaced nucleus, lacking cohesive glandular architecture

**CTNNA1 LOF phenotype in model systems:**
- *Ctnna1* knockout mice: embryonic lethal (early embryo cannot form proper epithelial layers); conditional gastric knockout: gastric hyperplasia + loss of glandular organization
- Human gastric organoids with CTNNA1 CRISPR knockout: loss of epithelial organization, increased invasive behavior in 3D culture; rescued by re-expression of CTNNA1

## Mechanism

### Germline CTNNA1 and HDGC

**CTNNA1 germline LOF was identified by Majewski et al. (2013)** in a CDH1-negative HDGC family (Dutch, multigenerational) with multiple cases of diffuse gastric cancer and lobular breast cancer. Subsequent HDGC cohort sequencing (Hansford et al. 2015, JAMA Oncology) established CTNNA1 as a validated HDGC predisposition gene in ~2-5% of HDGC probands who test negative for CDH1:

**CTNNA1-germline HDGC features:**
- Diffuse/signet ring cell gastric cancer; lobular breast cancer (same biological mechanism as CDH1 — E-cadherin pathway loss)
- Prophylactic total gastrectomy: recommended for pathogenic CTNNA1 carriers after genetic counseling; gastrectomy specimens show early SRCC foci (T1a) in the majority of carriers who undergo prophylactic surgery, validating the recommendation
- Penetrance: ~50-80% lifetime GC risk estimated but data limited (smaller family cohorts than CDH1); conservative estimates approach CDH1 penetrance
- Age of onset: 30s-60s; similar to CDH1-HDGC (which peaks 38-42 years); earlier-onset cases exist

**CTNNA1 somatic second hit in CDH1-germline tumors:**
In CDH1-germline HDGC, the somatic second hit is detected as LOH at CDH1 locus (16q22) in most tumor foci. However, some tumor foci in CDH1-germline stomachs instead show CTNNA1 somatic LOH at 5q31 — suggesting that the CTNNA1 pathway serves as an alternative or cooperating second hit mechanism. The shared E-cadherin-catenin pathway axis makes CTNNA1 functional loss equivalent to CDH1 functional loss in terms of downstream diffuse growth phenotype.

**CTNNA1 and lobular breast carcinoma:**
Lobular breast carcinoma is defined by E-cadherin loss (CDH1 somatic loss in ~85% of sporadic lobular BC). In CDH1-germline HDGC, lobular BC risk is elevated. Similarly, CTNNA1-germline carriers have elevated lobular BC risk because CTNNA1 LOF functionally disrupts the same E-cadherin-catenin complex required for breast epithelial cohesion. Annual breast MRI from age 30 is recommended for CTNNA1 carriers, mirroring CDH1-HDGC guidelines.

## Connections

- `connects-to` → **[CDH1](../../03-molecular/cdh1/README.md)** — CTNNA1 (alpha-E-catenin) and CDH1 (E-cadherin) function in the same cadherin-catenin complex; CDH1 LOF or CTNNA1 LOF both disrupt epithelial adhesion → diffuse gastric cancer; germline CDH1 (~25%) and CTNNA1 (~2-5%) cause HDGC; CDH1 is the primary HDGC gene.
- `connects-to` → **[CTNNB1](../../03-molecular/ctnnb1/README.md)** — CTNNA1 binds β-catenin (CTNNB1) at the cadherin-catenin complex and links it to F-actin; CTNNA1 LOF uncouples the cytoskeleton from the complex; distinct from CTNNB1 Wnt oncogenic role; CTNNA1 does not participate in Wnt/TCF signaling — its function is mechanical adhesion.
- `connects-to` → **[Gastric Cancer](../../07-system/gastric-cancer/README.md)** — CTNNA1 somatic loss drives signet ring cell gastric cancer via epithelial adhesion loss; somatic CTNNA1 LOH in CDH1-germline HDGC tumors as the second hit; Lauren diffuse-type GC driven by loss of E-cadherin/alpha-catenin axis; somatic CTNNA1 loss in ~5-10% sporadic GC.
- `connects-to` → **[Hereditary Diffuse Gastric Cancer](../../07-system/hereditary-diffuse-gastric-cancer/README.md)** — Germline CTNNA1 LOF causes HDGC in CDH1-negative families (~2-5% of HDGC); prophylactic gastrectomy is recommended for pathogenic CTNNA1 carriers; penetrance estimated similar to CDH1; somatic CTNNA1 serves as the second hit in CDH1-germline HDGC tumors.
- `connects-to` → **[Breast Cancer](../../07-system/breast-cancer/README.md)** — germline CTNNA1 LOF → elevated lobular breast carcinoma risk (same E-cadherin-alpha-catenin axis disrupted in sporadic lobular BC); annual breast MRI from age 30 recommended for CTNNA1 carriers; CTNNA1 loss → invasive lobular cancer pattern.
- `connects-to` → **[WNT/β-catenin](../../03-molecular/wnt-beta-catenin/README.md)** — CTNNA1 binds β-catenin at adherens junctions but does NOT participate in Wnt/TCF nuclear signaling; CTNNA1 LOF causes adhesion loss without activating Wnt target genes (MYC, CCND1); mechanistic distinction: CTNNA1 tumors lack nuclear β-catenin unlike APC-LOF or CTNNB1-GOF tumors.
- `connects-to` → **[APC](../../03-molecular/apc/README.md)** — APC scaffolds the β-catenin destruction complex; CTNNA1 LOF is mechanistically distinct — CTNNA1 tumors lack nuclear β-catenin; APC germline (FAP) causes CRC/desmoid while CTNNA1 germline causes diffuse GC/lobular BC; complementary tumor suppressors in the catenin axis.

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^majewski-2013-ctnna1]: Majewski IJ, Kluijt I, Cats A, et al. An alpha-E-catenin (CTNNA1) mutation in hereditary diffuse gastric cancer. *J Pathol.* 2013;229(5):621-629. [doi:10.1002/path.4155](https://doi.org/10.1002/path.4155) · [PubMed 23225153](https://pubmed.ncbi.nlm.nih.gov/23225153/)
[^hansford-2015-hdgc]: Hansford S, Kaurah P, Li-Chang H, et al. Hereditary Diffuse Gastric Cancer Syndrome: CDH1 Mutations and Beyond. *JAMA Oncol.* 2015;1(1):23-32. [doi:10.1001/jamaoncol.2014.168](https://doi.org/10.1001/jamaoncol.2014.168) · [PubMed 26182300](https://pubmed.ncbi.nlm.nih.gov/26182300/)
