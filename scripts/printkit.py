"""Shared print layout helpers for the studio.

All geometry is in millimetres. reportlab's native unit is the PostScript
point (1 pt = 1/72 in), so every public helper takes mm and converts.

Conventions used across every product line:
  * Cut lines: solid, 0.35 pt, soft black.
  * Valley folds: dashed (2 mm on, 1.2 mm off), 0.35 pt.
  * Glue areas: light grey fill with diagonal hatching and the word GLUE
    when the tab is large enough to hold legible text.
  * Calibration: a 50 mm bar and a 2 in bar on every true-size page, plus a
    printed instruction to print at 100% / Actual size.
"""
from __future__ import annotations

import os
from dataclasses import dataclass

from reportlab.lib.colors import Color, HexColor, black, white
from reportlab.lib.pagesizes import A4, letter
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas as rl_canvas

FONT_DIR = "/usr/share/fonts/truetype/dejavu"
_FONTS_REGISTERED = False

PAPERS = {"A4": A4, "Letter": letter}

INK = HexColor("#1C1C1C")
GREY_GLUE = HexColor("#D9D9D9")
GREY_MID = HexColor("#8A8A8A")


def register_fonts() -> None:
    """Register embeddable fonts (DejaVu, Bitstream Vera licence, free to embed)."""
    global _FONTS_REGISTERED
    if _FONTS_REGISTERED:
        return
    pdfmetrics.registerFont(TTFont("Sans", os.path.join(FONT_DIR, "DejaVuSans.ttf")))
    pdfmetrics.registerFont(TTFont("Sans-Bold", os.path.join(FONT_DIR, "DejaVuSans-Bold.ttf")))
    pdfmetrics.registerFont(TTFont("Serif", os.path.join(FONT_DIR, "DejaVuSerif.ttf")))
    pdfmetrics.registerFont(TTFont("Serif-Bold", os.path.join(FONT_DIR, "DejaVuSerif-Bold.ttf")))
    pdfmetrics.registerFont(TTFont("Mono", os.path.join(FONT_DIR, "DejaVuSansMono.ttf")))
    _FONTS_REGISTERED = True


def new_canvas(path: str, paper: str, title: str, author: str = "First Dollar") -> rl_canvas.Canvas:
    register_fonts()
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    c = rl_canvas.Canvas(path, pagesize=PAPERS[paper], pageCompression=1,
                         initialFontName="Sans", initialFontSize=10)
    c.setTitle(title)
    c.setAuthor(author)
    c.setCreator("scripts printkit (reportlab)")
    # Ask PDF viewers not to shrink-to-fit when printing (honoured by Acrobat/Preview).
    try:
        c.setViewerPreference("PrintScaling", "None")
    except Exception:  # older reportlab
        pass
    return c


def page_size_mm(paper: str) -> tuple[float, float]:
    w, h = PAPERS[paper]
    return w / mm, h / mm


@dataclass
class Gray:
    """Wrap colours so a whole document can be forced to greyscale."""

    enabled: bool = False

    def __call__(self, col):
        if not self.enabled or col is None:
            return col
        r, g, b = col.red, col.green, col.blue
        y = 0.299 * r + 0.587 * g + 0.114 * b
        return Color(y, y, y, alpha=getattr(col, "alpha", 1))


# --------------------------------------------------------------------------
# Primitive drawing in mm
# --------------------------------------------------------------------------

def rect(c, x, y, w, h, stroke=1, fill=0):
    c.rect(x * mm, y * mm, w * mm, h * mm, stroke=stroke, fill=fill)


def line(c, x1, y1, x2, y2):
    c.line(x1 * mm, y1 * mm, x2 * mm, y2 * mm)


def cut_style(c):
    c.setDash()
    c.setLineWidth(0.35)
    c.setStrokeColor(INK)


def fold_style(c):
    c.setDash(2 * mm, 1.2 * mm)
    c.setLineWidth(0.35)
    c.setStrokeColor(INK)


