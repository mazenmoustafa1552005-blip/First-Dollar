"""Build true-size printable dollhouse miniature PDFs.

Usage:
    python3 scripts/minis_build.py --set grocery [--out products]

Artwork for every item is drawn ONCE in real-life millimetres and scaled by
1/scale with a PDF transform, so all scales stay proportional. Cut lines,
fold lines and glue tabs are drawn afterwards at true size (not scaled) so
they stay crisp and printable.

Each output PDF = 1 instruction page (scale, item list with final dimensions,
assembly notes, calibration) + sheet pages (pieces, calibration on each page).
"""
from __future__ import annotations

import argparse
import json
import math
import os
import sys

from reportlab.lib.colors import HexColor, white
from reportlab.lib.units import mm

sys.path.insert(0, os.path.dirname(__file__))
import printkit as pk  # noqa: E402
from minis_sets import SETS  # noqa: E402

MARGIN = 12.0
GAP = 3.5
HEADER_H = 14.0
CAL_H = 18.0


# --------------------------------------------------------------------------
# Piece geometry
# --------------------------------------------------------------------------

def tab_size(*dims: float) -> float:
    """Glue tab depth in mm for a scaled piece."""
    return max(2.0, min(7.0, 0.4 * min(dims)))


class Piece:
    w: float
    h: float

    def draw(self, c, x, y, gray):
        raise NotImplementedError


class BoxNet(Piece):
    """Glued box: [tab][back W][side D][front W][side D], lid+base on front."""

    def __init__(self, item, scale):
        self.item = item
        self.s = scale
        self.W = item["w"] / scale
        self.D = item["d"] / scale
        self.H = item["h"] / scale
        self.t = tab_size(self.W, self.D, self.H)
        self.w = self.t + 2 * self.W + 2 * self.D
        self.h = self.H + 2 * (self.D + self.t)

    def _art(self, c, art, x, y, w_real, h_real, face, gray):
        c.saveState()
        p = c.beginPath()
        p.rect(x * mm, y * mm, w_real / self.s * mm, h_real / self.s * mm)
        c.clipPath(p, stroke=0, fill=0)
        c.translate(x * mm, y * mm)
        c.scale(1.0 / self.s, 1.0 / self.s)
        art(c, w_real, h_real, face, gray)
        c.restoreState()

    def draw(self, c, x, y, gray):
        it, W, D, H, t = self.item, self.W, self.D, self.H, self.t
        art = it["art"]
        x0 = x + t
        yb = y + t + D  # bottom of the main band
        panels = [("back", W, it["w"]), ("side", D, it["d"]), ("front", W, it["w"]), ("side", D, it["d"])]
        px = x0
        for face, pw, real_w in panels:
            self._art(c, art, px, yb, real_w, it["h"], face, gray)
            px += pw
        fx = x0 + W + D  # front panel x
        # lid (top) and base (bottom) on the front panel
        self._art(c, art, fx, yb + H, it["w"], it["d"], "top", gray)
        self._art(c, art, fx, yb - D, it["w"], it["d"], "top", gray)
        # glue tabs
        pk.glue_area(c, x, yb + 0.6, t, H - 1.2, gray)  # side seam tab
        pk.glue_area(c, fx + 0.4, yb + H + D, W - 0.8, t, gray)  # lid tab
        pk.glue_area(c, fx + 0.4, y, W - 0.8, t, gray)  # base tab
        for sx in (x0 + W, x0 + 2 * W + D):  # dust tabs on both sides, top and bottom
            pk.glue_area(c, sx + 0.3, yb + H, D - 0.6, t, gray)
            pk.glue_area(c, sx + 0.3, yb - t, D - 0.6, t, gray)

        # ---- cut outline (polygon) ----
        pk.cut_style(c)
        chamfer = min(0.6, t * 0.3)
        pts = []
        # walk counter-clockwise starting bottom-left of seam tab
        pts += [(x, yb + chamfer * 2), (x + t, yb)]
        # bottom edge: back panel
        pts += [(x0 + W, yb)]
        # side 1 bottom dust tab
        sx = x0 + W
        pts += [(sx + chamfer, yb - t), (sx + D - chamfer, yb - t), (sx + D, yb)]
        # front base + base tab
        pts += [(fx, yb - D), (fx + chamfer, y), (fx + W - chamfer, y), (fx + W, yb - D), (fx + W, yb)]
        # side 2 bottom dust tab
        sx = fx + W
        pts += [(sx + chamfer, yb - t), (sx + D - chamfer, yb - t), (sx + D, yb)]
        # right edge
        pts += [(sx + D, yb + H)]
        # side 2 top dust tab
        pts += [(sx + D - chamfer, yb + H + t), (sx + chamfer, yb + H + t), (sx, yb + H)]
        # front lid + lid tab
        pts += [(fx + W, yb + H + D), (fx + W - chamfer, yb + H + D + t), (fx + chamfer, yb + H + D + t), (fx, yb + H + D), (fx, yb + H)]
        # side 1 top dust tab
        sx = x0 + W
        pts += [(sx + D, yb + H), (sx + D - chamfer, yb + H + t), (sx + chamfer, yb + H + t), (sx, yb + H)]
        # back top and seam tab top
        pts += [(x0, yb + H), (x, yb + H - chamfer * 2)]
        p = c.beginPath()
        p.moveTo(pts[0][0] * mm, pts[0][1] * mm)
        for px_, py_ in pts[1:]:
            p.lineTo(px_ * mm, py_ * mm)
        p.close()
        c.drawPath(p, stroke=1, fill=0)

        # ---- folds ----
        pk.fold_style(c)
        for fxl in (x0, x0 + W, x0 + W + D, x0 + 2 * W + D):
            pk.line(c, fxl, yb, fxl, yb + H)
        pk.line(c, fx, yb + H, fx + W, yb + H)
        pk.line(c, fx, yb, fx + W, yb)
        pk.line(c, fx, yb + H + D, fx + W, yb + H + D)
        pk.line(c, fx, yb - D, fx + W, yb - D)
        for sx in (x0 + W, fx + W):
            pk.line(c, sx, yb + H, sx + D, yb + H)
            pk.line(c, sx, yb, sx + D, yb)
        c.setDash()


