"""Storefront images built from REAL renders of the customer PDFs.

Usage: python3 scripts/make_storefront.py <SKU>
Writes products/<SKU>/storefront/*.png (2400x1800, 4:3, sRGB) plus
a 375 px wide mobile check image. Images are labelled "Digital file preview"
so they are never mistaken for photos of a physical product.
"""
from __future__ import annotations

import glob
import os
import subprocess
import sys
import tempfile

from PIL import Image, ImageDraw, ImageFilter, ImageFont

FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
FONTB = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SERIFB = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
W, H = 2400, 1800

CONFIG = {
    "MYST-BDAY-01": {
        "bg": "#5B3FA0", "fg": "#FFFFFF", "accent": "#F2A541",
        "title": "The Case of the Vanishing Birthday Cake",
        "sub": "Printable detective party game, ages 8-12",
        "badges": ["2 to 8 detectives", "15-minute setup", "Color + ink-saver B&W", "A4 + US Letter"],
        "hero_pdf": "MYST-BDAY-01_PrintPack_Letter_Color.pdf", "hero_pages": [3, 5, 1, 7],
        "slides": [
            ("What you get", "MYST-BDAY-01_PrintPack_Letter_Color.pdf", [1, 2, 3, 4, 5, 6, 7, 8],
             "Host guide (5 pages) + print pack (8 pages)"),
            ("Ink-saver black and white version included", "MYST-BDAY-01_PrintPack_Letter_InkSaverBW.pdf", [3, 5, 7],
             "Same clues, outlines instead of color fills"),
        ],
    },
    "MYST-FAM-01": {
        "bg": "#1F3A5F", "fg": "#FFFFFF", "accent": "#F2C230",
        "title": "The Midnight Snack Mystery",
        "sub": "Family night detective game, ages 8-12",
        "badges": ["2 to 8 detectives", "No acting, no scary stuff", "Color + ink-saver B&W", "A4 + US Letter"],
        "hero_pdf": "MYST-FAM-01_PrintPack_Letter_Color.pdf", "hero_pages": [3, 5, 2],
        "slides": [
            ("What you get", "MYST-FAM-01_PrintPack_Letter_Color.pdf", [1, 2, 3, 4, 5, 6, 7, 8],
             "Host guide (5 pages) + print pack (8 pages)"),
            ("Ink-saver black and white version included", "MYST-FAM-01_PrintPack_Letter_InkSaverBW.pdf", [2, 3, 5],
             "Same clues, outlines instead of color fills"),
        ],
    },
    "MINI-GROC-01": {
        "bg": "#2F4F4F", "fg": "#FFFFFF", "accent": "#F4C542",
        "title": "The Corner Grocer: Pantry Set",
        "sub": "Printable dollhouse miniatures  |  1:6  1:12  1:16  1:24",
        "badges": ["4 scales, separate true-size PDFs", "A4 + US Letter", "Calibration ruler on every page",
                   "Original fictional brands"],
        "hero_pdf": "MINI-GROC-01_1-6_Letter.pdf", "hero_pages": [2, 3, 1],
        "slides": [
            ("Every scale is its own true-size file", "MINI-GROC-01_1-12_Letter.pdf", [1, 2],
             "Finished sizes listed for every item"),
            ("1:24 half scale sheet", "MINI-GROC-01_1-24_Letter.pdf", [2], "Cut, fold and glue lines on every piece"),
        ],
    },
}


def render(pdf, pages, tmp, dpi=110):
    out = []
    for p in pages:
        base = os.path.join(tmp, f"{os.path.basename(pdf)}_{p}")
        subprocess.run(["pdftoppm", "-r", str(dpi), "-png", "-f", str(p), "-l", str(p), "-singlefile", pdf, base], check=True)
        out.append(Image.open(base + ".png").convert("RGB"))
    return out


def shadowed(page, target_h):
    r = target_h / page.height
    pg = page.resize((int(page.width * r), target_h), Image.LANCZOS)
    pad = 40
    sh = Image.new("RGBA", (pg.width + pad * 2, pg.height + pad * 2), (0, 0, 0, 0))
    d = ImageDraw.Draw(sh)
    d.rectangle([pad + 12, pad + 18, pad + pg.width + 12, pad + pg.height + 18], fill=(0, 0, 0, 110))
    sh = sh.filter(ImageFilter.GaussianBlur(16))
    sh.paste(pg, (pad, pad))
    return sh


