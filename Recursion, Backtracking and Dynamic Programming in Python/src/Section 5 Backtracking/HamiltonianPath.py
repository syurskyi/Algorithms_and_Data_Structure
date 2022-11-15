
class HamiltonianPath:

    def __init__(self, adjacency_matrix):
        self.n = len(adjacency_matrix)
        self.adjacency_matrix = adjacency_matrix
        self.path = [0]

    def hamiltonian_path(self):

        if self.solve(1):
            self.show_hamiltonian_path()
        else:
            print('There is no solution to the problem...')

    def solve(self, position):

        # BASE CASE
        if position == self.n:
            return True

        for vertex_index in range(1, self.n):
            if self.is_feasible(vertex_index, position):
                # we include vertex (with vertex_index) in the solution
                self.path.append(vertex_index)

                if self.solve(position+1):
                    return True

                # when we have to backtrack
                # we have to remove vertex_index from the result (path)
                self.path.pop()

        # if we have considered all the vertexes without a success
        return False

    def is_feasible(self, vertex, actual_position):

        # check whether is there a connection between the nodes
        if self.adjacency_matrix[self.path[actual_position-1]][vertex] == 0:
            return False

        # whether we have already included that given vertex in the result
        for i in range(actual_position):
            if self.path[i] == vertex:
                return False

        return True

    def show_hamiltonian_path(self):
        for v in self.path:
            print(v)


if __name__ == '__main__':

    m = [[0, 1, 0, 0, 0, 1],
         [1, 0, 1, 0, 0, 0],
         [0, 1, 0, 0, 1, 0],
         [0, 0, 0, 0, 1, 1],
         [0, 0, 1, 1, 0, 1],
         [1, 0, 0, 1, 1, 0]]

    hamiltonian_path = HamiltonianPath(m)
    hamiltonian_path.hamiltonian_path()
