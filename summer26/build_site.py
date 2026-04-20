from __future__ import annotations

from html import escape
from pathlib import Path
from textwrap import dedent
from urllib.parse import quote


ROOT = Path(__file__).parent
SITE = ROOT / "site"


def commons_file_url(filename: str) -> str:
    return f"https://commons.wikimedia.org/wiki/Special:FilePath/{quote(filename)}"


def commons_page_url(filename: str) -> str:
    return f"https://commons.wikimedia.org/wiki/File:{quote(filename)}"


def maps_search_url(query: str) -> str:
    return f"https://www.google.com/maps/search/?api=1&query={quote(query)}"

RESEARCH_DATE = "April 17, 2026"
STAY_WINDOW = "June 28, 2026 to July 25, 2026"
STAY_NIGHTS = 27
FAMILY_MODEL = (
    "Family inventory was checked as 2 adults plus two children using common booking-engine age "
    "bands that best match ages 3 and 6."
)
GRANDPARENTS_MODEL = "Grandparents were checked as a separate room for 2 adults."


WHATSAPP_QUOTES = [
    "Hotele: Shelter",
    "Rogowo k/ Kołobrzegu też Marina w Kołobrzegu, Linea Marea - Pobierowo, Aquarius / Kołobrzeg/ Saltic/Łeba/",
    "Apollo Residence -Darlowo",
    "Saltic  resort Łeba i Grzybowo k / Kołobrzegu",
    "Czat mówi że najlepsze są Łeba,Ustka i Jastarnia.Nie najgorszy jest Kołobrzeg  W Świnoujściu hotele to Radisson Blu lub Hilton",
    "Te pokoje w Saltic w Łebie są dość siermiężne",
    "W Ustce jest niezły hotel Grand Lubicz uzdrowisko ale chyba kawałek od plaży",
    "Rosewia resort spa Jastrzębia góra",
]

INTERPRETATION_NOTES = [
    "The source note used `Shelter`; the official property appears to be `Shellter Hotel Resort & Spa` in Rogowo.",
    "The source note used `Marina w Kołobrzegu`; I treated that as `Marine Hotel` in Kołobrzeg.",
    "The source note used `Rosewia`; the resort brand is `Rosevia Resort & SPA`.",
    "Wave Międzyzdroje Resort & SPA was added as an extra comparison property.",
]


