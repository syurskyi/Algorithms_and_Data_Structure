import sys

class Problem():
    def solve(self):
        """
        Small data set: 
            100 -> 6033
            1000 -> 5803431
        http://forum.projecteuler.net/viewtopic.php?f=50&t=1817
        """
        for perimeter_bound in [100, 1000, 10000000]:
            print(self.get_primitive_triangle_count(perimeter_bound))

    def get_primitive_triangle_count(self, perimeter_bound):
        result = 0
        non_primitive_count = [0 for _ in range(perimeter_bound + 1)]
        for perimeter in range(3, perimeter_bound + 1):
            primitive_count = self.get_triangle_count(perimeter) - non_primitive_count[perimeter]
            result += primitive_count
            for bigger_perimeter in range(perimeter * 2, perimeter_bound + 1, perimeter):
                non_primitive_count[bigger_perimeter] += primitive_count
        return result

    """
    https://oeis.org/A005044
    """
    def get_triangle_count(self, n):
        mod12 = n % 12
        if mod12 == 0:
            return n**2 // 48
        if mod12 == 1 or mod12 == 5:
            return (n**2 + 6*n - 7) // 48
        if mod12 == 2 or mod12 == 10:
            return (n**2 - 4) // 48
        if mod12 == 3:
            return (n**2 + 6*n + 21) // 48
        if mod12 == 4 or mod12 == 8:
            return (n**2 - 16) // 48
        if mod12 == 6:
            return (n**2 + 12) // 48
        if mod12 == 7 or mod12 == 11:
            return (n**2 + 6*n + 5) // 48
        if mod12 == 9:
            return (n**2 + 6*n + 9) // 48

def main():
    problem = Problem()
    problem.solve()

if __name__ == '__main__':
    sys.exit(main())
