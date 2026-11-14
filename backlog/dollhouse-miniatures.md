# Backlog: printable dollhouse miniatures

Evidence base: `research/market-evidence.md` (2026-11-14, snippet level). [LP] small sets USD 1-5, 45-65 piece packs USD 5-10, shop or room kits USD 10-15; [SS] comparable shops 13k to 39.4k cumulative sales; [SC] Pinterest interest for "dollhouse printables" up about 30% in 12 months (the only rising signal found). Gaps: no 1:16, 1:24 or 1:48 printable shop kits found, no 1:6 shop or shelf kit; reviewers complain designs print too big (calibration helps).

Engine: `scripts/minis_build.py` + `minis_sets.py`. Shared style: flat vector packaging, fictional brands, one palette per shop. Each set: 1:6, 1:12, 1:16, 1:24 true-size PDFs (A4 + Letter); 1:48 only when the minimum glue tab is >= 2 mm and text is legible (currently rejected for packaging).

| Pri | SKU | Set | Distinct reason to buy | Price | Status | Next action (owner of action) |
|---|---|---|---|---|---|---|
| 1 | MINI-GROC-01 | The Corner Grocer: Pantry Set (5 boxes, 3 labels, sign, specials board, tags) | 4 scales in one purchase, calibration on every page | 9.99 (launch 7.99) | files-qa-pass, awaiting physical check | Print 1:12 and 1:24 Letter or A4 at 100% on card, assemble 1 box + 1 can + sign, measure, photograph (owner) |
| 2 | MINI-BAKE-01 | The Corner Bakery: bread bags, cake boxes, pastry trays, menu board | Pairs with grocery shop | 9.99 | idea | Write art functions for 8 items (Claude) |
| 3 | MINI-CAFE-01 | The Corner Cafe: cups and sleeves, menu, pastry case labels, coffee bags | Completes the street of shops | 9.99 | idea | After BAKE-01 |
| 4 | MINI-SHELF-01 | Shop shelving and crates (printable display units) | Requested in reviews; makes the sets usable | 5.99 | idea | Design shelf net with card thickness allowance (Claude) |
| 5 | MINI-GROC-02 | Fresh produce and freezer aisle add-on | Next purchase for GROC-01 buyers | 6.99 | idea | Later |
| 6 | MINI-BUN-01 | Main Street bundle (grocery, bakery, cafe, shelves) | Discount bundle | 22-25 | idea | After 3 sets release-ready |

Per-scale variants at USD 4.50 for own-traffic stores (Payhip/Gumroad) once a platform is confirmed.
