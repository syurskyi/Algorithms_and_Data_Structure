class Account:

    def __init__(self, name, start_balance=0):
        self.name = name
        self.start_balance = start_balance
        self._transactions = []

    @property
    def balance(self):
        return self.start_balance + sum(self._transactions)

    def __len__(self):
        return len(self._transactions)

    def __lt__(self, other):
        if not isinstance(other, Account):
            raise ValueError()
        return self.balance < other.balance

    def __gt__(self, other):
        if not isinstance(other, Account):
            raise ValueError()
        return self.balance > other.balance

    def __eq__(self, other):
        if not isinstance(other, Account):
            raise ValueError()
        return self.balance == other.balance

    def __le__(self, other):
        if not isinstance(other, Account):
            raise ValueError()
        return self.balance <= other.balance

    def __ge__(self, other):
        if not isinstance(other, Account):
            raise ValueError()
        return self.balance >= other.balance

    def __getitem__(self, item):
        return self._transactions[item]

    def __add__(self, other):
        if not isinstance(other, int):
            raise ValueError
        self._transactions.append(other)

    def __sub__(self, other):
        if not isinstance(other, int):
            raise ValueError
        self._transactions.append(-other)

    def __str__(self):
        return f'{self.name} account - balance: {self.balance}'
