---
schema: pathogen-entry/v1
id: salmonella-typhi
name: Salmonella typhi
atlas: 02-pathogen
scale: 02-bacteria
status: draft
last_reviewed: 2026-06-05
summary: "Gram-negative rod (Enterobacteriaceae); strictly human host. Vi capsule virulence. SPI-1 T3SS for M-cell invasion; SPI-2 T3SS for intracellular survival in macrophages. Causes typhoid fever: 11-21 million cases/year. Ty21a and Typbar-TCV vaccines available."
aliases: ["S. Typhi", "typhoid bacillus", "enteric fever agent", "Salmonella enterica serovar Typhi", "typhoid fever"]
sources:
  - id: mandell-principles
    type: textbook
    cite: "Bennett JE, Dolin R, Blaser MJ. Mandell, Douglas, and Bennett's Principles and Practice of Infectious Diseases. 9th ed. Elsevier; 2020."
    url: "https://www.elsevier.com/books/mandell-douglas-and-bennetts-principles-and-practice-of-infectious-diseases/bennett/978-0-323-48255-4"
    accessed: "2026-06-05"
  - id: murray-microbiology
    type: textbook
    cite: "Murray PR, Rosenthal KS, Pfaller MA. Medical Microbiology. 9th ed. Elsevier; 2021."
    url: "https://www.elsevier.com/books/medical-microbiology/murray/978-0-323-67378-4"
    accessed: "2026-06-05"
  - id: parry-2002-typhoid-review
    type: peer-reviewed
    cite: "Parry CM, Hien TT, Dougan G, White NJ, Farrar JJ. Typhoid fever. N Engl J Med. 2002;347(22):1770-82."
    doi: "10.1056/NEJMra020201"
    pmid: "12456854"
    url: "https://doi.org/10.1056/NEJMra020201"
  - id: crump-2019-typhoid-burden
    type: peer-reviewed
    cite: "Crump JA. Progress in Typhoid Fever Epidemiology. Clin Infect Dis. 2019;68(Suppl 1):S4-S9."
    doi: "10.1093/cid/ciy846"
    pmid: "30767000"
    url: "https://doi.org/10.1093/cid/ciy846"
  - id: galan-1994-spi1-t3ss
    type: peer-reviewed
    cite: "Galan JE, Curtiss R 3rd. Cloning and molecular characterization of genes whose products allow Salmonella typhimurium to penetrate tissue culture cells. Proc Natl Acad Sci USA. 1989;86(16):6383-7."
    doi: "10.1073/pnas.86.16.6383"
    pmid: "2548212"
    url: "https://doi.org/10.1073/pnas.86.16.6383"
  - id: who-typhoid-2018
    type: regulatory
    cite: "World Health Organization. Typhoid vaccines: WHO position paper, March 2018. Wkly Epidemiol Rec. 2018;93(13):153-172."
    url: "https://www.who.int/publications/i/item/who-wer9313"
    accessed: "2026-06-05"
cross_links:
  - target: 01-human/07-system/digestive-system
    relation: damages
    note: "S. Typhi causes Peyer-patch hyperplasia, ileal mucosal necrosis, and intestinal perforation (0.8-3% of cases) — a life-threatening complication requiring emergency surgery and carrying ~25% mortality."
  - target: 01-human/06-organ/small-intestine
    relation: infects
    note: "S. Typhi invades ileal M cells via SPI-1 T3SS effectors (SopB, SopE, SipA) that trigger actin rearrangement and bacterial uptake; M cells deliver the pathogen to subepithelial lymphoid tissue for systemic spread."
  - target: 01-human/04-cellular/macrophage
    relation: damages
    note: "SPI-2 T3SS prevents phagosome-lysosome fusion within the Salmonella-containing vacuole (SCV), enabling intracellular survival in macrophages and hematogenous dissemination to liver, spleen, and bone marrow."
  - target: 01-human/06-organ/liver
    relation: damages
    note: "S. Typhi disseminates to liver (hepatomegaly, elevated LFTs, rare fulminant hepatitis) and spleen (splenomegaly, rupture risk) — systemic macrophage foci sustain bacteremia and prolong the febrile illness."
---

