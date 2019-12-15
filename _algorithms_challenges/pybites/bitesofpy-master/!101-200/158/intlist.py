from decimal import Decimal


class IntList(list):
    def __init__(self, numbers):
        numbers = self._validate(numbers)
        super().__init__(numbers)

    def _validate(self, numbers):
        if isinstance(numbers, (int, float, Decimal)):
            numbers = [numbers]
        numbers = [int(n) for n in numbers if round(n, 0) == int(n)]
        if not isinstance(numbers, int) and any(not isinstance(x, int) for x in numbers):
            raise TypeError(f'{self.__class__.__name__} can only operate with integer values')
        return numbers

    def _elements(self):
        return [int(i) for i in super().copy()]

    @property
    def mean(self):
        elems = self._elements()
        return sum(elems) / len(elems)

    @property
    def median(self):
        elems = self._elements()
        elems.sort()
        n = len(elems)
        return (sum(elems[n // 2 - 1:n // 2 + 1]) / 2.0, elems[n // 2])[n % 2] if n > 0 else None

    def append(self, numbers):
        self._validate(numbers)
        super().append(numbers)

    def __add__(self, numbers):
        self._validate(numbers)
        return super().__add__(numbers)

    def __iadd__(self, numbers):
        self._validate(numbers)
        return super().__iadd__(numbers)
