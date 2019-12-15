import random
from collections import namedtuple
from math import ceil

LETTER_A_CODE = 65

ACTIONS = ['draw_card', 'play_again',
           'interchange_cards', 'change_turn_direction']
NUMBERS = range(1, 5)

PawCard = namedtuple('PawCard', 'card action')


def create_paw_deck(n=8):
    if n > 26:
        raise ValueError('maximum of 26 suits')
    deck = []
    for suit in range(n):
        deck.extend(f'{chr(LETTER_A_CODE + suit)}{x}' for x in NUMBERS)
    actions = list((ACTIONS * ceil(n / 4))[:n]) + ([None] * 3 * n)
    random.shuffle(actions)
    return [PawCard(card, action) for card, action in zip(deck, actions)]