# Salmonella typhi

## Overview

*Salmonella enterica* serovar Typhi (*S.* Typhi) is the causative agent of **typhoid fever** (enteric fever) — a systemic febrile illness unique to humans that remains a major global public health burden. Estimated to cause **11–21 million illnesses and 128,000–161,000 deaths annually**, typhoid is concentrated in South Asia (particularly Pakistan, India, Bangladesh), sub-Saharan Africa, and Southeast Asia, where it disproportionately affects children aged 5–15 years in settings with limited access to clean water and sanitation [^crump-2019-typhoid-burden].

Unlike most Salmonella serovars that infect a broad range of animal hosts, *S.* Typhi is an **obligate human pathogen** — its only reservoir is infected or convalescent humans (including asymptomatic carriers). This strict host specificity arises from multiple evolved interactions with human-specific proteins and the presence of the **Vi polysaccharide capsule** (encoded by the *viaB* locus), which enables evasion of human complement and macrophage killing via impaired opsonization.

The disease's defining feature is its **systemic course**: unlike the self-limited gastroenteritis caused by non-typhoidal Salmonella, *S.* Typhi achieves sustained bacteremia by exploiting macrophages as intracellular Trojan horses, disseminating from the intestine to the liver, spleen, bone marrow, and gallbladder. The gallbladder serves as the **chronic carrier reservoir** — approximately 1–4% of patients become long-term carriers after acute infection, intermittently shedding bacteria in stool for years or life (the most famous example: "Typhoid Mary").

The global emergence of **extensively drug-resistant (XDR) typhoid** — strains resistant to chloramphenicol, ampicillin, TMP-SMX, fluoroquinolones, and third-generation cephalosporins — in Pakistan (H58 XDR clade, from 2016) has dramatically complicated treatment and reinvigorated vaccine deployment efforts [^mandell-principles]. The WHO prequalified **Typbar-TCV (Vi-CRM197 conjugate vaccine)** in 2017, and it is now deployed in preventive campaigns across high-burden settings.

## Structure

### Cell Morphology and Microbiological Characteristics

*S.* Typhi is a **Gram-negative, non-spore-forming, facultatively anaerobic rod** in the family Enterobacteriaceae, measuring approximately 2–3 µm × 0.5–0.8 µm.

| Property | Detail |
|:---|:---|
| **Gram reaction** | Negative (outer membrane + thin peptidoglycan) |
| **Motility** | Peritrichous flagella (H antigen: Hd); motile; flagella shed at intracellular stages |
| **Capsule** | Vi polysaccharide (2-*N*-acetyl-4-amino-deoxy-galacturonic acid polymer); key virulence factor; shields LPS O-antigen from antibody and complement; inhibits TLR4 signaling via steric hindrance |
| **O antigen** | Somatic LPS: serogroup D (O9,12); serotyping by Kauffmann-White scheme |
| **H antigen** | Flagellar antigen: d (monophasic — unlike most Salmonella, *S.* Typhi has only one flagellar phase) |
| **Vi antigen** | Capsular antigen; diagnostic target; detected by Widal and Typhidot assays; present in ~90% of clinical isolates |
| **Biochemistry** | Lactose non-fermenter; H₂S negative (unlike *S.* Typhimurium); indole negative; urease negative; citrate negative |

### Genome and Key Virulence Determinants

The *S.* Typhi Ty2 reference genome is **4.8 Mb** with ~4,600 coding sequences, including ~200 pseudogenes — reflecting host restriction and gene decay compared to broad-host-range Salmonella. Key virulence elements:

| Element | Genes | Function |
|:---|:---|:---|
| **SPI-1 (Salmonella Pathogenicity Island 1)** | SopB, SopE, SopE2, SipA, SipC; T3SS structural components | Type III secretion system for intestinal invasion; injects effectors into M cells → actin rearrangement → macropinocytosis-like uptake |
| **SPI-2 (Salmonella Pathogenicity Island 2)** | SseB-F, SifA, SseJ, SsaV T3SS | Second T3SS expressed intracellularly; establishes and maintains the Salmonella-containing vacuole (SCV); prevents phagosome-lysosome fusion |
| **Vi capsule (viaB locus)** | TviA, TviB, TviC, TviD, TviE; VexA-VexE transporters | Vi polysaccharide synthesis and export; inhibits complement opsonization; dampens TLR4/TLR5 recognition of underlying LPS/flagellin |
| **Typhoid toxin** | CdtB (DNase) + PltA (ADP-ribosyltransferase) + PltB (binding) | A₂B₅ toxin secreted from SCV; CdtB induces DNA damage; PltA ADP-ribosylates heterotrimeric Gi proteins; associated with typhoid encephalopathy and chronic carrier state |
| **SPI-7** | Vi biosynthesis + sopD2 + sodd | Additional Vi regulation; SopD2 interferes with Rab7 late endosomal trafficking |

## Infection Mechanism

### Transmission and Infectious Dose

*S.* Typhi is transmitted by the **fecal-oral route** via ingestion of contaminated water or food (particularly water contaminated with sewage, raw produce irrigated with contaminated water, shellfish from polluted waters). Human-to-human transmission requires either contaminated food/water intermediary or rarely direct contact.

- **Infectious dose:** ~10³–10⁵ CFU (low compared to non-typhoidal Salmonella; Vi capsule protects from gastric acid, and *S.* Typhi tolerates acid via multiple acid tolerance response (ATR) systems)
- **Carrier state:** Chronic gallbladder carriers shed 10⁶–10⁹ CFU/g stool intermittently; associated with gallstones (biofilm formation)

### Step-by-Step Invasion

**Phase 1: Intestinal penetration (Days 1–7)**

1. **Gastric transit:** *S.* Typhi survives stomach acid (pH ≥1.5 for brief exposure); induced acid tolerance response (ATR) activates within minutes of acid exposure

2. **Ileal targeting:** Bacteria preferentially adhere to and invade the **M cells overlying Peyer's patches** of the terminal ileum — specialized antigen-sampling epithelial cells with reduced tight junctions and efficient transcytotic capacity [^galan-1994-spi1-t3ss]

3. **SPI-1 T3SS-mediated invasion:** Upon contact with M cell apical membrane:
   - The SPI-1 T3SS needle inserts into the host cell membrane and injects effectors: **SopE** and **SopE2** (guanine nucleotide exchange factors → activate Rac1 and Cdc42 → actin polymerization); **SopB** (phosphoinositide phosphatase → depletes PI(4,5)P₂ → sustains membrane ruffling); **SipA** (stabilizes actin filaments); **SipC** (inserts into membrane, nucleates actin)
   - Result: massive membrane ruffling and macropinocytosis-like **"Salmonella-induced filaments" (SIFs)** leading to bacterial engulfment in a large vacuole

4. **Subepithelial transit:** *S.* Typhi is transported across the M cell and deposited in the subepithelial space, where it is phagocytosed by **resident macrophages and dendritic cells** in the Peyer's patch

**Phase 2: Intracellular survival in macrophages (Days 3–14)**

5. **SCV establishment:** Unlike non-typhoidal Salmonella (which may escape to cytosol in some cells), *S.* Typhi preferentially remains within the **Salmonella-containing vacuole (SCV)** — a modified phagosomal compartment

6. **SPI-2 T3SS activation:** As the SCV acidifies (pH ~5.0), SPI-2 is induced and secretes effectors that:
   - **SifA** recruits LAMP1⁺ late endosomal membranes to extend SCV tubular networks (Salmonella-induced filaments, SIFs)
   - **SseJ** (acyltransferase) esterifies cholesterol in SCV membrane, altering membrane fluidity
   - **SseF/SseG** tether the SCV to the Golgi, intercepting trafficking vesicles for membrane and nutrient supply
   - **SspH2/SseI** dampen NF-κB activation and dendritic cell migration to lymph nodes (immune evasion)
   - Net effect: SCV resists lysosomal fusion, avoids reactive oxygen species, and becomes a **protected replication niche**

7. **Typhoid toxin secretion:** The typhoid toxin (CdtB + PltA + PltB) is secreted from within the SCV via a dedicated periplasmic secretion pathway and exported to the extracellular space. It is then re-endocytosed by host cells via its PltB binding subunit, which recognizes acetylated sialoglycans. The CdtB DNase subunit induces DNA double-strand breaks; PltA ADP-ribosylates Gαi; collectively causing cell cycle arrest, neurological symptoms (typhoid encephalopathy), and potentially facilitating the chronic carrier state

