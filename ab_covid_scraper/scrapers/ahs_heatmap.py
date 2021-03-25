import json
import re
from typing import Dict, Union

import requests
from bs4 import BeautifulSoup

from ab_covid_scraper.scrapers.scraper import Scraper


class AlbertaHealthServiceHeatmapScraper(Scraper):
    @staticmethod
    def code() -> str:
        return "AHSHEATMAP"

    @staticmethod
    def description() -> str:
        return "Fetch the AHS Covid Heatmap Data from https://www.alberta.ca/stats/covid-19-alberta-statistics.htm#geospatial"

    def scrape(self, *args, **kwargs) -> object:
        raw_data = self.get_data_body()
        reformatted_data = self.reformat(raw_data)
        return reformatted_data

    def get_data_body(self):
        """
        Scrape the data object from AHS(Alberta Health Service) website
        """
        response = requests.get("https://www.alberta.ca/stats/covid-19-alberta-statistics.htm#geospatial")
        soup = BeautifulSoup(response.content, features='html.parser')
        geospatial = soup.find('div', {'id': "geospatial"})
        script_tag = geospatial.find('script', recursive=False)
        data_str = script_tag.string
        return json.loads(data_str)

    def reformat(self, raw):
        """
        This function is to reformat the raw data retrived from webpage.

        The main information locates in the "x" property of raw data
        raw["x"]["calls"] is a list of objects, each object represent a function call to the drawing library
        The function name we are looking into is "addPolygons".
        The first "addPolygon" function represents the "Municipality" view.
        The second "addPolygon" function represents the " Local geographic area" view.
        All the information we need locates in the "args" property of the second "addPolygon" function.
        """
        calls = raw["x"]["calls"]

        reformatted_data = []

        # Find the second "addPolygons"
        found_addPolygons = 0
        call_addPolygon = None
        for call in calls:
            method = call["method"]
            if method == "addPolygons":
                found_addPolygons += 1
                if found_addPolygons == 2:
                    call_addPolygon = call
                    break
        assert call_addPolygon is not None, "Cannot find the addPolygan call in raw data"
        args = call_addPolygon["args"]
        border_list = args[0]
        graph_name = args[2]
        properties = args[3]

        info_list = args[6]

        for border, info_str, color in zip(border_list, info_list, properties['fillColor']):
            data = {'fillColor': color}
            info = self.parse_info_str(info_str)
            data["name"], data["total"], data["active"], data["recovered"], data["death"] = info["name"], info["total"], \
                                                                                            info["active"], info[
                                                                                                "recovered"], info[
                                                                                                "death"]
            data["border"] = []

            try:
                border_obj = border[0][0]
            except IndexError:
                continue
            for lat, lng in zip(border_obj["lat"], border_obj["lng"]):
                data["border"].append({"lat": lat, "lng": lng})

            reformatted_data.append(data)

        return reformatted_data

    def parse_info_str(self, info_str: str):
        data: Dict[str, Union[int, str]] = {}

        delimiter_pattern = r"<br(?: *)\/(?: *)>"
        item_strs = re.split(delimiter_pattern, info_str)
        item_strs = [BeautifulSoup(i.strip(), features='html.parser').get_text() for i in item_strs]

        data["name"] = item_strs[0]
        data["total"] = int(item_strs[1].split(' ')[0])
        data["active"] = int(item_strs[2].split(' ')[0])
        data["recovered"] = int(item_strs[3].split(' ')[0])
        data["death"] = int(item_strs[4].split(' ')[0])
        return data
