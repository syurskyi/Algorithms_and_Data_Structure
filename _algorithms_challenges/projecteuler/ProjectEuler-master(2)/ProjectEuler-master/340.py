import sys

class CrazyFunction():
    def get(self, n, a, b, c):
        if n > b:
            return n - c
        delta = 1 - 4*a + 3*c
        delta_pos, in_delta_pos = divmod(b - n, a) 
        return b - c + 1 - (delta_pos + 1) * delta - in_delta_pos - (a - 1) * delta_pos

    def get_sum(self, a, b, c):
        good_part_count = (b + 1) // a
        good_part_delta = self.get(b - a, a, b, c) - self.get(b, a, b, c)

        good_begin_pos = b - a + 1
        good_end_pos = b
        good_begin_value = self.get(good_begin_pos, a, b, c)
        good_end_value = self.get(good_end_pos, a, b, c)
        good_part_sum = (good_begin_value + good_end_value) * a // 2
        good_sum = (2 * good_part_sum + good_part_delta * (good_part_count - 1) * a) * good_part_count // 2

        rest_begin_pos = 0
        rest_end_pos = b - a * good_part_count
        rest_begin_value = self.get(rest_begin_pos, a, b, c)
        rest_end_value = self.get(rest_end_pos, a, b, c)
        rest_sum = (rest_begin_value + rest_end_value) * (rest_end_pos - rest_begin_pos + 1) // 2

        return rest_sum + good_sum

class Problem():
    def solve(self):
        self.sanity_check()
        self.get()

    def get(self):
        function = CrazyFunction()
        result = function.get_sum(21**7, 7**21, 12**7)
        print(result, result % 10**9)

    def sanity_check(self):
        function = CrazyFunction()
        assert(function.get(0, 50, 2000, 40) == 3240)
        assert(function.get(2000, 50, 2000, 40) == 2040)
        assert(function.get_sum(50, 2000, 40) == 5204240)

def main():
    problem = Problem()
    problem.solve()

if __name__ == '__main__':
    sys.exit(main())
