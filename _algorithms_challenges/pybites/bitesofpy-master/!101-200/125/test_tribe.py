import pytest

from tribe import get_top_books, load_page


@pytest.fixture(scope='module')
def content():
    """Load content once for all test"""
    return load_page()


def test_get_top_5_books(content):
    books = get_top_books(content=content)
    assert books == ['Man’s Search For Meaning',
                     ('The 4-Hour Workweek: Escape the 9-5, '
                      'Live Anywhere and Join the New Rich'),
                     'The Fountainhead',
                     'Sapiens: A Brief History of Humankind',
                     'Tao Te Ching']


def test_get_top_10_books(content):
    books = get_top_books(content=content, limit=10)
    assert books[5:] == [('The Better Angels of our Nature: Why Violence '
                          'Has Declined'),
                         ('The Beginning of Infinity: Explanations That '
                          'Transform ' 'the World'),
                         ('The War of Art: Break Through the Blocks and Win '
                          'Your Inner Creative Battles'),
                         'The Hero with a Thousand Faces ',
                         'Poor Charlie’s Almanack']