"""Build printable kids' mystery game PDFs from a content module.

Usage: python3 scripts/mystery_build.py --game bday [--out products]

Outputs per paper (A4, Letter) and style (Color, InkSaver B&W):
  <SKU>_HostGuide_<paper>_<style>.pdf   host only (contains the solution)
  <SKU>_PrintPack_<paper>_<style>.pdf   case files, suspect/evidence/hint cards,
                                        envelope labels, certificates
"""
from __future__ import annotations

import argparse
import importlib
import json
import os
import sys

from reportlab.lib.colors import HexColor, white
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.platypus import Paragraph

sys.path.insert(0, os.path.dirname(__file__))
import printkit as pk  # noqa: E402

GAMES = {"bday": "mystery_content_bday", "snack": "mystery_content_snack"}
M = 14.0  # page margin mm


class Theme:
    def __init__(self, ink_saver: bool):
        self.ink_saver = ink_saver
        self.g = pk.Gray(ink_saver)
        self.primary = HexColor("#5B3FA0")
        self.accent = HexColor("#F2A541")
        self.soft = HexColor("#F3EEFB")
        self.round_cols = {1: HexColor("#E4572E"), 2: HexColor("#2E86AB"), 3: HexColor("#3BA55C")}

    def band(self, c, x, y, w, h, col, r=0):
        """Filled band in colour; outlined band in ink-saver mode."""
        c.saveState()
        if self.ink_saver:
            c.setStrokeColor(pk.INK)
            c.setLineWidth(1)
            c.setFillColor(white)
            c.roundRect(x * mm, y * mm, w * mm, h * mm, r * mm, stroke=1, fill=1)
        else:
            c.setFillColor(col)
            c.roundRect(x * mm, y * mm, w * mm, h * mm, r * mm, stroke=0, fill=1)
        c.restoreState()

    def on_band(self):
        return pk.INK if self.ink_saver else white


def para(c, txt, x, ytop, w, size=10, font="Sans", color=pk.INK, leading=None, align=0):
    st = ParagraphStyle("p", fontName=font, fontSize=size, leading=leading or size * 1.32,
                        textColor=color, alignment=align)
    p = Paragraph(txt.replace("\n", "<br/>"), st)
    _, h = p.wrap(w * mm, 1000 * mm)
    p.drawOn(c, x * mm, ytop * mm - h)
    return h / mm


# ------------------------------------------------------------------ drawings

