import argparse


def main():
    parser = argparse.ArgumentParser(description='A scraper to scrape COVID-19 and weather information')
    parser.add_argument('info_code',
                        help='A code is assigned to the information source. Provide the info code to indicate the source')
    args = parser.parse_args()


if __name__ == '__main__':
    main()
