---
schema: human-scale-entry/v1
id: hla-b27
name: HLA-B27
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-07
summary: "HLA-B27 is an MHC Class I allele (chr6p21.3) carried by ~8% of Europeans; present in ~90% of ankylosing spondylitis patients; misfolding in ER drives UPR → IL-23 → Th17 → IL-17A axis; also associates with reactive arthritis, anterior uveitis, and IBD spondyloarthropathy."
aliases: ["HLA-B27", "HLA-B*27", "B27", "HLA-B*27:05", "MHC Class I B27", "HLA-B antigen", "spondyloarthropathy HLA", "ankylosing spondylitis gene"]
sources:
  - id: brown-2016-hlab27-review
    type: peer-reviewed
    cite: "Brown MA, Bradbury LA. The genetics of ankylosing spondylitis and axial spondyloarthritis. Rheum Dis Clin North Am. 2018;44(2):229-244."
    doi: "10.1016/j.rdc.2018.01.001"
    pmid: "29622524"
    url: "https://doi.org/10.1016/j.rdc.2018.01.001"
  - id: reveille-2012-hlab27-as
    type: peer-reviewed
    cite: "Reveille JD. Genetics of spondyloarthritis—beyond the MHC. Nat Rev Rheumatol. 2012;8(5):296-304."
    doi: "10.1038/nrrheum.2012.41"
    pmid: "22450551"
    url: "https://doi.org/10.1038/nrrheum.2012.41"
  - id: mear-1999-hlab27-misfolding
    type: peer-reviewed
    cite: "Mear JP, Schreiber KL, Münz C, et al. Misfolding of HLA-B27 as a result of its B pocket suggests a novel mechanism for its role in susceptibility to spondyloarthropathies. J Immunol. 1999;163(12):6665-70."
    doi: "10.4049/jimmunol.163.12.6665"
    pmid: "10586063"
    url: "https://doi.org/10.4049/jimmunol.163.12.6665"
cross_links:
  - target: 01-human/07-system/ankylosing-spondylitis
    relation: connects-to
    note: "HLA-B27 is the strongest genetic risk factor for AS (OR ~90); present in ~90% of AS patients vs. 8% controls; B*27:05 confers highest risk; B*27:09 does not — conformational differences explain; misfolding in ER → UPR → IL-23 upregulation → enthesitis and ankylosis."
  - target: 01-human/03-molecular/il-17a
    relation: connects-to
    note: "HLA-B27 misfolding → UPR stress → STAT3 → IL-23 upregulation in macrophages → Th17 and ILC3 IL-17A production → enthesitis, synovitis, and new bone formation in axSpA; IL-17A inhibitors (secukinumab, ixekizumab) are highly effective in HLA-B27+ axSpA."
  - target: 01-human/03-molecular/il-23
    relation: connects-to
    note: "HLA-B27 ER stress → IRE1α/XBP1 UPR arm → ↑IL-23 secretion by macrophages/DCs; IL-23 signals via STAT3 → RORγt → Th17 cells → IL-17A; IL-23 inhibitors (risankizumab, guselkumab) are under evaluation in axSpA; the B27-UPR-IL23-IL17 axis is the central AS disease pathway."
---

# HLA-B27

## Overview

**HLA-B27** is a **human leukocyte antigen (HLA) Class I** allele encoded on chromosome 6p21.3 within the major histocompatibility complex (MHC) — the most gene-dense region of the human genome. HLA-B27 is the **most powerful single genetic risk factor** for a group of inflammatory arthritides collectively termed **spondyloarthropathies (SpA)**: ankylosing spondylitis (AS), reactive arthritis (ReA), psoriatic arthritis with axial involvement, enteropathic arthritis, and juvenile-onset AS [^brown-2016-hlab27-review].

**Population genetics:**
- HLA-B27 prevalence in European populations: ~8% (ranges from 1-2% in Japanese to 50% in some Indigenous Arctic populations)
- In ankylosing spondylitis: present in ~90-95% of AS patients vs. ~8% controls → odds ratio of ~90 — one of the strongest HLA-disease associations in human genetics
- Healthy HLA-B27+ individuals have a lifetime AS risk of only ~1-5%, demonstrating that HLA-B27 is necessary but not sufficient for disease
- Familial aggregation: relative risk in first-degree relatives of AS patients = 63 (vs. general population) — most of this is attributable to HLA-B27

**HLA-B27 subtypes (>180 known):**