def draw_person(c, th, x, y, s, look):
    """Simple original figure in a s x s mm box at (x, y)."""
    g = th.g
    def F(col):
        c.setFillColor(g(HexColor(col)))
    c.saveState()
    c.setStrokeColor(pk.INK)
    c.setLineWidth(0.8)
    if look.get("cat"):
        F(look.get("fur", "#7F8C8D"))
        c.ellipse((x + s * .2) * mm, (y + s * .16) * mm, (x + s * .72) * mm, (y + s * .48) * mm, stroke=1, fill=1)
        for lx in (0.28, 0.4, 0.54, 0.64):
            c.rect((x + s * lx) * mm, (y + s * .08) * mm, s * .06 * mm, s * .12 * mm, stroke=1, fill=1)
        c.circle((x + s * .72) * mm, (y + s * .56) * mm, s * .14 * mm, stroke=1, fill=1)
        for ex in (-1, 1):
            p = c.beginPath()
            p.moveTo((x + s * (.72 + ex * .12)) * mm, (y + s * .62) * mm)
            p.lineTo((x + s * (.72 + ex * .11)) * mm, (y + s * .8) * mm)
            p.lineTo((x + s * (.72 + ex * .02)) * mm, (y + s * .68) * mm)
            p.close()
            c.drawPath(p, stroke=1, fill=1)
        c.setLineWidth(1.6)
        p = c.beginPath()
        p.moveTo((x + s * .2) * mm, (y + s * .34) * mm)
        p.curveTo((x + s * .06) * mm, (y + s * .4) * mm, (x + s * .06) * mm, (y + s * .62) * mm, (x + s * .14) * mm, (y + s * .7) * mm)
        c.drawPath(p, stroke=1, fill=0)
        c.setLineWidth(0.8)
        F("#1C1C1C")
        c.circle((x + s * .67) * mm, (y + s * .58) * mm, s * .018 * mm, stroke=0, fill=1)
        c.circle((x + s * .77) * mm, (y + s * .58) * mm, s * .018 * mm, stroke=0, fill=1)
        F("#2E6DB4")
        c.rect((x + s * .62) * mm, (y + s * .43) * mm, s * .2 * mm, s * .035 * mm, stroke=0, fill=1)
        c.restoreState()
        return
    if look.get("dog"):
        F("#C8873F")
        c.ellipse((x + s * .18) * mm, (y + s * .22) * mm, (x + s * .78) * mm, (y + s * .52) * mm, stroke=1, fill=1)
        for lx in (0.26, 0.38, 0.6, 0.72):
            c.rect((x + s * lx) * mm, (y + s * .1) * mm, s * .07 * mm, s * .15 * mm, stroke=1, fill=1)
        F("#C8873F")
        c.circle((x + s * .74) * mm, (y + s * .6) * mm, s * .15 * mm, stroke=1, fill=1)
        F("#6B3E1E")
        c.ellipse((x + s * .78) * mm, (y + s * .42) * mm, (x + s * .9) * mm, (y + s * .66) * mm, stroke=1, fill=1)
        F("#FFFFFF")
        c.ellipse((x + s * .7) * mm, (y + s * .5) * mm, (x + s * .86) * mm, (y + s * .58) * mm, stroke=0, fill=1)
        F("#1C1C1C")
        c.circle((x + s * .7) * mm, (y + s * .64) * mm, s * .02 * mm, stroke=0, fill=1)
        c.circle((x + s * .86) * mm, (y + s * .56) * mm, s * .025 * mm, stroke=0, fill=1)
        F("#C0392B")
        c.rect((x + s * .62) * mm, (y + s * .47) * mm, s * .1 * mm, s * .04 * mm, stroke=0, fill=1)
        c.setLineWidth(1.6)
        c.line((x + s * .18) * mm, (y + s * .42) * mm, (x + s * .08) * mm, (y + s * .58) * mm)
        c.restoreState()
        return
    cx = x + s / 2
    extra = look.get("extra")
    # cape behind body
    if extra in ("silvercape", "streamercape"):
        F("#AEB6BF" if extra == "silvercape" else "#2E6DB4")
        p = c.beginPath()
        p.moveTo((cx - s * .16) * mm, (y + s * .66) * mm)
        p.lineTo((cx + s * .16) * mm, (y + s * .66) * mm)
        p.lineTo((cx + s * .26) * mm, (y + s * .14) * mm)
        p.lineTo((cx - s * .26) * mm, (y + s * .14) * mm)
        p.close()
        c.drawPath(p, stroke=1, fill=1)
        if extra == "streamercape":
            c.setStrokeColor(g(HexColor("#9CC3EE")))
            for k in range(-2, 3):
                c.line((cx + k * s * .045) * mm, (y + s * .64) * mm, (cx + k * s * .085) * mm, (y + s * .16) * mm)
            c.setStrokeColor(pk.INK)
    # legs / dress
    F(look["legs"])
    if extra == "dress":
        p = c.beginPath()
        p.moveTo((cx - s * .12) * mm, (y + s * .55) * mm)
        p.lineTo((cx + s * .12) * mm, (y + s * .55) * mm)
        p.lineTo((cx + s * .2) * mm, (y + s * .2) * mm)
        p.lineTo((cx - s * .2) * mm, (y + s * .2) * mm)
        p.close()
        c.drawPath(p, stroke=1, fill=1)
        F(look["skin"])
        c.rect((cx - s * .09) * mm, (y + s * .08) * mm, s * .05 * mm, s * .12 * mm, stroke=1, fill=1)
        c.rect((cx + s * .04) * mm, (y + s * .08) * mm, s * .05 * mm, s * .12 * mm, stroke=1, fill=1)
    else:
        c.rect((cx - s * .11) * mm, (y + s * .1) * mm, s * .09 * mm, s * .25 * mm, stroke=1, fill=1)
        c.rect((cx + s * .02) * mm, (y + s * .1) * mm, s * .09 * mm, s * .25 * mm, stroke=1, fill=1)
    # shoes / boots
    F(look["shoes"])
    bh = s * (.12 if extra in ("boots", "raincoat", "streamercape") else .04)
    c.rect((cx - s * .13) * mm, (y + s * .06) * mm, s * .12 * mm, bh * mm, stroke=1, fill=1)
    c.rect((cx + s * .01) * mm, (y + s * .06) * mm, s * .12 * mm, bh * mm, stroke=1, fill=1)
    # torso
    F(look["top"])
    c.roundRect((cx - s * .13) * mm, (y + s * .33) * mm, s * .26 * mm, s * .3 * mm, s * .04 * mm, stroke=1, fill=1)
    if extra == "boots":  # overall straps
        c.line((cx - s * .08) * mm, (y + s * .63) * mm, (cx - s * .08) * mm, (y + s * .5) * mm)
        c.line((cx + s * .08) * mm, (y + s * .63) * mm, (cx + s * .08) * mm, (y + s * .5) * mm)
    # head
    F(look["skin"])
    c.circle(cx * mm, (y + s * .76) * mm, s * .13 * mm, stroke=1, fill=1)
    F(look["hair"])
    p = c.beginPath()
    p.arc((cx - s * .14) * mm, (y + s * .7) * mm, (cx + s * .14) * mm, (y + s * .92) * mm, 0, 180)
    p.close()
    c.drawPath(p, stroke=1, fill=1)
    F("#1C1C1C")
    c.circle((cx - s * .045) * mm, (y + s * .75) * mm, s * .014 * mm, stroke=0, fill=1)
    c.circle((cx + s * .045) * mm, (y + s * .75) * mm, s * .014 * mm, stroke=0, fill=1)
    if look.get("glasses"):
        c.saveState()
        c.setStrokeColor(g(HexColor(look["glasses"])))
        c.setLineWidth(1.4)
        c.circle((cx - s * .05) * mm, (y + s * .75) * mm, s * .035 * mm, stroke=1, fill=0)
        c.circle((cx + s * .05) * mm, (y + s * .75) * mm, s * .035 * mm, stroke=1, fill=0)
        c.line((cx - s * .015) * mm, (y + s * .75) * mm, (cx + s * .015) * mm, (y + s * .75) * mm)
        c.restoreState()
    c.setLineWidth(0.7)
    c.arc((cx - s * .04) * mm, (y + s * .68) * mm, (cx + s * .04) * mm, (y + s * .72) * mm, 200, 140)
    c.restoreState()


