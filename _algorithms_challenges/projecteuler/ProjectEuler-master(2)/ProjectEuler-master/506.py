import sys

class ClockSequence():
    def __init__(self):
        self.base_part = None
        self.base_part_sum = None
        self.incremental_part = None
        self.incremental_part_sum = None
        self.__init_parts()

    def get_sum(self, n):
        mod = 123454321
        inverse = 96007682
        q, r = divmod(n, 15)
        x = sum(self.base_part[:r]) % mod
        y = sum(self.incremental_part[:r]) % mod
        z = (pow(1000000, q, mod) - 1) * inverse * self.base_part_sum
        w = ((pow(1000000, q, mod) - 1) * inverse - q) * inverse * self.incremental_part_sum
        s = pow(1000000, q, mod) * x + (pow(1000000, q, mod) - 1) * inverse * y
        t = (z + w) % mod
        return (s + t) % mod
        
    def get_sum_naive(self, n):
        result = 0
        primitive_sequence = [1, 2, 3, 4, 3, 2]
        pos = 0
        for i in range(1, n + 1):
            value_list = []
            value_sum = 0
            while value_sum < i:
                value_list.append(primitive_sequence[pos])
                value_sum += primitive_sequence[pos]
                pos = (pos + 1) % 6
            result = (result + self.__get_rep(value_list)) % 123454321
        return result

    def __init_parts(self):
        primitive_sequence = [1, 2, 3, 4, 3, 2]
        sequence = []
        pos = 0
        for i in range(1, 30 + 1):
            value_list = []
            value_sum = 0
            while value_sum < i:
                value_list.append(primitive_sequence[pos])
                value_sum += primitive_sequence[pos]
                pos = (pos + 1) % 6
            sequence.append(self.__get_rep(value_list))
        self.base_part = list(sequence[:15])
        self.base_part_sum = sum(self.base_part)
        self.incremental_part = [sequence[i] % 1000000 for i in range(15, 30)]
        self.incremental_part_sum = sum(self.incremental_part)
        
    def __get_rep(self, value_list):
        return int(''.join(map(str, value_list)))

class Problem():
    def solve(self):
        clock_sequence = ClockSequence()
        for n in [11, 1000, 10**14]:
            print(n, '=>', clock_sequence.get_sum(n))

def main():
    problem = Problem()
    problem.solve()

if __name__ == '__main__':
    sys.exit(main())
