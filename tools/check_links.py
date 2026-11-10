#!/usr/bin/env python3
"""Check data/cross-subject/links.json and threads.json against the node files.

Usage:  python3 tools/check_links.py
Exits with status 1 and lists the problems if any check fails. Run it after editing either file.

Checks: every standard and node exists; field values are allowed; timing agrees with the two standards'
years; a link joins two different subjects; no link is listed twice; every thread named in a link exists.
"""
import glob
import json
import os
import sys

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
DATA = os.path.join(ROOT, "data")
RELATIONSHIPS = {"prerequisite", "application", "background"}
OVERLAPS = {"reinforce", "share", "open"}
TIMINGS = {"earlier", "same_year", "later"}
LINK_FIELDS = {"standard", "nodes", "links_to", "links_to_nodes", "relationship", "overlap",
               "shared_foundation", "wording_watch", "timing", "thread", "note"}


def years(y):
    """Year level ('F', '7', '7-8') as a (first, last) pair; Foundation is 0."""
    parts = [0 if p.strip().upper() == "F" else int(p) for p in str(y).split("-")]
    return parts[0], parts[-1]


def load_standards():
    std = {}
    for f in glob.glob(os.path.join(DATA, "*", "*.json")):
        try:
            d = json.load(open(f, encoding="utf-8"))
        except ValueError:
            continue
        s = d.get("standard") if isinstance(d, dict) else None
        if not s or "nodes" not in s:
            continue
        std[s["code"].upper()] = {
            "subject": os.path.basename(os.path.dirname(f)),
            "years": years(d["year_level"]),
            "nodes": {int(n["id"]) for n in s["nodes"] if str(n.get("id", "")).isdigit()},
        }
    return std


def main():
    std = load_standards()
    links = json.load(open(os.path.join(DATA, "cross-subject", "links.json"), encoding="utf-8"))["links"]
    threads = json.load(open(os.path.join(DATA, "cross-subject", "threads.json"), encoding="utf-8"))["threads"]
    problems = []

    def check_nodes(code, nodes, where):
        if code.upper() not in std:
            problems.append(f"{where}: no node file for {code}")
            return False
        for n in nodes or []:
            if n not in std[code.upper()]["nodes"]:
                problems.append(f"{where}: {code} has no node {n}")
        return True

    seen = set()
    for i, l in enumerate(links):
        where = f"links[{i}] {l.get('standard')} -> {l.get('links_to')}"
        extra = set(l) - LINK_FIELDS
        if extra:
            problems.append(f"{where}: unknown field(s) {sorted(extra)}")
        a, b = l.get("standard", ""), l.get("links_to", "")
        ok = check_nodes(a, l.get("nodes"), where) & check_nodes(b, l.get("links_to_nodes"), where)
        if l.get("relationship") not in RELATIONSHIPS | {None}:
            problems.append(f"{where}: relationship must be one of {sorted(RELATIONSHIPS)}")
        if l.get("overlap") not in OVERLAPS | {None}:
            problems.append(f"{where}: overlap must be one of {sorted(OVERLAPS)}")
        if not (l.get("relationship") or l.get("overlap") or l.get("shared_foundation") or l.get("wording_watch")):
            problems.append(f"{where}: needs a relationship, an overlap, shared_foundation or wording_watch")
        t = l.get("timing")
        if t not in TIMINGS:
            problems.append(f"{where}: timing must be one of {sorted(TIMINGS)}")
        if l.get("thread") and l["thread"] not in {th["id"] for th in threads}:
            problems.append(f"{where}: no thread '{l['thread']}'")
        key = (a.upper(), tuple(l.get("nodes") or []), b.upper(), tuple(l.get("links_to_nodes") or []))
        if key in seen:
            problems.append(f"{where}: listed twice")
        seen.add(key)
        if not ok:
            continue
        sa, sb = std[a.upper()], std[b.upper()]
        if sa["subject"] == sb["subject"]:
            problems.append(f"{where}: same subject ({sa['subject']}); use prior_knowledge in the node file")
        (a1, a2), (b1, b2) = sa["years"], sb["years"]
        # Two-year bands overlap single years, so only a clear contradiction is an error.
        if t == "earlier" and b1 > a1:
            problems.append(f"{where}: timing 'earlier' but {b} starts after {a}")
        if t == "later" and b2 < a1:
            problems.append(f"{where}: timing 'later' but {b} comes before {a}")
        if t == "same_year" and (b2 < a1 or b1 > a2):
            problems.append(f"{where}: timing 'same_year' but the years don't overlap")

    ids = set()
    for th in threads:
        if th["id"] in ids:
            problems.append(f"thread {th['id']}: listed twice")
        ids.add(th["id"])
        for m in th["members"]:
            check_nodes(m["standard"], m.get("nodes"), f"thread {th['id']}")
        if len({std.get(m['standard'].upper(), {}).get('subject') for m in th["members"]}) < 2:
            problems.append(f"thread {th['id']}: members are all one subject")

    if problems:
        print("\n".join(problems))
        sys.exit(1)
    print(f"OK: {len(links)} links, {len(threads)} threads")


if __name__ == "__main__":
    main()
