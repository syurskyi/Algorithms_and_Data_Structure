from dataclasses import dataclass
from functools import total_ordering
from typing import List

bites: List[int] = [283, 282, 281, 263, 255, 230, 216, 204, 197, 196, 195]
names: List[str] = [
    "snow",
    "natalia",
    "alex",
    "maquina",
    "maria",
    "tim",
    "kenneth",
    "fred",
    "james",
    "sara",
    "sam",
]


@dataclass
@total_ordering
class Ninja:
    """
    The Ninja class will have the following features:

    string: name
    integer: bites
    support <, >, and ==, based on bites
    print out in the following format: [469] bob
    """
    name: str
    bites: int

    def __lt__(self, other):
        return self.bites < other.bites

    def __eq__(self, other):
        return self.bites == other.bites

    def __str__(self):
        return f'[{self.bites}] {self.name}'


@dataclass
class Rankings:
    """
    The Rankings class will have the following features:

    method: add() that adds a Ninja object to the rankings
    method: dump() that removes/dumps the lowest ranking Ninja from Rankings
    method: highest() returns the highest ranking Ninja, but it takes an optional
            count parameter indicating how many of the highest ranking Ninjas to return
    method: lowest(), the same as highest but returns the lowest ranking Ninjas, also
            supports an optional count parameter
    returns how many Ninjas are in Rankings when len() is called on it
    method: pair_up(), pairs up study partners, takes an optional count
            parameter indicating how many Ninjas to pair up
    returns List containing tuples of the paired up Ninja objects
    """
    ninja_list = []

    def add(self, ninja):
        if ninja not in self.ninja_list:
            self.ninja_list.append(ninja)
        self.ninja_list.sort()

    def dump(self):
        return self.ninja_list.pop(0)

    def highest(self, count: int = 1):
        result = self.ninja_list[-count:]
        result.reverse()
        return result

    def lowest(self, count: int = 1):
        result = self.ninja_list[:count]
        return result

    def pair_up(self, count: int = 3):
        highest = self.highest(count)
        lowest = self.lowest(count)
        return list(zip(highest, lowest))

    def __len__(self):
        return len(self.ninja_list)
