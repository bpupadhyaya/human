# Scale 06 — Organ

Tissues coordinated into a single functional unit.

**[← Atlas One — Human](../README.md)** · **[← Atlases index](../../README.md)** · **[← Project README](../../../README.md)**

---

## What this scale captures

An organ is the unit at which most of clinical medicine operates. A patient comes in with chest pain — the question is *which organ*. An MRI shows a mass — *in which organ*. A drug is dosed for *which organ's* failing function. Organs are also the scale at which symptoms become legible, surgery becomes possible, and most public-health statistics are kept.

Entries at this scale describe **anatomy (gross and sub-gross), physiology (how the organ does its job), and pathology (how it fails)** — and bind together the tissues that compose it, the system it belongs to, and the diseases that target it.

## Entries in this scale

| Entry | Role |
|:---|:---|
| **[Heart](heart/README.md)** | Four-chambered muscular pump driving the cardiovascular system. |

*More organ entries will appear as the atlas grows. Required structure is defined in [`schemas/human-scale-entry.schema.md`](../../../schemas/human-scale-entry.schema.md).*

## Connections to other scales

- **Up to [07-system](../07-system/README.md)** — organs participate in larger systems (heart + vasculature + blood = cardiovascular system; kidneys + bladder + ureters = urinary system).
- **Down to [05-tissue](../05-tissue/README.md)** — `contains` links point down to the tissues that make up the organ.

## Cross-atlas connections

This is the scale at which many cross-atlas bridges become clinically meaningful:
- **Pathogens** *damage* organs (myocarditis damages heart; hepatitis damages liver). The pathogen-atlas back-links target an organ as the unit of clinical injury.
- **Medicines** *modulate* organ function (β-blockers slow the heart; diuretics offload the kidney). Drug labels are often organized by organ-system effect.

---

**[← Atlas One — Human](../README.md)** · **[← Atlases index](../../README.md)**
