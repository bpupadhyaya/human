---
schema: human-scale-entry/v1
id: il-10
name: Interleukin-10
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-07
summary: "IL-10 is the master anti-inflammatory cytokine; IL10 gene chr1q32.1; homodimer; IL-10Rα/IL-10Rβ → JAK1/TYK2 → STAT3 → suppresses NF-κB in macrophages, reducing TNF-α, IL-1β, IL-6, IL-12. Treg-derived IL-10 protects against GvHD; IL-10R mutations cause very-early-onset IBD."
aliases: ["IL10", "cytokine synthesis inhibitory factor", "CSIF", "B-cell-derived T-cell growth factor", "TGIF"]
sources:
  - id: moore-1993-il10-review
    type: peer-reviewed
    cite: "Moore KW, de Waal Malefyt R, Coffman RL, O'Garra A. Interleukin-10 and the interleukin-10 receptor. Annu Rev Immunol. 2001;19:683-765."
    doi: "10.1146/annurev.immunol.19.1.683"
    pmid: "11244051"
    url: "https://doi.org/10.1146/annurev.immunol.19.1.683"
  - id: ouyang-2011-il10-review
    type: peer-reviewed
    cite: "Ouyang W, Rutz S, Crellin NK, Valdez PA, Hymowitz SG. Regulation and functions of the IL-10 family of cytokines in inflammation and disease. Annu Rev Immunol. 2011;29:71-109."
    doi: "10.1146/annurev-immunol-031210-101312"
    pmid: "21166540"
    url: "https://doi.org/10.1146/annurev-immunol-031210-101312"
  - id: kotlarz-2012-il10r-ibd
    type: peer-reviewed
    cite: "Kotlarz D, Beier R, Murugan D, et al. Loss of interleukin-10 signaling and infantile inflammatory bowel disease: implications for diagnosis and therapy. Gastroenterology. 2012;143(2):347-355."
    doi: "10.1053/j.gastro.2012.04.045"
    pmid: "22549090"
    url: "https://doi.org/10.1053/j.gastro.2012.04.045"
cross_links:
  - target: 01-human/07-system/gvhd
    relation: connects-to
    note: "Treg-derived IL-10 is the dominant immunosuppressive brake on alloreactive donor T cells post-HSCT; low circulating IL-10 and IL-10R polymorphisms predict GvHD severity; IL-10 gene transfer and IL-10-secreting Treg infusions are investigational GvHD prevention strategies."
  - target: 01-human/07-system/atopic-dermatitis
    relation: connects-to
    note: "IL-10 from regulatory B cells and Th2 cells dampens AD inflammation; paradoxically, Th2-skewed IL-4/IL-13 environment suppresses macrophage IL-10 production; imbalance between IL-10 and type-2 cytokines determines AD chronicity; IL-10 serum levels inversely correlate with SCORAD."
  - target: 01-human/07-system/nash
    relation: connects-to
    note: "IL-10 from Kupffer cells and hepatic Tregs restrains NLRP3 inflammasome activation and stellate cell activation in NASH; IL-10 KO mice develop spontaneous steatohepatitis on high-fat diet; IL-10 deficiency correlates with fibrosis stage in human NASH biopsies."
  - target: 01-human/07-system/inflammatory-bowel-disease
    relation: connects-to
    note: "IL-10R mutations (IL10RA/IL10RB LOF) → VEO-IBD: infantile-onset perianal fistulizing Crohn's refractory to conventional therapy, curable by allo-HSCT; IL-10 KO mice develop spontaneous microbiota-driven colitis; IL-10 signaling is the molecular brake on gut inflammation."
  - target: 01-human/07-system/sepsis
    relation: connects-to
    note: "IL-10 mediates sepsis immunoparalysis: hyperinflammation → IL-10 surge → STAT3-driven macrophage suppression → impaired bacterial clearance → secondary nosocomial infections; plasma IL-10 >30 pg/mL on day 1 predicts mortality and secondary infection risk in septic patients."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "IL-10 is the master anti-inflammatory cytokine: IL-10Rα/β → JAK1/TYK2 → STAT3 → ↑IκBα → NF-κB suppression → ↓TNF-α, ↓IL-1β, ↓IL-6, ↓IL-12 in macrophages; Treg/Breg/M2-derived IL-10 resolves acute inflammation; IL-10 deficiency drives IBD, GvHD, and autoimmunity."
---

# Interleukin-10

## Overview

**Interleukin-10 (IL-10)** is the defining **master anti-inflammatory cytokine** of the immune system — a pleiotropic immunomodulatory molecule whose primary function is to terminate or constrain inflammatory responses initiated by innate and adaptive immune cells, preventing collateral tissue damage from prolonged immune activation [^moore-1993-il10-review].

