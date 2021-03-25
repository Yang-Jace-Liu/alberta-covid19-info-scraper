from abc import ABC, abstractmethod


class Scraper(ABC):
    """
    The scraper interface
    """

    @staticmethod
    @abstractmethod
    def code(self) -> str:
        """
        The code of this information source
        :return: A string indicating the unique code of this source
        """
        pass

    @staticmethod
    @abstractmethod
    def description(self) -> str:
        pass

    @abstractmethod
    def scrape(self, *args, **kwargs) -> object:
        """
        Scrape the information using the parameters in *args and **kwargs
        :return: The result of scraping
        """
        pass
