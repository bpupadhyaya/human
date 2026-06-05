#!/usr/bin/env python3
"""
validate-entries.py — validate atlas entries against their schemas.

Walks `atlases/`, parses YAML frontmatter from each `README.md`, validates the
frontmatter against the appropriate JSON Schema, resolves every cross-link
target, and checks body section requirements.

Usage:
    python tools/scripts/validate-entries.py
    python tools/scripts/validate-entries.py --root /path/to/repo
    python tools/scripts/validate-entries.py --strict   # warnings become errors
    python tools/scripts/validate-entries.py --quiet    # only print errors
    python tools/scripts/validate-entries.py --json     # machine-readable report

Exit codes:
    0  clean (or only warnings, in non-strict mode)
    1  one or more validation errors
    2  configuration error (missing schemas, bad invocation)

Dependencies:
    pip install pyyaml jsonschema referencing
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

try:
    import yaml
    from jsonschema import Draft202012Validator
    from referencing import Registry, Resource
    from referencing.jsonschema import DRAFT202012
except ImportError as exc:
    print(
        f"error: missing dependency ({exc.name}). "
        "Install with: pip install pyyaml jsonschema referencing",
        file=sys.stderr,
    )
    sys.exit(2)


# ──────────────────────────────────────────────────────────────────────────────
# Configuration
# ──────────────────────────────────────────────────────────────────────────────

VALID_SCALES = [
    "01-subatomic",
    "02-atomic",
    "03-molecular",
    "04-cellular",
    "05-tissue",
    "06-organ",
    "07-system",
    "08-whole-body",
]

PATHOGEN_VALID_SCALES = [
    "01-viruses",
    "02-bacteria",
    "03-fungi",
    "04-parasites",
    "05-prions",
    "06-environmental",
]

MEDICINE_VALID_SCALES = [
    "01-modern",
    "02-traditional",
    "03-food",
]

VACCINE_VALID_PLATFORMS = [
    "01-mrna",
    "02-viral-vector",
    "03-recombinant-subunit",
    "04-inactivated",
    "05-live-attenuated",
    "06-toxoid",
    "07-vhp",
]

# Required body sections, by scale. "Overview" is the first heading after `# Name`.
SCALE_REQUIRED_SECTIONS: dict[str, list[str]] = {
    "01-subatomic": ["Overview", "Structure", "Function", "Connections"],
    "02-atomic":    ["Overview", "Structure", "Function", "Connections"],
    "03-molecular": ["Overview", "Structure", "Function", "Mechanism", "Connections"],
    "04-cellular":  ["Overview", "Structure", "Function", "Lifecycle", "Connections"],
    "05-tissue":    ["Overview", "Structure", "Function", "Connections"],
    "06-organ":     ["Overview", "Structure", "Function", "Connections", "Pathology"],
    "07-system":    ["Overview", "Structure", "Function", "Connections", "Pathology"],
    "08-whole-body":["Overview", "Structure", "Function", "Connections", "Pathology"],
}

# Cross-link relations whose inverse is required on the other side.
# Maps each relation → set of acceptable inverse relations.
INVERSE_RELATIONS: dict[str, set[str]] = {
    "contains": {"part-of"},
    "composed-of": {"part-of"},
    "part-of": {"contains", "composed-of"},
    "expresses": {"expressed-by"},
    "expressed-by": {"expresses"},
    "infected-by": {"infects"},
    "infects": {"infected-by"},
    "damaged-by": {"damages"},
    "damages": {"damaged-by"},
    "target-of": {"targets"},
    "targets": {"target-of"},
    "modulated-by": {"modulates"},
    "modulates": {"modulated-by"},
    "treated-by": {"treats"},
    "treats": {"treated-by"},
    "prevented-by": {"prevents"},
    "prevents": {"prevented-by"},
}

# Symmetric relations (same name on both sides).
SYMMETRIC_RELATIONS = {"connects-to", "combined-with", "co-infects-with", "analogue-of"}


# ──────────────────────────────────────────────────────────────────────────────
# Reporter
# ──────────────────────────────────────────────────────────────────────────────

@dataclass
class Issue:
    severity: str  # "error" | "warning"
    file: Path
    message: str
    line: int | None = None

    def format(self, root: Path) -> str:
        rel = self.file.relative_to(root) if self.file.is_relative_to(root) else self.file
        loc = f"{rel}:{self.line}" if self.line else str(rel)
        return f"{self.severity}: {loc}: {self.message}"


@dataclass
class Reporter:
    root: Path
    strict: bool = False
    quiet: bool = False
    issues: list[Issue] = field(default_factory=list)
    files_seen: int = 0

    def error(self, file: Path, message: str, line: int | None = None) -> None:
        self.issues.append(Issue("error", file, message, line))

    def warn(self, file: Path, message: str, line: int | None = None) -> None:
        self.issues.append(Issue("warning", file, message, line))

    @property
    def errors(self) -> list[Issue]:
        return [i for i in self.issues if i.severity == "error"]

    @property
    def warnings(self) -> list[Issue]:
        return [i for i in self.issues if i.severity == "warning"]

    def render_text(self) -> str:
        out: list[str] = []
        for issue in self.issues:
            if self.quiet and issue.severity == "warning":
                continue
            out.append(issue.format(self.root))
        out.append(
            f"\n{self.files_seen} entries checked, "
            f"{len(self.errors)} error(s), {len(self.warnings)} warning(s)."
        )
        return "\n".join(out)

    def render_json(self) -> str:
        return json.dumps(
            {
                "files_seen": self.files_seen,
                "errors": [self._issue_dict(i) for i in self.errors],
                "warnings": [self._issue_dict(i) for i in self.warnings],
            },
            indent=2,
        )

    def _issue_dict(self, i: Issue) -> dict[str, Any]:
        return {
            "file": str(i.file.relative_to(self.root))
            if i.file.is_relative_to(self.root)
            else str(i.file),
            "line": i.line,
            "message": i.message,
        }

    def exit_code(self) -> int:
        if self.errors:
            return 1
        if self.strict and self.warnings:
            return 1
        return 0


# ──────────────────────────────────────────────────────────────────────────────
# Schema loading
# ──────────────────────────────────────────────────────────────────────────────

def load_registry(schemas_dir: Path) -> tuple[Registry, dict[str, dict]]:
    """Build a referencing Registry covering every *.schema.json in schemas_dir.

    Returns (registry, {filename: schema_dict}). Filenames (e.g. "citation.schema.json")
    are the URIs used for $ref resolution between sibling schemas.
    """
    registry = Registry()
    schemas: dict[str, dict] = {}
    for path in sorted(schemas_dir.glob("*.schema.json")):
        with path.open() as f:
            schema = json.load(f)
        schemas[path.name] = schema
        resource = Resource.from_contents(schema, default_specification=DRAFT202012)
        registry = registry.with_resource(uri=path.name, resource=resource)
    return registry, schemas


# ──────────────────────────────────────────────────────────────────────────────
# Frontmatter & body parsing
# ──────────────────────────────────────────────────────────────────────────────

FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n(.*)$", re.DOTALL)


def _jsonify(value: Any) -> Any:
    """Recursively coerce YAML-only types (date, datetime) to JSON-compatible
    strings, so jsonschema's `type: string` + `format: date` checks work."""
    if isinstance(value, dt.datetime):
        return value.isoformat()
    if isinstance(value, dt.date):
        return value.isoformat()
    if isinstance(value, dict):
        return {k: _jsonify(v) for k, v in value.items()}
    if isinstance(value, list):
        return [_jsonify(v) for v in value]
    return value


