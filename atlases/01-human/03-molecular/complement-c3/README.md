---
schema: human-scale-entry/v1
id: complement-c3
name: Complement C3
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-05
summary: "Most abundant complement protein (~1.3 mg/mL); central hub of classical, lectin, and alternative pathways. C3 convertase cleaves C3 → C3a (anaphylatoxin) + C3b (opsonin). Internal thioester enables covalent surface labelling for phagocytosis."
aliases: ["C3", "C3b", "iC3b", "C3d", "complement component 3", "C3a anaphylatoxin"]
sources:
  - id: stryer-biochemistry
    type: textbook
    cite: "Berg JM, Tymoczko JL, Stryer L. Biochemistry. 9th ed. W.H. Freeman; 2019."
    url: "https://www.macmillanlearning.com/college/us/product/Biochemistry/p/131911467X"
    accessed: "2026-06-05"
  - id: janeway-immunobiology
    type: textbook
    cite: "Murphy K, Weaver C. Janeway's Immunobiology. 9th ed. Garland Science; 2017."
    url: "https://www.garlandscience.com/product/isbn/9780815345053"
    accessed: "2026-06-05"
cross_links:
  - target: 01-human/07-system/immune-system
    relation: modulates
    note: "C3 is the central hub of all 3 complement pathways. C3b opsonises pathogens; C3a recruits neutrophils/mast cells; C3d on antigen lowers B cell activation threshold ~1000-fold via CR2/CD21 co-stimulation."
  - target: 01-human/04-cellular/macrophage
    relation: modulates
    note: "C3b and iC3b on opsonised targets bind CR1 and CR3 (Mac-1) on macrophages → phagocytic cup formation and phagolysosome maturation. iC3b-CR3 is especially important for phagocytosis of fungal cells (A. fumigatus)."
  - target: 01-human/05-tissue/glomerulus
    relation: modulates
    note: "Alternative pathway C3 dysregulation causes MPGN via GBM deposition. C3 nephritic factor (C3NeF) stabilises alternative C3 convertase → persistent C3 activation → MPGN type II/Dense Deposit Disease."
  - target: 01-human/03-molecular/c1-esterase-inhibitor
    relation: connects-to
    note: "C1-INH inhibits C1r/C1s, blocking the classical C3 convertase (C4b2a) formation; C1-INH deficiency → unchecked classical pathway → chronic C4 consumption → low C4 (hallmark of HAE); C3 is usually preserved in HAE because C3 convertase assembly is limited without sufficient C4b."
  - target: 01-human/07-system/hereditary-angioedema
    relation: connects-to
    note: "HAE from C1-INH deficiency uses low C4 as its hallmark diagnostic (chronic C1r/C1s activation → C4 consumption even between attacks, with C3 preserved); C3 is usually normal in HAE because C3 convertase assembly is limited by the insufficient C4b generated from unchecked C1."
  - target: 01-human/03-molecular/factor-h
    relation: connects-to
    note: "Factor H is the primary regulator of the alternative C3 convertase (C3bBb → decay acceleration) and Factor I cofactor (C3b → iC3b); CFH deficiency → runaway C3 consumption → C3 hypocomplementemia; C3 deposits in glomeruli (aHUS, C3 glomerulopathy) reflect unregulated C3b."
  - target: 01-human/07-system/ahus
    relation: connects-to
    note: "Uncontrolled alternative C3 convertase from CFH/CFI mutations → C3b deposits on glomerular endothelium → TMA (aHUS); low serum C3 reflects active complement consumption; C3 deposits on biopsy distinguish C3 glomerulopathy from IgA nephropathy (no immunoglobulin deposits)."
---

# Complement C3

## Overview

Complement C3 is the **most abundant complement protein** in human plasma (~1.3 mg/mL, ~185 kDa), and it occupies a unique position as the **convergence point of all three complement activation pathways**: classical, lectin, and alternative. All three pathways generate distinct **C3 convertase** enzymes that share the common function of cleaving C3 — initiating an amplification loop that can opsonize pathogens, recruit innate immune cells, and ultimately lyse targets via the membrane attack complex (MAC) [^janeway-immunobiology].

The central feature of C3 that makes it such a powerful opsonin is its **internal thioester bond** (between Cys988 and Gln991 of the α-chain, buried in a hydrophobic thioester domain). When C3 is cleaved, the thioester is exposed and rapidly reacts with hydroxyl or amine groups on target surfaces — forming a covalent ester or amide bond that covalently tags the pathogen surface with C3b for phagocytosis by receptors on neutrophils, macrophages, and dendritic cells [^stryer-biochemistry].

