"""Set definitions and original artwork for printable dollhouse miniatures.

All brands, names and artwork here are original and fictional.
Artwork functions draw in REAL-LIFE millimetres (the builder scales them).
Signature: art(c, w, h, face, gray) where face is one of
front, back, side, top, wrap.
"""
from __future__ import annotations

import math

from reportlab.lib.colors import HexColor
from reportlab.lib.units import mm

import printkit as pk


def H(x):
    return HexColor(x)


# ------------------------------------------------------------------ helpers

def box(c, g, x, y, w, h, col, r=0):
    c.setFillColor(g(H(col)))
    if r:
        c.roundRect(x * mm, y * mm, w * mm, h * mm, r * mm, stroke=0, fill=1)
    else:
        c.rect(x * mm, y * mm, w * mm, h * mm, stroke=0, fill=1)


def circ(c, g, x, y, r, col):
    c.setFillColor(g(H(col)))
    c.circle(x * mm, y * mm, r * mm, stroke=0, fill=1)


def label(c, g, x, y, s, max_w, size, col, font="Sans-Bold", anchor="center"):
    size = pk.fit_font(s, font, max_w, size, 1)
    c.setFillColor(g(H(col)))
    c.setFont(font, size)
    fn = {"center": c.drawCentredString, "left": c.drawString, "right": c.drawRightString}[anchor]
    fn(x * mm, y * mm, s)


def poly(c, g, pts, col):
    c.setFillColor(g(H(col)))
    p = c.beginPath()
    p.moveTo(pts[0][0] * mm, pts[0][1] * mm)
    for x, y in pts[1:]:
        p.lineTo(x * mm, y * mm)
    p.close()
    c.drawPath(p, stroke=0, fill=1)


def back_panel(c, g, w, h, bg, ink, brand):
    box(c, g, 0, 0, w, h, bg)
    label(c, g, w / 2, h - 0.12 * h, brand, w * 0.8, h * 0.07 * 2.6, "#3A3A3A")
    # decorative "nutrition" table (unreadable at scale by design)
    tx, tw = w * 0.12, w * 0.76
    ty = h * 0.25
    th = h * 0.45
    c.setStrokeColor(g(H("#6B6B6B")))
    c.setLineWidth(max(0.6, w * 0.01) * mm / mm)
    c.rect(tx * mm, ty * mm, tw * mm, th * mm, stroke=1, fill=0)
    rows = 9
    for i in range(1, rows):
        yy = ty + th * i / rows
        c.line(tx * mm, yy * mm, (tx + tw) * mm, yy * mm)
    # barcode
    bx, by, bw, bh = w * 0.55, h * 0.05, w * 0.33, h * 0.12
    box(c, g, bx, by, bw, bh, "#FFFFFF")
    n = 28
    for i in range(n):
        if (i * 7) % 5 in (0, 2):
            box(c, g, bx + bw * (0.06 + 0.88 * i / n), by + bh * 0.12, bw * 0.02, bh * 0.76, "#1C1C1C")


def side_panel(c, g, w, h, bg, ink, brand):
    box(c, g, 0, 0, w, h, bg)
    c.saveState()
    c.translate(w / 2 * mm, h / 2 * mm)
    c.rotate(90)
    label(c, g, 0, -w * 0.18, brand, h * 0.8, w * 0.55 * 2.83, ink)
    c.restoreState()


def make_box_art(brand, bg, ink, back_bg, front_fn):
    def art(c, w, h, face, g):
        if face == "front":
            front_fn(c, g, w, h)
        elif face == "back":
            back_panel(c, g, w, h, back_bg, ink, brand)
        elif face == "side":
            side_panel(c, g, w, h, bg, ink, brand)
        else:
            box(c, g, 0, 0, w, h, bg)
    return art


# ------------------------------------------------------------------ grocery fronts

def front_oats(c, g, w, h):
    box(c, g, 0, 0, w, h, "#F4C542")
    cx, cy = w / 2, h * 0.62
    for i in range(16):
        a = 2 * math.pi * i / 16
        poly(c, g, [(cx + math.cos(a - 0.08) * w * 0.2, cy + math.sin(a - 0.08) * w * 0.2),
                    (cx + math.cos(a) * w * 0.36, cy + math.sin(a) * w * 0.36),
                    (cx + math.cos(a + 0.08) * w * 0.2, cy + math.sin(a + 0.08) * w * 0.2)], "#F29E38")
    circ(c, g, cx, cy, w * 0.2, "#F7DC6F")
    # bowl
    poly(c, g, [(w * 0.18, h * 0.3), (w * 0.82, h * 0.3), (w * 0.68, h * 0.16), (w * 0.32, h * 0.16)], "#3E7CB1")
    for i in range(7):
        circ(c, g, w * (0.24 + i * 0.087), h * 0.31, w * 0.05, "#E8C07D")
    box(c, g, 0, h * 0.86, w, h * 0.14, "#C0392B")
    label(c, g, w / 2, h * 0.9, "SUNNY OATS", w * 0.9, 40, "#FFFFFF")
    label(c, g, w / 2, h * 0.06, "whole grain breakfast", w * 0.8, 16, "#7A4A12", "Sans")


