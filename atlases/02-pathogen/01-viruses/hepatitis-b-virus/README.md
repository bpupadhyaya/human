---
schema: pathogen-entry/v1
id: hepatitis-b-virus
name: Hepatitis B Virus
atlas: 02-pathogen
scale: 01-viruses
status: active
last_reviewed: 2026-06-04
summary: "Hepadnavirus (Hepadnaviridae). 3.2 kb rcDNA; smallest DNA virus. Infects hepatocytes via NTCP receptor; nuclear cccDNA minichromosome drives persistence. Chronic infection leads to cirrhosis and hepatocellular carcinoma."
taxonomy:
  family: Hepadnaviridae
  genus: Orthohepadnavirus
genome:
  type: DNA
  description: "3.2 kb partially double-stranded relaxed circular DNA (rcDNA); smallest DNA virus infecting humans"
replication_site: "Hepatocytes (liver)"
transmission:
  - blood (transfusion, needle sharing)
  - sexual contact
  - vertical/perinatal (mother-to-child)
aliases: ["HBV", "hepatitis B", "Australia antigen virus", "Dane particle virus"]
tags: [hepadnavirus, hepatitis, cirrhosis, hcc, hbsag, ccc-dna, liver]
sources:
  - id: blumberg-1965-australia-antigen
    type: peer-reviewed
    cite: "Blumberg BS, Alter HJ, Visnich S. A 'new' antigen in leukemia sera. JAMA. 1965;191(7):541-6."
    pmid: "14325610"
    url: "https://pubmed.ncbi.nlm.nih.gov/14325610/"
  - id: lok-2017-hbv-review
    type: peer-reviewed
    cite: "Lok AS, McMahon BJ, Brown RS Jr, et al. Antiviral therapy for chronic hepatitis B viral infection in adults: a systematic review and meta-analysis. Hepatology. 2016;63(1):284-306. [Review reference: Lok AS. Hepatitis B. N Engl J Med. 2017.]"
    doi: "10.1056/NEJMra1700786"
    url: "https://doi.org/10.1056/NEJMra1700786"
  - id: chang-1997-vaccine-efficacy
    type: peer-reviewed
    cite: "Chang MH, Chen CJ, Lai MS, et al. Universal hepatitis B vaccination in Taiwan and the incidence of hepatocellular carcinoma in children. N Engl J Med. 1997;336(26):1855-9."
    pmid: "9187068"
    url: "https://pubmed.ncbi.nlm.nih.gov/9187068/"
  - id: yan-2012-ntcp-receptor
    type: peer-reviewed
    cite: "Yan H, Zhong G, Xu G, et al. Sodium taurocholate cotransporting polypeptide is a functional receptor for human hepatitis B and D virus. eLife. 2012;1:e00049."
    doi: "10.7554/eLife.00049"
    pmid: "23150796"
    url: "https://doi.org/10.7554/eLife.00049"
cross_links:
  - target: 01-human/04-cellular/hepatocyte
    relation: infects
    note: "HBsAg preS1 domain binds NTCP (sodium-taurocholate cotransporting polypeptide) on hepatocytes; this is the primary and essentially exclusive cell type productively infected by HBV."
  - target: 01-human/06-organ/liver
    relation: infects
    note: "Hepatocytes in all zones of the hepatic lobule can be infected; HBsAg subviral particles and Dane particles circulate in blood at extraordinary concentrations during active replication."
  - target: 01-human/07-system/digestive-system
    relation: infects
    note: "The liver is the dominant organ of the digestive system targeted by HBV; cccDNA establishes a persistent nuclear minichromosome in hepatocytes that is refractory to current antiviral agents."
  - target: 01-human/04-cellular/hepatocyte
    relation: damages
    note: "HBV-mediated liver injury is primarily immune-mediated: CD8+ T cell killing of HBsAg-expressing hepatocytes. Direct cytopathic effect is minimal; immunotolerant neonates have minimal inflammation despite high viral loads."
  - target: 01-human/06-organ/liver
    relation: damages
    note: "Chronic HBV causes progressive hepatic fibrosis (Metavir F0→F4), cirrhosis, and hepatocellular carcinoma; HBsAg integrations and HBx transactivation promote oncogenesis even at low replication levels."
  - target: 01-human/07-system/digestive-system
    relation: damages
    note: "Chronic HBV damages the liver (dominant accessory digestive organ), causing cirrhosis and portal hypertension with GI sequelae: esophageal varices, ascites, spontaneous bacterial peritonitis, and hepatic encephalopathy."
  - target: 01-human/03-molecular/immunoglobulin-g
    relation: target-of
    note: "Anti-HBs IgG (≥10 mIU/mL) is the serological correlate of vaccine-induced protection; anti-HBc IgG marks prior or current infection. Passively administered anti-HBs HBIG prevents perinatal transmission."