C3 deficiency is the most severe complement deficiency, manifesting as recurrent pyogenic bacterial infections (pneumococcus, H. influenzae, meningococcus) because opsonization, phagocyte recruitment, and MAC lysis all depend on C3. Conversely, unregulated C3 activation underlies several immune-mediated diseases including MPGN, atypical HUS, PNH, and AMD [^janeway-immunobiology].

## Structure

### Chain structure and thioester bond

C3 is synthesized as a single **110 kDa pro-C3** chain in hepatocytes and monocytes, which is processed by furin-like proteases in the secretory pathway into:

| Chain | MW | Role |
|:---|:---|:---|
| **α-chain** | ~110 kDa | Contains the thioester domain (TED), the C3a anaphylatoxin (N-terminal 77 aa), the C3d domain (thioester-bearing fragment), and MG domains |
| **β-chain** | ~75 kDa | Contains macroglobulin (MG) domains 1–6; structural scaffold; binding interface for factor B, factor H, CR1 |

The two chains are linked by a **single disulfide bond**. In native C3, the thioester (Cys-Gln) is protected from hydrolysis by the surrounding hydrophobic pocket. Cleavage by C3 convertase (cuts Arg726-Ser727 of the α-chain) releases C3a and induces a conformational change that exposes the thioester — allowing millisecond-scale covalent tagging of nearby surfaces.

### Molecular domains relevant to function

| Domain | Location | Function |
|:---|:---|:---|
| **C3a** (77 aa) | α-chain N-terminus | Anaphylatoxin; released after convertase cleavage |
| **TED** (thioester domain) | α-chain | Covalent ester/amide bond to surface; recognizes C3 receptors |
| **ANA domain** | α-chain | Anaphylatoxin-like; binds complement inhibitors |
| **CUB domain** | α-chain | Recruits MASP-2; role in convertase assembly |
| **MG1–MG8** | Both chains | Macroglobulin fold scaffold; interactions with factor B/H |

## Function

### C3a: anaphylatoxin

The **77-amino acid C3a** fragment binds C3aR (a Gi/Gq-coupled GPCR) on mast cells, basophils, eosinophils, and smooth muscle [^janeway-immunobiology]:
- **Mast cell degranulation** → histamine, leukotrienes, prostaglandins (rapid vascular permeability)
- **Smooth muscle contraction** — bronchoconstriction and gut motility
- **Neutrophil chemotaxis** (weaker than C5a)
- **Anti-inflammatory roles**: C3a also modulates macrophage function and T cell polarization in certain tissue contexts

C3a is rapidly inactivated by **carboxypeptidase N** → C3a-desArg (loses the terminal Arg), which has greatly reduced C3aR affinity.

### C3b: master opsonin

C3b is the large fragment (α-chain without C3a, still attached to β-chain) produced after convertase cleavage. The exposed thioester reacts within microseconds with target surface hydroxyls (→ ester bond on carbohydrates) or amines (→ amide bond on proteins):

**Downstream fates of surface-bound C3b** [^janeway-immunobiology]:

| Fragment | Generated by | Receptor | Effector function |
|:---|:---|:---|:---|
| **C3b** | C3 convertase | CR1 (CD35) | Opsonization, immune complex transport; also forms alternative/classical C5 convertases |
| **iC3b** | Factor I + factor H (or MCP) | CR3 (Mac-1, αMβ2), CR4 (αXβ2) | Phagocytosis without pro-inflammatory activation; fungal and bacterial clearance |
| **C3dg / C3d** | Factor I (further cleavage) | CR2 (CD21) | B cell co-stimulation; C3d-coated antigen activates B cells ~1000-fold more efficiently |

### C3 convertases: all pathways converge

| Pathway | Pattern recognized | C3 convertase |
|:---|:---|:---|
| **Classical** | C1q binds IgG/IgM on antigen → C1r/C1s → C4→C4b + C2→C2a | **C4b2a** |
| **Lectin** | MBL/ficolin binds mannose/GlcNAc → MASP-1/2 → C4→C4b + C2→C2a | **C4b2a** |
| **Alternative** | Spontaneous C3 hydrolysis (tick-over: C3(H₂O)) + factor B + factor D → C3bBb (properdin/factor P stabilizes); amplification loop | **C3bBb** |