HOTELS = [
    {
        "rank": 1,
        "slug": "linea-mare-pobierowo",
        "name": "Linea Mare",
        "town": "Pobierowo",
        "town_slug": "pobierowo",
        "image": "https://r.profitroom.pl/lineamarepobierowo/images/202306201532590.zdj_cie_startowe.jpg",
        "image_credit": "Official hotel image",
        "signal": "Verified directly in the live booking engine",
        "signal_class": "verified",
        "headline": "Best overall match for the exact family layout you described.",
        "summary": (
            "This is the cleanest all-around fit I found. The resort openly positions itself as a "
            "rooms-and-apartments property by the sea, has strong kid infrastructure, and returned live "
            "inventory for both the parents-with-kids unit and a separate grandparents room across the full "
            "27-night sample window."
        ),
        "why_it_works": [
            "Official site explicitly offers both rooms and apartments.",
            "Family infrastructure is unusually strong: playroom, playground, kids water zone, family sauna, animations, and kids treatments.",
            "Live availability check returned family-sized options and adult-only room options for the same long stay.",
        ],
        "family_fit": [
            "Best for a hotel-connected stay where you still want apartment-style breathing room.",
            "Apartment categories exist, but the exact kitchenette specification still needs confirmation on the exact room category before paying.",
        ],
        "availability": [
            "Family search returned `Deluxe Plus Room*****` (5), `Family Room` (5), `Family Room Plus` (5), `Grand Apartment*****` (1), and `Premium Apartment***** with terrace` (1).",
            "Grandparents-room search returned separate adult inventory, including `Standard Room` (3) and `Deluxe Room*****` (5), plus larger categories.",
            f"Snapshot date: {RESEARCH_DATE}. Window checked: {STAY_WINDOW} ({STAY_NIGHTS} nights).",
        ],
        "watchouts": [
            "The best-fitting apartment categories may be expensive for a nearly full-month stay.",
            "Confirm kitchenette details before booking; the site clearly has apartments, but not every apartment label explicitly says kitchenette.",
        ],
        "sources": [
            ("Official hotel site", "https://www.lineamare.pl/en/"),
            (
                "Live family availability search",
                "https://booking.profitroom.com/en/lineamarepobierowo/pricelist/offers/?check-in=2026-06-28&check-out=2026-07-25&currency=PLN&r1_adults=2&r1_child0-3=1&r1_child4-12=1",
            ),
        ],
    },
    {
        "rank": 2,
        "slug": "rosevia-resort-spa",
        "name": "Rosevia Resort & SPA",
        "town": "Jastrzębia Góra",
        "town_slug": "jastrzebia-gora",
        "image": "https://r.profitroom.pl/roseviaresortspa/images/202503180818550.Rosevia_basen_dron_5_.jpg",
        "image_credit": "Official resort image",
        "signal": "Verified directly in the live booking engine",
        "signal_class": "verified",
        "headline": "Best apartment-first option if privacy and space matter more than classic hotel corridors.",
        "summary": (
            "Rosevia is the strongest true-resort apartment concept in the shortlist. The official site describes "
            "apartments in multiple houses, terraces or balconies, private beach access, heated pools, and a kids club. "
            "The live booking engine also returned a deep inventory of apartment categories for the long July window."
        ),
        "why_it_works": [
            "Apartment-led resort format suits parents with two small kids especially well.",
            "Private beach access and kids club make it feel more destination-like than a standard hotel.",
            "Verified long-stay inventory existed for both family and adult-only searches.",
        ],
        "family_fit": [
            "Probably the best pick if you want the grandparents close by but still want real separation and quiet at night.",
            "The resort format is likely easier for a micro-kitchen or kitchenette need than classic hotel-first properties.",
        ],
        "availability": [
            "Family search returned `Chillout Apartment` (7), `Chillout Plus Apartment` (7), `Chillout Garden Apartment` (2), `Comfort Apartment` (9), `Comfort Plus Apartment` (8), `Comfort Garden Apartment` (3), and `Premium Garden Apartment` (1).",
            "Separate adult-only inventory also showed up across the same period.",
            f"Snapshot date: {RESEARCH_DATE}. Window checked: {STAY_WINDOW} ({STAY_NIGHTS} nights).",
        ],
        "watchouts": [
            "This is more of a resort village feel than a single conventional hotel building.",
            "Jastrzębia Góra is beautiful, but some beach access in the area can involve more stairs and elevation than flatter towns.",
        ],
        "sources": [
            ("Official resort site", "https://www.rosevia.pl/en/"),
            (
                "Live family availability search",
                "https://booking.profitroom.com/en/roseviaresortspa/pricelist/offers/?check-in=2026-06-28&check-out=2026-07-25&currency=PLN&r1_adults=2&r1_child0-3=1&r1_child4-12=1",
            ),
        ],
    },
    {
        "rank": 3,
        "slug": "saltic-grzybowo",
        "name": "Saltic Resort & Spa Grzybowo",
        "town": "Grzybowo",
        "town_slug": "grzybowo",
        "image": "https://r.profitroom.pl/salticclubresort/images/202405221108340.Saltic_Grzybowo_summer_24_061.jpg",
        "image_credit": "Official resort image",
        "signal": "Verified directly in the live booking engine",
        "signal_class": "verified",
        "headline": "Excellent calmer-beach option near Kołobrzeg, with the clearest kitchenette wording of the shortlist.",
        "summary": (
            "Grzybowo gives you a quieter base than Kołobrzeg while staying close to city infrastructure. The biggest "
            "advantage here is that the live inventory explicitly included a `Premium Apartment with Kitchenette`, which "
            "maps neatly to your parents-plus-kids setup."
        ),
        "why_it_works": [
            "Quiet location is helpful with a 3-year-old and 6-year-old.",
            "Kitchenette appears directly in one live room category, which is a major practical win.",
            "The same long-stay search also returned adult-only room inventory for grandparents.",
        ],
        "family_fit": [
            "Strong practical pick if the kitchenette requirement is close to non-negotiable.",
            "The apartment-and-hotel hybrid is not as polished as Rosevia, but the logistics may be easier.",
        ],
        "availability": [
            "Family search returned `Standard Room with Balcony or Terrace` (50), `One-Bedroom Apartment` (9), `Premium Apartment with Kitchenette` (10), and `Two-Level One-Bedroom Apartment` (15).",
            "Grandparents-room search returned adult inventory including `Standard Room with Balcony or Terrace` (50), `Superior Room` (5), and `Superior Plus Room` (6).",
            f"Snapshot date: {RESEARCH_DATE}. Window checked: {STAY_WINDOW} ({STAY_NIGHTS} nights).",
        ],
        "watchouts": [
            "If you want a bigger promenade or lots of walkable city-life, Grzybowo is quieter than Kołobrzeg, not busier.",
            "The resort feel is family-friendly, but not as distinctly luxurious as the top two.",
        ],
        "sources": [
            ("Official resort site", "https://www.hotelsaltic.pl/grzybowo/en"),
            (
                "Live family availability search",
                "https://booking.profitroom.com/en/salticclubresort/pricelist/offers/?check-in=2026-06-28&check-out=2026-07-25&currency=PLN&r1_adults=2&r1_child0-3=1&r1_child4-12=1",
            ),
        ],
    },
    {
        "rank": 4,
        "slug": "saltic-leba",
        "name": "Saltic Resort & Spa Łeba",
        "town": "Łeba",
        "town_slug": "leba",
        "image": "https://r.profitroom.pl/salticresortspaleba/images/202309151849420.Hotel_Saltic_Leba_020.jpg",
        "image_credit": "Official resort image",
        "signal": "Verified directly in the live booking engine",
        "signal_class": "verified",
        "headline": "A strong functional pick in a very family-friendly town, with one finish caveat.",
        "summary": (
            "Łeba is one of the strongest towns in the note set, and the Saltic booking engine did return "
            "real long-stay availability for family and adult-only configurations. Functionally it works. The main hesitation "
            "is the source-note warning that some of the Łeba rooms feel a bit plain."
        ),
        "why_it_works": [
            "Łeba is a very family-friendly town because of the dunes, beach scale, and excursion value.",
            "The resort returned multiple apartment and room categories for the long July window.",
            "Grandparents-room availability also appeared in the same period.",
        ],
        "family_fit": [
            "Good if town quality matters almost as much as the property itself.",
            "Apartment categories exist, but the exact kitchenette situation should still be checked against the exact room type.",
        ],
        "availability": [
            "Family search returned `One-Bedroom Apartment` (54), `Two-Level One-Bedroom Apartment` (36), and `Superior Room with balcony or terrace` (42).",
            "Grandparents-room search returned adult inventory including `Standard Room` (11), `Superior Room with balcony or terrace` (42), and several larger premium categories.",
            f"Snapshot date: {RESEARCH_DATE}. Window checked: {STAY_WINDOW} ({STAY_NIGHTS} nights).",
        ],
        "watchouts": [
            "The source notes described the Łeba Saltic rooms as `dość siermiężne`, so I would expect the finish to matter less than the location.",
            "Łeba can feel busier and more seasonal than calmer western coast towns.",
        ],
        "sources": [
            ("Official resort site", "https://www.hotelsaltic.pl/leba/en"),
            (
                "Live family availability search",
                "https://booking.profitroom.com/en/salticresortspaleba/pricelist/offers/?check-in=2026-06-28&check-out=2026-07-25&currency=PLN&r1_adults=2&r1_child0-3=1&r1_child4-12=1",
            ),
        ],
    },
    {
        "rank": 5,
        "slug": "wave-miedzyzdroje",
        "name": "Wave Międzyzdroje Resort & SPA",
        "town": "Międzyzdroje",
        "town_slug": "miedzyzdroje",
        "image": "https://wavemiedzyzdroje.pl/wp-content/uploads/2024/05/about_us_photo1.jpg",
        "image_credit": "Official resort image",
        "signal": "Strong fit from the official site, but live July inventory was not fully verified",
        "signal_class": "strong",
        "headline": "The strongest premium wild-card: very likely to fit, but it needs manual inventory confirmation.",
        "summary": (
            "Wave absolutely deserves to be in the serious shortlist. The official site "
            "positions it as a luxury resort with spacious apartments by the beach, and the children page shows a real kids zone "
            "rather than token family marketing. It looks structurally very close to what you want. I just could not complete a "
            "clean July inventory proof at the same level as the Profitroom properties above."
        ),
        "why_it_works": [
            "Official site explicitly says apartments by the beach, plus spa and food.",
            "Kids page highlights a dedicated indoor zone with climbing wall, foam pool, and soft-play area.",
            "Międzyzdroje is a genuinely strong family town for beach time plus light outings.",
        ],
        "family_fit": [
            "Potentially one of the best experiences if budget is less sensitive and apartment quality matters a lot.",
            "Because the inventory proof is softer here, I would treat Wave as a premium shortlist item, not the safest booking lead.",
        ],
        "availability": [
            "I confirmed the official booking flow exists, but I did not capture the same hard room-count snapshot that I got for Linea Mare, Rosevia, and the Saltic properties.",
            "Conclusion: strong product fit, weaker availability certainty.",
            f"Research snapshot date: {RESEARCH_DATE}.",
        ],
        "watchouts": [
            "Likely one of the pricier options in the whole study.",
            "Do not assume kitchenette or grandparents-room availability without checking the exact apartment offer.",
        ],
        "sources": [
            ("Official resort site", "https://wavemiedzyzdroje.pl/"),
            ("Children page", "https://wavemiedzyzdroje.pl/dla-dzieci/"),
        ],
    },
    {
        "rank": 6,
        "slug": "apollo-residence",
        "name": "Apollo Residence",
        "town": "Darłówko / Darłowo",
        "town_slug": "darlowo-darlowko",
        "image": "https://apollo.masterm.pl/wp-content/plugins/react-integration/build/images/hero-apollo-morze-1-min.jpg",
        "image_credit": "Official residence image",
        "signal": "Promising apartment fit, but booking and hotel-service integration need manual confirmation",
        "signal_class": "strong",
        "headline": "A high-upside apartment choice if space matters most and hotel-style service matters less.",
        "summary": (
            "Apollo Residence looks very good from an apartment point of view. The official site highlights seaside apartments "
            "roughly 38 to 120 square meters in size, which is exactly the kind of space profile that works for parents with two "
            "young kids. The catch is that the site behaves more like an apartment residence or development-style presentation than "
            "a straightforward hotel booking system."
        ),
        "why_it_works": [
            "Large apartment sizes suggest comfortable real-world living for a longer family stay.",
            "Darłówko is calmer than the busiest flagship resort towns.",
            "Good option if a micro-kitchen or self-sufficient space matters more than spa theatrics.",
        ],
        "family_fit": [
            "Very attractive if the core requirement is an apartment first, hotel second.",
            "Much weaker if you want a clearly integrated resort setup with easy multi-room online booking.",
        ],
        "availability": [
            "I found an inquiry-oriented flow rather than a clean public hotel inventory engine.",
            "That means this property needs direct manual confirmation for late June and July.",
        ],
        "watchouts": [
            "Weakest online availability transparency among the serious contenders.",
            "The site does not make hotel-connected service levels as clear as Rosevia, Linea Mare, or Saltic.",
        ],
        "sources": [
            ("Official residence site", "https://apollo.masterm.pl/"),
        ],
    },
    {
        "rank": 7,
        "slug": "aquarius-spa",
        "name": "Hotel Aquarius SPA",
        "town": "Kołobrzeg",
        "town_slug": "kolobrzeg",
        "image": "https://www.aquariusspa.pl/wp-content/uploads/2024/06/28/opengraph-2zip7j.png",
        "image_credit": "Official hotel image",
        "signal": "Very strong family-hotel signal, but the exact July apartment setup was not directly verified",
        "signal_class": "strong",
        "headline": "Best Kołobrzeg hotel-first candidate if you are willing to trade some apartment certainty for family amenities.",
        "summary": (
            "Aquarius looks like a genuinely family-capable 5-star resort. The official navigation clearly exposes an `Apartment` "
            "category, and the children section highlights attractions, amenities, animations, and baby support. If you decide that "
            "a strong hotel with an apartment option is good enough, Aquarius becomes much more compelling."
        ),
        "why_it_works": [
            "Apartment category exists on the official site.",
            "Children programming is unusually explicit, including animations and baby-oriented amenities.",
            "Aquacenter, spa, and hotel scale make grandparents logistics easier than at smaller boutique properties.",
        ],
        "family_fit": [
            "Strong if you want a proper resort with lots of weather-proof infrastructure.",
            "Still needs exact-room confirmation if kitchenette is essential.",
        ],
        "availability": [
            "The site clearly uses a booking engine, but I did not complete a hard long-stay room-count verification.",
            "Conclusion: high-confidence product fit, medium-confidence date fit.",
        ],
        "watchouts": [
            "Kołobrzeg is convenient, but it is also more urban and more hotel-heavy than the best apartment-first options.",
            "Do not assume every `Apartment` category includes a micro-kitchen.",
        ],
        "sources": [
            ("Official hotel site", "https://www.aquariusspa.pl/en/"),
            ("Apartment page", "https://www.aquariusspa.pl/en/hotel-aquarius-spa/apartment/"),
            ("Children section", "https://www.aquariusspa.pl/en/hotel-aquarius-spa/for-kids/"),
        ],
    },
    {
        "rank": 8,
        "slug": "shellter-rogowo",
        "name": "Shellter Hotel Resort & Spa",
        "town": "Rogowo",
        "town_slug": "rogowo",
        "image": "https://hotelshellter.pl/wp-content/uploads/2024/11/shellter-hotel-resort-and-spa-logo.webp",
        "image_credit": "Official hotel image",
        "signal": "Good family-resort signal, but apartment depth is less clear than the top group",
        "signal_class": "strong",
        "headline": "A plausible quiet-family resort, but weaker than the top shortlist on apartment evidence.",
        "summary": (
            "The Shellter official site leans heavily into family-with-children positioning and mentions a playroom, game room, "
            "children’s water zone, and animations. As a family resort it makes sense. What I could not prove as strongly is that "
            "it solves your exact apartment-plus-grandparents-room layout better than the properties ranked above it."
        ),
        "why_it_works": [
            "Quieter Rogowo setting can be attractive with small children.",
            "Official family positioning is explicit rather than vague.",
            "Beach proximity is a major plus.",
        ],
        "family_fit": [
            "Worth considering if you want a quiet coast segment and a straightforward family resort.",
            "Less compelling if the apartment-with-micro-kitchen requirement is central.",
        ],
        "availability": [
            "Official booking page exists, but I did not capture the same hard long-stay inventory proof as the top verified group.",
            "Use this one as a secondary shortlist candidate, not the first call.",
        ],
        "watchouts": [
            "The source note used the name `Shelter`; the official property name appears to be `Shellter`.",
            "The official evidence for apartment depth is weaker than at Rosevia, Linea Mare, or Saltic Grzybowo.",
        ],
        "sources": [
            ("Official hotel site", "https://hotelshellter.pl/en/homepage/"),
            ("Reservation page", "https://hotelshellter.pl/en/reservation/"),
        ],
    },
    {
        "rank": 9,
        "slug": "grand-lubicz",
        "name": "Grand Lubicz Uzdrowisko",
        "town": "Ustka",
        "town_slug": "ustka",
        "image": "https://r.profitroom.pl/grandlubiczuzdrowiskoustka3/images/201602260940580._DSC4569.jpg",
        "image_credit": "Official hotel image",
        "signal": "Big-resort family option with a pricing signal, but not the cleanest apartment match",
        "signal_class": "strong",
        "headline": "A very good hotel recommendation, but not one of the best apartment recommendations.",
        "summary": (
            "The source notes flagged Grand Lubicz as a solid Ustka option and also warned that it is probably a bit away "
            "from the beach. My research agrees with the overall shape: this looks like a strong, infrastructure-heavy family resort "
            "with pools and wellness, but not an obvious apartment-first solution."
        ),
        "why_it_works": [
            "Strong all-weather infrastructure is helpful with kids and grandparents.",
            "Ustka itself is a pleasant family town with a good mix of beach and town convenience.",
            "I did capture a public pricing signal for the long stay, so it does not look immediately blocked out.",
        ],
        "family_fit": [
            "Best if you would accept a great hotel plus adjoining room logic instead of an ideal apartment setup.",
            "Weaker if kitchenette and flexible in-room living matter a lot.",
        ],
        "availability": [
            "A public pricing snapshot for 2 adults and 1 room over the long stay came back around USD 4,824 to USD 6,278.",
            "I did not verify the exact apartment-plus-grandparents-room configuration end to end.",
        ],
        "watchouts": [
            "Beach position is not as immediate as the best beachfront picks.",
            "This is more of a wellness resort than an apartment-led family base.",
        ],
        "sources": [
            ("Official hotel site", "https://www.grandlubicz.pl/en"),
        ],
    },
    {
        "rank": 10,
        "slug": "marine-hotel",
        "name": "Marine Hotel",
        "town": "Kołobrzeg",
        "town_slug": "kolobrzeg",
        "image": "",
        "image_credit": "",
        "signal": "Hotel-first option inferred from the source notes",
        "signal_class": "manual",
        "headline": "A respectable Kołobrzeg resort, but not the shape I would pick first for your layout.",
        "summary": (
            "I treated the note `Marina w Kołobrzegu` as Marine Hotel. The official site shows a big-service seaside hotel with a "
            "Kids Club, beach proximity, bowling, and lots of activity. That makes it easy to imagine as a pleasant vacation. It still "
            "reads more like a hotel-first decision than the apartment-leaning options above it."
        ),
        "why_it_works": [
            "Strong resort infrastructure and a direct seaside setting.",
            "Good if grandparents want a classic hotel experience.",
            "Kołobrzeg is easy from a logistics and convenience perspective.",
        ],
        "family_fit": [
            "Better if you are willing to soften the apartment requirement.",
            "Worse than the top group if the parents-and-kids unit really needs apartment living.",
        ],
        "availability": [
            "I did not capture a trustworthy long-stay July inventory proof for Marine itself.",
            "Treat this as a fallback hotel candidate rather than a lead booking target.",
        ],
        "watchouts": [
            "Name inference: the source notes said `Marina`; I mapped that to `Marine Hotel`.",
            "Kołobrzeg has many neighboring apartment products, which may actually be better for your needs than the core hotel.",
        ],
        "sources": [
            ("Official hotel site", "https://zdrojowahotels.pl/en/marine-hotel"),
        ],
    },
    {
        "rank": 11,
        "slug": "hilton-swinoujscie",
        "name": "Hilton Świnoujście Resort & Spa",
        "town": "Świnoujście",
        "town_slug": "swinoujscie",
        "image": "",
        "image_credit": "",
        "signal": "High-quality resort, but very likely the wrong shape unless you pivot away from apartment-first",
        "signal_class": "manual",
        "headline": "Excellent resort quality, weaker alignment to the apartment-and-kitchen priority.",
        "summary": (
            "The source notes named Hilton and Radisson for Świnoujście, and the Hilton clearly belongs on any premium resort shortlist. "
            "The official pages show a serious full-service resort inside the Baltic Park Molo complex, with strong dining, gym, and "
            "shared attraction access. The issue is not quality. The issue is fit: this is much more obviously a high-end hotel than "
            "an apartment-led family base."
        ),
        "why_it_works": [
            "Top-tier resort standards and a strong Świnoujście location.",
            "Good if grandparents prefer branded comfort and full hotel services.",
            "Large shared-complex attractions make weather days easier.",
        ],
        "family_fit": [
            "Only climbs the ranking if you are comfortable abandoning the apartment-first idea.",
            "Otherwise it stays more aspirational than practical.",
        ],
        "availability": [
            "I did not verify your exact long-stay July room mix.",
            "Treat as a premium manual-check candidate only.",
        ],
        "watchouts": [
            "Likely pricey and potentially suite-dependent for a comfortable 4-person parent-plus-kids setup.",
            "Kitchenette certainty is weak.",
        ],
        "sources": [
            ("Official Hilton site", "https://www.hilton.com/en/hotels/szzhihi-hilton-swinoujscie-resort-and-spa/"),
            ("Local resort page", "https://zdrojowahotels.pl/en/hilton-swinoujscie-resort-spa"),
        ],
    },
    {
        "rank": 12,
        "slug": "radisson-blu-swinoujscie",
        "name": "Radisson Blu Resort, Świnoujście",
        "town": "Świnoujście",
        "town_slug": "swinoujscie",
        "image": "",
        "image_credit": "",
        "signal": "Big-resort option, but not a leading fit for the apartment brief",
        "signal_class": "manual",
        "headline": "A strong mainstream resort, but I would not start here for this exact family format.",
        "summary": (
            "Radisson Blu in Świnoujście makes sense on paper because the destination is strong and the resort is a known flagship. "
            "But once I filtered everything through your actual layout needs, it ended up behind the apartment-first and verified "
            "hybrid options."
        ),
        "why_it_works": [
            "Świnoujście is one of the easiest big-beach destinations on the coast.",
            "Strong resort infrastructure is almost guaranteed.",
            "Grandparents would probably find it easy and comfortable.",
        ],
        "family_fit": [
            "Works better as a classic hotel holiday than as a long apartment-style family base.",
            "Only rises if the micro-kitchen preference becomes optional.",
        ],
        "availability": [
            "I did not confirm long-stay July availability for your exact configuration.",
            "This stayed in the study because it appeared in the source notes, not because it beat the top apartment-led properties.",
        ],
        "watchouts": [
            "Apartment certainty is weak.",
            "Compared with Wave in the same region, this one looks less naturally aligned with your stated setup.",
        ],
        "sources": [
            ("Official Radisson site", "https://www.radissonhotels.com/en-us/hotels/radisson-blu-resort-swinoujscie"),
            ("Local resort page", "https://zdrojowahotels.pl/en/radisson-blu"),
        ],
    },
]


