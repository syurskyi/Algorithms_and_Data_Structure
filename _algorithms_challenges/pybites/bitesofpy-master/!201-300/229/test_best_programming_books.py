import pytest

from best_programming_books import Book, display_books, load_data


@pytest.fixture(scope="session")
def dummy_book():
    title = "Python Testing with pytest"
    author = "Okken, Brian"
    year = 2017
    rank = 1
    rating = 5
    return Book(title, author, year, rank, rating)


@pytest.fixture(scope="session")
def python_books():
    data = load_data()
    if isinstance(data, list):
        return data
    return list(data)


def test_book_class_incorrectly():
    with pytest.raises(TypeError):
        Book()


def test_book_class(dummy_book):
    assert dummy_book.title == "Python Testing with pytest"
    assert dummy_book.author == "Okken, Brian"
    assert dummy_book.year == 2017
    assert dummy_book.rank == 1
    assert dummy_book.rating == 5


def test_book_class_str(dummy_book):
    actual = str(dummy_book)
    expected = ("[001] Python Testing with pytest (2017)"
                "\n      Okken, Brian 5.0")
    assert actual == expected


def test_load_data(python_books):
    assert len(python_books) == 36
    assert python_books[0].author == "Bader, Dan"
    assert python_books[-1].title == "Python for Tweens and Teens"
    assert python_books[10].rating == 4.66


@pytest.mark.parametrize(
    "index, expected",
    [
        (0, "[001] Python Tricks (2017)"),
        (1, "      Bader, Dan 4.74"),
        (2, "[002] Mastering Deep Learning Fundamentals with Python (2019)"),
        (3, "      Wilson, Richard 4.7"),
        (4, "[006] Python Programming (2019)"),
        (5, "      Fedden, Antony Mc 4.68"),
        (6, "[007] Python Programming (2019)"),
        (7, "      Mining, Joseph 4.68"),
        (8, "[009] A Smarter Way to Learn Python (2017)"),
        (9, "      Myers, Mark 4.66"),
        (10, "[010] Python Crash Course (2019)"),
        (11, "      Robert, Antonio 4.66"),
        (12, "[011] PYTHON PROGRAMMING (2019)"),
        (13, "      Campbell, Clive 4.66"),
        (14, "[012] Python Programming (2019)"),
        (15, "      Harvard, Chris 4.66"),
        (16, "[013] Python Programming (2019)"),
        (17, "      Samelson, Steven 4.66"),
        (18, "[014] Python Programming (2019)"),
        (19, "      James, Thomas 4.65"),
    ],
)
def test_display_books(python_books, index, expected, capfd):
    display_books(python_books, year=2017)
    output = capfd.readouterr()[0].splitlines()
    assert output[index] == expected


@pytest.mark.parametrize(
    "limit, expected", [(40, 72), (53, 72), (69, 72), (100, 72), (1000, 72)]
)
def test_display_books_plus(python_books, limit, expected, capfd):
    display_books(python_books, limit=limit)
    output = capfd.readouterr()[0].splitlines()
    assert len(output) == expected