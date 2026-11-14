# Tooling candidates for First Dollar

- Date checked: 2026-11-14
- Scope: research only. Nothing was installed, cloned, authorized or enabled.
- Method: GitHub search API (`gh api -X GET search/repositories`), raw.githubusercontent.com reads of README, SKILL.md, package.json and pyproject.toml, PyPI and npm registry JSON, the official Claude plugin marketplace manifest (`anthropics/claude-plugins-official/.claude-plugin/marketplace.json`), and web search.
- Access limits in this session:
  - `gh api repos/{owner}/{repo}` and the commits endpoints return HTTP 403 for every repo outside this session's configured repositories, so latest commit SHAs could not be read directly. SHAs below come only from the official marketplace manifest pins; everything else is `unknown`.
  - WebFetch could not resolve developer.etsy.com, developers.pinterest.com, help.metricool.com or www.canva.dev (host not in the session network allowlist). Official-doc facts below come from web search summaries of those pages and are marked "via search"; re-verify by opening the pages before relying on them.
- "Pushed" is the repo's `pushed_at` from the GitHub search API, a maintenance signal, not a release date.

## Already available in this session (no install needed)

| Capability | Source | Notes |
|---|---|---|
| Canva connector | `mcp__Canva__*` tools (connected) | Create, edit, resize, export designs; brand kits; video generation. Official Canva remote MCP. |
| Shopify connector | `mcp__Shopify__*` tools (connected) | Products, digital products, file upload, GraphQL, theme tools. Bound to the owner's sign-in. |
| Whop connector | `mcp__Whop__*` tools (connected, admin profile) | Products, files, experiences, payments. Write operations need explicit approval. |
| Google Drive connector | `mcp__Google_Drive__*` | Asset storage and handoff. |
| Trend research | `mcp__Trend_track__*`, `mcp__Trends_MCP__*`, `mcp__Ubersuggest__*` | Competitor ads/shops, trend series, keyword research. Some calls consume credits; check `check_credits` / `user_limits` first. |
| Skills | `anthropic-skills:pdf`, `print-upscale`, `product-art-design`, `etsy-listing-seo`, `pinterest-pins`, `short-form-editor`, `video-captions`, `clip-finder`, `free-voiceover`, `marketing-writing-kit`, `niche-sweet-spot-finder`, `skill-creator`, `kdp-publishing` | User-level skills already loaded. Cover much of PDF, listing copy, pins, short-form video and captions. |
| System tools | ffmpeg 6.1.1, ffprobe 6.1.1, pdftoppm (poppler), node 22.23.4, npx 10.9.9, uv/uvx 0.11.32, Python 3.13.18, reportlab 5.0.1, pypdf 6.17.0, Pillow 12.3.0 | Present now. Missing: inkscape, ghostscript, qpdf, PyMuPDF, cairosvg, pikepdf. |

Failed to connect this session (marketing/product-management plugin MCPs: ahrefs, similarweb, supermetrics, notion, figma and others): proxy refused the tunnel. Not needed for the core pipeline.

## Candidates table

