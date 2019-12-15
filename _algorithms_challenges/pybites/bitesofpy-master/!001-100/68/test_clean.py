import pytest

from Previous.clean import remove_punctuation


@pytest.mark.parametrize("input_argument, expected_return", [
    ('Hello, I am Tim.', 'Hello I am Tim'),
    (';String. with. punctuation characters!',
     'String with punctuation characters'),
    ('Watch out!!!', 'Watch out'),
    ('Spaces - should - work the same, yes?',
     'Spaces  should  work the same yes'),
    ("Some other (chars) |:-^, let's delete them",
     'Some other chars  lets delete them'),
])
def test_remove_punctuation(input_argument, expected_return):
    assert remove_punctuation(input_argument) == expected_return
