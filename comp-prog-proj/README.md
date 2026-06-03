# `comp-prog-proj/` — Computational Programming Projects

**Computational programming projects** that power the Human Engineering knowledge graph: models, classifiers, simulators, services, libraries, AI agents, data pipelines, and anything else that is **machine-executable**.

**[← Back to project README](../README.md)** · **[← Atlases](../atlases/README.md)**

---

## What lives here

One folder per project. Each project is a self-contained, independently buildable, independently testable unit of code. Projects may share data, schemas, and atlas content — but every project owns its own source tree, dependencies, tests, and documentation.

Projects can be in **any language** — Python, Go, Rust, TypeScript, Swift, Julia, C++, etc. Each project carries its own manifest (`pyproject.toml`, `package.json`, `Cargo.toml`, `go.mod`, etc.) and is buildable on its own.

---

## Naming

`kebab-case-noun/` — descriptive, lowercase, hyphen-separated. Examples:

- `pathogen-classifier/`
- `human-cell-graph/`
- `medicine-entry-validator/`
- `vaccine-design-loop/`
- `citation-finder-agent/`

Avoid: PascalCase, snake_case, abbreviations that aren't obvious, vendor/framework names in the folder name.

---

## Standard project skeleton

Every project should follow this minimum structure:

```
comp-prog-proj/
└── <project-name>/
    ├── README.md           # what it does, how to build, how to run, who maintains
    ├── LICENSE             # inherits MIT from root unless explicitly overridden
    ├── src/                # source code
    │   └── <project-name>/ # (Python convention; adapt per language)
    ├── tests/              # unit + integration tests
    ├── agents/             # OPTIONAL — AI agent definitions used by this project
    │   └── <agent-name>/
    │       ├── README.md
    │       ├── prompt.md   # system prompt / agent instructions
    │       └── tools.md    # tool / capability spec
    ├── docs/               # OPTIONAL — project-specific docs (architecture, API)
    ├── examples/           # OPTIONAL — runnable examples / demos
    └── <manifest>          # pyproject.toml | package.json | Cargo.toml | go.mod | …
```

**Required:** `README.md`, `src/`, `tests/`, a build manifest.
**Optional:** everything else, added when needed.

---

## AI agents — where they live

AI agents are **always nested inside a project**, never at the repo root. Two patterns:

### Pattern A — Project-specific agent
The agent is used only by one project. It lives at `comp-prog-proj/<project>/agents/<agent>/`.

```
comp-prog-proj/vaccine-design-loop/
├── README.md
├── src/
├── agents/
│   └── candidate-ranker/
│       ├── README.md
│       ├── prompt.md
│       └── tools.md
└── tests/
```

### Pattern B — Shared agent library
The agent is reused across multiple projects. Make a dedicated project for it, and other projects depend on it.

```
comp-prog-proj/
├── citation-finder-agent/        # the shared agent library project
│   ├── README.md
│   ├── src/
│   ├── prompt.md                 # agent prompt at top of src tree
│   └── tools.md
└── vaccine-design-loop/
    ├── README.md
    └── ... uses citation-finder-agent as a dependency
```

**Rule of thumb:** start with Pattern A. Extract to Pattern B only when ≥2 projects depend on the same agent.

---

## Adding a new project — checklist

1. **Choose a name** in `kebab-case-noun`.
2. `mkdir comp-prog-proj/<name>` and `cd` into it.
3. Initialize the build manifest for your language (`uv init`, `pnpm init`, `cargo init`, `go mod init`, etc.).
4. Create `README.md` at minimum. Describe:
   - **What** the project does (one paragraph)
   - **Which atlases** it consumes or produces content for
   - **How** to build, test, run
   - **Dependencies** on other projects in this repo (if any)
5. Create `src/`, `tests/`, and write your first test.
6. If it uses AI agents, add `agents/<agent-name>/` with `README.md`, `prompt.md`, `tools.md`.
7. Cross-reference: add a row to the project index below (this README).

---

## Cross-references

- **Atlases** (markdown knowledge) — `../atlases/`
- **Schemas** (data contracts your code may consume/produce) — `../schemas/`
- **Data** (datasets your code reads) — `../data/`
- **Notebooks** (research/exploration that may graduate into a project) — `../notebooks/`
- **Tools** (shared dev scripts, not user-facing code) — `../tools/`

---

## When to graduate a project out of this monorepo

Keep a project here while:
- It is closely coupled to atlas content
- It has fewer than ~3 external collaborators
- CI is fast enough

Move it to its own repo when:
- It has its own release cadence and versioning needs
- It accumulates a heavy dependency tree that slows monorepo CI
- An outside team or org wants to own it independently

When extracting: leave a small placeholder folder here with a `README.md` pointing to the new repo.

---

## Workspace tooling

We do **not** use monorepo workspace tooling (pnpm workspaces / cargo workspaces / nx / turborepo / bazel) yet. Each project builds standalone.

Adopt workspace tooling when:
- 3+ projects share dependencies and need synchronized versions, **or**
- CI starts redundantly rebuilding shared code

When that happens: choose the workspace tool that matches the dominant language and migrate. Estimated effort: 1–2 days.

---

## Current projects

*(none yet — populate as projects are created)*

| Project | Language | Status | What it does |
|:---|:---|:---|:---|
| — | — | — | — |

---

**[← Back to project README](../README.md)**
