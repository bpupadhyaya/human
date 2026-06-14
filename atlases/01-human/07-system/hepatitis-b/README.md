---
schema: human-scale-entry/v1
id: hepatitis-b
name: Hepatitis B
atlas: 01-human
scale: 07-system
status: draft
last_reviewed: 2026-06-08
summary: "HBV (hepadnavirus; RC-DNA; 3.2 kb) infects 296M people; replicates via pgRNA/reverse transcriptase; tenofovir/entecavir suppress but do not clear cccDNA; HBeAg seroconversion marks immune control; 50-55% of global HCC; functional cure (HBsAg loss) is emerging treatment goal."
aliases: ["HBV", "hepatitis B virus", "chronic hepatitis B", "CHB", "HBsAg", "HBeAg", "cccDNA HBV", "tenofovir HBV", "entecavir", "HBV cirrhosis", "HBV HCC", "hepadnavirus", "Dane particle", "hepatitis B vaccine", "NTCP receptor"]
sources:
  - id: terrault-2018-hbv-aasld
    type: peer-reviewed
    cite: "Terrault NA, Lok ASF, McMahon BJ, et al. Update on prevention, diagnosis, and treatment of chronic hepatitis B: AASLD 2018 hepatitis B guidance. Hepatology. 2018;67(4):1560-1599."
    doi: "10.1002/hep.29800"
    pmid: "29405329"
    url: "https://doi.org/10.1002/hep.29800"
    accessed: "2026-06-08"
  - id: schweitzer-2015-hbv-prevalence
    type: peer-reviewed
    cite: "Schweitzer A, Horn J, Mikolajczyk RT, Krause G, Ott JJ. Estimations of worldwide prevalence of chronic hepatitis B virus infection: a systematic review of data published between 1965 and 2013. Lancet. 2015;386(10003):1546-1555."
    doi: "10.1016/S0140-6736(15)61412-X"
    pmid: "26231459"
    url: "https://doi.org/10.1016/S0140-6736(15)61412-X"
    accessed: "2026-06-08"
