from Previous.marvel import (characters,
                             most_popular_characters,
                             max_and_min_years_new_characters,
                             get_percentage_female_characters)

half_size = int(len(characters)/2)

half_characters = characters[:half_size]


def test_most_popular_characters():
    actual = most_popular_characters()
    expected = ['Spider-Man', 'Captain America', 'Wolverine',
                'Iron Man', 'Thor']
    assert actual == expected


def test_max_and_min_years_new_characters():
    actual = max_and_min_years_new_characters()
    expected = ('1993', '1958')
    assert actual == expected


def test_get_percentage_female_characters():
    actual = get_percentage_female_characters()
    expected = 24.72
    assert actual == expected


def test_most_popular_characters_smaller_data_set_and_top_2():
    expected = ['Spider-Man', 'Captain America']
    actual = most_popular_characters(half_characters, top=2)
    assert actual == expected


def test_max_and_min_years_new_characters_smaller_data_set():
    expected = ('1992', '1959')
    actual = max_and_min_years_new_characters(half_characters)
    assert actual == expected


def test_get_percentage_female_characters_smaller_data_set():
    actual = get_percentage_female_characters(half_characters)
    expected = 28.73
    assert actual == expected