"""Blog posts generated at build time (added 2026-10-11). Executed by build.py after pages.py
(shares C, N, esc, write, TODAY, CLOSE). Hand-written posts in /blog/ are left alone; these five are
generated so they always carry the shared chrome, Article + Breadcrumb + FAQPage JSON-LD, and appear on
/blog/, /guides/, the sitemap and llms.txt. Never put a portfolio count in any of this copy."""
import re as _re, html as _html, json as _json

AUTHOR = {"@type": "Person", "@id": C.SITE + "/#author", "name": "Zachary Tye Wennstedt", "jobTitle": "Founder",
          "worksFor": {"@id": C.SITE + "/#org"}}


def _art(key, c1, c2, glyph, label, sub):
    """Simple, distinct cover art. key keeps gradient ids unique when several covers share a page."""
    return (f'<svg class="post-art" viewBox="0 0 1200 560" role="img" aria-label="{esc(label)}"><defs>'
            f'<linearGradient id="{key}g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{c1}"/><stop offset="1" stop-color="{c2}"/></linearGradient>'
            f'<radialGradient id="{key}r" cx="78%" cy="22%" r="60%"><stop offset="0" stop-color="#ffd98a" stop-opacity=".55"/><stop offset="1" stop-color="#ffd98a" stop-opacity="0"/></radialGradient></defs>'
            f'<rect width="1200" height="560" fill="url(#{key}g)"/><rect width="1200" height="560" fill="url(#{key}r)"/>'
            '<g opacity=".14" stroke="#fff" stroke-width="1.2" fill="none"><path d="M0 420 H1200M0 460 H1200M0 500 H1200"/></g>'
            '<rect x="110" y="150" width="640" height="96" rx="48" fill="#fffcf5"/>'
            f'<text x="160" y="212" font-family="Plus Jakarta Sans,system-ui,sans-serif" font-weight="800" font-size="40" fill="#141230">{esc(glyph)}</text>'
            f'<text x="112" y="330" font-family="Fraunces,Georgia,serif" font-weight="700" font-size="54" fill="#fffcf5">{esc(sub)}</text>'
            '<circle cx="960" cy="250" r="120" fill="none" stroke="#f7d998" stroke-width="14"/><path d="M1045 335 l70 70" stroke="#f7d998" stroke-width="22" stroke-linecap="round"/>'
            '<circle cx="960" cy="250" r="46" fill="#f7d998" opacity=".85"/></svg>')


POSTS = []


def post(slug, title, desc, h1, section, lede, art, sections, faqs, srcs, related, date="2026-10-11"):
    path = f"/blog/{slug}/"
    _y, _m, _d = (int(x) for x in date.split("-"))
    pubtxt = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"][_m - 1] + f" {_d}, {_y}"
    body = "".join(f'<h2 id="{a}">{h}</h2>\n{b}\n' for a, h, b in sections)
    words = len(_re.sub(r"<[^>]+>", " ", body).split())
    minutes = max(4, round(words / 230))
    toc = '<nav class="toc" aria-label="Contents"><h4>What is in here</h4><ol>' + "".join(f'<li><a href="#{a}">{_re.sub("<[^>]+>", "", h)}</a></li>' for a, h, _ in sections) + '</ol></nav>'
    crumbs = [("Home", "/"), ("The blog", "/blog/"), (section, path)]
    rel = "".join(f'<a href="{u}">{t}</a>' for u, t in related)
    main = ('<section style="padding:44px 0 6px"><div class="wrap narrow">' + C.crumbs_html(crumbs) +
            f'<span class="eyebrow">{section}</span>\n<h1 style="font-size:clamp(1.9rem,4.8vw,3rem)">{h1}</h1>\n'
            f'<p class="lede" style="margin-top:16px">{lede}</p>\n'
            f'<p class="artmeta"><span>By Zachary Tye Wennstedt</span><span>Eye To Ad Media, Denver</span><span>{minutes} min read</span><span>Published {pubtxt}</span></p>\n'
            f'</div></section>\n<div class="wrap narrow" style="padding-bottom:6px">{_art("a" + slug[:6].replace("-", ""), *art)}</div>\n'
            f'<section style="padding-top:26px"><div class="wrap narrow article body">\n{toc}\n{body}'
            '<p class="srcs" style="margin-top:28px"><b>Sources, none of them ours:</b> ' + " &middot; ".join(f'<a href="{u}" rel="noopener" target="_blank">{t}</a>' for t, u in srcs) + '</p>'
            '<div class="callout" style="margin-top:36px"><p><b>Rather have somebody find it for you?</b> We can access almost anything and find almost anything &mdash; '
            'names in our own portfolio, the low-hanging fruit still open to register, and the hidden gems other people own. Tell us the business and the city; a real person replies, usually within one business day.</p>'
            '<div class="btn-row"><a class="btn btn-p" href="/find-it-for-me/">Find it for me</a><a class="btn btn-s" href="/domains/">Browse domains</a></div></div>'
            '</div></section>\n'
            '<section class="tint"><div class="wrap narrow"><span class="eyebrow">Straight answers</span><h2 class="sec-h">Questions this raises.</h2>' + C.faq_html(faqs) + '</div></section>\n'
            f'<section><div class="wrap narrow"><div class="related"><span class="eyebrow">Keep going</span><div class="hubstrip">{rel}</div></div></div></section>\n' + CLOSE)
    art_ld = {"@type": "BlogPosting", "@id": C.SITE + path + "#post", "headline": _html.unescape(_re.sub("<[^>]+>", "", h1)), "description": desc,
              "url": C.SITE + path, "mainEntityOfPage": {"@id": C.SITE + path + "#page"}, "author": {"@id": C.SITE + "/#author"},
              "publisher": {"@id": C.SITE + "/#org"}, "datePublished": date, "dateModified": TODAY, "inLanguage": "en-US",
              "isPartOf": {"@id": C.SITE + "/blog/#blog"}, "articleSection": _html.unescape(section), "wordCount": words,
              "image": C.SITE + "/images/business-domains-for-sale.jpg"}
    write(path, C.page(path, title, desc, crumbs, main, N, [AUTHOR, art_ld, C.faq_ld(faqs)]))
    POSTS.append(dict(path=path, h1=h1, desc=desc, section=section, minutes=minutes, art=art, slug=slug, words=words, date=date))


G = dict(
    rank="https://developers.google.com/search/docs/appearance/ranking-systems-guide",
    starter="https://developers.google.com/search/docs/fundamentals/seo-starter-guide",
    spam="https://developers.google.com/search/docs/essentials/spam-policies",
    move="https://developers.google.com/search/docs/crawling-indexing/site-move-with-url-changes",
    coa="https://support.google.com/webmasters/answer/9370220",
    redirects="https://developers.google.com/search/docs/crawling-indexing/301-redirects",
    dupes="https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls",
    gbp="https://support.google.com/business/answer/3038177",
    local="https://support.google.com/business/answer/7091",
    lookup="https://lookup.icann.org/",
    udrp="https://www.icann.org/resources/pages/help/dndr/udrp-en",
    transfer="https://www.icann.org/resources/pages/transfer-policy-2016-06-01-en",
    errp="https://www.icann.org/resources/pages/errp-2013-02-28-en",
    ftc="https://reportfraud.ftc.gov/",
    ic3="https://www.ic3.gov/",
    uspto="https://tmsearch.uspto.gov/",
)

