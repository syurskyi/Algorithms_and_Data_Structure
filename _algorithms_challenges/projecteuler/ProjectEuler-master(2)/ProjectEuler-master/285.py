import math
import sys

class Problem():
    def solve(self):
        print(self.get_expected_value(10))
        print(self.get_expected_value(100000))

    def get_expected_value(self, k_bound):
        result = 0.0
        for k in range(1, k_bound + 1):
            area = self.get_area(k)
            result += k * area
        return result

    def get_area(self, k):
        internal_circle_area = self.__get_internal_circle_area(k)
        external_circle_area = self.__get_external_circle_area(k)
        constant_area = self.__get_constant_area(k)
        return external_circle_area - internal_circle_area - constant_area

    def __get_constant_area(self, k):
        if k == 1:
            return math.sqrt(5)/2 - 1
        x_begin = math.sqrt(4 * k**2 - 4 * k - 3) / (2 * k)
        x_end = math.sqrt(4 * k**2 + 4 * k - 3) / (2 * k)
        return (x_end - x_begin) / k

    def __get_internal_circle_area(self, k):
        if k == 1:
            return 0.0
        x_begin = 1 / k
        x_end = math.sqrt(4 * k**2 - 4 * k - 3) / (2 * k)
        d = 1 - 1 / (2 * k)
        return self.__get_sqrt_integral(d , x_begin, x_end)

    def __get_external_circle_area(self, k):
        x_begin = 1 / k
        x_end = math.sqrt(4 * k**2 + 4 * k - 3) / (2 * k)
        d = 1 + 1 / (2 * k)
        return self.__get_sqrt_integral(d, x_begin, x_end) 

    def __get_sqrt_integral(self, d, x_begin, x_end):
        return self.__get_value(d, x_end) - self.__get_value(d, x_begin)

    def __get_value(self, d, x):
        return x / 2 * math.sqrt(d**2 - x**2) + d**2 / 2 * math.atan(x / math.sqrt(d**2 - x**2))

def main():
    problem = Problem()
    problem.solve()

if __name__ == '__main__':
    sys.exit(main())
