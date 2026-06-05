---
schema: vaccine-entry/v1
id: bcg
name: "BCG (Bacillus Calmette-Guérin)"
atlas: 04-vaccine
platform: 05-live-attenuated
status: draft
last_reviewed: 2026-06-04
summary: "Live attenuated M. bovis; single intradermal dose at birth. 60–80% efficacy against severe TB (meningitis, miliary) in children; ~38% reduction in all-cause neonatal mortality via trained innate immunity. Most widely deployed vaccine: ~100 million doses/year."
target_pathogens:
  - mycobacterium-tuberculosis
antigens:
  - "live attenuated Mycobacterium bovis (BCG strain)"
delivery_system: "live attenuated mycobacterium"
adjuvants: []
route_of_administration: intradermal
dose_schedule: "single dose at birth or early childhood"
manufacturer: "multiple (Serum Institute of India, Japan BCG Lab, others)"
regulatory_status: "licensed in 170+ countries; WHO prequalified; universal childhood immunization in TB-endemic countries"
cold_chain: "2–8°C (lyophilized, reconstitute before use)"
discontinued: false
status: active
tags:
  - bcg
  - tuberculosis
  - mycobacterium-bovis
  - live-attenuated
  - neonatal
  - trained-immunity
  - neonatal-sepsis
  - leprosy
sources:
  - id: calmette-guerin-original
    type: historical
    cite: "Calmette A, Guérin C. Nouvelles recherches expérimentales sur la vaccination des bovins contre la tuberculose. Ann Inst Pasteur. 1920;34:553-560."
    url: "https://www.pasteur.fr/en/institut-pasteur/history/calmette-guerin"
    note: "Original development record of BCG at Institut Pasteur; first human dose administered 1921."
  - id: colditz-1994-jama-meta-analysis
    type: peer-reviewed
    cite: "Colditz GA, Brewer TF, Berkey CS, et al. Efficacy of BCG Vaccine in the Prevention of Tuberculosis: Meta-analysis of the Published Literature. JAMA. 1994;271(9):698-702."
    doi: "10.1001/jama.1994.03510370053038"
    url: "https://doi.org/10.1001/jama.1994.03510370053038"
    pmid: "8309034"
  - id: moorlag-2020-cell-host-microbe-trained-immunity
    type: peer-reviewed
    cite: "Moorlag SJCFM, Arts RJW, van Crevel R, Netea MG. Non-specific effects of BCG vaccine on viral infections. Cell Host Microbe. 2020;27(6):931-941."
    doi: "10.1016/j.chom.2020.05.013"
    url: "https://doi.org/10.1016/j.chom.2020.05.013"
    pmid: "32497527"
cross_links:
  - target: 02-pathogen/02-bacteria/mycobacterium-tuberculosis
    relation: immunizes-against
    evidence: colditz-1994-jama-meta-analysis
    note: "60–80% efficacy against severe TB (TB meningitis, miliary TB) in children; highly variable 0–80% against adult pulmonary TB."
  - target: 01-human/07-system/immune-system
    relation: elicits
    evidence: moorlag-2020-cell-host-microbe-trained-immunity
    note: "Drives strong Th1 response (IL-12 → IFN-γ); granuloma formation; long-lived CD4+ and CD8+ memory T cells; epigenetic reprogramming of innate monocytes (trained immunity)."
  - target: 01-human/04-cellular/t-helper-cell
    relation: elicits
    evidence: colditz-1994-jama-meta-analysis
    note: "Th1-dominant response critical for macrophage activation and mycobacterial killing; IFN-γ and TNF production."
  - target: 01-human/03-molecular/immunoglobulin-g
    relation: elicits
    note: "Anti-mycobacterial IgG produced, though humoral immunity is secondary to cellular immunity for TB protection."
---

# BCG (Bacillus Calmette-Guérin)

## Overview

**BCG** is a live-attenuated vaccine derived from *Mycobacterium bovis*, first developed by **Albert Calmette** and **Camille Guérin** at the Institut Pasteur in Paris over a period of 13 years (1908–1921). It was prepared by growing *M. bovis* through **230+ serial passages** on a medium of potato bile glycerine — each passage under non-selective pressure gradually attenuated virulence while retaining immunogenicity. The first human dose was administered on **July 18, 1921**, to a newborn in Paris whose mother had died of tuberculosis.

