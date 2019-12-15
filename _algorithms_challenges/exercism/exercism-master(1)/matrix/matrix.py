class Matrix:
    def __init__(self, matrix_string):
        self.rows = list(
            list(map(lambda x: int(x), _.split(" "))) for _ in matrix_string.split("\n")
        )

    def row(self, index):
        return self.rows[index - 1]

    def column(self, index):
        return list(row[index - 1] for row in self.rows)
