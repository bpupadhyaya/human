---
schema: pathogen-entry/v1
id: listeria-monocytogenes
name: Listeria monocytogenes
atlas: 02-pathogen
scale: 02-bacteria
status: draft
last_reviewed: 2026-06-05
summary: "Gram-positive facultative intracellular rod; psychrotrophic (grows at 4°C). InlA/InlB invasins → LLO pore-forming toxin → cytosolic escape → ActA actin comet-tail spread. Causes listeriosis: meningitis, septicemia, pregnancy-associated infection; CFR 20-30%."
aliases: ["L. monocytogenes", "Listeria", "listeriosis agent", "LM"]
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
  - id: cossart-2011-listeria-actin
    type: peer-reviewed
    cite: "Cossart P. Illuminating the landscape of host-pathogen interactions with the bacterium Listeria monocytogenes. Proc Natl Acad Sci USA. 2011;108(49):19484-91."
    doi: "10.1073/pnas.1112371108"
    pmid: "22114192"
    url: "https://doi.org/10.1073/pnas.1112371108"
  - id: vazquez-boland-2001-listeria-virulence
    type: peer-reviewed
    cite: "Vazquez-Boland JA, Kuhn M, Berche P, et al. Listeria pathogenesis and molecular virulence determinants. Clin Microbiol Rev. 2001;14(3):584-640."
    doi: "10.1128/CMR.14.3.584-640.2001"
    pmid: "11432815"
    url: "https://doi.org/10.1128/CMR.14.3.584-640.2001"
  - id: lecuit-2001-inla-ecadherin
    type: peer-reviewed
    cite: "Lecuit M, Dramsi S, Gottardi C, Fedor-Chaiken M, Gumbiner B, Cossart P. A single amino acid in E-cadherin responsible for host specificity towards the human pathogen Listeria monocytogenes. EMBO J. 1999;18(14):3956-63."
    doi: "10.1093/emboj/18.14.3956"
    pmid: "10406798"
    url: "https://doi.org/10.1093/emboj/18.14.3956"
  - id: who-listeria-2018
    type: regulatory
    cite: "World Health Organization. Listeriosis. WHO Fact Sheet. 2018."
    url: "https://www.who.int/news-room/fact-sheets/detail/listeriosis"
    accessed: "2026-06-05"
cross_links:
  - target: 01-human/06-organ/brain
    relation: damages
    note: "Listeria crosses the blood-brain barrier via infected monocytes and direct transcytosis, causing meningoencephalitis, brain abscesses, and rhombencephalitis — severe in immunocompromised and neonates."
  - target: 01-human/07-system/nervous-system
    relation: damages
    note: "Rhombencephalitis from brainstem Listeria invasion is a distinctive severe complication; CNS damage occurs via direct bacterial lysis (LLO) and inflammatory cell infiltration, with high mortality and neurological sequelae."
  - target: 01-human/04-cellular/macrophage
    relation: damages
    note: "After LLO-mediated phagosomal escape, Listeria replicates in the macrophage cytosol and uses ActA-driven actin polymerization to spread directly into adjacent cells, avoiding extracellular immune exposure."
  - target: 01-human/07-system/digestive-system
    relation: infects
    note: "Listeria colonizes intestinal epithelium via InlA-E-cadherin binding, causing febrile gastroenteritis; mucosal invasion enables hematogenous dissemination to liver, spleen, CNS, and placenta."
---

# Listeria monocytogenes

## Overview

*Listeria monocytogenes* is a **Gram-positive, facultative intracellular** food-borne pathogen and one of the most elegant bacterial models of host-cell invasion and cytosolic motility. It causes **listeriosis** — a disease with a relatively low incidence (~0.3 per 100,000 population annually in industrialized countries) but an unusually high **case fatality rate of 20–30%**, making it one of the deadliest food-borne infections in the world [^who-listeria-2018].

The organism has two defining biological features that underlie its pathogenicity and epidemiology:

