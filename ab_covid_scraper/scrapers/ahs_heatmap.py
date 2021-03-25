from ab_covid_scraper.scrapers.scraper import Scraper


class AlbertaHealthServiceHeatmapScraper(Scraper):
    @staticmethod
    def code(self) -> str:
        return "AHSHEATMAP"

    @staticmethod
    def description(self) -> str:
        "Fetch the AHS Heatmap Data from "

    def scrape(self, *args, **kwargs) -> object:
        pass
