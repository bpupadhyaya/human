#!/usr/bin/env python3
"""
generate-pages.py — Static page generator for the Human Engineering atlas.

For every atlas entry (README.md with YAML frontmatter containing an `id:` field)
that does not already have a hand-crafted docs/{id}.html, generates a styled stub
HTML page using the frontmatter data.

Usage:
    python3 tools/scripts/generate-pages.py [--dry-run]
"""

import argparse
import os
import sys
import yaml

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ATLASES_DIR = os.path.join(REPO_ROOT, "atlases")
DOCS_DIR = os.path.join(REPO_ROOT, "docs")

# ── Schema → visual config ────────────────────────────────────────────────────

SCHEMA_CONFIG = {
    "human-scale-entry": {
        "atlas_label": "Atlas One",
        "atlas_sub": "Host Biology",
        "grad_from": "#059669",
        "grad_to": "#064e3b",
        "accent": "#059669",
        "scale_names": {
            "01-subatomic": "Scale 01 — Subatomic",
            "02-atomic": "Scale 02 — Atomic",
            "03-molecular": "Scale 03 — Molecular",
            "04-cellular": "Scale 04 — Cellular",
            "05-tissue": "Scale 05 — Tissue",
            "06-organ": "Scale 06 — Organ",
            "07-system": "Scale 07 — System",
            "08-whole-body": "Scale 08 — Whole Body",
        },
    },
    "pathogen-entry": {
        "atlas_label": "Atlas Two",
        "atlas_sub": "Pathogen Atlas",
        "grad_from": "#dc2626",
        "grad_to": "#7f1d1d",
        "accent": "#dc2626",
    },
    "medicine-entry": {
        "atlas_label": "Atlas Three",
        "atlas_sub": "Medicine Atlas",
        "grad_from": "#7c3aed",
        "grad_to": "#4c1d95",
        "accent": "#7c3aed",
    },
    "vaccine-entry": {
        "atlas_label": "Atlas Four",
        "atlas_sub": "Vaccine Atlas",
        "grad_from": "#0891b2",
        "grad_to": "#164e63",
        "accent": "#0891b2",
        "platform_names": {
            "01-mrna": "01 — mRNA",
            "02-viral-vector": "02 — Viral Vector",
            "03-recombinant-subunit": "03 — Recombinant Subunit",
            "04-inactivated": "04 — Inactivated",
            "05-live-attenuated": "05 — Live-Attenuated",
            "06-toxoid": "06 — Toxoid",
            "07-vhp": "07 — VHP",
        },
    },
}

RELATION_CLASSES = {
    "part-of": "part",
    "contains": "part",
    "composed-of": "part",
    "damages": "damaged",
    "damaged-by": "damaged",
}

