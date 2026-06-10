---
schema: human-scale-entry/v1
id: secretory-iga
name: Secretory IgA
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-06
summary: "Dimeric IgA + J chain + secretory component (SC); dominant mucosal antibody in gut, saliva, colostrum. Transcytosed via pIgR. SC confers protease resistance. Functions: immune exclusion, viral neutralization, pathogen agglutination."
aliases: ["SIgA", "secretory IgA", "sIgA", "dimeric IgA", "mucosal IgA"]
sources:
  - id: mestecky-2015-mucosal-iga
    type: peer-reviewed
    cite: "Mestecky J, Roque Velasco LR, Moro I. Mucosal immunoglobulins. Immunol Rev. 2015;206(1):8-58."
    doi: "10.1111/j.0105-2896.2005.00280.x"
    pmid: "15941106"
    url: "https://doi.org/10.1111/j.0105-2896.2005.00280.x"
  - id: fagarasan-honjo-2003-iga
    type: peer-reviewed
    cite: "Fagarasan S, Honjo T. Intestinal IgA synthesis: regulation of front-line body defences. Nat Rev Immunol. 2003;3(1):63-72."
    doi: "10.1038/nri982"
    pmid: "12511876"
    url: "https://doi.org/10.1038/nri982"
cross_links:
  - target: 01-human/04-cellular/plasma-cell
    relation: expressed-by
    note: "Secretory IgA is produced by IgA-committed plasma cells residing in the lamina propria of mucosal tissues, derived from B cells activated in MALT/Peyer's patches."
  - target: 01-human/03-molecular/immunoglobulin-g
    relation: connects-to
    note: "Secretory IgA (mucosal) and IgG (systemic) are the two dominant effector antibody isotypes; IgA dominates mucosal surfaces while IgG dominates the blood and tissues."
  - target: 01-human/07-system/gut-microbiome
    relation: connects-to
    note: "SIgA shapes host-microbiome homeostasis: coats commensal bacteria to prevent translocation; IgA-seq identifies pathobiont-specific SIgA coating; SIgA deficiency → bacterial translocation and dysbiosis; Akkermansia and Bifidobacterium are high-SIgA-coating commensals."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "SIgA is the effector arm of mucosal immunity: pIgR transcytoses dimeric IgA across epithelium; 3-5 g/day secreted into gut lumen; immune exclusion is the primary mucosal defense before systemic IgG; selective IgA deficiency → recurrent respiratory and GI infections."
  - target: 01-human/07-system/iga-nephropathy
    relation: connects-to
    note: "Aberrant O-glycosylation of IgA1 hinge region → galactose-deficient IgA1 (Gd-IgA1) → anti-Gd-IgA1 IgG autoantibodies → immune complexes → mesangial deposition → complement activation → IgAN; Gd-IgA1 from mucosal plasma cells is the primary disease-causing immunoglobulin in IgAN."
  - target: 01-human/05-tissue/germinal-center
    relation: connects-to
    note: "IgA class switch recombination occurs in GC reactions within GALT (Peyer's patches, mesenteric lymph nodes); Tfh-derived TGF-β + IL-10 → IgA CSR; GC-derived lamina propria plasma cells secrete dimeric IgA transcytosed by pIgR into the gut lumen."
---

# Secretory IgA

## Overview

Secretory IgA (SIgA) is the **dominant antibody isotype at mucosal surfaces** and the most abundantly produced immunoglobulin in the human body — approximately 3–5 g/day secreted onto mucosal surfaces, exceeding the total daily production of all other immunoglobulin classes combined. It is the primary immune effector of the gut lumen, respiratory tract, saliva, tears, breast milk, and colostrum [^fagarasan-honjo-2003-iga].

Unlike serum IgG — which operates primarily in blood and tissues where proteases are scarce — SIgA is engineered for survival in the protease-rich, acidic, and microbiologically dense environment of mucosal surfaces. Its unique structural feature, the **secretory component (SC)**, derived from the polymeric Ig receptor (pIgR), confers exceptional resistance to luminal proteolysis.

