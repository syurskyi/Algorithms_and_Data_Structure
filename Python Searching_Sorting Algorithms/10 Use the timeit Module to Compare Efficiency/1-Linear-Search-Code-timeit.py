import timeit

NUM_REPETITIONS = 1000

# Linear Search Algorithm Implementation

def linear_search(lst, item):
    for i in range(len(lst)):
        if lst[i] == item:
            return i
    return -1

# List
a = [i for i in range(10000)]


# First Test - Finding an element at the beginning of the list

test_code_1 = '''

linear_search(a, 50)

'''

print("\n==> First test of Linear Search: Beginning")

time = timeit.timeit(test_code_1, number=NUM_REPETITIONS, globals=globals())

print("Total time to find the element:", time)
print("Average time per repetition:", time/NUM_REPETITIONS)


# Second Test - Finding an element in the middle of the list

test_code_2 = '''

linear_search(a, 4500)

'''

print("\n==> Second test of Linear Search: Middle")

time = timeit.timeit(test_code_2, number=NUM_REPETITIONS, globals=globals())

print("Total time to find the element:", time)
print("Average time per repetition:", time/NUM_REPETITIONS)


# Third Test - Finding an element at the end of the list

test_code_3 = '''

linear_search(a, 9999)

'''

print("\n==> Third test of Linear Search: End")

time = timeit.timeit(test_code_3, number=NUM_REPETITIONS, globals=globals())

print("Total time to find the element:", time)
print("Average time per repetition:", time/NUM_REPETITIONS)


