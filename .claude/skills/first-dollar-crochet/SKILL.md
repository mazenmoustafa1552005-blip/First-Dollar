---
name: first-dollar-crochet
description: Use when drafting, checking or packaging no-sew crochet (amigurumi) patterns for the studio sea-animal collection - US terms, materials, gauge/size, stitch counts, step photo list, tester workflow.
---

# No-sew crochet production

## Source of truth
Patterns are structured data in `scripts/crochet_pattern.py` (ops with consumed/produced stitch counts). Text is rendered from the same data, so instructions and counts cannot drift.
- Validate: `python3 scripts/crochet_pattern.py --pattern <key> --md <out.md>` (exit 1 on any count error).
- US terminology only (sc, hdc, dc, inc, dec, sl st, ch, MR).
- "No-sew" means parts are crocheted on or worked continuously; a yarn needle is only used to weave in ends. Say exactly that in listings.

## Honesty gates (customer-facing text)
- Until the owner crochets the sample: status DRAFT, size and yardage marked "estimate".
- Step photos and listing photos must be of the actual sample. Never use AI images or renders as product photos for crochet.
- Release only after: sample made and measured, yardage weighed, an external tester followed the written PDF, and errata fixed. Log in `products/<SKU>/qa/`.

## Collection design
Shared base (same nose-start body, same eye placement, same fin join) so a 4-pack feels coherent; each animal must add one distinct feature (tentacles, shell, bell, fin shape). Safety note for children under 3: embroider eyes.
