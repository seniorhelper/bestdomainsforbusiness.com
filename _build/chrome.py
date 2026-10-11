"""Shared page chrome for bestdomainsforbusiness.com (build-time only; Jekyll ignores _build/).
Header, quick-search bar, footer, tail scripts, <head> builder and the transformer that keeps
existing hand-written pages in sync with the shared chrome."""
import re, json, html

SITE = "https://bestdomainsforbusiness.com"
VER = "20261011c"
TEL = "1-800-481-8638"

BBB = ('<a class="bbb" href="https://www.bbb.org/us/co/denver/profile/advertising-agencies/search-converts-llc-1296-90228702/#sealclick" '
       'target="_blank" rel="nofollow noopener"><img src="https://seal-alaskaoregonwesternwashington.bbb.org/seals/blue-seal-200-65-bbb-90228702.png" '
       'width="200" height="65" loading="lazy" alt="Eye To Ad Media (Search Converts LLC) BBB Business Review"></a>')

FAVICONS = ('<link rel="icon" href="/favicon.ico" sizes="48x48">'
            '<link rel="icon" type="image/png" sizes="32x32" href="/images/favicon-32x32.png">'
            '<link rel="icon" type="image/png" sizes="16x16" href="/images/favicon-16x16.png">'
            '<link rel="apple-touch-icon" sizes="180x180" href="/images/apple-touch-icon.png">'
            '<link rel="manifest" href="/site.webmanifest">')

FONT_URL = "https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,600;9..144,700&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap"
FONTS = ('<link rel="preload" as="style" href="' + FONT_URL + '" onload="this.onload=null;this.rel=\'stylesheet\'">'
         '<noscript><link rel="stylesheet" href="' + FONT_URL + '"></noscript>')

LOGO = ('<picture><source type="image/webp" srcset="/images/best-domains-for-business-logo-560.webp">'
        '<img src="/images/best-domains-for-business-logo-560.png" alt="Best Domains for Business" width="280" height="112" fetchpriority="high"></picture>')

CHEV = '<svg width="10" height="7" viewBox="0 0 10 7" aria-hidden="true"><path d="M1 1l4 4 4-4" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>'

TOOLS_MENU = [
    ("/find-it-for-me/", "Find it for me", "Tell us your business. We match or source a name."),
    ("/domain-name-checker/", "Domain name checker", "Score any name, rules shown"),
    ("/domain-name-ideas/", "Name ideas from our portfolio", "Real names we own, explained"),
    ("/keyword-vs-brand-domain/", "Keyword or brand domain?", "Six questions, a straight answer"),
    ("/what-is-my-domain-worth/", "What is my domain worth?", "Honest factors + free written read"),
    ("/who-owns-this-domain/", "Who owns this domain?", "ICANN lookup + transfer guide"),
    ("/domain-buyer-checklist/", "Domain buyer&rsquo;s checklist", "Check it before you pay"),
    ("/guides/", "Guides &amp; resources", "Plain-English answers, sourced"),
]
MORE_MENU = [
    ("/find-a-domain/", "Find &amp; acquire a name", "Someone else owns it? We go get it"),
    ("/register-a-domain/", "Register a new name", "Check availability first"),
    ("/sell-your-domain/", "Sell your domain", "We buy and we broker"),
    ("/domain-and-website/", "Domain + website", "A name and a site built on it"),
    ("/developed-assets/", "Developed assets", "Live sites, not bare names"),
    ("/domain-broker/", "The broker&rsquo;s office", "Walk in. Ninety seconds."),
    ("/hosting/", "Hosting", "Where the name actually lives"),
    ("/does-a-keyword-domain-help-seo/", "Does a keyword domain help SEO?", "The straight answer"),
    ("/sit-down/", "The sit-down", "How this turns into leads"),
]
# shortcuts shown only in the mobile menu (hamburger)
MOB_SHORTCUTS = [
    ("/domains/home-services/", "Home services"), ("/domains/real-estate/", "Real estate"), ("/domains/health-beauty/", "Health &amp; beauty"),
    ("/domains/seo-marketing/", "Marketing &amp; SEO"), ("/domains/travel/", "Travel"), ("/domains/accessible-bath/", "Bath &amp; accessibility"),
    ("/domains/legal/", "Legal"), ("/domains/automotive/", "Automotive"), ("/domains/denver/", "Denver"), ("/domains/colorado/", "Colorado"),
]