# ------------------------------------------------------------------ 1
post("domain-name-taken-what-now",
     "Domain Name Taken? 8 Ways to Still Get a Great One",
     "The domain you wanted is registered. Eight practical options, from checking whether it is about to expire to modifiers, other owners and hidden gems.",
     "The domain you wanted is taken. Here is what to do next.",
     "Finding a name",
     "A registered domain is not the end of the road. It is the start of a short checklist that usually ends with either that name, a better one, or a cheaper one you had not thought of.",
     ("#1b1742", "#4c35e8", "yourname.com — taken?", "A taken domain name under a magnifying glass", "Taken is not the end."),
     [("t1", "First, find out what &ldquo;taken&rdquo; actually means",
       "<p>When a registrar says a name is unavailable, it only means somebody holds the registration. It tells you nothing about whether they use it, want it, or would sell it. Before you give up or start bidding, spend ten minutes finding out which of these you are looking at:</p>"
       "<ul><li><strong>A working business.</strong> A real site, real reviews, a phone number. These owners rarely sell cheaply, and sometimes not at all.</li>"
       "<li><strong>A parked page or a for-sale page.</strong> Ads, a &ldquo;this domain may be for sale&rdquo; banner, or a marketplace landing page. The owner is an investor or a registrar program, and there is a price somewhere.</li>"
       "<li><strong>Nothing at all.</strong> The name does not load or shows a registrar placeholder. Often someone registered it for a project that never happened.</li></ul>"
       "<p>Each of those leads somewhere different, so do not skip this step.</p>"),
      ("t2", "1. Read the public record",
       f"<p>Look the name up on <a href=\"{G['lookup']}\" rel=\"noopener\" target=\"_blank\">ICANN Lookup</a> (our <a href=\"/who-owns-this-domain/\">who owns this domain</a> page walks you through it). Most owner details are redacted for privacy now, but three fields still matter: the <strong>registrar</strong>, the <strong>creation date</strong> and the <strong>expiry date</strong>.</p>"
       "<p>An old creation date with a working site means an established owner. A creation date from last month means somebody just grabbed it, and it may be subject to a transfer restriction for a while. An expiry date in the next few weeks is the interesting one, which brings us to the next option.</p>"),
      ("t3", "2. Check whether it is about to expire",
       f"<p>Domains are rented a year or more at a time. When an owner forgets to renew, the name does not instantly become free. ICANN&rsquo;s <a href=\"{G['errp']}\" rel=\"noopener\" target=\"_blank\">Expired Registration Recovery Policy</a> gives the previous owner a window to renew after expiry, and most generic domains then pass through a redemption period (commonly 30 days) and a short pending-delete stage before they are released.</p>"
       "<p>Two honest warnings. First, many registrars sell expiring names through their own auctions during that window, so a good .com often changes hands before it ever drops. Second, a &ldquo;backorder&rdquo; service can try to catch a name the moment it is released, but nobody can promise you will get it. A backorder is a cheap lottery ticket, not a plan.</p>"),
      ("t4", "3. Look for a listing you missed",
       "<p>Plenty of names are openly for sale and the owner simply has not made it obvious. Search the exact domain in quotes, check whether it appears on the big aftermarket marketplaces, and look at the parked page for a small &ldquo;buy this domain&rdquo; link. If there is a listed price, you now know the ceiling. If there is a &ldquo;make offer&rdquo; button, you know the owner is willing to talk.</p>"),
      ("t5", "4. Approach the owner directly, properly",
       "<p>If the name is not listed, you can still ask. Most failed approaches fail because the first message sounds either desperate or insulting. Decide your number before you make contact, keep the message short, and do not tell a stranger how much the name means to your business.</p>"
       "<p>We wrote the full method, including how to find an owner behind privacy redaction and what to say, in <a href=\"/blog/how-to-buy-a-domain-someone-else-owns/\">how to buy a domain someone else owns</a>. If you are not sure what the name is worth, read <a href=\"/blog/what-a-domain-name-is-actually-worth/\">what a domain name is actually worth</a> first, and pay through escrow when you do agree a price (<a href=\"/blog/how-a-domain-transfer-actually-works/\">how transfers and escrow work</a>).</p>"),
      ("t6", "5. Add a word that makes it better, not just available",
       "<p>The lazy fix is to bolt something onto the name until a registrar says yes. The good fix is to add a word that helps a customer. For a local service business, that word is usually the city or the service:</p>"
       "<ul><li><em>smithroofing.com</em> is taken &rarr; <em>smithroofingdenver.com</em> tells people where you work.</li>"
       "<li><em>brightsmile.com</em> is taken &rarr; <em>brightsmiledental.com</em> tells people what you do.</li></ul>"
       "<p>Avoid modifiers that fail the phone test: numbers, hyphens, &ldquo;4&rdquo; for &ldquo;for&rdquo;, and doubled letters at word breaks. Run anything you shortlist through our <a href=\"/domain-name-checker/\">domain name checker</a>, which shows every rule it scores against.</p>"
       "<p>One caution: if the taken name belongs to a competitor in your own field and town, a near-copy will confuse customers and may create trademark trouble. Pick something clearly your own.</p>"),
      ("t7", "6. Consider a different extension, with your eyes open",
       "<p>The same word on .net, .co or a newer extension may be open. That can work, but every non-.com name leaks some visitors and email to whoever owns the .com, because people type .com by habit. Before you buy, look at who owns the .com version. If it is an unrelated hobby site, the leakage is a nuisance. If it is a competitor, walk away. Our guide <a href=\"/guides/com-vs-other-extensions/\">should your business domain be a .com?</a> covers how Google and customers treat each kind of extension.</p>"),
      ("t8", "7. Look for a better name that already exists",
       "<p>People fixate on one exact phrase and miss the ones next to it. The name you can buy today, outright, with no negotiation, may be stronger than the one you started with. That is the whole point of <a href=\"/domains/\">browsing a portfolio</a> by trade and city rather than guessing at a registrar: you see real, available-to-buy names grouped the way customers think. Start with the <a href=\"/domains/by-place/\">city and state pages</a> or a category such as <a href=\"/domains/home-services/\">home services</a>.</p>"),
      ("t9", "8. Use the trademark route only when it truly applies",
       f"<p>If you hold a trademark and someone registered a confusingly similar domain in bad faith, ICANN&rsquo;s <a href=\"{G['udrp']}\" rel=\"noopener\" target=\"_blank\">Uniform Domain-Name Dispute-Resolution Policy</a> (UDRP) exists for exactly that. It is not a way to take a descriptive name like a service and a city from someone who registered it first. Panels can and do rule against complainants who try that. If you think you have a real claim, talk to a trademark attorney, and check the <a href=\"{G['uspto']}\" rel=\"noopener\" target=\"_blank\">USPTO trademark search</a> for your own name before you build on it.</p>"),
      ("t9b", "Five mistakes that make a taken name cost more",
       "<ul><li><strong>Leading with your story.</strong> Telling an owner you have just signed a lease, printed signs or filed paperwork under that name tells them you cannot walk away.</li>"
       "<li><strong>Emailing from your business address.</strong> If your signature shows a funded company, expect the asking price to reflect it. A plain personal address and a short note work better.</li>"
       "<li><strong>Naming the first number.</strong> If the owner has a listed price, you have your ceiling. If not, asking what they would accept is often more useful than opening with a figure.</li>"
       "<li><strong>Registering lookalikes first.</strong> Buying the hyphenated or plural versions before you approach the owner can look like a threat, and some owners respond by refusing to deal at all.</li>"
       "<li><strong>Paying outside escrow.</strong> Even a friendly, honest-sounding owner can have a payment reversed or a transfer go wrong. Escrow protects both sides and costs little compared with the risk.</li></ul>"
       "<p>None of these are dramatic, but each one moves the price in the wrong direction or makes a deal less likely. The calmest buyer usually gets the best result.</p>"),
      ("t10", "Putting it together: a sensible order",
       "<ol><li>Find out what the current use is.</li><li>Read the registration record and note the expiry date.</li>"
       "<li>Look for a listing or a make-offer page.</li><li>Shortlist two or three modifier versions that pass the phone test.</li>"
       "<li>Check what already exists in portfolios like ours.</li><li>Only then decide whether the original name is worth pursuing, and what your walk-away number is.</li></ol>"
       "<p>Most people who work through that list end up happier than if they had simply paid whatever the first owner asked. And if you would rather hand it off, that is exactly what our <a href=\"/find-it-for-me/\">find it for me</a> service does: we start with the low-hanging fruit and keep going until we find the hidden gem that fits.</p>")],
     [("What does it mean when a domain is taken but has no website?", "Someone holds the registration but is not using it. They may be an investor, a business that never launched, or someone who forgot about it. It is often the easiest kind of owner to buy from, but check the record and approach carefully."),
      ("Can I get a domain when it expires?", "Sometimes. After expiry the previous owner gets a window to renew, and most generic domains then go through a redemption period before release. Many good names are sold at registrar auctions during that window, so a backorder is never a guarantee."),
      ("Is it worth buying a taken domain?", "It depends on what the name does for your business compared with the best alternative you could have today. Set a walk-away number before contacting the owner, and compare it with names you can buy outright."),
      ("Should I add a city to my domain name?", "For a local service business, a city often makes a taken name clearer and more useful, as long as the result is still short enough to say and type correctly. Run it through a domain name checker before committing.")],
     [("ICANN Lookup", G["lookup"]), ("ICANN Expired Registration Recovery Policy", G["errp"]), ("ICANN UDRP", G["udrp"]), ("USPTO Trademark Search", G["uspto"])],
     [("/find-it-for-me/", "Find it for me"), ("/who-owns-this-domain/", "Who owns this domain?"), ("/domain-name-checker/", "Domain name checker"), ("/blog/how-to-buy-a-domain-someone-else-owns/", "Buy a domain someone owns"), ("/domains/", "Browse domains")])

