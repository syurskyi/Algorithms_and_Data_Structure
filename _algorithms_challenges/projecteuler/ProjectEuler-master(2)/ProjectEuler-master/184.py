from fractions import Fraction
import sys

class Problem():
    def solve(self):
        for n in [105]:
            print('solution =>', n, '=>', self.get(n))

    def get(self, n):
        axis_class_count = n - 1
        count_map = self.__get_point_class_count_map(n)
        quadrant_total_count = sum(count_map.values())
        print('quadrant_total_count =>', quadrant_total_count)
        print('count_map size =>', len(count_map))

        point_class_list = sorted(list(count_map.keys()))
        point_class_list_len = len(point_class_list)

        quadrant_accumulated_count = [0]
        accumulated = 0
        for key in point_class_list:
            accumulated += count_map[key]
            quadrant_accumulated_count.append(accumulated)

        total_count = (2 * axis_class_count + quadrant_total_count) * axis_class_count * quadrant_total_count
        for i in range(point_class_list_len):
            if i % 10 == 0:
                print(i, '=>', total_count)
            c = count_map[point_class_list[i]]
            f = axis_class_count * (4 * quadrant_total_count + 3 * quadrant_accumulated_count[i] \
                    - 2 * count_map[point_class_list[i]] + 2 * axis_class_count) \
                    + quadrant_total_count * quadrant_accumulated_count[i]
            total_count += c * f
            for j in range(0, i + 1):
                c = count_map[point_class_list[i]] * count_map[point_class_list[j]]
                f = quadrant_accumulated_count[i] + axis_class_count + quadrant_accumulated_count[j]
                total_count += c * f
            for j in range(i + 1, point_class_list_len):
                c = count_map[point_class_list[i]] * count_map[point_class_list[j]]
                f = 2 * quadrant_total_count + 2 * axis_class_count \
                        + 2 * quadrant_accumulated_count[j] - count_map[point_class_list[j]] \
                        + 2 * quadrant_accumulated_count[i] - 2 * quadrant_accumulated_count[i + 1] 
                total_count += c * f
        return total_count

    def __get_point_class_count_map(self, r):
        count_map = {}
        count_map[Fraction(1, 1)] = self.__get_count_on_line(1, 1, r)
        stack = [(0, 1, 1, 1)]
        while stack:
            a, b, c, d = stack.pop()
            n = a + c
            m = b + d
            if m > r or n > r:
                continue
            count = self.__get_count_on_line(n, m, r)
            if count != 0: 
                count_map[Fraction(n, m)] = count
                count_map[Fraction(m, n)] = count
            stack.append((a, b, n, m))
            stack.append((n, m, c, d))
        return count_map

    def __get_count_on_line(self, x, y, r):
        c = x**2 + y**2
        r2 = r**2
        for i in range(1, r):
            if c * i**2 >= r2:
                return i - 1
        return r - 1

def main():
    problem = Problem()
    problem.solve()

if __name__ == '__main__':
    sys.exit(main())
