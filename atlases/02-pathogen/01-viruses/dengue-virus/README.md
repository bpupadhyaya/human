---
schema: pathogen-entry/v1
id: dengue-virus
name: Dengue virus
atlas: 02-pathogen
scale: 01-viruses
status: draft
last_reviewed: 2026-06-04
summary: "Enveloped +ssRNA flavivirus; 4 serotypes (DENV1–4). Infects dendritic cells; monocytes via ADE in secondary infection. 390 million infections/year; dengue hemorrhagic fever from immune vascular leak. No antiviral. Dengvaxia (CYD-TDV) approved for seropositive recipients only."
aliases: ["dengue", "DENV", "dengue fever virus", "dengue haemorrhagic fever virus", "DF", "DHF", "DENV1", "DENV2", "DENV3", "DENV4"]
sources:
  - id: bhatt-2013-dengue-global
    type: peer-reviewed
    cite: "Bhatt S, Gething PW, Brady OJ, et al. The global distribution and burden of dengue. Nature. 2013;496(7446):504-7."
    doi: "10.1038/nature12060"
    pmid: "23563266"
    url: "https://doi.org/10.1038/nature12060"
  - id: halstead-2007-ade
    type: peer-reviewed
    cite: "Halstead SB. Dengue. Lancet. 2007;370(9599):1644-52."
    doi: "10.1016/S0140-6736(07)61687-0"
    pmid: "17993365"
    url: "https://doi.org/10.1016/S0140-6736(07)61687-0"
  - id: who-2009-dengue-guidelines
    type: clinical-guideline
    cite: "World Health Organization. Dengue: Guidelines for Diagnosis, Treatment, Prevention and Control. WHO; 2009."
    url: "https://www.who.int/publications/i/item/9789241547871"
    accessed: "2026-06-04"
  - id: guzman-2016-dengue-review
    type: peer-reviewed
    cite: "Guzman MG, Gubler DJ, Izquierdo A, Martinez E, Halstead SB. Dengue infection. Nat Rev Dis Primers. 2016;2:16055."
    doi: "10.1038/nrdp.2016.55"
    pmid: "27534439"
    url: "https://doi.org/10.1038/nrdp.2016.55"
cross_links:
  - target: 01-human/04-cellular/dendritic-cell
    relation: infects
    evidence: halstead-2007-ade
    note: "Dengue virus initially infects skin-resident immature dendritic cells (Langerhans cells) after *Aedes aegypti* bite; DCs serve as both initial replication site and vehicle for systemic dissemination via lymphatics and bloodstream."
  - target: 01-human/07-system/immune-system
    relation: damages
    evidence: guzman-2016-dengue-review
    note: "NS1 protein activates complement and disrupts the glycocalyx of endothelial cells; NS5 inhibits STAT2 interferon signaling; secondary heterotypic infection triggers cross-reactive T-cell responses and ADE (Fcγ receptor-mediated uptake into monocytes/macrophages), amplifying viral load and causing systemic vascular leak (dengue hemorrhagic fever)."
  - target: 01-human/06-organ/liver
    relation: damages
    evidence: guzman-2016-dengue-review
    note: "Dengue virus infects hepatocytes via AXL and DC-SIGN; hepatic damage causes elevated AST/ALT in >80% of cases; fulminant hepatic failure in severe dengue contributes to coagulopathy and mortality."
  - target: 02-pathogen/06-environmental/aedes-aegypti
    relation: connects-to
    note: "Ae. aegypti is the primary vector; DENV replicates in midgut and salivary glands after 8-12 day extrinsic incubation period; Ae. albopictus is a secondary vector; transmitted to humans via infective saliva injected during bloodmeal."
  - target: 01-human/04-cellular/hepatocyte
    relation: infects
    note: "DENV infects hepatocytes via AXL receptor and DC-SIGN; hepatic damage elevates AST/ALT in >80% of dengue cases; severe dengue produces fulminant hepatic failure with coagulopathy and mortality risk."
---

# Dengue virus

## Overview

**Dengue virus (DENV)** is a **positive-sense single-stranded RNA (+ssRNA) flavivirus** transmitted primarily by *Aedes aegypti* and *Aedes albopictus* mosquitoes. It is the most prevalent arthropod-borne viral disease in humans: an estimated **390 million infections occur annually** across 128 countries, with ~96 million clinically apparent cases and ~20,000 deaths [^bhatt-2013-dengue-global]. Half the world's population lives in dengue-endemic regions.

Dengue is unique among common human pathogens in existing as **four serotypes (DENV1–4)** that are antigenically distinct enough that immunity to one does not provide cross-protection against the others. On the contrary, **antibody-dependent enhancement (ADE)** of infection means that cross-reactive antibodies from a primary infection can actually *increase* severity of a secondary heterotypic infection — the core mechanism of dengue hemorrhagic fever (DHF) and dengue shock syndrome (DSS).

There is no approved antiviral. The only licensed vaccine (CYD-TDV/Dengvaxia, Sanofi Pasteur) is restricted to seropositive individuals because of ADE risk in seronegative recipients [^who-2009-dengue-guidelines].

## Structure

**Virion:**
- **Genome:** ~10.7 kb +ssRNA; single open reading frame encoding a polyprotein (~3,391 aa) cleaved by host and viral proteases into 3 structural proteins (C, prM/M, E) and 7 non-structural proteins (NS1, NS2A, NS2B, NS3, NS4A, NS4B, NS5)
- **Nucleocapsid:** C protein (capsid) surrounds the genomic RNA
- **Envelope:** ~50 nm icosahedral virion with host-derived lipid bilayer; 90 E protein dimers arranged in herringbone pattern (flat at 37°C); pH-dependent rearrangement to trimers during endosomal fusion
- **E protein:** primary surface glycoprotein; mediates receptor binding and membrane fusion; organized into three structural domains (DI hinge, DII fusion loop, DIII receptor-binding)
- **NS1 protein:** secreted hexamer; activates complement, disrupts vascular endothelium — key pathogenic mediator

