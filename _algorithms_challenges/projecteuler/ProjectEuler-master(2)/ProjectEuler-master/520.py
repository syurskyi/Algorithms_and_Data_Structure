import sys

class Matrix():
    def multiply(self, x, y, mod):
        results = [[0 for j in range(len(y[0]))] for i in range(len(x))]
        for i in range(len(x)):
            for j in range(len(y[0])):
                for k in range(len(y)):
                    results[i][j] = (results[i][j] + x[i][k] * y[k][j]) % mod
        return results

    def power(self, x, power, mod):
        base = x
        rv = self.identity_matrix(len(x))
        while power > 0:
            if power & 1 == 1:
                rv = self.multiply(rv, base, mod)
            base = self.multiply(base, base, mod)
            power >>= 1
        return rv

    def identity_matrix(self, n):
        rv = [[0 for j in range(n)] for i in range(n)]
        for i in range(n):
            rv[i][i] = 1
        return rv

class Problem():
    def __init__(self):
        self.mod = 1000000123
        self.states = None
        self.inversed_states = None
        self.transition_matrix = None
        self.initial_state = None
        self.final_state = None

        self.__init_all()

    def solve(self):
        self.get(39)

    def get(self, n):
        count = 0
        x = self.transition_matrix
        for i in range(1, n + 1):
            y = Matrix().multiply(x, self.initial_state, self.mod)
            q = (Matrix().multiply(self.final_state, y, self.mod)[0][0] - 1) % self.mod
            count = (count + q) % self.mod
            print(i, '=>', q, '=>', count)
            if i < n:
                x = Matrix().multiply(x, x, self.mod)
                x = Matrix().multiply(x, self.transition_matrix, self.mod)
        print(count)

    def __init_all(self):
        states, inversed_states = self.__get_states()
        self.states = states
        self.inversed_states = inversed_states

        dim = len(states)
        transition_matrix = [[0 for j in range(dim)] for i in range(dim)]
        for curr_pos in range(dim):
            i, j, k, w, z = states[curr_pos]
            next_pos = inversed_states[(i, j, k, (w + 1) % 2, (z + 1) % 2)]
            transition_matrix[next_pos][curr_pos] += 1
            if k > 0:
                next_pos = inversed_states[(i, j, k - 1, w, 0)]
                transition_matrix[next_pos][curr_pos] += k
            if k < 4:
                next_pos = inversed_states[(i, j, k + 1, w, 0)]
                transition_matrix[next_pos][curr_pos] += 4 - k
            if i + j < 5:
                next_pos = inversed_states[(i, j + 1, k, w, 0)]
                transition_matrix[next_pos][curr_pos] += 5 - (i + j)
            if j > 0:
                next_pos = inversed_states[(i + 1, j - 1, k, w, 0)]
                transition_matrix[next_pos][curr_pos] += j
            if i > 0:
                next_pos = inversed_states[(i - 1, j + 1, k, w, 0)]
                transition_matrix[next_pos][curr_pos] += i
        self.transition_matrix = transition_matrix

        initial_state = [[0] for i in range(dim)]
        initial_state[inversed_states[(0, 1, 0, 0, 0)]][0] = 5
        initial_state[inversed_states[(0, 0, 1, 0, 0)]][0] = 4
        initial_state[inversed_states[(0, 0, 0, 1, 1)]][0] = 1
        self.initial_state = initial_state

        final_state = [[0 for i in range(dim)]]
        for j in range(5 + 1):
            final_state[0][inversed_states[(0, j, 0, 0, 0)]] = 1
            final_state[0][inversed_states[(0, j, 0, 1, 1)]] = 1
        self.final_state = final_state

    def __get_states(self):
        states = []
        for seen_odd_digits in range(0, 5 + 1):
            for i in range(seen_odd_digits + 1):
                j = seen_odd_digits - i
                for k in range(4 + 1):
                    for w in range(1 + 1):
                        for z in range(1 + 1):
                            states.append((i, j, k, w, z))

        inversed_states = {}
        for i in range(len(states)):
            inversed_states[states[i]] = i

        return states, inversed_states

def main():
    problem = Problem()
    problem.solve()

if __name__ == '__main__':
    sys.exit(main())
