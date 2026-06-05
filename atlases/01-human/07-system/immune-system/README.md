---
schema: human-scale-entry/v1
id: immune-system
name: Immune System
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-04
summary: "Two-layer defense: innate (fast, pattern recognition, complement, IFN) and adaptive (antigen-specific T/B lymphocytes, immunological memory). Peak adaptive response 7–14 days first exposure; memory recall 2–3 days. Organized around lymphoid organs."
aliases: ["immunity", "immune response", "lymphoid system", "humoral immunity", "cellular immunity"]
sources:
  - id: janeway-immunobiology-9e
    type: textbook
    cite: "Murphy K, Weaver C, Berg L. Janeway's Immunobiology. 9th ed. Garland Science; 2016."
    url: "https://www.garlandscience.com/product/isbn/9780815345053"
    accessed: "2026-06-04"
  - id: abbas-immunology-9e
    type: textbook
    cite: "Abbas AK, Lichtman AH, Pillai S. Cellular and Molecular Immunology. 9th ed. Elsevier; 2018."
    url: "https://www.elsevier.com/books/cellular-and-molecular-immunology/abbas/978-0-323-52323-3"
    accessed: "2026-06-04"
  - id: medzhitov-2007-innate
    type: peer-reviewed
    cite: "Medzhitov R. Recognition of microorganisms and activation of the immune response. Nature. 2007;449(7164):819-26."
    doi: "10.1038/nature06246"
    pmid: "17943118"
  - id: akbar-2016-immune-memory
    type: peer-reviewed
    cite: "Akbar AN, Gilroy DW. Aging immunity may exacerbate COVID-19. Science. 2020;369(6501):256-257."
    doi: "10.1126/science.abb0762"
    pmid: "32675364"
  - id: who-immunology-2012
    type: regulatory
    cite: "World Health Organization. Understanding the Immune System: How It Works. NIH Publication No. 03-5423. 2003."
    url: "https://www.niaid.nih.gov/sites/default/files/theimmunesystem.pdf"
    accessed: "2026-06-04"
  - id: iwasaki-medzhitov-2015
    type: peer-reviewed
    cite: "Iwasaki A, Medzhitov R. Control of adaptive immunity by the innate immune system. Nat Immunol. 2015;16(4):343-53."
    doi: "10.1038/ni.3123"
    pmid: "25789684"
cross_links:
  - target: 01-human/08-whole-body/human-body
    relation: part-of
    note: "The immune system is one of the major functional systems of the human body, spanning lymphoid organs, circulating cells, and soluble mediators throughout all tissues."
  - target: 01-human/04-cellular/dendritic-cell
    relation: contains
    note: "Dendritic cells are the professional antigen-presenting cells of the immune system, bridging innate detection and adaptive T cell priming."
  - target: 01-human/04-cellular/t-helper-cell
    relation: contains
    note: "CD4+ T helper cells are the master coordinators of adaptive immune responses, directing both cellular and humoral immunity."
  - target: 01-human/04-cellular/b-cell
    relation: contains
    note: "B lymphocytes are the antibody-producing arm of adaptive immunity, generating humoral protection via germinal center reactions."
  - target: 01-human/04-cellular/plasma-cell
    relation: contains
    note: "Plasma cells are the terminal antibody-secreting effectors of B cell differentiation; long-lived plasma cells in bone marrow maintain durable serum IgG titers."
  - target: 01-human/03-molecular/immunoglobulin-g
    relation: contains
    note: "IgG is the most abundant circulating antibody and the primary soluble effector molecule of humoral adaptive immunity."
  - target: 01-human/03-molecular/mhc-class-ii
    relation: contains
    note: "MHC class II molecules are expressed on professional APCs of the immune system and are the molecular platform for CD4+ T cell activation and adaptive immune priming."
  - target: 02-pathogen/01-viruses/sars-cov-2
    relation: damaged-by
    note: "SARS-CoV-2 evades and damages the immune system via multiple mechanisms: suppression of type I IFN production, dysregulation of innate sensing, lymphopenia (CD4+/CD8+ T cell depletion), and cytokine storm (IL-6, IL-1β, TNF) that causes immunopathology."
  - target: 02-pathogen/01-viruses/influenza-a
    relation: damaged-by
    note: "Influenza A NS1 protein blocks IFN-β induction; neuraminidase cleaves surface antibodies and sialic acids that aid innate immunity; annual antigenic drift requires continuous immune adaptation."
  - target: 02-pathogen/02-bacteria/mycobacterium-tuberculosis
    relation: damaged-by
    note: "M. tuberculosis blocks phagosome acidification and fusion with lysosomes (via ESAT-6, coronin-1A), evades macrophage killing, establishes latent intracellular infection, and can reactivate when cell-mediated immunity is suppressed."
  - target: 03-medicine/01-modern/04-cardio/aspirin
    relation: treated-by
    note: "Aspirin inhibits COX-1 and COX-2, reducing prostaglandin E2 (PGE2) production; PGE2 is an immunomodulatory lipid mediator that normally suppresses T cell activation and NK cell cytotoxicity, so aspirin has net immunostimulatory effects in some inflammatory contexts."