TOWNS = [
    {
        "slug": "pobierowo",
        "name": "Pobierowo",
        "image": commons_file_url("Pobierowo-centrum.jpg"),
        "headline": "Calmer pine-and-beach resort town with one of the strongest all-around hotel matches.",
        "summary": (
            "Pobierowo feels like one of the safest middle-ground destinations in the whole study: family-friendly, coastal, not too urban, "
            "and anchored by the strongest overall hotel match I found."
        ),
        "best_for": [
            "Families who want beach rhythm without a giant city-resort atmosphere.",
            "Trips where the hotel choice matters more than nightlife or promenade scale.",
        ],
        "watchouts": [
            "Less city energy than Kołobrzeg or Świnoujście.",
            "If you want lots of external attractions every day, the town itself is not the main draw.",
        ],
        "source_links": [
            ("Wikipedia", "https://en.wikipedia.org/wiki/Pobierowo"),
            ("Local guide", "https://pobierowo.net.pl/przewodnik/11083/html?pdf="),
            ("Anchor hotel", "https://www.lineamare.pl/en/"),
        ],
    },
    {
        "slug": "jastrzebia-gora",
        "name": "Jastrzębia Góra",
        "image": commons_file_url("Lisi Jar 2.jpg"),
        "headline": "Beautiful and stylish, especially if Rosevia is the reason you go.",
        "summary": (
            "Jastrzębia Góra is less about urban convenience and more about the atmosphere: dramatic coast, a more polished resort mood, "
            "and a very strong apartment-led base in Rosevia."
        ),
        "best_for": [
            "Families who want a nicer-feeling resort environment and are happy to pay for it.",
            "Trips where the property itself is the main event.",
        ],
        "watchouts": [
            "Beach access in the area can involve more stairs and elevation.",
            "Less practical than flatter towns if anyone in the group dislikes steeper access routes.",
        ],
        "source_links": [
            ("Wikipedia", "https://pl.wikipedia.org/wiki/Jastrzębia_Góra"),
            ("Local guide", "https://www.jastrzebia.org.pl/"),
            ("Anchor resort", "https://www.rosevia.pl/en/"),
        ],
    },
    {
        "slug": "grzybowo",
        "name": "Grzybowo",
        "image": commons_file_url("Grzybowo ul. Kwiatowa 29.12.2019 p.jpg"),
        "headline": "Quiet beach base next to Kołobrzeg, with one of the easiest kitchenette answers.",
        "summary": (
            "Grzybowo is compelling because it gives you access to the Kołobrzeg region without forcing you to sleep inside the busier city. "
            "For small kids and grandparents, that can be a very useful compromise."
        ),
        "best_for": [
            "Families who want a wide beach and calmer evenings.",
            "Trips where you still want occasional Kołobrzeg convenience nearby.",
        ],
        "watchouts": [
            "Less town life on foot than Kołobrzeg itself.",
            "More of a quiet-base strategy than a promenade destination.",
        ],
        "source_links": [
            ("Wikipedia", "https://en.wikipedia.org/wiki/Grzybowo,_Kołobrzeg_County"),
            ("Local guide", "https://grzybowo.pl/"),
            ("Anchor resort", "https://www.hotelsaltic.pl/grzybowo/en"),
        ],
    },
    {
        "slug": "leba",
        "name": "Łeba",
        "image": commons_file_url("Leba Dunes.jpg"),
        "headline": "A strong family town with real summer energy and outing value.",
        "summary": (
            "Łeba is one of the most naturally family-friendly destinations in the whole list because of the dunes, beach scale, and easy excursion logic. "
            "The hotel question is slightly more mixed than the town question."
        ),
        "best_for": [
            "Families who want a memorable town and do not mind more seasonality and activity.",
            "Trips where you expect to leave the hotel and explore.",
        ],
        "watchouts": [
            "Can feel busier and more tourist-heavy in peak summer.",
            "The source notes already warned that Saltic Łeba rooms may feel plainer than the town deserves.",
        ],
        "source_links": [
            ("Wikipedia", "https://pl.wikipedia.org/wiki/Łeba"),
            ("Official town site", "http://leba.eu/pl/"),
            ("Anchor resort", "https://www.hotelsaltic.pl/leba/en"),
        ],
    },
    {
        "slug": "miedzyzdroje",
        "name": "Międzyzdroje",
        "image": commons_file_url("Molo Międzyzdroje4.JPG"),
        "headline": "Classic premium resort town with beach, promenade, and one of the most promising added options.",
        "summary": (
            "Międzyzdroje deserves its late addition. It combines a well-known resort feel with a strong premium apartment-resort candidate in Wave, "
            "plus the broader appeal of the Wolin coast."
        ),
        "best_for": [
            "Families who want a more classic flagship seaside town.",
            "Trips where the parents want something a bit nicer without giving up kid appeal.",
        ],
        "watchouts": [
            "Premium pricing is likely.",
            "Wave looks great, but the exact July inventory still needs manual confirmation.",
        ],
        "source_links": [
            ("Wikipedia", "https://pl.wikipedia.org/wiki/Międzyzdroje"),
            ("Official town site", "https://miedzyzdroje.pl/"),
            ("Anchor resort", "https://wavemiedzyzdroje.pl/"),
        ],
    },
    {
        "slug": "darlowo-darlowko",
        "name": "Darłówko / Darłowo",
        "image": commons_file_url("Darłowo, latarnia morska (HB4).jpg"),
        "headline": "Potentially very practical if apartment space outranks hotel polish.",
        "summary": (
            "Darłówko is not the flashiest town in the set, but it may be one of the more practical if you end up favoring residence-style living "
            "over full resort packaging."
        ),
        "best_for": [
            "Families who want more square footage and calmer pace.",
            "Longer stays where apartment comfort matters a lot.",
        ],
        "watchouts": [
            "Apollo needs direct availability confirmation.",
            "The hotel-service layer is less clear than at the stronger resorts.",
        ],
        "source_links": [
            ("Wikipedia", "https://pl.wikipedia.org/wiki/Darłowo"),
            ("Official town site", "https://www.darlowo.pl/"),
            ("Anchor residence", "https://apollo.masterm.pl/"),
        ],
    },
    {
        "slug": "kolobrzeg",
        "name": "Kołobrzeg",
        "image": commons_file_url("Beach in Kołobrzeg 2.jpg"),
        "headline": "The easiest city-resort base, but usually less ideal for a clean apartment-first family setup.",
        "summary": (
            "Kołobrzeg is strong on convenience, infrastructure, and bad-weather options. It is weaker on the exact seaside-apartment-resort blend "
            "you described, at least within the named shortlist."
        ),
        "best_for": [
            "Families who want lots of restaurant, promenade, and backup options.",
            "Trips where grandparents appreciate a larger resort city.",
        ],
        "watchouts": [
            "Feels more urban than the best calm-family picks.",
            "The named Kołobrzeg options are more hotel-first than apartment-first.",
        ],
        "source_links": [
            ("Wikipedia", "https://pl.wikipedia.org/wiki/Kołobrzeg"),
            ("Official town site", "https://kolobrzeg.eu/"),
            ("Aquarius", "https://www.aquariusspa.pl/en/"),
            ("Marine Hotel", "https://zdrojowahotels.pl/en/marine-hotel"),
        ],
    },
    {
        "slug": "rogowo",
        "name": "Rogowo",
        "image": "https://hotelshellter.pl/wp-content/uploads/2025/02/DSCF3886-HDR-scaled.jpg",
        "headline": "Quiet strip location that only really works if Shellter wins you over.",
        "summary": (
            "Rogowo becomes interesting because of Shellter rather than because the town itself is a giant destination draw. "
            "That can still be a plus if your real plan is `hotel + beach + rest`."
        ),
        "best_for": [
            "Families who want a quieter coast segment.",
            "Trips where the resort does most of the heavy lifting.",
        ],
        "watchouts": [
            "Less destination depth than the stronger town picks.",
            "Apartment evidence is softer here than in the top-ranked properties.",
        ],
        "source_links": [
            ("Wikipedia", "https://pl.wikipedia.org/wiki/Rogowo_(powiat_gryficki)"),
            ("Area guide", "https://www.rewita.pl/"),
            ("Shellter", "https://hotelshellter.pl/en/homepage/"),
        ],
    },
    {
        "slug": "ustka",
        "name": "Ustka",
        "image": commons_file_url("POL Ustka ul Marynarki Polskiej 203.jpg"),
        "headline": "A very good family town, especially if a big wellness hotel is acceptable.",
        "summary": (
            "Ustka remains a solid destination candidate because it works well as a family town and Grand Lubicz gives it a strong infrastructure anchor. "
            "It lands lower mainly because the best local hotel is not the cleanest fit for the apartment brief."
        ),
        "best_for": [
            "Families who would happily use a large wellness resort.",
            "Trips where the town plus hotel facilities matter more than in-room kitchen flexibility.",
        ],
        "watchouts": [
            "Grand Lubicz appears to sit a bit away from the beach.",
            "Apartment-first solutions are less obvious than in the top towns.",
        ],
        "source_links": [
            ("Wikipedia", "https://pl.wikipedia.org/wiki/Ustka"),
            ("Tourism guide", "https://ustka.travel/"),
            ("Grand Lubicz", "https://www.grandlubicz.pl/en"),
        ],
    },
    {
        "slug": "swinoujscie",
        "name": "Świnoujście",
        "image": commons_file_url("Marina żeglarska w Świnoujściu.jpg"),
        "headline": "Big-beach flagship destination with strong hotels, but weaker alignment to your room-shape requirements.",
        "summary": (
            "Świnoujście is one of the easiest towns to sell in general because the beach is huge and the resort infrastructure is obvious. "
            "The reason it ranks lower here is that the named properties in town are excellent hotels, not the best apartment-led family bases."
        ),
        "best_for": [
            "Families who want a big, easy promenade-and-beach resort city.",
            "Trips where grandparents would enjoy a polished mainstream resort experience.",
        ],
        "watchouts": [
            "The best named options are hotel-first and likely expensive.",
            "Not ideal if the kitchenette request is strong.",
        ],
        "source_links": [
            ("Wikipedia", "https://pl.wikipedia.org/wiki/Świnoujście"),
            ("Official city site", "https://www.swinoujscie.pl/"),
            ("Hilton", "https://www.hilton.com/en/hotels/szzhihi-hilton-swinoujscie-resort-and-spa/"),
            ("Radisson", "https://www.radissonhotels.com/en-us/hotels/radisson-blu-resort-swinoujscie"),
        ],
    },
    {
        "slug": "jastarnia",
        "name": "Jastarnia",
        "image": "https://www.jastarnia.eu/_t/jastarnia//Jastarnia_plaza.jpg",
        "headline": "A strong town candidate, but the notes did not include a matching hotel candidate.",
        "summary": (
            "Jastarnia stood out in the source notes as a town recommendation rather than a hotel recommendation. "
            "That makes it important to keep on the radar, but it sits outside the final ranking because there was no specific shortlisted property to verify against your layout."
        ),
        "best_for": [
            "Families who love the Hel Peninsula feel and the sea-on-one-side, bay-on-the-other geography.",
            "Trips where town character matters more than a specific resort brand.",
        ],
        "watchouts": [
            "Needs a separate hotel search; it is not fully solved by the current shortlist alone.",
            "Because there is no named property here, I did not include it in the hotel ranking.",
        ],
        "source_links": [
            ("Town reference", "https://pl.wikipedia.org/wiki/Jastarnia"),
            ("Local tourism page", "https://www.jastarnia.eu/"),
        ],
    },
]