| # | Candidate | Area | Source URL | Version / pin | Date | License | Stars (search API) | Official? | Credentials | Cost | Recommendation |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | anthropics/skills (document-skills, example-skills) | PDF, design, skill authoring | https://github.com/anthropics/skills | commit unknown | pushed 2026-11-14 | Apache-2.0 per README and skills/pdf/LICENSE.txt (repo metadata shows none) | 194316 | Yes (Anthropic) | None | Free | Adopt (largely already present as user skills; install only if a project-pinned copy is wanted) |
| 2 | Official Claude plugin marketplace | Plugin directory | https://github.com/anthropics/claude-plugins-official | commit unknown | pushed 2026-11-14 | Apache-2.0 | 47244 | Yes (Anthropic) | None | Free | Adopt as the primary plugin source |
| 3 | canva plugin (canva-sdks/canva-skills) | Canva skills + MCP registration | https://github.com/canva-sdks/canva-skills | marketplace pin `bfcbc681560f6031e9949ea52f81e20beb87e39e` | unknown | Apache-2.0 (LICENSE file) | unknown | Yes (Canva) | Canva OAuth | Free plugin; some features need Canva Pro | Adopt later after owner auth (connector already live; plugin adds skills) |
| 4 | Canva remote MCP `https://mcp.canva.com/mcp` | Design ops | canva.dev/docs/connect/canva-mcp-server-setup | n/a (hosted) | unknown | Proprietary service | n/a | Yes | Canva OAuth | Canva plan dependent | Adopt (already connected) |
| 5 | Canva Dev MCP (`@canva/cli mcp`) | Building Canva apps | canva.dev/docs/apps/mcp-server | npm @canva/cli 2.19.0 | 2026-11-11 | "SEE LICENSE IN LICENSE.md" | n/a | Yes | None | Free | Reject (for building Canva apps, not designs) |
| 6 | Etsy OpenAPI Dev MCP | Etsy API docs/schemas | developer.etsy.com/documentation (via search) | unknown | unknown | unknown | n/a | Yes (Etsy) | No API key needed (via search) | Free | Adopt after confirming install command on the official page (docs-only, no shop access) |
| 7 | Bl0ck154/etsy-seller-mcp-hub | Etsy Open API v3 shop ops incl. file uploads | https://github.com/Bl0ck154/etsy-seller-mcp-hub | npm 0.5.0 | 2026-11-02 | MIT | 3 | No | Etsy app keystring + OAuth PKCE (listings_r/listings_w etc.) | Free; Etsy listing fees apply on publish | Adopt later after owner auth and code review (best fit for digital file upload) |
| 8 | mofiaboss/etsy-mcp | Etsy Open API v3 primitives (90 tools) | https://github.com/mofiaboss/etsy-mcp | PyPI version unknown (lookup failed) | pushed 2026-04-15 | MIT | 1 | No | Etsy app + OAuth PKCE, tokens on disk | Free | Adopt later as fallback (Python 3.13, uvx) |
| 9 | aserper/etsy-mcp | Etsy Open API v3 (37 tools) | https://github.com/aserper/etsy-mcp | package.json 1.0.0 | pushed 2026-04-02 | MIT | 12 | No | Etsy app + OAuth PKCE, tokens in `~/.etsy-mcp/tokens.json` | Free | Reject for now (no digital listing file tool listed in README) |
| 10 | DaveTheProfessor/etsy-ops-mcp | Etsy title/tag edits, confirmation-gated | https://github.com/DaveTheProfessor/etsy-ops-mcp | pyproject 1.0.0 | pushed 2026-07-15 | MIT per pyproject (repo metadata NOASSERTION) | 0 | No | ETSY_API_KEY + access token in env | Free | Adopt later (narrow, safe SEO edit tool) |
| 11 | administrativetrick/etsy-mcp-server | Etsy read-only search | https://github.com/administrativetrick/etsy-mcp-server | unknown | pushed 2025-12-12 | MIT | 21 | No | API key only; OAuth not implemented (via search) | Free | Reject (read-only, no writes or files) |
| 12 | rmarescu/gumroad-mcp | Gumroad products, sales, offer codes | https://github.com/rmarescu/gumroad-mcp | npm 0.0.8 | 2025-04-21 | MIT | 32 | No | Gumroad access token | Free | Reject (repo archived; no product creation or file upload) |
| 13 | stcmain/gumroad-mcp | Gumroad read-only analytics | https://github.com/stcmain/gumroad-mcp | unknown | pushed 2026-08-01 | MIT | 1 | No | Gumroad token (env) | Free | Adopt later after owner auth (read-only analytics only) |
| 14 | Payhip API | Payhip | https://payhip.com/api-reference (via search) | n/a | unknown | Proprietary | n/a | Yes | `payhip-api-key` header | Free API | No MCP exists; use manual upload + webhooks. Reject MCP search, plan manual fallback |
| 15 | Metricool official MCP | Scheduling + analytics (IG, TikTok, YT, Pinterest, more) | https://github.com/metricool/mcp-metricool (not reachable from this session); hosted endpoint `https://ai.metricool.com/mcp` (via search) | PyPI mcp-metricool 1.1.9 | 2025-10-07 (PyPI upload) | unknown | unknown | Yes (Metricool) | Metricool OAuth; Claude directory connector | Works on any Metricool plan incl. Free (via search); paid tiers add limits | Adopt later after owner auth (preferred scheduler) |
| 16 | vicampuzano/metricool-mcp | Docs for a remote Metricool MCP at `mcp.metricool.ai` | https://github.com/vicampuzano/metricool-mcp | unknown | pushed 2026-08-21 | none | 1 | Unclear; endpoint differs from Metricool's documented one | OAuth to a third-party endpoint | unknown | Reject (unverified endpoint receiving account OAuth) |
| 17 | Pinterest official MCP Server | Pinterest data | community.pinterest.biz post dated 2026-09-22 (via search) | unknown | 2026-09-22 | unknown | n/a | Yes (Pinterest) | unknown | unknown | Investigate; adopt later only after reading developers.pinterest.com/about-pinterest-mcp/ |
| 18 | clugtu/pinterest-mcp | Pinterest API v5 pins, boards, analytics | https://github.com/clugtu/pinterest-mcp | unknown | pushed 2026-03-12 | MIT | 8 | No | Pinterest Business account + registered app (client id/secret), token in `.pinterest_token.json` | Free | Adopt later after owner auth, only if Metricool cannot cover Pinterest |
| 19 | terryso/mcp-pinterest | Pinterest image scraper | https://github.com/terryso/mcp-pinterest | npm pinterest-mcp-server 1.2.0 | 2025-05-05 (npm); pushed 2026-11-02 | MIT | 52 | No | None (headless scraper) | Free | Reject (README says it is an unofficial scraper that may conflict with Pinterest ToS) |
| 20 | postiz plugin (gitroomhq/postiz-agent) | Social scheduling alternative | https://github.com/gitroomhq/postiz-agent | marketplace pin `86e02524377cc60a6cd6ef67fd10a3caeade8d2c`; package.json 2.0.27 | unknown | AGPL-3.0 | unknown | Vendor-official, in Anthropic marketplace | Postiz account/API | Postiz SaaS paid, or self-host | Reject for now (Metricool already chosen; keep as fallback) |
| 21 | kajisho5/ffmpeg-skill | FFmpeg editing, captions, 9:16 reframe, loudness, delivery checks | https://github.com/kajisho5/ffmpeg-skill | npm 3.8.12 | 2026-11-14 | MIT | 5500 | No | None ("no cloud, no API keys") | Free | Adopt (after reading scripts; stdlib Python + local ffmpeg 6.1+, which is present) |
| 22 | hyperframes plugin (heygen-com/hyperframes) | HTML-to-video compositions | https://github.com/heygen-com/hyperframes | marketplace pin `8d2b6e7bdc1c2c26d1abf64ef075c00a1bb230a2` | pushed 2026-11-14 | Apache-2.0 | 84108 | Vendor-official, in Anthropic marketplace | Render dependencies unknown | Local render free; HeyGen services billed | Adopt later (evaluate for animated covers/text reels) |
| 23 | ffroliva/gflow-cli | Google Flow (Veo/Imagen) CLI + MCP | https://github.com/ffroliva/gflow-cli | pyproject 0.98.0 | pushed 2026-11-14 | MIT | 394 | No; README says reverse-engineered, not affiliated with Google | Owner's Google session via headed Playwright Chromium | Spends Flow credits | Reject (ToS and account risk; use interactive Flow + export ingest) |
| 24 | Google Veo via Gemini API | Programmatic video | ai.google.dev pricing (via search) | Veo 3.1 Preview (via search) | unknown | Proprietary | n/a | Yes | Google API key + billing | Billed per second of video; third-party sources quote roughly USD 0.05 to 0.60/s, unverified | Adopt later only after explicit spend approval |
| 25 | chrome-devtools-mcp | Visual QA, mobile screenshots | https://github.com/ChromeDevTools/chrome-devtools-mcp | marketplace pin `a878bcad39584337e055778353246820deafa7c0` | pushed 2026-11-13 | Apache-2.0 | 55825 | Yes (Chrome team) | None | Free | Adopt (QA of listing renders and storefront at mobile widths) |
| 26 | shopify-ai-toolkit | Shopify dev skills | https://github.com/Shopify/Shopify-AI-Toolkit | marketplace pin `3c32168c6e4cb73f0b46243c82586176ca58bb48` | pushed 2026-10-27 | MIT | 637 | Yes (Shopify) | None for docs skills | Free | Adopt later (only if Shopify storefront is chosen; connector already live) |
| 27 | liquid-skills (Shopify/liquid-skills) | Liquid theme coding | https://github.com/Shopify/liquid-skills | marketplace pin `ae3e4cc3f454923e388bbd841fd931f0c7bf5be4` | unknown | unknown | unknown | Yes (Shopify) | None | Free | Adopt later (theme work only) |

