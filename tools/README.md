# `tools/` — Internal Scripts & Dev Utilities

Shared scripts, build helpers, CI configuration, and dev-time utilities that don't belong to any single project. **Internal-facing only** — none of this is shipped to end users.

**[← Back to project README](../README.md)**

---

## What lives here

```
tools/
├── scripts/             # shell, python, or other scripts callable from repo root
│   ├── new-atlas.sh         # scaffold a new atlas folder
│   ├── new-project.sh       # scaffold a new comp-prog-proj/<name>/ skeleton
│   ├── validate-entries.py  # cross-check atlas entries against schemas
│   └── check-links.sh       # find broken markdown links across the repo
│
├── ci/                  # GitHub Actions workflows live in /.github/workflows/,
│                        # but their helper scripts and configs live here
│
└── git-hooks/           # OPTIONAL — pre-commit hooks (link to via `core.hooksPath`)
```

Sub-folders are added as the need arises — don't pre-create empties.

---

## Distinction from `comp-prog-proj/`

| `tools/` | `comp-prog-proj/` |
|:---|:---|
| Used **by contributors and CI** during development | Used **by the project's purpose** — models, agents, services |
| Not part of the knowledge graph or end-user value | Directly contributes to the mission |
| Short, single-file scripts | Full projects with manifests, tests, and READMEs |
| Examples: lint, validate, scaffold, deploy | Examples: pathogen classifier, vaccine design loop |

If a "tool" grows into something with tests, a manifest, and external users — promote it to `comp-prog-proj/<name>/`.

---

## Conventions

- **Languages:** prefer Bash for thin glue scripts, Python for anything with logic, TypeScript for anything that needs to consume `package.json` workspaces.
- **Self-documenting:** every script begins with a header comment (or `--help` flag) explaining what it does and how to run it.
- **Idempotent:** scripts should be safe to re-run.
- **No external state:** scripts may read the repo, but should not silently write to remote services without confirmation.
- **Discoverable:** every tool listed in this README's "Available tools" table below.

---

## Available tools

*(none yet — populate as tools are added)*

| Tool | What it does | How to invoke |
|:---|:---|:---|
| — | — | — |

---

## What does NOT go here

- Production code → `comp-prog-proj/`
- Documentation → `atlases/`, `docs/`, or project READMEs
- Reusable libraries imported by multiple projects → `comp-prog-proj/<lib-name>/`
- GitHub Actions workflow YAML files → `/.github/workflows/` (root)

---

**[← Back to project README](../README.md)**