TOWN_DETAILS = {
    "pobierowo": {
        "family_spots": [
            ("Main beach", maps_search_url("Plaża Pobierowo")),
            ("Grunwaldzka promenade", maps_search_url("Grunwaldzka Pobierowo")),
            ("Cliff walk toward Trzęsacz", maps_search_url("klif Pobierowo")),
        ],
        "gallery": [
            (
                commons_file_url("Pobierowo-centrum.jpg"),
                "Pobierowo town center",
                "Wikimedia Commons",
                commons_page_url("Pobierowo-centrum.jpg"),
            ),
            (
                commons_file_url("Pobierowo, klif 1.JPG"),
                "Pobierowo cliff edge",
                "Wikimedia Commons",
                commons_page_url("Pobierowo, klif 1.JPG"),
            ),
        ],
    },
    "jastrzebia-gora": {
        "family_spots": [
            ("North Star monument", maps_search_url("Gwiazda Północy Jastrzębia Góra")),
            ("Lisi Jar gorge", maps_search_url("Lisi Jar Jastrzębia Góra")),
            ("Beach access near Rozewie", maps_search_url("plaża Rozewie")),
        ],
        "gallery": [
            (
                commons_file_url("Obelisk Gwiazda Polnocy 1.jpg"),
                "North Star monument",
                "Wikimedia Commons",
                commons_page_url("Obelisk Gwiazda Polnocy 1.jpg"),
            ),
            (
                commons_file_url("Lisi Jar 2.jpg"),
                "Lisi Jar ravine",
                "Wikimedia Commons",
                commons_page_url("Lisi Jar 2.jpg"),
            ),
        ],
    },
    "grzybowo": {
        "family_spots": [
            ("Grzybowo beach", maps_search_url("Plaża Grzybowo")),
            ("Cycle route to Kołobrzeg", maps_search_url("Grzybowo promenada rowerowa")),
            ("Harbor day trip in Kołobrzeg", maps_search_url("Port Kołobrzeg")),
        ],
        "gallery": [
            (
                commons_file_url("Grzybowo ul. Kwiatowa 29.12.2019 p.jpg"),
                "Grzybowo residential streets",
                "Wikimedia Commons",
                commons_page_url("Grzybowo ul. Kwiatowa 29.12.2019 p.jpg"),
            ),
        ],
    },
    "leba": {
        "family_spots": [
            ("Łeba beach", maps_search_url("Plaża Łeba")),
            ("Slowiński dunes access", maps_search_url("Wydmy Łeba Słowiński Park Narodowy")),
            ("Łeba marina", maps_search_url("Port Łeba")),
        ],
        "gallery": [
            (
                commons_file_url("Leba Dunes.jpg"),
                "Łeba dunes",
                "Wikimedia Commons",
                commons_page_url("Leba Dunes.jpg"),
            ),
        ],
    },
    "miedzyzdroje": {
        "family_spots": [
            ("Międzyzdroje pier", maps_search_url("Molo Międzyzdroje")),
            ("Promenade and beach", maps_search_url("Promenada Gwiazd Międzyzdroje")),
            ("Wolin park viewpoint", maps_search_url("Kawcza Góra Międzyzdroje")),
        ],
        "gallery": [
            (
                commons_file_url("Molo Międzyzdroje4.JPG"),
                "Międzyzdroje pier",
                "Wikimedia Commons",
                commons_page_url("Molo Międzyzdroje4.JPG"),
            ),
            (
                commons_file_url("Miedzyzdroje plaza (1).jpg"),
                "Międzyzdroje beach",
                "Wikimedia Commons",
                commons_page_url("Miedzyzdroje plaza (1).jpg"),
            ),
        ],
    },
    "darlowo-darlowko": {
        "family_spots": [
            ("Darłówko lighthouse", maps_search_url("Latarnia morska Darłówko")),
            ("Swing bridge", maps_search_url("Most rozsuwany Darłowo")),
            ("Castle in Darłowo", maps_search_url("Zamek Książąt Pomorskich Darłowo")),
        ],
        "gallery": [
            (
                commons_file_url("Darłowo, latarnia morska (HB4).jpg"),
                "Darłówko lighthouse",
                "Wikimedia Commons",
                commons_page_url("Darłowo, latarnia morska (HB4).jpg"),
            ),
            (
                commons_file_url("Darłowo, Zamek Książąt Pomorskich (HB1).jpg"),
                "Darłowo castle",
                "Wikimedia Commons",
                commons_page_url("Darłowo, Zamek Książąt Pomorskich (HB1).jpg"),
            ),
        ],
    },
    "kolobrzeg": {
        "family_spots": [
            ("Kołobrzeg beach", maps_search_url("Plaża Kołobrzeg")),
            ("Pier", maps_search_url("Molo Kołobrzeg")),
            ("Cathedral and old town", maps_search_url("Bazylika Konkatedralna Kołobrzeg")),
        ],
        "gallery": [
            (
                commons_file_url("2019 - Kołobrzeg Katedra.jpg"),
                "Kołobrzeg cathedral",
                "Wikimedia Commons",
                commons_page_url("2019 - Kołobrzeg Katedra.jpg"),
            ),
        ],
    },
    "rogowo": {
        "family_spots": [
            ("Rogowo beach", maps_search_url("Plaża Rogowo 72-330")),
            ("Lake Resko shore", maps_search_url("Jezioro Resko Przymorskie Rogowo")),
            ("Quiet walk toward Mrzeżyno", maps_search_url("Mrzeżyno plaża")),
        ],
        "gallery": [
            (
                "https://hotelshellter.pl/wp-content/uploads/2025/02/DSCF3886-HDR-scaled.jpg",
                "Rogowo beachfront setting",
                "Shellter official gallery",
                "https://hotelshellter.pl/en/homepage/",
            ),
        ],
    },
    "ustka": {
        "family_spots": [
            ("Ustka lighthouse", maps_search_url("Latarnia morska Ustka")),
            ("Harbor promenade", maps_search_url("Port Ustka")),
            ("Bluecher bunkers", maps_search_url("Bunkry Blüchera Ustka")),
        ],
        "gallery": [
            (
                commons_file_url("POL Ustka ul Marynarki Polskiej 203.jpg"),
                "Ustka promenade frontage",
                "Wikimedia Commons",
                commons_page_url("POL Ustka ul Marynarki Polskiej 203.jpg"),
            ),
            (
                commons_file_url("POL Ustka ul Grunwaldzka plac zabaw OSiR.jpg"),
                "Ustka playground",
                "Wikimedia Commons",
                commons_page_url("POL Ustka ul Grunwaldzka plac zabaw OSiR.jpg"),
            ),
        ],
    },
    "swinoujscie": {
        "family_spots": [
            ("Main beach", maps_search_url("Plaża Świnoujście")),
            ("Lighthouse", maps_search_url("Latarnia Morska Świnoujście")),
            ("Stawa Młyny", maps_search_url("Stawa Młyny Świnoujście")),
        ],
        "gallery": [
            (
                commons_file_url("Marina żeglarska w Świnoujściu.jpg"),
                "Świnoujście marina",
                "Wikimedia Commons",
                commons_page_url("Marina żeglarska w Świnoujściu.jpg"),
            ),
        ],
    },
    "jastarnia": {
        "family_spots": [
            ("Jastarnia pier", maps_search_url("Molo Jastarnia")),
            ("Bay-side walks", maps_search_url("Port Jastarnia")),
            ("Lighthouse area", maps_search_url("Latarnia morska Jastarnia")),
        ],
        "gallery": [
            (
                commons_file_url("Jastarnia pier.jpg"),
                "Jastarnia pier",
                "Wikimedia Commons",
                commons_page_url("Jastarnia pier.jpg"),
            ),
            (
                commons_file_url("Latarnia morska Jastarnia widziana od strony miasta.jpg"),
                "Jastarnia lighthouse",
                "Wikimedia Commons",
                commons_page_url("Latarnia morska Jastarnia widziana od strony miasta.jpg"),
            ),
        ],
    },
}


