
class KnightsTour:

    def __init__(self, board_size):
        self.board_size = board_size
        # possible horizontal components of the moves
        self.x_moves = [2, 1, -1, -2, -2, -1, 1, 2]
        self.y_moves = [1, 2, 2, 1, -1, -2, -2, -1]
        self.solution_matrix = [[-1 for _ in range(self.board_size)] for _ in range(self.board_size)]

    def solve_problem(self):

        # we start with the top left cell
        self.solution_matrix[0][0] = 0

        # first parameter is the counter
        # the second and third parameter is the location (0, 0)
        if self.solve(1, 0, 0):
            self.print_solution()
        else:
            print('There is no feasible solution...')

    def solve(self, step_counter, x, y):

        # base case
        if step_counter == self.board_size * self.board_size:
            return True

        # we have to consider all the possible moves and find the valid one
        for move_index in range(len(self.x_moves)):

            next_x = x + self.x_moves[move_index]
            next_y = y + self.y_moves[move_index]

            if self.is_valid_move(next_x, next_y):
                # it is a valid step so we can update the solution_matrix
                self.solution_matrix[next_x][next_y] = step_counter

                if self.solve(step_counter+1, next_x, next_y):
                    return True

                # BACKTRACK AS USUAL - we have to remove the step and
                # reinitialize the solution_matrix with -1
                self.solution_matrix[next_x][next_y] = -1

        return False

    def is_valid_move(self, x, y):

        # that the knight will not step outside the chessboard
        # the knight leaves the board horizontally
        if x < 0 or x >= self.board_size:
            return False

        # the knight leaves the board vertically
        if y < 0 or y >= self.board_size:
            return False

        # maybe we have already visited that given cell
        # which means that the value is not -1
        if self.solution_matrix[x][y] > -1:
            return False

        return True

    def print_solution(self):
        for i in range(self.board_size):
            for j in range(self.board_size):
                print(self.solution_matrix[i][j], end=' ')
            print('\n')


if __name__ == '__main__':

    # for small values backtracking is fast
    tour = KnightsTour(8)
    tour.solve_problem()
