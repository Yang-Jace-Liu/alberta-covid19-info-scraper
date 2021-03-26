import requests

from ab_covid_scraper.scrapers.scraper import Scraper


class WeatherGCScraper(Scraper):
    @staticmethod
    def code() -> str:
        return "WEATHERGC"

    @staticmethod
    def description() -> str:
        return "Daily weather data from https://climate.weather.gc.ca/climate_data/daily_data_e.html?StationID=50430"

    def scrape(self, *args, **kwargs) -> object:
        assert len(args) >= 1
        try:
            int(args[0])
            year = args[0]
        except ValueError:
            raise "Unknown argument year: %s" % args[0]

        try:
            format = args[1]
            assert format in ["xml", "csv"]
        except IndexError:
            format = "csv"

        api_url = "https://climate.weather.gc.ca/climate_data/bulk_data_e.html"

        params = {
            "stationID": "50430",
            "Year": year,
            "format": format,
            "time": "",
            "timeframe": 2,
            "submit": "Download Data"
        }

        r = requests.get(api_url, params=params)
        if int(r.status_code / 100) != 2:
            raise ConnectionError("Status code: " + str(r.status_code))
        return r.text
