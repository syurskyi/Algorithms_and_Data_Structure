
class SubsetSumProblem:

    def __init__(self, nums, m):
        self.nums = nums
        self.m = m
        self.S = [[False for _ in range(m+1)] for _ in range(len(nums)+1)]

    def solve(self):

        # initialize the first row and first column
        for i in range(len(self.nums) + 1):
            self.S[i][0] = True

        # we have to construct the table with the cells one by one
        for i in range(1, len(self.nums) + 1):
            for j in range(1, self.m + 1):
                if j < self.nums[i-1]:
                    self.S[i][j] = self.S[i-1][j]
                else:
                    if self.S[i - 1][j]:
                        # this is when we do NOT include the given item rowIndex
                        self.S[i][j] = self.S[i - 1][j]
                    else:
                        # do include the item i
                        self.S[i][j] = self.S[i - 1][j - self.nums[i - 1]]

    def show_result(self):

        print("The problem is feasible: %s" % self.S[len(self.nums)][self.m])

        if not self.S[len(self.nums)][self.m]:
            return

        # print out the items in the subset
        col_index = self.m
        row_index = len(self.nums)

        while col_index > 0 or row_index > 0:
            if self.S[row_index][col_index] == self.S[row_index - 1][col_index]:
                row_index = row_index - 1
            else:
                print('We take item: %d' % self.nums[row_index - 1])
                col_index = col_index - self.nums[row_index - 1]
                row_index = row_index - 1


if __name__ == '__main__':

    M = 11
    n = [1, 2, 5, 3]

    problem = SubsetSumProblem(n, M)
    problem.solve()
    problem.show_result()