**Phase 3: Systemic dissemination (Days 7–21)**

8. **Bacteremia:** Infected macrophages carry *S.* Typhi via the lymphatics to the thoracic duct and into the bloodstream — a **sustained, low-grade bacteremia** (typically <10 CFU/mL, requiring large blood volumes for culture sensitivity)

9. **Seeding of RES organs:** Bacteria seed macrophages of the **liver (Kupffer cells), spleen (red pulp macrophages), and bone marrow** — forming persistent foci of intracellular replication that maintain bacteremia

10. **Gallbladder colonization:** *S.* Typhi excreted in bile colonizes the gallbladder (especially on gallstones) forming a **biofilm reservoir** that seeds the intestine again, creating the secondary wave of intestinal disease (re-invasion of Peyer's patches → intestinal ulceration and potential perforation in week 3)

## Host Interactions

### Vi Capsule-Mediated Immune Evasion

The Vi polysaccharide capsule is the dominant virulence and immune evasion determinant of *S.* Typhi:

| Mechanism | Detail |
|:---|:---|
| **Complement evasion** | Vi capsule prevents C3b deposition on the bacterial surface; reduces opsonophagocytosis by neutrophils and macrophages |
| **TLR4 shielding** | Vi physically shields the underlying LPS O-antigen from TLR4/MD-2 recognition, blunting the initial innate inflammatory response |
| **TLR5 dampening** | Vi capsule expression is co-regulated with flagella suppression; non-flagellated intracellular bacteria avoid TLR5/NLRC4 detection |
| **Serum resistance** | Vi inhibits the bactericidal effect of normal serum (complement-mediated killing) — critical during the bacteremic phase |

### Innate Immune Subversion

| Mechanism | Effector | Detail |
|:---|:---|:---|
| **Phagosome arrest** | SPI-2 T3SS effectors (SifA, SseF, SseG) | SCV maintained at late endosomal stage; LAMP1⁺ but lysosomal hydrolases largely excluded |
| **Oxidative burst suppression** | SpiC, SseL (deubiquitinase) | Inhibit NADPH oxidase assembly; SseL removes ubiquitin from SCV membranes |
| **NF-κB suppression** | SspH1 (ubiquitin ligase targeting IKKβ), AvrA (acetyltransferase) | Dampen IL-8, TNF-α production — reduces the intensity of local inflammation and neutrophil recruitment |
| **DC migration block** | SseI | Inhibits IQGAP1 → impairs DC chemotaxis to lymph nodes → delayed T-cell priming |

### Adaptive Immunity and Carrier State

- **Protective immunity:** Primarily humoral (Vi-specific IgG from Vi-conjugate vaccines) + cell-mediated (CD4⁺ Th1, CD8⁺ CTL). Vi antibody titers >1 µg/mL correlate with protection in efficacy trials
- **Chronic carriage:** ~1–4% of convalescents; Vi capsule enables biofilm formation in the gallbladder; gallstones serve as scaffold. Eradication requires prolonged antibiotic therapy (fluoroquinolones or azithromycin ×4 weeks) with or without cholecystectomy
- **H58 genotype:** The dominant global lineage, now designated clade 4.3.1 (by Pathogenwatch MLST); harbors an IncHI1 plasmid mediating XDR resistance

## Connections

- **Damages** → [Digestive System](../../../01-human/07-system/digestive-system/README.md): *S.* Typhi causes mucosal hyperplasia and necrosis of ileal Peyer's patches, producing the classic "pea soup" diarrhea of typhoid. Re-invasion of intestinal mucosa in week 3 causes ulceration over Peyer's patches, with 0.8–3% of hospitalized cases progressing to intestinal perforation — a surgical emergency with ~25% mortality even with timely intervention.

- **Infects** → [Small Intestine](../../../01-human/06-organ/small-intestine/README.md): The terminal ileum's Peyer's patches are the primary portal of entry. SPI-1 T3SS effectors (SopE, SopB, SipA, SipC) reprogram the M-cell cytoskeleton to engulf bacteria; subepithelial macrophages then internalize the bacteria and initiate the systemic dissemination cascade.

- **Damages** → [Macrophage](../../../01-human/04-cellular/macrophage/README.md): Rather than being destroyed, *S.* Typhi co-opts macrophages as its systemic transport and replication vehicle. SPI-2 T3SS maintains the SCV against lysosomal fusion; infected Kupffer cells, splenic macrophages, and bone marrow macrophages sustain the bacteremia that defines typhoid fever's clinical course.

- **Damages** → [Liver](../../../01-human/06-organ/liver/README.md): Hepatomegaly and elevated transaminases occur in >50% of typhoid patients from hepatocyte infection and Kupffer cell inflammation. Rare fulminant hepatitis (<1%) can occur. The gallbladder — anatomically and physiologically connected to the liver — is the chronic carrier reservoir where biofilm *S.* Typhi persists on gallstones for years.

## Pathology

### Clinical Course: Typhoid Fever

The incubation period is **7–21 days** (typically 10–14 days), reflecting the time required for intestinal invasion, lymphatic transit, and sufficient systemic bacterial burden to produce symptoms. The classic presentation evolved before antibiotic treatment; modern antibiotic-treated typhoid may be abbreviated.

| Week | Clinical Features | Pathological Correlate |
|:---|:---|:---|
| **Week 1** | Stepwise rising fever (reaching 39–40°C by day 5–7), headache, malaise, relative bradycardia (pulse-temperature dissociation — Faget's sign) | Primary bacteremia from intestinal translocation; macrophage seeding of liver/spleen |
| **Week 2** | Sustained fever, splenomegaly, hepatomegaly, rose spots (salmon-colored 2–4 mm blanching maculopapules on trunk; 10–30% of patients; from bacteremic emboli), "pea soup" diarrhea or constipation | Peak bacteremia; hepatic and splenic Kupffer cell infection; intestinal Peyer's patch hyperplasia |
| **Week 3** | Complications: intestinal perforation (0.8–3%), intestinal hemorrhage (2–8%), encephalopathy ("typhoid state"), myocarditis, nephritis | Peyer's patch ulceration and necrosis from re-invasion; maximal organ involvement |
| **Week 4** | Gradual defervescence in survivors; high relapse risk (~5–10%) if treated sub-optimally | Immune clearance; residual macrophage foci; gallbladder colonization beginning |

### Complications

| Complication | Frequency | Management |
|:---|:---|:---|
| **Intestinal perforation** | 0.8–3% | Emergency surgery (repair or resection); IV antibiotics; ICU; 25% mortality even with surgery |
| **Intestinal hemorrhage** | 2–8% | Transfusion support; bowel rest; rarely surgical |
| **Typhoid encephalopathy** | 2–40% (variable definitions) | Dexamethasone (high-dose: 3 mg/kg then 1 mg/kg ×8 doses) reduces mortality in severe cases |
| **Myocarditis** | ~10% subclinical ECG changes | Supportive; rarely requires intervention |
| **Hepatic failure** | <1% | Supportive; liver transplant evaluation in fulminant cases |
| **Relapse** | 5–10% | Re-treat with same or alternative antibiotic |

### Diagnostics

| Method | Specimen | Sensitivity | Notes |
|:---|:---|:---|:---|
| **Blood culture** | 10–15 mL blood (3 sets) | 40–80% (Week 1–2) | Gold standard; yield falls after antibiotic exposure; optimal in first week |
| **Bone marrow culture** | Bone marrow aspirate | 85–95% | Higher yield than blood; less affected by prior antibiotics; invasive |
| **Stool culture** | Stool | 30–40% (Week 3) | Lower yield in systemic disease; useful in outbreak investigation |
| **Widal test** | Serum | Poor (40–60%); many false positives | Agglutination against O and H antigens; limited by poor specificity in endemic areas; largely replaced |
| **Typhidot (IgM/IgG dot ELISA)** | Serum | ~75–80% sensitivity, ~75–80% specificity | Rapid; better than Widal; limited by cross-reactivity in endemic settings |
| **TUBEX (anti-O9 IgM)** | Serum | ~69–77% sensitivity | Detects IgM against Vi-negative O9 antigen; not affected by Vi capsule |
| **PCR** | Blood | ~80–90% (experimental) | Not widely available; research use; targets flagellin *fliC* or *Vi viaB* |

### Treatment

**First-line (susceptible strains):**
- **Fluoroquinolones** (ciprofloxacin 500 mg BID ×7–10 days; ofloxacin; levofloxacin): Highly effective; rapid defervescence (3–5 days); high intracellular penetration
- **Azithromycin** (1 g loading dose then 500 mg/day ×7 days): Oral; safe in children and pregnancy; effective against nalidixic acid-resistant strains

**For XDR typhoid (Pakistan H58 XDR clade — resistant to chloramphenicol, ampicillin, TMP-SMX, fluoroquinolones, third-generation cephalosporins):**
- **Azithromycin** (resistant strains emerging): Still effective for uncomplicated disease from most XDR strains
- **Carbapenems** (meropenem, ertapenem): IV; for severe/complicated XDR typhoid; reserve agents

**Prevention:**
- **Ty21a (oral live-attenuated vaccine):** 3–4 doses; ~50–70% efficacy; requires cold chain; not for <5 years, immunocompromised [^who-typhoid-2018]
- **Vi-PS (unconjugated Vi polysaccharide vaccine, e.g., Typhim Vi):** Single IM dose; ~55–72% efficacy; not immunogenic in <2-year-olds; no T-cell memory
- **Typbar-TCV (Vi-CRM197 conjugate vaccine):** Vi polysaccharide conjugated to *Corynebacterium diphtheriae* CRM197 carrier protein; WHO-prequalified 2017; ~81.6% efficacy in randomized trial (Nepal); immunogenic from 6 months of age; T-cell dependent memory; now deployed in Gavi-supported campaigns across South Asia [^who-typhoid-2018]
- **WASH interventions:** Improved water, sanitation, and hygiene (WASH) are the ultimate preventive strategy; vaccines are an interim bridge

---

> **AI co-maintenance notice:** Portions of this entry were drafted or reviewed with AI assistance. All content is cross-checked against primary sources; contact bpupadhyaya@gmail.com for corrections.

[^parry-2002-typhoid-review]: Parry CM, Hien TT, Dougan G, White NJ, Farrar JJ. Typhoid fever. *N Engl J Med.* 2002;347(22):1770-82. [doi:10.1056/NEJMra020201](https://doi.org/10.1056/NEJMra020201) · [PubMed 12456854](https://pubmed.ncbi.nlm.nih.gov/12456854/)
[^crump-2019-typhoid-burden]: Crump JA. Progress in Typhoid Fever Epidemiology. *Clin Infect Dis.* 2019;68(Suppl 1):S4-S9. [doi:10.1093/cid/ciy846](https://doi.org/10.1093/cid/ciy846) · [PubMed 30767000](https://pubmed.ncbi.nlm.nih.gov/30767000/)
[^galan-1994-spi1-t3ss]: Galan JE, Curtiss R 3rd. Cloning and molecular characterization of genes whose products allow *Salmonella typhimurium* to penetrate tissue culture cells. *Proc Natl Acad Sci USA.* 1989;86(16):6383-7. [doi:10.1073/pnas.86.16.6383](https://doi.org/10.1073/pnas.86.16.6383) · [PubMed 2548212](https://pubmed.ncbi.nlm.nih.gov/2548212/)
[^who-typhoid-2018]: World Health Organization. Typhoid vaccines: WHO position paper, March 2018. *Wkly Epidemiol Rec.* 2018;93(13):153-172. [who.int/publications/i/item/who-wer9313](https://www.who.int/publications/i/item/who-wer9313)
[^mandell-principles]: Bennett JE, Dolin R, Blaser MJ. *Mandell, Douglas, and Bennett's Principles and Practice of Infectious Diseases.* 9th ed. Elsevier; 2020.
[^murray-microbiology]: Murray PR, Rosenthal KS, Pfaller MA. *Medical Microbiology.* 9th ed. Elsevier; 2021.