| Subtype | AS association | Key population |
|---|---|---|
| B*27:05 | Strong (reference AS allele) | Northern European, most worldwide |
| B*27:02 | Strong | Mediterranean |
| B*27:04 | Strong | East Asian |
| B*27:09 | **Absent** (does not cause AS) | Sardinian |
| B*27:07 | Moderate | South Asian; IBD-SpA association |
| B*27:06 | Absent | Southeast Asian |

The critical observation that B*27:09 (which differs from B*27:05 at only amino acid 116 in the peptide-binding B pocket) does **not** associate with AS has been central to understanding the molecular basis of HLA-B27 pathogenicity.

## Structure

### MHC Class I architecture

HLA-B27 is an MHC Class I heterodimer assembled in the endoplasmic reticulum:

**α-chain (HLA-B27 heavy chain; 44 kDa):**
- Encoded by *HLA-B* on chromosome 6p21.3
- Three extracellular domains:
  - **α1 domain** (aa 1–90): peptide-binding groove (N-terminal half)
  - **α2 domain** (aa 91–180): peptide-binding groove (C-terminal half); polymorphic between HLA alleles
  - **α3 domain** (aa 181–274): immunoglobulin-like; binds CD8 coreceptor
- Transmembrane domain + cytoplasmic tail

**β2-microglobulin (β2m; 12 kDa):**
- Encoded by *B2M* on chromosome 15q21.1 (NOT in MHC)
- Invariant (same across all Class I alleles)
- Required for proper heavy chain folding and surface expression

**Peptide (8-10 mer):**
- Loaded in the ER via the peptide-loading complex (PLC): TAP1/TAP2 + tapasin + calreticulin + ERp57
- Proteasome (cytoplasmic) generates peptides from intracellular proteins → transported to ER lumen by TAP → PLC trims N-terminus (ERAP1/2) → loaded onto Class I groove

**HLA-B27 peptide-binding groove (PBG) features:**
- **B pocket** — a deep, electronegative pocket accommodating the P2 (position 2) anchor residue of the peptide
- B*27:05: deep B pocket; **Asp-116** forms hydrogen bonds with the P2 Arg of peptide; strong preference for Arg at P2
- B*27:09: **His-116** instead of Asp-116 → shallower B pocket → altered peptide repertoire → different cellular stress responses
- This single amino acid difference at position 116 explains why B*27:09 does not cause AS — supporting the misfolding or free heavy chain hypotheses

## Function

### Normal function: antigen presentation to CD8+ T cells

HLA-B27, like all MHC Class I molecules, presents **intracellular peptides** to **CD8+ cytotoxic T lymphocytes (CTL)**:

1. Intracellular proteins (viral, bacterial, self) → proteasomal degradation → 8-10 mer peptides
2. TAP1/TAP2 translocates peptides into ER lumen
3. ERAP1/ERAP2 trim N-terminus to optimal length
4. Peptide loads into HLA-B27 groove via peptide-loading complex (tapasin, ERp57, calreticulin, calnexin)
5. Stable peptide-HLA-B27-β2m complex → Golgi → plasma membrane
6. CD8+ T cells recognize the peptide-HLA complex via TCR + CD8 coreceptor (CD8 binds α3 domain)
7. Intracellular antigen presentation → killing of infected or cancerous cells

### Pathogenic mechanisms in spondyloarthropathy

Three non-exclusive hypotheses:

**1. Misfolding/UPR hypothesis (currently most supported):**
- HLA-B27 heavy chains are intrinsically prone to misfolding in the ER (likely due to the cysteine-rich B pocket and reduced peptide repertoire compatibility)
- ER-accumulated misfolded HLA-B27 heavy chains → **unfolded protein response (UPR):**
  - **IRE1α → XBP1s** (spliced XBP1): most important UPR arm in SpA; XBP1s → ↑IL-23 expression in macrophages → IL-23 → STAT3 → RORγt → Th17/ILC3 → **IL-17A** → entheseal inflammation
  - **ATF6, PERK-eIF2α** arms also activated
- Supporting evidence: B*27:09 (no AS risk) does NOT aggregate in ER; UPR reduction by tapasin overexpression reduces IL-23 in B27-transgenic cells [^mear-1999-hlab27-misfolding]

**2. Arthritogenic peptide hypothesis:**
- HLA-B27 presents unique peptides (arthritogenic epitopes) from bacterial proteins via molecular mimicry to autoreactive CD8+ T cells
- Candidate mimicry antigens: *Klebsiella pneumoniae* nitroreductase (peptide homology to HLA-B27 sequence); *Chlamydia*, *Shigella*, *Salmonella* peptides (triggers of reactive arthritis)
- Reactive arthritis: classically follows urogenital Chlamydia or enteric (Salmonella, Shigella, Campylobacter) infection in HLA-B27+ individuals