def front_crackers(c, g, w, h):
    box(c, g, 0, 0, w, h, "#B8322A")
    for row in range(2):
        for col in range(3):
            x = w * (0.12 + col * 0.27)
            y = h * (0.12 + row * 0.3)
            box(c, g, x, y, w * 0.22, h * 0.25, "#E5B567", r=w * 0.015)
            for dx in range(3):
                for dy in range(3):
                    circ(c, g, x + w * 0.22 * (0.25 + dx * 0.25), y + h * 0.25 * (0.25 + dy * 0.25), w * 0.006, "#A8743A")
    label(c, g, w / 2, h * 0.8, "PIP & CO", w * 0.8, 38, "#FFFFFF")
    label(c, g, w / 2, h * 0.71, "sea salt crackers", w * 0.7, 18, "#FCE3B0", "Sans")


def front_milk(c, g, w, h):
    box(c, g, 0, 0, w, h, "#FFFFFF")
    poly(c, g, [(0, 0), (w, 0), (w, h * 0.3), (w * 0.6, h * 0.38), (w * 0.2, h * 0.3), (0, h * 0.34)], "#6DB56D")
    poly(c, g, [(0, 0), (w, 0), (w, h * 0.18), (w * 0.4, h * 0.25), (0, h * 0.2)], "#3F8F4F")
    circ(c, g, w * 0.75, h * 0.6, w * 0.12, "#F4D03F")
    box(c, g, 0, h * 0.75, w, h * 0.25, "#2E6DB4")
    label(c, g, w / 2, h * 0.86, "MEADOW", w * 0.85, 30, "#FFFFFF")
    label(c, g, w / 2, h * 0.78, "MILK", w * 0.6, 22, "#FFFFFF")
    label(c, g, w / 2, h * 0.47, "fresh whole milk", w * 0.8, 14, "#2E6DB4", "Sans")


def front_pasta(c, g, w, h):
    box(c, g, 0, 0, w, h, "#1F4E79")
    box(c, g, w * 0.15, h * 0.18, w * 0.7, h * 0.55, "#F3D9A4", r=w * 0.1)
    for i in range(9):
        x = w * (0.22 + i * 0.07)
        box(c, g, x, h * 0.2, w * 0.018, h * 0.51, "#D9A441")
    label(c, g, w / 2, h * 0.86, "NONNA BELLA", w * 0.9, 20, "#FFFFFF")
    label(c, g, w / 2, h * 0.79, "spaghetti", w * 0.8, 14, "#F3D9A4", "Sans")
    label(c, g, w / 2, h * 0.07, "500 g", w * 0.5, 12, "#FFFFFF", "Sans")


def front_tea(c, g, w, h):
    box(c, g, 0, 0, w, h, "#2F6B4F")
    poly(c, g, [(w * 0.62, h * 0.2), (w * 0.9, h * 0.5), (w * 0.62, h * 0.8), (w * 0.5, h * 0.5)], "#8BC48A")
    box(c, g, w * 0.69, h * 0.24, w * 0.01, h * 0.52, "#2F6B4F")
    label(c, g, w * 0.08, h * 0.55, "MORNING", w * 0.5, 22, "#FFFFFF", anchor="left")
    label(c, g, w * 0.08, h * 0.38, "garden tea", w * 0.45, 14, "#D6EBC9", "Sans", anchor="left")
    label(c, g, w * 0.08, h * 0.12, "20 tea bags", w * 0.45, 10, "#D6EBC9", "Sans", anchor="left")


# ------------------------------------------------------------------ wrap labels

