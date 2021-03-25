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

# Information Code

|Code|Data Source|Arguments|
|----|-------|-------------|
|AHSHEATMAP|https://www.alberta.ca/stats/covid-19-alberta-statistics.htm#geospatial|NULL