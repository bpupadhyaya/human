---
schema: human-scale-entry/v1
id: cftr
name: CFTR
atlas: 01-human
scale: 03-molecular
status: draft
last_reviewed: 2026-06-07
summary: "CFTR is an ATP-gated chloride and bicarbonate channel; F508del (most common CF mutation) causes protein misfolding and ER retention → absent surface expression → thick mucus; CFTR modulators (elexacaftor/tezacaftor/ivacaftor) restore partial function in F508del homozygotes."
aliases: ["CFTR", "cystic fibrosis transmembrane conductance regulator", "ABCC7", "CFTR channel", "CFTR F508del", "CFTR modulator", "CFTR ivacaftor", "CFTR chloride channel", "CFTR corrector", "CFTR potentiator"]
sources:
  - id: riordan-1989-cftr-cloning
    type: peer-reviewed
    cite: "Riordan JR, Rommens JM, Kerem B, et al. Identification of the cystic fibrosis gene: cloning and characterization of complementary DNA. Science. 1989;245(4922):1066-1073."
    doi: "10.1126/science.2475911"
    pmid: "2475911"
    url: "https://doi.org/10.1126/science.2475911"
  - id: heijerman-2019-etd-cf
    type: peer-reviewed
    cite: "Heijerman HGM, McKone EF, Downey DG, et al. Efficacy and safety of the elexacaftor plus tezacaftor plus ivacaftor combination regimen in people with cystic fibrosis homozygous for the F508del mutation: a double-blind, randomised, phase 3 trial. Lancet. 2019;394(10212):1940-1948."
    doi: "10.1016/S0140-6736(19)32597-8"
    pmid: "31679946"
    url: "https://doi.org/10.1016/S0140-6736(19)32597-8"
cross_links:
  - target: 01-human/07-system/cystic-fibrosis
    relation: connects-to
    note: "Biallelic CFTR LOF → cystic fibrosis; F508del is the most common CF allele (~70% worldwide); CFTR class I-VI mutations differ in whether protein is absent, misfolded, or dysfunctional; elexacaftor/tezacaftor/ivacaftor (Trikafta) transformed CF prognosis for F508del patients."
  - target: 01-human/03-molecular/prss1
    relation: connects-to
    note: "CFTR mutations act as disease modifiers in hereditary pancreatitis: CFTR LOF → reduced pancreatic duct bicarbonate → acidic duct fluid → enhanced trypsinogen activation → pancreatitis risk; compound heterozygosity with PRSS1 or SPINK1 mutations worsens disease severity."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "TGF-β1 is a major modifier of CF lung disease severity: TGF-β1 promoter polymorphisms (codon 10/25) correlate with lung function decline in CF; airway TGF-β1 signaling promotes fibrosis and reduces CFTR modulator efficacy; TGF-β1 blockade is explored as CF adjunct therapy."
  - target: 01-human/03-molecular/nlrp3-inflammasome
    relation: connects-to
    note: "NLRP3 inflammasome is constitutively activated in CF airway: CFTR LOF → abnormal mitochondrial reactive oxygen species → NLRP3 priming and activation → IL-1β/IL-18 release → neutrophilic airway inflammation; IL-1β inhibitors (canakinumab) explored in CF lung disease."
  - target: 01-human/07-system/pancreatic-cancer
    relation: connects-to
    note: "Chronic pancreatitis from CFTR LOF → exocrine destruction → pancreatic insufficiency in ~85% of CF patients; CFTR mutations are independent risk modifiers for sporadic PDAC; CFTR LOF → reduced pancreatic duct HCO3- → acidic fluid → trypsinogen activation → acinar damage."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "CFTR LOF → unresolved Pseudomonas biofilm → NF-κB activation → IL-8/CXCL8/GM-CSF → neutrophilic inflammation; NF-κB is constitutively activated in CF epithelia even without active infection; Trikafta therapy reduces NF-κB-driven airway cytokine levels."
  - target: 01-human/03-molecular/tnf-alpha
    relation: connects-to
    note: "TNF-α is chronically elevated in CF airway fluid and sputum; CFTR LOF → NF-κB hyperactivation → TNF-α/IL-1β → self-perpetuating inflammatory cycle; TNF-α-driven neutrophil elastase destroys airway structure; anti-TNF strategies have not demonstrated clinical benefit in CF trials."
