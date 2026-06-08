---
schema: human-scale-entry/v1
id: ccr5
name: CCR5
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-08
summary: "CCR5 (CC chemokine receptor 5; 7-TM GPCR) is the principal HIV-1 co-receptor for R5-tropic entry; CCL3/CCL4/CCL5 natural ligands; CCR5-Δ32 homozygosity → HIV-1 resistance; maraviroc (CCR5 antagonist) is the only approved HIV entry inhibitor; expressed on macrophages and T cells."
aliases: ["CC chemokine receptor 5", "CCR-5", "CD195", "RANTES receptor", "CC-CKR-5", "CKR-5", "maraviroc target", "HIV co-receptor"]
sources:
  - id: liu-1996-ccr5-delta32
    type: peer-reviewed
    cite: "Liu R, Paxton WA, Choe S, et al. Homozygous defect in HIV-1 coreceptor accounts for resistance of some multiply-exposed individuals to HIV-1 infection. Cell. 1996;86(3):367-377."
    doi: "10.1016/S0092-8674(00)80110-5"
    pmid: "8756719"
    url: "https://doi.org/10.1016/S0092-8674(00)80110-5"
    accessed: "2026-06-08"
  - id: samson-1996-ccr5-coreceptor
    type: peer-reviewed
    cite: "Samson M, Libert F, Doranz BJ, et al. Resistance to HIV-1 infection in caucasian individuals bearing mutant alleles of the CCR-5 chemokine receptor gene. Nature. 1996;382(6593):722-725."
    doi: "10.1038/382722a0"
    pmid: "8751444"
    url: "https://doi.org/10.1038/382722a0"
    accessed: "2026-06-08"
cross_links:
  - target: 01-human/07-system/hiv-aids
    relation: connects-to
    note: "CCR5 is the primary co-receptor for R5-tropic HIV-1 (CCR5-tropic virus predominates in sexual transmission); CCR5-Δ32 homozygosity confers complete resistance to R5-tropic HIV-1; maraviroc blocks HIV-1 gp120 binding to CCR5 → FDA-approved first-line agent (2007)."
  - target: 01-human/07-system/immune-system
    relation: expressed-by
    note: "CCR5 is expressed on CD4+ T cells, macrophages, and dendritic cells; CCL3/CCL4/CCL5 ligands recruit CCR5+ cells to sites of infection; CCR5+ macrophages are the main reservoir of HIV-1 in tissues; CCR5 expression on Th1 cells directs trafficking to inflamed tissues."
  - target: 01-human/07-system/multiple-sclerosis
    relation: connects-to
    note: "CCR5+ Th1 cells are recruited to the CNS in MS lesions; CCR5-Δ32 carriers have reduced MS severity in some cohorts; CCR5 antagonism has been proposed as adjunct therapy in neuroinflammation but remains experimental."
  - target: 01-human/07-system/rheumatoid-arthritis
    relation: connects-to
    note: "CCR5+ macrophages and T cells are abundant in RA synovium; CCL3/CCL4/CCL5 (CCR5 ligands) are elevated in RA synovial fluid; CCR5 antagonism with maraviroc has been explored in RA in small trials; CCR5 deletion does not worsen but slightly modifies RA susceptibility."
---

# CCR5

## Overview

CCR5 (CC chemokine receptor 5, gene *CCR5*, chromosome 3p21.31) is a **seven-transmembrane (7-TM) G protein-coupled receptor (GPCR)** that serves as a chemokine receptor for the CC chemokines CCL3 (MIP-1α), CCL4 (MIP-1β), and CCL5 (RANTES), and — critically — as the **principal co-receptor required for R5-tropic HIV-1 entry** into CD4⁺ T cells and macrophages [^liu-1996-ccr5-delta32].

The landmark discovery in 1996 that individuals homozygous for the **CCR5-Δ32 deletion** (a 32-bp frameshift mutation causing a truncated, non-cell-surface-expressed receptor) are essentially completely resistant to sexual transmission of HIV-1 [^samson-1996-ccr5-coreceptor] established CCR5 as both a biological gateway and a therapeutic target. This made CCR5 one of the most studied human genetic loci in infectious disease — a natural experiment in protective immunity that has guided drug development, vaccine strategy, and (controversially) gene-editing attempts.