def wrap_soup(c, w, h, face, g):
    box(c, g, 0, 0, w, h, "#C62828")
    box(c, g, 0, 0, w, h * 0.42, "#FFFFFF")
    for k in range(2):
        cx = w * (0.25 + 0.5 * k)
        label(c, g, cx, h * 0.72, "PIP & CO", w * 0.35, 18, "#FFFFFF")
        circ(c, g, cx, h * 0.24, h * 0.12, "#E53935")
        poly(c, g, [(cx - h * 0.04, h * 0.35), (cx, h * 0.39), (cx + h * 0.04, h * 0.35)], "#2E7D32")
        label(c, g, cx, h * 0.53, "tomato soup", w * 0.35, 10, "#FFE0B2", "Sans")
    box(c, g, 0, h * 0.94, w, h * 0.06, "#B8860B")
    box(c, g, 0, 0, w, h * 0.04, "#B8860B")


def wrap_peaches(c, w, h, face, g):
    box(c, g, 0, 0, w, h, "#FFE6C7")
    box(c, g, 0, h * 0.8, w, h * 0.2, "#E67E22")
    for k in range(2):
        cx = w * (0.25 + 0.5 * k)
        circ(c, g, cx - h * 0.06, h * 0.4, h * 0.17, "#F5A65B")
        circ(c, g, cx + h * 0.06, h * 0.38, h * 0.15, "#F08A4B")
        poly(c, g, [(cx, h * 0.56), (cx + h * 0.12, h * 0.66), (cx + h * 0.03, h * 0.58)], "#5E9E43")
        label(c, g, cx, h * 0.86, "GOLDEN GROVE", w * 0.4, 14, "#FFFFFF")
        label(c, g, cx, h * 0.1, "peach halves", w * 0.3, 10, "#B25A1B", "Sans")


def wrap_jam(c, w, h, face, g):
    box(c, g, 0, 0, w, h, "#FFFFFF")
    step = h / 6
    i = 0
    x = 0.0
    while x < w:
        if i % 2 == 0:
            box(c, g, x, 0, step, h, "#F7C6C7")
        x += step
        i += 1
    for j in range(6):
        if j % 2 == 0:
            box(c, g, 0, j * step, w, step, "#F7C6C7")
    for k in range(2):
        cx = w * (0.25 + 0.5 * k)
        box(c, g, cx - w * 0.15, h * 0.22, w * 0.3, h * 0.56, "#FFFFFF", r=h * 0.1)
        label(c, g, cx, h * 0.55, "Strawberry", w * 0.26, 11, "#B03A48", "Serif-Bold")
        label(c, g, cx, h * 0.33, "Hilltop Farm", w * 0.24, 8, "#555555", "Serif")


# ------------------------------------------------------------------ flats

def flat_sign(c, w, h, face, g):
    box(c, g, 0, 0, w, h, "#2F4F4F")
    box(c, g, w * 0.02, h * 0.08, w * 0.96, h * 0.84, "#FDF6E3", r=h * 0.08)
    label(c, g, w / 2, h * 0.42, "The Corner Grocer", w * 0.8, 70, "#2F4F4F", "Serif-Bold")
    label(c, g, w / 2, h * 0.18, "fresh food  |  friendly faces  |  est. 1952", w * 0.8, 22, "#8B5A2B", "Serif")


def flat_specials(c, w, h, face, g):
    box(c, g, 0, 0, w, h, "#8B5A2B")
    box(c, g, w * 0.06, h * 0.05, w * 0.88, h * 0.9, "#22313A")
    label(c, g, w / 2, h * 0.8, "TODAY'S SPECIALS", w * 0.8, 30, "#FFFFFF")
    items = ["Sunny Oats 2 for 1", "Fresh Bread  2.50", "Peaches  1.20", "Meadow Milk  0.99"]
    for i, s in enumerate(items):
        label(c, g, w / 2, h * (0.62 - i * 0.13), s, w * 0.75, 20, "#F6E7C1", "Serif")


def flat_tags(c, w, h, face, g):
    box(c, g, 0, 0, w, h, "#FFFFFF")
    labels = ["0.99", "1.20", "2.50", "SALE", "3.10", "NEW"]
    tw = w / 6
    cols = ["#F4C542", "#E67E22", "#C62828", "#2E6DB4", "#2F6B4F", "#B03A48"]
    for i, s in enumerate(labels):
        box(c, g, i * tw + tw * 0.05, h * 0.08, tw * 0.9, h * 0.84, cols[i], r=h * 0.08)
        label(c, g, i * tw + tw / 2, h * 0.36, s, tw * 0.8, 16, "#FFFFFF")