ICON_GLYPH = {"boot": "BOOT", "streamer": "STREAMER", "paw": "PAWS", "cake": "PHOTO", "speech": "STATEMENT",
              "camera": "VIDEO", "ruler": "MEASURE", "dots": "TRAIL", "sign": "SIGN", "wrapper": "BIN",
              "list": "NOTE"}


# ------------------------------------------------------------------ pages

def header(c, th, paper, title, kicker):
    pw, ph = pk.page_size_mm(paper)
    th.band(c, M, ph - M - 18, pw - 2 * M, 18, th.primary, r=4)
    pk.text(c, M + 6, ph - M - 8.5, kicker.upper(), 8, "Sans-Bold", th.on_band() if th.ink_saver else th.accent)
    pk.text(c, M + 6, ph - M - 15, title, 14, "Serif-Bold", th.on_band())
    return ph - M - 26


def footer(c, paper, game, label, page):
    pk.footer(c, paper, f"{game.SKU}  |  {game.TITLE}  |  {label}", f"{page}")


def host_guide(path, paper, th, game):
    c = pk.new_canvas(path, paper, f"{game.TITLE} Host Guide")
    pw, ph = pk.page_size_mm(paper)
    W = pw - 2 * M
    n = 1
    # --- cover
    # inset, not full-bleed: home printers cannot print to the paper edge
    th.band(c, M / 2, ph * 0.45, pw - M, ph * 0.55 - M / 2, th.primary, r=4)
    pk.text(c, M, ph - 30, "HOST GUIDE  |  KEEP THIS SECRET", 9, "Sans-Bold", th.on_band() if th.ink_saver else th.accent)
    y = para(c, f"<b>{game.TITLE}</b>", M, ph - 38, W, 30, "Serif-Bold", th.on_band(), 34)
    para(c, game.SUBTITLE, M, ph - 42 - y, W, 13, "Sans", th.on_band())
    xs = M
    for s in game.SUSPECTS:
        draw_person(c, th, xs, ph * 0.47, 28, s["look"])
        xs += 30
    y = ph * 0.45 - 12
    para(c, game.TAGLINE, M, y, W, 12, "Serif", pk.INK)
    y -= 22
    for k, v in game.FACTS.items():
        pk.text(c, M, y, k.capitalize(), 10, "Sans-Bold")
        pk.text(c, M + 24, y, v, 10)
        y -= 7
    footer(c, paper, game, "Host guide", n)
    c.showPage()
    n += 1
    # --- what to print + setup
    y = header(c, th, paper, "Before the party", "Setup in about 15 minutes")
    blocks = [
        ("What to print (PrintPack file)",
         "Case file: 2 pages per detective or team (print one set each).<br/>"
         "Suspect cards: 2 pages, print one set for the table.<br/>"
         "Evidence cards: 2 pages, print one set and cut along the corner marks.<br/>"
         "Hint cards and envelope labels: 1 page.<br/>"
         "Detective certificates: 1 page (2 per page), as many as you need.<br/>"
         "Tip: 'Fit to page' is fine for this game. Nothing needs to be printed at true size."),
        ("Get ready",
         "1. Cut out the suspect, evidence and hint cards.<br/>"
         "2. Stick the three envelope labels on three envelopes (or folded paper).<br/>"
         "3. " + "; ".join(f"ROUND {r} envelope: " + ", ".join(e["id"] for e in game.EVIDENCE if e["round"] == r) for r in (1, 2, 3)) + ".<br/>"
         "4. Keep the three hint cards face down with you. Hand one over only after its minute.<br/>"
         "5. Lay the six suspect cards face up in the middle of the table.<br/>"
         "6. Give each detective or team a case file and a pencil. Have a timer ready."),
        ("Black and white or color?",
         "Both versions contain exactly the same clues. The ink-saver version uses outlines instead of "
         "colored backgrounds. Every color clue is also written in words, so nothing is lost in gray."),
    ]
    for t, body in blocks:
        pk.text(c, M, y, t, 12, "Sans-Bold", th.g(th.primary))
        y -= 3
        y -= para(c, body, M, y, W, 10.5) + 8
    footer(c, paper, game, "Host guide", n)
    c.showPage()
    n += 1
    # --- how to play
    y = header(c, th, paper, "How to run the game", "About 45 to 60 minutes")
    steps = [
        ("0:00", "Read the opening script (next page) out loud. Introduce the six suspects."),
        ("0:05", "Open ROUND 1: The Scene. Read each card aloud and pass it round. Detectives fill in the tracker."),
        ("0:15", "Hint 1 is available if detectives are stuck. Open ROUND 2: Witnesses and checks."),
        ("0:30", "Hint 2 is available. Open ROUND 3: The trail."),
        ("0:40", "Hint 3 is available. Detectives discuss and fill in their accusation form."),
        ("0:45", "Each detective or team reads their accusation aloud. Then read the solution."),
        ("0:55", "Award points and certificates. " + getattr(game, "FINALE_SHORT", "")),
    ]
    for t, s in steps:
        th.band(c, M, y - 6.5, 16, 8, th.accent, r=2)
        pk.text(c, M + 8, y - 4, t, 9, "Sans-Bold", pk.INK, "center")
        y -= para(c, s, M + 20, y, W - 20, 10.5) + 5
    y -= 4
    pk.text(c, M, y, "Timed hints", 12, "Sans-Bold", th.g(th.primary))
    y -= 3
    y -= para(c, "Hints are optional. Offer a hint only when the minute shown on the hint card has passed "
                 "and the detectives ask for one. Teams that solve the case without hints can earn a bonus point.",
              M, y, W, 10.5) + 6
    pk.text(c, M, y, "Making it easier or harder", 12, "Sans-Bold", th.g(th.primary))
    y -= 3
    para(c, "Easier (ages 8 to 9): open all hints at their times automatically and allow detectives to keep the "
            "evidence cards. Harder (ages 11 to 12): no hints, and each round's cards are read aloud only once.",
         M, y, W, 10.5)
    footer(c, paper, game, "Host guide", n)
    c.showPage()
    n += 1
    # --- script
    y = header(c, th, paper, "Opening script (read aloud)", "Host script")
    for line in game.INTRO_SCRIPT:
        y -= para(c, line, M + 4, y, W - 8, 12, "Serif") + 5
    y -= 4
    pk.text(c, M, y, f"The rooms at {game.PLACE_NAME}", 12, "Sans-Bold", th.g(th.primary))
    y -= 3
    for name, d in game.LOCATIONS:
        y -= para(c, f"<b>{name}:</b> {d}", M, y, W, 10.5) + 2.5
    footer(c, paper, game, "Host guide", n)
    c.showPage()
    n += 1
    # --- solution
    y = header(c, th, paper, "The solution (host only)", "Do not show the detectives")
    para(c, f"<b>WHO:</b> {game.SOLUTION['who']}", M, y, W, 14, "Sans-Bold", th.g(th.primary))
    y -= 9
    y -= para(c, f"<b>WHERE:</b> {game.SOLUTION['where']}", M, y, W, 11) + 4
    pk.text(c, M, y, "Read this out loud", 12, "Sans-Bold", th.g(th.primary))
    y -= 3
    y -= para(c, " ".join(game.SOLUTION["story"]), M, y, W, 10.5, "Serif") + 6
    pk.text(c, M, y, "Why it was not the others", 12, "Sans-Bold", th.g(th.primary))
    y -= 3
    for who, why in game.SOLUTION["eliminations"]:
        y -= para(c, f"<b>{who}:</b> {why}", M, y, W, 10) + 2
    y -= 5
    pk.text(c, M, y, "Scoring", 12, "Sans-Bold", th.g(th.primary))
    y -= 3
    y -= para(c, "<br/>".join(f"{a}: {b} point{'s' if b > 1 else ''}" for a, b in game.SCORING), M, y, W, 10) + 6
    para(c, game.FINALE, M, y, W, 10, "Sans", pk.GREY_MID)
    footer(c, paper, game, "Host guide", n)
    c.showPage()
    c.save()


