---
name: first-dollar-qa
description: Use before marking any studio SKU ready - runs prepress PDF checks, calibration measurement, listing accuracy checks, blind-solve/physical-test gates, and updates the manifest and QA evidence.
---

# Studio QA gates

| Gate | Command / evidence | Applies |
|---|---|---|
| G1 PDF prepress | `python3 scripts/qa_pdf.py [--calibration] <pdfs>` saved to `qa/prepress-qa.jsonl` (page size, fonts embedded, 6 mm safe margin, calibration bars +/-0.25 mm) | all |
| G2 Visual render | `pdftoppm` renders inspected at full page and at 600 dpi on the smallest scale; note in `qa/visual.md` | all |
| G3 Logic | blind solve by a fresh subagent from buyer files only (`qa/blind-solve.md`) | mystery |
| G4 Stitch math | `crochet_pattern.py --pattern <key>` exit 0 | crochet |
| G5 Listing accuracy | `python3 scripts/listing_check.py <SKU>` | all |
| G6 Physical | owner print-and-assembly log with photo (miniatures), real playtest log (mystery), finished sample + external tester (crochet) | all, before release |
| G7 Mobile render | storefront images inspected at 375 px width | all |

Status ladder in `products/manifest.csv`: `idea > drafting > files-qa-pass > awaiting-physical-qa > release-ready > listed-draft > live`. Only the owner's logged evidence moves a SKU past `awaiting-physical-qa`. `live` requires the platform listing ID and URL.
