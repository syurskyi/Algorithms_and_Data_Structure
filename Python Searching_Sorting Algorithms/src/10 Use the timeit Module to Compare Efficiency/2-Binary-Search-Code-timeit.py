import timeit

NUM_REPETITIONS = 10000

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



# First Test - Finding an element at the beginning of the list

test_code_1 = '''

binary_search(a, 50)

'''

print("\n==> First test of Binary Search: Beginning")

time = timeit.timeit(test_code_1, number=NUM_REPETITIONS, globals=globals())

print("Total time to find the element:", time)
print("Average time per repetition:", time/NUM_REPETITIONS)



# Second Test - Finding an element in the middle of the list

test_code_2 = '''

binary_search(a, 4500)

'''

print("\n==> Second test of Binary Search: Middle")

time = timeit.timeit(test_code_2, number=NUM_REPETITIONS, globals=globals())

print("Total time to find the element:", time)
print("Average time per repetition:", time/NUM_REPETITIONS)



# Third Test - Finding an element at the end of the list

test_code_3 = '''

binary_search(a, 9999)

'''

print("\n==> Third test of Binary Search: End")

time = timeit.timeit(test_code_3, number=NUM_REPETITIONS, globals=globals())

print("Total time to find the element:", time)
print("Average time per repetition:", time/NUM_REPETITIONS)


