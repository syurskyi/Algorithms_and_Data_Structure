import sys

class Sequence():
    def __init__(self, number_list, k, mod):
        self.number_list = [number % k for number in number_list]
        self.k = k
        self.mod = mod
        self.one_map = self.__init_one_map()

    def __init_one_map(self):
        one_map = {}
        for number in self.number_list:
            one_map[number] = 1
        return one_map

    def count(self, n):
        if n == 1:
            return self.one_map
        half_count_map = self.count(n // 2)
        count_map = self.__merge(half_count_map, half_count_map)
        if n % 2 == 1:
            count_map = self.__merge(count_map, self.one_map)
        print('current n =>', n)
        return count_map

    def __merge(self, left_count_map, right_count_map):
        result = {}
        for left_key in left_count_map:
            left_count = left_count_map[left_key]
            for right_key in right_count_map:
                right_count = right_count_map[right_key]
                new_key = (left_key + right_key) % self.k
                if new_key not in result:
                    result[new_key] = 0
                result[new_key] = (result[new_key] + left_count * right_count) % self.mod
        return result

class Problem():
    def __init__(self):
        self.factorization = {
            3: [1, 3],
            4: [1, 2, 4],
            1111: [1, 11, 101, 1111],
            1234567898765: [1, 5, 41, 205, 25343, 126715, 237631, 1039063, 1188155, 5195315, 9742871, 48714355, 6022282433, 30111412165, 246913579753, 1234567898765],
        }

    def solve(self):
        #self.benchmark()
        print(self.get(1234567898765, 4321))

    def benchmark(self):
        assert(self.get(3, 4) == 4)
        assert(self.get(4, 11) == 8)
        assert(self.get(1111, 24) == 840643584)

    def get(self, n, k):
        sequence = Sequence(self.factorization[n], k, 10**9)
        return sequence.count(n)[(-n) % k]

def main():
    problem = Problem()
    problem.solve()

if __name__ == '__main__':
    sys.exit(main())
