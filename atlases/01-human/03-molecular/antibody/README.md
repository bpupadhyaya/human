---
schema: human-scale-entry/v1
id: antibody
name: Antibody
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-06
summary: "Y-shaped glycoproteins secreted by plasma cells; two heavy + two light chains. Variable domains (VH/VL) confer antigen specificity; constant domains determine isotype (IgG, IgA, IgM, IgE, IgD) and effector functions (neutralization, opsonization, complement activation, ADCC)."
aliases: ["immunoglobulin", "Ig", "antibody", "Ab", "gamma-globulin"]
sources:
  - id: schroeder-2010-ig-structure
    type: peer-reviewed
    cite: "Schroeder HW Jr, Cavacini L. Structure and function of immunoglobulins. J Allergy Clin Immunol. 2010;125(2 Suppl 2):S41-52."
    doi: "10.1016/j.jaci.2009.09.046"
    pmid: "20176268"
    url: "https://doi.org/10.1016/j.jaci.2009.09.046"
  - id: burton-2002-antibodies-vaccines
    type: peer-reviewed
    cite: "Burton DR. Antibodies, viruses and vaccines. Nat Rev Immunol. 2002;2(9):706-713."
    doi: "10.1038/nri891"
    pmid: "12209139"
    url: "https://doi.org/10.1038/nri891"
  - id: vidarsson-2014-igg-subclasses
    type: peer-reviewed
    cite: "Vidarsson G, Dekkers G, Rispens T. IgG subclasses and allotypes: from structure to effector functions. Front Immunol. 2014;5:520."
    doi: "10.3389/fimmu.2014.00520"
    pmid: "25368619"
    url: "https://doi.org/10.3389/fimmu.2014.00520"
cross_links:
  - target: 01-human/04-cellular/plasma-cell
    relation: expressed-by
    note: "Antibodies are secreted by plasma cells — terminally differentiated B cells that underwent class switch recombination and affinity maturation in germinal centers; long-lived bone marrow plasma cells secrete high-affinity antibodies constitutively for decades."
  - target: 01-human/04-cellular/b-cell
    relation: expressed-by
    note: "Naïve B cells express membrane-bound antibody (BCR, B cell receptor) as the antigen-recognition unit; upon activation, differentiation to plasma cells produces secreted antibody of the same antigen specificity; memory B cells retain BCR for rapid recall responses."
  - target: 01-human/03-molecular/immunoglobulin-g
    relation: connects-to
    note: "IgG is the most abundant serum antibody isotype (~75% of total Ig) and the dominant antibody in secondary immune responses; its four subclasses (IgG1-4) differ in effector function (complement activation, FcγR binding, ADCC) and are encoded by distinct constant-region genes."
  - target: 01-human/05-tissue/germinal-center
    relation: expressed-by
    note: "Germinal centers produce high-affinity, isotype-switched antibodies via somatic hypermutation and class switch recombination; GC-derived B cells differentiate into long-lived plasma cells or memory B cells carrying somatically matured antibody specificity."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "ADCC: IgG Fc binds FcγRIII (CD16) on NK cells → degranulation → perforin/granzyme release → target cell killing; ADCC mediates antiviral protection (HIV, CMV, influenza) and anti-tumor activity of trastuzumab and rituximab."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "FcγRI/II/III on macrophages bind IgG-opsonized targets → phagocytosis; antibody+C3b → enhanced opsonophagocytosis; macrophage FcγRIIA mediates platelet activation in HIT; ADCP is a key anti-tumor effector mechanism."
  - target: 01-human/04-cellular/mast-cell
    relation: connects-to
    note: "IgE (via FcεRI on mast cells) mediates type I hypersensitivity; allergen cross-links surface IgE → mast cell degranulation → histamine, leukotrienes → allergic symptoms; IgE-mast cell axis is the mechanistic basis of anaphylaxis."
---

# Antibody

## Overview

**Antibodies** (immunoglobulins, Ig) are **Y-shaped glycoprotein molecules** secreted by **plasma cells** — terminally differentiated B lymphocytes — that bind antigens with high specificity and mediate a diverse array of immune effector functions. They are the primary soluble mediators of **humoral immunity**: present in serum, mucosal secretions, colostrum, and on B cell surfaces (as B cell receptor, BCR), they defend the host through **pathogen neutralization, opsonization, complement activation, antibody-dependent cellular cytotoxicity (ADCC)**, and **neonatal passive immunity**.

The human immunoglobulin repertoire is vast: **10⁸–10¹¹ distinct antibody specificities** are generated through V(D)J recombination, junctional diversity, and somatic hypermutation — a combinatorial diversity sufficient to recognize virtually any molecular structure. The adaptive immune response narrows and refines this repertoire through clonal selection: antigen binding selects specific B cells for expansion and affinity maturation, generating high-affinity antibodies (femtomolar Kd) against the invading pathogen [^schroeder-2010-ig-structure].

Five classes (**isotypes**) of immunoglobulins exist in humans — IgG, IgA, IgM, IgD, IgE — each with distinct structural features, tissue distribution, and effector functions arising from their different heavy chain constant regions.