def parse_entry(text: str) -> tuple[dict | None, str, int]:
    """Parse YAML frontmatter and return (frontmatter, body, body_start_line).

    Returns (None, text, 1) if no frontmatter is present.
    """
    m = FRONTMATTER_RE.match(text)
    if not m:
        return None, text, 1
    frontmatter_text, body = m.group(1), m.group(2)
    try:
        frontmatter = yaml.safe_load(frontmatter_text)
    except yaml.YAMLError as exc:
        raise ValueError(f"YAML parse error in frontmatter: {exc}")
    if not isinstance(frontmatter, dict):
        raise ValueError("frontmatter must be a YAML mapping")
    frontmatter = _jsonify(frontmatter)
    body_start_line = frontmatter_text.count("\n") + 4  # 1 (open ---) + N + 1 (close ---) + 1
    return frontmatter, body, body_start_line


HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$", re.MULTILINE)
INLINE_CITATION_RE = re.compile(r"\[\^([a-z0-9][a-z0-9-]*)\]")


def extract_headings(body: str, body_start_line: int) -> list[tuple[int, int, str]]:
    """Return list of (level, line_number, text) for every markdown heading."""
    out = []
    for m in HEADING_RE.finditer(body):
        level = len(m.group(1))
        text = m.group(2).strip()
        # Compute 1-indexed line number relative to file start.
        line = body_start_line + body[: m.start()].count("\n")
        out.append((level, line, text))
    return out


