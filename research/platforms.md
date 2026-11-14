# Sales platform discovery: digital downloads from Egypt to international buyers

- Date checked: 2026-11-14 (every row below was checked on this date)
- Seller profile: individual seller resident in Egypt, one-time digital purchases (single items and bundles), English-speaking international buyers.
- Product lines:
  1. Printable kids' mystery party games (PDF, ages 8-12)
  2. Printable dollhouse miniatures (true-size PDFs at 1:6, 1:12, 1:24)
  3. No-sew crochet patterns (PDF, sea animals)

## Method and limits

- Started from buyer-intent searches per product line ("kids mystery party game printable", "printable dollhouse miniatures 1:12 PDF", "no sew crochet octopus pattern"), then expanded through category pages and competitor storefront links (Payhip, Gumroad, Ravelry, Ribblr, Night of Mystery, My Mystery Party, Pattern by Etsy).
- Platform eligibility, payout, fee and API claims were checked against each platform's own help center, developer docs or policy pages.
- Tooling gap (important): direct page fetching was blocked by this session's network allowlist for every external host tried (help.etsy.com, www.etsy.com, gumroad.com, docs.lemonsqueezy.com, help.payhip.com, www.ravelry.com). GitHub access to the open-source Gumroad repo was also denied. All official-doc claims below therefore come from the search engine's indexed text of the cited official URL, not from a live page load. Whop is the exception: its docs were read directly through the Whop docs MCP tool.
- Marketplace listing evidence comes from search-result snippets of live listing and category pages. Listing pages could not be opened, so counts are as indexed, may be stale, and each must be rechecked before use.

### Status labels used

- **CONFIRMED** = confirmed from public docs (URL given; indexed text unless marked "read directly")
- **CONDITIONAL** = public docs allow it, but it depends on the owner's own account verification or settings
- **UNSUPPORTED** = public docs say it is not possible
- **UNKNOWN** = not established; the exact open question is stated

### Evidence signal types (kept separate)

- **[LP]** listing price shown on the listing or in search snippets
- **[LR]** review count on a single listing
- **[SS]** cumulative shop sales (whole shop, all products)
- **[SC]** search or category result counts
- **[3P]** third-party estimates (none used for demand in this file)

---

## Cross-cutting Egypt payout facts

| Rail | Finding | Status |
|---|---|---|
| Stripe (direct account) | Egypt is not on Stripe's self-serve country list. Stripe docs mention Egypt only for Stripe Tax and as a Global Payouts recipient country (EGP), which is a platform-to-recipient product, not a merchant account. Third-party guides say Stripe is not supported in Egypt. Any platform that requires the seller's own Stripe account is blocked. | UNSUPPORTED for a direct Stripe account: https://stripe.com/global ; https://docs.stripe.com/global-payouts/recipient-countries |
| Payoneer | Etsy's own help pages name Egypt as a Payoneer country for Etsy Payments, USD deposits into Payoneer, then withdrawal to a local bank. Payoneer's Egypt withdrawal fee schedule was not found in public docs (generic pages say "up to 2%" or "up to 3%" for conversion withdrawals, conflicting). | CONFIRMED for Etsy route: https://help.etsy.com/hc/en-us/articles/16999319005207 ; withdrawal fee UNKNOWN: https://www.payoneer.com/pricing/ |
| PayPal (Egypt account) | PayPal Egypt pages describe receiving money and withdrawing to an Egyptian bank (up to 7 business days; withdrawal fee shown as 125.00 EGP on one page and 79.00 EGP on another). Egypt is in PayPal's Middle East and Africa conversion group (3.0% to convert received balances). Exact Egypt commercial receiving rate not shown in indexed text. | CONDITIONAL (owner must confirm the account can receive goods-and-services payments): https://www.paypal.com/eg/cshelp/article/how-do-i-withdraw-money-to-my-bank-account-help394 ; https://www.paypal.com/eg/business/paypal-business-fees |
| PayTabs / Paymob (regional) | Payhip lists PayTabs covering Egypt (from 2.25% per transaction). Paymob has an embedded Shopify integration for Egypt. | CONDITIONAL: https://help.payhip.com/article/372-connect-your-paytabs-account ; Paymob/Shopify per press coverage only |

