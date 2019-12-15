import pytest

from quotes import extract_quotes


expected_authors = [
    'B.B King', 'Wendy Kopp', 'Barack Obama', 'T.F. Hodge',
    'Helen Keller', 'Confucius', 'Les Brown', 'Winston Churchill',
    'Theodore Roosevelt', 'Zig Ziglar'
]

expected_quotes = [
    ('The beautiful thing about learning is nobody can take it away'
     ' from you.'),
    'Inexperience is an asset. Embrace it.',
    ('Change will not come if we wait for some other person, or if '
     'we wait for some other time. We are the ones we’ve been '
     'waiting for. We are the change that we seek.'),
    'The sky is not my limit… I am.',
    'Life is either a daring adventure or nothing at all.',
    'It does not matter how slowly you go as long as you do not stop.',
    ('Too many of us are not living our dreams because we are '
     'living our fears.'),
    ('Continuous efforts – not strength or intelligence – is the '
     'key to unlocking our potential.'),
    'Believe you can and you’re halfway there.',
    ('Success means doing the best we can with what we have. '
     'Success is the doing, not the getting; in the trying, '
     'not the triumph. Success is a personal standard, reaching '
     'for the highest that is in us, becoming all that we can be.')
]


@pytest.fixture(scope="module")
def output_your_code():
    return extract_quotes()


def test_quotes_type(output_your_code):
    assert type(output_your_code) == dict


def test_quotes_len(output_your_code):
    assert len(output_your_code) == 10


@pytest.mark.parametrize("author, quote",
                         zip(expected_authors, expected_quotes))
def test_quotes_dict_content(author, quote, output_your_code):
    assert output_your_code.get(author) == quote