The core function of SIgA is **immune exclusion** — preventing pathogens from adhering to and penetrating mucosal epithelium — without triggering the inflammatory damage that would accompany complement activation or opsonin-dependent killing. This "non-inflammatory" mode of mucosal defense is critical for maintaining barrier homeostasis while excluding billions of microorganisms daily.

## Structure

### Molecular Architecture

Secretory IgA is assembled from four distinct components:

| Component | Origin | Mass | Function |
|:---|:---|:---|:---|
| **2× IgA monomers** | Plasma cells (lamina propria) | 160 kDa each | Antigen-binding arms (Fab) + Fc effector region |
| **J chain** (joining chain) | Plasma cells | 15 kDa | Covalently (disulfide) links the two IgA monomers at Fc; essential for pIgR recognition |
| **Secretory component (SC)** | Epithelial cells (cleaved pIgR ectodomain) | 70 kDa | Non-covalently + covalently wrapped around the Fc and J-chain region; protease resistance; glycan shield |

The two IgA monomers are joined **tail-to-tail** via J chain disulfide bonds at their Cα3 domains, creating a dimeric structure with four Fab antigen-binding arms (enabling multivalent antigen agglutination).

### IgA Subclasses

In humans, two IgA subclasses exist:
- **IgA1** (~90% of serum IgA): extended hinge region (13 amino acids); susceptible to IgA1 proteases produced by Streptococcus pneumoniae, H. influenzae, Neisseria; dominant in upper respiratory and genitourinary mucosae
- **IgA2** (~10% of serum IgA, higher proportion in gut): shorter hinge; protease-resistant; dominant in the colon

### Secretory Component (SC)

SC is the cleaved ectodomain of the **polymeric Ig receptor (pIgR)**, retained on SIgA after transcytosis. SC:
- Contains 5 Ig-like domains, extensively N-glycosylated
- Wraps around and stabilizes the J-chain junction
- Carbohydrate residues provide a glycan shield protecting Fc from proteases
- SC domain 1 directly binds mucins (MUC2, MUC5B) in the mucus layer, anchoring SIgA in the protective mucus gel

## Function

### Immune Exclusion

The primary function of SIgA is **immune exclusion** — physically blocking pathogen attachment to mucosal epithelium:

- **Agglutination**: Multivalent SIgA crosslinks bacterial and viral surface antigens, forming immune complexes that are too large to penetrate the mucus layer and are cleared by peristalsis/mucociliary transport
- **Steric blocking**: SIgA bound to pili, fimbriae, adhesins, or viral attachment proteins prevents ligand-receptor engagement with epithelial receptors
- **Mucosal entrapment**: SIgA-antigen complexes bind mucin glycans via SC and are immobilized in the mucus gel, promoting mechanical clearance

### Viral Neutralization — Including Intracellular

A unique property of IgA: **intracellular neutralization during transcytosis**. pIgR-mediated transport of IgA through epithelial cells occurs in endosomal vesicles. If an intracellular pathogen is present within the epithelial cell (e.g., during early viral infection), IgA can neutralize it en route, without triggering apoptosis or inflammation. This mechanism provides a "stealth" first line of defense against epithelial viral invasion.

### Anti-Inflammatory Immune Defense

SIgA operates largely without triggering the complement cascade or recruiting neutrophils:
- IgA Fc binds **FcαRI (CD89)** on macrophages, neutrophils, and eosinophils — activating phagocytosis without strong pro-inflammatory cytokine production
- Absent complement activation (unlike IgG/IgM) preserves epithelial integrity
- Critical for maintaining tolerance to commensal microbiota: SIgA opsonizes commensals, modulating their access to the epithelial surface without elimination

### Neonatal Protection (Colostrum)

Colostrum contains extraordinarily high SIgA concentrations (~12 g/L, vs. 2 g/L in mature milk). Neonatal gut lacks its own SIgA for the first weeks of life; maternal SIgA from breastfeeding provides passive mucosal protection against enteric pathogens. This is the evolutionary rationale for the exceptionally high colostral SIgA concentration.

## Mechanism

### pIgR-Mediated Transcytosis

