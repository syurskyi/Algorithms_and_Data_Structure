import pytest

from speaker import (get_pycon_speaker_first_names,
                     get_percentage_of_female_speakers)


@pytest.fixture(scope='module')
def first_names():
    return get_pycon_speaker_first_names()


def test_get_pycon_speaker_first_names(first_names):
    assert len(first_names) == 112
    assert 'Luciano' in first_names
    assert 'Erin' in first_names
    assert 'Rachael' in first_names


def test_get_percentage_of_female_speakers(first_names):
    actual = get_percentage_of_female_speakers(first_names)
    expected = 28.57
    assert actual == expected