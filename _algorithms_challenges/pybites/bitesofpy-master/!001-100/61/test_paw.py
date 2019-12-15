from collections import Counter

import pytest

from paw import create_paw_deck


@pytest.fixture(scope="module")
def deck():
    return list(create_paw_deck())


@pytest.fixture(scope="module")
def small_deck():
    return list(create_paw_deck(4))


@pytest.fixture(scope="module")
def big_deck():
    return list(create_paw_deck(16))


def test_deck_size(deck, small_deck, big_deck):
    assert len(deck) == 32
    assert len(small_deck) == 16
    assert len(big_deck) == 64


def test_number_action_cards(deck, small_deck, big_deck):
    assert sum(1 for card in deck if card.action is not None) == 8
    assert sum(1 for card in deck if card.action is None) == 24

    assert sum(1 for card in small_deck if card.action is not None) == 4
    assert sum(1 for card in small_deck if card.action is None) == 12

    assert sum(1 for card in big_deck if card.action is not None) == 16
    assert sum(1 for card in big_deck if card.action is None) == 48


def test_all_action_cards_used(deck, small_deck, big_deck):
    cards = [card.action for card in deck if card.action is not None]
    assert sum(Counter(cards).values()) == 8

    cards = [card.action for card in small_deck if card.action is not None]
    assert sum(Counter(cards).values()) == 4

    cards = [card.action for card in big_deck if card.action is not None]
    assert sum(Counter(cards).values()) == 16


def test_action_cards_in_different_positions(deck):
    action_cards = [card.card for card in deck if card.action is not None]

    deck2 = list(create_paw_deck())
    action_cards2 = [card.card for card in deck2 if card.action is not None]
    assert action_cards != action_cards2

    deck3 = list(create_paw_deck())
    action_cards3 = [card.card for card in deck3 if card.action is not None]
    assert action_cards != action_cards2 != action_cards3


def test_deck_cards_numbers_constant(deck, small_deck, big_deck):
    for i in list('ABCDEFGH'):
        assert sum(1 for card in deck if card.card[0] == i) == 4
    for i in list('ABCD'):
        assert sum(1 for card in small_deck if card.card[0] == i) == 4
    for i in list('ABCDEFGHIJKLMNOP'):
        assert sum(1 for card in big_deck if card.card[0] == i) == 4


def test_deck_numbers_used():
    for i in range(1, 27):
        deck = list(create_paw_deck(i))
        assert sum(1 for card in deck if int(card.card[1:]) == 1) == i


def test_out_of_bound_arg():
    with pytest.raises(ValueError):
        create_paw_deck(n=27)