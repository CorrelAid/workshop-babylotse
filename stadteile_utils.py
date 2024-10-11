from functools import lru_cache

import geopandas as gpd

merge_stadtteile = {
    "Sachsenhausen-Nord": "Sachsenhausen",
    "Sachsenhausen-Süd": "Sachsenhausen",
    "Nordend-West": "Nordend",
    "Nordend-Ost": "Nordend",
    "Westend-Süd": "Westend",
    "Westend-Nord": "Westend",
}

merge_regions = {
    "Berkersheim": "Nord",
    "Bonames": "Nord",
    "Dornbusch": "Nord",
    "Eckenheim": "Nord",
    "Eschersheim": "Nord",
    "Frankfurter Berg": "Nord",
    "Ginnheim": "Nord",
    "Harheim": "Nord",
    "Heddernheim": "Nord",
    "Kalbach-Riedberg": "Nord",
    "Nieder-Erlenbach": "Nord",
    "Nieder-Eschbach": "Nord",
    "Niederursel": "Nord",
    "Preungesheim": "Nord",
    "Praunheim": "Nord",
    "Altstadt": "Mitte",
    "Gutleut-/Bahnhofsviertel": "Mitte",
    "Bockenheim": "Mitte",
    "Gallus": "Mitte",
    "Gutleutviertel": "Mitte",
    "Hausen": "Mitte",
    "Innenstadt": "Mitte",
    "Nordend": "Mitte",
    "Rödelheim": "Mitte",
    "Westend": "Mitte",
    "Bergen-Enkheim": "Ost",
    "Bornheim": "Ost",
    "Fechenheim": "Ost",
    "Ostend": "Ost",
    "Riederwald": "Ost",
    "Seckbach": "Ost",
    "Griesheim": "West",
    "Höchst": "West",
    "Nied": "West",
    "Schwanheim": "West",
    "Sindlingen": "West",
    "Sossenheim": "West",
    "Unterliederbach": "West",
    "Zeilsheim": "West",
    "Niederrad": "Süd",
    "Oberrad": "Süd",
    "Sachsenhausen": "Süd",
    "Umland": "Umland"
    
}


def get_stadtteile_gdf():
    stadtteile_gdf = gpd.read_file("data/ffmstadtteilewahlen.geojson")
    stadtteile_gdf["STTLNAME"] = stadtteile_gdf["STTLNAME"].replace(merge_stadtteile)
    stadtteile_gdf = stadtteile_gdf.dissolve("STTLNAME").reset_index()
    return stadtteile_gdf