Encoded by *IL10* on **chromosome 1q32.1**, IL-10 is produced by virtually every immune cell type — most prominently **Tregs, Th2 cells, M2 macrophages, regulatory B cells (Bregs), monocytes, mast cells, NK cells, and dendritic cells** — as well as epithelial cells under inflammatory conditions. Its expression marks the resolution phase of acute inflammation and the chronic tolerogenic milieu of immune privilege sites (gut, placenta, tumor microenvironment).

**Historical context:** Originally termed **cytokine synthesis inhibitory factor (CSIF)**, IL-10 was characterized in 1989 as a factor from murine Th2 clones that inhibited IFN-γ production by Th1 cells. The protein is conserved across vertebrates, and strikingly, the Epstein-Barr virus (EBV) encodes **BCRF1/vIL-10**, a near-perfect IL-10 viral homolog (78% amino acid identity) that the virus uses to suppress antiviral CTL responses — exploiting IL-10's immunosuppressive axis for viral immune evasion.

**Disease relevance:** IL-10 insufficiency drives inflammatory bowel disease (IBD), GvHD, psoriasis, and rheumatoid arthritis. IL-10 excess drives tumor immunosuppression, M2 polarization in cancer stroma, and susceptibility to intracellular infections (Mycobacterium tuberculosis, Leishmania). The IL-10 axis is a therapeutic target in both directions — recombinant IL-10 for Crohn's disease (abandoned due to paradoxical IFN-γ expansion) and IL-10 agonists for cancer immunotherapy (pegilodecakin/AM0010).

## Structure

**Gene and protein:**
- *IL10* gene: chromosome **1q32.1**; ~5 kb; 5 exons; contains NF-κB and AP-1 binding sites in promoter; single nucleotide polymorphisms at –1082, –819, –592 (ATA haplotype: low producer; GCC haplotype: high producer) associated with IBD and transplant rejection risk
- **Protein:** 178 aa pre-protein; 18 aa signal peptide → 160 aa mature monomer; molecular weight ~18.5 kDa monomer (~37 kDa non-covalent homodimer); forms antiparallel **homodimer** through domain swap — the two long helices (A and D) of each monomer swap, creating an interleaved structure that is critically required for receptor activation
- **Structural family:** Class 2 cytokine (structurally related to IFNs, IL-22, IL-26, IL-28/29); 6-helix bundle fold (αA-αF); two disulfide bonds (C12-C108, C62-C114 in mature monomer) required for stability

**Receptor complex:**
- **IL-10Rα (IL10RA; CD210a; chr11q23.3):** ~60 kDa; primary binding chain; Kd ~1-2 nM; constitutively expressed on hematopoietic cells (macrophages, monocytes, NK cells, B cells, T cells); low expression on non-hematopoietic cells; box 1/box 2 motifs associate with **JAK1**
- **IL-10Rβ (IL10RB; CDw210b; chr21q22.11):** ~50 kDa; shared signal-transducing subunit (also used by IL-22, IL-26, IL-28, IL-29); low-affinity binding (Kd >100 nM alone); associates with **TYK2**; chromosome 21 location explains connection to Down syndrome (trisomy 21) immune dysregulation
- **Tetramer complex:** 2× IL-10 homodimer + 2× IL-10Rα + 2× IL-10Rβ → 2:2:2 hexameric complex; IL-10 binds IL-10Rα through sites 1 and 3 (D-helix of each monomer) → IL-10Rβ recruited → JAK1/TYK2 transphosphorylation

**Signaling — canonical STAT3 pathway:**
- JAK1 (IL-10Rα) + TYK2 (IL-10Rβ) transphosphorylation → **STAT3** phosphorylation at Y705 (dominant) and S727
- pSTAT3 dimerizes → nuclear translocation → STAT3-responsive promoters: *SOCS3* (feedback inhibitor), *BCL-2*, *BCL-XL*, *MCL1*, anti-apoptotic genes
- **SOCS3 induction:** IL-10 induces SOCS3 within 30-60 min → SOCS3 binds JAK2 activation loop → JAK2 inhibition; SOCS3 is the primary negative feedback brake on IL-10 signaling duration
- **NF-κB suppression (central anti-inflammatory mechanism):**
  - IL-10/STAT3 → ↑IκBα (NF-κB inhibitor) expression → sequestration of p65/p50 NF-κB in cytoplasm
  - STAT3 directly competes with NF-κB p65 for CBP/p300 transcriptional coactivator binding at shared promoters (TNF-α, IL-1β, IL-6, IL-12p40, MIP-1α promoters)
  - Net effect: macrophages exposed to IL-10 fail to produce pro-inflammatory cytokines in response to LPS/TLR4 stimulation → LPS tolerance without true anergy