# ------------------------------------------------------------------ 2
post("exact-match-local-domains-what-google-says",
     "Exact-Match Domains for Local Businesses: What Google Says",
     "Does a city-plus-service domain help a local business rank? What Google's own documentation says, what an exact-match name really does, and how to use one.",
     "Exact-match domains for local service businesses: what Google actually says.",
     "Keyword domains",
     "A name like <em>denverroofrepair.com</em> is attractive for obvious reasons. Here is what Google has put in writing about names like that, what they genuinely do for a local business, and how to use one without wasting it.",
     ("#0b4a3a", "#0b7a53", "cityservice.com", "A city-plus-service domain name on a road sign", "What Google says."),
     [("t1", "The short answer",
       "<p>An exact-match domain (a name that matches what people search, such as a service plus a city) does not earn a Google ranking by itself. Google says so plainly. It can still be a very good business asset, for reasons that have nothing to do with a ranking trick. Both of those things are true at once, and most of the bad advice about domains comes from people who only tell you one of them.</p>"),
      ("t2", "What Google has published",
       f"<p>Google&rsquo;s <a href=\"{G['rank']}\" rel=\"noopener\" target=\"_blank\">guide to its search ranking systems</a> names an <strong>exact match domain system</strong>. It says the words in a domain name are one factor among many when Google decides whether content is relevant, and that the system exists so Google does not give too much credit to content hosted on domains designed to exactly match particular searches.</p>"
       f"<p>Google&rsquo;s <a href=\"{G['starter']}\" rel=\"noopener\" target=\"_blank\">SEO Starter Guide</a> goes further. It lists keywords in the domain name among the things not to focus on, advises picking a name that is best for your business, and says that from a ranking perspective the keywords in a domain name alone have hardly any effect beyond appearing in breadcrumbs.</p>"
       "<p>Read those together and the message is clear: a keyword in the domain is not a shortcut. Content, usefulness, reputation and, for local searches, your Google Business Profile do the work.</p>"),
      ("t3", "How local ranking works instead",
       f"<p>For map and local results, Google&rsquo;s help page on <a href=\"{G['local']}\" rel=\"noopener\" target=\"_blank\">how local results are ranked</a> describes three main factors: <strong>relevance</strong> (how well a profile matches the search), <strong>distance</strong> (how far the business is from the searcher or the location in the search) and <strong>prominence</strong> (how well known the business is, including reviews and links). Your domain name is not on that list.</p>"
       f"<p>There is also a trap here. Google&rsquo;s <a href=\"{G['gbp']}\" rel=\"noopener\" target=\"_blank\">Business Profile guidelines</a> say your profile name must reflect your real-world business name, as used on your signage and with customers, and they do not allow adding extra keywords or locations that are not part of that name. Owning <em>denverroofrepair.com</em> does not let you call your profile &ldquo;Denver Roof Repair&rdquo; unless that is genuinely your business&rsquo;s name. If you want the name to match, the clean way is to make it your actual trading name, registered properly where you operate.</p>"),
      ("t4", "What an exact-match name genuinely does",
       "<p>So why do businesses still pay for these names? Because they do real work that a ranking tweak never could:</p>"
       "<ul><li><strong>It says what you do before anyone clicks.</strong> In a list of results, in an email signature or on a yard sign, the name explains itself.</li>"
       "<li><strong>It survives the phone and the truck door.</strong> A plain service-and-city name is easy to say, hear and type. That matters for radio, referrals and vehicle wraps.</li>"
       "<li><strong>It is easy to remember.</strong> People who saw your van last week can find you again without remembering your brand.</li>"
       "<li><strong>People link to you with the words you want.</strong> When someone links using your domain as the text, that text describes your service naturally.</li>"
       "<li><strong>Nobody else can have it.</strong> There is exactly one of each. Owning it keeps a competitor from owning it.</li></ul>"
       "<p>None of those is a promise of rankings, and we will never sell a name on that basis. They are reasons a good name keeps paying for itself in every channel, not only search.</p>"),
      ("t5", "Three sensible ways to use one",
       "<p><strong>As your main brand.</strong> If your business name is, or can become, the descriptive phrase, building your main site on the exact-match name is simple and strong. Put the work into the site: real service pages, real photos, reviews, and a fast mobile experience.</p>"
       f"<p><strong>As a campaign address that redirects.</strong> A memorable name used on radio, print or a truck can point to the right page of your main site with a permanent (301) redirect. Google&rsquo;s documentation on <a href=\"{G['redirects']}\" rel=\"noopener\" target=\"_blank\">redirects</a> explains the options. This is about memorability and tracking, not rankings.</p>"
       "<p><strong>As a second business.</strong> If you genuinely run a separate line, for example a roofing company that also does gutters, a separate site with its own unique content can make sense.</p>"),
      ("t6", "The one way not to use one",
       f"<p>Do not buy ten city names and put near-identical pages on each one. Google&rsquo;s <a href=\"{G['spam']}\" rel=\"noopener\" target=\"_blank\">spam policies</a> describe doorway abuse: sites or pages created to rank for specific, similar searches that funnel people to the same place. A network of thin city sites is the textbook example, and it can damage your main site too. If you serve several towns, build genuinely useful location pages on one site. We cover the multi-domain question in more depth in <a href=\"/blog/should-a-business-own-more-than-one-domain/\">should a business own more than one domain?</a></p>"),
      ("t7", "How to judge an exact-match name before you buy",
       "<ul><li><strong>Is the phrase what customers actually say?</strong> &ldquo;Roofer&rdquo; or &ldquo;roofing&rdquo;? &ldquo;Attorney&rdquo; or &ldquo;lawyer&rdquo;? Ask a few customers.</li>"
       "<li><strong>Does it pass the phone test?</strong> No hyphens, no numbers, no doubled letters at word breaks. Our <a href=\"/domain-name-checker/\">domain name checker</a> scores this openly.</li>"
       "<li><strong>Is it a .com?</strong> People type .com by habit.</li><li><strong>Is the history clean?</strong> See <a href=\"/blog/check-a-domains-history-before-you-buy/\">how to check a domain&rsquo;s history</a>.</li>"
       "<li><strong>Will you still like it if you expand?</strong> A city name is a commitment to that city. A service name is a commitment to that service.</li></ul>"
       "<p>Still deciding between a descriptive name and an invented brand? Our <a href=\"/keyword-vs-brand-domain/\">keyword or brand domain</a> helper asks six questions and shows its reasoning. And if you want the long, sourced version of the SEO question, read <a href=\"/does-a-keyword-domain-help-seo/\">does a keyword domain help SEO?</a></p>"),
      ("t7b", "A worked example",
       "<p>Picture a roofing company in Aurora, Colorado called Peak &amp; Sons. Its owner is offered <em>auroraroofrepair.com</em>. Here is how we would think it through with him.</p>"
       "<p><strong>What it will not do:</strong> it will not push Peak &amp; Sons up the map results. Those depend on the company&rsquo;s Business Profile, its reviews, its distance from the searcher and how well known it is locally. The profile must stay &ldquo;Peak &amp; Sons Roofing&rdquo;, because that is the real business name.</p>"
       "<p><strong>What it can do:</strong> it is a perfect address for the side of a truck, a yard sign at every job, a radio spot and a postcard after hail season. People who see it remember it, and it tells them exactly what they get. Pointed with a permanent redirect at a strong &ldquo;roof repair in Aurora&rdquo; page on the main site, every visit lands where it should, and campaign tags in the destination address show how many came from the trucks.</p>"
       "<p><strong>The alternative:</strong> if the owner were starting fresh, he could trade as Aurora Roof Repair and build the main site on the name. That is a branding decision, not an SEO trick, and it has to be made properly, with the right business registration.</p>"
       "<p><strong>The decision:</strong> buy it if the price is in line with what a memorable name is worth across all those channels for years, not because someone promised a ranking.</p>"),
      ("t7c", "Three myths worth dropping",
       "<ul><li><strong>&ldquo;Exact-match domains were penalized, so they are worthless.&rdquo;</strong> Google reduced the credit given to low-quality sites on matching names. A good name with a good site is not penalized for its name.</li>"
       "<li><strong>&ldquo;A keyword domain is all the SEO you need.&rdquo;</strong> The site, the content and the reviews do the work.</li>"
       "<li><strong>&ldquo;More keywords in the name is better.&rdquo;</strong> Long names fail the phone test and look spammy. Short and clear wins.</li></ul>"),
      ("t8", "Where to look for one",
       "<p>The obvious city-and-service .com names for most trades were registered years ago, which is why they are worth something. Start with portfolios organized the way you think, by trade and place: <a href=\"/domains/denver/\">Denver</a>, <a href=\"/domains/colorado/\">Colorado</a>, <a href=\"/domains/home-services/\">home services</a>, <a href=\"/domains/legal/\">legal</a>, or <a href=\"/domains/\">search everything</a>. If what you want is not there, it may be sitting unused at another owner, and finding those hidden gems is what we do.</p>")],
     [("Does an exact-match domain help local SEO?", "Not by itself. Google's own documentation says keywords in a domain name have hardly any ranking effect on their own, and its exact match domain system is designed to avoid over-crediting such names. Local results depend on relevance, distance and prominence."),
      ("Can I use my keyword domain as my Google Business Profile name?", "Only if it is genuinely your real-world business name. Google's Business Profile guidelines do not allow adding keywords or locations that are not part of your actual name."),
      ("Is an exact-match domain bad for SEO?", "No. Google does not penalize a name for containing keywords. Problems come from thin or spammy content, or from networks of near-duplicate sites, not from the name itself."),
      ("Why would a local business pay for an exact-match domain?", "Because it says what you do, is easy to say and remember, works on vehicles, radio and print, and can only be owned by one business. Those are business benefits, not ranking guarantees.")],
     [("Google: ranking systems guide", G["rank"]), ("Google SEO Starter Guide", G["starter"]), ("Google Business Profile guidelines", G["gbp"]), ("Google: how local results are ranked", G["local"]), ("Google spam policies", G["spam"]), ("Google: redirects", G["redirects"])],
     [("/does-a-keyword-domain-help-seo/", "Does a keyword domain help SEO?"), ("/keyword-vs-brand-domain/", "Keyword or brand?"), ("/domains/home-services/", "Home services names"), ("/domains/by-place/", "Names by city"), ("/find-it-for-me/", "Find it for me")])

# ------------------------------------------------------------------ 3
post("move-to-a-new-domain-without-losing-seo",
     "Moving to a Better Domain Without Losing Your SEO",
     "Upgrading to a better domain? The step-by-step move Google documents: URL mapping, 301 redirects, Search Console's Change of Address tool, and what to update.",
     "How to move to a better domain without losing what you have built in search.",
     "Rebranding",
     "Trading up to a stronger name is one of the best upgrades a business can make. It is also the move most likely to cost traffic if it is rushed. Google documents exactly how to do it; here is that process in plain English.",
     ("#3a1c5c", "#7e22ce", "old.com → new.com", "An arrow from an old domain to a new domain", "Move without the drop."),
     [("t1", "Why a domain move is worth doing carefully",
       "<p>Your current domain has built up things that are invisible until you lose them: pages Google has indexed, links from other sites, bookmarks, printed materials and the habits of returning customers. A domain move keeps all of that working only if every old address sends people, and search engines, to the right new one.</p>"
       f"<p>Google treats this as a known, supported situation. Its guide to <a href=\"{G['move']}\" rel=\"noopener\" target=\"_blank\">site moves with URL changes</a> lays out the process, and done that way most sites settle down. Expect some fluctuation while Google recrawls; a small site often settles within weeks, larger sites take longer.</p>"),
      ("t2", "Step 1: Prepare the new domain",
       "<ul><li>Buy the new name and check its history first (<a href=\"/blog/check-a-domains-history-before-you-buy/\">here is how</a>). A name with a spammy past brings problems with it.</li>"
       "<li>Set up hosting and HTTPS on the new domain before anything goes live.</li>"
       "<li>Verify both the old and the new domain in Google Search Console, and in Bing Webmaster Tools if you use it. You will need both properties for the Change of Address step.</li>"
       "<li>Keep the new site blocked from public view only until launch day, and remember to remove any block. A forgotten &ldquo;noindex&rdquo; is one of the most common causes of a failed move.</li></ul>"),
      ("t3", "Step 2: Map every old URL to a new one",
       "<p>This is the step people skip, and it is the one that matters most. Make a spreadsheet with every URL on the old site in one column and its new home in the next. Pull the list from your sitemap, your analytics (any page that gets visits) and Search Console&rsquo;s performance and links reports (any page that earns clicks or links).</p>"
       "<p>Each old page should redirect to its closest equivalent, not to the new homepage. Sending everything to the homepage throws away the relevance each page earned and frustrates visitors who wanted something specific. If you are keeping the same page structure and only changing the domain, the mapping is simple: same path, new domain.</p>"),
      ("t4", "Step 3: Use permanent, server-side redirects",
       f"<p>Use <strong>permanent</strong> redirects (HTTP 301, or 308) from each old URL to its new URL, set up on the server or at your host. Google&rsquo;s page on <a href=\"{G['redirects']}\" rel=\"noopener\" target=\"_blank\">redirects and Google Search</a> explains that permanent server-side redirects are the clearest signal that a page has moved. JavaScript or meta-refresh redirects are weaker fallbacks; a &ldquo;domain forwarding&rdquo; toggle at a registrar can work but often redirects everything to the homepage, so test it.</p>"
       "<p>Avoid chains (old page &rarr; old page 2 &rarr; new page). Point each old URL straight at its final destination.</p>"),
      ("t5", "Step 4: Update everything you control",
       "<ul><li>Internal links on the new site should point to new URLs directly, not through redirects.</li>"
       "<li>Canonical tags, hreflang tags if you have them, and structured data should use the new domain.</li>"
       "<li>Submit the new XML sitemap in Search Console.</li>"
       "<li>Update your Google Business Profile website field, social profiles, email signatures, ad campaigns and payment or booking tools.</li>"
       "<li>Update business directory listings. If you are in the U.S., listings such as <a href=\"https://usabusinesssearch.com\" rel=\"noopener\" target=\"_blank\">USABusinessSearch.com</a> (and <a href=\"https://cobusinesslist.com\" rel=\"noopener\" target=\"_blank\">COBusinessList.com</a> in Colorado) are quick to change.</li>"
       "<li>Ask the sites that send you the most valuable links to update them. Redirects will carry them, but a direct link is always cleaner.</li></ul>"),
      ("t6", "Step 5: Tell Google with the Change of Address tool",
       f"<p>Once the redirects are live, use Search Console&rsquo;s <a href=\"{G['coa']}\" rel=\"noopener\" target=\"_blank\">Change of Address tool</a> on the old property and point it to the new one. It is designed for moving a whole site from one domain to another; it is not for moving from http to https or for changes within the same domain. The tool checks that your redirects work on important pages before it lets you confirm. Its effect lasts for a set period (Google currently describes 180 days), which is one more reason the redirects themselves must stay in place.</p>"),
      ("t7", "Step 6: Keep the redirects, and the old domain, for a long time",
       "<p>Google&rsquo;s site-move guide recommends keeping redirects for as long as possible, generally at least a year. Our advice is simpler: <strong>never let the old domain expire</strong>. Keep it on auto-renew with the redirects running. Old links, printed cards and customer bookmarks will keep arriving for years, and if the old name lapses, someone else can register it and catch that traffic, or worse, impersonate you.</p>"),
      ("t8", "Step 7: Watch the numbers for a few weeks",
       "<ul><li>Search Console: the Pages (indexing) report for the new site should rise as the old one falls. Check for 404 errors and fix any missed redirects.</li>"
       "<li>Analytics: look at visits by landing page, not just the total, so you can spot a page that lost its redirect.</li>"
       "<li>Calls and form fills: these are what actually matter. If they hold, the move worked.</li></ul>"
       "<p>Do not make other big changes (a new design, new URLs, removed content) in the same week if you can avoid it. When several things change at once, it is impossible to tell which one caused a dip.</p>"),
      ("t9", "Email and the less obvious bits",
       "<p>Keep email on the old domain working, or forward it, for at least as long as the redirects. Customers will keep replying to old threads. When you set up email on the new domain, configure SPF, DKIM and DMARC so your messages reach inboxes; our guide on <a href=\"/guides/domain-email-dns-transfer/\">what happens to email and DNS</a> covers the records involved. Update any logins that use an old-domain address so password resets still reach you.</p>"),
      ("t9b", "The mistakes we see most",
       "<ul><li><strong>Redirecting everything to the homepage.</strong> It is quick, and it throws away the value of every individual page.</li>"
       "<li><strong>Letting the old domain lapse.</strong> The redirects die with it, and a stranger can register the name you spent years building.</li>"
       "<li><strong>Launching with the new site still hidden.</strong> A leftover noindex tag or robots.txt block from the staging site stops Google indexing anything.</li>"
       "<li><strong>Changing everything at once.</strong> New domain, new design, new URLs and deleted pages in one weekend makes problems impossible to diagnose.</li>"
       "<li><strong>Forgetting the offline world.</strong> Business cards, vehicle wraps, invoices and voicemail greetings keep sending people to the old name for years. That is fine while the redirects run; it is a disaster if they stop.</li></ul>"),
      ("t9c", "A launch-day checklist",
       "<ol><li>Redirect map finished and tested on a sample of old URLs, including your top pages.</li><li>New site live on HTTPS, indexable, with the new sitemap submitted.</li>"
       "<li>Permanent redirects switched on for every old URL.</li><li>Change of Address submitted in Search Console.</li>"
       "<li>Business Profile, social profiles, directories and ads updated.</li><li>Old domain on auto-renew, email forwarding confirmed.</li>"
       "<li>A reminder in your calendar to review Search Console and analytics weekly for the first month.</li></ol>"),
      ("t10", "Is it worth it?",
       "<p>If the new name is clearly better, shorter, easier to say, a .com instead of a workaround, or simply the name customers already use for you, then usually yes. Done this way, you keep what you have built and gain a name that works harder in every channel. If you have not found that better name yet, <a href=\"/find-it-for-me/\">tell us what you do and where</a>; spotting the upgrade hiding in plain sight is exactly what we are good at. Browse <a href=\"/domains/\">the portfolio</a> or a category like <a href=\"/domains/seo-marketing/\">marketing &amp; SEO</a> to see the kind of names we mean.</p>")],
     [("Will I lose my Google rankings if I change domains?", "Some fluctuation is normal while Google recrawls. If you redirect every old URL to its closest new URL with permanent redirects, update your links and sitemap, and use Search Console's Change of Address tool, most sites settle back down."),
      ("How long should I keep 301 redirects after a domain change?", "Google's site-move guidance recommends as long as possible, generally at least a year. In practice, keep the old domain registered and redirecting indefinitely."),
      ("Should I redirect every old page to the new homepage?", "No. Redirect each old page to its closest equivalent on the new site. Sending everything to the homepage throws away relevance and frustrates visitors."),
      ("What is Google's Change of Address tool?", "A Search Console feature that tells Google a whole site has moved from one domain to another. Both domains must be verified and your redirects must already work.")],
     [("Google: site moves with URL changes", G["move"]), ("Google Search Console: Change of Address tool", G["coa"]), ("Google: redirects and Google Search", G["redirects"])],
     [("/guides/domain-email-dns-transfer/", "Email &amp; DNS during a move"), ("/blog/check-a-domains-history-before-you-buy/", "Check a domain's history"), ("/domain-and-website/", "Domain + website"), ("/domains/", "Browse domains"), ("/find-it-for-me/", "Find it for me")])