## Structure

### Basic immunoglobulin structure

All antibodies share a conserved **"Y" architecture** comprising four polypeptide chains:
- **Two identical heavy chains (H):** ~50 kDa each; consists of one variable domain (VH) + three or four constant domains (CH1-CH3 or CH1-CH4 depending on isotype)
- **Two identical light chains (L):** ~25 kDa each; consists of one variable domain (VL) + one constant domain (CL); two types — **kappa (κ)** or **lambda (λ)** — present in 60:40 ratio in humans
- Chains joined by **interchain disulfide bonds**: H-L bonds at CH1-CL junction; H-H bonds at hinge region

**Structural domains:**
- **Fab (Fragment, antigen-binding):** Each "arm" of the Y; contains VH + CH1 (heavy) + VL + CL (light); the **antigen-binding site** (paratope) is at the tip of Fab, formed by six hypervariable loops (CDR1-CDR3 of VH and VL)
- **Fc (Fragment, crystallizable):** The "stem" of the Y; consists of CH2 + CH3 (or CH2 + CH3 + CH4) of both heavy chains; determines isotype class and mediates effector functions via Fc receptors (FcγR, FcαR, FcεR) and complement C1q
- **Hinge region:** Flexible proline-rich segment between CH1 and CH2; allows independent movement of the two Fab arms; site of inter-heavy chain disulfide bonds; absent in IgM and IgE

**Variability:** CDRs (complementarity-determining regions) — H1, H2, H3 and L1, L2, L3 — are the hypervariable loops that form the antigen-combining site; CDR3 of the heavy chain (generated by V-D-J junction) is the most diverse and often the primary determinant of specificity.

### Isotype classes and properties

| Isotype | Heavy chain | Serum [mg/mL] | Half-life (days) | Key features |
|:---|:---|:---|:---|:---|
| **IgG** | γ (γ1-γ4) | 8–16 | 21 | Dominant secondary response; placental transfer; 4 subclasses; ADCC |
| **IgA** | α (α1, α2) | 1.5–3 | 6 | Mucosal immunity; secretory IgA (dimer + SC + J chain); colostrum |
| **IgM** | μ | 0.5–2 | 10 | Pentamer; first in primary response; strong complement activation via C1q |
| **IgD** | δ | <0.03 | 3 | Primarily BCR on naïve B cells; serum function unclear |
| **IgE** | ε | <0.0001 | 2 | Allergy/parasites; binds FcεRI on mast cells/basophils; immediate hypersensitivity |

**IgG subclasses (IgG1-4):** Differ in hinge length, inter-H disulfide bond pattern, complement activation efficiency (IgG1 > IgG3 >> IgG2 >> IgG4), and FcγR binding [^vidarsson-2014-igg-subclasses].

## Function

### Neutralization

Antibodies physically **block pathogen entry** or **inactivate toxins** by binding to surface proteins (viral capsid proteins, bacterial adhesins, toxin receptor-binding domains) and sterically preventing their interaction with host cell receptors. This is the primary mechanism of **vaccine-induced protection**. Examples: anti-HA neutralizing antibodies block influenza hemagglutinin–sialic acid binding; anti-spike (RBD) antibodies block SARS-CoV-2 ACE2 binding; anti-tetanus toxin antibodies block neuromuscular blockade.

### Opsonization

IgG coating of bacteria and viruses creates **opsonins** recognized by Fcγ receptors (FcγRI, FcγRIIa, FcγRIIIa) on macrophages and neutrophils → phagocytosis ~1,000-fold more efficient than unopsonized particles. IgG-opsonized targets also activate complement via C1q binding (classical pathway) → C3b deposition → further enhanced phagocytosis.

### Complement activation (CDC)

IgM (pentamer) or IgG clusters on target cell surfaces → C1q binding → classical complement cascade → **membrane attack complex (MAC, C5b-9)** → lysis of bacteria, virions, and tumor cells. IgG is less efficient than IgM per molecule (requires IgG clustering); this explains why IgM dominates early responses before affinity-matured IgG is produced.

### ADCC (Antibody-dependent cellular cytotoxicity)

IgG-coated target cells are recognized by FcγRIIIa (CD16) on **NK cells** → NK cell degranulation → perforin and granzyme release → target cell killing. ADCC is important for anti-tumor antibodies (trastuzumab, rituximab) and in HIV control.

### Neonatal passive immunity and FcRn

**Neonatal Fc receptor (FcRn)** mediates:
1. **Transplacental IgG transfer:** FcRn on syncytiotrophoblasts binds maternal IgG at acidic pH (6.0) in endosomes → transcytosis → fetal circulation; provides passive protection until ~6 months of age
2. **IgG homeostasis/half-life:** FcRn in endothelial cells rescues IgG from lysosomal degradation → 21-day half-life (vs ~7 days for IgA/IgM without FcRn protection)

## Mechanism

### Antigen-binding mechanism