def _menu(items, path):
    out = []
    for href, label, sub in items:
        on = ' class="on" aria-current="page"' if path == href else ""
        out.append(f'<a href="{href}"{on}>{label}<small>{sub}</small></a>')
    return "".join(out)


def header(path):
    def top(href, label, cls=""):
        on = path == href or (href == "/domains/" and path.startswith("/domains/")) or (href == "/blog/" and path.startswith("/blog/"))
        classes = " ".join(x for x in (cls, "on" if on else "") if x)
        return f'<a href="{href}"' + (f' class="{classes}"' if classes else "") + (' aria-current="page"' if on else "") + f'>{label}</a>'
    shortcuts = ('<div class="mnav-cats mob-only" aria-label="Browse by category"><p class="mnav-h">Jump to a category</p><div class="mnav-chips">'
                 + "".join(f'<a href="{h}">{l}</a>' for h, l in MOB_SHORTCUTS)
                 + '<a class="mnav-all" href="/domains/#browse-cats">All categories &rarr;</a><a class="mnav-all" href="/domains/by-place/">By city &amp; state &rarr;</a></div></div>')
    return ('<header class="hdr"><div class="hdr-in">\n'
            f'<a class="brand" href="/" aria-label="Best Domains for Business — home">{LOGO}</a>\n'
            '<button class="navtog" aria-label="Menu" aria-expanded="false" aria-controls="nav" data-navtog><span></span><span></span><span></span></button>\n'
            '<nav class="hdr-nav" id="nav" aria-label="Primary">'
            + top("/domains/", "Browse domains", "nav-browse") + top("/find-it-for-me/", "Find it for me", "nav-find") + "\n" + shortcuts + "\n"
            + top("/buy-a-domain/", "How buying works")
            + f'\n<span class="drop" data-drop><button type="button" aria-expanded="false">Free tools {CHEV}</button><span class="drop-menu">{_menu(TOOLS_MENU, path)}</span></span>'
            + top("/blog/", "Blog")
            + f'\n<span class="drop" data-drop><button type="button" aria-expanded="false">More {CHEV}</button><span class="drop-menu">{_menu(MORE_MENU, path)}</span></span>\n'
            + top("/contact/", "Contact")
            + f'\n<a class="hdr-tel" href="tel:+18004818638">{TEL}</a></nav></div></header>')


def qbar(n=None):
    return ('<div class="qbar"><div class="wrap qbar-in"><div class="qwrap">'
            '<form class="qform" action="/domains/" method="get" role="search">'
            '<label class="vh" for="qbar-q">Search business domains for sale</label>'
            '<input id="qbar-q" type="search" name="q" placeholder="Search domains — dentist, denver, walk-in tub…" autocomplete="off" enterkeyhint="search">'
            '<button type="submit">Search</button></form>'
            '<div class="qdrop" id="qbar-drop" role="listbox" aria-label="Matching domains" hidden></div></div>'
            '<a class="qbar-alt" href="/find-it-for-me/">Not here? We can find almost anything &rarr;</a></div></div><!--/qbar-->')


