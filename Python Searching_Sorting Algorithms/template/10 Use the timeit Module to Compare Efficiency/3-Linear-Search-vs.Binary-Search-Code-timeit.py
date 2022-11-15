import timeit

NUM_REPETITIONS = 1000

# Linear Search Algorithm Implementation

def linear_search(lst, item):
    for i in range(len(lst)):
        if lst[i] == item:
            return i
    return -1

# Binary Search Algorithm Implementation

def binary_search(data, item):
    low = 0
    high = len(data) - 1

    while low <= high:
        middle = (low + high)//2
        if data[middle] == item:
            return middle
        elif data[middle] > item:
            high = middle - 1
        else:
            low = middle + 1
    return -1

# List

a = [i for i in range(10000)]



# Testing Linear Search to find the number 8432 in a list with 10,000 elements

test_code_1 = '''

linear_search(a, 8432)

'''

print("\n==> Testing Linear Search")

time = timeit.timeit(test_code_1, number=NUM_REPETITIONS, globals=globals())

print("Total time to find the element:", time)
print("Average time per repetition:", time/NUM_REPETITIONS)



# Testing Binary Search to find the number 8432 in a list with 10,000 elements

test_code_2 = '''

binary_search(a, 8432)

'''

print("\n==> Testing Binary Search")

time = timeit.timeit(test_code_2, number=NUM_REPETITIONS, globals=globals())

print("Total time to find the element:", time)
print("Average time per repetition:", time/NUM_REPETITIONS)