1. **Psychrotrophic growth:** *L. monocytogenes* thrives at **4°C (refrigerator temperature)**, grows at salt concentrations up to 10%, and tolerates pH 4.4–9.4. This makes cold-chain contamination of ready-to-eat foods (deli meats, soft cheeses, smoked fish, raw sprouts) a persistent public health hazard
2. **Facultative intracellular lifestyle:** Using a remarkably well-characterized set of virulence factors, the bacterium invades non-phagocytic cells, escapes the phagosome, replicates freely in the host cytosol, and spreads directly from cell to cell using an **ActA-driven actin polymerization ("comet tail") mechanism** — without ever being exposed to the extracellular environment or circulating antibodies [^cossart-2011-listeria-actin]

Listeriosis disproportionately affects immunocompromised individuals, pregnant women (and their fetuses/neonates), elderly adults (>65 years), and patients on corticosteroids or TNF-α inhibitors. In these populations it presents as **meningoencephalitis, septicemia, and — during pregnancy — miscarriage, stillbirth, or severe neonatal disease**. Outbreaks are recurring and often linked to industrial food contamination events.

*L. monocytogenes* has become a foundational model organism in cell biology and innate immunity research, particularly for understanding actin dynamics, phagosomal escape, cytosolic innate sensing (cGAS-STING, NLRP3), and cell-to-cell bacterial spread [^vazquez-boland-2001-listeria-virulence].

## Structure

### Cell Morphology

*L. monocytogenes* is a **short Gram-positive rod**, 0.4–0.5 µm × 0.5–2.0 µm, occurring singly or in pairs. Key physical characteristics:

| Property | Detail |
|:---|:---|
| **Gram reaction** | Positive (thick peptidoglycan wall) |
| **Spores** | None formed |
| **Capsule** | None (though cell wall LTA contributes to surface properties) |
| **Motility** | Peritrichous flagella expressed at <37°C (tumbling motility, room temperature); flagella downregulated at 37°C inside the host — controlled by the PrfA transcriptional regulator |
| **Growth range** | 1°C to 45°C; optimum 30–37°C; psychrotrophic growth at 4°C is the public-health key property |
| **Hemolysis** | Beta-hemolysis on blood agar (from LLO); distinguishes pathogenic from non-pathogenic *Listeria* species |
| **Biochemistry** | Catalase-positive; oxidase-negative; produces acetoin (VP+); hydrolyses aesculin (esculin agar) |

### Genome and Virulence Gene Clusters

| Locus/Gene | Product | Function |
|:---|:---|:---|
| **PrfA regulon** | PrfA transcriptional activator | Master virulence regulator; temperature-sensitive (active at 37°C); activates all major virulence genes below |
| **inlA** | Internalin A (InlA) | Surface LPXTG-anchored protein; binds human E-cadherin (CDH1); required for invasion of intestinal epithelium and the placental barrier |
| **inlB** | Internalin B (InlB) | GW domain surface protein; binds hepatocyte growth factor receptor Met (c-Met) and gC1qR; required for hepatocyte and CNS endothelial cell invasion |
| **hly** | Listeriolysin O (LLO) | Cholesterol-dependent cytolysin (CDC family); pore-forming toxin that lyses the single- and double-membrane phagosomal vacuoles to release bacteria into cytosol |
| **plcA** | PI-PLC (phosphatidylinositol-specific PLC) | Assists LLO in disrupting the primary (single-membrane) phagosome |
| **plcB** | PC-PLC (broad-range PLC) | Processes the double-membrane vacuole formed during cell-to-cell spread |
| **actA** | ActA | Surface protein; nucleates Arp2/3 complex → branched actin polymerization at the bacterial surface → "comet tail" propulsion → protrusions into adjacent cells |
| **mpl** | Metalloprotease | Activates PC-PLC; degrades surface-bound InlB |

## Infection Mechanism

### Food-borne Acquisition and Intestinal Invasion

1. **Ingestion:** Contaminated ready-to-eat food (soft cheeses, deli meats, smoked salmon, raw sprouts) delivers *L. monocytogenes* to the gastrointestinal tract. The infectious dose in immunocompetent hosts is estimated at >10⁷–10⁸ CFU; in immunocompromised patients this may be orders of magnitude lower [^who-listeria-2018]

2. **Gastric survival:** *L. monocytogenes* tolerates stomach acidity (pH ≥4.4) and bile salts, aided by the bile salt hydrolase BilE and the stress response sigma factor σB

