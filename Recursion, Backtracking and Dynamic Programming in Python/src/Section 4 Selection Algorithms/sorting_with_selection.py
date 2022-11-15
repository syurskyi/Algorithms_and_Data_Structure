import random


class QuickSelect:

    def __init__(self, nums):
        self.nums = nums
        self.first_index = 0
        self.last_index = len(nums) - 1

    # this is how we can do sorting
    def sort(self):

        # the result will be another list (sorted order)
        sorted_list = []

        # because we decrement the k value (k'=k-1) this is why
        # we have to use range() like that
        for i in range(1, len(self.nums) + 1):
            sorted_list.append(self.run(i))

        return sorted_list

    def run(self, k):
        return self.select(self.first_index, self.last_index, k - 1)

    def select(self, first_index, last_index, k):

        pivot_index = self.partition(first_index, last_index)

        if pivot_index < k:
            return self.select(pivot_index + 1, last_index, k)
        elif pivot_index > k:
            return self.select(first_index, pivot_index - 1, k)

        return self.nums[pivot_index]

    def partition(self, first_index, last_index):

        pivot_index = random.randint(first_index, last_index)

        self.swap(pivot_index, last_index)

        for i in range(first_index, last_index):
            if self.nums[i] > self.nums[last_index]:
                self.swap(i, first_index)
                first_index += 1

        self.swap(last_index, first_index)

        return first_index

    def swap(self, i, j):
        self.nums[i], self.nums[j] = self.nums[j], self.nums[i]


if __name__ == '__main__':
    n = [1, 0, -1, 10, 100, -100]
    quick_select = QuickSelect(n)
    print(quick_select.sort())