# Scale 04 — Cellular

The smallest unit that is unambiguously alive.

**[← Atlas One — Human](../README.md)** · **[← Atlases index](../../README.md)** · **[← Project README](../../../README.md)**

---

## What this scale captures

A cell is a self-maintaining boundary, an internal economy of metabolism, and a copy of the genome — at minimum. The human body contains roughly 30 trillion cells across about 200 named cell types, and each type is a different specialization of the same basic plan.

Entries at this scale describe **morphology, lifecycle, and the molecules a cell expresses or makes** — what it looks like, where it comes from, what it does, when it dies, and how to recognize it.

## Entries in this scale

| Entry | Role |
|:---|:---|
| **[Cardiomyocyte](cardiomyocyte/README.md)** | The contractile cell of the heart. |

*More cellular entries will appear as the atlas grows. Required structure is defined in [`schemas/human-scale-entry.schema.md`](../../../schemas/human-scale-entry.schema.md).*

## Connections to other scales

- **Up to [05-tissue](../05-tissue/README.md)** — tissues are organized populations of cells. A cell entry's `part-of` link points up to its tissue.
- **Down to [03-molecular](../03-molecular/README.md)** — a cell's behavior is the integral of its expressed molecules. `expresses` cross-links point down to specific molecular entries.

## Cross-atlas connections

- **Pathogens** *infect* cells — host-cell tropism is defined at this scale (Coxsackievirus B targets cardiomyocytes via CAR; HIV targets CD4⁺ T cells via CD4/CCR5).
- **Medicines** can act at the cellular scale (cytotoxics, growth-factor agonists), though most act at the molecular scale and the cellular scale is where the *effect* is observed.

---

**[← Atlas One — Human](../README.md)** · **[← Atlases index](../../README.md)**