3. **Intestinal epithelial invasion — InlA/E-cadherin pathway:**
   - InlA (Internalin A) on the bacterial surface binds **E-cadherin (CDH1)** on intestinal epithelial cells. E-cadherin is normally located on the basolateral surface; it is accessible apically in the villous tips where cells are shed, and is expressed apically in mucosal folds and M cells
   - Binding triggers **clathrin-mediated phagocytosis** via recruitment of α-catenin/β-catenin/α-actinin; this co-opts the cadherin endocytosis machinery to bring the bacterium inside the epithelial cell [^lecuit-2001-inla-ecadherin]
   - InlA binds human E-cadherin with high affinity due to a glutamic acid at position 16 of E-cadherin; rodent E-cadherin (proline at position 16) is not bound — explaining the mouse model's poor fidelity to human listeriosis

4. **Alternative M-cell route:** Ileal Peyer's patch M cells, which have reduced tight junctions and specialized transcytotic function, are also invaded via InlA-independent mechanisms and serve as an efficient portal for bacterial entry into the subepithelial space

### Phagosomal Escape — the LLO Mechanism

After internalization, *L. monocytogenes* faces destruction in the phagosomal compartment:

1. **LLO (listeriolysin O)** is secreted by the bacterium and inserts into the phagosomal membrane as oligomeric pores. LLO is optimally active at the **acidic pH of the phagosome (pH 5.5)** and is rapidly inactivated at cytoplasmic pH (7.2) — an elegant safety mechanism that prevents it from lysing the host plasma membrane after escape

2. **PI-PLC (PlcA)** cooperates with LLO to disrupt the primary phagosomal membrane

3. The bacterium exits into the **host cytosol** — a nutrient-rich environment where it replicates rapidly (generation time ~1 hour at 37°C)

### Cytosolic Motility and Cell-to-Cell Spread

Once in the cytosol, *L. monocytogenes* achieves intracellular motility and cell-to-cell spread via **ActA-driven actin comet tail formation** — one of the best-characterized examples of pathogen exploitation of host cytoskeletal machinery:

1. **ActA** is expressed asymmetrically on one pole of the bacterium. It functions as a **WASP-family protein mimic**, directly activating the host **Arp2/3 complex** to nucleate branched actin networks

2. Host factors recruited include **VASP** (vasodilator-stimulated phosphoprotein), **profilin**, **cofilin**, and **ADF** — the same molecular ensemble that drives lamellipodium extension in motile cells

3. The actin comet tail propels the bacterium at **0.1–1.4 µm/min**, pushing it through the cytoplasm toward the cell periphery

4. The bacterium pushes against the plasma membrane, forming a **protrusion** into the adjacent cell. The protrusion is engulfed by the neighbor cell, forming a **double-membrane vacuole (secondary phagosome)**

5. **PC-PLC (PlcB)** and **LLO** cooperate to lyse both membranes of this double-membrane vacuole → bacteria released into the next cell's cytosol → cycle repeats

This mechanism allows *L. monocytogenes* to disseminate through tissues while remaining entirely intracellular, never exposed to extracellular antibodies, complement, or neutrophils.

### Crossing Barrier Epithelia

- **Blood-brain barrier (BBB):** *L. monocytogenes* crosses via: (i) infected monocytes acting as "Trojan horses" across inflamed BBB endothelium; (ii) direct InlB/Met-dependent invasion of brain microvascular endothelial cells; (iii) choroid plexus epithelial cells (InlA-dependent)

- **Feto-placental barrier:** InlA binds E-cadherin on human syncytiotrophoblasts; InlB binds Met on extravillous trophoblasts → placental invasion → maternal bacteremia → fetal bacteremia. Human placenta is uniquely susceptible due to differences from rodent placenta — the reason for the high pregnancy-associated risk in humans

## Host Interactions

### Innate Immunity and Cytosolic Sensing

Once *L. monocytogenes* reaches the cytosol, it triggers powerful innate immune sensing:

| Sensor | Ligand | Response |
|:---|:---|:---|
| **NOD1/NOD2** | Peptidoglycan fragments (MDP, iE-DAP) | NF-κB activation → IL-6, IL-12, TNF-α; antimicrobial peptides |
| **cGAS-STING** | Bacterial DNA (and mitochondrial DNA released by LLO pore-forming activity) | Type I IFN production; paradoxically, type I IFN *promotes* listeriosis by inducing lymphocyte apoptosis and downregulating IL-17 responses |
| **NLRP3 inflammasome** | LLO-induced K⁺ efflux | IL-1β and IL-18 maturation; pyroptosis |
| **AIM2 inflammasome** | Cytosolic dsDNA | IL-1β; pyroptosis; cell death limits bacterial spread |

