import timeit

NUM_REPETITIONS = 500

SETUP_CODE = "from random import shuffle"

# Bubble Sort Algorithm Implementations

def bubble_sort(lst):
    
    n = len(lst)
    
    for i in range(n):            
        for j in range(0, n-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]

def bubble_sort_optimized(lst):
    n = len(lst)
    
    for i in range(n):
        swapped = False
            
        for j in range(0, n-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
                swapped = True
                
        if not swapped:
            break

# First test case - Small list (50 elements)

test_code_1 = '''

a = [i for i in range(50)]

shuffle(a)

bubble_sort(a)

'''

print("\n==> First test of Bubble Sort: Small List")

time = timeit.timeit(test_code_1, setup=SETUP_CODE, number=NUM_REPETITIONS, globals=globals())

print("Total time to sort the list:", time)
print("Average time per repetition:", time/NUM_REPETITIONS)


# Second test case - Small list (50 elements) OPTIMIZED VERSION

test_code_2 = '''

a = [i for i in range(50)]

shuffle(a)

bubble_sort_optimized(a)

'''

print("\n==> Second test of Bubble Sort: Small List (OPTIMIZED)")

time = timeit.timeit(test_code_2, setup=SETUP_CODE, number=NUM_REPETITIONS, globals=globals())

print("Total time to sort the list:", time)
print("Average time per repetition:", time/NUM_REPETITIONS)


# Third test case - Large list (250 elements)

test_code_3 = '''

a = [i for i in range(250)]

shuffle(a)

bubble_sort(a)

'''

print("\n==> Third test of Bubble Sort: Large List")

time = timeit.timeit(test_code_3, setup=SETUP_CODE, number=NUM_REPETITIONS, globals=globals())

print("Total time to sort the list:", time)
print("Average time per repetition:", time/NUM_REPETITIONS)


# Fourth test case - Large list (250 elements) OPTIMIZED

test_code_4 = '''

a = [i for i in range(250)]

shuffle(a)

bubble_sort_optimized(a)

'''

print("\n==> Fourth test of Bubble Sort: Large List (OPTIMIZED)")

time = timeit.timeit(test_code_4, setup=SETUP_CODE, number=NUM_REPETITIONS, globals=globals())

print("Total time to sort the list:", time)
print("Average time per repetition:", time/NUM_REPETITIONS)


