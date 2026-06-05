---
schema: vaccine-entry/v1
id: mrna-1273
name: mRNA-1273 (Spikevax)
atlas: 04-vaccine
platform: 01-mrna
status: draft
last_reviewed: 2026-06-04
summary: "Modified-nucleoside mRNA-LNP encoding prefusion-stabilized (2P) SARS-CoV-2 spike. Moderna/NIH VRC; sequence-to-IND 42 days. 94.1% efficacy (COVE trial). FDA EUA December 2020; first mRNA vaccine on WHO Emergency Use Listing."
aliases: ["Spikevax", "Moderna COVID-19 vaccine", "CX-024414", "elasomeran"]
target_pathogens:
  - target: 02-pathogen/01-viruses/sars-cov-2
    antigen: spike-prefusion-2P
    coverage: ["wild-type (Wuhan-Hu-1)", "alpha", "beta", "delta", "omicron-BA.1", "omicron-BA.4/5", "XBB"]
antigens:
  - name: "SARS-CoV-2 spike (prefusion-stabilized, 2P)"
    source_pathogen: 02-pathogen/01-viruses/sars-cov-2
    modification: "K986P + V987P (2P stabilization, Graham/McLellan/Corbett); furin-cleavage site retained in original construct"
    encoded_as: "modified-nucleoside mRNA with N1-methylpseudouridine replacing uridine; codon-optimized; 5′ cap1, β-globin UTRs, ~100-nt poly(A) tail"
    structure_ref: { pdb: ["6VSB", "6VXX", "7JJI"] }
delivery_system: "lipid-nanoparticle (LNP); four-lipid composition: SM-102 (proprietary ionizable cationic lipid), PEG2000-DMG, cholesterol, DSPC; molar ratio ~50:1.5:38.5:10"
adjuvants: []
route_of_administration: "intramuscular"
dose_schedule:
  primary_series_adult: "2 doses, 28 days apart, 100 µg each (adults ≥18)"
  primary_series_adolescent: "2 doses, 28 days apart, 100 µg (ages 12–17, original EUA)"
  pediatric_50ug: "2 doses, 28 days apart, 50 µg (ages 6–11)"
  pediatric_25ug: "2 doses, 28 days apart, 25 µg (ages 6 months–5 years)"
  booster: "single 50 µg dose ≥ 5 months after primary; later updated bivalent / monovalent formulations"
manufacturer:
  developer: "Moderna, Inc. (Cambridge, Massachusetts) with NIAID Vaccine Research Center"
  partners: ["Acuitas Therapeutics (LNP IP licensing)", "Lonza (drug substance manufacturing)", "Catalent (fill-finish)", "ROVI (EU fill-finish)"]
regulatory_status:
  - body: "FDA"
    status: "EUA"
    date: "2020-12-18"
  - body: "EMA"
    status: "Conditional Marketing Authorization"
    date: "2021-01-06"
  - body: "MHRA"
    status: "Conditional Marketing Authorization"
    date: "2021-01-08"
  - body: "WHO"
    status: "Emergency Use Listing"
    date: "2021-04-30"
  - body: "FDA"
    status: "BLA-approved (Spikevax) — adults"
    date: "2022-01-31"
  - body: "FDA"
    status: "BLA-approved — pediatric (6 months–17 years)"
    date: "2024-07-10"
cold_chain: "−25°C to −15°C frozen for long-term storage (up to 9 months); 2°–8°C refrigerated for up to 30 days unpunctured"
discontinued: false
xrefs:
  drugbank: "DB15654"
  rxnorm: "2468230"
  vo: "VO:0005177"
clinical_trials:
  - id: "NCT04283461"
    tag: "Phase 1 (mRNA-1273 P201)"
  - id: "NCT04405076"
    tag: "Phase 2"
  - id: "NCT04470427"
    tag: "Phase 3 COVE"
  - id: "NCT04796896"
    tag: "Pediatric KidCOVE"