## Function

IL-10 acts as a rheostat for immune intensity: it is produced at the peak of an inflammatory response and suppresses further pro-inflammatory signaling, allowing tissue repair to proceed. In macrophages, IL-10/STAT3 directly represses *Tnf*, *Il1b*, *Il6*, *Il12b*, and *Nos2* transcription while upregulating *Il1rn* (IL-1Ra) and *Cd163* — converting activated M1 macrophages toward an M2/resolving phenotype. In T cells, IL-10 terminates effector programs without inducing apoptosis, establishing antigen-specific tolerance. In the gut, IL-10 maintains tolerance to commensal microbiota; loss of IL-10 signaling allows commensal-driven colitis (IL-10 KO mouse model; IL-10R mutations in VEO-IBD).

## Mechanism

**Anti-inflammatory effects by cell type:**

**Macrophages (primary target):**
- IL-10 → STAT3 → ↓IL-1β, ↓TNF-α, ↓IL-6, ↓IL-12, ↓IL-18, ↓CXCL8 production at transcriptional level
- ↓MHC class II (HLA-DR) and ↓CD80/CD86 (costimulatory molecules) surface expression → reduced T cell activation capacity
- ↑CD16 (FcγRIII) and ↑CD163 (hemoglobin-haptoglobin scavenger receptor) → M2 polarization phenotype
- ↑arginase-1 → competes with iNOS for arginine → ↓nitric oxide production
- ↑mannose receptor (CD206) and ↑IL-1Ra (IL-1 receptor antagonist) → anti-inflammatory effector profile

**T cells:**
- CD4+ Th1 cells: IL-10 → ↓IFN-γ, ↓IL-2, ↓TNF production; ↓CXCR3 expression → reduced trafficking to inflammation sites
- CD8+ CTL: ↓perforin/granzyme → reduced cytotoxicity (relevant in tumor immunosuppression)
- Treg cells: IL-10 is the principal effector molecule of Foxp3+ Tregs (alongside TGF-β) → cell-contact-independent suppression; IL-10-deficient Treg mice develop colitis despite intact Foxp3 expression

**Dendritic cells:**
- IL-10 → tolerogenic DC phenotype: ↓IL-12p70, ↓CD80/86, ↑PD-L1, ↑ILT4 → induces Treg differentiation rather than Th1/Th17 polarization
- Plasmacytoid DCs: IL-10 → ↓IFN-α production → dampens antiviral innate response (exploited by EBV/vIL-10)

**B cells:**
- IL-10 is a potent B cell growth and differentiation factor → plasma cell differentiation and IgG/IgA class switching
- Regulatory B cells (Bregs; CD19+CD24hiCD38hi) are defined by IL-10 production → suppress Th1/Th17; loss of Breg IL-10 → systemic autoimmunity