# ──────────────────────────────────────────────────────────────────────────────
# Entry discovery
# ──────────────────────────────────────────────────────────────────────────────

ATLAS_DIRS = ("01-human", "02-pathogen", "03-medicine", "04-vaccine")


def discover_entries(atlases_dir: Path) -> list[Path]:
    """Find every README.md under atlases/<atlas>/.../ that has YAML frontmatter.

    Skips top-level atlas READMEs and scale-level READMEs (those are indices, not entries).
    An entry is recognised by having a `schema:` key in its frontmatter.
    """
    entries: list[Path] = []
    if not atlases_dir.exists():
        return entries
    for atlas in ATLAS_DIRS:
        atlas_root = atlases_dir / atlas
        if not atlas_root.exists():
            continue
        for readme in atlas_root.rglob("README.md"):
            # Cheap filter: peek for `schema:` in the first 20 lines.
            try:
                with readme.open() as f:
                    head = "".join(f.readline() for _ in range(20))
            except OSError:
                continue
            if "schema:" in head and "---" in head:
                entries.append(readme)
    return entries


# ──────────────────────────────────────────────────────────────────────────────
# Validation
# ──────────────────────────────────────────────────────────────────────────────

def validate_entry(
    path: Path,
    root: Path,
    registry: Registry,
    schemas: dict[str, dict],
    reporter: Reporter,
) -> dict | None:
    """Validate a single entry. Returns parsed frontmatter (or None on hard failure)."""
    try:
        text = path.read_text(encoding="utf-8")
    except OSError as exc:
        reporter.error(path, f"cannot read file: {exc}")
        return None

    try:
        frontmatter, body, body_start_line = parse_entry(text)
    except ValueError as exc:
        reporter.error(path, str(exc), line=1)
        return None

    if frontmatter is None:
        reporter.error(path, "no YAML frontmatter found", line=1)
        return None

    schema_id = frontmatter.get("schema")
    if not schema_id:
        reporter.error(path, "frontmatter missing required field: schema", line=1)
        return None

    # Dispatch to per-schema validators.
    if schema_id == "human-scale-entry/v1":
        validate_human_entry(path, root, frontmatter, body, body_start_line, registry, schemas, reporter)
    elif schema_id == "pathogen-entry/v1":
        validate_pathogen_entry(path, root, frontmatter, body, body_start_line, registry, schemas, reporter)
    elif schema_id == "medicine-entry/v1":
        validate_medicine_entry(path, root, frontmatter, body, body_start_line, registry, schemas, reporter)
    elif schema_id == "vaccine-entry/v1":
        validate_vaccine_entry(path, root, frontmatter, body, body_start_line, registry, schemas, reporter)
    else:
        reporter.error(path, f"unknown schema: {schema_id}", line=1)

    return frontmatter