# ------------------------------------------------------------------ 4
post("domain-scams-that-target-small-businesses",
     "Domain Scams Targeting Small Businesses: How to Spot Them",
     "Fake renewal invoices, phony buyers who want an appraisal, look-alike escrow sites and auth-code phishing. How each domain scam works and how to stay safe.",
     "Domain scams that target small businesses, and how to spot every one.",
     "Buying safely",
     "Owning a domain puts you on a lot of mailing lists, and some of them are run by people who want your money or your name. Here are the scams we see most often, how each one works, and the simple habits that defeat all of them.",
     ("#5c1a1a", "#e0342c", "URGENT: renew now", "A fake domain renewal invoice with a warning sign", "Spot the scam."),
     [("t1", "Why domain owners get targeted",
       "<p>Domain registration records used to publish owners&rsquo; names, addresses and emails for anyone to read. Privacy redaction has reduced that a lot, but expiry dates, registrars and older scraped data are still easy to find. That makes domain owners an easy list to target, and small businesses are attractive because the person reading the mail is often also the person who pays the bills.</p>"
       "<p>None of these scams is sophisticated. They work because they arrive at a busy moment and look official, often with a deadline of a few days and a logo that resembles one you know. Learn the patterns once and they become easy to ignore, and you can teach whoever opens the mail or pays the invoices to spot them too.</p>"),
      ("t2", "1. The renewal notice that is really a transfer",
       "<p>A letter or email arrives that looks like an invoice: your domain name, an expiry date, a &ldquo;renew now&rdquo; amount. Read the small print and it is not from your registrar at all. Paying it authorizes a different company to transfer your domain to them, usually at a much higher yearly price.</p>"
       "<p><strong>How to stay safe:</strong> know who your registrar is (it is shown on <a href=\"/who-owns-this-domain/\">ICANN Lookup</a>), turn on auto-renew there, and only ever renew by logging in to that registrar directly, never through a link or a mailed form.</p>"),
      ("t3", "2. &ldquo;Someone is trying to register your brand in Asia&rdquo;",
       "<p>An email claims to come from a registrar or &ldquo;domain audit&rdquo; office overseas. A company, it says, has applied to register your business name under several country extensions, and as the brand owner you have a short window to register them first. The prices are high and the urgency is invented. There is no applicant.</p>"
       "<p><strong>How to stay safe:</strong> ignore it. If you genuinely sell into another country, research that country&rsquo;s extension yourself, through a registrar you choose.</p>"),
      ("t4", "3. The buyer who needs you to get an appraisal",
       "<p>Someone writes offering a surprisingly good price for a domain you own. They are keen, but first their company needs a &ldquo;certified appraisal&rdquo; from a specific website, which costs a modest fee. You pay; the buyer disappears. The appraisal site and the buyer are the same people.</p>"
       "<p><strong>How to stay safe:</strong> real buyers do not care which appraisal you have, and there is no such thing as a certified domain appraisal that a buyer must insist on. If you want to understand what a name is worth, read <a href=\"/blog/what-a-domain-name-is-actually-worth/\">what a domain name is actually worth</a> or use our free <a href=\"/what-is-my-domain-worth/\">value checklist</a>, which deliberately never invents a number.</p>"),
      ("t5", "4. The look-alike escrow site",
       "<p>Escrow is the right way to buy or sell a domain: a neutral party holds the money until the domain has transferred (<a href=\"/blog/how-a-domain-transfer-actually-works/\">how it works</a>). Scammers know that, so some deals arrive with an insistence on an &ldquo;escrow service&rdquo; you have never heard of. The site looks professional, shows the money as received, and urges you to transfer the domain. No money was ever there.</p>"
       "<p><strong>How to stay safe:</strong> choose a well-established escrow company yourself, type its address into your browser rather than clicking a link, log in to confirm funds are really held, and check that the company is licensed where it says it operates. Be wary of anyone who refuses every escrow service except theirs.</p>"),
      ("t6", "5. Phishing for your registrar login or auth code",
       f"<p>The real prize for many scammers is control of your domain itself. With your registrar login, or with the domain&rsquo;s authorization (EPP) code and an unlocked domain, they can move it away from you. Under ICANN&rsquo;s <a href=\"{G['transfer']}\" rel=\"noopener\" target=\"_blank\">Transfer Policy</a>, that code is what proves the right to transfer, so treat it like the keys to your shop. Phishing emails imitate your registrar (&ldquo;your domain has been suspended, log in to verify&rdquo;) to capture your password.</p>"
       "<p><strong>How to stay safe:</strong> turn on two-factor login at your registrar, keep the registrar lock on, use a unique password, keep your account email address at a <em>different</em> domain from the one you are protecting, and only ever share an auth code to complete a sale you agreed, after payment is secured in escrow.</p>"),
      ("t7", "6. The seller who does not own the domain",
       "<p>On the buying side, the risk flips. A name you want appears for sale at an attractive price, but the &ldquo;seller&rdquo; does not control it. They may be hoping you pay before you notice, or they may have stolen it.</p>"
       "<p><strong>How to stay safe:</strong> ask the seller to prove control, for example by putting a specific short message on the domain&rsquo;s landing page or adding a DNS record you choose. Pay only through escrow, check the domain&rsquo;s history (<a href=\"/blog/check-a-domains-history-before-you-buy/\">how</a>), and be suspicious of any recent change of registrar or creation date that does not fit the story you are being told. Our <a href=\"/domain-buyer-checklist/\">domain buyer&rsquo;s checklist</a> walks through every check.</p>"),
      ("t8", "7. &ldquo;Search engine registration&rdquo; invoices",
       "<p>A notice warns that your domain&rsquo;s &ldquo;search engine listing&rdquo; is about to expire and asks for an annual fee. Google and Bing do not charge to be included in search results. Your site is crawled for free; Search Console and Bing Webmaster Tools are free too.</p>"),
      ("t8b", "What a legitimate domain deal looks like",
       "<p>It helps to know what normal looks like, so the abnormal stands out. A genuine purchase usually goes like this:</p>"
       "<ol><li>Buyer and seller agree the price and what is included in writing, often by email.</li>"
       "<li>One side opens a transaction at an established escrow company that both have checked independently. The buyer pays the escrow company, not the seller.</li>"
       "<li>The escrow company confirms the funds are held. Both sides can see this by logging in to their own escrow account.</li>"
       "<li>The seller unlocks the domain and provides the authorization code, or pushes the domain to the buyer&rsquo;s account at the same registrar.</li>"
       "<li>The buyer confirms the domain is in their account. Only then does escrow release the money to the seller.</li></ol>"
       "<p>Nothing in that sequence requires an appraisal, an urgent deadline, a gift card, a crypto payment or a link you did not type yourself. Any of those is a reason to stop and check.</p>"),
      ("t9", "The habits that beat all of them",
       "<ul><li>Know your registrar and renew only by logging in there directly.</li><li>Auto-renew on, registrar lock on, two-factor login on.</li>"
       "<li>Never pay an invoice for a domain service you did not order.</li><li>Never pay a buyer&rsquo;s chosen appraiser, and never use an escrow service you did not choose and verify.</li>"
       "<li>Slow down whenever a message is urgent. Real deals survive a day of checking.</li></ul>"),
      ("t10", "If something has already happened",
       f"<p>Contact your registrar immediately; they can often freeze changes or help recover a domain that was moved without your authority. In the U.S., report fraud to the FTC at <a href=\"{G['ftc']}\" rel=\"noopener\" target=\"_blank\">ReportFraud.ftc.gov</a> and internet crime to the FBI&rsquo;s <a href=\"{G['ic3']}\" rel=\"noopener\" target=\"_blank\">IC3</a>. Keep every email and receipt.</p>"
       "<p>Buying from us? Every name in our portfolio is one we hold directly, we use escrow on request, and a real person answers the phone. If you are unsure about any offer or invoice, send it to us through the <a href=\"/contact/\">contact page</a> and we will tell you honestly what we think. And if the name you want belongs to someone else, our <a href=\"/find-it-for-me/\">find it for me</a> service handles the research and the approach safely, start to finish.</p>")],
     [("Is a domain renewal letter from a company I don't recognize a scam?", "Very often, yes. Check who your registrar actually is on ICANN Lookup and renew only by logging in to that registrar directly. Paying an unrecognized notice can authorize a transfer to another company."),
      ("Why would a domain buyer ask me to get an appraisal first?", "It is a common scam. The buyer and the paid appraisal site are often the same people. Genuine buyers do not require a specific paid appraisal."),
      ("How do I know an escrow service is real?", "Choose a long-established escrow company yourself, type its address directly rather than following a link, confirm funds in your own account there, and check its licensing. Be wary of anyone who insists on a service you have never heard of."),
      ("What should I do if my domain was stolen?", "Contact your registrar immediately, keep every record, and in the U.S. report it to the FTC at ReportFraud.ftc.gov and the FBI's IC3.")],
     [("ICANN Transfer Policy", G["transfer"]), ("ICANN Lookup", G["lookup"]), ("FTC: ReportFraud", G["ftc"]), ("FBI Internet Crime Complaint Center (IC3)", G["ic3"])],
     [("/domain-buyer-checklist/", "Buyer's checklist"), ("/blog/how-a-domain-transfer-actually-works/", "How transfers &amp; escrow work"), ("/who-owns-this-domain/", "Who owns this domain?"), ("/contact/", "Ask a person"), ("/find-it-for-me/", "Find it for me")])

