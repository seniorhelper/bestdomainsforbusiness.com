#!/usr/bin/env python3
"""Rebuilds every inventory-driven file from _build/inventory.tsv.

    python3 _build/build.py

Writes: assets/data/domains.json, domains/index.html, domains/<category>/ and collection pages,
the card grids on the 14 original category pages, zach.js inventory, sitemap.xml, llms.txt,
and applies the shared header/footer (chrome.py) to every page. Safe to run repeatedly."""
import os, re, json, html, glob, datetime, colorsys
from collections import OrderedDict
os.chdir(os.path.dirname(os.path.abspath(__file__)) + "/..")
import sys; sys.path.insert(0, "_build")
from segment import words_for, place_for, PLACES, REGIONS
import chrome as C

TODAY = datetime.date.today().isoformat()

# ---------------------------------------------------------------- categories
CATS = OrderedDict([
 ("marketing", ["Marketing & SEO", "#4c35e8", "seo-marketing"]),
 ("ai", ["AI & agents", "#0b7a53", "ai-agents"]),
 ("realestate", ["Real estate", "#10a05e", "real-estate"]),
 ("travel", ["Travel & hospitality", "#00b0c7", "travel"]),
 ("bath", ["Bath & accessibility", "#2e8fe0", "accessible-bath"]),
 ("trades", ["Home services & trades", "#f26b1d", "home-services"]),
 ("home", ["Mattresses, furniture & appliances", "#9a5b13", "mattresses-furniture-appliances"]),
 ("health", ["Health & beauty", "#e3357f", "health-beauty"]),
 ("auto", ["Automotive", "#e0342c", "automotive"]),
 ("insurance", ["Insurance", "#1d6fa5", "insurance"]),
 ("food", ["Restaurants & food", "#f5a700", "restaurants"]),
 ("pets", ["Pet & supplements", "#8b45d6", "pets"]),
 ("prof", ["Professional services", "#0e7c86", "professional"]),
 ("events", ["Media, events & tech", "#b031a8", "media-tech"]),
 ("vr", ["Virtual reality", "#7e22ce", "virtual-reality"]),
 ("legal", ["Legal & mediation", "#2246b8", "legal"]),
 ("cleanmove", ["Cleaning & moving", "#6fae14", "cleaning-moving"]),
 ("promo", ["Promotional products", "#ff6b5b", "promotional"]),
])
ORIGINAL_CATS = ["marketing", "realestate", "travel", "bath", "trades", "health", "auto", "food", "pets", "prof", "events", "legal", "cleanmove", "promo"]
NEW_CATS = {
 "ai": ("AI agent and automation domain names, owner-direct.",
        "Plain-language names for the businesses being built around AI agents right now: setup services, training courses, AI tools for advertising, SEO and accounting, and Denver-market AI consultancies. Every name is exact-match or short and brandable, and every price is negotiable."),
 "insurance": ("Insurance agency domain names, owner-direct.",
        "Names for auto, health and general insurance agencies, most of them tied to a real Colorado market such as Denver, Brighton or Loveland. Useful as an agency brand, a quote-request site for one town, or a second front door for an existing agency."),
 "home": ("Mattress, furniture and appliance store domain names.",
        "Retail names for the Denver metro and Colorado: mattress stores, a furniture store, appliance stores, an appliance repair company, and a few national names such as buywasheranddryer.com. Built for the signage, delivery-truck and search-ad side of home retail."),
 "vr": ("Virtual reality domain names, owner-direct.",
        "VR names for arcades and attractions, flight simulators, virtual shopping malls and immersive entertainment brands. Several have live sites on them today; ask what comes with each one."),
}

