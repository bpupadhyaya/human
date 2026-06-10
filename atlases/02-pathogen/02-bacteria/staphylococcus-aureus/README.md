---
schema: pathogen-entry/v1
id: staphylococcus-aureus
name: Staphylococcus aureus
atlas: 02-pathogen
scale: 02-bacteria
status: draft
last_reviewed: 2026-06-05
summary: "Gram-positive coccus; commensal of anterior nares (20–30% carriage). Causes skin infections (impetigo, furuncles), pneumonia, bacteraemia, endocarditis, osteomyelitis, toxic shock. MRSA (methicillin-resistant) resists β-lactams via mecA-encoded PBP2a. Leading nosocomial pathogen."
aliases: ["S. aureus", "staph aureus", "MRSA", "golden staph", "coagulase-positive staph"]
sources:
  - id: lowy-1998-staph-review
    type: peer-reviewed
    cite: "Lowy FD. Staphylococcus aureus infections. N Engl J Med. 1998;339(8):520-32."
    doi: "10.1056/NEJM199808203390806"
    pmid: "9709046"
    url: "https://doi.org/10.1056/NEJM199808203390806"
  - id: gordon-2008-mrsa-pathogenesis
    type: peer-reviewed
    cite: "Gordon RJ, Lowy FD. Pathogenesis of methicillin-resistant Staphylococcus aureus infection. Clin Infect Dis. 2008;46 Suppl 5:S350-9."
    doi: "10.1086/533591"
    pmid: "18462090"
    url: "https://doi.org/10.1086/533591"
cross_links:
  - target: 01-human/07-system/immune-system
    relation: infects
    note: "S. aureus evades innate immunity via multiple redundant mechanisms: Protein A (SpA) blocks Fc-mediated opsonisation by binding IgG Fc regions; leukocidins (PVL, HlgAB/HlgCB, LukED) form pores in and kill neutrophils and macrophages; biofilm physically resists phagocytosis; and the polysaccharide capsule impairs complement deposition."
  - target: 01-human/06-organ/liver
    relation: damages
    note: "S. aureus bacteraemia seeds hepatic abscesses (via arterial dissemination to the liver). Panton-Valentine leukocidin (PVL) causes extensive tissue necrosis at haematogenous seeding sites. Staphylococcal toxic shock toxin (TSST-1) causes hepatic dysfunction and elevated transaminases as part of multi-organ failure in toxic shock syndrome."
  - target: 01-human/04-cellular/dendritic-cell
    relation: damages
    note: "Staphylococcal superantigens TSST-1 and SEB (staphylococcal enterotoxin B) bypass normal antigen presentation by cross-linking MHC-II (Vβ-region outside of the peptide groove) with T-cell receptor Vβ chains on up to 20% of all T cells simultaneously, causing massive T-cell activation and cytokine storm — the mechanism of toxic shock syndrome."
  - target: 01-human/04-cellular/neutrophil
    relation: damages
    note: "PVL (LukSF-PV) binds CD45+CR3 → β-barrel pore → neutrophil lysis; SCIN blocks C3 convertase → reduced opsonisation; CHIPS blocks FPR1+C5aR → impaired chemotaxis; staphyloxanthin quenches NADPH-oxidase ROS; PVL CA-MRSA strains cause necrotising pneumonia and fasciitis."
  - target: 01-human/04-cellular/macrophage
    relation: damages
    note: "Alpha-toxin lyses macrophages; TSST-1 drives TNF-α/IL-1β cytokine storm in TSS; biofilm polarises macrophages toward M2 (IL-10↑, TGF-β↑) impairing clearance; intracellular SCV phenotype evades macrophage killing and persists in osteoblasts and endothelial cells."
  - target: 01-human/04-cellular/cardiomyocyte
    relation: damages
    note: "Infective endocarditis: FnBPs adhere to fibronectin on valve endothelium → bacteraemia seeds myocardium; alpha-toxin disrupts cardiomyocyte junctions; septic emboli cause myocardial abscesses; MRSA endocarditis: 30-40% in-hospital mortality and 20% emergency cardiac surgery rate."