**Serotypes:** DENV1–4 share ~60–75% amino acid identity; the E protein's domain III varies most between serotypes, determining serotype-specific antibody recognition.

## Infection Mechanism

**Entry:**
1. *Aedes* mosquito bite deposits DENV-containing saliva into dermis
2. Immature dendritic cells (Langerhans cells) are infected via **DC-SIGN** (CD209), **AXL receptor tyrosine kinase**, and **mannose receptor**; primary replication cycle in skin DCs
3. DCs migrate to draining lymph nodes; viremia established
4. Circulating monocytes infected via **Fcγ receptors** bearing cross-reactive IgG from prior serotype (ADE) — dramatically increases viral load in monocytes/macrophages

**Viral replication:**
- Receptor-mediated endocytosis → endosomal acidification → E protein trimerization and membrane fusion → RNA release into cytoplasm
- NS5 (RNA-dependent RNA polymerase) + NS3 (helicase/protease) on ER-derived replication complexes → genomic RNA amplification
- Virion assembly at ER membrane; budding as immature prM-containing particles; furin cleavage of prM → mature infectious virions

**Immune evasion:**
- **NS5** directly degrades STAT2, blocking IFN-α/β signaling
- **NS2B/NS3 protease** cleaves STING (cGAS-STING innate DNA sensor) homologues in some contexts
- **ADE:** In secondary heterotypic infection, serotype-cross-reactive IgG opsonizes virions → Fcγ receptor (FcγRI/II on monocytes/macrophages) mediates entry without neutralization → 100–1000-fold increase in intracellular viral load

## Host Interactions

**Clinical spectrum:**
- **Dengue fever (DF):** Most infections (~96 million/year); fever, severe headache, retro-orbital pain, myalgia, rash ("breakbone fever"); self-limited 7–10 days
- **Dengue hemorrhagic fever (DHF):** Plasma leakage from immune-mediated vascular permeability; hemoconcentration, thrombocytopenia, coagulopathy
- **Dengue shock syndrome (DSS):** Circulatory collapse; mortality 1–5% without treatment, <1% with fluid management
- **Severe organ involvement:** Encephalitis, myocarditis, acute liver failure, acute kidney injury

**ADE and secondary infection:**
Secondary infection with a different serotype is the strongest risk factor for severe dengue. Cross-reactive memory T cells also contribute: heterotypic T cells recognize peptides with lower affinity, produce inflammatory cytokines (IFN-γ, TNF-α, IL-2) abundantly but kill infected cells inefficiently, amplifying the systemic inflammatory response.

**Vascular leak mechanism:**
NS1 protein (secreted into blood at high levels: 1–50 µg/mL) directly disrupts the endothelial glycocalyx and activates complement, increasing vascular permeability without direct endothelial infection. Activated T cells and monocytes further release permeability factors (TNF-α, IL-8, MCP-1).

## Connections

- `infects` → **[Dendritic Cell](../../../01-human/04-cellular/dendritic-cell/README.md)** — skin-resident immature DCs (Langerhans cells) are the primary initial target; viral replication in DCs drives systemic dissemination; DC-SIGN and AXL receptor mediate entry.
- `damages` → **[Immune System](../../../01-human/07-system/immune-system/README.md)** — NS5-mediated STAT2 degradation blocks IFN-α/β signaling; ADE amplifies viral burden in monocytes/macrophages via Fcγ receptors; cross-reactive T-cell cytokine storm drives vascular leak and severe dengue.
- `damages` → **[Liver](../../../01-human/06-organ/liver/README.md)** — hepatocyte infection and immune-mediated hepatic damage cause elevated AST/ALT in >80% of cases; severe dengue produces fulminant hepatic failure contributing to coagulopathy and mortality.
- `connects-to` → **[Aedes aegypti](../../../02-pathogen/06-environmental/aedes-aegypti/README.md)** — Ae. aegypti is the primary vector; DENV replicates in midgut and salivary glands after 8-12 day extrinsic incubation period; Ae. albopictus is secondary vector; transmitted via infective saliva during bloodmeal.
- `infects` → **[Hepatocyte](../../../01-human/04-cellular/hepatocyte/README.md)** — DENV infects hepatocytes via AXL receptor and DC-SIGN; hepatic damage elevates AST/ALT in >80% of dengue cases; severe dengue produces fulminant hepatic failure with coagulopathy and mortality risk.

## Pathology

**Dengue hemorrhagic fever (DHF/DSS):**
The WHO grades DHF severity (Grades I–IV) by clinical markers of plasma leakage and bleeding:
- **Grade I:** Fever + nonspecific constitutional symptoms + positive tourniquet test only
- **Grade II:** Grade I + spontaneous bleeding
- **Grade III:** Grade II + circulatory failure (rapid/weak pulse, hypotension, cold clammy skin)
- **Grade IV (DSS):** Profound shock, undetectable pulse/BP

Thrombocytopenia (typically <100,000/µL) is universal in DHF — caused by immune complex deposition on platelets (IgG + complement), direct viral platelet infection, and bone marrow suppression. Disseminated intravascular coagulation (DIC) in the most severe cases.

**Critical phase:** Day 3–7 of illness; fever defervescence often marks the onset of plasma leakage — paradoxically, fever resolution signals the dangerous phase rather than recovery. Aggressive IV fluid management in this window is the cornerstone of treatment.

---

*This page is co-maintained with AI assistance. Content is for educational purposes and does not constitute medical advice. See [equalinformation.com/human](https://equalinformation.com/human) for the full atlas.*
