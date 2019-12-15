#! /usr/bin/env python

import requests
from bs4 import BeautifulSoup


def getPortions(soup):
    # this is a generator
    heading = soup.find('div', {'class': 'deck'})
    if heading:
        yield heading.text

    for p in soup.find_all('p', {'class': ''}):
        yield p.text


def readPage(url):
    page = requests.get(url)

    soup = BeautifulSoup(page.text, 'html.parser')

    for element in getPortions(soup):
        print('\n%s' % element)
        input("\nPress 'Enter' to continue: ")

    print('\nEnd of article.')


if __name__ == '__main__':
    url = 'https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture'
    readPage(url)
