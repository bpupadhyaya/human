# `media/` — Images, Videos, Diagrams

Shared visual assets referenced by [atlases](../atlases/), [docs](../docs/), and [comp-prog-proj](../comp-prog-proj/). Not for HTML-specific styling assets (those live in `docs/_assets/`).

**[← Back to project README](../README.md)**

---

## What lives here

Visual / multimedia content that documents biology, presents data, or illustrates concepts. **Source-of-truth** atlas content is markdown; media supports and enriches it.

```
media/
├── images/
│   ├── atlas-01-human/         # images supporting Atlas One
│   ├── atlas-02-pathogen/      # images supporting Atlas Two
│   ├── atlas-03-medicine/      # images supporting Atlas Three
│   └── shared/                 # brand marks, cross-atlas figures
├── diagrams/                   # mermaid sources, hand-drawn diagrams, system diagrams
│   ├── architecture/
│   └── biology/
├── videos/                     # short clips, lectures, recorded talks
└── audio/                      # OPTIONAL — podcasts, narrations, lectures
```

Sub-folders are created as needed — do not pre-create empty ones.

---

## Naming conventions

- **Lowercase, kebab-case, no spaces** — `spike-protein-structure.png`, not `Spike Protein Structure.PNG`
- **Descriptive over numeric** — `ace2-spike-binding.png` beats `figure-1.png`
- **Source format alongside derived** — keep editable sources (`.svg`, `.fig`, `.psd`, `.drawio`) and exported `.png`/`.pdf` together when possible

---

## File size & format guidance

| Type | Format preference | Notes |
|:---|:---|:---|
| Vector diagrams | `.svg` (preferred), `.pdf` | Editable, scalable, small |
| Raster images | `.png` for screenshots, `.jpg` for photos, `.webp` for web-optimized | Use lossless when source quality matters |
| Short clips | `.webm` (web), `.mp4` (universal fallback) | Keep under 25 MB inline; larger via git-lfs |
| Long-form video | External hosting (YouTube, Vimeo) | Embed link in atlas markdown; store transcript here |
| Diagram sources | `.mmd` (Mermaid), `.drawio`, `.fig` | Always commit alongside rendered output |

**Files larger than 10 MB** → use `git-lfs` (`git lfs track "*.mp4"`) before committing. Repo bloat is the most expensive long-term cost of a monorepo.

---

## How atlases reference media

From an atlas markdown file:

```markdown
<!-- atlases/02-pathogen/01-viruses/sars-cov-2.md -->

![SARS-CoV-2 spike protein bound to human ACE2](../../../media/images/atlas-02-pathogen/ace2-spike-binding.png)

See the [architecture diagram](../../../media/diagrams/architecture/host-pathogen-flow.svg) for the cross-atlas link path.
```

The path depth depends on where you are in `atlases/`. For deeper sub-folders (e.g., scale-level entries), it's one more `../`.

---

## Licensing

- Original media authored for this project: same license as the repo (MIT, attribution welcome but not required for media).
- **Third-party media** (figures from papers, screenshots, externally-sourced photos): include a `LICENSE.md` in the same folder noting source, author, and license (CC-BY, CC0, public domain, etc.). If a license is restrictive — **don't commit it** — link to the source instead.

---

## What does NOT go here

- HTML page-specific CSS / JS / favicons → `docs/_assets/`
- Logos for `comp-prog-proj/<project>/` projects → keep them inside their own project
- Large raw datasets (genome FASTAs, PDB files, etc.) → `data/`
- Generated outputs from notebooks → notebook output cells, or `data/` if persisted

---

**[← Back to project README](../README.md)**