---

# Immune System

## Overview

The immune system is the body's multilayered defense against pathogens, malignant cells, and foreign substances — and simultaneously the regulatory network that maintains tolerance to self [^janeway-immunobiology-9e]. It is not a single organ but a distributed system spanning every tissue in the body: cells circulate in blood and lymph, patrol tissues as resident populations, and communicate through soluble mediators (cytokines, chemokines, antibodies, complement proteins).

Two functionally distinct but deeply interconnected arms cooperate [^iwasaki-medzhitov-2015]:

1. **Innate immunity** — rapid (minutes to hours), broad-specificity, non-adaptive detection of molecular patterns associated with pathogens (PAMPs — pathogen-associated molecular patterns) or tissue damage (DAMPs — damage-associated molecular patterns). Effectors: phagocytes (neutrophils, macrophages), NK cells, innate lymphoid cells, dendritic cells, complement, type I interferons.

2. **Adaptive immunity** — slow first response (7–14 days), exquisitely antigen-specific, capable of immunological memory. Effectors: T lymphocytes (CD4+ helper, CD8+ cytotoxic, regulatory), B lymphocytes, antibodies. On second encounter with the same antigen, memory recall response peaks in 2–3 days with higher magnitude and affinity.

This two-layer architecture is why vaccination works: a vaccine primes the adaptive immune system at low cost (no disease), establishing memory cells and long-lived plasma cells that enable rapid, protective responses on subsequent natural exposure.

The immune system surveils approximately **37 trillion cells** in the human body via constitutive MHC-I self-presentation — any cell that fails to display normal MHC-I with normal self-peptides is detected as abnormal by NK cells and cytotoxic T cells. This surveillance is the primary defense against intracellular pathogens and cancer.

## Structure

### Primary lymphoid organs

Primary lymphoid organs are the sites of immune cell development and education:

| Organ | Function |
|:---|:---|
| **Bone marrow** | Origin of all immune cells (hematopoietic stem cells); site of B cell development, maturation, and central tolerance; long-lived plasma cell niche |
| **Thymus** | Site of T cell development: TCR rearrangement, positive selection (MHC restriction), negative selection (central tolerance/clonal deletion), Treg generation |

### Secondary lymphoid organs

Secondary lymphoid organs are where adaptive immune responses are initiated — where circulating naïve lymphocytes encounter antigen presented by dendritic cells:

| Organ | Specialization |
|:---|:---|
| **Lymph nodes** | Filter lymph draining tissues; T cell zones (paracortex) + B cell follicles (cortex); site of DC–T cell priming and germinal center reactions |
| **Spleen** | Filters blood; marginal zone (innate, T-independent B responses) + white pulp (T and B cell zones, GC reactions); red pulp (erythrophagocytosis) |
| **MALT (mucosa-associated lymphoid tissue)** | Tonsils, Peyer's patches (gut), bronchus-associated lymphoid tissue (BALT); front-line mucosal immunity; IgA production |

