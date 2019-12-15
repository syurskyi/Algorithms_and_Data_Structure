import itertools
import sys

class Problem():
    def solve(self):
        for n in [10, 100, 123456787654321]:
            print(n, '=>', self.get(n) % 1234567890)

    def get(self, n):
        nim_count_map = []
        d = 1
        while d <= n:
            nim_count_map.append(((n // d) + 1) // 2)
            d *= 2

        winning_position_count = 0
        for a, b, c in itertools.product(range(len(nim_count_map)), repeat=3):
            if a^b^c != 0:
                winning_position_count += nim_count_map[a] * nim_count_map[b] * nim_count_map[c]
        return winning_position_count

def main():
    problem = Problem()
    problem.solve()

if __name__ == '__main__':
    sys.exit(main())