FOOTER = ('<footer class="ftr"><div class="wrap"><div class="ftr-grid">\n'
          '<div class="ftr-about"><h2 class="fh">Best Domains for Business</h2><p>A deep, owner-held portfolio of exact-match business domains, plus the reach to source names we do not own. We can access almost anything and find almost anything. Experts at the low-hanging fruit and at finding hidden gems that take your brand to new heights. Run by Eye To Ad Media in Denver. Call 1-800-481-8638.</p>'
          f'<div class="ftr-bbb">{BBB}</div></div>\n'
          '<div><h2 class="fh">Browse &amp; buy</h2><ul><li><a href="/domains/">Browse domains</a></li><li><a href="/domains/#browse-cats">All categories</a></li><li><a href="/find-it-for-me/">Find it for me</a></li><li><a href="/domains/by-place/">Browse by city &amp; state</a></li><li><a href="/buy-a-domain/">How buying works</a></li><li><a href="/domain-broker/">The broker&rsquo;s office</a></li><li><a href="/domain-and-website/">Domain + website</a></li><li><a href="/developed-assets/">Developed assets</a></li><li><a href="/register-a-domain/">Register a new name</a></li></ul></div>\n'
          '<div><h2 class="fh">Tools &amp; answers</h2><ul><li><a href="/domain-name-checker/">Domain name checker</a></li><li><a href="/domain-name-ideas/">Name ideas from our portfolio</a></li><li><a href="/keyword-vs-brand-domain/">Keyword or brand domain?</a></li><li><a href="/what-is-my-domain-worth/">What is my domain worth?</a></li><li><a href="/who-owns-this-domain/">Who owns this domain?</a></li><li><a href="/domain-buyer-checklist/">Buyer&rsquo;s checklist</a></li><li><a href="/find-a-domain/">Find &amp; acquire a name</a></li><li><a href="/sell-your-domain/">Sell your domain</a></li><li><a href="/does-a-keyword-domain-help-seo/">Does a keyword domain help SEO?</a></li><li><a href="/hosting/">Hosting</a></li></ul></div>\n'
          '<div><h2 class="fh">Company</h2><ul><li><a href="/blog/">Blog</a></li><li><a href="/guides/">Guides</a></li><li><a href="/resources/">Resources</a></li><li><a href="/sit-down/">The sit-down</a></li><li><a href="/contact/">Contact</a></li><li><a href="/terms/">Terms</a></li><li><a href="/privacy/">Privacy</a></li><li><a href="https://eyetoad.com" rel="noopener">Denver SEO, AIO and GEO agency</a></li><li><a href="https://searchconverts.com" rel="noopener">Websites built to convert</a></li><li><a href="https://conversationalaibot.com" rel="noopener">AI chatbots for business</a></li><li><a href="https://mysaleshelp.com" rel="noopener">Sales training and objection handling</a></li></ul></div>\n'
          '</div><div class="ftr-legal"><span>&copy; 2026 Best Domains for Business. All rights reserved.</span><span>Powered by <a href="https://eyetoad.com" rel="noopener">Eye To Ad Media</a> &middot; Denver, Colorado</span></div></div></footer>')

TAIL = ('<div class="heartline"><a href="https://eyetoad.com" rel="noopener"><span class="hh" aria-hidden="true">&#10084;&#65039;</span> Need a website?</a></div>\n'
        '<div class="callbar"><a href="tel:+18004818638" aria-label="Call 1-800-481-8638">&#9742;&#65039; ' + TEL + '</a><a class="cb2" href="/find-it-for-me/">Find my domain</a><span class="sub">A real person answers</span></div>\n'
        f'<script src="/assets/js/nav.js?v={VER}" defer></script>\n<script src="/assets/js/finder.js?v={VER}" defer></script>\n<script src="/zach.js?v={VER}" defer></script>\n</body>\n</html>\n')

