"""Word segmentation + place detection for domain names (build-time only)."""
import re
VOCAB = set("""
24 7 a ad ads advertise advertising adventure adventures affordable agencia agency agent agents agentic agentics agonist ai aio all allofus and another
answering apartment apartments app appliance appliances arizona art artyoulove attorney attraction attractions auto autoglass bath bathroom bathrooms baths
bathtubs bathtub beach beaches beauty bed beds bedliners best big bot botox boulder brand branded brands brandranker broomfield buy boat business businesses
cabarete calming campers camping car card cards carpet cars castle catering cat cats charter cheap chews chicago chip cleaner cleaning cleanse co coin
colorado com comics come alive company companies condo condos contractor contractors costa rica crotch rockets crypto custom customize dance dacono days spa
day deal deals deck decks deep sea denver design designer designers detail detailing development developers dimension directory disco discount distribute
dive diving divorce dog dogs domain domains dominican republic drops dryer dui ear educational elderly en engine entertainment erie estes park expeditions
experts facials family fence fences find finder firestone fishing flight flights flying food for frederick free fun furnace furniture galaxy game games
glass global golden golf granite greeley group guide guider guides gut haircut hair hair salon handicap hawaii health help helps highlands ranch higuey home
homes honolulu hotel hotels house houses how hotline in inclusive insurance insurances installation ideas island islands jets junk kauai kit kids la
romana land landscaping lashes law lawyer lawyers learn less life board littleton local logo logos longmont long distance love loveland luxury lyons
made mall malls mao map marketing massage massages mattress mattresses maui me med meds medellin mediation mediator mediators melatonin merchandise mind minds
mmamobile mobile monthly monument motorcycles motorhome mover movers moving my nederland news nfc niwot ny oahu okc omaha ne online optimization
orthodontics orthodontist packages package paint painter painters painting paving party paw cream peace promise pens pen pergola builders builder personalized
pet pets peptides pizza place places plata poem about probiotic probiotics promotional products pro pros properties property puerto press release releases
prices print solutions rico real estate realty realstate remodel remodeling renovation rent rental rentals repair replacement resorts resort restaurant restaurants restaurantes rock
roll roof roofers roofing rug rv sale sales salon san pedro santo domingo save scuba search seniors senior safety seo service services set setup shampoo
shirts shop shops short term shower showers simulator simulators sick silent smart snorkeling social solution sosua spa spots springs stay store stores
strategies supplement supplements surf surfing classes lessons lesson sweatshirts taco tanning tap tent the things to do thornton tire tires toilet tool top
tour tours town townhomes townhouses trailer trailers training treat truck trucks tub tubs united states usa used utah vacation vacations virtual reality
visit vivir vr wall walls walk wears website websites web wedding weight loss west westminster whats what wheat ridge wheelchair accessible windshield with
world worlds yachts yacht zachary tye wennstedt action globalaction apoem bed blog bogota california centennial chicago coder colombia comealive
conversational converts doghampoo eye toad florida guidance houston miami new york niwot oklahoma city texas txs aurora boston hightech high tech kit lakewood arvada
washer appliance get la losangeles los angeles brighton estespark highlandsranch acreage advertisingfor near cheapest county gourmet outlet free online
""".split())
VOCAB |= {"glp1","glp","1","4","247"}
VOCAB |= set("aging safely belize accounting accountant cpa dentist dental book waxing directory now url drop drops mechanic whats up junk removal nutrition flooring geo save on i hi use link mma ohau onaroll it care list headphones caberete wax up".split())