# ------------------------------------------------------------------ 5
post("should-a-business-own-more-than-one-domain",
     "Should a Business Own More Than One Domain?",
     "Misspellings, defensive names, city domains and campaign URLs: when owning extra domains helps a small business, when it backfires, and how to set them up.",
     "Should a small business own more than one domain?",
     "Strategy",
     "Usually, a couple. Rarely, a lot. Here is how to decide which extra names are worth renewing every year, which ones quietly cause problems, and how to set them up so they help.",
     ("#5a3a08", "#c8963e", "one main site", "Several domain names pointing to one website", "One home, many doors."),
     [("t1", "The principle: one home, several doors",
       "<p>Almost every small business should have <strong>one main website</strong> on one main domain. That is where your content, reviews, links and reputation build up. Extra domains are useful as doors into that home: names people might type, names you do not want a competitor to own, and names that are easy to say on the radio. They become a problem when they turn into separate, thin copies of the same site.</p>"),
      ("t2", "Extra names that usually earn their keep",
       "<ul><li><strong>The .com of your brand</strong>, if your main site is on another extension. Otherwise some customers and emails will always go to whoever holds it.</li>"
       "<li><strong>The obvious misspelling</strong>, if your name has one. If people regularly spell it two ways, own both.</li>"
       "<li><strong>The defensive pair.</strong> If your name is a phrase, the singular/plural or &ldquo;the&rdquo; version can be worth holding so nobody builds a look-alike. Several names in <a href=\"/domains/\">our portfolio</a> are tagged <em>Defensive pair</em> for exactly this reason.</li>"
       "<li><strong>A short campaign address</strong> for radio, print, vehicles or a trade show, redirecting to a specific page so you can measure the response.</li></ul>"),
      ("t3", "Extra names that usually do not",
       "<ul><li>Every extension under the sun (.net, .org, .info, .biz, .us and so on) &ldquo;just in case&rdquo;. Unless impersonation is a real risk in your field, the renewals add up for little benefit.</li>"
       "<li>Long keyword variations you will never print or say.</li>"
       "<li>Names bought to host separate copies of your site for different towns, which brings us to the main warning.</li></ul>"),
      ("t4", "The city-site trap",
       f"<p>A common pitch goes like this: buy a domain for every nearby town, put a page on each, and rank everywhere. Google&rsquo;s <a href=\"{G['spam']}\" rel=\"noopener\" target=\"_blank\">spam policies</a> describe exactly this as <strong>doorway abuse</strong>, listing examples such as having multiple domain names or pages targeted at specific regions or cities that funnel users to one page. Thin, near-duplicate city sites tend not to rank, and they can drag down the reputation of the business behind them.</p>"
       f"<p>Duplicate content across several domains also splits the signals that should be building up on one site. Google&rsquo;s guidance on <a href=\"{G['dupes']}\" rel=\"noopener\" target=\"_blank\">consolidating duplicate URLs</a> explains how it picks one version and why you should tell it which one you prefer.</p>"
       "<p>If you genuinely serve several towns, the better approach is genuinely useful location pages on your main site: real jobs you have done there, local photos, who to call, travel areas, honest details. A city domain can then be a door that redirects to that page, which is useful on a local mailer or truck, without pretending to be a separate business.</p>"),
      ("t5", "When a second real website does make sense",
       "<p>A separate site on its own domain is right when it serves a genuinely different business or audience, with its own content: a landscaping company that launches a separate snow-removal brand, a dentist who opens a separately branded sleep-apnea clinic, a property manager with a vacation rental brand. The test is simple: would a customer think of these as two different things? If yes, two sites can be fine. If they are the same service with a different town name, they are one site.</p>"),
      ("t6", "How to set up extra domains properly",
       f"<ol><li><strong>Use permanent redirects.</strong> Point each extra domain at your main site, or at the specific page it advertises, with a 301 redirect. Google&rsquo;s <a href=\"{G['redirects']}\" rel=\"noopener\" target=\"_blank\">redirects documentation</a> explains why permanent server-side redirects are the clearest signal.</li>"
       "<li><strong>Give redirect domains HTTPS too.</strong> If someone types <em>https://</em> before a redirect-only name that has no certificate, they see a browser warning instead of your site. Most hosts and some registrars can issue a certificate for redirect domains; test both http and https versions.</li>"
       "<li><strong>Add tracking on campaign names.</strong> Redirect a radio or truck name to a page URL with campaign parameters so you can see the visits in analytics.</li>"
       "<li><strong>Protect domains that never send email.</strong> Publish SPF and DMARC records that say the domain sends no mail, so nobody can easily spoof it. See our guide on <a href=\"/guides/domain-email-dns-transfer/\">email and DNS records</a>.</li>"
       "<li><strong>Keep everything at one registrar</strong>, on auto-renew, with the registrar lock and two-factor login on. Put renewal dates in a calendar anyway.</li></ol>"),
      ("t6b", "What extra domains cannot protect you from",
       "<p>Owning a dozen variations of your name does not stop someone from using your brand in an ad, on a social profile or in a look-alike name you did not think of. Domains are one layer of brand protection, not all of it. If your name is distinctive and you plan to grow, a registered trademark does far more to protect it than a drawer full of extensions, and it is what gives you standing under ICANN&rsquo;s dispute process if someone registers a confusing name in bad faith. Check the USPTO database before you commit to a name, and talk to a trademark attorney if the brand matters to the value of the business.</p>"
       "<p>Equally, do not let defensive buying distract you from the domain that does the real work. A strong, easy-to-say main name, used consistently on your site, profile, vehicles and paperwork, protects you better than any number of backups.</p>"),
      ("t7", "An annual five-minute audit",
       "<p>Once a year, list every domain you own and ask three questions of each: Does anyone type or use this? Would it hurt if a competitor owned it? Is it set up correctly (redirecting, HTTPS working, renewing)? If the answer to the first two is no, let it lapse or sell it. Our <a href=\"/sell-your-domain/\">sell your domain</a> page will tell you honestly whether a name you no longer need is worth anything.</p>"),
      ("t7b", "A worked example",
       "<p>Imagine a family-run plumbing company, Ortega Plumbing, in Littleton, Colorado. Its main site is on <em>ortegaplumbing.com</em>. Customers sometimes type <em>ortegasplumbing.com</em>, with an extra s, and the company runs a radio spot every winter about frozen pipes.</p>"
       "<ul><li><strong>Main site:</strong> ortegaplumbing.com, with real service pages and a page for each town it regularly serves.</li>"
       "<li><strong>Misspelling:</strong> ortegasplumbing.com, redirected to the homepage. Cheap insurance against lost calls.</li>"
       "<li><strong>Campaign name:</strong> a short, easy-to-say name such as a frozen-pipes phrase with the city, redirected to the winter-emergency page with campaign tags, so the owner can see exactly what the radio spot produced.</li>"
       "<li><strong>Not bought:</strong> a separate domain and site for each of six suburbs, and every alternative extension of the brand. Neither would have earned its renewal.</li></ul>"
       "<p>Three domains, one website, every one of them doing a job. That is the pattern we recommend to almost every local business.</p>"),
      ("t7c", "What it really costs",
       "<p>A standard domain renewal is a modest yearly fee, but it is a fee forever. Ten names you do not need cost ten times as much every year, and each one is something else to keep secure. Premium names cost more up front because they are scarce, and then renew at the normal rate at most registrars for a .com. Before you buy any extra name, ask what it does for the business each year, not just on the day you buy it.</p>"),
      ("t8", "A sensible starter set",
       "<p>For a typical local service business: the main .com, the most common misspelling if there is one, and possibly one short, memorable campaign name that redirects to your main offer. That is often enough. If the right main name is the thing you are missing, <a href=\"/find-it-for-me/\">tell us what you do and where</a>; we look through our own names first, then the low-hanging fruit and the hidden gems beyond it. You can also browse by trade, such as <a href=\"/domains/home-services/\">home services</a> or <a href=\"/domains/health-beauty/\">health &amp; beauty</a>, or by <a href=\"/domains/by-place/\">city and state</a>.</p>")],
     [("Is it bad for SEO to have multiple domains?", "Owning several domains is not a problem. Running several near-duplicate sites for different cities or keywords can be, because Google's spam policies describe that as doorway abuse. Point extra domains at one main site with permanent redirects."),
      ("Should I buy the .net and .org of my business name?", "Only if impersonation or customer confusion is a real risk in your field. For most small businesses, the .com plus the most common misspelling is enough."),
      ("Do redirect-only domains need an SSL certificate?", "Yes, if anyone might visit the https version. Without a certificate, visitors see a browser warning before the redirect happens."),
      ("Can I use a separate domain for each city I serve?", "As a redirect to a genuinely useful location page on your main site, yes. As a separate thin site that copies your main site, no; that is the doorway pattern Google warns against.")],
     [("Google spam policies (doorway abuse)", G["spam"]), ("Google: consolidate duplicate URLs", G["dupes"]), ("Google: redirects and Google Search", G["redirects"])],
     [("/domains/", "Browse domains"), ("/blog/exact-match-local-domains-what-google-says/", "Exact-match local domains"), ("/guides/domain-email-dns-transfer/", "Email &amp; DNS guide"), ("/sell-your-domain/", "Sell a domain you don't need"), ("/find-it-for-me/", "Find it for me")])


