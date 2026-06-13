---
schema: human-scale-entry/v1
id: hepatitis-c
name: Hepatitis C
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-08
summary: "HCV (Hepacivirus; positive-sense ssRNA; genotypes 1-6) infects 58M people globally; NS3/4A cleaves MAVS → IRF3 not activated → chronicity in 80%; direct-acting antivirals (SOF/VEL, GLE/PIB) achieve >95% cure; cirrhosis → HCC risk 1-5%/year; no vaccine exists."
aliases: ["HCV", "hepatitis C virus", "chronic hepatitis C", "HCV cirrhosis", "HCV RNA", "NS3/4A", "sofosbuvir", "DAA", "direct-acting antiviral", "Epclusa", "Mavyret", "HCV genotype", "Hepacivirus"]
sources:
  - id: li-2005-hcv-mavs-cleavage
    type: peer-reviewed
    cite: "Li XD, Sun L, Seth RB, Pineda G, Chen ZJ. Hepatitis C virus protease NS3/4A cleaves mitochondrial antiviral signaling protein off the mitochondria to evade innate immunity. Proc Natl Acad Sci USA. 2005;102(49):17717-17722."
    doi: "10.1073/pnas.0508531102"
    pmid: "16301520"
    url: "https://doi.org/10.1073/pnas.0508531102"
    accessed: "2026-06-08"
  - id: ghany-2019-hcv-treatment
    type: peer-reviewed
    cite: "Ghany MG, Morgan TR; AASLD-IDSA HCV Guidance Panel. Hepatitis C Guidance 2019 Update: AASLD-IDSA Recommendations for Testing, Managing, and Treating Hepatitis C Virus Infection. Hepatology. 2020;71(2):686-721."
    doi: "10.1002/hep.31060"
    pmid: "31816268"
    url: "https://doi.org/10.1002/hep.31060"
    accessed: "2026-06-08"
cross_links:
  - target: 01-human/03-molecular/mavs
    relation: connects-to
    note: "HCV NS3/4A cleaves MAVS at Cys508 → soluble cytoplasmic MAVS cannot activate TBK1/IRF3 → no IFN-β; NS3/4A also cleaves TRIF → TLR3 signaling blocked; dual evasion of cytosolic and endosomal RNA sensing; MAVS cleavage is the primary reason HCV establishes chronicity."
  - target: 01-human/03-molecular/irf3
    relation: connects-to
    note: "HCV NS3/4A cleaves MAVS → TBK1-IRF3 not activated; NS5A additionally blocks TBK1 → IRF3 not phosphorylated; selective IRF3 inactivation while NF-κB persists → pro-survival hepatocyte signals; IRF3 pathway suppression is the key mechanism driving HCV chronicity."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "HCV evades type I IFN: NS3/4A blocks MAVS → no IFN-β; NS5A blocks PKR; high baseline ISG expression (ISG15, MX1 maximally induced by low-grade IFN) predicts pegIFN-α failure; DAAs bypass IFN-dependent antiviral mechanisms and achieve >95% cure regardless of IFN sensitivity."
  - target: 01-human/03-molecular/stat1
    relation: connects-to
    note: "Chronic HCV drives ISG pre-activation via low-grade IFN-α → STAT1/STAT2/ISGF3 saturated → pegIFN-α fails to induce additional antiviral ISGs; IL28B TT genotype = high baseline ISG expression → pegIFN non-response; DAAs achieve SVR regardless of STAT1/ISG baseline."
  - target: 01-human/07-system/hcc
    relation: connects-to
    note: "HCV cirrhosis → HCC incidence 1-5%/year (surveillance required); chronic HCV inflammation → NF-κB/STAT3 → hepatocyte proliferation under oxidative DNA damage → driver mutations (TP53, TERT, CTNNB1); DAA cure reduces HCC risk ~70% but established cirrhosis retains HCC risk."
  - target: 02-pathogen/01-viruses/hepatitis-c-virus
    relation: connects-to
    note: "Hepatitis C virus is a positive-sense RNA flavivirus whose NS3/4A protease cleaves MAVS to silence interferon, persisting in ~80% of those infected; unlike HBV it makes no nuclear reservoir, so direct-acting antivirals cure >95% — yet no vaccine exists."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "Chronic hepatitis C smolders in the liver, activating stellate cells via TGF-β and driving fibrosis to cirrhosis; DAA cure (SVR) cuts hepatocellular carcinoma risk ~70% but established cirrhosis still needs surveillance, and FibroScan has largely replaced biopsy for staging."
  - target: 01-human/04-cellular/b-cell
    relation: connects-to
    note: "HCV chronically stimulates B cells by binding CD81, driving type II mixed cryoglobulinemia (purpura, vasculitis, MPGN, neuropathy) and a raised risk of marginal-zone and other B-cell lymphomas; antiviral cure resolves cryoglobulinemia in ~80%."
  - target: 01-human/07-system/hepatitis-b
    relation: connects-to
    note: "HCV and HBV both cause chronic hepatitis → cirrhosis → HCC yet differ: HCV is an RNA flavivirus with no latent reservoir, cured >95% by DAAs, and has no vaccine; HBV is a DNA virus whose nuclear cccDNA reservoir antivirals suppress but cannot clear, and is vaccine-preventable."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "Chronic HCV activates hepatic stellate cells via TGF-β1 → myofibroblast transdifferentiation → collagen I/III deposition → progressive fibrosis (METAVIR F0–F4) → cirrhosis; DAA-induced SVR slows fibrogenesis but established cirrhosis persists, retaining HCC risk."
  - target: 01-human/07-system/type-2-diabetes
    relation: connects-to
    note: "HCV is metabolically active: the core protein degrades IRS-1/IRS-2 via PI3K/mTOR and SOCS3 → hepatic insulin resistance → type 2 diabetes (2–3× risk), which in turn accelerates fibrosis and HCC; DAA-induced SVR improves glycemic control and lowers incident diabetes."
  - target: 01-human/07-system/hiv-aids
    relation: connects-to
    note: "HCV and HIV commonly coinfect through shared blood-borne spread: HIV accelerates HCV liver fibrosis and cirrhosis, so coinfected patients are prioritized for direct-acting antiviral cure, which now clears HCV in most regardless of HIV status."
  - target: 01-human/07-system/follicular-lymphoma
    relation: connects-to
    note: "Chronic hepatitis C drives B-cell non-Hodgkin lymphomas including follicular and marginal-zone types: persistent antigen stimulation expands clonal B cells (also causing mixed cryoglobulinemia), and antiviral cure can make some HCV-associated lymphomas regress."
  - target: 01-human/04-cellular/hepatocyte
    relation: connects-to
    note: "Hepatitis C replicates in hepatocytes and rewires their lipid metabolism: the virus assembles on lipid droplets and uses hepatocyte lipoproteins, causing steatosis and insulin resistance—injuring the liver cell metabolically as well as by immune inflammation."
