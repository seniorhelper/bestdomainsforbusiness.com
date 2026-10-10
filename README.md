# bestdomainsforbusiness.com

Static site, GitHub Pages. Apex URLs, no `.html` in any path, all-lowercase slugs.

## Inventory and the build (read this before adding or removing a domain)

The domain list lives in ONE file: `_build/inventory.tsv` (domain, category key, tags, "Built for …" line).
After editing it, run:

```
python3 _build/build.py
```

That regenerates `assets/data/domains.json` (what the search uses), `/domains/` (full finder), every category,
place and niche page, the card grids on the original category pages, the chatbot's list in `zach.js`,
`sitemap.xml`, `llms.txt`, and re-applies the shared header/footer from `_build/chrome.py` to every page.
It is safe to run repeatedly. Jekyll does not publish folders that start with `_`, so `_build/` never goes live.

Category keys: marketing, ai, realestate, travel, bath, trades, home, health, auto, insurance, food, pets, prof,
events, vr, legal, cleanmove, promo. Tag letters: P D C X G B I E S (meanings in `/domains/`).

Owner operating brands (eyetoad.com, searchconverts.com, the *businesslist.com directories, worldbusinesssearch.com,
etc.) are not added as inventory. Some were already listed before 2026-10 and were left as they were — ask the owner.

## Structure

```
/                                  home
/domains/                          full finder — instant fuzzy search, filters, sort, offer modal
/domains/<category>/               18 category hubs (4 added 2026-10: ai-agents, insurance,
                                   mattresses-furniture-appliances, virtual-reality)
/domains/<place-or-niche>/         17 cross-listing pages (colorado, denver, hawaii, belize, …) + /domains/by-place/
/find-it-for-me/                   concierge: business + city + budget + timeline, live matches
/domain-name-checker/              transparent 100-point readability score
/domain-name-ideas/                ideas drawn only from real inventory
/keyword-vs-brand-domain/          six-question decision helper
/domain-buyer-checklist/           13-step due-diligence checklist
/guides/  /guides/<slug>/          guides hub + guides
/resources/                        authoritative outside links
/buy-a-domain/                     how an owner-direct purchase works
/register-a-domain/                check availability first → BuyWebURL
/find-a-domain/                    acquisition service, $1,500 + 15%
/who-owns-this-domain/             free WHOIS lookup tool → acquisition
/what-is-my-domain-worth/          fundamentals tool + free valuation form
/domain-and-website/               $99/mo custom-coded builds
/sell-your-domain/                 seller intake
/developed-assets/                 names with live sites on them
/hosting/                          hosting explainer + affiliate link
/does-a-keyword-domain-help-seo/   the honest-answer page
/sit-down/                         carried forward intact, 3D room preserved
/contact/  /terms/  /privacy/
```

## Shared components — do not inline these on a page

- `assets/css/site.css` — every design token and component. One file, cached across all 30 pages.
- `assets/js/nav.js` — mobile nav and dropdowns.
- `assets/js/finder.js` — search engine, header quick-search, offer/details modal, concierge, all form handling.
- `zach.js` — the chat assistant. Injects its own CSS and markup. Universal file, one copy.

## Chatbot behavior

- **X dismisses him completely** to a slim right-edge tab, stored in `localStorage` under `bdfb_zach_dismissed_v2`. He stays dismissed across every page until the visitor taps the tab.
- **–** minimizes the panel only; he stays on screen.
- Proactive arrival is suppressed entirely when the dismiss flag is set.
- Responses use no-repeat pools, so he does not say the same line twice in a session.
- Knows the full catalog, the tag system, the acquisition pricing, and refuses to promise rankings.

## Forms

FormSubmit AJAX (`https://formsubmit.co/ajax/…`), handled in `assets/js/finder.js`: `_honey` honeypot (bots get a silent thank-you, nothing is sent), 3-second time trap, interaction gate (no submit without a real keydown, pointerdown or input), success/failure states in the page, no `_next` redirect, destination address stored as base64 halves and assembled at runtime with `String.fromCharCode(64)`. The address never appears in markup.

## Standing rules honored

- No prices published anywhere.
- No search-volume figures published anywhere.
- No live links out to any listed domain — plain text only.
- Age claims only on agingsafelybaths.com and eyetoad.com.
- No ranking, traffic or citation guarantees on any page.
- No flashing or blinking animation; all motion respects `prefers-reduced-motion`.
- `phoenixsworld.com` is excluded from the portfolio and must stay excluded.
- Three Neuralink-adjacent names excluded for trademark exposure — do not re-add.

## Logo

`images/best-domains-for-business-logo.png` is alpha-keyed — transparent background, 800×320, 147KB. The old version had an opaque near-white background that showed as a rectangle against the translucent header. Do not replace it with a flattened copy.
