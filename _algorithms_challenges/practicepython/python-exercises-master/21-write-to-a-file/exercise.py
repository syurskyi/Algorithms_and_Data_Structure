#! /Users/piotrjankiewicz/anaconda3/bin/python3.6
import requests
from bs4 import BeautifulSoup


def getPortions(soup):
    # this is a generator
    heading = soup.find('div', {'class': 'deck'})
    if heading:
        yield heading.text

    for p in soup.find_all('p', {'class': ''}):
        yield p.text


def writePageToFile(url):
    page = requests.get(url)

    soup = BeautifulSoup(page.text, 'html.parser')

    name = input('Tell me the name of file in which page should be saved: ')

    open_file = open(name + '.txt', 'a')

    for element in getPortions(soup):
        open_file.write(element + '\n')

    open_file.close()

    print('\nArticle was saved in ' + name + '.txt file.')


if __name__ == '__main__':
    url = 'https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture'
    writePageToFile(url)