HOTEL_EXTERNALS = {
    "linea-mare-pobierowo": {
        "maps": maps_search_url("Hotel Linea Mare Pobierowo"),
        "booking_url": "https://www.booking.com/reviews/pl/hotel/linea-mare.html",
        "booking_snapshot": "Booking.com: 8.8/10 from 2,283 reviews.",
        "booking_praise": [
            "Guests repeatedly praise the breakfast spread, clean rooms, and the easy walk to the beach.",
            "Family-facing facilities, pools, and playground access show up often in positive reviews.",
        ],
        "booking_watch": [
            "A few reviews mention crowded peak-period breakfast service and slow problem resolution.",
            "Several guests note that the 5-star finish is not uniformly felt across every detail.",
        ],
        "tripadvisor_url": "https://www.tripadvisor.com/Hotel_Review-g652063-d25451248-Reviews-Linea_Mare-Pobierowo_Western_Pomerania_Province_Western_Poland.html",
        "tripadvisor_snapshot": "Tripadvisor: 4.1/5 from 24 reviews.",
        "tripadvisor_praise": [
            "Recent Tripadvisor reviews praise family stays, pools, spa design, and friendly staff.",
            "Modern rooms and strong food comments appear more often than weak-room complaints.",
        ],
        "tripadvisor_watch": [
            "Some guests say service consistency and housekeeping do not always feel 5-star.",
            "Noise, crowding, and family-sauna logistics came up in several lower reviews.",
        ],
    },
    "rosevia-resort-spa": {
        "maps": maps_search_url("Rosevia Resort & Spa Jastrzębia Góra"),
        "booking_url": "https://www.booking.com/reviews/pl/hotel/przyladek-rosevia-friends-amp-family-resort.pl.html",
        "booking_snapshot": "Booking.com: 8.8/10 from 125 reviews.",
        "booking_praise": [
            "Guests highlight the apartments, private beach access, breakfast quality, and family-ready grounds.",
            "The separate-bedroom layout and kitchenette-equipped apartments are a real plus for longer stays.",
        ],
        "booking_watch": [
            "Wi‑Fi reliability comes up as the main recurring issue.",
            "A few guests mention insects when sleeping with windows open near the forest.",
        ],
        "tripadvisor_url": "https://www.tripadvisor.com/Hotel_Review-g7233069-d8593897-Reviews-Rosevia_Resort_SPA-Rozewie_Pomerania_Province_Northern_Poland.html",
        "tripadvisor_snapshot": "Tripadvisor: 4.3/5 from 125 reviews.",
        "tripadvisor_praise": [
            "Tripadvisor guests like the high-spec apartments, kids care, playground, and beach setting.",
            "The official Tripadvisor description explicitly confirms fully equipped kitchenettes.",
        ],
        "tripadvisor_watch": [
            "Older reviews point to inconsistent restaurant service, AC issues, and weak Wi‑Fi.",
            "The resort mood is strong, but operational polish is not perfect at all times.",
        ],
    },
    "saltic-grzybowo": {
        "maps": maps_search_url("Hotel Saltic Resort & Spa Grzybowo"),
        "booking_url": "https://www.booking.com/reviews/pl/hotel/saltic-resort-amp-spa.html",
        "booking_snapshot": "Booking.com: about 8.4/10 from roughly 1,550 reviews.",
        "booking_praise": [
            "Review themes center on the beach access, breakfast, clean modern rooms, and family infrastructure.",
            "The kitchenette-bearing apartment categories are a meaningful practical advantage here.",
        ],
        "booking_watch": [
            "Multiple reviews mention crowding at breakfast, parking costs, and limited spa quiet time.",
            "Some guests found the wellness zone too small relative to hotel size.",
        ],
        "tripadvisor_url": "https://www.tripadvisor.com/Hotel_Review-g7675940-d17559137-Reviews-Hotel_Saltic_Resort_Spa_Grzybowo-Grzybowo_Western_Pomerania_Province_Western_Poland.html",
        "tripadvisor_snapshot": "Tripadvisor: 3.9/5 from 98 reviews.",
        "tripadvisor_praise": [
            "Tripadvisor reviews praise the beach-side setting, strong playroom, good breakfast, and modern suites.",
            "Several family reviews describe it as a very usable base with kids and dogs.",
        ],
        "tripadvisor_watch": [
            "Service consistency, noise, and extra charges are the biggest recurring negatives.",
            "Couples looking for quiet spa time often found the family-heavy atmosphere too loud.",
        ],
    },
    "saltic-leba": {
        "maps": maps_search_url("Hotel Saltic Resort & Spa Łeba"),
        "booking_url": "https://www.booking.com/reviews/pl/hotel/saltic-resort-amp-spa-leba-leba.html",
        "booking_snapshot": "Booking.com: 8.7/10 from 872 reviews.",
        "booking_praise": [
            "Booking reviewers like the forest-and-beach setting, kids animations, and the larger apartment options.",
            "Food, spa, and duplex apartments come up positively in many recent reviews.",
        ],
        "booking_watch": [
            "Weekend crowding, restaurant queues, and paid parking are recurring pain points.",
            "The tone of guest feedback fits the broader 'works, but not ultra-polished' impression.",
        ],
        "tripadvisor_url": "https://www.tripadvisor.com/Hotel_Review-g274730-d25169308-Reviews-Saltic_Resort_Spa_Leba-Leba_Pomerania_Province_Northern_Poland.html",
        "tripadvisor_snapshot": "Tripadvisor: 3.8/5 from 21 reviews.",
        "tripadvisor_praise": [
            "Tripadvisor guests like the forest location, clean bigger rooms, and family-suitable apartments.",
            "Positive reviews also mention the pool, beach access, and food quality.",
        ],
        "tripadvisor_watch": [
            "Negative reviews focus on usability of small standard rooms and crowded dining areas.",
            "Some guests felt the design worked better in photos than in practical day-to-day use.",
        ],
    },
    "wave-miedzyzdroje": {
        "maps": maps_search_url("Wave Międzyzdroje Resort & Spa"),
        "booking_url": "https://www.booking.com/reviews/pl/hotel/wave-miedzyzdroje-resort-amp-spa.html",
        "booking_snapshot": "Booking.com: about 9.0/10 from roughly 2,000 reviews.",
        "booking_praise": [
            "Guests consistently praise the apartments, sea views, beach access, breakfast, and kid appeal.",
            "Family reviews especially like the spa, animations, and the sense of a premium stay.",
        ],
        "booking_watch": [
            "The biggest complaint is operational: moving between buildings in bad weather is awkward.",
            "Crowded breakfast periods, parking cost, and occasional cleaning misses show up more than once.",
        ],
        "tripadvisor_url": "https://www.tripadvisor.com/Hotel_Review-g274732-d24145777-Reviews-Wave_Miedzyzdroje_Resort_Spa-Miedzyzdroje_Western_Pomerania_Province_Western_Poland.html",
        "tripadvisor_snapshot": "Tripadvisor: 3.9/5 from 65 reviews.",
        "tripadvisor_praise": [
            "Tripadvisor visitors like the room size, modern look, breakfast buffet, and beach position.",
            "The product still looks premium and family-friendly at the room-and-location level.",
        ],
        "tripadvisor_watch": [
            "Service organization, check-in flow, and wellness management are the most repeated complaints.",
            "This reinforces the view that the property is very attractive but less operationally proven than the top four.",
        ],
    },
    "apollo-residence": {
        "maps": maps_search_url("Apollo Residence Darłowo"),
        "booking_url": "https://www.booking.com/searchresults.html?ss=Apollo%20Residence%20Dar%C5%82owo",
        "booking_snapshot": "Booking.com: no clean direct Apollo Residence review page surfaced in this pass.",
        "booking_praise": [
            "Use Booking mainly as a search handoff here rather than as strong evidence.",
        ],
        "booking_watch": [
            "Name collision noise was high enough that I would only trust a manual address-level match.",
        ],
        "tripadvisor_url": "https://www.tripadvisor.com/Search?q=Apollo%20Residence%20Dar%C5%82owo",
        "tripadvisor_snapshot": "Tripadvisor: no stable property listing surfaced for Apollo Residence itself.",
        "tripadvisor_praise": [
            "Treat Apollo as an apartment-first manual-check option rather than a review-led choice.",
        ],
        "tripadvisor_watch": [
            "This is the weakest external-review footprint among the serious contenders.",
        ],
    },
    "aquarius-spa": {
        "maps": maps_search_url("Hotel Aquarius SPA Kołobrzeg"),
        "booking_url": "https://www.booking.com/reviews/pl/hotel/aquarius-spa.en-gb.html",
        "booking_snapshot": "Booking.com: 9.3/10 from 827 reviews.",
        "booking_praise": [
            "Guests love the breakfast, clean rooms, strong spa, and the kid-friendly resort setup.",
            "Booking also explicitly positions it as a top family choice inside Kołobrzeg.",
        ],
        "booking_watch": [
            "The main tradeoff is price versus value rather than guest dissatisfaction.",
            "It reads more like a strong hotel stay than an apartment-first stay.",
        ],
        "tripadvisor_url": "https://www.tripadvisor.com/Hotel_Review-g274727-d1541459-Reviews-Hotel_Aquarius_SPA-Kolobrzeg_Western_Pomerania_Province_Western_Poland.html",
        "tripadvisor_snapshot": "Tripadvisor: 4.4/5 from 511 reviews.",
        "tripadvisor_praise": [
            "Tripadvisor reviews praise large rooms, a strong breakfast buffet, and family-visible kid spaces.",
            "The hotel's spa and all-weather infrastructure are clear strengths.",
        ],
        "tripadvisor_watch": [
            "A minority of reviewers question whether the finish fully matches the price tag.",
            "It still looks more hotel-first than kitchenette-first.",
        ],
    },
    "shellter-rogowo": {
        "maps": maps_search_url("Shellter Hotel Resort & Spa Rogowo"),
        "booking_url": "https://www.booking.com/reviews/pl/hotel/shellter-resort-amp-spa.html",
        "booking_snapshot": "Booking.com: 9.2/10 from 305 reviews.",
        "booking_praise": [
            "Booking guests highlight the beachfront location, modern rooms, big breakfast, and family-room setup.",
            "The page itself reads as a strong new-build family resort with quiet-beach appeal.",
        ],
        "booking_watch": [
            "The evidence base is still young; this is not yet a deeply reviewed legacy property.",
        ],
        "tripadvisor_url": "https://www.tripadvisor.com/Hotel_Review-g1761255-d33342528-Reviews-Shellter_Hotel_Resort_Spa-Rogowo_Kuyavia_Pomerania_Province_Central_Poland.html",
        "tripadvisor_snapshot": "Tripadvisor: 4.3/5 from 3 reviews.",
        "tripadvisor_praise": [
            "Early Tripadvisor comments praise the location, fresh design, and easy beach access.",
        ],
        "tripadvisor_watch": [
            "The earliest detailed review flags service and buffet execution as below the design quality.",
            "With so few Tripadvisor reviews, this remains a lower-certainty read than the established top picks.",
        ],
    },
    "grand-lubicz": {
        "maps": maps_search_url("Grand Lubicz Uzdrowisko Ustka"),
        "booking_url": "https://www.booking.com/reviews/pl/hotel/grand-lubicz-uzdrowisko-ustka.en-gb.html",
        "booking_snapshot": "Booking.com: 9.3/10 from 1,167 reviews.",
        "booking_praise": [
            "Booking's guest summary is excellent: breakfast, pool complex, beach walk, and family facilities all score well.",
            "Children's infrastructure and bad-weather coverage are unusually strong here.",
        ],
        "booking_watch": [
            "High parking and food extras come up often enough to matter on a long stay.",
            "This is strong operationally, but still more hotel-heavy than apartment-heavy.",
        ],
        "tripadvisor_url": "https://www.tripadvisor.com/Hotel_Review-g663535-d7158474-Reviews-Grand_Lubicz_Hotel-Ustka_Pomerania_Province_Northern_Poland.html",
        "tripadvisor_snapshot": "Tripadvisor: 4.5/5 from 1,143 reviews.",
        "tripadvisor_praise": [
            "Tripadvisor positions it as the top-rated hotel in Ustka with standout cleanliness and family infrastructure.",
            "The pool and wellness complex are a major recurring strength.",
        ],
        "tripadvisor_watch": [
            "The town fit is good, but the room-shape fit is still weaker than the top apartment-led shortlist.",
        ],
    },
    "marine-hotel": {
        "maps": maps_search_url("Marine Hotel by Zdrojowa Kołobrzeg"),
        "booking_url": "https://www.booking.com/reviews/pl/hotel/marine.en-gb.html",
        "booking_snapshot": "Booking.com: 9.0/10 from roughly 2,710 reviews.",
        "booking_praise": [
            "Guests love the beach-front location, views, breakfast quality, and generally comfortable rooms.",
            "The review themes support it as a solid classic resort choice in Kołobrzeg.",
        ],
        "booking_watch": [
            "A few messy snippets still point to noise and peak-season crowding issues.",
        ],
        "tripadvisor_url": "https://www.tripadvisor.com/Hotel_Review-g274727-d1852572-Reviews-Marine_Hotel_Ultra_Marine_by_Zdrojowa-Kolobrzeg_Western_Pomerania_Province_Western_Poland.html",
        "tripadvisor_snapshot": "Tripadvisor: large long-running review footprint; themes are more useful than the exact score here.",
        "tripadvisor_praise": [
            "Tripadvisor reviews often like the sea views, spacious rooms, and friendly staff.",
        ],
        "tripadvisor_watch": [
            "Common complaints include an undersized pool/spa for the hotel size, breakfast crowding, and parking cost.",
            "That makes it pleasant, but still not the cleanest family-shape answer.",
        ],
    },
    "hilton-swinoujscie": {
        "maps": maps_search_url("Hilton Swinoujscie Resort And Spa"),
        "booking_url": "https://www.booking.com/reviews/pl/hotel/hilton-swinoujscie-resort-and-spa.html",
        "booking_snapshot": "Booking.com: 8.7/10 from 2,729 reviews.",
        "booking_praise": [
            "Booking highlights the beach location, family-room options, breakfast, and strong general facilities.",
            "There are even multi-room suite categories, which helps if you soften the apartment brief.",
        ],
        "booking_watch": [
            "Value for money is weaker than the headline luxury suggests.",
            "The strong hotel proposition still does not automatically solve your kitchenette preference.",
        ],
        "tripadvisor_url": "https://www.tripadvisor.com/Hotel_Review-g652064-d17886352-Reviews-Hilton_Swinoujscie_Resort_And_Spa-Swinoujscie_Western_Pomerania_Province_Western_Poland.html",
        "tripadvisor_snapshot": "Tripadvisor: direct listing available; guest tone is more mixed than the brand name implies.",
        "tripadvisor_praise": [
            "Tripadvisor guests like the beach location, kids club, aquapark link, and room comfort.",
        ],
        "tripadvisor_watch": [
            "Several reviews complain about service, food consistency, and weak response to on-site issues.",
            "This reinforces the ranking logic: premium, but not a proven apartment-first family base.",
        ],
    },
    "radisson-blu-swinoujscie": {
        "maps": maps_search_url("Radisson Blu Resort Swinoujscie"),
        "booking_url": "https://www.booking.com/reviews/pl/hotel/radisson-blu-resort.en-gb.html",
        "booking_snapshot": "Booking.com: 8.5/10 from 5,838 reviews.",
        "booking_praise": [
            "Booking's own guest summary praises the beach-and-promenade location, views, staff, and breakfast variety.",
            "Families also like the aquapark link and kid activities.",
        ],
        "booking_watch": [
            "The loud, crowded breakfast room and high price/parking burden are recurring negatives.",
        ],
        "tripadvisor_url": "https://www.tripadvisor.com/Hotel_Review-g652064-d12630173-Reviews-Radisson_Blu_Resort_Swinoujscie-Swinoujscie_Western_Pomerania_Province_Western_Poland.html",
        "tripadvisor_snapshot": "Tripadvisor: 4.1/5 from 2,016 reviews.",
        "tripadvisor_praise": [
            "Tripadvisor likes the views, central beach position, and the huge leisure stack.",
        ],
        "tripadvisor_watch": [
            "Crowding, breakfast chaos, and uneven service come up frequently enough to matter.",
            "Like Hilton, it is easier to recommend as a classic resort than as the ideal family apartment base.",
        ],
    },
}


HOTELS_BY_TOWN = {}
for hotel in HOTELS:
    HOTELS_BY_TOWN.setdefault(hotel["town_slug"], []).append(hotel)


SHORTLIST = [hotel for hotel in HOTELS if hotel["rank"] <= 4]

AVAILABILITY_MATRIX = {
    "linea-mare-pobierowo": {
        "family_unit": "Verified",
        "grandparents_room": "Verified",
        "kitchenette": "Likely in apartment categories; confirm exact unit",
    },
    "rosevia-resort-spa": {
        "family_unit": "Verified",
        "grandparents_room": "Verified",
        "kitchenette": "Very likely",
    },
    "saltic-grzybowo": {
        "family_unit": "Verified",
        "grandparents_room": "Verified",
        "kitchenette": "Strongest proof: live `Apartment with Kitchenette` category",
    },
    "saltic-leba": {
        "family_unit": "Verified",
        "grandparents_room": "Verified",
        "kitchenette": "Possible in apartment categories; confirm exact unit",
    },
    "wave-miedzyzdroje": {
        "family_unit": "Strong fit, not fully verified",
        "grandparents_room": "Needs manual confirmation",
        "kitchenette": "Likely, but not verified",
    },
    "apollo-residence": {
        "family_unit": "Looks strong",
        "grandparents_room": "Needs manual confirmation",
        "kitchenette": "Likely",
    },
    "aquarius-spa": {
        "family_unit": "Strong fit, not fully verified",
        "grandparents_room": "Likely",
        "kitchenette": "Unclear in exact apartment spec",
    },
    "shellter-rogowo": {
        "family_unit": "Possible",
        "grandparents_room": "Possible",
        "kitchenette": "Weak evidence",
    },
    "grand-lubicz": {
        "family_unit": "Possible, but hotel-first",
        "grandparents_room": "Likely",
        "kitchenette": "Weak evidence",
    },
    "marine-hotel": {
        "family_unit": "Possible, but hotel-first",
        "grandparents_room": "Likely",
        "kitchenette": "Weak evidence",
    },
    "hilton-swinoujscie": {
        "family_unit": "Possible, but suite-dependent",
        "grandparents_room": "Likely",
        "kitchenette": "Weak evidence",
    },
    "radisson-blu-swinoujscie": {
        "family_unit": "Possible, but hotel-first",
        "grandparents_room": "Likely",
        "kitchenette": "Weak evidence",
    },
}