---

# Hepatitis C

## Overview

**Hepatitis C** is a chronic liver disease caused by the **hepatitis C virus (HCV)** — a positive-sense single-stranded RNA virus of the family *Flaviviridae* (genus *Hepacivirus*). With an estimated **58 million people chronically infected** globally and ~1.5 million new infections per year (WHO), HCV remains a major cause of liver-related morbidity and mortality despite the existence of curative therapy. The virus causes chronic infection in approximately 80% of acutely infected individuals, eventually leading to liver fibrosis, cirrhosis, and hepatocellular carcinoma (HCC) in a significant proportion.

The defining feature of HCV biology is its extraordinary capacity for **innate immune evasion**: the HCV NS3/4A serine protease cleaves MAVS from the outer mitochondrial membrane [^li-2005-hcv-mavs-cleavage], selectively disabling the TBK1-IRF3-IFN-β axis while leaving NF-κB-driven pro-survival signaling intact. This molecular strategy underlies the virus's ability to establish lifelong infection in a fully immunocompetent host.

The discovery of **direct-acting antivirals (DAAs)** — agents targeting HCV-specific NS3/4A, NS5A, and NS5B — transformed HCV from an incurable chronic disease into one with >95% cure rates with 8–12 weeks of oral therapy [^ghany-2019-hcv-treatment]. This transformation represents one of the most dramatic successes in antiviral drug development, though global elimination targets remain constrained by diagnosis and access gaps.

**Epidemiology:**
- 58 million chronic infections worldwide; 290,000 HCV-attributable deaths/year
- Highest prevalence: Egypt (15%+, historical iatrogenic), Pakistan, Central Asia, East/North Africa, injection drug use populations globally
- Genotypes 1–6: GT1a/1b (North America, Europe — historically hardest to treat with IFN), GT2/3 (global), GT4 (Middle East, Africa), GT5/6 (South Africa, Southeast Asia)
- Modes of transmission: Blood-to-blood (injection drug use — dominant in high-income countries; unsafe healthcare injections — dominant globally); sexual transmission (low risk except HIV co-infection or rectal mucosa exposure); perinatal transmission (~5%)

## Structure

### HCV biology

