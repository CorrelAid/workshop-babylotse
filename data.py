import html

import pandas as pd
from stadteile_utils import stadtteil_mapping_func, stadtteil_region_mapping

final_categories = [
    "Public Accessibility and Transportation",
    "Childcare and Early Education Resources",
    "Family and Community Support Services",
    "Family-Friendly Amenities and Facilities",
    "Family Activities and Community Programs",
    "Parks, Playgrounds, and Green Spaces",
    "Healthcare Access, Services, and Facilities",
    "Safety, Cleanliness, and Facility Maintenance",
    "Community Social and Networking Opportunities",
    "Service Information and Resource Availability",
    "Housing Affordability and Availability",
    "Bureaucratic Processes and Delays",
    "Mental Health and Well-being",
]

final_categories_de = [
    "Transport und Barrierefreiheit",
    "Kinderbetreuung",
    "Soziale Unterstützung (Babylotse, Beratungsstellen usw.)",
    "Familienfreundlichkeit in der Öffentlichkeit",
    "Aktivitäten für Familien",
    "Parks, Spielplätze und Grünflächen",
    "Zugang zur Gesundheitsversorgung",
    "Sicherheit und Sauberkeit",
    "Soziale Netzwerke für Familien",
    "Zugang zu Informationen für Familien",
    "Wohnraum",
    "Bürokratie",
    "Psychische Gesundheit und Wohlbefinden",
]

category_mapping = dict(zip(final_categories, final_categories_de))

def load_data(file: str) -> pd.DataFrame:
    df = pd.read_csv(
        "./data/" + file,
        parse_dates=["Date Created"],
        usecols=[
            "Date Created",
            "Ich wohne im Stadtteil",
            "Das gefällt mir gut mit Baby in Frankfurt",
            "Das gefällt mir nicht gut mit Baby in Frankfurt",
        ],
    )
    df.columns = ["Date", "Stadtteil", "Positive", "Negative"]
    df.iloc[:, 1:] = df.iloc[:, 1:].map(html.unescape)
    df.iloc[:, 1:] = df.iloc[:, 1:].map(str.strip)
    df = df.replace(r"\r\r\n", ".", regex=True)
    df["Stadtteil"] = df["Stadtteil"].fillna("")
    df["Stadtteil"] = df["Stadtteil"].apply(stadtteil_mapping_func)
    df["Region"] = df["Stadtteil"].apply(stadtteil_region_mapping)

    return df