STYLES = dedent(
    """
    @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@500;600;700&family=Manrope:wght@400;500;600;700;800&display=swap');

    :root {
      --sand: #f7f1e7;
      --foam: #eef5f3;
      --sea: #0d616d;
      --deep: #092f39;
      --lagoon: #3a9aa5;
      --coral: #c87457;
      --sun: #f3d9a5;
      --ink: #1f2d34;
      --muted: #61737b;
      --line: rgba(13, 97, 109, 0.14);
      --panel: rgba(255, 255, 255, 0.88);
      --panel-strong: rgba(255, 255, 255, 0.96);
      --shadow: 0 24px 80px rgba(9, 47, 57, 0.12);
      --radius-xl: 28px;
      --radius-lg: 20px;
      --radius-md: 14px;
    }

    * { box-sizing: border-box; }
    html { scroll-behavior: smooth; }
    body {
      margin: 0;
      font-family: "Manrope", system-ui, sans-serif;
      color: var(--ink);
      background:
        radial-gradient(circle at 15% 0%, rgba(243, 217, 165, 0.45), transparent 32rem),
        radial-gradient(circle at 100% 10%, rgba(58, 154, 165, 0.14), transparent 28rem),
        linear-gradient(180deg, #f7f0e3 0%, #f5f1e8 22%, #edf5f3 60%, #f6f1e5 100%);
      min-height: 100vh;
    }

    body::before {
      content: "";
      position: fixed;
      inset: 0;
      pointer-events: none;
      background:
        linear-gradient(130deg, rgba(255,255,255,0.18), transparent 45%),
        radial-gradient(circle at 80% 0%, rgba(255,255,255,0.28), transparent 18rem);
      z-index: -1;
    }

    a { color: var(--sea); text-decoration: none; }
    a:hover { color: var(--deep); }
    p { margin: 0; }

    .wrapper {
      width: min(1220px, calc(100% - 28px));
      margin: 0 auto;
    }

    .topbar {
      position: sticky;
      top: 0;
      z-index: 30;
      backdrop-filter: blur(18px);
      background: rgba(247, 241, 231, 0.76);
      border-bottom: 1px solid rgba(9, 47, 57, 0.08);
    }

    .topbar-inner {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 1rem;
      padding: 0.9rem 0;
    }

    .brand {
      display: inline-flex;
      align-items: center;
      gap: 0.8rem;
      font-weight: 800;
      letter-spacing: 0.04em;
      text-transform: uppercase;
      color: var(--deep);
      font-size: 0.82rem;
    }

    .brand-mark {
      width: 2.2rem;
      height: 2.2rem;
      border-radius: 50%;
      background: linear-gradient(135deg, var(--sea), var(--lagoon));
      display: inline-flex;
      align-items: center;
      justify-content: center;
      color: #fff;
      font-weight: 800;
      box-shadow: 0 12px 24px rgba(13, 97, 109, 0.18);
    }

    .nav {
      display: flex;
      flex-wrap: wrap;
      gap: 0.7rem;
    }

    .nav a {
      padding: 0.58rem 0.84rem;
      border-radius: 999px;
      background: rgba(255,255,255,0.5);
      border: 1px solid rgba(9, 47, 57, 0.08);
      font-size: 0.84rem;
      color: var(--ink);
    }

    .hero {
      padding: 2.2rem 0 1.3rem;
    }

    .hero-grid {
      display: grid;
      grid-template-columns: 1.15fr 0.85fr;
      gap: 1rem;
      align-items: stretch;
    }

    .hero-copy, .hero-card, .panel, .card, .list-card, .town-card, .hotel-card, .source-card, .quote-card, .method-card, .note-card {
      background: var(--panel);
      border: 1px solid rgba(9, 47, 57, 0.08);
      box-shadow: var(--shadow);
      border-radius: var(--radius-xl);
    }

    .hero-copy {
      position: relative;
      overflow: hidden;
      padding: 1.6rem;
    }

    .hero-copy::after {
      content: "";
      position: absolute;
      right: -4rem;
      bottom: -5rem;
      width: 16rem;
      height: 16rem;
      border-radius: 50%;
      background: radial-gradient(circle, rgba(58,154,165,0.18), transparent 68%);
    }

    .eyebrow {
      display: inline-flex;
      padding: 0.42rem 0.75rem;
      border-radius: 999px;
      background: rgba(13, 97, 109, 0.08);
      color: var(--deep);
      font-weight: 700;
      letter-spacing: 0.03em;
      text-transform: uppercase;
      font-size: 0.68rem;
    }

    h1, h2, h3 {
      font-family: "Cormorant Garamond", Georgia, serif;
      line-height: 0.96;
      letter-spacing: -0.02em;
      margin: 0;
      color: var(--deep);
    }

    h1 { font-size: clamp(2.2rem, 4.9vw, 3.8rem); margin-top: 0.72rem; }
    h2 { font-size: clamp(1.58rem, 3.4vw, 2.2rem); }
    h3 { font-size: clamp(1.18rem, 1.9vw, 1.6rem); }

    .lede, .muted, .body-copy, .card p, li {
      color: var(--muted);
      line-height: 1.58;
      font-size: 0.95rem;
    }

    .lede {
      font-size: 0.95rem;
      max-width: 43rem;
      margin-top: 0.75rem;
    }

    .meta-row, .pill-row {
      display: flex;
      flex-wrap: wrap;
      gap: 0.7rem;
      margin-top: 0.9rem;
    }

    .pill, .signal {
      display: inline-flex;
      align-items: center;
      gap: 0.45rem;
      border-radius: 999px;
      padding: 0.48rem 0.72rem;
      border: 1px solid rgba(9, 47, 57, 0.08);
      background: rgba(255,255,255,0.72);
      font-size: 0.79rem;
      color: var(--ink);
      font-weight: 600;
    }

    .hero-card {
      overflow: hidden;
      display: grid;
      grid-template-rows: 12.5rem auto;
    }

    .hero-image,
    .card-image {
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: block;
    }

    .card-image-link {
      display: block;
      height: 100%;
    }

    .card-image-link:focus-visible {
      outline: 3px solid rgba(13, 97, 109, 0.55);
      outline-offset: 4px;
    }

    .hero-fallback,
    .image-fallback {
      background:
        linear-gradient(160deg, rgba(13,97,109,0.9), rgba(58,154,165,0.7)),
        linear-gradient(20deg, rgba(243,217,165,0.45), transparent 55%);
      position: relative;
      overflow: hidden;
    }

    .hero-fallback::before,
    .image-fallback::before {
      content: "";
      position: absolute;
      inset: auto -10% -35% auto;
      width: 18rem;
      height: 18rem;
      border-radius: 44% 56% 63% 37% / 36% 42% 58% 64%;
      background: rgba(255,255,255,0.15);
    }

    .hero-card-body {
      padding: 0.95rem 1.05rem 1.05rem;
    }

    .section {
      padding: 0.7rem 0 1.7rem;
    }

    .section-header {
      display: flex;
      flex-wrap: wrap;
      gap: 1rem;
      align-items: end;
      justify-content: space-between;
      margin-bottom: 0.95rem;
    }

    .section-note {
      max-width: 36rem;
      color: var(--muted);
      font-size: 0.88rem;
    }

    .grid {
      display: grid;
      gap: 1rem;
    }

    .grid-2 { grid-template-columns: repeat(2, minmax(0, 1fr)); }
    .grid-3 { grid-template-columns: repeat(3, minmax(0, 1fr)); }
    .grid-4 { grid-template-columns: repeat(4, minmax(0, 1fr)); }

    .method-card, .quote-card, .note-card, .panel, .card, .source-card {
      padding: 1rem;
    }

    .method-card strong,
    .note-card strong,
    .source-card strong {
      color: var(--deep);
      display: block;
      margin-bottom: 0.45rem;
      font-size: 1rem;
    }

    .hotel-card, .town-card {
      overflow: hidden;
      display: grid;
      grid-template-rows: 12.25rem auto;
    }

    .hotel-card-body, .town-card-body {
      padding: 0.82rem 0.9rem;
      display: grid;
      gap: 0.52rem;
    }

    .card-topline {
      display: flex;
      flex-wrap: wrap;
      justify-content: space-between;
      gap: 0.55rem;
      align-items: center;
    }

    .rank {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      width: 1.95rem;
      height: 1.95rem;
      border-radius: 50%;
      background: var(--deep);
      color: white;
      font-weight: 800;
      font-size: 0.82rem;
      box-shadow: 0 10px 24px rgba(9, 47, 57, 0.16);
    }

    .signal {
      font-size: 0.69rem;
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }

    .verified { background: rgba(28, 148, 111, 0.12); color: #155f47; border-color: rgba(28, 148, 111, 0.2); }
    .strong { background: rgba(13, 97, 109, 0.09); color: var(--deep); border-color: rgba(13, 97, 109, 0.18); }
    .manual { background: rgba(200, 116, 87, 0.12); color: #8d4c35; border-color: rgba(200, 116, 87, 0.2); }

    .compact-list,
    .source-list,
    .quote-list,
    .linked-list {
      list-style: none;
      margin: 0;
      padding: 0;
      display: grid;
      gap: 0.72rem;
    }

    .compact-list li,
    .linked-list li {
      padding-left: 1rem;
      position: relative;
    }

    .compact-list li::before,
    .linked-list li::before {
      content: "";
      position: absolute;
      left: 0;
      top: 0.8rem;
      width: 0.42rem;
      height: 0.42rem;
      border-radius: 50%;
      background: var(--coral);
    }

    .source-list li {
      display: flex;
      justify-content: space-between;
      gap: 1rem;
      padding: 0.68rem 0;
      border-bottom: 1px solid var(--line);
    }

    .source-list li:last-child { border-bottom: 0; }

    .source-label {
      color: var(--ink);
      font-weight: 700;
    }

    .matrix {
      width: 100%;
      border-collapse: collapse;
      overflow: hidden;
      border-radius: 20px;
      background: rgba(255,255,255,0.9);
      box-shadow: var(--shadow);
      border: 1px solid rgba(9, 47, 57, 0.08);
    }

    .matrix th,
    .matrix td {
      padding: 0.95rem 1rem;
      text-align: left;
      vertical-align: top;
      border-bottom: 1px solid var(--line);
      font-size: 0.95rem;
      line-height: 1.55;
    }

    .matrix th {
      color: var(--deep);
      font-size: 0.78rem;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      background: rgba(13, 97, 109, 0.06);
    }

    .matrix tr:last-child td {
      border-bottom: 0;
    }

    .panel {
      padding: 1rem;
    }

    .panel-grid {
      display: grid;
      grid-template-columns: 1.05fr 0.95fr;
      gap: 1rem;
    }

    .quote-card {
      background: linear-gradient(180deg, rgba(255,255,255,0.95), rgba(255,255,255,0.88));
    }

    .quote {
      margin: 0;
      padding: 1rem 1rem 1rem 1.2rem;
      border-left: 3px solid rgba(13, 97, 109, 0.22);
      background: rgba(13, 97, 109, 0.04);
      border-radius: 0 16px 16px 0;
      color: var(--ink);
      font-size: 0.96rem;
      line-height: 1.65;
    }

    .hero-actions {
      display: flex;
      flex-wrap: wrap;
      gap: 0.65rem;
      margin-top: 1rem;
    }

    .button {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 0.5rem;
      padding: 0.72rem 0.95rem;
      border-radius: 999px;
      font-weight: 700;
      background: var(--deep);
      color: white;
      box-shadow: 0 18px 36px rgba(9, 47, 57, 0.18);
    }

    .button.small {
      padding: 0.54rem 0.76rem;
      font-size: 0.8rem;
      box-shadow: none;
    }

    .button.secondary {
      background: rgba(255,255,255,0.74);
      color: var(--deep);
      border: 1px solid rgba(9, 47, 57, 0.09);
      box-shadow: none;
    }

    .page-hero {
      padding: 2.8rem 0 1.5rem;
    }

    .page-shell {
      display: grid;
      gap: 1rem;
    }

    .page-grid {
      display: grid;
      grid-template-columns: 1.05fr 0.95fr;
      gap: 1rem;
      align-items: start;
    }

    .sticky {
      position: sticky;
      top: 5.6rem;
    }

    .back-link {
      display: inline-flex;
      align-items: center;
      gap: 0.45rem;
      font-weight: 700;
      color: var(--deep);
      margin-bottom: 1rem;
    }

    .stat-band {
      display: grid;
      grid-template-columns: repeat(3, minmax(0, 1fr));
      gap: 0.65rem;
      margin-top: 1rem;
    }

    .stat {
      padding: 0.75rem 0.85rem;
      border-radius: 18px;
      background: rgba(255,255,255,0.72);
      border: 1px solid rgba(9, 47, 57, 0.08);
    }

    .stat span {
      display: block;
      color: var(--muted);
      font-size: 0.78rem;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      margin-bottom: 0.35rem;
    }

    .stat strong {
      color: var(--deep);
      font-size: 0.98rem;
    }

    .footer {
      padding: 0.6rem 0 3rem;
      color: var(--muted);
      font-size: 0.92rem;
    }

    .link-chips {
      display: flex;
      flex-wrap: wrap;
      gap: 0.55rem;
      margin-top: 0.9rem;
    }

    .chip-link {
      display: inline-flex;
      align-items: center;
      padding: 0.46rem 0.72rem;
      border-radius: 999px;
      border: 1px solid rgba(9, 47, 57, 0.08);
      background: rgba(255,255,255,0.72);
      color: var(--deep);
      font-size: 0.84rem;
      font-weight: 700;
    }

    .dense-copy {
      font-size: 0.9rem;
      line-height: 1.48;
      color: var(--muted);
    }

    .ranking-links a {
      display: inline-block;
      margin-right: 0.5rem;
      white-space: nowrap;
    }

    .review-grid,
    .gallery {
      display: grid;
      gap: 0.9rem;
    }

    .review-grid {
      grid-template-columns: repeat(2, minmax(0, 1fr));
      margin-top: 1rem;
    }

    .gallery {
      grid-template-columns: repeat(2, minmax(0, 1fr));
    }

    .review-card,
    .gallery-card {
      background: rgba(255,255,255,0.8);
      border: 1px solid rgba(9, 47, 57, 0.08);
      border-radius: var(--radius-lg);
      overflow: hidden;
    }

    .review-card {
      padding: 1rem;
    }

    .gallery-card img {
      display: block;
      width: 100%;
      height: 11.5rem;
      object-fit: cover;
    }

    .gallery-meta {
      padding: 0.8rem 0.9rem 0.9rem;
      display: grid;
      gap: 0.32rem;
    }

    .gallery-meta strong {
      color: var(--deep);
      font-size: 0.95rem;
    }

    .stack {
      display: grid;
      gap: 1rem;
    }

    @media (max-width: 980px) {
      .hero-grid,
      .page-grid,
      .panel-grid,
      .grid-4,
      .grid-3,
      .review-grid,
      .gallery {
        grid-template-columns: 1fr;
      }

      .grid-2 {
        grid-template-columns: 1fr;
      }

      .sticky {
        position: static;
      }

      .stat-band {
        grid-template-columns: 1fr;
      }

      .matrix,
      .matrix thead,
      .matrix tbody,
      .matrix th,
      .matrix td,
      .matrix tr {
        display: block;
      }

      .matrix thead {
        display: none;
      }

      .matrix tr {
        border-bottom: 1px solid var(--line);
      }

      .matrix td {
        border-bottom: 0;
        padding-top: 0.35rem;
        padding-bottom: 0.35rem;
      }

      .matrix td::before {
        content: attr(data-label);
        display: block;
        color: var(--deep);
        font-size: 0.73rem;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        margin-bottom: 0.18rem;
        font-weight: 700;
      }
    }

    @media (max-width: 720px) {
      .topbar-inner {
        align-items: flex-start;
        flex-direction: column;
      }

      .hero,
      .page-hero {
        padding-top: 2rem;
      }

      .hero-copy,
      .hero-card-body,
      .panel,
      .method-card,
      .quote-card,
      .source-card {
        padding: 1.1rem;
      }

      h1 {
        font-size: clamp(2.15rem, 14vw, 3.25rem);
      }
    }
    """
).strip()