---

# CFTR

## Overview

**CFTR** (Cystic Fibrosis Transmembrane conductance Regulator; also ABCC7) is a 1,480 amino acid (170 kDa) **ATP-binding cassette (ABC) transporter superfamily** member that functions as a **cAMP-activated, ATP-gated chloride and bicarbonate ion channel** expressed apically on epithelial cells lining the airways, gut, pancreatic ducts, bile ducts, sweat gland ducts, and vas deferens. Unlike most ABC transporters (which transport large molecules using ATP hydrolysis for export), CFTR is uniquely an ion channel: ATP binding at its two nucleotide-binding domains (NBD1, NBD2) drives channel gating; PKA-mediated phosphorylation of the regulatory (R) domain is required for ATP-gated activity. CFTR-mediated Cl⁻ and HCO₃⁻ secretion into epithelial lumens drives osmotic water secretion and maintains the thin, low-viscosity surface liquid layer that enables mucociliary clearance in the airways.

Biallelic CFTR mutations cause **cystic fibrosis (CF)**, the most common life-shortening recessive genetic disease in European ancestry populations (~1 in 2,500 births). CFTR was identified by positional cloning by Riordan, Rommens, and Tsui in 1989 — one of the landmark achievements of classical genetics [^riordan-1989-cftr-cloning]. The **F508del** mutation (deletion of Phe508 in NBD1) accounts for ~70% of CF alleles worldwide and causes protein misfolding with ER retention, absent surface expression, and absent channel function. The development of **CFTR modulators** — small molecules that correct protein folding (correctors) or potentiate channel opening (potentiators) — has transformed CF prognosis: the triple combination elexacaftor/tezacaftor/ivacaftor (Trikafta) achieves near-normalization of CFTR function in F508del homozygotes, improving ppFEV1 by ~14 percentage points and sweat chloride by ~40 mmol/L [^heijerman-2019-etd-cf].

**CFTR mutation classification (functional classes):**

| Class | Molecular defect | CFTR protein fate | Example mutations | Modulator strategy |
|---|---|---|---|---|
| I | Premature stop, frameshift, splice | No protein produced | G542X, W1282X, 621+1G>T | Nonsense read-through (ataluren; limited) |
| II | Misfolding → ER retention | Protein degraded in ER | F508del (most common) | Correctors (VX-661, VX-445) + potentiator |
| III (gating) | Protein reaches surface, non-functional gate | Surface-resident; gate stuck shut | G551D | Potentiator (ivacaftor alone) |
| IV | Reduced Cl⁻ conductance | Surface-resident; leaky channel | R117H | Potentiator (may benefit) |
| V | Reduced mRNA/protein expression | Less protein produced | 3849+10kbC>T, A455E | Potentiator ± corrector |
| VI | Surface instability | Rapid internalization from surface | 4326delTC | Correctors to stabilize |

## Structure

### CFTR protein domains

**Transmembrane domain 1 (TMD1; aa 1-390):**
- Six transmembrane helices (TM1-6); forms half of the chloride channel pore; TM6 lines the channel lumen and contains key residues for Cl⁻ selectivity and conductance
- TMD1 connects to NBD1 via intracellular coupling helices (ICH1, ICH2); ICH2 contains direct contacts to NBD1 Q-loop → transmits ATP-binding status to gate

**Nucleotide-binding domain 1 (NBD1; aa 389-672):**
- ABC superfamily fold; two subdomains (RecA-like ATPase core + ABC-specific α-helical subdomain)
- Walker A (P-loop; K464), Walker B (D572), ABC signature motif (LSGGQ); binds one ATP molecule
- **F508del (Phe508del)**: deletion of Phe508 from a surface-exposed loop in NBD1 → loss of three hydrophobic contacts with TMD1 intracellular loops → NBD1-TMD1 interface destabilization → global misfolding → ER retention and ERAD (ER-associated degradation)
- NBD1 crystal structures: first solved with suppressor mutations (F508C, I539T, R555K); native F508del NBD1 is structurally very similar to WT but the interdomain interface is disrupted

