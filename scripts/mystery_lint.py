"""Check a mystery content module against the countable design rules
(research/game-design-psychology.md): suspects <= 6, evidence <= 12 and <= 4 per
round, evidence card <= 50 words, suspect card <= 50 words, sentences <= 12 words
(warn at 13-14). Usage: python3 scripts/mystery_lint.py <module_key>"""
import importlib, re, sys
sys.path.insert(0, "scripts")
g = importlib.import_module(f"mystery_content_{sys.argv[1]}")
errs, warns = [], []
if len(g.SUSPECTS) > 6: errs.append(f"{len(g.SUSPECTS)} suspects > 6")
if len(g.EVIDENCE) > 12: errs.append(f"{len(g.EVIDENCE)} evidence > 12")
for r in {e["round"] for e in g.EVIDENCE}:
    n = sum(e["round"] == r for e in g.EVIDENCE)
    if n > 4: errs.append(f"round {r} has {n} cards > 4")
def sentences(t): return [x for x in re.split(r"[.!?]\s+|\n", t) if x.strip()]
for e in g.EVIDENCE:
    w = len(e["text"].split())
    if w > 50: errs.append(f"{e['id']} {w} words > 50")
    for s in sentences(e["text"]):
        n = len(s.split())
        if n > 14: errs.append(f"{e['id']} sentence {n} words: {s[:40]}")
        elif n > 12: warns.append(f"{e['id']} sentence {n} words")
for s in g.SUSPECTS:
    w = sum(len(s[k].split()) for k in ("wearing", "said", "fact"))
    if w > 50: errs.append(f"{s['id']} card {w} words > 50")
print(f"{g.SKU}: {len(g.SUSPECTS)} suspects, {len(g.EVIDENCE)} cards")
for w in warns: print("warn", w)
for e in errs: print("FAIL", e)
sys.exit(1 if errs else 0)