CSS = """    :root {
      --bg: #f2f2f7; --bg-elev: #ffffff; --bg-soft: #e5e5ea;
      --fg: #1c1c1e; --fg-soft: #3a3a3c; --muted: #6e6e73; --muted-2: #8e8e93;
      --border: #d1d1d6; --border-soft: #e5e5ea;
      --bio: #059669; --eng: #2563eb; --ai: #7c3aed; --human: #d97706;
      --accent: #0284c7;
      --radius-sm: 10px; --radius: 18px; --radius-lg: 24px; --maxw: 1120px;
    }
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    html { scroll-behavior: smooth; }
    body { font-family: -apple-system, BlinkMacSystemFont, "Inter", "Segoe UI", Roboto, sans-serif;
           background: var(--bg); color: var(--fg); line-height: 1.65; -webkit-font-smoothing: antialiased; }
    a { color: var(--bio); text-decoration: none; transition: color .15s; }
    a:hover { color: var(--human); }
    nav { position: sticky; top: 0; z-index: 50; backdrop-filter: saturate(180%) blur(20px);
          -webkit-backdrop-filter: saturate(180%) blur(20px);
          background: rgba(242,242,247,0.85); border-bottom: 1px solid var(--border-soft); }
    .nav-inner { max-width: var(--maxw); margin: 0 auto; padding: 0.85rem 1.5rem;
                 display: flex; align-items: center; justify-content: space-between; gap: 1rem; }
    .brand { display: flex; align-items: center; gap: 0.6rem; font-weight: 700;
             font-size: 0.98rem; letter-spacing: -0.01em; color: var(--fg); }
    .brand-mark { width: 26px; height: 26px; border-radius: 7px;
                  background: conic-gradient(from 140deg, var(--bio), var(--eng), var(--ai), var(--human), var(--bio));
                  box-shadow: 0 0 0 1px rgba(0,0,0,0.08), 0 4px 16px rgba(5,150,105,0.2); }
    .nav-links { display: flex; align-items: center; gap: 1.3rem; font-size: 0.92rem; }
    .nav-links a { color: var(--muted); font-weight: 500; }
    .nav-links a:hover { color: var(--fg); }
    .nav-back { display: inline-flex; align-items: center; gap: 0.4rem; color: var(--muted); }
    .nav-back svg { width: 14px; height: 14px; }
    @media (max-width: 760px) { .nav-links a:not(.nav-back) { display: none; } }
    .hero { max-width: var(--maxw); margin: 0 auto; padding: 4rem 1.5rem 2.5rem; }
    .hero-eyebrow { display: inline-flex; align-items: center; padding: 0.4rem 0.9rem;
                    border-radius: 999px; font-size: 0.75rem; font-weight: 700;
                    letter-spacing: 0.1em; text-transform: uppercase; margin-bottom: 1.5rem; }
    .hero h1 { font-size: clamp(2.2rem, 5vw, 3.8rem); font-weight: 800; letter-spacing: -0.03em;
               color: var(--fg); line-height: 1.06; margin-bottom: 1.1rem; }
    .hero .tagline { font-size: clamp(1.05rem, 1.6vw, 1.25rem); color: var(--fg-soft);
                     max-width: 700px; font-weight: 500; margin-bottom: 0.75rem; }
    .hero .aliases { font-size: 0.9rem; color: var(--muted); margin-top: 0.4rem; }
    .stat-row { display: flex; gap: 2.5rem; flex-wrap: wrap; margin-top: 2rem;
                padding-top: 1.5rem; border-top: 1px solid var(--border-soft); }
    .stat { display: flex; flex-direction: column; }
    .stat-num { font-size: 1.5rem; font-weight: 800; color: var(--fg); letter-spacing: -0.02em; line-height: 1; }
    .stat-label { font-size: 0.8rem; color: var(--muted); margin-top: 0.3rem;
                  letter-spacing: 0.04em; text-transform: uppercase; font-weight: 600; }
    main { max-width: var(--maxw); margin: 0 auto; padding: 0 1.5rem 2rem; }
    .stub-notice { background: rgba(251,191,36,0.1); border: 1px solid rgba(251,191,36,0.35);
                   border-radius: var(--radius-sm); padding: 0.75rem 1rem; font-size: 0.88rem;
                   color: #92400e; margin-bottom: 1.5rem; }
    .detail-card { background: var(--bg-elev); border: 1px solid var(--border-soft);
                   border-radius: var(--radius-lg); overflow: hidden; margin-bottom: 1.5rem;
                   box-shadow: 0 4px 14px rgba(0,0,0,0.04); }
    .detail-header { padding: 2rem 2rem 1.75rem; }
    .detail-header .entry-eyebrow { font-size: 0.72rem; font-weight: 700; letter-spacing: 0.12em;
                                    text-transform: uppercase; color: rgba(255,255,255,0.7); margin-bottom: 0.5rem; }
    .detail-header h2 { font-size: clamp(1.8rem, 3vw, 2.5rem); font-weight: 800; color: white;
                        letter-spacing: -0.03em; margin-bottom: 0.65rem; }
    .detail-header .summary { font-size: 0.98rem; color: rgba(255,255,255,0.88); line-height: 1.65; max-width: 780px; }
    .detail-body { padding: 2rem; display: flex; flex-direction: column; gap: 2rem; }
    .detail-section h3 { font-size: 0.76rem; font-weight: 700; letter-spacing: 0.1em;
                         text-transform: uppercase; color: var(--muted); margin-bottom: 0.8rem;
                         padding-bottom: 0.4rem; border-bottom: 1px solid var(--border-soft); }
    .data-table { width: 100%; border-collapse: collapse; font-size: 0.87rem; margin-top: 0.5rem; }
    .data-table th { text-align: left; padding: 0.5rem 0.65rem; background: var(--bg);
                     font-weight: 600; font-size: 0.74rem; text-transform: uppercase;
                     letter-spacing: 0.06em; color: var(--muted); }
    .data-table td { padding: 0.5rem 0.65rem; border-top: 1px solid var(--border-soft);
                     color: var(--fg-soft); vertical-align: top; line-height: 1.5; }
    .data-table td:first-child { font-weight: 600; color: var(--fg); white-space: nowrap; }
    .connections { display: flex; flex-wrap: wrap; gap: 0.6rem; }
    .conn-pill { display: inline-flex; align-items: center; gap: 0.4rem; padding: 0.4rem 0.85rem;
                 background: var(--bg); border: 1px solid var(--border); border-radius: 999px;
                 font-size: 0.82rem; color: var(--fg-soft); transition: all .15s; }
    .conn-pill:hover { background: var(--bg-soft); color: var(--fg); }
    .conn-pill .rel { font-weight: 700; font-size: 0.72rem; text-transform: uppercase;
                      letter-spacing: 0.05em; color: var(--bio); margin-right: 0.1rem; }
    .conn-pill.damaged .rel { color: #dc2626; }
    .conn-pill.part .rel { color: var(--ai); }
    .refs { list-style: none; display: flex; flex-direction: column; gap: 0.5rem; }
    .refs li { font-size: 0.82rem; color: var(--muted); line-height: 1.55; padding-left: 1.1rem; position: relative; }
    .refs li::before { content: '↗'; position: absolute; left: 0; color: var(--eng); font-size: 0.75rem; top: 0.05rem; }
    .refs li a { color: var(--eng); }
    footer { margin-top: 4rem; padding: 2.5rem 1.5rem 2rem; border-top: 1px solid var(--border-soft); text-align: center; }
    .footer-tag { font-size: 0.95rem; color: var(--muted); max-width: 620px; margin: 0 auto 1rem; }
    .footer-links { display: flex; gap: 1.25rem; justify-content: center; flex-wrap: wrap; font-size: 0.88rem; margin-bottom: 1rem; }
    .footer-links a { color: var(--muted); }
    .footer-links a:hover { color: var(--bio); }
    .footer-meta { font-size: 0.8rem; color: var(--muted-2); }"""


