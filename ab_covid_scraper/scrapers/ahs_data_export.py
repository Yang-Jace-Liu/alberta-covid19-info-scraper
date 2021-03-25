import json

import requests
from bs4 import BeautifulSoup

from ab_covid_scraper.scrapers.scraper import Scraper


class AHSDataExportScraper(Scraper):
    URL = "https://www.alberta.ca/stats/covid-19-alberta-statistics.htm#data-export"

    @staticmethod
    def code() -> str:
        return "AHSDATA"

    @staticmethod
    def description() -> str:
        return "Scrape COVID-19 data from https://www.alberta.ca/stats/covid-19-alberta-statistics.htm#data-export"

    def __init__(self):
        self._type_element_map = {
            "cases": "htmlwidget-bb35c0bfc61700d1e896"
        }

    def scrape(self, *args, **kwargs) -> object:
        assert len(args) > 0, "AHSData needs at least 1 argument: information type. Check docs for more information"
        type_str: str = args[0]

        assert type_str in self._type_element_map, "Unknown information type: %s" % type_str
        element = self._type_element_map.get(type_str)

        return self.scrape_data_for_element(element)

    def scrape_data_for_element(self, element):
        response = requests.get(self.URL)
        soup = BeautifulSoup(response.text, "html.parser")
        data = soup.find("script", {"data-for": element})
        if data is None:
            raise Exception("Error: cannot find element: %s" % element)
        data = json.loads(data.contents[0])
        return json.dumps(data["x"]["data"])