# Relation Vocabulary Schema (controlled enum of edge types)

The **controlled list of relation names** that every cross-link in the project's knowledge graph must use, with formal mappings to OBO Foundry ontologies (RO, BFO) so the graph is interoperable with external biomedical reasoning tools.

> **Status:** Proposal — supersedes the relation tables currently embedded in [`cross-link.schema.md`](cross-link.schema.md). The intent is that `cross-link.schema.md` keeps only the *edge data structure* (target/scale/evidence/note fields) and defers the *vocabulary* to this file, so the two concerns are cleanly separated.

**Consumers:**
- All atlas entries (every `cross_links[].relation` must be a member here)
- `tools/scripts/validate-entries.py`
- The graph-build step that emits JSON-LD / RDF — uses RO/BFO mappings to assign each edge a stable IRI
- Any project that walks the knowledge graph

---

## Why a separate vocabulary doc

Two different things were tangled in `cross-link.schema.md`:

1. **The edge data structure** — `target`, `relation`, `scale`, `evidence`, `note`. This is the *shape* of an edge.
2. **The relation enum** — what `relation` is allowed to be, what each relation *means*, atlas-pair legality, inverse rules. This is the *vocabulary*.

The vocabulary is the part that grows fastest (every new atlas, every new biological domain, can introduce new relation types). Splitting it out:

- Makes it cheap to add immune-system / vaccine relations without churning the data-structure spec.
- Lets the graph-build step import this single doc to populate the JSON-LD `@context`.
- Gives RO/OBO mappings a clear home.

---

## Relation entry shape

Every relation in this vocabulary is defined by:

| Field | Description |
|:---|:---|
| **Name** | The kebab-case string used in `cross_links[].relation`. |
| **Domain** | The atlas the source entry must belong to. |
| **Range** | The atlas the target entry must belong to. |
| **Inverse** | Reciprocal relation, if one exists. Validator can flag missing back-links. |
| **Symmetric?** | If true, both endpoints must declare the link. |
| **RO / OBO ID** | The Relation Ontology IRI this relation maps to, where one exists. Empty if the relation is project-specific. |
| **Use** | One-line description with a canonical example. |

---

## Atlas prefixes

For brevity in the tables below:

| Prefix | Atlas |
|:---|:---|
| **H** | `01-human` |
| **P** | `02-pathogen` |
| **M** | `03-medicine` |
| **V** | `04-vaccine` *(planned atlas — vaccines may live as a sub-tree of Medicine in the interim)* |

---

## Within Human Atlas (H → H)

| Name | Domain | Range | Inverse | Sym | RO / OBO | Use |
|:---|:---:|:---:|:---|:---:|:---|:---|
| `contains` | H | H | `part-of` |  | `BFO:0000051` (has part) | Heart `contains` myocardium |
| `part-of` | H | H | `contains` or `composed-of` |  | `BFO:0000050` (part of) | Myocardium `part-of` heart |
| `composed-of` | H | H | `part-of` |  | `RO:0002473` (composed primarily of) | Myocardium `composed-of` cardiomyocyte |
| `connects-to` | H | H | self | ✅ | `RO:0002170` (connected to) | Heart `connects-to` lungs |
| `regulates` | H | H | `regulated-by` |  | `RO:0002211` (regulates) | Sympathetic-system `regulates` heart |
| `regulated-by` | H | H | `regulates` |  | `RO:0002334` (regulated by) | Heart-rate `regulated-by` SA-node |
| `secretes` | H | H | `secreted-by` |  | `RO:0002234` (has output, restricted) | Cardiomyocyte `secretes` ANP |
| `secreted-by` | H | H | `secretes` |  | inverse of above | ANP `secreted-by` cardiomyocyte |
| `expresses` | H | H | `expressed-by` |  | `RO:0002292` (expresses) | Cardiomyocyte `expresses` β1-adrenergic-receptor |
| `expressed-by` | H | H | `expresses` |  | `RO:0002206` (expressed in) | β1-adrenergic-receptor `expressed-by` cardiomyocyte |
| `innervated-by` | H | H | (directional, no inverse required) |  | `RO:0002433` (innervated by, proposed) | Heart `innervated-by` autonomic-nervous-system |
| `vascularized-by` | H | H | (directional) |  | (project-specific) | Myocardium `vascularized-by` coronary-arteries |
| `binds` | H | H | `bound-by` |  | `RO:0002436` (molecularly interacts with, restricted) | Spike `binds` ACE2 (when both are H) |
| `bound-by` | H | H | `binds` |  | inverse | ACE2 `bound-by` ANG-II |
| `catalyzes` | H | H | `catalyzed-by` |  | `RO:0002327` (enables) | ACE2 `catalyzes` angiotensin cleavage |

---

## Human ↔ Pathogen (H ↔ P)

### H → P