HCV is an enveloped virus (~55-65 nm diameter) with a **9.6 kb positive-sense ssRNA genome** encoding a single polyprotein (~3,000 aa) cleaved by host and viral proteases:

| Protein | Type | Function |
|---------|------|----------|
| Core (C) | Structural | Nucleocapsid assembly; promotes lipid droplet association; suppresses apoptosis |
| E1, E2 | Structural | Envelope glycoproteins; E2 binds CD81 receptor; target of neutralizing antibodies; hypervariable region 1 (HVR1) of E2 mutates rapidly → immune evasion |
| p7 | Viroporin | Ion channel; facilitates virion maturation and release |
| NS2 | Non-structural | Cysteine protease; cleaves NS2-NS3 junction |
| NS3 | Non-structural | N-terminal serine protease (cleaves NS3-NS5B region with NS4A cofactor); C-terminal NTPase/helicase; target of protease inhibitors (glecaprevir, voxilaprevir, grazoprevir) |
| NS4A | Non-structural | NS3 protease cofactor and membrane anchor |
| NS4B | Non-structural | Induces ER-derived membranous web (replication organelle) |
| NS5A | Non-structural | RNA binding; replication complex assembly; IFN resistance; target of NS5A inhibitors (velpatasvir, pibrentasvir, daclatasvir) |
| NS5B | Non-structural | RNA-dependent RNA polymerase (RdRp); target of NS5B inhibitors (sofosbuvir, dasabuvir) |

### HCV entry

1. **CD81 binding**: HCV E2 hypervariable region binds tetraspanin **CD81** on hepatocytes (primary receptor); also binds SR-BI (scavenger receptor class B type I)
2. **Tight junction proteins**: Claudin-1 and occludin at hepatocyte tight junctions are essential co-receptors
3. **Endocytosis**: Clathrin-mediated → endosomal acidification → E1/E2 fusion → RNA release into cytoplasm
4. **Replication**: NS4B-induced **membranous web** (ER-derived replication compartment) → NS5B RdRp synthesizes negative-sense antigenome → new positive-sense genomes
5. **Assembly/release**: Core associates with lipid droplets → nucleocapsid assembled; virions bud into ER → trans-Golgi → secretion with VLDL pathway (lipoprotein association)

## Function

### Innate immune evasion (multi-layered)

HCV suppresses innate immunity at multiple nodes:

| Target | HCV protein | Mechanism |
|--------|------------|-----------|
| MAVS (TLR3-TRIF adaptor also) | NS3/4A protease | Cleavage of MAVS at Cys508 → releases MAVS from OMM; cleavage of TRIF at Cys372 → disrupts TLR3 → IRF3 |
| TBK1/IRF3 | NS5A | Binds TBK1 → blocks IRF3 phosphorylation; mechanism of ISG pre-activation without IFN-β induction |
| PKR | NS5A, E2 | Blocks PKR-mediated eIF2α phosphorylation → maintains hepatocyte translation despite dsRNA |
| JAK-STAT | NS5A, core | Blocks STAT1 phosphorylation; core protein activates SOCS3 → suppresses JAK-STAT |
| Apoptosis | Core, NS5A | Core activates Wnt/β-catenin; NS5A inhibits Bax-mediated apoptosis → hepatocyte survival despite viral damage |

The **net immunological state** in chronic HCV: low-grade IFN-α (from pDC sensing of circulating virus) drives baseline ISG expression (ISG15, MX1, OAS1) without IFN-β; NF-κB-driven inflammatory signals promote hepatocyte survival; T cell exhaustion (Tim-3, PD-1 upregulation) prevents viral clearance.

### IL28B/IFNL3 genetics

Polymorphisms near the *IL28B* gene (encoding IFN-λ3) predict spontaneous clearance and pegIFN/ribavirin response:
- **CC genotype** (rs12979860): ~45% spontaneous clearance; ~80% sustained virological response (SVR) with pegIFN/ribavirin (GT1)
- **TT genotype**: <15% spontaneous clearance; ~30-40% SVR; high baseline ISG expression (ISG15, OAS1) due to constitutive IFN-λ signaling → ISGF3 pathway already "exhausted" → pegIFN cannot induce additional response
- IL28B genotype is irrelevant for DAA therapy (>95% SVR regardless of genotype)

## Pathology

### Hepatic fibrosis and cirrhosis

Chronic HCV → portal triad inflammation → hepatic stellate cell (HSC) activation → TGF-β → collagen deposition → fibrosis (F0-F4 by METAVIR); cirrhosis (F4) develops in ~20% of patients after 20 years; accelerated by alcohol, HIV co-infection, male sex, age of infection acquisition.

