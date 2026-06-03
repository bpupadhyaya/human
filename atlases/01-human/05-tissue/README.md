# Scale 05 — Tissue

Cells specialized and organized into functional fabrics.

**[← Atlas One — Human](../README.md)** · **[← Atlases index](../../README.md)** · **[← Project README](../../../README.md)**

---

## What this scale captures

A tissue is a population of cells, plus the extracellular matrix between them, working together. Classical histology recognizes four basic types — epithelial, connective, muscle, nervous — but the body contains hundreds of named tissues if you count specialized variants (cardiac muscle vs. skeletal muscle vs. smooth muscle; cortical bone vs. trabecular bone; retinal pigment epithelium vs. simple cuboidal).

Entries at this scale describe **cellular composition, architecture, and function** — which cells live in this tissue, how they are arranged, and what the tissue does as a coherent unit.

## Entries in this scale

| Entry | Role |
|:---|:---|
| **[Myocardium](myocardium/README.md)** | The contractile muscle layer of the heart wall. |

*More tissue entries will appear as the atlas grows. Required structure is defined in [`schemas/human-scale-entry.schema.md`](../../../schemas/human-scale-entry.schema.md).*

## Connections to other scales

- **Up to [06-organ](../06-organ/README.md)** — organs are coordinated assemblies of tissues. A tissue entry's `part-of` link points up to its organ.
- **Down to [04-cellular](../04-cellular/README.md)** — `composed-of` links point down to the cell types that constitute the tissue.
- **Sideways to [03-molecular](../03-molecular/README.md)** — extracellular matrix molecules (collagens, elastin, fibronectin) operate at the tissue scale but are entries at the molecular scale.

## Cross-atlas connections

- **Pathogens** can damage tissues directly (necrosis, edema) or via immune-mediated injury.
- **Medicines** rarely target a tissue *as such* — most act on a molecule expressed by tissue cells. The tissue is where the effect manifests.

---

**[← Atlas One — Human](../README.md)** · **[← Atlases index](../../README.md)**