BCG is the **most widely used vaccine in human history** — approximately **100 million doses are given annually**, almost exclusively to neonates and infants. It remains a cornerstone of childhood immunization programs in all countries with meaningful tuberculosis burden, covering roughly 157 countries in WHO's global reporting.

Despite being more than a century old, BCG remains scientifically remarkable for two reasons that are only now being fully understood:

1. **It remains the only licensed vaccine against tuberculosis**, the world's leading single-pathogen infectious disease killer — and efforts to produce something better have been ongoing for 50+ years with only partial breakthroughs (M72/AS01E, VPM1002).
2. **It has nonspecific protective effects** beyond TB — reducing all-cause neonatal mortality, modulating responses to heterologous pathogens — now understood through the lens of **trained innate immunity**, an epigenetic reprogramming of myeloid progenitor cells that enhances their responsiveness to diverse future infections [^moorlag-2020-cell-host-microbe-trained-immunity].

## Antigen & Adjuvant

**Antigen — live attenuated *Mycobacterium bovis* (BCG strain):**

BCG is a replication-competent mycobacterium that undergoes limited multiplication after intradermal injection. It is derived from *M. bovis* (bovine tuberculosis) rather than *M. tuberculosis* (human TB), but the two species share ~99.9% genome identity. Attenuation occurred through the progressive loss of the **RD1 genomic region** (encoding the ESX-1 secretion system, critical for macrophage lysis and virulence) across the years of serial passage — a deletion that is irreversible and prevents reversion to virulence.

After injection, BCG is taken up by **macrophages and dendritic cells** at the intradermal site. It replicates inside the phagosome at the injection site and in draining lymph nodes, preventing phagosomal acidification and lysosomal fusion (using the same mechanisms as virulent *M. tuberculosis*). This intracellular niche allows BCG to:
- Deliver antigens via **MHC class II** (for CD4+ T-helper cell priming)
- Cross-present antigens via **MHC class I** (for CD8+ cytotoxic T-cell priming)
- Activate innate immune PRRs: TLR2/4/9, NOD2, and the NLRP3 inflammasome — via mycobacterial PAMPs (lipoarabinomannan, peptidoglycan, muramyl dipeptide, mycobacterial DNA)

No exogenous adjuvant is needed or used — the live organism's own PAMPs are sufficient to drive robust innate activation.

**Manufacturing:**

Multiple BCG vaccine strains are in use globally, derived from Calmette and Guérin's original culture but now diverged after decades of independent passage in different laboratories: **BCG-Tokyo 172** (Japan BCG Lab), **BCG-Russia**, **BCG-Pasteur 1173P2**, **BCG-Moreau** (Brazil), **BCG-Danish 1331** (Statens Serum Institut), and the **SSI** strain used by Serum Institute of India. These strains differ in immunogenicity and reactogenicity profiles. The **Serum Institute of India** is the largest single producer globally.

BCG is formulated as a **lyophilized (freeze-dried) powder**, reconstituted with sterile saline immediately before use. The lyophilized form is stable at 2–8°C for ~2 years; reconstituted vaccine must be used within 6–8 hours and kept refrigerated.

## Immunogenicity

**Th1 cellular response — the dominant protective arm:**

After BCG vaccination, the primary protective response is **CD4+ Th1 T-cell-mediated** [^colditz-1994-jama-meta-analysis]:
- Macrophages and dendritic cells infected with BCG produce **IL-12**, which drives naive CD4+ T-cell differentiation toward the Th1 phenotype
- Th1 cells produce **IFN-γ**, which in turn activates macrophages to upregulate phagolysosomal fusion, reactive nitrogen intermediates (iNOS), and autophagy — the primary killing mechanisms against *M. tuberculosis*
- **TNF-α** (from both macrophages and Th1 cells) is essential for granuloma formation and bacterial containment
- A local **granuloma** forms at the injection site (the characteristic BCG skin reaction: erythema → papule → pustule → ulceration → scar within 4–12 weeks); this granuloma is the histological footprint of the Th1 response

**CD8+ T cells:**

BCG's intracellular niche enables cross-presentation of mycobacterial antigens via MHC class I, priming **CD8+ cytotoxic T lymphocytes (CTLs)**. CD8+ T-cell responses are important for killing *M. tuberculosis*-infected macrophages and may contribute more to protection in high-burden adults than to pediatric protection from miliary or meningeal disease.