cross_links:
  - target: 01-human/03-molecular/cccdna
    relation: connects-to
    note: "HBV RC-DNA converts to cccDNA in hepatocyte nucleus → chromatinized minichromosome → templates all HBV transcripts including pgRNA; cccDNA persists for decades and is not cleared by tenofovir/entecavir; cccDNA elimination is the goal of curative HBV therapy."
  - target: 01-human/03-molecular/cgas-sting
    relation: connects-to
    note: "HBV RC-DNA and cccDNA activate cGAS → cGAMP → STING → IFN-β; HBx protein binds and inhibits STING → suppresses innate sensing; HBsAg vesicles also activate cGAS; cGAS-STING inhibition by HBx is a key mechanism of HBV innate immune evasion and chronicity."
  - target: 01-human/03-molecular/nf-kb
    relation: connects-to
    note: "HBx protein activates NF-κB → hepatocyte survival, HBV transcription from cccDNA, and inflammatory cytokine production; NF-κB activation by HBx prevents apoptosis of HBV-infected hepatocytes → viral persistence; NF-κB and AP-1 bind cccDNA promoters to enhance HBV replication."
  - target: 01-human/03-molecular/tgf-beta
    relation: connects-to
    note: "Chronic HBV hepatitis activates stellate cells via TGF-β1 → myofibroblast → collagen I/III → fibrosis → cirrhosis → HCC risk; TGF-β suppresses HBV-specific CD8+ T cells → immune exhaustion; TGF-β receptor inhibitors reduce HBV-induced fibrosis in preclinical models."
  - target: 01-human/07-system/hcc
    relation: connects-to
    note: "HBV causes ~50-55% of global HCC; mechanism: HBV integration near TERT/CCND1 → insertional mutagenesis; HBx transactivation → p53 inactivation, NF-κB, Wnt/β-catenin; HBsAg-positive cirrhosis has ~3-5%/year HCC incidence; antiviral therapy reduces but does not eliminate HCC risk."
  - target: 02-pathogen/01-viruses/hepatitis-b-virus
    relation: connects-to
    note: "Hepatitis B virus, a hepadnavirus, enters hepatocytes via NTCP and forms a nuclear cccDNA minichromosome that nucleoside analogs suppress but cannot clear; its HBx protein drives immune evasion and oncogenesis, and a recombinant HBsAg vaccine prevents infection."
  - target: 01-human/06-organ/liver
    relation: connects-to
    note: "Chronic hepatitis B inflames the liver — immune-mediated hepatocyte killing drives fibrosis and cirrhosis and makes HBV the leading infectious cause of hepatocellular carcinoma; antivirals cut but don't abolish HCC risk, mandating 6-monthly surveillance in cirrhosis."
  - target: 01-human/04-cellular/hepatocyte
    relation: connects-to
    note: "HBV is hepatotropic, entering hepatocytes through the bile-acid transporter NTCP; inside, RC-DNA becomes the persistent nuclear cccDNA that templates all viral RNAs, while HBx inactivates p53 and degrades the Smc5/6 restriction complex to keep the infected hepatocyte alive."
  - target: 01-human/07-system/hepatitis-c
    relation: connects-to
    note: "HBV and HCV both cause chronic hepatitis → cirrhosis → HCC but differ: HBV is a DNA virus with a persistent nuclear cccDNA reservoir that antivirals suppress but cannot clear; HCV is an RNA virus with no reservoir, cured >95% by DAAs; HBV is vaccine-preventable, HCV is not."
  - target: 01-human/03-molecular/p53
    relation: connects-to
    note: "HBx binds the p53 C-terminal regulatory domain → sequesters p53 in the cytoplasm → blocks PUMA/BAX-driven apoptosis so the infected hepatocyte survives; with HBV integration and aflatoxin-B1 TP53 R249S mutation, p53 inactivation is central to HBV hepatocarcinogenesis."
  - target: 01-human/04-cellular/t-cytotoxic-cell
    relation: connects-to
    note: "HBV-specific CD8+ cytotoxic T cells clear infected hepatocytes and, via non-cytolytic IFN-γ/TNF, suppress HBV transcription; in chronic HBV these CTLs become exhausted (PD-1, TIM-3, LAG-3) → failure to clear cccDNA → viral persistence."
  - target: 01-human/07-system/hiv-aids
    relation: connects-to
    note: "HBV and HIV share transmission routes and frequently coinfect: shared blood and sexual spread means many HIV patients carry HBV, accelerating fibrosis, and several drugs (tenofovir, lamivudine) treat both—so HIV regimens are chosen to cover HBV."
  - target: 01-human/04-cellular/macrophage
    relation: connects-to
    note: "Liver macrophages (Kupffer cells) shape hepatitis B outcomes: they sense viral products and present antigen, and the balance between cytotoxic T-cell clearance and macrophage-driven chronic inflammation decides whether HBV is cleared or smolders into fibrosis and cancer."
  - target: 01-human/07-system/anca-vasculitis
    relation: connects-to
    note: "Hepatitis B is classically linked to polyarteritis nodosa, not ANCA-associated vasculitis: circulating HBsAg immune complexes deposit in medium-sized arteries, so HBV-related PAN is immune-complex-driven and ANCA-negative—a key distinction from primary ANCA vasculitis."
  - target: 01-human/07-system/cholangiocarcinoma
    relation: connects-to
    note: "Hepatitis B raises cholangiocarcinoma risk, not just hepatocellular carcinoma: chronic HBV inflammation and cirrhosis can transform biliary epithelium too, making HBV a recognized risk factor for intrahepatic cholangiocarcinoma."
  - target: 01-human/04-cellular/natural-killer-cell
    relation: connects-to
    note: "Natural killer cells are key to controlling hepatitis B: NK cells provide early antiviral defense, but in chronic HBV they become functionally exhausted, contributing to viral persistence—so restoring NK and T-cell function is a goal of functional-cure strategies."
  - target: 01-human/07-system/immune-system
    relation: connects-to
    note: "Chronic hepatitis B is a disease of immune tolerance and exhaustion: whether HBV is cleared or becomes chronic depends on the host immune response—HBV outcomes are written by the immune system as much as the virus."
  - target: 01-human/03-molecular/type-i-interferon
    relation: connects-to
    note: "Type I interferon is both HBV's target and a therapy: HBV actively suppresses hepatocyte interferon induction to establish chronicity, and pegylated interferon-alpha—one of the few finite-course treatments—can drive HBsAg loss in a minority of patients."
  - target: 01-human/04-cellular/dendritic-cell
    relation: connects-to
    note: "HBV blunts dendritic cells to evade immunity: impaired antigen presentation and weak plasmacytoid-DC interferon output cripple the priming of antiviral T cells, helping explain why neonatal and chronic infection so often becomes a tolerant, persistent carrier state."
  - target: 01-human/07-system/nash
    relation: connects-to
    note: "Hepatitis B and NASH increasingly coexist and compound liver injury: metabolic steatohepatitis adds inflammation and fibrosis on top of viral damage, accelerating cirrhosis and liver cancer, so metabolic risk factors matter even in well-suppressed HBV."
  - target: 01-human/04-cellular/b-cell
    relation: connects-to
    note: "B cells decide hepatitis B's outcome: antibodies to the surface antigen (anti-HBs) neutralize the virus and are what the vaccine induces, so seroconversion from HBsAg to anti-HBs marks recovery and protective immunity—the basis of the first anti-cancer vaccine."
  - target: 01-human/05-tissue/fibrosis
    relation: connects-to
    note: "Chronic hepatitis B scars the liver toward cirrhosis: persistent immune attack on infected hepatocytes activates stellate cells to lay down collagen, so years of smoldering inflammation build the fibrosis that underlies liver failure and cancer risk."
  - target: 01-human/06-organ/kidney
    relation: connects-to
    note: "Hepatitis B can attack the kidney: deposited viral antigen-antibody complexes cause membranous nephropathy (especially in children), presenting as nephrotic-range protein loss—an immune-complex complication that can improve when the virus is suppressed."
  - target: 01-human/06-organ/placenta
    relation: connects-to
    note: "Most chronic hepatitis B starts at birth via the placenta: perinatal mother-to-child transmission causes lifelong infection far more often than adult exposure, so birth-dose vaccine plus antivirals in highly viremic mothers is the key to prevention."
  - target: 01-human/04-cellular/t-helper-cell
    relation: connects-to
    note: "Clearing hepatitis B hinges on T-helper cells: a strong CD4 response orchestrates the CD8 and antibody attack that resolves acute infection, while a weak, exhausted helper response lets HBV persist as chronic infection."
  - target: 01-human/04-cellular/regulatory-t-cell
    relation: connects-to
    note: "Regulatory T cells help hepatitis B persist: in chronic infection, expanded Tregs dampen the antiviral T-cell attack, contributing to immune tolerance of the virus—the flip side of the helper response needed to clear it."
