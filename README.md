# bestdomainsforbusiness.com

Static site, GitHub Pages. Apex URLs, no `.html` in any path, all-lowercase slugs.

## Uploading this

41 files total, so it goes in one pass — no batching needed.

1. Unzip.
2. Go to the repo home on GitHub.
3. **Add file → Upload files**, then drag in everything: `index.html`, `zach.js`, `CNAME`, `robots.txt`, `sitemap.xml`, `llms.txt`, `README.md`, and the folders `assets/`, `images/`, and every page folder.
4. Commit.

Dragging folders preserves their structure, so the page folders land correctly on their own.

## Structure

```
/                                  home
/domains/                          full catalog — 587 names, search + filters + profile modal
/domains/<category>/               14 category hubs
/buy-a-domain/                     how an owner-direct purchase works
/register-a-domain/                check availability first → BuyWebURL
/find-a-domain/                    acquisition service, $1,500 + 15%
/who-owns-this-domain/             free WHOIS lookup tool → acquisition
/what-is-my-domain-worth/          fundamentals tool + free valuation form
/domain-and-website/               $99/mo custom-coded builds
/sell-your-domain/                 seller intake
/developed-assets/                 36 names with live sites on them
/hosting/                          hosting explainer + affiliate link
/does-a-keyword-domain-help-seo/   the honest-answer page
/sit-down/                         carried forward intact, 3D room preserved
/contact/  /terms/  /privacy/
```

## Shared components — do not inline these on a page

- `assets/css/site.css` — every design token and component. One file, cached across all 30 pages.
- `assets/js/nav.js` — mobile nav, dropdown, and the hardened form handler.
- `zach.js` — the chat assistant. Injects its own CSS and markup. Universal file, one copy.

## Chatbot behavior

- **X dismisses him completely** to a slim right-edge tab, stored in `localStorage` under `bdfb_zach_dismissed_v2`. He stays dismissed across every page until the visitor taps the tab.
- **–** minimizes the panel only; he stays on screen.
- Proactive arrival is suppressed entirely when the dismiss flag is set.
- Responses use no-repeat pools, so he does not say the same line twice in a session.
- Knows all 587 names, the tag system, the acquisition pricing, and refuses to promise rankings.

## Forms

FormSubmit, hardened: `_honey` honeypot, 3.6s time trap, interaction gate (no submit without a real keydown or pointerdown), no `_next` redirect, destination address stored as base64 halves and assembled at runtime with `String.fromCharCode(64)`. The endpoint never appears in markup.

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
