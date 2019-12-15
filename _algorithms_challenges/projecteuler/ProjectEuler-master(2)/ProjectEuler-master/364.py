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

class ModInverse():
    def solve(a, m):
        x, y = ExtendedGCD.solve(a, m)
        return x % m

class Problem():
    def __init__(self):
        self.mod = 100000007
        self.power_2 = None
        self.factorial = None
        self.inverse_factorial = None

    def solve(self):
        self.benchmark()
        print(self.get(1000000))

    def benchmark(self):
        assert(self.get(10) == 61632)
        assert(self.get(1000) == 47255094)

    def get(self, n):
        self.power_2 = self.__set_power_2(n)
        self.factorial = self.__set_factorial(n)
        self.inverse_factorial = self.__set_inverse_factorial(n)
        x = self.__get_occupied_boundary_seat(n, 2)
        y = self.__get_occupied_boundary_seat(n, 1)
        z = self.__get_occupied_boundary_seat(n, 0)
        return (x + 2 * y + z) % self.mod

    def __get_occupied_boundary_seat(self, n, boundary_seat):
        begin_a = 0 if (n - 3 + boundary_seat) % 2 == 0 else 1
        end_a = (n - 3 + boundary_seat) // 3

        result = 0
        for a in range(begin_a, end_a + 1, 2):
            b = (n - 3 + boundary_seat - 3 * a) // 2
            x = (self.factorial[a + b])**2 * self.factorial[a + b + 1] * self.power_2[a] * self.inverse_factorial[b]
            for i in range(1, 2 - boundary_seat + 1):
                x *= (a + i)
            result += x
        return result % self.mod

    def __set_power_2(self, n):
        d = 1
        result = [d]
        for i in range(1, n + 1):
            d = (2 * d) % self.mod
            result.append(d)
        return result

    def __set_factorial(self, n):
        d = 1
        result = [d]
        for i in range(1, n + 1):
            d = (d * i) % self.mod
            result.append(d)
        return result

    def __set_inverse_factorial(self, n):
        d = 1
        result = [d]
        for i in range(1, n + 1):
            d = (d * ModInverse.solve(i, self.mod)) % self.mod
            result.append(d)
        return result

def main():
    problem = Problem()
    problem.solve()

if __name__ == '__main__':
    sys.exit(main())