---

# Hepatitis B

## Overview

**Hepatitis B** is a chronic liver disease caused by the **hepatitis B virus (HBV)** — a partially double-stranded relaxed circular DNA (RC-DNA) virus of the family *Hepadnaviridae* (genus *Orthohepadnavirus*). With an estimated **296 million people chronically infected** globally and 820,000 deaths annually, primarily from cirrhosis and hepatocellular carcinoma (HCC), HBV remains one of the most consequential viral pathogens in human history [^schweitzer-2015-hbv-prevalence]. The first recombinant vaccine against HBV (1982) was simultaneously the first cancer-prevention vaccine.

HBV is unique among human DNA viruses in that it **replicates via reverse transcription** of a pregenomic RNA (pgRNA) intermediate. This RNA-intermediate strategy, combined with the formation of a stable nuclear episomal reservoir — **covalently closed circular DNA (cccDNA)** — means that existing nucleoside reverse transcriptase inhibitors (NRTIs) can suppress viremia but cannot clear established infection. The **therapeutic frontier** is elimination of cccDNA: a "functional cure" (HBsAg loss) in which cccDNA is silenced or eliminated so that hepatitis B surface antigen (HBsAg) becomes undetectable.

**Clinical phases of chronic HBV:**
- **Immune tolerant**: HBeAg+, HBV DNA >1 million IU/mL, normal ALT, minimal liver injury; common in perinatally infected patients; high transmission risk
- **HBeAg+ immune active** (immune clearance): HBV DNA high, elevated ALT, active necro-inflammation and fibrogenesis; treatment indicated
- **HBeAg− inactive carrier**: HBV DNA <2,000 IU/mL, normal ALT, minimal fibrosis; low HCC risk but HBsAg+ means cccDNA persists
- **HBeAg− chronic hepatitis B**: HBV DNA >2,000 IU/mL variable, elevated ALT; driven by precore/BCP mutants that eliminate HBeAg production while maintaining replication
- **HBsAg loss** (functional cure): spontaneous 1-2%/year; pegIFN can increase; target of curative therapy