### Adaptive Immunity

Clearance of listeriosis requires **cell-mediated immunity (CMI)**:
- **CD8⁺ CTLs** recognizing *Listeria* peptides on MHC-I (because bacteria release protein into the cytosol where the class I antigen presentation pathway operates) are the primary protective effectors — this is why the CD4⁺/CD8⁺ T-cell-depleting effects of HIV, transplant immunosuppression, and corticosteroids so dramatically increase susceptibility
- **CD4⁺ Th1 cells** provide IFN-γ for macrophage activation and cytotoxic support
- **γδ T cells** contribute in the early phase before conventional T-cell responses are established
- **Antibody (humoral immunity):** Largely ineffective against intracellular *Listeria*; anti-LLO IgG can limit initial invasion but cannot clear established infection

### Virulence Factor Expression Regulation

The **PrfA regulon** is the master switch. PrfA is a member of the Crp/Fnr transcription factor family; it becomes active at 37°C (translational thermoswitch: an RNA thermometer in the 5' UTR of *prfA* mRNA melts at 37°C, allowing ribosome access). This ensures virulence genes are expressed in warm-blooded hosts but repressed in the food environment.

## Connections

- **Damages** → [Brain](../../../01-human/06-organ/brain/README.md): *Listeria* crosses the blood-brain barrier via infected monocytes ("Trojan horse") and direct InlB/Met-dependent invasion of brain microvascular endothelium. It causes meningoencephalitis — typically with mononuclear CSF pleocytosis — and rhombencephalitis, a distinctive brainstem form with cranial nerve palsies and cerebellar signs.

- **Damages** → [Nervous System](../../../01-human/07-system/nervous-system/README.md): Rhombencephalitis is a hallmark of *Listeria* CNS disease, reflecting the bacterium's tropism for brainstem tissue. LLO-mediated neuronal lysis and the accompanying inflammatory infiltrate cause focal neurological deficits, cranial neuropathies, and long-term neurological sequelae in survivors.

- **Damages** → [Macrophage](../../../01-human/04-cellular/macrophage/README.md): Macrophages attempt to destroy ingested *Listeria* but are subverted by LLO-mediated phagosomal escape. Bacteria replicate freely in the macrophage cytosol and use ActA-driven actin comet tails to spread into neighboring cells — the macrophage is converted from pathogen-killer to intracellular reservoir and dissemination vehicle.

- **Infects** → [Digestive System](../../../01-human/07-system/digestive-system/README.md): Listeriosis begins with intestinal invasion via InlA binding to E-cadherin on villous tip enterocytes and M cells in Peyer's patches. Febrile gastroenteritis may precede invasive disease; translocation across the intestinal epithelium initiates the bacteremia that seeds the CNS, placenta, and other deep-tissue sites.

## Pathology

### Clinical Presentations

| Syndrome | Population | Features | CFR |
|:---|:---|:---|:---|
| **Febrile gastroenteritis** | Healthy adults (outbreak setting) | Self-limited; watery diarrhea, fever, myalgia; no bacteremia | <1% |
| **Invasive listeriosis — primary bacteremia** | Immunocompromised, elderly | Fever, bacteremia, shock; without CNS involvement | 20–30% |
| **Meningoencephalitis** | Immunocompromised, elderly | Fever, stiff neck, altered consciousness; CSF: mononuclear pleocytosis, elevated protein; *Listeria* often reported as "Gram-positive rods" in CSF or blood culture | 30–40% |
| **Rhombencephalitis** | Adults (often previously healthy) | Brainstem involvement: cranial nerve palsies (VI, VII), ataxia, nystagmus, altered consciousness; MRI shows T2 hyperintensity in pons/medulla | ~50% |
| **Maternal-neonatal listeriosis** | Pregnant women (3rd trimester) and neonates | Maternal: flu-like illness with bacteremia → placental infection → fetal infection. Neonatal early-onset (<5 days): septicemia, pneumonia, granulomatosis infantiseptica. Neonatal late-onset (5–28 days): meningitis (from birth canal exposure) | Maternal: ~1%; neonatal: 20–40% |

### Diagnostics

| Method | Specimen | Notes |
|:---|:---|:---|
| **Blood culture** | Blood | Gold standard for bacteremia; BACTEC/BacT/Alert automated systems; colonies show beta-hemolysis; confirmed by catalase+, tumbling motility, CAMP test (enhanced hemolysis with *S. aureus*) |
| **CSF culture** | Cerebrospinal fluid | Gram-positive rods (may be misidentified as diphtheroids or contaminants — clinical vigilance required); CSF cell count: predominantly mononuclear (unusual among bacterial meningitis causes) |
| **MALDI-TOF MS** | Culture isolate | Rapid species ID from colony; high accuracy |
| **PCR** | Blood, CSF, placenta | Rapid; useful when cultures are negative; targets *hly* or *actA* genes |
| **Whole-genome sequencing (WGS)** | Outbreak investigation | MLST and cgMLST for outbreak source-tracing; mandatory in many national reference labs |

### Treatment

**Ampicillin** (IV; 2 g every 4 hours) is the drug of choice — *Listeria* is intrinsically resistant to all cephalosporins (a critical prescribing point in empirical meningitis treatment: add ampicillin to cover *Listeria* in at-risk patients even when a third-generation cephalosporin is given).

- **Synergy:** Gentamicin added to ampicillin for bacteremia and meningitis (synergistic killing in vitro and in animal models); standard for non-pregnant adults
- **Penicillin allergy:** Trimethoprim-sulfamethoxazole (TMP-SMX) is the best-validated alternative; bactericidal against *Listeria*
- **Duration:** Bacteremia: 14 days; meningitis: 21 days; brain abscess/rhombencephalitis: 42–56 days
- **Dexamethasone:** NOT recommended (unlike pneumococcal meningitis — dexamethasone reduces ampicillin CNS penetration and may worsen *Listeria* meningitis outcomes)
- **No vaccine:** No approved human vaccine. Prevention relies on food safety: HACCP protocols, temperature control, and avoidance of high-risk foods during pregnancy

---

> **AI co-maintenance notice:** Portions of this entry were drafted or reviewed with AI assistance. All content is cross-checked against primary sources; contact bpupadhyaya@gmail.com for corrections.

[^cossart-2011-listeria-actin]: Cossart P. Illuminating the landscape of host-pathogen interactions with the bacterium *Listeria monocytogenes*. *Proc Natl Acad Sci USA.* 2011;108(49):19484-91. [doi:10.1073/pnas.1112371108](https://doi.org/10.1073/pnas.1112371108) · [PubMed 22114192](https://pubmed.ncbi.nlm.nih.gov/22114192/)
[^vazquez-boland-2001-listeria-virulence]: Vazquez-Boland JA, Kuhn M, Berche P, et al. *Listeria* pathogenesis and molecular virulence determinants. *Clin Microbiol Rev.* 2001;14(3):584-640. [doi:10.1128/CMR.14.3.584-640.2001](https://doi.org/10.1128/CMR.14.3.584-640.2001) · [PubMed 11432815](https://pubmed.ncbi.nlm.nih.gov/11432815/)
[^lecuit-2001-inla-ecadherin]: Lecuit M, Dramsi S, Gottardi C, et al. A single amino acid in E-cadherin responsible for host specificity towards *Listeria monocytogenes*. *EMBO J.* 1999;18(14):3956-63. [doi:10.1093/emboj/18.14.3956](https://doi.org/10.1093/emboj/18.14.3956) · [PubMed 10406798](https://pubmed.ncbi.nlm.nih.gov/10406798/)
[^who-listeria-2018]: World Health Organization. *Listeriosis.* WHO Fact Sheet. 2018. [who.int/news-room/fact-sheets/detail/listeriosis](https://www.who.int/news-room/fact-sheets/detail/listeriosis)
[^mandell-principles]: Bennett JE, Dolin R, Blaser MJ. *Mandell, Douglas, and Bennett's Principles and Practice of Infectious Diseases.* 9th ed. Elsevier; 2020.
[^murray-microbiology]: Murray PR, Rosenthal KS, Pfaller MA. *Medical Microbiology.* 9th ed. Elsevier; 2021.
