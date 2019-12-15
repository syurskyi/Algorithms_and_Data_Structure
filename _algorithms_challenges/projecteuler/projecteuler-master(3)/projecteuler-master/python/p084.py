#!/usr/bin/env python

"""Problem 84: Monopoly odds"""

from heapq import nlargest
from random import choice, shuffle


class Dice:
    """Represents a pair of dice"""
    def __init__(self, sides=6):
        self.sides = sides
        self.rolls = [(i, j) for i in range(1, sides + 1)
                      for j in range(1, sides + 1)]

    def roll(self):
        return choice(self.rolls)


class Deck:
    """Represents a deck of Chance or Community Chest cards"""
    def __init__(self, size=16):
        self.size = size
        cards = list(range(size))
        shuffle(cards)
        self.cards = cards
        self.index = -1

    def draw(self):
        self.index = (self.index + 1) % self.size
        return self.cards[self.index]


def main():
    dice = Dice(sides=4)
    ch_deck = Deck()
    cc_deck = Deck()
    position = 0
    visits = [0]*40
    doubles = 0  # consecutive doubles

    for _ in range(1_000_000):
        roll = dice.roll()

        if roll[0] == roll[1]:
            if doubles == 2:
                doubles = 0
                position = 10
                visits[10] += 1
                continue
            doubles += 1
        else:
            doubles = 0

        score = roll[0] + roll[1]
        position = (position + score) % 40

        if position in (7, 22, 36):  # CH[123]
            card = ch_deck.draw()

            if card == 0:    # "Advance to GO"
                position = 0
            elif card == 1:  # "Go to JAIL"
                position = 10
            elif card == 2:  # "Go to C1"
                position = 11
            elif card == 3:  # "Go to E3"
                position = 24
            elif card == 4:  # "Go to H2"
                position = 39
            elif card == 5:  # "Go to R1"
                position = 5
            elif card == 6 or card == 7:  # "Go to next R" (there're two of these)
                if position == 7:
                    position = 15
                elif position == 22:
                    position = 25
                else:
                    position = 5
            elif card == 8:  # "Go to next U":
                if position == 22:
                    position = 28
                else:
                    position = 12
            elif card == 9:  # "Go back 3 squares":
                position -= 3

        # CC should be checked after CH to allow for moving back 3 from CH3
        if position in (2, 17, 33):  # CC[123]
            card = cc_deck.draw()

            if card == 0:    # "Advance to GO":
                position = 0
            elif card == 1:  # "Go to JAIL":
                position = 10
        elif position == 30:  # G2J
            position = 10

        visits[position] += 1

    return '{:02d}{:02d}{:02d}'.format(*nlargest(3, range(len(visits)),
                                                 key=visits.__getitem__))


if __name__ == '__main__':
    print(main())
