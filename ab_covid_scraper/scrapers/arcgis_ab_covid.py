import json

import requests

from ab_covid_scraper.scrapers.scraper import Scraper


class ArcgisABCovidScraper(Scraper):
    @staticmethod
    def code() -> str:
        return "ARCGISABCOVID"

    @staticmethod
    def description() -> str:
        return "Regional COVID-19 cases from https://robsonfletcher.maps.arcgis.com/apps/View/index.html?appid=23c067a0048d4320859e55be7d89949b"

    def scrape(self, *args, **kwargs) -> object:
        api_url = "https://services7.arcgis.com/mqgOnhfK77151sEK/arcgis/rest/services/Active_Cases_Per_Capita_by_Local_Geographic_Area/FeatureServer/0/query?f=json&returnGeometry=true&spatialRel=esriSpatialRelIntersects&geometry=%7B%22xmin%22%3A-15028131.257092927%2C%22ymin%22%3A5009377.085700966%2C%22xmax%22%3A-10018754.171396947%2C%22ymax%22%3A10018754.171396947%2C%22spatialReference%22%3A%7B%22wkid%22%3A102100%7D%7D&geometryType=esriGeometryEnvelope&inSR=102100&outFields=*&outSR=102100&resultType=tile&quantizationParameters=%7B%22mode%22%3A%22view%22%2C%22originPosition%22%3A%22upperLeft%22%2C%22tolerance%22%3A9783.93962049996%2C%22extent%22%3A%7B%22xmin%22%3A-13358372.004187994%2C%22ymin%22%3A6274308.252068483%2C%22xmax%22%3A-12245128.178839874%2C%22ymax%22%3A8399754.189188747%2C%22spatialReference%22%3A%7B%22wkid%22%3A102100%2C%22latestWkid%22%3A3857%7D%7D%7D"
        r = requests.get(api_url)
        obj = json.loads(r.text)
        return json.dumps(obj['features'])
