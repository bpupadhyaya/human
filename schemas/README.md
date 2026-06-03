# `schemas/` — Data Contracts & Entry Templates

Shared specifications that **multiple parts of the project must agree on**. Atlas entry templates, dataset schemas, API contracts, inter-project message formats.

**[← Back to project README](../README.md)**

---

## What lives here

Schemas are the **interface layer** of the project. When two things — an atlas entry and a classifier model, a dataset and a validation script, two different agents — need to agree on a structure, that structure lives here.

```
schemas/
├── medicine-entry.schema.md           # template for every Medicine Atlas entry
├── pathogen-entry.schema.md           # template for every Pathogen Atlas entry
├── human-scale-entry.schema.md        # template for Human Atlas scale entries
├── citation.schema.json               # citation format (DOI / PubMed / textbook / oral)
├── binding-affinity.schema.json       # for protein-ligand binding datasets
└── agent-config.schema.json           # for agent prompt + tool definitions
```

Sub-folders are not used — schemas are referenced often, so a flat namespace keeps lookup easy.

---

## Format

Two styles, depending on consumer:

### `.schema.md` — Human-authored, prose-and-table format
For atlas entry templates and other schemas read primarily by humans (and Claude).

```markdown
# Medicine Atlas Entry Schema

Every entry in the Medicine Atlas conforms to this structure:

## Required sections
- Name & class
- Origin / tradition
- Mechanism of action
- Evidence
- ...

## Optional sections
- Cultural context
- Open questions
- ...
```

### `.schema.json` — Machine-readable, JSON Schema format
For dataset schemas and API contracts read by tooling.

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://human-engineering.org/schemas/citation.schema.json",
  "title": "Citation",
  ...
}
```

If a schema is used by **both** humans and machines, write both files (`citation.schema.md` + `citation.schema.json`) and link them to each other.

---

## Naming

`<name>.schema.<ext>` — the `.schema` infix makes them grep-able and signals "this is a contract, not content".

- ✅ `medicine-entry.schema.md`
- ✅ `binding-affinity.schema.json`
- ❌ `medicine_template.md` (no `.schema` marker)
- ❌ `MedicineEntrySchema.md` (PascalCase)

---

## Required: every schema lists its consumers

At the top of every schema, list **which atlases, datasets, projects, and notebooks consume it**. This makes blast radius visible before a schema change.

```markdown
# Medicine Atlas Entry Schema

**Consumers:**
- atlases/03-medicine/*/  (all entries follow this)
- comp-prog-proj/medicine-entry-validator/
- comp-prog-proj/medicine-graph/  (deserialization)
- notebooks/2026-07-medicine-coverage-analysis/
```

When you propose a schema change, the consumer list tells you who needs to update.

---

## Versioning

For schemas that have **machine consumers** (validators, classifiers, agents):

- The first stable version is `v1` (declare in the schema file).
- Breaking changes bump to `v2`; keep `v1` until all consumers migrate.
- Non-breaking additions (new optional fields) stay on the same version.

For schemas that have **only human consumers** (atlas entry templates):

- No versioning. Update in place. Note significant changes in a `CHANGELOG.md` at the bottom of the schema file.

---

## How others reference schemas

From an atlas entry:

```markdown
> **Schema:** This entry follows [`schemas/medicine-entry.schema.md`](../../../schemas/medicine-entry.schema.md).
```

From a project:

```python
# Reference in code via path; validate at runtime
from jsonschema import validate
import json

SCHEMA = json.load(open("../../schemas/citation.schema.json"))
validate(instance=my_citation, schema=SCHEMA)
```

---

## What does NOT go here

- Instance data conforming to a schema → `data/`
- Documentation about the project as a whole → `atlases/` or root `README.md`
- Project-internal data structures (not shared across boundaries) → keep inside the project

---

**[← Back to project README](../README.md)**
