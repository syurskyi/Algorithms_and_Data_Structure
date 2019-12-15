from pathlib import Path
from urllib.request import urlretrieve
from dataclasses import dataclass

from bs4 import BeautifulSoup, Tag

url = "https://bites-data.s3.us-east-2.amazonaws.com/" "best-programming-books.html"
tmp = Path("/tmp")
html_file = tmp / "books.html"

if not html_file.exists():
    urlretrieve(url, html_file)


@dataclass
class Book:
    """Book class should instatiate the following variables:

    title - as it appears on the page
    author - should be entered as lastname, firstname
    year - four digit integer year that the book was published
    rank - integer rank to be updated once the books have been sorted
    rating - float as indicated on the page
    """

    title: str
    author: str
    year: int
    rank: int
    rating: float

    def _rating(self):
        res = f"{self.rating:.2f}"
        return res[:-1] if res[-1] == "0" else res

    def __str__(self):
        return (
            f"[{self.rank:03}] {self.title} ({self.year})\n"
            f"      {self.author} {self._rating()}"
        )


def _get_soup(file):
    return BeautifulSoup(file.read_text(), "html.parser")


def display_books(books, limit=10, year=None):
    """Prints the specified books to the console

    :param books: list of all the books
    :param limit: integer that indicates how many books to return
    :param year: integer indicating the oldest year to include
    :return: None
    """
    for b in books:
        if limit == 0:
            break
        if year is None or b.year >= year:
            print(b)
            limit -= 1


def load_data():
    """Loads the data from the html file

    Creates the soup object and processes it to extract the information
    required to create the Book class objects and returns a sorted list
    of Book objects.

    Books should be sorted by rating, year, title, and then by author's
    last name. After the books have been sorted, the rank of each book
    should be updated to indicate this new sorting order.The Book object
    with the highest rating should be first and go down from there.
    """
    soup = _get_soup(html_file)
    book_list = soup.find("div", {"class": "books"})
    books = []
    book: Tag
    for book in book_list.find_all("div", {"class": "book"}):
        title = book.select("h2.main")[0].text
        if "python" not in title.lower():
            continue
        try:
            author_a = book.select("h3.authors > a")[0].text.split(" ")
            author = f'{author_a[-1]}, {" ".join(author_a[:-1])}'
            date_span = book.select("span.date")
            if len(date_span) == 0:
                continue
            year = int(date_span[0].text[-4:])
            rank = int(book.select("div.rank > span")[0].text)
            rating = float(book.select("span.our-rating")[0].text)
        except AttributeError:
            continue
        books.append(
            Book(title=title, author=author, year=year, rank=rank, rating=rating)
        )
    res = []
    for n, b in enumerate(
        sorted(
            books, key=lambda b: (-b.rating, b.year, b.title.lower(), b.author.lower())
        ),
        start=1,
    ):
        b.rank = n
        res.append(b)
    return res


def main():
    books = load_data()
    display_books(books, limit=5, year=2017)
    """If done correctly, the previous function call should display the
    output below.
    """


if __name__ == "__main__":
    main()

"""
[001] Python Tricks (2017)
      Bader, Dan 4.74
[002] Mastering Deep Learning Fundamentals with Python (2019)
      Wilson, Richard 4.7
[006] Python Programming (2019)
      Fedden, Antony Mc 4.68
[007] Python Programming (2019)
      Mining, Joseph 4.68
[009] A Smarter Way to Learn Python (2017)
      Myers, Mark 4.66
"""
