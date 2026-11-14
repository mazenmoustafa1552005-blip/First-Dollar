"""Crochet pattern source-of-truth + stitch-count validator + text renderer.

Each round is a list of (group, times). A group is a list of ops; each op has
(consumed, produced) stitches. The validator checks that every round consumes
exactly the previous round's stitch count (unless it is marked partial) and
that the stated count equals the produced count. Text is rendered from the
same data, so the written pattern cannot drift from the checked counts.

Usage: python3 scripts/crochet_pattern.py --pattern whale [--md OUT.md]
Exit code 1 on any count error.
"""
from __future__ import annotations

import argparse
import sys

# ---------------------------------------------------------------- ops


def sc(n=1):
    return ("sc" if n == 1 else f"sc {n}", n, n)


def inc():
    return ("inc", 1, 2)


def dec():
    return ("dec", 2, 1)


def mr(n):
    return (f"{n} sc in magic ring", 0, n)


def in_one(text, k):
    """k stitches worked into one stitch, e.g. '(hdc, dc) in next st'."""
    return (text, 1, k)


def slst():
    return ("sl st in next st", 1, 1)


def render_group(group, times):
    body = ", ".join(op[0] for op in group)
    if times == 1:
        return body
    if len(group) == 1:
        return f"{body} x{times}"
    return f"({body}) x{times}"


def round_counts(groups):
    consumed = sum(sum(op[1] for op in g) * t for g, t in groups)
    produced = sum(sum(op[2] for op in g) * t for g, t in groups)
    return consumed, produced


# ---------------------------------------------------------------- patterns

WHALE = {
    "sku": "CRO-SEA-01",
    "name": "Bubbles the No-Sew Whale",
    "status": "DRAFT: not yet crocheted or tester-checked. Size and yardage are estimates.",
    "terms": "US crochet terms",
    "materials": [
        "Worsted weight (US 4 / aran-ish) cotton or acrylic yarn: main color about 30 to 40 m (estimate, confirm on sample)",
        "Small amount of contrast yarn for the fins (optional, can be main color)",
        "3.5 mm (E-4) crochet hook",
        "Pair of 8 mm safety eyes (for children under 3, embroider eyes instead)",
        "Polyester fiberfill stuffing, stitch marker, yarn needle for weaving in ends only",
    ],
    "gauge": "Gauge is not critical. Work tightly so stuffing does not show. "
             "Expected finished size about 11 to 13 cm long (estimate, to be measured on the sample).",
    "abbrev": {"MR": "magic ring", "sc": "single crochet", "inc": "2 sc in the same stitch",
               "dec": "single crochet decrease (invisible decrease recommended)", "hdc": "half double crochet",
               "dc": "double crochet", "sl st": "slip stitch", "ch": "chain", "st(s)": "stitch(es)"},
    "sections": [
        {"title": "Body (worked in continuous rounds from the nose)", "mode": "round", "start": 0,
         "rows": [
             ("R1", [([mr(6)], 1)], 6, None),
             ("R2", [([inc()], 6)], 12, None),
             ("R3", [([sc(), inc()], 6)], 18, None),
             ("R4", [([sc(2), inc()], 6)], 24, None),
             ("R5", [([sc(3), inc()], 6)], 30, None),
             ("R6", [([sc(4), inc()], 6)], 36, None),
             ("R7-R12", [([sc(36)], 1)], 36, "6 rounds. After R9, insert safety eyes between R9 and R10, about 8 sts apart."),
             ("R13", [([sc(4), dec()], 6)], 30, None),
             ("R14-R15", [([sc(30)], 1)], 30, "2 rounds."),
             ("R16", [([sc(3), dec()], 6)], 24, None),
             ("R17", [([sc(24)], 1)], 24, "Fasten the eye backs now. Begin stuffing firmly."),
             ("R18", [([sc(2), dec()], 6)], 18, None),
             ("R19", [([sc(), dec()], 6)], 12, "Finish stuffing the body. Leave the last part lightly stuffed."),
             ("R20", [([sc(12)], 1)], 12, None),
             ("R21", [([sc(), dec()], 4)], 8, None),
             ("R22", [([sc(8)], 1)], 8, "Do not stuff the tail."),
         ]},
        {"title": "Tail fluke (worked in rows straight off the body, no sewing)", "mode": "row", "start": 8,
         "rows": [
             ("Row 1", [([("sc 4 through both layers", 8, 4)], 1)], 4,
              "Flatten the opening so the stitches line up in 4 pairs. Work each sc through one stitch of the front and one of the back. Ch 1, turn."),
             ("Row 2", [([inc()], 4)], 8, "Ch 1, turn."),
             ("Row 3", [([in_one("(hdc, dc) in next st", 2), ("dc in next st", 1, 1),
                          in_one("(dc, hdc) in next st", 2), slst()], 2)], 12,
              "Fasten off and weave in the end."),
         ]},
        {"title": "Fins (make 2, crocheted directly onto the body)", "mode": "row", "start": None,
         "rows": [
             ("Fin", [([("ch 4", 0, 4)], 1)], 4,
              "Hold the whale nose up. Join yarn with a sl st around a stitch of R12 on one side, level with the eye "
              "and 3 rounds below it."),
             ("Fin, continued", [([("sc in 2nd ch from hook", 1, 1), ("hdc in next ch", 1, 1), ("dc in last ch", 1, 1)], 1)], 3,
              "Sl st around the next stitch of R12 to anchor. Fasten off, pull the tail inside the body. Repeat on the other side."),
         ]},
    ],
    "assembly": [
        "There is no sewing of parts: the tail is worked straight off the body and the fins are crocheted onto it.",
        "A yarn needle is used only to weave in ends.",
    ],
    "photos_needed": ["Materials flat lay", "R6 flat circle", "Eyes placed after R9", "Stuffing at R17",
                      "Flattened opening for the tail", "Finished tail", "Joining a fin", "Finished whale, 3 angles",
                      "Whale next to a ruler for size"],
}