def text(c, x, y, s, size=8, font="Sans", color=INK, anchor="left"):
    c.setFillColor(color)
    c.setFont(font, size)
    if anchor == "left":
        c.drawString(x * mm, y * mm, s)
    elif anchor == "center":
        c.drawCentredString(x * mm, y * mm, s)
    else:
        c.drawRightString(x * mm, y * mm, s)


def fit_font(s: str, font: str, max_w_mm: float, max_size: float, min_size: float = 1.5) -> float:
    """Largest font size (pt) <= max_size whose string width fits max_w_mm."""
    register_fonts()
    size = max_size
    while size > min_size and pdfmetrics.stringWidth(s, font, size) > max_w_mm * mm:
        size -= 0.1
    return max(size, min_size)


def glue_area(c, x, y, w, h, gray: Gray | None = None):
    """Hatched glue area. Outline is drawn by the caller as cut line."""
    g = gray or Gray()
    c.saveState()
    c.setFillColor(g(GREY_GLUE))
    c.setStrokeColor(g(GREY_GLUE))
    rect(c, x, y, w, h, stroke=0, fill=1)
    p = c.beginPath()
    p.rect(x * mm, y * mm, w * mm, h * mm)
    c.clipPath(p, stroke=0, fill=0)
    c.setStrokeColor(GREY_MID)
    c.setLineWidth(0.2)
    step = 1.6
    k = -h
    while k < w:
        line(c, x + k, y, x + k + h, y + h)
        k += step
    c.restoreState()
    if w >= 7 and h >= 2.6:
        size = fit_font("GLUE", "Sans-Bold", w * 0.8, min(h * 2.0, 6), 3)
        text(c, x + w / 2, y + h / 2 - size * 0.12, "GLUE", size, "Sans-Bold", GREY_MID, "center")


def calibration_block(c, x, y):
    """Draws a 50 mm bar and a 2 in bar with labels. Occupies about 62 x 16 mm.

    Returns (width_mm, height_mm) occupied.
    """
    c.saveState()
    c.setDash()
    c.setStrokeColor(INK)
    c.setFillColor(INK)
    c.setLineWidth(0.5)
    # 50 mm bar with 10 mm ticks
    line(c, x, y + 11, x + 50, y + 11)
    for i in range(6):
        tick = 2.4 if i in (0, 5) else 1.4
        line(c, x + i * 10, y + 11, x + i * 10, y + 11 + tick)
    text(c, x + 51.5, y + 10.4, "50 mm", 6, "Sans-Bold")
    # 2 inch bar with 1/2 in ticks
    inch = 25.4
    line(c, x, y + 4, x + 2 * inch, y + 4)
    for i in range(5):
        tick = 2.4 if i in (0, 4) else 1.4
        line(c, x + i * inch / 2, y + 4, x + i * inch / 2, y + 4 + tick)
    text(c, x + 2 * inch + 1.5, y + 3.4, "2 in", 6, "Sans-Bold")
    text(c, x, y, "Check: bars must measure exactly 50 mm and 2 in. Print at 100% / Actual size.", 5.2)
    c.restoreState()
    return 62, 16


def card_crop_marks(c, x, y, w, h, length=3.0, gap=1.0):
    """Corner crop marks outside a card so cutting lines stay invisible."""
    c.saveState()
    c.setDash()
    c.setLineWidth(0.3)
    c.setStrokeColor(GREY_MID)
    for cx, cy, dx, dy in ((x, y, -1, -1), (x + w, y, 1, -1), (x, y + h, -1, 1), (x + w, y + h, 1, 1)):
        line(c, cx + dx * gap, cy, cx + dx * (gap + length), cy)
        line(c, cx, cy + dy * gap, cx, cy + dy * (gap + length))
    c.restoreState()


def footer(c, paper, left: str, right: str, color=GREY_MID):
    pw, _ = page_size_mm(paper)
    text(c, 12, 7, left, 6.5, "Sans", color)
    text(c, pw - 12, 7, right, 6.5, "Sans", color, "right")


def white_color():
    return white


def black_color():
    return black
