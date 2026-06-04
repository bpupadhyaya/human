<div align="center">

# Atlas Four — The Vaccine Atlas

### Every vaccine humanity has used or is testing

The designed bridges between the [Human Atlas](../01-human/README.md) and the [Pathogen Atlas](../02-pathogen/README.md).

**[← Atlases index](../README.md)** · **[← Project README](../../README.md)**

[![License: MIT](https://img.shields.io/badge/License-MIT-00d9a3.svg?style=for-the-badge)](../../LICENSE)
[![In Progress](https://img.shields.io/badge/Status-Building-3aa9ff.svg?style=for-the-badge)](#help-build-the-atlas)
[![For Humanity](https://img.shields.io/badge/Built%20for-Humanity-ffb86b.svg?style=for-the-badge)](#)

</div>

---

> *"When the next fast-mutating pathogen appears, a candidate vaccine should be hours away — not months or years."*

The Vaccine Atlas catalogs every vaccine humanity has built, abandoned, or is investigating — modeled at the same standard of rigor as the Human and Pathogen atlases. It is the project's **central output artifact**: the thing the AI agent is ultimately being trained to design.

---

## Why a dedicated Vaccine Atlas?

The earliest framing of the project treated vaccines as one entry type within the [Medicine Atlas](../03-medicine/README.md). They are no longer. Vaccines are promoted to their own top-level atlas because:

- **Vaccines are the project's mission output.** Every other atlas exists to give the AI agent enough context to *design* a vaccine. The output deserves its own first-class home.
- **Cross-atlas relations read more naturally.** A vaccine `immunizes-against` a pathogen, `elicits` a response in the human immune system, is `same-platform-as` another vaccine. Burying these relations under "medicine" loses semantic clarity.
- **Vaccine taxonomy doesn't fit drug taxonomy.** Vaccines are organized by *platform* (mRNA, viral-vector, inactivated, ...) — fundamentally different from how drugs are organized (by class / target / indication).

Therapeutic medicines remain in the Medicine Atlas. Vaccines — preventive or therapeutic — live here.

---

## What this atlas captures

Every entry covers a single vaccine product (or vaccine candidate, or discontinued vaccine) with a complete profile:

- **Platform** — the underlying technology
- **Antigen design** — what the immune system actually sees, including modifications (e.g., 2P prefusion stabilization)
- **Delivery system** — LNP, viral capsid, adjuvanted protein, attenuated organism
- **Mechanism of immunity** — humoral, cellular, mucosal arms; correlates of protection
- **Manufacturing** — cell substrate, scale, cold chain, supply constraints
- **Trials** — Phase 1/2/3 designs, NCT IDs, primary endpoints, efficacy
- **Regulatory** — authorization timeline across global regulators
- **Safety** — adverse-event profile with rates and mechanisms
- **Variation & equity** — how response differs across populations; access by region

The full schema is documented in [`schemas/vaccine-entry.schema.md`](../../schemas/vaccine-entry.schema.md).

---

## The Platform Ladder

The atlas is organized by platform — fundamentally different technologies with different design constraints, manufacturing pipelines, and immune profiles. **Inclusive by design** — ancient, modern, traditional, investigational, and discontinued vaccines all fit.

| # | Platform | Examples | Status |
|:---:|:---|:---|:---|
| 01 | **[mRNA](01-mrna/README.md)** | mRNA-1273, BNT162b2, ARCT-154 | Building |
| 02 | **Viral vector** | AZD1222 (ChAdOx1), Ad26.COV2.S, Sputnik V, rVSV-ZEBOV | Planned |
| 03 | **Recombinant subunit** | NVX-CoV2373, Engerix-B (HBV), Shingrix | Planned |
| 04 | **Inactivated whole pathogen** | CoronaVac, Sinopharm, Covaxin, IPV (Salk), inactivated influenza | Planned |
| 05 | **Live attenuated** | MMR, BCG, OPV (Sabin), varicella, yellow fever, oral typhoid, rotavirus | Planned |
| 06 | **Virus-like particle (VLP)** | Gardasil-9, Cervarix, Hep E (Hecolin) | Planned |
| 07 | **Conjugate (polysaccharide–protein)** | Hib, PCV13/15/20, MenACWY-CRM | Planned |
| 08 | **Pure polysaccharide** | PPSV23, MPSV4 | Planned |
| 09 | **Toxoid** | Tetanus, diphtheria | Planned |
| 10 | **DNA** | ZyCoV-D, INO-4800 | Planned |
| 11 | **Peptide / epitope** | Investigational cancer vaccines | Planned |
| 12 | **Dendritic-cell / cellular** | Sipuleucel-T (Provenge) | Planned |
| 13 | **Plant-based protein** | Covifenz (discontinued) | Planned |
| 14 | **Bacterial vector** | Listeria-, Salmonella-vectored cancer vaccines | Planned |
| 99 | **Other / hybrid** | Novel platforms not yet categorized | Reserved |

Combination vaccines (DTaP, MMRV, hexavalent) live under their dominant platform; component antigens are recorded in `antigens:`.

---

## Connections to other atlases

Every vaccine entry is cross-referenced with the other three atlases:

- **Into the [Pathogen Atlas](../02-pathogen/README.md)** — `immunizes-against`, `targets-antigen-of`, `cross-protects-against`. Every vaccine targets at least one pathogen.
- **Into the [Human Atlas](../01-human/README.md)** — `elicits` (immune response), `induces-memory-in` (B/T cells), `delivered-via` (target tissue / cell type). The mechanism of protection lives at the Human Atlas immune-system level.
- **Into the [Medicine Atlas](../03-medicine/README.md)** — `contains-adjuvant`, `analogue-of` (same-platform alternatives).

These cross-references are what make the Vaccine Atlas the **interconnected node** the AI agent traverses when designing the next vaccine.

---

## What's planned

```
04-vaccine/
├── README.md                 (this file — overview)
├── 01-mrna/
│   ├── README.md
│   ├── mrna-1273/            (Moderna; Spikevax)
│   ├── bnt162b2/             (Pfizer-BioNTech; Comirnaty)
│   └── ...
├── 02-viral-vector/
├── 03-recombinant-subunit/
├── 04-inactivated/
├── 05-live-attenuated/
├── 06-virus-like-particle/
├── 07-conjugate/
├── 08-polysaccharide/
├── 09-toxoid/
├── 10-dna/
├── 11-peptide/
├── 12-dendritic-cell/
├── 13-plant-based/
├── 14-bacterial-vector/
└── 99-other/
```

Initial focus: COVID-19 vaccine family across platforms 01–04 (the most extensively-studied and best-documented vaccine family in human history) — a worked proof of concept for the four-atlas knowledge graph. Childhood / routine vaccines (MMR, BCG, polio, DTaP, HPV) follow.

---

## Help build the Atlas

Vaccinologists, immunologists, clinical-trial experts, manufacturing scientists, regulatory specialists, public-health workers, and historians of medicine — see the [project contribution guide](../../README.md#how-to-contribute), or contact **[bpupadhyaya@gmail.com](mailto:bpupadhyaya@gmail.com?subject=Vaccine%20Atlas%20%E2%80%94%20I'd%20like%20to%20contribute)**.

---

<div align="center">

### Free, for everyone, forever.

*Every vaccine humanity has built — modeled openly, so the next one is hours away.*

**[← Atlases index](../README.md)** · **[← Project README](../../README.md)**

</div>
