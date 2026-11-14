"""Compose a 1080x1920 vertical teaser from PDF renders with burned-in captions.

Usage: python3 scripts/make_preview_video.py <SKU>
Shots are defined in SHOTS below (page renders + caption). Captions sit inside
the safe zone (y 300-1500). Output: products/<SKU>/content/<SKU>_teaser_9x16.mp4
plus a cover PNG. Uses only local FFmpeg (no billed services).
"""
import os
import subprocess
import sys
import tempfile

from PIL import Image, ImageDraw, ImageFont

FONTB = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
W, H, FPS = 1080, 1920, 30

SHOTS = {
    "MYST-BDAY-01": {
        "bg": "#5B3FA0",
        "shots": [
            (None, "The birthday cake just VANISHED.", 2.2),
            (("MYST-BDAY-01_PrintPack_Letter_Color.pdf", 3, (0.0, 0.0, 1.0, 0.55)), "6 suspects...", 2.0),
            (("MYST-BDAY-01_PrintPack_Letter_Color.pdf", 5, (0.0, 0.05, 1.0, 0.33)), "12 clues...", 2.0),
            (("MYST-BDAY-01_PrintPack_Letter_Color.pdf", 5, (0.0, 0.05, 0.52, 0.3)), "A 19 cm ZIGZAG boot print. Whose is it?", 2.8),
            (("MYST-BDAY-01_PrintPack_Letter_Color.pdf", 1, (0.0, 0.0, 1.0, 0.6)), "Your kids are the detectives.", 2.4),
            (None, "Printable party game for ages 8-12. Link in bio.", 2.6),
        ],
    },
}


def render(pdf, page, tmp):
    base = os.path.join(tmp, f"r{page}")
    subprocess.run(["pdftoppm", "-r", "200", "-png", "-f", str(page), "-l", str(page), "-singlefile", pdf, base], check=True)
    return Image.open(base + ".png").convert("RGB")


def caption(d, text, y):
    f = ImageFont.truetype(FONTB, 66)
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if d.textlength(t, font=f) < W - 160:
            cur = t
        else:
            lines.append(cur)
            cur = w
    lines.append(cur)
    for i, ln in enumerate(lines):
        tw = d.textlength(ln, font=f)
        yy = y + i * 84
        d.rounded_rectangle([(W - tw) / 2 - 24, yy - 10, (W + tw) / 2 + 24, yy + 76], 18, fill="#FFFFFF")
        d.text((W / 2, yy + 33), ln, font=f, fill="#1C1C1C", anchor="mm")


def frame(cfg, folder, shot, tmp):
    src, text, _ = shot
    img = Image.new("RGB", (W, H), cfg["bg"])
    if src:
        pdf, page, (x0, y0, x1, y1) = src
        pg = render(os.path.join(folder, pdf), page, tmp)
        crop = pg.crop((int(x0 * pg.width), int(y0 * pg.height), int(x1 * pg.width), int(y1 * pg.height)))
        r = min((W - 80) / crop.width, 1000 / crop.height)
        crop = crop.resize((int(crop.width * r), int(crop.height * r)), Image.LANCZOS)
        img.paste(crop, ((W - crop.width) // 2, 760 - crop.height // 2 + 120))
        caption(ImageDraw.Draw(img), text, 330)
    else:
        caption(ImageDraw.Draw(img), text, 860)
    return img


def main():
    sku = sys.argv[1]
    cfg = SHOTS[sku]
    root = os.path.join("products", sku)
    folder = os.path.join(root, "customer-files")
    out_dir = os.path.join(root, "content")
    os.makedirs(out_dir, exist_ok=True)
    with tempfile.TemporaryDirectory() as tmp:
        lst = []
        for i, shot in enumerate(cfg["shots"]):
            p = os.path.join(tmp, f"s{i}.png")
            frame(cfg, folder, shot, tmp).save(p)
            if i == 0:
                frame(cfg, folder, cfg["shots"][3], tmp).save(os.path.join(out_dir, f"{sku}_cover_9x16.png"))
            lst.append((p, shot[2]))
        concat = os.path.join(tmp, "list.txt")
        with open(concat, "w") as f:
            for p, dur in lst:
                f.write(f"file '{p}'\nduration {dur}\n")
            f.write(f"file '{lst[-1][0]}'\n")
        out = os.path.join(out_dir, f"{sku}_teaser_9x16.mp4")
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", concat,
                        "-f", "lavfi", "-i", "anullsrc=r=48000:cl=stereo",
                        "-vf", f"fps={FPS},scale={W}:{H},format=yuv420p", "-c:v", "libx264", "-preset", "medium",
                        "-crf", "20", "-c:a", "aac", "-shortest", "-movflags", "+faststart", out], check=True)
    print(out)


if __name__ == "__main__":
    main()