**Memory duration:**

BCG-specific T-cell memory is long-lived — protection against severe TB in children has been documented up to 10–15 years post-vaccination in some studies. Antibody responses (anti-mycobacterial IgG) are induced but are not the primary correlate of protection, consistent with the paradigm that killing of intracellular bacteria is cell-mediated rather than antibody-dependent.

**Trained innate immunity [^moorlag-2020-cell-host-microbe-trained-immunity]:**

BCG is the canonical example of **trained immunity** — a recently characterized epigenetic phenomenon where innate immune cells (monocytes, NK cells, possibly myeloid progenitors in bone marrow) undergo long-lasting functional reprogramming following BCG vaccination. The key molecular mechanism:
- BCG activates monocytes via NOD2 and dectin-1 signaling → downstream activation of PI3K/Akt → upregulation of histone methyltransferase activity
- **H3K4me3** (trimethylation of histone 3 lysine 4, an activating mark) accumulates at promoters of proinflammatory cytokine genes: *IL-6*, *TNF*, *IL-12*, *IL-1β*
- Epigenetically primed monocytes show **enhanced cytokine production and pathogen killing** when subsequently challenged with heterologous stimuli including *Candida albicans*, *Staphylococcus aureus*, influenza virus, and other pathogens
- This is **non-antigen-specific** — the mechanism does not require TCR or BCR recognition of the second pathogen; it operates entirely at the level of innate pattern recognition and chromatin remodeling

## Efficacy & Effectiveness

**Against tuberculosis — Colditz 1994 JAMA meta-analysis [^colditz-1994-jama-meta-analysis]:**

The landmark 1994 meta-analysis (14 randomized trials, 12 case-control studies) remains the definitive quantitative summary:

| TB endpoint | BCG efficacy |
|:---|:---:|
| TB meningitis (children) | ~86% |
| Miliary TB (children) | ~75–80% |
| Any TB (children, high-quality trials) | ~60–80% |
| Adult pulmonary TB | **0–80% (highly variable)** |

The dramatic variability in protection against adult pulmonary TB is the defining scientific puzzle of BCG. Two principal hypotheses have been advanced:
- **Latitude hypothesis (geographic variation):** BCG efficacy correlates inversely with proximity to the equator. In tropical regions, environmental mycobacteria (*M. avium*, *M. kansasii*, *M. marinum*, *M. vaccae*) sensitize children before BCG vaccination, partially depleting or desensitizing the naive T-cell repertoire so BCG provides little additional protection; in northern latitudes (Norway, UK, US clinical trials in the 1950s), where environmental mycobacteria are rare, BCG efficacy reached 70–80%.
- **BCG strain variation:** Different BCG strains vary in their genomic content and immunogenicity; strains produced in the mid-20th century after extensive independent passage may have diverged in protective capacity.

**Against neonatal all-cause mortality:**

Multiple randomized trials in Guinea-Bissau, Bangladesh, and South Africa demonstrated that BCG at birth reduces **all-cause neonatal mortality by ~38%**, an effect far larger than would be expected from TB prevention alone in this age group. This excess protection is now attributed to **trained innate immunity** — enhanced killing of neonatal sepsis pathogens (*S. aureus*, *E. coli*, group B Streptococcus) via epigenetically reprogrammed monocytes and NK cells, not via antigen-specific T-cell responses [^moorlag-2020-cell-host-microbe-trained-immunity].

**Against leprosy:**

BCG provides 20–80% protection against *Mycobacterium leprae* (leprosy). The variability again correlates with latitude / environmental mycobacteria exposure. This cross-protection, together with the trained-immunity findings, has expanded the conceptual model of BCG from a narrow TB vaccine to a broad innate immune modulator.

**Against adult pulmonary TB reactivation:**

BCG is largely **ineffective** at preventing reactivation of latent *M. tuberculosis* infection in adults in high-burden countries. This gap drives the tuberculosis vaccine pipeline: next-generation candidates include **M72/AS01E** (GSK + Wellcome Trust; phase 2b: 54% VE against active TB in LTBI-positive adults), **VPM1002** (recombinant BCG overexpressing listeriolysin O), and **MTBVAC** (live attenuated *M. tuberculosis* itself). BCG **revaccination** of adults with LTBI is being tested in the **REVIMMUNE/BCG RISK trial**, following observational data from the Chingleput trial suggesting that a second dose in adults provides some protection.

