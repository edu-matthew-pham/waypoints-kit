#!/usr/bin/env python3
"""Build the kit's per-subject standard indexes from the ACARA Progressions data.

Usage:  python3 tools/build_index.py /path/to/acara-progressions/static/data
        python3 tools/build_index.py --cross-subject

Reads every node file (Progressions static/data, copied into the kit's data/ folder) (JSON with a top-level "standard" that has "nodes"),
and writes index/<subject>.md plus index/README.md into the kit root.
Re-run whenever the Progressions data changes.

--cross-subject only rebuilds index/cross-subject.md from data/cross-subject/ and refreshes the Other subjects
column in the existing index/<subject>.md tables. Run it after editing links.json or shared-ideas.json (and
tools/check_links.py first).
"""
import glob
import json
import os
import sys
from collections import defaultdict

BASE_URL = "https://raw.githubusercontent.com/edu-matthew-pham/waypoints-kit/main/data/"
KIT_DATA_BASE = BASE_URL


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

    info = {r[1].upper(): (subject, r[0], r[2]) for subject, rows in by_subject.items() for r in rows}
    cross_counts = build_cross_subject(out_dir, info)

    for subject, rows in sorted(by_subject.items()):
        rows.sort(key=lambda r: (year_key(r[0]), r[1]))
        lines = [
            f"# {subject}: standards with node files",
            "",
            "Open the link in the last column for the standard you need.",
            "",
            "The Other subjects column counts a standard's links to other subjects and the shared ideas it belongs to; the number links to its entry in [cross-subject.md](cross-subject.md).",
            "",
            "| Year | Code | Title | Waypoints | Other subjects | Node file |",
            "|---|---|---|---|---|---|",
        ]
        for year, code, title, n, rel in rows:
            k = cross_counts.get(code.upper(), 0)
            other = f"[{k}](cross-subject.md#{code.lower()})" if k else ""
            lines.append(f"| {year} | {code} | {title.replace('|', '/')} | {n} | {other} | {BASE_URL}{rel} |")
        with open(os.path.join(out_dir, f"{subject}.md"), "w", encoding="utf-8") as fh:
            fh.write("\n".join(lines) + "\n")

    # Glossary files: {subject}/*_glossary.json hold a whole year band. Slice them per standard
    # (data/glossary/<code>.json) so each is small enough to fetch whole, and index the slices.
    gl_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data", "glossary")
    os.makedirs(gl_dir, exist_ok=True)
    gl_rows = []
    for path in sorted(glob.glob(os.path.join(src, "**", "*_glossary.json"), recursive=True)):
        rel = os.path.relpath(path, src).replace(os.sep, "/")
        try:
            with open(path, encoding="utf-8") as fh:
                g = json.load(fh)
        except Exception:
            continue
        if not isinstance(g, dict) or not g.get("teacher_glossary"):
            continue
        by_code = defaultdict(lambda: {"teacher_glossary": [], "student_glossary": []})
        for e in g.get("teacher_glossary", []):
            if e.get("descriptor_code"):
                by_code[e["descriptor_code"]]["teacher_glossary"].append(e)
        for e in g.get("student_glossary", []):
            if e.get("descriptor_code"):
                by_code[e["descriptor_code"]]["student_glossary"].append(e)
        for code, parts in by_code.items():
            slice_ = {"subject": g.get("subject"), "year_levels": g.get("year_levels"), "descriptor_code": code, **parts}
            with open(os.path.join(gl_dir, f"{code}.json"), "w", encoding="utf-8") as fh:
                json.dump(slice_, fh, ensure_ascii=False, indent=1)
            gl_rows.append((rel.split("/")[0], code, len(parts["teacher_glossary"])))
    gl = [
        "# Glossaries",
        "",
        "Pre-built vocabulary for some standards, one small file per standard. Each has `teacher_glossary` (definition, likely misconception, response; `first_waypoint` says where a term first appears) and `student_glossary` (plain definition, example, sometimes sub-terms).",
        "",
        "If a standard isn't in the table, there is no pre-built glossary for it: draft one from the node file.",
        "",
        "| Subject | Standard | Terms | Glossary file |",
        "|---|---|---|---|",
    ]
    for subj, code, n in sorted(gl_rows):
        gl.append(f"| {subj} | {code} | {n} | {KIT_DATA_BASE}glossary/{code}.json |")
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
    readme.append("- [cross-subject](cross-subject.md): links between standards in different subjects, and shared ideas")
    with open(os.path.join(out_dir, "README.md"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(readme) + "\n")
    print({s: len(r) for s, r in sorted(by_subject.items())})


def build_cross_subject(out_dir, info):
    """Write index/cross-subject.md from data/cross-subject/links.json and shared-ideas.json.

    Each standard gets one entry: what it builds on from other subjects, what uses it in other
    subjects (derived from the same links), and the shared ideas it belongs to. Returns link counts by code.
    """
    cs_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data", "cross-subject")
    try:
        links = json.load(open(os.path.join(cs_dir, "links.json"), encoding="utf-8"))["links"]
        threads = json.load(open(os.path.join(cs_dir, "shared-ideas.json"), encoding="utf-8"))["shared_ideas"]
    except FileNotFoundError:
        return {}

    def name(code, nodes=None):
        subj, year, title = info.get(code.upper(), ("?", "?", ""))
        ns = f" node {', '.join(map(str, nodes))}" if nodes else ""
        return f"{code}{ns} {title} ({subj}, Year {year})"

    def kind(l):
        bits = [l["relationship"]] if l.get("relationship") else []
        if l.get("overlap"):
            bits.append(f"overlap: {l['overlap']}")
        if l.get("shared_foundation"):
            bits.append("shared foundation")
        if l.get("wording_watch"):
            bits.append(f"wording watch: \"{l['wording_watch']}\"")
        bits.append(l["timing"].replace("_", " "))
        return ", ".join(bits)

    ROLE = {"first": "First", "builds_on": "Builds on", "applies": "Applies", "repeats": "Repeats"}
    entries = defaultdict(lambda: {"on": [], "by": [], "threads": []})
    for l in links:
        a, b = l["standard"].upper(), l["links_to"].upper()
        mine = f"node {', '.join(map(str, l['nodes']))}: " if l.get("nodes") else ""
        theirs = f"node {', '.join(map(str, l['links_to_nodes']))}: " if l.get("links_to_nodes") else ""
        note = f" {l['note']}" if l.get("note") else ""
        entries[a]["on"].append(f"- {mine}{name(b, l.get('links_to_nodes'))}. {kind(l)}.{note}")
        entries[b]["by"].append(f"- {theirs}{name(a, l.get('nodes'))}. {kind(l)}.{note}")
    for th in threads:
        for m in th["members"]:
            entries[m["standard"].upper()]["threads"].append(f"- [{th['title']}](#{th['id']}) ({ROLE[m['role']]}): {m['frame']}")

    out = [
        "# Cross-subject links",
        "",
        "Links between standards in different subjects, and ideas taught in more than one place. A standard's prior knowledge in its own subject is in its node file (`prior_knowledge`); this page covers the rest. Made by `tools/build_index.py` from `data/cross-subject/links.json` and `shared-ideas.json`; edit those, not this page.",
        "",
        "Timing compares the other standard's year with this one's: earlier, same year or later. Something taught later can't be assumed: teach the small piece in the lesson.",
        "",
        "## Shared ideas",
        "",
    ]
    out += ["Skill ideas are ways of thinking each subject uses its own way; topic ideas are content taught in more than one place. Roles: First (where students first meet it), Builds on (goes deeper), Applies (uses it in its own context), Repeats (teaches it again at about the same level, often the same year: worth coordinating).", ""]
    for th in sorted(threads, key=lambda t: t["kind"] != "topic"):
        out += [f"### {th['title']} ({th['kind']})", "", f'<a id="{th["id"]}"></a>{th["description"]}', ""]
        out += [f"- {ROLE[m['role']]}: {name(m['standard'], m.get('nodes'))}. {m['frame']}" for m in th["members"]]
        if th.get("outside_kit"):
            out += ["", th["outside_kit"]]
        out.append("")
    out += ["## By standard", ""]
    for code in sorted(entries, key=lambda c: (info.get(c, ("~",))[0], year_key(info.get(c, ("", "99"))[1]), c)):
        e = entries[code]
        out += [f"### {name(code)}", "", f'<a id="{code.lower()}"></a>']
        if e["on"]:
            out += ["Builds on, from other subjects:", ""] + e["on"] + [""]
        if e["by"]:
            out += ["Used in other subjects by:", ""] + e["by"] + [""]
        if e["threads"]:
            out += ["Shared ideas:", ""] + e["threads"] + [""]
    with open(os.path.join(out_dir, "cross-subject.md"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(out))
    return {c: len(e["on"]) + len(e["by"]) + len(e["threads"]) for c, e in entries.items()}


def cross_only():
    """Rebuild index/cross-subject.md and the Other subjects column, leaving the rest of the index as it is."""
    root = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
    out_dir = os.path.join(root, "index")
    info = {}
    for path in glob.glob(os.path.join(root, "data", "*", "*.json")):
        try:
            d = json.load(open(path, encoding="utf-8"))
        except Exception:
            continue
        std = d.get("standard") if isinstance(d, dict) else None
        if isinstance(std, dict) and "nodes" in std:
            info[std["code"].upper()] = (os.path.basename(os.path.dirname(path)), d.get("year_level", ""), std.get("title", ""))
    counts = build_cross_subject(out_dir, info)
    note = "The Other subjects column counts a standard's links to other subjects and the shared ideas it belongs to; the number links to its entry in [cross-subject.md](cross-subject.md)."
    for path in glob.glob(os.path.join(out_dir, "*.md")):
        lines = open(path, encoding="utf-8").read().split("\n")
        try:
            h = lines.index(next(l for l in lines if l.startswith("| Year | Code |")))
        except StopIteration:
            continue
        cols = [c.strip() for c in lines[h].strip("|").split("|")]
        if "Other subjects" not in cols:
            at = cols.index("Node file")
            lines[h] = "| " + " | ".join(cols[:at] + ["Other subjects"] + cols[at:]) + " |"
            lines[h + 1] = "|" + "---|" * (len(cols) + 1)
            if note not in lines:
                lines[h:h] = [note, ""]
                h += 2
            fresh = True
        else:
            at, fresh = cols.index("Other subjects"), False
        for i in range(h + 2, len(lines)):
            if not lines[i].startswith("| "):
                break
            cells = [c.strip() for c in lines[i].strip().strip("|").split("|")]
            code = cells[1].upper()
            k = counts.get(code, 0)
            val = f"[{k}](cross-subject.md#{code.lower()})" if k else ""
            if fresh:
                cells.insert(at, val)
            else:
                cells[at] = val
            lines[i] = "| " + " | ".join(cells) + " |"
        with open(path, "w", encoding="utf-8") as fh:
            fh.write("\n".join(lines))
    readme = os.path.join(out_dir, "README.md")
    text = open(readme, encoding="utf-8").read()
    line = "- [cross-subject](cross-subject.md): links between standards in different subjects, and shared ideas"
    if line not in text:
        with open(readme, "w", encoding="utf-8") as fh:
            fh.write(text.rstrip("\n") + "\n" + line + "\n")
    print(f"cross-subject.md: {len(counts)} standards")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    if sys.argv[1] == "--cross-subject":
        cross_only()
    else:
        main(sys.argv[1])