def validate_human_entry(
    path: Path,
    root: Path,
    frontmatter: dict,
    body: str,
    body_start_line: int,
    registry: Registry,
    schemas: dict[str, dict],
    reporter: Reporter,
) -> None:
    schema = schemas.get("human-scale-entry.schema.json")
    if not schema:
        reporter.error(path, "human-scale-entry.schema.json not found in schemas/", line=1)
        return

    validator = Draft202012Validator(schema, registry=registry)
    schema_errors = sorted(validator.iter_errors(frontmatter), key=lambda e: list(e.absolute_path))
    for err in schema_errors:
        loc = "/".join(str(p) for p in err.absolute_path) or "<root>"
        reporter.error(path, f"frontmatter schema error at {loc}: {err.message}", line=1)

    # Stop if the basic shape is wrong.
    if schema_errors:
        return

    # Folder-name == id check.
    folder = path.parent.name
    if frontmatter["id"] != folder:
        reporter.error(
            path,
            f"id '{frontmatter['id']}' does not match folder name '{folder}'",
            line=1,
        )

    # Scale matches parent folder name.
    scale_folder = path.parent.parent.name
    if scale_folder in VALID_SCALES and frontmatter["scale"] != scale_folder:
        reporter.error(
            path,
            f"scale '{frontmatter['scale']}' does not match parent folder '{scale_folder}'",
            line=1,
        )

    # Body sections.
    headings = extract_headings(body, body_start_line)
    h1s = [h for h in headings if h[0] == 1]
    if not h1s:
        reporter.error(path, "body missing top-level `# <Name>` heading", line=body_start_line)
    else:
        level, line, text = h1s[0]
        if text != frontmatter["name"]:
            reporter.error(
                path,
                f"H1 heading '{text}' does not match frontmatter name '{frontmatter['name']}'",
                line=line,
            )

    section_titles = {h[2] for h in headings if h[0] == 2}
    required = SCALE_REQUIRED_SECTIONS.get(frontmatter["scale"], [])
    for required_section in required:
        if required_section not in section_titles:
            reporter.error(
                path,
                f"missing required body section: ## {required_section}",
                line=body_start_line,
            )

    # URL/linkability check: every source should have at least one of url, doi, pmid.
    for src in frontmatter.get("sources", []):
        has_link = bool(src.get("url") or src.get("doi") or src.get("pmid"))
        if not has_link:
            reporter.warn(
                path,
                f"sources[id={src.get('id', '?')}] has no url, doi, or pmid — citation is not linkable",
                line=1,
            )

    # Inline citation references resolve.
    source_ids = {s["id"] for s in frontmatter.get("sources", [])}
    for m in INLINE_CITATION_RE.finditer(body):
        cite_id = m.group(1)
        if cite_id not in source_ids:
            line = body_start_line + body[: m.start()].count("\n")
            reporter.warn(
                path,
                f"inline citation [^{cite_id}] does not match any sources[].id",
                line=line,
            )

    # Cross-link evidence references.
    for i, link in enumerate(frontmatter.get("cross_links", []) or []):
        evidence = link.get("evidence")
        if evidence and evidence not in source_ids:
            reporter.error(
                path,
                f"cross_links[{i}].evidence='{evidence}' does not match any sources[].id",
                line=1,
            )


