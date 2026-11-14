---
name: first-dollar-prepress
description: Use for exact print design and PDF export in the studio - true-size dollhouse miniature sheets (1:6/1:12/1:16/1:24), cut/fold/glue conventions, calibration marks, A4 and US Letter variants, and printable game layouts.
---

# Design and prepress

Exact geometry is done in code with reportlab (BSD) via `scripts/printkit.py`. Canva is for editable marketing visuals, not for cut lines or calibration.

## Conventions (printkit)
- Units are millimetres everywhere. Cut = solid 0.35 pt. Fold = dashed 2/1.2 mm. Glue = grey hatched area labelled GLUE when it fits.
- Every true-size page carries `calibration_block` (50 mm bar + 2 in bar) and "PRINT AT 100% / ACTUAL SIZE". PDFs set `PrintScaling=None`.
- Layout margin 12-14 mm; nothing closer than 6 mm to the paper edge (home printers). No full-bleed backgrounds.
- Fonts: DejaVu (embedded, free licence). Do not use fonts that cannot be embedded.

## Miniatures
- Sets live in `scripts/minis_sets.py`. Item artwork is drawn once in real-life mm and scaled by the builder, so all scales stay proportional. Kinds: `box` (glued net), `wrap` (cylinder label), `flat` (sign/tag, optional fold-over two-sided).
- Build: `python3 scripts/minis_build.py --set <key>`. Output: one PDF per scale per paper.
- Only ship a scale when the smallest glue tab is >= 2 mm and key text is >= about 1.5 mm cap height; record rejected scales with a reason (`rejected_scales`).
- Original fictional brands only. No real logos or trade dress.

## After every export
Run `first-dollar-qa` checks: `python3 scripts/qa_pdf.py --calibration <files>` for true-size files, without `--calibration` for games. Render pages with `pdftoppm -r 100` and inspect; zoom to 600 dpi on the smallest scale.