PATTERNS = {"whale": WHALE}


def validate(p):
    errors = []
    for sec in p["sections"]:
        prev = sec["start"]
        for label, groups, stated, _note in sec["rows"]:
            consumed, produced = round_counts(groups)
            if prev is not None and consumed != prev and sec["start"] is not None:
                errors.append(f"{sec['title']} {label}: consumes {consumed} but previous count is {prev}")
            if produced != stated:
                errors.append(f"{sec['title']} {label}: produces {produced} but states ({stated})")
            prev = produced
    return errors


def to_markdown(p):
    out = [f"# {p['name']} ({p['sku']})", "", f"> {p['status']}", "", f"Terminology: {p['terms']}", "", "## Materials"]
    out += [f"- {m}" for m in p["materials"]]
    out += ["", "## Gauge and size", p["gauge"], "", "## Abbreviations"]
    out += [f"- **{k}**: {v}" for k, v in p["abbrev"].items()]
    for sec in p["sections"]:
        out += ["", f"## {sec['title']}"]
        for label, groups, stated, note in sec["rows"]:
            text = ", ".join(render_group(g, t) for g, t in groups)
            out.append(f"- **{label}:** {text} ({stated})" + (f". {note}" if note else ""))
    out += ["", "## Assembly"] + [f"- {a}" for a in p["assembly"]]
    out += ["", "## Step photos required before release"] + [f"- [ ] {ph}" for ph in p["photos_needed"]]
    return "\n".join(out) + "\n"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pattern", required=True, choices=sorted(PATTERNS))
    ap.add_argument("--md")
    a = ap.parse_args()
    p = PATTERNS[a.pattern]
    errs = validate(p)
    for e in errs:
        print("ERROR", e)
    if a.md:
        with open(a.md, "w") as f:
            f.write(to_markdown(p))
    print("stitch counts OK" if not errs else f"{len(errs)} errors")
    sys.exit(1 if errs else 0)


if __name__ == "__main__":
    main()
