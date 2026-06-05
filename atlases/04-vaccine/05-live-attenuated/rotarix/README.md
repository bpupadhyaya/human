---
schema: vaccine-entry/v1
id: rotarix
name: "Rotarix (RIX4414)"
atlas: 04-vaccine
platform: 05-live-attenuated
status: draft
last_reviewed: 2026-06-05
summary: "Oral live-attenuated human rotavirus vaccine (G1P[8] strain RIX4414); 2-dose series at 2 and 4 months. 85–96% efficacy against severe RVGE in high-income settings; WHO prequalified 2007; deployed in 100+ country immunization programs."
aliases:
  - RIX4414
  - "rotavirus vaccine, live oral"
  - "human rotavirus vaccine"
target_pathogens:
  - target: 02-pathogen/01-viruses/rotavirus
    antigen: "VP7 (G1) and VP4 (P[8]) outer-capsid proteins"
    coverage:
      - "G1P[8] (homotypic)"
      - "G2P[4] (heterotypic, partial)"
      - "G3P[8] (heterotypic, partial)"
      - "G4P[8] (heterotypic, partial)"
      - "G9P[8] (heterotypic, partial)"
antigens:
  - "live attenuated human rotavirus RIX4414 strain (G1P[8])"
delivery_system: "live attenuated human rotavirus in oral liquid formulation"
adjuvants: []
route_of_administration: oral
dose_schedule:
  primary_series: "2 doses at 2 and 4 months of age (oral)"
  notes: "First dose must be given between 6 and 12 weeks of age; series must be completed by 24 weeks of age per WHO guidance"
manufacturer:
  developer: "GlaxoSmithKline (GSK)"
  production_sites: "GSK Biologicals, Rixensart, Belgium"
regulatory_status:
  - body: "WHO"
    status: "Prequalified"
    date: "2007"
  - body: "FDA (USA)"
    status: "Approved"
    date: "2008"
  - body: "EMA"
    status: "Approved"
    date: "2006"
cold_chain: "2–8°C; must NOT be frozen; oral applicator stored refrigerated; shelf life ~3 years"
discontinued: false
tags:
  - rotarix
  - rotavirus
  - live-attenuated
  - oral-vaccine
  - pediatric
  - gastroenteritis
  - rix4414
  - mucosal-immunity
  - secretory-iga
  - g1p8
sources:
  - id: vesikari-2006-nejm-rotarix-efficacy
    type: peer-reviewed
    cite: "Vesikari T, Karvonen A, Prymula R, et al. Efficacy of human rotavirus vaccine against rotavirus gastroenteritis during the first 2 years of life in European infants: randomised, double-blind controlled study. Lancet. 2007;370(9601):1757-1763."
    doi: "10.1016/S0140-6736(07)61744-9"
    pmid: "18037080"
    note: "Pivotal European phase III trial; 96.4% efficacy against severe rotavirus gastroenteritis (Vesikari score ≥11); formed basis for EMA/FDA approval."
  - id: madhi-2010-nejm-rotarix-africa
    type: peer-reviewed
    cite: "Madhi SA, Cunliffe NA, Steele D, et al. Effect of Human Rotavirus Vaccine on Severe Diarrhea in African Infants. N Engl J Med. 2010;362(4):289-298."
    doi: "10.1056/NEJMoa0904741"
    pmid: "20107215"
    note: "African phase III trial (South Africa, Malawi); 49% overall efficacy but 61% efficacy in South Africa vs 49% in Malawi; confirmed reduced efficacy in high-mortality settings."
  - id: who-rotarix-position-paper-2013
    type: who-guidance
    cite: "World Health Organization. Rotavirus vaccines WHO position paper – January 2013. Wkly Epidemiol Rec. 2013;88(5):49-64."
    url: "https://www.who.int/publications/i/item/WER8805"
    note: "WHO recommendation for universal infant rotavirus vaccination; SAGE review of efficacy, safety, and benefit-risk across income settings."
  - id: intusussception-who-gacvs-2011
    type: who-guidance
    cite: "Global Advisory Committee on Vaccine Safety. Rotavirus vaccines and intussusception. Wkly Epidemiol Rec. 2011;86(22):225-226."
    url: "https://www.who.int/publications/i/item/WER8622"
    note: "GACVS review of post-licensure intussusception signal; concluded excess risk ~1–2 per 100,000 doses; benefit-risk clearly favors vaccination globally."
  - id: jiang-2010-plos-one-pcv1-rotarix
    type: peer-reviewed
    cite: "Victoria JG, Wang C, Jones MS, et al. Viral Nucleic Acids in Live-Attenuated Vaccines: Detection of Minority Variants and an Adventitious Virus. J Virol. 2010;84(12):6033-6040."
    doi: "10.1128/JVI.02690-09"
    pmid: "20375157"
    note: "Detection of porcine circovirus type 1 (PCV1) DNA in Rotarix by deep sequencing; triggered 2010 temporary suspension by FDA; PCV1 deemed non-pathogenic to humans."
  - id: burnett-2020-elife-rotarix-lowefficiency
    type: peer-reviewed
    cite: "Burnett E, Parashar UD, Tate JE. Real-world effectiveness of rotavirus vaccines, 2006–19: a literature review and meta-analysis. Lancet Glob Health. 2020;8(9):e1195-e1202."
    doi: "10.1016/S2214-109X(20)30262-X"
    pmid: "32800145"
    note: "Meta-analysis of 57 studies; high-income efficacy 85–96%; lower-middle-income 63%; low-income ~40–60%; consistent with pre-licensure trial data."