# ---------------------------------------------------------------- collections (cross-listing landing pages)
def W(r, *ws): return any(w in r["ws"] or w in r["flat"] for w in ws)
COLLECTIONS = OrderedDict([
 ("colorado", dict(kind="place", label="Colorado", f=lambda r: r["region"] in ("denver", "colorado"),
   h1="Colorado business domain names, owner-direct.",
   intro="Every name in the portfolio tied to a Colorado market, from the Denver metro to Boulder, Longmont, Greeley, Loveland, Colorado Springs and the mountain towns. The owner is based in Denver, so this is the deepest part of the portfolio.")),
 ("denver", dict(kind="place", label="Denver metro", f=lambda r: r["region"] == "denver",
   h1="Denver domain names for local businesses.",
   intro="Names built for Denver and the surrounding metro: Aurora, Littleton, Centennial, Lakewood, Arvada, Wheat Ridge, Thornton, Westminster, Broomfield, Brighton, Golden and Castle Rock. Trades, health, legal, movers, auto, restaurants and more.")),
 ("hawaii", dict(kind="place", label="Hawaii", f=lambda r: r["region"] == "hawaii",
   h1="Hawaii domain names: Oahu, Maui, Kauai and more.",
   intro="Travel, diving, vacation rental, restaurant, real estate and SEO names for Hawaii and its islands, including Honolulu, Oahu, Maui, Kauai and the Big Island.")),
 ("belize", dict(kind="place", label="Belize", f=lambda r: r["region"] == "belize",
   h1="Belize domain names for travel, real estate and more.",
   intro="Names for tour operators, fishing charters, dive shops, hotels, restaurants, condo sales and real estate in Belize, including San Pedro.")),
 ("costa-rica", dict(kind="place", label="Costa Rica", f=lambda r: r["region"] == "costarica",
   h1="Costa Rica domain names, owner-direct.",
   intro="Real estate, condo, hotel, beach, surf school, rental, restaurant and SEO names for Costa Rica, including a local-language name for an SEO agency.")),
 ("dominican-republic", dict(kind="place", label="Dominican Republic", f=lambda r: r["region"] == "dominican",
   h1="Dominican Republic domain names: Cabarete, Sosua, Puerto Plata.",
   intro="Real estate, condo, restaurant, travel and SEO names for the Dominican Republic's north coast and beyond: Cabarete, Sosua, Puerto Plata, Santo Domingo, La Romana and Higuey.")),
 ("omaha", dict(kind="place", label="Omaha, Nebraska", f=lambda r: r["region"] == "nebraska",
   h1="Omaha domain names for local service businesses.",
   intro="Names for Omaha, Nebraska: fence contractors, mobile auto detailing, carpet and rug cleaning, an SEO agency and a walk-in tub dealer.")),
 ("international", dict(kind="place", label="International", f=lambda r: r["region"] in ("belize", "costarica", "dominican", "colombia", "puertorico"),
   h1="International domain names: Caribbean and Latin America.",
   intro="Names for markets outside the mainland U.S.: Belize, Costa Rica, the Dominican Republic, Colombia and Puerto Rico. Real estate, travel, restaurants and local SEO agencies.")),
 ("glp-1", dict(kind="niche", label="GLP-1 & weight loss", f=lambda r: "glp" in r["flat"] or W(r, "weight"),
   h1="GLP-1 and weight-loss clinic domain names.",
   intro="Names for GLP-1 and medical weight-loss clinics, peptide practices and patient-education sites, several of them for Denver, Littleton and Colorado. A domain is a name, not medical advice; any clinic using one still has to follow the advertising rules that apply to it.")),
 ("decks-and-fences", dict(kind="niche", label="Decks & fences", f=lambda r: W(r, "deck", "decks", "fence", "fences", "pergola"),
   h1="Deck builder and fence contractor domain names.",
   intro="Names for deck builders, pergola builders and fence contractors in the Denver metro, Colorado Springs, Monument and Omaha. Many come in defensive pairs so a competitor cannot own the near-miss.")),
 ("painters", dict(kind="niche", label="Painters", f=lambda r: W(r, "painter", "painters", "painting", "paint"),
   h1="Painting contractor domain names for Colorado.",
   intro="House painter and painting contractor names for Denver, Boulder, Arvada, Golden, Lakewood, Wheat Ridge and Brighton, plus a brandable hotline name.")),
 ("walk-in-tubs", dict(kind="niche", label="Walk-in tubs", f=lambda r: "walkin" in r["flat"] and "tub" in r["flat"],
   h1="Walk-in tub domain names for dealers and installers.",
   intro="Walk-in tub names for dealers across the U.S., from Denver, Omaha, Houston, Miami, Chicago and Boston to whole states such as Texas, Florida, Arizona, California and Utah.")),
 ("movers", dict(kind="niche", label="Movers", f=lambda r: W(r, "mover", "movers", "moving"),
   h1="Moving company domain names for Denver and Colorado.",
   intro="Local and long-distance mover names for Denver and Colorado, including defensive pairs.")),
 ("tires", dict(kind="niche", label="Tire shops", f=lambda r: W(r, "tire", "tires"),
   h1="Tire shop domain names for Denver and Brighton.",
   intro="Tire shop, tire store and tire repair names for Denver and Brighton, Colorado.")),
 ("greeley-lawyers", dict(kind="niche", label="Greeley lawyers", f=lambda r: r["c"] == "legal" and r["place"] == "Greeley",
   h1="Greeley, Colorado lawyer and attorney domain names.",
   intro="Names for law firms in Greeley, Colorado: DUI, divorce and family law attorneys, general practice firms and a mediator.")),
 ("silent-disco", dict(kind="niche", label="Silent disco", f=lambda r: W(r, "disco", "headphones"),
   h1="Silent disco rental domain names.",
   intro="Names for silent disco and headphone party rental companies, national and Denver.")),
 ("international-seo", dict(kind="niche", label="International SEO", f=lambda r: r["c"] == "marketing" and r["region"] in ("belize", "costarica", "dominican", "colombia", "puertorico"),
   h1="SEO and advertising agency domain names abroad.",
   intro="Local SEO and advertising agency names for Belize, Costa Rica, the Dominican Republic, Colombia and Puerto Rico.")),
])

TAGNAMES = {"P": "Premium", "D": "Developed", "C": "Category killer", "X": "Defensive pair", "B": "Brandable", "I": "International"}
PARENT = {}
for tok, label, region in PLACES:
    PARENT[label] = {"denver": "Colorado", "colorado": "Colorado", "hawaii": "Hawaii", "belize": "Belize", "dominican": "Dominican Republic",
                     "colombia": "Colombia", "costarica": "", "puertorico": "", "nebraska": "Nebraska", "national": ""}.get(region, "")
for l, p in {"Houston": "Texas", "Miami": "Florida", "Chicago": "Illinois", "Boston": "Massachusetts", "Oklahoma City": "Oklahoma", "Los Angeles": "California"}.items():
    PARENT[l] = p
for broad in ["Colorado", "Hawaii", "Belize", "Dominican Republic", "Colombia", "Texas", "Florida", "Utah", "Arizona", "California", "New York", "USA", "United States", "Costa Rica", "Puerto Rico"]:
    PARENT[broad] = ""


def esc(s): return html.escape(s, quote=True)