### Circulating cells

| Cell type | Approximate blood count | Primary function |
|:---|:---|:---|
| Neutrophils | 1.8–7.7 × 10⁹/L | First phagocytic responders; bacteria/fungi; NET formation |
| Monocytes | 0.2–1.0 × 10⁹/L | Phagocytosis; cytokine production; DC precursors |
| NK cells | 0.07–0.5 × 10⁹/L | Kill MHC-I-low cells; produce IFN-γ |
| CD4+ T cells | 0.4–1.1 × 10⁹/L | Coordinate adaptive response |
| CD8+ T cells | 0.2–0.9 × 10⁹/L | Kill infected/malignant cells |
| B cells | 0.05–0.4 × 10⁹/L | Produce antibodies; APCs |
| Eosinophils | 0.02–0.5 × 10⁹/L | Anti-parasite; allergy |
| Basophils/mast cells | <0.1 × 10⁹/L blood | IgE-mediated degranulation; allergy |

### Soluble mediators

- **Complement system** — 30+ plasma proteins; three activation pathways (classical, lectin, alternative) converging on C3 cleavage → C3b opsonization + MAC lysis + C5a anaphylatoxin
- **Cytokines** — soluble signaling proteins: interleukins (IL-1 through IL-38+), interferons (type I: IFN-α/β; type II: IFN-γ; type III: IFN-λ), TNF, TGF-β, colony-stimulating factors
- **Chemokines** — ~50 small cytokines guiding cell migration via concentration gradients (CXCL8/IL-8 for neutrophils; CCL19/21 for DC/T cell homing; CXCL13 for B cell follicle formation)
- **Antibodies (immunoglobulins)** — IgM (first response, complement activation), IgG (most abundant, long half-life, placental transfer), IgA (mucosal secretory), IgE (allergy, anti-parasite), IgD (B cell surface co-receptor)

## Function

### Innate immune response (Phase 1: minutes–hours)

When a pathogen breaches barriers (skin, mucosa), innate immune cells respond within minutes [^medzhitov-2007-innate]:

1. **Pattern recognition** — tissue macrophages and DCs recognize PAMPs via TLRs (TLR4: LPS; TLR3: dsRNA; TLR9: CpG DNA), NLRs (NOD2: bacterial muramyl dipeptide; NLRP3 inflammasome), RIG-I/MDA5 (cytosolic RNA), cGAS/STING (cytosolic DNA)
2. **Immediate effector response** — vasodilation, increased permeability (histamine from mast cells, bradykinin from plasma contact system); neutrophil recruitment via CXCL8; phagocytosis; complement activation
3. **Type I IFN induction** — TLR7/9 in pDCs or RIG-I/STING in infected cells triggers IRF3/7 → massive IFN-α/β secretion → IFNAR signaling on all neighboring cells → antiviral state (ISGs: OAS, MX1, PKR, IFIT)
4. **Cytokine storm risk** — excessive innate activation (especially IL-6, IL-1β, TNF, IL-18) can cause systemic inflammatory response syndrome (SIRS); this is the basis of the cytokine storm in severe COVID-19 and influenza

### Adaptive immune response (Phase 2: days 3–14)

4. **DC maturation and migration** (Days 1–3) — PAMPs trigger DC maturation; mature DCs upregulate MHC-II, CD80/86, CCR7; migrate to draining lymph nodes
5. **T cell priming** (Days 3–5) — DC–T cell pMHC-II–TCR interaction in lymph node paracortex; naïve CD4+ T cell activation + CD8+ T cell priming; Signals 1+2+3 trigger clonal expansion
6. **B cell activation and germinal center** (Days 5–14) — antigen-specific B cells activated at follicle border by cognate antigen + Tfh help; germinal centers form; affinity maturation, class switching, plasmablast and memory B cell generation
7. **Effector deployment** — cytotoxic CD8+ T cells kill infected cells; IgM then IgG antibodies neutralize pathogen; opsonization, ADCC, complement enhance clearance