cross_links:
  - target: 02-pathogen/01-viruses/rotavirus
    relation: prevents
    note: "G1P[8] live strain elicits VP7/VP4 neutralizing antibodies and mucosal IgA; 85–96% efficacy against severe RVGE in high-income settings; heterotypic protection against G2–G4, G9 strains via cross-reactive immunity."
  - target: 01-human/07-system/immune-system
    relation: elicits
    note: "Drives mucosal and systemic immunity: intestinal IgA secretion, serum IgG and IgA, rotavirus-specific CD4+ and CD8+ T-cell responses; innate activation via dsRNA (TLR3/MDA5) and NSP4 enterotoxin signaling."
  - target: 01-human/04-cellular/t-helper-cell
    relation: elicits
    note: "Th1/Th2 mixed CD4+ response; Th2-skewed IgA class-switching in Peyer's patches and mesenteric lymph nodes; Tfh cells support germinal center B-cell maturation for high-affinity anti-VP7/VP4 antibody production."
  - target: 01-human/06-organ/small-intestine
    relation: replicates-in
    note: "Oral attenuated virus colonizes small-intestinal epithelium transiently; infects enterocytes and M cells overlying Peyer's patches; local antigen presentation drives lamina propria IgA plasma cell differentiation."
---

# Rotarix (RIX4414)

## Overview

**Rotarix** is an oral live-attenuated rotavirus vaccine developed by **GlaxoSmithKline (GSK)**, derived from a single human rotavirus strain of serotype **G1P[8]** — the most globally prevalent rotavirus genotype, responsible for approximately 70–80% of rotavirus gastroenteritis (RVGE) cases in high-income countries and a substantial fraction worldwide. The vaccine strain, designated **RIX4414**, was attenuated by serial passage of a natural human isolate in Vero cells under defined laboratory conditions, selecting for variants with reduced intestinal replication fidelity while retaining immunogenicity and the capacity to replicate transiently in the infant gut after oral administration.

Rotarix received **EMA approval in 2006**, **FDA approval in 2008**, and was **WHO-prequalified in 2007** — now included in the Expanded Program on Immunization (EPI) of over **100 countries**. It is one of two globally dominant rotavirus vaccines; the other is **RotaTeq** (Merck), a pentavalent bovine-human reassortant vaccine containing G1, G2, G3, G4, and P[8] antigens administered as a 3-dose oral series.

Rotavirus remains the **leading cause of severe diarrheal disease in children under five** worldwide. Before universal vaccination, it caused approximately **528,000 child deaths annually** (WHO 2008 estimate), predominantly in South Asia and sub-Saharan Africa. Post-vaccination data (2006–2019 meta-analysis) document substantial real-world reduction in rotavirus hospitalizations in all settings where Rotarix has been introduced, though absolute protection is markedly lower in high-mortality, low-income countries — a phenomenon whose mechanistic basis remains one of the central open questions in pediatric vaccinology.

**Comparator vaccine — RotaTeq:**

RotaTeq (Merck; pentavalent bovine-human reassortant, G1–G4/P[8]) differs from Rotarix in three key respects: (1) it contains 5 reassortant strains rather than a single human strain; (2) it is given as a 3-dose series rather than 2 doses; (3) it uses bovine rotavirus backbone genes rather than a fully human strain. Both vaccines show comparable overall efficacy in high-income countries (~85–98% against severe RVGE) and comparable — and comparably disappointing — efficacy in low-income settings (~40–60%). Head-to-head comparative efficacy data are limited; country selection of one versus the other typically reflects cost, cold-chain volume, and national procurement agreements rather than strong evidence of differential effectiveness.

