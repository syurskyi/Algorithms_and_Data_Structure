import time
import random
from demos import quicksort, mergesort, bubblesort

def create_random_list(size, max_val):
    ran_list = []
    for num in range(size):
        ran_list.append(random.randint(1,max_val))
    return ran_list

# For those of you who are familiar with list comprehension covered
# in section 3, the code in the function above can be written as below:

# def create_random_list(size, max_val):
#     return [random.randint(1,max_val) for num in range(size)]

def analyze_func(func_name, arr):
    tic = time.time()
    func_name(arr)
    toc = time.time()
    seconds = toc-tic
    print(f"{func_name.__name__.capitalize()}\t-> Elapsed time: {seconds}")

size = int(input("What size list do you want to create? "))
max = int(input("What is the max value of the range? "))

l = create_random_list(size,max)
analyze_func(bubblesort, l.copy())
analyze_func(quicksort, l)
analyze_func(mergesort, l)
