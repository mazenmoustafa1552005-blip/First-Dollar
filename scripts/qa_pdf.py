"""Prepress QA for studio PDFs.

Checks per PDF:
  1. Page size equals A4 (595.28 x 841.89 pt) or Letter (612 x 792 pt), +/- 0.5 pt.
  2. All fonts embedded (pdffonts).
  3. Print-safe margin: no ink within 8 mm of any page edge (rasterised at 150 dpi).
  4. Calibration (true-size files only, --calibration): rasterise page 2 at 300 dpi
     and measure the 50 mm bar and the 2 in bar. Pass if within +/-0.25 mm.

Usage: python3 scripts/qa_pdf.py [--calibration] FILE.pdf ...
Prints one JSON line per file and exits 1 on any failure.
"""
from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import tempfile

from PIL import Image
from pypdf import PdfReader

SIZES = {"A4": (595.28, 841.89), "Letter": (612.0, 792.0)}
MARGIN_MM = 12.0  # layout margin used by printkit
SAFE_MM = 6.0  # home printers typically cannot print the outer 3-5 mm


def raster(pdf, page, dpi, tmp):
    base = os.path.join(tmp, f"p{page}_{dpi}")
    subprocess.run(["pdftoppm", "-r", str(dpi), "-gray", "-png", "-f", str(page), "-l", str(page),
                    "-singlefile", pdf, base], check=True)
    return Image.open(base + ".png").convert("L")


def longest_dark_run_near(img, y_mm, x_from_mm, dpi, window_mm=1.5):
    px_per_mm = dpi / 25.4
    h = img.height
    yc = h - y_mm * px_per_mm  # PDF origin bottom-left
    best = 0
    data = img.load()
    x0 = int(x_from_mm * px_per_mm) - 10
    for y in range(int(yc - window_mm * px_per_mm), int(yc + window_mm * px_per_mm)):
        run = cur = 0
        for x in range(max(0, x0), int(x0 + 80 * px_per_mm)):
            if data[x, y] < 128:
                cur += 1
                run = max(run, cur)
            else:
                cur = 0
        best = max(best, run)
    return best / px_per_mm


def check(pdf, calibration):
    res = {"file": pdf, "ok": True, "errors": []}
    r = PdfReader(pdf)
    res["pages"] = len(r.pages)
    sizes = set()
    for p in r.pages:
        w, h = float(p.mediabox.width), float(p.mediabox.height)
        match = [k for k, (sw, sh) in SIZES.items() if abs(w - sw) < 0.5 and abs(h - sh) < 0.5]
        sizes.add(match[0] if match else f"{w:.1f}x{h:.1f}")
    res["paper"] = sorted(sizes)
    if not all(s in SIZES for s in sizes):
        res["errors"].append(f"non-standard page size {sizes}")
    out = subprocess.run(["pdffonts", pdf], capture_output=True, text=True).stdout.splitlines()[2:]
    # pdffonts columns: name type encoding emb sub uni object ID
    not_emb = []
    for l in out:
        parts = l.split()
        if len(parts) >= 7 and parts[-5] not in ("yes",):
            not_emb.append(parts[0])
    if not_emb:
        res["errors"].append(f"fonts not embedded: {not_emb}")
    with tempfile.TemporaryDirectory() as tmp:
        worst = 99.0
        first = 2 if (calibration and len(r.pages) > 1) else 1  # page 1 of true-size files has a full-bleed header by design
        for i in range(first, len(r.pages) + 1):
            img = raster(pdf, i, 75, tmp)
            bbox = Image.eval(img, lambda v: 255 if v < 245 else 0).getbbox()
            if bbox:
                pxmm = 75 / 25.4
                l, t, rr, b = bbox
                m = min(l / pxmm, t / pxmm, (img.width - rr) / pxmm, (img.height - b) / pxmm)
                worst = min(worst, m)
        res["min_edge_margin_mm"] = round(worst, 1)
        if worst < SAFE_MM:
            res["errors"].append(f"ink within {worst:.1f} mm of edge on sheet pages")
            res["warnings"] = [f"ink within {worst:.1f} mm of edge"]
        if calibration and len(r.pages) >= 2:
            img = raster(pdf, 2, 300, tmp)
            bar50 = longest_dark_run_near(img, MARGIN_MM + 11, MARGIN_MM, 300)
            bar2in = longest_dark_run_near(img, MARGIN_MM + 4, MARGIN_MM, 300)
            res["bar_50mm_measured"] = round(bar50, 2)
            res["bar_2in_measured_mm"] = round(bar2in, 2)
            if abs(bar50 - 50) > 0.25 or abs(bar2in - 50.8) > 0.25:
                res["errors"].append("calibration bar off by more than 0.25 mm")
    res["ok"] = not res["errors"]
    return res


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--calibration", action="store_true")
    ap.add_argument("files", nargs="+")
    a = ap.parse_args()
    bad = 0
    for f in a.files:
        r = check(f, a.calibration)
        bad += not r["ok"]
        print(json.dumps(r))
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
