from typing.re import Pattern

import pytest

from username_validator import (Validator,
                                parse_social_platforms_string,
                                validate_username)


def test_parse_social_platforms_string():
    platforms = parse_social_platforms_string()
    assert len(platforms) == 3
    assert all([type(nw) == Validator for nw in platforms.values()])
    twitter = platforms.get('Twitter')
    assert type(twitter.range) == range  # range upper limit = exclusive!
    assert isinstance(twitter.regex, Pattern)  # nope, no regex here ;)


def test_validate_username_wrong_validator():
    with pytest.raises(ValueError):
        validate_username('Github', 'bob')


def test_validate_username_twitter_range():
    assert validate_username('Twitter', 'a')
    assert not validate_username('Twitter', '')
    assert not validate_username('Twitter', 'a'*16)


def test_validate_username_twitter_regex():
    assert validate_username('Twitter', 'bob')
    assert validate_username('Twitter', 'boB123')
    assert validate_username('Twitter', 'bo__89A')
    assert not validate_username('Twitter', 'bob-123')
    assert not validate_username('Twitter', 'bob@PyBites')
    assert not validate_username('Twitter', 'bob.')


def test_validate_username_facebook_range():
    assert validate_username('Facebook', 'abc123')
    assert not validate_username('Facebook', 'bob')
    assert not validate_username('Facebook', 'a'*51)


def test_validate_username_facebook_regex():
    assert validate_username('Facebook', 'bobb.')
    assert validate_username('Facebook', 'bob.PyBites')
    assert validate_username('Facebook', 'aAbB123')
    assert not validate_username('Facebook', 'bobb,')
    assert not validate_username('Facebook', 'bob$56')
    assert not validate_username('Facebook', 'bob123_')


def test_validate_username_reddit_range():
    assert validate_username('Reddit', 'abc')
    assert not validate_username('Reddit', 'ab')
    assert not validate_username('Reddit', 'a'*21)


def test_validate_username_reddit_regex():
    assert validate_username('Reddit', 'bob_PyBites')
    assert validate_username('Reddit', '-123ABC')
    assert validate_username('Reddit', '123-abc__')
    assert not validate_username('Reddit', 'bobb.')
    assert not validate_username('Reddit', 'bob@PyBites')
    assert not validate_username('Reddit', 'bob$56')