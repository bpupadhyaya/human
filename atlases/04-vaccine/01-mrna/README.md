<div align="center">

# Platform 01 — mRNA Vaccines

### Modified-nucleoside and self-amplifying RNA vaccines

**[← Vaccine Atlas](../README.md)** · **[← Atlases index](../../README.md)** · **[← Project README](../../../README.md)**

</div>

---

## What this platform is

An mRNA vaccine **delivers a synthetic messenger RNA encoding the target antigen into host cells**, where the cell's own ribosomes translate the mRNA into protein, present that protein to the immune system, and elicit antibody and T-cell responses. The RNA itself is degraded within days; nothing integrates into the genome.

Two sub-platforms are in clinical use:

- **Modified-nucleoside mRNA** — uses N1-methylpseudouridine (or pseudouridine) substitution to evade innate-immune RNA sensors and increase translation. The chemistry is the work of **Katalin Karikó and Drew Weissman** (2005; Nobel Prize in Physiology or Medicine, 2023). All three first-generation COVID-19 mRNA vaccines (mRNA-1273, BNT162b2, CVnCoV) used this chemistry.
- **Self-amplifying mRNA (saRNA)** — the mRNA encodes both the antigen *and* a viral replicase (typically alphavirus-derived) that amplifies the mRNA inside the cell, allowing much smaller doses. Approved examples: Arcturus ARCT-154, CSL-Arcturus Kostaive (2024).

Both are typically delivered in a **lipid nanoparticle (LNP)** — four-lipid mixture (ionizable cationic lipid, PEG-lipid, cholesterol, helper phospholipid) that encapsulates the mRNA, protects it from nucleases, and enables endosomal escape after cellular uptake.

---

## Why mRNA was the COVID-19 platform that shipped first

mRNA vaccines compress the design phase to days because **the only design step is the mRNA sequence** — no live organism culture, no protein expression and purification, no inactivation chemistry. Once the pathogen genome is sequenced, a candidate mRNA can be designed in silico and synthesized within days. mRNA-1273 went from sequence release (Jan 11, 2020) to first clinical batch shipped to NIH (Feb 24, 2020) — roughly six weeks.

The slow steps for mRNA vaccines are clinical trials and manufacturing scale-up — *not* the molecular design — which is exactly why this platform is central to the project's mission of collapsing pathogen-detected → vaccine-shipped to hours.

---

## Common architecture

| Component | Role |
|:---|:---|
| **5′ cap** | Anti-Reverse Cap Analog (ARCA) or enzymatic capping. Required for ribosome recruitment. |
| **5′ UTR** | Optimized for translation efficiency (often α-globin or human-derived). |
| **Coding sequence** | Codon-optimized antigen, often with structure-stabilizing modifications (2P, hexapro for spike). |
| **3′ UTR** | Stabilizes mRNA, extends half-life (often β-globin-derived). |
| **Poly(A) tail** | 100–150 nt; required for ribosome stability. |
| **Modified nucleosides** | N1-methylpseudouridine replaces uridine — evades TLR7/8/RIG-I, increases translation 10–1000×. |
| **LNP** | Encapsulation, protection, cellular delivery, endosomal escape. |

---

## Entries

| Entry | Status | Target | Developer |
|:---|:---|:---|:---|
| **[mrna-1273](mrna-1273/README.md)** (Spikevax) | draft | SARS-CoV-2 | Moderna + NIAID/VRC |
| **[bnt162b2](bnt162b2/README.md)** (Comirnaty) | stub | SARS-CoV-2 | Pfizer + BioNTech |

Planned: ARCT-154 (Kostaive, saRNA), CVnCoV (CureVac, discontinued; useful negative result), updated bivalent / monovalent SARS-CoV-2 boosters, mRNA-1345 (RSV), mRNA-4157 (personalized melanoma neoantigen, investigational).

---

**[← Vaccine Atlas](../README.md)** · **[Schema](../../../schemas/vaccine-entry.schema.md)**
