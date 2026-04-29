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


def booking_search_url(query: str) -> str:
    return f"https://www.booking.com/searchresults.html?ss={quote(query)}"


def tripadvisor_search_url(query: str) -> str:
    return f"https://www.tripadvisor.com/Search?q={quote(query)}"

RESEARCH_DATE = "April 20, 2026"
STAY_WINDOW = "June 28, 2026 to July 25, 2026"
STAY_NIGHTS = 27
FLYOUT_WINDOW = "June 27, 2026 to July 11, 2026"
FLYOUT_NIGHTS = 14
FAMILY_MODEL = (
    "Family inventory was checked as 2 adults plus two children using common booking-engine age "
    "bands that best match ages 3 and 6."
)
GRANDPARENTS_MODEL = "Grandparents were checked as a separate room for 2 adults."
OUTBOUND_MODEL = (
    "Fly-out options were judged from Aachen, Germany with the working assumption of rail access to Frankfurt Airport, "
    "a two-hour airport buffer, and a bias against flights that force a pre-5am wake-up."
)


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
    "This pass expands Świnoujście with the Baltic Park apartment ecosystem: Molo, Fort, and Loft.",
    "Sopot was added as a new town, but the strongest apartment-style family option there sits on the Gdańsk / Jelitkowo edge rather than on the pier itself.",
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
            "This is still the cleanest all-around fit in the study. The resort openly positions itself as a "
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
            "Rosevia remains the strongest true-resort apartment concept in the set. The official site describes "
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
            "Grzybowo still gives you one of the best practical answers in the whole study. The biggest "
            "advantage is that the live inventory explicitly included a `Premium Apartment with Kitchenette`, which "
            "maps neatly to your parents-plus-kids setup while keeping Kołobrzeg close by."
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
        "slug": "baltic-park-molo",
        "name": "Baltic Park Molo Apartments by Zdrojowa",
        "town": "Świnoujście",
        "town_slug": "swinoujscie",
        "image": "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/0c/de/26/f5/baltic-park-molo-apartments.jpg?w=1600&h=1000&s=1",
        "image_credit": "Tripadvisor property photo",
        "signal": "Beachfront apartment ecosystem with aquapark access",
        "signal_class": "strong",
        "headline": "Most promising new direct-beach apartment option in Świnoujście.",
        "summary": (
            "This is the most important addition in the new pass. Baltic Park Molo sits in the same high-energy "
            "Baltic Park resort zone as Hilton and Radisson, but the product shape is much better for your trip: suites, "
            "kitchenettes, promenade access, beach access, restaurants, and aquapark convenience in one compact ecosystem."
        ),
        "why_it_works": [
            "Official description explicitly says the suites have fully equipped kitchenettes.",
            "The location solves kid logistics unusually well: beach, promenade, food, and aquapark are all close together.",
            "Review evidence repeatedly mentions breakfast in the Hilton and easy access to the broader complex infrastructure.",
        ],
        "family_fit": [
            "This is one of the easiest 'parents in an apartment, grandparents nearby in the same ecosystem' ideas in the whole study.",
            "It looks stronger as a real-life family base than the classic hotel rooms at Hilton or Radisson next door.",
        ],
        "availability": [
            "Tripadvisor metasearch returned live pricing for the sample stay window and surfaced Booking.com as an active offer source.",
            "I did not verify the exact parents-plus-kids apartment and separate grandparents room end to end inside the official booking engine.",
            f"Research snapshot date: {RESEARCH_DATE}. Window checked: {STAY_WINDOW} ({STAY_NIGHTS} nights).",
        ],
        "watchouts": [
            "Parking fees, late-arrival communication, and some noise/ventilation complaints come up often enough to matter.",
            "The ecosystem is easy, but exact check-in and breakfast logistics should be confirmed before paying.",
        ],
        "sources": [
            ("Official apartment page", "https://zdrojowahotels.pl/en/baltic-park-molo"),
            ("Booking.com search / listing", booking_search_url("Baltic Park Molo Apartments by Zdrojowa Świnoujście")),
        ],
    },
    {
        "rank": 5,
        "slug": "golden-tulip-miedzyzdroje",
        "name": "Golden Tulip Międzyzdroje Residence",
        "town": "Międzyzdroje",
        "town_slug": "miedzyzdroje",
        "image": "https://media.iceportal.com/25592/photos/76919991_L.jpg",
        "image_credit": "Official site / IcePortal image",
        "signal": "Beach-apartment residence with very strong family review signal",
        "signal_class": "strong",
        "headline": "Best added Międzyzdroje option if you want a proven apartment residence near the beach.",
        "summary": (
            "Golden Tulip Międzyzdroje is exactly the kind of hotel-connected apartment residence that belongs in this study. "
            "Tripadvisor descriptions and guest reviews point to large units, kitchenettes, a short beach walk, pool access, and "
            "a much calmer family rhythm than the flashier premium towers."
        ),
        "why_it_works": [
            "Tripadvisor describes the rooms as apartments with refrigerators and kitchenettes.",
            "Family reviews repeatedly praise spacious layouts, breakfast, and the beach being very close.",
            "This gives Międzyzdroje a second serious product shape beyond the premium Wave option.",
        ],
        "family_fit": [
            "Very strong if you want an easier, more practical family apartment stay instead of a luxury-first stay.",
            "This may be the safer Międzyzdroje family base if Wave availability or pricing gets uncomfortable.",
        ],
        "availability": [
            "Tripadvisor metasearch returned live pricing for the sample stay, which is a meaningful positive signal for late June through July.",
            "I did not verify the exact two-booking combination for parents-plus-kids and grandparents separately in the official engine.",
            f"Research snapshot date: {RESEARCH_DATE}. Window checked: {STAY_WINDOW} ({STAY_NIGHTS} nights).",
        ],
        "watchouts": [
            "The residence sits on the quieter edge of town, which is either a plus or a minus depending on how much promenade life you want.",
            "Wellness scale looks smaller than at Wave, and Wi‑Fi appears weaker than the room product deserves.",
        ],
        "sources": [
            ("Official residence site", "https://miedzyzdroje.goldentulip.com/en-us/"),
            ("Booking.com reviews", "https://www.booking.com/reviews/pl/hotel/golden-tulip-miedzyzdroje-residence.en-gb.html"),
        ],
    },
    {
        "rank": 6,
        "slug": "saltic-leba",
        "name": "Saltic Resort & Spa Łeba",
        "town": "Łeba",
        "town_slug": "leba",
        "image": "https://r.profitroom.pl/salticresortspaleba/images/202309151849420.Hotel_Saltic_Leba_020.jpg",
        "image_credit": "Official resort image",
        "signal": "Verified directly in the live booking engine",
        "signal_class": "verified",
        "headline": "A strong functional pick in one of the most family-friendly towns on the coast.",
        "summary": (
            "Łeba is still one of the strongest towns in the whole note set, and the Saltic booking engine did return "
            "real long-stay availability for family and adult-only configurations. It slips slightly only because the new "
            "Świnoujście and Międzyzdroje apartment ecosystems fit the brief even more directly."
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
        "rank": 7,
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
            "Wave still deserves to stay high because the product shape is extremely attractive: large apartments, direct beach feel, "
            "real kids infrastructure, spa, and a proper premium-resort mood. It falls behind the more grounded apartment ecosystems only "
            "because the hard July inventory proof remains softer."
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
        "rank": 8,
        "slug": "baltic-park-fort",
        "name": "Baltic Park Fort by Zdrojowa",
        "town": "Świnoujście",
        "town_slug": "swinoujscie",
        "image": "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/18/b0/63/fd/baltic-park-fort-by-zdrojowa.jpg?w=1600&h=1000&s=1",
        "image_credit": "Tripadvisor property photo",
        "signal": "Same beachfront ecosystem, but slightly less friction-free than Molo",
        "signal_class": "strong",
        "headline": "Very viable Świnoujście backup if Molo is tight or priced out.",
        "summary": (
            "Baltic Park Fort belongs in the same promising cluster as Molo. The review evidence points to a strong location, "
            "big apartments, kitchen-and-balcony practicality, breakfast access in the Hilton, and one-hour aquapark access. "
            "It ranks below Molo because the operational friction looks higher."
        ),
        "why_it_works": [
            "Beach and promenade position are repeatedly praised by guests.",
            "Kitchen-and-balcony comments suggest the day-to-day apartment experience really works for families.",
            "The broader Baltic Park ecosystem still gives you weather-proof backup and dining choices.",
        ],
        "family_fit": [
            "Very plausible if the family wants Świnoujście but does not need the absolute newest-feeling apartment block.",
            "This is still much closer to your target shape than the classic rooms in Hilton or Radisson.",
        ],
        "availability": [
            "Booking.com and Tripadvisor both show active property footprint and live 2026 pricing signals.",
            "I did not verify the exact long-stay two-booking combination inside the official engine.",
            f"Research snapshot date: {RESEARCH_DATE}. Window checked: {STAY_WINDOW} ({STAY_NIGHTS} nights).",
        ],
        "watchouts": [
            "Reception being in another building, parking friction, and extra fees come up regularly.",
            "It looks easy to use once settled, but less seamless than Molo on the arrival/operations side.",
        ],
        "sources": [
            ("Official apartment page", "https://zdrojowahotels.pl/en/baltic-park-fort"),
            ("Booking.com listing", "https://www.booking.com/hotel/pl/baltic-park-fort-by-zdrojowa.pl.html"),
        ],
    },
    {
        "rank": 9,
        "slug": "golden-tulip-gdansk-residence",
        "name": "Golden Tulip Gdańsk Residence",
        "town": "Sopot edge / Jelitkowo",
        "town_slug": "sopot",
        "image": "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/1b/63/8f/bc/golden-tulip-gdansk-residence.jpg?w=1600&h=1000&s=1",
        "image_credit": "Tripadvisor property photo",
        "signal": "Best apartment-style family option around Sopot",
        "signal_class": "strong",
        "headline": "The strongest Sopot-area fit, even though it sits just on the Gdańsk side of the beach.",
        "summary": (
            "If the goal is Sopot-style access without losing the apartment logic, this is the property to know. "
            "Golden Tulip Gdańsk Residence sits in Jelitkowo near the Sopot edge, right by the sand, and the official "
            "description explicitly says the rooms have fully equipped kitchenettes."
        ),
        "why_it_works": [
            "Kitchenettes are clearly described in the official product and guest reviews.",
            "Families repeatedly mention the beach walk, play areas, paddling pool, and larger room layouts.",
            "This is the cleanest answer I found for 'Sopot, but with family apartment practicality.'",
        ],
        "family_fit": [
            "Very strong if you want the Tri-City zone but do not need to sleep right by Sopot pier.",
            "It is more convincing for your brief than the classic luxury hotels in central Sopot.",
        ],
        "availability": [
            "Tripadvisor metasearch returned live pricing for the sample stay, and Booking.com review traffic is deep and current.",
            "I did not verify the exact parents-plus-kids plus grandparents combination in a direct booking engine.",
            f"Research snapshot date: {RESEARCH_DATE}. Window checked: {STAY_WINDOW} ({STAY_NIGHTS} nights).",
        ],
        "watchouts": [
            "This is a Sopot-area solution, not a literal central-Sopot-on-the-pier solution.",
            "Several guests mention soft beds, occasional cleaning inconsistency, and limited kitchen hardware in some categories.",
        ],
        "sources": [
            ("Official residence site", "https://www.gdanskgoldentulip.pl/en/"),
            ("Booking.com reviews", "https://www.booking.com/reviews/pl/hotel/golden-tulip-gdansk-residence.html"),
        ],
    },
    {
        "rank": 10,
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
            "Apollo Residence still looks good from a pure apartment point of view. The official site highlights seaside apartments "
            "roughly 38 to 120 square meters in size, which is exactly the kind of space profile that works for parents with two "
            "young kids. The catch is that the site behaves more like an apartment residence than a conventional hotel booking flow."
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
            "The site does not make hotel-connected service levels as clear as Rosevia, Linea Mare, or Baltic Park Molo.",
        ],
        "sources": [
            ("Official residence site", "https://apollo.masterm.pl/"),
        ],
    },
    {
        "rank": 11,
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
            "category, and the children section highlights attractions, amenities, animations, and baby support. It remains one of "
            "the best hotel-first fallbacks if the apartment-led properties tighten."
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
        "rank": 12,
        "slug": "shellter-rogowo",
        "name": "Shellter Hotel Resort & Spa",
        "town": "Rogowo",
        "town_slug": "rogowo",
        "image": "https://hotelshellter.pl/wp-content/uploads/2025/02/DSCF3886-HDR-scaled.jpg",
        "image_credit": "Official hotel image",
        "signal": "Good family-resort signal, but apartment depth is less clear than the stronger beach ecosystems",
        "signal_class": "strong",
        "headline": "A plausible quiet-family resort, but weaker than the top apartment-led choices.",
        "summary": (
            "The Shellter official site leans heavily into family-with-children positioning and mentions a playroom, game room, "
            "children’s water zone, and animations. As a family resort it makes sense. What I still cannot prove as strongly is that "
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
            "Official booking page exists, but I did not capture the same hard long-stay inventory proof as the verified group.",
            "Use this one as a secondary shortlist candidate, not the first call.",
        ],
        "watchouts": [
            "The source note used the name `Shelter`; the official property name appears to be `Shellter`.",
            "The official evidence for apartment depth is weaker than at Rosevia, Linea Mare, or Baltic Park Molo.",
        ],
        "sources": [
            ("Official hotel site", "https://hotelshellter.pl/en/homepage/"),
            ("Reservation page", "https://hotelshellter.pl/en/reservation/"),
        ],
    },
    {
        "rank": 13,
        "slug": "sopot-marriott-resort-spa",
        "name": "Sopot Marriott Resort & Spa",
        "town": "Sopot",
        "town_slug": "sopot",
        "image": "https://www.sopotmarriott.pl/resourcefiles/homeimages/widok-z-lotu-ptaka_1.png?version=3302026103048",
        "image_credit": "Official hotel image",
        "signal": "Premium direct-beach hotel, but more hotel-first than apartment-first",
        "signal_class": "manual",
        "headline": "Best classic beachfront Sopot hotel if you decide apartment shape matters less.",
        "summary": (
            "Sopot Marriott is a strong beachfront resort with an excellent location, spa depth, and a family-friendly tone. "
            "It lands mid-pack because it looks like a very good hotel stay, not because it is the cleanest answer to the apartment-plus-grandparents-room brief."
        ),
        "why_it_works": [
            "Direct beach position is one of the strongest in the whole Sopot area.",
            "Booking and Tripadvisor both point to strong spa, breakfast, and family comfort.",
            "This is a good fallback if you want Sopot itself more than apartment certainty.",
        ],
        "family_fit": [
            "Works best if the parents-and-kids group can live comfortably in a hotel room or suite instead of an apartment.",
            "Grandparents would likely find the classic resort format easy.",
        ],
        "availability": [
            "Tripadvisor metasearch returned live sample-stay pricing and Booking.com has an active 2026 property footprint.",
            "I did not verify a two-booking setup with a separate grandparents room and kitchenette-bearing family unit.",
            f"Research snapshot date: {RESEARCH_DATE}. Window checked: {STAY_WINDOW} ({STAY_NIGHTS} nights).",
        ],
        "watchouts": [
            "This is more hotel-and-spa than apartment-and-residence.",
            "Value for money and room shape matter more here than beach quality, which is excellent.",
        ],
        "sources": [
            ("Official hotel site", "https://www.sopotmarriott.pl/"),
            ("Booking.com reviews", "https://www.booking.com/reviews/pl/hotel/sopot-marriott-resort-and-spa.html"),
        ],
    },
    {
        "rank": 14,
        "slug": "sheraton-sopot-hotel",
        "name": "Sheraton Sopot Hotel",
        "town": "Sopot",
        "town_slug": "sopot",
        "image": "https://www.sheratonsopot.pl/resourcefiles/homeimages/basen-sea-soul-spa.png?version=4082026121856",
        "image_credit": "Official hotel image",
        "signal": "Iconic beachfront Sopot hotel, but fundamentally hotel-first",
        "signal_class": "manual",
        "headline": "Prime central Sopot location, yet a weaker fit for the apartment brief than it first appears.",
        "summary": (
            "Sheraton Sopot is the obvious flagship if central Sopot matters. It is directly by the beach and pier, has high review scores, "
            "and would be easy to love as a premium hotel trip. It stays below the residence-style options because the room shape is simply less aligned with what you asked for."
        ),
        "why_it_works": [
            "Direct beach and pier location are hard to beat.",
            "Review evidence around breakfast, location, and room comfort is consistently strong.",
            "Grandparents would likely enjoy the classic luxury-hotel format.",
        ],
        "family_fit": [
            "The location is exceptional, but the apartment-with-kitchen logic is much weaker than at Golden Tulip Gdańsk Residence.",
            "This is better if the family is happy with premium hotel rooms rather than apartment living.",
        ],
        "availability": [
            "Booking.com and Tripadvisor both show strong active property signal and live 2026 visibility.",
            "I did not verify a family apartment plus separate grandparents-room combination, because that is not the natural product shape here.",
            f"Research snapshot date: {RESEARCH_DATE}. Window checked: {STAY_WINDOW} ({STAY_NIGHTS} nights).",
        ],
        "watchouts": [
            "This is likely one of the pricier Sopot options.",
            "If the kitchenette preference is real, central-Sopot prestige does not make up for the room-shape mismatch.",
        ],
        "sources": [
            ("Official hotel site", "https://www.sheratonsopot.pl/"),
            ("Booking.com reviews", "https://www.booking.com/reviews/pl/hotel/sheratonsopot.html"),
        ],
    },
    {
        "rank": 15,
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
            "Grand Lubicz remains a strong Ustka option with heavyweight pools, wellness, and family weather-proofing. "
            "It lands lower only because the newer additions brought in more apartment-native options right on the beach."
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
        "rank": 16,
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
            "Kids Club, beach proximity, bowling, and lots of activity. It still reads more like a hotel-first decision than the "
            "apartment-leaning options above it."
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
            "Kołobrzeg has better beach-apartment answers nearby than the core hotel itself.",
        ],
        "sources": [
            ("Official hotel site", "https://zdrojowahotels.pl/en/marine-hotel"),
        ],
    },
    {
        "rank": 17,
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
            "Hilton still belongs in the landscape because the broader Baltic Park district is so promising. "
            "But once Molo and Fort are on the table, the Hilton becomes much easier to classify: premium hotel, weaker room-shape fit."
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
        "rank": 18,
        "slug": "radisson-blu-swinoujscie",
        "name": "Radisson Blu Resort, Świnoujście",
        "town": "Świnoujście",
        "town_slug": "swinoujscie",
        "image": "",
        "image_credit": "",
        "signal": "Big-resort option, but not a leading fit for the apartment brief",
        "signal_class": "manual",
        "headline": "A strong mainstream resort, but not the first place to start for this room format.",
        "summary": (
            "Radisson Blu in Świnoujście still makes sense in a conventional luxury-hotel comparison. "
            "For this study, though, the apartment-led properties in the same district simply solve the brief more directly."
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
            "This stayed in the study because it appeared in the source notes, not because it beat the apartment-led properties nearby.",
        ],
        "watchouts": [
            "Apartment certainty is weak.",
            "Compared with Baltic Park Molo or Fort in the same district, this looks less naturally aligned with your stated setup.",
        ],
        "sources": [
            ("Official Radisson site", "https://www.radissonhotels.com/en-us/hotels/radisson-blu-resort-swinoujscie"),
            ("Local resort page", "https://zdrojowahotels.pl/en/radisson-blu"),
        ],
    },
    {
        "rank": 19,
        "slug": "baltic-park-loft",
        "name": "Baltic Park Loft by Zdrojowa",
        "town": "Świnoujście",
        "town_slug": "swinoujscie",
        "image": "",
        "image_credit": "",
        "signal": "Same complex ecosystem, but still the weakest direct evidence in this pass",
        "signal_class": "strong",
        "headline": "Worth checking if Molo and Fort are tight, but still the lowest-confidence Baltic Park lead.",
        "summary": (
            "Baltic Park Loft sits in the same attractive zone and Booking evidence suggests modern apartments, usable kitchens, "
            "Hilton breakfast, and aquapark access. The reason it sits last is not that it looks bad. The reason is that its direct evidence base "
            "is thinner than Molo, Fort, and the stronger standalone resorts."
        ),
        "why_it_works": [
            "Booking reviews point to modern interiors, beach access, kitchen usability, and family stays with children.",
            "The same Baltic Park ecosystem still gives you a very practical weather-proof vacation setup.",
            "This may become important if you decide Świnoujście is the town and the first two apartment buildings are sold out.",
        ],
        "family_fit": [
            "Potentially useful as a backup within the best new ecosystem added in this pass.",
            "Harder to rank high because it is the least independently proven property in that cluster.",
        ],
        "availability": [
            "Booking.com shows an active 2026 listing and review footprint, and Tripadvisor metasearch surfaced live pricing.",
            "I did not verify the exact multi-room July setup or find as much deep review context as for Molo and Fort.",
            f"Research snapshot date: {RESEARCH_DATE}. Window checked: {STAY_WINDOW} ({STAY_NIGHTS} nights).",
        ],
        "watchouts": [
            "This is the weakest-evidence property in the Baltic Park group.",
            "Service follow-through and sofa-bed comfort appear in the limited complaint set that is available.",
        ],
        "sources": [
            ("Official apartment page", "https://zdrojowahotels.pl/en/baltic-park-loft"),
            ("Booking.com listing", "https://www.booking.com/hotel/pl/baltic-park-loft-by-zdrojowa.html"),
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
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1e/Miedzyzdroje_plaza_%281%29.jpg/1200px-Miedzyzdroje_plaza_%281%29.jpg",
        "headline": "Now a two-path town: premium Wave on one side, practical family apartments on the other.",
        "summary": (
            "Międzyzdroje got stronger in this pass. Wave still covers the premium-apartment fantasy, but Golden Tulip Międzyzdroje "
            "Residence gives the town a second, more grounded family-apartment option close to the beach."
        ),
        "best_for": [
            "Families who want a classic resort town with a real promenade and proper beach rhythm.",
            "Trips where you want a choice between upscale resort feel and calmer apartment practicality.",
        ],
        "watchouts": [
            "Premium pricing is likely at the top end of the town's hotel set.",
            "Wave looks great, but Golden Tulip may be the safer value-and-layout answer for longer family stays.",
        ],
        "source_links": [
            ("Wikipedia", "https://pl.wikipedia.org/wiki/Międzyzdroje"),
            ("Official town site", "https://miedzyzdroje.pl/"),
            ("Wave Międzyzdroje", "https://wavemiedzyzdroje.pl/"),
            ("Golden Tulip Międzyzdroje Residence", "https://miedzyzdroje.goldentulip.com/en-us/"),
        ],
    },
    {
        "slug": "sopot",
        "name": "Sopot",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/04/Sopot_Molo_and_main_square_2024_aerial.jpg/1200px-Sopot_Molo_and_main_square_2024_aerial.jpg",
        "headline": "Beautiful beach-and-pier town, but the best family apartment fit sits just outside the postcard core.",
        "summary": (
            "Sopot is still one of the nicest seaside towns in Poland, but the family-layout answer is split in two. "
            "Sheraton and Marriott give you central or direct-beach resort quality, while Golden Tulip Gdańsk Residence "
            "on the Jelitkowo edge gives you the stronger apartment-with-kitchenette logic."
        ),
        "best_for": [
            "Families who want the Tri-City zone, beach access, and the option of a more polished urban-seaside trip.",
            "Trips where grandparents may appreciate Sopot's walkability, cafes, and easier off-beach dining.",
        ],
        "watchouts": [
            "The cleanest apartment-style family option is not right at Sopot pier; it sits closer to the Gdańsk / Jelitkowo side.",
            "True central Sopot beachfront hotels are strong on location but weaker on kitchenette-first family practicality.",
        ],
        "source_links": [
            ("Wikipedia", "https://en.wikipedia.org/wiki/Sopot"),
            ("Official tourism site", "https://visit.sopot.pl/"),
            ("Sheraton Sopot Hotel", "https://www.sheratonsopot.pl/"),
            ("Sopot Marriott Resort & Spa", "https://www.sopotmarriott.pl/"),
            ("Golden Tulip Gdańsk Residence", "https://www.gdanskgoldentulip.pl/en/"),
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
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/85/Swinoujscie_%28dron2%29.jpg/1200px-Swinoujscie_%28dron2%29.jpg",
        "headline": "Now one of the strongest town ecosystems in the study because the Baltic Park apartments finally solve the room shape.",
        "summary": (
            "Świnoujście changed the most in this pass. Once Baltic Park Molo, Fort, and Loft are added to the Hilton and Radisson context, "
            "the town stops looking like a hotel-first compromise and starts looking like one of the easiest kid-and-grandparents resort ecosystems on the coast."
        ),
        "best_for": [
            "Families who want one huge beach, a real promenade, aquapark backup, and easy food access.",
            "Trips where the family wants apartment living but still wants branded-hotel infrastructure nearby.",
        ],
        "watchouts": [
            "The Baltic Park district looks strong, but exact check-in and breakfast rules vary by building and should be confirmed.",
            "It is still a bigger, busier resort city than places like Pobierowo or Grzybowo.",
        ],
        "source_links": [
            ("Wikipedia", "https://pl.wikipedia.org/wiki/Świnoujście"),
            ("Official city site", "https://www.swinoujscie.pl/"),
            ("Baltic Park Molo", "https://zdrojowahotels.pl/en/baltic-park-molo"),
            ("Baltic Park Fort", "https://zdrojowahotels.pl/en/baltic-park-fort"),
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
            ("Kawcza Góra viewpoint", maps_search_url("Kawcza Góra Międzyzdroje")),
            ("Baltic Miniature Park", maps_search_url("Bałtycki Park Miniatur Międzyzdroje")),
        ],
        "gallery": [
            (
                "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1e/Miedzyzdroje_plaza_%281%29.jpg/1200px-Miedzyzdroje_plaza_%281%29.jpg",
                "Międzyzdroje beach",
                "Wikipedia image",
                "https://en.wikipedia.org/wiki/Mi%C4%99dzyzdroje",
            ),
            (
                "https://upload.wikimedia.org/wikipedia/commons/thumb/b/be/Mi%C4%99dzyzdroje_31%2C_wej%C5%9Bcie_na_molo.jpg/1000px-Mi%C4%99dzyzdroje_31%2C_wej%C5%9Bcie_na_molo.jpg",
                "Międzyzdroje pier entrance",
                "Wikipedia image",
                "https://en.wikipedia.org/wiki/Mi%C4%99dzyzdroje",
            ),
            (
                commons_file_url("Molo Międzyzdroje4.JPG"),
                "Międzyzdroje pier from the water",
                "Wikimedia Commons",
                commons_page_url("Molo Międzyzdroje4.JPG"),
            ),
        ],
    },
    "sopot": {
        "family_spots": [
            ("Sopot Pier", maps_search_url("Molo Sopot")),
            ("Main beach", maps_search_url("Plaża Sopot")),
            ("Monte Cassino promenade", maps_search_url("Bohaterów Monte Cassino Sopot")),
            ("Aquapark Sopot", maps_search_url("Aquapark Sopot")),
        ],
        "gallery": [
            (
                "https://upload.wikimedia.org/wikipedia/commons/thumb/0/04/Sopot_Molo_and_main_square_2024_aerial.jpg/1200px-Sopot_Molo_and_main_square_2024_aerial.jpg",
                "Sopot pier and square from above",
                "Wikipedia image",
                "https://en.wikipedia.org/wiki/Sopot",
            ),
            (
                "https://visit.sopot.pl/cmsImages/banerFacebook.jpg",
                "Sopot beachfront mood shot",
                "Visit Sopot official image",
                "https://visit.sopot.pl/",
            ),
            (
                "https://visit.sopot.pl/res/475377/28729821/teznia-solankowa-3-600x400.jpg",
                "Sopot brine graduation tower",
                "Visit Sopot official image",
                "https://visit.sopot.pl/",
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
            ("Baltic Park Molo Aquapark", maps_search_url("Baltic Park Molo Aquapark by Zdrojowa Świnoujście")),
            ("Promenade", maps_search_url("Promenada Świnoujście")),
            ("Stawa Młyny", maps_search_url("Stawa Młyny Świnoujście")),
            ("Lighthouse", maps_search_url("Latarnia Morska Świnoujście")),
        ],
        "gallery": [
            (
                "https://upload.wikimedia.org/wikipedia/commons/thumb/8/85/Swinoujscie_%28dron2%29.jpg/1200px-Swinoujscie_%28dron2%29.jpg",
                "Świnoujście beach district from above",
                "Wikipedia image",
                "https://en.wikipedia.org/wiki/%C5%9Awinouj%C5%9Bcie",
            ),
            (
                "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4d/Beacon_Stawa_M%C5%82yny%2C_%C5%9Awinouj%C5%9Bcie.jpg/1200px-Beacon_Stawa_M%C5%82yny%2C_%C5%9Awinouj%C5%9Bcie.jpg",
                "Stawa Młyny beacon",
                "Wikipedia image",
                "https://en.wikipedia.org/wiki/%C5%9Awinouj%C5%9Bcie",
            ),
            (
                "https://upload.wikimedia.org/wikipedia/commons/thumb/a/af/%C5%9Awinouj%C5%9Bcie_widok_z_promu.JPG/1200px-%C5%9Awinouj%C5%9Bcie_widok_z_promu.JPG",
                "Świnoujście harbor-side view",
                "Wikipedia image",
                "https://en.wikipedia.org/wiki/%C5%9Awinouj%C5%9Bcie",
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
    "baltic-park-molo": {
        "maps": maps_search_url("Baltic Park Molo Apartments by Zdrojowa Świnoujście"),
        "booking_url": booking_search_url("Baltic Park Molo Apartments by Zdrojowa Świnoujście"),
        "booking_snapshot": "Booking.com: about 8.4/10 from roughly 789 reviews.",
        "booking_praise": [
            "Guests often praise the location, easy beach access, promenade energy, and the practical apartment layout.",
            "Family stays repeatedly call out the aquapark access and the convenience of having restaurants and cafes nearby.",
        ],
        "booking_watch": [
            "Parking costs, sofa-bed comfort, and some arrival-day coordination problems are recurring complaints.",
            "The complex feels easy once settled, but guest feedback suggests check-in details should be read carefully.",
        ],
        "tripadvisor_url": tripadvisor_search_url("Baltic Park Molo Apartments by Zdrojowa"),
        "tripadvisor_snapshot": "Tripadvisor: 4.1/5 from 34 reviews.",
        "tripadvisor_praise": [
            "Tripadvisor guests like the roomy apartments, beach location, and the feeling of being inside a lively resort district.",
            "Positive reviews also mention that the setup works well for longer family stays compared with standard hotel rooms.",
        ],
        "tripadvisor_watch": [
            "Ventilation, street noise, late-arrival communication, and extra parking cost show up more than once.",
            "Some guests found the sofa bed weaker than the main bed, which matters for a longer stay.",
        ],
    },
    "golden-tulip-miedzyzdroje": {
        "maps": maps_search_url("Golden Tulip Międzyzdroje Residence"),
        "booking_url": "https://www.booking.com/reviews/pl/hotel/golden-tulip-miedzyzdroje-residence.en-gb.html",
        "booking_snapshot": "Booking.com: deep active review footprint with strong family-apartment sentiment.",
        "booking_praise": [
            "Booking reviews repeatedly emphasize large apartments, good breakfast, and the short walk to the beach.",
            "Families especially like the calmer location and the feeling of having usable space rather than just a hotel room.",
        ],
        "booking_watch": [
            "The quieter edge-of-town location is not ideal if you want maximum promenade life right outside the door.",
            "A few guests mention smaller wellness facilities and uneven Wi‑Fi quality.",
        ],
        "tripadvisor_url": tripadvisor_search_url("Golden Tulip Międzyzdroje Residence"),
        "tripadvisor_snapshot": "Tripadvisor: 4.2/5 from 217 reviews.",
        "tripadvisor_praise": [
            "Tripadvisor guests like the huge apartments, beach proximity, and the fact that the property feels genuinely family-ready.",
            "Breakfast quality and roomy layouts are more consistent themes than luxury-service complaints.",
        ],
        "tripadvisor_watch": [
            "The wellness zone appears smaller than the room product deserves.",
            "Some reviews frame the location as a little outside the center, which is either peaceful or mildly inconvenient.",
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
            "This reinforces the view that the property is very attractive but less operationally proven than the most verified tier.",
        ],
    },
    "baltic-park-fort": {
        "maps": maps_search_url("Baltic Park Fort by Zdrojowa Świnoujście"),
        "booking_url": "https://www.booking.com/hotel/pl/baltic-park-fort-by-zdrojowa.pl.html",
        "booking_snapshot": "Booking.com: about 8.3/10 from roughly 1,152 reviews.",
        "booking_praise": [
            "Guests like the beach-side position, larger apartments, and the convenience of the surrounding Baltic Park district.",
            "Families often mention aquapark access and the practical kitchen-and-balcony setup.",
        ],
        "booking_watch": [
            "Reception being outside the building and parking friction show up frequently.",
            "Several guests also mention extra cleaning or fee surprises that are worth checking before payment.",
        ],
        "tripadvisor_url": tripadvisor_search_url("Baltic Park Fort by Zdrojowa"),
        "tripadvisor_snapshot": "Tripadvisor: 3.9/5 from 26 reviews.",
        "tripadvisor_praise": [
            "Tripadvisor guests repeatedly praise the beach location, breakfast access in the Radisson/Hilton ecosystem, and apartment size.",
            "The kitchen and balcony comments support it as a genuinely usable family stay, not just a nice-looking listing.",
        ],
        "tripadvisor_watch": [
            "Administrative friction, parking, and reception logistics come up in weaker reviews.",
            "This looks practical, but less smooth than Molo.",
        ],
    },
    "golden-tulip-gdansk-residence": {
        "maps": maps_search_url("Golden Tulip Gdańsk Residence"),
        "booking_url": "https://www.booking.com/reviews/pl/hotel/golden-tulip-gdansk-residence.html",
        "booking_snapshot": "Booking.com: about 8.7/10 from roughly 3,500 reviews.",
        "booking_praise": [
            "Booking reviewers frequently call out the short beach walk, family facilities, and larger suite-like room feel.",
            "The property stands out as a better practical family stay than many classic Sopot hotels.",
        ],
        "booking_watch": [
            "Soft beds, inconsistent cleaning, and some kitchen limitations show up often enough to note.",
            "This is also more of a Sopot-edge location than a pure central-Sopot address.",
        ],
        "tripadvisor_url": tripadvisor_search_url("Golden Tulip Gdańsk Residence"),
        "tripadvisor_snapshot": "Tripadvisor: 4.1/5 from 449 reviews.",
        "tripadvisor_praise": [
            "Tripadvisor guests praise the beach access, paddling-pool-and-playroom family setup, and roomy units with kitchenettes.",
            "The comments line up well with a longer family stay rather than a short luxury break.",
        ],
        "tripadvisor_watch": [
            "Noise and cleanliness consistency appear more than once.",
            "Some reviewers felt the kitchenette hardware was basic rather than fully apartment-grade.",
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
    "sopot-marriott-resort-spa": {
        "maps": maps_search_url("Sopot Marriott Resort & Spa"),
        "booking_url": "https://www.booking.com/reviews/pl/hotel/mera-spa.html",
        "booking_snapshot": "Booking.com: strong direct-beach review signal with high recent satisfaction.",
        "booking_praise": [
            "Booking guests repeatedly praise the beach position, breakfast quality, rooftop views, and family-friendly atmosphere.",
            "This reads like a strong premium resort stay for families who do not insist on apartment living.",
        ],
        "booking_watch": [
            "Value for money and room shape are the main tradeoffs, especially for longer stays.",
            "It looks better as a premium hotel choice than as a kitchenette-led family base.",
        ],
        "tripadvisor_url": tripadvisor_search_url("Sopot Marriott Resort & Spa"),
        "tripadvisor_snapshot": "Tripadvisor: 4.4/5 from 928 reviews.",
        "tripadvisor_praise": [
            "Tripadvisor guests like the beach setting, pools, spa quality, and generally polished resort feel.",
            "The hotel performs well as a comfortable classic resort with kids and grandparents.",
        ],
        "tripadvisor_watch": [
            "The biggest issue for this study is shape, not quality: it is still more hotel than apartment.",
            "Some guests also question value versus the rate level in peak season.",
        ],
    },
    "sheraton-sopot-hotel": {
        "maps": maps_search_url("Sheraton Sopot Hotel"),
        "booking_url": "https://www.booking.com/reviews/pl/hotel/sheratonsopot.html",
        "booking_snapshot": "Booking.com: about 9.1/10 from roughly 2,972 reviews.",
        "booking_praise": [
            "Guests love the direct beach-and-pier location, strong breakfast, and the easy feeling of a premium central Sopot stay.",
            "The overall review tone is very strong if you want a classic luxury-hotel trip.",
        ],
        "booking_watch": [
            "Deposits, parking cost, and the lack of apartment-style room flexibility are the main practical negatives.",
            "This is a location-led luxury choice, not a kitchenette-led family-residence solution.",
        ],
        "tripadvisor_url": tripadvisor_search_url("Sheraton Sopot Hotel"),
        "tripadvisor_snapshot": "Tripadvisor: 4.4/5 from 1,037 reviews.",
        "tripadvisor_praise": [
            "Tripadvisor reviews strongly praise the location, breakfast, lounge, and private-beach feel.",
            "The guest tone supports it as a dependable central-Sopot flagship hotel.",
        ],
        "tripadvisor_watch": [
            "Parking, crowding, and value-for-money complaints recur more than serious quality failures.",
            "For this study, the bigger issue is still room shape rather than service weakness.",
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
    "baltic-park-loft": {
        "maps": maps_search_url("Baltic Park Loft by Zdrojowa Świnoujście"),
        "booking_url": "https://www.booking.com/hotel/pl/baltic-park-loft-by-zdrojowa.html",
        "booking_snapshot": "Booking.com: about 8.6/10 from roughly 242 reviews.",
        "booking_praise": [
            "Early guest feedback likes the modern apartments, beach access, kitchen practicality, and the same Baltic Park ecosystem benefits as the stronger sister buildings.",
            "The raw apartment product appears family-usable and well located.",
        ],
        "booking_watch": [
            "The review footprint is much thinner than for Molo and Fort, so confidence is lower.",
            "As with the rest of the complex, parking and operational details need careful checking.",
        ],
        "tripadvisor_url": tripadvisor_search_url("Baltic Park Loft by Zdrojowa"),
        "tripadvisor_snapshot": "Tripadvisor: no stable review footprint surfaced in this pass.",
        "tripadvisor_praise": [
            "Treat this mainly as a same-ecosystem backup if the stronger Baltic Park buildings are too tight or too expensive.",
        ],
        "tripadvisor_watch": [
            "This is the weakest-supported listing in the new Świnoujście cluster.",
            "Without deeper review depth, it should stay behind Molo and Fort.",
        ],
    },
}


HOTELS_BY_TOWN = {}
for hotel in HOTELS:
    HOTELS_BY_TOWN.setdefault(hotel["town_slug"], []).append(hotel)


SHORTLIST = [hotel for hotel in HOTELS if hotel["rank"] <= 6]

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
    "baltic-park-molo": {
        "family_unit": "Strong apartment fit",
        "grandparents_room": "Likely in same ecosystem; confirm exact pairing",
        "kitchenette": "High confidence: official description says kitchenette",
    },
    "golden-tulip-miedzyzdroje": {
        "family_unit": "Strong apartment fit",
        "grandparents_room": "Likely",
        "kitchenette": "High confidence from listings and reviews",
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
    "baltic-park-fort": {
        "family_unit": "Strong apartment fit",
        "grandparents_room": "Likely in same ecosystem; confirm exact pairing",
        "kitchenette": "Good evidence from guest reviews",
    },
    "golden-tulip-gdansk-residence": {
        "family_unit": "Strong apartment fit",
        "grandparents_room": "Likely",
        "kitchenette": "High confidence: official description says kitchenette",
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
    "sopot-marriott-resort-spa": {
        "family_unit": "Possible, but hotel-first",
        "grandparents_room": "Likely",
        "kitchenette": "Weak evidence",
    },
    "sheraton-sopot-hotel": {
        "family_unit": "Possible, but hotel-first",
        "grandparents_room": "Likely",
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
    "baltic-park-loft": {
        "family_unit": "Possible backup",
        "grandparents_room": "Possible in same ecosystem",
        "kitchenette": "Moderate evidence",
    },
}


FLYOUT_ROUTE_NOTES = [
    {
        "title": "Aachen to Frankfurt airport is workable on normal-morning trains",
        "body": (
            "Deutsche Bahn search pages surfaced sample Aachen Hbf -> Frankfurt Airport long-distance station journeys of "
            "06:18–08:19 and 07:38–09:13, plus a two-hour pattern. That makes late-morning to afternoon flights realistic "
            "without a stressful middle-of-the-night departure."
        ),
        "links": [
            ("DB journey search snapshot", "https://www.bahn.de/reisen/view/verbindung/aachen/flughafen-frankfurt.shtml"),
            ("Trip.com timing snapshot", "https://de.trip.com/trains/germany/route/aachen-to-frankfurt-m-flughafen-fernbf/"),
        ],
    },
    {
        "title": "Croatia has the cleanest open-jaw geometry",
        "body": (
            "Discover's published summer 2026 schedule shows non-stop Frankfurt service to Dubrovnik, Split, Zadar, and Lamezia's "
            "Croatian peers sit inside the same family of leisure routes. Wrocław's timetable and route databases also show direct "
            "seasonal returns from the Adriatic, so Croatia wins on transport simplicity."
        ),
        "links": [
            ("Discover summer 2026 schedule", "https://www.discover-airlines.com/content/dam/four_y/pdfs/b2b/4y_summer-flight-schedule_2026.pdf"),
            ("Wrocław Airport timetable", "https://airport.wroclaw.pl/en/passenger/departure/timetable/"),
        ],
    },
    {
        "title": "Italy works, but only when the resort is strong enough",
        "body": (
            "Italy can absolutely beat Poland on beauty, but the route layer is less forgiving. Sicily scored down because the direct "
            "Frankfurt -> Catania flight pattern is early enough to push you toward an airport hotel, while Calabria and Puglia scored "
            "better only when the resort itself clearly solved the apartment-plus-beach brief."
        ),
        "links": [
            ("Lufthansa Frankfurt -> Catania flight page", "https://www.flight.info/LH306"),
            ("FlightsFrom Frankfurt -> Lamezia", "https://www.flightsfrom.com/FRA-SUF"),
        ],
    },
    {
        "title": "Southern France is the best new route add through Nice",
        "body": (
            "France does not beat Croatia on apartment-resort depth, but Nice is a very comfortable transport gateway: Lufthansa runs "
            "frequent Frankfurt -> Nice service, and Wrocław's new Wizz Air Nice route gives a direct return several times a week. "
            "The best properties are either a proper beach residence tied to hotel services or a big holiday village above Agay Bay."
        ),
        "links": [
            ("Frankfurt -> Nice route", "https://www.flightsfrom.com/FRA-NCE"),
            ("Nice -> Wrocław route", "https://www.flightsfrom.com/NCE-WRO"),
            ("Wrocław Airport Nice announcement", "https://airport.wroclaw.pl/en/as-many-as-7-new-routes-from-wizz-air-from-wroclaw/"),
        ],
    },
]


FLYOUT_HOTELS = [
    {
        "flyout_rank": 1,
        "slug": "falkensteiner-residences-senia",
        "name": "Falkensteiner Residences Senia",
        "town": "Punta Skala / Petrčane",
        "town_slug": "punta-skala-petrcane",
        "image": "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/1c/2b/a5/bb/outdoor-pool.jpg?w=1600&h=1000&s=1",
        "image_credit": "Tripadvisor property photo",
        "signal": "Best fly-out balance of apartment proof, resort access, and Croatia routing",
        "signal_class": "strong",
        "headline": "The cleanest foreign fit if you want a real apartment inside a premium resort ecosystem.",
        "summary": (
            "Residences Senia is the strongest foreign addition because it checks almost every box at once: serviced apartments, "
            "sea-facing terraces, clear kitchen equipment evidence, resort restaurants and sports, and a travel pattern that is much "
            "more forgiving than Sicily. It is not the cheapest option, but this is exactly the type of abroad-only product that "
            "actually justifies the flight effort."
        ),
        "why_it_works": [
            "The official page calls Senia a set of premium sea-view holiday apartments inside Punta Skala, with breakfast and half-board options within the resort.",
            "Booking.com explicitly lists apartments with microwave, coffee machine, dishwasher, sofa bed, and balcony.",
            "Tripadvisor returned live June 27 to July 11 pricing for 2 rooms and describes it as serviced apartments inside a private resort peninsula.",
        ],
        "family_fit": [
            "Very strong if parents and kids want apartment living, but still want resort restaurants, pools, and sports nearby.",
            "This is also one of the easiest foreign leads for grandparents because they can stay in a classic neighboring room product inside the same Punta Skala system.",
        ],
        "availability": [
            "Tripadvisor returned live pricing for the sample window: from about USD 12,410 total for 2 rooms over 14 nights, with official-hotel availability visible.",
            "The official Falkensteiner site shows one-bedroom and two-bedroom residences, and the rental pages remain actively bookable for summer 2026.",
            f"Research snapshot date: {RESEARCH_DATE}. Window checked: {FLYOUT_WINDOW} ({FLYOUT_NIGHTS} nights).",
        ],
        "travel_fit": [
            "Aachen -> Frankfurt airport is realistic on standard-morning rail timings, so this can be a same-day departure if you target the later Zadar rotation instead of the earliest one.",
            "Discover's summer 2026 schedule shows non-stop Frankfurt -> Zadar service, and Wrocław's network still shows direct seasonal Zadar links.",
            "Current Zadar -> Wrocław schedule data shows an unpleasant 05:45 Monday pattern, so this is best booked around a non-Monday return if the final summer timetable stays similar.",
        ],
        "watchouts": [
            "One 2025 Tripadvisor review flagged construction in front of parts of the residence blocks.",
            "Value-for-money is weaker than the location and apartment quality, and some wellness access sits in the neighboring hotel stack rather than fully inside Senia itself.",
        ],
        "window": FLYOUT_WINDOW,
        "nights": FLYOUT_NIGHTS,
        "sources": [
            ("Official residences site", "https://www.falkensteiner.com/en/residences-senia"),
            ("Official apartment types", "https://www.falkensteiner.com/en/residences-senia/apartments"),
            ("Booking.com review page", "https://www.booking.com/reviews/hr/hotel/falkensteiner-senia-apartments-zadar.en-gb.html"),
            ("Tripadvisor listing", "https://www.tripadvisor.com/Hotel_Review-g1182225-d7707770-Reviews-Falkensteiner_Residences_Senia-Petrcane_Zadar_County_Dalmatia.html"),
            ("Discover summer 2026 schedule", "https://www.discover-airlines.com/content/dam/four_y/pdfs/b2b/4y_summer-flight-schedule_2026.pdf"),
            ("Zadar -> Wrocław route timing", "https://info.flightmapper.net/flight/Ryanair_FR_8494"),
        ],
    },
    {
        "flyout_rank": 2,
        "slug": "sun-gardens-dubrovnik",
        "name": "Sun Gardens Dubrovnik",
        "town": "Dubrovnik Riviera / Orašac",
        "town_slug": "dubrovnik-riviera-orasac",
        "image": "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/2b/ff/0a/1a/resort-aerial.jpg?w=1600&h=1000&s=1",
        "image_credit": "Tripadvisor property photo",
        "signal": "Most beautiful full-service residence resort in the foreign pass",
        "signal_class": "strong",
        "headline": "Best foreign luxury lead if the resort itself is the main event.",
        "summary": (
            "Sun Gardens is the most compelling 'this is why we flew abroad' property in the entire expansion. The residence product is "
            "clearly real rather than marketing fluff, the setting above the Adriatic is beautiful, and both Tripadvisor and Booking "
            "support the idea that families actually use it for longer, apartment-style stays rather than only short hotel breaks."
        ),
        "why_it_works": [
            "The residence pages explicitly show one- and two-bedroom sea-view and garden-view units with built-in or fully equipped kitchenettes.",
            "Tripadvisor returned live pricing for 2 rooms over the full 14-night sample and describes the resort as a five-star family resort with kids club, pools, beach, and sports center.",
            "Booking snippets mention two-bedroom residence categories and fully equipped kitchenettes, which is exactly the missing proof many luxury hotels never provide.",
        ],
        "family_fit": [
            "Extremely strong if the goal is a premium residence by the sea, with grandparents able to use the hotel side while the parents-and-kids unit lives more comfortably.",
            "This is also one of the most convincing 'beautiful enough to justify the flights' options in the study.",
        ],
        "availability": [
            "Tripadvisor surfaced live sample-stay pricing from about USD 9,727 total for the 2-room search, with multiple bookable partners visible.",
            "Booking.com has a heavy, current review footprint and explicitly references residence categories; I did not complete an official-engine two-booking pairing for parents-plus-kids and grandparents.",
            f"Research snapshot date: {RESEARCH_DATE}. Window checked: {FLYOUT_WINDOW} ({FLYOUT_NIGHTS} nights).",
        ],
        "travel_fit": [
            "Discover's summer 2026 schedule shows Frankfurt -> Dubrovnik operating daily from the end of March, which is the best Croatia frequency in the whole pass.",
            "Wrocław route databases still show direct seasonal Dubrovnik returns, so the open-jaw logic is clean even if the exact weekday choice still matters.",
            "The main transport trade-off is not route existence but the 20- to 25-minute final transfer from the airport and the need to choose a civilized outbound slot.",
        ],
        "watchouts": [
            "The resort is outside the old town, so this is a resort-first Dubrovnik trip rather than a walk-outside-and-you're-in-the-center trip.",
            "Some recent guest complaints mention slippery pool areas and occasional service inconsistency relative to the price.",
        ],
        "window": FLYOUT_WINDOW,
        "nights": FLYOUT_NIGHTS,
        "sources": [
            ("Official resort site", "https://www.dubrovniksungardens.com/"),
            ("Two-bedroom residence page", "https://www.dubrovniksungardens.com/en/accommodation/residences/two-bedroom-sea-view/two-bedroom-sea-view-residences"),
            ("Booking.com property page", "https://www.booking.com/hotel/hr/radisson-blu-resort-spa-dubrovnik-riviera.html"),
            ("Tripadvisor listing", "https://www.tripadvisor.com/Hotel_Review-g1943776-d1414005-Reviews-Sun_Gardens_Dubrovnik-Orasac_Dubrovnik_Dubrovnik_Neretva_County_Dalmatia.html"),
            ("Discover summer 2026 schedule", "https://www.discover-airlines.com/content/dam/four_y/pdfs/b2b/4y_summer-flight-schedule_2026.pdf"),
        ],
    },
    {
        "flyout_rank": 3,
        "slug": "zaton-holiday-resort",
        "name": "Zaton Holiday Resort",
        "town": "Zaton / Nin",
        "town_slug": "zaton-nin",
        "image": "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/11/45/4d/f4/zaton-holiday-resort.jpg?w=1600&h=1000&s=1",
        "image_credit": "Tripadvisor property photo",
        "signal": "Best all-in family ease if you value sandy beach and activity depth over polish",
        "signal_class": "strong",
        "headline": "The easiest Croatia resort for younger kids if you want everything on-site.",
        "summary": (
            "Zaton is less elegant than Senia or Sun Gardens, but it is one of the strongest pure family machines in the whole study: sandy "
            "beach, pine shade, apartments, supermarkets, pools, sports, playgrounds, and enough internal activity that you do not need to "
            "invent a plan every day."
        ),
        "why_it_works": [
            "The official site openly positions Zaton as a family-holiday destination with apartments, resort services, sandy beach, and multiple pool zones.",
            "The Nin tourism page confirms 3- and 4-star apartments in the resort, and Zaton's own apartment pages emphasize proximity to pools, playgrounds, and beach.",
            "Tripadvisor returned live 14-night pricing for 2 rooms and describes the resort as a family getaway with apartments in the pine forest and a long sandy beach.",
        ],
        "family_fit": [
            "Very strong with a 3-year-old and 6-year-old if you want flat, low-friction family days and less emphasis on luxury styling.",
            "It is a better practical answer than a romantic one: the stay works hard for children and grandparents, but it is not the chicest option in the foreign pass.",
        ],
        "availability": [
            "Tripadvisor returned active 2-room pricing for the sample stay from about USD 9,385 total.",
            "Booking review volume is very deep and current, which is a strong signal that the resort is both real and bookable for summer 2026.",
            f"Research snapshot date: {RESEARCH_DATE}. Window checked: {FLYOUT_WINDOW} ({FLYOUT_NIGHTS} nights).",
        ],
        "travel_fit": [
            "Like Senia, this can use the Frankfurt -> Zadar and Zadar -> Wrocław open-jaw geometry, with only a short final transfer from Zadar Airport.",
            "Zadar remains one of the more child-manageable foreign airports in the pass because you are not adding a long onward road transfer after landing.",
            "Return-day selection matters if the direct Zadar -> Wrocław pattern still includes the early Monday morning flight.",
        ],
        "watchouts": [
            "The resort is big, noisy, and sometimes described as crowded rather than peaceful.",
            "Tripadvisor and Booking complaints focus on buffet quality, extra charges, and too many people around the pool complex in peak periods.",
        ],
        "window": FLYOUT_WINDOW,
        "nights": FLYOUT_NIGHTS,
        "sources": [
            ("Official resort site", "https://www.zaton.hr/"),
            ("Official apartment notes", "https://www.zaton.hr/en/blog/253/finding-the-best-accommodation-at-zaton-holiday-resort"),
            ("Nin tourism page", "https://www.nin.hr/en/accommodation/zaton-holiday-resort"),
            ("Booking.com review page", "https://www.booking.com/reviews/hr/hotel/zaton-holiday-village.html"),
            ("Tripadvisor listing", "https://www.tripadvisor.com/Hotel_Review-g303820-d647873-Reviews-Zaton_Holiday_Resort-Nin_Zadar_County_Dalmatia.html"),
        ],
    },
    {
        "flyout_rank": 4,
        "slug": "villaggio-torre-ruffa-robinson",
        "name": "Villaggio Torre Ruffa Robinson",
        "town": "Capo Vaticano / Tropea coast",
        "town_slug": "capo-vaticano-tropea",
        "image": "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/07/27/8d/69/villaggio-torre-ruffa.jpg?w=1200&h=900&s=1",
        "image_credit": "Tripadvisor property photo",
        "signal": "Best southern Italy fit once direct Calabria flights are considered",
        "signal_class": "strong",
        "headline": "Best Italy transport-to-fit compromise if you still want an apartment with beach access.",
        "summary": (
            "Calabria rose because it solves more of the brief than Sicily does. Torre Ruffa is on the seafront, the apartments really do have "
            "fully equipped kitchenettes, the review signal is strong, and the Lamezia flight geometry looks easier than the Sicily option once "
            "you account for Aachen-to-Frankfurt timing."
        ),
        "why_it_works": [
            "The official rooms/aparthotel pages clearly separate rooms from apartments and residence-style options.",
            "Booking.com explicitly says the apartments include a fully equipped kitchenette and places the property directly on the seafront with mini club and entertainment.",
            "Tripadvisor returned live 2-room pricing for the 14-night sample and rated the property 4.5/5 from a very healthy review base.",
        ],
        "family_fit": [
            "Very good if you want an Italian coast option that is still functional rather than just scenic.",
            "This is less glamorous than Sicily, but more convincing on the actual apartment-plus-beach requirement.",
        ],
        "availability": [
            "Tripadvisor returned live sample-stay pricing from about USD 3,835 total for the 2-room search.",
            "Booking shows an active 2026 property page with apartments, private beach, and mini-club positioning; I did not verify the exact two-booking mix in the official engine.",
            f"Research snapshot date: {RESEARCH_DATE}. Window checked: {FLYOUT_WINDOW} ({FLYOUT_NIGHTS} nights).",
        ],
        "travel_fit": [
            "Frankfurt -> Lamezia direct service is active in the current 2026 schedule set, and route databases still show seasonal direct Lamezia -> Wrocław returns.",
            "This works better than Sicily because the transport signal is less dependent on a pre-dawn Frankfurt departure.",
            "The final road transfer to the Capo Vaticano/Tropea side still needs to be treated as roughly an hour, so it is simpler than Gargano but not instant.",
        ],
        "watchouts": [
            "The design feels more classic village resort than polished luxury resort.",
            "Recent complaints focus on dated rooms in some categories, tight beach spacing, and catering unevenness rather than on the coastline itself.",
        ],
        "window": FLYOUT_WINDOW,
        "nights": FLYOUT_NIGHTS,
        "sources": [
            ("Official rooms and apartments page", "https://villaggiorobinson.com/en/rooms/"),
            ("Official aparthotel page", "https://villaggiorobinson.com/camere/aparthotel-e-appartamenti/"),
            ("Booking.com review page", "https://www.booking.com/reviews/it/hotel/villaggio-torre-ruffa-robinson.html"),
            ("Tripadvisor listing", "https://www.tripadvisor.com/Hotel_Review-g1187099-d1100107-Reviews-Villaggio_Torre_Ruffa_Robinson-Torre_Ruffa_Province_of_Vibo_Valentia_Calabria.html"),
            ("FlightsFrom Frankfurt -> Lamezia", "https://www.flightsfrom.com/FRA-SUF"),
            ("FlightsFrom Lamezia -> Wrocław", "https://www.flightsfrom.com/SUF-WRO"),
        ],
    },
    {
        "flyout_rank": 5,
        "slug": "cap-esterel-holiday-village",
        "name": "Pierre & Vacances Cap Esterel Holiday Village",
        "town": "Agay / Estérel coast",
        "town_slug": "agay-esterel",
        "image": commons_file_url("AgayStRaphaël.JPG"),
        "image_credit": "Wikimedia Commons",
        "signal": "Best Southern France kids-machine, with very strong Nice route logic",
        "signal_class": "strong",
        "headline": "The most practical France add if pools, kids clubs, and scenery matter more than classic hotel polish.",
        "summary": (
            "Cap Esterel is the strongest France addition for young children because the product is designed as a full holiday village: "
            "apartments, pools, paid children's clubs, restaurants, sports, and the red-rock Estérel coastline above Agay Bay. It is "
            "less hotel-like than Senia or Sun Gardens, but the Nice flight geometry is clean and the day-to-day child logistics are strong."
        ),
        "why_it_works": [
            "Pierre & Vacances positions Cap Esterel as a large self-catering holiday village with apartment-style stays, restaurants, pools, sports, and children's clubs.",
            "The Agay / Estérel setting is one of the prettiest family-friendly stretches of the French Riviera, with red-rock scenery rather than generic resort sprawl.",
            "Nice Airport keeps transfers manageable, and the new Nice -> Wrocław direct route makes the open-jaw return much cleaner than many France ideas.",
        ],
        "family_fit": [
            "Very good if the children need easy pools, activities, and low-effort days more than a refined hotel corridor.",
            "Grandparents would need to be comfortable with a holiday-village rhythm; this is less elegant than a boutique hotel residence.",
        ],
        "availability": [
            "The official Pierre & Vacances booking footprint remains active for 2026, but I did not get the same direct two-room room-count proof as with the strongest Poland properties.",
            "Tripadvisor/Booking review depth is large enough to treat the property as a serious, bookable summer option rather than a marginal listing.",
            f"Research snapshot date: {RESEARCH_DATE}. Window checked: {FLYOUT_WINDOW} ({FLYOUT_NIGHTS} nights).",
        ],
        "travel_fit": [
            "Aachen -> Frankfurt plus Frankfurt -> Nice is the cleanest France outbound pattern because Lufthansa has frequent direct service and you can avoid pre-dawn rail if you choose a later flight.",
            "Nice -> Wrocław direct service is the key advantage over many French coast options; it keeps the return simple with kids and grandparents.",
            "Transfer from Nice Airport to Agay / Cap Esterel is roughly an hour by car in normal conditions, so this is materially easier than the deeper Gulf of Saint-Tropez options.",
        ],
        "watchouts": [
            "This is a holiday village, not a five-star hotel residence; reviews can sound mixed on maintenance, crowds, and uphill walking.",
            "The beach access is not as effortless as a hotel sitting directly on sand, so exact apartment location inside the village matters.",
        ],
        "window": FLYOUT_WINDOW,
        "nights": FLYOUT_NIGHTS,
        "sources": [
            ("Official Pierre & Vacances page", "https://www.pierreetvacances.com/gb-en/fp_SVL_self-catering-holiday-village-cap-esterel"),
            ("Children's clubs page", "https://www.pierreetvacances.com/gb-en/de_children-clubs"),
            ("Tripadvisor listing", "https://www.tripadvisor.com/Hotel_Review-g635814-d314427-Reviews-Village_Pierre_Vacances_Cap_Esterel-Agay_Saint_Raphael_French_Riviera_Cote_d_Azur.html"),
            ("Booking.com review page", "https://www.booking.com/reviews/fr/hotel/capesterel.fr.html"),
            ("Frankfurt -> Nice route", "https://www.flightsfrom.com/FRA-NCE"),
            ("Nice -> Wrocław route", "https://www.flightsfrom.com/NCE-WRO"),
        ],
    },
    {
        "flyout_rank": 6,
        "slug": "la-residence-du-bailli",
        "name": "La Résidence du Bailli",
        "town": "Rayol-Canadel / Gulf of Saint-Tropez",
        "town_slug": "rayol-canadel",
        "image": "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/06/24/77/9f/la-residence-du-bailli.jpg?w=1600&h=1000&s=1",
        "image_credit": "Tripadvisor property photo",
        "signal": "Best exact France apartment-plus-hotel-services shape",
        "signal_class": "strong",
        "headline": "The prettiest France apartment-residence lead, with direct sea access and hotel-domain services.",
        "summary": (
            "La Résidence du Bailli is the most on-brief France property shape I found: self-catering apartments in a preserved Gulf of "
            "Saint-Tropez cove, direct sea access, restaurants in season, and the ability to use services from the linked hotel domain. "
            "It is more serene and beautiful than child-programmed, so it ranks behind Cap Esterel for pure kids logistics."
        ),
        "why_it_works": [
            "Tripadvisor's hotel detail describes fully equipped seaside holiday apartments, direct access to the sea and beach, and three seasonal restaurants.",
            "Recent guest reviews specifically praise the well-equipped kitchen, proximity to the beach, and the option to use hotel services.",
            "Rayol-Canadel is one of the more beautiful and less overbuilt corners of the southern French coast, with gardens, coves, and the Îles d'Or views nearby.",
        ],
        "family_fit": [
            "Excellent for parents who want a real apartment, quiet evenings, and grandparents close by in the same small domain.",
            "Weaker than Zaton or Cap Esterel if the top priority is children's programming and weather-proof kid infrastructure.",
        ],
        "availability": [
            "Tripadvisor returned active 2-room pricing for the sample stay, from about USD 7,030 before taxes and fees, with Expedia/Hotels.com/Booking.com offers visible.",
            "The same Tripadvisor result rated the property 4.2/5 from 129 reviews and included recent April 2026 feedback.",
            f"Research snapshot date: {RESEARCH_DATE}. Window checked: {FLYOUT_WINDOW} ({FLYOUT_NIGHTS} nights).",
        ],
        "travel_fit": [
            "The Nice flight geometry is good, but Rayol-Canadel sits deeper into the Gulf of Saint-Tropez side than Agay, so the final transfer is the main penalty.",
            "This works best if the family is willing to pay for a private transfer and then stay mostly in place rather than move around daily.",
            "The return via Nice -> Wrocław direct is still much simpler than routing home through Paris or a multi-stop rail/flight combination.",
        ],
        "watchouts": [
            "This is not an all-singing kids-club resort; it is a beautiful seaside residence with services.",
            "Some reviews mention that pool access and service levels can be less seamless than the four-star framing suggests.",
        ],
        "window": FLYOUT_WINDOW,
        "nights": FLYOUT_NIGHTS,
        "sources": [
            ("Official residence page", "https://www.residence-lebaillidesuffren.com/en/"),
            ("Linked hotel domain", "https://www.domaine-lebaillidesuffren.com/en/"),
            ("Tripadvisor listing", "https://www.tripadvisor.com/Hotel_Review-g674121-d3340800-Reviews-La_Residence_du_Bailli-Rayol_Canadel_sur_Mer_French_Riviera_Cote_d_Azur_Provence_Alpes.html"),
            ("Booking.com review page", "https://www.booking.com/reviews/fr/hotel/la-ra-c-sidence-du-bailli.html"),
            ("Nice -> Wrocław route", "https://www.flightsfrom.com/NCE-WRO"),
        ],
    },
    {
        "flyout_rank": 7,
        "slug": "unahotels-naxos-beach-sicilia",
        "name": "UNAHOTELS Naxos Beach Sicilia",
        "town": "Giardini Naxos / Taormina edge",
        "town_slug": "giardini-naxos-taormina",
        "image": "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/1c/00/ba/1f/unahotels-naxos-beach.jpg?w=1600&h=1000&s=1",
        "image_credit": "Tripadvisor property photo",
        "signal": "Best Sicily beauty option, but the transport layer is less child-friendly",
        "signal_class": "strong",
        "headline": "The prettiest Italy lead if you are willing to accept tougher flight timing.",
        "summary": (
            "Naxos Beach makes the site because Sicily is genuinely more beautiful than a lot of northern-coast fallback ideas, and this resort is "
            "one of the few direct-beach family compounds that still reads credibly for young kids. The weakness is not the sea, the pools, or the "
            "children's programming. The weakness is the Frankfurt timing."
        ),
        "why_it_works": [
            "Tripadvisor describes a private beach, multiple pools, babysitting, children's entertainment, and villa-style accommodation inside the resort.",
            "Booking shows strong family sentiment, direct beach access, and a meaningful villa component rather than only standard rooms.",
            "Taormina, Etna, and the east-Sicily setting make this one of the strongest 'beautiful enough to fly' options in the entire study.",
        ],
        "family_fit": [
            "Good if the family wants a resort village with pools, private beach, and a real sense of place more than a perfect kitchenette-driven apartment.",
            "The room shape is less exact than Senia or Torre Ruffa, so I would treat Sicily as experience-first rather than layout-first.",
        ],
        "availability": [
            "Tripadvisor returned live sample-stay pricing from roughly USD 7,029 total for the 2-room search.",
            "Booking shows a heavy active review footprint and updated 2026 property pages, but I did not verify a grandparent-room pairing inside the official engine.",
            f"Research snapshot date: {RESEARCH_DATE}. Window checked: {FLYOUT_WINDOW} ({FLYOUT_NIGHTS} nights).",
        ],
        "travel_fit": [
            "The direct Frankfurt -> Catania Lufthansa pattern is the biggest problem: current flight data points to an early departure that makes same-day Aachen rail much less pleasant.",
            "Return-side geometry is better, because Catania stays inside Wrocław's southern-Europe seasonal network and the final transfer from CTA to Giardini Naxos is only around an hour.",
            "This becomes much more attractive if you are willing to sleep near Frankfurt the night before the outbound flight.",
        ],
        "watchouts": [
            "The room product looks more village-resort than premium residence, so do not oversell the apartment aspect.",
            "Breakfast and buffet comments are generally positive but can sound repetitive, and some room blocks feel more dated than the setting deserves.",
        ],
        "window": FLYOUT_WINDOW,
        "nights": FLYOUT_NIGHTS,
        "sources": [
            ("UNA family resort note", "https://www.gruppouna.it/it/newsroom/comunicati/early-booking"),
            ("Booking.com review page", "https://www.booking.com/reviews/it/hotel/atahotel-naxos-beach-resort.html"),
            ("Tripadvisor listing", "https://www.tripadvisor.com/Hotel_Review-g194774-d264464-Reviews-UNAHOTELS_Naxos_Beach_Sicilia-Giardini_Naxos_Province_of_Messina_Sicily.html"),
            ("Frankfurt -> Catania flight page", "https://www.flight.info/LH306"),
        ],
    },
]


FLYOUT_TOWNS = [
    {
        "slug": "punta-skala-petrcane",
        "name": "Punta Skala / Petrčane",
        "image": commons_file_url("Zadar, Croatia (Unsplash).jpg"),
        "headline": "Best foreign resort peninsula if you want premium apartments and very little day-to-day friction.",
        "summary": (
            "Punta Skala is less about town wandering and more about landing inside a very usable resort peninsula: sea views, private bays, "
            "sports, pools, and apartment living. That makes it one of the cleanest abroad upgrades over the Poland baseline."
        ),
        "best_for": [
            "Families who want a fly-out trip that still behaves predictably once they land.",
            "Trips where the resort itself matters more than being in the middle of a historic old town.",
        ],
        "watchouts": [
            "This is a peninsula-resort strategy, not a lively promenade-town strategy.",
            "The current route logic works best with a carefully chosen return day.",
        ],
        "travel_notes": [
            "Best route logic in the foreign pass: Frankfurt -> Zadar outbound, direct seasonal Zadar -> Wrocław return.",
            "Aachen rail into Frankfurt is workable on a normal morning, which is not true for every Italy option.",
        ],
        "maps_query": "Punta Skala Petrčane Croatia",
        "source_links": [
            ("Zadar tourism", "https://zadar.travel/"),
            ("Official resort", "https://www.falkensteiner.com/en/residences-senia"),
            ("Discover summer 2026 schedule", "https://www.discover-airlines.com/content/dam/four_y/pdfs/b2b/4y_summer-flight-schedule_2026.pdf"),
        ],
    },
    {
        "slug": "dubrovnik-riviera-orasac",
        "name": "Dubrovnik Riviera / Orašac",
        "image": commons_file_url("Dubrovnik Old Town 1.jpg"),
        "headline": "Best beauty-first Croatia base if you want a serious residence resort instead of a simple beach hotel.",
        "summary": (
            "This is the most photogenic foreign option in the pass. Orašac gives you sea views and resort calm, while Dubrovnik old town "
            "sits close enough for selective day trips instead of becoming the daily logistics burden."
        ),
        "best_for": [
            "Families who want one beautiful resort and a few high-value Dubrovnik outings rather than constant movement.",
            "Trips where the visual payoff really matters.",
        ],
        "watchouts": [
            "This is not a walk-to-old-town setup.",
            "The resort setting is gorgeous, but you need to actively choose the right outbound and return flight days.",
        ],
        "travel_notes": [
            "Frankfurt -> Dubrovnik is the strongest Croatia route on pure frequency, with daily summer service in Discover's 2026 schedule.",
            "The return side still works for Wrocław, but you should treat exact day and departure time as a final booking check rather than assume any date is equally nice.",
        ],
        "maps_query": "Orasac Dubrovnik Croatia",
        "source_links": [
            ("Visit Dubrovnik", "https://www.visitdubrovnik.hr/"),
            ("Sun Gardens Dubrovnik", "https://www.dubrovniksungardens.com/"),
            ("Discover summer 2026 schedule", "https://www.discover-airlines.com/content/dam/four_y/pdfs/b2b/4y_summer-flight-schedule_2026.pdf"),
        ],
    },
    {
        "slug": "zaton-nin",
        "name": "Zaton / Nin",
        "image": "https://www.zaton.hr/fileadmin/user_upload/2024/hero/zaton-holiday-resort-family-bay.jpg",
        "headline": "Best flat, sandy, little-kid Croatia base if the family wants easier beach days.",
        "summary": (
            "Zaton is more functional than romantic, but that matters with a 3-year-old and 6-year-old. Sandy beach, flat circulation, "
            "internal shops and activities, and near-zero need to improvise make it one of the best stress-reduction options abroad."
        ),
        "best_for": [
            "Families who want smoother beach logistics and fewer daily decisions.",
            "Trips where the children should be able to stay busy without constant driving.",
        ],
        "watchouts": [
            "You trade some charm and quiet for scale and crowding.",
            "The resort feeling is strong, but it is not the prettiest foreign option in the study.",
        ],
        "travel_notes": [
            "Shares the same Zadar airport geometry as Senia, but with an even simpler onward transfer.",
            "This is the easiest foreign option for younger kids if a sandy bay is a real plus.",
        ],
        "maps_query": "Zaton Holiday Resort Nin Croatia",
        "source_links": [
            ("Official resort", "https://www.zaton.hr/"),
            ("Nin tourism page", "https://www.nin.hr/en/accommodation/zaton-holiday-resort"),
            ("Zadar tourism", "https://zadar.travel/"),
        ],
    },
    {
        "slug": "giardini-naxos-taormina",
        "name": "Giardini Naxos / Taormina edge",
        "image": commons_file_url("Giardini Naxos at sunrise.JPG"),
        "headline": "Most beautiful Italy base in the pass, but with a real outbound-timing penalty.",
        "summary": (
            "This is the classic Sicily trade-off: huge scenic payoff, much richer day-trip value than a simple resort coast, and one of the "
            "better family compounds on the east side of the island. The transport layer is what keeps it from climbing higher."
        ),
        "best_for": [
            "Families who want beach plus iconic scenery plus easy Etna/Taormina optionality.",
            "Trips where a slightly more effortful outbound day is still worth it.",
        ],
        "watchouts": [
            "The direct Frankfurt -> Catania flight timing looks harsher than Croatia or Calabria.",
            "The best room categories read more like villas than true self-catering apartments.",
        ],
        "travel_notes": [
            "Return-side logic to Wrocław is workable through Catania's direct summer network, but the outbound from Frankfurt is early enough to be a real negative.",
            "This is the foreign option I would only take if beauty and Sicily itself are part of the goal, not just the hotel.",
        ],
        "maps_query": "Giardini Naxos Sicily Italy",
        "source_links": [
            ("Municipality", "https://www.comune.giardini-naxos.me.it/"),
            ("UNA family-resort note", "https://www.gruppouna.it/it/newsroom/comunicati/early-booking"),
            ("Lufthansa Frankfurt -> Catania flight page", "https://www.flight.info/LH306"),
        ],
    },
    {
        "slug": "capo-vaticano-tropea",
        "name": "Capo Vaticano / Tropea coast",
        "image": commons_file_url("CapoVaticano02.jpg"),
        "headline": "Best southern-Italy compromise between transport, beach beauty, and actual apartment usability.",
        "summary": (
            "Capo Vaticano and the Tropea side of Calabria do not have Sicily's fame, but the coastline is beautiful and the resort options "
            "can be more practical. In this pass Calabria scored as the strongest Italy answer once direct transport and apartment proof were weighted together."
        ),
        "best_for": [
            "Families who want Italy, but not at the price of a truly punishing outbound day.",
            "Trips where the beach and apartment matter more than the most famous sightseeing list.",
        ],
        "watchouts": [
            "The region feels lower-polish than Dubrovnik or some Sicily imagery suggests.",
            "You still need a transfer from Lamezia, even if it is manageable.",
        ],
        "travel_notes": [
            "Frankfurt -> Lamezia and Lamezia -> Wrocław direct seasonal logic makes Calabria materially easier than many other southern Italy ideas.",
            "This is the Italy destination where transport and family room shape finally start to line up.",
        ],
        "maps_query": "Capo Vaticano Calabria Italy",
        "source_links": [
            ("Calabria tourism", "https://calabriastraordinaria.it/en/"),
            ("Torre Ruffa Robinson", "https://villaggiorobinson.com/en/rooms/"),
            ("FlightsFrom Frankfurt -> Lamezia", "https://www.flightsfrom.com/FRA-SUF"),
            ("FlightsFrom Lamezia -> Wrocław", "https://www.flightsfrom.com/SUF-WRO"),
        ],
    },
    {
        "slug": "agay-esterel",
        "name": "Agay / Estérel coast",
        "image": commons_file_url("AgayStRaphaël.JPG"),
        "headline": "Best Southern France child-logistics base if you want pools, activities, and Riviera scenery.",
        "summary": (
            "Agay is the France option that makes the most sense with small kids: close enough to Nice Airport, framed by the red Estérel "
            "massif, and calmer than the showier Cannes/Saint-Tropez circuit. The trade-off is that the best property is a holiday village, not a classic hotel."
        ),
        "best_for": [
            "Families who want Southern France scenery without making every day depend on driving or sightseeing.",
            "Trips where children need pools, activities, and short beach outings more than white-glove hotel service.",
        ],
        "watchouts": [
            "The terrain can be hilly, so apartment location inside the village matters with a 3-year-old and grandparents.",
            "It is scenic and useful, but less polished than the highest-ranked Croatia residence resorts.",
        ],
        "travel_notes": [
            "Best France airport logic: Aachen rail to Frankfurt, direct Frankfurt -> Nice, then about an hour by car to Agay / Cap Esterel.",
            "The return is unusually clean for Southern France because Nice -> Wrocław direct service exists several times weekly.",
        ],
        "maps_query": "Agay Cap Esterel Saint Raphael France",
        "source_links": [
            ("Official Cap Esterel page", "https://www.pierreetvacances.com/gb-en/fp_SVL_self-catering-holiday-village-cap-esterel"),
            ("Saint-Raphaël tourism", "https://www.saint-raphael.com/en/"),
            ("Nice -> Wrocław route", "https://www.flightsfrom.com/NCE-WRO"),
        ],
    },
    {
        "slug": "rayol-canadel",
        "name": "Rayol-Canadel / Gulf of Saint-Tropez",
        "image": "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/07/d2/8d/57/la-residence-du-bailli.jpg?w=1600&h=1000&s=1",
        "headline": "Most beautiful Southern France residence idea, with direct sea access and quieter rhythm.",
        "summary": (
            "Rayol-Canadel is the elegant France counterpoint to Cap Esterel: more beautiful, quieter, and more apartment-residence shaped, "
            "but less programmed for kids. It is best if the family wants a protected cove, easy beach time, gardens, and a slower stay."
        ),
        "best_for": [
            "Families who want a real Mediterranean cove and apartment independence rather than a big resort machine.",
            "Trips where grandparents would prefer calm views, restaurants, and short walks over constant animation.",
        ],
        "watchouts": [
            "The transfer from Nice is longer than Agay, especially in summer traffic.",
            "Children's infrastructure is thinner than Cap Esterel, Zaton, or Sun Gardens.",
        ],
        "travel_notes": [
            "Uses the same strong Nice open-jaw logic, but the final transfer is the biggest weakness.",
            "This works best as a stay-put beach residence, not as a base for daily Côte d'Azur driving.",
        ],
        "maps_query": "Rayol Canadel sur Mer France",
        "source_links": [
            ("Official residence", "https://www.residence-lebaillidesuffren.com/en/"),
            ("Rayol-Canadel tourism", "https://www.visitvar.com/what-to-do/beaches/rayol-canadel-sur-mer"),
            ("Nice -> Wrocław route", "https://www.flightsfrom.com/NCE-WRO"),
        ],
    },
]


FLYOUT_TOWN_DETAILS = {
    "punta-skala-petrcane": {
        "family_spots": [
            ("Punta Skala peninsula", maps_search_url("Punta Skala Petrčane Croatia")),
            ("Petrčane waterfront", maps_search_url("Petrčane waterfront Croatia")),
            ("Zadar old town day trip", maps_search_url("Zadar old town Croatia")),
            ("Queen's Beach Nin", maps_search_url("Kraljičina Plaža Nin Croatia")),
        ],
        "gallery": [
            (
                commons_file_url("Zadar, Croatia (Unsplash).jpg"),
                "Zadar region waterfront mood",
                "Wikimedia Commons",
                commons_page_url("Zadar, Croatia (Unsplash).jpg"),
            ),
            (
                commons_file_url("Small beach in front of the University of Zadar, Croatia (48669896633).jpg"),
                "North Dalmatia beach look",
                "Wikimedia Commons",
                commons_page_url("Small beach in front of the University of Zadar, Croatia (48669896633).jpg"),
            ),
        ],
    },
    "dubrovnik-riviera-orasac": {
        "family_spots": [
            ("Sun Gardens beachfront", maps_search_url("Sun Gardens Dubrovnik beach")),
            ("Dubrovnik old town", maps_search_url("Old Town Dubrovnik")),
            ("Trsteno Arboretum", maps_search_url("Trsteno Arboretum")),
            ("Copacabana / Lapad beach", maps_search_url("Lapad Beach Dubrovnik")),
        ],
        "gallery": [
            (
                commons_file_url("Dubrovnik Old Town 1.jpg"),
                "Dubrovnik old town from above",
                "Wikimedia Commons",
                commons_page_url("Dubrovnik Old Town 1.jpg"),
            ),
            (
                commons_file_url("Old City, Dubrovnik.jpg"),
                "Dubrovnik old city waterfront",
                "Wikimedia Commons",
                commons_page_url("Old City, Dubrovnik.jpg"),
            ),
        ],
    },
    "zaton-nin": {
        "family_spots": [
            ("Zaton Holiday Resort", maps_search_url("Zaton Holiday Resort Croatia")),
            ("Queen's Beach Nin", maps_search_url("Kraljičina Plaža Nin Croatia")),
            ("Nin old town", maps_search_url("Nin old town Croatia")),
            ("Zadar old town", maps_search_url("Zadar old town Croatia")),
        ],
        "gallery": [
            (
                "https://www.zaton.hr/fileadmin/user_upload/2024/hero/zaton-holiday-resort-family-bay.jpg",
                "Zaton family beach bay",
                "Zaton Holiday Resort official image",
                "https://www.zaton.hr/",
            ),
            (
                commons_file_url("Zadar, Croatia (Unsplash).jpg"),
                "Zadar / Nin region atmosphere",
                "Wikimedia Commons",
                commons_page_url("Zadar, Croatia (Unsplash).jpg"),
            ),
        ],
    },
    "giardini-naxos-taormina": {
        "family_spots": [
            ("Giardini Naxos beach", maps_search_url("Giardini Naxos beach Sicily")),
            ("Taormina cable car", maps_search_url("Taormina cable car")),
            ("Isola Bella", maps_search_url("Isola Bella Taormina")),
            ("Mount Etna south side", maps_search_url("Rifugio Sapienza Etna")),
        ],
        "gallery": [
            (
                commons_file_url("Giardini Naxos at sunrise.JPG"),
                "Giardini Naxos sunrise",
                "Wikimedia Commons",
                commons_page_url("Giardini Naxos at sunrise.JPG"),
            ),
            (
                commons_file_url("Giardini-naxos beach, Messina, Sicily, Italy - panoramio.jpg"),
                "Giardini Naxos beach",
                "Wikimedia Commons",
                commons_page_url("Giardini-naxos beach, Messina, Sicily, Italy - panoramio.jpg"),
            ),
        ],
    },
    "capo-vaticano-tropea": {
        "family_spots": [
            ("Torre Ruffa beach", maps_search_url("Torre Ruffa beach Calabria")),
            ("Capo Vaticano viewpoint", maps_search_url("Capo Vaticano viewpoint")),
            ("Tropea old town", maps_search_url("Tropea old town")),
            ("Santa Maria beach", maps_search_url("Santa Maria beach Ricadi")),
        ],
        "gallery": [
            (
                commons_file_url("CapoVaticano02.jpg"),
                "Capo Vaticano beach",
                "Wikimedia Commons",
                commons_page_url("CapoVaticano02.jpg"),
            ),
            (
                commons_file_url("Beach in Tropea - Italy 2015.JPG"),
                "Tropea beach",
                "Wikimedia Commons",
                commons_page_url("Beach in Tropea - Italy 2015.JPG"),
            ),
        ],
    },
    "agay-esterel": {
        "family_spots": [
            ("Cap Esterel village", maps_search_url("Village Pierre Vacances Cap Esterel Agay")),
            ("Agay beach", maps_search_url("Plage d'Agay Saint Raphael")),
            ("Dramont beach", maps_search_url("Plage du Dramont Saint Raphael")),
            ("Saint-Raphaël waterfront", maps_search_url("Saint Raphael waterfront France")),
        ],
        "gallery": [
            (
                commons_file_url("AgayStRaphaël.JPG"),
                "Agay and the Estérel coastline",
                "Wikimedia Commons",
                commons_page_url("AgayStRaphaël.JPG"),
            ),
            (
                commons_file_url("AgayStRaphaël.JPG"),
                "Agay bay and Estérel coastline",
                "Wikimedia Commons",
                commons_page_url("AgayStRaphaël.JPG"),
            ),
        ],
    },
    "rayol-canadel": {
        "family_spots": [
            ("La Résidence du Bailli", maps_search_url("La Residence du Bailli Rayol Canadel")),
            ("Rayol beach", maps_search_url("Plage du Rayol Canadel")),
            ("Domaine du Rayol gardens", maps_search_url("Domaine du Rayol")),
            ("Le Lavandou harbor", maps_search_url("Le Lavandou harbor France")),
        ],
        "gallery": [
            (
                "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/07/d2/8d/57/la-residence-du-bailli.jpg?w=1600&h=1000&s=1",
                "Beach below La Résidence du Bailli",
                "Tripadvisor traveler photo",
                "https://www.tripadvisor.com/Hotel_Review-g674121-d3340800-Reviews-La_Residence_du_Bailli-Rayol_Canadel_sur_Mer_French_Riviera_Cote_d_Azur_Provence_Alpes.html",
            ),
            (
                "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/06/24/77/9f/la-residence-du-bailli.jpg?w=1600&h=1000&s=1",
                "Rayol residence and Mediterranean setting",
                "Tripadvisor property photo",
                "https://www.tripadvisor.com/Hotel_Review-g674121-d3340800-Reviews-La_Residence_du_Bailli-Rayol_Canadel_sur_Mer_French_Riviera_Cote_d_Azur_Provence_Alpes.html",
            ),
        ],
    },
}


FLYOUT_HOTEL_EXTERNALS = {
    "falkensteiner-residences-senia": {
        "maps": maps_search_url("Falkensteiner Residences Senia"),
        "booking_url": "https://www.booking.com/reviews/hr/hotel/falkensteiner-senia-apartments-zadar.en-gb.html",
        "booking_snapshot": "Booking.com: 8.7/10 from 283 reviews.",
        "booking_praise": [
            "Guests consistently praise the sea view, modern apartments, and genuinely useful kitchen equipment.",
            "The neighboring Falkensteiner resort stack, pools, and breakfast options make it feel easier than a standalone rental.",
        ],
        "booking_watch": [
            "Value for money is the main pushback, and Wi-Fi is weaker than the rest of the product.",
            "Some wellness access depends on the nearby hotel side and may come with extra cost.",
        ],
        "tripadvisor_url": "https://www.tripadvisor.com/Hotel_Review-g1182225-d7707770-Reviews-Falkensteiner_Residences_Senia-Petrcane_Zadar_County_Dalmatia.html",
        "tripadvisor_snapshot": "Tripadvisor: 4.4/5 from 101 reviews.",
        "tripadvisor_praise": [
            "Tripadvisor reviews praise huge, clean apartments, breakfast at Iadera, and the easy private-bay setting.",
            "Longer-stay guests explicitly describe cooking in the apartments and leaving more relaxed than they arrived.",
        ],
        "tripadvisor_watch": [
            "A 2025 review flagged construction noise in front of parts of the property.",
            "Operational extras and resort pricing remain the biggest friction points.",
        ],
    },
    "sun-gardens-dubrovnik": {
        "maps": maps_search_url("Sun Gardens Dubrovnik"),
        "booking_url": "https://www.booking.com/reviews/hr/hotel/radisson-blu-resort-spa-dubrovnik-riviera.en-gb.html",
        "booking_snapshot": "Booking.com: very large review footprint with residence-specific family stays and kitchenette-equipped units visible.",
        "booking_praise": [
            "Guests love the sea views, resort cleanliness, breakfast spread, and the space of the residence product.",
            "Booking snippets explicitly mention 2-bedroom residence categories and fully equipped kitchenettes, which is unusually helpful for this type of resort.",
        ],
        "booking_watch": [
            "The resort is physically large, so some guests dislike the walking and the distance from old town.",
            "A few recent reviews mention service inconsistency and the need to know which residence block you are booking.",
        ],
        "tripadvisor_url": "https://www.tripadvisor.com/Hotel_Review-g1943776-d1414005-Reviews-Sun_Gardens_Dubrovnik-Orasac_Dubrovnik_Dubrovnik_Neretva_County_Dalmatia.html",
        "tripadvisor_snapshot": "Tripadvisor: 4.4/5 from 3,042 reviews.",
        "tripadvisor_praise": [
            "Tripadvisor repeatedly praises the immaculate grounds, huge breakfast, kids enjoyment, and beautiful residence sea views.",
            "Recent reviews from April 2026 describe spacious one-bedroom residences and a very strong overall family stay.",
        ],
        "tripadvisor_watch": [
            "The biggest drawback is not the resort quality but the size and separation from Dubrovnik proper.",
            "A minority of guests still mention slippery pool areas and service that is not always at true top-tier level.",
        ],
    },
    "zaton-holiday-resort": {
        "maps": maps_search_url("Zaton Holiday Resort Croatia"),
        "booking_url": "https://www.booking.com/reviews/hr/hotel/zaton-holiday-village.html",
        "booking_snapshot": "Booking.com: very large apartment review footprint, with repeated family comments around the sandy beach and pool complex.",
        "booking_praise": [
            "Guests repeatedly call it a big, clean family resort with excellent child appeal and enough infrastructure to stay self-sufficient.",
            "The apartment product is described as practical and easy rather than glamorous.",
        ],
        "booking_watch": [
            "Peak-summer crowding, food pricing, and reception responsiveness are the recurring complaints.",
            "This is a scale play: very convenient with children, but not quiet.",
        ],
        "tripadvisor_url": "https://www.tripadvisor.com/Hotel_Review-g303820-d647873-Reviews-Zaton_Holiday_Resort-Nin_Zadar_County_Dalmatia.html",
        "tripadvisor_snapshot": "Tripadvisor: 3.9/5 from 3,710 reviews.",
        "tripadvisor_praise": [
            "Tripadvisor guests love the family atmosphere, pool and slide zones, long sandy beach, and broad activity stack.",
            "The strongest praise comes from families who want an all-in-one resort with very little friction.",
        ],
        "tripadvisor_watch": [
            "The most negative reviews are blunt about noise, crowds, paid loungers, and uneven buffet quality.",
            "This is a high-energy family machine, not a calm design resort.",
        ],
    },
    "villaggio-torre-ruffa-robinson": {
        "maps": maps_search_url("Villaggio Torre Ruffa Robinson"),
        "booking_url": "https://www.booking.com/reviews/it/hotel/villaggio-torre-ruffa-robinson.html",
        "booking_snapshot": "Booking.com: 8.7/10 from 70 reviews.",
        "booking_praise": [
            "Booking explicitly confirms seafront location, private beach, mini club, and apartments with fully equipped kitchenettes.",
            "Recent guests praise the food, cleanliness, layout, and the fact that it works especially well for families with children.",
        ],
        "booking_watch": [
            "The resort is more practical than luxurious, and room finish varies by category.",
            "Some guests mention dated details and tighter beach spacing than the marketing mood suggests.",
        ],
        "tripadvisor_url": "https://www.tripadvisor.com/Hotel_Review-g1187099-d1100107-Reviews-Villaggio_Torre_Ruffa_Robinson-Torre_Ruffa_Province_of_Vibo_Valentia_Calabria.html",
        "tripadvisor_snapshot": "Tripadvisor: 4.5/5 from 1,371 reviews.",
        "tripadvisor_praise": [
            "Tripadvisor guests repeatedly praise the sea, animation, food, and relaxed family atmosphere.",
            "Bungalows and apartments are described as clean and usable rather than merely decorative.",
        ],
        "tripadvisor_watch": [
            "Criticisms center on dated rooms in some categories and inconsistent food execution rather than on the location itself.",
            "This is not a polished luxury resort, so the pitch should stay grounded.",
        ],
    },
    "unahotels-naxos-beach-sicilia": {
        "maps": maps_search_url("UNAHOTELS Naxos Beach Sicilia"),
        "booking_url": "https://www.booking.com/reviews/it/hotel/atahotel-naxos-beach-resort.html",
        "booking_snapshot": "Booking.com: 8.5/10 from 1,896 reviews.",
        "booking_praise": [
            "Guests praise the direct sea access, large gardens, Olympic pool, and the family-ready feel of the resort.",
            "The property reads as a very good family resort village even when it is not a perfect apartment match.",
        ],
        "booking_watch": [
            "Breakfast can feel repetitive and noisy, and some room blocks feel dated.",
            "This is more resort-village than residence-luxury.",
        ],
        "tripadvisor_url": "https://www.tripadvisor.com/Hotel_Review-g194774-d264464-Reviews-UNAHOTELS_Naxos_Beach_Sicilia-Giardini_Naxos_Province_of_Messina_Sicily.html",
        "tripadvisor_snapshot": "Tripadvisor: 4.2/5 from 3,495 reviews.",
        "tripadvisor_praise": [
            "Tripadvisor guests repeatedly describe it as a strong family holiday with villas, entertainment, beach, and pools.",
            "The location under Etna and near Taormina adds much more destination value than a generic fly-and-flop resort.",
        ],
        "tripadvisor_watch": [
            "The room product is less polished than the setting, and some guests still describe it as dated for the rate level.",
            "The transport penalty remains the biggest reason it does not rank higher.",
        ],
    },
    "cap-esterel-holiday-village": {
        "maps": maps_search_url("Village Pierre Vacances Cap Esterel Agay"),
        "booking_url": "https://www.booking.com/reviews/fr/hotel/capesterel.fr.html",
        "booking_snapshot": "Booking.com: large review footprint for the Cap Esterel apartment village; scores are more practical than luxury.",
        "booking_praise": [
            "Guests like the views, pools, activity depth, and the fact that apartments make family days more self-sufficient.",
            "The strongest comments are from families who want a lot of on-site structure rather than a tiny boutique residence.",
        ],
        "booking_watch": [
            "Maintenance, crowds, parking, and uphill walking are recurring friction points.",
            "Apartment category and exact location inside the village matter more here than the brand name alone.",
        ],
        "tripadvisor_url": "https://www.tripadvisor.com/Hotel_Review-g635814-d314427-Reviews-Village_Pierre_Vacances_Cap_Esterel-Agay_Saint_Raphael_French_Riviera_Cote_d_Azur.html",
        "tripadvisor_snapshot": "Tripadvisor: broad mixed review footprint for a large family holiday village.",
        "tripadvisor_praise": [
            "Guests praise the scenery, sea views, pools, and activity stack for children.",
            "The property feels most successful when expectations are set around a lively self-catering village, not a polished hotel.",
        ],
        "tripadvisor_watch": [
            "Reviews are mixed on service, queueing, cleanliness, and the amount of walking.",
            "This is why it ranks as a useful France option, not as a top-three foreign lead.",
        ],
    },
    "la-residence-du-bailli": {
        "maps": maps_search_url("La Residence du Bailli Rayol Canadel"),
        "booking_url": "https://www.booking.com/reviews/fr/hotel/la-ra-c-sidence-du-bailli.html",
        "booking_snapshot": "Booking.com/OTA footprint shows active apartment inventory; Tripadvisor metasearch surfaced Booking.com offers for the sample stay.",
        "booking_praise": [
            "Guests praise the quiet cove, direct beach proximity, and the usefulness of apartment kitchens.",
            "The residence is repeatedly described as a calm, beautiful place rather than a generic serviced apartment block.",
        ],
        "booking_watch": [
            "Service expectations should stay modest: this is a residence with services, not a full luxury resort.",
            "Pool access and exact seasonal restaurant availability should be checked before paying.",
        ],
        "tripadvisor_url": "https://www.tripadvisor.com/Hotel_Review-g674121-d3340800-Reviews-La_Residence_du_Bailli-Rayol_Canadel_sur_Mer_French_Riviera_Cote_d_Azur_Provence_Alpes.html",
        "tripadvisor_snapshot": "Tripadvisor: 4.2/5 from 129 reviews; live sample-stay pricing surfaced from about USD 7,030 before taxes and fees.",
        "tripadvisor_praise": [
            "Recent guests praise the beach setting, well-equipped kitchens, cleanliness, gardens, and sea-facing calm.",
            "One review explicitly notes the ability to use services offered by the hotel, which is exactly the shape we were looking for.",
        ],
        "tripadvisor_watch": [
            "A minority of reviews call out service inconsistency and a residence feel that is simpler than four-star expectations.",
            "It is not the most kid-programmed option, so the children need to be happy with beach, pool, and low-key days.",
        ],
    },
}


VENICE_ROUTE_NOTES = [
    {
        "title": "The Venice route is real, but it uses two Venice airports",
        "body": (
            "Frankfurt -> Venice Marco Polo has direct Lufthansa service, while Venice Treviso -> Wrocław is the cleaner direct-return "
            "signal. That means the best bases need to work for both airport transfers, not just look close to Venice on a map."
        ),
        "links": [
            ("Frankfurt -> Venice route", "https://www.flightsfrom.com/FRA-VCE"),
            ("Lufthansa", "https://www.lufthansa.com/"),
            ("Treviso -> Wrocław route", "https://www.flightsfrom.com/TSF-WRO"),
            ("Ryanair", "https://www.ryanair.com/"),
        ],
    },
    {
        "title": "The family base should be a beach town, not Venice city",
        "body": (
            "For a 3-year-old, 6-year-old, parents, and grandparents, the best Venice-direction holiday is Cavallino, Jesolo, Bibione, "
            "or Chioggia/Sottomarina: beach first, apartment first, Venice as a selective day trip."
        ),
        "links": [
            ("Cavallino-Treporti tourism", "https://www.visitcavallino.com/en/"),
            ("Bibione tourism", "https://www.bibione.com/en/"),
            ("Jesolo tourism", "https://www.visitjesolo.it/en/"),
            ("Chioggia tourism", "https://www.chioggia.org/"),
        ],
    },
    {
        "title": "South of Venice was checked, but it is a backup lane",
        "body": (
            "Chioggia/Sottomarina gives the best southern angle because it has lagoon charm plus beach hotels. Isamar is a big kid-machine, "
            "but review quality is mixed; Mosella is much cleaner and more elegant, though less of a full resort."
        ),
        "links": [
            ("Mosella Suite Hotel", "https://www.mosellasuitehotel.it/en/"),
            ("Isaresidence", "https://www.isaresidence.com/en/"),
            ("Sottomarina map", maps_search_url("Sottomarina Chioggia beach Italy")),
        ],
    },
]


VENICE_DIRECTION_HOTELS = [
    {
        "venice_rank": 1,
        "slug": "junior-family-hotel-apartments",
        "name": "Junior Family Hotel & Apartments",
        "town": "Cavallino-Treporti",
        "town_slug": "cavallino-treporti",
        "image": "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/2b/56/2a/95/piscina-hotel.jpg?w=1600&h=1000&s=1",
        "image_credit": "Tripadvisor property photo",
        "signal": "Best exact Venice-direction room shape",
        "signal_class": "verified",
        "headline": "The cleanest near-Venice answer: apartments, hotel services, pool, and a very short beach walk.",
        "summary": (
            "Junior is the best Venice-direction fit because it is not just a nice beach hotel. It has a real apartment layer, strong family "
            "reviews, useful hotel services, and a location that keeps both Venice and the beach manageable. It is less glamorous than "
            "Falkensteiner Jesolo, but it solves the actual room-shape problem much better."
        ),
        "why_it_works": [
            "Tripadvisor returned a 4.7/5 profile from 435 reviews and live official-site availability for the June 27 to July 11 sample.",
            "Recent reviews specifically mention apartments, kitchen corners, two-bedroom layouts, terraces, and family-friendly beach logistics.",
            "The property sits in Cavallino-Treporti, which keeps Venice day-trip access possible without making Venice city the daily base.",
        ],
        "family_fit": [
            "Very strong for parents and kids in an apartment-style unit, with grandparents able to take a separate hotel or apartment room.",
            "Best for a quieter, smaller hotel rhythm rather than a giant holiday village with hundreds of moving parts.",
        ],
        "availability": [
            "Tripadvisor returned live sample-stay pricing from about USD 5,520 total for the 2-room search, with the official hotel site visible as the provider.",
            "This was the cleanest Venice-direction availability signal in the pass because it matched the apartment-plus-hotel brief rather than only a normal room search.",
            f"Research snapshot date: {RESEARCH_DATE}. Window checked: {FLYOUT_WINDOW} ({FLYOUT_NIGHTS} nights).",
        ],
        "travel_fit": [
            "Frankfurt -> Venice Marco Polo can work as the outbound; Cavallino is close enough that the arrival transfer is not the holiday's main event.",
            "Treviso -> Wrocław is the cleaner direct-return signal, and Cavallino remains reasonable for that return airport too.",
            "This is one of the few Italy ideas where the airport layer, beach layer, and apartment layer all point in the same direction.",
        ],
        "watchouts": [
            "The beach is close rather than fully inside a private resort bubble, so this is not a gated-resort answer.",
            "Exact apartment category matters: do not book a standard hotel room if the kitchenette/apartment shape is the reason to choose it.",
        ],
        "window": FLYOUT_WINDOW,
        "nights": FLYOUT_NIGHTS,
        "sources": [
            ("Official site", "https://www.junior-family.it/en/"),
            ("Booking.com search", booking_search_url("Junior Family Hotel Apartments Cavallino Treporti")),
            ("Tripadvisor listing", "https://www.tripadvisor.com/Hotel_Review-g194724-d653729-Reviews-Junior_Family_Hotel_Apartments-Cavallino_Treporti_Veneto.html"),
            ("Frankfurt -> Venice route", "https://www.flightsfrom.com/FRA-VCE"),
            ("Treviso -> Wrocław route", "https://www.flightsfrom.com/TSF-WRO"),
        ],
    },
    {
        "venice_rank": 2,
        "slug": "lino-delle-fate-bibione",
        "name": "Lino Delle Fate Eco Village Resort",
        "town": "Bibione",
        "town_slug": "bibione-venice-direction",
        "image": "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/28/fe/40/07/lino-delle-fate-eco-village.jpg?w=1600&h=1000&s=1",
        "image_credit": "Tripadvisor property photo",
        "signal": "Best apartment-resort product if the longer transfer is acceptable",
        "signal_class": "verified",
        "headline": "A real eco-village resort with bungalows, kitchens, pools, and an unusually strong family layout.",
        "summary": (
            "Lino delle Fate is probably the best pure accommodation product in the Venice direction: independent bungalows, apartment-style "
            "living, a car-light resort feel, pools, bike paths, and a beach/nature setting. It ranks just behind Junior because Bibione is "
            "farther from the Venice airports, but the stay itself is extremely close to the original brief."
        ),
        "why_it_works": [
            "The official site and Tripadvisor both describe independent bungalows/apartments rather than ordinary hotel rooms.",
            "Tripadvisor returned a 3.9/5 profile from 214 reviews and live sample-stay pricing, with Booking.com and Expedia-family offers visible.",
            "Guest comments repeatedly praise the pool area, quiet beach rhythm, spacious bungalows, and family structure.",
        ],
        "family_fit": [
            "Excellent for parents and kids who want their own apartment rhythm and enough kitchen independence to survive young-child mornings.",
            "Grandparents could either take a separate bungalow/unit or a more classic room category, depending on what the official engine exposes.",
        ],
        "availability": [
            "Tripadvisor returned live sample-stay pricing from about USD 7,589 total for the 2-room search, with multiple partners surfaced.",
            "The key follow-up before booking is exact unit pairing: one family bungalow/apartment plus a separate grandparents room or second unit.",
            f"Research snapshot date: {RESEARCH_DATE}. Window checked: {FLYOUT_WINDOW} ({FLYOUT_NIGHTS} nights).",
        ],
        "travel_fit": [
            "Bibione is farther from Venice Marco Polo and Treviso than Cavallino/Jesolo, so it only wins if the property quality is the reason for Italy.",
            "The airport geometry still works, but this is the Venice-direction option where I would pre-book a private transfer rather than improvise.",
            "The upside is that once you arrive, the day-to-day family logistics are stronger than many prettier but hotel-only Italy options.",
        ],
        "watchouts": [
            "Transfer length is the biggest negative compared with Cavallino and Jesolo.",
            "Some reviews mention crowding at breakfast/restaurant moments and variable service, so the bungalow product is more convincing than the dining layer.",
        ],
        "window": FLYOUT_WINDOW,
        "nights": FLYOUT_NIGHTS,
        "sources": [
            ("Official site", "https://www.linodellefateresort.com/eng/"),
            ("Booking.com search", booking_search_url("Lino Delle Fate Eco Village Resort Bibione")),
            ("Tripadvisor listing", "https://www.tripadvisor.com/Hotel_Review-g194691-d15208558-Reviews-Lino_Delle_Fate_Eco_Village_Resort-Bibione_San_Michele_Al_Tagliamento_Veneto.html"),
            ("Bibione tourism", "https://www.bibione.com/en/"),
        ],
    },
    {
        "venice_rank": 3,
        "slug": "villaggio-turistico-internazionale-bibione",
        "name": "Villaggio Turistico Internazionale",
        "town": "Bibione",
        "town_slug": "bibione-venice-direction",
        "image": "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/23/38/7d/a3/new-waterpark.jpg?w=1600&h=1000&s=1",
        "image_credit": "Tripadvisor property photo",
        "signal": "Best Bibione kid-machine with apartment inventory",
        "signal_class": "verified",
        "headline": "A big, direct-beach family village with waterpark energy, restaurants, and apartment/bungalow-style options.",
        "summary": (
            "VTI is the practical Bibione alternative to Lino delle Fate: less elegant, more energetic, and more obviously built for children. "
            "It belongs in the Venice direction because it combines private-beach logistics, pools/waterpark, sports, restaurants, and lodging "
            "that can work more like a family unit than a standard hotel corridor."
        ),
        "why_it_works": [
            "Tripadvisor returned a 4.4/5 profile from 1,167 reviews, with live June 27 to July 11 availability visible through major partners.",
            "The official site positions the property as a holiday village in Bibione with beach, restaurants, pools, and family infrastructure.",
            "Guest comments praise the clean family infrastructure, activities, food, and houses/apartments that feel equipped for longer stays.",
        ],
        "family_fit": [
            "Strong for children who need animation, pools, sports, and easy beach days.",
            "Grandparents need to be comfortable with a large holiday-village setting rather than a quiet boutique hotel.",
        ],
        "availability": [
            "Tripadvisor surfaced live partner offers for the sample stay, including Booking.com/Expedia-family channels and visible room counts on some offers.",
            "The exact price moved by provider and unit type, so treat this as available-but-needs-room-pairing rather than a final quote.",
            f"Research snapshot date: {RESEARCH_DATE}. Window checked: {FLYOUT_WINDOW} ({FLYOUT_NIGHTS} nights).",
        ],
        "travel_fit": [
            "Uses the same Venice airport logic as Lino delle Fate: feasible, but transfer planning matters more than with Cavallino/Jesolo.",
            "The reward for the longer transfer is a very self-contained kid holiday once you are there.",
            "This is a better fit if the family wants lively structure every day rather than calm design.",
        ],
        "watchouts": [
            "Scale and crowding are the predictable trade-offs.",
            "Extra costs for beach/services and mixed value comments appear in review summaries, so compare final package inclusions carefully.",
        ],
        "window": FLYOUT_WINDOW,
        "nights": FLYOUT_NIGHTS,
        "sources": [
            ("Official site", "https://www.vti.it/en/"),
            ("Booking.com search", booking_search_url("Villaggio Turistico Internazionale Bibione")),
            ("Tripadvisor listing", "https://www.tripadvisor.com/Hotel_Review-g194691-d1893321-Reviews-Villaggio_Turistico_Internazionale-Bibione_San_Michele_Al_Tagliamento_Veneto.html"),
            ("Bibione tourism", "https://www.bibione.com/en/"),
        ],
    },
    {
        "venice_rank": 4,
        "slug": "mosella-suite-hotel",
        "name": "Mosella Suite Hotel",
        "town": "Sottomarina / Chioggia",
        "town_slug": "sottomarina-chioggia",
        "image": "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/21/8f/12/de/mosella-suite-hotel.jpg?w=1600&h=1000&s=1",
        "image_credit": "Tripadvisor property photo",
        "signal": "Best south-of-Venice suite-hotel wildcard",
        "signal_class": "verified",
        "headline": "A polished suite hotel between lagoon and beach, more elegant than the big southern holiday villages.",
        "summary": (
            "Mosella is the most interesting south-of-Venice addition. It is not a giant kids resort, but it gives a more beautiful and compact "
            "suite-hotel answer near Chioggia/Sottomarina: lagoon views, beach access, pool, breakfast, bikes, restaurant context, and apartment-like "
            "reviews. This is the grown-up Venice-direction wildcard."
        ),
        "why_it_works": [
            "Tripadvisor returned a 4.8/5 profile from 223 reviews and live Booking.com/Vio sample-stay availability.",
            "Recent guest comments repeatedly mention spacious suites/apartments, modern rooms, breakfast, parking, bikes, pool, and the lagoon/beach position.",
            "Chioggia gives a real town and lagoon atmosphere rather than only a holiday-village strip.",
        ],
        "family_fit": [
            "Good if the adults want beauty, calm, and a proper town nearby, and the kids are happy with beach/pool rather than full animation.",
            "Less bulletproof than Junior or Lino for the kitchenette brief, so the exact suite category needs to be checked before it becomes a top pick.",
        ],
        "availability": [
            "Tripadvisor returned live sample-stay pricing from about USD 7,264 total for the 2-room search, with Booking.com availability visible.",
            "The best next step is to verify which family suite or apartment category gives the needed kitchen/micro-kitchen setup.",
            f"Research snapshot date: {RESEARCH_DATE}. Window checked: {FLYOUT_WINDOW} ({FLYOUT_NIGHTS} nights).",
        ],
        "travel_fit": [
            "Sottomarina is south of Venice and still workable from both Venice airports, though the final drive is less tidy than Jesolo/Cavallino.",
            "It becomes more attractive if you want Chioggia/lagoon atmosphere as part of the trip rather than only beach infrastructure.",
            "For young kids, the transfer is acceptable but should be private rather than stitched together with public transport.",
        ],
        "watchouts": [
            "This is not a classic kids-club resort, so it should not be chosen if daily child programming is essential.",
            "Kitchenette confidence is category-dependent; book only after confirming the exact suite layout.",
        ],
        "window": FLYOUT_WINDOW,
        "nights": FLYOUT_NIGHTS,
        "sources": [
            ("Official site", "https://www.mosellasuitehotel.it/en/"),
            ("Booking.com search", booking_search_url("Mosella Suite Hotel Sottomarina")),
            ("Tripadvisor listing", "https://www.tripadvisor.com/Hotel_Review-g194923-d17557020-Reviews-Mosella_Suite_Hotel-Sottomarina_Chioggia_Veneto.html"),
            ("Chioggia tourism", "https://www.chioggia.org/"),
        ],
    },
    {
        "venice_rank": 5,
        "slug": "falkensteiner-hotel-spa-jesolo",
        "name": "Falkensteiner Hotel & Spa Jesolo",
        "town": "Lido di Jesolo",
        "town_slug": "lido-di-jesolo",
        "image": "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/1d/69/10/b6/falkensteiner-hotel-spa.jpg?w=1600&h=1000&s=1",
        "image_credit": "Tripadvisor property photo",
        "signal": "Most beautiful premium hotel, weaker on apartment shape",
        "signal_class": "strong",
        "headline": "The premium direct-beach option near Venice if hotel quality beats kitchenette certainty.",
        "summary": (
            "Falkensteiner Jesolo is the Venice-direction beauty play: direct beach, stylish pools, spa, strong breakfast, kids club, and very easy "
            "airport geography. It ranks lower only because the apartment/kitchenette proof is weaker than Junior, Lino, VTI, or Mosella."
        ),
        "why_it_works": [
            "Tripadvisor returned a 4.3/5 profile from 646 reviews and live sample-stay availability with major OTAs.",
            "The property description emphasizes a family-friendly five-star beach hotel with pools, spa, kids club, restaurants, and direct Adriatic setting.",
            "Jesolo is one of the simplest Venice-direction bases for airport transfers and beach logistics.",
        ],
        "family_fit": [
            "Strong if grandparents want a polished hotel and the parents are willing to compromise on kitchenette/apartment independence.",
            "Best as a premium hotel fallback, not as the most exact room-shape answer.",
        ],
        "availability": [
            "Tripadvisor returned live sample-stay pricing from about USD 16,599 total for the 2-room search, with many rooms remaining on Expedia/Hotels.com.",
            "Booking.com also surfaced availability in the metasearch feed, including refundable/breakfast-included messaging.",
            f"Research snapshot date: {RESEARCH_DATE}. Window checked: {FLYOUT_WINDOW} ({FLYOUT_NIGHTS} nights).",
        ],
        "travel_fit": [
            "Jesolo is one of the easiest beach bases from Venice Marco Polo and still manageable for Treviso return to Wrocław.",
            "This is the least stressful Venice-direction airport transfer among the premium hotel ideas.",
            "The flight geometry is a strong reason to keep it on the list even though the room shape is less perfect.",
        ],
        "watchouts": [
            "Very expensive in the sample window compared with the apartment-first options.",
            "Review summaries praise beach/pools/spa but also flag value, parking/drinks, and occasional service inconsistency.",
        ],
        "window": FLYOUT_WINDOW,
        "nights": FLYOUT_NIGHTS,
        "sources": [
            ("Official site", "https://www.falkensteiner.com/en/hotel-spa-jesolo"),
            ("Booking.com search", booking_search_url("Falkensteiner Hotel Spa Jesolo")),
            ("Tripadvisor listing", "https://www.tripadvisor.com/Hotel_Review-g580246-d7179326-Reviews-Falkensteiner_Hotel_Spa_Jesolo-Jesolo_Veneto.html"),
            ("Jesolo tourism", "https://www.visitjesolo.it/en/"),
        ],
    },
    {
        "venice_rank": 6,
        "slug": "isaresidence-isamar-chioggia",
        "name": "Isaresidence / Isamar Holiday Village",
        "town": "Isola Verde / Chioggia",
        "town_slug": "sottomarina-chioggia",
        "image": "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/11/3e/7d/87/view-water-park.jpg?w=1600&h=1000&s=1",
        "image_credit": "Tripadvisor property photo",
        "signal": "Big south-of-Venice kid-machine, but review quality is mixed",
        "signal_class": "strong",
        "headline": "A huge beach-and-waterpark village south of Venice, useful but less elegant and less review-clean.",
        "summary": (
            "Isamar/Isaresidence is worth keeping because it is exactly the kind of large family complex that can make young-child days easy: "
            "beach, waterpark, pools, entertainment, restaurants, bungalows, mobile homes, and apartments. It ranks last in the Venice direction "
            "because the review signal is much messier than the top five."
        ),
        "why_it_works": [
            "Tripadvisor describes a large holiday park south of the Venetian lagoon with private beach, waterpark, bars, restaurants, sports, entertainment, and apartments/bungalows.",
            "The official Isaresidence site keeps the apartment-residence angle visible for the same Isamar ecosystem.",
            "Recent guest comments praise the waterpark, beach, pools, supermarket, and child activity depth.",
        ],
        "family_fit": [
            "Strong if children need a full-scale activity village and adults accept a less refined setting.",
            "Grandparents should be checked carefully against the exact accommodation location inside the complex because scale can become friction.",
        ],
        "availability": [
            "Tripadvisor did not return a live price in the sample metasearch feed, so this remains a backup that needs direct official-engine confirmation.",
            "The property itself is active and heavily reviewed, but it should not outrank hotels with cleaner June 27 to July 11 availability evidence.",
            f"Research snapshot date: {RESEARCH_DATE}. Window checked: {FLYOUT_WINDOW} ({FLYOUT_NIGHTS} nights).",
        ],
        "travel_fit": [
            "This is the most explicitly south-of-Venice family village in the pass, but transfer simplicity is weaker than Jesolo/Cavallino.",
            "It is viable if the family wants a stay-put waterpark village, not if the goal is frequent Venice outings.",
            "I would only book it with a private transfer and a very specific accommodation location inside the village.",
        ],
        "watchouts": [
            "Tripadvisor score is only 3.4/5 from a large review base, with complaints around cleanliness, organization, costs, and room variability.",
            "The sea/beach setting is practical, but not as beautiful as the stronger Croatia, France, or Bibione leads.",
        ],
        "window": FLYOUT_WINDOW,
        "nights": FLYOUT_NIGHTS,
        "sources": [
            ("Official Isaresidence site", "https://www.isaresidence.com/en/"),
            ("Booking.com search", booking_search_url("Isamar Holiday Village Chioggia")),
            ("Tripadvisor listing", "https://www.tripadvisor.com/Hotel_Review-g1186877-d237883-Reviews-Isamar_Holiday_Village-Isola_Verde_Chioggia_Veneto.html"),
            ("Chioggia tourism", "https://www.chioggia.org/"),
        ],
    },
]


VENICE_DIRECTION_TOWNS = [
    {
        "slug": "cavallino-treporti",
        "name": "Cavallino-Treporti",
        "image": commons_file_url("Panorama of wonderful European beach at Cavallino.jpg"),
        "headline": "Best near-Venice beach strip for apartment stays, Venice day trips, and manageable airport transfers.",
        "summary": (
            "Cavallino-Treporti is the sweet spot for the Venice direction: family beach town first, lagoon/Venice access second, and close "
            "enough to both Venice airports to avoid a punishing transfer day."
        ),
        "best_for": [
            "Families who want a beach base that still allows a selective Venice or lagoon outing.",
            "Trips where a smaller apartment-hotel rhythm is more attractive than a giant waterpark village.",
        ],
        "watchouts": [
            "Some accommodation is spread along a long coastal strip, so exact walking distance to beach and restaurants matters.",
            "The best properties are not in Venice itself; this is a beach-town strategy.",
        ],
        "travel_notes": [
            "Best Venice-direction transfer logic among the apartment-first options.",
            "Works for Frankfurt -> Venice Marco Polo outbound and Treviso -> Wrocław return without putting the family too far east or south.",
        ],
        "maps_query": "Cavallino-Treporti Italy",
        "source_links": [
            ("Cavallino-Treporti tourism", "https://www.visitcavallino.com/en/"),
            ("Junior Family Hotel & Apartments", "https://www.junior-family.it/en/"),
            ("Frankfurt -> Venice route", "https://www.flightsfrom.com/FRA-VCE"),
            ("Treviso -> Wrocław route", "https://www.flightsfrom.com/TSF-WRO"),
        ],
    },
    {
        "slug": "bibione-venice-direction",
        "name": "Bibione",
        "image": commons_file_url("Bibione spiaggia.jpg"),
        "headline": "Best apartment-resort depth in the Venice direction, at the cost of a longer airport transfer.",
        "summary": (
            "Bibione is farther from the airports, but it has the strongest concentration of family-resort apartment products in this Venice "
            "pass. It is the place to choose if the stay itself matters more than shaving 25 minutes off the transfer."
        ),
        "best_for": [
            "Families who want resort-apartment depth, pools, bungalows, bike paths, and very low daily friction.",
            "Trips where the property quality is the reason to choose Italy over Poland.",
        ],
        "watchouts": [
            "Transfers from Venice airports are materially longer than Cavallino or Jesolo.",
            "The town is a classic holiday resort town, so charm is beach-family practicality rather than old-world Venice atmosphere.",
        ],
        "travel_notes": [
            "Feasible from both Venice airports, but this is where a private transfer becomes the sane default.",
            "Ranks highly only because the accommodation fit is unusually strong.",
        ],
        "maps_query": "Bibione Italy",
        "source_links": [
            ("Bibione tourism", "https://www.bibione.com/en/"),
            ("Lino Delle Fate", "https://www.linodellefateresort.com/eng/"),
            ("Villaggio Turistico Internazionale", "https://www.vti.it/en/"),
        ],
    },
    {
        "slug": "lido-di-jesolo",
        "name": "Lido di Jesolo",
        "image": commons_file_url("Lido di Jesolo 1.jpg"),
        "headline": "Best premium-hotel beach base near Venice, but less convincing for kitchenette apartments.",
        "summary": (
            "Jesolo is the easiest classic beach resort base from Venice Marco Polo: direct beach hotels, promenades, restaurants, family "
            "attractions, and quick transfers. It only scores down because the best hotel found is hotel-first, not apartment-first."
        ),
        "best_for": [
            "Families who want polished beach-hotel services and the shortest Venice-direction transfer.",
            "Grandparents who would prefer classic hotel comfort over a bungalow village.",
        ],
        "watchouts": [
            "Apartment-with-kitchen evidence is weaker in the premium hotel layer.",
            "Peak-season Jesolo can feel busy and urban compared with Bibione's resort-village products.",
        ],
        "travel_notes": [
            "Strongest pure airport convenience in the Venice direction.",
            "Use this town if the family decides premium hotel comfort matters more than self-catering certainty.",
        ],
        "maps_query": "Lido di Jesolo Italy",
        "source_links": [
            ("Jesolo tourism", "https://www.visitjesolo.it/en/"),
            ("Falkensteiner Jesolo", "https://www.falkensteiner.com/en/hotel-spa-jesolo"),
            ("Frankfurt -> Venice route", "https://www.flightsfrom.com/FRA-VCE"),
        ],
    },
    {
        "slug": "sottomarina-chioggia",
        "name": "Sottomarina / Chioggia",
        "image": commons_file_url("Sottomarina Chioggia.jpg"),
        "headline": "Best south-of-Venice angle: lagoon town charm plus beach, but weaker resort certainty.",
        "summary": (
            "Chioggia/Sottomarina is the useful southern counterweight to Jesolo and Bibione. It gives a real lagoon town, beach access, and "
            "some interesting suite/residence products, but it is less obviously built around the exact apartment-hotel-with-kids brief."
        ),
        "best_for": [
            "Families who want a prettier, more local Venice-lagoon feel and are comfortable with a calmer beach rhythm.",
            "Trips where adults value Chioggia, harbor views, and restaurants as much as kid programming.",
        ],
        "watchouts": [
            "The strongest exact family-resort product is not as clean as Cavallino or Bibione.",
            "Large holiday villages here can be very practical but have mixed review quality.",
        ],
        "travel_notes": [
            "South of Venice is viable, but it is less transfer-efficient than Jesolo or Cavallino.",
            "Best handled with a private transfer and a stay-put plan rather than repeated Venice outings.",
        ],
        "maps_query": "Sottomarina Chioggia Italy",
        "source_links": [
            ("Chioggia tourism", "https://www.chioggia.org/"),
            ("Mosella Suite Hotel", "https://www.mosellasuitehotel.it/en/"),
            ("Isaresidence", "https://www.isaresidence.com/en/"),
        ],
    },
]


VENICE_DIRECTION_TOWN_DETAILS = {
    "cavallino-treporti": {
        "family_spots": [
            ("Junior Family Hotel & Apartments", maps_search_url("Junior Family Hotel Apartments Cavallino Treporti")),
            ("Cavallino beach", maps_search_url("Cavallino-Treporti beach")),
            ("Punta Sabbioni ferry to Venice", maps_search_url("Punta Sabbioni ferry Venice")),
            ("Lio Piccolo lagoon outing", maps_search_url("Lio Piccolo Cavallino Treporti")),
        ],
        "gallery": [
            (
                commons_file_url("Panorama of wonderful European beach at Cavallino.jpg"),
                "Cavallino beach panorama",
                "Wikimedia Commons",
                commons_page_url("Panorama of wonderful European beach at Cavallino.jpg"),
            ),
            (
                commons_file_url("Cavallino banner.jpg"),
                "Cavallino-Treporti coastal read",
                "Wikimedia Commons",
                commons_page_url("Cavallino banner.jpg"),
            ),
        ],
    },
    "bibione-venice-direction": {
        "family_spots": [
            ("Lino Delle Fate", maps_search_url("Lino Delle Fate Eco Village Resort Bibione")),
            ("Villaggio Turistico Internazionale", maps_search_url("Villaggio Turistico Internazionale Bibione")),
            ("Bibione beach", maps_search_url("Bibione beach")),
            ("Bibione lighthouse", maps_search_url("Bibione lighthouse")),
        ],
        "gallery": [
            (
                commons_file_url("Bibione spiaggia.jpg"),
                "Bibione beach",
                "Wikimedia Commons",
                commons_page_url("Bibione spiaggia.jpg"),
            ),
            (
                commons_file_url("Bibione Faro.jpg"),
                "Bibione lighthouse",
                "Wikimedia Commons",
                commons_page_url("Bibione Faro.jpg"),
            ),
        ],
    },
    "lido-di-jesolo": {
        "family_spots": [
            ("Falkensteiner Jesolo", maps_search_url("Falkensteiner Hotel Spa Jesolo")),
            ("Lido di Jesolo beach", maps_search_url("Lido di Jesolo beach")),
            ("Caribe Bay waterpark", maps_search_url("Caribe Bay Jesolo")),
            ("Jesolo promenade", maps_search_url("Lido di Jesolo promenade")),
        ],
        "gallery": [
            (
                commons_file_url("Lido di Jesolo 1.jpg"),
                "Lido di Jesolo beachfront",
                "Wikimedia Commons",
                commons_page_url("Lido di Jesolo 1.jpg"),
            ),
            (
                commons_file_url("Jesolo Beach View.jpg"),
                "Jesolo beach view",
                "Wikimedia Commons",
                commons_page_url("Jesolo Beach View.jpg"),
            ),
        ],
    },
    "sottomarina-chioggia": {
        "family_spots": [
            ("Mosella Suite Hotel", maps_search_url("Mosella Suite Hotel Sottomarina")),
            ("Isaresidence / Isamar", maps_search_url("Isaresidence Isamar Holiday Village Chioggia")),
            ("Sottomarina beach", maps_search_url("Sottomarina beach")),
            ("Chioggia old town", maps_search_url("Chioggia old town")),
        ],
        "gallery": [
            (
                commons_file_url("Sottomarina Chioggia.jpg"),
                "Sottomarina and Chioggia",
                "Wikimedia Commons",
                commons_page_url("Sottomarina Chioggia.jpg"),
            ),
            (
                commons_file_url("Spiaggia sottomarina.JPG"),
                "Sottomarina beach",
                "Wikimedia Commons",
                commons_page_url("Spiaggia sottomarina.JPG"),
            ),
        ],
    },
}


VENICE_DIRECTION_HOTEL_EXTERNALS = {
    "junior-family-hotel-apartments": {
        "maps": maps_search_url("Junior Family Hotel Apartments Cavallino Treporti"),
        "booking_url": booking_search_url("Junior Family Hotel Apartments Cavallino Treporti"),
        "booking_snapshot": "Booking.com/OTA search: active apartment-hotel footprint; final room-category pairing should be checked directly before booking.",
        "booking_praise": [
            "The listing ecosystem supports the hotel-plus-apartments positioning rather than only standard rooms.",
            "The low-friction Cavallino location is the main reason this leads the Venice direction.",
        ],
        "booking_watch": [
            "Use Booking.com mainly as a cross-check; the clearest sample-stay provider surfaced through Tripadvisor was the official hotel site.",
            "Exact kitchen/kitchenette details are category-dependent.",
        ],
        "tripadvisor_url": "https://www.tripadvisor.com/Hotel_Review-g194724-d653729-Reviews-Junior_Family_Hotel_Apartments-Cavallino_Treporti_Veneto.html",
        "tripadvisor_snapshot": "Tripadvisor: 4.7/5 from 435 reviews; live sample pricing from about USD 5,520 via official hotel site.",
        "tripadvisor_praise": [
            "Guests repeatedly praise the friendly staff, cleanliness, beach proximity, pool, and relaxed family atmosphere.",
            "Recent apartment reviews mention kitchen corners, larger layouts, terraces, and easy beach/restaurants nearby.",
        ],
        "tripadvisor_watch": [
            "The beach is a short walk rather than a full private-resort bubble.",
            "Apartment type matters; avoid booking a normal hotel room if self-catering is the point.",
        ],
    },
    "lino-delle-fate-bibione": {
        "maps": maps_search_url("Lino Delle Fate Eco Village Resort Bibione"),
        "booking_url": booking_search_url("Lino Delle Fate Eco Village Resort Bibione"),
        "booking_snapshot": "Booking.com/OTA footprint: active summer listing signal for an eco-village resort with apartment and bungalow categories.",
        "booking_praise": [
            "The strongest appeal is the independent bungalow/apartment setup with kitchen equipment and child-friendly outdoor space.",
            "The product reads much more like a self-contained family stay than a standard hotel room.",
        ],
        "booking_watch": [
            "The exact family-plus-grandparents pairing needs direct confirmation because the best unit mix may be two separate bungalows/units.",
            "Dining comments are less consistently positive than the accommodation/pool comments.",
        ],
        "tripadvisor_url": "https://www.tripadvisor.com/Hotel_Review-g194691-d15208558-Reviews-Lino_Delle_Fate_Eco_Village_Resort-Bibione_San_Michele_Al_Tagliamento_Veneto.html",
        "tripadvisor_snapshot": "Tripadvisor: 3.9/5 from 214 reviews; live sample pricing surfaced from about USD 7,589.",
        "tripadvisor_praise": [
            "Guests praise the clean resort feel, pools, spacious bungalows, quiet beach rhythm, and child-friendly layout.",
            "The resort's nature setting and car-light layout are repeatedly more convincing than a normal beach hotel.",
        ],
        "tripadvisor_watch": [
            "Some guests mention crowded breakfast/restaurant moments and service inconsistency.",
            "Transfer time from Venice airports is the biggest strategic negative.",
        ],
    },
    "villaggio-turistico-internazionale-bibione": {
        "maps": maps_search_url("Villaggio Turistico Internazionale Bibione"),
        "booking_url": booking_search_url("Villaggio Turistico Internazionale Bibione"),
        "booking_snapshot": "Booking.com/OTA footprint: active partner availability surfaced in Tripadvisor's sample-stay feed.",
        "booking_praise": [
            "Guests like the scale of the family infrastructure: pools, beach, sports, activities, restaurants, and apartment/bungalow-style stays.",
            "The village is especially strong if the children need structure every day.",
        ],
        "booking_watch": [
            "Peak-season value and extra-cost details should be compared carefully.",
            "This is a lively village, not a quiet design resort.",
        ],
        "tripadvisor_url": "https://www.tripadvisor.com/Hotel_Review-g194691-d1893321-Reviews-Villaggio_Turistico_Internazionale-Bibione_San_Michele_Al_Tagliamento_Veneto.html",
        "tripadvisor_snapshot": "Tripadvisor: 4.4/5 from 1,167 reviews; sample-stay OTA offers were visible.",
        "tripadvisor_praise": [
            "Guests praise the beachfront setting, cleanliness, activities, waterpark/pool zones, and friendly service.",
            "Recent comments describe houses/accommodation as equipped for a real family stay.",
        ],
        "tripadvisor_watch": [
            "Value-for-money and extra costs appear as recurring cautions.",
            "Crowds are the predictable price of choosing a high-infrastructure family village.",
        ],
    },
    "mosella-suite-hotel": {
        "maps": maps_search_url("Mosella Suite Hotel Sottomarina"),
        "booking_url": booking_search_url("Mosella Suite Hotel Sottomarina"),
        "booking_snapshot": "Booking.com surfaced in Tripadvisor metasearch for the sample stay, with breakfast-included availability.",
        "booking_praise": [
            "The hotel/residence shape is much more polished than the big south-of-Venice holiday villages.",
            "The lagoon-plus-beach location gives adults a stronger sense of place than many resort strips.",
        ],
        "booking_watch": [
            "Confirm the exact suite category before treating it as a kitchenette apartment.",
            "This is not a kids-club resort, so do not choose it for daily animation.",
        ],
        "tripadvisor_url": "https://www.tripadvisor.com/Hotel_Review-g194923-d17557020-Reviews-Mosella_Suite_Hotel-Sottomarina_Chioggia_Veneto.html",
        "tripadvisor_snapshot": "Tripadvisor: 4.8/5 from 223 reviews; live sample pricing from about USD 7,264.",
        "tripadvisor_praise": [
            "Guests repeatedly praise spacious suites/apartments, modern design, breakfast, parking, staff, and lagoon/beach position.",
            "Recent comments make it feel like a credible suite-hotel rather than a generic beach block.",
        ],
        "tripadvisor_watch": [
            "Kitchenette evidence is less standardized than Junior or Lino.",
            "Child programming is light compared with Bibione/Cavallino holiday villages.",
        ],
    },
    "falkensteiner-hotel-spa-jesolo": {
        "maps": maps_search_url("Falkensteiner Hotel Spa Jesolo"),
        "booking_url": booking_search_url("Falkensteiner Hotel Spa Jesolo"),
        "booking_snapshot": "Booking.com/OTA footprint: live sample-stay availability surfaced through Tripadvisor, with breakfast/free-cancellation messaging visible.",
        "booking_praise": [
            "The premium beach-hotel product is clearly active and easy to book.",
            "It is one of the strongest Venice-direction options for grandparents who prefer classic hotel comfort.",
        ],
        "booking_watch": [
            "Price is very high and apartment/kitchenette evidence is weak.",
            "This should be booked as a hotel choice, not as a self-catering solution.",
        ],
        "tripadvisor_url": "https://www.tripadvisor.com/Hotel_Review-g580246-d7179326-Reviews-Falkensteiner_Hotel_Spa_Jesolo-Jesolo_Veneto.html",
        "tripadvisor_snapshot": "Tripadvisor: 4.3/5 from 646 reviews; live sample pricing from about USD 16,599.",
        "tripadvisor_praise": [
            "Guests praise the direct beach, modern rooms, pools, spa, breakfast, and family-friendly feel.",
            "Jesolo's transfer logic is one of the easiest in the Venice pass.",
        ],
        "tripadvisor_watch": [
            "Common complaints center on value, paid extras, parking/drink costs, and occasional service inconsistency.",
            "It is weaker than the leaders on the apartment/kitchenette brief.",
        ],
    },
    "isaresidence-isamar-chioggia": {
        "maps": maps_search_url("Isaresidence Isamar Holiday Village Chioggia"),
        "booking_url": booking_search_url("Isamar Holiday Village Chioggia"),
        "booking_snapshot": "Booking.com/OTA search: active property ecosystem, but Tripadvisor did not return live sample-stay pricing.",
        "booking_praise": [
            "The appeal is all-in family infrastructure: waterpark, beach, pools, sports, restaurants, shops, and apartment/mobile-home inventory.",
            "This is the most child-programmed south-of-Venice backup.",
        ],
        "booking_watch": [
            "Do not treat it as availability-verified until the official engine confirms the exact dates and unit pairing.",
            "Accommodation location inside the complex matters for grandparents and small children.",
        ],
        "tripadvisor_url": "https://www.tripadvisor.com/Hotel_Review-g1186877-d237883-Reviews-Isamar_Holiday_Village-Isola_Verde_Chioggia_Veneto.html",
        "tripadvisor_snapshot": "Tripadvisor: 3.4/5 from 2,103 reviews; no live price returned in the sample metasearch feed.",
        "tripadvisor_praise": [
            "Guests praise the waterpark, kids club, private beach, activities, supermarket, and family scale.",
            "The strongest reviews come from families who want a big stay-put holiday village.",
        ],
        "tripadvisor_watch": [
            "Cleanliness, organization, service, costs, and room variability appear often enough to keep it below the leaders.",
            "It is practical rather than beautiful.",
        ],
    },
}


FLYOUT_SHORTLIST = sorted(FLYOUT_HOTELS, key=lambda hotel: hotel["flyout_rank"])
VENICE_DIRECTION_SHORTLIST = sorted(VENICE_DIRECTION_HOTELS, key=lambda hotel: hotel["venice_rank"])
ALL_HOTELS = HOTELS + FLYOUT_HOTELS + VENICE_DIRECTION_HOTELS
ALL_TOWNS = TOWNS + FLYOUT_TOWNS + VENICE_DIRECTION_TOWNS
ALL_TOWN_DETAILS = {**TOWN_DETAILS, **FLYOUT_TOWN_DETAILS, **VENICE_DIRECTION_TOWN_DETAILS}
ALL_HOTEL_EXTERNALS = {**HOTEL_EXTERNALS, **FLYOUT_HOTEL_EXTERNALS, **VENICE_DIRECTION_HOTEL_EXTERNALS}

HOTELS_BY_TOWN = {}
for hotel in ALL_HOTELS:
    HOTELS_BY_TOWN.setdefault(hotel["town_slug"], []).append(hotel)


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

    h1 { font-size: clamp(1.8rem, 3.05vw, 2.55rem); margin-top: 0.72rem; }
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
        font-size: clamp(1.8rem, 9vw, 2.45rem);
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


def hotel_rank_value(hotel: dict) -> int:
    return hotel.get("rank", hotel.get("flyout_rank", hotel.get("venice_rank", 0)))


def hotel_rank_badge(hotel: dict) -> str:
    return str(hotel_rank_value(hotel))


def hotel_rank_text(hotel: dict) -> str:
    if "rank" in hotel:
        return f"Poland #{hotel['rank']}"
    if "flyout_rank" in hotel:
        return f"Fly-out #{hotel['flyout_rank']}"
    return f"Venice #{hotel['venice_rank']}"


def hotel_window(hotel: dict) -> str:
    return hotel.get("window", STAY_WINDOW)


def hotel_nights(hotel: dict) -> int:
    return hotel.get("nights", STAY_NIGHTS)


def hotel_track(hotel: dict) -> str:
    if "rank" in hotel:
        return "Poland baseline"
    if "flyout_rank" in hotel:
        return "Fly-out shortlist"
    return "Venice direction"


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
          <meta name="description" content="Family beach study across Poland, Croatia, Italy, France, and the Venice direction, screened for apartment-friendly resort stays and child-manageable travel.">
          <link rel="stylesheet" href="{prefix}assets/styles.css">
        </head>
        <body>
          <header class="topbar">
            <div class="wrapper topbar-inner">
              <a class="brand" href="{prefix}index.html">
                <span class="brand-mark">FC</span>
                <span>Family Coast Summer Study</span>
              </a>
              <nav class="nav">
                <a href="{prefix}index.html#flyout">Fly-Outs</a>
                <a href="{prefix}index.html#venice-direction">Venice</a>
                <a href="{prefix}index.html#shortlist">Top Picks</a>
                <a href="{prefix}index.html#ranking">Poland Rank</a>
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
    towns_by_slug = {town["slug"]: town for town in ALL_TOWNS}

    flyout_cards = []
    for hotel in FLYOUT_SHORTLIST:
        hotel_page = hotel_link(hotel)
        town = towns_by_slug[hotel["town_slug"]]
        town_page = town_link(town)
        flyout_cards.append(
            f"""
            <article class="hotel-card">
              {render_image(hotel["image"], hotel["name"], hotel["name"], href=hotel_page)}
              <div class="hotel-card-body">
                <div class="card-topline">
                  <span class="rank">{hotel_rank_badge(hotel)}</span>
                  <span class="signal {hotel["signal_class"]}">{escape(hotel["signal"])}</span>
                </div>
                <div>
                  <h3>{escape(hotel["name"])}</h3>
                  <p class="muted" style="margin-top:0.35rem;">{escape(hotel["town"])}</p>
                </div>
                <p>{escape(hotel["headline"])}</p>
                <p class="dense-copy">{escape(hotel["travel_fit"][0])}</p>
                <p class="dense-copy">{escape(hotel_window(hotel))} | {hotel_nights(hotel)} nights</p>
                <div class="hero-actions" style="margin-top:0;">
                  <a class="button secondary small" href="{hotel_page}">Hotel report</a>
                  <a class="button secondary small" href="{town_page}">Town page</a>
                </div>
              </div>
            </article>
            """
        )

    route_cards = []
    for note in FLYOUT_ROUTE_NOTES:
        route_cards.append(
            f"""
            <article class="note-card">
              <strong>{escape(note["title"])}</strong>
              <p>{escape(note["body"])}</p>
              {render_link_chips(note["links"])}
            </article>
            """
        )

    venice_cards = []
    for hotel in VENICE_DIRECTION_SHORTLIST:
        hotel_page = hotel_link(hotel)
        town = towns_by_slug[hotel["town_slug"]]
        town_page = town_link(town)
        venice_cards.append(
            f"""
            <article class="hotel-card">
              {render_image(hotel["image"], hotel["name"], hotel["name"], href=hotel_page)}
              <div class="hotel-card-body">
                <div class="card-topline">
                  <span class="rank">{hotel_rank_badge(hotel)}</span>
                  <span class="signal {hotel["signal_class"]}">{escape(hotel["signal"])}</span>
                </div>
                <div>
                  <h3>{escape(hotel["name"])}</h3>
                  <p class="muted" style="margin-top:0.35rem;">{escape(hotel["town"])}</p>
                </div>
                <p>{escape(hotel["headline"])}</p>
                <p class="dense-copy">{escape(hotel["travel_fit"][0])}</p>
                <p class="dense-copy">{escape(hotel_window(hotel))} | {hotel_nights(hotel)} nights</p>
                <div class="hero-actions" style="margin-top:0;">
                  <a class="button secondary small" href="{hotel_page}">Hotel report</a>
                  <a class="button secondary small" href="{town_page}">Town page</a>
                </div>
              </div>
            </article>
            """
        )

    venice_note_cards = []
    for note in VENICE_ROUTE_NOTES:
        venice_note_cards.append(
            f"""
            <article class="note-card">
              <strong>{escape(note["title"])}</strong>
              <p>{escape(note["body"])}</p>
              {render_link_chips(note["links"])}
            </article>
            """
        )

    shortlist_cards = []
    for hotel in SHORTLIST:
        hotel_page = hotel_link(hotel)
        town_page = town_link(towns_by_slug[hotel["town_slug"]])
        shortlist_cards.append(
            f"""
            <article class="hotel-card">
              {render_image(hotel["image"], hotel["name"], hotel["name"], href=hotel_page)}
              <div class="hotel-card-body">
                <div class="card-topline">
                  <span class="rank">{hotel_rank_badge(hotel)}</span>
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
                  <span class="rank">{hotel_rank_badge(hotel)}</span>
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
    for town in ALL_TOWNS:
        linked_hotels = sorted(HOTELS_BY_TOWN.get(town["slug"], []), key=hotel_rank_value)
        if linked_hotels:
            hotel_labels = ", ".join(hotel["name"] for hotel in linked_hotels[:3])
            if len(linked_hotels) > 3:
                hotel_labels += f", +{len(linked_hotels) - 3} more"
        else:
            hotel_labels = "No linked hotel yet"
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
                <p class="dense-copy">{len(linked_hotels)} linked stay option(s): {escape(hotel_labels)}</p>
                <a class="button secondary small" href="{town_page}">Town page</a>
              </div>
            </article>
            """
        )

    hero_ranked_links = " ".join(
        f'<a href="{hotel_link(hotel)}">{hotel["flyout_rank"]}. {escape(hotel["name"])}</a>'
        for hotel in FLYOUT_SHORTLIST
    )

    venice_ranked_links = " ".join(
        f'<a href="{hotel_link(hotel)}">{hotel["venice_rank"]}. {escape(hotel["name"])}</a>'
        for hotel in VENICE_DIRECTION_SHORTLIST[:5]
    )

    poland_ranked_links = " ".join(
        f'<a href="{hotel_link(hotel)}">{hotel["rank"]}. {escape(hotel["name"])}</a>'
        for hotel in HOTELS[:6]
    )

    html = f"""
    <main>
      <section class="hero">
        <div class="wrapper hero-grid">
          <div class="hero-copy">
            <span class="eyebrow">Family Vacation Study</span>
            <h1>Best Family Coast Fits</h1>
            <p class="lede">
              Poland baseline plus Croatia, France, and a new Venice-direction pass, screened for child-manageable flights,
              beach access, and resort-linked apartment options.
            </p>
            <div class="meta-row">
              <span class="pill">{escape(RESEARCH_DATE)} research snapshot</span>
              <span class="pill">Fly-out window: {escape(FLYOUT_WINDOW)}</span>
              <span class="pill">Poland baseline: {escape(STAY_WINDOW)}</span>
            </div>
            <div class="hero-actions">
              <a class="button" href="#flyout">Fly-out shortlist</a>
              <a class="button secondary" href="#venice-direction">Venice direction</a>
              <a class="button secondary" href="#shortlist">Poland baseline</a>
            </div>
          </div>
          <div class="hero-card">
            {render_image("https://dynamic-media-cdn.tripadvisor.com/media/photo-o/1c/2b/a5/bb/outdoor-pool.jpg?w=1600&h=1000&s=1", "Croatia fly-out resort view", "Fly-Out Coast", "hero-image")}
            <div class="hero-card-body">
              <span class="eyebrow">Fly-out order</span>
              <h3 style="margin-top:0.65rem;">Current abroad leaders</h3>
              <p class="dense-copy ranking-links" style="margin-top:0.75rem;">
                {hero_ranked_links}
              </p>
              <p class="dense-copy ranking-links" style="margin-top:0.7rem;">
                Venice lane: {venice_ranked_links}
              </p>
            </div>
          </div>
        </div>
      </section>

      <section class="section" id="flyout">
        <div class="wrapper">
          <div class="section-header">
            <div>
              <span class="eyebrow">Fly-Out Shortlist</span>
              <h2>Best Croatia, Italy + France Options</h2>
            </div>
            <p class="section-note">14-night screen for June 27, 2026 to July 11, 2026, assuming Aachen rail to Frankfurt and a Wrocław return.</p>
          </div>
          <div class="grid grid-3">
            {"".join(route_cards)}
          </div>
          <div class="grid grid-2" style="margin-top:1rem;">
            {"".join(flyout_cards)}
          </div>
        </div>
      </section>

      <section class="section" id="venice-direction">
        <div class="wrapper">
          <div class="section-header">
            <div>
              <span class="eyebrow">Venice Direction</span>
              <h2>Near-Venice Family Resorts</h2>
            </div>
            <p class="section-note">Separate screen for Frankfurt -> Venice outbound plus a Treviso -> Wrocław return, with Cavallino, Bibione, Jesolo, and Chioggia checked.</p>
          </div>
          <div class="grid grid-3">
            {"".join(venice_note_cards)}
          </div>
          <div class="grid grid-2" style="margin-top:1rem;">
            {"".join(venice_cards)}
          </div>
        </div>
      </section>

      <section class="section" id="shortlist">
        <div class="wrapper">
          <div class="section-header">
            <div>
              <span class="eyebrow">Poland Baseline</span>
              <h2>Best No-Flight Bets</h2>
            </div>
            <p class="section-note">27-night benchmark for the same family room shape, kept as the domestic baseline.</p>
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
              <h2>Full Poland Hotel Ranking</h2>
            </div>
            <p class="section-note">Ordered by fit, beach convenience, and room shape inside the Poland-only baseline.</p>
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
              <h2>Poland Fit Matrix</h2>
            </div>
            <p class="section-note">Fastest read for the no-flight baseline before opening the full reports.</p>
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
            <p class="section-note">Poland, Croatia, and Italy destination pages with map pins, town photos, and linked hotel reports.</p>
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
            <h2 style="margin-top:0.8rem;">Original Poland Inputs</h2>
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
              <strong>Strongest fly-out fit</strong>
              <p>Falkensteiner Senia is the cleanest abroad answer, with Sun Gardens as the beauty-first premium alternative and Zaton as the easiest little-kid machine.</p>
            </article>
            <article class="note-card">
              <strong>Best no-flight fit</strong>
              <p>Linea Mare, Rosevia, and Saltic Grzybowo remain the domestic anchors because they combine the room shape best with the strongest July proof.</p>
            </article>
            <article class="note-card">
              <strong>Main caveat</strong>
              <p>Every availability statement here is a snapshot from {escape(RESEARCH_DATE)}. Exact outbound and return days still matter, especially for the foreign open-jaw flights.</p>
            </article>
          </div>
        </div>
      </section>
    </main>
    """
    (SITE / "index.html").write_text(layout("Family Coast Summer Study", html), encoding="utf-8")


def build_hotel_pages() -> None:
    towns_by_slug = {town["slug"]: town for town in ALL_TOWNS}
    for hotel in ALL_HOTELS:
        town = towns_by_slug[hotel["town_slug"]]
        external = ALL_HOTEL_EXTERNALS[hotel["slug"]]
        if "rank" in hotel:
            index_anchor = "ranking"
            back_label = "Back to Poland ranking"
        elif "flyout_rank" in hotel:
            index_anchor = "flyout"
            back_label = "Back to fly-out shortlist"
        else:
            index_anchor = "venice-direction"
            back_label = "Back to Venice direction"
        town_travel_block = ""
        if town.get("travel_notes"):
            town_travel_block = (
                '<div class="source-card" style="margin-top:1rem;">'
                "<strong>Travel notes</strong>"
                f'{render_points(town["travel_notes"])}'
                "</div>"
            )
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
            <a class="back-link" href="../index.html#{index_anchor}">{back_label}</a>
            <div class="page-grid">
              <section class="hero-copy">
                <span class="eyebrow">Hotel Report</span>
                <h1>{escape(hotel["name"])}</h1>
                <p class="lede">{escape(hotel["headline"])}</p>
                <div class="pill-row">
                  <span class="signal {hotel["signal_class"]}">{escape(hotel["signal"])}</span>
                  <span class="pill">{escape(hotel_rank_text(hotel))}</span>
                  <span class="pill">{escape(hotel["town"])}</span>
                </div>
                <div class="stat-band">
                  <div class="stat"><span>Research snapshot</span><strong>{escape(RESEARCH_DATE)}</strong></div>
                  <div class="stat"><span>Window checked</span><strong>{escape(hotel_window(hotel))}</strong></div>
                  <div class="stat"><span>Study track</span><strong>{escape(hotel_track(hotel))}</strong></div>
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
                  <strong>Travel fit</strong>
                  {render_points(hotel.get("travel_fit", ["No flight screen needed. This property belongs to the Poland baseline."]))}
                </div>
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
                {town_travel_block}
                <div class="hero-actions" style="margin-top:1rem;">
                  <a class="button secondary small" href="../index.html#{index_anchor}">{back_label}</a>
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
    for town in ALL_TOWNS:
        hotels = sorted(HOTELS_BY_TOWN.get(town["slug"], []), key=hotel_rank_value)
        detail = ALL_TOWN_DETAILS[town["slug"]]
        town_map = maps_search_url(town.get("maps_query", f"{town['name']} Poland"))
        travel_panel = ""
        if town.get("travel_notes"):
            travel_panel = (
                '<article class="panel">'
                '<span class="eyebrow">Travel</span>'
                '<h2 style="margin-top:0.8rem;">Route Notes</h2>'
                f'{render_points(town["travel_notes"])}'
                "</article>"
            )
        quick_links = [("Google Maps", town_map)] + town["source_links"]
        hotel_cards = []
        for hotel in hotels:
            hotel_cards.append(
                f"""
                <article class="source-card">
                  <strong>{escape(hotel_rank_text(hotel))}: {escape(hotel["name"])}</strong>
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

            {travel_panel}

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