who_essential_medicine: true
sources:
  - id: jackson-2020-phase-1
    type: peer-reviewed
    cite: "Jackson LA, Anderson EJ, Rouphael NG, et al. An mRNA Vaccine against SARS-CoV-2 — Preliminary Report. NEJM. 2020;383(20):1920-1931."
    doi: "10.1056/NEJMoa2022483"
    pmid: "32663912"
    url: "https://doi.org/10.1056/NEJMoa2022483"
  - id: anderson-2020-older-adults
    type: peer-reviewed
    cite: "Anderson EJ, Rouphael NG, Widge AT, et al. Safety and Immunogenicity of SARS-CoV-2 mRNA-1273 Vaccine in Older Adults. NEJM. 2020;383(25):2427-2438."
    doi: "10.1056/NEJMoa2028436"
    pmid: "32991794"
  - id: corbett-2020-preclinical
    type: peer-reviewed
    cite: "Corbett KS, Edwards DK, Leist SR, et al. SARS-CoV-2 mRNA vaccine design enabled by prototype pathogen preparedness. Nature. 2020;586(7830):567-571."
    doi: "10.1038/s41586-020-2622-0"
    pmid: "32756549"
  - id: baden-2021-cove
    type: peer-reviewed
    cite: "Baden LR, El Sahly HM, Essink B, et al. Efficacy and Safety of the mRNA-1273 SARS-CoV-2 Vaccine. NEJM. 2021;384(5):403-416."
    doi: "10.1056/NEJMoa2035389"
    pmid: "33378609"
  - id: el-sahly-2021-cove-followup
    type: peer-reviewed
    cite: "El Sahly HM, Baden LR, Essink B, et al. Efficacy of the mRNA-1273 SARS-CoV-2 Vaccine at Completion of Blinded Phase. NEJM. 2021;385(19):1774-1785."
    doi: "10.1056/NEJMoa2113017"
    pmid: "34551225"
  - id: wrapp-2020-spike-cryoem
    type: peer-reviewed
    cite: "Wrapp D, Wang N, Corbett KS, et al. Cryo-EM structure of the 2019-nCoV spike in the prefusion conformation. Science. 2020;367(6483):1260-1263."
    doi: "10.1126/science.abb2507"
    pmid: "32075877"
  - id: pardi-2018-mrna-review
    type: peer-reviewed
    cite: "Pardi N, Hogan MJ, Porter FW, Weissman D. mRNA vaccines — a new era in vaccinology. Nat Rev Drug Discov. 2018;17(4):261-279."
    doi: "10.1038/nrd.2017.243"
    pmid: "29326426"
  - id: kariko-2005-modified-nucleosides
    type: peer-reviewed
    cite: "Karikó K, Buckstein M, Ni H, Weissman D. Suppression of RNA recognition by Toll-like receptors: the impact of nucleoside modification and the evolutionary origin of RNA. Immunity. 2005;23(2):165-175."
    doi: "10.1016/j.immuni.2005.06.008"
    pmid: "16111635"
  - id: pallesen-2017-2p-stabilization
    type: peer-reviewed
    cite: "Pallesen J, Wang N, Corbett KS, et al. Immunogenicity and structures of a rationally designed prefusion MERS-CoV spike antigen. PNAS. 2017;114(35):E7348-E7357."
    doi: "10.1073/pnas.1707304114"
    pmid: "28807998"
  - id: mevorach-2021-myocarditis
    type: peer-reviewed
    cite: "Mevorach D, Anis E, Cedar N, et al. Myocarditis after BNT162b2 mRNA Vaccine against Covid-19 in Israel. NEJM. 2021;385(23):2140-2149."
    doi: "10.1056/NEJMoa2109730"
    pmid: "34614328"