def parse_frontmatter(path):
    with open(path, encoding="utf-8") as f:
        text = f.read()
    if not text.startswith("---"):
        return None
    end = text.find("\n---", 3)
    if end == -1:
        return None
    try:
        return yaml.safe_load(text[3:end])
    except yaml.YAMLError:
        return None


def find_cfg(schema):
    for key, val in SCHEMA_CONFIG.items():
        if schema.startswith(key):
            return val
    return None


def esc(s):
    if s is None:
        return ""
    return (str(s).replace("&", "&amp;").replace("<", "&lt;")
            .replace(">", "&gt;").replace('"', "&quot;"))


def hex_to_rgb(h):
    h = h.lstrip("#")
    r, g, b = int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)
    return f"{r},{g},{b}"


def mk_stat(num, label):
    return (f'<div class="stat">'
            f'<span class="stat-num">{esc(num)}</span>'
            f'<span class="stat-label">{esc(label)}</span>'
            f'</div>')


def mk_row(label, value):
    if value is None or value == "" or value == [] or value == {}:
        return ""
    if isinstance(value, list):
        value = "; ".join(str(v) for v in value)
    return f"<tr><td>{esc(label)}</td><td>{esc(value)}</td></tr>"


def mk_source(src):
    cite = src.get("cite", "")
    doi = src.get("doi")
    pmid = src.get("pmid")
    url = src.get("url")
    link = (doi and f"https://doi.org/{doi}") or url
    text = f'<a href="{esc(link)}" target="_blank" rel="noopener noreferrer">{esc(cite)}</a>' if link else esc(cite)
    pmid_link = (f' &middot; <a href="https://pubmed.ncbi.nlm.nih.gov/{esc(pmid)}/"'
                 f' target="_blank" rel="noopener noreferrer">PubMed {esc(pmid)}</a>') if pmid else ""
    return f"<li>{text}{pmid_link}</li>"