| Name | Inverse | RO / OBO | Use |
|:---|:---|:---|:---|
| `infected-by` | `infects` | inverse of `RO:0002453` (host of) | Cardiomyocyte `infected-by` coxsackievirus-b |
| `damaged-by` | `damages` | (project-specific) | Heart `damaged-by` coxsackievirus-b |
| `defends-against` | `evaded-by` | (project-specific) | Immune-system `defends-against` SARS-CoV-2 |
| `bound-by` *(cross-atlas variant)* | `binds` | inverse of `RO:0002436` | ACE2 `bound-by` SARS-CoV-2 spike |

### P → H

| Name | Inverse | RO / OBO | Use |
|:---|:---|:---|:---|
| `infects` | `infected-by` | `RO:0002453` (host of, restricted)  | Coxsackievirus-b `infects` cardiomyocyte |
| `damages` | `damaged-by` | (project-specific) | Coxsackievirus-b `damages` heart |
| `evades` | `defends-against` | (project-specific) | Coxsackievirus-b `evades` immune-system |
| `binds` *(cross-atlas variant)* | `bound-by` | `RO:0002436` | SARS-CoV-2 spike `binds` ACE2 |
| `enters-via` | (no inverse required) | (project-specific) | SARS-CoV-2 `enters-via` ACE2 |
| `replicates-in` | (no inverse required) | (project-specific) | SARS-CoV-2 `replicates-in` type-ii-pneumocyte |

---

## Human ↔ Medicine (H ↔ M)

### H → M

| Name | Inverse | RO / OBO | Use |
|:---|:---|:---|:---|
| `target-of` | `targets` | inverse of `RO:0002436` (restricted) | β1-adrenergic-receptor `target-of` metoprolol |
| `modulated-by` | `modulates` | (project-specific) | Heart `modulated-by` metoprolol |

### M → H

| Name | Inverse | RO / OBO | Use |
|:---|:---|:---|:---|
| `targets` | `target-of` | `RO:0002436` (restricted) | Metoprolol `targets` β1-adrenergic-receptor |
| `modulates` | `modulated-by` | (project-specific) | Metoprolol `modulates` heart |
| `agonizes` | (no inverse required) | (project-specific) | Salbutamol `agonizes` β2-adrenergic-receptor |
| `antagonizes` | (no inverse required) | (project-specific) | Metoprolol `antagonizes` β1-adrenergic-receptor |
| `inhibits` | (no inverse required) | `RO:0002408` (directly inhibits) | Atorvastatin `inhibits` HMG-CoA-reductase |
| `activates` | (no inverse required) | `RO:0002406` (directly activates) | Nitroglycerin `activates` guanylate-cyclase |

---

## Pathogen ↔ Medicine (P ↔ M)

### P → M

| Name | Inverse | RO / OBO | Use |
|:---|:---|:---|:---|
| `treated-by` | `treats` | (project-specific) | Coxsackievirus-b `treated-by` ivig |
| `prevented-by` | `prevents` | (project-specific) | SARS-CoV-2 `prevented-by` mrna-1273 |
| `resistant-to` | `ineffective-against` | (project-specific) | MRSA `resistant-to` methicillin |

### M → P

| Name | Inverse | RO / OBO | Use |
|:---|:---|:---|:---|
| `treats` | `treated-by` | `RO:0002606` (is substance that treats) | Acyclovir `treats` herpes-simplex-virus-1 |
| `prevents` | `prevented-by` | (project-specific) | Mrna-1273 `prevents` SARS-CoV-2 |
| `ineffective-against` | `resistant-to` | (project-specific) | Methicillin `ineffective-against` MRSA |

---

## Within atlases (peer relations)

| Name | Atlas | Sym | RO / OBO | Use |
|:---|:---:|:---:|:---|:---|
| `analogue-of` | M → M | ✅ | (project-specific) | Atenolol `analogue-of` metoprolol |
| `combined-with` | M → M | ✅ | (project-specific) | Lisinopril `combined-with` hydrochlorothiazide |
| `mutates-from` | P → P |  | (project-specific) | SARS-CoV-2-omicron `mutates-from` SARS-CoV-2-delta |
| `co-infects-with` | P → P | ✅ | (project-specific) | HIV `co-infects-with` mycobacterium-tuberculosis |
| `subspecies-of` | P → P |  | `BFO:0000050` (part of, restricted) | Influenza-a-h1n1 `subspecies-of` influenza-a |

---

## Immune relations (proposed — needed for vaccine reasoning)

These are new — not in `cross-link.schema.md` today. They are required for the agent to reason about how a vaccine elicits protection. They are mostly **H → H** because the immune system is part of the Human Atlas, but several will cross into Pathogen and Vaccine atlases.

### Antigen presentation & recognition (H → H)

| Name | RO / OBO | Use |
|:---|:---|:---|
| `presents-via-mhc-i` | (project-specific) | Infected-cell `presents-via-mhc-i` viral-peptide |
| `presents-via-mhc-ii` | (project-specific) | Dendritic-cell `presents-via-mhc-ii` viral-peptide |
| `recognized-by-tcr` | (project-specific) | Mhc-i-peptide-complex `recognized-by-tcr` cd8-t-cell |
| `recognized-by-bcr` | (project-specific) | Spike-rbd `recognized-by-bcr` naive-b-cell |
| `produces-antibody` | (project-specific) | Plasma-cell `produces-antibody` igg-anti-spike |
| `clonally-selects` | (project-specific) | Germinal-center `clonally-selects` high-affinity-b-cell |
| `class-switches-to` | (project-specific) | Igm-b-cell `class-switches-to` igg-b-cell |

