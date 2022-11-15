class QueensProblem:

    def __init__(self, n):
        self.n = n
        self.chess_table = [[0 for i in range(n)] for j in range(n)]

    def solve_n_queens(self):

        # we start with the first queen (with index 0)
        if self.solve(0):
            self.print_queens()
        else:
            # when we have considered all the possible configurations without a success
            # then it means there is no solution (3x3 with 3 queens)
            print('There is no solution to the problem...')

    # col_index is the same as the index of the queen
    def solve(self, col_index):

        # we have solved the problem - base case
        if col_index == self.n:
            return True

        # let's try to find a position for queen (col_index) within a given column
        for row_index in range(self.n):
            if self.is_place_valid(row_index, col_index):
                # 1 means that there is a queen at the given location
                self.chess_table[row_index][col_index] = 1

                # we call the same function with col_index+1
                # we try to find the location of the next queen in the next column
                if self.solve(col_index+1):
                    return True

                # BACKTRACK
                print('BACKTRACKING ...')
                self.chess_table[row_index][col_index] = 0

        # when we have considered all the rows in a col without
        # finding a valid cell for the queen
        return False

    def is_place_valid(self, row_index, col_index):

        # check the rows (whether given queens can attack each other horizontally)
        # it means that there is already at least 1 queen in that given row
        for i in range(self.n):
            if self.chess_table[row_index][i] == 1:
                return False

        # we do not have to check the same column because we implement the problem
        # such that we assign 1 queen to every single column

        # we have to check the diagonals
        # from top left to bottom right
        j = col_index
        for i in range(row_index, -1, -1):

            if i < 0:
                break

            if self.chess_table[i][j] == 1:
                return False

            j = j - 1

        # we have to check the diagonals
        # from top right to bottom left
        j = col_index
        for i in range(row_index, self.n):

            if j < 0:
                break

            if self.chess_table[i][j] == 1:
                return False

            j = j - 1

        return True

    def print_queens(self):
        for i in range(self.n):
            for j in range(self.n):
                if self.chess_table[i][j] == 1:
                    print(' Q ', end='')
                else:
                    print(' - ', end='')
            print('\n')


if __name__ == '__main__':
    queens = QueensProblem(100)
    queens.solve_n_queens()
