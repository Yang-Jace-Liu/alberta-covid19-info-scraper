import datetime
import json
import re

import requests

from ab_covid_scraper.scrapers.scraper import Scraper


class WeatherStatsScraper(Scraper):
    data_pattern = r"\{\"c\":\[\{\"v\"\:new Date\(([\d\ ]+),([\d\ ]+),([\d\ ]+)\)\},{\"v\":(-?\d+(?:\.\d+))},{\"v\":(-?\d+(?:\.\d+))},{\"v\":(-?\d+(?:\.\d+))},{\"v\":(-?\d+(?:\.\d+))}\]\}"

    @staticmethod
    def code() -> str:
        return "WEATHERSTATS"

    @staticmethod
    def description() -> str:
        return "The highest, lowest, and mean temperature in recent 2 weeks: https://calgary.weatherstats.ca/charts/temperature-daily.html"

    def scrape(self, *args, **kwargs) -> object:
        api_url = "https://calgary.weatherstats.ca/data/temperature-daily.js"
        r = requests.get(api_url)
        if int(r.status_code / 100) != 2:
            raise ConnectionError("HTTP status code is %d" % r.status_code)
        content = r.text
        matches = re.finditer(self.data_pattern, content)
        points = []
        for match in matches:
            points.append(self.parse(match))
        return json.dumps(points)

    def parse(self, match):
        year = int(match.group(1).strip())
        month = int(match.group(2).strip())
        day = int(match.group(3).strip())
        maximum = float(match.group(4).strip())
        hourly_mean = float(match.group(5).strip())
        min_max_mean = float(match.group(6).strip())
        minimum = float(match.group(7).strip())
        s = datetime.datetime.strftime(datetime.date(year, month, day), "%Y-%m-%d")
        return {
            "date": s,
            "maximum": maximum,
            "minimum": minimum,
            "hourly_mean": hourly_mean,
            "min_max_mean": min_max_mean
        }