def ensure_dirs() -> None:
    (SITE / "assets").mkdir(parents=True, exist_ok=True)
    (SITE / "hotels").mkdir(parents=True, exist_ok=True)
    (SITE / "towns").mkdir(parents=True, exist_ok=True)


def render_image(
    url: str,
    alt: str,
    fallback_label: str,
    klass: str = "card-image",
    href: str | None = None,
) -> str:
    if url:
        image_html = f'<img class="{klass}" src="{escape(url)}" alt="{escape(alt)}" loading="lazy">'
    else:
        image_html = (
            '<div class="image-fallback">'
            '<div style="padding:1.3rem;color:white;font-weight:800;letter-spacing:0.05em;text-transform:uppercase;">'
            f"{escape(fallback_label)}"
            "</div>"
            "</div>"
        )
    if href:
        return f'<a class="card-image-link" href="{escape(href)}" aria-label="{escape(alt)}">{image_html}</a>'
    return image_html


def render_sources(items: list[tuple[str, str]]) -> str:
    body = []
    for label, url in items:
        body.append(
            "<li>"
            f'<span class="source-label">{escape(label)}</span>'
            f'<a href="{escape(url)}" target="_blank" rel="noreferrer">open source</a>'
            "</li>"
        )
    return '<ul class="source-list">' + "".join(body) + "</ul>"


def render_link_chips(items: list[tuple[str, str]]) -> str:
    return (
        '<div class="link-chips">'
        + "".join(
            f'<a class="chip-link" href="{escape(url)}" target="_blank" rel="noreferrer">{escape(label)}</a>'
            for label, url in items
        )
        + "</div>"
    )


def render_gallery(items: list[tuple[str, str, str, str]]) -> str:
    cards = []
    for url, alt, credit, source in items:
        cards.append(
            '<article class="gallery-card">'
            f'<img src="{escape(url)}" alt="{escape(alt)}" loading="lazy">'
            '<div class="gallery-meta">'
            f"<strong>{escape(alt)}</strong>"
            f'<span class="dense-copy">{escape(credit)}</span>'
            f'<a href="{escape(source)}" target="_blank" rel="noreferrer">open image source</a>'
            "</div>"
            "</article>"
        )
    return '<div class="gallery">' + "".join(cards) + "</div>"


def render_points(items: list[str], klass: str = "compact-list") -> str:
    return f'<ul class="{klass}">' + "".join(f"<li>{escape(item)}</li>" for item in items) + "</ul>"


def hotel_link(hotel: dict, depth: int = 0) -> str:
    prefix = "../" * depth
    return f"{prefix}hotels/{hotel['slug']}.html"


def town_link(town: dict, depth: int = 0) -> str:
    prefix = "../" * depth
    return f"{prefix}towns/{town['slug']}.html"


def layout(title: str, body: str, depth: int = 0) -> str:
    prefix = "../" * depth
    return dedent(
        f"""
        <!doctype html>
        <html lang="en">
        <head>
          <meta charset="utf-8">
          <meta name="viewport" content="width=device-width, initial-scale=1">
          <title>{escape(title)}</title>
          <meta name="description" content="Polish coast vacation study for a family with two children and grandparents.">
          <link rel="stylesheet" href="{prefix}assets/styles.css">
        </head>
        <body>
          <header class="topbar">
            <div class="wrapper topbar-inner">
              <a class="brand" href="{prefix}index.html">
                <span class="brand-mark">PL</span>
                <span>Polish Sea Family Study</span>
              </a>
              <nav class="nav">
                <a href="{prefix}index.html#shortlist">Top Picks</a>
                <a href="{prefix}index.html#ranking">Full Ranking</a>
                <a href="{prefix}index.html#towns">Towns</a>
                <a href="{prefix}index.html#matrix">Fit Matrix</a>
              </nav>
            </div>
          </header>
          {body}
          <footer class="footer">
            <div class="wrapper">
              Built from a live research snapshot taken on {RESEARCH_DATE}. Availability can change after that date.
            </div>
          </footer>
        </body>
        </html>
        """
    ).strip()


def build_index() -> None:
    shortlist_cards = []
    for hotel in SHORTLIST:
        hotel_page = hotel_link(hotel)
        town_page = town_link(next(t for t in TOWNS if t["slug"] == hotel["town_slug"]))
        shortlist_cards.append(
            f"""
            <article class="hotel-card">
              {render_image(hotel["image"], hotel["name"], hotel["name"], href=hotel_page)}
              <div class="hotel-card-body">
                <div class="card-topline">
                  <span class="rank">{hotel["rank"]}</span>
                  <span class="signal {hotel["signal_class"]}">{escape(hotel["signal"])}</span>
                </div>
                <div>
                  <h3>{escape(hotel["name"])}</h3>
                  <p class="muted" style="margin-top:0.35rem;">{escape(hotel["town"])}</p>
                </div>
                <p>{escape(hotel["headline"])}</p>
                <div class="hero-actions" style="margin-top:0;">
                  <a class="button secondary small" href="{hotel_page}">Open hotel page</a>
                  <a class="button secondary small" href="{town_page}">Open town page</a>
                </div>
              </div>
            </article>
            """
        )

    ranking_cards = []
    for hotel in HOTELS:
        row = AVAILABILITY_MATRIX[hotel["slug"]]
        hotel_page = hotel_link(hotel)
        ranking_cards.append(
            f"""
            <article class="hotel-card">
              {render_image(hotel["image"], hotel["name"], hotel["name"], href=hotel_page)}
              <div class="hotel-card-body">
                <div class="card-topline">
                  <span class="rank">{hotel["rank"]}</span>
                  <span class="signal {hotel["signal_class"]}">{escape(hotel["signal"])}</span>
                </div>
                <div>
                  <h3>{escape(hotel["name"])}</h3>
                  <p class="muted" style="margin-top:0.35rem;">{escape(hotel["town"])}</p>
                </div>
                <p class="dense-copy">{escape(row["family_unit"])} family fit. {escape(row["grandparents_room"])} grandparents room. {escape(row["kitchenette"])}</p>
                <div class="hero-actions" style="margin-top:0;">
                  <a class="button secondary small" href="{hotel_page}">Hotel report</a>
                </div>
              </div>
            </article>
            """
        )

    matrix_rows = []
    for hotel in HOTELS:
        row = AVAILABILITY_MATRIX[hotel["slug"]]
        matrix_rows.append(
            "<tr>"
            f'<td data-label="Rank"><strong>#{hotel["rank"]} {escape(hotel["name"])}</strong><br><span class="muted">{escape(hotel["town"])}</span></td>'
            f'<td data-label="Family unit">{escape(row["family_unit"])}</td>'
            f'<td data-label="Grandparents room">{escape(row["grandparents_room"])}</td>'
            f'<td data-label="Kitchenette confidence">{escape(row["kitchenette"])}</td>'
            "</tr>"
        )

    town_cards = []
    for town in TOWNS:
        linked_hotels = HOTELS_BY_TOWN.get(town["slug"], [])
        hotel_labels = ", ".join(hotel["name"] for hotel in linked_hotels) if linked_hotels else "No matching hotel in the source notes"
        town_page = town_link(town)
        town_cards.append(
            f"""
            <article class="town-card">
              {render_image(town["image"], town["name"], town["name"], href=town_page)}
              <div class="town-card-body">
                <div>
                  <h3>{escape(town["name"])}</h3>
                  <p class="muted" style="margin-top:0.5rem;">{escape(town["headline"])}</p>
                </div>
                <p>{escape(hotel_labels)}</p>
                <a class="button secondary small" href="{town_page}">Town page</a>
              </div>
            </article>
            """
        )

    hero_ranked_links = " ".join(
        [
            f'<a href="{hotel_link(HOTELS[0])}">1. Linea Mare</a>',
            f'<a href="{hotel_link(HOTELS[1])}">2. Rosevia</a>',
            f'<a href="{hotel_link(HOTELS[2])}">3. Saltic Grzybowo</a>',
            f'<a href="{hotel_link(HOTELS[3])}">4. Saltic Łeba</a>',
            f'<a href="{hotel_link(HOTELS[4])}">5. Wave Międzyzdroje</a>',
        ]
    )

    html = f"""
    <main>
      <section class="hero">
        <div class="wrapper hero-grid">
          <div class="hero-copy">
            <span class="eyebrow">Family Vacation Study</span>
            <h1>Best Polish Coast Fits</h1>
            <p class="lede">
              Filtered for one room shape: parents and kids in an apartment-style unit, grandparents in a separate room,
              ideally in the same resort, with kitchenette evidence where possible.
            </p>
            <div class="meta-row">
              <span class="pill">{escape(RESEARCH_DATE)} research snapshot</span>
              <span class="pill">{escape(STAY_WINDOW)} sample stay</span>
              <span class="pill">{escape(str(STAY_NIGHTS))} nights tested where possible</span>
            </div>
            <div class="hero-actions">
              <a class="button" href="#shortlist">Top picks</a>
              <a class="button secondary" href="#matrix">Fit matrix</a>
              <a class="button secondary" href="#towns">Town pages</a>
            </div>
          </div>
          <div class="hero-card">
            {render_image("https://r.profitroom.pl/lineamarepobierowo/images/202306201532590.zdj_cie_startowe.jpg", "Polish coast resort view", "Polish Coast", "hero-image")}
            <div class="hero-card-body">
              <span class="eyebrow">Bottom line</span>
              <h3 style="margin-top:0.65rem;">Current best-fit order</h3>
              <p class="dense-copy ranking-links" style="margin-top:0.75rem;">
                {hero_ranked_links}
              </p>
            </div>
          </div>
        </div>
      </section>

      <section class="section" id="shortlist">
        <div class="wrapper">
          <div class="section-header">
            <div>
              <span class="eyebrow">Shortlist</span>
              <h2>Best Bets Right Now</h2>
            </div>
            <p class="section-note">These are the strongest first calls.</p>
          </div>
          <div class="grid grid-2">
            {"".join(shortlist_cards)}
          </div>
        </div>
      </section>

      <section class="section" id="ranking">
        <div class="wrapper">
          <div class="section-header">
            <div>
              <span class="eyebrow">Ranking</span>
              <h2>Full Hotel Ranking</h2>
            </div>
            <p class="section-note">Ordered by fit, not prestige.</p>
          </div>
          <div class="grid grid-3">
            {"".join(ranking_cards)}
          </div>
        </div>
      </section>

      <section class="section" id="matrix">
        <div class="wrapper">
          <div class="section-header">
            <div>
              <span class="eyebrow">Comparison</span>
              <h2>Quick-Glance Fit Matrix</h2>
            </div>
            <p class="section-note">Fastest read before opening the full reports.</p>
          </div>
          <table class="matrix">
            <thead>
              <tr>
                <th>Hotel</th>
                <th>Parents + kids unit</th>
                <th>Grandparents room</th>
                <th>Kitchenette confidence</th>
              </tr>
            </thead>
            <tbody>
              {"".join(matrix_rows)}
            </tbody>
          </table>
        </div>
      </section>

      <section class="section" id="towns">
        <div class="wrapper">
          <div class="section-header">
            <div>
              <span class="eyebrow">Destinations</span>
              <h2>Town Pages</h2>
            </div>
            <p class="section-note">Now with town photos, map links, and quick pins.</p>
          </div>
          <div class="grid grid-3">
            {"".join(town_cards)}
          </div>
        </div>
      </section>

      <section class="section">
        <div class="wrapper panel-grid">
          <article class="quote-card">
            <span class="eyebrow">Source Notes</span>
            <h2 style="margin-top:0.8rem;">Original Hotel Notes</h2>
            <div class="quote-list" style="margin-top:1rem;">
              {"".join(f'<blockquote class="quote">{escape(quote)}</blockquote>' for quote in WHATSAPP_QUOTES)}
            </div>
          </article>
          <article class="quote-card">
            <span class="eyebrow">Interpretation</span>
            <h2 style="margin-top:0.8rem;">Normalization Notes</h2>
            {render_points(INTERPRETATION_NOTES)}
          </article>
        </div>
      </section>

      <section class="section">
        <div class="wrapper">
          <div class="grid grid-3">
            <article class="note-card">
              <strong>Safest booking leads</strong>
              <p>Linea Mare, Rosevia, Saltic Grzybowo, and Saltic Łeba are the strongest first calls because I verified them directly against live inventory.</p>
            </article>
            <article class="note-card">
              <strong>Best premium upside</strong>
              <p>Wave Międzyzdroje looks like it could be excellent if availability and apartment details check out, but it is not as strongly proven as the top four.</p>
            </article>
            <article class="note-card">
              <strong>Main caveat</strong>
              <p>Every availability statement here is a snapshot from {escape(RESEARCH_DATE)}. Even very good options can tighten quickly for July.</p>
            </article>
          </div>
        </div>
      </section>
    </main>
    """
    (SITE / "index.html").write_text(layout("Polish Sea Family Study", html), encoding="utf-8")


