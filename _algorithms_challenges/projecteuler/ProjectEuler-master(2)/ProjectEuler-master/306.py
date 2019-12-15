import bisect
import itertools
import sys

class GameStateMapBuilder():
    def __init__(self, n):
        self.n = n
        self.solution_vector = [0 for _ in range(n)]
        self.values = {}
        self.__init_values()
        self.__backtrack(0)

    def get(self):
        return self.values

    def __init_values(self):
        for i in range(self.n + 1):
            self.values[i] = set()

    def __backtrack(self, dim):
        if dim >= self.n:
            return
        for i in range(self.n + 1):
            self.solution_vector[dim] = i
            paper_length = self.__get_paper_length(dim)
            left_length = self.n - paper_length
            if left_length < 0:
                break
            game_state = tuple(self.solution_vector[:dim + 1] + [0 for i in range(dim + 1, self.n)])
            self.values[paper_length].add(game_state)
            if left_length > dim + 1:
                self.__backtrack(dim + 1)

    def __get_paper_length(self, dim):
        result = 0
        for i in range(dim + 1):
            result += (i + 1) * self.solution_vector[i]
        return result

class Game():
    def get(self, n):
        builder = GameStateMapBuilder(n)
        game_state_map = builder.get()
        winning_states = set()
        for i in range(n + 1):
            for state in game_state_map[i]:
                if state in winning_states:
                    continue
                prev_states = self.__search_perv_states(state, n)
                winning_states |= prev_states

        losing_strips = []
        for i in range(n):
            state = [0 for _ in range(n)]
            state[i] = 1
            state = tuple(state)
            if state not in winning_states:
                losing_strips.append(i + 1)
        return losing_strips

    def __search_perv_states(self, state, n):
        result = set()

        prev_state = list(state)
        prev_state[1] += 1
        result.add(tuple(prev_state))

        for i in range(n - 2):
            if state[i] < 1:
                continue
            prev_state = list(state)
            prev_state[i] -= 1
            prev_state[i + 2] += 1
            result.add(tuple(prev_state))

        for i in range(n):
            for j in range(i, n - i - 3):
                if i == j:
                    if state[i] < 2:
                        continue
                else:
                    if state[i] < 1 or state[j] < 1:
                        continue
                prev_state = list(state)
                prev_state[i] -= 1
                prev_state[j] -= 1
                prev_state[i + j + 3] += 1
                result.add(tuple(prev_state))
        return result

class Problem():
    def solve(self):
        for n in [5, 50, 1000000]:
            print(n, '=>', self.get(n))

    def benchmark(self):
        losing_strips = Game().get(50)
        print(losing_strips)

    def get(self, n):
        losing_strips = [1, 5, 9, 15, 21, 25, 29, 35, 39, 43, 55, 59, 63]
        if n <= 63:
            return n - bisect.bisect(losing_strips, n)
        while True:
            last = losing_strips[-5] + 34
            if last > n:
                break
            losing_strips.append(last)
        return n - len(losing_strips)

def main():
    problem = Problem()
    problem.solve()

if __name__ == '__main__':
    sys.exit(main())
