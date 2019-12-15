from string import ascii_uppercase, digits
import random

from license import validate_license

ALPHABET = ascii_uppercase + digits


def _create_license():
    return 'PB-' + '-'.join(
        [''.join(random.sample(ALPHABET, 8))
         for _ in range(4)]
    )


def test_valid_license():
    for _ in range(10):
        key = _create_license()
        assert validate_license(key)


def test_return_type():
    key = _create_license()
    assert validate_license(key) is True
    assert validate_license(key[:-1]) is False


def test_invalid_license():
    pool = [_create_license() for _ in range(5)]
    lcase_key = pool[0].lower()
    assert not validate_license(lcase_key)
    shorter_key = pool[1][:-2]
    assert not validate_license(shorter_key)
    longer_key = pool[2] + 'A'
    assert not validate_license(longer_key)
    wrong_prefix = 'AB-' + pool[3][3:]
    assert not validate_license(wrong_prefix)
    empty_key = ''
    assert not validate_license(empty_key)
    key_reversed = pool[4][::-1]
    assert not validate_license(key_reversed)


def test_valid_prefix():
    license = "PB-U8N435EH-PG65PW87-IXPWQG5T-898XSZI4"
    assert validate_license(license)
    assert not validate_license(license.replace('PB', 'APB'))
    assert not validate_license(license.replace('PB', 'COAPB'))