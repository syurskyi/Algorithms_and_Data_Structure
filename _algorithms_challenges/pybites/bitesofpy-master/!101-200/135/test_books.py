from books import (sort_books_by_len_of_title,
                   sort_books_by_first_authors_last_name,
                   sort_books_by_number_of_page,
                   sort_books_by_published_date)


def test_sort_books_by_len_of_title():
    last_book = sort_books_by_len_of_title()[-1]
    assert last_book.title == 'Automate the Boring Stuff with Python'


def test_sort_books_by_first_authors_last_name():
    last_book = sort_books_by_first_authors_last_name()[-1]
    assert last_book.title == 'Automate the Boring Stuff with Python'


def test_sort_books_by_number_of_page():
    last_book = sort_books_by_number_of_page()[-1]
    assert last_book.title == 'Fluent Python'


def test_sort_books_by_published_date():
    last_book = sort_books_by_published_date()[-1]
    assert last_book.title == 'Python Interviews'