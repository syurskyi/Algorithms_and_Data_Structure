import timeit

NUM_REPETITIONS = 100

SETUP_CODE = "from random import shuffle"

def selection_sort(lst):
    for i in range(len(lst)):
        min_index = i
        for curr_index in range(i+1, len(lst)):
            if lst[min_index] > lst[curr_index]:
                min_index = curr_index
        lst[i], lst[min_index] = lst[min_index], lst[i]

def insertion_sort(lst):
    for i in range(1, len(lst)):
        elem_selected = lst[i]

        while i > 0 and elem_selected < lst[i-1]:
            lst[i] = lst[i-1]
            i -= 1

        lst[i] = elem_selected

# First test case - Selection Sort

test_code_1 = '''

a = [i for i in range(1000)]

shuffle(a)

selection_sort(a)

'''

print("\n==> Testing Selection Sort")

time = timeit.timeit(test_code_1, setup=SETUP_CODE, number=NUM_REPETITIONS, globals=globals())

print("Total time to sort the list:", time)
print("Average time per repetition:", time/NUM_REPETITIONS)


# Second test case - Insertion Sort

test_code_2 = '''

b = [i for i in range(1000)]

shuffle(b)

insertion_sort(b)

'''

print("\n==> Testing Insertion Sort")

time = timeit.timeit(test_code_2, setup=SETUP_CODE, number=NUM_REPETITIONS, globals=globals())

print("Total time to sort the list:", time)
print("Average time per repetition:", time/NUM_REPETITIONS)
