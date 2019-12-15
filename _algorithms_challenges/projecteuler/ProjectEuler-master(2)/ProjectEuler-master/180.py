import itertools
import fractions
import sys

class Problem():
    def __init__(self):
        self.n_solutions = [-2, -1, 1, 2]
        self.keys = None
        self.numbers = None

    def __init_keys(self, order):
        self.keys = set()
        for a, b in itertools.combinations(range(1, order + 1), 2):
            self.keys.add(fractions.Fraction(a, b))
        self.keys = sorted(list(self.keys))

    def __init_numbers(self, order):
        self.__init_keys(order)
        self.numbers = {}
        for n in self.n_solutions:
            self.numbers[n] = {}
            for key in self.keys:
                self.numbers[n][key**n] = key

    def solve(self):
        result = self.get(35)
        print("answer =>", result.numerator + result.denominator)
        print("exact rational number =>", result)

    def get(self, order):
        self.__init_numbers(order)
        final_result = set()
        for n in self.n_solutions:
            sub_result = self.__get_golden_triple(n)
            final_result |= sub_result
            print(n, "=>", len(sub_result), len(final_result))
        return sum(final_result)

    def __get_golden_triple(self, n):
        result = set()
        for x, y in itertools.combinations_with_replacement(self.numbers[n], 2):
            z = x + y
            if z in self.numbers[n]:
                result.add(self.numbers[n][x] + self.numbers[n][y] + self.numbers[n][z])
        return result

def main():
    problem = Problem()
    problem.solve()
    
if __name__ == '__main__':
    sys.exit(main())
