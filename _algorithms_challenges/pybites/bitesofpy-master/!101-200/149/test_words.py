from words import sort_words_case_insensitively


def test_sort_words_case_insensitively():
    words = ("It's almost Holidays and PyBites wishes You a "
             "Merry Christmas and a Happy 2019").split()
    actual = sort_words_case_insensitively(words)
    expected = ['a', 'a', 'almost', 'and', 'and', 'Christmas',
                'Happy', 'Holidays', "It's", 'Merry', 'PyBites',
                'wishes', 'You', '2019']
    assert actual == expected


def test_sort_words_case_insensitively_another_phrase():
    words = ("Andrew Carnegie's 64-room chateau at 2 East 91st "
             "Street was converted into the Cooper-Hewitt National "
             "Design Museum of the Smithsonian Institution "
             "in the 1970's").split()
    actual = sort_words_case_insensitively(words)
    expected = ['Andrew', 'at', "Carnegie's", 'chateau', 'converted',
                'Cooper-Hewitt', 'Design', 'East', 'in', 'Institution',
                'into', 'Museum', 'National', 'of', 'Smithsonian',
                'Street', 'the', 'the', 'the', 'was', "1970's", '2',
                '64-room', '91st']
    assert actual == expected