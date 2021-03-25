from typing import List, Type, Optional

from ab_covid_scraper.scrapers.scraper import Scraper


class ScraperWrapper(object):
    def __init__(self, cls: Type[Scraper], code, description):
        self._cls = cls
        self._code = code
        self._description = description

    @property
    def cls(self):
        return self._cls

    @property
    def code(self):
        return self._code

    @property
    def description(self):
        return self._description

    def run(self, *args, **kwargs):
        instance = self._cls()
        instance.scrape(*args, **kwargs)


class ScraperManager(object):
    # TODO: Optimize this using Dict, code as the key
    scrapers: List[Type[Scraper]] = []

    @staticmethod
    def get_available_scrapers() -> List[ScraperWrapper]:
        return [ScraperWrapper(scraper, scraper.code, scraper.description) for scraper in ScraperManager.scrapers]

    @staticmethod
    def get_scraper(code) -> Optional[ScraperWrapper]:
        try:
            scraper_cls = next(filter(lambda x: x.code == code, ScraperManager.scrapers))
            return ScraperWrapper(scraper_cls, scraper_cls.code, scraper_cls.description)
        except StopIteration:
            return None

    @staticmethod
    def add_scraper(cls: Type[Scraper]):
        ScraperManager.scrapers.append(cls)