# ---------------------------------------------------------------- load
recs = []
for line in open("_build/inventory.tsv"):
    if line.startswith("#") or not line.strip(): continue
    d, c, t, b = line.rstrip("\n").split("\t")
    assert c in CATS, (d, c)
    w = words_for(d); place, region = place_for(d, b)
    sld = d.split(".")[0]
    recs.append(dict(d=d, c=c, t=t, b=b[len("Built for "):].rstrip() if b.startswith("Built for ") else b, w=w, ws=set(w),
                     flat=sld.replace("-", ""), sld=sld, tld=d[len(sld) + 1:], place=place, parent=PARENT.get(place, ""), region=region))
recs.sort(key=lambda r: r["d"])
N = len(recs)
for k in CATS: CATS[k].append(sum(1 for r in recs if r["c"] == k))

# places dictionary for the client search (alias -> [label, region, parent])
places = {}
for tok, label, region in PLACES:
    places[tok] = [label, region, PARENT.get(label, "")]
for alias, label in {"co": "Colorado", "colorado": "Colorado", "hi": "Hawaii", "ne": "Nebraska", "nebraska": "Nebraska", "dr": "Dominican Republic",
                     "cr": "Costa Rica", "tx": "Texas", "fl": "Florida", "az": "Arizona", "ut": "Utah", "nyc": "New York", "newyork": "New York",
                     "oklahomacity": "Oklahoma City", "us": "USA", "unitedstates": "United States", "il": "Illinois", "illinois": "Illinois",
                     "massachusetts": "Massachusetts", "oklahoma": "Oklahoma", "denvermetro": "Denver"}.items():
    reg = next((p[1] for p in places.values() if p[0] == label), "")
    places[alias] = [label, reg, PARENT.get(label, "")]
for st in ["Texas", "Florida", "Illinois", "Massachusetts", "Oklahoma", "California", "Nebraska"]:
    places.setdefault(st.lower(), [st, "us" if st != "Nebraska" else "nebraska", ""])

uses = json.load(open("_build/uses.json"))
regions_used = OrderedDict((k, v) for k, v in REGIONS.items() if any(r["region"] == k for r in recs) and k)
data = {"v": 1, "built": TODAY,
        "cats": {k: v[:3] for k, v in CATS.items()},
        "regions": regions_used, "places": places, "uses": uses,
        "d": [[r["d"], r["c"], r["t"], r["b"], " ".join(r["w"]), r["place"], r["parent"], r["region"]] for r in recs]}
os.makedirs("assets/data", exist_ok=True)
json.dump(data, open("assets/data/domains.json", "w"), ensure_ascii=False, separators=(",", ":"))
import hashlib
_h = hashlib.sha1(open("assets/data/domains.json", "rb").read()).hexdigest()[:10]
_f = open("assets/js/finder.js").read()
_f = re.sub(r'domains\.json\?v=[^"]*"', 'domains.json?v=' + _h + '"', _f)
open("assets/js/finder.js", "w").write(_f)


# ---------------------------------------------------------------- category color classes (cards)
_css = open("assets/css/site.css").read()
_block = "/*cat-colors*/" + "".join(f".k-{k}{{--h:{v[1]}}}" for k, v in CATS.items()) + "/*/cat-colors*/"
_css = re.sub(r"/\*cat-colors\*/.*?/\*/cat-colors\*/", lambda m: _block, _css) if "/*cat-colors*/" in _css else _css.rstrip("\n") + "\n" + _block + "\n"
open("assets/css/site.css", "w").write(_css)

# ---------------------------------------------------------------- helpers
def contrast_safe(hexc, bg=(255, 252, 245), target=4.6):
    def lum(rgb):
        def ch(c):
            c = c / 255; return c / 12.92 if c <= .03928 else ((c + .055) / 1.055) ** 2.4
        r, g, b = rgb; return .2126 * ch(r) + .7152 * ch(g) + .0722 * ch(b)
    rgb = tuple(int(hexc[i:i + 2], 16) for i in (1, 3, 5))
    for _ in range(40):
        L1, L2 = lum(rgb), lum(bg)
        if (max(L1, L2) + .05) / (min(L1, L2) + .05) >= target: break
        rgb = tuple(max(0, int(c * .92)) for c in rgb)
    return "#%02x%02x%02x" % rgb


def card(r):
    tags = "".join(f'<span class="tag t-{t}">{TAGNAMES[t]}</span>' for t in r["t"] if t in TAGNAMES)
    loc = f'<span class="dloc">{esc(r["place"])}</span>' if r["place"] else ""
    dq = esc(r["d"])
    return (f'<article class="dcard k-{r["c"]}" data-d="{dq}"><button type="button" class="dn" data-open>{esc(r["sld"])}<span class="tld">.{esc(r["tld"])}</span></button>'
            f'<p class="du">Built for {esc(r["b"])}</p><p class="dt">{tags}{loc}</p>'
            f'<div class="dact"><a class="dask" href="/contact/?d={dq}" data-inquire>Make an offer</a><button type="button" class="dmore" data-open>Details</button></div></article>')


def grid(rs): return '<div class="dgrid">' + "".join(card(r) for r in rs) + '</div>'


def itemlist(path, name, rs):
    return {"@type": "ItemList", "@id": C.SITE + path + "#list", "name": name,
            "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": r["d"]} for i, r in enumerate(rs)]}


def hubstrip(extra=""):
    return ('<div class="hubstrip">' + "".join(f'<a href="/domains/{v[2]}/">{esc(v[0])}</a>' for v in CATS.values()) + extra + '</div>')


def placestrip():
    return ('<div class="hubstrip">' + "".join(f'<a href="/domains/{k}/">{esc(v["label"])}</a>'
                                              for k, v in COLLECTIONS.items() if v["kind"] == "place") + '</div>')


