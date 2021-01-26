import random


class QuickSelect:

    def __init__(self, nums):
        self.nums = nums
        self.first_index = 0
        self.last_index = len(nums) - 1

    def run(self, k):
        return self.select(self.first_index, self.last_index, k-1)

    # PARTITION PHASE
    def partition(self, first_index, last_index):

        # generate a random value within the range [first, last]
        pivot_index = random.randint(first_index, last_index)

        self.swap(pivot_index, last_index)

        for i in range(first_index, last_index):
            if self.nums[i] > self.nums[last_index]:
                self.swap(i, first_index)
                first_index += 1

        self.swap(first_index, last_index)

        # it is the index of the pivot
        return first_index

    def swap(self, i, j):
        self.nums[i], self.nums[j] = self.nums[j], self.nums[i]

    # THIS IS THE SELECTION PHASE
    def select(self, first_index, last_index, k):

        pivot_index = self.partition(first_index, last_index)

        # selection phase when we compare the pivot_index with k
        if pivot_index < k:
            # we have to discard the left sub-array and keep
            # considering the items on the right
            return self.select(pivot_index + 1, last_index, k)
        elif pivot_index > k:
            # we have to discard the right sub-array
            return self.select(first_index, pivot_index - 1, k)

        # we have found the item we are looking for
        return self.nums[pivot_index]


x = [1, 2, -5, 10, 100, -7, 3, 4]
select = QuickSelect(x)
print(select.run(2))