**Regulatory (R) domain (aa 590-830):**
- Intrinsically disordered; unique to CFTR (absent in other ABC transporters)
- Contains ~10 PKA phosphorylation sites (S660, S700, S712, S737, S768, S795, S813 are functional); phosphorylation by PKA (cAMP → adenylyl cyclase → PKA) is required for CFTR channel activity — unphosphorylated R domain inhibits gating; phosphorylated R domain relieves autoinhibition
- PKC phosphorylation (S686, T682) provides baseline activation
- R domain disordered region acts as a "switch": unphosphorylated R domain occludes NBD1-NBD2 dimerization; phosphorylated R domain moves away → allows NBD dimer to form → ATP-dependent gating

**Nucleotide-binding domain 2 (NBD2; aa 1,210-1,480):**
- Second ABC ATPase domain; Walker A/B + signature motif; binds second ATP
- **Asymmetric NBD dimer**: NBD1-NBD2 heterodimerization creates two composite ATP-binding sites; Site 1 (NBD1-Walker A/B + NBD2 LSGGQ): degenerate site — binds ATP but hydrolyzes slowly; Site 2 (NBD2-Walker A/B + NBD1 LSGGQ): active hydrolysis site — ATP hydrolysis at Site 2 drives channel closure
- Channel gating cycle: phosphorylated R domain + ATP binding at both sites → NBD dimer forms → channel opens; ATP hydrolysis at Site 2 → NBD dimer separates → channel closes

**Transmembrane domain 2 (TMD2; aa 830-1,202):**
- Six transmembrane helices (TM7-12); forms the other half of the channel pore; TM12 contains key pore residues; forms coupled structure with TMD1 for Cl⁻ conduction

### CFTR as a chloride channel — biophysics

**Ion selectivity:**
- Cl⁻ >> HCO₃⁻ >> F⁻; minimal cation permeability; selectivity maintained by positively charged pore residues (R334, K95)
- Relative permeability: PCl:PHCO3 ~4:1 (important for airway surface liquid pH)
- Conductance: ~8-10 pS (picosiemens) in whole-cell; CFTR opens in bursts with intrabursts of millisecond closures

**Regulation by cAMP:**
- β-adrenergic receptor → Gs → adenylyl cyclase → cAMP → PKA → R domain phosphorylation → CFTR activation
- In airway: β-agonists (albuterol, salmeterol) transiently potentiate CFTR activity; ivacaftor potentiates gating independent of cAMP

## Function

### CFTR in airway epithelium

**Airway surface liquid (ASL) homeostasis:**
- Normal airway: CFTR apical Cl⁻ secretion (lumen-directed) drives water secretion → low-viscosity periciliary liquid layer (PCL; ~7 µm thick) and mucus gel layer (~70 µm)
- Coupled with ENaC (epithelial Na⁺ channel): ENaC absorbs Na⁺ (lumen → cell); CFTR-mediated Cl⁻ secretion counterbalances Na⁺ absorption to maintain PCL volume
- CFTR LOF → no Cl⁻ secretion → Na⁺ and water reabsorbed via ENaC unopposed → dehydrated, thickened mucus → impaired mucociliary clearance → mucus plugging → airway obstruction
- CFTR also secretes HCO₃⁻ → maintains airway pH ~6.6; in CF: acidic ASL → impaired bactericidal activity of secretory IgA and defensins → pathogen colonization

**Mucociliary clearance failure in CF:**
- Thickened dehydrated mucus adheres to airway epithelium → ciliary beating impaired → mucus not cleared
- Stagnant mucus → anaerobic niche → Pseudomonas aeruginosa colonization (first in 40-50% of CF patients by age 20 in pre-modulator era)
- Pseudomonas adopts biofilm phenotype in CF mucus → antibiotic tolerance → chronic infection → inflammatory vicious cycle

### CFTR in pancreas