def nichestrip():
    return ('<div class="hubstrip">' + "".join(f'<a href="/domains/{k}/">{esc(v["label"])}</a>'
                                              for k, v in COLLECTIONS.items() if v["kind"] == "niche") + '</div>')


ADS = open("_build/catalog-ads.html").read()
CLOSE = open("_build/catalog-close.html").read()
TAGSEC = open("_build/catalog-tags.html").read()

HERO_BG = ('<svg class="hero-bg" viewBox="0 0 1200 620" preserveAspectRatio="xMidYMid slice" aria-hidden="true"><defs>'
           '<radialGradient id="hbA" cx="84%" cy="12%" r="60%"><stop offset="0" stop-color="{c}" stop-opacity=".17"/><stop offset="1" stop-color="{c}" stop-opacity="0"/></radialGradient>'
           '<radialGradient id="hbB" cx="6%" cy="90%" r="56%"><stop offset="0" stop-color="#f5a700" stop-opacity=".16"/><stop offset="1" stop-color="#f5a700" stop-opacity="0"/></radialGradient></defs>'
           '<rect width="1200" height="620" fill="url(#hbA)"/><rect width="1200" height="620" fill="url(#hbB)"/></svg>')


def list_page(path, title, desc, crumbs, eyebrow, color, h1, intro, rs, uses_list=None, faqs=None, nearby=""):
    ecol = contrast_safe(color)
    body = (f'<section class="hero" style="padding:40px 0 22px">{HERO_BG.replace("{c}", color)}<div class="wrap">' + C.crumbs_html(crumbs) +
            f'<span class="eyebrow" style="color:{ecol}">{esc(eyebrow)}</span>\n<h1 style="font-size:clamp(2rem,5.2vw,3.2rem);max-width:22ch">{esc(h1)}</h1>\n'
            f'<p class="lede">{intro}</p>\n<p class="hcount">Every name on this page is for sale and every price is negotiable &middot; tap <b>Make an offer</b> on any card &middot; do not see the one you want? <a href="/find-it-for-me/">We can find it</a>.</p>'
            '<div class="btn-row"><a class="btn btn-p" href="/find-it-for-me/">Not sure which? Let us pick</a><a class="btn btn-s" href="tel:+18004818638">Call 1-800-481-8638</a></div>'
            '</div></section>\n<div class="wrap">' + grid(rs) + '</div>\n')
    if uses_list:
        body += ('<section class="tint"><div class="wrap"><div class="grid g2" style="align-items:start"><div class="body"><span class="eyebrow">What these get used for</span>'
                 f'<h2 class="sec-h" style="font-size:clamp(1.55rem,3.6vw,2.2rem)">Five honest uses for one of these names.</h2><ul>' + "".join(f"<li>{esc(u)}</li>" for u in uses_list) +
                 '</ul><p style="font-size:.95rem;color:var(--ink-70)">None of these are promises. They are what buyers actually do with a name once they own it, and every one depends on the business behind it.</p></div>'
                 '<div><div class="card" style="padding:26px"><h3 style="margin-bottom:8px">Want us to shortlist for you?</h3><p>Tell us what you do and where. We will match names from this list and the rest of the portfolio, or go find one if we do not have it. We can access almost anything and find almost anything.</p>'
                 '<div class="btn-row" style="margin-top:14px"><a class="btn btn-p" href="/find-it-for-me/">Find it for me</a></div></div></div></div></div></section>\n')
    if faqs:
        body += ('<section><div class="wrap narrow"><span class="eyebrow">Straight answers</span><h2 class="sec-h">Before you call.</h2>' + C.faq_html(faqs) +
                 f'<div style="margin-top:30px"><span style="font-size:.87rem;color:var(--ink-70);font-weight:700">Browse more:</span>{nearby}</div></div></section>\n')
    body += CLOSE
    extra = [itemlist(path, h1.rstrip("."), rs)] + ([C.faq_ld(faqs)] if faqs else [])
    return C.page(path, title, desc, crumbs, body, N, extra)


def std_faqs(noun):
    return [
        (f"Are all of these {noun} names really for sale?", "Yes. Every name in the portfolio is for sale, including the ones with live sites on them. There is no hidden reserve list."),
        ("Why are there no prices on the page?", "Because the right number depends on what you are doing with it. A name bought bare, with a site built on it, or as part of a cluster are different conversations. Every price is negotiable and quoted by a person."),
        ("How fast can I have the domain?", "Once payment clears, you get the authorization code and transfer instructions the same business day. The registrars control the transfer itself, which typically takes a few days for a .com. <a href=\"/blog/how-a-domain-transfer-actually-works/\">How transfers work</a>."),
        ("What if the name I want is not here?", "Tell us what you need on the <a href=\"/find-it-for-me/\">find it for me</a> page. If we do not own a fit, we check whether it is simply available to register before suggesting anything that costs money."),
    ]


written = []
def write(path, content):
    fn = path.strip("/") + "/index.html" if path != "/" else "index.html"
    os.makedirs(os.path.dirname(fn) or ".", exist_ok=True)
    open(fn, "w").write(content); written.append(path)