def build_hotel_pages() -> None:
    for hotel in HOTELS:
        town = next(t for t in TOWNS if t["slug"] == hotel["town_slug"])
        external = HOTEL_EXTERNALS[hotel["slug"]]
        quick_links = [
            ("Official site", hotel["sources"][0][1]),
            ("Google Maps", external["maps"]),
            ("Booking.com", external["booking_url"]),
            ("Tripadvisor", external["tripadvisor_url"]),
        ]
        evidence_links = hotel["sources"] + [
            ("Google Maps", external["maps"]),
            ("Booking.com reviews / listing", external["booking_url"]),
            ("Tripadvisor listing", external["tripadvisor_url"]),
        ]
        body = f"""
        <main class="page-hero">
          <div class="wrapper page-shell">
            <a class="back-link" href="../index.html#ranking">Back to ranking</a>
            <div class="page-grid">
              <section class="hero-copy">
                <span class="eyebrow">Hotel Report</span>
                <h1>{escape(hotel["name"])}</h1>
                <p class="lede">{escape(hotel["headline"])}</p>
                <div class="pill-row">
                  <span class="signal {hotel["signal_class"]}">{escape(hotel["signal"])}</span>
                  <span class="pill">Rank #{hotel["rank"]}</span>
                  <span class="pill">{escape(hotel["town"])}</span>
                </div>
                <div class="stat-band">
                  <div class="stat"><span>Research snapshot</span><strong>{escape(RESEARCH_DATE)}</strong></div>
                  <div class="stat"><span>Window checked</span><strong>{escape(STAY_WINDOW)}</strong></div>
                  <div class="stat"><span>Priority filter</span><strong>Apartment + separate grandparents room</strong></div>
                </div>
                {render_link_chips(quick_links)}
              </section>
              <aside class="hero-card sticky">
                {render_image(hotel["image"], hotel["name"], hotel["name"], "hero-image")}
                <div class="hero-card-body">
                  <span class="eyebrow">Town</span>
                  <h3 style="margin-top:0.8rem;">{escape(town["name"])}</h3>
                  <p class="muted" style="margin-top:0.7rem;">{escape(town["headline"])}</p>
                  <div class="hero-actions" style="margin-top:1rem;">
                    <a class="button secondary small" href="../towns/{town["slug"]}.html">Open town page</a>
                  </div>
                </div>
              </aside>
            </div>

            <div class="page-grid">
              <article class="panel">
                <span class="eyebrow">Verdict</span>
                <h2 style="margin-top:0.8rem;">Why It Lands Here</h2>
                <p class="body-copy" style="margin-top:0.9rem;">{escape(hotel["summary"])}</p>
                <div class="grid grid-2" style="margin-top:1.2rem;">
                  <div class="source-card">
                    <strong>Why it works</strong>
                    {render_points(hotel["why_it_works"])}
                  </div>
                  <div class="source-card">
                    <strong>Family-fit notes</strong>
                    {render_points(hotel["family_fit"])}
                  </div>
                </div>
              </article>
              <article class="panel">
                <span class="eyebrow">Availability</span>
                <h2 style="margin-top:0.8rem;">What Was Actually Verified</h2>
                {render_points(hotel["availability"])}
                <div class="source-card" style="margin-top:1rem;">
                  <strong>Watch-outs</strong>
                  {render_points(hotel["watchouts"])}
                </div>
              </article>
            </div>

            <article class="panel">
              <span class="eyebrow">Reviews</span>
              <h2 style="margin-top:0.8rem;">What Booking + Tripadvisor Guests Say</h2>
              <div class="review-grid">
                <article class="review-card">
                  <strong>Booking.com snapshot</strong>
                  <p class="dense-copy">{escape(external["booking_snapshot"])}</p>
                  <p class="dense-copy" style="margin-top:0.75rem;"><strong style="color:var(--deep);">Guests praise</strong></p>
                  {render_points(external["booking_praise"])}
                  <p class="dense-copy" style="margin-top:0.75rem;"><strong style="color:var(--deep);">Common complaints</strong></p>
                  {render_points(external["booking_watch"])}
                </article>
                <article class="review-card">
                  <strong>Tripadvisor snapshot</strong>
                  <p class="dense-copy">{escape(external["tripadvisor_snapshot"])}</p>
                  <p class="dense-copy" style="margin-top:0.75rem;"><strong style="color:var(--deep);">Guests praise</strong></p>
                  {render_points(external["tripadvisor_praise"])}
                  <p class="dense-copy" style="margin-top:0.75rem;"><strong style="color:var(--deep);">Common complaints</strong></p>
                  {render_points(external["tripadvisor_watch"])}
                </article>
              </div>
            </article>

            <div class="page-grid">
              <article class="panel">
                <span class="eyebrow">Sources</span>
                <h2 style="margin-top:0.8rem;">Linked Evidence</h2>
                {render_sources(evidence_links)}
              </article>
              <article class="panel">
                <span class="eyebrow">Context</span>
                <h2 style="margin-top:0.8rem;">Town Fit</h2>
                <p>{escape(town["summary"])}</p>
                <div class="hero-actions" style="margin-top:1rem;">
                  <a class="button secondary small" href="../index.html#shortlist">Back to shortlist</a>
                  <a class="button secondary small" href="../index.html#towns">Back to towns</a>
                </div>
              </article>
            </div>
          </div>
        </main>
        """
        (SITE / "hotels" / f"{hotel['slug']}.html").write_text(
            layout(f"{hotel['name']} - Hotel Report", body, depth=1),
            encoding="utf-8",
        )


def build_town_pages() -> None:
    for town in TOWNS:
        hotels = HOTELS_BY_TOWN.get(town["slug"], [])
        detail = TOWN_DETAILS[town["slug"]]
        town_map = maps_search_url(f"{town['name']} Poland")
        quick_links = [("Google Maps", town_map)] + town["source_links"]
        hotel_cards = []
        for hotel in hotels:
            hotel_cards.append(
                f"""
                <article class="source-card">
                  <strong>#{hotel["rank"]} {escape(hotel["name"])}</strong>
                  <p class="dense-copy">{escape(hotel["headline"])}</p>
                  <a href="../hotels/{hotel["slug"]}.html">Open hotel report</a>
                </article>
                """
            )
        if not hotel_cards:
            hotel_cards.append(
                """
                <article class="source-card">
                  <strong>No matching hotel in the source notes</strong>
                  <p>This town remains interesting, but it would need a fresh hotel search to become a booking-ready option.</p>
                </article>
                """
            )

        body = f"""
        <main class="page-hero">
          <div class="wrapper page-shell">
            <a class="back-link" href="../index.html#towns">Back to town index</a>
            <div class="page-grid">
              <section class="hero-copy">
                <span class="eyebrow">Town Report</span>
                <h1>{escape(town["name"])}</h1>
                <p class="lede">{escape(town["headline"])}</p>
                <p class="body-copy" style="margin-top:0.9rem;">{escape(town["summary"])}</p>
                <div class="pill-row">
                  <span class="pill">{escape(RESEARCH_DATE)} snapshot</span>
                  <span class="pill">{escape(str(len(hotels)))} hotel option(s) tied to this town</span>
                </div>
                {render_link_chips(quick_links)}
              </section>
              <aside class="hero-card sticky">
                {render_image(town["image"], town["name"], town["name"], "hero-image")}
                <div class="hero-card-body">
                  <span class="eyebrow">Quick take</span>
                  <h3 style="margin-top:0.8rem;">Town fit for this trip</h3>
                  <p class="dense-copy" style="margin-top:0.75rem;">This page focuses on beach logistics, family rhythm, and what nearby map pins actually help with kids and grandparents.</p>
                </div>
              </aside>
            </div>

            <div class="page-grid">
              <article class="panel">
                <span class="eyebrow">Strengths</span>
                <h2 style="margin-top:0.8rem;">Why This Town Works</h2>
                {render_points(town["best_for"])}
              </article>
              <article class="panel">
                <span class="eyebrow">Cautions</span>
                <h2 style="margin-top:0.8rem;">What to Watch</h2>
                {render_points(town["watchouts"])}
              </article>
            </div>

            <div class="page-grid">
              <article class="panel">
                <span class="eyebrow">Town Photos</span>
                <h2 style="margin-top:0.8rem;">Street-and-Beach Read</h2>
                {render_gallery(detail["gallery"])}
              </article>
              <article class="panel">
                <span class="eyebrow">Google Maps</span>
                <h2 style="margin-top:0.8rem;">Useful Family Pins</h2>
                {render_sources(detail["family_spots"])}
              </article>
            </div>

            <div class="page-grid">
              <article class="panel">
                <span class="eyebrow">Hotels</span>
                <h2 style="margin-top:0.8rem;">Properties Linked to This Town</h2>
                <div class="grid">
                  {"".join(hotel_cards)}
                </div>
              </article>
              <article class="panel">
                <span class="eyebrow">Sources</span>
                <h2 style="margin-top:0.8rem;">Reference Links</h2>
                {render_sources([("Google Maps", town_map)] + town["source_links"])}
              </article>
            </div>
          </div>
        </main>
        """
        (SITE / "towns" / f"{town['slug']}.html").write_text(
            layout(f"{town['name']} - Town Report", body, depth=1),
            encoding="utf-8",
        )


def main() -> None:
    ensure_dirs()
    (SITE / "assets" / "styles.css").write_text(STYLES + "\n", encoding="utf-8")
    build_index()
    build_hotel_pages()
    build_town_pages()


if __name__ == "__main__":
    main()
