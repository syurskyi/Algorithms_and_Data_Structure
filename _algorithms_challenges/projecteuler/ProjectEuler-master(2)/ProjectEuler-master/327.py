import sys

class Problem():
    def solve(self):
        for capacity, room in [(3, 3), (3, 6), (4, 6)]:
            print(capacity, room, '=>', self.get(capacity, room))
        for capacity_begin, capacity_end, room in [(3, 4, 6), (3, 10, 10), (3, 40, 30)]:
            print((capacity_begin, capacity_end), room, '=>', self.get_sum(capacity_begin, capacity_end, room))

    def get_sum(self, capacity_begin, capacity_end, room):
        result = 0
        for capacity in range(capacity_begin, capacity_end + 1):
            result += self.get(capacity, room)
        return result

    def get(self, capacity, room):
        if capacity > room:
            return room + 1
        # In x-th room we need y = |capacity| cards to go through all the rest rooms.
        x = room - capacity + 1
        y = capacity
        # Backtracking
        q = capacity - 2
        for i in range(x):
            k, r = self.__get_k_r_pair(capacity, y, q)
            y = capacity * k + r
        return y

    def __get_k_r_pair(self, capacity, y, q):
        for r in range(capacity, 0, -1):
            a, b = divmod(y - r + 1, q)
            if b == 0:
                return a, r

def main():
    problem = Problem()
    problem.solve()

if __name__ == '__main__':
    sys.exit(main())