---

## Candidate matrix (per-platform subsections)

### 1. Etsy (marketplace discovery)

- Official links: https://help.etsy.com/hc/en-us/articles/115015710408 (eligible countries), https://help.etsy.com/hc/en-us/articles/16999319005207 (Payoneer), https://www.etsy.com/legal/etsy-payments/ (payments policy), https://help.etsy.com/hc/en-us/articles/360035902374 (fee basics), https://help.etsy.com/hc/en-us/articles/115015628347 (digital listings), https://developers.etsy.com/documentation/tutorials/listings/ (API)
- Discovery type: marketplace discovery (strongest buyer intent of all candidates for all three lines).
- Suitable lines and formats: all three. Instant download, up to 5 files per listing, 20MB per file (CONFIRMED, digital listings article). Large true-size multi-scale sets may need splitting or ZIP.
- Egypt individual seller eligibility: Egypt is listed among countries that use Etsy Payments with a Payoneer Payment Account. **CONFIRMED** (URLs above). Note: the two Etsy help pages give slightly different country lists, but both include Egypt.
- Onboarding: Etsy Payments enrollment through Payoneer; Payoneer performs identity verification; respond within 30 days; bank account must be in the same country as the Payoneer registration; name/address/date of birth must match ID. One-time shop set-up fee that "varies by location" (amount for Egypt UNKNOWN; India example is USD 10). **CONDITIONAL** on account verification.
- Payout: Payoneer, deposits in USD only, then withdraw to an Egyptian bank (Payoneer minimums and fees apply). **CONFIRMED** route; Payoneer threshold and Egypt withdrawal fee **UNKNOWN**.
- Fees: USD 0.20 listing fee per listing (CONFIRMED, fee basics); 6.5% transaction fee on order total (CONFIRMED); payment processing fee for Egypt 6.5% + USD 0.30 per order, exclusive of VAT, assessed on gross order (CONFIRMED, payments policy). Combined headline about 13% + USD 0.30 + listing fee, before Payoneer withdrawal costs. Currency conversion fee applies if listing currency differs from payment account currency (list in USD).
- Comparable listings and buying evidence (search snippets of etsy.com, 2026-11-14):
  - Line 1: "Printable Murder Mystery Style Game for Kids, Birthday Mystery Party Game, Detective Party..." (listing 4302983274): [LR] 161 reviews, [LP] USD 8.28 sale price. A "Missing Birthday Cake" printable kit, ages 7-12: [LP] USD 7.99, [LR] 120 reviews. Others: [LP] USD 6.95 (8 clues, ages 8-12), [LP] USD 2.19 on sale, [LP] about USD 8 (18 puzzles, 45-60 min), escape-room style [LP] USD 9.74; family Christmas mystery ages 8+ [LP] USD 15.44; personalized kits for up to 20 kids [LP] USD 109.00 and USD 134.60. No bestseller badge visible in snippets.
  - Line 2: printable dollhouse shops showing [SS] 29.2k sales with 5.0 (10.5k reviews), [SS] 13k sales with 4.8 (2.7k), [SS] 39.4k sales (11 years). Book cover listings [LR] 78 and 54 reviews. [LP] range about USD 0.50 to 15.54; English Cottage kit [LP] USD 8.55; armchair PDF kits [LP] USD 5 to 6.50. Multi-scale listings (1:6, 1:12, 1:24) exist; 1:24 often delivered as "print at 50%".
  - Line 3: ChassityAnnDesigns26 (no-sew sea turtle) [SS] about 47.7k sales, 4.9 from 5.1k shop reviews, listing flagged by Etsy as high sales volume in past 6 months; AlterEgoCrochet (no-sew whale) [SS] about 47.3k sales, 4.9 from 5.9k; GreenFoxFarmsDesigns [SS] about 11.9k; no-sew squid listing [LR] 1,462 reviews at 4.9; whale/narwhal/dolphin set [LR] 676 reviews at 3.5 (quality warning). Single no-sew octopus patterns [LP] about USD 2.94 to 3.99. One bundle shows conflicting counts (92 visible vs 26,046 in structured data): treat as unresolved.