**Pancreatic duct fluid secretion:**
- Ductal epithelial CFTR secretes HCO₃⁻ into duct lumen (driven by AE2/pendrin SLC26A6 exchange) → alkaline duct fluid pH ~8.0-8.2 → maintains trypsinogen in inactive form and flushes secreted enzymes into duodenum
- CFTR LOF → low-volume, acidic duct fluid → protein precipitates in duct → obstruction → acinar cell autolysis → pancreatitis (same mechanism as PRSS1 disease, but via ductal rather than acinar mechanism)
- CF pancreatic insufficiency (~85% of CF patients): exocrine pancreatic destruction → steatorrhea, fat-soluble vitamin deficiency → requires pancreatic enzyme replacement therapy (Creon/Zenpep)
- CF-related diabetes (CFRD): insulin deficiency from β-cell destruction (not classic T1DM or T2DM); treated with insulin (not oral agents); distinct insulin resistance pattern

### CFTR in vas deferens

- Almost all males with CF have **congenital bilateral absence of the vas deferens (CBAVD)**: vas deferens requires functional CFTR for development → obstructive azoospermia → infertility
- CBAVD without classic CF lung/pancreatic disease: caused by mild CFTR mutations (e.g., R117H in combination with poly-T tract variants); isolated CBAVD testing should include CFTR genotyping
- Fertility options: testicular sperm extraction (TESE) + ICSI (intracytoplasmic sperm injection) — highly effective; CF partner carrier testing required before conception

## Mechanism

### CFTR modulator pharmacology

**Potentiators (ivacaftor, VX-770):**
- Mechanism: bind to a hydrophobic transmembrane site (TM4, TM6, TM11 region) → stabilize open-channel conformation → increase channel open probability (Po) from ~0.1 to ~0.5 in G551D; channel is at cell surface but gating is defective in Class III mutations
- **Ivacaftor (Kalydeco)**: FDA-approved 2012 for G551D (first modulator); transformed outcomes for ~5% of CF population with gating mutations; sweat Cl⁻ ↓ ~50 mmol/L; ppFEV1 ↑ ~10-12 pp
- F508del: CFTR is absent from the surface (Class II), so ivacaftor alone is ineffective without a corrector

**Correctors (lumacaftor, tezacaftor, elexacaftor, VX-809, VX-661, VX-445):**
- Mechanism: bind to CFTR domains to stabilize F508del misfolded intermediates during biosynthesis → reduce ER retention → more CFTR reaches cell surface; elexacaftor (VX-445) binds NBD1-TMD1 interface (where F508del disrupts the fold) most effectively
- Generation 1: lumacaftor (VX-809) → modest F508del surface correction alone (~15%); lumacaftor + ivacaftor (Orkambi) — modest benefit (ppFEV1 ↑ ~3 pp) but drug-drug interaction (lumacaftor induces CYP3A → reduces ivacaftor levels)
- Generation 2: tezacaftor (VX-661) — improved corrector; tezacaftor + ivacaftor (Symdeko) — ppFEV1 ↑ ~4 pp
- Generation 3 (triple combination): **elexacaftor + tezacaftor + ivacaftor (Trikafta, ETD)**:
  - Elexacaftor acts at a different corrector site than tezacaftor → additive effect on F508del surface expression
  - ppFEV1 ↑ ~14 percentage points vs. placebo (Heijerman 2019) [^heijerman-2019-etd-cf]; sweat Cl⁻ ↓ ~41 mmol/L; BMI ↑; exacerbations ↓ ~63%
  - Eligible for F508del homozygotes (~45% of CF patients) and F508del heterozygotes with one responsive mutation (~90% total CF patients eligible)
  - Transforms CF from a progressive fatal disease to a manageable chronic condition; lung transplant rates have declined

**Nonsense suppression (ataluren, ELX-02):**
- Class I mutations (premature stops → no protein) → ataluren promotes ribosomal read-through of UGA stops → some full-length CFTR produced
- Ataluren approved in some EU countries for CF with nonsense mutations; modest benefit; trial failures in US (FDA not approved)
- ELX-02 (an aminoglycoside analog) in trials for G542X

**ASL hydrators (hypertonic saline, mannitol):**
- Not modulators; work independently of CFTR genotype by osmotically drawing water onto the airway surface → thin mucus → improve mucociliary clearance
- 7% hypertonic saline (inhaled): standard CF airway therapy; ppFEV1 modest improvement (~3 pp); reduces exacerbations ~56%
- Mannitol (Bronchitol): dry powder inhaled osmotic; reduces exacerbations