def mk_pill(cl):
    target = cl.get("target", "")
    relation = cl.get("relation", "")
    note = cl.get("note", "")
    target_id = target.split("/")[-1] if "/" in target else target
    label = target_id.replace("-", " ").title()
    rel_class = RELATION_CLASSES.get(relation, "")
    cls = f'conn-pill {rel_class}'.strip() if rel_class else "conn-pill"
    title = f' title="{esc(note)}"' if note else ""
    return (f'<a class="{cls}" href="{esc(target_id)}.html"{title}>'
            f'<span class="rel">{esc(relation)}</span>{esc(label)}</a>')


def build_stats(fm, cfg, schema):
    rows = []
    if "human-scale-entry" in schema:
        scale = fm.get("scale", "—")
        scale_label = cfg.get("scale_names", {}).get(scale, scale)
        rows = [mk_stat(scale_label, "Scale"),
                mk_stat(fm.get("status", "—"), "Status"),
                mk_stat(fm.get("last_reviewed", "—"), "Last Reviewed")]
    elif "pathogen-entry" in schema:
        rows = [mk_stat(fm.get("scale", "—"), "Class"),
                mk_stat(fm.get("status", "—"), "Status"),
                mk_stat(fm.get("last_reviewed", "—"), "Last Reviewed")]
    elif "medicine-entry" in schema:
        roa = fm.get("route_of_administration", "—")
        if isinstance(roa, list):
            roa = ", ".join(roa)
        rows = [mk_stat(fm.get("scale", fm.get("stream", "—")), "Stream"),
                mk_stat(roa, "Route"),
                mk_stat(fm.get("status", "—"), "Status"),
                mk_stat(fm.get("last_reviewed", "—"), "Last Reviewed")]
    elif "vaccine-entry" in schema:
        platform = fm.get("platform", "—")
        pname = cfg.get("platform_names", {}).get(platform, platform)
        rows = [mk_stat(pname, "Platform"),
                mk_stat(fm.get("route_of_administration", "—"), "Route"),
                mk_stat(fm.get("cold_chain", "—"), "Cold Chain"),
                mk_stat(fm.get("status", "—"), "Status")]
    return "\n        ".join(rows)


def build_meta_table(fm, schema):
    rows = [mk_row("ID", fm.get("id")),
            mk_row("Name", fm.get("name")),
            mk_row("Status", fm.get("status")),
            mk_row("Last reviewed", fm.get("last_reviewed"))]

    if "human-scale-entry" in schema:
        rows += [mk_row("Atlas", fm.get("atlas")),
                 mk_row("Scale", fm.get("scale"))]
        for k, v in (fm.get("taxonomy") or {}).items():
            rows.append(mk_row(k.replace("_", " ").title(), v))

    elif "pathogen-entry" in schema:
        rows.append(mk_row("Class", fm.get("scale")))
        for k, v in (fm.get("taxonomy") or {}).items():
            rows.append(mk_row(k.replace("_", " ").title(), v))

    elif "medicine-entry" in schema:
        rows += [mk_row("Stream", fm.get("scale", fm.get("stream"))),
                 mk_row("Drug class", fm.get("drug_class")),
                 mk_row("Mechanism", fm.get("mechanism_brief")),
                 mk_row("Route", fm.get("route_of_administration"))]

    elif "vaccine-entry" in schema:
        platform = fm.get("platform", "")
        pname = SCHEMA_CONFIG["vaccine-entry"].get("platform_names", {}).get(platform, platform)
        rows.append(mk_row("Platform", pname))
        rows.append(mk_row("Delivery system", fm.get("delivery_system")))
        adj = fm.get("adjuvants") or []
        rows.append(mk_row("Adjuvants", ", ".join(str(a) for a in adj) if adj else "None"))
        rows.append(mk_row("Route", fm.get("route_of_administration")))
        ds = fm.get("dose_schedule")
        if isinstance(ds, dict):
            for k, v in ds.items():
                rows.append(mk_row(f"Dose — {k.replace('_', ' ')}", v))
        else:
            rows.append(mk_row("Dose schedule", ds))
        mfr = fm.get("manufacturer") or {}
        if isinstance(mfr, dict):
            rows.append(mk_row("Developer", mfr.get("developer")))
            partners = mfr.get("partners", [])
            if partners:
                rows.append(mk_row("Partners", ", ".join(str(p) for p in partners)))
        else:
            rows.append(mk_row("Manufacturer", mfr))
        rows.append(mk_row("Cold chain", fm.get("cold_chain")))
        for r in (fm.get("regulatory_status") or []):
            if isinstance(r, dict):
                rows.append(mk_row(
                    f'{r.get("body", "?")} ({r.get("date", "?")})', r.get("status")))

    return "\n            ".join(r for r in rows if r)