def _validate_common_fields(
    path: Path,
    frontmatter: dict,
    body: str,
    body_start_line: int,
    reporter: Reporter,
    required_sections: list[str],
    expected_atlas: str,
    valid_scales: list[str],
) -> None:
    """Shared validation logic for pathogen and medicine entries."""
    # Required top-level fields.
    required_fields = ["schema", "id", "name", "atlas", "scale", "status",
                       "last_reviewed", "summary", "sources", "cross_links"]
    for fld in required_fields:
        if fld not in frontmatter or frontmatter[fld] is None:
            reporter.error(path, f"frontmatter missing required field: {fld}", line=1)

    # id matches folder name.
    folder = path.parent.name
    entry_id = frontmatter.get("id", "")
    if entry_id and entry_id != folder:
        reporter.error(
            path,
            f"id '{entry_id}' does not match folder name '{folder}'",
            line=1,
        )

    # atlas check.
    atlas = frontmatter.get("atlas", "")
    if atlas and atlas != expected_atlas:
        reporter.error(
            path,
            f"atlas '{atlas}' is not '{expected_atlas}' for this schema",
            line=1,
        )

    # scale check.
    scale = frontmatter.get("scale", "")
    if scale and scale not in valid_scales:
        reporter.error(
            path,
            f"scale '{scale}' is not valid; expected one of {valid_scales}",
            line=1,
        )

    # Scale matches parent folder.
    scale_folder = path.parent.parent.name
    if scale and scale_folder in valid_scales and scale != scale_folder:
        reporter.error(
            path,
            f"scale '{scale}' does not match parent folder '{scale_folder}'",
            line=1,
        )

    # summary length.
    summary = frontmatter.get("summary", "")
    if summary and len(summary) > 280:
        reporter.error(
            path,
            f"summary is {len(summary)} characters; must be ≤280",
            line=1,
        )

    # Source linkability.
    for src in frontmatter.get("sources", []) or []:
        has_link = bool(src.get("url") or src.get("doi") or src.get("pmid"))
        if not has_link:
            reporter.warn(
                path,
                f"sources[id={src.get('id', '?')}] has no url, doi, or pmid — citation is not linkable",
                line=1,
            )

    # Body sections.
    headings = extract_headings(body, body_start_line)
    h1s = [h for h in headings if h[0] == 1]
    if not h1s:
        reporter.error(path, "body missing top-level `# <Name>` heading", line=body_start_line)
    else:
        level, line, text = h1s[0]
        name = frontmatter.get("name", "")
        if name and text != name:
            reporter.error(
                path,
                f"H1 heading '{text}' does not match frontmatter name '{name}'",
                line=line,
            )

    section_titles = {h[2] for h in headings if h[0] == 2}
    for required_section in required_sections:
        if required_section not in section_titles:
            reporter.error(
                path,
                f"missing required body section: ## {required_section}",
                line=body_start_line,
            )

    # Inline citation references resolve.
    source_ids = {s["id"] for s in frontmatter.get("sources", []) or []}
    for m in INLINE_CITATION_RE.finditer(body):
        cite_id = m.group(1)
        if cite_id not in source_ids:
            line = body_start_line + body[: m.start()].count("\n")
            reporter.warn(
                path,
                f"inline citation [^{cite_id}] does not match any sources[].id",
                line=line,
            )

    # Cross-link evidence references.
    for i, link in enumerate(frontmatter.get("cross_links", []) or []):
        evidence = link.get("evidence")
        if evidence and evidence not in source_ids:
            reporter.error(
                path,
                f"cross_links[{i}].evidence='{evidence}' does not match any sources[].id",
                line=1,
            )


PATHOGEN_REQUIRED_SECTIONS = [
    "Overview", "Structure", "Infection Mechanism", "Host Interactions", "Connections", "Pathology"
]

MEDICINE_REQUIRED_SECTIONS = [
    "Overview", "Mechanism", "Clinical Use", "Evidence", "Connections"
]

VACCINE_REQUIRED_SECTIONS = [
    "Overview", "Immunogenicity", "Safety", "Connections"
]


def validate_pathogen_entry(
    path: Path,
    root: Path,
    frontmatter: dict,
    body: str,
    body_start_line: int,
    registry: Registry,
    schemas: dict[str, dict],
    reporter: Reporter,
) -> None:
    _validate_common_fields(
        path, frontmatter, body, body_start_line, reporter,
        required_sections=PATHOGEN_REQUIRED_SECTIONS,
        expected_atlas="02-pathogen",
        valid_scales=PATHOGEN_VALID_SCALES,
    )


def validate_medicine_entry(
    path: Path,
    root: Path,
    frontmatter: dict,
    body: str,
    body_start_line: int,
    registry: Registry,
    schemas: dict[str, dict],
    reporter: Reporter,
) -> None:
    _validate_common_fields(
        path, frontmatter, body, body_start_line, reporter,
        required_sections=MEDICINE_REQUIRED_SECTIONS,
        expected_atlas="03-medicine",
        valid_scales=MEDICINE_VALID_SCALES,
    )