PLACES = [  # (token sequence as it appears in a name, label, region)
 ("denver","Denver","denver"),("aurora","Aurora","denver"),("littleton","Littleton","denver"),("centennial","Centennial","denver"),
 ("highlandsranch","Highlands Ranch","denver"),("lakewood","Lakewood","denver"),("arvada","Arvada","denver"),("wheatridge","Wheat Ridge","denver"),
 ("thornton","Thornton","denver"),("westminster","Westminster","denver"),("broomfield","Broomfield","denver"),("brighton","Brighton","denver"),
 ("golden","Golden","denver"),("castlerock","Castle Rock","denver"),
 ("boulder","Boulder","colorado"),("longmont","Longmont","colorado"),("loveland","Loveland","colorado"),("greeley","Greeley","colorado"),
 ("dacono","Dacono","colorado"),("erie","Erie","colorado"),("firestone","Firestone","colorado"),("frederick","Frederick","colorado"),
 ("estespark","Estes Park","colorado"),("lyons","Lyons","colorado"),("nederland","Nederland","colorado"),("niwot","Niwot","colorado"),
 ("monument","Monument","colorado"),("coloradosprings","Colorado Springs","colorado"),("colorado","Colorado","colorado"),
 ("omaha","Omaha","nebraska"),
 ("maui","Maui","hawaii"),("oahu","Oahu","hawaii"),("ohau","Oahu","hawaii"),("kauai","Kauai","hawaii"),("honolulu","Honolulu","hawaii"),
 ("bigisland","Big Island","hawaii"),("hawaii","Hawaii","hawaii"),
 ("sanpedro","San Pedro","belize"),("belize","Belize","belize"),
 ("costarica","Costa Rica","costarica"),
 ("cabarete","Cabarete","dominican"),("caberete","Cabarete","dominican"),("puertoplata","Puerto Plata","dominican"),("sosua","Sosua","dominican"),("santodomingo","Santo Domingo","dominican"),
 ("laromana","La Romana","dominican"),("higuey","Higuey","dominican"),("dominicanrepublic","Dominican Republic","dominican"),("dominican","Dominican Republic","dominican"),
 ("bogota","Bogota","colombia"),("medellin","Medellin","colombia"),("colombia","Colombia","colombia"),("puertorico","Puerto Rico","puertorico"),
 ("boston","Boston","us"),("utah","Utah","us"),("arizona","Arizona","us"),("california","California","us"),("chicago","Chicago","us"),
 ("florida","Florida","us"),("houston","Houston","us"),("miami","Miami","us"),("okc","Oklahoma City","us"),("texas","Texas","us"),
 ("losangeles","Los Angeles","us"),("usa","USA","national"),("unitedstates","United States","national"),("america","USA","national"),("ny","New York","us"),("txs","Texas","us"),
]
REGIONS = {"denver":"Denver metro","colorado":"Colorado (outside Denver metro)","nebraska":"Omaha, Nebraska","hawaii":"Hawaii",
 "belize":"Belize","costarica":"Costa Rica","dominican":"Dominican Republic","colombia":"Colombia","puertorico":"Puerto Rico",
 "us":"Other U.S. markets","national":"Nationwide (USA)","":"Not tied to a place"}

def segment(s):
    s = s.lower()
    n = len(s); best = [(0, [])] + [None]*n
    for i in range(1, n+1):
        for j in range(max(0, i-20), i):
            if best[j] is None: continue
            w = s[j:i]
            if w in VOCAB: cost = 1.0 + (0.6 if len(w) == 1 and not w.isdigit() else 0)
            elif len(w) == 1: cost = 3.0
            else: continue
            c = best[j][0] + cost
            if best[i] is None or c < best[i][0]: best[i] = (c, best[j][1] + [w])
    return best[n][1]

def words_for(domain):
    sld = domain.split(".")[0]
    out = []
    for part in sld.split("-"):
        out += segment(part)
    # merge consecutive single letters back into a run (unknown fragments)
    merged = []
    for w in out:
        if merged and len(w) == 1 and not w.isdigit() and len(merged[-1]) <= 2 and merged[-1].isalpha() and merged[-1] not in VOCAB:
            merged[-1] += w
        else: merged.append(w)
    return merged

def place_for(domain, blurb):
    w = words_for(domain)
    grams = set()
    for i in range(len(w)):
        for j in range(i+1, min(len(w), i+4)+1):
            grams.add("".join(w[i:j]))
    b = blurb.lower()
    hits = []
    for tok, label, region in PLACES:
        if tok in grams or (" " + label.lower() + ".") in b or (" " + label.lower() + ",") in b:
            hits.append((label, region))
    if not hits: return "", ""
    broad = ["Colorado", "Hawaii", "Dominican Republic", "Colombia"]
    hits.sort(key=lambda h: h[0] in broad)
    return hits[0]