**Epidemiology:**
- Global: 296 million chronic infections; highest burden in sub-Saharan Africa, East and Southeast Asia
- Transmission: perinatal (dominant in Asia — infant HBV vaccination critical); sexual; blood-to-blood
- Perinatal transmission: ~90% of perinatally infected neonates become chronic; only 5-10% of adult-acquired infections become chronic
- Vaccination: HBsAg subunit vaccine; WHO-recommended birth dose + 2 infant doses; >95% protection; no booster needed for immunocompetent persons

## Structure

### HBV biology

HBV is an enveloped virus (~42 nm Dane particle; subviral HBsAg particles are 22 nm spheres/tubules, vastly outnumber virions):

- **Genome**: 3.2 kb partially double-stranded relaxed circular DNA (RC-DNA); negative-sense (-) strand complete; positive-sense (+) strand incomplete (variable length)
- **Four overlapping open reading frames** encode all proteins from the same compact genome

| Protein | Function |
|---------|----------|
| HBsAg (L, M, S) | Three envelope proteins from same ORF; L-HBsAg preS1 domain binds NTCP receptor; HBsAg loss = functional cure; S-HBsAg is diagnostic antigen |
| HBcAg / HBeAg | Core/capsid protein; HBeAg is HBcAg precursor secreted → immunomodulatory; anti-HBe seroconversion marks immune control |
| Pol (P) | Multidomain: terminal protein (primes DNA synthesis) + spacer + reverse transcriptase (RT) + RNase H; target of NRTIs |
| HBx | Transactivator (no enzymatic domain); activates NF-κB; inhibits STING; inactivates p53; activates Wnt/β-catenin; required for cccDNA transcription |

### HBV entry

HBV entry requires the **sodium-taurocholate cotransporting polypeptide (NTCP; SLC10A1)** on hepatocytes as the functional receptor:

1. L-HBsAg preS1 peptide (aa 2-48) binds NTCP
2. Clathrin-mediated endocytosis → escape to cytoplasm → nucleocapsid
3. Nuclear pore complex → RC-DNA delivered to nucleus
4. Host enzymes (PCNA/DNA polymerase, topoisomerase II, DNA ligase) convert RC-DNA → cccDNA
5. cccDNA chromatinized → minichromosome → transcribed by RNA Pol II

**Therapeutic implication**: Bulevirtide (NTCP inhibitor) is approved in EU for chronic HBV+HDV — blocks HBV/HDV cell entry.

## Function

### HBV replication cycle

1. **Nuclear cccDNA** serves as transcriptional template → pgRNA (3.5 kb), preC RNA (→HBeAg), 2.4/2.1 kb (→L/S HBsAg), 0.7 kb (→HBx)
2. **Cytoplasmic replication**: pgRNA + Pol packaged into nucleocapsid → Pol uses terminal protein domain to prime (-) strand synthesis (via protein primer, not RNA primer) → pgRNA reverse-transcribed → RC-DNA; RNase H degrades pgRNA template
3. **Nuclear recycling**: Some nucleocapsids re-import to nucleus → additional cccDNA copies (~5-50/hepatocyte)
4. **Virion assembly**: Other nucleocapsids enveloped at ER by HBsAg → secreted Dane particles

### Immune response and evasion