**F508del protein stability:**
- Even with ETD correcting F508del to the surface, the protein remains thermally unstable (partially unfolded at body temperature) → shorter half-life on the surface (~16 h vs. ~24 h for WT)
- Pharmacological chaperones and combination correctors (next-generation) aim to further stabilize F508del on the surface for longer duration channel activity

## Connections

- `connects-to` → **[Cystic Fibrosis](../../07-system/cystic-fibrosis/README.md)** — Biallelic CFTR LOF → cystic fibrosis; F508del is the most common CF allele (~70% worldwide); CFTR class I-VI mutations differ in whether protein is absent, misfolded, or dysfunctional; elexacaftor/tezacaftor/ivacaftor (Trikafta) transformed CF prognosis for F508del patients.
- `connects-to` → **[PRSS1](../../03-molecular/prss1/README.md)** — CFTR mutations act as disease modifiers in hereditary pancreatitis: CFTR LOF → reduced pancreatic duct bicarbonate → acidic duct fluid → enhanced trypsinogen activation → pancreatitis risk; compound heterozygosity with PRSS1 or SPINK1 mutations worsens disease severity.
- `connects-to` → **[TGF-β](../../03-molecular/tgf-beta/README.md)** — TGF-β1 is a major modifier of CF lung disease severity: TGF-β1 promoter polymorphisms (codon 10/25) correlate with lung function decline in CF; airway TGF-β1 signaling promotes fibrosis and reduces CFTR modulator efficacy; TGF-β1 blockade is explored as CF adjunct therapy.
- `connects-to` → **[NLRP3 Inflammasome](../../03-molecular/nlrp3-inflammasome/README.md)** — NLRP3 inflammasome is constitutively activated in CF airway: CFTR LOF → abnormal mitochondrial reactive oxygen species → NLRP3 priming and activation → IL-1β/IL-18 release → neutrophilic airway inflammation; IL-1β inhibitors (canakinumab) explored in CF lung disease.
- `connects-to` → **[Pancreatic Cancer](../../07-system/pancreatic-cancer/README.md)** — Chronic pancreatitis from CFTR LOF → exocrine destruction → pancreatic insufficiency in ~85% of CF patients; CFTR mutations are independent risk modifiers for sporadic PDAC; CFTR LOF → reduced pancreatic duct HCO₃⁻ → acidic fluid → trypsinogen activation → acinar damage.
- `connects-to` → **[NF-κB](../../03-molecular/nf-kb/README.md)** — CFTR LOF → unresolved Pseudomonas biofilm → NF-κB activation → IL-8/CXCL8/GM-CSF → neutrophilic inflammation; NF-κB is constitutively activated in CF epithelia even without active infection; Trikafta therapy reduces NF-κB-driven airway cytokine levels.
- `connects-to` → **[TNF-α](../../03-molecular/tnf-alpha/README.md)** — TNF-α is chronically elevated in CF airway fluid and sputum; CFTR LOF → NF-κB hyperactivation → TNF-α/IL-1β → self-perpetuating inflammatory cycle; TNF-α-driven neutrophil elastase destroys airway structure; anti-TNF strategies have not demonstrated clinical benefit in CF trials.

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*

[^riordan-1989-cftr-cloning]: Riordan JR, Rommens JM, Kerem B, et al. Identification of the cystic fibrosis gene: cloning and characterization of complementary DNA. *Science.* 1989;245(4922):1066-1073. [doi:10.1126/science.2475911](https://doi.org/10.1126/science.2475911) · [PubMed 2475911](https://pubmed.ncbi.nlm.nih.gov/2475911/)
[^heijerman-2019-etd-cf]: Heijerman HGM, McKone EF, Downey DG, et al. Efficacy and safety of the elexacaftor plus tezacaftor plus ivacaftor combination regimen in people with cystic fibrosis homozygous for the F508del mutation. *Lancet.* 2019;394(10212):1940-1948. [doi:10.1016/S0140-6736(19)32597-8](https://doi.org/10.1016/S0140-6736(19)32597-8) · [PubMed 31679946](https://pubmed.ncbi.nlm.nih.gov/31679946/)