def build_eyebrow(fm, cfg, schema):
    if "human-scale-entry" in schema:
        scale = fm.get("scale", "")
        label = cfg.get("scale_names", {}).get(scale, scale)
        return f'{cfg["atlas_label"]} &middot; {cfg["atlas_sub"]} &middot; {esc(label)}'
    elif "pathogen-entry" in schema:
        return f'{cfg["atlas_label"]} &middot; {cfg["atlas_sub"]} &middot; {esc(fm.get("scale", ""))}'
    elif "medicine-entry" in schema:
        return f'{cfg["atlas_label"]} &middot; {cfg["atlas_sub"]} &middot; {esc(fm.get("scale", ""))}'
    elif "vaccine-entry" in schema:
        platform = fm.get("platform", "")
        pname = cfg.get("platform_names", {}).get(platform, platform)
        return f'{cfg["atlas_label"]} &middot; {cfg["atlas_sub"]} &middot; Platform {esc(pname)}'
    return cfg["atlas_label"]


def render(fm, cfg):
    schema = fm.get("schema", "")
    name = fm.get("name", fm.get("id", "Entry"))
    entry_id = fm.get("id", "")
    summary = fm.get("summary", "")
    aliases = fm.get("aliases") or []
    aliases_str = ", ".join(str(a) for a in aliases) if aliases else ""

    grad = f'background: linear-gradient(135deg, {cfg["grad_from"]}, {cfg["grad_to"]});'
    accent_bg = f'background: rgba({hex_to_rgb(cfg["accent"])},0.1); color: {cfg["accent"]};'

    stats_html = build_stats(fm, cfg, schema)
    meta_html = build_meta_table(fm, schema)
    eyebrow = build_eyebrow(fm, cfg, schema)

    cross_links = fm.get("cross_links") or []
    conn_html = ("\n            ".join(mk_pill(cl) for cl in cross_links)
                 if cross_links else "<p>No cross-links defined.</p>")

    sources = fm.get("sources") or []
    src_html = ("\n            ".join(mk_source(s) for s in sources)
                if sources else "<li>No sources listed.</li>")

    alias_line = (f'<p class="aliases">Also known as: {esc(aliases_str)}</p>'
                  if aliases_str else "")

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="{esc(summary[:160])}">
  <meta property="og:title" content="{esc(name)} — Human Engineering">
  <meta name="theme-color" content="#f2f2f7">
  <title>{esc(name)} — Human Engineering</title>
  <style>
{CSS}
  </style>
