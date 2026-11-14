# First Dollar

Workspace for First Dollar, an independent digital-download business (kids' mystery games, dollhouse miniatures, no-sew crochet). Not related to any other project or store.

Brief: `CLAUDE.md`. Plan and status: `PROJECT.md`. Skills: `../.claude/skills/first-dollar-*`.

## Folders
- `research/` platforms matrix, search log, market evidence, organic research, tooling candidates, capability inventory, provenance, smoke tests
- `backlog/` one prioritized backlog per line
- `scripts/` reproducible builders and QA (printkit, minis, mystery, crochet, storefront, video, checks)
- `products/<SKU>/` release folder: customer-files, BUYER-GUIDE.md, source, storefront, listing, content, qa; `products/manifest.csv` is the source of truth for status
- `integrations/` connection states and fallbacks; `analytics/` calendar and weekly numbers; `checkpoints/` one note per batch

## Resume in a new session
1. Read `PROJECT.md` (open items with owners) and the newest file in `checkpoints/`.
2. Read `products/manifest.csv`.
3. Rebuild and re-check anything you change (run from the repo root):
   - `python3 scripts/minis_build.py --set grocery` then `python3 scripts/qa_pdf.py --calibration products/MINI-GROC-01/customer-files/*.pdf`
   - `python3 scripts/mystery_build.py --game bday` then `python3 scripts/qa_pdf.py products/MYST-BDAY-01/customer-files/*.pdf`
   - `python3 scripts/crochet_pattern.py --pattern whale`
   - `python3 scripts/listing_check.py <SKU>`, `python3 scripts/make_storefront.py <SKU>`, `python3 scripts/make_preview_video.py <SKU>`
