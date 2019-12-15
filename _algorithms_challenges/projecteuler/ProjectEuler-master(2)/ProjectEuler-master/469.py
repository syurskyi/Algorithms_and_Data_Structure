from fractions import Fraction
import math
import sys

class Problem():
    def solve(self):
        N = 100
        linear_table_expected_values = [Fraction(0), Fraction(0), Fraction(1)]
        for i in range(3, N + 1):
            expected_value = (i - 1) * 2
            expected_value += 2 * linear_table_expected_values[i - 2]
            for j in range(i - 3 + 1):
                expected_value += linear_table_expected_values[j]
                expected_value += linear_table_expected_values[i - 3 - j]
            expected_value /= i
            linear_table_expected_values.append(expected_value)

        for i in range(3, N + 1):
            round_table_expected_value = (linear_table_expected_values[i - 3] + 2) / i
            print(i, '=>', float(round_table_expected_value))            

def main():
    problem = Problem()
    problem.solve()

if __name__ == '__main__':
    sys.exit(main())