class WrapLabel(Piece):
    """Cylinder label: circumference x height plus overlap glue strip."""

    def __init__(self, item, scale):
        self.item = item
        self.s = scale
        self.C = math.pi * item["dia"] / scale
        self.H = item["h"] / scale
        self.t = max(1.5, min(5.0, 0.15 * self.C))
        self.w = self.C + self.t
        self.h = self.H

    def draw(self, c, x, y, gray):
        it = self.item
        c.saveState()
        p = c.beginPath()
        p.rect(x * mm, y * mm, self.C * mm, self.H * mm)
        c.clipPath(p, stroke=0, fill=0)
        c.translate(x * mm, y * mm)
        c.scale(1.0 / self.s, 1.0 / self.s)
        it["art"](c, math.pi * it["dia"], it["h"], "wrap", gray)
        c.restoreState()
        pk.glue_area(c, x + self.C, y, self.t, self.H, gray)
        pk.cut_style(c)
        pk.rect(c, x, y, self.w, self.h)
        pk.fold_style(c)
        pk.line(c, x + self.C, y, x + self.C, y + self.H)
        c.setDash()


class Flat(Piece):
    """Flat printed piece (sign, price tag). Optional fold-back stand."""

    def __init__(self, item, scale):
        self.item = item
        self.s = scale
        self.W = item["w"] / scale
        self.H = item["h"] / scale
        self.double = item.get("double", False)  # fold in half: printed both sides
        self.w = self.W
        self.h = self.H * (2 if self.double else 1)

    def draw(self, c, x, y, gray):
        it = self.item
        faces = [(y, "front")] + ([(y + self.H, "back")] if self.double else [])
        for fy, face in faces:
            c.saveState()
            p = c.beginPath()
            p.rect(x * mm, fy * mm, self.W * mm, self.H * mm)
            c.clipPath(p, stroke=0, fill=0)
            if face == "back":  # rotate 180 so it reads correctly after folding
                c.translate((x + self.W) * mm, (fy + self.H) * mm)
                c.rotate(180)
            else:
                c.translate(x * mm, fy * mm)
            c.scale(1.0 / self.s, 1.0 / self.s)
            it["art"](c, it["w"], it["h"], "front", gray)
            c.restoreState()
        pk.cut_style(c)
        pk.rect(c, x, y, self.w, self.h)
        if self.double:
            pk.fold_style(c)
            pk.line(c, x, y + self.H, x + self.W, y + self.H)
            c.setDash()


