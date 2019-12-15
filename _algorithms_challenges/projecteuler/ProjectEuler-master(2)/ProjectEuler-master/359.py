import itertools
import sys

class HilbertNewHotel():
    def P(self, f, r):
        r1 = f**2 // 2 if f > 1 else 1
        if r == 1:
            return r1
        
        x = self._int_sqrt(2 * r1 + 1)
        if x**2 < 2 * r1 + 1:
            x += 1
        r2 = x**2 - r1
        if r == 2:
            return r2

        if r % 2 == 0:
            n = (r // 2) - 1
            S = n * (2*x + 2*n + 1)
            return S + r2
        else:
            n = (r // 2)
            S = n * (2*x + 2*n - 1)
            return S + r1

    def benchmark(self, bound):
        hotel = self._build(bound)
        for floor in hotel:
            print(floor)

    def _build(self, bound):
        hotel = []
        square_set = set([i**2 for i in range(1, 2 * bound)])
        for n in range(1, bound + 1):
            found = False
            for floor in hotel:
                m = floor[-1]
                if (n + m) in square_set:
                    floor.append(n)
                    found = True
                    break
            if not found:
                hotel.append([n])
        return hotel

    def _int_sqrt(self, n):
        guess = (n >> n.bit_length() // 2) + 1
        result = (guess + n // guess) // 2
        while abs(result - guess) > 1:
            guess = result
            result = (guess + n // guess) // 2
        while result * result > n:
            result -= 1
        return result

class Problem():
    def solve(self):
        self.sanity_check()
        print(self.get({2: 27, 3: 12}))

    def sanity_check(self):
        hotel = HilbertNewHotel()
        assert(hotel.P(1, 1) == 1)
        assert(hotel.P(1, 2) == 3)
        assert(hotel.P(2, 1) == 2)
        assert(hotel.P(10, 20) == 440)
        assert(hotel.P(25, 75) == 4863)
        assert(hotel.P(99, 100) == 19454)

    def get(self, factorization):
        rv = 0
        divisors = self.get_all_divisors(factorization)
        N = divisors[-1]
        hotel = HilbertNewHotel()
        for f in divisors:
            r = N // f
            rv += hotel.P(f, r)
        return rv % 10**8

    def get_all_divisors(self, f):
        unpacking = [[p**e for e in range(f[p] + 1)] for p in f]
        return sorted([self._product(divisor) for divisor in itertools.product(*unpacking)])

    def _product(self, sequence):
        rv = 1
        for number in sequence:
            rv *= number
        return rv

def main():
    problem = Problem()
    problem.solve()

if __name__ == '__main__':
    sys.exit(main())