**Clinical impact:**
- **Maraviroc** (Pfizer, FDA approved 2007): The only approved CCR5 antagonist antiretroviral; first-in-class entry inhibitor; restricts R5-tropic HIV-1 from binding; requires prior tropism testing (Trofile/next-generation sequencing assay) to exclude CXCR4-using (X4-tropic) virus
- **CCR5-Δ32 frequency:** ~1% of Northern Europeans are homozygous (near-complete HIV resistance); ~10% heterozygous (partial reduced acquisition and slower progression)
- **Berlin/London/City of Hope patients:** Allogeneic stem cell transplantation from CCR5-Δ32 homozygous donors → functional HIV cure in a small number of cases

## Structure

### Protein and Receptor Topology

CCR5 is a canonical **class A (rhodopsin-like) GPCR:**
- **Structure:** 352 amino acids; 7 transmembrane α-helices (TM1–TM7); extracellular N-terminus (27 aa) + 3 extracellular loops (ECL1–3); intracellular C-terminus + 3 intracellular loops coupled to Gαi
- **Disulfide bond:** Cys101 (ECL1) – Cys178 (ECL2) — critical for receptor folding and ligand binding
- **N-terminus modifications:** Sulfation of Tyr10, Tyr14 on the N-terminus required for high-affinity CCL5 binding; these sulfotyrosines also contact HIV-1 gp120 V3 loop
- **Palmitoylation:** Cys321 and Cys323 in the C-terminus — anchors helix 8 to the membrane

### CCR5-Δ32 Mutation

The **Δ32 allele** (rs333; chr3:46,414,943–46,414,974) is a 32-bp deletion in the coding region:
- Frameshift at position 185 → premature stop codon → truncated 215-aa protein lacking TM helices 5–7 and C-terminus
- The truncated protein is retained in the endoplasmic reticulum → not expressed on the cell surface
- **Origin:** Estimated to have arisen in Northern Europe ~700–2,000 years ago; highest frequency in Scandinavia (~15% allele frequency); may have been selected by protection against a prior epidemic (bubonic plague, smallpox — still debated)
- **Effect:**
  - Homozygous (Δ32/Δ32): ~1% of Northern Europeans; near-complete resistance to R5-tropic HIV-1 acquisition; apparently healthy (mild increase in West Nile virus susceptibility described)
  - Heterozygous (Δ32/WT): ~1.5× reduced HIV-1 acquisition risk; ~2 year slower progression to AIDS

### HIV-1 Entry Mechanism

HIV-1 entry requires sequential engagement of two cell-surface molecules:
1. **gp120 (surface envelope glycoprotein)** binds **CD4** (primary receptor; found on Th1/Th2/Treg CD4⁺ T cells, macrophages, DCs) → conformational change in gp120 exposes the V3 loop (co-receptor binding domain)
2. V3 loop + gp120 C1-C4 domains bind **CCR5** (R5-tropic) or **CXCR4** (X4-tropic) → gp41 heptad repeats fold → six-helix bundle fusion intermediate → viral membrane fusion → capsid entry

**Tropism:**
- **R5-tropic (CCR5-using):** Predominant in early/acute HIV-1 infection; transmitted sexually; infects macrophages and T cells
- **X4-tropic (CXCR4-using):** Emerges in ~50% of AIDS patients; higher pathogenicity; correlates with accelerated CD4 decline
- **Dual-tropic (R5X4):** Can use both co-receptors; maraviroc is ineffective against X4 or dual-tropic virus

## Function

### Physiological Chemokine Signalling

CCR5's natural role is as a **chemoattractant receptor** guiding inflammatory cell migration:
- **CCL3 (MIP-1α) + CCL4 (MIP-1β):** Produced by macrophages, NK cells, and T cells; recruit CCR5⁺ cells to infection sites via Gi-protein → ↓cAMP → MAPK → cell migration
- **CCL5 (RANTES):** Produced by platelets, T cells, and endothelium; potent CCR5 agonist; involved in memory CD4⁺ T cell trafficking; CCL5/CCR5 axis governs Th1 cell homing to inflamed tissues (rheumatoid synovium, MS lesions, TB granuloma)

