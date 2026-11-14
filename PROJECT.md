# Project plan and status

Updated: 2026-11-14 (end of run 1). PM and implementation lead: Claude. Owner: the seller (account, payment, physical and approval actions).

## Roadmap
| Phase | Goal | Status |
|---|---|---|
| 0 Setup | Workspace, skills, capability inventory, platform matrix | Done (run 1), platform claims need live-page re-check |
| 1 First batch | 1 SKU per line through file QA | Done for mystery + miniatures; crochet is a validated draft |
| 2 Physical QA | Playtest, print-and-assembly, crochet sample + tester | Waiting on owner |
| 3 Channel set-up | Etsy shop (primary for all 3 lines) + one own-traffic checkout | Waiting on owner account checks |
| 4 Listing drafts | Etsy drafts via API or manual upload package | After phase 3 + approval |
| 5 Organic launch | Pinterest + 2 Instagram accounts (minis, crochet), weekly measurement | After first listing is live |
| 6 Scale | Batch 2: Christmas or family-night game, bakery set, octopus | Next run (independent of owner blockers) |

## Channel decision (from research/platforms.md, refresh before connecting)
Etsy ranks first for all three lines (confirmed Egypt eligibility with Payoneer payouts in USD; fees about 13% + USD 0.30 per order before withdrawal fees, search-snippet level). Second channels depend on owner answers: PayPal Egypt commercial receiving decides Ravelry, LoveCrafts and Payhip; Gumroad needs a test payout to an Egyptian bank; Lemon Squeezy lists Egypt bank payouts but has transition risk. Stripe cannot be opened in Egypt, which rules out Stripe-only platforms (Ribblr).

## Open items (next action and owner)
| # | Item | Next action | Owner | Blocks |
|---|---|---|---|---|
| 1 | Etsy shop for Egypt | Start Etsy seller sign-up as an individual; note the set-up fee shown, Payoneer enrollment result | Owner | listings |
| 2 | Payoneer | Check minimum withdrawal and fee to an Egyptian bank | Owner | pricing net margin |
| 3 | PayPal Egypt | Confirm the account can receive goods-and-services payments from abroad, fee, withdrawal fee | Owner | Ravelry, LoveCrafts, Payhip |
| 4 | Network allowlist | Allow etsy.com, help.etsy.com, developer.etsy.com, ravelry.com, payhip.com, gumroad.com, docs.lemonsqueezy.com, help.metricool.com, developers.pinterest.com so claims can be verified on live pages | Owner (environment settings) | evidence quality |
| 5 | MYST-BDAY-01 playtest | Run with 4+ kids aged 8-12; log players, time, hints used, solved?, confusions in products/MYST-BDAY-01/qa/playtest.md | Owner | release |
| 6 | MINI-GROC-01 physical check | Print 1:12 and 1:24 at 100% on 160-200 gsm card; measure bars; assemble 1 box, 1 can, sign; photos; log qa/physical.md | Owner | release, photos, video |
| 7 | CRO-SEA-01 sample | Crochet from source/CRO-SEA-01_pattern_DRAFT.md; weigh yarn; 9 step photos; note unclear steps | Owner | crochet line |
| 8 | Crochet tester | Recruit 1 external tester (e.g. via a crochet community that allows tester calls) | Owner + Claude drafts the call | crochet release |
| 9 | Christmas game decision | Decide by 2026-11-18 whether to build MYST-XMAS-01 for December | Owner (Claude recommends: yes only as a short 30-min version) | seasonal window |
| 10 | Shopify re-auth / use | Shopify connector needs sign-in; it belongs to an unrelated store; First Dollar would need its own Shopify store if Shopify is ever chosen | Owner | none |
| 11 | Canva | Optionally set up a brand kit per line; Claude to run a create/export/edit test | Claude (next run) | editable visuals |
| 12 | Metricool / Pinterest | Connect when the first listing is live | Owner | scheduling |
| 13 | Trademark sanity check of fictional brand names | Quick search before scaling minis line | Claude (next run) | low |
| 14 | Batch 2 production | Bakery set, family-night game, octopus draft | Claude (next run) | none |

## Spend and approvals
No money spent and no account changed this run. Nothing published. Any listing fee, paid plan, Veo API use or live publish needs explicit owner approval at that time.
