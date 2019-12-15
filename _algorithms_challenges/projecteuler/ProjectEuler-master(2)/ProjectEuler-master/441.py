import itertools
import fractions
import sys

class PrimeFactorTable():
    def __init__(self, sieve_range):
        self.values = [[] for _ in range(sieve_range + 1)]
        for i in range(2, sieve_range + 1):
            if not self.values[i]:
                for j in range(i, sieve_range + 1, i):
                    self.values[j].append(i)
    
    def get(self, n):
        return self.values[n]

class HarmonicSum():
    def __init__(self, bound):
        self.table = PrimeFactorTable(bound)
        self.values = self.__init_values(bound)

    def __init_values(self, bound):
        result = [0.0]
        for i in range(1, bound + 1):
            result.append(result[-1] + 1 / i)
        return result

    def get_coprime_sum(self, lower_bound, upper_bound, n):
        result = self.__get_sum(lower_bound, upper_bound)
        factor_list = self.table.get(n)
        for i in range(1, len(factor_list) + 1):
            for sub_list in itertools.combinations(factor_list, i):
                n = self.__product(sub_list)
                sub_lower_bound = (lower_bound - 1) // n + 1
                sub_upper_bound = upper_bound // n
                sub_sum = self.__get_sum(sub_lower_bound, sub_upper_bound) / n * (-1)**i
                result += sub_sum
                #print(sub_list, n, "=>", sub_lower_bound, sub_upper_bound)
        #print("get_coprime_sum =>", lower_bound, upper_bound, "with", n, factor_list, "=>", result)
        return result

    def __get_sum(self, lower_bound, upper_bound):
        if lower_bound > upper_bound:
            return 0
        elif lower_bound == 0:
            return self.values[upper_bound]
        else:
            return self.values[upper_bound] - self.values[lower_bound - 1]

    def __product(self, number_list):
        result = 1
        for n in number_list:
            result *= n
        return result

class Problem():
    def solve(self):
        for n in [2, 10, 100, 10**7]:
            print(n, "=>", self.get(n))

    def get(self, bound):
        harmonic_sum = HarmonicSum(bound)        
        result = 0.0
        for p in range(1, bound // 2):
            result += harmonic_sum.get_coprime_sum(p + 1, bound - p - 1, p) * (p + 1) / p
        for q in range(bound // 2 + 1, bound + 1):
            result += harmonic_sum.get_coprime_sum(bound - q, q - 1, q) * (bound + 1 - q) / q
        return result

    def get_naive(self, bound):
        result = 0.0
        stack = [(0, 1, 1, 1)]
        while stack:
            a, b, c, d = stack.pop()
            p = a + c
            q = b + d
            if q > bound:
                continue
            count = min(bound, p + q) - q + 1
            result += count / (p * q)
            stack.append((a, b, p, q))
            stack.append((p, q, c, d))
        return result

def main():
    problem = Problem()
    problem.solve()

if __name__ == '__main__':
    sys.exit(main())