**Assessment:** FibroScan (liver stiffness by transient elastography) has largely replaced liver biopsy; APRI and FIB-4 scores as non-invasive surrogate markers.

### Hepatocellular carcinoma (HCC)

HCV cirrhosis → HCC risk 1–5% per year (annual ultrasound surveillance ± AFP required):
- **Mechanism**: Chronic inflammation → NF-κB → compensatory hepatocyte proliferation under oxidative DNA damage → driver mutations (TP53, CTNNB1 — β-catenin, TERT promoter); HCV Core directly activates Wnt/β-catenin
- DAA-achieved SVR reduces HCC risk by ~70% but does not eliminate it — established cirrhosis retains surveillance requirement

### Extrahepatic manifestations

- **Type II cryoglobulinemia**: HCV binds CD81 on B cells → polyclonal → then monoclonal RF-producing B cell expansion → IgM RF + polyclonal IgG immune complexes → cryoprecipitate at low temperatures → vasculitis, purpura, membranoproliferative glomerulonephritis, peripheral neuropathy; treatment: DAA cure resolves cryoglobulinemia in ~80%
- **Lymphoma**: Chronic HCV B cell stimulation → marginal zone lymphoma, splenic lymphoma, DLBCL; cure rates higher after SVR
- **Insulin resistance / type 2 diabetes**: HCV Core activates IRS-1 degradation via PI3K/mTOR; improves after SVR
- **Thyroid disease**: Thyroiditis (autoimmune); aggravated by IFN-α treatment

### Diagnosis

- **Anti-HCV antibody** (ELISA): Screening; positive from ~6 weeks post-infection; persists after cure (not a marker of active infection)
- **HCV RNA (RT-PCR)**: Quantitative viral load (IU/mL); confirms active infection; used for treatment monitoring (week 4, end of treatment, 12 weeks post-treatment SVR12)
- **Genotype**: HCV genotyping assay (NS5B sequencing or line probe); important for some regimens but irrelevant for pan-genotypic DAAs
- **HCV core antigen**: Less sensitive than RNA PCR but simpler; useful in resource-limited settings

### Treatment

**Direct-acting antivirals (DAAs):**

| Regimen | Targets | Genotypes | Duration | SVR12 |
|---------|---------|-----------|----------|-------|
| SOF/VEL (Epclusa) | NS5B + NS5A | Pan-genotypic (GT1-6) | 12 weeks | >97% |
| GLE/PIB (Mavyret) | NS3/4A + NS5A | Pan-genotypic (GT1-6) | 8 weeks | >97% |
| LDV/SOF (Harvoni) | NS5A + NS5B | GT1/4/5/6 | 8–12 weeks | >94% |
| GZR/EBR (Zepatier) | NS3/4A + NS5A | GT1/4 | 12 weeks | >92% |

- **SVR12** (undetectable HCV RNA 12 weeks after end of treatment) = cure; durable in >99% of cases
- **Decompensated cirrhosis**: SOF/VEL ± ribavirin (GLE/PIB contraindicated)
- **DAA resistance**: NS5A resistance-associated substitutions (RASs) can reduce efficacy; voxilaprevir overcomes most NS5B/NS5A RASs
- **Monitoring**: LFT, CBC, renal function (sofosbuvir — dose adjust if eGFR <30 for certain regimens)
- **Drug interactions**: Rifampicin, carbamazepine, proton pump inhibitors (reduce ledipasvir absorption), amiodarone + sofosbuvir (bradycardia)

**No HCV vaccine exists** — high genetic diversity of E1/E2 hypervariable regions prevents broadly effective vaccine development; this remains a major gap in WHO elimination strategy.

### Prevention

- Harm reduction (needle exchange, opioid substitution therapy)
- Universal blood product screening (eliminated transfusion-acquired HCV in high-income settings)
- Healthcare injection safety (primary driver of HCV in low/middle-income settings)
- Treatment as prevention: DAA cure eliminates onward transmission

## Connections

**→ [MAVS](../../../03-molecular/mavs/)**: HCV NS3/4A serine protease cleaves MAVS at Cys508 → releases MAVS from outer mitochondrial membrane → soluble cytoplasmic MAVS cannot activate TBK1/IRF3 → no IFN-β → viral persistence; TRIF (TLR3 adaptor) is also cleaved by NS3/4A → dual evasion of endosomal and cytosolic RNA sensing.

**→ [IRF3](../../../03-molecular/irf3/)**: HCV NS3/4A cleaves MAVS upstream of TBK1-IRF3; NS5A additionally blocks TBK1 activity → IRF3 not phosphorylated → IFN-β not transcribed; selective IRF3 inactivation while NF-κB persists → pro-survival hepatocyte signaling; IRF3 pathway suppression is the key mechanism of HCV chronicity.

