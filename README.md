# Alberta Covid Info Scraper

# Installation
```bash
git clone https://github.com/Yang-Jace-Liu/alberta-covid19-info-scraper
pip install .
```

# Usage
```bash
usage: ab-covid-scraper.py [-h] {run,list} ...

A scraper to scrape COVID-19 and weather information

optional arguments:
  -h, --help  show this help message and exit

commands:
  {run,list}
    run       Run a scraper to get the information
    list      List all available scrapers
```

# Docker Usage
```bash
usage: docker exec -it [container-id] python3 home/scripts/ab-covid-scraper.py [-h] {run,list} ...
```

# Information Code

|Code|Data Source|Description|Arguments|
|----|-----------|-----------|---------|
|AHSHEATMAP|https://www.alberta.ca/stats/covid-19-alberta-statistics.htm#geospatial|Geospatial COVID information|NULL
|AHSDATA|https://www.alberta.ca/stats/covid-19-alberta-statistics.htm#data-export|COVID statistics|data_type. Check [AHSDATA](#AHSDATA)
|WEATHERGC|https://climate.weather.gc.ca/climate_data/daily_data_e.html?StationID=50430|Weather history|year, format. Check [WEATHERGC](#WEATHERGC)
|WEATHERSTATS|https://calgary.weatherstats.ca/charts/temperature-daily.html|The highest, lowest, and mean temperature in recent 2 weeks|NULL
|ARCGISABCOVID|https://robsonfletcher.maps.arcgis.com/apps/View/index.html?appid=23c067a0048d4320859e55be7d89949b|Regional Covid-19 information|NULL

# AHSDATA

## Arguments:

* data_type: A string to indicate the kind of information type it will scrape.

## data_type 

|Value|Description|
|-----|-----------|
|cases|The information of each case, including age range, area, the date the case got test positive, if recovered, and if the case is confirmed.
|cases_last_week_by_zone|The number of cases in last week by zones.|
|cases_active_by_zone|The number of active cases by zones.|
|cases_last_week_by_age|The number of cases in last week by ages.|
|cases_active_by_age|The number of active cases by ages.|
|cases_last_week_by_source|The number of cases in last week by infection reasons.|
|cases_active_by_source|The number of active cases by infection reasons.|
|cases_per_day_by_state|The per-day number of total cases, active cases, recovered cases and deaths.|
|cases_per_day_by_source|The per-day number of cases in different reasons: known exposure, travel, and unknown exposure.|
|cases_per_day_by_confirmation|The per-day number of confirmed cases and probable cases.|
|cases_per_day_by_age|The per-day number of cases by ages.|
|density_per_day_by_age|The per-day density (number of cases per 100,000 population) by ages.

# WEATHERGC

## Argument:

* year: The year of weather data
* format (optional): The format of required data. Available formats: csv, xml. Default format is csv.