Dimeric IgA (J chain-linked, produced by lamina propria plasma cells) reaches the basolateral surface of intestinal/respiratory epithelial cells and is transported to the luminal surface via a receptor-mediated transcytosis pathway:

1. **Basolateral binding** — dimeric IgA binds the **polymeric Ig receptor (pIgR)** on the basolateral epithelial surface; J chain is essential for high-affinity pIgR recognition
2. **Endocytosis** — pIgR-IgA complex is internalized via clathrin-coated pits into early endosomes
3. **Transcytosis** — vesicles are transported across the cell interior toward the apical surface
4. **Proteolytic cleavage** — pIgR ectodomain (SC) is cleaved from its transmembrane anchor by membrane proteases at the apical surface
5. **Secretion** — SC remains covalently associated with IgA Fc (via disulfide bonds formed during transcytosis); the SC-IgA complex (=SIgA) is released into the luminal secretion

## Connections

- `expressed-by` → **[Plasma Cell](../../04-cellular/plasma-cell/README.md)** — IgA-committed lamina propria plasma cells derived from MALT/Peyer's patch germinal centers are the sole source of dimeric IgA
- `connects-to` → **[Immunoglobulin G](../immunoglobulin-g/README.md)** — SIgA (mucosal) and IgG (systemic) are the two dominant effector antibody isotypes serving complementary anatomical compartments
- `connects-to` → **[Gut Microbiome](../../07-system/gut-microbiome/README.md)** — SIgA shapes host-microbiome homeostasis: coats commensal bacteria to prevent translocation; IgA-seq identifies pathobiont-specific SIgA coating; SIgA deficiency → bacterial translocation and dysbiosis; Akkermansia and Bifidobacterium are high-SIgA-coating commensals.
- `connects-to` → **[Immune System](../../07-system/immune-system/README.md)** — SIgA is the effector arm of mucosal immunity: pIgR transcytoses dimeric IgA across epithelium; 3-5 g/day secreted into gut lumen; immune exclusion is the primary mucosal defense before systemic IgG; selective IgA deficiency → recurrent respiratory and GI infections.
- `connects-to` → **[IgA Nephropathy](../../07-system/iga-nephropathy/README.md)** — Aberrant O-glycosylation of IgA1 hinge region → galactose-deficient IgA1 (Gd-IgA1) → anti-Gd-IgA1 IgG autoantibodies → immune complexes → mesangial deposition → complement activation → IgAN; Gd-IgA1 from mucosal plasma cells is the primary disease-causing immunoglobulin in IgAN.
- `connects-to` → **[OPV (Oral Polio Vaccine)](../../../../04-vaccine/05-live-attenuated/oral-polio-vaccine/README.md)** — OPV gut replication uniquely drives intestinal sIgA (unlike injected IPV); sIgA blocks poliovirus at the gut portal and prevents fecal-oral transmission — the eradication-critical immune correlate that enabled wild poliovirus elimination.
- `connects-to` → **[Germinal Center](../../05-tissue/germinal-center/README.md)** — IgA CSR occurs in GC reactions within GALT (Peyer's patches, mesenteric lymph nodes); Tfh-derived TGF-β + IL-10 → IgA class switching; GC-derived lamina propria plasma cells secrete dimeric IgA transcytosed by pIgR into the gut lumen.

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^mestecky-2015-mucosal-iga]: Mestecky J, Roque Velasco LR, Moro I. Mucosal immunoglobulins. *Immunol Rev.* 2015;206(1):8-58. [doi:10.1111/j.0105-2896.2005.00280.x](https://doi.org/10.1111/j.0105-2896.2005.00280.x) · [PubMed 15941106](https://pubmed.ncbi.nlm.nih.gov/15941106/)
[^fagarasan-honjo-2003-iga]: Fagarasan S, Honjo T. Intestinal IgA synthesis: regulation of front-line body defences. *Nat Rev Immunol.* 2003;3(1):63-72. [doi:10.1038/nri982](https://doi.org/10.1038/nri982) · [PubMed 12511876](https://pubmed.ncbi.nlm.nih.gov/12511876/)
