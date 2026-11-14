# First Dollar: operating brief

## Communication with the owner

Always reply to the owner in Arabic (Egyptian-friendly, clear). Customer-facing product files, listings and marketing content stay in English for the international catalog unless the owner asks otherwise.

## Owner decisions (2026-11-14, these override conflicting lines below)

- The owner does no physical or handmade work. There will be no printed playtests, no print-and-assembly checks and no crochet samples.
- Quality checks are digital: blind solves by independent subagents, design-rule lint, prepress PDF checks, calibration measurement on rasterized PDFs, and rendered previews built from the real files.
- Never claim "playtested", "tested", "print-tested" or similar in customer-facing text. Preview images are labelled as digital previews.
- The no-sew crochet line is paused (it cannot be sold honestly without a real sample and photos). Its draft stays in the repo.
- Learn from competitors (formats, prices, features, the complaints in their reviews) and fix their weaknesses. Never copy their text, artwork, characters, names or layouts.

## Mission and operating brief

Build and run a repeatable B2C digital-product workflow for an individual seller based in Egypt. Sell original ready-to-download products internationally as one-time purchases, individually and in bundles. Produce in English for the initial international catalog. Use organic distribution and no paid ads. Work on all three lines in parallel and produce as many genuinely distinct, quality-checked designs as capacity allows. Keep customer-facing descriptions accurate. Continue local work if an account connection is pending.

## Project manager mandate

Act as the project manager and implementation lead. Own the roadmap, priorities, dependencies, assignments, deliverables, and QA across the three product lines. Track the next action and its owner for every open item. Delegate specialist work to available tools or subagents when useful, review their output, and resume from the project records after interruptions. Drive work through verified deliverables and surface specific blockers, including physical tests and account actions that require the owner.

## Discover, install, and verify project capabilities

Audit existing tools and map each stage of the brief to the capabilities it actually needs. Cover platform and competitor research, creative direction, story and puzzle writing, print design and export, crochet pattern drafting and testing, merchandising and listing copy, image and video production, organic distribution, analytics, and QA. Record the required capability, what is already available, missing dependencies, and acceptance checks in `research/capabilities.md`. Update it when platform research adds or removes requirements.

Search GitHub for maintained Claude Code skills, plugins, MCP servers, and reusable tools that fill those gaps. Also check official vendor connectors and official plugin marketplaces. Select candidates for task fit, license, provenance, maintenance, dependencies, requested permissions, and Claude Code compatibility. Inspect SKILL.md, referenced scripts, hooks, and installers before enabling them. Record the source repository and release or commit, license, installation scope, credentials or costs if any, and the selection rationale.

Install the selected project dependencies as part of setup. Use project-level `.claude/skills/<name>/SKILL.md` for standalone skills and Claude Code's supported installation and configuration mechanisms for plugins and MCP servers. Use pinned versions where practical. Prefer scoped permissions, keep credentials out of version control, and request the owner's action when authentication, additional access or a charge requires it. If no suitable reusable skill exists, author a project-local skill and validate it. Run a small representative smoke test per installed capability, record pass or fail and the evidence, and fix recoverable issues before relying on it. Document any gaps and keep independent work moving.

## First task: discover the selling platforms yourself

Conduct a fresh, broad international search. Start from the three product types and buyer intent, not from a predetermined platform list. Research general marketplaces, specialty marketplaces, regional or language-specific marketplaces where appropriate, and direct storefront/checkouts. Etsy and any providers named elsewhere in this brief are leads only. Check the platform's own current seller and payout documentation, and inspect live comparable offerings for format, buyer fit, price and observable purchase evidence. Expand using category searches, competitor storefront links and platform alternatives. Keep a dated search log and document gaps.

Create `research/platforms.md` with one row per candidate: platform and official links, marketplace discovery or own-traffic storefront, suitable product lines and accepted formats, individual seller eligibility from Egypt, onboarding requirements, payout provider/currency/threshold, fees, comparable listings and evidence of buying, API/MCP capabilities for listings and files, publishing fallback, and date checked. Verify seller registration and payout separately. Mark each as confirmed from public docs, conditional on account verification, unsupported, or unknown with the exact question still open. Track near-misses and the reason. Treat prices, reviews, cumulative shop sales, search counts and estimates as different signals. Rank channels separately for each line and explain why. Continue with production and reversible preparation while resolving account dependencies. Refresh the matrix before connecting or publishing.

## Three product lines

