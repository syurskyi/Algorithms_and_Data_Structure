from collections import namedtuple
from datetime import datetime

Transaction = namedtuple('Transaction', 'giver points date')
Transaction.__new__.__defaults__ = (datetime.now(),)  # http://bit.ly/2rmiUrL


class User:
    def __init__(self, name: str):
        self._name = name
        self._transactions = []

    def __str__(self):
        return f"{self.name} has a karma of {self.karma} and {self.fans} fan{'s' if self.fans > 1 else ''}"

    def __add__(self, other: Transaction):
        if not isinstance(other, Transaction):
            raise TypeError('Can only add a transaction')
        self._transactions.append(other)

    @property
    def name(self) -> str:
        return self._name

    @property
    def fans(self) -> int:
        return len({x.giver for x in self._transactions})

    @property
    def points(self) -> list:
        return [x.points for x in self._transactions]

    @property
    def karma(self) -> int:
        return sum(self.points)
