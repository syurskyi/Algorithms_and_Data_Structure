import sys

class ExtendedGCD():
    def solve(a, b):
        x, y = 0, 1
        last_x, last_y = 1, 0
        while b != 0:
            q, r = divmod(a, b)
            a, b = b, r
            x, last_x = last_x - q * x, x
            y, last_y = last_y - q * y, y
        return last_x, last_y

# Solve x = a_i (mod n_i) where n_i are coprime.
class ChineseRemainderTheorem():
    def solve(a_list, n_list):
        a = a_list[0]
        m = n_list[0]
        for i in range(1, len(n_list)):
            n = n_list[i]
            b = a_list[i]
            q = m * n
            x, y = ExtendedGCD.solve(m, n)
            root = (a + (b - a) * x * m) % q
            a, m = root, q
        return a

# Solve ax = 1 (mod m).
class ModInverse():
    def solve(a, m):
        x, y = ExtendedGCD.solve(a, m)
        return x % m

class Problem():
    def __init__(self):
        self.inverse_fifteen = ModInverse.solve(15, 17**7)

    def solve(self):
        self.benchmark()
        print(self.get(10**18))

    def benchmark(self):
        assert(self.get_naive(4) == 82)
        assert(self.get_naive(10**9) == 126897180)

    def get_naive(self, n):
        x = pow(2, n, 17**7)
        return (2 * self.inverse_fifteen * (x - 1) * (3 * x - 7)) % 17**7

    def get(self, k):
        reduced_e = k % (16 * 17**5)
        a = pow(10, reduced_e, 17**6)
        reduced_n = ChineseRemainderTheorem.solve([0, a], [16, 17**6])
        x = pow(2, reduced_n, 17**7)
        return (2 * self.inverse_fifteen * (x - 1) * (3 * x - 7)) % 17**7

def main():
    problem = Problem()
    problem.solve()

if __name__ == '__main__':
    sys.exit(main())
