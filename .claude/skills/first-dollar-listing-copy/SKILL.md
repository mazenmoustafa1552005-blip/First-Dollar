---
name: first-dollar-listing-copy
description: Use to write studio marketplace listings - English title, buyer-focused selling points, description, tags, price rationale and per-platform export package (Etsy first, then Payhip/Gumroad/Ravelry/LoveCrafts), with accuracy checks against the actual files.
---

# Listing copy

Also load the user-level `anthropic-skills:etsy-listing-seo` skill for Etsy keyword method.

## Per SKU, write `products/<SKU>/listing/listing.md` with
- Title (Etsy max 140 chars, front-load the buyer's search phrase).
- 5 selling points that are TRUE of the files (page counts, scales, paper sizes, B&W option, setup time).
- Description: what you get (file list with page counts), how it works, print instructions, licence (personal use), what is NOT included (physical items, editable files unless provided).
- 13 Etsy tags (max 20 chars each), plus platform-specific keyword lines.
- Price + rationale citing dated `[LP]` comparables from `research/market-evidence.md`, launch price vs list price.
- Next purchase: the bundle or companion SKU.

## Accuracy rules
- Every number in copy must be checked against the generated PDFs (page counts via pypdf, scales and sizes from the builder). Run `python3 scripts/listing_check.py <SKU>`.
- Do not say "playtested", "tested pattern" or "bestseller" without logged evidence.
- Digital download wording: "No physical item will be shipped."
- Etsy per-file limit is 20 MB and 5 files per listing: plan zips or merged files accordingly.