GROCERY = {
    "sku": "MINI-GROC-01",
    "title": "The Corner Grocer: Pantry Set",
    "mono": False,
    "scales": [6, 12, 16, 24],
    "rejected_scales": {"48": "packaging text and glue tabs fall below about 1.5 mm; not practical to cut or read"},
    "scale_names": {"6": "playscale, 11.5 to 12 in fashion dolls", "12": "1 in = 1 ft, classic dollhouse",
                    "16": "3/4 in = 1 ft, many play dollhouses", "24": "half scale, 1/2 in = 1 ft"},
    "palette": {"header": "#2F4F4F"},
    "items": [
        {"name": "Sunny Oats cereal box", "kind": "box", "w": 195, "d": 70, "h": 290,
         "art": make_box_art("SUNNY OATS", "#F4C542", "#7A4A12", "#FFF4D6", front_oats),
         "qty": {"6": 2, "12": 3, "16": 3, "24": 4}},
        {"name": "Pip & Co crackers box", "kind": "box", "w": 200, "d": 60, "h": 150,
         "art": make_box_art("PIP & CO", "#B8322A", "#FFFFFF", "#FCE3B0", front_crackers),
         "qty": {"6": 2, "12": 3, "16": 3, "24": 4}},
        {"name": "Meadow Milk carton", "kind": "box", "w": 95, "d": 95, "h": 245,
         "art": make_box_art("MEADOW MILK", "#2E6DB4", "#FFFFFF", "#EAF2FB", front_milk),
         "qty": {"6": 2, "12": 4, "16": 4, "24": 6}},
        {"name": "Nonna Bella spaghetti box", "kind": "box", "w": 70, "d": 30, "h": 260,
         "art": make_box_art("NONNA BELLA", "#1F4E79", "#FFFFFF", "#F3D9A4", front_pasta),
         "qty": {"6": 2, "12": 4, "16": 4, "24": 6}},
        {"name": "Morning Garden tea box", "kind": "box", "w": 130, "d": 70, "h": 75,
         "art": make_box_art("MORNING TEA", "#2F6B4F", "#FFFFFF", "#D6EBC9", front_tea),
         "qty": {"6": 2, "12": 4, "16": 4, "24": 6}},
        {"name": "Tomato soup can label", "kind": "wrap", "dia": 74, "h": 100, "art": wrap_soup,
         "qty": {"6": 3, "12": 6, "16": 6, "24": 10}},
        {"name": "Peach halves can label", "kind": "wrap", "dia": 87, "h": 105, "art": wrap_peaches,
         "qty": {"6": 3, "12": 6, "16": 6, "24": 10}},
        {"name": "Strawberry jam jar label", "kind": "wrap", "dia": 70, "h": 45, "art": wrap_jam,
         "qty": {"6": 3, "12": 6, "16": 6, "24": 10}},
        {"name": "Shop sign (fold, two-sided)", "kind": "flat", "w": 600, "h": 150, "double": True,
         "art": flat_sign, "qty": {"6": 1, "12": 1, "16": 1, "24": 2}},
        {"name": "Specials chalkboard (fold, two-sided)", "kind": "flat", "w": 300, "h": 400, "double": True,
         "art": flat_specials, "qty": {"6": 1, "12": 1, "16": 1, "24": 2}},
        {"name": "Shelf price tag strip", "kind": "flat", "w": 240, "h": 30, "art": flat_tags,
         "qty": {"6": 2, "12": 3, "16": 3, "24": 4}},
    ],
    "assembly": {
        "all": [
            "Score every dashed line with an empty pen against a ruler BEFORE cutting the piece out.",
            "Boxes: fold all panels inward, glue the side seam tab first, then the dust tabs, then the lid and base.",
            "Can and jar labels wrap around a dowel, straw or rolled card tube. Glue the grey strip under the far edge.",
            "Two-sided signs: fold on the dashed line, glue back to back, then trim the edges together.",
        ],
        "6": ["Can cores at 1:6: about 12 mm (cans) and 12 mm (jam). A marker cap or rolled card tube works."],
        "16": ["Can cores at 1:16: about 4.5 to 5.5 mm. A thin dowel, skewer bundle or rolled card works."],
        "12": ["Can cores at 1:12: about 6 to 7 mm. Use a 6 mm dowel or a rolled strip of card."],
        "24": ["1:24 boxes are tiny: for crisp corners, wrap the net around a small block cut from foam board.",
               "Can cores at 1:24: about 3 mm. A cocktail stick or a tight roll of paper works."],
    },
    "licence": [
        "Personal use: print as many copies as you like for your own dollhouses and play.",
        "Not permitted: reselling or sharing the digital file, or selling printed copies.",
        "All brand names and artwork are fictional and original to this set.",
    ],
}

SETS = {"grocery": GROCERY}
