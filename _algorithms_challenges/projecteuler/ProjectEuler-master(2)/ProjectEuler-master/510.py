import bisect
import fractions
import itertools
import math
import sys

class Problem():
    def solve(self):
        for n in [5, 100, 10**9]:
            print(n, '=>', self.get(n))

    def get(self, n):
        bound = int(math.sqrt(n)) + 1
        square_divisors = self.__get_square_divisors(bound)
        result = 0
        for i in range(1, bound + 1):
            if i**2 > n:
                break
            begin_pos = bisect.bisect(square_divisors[i - 1], i)
            end_pos = bisect.bisect(square_divisors[i - 1], 2 * i)
            for d in square_divisors[i - 1][begin_pos:end_pos]:
                a = i**2
                b = (d - i)**2
                c = a * b // d**2
                g = fractions.gcd(fractions.gcd(a, b), c)
                if g > 1:
                    continue
                f = n // a
                result += (a + b + c) * f * (f + 1) // 2
                #print('(a, b, c) =>', a, b, c)
        return result

    def __get_square_divisors(self, n):
        factorization = [[] for _ in range(n + 1)]
        d = [_ for _ in range(n + 1)]
        for i in range(2, n + 1):
            if factorization[i]:
                continue
            for j in range(i, n + 1, i):
                e = 0
                while d[j] % i == 0:
                    d[j] = d[j] // i
                    e += 1
                factorization[j].append((i, e))

        result = [[1]]
        for i in range(2, n + 1):
            unpacking = [[p**j for j in range(2 * e + 1)] for p, e in factorization[i]]
            all_divisors = sorted([self.__product(divisor) for divisor in itertools.product(*unpacking)])
            result.append(all_divisors)
        return result

    def __product(self, list):
        result = 1
        for number in list:
            result *= number
        return result

def main():
    problem = Problem()
    problem.solve()

if __name__ == '__main__':
    sys.exit(main())