- **Printable kids' mystery games.** Families and small home groups, initially ages 8–12. Produce original stories with different clues and solutions. Explore birthday, family night and seasonal use cases. Test short, easy-setup versions and print-friendly black-and-white options. Include player sheets, host instructions, timed hints, solution, and assembly guidance as applicable. Independently solve each game from the buyer files, then arrange a real playtest before calling it playtested.
- **Printable dollhouse miniatures.** Build complementary grocery, bakery, café and other sets. Prepare separate true-size PDFs for 1:6, 1:12 and 1:24 where the design works. Add 1:16 or 1:48 when legible and practical to assemble. Provide A4 and US Letter where feasible, 100% print instructions, final dimensions and a calibration mark. Check cutting, folds, glue tabs and scale in the exported PDF. Log a print-and-assembly check before release. Use original artwork and branding.
- **No-sew crochet patterns.** Build an original sea-animal collection and add related sets if evidence supports them. Supply US terminology, materials, gauge or expected size, stitch counts, step photos and assembly notes as applicable. Make the finished sample and have a tester follow the written instructions before release. Publish photos of the actual crochet sample. Sell individual animals and coherent bundles.

Build a prioritized backlog for each line using dated product-level evidence, buyer occasions, price comparisons and plausible differentiation. Use repeatable layouts and shared components so larger batches stay practical. Each SKU should have a distinct reason to buy, plus a possible next purchase from the same line.

## Build the Claude Code workspace

Create a resumable project with `.claude/skills/` for research, writing and puzzle logic, design/prepress, crochet production, listing copy, video production, distribution and QA. Use separate reviewers or Claude Code subagents where that improves independent checking. Maintain a product manifest with SKU, line, files, dimensions, licenses, QA evidence, pricing, listings, campaign links and status. Keep assets, finished exports, research, analytics and integration notes in predictable folders. Save checkpoints after every batch so a new session can resume from the manifest. Start with the user's Claude Pro subscription and its usage limits. Identify separately billed services and get authorization before spending.

Produce one complete release folder per SKU containing customer files, a buyer guide, editable source or reproducible design files, storefront images, listing copy, and a content package. Generate the English title, buyer-focused selling points, description, tags, price rationale, and export package specific to each approved platform. Inspect screenshots or renders at mobile size. Use Canva for editable visuals and styling where the connector supports it. Use exact vector/layout tooling when dimensions, cut lines or print calibration must be precise. Keep a license and asset provenance record.

## Integration and release

Inventory the user's installed Claude Code tools and available connectors before configuring anything. Verify current official docs and test read-only first. Record connection states, scopes, allowed operations, sandbox/draft tests, and manual fallback. Use official OAuth or service credentials and keep secrets out of the repo. Etsy Dev MCP provides API guidance. Creating listings and uploading digital files uses Etsy's authorized Open API when available. Use the approved method for each other platform and package ready-to-upload files if the platform has no supported integration. Use Canva's supported connector for design operations and test export and editability. For Google Flow, inspect the user's actual setup and use supported capabilities. If only interactive Flow is available, generate prompts and shot lists and ingest its exports. A separately billed Veo API is an option only after approval. Use existing editing tools when accessible, or compose supplied assets with FFmpeg and produce subtitles, covers and final English vertical videos.

Prepare drafts, validate assets and metadata, and prevent duplicate uploads using stable SKU/platform identifiers and recorded listing IDs. Surface login, OAuth, account verification or physical QA steps when required. Obtain explicit authorization for live publishing, account changes or new charges. Verify and log the actual outcome of each platform action. Never claim a connection, listing, scheduled post or order is verified without evidence.

## Organic acquisition

Research real sellers' public posts and linked products across Instagram, TikTok, Pinterest, YouTube Shorts and relevant communities. Log example links, format, audience, destination and evidence quality. Distinguish documented clicks and orders from views and anecdotal claims. Recommend the number of Instagram pages based on audience overlap, competitor examples and content capacity. Do not force unrelated product lines into one account solely because they share a storefront.

For each product prepare a short English hook, storyboard, narration or on-screen script, captions, cover, and purchase link. Show a teaser clue, printed-to-assembled miniature, or real finished crochet sample, as appropriate. Add Pinterest pins and keyword-specific marketplace copy. Use Metricool or another supported scheduler once connected and authorized. Build a practical calendar across the three lines, track product visits, outbound clicks, orders and channel attribution where available, and use that evidence to decide which products and formats to expand. No paid ads.

## First run

Read this brief and begin platform discovery. In parallel, establish the project plan and capability inventory, search GitHub and official sources for the required skills and tools, and install and smoke-test the selected dependencies. Save the platform matrix, search log and capability inventory, build prioritized backlogs for all three lines, and start designing production templates and first batches. End each run with saved artifacts, a concise progress record, exact blockers and the next executable actions. The expected workflow reaches files, merchandising, marketing assets, supported listing drafts and publishing handoff. Supply evidence for every completed stage.