## Per-candidate notes

### Anthropic skills repo and official marketplace
- anthropics/skills README states the docx, pdf, pptx and xlsx skills are open source under Apache 2.0, with the caveat that they are for demonstration and may differ from Claude's built-in behavior. Install path per README: `/plugin marketplace add anthropics/skills`, then `/plugin install document-skills@anthropic-agent-skills`.
- The official marketplace manifest lists 317 plugins. Relevant entries found: canva, chrome-devtools-mcp, hyperframes, postiz, shopify-ai-toolkit, liquid-skills, liquid-lsp, playwright, superdesign, figma, runway-api, stripe, windsor-ai. No Etsy, Gumroad, Payhip, Pinterest or Metricool plugin is listed.
- Entries pinned to a commit SHA in the manifest are the most reproducible install targets.

### Etsy
- Official: Etsy's developer docs describe an "OpenAPI Dev MCP" that exposes endpoint details, schemas, auth requirements and OAuth scopes, needs no API key, and works with Claude (via search). It is documentation-only and cannot create listings. Exact install command not verified in this session.
- Digital files: `uploadListingFile` is `POST /v3/application/shops/{shop_id}/listings/{listing_id}/files`, requires a `listings_w` OAuth token and `x-api-key`, and takes either a binary `file` or an existing `file_id` (via search of Etsy's listings tutorial). Commonly reported limits of 20 MB per file and 5 files per listing are not confirmed from Etsy's own docs.
- Bl0ck154/etsy-seller-mcp-hub: README says 79 tools, CLI `etsyctl`, local HTTP gateway, "upload product images, videos or files", `ETSY_MCP_READ_ONLY=1` read-only mode, multipart uploads capped at 64 MiB by default, refuses external binding in Docker without an auth token file, non-root Dockerfile, links a SECURITY-REVIEW doc. package.json has zero runtime dependencies and no install hooks (scripts: start, test, check). Low star count; read `src/client.mjs`, `src/oauth.mjs`, `src/mcp-tools.mjs` before enabling, and start read-only. It also includes a "gpt-adapter" and "mcp-oauth" module; confirm they do not open a listener by default.
- mofiaboss/etsy-mcp: README claims 90 tools including listing digital files, `uvx etsy-mcp@latest`, `etsy-mcp auth login` PKCE flow. Python 3.13+. Root pyproject is a uv workspace with the package in `apps/etsy`; actual PyPI version not confirmed.
- aserper/etsy-mcp: OAuth PKCE, 10 req/s limiter, retries; deps `@modelcontextprotocol/sdk`, `dotenv`, `open`, `zod`. No install hooks. Its `generate-types` script fetches Etsy's OpenAPI spec over the network (dev only). README tool table lists image and video upload but no listing file upload.
- DaveTheProfessor/etsy-ops-mcp: only dependency `mcp>=1.12,<2`; every write needs `confirm_write=true` and a matching `expected_title`; no delete or publish. Good model for safe SEO edits.
- All third-party Etsy servers require the owner to register an Etsy app and authorize OAuth. Etsy's API terms require the "not endorsed or certified by Etsy" notice for apps; check the app tier the owner qualifies for.

### Gumroad and Payhip
- No official Gumroad MCP found. rmarescu/gumroad-mcp is archived (last npm 0.0.8, 2025-04-21) and covers products enable/disable, sales and offer codes only. stcmain/gumroad-mcp is read-only (GET only), paginates sales fully, redacts buyer emails to domain, pins `mcp<2`. Neither creates products or uploads files, so Gumroad publishing stays manual with prepared upload packages.
- Payhip: official API reference at payhip.com/api-reference documents coupons and license keys with a `payhip-api-key` header, plus webhooks (via search). No product-creation or file-upload endpoint found and no MCP. Plan: manual upload checklist per SKU.

### Canva
- The live session already has Canva's official remote MCP tools. Canva's setup page gives `claude mcp add --transport http Canva https://mcp.canva.com/mcp` (via search). The official `canva` plugin in Anthropic's marketplace bundles skills (e.g. resize-for-social-media) and registers the same endpoint; its `.mcp.json` contains only that HTTP URL, no local process.
- One aggregator claims a separate `api.canva.com/connect/v1/mcp` endpoint for Developer Portal apps; unverified.

### Metricool and social scheduling
- Metricool's own pages describe an official MCP at `https://ai.metricool.com/mcp`, listed in Claude's connector directory, usable on any Metricool plan including Free, with the open-source server at github.com/metricool/mcp-metricool and on PyPI (via search). PyPI `mcp-metricool` latest seen: 1.1.9, uploaded 2025-10-07. The GitHub repo was not searchable from this session (HTTP 422), so stars and license are unknown.
- Covers scheduling for Instagram (Reels, Stories), TikTok, YouTube Shorts, Pinterest and more, best-time-to-post and analytics, per vicampuzano's README; treat that repo's `mcp.metricool.ai` endpoint as unverified and do not authorize it.
- Owner action: create/connect Metricool account, link each social profile in Metricool, then add the connector through Claude settings or `claude mcp add --transport http`.

### Pinterest
- Pinterest published "Introducing the Pinterest MCP Server" on its business community on 2026-09-22 (via search); feature set, auth and availability not confirmed. A third-party vendor page claimed on 2026-11-08 that no official server exists, so the conflict is open.
- clugtu/pinterest-mcp wraps API v5 (create/update/delete pins, boards, analytics, bulk create). Requires a Pinterest Business account and a registered developer app; Pinterest gates write access behind app review (standard access), so owner action is needed.
- terryso/mcp-pinterest is a headless scraper by its own README. Reject.

### Video and Google Flow / Veo
- kajisho5/ffmpeg-skill: SKILL.md frontmatter is clean (name, description only), no hooks. Tools are stdlib Python scripts calling local ffmpeg/ffprobe; 42 tools incl. captions/karaoke, `fit.py --aspect 9:16`, silence removal, loudness to -14 LUFS, delivery checks. Network: README says "no cloud"; the npm `npx ffmpeg-skill` installer was not inspected, so prefer copying the pinned skill folder into `.claude/skills/` from a reviewed tarball over running npx. SKILL.md links a sibling `color-grading-skill` (not needed).
- hyperframes: HTML-to-video rendering; evaluate later for animated text covers. Dependencies not inspected.
- Google Flow: no official Flow API or MCP was found. gflow-cli drives the owner's logged-in Flow session through Playwright and is self-described as reverse-engineered and subject to Google's ToS. Recommended: owner uses interactive Flow; studio generates prompts and shot lists, then ingests downloaded clips. Veo through the Gemini API is a separately billed option (pricing from third-party sources only; Google's pricing page not opened). Egypt availability for Flow and the Veo API not confirmed.

### QA
- chrome-devtools-mcp (official Chrome team, Apache-2.0) for rendering storefront and listing previews at 375/430/768/1440 px, console and network audit. Playwright plugin is also in the official marketplace as an alternative.

## Print PDF packages (exact dimensions, cut/fold lines, calibration marks)

| Package | Role | Latest seen | License | Status here | Notes |
|---|---|---|---|---|---|
| reportlab | Primary vector page builder: exact page sizes in points (A4 595.28x841.89, Letter 612x792), mm units, dashed fold lines, solid cut lines, registration and 100% calibration squares | PyPI 5.1.0 (installed 5.0.1) | BSD | Installed | Best default; permissive license; full control of line dash, colour, bleed via larger page box. |
| pypdf | Merge, set TrimBox/BleedBox/MediaBox, metadata, page checks | PyPI 7.1.0 (installed 6.17.0) | BSD-3-Clause | Installed | Use for post-processing and box verification. |
| pikepdf | Low-level PDF edits on qpdf, repair, linearize | PyPI 10.18.1 | MPL-2.0 | Missing | Optional; useful for structural validation. |
| PyMuPDF (fitz) | Render pages to PNG for QA, measure drawings, extract vectors | PyPI 2.1 | AGPL-3.0 or Artifex commercial | Missing | Fine for internal QA tooling; avoid embedding in anything distributed. pdftoppm (poppler) is already present for rasterized QA. |
| cairosvg | SVG to PDF/PNG conversion | PyPI 2.9.1 | LGPL-3.0-or-later | Missing | Good for SVG-authored artwork; needs system cairo. Check unit handling (96 dpi px) when sizing. |
| Inkscape (CLI) | SVG to PDF with exact mm sizing, text to path, PDF/X-ish exports | unknown | GPL-2.0-or-later | Missing (apt) | Use as a tool, not a library, so GPL does not affect output files. Heavier install. |
| Ghostscript | PDF/X conversion, preflight, font embedding checks | unknown | AGPL-3.0 (or commercial) | Missing | Optional preflight only. |
| qpdf | Structural check (`qpdf --check`) | unknown | Apache-2.0 | Missing | Lightweight validator. |

Recommendation: reportlab for generation, pypdf for box setting and verification, pdftoppm for 300 dpi raster QA (already present). Add pikepdf and qpdf for validation if needed; add cairosvg or Inkscape only if artwork is authored in SVG.

## Recommended install set

Project scope, pinned, after reading the referenced files:
1. Official marketplace plugin `chrome-devtools-mcp` at pin `a878bcad39584337e055778353246820deafa7c0` (visual QA).
2. `kajisho5/ffmpeg-skill` copied into `.claude/skills/ffmpeg-skill/` from npm 3.8.12 tarball after reviewing `scripts/` (local FFmpeg video pipeline).
3. Etsy OpenAPI Dev MCP (docs only, no key) once the official install command is read on developer.etsy.com.
4. Python: keep reportlab and pypdf (present); optionally add `pikepdf==10.18.1` and system `qpdf` for PDF validation.
5. Optional: official `canva` plugin at pin `bfcbc681560f6031e9949ea52f81e20beb87e39e` for its skills (connector already active).
6. Optional: anthropics/skills `document-skills` only if a project-pinned copy is preferred over the existing user-level pdf skill.

Do not install: gflow-cli, terryso/mcp-pinterest, vicampuzano/metricool-mcp endpoint, rmarescu/gumroad-mcp (archived), administrativetrick/etsy-mcp-server, Canva Dev MCP.

## Requires owner action

| Item | Owner action | Spend |
|---|---|---|
| Etsy shop management MCP (Bl0ck154 hub, fallback mofiaboss) | Register Etsy developer app, choose app tier, authorize OAuth PKCE with listings_r/listings_w and shops scopes; start in `ETSY_MCP_READ_ONLY=1` | Etsy listing fees on publish only |
| Metricool official MCP | Create Metricool account, connect Instagram, TikTok, YouTube, Pinterest profiles, add connector in Claude | Free plan supported (via search); paid plan optional |
| Pinterest | Business account; read the official Pinterest MCP page; if using clugtu/pinterest-mcp, register app and request API access | Free |
| Gumroad | Create access token for read-only analytics (stcmain/gumroad-mcp); product uploads stay manual | Gumroad fees on sales |
| Payhip | Manual product upload; optional API key for coupons/webhooks | Payhip fees on sales |
| Google Flow / Veo | Confirm which Flow plan is available in Egypt; run Flow interactively and export clips. Veo API only with explicit spend approval | Flow credits; Veo API billed per second |
| Shopify / Whop | Already connected; any product creation or publishing needs explicit approval | Platform fees |
| Network allowlist | Allow developer.etsy.com, developers.pinterest.com, help.metricool.com, www.canva.dev and ai.google.dev if the next session must verify official docs directly | None |
| GitHub repo access | Attach candidate repos (read) if exact commit SHAs must be recorded before install | None |

## Open questions
- Exact Etsy Dev MCP install command and package name.
- Whether Pinterest's official MCP supports organic pin creation and who can use it.
- Metricool MCP license and current release on GitHub (repo not reachable here).
- Official Etsy digital file size and count limits.
- Flow and Veo API availability for an Egypt-based account.
