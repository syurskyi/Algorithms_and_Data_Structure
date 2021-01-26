
class ColoringProblem:

    def __init__(self, adjacency_matrix, num_colors):
        self.n = len(adjacency_matrix)
        self.adjacency_matrix = adjacency_matrix
        self.num_colors = num_colors
        self.colors = [0 for _ in range(self.n)]

    def coloring_problem(self):

        # we call the solve with first vertex (index 0)
        if self.solve(0):
            self.show_result()
        else:
            print('There is no feasible solution...')

    def solve(self, node_index):

        if node_index == self.n:
            return True

        # consider the colors
        for color_index in range(1, self.num_colors+1):
            if self.is_color_valid(node_index, color_index):
                self.colors[node_index] = color_index

                if self.solve(node_index+1):
                    return True

                # BACKTRACKING
                # in this case backtracking means doing "nothing"

        return False

    def is_color_valid(self, node_index, color_index):

        # we have to check that the nodes are connected
        # AND we have to check that the given color is not shared
        # with these adjacent nodes
        for i in range(self.n):
            if self.adjacency_matrix[node_index][i] == 1 and color_index == self.colors[i]:
                return False

        return True

    def show_result(self):
        for v, c in zip(range(self.n), self.colors):
            print('Node %d has color value %d' % (v, c))


if __name__ == '__main__':

    m = [[0, 1, 1, 1],
         [1, 0, 1, 0],
         [1, 1, 0, 1],
         [1, 0, 1, 0]]

    problem = ColoringProblem(m, 3)
    problem.coloring_problem()