# ---------------------------------------------------------------- new category pages
for k, (h1, intro) in NEW_CATS.items():
    lab, col, slug, n = CATS[k]
    rs = [r for r in recs if r["c"] == k]
    path = f"/domains/{slug}/"
    title = f"{lab} Domain Names for Sale" if len(lab) < 34 else f"{lab.replace('Mattresses, furniture & appliances','Mattress, Furniture & Appliance')} Domains"
    desc = f"{lab} domain names for sale, owner-direct from Denver. No auction, every price negotiable. Make an offer in two taps or call 1-800-481-8638."
    if len(desc) > 158: desc = f"{lab} domain names for sale, owner-direct from Denver. No auction, every price negotiable. Make an offer in two taps."
    others = "".join(f'<a href="/domains/{v[2]}/">{esc(v[0])}</a>' for kk, v in CATS.items() if kk != k)
    write(path, list_page(path, title, desc, [("Home", "/"), ("The domains", "/domains/"), (lab, path)], lab, col, h1, intro, rs,
                          uses[k], std_faqs(lab.lower()), '<div class="hubstrip">' + others + '</div>'))

# ---------------------------------------------------------------- collection pages
for k, v in COLLECTIONS.items():
    rs = [r for r in recs if v["f"](r)]
    rs.sort(key=lambda r: (list(CATS).index(r["c"]), r["d"]))
    path = f"/domains/{k}/"
    lab = v["label"]
    title = (f"{lab} Domain Names for Sale" if v["kind"] == "place" else f"{lab} Domain Names for Sale")
    if len(title) > 60: title = title.replace(" for Sale", "")
    desc = f"{lab} domain names for sale, owner-direct. {('Grouped by industry. ' if v['kind']=='place' else '')}No auction, every price negotiable. Make an offer in two taps."
    if len(desc) > 158: desc = desc.replace(" Make an offer in two taps.", "")
    # group place pages by industry for scanning
    nearby = (placestrip() if v["kind"] == "place" else nichestrip())
    page_html = list_page(path, title, desc, [("Home", "/"), ("The domains", "/domains/"), (lab, path)], lab, "#4c35e8", v["h1"], v["intro"], rs,
                          None, std_faqs(lab), nearby)
    write(path, page_html)

# by-place hub
bp_rows = "".join(f'<a class="card" href="/domains/{k}/"><span class="kicker">Place</span><h3>{esc(v["label"])}</h3><p>{esc(v["intro"][:150].rsplit(" ",1)[0])}&hellip;</p><span class="more">See the names</span></a>'
                  for k, v in COLLECTIONS.items() if v["kind"] == "place")
nc_rows = "".join(f'<a class="card" href="/domains/{k}/"><span class="kicker">Niche</span><h3>{esc(v["label"])}</h3><p>{esc(v["intro"][:110].rsplit(" ",1)[0])}&hellip;</p><span class="more">See the names</span></a>'
                  for k, v in COLLECTIONS.items() if v["kind"] == "niche")
bp = ('<section class="hero" style="padding:40px 0 26px"><div class="wrap">' + C.crumbs_html([("Home", "/"), ("The domains", "/domains/"), ("By place", "/domains/by-place/")]) +
      '<span class="eyebrow">Browse by place &amp; niche</span><h1 style="font-size:clamp(2rem,5.2vw,3.2rem);max-width:20ch">Business domains by city, state and country.</h1>'
      f'<p class="lede">Most names in the portfolio are tied to a real place. Pick yours, or pick a niche below. You can also search any city on the <a href="/domains/">main finder</a> &mdash; and if your city is not here, <a href="/find-it-for-me/">we can go find it</a>.</p></div></section>'
      f'<section style="padding-top:20px"><div class="wrap"><h2 class="sec-h">By place</h2><div class="grid g3">{bp_rows}</div>'
      f'<h2 class="sec-h" style="margin-top:48px">By niche</h2><div class="grid g4">{nc_rows}</div>'
      f'<h2 class="sec-h" style="margin-top:48px">By industry</h2>{hubstrip()}</div></section>' + CLOSE)
write("/domains/by-place/", C.page("/domains/by-place/", "Business Domains by City, State and Niche",
                                   "Browse business domains by place: Colorado, Denver, Hawaii, Belize, Costa Rica, the Dominican Republic and Omaha, or by niche such as movers and painters.",
                                   [("Home", "/"), ("The domains", "/domains/"), ("By place", "/domains/by-place/")], bp, N))

# ---------------------------------------------------------------- original 14 category pages: refresh grid + ItemList + count + contrast
for k in ORIGINAL_CATS:
    lab, col, slug, n = CATS[k]
    fn = f"domains/{slug}/index.html"; s = open(fn).read()
    rs = [r for r in recs if r["c"] == k]
    s = re.sub(r'<div class="wrap"><div class="dgrid">.*?</div></div>\n', lambda m: '<div class="wrap">' + grid(rs) + '</div>\n', s, count=1, flags=re.S)
    s = re.sub(r'\n?<p class="hcount">.*?</p>', "", s)
    s = re.sub(r'(<p class="lede">.*?</p>)', lambda m: m.group(1) + '\n<p class="hcount">Every name in this category is for sale &middot; tap <b>Make an offer</b> on any card, or <a href="/find-it-for-me/">let us shortlist for you</a> &mdash; including names we do not own yet.</p>', s, count=1, flags=re.S)
    s = re.sub(r'(<span class="eyebrow" style="color:)(#[0-9a-fA-F]{6})', lambda m: m.group(1) + contrast_safe(m.group(2)), s)
    def fix_ld(m):
        j = json.loads(m.group(1))
        for x in j["@graph"]:
            if x.get("@type") == "ItemList":
                x.pop("numberOfItems", None); x["itemListElement"] = [{"@type": "ListItem", "position": i + 1, "name": r["d"]} for i, r in enumerate(rs)]
        return '<script type="application/ld+json">' + json.dumps(j, ensure_ascii=False, separators=(",", ":")) + '</script>'
    s = re.sub(r'<script type="application/ld\+json">(.*?)</script>', fix_ld, s, count=1, flags=re.S)
    t = f"{lab} Domain Names for Sale"
    d = f"Exact-match {lab.lower()} domain names for sale, owner-direct from Denver. No auction, every price negotiable. Call 1-800-481-8638."
    s = C.set_meta(s, f"/domains/{slug}/", t, d)
    open(fn, "w").write(s)