# ------------------------------------------------------------------ added 2026-10-12 (three buyer-intent posts)
G.update(
    iana_ai="https://www.iana.org/domains/root/db/ai.html",
    multireg="https://developers.google.com/search/docs/specialty/international/managing-multi-regional-sites",
    dnib="https://www.dnib.com/articles/the-domain-name-industry-brief-q2-2026",
    tm_strong="https://www.uspto.gov/trademarks/basics/strong-trademarks",
    tm_search="https://www.uspto.gov/trademarks/basics/why-search-similar-trademarks",
    aba71="https://www.americanbar.org/groups/professional_responsibility/publications/model_rules_of_professional_conduct/rule_7_1_communication_concerning_a_lawyer_s_services/comment_on_rule_7_1/",
    co_trade="https://www.sos.state.co.us/pubs/business/FAQs/tradeNames.html",
    co_tm="https://www.sos.state.co.us/pubs/business/FAQs/trademarks.html",
)


def _x(key, text):
    """External link in the house style (opens in a new tab, no referrer games)."""
    return f'<a href="{G[key]}" rel="noopener" target="_blank">{text}</a>'


# ------------------------------------------------------------------ 6
post("how-to-choose-a-domain-name-for-an-ai-startup",
     "How to Choose a Domain Name for an AI Startup",
     "Should an AI company use .ai or .com, put AI in the name, or go brandable? A practical checklist on extensions, trademarks, the phone test and resale.",
     "How to choose a domain name for an AI startup.",
     "AI names",
     "Every AI founder hits the same three questions in the first week: .ai or .com, whether the word AI belongs in the name, and whether to describe the product or invent a brand. Here is how to answer each one with sources rather than hunches.",
     ("#06261c", "#0b7a53", "yourproduct.ai or .com?", "An AI startup name being compared across two extensions", "Name it to last."),
     [("a1", "Start with what the name has to do",
       "<p>Before you look at a single extension, write down who has to find you and how. An AI product sold self-serve to developers lives and dies on a short, memorable brand that people pass around in chat and code. An AI <em>service</em> sold to local businesses, such as setting up agents for an accounting firm or running AI tools for a marketing team, usually wins on a name that explains itself on a phone call. Those are different jobs, and the right domain for one is often wrong for the other.</p>"
       "<p>Three questions narrow it quickly:</p>"
       "<ul><li><strong>Who types it?</strong> Technical buyers tolerate an unusual spelling; a busy owner hearing your name on a podcast will not.</li>"
       "<li><strong>Will the product change?</strong> Most AI products pivot at least once. A name tied to one feature can age badly.</li>"
       "<li><strong>Is this the company or a campaign?</strong> A company name needs to last; a campaign or lead-generation name can be literal and temporary.</li></ul>"),
      ("a2", "The .ai versus .com question",
       f"<p>It helps to know what .ai actually is. According to the {_x('iana_ai', 'IANA root zone database')}, .ai is the country-code top-level domain of Anguilla, and its manager of record is the Government of Anguilla. It became the default AI extension because of the letters, not because of anything technical.</p>"
       f"<p>For search, the extension matters less than people fear. Google's guide to {_x('multireg', 'multi-regional and multilingual sites')} lists .ai among the country-code extensions it treats as generic, meaning it is not read as a signal that your site targets Anguilla (Google notes that list can change). The {_x('starter', 'SEO Starter Guide')} goes further and says the extension only matters if you are targeting a specific country's users, and even then it is usually a low-impact signal.</p>"
       f"<p>Where the extension does matter is people. The {_x('dnib', 'Verisign Domain Name Industry Brief')} still ranks .com as the largest top-level domain by registrations, and that habit shows up in typing and email. If you build on <em>yourbrand.ai</em> and someone else owns <em>yourbrand.com</em>, some of your visitors and some of your email will go to them. That is a nuisance if the .com is an unrelated parked page and a real problem if it is a competitor.</p>"
       "<p>Two practical notes on .ai itself. Policies for a country-code extension are set by its registry rather than by the contracts that govern .com, so read your registrar's terms for .ai registration periods, renewals and transfers instead of assuming they match. And put renewals on auto-pay with a backup card; losing a startup's main domain to an expired card is an avoidable disaster. Our guide <a href=\"/guides/com-vs-other-extensions/\">should your business domain be a .com?</a> covers the trade-off for every common extension.</p>"),
      ("a3", "Should AI be in the name at all?",
       "<p>Putting AI in the name gives an instant category signal. Right now that is useful: a buyer scanning a list knows what you do. It also has three costs worth weighing.</p>"
       f"<ul><li><strong>Trademark strength.</strong> The USPTO's page on {_x('tm_strong', 'strong trademarks')} explains that descriptive marks are weak and harder to protect, while invented and arbitrary words are the strongest. A name that is mostly the word AI plus a generic noun is close to descriptive.</li>"
       "<li><strong>Crowding.</strong> Many new companies are making the same move, so an AI-plus-noun name can blur into its neighbours in search results, app stores and conversation.</li>"
       "<li><strong>Shelf life.</strong> If AI becomes as assumed in software as the internet is, a name built on the label may feel dated. That is a judgement call, not a prediction.</li></ul>"
       "<p>One thing AI in the domain will not do is rank you. Google's starter guide says keywords in a domain name alone have hardly any effect beyond appearing in breadcrumbs. Choose the word for people, not for an algorithm.</p>"),
      ("a4", "Descriptive, brandable, or both",
       "<p>There are three workable patterns for an AI company, and each fits a different business:</p>"
       "<ul><li><strong>Descriptive.</strong> The name is the service: AI agent setup, AI for accounting firms, learning to use AI agents. Best for service businesses, courses and lead-generation sites, because the name answers the caller's first question.</li>"
       "<li><strong>Brandable.</strong> An invented or borrowed word with no keyword to carry. Best for venture-backed products expected to grow beyond one feature, and strongest for trademark purposes.</li>"
       "<li><strong>Hybrid.</strong> A short brand word plus a hint of the category. A good compromise when you need memorability and a clue to what you do.</li></ul>"
       "<p>If you are torn, our six-question <a href=\"/keyword-vs-brand-domain/\">keyword or brand domain helper</a> shows its reasoning as you answer. You can also browse real examples of both styles on our <a href=\"/domains/ai-agents/\">AI and agents domain names</a> page, every one owner-direct and negotiable.</p>"),
      ("a5", "Clear the trademark before you fall in love",
       f"<p>AI naming has a specific trap: names that lean on a famous model, lab or product. They feel clever, attract attention, and invite a letter from a legal department. The USPTO explains {_x('tm_search', 'why to search for similar trademarks')} before you commit: an application can be refused for likelihood of confusion with an existing mark when the names are similar and the goods or services are related, and they do not need to be identical to count. The USPTO also says the examiner only checks the federal database, so state registrations and ordinary internet use are your job to search.</p>"
       f"<p>If someone else owns a domain that copies your registered mark in bad faith, ICANN's {_x('udrp', 'Uniform Domain-Name Dispute-Resolution Policy')} is the usual route for generic extensions. The same process can be used against you if your name copies theirs. A short session with a trademark attorney before launch costs far less than a rebrand after it.</p>"),
      ("a6", "Run the phone test and the spelling test",
       "<p>AI brands love dropped vowels, doubled letters and invented endings. Each one adds a chance that someone types the name wrong. Say the name once to a friend who has never heard it and ask them to type it. If they hesitate, ask whether the cleverness is worth the leak. Our <a href=\"/domain-name-checker/\">domain name checker</a> scores length, hyphens, numerals, word count and clarity, and shows every rule it applies, and <a href=\"/blog/picking-a-business-name-that-passes-the-phone-test/\">picking a name that passes the phone test</a> explains the thinking behind it.</p>"),
      ("a7", "Check the name's past",
       "<p>Plenty of short, AI-flavoured names have been registered before, sometimes for projects that left a poor reputation behind: spam, scraped content or an abandoned crypto token. Look at the Wayback Machine, run a site: search and check the registration record before you pay. Our walk-through, <a href=\"/blog/check-a-domains-history-before-you-buy/\">how to check a domain's history</a>, takes about ten minutes.</p>"),
      ("a8", "Plan a small, sensible set",
       "<p>Once you have the main name, consider the .com or .ai counterpart if it is available, and the most likely misspelling. Point them at your main site with permanent redirects. Resist building separate thin sites on each variation; Google's spam policies describe many near-identical sites aimed at small variations of a search as doorway abuse. Our article on <a href=\"/blog/should-a-business-own-more-than-one-domain/\">owning more than one domain</a> covers the setup.</p>"),
      ("a9", "A one-page checklist",
       "<ol><li>Decide whether this is a company name, a product name or a campaign name.</li>"
       "<li>Pick a pattern: descriptive for services, brandable for products, hybrid if you need both.</li>"
       "<li>Choose the extension for people, then check who owns the other one.</li>"
       "<li>Search the USPTO database, state records and the open web for similar names in related fields.</li>"
       "<li>Run the phone test and the checker.</li>"
       "<li>Check the domain's history before paying.</li>"
       "<li>Secure the counterpart and the obvious misspelling, and redirect them.</li></ol>"
       "<p>If the name you want is taken, it is rarely the end; <a href=\"/blog/domain-name-taken-what-now/\">here is what to do next</a>. And if you would rather hand the search to someone who does this every day, tell us about the product on <a href=\"/find-it-for-me/\">find it for me</a>. We start with the names we own, then the low-hanging fruit still open to register, then the hidden gems other people hold.</p>")],
     [("Is a .ai domain bad for SEO?", "No. Google lists .ai among the country-code extensions it treats as generic, and its SEO Starter Guide says the extension is a low-impact signal at most. The bigger risks with .ai are visitors typing .com by habit and renewal terms you have not read."),
      ("Should my AI startup put AI in its domain name?", "It is a fair choice for a service business that wants an obvious category signal. For a product that may grow or pivot, a brandable name is usually easier to protect as a trademark and less likely to date."),
      ("Do I need to own both the .ai and the .com?", "Not always, but check who owns the one you do not buy. An unrelated parked page is a minor leak; a competitor on the other extension is a reason to choose a different name."),
      ("How do I check whether an AI name is already trademarked?", "Search the USPTO's federal trademark database, your state's records and the open web for similar names used for related goods or services. A trademark attorney can run and interpret a full clearance search.")],
     [("IANA .ai delegation record", G["iana_ai"]), ("Google: multi-regional sites (generic ccTLDs)", G["multireg"]), ("Google SEO Starter Guide", G["starter"]),
      ("Verisign Domain Name Industry Brief, Q2 2026", G["dnib"]), ("USPTO: strong trademarks", G["tm_strong"]), ("USPTO: why search for similar trademarks", G["tm_search"]), ("ICANN UDRP", G["udrp"])],
     [("/domains/ai-agents/", "AI &amp; agents domains"), ("/keyword-vs-brand-domain/", "Keyword or brand?"), ("/domain-name-checker/", "Domain name checker"), ("/guides/com-vs-other-extensions/", ".com vs other extensions"), ("/find-it-for-me/", "Find it for me")],
     date="2026-10-12")