cross_links:
  - target: 02-pathogen/01-viruses/sars-cov-2
    relation: immunizes-against
    evidence: baden-2021-cove
    note: "Phase 3 COVE: 94.1% efficacy against symptomatic COVID-19 (95% CI 89.3–96.8) at median 2 months follow-up; sustained ~93% at 5+ months for primary series, against pre-Omicron strains."
  - target: 02-pathogen/01-viruses/sars-cov-2
    relation: targets-antigen-of
    evidence: corbett-2020-preclinical
    note: "Encodes the SARS-CoV-2 spike (S) glycoprotein with 2P prefusion stabilization (K986P + V987P)."
  - target: 04-vaccine/01-mrna/bnt162b2
    relation: same-platform-as
    note: "Both modified-nucleoside mRNA-LNP encoding 2P-stabilized spike. Differ in lipid composition (SM-102 vs ALC-0315), dose (100 µg vs 30 µg), and dose interval."
  - target: 01-human/06-organ/heart
    relation: causes-adverse-event-in
    scale: 06-organ
    evidence: mevorach-2021-myocarditis
    note: "Rare myocarditis / pericarditis adverse event, predominantly in young adult males within 1–7 days of dose 2; incidence ~10–25 per 100,000 in highest-risk age band; typically self-limiting with full recovery."
  - target: 01-human/04-cellular/cardiomyocyte
    relation: causes-adverse-event-in
    scale: 04-cellular
    evidence: mevorach-2021-myocarditis
    note: "Mechanism of vaccine-associated myocarditis is incompletely understood — proposed mechanisms include molecular mimicry between spike and cardiac proteins, hyperimmune response to LNP/mRNA, and dysregulated cytokine signaling. Histology resembles lymphocytic myocarditis but milder."
---

# mRNA-1273 (Spikevax)

## Overview

**mRNA-1273** is a modified-nucleoside mRNA vaccine encoding the SARS-CoV-2 spike (S) glycoprotein, stabilized in the prefusion conformation by two proline substitutions (the **"2P" mutations**, K986P and V987P), delivered in a four-lipid lipid nanoparticle (LNP). It was co-developed by **Moderna** (Cambridge, Massachusetts) and the **NIH Vaccine Research Center** (NIAID/VRC) under the leadership of Barney Graham, Kizzmekia Corbett, and Jason McLellan.

The vaccine is the most consequential proof of concept for a hypothesis the project's mission depends on: **once the pathogen genome is in hand, a candidate vaccine can be designed in days, not years.** The sequence of SARS-CoV-2 was released by Zhang Yongzhen's group on January 10–11, 2020 [^wrapp-2020-spike-cryoem]. By January 13, 2020, Moderna and the VRC had finalized the mRNA-1273 sequence. The first clinical batch was shipped to NIH on **February 24, 2020** — roughly six weeks from sequence to vial — and the first volunteer was dosed on **March 16, 2020** [^jackson-2020-phase-1]. Phase 3 efficacy (94.1%) was reported in November 2020 [^baden-2021-cove]; FDA Emergency Use Authorization was granted on **December 18, 2020**.

The platform delivered because three streams of decade-long work matured at exactly the right time: **modified-nucleoside mRNA chemistry** (Karikó & Weissman, 2005 onward [^kariko-2005-modified-nucleosides]), **prefusion-stabilized class-I fusion glycoproteins** (Graham, McLellan, Corbett, on RSV F and MERS spike before COVID [^pallesen-2017-2p-stabilization]), and **lipid-nanoparticle delivery** (Pieter Cullis and the Acuitas / Arbutus IP lineage [^pardi-2018-mrna-review]). mRNA-1273 was not designed in 6 weeks. It was designed over 15 years; the last 6 weeks were *assembly*.

## Platform

mRNA-1273 is a **first-generation modified-nucleoside mRNA vaccine** — the same broad architecture as BNT162b2 (Pfizer-BioNTech), with which it shares the 2P-stabilized spike antigen and modified-nucleoside chemistry, while differing in dose and lipid composition.

The mRNA construct contains:

- **5′ cap (cap1, m7G(5′)ppp(5′)Nm-)** — required for ribosome recruitment and protection from 5′ exonucleases.
- **5′ UTR** — optimized for translation efficiency.
- **Coding sequence** — codon-optimized full-length SARS-CoV-2 spike with K986P + V987P stabilizing substitutions; signal peptide and transmembrane domain retained for native-like membrane anchoring after translation.
- **3′ UTR** — based on β-globin to stabilize the mRNA.
- **Poly(A) tail** — ~100 nucleotides.
- **Modified nucleoside** — every uridine is replaced with **N1-methylpseudouridine (m1Ψ)**, which evades TLR7/TLR8 and RIG-I sensing of "foreign" RNA and dramatically increases translation [^kariko-2005-modified-nucleosides] [^pardi-2018-mrna-review].

