import pytest

from Previous.gravatar import create_gravatar_url

BASE_URL = "https://www.gravatar.com/avatar/"
HASHED_INFO_EMAIL = "ff2de96de035e1ccdb39ca31d3fe4a5c"
HASHED_SUPPORT_EMAIL = "1c888a408baa7a685c7c06155e48de84"
SIZE, DEFAULT = 200, 'robohash'

EXPECTED = iter([  # make an iterator
    f'{BASE_URL}{HASHED_INFO_EMAIL}?s={SIZE}&r=g&d={DEFAULT}',
    f'{BASE_URL}{HASHED_INFO_EMAIL}?s={SIZE}&r=g&d={DEFAULT}',
    f'{BASE_URL}{HASHED_INFO_EMAIL}?s=40&r=g&d={DEFAULT}',
    f'{BASE_URL}{HASHED_SUPPORT_EMAIL}?s={SIZE}&r=g&d={DEFAULT}',
    f'{BASE_URL}{HASHED_SUPPORT_EMAIL}?s={SIZE}&r=g&d={DEFAULT}',
    f'{BASE_URL}{HASHED_SUPPORT_EMAIL}?s=1000&r=g&d={DEFAULT}',
])


@pytest.mark.parametrize("email, size", [
    ("info@pybit.es", 200),
    ("info@pybit.es ", 200),
    ('info@pybit.ES', 40),
    ('support@pybit.es', 200),
    ('support@PYBIT.es', 200),
    (' support@pybit.es', 1000),
])
def test_gravatar(email, size):
    actual = create_gravatar_url(email, size=size)
    expected = next(EXPECTED)
    assert actual == expected