---

# Staphylococcus aureus

## Overview

*Staphylococcus aureus* is a **Gram-positive, catalase-positive, coagulase-positive coccus** and one of the most successful and clinically important human pathogens. It is simultaneously a **ubiquitous commensal** — colonising the anterior nares of approximately 20–30% of healthy adults persistently and a further 30% intermittently — and an **extraordinarily versatile pathogen** capable of causing a spectrum from trivial skin infections to rapidly fatal multi-organ disease [^lowy-1998-staph-review].

*S. aureus* achieves its clinical breadth through one of the largest virulence factor repertoires of any bacterial pathogen: adhesins for colonisation, toxins for host cell disruption, immune evasion proteins for phagocyte killing, and a remarkable capacity for horizontal acquisition of resistance genes. The emergence of **methicillin-resistant *S. aureus*** (MRSA) — first identified in 1961 in the UK — has created a persistent global public health emergency. MRSA accounts for the majority of hospital-acquired *S. aureus* infections in many countries and carries a case-fatality rate for bacteraemia of ~20–30%, compared to ~15–20% for methicillin-sensitive *S. aureus* (MSSA) bacteraemia [^gordon-2008-mrsa-pathogenesis].

Global burden:
- *S. aureus* bacteraemia: ~700,000 deaths/year globally (estimated); case-fatality rate ~20–30%
- Healthcare-associated *S. aureus* infections affect >2 million hospitalised patients/year in the US alone
- Community-acquired MRSA (CA-MRSA), driven by the USA300 clone in North America, causes severe necrotising skin infections and pneumonia in otherwise healthy young adults

## Structure

### Morphology

*S. aureus* cells are **spherical cocci** (~0.5–1.5 µm diameter) that divide in multiple planes, forming characteristic **grape-like clusters** (staphyle = bunch of grapes, Greek). They are non-motile, non-spore-forming, and facultative anaerobes. The species name "aureus" (golden) reflects production of **carotenoid pigment (staphyloxanthin)** — a virulence factor that quenches reactive oxygen species from neutrophil NADPH oxidase.

### Cell Wall