The mRNA itself is degraded by intracellular RNases within days to weeks. There is no genomic integration, no reverse transcription in the cytoplasm by host machinery, and no replication.

## Antigen design

The antigen is the **full-length SARS-CoV-2 spike (S) glycoprotein**, locked in the **prefusion conformation** by two stabilizing proline substitutions at residues 986 and 987 (the **"2P" mutation**) [^corbett-2020-preclinical] [^pallesen-2017-2p-stabilization]. The 2P design, originally developed by the Graham/McLellan/Corbett group on RSV F and MERS-CoV S in 2013–2017, exploits a feature of class-I fusion glycoproteins: their *prefusion* form is the immunogenically protective conformation, but it is intrinsically unstable and rapidly transitions to the post-fusion form. Substituting two flexible residues with prolines locks the central helix in its prefusion bundle, preserving the neutralizing-epitope landscape (notably the RBD-up state and the NTD supersite).

Structural references: cryo-EM structures of the 2P-stabilized spike trimer were solved within weeks of sequence release (PDB 6VSB at 3.5 Å) [^wrapp-2020-spike-cryoem]; this was used to validate that the encoded protein folded as designed.

## Delivery system

The mRNA is encapsulated in a **lipid nanoparticle (LNP)** with four lipid components:

| Component | Role | Approximate molar % |
|:---|:---|:---:|
| **SM-102** (Moderna's proprietary ionizable cationic lipid) | At low pH (endosome): protonated, disrupts membrane → cytoplasmic release. At physiological pH: nearly neutral, evades clearance. | ~50% |
| **DSPC** (1,2-distearoyl-sn-glycero-3-phosphocholine) | Helper / structural phospholipid. | ~10% |
| **Cholesterol** | Membrane stabilizer; modulates fluidity. | ~38.5% |
| **PEG2000-DMG** (PEGylated lipid) | Surface coating; prevents aggregation; extends circulation. Sheds within hours. | ~1.5% |

The LNP is a ~80–100 nm sphere with the mRNA in its hydrophilic core, surrounded by a lipid bilayer/multi-lamellar architecture. After intramuscular injection, LNPs are taken up by local cells (myocytes, dermal dendritic cells, draining-lymph-node cells) via endocytosis, the ionizable lipid disrupts the endosomal membrane, and the mRNA is released into the cytoplasm where ribosomes translate it.

## Immunogenicity

Translated spike protein is processed via two pathways simultaneously:

1. **MHC class I presentation** of intracellular spike-derived peptides → priming of **CD8 T cells** (cytotoxic). Provides cellular immunity, especially important against intracellular viral replication once the host is later infected.
2. **Secretion / shedding of intact spike trimers** from the cell surface → uptake by **B cells via BCR** in the draining lymph node → germinal-center reaction → class-switched, somatically-hypermutated **IgG anti-spike antibodies**. Provides humoral / neutralizing immunity. The dominant neutralizing epitope class targets the receptor-binding domain (RBD) and blocks spike-ACE2 engagement.

CD4 T-helper cells (Th1-skewed for mRNA platforms) provide help to both arms.

**Correlates of protection:** anti-spike (RBD-binding) IgG titer correlates strongly with protection against symptomatic disease. Neutralizing antibody titer correlates even more strongly. T-cell responses correlate with protection against severe disease and with cross-variant protection where neutralizing antibody is partially evaded.

**Duration:** humoral protection wanes over 4–8 months (especially neutralizing titer); cellular protection (especially against severe disease) is more durable, persisting >12 months. Boosters restore peak titers and broaden the response.

## Manufacturing

Drug substance (mRNA) is produced by **in vitro transcription (IVT)** from a linearized DNA plasmid template using T7 RNA polymerase, with N1-methylpseudouridine triphosphate replacing UTP. Capping is enzymatic (vaccinia virus capping enzyme) or via co-transcriptional cap analog. Purification removes residual DNA template, NTPs, dsRNA byproducts (which are highly inflammatory), and protein. Drug product manufacturing encapsulates the purified mRNA in LNPs via rapid microfluidic mixing of mRNA-in-aqueous-buffer with lipids-in-ethanol.

Major manufacturing partners: **Lonza** (drug substance, Switzerland and US), **Catalent** (fill-finish, US), **ROVI** (fill-finish, Spain). At peak production (2021–2022), global capacity reached ~1 billion doses/year.

**Cold chain:** long-term storage at −25°C to −15°C (standard pharmaceutical freezer) for up to 9 months; refrigerated (2–8°C) up to 30 days unpunctured. Less stringent than BNT162b2's original ultra-cold (−80°C) requirement, owing to differences in LNP formulation.

## Trials

| Phase | Trial | N | Primary readout | Result |
|:---:|:---|---:|:---|:---|
| 1 | NCT04283461 (P201) | 45 | Safety, dose-finding (25/100/250 µg) | Acceptable safety; binding + neutralizing antibody at all doses [^jackson-2020-phase-1] |
| 1 | NCT04283461 expansion | 40 | Older-adult safety + immunogenicity | Comparable response in 56–70 / >70 cohorts [^anderson-2020-older-adults] |
| 2 | NCT04405076 | 600 | Dose confirmation (50/100 µg) | 100 µg selected for Phase 3 |
| 3 | NCT04470427 (COVE) | 30,420 | Symptomatic COVID-19 ≥14 days post-dose-2 | **94.1% efficacy** (95% CI 89.3–96.8) [^baden-2021-cove] |
| 3 | COVE blinded-phase completion | 30,420 | Sustained efficacy through ~5 months | 93.2% efficacy (95% CI 91.0–94.8) [^el-sahly-2021-cove-followup] |
| 2/3 | NCT04796896 (KidCOVE) | ~13,000 | Pediatric (6 mo – 17 yr) safety + immunogenicity | Bridged to adult immunogenicity; non-inferiority confirmed |

Severe disease prevention in COVE: 100% (30 cases / 0 in vaccine arm in primary analysis).

## Regulatory

| Date | Body | Action |
|:---|:---|:---|
| 2020-12-18 | FDA | Emergency Use Authorization (adults ≥18) |
| 2021-01-06 | EMA | Conditional Marketing Authorization |
| 2021-01-08 | MHRA | Conditional authorization (UK) |
| 2021-04-30 | WHO | Emergency Use Listing |
| 2021-05-12 | FDA | EUA expanded to ages 12–17 |
| 2021-08-12 | FDA | Booster authorization (immunocompromised) |
| 2022-01-31 | FDA | Full approval as **Spikevax** (adults) |
| 2022-06-17 | FDA | EUA for ages 6 months – 17 years (lower doses) |
| 2024-07-10 | FDA | Full approval expanded to pediatric population |

Variant-targeted formulations (bivalent BA.1, bivalent BA.4/5, monovalent XBB.1.5) followed under amended authorizations.

## Safety

**Common reactogenicity** (within 1–3 days of dose):
- Local: injection-site pain (~85%), erythema, swelling.
- Systemic: fatigue (~60%), headache (~55%), myalgia, chills, fever (~15% after dose 2). Reactogenicity is consistently more pronounced after dose 2 and at the 100 µg adult dose than at lower doses.

**Rare but established adverse events:**
- **Myocarditis / pericarditis** — predominantly young adult males within 1–7 days of dose 2 [^mevorach-2021-myocarditis]. Israeli surveillance reported ~10–25 cases per 100,000 in the highest-risk age band (16–29-year-old males), with most cases mild and self-limiting (median hospital stay 3–4 days; full recovery typical). Mechanism is incompletely understood — proposed contributors include molecular mimicry between spike epitopes and α-myosin / cardiac proteins, dysregulated innate-immune signaling to the LNP/mRNA, and individual susceptibility loci.
- **Anaphylaxis** — ~2–5 per million doses, typically within 15–30 min, related to PEG component of the LNP; manageable with standard observation period and epinephrine.

**No association** has been confirmed with: thrombosis with thrombocytopenia syndrome (which is associated with adenovirus-vector vaccines, not mRNA), infertility, or genomic integration.

## Variation

- **Age:** lower neutralizing titers in older adults (>65), ~2-fold lower than in 18–55 cohort, but still protective; pediatric responses match or exceed adult responses at the dose-adjusted equivalent.
- **Sex:** myocarditis adverse-event signal is markedly male-predominant in adolescents/young adults. Antibody titers slightly higher in females on average.
- **Immunocompromised:** transplant recipients, patients on B-cell-depleting therapies (e.g., rituximab) show markedly reduced antibody response — additional doses and alternative strategies (passive antibody prophylaxis) recommended.
- **Prior infection ("hybrid immunity"):** prior SARS-CoV-2 infection plus vaccination produces broader, higher-magnitude, and more durable responses than either alone.
- **Variant evasion:** Omicron BA.1 reduced neutralizing titer ~10–20× vs ancestral, motivating bivalent and updated monovalent boosters; T-cell epitope coverage was preserved more broadly than B-cell, helping maintain protection against severe disease.

## Equity & access

- **Pricing:** ~$15–25/dose (US government procurement, 2020–2022); higher in private markets post-2023.
- **COVAX:** Moderna donated and discounted doses to COVAX, but mRNA-1273 was not the dominant vaccine in low/middle-income countries owing to cold-chain and price considerations — that role fell to AZD1222 (Oxford-AstraZeneca) and inactivated platforms (CoronaVac, Sinopharm).
- **IP / licensing:** Moderna pledged not to enforce its COVID-19 vaccine patents during the pandemic but reasserted enforcement in 2022; ongoing litigation with Pfizer-BioNTech and others.
- **Local manufacturing:** Moderna announced facilities in Kenya, Australia, UK, and Canada to expand global capacity — most still in build-out as of mid-2026.

## Open questions

- **Mechanism of vaccine-associated myocarditis** — molecular mimicry vs. cytokine-driven vs. LNP-specific innate response. Resolution would inform safer next-generation mRNA designs (e.g., dose-fractionation, alternative lipids, antigen modifications).
- **Mucosal immunity** — IM mRNA-1273 elicits weak mucosal IgA; intranasal mRNA delivery is in development to address this gap, which would close a major bottleneck on transmission blocking.
- **Self-amplifying mRNA at lower doses** — saRNA platforms (ARCT-154 / Kostaive) achieve protection at ~1/10 the dose; next-generation candidates may displace m1Ψ-modified mRNA if reactogenicity and durability profiles improve.
- **Pan-coronavirus / variant-proof spike designs** — hexapro stabilization, designed nanoparticle scaffolds, conserved-epitope display. Multiple candidates are in clinical development.
- **Correlates of protection with strict CIs** — population-level threshold values for anti-RBD IgG and pseudovirus-neutralizing titer that confer protection have been estimated but not yet codified as regulatory bridging endpoints, which would speed authorization of variant-updated formulations.

## Connections

- **Target pathogen**: [`02-pathogen/01-viruses/sars-cov-2`](../../../02-pathogen/01-viruses/sars-cov-2/README.md)
- **Sibling mRNA vaccine**: [`04-vaccine/01-mrna/bnt162b2`](../bnt162b2/README.md) (Pfizer-BioNTech, ALC-0315 LNP, 30 µg)
- **Antigen target**: prefusion-stabilized spike protein; B cells in draining lymph nodes generate anti-RBD IgG
- **Immune effectors**: CD4+ Th1 T cells, CD8+ cytotoxic T cells, anti-spike neutralizing IgG (IgG1/IgG3)

## See also

- [`02-pathogen/01-viruses/sars-cov-2`](../../../02-pathogen/01-viruses/sars-cov-2/README.md) — the target pathogen
- [`04-vaccine/01-mrna/bnt162b2`](../bnt162b2/README.md) — sibling mRNA-LNP vaccine (Pfizer-BioNTech)
- [`04-vaccine/01-mrna/README.md`](../README.md) — mRNA platform overview
- [`schemas/vaccine-entry.schema.md`](../../../../schemas/vaccine-entry.schema.md) — schema this entry conforms to
