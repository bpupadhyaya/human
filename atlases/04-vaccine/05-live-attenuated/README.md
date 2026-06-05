<div align="center">

# Platform 05 — Live-Attenuated Vaccines

### Replication-competent attenuated pathogen vaccines

**[← Vaccine Atlas](../README.md)** · **[← Atlases index](../../README.md)** · **[← Project README](../../../README.md)**

</div>

---

## What this platform is

A live-attenuated vaccine contains **replication-competent pathogens whose virulence has been reduced by serial passage, genetic modification, or selection** so that they can infect and replicate briefly in the host without causing disease in immunocompetent individuals. The limited replication closely mimics natural infection, allowing the immune system to encounter antigens via the same cellular machinery as the wild-type pathogen — producing **robust, long-lived, broad cellular and humoral immunity**, typically from a single dose.

Key characteristics of the platform:

- **Replication-competent** — the attenuated pathogen undergoes limited multiplication at the inoculation site and/or draining lymph nodes; antigen persistence is longer than non-replicating platforms, fueling stronger germinal-center reactions and durable T-cell memory
- **Broad antigen presentation** — MHC class I and II processing occurs naturally during intracellular replication, generating CD4+, CD8+, and B-cell responses simultaneously; no need for exogenous adjuvant
- **Long-lived immunity** — single-dose protection lasting decades (or lifetime) is common (yellow fever vaccine, for example); memory T-cell responses outlast antibody titers
- **Nonspecific (trained immunity) effects** — some live-attenuated vaccines (notably BCG) epigenetically reprogram innate immune cells to enhance heterologous pathogen defense; this is over and above antigen-specific protection
- **Contraindicated in severe immunodeficiency** — replication-competent vaccines can cause disseminated disease in individuals with SCID, HIV with CD4 < 200, or on high-dose immunosuppression; careful screening is required
- **Typically single dose** — most live-attenuated vaccines in routine use are single-dose; oral poliovirus (OPV/Sabin) is a notable exception requiring 3 doses for full seroconversion
- **Cold chain: 2–8°C (lyophilized)** — lyophilization confers thermostability superior to liquid formulations; reconstitution with sterile diluent is required before use; must be used within hours of reconstitution

---

## Common architecture

| Component | Role |
|:---|:---|
| **Attenuated pathogen** | Replication-competent organism with virulence determinants deleted, mutated, or outgrown by serial passage; cannot revert to wild-type in most cases |
| **Stabilizers** | Sucrose, gelatin, sorbitol, lactose — protect viability during lyophilization and storage |
| **Diluent** | Sterile water or buffered saline; supplied separately; vaccine reconstituted immediately before injection |
| **No adjuvant** | Innate sensing of live pathogen PAMPs (LPS, peptidoglycan, flagellin, dsRNA) substitutes for exogenous adjuvant |

---

## Entries

| Entry | Status | Target | Developer |
|:---|:---|:---|:---|
| **[BCG](bcg/README.md)** (Bacillus Calmette-Guérin) | draft | Mycobacterium tuberculosis | Multiple (Serum Institute of India, Japan BCG Lab, others) |

Planned: MMR (measles-mumps-rubella, Merck M-M-R II / GSK Priorix), OPV Sabin (oral poliovirus types 1/2/3), varicella (Varivax), yellow fever (YF-VAX / Stamaril), oral typhoid Ty21a (Vivotif), rotavirus (Rotarix, RotaTeq), MMRV (ProQuad), dengue (Dengvaxia — chimeric yellow fever/dengue, special case).

---

**[← Vaccine Atlas](../README.md)** · **[Schema](../../../schemas/vaccine-entry.schema.md)**
