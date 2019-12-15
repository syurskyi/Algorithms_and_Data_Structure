import sys

class Problem():
    def __init__(self):
        self.one_map = self.__init_one_map()
        self.mod = 10**9

    def solve(self):
        for n in [9, 42, 11**12]:
            print(n, '=>', self.get(n))

    def get(self, n):
        count_map = self.count(n)
        if 0 in count_map[23]:
            return count_map[23][0]
        else:
            return 0

    def count(self, n):
        if n == 1:
            return self.one_map
        else:
            half_count_map = self.count(n // 2)
            count_map = self.__merge(half_count_map, half_count_map, pow(10, n // 2, 23))
            if n % 2 == 1:
                count_map = self.__merge(count_map, self.one_map, 10)
            print('current n =>', n)
            return count_map
            
    def __init_one_map(self):
        one_map = [{} for _ in range(23 + 1)]
        for digit in range(10):
            digit_sum = digit
            one_map[digit][digit] = 1
        return one_map

    def __merge(self, left_count_map, right_count_map, delta):
        result = [{} for _ in range(23 + 1)]
        for i in range(23 + 1):
            for j in range(23 - i + 1):
                left = left_count_map[i]
                right = right_count_map[j]
                for left_key in left:
                    left_count = left[left_key]
                    for right_key in right:
                        right_count = right[right_key]
                        key = (left_key * delta + right_key) % 23
                        if key not in result[i + j]:
                            result[i + j][key] = 0
                        result[i + j][key] = (result[i + j][key] + left_count * right_count) % self.mod
        return result

def main():
    problem = Problem()
    problem.solve()

if __name__ == '__main__':
    sys.exit(main())