</head>
<body>

  <nav>
    <div class="nav-inner">
      <a href="index.html" class="brand">
        <span class="brand-mark" aria-hidden="true"></span>
        Human Engineering
      </a>
      <div class="nav-links">
        <a href="index.html#mission">Mission</a>
        <a href="pathogens.html">Pathogens</a>
        <a href="medicine.html">Medicine</a>
        <a href="index.html" class="nav-back">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M19 12H5"/><path d="M12 19l-7-7 7-7"/></svg>
          Home
        </a>
      </div>
    </div>
  </nav>

  <div class="hero">
    <div class="hero-eyebrow" style="{accent_bg}">{eyebrow}</div>
    <h1>{esc(name)}</h1>
    <p class="tagline">{esc(summary)}</p>
    {alias_line}
    <div class="stat-row">
        {stats_html}
    </div>
  </div>

  <main>
    <div class="stub-notice">
      This is an auto-generated stub page built from atlas entry frontmatter. A richer
      hand-crafted page is planned. See the
      <a href="https://github.com/bpupadhyaya/human/tree/main/atlases" target="_blank" rel="noopener noreferrer">atlas source</a>
      for the full entry including detailed body sections.
    </div>

    <div class="detail-card">
      <div class="detail-header" style="{grad}">
        <div class="entry-eyebrow">{esc(entry_id)}</div>
        <h2>{esc(name)}</h2>
        <p class="summary">{esc(summary)}</p>
      </div>
      <div class="detail-body">

        <div class="detail-section">
          <h3>Entry Metadata</h3>
          <table class="data-table">
            <tr><th>Field</th><th>Value</th></tr>
            {meta_html}
          </table>
        </div>

        <div class="detail-section">
          <h3>Cross-Atlas Connections</h3>
          <div class="connections">
            {conn_html}
          </div>
        </div>

        <div class="detail-section">
          <h3>Sources</h3>
          <ul class="refs">
            {src_html}
          </ul>
        </div>

      </div>
    </div>
  </main>

  <footer>
    <p class="footer-tag">Human Engineering is an open, free, global project to model human biology end-to-end — in the service of all of humanity.</p>
    <div class="footer-links">
      <a href="index.html">Home</a>
      <a href="pathogens.html">Pathogens</a>
      <a href="medicine.html">Medicine</a>
      <a href="https://github.com/bpupadhyaya/human" target="_blank" rel="noopener noreferrer">GitHub</a>
    </div>
    <p class="footer-meta">&copy; <span id="year"></span> Bhim Upadhyaya &middot; MIT License &middot; Built in the open.</p>
    <p class="footer-meta" style="margin-top:0.6rem;font-style:italic;"><em>This site is co-maintained by AI agents under human direction. Every effort is made for accuracy, but not every detail is manually reviewed each time.</em></p>
  </footer>

  <script>document.getElementById('year').textContent = new Date().getFullYear();</script>
</body>
</html>
"""


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true",
                        help="Print what would be generated without writing files.")
    args = parser.parse_args()

    generated, skipped_existing, skipped_no_id, errors = [], [], [], []

    for dirpath, _dirs, filenames in os.walk(ATLASES_DIR):
        if "README.md" not in filenames:
            continue
        readme_path = os.path.join(dirpath, "README.md")
        fm = parse_frontmatter(readme_path)
        if fm is None:
            continue

        entry_id = fm.get("id")
        if not entry_id:
            skipped_no_id.append(os.path.relpath(readme_path, REPO_ROOT))
            continue

        schema = fm.get("schema", "")
        cfg = find_cfg(schema)
        if cfg is None:
            skipped_no_id.append(f"{os.path.relpath(readme_path, REPO_ROOT)} (unknown schema: {schema!r})")
            continue

        out_path = os.path.join(DOCS_DIR, f"{entry_id}.html")
        if os.path.exists(out_path):
            skipped_existing.append(entry_id)
            continue

        if args.dry_run:
            print(f"  would generate → docs/{entry_id}.html  [{schema}]")
            generated.append(entry_id)
            continue

        try:
            html = render(fm, cfg)
            with open(out_path, "w", encoding="utf-8") as f:
                f.write(html)
            generated.append(entry_id)
            print(f"  + docs/{entry_id}.html")
        except Exception as exc:
            errors.append(f"{entry_id}: {exc}")
            print(f"  ! ERROR {entry_id}: {exc}", file=sys.stderr)

    verb = "Would generate" if args.dry_run else "Generated"
    print(f"\n{verb}: {len(generated)}")
    print(f"Skipped (hand-crafted page exists): {len(skipped_existing)}")
    print(f"Skipped (no id / unknown schema): {len(skipped_no_id)}")
    if errors:
        print(f"\nErrors ({len(errors)}):")
        for e in errors:
            print(f"  ! {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