### Memory and recall

After primary response contraction, long-lived memory cells persist:
- **Memory CD4+ and CD8+ T cells** — distributed in lymphoid and non-lymphoid tissues (including tissue-resident memory T cells, T_RM); respond within hours
- **Memory B cells** — circulate; respond within 1–3 days on re-encounter
- **Long-lived plasma cells (LLPCs)** — in bone marrow; continuously secrete IgG for years, maintaining serum antibody titers that provide immediate neutralization on re-exposure

## Connections

- **Part of:** [human-body](../../08-whole-body/human-body/README.md)
- **Contains:** [dendritic-cell](../../04-cellular/dendritic-cell/README.md), [t-helper-cell](../../04-cellular/t-helper-cell/README.md), [b-cell](../../04-cellular/b-cell/README.md), [plasma-cell](../../04-cellular/plasma-cell/README.md), [immunoglobulin-g](../../03-molecular/immunoglobulin-g/README.md)
- **Damaged by:** [sars-cov-2](../../../../02-pathogen/01-viruses/sars-cov-2/README.md), [influenza-a](../../../../02-pathogen/01-viruses/influenza-a/README.md), [mycobacterium-tuberculosis](../../../../02-pathogen/02-bacteria/mycobacterium-tuberculosis/README.md)
- **Treated by:** [aspirin](../../../../03-medicine/01-modern/04-cardio/aspirin/README.md) (immunomodulatory via COX inhibition → reduced PGE2)

## Pathology

### Immunodeficiency

**Primary immunodeficiencies** are monogenic disorders of immune development or function:
- **Severe Combined Immunodeficiency (SCID)** — absence of both T and B cell function; ADA-SCID (adenosine deaminase deficiency), X-SCID (IL-2Rγ chain mutation), RAG1/2 mutations. Untreated, invariably fatal in infancy. Curable by hematopoietic stem cell transplantation or gene therapy (ADA-SCID is the first human gene therapy success, 1990).
- **X-linked agammaglobulinemia (XLA)** — BTK mutation; B cell development arrest at pro-B stage; absent serum immunoglobulins; treated with IV immunoglobulin (IVIG)
- **DiGeorge syndrome** — thymic aplasia (22q11.2 deletion); absent T cell development; severe susceptibility to viral and fungal infections

**Secondary immunodeficiencies** (acquired):
- **HIV-1/AIDS** — retrovirus selectively infecting and depleting CD4+ T cells (via CCR5/CXCR4 co-receptors); CD4+ count <200 cells/µL defines AIDS; opportunistic infections (PCP, CMV retinitis, cryptococcal meningitis, MAI) are the proximate causes of death. ART (antiretroviral therapy) can fully reconstitute CD4+ counts and prevent progression.
- **Iatrogenic** — immunosuppressive drugs (corticosteroids, cyclophosphamide, tacrolimus, biologics like rituximab, anti-TNF) used in autoimmunity, transplantation, and cancer cause secondary immunodeficiency

### Autoimmunity

When central and peripheral tolerance fail, self-reactive T and B cells escape deletion and attack host tissues:
- **Systemic lupus erythematosus (SLE)** — loss of tolerance to nuclear antigens (dsDNA, histones, Sm); anti-dsDNA antibodies form immune complexes; complement-mediated damage in kidneys (lupus nephritis), skin, joints, brain. HLA-DR2/DR3 strongly associated. Type I IFN signature is pathognomonic.
- **Rheumatoid arthritis (RA)** — anti-citrullinated protein antibodies (ACPA/anti-CCP) + rheumatoid factor (RF) attack synovial joint membranes; Th17-driven neutrophilic/macrophage synovitis → cartilage and bone destruction. HLA-DRB1 shared epitope is the major genetic risk factor.
- **Type 1 diabetes (T1D)** — autoreactive CD8+ T cells destroy insulin-secreting pancreatic β-cells; Th1-dominant; HLA-DQ8/DR4 strongly associated
- **Multiple sclerosis (MS)** — autoreactive T cells (Th17 prominent) and B cells damage CNS myelin; HLA-DRB1\*15:01 is the strongest genetic risk factor

