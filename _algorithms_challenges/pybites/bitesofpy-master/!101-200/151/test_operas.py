import pytest

from operas import operas_both_at_premiere


def test_wagner_verdi():
    # materializing to list to support generator as return
    wagner_verdi = list(operas_both_at_premiere("wagner", "verdi"))
    assert len(wagner_verdi) == 10
    assert "Otello" not in wagner_verdi


def test_verdi_wagner():
    verdi_wagner = list(operas_both_at_premiere("verdi", "wagner"))
    assert len(verdi_wagner) == 11

    # premiere after Wagner's death (composed in 1833)
    assert "The Fairies" not in verdi_wagner


def test_beethoven_wagner():
    beethoven_wagner = list(operas_both_at_premiere("beethoven", "wagner"))
    assert len(beethoven_wagner) == 0


def test_wagner_beethoven():
    wagner_beethoven = list(operas_both_at_premiere("wagner", "beethoven"))
    assert len(wagner_beethoven) == 0


def test_beethoven_mozart():
    beethoven_mozart = list(operas_both_at_premiere("beethoven", "mozart"))
    assert len(beethoven_mozart) == 5
    assert "Apollo and Hyacinth" not in beethoven_mozart


def test_non_listed_composer():
    with pytest.raises(ValueError):
        list(operas_both_at_premiere("verdi", "dvorak"))


def test_non_listed_guest():
    # a guest must be in the list of composers
    with pytest.raises(ValueError):
        list(operas_both_at_premiere("dvorak", "verdi"))