KINDS = {"box": BoxNet, "wrap": WrapLabel, "flat": Flat}


# --------------------------------------------------------------------------
# Layout
# --------------------------------------------------------------------------

def pack(pieces, paper):
    """Shelf packing, tallest first. Returns list of pages of (piece, x, y)."""
    pw, ph = pk.page_size_mm(paper)
    usable_w = pw - 2 * MARGIN
    top = ph - MARGIN - HEADER_H
    bottom = MARGIN + CAL_H
    pieces = sorted(pieces, key=lambda p: (-p.h, -p.w))
    pages, cur, cx, cy, row_h = [], [], MARGIN, top, 0.0
    for pc in pieces:
        if pc.w > usable_w or pc.h > top - bottom:
            raise ValueError(f"piece too large for {paper}: {pc.item['name']} {pc.w:.1f}x{pc.h:.1f} mm")
        if cx + pc.w > MARGIN + usable_w + 1e-6:
            cx, cy, row_h = MARGIN, cy - row_h - GAP, 0.0
        if cy - pc.h < bottom:
            pages.append(cur)
            cur, cx, cy, row_h = [], MARGIN, top, 0.0
        cur.append((pc, cx, cy - pc.h))
        cx += pc.w + GAP
        row_h = max(row_h, pc.h)
    if cur:
        pages.append(cur)
    return pages


def final_dims(item, scale):
    if item["kind"] == "box":
        return f'{item["w"]/scale:.1f} x {item["d"]/scale:.1f} x {item["h"]/scale:.1f} mm (W x D x H)'
    if item["kind"] == "wrap":
        return f'{item["dia"]/scale:.1f} mm diameter x {item["h"]/scale:.1f} mm label'
    return f'{item["w"]/scale:.1f} x {item["h"]/scale:.1f} mm'


def inches(v_mm):
    return v_mm / 25.4


