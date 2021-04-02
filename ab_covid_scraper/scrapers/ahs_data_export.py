import json
from typing import Dict

import requests
from bs4 import BeautifulSoup

from ab_covid_scraper.scrapers.scraper import Scraper


class AHSDataSelector(object):
    def __init__(self, index, tab_id=None):
        self._tab_id = tab_id
        self._index = index

    def select(self, page: BeautifulSoup) -> str:
        if self._tab_id is not None:
            page = page.find('div', id=self._tab_id)

        element = page.findAll('div', id=lambda x: x and x.startswith('htmlwidget-'))[self._index]
        return element.get('id')


class AHSDataExportScraper(Scraper):
    URL = "https://www.alberta.ca/stats/covid-19-alberta-statistics.htm#data-export"

    @staticmethod
    def code() -> str:
        return "AHSDATA"

    @staticmethod
    def description() -> str:
        return "Scrape COVID-19 data from https://www.alberta.ca/stats/covid-19-alberta-statistics.htm"

    def __init__(self):
        self._type_element_map: Dict[str, AHSDataSelector] = {
            "cases": AHSDataSelector(0, 'data-export'),
            "cases_last_week_by_zone": AHSDataSelector(0, "new-cases"),
            "cases_active_by_zone": AHSDataSelector(1, "new-cases"),
            "cases_last_week_by_age": AHSDataSelector(2, "new-cases"),
            "cases_active_by_age": AHSDataSelector(3, "new-cases"),
            "cases_last_week_by_source": AHSDataSelector(4, "new-cases"),
            "cases_active_by_source": AHSDataSelector(5, "new-cases"),
            "cases_per_day_by_state": AHSDataSelector(0, "total-cases"),
            "cases_per_day_by_source": AHSDataSelector(1, "total-cases"),
            "cases_per_day_by_confirmation": AHSDataSelector(2, "total-cases"),
            "cases_per_day_by_age": AHSDataSelector(0, "characteristics"),
            "density_per_day_by_age": AHSDataSelector(1, "characteristics")
        }

    def scrape(self, *args, **kwargs) -> str:
        assert len(args) > 0, "AHSData needs at least 1 argument: information type. Check docs for more information"
        type_str: str = args[0]

        assert type_str in self._type_element_map, "Unknown information type: %s" % type_str
        element = self._type_element_map.get(type_str)

        return self.scrape_data_for_element(element)

    def scrape_data_for_element(self, element: AHSDataSelector):
        response = requests.get(self.URL)
        soup = BeautifulSoup(response.text, "html.parser")
        widget_id_str = element.select(soup)
        data = soup.find("script", {"data-for": widget_id_str})
        if data is None:
            raise Exception("Error: cannot find element: %s" % element)
        data = json.loads(data.contents[0])
        return json.dumps(data["x"]["data"])
