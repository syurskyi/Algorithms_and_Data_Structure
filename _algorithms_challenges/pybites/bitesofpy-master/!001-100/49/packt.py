from collections import namedtuple

from bs4 import BeautifulSoup as Soup
import requests

CONTENT = requests.get('http://bit.ly/2EN2Ntv').text

Book = namedtuple('Book', 'title description image link')


def get_book():
    """make a Soup object, parse the relevant html sections, and return a Book namedtuple"""
    soup = Soup(CONTENT)
    dotd = soup.find(id='deal-of-the-day')
    image_base = dotd.find(class_='dotd-main-book-image')
    title_base = dotd.find(class_='dotd-title')

    title = title_base.find('h2').text.strip()
    description = title_base.parent.find_all('div')[2].text.strip()
    image = image_base.find('img').attrs['src']
    link = image_base.find('a').attrs['href']

    return Book(title, description, image, link)
