from split import get_sentences

TEXT = """
PyBites was founded 19th of December 2016. That means that today,
14th of October 2019 we are 1029 days old. Time flies when you code
in Python. Anyways, good luck with this Bite. What is your favorite editor?
"""  # contains 5 sentences

TEXT_WITH_DOTS = """
We are looking forward attending the next Pycon in the U.S.A.
in 2020. Hope you do so too. There is no better Python networking
event than Pycon. Meet awesome people and get inspired. Btw this
dot (.) should not end this sentence, the next one should. Have fun!
"""  # contains 6 sentences


def test_get_sentences():
    actual = get_sentences(TEXT)
    expected = [
        "PyBites was founded 19th of December 2016.",
        "That means that today, 14th of October 2019 we are 1029 days old.",
        "Time flies when you code in Python.",
        "Anyways, good luck with this Bite.",
        "What is your favorite editor?"
    ]
    assert actual == expected


def test_dot_mid_sentence():
    actual = get_sentences(TEXT_WITH_DOTS)
    expected = [
        ("We are looking forward attending the next Pycon in the "
         "U.S.A. in 2020."),
        "Hope you do so too.",
        "There is no better Python networking event than Pycon.",
        "Meet awesome people and get inspired.",
        "Btw this dot (.) should not end this sentence, the next one should.",
        "Have fun!"
    ]
    assert actual == expected