def validate_vaccine_entry(
    path: Path,
    root: Path,
    frontmatter: dict,
    body: str,
    body_start_line: int,
    registry: Registry,
    schemas: dict[str, dict],
    reporter: Reporter,
) -> None:
    required_fields = ["schema", "id", "name", "atlas", "platform", "status",
                       "last_reviewed", "summary", "sources", "cross_links"]
    for fld in required_fields:
        if fld not in frontmatter or frontmatter[fld] is None:
            reporter.error(path, f"frontmatter missing required field: {fld}", line=1)

    folder = path.parent.name
    entry_id = frontmatter.get("id", "")
    if entry_id and entry_id != folder:
        reporter.error(path, f"id '{entry_id}' does not match folder name '{folder}'", line=1)

    atlas = frontmatter.get("atlas", "")
    if atlas and atlas != "04-vaccine":
        reporter.error(path, f"atlas '{atlas}' is not '04-vaccine' for this schema", line=1)

    platform = frontmatter.get("platform", "")
    if platform and platform not in VACCINE_VALID_PLATFORMS:
        reporter.error(
            path,
            f"platform '{platform}' is not valid; expected one of {VACCINE_VALID_PLATFORMS}",
            line=1,
        )

    platform_folder = path.parent.parent.name
    if platform and platform_folder in VACCINE_VALID_PLATFORMS and platform != platform_folder:
        reporter.error(
            path,
            f"platform '{platform}' does not match parent folder '{platform_folder}'",
            line=1,
        )

    summary = frontmatter.get("summary", "")
    if summary and len(summary) > 280:
        reporter.error(path, f"summary is {len(summary)} characters; must be ≤280", line=1)

    for src in frontmatter.get("sources", []) or []:
        has_link = bool(src.get("url") or src.get("doi") or src.get("pmid"))
        if not has_link:
            reporter.warn(
                path,
                f"sources[id={src.get('id', '?')}] has no url, doi, or pmid — citation is not linkable",
                line=1,
            )

    headings = extract_headings(body, body_start_line)
    h1s = [h for h in headings if h[0] == 1]
    if not h1s:
        reporter.error(path, "body missing top-level `# <Name>` heading", line=body_start_line)
    else:
        _, line_no, text = h1s[0]
        name = frontmatter.get("name", "")
        if name and text != name:
            reporter.error(
                path,
                f"H1 heading '{text}' does not match frontmatter name '{name}'",
                line=line_no,
            )

    section_titles = {h[2] for h in headings if h[0] == 2}
    for required_section in VACCINE_REQUIRED_SECTIONS:
        if required_section not in section_titles:
            reporter.error(
                path,
                f"missing required body section: ## {required_section}",
                line=body_start_line,
            )

    source_ids = {s["id"] for s in frontmatter.get("sources", []) or []}
    for m in INLINE_CITATION_RE.finditer(body):
        cite_id = m.group(1)
        if cite_id not in source_ids:
            line = body_start_line + body[: m.start()].count("\n")
            reporter.warn(
                path,
                f"inline citation [^{cite_id}] does not match any sources[].id",
                line=line,
            )

    for i, link in enumerate(frontmatter.get("cross_links", []) or []):
        evidence = link.get("evidence")
        if evidence and evidence not in source_ids:
            reporter.error(
                path,
                f"cross_links[{i}].evidence='{evidence}' does not match any sources[].id",
                line=1,
            )


