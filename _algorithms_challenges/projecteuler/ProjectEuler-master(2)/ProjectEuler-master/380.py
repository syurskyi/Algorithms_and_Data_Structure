import math
import sys

class Problem():
    def solve(self):
        self.benchmark()
        print(self.get_log(500, 100))

    def benchmark(self):
        assert(round(self.get(1, 1)) == 1)
        assert(round(self.get(2, 2)) == 4)
        assert(round(self.get(3, 4)) == 2415)

        exponent, coefficient = self.get_log(9, 12)
        assert(exponent == 46)
        assert(coefficient == 2.572)

    def get_log(self, m, n):
        result = 0
        for h in range(1, m):
            x = self.__sigma(h, m)
            for k in range(1, n):
                y = self.__sigma(k, n)
                result += math.log10(x + y)
        exponent = int(result)
        coefficient = round(pow(10, result - exponent), 4)
        return exponent, coefficient

    def get(self, m, n):
        result = 1
        for h in range(1, m):
            x = self.__sigma(h, m)
            for k in range(1, n):
                y = self.__sigma(k, n)
                result *= (x + y)
        return result

    def __sigma(self, k, n):
        return 4 * math.sin((k * math.pi)/ (2 * n))**2

def main():
    problem = Problem()
    problem.solve()

if __name__ == '__main__':
    sys.exit(main())