| Component | Host response | HBV counter |
|-----------|--------------|-------------|
| cGAS-STING | Detects RC-DNA/cccDNA → IFN-β | HBx binds and inhibits STING; minimizes cytosolic DNA exposure |
| RIG-I/MAVS | Detects dsRNA replication intermediates → IFN-β | Nucleocapsid sequesters dsRNA; HBx inhibits MAVS signaling |
| CD8+ T cells | HBV-specific CTLs clear infected hepatocytes | T cell exhaustion (PD-1, TIM-3, LAG-3 upregulation) in chronic HBV |
| CD4+ T cells | Th1 → IFN-γ, IL-2 → CD8+ help | HBeAg immune tolerance during immune-tolerant phase |
| Type I IFN | Antiviral ISG induction | NS4B analog (HBV polyprotein) blocks IFN signaling; low IFN-α/β in chronic HBV |

### HBx protein — master transactivator

HBx is essential for HBV replication and oncogenesis:
- **NF-κB activation**: HBx → IKKα/β → IκBα degradation → NF-κB → hepatocyte survival, pro-inflammatory cytokines, cccDNA promoter activation
- **p53 inactivation**: HBx binds p53 C-terminal regulatory domain → sequesters p53 in cytoplasm → blocks PUMA/BAX pro-apoptotic transcription → infected hepatocyte survives
- **STING inhibition**: HBx binds and degrades STING → impaired cGAS-STING-IFN-β response to HBV DNA
- **Wnt activation**: HBx inhibits GSK-3β → β-catenin not phosphorylated → nuclear β-catenin → TCF/LEF → MYC, cyclin D1 → hepatocyte proliferation → HCC promotion
- **Smc5/6 restriction**: HBx hijacks DDB1-CRL4 ubiquitin ligase → degrades Smc5/6 complex that restricts cccDNA transcription → enables robust cccDNA-driven HBV transcription

## Pathology

### HBV-related hepatocellular carcinoma (HCC)

HBV is the **leading infectious cause of cancer worldwide**, accounting for ~50-55% of global HCC:

- **Insertional mutagenesis**: HBV integrates (randomly) near TERT promoter (most common), CCND1, MLL4, FN1, HBsAg-SLC35A5 → TERT promoter activation → telomerase → replicative immortality; CCND1 integration → cyclin D1 overexpression
- **HBx oncogenesis**: Constitutive p53 inactivation; NF-κB/STAT3 survival signaling; Wnt/β-catenin activation; epigenetic dysregulation (promoter hypermethylation via DNMT3A)
- **Co-carcinogens**: Aflatoxin B1 (AFB1; in sub-Saharan Africa/SE Asia) → CYP450 → AFB1-epoxide → TP53 R249S hotspot mutation + HBV integration = multiplicative HCC risk
- **HCC driver mutations** in HBV-HCC: TERT promoter (>50%), TP53 (~30-40%), CTNNB1 (~20-25%), AXIN1 (~10%)

**HCC surveillance** (AASLD 2018): Ultrasound ± AFP every 6 months for HBsAg+ patients with cirrhosis OR HBsAg+ patients with HCC risk score ≥10 (PAGE-B score) even without cirrhosis.

### Hepatitis D (HDV) co-infection

HDV is a satellite RNA virus that requires HBsAg for virion assembly:
- Co-infection (simultaneous HBV+HDV): usually self-limiting; < 5% chronic HDV
- Superinfection (HDV in chronic HBV+): ~80% chronic HDV; accelerated cirrhosis (3-5× faster); highest HCC risk of any viral hepatitis
- Treatment: Bulevirtide (NTCP inhibitor, EU-approved 2020) blocks both HBV and HDV entry; pegIFN-λ (investigational)

### Diagnosis

| Test | Interpretation |
|------|---------------|
| HBsAg+ | Active HBV infection (acute or chronic) |
| Anti-HBs+ | Immune (vaccination or resolved infection) |
| HBeAg+ | High viral replication; high infectivity |
| Anti-HBe+ | Reduced replication (seroconversion milestone) |
| Anti-HBc IgM | Acute HBV or reactivation |
| HBV DNA (IU/mL) | Viral load; guides treatment; goal <20 IU/mL on therapy |
| HBV genotype | A-H; affects pegIFN response; A/B > C/D to pegIFN; C/D more common in Asia |