# ------------------------------------------------------------------ 7
post("choosing-a-domain-name-for-a-law-firm",
     "How to Choose a Domain Name for a Law Firm",
     "Partner names, practice-area phrases or a trade name? How the ABA model rule treats firm names and web addresses, and how to pick a law firm domain that lasts.",
     "Choosing a domain name for a law firm: the ethics rules, the practical tests and what lasts.",
     "Legal names",
     "A law firm's domain is not just marketing. Under the ABA's model rules it counts as a professional designation, which means the same not-misleading standard that applies to your letterhead applies to your web address. Here is how to pick one that passes both the ethics test and the phone test.",
     ("#141d4a", "#2246b8", "yourfirm.com", "A law firm's name on an office door and a web address", "Name, not slogan."),
     [("l1", "Your domain is a professional designation",
       f"<p>The ABA's {_x('aba71', 'comment to Model Rule 7.1')} says firm names, letterhead and professional designations are communications about a lawyer's services. It allows a firm to be designated by the names of some or all of its current members, by the names of deceased members where there has been a succession in the firm's identity, or by a trade name that is not false or misleading. It then adds the line that matters here: a lawyer or law firm may also be designated by a distinctive website address, social media username or comparable professional designation that is not misleading.</p>"
       "<p>In plain terms, your domain is judged like your firm name. Two caveats before going further. First, the model rules are a template; your state's adopted version is what binds you, and some states restrict trade names more tightly than the model rule does. Second, this article is practical guidance from people who sell domains, not legal advice. If a name feels borderline, ask your state bar's ethics hotline before you buy it.</p>"),
      ("l2", "What makes a law firm name misleading",
       "<p>The same ABA comment lists the classic problems. A firm name or designation is misleading if it implies a connection with:</p>"
       "<ul><li>a government agency,</li><li>a deceased lawyer who was not a former member of the firm,</li><li>a lawyer not associated with the firm or a predecessor firm,</li><li>a nonlawyer, or</li><li>a public or charitable legal services organization.</li></ul>"
       "<p>It also flags geographic trade names. Its example is a name like Springfield Legal Clinic, which may need an express statement that the firm is not a public legal aid organization. Translate that to domains and a few patterns deserve a second look: anything with words like <em>legal aid</em>, <em>public defender</em>, <em>county</em> or <em>state</em> that could suggest an official body, and anything that borrows the name of a lawyer who is not at your firm.</p>"
       "<p>Superlatives are the other trap. The comment to Rule 7.1 warns that an unsubstantiated claim or comparison about a lawyer's services can be misleading if it is presented with enough specificity that a reasonable person would think it can be substantiated. A domain that calls a firm the best or the top in a city is a claim. Whether a given name crosses the line depends on your jurisdiction, so check before you build a practice on it.</p>"),
      ("l3", "The three patterns that work",
       "<p><strong>Partner surnames.</strong> The traditional choice, and the most clearly permitted. It is also the most fragile online: surnames are often hard to spell after hearing them once, long multi-partner names make long domains, and a name partner leaving raises questions under your state's rules. If you go this way, consider a short form people actually say.</p>"
       "<p><strong>Practice area plus place.</strong> Names in the form of a practice and a city, such as a DUI attorney or divorce lawyer name for one town, explain themselves to a caller and are easy to remember from a radio spot or a bus bench. They are descriptive, so they are weak as trademarks, and they tie you to one practice and one market. Many firms use one as a second front door that redirects to the main site.</p>"
       "<p><strong>A trade name.</strong> Permitted in many jurisdictions if it is not misleading, and the most flexible as a brand. Check your state's version of the rule first, and make sure the trade name appears consistently on letterhead, signage and filings, not only in the web address.</p>"
       "<p>You can see real examples of the second pattern on our <a href=\"/domains/legal/\">legal and mediation domain names</a> page, including a cluster of <a href=\"/domains/greeley-lawyers/\">Greeley, Colorado lawyer names</a>. Every one is owner-direct and negotiable.</p>"),
      ("l3b", "A note for solo practitioners",
       "<p>Solo lawyers have the simplest path and often overthink it. Your own name plus a short word such as <em>law</em> or the practice area is clearly permitted under the model rule's approach to member names, is easy to say in court and on the phone, and moves with you if you later join or start a firm. If your full name is long or often misspelled, test a shorter form, such as first initial and surname, and redirect the full version to it.</p>"
       "<p>What to avoid as a solo: a name that sounds like a large firm with several partners when there is one lawyer, or a plural like <em>attorneys</em> or <em>group</em> that could suggest colleagues you do not have. Under a not-misleading standard, a domain that overstates the size of a practice is exactly the kind of thing to check with your state bar first.</p>"),
      ("l4", "The practical tests",
       "<p>Once a name clears the ethics question, it still has to work in the real world. Clients often hear a firm's name in a stressful moment, from a friend, a referral or a phone call, and then type it from memory.</p>"
       "<ul><li><strong>The phone test.</strong> Say it once and see whether someone can type it. Hyphens, numerals, doubled letters at word breaks and unusual surname spellings all leak clients. Our <a href=\"/domain-name-checker/\">domain name checker</a> shows exactly where a name loses points.</li>"
       "<li><strong>Length.</strong> Shorter is easier to say, print and type on a phone. A practice-and-city name can still be short if both words are common.</li>"
       f"<li><strong>Extension.</strong> Google's {_x('starter', 'SEO Starter Guide')} says the extension only matters for country targeting, and even then it is a low-impact signal. People still type .com by habit, so if you choose another extension, check who owns the .com version. If any legal-specific extension interests you, read its registry's eligibility rules first.</li>"
       "<li><strong>Email.</strong> You will read this domain aloud in every email address you give out. If it is awkward to spell for a court clerk, it is the wrong domain.</li></ul>"),
      ("l5", "Do not rename your Google profile to match the domain",
       f"<p>A descriptive domain does not change what you can call yourself on Google Maps. Google's {_x('gbp', 'guidelines for representing your business')} say the profile name should reflect the business's real-world name as used on its storefront, website and stationery, and that adding unnecessary information to the name is not permitted and can lead to suspension. If your firm is Martinez &amp; Cole, your profile is Martinez &amp; Cole, even if your redirect domain says DUI lawyer Greeley.</p>"
       "<p>That is a reason to choose the main domain to match the name you actually practise under, and to use descriptive names as secondary doors rather than as a back door to a keyword-stuffed listing.</p>"),
      ("l6", "One site, several doors",
       f"<p>Firms with several practice areas are often tempted to build a separate small site on each descriptive domain. Two problems. Every one of those sites is attorney advertising and has to meet your state's rules. And a set of thin, near-identical sites aimed at slight variations of the same search is what Google's {_x('spam', 'spam policies')} call doorway abuse. The cleaner setup is one strong main site with a genuinely useful page for each practice area, and any extra domains pointed at the matching page with permanent redirects. Our article on <a href=\"/blog/should-a-business-own-more-than-one-domain/\">owning more than one domain</a> shows how to set that up.</p>"),
      ("l7", "Before you buy",
       f"<ol><li>Check your state's version of Rule 7.1 and any ethics opinions on trade names and web addresses.</li>"
       f"<li>Search the {_x('tm_search', 'USPTO trademark database')} and your state's business records for similar names in legal services.</li>"
       "<li>Check the domain's past on the Wayback Machine and with a site: search. A law firm does not want to inherit a spam history; our <a href=\"/blog/check-a-domains-history-before-you-buy/\">history checklist</a> takes ten minutes.</li>"
       "<li>Confirm the name works on letterhead, a business card, an email signature and a voicemail greeting.</li>"
       "<li>Put it on auto-renew with the registrar lock and two-factor login on.</li></ol>"
       "<p>If you know the practice and the market but not the name, tell us on <a href=\"/find-it-for-me/\">find it for me</a>. We look at our own names first, then what is still open to register, then the hidden gems held by other owners, and we will tell you plainly if a name you like looks risky.</p>")],
     [("Can a law firm use a domain name that is not the firm's name?", "Under the ABA model rule, a firm may be designated by a distinctive website address that is not misleading. Your state's version of the rule controls, so check it and any related ethics opinions before you rely on a descriptive or trade-name domain."),
      ("Is it allowed to use best or top in a law firm domain?", "It is risky. The comment to ABA Model Rule 7.1 says unsubstantiated claims or comparisons can be misleading. Whether a particular name crosses the line depends on your jurisdiction, so ask your state bar before buying one."),
      ("Can I put my practice area in my Google Business Profile name?", "Only if it is genuinely part of your real-world business name. Google's guidelines say adding unnecessary information to the name is not permitted and can lead to suspension."),
      ("Should a law firm have a separate website for each practice area?", "Usually not. One main site with a strong page for each practice area is easier to keep compliant, and extra domains can redirect to those pages instead of hosting thin copies.")],
     [("ABA: Comment on Model Rule 7.1", G["aba71"]), ("Google Business Profile guidelines", G["gbp"]), ("Google spam policies", G["spam"]), ("Google SEO Starter Guide", G["starter"]),
      ("USPTO: why search for similar trademarks", G["tm_search"])],
     [("/domains/legal/", "Legal &amp; mediation domains"), ("/domains/greeley-lawyers/", "Greeley lawyer names"), ("/domain-name-checker/", "Domain name checker"), ("/blog/check-a-domains-history-before-you-buy/", "Check a domain's history"), ("/find-it-for-me/", "Find it for me")],
     date="2026-10-12")

