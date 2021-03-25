#!/usr/bin/env python3

from distutils.core import setup

from setuptools import find_packages

requirements = [
    "pytest",
    "requests",
    "beautifulsoup4"
]

setup(name='alberta-covid-info-scraper',
      version='0.0.1dev1',
      description='A scraper to scrape COVID-19 and weather information',
      author='Yang Liu',
      author_email='yang.liu5@ucalgary.ca',
      packages=find_packages(),
      scripts=['scripts/ab-covid-scraper.py'],
      install_requires=requirements
      )
