# Integrations and connection states

Checked 2026-11-14. Never record secrets here. Live publishing, account changes and spend need explicit owner approval each time.

| Service | Purpose | State (evidence) | Scopes / allowed ops | Draft or sandbox test | Manual fallback |
|---|---|---|---|---|---|
| Canva (official connector) | Editable marketing visuals | Connected; `list-brand-kits` returned an empty list (read-only test PASS) | design create/edit/export available; not yet used | Next: create one pin design from the storefront hero, export PNG, confirm editability | Pillow-generated images in storefront/ |
| Whop (official connector) | Possible own-traffic checkout | Connected as a user, admin profile, no business account selected (`connection_status`) | Very broad (payments, payouts, products). Use read-only until the owner approves a Whop store | none | n/a |
| Shopify | (unrelated store) | Needs re-authentication; the connected store belongs to a separate business | Do NOT use for First Dollar without explicit approval | none | n/a |
| Google Drive | Asset handoff to owner (e.g. phone footage) | Listed, not tested | | Next: list recent files read-only | Commit to repo / upload to chat |
| Etsy Open API v3 | Draft listings + digital file upload | Not connected: needs Etsy shop, developer app (keystring) and OAuth by the owner | listings_w, listings_r (when created) | Create listing in draft state only, record listing_id in manifest | Manual upload using listing.md + file plan |
| Etsy Dev MCP | API guidance | Not installed (install command unconfirmed: developer.etsy.com blocked) | docs only | | Read docs in browser |
| Metricool MCP | Scheduling + analytics | Not connected (owner OAuth) | | | Ready-to-post packages in content/ |
| Pinterest API | Pin publishing | Not connected (owner business account + app) | | | Manual pin upload |
| Google Flow / Veo | Video generation | Owner setup unknown; Veo API is billed (approval needed) | | | Prompt + shot lists; FFmpeg composition of real footage |
| Payhip / Gumroad / Lemon Squeezy / Ravelry / LoveCrafts | Storefronts | No write integration exists | | | Upload checklists per platform (to write when the platform is approved) |

Duplicate-upload guard: stable IDs are `<SKU>@<platform>`; record listing_id in `products/manifest.csv` `listings` column immediately after any create call, and check it before any create.