**CCR5 expression pattern:**
- CD4⁺ T cells (especially Th1 and Treg subsets)
- CD8⁺ T cells (partial)
- Monocytes and macrophages (major tissue HIV-1 reservoir)
- Microglia (brain)
- Dendritic cells
- NK cells
- NOT efficiently expressed on naïve T cells or B cells

### CCR5 as HIV-1 Tissue Reservoir

Tissue macrophages expressing CCR5 are long-lived HIV-1 reservoirs that:
- Survive ART (unlike productively infected CD4⁺ T cells)
- Persist in brain (microglia → HIV-associated neurocognitive disorder, HAND)
- Reside in gut-associated lymphoid tissue (GALT) — the predominant site of CD4 depletion in acute HIV-1 infection
- Produce low-level HIV-1 during ART-suppressed infection — contribute to viral rebound on ART interruption

### CCR5 Internalization and HIV Immune Evasion

CCL5 (RANTES) and other CCR5 agonists competitively protect against HIV-1 infection by:
1. Receptor internalization (CCR5 endocytosis → unavailable for gp120 binding)
2. Steric competition with V3 loop binding

This is the mechanism by which heterozygous CCR5-Δ32 individuals partially suppress HIV-1 (higher CCL5 on the WT allele's receptor drives more internalization of the remaining CCR5).

## Mechanism

### Maraviroc Mechanism and Pharmacology

Maraviroc (MVC; Pfizer Celsentri/Selzentry; FDA approved 2007):
- **Class:** CCR5 allosteric antagonist (not a CCR5 agonist or competitive inhibitor; does not block chemokine binding)
- **Binding site:** Transmembrane binding pocket formed by TM helices 1–3 and 6–7 → stabilises CCR5 in a conformation incompatible with gp120 V3 loop docking; distinct from CCL3/CCL4/CCL5 binding site
- **Selectivity requirement:** **Tropism testing is mandatory before prescribing maraviroc** — X4-tropic HIV-1 is completely insensitive; prescribing maraviroc for X4-tropic infection leads to treatment failure
- **Pharmacokinetics:** Oral bioavailability 23–33%; CYP3A4 substrate; dose adjustment with CYP3A inhibitors (ritonavir/cobicistat boost: reduce to 150 mg BID; efavirenz: increase to 600 mg BID)
- **Clinical use:** MERIT trial (2008): maraviroc BID non-inferior to efavirenz as initial therapy in R5-tropic infection; used in treatment-experienced patients with CCR5-tropic virus; also explored in prevention (topical gel) and as adjunct in HSCT conditioning for "functional cure" strategies

### Gene-Editing Approaches

The CCR5-Δ32 natural experiment inspired gene-editing strategies to confer HIV-1 resistance:
- **He Jiankui controversy (2018):** CRISPR-Cas9 editing of CCR5 in human embryos (CCR5 disruption) → birth of genetically modified twins ("Lulu and Nana"); widely condemned internationally; edit incomplete (mosaicism); He sentenced to prison
- **Zinc finger nuclease (ZFN) CCR5 editing** of autologous CD4⁺ T cells: Phase I trials (SB-728, Sangamo) showed safety and transient CD4 increase; not approved
- **Allogeneic HSCT from CCR5-Δ32 donors:** Berlin (2009), London (2019), Düsseldorf (2023), City of Hope (2023) patients achieved durable HIV remission after HSCT for haematological malignancy

### CXCR4 as Alternative HIV-1 Co-receptor

CXCR4 (CXC chemokine receptor 4; CXCL12/SDF-1 receptor):
- X4-tropic virus emerges as CD4 count falls → syncytia-forming, highly pathogenic in AIDS
- No approved CXCR4 antagonist for HIV (plerixafor/AMD3100 is an approved CXCR4 antagonist for HSCT mobilisation but not for HIV)
- CXCR4 tropism correlates with faster progression to AIDS; ~50% of AIDS-stage patients harbour dual-tropic or X4-tropic virus

## Connections

- `connects-to` → **[HIV/AIDS](../../07-system/hiv-aids/README.md)** — CCR5 is the principal entry co-receptor for R5-tropic HIV-1 (predominant in sexual transmission); CCR5-Δ32 homozygosity confers near-complete HIV-1 resistance; maraviroc allosterically blocks gp120/CCR5 interaction; HSCT from Δ32 donors has achieved functional cure in rare cases.
- `expressed-by` → **[Immune System](../../07-system/immune-system/README.md)** — CCR5 is expressed on CD4⁺ T cells (Th1, Treg), macrophages, and DCs; CCL3/CCL4/CCL5 recruit CCR5⁺ cells to inflammatory sites; tissue macrophages expressing CCR5 serve as the long-lived HIV-1 reservoir in brain, gut, and lymph nodes.
- `connects-to` → **[Multiple Sclerosis](../../07-system/multiple-sclerosis/README.md)** — CCR5⁺ Th1 cells are recruited to CNS white matter lesions in MS; CCR5-Δ32 carriers have modestly reduced MS severity; CCR5 antagonism with maraviroc has been explored in neuroinflammation models but lacks strong clinical evidence.
- `connects-to` → **[Rheumatoid Arthritis](../../07-system/rheumatoid-arthritis/README.md)** — CCR5⁺ macrophages and T cells predominate in RA synovium; CCL3/CCL4/CCL5 are elevated in RA synovial fluid; maraviroc has been explored in small RA trials with modest benefit; CCR5-Δ32 does not dramatically alter RA risk but may modulate disease course.

## Pathology

| Condition | Mechanism | Key Features |
|:---|:---|:---|
| **HIV-1 susceptibility** | CCR5 (WT) + CD4 → gp120-V3 binding → membrane fusion → viral entry | R5-tropic HIV-1 dominates early infection; WT CCR5 is required for R5 entry; maraviroc blocks |
| **CCR5-Δ32 protection** | Truncated protein not expressed on cell surface → R5-tropic HIV-1 cannot enter CCR5-null cells | Homozygous Δ32: >90% protection from sexual acquisition; heterozygous: ~1.5× reduced risk |
| **West Nile virus susceptibility** | CCR5 may be required for efficient WNV clearance; Δ32/Δ32 individuals → increased WNV severity | Rare genetic trade-off; CCR5 protective for WNV but expendable for general immunity |
| **CCR5 in neuroinflammation** | Microglial CCR5 participates in synaptic pruning and neuroinflammatory recruitment; CCR5 inhibition explored in cognitive impairment (TBI, Alzheimer's models) | CCR5 antagonism improved memory in TBI mouse models; Phase II trials ongoing |
| **Graft-vs-host disease** | CCR5⁺ Th1 cells mediate GvHD; CCR5 blockade has been explored as prophylaxis | Maraviroc in GvHD prophylaxis: GVHD incidence reduced in some trials |

## See Also

- [^liu-1996-ccr5-delta32] Liu R et al. Homozygous defect in HIV-1 coreceptor accounts for resistance of some multiply-exposed individuals to HIV-1 infection. *Cell.* 1996;86(3):367-377. [doi:10.1016/S0092-8674(00)80110-5](https://doi.org/10.1016/S0092-8674(00)80110-5) · [PubMed 8756719](https://pubmed.ncbi.nlm.nih.gov/8756719/)
- [^samson-1996-ccr5-coreceptor] Samson M et al. Resistance to HIV-1 infection bearing mutant alleles of the CCR-5 chemokine receptor gene. *Nature.* 1996;382(6593):722-725. [doi:10.1038/382722a0](https://doi.org/10.1038/382722a0) · [PubMed 8751444](https://pubmed.ncbi.nlm.nih.gov/8751444/)
- Related entries: [hiv-aids](../../07-system/hiv-aids/README.md), [cxcl12](../cxcl12/README.md), [immune-system](../../07-system/immune-system/README.md)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