**3. Free heavy chain (FHC) hypothesis:**
- HLA-B27 heavy chains can form homodimers on the cell surface or in early endosomes (FHC β2m-free dimers)
- FHC dimers bind NK cell receptors (KIR3DL2 on NK and T cells) and macrophage receptors (LILRB2/ILT4) → activating signals → IL-23 production
- NK cell KIR3DL2 recognition of FHC may contribute to innate immune activation at entheses

## Mechanism

### HLA-B27 → IL-23 → IL-17A → enthesitis pathogenic cascade

```
HLA-B27 misfolding in ER
    ↓
UPR (IRE1α → XBP1s; ATF6; PERK)
    ↓
↑IL-23 in macrophages/DCs (XBP1s-driven)
    ↓
IL-23 → IL-23R on Th17 cells and ILC3
    ↓
STAT3 → RORγt → ↑IL-17A + IL-22
    ↓ (entheses)
IL-17A → RANKL + MMP3/9 → osteoclast activation → bone erosion
IL-17A → WNT pathway → osteoblast activation → new bone (syndesmophytes)
IL-17A → CXCL5/8 → neutrophil recruitment → entheseal inflammation
    ↓
Chronic enthesitis → sacroiliitis → spinal fusion (AS)
```

**ERAP1 modifier effect:** ERAP1 (ER aminopeptidase 1) is encoded on chromosome 5q15; it trims peptides for optimal HLA-I loading. ERAP1 polymorphisms only increase AS risk in the context of HLA-B27 — strong epistasis. This suggests ERAP1 modifies the peptide repertoire available to HLA-B27, altering the frequency of misfolding-prone versus well-folded HLA-B27/peptide complexes.

**IL-23 inhibitor paradox in axSpA:** Despite IL-23 being pathologically upstream of IL-17A in AS, IL-23 inhibitors (risankizumab, guselkumab) have shown **surprisingly modest efficacy** in AS compared to IL-17A inhibitors — suggesting that ILC3 (which can produce IL-17A independently of IL-23 at entheses) or other IL-23-independent IL-17A sources are important at the effector site.

## Connections

- `connects-to` → **[Ankylosing Spondylitis](../../07-system/ankylosing-spondylitis/README.md)** — HLA-B27 is the strongest genetic risk factor for AS (OR ~90); present in ~90% of AS patients vs. 8% controls; B*27:05 confers highest risk; B*27:09 does not — conformational differences explain; misfolding in ER → UPR → IL-23 upregulation → enthesitis and ankylosis.
- `connects-to` → **[IL-17A](../il-17a/README.md)** — HLA-B27 misfolding → UPR stress → STAT3 → IL-23 upregulation in macrophages → Th17 and ILC3 IL-17A production → enthesitis, synovitis, and new bone formation in axSpA; IL-17A inhibitors (secukinumab, ixekizumab) are highly effective in HLA-B27+ axSpA.
- `connects-to` → **[IL-23](../il-23/README.md)** — HLA-B27 ER stress → IRE1α/XBP1 UPR arm → ↑IL-23 secretion by macrophages/DCs; IL-23 signals via STAT3 → RORγt → Th17 cells → IL-17A; IL-23 inhibitors (risankizumab, guselkumab) are under evaluation in axSpA; the B27-UPR-IL23-IL17 axis is the central AS disease pathway.

[^brown-2016-hlab27-review]: Brown MA, Bradbury LA. The genetics of ankylosing spondylitis and axial spondyloarthritis. *Rheum Dis Clin North Am.* 2018;44(2):229-244. [doi:10.1016/j.rdc.2018.01.001](https://doi.org/10.1016/j.rdc.2018.01.001) · [PubMed 29622524](https://pubmed.ncbi.nlm.nih.gov/29622524/)
[^reveille-2012-hlab27-as]: Reveille JD. Genetics of spondyloarthritis — beyond the MHC. *Nat Rev Rheumatol.* 2012;8(5):296-304. [doi:10.1038/nrrheum.2012.41](https://doi.org/10.1038/nrrheum.2012.41) · [PubMed 22450551](https://pubmed.ncbi.nlm.nih.gov/22450551/)
[^mear-1999-hlab27-misfolding]: Mear JP, Schreiber KL, Münz C, et al. Misfolding of HLA-B27 as a result of its B pocket suggests a novel mechanism for its role in susceptibility to spondyloarthropathies. *J Immunol.* 1999;163(12):6665-70. [doi:10.4049/jimmunol.163.12.6665](https://doi.org/10.4049/jimmunol.163.12.6665) · [PubMed 10586063](https://pubmed.ncbi.nlm.nih.gov/10586063/)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