### Treatment

**Antiviral therapy indications** (AASLD 2018): HBV DNA >2,000 IU/mL + elevated ALT; or HBV DNA >20,000 + any ALT; or cirrhosis + any detectable HBV DNA; or HCC regardless of HBV DNA.

| Agent | Class | HBV DNA suppression | cccDNA | Notes |
|-------|-------|---------------------|--------|-------|
| **Tenofovir alafenamide (TAF)** | NRTI | >99%; high barrier to resistance | Not cleared | Preferred; lower renal/bone toxicity than TDF |
| **Tenofovir disoproxil fumarate (TDF)** | NRTI | >99%; high barrier | Not cleared | Preferred in pregnancy (safety data); lower cost |
| **Entecavir (ETV)** | NRTI | >99%; high barrier | Not cleared | Preferred; no resistance in treatment-naive |
| **Pegylated IFN-α-2a** | Immunomodulator | ~25-40% HBeAg loss | May reduce cccDNA | 48 weeks finite; ~3-7% HBsAg loss; HCV genotype A/B best |
| **Bulevirtide** | NTCP inhibitor | + reduces HDV | Not cleared | EU-approved for HBV+HDV |

**Novel agents in trials (curative pipeline):**
- **Capsid assembly modulators (CAMs)**: JNJ-6379, ABI-H0731 → prevent pgRNA encapsidation → block new cccDNA synthesis
- **siRNA / ASO targeting HBsAg**: Interferon alfa-loaded RNAi (JNJ-3989, VIR-2218, RG6346) → reduce HBsAg → restore immune recognition
- **Core protein allosteric modulators (CPAMs)**: Inhibit nucleocapsid assembly; some also destabilize cccDNA
- **TLR7/8 agonists**: Innate immune activation → IFN-α/APOBEC3 → non-cytolytic cccDNA deamination/clearance
- **CRISPR/Cas9**: Direct cccDNA cutting (preclinical); specificity challenges remain

## Connections

**→ [cccDNA](../../../03-molecular/cccdna/)**: HBV RC-DNA converts to cccDNA in hepatocyte nucleus → chromatinized minichromosome → templates all HBV transcripts including pgRNA and subgenomic RNAs; cccDNA persists for decades and is not cleared by tenofovir/entecavir; approximately 5–50 copies per hepatocyte; cccDNA elimination is the goal of curative HBV therapy.

**→ [cGAS-STING](../../../03-molecular/cgas-sting/)**: HBV RC-DNA and cccDNA activate cGAS → cGAMP → STING → TBK1/IRF3 → IFN-β; HBx protein binds and inhibits STING at the palmitoylation site → suppresses innate sensing; HBsAg-containing subviral particles also activate cGAS; cGAS-STING agonists are being investigated as curative HBV therapy to stimulate APOBEC3-mediated cccDNA clearance.

**→ [NF-κB](../../../03-molecular/nf-kb/)**: HBx protein activates NF-κB → hepatocyte survival, HBV transcription from cccDNA, and pro-inflammatory cytokine production; NF-κB activation by HBx prevents apoptosis of HBV-infected hepatocytes → viral persistence; NF-κB and AP-1 binding sites on cccDNA promoters are critical for robust HBV transcription; NF-κB also drives HBV-associated liver inflammation.

**→ [TGF-β](../../../03-molecular/tgf-beta/)**: Chronic HBV hepatitis activates hepatic stellate cells via TGF-β1 from Kupffer cells and hepatocytes → myofibroblast transdifferentiation → collagen I/III deposition → progressive fibrosis → cirrhosis → HCC risk; TGF-β also suppresses HBV-specific CD8+ T cells → immune exhaustion → viral persistence; TGF-β receptor inhibitors (galunisertib) reduce HBV-induced hepatic fibrosis in preclinical models.

**→ [HCC](../hcc/)**: HBV is the leading viral cause of HCC (~50-55% of global cases); mechanisms include insertional mutagenesis near TERT/CCND1, HBx transactivation activating p53 inactivation and Wnt/β-catenin, and aflatoxin B1 co-exposure generating TP53 R249S hotspot; HBsAg-positive cirrhosis carries ~3-5%/year HCC incidence; tenofovir/entecavir reduce HCC risk ~70% but do not eliminate it, requiring continued 6-monthly surveillance.

