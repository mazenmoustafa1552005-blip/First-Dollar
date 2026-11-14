# License and asset provenance

| Asset | Used in | Source | License | Notes |
|---|---|---|---|---|
| DejaVu Sans / Serif / Mono fonts | all PDFs and images | system package fonts-dejavu | Bitstream Vera + public domain changes: free to embed and redistribute in documents | Embedded subset in every PDF (pdffonts check) |
| Miniature artwork and brands (Sunny Oats, Pip & Co, Meadow Milk, Nonna Bella, Morning Garden tea, Golden Grove, Hilltop Farm, The Corner Grocer) | MINI-GROC-01 | drawn in code: scripts/minis_sets.py | original work of the studio | Fictional brands; checked against obvious real trade dress by design (no real logos). A trademark search of the names was not performed: do before scaling the line |
| Mystery story, characters, clues, figures | MYST-BDAY-01 | scripts/mystery_content_bday.py, mystery_build.py | original work | Written this run |
| Crochet pattern Bubbles the No-Sew Whale | CRO-SEA-01 | scripts/crochet_pattern.py | original work | Standard amigurumi increase/decrease sequences are common technique, not copyrightable expression |
| Storefront images and teaser video | storefront/, content/ | rendered from the PDFs with Pillow + FFmpeg | original | Labelled "Digital file preview" |
| Silent audio track | teaser video | FFmpeg anullsrc | n/a | Add music only from a commercially licensed source and log it here |
| Python libs | build | reportlab 5.0.1 (BSD), pypdf 6.17.0 (BSD-3), Pillow 12.3.0 (MIT-CMU) | permissive | tooling only, not redistributed in products |
