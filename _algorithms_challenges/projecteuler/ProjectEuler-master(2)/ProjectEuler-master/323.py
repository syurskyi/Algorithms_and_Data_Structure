from fractions import Fraction
import sys

class Problem():
    def solve(self):
        expected_value = Fraction(0)
        for i in range(200):
            prob = Fraction(1) - (Fraction(1) - Fraction(1, 2**i))**32
            expected_value += prob
        print(float(expected_value))
    
def main():
    problem = Problem()
    problem.solve()
    
if __name__ == '__main__':
    sys.exit(main())