def resolve_cross_links(
    entries_with_frontmatter: list[tuple[Path, dict]],
    root: Path,
    reporter: Reporter,
) -> None:
    """Check every cross-link target resolves to an existing entry, and that
    inverse-relation back-links are present (warning only)."""
    atlases_dir = root / "atlases"
    # Index: target-path-string → frontmatter
    by_target: dict[str, dict] = {}
    for path, fm in entries_with_frontmatter:
        try:
            rel = path.parent.relative_to(atlases_dir)
        except ValueError:
            continue
        by_target[str(rel).replace("\\", "/")] = fm

    for path, fm in entries_with_frontmatter:
        for i, link in enumerate(fm.get("cross_links", []) or []):
            target = link.get("target")
            relation = link.get("relation")
            if not target:
                continue
            target_readme = atlases_dir / target / "README.md"
            if not target_readme.exists():
                reporter.error(
                    path,
                    f"cross_links[{i}].target '{target}' does not resolve to an existing entry "
                    f"(expected file: atlases/{target}/README.md)",
                    line=1,
                )
                continue

            target_fm = by_target.get(target)
            if target_fm is None:
                continue  # Target exists but had no parsed frontmatter; already reported elsewhere.

            # Inverse-link check.
            expected_inverses = INVERSE_RELATIONS.get(relation, set()) if relation else set()
            self_target = (
                str(path.parent.relative_to(atlases_dir)).replace("\\", "/")
            )
            if expected_inverses:
                target_links = target_fm.get("cross_links") or []
                has_inverse = any(
                    l.get("target") == self_target and l.get("relation") in expected_inverses
                    for l in target_links
                )
                if not has_inverse:
                    inverse_str = " or ".join(sorted(f"'{r}'" for r in expected_inverses))
                    reporter.warn(
                        path,
                        f"cross_links[{i}] '{relation} → {target}' has no inverse "
                        f"({inverse_str}) back-link in target",
                        line=1,
                    )
            elif relation in SYMMETRIC_RELATIONS:
                target_links = target_fm.get("cross_links") or []
                has_back = any(
                    l.get("target") == self_target and l.get("relation") == relation
                    for l in target_links
                )
                if not has_back:
                    reporter.warn(
                        path,
                        f"symmetric cross_links[{i}] '{relation} → {target}' missing matching "
                        f"back-link in target",
                        line=1,
                    )


# ──────────────────────────────────────────────────────────────────────────────
# CLI
# ──────────────────────────────────────────────────────────────────────────────

def find_repo_root(start: Path) -> Path:
    """Find the repo root by walking up looking for the schemas/ + atlases/ pair."""
    for candidate in [start, *start.parents]:
        if (candidate / "schemas").is_dir() and (candidate / "atlases").is_dir():
            return candidate
    return start


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--root", type=Path, default=None, help="Repo root (default: auto-detect).")
    parser.add_argument("--strict", action="store_true", help="Treat warnings as errors.")
    parser.add_argument("--quiet", action="store_true", help="Suppress warnings in output.")
    parser.add_argument("--json", action="store_true", help="Emit a machine-readable JSON report.")
    args = parser.parse_args(argv)

    root = args.root or find_repo_root(Path(__file__).resolve().parent)
    schemas_dir = root / "schemas"
    atlases_dir = root / "atlases"

    if not schemas_dir.is_dir():
        print(f"error: schemas/ not found at {schemas_dir}", file=sys.stderr)
        return 2
    if not atlases_dir.is_dir():
        print(f"error: atlases/ not found at {atlases_dir}", file=sys.stderr)
        return 2

    registry, schemas = load_registry(schemas_dir)
    if "human-scale-entry.schema.json" not in schemas:
        print(
            "error: schemas/human-scale-entry.schema.json missing — cannot validate Human Atlas entries.",
            file=sys.stderr,
        )
        return 2

    reporter = Reporter(root=root, strict=args.strict, quiet=args.quiet)
    entries = discover_entries(atlases_dir)
    reporter.files_seen = len(entries)

    parsed: list[tuple[Path, dict]] = []
    for path in entries:
        fm = validate_entry(path, root, registry, schemas, reporter)
        if fm:
            parsed.append((path, fm))

    resolve_cross_links(parsed, root, reporter)

    if args.json:
        print(reporter.render_json())
    else:
        print(reporter.render_text())

    return reporter.exit_code()


if __name__ == "__main__":
    sys.exit(main())