**→ [Type I Interferon](../../../03-molecular/type-i-interferon/)**: HCV evades type I IFN at multiple levels: NS3/4A blocks MAVS → no IFN-β induction; NS5A and NS5B block PKR and OAS; high baseline ISG expression (from chronic low-grade IFN) predicts pegIFN-α treatment failure (ISG15, MX1 already maximally induced); DAAs replaced IFN-based therapy.

**→ [STAT1](../../../03-molecular/stat1/)**: Chronic HCV establishes a state of ISG pre-activation via low-grade IFN-α: baseline STAT1/STAT2 signaling saturates the ISGF3 pathway → pegIFN-α/ribavirin fails to induce additional antiviral ISGs; elevated pretreatment ISG expression (IL28B genotype CC) predicts pegIFN non-response; DAA therapy bypasses STAT1-dependent IFN resistance.

**→ [HCC](../hcc/)**: HCV cirrhosis → HCC incidence 1-5% per year; HCV-driven HCC: chronic inflammation → NF-κB, TGF-β, IL-6/STAT3 → hepatocyte regeneration under oxidative stress → driver mutations; DAA cure reduces HCC risk by ~70% but does not eliminate it in established cirrhosis — surveillance continues.

- `connects-to` → **[Hepatitis C Virus](../../../02-pathogen/01-viruses/hepatitis-c-virus/README.md)** — Hepatitis C virus is a positive-sense RNA flavivirus whose NS3/4A protease cleaves MAVS to silence interferon, persisting in ~80% of those infected; unlike HBV it makes no nuclear reservoir, so direct-acting antivirals cure >95% — yet no vaccine exists.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — Chronic hepatitis C smolders in the liver, activating stellate cells via TGF-β and driving fibrosis to cirrhosis; DAA cure (SVR) cuts hepatocellular carcinoma risk ~70% but established cirrhosis still needs surveillance, and FibroScan has largely replaced biopsy for staging.
- `connects-to` → **[B Cell](../../04-cellular/b-cell/README.md)** — HCV chronically stimulates B cells by binding CD81, driving type II mixed cryoglobulinemia (purpura, vasculitis, MPGN, neuropathy) and a raised risk of marginal-zone and other B-cell lymphomas; antiviral cure resolves cryoglobulinemia in ~80%.
- `connects-to` → **[Hepatitis B](../hepatitis-b/README.md)** — HCV and HBV both cause chronic hepatitis → cirrhosis → HCC yet differ: HCV is an RNA flavivirus with no latent reservoir, cured >95% by DAAs, and has no vaccine; HBV is a DNA virus whose nuclear cccDNA reservoir antivirals suppress but cannot clear, and is vaccine-preventable.
- `connects-to` → **[Transforming Growth Factor Beta](../../03-molecular/tgf-beta/README.md)** — Chronic HCV activates hepatic stellate cells via TGF-β1 → myofibroblast transdifferentiation → collagen I/III deposition → progressive fibrosis (METAVIR F0–F4) → cirrhosis; DAA-induced SVR slows fibrogenesis but established cirrhosis persists, retaining HCC risk.
- `connects-to` → **[Type 2 Diabetes](../type-2-diabetes/README.md)** — HCV is metabolically active: the core protein degrades IRS-1/IRS-2 via PI3K/mTOR and SOCS3 → hepatic insulin resistance → type 2 diabetes (2–3× risk), which in turn accelerates fibrosis and HCC; DAA-induced SVR improves glycemic control and lowers incident diabetes.
- `connects-to` → **[HIV/AIDS](../hiv-aids/README.md)** — HCV and HIV commonly coinfect through shared blood-borne spread: HIV accelerates HCV liver fibrosis and cirrhosis, so coinfected patients are prioritized for direct-acting antiviral cure, which now clears HCV in most regardless of HIV status.
- `connects-to` → **[Follicular Lymphoma](../follicular-lymphoma/README.md)** — Chronic hepatitis C drives B-cell non-Hodgkin lymphomas including follicular and marginal-zone types: persistent antigen stimulation expands clonal B cells (also causing mixed cryoglobulinemia), and antiviral cure can make some HCV-associated lymphomas regress.
- `connects-to` → **[Hepatocyte](../../04-cellular/hepatocyte/README.md)** — Hepatitis C replicates in hepatocytes and rewires their lipid metabolism: the virus assembles on lipid droplets and uses hepatocyte lipoproteins, causing steatosis and insulin resistance—injuring the liver cell metabolically as well as by immune inflammation.