| Component | Description | Virulence / Resistance Role |
|:---|:---|:---|
| **Peptidoglycan** | Thick Gram-positive wall (~20–40 nm); cross-linked pentaglycine bridges (unique to *S. aureus*) | β-lactam target (PBPs 1–4); TLR2/NOD2 PAMP; structural rigidity |
| **Teichoic acids** | Wall teichoic acids (WTA; ribitol-phosphate backbone, D-alanine and GlcNAc decorations) + LTA | WTA is the dominant PAMP for TLR2; WTA also mediates nasal colonisation by binding MRSA to nasal epithelium via SDRP (scavenger receptor); target for anti-WTA phage enzybiotics |
| **Polysaccharide capsule** | Types 5 and 8 (in ~80% of clinical isolates) | Inhibits complement C3b deposition; impairs opsonophagocytosis; inversely correlated with biofilm formation |
| **PBP2a (PBP2')** | Low-affinity penicillin-binding protein encoded by *mecA* on SCCmec | Core of MRSA resistance — maintains transpeptidase activity when conventional PBPs are inhibited by β-lactams |
| **Protein A (SpA)** | Cell wall-anchored protein; binds IgG Fc and Fab (VH3) regions | Blocks opsonophagocytosis (anti-opsonic); captures and re-activates B cells (non-specific Fab binding); decoy for antibody-mediated complement |

### Virulence Factors

*S. aureus* maintains one of the most complex virulence regulons of any bacterial pathogen, controlled primarily by the **Agr** (accessory gene regulator) quorum-sensing system:

| Category | Factor | Mechanism |
|:---|:---|:---|
| **Adhesins (MSCRAMMs)** | ClfA/ClfB (clumping factor A/B), FnBPA/B, IsdA/B, CNA (collagen adhesin) | Bind fibrinogen, fibronectin, collagen, elastin; essential for colonisation of surfaces and tissue invasion |
| **Toxins — pore-forming** | α-toxin (Hla), β/γ-haemolysin, PVL (LukSF-PV), TSST-1, leukocidins (LukED, HlgAB) | Lyse erythrocytes, leukocytes, platelets; PVL kills neutrophils and causes tissue necrosis |
| **Toxins — superantigens** | TSST-1, SEA–SEE, SEIRA-SEIRU (SEs) | Bypass MHC-II groove peptide presentation; activate Vβ-specific T cells; cause TSS, staphylococcal scalded skin syndrome, food poisoning |
| **Immune evasion** | Protein A, Sbi (second IgG-binding protein), CHIPS, SCIN, SSL proteins | Block Fc-mediated opsonisation, inhibit complement C3 convertase, block FPR1 chemokine receptor (CHIPS) |
| **Enzymes** | Coagulase (Coa, vWbp), staphylokinase (SAK), proteases (V8/Glu-C, aureolysin), lipases, nucleases | Coagulase clots fibrinogen → fibrin shield around bacteria; staphylokinase dissolves fibrin clots (escape from abscess); proteases degrade IgG, complement proteins, antimicrobial peptides |
| **Biofilm** | PNAG (polysaccharide intercellular adhesin encoded by *ica* locus), eDNA, protein surface adhesins | Resist phagocytosis; 1,000-fold higher antibiotic tolerance; catheter and implant colonisation |
| **Carotenoid (Staphyloxanthin)** | Membrane carotenoid pigment | Quenches singlet oxygen and hydrogen peroxide from neutrophil oxidative burst; target of cholesterol biosynthesis inhibitors |

### Genome

- **Genome size:** ~2.8–2.9 Mb; GC content ~33%
- **Core genome:** ~1,700–2,000 genes conserved across all strains
- **Pathogenicity islands (SaPIs):** Mobile genetic elements encoding superantigen toxin genes (TSST-1, SEs); can be transduced by phages
- **Staphylococcal cassette chromosome *mec*** (**SCCmec**): Mobile element carrying *mecA* gene (and in SCCmec types I–V, additional resistance determinants); integration site at *orfX*; 11 SCCmec types identified
- **USA300 clone:** CA-MRSA dominant in North America; SCCmec type IV; carries *lukSF-PV* (PVL) and *arginine catabolic mobile element* (ACME); highly transmissible
- **Agr quorum-sensing:** Four allelic groups (agr types I–IV) produce autoinducing peptide (AIP) pheromones; activate at high cell density; upregulate secreted virulence factors (toxins, proteases) and downregulate surface adhesins — a switch from colonisation to invasive phenotype

## Infection Mechanism

### Colonisation and Nasal Carriage

The anterior nares are the primary reservoir:
- **Adhesion to nasal epithelium:** WTA mediates binding to scavenger receptor SREC-I and other nasal epithelial receptors; ClfB and IsdA bind loricrin and cytokeratin-10 in the nasal squamous epithelium
- Persistent nasal carriers (30% of adults) carry higher bacterial loads than intermittent carriers and have higher risk of auto-inoculation to skin wounds and surgical sites
- Nasal decolonisation with intranasal mupirocin (ointment) ± chlorhexidine body wash before elective surgery significantly reduces SSI (surgical site infection) rates in MRSA carriers

### Skin Infection Pathway

1. **Breach of skin barrier:** Trauma, eczema (which upregulates fibronectin and fibrinogen binding sites), insect bites, or surgical incisions expose subepithelial matrix proteins (fibronectin, fibrinogen, collagen)
2. **Adhesion:** MSCRAMMs (FnBPA/B, ClfA, CNA) tether *S. aureus* cells to exposed matrix proteins
3. **Local proliferation and Agr activation:** As bacterial density increases, Agr switches virulence programme from adhesins to secreted toxins; α-toxin lyses keratinocytes and endothelial cells; leukocidins kill infiltrating neutrophils
4. **Abscess formation:** Coagulase converts fibrinogen → fibrin, creating a walled-off fibrin capsule around the bacterial colony — the pathological basis of the furuncle (boil). This protects bacteria from phagocytosis but also limits tissue invasion
5. **Local vs. invasive disease:** Most skin infections (impetigo, furuncles, cellulitis) are self-limited or respond to drainage. Complicated infections occur when bacteria breach the fibrin wall → lymphatics/bloodstream → bacteraemia

### Bacteraemia and Deep Infection Seeding

*S. aureus* bacteraemia occurs in up to 40% of all *S. aureus* infections that access the bloodstream:

1. **Intravascular adhesion:** FnBPA/B binds fibronectin on activated endothelium; ClfA and ClfB bind fibrinogen/thrombin; Hla (α-toxin) disrupts endothelial tight junctions
2. **Intracellular persistence:** *S. aureus* invades non-professional phagocytes (endothelial cells, keratinocytes, osteoblasts) via FnBP-integrin α5β1 interaction → inside cells, bacteria switch to small colony variant (SCV) phenotype with reduced metabolic activity — evading antibiotic killing and maintaining persistent infection
3. **Deep seeding:** Bacteraemia seeds endocardium (especially tricuspid valve, IV drug users; mitral/aortic valves if prosthetic), bone/joint (haematogenous osteomyelitis), vertebrae (discitis), kidney (cortical abscess), brain (cerebral abscess), and liver

## Host Interactions

### Immune Evasion Arsenal

*S. aureus* deploys an uniquely comprehensive immune evasion repertoire:

| Evasion Mechanism | Virulence Factors | Target |
|:---|:---|:---|
| **Anti-opsonisation** | Protein A (SpA), Sbi, polysaccharide capsule | Block IgG Fc binding to FcγR on neutrophils; block C3b deposition |
| **Complement inhibition** | SCIN (staphylococcal complement inhibitor), Efb, Ecb | Inhibit C3 convertase; block C3b/iC3b opsonisation |
| **Chemotaxis inhibition** | CHIPS (chemotaxis inhibitory protein) | Blocks FPR1 and C5aR on neutrophils → impairs neutrophil recruitment to infection site |
| **Leukocyte killing** | PVL (LukSF-PV), LukED, HlgAB/HlgCB, α-toxin | Form β-barrel pores in neutrophil/macrophage membranes → lysis; PVL specifically targets CD45 and CR3 on human (but not murine) leukocytes |
| **Superantigen T-cell hyperactivation** | TSST-1, SEB–SEE | Activate 5–20% of all T cells non-specifically → cytokine storm (TSS); subsequent T-cell exhaustion/anergy impairs specific anti-staph immunity |
| **Biofilm** | PNAG, eDNA, Bap protein | Matrix sequesters antibiotics; impairs neutrophil phagocytosis; dispersin B-resistant |
| **Intracellular hiding** | FnBP-α5β1 integrin invasion → SCV phenotype | Evades antibiotics (reduced electron transport → reduced aminoglycoside/rifampicin uptake); persists in osteoblasts, endothelial cells |
| **Fibrin shield** | Coagulase (Coa), vWbp | Fibrin clot around bacteria blocks neutrophil access |

### Superantigen Biology

The staphylococcal superantigens (SAgs: TSST-1, SEB-SEIRU) deserve special emphasis as they represent the most potent T-cell activators known:

- Normal antigen presentation: a processed peptide (~15 AA) is presented in the MHC-II peptide groove; contacts the CDR1α, CDR2β of ~0.001% of T cells
- SAg mechanism: TSST-1 and SEs **bind outside the MHC-II peptide groove** (α1 and β1 domains) and cross-link to the TCR Vβ chain (outside CDR3 region) → activate ALL T cells bearing a particular Vβ family (~5–20% of the entire T cell repertoire simultaneously)
- Result: Massive CD4⁺ and CD8⁺ T-cell activation → IL-2, TNF-α, IFN-γ tsunami → fever, hypotension, multi-organ failure (toxic shock)
- Subsequently: T-cell exhaustion/anergy and Treg expansion, impairing specific adaptive anti-staph responses for months

### Cytokine Profile

- **Acute infection (skin/soft tissue):** TNF-α, IL-1β, IL-6 (NF-κB activation by LTA, peptidoglycan via TLR2/NOD2); IL-8/CXCL8 (neutrophil recruitment); IL-17 (Th17 protection)
- **Toxic shock syndrome:** TNF-α ↑↑↑, IFN-γ ↑↑↑, IL-2 ↑↑↑, IL-6 ↑↑ (superantigen-driven storm)
- **Biofilm infection (chronic):** IL-10 ↑, TGF-β ↑; relative immunosuppression; M2 macrophage polarisation around biofilm — tolerogenic milieu that impairs clearance

## Connections

**Infects** → [Immune system](../../../01-human/07-system/immune-system/README.md): *S. aureus* carries the most comprehensive immune evasion toolkit in clinical bacteriology — Protein A blocking opsonophagocytosis, SCIN/CHIPS crippling complement and chemotaxis, PVL and other leukocidins killing the neutrophils that do arrive, and superantigens bypassing and ultimately exhausting adaptive immunity. This combination makes *S. aureus* uniquely capable of persistent infection even in immunocompetent hosts.

**Damages** → [Liver](../../../01-human/06-organ/liver/README.md): Haematogenous seeding during bacteraemia can produce hepatic abscesses. More clinically significant is the contribution of staphylococcal toxins — particularly TSST-1-driven cytokine storm — to hepatic dysfunction in toxic shock syndrome, manifesting as elevated transaminases, jaundice, and occasionally acute liver failure in severe TSS.

**Damages** → [Dendritic cell](../../../01-human/04-cellular/dendritic-cell/README.md): Superantigens TSST-1 and SEB subvert the central function of antigen-presenting cells by cross-linking MHC-II with TCR Vβ chains outside the peptide groove — the normal quality-controlled pathway of adaptive immunity. This bypasses epitope-specific responses that DCs are designed to orchestrate, instead triggering mass polyclonal T-cell activation that overwhelms the system.

**Damages** → [Neutrophil](../../../01-human/04-cellular/neutrophil/README.md): PVL (LukSF-PV) binds CD45 and CR3 on human neutrophils to form β-barrel pores → cell lysis. SCIN inhibits C3 convertase, reducing opsonisation, while CHIPS blocks FPR1 and C5aR, impairing neutrophil chemotaxis to the infection site. Staphyloxanthin quenches neutrophil NADPH-oxidase reactive oxygen species — together these make CA-MRSA PVL strains uniquely lethal.

**Damages** → [Macrophage](../../../01-human/04-cellular/macrophage/README.md): Alpha-toxin lyses macrophages at high local concentrations. TSST-1 superantigen drives TNF-α and IL-1β cytokine storm in toxic shock syndrome. Biofilm infection shifts macrophages toward M2 polarisation (IL-10↑, TGF-β↑), creating a tolerogenic milieu that impairs clearance. Intracellular small colony variant (SCV) bacteria evade macrophage killing.

**Damages** → [Cardiomyocyte](../../../01-human/04-cellular/cardiomyocyte/README.md): Infective endocarditis begins with FnBP adhesion to fibronectin on damaged valve endothelium; bacteraemia then seeds the myocardium. Alpha-toxin disrupts cardiomyocyte tight junctions; septic emboli from vegetations cause myocardial abscesses. MRSA endocarditis carries 30–40% in-hospital mortality and a 20% rate of emergency cardiac surgery.

## Pathology

### Disease Spectrum

| Disease | Features | Mortality / Outcome |
|:---|:---|:---|
| **Impetigo** | Superficial skin; honey-crusted lesions; epidermolytic toxin A/B (ETA/ETB) cause desmoglein-1 cleavage | Excellent; topical/oral antibiotics |
| **Furuncle/carbuncle** | Deep folliculitis; abscess; PVL strains in CA-MRSA | Excellent with drainage; antibiotic adjunct |
| **Necrotising fasciitis (type II)** | Rapidly spreading fascial necrosis; PVL + α-toxin; emergency debridement required | 30–70%; surgical emergency |
| **Necrotising pneumonia** | CA-MRSA (PVL strains) post-influenza; haemoptysis; rapid respiratory failure | 60–75% |
| **Bacteraemia** | Fever, positive blood cultures; must rule out endocarditis (14-day minimum treatment) | 20–30% |
| **Infective endocarditis** | Tricuspid (IV drug users) or left-sided (prosthetic valves, healthcare); embolic phenomena; vegetation on echo | 20–40% (native valve), 45–60% (prosthetic valve) |
| **Osteomyelitis** | Haematogenous (children) or contiguous (diabetic foot, post-surgical); vertebral discitis in adults | 0–5% (acute); 25–50% (chronic MRSA) |
| **Toxic shock syndrome (TSS)** | Fever >38.9°C; hypotension; diffuse macular rash → desquamation; multi-organ dysfunction; TSST-1 (menstrual TSS) or SE (non-menstrual) | 5–15% case fatality |
| **Scalded skin syndrome (SSSS)** | Neonates/immunocompromised; ETA/ETB toxaemia → widespread superficial blistering (Nikolsky positive) | <5% in children; 30–60% in adults |

### Treatment

- **MSSA:** First-line — **anti-staphylococcal penicillins** (flucloxacillin IV; dicloxacillin/nafcillin in US) or **cefazolin** (equivalent efficacy, better tolerability for bacteraemia/endocarditis)
- **MRSA:** First-line — **vancomycin** (glycopeptide; inhibits transglycosylase/transpeptidase by binding D-Ala-D-Ala terminus; target AUC/MIC ≥400–600 μg·h/mL); **daptomycin** (cyclic lipopeptide; depolarises Gram-positive cell membrane; not for pneumonia — inhibited by surfactant); **linezolid** (oxazolidinone; protein synthesis inhibitor; excellent oral bioavailability)
- **Newer agents:** Ceftaroline (5th-gen cephalosporin with MRSA activity; binds PBP2a); tedizolid; dalbavancin/oritavancin (long-acting lipoglycopeptides; single-dose for ABSSSI)
- **VRSA (vancomycin-resistant *S. aureus*):** Extremely rare (<20 cases ever); *vanA* acquired from VRE; treated with linezolid, daptomycin combination
- **Biofilm infections (implant, prosthetic valve):** Device removal is often required; combination therapy with rifampicin (biofilm-penetrating) when device cannot be removed [^gordon-2008-mrsa-pathogenesis]

[^lowy-1998-staph-review]: Lowy FD. *Staphylococcus aureus* infections. *N Engl J Med.* 1998;339(8):520-32. [doi:10.1056/NEJM199808203390806](https://doi.org/10.1056/NEJM199808203390806) · [PubMed 9709046](https://pubmed.ncbi.nlm.nih.gov/9709046/)
[^gordon-2008-mrsa-pathogenesis]: Gordon RJ, Lowy FD. Pathogenesis of methicillin-resistant *Staphylococcus aureus* infection. *Clin Infect Dis.* 2008;46 Suppl 5:S350-9. [doi:10.1086/533591](https://doi.org/10.1086/533591) · [PubMed 18462090](https://pubmed.ncbi.nlm.nih.gov/18462090/)

---
*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