**IL-10 in gut homeostasis and IBD:**
- The intestinal mucosa maintains IL-10 at concentrations ~10-100× higher than systemic circulation
- **IL-10 knockout mice** develop severe spontaneous colitis (resembling Crohn's disease) by 3-4 months; germ-free IL-10 KO mice do not develop colitis → microbiota-driven, IL-10-gated inflammation
- **IL-10R mutations → very-early-onset IBD (VEO-IBD):** Autosomal recessive loss-of-function mutations in *IL10RA* or *IL10RB* → complete loss of IL-10 signaling → infantile-onset perianal fistulizing Crohn's disease refractory to all conventional therapies [^kotlarz-2012-il10r-ibd]; allogeneic HSCT is curative (provides donor-derived cells with functional IL-10Rα)

**IL-10 in cancer:**
- IL-10 has dual cancer roles — paradoxical:
  - **Tumor-promoting:** IL-10 in TME → M2 tumor-associated macrophages (TAM) → suppressed CD8+ CTL → tumor immune escape; TIL exhaustion (PD-1+TIM-3+ phenotype) accompanied by IL-10 secretion
  - **Anti-tumor:** IL-10 can activate NK cells and CD8+ CTL via STAT3-dependent cytotoxic gene programs when delivered pharmacologically at supraphysiological concentrations
- **Pegilodecakin (AM0010):** PEGylated recombinant human IL-10; Phase 1/2 trials in metastatic pancreatic cancer + renal cell carcinoma; paradoxical expansion of CD8+ effector T cells and IFN-γ at pharmacological doses (distinct from endogenous immunosuppressive IL-10); Phase 2 in combination with pembrolizumab; development program ongoing

**IL-10 in GvHD:**
- Allo-HSCT → alloreactive donor T cells recognize host MHC → cytokine storm (TNF-α, IL-6, IFN-γ)
- IL-10-producing Tregs from donor graft restrain this response; low ratio of Treg:Tconv in graft → higher GvHD risk
- **IL-10 serum levels** measured on day 7-14 post-HSCT predict GvHD: patients who develop grade II-IV acute GvHD show significantly lower IL-10 at day +7
- **IL-10 gene polymorphisms** (ATA/ATA low-producer haplotype) in donor or recipient → higher GvHD incidence and severity
- **IL-10-secreting Treg therapy:** Adoptive transfer of ex vivo expanded donor Tregs (which produce IL-10/TGF-β) → reduced grade III/IV GvHD in Phase 1/2 trials (ONE trial, ORCA-T)

## Connections

- `connects-to` → **[GvHD](../../07-system/gvhd/README.md)** — Treg-derived IL-10 is the dominant immunosuppressive brake on alloreactive donor T cells post-HSCT; low circulating IL-10 and IL-10R polymorphisms predict GvHD severity; IL-10 gene transfer and IL-10-secreting Treg infusions are investigational GvHD prevention strategies.
- `connects-to` → **[Atopic Dermatitis](../../07-system/atopic-dermatitis/README.md)** — IL-10 from regulatory B cells and Th2 cells dampens AD inflammation; paradoxically, Th2-skewed IL-4/IL-13 environment suppresses macrophage IL-10 production; imbalance between IL-10 and type-2 cytokines determines AD chronicity; IL-10 serum levels inversely correlate with SCORAD.
- `connects-to` → **[NASH](../../07-system/nash/README.md)** — IL-10 from Kupffer cells and hepatic Tregs restrains NLRP3 inflammasome activation and stellate cell activation in NASH; IL-10 KO mice develop spontaneous steatohepatitis on high-fat diet; IL-10 deficiency correlates with fibrosis stage in human NASH biopsies.
- `connects-to` → **[Inflammatory Bowel Disease](../../07-system/inflammatory-bowel-disease/README.md)** — IL-10R mutations (IL10RA/IL10RB LOF) → VEO-IBD: infantile-onset perianal fistulizing Crohn's refractory to conventional therapy, curable by allo-HSCT; IL-10 KO mice develop spontaneous microbiota-driven colitis; IL-10 signaling is the molecular brake on gut inflammation.
- `connects-to` → **[Sepsis](../../07-system/sepsis/README.md)** — IL-10 mediates sepsis immunoparalysis: hyperinflammation → IL-10 surge → STAT3-driven macrophage suppression → impaired bacterial clearance → secondary nosocomial infections; plasma IL-10 >30 pg/mL on day 1 predicts mortality and secondary infection risk in septic patients.
- `connects-to` → **[Immune System](../../07-system/immune-system/README.md)** — IL-10 is the master anti-inflammatory cytokine: IL-10Rα/β → JAK1/TYK2 → STAT3 → ↑IκBα → NF-κB suppression → ↓TNF-α, ↓IL-1β, ↓IL-6, ↓IL-12 in macrophages; Treg/Breg/M2-derived IL-10 resolves acute inflammation; IL-10 deficiency drives IBD, GvHD, and autoimmunity.

[^moore-1993-il10-review]: Moore KW, de Waal Malefyt R, Coffman RL, O'Garra A. Interleukin-10 and the interleukin-10 receptor. *Annu Rev Immunol.* 2001;19:683-765. [doi:10.1146/annurev.immunol.19.1.683](https://doi.org/10.1146/annurev.immunol.19.1.683) · [PubMed 11244051](https://pubmed.ncbi.nlm.nih.gov/11244051/)
[^ouyang-2011-il10-review]: Ouyang W, Rutz S, Crellin NK, Valdez PA, Hymowitz SG. Regulation and functions of the IL-10 family of cytokines in inflammation and disease. *Annu Rev Immunol.* 2011;29:71-109. [doi:10.1146/annurev-immunol-031210-101312](https://doi.org/10.1146/annurev-immunol-031210-101312) · [PubMed 21166540](https://pubmed.ncbi.nlm.nih.gov/21166540/)
[^kotlarz-2012-il10r-ibd]: Kotlarz D, Beier R, Murugan D, et al. Loss of interleukin-10 signaling and infantile inflammatory bowel disease: implications for diagnosis and therapy. *Gastroenterology.* 2012;143(2):347-355. [doi:10.1053/j.gastro.2012.04.045](https://doi.org/10.1053/j.gastro.2012.04.045) · [PubMed 22549090](https://pubmed.ncbi.nlm.nih.gov/22549090/)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
