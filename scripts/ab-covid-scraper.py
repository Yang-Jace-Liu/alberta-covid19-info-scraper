import argparse

from ab_covid_scraper.scrapers import ScraperManager


def main():
    parser = argparse.ArgumentParser(description='A scraper to scrape COVID-19 and weather information')
    parser.add_argument('info_code',
                        help='A code is assigned to the information source. Provide the info code to indicate the source')
    parser.add_argument('arguments', nargs='*', help='Arguments for this information source')
    args = parser.parse_args()

    scraper = ScraperManager.get_scraper(args.info_code)

    if scraper is None:
        print("Unknown info_code: %s" % args.info_code)
        return 1
    else:
        result = scraper.run(*args.arguments)
        print(result)
        return 0


if __name__ == '__main__':
    exit(main())
