# Platform discovery search log

- Date of all entries: 2026-11-14
- Tools: WebSearch (standard and extended modes, often restricted to the platform's own domain), WebFetch (blocked, see below), Whop docs MCP (docs_search, docs_query), gh CLI (blocked).
- No personal information about the seller was used in any query.

## Access gaps encountered

| Attempt | Result | Consequence |
|---|---|---|
| WebFetch help.etsy.com/hc/articles/115015710408 | Blocked: host not in session network allowlist (ENOTFOUND) | Etsy claims rely on search-indexed text |
| WebFetch gumroad.com/help/article/13-getting-paid | Blocked (same) | Gumroad payout table read from index only |
| WebFetch docs.lemonsqueezy.com supported-countries | Blocked (same) | Egypt bank payout claim from index only |
| WebFetch help.payhip.com Stripe article | Blocked (same) | Payhip claims from index only |
| WebFetch www.etsy.com/market/kids_mystery_party_game | Blocked (same) | Listing evidence from snippets only; no live sort by bestseller |
| WebFetch www.ravelry.com pattern search | Blocked (same) | No Ravelry project counts or fee table |
| gh issue view / gh api antiwork/gumroad issue 2164 | GraphQL disabled; REST denied (repo not attached) | Could not read status of Egypt payout issue |
| add_repo antiwork/gumroad (read) | Denied by permission classifier | Same gap; left for owner |

To close these gaps, the owner can allow these hosts in the session network settings: help.etsy.com, www.etsy.com, gumroad.com, docs.lemonsqueezy.com, help.payhip.com, www.ravelry.com.

## Queries and key findings

### Egypt payout rails and platform eligibility

1. "Etsy Payments supported countries list sellers Egypt": Egypt listed in Etsy's Payoneer group (help.etsy.com/hc/articles/115015710408). Two Etsy help pages list slightly different countries; both include Egypt.
2. "Gumroad payout countries supported list PayPal Stripe": Gumroad does not support Payoneer, Wise, wires; bank payout or PayPal only. No country detail.
3. "Lemon Squeezy payout supported countries list Egypt" (standard): official list truncated in snippet; unresolved.
4. "Payhip payouts PayPal Stripe supported countries sellers": 13 processors; Stripe and PayPal in all supported locations; first PayPal sale goes through approval.
5. "Gumroad getting paid countries bank account PayPal not supported countries payout minimum $10" (gumroad.com): current minimum USD 100 (older page said USD 10); local currency only.
6. "Lemon Squeezy supported countries bank payouts PayPal payouts Egypt" (extended, lemonsqueezy.com): index states Egypt is on the bank payout list; PayPal 200+ countries.
7. "Payhip connect Stripe account which countries available; Payhip fees 5% free plan": fees 5% / 2% (USD 29) / 0% (USD 99). No Stripe country list.
8. "Etsy Payments Payoneer countries Egypt help" (etsy.com): USD-only deposits to Payoneer; Egypt processing fee 6.5% + USD 0.30; shop suspended until enrolled (policy as of 2024-01-31).
9. "Gumroad help "Egypt" payout bank PayPal" (extended): Egypt listed with EGP; GitHub issue #2164 "Enable PayPal payouts for Egypt" citing "current bank payout issues"; third-party claims Egypt excluded from PayPal Connect.
10. "PayPal Egypt receive payments withdraw to bank account..." (paypal.com): withdrawals to Egyptian banks up to 7 business days; 125.00 EGP withdrawal fee on one page.
11. "Stripe global availability countries Egypt Stripe account" (stripe.com): Egypt absent from main country list; present for Stripe Tax and Global Payouts recipients only.
12. "Payoneer Egypt withdraw to local bank EGP fees Etsy marketplace" (payoneer.com): no Egypt-specific schedule; generic conversion withdrawal fee "up to 2%" vs "up to 3%" (conflict).
13. "Gumroad Egypt bank payouts paused EGP creators Egypt 2025 2026" (extended): no public pause report found; issue #2164 is the only signal.
14. "Lemon Squeezy Stripe acquisition 2025 2026 Stripe Managed Payments migration supported countries": Stripe Managed Payments public preview Feb 2026; migration path pushed; digital download delivery reportedly missing there (third-party).
15. "Ko-fi shop digital downloads PayPal Stripe supported countries fees 0% Gold" (ko-fi.com): PayPal or Stripe only; 5% shop fee; Gold price conflicting (USD 12 vs 8).
16. "Sellfy payment PayPal Stripe supported countries fees digital products file size limit" (sellfy.com): Stripe/PayPal; 0% fee; plan caps; 50 files per product.
17. "PayPal Egypt can receive payments for goods and services ... fees" (paypal.com): Egypt business fee page exists; catch-all 3.40% + fixed fee likely; withdrawal fee 79 EGP on another page (conflict); 3.0% conversion on received balances.
18. "Stripe not available in Egypt businesses sign up 2026 ...": third-party guides confirm unsupported; workaround is a foreign entity (out of scope for an individual); Paystack Egypt private beta.
19. "Ko-fi PayPal countries Egypt creators receive payments": no Egypt-specific Ko-fi statement.
20. "Payhip payment gateways list PayTabs Paymob Egypt ...": PayTabs covers Egypt (from 2.25%); no Paymob on Payhip.
21. "Dodo Payments supported payout countries Egypt ...": Egypt listed under a grandfathered clause; fees conflict; SaaS focus.
22. "Polar.sh merchant of record supported countries payouts Egypt ...": Stripe Connect Express payouts; Egypt not visible in truncated list.
23. "Lemon Squeezy fees 5% + 50 cents pricing payout fee international": 5% + USD 0.50; +1.5% international; +1.5% PayPal; payout 1% bank outside US, PayPal 3% capped USD 30.
24. ""Egypt" "EGP" Gumroad getting paid bank payouts table minimum": Egypt EGP row with no higher minimum; 7-day hold; instant payouts USD 1 minimum.
25. "Lemon Squeezy store activation identity verification review approval": questionnaire + government ID; 1-3 business days; KYC/KYB.
26. "Shopify available in Egypt payment providers Shopify Payments not available Egypt Paymob PayPal": PayPal Express available per staff answer; Paymob embedded integration; Shopify Payments not confirmed.
27. "Selar creator platform payout countries Egypt digital products": Egypt not confirmed.
28. "Stan Store payouts ... ; Podia payouts supported countries": Stan uses Stripe Custom accounts in a fixed list, PayPal fallback; Podia Stripe/PayPal, no country list.
29. "Big Cartel digital downloads Pulley; Big Cartel supported countries Stripe PayPal": digital products native in new admin or Pulley (USD 6/month); Stripe or PayPal.

### Whop (read directly via Whop docs MCP)

30. docs_query rg "egypt": Egypt present in /manage-your-business/manage-payouts/set-up-payouts.mdx supported country list.
31. docs_search "payout methods supported countries withdraw fees": 200+ countries; bank, wallet or crypto per country; standard up to 5 business days.
32. docs_query /payments-and-billing/fees/fees.mdx: cards 2.7% + USD 0.30, +1.5% international, +1% FX; payout fees: next-day ACH USD 2.50, RTP 4% + 2.50, crypto 5% + 1.00, Venmo 5% + 2.50, wire USD 23.00, international local banks varies.
33. docs_search "sell digital downloads files app upload PDF file size limit": POST /files with presigned single or multipart upload (to about 50GB); attachment targets documented are legal docs and dispute evidence, product delivery attachment not confirmed.
34. docs_query for marketplace/discover fees: only ledger line types (marketplace_affiliate_fee) found; no published rate.

### Marketplace fees, limits and APIs

35. "Etsy Open API v3 uploadListingFile digital listing file endpoint" (developers.etsy.com): createDraftListing type "download", then POST .../listings/{listing_id}/files, listings_w scope.
36. "Etsy digital items file size limit 5 files 20MB help" (etsy.com): 5 files, 20MB each.
37. "Etsy fees listing fee $0.20 transaction fee 6.5% shop setup fee countries": USD 0.20 listing, 6.5% transaction.
38. "Gumroad fees 10% + 50 cents Discover 30% help center": confirmed on pricing page.
39. "Etsy seller Egypt open shop 2026 verification Payoneer problems reddit": no Reddit results; Etsy community reports of Payoneer sync and ID mismatch issues (not Egypt-specific).
40. "Etsy "Egypt" payment processing fee "6.5%" Etsy Payments policy": confirmed 6.5% + USD 0.30, on gross order, excl. VAT.
41. "Etsy shop setup fee one-time new sellers which countries help": fee varies by location; India USD 10; Egypt amount not shown.
42. "Payhip API documentation create product upload file endpoints": API supports only Coupons and License Keys; product files up to 5GB via dashboard.
43. "Gumroad API v2 create product endpoint upload file docs": create endpoint contested (mirror says 404 not implemented); no file upload endpoint.
44. "Lemon Squeezy API create product not supported files upload API": files are read objects attached to variants; no upload endpoint found.
45. "Gumroad MCP server official create products 2026": only community MCP servers, read/enable/disable only.
46. "Etsy Dev MCP server what it does" (developers.etsy.com): docs/schema helper, does not call the API.
47. "Etsy API commercial access app approval personal access developer terms 2026": tiered app access with manual review for broader access (partly third-party).
48. "Shopify Digital Downloads app file size limit 5GB help": 50 files per variant, 5GB combined; admin product-page files 500MB.

### Specialty marketplaces

49. "Ravelry pattern store sellers payment PayPal Stripe fees how to sell patterns" (ravelry.com): PayPal is the only processor; designers pay invoices by PayPal.
50. "Ribblr sell patterns designer payout PayPal commission fees": staff: "We currently only operate with Stripe"; fee reportedly from 4% (min 25 cents); $elFee and Gems fee waivers.
51. "LoveCrafts sell your patterns independent designer program commission payout PayPal": PayPal payouts in GBP/USD/EUR; PayPal details required to publish; LoveCrafts handles VAT.
52. "Teachers Pay Teachers seller payout methods PayPal international sellers payout fee": Hyperwallet; methods depend on country; US fees listed.
53. "Teachers Pay Teachers seller fees 2026 Premium Seller retired new fee structure": Premium closed to new members 2026-10-01; Exclusive tier requires TPT-only selling; Basic share figures conflict (third-party).
54. "Creative Fabrica become a designer payout PayPal Payoneer royalties crochet patterns": PayPal, Payoneer or bank (USD 20 fee, USD 100 minimum).
55. "Creative Market shop owner payout PayPal Payoneer countries commission 2026": PayPal only to receivable countries; Payoneer not official.
56. "Makerist sell crochet patterns designer commission payout": no official terms found.
57. "Teachers Pay Teachers sell from outside US international seller countries eligible Hyperwallet tax W-8BEN": no TPT country list found.
58. "Ravelry pattern sales fees designers tiered fee schedule current": third-party only (none under about USD 30/month; 3.5% to USD 1,500).
59. "Creative Fabrica sell as designer application crochet patterns printables royalties": 50% of net price per current terms; perpetual non-exclusive license.

### Comparable listings and buyer intent

60. "kids murder mystery party game printable ages 8-12 etsy" (extended): category pages /market/kids_mystery_party, /market/kids_mystery_party_game; prices USD 2.19 to 134.60.
61. "printable dollhouse miniatures 1:12 PDF instant download etsy" (extended): prices about USD 0.50 to 15.54; wallpaper, packaging, books, kits.
62. "no sew crochet pattern sea animal amigurumi PDF etsy octopus whale" (extended): many no-sew octopus listings USD 2.94 to 3.99; bundles.
63. "etsy kids mystery party game printable bestseller reviews sales detective birthday" (extended): listing 4302983274 with 161 reviews at USD 8.28; Missing Birthday Cake kit USD 7.99 with 120 reviews; no bestseller badges visible.
64. "etsy shop printable dollhouse miniatures sales reviews 1:6 1:24 printable kit bestseller" (extended): shops at 29.2k, 13k and 39.4k cumulative sales; multi-scale listings exist.
65. "etsy no sew amigurumi pattern shop sales reviews bestseller sea creatures" (extended): ChassityAnnDesigns26 about 47.7k sales; AlterEgoCrochet about 47.3k; squid listing 1,462 reviews; DigitalCrochetBloom 3.5 from 676 (quality risk); one bundle with inconsistent counts.
66. "no sew amigurumi octopus crochet pattern ravelry": many free no-sew octopus patterns; paid USD 2.20 to 9.16.
67. "no sew sea animal crochet pattern ribblr OR lovecrafts": Ribblr paid no-sew sea patterns USD 2.92 to 8.64; nothing from LoveCrafts surfaced.
68. "mystery party game kids printable teacherspayteachers detective classroom mystery ages 8-12": several grade 3-6 escape-room mysteries; prices not captured.
69. "Gumroad Discover marketplace printable party games crochet patterns sales count ratings": crochet pattern product showing 152 sales; sparse printable party games.
70. "kids mystery party game download instant ages 8-12 birthday printable -etsy": competitor stores Night of Mystery (kids kits ages 8-12, tiered by guests) and My Mystery Party (Diamond Heist, min age 12).
71. "printable dollhouse miniatures shop 1:12 1:24 PDF downloads Payhip OR Gumroad OR Shopify store": Payhip dollhouse poster sets about USD 2.79; Gumroad sofa template USD 3.95; Pattern by Etsy storefront in use; independent multi-scale store (Portraits by NC).

## Remaining gaps (summary)

- Direct verification of all indexed official-doc claims once hosts are allowed.
- Egypt status for TPT (Hyperwallet), LoveCrafts, Creative Fabrica, Creative Market, Makerist, Selar, Polar.
- Current Ravelry fee tiers (login required) and Ravelry API write capability.
- Gumroad Egypt bank payout issue status (#2164) and Gumroad create-product API status.
- Payoneer and PayPal Egypt withdrawal fees (conflicting or missing).
- Etsy shop set-up fee amount for Egypt.
- Live listing sort by "Best Selling" and bestseller badges on Etsy (fetch blocked).