The alternative pathway provides a **constitutive low-level tick-over** that amplifies C3 deposition on any surface lacking membrane regulators. All mammalian self-cells express GPI-anchored regulators (DAF/CD55, CD59) or surface-bound factor H that block alternative pathway amplification — "self" vs. "non-self" discrimination.

### Amplification and MAC formation

C3b deposits covalently on the target surface → C3bBb (alternative C5 convertase = C3b + Bb + C3b) or C4b2a3b (classical/lectin C5 convertase) → C5 cleaved → **C5a** (potent anaphylatoxin, chemotactic for neutrophils) + **C5b** → binds C6 → C5b-6 binds C7 → C5b-67 inserts into membrane bilayer → C8 → C9 polymerizes (poly-C9, 18 monomers) → **MAC (C5b-6789)** → transmembrane pore (10 nm internal diameter) → osmotic lysis of bacteria, nucleated cells, and PNH erythrocytes.

## Mechanism

### Alternative pathway amplification

The alternative pathway acts as both an initiating and **amplifying** mechanism for C3 deposition:

1. Spontaneous hydrolysis of native C3 → **C3(H₂O)** (conformation mimics C3b)
2. C3(H₂O) + factor B → C3(H₂O)Bb (initial C3 convertase)
3. C3b deposited on any surface → factor B binds C3b → factor D cleaves Bb → **C3bBb** (alternative C3 convertase)
4. **Properdin (factor P)** binds C3bBb → stabilizes the convertase (half-life: <90 s without properdin, ~30 min with properdin)
5. C3bBb cleaves more C3 → more C3b on surface → more C3bBb → exponential amplification (**the amplification loop**)

### Regulation

Self-cells avoid complement attack by expressing:

| Regulator | Type | Mechanism |
|:---|:---|:---|
| **Factor H** | Soluble plasma protein | Binds C3b (blocks factor B, accelerates decay of C3bBb, cofactor for factor I); preferentially recognizes polyanions (sialic acid, GAGs) on self-surfaces |
| **DAF (CD55)** | GPI-anchored membrane protein | Accelerates decay of C3bBb and C4b2a on the cell surface |
| **MCP (CD46)** | Transmembrane protein | Cofactor for factor I-mediated cleavage of C3b → iC3b on cell surface |
| **CR1 (CD35)** | Transmembrane protein | Cofactor for factor I; immune complex transport to liver/spleen on RBCs |
| **Factor I** | Soluble serine protease | Cleaves C3b → iC3b (with cofactors H, MCP, CR1); and iC3b → C3dg + C3c |
| **CD59 (protectin)** | GPI-anchored membrane protein | Blocks poly-C9 formation → prevents MAC assembly on self-cells |

## Connections

- `modulates` → **[immune-system](../../07-system/immune-system/README.md)** — C3 is the convergence hub of all 3 complement pathways; C3b opsonizes pathogens, C3a recruits neutrophils/mast cells, C3d lowers B cell activation threshold ~1000-fold via CR2/CD21 co-stimulation [^janeway-immunobiology]
- `modulates` → **[macrophage](../../04-cellular/macrophage/README.md)** — C3b/iC3b on opsonised targets bind CR1/CR3 (Mac-1/αMβ2) on macrophages → phagocytic cup formation; iC3b-CR3 is critical for fungal (A. fumigatus) and mycobacterial clearance [^janeway-immunobiology]
- `modulates` → **[glomerulus](../../05-tissue/glomerulus/README.md)** — alternative pathway dysregulation drives C3 deposition in GBM causing MPGN; C3 nephritic factor (C3NeF) stabilises C3bBb → persistent complement activation → Dense Deposit Disease [^janeway-immunobiology]
- `connects-to` → **[C1-Esterase Inhibitor](../c1-esterase-inhibitor/README.md)** — C1-INH inhibits C1r/C1s, blocking the classical C3 convertase (C4b2a) formation; C1-INH deficiency → unchecked classical pathway → chronic C4 consumption → low C4 (hallmark of HAE); C3 is usually preserved in HAE because C3 convertase assembly is limited without sufficient C4b.
- `connects-to` → **[Hereditary Angioedema](../../07-system/hereditary-angioedema/README.md)** — HAE from C1-INH deficiency uses low C4 as its hallmark diagnostic (chronic C1r/C1s activation → C4 consumption even between attacks, with C3 preserved); C3 is usually normal in HAE because C3 convertase assembly is limited by the insufficient C4b generated from unchecked C1.
- `connects-to` → **[Factor H](../factor-h/README.md)** — Factor H is the primary regulator of the alternative C3 convertase (C3bBb → decay acceleration) and Factor I cofactor (C3b → iC3b); CFH deficiency → runaway C3 consumption → C3 hypocomplementemia; C3 deposits in glomeruli (aHUS, C3 glomerulopathy) reflect unregulated C3b.
- `connects-to` → **[Atypical HUS](../../07-system/ahus/README.md)** — Uncontrolled alternative C3 convertase from CFH/CFI mutations → C3b deposits on glomerular endothelium → TMA (aHUS); low serum C3 reflects active complement consumption; C3 deposits on biopsy distinguish C3 glomerulopathy from IgA nephropathy (no immunoglobulin deposits).

