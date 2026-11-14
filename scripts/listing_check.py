"""Check listing copy against the real customer files.

Usage: python3 scripts/listing_check.py <SKU>

Reads products/<SKU>/listing/listing.md. The file must contain a block

```claims
key: value
```
Supported claim keys (all optional):
  hostguide_pages, printpack_pages : int, checked with pypdf on every variant
  scales                          : comma list like 6,12,16,24 (files must exist for each, no others)
  papers                          : comma list A4,Letter
  bw_version                      : yes/no (InkSaverBW files present)
Also checks: Etsy title <= 140 chars, exactly 13 tags each <= 20 chars, and
blocked words (playtested, tested pattern, bestseller, best seller) unless the
manifest status allows them. Exit 1 on any failure.
"""
import glob
import os
import re
import sys

from pypdf import PdfReader

sku = sys.argv[1]
root = os.path.join("products", sku)
txt = open(os.path.join(root, "listing", "listing.md")).read()
files = sorted(glob.glob(os.path.join(root, "customer-files", "*.pdf")))
errs, notes = [], []

m = re.search(r"```claims\n(.*?)```", txt, re.S)
claims = dict(l.split(":", 1) for l in m.group(1).strip().splitlines()) if m else {}
claims = {k.strip(): v.strip() for k, v in claims.items()}


def pages(pattern):
    return {os.path.basename(f): len(PdfReader(f).pages) for f in files if pattern in os.path.basename(f)}


for key, pat in (("hostguide_pages", "HostGuide"), ("printpack_pages", "PrintPack")):
    if key in claims:
        got = pages(pat)
        bad = {f: n for f, n in got.items() if n != int(claims[key])}
        (errs if bad or not got else notes).append(f"{key}={claims[key]} actual={got}")
if "scales" in claims:
    want = {s.strip() for s in claims["scales"].split(",")}
    have = {re.search(r"_1-(\d+)_", os.path.basename(f)).group(1) for f in files if "_1-" in f}
    (errs if want != have else notes).append(f"scales claimed={sorted(want)} files={sorted(have)}")
if "papers" in claims:
    want = {s.strip() for s in claims["papers"].split(",")}
    have = {p for p in ("A4", "Letter") if any(f"_{p}" in os.path.basename(f) for f in files)}
    (errs if want != have else notes).append(f"papers claimed={sorted(want)} files={sorted(have)}")
if "bw_version" in claims:
    have = any("BW" in f for f in files)
    (errs if (claims["bw_version"] == "yes") != have else notes).append(f"bw_version={claims['bw_version']} present={have}")

t = re.search(r"^## Title\n+(.+)$", txt, re.M)
if not t:
    errs.append("missing '## Title'")
elif len(t.group(1).strip()) > 140:
    errs.append(f"title {len(t.group(1).strip())} chars > 140")
else:
    notes.append(f"title {len(t.group(1).strip())} chars")
tg = re.search(r"^## Tags\n+(.+)$", txt, re.M)
tags = [x.strip() for x in tg.group(1).split(",")] if tg else []
if len(tags) != 13 or any(len(x) > 20 for x in tags):
    errs.append(f"tags: {len(tags)} tags, too long: {[x for x in tags if len(x) > 20]}")
else:
    notes.append("13 tags ok")
for w in ("playtested", "tested pattern", "bestseller", "best seller"):
    body = txt.split("```claims")[0].lower()
    if w in body:
        errs.append(f"blocked claim word present: {w}")

for n in notes:
    print("ok  ", n)
for e in errs:
    print("FAIL", e)
sys.exit(1 if errs else 0)
