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
            "cases": "htmlwidget-bb35c0bfc61700d1e896",
            "cases_last_week_by_zone": "htmlwidget-a4f0a1c47709305f3ca2",
            "cases_active_by_zone": "htmlwidget-b3c20fdf3ca9927ff8d9",
            "cases_last_week_by_age": "htmlwidget-afc37081ff68d8aedc3f",
            "cases_active_by_age": "htmlwidget-6955d71f98735c8e486a",
            "cases_last_week_by_source": "htmlwidget-154345f031d427a8c16d",
            "cases_active_by_source": "htmlwidget-d187025499ef06d2c1fa",
            "cases_per_day_by_status": "htmlwidget-0cd08c3028c479b58ba7",
            "cases_per_day_by_source": "htmlwidget-fb64085719406f5b8314",
            "cases_per_day_by_confirmation": "htmlwidget-755ed844fe564420a516",
            "cases_per_day_by_age": "htmlwidget-cd5ae5f9b4cb4cee35a8",
            "density_per_day_by_age": "htmlwidget-719b898fa4c1fb47ce2a"
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