---

# Hepatitis B Virus

## Overview

Hepatitis B Virus (HBV) is a member of the family *Hepadnaviridae* (genus *Orthohepadnavirus*) and the causative agent of hepatitis B, a liver disease affecting approximately **254 million people chronically** worldwide, with an estimated **820,000 deaths per year** attributable to cirrhosis and hepatocellular carcinoma (HCC). HBV was the first hepatitis virus characterised, following Baruch Blumberg's discovery in 1965 of the "Australia antigen" (later identified as HBsAg) in the serum of an Australian Aboriginal patient [^blumberg-1965-australia-antigen] — a discovery that earned the 1976 Nobel Prize in Physiology or Medicine.

HBV is notable as the **world's smallest DNA virus** capable of infecting humans (3.2 kb genome), yet achieves remarkable persistence through nuclear covalently closed circular DNA (cccDNA) — a viral minichromosome that current antiviral drugs cannot eliminate. Effective vaccines have been available since 1982; universal infant vaccination has dramatically reduced incidence in countries with high coverage programmes, with Taiwan demonstrating a 90% reduction in childhood HCC incidence after two decades of universal vaccination [^chang-1997-vaccine-efficacy].

## Structure

### Virion and Subviral Particles

HBV-infected blood contains three morphologically distinct forms:

| Particle | Diameter | Composition | Function |
|:---|:---:|:---|:---|
| **Dane particle** (complete virion) | 42 nm | rcDNA core + polymerase, surrounded by HBcAg capsid, enveloped by lipid bilayer + HBsAg | Infectious virion |
| **HBsAg spherical particle** (subviral) | 22 nm | HBsAg + lipid; no nucleocapsid | Non-infectious; in 1,000–10,000× molar excess over Dane particles in serum |
| **HBsAg filamentous particle** (subviral) | 22 nm × variable length | HBsAg + lipid | Non-infectious; may act as antibody decoy |

The **22 nm HBsAg subviral particles** circulate at up to 10¹³ particles/mL in high-replicators, acting as an enormous antibody "decoy" that absorbs anti-HBs antibodies and facilitates immune evasion.

### Genome Organisation

The 3.2 kb **relaxed circular DNA (rcDNA)** consists of a complete minus (−) strand and an incomplete plus (+) strand, held in circular form by cohesive overlapping ends. The genome contains **four overlapping open reading frames** that collectively encode more protein per nucleotide than virtually any other known virus:

| ORF | Protein(s) | Function |
|:---:|:---|:---|
| **S** | preS1/preS2/S → Large, Medium, Small HBsAg | Surface envelope glycoproteins; preS1 binds NTCP (entry receptor) |
| **C** | preCore/C → HBeAg, HBcAg | HBcAg: capsid protein; HBeAg: secreted tolerogen; signals active replication |
| **P** | HBV Polymerase (P) | Reverse transcriptase + RNase H + terminal protein; target of TDF, TAF, ETV |
| **X** | HBx | Transcriptional transactivator; ubiquitin proteasome pathway modulation; essential for cccDNA transcription; oncogenic |

## Infection Mechanism

### Receptor Binding and Entry

Entry of HBV into hepatocytes is a two-step process:

1. **Initial attachment:** The large HBsAg (LHBsAg) preS1 domain (particularly amino acids 2–48) binds to **heparan sulfate proteoglycans (HSPGs)** on the hepatocyte surface, concentrating virions at the cell surface.

2. **High-affinity receptor binding and internalisation:** The preS1 domain then engages **NTCP (sodium-taurocholate cotransporting polypeptide; SLC10A1)**, the bile acid transporter on the basolateral membrane of hepatocytes, as the specific functional receptor [^yan-2012-ntcp-receptor]. NTCP is expressed almost exclusively on hepatocytes, explaining the strict hepatotropism of HBV. Internalisation likely occurs via clathrin-mediated endocytosis.

Bulevirtide (Hepcludex), a synthetic preS1 lipopeptide that competitively inhibits HBsAg binding to NTCP, is the first entry inhibitor approved for chronic hepatitis D co-infection.

### Nuclear Import and cccDNA Formation

After cytoplasmic uncoating, the partially double-stranded rcDNA is transported into the nucleus, where the viral polymerase completes the plus-strand and cellular DNA repair enzymes convert rcDNA to **covalently closed circular DNA (cccDNA)** — an episomal minichromosome of ~3.2 kb associated with histones and viral/host proteins.

cccDNA serves as the **persistent transcriptional template** for all viral RNAs:
- Pregenomic RNA (pgRNA) — the ~3.5 kb template for reverse transcription and translation of core protein and polymerase
- Subgenomic RNAs — templates for HBsAg, HBx, and HBeAg

cccDNA is not targeted by current nucleoside analogue antivirals (tenofovir, entecavir), which act downstream on the reverse transcriptase step. This is why **virological suppression does not equal cure**: cccDNA persists in non-dividing hepatocytes for decades.

### Reverse Transcription

HBV replicates its DNA genome through an RNA intermediate — an evolutionary strategy shared with retroviruses:

1. pgRNA is packaged with HBV polymerase into new capsids
2. HBV polymerase acts as a **reverse transcriptase**: synthesises (−) DNA strand using pgRNA as template, degrading the pgRNA via the RNase H domain
3. Plus (+) DNA strand is partially synthesised using (−) strand as template → produces the characteristic rcDNA molecule

This RNA-intermediate replication strategy is the mechanistic basis for HBV susceptibility to nucleoside/nucleotide RT inhibitors (NRTIs).

## Host Interactions

### Immunological Tolerance vs Immunopathology

The outcome of HBV infection is determined primarily by the host immune response, not direct viral cytotoxicity:

- **Perinatal/neonatal infection:** Immature immune system + HBeAg-mediated tolerisation → immunotolerant phase with high viral loads but minimal liver inflammation → **90% progress to chronic infection**
- **Adult infection:** Robust CD4+ and CD8+ T cell response → vigorous hepatocellular destruction in the attempt to clear virus → **<5% chronicity** (>95% resolve acutely)

CD8+ cytotoxic T lymphocytes (CTLs) recognising HBV epitopes on HLA class I molecules drive hepatocyte killing. The characteristic aminotransferase (ALT/AST) elevation in hepatitis B directly reflects immune-mediated hepatocyte destruction.

### HBx and Oncogenesis

The **HBx protein** is a multifunctional transactivator with no known enzymatic activity but multiple protein-protein interaction domains. HBx:
- Is essential for cccDNA transcription (interacts with CCPG/host chromatin remodelling complexes)
- Activates the Src/Ras/ERK and PI3K/AKT signalling pathways
- Inhibits p53 function and promotes cell survival
- Drives aberrant epigenetic reprogramming of host hepatocytes

HBsAg DNA integrations into the host genome — which occur stochastically and accumulate over years of chronic infection — can directly disrupt tumour suppressor genes and activate oncogenes, promoting HCC development even in patients with suppressed viral replication [^lok-2017-hbv-review].

### Serological Markers

