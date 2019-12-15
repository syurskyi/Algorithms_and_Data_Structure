import sys
        
class MinimumSubTriangleProblem():        
    def __init__(self):
        self.triangle = None
        self.num_row = None
        self.acc_row_sums = None     
        
    def min_sub_triangle(self, triangular_array):
        self._init_triangle(triangular_array)
        self._init_acc_row_sums()
        min_so_far = 0
        for i in range(self.num_row):
            print(i, '=>', min_so_far)
            for j in range(i+1):
                curr_sum = 0
                for k in range(i, self.num_row):
                    curr_sum += self.acc_row_sums[k][j+k-i+1] - self.acc_row_sums[k][j]
                    min_so_far = min(min_so_far, curr_sum)
        return min_so_far
        
    def _init_triangle(self, triangular_array):
        self.triangle = []
        curr_row, curr_pos = 1, 0
        while curr_pos < len(triangular_array):
            self.triangle.append(triangular_array[curr_pos:curr_pos + curr_row])
            curr_row, curr_pos = curr_row + 1, curr_pos + curr_row
        self.num_row = curr_row - 1
    
    def _init_acc_row_sums(self):
        self.acc_row_sums = []
        for row in self.triangle:
            acc_sum = 0
            acc_row_sum = [0]
            for i in row:
                acc_sum += i
                acc_row_sum.append(acc_sum)
            self.acc_row_sums.append(acc_row_sum)

class LinearCongruentialGenerator():
    def generate(self, bound):
        t = 0
        for k in range(1, bound + 1):
            t = (615949*t + 797807) % 2**20
            yield t - 2**19
        
def main():
    problem = MinimumSubTriangleProblem()
    
    array = [
            15, 
            -14, -7, 
            20, -13, -5, 
            -3, 8, 23, -26, 
            1, -4, -5, -18, 5,
            -16, 31, 2, 9, 28, 3
    ]
    print(problem.min_sub_triangle(array))
    
    generator = LinearCongruentialGenerator()
    array = list(generator.generate(500500))
    print(problem.min_sub_triangle(array))
    
if __name__ == '__main__':
    sys.exit(main())
