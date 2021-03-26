#!/usr/bin/env python3
import argparse

from ab_covid_scraper.scrapers import ScraperManager


def main():
    parser = argparse.ArgumentParser(description='A scraper to scrape COVID-19 and weather information')
    subparsers = parser.add_subparsers(title='commands', required=True, dest='command')

    parser_run = subparsers.add_parser('run', help='Run a scraper to get the information')
    parser_run.set_defaults(func=run_scraper)
    parser_run.add_argument('info_code',
                            help='A code is assigned to the information source. Provide the info code to indicate the source')
    parser_run.add_argument('arguments', nargs='*', help='Arguments for this information source')

    parser_list = subparsers.add_parser('list', help='List all available scrapers')
    parser_list.set_defaults(func=list_scrapers)

    args = parser.parse_args()
    args.func(args)


def run_scraper(args):
    scraper = ScraperManager.get_scraper(args.info_code)
    if scraper is None:
        print("Unknown info_code: %s" % args.info_code)
        return 1
    result = scraper.run(*args.arguments)
    if result is None:
        return 1
    print(result)
    return 0


def list_scrapers(args):
    scrapers = ScraperManager.get_available_scrapers()
    for scraper in scrapers:
        print("%10s    %s" % (scraper.code(), scraper.description()))


if __name__ == '__main__':
    exit(main())
