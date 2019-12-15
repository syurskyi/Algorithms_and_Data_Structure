import fractions
import itertools
import sys

class Problem():
    def solve(self):
        assert(self.get(200) == 5)
        print(self.get(1000000))
    
    def get(self, bound):
        walls_map = [[] for _ in range(bound + 1)]
        sqrt_bound = self._int_sqrt(bound)
        for n in range(1, sqrt_bound + 1):
            for m in range(n + 1, sqrt_bound, 2):
                if n**2 + m**2 >= bound:
                    break
                if fractions.gcd(m, n) > 1:
                    continue
                a = m**2 - n**2
                b = 2*m*n
                c = m**2 + n**2
                for k in range(1, bound):
                    if k*c >= bound:
                        break
                    walls_map[a*k].append(b*k)
                    walls_map[b*k].append(a*k)
        rv = 0
        for walls in walls_map:
            for a, b in itertools.combinations(walls, 2):
                if (a*b) % (a+b) == 0:
                    rv += 1
        return rv

    """
    http://www.codecodex.com/wiki/Calculate_an_integer_square_root
    """
    def _int_sqrt(self, n):
        guess = (n >> n.bit_length() // 2) + 1
        result = (guess + n // guess) // 2
        while abs(result - guess) > 1:
            guess = result
            result = (guess + n // guess) // 2
        while result * result > n:
            result -= 1
        return result

def main():
    problem = Problem()
    problem.solve()

if __name__ == '__main__':
    sys.exit(main())
