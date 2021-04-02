import pytest

from ab_covid_scraper.scrapers.ahs_data_export import AHSDataExportScraper
from ab_covid_scraper.scrapers.scraper import Scraper


@pytest.fixture
def scraper() -> Scraper:
    return AHSDataExportScraper()


def test_ahs_data_export(scraper):
    out: str = scraper.scrape("cases")
    assert len(out) > 1000


def test_ahs_other_data_sources(scraper):
    sources = (
        "cases_last_week_by_zone",
        "cases_active_by_zone",
        "cases_last_week_by_age",
        "cases_active_by_age",
        "cases_last_week_by_source",
        "cases_active_by_source",
        "cases_per_day_by_state",
        "cases_per_day_by_source",
        "cases_per_day_by_confirmation",
        "cases_per_day_by_age",
        "density_per_day_by_age"
    )
    for source in sources:
        out = scraper.scrape(source)
        assert len(out) > 100