ORG = {"@type": "Organization", "@id": SITE + "/#org", "name": "Best Domains for Business", "url": SITE, "telephone": "+1-800-481-8638",
       "email": "info@eyetoad.com", "description": "Owner-direct business domain names and a find-it-for-me sourcing service: we sell names from our own portfolio and locate, value and negotiate for names we do not own.", "slogan": "We can access almost anything and find almost anything.", "parentOrganization": {"@type": "Organization", "name": "Eye To Ad Media", "url": "https://eyetoad.com"},
       "address": {"@type": "PostalAddress", "streetAddress": "1001 Bannock St #660", "addressLocality": "Denver", "addressRegion": "CO", "postalCode": "80204", "addressCountry": "US"},
       "logo": SITE + "/images/best-domains-for-business-logo.png", "sameAs": ["https://eyetoad.com", "https://searchconverts.com"]}
WEBSITE = {"@type": "WebSite", "@id": SITE + "/#site", "url": SITE, "name": "Best Domains for Business", "publisher": {"@id": SITE + "/#org"},
           "potentialAction": {"@type": "SearchAction", "target": {"@type": "EntryPoint", "urlTemplate": SITE + "/domains/?q={search_term_string}"},
                               "query-input": "required name=search_term_string"}}


def jsonld(path, title, desc, crumbs, extra=()):
    g = [ORG, WEBSITE,
         {"@type": "WebPage", "@id": SITE + path + "#page", "url": SITE + path, "name": title, "description": desc,
          "isPartOf": {"@id": SITE + "/#site"}, "about": {"@id": SITE + "/#org"}, "inLanguage": "en-US"},
         {"@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n, "item": SITE + u} for i, (n, u) in enumerate(crumbs)]}]
    g += list(extra)
    return '<script type="application/ld+json">' + json.dumps({"@context": "https://schema.org", "@graph": g}, ensure_ascii=False, separators=(",", ":")) + '</script>'


def faq_ld(pairs):
    strip = lambda s: re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", html.unescape(s))).strip()
    return {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": strip(q), "acceptedAnswer": {"@type": "Answer", "text": strip(a)}} for q, a in pairs]}


def faq_html(pairs):
    return '<div class="faq">' + "".join(f'<details><summary>{q}</summary><div class="ans"><p>{a}</p></div></details>' for q, a in pairs) + '</div>'


def head(path, title, desc, ld, extra_head=""):
    t, d = html.escape(title, quote=True), html.escape(desc, quote=True)
    return ('<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
            '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n<meta name="theme-color" content="#fffcf5">\n'
            f'<title>{t}</title>\n<meta name="description" content="{d}">\n<link rel="canonical" href="{SITE}{path}">\n'
            '<meta property="og:type" content="website">\n<meta property="og:site_name" content="Best Domains for Business">\n'
            f'<meta property="og:title" content="{t}">\n<meta property="og:description" content="{d}">\n<meta property="og:url" content="{SITE}{path}">\n'
            f'<meta property="og:image" content="{SITE}/images/business-domains-for-sale.jpg">\n<meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">\n'
            '<meta name="twitter:card" content="summary_large_image">\n' + FAVICONS + '\n'
            '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
            + FONTS + '\n'
            f'<link rel="stylesheet" href="/assets/css/site.css?v={VER}">\n' + extra_head + ld + '\n</head>\n<body>\n<a class="skip" href="#main">Skip to content</a>\n')


def page(path, title, desc, crumbs, main, n, extra_ld=(), extra_head="", show_qbar=True):
    return (head(path, title, desc, jsonld(path, title, desc, crumbs, extra_ld), extra_head) + header(path) + "\n"
            + (qbar(n) if show_qbar else "") + '\n<main id="main">\n' + main + '\n</main>\n' + FOOTER + "\n" + TAIL)


def crumbs_html(crumbs):
    parts = []
    for i, (n, u) in enumerate(crumbs):
        parts.append(n if i == len(crumbs) - 1 else f'<a href="{u}">{n}</a>')
    return '<p class="crumbs">' + " &rsaquo; ".join(parts) + '</p>'


# ---------------- titles/descriptions for existing pages (<=60 / <=158) ----------------
META = {
    "/": ("Business Domain Names for Sale, Owner-Direct",
          "Search a deep portfolio of exact-match business domains by trade or city, or let us find the one you want. Owner-direct from Denver, every price negotiable."),
    "/domains/": ("Browse Business Domains for Sale | Domain Finder",
                  "Instant search across our business domain portfolio by service, city or state. Filter by industry and location, then make an offer in two taps."),
    "/buy-a-domain/": ("How to Buy a Domain Name Owner-Direct, Step by Step",
                       "How buying a domain from us works: pick the name, get a real number on a call, pay, and get the auth code the same business day. No auction."),
    "/contact/": ("Contact Best Domains for Business | 1-800-481-8638",
                  "Ask about any domain, make an offer, or tell us the name you are hunting for. A real person at Eye To Ad Media answers. Call 1-800-481-8638."),
    "/developed-assets/": ("Developed Domains With Live Websites for Sale",
                           "Domain names sold with a website already built on them: real pages, structure and history. A business asset, not a bare name. Every price negotiable."),
    "/does-a-keyword-domain-help-seo/": ("Does a Keyword Domain Help SEO? The Honest Answer",
                                         "A keyword in your domain does not earn a ranking by itself. What exact-match names really do for clicks, recall and branded search, with sources."),
    "/domain-and-website/": ("Buy a Domain and Custom Website Together",
                             "Buy the domain and have the site built on it: custom-coded websites from $99 a month with a buyout option. Built for search and AI engines."),
    "/domain-broker/": ("Domain Broker in Denver: Owner-Direct Names",
                        "A domain broker with a phone number and a person behind it. Owner-direct names with no auction premium, plus buyer-side acquisition."),
    "/find-a-domain/": ("Domain Acquisition Service: We Negotiate for You",
                        "Want a domain someone else owns? We research the owner, value it honestly and negotiate for you. Cheapest outcome first, no promises."),
    "/hosting/": ("Domain Hosting: Where Your Name Actually Lives",
                  "Your domain needs hosting before anything shows up. What you need, what you can skip, and why cheap, slow hosting costs more than it saves."),
    "/privacy/": ("Privacy Policy | Best Domains for Business",
                  "How Best Domains for Business handles what you send us: used to answer you, never sold or shared. No advertising cookies or trackers."),
    "/register-a-domain/": ("Register a Domain: Check Availability First",
                            "Before you buy a domain from anyone, check whether it is simply available to register. How to check, and what to do if it is taken."),
    "/sell-your-domain/": ("Sell Your Domain Name: We Buy and We Broker",
                           "Thinking of selling a domain? Tell us the name. We either make an offer ourselves or broker it to the buyer who needs it. No upfront cost to have us look."),
    "/sit-down/": ("The Sit-Down: How a Domain Turns Into Leads",
                   "The honest walkthrough: what a keyword domain does, what the website has to do after it, and how the two turn searches into phone calls."),
    "/terms/": ("Terms of Service | Best Domains for Business",
                "Terms for buying domains, acquisition engagements and using bestdomainsforbusiness.com, operated by Eye To Ad Media in Denver, Colorado."),
    "/what-is-my-domain-worth/": ("What Is My Domain Worth? Honest Free Valuation",
                                  "No fake appraisal number. Check the factors buyers actually pay for, work through an honest checklist, then get a free written read from a person."),
    "/who-owns-this-domain/": ("Who Owns This Domain? Free Lookup + Transfer Guide",
                               "Look up any domain on ICANN Lookup, read the record, and learn how a transfer works, including the 60-day locks. Then get help buying it."),
    "/blog/": ("Domain Buying Blog: Plain-English Guides",
               "Long-form articles on finding, buying, valuing and moving to a better business domain, written by a person who sells them and will not promise rankings."),
    "/blog/buying-a-website-that-already-works/": ("Buying a Website That Already Works: What to Check",
                                                   "Due diligence on an established website: verify traffic at the source, reconcile revenue, and learn which parts of a site actually transfer."),
    "/blog/check-a-domains-history-before-you-buy/": ("How to Check a Domain's History Before You Buy",
                                                      "Five free checks that show how a domain was used before you pay: Wayback Machine, a site: search, the registration record, blocklists, trademarks."),
    "/blog/how-a-domain-transfer-actually-works/": ("How a Domain Transfer Works: Auth Codes and Escrow",
                                                    "What an auth code is, why the registrar lock matters, how escrow protects both sides, and the 60-day rule that catches buyers mid-deal."),
    "/blog/how-to-buy-a-domain-someone-else-owns/": ("How to Buy a Domain Someone Else Owns",
                                                     "The full playbook: find the real owner, read the record, work out your number, make an approach that gets a reply, and know when to walk."),
    "/blog/picking-a-business-name-that-passes-the-phone-test/": ("Pick a Business Name That Passes the Phone Test",
                                                                  "Say it once and see if they can type it. Six rules for a domain you will not regret, and the descriptive versus brandable trade-off."),
    "/blog/what-a-domain-name-is-actually-worth/": ("What a Domain Name Is Actually Worth",
                                                    "Why three appraisal tools give three answers, the five things that really move a domain's price, and how to arrive at a real number."),
}


def set_meta(s, path, title, desc):
    t, d = html.escape(title, quote=False).replace('"', "&quot;"), html.escape(desc, quote=True)
    s = re.sub(r"<title>.*?</title>", lambda m: f"<title>{t}</title>", s, count=1, flags=re.S)
    s = re.sub(r'<meta name="description" content="[^"]*">', lambda m: f'<meta name="description" content="{d}">', s, count=1)
    s = re.sub(r'<meta property="og:title" content="[^"]*">', lambda m: f'<meta property="og:title" content="{t}">', s, count=1)
    s = re.sub(r'<meta property="og:description" content="[^"]*">', lambda m: f'<meta property="og:description" content="{d}">', s, count=1)
    # keep the WebPage node in JSON-LD in sync
    def fix_ld(m):
        j = json.loads(m.group(1))
        for x in j.get("@graph", []):
            if x.get("@type") == "WebPage":
                x["name"] = title; x["description"] = desc
        return '<script type="application/ld+json">' + json.dumps(j, ensure_ascii=False, separators=(",", ":")) + '</script>'
    s = re.sub(r'<script type="application/ld\+json">(.*?)</script>', fix_ld, s, count=1, flags=re.S)
    return s


def apply_chrome(s, path, n, show_qbar=True):
    """Bring an existing hand-written page onto the shared chrome. Idempotent."""
    # favicons
    s = re.sub(r'\n?(<link rel="icon"[^>]*>|<link rel="apple-touch-icon"[^>]*>|<link rel="manifest"[^>]*>)+', "", s)
    s = s.replace('<meta name="twitter:card" content="summary_large_image">', '<meta name="twitter:card" content="summary_large_image">\n' + FAVICONS, 1)
    s = re.sub(re.escape(FAVICONS) + r'\n+', FAVICONS + '\n', s)
    s = s.replace('<link href="' + FONT_URL + '" rel="stylesheet">', FONTS)
    s = s.replace("/images/business-domains-for-sale.png", "/images/business-domains-for-sale.jpg")
    s = re.sub(r'<link rel="stylesheet" href="/assets/css/site\.css[^"]*">', f'<link rel="stylesheet" href="/assets/css/site.css?v={VER}">', s)
    # header + quick search bar
    s = re.sub(r'<header class="hdr">.*?</header>\n?(<div class="qbar">.*?<!--/qbar-->\n?)?', lambda m: header(path) + "\n" + (qbar(n) + "\n" if show_qbar else ""), s, count=1, flags=re.S)
    # footer + tail
    s = re.sub(r'<footer class="ftr">.*$', lambda m: FOOTER + "\n" + TAIL, s, count=1, flags=re.S)
    return s
