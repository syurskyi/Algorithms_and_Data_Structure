import sys

class Factorial():
    def __init__(self, bound):
        self.values = self.__init_values(bound)

    def __init_values(self, bound):
        values = [1]
        for i in range(1, bound + 1):
            values.append(values[-1] * i)
        return values

class Divisor():
    def __init__(self, bound):
        self.values = self.__init_values(bound)

    def __init_values(self, bound):
        values = [[] for i in range(bound + 1)]
        for i in range(1, bound + 1):
            for j in range(i, bound + 1, i):
                values[j].append(i)
        return values

class EulerTotientFunction():
    def __init__(self, bound):
        self.values = self.__init_values(bound)

    def __init_values(self, bound):
        values = [i for i in range(bound + 1)]
        for i in range(2, bound + 1):
            if values[i] != i:
                continue
            for j in range(i, bound + 1, i):
                values[j] = values[j] - values[j] // i
        return values

class Problem():
    def __init__(self):
        self.factorial = Factorial(100)
        self.divisor = Divisor(100)
        self.euler_totient_function = EulerTotientFunction(100)

    def solve(self):
        print(self.get(10**15))

    def get(self, bound):
        return self.get_trivial_case(bound) + self.get_nontrivial_case(bound)

    def get_trivial_case(self, bound):
        result = 0
        m = 2
        while True:
            x = self.f(m, 1)
            if x > bound:
                break
            else:
                print('''f(%d, %d) = %d'''%(m, 1, x))
                result += x
                m += 1
        return result

    def get_nontrivial_case(self, bound):
        result = 0
        m = 2
        while True:
            n = 2
            while True:
                x = self.f(m, n)
                if x > bound:
                    break
                else:
                    print('''f(%d, %d) = %d'''%(m, n, x))
                    result += x
                    n += 1
            if n == 2:
                break
            else:
                m += 1
        return result

    def f(self, m, n):
        if n == 1:
            return self.factorial.values[m - 1]

        result = 0
        n_divisor = self.divisor.values[n]
        for d in n_divisor:
            result += self.factorial.values[d * m] // (self.factorial.values[d])**m * self.euler_totient_function.values[n // d]
        result = result // (m * n)
        return result

def main():
    problem = Problem()
    problem.solve()

if __name__ == '__main__':
    sys.exit(main())