- API/MCP: Open API v3 supports createDraftListing with type "download", then uploadListingFile (POST /v3/application/shops/{shop_id}/listings/{listing_id}/files) with listings_w scope and x-api-key. **CONFIRMED** (listings tutorial). App access tiers: own-shop app with automated approval vs Personal and Commercial access with manual review (tier details from indexed docs and third-party guides; exact current tier rules **CONDITIONAL**). Etsy Dev MCP server (https://mcp.api.etsycloud.com/mcp) is a docs/schema helper only; it does not call the API or change a shop. **CONFIRMED**: https://developers.etsy.com/documentation/mcp_server/devmcpserver/
- Publishing fallback: manual listing in Shop Manager (always available).
- Date checked: 2026-11-14

### 2. Teachers Pay Teachers (TPT) (marketplace discovery, education niche)

- Official links: https://www.teacherspayteachers.com/University/Payout
- Discovery type: marketplace discovery (teachers, homeschool, party use).
- Suitable lines: Line 1 strongly (classroom mysteries, escape rooms for grades 3-6). Line 2 weak. Line 3 not a fit.
- Egypt eligibility: payouts run through Hyperwallet; options "depend on your country" (direct deposit, PayPal, Venmo, wire). Egypt not named in indexed text. **UNKNOWN**: does TPT accept seller accounts from Egypt, and which Hyperwallet method (PayPal or wire) is offered for Egypt?
- Onboarding: seller account plus US tax form (W-8BEN for non-US individuals expected; not confirmed for TPT in indexed text). **UNKNOWN**.
- Payout: Hyperwallet; US per-payout fees USD 0.05 PayPal, USD 0.40 direct deposit; international fees vary and are visible only inside Hyperwallet. **CONFIRMED** for US fees; Egypt **UNKNOWN**.
- Fees: fee structure changed in 2026: Premium Seller closed to new members 2026-10-01; new "Exclusive Seller" tier requires selling only on TPT. Basic payout share reported as 55% plus a per-resource fee (third-party, conflicting with older 60% figures). **UNKNOWN** until TPT's own fee page is read. Exclusivity would conflict with Etsy/own-store sales, so Basic is the only compatible tier.
- Comparable listings: Murder Mystery Escape Room (ages 8-12, 12 puzzles), Operation Missing Trophy (grades 3-6), Case of the Missing Christmas Candy (ages 6-12), Detective Escape Room (ages 7-12). Prices and ratings not captured in snippets (gap).
- API/MCP: no public seller API found. **UNKNOWN** (no evidence of one).
- Publishing fallback: manual upload.
- Date checked: 2026-11-14

### 3. Ravelry (specialty marketplace, crochet)

- Official links: https://www.ravelry.com/help/search?query=selling+patterns
- Discovery type: marketplace discovery inside the largest knit/crochet pattern database; designers can also use buy-now links on their own sites.
- Suitable lines: Line 3 only. PDF patterns.
- Egypt eligibility: no country restriction found; PayPal is the only payment processor and designers must also pay Ravelry invoices by PayPal. **CONDITIONAL** on an Egypt PayPal account that can receive commercial payments.
- Onboarding: Ravelry Pro (free designer tools) and PayPal connection in Pattern Sales settings. **CONFIRMED** (help search page).
- Payout: paid directly into PayPal at checkout; PayPal Egypt withdrawal to bank. **CONDITIONAL**.
- Fees: tiered monthly fee by sales; third-party sources say none under about USD 30/month and 3.5% between USD 30 and 1,500; fee table is behind login. **UNKNOWN** (exact current tiers); PayPal fees extra.
- Comparable listings: many free no-sew octopus patterns (Mini Octopus by Tidzhen Gyuldzhu, rated 4.9 from 10 votes; No-Sew Bubbles the Octopus, free). Paid: Plush Octopus EUR 2.98 [LP], Amigurumi Crochet Octopus USD 2.20 [LP], Cuddle Octopus USD 4.00 [LP], Wheat Stitch Octopus USD 9.16 [LP]. Sales counts not public on Ravelry (gap); project counts not captured.
- API/MCP: Ravelry has an API (not verified for pattern store uploads in this pass). **UNKNOWN**: does the Ravelry API allow creating a pattern store listing and uploading the PDF?
- Publishing fallback: manual upload.
- Date checked: 2026-11-14

### 4. LoveCrafts independent designer program (specialty marketplace, crochet)

- Official links: https://lovecrafts.com/en-gb/c/article/designer-handbook-payment-pricing-taxes ; https://www.lovecrafts.com/en-us/c/article/designer-handbook-getting-started
- Discovery type: marketplace discovery (yarn retailer audience).
- Suitable lines: Line 3.
- Egypt eligibility: no country restriction found in indexed text. **UNKNOWN**: is an Egypt-resident designer accepted?
- Onboarding: designer account; patterns cannot publish without PayPal billing details. **CONFIRMED**.
- Payout: PayPal, in GBP, USD or EUR depending on pricing preferences. **CONFIRMED** (handbook); Egypt PayPal receipt **CONDITIONAL**. Monthly in arrears on the 25th per third-party source (**UNKNOWN** officially).
- Fees: tiered (third-party: about 4% + USD 0.35 under USD 40/month, 5% from 40 to 1,500). **UNKNOWN** officially. LoveCrafts handles VAT. **CONFIRMED**.
- Comparable listings: none surfaced for no-sew sea animals in search (gap).
- API/MCP: none found. **UNKNOWN**.
- Publishing fallback: manual upload.
- Date checked: 2026-11-14

### 5. Creative Fabrica (marketplace discovery, crafts)

- Official links: https://help.creativefabrica.com/hc/en-us/articles/360029930872 (payouts); https://www.creativefabrica.com/open-store/ ; https://www.creativefabrica.com/designers-terms-conditions-v1-5
- Discovery type: marketplace plus subscription pool.
- Suitable lines: Line 3 (crochet toy patterns are sold there), possibly Line 2 (paper crafts). Line 1 weak.
- Egypt eligibility: designer application required; no country restriction found. **UNKNOWN**: Egypt acceptance.
- Payout: PayPal, Payoneer or bank transfer; bank transfer has USD 20 handling fee and USD 100 minimum; Payoneer requires adding Creative Fabrica as a funding source. **CONFIRMED** (payout article). Payoneer makes this one of the cleaner Egypt rails, **CONDITIONAL** on acceptance.
- Fees: designer share 50% of net price for single sales per current terms; subscription earnings via point pool. **CONFIRMED** (terms v1.5, indexed). Broad non-exclusive perpetual license granted to Creative Fabrica.
- Comparable listings: crochet toy pattern listings exist; no sales counts captured (gap).
- API/MCP: none found. **UNKNOWN**.
- Publishing fallback: manual upload.
- Date checked: 2026-11-14

### 6. Gumroad (own-traffic storefront, small Discover marketplace)

- Official links: https://gumroad.com/help/article/13-getting-paid ; https://gumroad.com/help/article/223-payoneer-and-gumroad ; https://gumroad.com/pricing ; https://gumroad.com/api
- Discovery type: mostly own traffic; Discover marketplace exists (30% fee).
- Suitable lines: all three; competitors present (dollhouse sofa template USD 3.95 [LP]; crochet patch pattern "A012" 152 sales [SS-listing level, shown as sales count]).
- Egypt eligibility: Gumroad's getting-paid table lists Egypt with payout currency EGP. **CONFIRMED** (indexed). Risk flag: a public Gumroad GitHub issue (antiwork/gumroad #2164, about a year old) proposes enabling PayPal payouts for Egypt "to circumvent the current bank payout issues"; whether resolved is **UNKNOWN** (GitHub not reachable from this session).
- Onboarding: payout settings with local bank details and identity info. **CONDITIONAL**.
- Payout: direct bank deposit in EGP to a local Egyptian bank; minimum USD 100 (no higher Egypt minimum shown); 7-day hold on scheduled payouts; Payoneer and Wise not supported; PayPal fallback only where bank payouts unavailable. **CONFIRMED** (indexed) but **CONDITIONAL** on the bank issue above.
- Fees: 10% + USD 0.50 per direct sale; 30% on Discover sales; card/PayPal processing included or extra per help article (conflicting versions). **CONFIRMED** headline (pricing page).
- API/MCP: API v2 can list, update, enable/disable products; create-product endpoint is contested (one docs mirror says POST /v2/products is not implemented and returns 404); no file upload endpoint found. Community MCP servers (keithah, rmarescu) are read/enable/disable only. **UNKNOWN** for create and file upload; treat as manual.
- Publishing fallback: manual dashboard upload.
- Date checked: 2026-11-14

### 7. Lemon Squeezy (own-traffic checkout, merchant of record)

- Official links: https://docs.lemonsqueezy.com/help/getting-started/supported-countries ; https://docs.lemonsqueezy.com/help/getting-started/fees ; https://docs.lemonsqueezy.com/help/getting-started/activate-your-store ; https://docs.lemonsqueezy.com/api/files
- Discovery type: own traffic only (no marketplace).
- Suitable lines: all three; files up to 5GB total per product.
- Egypt eligibility: Egypt listed under supported bank payout countries (and PayPal payouts cover 200+ countries). **CONFIRMED** (indexed text of supported-countries page).
- Onboarding: store activation questionnaire plus identity verification (government ID), 1-3 business days; KYC/KYB on every store; digital goods it fulfils are generally approved. **CONDITIONAL**.
- Payout: bank payout (1% per payout outside US) or PayPal (3% capped at USD 30 outside US). Currency for Egypt bank payouts **UNKNOWN**.
- Fees: 5% + USD 0.50 per transaction; +1.5% international (non-US) transactions; +1.5% PayPal. Merchant of record: collects and remits sales tax/VAT. **CONFIRMED**.
- Platform risk: Stripe acquired Lemon Squeezy (2024) and is steering merchants toward Stripe Managed Payments, which reportedly lacks digital file delivery. **UNKNOWN** long-term availability.
- API/MCP: API exposes Files as read (retrieve) objects attached to variants; no create-product or file-upload endpoint found. **UNKNOWN**, treat as manual.
- Publishing fallback: manual dashboard upload.
- Date checked: 2026-11-14

### 8. Payhip (own-traffic storefront)

- Official links: https://help.payhip.com/article/65-connecting-your-stripe-account ; https://help.payhip.com/article/64-how-do-i-sell-physical-products (PayPal) ; https://help.payhip.com/article/372-connect-your-paytabs-account ; https://payhip.com/api-reference ; https://help.payhip.com/article/59-adding-a-digital-product
- Discovery type: own traffic (no meaningful marketplace).
- Suitable lines: all three; bundles supported; files up to 5GB each. Competitors present: dollhouse poster sets about USD 2.79 [LP]; crochet designers (e.g. Woolly Thoughts store linked from Ravelry).
- Egypt eligibility: Stripe not usable (Stripe unsupported in Egypt). PayPal "available in all supported locations". PayTabs listed for Egypt. **CONDITIONAL** on PayPal Egypt receiving or PayTabs onboarding.
- Onboarding: connect PayPal (business account needed outside listed personal-account countries) or PayTabs merchant account. First PayPal transaction goes through automatic approval that may delay payout. **CONDITIONAL**.
- Payout: funds settle directly in the seller's PayPal or PayTabs account (Payhip does not hold funds). Currency and threshold set by PayPal/PayTabs. **CONDITIONAL**.
- Fees: Free plan 5% per sale; Plus USD 29/month 2%; Pro USD 99/month 0%; plus processor fees (PayTabs from 2.25%). **CONFIRMED**. Payhip handles EU VAT on digital goods (not rechecked in this pass: **UNKNOWN**).
- API/MCP: API currently covers only Coupons and License Keys; no product creation or file upload. **UNSUPPORTED** (per Payhip API reference, indexed).
- Publishing fallback: manual dashboard upload (only path).
- Date checked: 2026-11-14

### 9. Whop (own-traffic storefront with marketplace; MCP available in this workspace)

- Official links (read directly via Whop docs MCP): https://docs.whop.com/manage-your-business/manage-payouts/set-up-payouts ; https://docs.whop.com/manage-your-business/manage-payouts/payout-methods ; https://docs.whop.com/payments-and-billing/fees/fees ; https://docs.whop.com/developer/guides/direct-file-uploads
- Discovery type: mainly own traffic; Whop marketplace audience skews to communities, courses, software, not kids' printables or crafts.
- Suitable lines: technically all three as file products; weak buyer fit.
- Egypt eligibility: Egypt appears in the supported payout countries list. **CONFIRMED** (read directly).
- Payout: bank, mobile wallet or crypto depending on country; standard up to 5 business days; methods for Egypt shown only in dashboard. Payout fees: next-day ACH USD 2.50 (US), bank wire USD 23.00, crypto 5% + USD 1.00, international local banks "varies by country". **CONFIRMED**; Egypt method and fee **UNKNOWN**.
- Fees: card processing 2.7% + USD 0.30, +1.5% international cards, +1% currency conversion. **CONFIRMED**. Any Whop marketplace/affiliate fee for discovery sales **UNKNOWN**.
- API/MCP: full API including POST /files (presigned upload, multipart to about 50GB) and products/variants create; Whop MCP is connected in this workspace with products_create and files_create tools. **CONFIRMED**. Whether a file can be attached as the delivered download of a product through the API **UNKNOWN** (Create File docs mention legal documents and dispute evidence as attachment targets).
- Publishing fallback: manual dashboard.
- Date checked: 2026-11-14

### 10. Shopify plus Digital Downloads app (own-traffic storefront)

- Official links: https://help.shopify.com/en/manual/products/digital-service-product/digital-downloads ; https://shopify.dev/docs/api/admin-graphql/latest/mutations/filecreate
- Discovery type: own traffic only (Shop app gives minor discovery).
- Suitable lines: all three, bundles via product setup.
- Egypt eligibility: Shopify store sign-up from Egypt is possible (community staff answers reference an Egypt gateway page); Shopify Payments not confirmed for Egypt. Gateways: PayPal Express Checkout (staff answer) and Paymob embedded integration (press). **CONDITIONAL**.
- Payout: via PayPal or Paymob (local EGP settlement); Paymob reportedly restricts some business models. **CONDITIONAL**; Paymob acceptance for international card buyers paying in USD **UNKNOWN**.
- Fees: monthly Shopify plan plus third-party gateway transaction fee (amounts not rechecked in this pass: **UNKNOWN**).
- Formats: Digital Products app allows up to 50 files per variant, 5GB combined. **CONFIRMED**.
- API/MCP: Admin GraphQL (productCreate, fileCreate with staged uploads) **CONFIRMED**; a Shopify MCP is connected in this workspace with create-digital-product, upload-digital-product-file and publish-digital-product tools. Note: the workspace's connected Shopify store belongs to an unrelated business and must not be used; First Dollar would need its own store.
- Publishing fallback: Shopify admin manual upload.
- Date checked: 2026-11-14

### 11. Ko-fi Shop (own-traffic storefront)

- Official links: https://help.ko-fi.com/hc/en-us/articles/360009712917-Ko-fi-Shop-FAQ ; https://help.ko-fi.com/hc/en-us/articles/360009265834-Can-I-use-Stripe-in-my-country
- Discovery type: own traffic (small Explore section).
- Suitable lines: all three, digital downloads with instant access.
- Egypt eligibility: needs PayPal or Stripe; Stripe unavailable in Egypt, so PayPal only. **CONDITIONAL**.
- Payout: directly to seller's PayPal. **CONDITIONAL**.
- Fees: 5% shop fee, or 0% with Ko-fi Gold (price shown as USD 12/month on one page and USD 8 on another). **CONFIRMED** 5%; Gold price **UNKNOWN**.
- API/MCP: webhooks only found; no listing API. **UNKNOWN** (likely none).
- Publishing fallback: manual.
- Date checked: 2026-11-14

### 12. Sellfy (own-traffic storefront)

- Official links: https://sellfy.com/pricing/ ; https://docs.sellfy.com/article/207-selling-digital-products
- Discovery type: own traffic.
- Suitable lines: all three; up to 50 files per product; storage 10GB/15GB/20GB by plan; keep files under 5GB.
- Egypt eligibility: Stripe and PayPal only; "available worldwide" but depends on processor availability. Effectively PayPal-only for Egypt. **CONDITIONAL**.
- Fees: paid plans from about USD 22/month, 0% transaction fee, yearly sales caps (USD 10k Starter). **CONFIRMED**.
- API/MCP: not checked in depth. **UNKNOWN**.
- Publishing fallback: manual.
- Date checked: 2026-11-14

---

## Near-misses and why rejected (or parked)

| Candidate | Why rejected or parked | Status |
|---|---|---|
| Ribblr | Strong crochet audience and visible no-sew sea animal demand (e.g. 6-in-1 No-Sew Marine bundle USD 8.64, no-sew sea turtle USD 2.92-4.25), but staff state "we currently only operate with Stripe", and Stripe is unavailable in Egypt. Also converts patterns to Ribblr's interactive format (no PDF download). | UNSUPPORTED for Egypt payouts unless Ribblr adds another rail: https://meet.ribblr.com/t/new-payment-methods/352034 |
| Stripe-only checkouts (Stan Store Stripe path, Podia Stripe path) | Require a seller Stripe account (Stan uses Stripe Custom accounts in a fixed country list). Stan and Podia offer PayPal as a fallback, but neither has marketplace discovery, so they add little over Payhip. | UNSUPPORTED via Stripe; PayPal path CONDITIONAL: https://help.stan.store/article/217-countries-available-for-stripe-custom-accounts |
| Big Cartel | Digital products now native or via Pulley (USD 6/month); payments via Stripe or PayPal only; no discovery. | Parked, CONDITIONAL on PayPal: https://bigcartel.com/resources/help/article/pulley |
| Amazon (marketplace) / KDP | Amazon does not sell third-party PDF downloads; Kindle ebooks do not preserve true-size printable scale, so Lines 1 and 2 fail. A KDP crochet pattern book is possible later but is a different product. | Rejected for PDF delivery (not researched further) |
| Creative Market | Accepts PayPal only where PayPal can receive; craft patterns and kids' games are not its core design-asset categories; commission and minimum not confirmed. | Parked, UNKNOWN fit: https://support.creativemarket.com/hc/en-us/sections/200249974-Taxes-Payouts |
| Makerist | Crochet pattern marketplace (strong in French and German); no official seller terms or payout data found. | UNKNOWN: commission, payout rail, Egypt eligibility |
| Selar | Africa-focused creator checkout; Egypt not named in its support pages. | UNKNOWN: Egypt payouts |
| Polar.sh | Merchant of record using Stripe Connect Express for payouts; Egypt not visible in indexed list; software focus. | UNKNOWN: Egypt in payout list |
| Dodo Payments | Merchant of record, lists Egypt among accepted and grandfathered countries; SaaS focus; fees conflict across sources. | UNKNOWN: Egypt payout eligibility for new merchants |
| Pattern by Etsy | Etsy's own-site add-on (competitor "acasualcottage.patternbyetsy.com" seen). Adds an own-traffic site using the same Etsy Payments rail; monthly fee not rechecked. | Parked as later add-on to Etsy |
| Night of Mystery / My Mystery Party | Direct competitors in Line 1 with their own stores (kids kits for ages 8-12, tiered by guest count); not platforms the seller can sell on. | Competitor reference only |

---

## Per-line channel rankings

### Line 1: Kids' mystery party games (PDF, ages 8-12)

1. **Etsy**: clearest live demand ([LR] 161 and 120 reviews on comparable kits at [LP] about USD 7-8), Egypt payout rail confirmed through Payoneer. Main cost is about 13% + USD 0.30 per order plus Payoneer withdrawal.
2. **Teachers Pay Teachers (Basic tier)**: classroom and homeschool mystery and escape-room demand for grades 3-6 exists; adds a second discovery audience. Ranked second only if Egypt Hyperwallet onboarding works. Avoid the new Exclusive tier because it bars selling elsewhere.
3. **Lemon Squeezy or Payhip as own-traffic checkout** (for Pinterest/social traffic and bundles): Lemon Squeezy has Egypt bank payouts listed and handles tax but carries platform-transition risk; Payhip has better storefront and bundle tools but depends on PayPal Egypt or PayTabs.

### Line 2: Printable dollhouse miniatures (1:6, 1:12, 1:24)

1. **Etsy**: dominant channel; comparable shops show [SS] 13k to 39.4k cumulative sales and multi-scale listings. The 20MB per file limit matters for high-resolution true-size sheets: plan per-scale files or compressed PDFs.
2. **Payhip**: competitors already sell dollhouse printables there (about USD 2.79 poster sets), bundles across scales are easy; conditional on PayPal or PayTabs.
3. **Gumroad**: competitors present (sofa template USD 3.95); EGP bank payout listed but the open Egypt bank-payout issue must be cleared first.

### Line 3: No-sew crochet patterns (sea animals, PDF)

1. **Etsy**: strongest evidence (no-sew sea animal shops at [SS] about 47k sales; no-sew squid [LR] 1,462 reviews; single patterns [LP] about USD 3-4).
2. **Ravelry**: the default search engine for crochet buyers; many free competing octopus patterns mean a free lead pattern plus paid bundle strategy; payouts PayPal-only, so conditional on PayPal Egypt receiving commercial payments.
3. **LoveCrafts or Creative Fabrica**: LoveCrafts pays by PayPal and handles VAT; Creative Fabrica pays by Payoneer (useful if PayPal fails) but takes a perpetual non-exclusive license. Ribblr would rank here on audience but is blocked by its Stripe-only payouts.

---

## Open questions for the owner's account verification

1. Etsy: what is the one-time shop set-up fee shown for Egypt at onboarding, and does Payoneer enrollment complete for an individual (no business registration)?
2. Payoneer: what is the minimum withdrawal and fee for USD to an Egyptian bank (EGP or USD account), as shown inside the Payoneer account?
3. PayPal Egypt: can the owner's account receive goods-and-services payments from abroad (not only personal transfers), what is the receiving fee, and is the bank withdrawal fee 79 or 125 EGP?
4. Gumroad: in payout settings, does Egypt (EGP bank account) save and pay out successfully today, or does it fail with the "bank payout issues" noted in Gumroad GitHub issue #2164?
5. Lemon Squeezy: does store activation approve an individual in Egypt, and in which currency are Egypt bank payouts sent?
6. Teachers Pay Teachers: can an Egypt resident open a seller account, and which Hyperwallet methods and fees appear for Egypt?
7. Payhip: does the PayTabs option appear in Payment Details for an Egypt-based seller, and does PayTabs onboard an individual (not a registered company)?
8. Ravelry: what are the current pattern-store fee tiers (behind login), and is there any country restriction for designers?
9. LoveCrafts and Creative Fabrica: are designer applications from Egypt accepted?
10. Whop: which payout methods and fees appear for Egypt in the Balances withdraw modal, and can a file be attached as the delivered download through the API?
11. Shopify: if used, would Paymob accept an Egypt individual selling digital downloads to international card buyers in USD, and which store/account would be used (a new, separate store would be needed)?
12. Etsy API: is an own-shop app approved quickly enough for uploadListingFile automation, or should publishing stay manual?

Network note for the next pass: allow help.etsy.com, www.etsy.com, gumroad.com, docs.lemonsqueezy.com, help.payhip.com and www.ravelry.com in the session's network settings so these pages can be fetched directly and the indexed claims re-verified.
