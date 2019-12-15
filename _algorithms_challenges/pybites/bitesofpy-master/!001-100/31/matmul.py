class Matrix(object):

    def __init__(self, values):
        self._values = values

    def __repr__(self):
        return f'<Matrix values="{self.values}">'

    @property
    def values(self):
        return self._values

    @staticmethod
    def _matrix_mult(mat1, mat2):
        result = [([sum(a * b for a, b in zip(x, y)) for y in zip(*mat2)]) for x in mat1]
        return result

    def __matmul__(self, other):
        return Matrix(self._matrix_mult(self.values, other.values))

    def __rmatmul__(self, other):
        return Matrix(self._matrix_mult(other.values, self.values))

    def __imatmul__(self, other):
        self._values = self._matrix_mult(self.values, other.values)
        return self