## Antigen & Formulation

**Viral strain and attenuation:**

The RIX4414 strain was derived from a **human G1P[8] rotavirus isolate** and attenuated by approximately 30–35 serial passages in Vero cells. Rotavirus is a non-enveloped, triple-layered icosahedral virus with an 11-segment double-stranded RNA (dsRNA) genome. The outer capsid contains two immunodominant proteins:

- **VP7** (glycoprotein; G-type antigen): the major target of serotype-specific neutralizing antibodies; RIX4414 expresses the G1 VP7 serotype
- **VP4** (protease-cleaved protein; P-type antigen): cleaved by intestinal trypsin into VP8* and VP5*; VP8* contains the sialic acid / HBGA binding domain; VP4 P[8] genotype elicits broadly cross-reactive neutralizing antibodies

Rotarix elicits **both homotypic neutralizing antibodies** (anti-G1, anti-P[8]) and **heterotypic cross-reactive antibodies** against G2, G3, G4, G9, and G12 strains — a degree of cross-serotype protection confirmed in clinical trials and post-licensure surveillance. The mechanism of heterotypic protection involves cross-reactive epitopes on VP4/P[8] shared across most circulating strains, and possibly on conserved inner-capsid proteins (VP6, VP2) that are not classical neutralization targets but may mediate non-neutralizing protective immunity via IgA.

**Formulation:**

Rotarix is supplied as a **lyophilized powder** (in some markets) or as a **liquid formulation** in a prefilled oral applicator. The liquid applicator (approved in the US and many markets) is a single-use 1.5 mL oral syringe containing the reconstituted vaccine in a calcium carbonate/sucrose buffer at neutral pH to protect the virus from gastric acid. No latex; no adjuvant. The calcium carbonate acts as a **gastric acid neutralizer**, raising gastric pH transiently to protect the live virus from acid denaturation during transit to the small intestine — a critical formulation consideration absent from parenteral vaccines. Each dose contains ≥ 10^6 CCID₅₀ (50% cell-culture infectious dose) of live RIX4414 virus.

**Dose schedule and age constraints:**

The 2-dose series is given at **2 months and 4 months of age**. WHO and national guidelines impose strict age limits:
- First dose: **6–12 weeks of age** (not before 6 weeks; no data for delayed first dose after 12 weeks)
- Second dose: ≥4 weeks after first dose
- Series completion: **by 24 weeks of age** (US: by 8 months per ACIP; WHO: by 6 months)

These constraints exist because older infants (>32 weeks) had a small but measurable elevated intussusception risk in post-marketing surveillance, linked to the age-dependent susceptibility of the intestinal lymphoid tissue to ileocecal invagination (see Safety section). The age restrictions effectively ensure the vaccine is given during the developmental window when intussusception baseline risk is lowest.

**Cold chain:**

Rotarix is stored at **2–8°C and must not be frozen**. Unlike the lyophilized BCG, freezing inactivates the liquid Rotarix formulation irreversibly. Vial Monitor (VVM) indicators are used in GAVI/Unicef supply-chain contexts.

## Immunogenicity

**Mucosal immune response — the primary protective arm:**

Oral live-attenuated rotavirus vaccines elicit protection primarily through **intestinal mucosal immunity**, fundamentally different from the systemic cellular immunity that is the correlate of protection for BCG or parenteral vaccines. After oral administration, the attenuated RIX4414 virus replicates transiently in small-intestinal epithelial cells and, critically, in **M cells overlying the Peyer's patches** — specialized follicle-associated epithelial cells that sample luminal antigens and deliver them to underlying dendritic cells and B cells in the subepithelial dome.

The mucosal immune cascade proceeds as follows:

1. **Antigen uptake:** M cells and follicular dendritic cells in Peyer's patches take up rotavirus particles and deliver viral antigens (VP7, VP4, VP6, NSP4) to the subepithelial dome
2. **B-cell priming and class-switching:** Naive B cells in Peyer's patch germinal centers encounter viral antigen; cytokine signals from follicular T-helper cells (Tfh) and the mucosal cytokine environment (IL-10, TGF-β, IL-4) drive **IgA class-switch recombination**
3. **Plasma-cell differentiation and homing:** IgA-committed plasma cell precursors exit Peyer's patches, travel through mesenteric lymph nodes and thoracic duct into circulation, and home back to the **intestinal lamina propria** via α4β7 integrin / MAdCAM-1 interaction — a gut-specific trafficking receptor that ensures the antibody-secreting cells return to the mucosal site of original antigen exposure
4. **Secretory IgA production:** Lamina propria plasma cells produce dimeric IgA, which is transported across enterocytes by the **polymeric immunoglobulin receptor (pIgR)** and secreted as **secretory IgA (sIgA)** into the gut lumen, where it coats viral particles, blocks VP8* binding to HBGA receptors on enterocytes, and prevents productive infection

**Serum antibody responses:**

Rotarix also elicits measurable **serum IgA and serum IgG** (anti-VP7, anti-VP4, anti-VP6). Serum anti-rotavirus IgA is the immunological correlate most consistently associated with protection in clinical trials, with seroconversion (≥4-fold rise in anti-rotavirus IgA) occurring in ~77–85% of infants in high-income trials and ~50–60% in low-income settings — mirroring the efficacy gradient. Serum IgG levels are also elevated post-vaccination but are secondary correlates.

**T-cell responses:**

Rotavirus-specific **CD4+ and CD8+ T cells** are generated following Rotarix vaccination, though cellular immunity has not been established as an independent correlate of protection. Th2-skewed CD4+ T-cell responses in Peyer's patches provide the IgA class-switch help via IL-4, IL-5, IL-13, and IL-21 (Tfh cytokines). CD8+ cytotoxic T cells specific for rotavirus VP6 have been detected in vaccinated infants and may contribute to clearance of established infection.

**Innate immune sensing:**

Replication of the live attenuated virus in intestinal epithelial cells is sensed by innate RNA-sensing receptors — **TLR3** (endosomal dsRNA sensor) and **MDA5/RIG-I** (cytosolic RNA helicases) — triggering type I interferon (IFN-α/β) production, NF-κB activation, and a local inflammatory milieu that serves as the intrinsic adjuvant for adaptive immune priming. The viral non-structural protein **NSP4** acts as an endogenous enterotoxin (disrupting Ca²⁺ homeostasis and chloride secretion) and may also modulate innate signaling.

## Efficacy

**High-income countries:**

The pivotal **European phase III trial** (Vesikari et al., Lancet 2007) enrolled 3,994 infants in Finland, Czech Republic, and other European countries. Against severe RVGE (Vesikari clinical severity score ≥11), Rotarix demonstrated **96.4% vaccine efficacy** during the first rotavirus season and **85.6% efficacy** over 2 years — the latter figure capturing the broader spectrum of circulating strains. Against any RVGE requiring hospitalization or emergency care visit, efficacy was 90.4%.

Real-world post-licensure studies in Europe, Australia, and North America consistently document **70–90% reductions** in rotavirus hospitalizations after program introduction. In the United States (RotaTeq program), hospitalizations for rotavirus diarrhea in children under 5 declined by ~80% within 3 years of vaccine introduction, with indirect (herd) protection extending to unvaccinated older children and adults.

**Low- and middle-income countries:**

The **African phase III trial** (Madhi et al., NEJM 2010) conducted in South Africa and Malawi found overall efficacy of **49%** against severe RVGE over two rotavirus seasons — dramatically lower than the European trial. Notably, efficacy in South Africa (61%) was substantially higher than in Malawi (49%), suggesting that within-continent heterogeneity in host, microbiome, and environmental factors modifies vaccine response.

The **2020 Burnett et al. Lancet Global Health meta-analysis** (57 studies) quantified efficacy by country income level:

| Setting | Rotarix efficacy against severe RVGE |
|:---|:---:|
| High income | 85–96% |
| Upper-middle income | ~75% |
| Lower-middle income | ~63% |
| Low income | ~40–60% |

**Hypotheses for efficacy gradient — an open scientific problem:**

The reduced efficacy in low-income settings is one of the most studied — and still unresolved — questions in pediatric vaccine immunology. Leading mechanistic hypotheses include:

1. **Gut microbiome interference:** Low-income settings have higher enteric pathogen burden, altered microbiome composition, and higher rates of environmental enteropathy — a chronic subclinical intestinal inflammation with villous blunting, increased intestinal permeability, and altered lymphoid tissue architecture. This may impair M-cell-mediated antigen sampling and Peyer's patch B-cell priming.
2. **Maternal antibody interference:** High transplacental transfer of maternal anti-rotavirus IgG (from prior natural infection, higher in high-seroprevalence populations) may neutralize the attenuated vaccine virus in the infant gut before sufficient Peyer's patch priming occurs.
3. **Concurrent oral poliovirus vaccine (OPV) administration:** Co-administration of OPV (standard in low-income EPI schedules) has been associated with reduced rotavirus vaccine immunogenicity in some studies. The mechanism may involve viral interference (OPV occupying innate signaling pathways) or replication competition in intestinal epithelium.
4. **HBGA (histo-blood group antigen) genetics:** VP8* of P[8] rotavirus binds H-type 1/Lewis b HBGAs as cellular receptors. Secretor-negative individuals (who do not express H-type 1 antigen in intestinal mucus, ~20% of populations) may be intrinsically resistant to P[8] infection — but also to P[8] vaccine-strain replication, limiting mucosal priming. HBGA secretor-status distributions vary by population and may partly explain geographic efficacy differences.
5. **Malnutrition and zinc deficiency:** Zinc deficiency (common in high-mortality settings) impairs intestinal mucosal immune function and may reduce IgA secretory capacity. Severe acute malnutrition reduces CD4+ T-cell counts and Peyer's patch cellularity.

The efficacy gap underscores a broader challenge: live oral vaccines (OPV, cholera, typhoid, rotavirus) consistently underperform in high-mortality settings relative to parenteral or conjugate vaccines — an effect that may reflect fundamental differences in mucosal immune priming capacity under conditions of environmental enteropathy and micronutrient deficiency.

## Safety

Rotarix has an excellent safety profile accumulated across hundreds of millions of doses globally, with two noteworthy episodes that deserve scientific and historical context.

**Expected local and systemic reactions:**

Because Rotarix is oral, there is no injection-site reaction. Common post-dose events are mild and transient:
- **Fussiness/irritability:** 25–50% of infants (comparable to placebo arms in phase III trials)
- **Mild diarrhea or vomiting:** 10–20% within 7 days of dose 1; rates comparable to placebo
- **Transient low-grade fever:** ~10%; not a signal distinguishable from background rate at this age

**Intussusception:**

Intussusception is a telescoping of one segment of intestine into an adjacent segment, most commonly at the ileocecal junction, and is the most serious safety concern for rotavirus vaccines. A first-generation rotavirus vaccine, **RotaShield** (Wyeth; rhesus-human tetravalent reassortant), was withdrawn in 1999 — just nine months after licensure — following identification of approximately **1 intussusception case per 4,700–9,474 vaccine recipients** in the first two weeks post-dose.

Rotarix and RotaTeq were developed and evaluated post-RotaShield with intussusception as a primary safety endpoint. Their phase III trials (Rotarix: ROTA-036; RotaTeq: REST trial) each enrolled ~60,000–70,000 infants with active intussusception surveillance — powered to rule out a relative risk comparable to RotaShield.

Post-licensure surveillance has been more nuanced:
- **Australia (2010), Mexico (2011), and US (PRISM, 2014) post-marketing studies** identified a small excess intussusception risk of approximately **1–2 cases per 100,000 vaccinated infants**, predominantly in the 1–7 days after the first dose
- This risk is concentrated in infants vaccinated at older ages (>12 weeks), supporting the hypothesis that the lymphoid hyperplasia induced by natural rotavirus antigen exposure (via the vaccine) serves as a lead point for intussusception preferentially in older infants with more developed Peyer's patches
- The absolute excess risk (~1–2/100,000) must be weighed against the benefit: in low-income settings, rotavirus causes approximately **200–400 deaths per 100,000 unvaccinated children** under age 5, making the benefit-risk ratio overwhelmingly favorable

WHO GACVS reviewed the intussusception data in 2011 and concluded that **the benefit-risk profile clearly favors continued use in all settings** — a conclusion reaffirmed in subsequent position papers. National programs have responded by maintaining the age-restriction windows (first dose 6–12 weeks) to minimize risk in older infants, rather than suspending programs.

**2010 PCV1 DNA detection and temporary suspension:**

In March 2010, the FDA **temporarily suspended Rotarix** after researchers using unbiased deep sequencing (metagenomic viral discovery) detected **porcine circovirus type 1 (PCV1) DNA** in Rotarix vaccine lots. PCV1 is a non-pathogenic porcine virus of no known biological hazard to humans; it was present at trace levels as a contaminant of the porcine-trypsin reagents used in Vero cell manufacturing (trypsin of porcine origin is a standard reagent in cell-culture-based vaccine manufacturing).