def instruction_page(c, st, scale, paper, gray, sku):
    pw, ph = pk.page_size_mm(paper)
    brand = st["palette"]
    c.setFillColor(gray(HexColor(brand["header"])))
    pk.rect(c, 0, ph - 34, pw, 34, stroke=0, fill=1)
    pk.text(c, MARGIN, ph - 18, st["title"], 20, "Serif-Bold", white)
    pk.text(c, MARGIN, ph - 27, f"Scale 1:{scale}  |  {st['scale_names'].get(str(scale), '')}  |  {paper} paper", 10, "Sans", white)
    y = ph - 46
    pk.text(c, MARGIN, y, "Before you print", 12, "Sans-Bold")
    y -= 6
    for line_ in [
        "1. Print at 100% / Actual size. Turn OFF 'Fit to page', 'Shrink oversized pages' and 'Scale to fit'.",
        "2. Measure the calibration bars at the bottom of every page: 50 mm and 2 in. If they differ, check printer settings.",
        "3. Best paper: 160 to 200 gsm (60 to 75 lb cover) matte card. Labels for cans: 80 to 120 gsm paper.",
        "4. Tools: craft knife and cutting mat, metal ruler, empty ballpoint pen for scoring, tacky glue or a glue stick.",
    ]:
        pk.text(c, MARGIN, y, line_, 8.2)
        y -= 5
    y -= 3
    pk.text(c, MARGIN, y, "Line key", 12, "Sans-Bold")
    y -= 8
    pk.cut_style(c)
    pk.line(c, MARGIN, y + 1.2, MARGIN + 14, y + 1.2)
    pk.text(c, MARGIN + 17, y, "Solid line: cut", 8.2)
    pk.fold_style(c)
    pk.line(c, MARGIN + 60, y + 1.2, MARGIN + 74, y + 1.2)
    c.setDash()
    pk.text(c, MARGIN + 77, y, "Dashed line: score and fold", 8.2)
    pk.glue_area(c, MARGIN + 130, y - 1, 12, 4.4, gray)
    pk.text(c, MARGIN + 145, y, "Gray hatched: glue", 8.2)
    y -= 10
    pk.text(c, MARGIN, y, "What is in this file (finished sizes at this scale)", 12, "Sans-Bold")
    y -= 7
    for it in st["items"]:
        q = it["qty"].get(str(scale), 0)
        if not q:
            continue
        d = final_dims(it, scale)
        pk.text(c, MARGIN, y, f"{it['name']}  x{q}", 8.6, "Sans-Bold")
        pk.text(c, MARGIN + 82, y, d, 8.2)
        y -= 4.8
    y -= 4
    pk.text(c, MARGIN, y, "Assembly", 12, "Sans-Bold")
    y -= 6
    notes = list(st["assembly"]["all"]) + list(st["assembly"].get(str(scale), []))
    for n in notes:
        pk.text(c, MARGIN, y, "- " + n, 8.2)
        y -= 4.8
    y -= 4
    pk.text(c, MARGIN, y, "License", 12, "Sans-Bold")
    y -= 6
    for n in st["licence"]:
        pk.text(c, MARGIN, y, n, 7.6)
        y -= 4.4
    pk.calibration_block(c, MARGIN, MARGIN)
    pk.footer(c, paper, f"{sku}  |  original artwork, fictional brands", "page 1")
    c.showPage()


def build(set_key, out_root, mono_too=True):
    st = SETS[set_key]
    results = []
    for scale in st["scales"]:
        for paper in ("A4", "Letter"):
            for mono in ([False, True] if mono_too and st.get("mono") else [False]):
                gray = pk.Gray(mono)
                sku = st["sku"]
                tag = f"1-{scale}_{paper}" + ("_BW" if mono else "")
                folder = os.path.join(out_root, sku, "customer-files")
                path = os.path.join(folder, f"{sku}_{tag}.pdf")
                c = pk.new_canvas(path, paper, f"{st['title']} 1:{scale} {paper}")
                instruction_page(c, st, scale, paper, gray, sku)
                pieces = []
                for it in st["items"]:
                    for _ in range(it["qty"].get(str(scale), 0)):
                        pieces.append(KINDS[it["kind"]](it, scale))
                pages = pack(pieces, paper)
                pw, ph = pk.page_size_mm(paper)
                for i, pg in enumerate(pages, start=2):
                    pk.text(c, MARGIN, ph - MARGIN - 6, f"{st['title']}  |  1:{scale}  |  {paper}", 9, "Sans-Bold")
                    pk.text(c, pw - MARGIN, ph - MARGIN - 6, "PRINT AT 100% / ACTUAL SIZE", 8, "Sans-Bold", anchor="right")
                    for pc, x, y in pg:
                        pc.draw(c, x, y, gray)
                    pk.calibration_block(c, MARGIN, MARGIN)
                    pk.footer(c, paper, f"{sku}  |  personal use license", f"page {i}")
                    c.showPage()
                c.save()
                results.append({"file": os.path.relpath(path), "scale": scale, "paper": paper,
                                "mono": mono, "pages": len(pages) + 1, "pieces": len(pieces)})
    return results


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--set", required=True, choices=sorted(SETS))
    ap.add_argument("--out", default="products")
    a = ap.parse_args()
    res = build(a.set, a.out)
    print(json.dumps(res, indent=1))


if __name__ == "__main__":
    main()
