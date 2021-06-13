FROM python:3

RUN mkdir /scraper_app

WORKDIR /scraper_app

COPY setup.py .

COPY scripts ./scripts

COPY ab_covid_scraper ./ab_covid_scraper

RUN python3 setup.py install

ENTRYPOINT ["ab-covid-scraper.py"]