# ---------------------------------------------------------------- catalog page
cat_opts = "".join(f'<option value="{k}">{esc(v[0])}</option>' for k, v in CATS.items())
loc_opts = '<option value="co-all">All of Colorado</option>' + \
           "".join(f'<option value="{k}">{esc(v)}</option>' for k, v in regions_used.items())
POP = ["dentist", "denver", "walk in tub", "hawaii", "belize", "fence omaha", "ai agent", "glp-1", "movers", "real estate costa rica"]
catalog_main = (
 '<section class="hero" style="padding:34px 0 18px">' + HERO_BG.replace("{c}", "#4c35e8") + '<div class="wrap">' +
 C.crumbs_html([("Home", "/"), ("The domains", "/domains/")]) +
 '<span class="eyebrow">Browse domains</span>\n<h1 style="font-size:clamp(2rem,5.4vw,3.4rem);max-width:19ch">Find your business domain.</h1>\n'
 '<p class="lede">Search by anything &mdash; a city, a service, a word you half remember. Every name here is for sale and negotiable, quoted by a person rather than a price tag. Not here? That is where we shine: we can access almost anything and find almost anything, from the low-hanging fruit to the hidden gems. <a href="/find-it-for-me/">Tell us what you need</a>.</p>\n'
 '<p class="jump"><a href="#browse-cats">Browse by category</a><a href="/domains/by-place/">Browse by city &amp; state</a><a href="/find-it-for-me/">Have us find one</a></p>\n'
 '</div></section>\n'
 '<div class="finder" id="finder-app"><div class="wrap">\n'
 '<form class="frow" id="finder-form" role="search" action="/domains/" method="get"><div class="fsearch">'
 '<label class="vh" for="srch">Search business domains</label><input id="srch" name="q" type="search" placeholder="Try dentist, denver, walk-in tub, hawaii, fence omaha…" autocomplete="off" enterkeyhint="search">'
 '<button type="submit">Search</button></div></form>\n'
 '<div class="fsel">'
 f'<label>Industry<select id="f-cat"><option value="">All industries</option>{cat_opts}</select></label>'
 f'<label>Location<select id="f-loc"><option value="">Anywhere</option>{loc_opts}</select></label>'
 '<label>Type<select id="f-type"><option value="">Bare &amp; developed</option><option value="dev">Developed (live site)</option><option value="bare">Bare names only</option></select></label>'
 '<label>Extension<select id="f-tld"><option value="">Any extension</option><option value="com">.com only</option><option value="other">Other extensions</option></select></label>'
 '<label>Sort<select id="f-sort"><option value="rel">Best match</option><option value="short">Shortest first</option><option value="az">A to Z</option><option value="cat">By industry</option></select></label>'
 '</div>\n<div class="fmeta"><span id="tally" aria-live="polite">Showing the full portfolio</span><p id="qhint" hidden></p><button class="chip" id="clr" type="button">Clear all</button></div>\n' +
 '<div class="chips" id="tagchips" role="group" aria-label="Filter by tag">' +
 "".join(f'<button class="chip" type="button" aria-pressed="false" data-tag="{t}">{n}</button>' for t, n in [("P", "Premium"), ("C", "Category killer"), ("X", "Defensive pair"), ("B", "Brandable"), ("I", "International"), ("S", "Say-it-once")]) +
 '</div>\n<div class="popq"><span>Popular:</span>' + "".join(f'<button type="button" data-q="{esc(q)}">{esc(q)}</button>' for q in POP) + '</div>\n'
 '</div></div>\n'
 '<div class="wrap"><div class="dgrid" id="grid">' + "".join(card(r) for r in recs) + '</div>\n'
 '<div class="empty" id="empty" hidden><p style="font-size:1.15rem"><strong>Nothing in the portfolio matches <span id="empty-q">that</span>.</strong></p>'
 '<p>That is not the end of it. Tell us what your business does and where, and we will check our names, the open market and whether it is simply available to register.</p>'
 '<div class="btn-row" style="justify-content:center"><a class="btn btn-p" id="empty-cta" href="/find-it-for-me/">Find it for me</a><a class="btn btn-s" href="/register-a-domain/">Check if it is available</a></div></div>\n'
 '</div>\n' + TAGSEC + '\n'
 '<section id="browse-cats"><div class="wrap"><span class="eyebrow">By trade</span><h2 class="sec-h">Browse a category instead.</h2>'
 '<p class="lede">Every category has its own page with the full list and what those names tend to get used for.</p>' + hubstrip() +
 '<h2 class="sec-h" style="margin-top:40px;font-size:clamp(1.4rem,3.2vw,1.9rem)">Or by place and niche.</h2>' + placestrip() + nichestrip() + ADS + '</div></section>\n' + CLOSE)
cat_title, cat_desc = C.META["/domains/"]
cat_title, cat_desc = cat_title.replace("{n}", str(N)), cat_desc.replace("{n}", str(N))
write("/domains/", C.page("/domains/", cat_title, cat_desc, [("Home", "/"), ("The domains", "/domains/")], catalog_main, N,
                          [], show_qbar=False))