## Pathology

| Condition | Mechanism | Clinical / diagnostic |
|:---|:---|:---|
| **C3 deficiency** | Autosomal recessive; null mutations in *C3* (rare, ~1:1,000,000) | Recurrent pyogenic bacterial infections (Streptococcus, Haemophilus, Neisseria), immune complex glomerulonephritis, SLE-like disease; ↓C3, ↓CH50, ↓AH50 |
| **Dense Deposit Disease (MPGN type II)** | C3 nephritic factor (C3NeF) — IgG autoantibody stabilises C3bBb → continuous C3 consumption → hypocomplementaemia → C3-only deposits in GBM | ↓↓C3, normal C4; dense osmophilic GBM deposits on EM; eculizumab emerging |
| **MPGN type III** | Factor H mutations or autoantibodies → impaired C3b inactivation → complement-mediated GN | ↓C3; subendothelial + subepithelial deposits |
| **PNH (Paroxysmal Nocturnal Haemoglobinuria)** | *PIGA* somatic mutation → loss of GPI anchors (DAF, CD59) on haematopoietic clone → unregulated MAC on RBCs → intravascular haemolysis + thrombosis | ↓GPI proteins by flow cytometry; eculizumab/ravulizumab (anti-C5) → standard of care |
| **Atypical HUS (aHUS)** | Factor H, CD46, factor I, or factor B mutations/autoantibodies → complement-mediated microangiopathy → TMA in kidney/brain/heart | TMA with ↓C3; eculizumab dramatically effective; distinguish from TTP (ADAMTS13) and Shiga-toxin HUS |
| **AMD (Age-related Macular Degeneration)** | CFH Y402H polymorphism → reduced factor H affinity for retinal Bruch's membrane → ↑alternative pathway complement → drusen, RPE damage | ~50% of AMD genetic risk attributable to CFH; complement inhibitors (pegcetacoplan) in geographic atrophy |
| **CHAPLE disease** | Biallelic *CD55* loss → complement hyperactivation → gut protein-losing enteropathy, angioedema, thrombosis | ↑C5b-9 in serum; eculizumab effective |
| **Systemic lupus erythematosus** | Complement deficiencies (C1q/C2/C4) → impaired immune complex clearance → → IC accumulation → tissue damage; paradoxically C3/C4 consumed during flares | Serum C3/C4 levels monitor disease activity |

## See Also

- [IL-6](../il-6/README.md) — cytokine driving C3 upregulation during acute-phase response
- [TNF-alpha](../tnf-alpha/README.md) — synergizes with complement anaphylatoxins (C3a, C5a) in inflammation
- [Macrophage](../../04-cellular/macrophage/README.md) — primary complement receptor-expressing phagocyte (CR1, CR3, CR4)
- [B-cell](../../04-cellular/b-cell/README.md) — C3d-CR2 co-stimulation dramatically lowers activation threshold; BCR signal augmentation
- [Neutrophil](../../04-cellular/neutrophil/README.md) — primary C5a responder; CR1/CR3 expressing professional phagocyte
- [Immune system](../../07-system/immune-system/README.md) — overarching system context; complement is an arm of innate immunity
- [Glomerulus](../../05-tissue/glomerulus/README.md) — key site of complement-mediated pathology (MPGN, aHUS)
- [Kidney](../../06-organ/kidney/README.md) — target organ in complement-mediated nephritis

[^stryer-biochemistry]: Berg JM, Tymoczko JL, Stryer L. *Biochemistry.* 9th ed. W.H. Freeman; 2019. [Macmillan Learning](https://www.macmillanlearning.com/college/us/product/Biochemistry/p/131911467X)
[^janeway-immunobiology]: Murphy K, Weaver C. *Janeway's Immunobiology.* 9th ed. Garland Science; 2017. [Garland Science](https://www.garlandscience.com/product/isbn/9780815345053)
