import sys

class TowerOfHanoi():
    def __init__(self):
        self.movement = []

    def simulate(self, n):
        a, b, c = 0, 1, 2
        self.__move_tower(n, a, c, b)
        return self.__statistics(a, b, c)

    def __move_tower(self, height, from_peg, to_peg, with_peg):
        if height >= 1:
            self.__move_tower(height - 1, from_peg, with_peg, to_peg)
            self.__move_disk(from_peg, to_peg)
            self.__move_tower(height - 1, with_peg, to_peg, from_peg)

    def __move_disk(self, from_peg, to_peg):
        self.movement.append((from_peg, to_peg))

    def __statistics(self, a, b, c):
        stat = {}
        movement_count = len(self.movement)
        for i in range(movement_count - 1):
            curr_from_peg, curr_to_peg = self.movement[i]
            next_from_peg, next_to_peg = self.movement[i + 1]
            for curr_movement in [(curr_from_peg, curr_to_peg), (curr_to_peg, next_from_peg)]:
                if curr_movement not in stat:
                    stat[curr_movement] = 0
                stat[curr_movement] += 1
        curr_movement = self.movement[movement_count - 1]
        if curr_movement not in stat:
            stat[curr_movement] = 0
        stat[curr_movement] += 1
        return self.__merge_statistics(stat, a, b, c)

    def __merge_statistics(self, stat, a, b, c):
        if (a, b) in stat and (b, c) in stat and stat[(a, b)] == stat[(b, c)]:
            if (a, c) not in stat:
                stat[(a, c)] = 0
            stat[(a, c)] += stat[(a, b)]
            stat.pop((a, b), None)
            stat.pop((b, c), None)
        if (c, b) in stat and (b, a) in stat and stat[(c, b)] == stat[(b, a)]:
            if (c, a) not in stat:
                stat[(c, a)] = 0
            stat[(c, a)] += stat[(c, b)]
            stat.pop((c, b), None)
            stat.pop((b, a), None)
        return stat        

class Problem():
    def __init__(self):
        self.mod = 10**9

    def solve(self):
        #self.benchmark()
        print(self.get())

    def get(self):
        total_expected_number = 0
        prev_g, curr_g = 0, 1
        k, a, b, c = 10, 3, 6, 9
        for n in range(1, 10000 + 1):
            expected_number = (2 * curr_g * (c - a) * (k - 1) - (2 * k - b - c) * (c - b)) % self.mod
            total_expected_number = (total_expected_number + expected_number) % self.mod
            prev_g, curr_g = curr_g, (curr_g + 2 * prev_g + 1) % self.mod
            k = (k * 10) % self.mod
            a = (a * 3) % self.mod
            b = (b * 6) % self.mod
            c = (c * 9) % self.mod
        return total_expected_number

    def benchmark(self):
        for n in range(1, 10 + 1):
            print(n, '=>', TowerOfHanoi().simulate(n))
        assert(self.get_expected_number(2, 5, 1, 3, 5) == 60)
        assert(self.get_expected_number(3, 20, 4, 9, 17) == 2358)

    def get_expected_number(self, n, k, a, b, c):
        g = (2**(n + 2) - 3 - (-1)**n) // 6
        return 2 * g * (c - a) * (k - 1) - (2 * k - b - c) * (c - b)

def main():
    problem = Problem()
    problem.solve()

if __name__ == '__main__':
    sys.exit(main())