def case_file(c, th, paper, game, n):
    pw, ph = pk.page_size_mm(paper)
    W = pw - 2 * M
    y = header(c, th, paper, "Detective case file", game.CASE_LABEL)
    pk.text(c, M, y, "Detective name: ______________________________", 11, "Sans")
    y -= 9
    y -= para(c, game.CASE_SUMMARY, M, y, W, 10.5) + 5
    # tracker grid
    pk.text(c, M, y, "Evidence tracker", 12, "Sans-Bold", th.g(th.primary))
    y -= 4
    pk.text(c, M, y - 3, "Tick if a clue fits the suspect, cross if it rules them out, leave blank if it says nothing about them.", 8.5, "Sans", pk.GREY_MID)
    y -= 7
    names = [s["name"] for s in game.SUSPECTS]
    rh = 7.4
    rows = [e["id"] + " " + e["title"] for e in game.EVIDENCE]
    label_w = 62
    cw = (W - label_w) / len(names)
    top = y
    th.band(c, M, top - rh, W, rh, th.soft)
    for i, nm in enumerate(names):
        pk.text(c, M + label_w + cw * i + cw / 2, top - rh + 2.3, nm, pk.fit_font(nm, "Sans-Bold", cw - 2, 8.5), "Sans-Bold", anchor="center")
    for r_i, r in enumerate(rows):
        yy = top - rh * (r_i + 2)
        pk.text(c, M + 1.5, yy + 2.3, r, pk.fit_font(r, "Sans", label_w - 3, 8), "Sans")
    c.setStrokeColor(pk.INK)
    c.setLineWidth(0.4)
    for r_i in range(len(rows) + 2):
        pk.line(c, M, top - rh * r_i, M + W, top - rh * r_i)
    pk.line(c, M, top, M, top - rh * (len(rows) + 1))
    for i in range(len(names) + 1):
        pk.line(c, M + label_w + cw * i, top, M + label_w + cw * i, top - rh * (len(rows) + 1))
    pk.line(c, M + W, top, M + W, top - rh * (len(rows) + 1))
    y = top - rh * (len(rows) + 1) - 8
    pk.text(c, M, y, "Notes", 12, "Sans-Bold", th.g(th.primary))
    c.setStrokeColor(pk.GREY_MID)
    for k in range(1, 6):
        if y - k * 8 < M + 12:
            break
        pk.line(c, M, y - k * 8, M + W, y - k * 8)
    footer(c, paper, game, "Case file page 1 of 2", n)
    c.showPage()
    # page 2: suspects summary + accusation
    y = header(c, th, paper, "Suspects and your accusation", "Case file page 2")
    colw = W / 3
    for i, s in enumerate(game.SUSPECTS):
        cx = M + (i % 3) * colw
        cy = y - (i // 3) * 44
        draw_person(c, th, cx, cy - 26, 24, s["look"])
        pk.text(c, cx + 26, cy - 6, s["name"], 10, "Sans-Bold")
        para(c, s["wearing"], cx + 26, cy - 8, colw - 28, 7.8, "Sans", pk.INK)
    y -= 90
    pk.text(c, M, y, "THE PLACE", 9, "Sans-Bold", th.g(th.primary))
    y -= 2
    for name, d in game.LOCATIONS:
        y -= para(c, f"<b>{name}:</b> {d}", M, y, W, 8.4) + 0.6
    y -= 4
    th.band(c, M, y - 92, W, 92, th.soft, r=4)
    yy = y - 8
    pk.text(c, M + 5, yy, "MY ACCUSATION", 13, "Sans-Bold", th.g(th.primary))
    yy -= 11
    for lab in game.ACCUSE:
        pk.text(c, M + 5, yy, lab, 10.5, "Sans-Bold")
        c.setStrokeColor(pk.INK)
        lx = max(M + 58, M + 5 + pdfmetrics.stringWidth(lab, "Sans-Bold", 10.5) / mm + 3)
        pk.line(c, lx, yy - 0.8, M + W - 6, yy - 0.8)
        yy -= 14
    footer(c, paper, game, "Case file page 2 of 2", n + 1)
    c.showPage()


def card_grid(paper, cw, ch, cols, rows):
    pw, ph = pk.page_size_mm(paper)
    gx = (pw - cols * cw) / (cols + 1)
    top = ph - M - 10
    gy = min(8.0, (top - M - 10 - rows * ch) / max(rows - 1, 1))
    slots = []
    for r in range(rows):
        for col in range(cols):
            slots.append((gx + col * (cw + gx), top - (r + 1) * ch - r * gy))
    return slots


def suspect_cards(c, th, paper, game, n):
    cw, ch = 88, 118
    slots = card_grid(paper, cw, ch, 2, 2)
    for i, s in enumerate(game.SUSPECTS):
        if i and i % 4 == 0:
            footer(c, paper, game, "Suspect cards", n)
            c.showPage()
            n += 1
        if i % 4 == 0:
            pk.text(c, M, pk.page_size_mm(paper)[1] - M - 2, "SUSPECT CARDS  |  cut along the corner marks", 9, "Sans-Bold")
        x, y = slots[i % 4]
        pk.card_crop_marks(c, x, y, cw, ch)
        c.setStrokeColor(pk.INK)
        c.setLineWidth(0.8)
        c.roundRect(x * mm, y * mm, cw * mm, ch * mm, 4 * mm, stroke=1, fill=0)
        th.band(c, x, y + ch - 14, cw, 14, th.primary, r=4)
        pk.text(c, x + 5, y + ch - 7, s["name"], 13, "Serif-Bold", th.on_band())
        pk.text(c, x + 5, y + ch - 11.8, s["role"], 8, "Sans", th.on_band())
        pk.text(c, x + cw - 5, y + ch - 9, s["id"], 9, "Sans-Bold", th.on_band(), "right")
        draw_person(c, th, x + cw / 2 - 22, y + ch - 62, 44, s["look"])
        yy = y + ch - 66
        for lab, key in (("Wearing", "wearing"), ("Says", "said"), ("Known fact", "fact")):
            pk.text(c, x + 5, yy, lab.upper(), 7, "Sans-Bold", th.g(th.primary))
            yy -= 1.5
            yy -= para(c, s[key], x + 5, yy, cw - 10, 8.6) + 2.5
    footer(c, paper, game, "Suspect cards", n)
    c.showPage()
    return n + 1


def evidence_cards(c, th, paper, game, n):
    cw, ch = 88, 58
    slots = card_grid(paper, cw, ch, 2, 4)
    for i, e in enumerate(game.EVIDENCE):
        if i and i % 8 == 0:
            footer(c, paper, game, "Evidence cards", n)
            c.showPage()
            n += 1
        if i % 8 == 0:
            pk.text(c, M, pk.page_size_mm(paper)[1] - M - 2, "EVIDENCE CARDS  |  sort into ROUND 1, 2 and 3 envelopes", 9, "Sans-Bold")
        x, y = slots[i % 8]
        col = th.round_cols[e["round"]]
        pk.card_crop_marks(c, x, y, cw, ch)
        c.setStrokeColor(pk.INK)
        c.setLineWidth(0.8)
        c.roundRect(x * mm, y * mm, cw * mm, ch * mm, 3 * mm, stroke=1, fill=0)
        th.band(c, x, y + ch - 11, cw, 11, col, r=3)
        pk.text(c, x + 4, y + ch - 7.4, f"{e['id']}  {e['title']}", pk.fit_font(f"{e['id']}  {e['title']}", "Sans-Bold", cw - 30, 10), "Sans-Bold", th.on_band())
        pk.text(c, x + cw - 4, y + ch - 7.4, f"ROUND {e['round']}", 7.5, "Sans-Bold", th.on_band(), "right")
        size = 8.6
        while size > 6.8:
            st = ParagraphStyle("t", fontName="Sans", fontSize=size, leading=size * 1.28)
            _, hh = Paragraph(e["text"].replace("\n", "<br/>"), st).wrap((cw - 8) * mm, 999 * mm)
            if hh / mm <= ch - 18:
                break
            size -= 0.2
        para(c, e["text"], x + 4, y + ch - 14, cw - 8, size)
        pk.text(c, x + cw - 4, y + 3, ICON_GLYPH.get(e["icon"], ""), 6.5, "Sans-Bold", pk.GREY_MID, "right")
    footer(c, paper, game, "Evidence cards", n)
    c.showPage()
    return n + 1


def hints_and_labels(c, th, paper, game, n):
    pw, ph = pk.page_size_mm(paper)
    W = pw - 2 * M
    pk.text(c, M, ph - M - 2, "HINT CARDS  |  the host keeps these and hands one over only after its minute", 9, "Sans-Bold")
    cw, ch = 54, 80
    gx = (pw - 3 * cw) / 4
    y = ph - M - 10 - ch
    for i, h in enumerate(game.HINTS):
        x = gx + i * (cw + gx)
        pk.card_crop_marks(c, x, y, cw, ch)
        c.setStrokeColor(pk.INK)
        c.setLineWidth(0.8)
        c.roundRect(x * mm, y * mm, cw * mm, ch * mm, 3 * mm, stroke=1, fill=0)
        th.band(c, x + 3, y + ch - 27, cw - 6, 24, th.accent, r=3)
        pk.text(c, x + cw / 2, y + ch - 12, f"HINT {i + 1}", 15, "Sans-Bold", pk.INK, "center")
        pk.text(c, x + cw / 2, y + ch - 22, f"not before minute {h['minute']}", 8.5, "Sans-Bold", pk.INK, "center")
        para(c, h["text"], x + 4, y + ch - 31, cw - 8, 8.8)
    y -= 16
    pk.text(c, M, y, "ENVELOPE LABELS  |  cut out and stick on three envelopes", 9, "Sans-Bold")
    y -= 6
    lw, lh = (W - 8) / 3, 34
    names = {1: "THE SCENE", 2: "WITNESSES AND CHECKS", 3: "THE TRAIL"}
    for r in (1, 2, 3):
        x = M + (r - 1) * (lw + 4)
        pk.cut_style(c)
        pk.rect(c, x, y - lh, lw, lh)
        th.band(c, x + 2.5, y - lh + 2.5, lw - 5, lh - 5, th.round_cols[r], r=3)
        pk.text(c, x + lw / 2, y - 14, f"ROUND {r}", 15, "Sans-Bold", th.on_band(), "center")
        pk.text(c, x + lw / 2, y - 22, names[r], pk.fit_font(names[r], "Sans-Bold", lw - 10, 9), "Sans-Bold", th.on_band(), "center")
        ids = ", ".join(e["id"] for e in game.EVIDENCE if e["round"] == r)
        pk.text(c, x + lw / 2, y - 28, ids, 7.5, "Sans", th.on_band(), "center")
    footer(c, paper, game, "Hints and labels", n)
    c.showPage()
    return n + 1


def certificates(c, th, paper, game, n):
    pw, ph = pk.page_size_mm(paper)
    W = pw - 2 * M
    hh = (ph - 2 * M - 14) / 2
    for k in range(2):
        y = M + 6 + k * (hh + 6)
        pk.cut_style(c)
        c.setDash(1 * mm, 1 * mm)
        pk.rect(c, M, y, W, hh)
        c.setDash()
        th.band(c, M + 5, y + 5, W - 10, hh - 10, th.soft, r=6)
        pk.text(c, pw / 2, y + hh - 26, "OFFICIAL DETECTIVE CERTIFICATE", 16, "Sans-Bold", th.g(th.primary), "center")
        pk.text(c, pw / 2, y + hh - 40, "This certifies that", 11, "Serif", pk.INK, "center")
        pk.line(c, pw / 2 - 55, y + hh - 58, pw / 2 + 55, y + hh - 58)
        pk.text(c, pw / 2, y + hh - 70, f"helped solve {game.TITLE.replace('The Case of the ', 'the case of the ')}", 10.5, "Serif", pk.INK, "center")
        pk.text(c, pw / 2, y + 18, "Case closed.   Date: ____________", 10, "Sans", pk.INK, "center")
    footer(c, paper, game, "Certificates", n)
    c.showPage()
    return n + 1


def print_pack(path, paper, th, game):
    c = pk.new_canvas(path, paper, f"{game.TITLE} Print Pack")
    n = 1
    case_file(c, th, paper, game, n)
    n += 2
    n = suspect_cards(c, th, paper, game, n)
    n = evidence_cards(c, th, paper, game, n)
    n = hints_and_labels(c, th, paper, game, n)
    n = certificates(c, th, paper, game, n)
    c.save()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--game", required=True, choices=sorted(GAMES))
    ap.add_argument("--out", default="products")
    a = ap.parse_args()
    game = importlib.import_module(GAMES[a.game])
    folder = os.path.join(a.out, game.SKU, "customer-files")
    out = []
    for paper in ("A4", "Letter"):
        for ink in (False, True):
            th = Theme(ink)
            style = "InkSaverBW" if ink else "Color"
            hp = os.path.join(folder, f"{game.SKU}_HostGuide_{paper}_{style}.pdf")
            pp = os.path.join(folder, f"{game.SKU}_PrintPack_{paper}_{style}.pdf")
            host_guide(hp, paper, th, game)
            print_pack(pp, paper, th, game)
            out += [hp, pp]
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