## Connections

BCG's position in the four-atlas knowledge graph spans three scales of biological organization:

- **Immunizes against** → [`02-pathogen/02-bacteria/mycobacterium-tuberculosis`](../../../../02-pathogen/02-bacteria/mycobacterium-tuberculosis/README.md) — 60–80% efficacy severe pediatric TB; variable for adult pulmonary TB
- **Elicits** → [`01-human/immune-system`](../../../../01-human/immune-system/README.md) — canonical Th1 IL-12/IFN-γ axis; granuloma formation; CD4+ and CD8+ memory; trained innate immunity of monocytes and NK cells
- **Elicits** → [`01-human/04-cellular/t-helper-cell`](../../../../01-human/04-cellular/t-helper-cell/README.md) — Th1 dominant; IFN-γ and TNF-α the critical effector cytokines for macrophage activation
- **Produces** → [`01-human/03-molecular/immunoglobulin-g`](../../../../01-human/03-molecular/immunoglobulin-g/README.md) — anti-mycobacterial IgG, secondary to cellular arm
- **Platform contrast** → [`04-vaccine/04-inactivated/coronavac`](../../04-inactivated/coronavac/README.md) — whole inactivated vs. live-attenuated; BCG has no alum adjuvant, elicits stronger cellular response, but cannot be used in SCID
- **Trained-immunity contrast** → [`04-vaccine/01-mrna/mrna-1273`](../../01-mrna/mrna-1273/README.md) — mRNA vaccines do not produce trained innate immunity; BCG's epigenetic reprogramming of myeloid cells is unique to live-attenuated platforms

## Safety

BCG has an excellent safety record accumulated over **100 years of use** and **100 million doses per year**. However, specific risks must be understood because the vaccine contains a live replicating organism.

**Expected local reaction:**

Intradermal BCG injection produces a **predictable local reaction sequence** at the injection site (typically the left upper arm):
- Week 1–2: small erythematous papule (2–5 mm)
- Week 2–4: papule enlarges and may become pustular / ulcerate
- Week 4–12: ulcer heals; a small flat scar (2–10 mm) remains permanently

This scar is **expected and desirable** — it is the clinical marker of successful BCG vaccination, confirmed by trained healthcare workers. Absence of scar (~5–10% of vaccinees) does not reliably predict failed immunization, but revaccination may be considered in some national programs.

**BCG-itis (regional lymphadenopathy):**

Ipsilateral axillary or supraclavicular lymphadenopathy occurs in **1–2% of vaccinees**, usually within 2–6 months of vaccination. Most cases resolve spontaneously. Suppurative lymphadenitis (abscess formation) occurs in ~0.1–0.4% and may require aspiration or isoniazid therapy. This is more common with some BCG strains (notably BCG-Japan 172) and in younger neonates.

**Disseminated BCG disease:**

The most serious adverse event. Occurs in children with severe combined immunodeficiency (**SCID**), complete **IFN-γ receptor deficiency**, **IL-12/IL-12R pathway defects**, or **HIV with advanced immunosuppression**. BCG replicates uncontrolled when cell-mediated immunity is absent, seeding bone, lymph nodes, liver, spleen, and CNS. Fatal if untreated; treatment requires multi-drug anti-mycobacterial therapy. Global incidence: **0.06–1.56 per 100,000** vaccinees, with the upper end in settings where neonatal HIV exposure is high and where BCG is given at birth before HIV status of the infant is known.

**This is the reason BCG is contraindicated in:**
- Known SCID or primary immunodeficiency
- HIV-infected infants with CD4 count below threshold (WHO has specific guidelines by age)
- Individuals on high-dose systemic corticosteroids or biologic immunosuppression

**Keloid formation:**

Hypertrophic scarring or keloid at the injection site occurs more commonly in darker-skinned individuals (~1–3%) and is a cosmetic concern. Technique (correct intradermal placement, correct dose volume of 0.1 mL) reduces but does not eliminate this risk.

**No association** with:
- Disseminated disease in immunocompetent individuals
- BCG-induced TB — the attenuated organism cannot cause pulmonary TB
- Autoimmune sequelae

---

**[← Platform 05 (Live-Attenuated)](../README.md)** · **[← Vaccine Atlas](../../README.md)** · **[Schema](../../../../schemas/vaccine-entry.schema.md)**