# ---------------------------------------------------------------- zach.js inventory
z = open("zach.js").read()
idx = json.dumps([[r["d"], r["c"], r["t"]] for r in recs], separators=(",", ":"))
z = re.sub(r"var IDX = \[\[.*?\]\];", lambda m: "var IDX = " + idx + ";", z, count=1, flags=re.S)
catn = {k: v[0].lower().replace("&", "and") for k, v in CATS.items()}
cathub = {k: v[2] for k, v in CATS.items()}
z = re.sub(r"var CATN = \{.*?\};", lambda m: "var CATN = " + json.dumps(catn) + ";", z, count=1, flags=re.S)
z = re.sub(r"var CATHUB = \{.*?\};", lambda m: "var CATHUB = " + json.dumps(cathub) + ";", z, count=1, flags=re.S)
open("zach.js", "w").write(z)

# ---------------------------------------------------------------- hand-authored pages + upgrades
exec(open("_build/pages.py").read())
exec(open("_build/blog.py").read())
print("blog posts:", [(x["path"], x["words"]) for x in POSTS])

# ---------------------------------------------------------------- developed assets: regenerated from inventory (D tag = verified live site)
DEV = [r for r in recs if "D" in r["t"]]
FEATURED = ["eyetoad.com", "usabusinesssearch.com", "pressreleaseforbusiness.com", "allofus.one",
            "cobusinesslist.com", "worldvrmall.com", "bestshowerkit.com", "linkrestaurants.com"]
def devcard(r):
    tags = "".join(f'<span class="tag t-{t}">{TAGNAMES[t]}</span>' for t in r["t"] if t in TAGNAMES)
    dq = esc(r["d"])
    return (f'<article class="dcard k-{r["c"]}"><span class="dn">{esc(r["sld"])}<span class="tld">.{esc(r["tld"])}</span></span>'
            f'<p class="du">Built for {esc(r["b"])}</p><p class="dt">{tags}</p>'
            f'<div class="dact"><a class="dask" href="/contact/?d={dq}">Make an offer</a>'
            f'<a class="dmore dlive" href="https://{dq}/" target="_blank" rel="noopener">See live site &#8599;</a></div></article>')
def cube(r):
    lab = CATS[r["c"]][0]; col = CATS[r["c"]][1]
    return (f'<a class="cw" href="https://{esc(r["d"])}/" target="_blank" rel="noopener" style="--h:{col}" aria-label="{esc(r["d"])} (opens live site)"><span class="cube spin">'
            f'<span class="f front">{esc(r["sld"])}<span style="color:var(--ink-50)">.{esc(r["tld"])}</span></span><span class="f back">{esc(lab)}</span>'
            f'<span class="f right">Built for {esc(r["b"])}</span><span class="f left">Live site</span><span class="f top"></span><span class="f bottom"></span></span>'
            f'<span class="lbl">{esc(r["sld"])}<span class="tld" style="color:var(--ink-50)">.{esc(r["tld"])}</span><em>{esc(lab)}</em><span class="spotpill">Developed</span></span></a>')
_by = {r["d"]: r for r in DEV}
_cubes = "".join(cube(_by[d]) for d in FEATURED if d in _by)
_groups = [(k, [r for r in DEV if r["c"] == k]) for k in CATS]
_groups = [(k, rs) for k, rs in _groups if rs]
_jump = '<p class="devjump">' + "".join(f'<a href="#dev-{CATS[k][2]}">{esc(CATS[k][0])}</a>' for k, rs in _groups) + '</p>'
_list = ('<div class="wrap">' + _jump + "".join(
    f'<h3 class="devh" id="dev-{CATS[k][2]}">{esc(CATS[k][0])}</h3><div class="dgrid">' + "".join(devcard(r) for r in rs) + '</div>'
    for k, rs in _groups) + '</div>\n')
fn = "developed-assets/index.html"; s = open(fn).read()
s = re.sub(r'<div class="cubes">.*?</a></div>', lambda m: '<div class="cubes">' + _cubes + '</div>', s, count=1, flags=re.S)
s = re.sub(r'<div class="wrap">(?:<p class="devjump">|<div class="dgrid">).*?\n(?=<section class="tint">)', lambda m: _list, s, count=1, flags=re.S)
s = s.replace('<span class="eyebrow">Eight of them, up close</span>', '<span class="eyebrow">A few of them, up close</span>')
s = s.replace('<h2 class="sec-h">The rest of them, in a list.</h2>', '<h2 class="sec-h">Every developed name, by industry.</h2><p class="lede" style="margin-top:8px">Each one is a working site you can open and look at before you call. Tap <b>See live site</b>, then <b>Make an offer</b> on the one that fits.</p>')
open(fn, "w").write(s)
assert s.count('class="dcard') == len(DEV), "developed grid did not regenerate"

# ---------------------------------------------------------------- shared chrome + meta on every page
NOQBAR = {"/", "/domains/"}
for fn in sorted(glob.glob("**/index.html", recursive=True)):
    if fn.startswith("_"): continue
    path = "/" + fn[:-len("index.html")]
    s = open(fn).read()
    s = C.apply_chrome(s, path, N, show_qbar=path not in NOQBAR)
    # cube faces: break long names only at word boundaries (no "conversationalaib / ot")
    def _wbr(m):
        sld = m.group(2).replace("<wbr>", "")
        parts = []
        for chunk in sld.split("-"):
            parts.append("<wbr>".join(words_for(chunk + ".com")))
        return m.group(1) + "-<wbr>".join(parts) + m.group(3)
    s = re.sub(r'(<span class="f front">)([a-z0-9<>wbr-]+?)(<span)', _wbr, s)
    if path in C.META:
        t, d = C.META[path]; s = C.set_meta(s, path, t.replace("{n}", str(N)), d.replace("{n}", str(N)))
    open(fn, "w").write(s)