The FDA convened an expert advisory committee in May 2010, which concluded:
- PCV1 is not known to cause disease in any animal species
- No epidemiological signal of harm was detectable in post-licensure data
- The detection reflected advances in deep-sequencing sensitivity rather than a new contamination event — PCV1 DNA was almost certainly present in earlier lots tested by conventional assays

The FDA lifted the suspension in May 2010 and Rotarix use resumed. The episode catalyzed important regulatory changes: FDA began requiring deep-sequencing-based adventitious agent testing for live viral vaccines, updating 21 CFR 610 guidance. It also prompted a broader discussion of the philosophical distinction between sequence detection (a molecular finding) and biological hazard (a toxicological/epidemiological determination).

**Contraindications:**

- **Severe combined immunodeficiency (SCID):** Oral live-attenuated rotavirus can cause prolonged, severe, or fatal vaccine-strain gastroenteritis in SCID infants; screening recommendations vary by country
- **History of intussusception:** Prior intussusception is a contraindication due to recurrence risk
- **Intestinal malformation:** Meckel's diverticulum, intestinal malrotation — uncorrected structural lesions predispose to intussusception
- **Latex allergy:** Some earlier Rotarix applicator versions contained latex; current formulations are latex-free — verify by lot
- **Acute severe gastroenteritis:** Delay until recovery (replication competition may reduce immunogenicity)
- **Known hypersensitivity:** To any vaccine component

**HIV exposure:** Unlike BCG, Rotarix is **not contraindicated in HIV-exposed or HIV-infected infants**. WHO recommends routine Rotarix vaccination in HIV-exposed infants regardless of HIV status — the benefit (preventing severe rotavirus diarrhea, which carries high mortality in HIV-positive children) outweighs any theoretical safety concern, and clinical trial data from Africa showed acceptable safety in HIV-exposed cohorts.

## Connections

Rotarix's position in the four-atlas knowledge graph spans the full scale of biological organization — from viral molecular biology to whole-body mucosal immunity:

- **Prevents** → [`02-pathogen/01-viruses/rotavirus`](../../../../02-pathogen/01-viruses/rotavirus/README.md) — G1P[8] live strain elicits VP7/VP4 neutralizing antibodies and mucosal IgA; 85–96% efficacy against severe RVGE in high-income settings; heterotypic cross-protection via conserved VP4 P[8] epitopes
- **Elicits** → [`01-human/07-system/immune-system`](../../../../01-human/07-system/immune-system/README.md) — mucosal sIgA in gut lumen, serum IgA/IgG, CD4+/CD8+ T cells; innate dsRNA sensing via TLR3/MDA5; systemic adaptive response with gut-homing α4β7⁺ plasmablasts
- **Elicits** → [`01-human/04-cellular/t-helper-cell`](../../../../01-human/04-cellular/t-helper-cell/README.md) — Th2/Tfh-dominant CD4+ response in Peyer's patches; IL-4/IL-21 drive IgA class switching; Tfh support germinal center affinity maturation for high-quality anti-VP7/VP4 antibodies
- **Replicates-in** → [`01-human/06-organ/small-intestine`](../../../../01-human/06-organ/small-intestine/README.md) — attenuated virus colonizes small-intestinal epithelium and M cells in Peyer's patches; local antigen presentation drives lamina propria IgA plasma cell differentiation and mucosal memory

**Platform comparison:**
- **RotaTeq** (Merck; pentavalent bovine-human reassortant; G1–G4/P[8]): 3-dose series, comparable efficacy in high-income settings, same challenge of reduced efficacy in low-income settings
- **BCG** [`04-vaccine/05-live-attenuated/bcg`](../bcg/README.md): canonical parenteral live-attenuated comparator — Th1-dominant cellular response vs. Rotarix's Th2/IgA-dominant mucosal response; BCG elicits trained innate immunity (monocyte epigenetic reprogramming), a mechanism not described for Rotarix
- **Rotavirus oral vaccine pipeline:** Next-generation candidates include **ROTAVAC** (Bharat Biotech, India; neonatal G9P[11] strain), **ROTASIIL** (Serum Institute; bovine-human reassortant, heat-stable), and **RV3-BB** (Murdoch Children's Research Institute; neonatal strain given at birth) — all aimed at improving low-income-country efficacy

---

**[← Platform 05 (Live-Attenuated)](../README.md)** · **[← Vaccine Atlas](../../README.md)** · **[Schema](../../../../schemas/vaccine-entry.schema.md)**