- `connects-to` → **[Hepatitis B Virus](../../../02-pathogen/01-viruses/hepatitis-b-virus/README.md)** — Hepatitis B virus, a hepadnavirus, enters hepatocytes via NTCP and forms a nuclear cccDNA minichromosome that nucleoside analogs suppress but cannot clear; its HBx protein drives immune evasion and oncogenesis, and a recombinant HBsAg vaccine prevents infection.
- `connects-to` → **[Liver](../../06-organ/liver/README.md)** — Chronic hepatitis B inflames the liver — immune-mediated hepatocyte killing drives fibrosis and cirrhosis and makes HBV the leading infectious cause of hepatocellular carcinoma; antivirals cut but don't abolish HCC risk, mandating 6-monthly surveillance in cirrhosis.
- `connects-to` → **[Hepatocyte](../../04-cellular/hepatocyte/README.md)** — HBV is hepatotropic, entering hepatocytes through the bile-acid transporter NTCP; inside, RC-DNA becomes the persistent nuclear cccDNA that templates all viral RNAs, while HBx inactivates p53 and degrades the Smc5/6 restriction complex to keep the infected hepatocyte alive.
- `connects-to` → **[Hepatitis C](../hepatitis-c/README.md)** — HBV and HCV both cause chronic hepatitis → cirrhosis → HCC but differ: HBV is a DNA virus with a persistent nuclear cccDNA reservoir that antivirals suppress but cannot clear; HCV is an RNA virus with no reservoir, cured >95% by DAAs; HBV is vaccine-preventable, HCV is not.
- `connects-to` → **[p53](../../03-molecular/p53/README.md)** — HBx binds the p53 C-terminal regulatory domain → sequesters p53 in the cytoplasm → blocks PUMA/BAX-driven apoptosis so the infected hepatocyte survives; with HBV integration and aflatoxin-B1 TP53 R249S mutation, p53 inactivation is central to HBV hepatocarcinogenesis.
- `connects-to` → **[Cytotoxic T Cell](../../04-cellular/t-cytotoxic-cell/README.md)** — HBV-specific CD8+ cytotoxic T cells clear infected hepatocytes and, via non-cytolytic IFN-γ/TNF, suppress HBV transcription; in chronic HBV these CTLs become exhausted (PD-1, TIM-3, LAG-3) → failure to clear cccDNA → viral persistence.
- `connects-to` → **[HIV/AIDS](../hiv-aids/README.md)** — HBV and HIV share transmission routes and frequently coinfect: shared blood and sexual spread means many HIV patients carry HBV, accelerating fibrosis, and several drugs (tenofovir, lamivudine) treat both—so HIV regimens are chosen to cover HBV.
- `connects-to` → **[Macrophage](../../04-cellular/macrophage/README.md)** — Liver macrophages (Kupffer cells) shape hepatitis B outcomes: they sense viral products and present antigen, and the balance between cytotoxic T-cell clearance and macrophage-driven chronic inflammation decides whether HBV is cleared or smolders into fibrosis and cancer.
- `connects-to` → **[ANCA Vasculitis](../anca-vasculitis/README.md)** — Hepatitis B is classically linked to polyarteritis nodosa, not ANCA-associated vasculitis: circulating HBsAg immune complexes deposit in medium-sized arteries, so HBV-related PAN is immune-complex-driven and ANCA-negative—a key distinction from primary ANCA vasculitis.
- `connects-to` → **[Cholangiocarcinoma](../cholangiocarcinoma/README.md)** — Hepatitis B raises cholangiocarcinoma risk, not just hepatocellular carcinoma: chronic HBV inflammation and cirrhosis can transform biliary epithelium too, making HBV a recognized risk factor for intrahepatic cholangiocarcinoma.
- `connects-to` → **[Natural Killer Cell](../../04-cellular/natural-killer-cell/README.md)** — Natural killer cells are key to controlling hepatitis B: NK cells provide early antiviral defense, but in chronic HBV they become functionally exhausted, contributing to viral persistence—so restoring NK and T-cell function is a goal of functional-cure strategies.
- `connects-to` → **[Immune System](../immune-system/README.md)** — Chronic hepatitis B is a disease of immune tolerance and exhaustion: whether HBV is cleared or becomes chronic depends on the host immune response—HBV outcomes are written by the immune system as much as the virus.
- `connects-to` → **[Type I Interferon](../../03-molecular/type-i-interferon/README.md)** — Type I interferon is both HBV's target and a therapy: HBV actively suppresses hepatocyte interferon induction to establish chronicity, and pegylated interferon-alpha—one of the few finite-course treatments—can drive HBsAg loss in a minority of patients.
- `connects-to` → **[Dendritic Cell](../../04-cellular/dendritic-cell/README.md)** — HBV blunts dendritic cells to evade immunity: impaired antigen presentation and weak plasmacytoid-DC interferon output cripple the priming of antiviral T cells, helping explain why neonatal and chronic infection so often becomes a tolerant, persistent carrier state.
- `connects-to` → **[NASH](../nash/README.md)** — Hepatitis B and NASH increasingly coexist and compound liver injury: metabolic steatohepatitis adds inflammation and fibrosis on top of viral damage, accelerating cirrhosis and liver cancer, so metabolic risk factors matter even in well-suppressed HBV.
- `connects-to` → **[B Cell](../../04-cellular/b-cell/README.md)** — B cells decide hepatitis B's outcome: antibodies to the surface antigen (anti-HBs) neutralize the virus and are what the vaccine induces, so seroconversion from HBsAg to anti-HBs marks recovery and protective immunity—the basis of the first anti-cancer vaccine.
- `connects-to` → **[Fibrosis](../../05-tissue/fibrosis/README.md)** — Chronic hepatitis B scars the liver toward cirrhosis: persistent immune attack on infected hepatocytes activates stellate cells to lay down collagen, so years of smoldering inflammation build the fibrosis that underlies liver failure and cancer risk.
- `connects-to` → **[Kidney](../../06-organ/kidney/README.md)** — Hepatitis B can attack the kidney: deposited viral antigen-antibody complexes cause membranous nephropathy (especially in children), presenting as nephrotic-range protein loss—an immune-complex complication that can improve when the virus is suppressed.
- `connects-to` → **[Placenta](../../06-organ/placenta/README.md)** — Most chronic hepatitis B starts at birth via the placenta: perinatal mother-to-child transmission causes lifelong infection far more often than adult exposure, so birth-dose vaccine plus antivirals in highly viremic mothers is the key to prevention.
- `connects-to` → **[T Helper Cell](../../04-cellular/t-helper-cell/README.md)** — Clearing hepatitis B hinges on T-helper cells: a strong CD4 response orchestrates the CD8 and antibody attack that resolves acute infection, while a weak, exhausted helper response lets HBV persist as chronic infection.
- `connects-to` → **[Regulatory T Cell](../../04-cellular/regulatory-t-cell/README.md)** — Regulatory T cells help hepatitis B persist: in chronic infection, expanded Tregs dampen the antiviral T-cell attack, contributing to immune tolerance of the virus—the flip side of the helper response needed to clear it.
- `connects-to` → **[Placenta](../../06-organ/placenta/README.md)** — Most chronic hepatitis B starts at birth via the placenta: perinatal mother-to-child transmission causes lifelong infection far more often than adult exposure, so birth-dose vaccine plus antivirals in highly viremic mothers is the key to prevention.
- `connects-to` → **[T Helper Cell](../../04-cellular/t-helper-cell/README.md)** — Clearing hepatitis B hinges on T-helper cells: a strong CD4 response orchestrates the CD8 and antibody attack that resolves acute infection, while a weak, exhausted helper response lets HBV persist as chronic infection.
- `connects-to` → **[Regulatory T Cell](../../04-cellular/regulatory-t-cell/README.md)** — Regulatory T cells help hepatitis B persist: in chronic infection, expanded Tregs dampen the antiviral T-cell attack, contributing to immune tolerance of the virus—the flip side of the helper response needed to clear it.