# ---------------------------------------------------------------- sitemap
pages = sorted("/" + fn[:-len("index.html")] for fn in glob.glob("**/index.html", recursive=True) if not fn.startswith("_"))
def prio(p):
    if p == "/": return "1.0"
    if p in ("/domains/", "/find-it-for-me/"): return "0.9"
    if p.startswith("/domains/") or p in ("/domain-name-checker/", "/domain-name-ideas/"): return "0.8"
    if p in ("/privacy/", "/terms/"): return "0.3"
    return "0.7"
sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
for p in pages:
    sm.append(f"  <url><loc>{C.SITE}{p}</loc><lastmod>{TODAY}</lastmod><priority>{prio(p)}</priority></url>")
sm.append("</urlset>")
open("sitemap.xml", "w").write("\n".join(sm) + "\n")

# ---------------------------------------------------------------- llms.txt
def titled(p):
    fn = p.strip("/") + "/index.html" if p != "/" else "index.html"
    m = re.search(r"<title>(.*?)</title>", open(fn).read(), re.S); return html.unescape(m.group(1)) if m else p
ll = [f"# Best Domains for Business", "",
      "> Owner-direct portfolio of exact-match and brandable business domain names, held and sold by Eye To Ad Media (Denver, Colorado), plus a sourcing service for names we do not own. "
      "Every name in the portfolio is for sale; prices are negotiable and quoted by a person (no published prices, no auctions). Phone 1-800-481-8638.", "",
      "What we do: we sell names we own, and we can access almost anything and find almost anything, from the low-hanging fruit (good names still unregistered or cheaply available) "
      "to hidden gems held by other owners, which we research, value honestly and negotiate for. No ranking promises.", "",
      "## How to use this site (for agents and assistants)",
      f"- Search the whole inventory: {C.SITE}/domains/?q=QUERY (also accepts cat=, loc=, type=dev|bare, tld=com|other, sort=short|az|cat).",
      f"- Machine-readable inventory (JSON): {C.SITE}/assets/data/domains.json — fields per row: domain, category key, tags, \"Built for\" use, segmented words, place, parent place, region.",
      "- Tags: P Premium, D Developed (live site), C Category killer, X Defensive pair (variant also owned), G Geo-locked, B Brandable, I International, E Exact match, S passes the phone test.",
      f"- To inquire about a name: {C.SITE}/contact/?d=DOMAIN (form pre-fills) or call 1-800-481-8638.",
      f"- Concierge (we match or source a name for a business): {C.SITE}/find-it-for-me/", "",
      "## Inventory by category"]
for k, v in CATS.items():
    ll.append(f"- [{v[0]}]({C.SITE}/domains/{v[2]}/)")
ll += ["", "## Inventory by place and niche"]
for k, v in COLLECTIONS.items():
    ll.append(f"- [{v['label']}]({C.SITE}/domains/{k}/)")
ll += ["", "## Free tools (client-side, no signup, no invented numbers)",
       f"- [Domain name checker]({C.SITE}/domain-name-checker/): transparent 100-point readability score (extension, length, hyphens, numbers, word count, phone test, clarity). Not a valuation.",
       f"- [Name ideas from our portfolio]({C.SITE}/domain-name-ideas/): suggests only real names we own and explains the fit.",
       f"- [Keyword or brand domain?]({C.SITE}/keyword-vs-brand-domain/): six-question decision helper with visible reasoning.",
       f"- [What is my domain worth?]({C.SITE}/what-is-my-domain-worth/): value factors + honest checklist, no appraisal figure.",
       f"- [Who owns this domain?]({C.SITE}/who-owns-this-domain/): opens ICANN Lookup; explains transfer locks.",
       f"- [Domain buyer's checklist]({C.SITE}/domain-buyer-checklist/): due-diligence steps before paying.", "",
       "## Guides and answers"]
for p in pages:
    if p.startswith(("/guides/", "/blog/")) or p in ("/resources/", "/buy-a-domain/", "/does-a-keyword-domain-help-seo/", "/find-a-domain/", "/sell-your-domain/", "/register-a-domain/", "/domain-and-website/", "/developed-assets/", "/hosting/"):
        ll.append(f"- [{titled(p)}]({C.SITE}{p})")
ll += ["", "## Facts and policies",
       "- Operator: Eye To Ad Media, 1001 Bannock St #660, Denver, CO 80204. Phone 1-800-481-8638.",
       "- No ranking, traffic or AI-citation guarantees. Keywords in a domain do not earn a Google ranking on their own.",
       "- Acquisition of names owned by others: $1,500 engagement fee, then 15% of the purchase price on close (15% or $1,500, whichever is greater). See /find-a-domain/.",
       "- After payment clears, the buyer receives the authorization code the same business day; registrars control transfer timing.",
       "- Language: English. Questions are answered by email or phone by a real person.",
       f"- Inventory last rebuilt: {TODAY}.", ""]
open("llms.txt", "w").write("\n".join(ll))

print("records", N, "pages", len(pages), "(internal only; never publish this count)")
print({k: v[3] for k, v in CATS.items()})
print({k: sum(1 for r in recs if v["f"](r)) for k, v in COLLECTIONS.items()})
