from python_news import get_top_titles, Entry

homepage = ("https://bites-data.s3.us-east-2.amazonaws.com/"
            "news.python.sc/index.html")
page2 = ("https://bites-data.s3.us-east-2.amazonaws.com/"
         "news.python.sc/index2.html")


def test_homepage():
    actual = get_top_titles(homepage)
    expected = [
        Entry(title='How do you set up your Python development environment?',
              points=15, comments=8),
        Entry(title='Python alternative to Docker (www.mattlayman.com)',
              points=9, comments=4),
        Entry(title='Debugging Python programs (stribny.name)',
              points=9, comments=3),
        Entry(title='New features planned for Python 4.0 (charlesleifer.com)',
              points=9, comments=2),
        Entry(title='Python 3.8 is out (www.python.org)',
              points=9, comments=0),
    ]
    assert actual == expected


def test_page2():
    actual = get_top_titles(page2, top=2)
    expected = [
        Entry(title='Django REST Framework - Typed Views (github.com)',
              points=4, comments=0),
        Entry(title=('Show 🐍: A news aggregator for the Python community '
                     'written in Python/Django (github.com)'),
              points=3, comments=1),
    ]
    assert actual == expected