@lru_cache
def create_stadtteil_mapping() -> dict[str, str]:
    stadtteile_gdf = get_stadtteile_gdf()

    stadtteil_mapping = {
        k: v
        for k, v in zip(
            stadtteile_gdf["STTLNAME"].str.lower(), stadtteile_gdf["STTLNAME"]
        )
    }

    stadtteil_mapping["sachsenhausen"] = "Sachsenhausen"
    stadtteil_mapping["nordend-west"] = "Nordend"
    stadtteil_mapping["enkheim"] = "Bergen-Enkheim"
    stadtteil_mapping["bergen enkheim"] = "Bergen-Enkheim"
    stadtteil_mapping["bergen"] = "Bergen-Enkheim"
    stadtteil_mapping["alt-eschersheim"] = "Eschersheim"
    stadtteil_mapping["riedberg"] = "Kalbach-Riedberg"
    stadtteil_mapping["riedberg uni campus"] = "Kalbach-Riedberg"
    stadtteil_mapping["riedber"] = "Kalbach-Riedberg"
    stadtteil_mapping["frankfurt höchst"] = "Höchst"
    stadtteil_mapping["bockenheim-rebstock"] = "Bockenheim"
    stadtteil_mapping["bockenheim - city west"] = "Bockenheim"
    stadtteil_mapping["niederrae"] = "Niederrad"
    stadtteil_mapping["schwanheim goldstein"] = "Schwanheim"
    stadtteil_mapping["westend süd"] = "Westend"
    stadtteil_mapping["innerstadt 1"] = "Innenstadt"
    stadtteil_mapping["frankfurt am main rödelheim"] = "Rödelheim"
    stadtteil_mapping["niederursel/ nordweststadt"] = "Niederursel"
    stadtteil_mapping["nordwes"] = "Niederursel"
    stadtteil_mapping["europaviertel"] = "Gallus"
    stadtteil_mapping["europa-viertel"] = "Gallus"
    stadtteil_mapping["rebstock"] = "Bockenheim"
    stadtteil_mapping["goldstein"] = "Schwanheim"
    stadtteil_mapping["bahnhofviertel"] = "Gutleut-/Bahnhofsviertel"
    stadtteil_mapping["gutleut"] = "Gutleut-/Bahnhofsviertel"
    stadtteil_mapping["gutleutviertel"] = "Gutleut-/Bahnhofsviertel"
    stadtteil_mapping["niedereschbach"] = "Nieder-Eschbach"
    stadtteil_mapping["römerstadt"] = "Heddernheim"
    stadtteil_mapping["60388"] = "Bergen-Enkheim"
    stadtteil_mapping["europa allee"] = "Gallus"
    stadtteil_mapping["frankfurt-nied"] = "Nied"
    stadtteil_mapping["nordend-ost "] = "Nordend"
    stadtteil_mapping["kalbach"] = "Kalbach-Riedberg"
    stadtteil_mapping["rebstockpark"] = "Bockenheim"
    stadtteil_mapping["goldstein schwanheim "] = "Schwanheim"
    stadtteil_mapping["Mertonviertel"] = "Heddernheim"
    stadtteil_mapping["nordend ost"] = "Nordend"
    stadtteil_mapping["preungesheim-frankfurter bogen"] = (
        "Preungesheim-Frankfurter Bogen"
    )
    stadtteil_mapping["sachsenhausen süd"] = "Sachsenhausen"
    stadtteil_mapping["nordend west "] = "Nordend"
    stadtteil_mapping["nordend west"] = "Nordend"
    stadtteil_mapping["friedberg"] = "Umland"
    stadtteil_mapping["rebstockviertel, bockenheim"] = "Bockenheim"
    stadtteil_mapping["ostend / gutleut"] = "Gutleut-/Bahnhofsviertel"
    stadtteil_mapping["altstadr"] = "Altstadt"
    stadtteil_mapping["hockenheim"] = "Bockenheim"
    stadtteil_mapping["stadtmitte"] = "Innenstadt"
    stadtteil_mapping["norden"] = "Nordend"
    stadtteil_mapping["nordweststadt"] = "Niederursel"
    stadtteil_mapping["nordend-ost"] = "Nordend"
    stadtteil_mapping["goldstein schwanheim"] = "Schwanheim"
    stadtteil_mapping["mertonviertel"] = "Heddernheim"
    stadtteil_mapping["praunheim/heddernheim"] = "Praunheim"
    stadtteil_mapping["bornheim mitte"] = "Bornheim"
    stadtteil_mapping["nordend/dornbusch"] = "Dornbusch"
    stadtteil_mapping["bockenheim rebstockbad"] = "Bockenheim"
    stadtteil_mapping["ostend/bornheim  grenzgebiet"] = "Bornheim"
    stadtteil_mapping["frankfurt mitte"] = "Innenstadt"
    stadtteil_mapping["sachenhausen"] = "Sachsenhausen"
    stadtteil_mapping["nordwestzentrum"] = "Heddernheim"
    stadtteil_mapping["west"] = "Westend"
    stadtteil_mapping["bocken"] = "Bockenheim"
    stadtteil_mapping["preungesheim-frankfurter bogen"] = "Preungesheim"

    # UMLAND
    stadtteil_mapping["neu-isenburg"] = "Umland"
    stadtteil_mapping["dreieich"] = "Umland"
    stadtteil_mapping["bad homburg"] = "Umland"
    stadtteil_mapping["bad vilbel"] = "Umland"
    stadtteil_mapping["butzbach"] = "Umland"
    stadtteil_mapping["montabaur"] = "Umland"
    stadtteil_mapping["ober-erlenbach"] = "Umland"
    stadtteil_mapping["offenbach"] = "Umland"
    stadtteil_mapping["flörsheim"] = "Umland"
    stadtteil_mapping["hattersheim"] = "Umland"
    stadtteil_mapping["kelkheim"] = "Umland"
    stadtteil_mapping["langenselbold"] = "Umland"
    stadtteil_mapping["mörfelden"] = "Umland"
    stadtteil_mapping["maintal"] = "Umland"
    stadtteil_mapping["mainz"] = "Umland"
    stadtteil_mapping["hofheim"] = "Umland"
    stadtteil_mapping["maintal-bischofsheim"] = "Umland"
    stadtteil_mapping["hattersheim (früher ffm)"] = "Umland"

    # FRANKFURT ALLGEMEIN
    stadtteil_mapping["ich wohne in stadtteil frankfurt"] = "Frankfurt"
    stadtteil_mapping["frankfurt"] = "Frankfurt"
    stadtteil_mapping["frankfurt am main"] = "Frankfurt"
    stadtteil_mapping["i live in the district, seilerstrasse 18 frankfurt 60313"] = (
        "Frankfurt"
    )

    return stadtteil_mapping


def stadtteil_mapping_func(stadtteil: str) -> str:
    mapping = create_stadtteil_mapping()
    stadtteil = stadtteil.strip().lower()
    response = mapping.get(stadtteil, "SPAM")

    if response == "SPAM":
        print("Angegebener Stadtteil konnte nicht zugeordnet werden: " + stadtteil)

    return response

def stadtteil_region_mapping(stadtteil: str) -> str:
    response = merge_regions.get(stadtteil)

    if response is None:
        print("Angegebener Stadtteil konnte keiner Region zugewiesen werden: " + stadtteil)

    return response