# Cross-Link Schema

The structure of every edge in the project's knowledge graph. A cross-link is how an entry references another entry — within an atlas, or across atlases.

> **Machine-readable companion:** [`cross-link.schema.json`](cross-link.schema.json) — JSON Schema for validators.

**Consumers:**
- `atlases/*/**/README.md` (every atlas entry's `cross_links` array)
- `tools/scripts/validate-entries.py`
- `comp-prog-proj/*/` (any project that walks the knowledge graph)

---

## Why this exists

The project's central claim is that the three atlases together form a **navigable knowledge graph** — not three separate lists. The graph is only as good as the edges. A common edge schema makes those edges:

- **Validatable** — every link resolves to a real entry, every relation is from a controlled vocabulary.
- **Queryable** — agents and tools can answer "what does this drug target?" or "which pathogens damage cardiomyocytes?" by walking edges.
- **Symmetric where appropriate** — the validator can flag missing back-links (e.g., heart `damaged-by` Coxsackievirus B should imply Coxsackievirus B `damages` heart).

---

## Fields

| Field | Required | Type | Description |
|:---|:---:|:---|:---|
| `target` | ✅ | string | Path relative to `atlases/`, with no file extension. Format: `<atlas>/<...>/<entry-id>`. Examples: `01-human/06-organ/heart`, `02-pathogen/viruses/coxsackievirus-b`. |
| `relation` | ✅ | enum | One of the controlled relation names below. The validator additionally checks that the chosen relation is *legal* for this `(source-atlas, target-atlas)` pair. |
| `scale` | optional | enum | Scale at which the interaction takes place. Use when the target entry exists at multiple scales of relevance (e.g., a virus binds at the molecular scale but causes symptoms at the organ scale). One of: `01-subatomic`, `02-atomic`, `03-molecular`, `04-cellular`, `05-tissue`, `06-organ`, `07-system`, `08-whole-body`. |
| `evidence` | optional | string | An `id` from this entry's `sources` array — the citation that supports the claim of this link. Strongly preferred for cross-atlas links. |
| `note` | optional | string | One-line clarification. Specific receptor, specific tissue, specific mechanism. |

---

## Controlled relation vocabulary

Relations are atlas-pair-aware. The validator enforces that the chosen relation matches the source/target atlas combination.

### Within Human Atlas (01-human → 01-human)

| Relation | Direction | Use |
|:---|:---|:---|
| `contains` | larger → smaller | Heart `contains` myocardium |
| `part-of` | smaller → larger | Myocardium `part-of` heart |
| `composed-of` | tissue/organ → cell-types/molecules | Myocardium `composed-of` cardiomyocyte |
| `connects-to` | sibling at same scale | Heart `connects-to` lungs (via pulmonary circulation) |
| `regulates` | functional control | Sympathetic-system `regulates` heart |
| `secretes` | producer → product | Cardiomyocyte `secretes` ANP |
| `expresses` | cell → molecule | Cardiomyocyte `expresses` β1-adrenergic-receptor |
| `innervated-by` | tissue/organ → nerve-system | Heart `innervated-by` autonomic-nervous-system |
| `vascularized-by` | tissue/organ → vessels | Myocardium `vascularized-by` coronary-arteries |

### Human → Pathogen (01-human → 02-pathogen)

| Relation | Use |
|:---|:---|
| `infected-by` | Cardiomyocyte `infected-by` coxsackievirus-b |
| `damaged-by` | Heart `damaged-by` coxsackievirus-b |
| `defends-against` | Immune-system `defends-against` coxsackievirus-b |

### Human → Medicine (01-human → 03-medicine)

| Relation | Use |
|:---|:---|
| `target-of` | β1-adrenergic-receptor `target-of` metoprolol |
| `modulated-by` | Heart `modulated-by` metoprolol |

### Pathogen → Human (02-pathogen → 01-human)

| Relation | Use |
|:---|:---|
| `infects` | Coxsackievirus-b `infects` cardiomyocyte |
| `damages` | Coxsackievirus-b `damages` heart |
| `evades` | Coxsackievirus-b `evades` immune-system |

### Pathogen → Medicine (02-pathogen → 03-medicine)

| Relation | Use |
|:---|:---|
| `treated-by` | Coxsackievirus-b `treated-by` ivig |
| `prevented-by` | Sars-cov-2 `prevented-by` mrna-vaccine |
| `resistant-to` | Mrsa `resistant-to` methicillin |

### Medicine → Human (03-medicine → 01-human)

| Relation | Use |
|:---|:---|
| `targets` | Metoprolol `targets` β1-adrenergic-receptor |
| `modulates` | Metoprolol `modulates` heart |

### Medicine → Pathogen (03-medicine → 02-pathogen)

| Relation | Use |
|:---|:---|
| `treats` | Acyclovir `treats` herpes-simplex-virus-1 |
| `prevents` | Mrna-vaccine `prevents` sars-cov-2 |

### Within atlases (peer relations)

| Relation | Atlas | Use |
|:---|:---|:---|
| `analogue-of` | medicine → medicine | Atenolol `analogue-of` metoprolol |
| `combined-with` | medicine → medicine | Lisinopril `combined-with` hydrochlorothiazide |
| `mutates-from` | pathogen → pathogen | Sars-cov-2-omicron `mutates-from` sars-cov-2-delta |
| `co-infects-with` | pathogen → pathogen | HIV `co-infects-with` mycobacterium-tuberculosis |

---

## Inverse-link rules

Many relations have a defined inverse. The validator flags missing inverses.

| Relation | Inverse |
|:---|:---|
| `contains` | `part-of` |
| `composed-of` | `part-of` |
| `infected-by` | `infects` |
| `damaged-by` | `damages` |
| `target-of` | `targets` |
| `modulated-by` | `modulates` |
| `treated-by` | `treats` |
| `prevented-by` | `prevents` |

`connects-to`, `combined-with`, `co-infects-with`, `analogue-of` are symmetric — both sides must declare the link.

`regulates`, `secretes`, `expresses`, `innervated-by`, `vascularized-by`, `evades`, `mutates-from` are directional and have no required inverse.

---

## Examples

### Heart entry referencing its tissue and a pathogen

```yaml
---
id: heart
atlas: 01-human
scale: 06-organ
cross_links:
  - target: 01-human/05-tissue/myocardium
    relation: contains
  - target: 01-human/05-tissue/endocardium
    relation: contains
  - target: 01-human/07-system/cardiovascular-system
    relation: part-of
  - target: 02-pathogen/viruses/coxsackievirus-b
    relation: damaged-by
    scale: 04-cellular
    evidence: pollack-2015-myocarditis-review
    note: "Cytolytic infection of cardiomyocytes; immune-mediated inflammation amplifies."
  - target: 03-medicine/cardiovascular/metoprolol
    relation: modulated-by
    scale: 03-molecular
    note: "Acts via β1-adrenergic-receptor; reduces HR and contractility."
---
```

### Coxsackievirus B entry — the inverse links

```yaml
---
id: coxsackievirus-b
atlas: 02-pathogen
cross_links:
  - target: 01-human/04-cellular/cardiomyocyte
    relation: infects
    scale: 04-cellular
  - target: 01-human/06-organ/heart
    relation: damages
    scale: 06-organ
---
```

---

## Validation rules (enforced by `tools/scripts/validate-entries.py`)

1. `target` must resolve to an existing entry (a `README.md` at the path `atlases/<target>/README.md`).
2. `relation` must be in the global enum.
3. `(source-atlas, target-atlas, relation)` must be a legal triple per the tables above.
4. If `relation` has a defined inverse, the target entry must declare the inverse back-link to this entry. Missing back-links are warnings (not errors) so authors can land one side first.
5. If `scale` is set, it must be one of the 8 valid scales.
6. If `evidence` is set, it must match an `id` in the source entry's `sources` array.

---

**[← Back to schemas index](README.md)**