Antibody-antigen interaction is **non-covalent** (H-bonds, van der Waals, electrostatic, hydrophobic): the paratope (CDR loops) is complementary in shape to the epitope on the antigen. CDRs adopt a range of geometries — flat loops for protein interfaces, deep pockets for small haptens, long protruding loops for peptides in grooves. **Affinity** is measured as Kd = koff/kon; germline antibodies have Kd ~10⁻⁶ to 10⁻⁸ M; affinity-matured antibodies reach 10⁻¹⁰ to 10⁻¹² M.

### Class switch recombination (CSR)

During B cell activation, **AID (Activation-Induced Cytidine Deaminase)** introduces DNA double-strand breaks between switch regions upstream of CH genes → NHEJ joins VDJ to a new CH gene → irreversible switch from IgM to IgG, IgA, or IgE (same VDJ/specificity, different isotype). Cytokine environment determines isotype: IL-4/IL-13 → IgE/IgG4; IFN-γ → IgG1/IgG3; TGF-β + IL-10 → IgA.

### Monoclonal antibodies in medicine [^burton-2002-antibodies-vaccines]

Therapeutic monoclonal antibodies (mAbs) — produced by hybridoma technology or recombinant expression — are the fastest-growing drug class:
- **Tumor targeting:** Rituximab (anti-CD20, B cell lymphoma); trastuzumab (anti-HER2, breast cancer); cetuximab (anti-EGFR, colorectal cancer)
- **Inflammatory diseases:** Adalimumab (anti-TNF-α); tocilizumab (anti-IL-6R); dupilumab (anti-IL-4Rα)
- **Antibody-drug conjugates (ADCs):** T-DM1 (trastuzumab-emtansine): antibody specificity + chemotherapy payload
- **Bispecific antibodies:** Blinatumomab (anti-CD19 × anti-CD3); redirect T cells to kill tumor cells

## Connections

- `expressed-by` → **[Plasma Cell](../../04-cellular/plasma-cell/README.md)** — plasma cells are the dedicated antibody factories of the immune system; a single plasma cell secretes ~2,000 antibody molecules per second for its entire lifespan.
- `expressed-by` → **[B Cell](../../04-cellular/b-cell/README.md)** — naïve and memory B cells display membrane-bound antibody (BCR) as their antigen recognition unit; BCR signaling drives B cell activation, clonal expansion, and differentiation.
- `connects-to` → **[Immunoglobulin G](../immunoglobulin-g/README.md)** — IgG is the dominant serum isotype; its four subclasses (IgG1-4) mediate the bulk of secondary immune responses, ADCC, complement activation, and transplacental passive immunity.
- `expressed-by` → **[Germinal Center](../../05-tissue/germinal-center/README.md)** — germinal centers produce the high-affinity, isotype-switched antibodies that underlie durable humoral immunity; B cells exit GCs as long-lived plasma cells or memory B cells carrying somatically matured antibodies.
- `connects-to` → **[Natural Killer Cell](../../04-cellular/natural-killer-cell/README.md)** — ADCC: IgG Fc binds FcγRIII (CD16) on NK cells → degranulation → perforin/granzyme release → target cell killing; ADCC mediates antiviral protection against HIV, CMV, and influenza and underlies anti-tumor activity of trastuzumab and rituximab.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — FcγRI/II/III on macrophages bind IgG-opsonized targets → phagocytosis; IgG+C3b together synergistically enhance opsonophagocytosis; macrophage FcγRIIA drives platelet activation in HIT; ADCP is a key anti-tumor effector mechanism of therapeutic antibodies.
- `connects-to` → **[Mast Cell](../../04-cellular/mast-cell/README.md)** — IgE binds FcεRI on mast cells with high affinity; allergen cross-links mast cell–bound IgE → immediate degranulation → histamine, leukotrienes, prostaglandins → allergic symptoms; IgE-mast cell axis is the mechanistic basis of type I hypersensitivity and anaphylaxis.

[^schroeder-2010-ig-structure]: Schroeder HW Jr, Cavacini L. Structure and function of immunoglobulins. *J Allergy Clin Immunol.* 2010;125(2 Suppl 2):S41-52. [doi:10.1016/j.jaci.2009.09.046](https://doi.org/10.1016/j.jaci.2009.09.046) · [PubMed 20176268](https://pubmed.ncbi.nlm.nih.gov/20176268/)
[^burton-2002-antibodies-vaccines]: Burton DR. Antibodies, viruses and vaccines. *Nat Rev Immunol.* 2002;2(9):706-713. [doi:10.1038/nri891](https://doi.org/10.1038/nri891) · [PubMed 12209139](https://pubmed.ncbi.nlm.nih.gov/12209139/)
[^vidarsson-2014-igg-subclasses]: Vidarsson G, Dekkers G, Rispens T. IgG subclasses and allotypes: from structure to effector functions. *Front Immunol.* 2014;5:520. [doi:10.3389/fimmu.2014.00520](https://doi.org/10.3389/fimmu.2014.00520) · [PubMed 25368619](https://pubmed.ncbi.nlm.nih.gov/25368619/)

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
