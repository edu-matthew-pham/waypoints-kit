#!/usr/bin/env python3
"""Build the kit's per-subject standard indexes from the ACARA Progressions data.

Usage:  python3 tools/build_index.py /path/to/acara-progressions/static/data

Reads every node file (Progressions static/data, copied into the kit's data/ folder) (JSON with a top-level "standard" that has "nodes"),
and writes index/<subject>.md plus index/README.md into the kit root.
Re-run whenever the Progressions data changes.
"""
import glob
import json
import os
import sys
from collections import defaultdict

BASE_URL = "https://raw.githubusercontent.com/edu-matthew-pham/waypoints-kit/main/data/"


def year_key(y):
    s = str(y)
    if s.upper() == "F":
        return (0, s)
    digits = "".join(c for c in s if c.isdigit())
    return (int(digits) if digits else 99, s)


def main(src):
    out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "index")
    os.makedirs(out_dir, exist_ok=True)
    by_subject = defaultdict(list)
    for path in sorted(glob.glob(os.path.join(src, "**", "*.json"), recursive=True)):
        rel = os.path.relpath(path, src).replace(os.sep, "/")
        try:
            with open(path, encoding="utf-8") as fh:
                d = json.load(fh)
        except Exception:
            continue
        std = d.get("standard") if isinstance(d, dict) else None
        if not isinstance(std, dict) or "nodes" not in std:
            continue
        by_subject[rel.split("/")[0]].append(
            (d.get("year_level", ""), std.get("code", ""), std.get("title", ""), len(std["nodes"]), rel)
        )

    for subject, rows in sorted(by_subject.items()):
        rows.sort(key=lambda r: (year_key(r[0]), r[1]))
        lines = [
            f"# {subject}: standards with node files",
            "",
            "Open the link in the last column for the standard you need.",
            "",
            "| Year | Code | Title | Waypoints | Node file |",
            "|---|---|---|---|---|",
        ]
        for year, code, title, n, rel in rows:
            lines.append(f"| {year} | {code} | {title.replace('|', '/')} | {n} | {BASE_URL}{rel} |")
        with open(os.path.join(out_dir, f"{subject}.md"), "w", encoding="utf-8") as fh:
            fh.write("\n".join(lines) + "\n")

    # Glossary files: {subject}/*_glossary.json with teacher_glossary entries keyed by descriptor_code
    gl_rows = []
    for path in sorted(glob.glob(os.path.join(src, "**", "*_glossary.json"), recursive=True)):
        rel = os.path.relpath(path, src).replace(os.sep, "/")
        try:
            with open(path, encoding="utf-8") as fh:
                g = json.load(fh)
        except Exception:
            continue
        entries = g.get("teacher_glossary") if isinstance(g, dict) else None
        if not entries:
            continue
        codes = sorted({e.get("descriptor_code", "") for e in entries if e.get("descriptor_code")})
        gl_rows.append((rel.split("/")[0], ", ".join(str(y) for y in g.get("year_levels", [])), len(entries), codes, rel))
    gl = [
        "# Glossaries",
        "",
        "Pre-built vocabulary for some subjects. Open the link for the file you need. Each file has `teacher_glossary` (definition, likely misconception, response) and `student_glossary` (plain definition, example). Filter entries by `descriptor_code`; `first_waypoint` says where a term first appears.",
        "",
        "If a standard's code isn't listed under any file below, there is no pre-built glossary for it: draft one from the node file.",
        "",
        "| Subject | Years | Terms | Glossary file | Standards covered |",
        "|---|---|---|---|---|",
    ]
    for subj, yrs, n, codes, rel in gl_rows:
        gl.append(f"| {subj} | {yrs} | {n} | {BASE_URL}{rel} | {', '.join(codes)} |")
    with open(os.path.join(out_dir, "glossaries.md"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(gl) + "\n")

    readme = [
        "# Index of standards",
        "",
        "Every standard with a node file, by subject. Each table row ends in the link to its node file.",
        "",
    ]
    for subject, rows in sorted(by_subject.items()):
        readme.append(f"- [{subject}]({subject}.md): {len(rows)} standards")
    readme.append("")
    readme.append("- [glossaries](glossaries.md): pre-built vocabulary files (some subjects only)")
    with open(os.path.join(out_dir, "README.md"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(readme) + "\n")
    print({s: len(r) for s, r in sorted(by_subject.items())})


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    main(sys.argv[1])
