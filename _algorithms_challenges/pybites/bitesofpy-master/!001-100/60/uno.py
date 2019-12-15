from collections import namedtuple

SUITS = 'Red Green Yellow Blue'.split()

UnoCard = namedtuple('UnoCard', 'suit name')

SUIT_VALUES = '1,2,3,4,5,6,7,8,9,Draw Two,Skip,Reverse'.split(',')


def create_uno_deck():
    """Create a deck of 108 Uno cards.
       Return a list of UnoCard namedtuples
       (for cards w/o suit use None in the namedtuple)"""
    cards = []
    for suit in SUITS:
        add_suit(cards.append, suit)
    for value in 'Wild,Wild Draw Four'.split(',') * 4:
        cards.append(UnoCard(None, value))
    return cards


def add_suit(cards_append, suit: str):
    cards_append(UnoCard(suit, '0'))
    for value in SUIT_VALUES:
        cards_append(UnoCard(suit, value))
        cards_append(UnoCard(suit, value))