### Hypersensitivity (Gell-Coombs classification)

| Type | Mechanism | Examples |
|:---|:---|:---|
| I (immediate) | IgE-mediated mast cell/basophil degranulation | Anaphylaxis, atopy, asthma |
| II (cytotoxic) | IgG/IgM against cell-surface antigens → complement + ADCC | Autoimmune hemolytic anemia, Goodpasture |
| III (immune complex) | IgG immune complex deposition → complement → tissue inflammation | SLE nephritis, serum sickness |
| IV (delayed-type) | Th1-mediated macrophage activation / Tc-mediated cytotoxicity | Contact dermatitis, tuberculin reaction, T1D |

**Anaphylaxis** is the most immediately life-threatening: systemic mast cell degranulation (IgE crosslinking by allergen → FcεRI → histamine, tryptase, LTC4) causes airway edema, bronchospasm, and circulatory collapse. Treatment: epinephrine (reverses bronchospasm and vasoconstriction).

### Immune evasion by pathogens

- **SARS-CoV-2** — NSP1 blocks mRNA translation of innate immune genes; ORF3b and ORF6 suppress IFN-β; N protein prevents TRIM25-mediated RIG-I ubiquitination; spike downregulates MHC-I on infected cells. Severe disease associated with defective early IFN response and subsequent hyperinflammation.
- **Influenza A** — NS1 binds TRIM25, blocking RIG-I signaling and IFN-β production; PB1-F2 promotes mitochondrial apoptosis in immune cells; neuraminidase cleaves sialic acids that normally facilitate IgA binding; antigenic drift in HA/NA evades existing antibody responses annually.
- **M. tuberculosis** — ESAT-6 perforates phagosomal membrane; LipoArabinomannan (LAM) from the mycobacterial cell wall blocks phagosome maturation (blocks Rab7, preventing lysosome fusion); coronin-1A retains functional mitochondria near the phagosome; the bacterium can persist for decades in granulomas. Reactivation risk is highest when cell-mediated immunity is suppressed (HIV co-infection, anti-TNF therapy, malnutrition).

[^janeway-immunobiology-9e]: Murphy K, Weaver C, Berg L. *Janeway's Immunobiology.* 9th ed. Garland Science; 2016.
[^abbas-immunology-9e]: Abbas AK, Lichtman AH, Pillai S. *Cellular and Molecular Immunology.* 9th ed. Elsevier; 2018.
[^medzhitov-2007-innate]: Medzhitov R. Recognition of microorganisms and activation of the immune response. *Nature.* 2007;449(7164):819-26. [doi:10.1038/nature06246](https://doi.org/10.1038/nature06246) · [PubMed 17943118](https://pubmed.ncbi.nlm.nih.gov/17943118/)
[^iwasaki-medzhitov-2015]: Iwasaki A, Medzhitov R. Control of adaptive immunity by the innate immune system. *Nat Immunol.* 2015;16(4):343-53. [doi:10.1038/ni.3123](https://doi.org/10.1038/ni.3123) · [PubMed 25789684](https://pubmed.ncbi.nlm.nih.gov/25789684/)
[^akbar-2016-immune-memory]: Akbar AN, Gilroy DW. Aging immunity may exacerbate COVID-19. *Science.* 2020;369(6501):256-257. [doi:10.1126/science.abb0762](https://doi.org/10.1126/science.abb0762) · [PubMed 32675364](https://pubmed.ncbi.nlm.nih.gov/32675364/)
[^who-immunology-2012]: World Health Organization / NIH. Understanding the Immune System: How It Works. NIH Publication No. 03-5423. [Read online →](https://www.niaid.nih.gov/sites/default/files/theimmunesystem.pdf)