# ------------------------------------------------------------------ 8
post("how-to-name-a-home-services-business",
     "How to Name a Home Services Business (and Its Domain)",
     "Naming a roofing, painting, fencing or cleaning company? How to pick a name and domain that work on a truck, a phone call, Google Maps and your state filing.",
     "How to name a home services business, and pick a domain that fits it.",
     "Naming a business",
     "A roofer's name has to work in places a software brand never sees: a truck door at forty miles an hour, a yard sign, a rushed phone call, an invoice. Here is a practical way to choose a home services name and a domain that fits it, with the rules from Google and the state that most people find out about too late.",
     ("#5a2a06", "#f26b1d", "yourtrade.com", "A home services truck with a business name and web address", "Built for the truck."),
     [("h1", "Where a home services name has to work",
       "<p>Most naming advice is written for apps. A painter, fence builder, mover or house cleaner has a different set of tests, and the name either passes them or quietly costs calls for years:</p>"
       "<ul><li><strong>The truck and the yard sign.</strong> Read at a distance, often for a second or two. Short words, no hyphens, nothing that needs explaining.</li>"
       "<li><strong>The phone.</strong> Customers hear your name from a neighbour and type it later. If they get it wrong, the call goes to whoever ranks for the misspelling.</li>"
       "<li><strong>Google Maps.</strong> Your profile name has rules (more on that below), and it must match what is on the truck.</li>"
       "<li><strong>The paperwork.</strong> Licences, insurance certificates, invoices and your state filing should all carry the same name.</li></ul>"),
      ("s2", "Three kinds of name, and what each costs you",
       "<p><strong>Your own name</strong>, as in Ortega Plumbing. Personal, trustworthy, easy to protect. The cost: it says nothing about where you work, unusual surnames are hard to spell, and it can be harder to sell the business later because the name is you.</p>"
       "<p><strong>A brand</strong>, a memorable word or phrase. Flexible and easier to protect. The cost: it takes longer for people to connect the name with the trade, so you spend more on signage and ads early on.</p>"
       "<p><strong>A descriptive name</strong>, the service plus the place, such as a deck builder name for one Denver suburb. It explains itself on a truck and a phone call. The cost: it is weak as a trademark, and it can box you in. A company named for decks that later adds fences, or for one suburb that expands across the metro, may outgrow the name.</p>"
       "<p>A common answer is to combine them: a short company name that can grow, and a descriptive domain or two that point at the matching service pages. Our <a href=\"/keyword-vs-brand-domain/\">keyword or brand helper</a> walks through the trade-off in six questions.</p>"),
      ("s3", "The Google Maps rule most owners learn too late",
       f"<p>Google's {_x('gbp', 'guidelines for representing your business')} say your Business Profile name should reflect your real-world name, as used consistently on your storefront, website and stationery and as known to customers. They also say including unnecessary information in the name is not permitted and can lead to suspension.</p>"
       "<p>That has a direct consequence for naming. If you want the words <em>roofing</em> or <em>Denver</em> to appear in your Maps listing, they have to be part of your genuine business name, on the truck, the invoices and your filing. You cannot run as Smith Construction everywhere else and call yourself Denver Roof Repair Experts on Google. Decide early which name you will actually trade under, because changing it later means new signage, new filings and a profile that has to be re-verified.</p>"),
      ("s4", "File the name with your state",
       f"<p>Most states require you to register a name you trade under if it is not your legal name. In Colorado, the {_x('co_trade', 'Secretary of State trade name FAQ')} explains that a for-profit business using a name other than its true entity name, or an individual using a name other than their legal first and last name, must file a statement of trade name. The same page notes that a trade name cannot be reserved in advance.</p>"
       f"<p>A trade name filing is not a trademark. The Colorado Secretary of State's {_x('co_tm', 'trademark FAQ')} treats trademarks as a separate filing, and neither one is a federal registration. If you plan to grow beyond one market, look at the USPTO database too. The USPTO explains {_x('tm_search', 'why to search for similar trademarks')}: names can conflict when they are similar and the services are related, even if they are not identical. Two fence companies with near-identical names in the same metro is exactly the confusion the law cares about, and it is bad for business even when nobody sues.</p>"),
      ("s5", "What the domain does, and does not, do",
       f"<p>A city-and-service domain will not rank you on its own. Google's {_x('starter', 'SEO Starter Guide')} says keywords in a domain name alone have hardly any effect beyond appearing in breadcrumbs. Rankings come from the site, the service pages, reviews and a consistent profile. We cover the details in <a href=\"/blog/exact-match-local-domains-what-google-says/\">exact-match domains for local businesses</a>.</p>"
       "<p>What a descriptive domain genuinely does is make you easy to remember and easy to type. Someone who saw a truck that said a painter name plus the town can find it again. That is worth a lot in a trade where most work comes from referrals, signs and repeat customers.</p>"
       "<p>Whatever you choose, run it through the phone test. Say it once; can a stranger type it? Our <a href=\"/domain-name-checker/\">domain name checker</a> scores hyphens, numerals, length and word count, and <a href=\"/blog/picking-a-business-name-that-passes-the-phone-test/\">this article on the phone test</a> explains why each one matters.</p>"),
      ("s5b", "Putting the domain on the truck",
       "<p>Once you have a domain, it should be on every vehicle, sign and invoice, and it should be printed the way people will type it. Leave off the <em>www</em> and the <em>https</em>; neither is needed and both make the line longer. If the domain joins several words, consider capitalising the start of each word on the truck so it reads at a glance, even though people will type it in lower case. Keep the phone number and the domain on the same panel, large enough to read from the next lane.</p>"
       "<p>Then make sure the address goes somewhere useful. A visitor who typed your domain from a van has one question: can you do my job, where I live, soon? Send them to a page that answers that, with your service area and a phone number at the top, not to a generic homepage slideshow.</p>"),
      ("s6", "Avoid the near-copy",
       "<p>When the obvious name is taken, the temptation is to bolt on a letter, a hyphen or a different suburb and use something that looks almost the same as a competitor's. Customers will mix you up, reviews will land on the wrong business, and you may invite a trademark complaint. Pick something clearly your own. If the name you want is held by someone who is not using it, <a href=\"/blog/how-to-buy-a-domain-someone-else-owns/\">buying it properly</a> is often cheaper than years of confusion.</p>"),
      ("s7", "A worked example",
       "<p>Imagine a painter starting out in Arvada, Colorado. She is weighing three options: her own surname plus Painting, a brand word, or a descriptive name for painters in Arvada.</p>"
       "<ul><li>She expects to work across the west metro within two years, so a name tied only to Arvada would be limiting as the <em>company</em> name.</li>"
       "<li>Her surname is easy to spell, so she trades under it, files the trade name with the state and puts it on the van and her Google profile.</li>"
       "<li>She also secures a descriptive painters-and-town domain and redirects it to her Arvada page, so people who remember the van can still find her.</li></ul>"
       "<p>One trading name everywhere, one website, one extra door. Nothing that breaks Google's rules, nothing she will outgrow.</p>"),
      ("s8", "A short checklist",
       "<ol><li>Decide which name you will genuinely trade under, on the truck, the invoices and Google.</li>"
       "<li>Check that it will still fit if you add services or towns.</li>"
       "<li>Search your state's business records and the USPTO database for similar names in your trade.</li>"
       "<li>File the trade name if it differs from your legal name.</li>"
       "<li>Choose the domain: the trading name if you can get it, plus a descriptive door if it helps people find you.</li>"
       "<li>Run the phone test, then put the domain on auto-renew with the lock on.</li></ol>"
       "<p>Browse ready-to-use names by trade on our <a href=\"/domains/home-services/\">home services and trades</a> page, or by niche: <a href=\"/domains/painters/\">painters</a>, <a href=\"/domains/decks-and-fences/\">decks and fences</a>, <a href=\"/domains/movers/\">movers</a> and <a href=\"/domains/cleaning-moving/\">cleaning and moving</a>. Most are tied to a real market such as <a href=\"/domains/denver/\">the Denver metro</a> or <a href=\"/domains/colorado/\">Colorado</a>. If yours is not there, tell us the trade and the town on <a href=\"/find-it-for-me/\">find it for me</a> and we will go looking.</p>")],
     [("Does my home services business name have to match my Google Business Profile?", "Yes. Google's guidelines say the profile name should reflect your real-world name as used on your storefront, website and stationery, and that adding unnecessary information can lead to suspension."),
      ("Do I need to register a trade name in Colorado?", "According to the Colorado Secretary of State, a for-profit business using a name other than its true entity name, or an individual using a name other than their legal name, must file a statement of trade name."),
      ("Will a city-and-service domain help my business rank?", "Not by itself. Google's SEO Starter Guide says keywords in a domain name alone have hardly any effect. A descriptive domain mainly helps people remember and type your address."),
      ("Should I name my company after my town?", "Only if you expect to stay there. A town in the company name can limit you when you expand; a town in a secondary domain that redirects to a location page does not.")],
     [("Google Business Profile guidelines", G["gbp"]), ("Colorado SOS: trade names FAQ", G["co_trade"]), ("Colorado SOS: trademarks FAQ", G["co_tm"]), ("Google SEO Starter Guide", G["starter"]),
      ("USPTO: why search for similar trademarks", G["tm_search"])],
     [("/domains/home-services/", "Home services domains"), ("/domains/painters/", "Painter names"), ("/domains/decks-and-fences/", "Deck &amp; fence names"), ("/blog/exact-match-local-domains-what-google-says/", "Exact-match local domains"), ("/find-it-for-me/", "Find it for me")],
     date="2026-10-12")


# ------------------------------------------------------------------ blog index + guides hub hooks
def _card(p):
    return (f'<a class="post" href="{p["path"]}">{_art("c" + p["slug"][:6].replace("-", ""), *p["art"])}'
            f'<span class="post-b"><h3>{p["h1"]}</h3><p>{esc(p["desc"])}</p><span class="meta">{p["section"]} &middot; {p["minutes"]} min read</span></span></a>')


_NEWEST = sorted(POSTS, key=lambda p: p["date"], reverse=True)  # stable: same-day posts keep their order


def _blog_index(s):
    cards = "<!--newposts-->" + "".join(_card(p) for p in _NEWEST) + "<!--/newposts-->"
    if "<!--newposts-->" in s:
        s = _re.sub(r"<!--newposts-->.*?<!--/newposts-->", lambda m: cards, s, count=1, flags=_re.S)
    else:
        s = s.replace('<div class="wrap"><div class="postgrid">', '<div class="wrap"><div class="postgrid">' + cards, 1)
    def fix(m):
        j = _json.loads(m.group(1))
        for x in j.get("@graph", []):
            if x.get("@type") == "Blog":
                old = [b for b in x.get("blogPost", []) if not any(b.get("url") == C.SITE + p["path"] for p in POSTS)]
                new = [{"@type": "BlogPosting", "headline": _html.unescape(_re.sub("<[^>]+>", "", p["h1"])), "url": C.SITE + p["path"], "description": p["desc"], "datePublished": p["date"]} for p in _NEWEST]
                x["blogPost"] = new + old
        return '<script type="application/ld+json">' + _json.dumps(j, ensure_ascii=False, separators=(",", ":")) + '</script>'
    s = _re.sub(r'<script type="application/ld\+json">(.*?)</script>', fix, s, count=1, flags=_re.S)
    return s


edit("blog/index.html", _blog_index)


def _guides(s):
    block = ('<!--blognew--><span class="eyebrow" style="margin-top:46px">New on the blog</span><div class="grid g2">' +
             "".join(f'<a class="card" href="{p["path"]}"><h3>{p["h1"]}</h3><p>{esc(p["desc"])}</p><span class="more">Read</span></a>' for p in _NEWEST) + '</div><!--/blognew-->')
    if "<!--blognew-->" in s:
        return _re.sub(r"<!--blognew-->.*?<!--/blognew-->", lambda m: block, s, count=1, flags=_re.S)
    return s.replace('<span class="eyebrow" style="margin-top:46px">Long reads</span>', block + '<span class="eyebrow" style="margin-top:46px">Long reads</span>', 1)


edit("guides/index.html", _guides)


def _home_blog(s):
    block = ('<!--homeblog--><section><div class="wrap"><span class="eyebrow">From the blog</span><h2 class="sec-h">Straight answers before you buy.</h2><div class="grid g3">' +
             "".join(f'<a class="card" href="{p["path"]}"><span class="kicker">{p["section"]}</span><h3>{p["h1"]}</h3><span class="more">Read it</span></a>' for p in [q for q in POSTS if q["date"] == "2026-10-11"][:3]) +
             '</div><p style="margin-top:18px"><a href="/blog/">All articles &rarr;</a></p></div></section><!--/homeblog-->')
    if "<!--homeblog-->" in s:
        return _re.sub(r"<!--homeblog-->.*?<!--/homeblog-->", lambda m: block, s, count=1, flags=_re.S)
    i = s.find('<span class="eyebrow">Straight answers</span>')
    if i < 0: return s
    j = s.rfind("<section", 0, i)
    return s[:j] + block + "\n" + s[j:]


edit("index.html", _home_blog)
