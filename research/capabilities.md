# Capability inventory

Last updated: 2026-11-14 (run 1). Evidence log: `research/smoke-tests.log`. Candidate research: `research/tooling-candidates.md`.

Status key: PASS = smoke-tested this run with evidence; READY = available, not yet exercised on a product; BLOCKED = needs owner action; GAP = no capability yet.

## Stage to capability map

| Stage | Required capability | Available now | Missing / dependency | Acceptance check | Status |
|---|---|---|---|---|---|
| Platform and competitor research | Web search, page fetch, dated log | WebSearch; web-fetch agent; Whop docs connector; Trends MCP, Trend_track, Ubersuggest (credit-metered) | Network allowlist blocks etsy.com, ravelry.com, help.etsy.com, gumroad.com, payhip.com, developer.etsy.com and others: claims are search-snippet level | Every claim has status + URL; blocked hosts logged as gaps | PASS (with gap) |
| Creative direction | House style per line, palettes | `first-dollar-prepress` + `first-dollar-puzzle-writing` skills; product-art-design user skill | Canva brand kit not set up (list-brand-kits returned none) | Style sheet per line in backlog | READY |
| Story and puzzle writing | Logic design + independent solve | `first-dollar-puzzle-writing` skill, content modules, fresh-subagent blind solve | Real playtest needs the owner | Unique solution in 2 blind solves; every innocent eliminated by a hard clue | PASS (MYST-BDAY-01) |
| Print design and export | Exact mm geometry, cut/fold/glue, calibration, A4 + Letter, embedded fonts | `scripts/printkit.py`, `minis_build.py`, `mystery_build.py` (reportlab 5.0.1) | Inkscape/qpdf not installed (not needed yet) | `qa_pdf.py`: page size, fonts embedded, 6 mm safe margin, bars 50 mm and 2 in within 0.25 mm | PASS (14 + 8 PDFs) |
| Prepress QA | Rasterized measurement, negative test | `qa_pdf.py`, pdftoppm 24.02 | Physical print-and-assembly check by owner | 98% scaled file must FAIL: measured 49.19 mm, failed as expected | PASS |
| Crochet drafting | Stitch-count math, US terms, rendered text | `crochet_pattern.py` (structured source, validator, markdown) | Physical sample, step photos, yardage, external tester | Real pattern 0 errors; corrupted count detected | PASS (math only) |
| Crochet testing | Sample + tester | none | Owner crochets sample; recruit tester | Tester log with errata | BLOCKED (owner) |
| Merchandising and listing copy | Title/tags/description/price per platform, accuracy check | `first-dollar-listing-copy` skill, `listing_check.py`, etsy-listing-seo user skill | Live Etsy keyword data (blocked host) | Claims match PDFs; title <= 140; 13 tags <= 20 chars | PASS (2 SKUs; caught a 141-char title) |
| Storefront images | Mockups from real renders, mobile check | `make_storefront.py` (Pillow) | Real photos of assembled minis / crochet sample | 4:3 2400x1800 PNG + 375 px check inspected | PASS |
| Image generation (marketing) | Editable visuals | Canva connector (read-only test passed), image-generation user skill | Canva brand kit; owner Canva plan tier unknown | Create + export + edit test design | READY (read-only tested) |
| Video production | 9:16 composition, captions, cover | FFmpeg 6.1.1, `make_preview_video.py`, short-form-editor / video-captions / free-voiceover user skills | Google Flow setup unknown (interactive only assumed); Veo API is billed: needs approval | 1080x1920 H.264 yuv420p + AAC, frame inspected at phone size | PASS (teaser) |
| Organic distribution | Calendar, captions, pins, scheduler | `first-dollar-distribution` skill, pinterest-pins user skill, calendar CSV | Metricool MCP not connected (owner OAuth); Pinterest API app (owner) | Post marked scheduled only with scheduler ID | READY / BLOCKED for scheduling |
| Analytics | Visits, clicks, orders by channel | weekly.csv template | Platform stats need connected accounts | Weekly row per channel with source | GAP until accounts exist |
| Marketplace integration: Etsy | Draft listing + digital file upload via Open API v3 | none connected | Etsy shop + developer app + OAuth (owner); candidate MCP `Bl0ck154/etsy-seller-mcp-hub` 0.5.0 (needs code review, repo not readable via API from this session) | Draft listing created, file uploaded, listing ID recorded | BLOCKED (owner) |
| Marketplace integration: Whop | Products/files API | Whop MCP connected: user-level, admin profile, no business account selected | Business account and fit decision; any write needs explicit approval | Read-only `connection_status` returned identity and scopes | PASS (read-only) |
| Marketplace integration: Shopify | Digital products | Shopify MCP | Needs re-authentication; connected store belongs to a separate, unrelated business; not to be used for First Dollar without explicit approval | n/a | BLOCKED |
| Payhip / Gumroad / Lemon Squeezy / Ravelry | Upload | none (no write MCP exists) | Manual upload packages | Upload checklist per platform | Manual fallback |

## Installed this run

| Item | Source / version | Scope | Credentials | Rationale |
|---|---|---|---|---|
| 8 project skills | authored here: `.claude/skills/first-dollar-*/SKILL.md` | project | none | No maintained public skill covers true-size miniature prepress, kid-safe puzzle logic with blind solve, or stitch-count validation; authored and validated via the scripts they call |
| Python libs | reportlab 5.0.1, pypdf 6.17.0, Pillow 12.3.0 (pinned in `requirements.txt`) | already in environment | none | BSD/MIT-style licences; smoke-tested |
| System tools | ffmpeg 6.1.1, poppler 24.02.0 | already in environment | none | Smoke-tested |

## Considered and not installed this run (see tooling-candidates.md)
- kajisho5/ffmpeg-skill (MIT): local FFmpeg already passes the video acceptance check; adopt only after reading its scripts.
- Bl0ck154/etsy-seller-mcp-hub (MIT, 0.5.0): best Etsy file-upload fit but low adoption; requires code review and owner Etsy OAuth. Start read-only.
- Metricool official MCP (`ai.metricool.com/mcp`): after owner connects Metricool.
- chrome-devtools-mcp: not needed now; mobile checks use rendered PNGs.
- Rejected: gflow-cli (reverse-engineered Google login automation), terryso Pinterest scraper, archived rmarescu/gumroad-mcp, unverified `mcp.metricool.ai`, Canva Dev MCP (for building Canva apps).

## Separately billed services (none used; approval required before any spend)
Etsy listing fee USD 0.20 per listing + transaction/payment fees; possible Etsy shop set-up fee (unknown for Egypt); Veo API per-second billing; Canva Pro (if needed); Metricool paid tiers; credit-metered research tools (Trend_track, Ubersuggest).
