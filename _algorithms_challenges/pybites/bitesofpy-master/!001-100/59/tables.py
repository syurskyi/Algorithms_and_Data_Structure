class MultiplicationTable:

    def __init__(self, length):
        """Create a 2D self._table of (x, y) coordinates and
           their calculations (form of caching)"""
        self._len = length
        self._table = [[x * y for x in range(1, length + 1)] for y in range(1, length + 1)]

    def __len__(self):
        """Returns the area of the table (len x* len y)"""
        return len(self._table) * len(self._table[0])

    def __str__(self):
        """Returns a string representation of the table"""
        return '\n'.join(' | '.join([str(x) for x in y]) for y in self._table)

    def calc_cell(self, x, y):
        """Takes x and y coords and returns the (pre-calculated) result"""
        if x > self._len or y > self._len:
            raise IndexError()
        return self._table[x - 1][y - 1]
