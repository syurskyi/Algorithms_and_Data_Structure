import bisect
import math
import sys

class Problem():
    def solve(self):
        for n in [29, 100000]:
            print(n, '=>', self.get(n))

    def get(self, n):
        nim = self.__get_nim_value_list(n)
        nim_pos_map = {}
        for pos in range(n + 1):
            value = nim[pos]
            if value not in nim_pos_map:
                nim_pos_map[value] = []
            nim_pos_map[value].append(pos)

        count = 0
        for a in nim_pos_map:
            for b in nim_pos_map:
                c = a^b
                if c not in nim_pos_map:
                    continue
                a_pos_list = nim_pos_map[a]
                b_pos_list = nim_pos_map[b]
                c_pos_list = nim_pos_map[c]
                for b_pos in b_pos_list:
                    x = bisect.bisect(a_pos_list, b_pos)
                    y = len(c_pos_list) - bisect.bisect_left(c_pos_list, b_pos)
                    count += x * y
        return count

    def __get_nim_value_list(self, n):
        value_list = [0 for i in range(n + 1)]
        square_bound = int(math.sqrt(n))
        assert(square_bound**2 <= n and (square_bound + 1)**2 > n)
        
        square_list = [i**2 for i in range(square_bound + 2)]
        for i in range(1, square_bound + 1):
            j_begin, j_end = square_list[i], min(n, square_list[i + 1] - 1)
            for j in range(j_begin, j_end + 1):
                r_list = set()
                for k in range(1, i + 1):
                    r_list.add(value_list[j - square_list[k]])
                value_list[j] = self.__get_mex(r_list)
        return value_list

    def __get_mex(self, r_list):
        for i in range(len(r_list) + 1):
            if i not in r_list:
                return i

def main():
    problem = Problem()
    problem.solve()

if __name__ == '__main__':
    sys.exit(main())