### Antibody / TCR action (H → P or H → H)

| Name | RO / OBO | Use |
|:---|:---|:---|
| `neutralizes` | (project-specific) | Igg-anti-spike `neutralizes` SARS-CoV-2 (H → P) |
| `opsonizes` | (project-specific) | Igg `opsonizes` bacterium (H → P) |
| `cross-reactive-with` | (project-specific) | Igg-anti-spike `cross-reactive-with` sars-cov-1-spike (H → P, symmetric) |

---

## Vaccine relations (proposed — needed for the Vaccine Atlas)

A new atlas (planned `04-vaccine/` or as a sub-tree under `03-medicine/02-vaccines/`) needs its own relation set bridging to Pathogen, Human (immune system), and other Medicines.

### V → P

| Name | Inverse | Use |
|:---|:---|:---|
| `immunizes-against` | `immunized-by` | Mrna-1273 `immunizes-against` SARS-CoV-2 |
| `targets-antigen-of` | (no inverse) | Mrna-1273 `targets-antigen-of` SARS-CoV-2 |
| `cross-protects-against` | (symmetric) | Mrna-1273 `cross-protects-against` SARS-CoV-2-omicron |

### V → H

| Name | Inverse | Use |
|:---|:---|:---|
| `elicits` | (no inverse) | Mrna-1273 `elicits` neutralizing-antibody-response |
| `induces-memory-in` | (no inverse) | Mrna-1273 `induces-memory-in` cd4-t-cell |
| `delivered-via` | (no inverse) | Mrna-1273 `delivered-via` lipid-nanoparticle |

### V → V

| Name | Inverse | Use |
|:---|:---|:---|
| `same-platform-as` | (symmetric) | Mrna-1273 `same-platform-as` bnt162b2 |
| `boosted-by` | `boosts` | Bnt162b2 `boosted-by` bnt162b2-bivalent |

### V → M

| Name | Inverse | Use |
|:---|:---|:---|
| `contains-adjuvant` | (no inverse) | Nvx-cov2373 `contains-adjuvant` matrix-m |
| `analogue-of` *(reuse)* | (symmetric) | Bnt162b2 `analogue-of` mrna-1273 |

---

## Inverse-link summary

The validator flags missing inverses (warnings, not errors — author can land one side first). Symmetric relations require both endpoints to declare the link.

The full inverse map is defined inline in the tables above; tooling reads the column directly.

---

## Adding a new relation

A new relation enters the vocabulary via:

1. **PR adds a row** to the appropriate table in this file.
2. **Choose an OBO/RO mapping** if one fits — search [OBO Relation Ontology](https://obofoundry.org/ontology/ro.html) and [BFO](https://obofoundry.org/ontology/bfo.html). If none fits, mark as `(project-specific)` and document the gap in the row.
3. **Define inverse** (if any) and symmetry.
4. **Update legal-triple matrix** in `cross-link.schema.md` (or here, if/when that table moves).
5. **Bump validator** to accept the new name.

---

## Versioning

This is `relation-vocabulary/v1`. Adding new relations is **non-breaking** (existing entries keep validating). Removing or renaming relations is **breaking** — bump to `v2` and migrate entries.

---

## Open issues to resolve before adoption

These are flagged for discussion, not yet decided:

1. **Where does `cross_links[].relation` legality live?** Today the source/target/relation triple legality is enforced via tables in `cross-link.schema.md`. Proposal: keep it there (data-structure spec) and reference *into* this vocabulary doc by name.
2. **`binds` in multiple atlas pairs.** `binds` appears as both H→H and P→H today. The simplest model is: the *relation* is the same; only the source/target atlas pair differs. The validator dispatches behavior off the pair, not the relation name. Confirm this is acceptable.
3. **Vaccine atlas placement.** The relations above assume `04-vaccine/`. If vaccines instead live as `03-medicine/02-vaccines/`, the V → ... relations are still well-defined (just with M as their domain) but lose semantic clarity. Worth deciding before adding many vaccine entries.
4. **RO mapping rigor.** Several relations above are marked `(project-specific)` for now. A follow-up sweep with a domain-experienced ontologist (or the OBO community) would tighten these.
5. **Whether `taxonomy` (in current `human-scale-entry`) should be replaced by `xrefs`** (introduced in `entry-frontmatter.schema.md`). They overlap heavily — `taxonomy.uniprot` ≡ `xrefs.uniprot`. Recommend deprecating `taxonomy` in favor of `xrefs`.

---

**[← Back to schemas index](README.md)** · **[Cross-link data structure spec](cross-link.schema.md)** · **[Entry frontmatter spine](entry-frontmatter.schema.md)**