| Marker | Significance |
|:---|:---|
| HBsAg positive | Active HBV infection (acute or chronic) |
| Anti-HBs positive | Resolved infection or successful vaccination (protective) |
| HBeAg positive | Active viral replication; high infectivity |
| Anti-HBe positive | Reduced replication (but HBeAg-negative mutants can still replicate actively) |
| Anti-HBc IgM | Acute/recent infection |
| Anti-HBc IgG | Prior or current infection (persists lifelong) |
| HBV DNA (quantitative) | Viral load; guides treatment decisions and monitoring |

## Connections

- **Infects** → [Hepatocyte](../../../01-human/04-cellular/hepatocyte/README.md): preS1/NTCP-mediated entry; cccDNA establishes persistent nuclear minichromosome; the only cell type productively infected in vivo.
- **Infects** → [Liver](../../../01-human/06-organ/liver/README.md): HBsAg subviral particles and Dane particles produced in vast excess; cccDNA persists even under antiviral therapy.
- **Infects** → [Digestive System](../../../01-human/07-system/digestive-system/README.md): Liver (the central metabolic organ of the digestive system) is the exclusive site of HBV replication.
- **Damages** → [Hepatocyte](../../../01-human/04-cellular/hepatocyte/README.md): Immune-mediated cytolysis by CD8+ CTLs; HBx-driven oncogenic transformation; HBsAg integrations disrupt hepatocyte genome integrity.
- **Damages** → [Liver](../../../01-human/06-organ/liver/README.md): Progressive fibrosis → cirrhosis → HCC; immune-mediated acute and chronic hepatitis; HBx transactivation promotes hepatocarcinogenesis.
- **Target of** → [Immunoglobulin G](../../../01-human/03-molecular/immunoglobulin-g/README.md): Anti-HBs IgG (≥10 mIU/mL) is the correlate of vaccine-induced protection; HBIG (hepatitis B immune globulin) provides passive prophylaxis at birth for neonates of HBsAg-positive mothers.

## Pathology

### Acute Hepatitis B

Most adult primary infections are self-limiting:
- Symptoms: jaundice, fatigue, nausea, right upper quadrant pain, elevated ALT/AST (often >1,000 IU/L)
- Histology: hepatocyte swelling and ballooning, lobular inflammation, spotty necrosis, cholestasis
- Outcome: >95% resolve with HBsAg clearance, anti-HBs seroconversion, and lifelong protective immunity
- **Fulminant hepatic failure:** Rare (<1% of acute cases) but life-threatening; massive hepatocyte necrosis, coagulopathy, encephalopathy; may require liver transplantation

### Chronic Hepatitis B

Chronic HBV (HBsAg positive >6 months) is classified by replication phase:

| Phase | HBeAg | HBV DNA | ALT | Histology | Clinical significance |
|:---|:---:|:---:|:---:|:---|:---|
| **HBeAg+ immune tolerant** | + | Very high (>10⁷ IU/mL) | Normal | Minimal inflammation | Low immediate risk; perinatal acquisition |
| **HBeAg+ immune active** | + | High | Elevated | Active hepatitis, fibrosis | Risk of progression; treat |
| **HBeAg− immune inactive** | − | Low (<2,000 IU/mL) | Normal | Minimal | Favourable; monitor |
| **HBeAg− immune active** | − | Moderate–high | Elevated | Active hepatitis | HBeAg-negative variant (preCore/BCP mutations); treat |
| **Occult HBV** | − | Very low | Normal | Variable | HBsAg negative, anti-HBc+; reactivation risk with immunosuppression |

### Fibrosis Progression and Cirrhosis

Chronic immune-mediated hepatocyte injury → hepatic stellate cell activation → progressive collagen deposition → **fibrosis (Metavir staging: F0 [none] → F4 [cirrhosis])**.

- ~20–30% of chronically infected patients develop cirrhosis over 20–30 years
- Cirrhosis complications: portal hypertension, oesophageal varices, ascites, spontaneous bacterial peritonitis, hepatorenal syndrome, hepatic encephalopathy
- Decompensated cirrhosis carries ~15–20% annual mortality without treatment