def wrap(draw, text, font, max_w):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if draw.textlength(t, font=font) <= max_w:
            cur = t
        else:
            lines.append(cur)
            cur = w
    lines.append(cur)
    return lines


def preview_tag(d):
    f = ImageFont.truetype(FONT, 34)
    d.rounded_rectangle([W - 560, H - 90, W - 40, H - 30], 24, fill="#FFFFFF")
    d.text((W - 300, H - 60), "Digital file preview", font=f, fill="#1C1C1C", anchor="mm")


def hero(cfg, folder, tmp):
    img = Image.new("RGB", (W, H), cfg["bg"])
    d = ImageDraw.Draw(img)
    pages = render(os.path.join(folder, cfg["hero_pdf"]), cfg["hero_pages"], tmp)
    x = 1080
    angles = [-7, 4, -2, 8]
    for i, pg in enumerate(pages[:3]):
        s = shadowed(pg, 1150).rotate(angles[i], expand=True, resample=Image.BICUBIC)
        img.paste(s, (x + i * 300 - 60, 230 - i * 40 + (i % 2) * 60), s)
    d = ImageDraw.Draw(img)
    ft = ImageFont.truetype(SERIFB, 112)
    y = 230
    for line in wrap(d, cfg["title"], ft, 1000):
        d.text((110, y), line, font=ft, fill=cfg["fg"])
        y += 130
    fs = ImageFont.truetype(FONT, 46)
    y += 30
    for line in wrap(d, cfg["sub"], fs, 980):
        d.text((110, y), line, font=fs, fill=cfg["accent"])
        y += 60
    fb = ImageFont.truetype(FONTB, 42)
    y += 50
    for b in cfg["badges"]:
        tw = d.textlength(b, font=fb)
        d.rounded_rectangle([110, y, 110 + tw + 70, y + 84], 42, fill="#FFFFFF")
        d.text((145, y + 42), b, font=fb, fill="#1C1C1C", anchor="lm")
        y += 108
    preview_tag(d)
    return img


def slide(cfg, folder, tmp, title, pdf, pages, note):
    img = Image.new("RGB", (W, H), "#F8F6F4")
    d = ImageDraw.Draw(img)
    ft = ImageFont.truetype(FONTB, 84)
    d.text((W // 2, 120), title, font=ft, fill="#1C1C1C", anchor="mm")
    fn = ImageFont.truetype(FONT, 46)
    d.text((W // 2, 215), note, font=fn, fill="#555555", anchor="mm")
    rs = render(os.path.join(folder, pdf), pages, tmp, dpi=90)
    n = len(rs)
    cols = min(n, 4)
    rows = (n + cols - 1) // cols
    th = int(min((H - 420) / rows - 40, 1200))
    ims = [shadowed(r, th) for r in rs]
    tot_w = sum(im.width for im in ims[:cols]) - 80 * (cols - 1)
    for i, im in enumerate(ims):
        r_, c_ = divmod(i, cols)
        x = (W - tot_w) // 2 + c_ * (im.width - 80)
        y = 290 + r_ * (th + 20)
        img.paste(im, (x, y), im)
    preview_tag(d)
    return img


def main():
    sku = sys.argv[1]
    cfg = CONFIG[sku]
    root = os.path.join("products", sku)
    folder = os.path.join(root, "customer-files")
    out = os.path.join(root, "storefront")
    os.makedirs(out, exist_ok=True)
    with tempfile.TemporaryDirectory() as tmp:
        imgs = [hero(cfg, folder, tmp)] + [slide(cfg, folder, tmp, *s) for s in cfg["slides"]]
    for i, im in enumerate(imgs, 1):
        im.save(os.path.join(out, f"{sku}_storefront_{i:02d}.png"), optimize=True)
    m = imgs[0].resize((375, int(375 * H / W)), Image.LANCZOS)
    m.save(os.path.join(out, f"{sku}_mobile375_check.png"))
    print("\n".join(sorted(glob.glob(os.path.join(out, "*.png")))))


if __name__ == "__main__":
    main()
