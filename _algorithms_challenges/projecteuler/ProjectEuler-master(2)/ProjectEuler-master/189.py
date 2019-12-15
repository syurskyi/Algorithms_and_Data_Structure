import itertools
import sys

class Problem():
    def __init__(self):
        self.color = ["r", "g", "b"]
        self.color_count = len(self.color)
        self.small_cases = self.__init_small_cases()

    def solve(self):
        print(self.get(8))

    def get(self, n):
        coloring_rows_map = self.__generate_coloring_rows_map(n)
        counting_rows_map = self.__generate_counting_rows_map(n)
        for i in range(2, n + 1):
            for prev_row_pos in range(len(coloring_rows_map[i - 1])):
                prev_row = coloring_rows_map[i - 1][prev_row_pos]
                for curr_row_pos in range(len(coloring_rows_map[i])):
                    curr_row = coloring_rows_map[i][curr_row_pos]
                    sub_case_count = 1
                    for j in range(i - 1):
                        sub_case_count *= self.small_cases[prev_row[j] + curr_row[j] + curr_row[j + 1]]
                        if sub_case_count == 0:
                            break
                    counting_rows_map[i][curr_row_pos] += sub_case_count * counting_rows_map[i - 1][prev_row_pos]
            print("Current =>", i, sum(counting_rows_map[i]))
        return sum(counting_rows_map[n])

    def __init_small_cases(self):
        cases = {}
        for n in itertools.product(self.color, repeat=self.color_count):
            cases[''.join(n)] = self.color_count - len(set(n))
        return cases

    def __generate_coloring_rows_map(self, bound):
        rows_map = {}
        for n in range(1, bound + 1):
            rows_map[n] = list(itertools.product(self.color, repeat=n))
        return rows_map

    def __generate_counting_rows_map(self, bound):
        rows_map = {}
        rows_map[1] = [1 for _ in range(self.color_count)]
        for n in range(2, bound + 1):
            rows_map[n] = [0 for _ in range(self.color_count**n)]
        return rows_map

def main():
    problem = Problem()
    problem.solve()

if __name__ == '__main__':
    sys.exit(main())