### Hepatocellular Carcinoma

HBV-associated HCC is the most common form of primary liver cancer globally:
- **20–30% of HBV cirrhotics** develop HCC over their lifetime
- HCC can arise in non-cirrhotic HBV carriers (particularly those with high viral loads, HBV genotype C or F, or HBx integrations)
- Mechanism: HBx transactivation, chromosomal instability from HBsAg integrations, chronic inflammation/regeneration
- Surveillance: 6-monthly ultrasound ± AFP in cirrhotic patients
- Antiviral therapy with suppression of HBV DNA replication reduces but does not eliminate HCC risk

### Extrahepatic Manifestations

Immune complex deposition (HBsAg–anti-HBs or HBsAg–anti-HBc) can cause:
- **Polyarteritis nodosa (PAN):** Necrotising medium-vessel vasculitis; ~10% of PAN cases associated with HBV
- **Membranous nephropathy:** HBsAg immune complex deposition in glomerular basement membrane; common in children in endemic areas
- **Cryoglobulinaemia (rare)**
- **Arthritis / arthralgias** during prodromal phase (Gianotti-Crosti–like syndrome in children)

### Prevention and Treatment

**Vaccination:**
- 3-dose recombinant HBsAg vaccine series (0, 1, 6 months)
- Anti-HBs titer ≥10 mIU/mL = protective
- Neonates born to HBsAg+ mothers receive vaccine + HBIG within 12 hours of birth → reduces perinatal transmission by ~95% [^chang-1997-vaccine-efficacy]
- First vaccine proven to prevent a human cancer (HCC)

**Antiviral therapy (chronic HBV):**
- **Nucleos(t)ide analogues (NAs):** Tenofovir disoproxil fumarate (TDF), tenofovir alafenamide (TAF), entecavir (ETV) — potent HBV polymerase RT inhibitors; suppress HBV DNA to undetectable levels; reduce fibrosis progression, decompensation, and HCC risk; do **not** eliminate cccDNA
- **Pegylated interferon-α (Peg-IFN):** Immunomodulatory; finite 48-week course; achieves HBsAg loss ("functional cure") in ~3–7% of treated patients; limited by side effects

**Functional cure goal:** HBsAg loss (± anti-HBs seroconversion) — achievable in ~1% of NA-treated patients per year, and considered the practical endpoint of current therapy [^lok-2017-hbv-review]. Novel agents targeting cccDNA transcription (capsid assembly modulators, RNAi agents, core protein allosteric inhibitors) are under clinical development.

## See Also

- [Hepatocyte](../../../01-human/04-cellular/hepatocyte/README.md) — exclusive target cell
- [Liver](../../../01-human/06-organ/liver/README.md) — the organ damaged
- [Digestive System](../../../01-human/07-system/digestive-system/README.md) — system-level context

[^blumberg-1965-australia-antigen]: Blumberg BS, Alter HJ, Visnich S. A 'new' antigen in leukemia sera. *JAMA.* 1965;191(7):541-6. [PubMed 14325610](https://pubmed.ncbi.nlm.nih.gov/14325610/)
[^lok-2017-hbv-review]: Lok AS. Hepatitis B. *N Engl J Med.* 2017. [doi:10.1056/NEJMra1700786](https://doi.org/10.1056/NEJMra1700786)
[^chang-1997-vaccine-efficacy]: Chang MH, Chen CJ, Lai MS, et al. Universal hepatitis B vaccination in Taiwan and the incidence of hepatocellular carcinoma in children. *N Engl J Med.* 1997;336(26):1855-9. [PubMed 9187068](https://pubmed.ncbi.nlm.nih.gov/9187068/)
[^yan-2012-ntcp-receptor]: Yan H, Zhong G, Xu G, et al. Sodium taurocholate cotransporting polypeptide is a functional receptor for human hepatitis B and D virus. *eLife.* 2012;1:e00049. [doi:10.7554/eLife.00049](https://doi.org/10.7554/eLife.00049)
