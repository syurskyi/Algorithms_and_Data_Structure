class MazeProblem:

    def __init__(self, maze_matrix):
        self.maze_matrix = maze_matrix
        self.maze_size = len(maze_matrix)
        self.solution_matrix = [[' - ' for _ in range(self.maze_size)] for _ in range(self.maze_size)]
        self.moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def solve_problem(self):

        # we start with (0,0)
        self.solution_matrix[0][0] = ' S '

        if self.solve(0, 0):
            self.show_result()
        else:
            print('There is no feasible solution...')

    def solve(self, x, y):

        if self.is_finished(x, y):
            return True

        for move in self.moves:

            next_x = x + move[0]
            next_y = y + move[1]

            if self.is_valid(next_x, next_y):
                self.solution_matrix[next_x][next_y] = ' S '

                if self.solve(next_x, next_y):
                    return True

                # BACKTRACK
                self.solution_matrix[next_x][next_y] = ' '

        return False

    def is_valid(self, x, y):

        # we do not step out of the board
        # horizontally and then vertically
        if x < 0 or x >= self.maze_size:
            return False

        if y < 0 or y >= self.maze_size:
            return False

        # there may be obstacles (we are not able to use cells that are obstacles)
        # 0 represents obstacles !!!
        if self.maze_matrix[x][y] == 0:
            return False

        # let's check whether we have already included that cell in the solution
        if self.solution_matrix[x][y] == ' S ':
            return False

        return True

    def is_finished(self, x, y):
        if x == self.maze_size - 1 and y == self.maze_size - 1:
            return True

    def show_result(self):
        for x in range(self.maze_size):
            for y in range(self.maze_size):
                print(self.solution_matrix[x][y], end=' ')
            print('\n')


if __name__ == '__main__':

    # 1: valid cells 0: walls or obstacles
    maze = [[1, 1, 1, 1, 1],
            [0, 0, 0, 0, 1],
            [1, 0, 1, 0, 1],
            [1, 0, 1, 0, 1],
            [1, 1, 1, 0, 1]]

    maze = MazeProblem(maze)
    maze.solve_problem()
